# Visual-quality-first scientific figure generation guide

## Purpose

이 guide는 논문, 연구 note, 발표와 public research page를 위한 시각 완성도 높은 figure candidate를 만드는 규칙이다.

이 track의 우선순위는 다음과 같다.

1. 강한 visual hierarchy
2. Gnaroshi만의 저자성
3. subject의 즉시 인식
4. 조형과 material의 완성도
5. 논문 또는 연구 맥락에서의 신뢰감

Generated candidate는 `technical-figure-code.md`의 code baseline을 대체하지 않는다. Code baseline이 즉시 사용 가능한 안전망이라면, 이 track은 더 아름답고 기억에 남는 최종 방향을 탐색한다.

## Paired review contract

사용자가 하나의 track만 요청하지 않았다면 code baseline과 generated candidate를 같은 review surface에서 나란히 보여준다.

비교할 때 다음을 분리한다.

| Code baseline | Generated candidate |
| --- | --- |
| 정확성 | visual authorship |
| 편집성과 반복 export | 조형과 분위기 |
| dense label과 관계 | 빠른 subject recognition |
| 즉시 사용 가능성 | final-direction potential |
| deterministic source | variation과 art direction |

두 결과의 약점을 평균내어 비슷한 중간 결과 두 개를 만들지 않는다. 필요한 경우 code baseline의 annotation layer와 generated candidate의 visual layer를 결합한 hybrid를 별도 후보로 만든다.

## Use this track when

- research concept를 한 장면으로 설명해야 한다.
- abstract, introduction, cover, poster 또는 hero 성격의 figure가 필요하다.
- method의 핵심 아이디어를 적은 수의 visual object로 보여줄 수 있다.
- experimental apparatus나 action을 구체적인 scene으로 설명할 수 있다.
- 기존 technical diagram이 정확하지만 anonymous하거나 template-like하다.
- Gnaroshi identity가 figure에서 충분히 느껴져야 한다.

Dense architecture, 많은 수식, exact data plot, 긴 label과 복잡한 connector가 핵심이면 generation만으로 완료하지 않는다.

## Visual thesis

각 candidate를 만들기 전에 다음 문장을 완성한다.

> 이 figure의 visual subject는 ___이고, 독자가 가장 먼저 보아야 할 변화 또는 관계는 ___이다.

Subject와 핵심 변화가 한 문장 안에서 명확하지 않으면 generation prompt를 길게 쓰기 전에 범위를 줄인다.

“AI”, “research”, “intelligence”, “efficiency”처럼 추상적인 단어만 subject로 사용하지 않는다. 실제로 보이는 object, action, state, contrast 또는 environment를 정한다.

## Reference package

Generation을 시작하기 전에 작은 reference package를 만든다.

### Required roles

1. **Identity reference**
   - `identity/approved/gnaroshi-base-v1.png`
   - `guides/image-assets.md`
   - target project의 current identity asset

2. **Product or publication reference**
   - target site 또는 application의 current render
   - design token
   - approved figure 또는 screenshot

3. **Subject reference**
   - 실제 apparatus, object, environment, material 또는 diagram family
   - paper-specific reference는 원래 project boundary 안에서만 사용

4. **Implementation evidence**
   - implemented system을 표현하면 `technical-figure-code.md`의 implementation source bundle과 evidence map
   - current commit, config, test와 verified runtime behavior
   - 시각화할 수 있지만 아직 확인하지 못한 항목의 목록

5. **Rejection reference**
   - 이전 candidate가 실패했다면 무엇이 generic, artificial, crowded, toy-like 또는 anonymous했는지 한 문장으로 기록

각 reference의 역할을 명시한다. Identity reference에서 subject를 복사하거나 subject reference에서 visual style을 무비판적으로 가져오지 않는다.

### Implementation-grounded generation

Generated candidate가 실제 software, model, pipeline, state 또는 execution behavior를 표현하면 visual thesis를 만들기 전에 code guide의 evidence map을 읽는다.

- Generation은 composition, metaphor, material과 focal hierarchy를 자유롭게 탐색할 수 있다.
- Evidence map에 없는 module, path, state, frequency, sharing, cache, tensor shape와 output을 기술 사실처럼 추가하지 않는다.
- Visual simplification으로 element를 합치면 무엇을 합쳤는지 review note에 기록한다.
- 아름다운 candidate가 code baseline과 다른 technical story를 말하면 visual quality와 관계없이 reject한다.
- Generated layer만으로 exact relationship을 검증하지 않는다. Final hybrid의 annotation과 connector는 evidence map을 다시 기준으로 검토한다.

## Gnaroshi visual character

Gnaroshi figure는 다음 긴장을 가진다.

- warm off-white와 deep near-black
- restrained research green과 sharp teal/orange
- quiet editorial field와 강한 focal subject
- realistic scientific material과 작은 angular identity cue
- modern clarity와 limited pixel boundary

