# App identity family candidate generation

## Scope

Pixel P5 supersedes P4 for active owner review. P4 fixed the generated-raster problem, but owner review identified three remaining system failures:

- four cyan eye shapes floated as unrelated decorations instead of reading as one intentional gaze;
- app artwork touched the mascot layer without a strong boundary;
- the six foregrounds shared pixel rendering but not a common object scale, container, perspective or semantic construction.

P5 uses one `hero-instrument` scheme. Every app has the same ear-and-visor canopy and the same bordered pro-instrument plate. The only changing elements are one role color and one representative work instrument with a visible action or result.

P5 does not approve a candidate, alter a production icon or define platform exports. P1–P4 remain review history only.

## Reference model

P5 uses reusable principles from the [Apple Human Interface Guidelines for app icons](https://developer.apple.com/design/human-interface-guidelines/app-icons/): one core idea, centered primary content, minimal shapes, clear foreground edges and consistent cross-platform recognition.

It does not copy Motion, Keynote, Final Cut Pro or any other Apple artwork. No Apple clapperboard, lectern, hardware silhouette, color wheel, material, trademark or proprietary asset appears in P5. The adopted pattern is the general `representative instrument + visible result` relationship, not any specific icon.

## Exact identity reference

- approved base: `identity/approved/gnaroshi-base-v1.png`
- source candidate: `identity/candidates/07-cel-shaded.png`
- approved-base SHA-256: `2056b9e5cf7e3464aaf9c108849f0ec43ac1fbacd427ce73a6441e2619c380f6`
- verified relationship: approved base and retained source candidate are byte-identical

The approved raster remains the reference for large ear shape, angular gaze and orange/teal recognition. P5 does not regenerate the mascot from a prompt.

## Fixed P5 construction

- source tool: `identity/tools/build_app_family_p5.py`
- source directory: `identity/review/candidates/p5-64/`
- review exports: `identity/review/candidates/*.png`
- grid: actual `64×64` RGB PNG
- export: `2048×2048`, nearest-neighbor only
- no image-generation model used
- no anti-aliasing, gradients, blur, glow, soft shadow or sub-pixel stroke

Every application reuses the same coordinates for:

1. deep charcoal tile and stepped outer frame;
2. orange ears and dark visor canopy;
3. four one-pixel cyan eye slits inside the visor;
4. black separation outline;
5. app-color outer rim and inner highlight;
6. dark front-facing instrument surface;
7. lower base/shadow and safe area.

The review builder rejects an export that is not an exact nearest-neighbor expansion of its corresponding 64px source.

## Role semantics

The icon test is `object + action/result`, not repository name association.

| Candidate ID | Product | Representative instrument | Visible action/result | Why this is the role rather than the name |
| --- | --- | --- | --- | --- |
| `studio-p5` | Gnaroshi Studio | editorial manuscript console | source tabs enter, a pen edits, publish output leaves | combines coordination, authoring and publishing instead of showing a generic studio panel |
| `paperflow-p5` | PaperFlow | guarded document sorter | one paper becomes ordered indexed slots | shows safe library organization instead of a decorative paper or flowing line |
| `arxiv-discovery-p5` | Arxiv Discovery | research radar scope | incoming paper blips cross a sweep and one result is acquired | shows active discovery instead of a magnifier or isolated document |
| `tr-gpu-monitor-p5` | TR GPU Monitor | dual-fan GPU instrument | live telemetry crosses the hardware and remote state remains attached | shows monitored hardware and status without a vendor logo or command line |
| `runshelf-p5` | RunShelf | stacked run-record archive | a run retains metric curve, status and artifact marker | shows durable experiment evidence rather than a literal furniture shelf |
| `contentdeck-p5` | ContentDeck | subtitle-study player | media, subtitle and bounded A–B segment coexist in one instrument | shows language practice rather than play or repeat alone |

## Source checksums

| Candidate ID | 64px source SHA-256 |
| --- | --- |
| `gnaroshi-main-p5` | `546913ec65e1e2883ed17fb68513f710b6273b5c2bef7d9f36dfb8b75846bbcc` |
| `studio-p5` | `c28d93f21951e028d1509ea921a2c15d1de4b7beb4b48a790327f82c88ecc49d` |
| `paperflow-p5` | `03f0d6d368545af2ba04446395d9626a016a319613afda1d3d3ef10ca83bf708` |
| `arxiv-discovery-p5` | `2a8b42bfed74068f10ddae974a0f9a42f347f4806b671e9e255fae0252babdaf` |
| `tr-gpu-monitor-p5` | `09489c4d7886685cdb6e3b50217c1d5aa35e6aaf61ad7c18fc7ca6339d5a0a47` |
| `runshelf-p5` | `aa86a80de3939904b4564a0d09846fb217fd74cb805a2d7cff4126399533837c` |
| `contentdeck-p5` | `8baee1beb9ab67fe2a1b246ee6cceca5f4268ecc1ead08be2fe53468bd0dab96` |

## Refresh review files

Candidate binaries and review PNGs remain under ignored `identity/review/` paths until owner selection.

```bash
python3 identity/tools/build_app_family_p5.py \
  --output-dir identity/review/candidates

python3 identity/tools/build_app_family_review.py \
  --candidate-dir identity/review/candidates \
  --output-dir identity/review
```

The sheets cover square, circular and approximate macOS squircle masks at 16/32/64/128/256px on light and dark surfaces. Production work remains blocked on explicit selection by candidate ID.
