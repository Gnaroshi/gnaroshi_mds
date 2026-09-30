# Gnaroshi guidance

- 작업 시작 시 `gnaroshiGuidance`의 `gnaroshi://index`와 `gnaroshi://agents`를 읽고 index의 작업별 지침을 따른다.
- MCP가 없으면 `https://github.com/Gnaroshi/gnaroshi_mds`의 local clone에서 `README.md`와 `AGENTS.md`를 직접 읽는다. Clean `main` checkout은 접근 권한과 network가 허용할 때 `git pull --ff-only origin main`으로 갱신한다. 사용자 변경을 덮어쓰지 않는다.
- Remote-SSH에서는 target project의 `AGENTS.md`에 clone의 absolute path를 명시한다. 연결용 clone은 읽기 참조로 사용하고 reusable rule 변경은 canonical checkout에 반영한다.
