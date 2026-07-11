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

## Responsive acceptance

- shared breakpoint와 spacing token을 사용한다.
- 작은 viewport에서 navigation, button group, table, code block, form을 실제로 검증한다.
- component는 wrap/reflow하고, 본질적으로 넓은 content는 자체 scroll container를 가진다.
- 고정 width/min-width 때문에 parent를 넘지 않게 한다.
- focus, keyboard, contrast, heading order와 reduced motion을 검증한다.

## Security and release

- secret은 deployment secret store에만 둔다.
- CORS, validation, rate limit, error handling을 유지한다.
- build에는 content/schema/static check를 포함한다.
- deploy provenance와 rollback 경로를 남긴다.
- 사용자에게 보이는 metric은 실제 evidence가 있을 때만 노출한다.
