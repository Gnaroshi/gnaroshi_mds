# Gnaroshi application icon family review

Status: **owner selection required**. The recommendation field is a review-quality screen only; no candidate is approved or selected by this document.

This is the simplified C/D round. It replaces the first A/B round for active review without deleting its history. The new compositions make the mascot smaller, remove miniature decorative detail, and make the application role a larger single symbol or frame.

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
| `studio-c` | Gnaroshi Studio | High | High | Face high; writing cue high | High | High | Recommended for owner review | One document-and-stylus symbol reads immediately and removes the miniature workspace decoration from the first round. |
| `studio-d` | Gnaroshi Studio | Medium-high | High | Face high; hub cue medium | High | High | Recommended for owner review | The smaller mascot and broad connected frame express central coordination, though the hub is less specific than C's writing cue. |
| `paperflow-c` | PaperFlow | High | High | Face high; flow cue high | High | High | Recommended for owner review | Three papers merging into one arrow communicate safe organized movement with one bold symbol. |
| `paperflow-d` | PaperFlow | High | High | Face high; flow cue high | High | High | Recommended for owner review | The single paper on a broad ribbon makes the flow role primary while keeping the mascot recognizable. |
| `arxiv-discovery-c` | Arxiv Discovery | High | High | Face high; discovery cue high | High | High | Recommended for owner review | A document and magnifier remain distinct at small size without using the arXiv logo. |
| `arxiv-discovery-d` | Arxiv Discovery | High | High | Face high; scan cue high | High | High | Recommended for owner review | Broad scan corners and one paper create the clearest provider-style scanning treatment in the family. |
| `tr-gpu-monitor-c` | TR GPU Monitor | High | High | Face high; GPU cue high | High | High | Recommended for owner review | The single chip and pulse are direct, vendor-neutral, and substantially simpler than the first round. |
| `tr-gpu-monitor-d` | TR GPU Monitor | High | High | Face high; chip cue high | High | High | Recommended for owner review | The chip frame makes monitoring the dominant identity while the smaller mascot remains centered. |
| `runshelf-c` | RunShelf | High | High | Face high; shelf cue high | High | High | Recommended for owner review | Three plain indexed blocks on one shelf avoid the previous fitness and chart ambiguity. |
| `runshelf-d` | RunShelf | Medium-high | High | Face high; shelf cue medium-high | High | High | Recommended for owner review | The broad shelf frame is simple and coherent, although it can also read as a storage grid before the product context is known. |
| `contentdeck-c` | ContentDeck | High | High | Face high; media cue high | High | High | Recommended for owner review | Loop, play, and subtitle strip form one direct media-learning symbol without resembling a provider logo. |
| `contentdeck-d` | ContentDeck | High | High | Face high; media cue high | High | High | Recommended for owner review | The mascot inside the loop with a subtitle base is the most integrated treatment and stays simple at small sizes. |

## Owner decision

Record an explicit selection, rejection, or request for revision in a follow-up change. Selection must name the candidate ID and must not directly overwrite production icons; platform exports and application updates remain separate work.
