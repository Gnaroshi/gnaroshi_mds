# Gnaroshi application identity and icon guidance

## Approved visual base

- Approved raster base: `identity/approved/gnaroshi-base-v1.png`
- Selection metadata: `identity/approved/metadata.json`
- Source candidate: `identity/candidates/07-cel-shaded.png`
- Origin reference: `identity/reference/gnaroshi-origin-2020.jpeg`

Source candidate와 approved base는 보존한다. Platform export나 role variant를 만들 때 approved base를 직접 덮어쓰지 않는다.

## Icon classes

### Full-color app and product identity

- Full-color application/product icon은 raster master에서 시작한다.
- Gnaroshi family icon은 `gnaroshi-base-v1`의 recognizable mascot, silhouette, teal/orange identity를 유지한다.
- Application role에 맞는 작은 variant element를 추가할 수 있다.
- PNG master를 보존하고 ICNS, asset catalog, Windows ICO/PNG, web PNG 등 platform requirement에 맞춰 export한다.
- Platform mask, safe area, corner treatment와 small-size optical correction은 export마다 검증한다.

### Functional UI icons

- Toolbar, navigation, status, form action에는 SF Symbols, Lucide 또는 application 안에서 일관된 custom monochrome vector icon을 사용할 수 있다.
- Functional control까지 모두 raster mascot으로 만들지 않는다.
- 한 application 안에서 stroke, fill, optical size, label treatment를 섞지 않는다.
- Essential meaning을 icon 하나에만 의존하지 않고 accessible label, text 또는 state와 함께 제공한다.
- Brand illustration과 functional icon system을 별도 layer로 유지한다.

### Menu-bar icons

- macOS menu-bar icon은 monochrome template asset을 사용한다.
- Full-color mascot, pastel fill, gradient, shadow를 menu bar에 그대로 넣지 않는다.
- Light/dark menu bar에서 system tint와 selected state를 검증한다.

## Base mascot preservation

- 큰 귀, 날카로운 눈, 넓은 얼굴/이빨, 강한 중심 silhouette와 teal/orange 대비가 즉시 인식되어야 한다.
- Role element가 얼굴, 눈, 귀 또는 주요 silhouette를 가리지 않는다.
- Role element는 전체 visual identity의 약 25% 이하를 권장한다.
- Text, watermark, franchise logo, official emblem, trademark 또는 existing game asset의 direct copy를 넣지 않는다.
- 특정 game publisher가 selected design을 소유한다고 주장하지 않는다.

## Application role family

| Product family | Identity role | Suitable secondary motif |
| --- | --- | --- |
| Gnaroshi Studio | coordination, writing, publishing, central control | 연결 ring, 작은 page/pen, controlled hub cue |
| PaperFlow | papers, organization, safe flow | layered paper, ordered path, guarded flow cue |
| Arxiv crawler | discovery, scanning, incoming papers | scan arc, incoming sheet, discovery spark |
| TR GPU Monitor | GPU, telemetry, remote status | small chip grid, telemetry line, remote status pulse |
| RunShelf | experiment runs, shelves, indexed results | shelf line, indexed block, run marker |
| ContentDeck / `content-looper` | playback, looping, subtitles, learning | loop arc, play cue, compact subtitle strip |

Secondary motif는 logo collage가 아니라 작은 role cue다. Base mascot의 pose와 expression을 무리하게 바꿔 family recognition을 잃지 않는다.

## Shared palette

Dark mode가 primary working theme이며 bright pastel은 제한된 role accent로 사용한다.

### Base dark surfaces

| Token | Recommended color | Use |
| --- | --- | --- |
| `surface-near-black` | `#11151B` | app canvas, deepest background |
| `surface-charcoal` | `#181E26` | primary panel and sidebar |
| `surface-blue-gray` | `#222B38` | raised/inset surface |
| `text-primary-dark` | `#F4F7FA` | primary text on dark surfaces |
| `text-secondary-dark` | `#B7C0CC` | secondary text after contrast verification |

Pure black을 기본 canvas로 사용하지 않는다. Surface hierarchy는 spacing과 제한된 separator를 함께 사용하고 card-within-card decoration으로 만들지 않는다.

### Shared identity colors

| Token | Recommended color | Use |
| --- | --- | --- |
| `identity-teal` | `#3FA6A0` | shared mascot/identity cue |
| `identity-orange` | `#E88945` | warm shared identity cue |

### Pastel role accents

| Accent | Recommended color |
| --- | --- |
| lavender | `#B8A7F3` |
| mint | `#8FD9C0` |
| sky blue | `#82C7EE` |
| peach | `#F2B58D` |
| butter yellow | `#E9D27A` |
| soft coral | `#E9948E` |

- Pastel accent는 selection, category, application role을 구분하는 보조 color다.
- Pastel color를 success, warning, error, unavailable 같은 semantic status color의 대체로 사용하지 않는다.
- Status는 semantic token, text/icon label과 함께 표시한다.
- Pastel filled control에는 contrast가 검증된 dark foreground를 사용한다.
- Text와 interactive state는 WCAG contrast를 통과해야 하며 실제 component pairing마다 측정한다.
- Neon saturation, excessive glow, 모든 surface의 gradient, gradient text를 피한다.
- Gradient는 identity artwork나 하나의 restrained accent area에만 필요할 때 사용한다.
- Light mode도 navigation, status, focus, disabled, error, chart와 form을 포함해 완전하고 usable해야 한다.

## Export and acceptance

- Raster master와 generation/selection metadata를 보존한다.
- 16px, 32px, 64px, 128px와 platform launcher size에서 확인한다.
- Light/dark background, platform mask, grayscale/menu-bar context를 구분해 검증한다.
- 한 중심 subject, safe margin, no text/watermark, readable eyes/ears/face mass를 유지한다.
- Role variants를 한 화면에 놓고 base recognition, role distinction, saturation balance를 비교한다.
- App icon, functional UI icon, menu-bar template을 서로의 export로 재사용하지 않는다.
