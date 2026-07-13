# App identity family candidate generation

## Scope

The pixel P2 review set supersedes P1 for active owner review. P1 established a common pixel treatment but placed the mascot at the upper-left and treated every product role as a small lower-right attachment. Owner review found that composition off-center, weaker at small sizes and too generic for Arxiv Discovery, RunShelf and ContentDeck.

P2 corrects the system without approving a candidate, altering a production icon or defining a platform export. Earlier A/B, C/D and P1 files remain review history only.

The exact identity reference remains:

- approved base: `identity/approved/gnaroshi-base-v1.png`
- source candidate: `identity/candidates/07-cel-shaded.png`
- approved-base SHA-256: `2056b9e5cf7e3464aaf9c108849f0ec43ac1fbacd427ce73a6441e2619c380f6`
- verified relationship: the approved base and retained source candidate are byte-identical

The approved base was supplied as raster reference input for the shared pixel construction. P2 app candidates were generated only by editing one of the two common P2 templates; the mascot was not independently described or regenerated for each app.

## Centered main reference

- Review-only reference: `identity/review/candidates/gnaroshi-main-p2.png`
- Pre-normalization SHA-256: `add782d9ceda9898cfd2d3a94b8031b9161290190abe5943d5d3360a2586d99b`
- Construction: mascot centered on the horizontal and vertical axes, no role object or empty panel
- Purpose: define the neutral Gnaroshi family mark separately from application variants

The main reference is not one of the 12 app candidates and is not a production selection.

## Shared P2 templates

| Template | Review-only path | Pre-normalization SHA-256 | Fixed composition |
| --- | --- | --- | --- |
| P2A `vertical-panel` | `identity/review/candidates/pixel-family-template-p2a.png` | `754f116111d967a6d04809d80128a4fae241aa130bfb247e42b05702e331f422` | large centered mascot above one common lower role panel |
| P2B `role-first` | `identity/review/candidates/pixel-family-template-p2b.png` | `6419af499df1ae5ffcea7c69a0f9cbf64feb1b50baf04b07b4f8175bc619360b` | small centered mascot crest above one dominant central role emblem |

Both templates share the deep charcoal background, stepped frame, orange/teal mascot palette, symmetric center axis, hard pixel edges and common outline language. Current generated sources are `1254×1254` review rasters representing a `64×64` logical target; they are normalized to `2048×2048` with nearest-neighbor resampling for review. They are not yet coordinate-quantized production masters.

## P2 semantic vocabulary

| Application | Candidate A | Candidate B | Product meaning encoded | Key colors |
| --- | --- | --- | --- | --- |
| Gnaroshi Studio | `studio-p2a` | `studio-p2b` | writing document + pencil + outward publish cue | lavender + mint |
| PaperFlow | `paperflow-p2a` | `paperflow-p2b` | multiple papers following a guided path into an organized tray | mint + sky blue |
| Arxiv Discovery | `arxiv-discovery-p2a` | `arxiv-discovery-p2b` | multiple incoming papers passing a scan gate and producing a discovery spark | sky blue + peach |
| TR GPU Monitor | `tr-gpu-monitor-p2a` | `tr-gpu-monitor-p2b` | GPU hardware + live telemetry + remote nodes | soft coral + teal/aqua |
| RunShelf | `runshelf-p2a` | `runshelf-p2b` | three experiment-run lanes from common start markers to indexed result markers | butter yellow + teal |
| ContentDeck | `contentdeck-p2a` | `contentdeck-p2b` | dominant subtitle card + selected segment brackets + playback/loop cue | peach + lavender |

The P2 vocabulary intentionally removes the P1 magnifying glass, generic run blocks and repeat-first ContentDeck symbol. It also avoids vendor logos, repository names, text, miniature dashboards and app-specific mascot poses.

## Review files and tooling

Candidate masters and rendered review PNGs live under ignored `identity/review/` paths until the owner selects a direction. The tool normalizes square sources to `2048×2048` with nearest-neighbor resampling and creates:

- `app-family-contact-sheet.png`: centered main reference followed by A/B comparison per app
- `app-family-dark-preview.png`
- `app-family-light-preview.png`
- `app-family-small-sizes.png`: main plus all 12 candidates at 16/32/64/128/256px

Refresh the sheets with:

```bash
python3 identity/tools/build_app_family_review.py \
  --candidate-dir identity/review/candidates \
  --output-dir identity/review
```

The squircle is a review approximation. Production selection still requires a deterministic `64×64` grid, palette cleanup, optical 16/32px exports and real platform mask verification.
