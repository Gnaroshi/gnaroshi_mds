# Application guidance

## Product order

1. 사용자 약속과 non-goal을 확정한다.
2. 실행 가능한 app host와 핵심 vertical slice를 만든다.
3. data model과 source of truth를 고정한다.
4. empty/loading/error/edit/permission state를 포함한 workflow를 완성한다.
5. 실제 device 또는 최소 지원 window에서 검증한다.
6. distribution, recovery, privacy를 확인한다.

## Architecture

- local-first data는 사용자가 명시적으로 선택하지 않는 한 외부로 보내지 않는다.
- 여러 local repository가 고정된 parent 아래 함께 있는 개인용 app은 알려진 folder name과 구조를 검증해 자동 연결하고, 누락되거나 유효하지 않은 항목에만 manual setup을 요구한다.
- desktop app은 개발 중 hot reload 경로와 독립 실행 bundle 경로를 분리하고, 자주 쓰는 local build는 repository 안의 예측 가능한 Git-ignored 경로에서 바로 열 수 있게 한다.
- installer나 disk image처럼 느린 배포 산출물은 매 edit마다 만들지 않고 명시적인 release/bundle 명령에서만 생성한다.
- macOS permission을 사용하는 app은 stable bundle ID, signing identity와 installed path를 유지한다. 반복 development bundle을 ad-hoc identity로 배포하지 않고 [`app-distribution.md`](app-distribution.md)의 development/release signing을 적용한다.
- macOS local build를 Spotlight나 app launcher에 노출할 때는 repository bundle symlink만 등록하지 않는다. Spotlight가 실제로 index하는 Applications 위치에 작은 real launcher bundle을 한 번 만들고 repository build를 열게 하며, `mdls`와 `mdfind` 결과를 확인한다.
- macOS의 floating intake/status window가 사용자의 현재 작업 옆에 계속 있어야 하는 제품이면 모든 Spaces 참여를 기본으로 하고 명시적인 opt-out을 제공한다. Space membership과 cursor/focused display placement는 별도 설정 축으로 취급하며, display 선택이 Desktop 전환 추적을 대신한다고 가정하지 않는다.
- Packaged desktop UI나 behavior를 바꾼 작업은 source/build artifact에서 끝내지 않는다. 사용자가 source-only 검증을 명시하지 않았다면 [`app-distribution.md`](app-distribution.md)의 local development delivery contract에 따라 signed stable install, Spotlight launch target과 exact build provenance까지 확인한다.
- external provider는 protocol/interface 뒤에 두고 mock과 real provider를 분리한다.
- 다른 Gnaroshi application과 연결할 때는 [`app-integration.md`](app-integration.md)의 independent-app, manifest, typed-adapter와 degraded-mode contract를 적용한다.
- Release에서 fake data로 조용히 fallback하지 않는다.
- credential은 client code나 repository에 넣지 않는다.
- 큰 화면이나 manager 하나에 책임을 몰지 말고 feature boundary로 나눈다.
- destructive action은 scope, preservation, confirmation을 명확히 표시한다.
- Confirmation friction은 실제 위험에 비례시킨다. Current dry-run/preview, 자동 backup, idempotency와 rollback이 있는 반복 apply는 범위와 보존 항목을 짧게 보여주는 한 번의 명시적 confirmation으로 실행하고, 매 실행마다 긴 문장을 다시 입력하게 하지 않는다. Typed confirmation은 되돌릴 수 없는 삭제, 광범위한 overwrite, 복구 수단이 없는 변경처럼 오입력 비용이 큰 작업에만 사용한다.

## Process and resource lifecycle

- 모든 subprocess, timer, polling task, observer, local server, socket과 file handle에는 명시적인 owner와 시작·취소·종료 경계가 있어야 한다. View 재생성이나 refresh가 같은 background work를 중복 시작하지 않게 idempotent start를 사용한다.
- 일반 CLI, health/status command와 one-shot adapter는 종료 뒤 child process나 listening port를 남기지 않는다. 지속 실행이 필요한 daemon/service는 optional background service로 명시하고 lifecycle, PID/port ownership, stop command와 recovery를 문서화한다.
- Subprocess는 shell string이 아니라 typed argument로 시작하고 timeout, cancellation, stdout/stderr drain과 exit wait를 처리한다. Parent가 종료되거나 task가 취소될 때 child와 필요한 process group을 정상 종료하고 reap한다. 의도하지 않은 detached/background child를 만들지 않는다.
- SSH multiplexing 같은 reusable connection은 host별 stable ownership과 bounded lifetime을 사용한다. Poll마다 detached master를 새로 만들지 않고, application shutdown과 configuration removal에서 해당 app이 소유한 connection만 명시적으로 닫는다. 사용자의 unrelated SSH session과 socket은 건드리지 않는다.
- Electron/desktop app은 window close와 application quit를 구분한다. App-owned local server, media resolver와 child process는 quit에서 종료하고, reload/crash/retry에서도 중복 listener와 orphan process가 남지 않게 한다.
- Lifecycle validation은 최소 세 번의 launch → idle/refresh → graceful quit cycle에서 process, child process, thread/task, file descriptor와 listening port가 baseline으로 돌아오는지 확인한다. Timeout, malformed response, unreachable host와 cancellation 경로도 포함하며, 검증용으로 실행한 app과 server는 evidence 수집 직후 종료한다.

## UI contract

- Primary application UI에는 현재 작업을 이해하고 완료하는 데 필요한 사용자 목표, blocker, progress, result와 next action만 노출한다. Repository path, executable/command, PID, hash, schema/version, raw API/backend 상태, artifact filename과 raw log는 기본 화면·dashboard·floating workflow에서 숨기고 `Settings > Advanced/Diagnostics`, explicit Details, Reports 또는 Logs로 이동한다. 잠재적으로 유용하다는 이유만으로 primary UI에 계속 표시하지 않는다.
- Technical details는 기본값을 off/collapsed로 유지하고 사용자가 명시적으로 열었을 때만 표시한다. Error는 기술 문자열을 그대로 던지지 않고 사용자 언어의 요약, 보존된 data와 recovery action을 먼저 제공한다. Safety, privacy, destructive scope와 blocker는 technical detail로 분류해 숨기지 않는다.
- 현재 상태, blocker, 다음 valid action을 3초 안에 찾을 수 있어야 한다.
- 의존 작업은 번호와 prerequisite를 보여주고 성공한 경우에만 다음 단계로 진행한다.
- minimum window/device에서 control과 text가 잘리지 않아야 한다.
- essential meaning을 hover, color, icon 하나에만 의존하지 않는다.
- app identity와 functional/menu-bar icon에는 [`image-assets.md`](image-assets.md)와 [`app-icons.md`](app-icons.md)를 적용한다.

## Minimum maintained Markdown

- `AGENTS.md`
- `README.md`
- 제품 범위/MVP 문서
- architecture 또는 data model 문서
- design/UX 문서
- 실제로 권한·배포·복구가 있는 경우에만 해당 운영 문서
