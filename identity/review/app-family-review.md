# Gnaroshi application icon family review

Status: **owner selection required**. No P3 candidate is approved, recommended as final or selected by this document.

P3 uses one `overlap-workflow` family: the role workflow occupies the foreground and a partial shared mascot remains behind it. It replaces P2's detached complete crest and abstract role glyphs after owner feedback that the icons still required an explanation before their product roles could be understood.

The exact approved base is recorded in [`../approved/metadata.json`](../approved/metadata.json). Review binaries are intentionally ignored and must not be promoted to app icon sets, Electron/Tauri assets, favicons, menu-bar assets, website media or package metadata without explicit owner selection.

## Review criteria

- Workflow clarity: recognize the principal object and action before reading the app name.
- Product distinction: do not confuse PaperFlow organization with Arxiv discovery, or ContentDeck study with generic repeat playback.
- Base fidelity: the same large ears, helmet, cyan eyes and teal/orange family remain behind every workflow.
- 32px readability: the workflow subject leads; unnecessary secondary detail may disappear without changing its broad meaning.
- Family consistency: background, frame, mascot crop, overlap depth, pixel treatment and lighting remain stable.
- Surface quality: boundary and key color remain legible on dark and light surfaces.

## Candidate record

| Candidate ID | Application | Workflow clarity | Base fidelity | 32px readability | Dark/light quality | Review status | Reason |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `studio-p3` | Gnaroshi Studio | Medium-high | High | Medium-high | High | Owner review | Central workbench and pen show authoring; incoming research and outgoing publish rays add coordination, though this is the densest role scene. |
| `paperflow-p3` | PaperFlow | High | High | Medium | High | Owner review | Papers visibly travel through a sorter into library drawers; the 32px optical master should remove chart marks and retain paper/sorter/drawer masses. |
| `arxiv-discovery-p3` | Arxiv Discovery | High | High | High | High | Owner review | Radar sweep, multiple incoming papers and one discovered result distinguish discovery from organization. |
| `tr-gpu-monitor-p3` | TR GPU Monitor | High | High | High | High | Owner review | GPU hardware, live metrics and remote-host link remain distinct at 32px without vendor branding. |
| `runshelf-p3` | RunShelf | Medium-high | High | Medium-high | High | Owner review | Flask, metric trace, artifact cube and stacked records show experiment memory rather than launch; owner should confirm the experiment metaphor matches the product voice. |
| `contentdeck-p3` | ContentDeck | High | High | High | High | Owner review | Actual media frame, dominant subtitles and bounded timeline loop read as caption-segment practice rather than repeat alone. |

The 16px views are family-color checks, not full workflow tests. At 32px, PaperFlow and Studio retain their main foreground masses but need deterministic optical simplification after selection. The review rasters still contain extra shade steps and are not exact coordinate-quantized `64×64` masters.

## Owner decision

Record explicit selection, rejection or revision by P3 candidate ID. Semantic approval comes before palette/grid cleanup or any production export. No production repository changes occur in this review step.
