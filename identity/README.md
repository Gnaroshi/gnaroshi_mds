# Gnaroshi identity assets

## Origin

`reference/gnaroshi-origin-2020.jpeg`는 사용자가 2020년에 직접 만든 원본 reference다. Gnar의 작은 야수 이미지와 Garrosh의 강한 전사 이미지를 결합한 `gnar + garosh -> gnaroshi`에서 이름과 GitHub identity가 시작되었다.

원본은 역사와 identity의 기준이며, 낮은 해상도와 오래된 생성 품질을 그대로 최종 icon으로 사용해야 한다는 뜻은 아니다.

## Candidate selection

`candidates/`에는 서로 다른 그림체와 디자인의 raster 후보를 둔다. 선택 전에는 모두 concept이며, 사용자가 선택한 후보만 이후 app icon size set과 production export로 발전시킨다.

## Approved base

- Approved on: 2026-07-12
- Approved base: `approved/gnaroshi-base-v1.png`
- Source candidate: `candidates/07-cel-shaded.png`
- Metadata: `approved/metadata.json`
- Direction: cel-shaded animation
- Status: Gnaroshi application identity family의 owner-approved visual base다. App별 production icon은 이 base에서 role variant와 platform export를 만든다.

Source candidate는 삭제하거나 덮어쓰지 않는다. Approved base도 immutable master로 보존하고 derivative만 별도 path에 만든다. 앞으로 Gnaroshi identity icon을 새로 만들거나 다듬을 때는 사용자가 다른 방향을 지정하지 않는 한 approved base의 단순한 형태, 굵고 통제된 윤곽, 선명한 주황·청록 대비와 작은 크기 인식성을 기준으로 삼는다.

Role family, functional/menu-bar icon, shared dark/pastel palette와 export rule은 [`../guides/app-icons.md`](../guides/app-icons.md)에 있다.

평가 순서:

1. 작은 크기 인식성
2. Gnaroshi identity 유지
3. 단순한 silhouette
4. app/program 성격과의 적합성
5. light/dark background 호환성
