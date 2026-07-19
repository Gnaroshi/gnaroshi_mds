# Code-based technical figure guide

## Role

이 guide는 논문, 연구 note와 발표 자료의 기술 도식을 code로 제작해 빠르게 검증하고 반복 export하는 선택적 track이다.

이 track의 우선순위는 다음과 같다.

1. 실제 구현과 기술 관계의 정확성
2. exact text, 수식, 시간축과 connector의 가독성
3. 편집 가능성과 반복 가능한 export
4. paper placement에서의 정보 위계
5. 제한된 시간 안의 usable 결과

Code-based figure는 시각적으로 평범할 수 있다. 정확성과 편집성이 중요한 작업에서 즉시 사용할 수 있는 결과를 제공하지만, 모든 논문 figure의 기본값이나 generated figure의 의무적인 안전망은 아니다.

## Request authority and track selection

현재 사용자 요청이 medium, 산출물 수, 작업 범위와 우선순위의 최상위 권한이다.

- 사용자가 code-based figure를 요청했을 때 이 track으로 제작한다.
- 사용자가 generated raster만 요청했다면 `scientific-figure-generation.md`를 primary track으로 사용한다.
- 사용자가 두 방식을 함께 요청했을 때만 code와 generated 결과를 나란히 만든다.
- 두 guide를 모두 읽는 것은 경계를 이해하기 위한 것이며, 두 결과를 자동으로 만들라는 뜻이 아니다.
- Generated raster 요청을 이 guide와의 충돌로 보고하지 않는다.
- Code version을 “정확성을 위해 반드시 필요하다”는 이유로 임의 추가하지 않는다. 필요하면 사용자에게 선택지로 제안하고, 명시적으로 승인되었을 때만 추가한다.
- 이전 figure의 내용, layout 또는 wording을 그대로 재사용하지 않는다. 기존 artifact는 승인된 reference일 때만 positive source이며, 실패한 artifact는 rejection evidence일 뿐이다.

## Use this track when

- architecture, pipeline, state transition, timing 또는 data flow가 핵심이다.
- label, 수식, 변수, 축 또는 verified technical relationship가 많다.
- 여러 언어, dataset, configuration으로 반복 export해야 한다.
- 실제 값에서 plot을 생성해야 한다.
- editable source와 deterministic reproduction이 필요하다.
- 사용자가 못생겨도 바로 쓸 수 있는 code version을 명시적으로 요청했다.

Concept scene, cover illustration 또는 visual-quality-first raster가 목적이면 이 track으로 자동 전환하지 않는다.

## Figure role before layout

같은 구현도 figure가 놓이는 위치에 따라 보여줄 정보량이 달라진다.

### Introduction overview

Introduction figure는 구현 전체를 압축한 architecture dump가 아니다.

- 독자가 먼저 기억해야 할 한 문장을 정한다.
- main contribution 또는 `Ours`를 가장 큰 면적과 가장 강한 contrast로 둔다.
- baseline, input, output과 evaluation context는 main contribution을 이해하는 데 필요한 만큼만 둔다.
- multipart가 필요하면 논리적으로 연결된 panel만 유지한다.
- loss, tensor shape, auxiliary branch와 세부 training path는 main claim에 필수일 때만 포함한다.
- 한 panel에 두 개 이상의 독립된 reading direction을 넣지 않는다.
- 세부 구현을 설명하려면 별도의 method 또는 architecture figure로 이동한다.

### Method or architecture figure

- 구현상 중요한 module, path, state, loss와 share/freeze relation을 보여줄 수 있다.
- 각 panel은 한 semantic layer에 집중한다. 예: inference path, training objective, temporal schedule.
- 한 panel에서 training과 inference edge를 섞으면 line style 또는 boundary를 명시적으로 분리한다.
- 모든 connector와 operator는 evidence map으로 검증한다.

### Experiment or result figure

- 실제 data, condition, unit, axis와 aggregation을 source에서 확인한다.
- illustration, observation frame와 measured result를 시각적으로 구분한다.
- generated frame이나 임의 숫자를 benchmark evidence처럼 사용하지 않는다.

## Brief inputs

Drawing 전에 다음을 확인한다.

