# App identity family candidate generation

## Scope

This review set explores role-specific application identity derivatives. It does not approve a candidate, alter a production icon, or define a platform export.

The simplified C/D round responds to owner feedback on the first A/B round: the mascot occupied too much of the tile, the compositions read as character illustrations rather than application icons, and the small role objects did not identify the applications strongly enough.

The exact generation reference was:

- approved base: `identity/approved/gnaroshi-base-v1.png`
- source candidate: `identity/candidates/07-cel-shaded.png`
- SHA-256: `2056b9e5cf7e3464aaf9c108849f0ec43ac1fbacd427ce73a6441e2619c380f6`
- verified relationship: the approved base and retained source candidate are byte-identical

Every candidate was created as an image edit with the approved base supplied as the raster reference input. The mascot was not recreated from a text description alone.

## Shared generation constraints

- Preserve the approved face, head shape, ears, four eyes, teeth, expression, cel-shaded rendering, and orange/teal identity exactly enough to keep family recognition.
- Reduce the mascot footprint to approximately 45–55 percent of the square instead of filling most of the tile.
- Give the role treatment approximately 28–38 percent of the composition while keeping it to one combined symbol or frame.
- Keep the role cue clear of the face, eyes, ears, teeth, and primary silhouette; it may read before the mascot when that improves application-role clarity.
- Use a deep charcoal-blue or dark blue-gray background, never pure black.
- Retain a strong silhouette, safe margin, and 32 px/64 px readability.
- Use broad outlines, large shapes, and no more than two shading levels for role artwork.
- Do not add text, watermarks, repository names, franchise logos, copied armor or emblems, neon, muddy color, excessive glow, miniature UI, card collages, or a busy scene.
- Candidate C places one direct role symbol in the lower-right foreground.
- Candidate D integrates one role frame behind or around the smaller mascot.

## Candidate prompts

| Candidate IDs | Product | Role treatment | Accents |
| --- | --- | --- | --- |
| `studio-c`, `studio-d` | Gnaroshi Studio | document and stylus; connected workspace hub frame | lavender, mint |
| `paperflow-c`, `paperflow-d` | PaperFlow | papers merging into one flow arrow; one paper on a broad flow ribbon | mint, sky blue |
| `arxiv-discovery-c`, `arxiv-discovery-d` | Arxiv Discovery | document with magnifier; document within scan corners | sky blue, peach |
| `tr-gpu-monitor-c`, `tr-gpu-monitor-d` | TR GPU Monitor | GPU chip with one pulse; GPU chip frame | aqua, soft coral |
| `runshelf-c`, `runshelf-d` | RunShelf | three indexed blocks on one shelf; one shelf frame | butter yellow, teal |
| `contentdeck-c`, `contentdeck-d` | ContentDeck | loop/play with subtitle strip; loop frame with subtitle strip | peach, lavender |

## Review files and tooling

Candidate masters and rendered review PNGs live under ignored `identity/review/` paths until the owner selects a direction. The normalized review masters are 2048×2048 square PNGs. The generation originals remain outside the repository and are not overwritten.

Generate or refresh the review sheets with the bundled workspace Python runtime and Pillow:

```bash
python3 identity/tools/build_app_family_review.py \
  --candidate-dir identity/review/candidates \
  --output-dir identity/review
```

The tool validates the twelve current C/D masters, normalizes non-2048 square inputs to 2048×2048, and creates:

- `app-family-contact-sheet.png`: squircle, circle, and square-mask comparison
- `app-family-dark-preview.png`: dark-surface comparison
- `app-family-light-preview.png`: light-surface comparison
- `app-family-small-sizes.png`: 16, 32, 64, 128, and 256 px comparison on both surfaces

The squircle is a review approximation. Production platform masks and optical corrections are separate work after owner selection.
