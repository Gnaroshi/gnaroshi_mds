# UI/UX preferences

## Desired experience

Simple means low cognitive load, not missing information. A first-time user must be able to answer these questions immediately:

1. 이 app/program은 무엇을 위한 것인가?
2. 지금 상태는 무엇인가?
3. 먼저 무엇을 준비해야 하는가?
4. 어떤 순서로 실행해야 하는가?
5. 다음 행동과 그 결과는 무엇인가?

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
- 반복되는 card/list action column은 label 길이마다 자체 폭을 계산하지 않는다. 같은 hierarchy의 button은 공통 control height, icon-label gap, vertical baseline과 column width를 공유하고, 긴 label은 정해진 wrap/compact policy로 처리한다. Card별 button 폭과 수직 위치가 제멋대로 달라지면 기능이 동작해도 PASS가 아니다.
- Connected Apps처럼 app별 기능이 다른 화면은 모든 card에 하나의 generic action만 복제하지 않는다. 공통 `Open`과 status grammar는 통일하되, provider가 실제 지원하는 2–3개의 가장 자주 쓰는 typed action을 같은 card에서 바로 발견할 수 있게 하고 나머지 technical evidence만 disclosure로 내린다.
- Task-generated feedback은 trigger, field 또는 affected item 가까이에 둔다. Page-wide 문제만 page feedback region에 두고, 별도 작업의 message를 한 global banner에 섞지 않는다.
- Inline feedback과 page feedback region은 기존 content를 덮거나 가리지 않는다. Conditional message가 중요한 editor, list, form 또는 control을 밀어내는 경우 reserved region, replacement state 또는 명시적 transition layout을 사용한다.
- Modal alert는 data loss, irreversible action, credential/security 경계처럼 즉시 결정을 요구할 때만 사용한다. 일반 success, retry 가능한 fetch failure와 상태 정보는 current context 안에서 전달한다.
- Success가 결과 자체로 명확하면 불필요한 message를 추가하지 않는다. 결과가 offscreen이거나 canonical write, copy, import, external launch처럼 확인이 필요하면 짧고 persistent한 context feedback을 제공한다.
- Error는 무엇이 실패했는지, 보존된 것은 무엇인지, 다음 valid action을 함께 말한다. 자동 dismiss toast를 error 또는 유일한 recovery 안내로 사용하지 않는다.
- Action이 새 view, item 또는 dialog를 열면 focus와 selection을 새 context로 이동하고 돌아갈 위치를 보존한다. Screen reader에는 live region을 사용하되 같은 message를 여러 `role=alert`로 중복 발표하지 않는다.
- Async action 중 관련 input, selection과 navigation이 결과와 충돌할 수 있으면 operation scope만 잠근다. App 전체를 이유 없이 막지 않고, stale response가 새 selection을 덮지 않도록 request identity/cancellation을 적용한다.
- `Continue`, `Resume`, `Retry`처럼 이전 상태를 이어가는 동사는 대상과 복원 지점을 증명할 수 있을 때만 사용한다. 사용자가 무엇을 이어가는지 알 수 있도록 document/item, 단계 또는 pass, 마지막 상태와 필요하면 elapsed time을 같은 맥락에 표시한다. 단순히 과거 기록이 있다는 이유로 `Continue`라고 부르지 않는다.
- 변경 감지는 별도 boolean을 독립적으로 관리하기보다 현재 draft와 canonical saved value의 비교에서 파생한다. 사용자가 편집을 정확히 되돌리면 dirty indicator, Save action과 Recovery snapshot도 원래 상태로 돌아가야 한다.
- Same-page/hash navigation은 click, keyboard activation, direct hash load, browser back/forward와 scroll/focus offset을 모두 같은 acceptance contract로 검증한다. Sticky header나 local nav 아래에 target이 가려지면 실패로 본다.
- State-transition test는 각 상태를 따로 확인하는 데서 끝내지 않는다. "A가 current일 때 B는 current가 아니다", "current item은 한 개다", "stale async result가 새 selection을 덮지 않는다" 같은 negative invariant를 포함한다.
- Minimal interface를 정지 화면으로 해석하지 않는다. Owner가 contemporary interaction을 요구하면 navigation destination, reading/task progress, current/pressed/open state처럼 사용자가 이해할 수 있는 변화에 native progressive motion을 연결한다. 자동 loop, custom cursor, decorative parallax와 motion-only feedback은 사용하지 않고 reduced-motion에서는 같은 상태를 즉시 전달한다.
- Motion acceptance는 animation 선언 유무가 아니라 정상 속도에서 변화가 인지되는지로 판단한다. 시작·중간·종료 frame 또는 실제 계산값을 비교하고, text contrast와 layout geometry는 모든 frame에서 유지하며, reduced-motion에서는 동일한 정보와 action state를 즉시 제공한다.
- Experimental interaction API는 normal navigation, reload, locale switch, focus 또는 requestAnimationFrame lifecycle을 불안정하게 만들면 해당 경로에서 opt out하거나 안정된 fallback으로 되돌린다. 최신 기술 사용 자체를 acceptance criterion보다 우선하지 않는다.
- Hidden accessibility instruction은 실제 interaction contract와 일치해야 하고 layout utility가 정의되지 않아 visible text로 새지 않도록 component test와 packaged runtime에서 확인한다. Keyboard 도움말이 routine task에 필요하지 않으면 toolbar의 Help/Guide처럼 요청 가능한 위치로 이동한다.

