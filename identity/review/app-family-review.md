# Gnaroshi application icon family review

Status: **owner selection required**. No P1 candidate is approved or selected by this document.

Pixel P1 is a single coordinated family: one fixed mascot template, one fixed role-glyph position, one canonical glyph per application and one application key color. The prior A/B and C/D rounds are superseded for active review because their mascot scale, lighting, frame and role-object density were not consistent enough and several symbols were ambiguous.

The exact approved base is recorded in [`../approved/metadata.json`](../approved/metadata.json). Review binaries are intentionally ignored and must not be promoted to application icon sets, Electron/Tauri assets, favicons, menu-bar assets, website media or package metadata without a separate owner decision.

## Review criteria

- Role clarity: identify the application role before reading its name.
- Base identity fidelity: recognize the same ears, four eyes, teeth, face and orange/teal family.
- 32px readability: both mascot and role glyph survive without blending together.
- Family consistency: mascot, frame, background, role anchor and pixel scale do not change between apps.
- Surface quality: boundary and key color remain legible on dark and light surfaces.

## Candidate record

| Candidate ID | Application | Role clarity | Base identity fidelity | 32px readability | Dark/light quality | Review status | Reason |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `studio-p1` | Gnaroshi Studio | High: document + pencil | High: fixed template | Medium-high | High | Owner review | Direct writing/publishing cue; no generic gear or dashboard. |
| `paperflow-p1` | PaperFlow | High: papers + one flow arrow | High: fixed template | Medium-high | High | Owner review | Shows organized paper movement without a Zotero or folder logo. |
| `arxiv-discovery-p1` | Arxiv Discovery | High: document + magnifier | High: fixed template | Medium-high | High | Owner review | Discovery cue is direct and does not use the arXiv logo. |
| `tr-gpu-monitor-p1` | TR GPU Monitor | High: GPU chip + pulse | High: fixed template | Medium-high | High | Owner review | Vendor-neutral telemetry cue; no server dashboard or terminal. |
| `runshelf-p1` | RunShelf | Medium: flat run cards + shelf + dot | High: fixed template | Medium-low | High | Owner review | The server-like draft was replaced, but the shelf meaning is still the weakest at 32px. |
| `contentdeck-p1` | ContentDeck | High: loop + play + subtitle | High: fixed template | Medium-high | High | Owner review | Playback, repetition and subtitles form one compact combined symbol. |

The 16px exports primarily preserve family color and silhouette; application-role recognition starts at 32px and is reliable at 64px. Some generated glyph fills still contain more shade steps than the two-step production rule permits. After owner selection, the chosen master needs deterministic 64×64 grid quantization, palette cleanup and optical 16/32px exports before production use.

## Owner decision

Review the P1 IDs together as a family. Record explicit selections, rejections or requested revisions by candidate ID. Selection still requires a later production-export change per application.
