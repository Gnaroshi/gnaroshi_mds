# Gnaroshi canonical guidance

이 저장소는 Gnaroshi의 재사용 가능한 Codex·ChatGPT 개발 지침의 공개 source of truth다.

## 시작 순서

1. `README.md`와 `catalog/projects.md`를 읽는다.
2. 현재 작업을 research, application, web application 중 하나로 분류한다.
3. 해당 `guides/` 문서와 `guides/ui-ux.md`, 이미지 작업이면 `guides/image-assets.md`를 읽는다.
4. 대상 프로젝트의 자체 `AGENTS.md`와 문서를 더 구체적인 지침으로 적용한다.

## 업데이트 원칙

- 반복해서 사용할 새 선호, 문서 패턴, 작업 규칙이 확인되면 이 저장소를 먼저 업데이트하고 GitHub와 동기화한다.
- 비밀, credential, 개인 연구 원문, private transcript, 자동 생성 로그, 일회성 작업 기록은 이 저장소로 가져오지 않는다.
- 조사 결과 실제 사용한 문서 유형만 유지한다. 미래에 쓸 것이라는 이유만으로 빈 템플릿을 늘리지 않는다.
- 프로젝트 고유 사실은 원래 프로젝트에 남기고, 여기에는 여러 프로젝트에 적용되는 규칙만 요약한다.

## 사용자 경험

- 단순함을 우선하되 필요한 정보, 목적, 선행 조건, 작업 순서, 현재 상태와 다음 행동은 한 화면에서 파악 가능해야 한다.
- 처음 사용하는 사람도 무엇을 왜 어떤 순서로 해야 하는지 즉시 이해할 수 있어야 한다.
- 불필요한 문구, 설명을 위한 설명, 장식용 component를 넣지 않는다.
- padding과 margin은 공통 spacing token을 사용하며 임의 값과 불균형한 여백을 만들지 않는다.
- 반응형 크기에서 component, text, control이 잘리지 않게 wrap, reflow, scroll, min/max constraint를 명시하고 최소 viewport에서 검증한다.

## 이미지

- 사용자가 별도로 vector를 요청하지 않는 한 이미지 요청은 raster image 요청으로 해석한다.
- 사용자가 명시적으로 요청하지 않는 한 SVG를 포함한 vector image를 절대 생성하지 않는다.
- application/program icon의 identity reference는 `identity/reference/gnaroshi-origin-2020.jpeg`이다.
- 새 icon은 reference의 역사와 핵심 인상만 계승하고 특정 게임의 logo, UI, trademark를 복제하지 않는다.
