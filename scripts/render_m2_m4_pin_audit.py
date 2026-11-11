#!/usr/bin/env python3
"""Render 600x480 coordinate grid + anchor pin audit overlays for Milestones 2-4.

Simulates the exact SVG <image x=... y=... width=... height=... preserveAspectRatio="xMidYMid meet" />
rendering inside viewBox="0 0 600 480" so every anchor [x, y] in diagram_anchors/*.json
can be visually verified via read_file.
"""

import json
import os
import re
from PIL import Image, ImageDraw, ImageFont

PROJECT_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
DIAGRAM_BANK_DIR = os.path.join(PROJECT_ROOT, "src", "components", "workspace", "modalities", "diagram_bank")
PUBLIC_DIAGRAMS_DIR = os.path.join(PROJECT_ROOT, "public", "diagrams")
ANCHORS_DIR = os.path.join(PROJECT_ROOT, "caps-ai-backend", "app", "data", "diagram_anchors")
OUT_DIR = os.path.join(PROJECT_ROOT, "calibration_shots", "audit_m2_m4")

ITEMS = [
    ("alveolus_gas_exchange", "AlveolusGasExchangeSvg.jsx", "alveolus_gas_exchange.json"),
    ("digestive_system", "HumanDigestiveSvg.jsx", "digestive_system.json"),
    ("intestinal_villus", "IntestinalVillusSvg.jsx", "intestinal_villus.json"),
    ("human_nephron", "HumanNephronSvg.jsx", "human_nephron.json"),
    ("human_eye", "HumanEyeSvg.jsx", "human_eye.json"),
    ("human_ear", "HumanEarSvg.jsx", "human_ear.json"),
    ("endocrine_system", "EndocrineSystemSvg.jsx", "endocrine_system.json"),
    ("male_reproductive", "MaleReproductiveSvg.jsx", "male_reproductive.json"),
    ("female_reproductive", "FemaleReproductiveSvg.jsx", "female_reproductive.json"),
    ("meiosis_crossing_over", "MeiosisCrossingOverSvg.jsx", "meiosis_crossing_over.json"),
    ("plant_cell", "PlantCellSvg.jsx", "plant_cell.json"),
    ("animal_cell", "AnimalCellSvg.jsx", "animal_cell.json"),
    ("mitosis_stages", "MitosisStagesSvg.jsx", "mitosis_stages.json"),
    ("plant_leaf", "PlantLeafSvg.jsx", "plant_leaf.json"),
    ("distillation_apparatus", "DistillationApparatusSvg.jsx", "distillation_apparatus.json"),
    ("titration_apparatus", "TitrationApparatusSvg.jsx", "titration_apparatus.json"),
    ("galvanic_cell", "GalvanicCellSvg.jsx", "galvanic_cell.json"),
    ("solar_system_earth_space", "SolarSystemEarthSpaceSvg.jsx", "solar_system_earth_space.json"),
    ("particle_model", "ParticleModelSvg.jsx", "particle_model.json"),
]


def parse_first_image_box(jsx_path):
    with open(jsx_path, "r", encoding="utf-8") as f:
        jsx = f.read()
    m = re.search(r'<image[\s\S]*?/>', jsx)
    if not m:
        raise ValueError(f"No <image> in {jsx_path}")
    tag = m.group(0)
    href = re.search(r'href=["\']([^"\']+)["\']', tag).group(1)
    x = float(re.search(r'\bx=["\']([^"\']+)["\']', tag).group(1))
    y = float(re.search(r'\by=["\']([^"\']+)["\']', tag).group(1))
    w = float(re.search(r'\bwidth=["\']([^"\']+)["\']', tag).group(1))
    h = float(re.search(r'\bheight=["\']([^"\']+)["\']', tag).group(1))
    return href, x, y, w, h


