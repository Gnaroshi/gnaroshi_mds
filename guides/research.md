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
