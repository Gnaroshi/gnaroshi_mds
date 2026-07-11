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
- desktop app은 개발 중 hot reload 경로와 독립 실행 bundle 경로를 분리하고, 자주 쓰는 local build는 repository 안의 예측 가능한 Git-ignored 경로에서 바로 열 수 있게 한다.
- installer나 disk image처럼 느린 배포 산출물은 매 edit마다 만들지 않고 명시적인 release/bundle 명령에서만 생성한다.
- external provider는 protocol/interface 뒤에 두고 mock과 real provider를 분리한다.
- Release에서 fake data로 조용히 fallback하지 않는다.
- credential은 client code나 repository에 넣지 않는다.
- 큰 화면이나 manager 하나에 책임을 몰지 말고 feature boundary로 나눈다.
- destructive action은 scope, preservation, confirmation을 명확히 표시한다.

## UI contract

- 현재 상태, blocker, 다음 valid action을 3초 안에 찾을 수 있어야 한다.
- 의존 작업은 번호와 prerequisite를 보여주고 성공한 경우에만 다음 단계로 진행한다.
- minimum window/device에서 control과 text가 잘리지 않아야 한다.
- essential meaning을 hover, color, icon 하나에만 의존하지 않는다.
- app icon과 generated visual에는 [`image-assets.md`](image-assets.md)를 적용한다.

## Minimum maintained Markdown

- `AGENTS.md`
- `README.md`
- 제품 범위/MVP 문서
- architecture 또는 data model 문서
- design/UX 문서
- 실제로 권한·배포·복구가 있는 경우에만 해당 운영 문서
