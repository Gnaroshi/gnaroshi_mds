# 프로젝트 조사 목록

2026-07-11~12에 `/Users/gnaroshi/Desktop/project`와 `/Users/gnaroshi/Desktop/programming/git`에서 확인한 역할·문서 위치다. 작업 시작 시 대상 repository의 현재 문서와 구현을 다시 확인한다.

## Application

| Product / repository | 역할 | 당시 확인한 문서·entry point |
| --- | --- | --- |
| Gnaroshi Studio / `Gnaroshi/gnaroshi-studio` | 로컬 authoring·publishing과 앱 연동 | `AGENTS.md`, `README.md`, `docs/app-architecture.md`, `docs/workspaces.md`, `docs/security.md`, `docs/recovery.md`, `docs/publishing.md` |
| PaperFlow / `Gnaroshi/paperflow` | Zotero library·linked-local PDF 관리 | `README.md`, `PaperFlowApp/README.md`, `design.md`, `PaperFlowApp/UI_UX_CHECKLIST.md` |
| Arxiv Discovery / `Gnaroshi/Arxiv-newest-paper-crawler` | 논문 발견·선택적 번역·PDF 수집 | `README.md`, `pyproject.toml` |
| TR GPU Monitor / `Gnaroshi/tr-gpu-monitor` | SSH host의 GPU·process 관측 | `README.md` |
| RunShelf / `Gnaroshi/runshelf` | 실험·idea·metric·lineage·artifact reference 관리 | `README.md`, `pyproject.toml`, `apps/RunShelfApp/Package.swift` |
| ContentDeck / `Gnaroshi/content-looper` | Media·loop·subtitle 학습 | `README.md`, `bin/README.md`, `package.json` |
| `application-gn_traveler` | SwiftUI iPhone 여행 앱 | `AGENTS.md`, MVP·screen·data·design·icon·privacy·QA·release 문서 |
| `application-crawler-boj_web_crawler` | BOJ crawler | `README.md`, Python metadata |

Studio 연동의 소유권·허용 경계는 [app-integration](../guides/app-integration.md)을 따른다. 제품 역할만으로 현재 capability 구현이나 승인을 추정하지 않는다.

## Research

| Repository | 역할 | 당시 확인한 문서 |
| --- | --- | --- |
| `gnaroshi-paper-lab` | Private paper research source | `AGENTS.md`, `README.md`, reading·review·graph·visibility 문서 |
| `gnaroshi-writing` | Private technical writing source | `AGENTS.md`, `README.md`, content·paper-to-blog 문서 |
| `LAB-Lab_LVM-IP-self_study` | Vision 연구 학습 archive | Root/week README |
| `univ_ajou-24_1-data_mining` | Data-mining 학습 archive | `README.md` |

## Web application

| Repository | 역할 | 당시 확인한 문서 |
| --- | --- | --- |
| `gnaroshi.github.io` | 공개 Astro website | `AGENTS.md`, product·design·architecture·import·deployment·QA 문서 |
| `gnaroshi-api` | Cloudflare Worker·AI API | `AGENTS.md`, `README.md`, Worker API 문서 |
| `gnaroshi-content-feed` | 검증된 공개 generated data | `AGENTS.md`, `README.md`, fixture·migration 문서 |
| `webpage-hushgarden` | Web prototype | `AGENTS.md`, `PLAN.md`, `README.md` |

## 제외한 근거

- Backup·legacy·중복 app folder는 canonical source로 사용하지 않았다.
- Practice·환경 설정 저장소와 외부 fork를 제품 문서 표준의 근거로 사용하지 않았다.
- Dependency/build output·cache README·자동 apply log는 유지 지침에서 제외했다.
- Git metadata와 의미 있는 문서가 없는 폴더는 역할을 추정하지 않았다.
