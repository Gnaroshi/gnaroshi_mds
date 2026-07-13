# Gnaroshi application icon family review

Status: **owner selection required**. No P4 candidate is approved, recommended as final or selected by this document.

P4 removes the generated-scene look and awkward partial-face overlap. Each app reuses exactly the same ears-and-four-eyes identity band; the functional role occupies the foreground. The neutral `gnaroshi-main-p4` keeps that mark centered without an application role.

The exact approved base is recorded in [`../approved/metadata.json`](../approved/metadata.json). Review binaries are ignored and must not be promoted to app icon sets, Electron/Tauri assets, favicons, menu-bar assets, website media or package metadata without explicit owner selection.

## Review criteria

- Intentional identity crop: the ears-and-eyes band must look like a deliberate brand mark, never a face hidden behind another object.
- Non-generated construction: every edge must align to the 64px grid and remain reproducible from the checked-in tool.
- Functional clarity: the lower subject should communicate the app's object and action before its name is read.
- Product distinction: PaperFlow organization must not resemble arXiv discovery; ContentDeck study must not read as repeat playback alone.
- 32px readability: role mass and key color lead; identity remains recognizable but secondary.
- Family consistency: frame, identity-band pixels, outline weight, depth and material remain identical.
- Surface quality: silhouettes and accents remain visible on light and dark surfaces.

## Candidate record

| Candidate ID | Application | Role clarity | Base fidelity | 32px readability | Dark/light quality | Review status | Reason |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `studio-p4` | Gnaroshi Studio | Medium-high | High | Medium-high | High | Owner review | Inputs, central authoring hub/pen nib and publish output express coordination plus creation. The hub is intentionally denser than the other roles; confirm it reads as Studio rather than a generic network tool. |
| `paperflow-p4` | PaperFlow | High | High | High | High | Owner review | Papers, guarded funnel/check and library drawers show safe organization rather than download or deletion. |
| `arxiv-discovery-p4` | Arxiv Discovery | High | High | High | High | Owner review | Radar field, scan sweep and multiple incoming papers show discovery, not merely a document or magnifier. |
| `tr-gpu-monitor-p4` | TR GPU Monitor | High | High | High | High | Owner review | Dual-fan GPU, metric pulse and remote link identify read-only hardware monitoring without vendor marks. |
| `runshelf-p4` | RunShelf | Medium-high | High | High | High | Owner review | Stacked record tabs, experiment cue and retained metric/artifact show organized experiment results. Confirm the small flask remains appropriate to RunShelf's verified product role. |
| `contentdeck-p4` | ContentDeck | High | High | High | High | Owner review | Media screen, dominant subtitle block and bounded loop show subtitle-segment study rather than generic repeat playback. |

At 16px the candidates are identity/key-color indicators. At 32px their primary object remains distinct; detailed secondary actions become fully legible at 64px. Studio and RunShelf are intentionally recorded as the two candidates that still require the most semantic scrutiny instead of being auto-recommended.

## Owner decision

Record selection, rejection or revision with the P4 candidate ID. No production repository changes occur in this review step.
