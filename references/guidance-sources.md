# 지침 구성의 조사 근거

확인일: 2026-09-30. 지침의 구성·탐색 방식을 변경할 때 비교한다. 적용 규칙은 [AGENTS.md](../AGENTS.md#문서-유지), 작업 선택은 [README.md](../README.md)에 둔다.

| 출처 | 확인한 방식 | 이 저장소의 적용 |
| --- | --- | --- |
| OpenAI [AGENTS.md 탐색](https://learn.chatgpt.com/docs/agent-configuration/agents-md) | Global과 project directory 지침을 순서대로 읽고 더 구체적인 지침을 우선한다. | [bootstrap](../bootstrap/global-AGENTS.md)은 연결만 제공한다. 별도 clone·MCP 문서를 자동으로 읽는다고 가정하지 않고 진입점을 명시한다. |
| OpenAI [Rethinking skills and prompts](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra) | 과도한 필독 목록과 오래된 제약을 재검토하고, 짧은 진입점에서 작업별 상세 문서로 연결한다. | 연구 figure의 공통 기준에서 제작 방식을 선택한다. 기술 도식 작업에 생성 일러스트 절차를 일괄 적용하지 않는다. |
| Anthropic [Memory와 지침 구성](https://code.claude.com/docs/en/memory) | 반복해서 설명해야 하는 규칙을 기록하고, 구체성·적용 범위·충돌 여부를 검토한다. 상세 절차는 필요할 때 읽는다. | 규칙 추가·문서 분리 기준을 AGENTS에 둔다. Claude 전용 import나 path 설정을 Codex 문서에 복사하지 않는다. |
| GitHub [Repository custom instructions](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions) | Repository 공통 규칙과 경로별 규칙을 구분한다. 실제 build·test·validation 정보를 제공한다. | 공통 작업 경계와 작업별 guide를 구분하고, 실제 검증 명령을 AGENTS에 둔다. 제품별 명령은 대상 저장소에서 관리한다. |
| Vercel Next.js [Skills authoring guide](https://github.com/vercel/next.js/blob/canary/.agents/skills/README.md) | 항상 필요한 짧은 규칙과 조건부 상세 workflow를 분리한다. 단순한 사실만으로 skill을 만들지 않는다. | 독립적인 적용 조건과 고유 규칙이 없는 문서는 합치거나 삭제한다. 기존 Markdown과 MCP로 충분한 지침을 일괄 skill로 포장하지 않는다. |

도구마다 자동 탐색·상속 방식이 다르므로 해당 형식의 효과를 다른 도구에 추정하지 않는다. 문서 길이나 파일 수를 목표로 삼지 않고, 필요한 규칙의 선택·실행·검증이 가능한지 확인한다.
