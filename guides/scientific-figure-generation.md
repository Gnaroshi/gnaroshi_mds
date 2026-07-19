# Generated-raster scientific figure guide

## Role

이 guide는 논문, 연구 note, 발표와 public research page를 위한 visual-quality-first raster figure를 생성하고 완성하는 규칙이다.

Generated figure의 목표는 단순히 분위기 좋은 illustration을 만드는 것이 아니다.

1. Figure role과 한 문장 claim이 즉시 보인다.
2. 기술 관계, terminology와 real evidence가 정확하다.
3. Final PNG에 필요한 text, arrow, time index와 label이 실제로 존재한다.
4. Gnaroshi visual identity가 hierarchy, spacing, edge와 restrained accent에서 느껴진다.
5. Paper size에서 읽을 수 있고 scientific figure로 신뢰할 수 있다.

## Request authority and medium boundary

현재 사용자 요청이 medium, 산출물 수, 작업 범위와 우선순위의 최상위 권한이다.

- 사용자가 generated raster만 요청하면 이 guide를 primary production track으로 사용한다.
- `technical-figure-code.md`를 함께 읽더라도 code-based figure를 자동으로 만들지 않는다.
- Generated raster 요청을 code guidance와의 충돌로 보고하지 않는다.
- Code baseline, generated candidate와 side-by-side review는 사용자가 두 track을 명시적으로 요청했을 때만 만든다.
- Final output이 raster라는 조건은 exact text, arrow와 annotation을 생략해도 된다는 뜻이 아니다. Generated base를 raster editor, image editing 또는 typesetting layer와 합성해 최종 PNG로 완성할 수 있다.
- 이전 figure의 content, composition, panel structure와 wording을 그대로 재사용하지 않는다. 이전 결과가 실패했다면 rejection reference로만 사용한다.

## Classify the figure before generation

Figure family를 먼저 분류한다. 서로 다른 family의 grammar를 섞으면 결과가 scientific diagram이 아니라 pseudo-machinery나 decorative poster가 되기 쉽다.

### A. Technical explanatory figure

Architecture, pipeline, temporal process, model comparison, training objective 또는 implementation behavior를 설명한다.

- Flat 2D orthographic scientific graphic을 기본으로 한다.
- Module, tensor, feature, latent, operator와 state는 simple field, band, token strip, line, bracket 또는 typeset notation으로 표현한다.
- Exact relationship는 arrow, alignment, grouping과 real text로 설명한다.
- Perspective, volumetric depth, cinematic lighting과 material rendering을 사용하지 않는다.
- 3D cube, portal, rail, pipe, tank, motor, clamp, machine part, glowing chamber와 isometric component로 computation을 표현하지 않는다.
- Visual metaphor가 evidence map의 technical relation을 대신하지 않는다.

### B. Physical concept or apparatus scene

Robot, camera, workspace, sensor, object와 physical action처럼 실제 공간의 대상을 설명한다.

- 실제 physical geometry를 이해하는 데 필요하면 perspective, light와 material을 사용할 수 있다.
- Illustration이면 caption과 alt text에서 illustration임을 밝힌다.
- 실제 experiment evidence처럼 보이게 만들지 않는다.
- Physical scene를 technical pipeline의 module replacement로 사용하지 않는다.

### C. Data or result figure

- Plot, axis, data mark, statistic과 value는 actual data renderer에서 만든다.
- Generated visual은 non-data context 또는 illustration에만 사용한다.
- Fake graph, plausible number와 fabricated screen을 만들지 않는다.

### D. Hybrid figure

- Real observation, generated non-evidentiary scene 또는 visual field를 anchor로 사용할 수 있다.
- Module label, arrow, equation, legend, axis와 data는 separate exact layer로 만든다.
- Final deliverable은 하나의 검증된 raster로 합성한다.

Figure가 둘 이상의 family에 해당하면 panel별로 grammar를 분리하고, technical panel에 physical-scene style을 넘기지 않는다.

## Figure role and information budget

### Introduction overview

Introduction figure는 상세 구현을 모두 보여주는 곳이 아니다.

- 독자가 기억해야 할 한 문장을 먼저 쓴다.
- Main contribution 또는 `Ours`를 가장 크고 가장 선명한 focal region으로 둔다.
- Baseline과 context는 comparison을 이해하는 데 필요한 만큼만 작게 둔다.
- Input → main idea → consequence의 한 reading path를 우선한다.
- 논리적으로 연결되지 않은 panel은 분리한다.
- Loss, auxiliary branch, tensor dimension, parameter-freezing과 detailed scheduler는 main claim에 필수일 때만 남긴다.
- Figure가 2초 안에 broad subject를 설명하지 못하면 panel이나 concept 수를 줄인다.

