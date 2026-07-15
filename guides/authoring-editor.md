# Authoring editor guidance

## Writing surface

- Long-form editor는 title/metadata form과 경쟁하지 않는 충분한 width를 갖고 cursor, selection, undo history와 scroll position을 mode 전환 중 보존한다.
- Markdown source는 canonical text이고 preview는 derived view다. Preview failure가 source editing 또는 recovery를 막지 않는다.
- Formatting action은 cursor/selection에 예측 가능한 Markdown을 삽입하고 focus를 editor로 돌려준다. Inline math와 display math를 서로 다른 action으로 제공한다.
- LaTeX는 `$…$` inline과 `$$\n…\n$$` display form을 지원하고 malformed formula는 source를 보존한 채 해당 formula 가까이에 설명한다.
- Formula validation은 raw dollar-sign regex가 아니라 실제 Markdown math syntax tree의 inline/display math node만 검사한다. Inline code, fenced code, escaped dollar와 일반 가격 표기를 수식 오류로 오인하지 않는다.
- Editor document identity가 바뀌면 본문이 우연히 같아도 undo/redo history를 새 document에 전달하지 않는다. External hydration은 undo history에 넣지 않고 document별 editor lifetime 또는 compartment를 명시적으로 분리한다.

## Screenshots and images

- Image import는 native user selection, clipboard 또는 explicit drop처럼 user activation이 있는 경로에서만 시작한다. Broad filesystem permission이나 repository-wide external asset scan을 요구하지 않는다.
- Canonical repository 안의 bounded asset directory로 copy하고 absolute local path를 Markdown, preview, log 또는 public content에 쓰지 않는다.
- File extension만 믿지 않고 magic bytes, decoded dimensions와 size limit을 검증한다. 초기 지원 format은 PNG, JPEG와 WebP처럼 정적 raster allowlist를 우선한다.
- Filename은 sanitized name과 content hash를 사용하고 duplicate import는 idempotent하게 처리한다. Symlink와 canonical containment를 검증한다.
- Insert action은 Markdown image destination과 편집 가능한 alt-text placeholder를 만들고 alt text selection으로 focus를 이동한다.
- Async picker/paste/drop은 시작 document identity, revision text, selection과 focus policy를 함께 보존한다. 같은 본문을 가진 다른 document로 전환되었거나 원문이 변했으면 link insertion을 거부하고 saved asset과 recovery action을 설명한다.
- Paste/drop 동안 사용자가 다른 control로 이동했으면 focus를 탈취하지 않는다. Modal picker를 명시적으로 완료한 경우에는 alt-text selection으로 editor focus를 돌려준다.
- File read 이전부터 synchronous in-flight guard를 잡아 빠른 paste/drop이 React state update보다 먼저 중복 실행되지 않게 한다.
- Local preview는 exact imported asset reference만 bounded read한다. Remote image를 authoring preview에서 자동 fetch하지 않는다.
- Preview loading/success/decode-error state는 exact asset identity에 묶어 document 전환 중 이전 image가 새 alt text와 함께 보이지 않게 한다. Frame geometry와 feedback region은 pending/result/error 사이에 고정하고 긴 message는 bounded scroll/disclosure로 읽을 수 있게 한다.
- Private asset, publication-approved asset과 missing asset을 구분한다. Public projection은 declared public asset만 copy/rewrite하고 undeclared, private 또는 missing reference를 fail closed한다.
- Paper note screenshot과 private research attachment는 publication asset이 아니다. 별도 owner action 없이는 feed나 website로 복사하지 않는다.

## Validation

- Image picker cancel, unsupported type, spoofed extension, oversized file/pixel dimensions, symlink escape, duplicate content와 missing preview
- Cursor insertion, alt-text selection, same-text document 전환 undo isolation, inline/display math, malformed math, code/fence false-positive 제외와 source/preview mode preservation
- Private asset이 publish staging과 public output에 포함되지 않는 privacy test
- Minimum window, dark/light theme, keyboard-only flow와 layout-stable pending/success/error feedback
