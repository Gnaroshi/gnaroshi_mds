# UI/UX preferences

사용자 화면의 설계·구현·검증에 적용한다. DOM/CSS/ARIA 조건은 웹·webview에 적용하고 native에서는 대응하는 플랫폼 control과 접근성 semantics를 사용한다.

## Desired experience

처음 사용하는 사람이 다음을 즉시 파악할 수 있게 한다:

1. 이 app/program은 무엇을 위한 것인가?
2. 지금 상태는 무엇인가?
3. 먼저 무엇을 준비해야 하는가?
4. 어떤 순서로 실행해야 하는가?
5. 다음 행동과 그 결과는 무엇인가?

## Design iteration and reference interpretation

- 진행 중인 디자인 개선 과업에서 후속 비판은 별도 중단·범위 변경 지시가 없는 한 기존 범위 안의 반복 개선 요청으로 이해한다.
- 누적된 사용자 의견이 충분하면 새 reference를 다시 요구하며 수정을 미루지 않는다.
- 개선점 audit는 이전에 승인·제외·보류한 결정을 먼저 적용한다. 요청된 항목 수를 채우려고 이미 거절된 기능, 원문 문서에 맡긴 설명, 독자의 전문성을 무시한 안내를 다시 제안하지 않는다. 프로젝트별 결정은 해당 저장소에 남기며 사용자가 범위를 바꾸기 전까지 후속 검토에도 유지한다.
- 이전 버전으로 되돌린 뒤 개선하라는 요청은 지정 버전의 component 구조와 선택 표현을 기준으로 복원하고, 지적된 결함을 그 안에서 보완한다. 복원을 별도 재디자인으로 대체하지 않는다.
- 지침과 reference에서는 위계·밀도·상호작용의 의도를 해석하고, font·window·margin·padding 수치나 특정 앱의 외형을 그대로 복제하지 않는다. 현재 제품의 사용 목적과 플랫폼·접근성 제약에 맞게 독립적으로 설계하고 실제 크기에서 검증한다.
- 디자인 지침의 기본 패턴을 모든 표현에 대한 금지 규칙으로 해석하지 않는다. 사용자가 창의적인 직접 조작이나 탐색을 요청하면 승인된 방향과 피드백의 의도를 우선해 별도의 상호작용을 설계한다. 체크리스트 항목을 채운 정지 화면이나 미세한 hover 변화만으로 그 요청을 완료했다고 판단하지 않으며, 실제 조작 결과와 전체 읽기 흐름으로 검증한다. 데이터 진실성, 작업 보존, 가독성과 접근성은 표현상의 예외와 구분해 유지한다.
- Reference를 고를 때 먼저 surface를 작업용 app, 읽기 중심 문서, 홍보·브랜드 화면으로 구분한다. 작업용 app의 익숙한 control·시스템 폰트·밀도·일관성은 차별화 부족이 아니다. 개성은 제품의 목적을 설명하는 지점에 집중하고 매 화면의 장식으로 반복하지 않는다.
- 외부 design Markdown은 원저자, 정확한 파일, 확인일과 가능한 파일별 변경일을 기록한다. 공식 플랫폼 제약, 접근성 기준, 특정 design system 내부 규칙과 미학적 취향을 분리한다. 최신성·유명도만으로 기존 결정을 바꾸지 않으며 충돌하는 규칙은 적용/유지/제외 이유를 남긴다. 원문 비교는 [출처와 적용 판단](../references/design-sources.md)를 참고한다.

## Highest-priority user-facing information boundary

Safety, accessibility와 data integrity를 훼손하지 않는 범위에서 다음 규칙을 다른 density, decoration, dashboard completeness 요구보다 우선한다.

- 기본 화면에는 사용자가 지금 이해·결정·실행해야 하는 정보만 둔다. 문구나 값 하나를 제거해도 사용자의 판단, 안전 또는 다음 행동이 달라지지 않으면 숨긴다.
- Repository/local path, executable, raw command, PID, hash, schema/version, API/backend/provider 명칭, environment variable, artifact filename과 raw log는 developer-facing detail이다. Primary navigation, dashboard, floating intake/status window, routine result card와 일반 error 본문에 노출하지 않는다.
- 일부 사용자가 troubleshooting, audit 또는 호기심으로 확인할 수 있는 정보는 `Settings > Advanced/Diagnostics`, explicit `Details`, Reports 또는 Logs에 progressive disclosure로 배치한다. 기본값은 off/collapsed이고, 기술 정보가 primary action보다 먼저 보이지 않게 한다.
- Error와 warning은 평이한 실패/영향 요약, 보존된 것과 next action을 기본으로 보여준다. Copy 가능한 error code, command와 raw output은 별도 technical detail에 둔다.
- Safety warning, destructive scope, privacy·비용 영향, blocker와 recovery action은 사용자 결정에 필요한 정보이므로 숨기지 않는다. 같은 사실을 반복하는 장문 설명은 한 번의 짧은 consequence-oriented 문구로 합친다.
- 구현 후에는 primary UI source에 developer-facing literal이 다시 들어오지 않도록 focused copy test 또는 lint를 유지한다.

## Required

