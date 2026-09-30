# Gnaroshi application icon family review

2026-07-14 선택 기록. 6개 app role은 production에 사용한다. 함께 승인됐던 `gnaroshi-main-p5`는 현재 full-face 규칙에 맞지 않아 historical asset으로 보존하며 웹·global 대표 identity에 사용하지 않는다.

P4에서 지적된 floating eye, mascot/role 경계 부족, app별 scale·perspective 불일치를 P5의 공통 canopy와 bordered role plate로 수정했다. 현재 구성 규칙은 [app-icons](../../guides/app-icons.md), byte provenance는 [metadata](../approved/apps/metadata.json)에 있다.

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

The owner approved `gnaroshi-main-p5`, `studio-p5`, `paperflow-p5`, `arxiv-discovery-p5`, `tr-gpu-monitor-p5`, `runshelf-p5` and `contentdeck-p5` on 2026-07-14. 현재 사용 범위는 [identity 목록](../README.md)을 따른다. 다른 후보로의 production 교체는 새 owner 결정과 metadata 갱신이 필요하다.
