#!/usr/bin/env python3
"""Remediates Milestone 2–4 raster textbook and exam stipple plates.

1. Removes the 3 blue horizontal transition arrows from synapsis_crossing_over_nolabels.png
   to produce a 100% unlabeled meiosis_crossing_over_textbook.jpg.
2. Produces meiosis_crossing_over_exam_stipple.jpg where one homologous chromosome is
   pure white with black outline and the other is dot-stippled with black outline,
   making recombinant chromatid segments unmistakably clear in black-and-white.
3. Produces open-lumen pen-and-ink line-art + sparse dot-stipple exam plates for
   villus_exam_stipple.jpg, nephron_exam_stipple.jpg, and male_reproductive_exam_stipple.jpg
   with zero solid black silhouettes.
"""

import os
import numpy as np
from PIL import Image, ImageFilter, ImageOps

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIAGRAMS_DIR = os.path.join(ROOT, "public", "diagrams")


def make_open_lumen_stipple(src_path: str, dst_path: str, edge_percentile: float = 86.0) -> None:
    """Converts a 3D textbook plate into an open-lumen pen-and-ink line-art + sparse stipple plate."""
    img = Image.open(src_path).convert("RGB")
    arr = np.asarray(img, dtype=np.float32)

    # Identify pure white background
    is_bg = (arr[:, :, 0] > 242) & (arr[:, :, 1] > 242) & (arr[:, :, 2] > 242)

    # Grayscale luminance
    gray = 0.299 * arr[:, :, 0] + 0.587 * arr[:, :, 1] + 0.114 * arr[:, :, 2]

    # Difference of Gaussians + Sobel gradient magnitude for crisp pen-and-ink outlines
    pil_gray = Image.fromarray(gray.astype(np.uint8))
    g1 = np.asarray(pil_gray.filter(ImageFilter.GaussianBlur(radius=0.8)), dtype=np.float32)
    g2 = np.asarray(pil_gray.filter(ImageFilter.GaussianBlur(radius=2.4)), dtype=np.float32)
    dog = np.maximum(0.0, g2 - g1)

    # Color channel gradients (captures boundaries between red/blue vessels and tissue of similar luminance)
    gx = np.abs(np.diff(arr, axis=1, prepend=arr[:, :1, :])).max(axis=2)
    gy = np.abs(np.diff(arr, axis=0, prepend=arr[:1, :, :])).max(axis=2)
    grad = np.hypot(gx, gy)

    edge_strength = dog * 2.2 + grad * 0.75
    thresh = np.percentile(edge_strength[~is_bg], edge_percentile) if np.any(~is_bg) else 15.0
    is_edge = (edge_strength > max(thresh, 11.0)) & (~is_bg)

    # Create deterministic blue-noise-like Bayer/halftone stipple grid on pure white
    h, w = gray.shape
    yy, xx = np.meshgrid(np.arange(h), np.arange(w), indexing="ij")
    # Sparse stipple dot centers every 5 pixels with staggered row offset
    period = 5
    row_shift = ((yy // period) % 2) * (period // 2)
    dx = (xx + row_shift) % period - (period // 2)
    dy = yy % period - (period // 2)
    dist_sq = dx * dx + dy * dy

    # Normalize tissue darkness into [0.0, 1.0] but lift strongly so interiors stay open white
    darkness = np.clip((245.0 - gray) / 245.0, 0.0, 1.0)
    # Place tiny 1px dot if darkness > 0.22, 2px dot only in deepest shadows (> 0.68)
    is_stipple_dot = (
        (~is_bg)
        & (~is_edge)
        & (
            ((darkness > 0.22) & (dist_sq == 0))
            | ((darkness > 0.65) & (dist_sq <= 1) & (((xx + yy) % 2) == 0))
        )
    )

    out = np.full((h, w), 255, dtype=np.uint8)
    out[is_stipple_dot] = 45
    out[is_edge] = 18

    # Slight anti-aliasing pass while preserving crisp contrast
    out_img = Image.fromarray(out, mode="L").convert("RGB")
    out_img.save(dst_path, "JPEG", quality=95)
    white_pct = float(np.mean(out > 220) * 100.0)
    black_pct = float(np.mean(out < 50) * 100.0)
    print(f"Saved {os.path.basename(dst_path)} (white={white_pct:.1f}%, ink={black_pct:.1f}%)")


def build_meiosis_plates() -> None:
    src_path = os.path.join(DIAGRAMS_DIR, "source_plates", "synapsis_crossing_over_nolabels.png")
    img = Image.open(src_path).convert("RGBA")
    white_bg = Image.new("RGB", img.size, (255, 255, 255))
    white_bg.paste(img, (0, 0), img)

    bbox = white_bg.convert("L").point(lambda p: 0 if p > 250 else 255).getbbox()
    cropped = white_bg.crop(bbox)
    canvas = Image.new("RGB", (600, 480), (255, 255, 255))
    w, h = cropped.size
    scale = min(540 / w, 400 / h)
    new_w, new_h = int(w * scale), int(h * scale)
    resized = cropped.resize((new_w, new_h), Image.Resampling.LANCZOS)
    canvas.paste(resized, ((600 - new_w) // 2, (480 - new_h) // 2))

    arr = np.asarray(canvas, dtype=np.uint8).copy()
    r = arr[:, :, 0].astype(np.int16)
    g = arr[:, :, 1].astype(np.int16)
    b = arr[:, :, 2].astype(np.int16)

    # Remove the 3 isolated blue transition arrows by connected-component area:
    # Chromosome pairs each have > 2,000 pixels; the 3 arrows each have < 600 pixels.
    non_white = (r < 245) | (g < 245) | (b < 245)
    visited = np.zeros_like(non_white, dtype=bool)
    h, w = non_white.shape
    for y0 in range(h):
        for x0 in range(w):
            if non_white[y0, x0] and not visited[y0, x0]:
                stack = [(y0, x0)]
                visited[y0, x0] = True
                comp = []
                while stack:
                    cy, cx = stack.pop()
                    comp.append((cy, cx))
                    for ny in range(max(0, cy - 1), min(h, cy + 2)):
                        for nx in range(max(0, cx - 1), min(w, cx + 2)):
                            if non_white[ny, nx] and not visited[ny, nx]:
                                visited[ny, nx] = True
                                stack.append((ny, nx))
                if len(comp) < 900:
                    for cy, cx in comp:
                        arr[cy, cx, :] = 255

    textbook_out = os.path.join(DIAGRAMS_DIR, "meiosis_crossing_over_textbook.jpg")
    Image.fromarray(arr).save(textbook_out, "JPEG", quality=96)
    print(f"Saved {os.path.basename(textbook_out)} (blue arrows removed)")

    # Now build meiosis_crossing_over_exam_stipple.jpg:
    # Distinguish the two homologous chromosomes:
    # - Homologue 1 (Blue-ish: b > r + 25): pure white interior + crisp black outline
    # - Homologue 2 (Purple/Violet: r and b both present, r >= b - 25): stippled interior + crisp black outline
    r = arr[:, :, 0].astype(np.float32)
    g = arr[:, :, 1].astype(np.float32)
    b = arr[:, :, 2].astype(np.float32)

    is_bg = (r > 240) & (g > 240) & (b > 240)
    is_blue_chrom = (~is_bg) & ((b - r) > 32)
    is_purple_chrom = (~is_bg) & (~is_blue_chrom)

    # Compute crisp boundaries (both outer chromosome boundary and chiasma/recombinant boundary)
    gx = np.abs(np.diff(arr.astype(np.float32), axis=1, prepend=arr[:, :1, :])).max(axis=2)
    gy = np.abs(np.diff(arr.astype(np.float32), axis=0, prepend=arr[:1, :, :])).max(axis=2)
    grad = np.hypot(gx, gy)
    is_outline = (grad > 28.0) & (~is_bg)

    h, w = r.shape
    yy, xx = np.meshgrid(np.arange(h), np.arange(w), indexing="ij")
    period = 4
    row_shift = ((yy // period) % 2) * (period // 2)
    dx = (xx + row_shift) % period - (period // 2)
    dy = yy % period - (period // 2)
    dist_sq = dx * dx + dy * dy

    # Purple chromosome gets a clean stipple dot pattern; blue chromosome stays open white!
    is_purple_stipple = is_purple_chrom & (~is_outline) & (dist_sq <= 1) & (((xx + yy) % 2) == 0)

    exam_out_arr = np.full((h, w), 255, dtype=np.uint8)
    exam_out_arr[is_purple_stipple] = 40
    exam_out_arr[is_outline] = 15

    exam_path = os.path.join(DIAGRAMS_DIR, "meiosis_crossing_over_exam_stipple.jpg")
    Image.fromarray(exam_out_arr, mode="L").convert("RGB").save(exam_path, "JPEG", quality=96)
    print(f"Saved {os.path.basename(exam_path)} (two-tone white vs stippled recombinant chromatids)")


if __name__ == "__main__":
    build_meiosis_plates()
    make_open_lumen_stipple(
        os.path.join(DIAGRAMS_DIR, "villus_textbook.jpg"),
        os.path.join(DIAGRAMS_DIR, "villus_exam_stipple.jpg"),
        edge_percentile=85.0,
    )
    make_open_lumen_stipple(
        os.path.join(DIAGRAMS_DIR, "nephron_textbook.jpg"),
        os.path.join(DIAGRAMS_DIR, "nephron_exam_stipple.jpg"),
        edge_percentile=84.0,
    )
    make_open_lumen_stipple(
        os.path.join(DIAGRAMS_DIR, "male_reproductive_textbook.jpg"),
        os.path.join(DIAGRAMS_DIR, "male_reproductive_exam_stipple.jpg"),
        edge_percentile=85.0,
    )
