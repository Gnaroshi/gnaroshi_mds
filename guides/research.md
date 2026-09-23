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

## Assignment grading feedback

- 과제 채점 피드백은 사용자가 지정한 답안과 평가 기준을 근거로, 틀린 부분이나 필요한 제출 파일이 없는 이유만 간결하게 설명한다. 요청하지 않은 재제출·수정 지시나 일반적인 격려는 넣지 않는다.
- Excel 피드백은 전체 총점으로 구분한다. 총점 만점인 학생에게만 정확히 `잘 이해하셨습니다.` 한 문장을 쓰며 영역별 점수, 다른 피드백이나 이모티콘을 덧붙이지 않는다. 총점에서 감점된 학생은 모든 평가 영역의 `[영역명][획득점수/영역만점]`을 표시하고, 그중 만점 영역도 점수만 표시한다. 감점 학생의 피드백 어디에도 `잘 이해하셨습니다.`나 다른 격려 문구를 넣지 않으며, 감점 문항의 오답이나 제출 누락에 대한 피드백만 작성한다. 코드 오답은 아래의 원본 답안·제출 코드 비교 형식을 따른다.
- 코드 오답 피드백은 `(Qn) 답안:` 아래 답안지의 원본 코드를 그대로 넣고, 이어서 `(Qn) 제출하신 코드:` 아래 실제 제출 코드를 그대로 넣는다. 자연어 오류 설명으로 이 코드 비교를 대신하지 않는다. 필요한 파일이나 코드가 없으면 확인할 수 없어 감점하였다는 문구를 쓰고 제출 코드를 만들어 넣지 않는다.
- 이전 학기 자료는 작성 방식의 참고로 사용한다. 과제별 답안, 배점, 예외와 사용자가 이번 작업에서 확정한 기준을 이전 학기 기준으로 바꾸지 않는다. 수강생 정보, 제출물과 개별 점수는 공개 지침에 기록하지 않는다.
- 검토용 Excel의 감점 사유는 항목별 배점, 답안에서 요구한 내용, 실제 제출 내용과의 차이와 감점 점수를 구체적으로 적는다. 학생에게 전달하는 원본 답안·제출 코드 비교 피드백과 검토용 설명을 구분한다.
- 채점을 마친 뒤 제출 원문, 문항별 점수, 총점과 피드백을 다시 대조하여 누락, 잘못 부여한 점수, 인용 오류와 합계 오류를 확인한다.
- 사용자가 직접 수정한 note 등 기존 문서를 보존하고, 요청한 수정 범위 밖의 문서는 덮어쓰거나 채점 산출물에서 다시 생성하지 않는다.

## Research topic recommendations

- 대학원 수업·연구 프로젝트에서 "재미있고 흥미롭고 기발한 주제"는 학술적으로 의미 있는 질문과 탐구의 흥미로 해석한다. 사용자가 요청하지 않은 게임화·오락형 시연을 주제 선정의 기본 방향으로 삼지 않는다.
- 연구자·연구원·교수에게 설명할 문제의 중요성, 기존 연구와의 관계, 검증 가능한 질문, 데이터와 평가 방법을 먼저 제시한다. 발표 연출이나 눈에 띄는 이름으로 학술적 기여를 대신하지 않는다.
- 시간·계산 자원 제약은 연구 범위와 구현 부담을 줄이는 조건이다. 대조 실험, 평가의 타당성, 결과 해석의 엄밀성을 생략하는 근거로 사용하지 않는다.

## Theory-to-code learning

- 연구 방법을 code level로 학습하는 실습에서는 핵심 연산의 줄·구획마다 한글 주석으로 수식의 변수, tensor shape, 입력·출력과 코드 흐름을 연결한다.
- 복잡한 실제 repository를 단순화할 때는 생략·대체한 부분을 명시하고, 원래 구현의 함수와 실습 코드의 대응 관계를 남긴다.
- 학습과 추론을 분리해 실행 가능한 작은 예제를 제공하고, 중간 tensor와 실제 실행 결과의 시각화를 함께 보여 준다. 설명용 경로와 학습된 모델의 생성 결과를 구분한다.

## Minimum maintained Markdown

- `AGENTS.md`: privacy, ownership, publish boundary, validation
- `README.md`: canonical structure and workflow
- 연구 방법 또는 reading workflow 문서
- schema/visibility 문서가 실제로 존재할 때 해당 contract 문서

## Scientific figures

- 논문·연구 figure 작업은 `technical-figure-code.md`와 `scientific-figure-generation.md`를 함께 읽는다.
- 현재 사용자 요청이 figure role, output format, 산출물 수와 우선순위의 최상위 권한이다. Code/generated 결과는 둘 다 요청되었을 때만 함께 만든다.
- PNG/raster는 export format이다. Technical architecture, pipeline, operator, state transition과 data plot은 constructed schematic으로 만들고 image generation은 cover, teaser와 non-technical concept에 제한한다.
- Usable baseline과 아름다운 technical final을 함께 요청하면 code baseline과 polished constructed schematic을 같은 evidence map에서 만들고, image-generated pipeline을 대안으로 사용하지 않는다.
- 실제 구현을 설명하는 figure는 current working tree, config, tests와 필요한 runtime evidence를 먼저 조사하고 모든 visible module, arrow, operator, time index, shared/frozen/detached state와 label을 source file과 symbol에 연결한 evidence map을 유지한다.
- Introduction figure는 한 문장 claim과 main contribution을 가장 크게 보여주고 full architecture dump를 피한다. Technical panel은 flat 2D로 만들며 computation을 3D object나 pseudo-machine으로 표현하지 않는다.
- Final technical raster에는 required semantic text를 실제로 포함한다. Blank annotation plate와 pseudo-text는 deliverable이 아니다.
- Target venue size를 우선하고, venue가 정해지지 않았으면 약 89/182 mm와 300/600 dpi를 working reference로 사용한다. 16:9는 paper 기본값이 아니다.
- Semantic rejection은 과거 visual score와 pass 판정을 무효화한다. Rejected candidate를 보존했다는 이유로 publication asset로 사용하지 않는다.
- Figure에 reusable한 owner 승인·거절 기준이 생기면 해당 guide의 decision log를 같은 작업에서 갱신한다.
