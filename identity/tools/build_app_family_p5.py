#!/usr/bin/env python3
"""Build deterministic 64x64 P5 hero-instrument app icon review masters."""

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path

from PIL import Image, ImageDraw


GRID = 64
EXPORT = 2048

BG = "#111923"
SURFACE = "#1B2633"
SURFACE_HI = "#26384A"
FRAME = "#344454"
OUTLINE = "#071018"
WHITE = "#F4F7FA"
PAPER_DIM = "#CBD7E1"

ORANGE = "#E88945"
ORANGE_HI = "#F5B461"
ORANGE_DARK = "#9D4824"
EAR_INNER = "#26384A"
CYAN = "#57DDEA"
TEAL = "#3FA6A0"
TEAL_DARK = "#23756F"

LAVENDER = "#B8A7F3"
LAVENDER_DARK = "#6F5FA9"
MINT = "#8FD9C0"
MINT_DARK = "#3F947D"
SKY = "#82C7EE"
SKY_DARK = "#327FAF"
PEACH = "#F2B58D"
PEACH_DARK = "#B96F4E"
BUTTER = "#E9D27A"
BUTTER_DARK = "#A58B32"
CORAL = "#E9948E"
CORAL_DARK = "#A75454"


def mirror(points: list[tuple[int, int]]) -> list[tuple[int, int]]:
    return [(GRID - 1 - x, y) for x, y in points]


def polygon(
    draw: ImageDraw.ImageDraw,
    points: list[tuple[int, int]],
    fill: str,
    *,
    outline: str = OUTLINE,
    width: int = 2,
) -> None:
    draw.polygon(points, fill=fill, outline=outline, width=width)


def rect(
    draw: ImageDraw.ImageDraw,
    box: tuple[int, int, int, int],
    fill: str,
    *,
    outline: str = OUTLINE,
    width: int = 2,
    radius: int = 0,
) -> None:
    if radius:
        draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)
    else:
        draw.rectangle(box, fill=fill, outline=outline, width=width)


def line(
    draw: ImageDraw.ImageDraw,
    points: list[tuple[int, int]],
    fill: str,
    *,
    width: int = 2,
) -> None:
    draw.line(points, fill=fill, width=width, joint="curve")


def base_tile() -> tuple[Image.Image, ImageDraw.ImageDraw]:
    image = Image.new("RGB", (GRID, GRID), BG)
    draw = ImageDraw.Draw(image)
    outer = [(6, 1), (57, 1), (62, 6), (62, 57), (57, 62), (6, 62), (1, 57), (1, 6)]
    inner = [(7, 3), (56, 3), (60, 7), (60, 56), (56, 60), (7, 60), (3, 56), (3, 7)]
    draw.polygon(outer, fill=FRAME)
    draw.polygon(inner, fill=BG)
    draw.line([(8, 5), (55, 5)], fill=SURFACE, width=2)
    return image, draw


def identity_canopy(draw: ImageDraw.ImageDraw, *, y_offset: int = 0) -> None:
    """Draw one shared ear-and-visor mark; no floating facial fragments."""
    left_ear = [
        (7, 24 + y_offset),
        (7, 9 + y_offset),
        (10, 5 + y_offset),
        (24, 17 + y_offset),
        (22, 25 + y_offset),
        (14, 20 + y_offset),
    ]
    polygon(draw, left_ear, ORANGE)
    polygon(draw, mirror(left_ear), ORANGE)

    left_inner = [
        (10, 17 + y_offset),
        (10, 10 + y_offset),
        (12, 9 + y_offset),
        (20, 17 + y_offset),
        (18, 21 + y_offset),
        (14, 17 + y_offset),
    ]
    polygon(draw, left_inner, EAR_INNER, width=1)
    polygon(draw, mirror(left_inner), EAR_INNER, width=1)
    line(draw, [(9, 10 + y_offset), (12, 8 + y_offset), (22, 17 + y_offset)], ORANGE_HI, width=1)
    line(draw, mirror([(9, 10 + y_offset), (12, 8 + y_offset), (22, 17 + y_offset)]), ORANGE_HI, width=1)

    visor = [
        (13, 20 + y_offset),
        (21, 16 + y_offset),
        (29, 18 + y_offset),
        (34, 18 + y_offset),
        (42, 16 + y_offset),
        (50, 20 + y_offset),
        (47, 27 + y_offset),
        (16, 27 + y_offset),
    ]
    polygon(draw, visor, SURFACE_HI, width=2)
    line(draw, [(15, 20 + y_offset), (22, 17 + y_offset), (29, 19 + y_offset)], ORANGE_DARK, width=2)
    line(draw, mirror([(15, 20 + y_offset), (22, 17 + y_offset), (29, 19 + y_offset)]), ORANGE_DARK, width=2)

    eye_slits = (
        [(16, 23 + y_offset), (22, 20 + y_offset)],
        [(25, 22 + y_offset), (30, 20 + y_offset)],
    )
    for eye in eye_slits:
        line(draw, eye, CYAN, width=1)
        line(draw, mirror(eye), CYAN, width=1)


