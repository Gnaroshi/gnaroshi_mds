# Gnaroshi application icon family review

Status: **owner selection required**. The recommendation field is a review-quality screen only; no candidate is approved or selected by this document.

The candidates use the exact approved base identified in [`../approved/metadata.json`](../approved/metadata.json). Review binaries are intentionally ignored and must not be promoted to application icon sets, Electron/Tauri assets, favicons, menu-bar assets, website media, or package metadata without a separate owner decision.

## Review criteria

- Role clarity: whether the app purpose can be inferred without a wordmark.
- Base identity fidelity: whether the approved face, ears, four eyes, teeth, silhouette, cel shading, and teal/orange identity remain primary.
- 32 px readability: whether the face remains readable and the role cue survives without competing with it.
- Surface quality: whether the boundary and accents remain legible on dark and light review surfaces.
- Recommended/rejected: a non-binding review-quality screen. `Recommended for owner review` means the candidate is coherent enough to compare; `Reject from this round` means it should not be promoted without revision.

## Candidate record

| Candidate ID | Application | Role clarity | Base identity fidelity | 32 px readability | Dark-mode quality | Light-mode quality | Recommended/rejected | Reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `studio-a` | Gnaroshi Studio | Medium-high | High | Face high; role cue low | High | High | Recommended for owner review | The foreground panel and stylus are compact and distinct at launcher size, but become a color cue rather than a readable object at 32 px. |
| `studio-b` | Gnaroshi Studio | Medium | High | Face high; role cue low | High | High | Recommended for owner review | The layered workspace stays behind the mascot and preserves the silhouette; its role meaning is intentionally subtle at small sizes. |
| `paperflow-a` | PaperFlow | High | High | Face high; role cue medium | High | High | Recommended for owner review | The paper stack and mint/sky flow remain recognizable without a Zotero mark and stay subordinate to the face. |
| `paperflow-b` | PaperFlow | Medium-high | High | Face high; role cue low-medium | High | High | Recommended for owner review | The background papers and flow create a clean family variant, although the role cue loses detail before the mascot does. |
| `arxiv-discovery-a` | Arxiv Discovery | High | High | Face high; role cue medium | High | High | Recommended for owner review | The foreground scroll and lens communicate document discovery clearly; the lens becomes a small blue/orange cue at 32 px. |
| `arxiv-discovery-b` | Arxiv Discovery | High | High | Face high; role cue medium | High | High | Recommended for owner review | The document and lens read clearly behind the ears without using the arXiv identity; compare its relatively prominent upper emblem with A. |
| `tr-gpu-monitor-a` | TR GPU Monitor | High | High | Face high; role cue medium | High | High | Recommended for owner review | The compact GPU and pulse are immediately recognizable without a vendor logo and remain below the face. |
| `tr-gpu-monitor-b` | TR GPU Monitor | Medium-high | High | Face high; role cue low | High | High | Recommended for owner review | The chip outline and pulse preserve the central mascot, but the thin telemetry treatment is faint at 32 px. |
| `runshelf-a` | RunShelf | Medium-high | High | Face high; role cue low-medium | High | High | Recommended for owner review | The shelf and three cards are readable at launcher size; the running-person pictogram may suggest fitness rather than experiment runs. |
| `runshelf-b` | RunShelf | Medium | High | Face high; role cue low | High | High | Reject from this round | The upper shelf remains subordinate, but incidental card pictograms add density and introduce an unnecessary emblem-like face that should be removed in a refinement. |
| `contentdeck-a` | ContentDeck | High | High | Face high; role cue medium | High | High | Recommended for owner review | The loop/play and text-free subtitle card form a clear playback-learning cue and retain separation on both surfaces. |
| `contentdeck-b` | ContentDeck | High | High | Face high; role cue medium | High | High | Recommended for owner review | The background loop is clear and the subtitle-card cue stays secondary; compare the larger emblem presence with candidate A. |

## Owner decision

Record an explicit selection, rejection, or request for revision in a follow-up change. Selection must name the candidate ID and must not directly overwrite production icons; platform exports and application updates remain separate work.