### Shared palette

- warm page: `#f4f5f2`
- figure surface: `#fcfdfb`
- primary ink: `#18201c`
- secondary ink: `#3f4943`
- primary green: `#126954`
- soft green: `#dcebe5`
- identity teal: `#3fa6a0`
- identity orange: `#e88945`

Generated scene에서는 이 값을 literal UI palette처럼 모든 object에 칠하지 않는다. 전체 material과 light는 warm neutral로 유지하고, green·teal·orange는 focal object, edge, tool, annotation field 또는 small ownership cue에 제한한다.

### Shape character

Approved identity에서 다음 인상만 가져온다.

- sharp silhouette
- bold controlled edge
- alert focal point
- orange and teal tension
- compact strength
- angular rather than soft or bubbly

Mascot의 귀, 눈, 이빨, armor 또는 얼굴 구조를 scientific subject에 붙이지 않는다. Logo를 배경 장식이나 watermark로 넣지 않는다.

### Editorial composition

- 한 개의 primary subject를 둔다.
- primary subject가 canvas의 충분한 면적을 차지하게 한다.
- foreground, focal plane, context의 세 깊이를 명확히 한다.
- 빈 공간은 title 또는 annotation이 들어갈 수 있는 deliberate field로 남긴다.
- 대칭보다 의미 있는 비대칭을 우선한다.
- cinematic spectacle보다 research-editorial calm을 유지한다.
- background detail은 subject를 설명할 때만 둔다.

## Candidate directions

처음부터 하나의 polished image에 고정하지 않는다. 최소 세 방향은 composition과 visual grammar가 실제로 달라야 한다.

권장 direction family:

1. **Editorial apparatus**
   - 실제 장비, object와 action이 중심
   - believable material과 light
   - 가장 concrete하고 논문 친화적

2. **Graphic scientific illustration**
   - flat 또는 restrained depth
   - 명확한 silhouette와 color field
   - 적은 object와 강한 hierarchy

3. **Hybrid concept figure**
   - 하나의 scene 또는 central illustration
   - 별도 typeset annotation layer
   - 정확한 text와 아름다운 visual을 분리

세 candidate가 crop과 색만 다르고 같은 구도라면 exploration으로 보지 않는다.

## Generation prompt structure

Prompt는 다음 순서로 작성한다.

### 1. Concrete subject

무엇이 어디에서 무엇을 하는지 한 문장으로 쓴다.

### 2. Visual argument

독자가 가장 먼저 보아야 할 object, contrast, transition 또는 action을 쓴다.

### 3. Composition

- camera angle 또는 view
- focal subject의 위치와 크기
- foreground와 background 역할
- annotation safe area
- crop과 aspect ratio

### 4. Material and rendering

- believable material
- edge sharpness
- lighting direction
- depth 수준
- illustration, painterly, restrained realism, graphic 또는 hybrid 중 하나

### 5. Gnaroshi cues

- warm neutral field
- deep ink-like contrast
- restrained green
- small teal/orange tension
- angular, controlled edge
- optional 2 px or stepped accent in the later layout layer

### 6. Exclusions

해당 작업에서 발생하기 쉬운 failure를 구체적으로 나열한다.

### 7. Output

- raster
- aspect ratio
- target size
- background or transparency
- candidate ID

Prompt 안에 style adjective를 끝없이 쌓지 않는다. Subject, action, composition과 material이 먼저 명확해야 한다.

## Text and annotation boundary

Generation model이 다음을 그리게 하지 않는다.

- 논문 title
- 긴 label
- exact equation
- axis와 tick
- code
- terminal output
- architecture 관계
- data value
- paragraph

Generated visual에 label이 필요하면 빈 annotation zone을 계획하고 별도 composition 단계에서 실제 text를 추가한다. Generated pseudo-text를 흐리게 숨기거나 그럴듯한 기술 정보처럼 남기지 않는다.

Short symbolic glyph도 의미가 반드시 정확해야 하면 별도 layer에서 만든다.

## Figure families

### Concept scene

- 한 개의 실제 활동을 보여준다.
- subject는 2초 안에 식별되어야 한다.
- human hand, robot, sensor, paper, display와 object의 관계가 plausible해야 한다.
- generated writing과 fake code를 피한다.
- lab를 neon sci-fi set처럼 만들지 않는다.

### Method concept

- module box를 많이 그리는 대신 핵심 mechanism을 하나의 visual metaphor 또는 spatial action으로 바꾼다.
- input, transformation, output을 distinct object 또는 region으로 보여준다.
- exact architecture는 code baseline 또는 annotation layer에 맡긴다.

### Experiment overview

- apparatus, sensor, target, environment와 action을 한 view에서 이해하게 한다.
- 실제 evidence가 아닌 경우 illustration임을 caption과 alt text에서 밝힌다.
- plausible value나 fake result를 합성하지 않는다.

