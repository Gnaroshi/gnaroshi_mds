# Scientific illustration generation guide

## Role

이 guide는 논문, poster, 발표와 public research page에서 **image-generation model을 사용할 수 있는 범위**와 generated illustration의 품질 기준을 정의한다.

이 guide는 technical architecture, pipeline, operator graph 또는 data plot을 image model로 그리는 지침이 아니다. 그런 figure는 `technical-figure-code.md`의 evidence와 construction workflow를 사용한다.

Generated illustration의 우선순위는 다음과 같다.

1. 실제 subject와 activity의 즉시 인식
2. Scientific credibility와 evidence boundary
3. Gnaroshi visual authorship
4. Restrained composition과 paper/slide placement 적합성
5. Raster craft와 export quality

## Production method and export format are different

`PNG`, `TIFF`와 `raster`는 final file format 또는 export 방식이다. 이것만으로 image-generation model을 사용하라는 뜻이 되지 않는다.

다음 두 축을 분리한다.

| Question | Examples |
| --- | --- |
| 어떻게 제작하는가 | code, Figma, slide tool, manual drawing, raster editor, image-generation model |
| 무엇으로 전달하는가 | PNG, TIFF, PDF, EPS, SVG |

따라서:

- Code, Figma 또는 manual layout으로 만든 flat technical schematic도 final PNG로 export할 수 있다.
- Image-generation model이 만든 PNG라고 해서 technical figure가 되는 것은 아니다.
- Final raster 요청과 image-model-only 요청을 같은 뜻으로 해석하지 않는다.
- Figure brief에 `generated`라는 단어가 있어도 architecture, pipeline, formula, arrow와 exact module label이 핵심이면 constructed technical schematic이 필요하다.

## Request authority and boundary

현재 사용자 요청이 figure role, output format, 산출물 수와 작업 범위의 최상위 권한이다. 다만 publication-ready technical semantics를 image model의 추정에 맡기지는 않는다.

- 사용자가 cover, teaser 또는 non-technical concept illustration을 요청하면 이 guide를 primary track으로 사용한다.
- 사용자가 final PNG를 요청한 technical figure는 `technical-figure-code.md`의 constructed workflow로 제작하고 PNG로 export한다.
- 사용자가 image-model-only technical pipeline을 명시하면 exact text, connector와 operator를 보장할 수 없는 한 publication-ready technical figure라고 보고하지 않는다. Generated sketch와 limitation을 명시하거나 constructed annotation을 승인받는다.
- Code와 generated 결과는 둘 다 요청했을 때만 함께 만든다.
- 두 guide를 모두 읽는 것은 경계를 구분하기 위한 것이며 paired output을 자동으로 만들라는 뜻이 아니다.
- 이전 figure의 content, composition, panel structure와 wording을 그대로 재사용하지 않는다. 실패한 artifact는 rejection reference다.

## Image generation is allowed for

### Cover or teaser illustration

- Paper의 broad problem, environment 또는 contribution theme를 한 장면으로 소개한다.
- Exact architecture, loss와 operator를 설명하지 않는다.
- Caption이나 adjacent copy 없이도 broad subject가 2초 안에 보인다.

### Non-technical concept illustration

- 실제 physical object, robot, sensor, workspace 또는 activity를 concrete scene으로 보여준다.
- Illustration임을 caption과 alt text에서 밝힌다.
- Model output, benchmark observation 또는 experiment evidence처럼 보이게 만들지 않는다.

### Physical apparatus concept

- 실제 spatial arrangement와 physical relationship를 이해시키는 데 필요한 경우에만 사용한다.
- 장비, camera, object와 motion이 plausible해야 한다.
- Exact measurement, result 또는 unobserved component를 합성하지 않는다.

### Decorative support outside the technical panel

- Poster나 web page에서 technical figure와 분리된 hero/cover region
- Non-data background texture 또는 crop
- Technical panel의 arrow, module, legend와 겹치지 않는 별도 illustration

## Image generation is not allowed for

