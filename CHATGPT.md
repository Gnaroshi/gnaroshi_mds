# ChatGPT usage

이 저장소를 연결한 ChatGPT는 대화 시작 시 다음 순서를 따른다.

1. `README.md`와 `AGENTS.md`를 읽는다.
2. `catalog/projects.md`에서 작업 대상을 확인한다.
3. 작업 유형에 맞는 `gnaroshi://guides/...` resource 또는 같은 경로의 Markdown을 읽는다.
4. application integration이면 `guides/app-integration.md`, cross-repository change이면 `guides/cross-repo-changes.md`, visual identity이면 `guides/app-icons.md`를 추가로 읽는다.
5. 논문·연구 figure이면 `guides/technical-figure-code.md`와 `guides/scientific-figure-generation.md`를 모두 읽되, 현재 사용자가 요청한 role, output format과 산출물 수를 따른다. PNG/raster와 image generation을 혼동하지 않고, technical schematic은 constructed 2D로 만들며 generated imagery는 cover, teaser와 non-technical concept에 제한한다.
6. 대상 프로젝트의 최신 문서를 더 구체적인 사실로 사용한다.
7. 대화에서 재사용 가능한 선호나 규칙이 새로 확정되면 `gnaroshi_mds` 업데이트를 먼저 제안하거나 수행한다.

ChatGPT 데스크톱은 Codex host의 MCP 설정을 공유할 수 있다. ChatGPT 웹은 로컬 MCP 설정을 읽지 않으므로 GitHub 저장소를 프로젝트 source로 연결하거나 이 문서를 project instruction에 넣는다. Codex CLI나 MCP를 설치할 수 없는 VS Code Remote-SSH server에서는 cloned repository의 Markdown을 absolute path로 직접 읽는다.
