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

## 사용자 경험

- 단순함을 우선하되 필요한 정보, 목적, 선행 조건, 작업 순서, 현재 상태와 다음 행동은 한 화면에서 파악 가능해야 한다.
- 처음 사용하는 사람도 무엇을 왜 어떤 순서로 해야 하는지 즉시 이해할 수 있어야 한다.
- 불필요한 문구, 설명을 위한 설명, 장식용 component를 넣지 않는다.
- padding과 margin은 공통 spacing token을 사용하며 임의 값과 불균형한 여백을 만들지 않는다.
- 반응형 크기에서 component, text, control이 잘리지 않게 wrap, reflow, scroll, min/max constraint를 명시하고 최소 viewport에서 검증한다.
- Packaged desktop application을 변경한 작업은 source-only 요청이 아니라면 signed stable install과 실제 Spotlight/launcher 반영까지 완료한다. 실행 중 app에 미저장 상태가 있을 수 있으면 강제 종료하지 말고 안전한 종료 뒤 같은 작업에서 설치를 재개하며, 자세한 조건은 `guides/app-distribution.md`를 따른다.

## 이미지

- Full-color generated visual과 application/product identity는 사용자가 다른 format을 요청하지 않는 한 raster로 만든다.
- Functional UI icon은 SF Symbols, Lucide 또는 일관된 custom monochrome vector system을 사용할 수 있고 모든 toolbar control을 mascot으로 만들지 않는다.
- Menu-bar icon은 full-color mascot이 아니라 monochrome template asset을 사용한다.
- Gnaroshi application identity의 approved base는 `identity/approved/gnaroshi-base-v1.png`이며 새 role variant는 base recognition을 유지한다.
- 새 identity asset은 origin history와 핵심 인상만 계승하고 특정 게임의 logo, UI, trademark 또는 direct asset copy를 포함하지 않는다.
