# Gnaroshi application icon family review

Status: **owner approved on 2026-07-14**. P5 is the selected production family.

P5 is one `hero-instrument` family. Every app uses the same ear-and-visor canopy, black separation outline, colored role rim, dark instrument surface, front-facing perspective and depth. The role instrument changes; the visual system does not.

The exact approved base is recorded in [`../approved/metadata.json`](../approved/metadata.json). The selected P5 masters and checksums are recorded in [`../approved/apps/metadata.json`](../approved/apps/metadata.json). Review binaries remain ignored; production repositories use only the promoted masters.

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
| `studio-p5` | Gnaroshi Studio | manuscript authoring with multiple inputs and one publish output | High | High | High | Approved | At 16px only the page/pen mass remains; coordination becomes explicit at 32–64px. |
| `paperflow-p5` | PaperFlow | a paper passes through a guarded sorter into indexed slots | High | High | High | Approved | The small check/sorter interior is secondary; paper and output slots carry the 32px reading. |
| `arxiv-discovery-p5` | Arxiv Discovery | a radar sweep acquires incoming paper targets | High | High | High | Approved | Ensure the white targets continue to read as papers rather than generic radar blips. |
| `tr-gpu-monitor-p5` | TR GPU Monitor | dual-fan GPU with live telemetry and remote state | High | High | High | Approved | No identified semantic collision at 32px. |
| `runshelf-p5` | RunShelf | stacked run records preserve metric, status and artifact | High | High | High | Approved | The record stack must remain visible so the curve does not reduce the meaning to analytics. |
| `contentdeck-p5` | ContentDeck | subtitled media with an explicitly bounded practice segment | High | High | High | Approved | A–B handles are clearest at 64px; subtitle and bounded bar remain distinct at 32px. |

At 16px the candidates are family/key-color indicators. At 32px each primary instrument remains distinct. Detailed action/result cues are judged at 64px. These limits are stated rather than treating small decorative detail as successful semantic communication.

## Owner decision

The owner approved `gnaroshi-main-p5`, `studio-p5`, `paperflow-p5`, `arxiv-discovery-p5`, `tr-gpu-monitor-p5`, `runshelf-p5` and `contentdeck-p5` on 2026-07-14. No alternative candidate may replace these production sources without a new owner decision and metadata update.
