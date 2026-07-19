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

- dry-run을 기본으로 하고 write는 명시적 `--apply`와 검증을 요구한다.
- seed, demo, 빈 record, generated fixture를 실제 연구 활동으로 집계하지 않는다.
- 관측값, 추론, 의견을 구분한다.
- 실패와 미완료 상태를 숨기지 않는다.
- 자동 생성 report는 artifact이며 장기 지침 문서가 아니다.

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