## Information hierarchy and density

- Navigation group과 screen heading은 implementation layer가 아니라 사용자 목표와 결과를 이름으로 사용한다. 한 item만 가진 group, 모호한 container label과 raw technical noun은 grouping 이득이 없으면 합치거나 이름을 바꾼다.
- Current location, primary task와 next action은 secondary status, repository path, hash, schema/version detail보다 먼저 보여준다. Raw provenance와 diagnostic value는 사용자가 요청할 때 disclosure, Details 또는 inspector에서 보여준다.
- Empty state의 primary action은 사용자가 방금 막힌 workflow의 다음 유효 단계로 이어져야 한다. 일반 adjacent page, broad research page, marketing page로 보내는 CTA는 그곳이 실제 다음 행동일 때만 primary로 둔다.
- `Now`, `Current`, `Recent`, freshness, health처럼 시간성을 주장하는 surface는 공통 freshness policy를 공유한다. 같은 data가 한 화면에서는 stale로 숨겨지고 다른 화면에서는 current로 보이면 안 되며, stale이면 last updated, 영향, 다음 확인 경로를 표시한다.
- 한 card에서 같은 target을 가리키는 image, title, text CTA가 반복되면 tab stop을 최소화한다. 전체 card click handler 대신 필요한 실제 anchor만 남기고 evidence caption은 숨기지 않는다.
- 긴 상세 페이지는 local navigation을 추가하기 전에 중복 section과 반복 copy를 먼저 줄인다. 줄인 뒤에도 긴 경우 stable heading ID와 permalink, keyboard-accessible local navigation을 제공한다.
- Spacing은 먼저 관계를 표현한다. 가까운 요소는 같은 task group, 더 큰 간격은 section boundary를 뜻한다. Divider는 scrolling region, navigation group 또는 의미가 다른 dense row처럼 공간만으로 경계가 불충분할 때 일관되게 사용한다.
- 같은 경계를 sticky/local navigation의 surface와 바로 뒤 full-width divider로 반복하지 않는다. Sequence connector는 실제 numbered step 사이를 이어 인과나 순서를 설명해야 하며, 내용 아래에 독립적으로 남는 선은 제거하거나 의미가 드러나는 grouping으로 바꾼다.
- Font size는 hierarchy를 만들기 위한 유일한 수단이 아니다. Visible non-decorative caption/help는 기본 12px 이상, navigation/form/control은 보통 13–14px 이상, 긴 authoring text는 보통 15–17px에서 실제 EN/KO 가독성을 검증한다. 더 작은 text가 필요하면 정보 자체를 숨기거나 재구성할 수 없는지 먼저 검토한다.
- Typography, spacing, radius, divider와 control height는 semantic token으로 제한한다. Component마다 임의 값으로 밀도를 미세 조정하지 않는다.
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

