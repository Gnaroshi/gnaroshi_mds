# Gnaroshi application icon family review

Status: **owner selection required**. No P5 candidate is approved, recommended as final or selected by this document.

P5 is one `hero-instrument` family. Every app uses the same ear-and-visor canopy, black separation outline, colored role rim, dark instrument surface, front-facing perspective and depth. The role instrument changes; the visual system does not.

The exact approved base is recorded in [`../approved/metadata.json`](../approved/metadata.json). Review binaries are ignored and must not be promoted to app icon sets, Electron/Tauri assets, favicons, menu-bar assets, website media or package metadata without explicit owner selection.

## Review criteria

- Gaze quality: four cyan eye slits must read as one restrained visor, not floating face fragments.
- Layer separation: the role plate border must clearly separate mascot identity from application function.
- Scheme consistency: all six plates use the same bounds, perspective, border weight, highlight, inner surface and base.
- Role clarity: the hero object must show a representative instrument plus an action/result, not merely illustrate the product name.
- Product distinction: PaperFlow organization must not resemble arXiv acquisition; ContentDeck study must not resemble generic playback; RunShelf must not resemble a dashboard alone.
- 32px readability: the role instrument leads while the common canopy remains a secondary family cue.
- Surface quality: silhouette, border and key color remain visible on light and dark surfaces.

## Candidate record

| Candidate ID | Application | Role reading with name hidden | Scheme consistency | 32px readability | Dark/light quality | Review status | Remaining risk |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `studio-p5` | Gnaroshi Studio | manuscript authoring with multiple inputs and one publish output | High | High | High | Owner review | At 16px only the page/pen mass remains; coordination becomes explicit at 32–64px. |
| `paperflow-p5` | PaperFlow | a paper passes through a guarded sorter into indexed slots | High | High | High | Owner review | The small check/sorter interior is secondary; paper and output slots carry the 32px reading. |
| `arxiv-discovery-p5` | Arxiv Discovery | a radar sweep acquires incoming paper targets | High | High | High | Owner review | Ensure the white targets continue to read as papers rather than generic radar blips. |
| `tr-gpu-monitor-p5` | TR GPU Monitor | dual-fan GPU with live telemetry and remote state | High | High | High | Owner review | No identified semantic collision at 32px. |
| `runshelf-p5` | RunShelf | stacked run records preserve metric, status and artifact | High | High | High | Owner review | The record stack must remain visible so the curve does not reduce the meaning to analytics. |
| `contentdeck-p5` | ContentDeck | subtitled media with an explicitly bounded practice segment | High | High | High | Owner review | A–B handles are clearest at 64px; subtitle and bounded bar remain distinct at 32px. |

At 16px the candidates are family/key-color indicators. At 32px each primary instrument remains distinct. Detailed action/result cues are judged at 64px. These limits are stated rather than treating small decorative detail as successful semantic communication.

## Owner decision

Record selection, rejection or revision with the P5 candidate ID. No production repository changes occur in this review step.
