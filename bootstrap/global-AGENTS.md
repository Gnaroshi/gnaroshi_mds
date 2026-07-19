# Gnaroshi global working agreements

## Canonical guidance

- At the beginning of substantive development work, read the `gnaroshiGuidance` MCP resource `gnaroshi://index`. If MCP or Codex CLI is unavailable, use a cloned `gnaroshi_mds` checkout, fast-forward it from `https://github.com/Gnaroshi/gnaroshi_mds` when network access and authorization allow, and read its Markdown directly. In VS Code Remote-SSH, the target project's `AGENTS.md` should name the clone's absolute path because sibling repositories are not assumed to be discovered automatically.
- Classify the task as research, application, or web application and read the matching guide before making design or documentation decisions.
- Project-local `AGENTS.md` and user instructions remain more specific and take precedence.
- When a conversation establishes a reusable preference or workflow rule, update `gnaroshi_mds` and push it before finishing, provided the change is authorized. Never copy secrets, private research content, credentials, transient logs, or project-specific implementation details into it.

## Design and images

- Prefer simple interfaces that show purpose, prerequisites, order, current state, and next action clearly to a first-time user.
- Avoid unnecessary text, decorative components, inconsistent padding or margins, and responsive clipping.
- Unless the user explicitly asks for a vector image, interpret image-generation requests as raster and never generate SVG or another vector format.
- For paper and research figures, read both figure guides but let the current request control the role, output format, and number of outputs. Do not add a code baseline, generated candidate, or paired review unless requested.
- Treat PNG/raster as an export format, not a generation method. Build technical schematics as flat constructed graphics with real text; reserve image generation for covers, teasers, and non-technical concepts.
- Ground implemented-system figures in the current working tree and an evidence map for every visible module, arrow, operator, time index, training state, and technical label. Keep technical panels flat, and require exact readable semantic text in final rasters instead of blank labels, pseudo-text, or 3D computation metaphors.
- Functional UI icons may use SF Symbols, Lucide, or a consistent custom monochrome vector system; the raster default is not a blanket rule for every toolbar control.
