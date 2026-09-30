#!/usr/bin/env python3
"""Check local document routing, MCP resources and identity provenance."""
from __future__ import annotations

import hashlib
import json
import re
import struct
import subprocess
import sys
from collections import deque
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r'\]\(([^\s)]+)(?:\s+"[^"]*")?\)|\b(?:src|href)="([^"]+)"')


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def headings(text: str) -> set[str]:
    slugs: set[str] = set()
    counts: dict[str, int] = {}
    fenced = False
    for line in text.splitlines():
        if line.startswith(('```', '~~~')):
            fenced = not fenced
        if fenced or not re.match(r'^#{1,6} ', line):
            continue
        name = re.sub(r'^#+\s+', '', line).strip().lower()
        name = re.sub(r'[^\w\-\s]', '', name).replace(' ', '-')
        count = counts.get(name, 0)
        counts[name] = count + 1
        slugs.add(f'{name}-{count}' if count else name)
    return slugs


def check_documents() -> tuple[int, int]:
    names = subprocess.check_output(
        ['git', 'ls-files', '--cached', '--others', '--exclude-standard', '-z', '--', '*.md'],
        cwd=ROOT, text=True,
    ).split('\0')
    documents = {
        (ROOT / name).resolve(): (ROOT / name).read_text(encoding='utf-8')
        for name in names if name and (ROOT / name).is_file()
    }
    edges: dict[Path, set[Path]] = {path: set() for path in documents}
    checked = 0
    for path, text in documents.items():
        for match in LINK.finditer(text):
            value = (match.group(1) or match.group(2)).strip('<>')
            url = urlsplit(value)
            if url.scheme or url.netloc:
                continue
            target = (path.parent / unquote(url.path)).resolve() if url.path else path
            location = f'{path.relative_to(ROOT)}:{text.count(chr(10), 0, match.start()) + 1}'
            require(target.is_relative_to(ROOT), f'{location}: outside repository: {value}')
            require(target.exists(), f'{location}: missing target: {value}')
            if target in documents:
                edges[path].add(target)
                if url.fragment:
                    require(unquote(url.fragment) in headings(documents[target]),
                            f'{location}: missing heading: {value}')
            checked += 1
    queue = deque([ROOT / 'README.md'])
    reached: set[Path] = set()
    while queue:
        path = queue.popleft()
        if path in reached:
            continue
        reached.add(path)
        queue.extend(edges.get(path, set()) - reached)
    missing = sorted(str(path.relative_to(ROOT)) for path in documents.keys() - reached)
    require(not missing, f'Documents unreachable from README: {missing}')
    return len(documents), checked


def check_mcp() -> int:
    registry = json.loads((ROOT / 'mcp/resources.json').read_text())
    for field in ('uri', 'name', 'path'):
        values = [item[field] for item in registry]
        require(len(values) == len(set(values)), f'Duplicate MCP {field}')
    paths = {item['path'] for item in registry}
    guides = {str(path.relative_to(ROOT)) for path in (ROOT / 'guides').glob('*.md')}
    require(guides <= paths, f'Unregistered guides: {sorted(guides - paths)}')
    for item in registry:
        path = (ROOT / item['path']).resolve()
        require(path.is_relative_to(ROOT) and path.is_file(), f'Invalid resource path: {item}')
        require(all(item.get(key) for key in ('uri', 'name', 'title', 'description', 'path')),
                f'Incomplete resource metadata: {item}')
    requests = [
        {'jsonrpc': '2.0', 'id': 1, 'method': 'initialize', 'params': {
            'protocolVersion': '2025-06-18', 'capabilities': {},
            'clientInfo': {'name': 'guidance-check', 'version': '1'}}},
        {'jsonrpc': '2.0', 'method': 'notifications/initialized'},
        {'jsonrpc': '2.0', 'id': 2, 'method': 'resources/list'},
    ]
    requests.extend({'jsonrpc': '2.0', 'id': index + 3, 'method': 'resources/read',
                     'params': {'uri': item['uri']}} for index, item in enumerate(registry))
    requests.append({'jsonrpc': '2.0', 'id': 999, 'method': 'resources/read',
                     'params': {'uri': 'gnaroshi://missing'}})
    result = subprocess.run([sys.executable, '-B', str(ROOT / 'mcp/server.py')],
                            input=''.join(json.dumps(x) + '\n' for x in requests),
                            text=True, capture_output=True, timeout=15, check=True)
    require(not result.stderr, f'MCP stderr: {result.stderr}')
    responses = [json.loads(line) for line in result.stdout.splitlines()]
    require(len(responses) == len(registry) + 3, 'Unexpected MCP response count')
    by_id = {item['id']: item for item in responses}
    require('resources' in by_id[1]['result']['capabilities'], 'Missing resource capability')
    listed = by_id[2]['result']['resources']
    require({item['uri'] for item in listed} == {item['uri'] for item in registry},
            'MCP listing differs from registry')
    for index, item in enumerate(registry):
        contents = by_id[index + 3]['result']['contents']
        require(len(contents) == 1 and contents[0]['uri'] == item['uri'], 'Wrong resource identity')
        require(contents[0]['text'] == (ROOT / item['path']).read_text(),
                f'Resource contents differ: {item["uri"]}')
    require(by_id[999]['error']['code'] == -32002, 'Unknown resource should be rejected')
    return len(registry)


def check_identity() -> int:
    base_dir = ROOT / 'identity/approved'
    base = json.loads((base_dir / 'metadata.json').read_text())
    master = (base_dir / 'gnaroshi-base-v1.png').read_bytes()
    require(hashlib.sha256(master).hexdigest() == base['sha256'], 'Base image hash mismatch')
    require(master == (ROOT / 'identity/candidates' / base['sourceCandidate']).read_bytes(),
            'Base image differs from selected candidate')
    app_dir = base_dir / 'apps'
    metadata = json.loads((app_dir / 'metadata.json').read_text())
    active = metadata['apps']
    historical = metadata.get('historicalAssets', [])
    require(len(active) == 6, 'Expected six approved application roles')
    require(not any(x['sourceCandidate'] == 'gnaroshi-main-p5' for x in active),
            'Abbreviated global mark must not be a production role')
    for item in historical:
        require(item['usageStatus'] == 'historical' and not item['targetPlatforms'],
                'Historical assets must have no current production targets')
    for item in active + historical:
        image = (app_dir / item['masterFile']).read_bytes()
        require(hashlib.sha256(image).hexdigest() == item['masterSha256'],
                f'Image hash mismatch: {item["masterFile"]}')
        require(image[:8] == b'\x89PNG\r\n\x1a\n', 'Expected PNG master')
        require(list(struct.unpack('>II', image[16:24])) == item['masterSize'],
                f'Image dimensions mismatch: {item["masterFile"]}')
    return len(active) + len(historical)


def main() -> None:
    document_count, link_count = check_documents()
    resource_count = check_mcp()
    asset_count = check_identity()
    print(f'PASS: {document_count} documents, {link_count} local links, '
          f'{resource_count} MCP resources, base identity and {asset_count} P5 masters')


if __name__ == '__main__':
    main()
