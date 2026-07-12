# Image generation and identity asset policy

## Default format

- 사용자가 별도로 vector image를 요청하지 않는 한 full-color image generation 요청은 raster 요청이다.
- 명시적 요청이 없으면 full-color identity, illustration과 scene을 SVG, EPS, AI, PDF vector 또는 code-drawn vector asset으로 생성하지 않는다.
- App/product identity master와 illustration 후보는 PNG, WebP, AVIF 또는 JPEG로 만든다.
- 배포 형식은 platform 요구사항에 맞추되 master raster를 보존한다.
- Functional UI icon과 menu-bar asset은 이 raster default의 blanket 대상이 아니며 [`app-icons.md`](app-icons.md)의 vector/template rule을 따른다.

## Gnaroshi identity

Origin reference: `identity/reference/gnaroshi-origin-2020.jpeg`

Approved application identity base: `identity/approved/gnaroshi-base-v1.png`

- 사용자가 2020년에 직접 만든 초기 이미지다.
- 이름과 mascot의 기원은 Gnar와 Garrosh의 결합인 `gnar + garosh -> gnaroshi`다.
- GitHub username `Gnaroshi`와 같은 개인 identity를 나타낸다.
- 핵심 인상은 작은 야수의 민첩함, 강한 전사의 존재감, 큰 귀, 날카로운 눈, 이빨, 주황/청록 대비다.
- 새 디자인은 이 history와 인상만 계승한다. 특정 게임 UI, 공식 logo, armor emblem 또는 원본 캐릭터를 그대로 복제하지 않는다.

## Icon acceptance

- 작은 크기에서도 읽히는 단순하고 강한 silhouette
- 한 개의 중심 subject와 충분한 safe margin
- text, watermark, UI mockup, 복잡한 background scene 없음
- 16px/32px/64px thumbnail에서도 눈, 귀, 얼굴 덩어리가 구분됨
- light/dark surface 모두에서 boundary가 사라지지 않음
- 후보는 서로 다른 style과 material을 탐색하되 동일 identity를 유지함

## Preferred direction

- Owner-approved 기준 asset은 `identity/approved/gnaroshi-base-v1.png`이며 selection provenance와 hash는 `identity/approved/metadata.json`에 있다.
- `identity/candidates/07-cel-shaded.png`는 source candidate로 그대로 보존한다.
- 사용자가 다른 방향을 요청하지 않는 한 Gnaroshi 관련 icon refinement는 cel-shaded raster style을 따른다.
- 유지할 특성은 굵고 통제된 outline, 단순한 2단계 명암, 큰 귀와 눈의 명확한 silhouette, 주황·청록 대비, 작은 크기 인식성이다.
- Role variant, functional icon, menu-bar template, shared palette와 platform export는 [`app-icons.md`](app-icons.md)를 따른다.
