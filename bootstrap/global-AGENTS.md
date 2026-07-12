# Gnaroshi global working agreements

## Canonical guidance

- At the beginning of substantive development work, read the `gnaroshiGuidance` MCP resource `gnaroshi://index`. If MCP is unavailable, inspect the latest local checkout at `/Users/gnaroshi/Desktop/programming/git/gnaroshi_mds` and sync it from `https://github.com/Gnaroshi/gnaroshi_mds` when network access and authorization allow.
- Classify the task as research, application, or web application and read the matching guide before making design or documentation decisions.
- Project-local `AGENTS.md` and user instructions remain more specific and take precedence.
- When a conversation establishes a reusable preference or workflow rule, update `gnaroshi_mds` and push it before finishing, provided the change is authorized. Never copy secrets, private research content, credentials, transient logs, or project-specific implementation details into it.

## Design and images

- Prefer simple interfaces that show purpose, prerequisites, order, current state, and next action clearly to a first-time user.
- Avoid unnecessary text, decorative components, inconsistent padding or margins, and responsive clipping.
- Unless the user explicitly asks for a vector image, interpret image-generation requests as raster and never generate SVG or another vector format.
- Functional UI icons may use SF Symbols, Lucide, or a consistent custom monochrome vector system; the raster default is not a blanket rule for every toolbar control.
