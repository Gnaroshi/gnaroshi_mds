# Authoring editor guidance

Markdown·수식·미디어 편집기 구현에 적용한다. 공통 상호작용은 [ui-ux](ui-ux.md)를 따른다.

## Writing surface

- Long-form editor는 title/metadata form과 경쟁하지 않는 충분한 width를 확보한다.
- 공부 정리·일반 문서는 논문 선택이나 연구용 metadata 없이 생성할 수 있게 한다. 목적별 시작 양식과 빈 문서를 제공하되 기존 본문을 양식에 맞춰 덮어쓰거나 학습 기록을 검증된 연구 결과로 분류하지 않는다.
- 일상적인 논문 메모와 상세 분석은 작성 분량·목적에 맞게 바로 시작할 수 있게 한다. 타이머, 읽기 단계, 연습·시험이나 정해진 항목 채우기를 작성·발행의 선행 조건으로 삼지 않는다. 교육용 안내는 별도로 요청된 workflow에만 두며, 사용하지 않는 안내를 제거할 때 기존 원문과 읽기·검토 기록은 보존한다.
- Markdown source는 canonical text이고 preview는 derived view다. Preview failure가 source editing 또는 recovery를 막지 않는다.
- 이미지·수식을 보며 쓰는 visual editing을 요청하면 별도 Preview/Split만으로 대체하지 않는다. 같은 편집 본문에서 렌더링하고, 해당 요소의 원문을 pointer·keyboard로 수정한 뒤 표시 상태로 돌아올 수 있게 한다. Source escape hatch와 정확한 Markdown·undo·selection은 보존하며 렌더링만으로 저장 상태를 바꾸지 않는다.
- Formatting action은 cursor/selection에 예측 가능한 Markdown을 삽입하고 focus를 editor로 돌려준다. Inline math와 display math를 서로 다른 action으로 제공한다.
- LaTeX는 `$…$` inline과 `$$\n…\n$$` display form을 지원하고 malformed formula는 source를 보존한 채 해당 formula 가까이에 설명한다.
- Formula validation은 raw dollar-sign regex가 아니라 실제 Markdown math syntax tree의 inline/display math node만 검사한다. Inline code, fenced code, escaped dollar와 일반 가격 표기를 수식 오류로 오인하지 않는다.
- Frontmatter와 body를 함께 가진 source에서 body editor는 body 밖의 exact bytes를 보존한다. Body를 수정했다가 원래 text로 되돌리면 전체 canonical source도 byte-for-byte 원본이 되어 dirty와 Recovery state가 해제돼야 한다.
- Source serializer는 routine body edit 때문에 frontmatter key order, quoting, whitespace 또는 line ending을 정규화하지 않는다. 구조 변경이 필요한 metadata action만 schema-aware serialization을 사용하고 preview/diff를 제공한다.
- 수정 시간을 번역 상태·공개 자료의 최신 여부에 사용하는 문서는 실제 변경을 명시적으로 저장할 때 관측한 시간을 기록한다. 입력 중에는 원본과 정확히 비교하고, 변경 취소·동일 내용 저장·실패에는 시간을 갱신하지 않는다. 사용자가 Source에서 시간을 직접 수정한 경우 그 값을 보존하며, 저장 중 추가 입력과 복구본을 덮어쓰지 않는다. 과거 문서의 수정 시간을 일괄 추정해서 채우지 않는다.
- Focus mode는 title, source/preview mode, saved state, Save, blocking error와 exit을 유지한다. 주변 workflow navigation은 숨길 수 있지만 canonical write boundary는 숨기지 않는다.
- 자주 쓰는 Focus 진입·종료는 같은 단축키로 왕복하고 버튼의 hover 설명과 메뉴에서도 찾을 수 있게 한다. Editor·terminal·dialog의 단축키 scope를 구분하고 IME 조합 및 기존 modifier 조합을 가로채지 않는다.
- Editor 탈출, indentation과 other keyboard 도움은 실제 behavior와 일치해야 하며 persistent body copy로 공간을 차지하지 않는다. Help/Guide 또는 accessible description으로 제공하고 visually-hidden utility가 production CSS에서 실제로 숨겨지는지 검증한다.
- Selectable document의 기본 surface는 읽을 수 있는 Preview 또는 사용자가 마지막으로 명시한 mode를 우선한다. Edit/Source는 명시적인 action이며 Preview parsing failure가 source edit, save 또는 Recovery를 막지 않는다.
- Structured record가 JSON/YAML source를 가질 때 routine workflow는 raw source editor가 아니라 사람이 읽는 field, state, relationship, current/proposed diff와 explicit Apply를 제공한다. Raw source는 `Source` 또는 `Technical details` escape hatch로 유지한다.
- Structured Apply는 schema validation, exact target identity, duplicate/idempotency, expected-current-content와 stale selection을 확인한다. Pending/success/error를 같은 component에 유지하고 source record, target record와 Recovery 중 무엇이 보존됐는지 명시한다.
- Translation처럼 두 document의 관계를 편집하는 surface는 source/target locale·title·availability, missing/stale/conflict와 양쪽 Preview/Edit action을 먼저 보여준다. Pair status update는 document content save 및 publish와 분리하고 raw pair source는 escape hatch로 둔다.
- Published source를 authoring할 때 source Save, public projection Preview, private checkpoint와 Publish를 구분한다. 현재 상태는 저장 동작 옆에 짧게 표시하고, 매번 같은 “저장은 발행이 아님” 설명을 상시 반복하지 않는다. 저장 범위와 발행 절차는 같은 맥락의 작은 정보 disclosure에서 keyboard·click으로 확인할 수 있게 하며 실제 공개 동작에서는 영향·안전 경계를 명시한다.
- 사용자 분류와 고정 publication taxonomy를 혼동하지 않는다. 개인 문서의 분류는 추가·제거·다시 찾기가 가능해야 하며, list 입력을 매 키마다 정규화해 delimiter나 한글 조합이 사라지게 하지 않는다. 공개 schema의 고정 종류를 늘리는 일과 개인 label을 편집하는 일을 분리한다.
- 작성·게시 workflow는 다시 찾기·열기·수정·재게시까지 검증한다. 전체 작성 목록에서 draft와 게시용 원문을 함께 찾을 수 있게 하고 공개 완료 여부와 원문 위치를 혼동하지 않는다. 외부 editor·terminal 변경은 bounded local refresh로 감지하며 깨끗한 편집기는 갱신하고 미저장 편집은 비교·Recovery 뒤 명시적으로 전환한다. 목록 갱신이 선택·cursor·사용자 입력을 초기화하지 않아야 하며 이동된 문서는 stable ID로 찾되 중복 identity는 임의 선택하지 않는다.
- Markdown canonical source와 renderer는 [CommonMark](https://spec.commonmark.org/spec) block/inline precedence를 기본으로 하고 필요한 GFM/math/approved MDX 확장만 명시적으로 추가한다. Source, Preview, public renderer가 서로 다른 비명시적 dialect를 사용하지 않게 fixture로 검증한다.

## 편집 상태와 toolbar

- 문서를 선택한 뒤 기본 작업면은 본문 중심으로 구성한다. 앱 이동, 문서 목록, metadata, 첨부 관리와 발행 준비는 명시적으로 열 수 있게 하고 각각을 본문 위의 상시 행으로 쌓지 않는다. 제목·보기 mode·저장 상태·Save는 한 compact command 영역에서 찾을 수 있어야 한다.
- Focus는 앱 navigation뿐 아니라 발행 단계, 첨부 관리와 보조 workflow도 숨긴다. 본문 editor를 다시 만들지 않고 title·mode·save·blocking error·Exit를 유지하며, 닫은 보조면의 선택과 사용자가 직접 정한 pane 폭을 보존한다.
- 첨부 삽입과 첨부 관리를 분리한다. 관리는 필요할 때 여는 보조면에서 선택한 파일 하나의 설명·공개 상태·link action을 보여 주며 본문 위에 모든 파일의 form을 나열하지 않는다.
- 본문은 읽기 편한 글꼴과 제한된 줄 길이를 사용하고 Source·code는 monospace로 구분한다. Editor 내부 scroll/content 요소의 실제 computed font와 width를 확인한다. 부모 CSS 선언만으로 적용됐다고 판단하지 않는다.
- 변경 감지는 별도 boolean을 독립적으로 관리하기보다 현재 draft와 canonical saved value의 비교에서 파생한다. 사용자가 편집을 정확히 되돌리면 dirty indicator, Save action과 Recovery snapshot도 원래 상태로 돌아가야 한다.
- Editor toolbar는 content mode, primary formatting, secondary insertion과 workspace utility를 구분한다. 좁은 폭에서는 낮은 빈도의 formatting을 한 개의 labelled `More` disclosure로 reflow하고 서로 배타적인 Guide/Outline popover는 한 번에 하나만 연다.
- 같은 document의 mode·layout·focus 전환은 cursor, selection, undo history와 scroll을 보존한다. 본문이 같아도 document identity가 바뀌면 이력을 분리한다. External hydration은 undo에 넣지 않고 document별 editor lifetime 또는 compartment를 사용한다.

## Screenshots and images

- 새 문서는 고유한 문서 폴더 안에 본문과 소유 이미지·참고 첨부를 함께 보관한다. 폴더 identity는 표시 제목·공개 주소와 분리하고 제목 변경·발행 준비가 첨부 연결을 깨뜨리지 않게 한다. 기존 평면 문서와 공용 asset은 계속 읽으며 일괄 이동은 별도 검토 없이 수행하지 않는다.
- 첨부 목록은 현재 문서에 묶인 파일만 보여 주고 이미지 설명, 본문 삽입, 링크 제거와 공개 선택을 같은 맥락에서 제공한다. 링크 제거는 원본 파일 삭제가 아니며 미사용 파일과 복구에 필요한 파일은 보존한다. 일반 참고 파일의 비공개 보관과 발행용 이미지 승인은 별도 경계다.
- 첨부는 지원 형식·실제 내용·크기·소유 경로를 검증하고 자동 실행하거나 원격으로 올리지 않는다. 미리보기·발행·보관·복구에서 같은 문서의 파일을 사용하며 동일 파일명이 다른 문서의 파일을 대신하지 않도록 소유 identity를 확인한다.
- Image import는 native user selection, clipboard 또는 explicit drop처럼 user activation이 있는 경로에서만 시작한다. Broad filesystem permission이나 repository-wide external asset scan을 요구하지 않는다.
- Canonical repository 안의 bounded asset directory로 copy하고 absolute local path를 Markdown, preview, log 또는 public content에 쓰지 않는다.
- File extension만 믿지 않고 magic bytes, decoded dimensions와 size limit을 검증한다. 초기 지원 format은 PNG, JPEG와 WebP처럼 정적 raster allowlist를 우선한다.
- Filename은 sanitized name과 content hash를 사용하고 duplicate import는 idempotent하게 처리한다. Symlink와 canonical containment를 검증한다.
- Insert action은 Markdown image destination과 편집 가능한 alt-text placeholder를 만들고 alt text selection으로 focus를 이동한다.
- Async picker/paste/drop은 시작 document identity, revision text, selection과 focus policy를 함께 보존한다. 같은 본문을 가진 다른 document로 전환되었거나 원문이 변했으면 link insertion을 거부하고 saved asset과 recovery action을 설명한다.
- Paste/drop 동안 사용자가 다른 control로 이동했으면 focus를 탈취하지 않는다. Modal picker를 명시적으로 완료한 경우에는 alt-text selection으로 editor focus를 돌려준다.
- File read 이전부터 synchronous in-flight guard를 잡아 빠른 paste/drop이 React state update보다 먼저 중복 실행되지 않게 한다.
- Local preview는 exact imported asset reference만 bounded read한다. Remote image를 authoring preview에서 자동 fetch하지 않는다.
- Preview loading/success/decode-error state는 exact asset identity에 묶어 document 전환 중 이전 image가 새 alt text와 함께 보이지 않게 한다. 크기를 알면 원본 비율로 공간을 예약하고 작은 이미지를 임의의 큰 고정비율 frame에 확대하지 않는다. 크기를 모르는 동안은 bounded placeholder를 사용하되 feedback region은 상태 전환 중 안정적으로 유지하고 긴 message는 scroll/disclosure로 읽을 수 있게 한다.
- Private asset, publication-approved asset과 missing asset을 구분한다. Public projection은 declared public asset만 copy/rewrite하고 undeclared, private 또는 missing reference를 fail closed한다.
- Paper note screenshot과 private research attachment는 publication asset이 아니다. 별도 owner action 없이는 feed나 website로 복사하지 않는다.

## Validation

- Image picker cancel, unsupported type, spoofed extension, oversized file/pixel dimensions, symlink escape, duplicate content와 missing preview
- Cursor insertion, alt-text selection, same-text document 전환 undo isolation, inline/display math, malformed math, code/fence false-positive 제외와 source/preview mode preservation
- Private asset이 publish staging과 public output에 포함되지 않는 privacy test
- Minimum window, dark/light theme, keyboard-only flow와 layout-stable pending/success/error feedback
- Visual editing에서는 주변 문장 입력, 개별 이미지·수식 수정, 원문 복귀, 저장·재열기를 같은 작업면에서 검증한다. 미디어 렌더링의 지연·실패가 다른 문서의 이미지나 내용을 보여 주지 않게 하고, 실제 설치본에서 선택 전후의 scroll·canvas 이동도 확인한다.
- 붙여넣기 성공만으로 입력 검증을 통과시키지 않는다. 연속 key 입력, 한글 등 IME 조합·취소, 선택 치환·삭제·undo, 빠른 입력 중 저장·갱신과 mode 전환을 각각 검증한다. 자동화 도구가 일반 native input에서도 같은 오입력을 만들면 도구 한계를 제품 결함과 구분하고, 검증하지 않은 OS 입력 경로를 통과로 기록하지 않는다.