Introduction figure의 기본 budget은 one-sentence claim, one dominant mechanism과 최소한의 before/after 또는 input/output context다. 이 범위를 넘는 detail은 method figure로 이동한다.

### Method or architecture figure

- Exact input, module, output, operator와 temporal dependency를 보여줄 수 있다.
- Panel마다 inference, training, objective 또는 schedule 중 하나의 질문에 집중한다.
- Technical completeness보다 auditable reading order를 우선하고, 생략한 detail은 caption 또는 별도 panel로 보낸다.

### Experiment overview

- Actual apparatus, sensor, observation, task와 action을 보여준다.
- Real image와 illustration을 명확히 구분한다.
- Qualitative result와 decorative scene가 섞이지 않게 한다.

## Publication-first principles

- Figure를 만들기 전에 독자가 얻어야 할 message를 한 문장으로 쓴다.
- Clarity와 logical connection을 유지하는 범위에서 figure와 panel을 최소화한다.
- Beauty가 technical message, data provenance 또는 readability를 이기지 못한다.
- Color는 grouping, comparison, state와 focal hierarchy에만 사용한다.
- Intended single- or double-column size에서 text와 arrow를 검증한다.
- Caption은 context와 abbreviation을 설명할 수 있지만, figure 안의 잘못된 edge나 누락된 required label을 보완하지 못한다.

## Implementation grounding for generated technical figures

Generated technical figure도 `technical-figure-code.md`의 implementation source bundle, terminology authority와 evidence map을 그대로 사용한다.

### Non-negotiable rules

- Composition을 만들기 전에 current code, config, tests와 필요한 runtime trace를 조사한다.
- Module의 signature뿐 아니라 actual call site와 preprocessing을 확인한다.
- Every arrow, merge, split, time index, shared/frozen/detached state와 loss edge를 evidence map에 연결한다.
- `mean`, add, concat, gating, residual, pooling과 attention을 모양으로 추정하거나 서로 바꾸지 않는다.
- 이름에 `delta`, `encoder`, `update` 또는 `reactive`가 들어간다는 이유로 input과 behavior를 추정하지 않는다.
- `action_t`와 `observation_{t+1}` 사이의 environment transition을 module data flow처럼 그리지 않는다.
- Training과 inference path, current state와 next-state target을 구분한다.
- Evidence map에 없는 path, module, frequency, cache, shape 또는 output을 추가하지 않는다.
- Visual simplification으로 element를 합쳤다면 무엇을 합쳤는지 review note에 기록한다.
- 아름다운 figure가 current implementation과 다른 story를 말하면 자동 reject한다.

### Wording authority

Figure의 exact terminology는 다음 순서로 결정한다.

1. 현재 사용자가 이번 작업에서 승인하거나 요구한 wording
2. Target paper의 current abstract, method와 terminology table
3. Current code의 public identifier와 config/log name
4. Older draft 또는 이전 generated figure

이전 figure의 표현을 그대로 사용하라는 일반 규칙은 없다. 승인되지 않은 `Reactive latent update` 같은 새 phrase, 더 그럴듯해 보이는 synonym 또는 marketing wording을 만들지 않는다.

## Reference package

Generation 전에 작은 reference package를 만든다.

1. **Figure brief**
   - figure role
   - one-sentence claim
   - required semantic inventory
   - target paper size

2. **Implementation evidence**
   - inspected branch, commit과 dirty state
   - evidence map
   - verified terminology
   - current paper/code mismatch

3. **Publication references**
   - 같은 role의 strong scientific figure
   - introduction과 method figure를 구분해 수집
   - content를 복사하지 않고 information density, hierarchy와 annotation grammar를 분석

4. **Identity references**
   - `identity/approved/gnaroshi-base-v1.png`
   - `guides/image-assets.md`
   - target site 또는 project의 current render와 token

5. **Real subject and evidence assets**
   - actual apparatus, environment, observation 또는 dataset frame
   - source, version, task/scene와 usage boundary

6. **Rejection references**
   - 이전 candidate가 틀린 arrow, operator, wording 또는 time relation
   - 3D pseudo-machinery, empty label, generic palette, clutter와 weak `Ours`
   - 재사용할 content가 아니라 반복하지 않을 failure로 기록

