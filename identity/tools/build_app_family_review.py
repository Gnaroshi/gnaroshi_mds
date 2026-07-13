#!/usr/bin/env python3
"""Normalize P2 app-family candidates and build non-production review sheets."""

from __future__ import annotations

import argparse
import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


MASTER_SIZE = 2048
SMALL_SIZES = (16, 32, 64, 128, 256)
MAIN_REFERENCE = ("gnaroshi-main-p2", "Gnaroshi main/default")
APPS = (
    ("studio", "Gnaroshi Studio"),
    ("paperflow", "PaperFlow"),
    ("arxiv-discovery", "Arxiv Discovery"),
    ("tr-gpu-monitor", "TR GPU Monitor"),
    ("runshelf", "RunShelf"),
    ("contentdeck", "ContentDeck"),
)
CANDIDATES = tuple(
    (f"{slug}-p2{variant}", app, variant.upper())
    for slug, app in APPS
    for variant in ("a", "b")
)

DARK = "#111923"
DARK_PANEL = "#1B2633"
LIGHT = "#F4F7FA"
LIGHT_PANEL = "#E6ECF2"
INK = "#17202A"
PAPER = "#F4F7FA"
MUTED_DARK = "#AEBBC8"
MUTED_LIGHT = "#566575"
STROKE_DARK = "#344454"
STROKE_LIGHT = "#CDD6DF"


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    names = (
        "/System/Library/Fonts/SFNS.ttf",
        "/System/Library/Fonts/Helvetica.ttc",
        "/Library/Fonts/Arial Bold.ttf" if bold else "/Library/Fonts/Arial.ttf",
    )
    for name in names:
        try:
            return ImageFont.truetype(name, size=size, index=1 if bold and name.endswith(".ttc") else 0)
        except (OSError, ValueError):
            continue
    return ImageFont.load_default()


def normalize(candidate_dir: Path) -> dict[str, Image.Image]:
    masters: dict[str, Image.Image] = {}
    required = (MAIN_REFERENCE[0],) + tuple(candidate_id for candidate_id, _, _ in CANDIDATES)
    for candidate_id in required:
        path = candidate_dir / f"{candidate_id}.png"
        if not path.is_file():
            raise FileNotFoundError(f"missing candidate: {path}")
        with Image.open(path) as source:
            if source.width != source.height:
                raise ValueError(f"candidate must be square: {path} is {source.size}")
            image = source.convert("RGB")
        if image.size != (MASTER_SIZE, MASTER_SIZE):
            image = image.resize((MASTER_SIZE, MASTER_SIZE), Image.Resampling.NEAREST)
            image.save(path, format="PNG", optimize=True)
        masters[candidate_id] = image
    return masters


def mask(size: int, shape: str) -> Image.Image:
    result = Image.new("L", (size, size), 0)
    draw = ImageDraw.Draw(result)
    if shape == "circle":
        draw.ellipse((0, 0, size - 1, size - 1), fill=255)
    elif shape == "squircle":
        center = (size - 1) / 2
        radius = center
        exponent = 5.0
        points: list[tuple[float, float]] = []
        for step in range(361):
            angle = math.tau * step / 360
            cosine = math.cos(angle)
            sine = math.sin(angle)
            x = center + radius * math.copysign(abs(cosine) ** (2 / exponent), cosine)
            y = center + radius * math.copysign(abs(sine) ** (2 / exponent), sine)
            points.append((x, y))
        draw.polygon(points, fill=255)
    elif shape == "square":
        draw.rectangle((0, 0, size - 1, size - 1), fill=255)
    else:
        raise ValueError(f"unknown mask shape: {shape}")
    return result


def icon(image: Image.Image, size: int, shape: str = "squircle") -> Image.Image:
    resized = image.resize((size, size), Image.Resampling.NEAREST)
    result = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    result.paste(resized, (0, 0), mask(size, shape))
    return result


def label(draw: ImageDraw.ImageDraw, xy: tuple[int, int], text: str, *, size: int, fill: str, bold: bool = False) -> None:
    draw.text(xy, text, font=font(size, bold), fill=fill)


def build_contact_sheet(masters: dict[str, Image.Image], output: Path) -> None:
    width, row_height = 1800, 300
    height = 230 + len(APPS) * row_height + 50
    canvas = Image.new("RGBA", (width, height), DARK)
    draw = ImageDraw.Draw(canvas)
    label(draw, (50, 28), "Gnaroshi app icon family — pixel P2", size=38, fill=PAPER, bold=True)
    label(draw, (51, 76), "Centered main · A: vertical role panel · B: role-first emblem", size=19, fill=MUTED_DARK)

    canvas.alpha_composite(icon(masters[MAIN_REFERENCE[0]], 132), (50, 104))
    label(draw, (205, 130), MAIN_REFERENCE[1], size=23, fill=PAPER, bold=True)
    label(draw, (205, 166), "Centered on both axes · no application role", size=17, fill=MUTED_DARK)
    label(draw, (1015, 135), "A", size=28, fill=PAPER, bold=True)
    label(draw, (1060, 141), "centered mascot + lower role panel", size=17, fill=MUTED_DARK)
    label(draw, (1405, 135), "B", size=28, fill=PAPER, bold=True)
    label(draw, (1450, 141), "small crest + dominant role", size=17, fill=MUTED_DARK)

    for row, (slug, app) in enumerate(APPS):
        y = 230 + row * row_height
        draw.rounded_rectangle((40, y + 10, width - 40, y + row_height - 10), radius=22, fill=DARK_PANEL, outline=STROKE_DARK, width=2)
        label(draw, (68, y + 58), app, size=25, fill=PAPER, bold=True)
        label(draw, (68, y + 98), "role comparison", size=16, fill=MUTED_DARK)
        for col, variant in enumerate(("a", "b")):
            candidate_id = f"{slug}-p2{variant}"
            x = 660 + col * 520
            canvas.alpha_composite(icon(masters[candidate_id], 238), (x, y + 30))
            canvas.alpha_composite(icon(masters[candidate_id], 64, "circle"), (x + 260, y + 84))
            canvas.alpha_composite(icon(masters[candidate_id], 32, "square"), (x + 278, y + 169))
            label(draw, (x + 260, y + 36), variant.upper(), size=25, fill=PAPER, bold=True)
            label(draw, (x + 260, y + 218), candidate_id, size=16, fill=MUTED_DARK)
    canvas.convert("RGB").save(output, format="PNG", optimize=True)


