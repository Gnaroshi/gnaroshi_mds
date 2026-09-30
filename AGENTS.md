# 공통 작업 규칙

## 적용

- [README.md](README.md)의 작업별 목록으로 필요한 지침을 선택한다. 현재 사용자 요청과 대상 프로젝트의 구체적인 지침을 우선한다.
- 구현 사실은 대상 저장소의 현재 코드·설정·테스트와 필요한 실행 결과로 확인한다. 과거 문서나 catalog를 현재 구현의 증거로 사용하지 않는다.
- 여러 저장소 또는 주요 구조·계약을 바꾸면 [cross-repo-changes](guides/cross-repo-changes.md)의 baseline, 보존 범위, 호환성, 검증, rollback과 commit 기록을 적용한다.

## 문서 유지

- 규칙은 적용 작업에 맞는 문서 한 곳에 둔다. 다른 문서는 조건과 링크만 제공한다. 작업별 읽기 목록은 README에서 관리한다.
- 문장은 실행, 판단, 제약, 검증 또는 출처 확인에 필요한 내용만 남긴다. 대화의 발언을 그대로 규칙으로 옮기거나 독자 선언, 저장소 소개, 반복 요약을 추가하지 않는다.
- 재사용 가능한 새 선호와 규칙은 이 저장소에 반영하고 승인된 범위에서 commit·push한다. 기존 규칙을 옮기거나 줄일 때 적용 조건, 예외와 안전 경계를 보존한다.
- 프로젝트 고유 구현, 원고, 실험 결과, 개인 정보, credential, private transcript와 임시 로그는 가져오지 않는다. 프로젝트별 spec·검증 결과는 해당 프로젝트에 둔다.
- 문서 유형과 디렉터리는 실제 사용 범위에 맞춰 만든다. 빈 template, 같은 내용을 복제한 guide, 작업별 versioned guideline을 만들지 않는다.
- 현재 규칙과 과거 조사·승인 기록을 분리한다. 과거 기록은 출처나 결정 근거가 필요할 때만 보존하고 현재 사용 가능 여부를 표시한다.
- 문서 이동·삭제 시 내부 링크, 읽기 경로와 MCP 등록표를 함께 갱신한다. 기존 MCP URI는 가능한 한 유지하고 전체 resource를 읽어 검증한다.
- 설명은 짧고 평이하게 쓰고, 필요한 용어와 비교 조건은 처음 사용할 때 정의한다.

## 검증과 사용자 작업 보존

- 정확성, 데이터 보존과 실제 위험에 필요한 검증만 수행한다. 이미 승인된 작업에 반복 승인이나 동일 조건의 재검증을 추가하지 않는다.
- Agent가 검증용으로 시작한 앱·서버·provider는 evidence 수집 직후 정상 종료한다. 종료 시 자식·분리 process와 listening port가 남지 않았는지 확인한다. 사용자가 실행한 앱이나 미저장 상태가 의심되는 process는 강제 종료하지 않는다.
- 사용자 작업 중 focus를 빼앗거나 주 모니터에 검증 창을 열지 않는다. Headless·CLI·비활성 background 검증을 우선한다. 실제 창이 필요하면 보조 display와 focus 보존을 보장하고, 보장할 수 없으면 해당 visual 검증의 미완료 범위를 보고한다.
- Packaged desktop 변경은 source-only 요청이 없으면 [배포 가이드](guides/app-distribution.md)의 signed stable install과 launcher 검증까지 수행한다.

## GitHub Actions

- Owner가 Actions 사용을 금지한 작업에서는 workflow 실행·재실행·취소·활성화·비활성화·수정과 run/check/log 조회·CI 진단을 하지 않는다. 재개는 owner가 명시한 범위에서만 한다.
- 이 제한은 local inspection/build/test/signed install과 일반 Git·branch·PR metadata 작업을 막지 않는다. PR check를 대신 조회하거나 CI 성공을 추정하지 않는다.
- Build, test, lint, contract, packaging과 signature 검증을 local에서 먼저 수행한다. Actions를 반복 개발·디버깅 loop로 사용하지 않는다.
- 허용된 workflow가 실패하면 원인을 한 번 분류한다. Code/configuration 문제는 local에서 재현·수정·검증한 뒤 새 commit을 한 번 push한다. Billing, quota, runner, secret/approval 또는 account 문제는 workflow나 제품 code로 우회하지 않고 blocker가 해소될 때까지 이를 해결하려는 추가 push·rerun을 중단한다.
- Rerun은 현재 PR/release의 최신 relevant SHA와 실패 job만 대상으로 한다. 과거 run을 일괄 재실행하거나 같은 원인의 실패를 반복 실행하지 않는다.
- Expensive macOS packaging·signing·notarization·release는 required validation 또는 owner-approved release 시점에만 실행한다. 안전한 path filter, concurrency cancellation, cache와 job 분리를 사용하되 required check나 release integrity를 약화하지 않는다.
