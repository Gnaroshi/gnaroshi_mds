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

## Interaction response contract

모든 interactive component는 실행 가능 여부뿐 아니라 사용자의 행동이 어떻게 처리됐는지 같은 맥락에서 보여준다.

- Action마다 idle, pending, success, error와 retry/next-action 상태를 정의한다. 비동기 action은 중복 실행을 막고, 진행 중 label 또는 indicator와 완료 결과를 제공한다.
- Pending label과 indicator는 control의 폭과 주변 layout을 불필요하게 바꾸지 않는다. Button content와 feedback region은 예상 가능한 최소 크기를 예약해 상태 변화 때문에 인접 control이나 작성 surface가 이동하지 않게 한다.
- Task-generated feedback은 trigger, field 또는 affected item 가까이에 둔다. Page-wide 문제만 page feedback region에 두고, 별도 작업의 message를 한 global banner에 섞지 않는다.
- Inline feedback과 page feedback region은 기존 content를 덮거나 가리지 않는다. Conditional message가 중요한 editor, list, form 또는 control을 밀어내는 경우 reserved region, replacement state 또는 명시적 transition layout을 사용한다.
- Modal alert는 data loss, irreversible action, credential/security 경계처럼 즉시 결정을 요구할 때만 사용한다. 일반 success, retry 가능한 fetch failure와 상태 정보는 current context 안에서 전달한다.
- Success가 결과 자체로 명확하면 불필요한 message를 추가하지 않는다. 결과가 offscreen이거나 canonical write, copy, import, external launch처럼 확인이 필요하면 짧고 persistent한 context feedback을 제공한다.
- Error는 무엇이 실패했는지, 보존된 것은 무엇인지, 다음 valid action을 함께 말한다. 자동 dismiss toast를 error 또는 유일한 recovery 안내로 사용하지 않는다.
- Action이 새 view, item 또는 dialog를 열면 focus와 selection을 새 context로 이동하고 돌아갈 위치를 보존한다. Screen reader에는 live region을 사용하되 같은 message를 여러 `role=alert`로 중복 발표하지 않는다.
- Async action 중 관련 input, selection과 navigation이 결과와 충돌할 수 있으면 operation scope만 잠근다. App 전체를 이유 없이 막지 않고, stale response가 새 selection을 덮지 않도록 request identity/cancellation을 적용한다.

## Information hierarchy and density

- Navigation group과 screen heading은 implementation layer가 아니라 사용자 목표와 결과를 이름으로 사용한다. 한 item만 가진 group, 모호한 container label과 raw technical noun은 grouping 이득이 없으면 합치거나 이름을 바꾼다.
- Current location, primary task와 next action은 secondary status, repository path, hash, schema/version detail보다 먼저 보여준다. Raw provenance와 diagnostic value는 사용자가 요청할 때 disclosure, Details 또는 inspector에서 보여준다.
- Spacing은 먼저 관계를 표현한다. 가까운 요소는 같은 task group, 더 큰 간격은 section boundary를 뜻한다. Divider는 scrolling region, navigation group 또는 의미가 다른 dense row처럼 공간만으로 경계가 불충분할 때 일관되게 사용한다.
- Font size는 hierarchy를 만들기 위한 유일한 수단이 아니다. Visible non-decorative caption/help는 기본 12px 이상, navigation/form/control은 보통 13–14px 이상, 긴 authoring text는 보통 15–17px에서 실제 EN/KO 가독성을 검증한다. 더 작은 text가 필요하면 정보 자체를 숨기거나 재구성할 수 없는지 먼저 검토한다.
- Typography, spacing, radius, divider와 control height는 semantic token으로 제한한다. Component마다 임의 값으로 밀도를 미세 조정하지 않는다.
- Minimum supported window에서 primary navigation label을 모두 숨겨 icon-only로 만들지 않는다. Reflow, narrower but readable label, disclosure 또는 secondary action 축소를 먼저 사용한다.

