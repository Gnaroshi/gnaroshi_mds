#!/usr/bin/env python3
"""Export the owner-approved P5 family as canonical 2048px PNG masters."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

from PIL import Image

from build_app_family_p5 import BUILDERS, EXPORT, build


SELECTED_AT = "2026-07-14"

APP_EXPORTS = {
    "gnaroshi-main-p5": {
        "id": "gnaroshi-main-v1",
        "file": "gnaroshi-main-v1.png",
        "product": "gnaroshi.dev",
        "targets": ["web identity", "favicon", "social preview identity element"],
    },
    "studio-p5": {
        "id": "gnaroshi-studio-v1",
        "file": "gnaroshi-studio-v1.png",
        "product": "Gnaroshi Studio",
        "targets": ["macOS Tauri application", "Studio managed-app card"],
    },
    "paperflow-p5": {
        "id": "paperflow-v1",
        "file": "paperflow-v1.png",
        "product": "PaperFlow",
        "targets": ["macOS Swift application", "Studio managed-app card"],
    },
    "arxiv-discovery-p5": {
        "id": "arxiv-discovery-v1",
        "file": "arxiv-discovery-v1.png",
        "product": "Arxiv Discovery",
        "targets": ["web favicon", "Studio managed-app card"],
    },
    "tr-gpu-monitor-p5": {
        "id": "tr-gpu-monitor-v1",
        "file": "tr-gpu-monitor-v1.png",
        "product": "TR GPU Monitor",
        "targets": ["macOS Swift application", "Studio managed-app card"],
    },
    "runshelf-p5": {
        "id": "runshelf-v1",
        "file": "runshelf-v1.png",
        "product": "RunShelf",
        "targets": ["macOS Swift application", "Studio managed-app card"],
    },
    "contentdeck-p5": {
        "id": "contentdeck-v1",
        "file": "contentdeck-v1.png",
        "product": "ContentDeck",
        "targets": ["macOS Electron application", "web favicon", "Studio managed-app card"],
    },
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)

    records = []
    for candidate_id, export in APP_EXPORTS.items():
        if candidate_id not in BUILDERS:
            raise ValueError(f"Unknown approved candidate: {candidate_id}")

        source = build(candidate_id)
        source_path = args.output_dir / f".{candidate_id}-source.png"
        source.save(source_path, format="PNG", optimize=True)
        source_sha = sha256(source_path)
        source_path.unlink()

        master_path = args.output_dir / export["file"]
        source.resize((EXPORT, EXPORT), Image.Resampling.NEAREST).save(
            master_path,
            format="PNG",
            optimize=True,
        )
        records.append(
            {
                "id": export["id"],
                "product": export["product"],
                "sourceCandidate": candidate_id,
                "sourceSize": [source.width, source.height],
                "sourceSha256": source_sha,
                "masterFile": export["file"],
                "masterSize": [EXPORT, EXPORT],
                "masterSha256": sha256(master_path),
                "exportedAt": SELECTED_AT,
                "targetPlatforms": export["targets"],
            }
        )

    metadata = {
        "schemaVersion": 1,
        "family": "gnaroshi-p5-hero-instrument",
        "selectedAt": SELECTED_AT,
        "ownerApproved": True,
        "rendering": "64px deterministic pixel source expanded to 2048px with nearest-neighbor resampling",
        "baseReference": "../gnaroshi-base-v1.png",
        "restrictions": [
            "Use only these owner-approved P5 candidates for production identity exports.",
            "Do not redraw, prompt-regenerate, smooth, blur, or interpolate the pixel masters.",
            "Do not use the full-color mascot as a menu-bar or functional toolbar icon.",
            "Keep application builds independent from network access to gnaroshi_mds.",
        ],
        "apps": records,
    }
    (args.output_dir / "metadata.json").write_text(
        json.dumps(metadata, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    print(f"Exported {len(records)} approved P5 masters to {args.output_dir}")


if __name__ == "__main__":
    main()