## Required semantic inventory

Technical figure는 prompt 전에 다음 inventory를 만든다.

- panel letter와 short panel title
- main contribution의 exact public name
- required module names
- required inputs and outputs
- each arrow의 start, end, direction and meaning
- each merge/split의 exact operator
- all time, state, chunk and refresh notation
- shared, frozen, trainable, detached and loss status
- real observation slot and source
- caption으로 이동할 detail
- figure에서 의도적으로 생략할 verified detail

이 inventory가 비어 있거나 evidence map과 연결되지 않으면 generation을 시작하지 않는다.

## Text is mandatory in the final technical raster

Image model이 exact typography를 안정적으로 만들지 못하더라도 final technical figure에서 text를 없애지 않는다.

- Generated base는 blank semantic placeholder가 있는 상태로 final deliverable이 아니다.
- Final PNG에는 필요한 panel title, module label, input/output, operator, time index, legend와 concise transition label이 actual readable text로 들어가야 한다.
- Pseudo-text, misspelled label, random symbol와 비어 있는 title plate는 허용하지 않는다.
- Image model이 text를 틀리면 raster editing, image editing 또는 separate typesetting layer로 수정한다.
- Generated base의 잘못된 text는 덮어 쓰거나 제거한 뒤 final을 export한다. 흐리게 숨겨 남기지 않는다.
- Exact equation, axis, tick과 data value도 verified layer로 만든다.
- Figure title 전체를 넣을 필요는 없지만, 그림만 보아도 module과 relation을 구분하는 semantic text는 필수다.
- 모든 text를 expected paper size에서 직접 읽어본다.

## Flat 2D visual grammar for technical figures

### Composition

- 한 개의 dominant reading path를 둔다.
- `Ours` 또는 main mechanism이 canvas의 가장 넓은 meaningful area를 차지한다.
- Baseline은 alignment와 limited contrast로 비교하되 main contribution과 같은 면적을 자동 배정하지 않는다.
- Time은 하나의 horizontal rail 또는 aligned small multiple로 표현한다.
- Training/inference는 row, panel 또는 explicit boundary로 나눈다.
- Whitespace로 group을 만들고 border는 필요한 boundary에만 둔다.
- Connector가 교차하면 visual effect를 추가하지 말고 layout을 바꾼다.

### Shape

- Flat field, straight rule, bracket, token strip, square 또는 restrained small-radius rectangle를 사용한다.
- Shape 종류는 semantic category 수보다 많지 않게 유지한다.
- Bevel, extrusion, perspective face, glossy surface, glass, pipe, wire bundle와 mechanical joint를 사용하지 않는다.
- Latent나 feature를 faceted crystal, ribbon tunnel, glowing fluid, container 또는 physical payload로 표현하지 않는다.
- Robot icon과 camera icon은 실제 observation source를 구분할 때만 작게 사용한다.

### Gnaroshi palette

- warm page: `#f4f5f2`
- figure surface: `#fcfdfb`
- primary ink: `#18201c`
- secondary ink: `#3f4943`
- muted ink: `#5f6b63`
- quiet border: `#d5dbd4`
- strong border: `#aab5ac`
- primary green: `#126954`
- soft green: `#dcebe5`
- identity teal: `#3fa6a0`
- identity orange: `#e88945`

Neutral이 canvas 대부분을 차지한다. Green은 main contribution 또는 verified active path, teal은 endpoint나 secondary state, orange는 rare index, change point 또는 small emphasis에 제한한다.

Identity는 3D style, mascot, logo watermark 또는 orange/teal object의 반복에서 만들지 않는다. 다음에서 만든다.

- clear asymmetric hierarchy
- generous warm negative space
- deep ink rule
- restrained research green focal path
- sharp but quiet edge
- rare teal/orange ownership cue
- controlled spacing rhythm

### Typography

- Actual typeset sans-serif를 사용한다.
- Math와 variable은 consistent math rendering을 사용한다.
- Sentence case를 기본으로 한다.
- 모든 label을 같은 bold weight로 만들지 않는다.
- Final size에서 약 8 pt 미만으로 내려가지 않게 한다.
- Text를 textured, shaded 또는 busy region 위에 직접 올리지 않는다.

## Generated physical scenes

Physical concept 또는 apparatus scene에서는 실제 공간을 묘사할 수 있다.