- Model architecture
- Software or training pipeline
- Temporal state transition
- Tensor, latent 또는 feature flow
- Operator graph
- Loss and gradient relationship
- Exact apparatus wiring
- Data plot, axis, statistic 또는 result
- Benchmark observation 또는 qualitative result 대체
- Module, state와 computation을 3D object로 바꾼 pseudo-diagram

Technical information을 표현해야 하면 flat 2D constructed schematic을 사용한다.

## Beautiful technical figures

시각적으로 완성도 높은 technical figure가 필요하다고 해서 image model을 사용하지 않는다.

1. `technical-figure-code.md`로 semantically complete baseline을 만든다.
2. Evidence map을 잠근다.
3. Figma, slide tool, raster editor 또는 manual layout에서 hierarchy와 spacing을 polish한다.
4. Real typeset text, verified arrows와 equations를 유지한다.
5. Target paper size에서 검증하고 final PNG/PDF로 export한다.

이 결과는 `polished constructed schematic`이다. Generated illustration과 다른 track이다.

## Figure role and information boundary

### Introduction

Introduction에 generated illustration을 사용하려면 broad problem이나 physical activity를 보여주는 teaser 역할이어야 한다.

- One-sentence message를 먼저 정한다.
- Main contribution을 adjacent text 또는 별도 constructed schematic과 연결한다.
- Full architecture, loss와 scheduler를 illustration에 압축하지 않는다.
- `Ours`의 technical superiority를 크기나 glowing object만으로 주장하지 않는다.

### Method and architecture

Generated illustration을 핵심 technical panel로 사용하지 않는다. Method/architecture는 constructed schematic을 사용한다.

Physical apparatus inset이 필요하면:

- technical schematic과 panel boundary를 분명히 나눈다.
- Illustration이라고 표시한다.
- Apparatus inset에서 module graph나 data flow를 대신 설명하지 않는다.

### Experiment and result

- Real observation, real apparatus photo와 actual plot을 우선한다.
- Generated scene는 evidence가 아니다.
- Generated scene를 qualitative example, baseline output, failure case 또는 benchmark frame 위치에 넣지 않는다.

## Reference package

Generation 전에 다음 reference role을 분리한다.

1. **Figure brief**
   - cover, teaser, non-technical concept 또는 physical apparatus
   - one-sentence message
   - target placement와 crop

2. **Subject reference**
   - real robot, apparatus, object, environment와 action
   - geometry, affordance와 mechanics 확인

3. **Evidence reference**
   - 실제 observation, apparatus photo 또는 public benchmark asset
   - generated image로 대체하면 안 되는 항목 표시

4. **Identity reference**
   - `identity/approved/gnaroshi-base-v1.png`
   - `guides/image-assets.md`
   - target project의 current render와 token

5. **Publication reference**
   - 같은 role의 cover, teaser 또는 concept illustration
   - content를 복사하지 않고 hierarchy, density와 crop만 분석

6. **Rejection reference**
   - 3D pseudo-machinery
   - blank label plate
   - generic AI artwork
   - poster-like crop used as a paper schematic
   - previously approved but later rejected artifact

## Real images and benchmark assets

- Benchmark RGB observation은 official public repository/dataset, paper project page 또는 사용자 실행에서 수집한 real frame을 사용한다.
- Generated robot scene를 observation, qualitative result 또는 evidence에 넣지 않는다.
- Source URL 또는 repository revision, dataset version, task/scene, frame index와 usage boundary를 기록한다.
- 사용자가 나중에 편집할 목적이면 original asset과 crop preview를 분리해 저장한다.
- Public repository에 넣기 전에 redistribution boundary를 확인한다.
- Real frame을 아직 구하지 못했으면 labeled neutral placeholder를 사용하고 limitation을 보고한다. Fake thumbnail을 생성하지 않는다.

## Gnaroshi visual character

### Palette

- warm page: `#f4f5f2`
- figure surface: `#fcfdfb`
- primary ink: `#18201c`
- secondary ink: `#3f4943`
- primary green: `#126954`
- soft green: `#dcebe5`
- identity teal: `#3fa6a0`
- identity orange: `#e88945`

Generated scene에서는 이 값을 UI palette처럼 모든 object에 칠하지 않는다. Warm neutral이 대부분을 차지하고 green, teal과 orange는 focal object 또는 작은 ownership cue에 제한한다.