- 화면마다 하나의 명확한 목적과 primary action을 둔다.
- prerequisite, blocker, progress, result, next action을 같은 workflow 안에서 연결한다.
- 중요한 정보는 한 번에 scan 가능하게 하고 세부사항만 progressive disclosure한다.
- empty, loading, error, success, disabled, permission-denied state를 설계한다.
- 버튼은 결과를 예측할 수 있는 동사를 사용한다.
- User-facing copy는 target locale에서 실제로 쓰는 자연스러운 용어와 문장 구조를 사용한다. 직역투, 불필요한 영어·developer jargon과 같은 개념의 표현 변형을 피하고, 대표 workflow 전체에서 terminology와 tone의 일관성을 검증한다.
- destructive action은 일반 action과 분리하고 변경 범위를 표시한다.
- 되돌릴 수 있는 routine apply는 최신 preview와 backup 상태를 같은 맥락에 표시하고 한 번의 명시적 action으로 실행한다. 위험을 낮추지 않는 긴 typed phrase, 중복 checkbox와 반복 설명을 confirmation처럼 쌓지 않는다. Irreversible 또는 recovery가 불확실한 작업만 typed confirmation처럼 더 강한 friction을 사용한다.
- navigation 선택지가 상호 배타적이면 direct link, tab, 또는 한 번에 하나만 열리는 disclosure를 사용한다. 여러 navigation disclosure가 독립적으로 열린 채 중첩되지 않게 한다.
- 하나의 navigation scope 안에서는 current/selected 상태가 하나만 보여야 한다. Route current, hash/location current, selected tab이 동시에 peer item처럼 보이면 안 되며, page-level current와 in-page current를 함께 보여야 하면 hierarchy를 분리하거나 route current를 비활성화한다.
- Current item은 시각 affordance와 semantics가 일치해야 한다. 현재 item이 inert label이면 hover, pointer, click/reload affordance를 제거하고, link로 유지한다면 repeated action의 의미와 selected style을 명확히 구분한다.
- 공개 evidence나 실제 기능이 없는 capability는 disabled menu나 빈 dashboard로 광고하지 않고 숨긴다. route 보존이 필요하면 direct navigation에서 제외한다.

## Interaction response contract

모든 interactive component는 실행 가능 여부뿐 아니라 사용자의 행동이 어떻게 처리됐는지 같은 맥락에서 보여준다.