- figure role: introduction, method, architecture, experiment, result 또는 appendix
- 독자가 먼저 알아야 할 한 문장
- figure가 증명하거나 설명할 claim
- 필요한 panel과 각 panel의 독립적인 질문
- target paper, column width, slide 또는 web placement
- target size와 output format
- 언어와 승인된 terminology
- print, grayscale와 accessibility 제약
- 필요한 code, config, test, runtime trace
- 사용할 real screenshot, benchmark frame, photo 또는 plot

Paper-specific module, label, claim 또는 layout을 이 reusable guide의 영구 규칙으로 추가하지 않는다.

## Implementation-grounded source of truth

실제 구현을 설명하는 figure는 대상 repository의 current working tree와 검증 가능한 runtime behavior를 기술 source of truth로 사용한다.

Paper, README와 architecture document는 intent와 public terminology를 제공하지만 current behavior를 자동으로 증명하지 않는다. 반대로 code identifier가 public figure의 최종 wording을 자동으로 결정하지도 않는다. 구현 관계와 public terminology를 각각 검증해 연결한다.

### Implementation source bundle

Repository 전체에 접근할 수 없고 file을 전달해야 한다면 다음을 우선 제공한다.

1. 대상 repository의 `AGENTS.md`
2. current branch, commit SHA와 dirty-state 여부
3. target paper의 current abstract, introduction, method와 figure brief
4. architecture 또는 method document
5. training entry point
6. inference 또는 evaluation entry point
7. figure에 등장할 core module과 interface/type definition
8. default config, paper experiment config와 feature flag
9. input, observation, state, output와 action schema
10. loss, objective, optimizer와 parameter-freezing 설정
11. cache, memory, recurrent state 또는 temporal update logic
12. representative unit, integration 또는 shape test
13. privacy-safe sample input/output, trace 또는 tensor-shape log가 실제 behavior 확인에 필요할 때 해당 artifact
14. figure에서 사용할 승인된 real image와 그 provenance

Codex가 repository를 직접 읽을 수 있으면 file을 복사해 보내는 대신 figure scope와 관련 path를 알려준다. Secret, private dataset, credential, unpublished raw result와 식별 가능한 log는 전달하지 않는다.

### Terminology authority

Figure wording은 다음 순서로 결정한다.

1. 현재 사용자가 이번 작업에서 승인하거나 요구한 wording
2. target paper의 current terminology table, abstract와 method
3. current code의 public identifier, config key와 logged name
4. older draft 또는 이전 figure

이전 생성물이 사용한 표현은 자동으로 승인된 wording이 아니다. 새로운 synonym, marketing phrase 또는 그럴듯한 module name을 만들지 않는다.

User-facing wording과 code symbol이 다르면 둘을 evidence map에서 연결하고 figure에는 승인된 public wording을 사용한다. 불일치가 의미를 바꾸면 조용히 합치지 않고 보고한다.

### Evidence map

Drawing을 시작하기 전에 최소한 다음 표를 만든다.

| Figure element | Verified statement | Producer → consumer | Time/state | Exact operator | Source file and symbol | Test/runtime evidence | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| module, state, edge, label 또는 output | figure가 주장할 사실 | 실제 call/data direction | `t`, `t+1`, init, update 또는 shared state | concat, add, mean, attention, detach, loss 등 | repository-relative path와 symbol | test, trace, shape check 또는 `not observed` | high, medium, low |

Evidence map은 review artifact다. Final figure에 source path를 노출할 필요는 없지만 deliverable과 함께 제공한다.

### Mandatory semantic audit

#### Modules and inputs

- Module 이름만 보고 input을 추정하지 않는다.
- `forward` 또는 equivalent signature와 실제 call site를 함께 확인한다.
- wrapper, preprocessing, feature construction과 config-selected branch를 따라간다.
- 한 module에 여러 input이 들어오면 생략이 figure claim을 바꾸는지 확인한다.
- 이름에 `delta`, `fusion`, `encoder`, `update`가 있다는 이유로 delta-only, mean fusion 또는 recurrent update라고 단정하지 않는다.

#### Arrows and direction

