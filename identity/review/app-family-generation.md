# App identity family candidate generation

## Scope

This review set explores role-specific application identity derivatives. It does not approve a candidate, alter a production icon, or define a platform export.

The exact generation reference was:

- approved base: `identity/approved/gnaroshi-base-v1.png`
- source candidate: `identity/candidates/07-cel-shaded.png`
- SHA-256: `2056b9e5cf7e3464aaf9c108849f0ec43ac1fbacd427ce73a6441e2619c380f6`
- verified relationship: the approved base and retained source candidate are byte-identical

Every candidate was created as an image edit with the approved base supplied as the raster reference input. The mascot was not recreated from a text description alone.

## Shared generation constraints

- Preserve approximately 75 percent of the approved face, head shape, ears, four eyes, teeth, silhouette, cel-shaded rendering, and orange/teal identity.
- Limit the role treatment to approximately 25 percent.
- Keep the role cue subordinate and clear of the face, eyes, ears, teeth, and primary silhouette.
- Use a deep charcoal-blue or dark blue-gray background, never pure black.
- Retain a strong silhouette, safe margin, and 32 px/64 px readability.
- Do not add text, watermarks, repository names, franchise logos, copied armor or emblems, neon, muddy color, excessive glow, or a busy scene.
- Candidate A places the role object in the lower-right foreground.
- Candidate B places the role object as a background emblem.

## Candidate prompts

| Candidate IDs | Product | Role treatment | Accents |
| --- | --- | --- | --- |
| `studio-a`, `studio-b` | Gnaroshi Studio | layered workspace panel and stylus; subtle coordination cue | lavender, mint |
| `paperflow-a`, `paperflow-b` | PaperFlow | paper stack and one flowing ribbon/path | mint, sky blue |
| `arxiv-discovery-a`, `arxiv-discovery-b` | Arxiv Discovery | rolled document and compact lens/scanning cue | sky blue, peach |
| `tr-gpu-monitor-a`, `tr-gpu-monitor-b` | TR GPU Monitor | compact GPU chip and one telemetry pulse | aqua, soft coral |
| `runshelf-a`, `runshelf-b` | RunShelf | two or three run cards on a shelf and one status marker | butter yellow, teal |
| `contentdeck-a`, `contentdeck-b` | ContentDeck | loop ring, play cue, and text-free subtitle card | peach, lavender |

## Review files and tooling

Candidate masters and rendered review PNGs live under ignored `identity/review/` paths until the owner selects a direction. The normalized review masters are 2048×2048 square PNGs. The generation originals remain outside the repository and are not overwritten.

Generate or refresh the review sheets with the bundled workspace Python runtime and Pillow:

```bash
python3 identity/tools/build_app_family_review.py \
  --candidate-dir identity/review/candidates \
  --output-dir identity/review
```

The tool validates all twelve masters, normalizes non-2048 square inputs to 2048×2048, and creates:

- `app-family-contact-sheet.png`: squircle, circle, and square-mask comparison
- `app-family-dark-preview.png`: dark-surface comparison
- `app-family-light-preview.png`: light-surface comparison
- `app-family-small-sizes.png`: 16, 32, 64, 128, and 256 px comparison on both surfaces

The squircle is a review approximation. Production platform masks and optical corrections are separate work after owner selection.
