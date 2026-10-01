# Web application guidance

웹 UI·API·공개 데이터·웹 배포에 적용한다. UI 변경은 [ui-ux](ui-ux.md), 편집기 구현은 [authoring-editor](authoring-editor.md)를 함께 적용한다.

## Ownership

- presentation, canonical content, generated public data, API를 가능한 한 분리하고 각 source of truth를 문서화한다.
- public site가 private research source를 직접 import하지 않게 한다.
- generated feed는 편집 surface가 아니며 publisher와 validator를 통해 갱신한다.
- API availability가 선택적이면 no-API fallback을 보존한다.

## UI and content

- 첫 viewport에서 정체성, 목적, 핵심 경로와 다음 행동이 보여야 한다.
- long-form content는 읽기 폭과 heading hierarchy를 우선한다.
- data가 없을 때 zero-filled dashboard를 보여주지 말고 첫 유효 행동 하나를 안내한다.
- 중요한 content를 mobile에서 숨기지 않는다.
- JavaScript와 image는 설명이나 상호작용에 필요할 때만 추가한다.
- Project/application page는 실제 product screen이나 검증 artifact로 핵심 user scenario를 보여 준다. Demo fixture를 사용하면 public caption에서 demo임을 숨기지 않는다.
- Project evidence media는 sighted user와 assistive technology 모두에게 같은 provenance boundary를 제공한다. Meaningful screenshot/diagram을 `aria-hidden` link 안에만 두지 말고, concise alt와 visible caption 또는 nearby evidence text를 함께 둔다.
- Generated concept scene, diagram, screenshot, demo fixture는 public page에서 서로 다른 media type으로 드러나야 한다. Disclosure가 alt text에만 있거나 developer document에만 있으면 public disclosure로 보지 않는다.
- Language switcher는 현재 locale을 reload-only link처럼 보이게 하지 않는다. 현재 locale은 selected/inert state로 표현하고, translation unavailable 상태는 desktop과 mobile 모두에서 hover-only title이 아니라 visible text 또는 disabled/redirect explanation으로 제공한다.
- 실제 translation pair의 locale switch는 query뿐 아니라 양쪽 route에 존재하는 hash/location state도 보존한다. Translation unavailable fallback에는 존재하지 않는 detail hash를 전달하지 않는다.
- Site-owned internal href는 배포된 canonical pathname과 일치시켜 불필요한 redirect를 만들지 않는다. Collection과 page route의 trailing slash 정책을 navigation, CTA, footer와 hash URL에 동일하게 적용한다.
- Empty collection과 archive route는 화면의 empty state뿐 아니라 robots와 sitemap 노출도 content evidence와 함께 gate한다. 첫 공개 항목이 생기면 같은 규칙으로 자동 복귀해야 한다.
- Public page의 large visual은 two-second semantic test를 통과해야 하며, identity/portrait/evidence가 없을 때 큰 monogram이나 placeholder tile로 첫 viewport를 채우지 않는다.

## Research project pages