### Identity boundary

Identity는 다음 인상에서 가져온다.

- sharp controlled silhouette
- compact strength
- warm field and deep ink contrast
- restrained green
- rare teal/orange tension
- generous negative space

Mascot의 얼굴, 귀, 눈, 이빨, armor 또는 logo를 scientific subject에 붙이지 않는다. Logo watermark를 넣지 않는다.

### Composition

- 한 개의 primary subject를 둔다.
- Subject의 physical action이나 broad contrast가 먼저 보이게 한다.
- Background detail은 subject comprehension에 필요할 때만 둔다.
- Cinematic spectacle보다 research-editorial calm을 유지한다.
- Annotation을 나중에 넣는다면 busy region이 아닌 deliberate quiet field를 남긴다.
- Blank callout plate를 만들어 technical label의 대체물처럼 두지 않는다.

## Prompt structure

### 1. Figure role

Cover, teaser, non-technical concept 또는 physical apparatus임을 명시한다.

### 2. Concrete subject

무엇이 어디에서 무엇을 하는지 한 문장으로 쓴다.

### 3. Visual message

독자가 가장 먼저 볼 physical action, contrast 또는 environment를 쓴다.

### 4. Composition

- view와 crop
- focal subject의 위치와 크기
- context의 역할
- quiet annotation field if needed
- target placement

### 5. Rendering

- illustration, restrained realism, editorial graphic 또는 painterly 중 하나
- believable material and mechanics
- controlled edge
- restrained lighting

### 6. Gnaroshi cues

- warm neutral field
- deep ink contrast
- limited research green
- rare teal/orange tension
- angular controlled silhouette

### 7. Evidence exclusions

- no fake observation
- no fake result
- no fake screen
- no technical module graph
- no generated equation or data

### 8. Output

- raster dimensions
- target physical placement
- background or transparency
- candidate ID

## Text and annotation

Generated illustration에 image model이 의미 있는 technical text를 그리게 하지 않는다.

- Title, short label와 caption이 필요하면 separate real typesetting layer를 사용한다.
- Pseudo-text, random glyph와 misspelled text를 final에 남기지 않는다.
- Blank label plate를 technical completeness처럼 제시하지 않는다.
- Technical label, equation, legend와 arrow가 필요해지는 순간 constructed schematic track으로 이동한다.
- Generated base의 잘못된 text는 제거한 뒤 final을 export한다.

## Paper-first size and raster export

Target venue의 figure specification이 항상 우선한다.

Venue가 아직 정해지지 않았다면 working reference로 다음을 사용한다.

- single column: 약 89 mm
- double column: 약 182 mm
- color or grayscale raster: final physical size에서 최소 300 dpi
- black-and-white line art: final physical size에서 최소 600 dpi

16:9는 paper figure의 기본값이 아니다. Slide, video, website hero 또는 사용자가 명시한 wide placement에만 사용한다.

Pixel dimension은 intended physical size와 dpi에서 계산한다. Low-resolution image를 나중에 upscale해 publication quality라고 보고하지 않는다.

## Permanent negative constraints

- technical architecture generated as a complete image
- 3D cube, portal, pipe, rail, tank, clamp or machine assembly used for computation
- crystal, ribbon, fluid or energy used for latent or feature flow
- isometric pipeline or dashboard
- pseudo-industrial cutaway
- game HUD or sci-fi control panel
- blank technical label plate
- pseudo-text, fake equation or random glyph
- generic robot-head, brain, lock, gauge, shield or sparkle
- floating holographic UI
- neon laboratory
- glassmorphism
- glossy toy-like 3D
- decorative wire or circuit background
- full-image pixel art
- pasted mascot or logo watermark
- fake benchmark frame, result, graph, screen or terminal output
- 16:9 web hero used by default as a paper figure

## Review workflow

### 1. Role gate

먼저 이 artifact가 정말 generated illustration에 해당하는지 확인한다.

- Technical relationship가 핵심이면 reject하고 constructed schematic으로 이동한다.
- Result나 observation evidence가 필요하면 real asset으로 이동한다.

### 2. Evidence gate