- Action마다 idle, pending, success, error와 retry/next-action 상태를 정의한다. 비동기 action은 중복 실행을 막고, 진행 중 label 또는 indicator와 완료 결과를 제공한다.
- Pending label과 indicator는 control의 폭과 주변 layout을 불필요하게 바꾸지 않는다. Button content와 feedback region은 예상 가능한 최소 크기를 예약해 상태 변화 때문에 인접 control이나 작성 surface가 이동하지 않게 한다.
- 공간 예약은 실제 발생하는 상태에만 적용한다. 오류나 결과를 그 위치에 표시하지 않는 field마다 빈 feedback 행을 두지 않는다. 같은 행의 button은 빈 예약 영역이 아니라 실제 input의 baseline·중앙에 맞춘다.
- 반복되는 card/list action column은 label 길이마다 자체 폭을 계산하지 않는다. 같은 hierarchy의 button은 공통 control height, icon-label gap, vertical baseline과 column width를 공유하고, 긴 label은 정해진 wrap/compact policy로 처리한다. Card별 button 폭과 수직 위치가 제멋대로 달라지면 기능이 동작해도 PASS가 아니다.
- Task-generated feedback은 trigger, field 또는 affected item 가까이에 둔다. Page-wide 문제만 page feedback region에 두고, 별도 작업의 message를 한 global banner에 섞지 않는다.
- Inline feedback과 page feedback region은 기존 content를 덮거나 가리지 않는다. Conditional message가 중요한 editor, list, form 또는 control을 밀어내는 경우 reserved region, replacement state 또는 명시적 transition layout을 사용한다.
- Modal alert는 data loss, irreversible action, credential/security 경계처럼 즉시 결정을 요구할 때만 사용한다. 일반 success, retry 가능한 fetch failure와 상태 정보는 current context 안에서 전달한다.
- Success가 결과 자체로 명확하면 불필요한 message를 추가하지 않는다. 결과가 offscreen이거나 canonical write, copy, import, external launch처럼 확인이 필요하면 짧고 persistent한 context feedback을 제공한다.
- Error는 무엇이 실패했는지, 보존된 것은 무엇인지, 다음 valid action을 함께 말한다. 자동 dismiss toast를 error 또는 유일한 recovery 안내로 사용하지 않는다.
- 여러 단계의 작업에서는 현재 단계와 미완료 이유를 함께 표시한다. 실패 항목마다 펼칠 수 있는 해결 안내와 해당 설정·문서로 이동하는 action을 제공한다. 내부 오류 문자열로 문서를 추측하지 말고 구조화된 원인과 stable ID로 대상을 찾으며, 안내를 여는 것만으로 수정·공개하지 않는다.
- Action이 새 view, item 또는 dialog를 열면 focus와 selection을 새 context로 이동하고 돌아갈 위치를 보존한다. Screen reader에는 live region을 사용하되 같은 message를 여러 `role=alert`로 중복 발표하지 않는다.
- 비동기 action의 완료 후 focus 이동은 그 action이 아직 사용자 의도를 소유할 때만 한다. 대기 중 다른 control·단계를 선택하거나 keyboard navigation·창 전환을 하면 예약된 focus를 취소한다. 완료로 trigger가 사라지면 새 작업면의 heading 같은 명확한 위치를 제공하되 background refresh·polling은 focus를 가져가지 않는다.
- 이 의도는 결과를 받은 뒤가 아니라 action을 시작할 때 기록한다. 대기 중 창을 떠났다가 돌아왔거나 다른 작업을 선택했다면, 완료 시점에 같은 control이 보인다는 이유로 취소된 focus 요청을 되살리지 않는다. 준비 지연·이탈 후 복귀·취소·실패·unmount에서 listener 정리와 focus 비이동을 검증한다.
- 반복해서 사용하는 목록·section의 펼침 상태는 역할에 맞는 초기값과 사용자의 마지막 명시적 선택을 구분한다. 선택 이후에는 filter·tab 이동, 새 데이터 수신이나 일반 action이 이를 덮어쓰지 않도록 유지한다. 숨겨진 결과의 feedback·접근성 focus는 section trigger에서 제공할 수 있으며, 상태 복원과 초기값을 각각 재실행으로 검증한다. 기술 진단·위험한 세부정보의 기본 숨김 규칙은 유지한다.
- Async action 중 관련 input, selection과 navigation이 결과와 충돌할 수 있으면 operation scope만 잠근다. App 전체를 이유 없이 막지 않고, stale response가 새 selection을 덮지 않도록 request identity/cancellation을 적용한다.
- `Continue`, `Resume`, `Retry`처럼 이전 상태를 이어가는 동사는 대상과 복원 지점을 증명할 수 있을 때만 사용한다. 사용자가 무엇을 이어가는지 알 수 있도록 document/item, 단계 또는 pass, 마지막 상태와 필요하면 elapsed time을 같은 맥락에 표시한다. 단순히 과거 기록이 있다는 이유로 `Continue`라고 부르지 않는다.
- State-transition test는 각 상태를 따로 확인하는 데서 끝내지 않는다. "A가 current일 때 B는 current가 아니다", "current item은 한 개다", "stale async result가 새 selection을 덮지 않는다" 같은 negative invariant를 포함한다.
- Minimal interface를 정지 화면으로 해석하지 않는다. Owner가 contemporary interaction을 요구하면 직접 선택·드래그·탐색하는 대상과 결과를 먼저 설계하고 navigation destination, reading/task progress, current/pressed/open state에 맞는 motion을 연결한다. 현재 단계는 색이나 진행선만으로 표시하지 않고 구별되는 형태와 명시적인 label을 함께 제공한다. 자동 loop, custom cursor와 decorative parallax는 기본적으로 추가하지 않는다. 명시적으로 승인된 시각 실험은 목적·범위·성능 비용을 프로젝트에 기록하고, motion-only feedback을 피하며 reduced-motion에서는 같은 내용을 조작할 수 있게 한다.
- Motion acceptance는 animation 선언 유무가 아니라 정상 속도에서 변화가 인지되는지로 판단한다. 시작·중간·종료 frame 또는 실제 계산값을 비교하고, text contrast와 layout geometry는 모든 frame에서 유지하며, reduced-motion에서는 동일한 정보와 action state를 즉시 제공한다.
- Interactive web experience를 요청하면 첫 주요 탐색 경로에 발견 가능한 state-changing 조작을 제공한다. Hover 반응이나 숨겨진 identity 효과만으로 사이트 전체의 interactive 요구를 충족했다고 보고하지 않는다. 선택·직접 조작은 실제 content와 맥락을 바꾸며, pointer·touch·keyboard와 정적 fallback에서 같은 정보 경계를 유지한다.
- Owner가 immersive 3D와 pointer-reactive background를 명시적으로 요청하면 작은 hover·carousel 개선으로 범위를 축소하지 않는다. 첫 viewport에서 발견되는 실제 공간 장면과 직접 조작을 검수하며, 관련 사례는 가능하면 로딩 화면이 아니라 완성된 장면과 입력 후 상태까지 직접 확인한다. 접근·렌더링이 막힌 사례는 확인한 부분과 미확인 부분을 분리해 기록한다.
- Expressive scene은 text·navigation·실제 evidence와 다른 rendering layer로 둔다. Pointer나 camera가 움직이는 동안에도 본문 영역을 침범하지 않으며, abstract illustration을 측정 결과나 실제 제품 상태처럼 설명하지 않는다. Renderer load 성공만으로 통과시키지 말고 실제 painted pixels, 입력 전후 형태 변화, pause, offscreen stop, 최소 화면의 framing을 확인한다.
- 공간 장면도 페이지의 주제·실제 자료·탐색 결과를 연결해야 한다. 무관한 도형을 여러 페이지에 반복하거나 숨겨진 효과만 추가해 interactive 요구를 충족했다고 판단하지 않는다. 참고 사례는 실제 구현·공개 source·prompt 예시를 구분하고, prompt 파일만 있는 저장소를 검증한 앱으로 소개하지 않는다.
- Ambient motion이 승인되면 시작·입력 후의 실행 시간, frame/pixel budget과 명시적인 정지 control을 정한다. 정지 선택을 navigation과 locale 변경 뒤에도 존중하고, reduced-motion과 graphics failure에서 같은 콘텐츠·핵심 경로를 유지한다. 조작이 없는 동안 계속 GPU를 사용해야 할 이유가 없으면 render를 멈춘다.
- FPS 제한과 timer만으로 최적화를 선언하지 않는다. 같은 기기·viewport·입력에서 변경 전후 main-thread 작업·초기 전송량·idle 비용을 비교하고, 개발 서버와 production build를 구분한다. CPU 제한 실험은 실험 조건과 한계를 함께 기록하며 실제 사용자 지표로 과장하지 않는다.
- 여러 페이지의 interactive 개선은 각 페이지의 정보와 사용자 목적에 맞는 조작으로 설계한다. 하나의 효과를 모든 페이지에 반복하지 않으며, 선택 전후·키보드 포커스·애니메이션 중간·최소 화면에서 인접 component의 간격과 가림을 실제 화면으로 검증한다.
- Owner가 창의적인 개인 identity interaction을 명시적으로 요청하면 작은 hover 효과만으로 요청을 충족했다고 보고하지 않는다. 승인된 identity를 보존한 opt-in 변형·입체·재질 반응을 실제 입력과 상태 전환으로 구현할 수 있다. 본문·근거 미디어와 분리하고 keyboard, reset, reduced-motion, 실패 시 원본 fallback을 제공하며, 무거운 engine은 요청 시에만 load하고 idle·offscreen·background에서는 render를 멈춘다.
- Motion의 체감도를 높이려고 section 전체를 이동시켜 인접 content와의 거리를 벌리지 않는다. 같은 scroll 위치의 일반·reduced-motion 화면에서 관계별 간격을 비교하고, current state·방향·요청한 펼침에 움직임을 집중한다. 글자나 수치를 읽어야 하는 evidence media는 hover 확대·inset 장식으로 잘라내지 않으며, 강조와 확대 열기를 구분한다.
- Experimental interaction API는 normal navigation, reload, locale switch, focus 또는 requestAnimationFrame lifecycle을 불안정하게 만들면 해당 경로에서 opt out하거나 안정된 fallback으로 되돌린다. 최신 기술 사용 자체를 acceptance criterion보다 우선하지 않는다.
- Hidden accessibility instruction은 실제 interaction contract와 일치해야 하고 layout utility가 정의되지 않아 visible text로 새지 않도록 component test와 packaged runtime에서 확인한다. Keyboard 도움말이 routine task에 필요하지 않으면 toolbar의 Help/Guide처럼 요청 가능한 위치로 이동한다.

