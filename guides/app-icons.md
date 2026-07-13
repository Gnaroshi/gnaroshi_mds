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
- 기본 Gnaroshi icon은 mascot을 수평·수직 중심축에 두며 이유 없이 한쪽 구석으로 밀지 않는다.
- App variant에서는 mascot이 tile을 가득 채우지 않게 약 35–50% footprint를 starting point로 삼고 충분한 negative space를 둔다. 정확한 면적 비율보다 얼굴·귀·네 눈·이빨의 recognition을 우선한다.
- Role treatment는 한 개의 결합된 symbol 또는 frame으로 제한하고 약 35–50% 안에서 application purpose가 읽히는 크기로 조정한다. 여러 miniature prop, 작은 UI control, card collage로 역할을 설명하지 않는다.
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

- Base/default icon의 mascot은 tile 정중앙에 둔다. Role variant도 공통 수직 중심축을 유지하며 app마다 좌우 corner로 이동시키지 않는다.
- App family는 아래 두 composition만 후보로 비교한다. 한 review round 안에서 임의의 세 번째 구조를 섞지 않는다.
  - `vertical-panel`: 같은 크기의 mascot을 위쪽 중앙에 두고, 얼굴 아래의 공통 role panel에 큰 glyph를 둔다.
  - `role-first`: 같은 크기의 작은 mascot crest를 위쪽 중앙에 두고, tile 중앙의 큰 role emblem을 primary subject로 둔다.
- Role glyph는 `vertical-panel`에서 약 `28–34px`, `role-first`에서 약 `32–38px` bounding box를 사용하고 같은 2px outline, corner radius와 내부 spacing을 공유한다.
- Mascot과 role 영역 사이에 최소 3 logical pixel의 negative space를 둔다. Role panel이나 emblem이 얼굴, 귀, 눈 또는 이빨과 겹치지 않게 한다.
- Tile border, background, mascot anchor, role container와 corner treatment는 각 composition family 안에서 동일해야 한다. Key color만 바꾸어 frame geometry가 달라지지 않게 한다.
- 64px 이상에서는 mascot과 role을 함께 읽을 수 있어야 한다. 16px/32px optical export에서는 role glyph의 visual mass와 contrast를 mascot보다 크게 유지해 app role을 먼저 구분하고, mascot은 family crest로 단순화할 수 있다.
- Icon은 mascot portrait가 아니라 application launcher로 읽혀야 한다. Role glyph, key-color field, mascot family의 순서로 1초 안에 app role과 family를 구분할 수 있어야 한다.

### Role glyph vocabulary and key colors

Role glyph는 아래 canonical symbol에서 시작한다. 의미를 흐리는 장식, 두 번째 metaphor 또는 miniature interface를 추가하지 않는다.

| Product | Canonical role glyph | Key color | Secondary color |
| --- | --- | --- | --- |
| Gnaroshi Studio | 중앙 document, 굵은 pencil과 바깥으로 향하는 publish cue를 한 형태로 결합 | lavender `#B8A7F3` | mint `#8FD9C0` |
| PaperFlow | 여러 paper sheet가 하나의 정돈된 tray로 안전하게 흐르는 결합 형태 | mint `#8FD9C0` | sky `#82C7EE` |
| Arxiv Discovery | 여러 incoming paper가 하나의 굵은 scan line/frame을 통과하고 discovery spark가 남는 형태 | sky `#82C7EE` | peach `#F2B58D` |
| TR GPU Monitor | compact GPU chip, 한 줄의 telemetry pulse와 작은 remote-node cue의 결합 | soft coral `#E9948E` | aqua/teal `#3FA6A0` |
| RunShelf | 세 experiment run lane이 같은 shelf bracket 안에서 시작 marker부터 indexed result marker로 이어지는 형태 | butter yellow `#E9D27A` | teal `#3FA6A0` |
| ContentDeck | 큰 subtitle card, segment bracket, play triangle과 한 개의 loop arc를 결합한 형태 | peach `#F2B58D` | lavender `#B8A7F3` |

- Studio에는 generic gear, dashboard grid 또는 command-center collage를 사용하지 않는다. Document와 pencil이 writing/publishing 역할을 직접 보여준다.
- PaperFlow에는 Zotero logo나 generic folder를 사용하지 않는다. 여러 paper가 하나의 안전한 흐름으로 정리되는 방향성을 보여준다.
- Arxiv Discovery에는 arXiv logo나 generic magnifier를 사용하지 않는다. 여러 incoming paper와 scan boundary가 지속적인 paper discovery를 먼저 읽히게 한다.
- TR GPU Monitor에는 vendor logo, server rack 또는 command line을 넣지 않는다. Chip, telemetry와 remote status를 하나의 굵은 glyph로 결합한다.
- RunShelf에는 runner, fitness cue, server block 또는 unreadable chart를 넣지 않는다. 시작부터 결과까지 이어지는 run lane과 indexed result가 experiment-run indexing을 보여준다.
- ContentDeck에는 provider logo나 player UI 전체를 넣지 않는다. Subtitle card를 primary로, segment loop와 playback cue를 secondary로 두어 단순 반복재생이 아니라 자막 기반 media learning을 보여준다.

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