- Arrow 하나는 verified producer에서 verified consumer로 값, state, gradient 또는 supervision이 이동한다는 주장이다.
- 단순한 spatial proximity, 시간 순서 또는 conceptual association에는 arrow를 쓰지 않는다.
- `action_t`에서 `observation_{t+1}`으로 edge를 그리려면 environment transition 또는 feedback path가 figure scope와 code에 명시되어 있어야 한다.
- Current action이 다음 step의 input 전체를 직접 만든 것처럼 보이는 perimeter connector를 사용하지 않는다.
- Bidirectional, recurrent, detached와 supervision edge는 서로 다른 의미로 표시하고 legend에서 정의한다.
- Arrowhead가 없거나 방향을 읽을 수 없는 connector는 사용하지 않는다.

#### Operators and fusion

- `mean`, sum, add, concat, stack, gating, residual, attention, pooling, normalization과 detach는 서로 대체할 수 없다.
- Conv output과 camera feature가 같은 위치로 모인다는 이유로 mean operator를 추가하지 않는다.
- 여러 line이 한 node로 들어가는 것만으로 fusion operator를 암시하지 않는다. Exact operator를 label하거나, 구현상 high-level merge만 확인되었다면 중립적인 boundary로 그린다.
- Loss edge와 forward edge를 같은 arrow style로 그리지 않는다.
- Tensor shape와 dimension은 current config/test로 확인한 값만 표시한다.

#### Time and state

- 모든 `t`, `t+1`, chunk index, refresh interval과 recurrence를 code의 loop 또는 scheduler에 연결한다.
- Observation time, latent time, action time과 target time이 다르면 별도 row 또는 notation으로 분리한다.
- Initialization, full update, cached reuse, sparse refresh와 reset condition을 각각 확인한다.
- Figure를 단순화하더라도 cross-time dependency를 새로 만들거나 실제 dependency를 뒤집지 않는다.

#### Training and inference

- Training path와 inference path를 별도로 추적한다.
- `requires_grad`, optimizer parameter group, detached tensor, evaluation mode와 checkpoint loading을 확인하기 전에는 frozen 또는 trainable로 표시하지 않는다.
- Teacher/student, target/prediction, stop-gradient와 loss target의 방향을 정확히 확인한다.
- Shared module은 object identity, weight reuse 또는 repeated call 중 무엇이 shared인지 명시한다.
- Paper experiment config와 default config가 다르면 figure가 어느 것을 설명하는지 밝힌다.

#### Runtime verification

- Import relation만으로 runtime data flow를 추정하지 않는다.
- Static inspection만으로 dynamic dispatch, optional branch, shape 또는 update frequency를 확정할 수 없으면 focused test, dry run, trace 또는 shape logging을 사용한다.
- Code와 test가 current behavior를 보여주고 document가 다른 내용을 말하면 mismatch를 보고한다.
- 근거가 부족한 element나 connector는 확정해 그리지 않는다. 범위에서 제거하거나 `unverified` review note로 분리한다.

### Real benchmark and observation assets

- LIBERO 같은 benchmark observation은 공식 공개 asset, 재현 가능한 dataset sample 또는 사용자 실행에서 얻은 real frame을 사용한다.
- AI-generated scene를 benchmark observation이나 qualitative result로 대체하지 않는다.
- 나중에 사용자가 편집할 frame이면 별도 asset folder에 원본을 모으고 source URL 또는 dataset version, task/scene, frame index와 usage boundary를 기록한다.
- Figure slot만 먼저 만들 때는 `Primary RGB`, `Wrist RGB`처럼 의미가 명확한 실제 text placeholder를 사용한다. 정체를 알 수 없는 fake thumbnail을 넣지 않는다.

### Required provenance output

Implementation-grounded figure의 review package에는 다음을 포함한다.

- inspected branch와 commit SHA
- dirty-state 여부
- inspected path 목록
- evidence map
- code/document/wording mismatch
- runtime으로 확인하지 못한 부분
- real external asset provenance

## Medium and output

Code-based figure에는 다음을 사용할 수 있다.

- HTML/CSS
- Canvas
- plotting library
- programmatic raster drawing
- document 또는 slide API
- layout와 annotation을 위한 Figma scripting

Mermaid는 관계를 빠르게 검토하는 planning artifact로만 사용한다. Mermaid 기본 render를 publication figure로 제출하지 않는다.

