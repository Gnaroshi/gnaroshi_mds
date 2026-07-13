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
- Approved full identity에서는 base의 얼굴, 눈, 귀와 주요 silhouette를 보존한다. Compact pixel launcher family에서는 완전한 얼굴을 어색하게 자르거나 가리지 않고, 양쪽 큰 귀와 네 개의 cyan eye만 deliberate identity band로 추출할 수 있다. 이때 role이 없는 main mark도 같은 band를 tile 정중앙에 배치할 수 있다.
- App role variant는 복잡한 character illustration이 아니라 작은 크기에서 용도가 구분되는 application icon으로 읽혀야 한다.
- 기본 Gnaroshi icon은 mascot을 수평·수직 중심축에 두며 이유 없이 한쪽 구석으로 밀지 않는다.
- App variant에서 snout, teeth, cheek, chest 또는 armor 일부만 잘린 채 남기지 않는다. 완전한 mascot portrait를 쓰지 않으면 ears-and-eyes band만 사용하고 나머지 얼굴은 명시적으로 제거한다.
- Role treatment는 tile 전면의 약 60–75%를 차지하고 최대 2–3개의 큰 visual mass로 구성한다. 실제 user action과 object를 보여주되 miniature illustration이나 여러 작은 prop을 모은 장면으로 만들지 않는다.
- Role subject가 먼저 보여야 한다. Identity band는 orange ear silhouette와 네 cyan eye만으로 family를 표시하며 role object의 outline이나 key color와 경쟁하지 않는다.
- Text, watermark, franchise logo, official emblem, trademark 또는 existing game asset의 direct copy를 넣지 않는다.
- 특정 game publisher가 selected design을 소유한다고 주장하지 않는다.

## Pixel application family

Owner가 pixel direction을 선택한 Gnaroshi application family는 서로 다른 pixel illustration을 모은 것이 아니라 하나의 반복 가능한 icon system으로 만든다.

### Shared grid and construction

- 모든 master는 처음부터 실제 `64×64` raster pixel grid에서 설계하고 nearest-neighbor 방식으로만 큰 raster export를 만든다.
- Anti-aliasing, sub-pixel stroke, blur, soft shadow, glow와 gradient를 사용하지 않는다.
- 주요 silhouette과 role glyph에는 2 logical pixel을 기본 outline으로 사용한다. 1 pixel detail은 눈, 이빨 또는 꼭 필요한 내부 구분에만 제한한다.
- Background, stepped frame, identity-band anchor, ear/eye position, outline value와 light direction은 family 전체에서 고정한다.
- Approved base를 직접 pixel master의 raster reference로 사용한다. App마다 text description만으로 mascot을 다시 생성하지 않는다.
- 먼저 한 개의 canonical ears-and-eyes pixel band를 확정하고, 모든 app variant는 그 동일 pixel coordinates를 재사용한다.
- Image generation은 role metaphor를 탐색하는 concept 단계에만 사용할 수 있다. Owner가 artificial/generated look를 지적한 뒤의 active pixel master는 generated large raster를 축소한 결과가 아니라 좌표, palette와 layer가 결정론적으로 재현되는 `64×64` source여야 한다.
- 16px/32px에서는 새로운 detail을 축소해 보존하려 하지 말고 optical small-size export에서 불필요한 detail을 제거한다.

### Fixed composition

- Base/default icon의 mascot은 tile 정중앙에 둔다. Role variant도 공통 수직 중심축을 유지하며 app마다 좌우 corner로 이동시키지 않는다.
- Current role family는 `identity-band` composition을 사용한다. 같은 orange ear silhouette와 네 cyan eye를 tile 뒤쪽 상단의 하나의 band로 두고, role subject가 아래쪽 전면을 차지한다.
- Identity band에는 nose, mouth, teeth, cheek, body, armor torso 또는 잘린 face edge를 넣지 않는다. 완전한 얼굴이 가려진 것처럼 보이지 않고 의도적으로 추출한 brand mark로 읽혀야 한다.
- Role subject는 약 `42–48px` bounding box, 같은 2px outline, flat front/three-quarter perspective와 내부 spacing을 사용한다. App의 대표 object와 action을 최대 세 개의 큰 mass로 단순화한다.
- Tile border, background, identity-band pixels와 role-subject anchor는 family 전체에서 동일해야 한다. Key color와 role geometry만 바꾸고 lighting, material, outline density를 달리하지 않는다.
- 16px/32px optical export에서는 role subject의 visual mass와 contrast가 mascot보다 커야 한다. 64px 이상에서는 role action과 mascot family가 함께 읽혀야 한다.
- Icon은 mascot portrait, AI illustration이나 rebus puzzle이 아니라 application launcher로 읽혀야 한다. 이름을 가린 32px 비교에서 foreground만 보고 대표 workflow를 말할 수 없거나 AI-generated scene처럼 보이면 geometry를 줄이고 다시 설계한다.

### Role glyph vocabulary and key colors

Role glyph는 아래 canonical symbol에서 시작한다. 의미를 흐리는 장식, 두 번째 metaphor 또는 miniature interface를 추가하지 않는다.

| Product | Canonical role glyph | Key color | Secondary color |
| --- | --- | --- | --- |
| Gnaroshi Studio | central hub/workbench + large pen nib + connected publish rays | lavender `#B8A7F3` | mint `#8FD9C0` |
| PaperFlow | two paper sheets + one sorter/funnel + indexed library slots | mint `#8FD9C0` | sky `#82C7EE` |
| Arxiv Discovery | one radar field/sweep + incoming papers + one discovered highlight | sky `#82C7EE` | peach `#F2B58D` |
| TR GPU Monitor | recognizable dual-fan GPU + live telemetry + remote nodes | soft coral `#E9948E` | aqua/teal `#3FA6A0` |
| RunShelf | stacked run records + experiment cue + metric-to-artifact trace | butter yellow `#E9D27A` | teal `#3FA6A0` |
| ContentDeck | media frame + dominant subtitle block + bounded segment loop | peach `#F2B58D` | lavender `#B8A7F3` |

- Studio에는 generic document icon, gear, dashboard grid 또는 command-center collage를 사용하지 않는다. Central workbench, connected work와 author/publish action이 함께 보여야 한다.
- PaperFlow에는 Zotero logo, generic folder, download arrow나 빈 tray만 사용하지 않는다. Paper가 분류되어 library record로 정돈되는 action을 보여준다.
- Arxiv Discovery에는 arXiv logo, generic magnifier나 scan gate 하나만 사용하지 않는다. 여러 paper가 radar sweep 안에서 발견되는 action을 보여준다.
- TR GPU Monitor에는 vendor logo, server rack 또는 command line을 넣지 않는다. Chip, telemetry와 remote status를 하나의 굵은 glyph로 결합한다.
- RunShelf에는 runner, fitness cue, server block, slider lane 또는 unreadable chart를 넣지 않는다. Experiment와 metric evidence가 durable indexed record로 남는 관계를 보여준다.
- ContentDeck에는 provider logo, repeat glyph 하나 또는 player UI 전체를 넣지 않는다. Media frame 안의 subtitle와 bounded segment practice가 한 scene으로 읽혀야 한다.

Role glyph는 icon 안의 설명문이 아니다. 각 glyph는 product promise를 한 개의 결합된 silhouette로 압축하고, 이름을 가린 32px 비교에서도 다른 app과 혼동되지 않아야 한다.

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