def render_item(master, comp_name, json_name):
    os.makedirs(OUT_DIR, exist_ok=True)
    jsx_path = os.path.join(DIAGRAM_BANK_DIR, comp_name)
    json_path = os.path.join(ANCHORS_DIR, json_name)

    href, bx, by, bw, bh = parse_first_image_box(jsx_path)
    img_rel = href.replace("/diagrams/", "")
    img_path = os.path.join(PUBLIC_DIAGRAMS_DIR, img_rel)

    # Render at 2x (1200x960) for crisp readability of coordinates and pin labels,
    # while labeling coordinates in 600x480 SVG viewBox units!
    SCALE = 2
    canvas = Image.new("RGB", (600 * SCALE, 480 * SCALE), (255, 255, 255))

    plate = Image.open(img_path).convert("RGB")
    pw, ph = plate.size
    # preserveAspectRatio="xMidYMid meet" inside (bx, by, bw, bh)
    scale_factor = min((bw * SCALE) / pw, (bh * SCALE) / ph)
    new_w = int(round(pw * scale_factor))
    new_h = int(round(ph * scale_factor))
    resized = plate.resize((new_w, new_h), Image.Resampling.LANCZOS)
    dest_x = int(round(bx * SCALE + (bw * SCALE - new_w) / 2.0))
    dest_y = int(round(by * SCALE + (bh * SCALE - new_h) / 2.0))
    canvas.paste(resized, (dest_x, dest_y))

    draw = ImageDraw.Draw(canvas, "RGBA")

    # Draw 50px major grid and 25px minor grid in 600x480 coordinates
    for gx in range(0, 601, 25):
        px = gx * SCALE
        is_major = (gx % 50 == 0)
        color = (0, 120, 255, 90 if is_major else 40)
        draw.line([(px, 0), (px, 480 * SCALE)], fill=color, width=2 if is_major else 1)
        if is_major and 0 < gx < 600:
            draw.text((px + 3, 4), str(gx), fill=(0, 80, 200, 220))
            draw.text((px + 3, 462 * SCALE), str(gx), fill=(0, 80, 200, 220))

    for gy in range(0, 481, 25):
        py = gy * SCALE
        is_major = (gy % 50 == 0)
        color = (0, 120, 255, 90 if is_major else 40)
        draw.line([(0, py), (600 * SCALE, py)], fill=color, width=2 if is_major else 1)
        if is_major and 0 < gy < 480:
            draw.text((4, py + 2), str(gy), fill=(0, 80, 200, 220))
            draw.text((575 * SCALE, py + 2), str(gy), fill=(0, 80, 200, 220))

    with open(json_path, "r", encoding="utf-8") as f:
        adata = json.load(f)
    anchors = adata.get("anchors", {})

    # Sort anchors by y to distribute side callouts cleanly without overlap
    left_items = []
    right_items = []
    for idx, (key, val) in enumerate(anchors.items()):
        ax, ay = val["anchor"]
        side = val.get("side", "left" if ax < 300 else "right")
        entry = (ay, key, ax, ay, side)
        if side == "left":
            left_items.append(entry)
        else:
            right_items.append(entry)

    left_items.sort(key=lambda t: t[0])
    right_items.sort(key=lambda t: t[0])

    PALETTE = [
        (220, 38, 38, 255),
        (37, 99, 235, 255),
        (5, 150, 105, 255),
        (217, 119, 6, 255),
        (124, 58, 237, 255),
        (219, 39, 119, 255),
        (8, 145, 178, 255),
        (101, 163, 13, 255),
    ]

    def draw_group(items, is_left):
        n = len(items)
        for i, (_, key, ax, ay, _) in enumerate(items):
            color = PALETTE[i % len(PALETTE)]
            px, py = int(ax * SCALE), int(ay * SCALE)
            # Target bullseye on exact [ax, ay]
            r_outer = 9
            r_inner = 4
            draw.ellipse([px - r_outer, py - r_outer, px + r_outer, py + r_outer], outline=(255, 255, 255, 255), width=3)
            draw.ellipse([px - r_outer, py - r_outer, px + r_outer, py + r_outer], outline=color, width=2)
            draw.ellipse([px - r_inner, py - r_inner, px + r_inner, py + r_inner], fill=color)

            # Label box near side margin
            slot_y = int((55 + i * (370.0 / max(1, n - 1 if n > 1 else 1))) * SCALE) if n > 1 else py
            bx_edge = int((110 if is_left else 490) * SCALE)
            draw.line([(px, py), (bx_edge, slot_y)], fill=color, width=3)
            label_txt = f"{key} [{ax},{ay}]"
            tx = 8 * SCALE if is_left else 494 * SCALE
            draw.rectangle([tx - 2, slot_y - 11, tx + len(label_txt) * 7 + 4, slot_y + 11], fill=(255, 255, 255, 235), outline=color, width=2)
            draw.text((tx + 2, slot_y - 7), label_txt, fill=(15, 23, 42, 255))

    draw_group(left_items, True)
    draw_group(right_items, False)

    out_path = os.path.join(OUT_DIR, f"{master}_audit.png")
    canvas.save(out_path)
    print(f"Saved {out_path}")


def main():
    for master, comp, js in ITEMS:
        render_item(master, comp, js)


if __name__ == "__main__":
    main()
