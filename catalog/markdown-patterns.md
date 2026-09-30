# Markdown patterns actually in use

[프로젝트 조사](projects.md)에서 확인한 문서 유형이다. 대상 프로젝트의 기존 문서 중 같은 역할의 파일을 우선 사용한다.

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
