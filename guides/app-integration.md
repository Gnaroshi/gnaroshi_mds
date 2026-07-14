# Application integration guidance

## Product boundary

- 각 application은 Studio 없이도 install, launch, core workflow, recovery를 독립적으로 수행할 수 있어야 한다.
- Gnaroshi Studio는 ecosystem의 control plane이다. 다른 application의 UI, source code, canonical data를 흡수하는 monolith가 아니다.
- Studio는 discovery, launch, read-only status, reviewed handoff와 명시적으로 승인된 command를 조정한다.
- 각 application은 자기 domain data, credential, destructive confirmation, notification과 recovery를 계속 소유한다.
- integration이 없어도 기존 standalone workflow와 data portability가 유지되어야 한다.

## Application manifest

Studio와 연결되는 application은 versioned manifest를 app bundle 또는 executable과 함께 제공한다. Manifest는 사람이 편집하는 arbitrary command template이 아니라 application이 배포하는 capability declaration이다.

권장 field:

- manifest schema version
- stable application ID와 display name
- application version과 minimum compatible Studio version
- release version과 Git commit/build provenance
- bundle ID 또는 fixed executable identity
- 제공 capability: launch, status, command, handoff, deep link, local service
- 각 capability의 contract version과 read/write classification
- supported transport와 lifecycle owner
- deep-link scheme와 allowlisted route
- JSON status command의 fixed subcommand 정보
- data sensitivity와 redaction level
- degraded-mode behavior
- health contract version, freshness window와 fixed recent-activity command
- signed-release와 source-checkout update channel

Manifest에 credential, token, local secret, user content, raw shell string, mutable runtime state, private path를 넣지 않는다. Unknown major manifest version은 fail closed하고 optional unknown field만 무시한다.

Tracked manifest의 semantic version은 release source와 일치해야 한다. Release asset으로 manifest를 publish할 때 commit SHA, commit count, build time, artifact checksum과 signing/notarization state는 generated provenance에 기록하고 tracked source에 임의의 current HEAD를 하드코딩하지 않는다.

## Typed adapters and provider interfaces

- Studio에는 application별 UI shortcut이 아니라 공통 typed provider interface와 application-specific adapter를 둔다.
- 권장 interface는 discovery, launch, status, command, handoff다.
- Adapter는 capability를 명시적으로 negotiate하고 status capability를 write permission으로 확대 해석하지 않는다.
- Fixed executable, fixed subcommand, typed argument array를 사용한다. UI/config에서 arbitrary shell string을 받아 실행하지 않는다.
- Timeout, cancellation, stdout/stderr size, exit code와 redaction을 adapter contract에 포함한다.
- 다른 repository source를 복사해 adapter를 만들지 않고 public/stable contract만 구현한다.

## Read-only first

1. application discovery와 launch를 먼저 검증한다.
2. read-only status와 export를 추가한다.
3. file/data handoff를 preview와 idempotency check 뒤에 추가한다.
4. write command는 standalone recovery와 confirmation이 검증된 뒤 별도 review로 추가한다.

초기 integration은 destructive action, publish, install, model download, remote job control, cleanup을 호출하지 않는다. Write integration이 필요해도 owning application의 scope preview, confirmation, audit와 rollback을 우회하지 않는다.

## JSON status commands

CLI가 있는 application은 fixed status subcommand와 machine-readable JSON을 우선한다.

```text
<application> integration status --json
```

- stdout은 한 versioned JSON response만 출력하고 human log는 stderr로 분리한다.
- Response는 provider ID/version, contract version, capability, generated time, freshness, status, data, warnings, errors를 포함한다.
- Status는 최소 `ok`, `partial`, `blocked`, `unavailable`, `stale`, `incompatible`, `failed`를 구분한다.
- Empty, unavailable, permission-limited와 stale을 healthy/idle로 합치지 않는다.
- Error는 stable code와 redacted message를 사용하고 credential, raw command, private path를 echo하지 않는다.
- Status command는 canonical data나 remote state를 변경하지 않는다.

## Health and recent activity

- Health는 status와 별도 의미를 가진 versioned read-only contract다. App availability, required prerequisite, permission limitation, freshness, blocker와 next valid action을 구분한다.
- Health가 cache를 사용하면 observed time, generated time, freshness threshold와 stale 판정을 포함한다. 만료된 healthy 결과를 현재 healthy로 재사용하지 않는다.
- Recent activity는 owning application이 이미 관측하고 보존한 safe summary만 제공한다. Studio가 private database, localStorage, workspace file 또는 SSH state를 직접 읽어 recent를 재구성하지 않는다.
- Recent item은 stable opaque ID, type, occurred time, short label, actionability와 safe resource reference만 포함한다. Private path, content body, URL credential, raw command, host identity와 secret-bearing process argument를 제외한다.
- Recent가 비어 있음, provider unavailable과 permission blocked를 같은 상태로 합치지 않는다.
- Manifest는 fixed recent-activity subcommand와 timeout/limit을 선언할 수 있다. UI는 bounded limit을 사용하고 provider가 더 많은 record를 반환하면 거부한다.