def role_plate(draw: ImageDraw.ImageDraw, accent: str, accent_dark: str) -> None:
    """Draw the same separated pro-instrument container for every app."""
    rect(draw, (5, 25, 58, 59), OUTLINE, radius=5, width=1)
    rect(draw, (7, 26, 56, 57), accent_dark, radius=4, width=1)
    rect(draw, (9, 28, 54, 55), accent, radius=3, width=1)
    rect(draw, (11, 30, 52, 53), SURFACE, radius=2, width=2)
    draw.line([(13, 31), (50, 31)], fill=SURFACE_HI, width=1)
    draw.rectangle((13, 53, 50, 55), fill=accent_dark)


def draw_main(draw: ImageDraw.ImageDraw) -> None:
    identity_canopy(draw, y_offset=15)


def draw_studio(draw: ImageDraw.ImageDraw) -> None:
    # Editorial console: source tabs -> manuscript + pen -> publish output.
    for top in (34, 40, 46):
        rect(draw, (13, top, 17, top + 3), LAVENDER, radius=1, width=1)
    line(draw, [(17, 35), (20, 38)], TEAL, width=1)
    line(draw, [(17, 41), (20, 41)], TEAL, width=1)
    line(draw, [(17, 47), (20, 44)], TEAL, width=1)
    rect(draw, (19, 33, 43, 50), WHITE, radius=2)
    line(draw, [(31, 35), (31, 48)], PAPER_DIM, width=1)
    line(draw, [(22, 37), (28, 37)], LAVENDER_DARK, width=1)
    line(draw, [(34, 37), (40, 37)], LAVENDER_DARK, width=1)
    line(draw, [(22, 40), (28, 40)], LAVENDER_DARK, width=1)
    polygon(draw, [(26, 47), (34, 35), (37, 38), (29, 49)], TEAL, width=1)
    draw.rectangle((27, 47, 29, 49), fill=TEAL_DARK)
    line(draw, [(43, 41), (48, 41)], TEAL, width=2)
    polygon(draw, [(47, 37), (51, 41), (47, 45)], LAVENDER, width=1)


def draw_paperflow(draw: ImageDraw.ImageDraw) -> None:
    # Guarded sorter: one paper enters and becomes ordered indexed slots.
    rect(draw, (13, 34, 22, 46), WHITE, radius=1)
    polygon(draw, [(18, 34), (22, 34), (22, 38)], PAPER_DIM, width=1)
    line(draw, [(15, 40), (20, 40)], MINT_DARK, width=1)
    line(draw, [(18, 45), (25, 45)], TEAL, width=2)
    polygon(draw, [(23, 34), (38, 34), (36, 42), (32, 47), (29, 47), (25, 42)], MINT, width=2)
    polygon(draw, [(28, 38), (34, 38), (32, 43), (30, 45), (28, 42)], SURFACE, width=1)
    line(draw, [(28, 40), (30, 42), (34, 38)], WHITE, width=1)
    line(draw, [(36, 45), (40, 45)], TEAL, width=2)
    rect(draw, (39, 33, 50, 49), MINT_DARK, radius=2)
    for top in (35, 40, 45):
        rect(draw, (42, top, 48, top + 3), WHITE, radius=1, width=1)


def draw_arxiv(draw: ImageDraw.ImageDraw) -> None:
    # Research radar: paper blips cross a sweep and one result is acquired.
    draw.ellipse((17, 31, 47, 52), fill=SKY_DARK, outline=OUTLINE, width=2)
    draw.arc((21, 34, 43, 50), 180, 345, fill=SKY, width=1)
    line(draw, [(32, 33), (32, 51)], SKY, width=1)
    line(draw, [(19, 43), (45, 43)], SKY, width=1)
    polygon(draw, [(32, 43), (45, 35), (43, 49)], SKY, width=1)
    rect(draw, (14, 35, 19, 41), WHITE, radius=1, width=1)
    rect(draw, (43, 33, 49, 40), WHITE, radius=1, width=1)
    rect(draw, (36, 44, 43, 51), WHITE, radius=1)
    draw.rectangle((38, 46, 41, 47), fill=TEAL)
    draw.rectangle((39, 42, 41, 44), fill=CYAN)


def draw_fan(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int]) -> None:
    draw.ellipse(box, fill=SURFACE_HI, outline=OUTLINE, width=2)
    x0, y0, x1, y1 = box
    cx, cy = (x0 + x1) // 2, (y0 + y1) // 2
    draw.rectangle((cx - 1, y0 + 3, cx + 1, cy - 2), fill=CORAL_DARK)
    draw.rectangle((cx - 1, cy + 2, cx + 1, y1 - 3), fill=CORAL_DARK)
    draw.rectangle((x0 + 3, cy - 1, cx - 2, cy + 1), fill=CORAL_DARK)
    draw.rectangle((cx + 2, cy - 1, x1 - 3, cy + 1), fill=CORAL_DARK)
    draw.rectangle((cx - 1, cy - 1, cx + 1, cy + 1), fill=CORAL)