## Forms and metadata authoring

- 사용자가 identifier, URL 또는 existing record로 시작할 수 있으면 metadata lookup/import를 manual entry보다 먼저 제공한다. 자동 입력값의 source와 lookup state를 표시하고 생성·저장 전에 사용자가 검토할 수 있게 한다.
- 첫 단계는 record 생성에 정말 필요한 최소 field와 사용자 intent만 요구한다. Publication, provenance, advanced analysis와 드물게 쓰는 metadata는 record가 만들어진 뒤 progressive disclosure한다.
- 각 field는 persistent label, plain-language purpose, required/optional 상태, realistic example 또는 format hint, validation과 recovery guidance를 필요에 따라 제공한다. Placeholder만으로 label이나 instruction을 대신하지 않는다.
- Validation은 사용자가 입력하기 전부터 error를 표시하지 않는다. Submit 또는 blur 뒤 invalid field 가까이에 이유와 valid example을 제공하고, 여러 error가 있으면 summary에서 해당 field로 focus를 이동할 수 있게 한다.
- Comma-delimited string처럼 사용자가 format을 기억해야 하는 입력은 domain이 list라면 token/list editor, repeated row, autocomplete 또는 paste normalization을 우선한다. Manual raw source editing은 escape hatch로 유지할 수 있다.
- Auto-filled, user-edited, required-missing과 source-stale 상태를 구분한다. Source refresh가 user edit을 덮을 수 있으면 diff/preview 또는 explicit overwrite selection을 제공한다.
- Metadata와 long-form authoring이 경쟁하면 minimum window에서 좁은 multi-column form으로 모두 압축하지 않는다. Details mode, labeled inspector 또는 context switch로 충분한 width를 주고 authoring state와 focus를 보존한다.

## Component-level review loop

- Broad UI change는 screen 전체에 대한 vague approval 한 번으로 끝내지 않는다. Navigation, form, editor toolbar, dialog, list row, status/feedback, destructive action처럼 변경 component를 나눠 review한다.
- 각 component review는 purpose, expected action/result, idle/pending/success/error, keyboard/focus, narrow window, dark/light, content length, layout stability와 regression을 pass/fail로 기록한다.
- Reviewer가 `OK`를 주려면 blocker가 없다는 말뿐 아니라 acceptance criterion별 증거를 남겨야 한다. Fail 또는 ambiguous item은 같은 component를 수정하고 다시 review한다.
- Component들이 통과한 뒤 전체 workflow에서 hierarchy, state continuity와 cross-component feedback을 다시 검증한다. Component pass가 전체 product flow pass를 대신하지 않는다.

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

## Reference basis

이 문서는 특정 design system의 visual appearance를 복제하지 않고 다음 공식 guidance에서 반복되는 interaction 원칙을 재사용한다.

- [Apple Human Interface Guidelines: Feedback](https://developer.apple.com/design/human-interface-guidelines/feedback), [Alerts](https://developer.apple.com/design/human-interface-guidelines/alerts), [Progress indicators](https://developer.apple.com/design/human-interface-guidelines/progress-indicators), [Buttons](https://developer.apple.com/design/human-interface-guidelines/buttons)
- [Carbon Design System: Notifications](https://carbondesignsystem.com/patterns/notification-pattern/), [Spacing](https://carbondesignsystem.com/elements/spacing/overview/)
- [Primer: Forms](https://primer.style/product/ui-patterns/forms/), [Navigation](https://primer.style/product/ui-patterns/navigation/), [Notification messaging](https://primer.style/product/ui-patterns/notification-messaging/)
- [GitHub Docs writing best practices](https://docs.github.com/en/contributing/writing-for-github-docs/best-practices-for-github-docs)와 [basic Markdown writing](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
- [Zotero: Adding items and metadata by identifier](https://www.zotero.org/support/adding_items_to_zotero)
