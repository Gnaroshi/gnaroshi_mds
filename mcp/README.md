# Guidance 접근

## Local files / Remote-SSH

- Clone의 `README.md`와 `AGENTS.md`를 먼저 읽고 README의 작업별 목록을 따른다.
- 연결용 clone은 읽기 참조로 사용한다. 작업 전 remote와 branch·dirty state를 확인하고 clean `main`만 `git pull --ff-only origin main`으로 갱신한다. Diverged·dirty checkout을 reset하거나 덮어쓰지 않는다.
- Remote-SSH target의 `AGENTS.md`에 clone의 absolute path를 명시한다. Sibling repository가 자동 발견된다고 가정하지 않는다.
- 연결 문구는 [bootstrap/global-AGENTS.md](../bootstrap/global-AGENTS.md)를 사용한다. Markdown 접근을 위해 CLI나 MCP를 추가 설치할 필요는 없다.

## MCP 연결

[server.py](server.py)는 Python 표준 라이브러리만 사용하는 읽기 전용 STDIO server다.

```bash
codex mcp add gnaroshiGuidance -- python3 /absolute/path/to/gnaroshi_mds/mcp/server.py
```

`/absolute/path/to/gnaroshi_mds`를 실제 clone 경로로 바꾼다. 진입점은 `gnaroshi://index`와 `gnaroshi://agents`이며 작업별 선택은 index를 따른다.

## Resource 관리

- [resources.json](resources.json)이 URI·파일·description의 등록표다. 새 guide를 추가하거나 파일을 이동할 때 함께 갱신한다.
- 기존 URI는 아래처럼 유지한다. 통합된 resource는 `aliasOf`로 canonical URI를 지정하고 같은 파일을 제공한다. 새 읽기 목록에는 canonical URI를 사용하며 alias chain은 만들지 않는다.
- Resource 내용은 파일을 읽을 때 갱신된다. Server code나 initialize instruction 변경은 server process가 새로 시작된 뒤 적용된다.
- 저장소 루트에서 `python3 scripts/check_guidance.py`로 전체 resource의 실제 STDIO 응답과 문서·asset 참조를 검증한다.

| 기존 URI | 현재 대상 |
| --- | --- |
| `gnaroshi://catalog/projects` | `gnaroshi://index` → [작업별 지침](../README.md). 과거 프로젝트 snapshot은 제거했다. |
| `gnaroshi://catalog/markdown-patterns` | `gnaroshi://agents` → [문서 유지 규칙](../AGENTS.md#문서-유지) |
| `gnaroshi://guides/design-references` | [references/design-sources.md](../references/design-sources.md). URI는 그대로 유지한다. |