SVG 또는 vector final은 사용자가 명시적으로 요청할 때만 선택한다. 별도 요청이 없으면 editable source와 고해상도 PNG를 제공한다.

Technical architecture는 기본적으로 flat 2D orthographic layout으로 만든다. 실제 3D geometry, spatial trajectory 또는 3D measurement가 연구 대상일 때만 3D representation을 사용한다. Module, tensor, operator와 pipeline을 cube, portal, rail, pipe, tank, machine part 또는 isometric object로 바꾸지 않는다.

## Construction principles

### Solve the argument before styling

먼저 다음 세 수준을 나눈다.

1. thumbnail에서도 보이는 primary argument
2. 짧게 살펴보면 보이는 main structure
3. 가까이 읽을 때 필요한 label, 수식과 annotation

모든 node와 label을 같은 크기, 같은 border와 같은 contrast로 만들지 않는다. `Ours` 또는 main mechanism이 supporting context보다 작으면 hierarchy가 실패한 것이다.

### Use geometry for meaning

- 가까운 요소는 같은 group으로 본다.
- 큰 간격은 단계 또는 역할의 전환을 나타낸다.
- 같은 계층은 common baseline, width 또는 rhythm을 공유한다.
- 중요도가 다르면 면적과 contrast도 달라야 한다.
- Box는 실제 module, state, loss, data group 또는 boundary에만 사용한다.
- 단순한 시간 순서와 비교는 위치, alignment와 번호로 먼저 설명하고 arrow는 verified transfer에만 둔다.

### Keep one reading direction

- pipeline: left to right
- hierarchy: top to bottom
- comparison: aligned rows or columns
- time: one continuous axis
- recurrence: visible initialization, repeat condition and exit

Connector가 교차하면 line routing을 늘리기 전에 node 순서를 바꾼다.

### Group repetition

Time step, shared head, repeated block 또는 동일한 observation을 큰 box로 반복하지 않는다. Rail, bracket, shared band, small multiple, `×N`, aligned column 또는 explicit repeat marker를 사용한다.

### Keep semantic text real

- Module name, time index, operator, axis, legend와 short transition label은 actual typeset text로 넣는다.
- Meaningful label을 비워 둔 채 blank plate 또는 empty title box로 전달하지 않는다.
- Screenshot 또는 generated raster 안의 작은 text에 의미를 의존하지 않는다.
- 수식은 math renderer로 조판한다.
- Caption은 figure의 관계 오류를 보완하는 수단이 아니다.

## Gnaroshi visual system

대상 project의 latest design token과 actual render가 가장 구체적인 source다. 별도 token이 없으면 다음 공통 방향을 사용한다.

### Palette

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

Neutral이 canvas의 대부분을 차지하게 한다. Green은 main path 또는 selected state, teal과 orange는 작은 endpoint, rule, index 또는 corner에 제한한다. Generic royal blue를 기술적인 느낌을 내기 위한 기본색으로 사용하지 않는다.

### Typography

- 제목과 label은 system sans-serif를 사용한다.
- 변수, short index와 metadata만 system monospace를 사용할 수 있다.
- Sentence case를 기본으로 한다.
- Final placement에서 일반 label이 약 8 pt 아래로 내려가지 않게 한다.
- Condensed type, outline type, bitmap font와 과도한 bold를 피한다.

### Shape and spacing

- Square 또는 restrained small-radius corner를 사용한다.
- 1–2 px divider와 2 px strong edge를 일관되게 사용한다.
- Blur shadow, bevel, glass, extrusion과 material highlight를 사용하지 않는다.
- Rounded card grid, pill badge와 nested dashboard를 만들지 않는다.
- Whitespace로 먼저 group을 만들고 필요할 때 divider를 추가한다.
- Equal-width panel을 자동으로 만들지 않는다. Main contribution에 더 많은 면적을 준다.
- Panel letter는 publication navigation으로 작게 둔다.
- Caption을 반복하는 boxed slogan을 figure 아래에 만들지 않는다.

## Workflow

### 1. Confirm the requested track and role

Code result이 실제로 요청되었는지 확인하고 introduction, method, architecture 또는 result 중 하나로 분류한다.

### 2. Inspect implementation and terminology

Source bundle을 읽고 current implementation, current paper wording와 mismatch를 기록한다.

### 3. Build the evidence map