- Robot, sensor, object와 action의 mechanics가 plausible해야 한다.
- Primary subject가 2초 안에 식별되어야 한다.
- Neon lab, holographic UI, magic particle와 generic AI symbolism을 피한다.
- Scene의 light와 material은 subject comprehension을 돕는 범위에서만 사용한다.
- Illustration은 benchmark image나 experiment result가 아니다.
- Technical module, latent update 또는 feature fusion을 physical machine으로 재현하지 않는다.

## Real benchmark images

- LIBERO 등 benchmark의 RGB observation은 official public repository/dataset, paper project page 또는 사용자 실행에서 수집한 real frame을 사용한다.
- Generated robot scene를 `Primary RGB`, `Wrist RGB` 또는 qualitative result에 넣지 않는다.
- Source URL 또는 repository revision, dataset version, task/scene, frame index와 license/usage note를 기록한다.
- 사용자가 나중에 편집할 목적이면 original asset과 crop preview를 분리해 저장하고 명확한 filename을 사용한다.
- Public repository에 넣기 전에는 source와 redistribution boundary를 확인한다.
- Real frame을 아직 구하지 못했으면 actual text가 있는 neutral placeholder를 사용하고 limitation을 보고한다. Fake thumbnail을 생성해 채우지 않는다.

## Candidate directions

사용자가 여러 candidate를 요청했을 때만 여러 방향을 만든다. Crop과 색만 다른 같은 구도를 세 개 만드는 것은 exploration이 아니다.

### Technical figure directions

1. **Flat annotated overview**
   - one main path
   - concise exact labels
   - method contribution이 가장 큰 central field

2. **Temporal comparison strip**
   - baseline과 ours를 aligned row로 비교
   - time, refresh와 state transition을 한 axis에서 읽음
   - repeated step을 small multiple이나 bracket으로 압축

3. **Focal mechanism with supporting context**
   - central mechanism을 크게 표시
   - input, supervision과 output은 얇은 supporting band
   - introduction 또는 method key figure에 적합

세 방향 모두 flat 2D technical grammar를 유지한다. 3D/object style을 “다른 candidate”로 추가하지 않는다.

### Physical or hybrid directions

- real-evidence montage with restrained annotation
- concrete apparatus illustration
- generated non-evidentiary scene plus exact typeset overlay

## Technical generation prompt structure

Prompt는 다음 순서로 작성한다.

### 1. Figure role and one-sentence claim

Introduction인지 method인지 명시하고, 독자가 가장 먼저 이해해야 할 문장을 쓴다.

### 2. Exact semantic content

- panel list
- approved labels
- inputs and outputs
- verified arrows
- exact operators
- time/state notation
- main contribution and supporting context

### 3. Hierarchy

- `Ours`의 위치와 dominant area
- supporting baseline의 smaller area
- reading direction
- whitespace와 annotation zone

### 4. Technical visual grammar

- flat 2D orthographic
- no perspective
- no material or volumetric depth
- simple field, rule, bracket, token strip and exact connector

### 5. Gnaroshi identity

- warm neutral field
- deep ink hierarchy
- restrained research green
- rare teal/orange cue
- square, angular and controlled edge

### 6. Mandatory finishing contract

- image generation output은 base layer일 수 있음
- final raster에는 verified typeset text, arrow, operator와 time index를 합성
- blank label과 pseudo-text는 final에서 금지

### 7. Negative constraints

해당 figure에서 반복되기 쉬운 semantic, composition과 style failure를 구체적으로 쓴다.

### 8. Output

- PNG
- aspect ratio and pixel size
- target paper width
- background
- candidate ID

Technical prompt에 camera angle, cinematic light, believable material, foreground/background depth 같은 scene language를 넣지 않는다.

## Permanent negative constraints for technical figures

- 3D cube, portal, rail, pipe, tank, clamp, motor or machine assembly
- faceted crystal feature or latent
- wavy ribbon used as unexplained state
- glowing chamber or energy flow
- isometric pipeline or dashboard
- pseudo-industrial cutaway
- game HUD or sci-fi control panel
- miniature diorama
- glossy toy-like 3D
- blank title plate or empty annotation box
- missing module label, time index or operator
- pseudo-text, misspelled term or random glyph
- generic corporate infographic
- equal rounded cards
- default royal-blue technical palette
- generic robot-head, brain, lock, sparkle or circuit icon
- floating holographic UI
- decorative wire or circuit background
- blur-heavy shadow, glassmorphism or bevel
- full-image pixel art or bitmap typography
- pasted mascot or logo watermark
- fake benchmark frame, result, graph, screen or terminal output
- arrow added only to fill whitespace
- invented mean, merge, gating, residual or recurrence
- action edge routed to future inputs without verified transition
- wording replaced by an unapproved synonym
- `Ours` smaller than secondary context
- introduction figure containing the full implementation graph

