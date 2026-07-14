# App identity family candidate generation

## Scope

Pixel P5 supersedes P4 and was owner-approved for production on 2026-07-14. P4 fixed the generated-raster problem, but owner review identified three remaining system failures:

- four cyan eye shapes floated as unrelated decorations instead of reading as one intentional gaze;
- app artwork touched the mascot layer without a strong boundary;
- the six foregrounds shared pixel rendering but not a common object scale, container, perspective or semantic construction.

P5 uses one `hero-instrument` scheme. Every app has the same ear-and-visor canopy and the same bordered pro-instrument plate. The only changing elements are one role color and one representative work instrument with a visible action or result.

P1–P4 remain review history only. P5 canonical 2048px masters are exported to `identity/approved/apps/`; each application still owns its deterministic platform exports.

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
| `gnaroshi-main-p5` | `81853cd37db6fc592d0d966da1f949c0a246ed2bc197e5f94dd624c69fda164c` |
| `studio-p5` | `693a04561d423c59c7f01352b7599b38ea6506506bb2a3507b344fa7fbfc7ed7` |
| `paperflow-p5` | `dbfe1e609aeeeae5788dcb4ce227b65446d469bf3ececcc51d9cc8bfd8627aa2` |
| `arxiv-discovery-p5` | `5f03aef0733536fe2fd411450c4f3e49393df98b53412b325e76803c04e9de0a` |
| `tr-gpu-monitor-p5` | `b87db0f137cf08ed6778520a09daf57902d371867d0664689cc2f8758ca7f8ec` |
| `runshelf-p5` | `80d78ebfee755ccecb9927c176f0dc7d4c7e2521ce89eb9979aea343d954a390` |
| `contentdeck-p5` | `6db90777b602fdee3ce86d833db8d9f39d515e8d33b7b1ff87eea2f904711703` |

## Refresh review files

Candidate binaries and review PNGs remain under ignored `identity/review/` paths. The approved exports are generated separately into the tracked canonical directory.

```bash
python3 identity/tools/build_app_family_p5.py \
  --output-dir identity/review/candidates

python3 identity/tools/build_app_family_review.py \
  --candidate-dir identity/review/candidates \
  --output-dir identity/review
```

The sheets cover square, circular and approximate macOS squircle masks at 16/32/64/128/256px on light and dark surfaces.

## Export approved masters

```bash
python3 identity/tools/promote_app_family_p5.py \
  --output-dir identity/approved/apps
```

This command exports only the owner-approved P5 IDs and refreshes their SHA-256 metadata. It does not update any application repository.
