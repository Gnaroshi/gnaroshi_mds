# Gnaroshi canonical guidance

이 저장소는 Gnaroshi의 재사용 가능한 Codex·ChatGPT 개발 지침의 공개 source of truth다.

## 시작 순서

1. `README.md`와 `catalog/projects.md`를 읽는다.
2. 현재 작업을 research, application, web application 중 하나로 분류한다.
3. 해당 `guides/` 문서와 `guides/ui-ux.md`를 읽는다.
4. application integration이면 `guides/app-integration.md`, multi-repository change이면 `guides/cross-repo-changes.md`를 읽는다.
5. application signing, packaging, version 또는 update 작업이면 `guides/app-distribution.md`를 읽는다.
6. visual 작업이면 `guides/image-assets.md`와 `guides/app-icons.md`를 읽는다.
7. 대상 프로젝트의 자체 `AGENTS.md`와 문서를 더 구체적인 지침으로 적용한다.

## 업데이트 원칙

- 반복해서 사용할 새 선호, 문서 패턴, 작업 규칙이 확인되면 이 저장소를 먼저 업데이트하고 GitHub와 동기화한다.
- 비밀, credential, 개인 연구 원문, private transcript, 자동 생성 로그, 일회성 작업 기록은 이 저장소로 가져오지 않는다.
- 조사 결과 실제 사용한 문서 유형만 유지한다. 미래에 쓸 것이라는 이유만으로 빈 템플릿을 늘리지 않는다.
- 프로젝트 고유 사실은 원래 프로젝트에 남기고, 여기에는 여러 프로젝트에 적용되는 규칙만 요약한다.
- Cross-repository와 architecture change는 `guides/cross-repo-changes.md`의 baseline, preservation, compatibility, validation, rollback과 commit body를 사용한다.

## GitHub 작업 경계

- Owner가 GitHub Actions를 별도 요청 전까지 사용하지 말라고 정한 작업에서는 workflow 실행·재실행·취소·활성화·비활성화·수정뿐 아니라 run/check/log 조회와 CI 진단도 수행하지 않는다.
- 이 경계는 local inspection/build/test/signed install과 Git status/diff/commit/push, branch 및 PR의 일반 code-management metadata 작업을 막지 않는다. 다만 PR check 상태를 대신 조회하거나 CI 성공을 추정하지 않는다.
- Actions가 다시 필요하면 owner의 명시적인 요청을 받은 뒤에만 해당 workflow 범위와 허용된 action을 확인한다. 기존 workflow를 임의로 우회하거나 약화하지 않는다.
- GitHub Actions는 제한된 유료 실행 자원으로 취급한다. 가능한 build, unit/integration/contract test, lint, packaging과 signature 검증은 먼저 local에서 실행하고, Actions를 반복적인 개발·디버깅 loop나 local test 대용으로 사용하지 않는다.
- Workflow가 실패하면 허용된 범위에서 원인을 한 번 분류한다. Code/configuration failure는 같은 조건을 local에서 재현하고 수정·검증한 뒤 새 commit을 한 번 push한다. Billing, quota, runner 또는 account gate처럼 code와 무관한 failure는 workflow나 제품 code를 임의로 바꾸지 않고 외부 blocker가 해소될 때까지 추가 push와 rerun을 중단한다.
- Rerun이 필요하면 현재 PR 또는 release의 최신 relevant SHA와 실패 job만 대상으로 한다. Superseded commit의 과거 run을 일괄 재실행하지 않으며, 동일 원인 실패가 반복되면 추가 실행을 누적시키지 않는다.
- Expensive macOS packaging, signing, notarization과 release workflow는 required validation 또는 owner-approved release 시점에만 실행한다. Workflow 설계 시 안전한 path filter, concurrency cancellation, dependency cache와 job 분리를 사용하되 required check와 release integrity를 약화해 비용을 줄이지 않는다.

## 사용자 경험

- 사용자-facing 정보 경계는 safety, accessibility, data integrity 다음으로 우선하는 presentation 원칙이다. 기본 화면에는 사용자가 목적, 선행 조건, 현재 상태, 결과와 다음 행동을 이해하거나 결정하는 데 필요한 정보만 둔다. 구현 경로, raw command, PID, hash, schema/version, API/backend 이름, artifact filename, raw log처럼 개발자에게만 필요한 값과 제거해도 사용자의 판단·행동이 달라지지 않는 문구는 기본 UI에서 숨긴다.
- 문제 해결이나 호기심 때문에 일부 사용자가 볼 수 있는 기술 정보는 `Settings > Advanced/Diagnostics`, 명시적인 `Details`, Reports 또는 Logs에 progressive disclosure로 둔다. 기본값은 닫힘 또는 꺼짐이며, error 본문에는 평이한 실패 요약·보존된 것·다음 행동을 먼저 보여주고 copy 가능한 기술 원인은 세부정보 안에 둔다. 이 규칙을 이유로 안전 경고, blocker, data-loss/privacy 영향 또는 recovery action을 숨기지 않는다.
- 단순함을 우선하되 필요한 정보, 목적, 선행 조건, 작업 순서, 현재 상태와 다음 행동은 한 화면에서 파악 가능해야 한다.
- 처음 사용하는 사람도 무엇을 왜 어떤 순서로 해야 하는지 즉시 이해할 수 있어야 한다.
- 불필요한 문구, 설명을 위한 설명, 장식용 component를 넣지 않는다.
- padding과 margin은 공통 spacing token을 사용하며 임의 값과 불균형한 여백을 만들지 않는다.
- 반응형 크기에서 component, text, control이 잘리지 않게 wrap, reflow, scroll, min/max constraint를 명시하고 최소 viewport에서 검증한다.
- 모든 user action은 같은 맥락에서 pending/result/error/next action을 보여주고, feedback 때문에 기존 component가 가려지거나 불필요하게 이동하지 않게 한다. Broad UI change는 변경 component별 acceptance review 뒤 전체 workflow를 다시 검증한다.
- Packaged desktop application을 변경한 작업은 source-only 요청이 아니라면 signed stable install과 실제 Spotlight/launcher 반영까지 완료한다. 실행 중 app에 미저장 상태가 있을 수 있으면 강제 종료하지 말고 안전한 종료 뒤 같은 작업에서 설치를 재개하며, 자세한 조건은 `guides/app-distribution.md`를 따른다.
- 검증을 위해 agent가 실행한 application, local server와 provider process는 필요한 evidence를 수집한 즉시 정상 종료하고, 작업을 마치기 전에 app-owned child process, detached process와 listening port가 남지 않았는지 확인한다. 사용자가 원래 실행한 app이나 미저장 상태가 의심되는 process는 강제 종료하지 않는다.

## 이미지

- Full-color generated visual과 application/product identity는 사용자가 다른 format을 요청하지 않는 한 raster로 만든다.
- Functional UI icon은 SF Symbols, Lucide 또는 일관된 custom monochrome vector system을 사용할 수 있고 모든 toolbar control을 mascot으로 만들지 않는다.
- Menu-bar icon은 full-color mascot이 아니라 monochrome template asset을 사용한다.
- Gnaroshi application identity의 approved base는 `identity/approved/gnaroshi-base-v1.png`이며 새 role variant는 base recognition을 유지한다.
- 새 identity asset은 origin history와 핵심 인상만 계승하고 특정 게임의 logo, UI, trademark 또는 direct asset copy를 포함하지 않는다.
