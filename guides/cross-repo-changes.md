# Cross-repository change guidance

## When this applies

두 개 이상의 repository contract, release order, application compatibility, data handoff, deployment 또는 rollback이 함께 바뀌는 change에 적용한다. 한 repository의 trivial one-file fix와 독립적인 typo 수정에는 긴 commit body를 요구하지 않는다.

Cross-repository 또는 architecture change는 시작 전에 repository별 baseline과 preservation contract를 기록하고, repository별 focused commit/PR로 전달한다.

## Required change record

각 participating repository에 다음을 기록한다.

- baseline commit: 작업 시작 시 branch와 full commit SHA
- preserved functionality: 현재 동작 중 반드시 유지할 promise, workflow, data와 safety boundary
- MDS guidance applied: 적용한 reusable guidance와 적용 위치
- MDS guidance intentionally not applied: 더 나은 existing decision 또는 project-specific rule 때문에 적용하지 않은 guidance와 이유
- compatibility changes: schema, manifest, CLI, deep link, file format, bundle/executable identity, minimum version 변화
- migration steps: old/new version coexistence, order, backfill, user action, deprecation window
- tests: repository-local unit/integration/contract/privacy/release test와 cross-version matrix
- rollback: code, schema, data, release와 deployment를 안전하게 되돌리는 순서
- related commits and PRs: repository별 branch, commit, PR과 merge/deploy order

Baseline 이후 unrelated user change가 발견되면 범위에 포함하지 않고 별도로 보존한다.

## Preservation matrix

Implementation 전에 최소 다음 표를 만든다.

| Repository | Baseline | Preserved behavior | Contract change | Migration | Validation | Rollback |
| --- | --- | --- | --- | --- | --- | --- |

관측된 current behavior와 문서의 intended behavior가 다르면 둘을 구분한다. MDS가 항상 정답이라고 가정하지 않고 `APPLY_MDS`, `KEEP_EXISTING`, `UPDATE_BOTH` 결정을 사용할 수 있다.

## Delivery order

1. 모든 repository baseline, worktree clean/dirty, upstream state를 기록한다.
2. Canonical owner와 compatibility direction을 확정한다.
3. Backward-compatible contract/producer 또는 reader tolerance를 먼저 배포한다.
4. Consumer를 새 contract로 이동한다.
5. Cross-version test와 degraded mode를 검증한다.
6. Migration이 완료된 뒤에만 legacy path를 제거한다.
7. 각 PR에 관련 PR과 required merge/deploy order를 연결한다.

모든 repository를 하나의 거대한 commit처럼 다루지 않는다. 각 repository commit은 해당 repository의 사실과 검증만 포함하되 cross-repo context와 related links를 남긴다.

## Compatibility and migration

- Stable ID와 provenance를 유지하고 display name/slug/path와 분리한다.
- Unknown new optional field는 old reader가 무시할 수 있게 하고 incompatible major version은 fail closed한다.
- Producer와 consumer가 서로 다른 version인 기간을 테스트한다.
- Migration은 preview/dry-run, explicit apply, idempotency와 interruption recovery를 갖는다.
- Direct database sharing이나 simultaneous mutable writes로 migration을 우회하지 않는다.
- Rollback이 old reader를 깨뜨리는 irreversible write를 먼저 수행하지 않는다.

## Validation

Repository-local test 외에 다음 matrix를 검증한다.

- old producer → new consumer
- new producer → tolerant old consumer, 또는 명시적 incompatibility
- provider/application unavailable
- partial/stale/corrupt handoff
- migration interruption and retry
- rollback after partial rollout
- privacy and credential redaction across repository boundaries

실행하지 못한 test, dependency, external approval, deployment state를 PR에 정확히 남긴다.

## Required commit body

Cross-repository와 architecture change commit은 다음 section을 사용한다.

```text
Context:

Existing behavior preserved:

MDS guidance applied:

Intentional deviations:

Compatibility:

Validation:

Risk and rollback:

Related repositories:
```

각 section은 해당 repository의 concrete fact를 짧게 기록한다. 관련 내용이 없으면 이유를 한 줄로 명시하고 section을 삭제하지 않는다.

Trivial one-file fix, typo, comment-only change에는 이 body를 강제하지 않는다. 한 repository change라도 architecture, public contract, migration, destructive behavior, credential boundary, release/rollback을 바꾸면 detailed body를 사용한다.

## Pull request record

PR description에는 다음을 포함한다.

- repository baseline과 target branch
- change scope와 preserved behavior
- compatibility/migration sequence
- validation result와 expected fail-closed result
- rollback trigger와 exact recovery owner
- related PR links와 merge/deploy order
- owner decision이 필요한 unresolved item

관련 PR이 merge되기 전에는 존재하지 않는 commit/PR link를 추정하지 않는다. 생성 후 실제 URL과 SHA로 갱신한다.