- Generated object가 measured or observed evidence처럼 보이지 않는가?
- Real image와 illustration boundary가 명확한가?
- Fake result, screen 또는 observation이 없는가?

### 3. Two-second test

Adjacent copy 없이 broad subject와 primary physical action이 보이는지 확인한다.

### 4. Full-resolution inspection

Anatomy, mechanics, duplicated object, impossible geometry, pseudo-text, artifact와 inconsistent lighting을 확인한다.

### 5. Gnaroshi comparison

- Warm neutral, deep ink와 limited accents가 유지되는가?
- Generic AI artwork가 아니라 controlled editorial illustration로 보이는가?
- Subject가 identity decoration보다 먼저 보이는가?

### 6. Placement review

- intended paper size, poster, slide 또는 web crop
- 160 px thumbnail
- grayscale if used in print
- contrast and color-blind-safe distinction

### 7. Owner review

Generated illustration은 owner approval 전에는 publication asset로 승격하지 않는다.

## Semantic gate before visual score

다음 중 하나라도 해당하면 점수를 매기지 않고 reject한다.

- Wrong artifact type: technical pipeline을 generated illustration로 만듦
- Fake evidence
- Missing disclosure
- Pseudo-text
- Technical meaning을 3D metaphor로 대체
- Paper placement와 다른 16:9 poster composition

Gate를 통과한 illustration만 다음을 평가한다.

| Dimension | Gate |
| --- | --- |
| Subject clarity | 4 이상 |
| Scientific credibility | 4 이상 |
| Gnaroshi distinctiveness | 4 이상 |
| Craft and restraint | 4 이상 |
| Placement resilience | 4 이상 |

Numeric score는 owner approval을 대신하지 않는다.

## Rejection records

후보가 나중에 reject되면 과거의 추천, 점수와 “pass” 표시는 publication approval로 사용할 수 없다.

- Candidate root에 rejection status와 날짜를 눈에 띄게 기록한다.
- `REJECTED_DO_NOT_USE.md`에 rejection reason과 replacement direction을 남길 수 있다.
- 과거 review 문서는 history로 보존하되 top에 현재 status를 추가한다.
- Rejected asset을 recommended list, paired review winner 또는 final deliverable로 계속 노출하지 않는다.
- Rejected asset을 삭제하지 않았다는 사실은 approval을 의미하지 않는다.

## Deliverables

- full-resolution raster
- intended-placement preview
- thumbnail
- source prompt and candidate ID
- reference package 목록
- real asset provenance
- alt text draft
- concept-illustration disclosure
- known limitation
- owner approval status

Technical evidence map이나 constructed schematic은 해당 작업에서 함께 요청되었을 때 별도 deliverable로 제공한다.

## Direct-file invocation

Codex CLI나 MCP가 없는 VS Code Remote-SSH 환경에서는 remote filesystem의 cloned guidance를 직접 읽는다.

> Figure 작업 전에 `<gnaroshi_mds-clone>`의 `main`을 `git pull --ff-only`로 최신화하라. `<gnaroshi_mds-clone>/AGENTS.md`, `guides/research.md`, `guides/technical-figure-code.md`, `guides/scientific-figure-generation.md`를 처음부터 다시 읽어라. PNG/raster는 export format이고 image-generation method와 다르다. Technical architecture, pipeline, tensor/latent flow, operator, loss, state transition과 data plot은 image model로 그리지 말고 `technical-figure-code.md`의 flat constructed schematic workflow를 사용하라. Image generation은 cover, teaser, non-technical physical concept 또는 technical panel 밖의 decorative support에만 사용하라. Real observation과 result는 sourced asset을 사용하고 fake substitute를 만들지 마라. 16:9를 paper 기본값으로 사용하지 말고 target venue 또는 약 89/182 mm placement에서 검증하라. Rejected candidate의 과거 점수나 추천을 approval로 사용하지 마라.

Remote path가 다르면 clone의 absolute path만 바꾼다. Guidance clone은 read-only reference로 취급한다.

## MCP invocation

MCP가 이미 제공되는 환경에서만 다음 resource를 읽는다.