Module뿐 아니라 모든 connector, operator, time index, share/freeze state와 visible label을 표에 넣는다.

### 4. Write the one-sentence argument

독자가 figure를 보고 기억해야 할 한 문장을 쓴다. Introduction figure가 이 문장을 넘어서 여러 독립적 이야기를 담으면 범위를 줄인다.

### 5. Low-detail layout

Gray block과 line만으로 reading order, panel weight, density와 focal point를 확인한다. Main contribution의 면적을 먼저 확보한다.

### 6. First semantically complete render

전체 label, math, connector, time index와 real image slot이 보이는 첫 PNG를 만든다. Blank label, pseudo-text와 미검증 edge가 있으면 styling으로 넘어가지 않는다.

### 7. Line-by-line semantic red team

Figure에서 다음 항목을 모두 추출해 evidence map과 대조한다.

- 모든 arrow의 start, end, direction과 meaning
- 모든 merge/split 지점의 exact operator
- 모든 `t`, `t+1`, chunk와 refresh notation
- 모든 module의 actual inputs와 outputs
- 모든 frozen, trainable, shared, detached와 loss 표시
- 모든 public wording과 abbreviation
- `Ours`의 claimed scope와 visual dominance

하나라도 틀리면 visual polish 전에 수정한다.

### 8. Gnaroshi pass

Typography hierarchy, warm neutral field, square edges, restrained green과 작은 teal/orange cue를 적용한다. Identity를 만들기 위해 box, icon 또는 decoration을 늘리지 않는다.

### 9. Reduction and scale verification

없어도 argument나 판단이 달라지지 않는 border, arrow, icon과 caption-like copy를 제거한다.

다음 크기로 확인한다.

- working size
- expected single- or double-column placement
- 160 px thumbnail
- grayscale

EN/KO variant가 있으면 longest label과 line break를 실제로 render한다.

## Automatic rejection

다음 중 하나라도 있으면 code baseline으로도 reject한다.

- Figure의 required semantic label이나 panel title이 비어 있다.
- Evidence가 없는 arrow, operator, time dependency 또는 module input이 있다.
- Action과 next observation의 관계가 실제 environment/data flow와 다르게 그려졌다.
- Add, mean, concat, pooling, gating 또는 residual이 code와 다르다.
- Training과 inference path가 구분되지 않아 다른 동작으로 읽힌다.
- Current user wording을 임의의 새 표현으로 바꿨다.
- Main contribution 또는 `Ours`가 supporting path보다 작거나 약하다.
- Introduction figure가 full architecture, loss와 evaluation schedule을 한꺼번에 보여준다.
- Module, feature 또는 operator를 3D cube, portal, pipe, rail, tank나 pseudo-machine으로 표현한다.
- Fake benchmark image, fake result, pseudo-code 또는 pseudo-text를 사용한다.
- Paper size에서 text, arrowhead 또는 dashed line을 읽을 수 없다.

## Minimum acceptance

- Figure의 한 문장 argument가 2초 안에 보인다.
- Text, math, time index와 operator가 선명하고 정확하다.
- Label, connector와 image가 겹치거나 잘리지 않는다.
- Main path와 supporting path가 grayscale에서도 구분된다.
- 모든 visible connector와 technical claim이 evidence map entry를 가진다.
- Exact wording이 current terminology authority와 일치한다.
- Introduction figure는 main contribution이 가장 크고 세부 구현은 억제되어 있다.
- Real benchmark frame과 generated illustration의 경계가 명확하다.
- Export가 deterministic하거나 같은 source에서 다시 만들 수 있다.

## Deliverables

- editable source
- high-resolution PNG
- expected paper-size preview
- 160 px thumbnail
- grayscale preview
- 사용한 font와 external asset 목록
- inspected branch, commit과 dirty state
- inspected path 목록
- implementation evidence map
- code/document/wording mismatch
- runtime으로 확인하지 못한 부분
- real image provenance
- 알려진 visual limitation

Generated candidate 또는 side-by-side review는 사용자가 함께 요청했을 때만 deliverable에 추가한다.

## Codex invocation

Target repository와 이 guidance를 읽을 수 있는 Codex에는 다음 지시를 사용한다.

