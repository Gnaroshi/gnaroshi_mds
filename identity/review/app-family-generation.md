# App identity family candidate generation

## Scope

The pixel P1 review set replaces the C/D round as the active owner-review set. It does not approve a candidate, alter a production icon, or define a platform export. Earlier A/B and C/D files remain review history only.

The exact identity reference was:

- approved base: `identity/approved/gnaroshi-base-v1.png`
- source candidate: `identity/candidates/07-cel-shaded.png`
- approved-base SHA-256: `2056b9e5cf7e3464aaf9c108849f0ec43ac1fbacd427ce73a6441e2619c380f6`
- verified relationship: the approved base and retained source candidate are byte-identical

The approved base was supplied as raster reference input to create one common pixel template. Each application candidate then used that same pixel template as its only raster reference. Applications were not generated as independent mascot illustrations.

## Shared pixel template

- Review-only template: `identity/review/candidates/pixel-family-template.png`
- Template SHA-256 before review normalization: `00831832c7861bdfb8e213a6e3bd6ff2e0f900be755baad07138d0183c83dd56`
- Design target: `64×64` logical pixel grid
- Current template source: generated `1254×1254` review raster, not yet a coordinate-quantized production grid
- Fixed elements: mascot scale, upper-left anchor, four eyes, ears, teeth, orange/teal palette, deep charcoal background, stepped frame
- Reserved element: one lower-right role-glyph area using one canonical glyph and one key color

The first template attempt was rejected before it received a candidate ID because it filled the tile and did not preserve a usable role-glyph zone. A first RunShelf attempt was also rejected before ID assignment because its blocks read as server equipment rather than experiment records.

## P1 candidate system

| Candidate ID | Product | Canonical role glyph | Key color |
| --- | --- | --- | --- |
| `studio-p1` | Gnaroshi Studio | document and pencil | lavender `#B8A7F3` |
| `paperflow-p1` | PaperFlow | stacked papers merging into one arrow | mint `#8FD9C0` |
| `arxiv-discovery-p1` | Arxiv Discovery | document and magnifying lens | sky `#82C7EE` |
| `tr-gpu-monitor-p1` | TR GPU Monitor | GPU chip and telemetry pulse | soft coral `#E9948E` |
| `runshelf-p1` | RunShelf | three flat run cards on a shelf with one status dot | butter yellow `#E9D27A` |
| `contentdeck-p1` | ContentDeck | loop, play, and subtitle strip | peach `#F2B58D` |

Every role glyph uses the same lower-right anchor, similar visual mass, broad square-pixel outline and no text, vendor mark, repository name or miniature interface.

## Review files and tooling

Candidate masters and rendered review PNGs live under ignored `identity/review/` paths until the owner selects a direction. The tool normalizes generated square sources to 2048×2048 with nearest-neighbor resampling and creates:

- `app-family-contact-sheet.png`
- `app-family-dark-preview.png`
- `app-family-light-preview.png`
- `app-family-small-sizes.png`

Refresh the sheets with:

```bash
python3 identity/tools/build_app_family_review.py \
  --candidate-dir identity/review/candidates \
  --output-dir identity/review
```

The squircle is a review approximation. Production masks, optical small-size corrections and platform exports are separate work after owner selection.
