# Application distribution, signing and updates

## macOS identity and permission continuity

- macOS privacy approval를 우회하거나 자동 승인하려 하지 않는다. 최초 접근, 새 보호 자원, entitlement 변화와 사용자가 reset한 TCC state는 system confirmation을 요구할 수 있다.
- 반복 permission prompt를 줄이려면 bundle ID, signing team/identity, entitlements와 installed application path를 안정적으로 유지한다.
- 로컬 app bundle을 매 build마다 ad-hoc 서명하지 않는다. release와 같은 team의 identity를 우선하고 예측 가능한 ignored output에서 `~/Applications` 같은 stable install location으로 설치한다. Development와 release certificate의 team이 다르면 권한 민감 local package에는 local Keychain의 `Developer ID Application` identity를 사용할 수 있다. 이 빌드는 local-only이고 dirty provenance를 허용할 수 있지만 public artifact로 배포하지 않는다.
- Release는 `Developer ID Application`, hardened runtime, timestamp, notarization과 stapling을 요구한다. Distribution build가 요구 조건을 충족하지 못하면 unsigned/ad-hoc release로 조용히 fallback하지 않는다.
- Debug host, raw interpreter, `tauri dev`, `electron .`, `swift run`은 packaged app과 다른 code identity다. Privacy-sensitive workflow 검증은 signed installed development bundle로 수행한다.
- Certificate, private key, notary credential, App Store Connect key와 updater private key는 Keychain 또는 GitHub Actions secret에만 둔다. Repository, manifest, log, CLI argument와 artifact에 넣지 않는다.
- Signing identity 탐색은 exact class와 team을 검증한다. 같은 bundle ID를 다른 team으로 서명하면 permission continuity가 보장되지 않으므로, local permission build와 release는 같은 team을 사용하거나 전환 시 한 번의 system approval 가능성을 명시한다.

Signing은 이미 승인된 permission을 안정된 application identity에 연결하는 수단이지 새 permission을 대신 승인하는 수단이 아니다.

## Local development delivery contract

- Packaged desktop application의 동작이나 UI를 바꾼 작업은 사용자가 source-only 또는 development-server 검증만 명시하지 않는 한 source build 성공만으로 완료하지 않는다. 현재 source HEAD를 signed application으로 만들고 stable install location에 교체 설치한 뒤 실제 설치본의 provenance를 확인해야 한다.
- 개발자가 실행하는 repository binary, target/build bundle과 사용자가 Spotlight, Dock 또는 Finder에서 여는 installed bundle을 구분한다. 사용자-facing 검증과 handoff에는 installed bundle을 사용하고 build output을 열어 변경 반영을 대신하지 않는다.
- 교체 전 실행 중인 installed application을 탐지한다. 미저장 작업 가능성이 있으면 강제 종료하지 않고 사용자에게 저장·종료를 요청한 뒤 같은 작업에서 설치를 재개한다. 종료 대기 때문에 설치하지 못했다면 변경이 Spotlight에 반영됐다고 보고하지 않는다.
- 교체 설치는 stable bundle ID, signing team/identity, entitlements와 install path를 유지하고 가능한 경우 atomic replacement를 사용한다. 기존 승인을 보존하기 위해 매 작업마다 app을 다른 path에서 실행하거나 launcher bundle을 새 identity로 재생성하지 않는다.
- 설치 뒤에는 최소한 installed bundle의 source commit/build provenance, `codesign --verify --deep --strict`, bundle/team identity, launcher target과 Spotlight index를 확인한다. 사용자가 바로 확인해야 하는 작업이면 새 installed bundle을 한 번 실행해 실제 launch target도 확인한다.
- `/Applications`의 Spotlight용 launcher가 별도 bundle이면 stable launcher identity와 path를 유지하고 stable installed application만 연다. Launcher가 가리키는 target, `mdls`와 `mdfind` 결과를 갱신·검증하며 ephemeral repository path 또는 symlink 자체를 검색 결과로 의존하지 않는다.
- 반복 build·install 때문에 동일한 Desktop/Documents/Downloads, network volume, camera, microphone 또는 automation permission을 다시 요구하면 먼저 code identity, entitlement diff, install path와 launcher target drift를 defect로 조사한다. 편의를 위해 TCC database를 reset·편집하거나 permission prompt를 자동 승인하지 않는다.
- 새 protected resource, entitlement, signing team 또는 designated requirement가 실제로 바뀌면 macOS가 새 승인을 요구할 수 있다. 이를 숨기지 않고 변화 이유와 한 번 필요한 사용자 action을 명시한다.

