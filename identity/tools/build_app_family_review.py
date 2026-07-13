#!/usr/bin/env python3
"""Normalize P3 app-family candidates and build non-production review sheets."""

from __future__ import annotations

import argparse
import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


MASTER_SIZE = 2048
SMALL_SIZES = (16, 32, 64, 128, 256)
MAIN_REFERENCE = ("gnaroshi-main-p3", "Gnaroshi main/default", "centered neutral identity")
CANDIDATES = (
    ("studio-p3", "Gnaroshi Studio", "research → authoring workbench → publish"),
    ("paperflow-p3", "PaperFlow", "papers → safe sorter → library drawers"),
    ("arxiv-discovery-p3", "Arxiv Discovery", "incoming papers discovered by radar scan"),
    ("tr-gpu-monitor-p3", "TR GPU Monitor", "remote GPU hardware and live telemetry"),
    ("runshelf-p3", "RunShelf", "experiment metrics and artifacts stored as run records"),
    ("contentdeck-p3", "ContentDeck", "media subtitles and bounded segment practice"),
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
    width, row_height = 1680, 370
    height = 215 + 3 * row_height + 45
    canvas = Image.new("RGBA", (width, height), DARK)
    draw = ImageDraw.Draw(canvas)
    label(draw, (50, 28), "Gnaroshi app icon family — pixel P3", size=38, fill=PAPER, bold=True)
    label(draw, (51, 76), "Concrete workflow foreground · partial mascot behind · one shared overlap system", size=19, fill=MUTED_DARK)
    canvas.alpha_composite(icon(masters[MAIN_REFERENCE[0]], 112), (52, 102))
    label(draw, (184, 125), MAIN_REFERENCE[1], size=21, fill=PAPER, bold=True)
    label(draw, (184, 160), MAIN_REFERENCE[2], size=16, fill=MUTED_DARK)

    for index, (candidate_id, app, role) in enumerate(CANDIDATES):
        row, col = divmod(index, 2)
        x = 40 + col * 815
        y = 215 + row * row_height
        draw.rounded_rectangle((x, y + 12, x + 785, y + 347), radius=22, fill=DARK_PANEL, outline=STROKE_DARK, width=2)
        canvas.alpha_composite(icon(masters[candidate_id], 270), (x + 22, y + 40))
        label(draw, (x + 318, y + 56), app, size=24, fill=PAPER, bold=True)
        label(draw, (x + 318, y + 94), candidate_id, size=16, fill=MUTED_DARK)
        label(draw, (x + 318, y + 132), role, size=15, fill=PAPER)
        label(draw, (x + 318, y + 174), "small-size check", size=14, fill=MUTED_DARK)
        canvas.alpha_composite(icon(masters[candidate_id], 64, "circle"), (x + 318, y + 208))
        canvas.alpha_composite(icon(masters[candidate_id], 32, "square"), (x + 405, y + 240))
        canvas.alpha_composite(icon(masters[candidate_id], 128, "squircle"), (x + 470, y + 190))
    canvas.convert("RGB").save(output, format="PNG", optimize=True)


def build_surface_preview(masters: dict[str, Image.Image], output: Path, *, light: bool) -> None:
    background = LIGHT if light else DARK
    panel_fill = LIGHT_PANEL if light else DARK_PANEL
    foreground = INK if light else PAPER
    muted = MUTED_LIGHT if light else MUTED_DARK
    stroke = STROKE_LIGHT if light else STROKE_DARK
    width, columns, row_height = 1740, 3, 350
    rows = math.ceil(len(CANDIDATES) / columns)
    height = 105 + rows * row_height + 40
    canvas = Image.new("RGBA", (width, height), background)
    draw = ImageDraw.Draw(canvas)
    label(draw, (48, 28), f"App family P3 — {'light' if light else 'dark'} surface", size=34, fill=foreground, bold=True)
    label(draw, (49, 72), "macOS-style squircle review mask · no production selection", size=17, fill=muted)
    for index, (candidate_id, app, role) in enumerate(CANDIDATES):
        row, col = divmod(index, columns)
        x = 38 + col * 565
        y = 105 + row * row_height
        draw.rounded_rectangle((x, y + 15, x + 535, y + 328), radius=22, fill=panel_fill, outline=stroke, width=2)
        canvas.alpha_composite(icon(masters[candidate_id], 230), (x + 18, y + 42))
        label(draw, (x + 270, y + 78), app, size=19, fill=foreground, bold=True)
        label(draw, (x + 270, y + 114), candidate_id, size=14, fill=muted)
        label(draw, (x + 270, y + 154), role, size=13, fill=foreground)
    canvas.convert("RGB").save(output, format="PNG", optimize=True)


def build_small_sizes(masters: dict[str, Image.Image], output: Path) -> None:
    items = (MAIN_REFERENCE,) + CANDIDATES
    width, row_height = 1780, 322
    height = 110 + len(items) * row_height + 40
    canvas = Image.new("RGBA", (width, height), "#DDE4EB")
    draw = ImageDraw.Draw(canvas)
    label(draw, (45, 28), "App family P3 — small-size review", size=34, fill=INK, bold=True)
    label(draw, (46, 72), "16 / 32 / 64 / 128 / 256 px · nearest-neighbor · light and dark", size=17, fill=MUTED_LIGHT)
    for row, (candidate_id, app, role) in enumerate(items):
        y = 110 + row * row_height
        draw.rounded_rectangle((30, y + 8, width - 30, y + row_height - 8), radius=22, fill=LIGHT, outline=STROKE_LIGHT, width=2)
        label(draw, (55, y + 32), candidate_id, size=21, fill=INK, bold=True)
        label(draw, (55, y + 66), app, size=15, fill=MUTED_LIGHT)
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
    print(f"validated {len(CANDIDATES)} P3 workflow candidates plus centered main reference at {MASTER_SIZE}x{MASTER_SIZE}")


if __name__ == "__main__":
    main()
