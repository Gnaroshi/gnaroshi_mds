# Gnaroshi guidance MCP

`server.py` exposes the repository's canonical Markdown as read-only MCP resources. It has no third-party dependency and never writes to project files.

## Install on this Mac

```bash
codex mcp add gnaroshiGuidance -- \
  python3 /Users/gnaroshi/Desktop/programming/git/gnaroshi_mds/mcp/server.py
```

Restart Codex or the ChatGPT desktop app after changing MCP configuration. Codex CLI, IDE extension, and the desktop app can share the configuration when they run on the same configured host.

ChatGPT web does not read local Codex MCP configuration. Connect the GitHub repository to a ChatGPT project and use `CHATGPT.md` there.

## Read order

1. `gnaroshi://index`
2. `gnaroshi://agents`
3. `gnaroshi://catalog/projects`
4. one of `gnaroshi://guides/research`, `gnaroshi://guides/application`, `gnaroshi://guides/web-application`
5. `gnaroshi://guides/ui-ux`
6. `gnaroshi://guides/app-integration` for application ecosystem work
7. `gnaroshi://guides/cross-repo-changes` for multi-repository or architecture changes
8. `gnaroshi://guides/app-distribution` for signing, packaging, version, and update work
9. `gnaroshi://guides/image-assets` and `gnaroshi://guides/app-icons` for image and identity work
10. `gnaroshi://guides/technical-figure-code` and `gnaroshi://guides/scientific-figure-generation` for paper and research figure work
11. `gnaroshi://guides/authoring-editor` for long-form Markdown, media, and formula authoring work

Reading both figure resources establishes their boundaries; it does not require paired output. The current user request controls the figure role, final format, and output count. Technical schematics remain constructed; generated imagery is limited to illustration roles.

## VS Code Remote-SSH without Codex CLI or MCP

MCP is not required. On a security-constrained SSH server:

1. Clone `gnaroshi_mds` once.
2. Before each figure task, run `git -C <gnaroshi_mds-clone> pull --ff-only origin main`.
3. In the target repository's `AGENTS.md`, require direct reads of:
   - `<gnaroshi_mds-clone>/AGENTS.md`
   - `<gnaroshi_mds-clone>/guides/research.md`
   - `<gnaroshi_mds-clone>/guides/technical-figure-code.md`
   - `<gnaroshi_mds-clone>/guides/scientific-figure-generation.md`
4. Treat the clone as a read-only reference. Keep project-specific figure specs and evidence maps in the target repository.

The VS Code extension can read these files through the remote workspace filesystem. Do not install Codex CLI or open an MCP service solely to consume this guidance.

Recommended target-repository `AGENTS.md` snippet:

```md
## Gnaroshi figure guidance

For every paper or research figure task:

1. Run `git -C <gnaroshi_mds-clone> pull --ff-only origin main`.
2. Read `<gnaroshi_mds-clone>/AGENTS.md`.
3. Read `<gnaroshi_mds-clone>/guides/research.md`.
4. Read `<gnaroshi_mds-clone>/guides/technical-figure-code.md`.
5. Read `<gnaroshi_mds-clone>/guides/scientific-figure-generation.md`.
6. Record the inspected `gnaroshi_mds` commit in the project-local figure spec.

The guidance clone is read-only. Reusable rules belong in `gnaroshi_mds`;
project-specific terminology, captions, implementation evidence, and figure
specifications stay in this repository.
```

## Manual protocol check

```bash
printf '%s\n' \
  '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2025-06-18","capabilities":{},"clientInfo":{"name":"check","version":"1"}}}' \
  '{"jsonrpc":"2.0","method":"notifications/initialized"}' \
  '{"jsonrpc":"2.0","id":2,"method":"resources/list"}' \
  | python3 mcp/server.py
```