## Review workflow

### 1. Semantic review before aesthetic review

Figure에서 다음을 추출해 evidence map과 line-by-line으로 대조한다.

- all visible labels and wording
- every arrow start, end, direction and meaning
- every operator and merge/split
- every time and state index
- each module input and output
- frozen, shared, detached, trainable and loss status
- real versus illustrated image boundary

Semantic error 하나라도 있으면 candidate를 reject하고 styling review로 넘기지 않는다.

### 2. Figure-role review

- Introduction에서 one-sentence claim이 가장 먼저 보이는가?
- `Ours`가 면적, position과 contrast에서 dominant한가?
- Method detail이 introduction overview를 압도하지 않는가?
- Panel들이 논리적으로 연결되는가?

### 3. Text review

- Required label이 모두 실제로 있는가?
- Blank plate, pseudo-text와 spelling error가 없는가?
- Paper size에서 읽히는가?
- Wording이 current authority와 정확히 일치하는가?

### 4. Two-second and thumbnail review

Adjacent copy 없이 broad subject, main contribution과 reading direction이 보이는지 확인한다.

### 5. Full-resolution craft review

Overlap, clipping, duplicated object, impossible geometry, noisy edge, residual generated text와 inconsistent line weight를 확인한다.

### 6. Gnaroshi comparison

Target site의 current render와 approved identity reference를 나란히 둔다.

- Warm neutral, deep ink와 limited accents가 유지되는가?
- Identity가 mascot이나 반복된 3D object가 아니라 hierarchy와 spacing에서 보이는가?
- Generic AI/PowerPoint/game artwork로 보이지 않는가?
- Subject가 identity decoration보다 먼저 보이는가?

### 7. Scale and accessibility review

- expected single- or double-column size
- 160 px thumbnail
- grayscale
- contrast
- color-blind-safe distinction
- EN/KO longest label

### 8. Owner review

Generated candidate는 owner approval 전에는 final publication asset로 승격하지 않는다. Side-by-side code comparison은 owner가 요청했을 때만 추가한다.

## Automatic rejection

다음 중 하나라도 있으면 점수와 무관하게 reject한다.

- Implementation evidence와 다른 arrow, operator, time relation 또는 module input
- Required technical text가 없거나 blank box로 남아 있음
- Pseudo-text 또는 승인되지 않은 wording
- Technical computation을 3D object나 pseudo-machine으로 표현
- Main contribution 또는 `Ours`가 supporting context보다 작음
- Introduction figure가 복잡한 full architecture dump로 보임
- Generated benchmark image나 fake result를 evidence처럼 사용
- Final paper size에서 label이나 arrow direction을 읽을 수 없음

## Visual scoring after the semantic gate

Semantic gate를 통과한 candidate만 0–5로 평가한다.

| Dimension | Gate |
| --- | --- |
| One-sentence message clarity | 4 이상 |
| Main-contribution hierarchy | 4 이상 |
| Text readability | 4 이상 |
| Gnaroshi distinctiveness | 4 이상 |
| Scientific credibility | 4 이상 |
| Craft and restraint | 4 이상 |
| Crop and grayscale resilience | 4 이상 |

Numeric pass는 owner approval을 대신하지 않는다.

## Deliverables

- verified full-resolution PNG
- expected paper-size preview
- 160 px thumbnail
- grayscale preview
- exact text inventory
- final generation/editing prompt
- candidate ID
- reference package 목록
- inspected branch, commit과 dirty state
- implementation evidence map
- code/document/wording mismatch
- real image provenance
- alt text draft
- illustration disclosure when applicable
- rejection 또는 limitation note

Code source, code baseline 또는 side-by-side review sheet는 사용자가 함께 요청했을 때만 제공한다.

## Codex invocation

Target repository와 이 guidance를 읽을 수 있는 Codex에는 다음 지시를 사용한다.

