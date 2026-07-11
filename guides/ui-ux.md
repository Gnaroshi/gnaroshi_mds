# UI/UX preferences

## Desired experience

Simple means low cognitive load, not missing information. A first-time user must be able to answer these questions immediately:

1. 이 app/program은 무엇을 위한 것인가?
2. 지금 상태는 무엇인가?
3. 먼저 무엇을 준비해야 하는가?
4. 어떤 순서로 실행해야 하는가?
5. 다음 행동과 그 결과는 무엇인가?

## Required

- 화면마다 하나의 명확한 목적과 primary action을 둔다.
- prerequisite, blocker, progress, result, next action을 같은 workflow 안에서 연결한다.
- 중요한 정보는 한 번에 scan 가능하게 하고 세부사항만 progressive disclosure한다.
- empty, loading, error, success, disabled, permission-denied state를 설계한다.
- 버튼은 결과를 예측할 수 있는 동사를 사용한다.
- destructive action은 일반 action과 분리하고 변경 범위를 표시한다.

## Avoid

- 없어도 의미가 같은 text, 반복 안내, marketing filler, 장황한 설명
- 장식만을 위한 card, badge, gradient, animation, icon
- 서로 전혀 맞지 않는 padding/margin과 임의 spacing 값
- card 안의 card, 불필요한 border와 shadow
- 작은 viewport에서 잘리는 text, button, form, table, navigation
- hover-only 정보, color-only status, 이유 없는 disabled control
- 반응형이라는 이유로 중요한 기능이나 정보를 숨기는 것

## Layout verification

- spacing token을 만들고 component 내부/사이 간격의 역할을 구분한다.
- 지원 최소 크기, 일반 크기, 넓은 크기에서 검증한다.
- 긴 번역, Dynamic Type 또는 browser zoom, 실제 content 길이를 사용한다.
- wrap과 reflow가 우선이며 data table/code처럼 필요한 경우에만 명시적 scroll을 사용한다.
- screenshot 또는 실제 runtime으로 clipping, overlap, overflow를 확인한다.
