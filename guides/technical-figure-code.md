# Code-based technical figure guide

## Purpose

이 guide는 논문, 연구 note와 발표 자료에 바로 넣을 수 있는 기술 도식의 baseline을 빠르게 만드는 규칙이다.

이 track의 우선순위는 다음과 같다.

1. 기술 관계와 표기의 정확성
2. 편집 가능성
3. 반복 가능한 export
4. 논문 크기에서의 가독성
5. 제한된 시간 안의 완료

Code baseline은 시각적으로 평범할 수 있다. 이를 숨기지 않는다. 이 track은 최종 art direction을 대신하는 것이 아니라, 연구자가 당장 사용할 수 있는 안전한 결과와 비교 기준을 제공한다.

## Paired review contract

사용자가 한 track만 요청하지 않았다면 다음 두 결과를 함께 준비한다.

- 이 guide를 따르는 `Code baseline`
- `scientific-figure-generation.md`를 따르는 `Generated candidate`

두 결과를 같은 review sheet 또는 같은 응답에서 나란히 보여준다. Code baseline은 정확성, 편집성, 가독성으로 평가하고 generated candidate는 시각적 위계, 조형, Gnaroshi distinctiveness와 완성도로 평가한다.

Code baseline이 generated candidate를 흉내 내기 위해 복잡한 장식 code를 누적하지 않는다. Generated candidate가 code baseline처럼 모든 관계를 작은 box와 arrow로 설명하도록 강제하지 않는다.

Hybrid 작업은 두 결과를 실제 크기로 비교한 뒤 선택한다.

## Use this track when

- label, 수식, 변수, 축 또는 관계가 많다.
- architecture, pipeline, state transition, timing 또는 data flow가 핵심이다.
- 수정 가능성과 재현성이 중요하다.
- 여러 언어나 여러 dataset으로 반복 export해야 한다.
- 실제 값에서 plot을 생성해야 한다.
- 제출 또는 검토 시점이 가까워 즉시 사용할 수 있는 결과가 필요하다.

Concept scene, cover illustration, visual metaphor 또는 정교한 editorial artwork가 목적이면 이 track만으로 끝내지 않는다.

## Inputs

작업 brief에서 다음을 확인한다.

- figure의 목적
- 독자가 먼저 알아야 할 한 문장
- figure family: architecture, pipeline, workflow, comparison, plot, apparatus, hybrid
- 필요한 concept, 관계, 수식 또는 data
- 언어
- single-column, double-column, slide 또는 web placement
- target size와 output format
- print, grayscale, accessibility 제약
- 사용 가능한 screenshot, photo, plot 또는 reference

이 guide에는 paper-specific module, label, claim 또는 layout을 영구 규칙으로 추가하지 않는다.

## Medium selection

Code-based figure에는 다음을 사용할 수 있다.

- HTML/CSS
- Canvas
- plotting library
- programmatic raster drawing
- document 또는 slide API
- layout와 annotation을 위한 Figma scripting

Mermaid는 관계를 빠르게 확인하는 planning artifact로만 사용한다. Mermaid 기본 render를 publication figure로 제출하지 않는다.

SVG 또는 vector final은 사용자가 명시적으로 요청할 때만 선택한다. 별도 요청이 없으면 review output은 고해상도 PNG로 제공한다.

## Construction principles

### Solve hierarchy before styling

먼저 다음 세 수준을 나눈다.

1. thumbnail에서도 보이는 primary argument
2. 짧게 살펴보면 보이는 main structure
3. 가까이 읽을 때 필요한 label, 수식과 annotation

모든 node와 label을 같은 크기와 같은 border로 만들지 않는다.

### Use geometry for meaning

- 가까운 요소는 같은 group으로 본다.
- 큰 간격은 단계 또는 역할의 전환을 나타낸다.
- 같은 계층은 common baseline, width 또는 rhythm을 공유한다.
- 중요도가 다르면 면적과 contrast도 달라야 한다.
- box는 실제 module, state, loss, data group 또는 boundary에만 사용한다.
- 단순한 순서는 위치와 번호로 먼저 설명하고 arrow는 필요한 곳에만 둔다.

### Prefer a clear reading direction

- pipeline: left to right
- hierarchy: top to bottom
- comparison: aligned rows or columns
- time: one continuous axis
- recurrence: visible start, repeat condition, and exit

한 figure에서 reading direction을 반복해서 바꾸지 않는다. Connector가 교차하면 node 순서를 먼저 바꾼다.

### Group repetition

Time step, shared head, repeated block 또는 동일한 observation을 큰 box로 반복하지 않는다. Rail, bracket, shared band, small multiple, `×N`, aligned column 또는 explicit repeat marker를 사용한다.

### Keep text real

Label과 수식은 raster image 안에 생성하지 않는다. 가능한 한 real text와 math renderer를 사용한다. 작은 screenshot 안의 text가 의미를 전달해야 하면 별도 callout으로 다시 표기한다.

## Gnaroshi baseline styling

