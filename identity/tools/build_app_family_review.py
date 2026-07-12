#!/usr/bin/env python3
"""Normalize app-family candidates and build non-production review sheets."""

from __future__ import annotations

import argparse
import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


MASTER_SIZE = 2048
SMALL_SIZES = (16, 32, 64, 128, 256)
CANDIDATES = (
    ("studio-a", "Gnaroshi Studio"),
    ("studio-b", "Gnaroshi Studio"),
    ("paperflow-a", "PaperFlow"),
    ("paperflow-b", "PaperFlow"),
    ("arxiv-discovery-a", "Arxiv Discovery"),
    ("arxiv-discovery-b", "Arxiv Discovery"),
    ("tr-gpu-monitor-a", "TR GPU Monitor"),
    ("tr-gpu-monitor-b", "TR GPU Monitor"),
    ("runshelf-a", "RunShelf"),
    ("runshelf-b", "RunShelf"),
    ("contentdeck-a", "ContentDeck"),
    ("contentdeck-b", "ContentDeck"),
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
    for candidate_id, _ in CANDIDATES:
        path = candidate_dir / f"{candidate_id}.png"
        if not path.is_file():
            raise FileNotFoundError(f"missing candidate: {path}")
        with Image.open(path) as source:
            if source.width != source.height:
                raise ValueError(f"candidate must be square: {path} is {source.size}")
            image = source.convert("RGB")
        if image.size != (MASTER_SIZE, MASTER_SIZE):
            image = image.resize((MASTER_SIZE, MASTER_SIZE), Image.Resampling.LANCZOS)
            image.save(path, format="PNG", optimize=True)
        masters[candidate_id] = image
    return masters


def mask(size: int, shape: str) -> Image.Image:
    result = Image.new("L", (size, size), 0)
    draw = ImageDraw.Draw(result)
    if shape == "circle":
        draw.ellipse((0, 0, size - 1, size - 1), fill=255)
    elif shape == "squircle":
        # A superellipse review approximation of the macOS launcher mask.
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
    resized = image.resize((size, size), Image.Resampling.LANCZOS)
    result = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    result.paste(resized, (0, 0), mask(size, shape))
    return result


def label(draw: ImageDraw.ImageDraw, xy: tuple[int, int], text: str, *, size: int, fill: str, bold: bool = False) -> None:
    draw.text(xy, text, font=font(size, bold), fill=fill)


def build_contact_sheet(masters: dict[str, Image.Image], output: Path) -> None:
    width, row_height = 1600, 320
    height = 110 + 6 * row_height + 50
    canvas = Image.new("RGBA", (width, height), DARK)
    draw = ImageDraw.Draw(canvas)
    label(draw, (54, 34), "Gnaroshi app icon family — owner review", size=36, fill=PAPER, bold=True)
    label(draw, (55, 78), "Each candidate: macOS-style squircle, circular mask, square tile", size=18, fill=MUTED_DARK)

    for row in range(6):
        y = 110 + row * row_height
        app = CANDIDATES[row * 2][1]
        label(draw, (55, y + 12), app, size=24, fill=PAPER, bold=True)
        for col in range(2):
            candidate_id = CANDIDATES[row * 2 + col][0]
            x = 55 + col * 760
            panel = (x, y + 50, x + 730, y + 300)
            draw.rounded_rectangle(panel, radius=24, fill=DARK_PANEL, outline=STROKE_DARK, width=2)
            label(draw, (x + 24, y + 66), candidate_id, size=20, fill=PAPER, bold=True)
            canvas.alpha_composite(icon(masters[candidate_id], 190, "squircle"), (x + 24, y + 96))
            canvas.alpha_composite(icon(masters[candidate_id], 118, "circle"), (x + 252, y + 132))
            canvas.alpha_composite(icon(masters[candidate_id], 118, "square"), (x + 407, y + 132))
            label(draw, (x + 258, y + 258), "circle", size=16, fill=MUTED_DARK)
            label(draw, (x + 425, y + 258), "square", size=16, fill=MUTED_DARK)
            label(draw, (x + 558, y + 174), "A: foreground" if candidate_id.endswith("-a") else "B: background", size=17, fill=MUTED_DARK)
    canvas.convert("RGB").save(output, format="PNG", optimize=True)


def build_surface_preview(masters: dict[str, Image.Image], output: Path, *, light: bool) -> None:
    background = LIGHT if light else DARK
    panel_fill = LIGHT_PANEL if light else DARK_PANEL
    foreground = INK if light else PAPER
    muted = MUTED_LIGHT if light else MUTED_DARK
    stroke = STROKE_LIGHT if light else STROKE_DARK
    width, row_height = 1400, 235
    height = 100 + 6 * row_height + 45
    canvas = Image.new("RGBA", (width, height), background)
    draw = ImageDraw.Draw(canvas)
    label(draw, (48, 30), f"App family — {'light' if light else 'dark'} surface", size=34, fill=foreground, bold=True)
    label(draw, (49, 72), "macOS-style squircle review mask", size=17, fill=muted)
    for row in range(6):
        y = 100 + row * row_height
        app = CANDIDATES[row * 2][1]
        label(draw, (48, y + 92), app, size=22, fill=foreground, bold=True)
        for col in range(2):
            candidate_id = CANDIDATES[row * 2 + col][0]
            x = 325 + col * 520
            draw.rounded_rectangle((x, y + 18, x + 490, y + 216), radius=22, fill=panel_fill, outline=stroke, width=2)
            canvas.alpha_composite(icon(masters[candidate_id], 170), (x + 16, y + 32))
            label(draw, (x + 210, y + 82), candidate_id, size=22, fill=foreground, bold=True)
            label(draw, (x + 210, y + 118), "foreground role marker" if candidate_id.endswith("-a") else "background role emblem", size=16, fill=muted)
    canvas.convert("RGB").save(output, format="PNG", optimize=True)


def build_small_sizes(masters: dict[str, Image.Image], output: Path) -> None:
    width, row_height = 1700, 340
    height = 110 + len(CANDIDATES) * row_height + 40
    canvas = Image.new("RGBA", (width, height), "#DDE4EB")
    draw = ImageDraw.Draw(canvas)
    label(draw, (45, 28), "App family — small-size review", size=34, fill=INK, bold=True)
    label(draw, (46, 72), "16 / 32 / 64 / 128 / 256 px on light and dark surfaces", size=17, fill=MUTED_LIGHT)
    for row, (candidate_id, app) in enumerate(CANDIDATES):
        y = 110 + row * row_height
        draw.rounded_rectangle((30, y + 10, width - 30, y + row_height - 10), radius=22, fill=LIGHT, outline=STROKE_LIGHT, width=2)
        label(draw, (55, y + 34), candidate_id, size=22, fill=INK, bold=True)
        label(draw, (55, y + 69), app, size=16, fill=MUTED_LIGHT)
        for surface_index, (surface, foreground, title) in enumerate(((LIGHT_PANEL, INK, "light"), (DARK_PANEL, PAPER, "dark"))):
            x0 = 265 + surface_index * 700
            draw.rounded_rectangle((x0, y + 28, x0 + 665, y + 300), radius=18, fill=surface)
            label(draw, (x0 + 18, y + 43), title, size=16, fill=foreground, bold=True)
            x = x0 + 20
            for size in SMALL_SIZES:
                top = y + 282 - size
                canvas.alpha_composite(icon(masters[candidate_id], size), (x, top))
                label(draw, (x, y + 285), str(size), size=13, fill=foreground)
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
    print(f"validated {len(masters)} candidates at {MASTER_SIZE}x{MASTER_SIZE}")


if __name__ == "__main__":
    main()
