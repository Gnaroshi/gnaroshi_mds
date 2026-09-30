# Research guidance

## Source of truth

- 논문 note, reading evidence, implementation attempt, review와 recall record의 canonical owner를 명시한다.
- PDF, credential, private review export와 개인 원문은 public repository에 올리지 않는다.
- public output은 명시적으로 선택한 field만 schema validation 후 별도 feed로 publish한다.
- slug, identifier, provenance와 visibility를 안정적으로 유지한다.

## Workflow

1. 수집하거나 queue에 등록한다.
2. 읽기 pass와 질문을 기록한다.
3. 주장과 근거, 출처, 읽은 시점을 분리해 남긴다.
4. 구현 또는 재현 결과를 논문 record와 연결한다.
5. review/recall로 이해도를 검증한다.
6. 공개 가능한 field만 의도적으로 publish한다.

## Safety and evidence

- 원본 삭제·덮어쓰기나 공개 범위 변경처럼 실제 위험이 있는 작업에는 대상과 영향을 먼저 검증한다. 이미 승인된 일상 작업에 일괄적인 dry-run, `--apply`, 반복 확인을 요구하지 않는다.
- seed, demo, 빈 record, generated fixture를 실제 연구 활동으로 집계하지 않는다.
- 관측값, 추론, 의견을 구분한다.
- 실패와 미완료 상태를 숨기지 않는다.
- 자동 생성 report는 artifact이며 장기 지침 문서가 아니다.

## Training execution and explanation

- 학습 실행은 가장 최근의 사용자 요청을 따른다. 명령만 요청하면 직접 실행하지 않고, 이후 실행을 요청하면 이전의 명령 제공 선호를 이유로 멈추지 않는다. tmux pane별 명령은 각 pane에 붙여 넣을 완결된 형태로 준다. 요청 없이 계속 상태를 조회·대기하지 않는다.
- 실행 준비에는 필요한 짧은 검증만 포함한다. 긴 학습의 완료를 기다리며 대화를 점유하지 않고, 사용자가 결과 확인이나 모니터링을 요청했을 때 해당 범위만 확인한다.
- 전체 데이터 학습·평가를 요청하면 소규모 시험이나 일부 표본으로 대신하지 않는다. 전체 train/test 범위와 제외 기준을 명시하고, 짧은 시험은 본 실행 전 확인에만 사용한다. 전체 실행이 어려우면 축소 실행을 완료 결과로 제시하지 말고 이유와 미완료 범위를 알린다.
- 사용자가 열어 둔 tmux의 살아 있는 pane을 보존한다. 지정한 pane 안에서 작업을 실행하고 완료 뒤에도 shell이 남도록 한다. pane 정리를 요청하면 종료가 확인된 pane만 정리하며, 살아 있는 pane을 닫거나 교체하지 않는다.
- 모델 이름만 적지 않는다. 가져온 모델의 출처와 checkpoint, 공개된 기존 학습 이력, 이번 실험에서 추가로 학습하는 데이터와 목표를 구분해 설명한다. 공개되지 않은 이력은 추정하지 않는다.
- `학습 전`은 무엇을 추가로 학습하기 전인지 명시한다. 비교 조건은 처음 등장할 때 입력 데이터, 생성 방법과 학습 여부를 짧게 정의하고, 뜻을 설명하지 않은 별칭만으로 결과를 제시하지 않는다.
- 실험을 확대하거나 수정할 때 사용자가 요청한 비교 조건을 다른 방법으로 조용히 대체하지 않는다. 방법·데이터 범위·평가 방식이 바뀌면 별도 실험으로 이름과 대응 관계를 기록하고, 원래 요청에서 아직 실행하지 않은 범위를 명시한다. 같은 별칭을 다른 뜻으로 재사용할 때도 차이를 먼저 설명한다.
- 결과에는 비율과 함께 맞힌 수·전체 수를 적고, 문항 수·교란 입력 수·학습 반복으로 처리한 입력 수를 구분한다. 방법을 예시로 설명할 때는 실제 입력·추가 문장·모델 답을 함께 보여 주고, 실제 기록과 가상 예시를 구분한다.

## Research topic recommendations

- 대학원 수업·연구 프로젝트에서 "재미있고 흥미롭고 기발한 주제"는 학술적으로 의미 있는 질문과 탐구의 흥미로 해석한다. 사용자가 요청하지 않은 게임화·오락형 시연을 주제 선정의 기본 방향으로 삼지 않는다.
- 연구자·연구원·교수에게 설명할 문제의 중요성, 기존 연구와의 관계, 검증 가능한 질문, 데이터와 평가 방법을 먼저 제시한다. 발표 연출이나 눈에 띄는 이름으로 학술적 기여를 대신하지 않는다.
- 시간·계산 자원 제약은 연구 범위와 구현 부담을 줄이는 조건이다. 대조 실험, 평가의 타당성, 결과 해석의 엄밀성을 생략하는 근거로 사용하지 않는다.

## Theory-to-code learning

- 연구 방법을 code level로 학습하는 실습에서는 핵심 연산의 줄·구획마다 한글 주석으로 수식의 변수, tensor shape, 입력·출력과 코드 흐름을 연결한다.
- 복잡한 실제 repository를 단순화할 때는 생략·대체한 부분을 명시하고, 원래 구현의 함수와 실습 코드의 대응 관계를 남긴다.
- 학습과 추론을 분리해 실행 가능한 작은 예제를 제공하고, 중간 tensor와 실제 실행 결과의 시각화를 함께 보여 준다. 설명용 경로와 학습된 모델의 생성 결과를 구분한다.

## 유지 문서

- `AGENTS.md`: privacy, ownership, publish boundary, validation
- `README.md`: canonical structure and workflow
- 연구 방법·reading workflow는 README 또는 기존 전문 문서에 기록한다.
- Schema·visibility contract가 있는 경우 해당 문서를 유지한다. 같은 역할의 파일을 중복 생성하지 않는다.

## 원고 검토

- Live Overleaf project는 읽기 전용으로 검토한다. Source 입력·교체·삭제와 recompile을 수행하지 않고, 확인한 file·section·line과 사용자가 적용할 replacement 또는 patch를 제공한다.

## Figure

[공통 규칙](research-figures.md), [기술 도식](technical-figure-code.md), [생성 일러스트](scientific-figure-generation.md)를 읽는다.