> `gnaroshi://index`, `gnaroshi://guides/research`, `gnaroshi://guides/technical-figure-code`, `gnaroshi://guides/scientific-figure-generation`을 먼저 읽어라. 현재 요청이 medium과 산출물 수의 최상위 권한이다. Generated raster가 요청되었으면 이를 primary track으로 사용하고 code version이나 paired review를 자동 추가하거나 guidance conflict라고 주장하지 마라. 이전 figure의 content, layout과 wording을 그대로 재사용하지 말고, 실패한 이전 preview는 rejection reference로만 사용하라. Figure를 introduction, method/architecture, experiment 또는 result로 먼저 분류하고 독자가 기억해야 할 한 문장을 작성하라. 실제 구현을 설명하면 current working tree의 entry point, module signature와 actual call site, config, tests, loss, temporal update와 필요한 runtime trace를 조사해 모든 visible module, arrow, operator, time index, shared/frozen/detached state와 label을 evidence map에 연결하라. Mean/add/concat/gating/residual, module input과 `t`→`t+1` relation을 이름이나 시각적 편의로 추정하지 마라. Introduction figure에서는 main contribution 또는 Ours를 가장 크게 두고 full architecture dump를 만들지 마라. Technical panel은 flat 2D orthographic graphic으로 만들고 feature, latent, operator와 pipeline을 3D cube, portal, rail, pipe, tank, ribbon, machine part 또는 game UI로 표현하지 마라. Final PNG에는 approved module name, input/output, arrow, operator, time index와 필요한 panel title을 actual readable text로 넣어라. Blank label plate와 pseudo-text가 있는 generated base는 deliverable이 아니다. Image model의 text가 틀리면 raster editing 또는 separate typesetting layer로 고쳐 하나의 final PNG로 합성하라. LIBERO 같은 benchmark observation은 real sourced frame만 사용하고 generated substitute를 evidence처럼 넣지 마라. 마지막에 figure의 모든 label, arrow, operator와 time index를 추출해 evidence map과 line-by-line으로 재검증하고 semantic error가 있으면 자동 reject하라.

Repository에 직접 접근할 수 없는 Codex에는 위 지시와 함께 `technical-figure-code.md`의 implementation source bundle을 전달한다.

## Reference basis

- [Nature formatting guide](https://www.nature.com/nature/for-authors/formatting-guide): figure를 clarity와 logical connection에 필요한 만큼만 단순하게 유지하고 unnecessary panel, color와 detail을 피한다.
- [Nature research figure specifications](https://research-figure-guide.nature.com/figures/preparing-figures-our-specifications/): final size에서 readable text, line과 production-quality raster를 확인한다.
- [PLOS Computational Biology — Ten Simple Rules for Better Figures](https://journals.plos.org/ploscompbiol/article?id=10.1371%2Fjournal.pcbi.1003833): message를 먼저 정하고 beauty보다 evidence와 communication을 우선한다.
- [IEEE Author Center — Resolution and Size](https://journals.ieeeauthorcenter.ieee.org/create-your-ieee-journal-article/create-graphics-for-your-article/resolution-and-size/): publication size와 raster resolution을 generation 시작 단계에서 정한다.
- [Octo paper](https://octo-models.github.io/paper.pdf): Figure 1의 broad research story와 Figure 2의 labeled flat architecture를 역할에 따라 분리한 robotics reference다.
- [π0 paper](https://www.physicalintelligence.company/download/pi0.pdf): real robot-task images를 활용하면서 central method message를 concise하게 유지하는 introduction reference다.
- [Diffusion Policy paper](https://diffusion-policy.cs.columbia.edu/diffusion_policy_ijrr.pdf): real observation, mechanism, action trajectory와 result의 역할을 구분하는 robotics reference다.

## Decision log

### 2026-07-19 — Establish the generated-raster track

Generated scientific figure work needs visual hierarchy and authorship beyond a default programmatic diagram.

### 2026-07-20 — Make requested medium authoritative

Generated-raster-only work is a valid primary path. Reading the code guide provides semantic verification rules but does not require a code output, paired result or conflict warning.

### 2026-07-20 — Require a complete semantic text layer

A technical raster without required labels, arrows, time indices and operators is unfinished. Generated text artifacts and blank annotation plates are rejected; exact text is composited and verified before final PNG export.

### 2026-07-20 — Ban pseudo-3D computation

Technical modules, features, latents, operators and pipelines use flat 2D scientific grammar. Portals, cubes, rails, pipes, tanks, ribbons and machine parts are not visual substitutes for implementation semantics.

### 2026-07-20 — Put the contribution before architecture detail

Introduction figures communicate one dominant claim and make `Ours` visually primary. Full architecture, loss and temporal mechanics move to method or appendix figures.

### 2026-07-20 — Bind every visible relation to current implementation

Generated beauty cannot compensate for an incorrect edge, operator, time relation, module input or wording. Semantic review happens before aesthetic scoring.
