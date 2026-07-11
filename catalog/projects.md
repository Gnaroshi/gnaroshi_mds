# Project catalog

2026-07-11에 다음 두 경로의 프로젝트와 Markdown을 읽기 전용으로 조사했다.

- `/Users/gnaroshi/Desktop/project`
- `/Users/gnaroshi/Desktop/programming/git`

최근 commit, 프로젝트 자체 `AGENTS.md`, 제품·설계·운영 문서, 실행 가능한 README가 있는 프로젝트를 우선한다. 아래 분류는 코드의 저장 위치가 아니라 주된 사용자 가치 기준이다.

## Research

| Project | Role | Used documentation evidence |
| --- | --- | --- |
| `gnaroshi-paper-lab` | private canonical paper research source | `AGENTS.md`, `README.md`, reading/review/graph/visibility docs |
| `paperflow` | Zotero 정리와 연구 자료 운영 | `README.md`, `design.md`, `PaperFlowApp/UI_UX_CHECKLIST.md`, generated audit reports |
| `gnaroshi-writing` | private canonical technical writing source | `AGENTS.md`, `README.md`, content and paper-to-blog docs |
| `Arxiv-newest-paper-crawler` | arXiv 수집 utility | `README.md`, active Python project metadata |
| `LAB-Lab_LVM-IP-self_study` | vision research study archive | root/week README files |
| `univ_ajou-24_1-data_mining` | data-mining research archive | `README.md` |

핵심 규칙은 [`guides/research.md`](../guides/research.md)에 있다.

## Application

| Project | Role | Used documentation evidence |
| --- | --- | --- |
| `gnaroshi-studio` | local-first desktop authoring/publishing application | `AGENTS.md`, `README.md`, architecture/editor/publisher/security/recovery docs |
| `application-gn_traveler` | SwiftUI iPhone travel application | `AGENTS.md`, MVP, screen, data, design, icon, privacy, QA, release docs |
| `application-content_looper` | desktop media/content utility | root and binary README, Vite application metadata |
| `application-server_gpu_monitor` | local GPU monitoring application | app README |
| `application-crawler-boj_web_crawler` | BOJ crawler utility | `README.md`, Python project metadata |

핵심 규칙은 [`guides/application.md`](../guides/application.md)에 있다.

## Web application

| Project | Role | Used documentation evidence |
| --- | --- | --- |
| `gnaroshi.github.io` | public Astro website and research web application | `AGENTS.md`, product/design/architecture/import/deployment/QA docs |
| `gnaroshi-api` | Cloudflare Worker and AI API boundary | `AGENTS.md`, `README.md`, Worker API docs |
| `gnaroshi-content-feed` | validated public generated-data boundary | `AGENTS.md`, `README.md`, fixture and migration docs |
| `webpage-hushgarden` | web product prototype | `AGENTS.md`, `PLAN.md`, `README.md` |

핵심 규칙은 [`guides/web-application.md`](../guides/web-application.md)에 있다.

## Deliberately not promoted

- `*_backup`, `*-lagacy`, duplicated app folders: 참고용 snapshot이며 canonical source가 아니다.
- `practice-*`, `setting-*`, `git-settings`: 학습·환경 저장소이며 제품 문서 표준의 근거로 사용하지 않는다.
- `github-readme-stats`: 외부 프로젝트 fork의 문서를 개인 표준으로 가져오지 않는다.
- `.pytest_cache/README.md`, dependency/build output, 자동 생성 apply log: 사람이 유지하는 지침이 아니다.
- Git metadata와 의미 있는 Markdown이 모두 없는 폴더: 분류는 추정하지 않는다.
