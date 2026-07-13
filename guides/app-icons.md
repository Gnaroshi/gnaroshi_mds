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
- Website favicon과 compact brand mark도 full-color product identity에 포함한다. 기존 interaction palette는 유지하고 mascot의 teal/orange는 제한된 ownership cue로 적용할 수 있다.

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
- App role variant는 복잡한 character illustration이 아니라 작은 크기에서 용도가 구분되는 application icon으로 읽혀야 한다.
- Mascot이 tile을 가득 채우지 않게 약 45–60% footprint를 starting point로 삼고 충분한 negative space를 둔다. 정확한 면적 비율보다 얼굴·귀·네 눈·이빨의 recognition을 우선한다.
- Role treatment는 한 개의 결합된 symbol 또는 frame으로 제한하고 약 25–40% 안에서 application purpose가 읽히는 크기로 조정한다. 여러 miniature prop, 작은 UI control, card collage로 역할을 설명하지 않는다.
- Role treatment가 mascot보다 먼저 보일 수는 있지만 얼굴, 눈, 귀, 이빨 또는 family silhouette를 가리거나 다른 character처럼 보이게 만들면 안 된다.
- Text, watermark, franchise logo, official emblem, trademark 또는 existing game asset의 direct copy를 넣지 않는다.
- 특정 game publisher가 selected design을 소유한다고 주장하지 않는다.

## Pixel application family

Owner가 pixel direction을 선택한 Gnaroshi application family는 서로 다른 pixel illustration을 모은 것이 아니라 하나의 반복 가능한 icon system으로 만든다.

### Shared grid and construction

- 모든 master는 `64×64` logical pixel grid에서 설계하고 nearest-neighbor 방식으로만 큰 raster export를 만든다.
- Anti-aliasing, sub-pixel stroke, blur, soft shadow, glow와 gradient를 사용하지 않는다.
- 주요 silhouette과 role glyph에는 2 logical pixel을 기본 outline으로 사용한다. 1 pixel detail은 눈, 이빨 또는 꼭 필요한 내부 구분에만 제한한다.
- Background, stepped frame, mascot anchor, face scale, ear position, outline value와 light direction은 family 전체에서 고정한다.
- Approved base를 직접 pixel master의 raster reference로 사용한다. App마다 text description만으로 mascot을 다시 생성하지 않는다.
- 먼저 한 개의 canonical pixel mascot master를 확정하고, 모든 app variant는 그 동일 master를 reference로 사용한다.
- 16px/32px에서는 새로운 detail을 축소해 보존하려 하지 말고 optical small-size export에서 불필요한 detail을 제거한다.

### Fixed composition

- Mascot은 tile의 왼쪽 위 또는 중앙에 고정된 동일 anchor와 scale로 배치한다. App마다 pose, expression, crop 또는 시점을 바꾸지 않는다.
- Role glyph는 한 개의 `20–24px` bounding box 안에서 같은 stroke와 corner language로 만든다.
- Role glyph가 작아져 의미를 잃지 않게 mascot과 role 영역을 분리하고 두 요소 사이에 최소 3 logical pixel의 negative space를 둔다.
- Tile border와 corner treatment는 모든 app에서 동일해야 한다. Key color만 바꾸어 frame geometry가 달라지지 않게 한다.
- Icon은 mascot portrait가 아니라 application launcher로 읽혀야 한다. Mascot, role glyph, key-color field의 순서로 1초 안에 family와 app role을 구분할 수 있어야 한다.

### Role glyph vocabulary and key colors

Role glyph는 아래 canonical symbol에서 시작한다. 의미를 흐리는 장식, 두 번째 metaphor 또는 miniature interface를 추가하지 않는다.

| Product | Canonical role glyph | Key color | Secondary color |
| --- | --- | --- | --- |
| Gnaroshi Studio | 한 장의 문서와 굵은 연필 | lavender `#B8A7F3` | mint `#8FD9C0` |
| PaperFlow | 겹친 문서가 하나의 오른쪽 flow arrow로 합쳐지는 형태 | mint `#8FD9C0` | sky `#82C7EE` |
| Arxiv Discovery | 문서와 큰 magnifying lens | sky `#82C7EE` | peach `#F2B58D` |
| TR GPU Monitor | compact GPU chip과 한 줄의 telemetry pulse | soft coral `#E9948E` | aqua/teal `#3FA6A0` |
| RunShelf | 한 선반 위의 세 개 indexed run block과 하나의 status dot | butter yellow `#E9D27A` | teal `#3FA6A0` |
| ContentDeck | loop ring 안의 play triangle과 하나의 subtitle strip | peach `#F2B58D` | lavender `#B8A7F3` |

- Studio에는 generic gear, dashboard grid 또는 command-center collage를 사용하지 않는다. Document와 pencil이 writing/publishing 역할을 직접 보여준다.
- PaperFlow에는 Zotero logo나 generic folder를 사용하지 않는다. 여러 paper가 하나의 안전한 흐름으로 정리되는 방향성을 보여준다.
- Arxiv Discovery에는 arXiv logo를 사용하지 않는다. Document와 magnifier가 discovery를 먼저 읽히게 한다.
- TR GPU Monitor에는 vendor logo, server rack 또는 command line을 넣지 않는다. Chip과 pulse만 사용한다.
- RunShelf에는 runner, fitness cue 또는 unreadable chart를 넣지 않는다. Shelf와 indexed blocks가 run indexing을 보여준다.
- ContentDeck에는 provider logo나 player UI 전체를 넣지 않는다. Loop, play, subtitle을 하나의 결합 glyph로 만든다.

Key color는 app role을 구분하는 identity color다. Available, success, warning, failed 같은 semantic state를 대신하지 않는다.

## Application role family

| Product family | Identity role | Suitable secondary motif |
| --- | --- | --- |
| Gnaroshi Studio | coordination, writing, publishing, central control | 연결 ring, 작은 page/pen, controlled hub cue |
| PaperFlow | papers, organization, safe flow | layered paper, ordered path, guarded flow cue |
| Arxiv crawler | discovery, scanning, incoming papers | scan arc, incoming sheet, discovery spark |
| TR GPU Monitor | GPU, telemetry, remote status | small chip grid, telemetry line, remote status pulse |
| RunShelf | experiment runs, shelves, indexed results | shelf line, indexed block, run marker |
| ContentDeck / `content-looper` | playback, looping, subtitles, learning | loop arc, play cue, compact subtitle strip |

Secondary motif는 logo collage가 아니라 하나의 굵고 단순한 role cue다. 작은 크기에서 의미가 사라지는 가는 선, 세부 pictogram, miniature interface를 피한다. Base mascot의 pose와 expression을 무리하게 바꿔 family recognition을 잃지 않는다.

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
