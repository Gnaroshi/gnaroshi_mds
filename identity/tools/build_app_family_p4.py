#!/usr/bin/env python3
"""Build deterministic 64x64 P4 pixel app-family review masters."""

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path

from PIL import Image, ImageDraw


GRID = 64
EXPORT = 2048

BG = "#111923"
SURFACE = "#1B2633"
FRAME = "#344454"
OUTLINE = "#071018"
INK = "#17202A"
WHITE = "#F4F7FA"
PAPER_DIM = "#CBD7E1"

ORANGE = "#E88945"
ORANGE_HI = "#F5B461"
ORANGE_DARK = "#9D4824"
EAR_INNER = "#26384A"
CYAN = "#57DDEA"
CYAN_DARK = "#168A9A"

LAVENDER = "#B8A7F3"
LAVENDER_DARK = "#6F5FA9"
MINT = "#8FD9C0"
MINT_DARK = "#3FA68E"
SKY = "#82C7EE"
SKY_DARK = "#327FAF"
PEACH = "#F2B58D"
PEACH_DARK = "#B96F4E"
BUTTER = "#E9D27A"
BUTTER_DARK = "#A58B32"
CORAL = "#E9948E"
CORAL_DARK = "#A75454"
TEAL = "#3FA6A0"


def mirror(points: list[tuple[int, int]]) -> list[tuple[int, int]]:
    return [(GRID - 1 - x, y) for x, y in points]


def polygon(draw: ImageDraw.ImageDraw, points: list[tuple[int, int]], fill: str, *, outline: str = OUTLINE, width: int = 2) -> None:
    draw.polygon(points, fill=fill, outline=outline, width=width)


def rect(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], fill: str, *, outline: str = OUTLINE, width: int = 2, radius: int = 0) -> None:
    if radius:
        draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)
    else:
        draw.rectangle(box, fill=fill, outline=outline, width=width)


def line(draw: ImageDraw.ImageDraw, points: list[tuple[int, int]], fill: str, *, width: int = 2) -> None:
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


def identity_band(draw: ImageDraw.ImageDraw, *, y_offset: int = 0) -> None:
    left_ear = [(7, 24 + y_offset), (7, 9 + y_offset), (10, 5 + y_offset), (24, 17 + y_offset), (22, 25 + y_offset), (14, 20 + y_offset)]
    polygon(draw, left_ear, ORANGE)
    polygon(draw, mirror(left_ear), ORANGE)

    left_inner = [(10, 17 + y_offset), (10, 10 + y_offset), (12, 9 + y_offset), (20, 17 + y_offset), (18, 21 + y_offset), (14, 17 + y_offset)]
    polygon(draw, left_inner, EAR_INNER, width=1)
    polygon(draw, mirror(left_inner), EAR_INNER, width=1)
    line(draw, [(9, 10 + y_offset), (12, 8 + y_offset), (22, 17 + y_offset)], ORANGE_HI, width=1)
    line(draw, mirror([(9, 10 + y_offset), (12, 8 + y_offset), (22, 17 + y_offset)]), ORANGE_HI, width=1)

    left_brow = [(13, 21 + y_offset), (22, 16 + y_offset), (30, 19 + y_offset), (29, 24 + y_offset), (22, 21 + y_offset), (16, 26 + y_offset)]
    polygon(draw, left_brow, ORANGE_DARK)
    polygon(draw, mirror(left_brow), ORANGE_DARK)

    outer_socket = [(13, 23 + y_offset), (18, 19 + y_offset), (24, 21 + y_offset), (22, 27 + y_offset), (17, 27 + y_offset)]
    inner_socket = [(24, 21 + y_offset), (27, 18 + y_offset), (31, 20 + y_offset), (30, 24 + y_offset), (27, 24 + y_offset)]
    polygon(draw, outer_socket, OUTLINE, width=1)
    polygon(draw, mirror(outer_socket), OUTLINE, width=1)
    polygon(draw, inner_socket, OUTLINE, width=1)
    polygon(draw, mirror(inner_socket), OUTLINE, width=1)

    draw.polygon([(16, 23 + y_offset), (19, 21 + y_offset), (22, 22 + y_offset), (21, 25 + y_offset), (18, 26 + y_offset)], fill=CYAN)
    draw.polygon(mirror([(16, 23 + y_offset), (19, 21 + y_offset), (22, 22 + y_offset), (21, 25 + y_offset), (18, 26 + y_offset)]), fill=CYAN)
    draw.polygon([(26, 21 + y_offset), (28, 20 + y_offset), (30, 21 + y_offset), (29, 23 + y_offset), (27, 23 + y_offset)], fill=CYAN)
    draw.polygon(mirror([(26, 21 + y_offset), (28, 20 + y_offset), (30, 21 + y_offset), (29, 23 + y_offset), (27, 23 + y_offset)]), fill=CYAN)
    draw.point((19, 22 + y_offset), fill=WHITE)
    draw.point((44, 22 + y_offset), fill=WHITE)


