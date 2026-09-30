# 연구용 생성 일러스트

Cover, teaser, 비기술적 concept와 물리적 장면의 illustration에 적용한다. [공통 figure 규칙](research-figures.md)의 제작 경계·출처·크기·palette·최종 검토를 따른다. Architecture, pipeline, operator, state와 데이터 관계는 [기술 도식](technical-figure-code.md)으로 구성한다.

## 허용 범위

- Paper의 broad problem, environment 또는 활동을 소개하는 cover/teaser
- 실제 robot, sensor, object, workspace와 활동을 보여주는 비기술적 concept
- 공간 배치를 이해시키는 apparatus concept. 정확한 배선·측정값·관측하지 않은 부품을 evidence로 합성하지 않는다.
- Technical panel과 분리된 poster/web hero, 비데이터 texture·crop

Illustration임을 caption과 alt text에 표시한다. 실제 observation·장비 사진·model output·benchmark·qualitative result를 대체하지 않는다. Technical inset과 함께 쓰면 panel boundary를 구분하고 module graph나 data flow를 illustration에 맡기지 않는다.

## Reference와 prompt

생성 전 아래 항목을 구분해 준비한다.

| 항목 | 필요한 내용 |
| --- | --- |
| Brief | 역할, 한 문장 message, placement와 crop |
| Subject | 실제 물체·활동의 geometry, affordance와 mechanics |
| Evidence | 생성물로 대체하면 안 되는 실제 이미지·결과와 출처 |
| Visual reference | 프로젝트의 승인된 render/token, 비슷한 역할의 hierarchy·density |
| Rejection reference | 이전 실패의 이유와 금지할 표현 |

Prompt에는 역할 → 무엇이 어디서 무엇을 하는지 → 핵심 활동·대비 → view/crop/초점 → rendering/material/light → 제한된 색 → evidence 제외 조건 → 크기·투명도·candidate ID 순으로 작성한다.

- 하나의 primary subject와 물리적 활동이 먼저 보여야 한다. 배경은 이해에 필요한 만큼만 둔다.
- Illustration, restrained realism, editorial graphic 또는 painterly 중 작업에 맞는 표현을 정하고 물리적으로 가능한 geometry·mechanics를 유지한다.
- Warm neutral, deep ink와 작은 green/teal/orange 강조를 사용한다. Mascot의 얼굴·귀·눈·이빨·armor나 logo를 subject에 붙이지 않는다.
- Annotation이 필요하면 조용한 여백과 별도 실제 typesetting layer를 사용한다. Technical label·수식·legend·arrow가 필요하면 해당 부분은 직접 구성한다.
- Image model에 의미 있는 technical text를 맡기지 않는다. 잘못된 text·random glyph·blank callout plate는 final에 남기지 않는다.

## 제외할 표현

- Computation을 대신하는 cube·portal·pipe·rail·tank·clamp·기계 조립도
- Latent/feature를 대신하는 crystal·ribbon·fluid·energy
- Isometric pipeline, pseudo-industrial cutaway, game HUD와 sci-fi dashboard
- Generic robot-head·brain·lock·gauge·shield·sparkle, floating holographic UI
- Neon laboratory, glossy toy-like 3D, glassmorphism, 장식 wire/circuit
- Fake observation·result·graph·screen·terminal output, pseudo-equation

## 검토와 결과

1. 역할과 evidence 경계를 먼저 검사한다. 기술 관계가 핵심이면 constructed schematic으로, 관측·결과가 필요하면 실제 asset으로 전환한다.
2. 설명 없이 broad subject와 primary activity가 2초 안에 읽히는지 확인한다.
3. 원본 해상도에서 anatomy, mechanics, 중복 물체, 불가능한 geometry, text artifact와 조명 일관성을 검사한다.
4. 최종 배치에서 subject clarity, scientific credibility, 절제된 색·형태, crop·축소 내구성을 확인한다.
5. Owner approval 전에는 publication asset로 승격하지 않는다. 점수나 자체 검토가 승인을 대신하지 않는다.

요청한 raster, prompt·candidate ID, reference/실제 asset 출처, alt text·illustration disclosure, 알려진 한계와 approval status를 제공한다. Placement preview와 thumbnail은 검증에 사용하고 별도 제출 수는 요청을 따른다. Rejected 후보는 [공통 status 규칙](research-figures.md#최종-검토)에 따라 현재 사용 대상에서 제외한다.
