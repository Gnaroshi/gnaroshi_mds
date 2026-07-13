# Gnaroshi application icon family review

Status: **owner selection required**. No P2 candidate is approved, recommended as final or selected by this document.

Pixel P2 compares two coherent composition families while keeping each family internally fixed:

- A / `vertical-panel`: the centered mascot remains prominent and the role glyph sits in a common panel below the face.
- B / `role-first`: the same family identity becomes a smaller centered crest and the role glyph becomes the dominant launcher subject.

P2 replaces the P1 upper-left mascot and lower-right attachment composition. It also replaces ambiguous single-function metaphors with product-purpose glyphs. The exact approved base is recorded in [`../approved/metadata.json`](../approved/metadata.json). Review binaries are intentionally ignored and must not be promoted to app icon sets, Electron/Tauri assets, favicons, menu-bar assets, website media or package metadata without explicit owner selection.

## Review criteria

- Role clarity: identify the application purpose before reading its name.
- Base identity fidelity: recognize the same ears, four eyes, teeth, face and orange/teal family.
- 32px readability: the role glyph leads while the mascot remains a recognizable family crest.
- Family consistency: background, frame, mascot treatment, role container, outline and pixel scale do not change inside A or B.
- Surface quality: boundary and key color remain legible on dark and light surfaces.

## Candidate record

| Candidate ID | Application | Role clarity | Base fidelity | 32px readability | Dark/light quality | Review status | Reason |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `studio-p2a` | Gnaroshi Studio | High | High | Medium-high | High | Owner review | Centered mascot plus document, pencil and publish cue; writing remains explicit. |
| `studio-p2b` | Gnaroshi Studio | High | High | High | High | Owner review | The larger document/pencil silhouette leads before the crest. |
| `paperflow-p2a` | PaperFlow | High | High | Medium-high | High | Owner review | Multiple papers visibly converge into an organized tray rather than a generic folder. |
| `paperflow-p2b` | PaperFlow | High | High | High | High | Owner review | Large guided flow and tray remain distinct from discovery scanning. |
| `arxiv-discovery-p2a` | Arxiv Discovery | High | High | Medium-high | High | Owner review | Incoming papers cross a scan gate; no generic magnifier or arXiv logo. |
| `arxiv-discovery-p2b` | Arxiv Discovery | High | High | High | High | Owner review | Scan gate and discovery spark dominate at small sizes. |
| `tr-gpu-monitor-p2a` | TR GPU Monitor | High | High | Medium-high | High | Owner review | GPU, telemetry and remote nodes are combined without vendor branding. |
| `tr-gpu-monitor-p2b` | TR GPU Monitor | High | High | High | High | Owner review | The GPU silhouette leads and retains the remote-status cue. |
| `runshelf-p2a` | RunShelf | Medium-high | High | Medium-high | High | Owner review | Start-to-result lanes express experiment runs; owner should confirm that the bracket reads as an index rather than sliders. |
| `runshelf-p2b` | RunShelf | Medium-high | High | High | High | Owner review | Large lanes and distinct result markers improve the previous block/shelf metaphor, but still require owner semantic validation. |
| `contentdeck-p2a` | ContentDeck | High | High | Medium-high | High | Owner review | Subtitle card is primary; segment brackets and loop are secondary. |
| `contentdeck-p2b` | ContentDeck | High | High | High | High | Owner review | Dominant subtitle card prevents the icon from reading as generic repeat playback. |

The 16px views are identity and color checks; role recognition is evaluated primarily at 32px and 64px. Generated glyph fills still contain more shade steps than the two-step production rule permits, and the review rasters are not exact coordinate-quantized `64×64` masters. Those are post-selection production tasks, not reasons to auto-select a candidate now.

## Owner decision

Review A and B as complete families, then record explicit selections, rejections or revision requests by candidate ID. The owner may select one composition family for every app or request a specific semantic refinement before production export. No production repository changes occur in this review step.
