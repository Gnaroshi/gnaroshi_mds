# 기술 도식과 데이터 plot

Architecture, pipeline, state, operator, 시간 관계와 데이터 plot에 적용한다. [공통 figure 규칙](research-figures.md)의 역할·크기·시각 기준을 따른다. Code, Figma, slide tool, canvas 또는 raster editor로 구성할 수 있으며, 정확성·실제 text·편집 가능성·재현 가능한 export를 우선한다.

## 구현 근거

구현을 설명하는 figure는 대상 repository의 current working tree와 필요한 runtime evidence를 기준으로 만든다. Paper와 문서는 intent·공개 terminology의 근거이며 실제 동작은 코드·설정·테스트로 확인한다.

제작 전에 다음을 조사한다.

- 대상 `AGENTS.md`, branch, commit, dirty state
- 현재 abstract·introduction·method, figure brief와 architecture 문서
- Training, inference/evaluation entry point, core module signature와 실제 call site
- Input·state·output·action schema, default/experiment config와 feature flag
- Loss, optimizer parameter group, checkpoint와 freezing/detach 설정
- Cache·memory·recurrent state의 초기화, 갱신·재사용·reset 경계
- Unit/integration/shape test와 필요한 privacy-safe sample·trace

직접 접근할 수 없는 경우에만 필요한 source bundle을 받는다. Secret, 식별 가능한 log와 private dataset을 공개 review package에 넣지 않는다. Import나 module 이름만으로 동작을 추정하지 않는다.

## 용어

1. 현재 사용자가 승인·요구한 wording
2. Target paper의 current terminology, abstract와 method
3. Current code의 public identifier, config key와 logged name
4. 의미를 다시 검증한 이전 draft

새 synonym이나 그럴듯한 module 이름을 만들지 않는다. 공개 wording과 code symbol이 다르면 아래 evidence map에서 연결한다. 불일치가 의미를 바꾸면 보고한다.

## Evidence map

모든 visible module, input/output, connector, operator, time index, training state와 technical label을 제작 전에 연결한다. 데이터 plot은 데이터 source·조건·변환·집계 근거를 기록한다.

| Figure element | Verified statement | Producer → consumer | Time/state | Exact operator | Source file and symbol/data | Test/runtime evidence | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Module·edge·label·output | 그림이 주장할 사실 | 실제 전달 방향 | 시간·초기화·갱신·공유 상태 | 실제 연산 | Repository-relative path와 symbol 또는 데이터 출처 | Test·trace·shape check 또는 `not observed` | high / medium / low |

근거 없는 관계는 확정해 그리지 않는다. 범위에서 제외하거나 review note에 `unverified`로 기록한다. Evidence map은 결과와 함께 제공하며 figure 안에 source path를 표시할 필요는 없다.

## 의미 검증

### Module과 input

- Signature와 실제 call site를 함께 추적하고 wrapper, preprocessing, feature construction과 config-selected branch를 확인한다.
- 여러 input 중 일부를 생략할 때 claim이 바뀌지 않는지 확인한다. `delta`, `fusion`, `encoder`, `update`라는 이름은 입력이나 연산의 증거가 아니다.

### Arrow와 operator

- Arrow는 producer에서 consumer로 값·state·gradient·supervision이 전달된다는 주장이다. 단순한 근접·시간 순서는 위치·번호·alignment로 표현한다.
- `action_t → observation_{t+1}`은 environment transition 또는 feedback이 scope와 구현에서 확인될 때만 그린다. Action이 다음 input 전체를 직접 만드는 것처럼 연결하지 않는다.
- 양방향·재귀·detach·supervision과 forward edge의 의미를 line style·legend로 구분하고 방향을 읽을 수 있는 arrowhead를 사용한다.
- Mean, sum/add, concat, stack, gating, residual, attention, pooling, normalization과 detach를 정확히 구분한다. 여러 선이 모인다는 이유로 fusion 연산을 합성하지 않는다.
- High-level merge만 확인되면 중립 boundary를 사용한다. Shape와 dimension은 current config/test로 확인한 값만 표시한다.

### 시간·학습 상태

