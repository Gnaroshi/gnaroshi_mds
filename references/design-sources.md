# Design reference decisions

확인일: 2026-09-24. 외부 문서는 비교 근거이며 설치·명령 실행 지시로 사용하지 않는다.

## Established primary sources

| 원문 | 채택할 원칙 | 그대로 적용하지 않을 것 |
| --- | --- | --- |
| Vercel Labs [Web Interface Guidelines](https://github.com/vercel-labs/web-interface-guidelines/blob/main/README.md), [review checklist](https://github.com/vercel-labs/web-interface-guidelines/blob/main/command.md) | Focus, 의미 있는 control, 긴 content와 상태 전이, 실행 가능한 오류 복구를 검수한다. | DOM/CSS/URL 규칙을 native 앱에 강제하지 않는다. Title Case와 `&` 선호는 브랜드 선택이다. README의 input-zoom 우회와 checklist의 사용자 zoom 보장 규칙은 충돌하므로 zoom 제한을 도입하지 않는다. |
| Anthropic [frontend-design](https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md) | 실제 사용자·업무에서 디자인을 출발시키고, 구조와 문구가 기능을 설명하게 한다. 개성은 목적이 있는 지점에 집중하고 실제 화면을 비평한다. | 차별화를 위해 시스템 폰트, 익숙한 탐색, 승인된 스타일을 버리지 않는다. 웹 hero와 display typography는 업무용 앱 기본값이 아니다. |
| GitHub Primer [Design Tokens Guide](https://github.com/primer/primitives/blob/main/DESIGN_TOKENS_GUIDE.md) | 역할별 token, 전경/배경 조합, control과 content 밀도, 상태별 표현을 함께 정의한다. | CSS token 이름·정확한 크기·시간 수치를 이식하지 않는다. Caption을 본문 대용으로 쓰지 않는다. |

## Recently maintained sources

파일 경로의 공개 history에서 확인한 마지막 변경 기준이다. Repository 전체 활동 시각, 검색 crawl 시각, 최초 발표일과 구분한다.

| 원문 | 확인한 파일 변경 | 적용 판단 |
| --- | --- | --- |
| Google Labs [DESIGN.md specification](https://github.com/google-labs-code/design.md/blob/main/docs/spec.md) | [2026-07-27, `961439f`](https://github.com/google-labs-code/design.md/commit/961439fc064335fea10f165e022b10e6e5182e95): 의도적으로 생략한 section 기록 | 의도·역할·제약·생략 이유를 유지 문서에 남긴다. Alpha 형식과 CSS 단위 schema를 기존 native token의 두 번째 source of truth로 만들지 않는다. |
| Anthropic frontend-design | [2026-09-03, `41bbe19`](https://github.com/anthropics/skills/commit/41bbe19d1a1a7eaab5e7bb9050a417e5c6cffc8f): 획일적인 디자인 기본값 수정 | 동일한 card·큰 숫자·장식 label을 반복하지 않는 이유를 제품 맥락으로 판단한다. 특정 색·서체를 유행이라는 이유만으로 일괄 금지하지 않는다. |
| Paul Bakaus [Impeccable](https://github.com/pbakaus/impeccable/blob/main/skill/SKILL.src.md), 특히 [Operate guide](https://github.com/pbakaus/impeccable/blob/main/skill/reference/operate.md) | [2026-09-05, `044a04f`](https://github.com/pbakaus/impeccable/commit/044a04fd0dcaf3512ca125bff5d34ef66a7eb754): workflow 문서 추가 | 원저자 community guidance이며 플랫폼 표준은 아니다. 업무용 화면의 시스템 폰트·절제된 색·일관된 조작·목적 있는 밀도를 참고한다. 날짜는 root skill의 변경이며 각 reference의 수정일을 뜻하지 않는다. |
| Google Labs [Stitch design-md](https://github.com/google-labs-code/stitch-skills/blob/main/plugins/stitch-utilities/skills/design-md/SKILL.md) | [경로 history](https://github.com/google-labs-code/stitch-skills/commits/main/plugins/stitch-utilities/skills/design-md/SKILL.md): 2026-05-10 재배치 | 화면의 시각적 역할을 문서화하는 참고다. 파일 이동을 새로운 방법론 발표로 간주하지 않는다. |

적용을 변경할 때 원문을 다시 확인한다.

## Platform and conflict resolution

- 사용자 요구와 프로젝트의 보존 계약, 접근성·안전, 플랫폼의 실제 동작을 외부 aesthetic recipe보다 우선한다. 원문의 `MUST`는 해당 시스템 안에서의 규칙이지 모든 제품의 법칙이 아니다.
- [Apple typography](https://developer.apple.com/design/human-interface-guidelines/typography?changes=lat_2_6)를 native 글자 역할·Dynamic Type·플랫폼 차이의 기준으로 사용한다. CSS px와 Apple pt를 동일한 숫자 규칙으로 취급하지 않는다.
- [WCAG 2.2 target size](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html)의 24 CSS px와 예외는 웹 접근성 기준이다. 이를 이유로 기존 iOS 44pt touch contract를 축소하지 않는다.
- Recipe끼리 충돌하면 한 규칙을 조용히 선택하지 않고 적용 이유와 제외 이유를 적는다. 예: Impeccable의 일반 craft 효과 지침보다 작업용 Operate 맥락을 우선하며, native control을 장식용 custom control로 교체하지 않는다.
- Reference가 제안한 visual 값을 복사하지 않는다. 유지 중인 제품 문서에 `문제 → 근거 → 적용/유지/제외 → 변경 component → 검증`만 남기고 중복된 DESIGN.md나 빈 template은 만들지 않는다.

## Interaction source links

- [Apple Human Interface Guidelines: Feedback](https://developer.apple.com/design/human-interface-guidelines/feedback), [Alerts](https://developer.apple.com/design/human-interface-guidelines/alerts), [Progress indicators](https://developer.apple.com/design/human-interface-guidelines/progress-indicators), [Buttons](https://developer.apple.com/design/human-interface-guidelines/buttons)
- [Carbon Design System: Notifications](https://carbondesignsystem.com/patterns/notification-pattern/), [Spacing](https://carbondesignsystem.com/elements/spacing/overview/)
- [Primer: Forms](https://primer.style/product/ui-patterns/forms/), [Navigation](https://primer.style/product/ui-patterns/navigation/), [Notification messaging](https://primer.style/product/ui-patterns/notification-messaging/)
- [GitHub Docs writing best practices](https://docs.github.com/en/contributing/writing-for-github-docs/best-practices-for-github-docs)와 [basic Markdown writing](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
- [Zotero: Adding items and metadata by identifier](https://www.zotero.org/support/adding_items_to_zotero)
- [WAI-ARIA APG Window Splitter Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/windowsplitter/)과 [Tabs Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/tabs/)
- [WCAG 2.2 Error Identification](https://www.w3.org/WAI/WCAG22/Understanding/error-identification.html)과 [Status Messages](https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html)
