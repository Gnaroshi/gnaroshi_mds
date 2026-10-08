# Web application guidance

웹 UI·API·공개 데이터·웹 배포에 적용한다. UI 변경은 [ui-ux](ui-ux.md), 편집기 구현은 [authoring-editor](authoring-editor.md)를 함께 적용한다.

## Ownership

- presentation, canonical content, generated public data, API를 가능한 한 분리하고 각 source of truth를 문서화한다.
- public site가 private research source를 직접 import하지 않게 한다.
- generated feed는 편집 surface가 아니며 publisher와 validator를 통해 갱신한다.
- API availability가 선택적이면 no-API fallback을 보존한다.

## UI and content

- 첫 viewport에서 정체성, 목적, 핵심 경로와 다음 행동이 보여야 한다.
- long-form content는 읽기 폭과 heading hierarchy를 우선한다.
- data가 없을 때 zero-filled dashboard를 보여주지 말고 첫 유효 행동 하나를 안내한다.
- 중요한 content를 mobile에서 숨기지 않는다.
- JavaScript와 image는 설명이나 상호작용에 필요할 때만 추가한다.
- Project/application page는 실제 product screen이나 검증 artifact로 핵심 user scenario를 보여 준다. Demo fixture를 사용하면 public caption에서 demo임을 숨기지 않는다.
- Project evidence media는 sighted user와 assistive technology 모두에게 같은 provenance boundary를 제공한다. Meaningful screenshot/diagram을 `aria-hidden` link 안에만 두지 말고, concise alt와 visible caption 또는 nearby evidence text를 함께 둔다.
- Generated concept scene, diagram, screenshot, demo fixture는 public page에서 서로 다른 media type으로 드러나야 한다. Disclosure가 alt text에만 있거나 developer document에만 있으면 public disclosure로 보지 않는다.
- 콘텐츠 언어와 고정 navigation label의 언어를 분리한다. Owner가 익숙한 영어 메뉴를 선택하면 번역된 본문에도 같은 메뉴명을 유지하고, breadcrumb·mobile·footer까지 일관되게 적용한다. 본문·날짜·실제 작업 안내는 해당 locale을 유지한다.
- Language switcher는 현재 locale을 selected/inert state로 표현한다. 번역이 없다는 설명은 언어 선택을 요청했을 때 keyboard와 touch로 접근 가능한 control 안에서 제공하며 header와 본문 위에 반복하지 않는다. 없는 번역을 있는 것처럼 연결하거나 계획이 확인되지 않은 `준비 중`을 표시하지 않는다. 다른 언어의 목록으로 보내면 해당 목적지를 명확히 이름 붙인다.
- 공개 글의 제목 앞에 content type·언어 배지·추정 읽기 시간 같은 metadata를 관례적으로 쌓지 않는다. 읽기 결정에 실제 필요한 날짜·출처 등만 남기며, 추정 읽기 시간과 실제 기록된 읽기 활동을 구분한다. 제목과 본문에 폭 제한을 중첩하지 않고 넓은 화면에서도 읽기 면적과 첫 본문 진입 위치를 검수한다.
- 실제 translation pair의 locale switch는 query뿐 아니라 양쪽 route에 존재하는 hash/location state도 보존한다. Translation unavailable fallback에는 존재하지 않는 detail hash를 전달하지 않는다.
- Site-owned internal href는 배포된 canonical pathname과 일치시켜 불필요한 redirect를 만들지 않는다. Collection과 page route의 trailing slash 정책을 navigation, CTA, footer와 hash URL에 동일하게 적용한다.
- Empty collection과 archive route는 화면의 empty state뿐 아니라 robots와 sitemap 노출도 content evidence와 함께 gate한다. 첫 공개 항목이 생기면 같은 규칙으로 자동 복귀해야 한다.
- Public page의 large visual은 two-second semantic test를 통과해야 하며, identity/portrait/evidence가 없을 때 큰 monogram이나 placeholder tile로 첫 viewport를 채우지 않는다.

## Research project pages

