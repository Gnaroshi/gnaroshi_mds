# 작업별 지침

[AGENTS.md](AGENTS.md)와 대상 프로젝트의 `AGENTS.md`를 읽고, 아래에서 현재 작업에 해당하는 문서만 선택한다. 문서 안의 추가 링크도 명시된 작업 조건에 맞을 때 읽는다. 대상 프로젝트의 구조·명령·구현 상태는 그 저장소에서 확인한다.

| 작업 | 읽을 문서 |
| --- | --- |
| 논문 조사·읽기·재현, 학습·평가, 연구 주제, 원고 검토 | [research](guides/research.md) |
| 학생 과제의 문제풀이·제출 코드 채점 | [assignment-grading](guides/assignment-grading.md) |
| Native·desktop·CLI·로컬 도구 개발 | [application](guides/application.md) |
| 웹 UI·API·공개 데이터·웹 배포 | [web-application](guides/web-application.md) |
| UI 설계·구현·검증 | [ui-ux](guides/ui-ux.md) |
| Markdown·수식·미디어 편집기 구현 | [authoring-editor](guides/authoring-editor.md) |
| Gnaroshi 앱 간 연동 | [app-integration](guides/app-integration.md) |
| 여러 저장소의 계약 변경 또는 단일 저장소의 주요 구조·공개 계약·마이그레이션 변경 | [cross-repo-changes](guides/cross-repo-changes.md) |
| 앱 서명·패키징·버전·설치·업데이트 | [app-distribution](guides/app-distribution.md) |
| 이미지 제작·스크린샷 | [image-assets](guides/image-assets.md) |
| 앱·웹 identity, 기능·메뉴바 아이콘 | [image-assets](guides/image-assets.md), [app-icons](guides/app-icons.md), [현재 asset 목록](identity/README.md) |
| 논문·연구 figure | [공통 규칙](guides/research-figures.md) → 제작 방식에 따라 [기술 도식·plot](guides/technical-figure-code.md) 또는 [생성 일러스트](guides/scientific-figure-generation.md) |
| 지침 문서 추가·이동·정리 | [문서 유지](AGENTS.md#문서-유지). 외부 방식 비교는 [조사 근거](references/guidance-sources.md) |
| 외부 디자인 기준 비교·갱신 | [출처와 적용 판단](references/design-sources.md) |

## 경로

| 경로 | 보관 내용 |
| --- | --- |
| `AGENTS.md` | 공통 작업 경계와 문서 유지 규칙 |
| `guides/` | 작업별 실행·구현·검증 규칙 |
| `references/` | 외부 기준의 출처와 적용 판단 |
| `identity/` | 원본·후보·승인 asset, 선택 기록과 생성 도구 |
| `bootstrap/` | 다른 환경의 `AGENTS.md`에 넣을 연결 지침 |
| `mcp/` | 읽기 전용 resource server와 URI 등록표 |
| `scripts/` | 문서·MCP·asset 참조 검증 |

## 접근과 검증

- MCP 진입점: `gnaroshi://index`. 연결과 원격 파일 접근은 [mcp/README.md](mcp/README.md)를 따른다.
- 다른 환경의 연결 지침: [bootstrap/global-AGENTS.md](bootstrap/global-AGENTS.md).
- 문서 변경 검증은 [문서 유지](AGENTS.md#문서-유지)를 따른다.