## Timeline과 interactive plot

- 시간 순서의 관측·trajectory viewer는 Space로 재생/정지하고 좌우 화살표로 이전/다음 시점을 탐색할 수 있게 한다. Text input, select와 편집 영역의 기본 키 동작을 가로채지 않고 재생 중 이동, 첫/마지막 시점과 키 반복을 검증한다.
- 회전·드래그 가능한 plot은 실제 point 위에서 pointer down→move→up을 실행해 검증한다. 확대 가능한 3D plot은 실제 wheel/trackpad 입력으로 확대하고 이어서 drag로 회전하는 연속 동작을 검증한다. 확대와 회전 control의 기능·현재 mode를 명확히 표시하고, 확대 뒤에도 회전할 수 있어야 한다. Click callback에서 active drag 중 scene을 재생성하지 않으며, 시점 선택·재생 갱신은 확대 배율, camera와 pointer 상태를 보존한다. 정적 screenshot, 개별 mode 전환이나 camera 값을 직접 설정한 검증으로 실제 입력에 따른 연속 동작 검증을 대신하지 않는다.

## Information hierarchy and density

- Navigation group과 screen heading은 implementation layer가 아니라 사용자 목표와 결과를 이름으로 사용한다. 한 item만 가진 group, 모호한 container label과 raw technical noun은 grouping 이득이 없으면 합치거나 이름을 바꾼다. 이름만으로 대상의 역할이 분명하지 않으면 처음 보는 사람이 구분할 수 있는 짧은 역할 label을 함께 표시하되, 주변 제목이나 선택 상태가 이미 역할을 알려주면 반복하지 않는다.
- SPA 형태의 작업 도구는 일정·장소·준비·예산처럼 서로 다른 작업을 독립 화면으로 전환한다. 선택한 날짜·항목, 검색·필터, 입력과 목록 위치를 화면 이동 뒤에도 보존하고 뒤로·앞으로·직접 주소 진입을 지원한다. 모든 작업을 긴 문서에 나열한 뒤 anchor로 이동하는 방식으로 대체하지 않는다.
- Current location, primary task와 next action은 secondary status, repository path, hash, schema/version detail보다 먼저 보여준다. Raw provenance와 diagnostic value는 사용자가 요청할 때 disclosure, Details 또는 inspector에서 보여준다.
- Empty state의 primary action은 사용자가 방금 막힌 workflow의 다음 유효 단계로 이어져야 한다. 일반 adjacent page, broad research page, marketing page로 보내는 CTA는 그곳이 실제 다음 행동일 때만 primary로 둔다.
- Master-detail에서 collection이 비어 있으면 왼쪽 `No items`와 오른쪽 `Select an item`을 동시에 렌더링하지 않는다. 하나의 empty state가 prerequisite와 다음 action을 소유하며 불필요한 빈 detail pane은 제거한다.
- Empty state의 생성 action과 screen header의 같은 생성 action을 동시에 primary로 반복하지 않는다. Collection이 비었을 때는 empty state가 다음 action을 소유하고, record가 생긴 뒤에는 persistent header action으로 전환할 수 있다.
- Count가 0이고 empty state 자체가 그 사실을 설명하면 heading 옆의 `0` badge를 반복하지 않는다. Count는 비교, triage 또는 navigation 결정을 실제로 바꿀 때만 표시한다.
- `Now`, `Current`, `Recent`, freshness, health처럼 시간성을 주장하는 surface는 공통 freshness policy를 공유한다. 같은 data가 한 화면에서는 stale로 숨겨지고 다른 화면에서는 current로 보이면 안 되며, stale이면 last updated, 영향, 다음 확인 경로를 표시한다.
- 한 card에서 같은 target을 가리키는 image, title, text CTA가 반복되면 tab stop을 최소화한다. 전체 card click handler 대신 필요한 실제 anchor만 남기고 evidence caption은 숨기지 않는다.
- 긴 상세 페이지는 local navigation을 추가하기 전에 중복 section과 반복 copy를 먼저 줄인다. 줄인 뒤에도 긴 경우 stable heading ID와 permalink, keyboard-accessible local navigation을 제공한다. 읽기 중심 페이지는 공간이 충분한 desktop에서 본문 옆 목차로 현재 section과 subsection을 보여 주고, 좁은 화면에서는 같은 계층을 펼침 메뉴로 제공한다. 메뉴가 닫혀 있어도 현재 subsection을 trigger에 표시해 상위 section명만으로 위치를 뭉뚱그리지 않는다. Scroll과 직접 이동 모두 현재 위치를 갱신하며, 본문 폭을 침범하지 않고 페이지 처음으로 돌아갈 경로를 제공한다.
- 여러 단계의 section이 있는 긴 문서는 `2`, `2-a`처럼 상위·하위 관계가 드러나는 번호를 제목과 목차에 일관되게 사용한다. 화면 폭에 따라 목차 배치는 바뀔 수 있지만 번호·읽는 순서·현재 위치는 유지한다. 번호를 제목이나 의미 있는 label 대신 쓰지 않는다.
- Spacing은 먼저 관계를 표현한다. 가까운 요소는 같은 task group, 더 큰 간격은 section boundary를 뜻한다. Divider는 scrolling region, navigation group 또는 의미가 다른 dense row처럼 공간만으로 경계가 불충분할 때 일관되게 사용한다.
- Compactness는 중복 heading·metadata·container·누적 inset을 제거한 결과여야 한다. Icon의 그림 크기와 실제 hit area를 구분하고 text 확대, touch target, keyboard/focus를 희생하지 않는다. Context에 이미 보이는 metadata는 반복하지 않되 현재 filter·sort·paused 같은 결정에 필요한 상태는 숨기지 않는다.
- 여백 검수는 화면 전체의 빈 면적 비율이 아니라 관계별 budget으로 한다: header→첫 유효 content, row 내부, section 사이, fixed action→keyboard/safe area. 짧은 실제 목록 아래의 여유 공간은 오류가 아니며 filler나 큰 row로 채우지 않는다. 문구·component의 추가·재설계·삭제·축약마다 같은 fixture·viewport·text size의 전후 측정과 screenshot으로 정렬·위계와 누적 padding, 잘림, 겹침을 확인한다. Container 경계만 재지 말고 실제 글자·수치·아이콘 사이 거리와 기준선을 확인하며, 함께 읽는 비교 값을 남는 폭만큼 벌리지 않는다.
- 같은 경계를 sticky/local navigation의 surface와 바로 뒤 full-width divider로 반복하지 않는다. Sequence connector는 실제 numbered step 사이를 이어 인과나 순서를 설명해야 하며, 내용 아래에 독립적으로 남는 선은 제거하거나 의미가 드러나는 grouping으로 바꾼다.
- Font size만으로 hierarchy를 만들지 않는다. 역할·weight·alignment·grouping을 먼저 정하고 본문을 caption으로 축소하지 않는다. Web의 caption 12 CSS px, control 13–14 CSS px, 긴 authoring text 15–17 CSS px는 시작점이지 native 최소값이나 모든 제품의 고정값이 아니다. Native는 플랫폼 semantic text style과 확대 동작을 사용하고 실제 EN/KO·긴 content·큰 text에서 검증한다. 사용자 확대 설정을 무시하는 고정 작은 글자로 compactness를 만들지 않는다.
- Typography, spacing, radius, divider와 control height는 semantic token으로 제한한다. Component마다 임의 값으로 밀도를 미세 조정하지 않는다. 글자 크기를 바꾸면 line-height, cell padding·행 높이, 제목·보조 정보의 줄바꿈, 고정 열 폭, 배경 면적과 구분선도 함께 재조정한다. 같은 content·viewport에서 전후를 비교해 잘림뿐 아니라 시각적 밀도·정렬·위계가 자연스러운지 검토한다.
- Color는 identity, action/selection, semantic status, neutral hierarchy로 역할을 나눈다. 사용자 지정 category 색이 error/success 상태를 대신하지 않으며 동일한 역할은 화면·widget·editor에서 이어진다. 전경/배경 조합을 light/dark 각각 검증하고 선택·완료·오류는 shape, label 또는 symbol로도 구분한다. 저장된 사용자 색과 접근성을 위한 display color 보정은 분리한다.
- Minimum supported window에서 primary navigation label을 모두 숨겨 icon-only로 만들지 않는다. Reflow, narrower but readable label, disclosure 또는 secondary action 축소를 먼저 사용한다.

