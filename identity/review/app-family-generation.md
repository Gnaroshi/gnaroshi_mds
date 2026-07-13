# App identity family candidate generation

## Scope

Pixel P4 supersedes P3 for active owner review. P3 made each workflow more concrete, but review still found three structural problems: the raster scenes looked AI-generated, the partly hidden face looked accidental, and the mascot competed with the application role.

P4 changes the construction rather than asking an image model for another variation:

- every active source master is drawn directly on a deterministic `64×64` grid;
- one identical `ears + four cyan eyes` band is the only mascot fragment used by app variants;
- no nose, mouth, teeth, cheek, body or half-hidden face remains;
- the lower 60–75% is reserved for a small number of large, functional role shapes;
- the `2048×2048` review export is a nearest-neighbor copy of the 64px source.

P4 does not approve a candidate, alter a production icon or define platform exports. P1–P3 remain review history only.

## Exact identity reference

- approved base: `identity/approved/gnaroshi-base-v1.png`
- source candidate: `identity/candidates/07-cel-shaded.png`
- approved-base SHA-256: `2056b9e5cf7e3464aaf9c108849f0ec43ac1fbacd427ce73a6441e2619c380f6`
- verified relationship: approved base and retained source candidate are byte-identical

The approved raster remains the identity reference for ear shape, four-eye arrangement, teal/orange recognition and attitude. P4 deliberately extracts those features into a compact band; it does not regenerate the mascot from a prompt.

## Deterministic construction

- source tool: `identity/tools/build_app_family_p4.py`
- source directory: `identity/review/candidates/p4-64/`
- review exports: `identity/review/candidates/*.png`
- grid: actual `64×64` RGB PNG
- export: `2048×2048`, nearest-neighbor only
- common pixels: background, stepped frame, orange ears, inner ears, brows and four cyan eyes
- variable pixels: one role composition and its assigned pastel colors
- prohibited effects: anti-aliasing, gradients, blur, glow, soft shadows and sub-pixel strokes

Because the source is code-defined, rerunning the tool with the same Pillow behavior produces the same source bytes. The review builder rejects an export that is not an exact nearest-neighbor expansion of its corresponding 64px master.

## P4 role vocabulary

| Candidate ID | Product | Primary reading | Large functional shapes | Key colors |
| --- | --- | --- | --- | --- |
| `studio-p4` | Gnaroshi Studio | connected work enters an authoring/control hub and leaves through publish output | hub, pen nib, input/output nodes | lavender + mint |
| `paperflow-p4` | PaperFlow | papers pass through a safe sorter into an indexed library | paper stack, funnel/check, library drawers | mint + sky blue |
| `arxiv-discovery-p4` | Arxiv Discovery | a radar sweep finds incoming research papers | radar field, highlighted sweep, papers | sky blue + peach |
| `tr-gpu-monitor-p4` | TR GPU Monitor | a remote dual-fan GPU reports live telemetry | GPU card, metric bars/pulse, remote nodes | soft coral + teal |
| `runshelf-p4` | RunShelf | an experiment result becomes a stored run record | stacked records, experiment flask, metric/artifact trace | butter yellow + teal |
| `contentdeck-p4` | ContentDeck | subtitled media repeats one bounded study segment | media frame, subtitle block, loop boundary | peach + lavender |

## Source checksums

| Candidate ID | 64px source SHA-256 |
| --- | --- |
| `gnaroshi-main-p4` | `9fb7e6f18445c639dab97bc32877463562bb85a06bb379f3c2150ddf0e6aefb8` |
| `studio-p4` | `bde68273bcbe7cae84a678aa93fc3891901b2df8661e3a288659f114e8588a95` |
| `paperflow-p4` | `c15f9ae949a9e77841a4674a70de659f1e5b76e863c983ee8c9f8e3eaa08e84b` |
| `arxiv-discovery-p4` | `944a41c4a17fb65b5c498ed77b7f6adade32e826e2a803c1e0a1d49791507668` |
| `tr-gpu-monitor-p4` | `2fb719c394aafe8a0d1bd6617ef551bf3494d536b85d3b4daf7c5b8ea8af5b9c` |
| `runshelf-p4` | `74a9c14478bf7eb61012a0f7cae8195919636416c95931b3241f7437dc6d1921` |
| `contentdeck-p4` | `13aaad8925929e58cb0e488118c33f9d92720b9403379a80fe4e6b93a815f789` |

## Refresh review files

Candidate binaries and review PNGs remain under ignored `identity/review/` paths until owner selection.

```bash
python3 identity/tools/build_app_family_p4.py \
  --output-dir identity/review/candidates

python3 identity/tools/build_app_family_review.py \
  --candidate-dir identity/review/candidates \
  --output-dir identity/review
```

The review sheets show square, circular and approximate macOS squircle masks at 16/32/64/128/256px on light and dark surfaces. Production work remains blocked on explicit selection by candidate ID.