- 연구 구현 저장소의 기본 브랜치는 실제 구현 코드용으로 유지한다. Project website를 같은 저장소에 게시할 때는 전용 배포 브랜치를 사용하며, 별도 저장소가 필요한 이유가 없으면 웹사이트용 중간 저장소를 추가하지 않는다.
- 관련 분야의 여러 공식 project page를 실제로 열어 소개·방법·실험·영상의 순서를 비교하고, 채택·제외 판단을 대상 프로젝트에 기록한다. 한두 개 template의 외형만으로 해당 분야의 일반적인 구성이라 단정하지 않는다.
- 논문의 문제·기여·방법 설명에서 실험 근거로 이어지는 흐름을 먼저 설계한다. 지적된 block뿐 아니라 전체 읽기 순서를 원문과 대조하며, 상세 실험은 장비·작업·평가 조건을 성능 결과보다 앞에 둔다. Overview는 상세 결과보다 앞에 두고, 중요한 ablation과 정량 표는 기본 노출하며 각 그림·영상이 검증하는 주장을 가까운 본문으로 설명한다. 큰 그림·영상에서 찾아야 할 개념과 실험 조건은 해당 자료 앞에 짧게 정의한다. 성능·일반화·데이터 효율성의 결과를 모은 뒤 ablation과 내부 분석으로 넘어가고, 감독 신호를 만드는 외부 모델의 출력은 제안 모델이 학습한 결과와 구분해 Method에 배치한다.
- 별도의 짧은 요약 보기가 요청되면 상세 페이지를 보존하고 문제 → 핵심 방법 → 서로 다른 주장을 입증하는 소수의 대표 근거로 읽기 경로를 다시 구성한다. 기존 section을 모두 축소·복제하지 않으며 요약에서 상세 결과와 원문으로 이동할 수 있게 한다. 짧은 보기나 기본 진입 페이지에도 주요 비교표를 유지해 비교 방법·backbone·평가 조건을 함께 읽을 수 있게 하고, 유리한 개별 수치만 골라 주요 비교 근거를 대체하지 않는다. 두 보기는 검증된 metadata·수치와 원본 asset을 공유하고, 대표 결과의 backbone·평가 범위를 명시해 선택된 실험을 전체 성능 주장으로 확대하지 않는다. 반복되는 결과 요약은 같은 데이터와 표현을 공유하고 지표·집계 범위를 통일하며, 한 보기의 평균을 다른 보기에서 선택한 하위 실험으로 바꾸지 않는다. 특정 하위 실험만 측정한 ablation·plot은 그 범위를 명시하고 평균 결과로 재명명하지 않는다. Component를 추가·변경하면 두 보기 전체에서 같은 역할의 글자·아이콘·조작과 미디어 frame을 함께 시각 검수한다.
- 연구 소개 페이지에서 `Abstract`로 표시한 본문은 원고의 초록 문구를 그대로 보존하고, 별도의 짧은 설명은 `Overview`로 구분한다. 영상 중심의 짧은 페이지는 소개 영상을 앞에 두고 Method 본문을 간결하게 유지한다. 대표 데모는 desktop에서 한 행에 약 세 개를 함께 살펴볼 수 있는 gallery를 우선하되, 실제 동작·자막·control이 읽히는 크기로 정하고 좁은 화면에서는 열 수를 줄인다.
- 제공된 PPT나 편집 source가 있으면 합성된 완성 영상을 crop하기 전에 원본 embedded media와 animation을 확인해 우선 사용한다. 의미 있는 재생 속도·동기화·등장 순서를 보존하고, 정지 이미지나 별도 재구성으로 대체한 경우 원본 animation을 그대로 보존했다고 표현하지 않는다. 원본을 보존한 채 웹 배포용 영상을 압축하고 해상도·프레임 시각·음성·시각 품질을 비교한다. 재생 인덱스를 앞에 두어 순차 재생을 지원하고 숨겨진 데모는 미리 내려받지 않는다.
- Research project page는 문제·핵심 아이디어·개선된 행동을 먼저 전달한다. 방법·모듈·실험 조건의 과학 용어는 논문 원문과 대조하고, 설명을 꾸미기 위해 원문에 없는 개념명을 만들지 않는다. Method는 개념과 전체 흐름 중심으로 압축하고, 세부 학습 시각화는 검증하는 주장에 따라 실험·정성 분석에 배치한다. 수식 설명과 기호 사전을 늘려 첫 독자의 이해 부담을 키우지 않는다. 수식이 개념 이해에 직접 필요한 경우에만 입력·출력·연산 역할과 기호를 가까이 설명한다.
- 강조 수치와 요약은 논문의 핵심 기여를 입증하는 내용으로 고른다. 학습 비용·파라미터 증가 같은 overhead를 장점처럼 배치하지 않고, 해석에 필요한 실험 조건·비교 범위·출처는 해당 근거 옆에 짧게 남긴다. 저자 소속은 저자별로 확인하며 논문과 추가 실험의 집계 범위를 섞지 않는다.
- 연구 미디어는 원본 비율과 내용을 보존하면서 같은 역할의 표시 영역을 일관되게 구성한다. 작은 화면에 맞추려고 왜곡하거나 복합 그림 전체를 읽을 수 없게 축소하지 않는다. 의미 있는 원본 panel은 순서와 label을 보존해 재배치하고 원본 확대를 제공하며, 실제 휴대폰·태블릿 폭에서 figure 내부 글자와 본문의 읽기 흐름을 확인한다.
- 섹션명, 하위 방법 단계와 설명은 의미에 맞는 heading 계층으로 구분한다. 본문·표·그림·영상은 하나의 읽기 column 경계 안에 두고, 작은 근거 이미지를 column 폭까지 무조건 늘리지 않는다. 본문에 독립적인 폭 제한을 겹쳐 넓은 화면에서 한쪽만 비는 공간을 만들지 않는다. Caption은 자신이 설명하는 figure의 폭과 정렬을 따르고 배경·구분선·간격으로 본문과 구분한다. 장비·실험 환경을 식별하는 사진은 핵심 사양과 가까이 묶어 압축하고, 결과를 해석하는 데 필요한 세부 정보가 없으면 큰 결과 figure와 같은 비중으로 확대하지 않는다.
- 본문 양끝 정렬을 요청하면 대상 설명 문단에 일관되게 적용하되 마지막 줄은 시작점에 정렬한다. 언어에 맞는 자동 하이픈 처리를 사용하고 좁은 화면에서 단어 간격이 과도해지지 않는지 확인한다. 제목·캡션·표·탐색 UI까지 일괄 적용하지 않는다.
- 같은 실험의 비교 영상과 정량 표는 한 묶음으로 인접하게 배치한다. 평균 등 결과 요약은 관련 표·차트에 묶고, 영상 재생 control에 붙은 설명처럼 보이지 않도록 위치·간격·경계로 구분한다. 검증 목적이 겹치는 영상·그림은 통합하거나 task 탭으로 묶는다. 긴 페이지는 단순한 margin 축소보다 중복 목적과 분리된 근거 묶음을 먼저 줄이고, 같은 viewport의 전체 길이와 읽기 흐름을 전후 비교한다.
- 결과표는 열·행 간격과 단위 위치를 통일하며 반복되는 단위를 각 셀에 넣지 않는다. 열이 적은 표는 내용에 맞는 폭으로 읽기 column 안에서 가운데 배치해 label과 수치 사이가 과도하게 벌어지지 않게 한다. Ablation은 baseline에서 최종 방법으로 읽히게 정렬하고, 비교 방법의 학회·연도와 원 논문 링크를 확인해 제공한다. 학회·연도처럼 방법을 식별하는 보조 정보는 방법명 옆에 간결하게 두고, 그 정보 자체를 비교할 필요가 없으면 별도 열을 만들지 않는다. 페이지에서 이미 명확한 제안 방법의 학회 정보는 결과 행마다 반복하지 않는다.
- 표는 제목·측정 지표와 단위 → 수치 → 간결한 원문 출처의 위계로 읽히게 한다. 제목과 단위는 위쪽에서 역할을 구분하고, 아래에는 출처를 짧게 남긴다. `Source`·`Evaluation` 같은 반복 label이나 주변 설명에 있는 평가 조건을 footer에 다시 늘어놓지 않는다. 중복 label을 삭제해 달라는 요청에 다른 이름의 label이나 badge를 대신 추가하지 않는다. 해석에 필요한 조건은 근거 앞의 짧은 설명에 두고, 필요한 번호 각주는 출처와 간격·구분선으로 구별하며 좁은 화면에서도 읽을 수 있게 유지한다. 원문에서 재구성한 표는 그 사실과 검증된 표 번호를 밝히며, 원문 페이지를 확인했으면 해당 페이지로 연결한다. 여러 문서의 결과를 합쳤거나 추가 실험으로 일부 행을 교체했다면 각 출처의 적용 행·범위를 명시하고 전체가 한 원표에서 온 것처럼 표시하지 않는다.
- 영상 탭은 선택 전후 버튼·설명·표시 영역의 크기를 유지해 주변 내용이 이동하지 않게 한다. 원본의 고정 여백·테두리를 제거할 때는 전체 시간 범위에서 실제 내용을 자르지 않는지 확인하고 poster·재생·확대에 같은 표시 영역을 적용한다. 밝기 보정은 원본과 다양한 실제 프레임을 비교해 물체 경계와 밝은 영역의 구분을 검수하며, 명도를 낮추는 것과 과노출로 이미 소실된 디테일을 복원하는 것을 혼동하지 않는다.
- 비교 영상의 모델명·뷰 이름은 해당 영상 앞에 두어 재생 전에 대상을 식별할 수 있게 한다. 재생·시간 탐색·확대 조작은 일관되게 제공하며, 개별 재생을 기본으로 하고 함께 재생하는 control은 영상 묶음 바로 아래에 둔다. 식별 label, 재생 control, 결과 근거의 역할을 배치와 위계로 구별한다. 함께 재생할 때 개별 재생·탐색 control의 중복 노출을 피하고 개별 조작으로 돌아가는 경로를 제공한다. 모드를 바꿀 때 일시정지·현재 프레임·탐색 상태가 예측 가능하게 이어지도록 검증하며, 주변 제목과 같은 label을 반복하지 않는다. 재생·일시정지·다시 시작·확대는 익숙한 icon과 접근 가능한 이름·tooltip으로 압축하고, 이미 클릭 가능한 그림에 동일한 확대 text link를 덧붙이지 않는다.

