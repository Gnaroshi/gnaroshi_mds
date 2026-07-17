# Web application guidance

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
- Public page의 large visual은 two-second semantic test를 통과해야 하며, identity/portrait/evidence가 없을 때 큰 monogram이나 placeholder tile로 첫 viewport를 채우지 않는다.

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
- Hash-link interaction은 static build에서도 click, Enter, direct URL load, back/forward, sticky offset, exactly-one-current invariant를 자동화한다.
- Visual regression은 route screenshot만으로 완료하지 않는다. Empty/populated feed, translated/untranslated pair, stale/fresh data, hover/focus/current states를 대표 fixture로 분리해 확인한다.

## Security and release

- secret은 deployment secret store에만 둔다.
- CORS, validation, rate limit, error handling을 유지한다.
- build에는 content/schema/static check를 포함한다.
- deploy provenance와 rollback 경로를 남긴다.
- 사용자에게 보이는 metric은 실제 evidence가 있을 때만 노출한다.