def draw_gpu(draw: ImageDraw.ImageDraw) -> None:
    # Hardware instrument: dual-fan GPU with live pulse and remote state.
    rect(draw, (12, 33, 51, 49), CORAL_DARK, radius=2)
    rect(draw, (14, 34, 49, 47), SURFACE, radius=1, width=1)
    draw_fan(draw, (15, 35, 27, 47))
    draw_fan(draw, (36, 35, 48, 47))
    line(draw, [(27, 43), (30, 39), (33, 45), (36, 40)], TEAL, width=1)
    draw.rectangle((20, 49, 44, 51), fill=OUTLINE)
    for x in range(22, 43, 4):
        draw.rectangle((x, 50, x + 2, 51), fill=CORAL)
    rect(draw, (46, 31, 50, 34), TEAL, radius=1, width=1)
    line(draw, [(48, 34), (48, 36), (51, 36)], CYAN, width=1)


def draw_runshelf(draw: ImageDraw.ImageDraw) -> None:
    # Indexed archive: stacked run records retain metric, status and artifact.
    rect(draw, (17, 32, 45, 39), BUTTER_DARK, radius=2)
    rect(draw, (15, 35, 47, 43), BUTTER, radius=2)
    rect(draw, (13, 38, 49, 50), WHITE, radius=2)
    draw.rectangle((16, 40, 20, 48), fill=BUTTER_DARK)
    for top in (41, 44, 47):
        draw.rectangle((17, top, 19, top + 1), fill=BUTTER)
    line(draw, [(23, 47), (27, 43), (31, 45), (36, 40), (41, 42)], TEAL, width=2)
    for x, y in ((23, 47), (27, 43), (31, 45), (36, 40), (41, 42)):
        draw.point((x, y), fill=CYAN)
    draw.ellipse((42, 39, 47, 44), fill=TEAL, outline=OUTLINE, width=1)
    rect(draw, (40, 46, 47, 49), BUTTER, radius=1, width=1)
    line(draw, [(11, 51), (51, 51)], BUTTER_DARK, width=2)


def draw_contentdeck(draw: ImageDraw.ImageDraw) -> None:
    # Study player: media, subtitle and bounded A-B loop in one instrument.
    rect(draw, (13, 32, 50, 49), PEACH_DARK, radius=2)
    rect(draw, (15, 34, 48, 47), SURFACE_HI, radius=1, width=1)
    draw.rectangle((17, 35, 46, 40), fill=SKY_DARK)
    polygon(draw, [(29, 35), (29, 40), (34, 37)], PEACH, width=1)
    rect(draw, (17, 40, 46, 46), WHITE, radius=1, width=1)
    draw.rectangle((20, 42, 43, 43), fill=PEACH_DARK)
    draw.rectangle((23, 45, 40, 45), fill=SURFACE)
    line(draw, [(18, 50), (45, 50)], TEAL, width=2)
    draw.rectangle((20, 47, 22, 52), fill=TEAL)
    draw.rectangle((42, 47, 44, 52), fill=TEAL)
    polygon(draw, [(20, 49), (24, 51), (21, 53)], TEAL, width=1)


BUILDERS = {
    "gnaroshi-main-p5": (draw_main, None, None),
    "studio-p5": (draw_studio, LAVENDER, LAVENDER_DARK),
    "paperflow-p5": (draw_paperflow, MINT, MINT_DARK),
    "arxiv-discovery-p5": (draw_arxiv, SKY, SKY_DARK),
    "tr-gpu-monitor-p5": (draw_gpu, CORAL, CORAL_DARK),
    "runshelf-p5": (draw_runshelf, BUTTER, BUTTER_DARK),
    "contentdeck-p5": (draw_contentdeck, PEACH, PEACH_DARK),
}


def build(candidate_id: str) -> Image.Image:
    image, draw = base_tile()
    builder, accent, accent_dark = BUILDERS[candidate_id]
    if candidate_id == "gnaroshi-main-p5":
        builder(draw)
    else:
        identity_canopy(draw)
        role_plate(draw, accent, accent_dark)
        builder(draw)
    return image


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    source_dir = args.output_dir / "p5-64"
    source_dir.mkdir(parents=True, exist_ok=True)
    args.output_dir.mkdir(parents=True, exist_ok=True)

    for candidate_id in BUILDERS:
        source = build(candidate_id)
        source_path = source_dir / f"{candidate_id}.png"
        export_path = args.output_dir / f"{candidate_id}.png"
        source.save(source_path, format="PNG", optimize=True)
        source.resize((EXPORT, EXPORT), Image.Resampling.NEAREST).save(export_path, format="PNG", optimize=True)
        digest = hashlib.sha256(source_path.read_bytes()).hexdigest()
        print(f"{candidate_id}: {digest}")


if __name__ == "__main__":
    main()