- 관련 분야의 여러 공식 project page를 실제로 열어 소개·방법·실험·영상의 순서를 비교하고, 채택·제외 판단을 대상 프로젝트에 기록한다. 한두 개 template의 외형만으로 해당 분야의 일반적인 구성이라 단정하지 않는다.
- 논문의 문제·기여·방법 설명에서 실험 근거로 이어지는 흐름을 먼저 설계한다. Overview는 상세 결과보다 앞에 두고, 중요한 ablation과 정량 표는 기본 노출하며 각 그림·영상이 검증하는 주장을 가까운 본문으로 설명한다. 큰 그림·영상에서 찾아야 할 개념과 실험 조건은 해당 자료 앞에 짧게 정의한다. 성능·일반화·데이터 효율성의 결과를 모은 뒤 ablation과 내부 분석으로 넘어가고, 감독 신호를 만드는 외부 모델의 출력은 제안 모델이 학습한 결과와 구분해 Method에 배치한다.
- 제공된 PPT나 편집 source가 있으면 합성된 완성 영상을 crop하기 전에 원본 embedded media와 animation을 확인해 우선 사용한다. 의미 있는 재생 속도·동기화·등장 순서를 보존하고, 정지 이미지나 별도 재구성으로 대체한 경우 원본 animation을 그대로 보존했다고 표현하지 않는다.
- Research project page는 문제·핵심 아이디어·개선된 행동을 먼저 전달한다. Method는 개념과 전체 흐름 중심으로 압축하고, 세부 학습 시각화는 검증하는 주장에 따라 실험·정성 분석에 배치한다. 수식 설명과 기호 사전을 늘려 첫 독자의 이해 부담을 키우지 않는다. 수식이 개념 이해에 직접 필요한 경우에만 입력·출력·연산 역할과 기호를 가까이 설명한다.
- 강조 수치와 요약은 논문의 핵심 기여를 입증하는 내용으로 고른다. 학습 비용·파라미터 증가 같은 overhead를 장점처럼 배치하지 않고, 해석에 필요한 실험 조건·비교 범위·출처는 해당 근거 옆에 짧게 남긴다. 저자 소속은 저자별로 확인하며 논문과 추가 실험의 집계 범위를 섞지 않는다.
- 연구 그림은 작은 화면에서 전체를 축소하는 것만으로 끝내지 않는다. 의미 있는 원본 panel은 순서와 label을 보존해 재배치하고 원본 확대를 제공하며, 실제 휴대폰·태블릿 폭에서 figure 내부 글자와 본문의 읽기 흐름을 확인한다.
- 섹션명, 하위 방법 단계와 설명은 의미에 맞는 heading 계층으로 구분한다. 본문·표·그림·영상은 하나의 읽기 column 경계 안에 두고, 작은 근거 이미지를 column 폭까지 무조건 늘리지 않는다. Caption은 자신이 설명하는 figure의 폭과 정렬을 따르고 배경·구분선·간격으로 본문과 구분한다.
- 같은 실험의 비교 영상과 정량 표는 한 묶음으로 인접하게 배치한다. 검증 목적이 겹치는 영상·그림은 통합하거나 task 탭으로 묶는다. 긴 페이지는 단순한 margin 축소보다 중복 목적과 분리된 근거 묶음을 먼저 줄이고, 같은 viewport의 전체 길이와 읽기 흐름을 전후 비교한다.
- 결과표는 열·행 간격과 단위 위치를 통일하며 반복되는 단위를 각 셀에 넣지 않는다. Ablation은 baseline에서 최종 방법으로 읽히게 정렬하고, 비교 방법의 학회·연도와 원 논문 링크를 확인해 제공한다.
- 영상 탭은 선택 전후 버튼·설명·표시 영역의 크기를 유지해 주변 내용이 이동하지 않게 한다. 원본의 고정 여백을 제거할 때는 전체 시간 범위에서 실제 내용을 자르지 않는지 확인하고 poster·재생·확대에 같은 표시 영역을 적용한다.
- 영상에는 재생·시간 탐색·확대 조작을 일관되게 제공한다. 함께 재생하는 영상 묶음의 control은 해당 미디어 옆에 두고 개별 control과 적용 범위를 구분하며, 주변 제목과 같은 label을 반복하지 않는다. 재생·일시정지·다시 시작·확대는 익숙한 icon과 접근 가능한 이름·tooltip으로 압축하고, 이미 클릭 가능한 그림에 동일한 확대 text link를 덧붙이지 않는다.

## Identity color

- Existing website interaction palette가 검증되어 있으면 Gnaroshi identity를 보인다는 이유만으로 전체 palette를 교체하지 않는다.
- `identity-teal`과 `identity-orange`는 favicon, compact brand mark, ownership marker와 project evidence accent처럼 제한된 identity cue에 사용한다.
- Status, focus, heatmap, chart와 semantic interaction color는 identity palette와 분리한다.
- Website mascot mark는 approved raster base의 ears, eyes, face mass와 teal/orange contrast를 유지하고 16px/32px/64px에서 검증한다.

## Responsive acceptance

- shared breakpoint와 spacing token을 사용한다.
- 작은 viewport에서 navigation, button group, table, code block, form을 실제로 검증한다.
- component는 wrap/reflow하고, 본질적으로 넓은 content는 자체 scroll container를 가진다.
- 고정 width/min-width 때문에 parent를 넘지 않게 한다.
- focus, keyboard, contrast, heading order와 reduced motion을 검증한다.
- Local in-page navigation은 populated state에서도 active item이 좁은 viewport에서 발견 가능해야 한다. Scrollbar를 숨기면 edge fade, active auto-scroll, wrapping, disclosure 같은 다른 cue를 제공한다.
- Hash-link interaction은 static build에서도 click, Enter, direct URL load, back/forward, focus 이동, sticky offset과 exactly-one-current invariant를 검증한다. Sticky header나 local nav 아래 target이 가려지면 실패다.
- Route current item이 hash navigation 뒤 non-current가 될 수 있으면 operable element semantics도 함께 전환한다. `aria-current`만 제거한 inert label을 남기지 않는다.
- Screenshot 외에 실제 link 작동, browser history, hash focus와 locale 전환을 실행해 검증한다. Empty/populated feed, translated/untranslated pair, stale/fresh data와 hover/focus/current state를 대표 fixture로 분리한다.

## Security and release

- secret은 deployment secret store에만 둔다.
- CORS, validation, rate limit, error handling을 유지한다.
- build에는 content/schema/static check를 포함한다.
- deploy provenance와 rollback 경로를 남긴다.
- 사용자에게 보이는 metric은 실제 evidence가 있을 때만 노출한다.
