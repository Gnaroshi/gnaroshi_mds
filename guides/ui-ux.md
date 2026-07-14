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
- navigation 선택지가 상호 배타적이면 direct link, tab, 또는 한 번에 하나만 열리는 disclosure를 사용한다. 여러 navigation disclosure가 독립적으로 열린 채 중첩되지 않게 한다.
- 공개 evidence나 실제 기능이 없는 capability는 disabled menu나 빈 dashboard로 광고하지 않고 숨긴다. route 보존이 필요하면 direct navigation에서 제외한다.

## Avoid

- 없어도 의미가 같은 text, 반복 안내, marketing filler, 장황한 설명
- 장식만을 위한 card, badge, gradient, animation, icon
- 서로 전혀 맞지 않는 padding/margin과 임의 spacing 값
- card 안의 card, 불필요한 border와 shadow
- 작은 viewport에서 잘리는 text, button, form, table, navigation
- hover-only 정보, color-only status, 이유 없는 disabled control
- 반응형이라는 이유로 중요한 기능이나 정보를 숨기는 것

## Pixel visual layer

Owner-selected pixel direction은 content를 retro-game interface로 바꾸는 theme가 아니라 identity와 interaction chrome에 적용하는 공통 visual grammar다.

- Pixel treatment는 app/product identity, launcher tile, small role glyph, border corner, separator, focus ring, selected navigation marker와 primary control edge에 우선 적용한다.
- Body text, long-form writing, mathematical notation, code readability와 실제 product screenshot은 pixelation하지 않는다.
- Body와 prose에 bitmap font를 강제하지 않는다. 제한된 eyebrow, technical label 또는 display accent에는 system mono를 사용할 수 있지만 EN/KO legibility를 실제 크기에서 검증한다.
- Border, corner, shadow와 spacing은 2px 또는 4px step을 반복해 family grammar를 만든다. Component마다 임의의 pixel decoration을 추가하지 않는다.
- Rounded pill, soft blur shadow, glassmorphism과 pixel step을 한 component 안에서 혼합하지 않는다.
- Pixel shadow는 depth가 필요한 primary control 또는 identity tile에만 짧고 hard-edged하게 사용한다. 모든 card를 떠 있는 game inventory slot처럼 만들지 않는다.
- Actual app role은 key color와 canonical role glyph로 구분한다. 색만으로 app 또는 status를 구분하지 않고 accessible label을 유지한다.
- Light/dark mode에서 동일 geometry를 유지하고 palette와 contrast만 조정한다.
- Reduced motion, keyboard focus, zoom, long Korean copy와 minimum viewport requirements는 pixel style보다 우선한다.

## Layout verification

- spacing token을 만들고 component 내부/사이 간격의 역할을 구분한다.
- 지원 최소 크기, 일반 크기, 넓은 크기에서 검증한다.
- 긴 번역, Dynamic Type 또는 browser zoom, 실제 content 길이를 사용한다.
- wrap과 reflow가 우선이며 data table/code처럼 필요한 경우에만 명시적 scroll을 사용한다.
- screenshot 또는 실제 runtime으로 clipping, overlap, overflow를 확인한다.

## Settings and form alignment

- 설정 화면은 label/detail 영역과 control 영역의 공통 column을 정의하고 모든 row가 같은 축을 사용한다.
- picker, text field, slider, stepper처럼 값을 편집하는 control은 같은 너비와 시작 위치를 공유한다.
- boolean 값은 임의 위치의 labelled checkbox로 두지 않고 공통 control column의 같은 축에 switch로 정렬한다.
- 한 기능에 종속된 세부 control은 parent toggle 바로 아래에 두고 기능이 꺼져 있으면 숨기거나 명확히 비활성화한다.
- preview, reset, open, verify 같은 command button은 값 편집 row와 섞지 않고 별도 action 영역으로 분리한다.
- 좁은 viewport에서는 label-over-control로 reflow하되 label, 설명, control의 의미 순서를 유지한다.
- 서로 다른 section에서 같은 의미의 설정은 같은 row component와 interaction pattern을 재사용한다.
