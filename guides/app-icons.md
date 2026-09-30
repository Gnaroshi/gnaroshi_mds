# Identity와 icon

승인된 원본·production master·과거 후보의 위치와 상태는 [identity 목록](../identity/README.md)을 기준으로 한다. 기존 승인 원본은 덮어쓰지 않고 derivative를 별도 경로에 만든다.

## 용도

| 용도 | 형식과 조건 |
| --- | --- |
| 앱·제품 identity | Raster master에서 platform asset으로 export. Mask, safe area, corner와 작은 크기 보정 검증 |
| Gnaroshi 웹 대표 mark·favicon·touch/manifest icon | Approved base의 전체 얼굴·귀·눈·얼굴 덩어리·이빨을 보존한 pixel raster. 귀·visor만 남긴 축약형 금지 |
| Compact application role family | 아래 P5 pixel system과 production master 사용 |
| Toolbar·navigation·status·form action | SF Symbols, Lucide 또는 일관된 monochrome vector system. Stroke·fill·optical size·label 처리 통일 |
| macOS menu bar | Monochrome template asset. System tint, selected state와 light/dark 검증 |

- 기능의 의미를 icon이나 색만으로 전달하지 않고 accessible label·text·state를 제공한다. Full-color mascot을 기능·메뉴바 icon으로 재사용하지 않는다.
- 큰 귀, 날카로운 눈, 강한 중심 silhouette와 teal/orange 대비를 유지한다. 일반 identity는 중심축에 두고 app마다 mascot pose·표정을 무리하게 바꾸지 않는다.
- Text, watermark, 복잡한 배경, franchise logo, UI, 공식 emblem과 기존 게임 asset의 직접 복사를 넣지 않는다. 특정 publisher의 소유물이라고 주장하지 않는다.

## P5 pixel application family

### 제작

- 실제 `64×64` raster grid에서 시작하고 큰 export는 nearest-neighbor만 사용한다. Anti-aliasing, sub-pixel stroke, blur, glow, soft shadow와 gradient를 사용하지 않는다.
- Major silhouette·role에는 2 logical pixel outline을 기본으로 쓰고 1px detail은 눈과 필수 내부 구분에 제한한다.
- Approved base를 직접 reference로 사용한다. App마다 prompt로 mascot을 재생성하지 않는다.
- Active master의 좌표·palette·layer와 재현용 tool·dependency 버전을 고정한다. 재생성 결과가 승인 master와 다르면 새 후보로 검토하고 기존 파일을 덮어쓰지 않는다. Generated raster는 role 탐색용 concept으로만 사용한다.
- Source grid, scale factor, palette와 SHA-256을 metadata에 기록한다. 16/32px optical export에서는 detail을 줄여 주요 덩어리를 보존한다.

### 공통 배치

- 모든 app이 같은 background, stepped frame, canopy 좌표, ear/visor, role plate, outline, light direction과 perspective를 공유한다.
- 뒤쪽 상단 canopy는 큰 orange 귀와 하나의 dark visor 안 네 개의 좁은 cyan eye slit으로 만든다. Nose, mouth, teeth, cheek, torso와 잘린 face edge를 남기지 않는다.
- 아래 전면 role plate는 tile의 약 60–75%를 차지한다. 최소 2px outer outline, 2px app-color rim과 dark inner surface로 canopy와 분리한다.
- 대표 작업물·도구 하나와 action/result cue 최대 하나를 결합한다. Front-facing perspective, `32–38px` bounding box, 2px outer outline, 1px internal separator와 같은 중심을 유지한다.
- App별 변경은 role geometry와 key color로 제한한다. 여러 작은 prop, miniature UI, portrait나 rebus puzzle로 만들지 않는다.
- Role subject의 mass·contrast가 canopy보다 먼저 읽혀야 한다. 16px는 family·key color, 32px는 primary instrument 구분, 64px 이상은 action/result까지 검증한다.

## 색과 role

| Product | 대표 도구와 결과 | Key color | 피할 대체물 |
| --- | --- | --- | --- |
| Gnaroshi Studio | Source tabs → manuscript·pen → publish output | `#B8A7F3` | Generic document·gear·dashboard·command-center collage |
| PaperFlow | Paper → guarded sorter → indexed slots | `#8FD9C0` | Zotero logo·folder·download arrow·빈 tray |
| Arxiv Discovery | Paper blips → radar sweep → acquired result | `#82C7EE` | arXiv logo·generic magnifier·scan gate만 사용 |
| TR GPU Monitor | Dual-fan GPU + telemetry + remote state | `#E9948E` | Vendor logo·server rack·command line |
| RunShelf | Indexed run records + metric·status·artifact | `#E9D27A` | Fitness·server block·slider lane·읽을 수 없는 chart |
| ContentDeck | Media + subtitle + bounded A–B practice | `#F2B58D` | Provider logo·repeat glyph만 사용·전체 player UI |

Identity teal은 `#3FA6A0`, orange는 `#E88945`다. Common result cue는 teal을 사용한다. Key color는 app role을 구분하며 success·warning·error를 대신하지 않는다. App canvas·text·control의 palette는 [ui-ux](ui-ux.md#gnaroshi-interface-palette)를 따른다.

## 검증과 export

- 16/32/64/128px와 실제 launcher size에서 silhouette, safe margin, role 구분과 family 인식을 확인한다.
- Light/dark, platform mask, grayscale와 menu-bar context를 구분해 검증한다. 이름을 가린 32px 비교에서 primary instrument가 구분되지 않으면 geometry를 단순화한다.
- Raster master와 selection metadata를 보존한다. ICNS, asset catalog, ICO, web PNG 등은 대상 repository에서 생성하며 build 중 이 저장소에서 다운로드하지 않는다.