def build_surface_preview(masters: dict[str, Image.Image], output: Path, *, light: bool) -> None:
    background = LIGHT if light else DARK
    panel_fill = LIGHT_PANEL if light else DARK_PANEL
    foreground = INK if light else PAPER
    muted = MUTED_LIGHT if light else MUTED_DARK
    stroke = STROKE_LIGHT if light else STROKE_DARK
    width, columns, row_height = 1840, 4, 340
    rows = math.ceil(len(CANDIDATES) / columns)
    height = 105 + rows * row_height + 40
    canvas = Image.new("RGBA", (width, height), background)
    draw = ImageDraw.Draw(canvas)
    label(draw, (48, 28), f"App family P2 — {'light' if light else 'dark'} surface", size=34, fill=foreground, bold=True)
    label(draw, (49, 72), "macOS-style squircle review mask · no production selection", size=17, fill=muted)
    for index, (candidate_id, app, variant) in enumerate(CANDIDATES):
        row, col = divmod(index, columns)
        x = 38 + col * 450
        y = 105 + row * row_height
        draw.rounded_rectangle((x, y + 15, x + 425, y + 318), radius=22, fill=panel_fill, outline=stroke, width=2)
        canvas.alpha_composite(icon(masters[candidate_id], 218), (x + 16, y + 38))
        label(draw, (x + 250, y + 90), f"{app} {variant}", size=18, fill=foreground, bold=True)
        label(draw, (x + 250, y + 126), candidate_id, size=14, fill=muted)
        label(draw, (x + 250, y + 164), "P2 owner review", size=14, fill=muted)
    canvas.convert("RGB").save(output, format="PNG", optimize=True)


def build_small_sizes(masters: dict[str, Image.Image], output: Path) -> None:
    items = ((MAIN_REFERENCE[0], MAIN_REFERENCE[1], "MAIN"),) + CANDIDATES
    width, row_height = 1780, 322
    height = 110 + len(items) * row_height + 40
    canvas = Image.new("RGBA", (width, height), "#DDE4EB")
    draw = ImageDraw.Draw(canvas)
    label(draw, (45, 28), "App family P2 — small-size review", size=34, fill=INK, bold=True)
    label(draw, (46, 72), "16 / 32 / 64 / 128 / 256 px · nearest-neighbor · light and dark", size=17, fill=MUTED_LIGHT)
    for row, (candidate_id, app, variant) in enumerate(items):
        y = 110 + row * row_height
        draw.rounded_rectangle((30, y + 8, width - 30, y + row_height - 8), radius=22, fill=LIGHT, outline=STROKE_LIGHT, width=2)
        label(draw, (55, y + 32), candidate_id, size=21, fill=INK, bold=True)
        label(draw, (55, y + 66), f"{app} · {variant}", size=15, fill=MUTED_LIGHT)
        for surface_index, (surface, foreground, title) in enumerate(((LIGHT_PANEL, INK, "light"), (DARK_PANEL, PAPER, "dark"))):
            x0 = 290 + surface_index * 720
            draw.rounded_rectangle((x0, y + 25, x0 + 685, y + 288), radius=18, fill=surface)
            label(draw, (x0 + 18, y + 40), title, size=16, fill=foreground, bold=True)
            x = x0 + 20
            for size in SMALL_SIZES:
                top = y + 270 - size
                canvas.alpha_composite(icon(masters[candidate_id], size), (x, top))
                label(draw, (x, y + 274), str(size), size=13, fill=foreground)
                x += size + 28
    canvas.convert("RGB").save(output, format="PNG", optimize=True)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--candidate-dir", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    masters = normalize(args.candidate_dir)
    build_contact_sheet(masters, args.output_dir / "app-family-contact-sheet.png")
    build_surface_preview(masters, args.output_dir / "app-family-dark-preview.png", light=False)
    build_surface_preview(masters, args.output_dir / "app-family-light-preview.png", light=True)
    build_small_sizes(masters, args.output_dir / "app-family-small-sizes.png")
    print(f"validated {len(CANDIDATES)} P2 role candidates plus centered main reference at {MASTER_SIZE}x{MASTER_SIZE}")


if __name__ == "__main__":
    main()