- Broad UI change는 screen 전체에 대한 vague approval 한 번으로 끝내지 않는다. Navigation, form, editor toolbar, dialog, list row, status/feedback, destructive action처럼 변경 component를 나눠 review한다.
- 각 component review는 purpose, expected action/result, idle/pending/success/error, keyboard/focus, narrow window, dark/light, content length, layout stability와 regression을 pass/fail로 기록한다.
- Reviewer가 `OK`를 주려면 blocker가 없다는 말뿐 아니라 acceptance criterion별 증거를 남겨야 한다. Fail 또는 ambiguous item은 같은 component를 수정하고 다시 review한다.
- Component들이 통과한 뒤 전체 workflow에서 hierarchy, state continuity와 cross-component feedback을 다시 검증한다. Component pass가 전체 product flow pass를 대신하지 않는다.
- Desktop UI 검토는 source render, test fixture 또는 showcase만으로 완료하지 않는다. 실제 signed stable install에서 real representative record를 선택하고 navigation, edit/revert, mode change, pending/result/error, destructive entry point와 minimum window를 직접 실행해 source와 설치본의 일치를 확인한다.
- Visual screenshot pass는 interaction pass가 아니다. Hover/click/focus/current state, translated-unavailable state, populated/empty fixtures, route-hash transitions와 stale/fresh cases를 별도 runtime test로 실행한다.
- Visual screenshot이 정상이더라도 link operability, browser history, hash focus와 locale transition을 검증하지 않았다면 완료로 보지 않는다.

## Avoid

- 없어도 의미가 같은 text, 반복 안내, marketing filler, 장황한 설명
- 장식만을 위한 card, badge, gradient, animation, icon
- 승인된 identity나 실제 evidence를 대신하는 큰 initial/monogram/placeholder tile
- 서로 전혀 맞지 않는 padding/margin과 임의 spacing 값
- card 안의 card, 불필요한 border와 shadow
- 작은 viewport에서 잘리는 text, button, form, table, navigation
- hover-only 정보, color-only status, 이유 없는 disabled control
- 반응형이라는 이유로 중요한 기능이나 정보를 숨기는 것

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
- 긴 번역, Dynamic Type 또는 browser zoom, 실제 content 길이를 사용한다.
- wrap과 reflow가 우선이며 data table/code처럼 필요한 경우에만 명시적 scroll을 사용한다.
- screenshot 또는 실제 runtime으로 clipping, overlap, overflow를 확인한다.
- 순서가 중요한 flow diagram은 intermediate breakpoint에서도 읽는 순서와 causality가 유지되어야 한다. Connector를 숨긴 fallback을 2-column grid로 바꿀 때는 numbering, row order와 visual grouping이 단계 순서를 흐리지 않는지 검증한다.

## Resizable workspace surfaces

