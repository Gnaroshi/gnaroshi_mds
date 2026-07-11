#!/usr/bin/env python3
"""Dependency-free read-only MCP resource server for gnaroshi_mds."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
RESOURCE_FILE = ROOT / "mcp" / "resources.json"
SERVER_NAME = "gnaroshi-guidance"
SERVER_VERSION = "1.0.0"
DEFAULT_PROTOCOL_VERSION = "2025-06-18"
INSTRUCTIONS = (
    "Start with gnaroshi://index, classify work as research, application, or web "
    "application, then read the matching guide plus ui-ux and image-assets when "
    "relevant. Project-local instructions are more specific. Reusable preferences "
    "belong in gnaroshi_mds; never copy secrets or private research content."
)


def load_resources() -> list[dict[str, str]]:
    return json.loads(RESOURCE_FILE.read_text(encoding="utf-8"))


def send(payload: dict[str, Any]) -> None:
    sys.stdout.write(json.dumps(payload, ensure_ascii=False, separators=(",", ":")) + "\n")
    sys.stdout.flush()


def result(request_id: Any, value: dict[str, Any]) -> None:
    send({"jsonrpc": "2.0", "id": request_id, "result": value})


def error(request_id: Any, code: int, message: str) -> None:
    send({"jsonrpc": "2.0", "id": request_id, "error": {"code": code, "message": message}})


def resource_listing() -> list[dict[str, str]]:
    fields = ("uri", "name", "title", "description")
    return [
        {**{field: item[field] for field in fields}, "mimeType": "text/markdown"}
        for item in load_resources()
    ]


def read_resource(uri: str) -> dict[str, Any]:
    item = next((entry for entry in load_resources() if entry["uri"] == uri), None)
    if item is None:
        raise KeyError(f"Unknown resource URI: {uri}")

    path = (ROOT / item["path"]).resolve()
    if ROOT not in path.parents and path != ROOT:
        raise ValueError("Resource path escapes repository root")
    return {
        "contents": [
            {
                "uri": uri,
                "mimeType": "text/markdown",
                "text": path.read_text(encoding="utf-8"),
            }
        ]
    }


def handle(message: dict[str, Any]) -> None:
    method = message.get("method")
    request_id = message.get("id")
    params = message.get("params") or {}

    if request_id is None:
        return
    if method == "initialize":
        result(
            request_id,
            {
                "protocolVersion": params.get("protocolVersion", DEFAULT_PROTOCOL_VERSION),
                "capabilities": {"resources": {"subscribe": False, "listChanged": False}},
                "serverInfo": {"name": SERVER_NAME, "version": SERVER_VERSION},
                "instructions": INSTRUCTIONS,
            },
        )
    elif method == "ping":
        result(request_id, {})
    elif method == "resources/list":
        result(request_id, {"resources": resource_listing()})
    elif method == "resources/read":
        try:
            result(request_id, read_resource(params.get("uri", "")))
        except (KeyError, OSError, ValueError) as exc:
            error(request_id, -32002, str(exc))
    elif method in {"resources/templates/list", "prompts/list", "tools/list"}:
        key = {"resources/templates/list": "resourceTemplates", "prompts/list": "prompts", "tools/list": "tools"}[method]
        result(request_id, {key: []})
    else:
        error(request_id, -32601, f"Method not found: {method}")


def main() -> None:
    for line in sys.stdin:
        try:
            message = json.loads(line)
            if isinstance(message, dict):
                handle(message)
        except json.JSONDecodeError as exc:
            error(None, -32700, f"Parse error: {exc}")
        except Exception as exc:  # keep the STDIO server alive for later requests
            error(None, -32603, f"Internal error: {exc}")


if __name__ == "__main__":
    main()
