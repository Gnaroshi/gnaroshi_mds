# App identity family candidate generation

## Scope

The pixel P3 review set supersedes P2 for active owner review. P2B improved small-size role prominence, but owner review found that its abstract glyphs still did not communicate what any application actually does. The detached mascot crest also repeated more of the mascot than the role needed.

P3 changes the visual grammar:

- the application workflow is a large concrete foreground scene, not an abstract badge;
- the mascot is a shared partial background layer, not a complete separate crest;
- the foreground overlaps the mascot while preserving the large ears, helmet and cyan eyes as family recognition;
- every role scene shows a real object undergoing the app's representative action.

P3 does not approve a candidate, alter a production icon or define a platform export. Earlier A/B, C/D, P1 and P2 files remain review history only.

## Exact identity reference

- approved base: `identity/approved/gnaroshi-base-v1.png`
- source candidate: `identity/candidates/07-cel-shaded.png`
- approved-base SHA-256: `2056b9e5cf7e3464aaf9c108849f0ec43ac1fbacd427ce73a6441e2619c380f6`
- verified relationship: the approved base and retained source candidate are byte-identical

The approved base and the P2 pixel treatment were supplied as raster references for one common P3 template. Every application candidate then edited that same template; applications were not generated as independent mascot illustrations.

## Shared P3 construction

- Neutral review reference: `identity/review/candidates/gnaroshi-main-p3.png`
- Overlap template: `identity/review/candidates/pixel-family-template-p3.png`
- Template pre-normalization SHA-256: `50adeb4d372440b55fc54dbeefcecd4b40f524dbafcaa882d27001b76b3cd920`
- Composition: large role workflow in the lower/front layer; matching mascot ears, helmet and eyes behind it
- Fixed elements: deep charcoal background, stepped frame, mascot crop/anchor, orange/teal palette, pixel scale, outline and lighting
- Variable elements: one concrete workflow subject and its approved role colors

The generated sources are review rasters representing a `64×64` logical target. The review tool normalizes them to `2048×2048` with nearest-neighbor resampling. They are not coordinate-quantized production masters.

## P3 workflow vocabulary

| Candidate ID | Product | Concrete foreground workflow | Key colors |
| --- | --- | --- | --- |
| `studio-p3` | Gnaroshi Studio | research sheets enter a central authoring workbench where a pen creates a line that exits through a publish gate | lavender + mint |
| `paperflow-p3` | PaperFlow | research papers move on a conveyor through a guarded sorter into indexed library drawers | mint + sky blue |
| `arxiv-discovery-p3` | Arxiv Discovery | a radar sweep discovers one of several incoming research papers and passes it to a receiving slot | sky blue + peach |
| `tr-gpu-monitor-p3` | TR GPU Monitor | a recognizable GPU card exposes live metric bars/pulse and connects to remote hosts | soft coral + teal/aqua |
| `runshelf-p3` | RunShelf | experiment, metric trace and artifact evidence are retained as stacked run records in a ledger shelf | butter yellow + teal |
| `contentdeck-p3` | ContentDeck | a media screen shows large subtitles while two boundary pins loop one selected learning segment | peach + lavender |

P3 intentionally rejects the P2 document-only Studio, abstract PaperFlow arrows, scan gate, run lanes and repeat-first ContentDeck symbol. It also avoids vendor logos, repository names, text, terminal content, provider marks and app-specific mascot poses.

## Review files and tooling

Candidate masters and rendered review PNGs live under ignored `identity/review/` paths until the owner selects a direction. The tool creates:

- `app-family-contact-sheet.png`: centered neutral main plus six P3 workflow scenes
- `app-family-dark-preview.png`
- `app-family-light-preview.png`
- `app-family-small-sizes.png`: main plus P3 candidates at 16/32/64/128/256px

Refresh the sheets with:

```bash
python3 identity/tools/build_app_family_review.py \
  --candidate-dir identity/review/candidates \
  --output-dir identity/review
```

The squircle is a review approximation. Production selection still requires a deterministic `64×64` grid, simplified optical 16/32px masters, palette cleanup and real platform-mask verification.