def draw_main(draw: ImageDraw.ImageDraw) -> None:
    identity_band(draw, y_offset=16)


def draw_studio(draw: ImageDraw.ImageDraw) -> None:
    line(draw, [(10, 36), (18, 36), (22, 40)], MINT, width=3)
    line(draw, [(10, 44), (18, 44), (22, 41)], MINT, width=3)
    rect(draw, (7, 33, 12, 38), LAVENDER, radius=1)
    rect(draw, (7, 41, 12, 46), LAVENDER, radius=1)
    rect(draw, (20, 29, 44, 55), LAVENDER_DARK, radius=4)
    rect(draw, (23, 32, 41, 52), LAVENDER, radius=2)
    polygon(draw, [(31, 33), (36, 36), (37, 43), (32, 50), (27, 43), (28, 36)], MINT)
    line(draw, [(32, 36), (32, 46)], MINT_DARK, width=2)
    draw.rectangle((31, 40, 33, 42), fill=INK)
    line(draw, [(44, 41), (51, 41), (55, 36)], MINT, width=3)
    line(draw, [(51, 41), (57, 41)], MINT, width=3)
    line(draw, [(51, 41), (55, 47)], MINT, width=3)
    polygon(draw, [(54, 34), (59, 36), (55, 39)], MINT, width=1)
    polygon(draw, [(56, 38), (61, 41), (56, 44)], MINT, width=1)
    polygon(draw, [(54, 45), (59, 47), (55, 50)], MINT, width=1)


def draw_paper(draw: ImageDraw.ImageDraw, x: int, y: int, *, fill: str = WHITE) -> None:
    rect(draw, (x, y, x + 10, y + 13), fill, radius=1)
    polygon(draw, [(x + 6, y), (x + 10, y), (x + 10, y + 4)], PAPER_DIM, width=1)
    line(draw, [(x + 2, y + 6), (x + 7, y + 6)], SKY_DARK, width=1)
    line(draw, [(x + 2, y + 9), (x + 8, y + 9)], SKY_DARK, width=1)


def draw_paperflow(draw: ImageDraw.ImageDraw) -> None:
    draw_paper(draw, 7, 34)
    draw_paper(draw, 12, 28)
    line(draw, [(18, 41), (26, 41)], SKY, width=3)
    polygon(draw, [(23, 29), (41, 29), (38, 40), (34, 45), (30, 45), (26, 40)], MINT)
    polygon(draw, [(28, 33), (36, 33), (34, 39), (32, 42), (30, 39)], BG, width=1)
    line(draw, [(38, 41), (43, 41)], SKY, width=3)
    rect(draw, (42, 31, 57, 54), SKY_DARK, radius=2)
    for top in (34, 41, 48):
        rect(draw, (45, top, 54, top + 4), SKY, radius=1, width=1)
        draw.rectangle((47, top + 1, 51, top + 2), fill=WHITE)
    line(draw, [(29, 36), (31, 38), (35, 34)], WHITE, width=2)


def draw_arxiv(draw: ImageDraw.ImageDraw) -> None:
    draw.ellipse((15, 27, 49, 61), fill=SKY_DARK, outline=OUTLINE, width=2)
    draw.ellipse((20, 32, 44, 56), outline=SKY, width=1)
    line(draw, [(32, 29), (32, 58)], SKY, width=1)
    line(draw, [(17, 44), (47, 44)], SKY, width=1)
    polygon(draw, [(32, 44), (47, 35), (44, 53)], PEACH, width=1)
    rect(draw, (10, 31, 18, 41), WHITE, radius=1, width=1)
    rect(draw, (45, 29, 53, 39), WHITE, radius=1, width=1)
    rect(draw, (28, 48, 37, 59), WHITE, radius=1)
    line(draw, [(12, 35), (16, 35)], SKY_DARK, width=1)
    line(draw, [(47, 33), (51, 33)], SKY_DARK, width=1)
    line(draw, [(30, 52), (35, 52)], PEACH_DARK, width=1)
    draw.rectangle((39, 46, 41, 48), fill=ORANGE_HI)
    draw.point((42, 44), fill=ORANGE_HI)