### Data-led editorial figure

- plot 자체는 실제 data renderer로 만든다.
- generated visual은 background texture, framing, subject illustration 또는 non-data context에만 사용한다.
- data mark, axis와 annotation을 generated raster에 맡기지 않는다.

### Hybrid

- generated scene 또는 central object를 visual anchor로 사용한다.
- label, arrow, plot, equation과 legend는 별도 typeset layer로 만든다.
- raster와 text layer의 contrast, scale와 edge quality를 맞춘다.
- generated layer가 evidence처럼 오인되지 않게 한다.

## Gnaroshi identity motifs

Candidate마다 다음 중 2–3개만 선택한다.

- large editorial title field
- near-black frame or rule
- deep green focal path
- teal endpoint
- rare orange square or edge
- angular silhouette
- stepped corner in the later layout layer
- short hard shadow
- generous warm negative space
- monospaced small index added after generation

모든 motif를 한 candidate에 넣으면 identity가 아니라 theme가 된다.

## Permanent negative constraints

- generic corporate infographic
- PowerPoint academic template
- equal rounded cards
- default royal-blue technical palette
- generic robot-head or brain icon
- AI sparkle and magic particles
- floating holographic UI
- random equation
- pseudo-code and pseudo-text
- cyberpunk and neon laboratory
- glossy toy-like 3D
- miniature diorama
- isometric dashboard
- glassmorphism
- blur-heavy shadow
- decorative circuit background
- full-image pixel art
- bitmap typography
- pasted mascot
- logo watermark
- unrelated props
- fake result, fake graph, fake screen, fake terminal output

## Review workflow

### 1. Full image inspection

Thumbnail만 보지 않고 original resolution에서 anatomy, mechanics, material, text artifact, duplicated object와 impossible geometry를 확인한다.

### 2. Two-second test

Adjacent copy 없이 broad subject와 primary action이 보이는지 확인한다.

### 3. Gnaroshi comparison

Approved identity, target project의 current render와 candidate를 나란히 둔다.

질문:

- generic AI artwork가 아니라 Gnaroshi가 만든 figure처럼 보이는가?
- warm neutral, deep ink와 limited accents가 유지되는가?
- sharp하고 controlled한 visual character가 있는가?
- subject가 identity decoration보다 먼저 보이는가?
- mascot을 붙이지 않아도 family resemblance가 있는가?

### 4. Scientific credibility

- object와 apparatus가 plausible한가?
- fake evidence처럼 보이는가?
- 연구 관계를 오해하게 만드는 visual이 있는가?
- scene이 concept illustration임을 공개할 수 있는가?

### 5. Crop tests

- working size
- paper placement
- slide
- 160 px thumbnail
- mobile crop when web use is planned

### 6. Paired review

Code baseline과 generated candidate를 함께 본다.

각 결과 아래에 다음을 표시한다.

- strongest use
- known limitation
- recommended next step: use baseline, refine candidate, or build hybrid

Owner approval 전에는 generated candidate를 production figure로 승격하지 않는다.

## Scoring

각 candidate를 0–5로 평가한다.

| Dimension | Gate |
| --- | --- |
| Subject clarity | 4 이상 |
| Visual hierarchy | 4 이상 |
| Gnaroshi distinctiveness | 4 이상 |
| Scientific credibility | 4 이상 |
| Craft and material quality | 4 이상 |
| Crop resilience | 4 이상 |
| Restraint | 4 이상 |

한 항목이라도 gate 아래면 polish 대상으로 유지한다. Numeric pass는 owner approval을 대신하지 않는다.

## Deliverables

- full-resolution raster candidate
- 160 px thumbnail
- paper-size preview
- reference package 목록
- implementation-grounded 작업이면 inspected commit과 evidence map
- generation prompt
- candidate ID
- alt text 초안
- concept illustration disclosure
- rejection 또는 limitation note
- code baseline과의 side-by-side review sheet

## Decision log

### 2026-07-19 — Establish the visual-quality track

Scientific figure work needs a separate generated path whose purpose is visual authorship and craft, not merely a decorated technical diagram.

### 2026-07-19 — Require paired review

When speed and visual quality both matter, review an immediately usable code baseline beside a generated candidate. Keep their acceptance criteria distinct and choose a final or hybrid direction after viewing the rendered outputs.

### 2026-07-19 — Strengthen Gnaroshi authorship without mascot decoration

Use warm neutral fields, deep ink, restrained research green, sharp teal/orange tension, angular edges, strong focal hierarchy, and editorial negative space. Do not manufacture identity by pasting the mascot or logo into the figure.

### 2026-07-19 — Bind generated implementation figures to code evidence

Visual generation may reinterpret composition and material, but an implemented system's technical story must come from the code guide's source bundle and evidence map.