## Identity color

- Existing website interaction palette가 검증되어 있으면 Gnaroshi identity를 보인다는 이유만으로 전체 palette를 교체하지 않는다. 사용자가 로고 기반 palette를 요청하면 실제 asset에서 색을 추출해 전경·배경 대비를 검증하고 역할별로 적용한다. 여러 로고 색은 활용 가능한 palette이며 section마다 다른 색을 배정하라는 의미가 아니다. 제목·목차·선택 상태·동일한 control은 section과 route가 달라도 공통 색 체계를 유지하고, section별 색 구분은 명시적으로 요청된 경우에만 적용한다. 사용자가 지정한 결과 강조색 등 의미가 분명한 보조색은 필요한 역할에 제한해 일관되게 사용한다. 논문 그림·차트의 의미 색은 brand 색으로 덮어쓰지 않는다.
- `identity-teal`과 `identity-orange`는 favicon, compact brand mark, ownership marker와 project evidence accent처럼 제한된 identity cue에 사용한다.
- Status, focus, heatmap, chart와 semantic interaction color는 identity palette와 분리한다.
- Website mascot mark는 approved raster base의 ears, eyes, face mass와 teal/orange contrast를 유지하고 16px/32px/64px에서 검증한다.

## Responsive acceptance

- shared breakpoint와 spacing token을 사용한다.
- 작은 viewport에서 navigation, button group, table, code block, form을 실제로 검증한다.
- component는 wrap/reflow하고, 본질적으로 넓은 content는 자체 scroll container를 가진다.
- 고정 width/min-width 때문에 parent를 넘지 않게 한다.
- focus, keyboard, contrast, heading order와 reduced motion을 검증한다.
- Local in-page navigation은 populated state에서도 active item이 좁은 viewport에서 발견 가능해야 한다. Scrollbar를 숨기면 edge fade, active auto-scroll, wrapping, disclosure 같은 다른 cue를 제공한다.
- Hash-link interaction은 static build에서도 click, Enter, direct URL load, back/forward, focus 이동, sticky offset과 exactly-one-current invariant를 검증한다. Sticky header나 local nav 아래 target이 가려지면 실패다.
- Route current item이 hash navigation 뒤 non-current가 될 수 있으면 operable element semantics도 함께 전환한다. `aria-current`만 제거한 inert label을 남기지 않는다.
- Screenshot 외에 실제 link 작동, browser history, hash focus와 locale 전환을 실행해 검증한다. Empty/populated feed, translated/untranslated pair, stale/fresh data와 hover/focus/current state를 대표 fixture로 분리한다.