- `t`, `t+1`, chunk, refresh interval과 recurrence를 실제 loop/scheduler에 연결한다. Observation·latent·action·target의 시점이 다르면 분리한다.
- Initialization, full update, cached reuse, sparse refresh와 reset을 구분한다. 단순화로 cross-time dependency를 새로 만들거나 뒤집지 않는다.
- Training과 inference를 각각 추적한다. `requires_grad`, optimizer group, detach, evaluation mode와 checkpoint를 확인한 뒤 frozen/trainable을 표시한다.
- Teacher/student, target/prediction, stop-gradient와 loss 방향을 확인한다. Shared는 object identity, weight reuse, repeated call 중 무엇인지 명시한다.
- Default와 paper experiment config가 다르면 설명 대상 config를 기록한다.

### Runtime

- Static inspection으로 dynamic dispatch, optional branch, shape와 갱신 주기를 확인할 수 없으면 focused test, dry run 또는 trace를 사용한다.
- Code·test·문서 간 불일치와 runtime에서 관측하지 못한 범위를 기록한다.

## Representation-space plot

- PCA 축에는 PC 번호, 설명 분산과 압축한 대상의 의미를 표시한다. 가까운 점은 표시된 부분 공간에서 가깝다는 뜻이며 생략한 차원·행동·성공률의 동일성을 뜻하지 않는다.
- 정규화, 중심화, pooling, token mask와 projection fit 범위를 기록한다. 공통 좌표 비교에는 공통 축을 fit하며, 별도로 fit한 공간의 이동량을 직접 비교하지 않는다.
- Cosine similarity는 원래 비교 벡터에서 계산한다. 1·0·−1의 방향 의미, 크기를 무시한다는 점, similarity와 `1−cosine` distance의 label·범위를 구분한다.
- Condition, model output과 실제 실행 command를 구분한다. Prediction horizon, policy query와 environment step의 시간 단위를 보존한다.
- 공유 관측 replay와 독립 rollout을 구분한다. 독립 rollout의 같은 step에는 관측 차이가 포함된다. 종료 경로를 복제해 비교 값을 채우지 않고 실제 평가 결과로 성공·실패를 분류한다.

## 구성과 검증 순서

1. Brief와 evidence map을 완성한다.
2. Gray block과 선으로 reading order, panel별 면적과 main contribution의 위계를 정한다.
3. 모든 label·수식·connector·time index를 실제 text로 넣어 첫 render를 만든다.
4. Render의 각 arrow 시작·끝·방향, merge/split 연산, 시간, input/output, share/freeze/detach, wording을 evidence map과 대조한다.
5. 의미가 맞으면 typography·간격·grouping·대비를 개선한다. Polish 중 topology와 wording을 임의로 바꾸지 않는다.
6. [공통 최종 검토](research-figures.md#최종-검토)와 최종 physical size 검증을 수행한다.

- Pipeline은 좌→우, hierarchy는 위→아래, comparison은 정렬된 행·열, time은 연속 축으로 구성한다. 한 panel의 reading direction을 일관되게 유지한다.
- Connector가 교차하면 routing을 늘리기 전에 node 순서를 바꾼다. Box는 module·state·loss·data group·boundary에만 사용한다.
- 반복 step과 shared head는 bracket, band, small multiple, `×N`으로 묶는다. 재귀는 초기화·반복·종료 조건을 표시한다.
- 수식은 math renderer로 조판하고 editable text/layer를 유지한다. Caption으로 관계 오류를 보완하지 않는다.
- Mermaid 기본 render는 관계 검토용으로만 쓰고 publication figure로 제출하지 않는다.
- Baseline과 polished final을 함께 요청한 경우 같은 배치에서 비교하고 topology·wording 일치 여부를 기록한다.

## 결과

- 요청한 final format과 재생성 가능한 editable source
- 사용한 font·asset·데이터 출처
- 구현 figure의 inspected branch·commit·dirty state·path와 evidence map
- Code/document/wording mismatch, 미검증 runtime 범위와 알려진 visual limitation

Preview·thumbnail·grayscale은 검증에 사용한다. 별도 제출 여부와 결과 수는 현재 요청을 따른다.