- Sidebar/content, master/detail, editor/inspector와 editor/preview처럼 사용자가 작업 폭을 선택해야 하는 경계는 재사용 가능한 resizable pane primitive를 사용한다. 화면별 absolute width와 ad-hoc pointer handler를 반복하지 않는다.
- Divider는 focus 가능한 `separator` widget으로 구현하고 orientation, current/min/max value와 대상 pane을 accessible name으로 제공한다. Pointer뿐 아니라 Arrow key, 큰 step, min/max 이동과 collapse/expand를 keyboard로 제공한다.
- Drag 시작 시 pointer capture와 text-selection 방지를 사용하고 종료/cancel/lost capture에서 모두 정리한다. Divider를 끌다가 문서 text가 선택되거나 resize cursor가 app 전체에 남지 않게 한다.
- 합리적인 pane별 minimum, maximum과 primary content minimum을 동시에 적용한다. Persisted size가 현재 usable viewport를 벗어나면 안전하게 clamp하되 사용자의 저장값을 불필요하게 잃지 않는다.
- Double-click reset, explicit collapse/expand와 local persistence를 제공한다. Collapsed pane은 시각적으로만 0px이 아니라 focus와 accessibility tree에서도 제외하고, expand control은 계속 접근 가능해야 한다.
- Narrow window의 Split은 preview를 화면 밖으로 밀지 않는다. Side-by-side에서 stacked로 전환하거나 명시적 방향 선택을 제공하고 현재 정책을 짧게 표시한다. 두 pane은 독립 scroll을 유지한다.
- Route, document, mode와 focus 전환은 mounted editor identity, cursor, selection, undo history, scroll과 유효 pane state를 보존한다. Focus mode가 주변 pane을 숨겨도 canonical save/error boundary를 unmount하지 않는다.
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
- Backup, cache와 Recovery처럼 운영 성격이 다른 설정은 한 card 안에 합치지 않는다. Recovery의 destructive action은 routine restore와 시각적으로 분리하고 exact item을 이름으로 표시한다.

## Authoring and history controls

- Editor toolbar는 content mode, primary formatting, secondary insertion과 workspace utility를 구분한다. 좁은 폭에서는 낮은 빈도의 formatting을 한 개의 labelled `More` disclosure로 reflow하고 서로 배타적인 Guide/Outline popover는 한 번에 하나만 연다.
- Popover, disclosure와 dialog의 semantic role은 실제 keyboard behavior와 일치해야 한다. Menu key handling을 구현하지 않은 일반 action list를 `menu/menuitem`으로 가장하지 않는다. Escape는 닫고 trigger로 focus를 돌리며 outside click과 mode change도 stale overlay를 남기지 않는다.
- Focus mode는 주변 chrome을 줄여도 document identity, edit/preview mode, saved/unsaved state, Save action, blocking error와 exit action을 유지한다. 집중 모드가 저장 경계나 실패를 숨겨서는 안 된다.
- History correction/delete는 row에서 발견 가능해야 하고 exact target과 영향 범위를 확인한다. Immutable audit source를 보존해야 하는 domain이면 correction event와 recoverable journal을 사용하고, interrupted write는 다음 read/list 전에 안전하게 resume하거나 conflict로 fail closed한다.

## Reference basis

이 문서는 특정 design system의 visual appearance를 복제하지 않고 다음 공식 guidance에서 반복되는 interaction 원칙을 재사용한다.

- [Apple Human Interface Guidelines: Feedback](https://developer.apple.com/design/human-interface-guidelines/feedback), [Alerts](https://developer.apple.com/design/human-interface-guidelines/alerts), [Progress indicators](https://developer.apple.com/design/human-interface-guidelines/progress-indicators), [Buttons](https://developer.apple.com/design/human-interface-guidelines/buttons)
- [Carbon Design System: Notifications](https://carbondesignsystem.com/patterns/notification-pattern/), [Spacing](https://carbondesignsystem.com/elements/spacing/overview/)
- [Primer: Forms](https://primer.style/product/ui-patterns/forms/), [Navigation](https://primer.style/product/ui-patterns/navigation/), [Notification messaging](https://primer.style/product/ui-patterns/notification-messaging/)
- [GitHub Docs writing best practices](https://docs.github.com/en/contributing/writing-for-github-docs/best-practices-for-github-docs)와 [basic Markdown writing](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
- [Zotero: Adding items and metadata by identifier](https://www.zotero.org/support/adding_items_to_zotero)
- [WAI-ARIA APG Window Splitter Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/windowsplitter/)과 [Tabs Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/tabs/)
- [WCAG 2.2 Error Identification](https://www.w3.org/WAI/WCAG22/Understanding/error-identification.html)과 [Status Messages](https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html)