로컬 전달의 완료 증거는 public release 완료를 의미하지 않는다. Notarization, stapling, signed updater와 release artifact 검증은 아래 release rule을 별도로 충족해야 한다.

## Git-derived version provenance

- 사용자-facing version은 SemVer이며 source, package metadata, app bundle과 integration manifest가 같은 값을 사용한다.
- Release tag는 `v<semver>`를 사용하고 tag가 가리키는 commit에서만 release artifact를 만든다.
- Build number는 monotonic Git commit count 또는 CI run number를 사용할 수 있다. macOS `CFBundleVersion`에는 숫자형 build number를 사용한다.
- About, `--version --json`, health/status와 generated release manifest는 full commit SHA 또는 validated short SHA와 build number를 제공한다.
- Dirty source build는 `dirty: true`로 표시하고 production release를 만들지 않는다.
- Changelog는 이전 release tag 이후 commit log에서 생성하되 commit message를 product feature claim으로 그대로 확대 해석하지 않는다.
- 과거 tag나 published release를 새 의미로 이동시키거나 force-update하지 않는다. 잘못된 release는 새 patch version과 correction note로 고친다.

## Published application manifest

Release마다 provider-owned `gnaroshi.app.json`을 app bundle/CLI package와 GitHub Release asset에 포함한다. Generated release copy는 다음 provenance를 함께 제공한다.

- release version and tag
- source commit and numeric build
- manifest/integration/health contract versions
- artifact filenames, platform/architecture and SHA-256
- code-signing class, notarization and stapling result
- minimum compatible Studio version
- update channel and release URL

Tracked manifest에는 secret, token, local checkout path 또는 mutable latest state를 넣지 않는다. Published manifest와 artifact checksum이 다르면 update/install을 중단한다.

## Source-checkout update channel

- Source checkout은 verified repository remote와 clean/dirty state를 먼저 확인한다.
- 자동 동작은 fixed `git fetch --prune origin`까지로 제한한다. Fetch는 현재 branch, worktree와 file을 변경하지 않는다.
- Merge, rebase, reset, checkout, pull, dependency install, build와 app replacement는 preview와 명시적 승인 뒤에 별도 단계로 수행한다.
- Dirty checkout은 update availability를 보여줄 수 있지만 apply를 차단하고 현재 file을 보존한다.
- Ahead/diverged state를 behind와 구분한다. Remote default branch가 새 commit을 가진다는 이유만으로 local commit을 버리지 않는다.

## Signed-release update channel

- DMG/ZIP/app 사용자는 authenticated release metadata 또는 public HTTPS release endpoint에서 update를 확인한다.
- Auto-download/install은 Developer ID signature, notarization, updater-specific signature, checksum, atomic replacement, running-app handoff와 rollback이 모두 검증된 뒤에만 활성화한다.
- 조건이 부족하면 update available 알림과 verified release page/download action만 제공한다.
- Private GitHub repository는 일반 사용자에게 unauthenticated update feed가 아니다. Public distribution이 필요하면 public release repository 또는 privacy-reviewed public update endpoint를 별도로 소유한다.
- Update check failure는 app health failure가 아니다. Installed app은 offline/degraded update state에서도 independently runnable해야 한다.

## Notification behavior

- 시작 시 또는 bounded interval에 한 번 확인하고 rate limit, offline과 GitHub/API failure를 명시한다.
- Current version, available version, channel, release notes link와 valid next action을 보여준다.
- Mandatory update는 security/contract incompatibility처럼 owner가 명시한 경우에만 사용한다.
- Source fetch와 binary download/install을 같은 button이나 status로 표현하지 않는다.

## Release validation

- Bundle identifier, team identifier, designated requirement, entitlements와 stable install path
- `codesign --verify --deep --strict`, Gatekeeper assessment, notarization and stapling
- Version/tag/commit/build consistency and clean source
- Manifest schema, provider health/recent fixtures and privacy redaction
- Artifact SHA-256 and update signature verification
- Old app/new Studio, new app/old Studio, offline, private release, dirty checkout and rollback
- First permission grant and subsequent signed rebuild/reinstall without an unnecessary repeated prompt; system-required new permission prompts remain expected
