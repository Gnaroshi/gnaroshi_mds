# Markdown patterns actually in use

다음 문서 유형은 조사 대상 프로젝트에서 실제로 반복 사용되었다. 중앙 저장소는 이 유형만 유지하고, 필요가 확인되기 전에는 새 template category를 만들지 않는다.

| Type | Purpose | Evidence examples |
| --- | --- | --- |
| `AGENTS.md` | 경계, 금지사항, 검증 명령, agent 작업 방식 | paper lab, studio, website, API, feed, GN Traveler |
| `README.md` | 목적, source of truth, 구조, install/run, 핵심 workflow | 거의 모든 active project |
| Product/MVP | 사용자 약속, 범위, non-goal, blocker | GN Traveler `MVP_DEFINITION`, website `product` |
| Architecture/ADR | 소유권, component boundary, 기술 결정 | Studio architecture docs, website architecture, GN Traveler ADR |
| Data/content contract | schema, model, provenance, public/private boundary | paper lab, content feed, Studio, GN Traveler |
| Design/UI/UX | hierarchy, tokens, responsive rules, accessibility, state | PaperFlow `design`, website `design`, GN Traveler design and UX audits |
| Security/privacy | secret handling, local data, permissions, CORS, provider boundary | API, Studio, GN Traveler |
| Operations | setup, deployment, monitoring, release, rollback, recovery | website and Studio docs |
| Verification/audit | traceability, QA, smoke test, release readiness | GN Traveler and website reports |
| Migration | source inventory, ownership transfer, rollback | Gnaroshi repository split docs |

## Keep documents useful

- 한 문서는 하나의 안정된 질문에 답한다.
- 상태가 바뀌는 report와 장기 규칙을 한 파일에 섞지 않는다.
- 제목만 다른 중복 문서를 만들지 말고 canonical 문서를 연결한다.
- 완료된 일회성 audit는 근거가 필요할 때만 보존하고 일반 지침으로 복사하지 않는다.
- README에는 전체 세부사항을 복제하지 않고 읽기 순서와 실행 경로를 둔다.