## Forms and metadata authoring

- 사용자가 identifier, URL 또는 existing record로 시작할 수 있으면 metadata lookup/import를 manual entry보다 먼저 제공한다. 자동 입력값의 source와 lookup state를 표시하고 생성·저장 전에 사용자가 검토할 수 있게 한다.
- 첫 단계는 record 생성에 정말 필요한 최소 field와 사용자 intent만 요구한다. Publication, provenance, advanced analysis와 드물게 쓰는 metadata는 record가 만들어진 뒤 progressive disclosure한다.
- 각 field는 persistent label, plain-language purpose, required/optional 상태, realistic example 또는 format hint, validation과 recovery guidance를 필요에 따라 제공한다. Placeholder만으로 label이나 instruction을 대신하지 않는다.
- Validation은 사용자가 입력하기 전부터 error를 표시하지 않는다. Submit 또는 blur 뒤 invalid field 가까이에 이유와 valid example을 제공하고, 여러 error가 있으면 summary에서 해당 field로 focus를 이동할 수 있게 한다.
- Comma-delimited string처럼 사용자가 format을 기억해야 하는 입력은 domain이 list라면 token/list editor, repeated row, autocomplete 또는 paste normalization을 우선한다. Manual raw source editing은 escape hatch로 유지할 수 있다.
- Auto-filled, user-edited, required-missing과 source-stale 상태를 구분한다. Source refresh가 user edit을 덮을 수 있으면 diff/preview 또는 explicit overwrite selection을 제공한다.
- Metadata와 long-form authoring이 경쟁하면 minimum window에서 좁은 multi-column form으로 모두 압축하지 않는다. Details mode, labeled inspector 또는 context switch로 충분한 width를 주고 authoring state와 focus를 보존한다.