## Security and release

- 작성 도구의 공개·공개 취소는 검토한 대상과 영향 범위를 한 번 승인한 뒤 검증·이력 저장·전송·배포·실제 반영 확인까지 이어지는 사용자 작업으로 구현한다. Save와 Publish는 분리하되, 이미 승인한 동일 범위의 내부 단계를 반복 확인으로 나누지 않는다. 실패한 단계와 보존된 원본·진행 기록을 표시하고, 재시도는 같은 승인 범위에서 이어가며 변경된 입력에는 새 검토를 요구한다.
- 공개 글 삭제는 원본 보관과 공개 사이트 제거를 구분한다. 다른 글·번역·첨부파일·링크에 미치는 영향을 미리 확인하고, 배포 성공뿐 아니라 대상 주소의 실제 제거까지 확인한 뒤 완료로 표시한다. CI 사용 제한은 hosting·domain·repository·인증 방식을 임의로 바꿀 권한이 아니다.
- 로컬 준비와 원격 게시의 의존성·권한·상태를 분리한다. 게시까지 승인된 웹 수정 작업은 로컬 검수 후 기존 게시 경로와 공개 반영 확인까지 이어간다. 로컬 미리보기·피드백 요청만으로 기존 게시 승인을 철회하거나 보류한 것으로 해석하지 않으며, 명시적인 로컬 전용·게시 보류 지시가 있으면 그 범위를 따른다. 작성·검증·이력 저장·사용자가 승인한 복구 가능한 원본 보관·정적 결과물 생성은 CI나 호스팅 인증을 요구하지 않는다. CI 중단·할당량 소진·오프라인이면 로컬 기능을 유지하고, 결과물과 정확한 입력 식별자를 보존해 나중에 같은 결과물로 게시를 재개한다. 의존성이 캐시에 없으면 필요한 설치만 설명하고 원격 CI로 몰래 전환하거나 검증을 생략하지 않는다.
- 로컬 실행과 CI 실행을 지원하면 Settings와 게시 흐름에서 선택할 수 있는 하나의 실행 방식으로 제공한다. CI를 쓸 수 없는 현재 환경에서는 검증된 local 방식을 기본으로 하고, 나중에 CI 방식으로 바꿀 수 있게 한다. 일반적인 게시 승인에 더해 내부 호스팅 처리를 위한 별도 허용 checkbox를 요구하지 않는다. 실행 방식 선택만으로 게시를 시작하거나 진행 중 작업의 방식을 바꾸지 않는다.
- CI 실패 시 같은 공개 대상·검증·입력을 유지하는 local 재시도를 실패 위치에 제공한다. 이미 실행 중이거나 접수 여부가 불명확한 원격 작업을 중복 배포하지 않도록 먼저 결과를 확인하며, 완료된 단계와 결과물을 재사용한다. 검증 실패를 CI 장애로 취급해 우회하거나 hosting·domain을 바꾸지 않는다.
- 로컬 빌드와 호스팅 제공자의 최종 게시 처리는 구분하되 실제 동작에 필요한 설명만 남긴다. 제공자 내부 절차가 있다는 이유만으로 fallback을 막거나, CI quota 부족을 확인되지 않은 호스팅 장애로 확대하지 않는다. 원격 전송·실제 반영이 실패하면 준비 결과를 보존하고 같은 방식의 재시도 또는 사용 가능한 대안을 제공하며, `로컬 준비 완료`를 `게시 완료` 또는 `공개 삭제 완료`로 표시하지 않는다.
- 상태 조회와 문제 해결 안내도 CI에 묶지 않는다. 기본 로컬 검사는 인증·workflow 조회 없이 끝나야 하며, 선택적 원격 정보가 없어도 로컬 변경·이력·검증 결과를 제공한다. 원격 검사는 사용자가 요청할 때 경계를 명시하고, 금지되거나 사용할 수 없는 CI 실행 명령을 유일한 복구 수단으로 안내하지 않는다.
- secret은 deployment secret store에만 둔다.
- CORS, validation, rate limit, error handling을 유지한다.
- build에는 content/schema/static check를 포함한다.
- deploy provenance와 rollback 경로를 남긴다.
- 사용자에게 보이는 metric은 실제 evidence가 있을 때만 노출한다.
