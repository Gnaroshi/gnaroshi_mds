# Gnaroshi guidance MCP

`server.py` exposes the repository's canonical Markdown as read-only MCP resources. It has no third-party dependency and never writes to project files.

## Install on this Mac

```bash
codex mcp add gnaroshiGuidance -- \
  python3 /Users/gnaroshi/Desktop/programming/git/gnaroshi_mds/mcp/server.py
```

Restart Codex or the ChatGPT desktop app after changing MCP configuration. Codex CLI, IDE extension, and the desktop app on the same Codex host share the configuration.

ChatGPT web does not read local Codex MCP configuration. Connect the GitHub repository to a ChatGPT project and use `CHATGPT.md` there.

## Read order

1. `gnaroshi://index`
2. `gnaroshi://agents`
3. `gnaroshi://catalog/projects`
4. one of `gnaroshi://guides/research`, `gnaroshi://guides/application`, `gnaroshi://guides/web-application`
5. `gnaroshi://guides/ui-ux`
6. `gnaroshi://guides/image-assets` for visual work

## Manual protocol check

```bash
printf '%s\n' \
  '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2025-06-18","capabilities":{},"clientInfo":{"name":"check","version":"1"}}}' \
  '{"jsonrpc":"2.0","method":"notifications/initialized"}' \
  '{"jsonrpc":"2.0","id":2,"method":"resources/list"}' \
  | python3 mcp/server.py
```