## Component-level review loop

- 시각 방향을 반복 탐색하는 단계에서는 기본 글자 크기의 핵심 동선·밀도·실제 조작부터 검증한다. Owner가 검수 시점을 지정하면 최대 Dynamic Type 등 확대 크기의 전체 검수는 최종 배포 gate로 미루고 현재 반복마다 다시 실행하지 않는다. 기존 글자 확대 지원·읽기 순서·터치 영역은 제거하거나 작은 고정 글씨로 대체하지 않는다.
- Broad UI change는 screen 전체에 대한 vague approval 한 번으로 끝내지 않는다. Navigation, form, editor toolbar, dialog, list row, status/feedback, destructive action처럼 변경 component를 나눠 review한다.
- 각 component review는 purpose, expected action/result, idle/pending/success/error, keyboard/focus, narrow window, dark/light, content length, layout stability와 regression을 pass/fail로 기록한다. 글자·문구·component 변경은 실제 content의 상·우·하·좌 inset과 인접 component 간격을 측정하고, 같은 역할의 다른 instance에서도 짧은/긴 label·기본/선택 상태·숨겨진 panel을 연 상태를 비교한다. 검토한 instance·viewport·상태별 측정값과 screenshot 경로를 프로젝트 검증 기록에 남기며, font size 일치나 overflow 없음만으로 여백·디자인 검수를 통과시키지 않는다.
- Reviewer가 `OK`를 주려면 blocker가 없다는 말뿐 아니라 acceptance criterion별 증거를 남겨야 한다. Fail 또는 ambiguous item은 같은 component를 수정하고 다시 review한다.
- Source 문자열·정적 markup 검사는 실제 control 조작, mode 전환, 저장/되돌리기, resize와 focus 검증을 대신하지 않는다. 재현 가능한 browser/component harness는 제품 component를 직접 사용하고, 전시용으로 따로 만든 UI를 제품 동작의 증거로 쓰지 않는다.
- Component들이 통과한 뒤 전체 workflow에서 hierarchy, state continuity와 cross-component feedback을 다시 검증한다. 같은 역할의 글자·조작·caption이 다른 section에서도 일관되는지 실제 화면으로 비교하고, 좁은·일반·넓은 폭과 선택 상태 전환에서도 관계별 간격을 확인한다. Component pass가 전체 product flow pass를 대신하지 않는다.
- Clipping 검사는 바깥 button·card의 경계만 재지 않는다. 내부 title·label·상태 문구가 실제로 사용할 수 있는 폭도 확인한다. Icon이 제거된 뒤 오래된 grid track이 남는 경우처럼, container가 정상 크기여도 핵심 문구가 잘리면 실패다.
- 전면 검수를 요청받으면 실제 route·보조면·dialog·공통 control을 목록화하고 빠진 곳을 확인한다. 기능 test, 실제 입력, 화면 조합의 시각 검토와 설치본 검증을 구분해 기록하며 일부 대표 screenshot이나 source 문자열 검사로 전체 통과를 선언하지 않는다. 이전 완료 판단과 사용자 재현이 충돌하면 해당 acceptance를 다시 연다.
- Packaged WebView 앱은 routine 우클릭에 Reload·개발자 도구 같은 browser chrome을 노출하지 않는다. 표준 text 편집·선택·복사 메뉴는 보존하고 실제 native context menu와 keyboard 경로를 검증한다. 오류 복구를 위한 재시작은 미저장 내용을 보존하는 명시적 제품 동작이어야 한다.
- Desktop 검증 대상은 [app-distribution](app-distribution.md)의 signed stable install이다. Representative record로 navigation, edit/revert, mode, pending/result/error, destructive entry point와 minimum window를 검증한다. 창 실행은 [공통 작업 보존 규칙](../AGENTS.md#검증과-사용자-작업-보존)을 따른다.

## Avoid

- 없어도 의미가 같은 text, 반복 안내, marketing filler, 장황한 설명
- 장식만을 위한 card, badge, gradient, animation, icon
- 승인된 identity나 실제 evidence를 대신하는 큰 initial/monogram/placeholder tile
- 서로 전혀 맞지 않는 padding/margin과 임의 spacing 값
- card 안의 card, 불필요한 border와 shadow
- 작은 viewport에서 잘리는 text, button, form, table, navigation
- hover-only 정보, color-only status, 이유 없는 disabled control
- 반응형이라는 이유로 중요한 기능이나 정보를 숨기는 것

## Gnaroshi interface palette

Gnaroshi 앱의 기본 방향은 dark working theme과 제한된 pastel accent다. 프로젝트의 승인된 palette가 있으면 우선하며, identity를 이유로 검증된 웹 interaction palette를 교체하지 않는다.

### Base dark surfaces

| Token | Recommended color | Use |
| --- | --- | --- |
| `surface-near-black` | `#11151B` | app canvas, deepest background |
| `surface-charcoal` | `#181E26` | primary panel and sidebar |
| `surface-blue-gray` | `#222B38` | raised/inset surface |
| `text-primary-dark` | `#F4F7FA` | primary text on dark surfaces |
| `text-secondary-dark` | `#B7C0CC` | secondary text after contrast verification |

Pure black을 기본 canvas로 사용하지 않는다. Surface hierarchy는 spacing과 제한된 separator를 함께 사용하고 card-within-card decoration으로 만들지 않는다.

Identity teal/orange와 앱별 role accent 값은 [app-icons](app-icons.md#색과-role)를 사용한다. Status는 별도 semantic token과 text/icon으로 표시한다. Pastel filled control의 foreground contrast를 확인하고, light mode도 navigation·focus·disabled·error·chart·form을 모두 지원한다. Neon, glow, gradient text와 전체 surface의 gradient를 피하며 gradient는 필요한 identity artwork나 제한된 accent에만 사용한다.

## Pixel visual layer

Owner-selected pixel direction은 content를 retro-game interface로 바꾸는 theme가 아니라 identity와 interaction chrome에 적용하는 공통 visual grammar다.

- Pixel treatment는 app/product identity, launcher tile, small role glyph, border corner, separator, focus ring, selected navigation marker와 primary control edge에 우선 적용한다.
- Body text, long-form writing, mathematical notation, code readability와 실제 product screenshot은 pixelation하지 않는다.
- Body와 prose에 bitmap font를 강제하지 않는다. 제한된 eyebrow, technical label 또는 display accent에는 system mono를 사용할 수 있지만 EN/KO legibility를 실제 크기에서 검증한다.
- Border, corner, shadow와 spacing은 2px 또는 4px step을 반복해 family grammar를 만든다. Component마다 임의의 pixel decoration을 추가하지 않는다.
- Rounded pill, soft blur shadow, glassmorphism과 pixel step을 한 component 안에서 혼합하지 않는다.
- Pixel shadow는 depth가 필요한 primary control 또는 identity tile에만 짧고 hard-edged하게 사용한다. 모든 card를 떠 있는 game inventory slot처럼 만들지 않는다.
- Actual app role은 key color와 canonical role glyph로 구분한다. 색만으로 app 또는 status를 구분하지 않고 accessible label을 유지한다.
- Light/dark mode에서 동일 geometry를 유지하고 palette와 contrast만 조정한다.
- Reduced motion, keyboard focus, zoom, long Korean copy와 minimum viewport requirements는 pixel style보다 우선한다.

## Layout verification

- spacing token을 만들고 component 내부/사이 간격의 역할을 구분한다.
- 지원 최소 크기, 일반 크기, 넓은 크기에서 검증한다.
- Flex column 안의 tab/segmented row는 content가 많아도 높이가 0으로 shrink되지 않게 `flex-shrink`, minimum block size와 scroll ownership을 검증한다. Horizontal overflow를 설정하면 암묵적인 vertical clipping이 생기지 않는지 실제 bounding box로 확인한다.
- 긴 번역, Dynamic Type 또는 browser zoom, 실제 content 길이를 사용한다.
- wrap과 reflow가 우선이며 data table/code처럼 필요한 경우에만 명시적 scroll을 사용한다. 배치 전환은 usable content width와 실제 label·control·media의 읽을 수 있는 최소 폭으로 정한다. 넓은 mobile breakpoint 하나로 아직 함께 들어가는 요소를 모두 세로로 쌓지 않으며, 전환 직전·직후 폭에서 줄 수·전체 높이·비교 가능성을 확인한다.
- screenshot과 실제 runtime 조작으로 clipping, overlap, overflow를 확인한다. Sticky/fixed control의 offset과 예약 영역은 실제 header/navigation 경계·control 높이·safe area로 정한다. Content 시작·중간·끝과 고정 진입·해제 위치를 실제로 scroll하여 본문·media·인접 control의 가림을 확인한다. 지속 접근이 요청된 control은 content를 가리지 않는 예약 영역에 유지하며, 가림을 해결한다는 이유로 고정을 제거하지 않는다. 지속 접근이 필요 없으면 일반 흐름으로 되돌릴 수 있다. 조작에 계속 닿는다는 사실만으로 검증을 통과시키지 않는다.
- 순서가 중요한 flow diagram은 intermediate breakpoint에서도 읽는 순서와 causality가 유지되어야 한다. Connector를 숨긴 fallback을 2-column grid로 바꿀 때는 numbering, row order와 visual grouping이 단계 순서를 흐리지 않는지 검증한다.

## Resizable workspace surfaces

- Sidebar/content, master/detail, editor/inspector와 editor/preview처럼 사용자가 작업 폭을 선택해야 하는 경계는 재사용 가능한 resizable pane primitive를 사용한다. 화면별 absolute width와 ad-hoc pointer handler를 반복하지 않는다.
- Divider는 focus 가능한 `separator` widget으로 구현하고 orientation, current/min/max value와 대상 pane을 accessible name으로 제공한다. Pointer뿐 아니라 Arrow key, 큰 step, min/max 이동과 collapse/expand를 keyboard로 제공한다.
- Drag 시작 시 pointer capture와 text-selection 방지를 사용하고 종료/cancel/lost capture에서 모두 정리한다. Divider를 끌다가 문서 text가 선택되거나 resize cursor가 app 전체에 남지 않게 한다.
- 합리적인 pane별 minimum, maximum과 primary content minimum을 동시에 적용한다. Persisted size가 현재 usable viewport를 벗어나면 안전하게 clamp하되 사용자의 저장값을 불필요하게 잃지 않는다.
- Double-click reset, explicit collapse/expand와 local persistence를 제공한다. Collapsed pane은 시각적으로만 0px이 아니라 focus와 accessibility tree에서도 제외하고, expand control은 계속 접근 가능해야 한다.
- 좁은 window에서 pane을 화면 밖으로 밀지 않는다. Side-by-side를 stacked로 전환하거나 방향 선택을 제공한다. Pane별 scroll과 유효 size를 보존하며 editor 내부 상태는 [authoring-editor](authoring-editor.md)의 document 경계를 따른다.
- Component test에는 clamp, malformed persistence, keyboard direction, separator semantics와 collapse state를 포함한다. Showcase에는 실제 drag 가능한 nested pane fixture를 두고 normal, minimum과 wide runtime에서 pointer/keyboard/reset/persistence를 다시 검증한다.

## Settings and form alignment

- 설정 화면은 label/detail 영역과 control 영역의 공통 column을 정의하고 모든 row가 같은 축을 사용한다.
- picker, text field, slider, stepper처럼 값을 편집하는 control은 같은 너비와 시작 위치를 공유한다.
- boolean 값은 임의 위치의 labelled checkbox로 두지 않고 공통 control column의 같은 축에 switch로 정렬한다.
- 한 기능에 종속된 세부 control은 parent toggle 바로 아래에 두고 기능이 꺼져 있으면 숨기거나 명확히 비활성화한다.
- preview, reset, open, verify 같은 command button은 값 편집 row와 섞지 않고 별도 action 영역으로 분리한다.
- 좁은 viewport에서는 label-over-control로 reflow하되 label, 설명, control의 의미 순서를 유지한다.
- 서로 다른 section에서 같은 의미의 설정은 같은 row component와 interaction pattern을 재사용한다.
- 정렬 breakpoint는 전체 window width가 아니라 navigation과 inset을 제외한 usable content width를 기준으로 검증한다. Table형 application override는 application/status/access/source처럼 의미 있는 column을 공유하고, 공간이 부족하면 label-over-control 순서로 stack한다.
- Manual save와 auto-save를 같은 화면에서 함께 사용하면 section 단위로 명시한다. Global Save가 자동 저장되는 section까지 저장하는 것처럼 보이지 않게 하고 각 action의 pending/result/error feedback을 해당 section에 예약한다.
- Manual Save는 canonical value와 다른 draft가 있을 때만 활성화한다. 안정된 위치에 `Saved`, `Unsaved changes`, `Saving`, `Error`를 표시하고 disabled primary control을 활성처럼 칠하지 않는다.
- Backup, cache와 Recovery처럼 운영 성격이 다른 설정은 한 card 안에 합치지 않는다. Recovery의 destructive action은 routine restore와 시각적으로 분리하고 exact item을 이름으로 표시한다.

## Overlay와 history control

- Popover, disclosure와 dialog의 semantic role은 실제 keyboard behavior와 일치해야 한다. Menu key handling을 구현하지 않은 일반 action list를 `menu/menuitem`으로 가장하지 않는다. Escape는 닫고 trigger로 focus를 돌리며 outside click과 mode change도 stale overlay를 남기지 않는다.
- History correction/delete는 row에서 발견 가능해야 하고 exact target과 영향 범위를 확인한다. Immutable audit source를 보존해야 하는 domain이면 correction event와 recoverable journal을 사용하고, interrupted write는 다음 read/list 전에 안전하게 resume하거나 conflict로 fail closed한다.
