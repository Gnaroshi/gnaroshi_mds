# gnaroshi_mds

Gnaroshi의 Codex·ChatGPT 개발 지침을 관리하는 공개 source of truth입니다.

이 저장소는 `/Users/gnaroshi/Desktop/project`와 `/Users/gnaroshi/Desktop/programming/git`에서 실제로 사용한 Markdown 문서를 조사해, 반복해서 필요한 규칙만 세 범주로 정리합니다.

- Research: 논문 수집, 읽기, 구현, 근거 기록, 공개 경계
- Application: macOS/iOS/desktop/CLI 제품과 로컬 도구
- Web application: 웹 UI, API, public feed, 배포와 운영

## Agent read order

1. [`AGENTS.md`](AGENTS.md)
2. [`catalog/projects.md`](catalog/projects.md)
3. 작업 유형에 맞는 `guides/` 문서
4. application ecosystem integration이면 [`guides/app-integration.md`](guides/app-integration.md), multi-repository change이면 [`guides/cross-repo-changes.md`](guides/cross-repo-changes.md)
5. application signing, packaging, version 또는 update 작업이면 [`guides/app-distribution.md`](guides/app-distribution.md)
6. visual identity이면 [`guides/image-assets.md`](guides/image-assets.md)와 [`guides/app-icons.md`](guides/app-icons.md)
7. 대상 프로젝트 자체의 `AGENTS.md`와 문서

프로젝트별 지침이 이 저장소의 일반 지침보다 구체적이면 프로젝트 지침을 따릅니다. 새로 확인된 재사용 가능한 선호나 작업 규칙은 이 저장소에 먼저 반영하고 GitHub에 동기화합니다. 비밀, 개인 연구 원문, 임시 로그, 프로젝트 고유 구현 세부사항은 이곳에 복사하지 않습니다.

## MCP resource server

`mcp/server.py`는 이 저장소의 Markdown을 `gnaroshi://...` URI로 제공하는 의존성 없는 STDIO MCP resource server입니다. 설치와 resource 목록은 [`mcp/README.md`](mcp/README.md)를 참고하세요.

## Identity assets

Origin, 후보와 owner-approved base는 [`identity/README.md`](identity/README.md)에 정리합니다. Full-color identity와 생성 visual은 별도 요청이 없으면 raster로 만들고, functional UI icon과 menu-bar template은 [`guides/app-icons.md`](guides/app-icons.md)의 platform rule을 따릅니다.

Application signing, Git-derived version provenance, release manifests와 source/release update channel은 [`guides/app-distribution.md`](guides/app-distribution.md)를 따릅니다.