대상 project의 최신 design token과 실제 render가 가장 구체적인 source다. 별도 token이 없으면 다음 공통 방향을 사용한다.

### Shared palette

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

Neutral이 canvas의 대부분을 차지하게 한다. Green은 main path 또는 selected state에 사용하고 teal과 orange는 작은 endpoint, rule, index 또는 corner에 제한한다.

Generic royal blue를 기술적인 느낌을 내기 위한 기본색으로 사용하지 않는다. 별도 information family가 필요할 때만 supporting color를 추가한다.

### Typography

- 제목과 label은 system sans-serif를 사용한다.
- 변수, short index와 metadata만 system monospace를 사용할 수 있다.
- 수식은 math renderer로 조판한다.
- sentence case를 기본으로 한다.
- final placement에서 일반 label이 약 8 pt 아래로 내려가지 않게 한다.
- condensed type, outline type, bitmap font와 과도한 bold를 피한다.

### Shape

- square corner를 기본으로 한다.
- 1–2 px divider와 2 px strong edge를 일관되게 사용한다.
- blur shadow를 사용하지 않는다.
- 한 개의 focal element에만 짧은 hard offset shadow를 사용할 수 있다.
- rounded card grid, pill badge와 nested card를 만들지 않는다.
- pixel grammar는 2 px corner, marker 또는 selected boundary에만 적용한다.

### Layout

- equal-width panel을 기본값으로 삼지 않는다.
- 중요하거나 복잡한 부분에 더 많은 면적을 준다.
- whitespace로 먼저 group을 만들고 필요할 때 divider를 추가한다.
- panel letter는 publication navigation으로 작게 둔다.
- caption을 반복하는 boxed slogan을 figure 아래에 만들지 않는다.

## Workflow

### 1. Semantic map

Figure brief를 node, relationship, group, sequence, comparison, state와 annotation으로 정리한다.

### 2. Low-detail layout

Text와 color를 다듬기 전에 gray block과 line만으로 reading order, group, density와 focal point를 확인한다.

### 3. First usable render

최소 style로 전체 label, math, connector와 data가 보이는 첫 PNG를 만든다. 이 단계에서 design polishing보다 clipping, overlap, missing glyph와 관계 오류를 먼저 확인한다.

### 4. Gnaroshi pass

Typography hierarchy, warm neutral field, square edges, restrained green과 작은 teal/orange cue를 적용한다. 시각 identity를 만들기 위해 box 수나 장식을 늘리지 않는다.

### 5. Reduction

없어도 reading order나 판단이 달라지지 않는 border, arrow, icon, caption-like copy와 accent를 제거한다.

### 6. Scale verification

다음 크기로 render를 확인한다.

- working size
- expected paper placement
- 160 px thumbnail
- grayscale

EN/KO variant가 있으면 longest label과 line break를 실제로 render한다.

### 7. Export

제공 항목:

- editable source
- high-resolution PNG
- paper-size preview
- 160 px thumbnail
- grayscale preview
- 사용한 font와 external asset 목록
- 알려진 visual limitation

## Minimum acceptance

다음 조건을 모두 만족하면 즉시 사용 가능한 baseline으로 간주한다.

- text와 math가 선명하다.
- label, connector와 image가 겹치거나 잘리지 않는다.
- reading order가 한눈에 보인다.
- main path와 supporting path가 color 없이도 구분된다.
- arrowhead와 dashed line이 paper size에서 보인다.
- figure의 가장 중요한 부분이 다른 부분보다 강하다.
- screenshot이나 generated raster 안의 작은 text에 의미를 의존하지 않는다.
- export가 deterministic하거나 같은 source에서 다시 만들 수 있다.
- figure가 정확하더라도 시각적으로 평범하면 그 limitation을 명시한다.

## Failure modes

- 모든 개념을 동일한 rounded box로 표현
- equal-panel PowerPoint template
- royal-blue border와 green fill의 자동 조합
- arrow가 text와 box를 관통
- 긴 perimeter connector
- 반복된 shared module card
- generic lock, brain, robot-head, sparkle 또는 circuit icon
- caption을 반복하는 하단 summary box
- code generator의 기본 font와 기본 color를 그대로 사용
- polish를 시도하며 DOM, coordinate 또는 drawing code만 복잡해짐
- technically complete하지만 thumbnail에서 argument가 보이지 않음

## Stop rule

Code baseline이 minimum acceptance를 통과하면 usable 상태로 고정한다. 시각 완성도를 높이기 위해 끝없이 code를 덧붙이지 않는다. 더 강한 조형이 필요하면 generated candidate 또는 별도의 art-direction 작업으로 이동한다.

## Decision log

### 2026-07-19 — Establish the usable baseline track

Code-based technical figures are an explicit fast track. They prioritize correctness, editability, reproducibility, and immediate use. Visual plainness is acceptable when it is disclosed rather than mistaken for a polished final direction.

### 2026-07-19 — Reject code as the universal answer

Programmatic drawing is not the default solution for visual-quality-first figure work. A code baseline and a generated candidate should be reviewed together when both speed and visual quality matter.
