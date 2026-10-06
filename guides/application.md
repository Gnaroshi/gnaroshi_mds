# Application guidance

Native·desktop·CLI·로컬 도구 개발에 적용한다. UI는 [ui-ux](ui-ux.md), signed build·설치·launcher·업데이트는 [app-distribution](app-distribution.md)를 따른다.

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
- 개발용 hot reload와 packaged bundle을 구분한다. Build output은 예측 가능한 Git-ignored 경로에 두고 사용자에게 전달할 때 stable installed bundle을 사용한다.
- Owner가 특정 개인 기기에 변경본을 바로 설치하는 검수 workflow를 명시한 프로젝트는 검증된 변경 후 같은 작업에서 해당 기기의 업데이트 설치까지 수행한다. Source-only 요청이 없으면 매번 설치 지시를 다시 요구하거나 캡처 전달로 끝내지 않는다. 기존 데이터·서명·app identity를 유지하고 설치 성공을 확인한다. 연결·잠금·서명 또는 미저장 작업 때문에 진행할 수 없으면 미설치 상태와 필요한 조치를 알리며, 다른 기기나 공개 배포로 권한을 확대하지 않는다.
- installer나 disk image처럼 느린 배포 산출물은 매 edit마다 만들지 않고 명시적인 release/bundle 명령에서만 생성한다.
- external provider는 protocol/interface 뒤에 두고 mock과 real provider를 분리한다.
- 다른 Gnaroshi application과 연결할 때는 [`app-integration.md`](app-integration.md)의 independent-app, manifest, typed-adapter와 degraded-mode contract를 적용한다.
- Release에서 fake data로 조용히 fallback하지 않는다.
- credential은 client code나 repository에 넣지 않는다.
- 개인 Mac 재설치 도구는 Git의 설치 목록·이식 가능한 설정과 외부 저장소의 원본 파일·앱 상태·대화 백업을 분리한다. 일반 자료는 폴더로 직접 탐색할 수 있게 보관하고, Mac 메타데이터가 필요한 복원본은 별도 Mac 파일시스템 보관함을 사용한다.
- 큰 화면이나 manager 하나에 책임을 몰지 말고 feature boundary로 나눈다.
- UI를 줄일 때 사라진 container의 style, helper와 전시용 구현도 함께 정리한다. 검증 fixture는 production dependency graph에서 제외하고, lazy feature의 큰 parser·renderer가 shared chunk를 통해 시작 화면에 다시 포함되지 않는지 실제 build output으로 확인한다. 코드량 감소만으로 성능 개선을 주장하지 않는다.

## Native integration

- macOS의 floating intake/status window가 사용자의 현재 작업 옆에 계속 있어야 하는 제품이면 모든 Spaces 참여를 기본으로 하고 명시적인 opt-out을 제공한다. Space membership과 cursor/focused display placement는 별도 설정 축으로 취급하며, display 선택이 Desktop 전환 추적을 대신한다고 가정하지 않는다.
- System-wide shortcut은 같은 app의 새 window와 별도 application instance/process 중 의도한 결과를 먼저 구분한다. Config 저장·구문 검사·hotkey 등록 성공만으로 완료 처리하지 않고 representative foreground app과 지원 input language/layout에서 실제 key input과 결과를 확인한다. 별도 instance는 새 PID로 검증하며, 실제 입력 검증이 막히면 미검증 범위를 명시하고 완료로 단정하지 않는다.
- Repository terminal action이 있는 macOS application은 owner preference로 Ghostty를 우선할 수 있다. 이 경우 exact installed bundle identity를 검증하고 canonical working directory만 fixed argument로 전달하며, Settings에서 명시적인 system Terminal fallback/override를 제공한다. Terminal 선택을 arbitrary executable이나 shell command field로 만들지 않고 one-shot launcher process를 wait/reap한다.

## Process and resource lifecycle

- 모든 subprocess, timer, polling task, observer, local server, socket과 file handle에는 명시적인 owner와 시작·취소·종료 경계가 있어야 한다. View 재생성이나 refresh가 같은 background work를 중복 시작하지 않게 idempotent start를 사용한다.
- 일반 CLI, health/status command와 one-shot adapter는 종료 뒤 child process나 listening port를 남기지 않는다. 지속 실행이 필요한 daemon/service는 optional background service로 명시하고 lifecycle, PID/port ownership, stop command와 recovery를 문서화한다.
- Subprocess는 shell string이 아니라 typed argument로 시작하고 timeout, cancellation, stdout/stderr drain과 exit wait를 처리한다. Parent가 종료되거나 task가 취소될 때 child와 필요한 process group을 정상 종료하고 reap한다. 의도하지 않은 detached/background child를 만들지 않는다.
- SSH multiplexing 같은 reusable connection은 host별 stable ownership과 bounded lifetime을 사용한다. Poll마다 detached master를 새로 만들지 않고, application shutdown과 configuration removal에서 해당 app이 소유한 connection만 명시적으로 닫는다. 사용자의 unrelated SSH session과 socket은 건드리지 않는다.
- Electron/desktop app은 window close와 application quit를 구분한다. App-owned local server, media resolver와 child process는 quit에서 종료하고, reload/crash/retry에서도 중복 listener와 orphan process가 남지 않게 한다.
- Lifecycle validation은 최소 세 번의 launch → idle/refresh → graceful quit cycle에서 process, child process, thread/task, file descriptor와 listening port가 baseline으로 돌아오는지 확인한다. Timeout, malformed response, unreachable host와 cancellation 경로도 포함하며, 검증용으로 실행한 app과 server는 evidence 수집 직후 종료한다.
- Automated lifecycle test는 window 없는 harness와 fake process/server를 우선한다. 실제 UI 실행은 [공통 작업 보존 규칙](../AGENTS.md#검증과-사용자-작업-보존)을 따른다.

## UI contract

- 유지 중인 design/UX 문서 한 곳에 대상 사용자·주 작업, 승인된 시각 방향, semantic token의 code 위치, component의 기본/선택/진행/실패 상태와 의도적으로 제외한 표현을 연결한다. 새 design-md 형식이 있다는 이유로 token 값의 두 번째 원본이나 중복 문서를 만들지 않는다. Reference의 웹 스타일을 native control, safe area, text 확대와 lifecycle 위에 강제하지 않는다.
- 의존 작업은 번호와 prerequisite를 보여주고 성공한 경우에만 다음 단계로 진행한다.
- app identity와 functional/menu-bar icon에는 [`image-assets.md`](image-assets.md)와 [`app-icons.md`](app-icons.md)를 적용한다.

## 유지 문서

- `AGENTS.md`: 작업 경계와 검증 명령.
- `README.md`: 제품 범위, 구조, 실행과 핵심 workflow.
- Architecture·data model·UI가 복잡하면 해당 설계 문서에 ownership·contract·상태를 기록한다. UI가 없는 CLI에 design 문서를 요구하지 않는다.
- 권한·배포·복구가 있는 경우 해당 운영 절차를 유지한다. 기존 문서가 같은 역할을 충족하면 별도 파일을 만들지 않는다.
