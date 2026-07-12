# Project catalog

2026-07-11에 다음 두 경로의 프로젝트와 Markdown을 읽기 전용으로 조사했고, 2026-07-12에 Gnaroshi application ecosystem audit로 application 역할과 Studio integration boundary를 다시 확인했다.

- `/Users/gnaroshi/Desktop/project`
- `/Users/gnaroshi/Desktop/programming/git`

최근 commit, 프로젝트 자체 `AGENTS.md`, 제품·설계·운영 문서, 실행 가능한 README가 있는 프로젝트를 우선한다. 아래 분류는 코드의 저장 위치가 아니라 주된 사용자 가치 기준이다.

## Gnaroshi application ecosystem

Application category는 주 언어나 repository folder가 아니라 사용자가 얻는 주된 가치로 정한다. Canonical source documents가 부족한 project는 존재하지 않는 문서를 추정하지 않고 현재 확인된 source만 기록한다.

| Product name | Repository | Role | Application category | Canonical source documents | Integration with Gnaroshi Studio |
| --- | --- | --- | --- | --- | --- |
| Gnaroshi Studio | `Gnaroshi/gnaroshi-studio` | private paper·writing workflow를 조정하고 검증된 public projection을 명시적으로 publish하는 local-first authoring control plane | authoring and publishing application | `AGENTS.md`, `README.md`, `docs/app-architecture.md`, `docs/workspaces.md`, `docs/security.md`, `docs/recovery.md`, `docs/publishing.md` | ecosystem control plane이며 다른 app을 흡수하지 않고 typed provider contract로 launch, status, handoff를 조정한다 |
| PaperFlow | `Gnaroshi/paperflow` | Zotero library와 linked-local PDF를 dry-run, review, confirmation, backup/rollback 순서로 안전하게 운영한다 | research library application | `README.md`, `PaperFlowApp/README.md`, `design.md`, `PaperFlowApp/UI_UX_CHECKLIST.md` | selected Zotero/PDF reference, read-only status, launch/deep link를 제공하며 Studio는 Zotero database나 destructive command를 직접 다루지 않는다 |
| Arxiv newest paper crawler | `Gnaroshi/Arxiv-newest-paper-crawler` | 최근 arXiv paper를 발견하고 선택적으로 abstract translation과 PDF download를 수행해 local candidates로 정리한다 | research discovery application | `README.md`, `pyproject.toml` | versioned candidate export와 read-only status/typed command를 제공하고 Studio는 review된 candidate만 private queue로 import한다 |
| TR GPU Monitor | `Gnaroshi/tr-gpu-monitor` | SSH-accessible remote host의 NVIDIA GPU와 process 상태를 read-only로 관찰하고 local notification을 제공한다 | infrastructure monitoring application | `README.md` | minimal read-only status와 native detail launch를 제공하며 Studio는 SSH credential, private storage, remote job control을 소유하지 않는다 |
| RunShelf | `Gnaroshi/runshelf` | experiment run, idea, metric, lineage와 external artifact reference를 transparent local files로 보존하고 탐색한다 | research experiment application | `README.md`, `pyproject.toml`, `apps/RunShelfApp/Package.swift` | selected run/idea evidence reference와 read-only query/deep link를 제공하며 Studio는 training launch나 artifact binary copy를 수행하지 않는다 |
| ContentDeck | `Gnaroshi/content-looper` | supported media link를 playback·loop·subtitle learning workflow로 전환하고 local study state를 보존한다 | media learning application | `README.md`, `bin/README.md`, `package.json` | source/segment deep link와 explicit session export를 제공하며 Studio는 player UI, localStorage, model installation을 흡수하지 않는다 |

공통 integration rule은 [`guides/app-integration.md`](../guides/app-integration.md), multi-repository delivery rule은 [`guides/cross-repo-changes.md`](../guides/cross-repo-changes.md), shared visual family는 [`guides/app-icons.md`](../guides/app-icons.md)에 있다.

## Research

| Project | Role | Used documentation evidence |
| --- | --- | --- |
| `gnaroshi-paper-lab` | private canonical paper research source | `AGENTS.md`, `README.md`, reading/review/graph/visibility docs |
| `gnaroshi-writing` | private canonical technical writing source | `AGENTS.md`, `README.md`, content and paper-to-blog docs |
| `LAB-Lab_LVM-IP-self_study` | vision research study archive | root/week README files |
| `univ_ajou-24_1-data_mining` | data-mining research archive | `README.md` |

핵심 규칙은 [`guides/research.md`](../guides/research.md)에 있다.

## Application

| Project | Role | Used documentation evidence |
| --- | --- | --- |
| `application-gn_traveler` | SwiftUI iPhone travel application | `AGENTS.md`, MVP, screen, data, design, icon, privacy, QA, release docs |
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