## Update channels

Update discovery와 installation은 capability negotiation 대상이며 health/status 권한에서 추론하지 않는다. Signing, version provenance, source checkout과 signed release channel은 [`app-distribution.md`](app-distribution.md)를 따른다.

## Deep links

- Deep link는 launch, navigation, safe prefill에 사용한다.
- Stable opaque ID를 우선하고 secret, raw private note, credential, SSH host, local path를 URL에 넣지 않는다.
- Route와 parameter는 receiver가 allowlist와 schema로 검증한다.
- Deep link만으로 save, apply, delete, publish, install, model download, background-service enable을 실행하지 않는다.
- 현재 state를 교체하거나 file을 import할 때는 receiver가 preview와 confirmation을 제공한다.
- Application이 unavailable이면 link와 reference를 보존하고 install/select/launch 안내로 degrade한다.

## File and data handoff

- Handoff는 versioned schema, stable provider ID, provenance, generated time과 필요한 경우 content hash를 가진다.
- User-selected path 또는 application-owned export를 사용하고 다른 app의 mutable internal directory를 watch하지 않는다.
- Write는 atomic하게 수행하고 import 전에 schema와 hash를 검증한다.
- Studio import는 private draft/reference가 기본이며 save가 publish나 source-app write를 유발하지 않는다.
- 동일 stable external ID의 반복 import는 idempotent해야 한다.
- 관측되지 않은 field, completion, score, visibility, translation, metric, timestamp를 합성하지 않는다.

## Local HTTP only when necessary

Local HTTP는 high-frequency status, long-running lifecycle 또는 CLI/file transport로 해결할 수 없는 경우에만 사용한다.

- loopback에 bind하거나 user-owned Unix-domain socket을 사용한다.
- Browser가 접근할 수 있으면 exact origin 또는 per-launch capability token을 요구한다.
- CORS wildcard, unauthenticated mutation, fixed-port assumption을 피한다.
- Endpoint discovery는 user-only app-support state로 제공하고 repository file이나 public URL query를 사용하지 않는다.
- Health/capability/status와 mutating endpoint를 분리한다.
- Request/response size, rate, timeout, logging과 shutdown을 제한한다.
- Service lifecycle owner, start/stop/restart, login launch 여부를 UI에 명확히 표시한다.

## Prohibited coupling

- 다른 application의 private database, shared mutable SQLite, UserDefaults domain, localStorage, Keychain, SSH key, cache를 직접 읽거나 쓰지 않는다.
- Internal report filename, undocumented JSON shape, HTML scraping을 stable integration으로 취급하지 않는다.
- `sh -c`, `bash -c`, user-provided executable text, interpolated shell command를 provider interface로 제공하지 않는다.
- Application UI를 Studio webview에 embed하지 않는다.
- Local contract로 충분한데 remote cloud service를 추가하지 않는다.

## Degraded mode

Application이 missing, stopped, outdated, permission-limited, incompatible일 때 Studio와 owning application의 core workflow는 계속 동작해야 한다.

- Missing: install/select/launch action과 필요한 prerequisite를 표시한다.
- Stopped: unavailable로 표시하고 expired healthy state를 재사용하지 않는다.
- Stale: last update와 freshness를 표시한다.
- Partial: 관측된 fact만 보여주고 누락 scope를 명시한다.
- Incompatible: supported/received contract version을 보여주고 write를 차단한다.
- Failed handoff: source data와 기존 destination을 보존하고 새 preview를 요구한다.

Provider가 없어도 existing external reference를 삭제하거나 가짜 result로 대체하지 않는다.

## Validation

- Manifest/status/handoff valid, partial, stale, incompatible, corrupt fixture
- shell metacharacter를 포함한 ID/path의 typed-argument test
- provider absence, crash, timeout, cancellation, output-limit test
- deep-link route/parameter rejection과 log redaction test
- repeated import idempotency와 preview/hash mismatch test
- read-only capability가 data, repository, remote host를 변경하지 않는 test
- secret, private path, unselected content가 public output에 도달하지 않는 privacy test