> `gnaroshi://index`, `gnaroshi://guides/research`, `gnaroshi://guides/technical-figure-code`, `gnaroshi://guides/scientific-figure-generation`을 먼저 읽어라. 현재 요청이 medium과 산출물 수의 최상위 권한이다. Code-based figure가 명시적으로 요청되지 않았다면 code version이나 paired review를 자동 추가하지 마라. 이전 figure의 content, layout과 wording을 그대로 재사용하지 말고, current user wording과 target repository의 current working tree를 조사하라. Training/inference entry point, core module의 signature와 actual call site, schema, config, loss, state update, optimizer/freezing, tests와 필요한 runtime trace를 확인하라. 모든 visible module, arrow, operator, time index, shared/frozen/detached state와 label마다 source file, symbol, producer→consumer, verification state를 기록한 evidence map을 drawing 전에 작성하라. Mean/add/concat/gating/residual 같은 operator와 `t`→`t+1` dependency를 이름이나 모양으로 추정하지 마라. Introduction figure라면 한 문장 claim과 main contribution을 가장 크게 두고 full architecture dump를 만들지 마라. Technical pipeline은 flat 2D로 그리고 module이나 feature를 3D cube, portal, pipe, rail 또는 machine part로 표현하지 마라. Required label을 blank box로 남기지 말고 actual typeset text로 넣어라. 마지막에 모든 arrow, operator, time index와 wording을 figure에서 추출해 evidence map과 line-by-line으로 다시 대조하라. 근거가 없는 관계는 그리지 말고 code/document mismatch와 미검증 항목을 보고하라.

Repository에 직접 접근할 수 없는 Codex에는 위 지시와 함께 `Implementation source bundle`의 file을 전달한다.

## Reference basis

- [Nature formatting guide](https://www.nature.com/nature/for-authors/formatting-guide): clarity와 단순성을 유지하고 불필요한 panel, color와 detail을 제거한다.
- [Nature research figure specifications](https://research-figure-guide.nature.com/figures/preparing-figures-our-specifications/): final size에서 readable text와 production-quality export를 검증한다.
- [PLOS Computational Biology — Ten Simple Rules for Better Figures](https://journals.plos.org/ploscompbiol/article?id=10.1371%2Fjournal.pcbi.1003833): message를 먼저 정하고 figure를 실제 data 또는 model과 연결한다.
- [IEEE Author Center — Resolution and Size](https://journals.ieeeauthorcenter.ieee.org/create-your-ieee-journal-article/create-graphics-for-your-article/resolution-and-size/): intended publication size와 raster resolution을 처음부터 고려한다.
- [Octo paper](https://octo-models.github.io/paper.pdf): overview와 architecture의 정보량을 분리하고, architecture를 text, token group과 arrow가 있는 flat technical graphic으로 설명하는 robotics reference다.
- [π0 paper](https://www.physicalintelligence.company/download/pi0.pdf): introduction figure에서 real robot-task evidence와 concise central method story를 결합하는 reference다.
- [Diffusion Policy paper](https://diffusion-policy.cs.columbia.edu/diffusion_policy_ijrr.pdf): method mechanism, observation, trajectory와 result를 역할별로 분리하는 robotics reference다.

## Decision log

### 2026-07-19 — Establish the optional code track

Code-based technical figures prioritize correctness, editability, reproducibility, and immediate use. Visual plainness is acceptable when disclosed.

### 2026-07-20 — Make the current request authoritative

Reading both figure guides does not authorize automatic paired output. Generated-raster-only and other explicit medium requests take precedence; a code result is produced only when requested.

### 2026-07-20 — Require edge-level implementation evidence

Every visible arrow, operator, time dependency, module input, training state and technical label must be traced to current code, configuration, tests or focused runtime evidence. Module names are not evidence of their inputs or behavior.

### 2026-07-20 — Separate introduction compression from architecture completeness

An introduction figure communicates one main contribution with dominant visual hierarchy. Detailed architecture, objective and temporal mechanics move to method or appendix figures instead of being compressed into a crowded overview.

### 2026-07-20 — Reject pseudo-3D computation

Technical modules, tensors, operators and pipelines remain flat and auditable. Three-dimensional objects are reserved for actual spatial data, physical geometry or apparatus, not used as decorative computation metaphors.
