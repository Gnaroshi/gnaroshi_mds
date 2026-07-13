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
    ("studio-p1", "Gnaroshi Studio"),
    ("paperflow-p1", "PaperFlow"),
    ("arxiv-discovery-p1", "Arxiv Discovery"),
    ("tr-gpu-monitor-p1", "TR GPU Monitor"),
    ("runshelf-p1", "RunShelf"),
    ("contentdeck-p1", "ContentDeck"),
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
    resized = image.resize((size, size), Image.Resampling.NEAREST)
    result = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    result.paste(resized, (0, 0), mask(size, shape))
    return result


def label(draw: ImageDraw.ImageDraw, xy: tuple[int, int], text: str, *, size: int, fill: str, bold: bool = False) -> None:
    draw.text(xy, text, font=font(size, bold), fill=fill)


def build_contact_sheet(masters: dict[str, Image.Image], output: Path) -> None:
    width, row_height = 1600, 360
    height = 110 + 3 * row_height + 50
    canvas = Image.new("RGBA", (width, height), DARK)
    draw = ImageDraw.Draw(canvas)
    label(draw, (54, 34), "Gnaroshi app icon family — pixel P1", size=36, fill=PAPER, bold=True)
    label(draw, (55, 78), "One fixed mascot template · one canonical role glyph · one key color per app", size=18, fill=MUTED_DARK)

    for row in range(3):
        y = 110 + row * row_height
        for col in range(2):
            candidate_id, app = CANDIDATES[row * 2 + col]
            x = 55 + col * 760
            panel = (x, y + 22, x + 730, y + 338)
            draw.rounded_rectangle(panel, radius=24, fill=DARK_PANEL, outline=STROKE_DARK, width=2)
            label(draw, (x + 24, y + 42), app, size=24, fill=PAPER, bold=True)
            label(draw, (x + 24, y + 76), candidate_id, size=17, fill=MUTED_DARK)
            canvas.alpha_composite(icon(masters[candidate_id], 210, "squircle"), (x + 24, y + 108))
            canvas.alpha_composite(icon(masters[candidate_id], 128, "circle"), (x + 272, y + 150))
            canvas.alpha_composite(icon(masters[candidate_id], 128, "square"), (x + 438, y + 150))
            label(draw, (x + 285, y + 288), "circle", size=16, fill=MUTED_DARK)
            label(draw, (x + 458, y + 288), "square", size=16, fill=MUTED_DARK)
            label(draw, (x + 588, y + 198), "pixel P1", size=17, fill=MUTED_DARK)
    canvas.convert("RGB").save(output, format="PNG", optimize=True)


def build_surface_preview(masters: dict[str, Image.Image], output: Path, *, light: bool) -> None:
    background = LIGHT if light else DARK
    panel_fill = LIGHT_PANEL if light else DARK_PANEL
    foreground = INK if light else PAPER
    muted = MUTED_LIGHT if light else MUTED_DARK
    stroke = STROKE_LIGHT if light else STROKE_DARK
    width, row_height = 1680, 340
    height = 100 + 2 * row_height + 45
    canvas = Image.new("RGBA", (width, height), background)
    draw = ImageDraw.Draw(canvas)
    label(draw, (48, 30), f"App family — {'light' if light else 'dark'} surface", size=34, fill=foreground, bold=True)
    label(draw, (49, 72), "macOS-style squircle review mask", size=17, fill=muted)
    for row in range(2):
        y = 100 + row * row_height
        for col in range(3):
            candidate_id, app = CANDIDATES[row * 3 + col]
            x = 45 + col * 545
            draw.rounded_rectangle((x, y + 18, x + 515, y + 318), radius=22, fill=panel_fill, outline=stroke, width=2)
            canvas.alpha_composite(icon(masters[candidate_id], 220), (x + 18, y + 40))
            label(draw, (x + 258, y + 108), app, size=20, fill=foreground, bold=True)
            label(draw, (x + 258, y + 142), candidate_id, size=16, fill=muted)
            label(draw, (x + 258, y + 178), "fixed pixel template", size=15, fill=muted)
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