> `gnaroshi://index`, `gnaroshi://guides/research`, `gnaroshi://guides/technical-figure-code`, `gnaroshi://guides/scientific-figure-generation`을 먼저 읽어라. Current request가 figure role과 output count를 결정하지만, raster export와 image generation을 혼동하지 마라. Technical schematic은 constructed flat 2D로 만들고 generated imagery는 cover, teaser와 non-technical concept에만 사용하라.

MCP는 optional convenience다. 이 guide를 적용하기 위해 Codex CLI나 MCP를 서버에 설치할 필요는 없다.

## Canonicality

Reusable figure policy를 target project의 output folder에 새 versioned guideline으로 복제하지 않는다.

- Reusable rule은 이 repository의 두 figure guide를 업데이트한다.
- Project-local `figure_spec`, caption, terminology와 evidence map은 target project에 둔다.
- Target project의 snapshot ZIP은 provenance artifact일 수 있지만 canonical guidance가 아니다.
- Project-local spec에는 사용한 `gnaroshi_mds` commit을 기록한다.

## Reference basis

- [Nature formatting guide](https://www.nature.com/nature/for-authors/formatting-guide): clarity에 필요한 만큼 단순하게 만들고 unnecessary panel, color와 detail을 피한다.
- [Nature research figure specifications](https://research-figure-guide.nature.com/figures/preparing-figures-our-specifications/): readable/editable text, final-size resolution과 accessibility를 검증한다.
- [PLOS Computational Biology — Ten Simple Rules for Better Figures](https://journals.plos.org/ploscompbiol/article?id=10.1371%2Fjournal.pcbi.1003833): message와 support medium을 먼저 정하고 beauty보다 scientific communication을 우선한다.
- [IEEE Author Center — Resolution and Size](https://journals.ieeeauthorcenter.ieee.org/create-your-ieee-journal-article/create-graphics-for-your-article/resolution-and-size/): one/two-column width와 300/600 dpi raster 기준을 publication size에서 적용한다.
- [Octo paper](https://octo-models.github.io/paper.pdf): broad overview와 exact labeled architecture를 다른 figure role로 분리하는 robotics reference다.
- [π0 paper](https://www.physicalintelligence.company/download/pi0.pdf): real robot-task evidence와 concise introductory story를 결합하는 reference다.
- [Diffusion Policy paper](https://diffusion-policy.cs.columbia.edu/diffusion_policy_ijrr.pdf): observation, mechanism, trajectory와 result의 visual role을 분리하는 robotics reference다.
- [RT-1 project and paper](https://robotics-transformer1.github.io/): real robot-task material과 model/action explanation을 역할별로 분리하는 robotics reference다.
- [OpenVLA project and paper](https://openvla.github.io/): generated substitute가 아닌 real evaluation media를 사용하는 VLA reference다.
- [ACT paper](https://tonyzhaozh.github.io/aloha/aloha.pdf): physical system evidence와 labeled technical architecture를 별도 visual grammar로 제시하는 reference다.

## Decision log

### 2026-07-19 — Establish generated visual exploration

Scientific communication may use generated raster illustration when its purpose is visual subject recognition and authorship rather than exact technical topology.

### 2026-07-20 — Separate raster export from image generation

PNG and raster describe output, not how a figure is built. Publication-ready technical schematics remain constructed and auditable even when their final export is PNG.

### 2026-07-20 — Restrict generation to illustration roles

Image-generation models are limited to cover, teaser, non-technical physical concept and clearly separated decorative support. Architecture, pipeline, state, operator and data relationships use constructed figures.

### 2026-07-20 — Reject blank labels and pseudo-3D computation

Blank annotation plates do not replace real text. Cubes, portals, rails, pipes, crystals and machine parts do not represent modules, latents or data flow.

### 2026-07-20 — Restore paper-first sizing

Sixteen-by-nine is not a paper default. Target venue dimensions take precedence, with approximately 89/182 mm and 300/600 dpi used only as a fallback working reference.

### 2026-07-20 — Make semantic status irreversible by visual scores

A semantic rejection invalidates earlier visual pass scores. Rejected candidates remain provenance records and are never publication assets merely because they were preserved.