def draw_fan(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int]) -> None:
    draw.ellipse(box, fill=SURFACE, outline=OUTLINE, width=2)
    x0, y0, x1, y1 = box
    cx, cy = (x0 + x1) // 2, (y0 + y1) // 2
    draw.rectangle((cx - 1, y0 + 3, cx + 1, cy - 2), fill=CORAL_DARK)
    draw.rectangle((cx - 1, cy + 2, cx + 1, y1 - 3), fill=CORAL_DARK)
    draw.rectangle((x0 + 3, cy - 1, cx - 2, cy + 1), fill=CORAL_DARK)
    draw.rectangle((cx + 2, cy - 1, x1 - 3, cy + 1), fill=CORAL_DARK)
    draw.ellipse((cx - 2, cy - 2, cx + 2, cy + 2), fill=CORAL, outline=OUTLINE, width=1)


def draw_gpu(draw: ImageDraw.ImageDraw) -> None:
    rect(draw, (6, 29, 57, 54), CORAL_DARK, radius=3)
    rect(draw, (8, 31, 55, 52), SURFACE, radius=2, width=1)
    draw_fan(draw, (10, 34, 25, 49))
    draw_fan(draw, (39, 34, 54, 49))
    for y, length in ((35, 8), (40, 6), (45, 9)):
        draw.rectangle((28, y, 28 + length, y + 2), fill=TEAL)
    line(draw, [(28, 50), (31, 47), (34, 51), (37, 47)], CYAN, width=1)
    draw.rectangle((15, 54, 48, 57), fill=OUTLINE)
    for x in range(18, 47, 4):
        draw.rectangle((x, 55, x + 2, 57), fill=BUTTER)
    rect(draw, (49, 26, 53, 30), TEAL, radius=1, width=1)
    rect(draw, (55, 28, 59, 32), TEAL, radius=1, width=1)
    line(draw, [(51, 30), (51, 32), (56, 32)], CYAN, width=1)


def draw_flask(draw: ImageDraw.ImageDraw) -> None:
    polygon(draw, [(15, 42), (20, 42), (20, 46), (24, 53), (11, 53), (15, 46)], MINT, width=1)
    draw.rectangle((16, 43, 19, 47), fill=BG)
    draw.rectangle((14, 50, 21, 52), fill=BUTTER)


def draw_runshelf(draw: ImageDraw.ImageDraw) -> None:
    rect(draw, (13, 28, 51, 35), BUTTER_DARK, radius=2)
    rect(draw, (11, 32, 53, 41), BUTTER, radius=2)
    line(draw, [(45, 35), (47, 37), (51, 33)], TEAL, width=2)
    rect(draw, (7, 37, 57, 56), TEAL, radius=3)
    rect(draw, (10, 39, 54, 53), BUTTER, radius=2, width=1)
    draw_flask(draw)
    line(draw, [(25, 50), (30, 46), (34, 48), (39, 43), (44, 45)], TEAL, width=2)
    for x, y in ((25, 50), (30, 46), (34, 48), (39, 43), (44, 45)):
        draw.rectangle((x - 1, y - 1, x + 1, y + 1), fill=TEAL)
    polygon(draw, [(46, 43), (51, 41), (54, 44), (54, 50), (49, 52), (46, 49)], TEAL, width=1)
    line(draw, [(49, 44), (52, 45), (52, 49)], BUTTER, width=1)


def draw_contentdeck(draw: ImageDraw.ImageDraw) -> None:
    rect(draw, (7, 28, 57, 56), PEACH_DARK, radius=3)
    rect(draw, (10, 31, 54, 53), SURFACE, radius=2, width=1)
    draw.rectangle((12, 33, 52, 42), fill=SKY_DARK)
    polygon(draw, [(29, 34), (29, 41), (36, 37)], PEACH, width=1)
    rect(draw, (12, 41, 52, 50), PEACH, radius=1, width=1)
    draw.rectangle((16, 44, 48, 45), fill=INK)
    draw.rectangle((18, 47, 45, 48), fill=INK)
    line(draw, [(17, 53), (47, 53)], LAVENDER, width=2)
    draw.rectangle((20, 50, 22, 56), fill=LAVENDER)
    draw.rectangle((42, 50, 44, 56), fill=LAVENDER)
    line(draw, [(42, 57), (38, 59), (27, 59), (22, 56)], LAVENDER, width=2)
    polygon(draw, [(21, 54), (25, 56), (22, 59)], LAVENDER, width=1)


BUILDERS = {
    "gnaroshi-main-p4": draw_main,
    "studio-p4": draw_studio,
    "paperflow-p4": draw_paperflow,
    "arxiv-discovery-p4": draw_arxiv,
    "tr-gpu-monitor-p4": draw_gpu,
    "runshelf-p4": draw_runshelf,
    "contentdeck-p4": draw_contentdeck,
}


def build(candidate_id: str) -> Image.Image:
    image, draw = base_tile()
    if candidate_id == "gnaroshi-main-p4":
        draw_main(draw)
    else:
        identity_band(draw)
        BUILDERS[candidate_id](draw)
    return image


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    source_dir = args.output_dir / "p4-64"
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
