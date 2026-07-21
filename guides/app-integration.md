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

## Integration consent and operating-system permissions

Studio가 관리하는 integration access와 operating system이 각 application에 부여하는 privacy permission은 서로 다른 경계다.

- 서로 다른 bundle ID의 독립 application은 Studio의 macOS TCC permission을 상속하지 않는다. 같은 signing team, App Group 또는 stable install path도 Files & Folders, Accessibility, Automation, camera, microphone 같은 승인을 다른 app에 전달하지 않는다.
- Stable bundle ID, designated requirement, signing team, entitlement와 install path는 동일 app update의 permission continuity를 돕지만 새 권한을 승인하거나 다른 app의 승인을 대체하지 않는다.
- Studio 설정은 app별 integration access를 `ask`, `allow once`, `allow`, `deny`처럼 관리할 수 있다. 이를 macOS permission이 granted된 것으로 표현하지 않는다.
- Persistent grant는 verified app ID, bundle ID, signing team/designated requirement, contract major와 capability policy에 묶고 identity 또는 effect가 바뀌면 fail closed한다.
- Status, health, recent activity, launch, resource open, handoff preview와 write/apply는 별도 capability다. 한 capability 승인을 다른 effect로 확대하지 않는다.
- 승인 전 background refresh는 provider process를 실행하지 않는다. Revoke는 다음 operation부터 즉시 적용하고 provider-derived private cache도 제거한다.
- Studio는 TCC database를 읽거나 수정하거나 `tccutil` reset, 자동 클릭, 임의 설정 pane URL로 승인을 우회하지 않는다. Provider-owned permission은 provider가 자기 setup flow에서 요청하고 Studio는 sanitized blocker와 next action만 보여준다.
- 모든 authorization은 UI preflight만으로 끝내지 않고 native broker가 typed request, verified provider identity와 current grant를 다시 확인한다.

모든 provider가 denied 또는 unavailable이어도 Studio의 독립 authoring workflow는 계속 동작해야 한다.

## Read-only first

1. application discovery와 launch를 먼저 검증한다.
2. read-only status와 export를 추가한다.
3. file/data handoff를 preview와 idempotency check 뒤에 추가한다.
4. write command는 standalone recovery와 confirmation이 검증된 뒤 별도 review로 추가한다.

초기 integration은 destructive action, publish, install, model download, remote job control, cleanup을 호출하지 않는다. Write integration이 필요해도 owning application의 scope preview, confirmation, audit와 rollback을 우회하지 않는다.

Application launch availability is independent from status-provider health.
When Studio has a compatible provider identity and an exact verified launch
target, it keeps a plainly labeled Open action available even when status is
stale, degraded, empty, or temporarily failed. Refresh and setup remain separate
actions; a failed summary must not hide an otherwise runnable application.

CLI/web-only applications may expose an explicit local-UI launch capability
without pretending to be a native bundle. The control plane must use a fixed
loopback address, own and reap the child process, refuse an unrelated listener,
and never embed the full UI.

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

## Control-plane interaction model

- 여러 provider를 한 화면에서 관리해도 unrelated app operation을 page-wide lock으로 막지 않는다. Single-flight, pending/result/error와 cancellation identity는 application 단위로 소유하고, global refresh처럼 실제 shared resource를 쓰는 작업만 별도 global state로 둔다.
- Async result에는 application/request generation을 연결한다. App A의 늦은 status나 이전 App A request가 App B 또는 최신 App A state를 덮어쓰지 않아야 한다.
- Overview는 app name과 role, availability, installed version, update readiness, blocker와 valid next action을 primary layer에서 보여준다. Commit, executable, provider command, path와 raw response는 technical disclosure로 내린다.
- App별 control을 같은 크기와 grid로 정렬하되 기능을 획일화하지 않는다. 각 provider가 실제로 선언한 capability에 맞는 role-specific action과 result structure를 사용하며 manifest에 없는 action은 렌더링하거나 실행하지 않는다.
- Search/filter/view 선택 같은 control-plane presentation preference는 local UI state다. Provider data나 tracked manifest를 오염시키지 않고 invalid stored value는 safe default로 복원한다.
- Freshness는 relative label과 exact timestamp를 함께 제공한다. Window focus refresh는 bounded read-only status check만 수행하고 source fetch, dependency install, build, app replacement 또는 launch를 시작하지 않는다.
- Recent activity가 typed resource와 actionable flag를 제공할 때만 direct Open을 노출한다. Summary만 있는 item에 action을 추측하거나 private resource identifier를 합성하지 않는다.
- Read-only result는 사용자가 UI에서 clear할 수 있어도 provider record를 delete한 것으로 표현하지 않는다. Clear는 control-plane presentation state만 제거한다.

## Update channels

Update discovery와 installation은 capability negotiation 대상이며 health/status 권한에서 추론하지 않는다. Signing, version provenance, source checkout과 signed release channel은 [`app-distribution.md`](app-distribution.md)를 따른다.

- Studio에 내장된 compatibility manifest version은 remote release availability의 증거가 아니다. 실제 release metadata를 확인하지 않았다면 `not checked` 또는 `unknown`으로 표시한다.
- Source checkout status, signed release status와 selected launch target은 서로 다른 evidence와 checked time을 가진다.
- 여러 app copy가 있을 때 bundle ID만으로 Launch Services에 선택을 맡기지 않는다. Verified installed release, 사용자가 선택한 local development build 또는 explicit ask policy에 따라 exact canonical bundle path를 연다.
- Status provider executable, provider manifest와 실제 launch bundle의 provenance가 다르면 launch를 차단하고 blocker와 next action을 표시한다.
- Launch validation은 manifest 일부 field를 spot-check하지 않는다. Supported schema 전체, actual bundle executable, bundle/signing identity, clean build provenance와 exact commit을 검증하고 다른 copy가 이미 실행 중이면 path mismatch를 차단한다.
- macOS native bundle이 존재하면 Studio의 `Open`은 verified exact `.app`을 열어야 한다. Legacy/local web UI는 별도 action으로 유지할 수 있지만 native application action을 browser page로 대체하거나 web service를 desktop app처럼 표시하지 않는다.
- Owner-enabled local update-before-open은 arbitrary shell 없이 provider repository의 fixed installer만 호출하고 [`app-distribution.md`](app-distribution.md)의 clean source, running-app, signing, provenance와 rollback 조건을 모두 따른다.
- Native와 web runtime이 같은 manifest를 각각 검증하면 allowlisted platform/capability/icon, semantic version, command token, deep-link syntax, timeout, privacy와 distribution bound의 parity fixture를 유지한다. 한쪽의 느슨한 shadow validator를 `full schema`라고 부르지 않는다.
- 한 provider action이 성공한 뒤 수행하는 background evidence refresh는 다른 app의 blocker 때문에 이미 성공한 결과를 error로 바꾸지 않는다. Explicit global check만 aggregate partial failure를 전체 check feedback으로 표현한다.

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
