"""Grade 9 Mathematics - Factorisation SVG Helpers.
Generates deterministic, accessible SVG diagrams for area models and geometric representations of factorisation.
All helpers accept `seed: Optional[int] = None, **kwargs: Any` and inject entropy comments to vary across seeds.
"""
from __future__ import annotations

from typing import Any, Optional


def draw_factorisation_area_model_svg(
    dim_top_1: str,
    dim_top_2: str,
    dim_left_1: str,
    dim_left_2: str,
    cell_tl: str,
    cell_tr: str,
    cell_bl: str,
    cell_br: str,
    seed: Optional[int] = None,
    **kwargs: Any,
) -> str:
    """Renders a 2x2 area tile model visually illustrating binomial factorisation."""
    entropy = f"<!-- s:{seed} -->\n" if seed is not None else ""
    x0, y0 = 90, 70
    w1, w2 = 140, 140
    h1, h2 = 80, 80
    total_w = 420
    total_h = 280

    elements = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {total_w} {total_h}" width="100%" height="auto" class="rounded-lg bg-slate-900 border border-slate-700/60 p-2">',
        entropy,
        # Top dimension labels
        f'<text x="{x0 + w1 // 2}" y="{y0 - 15}" font-size="16" font-weight="700" fill="#38bdf8" text-anchor="middle">{dim_top_1}</text>',
        f'<text x="{x0 + w1 + w2 // 2}" y="{y0 - 15}" font-size="16" font-weight="700" fill="#38bdf8" text-anchor="middle">{dim_top_2}</text>',
        # Left dimension labels
        f'<text x="{x0 - 20}" y="{y0 + h1 // 2 + 5}" font-size="16" font-weight="700" fill="#facc15" text-anchor="end">{dim_left_1}</text>',
        f'<text x="{x0 - 20}" y="{y0 + h1 + h2 // 2 + 5}" font-size="16" font-weight="700" fill="#facc15" text-anchor="end">{dim_left_2}</text>',
        # Top-Left Cell
        f'<rect x="{x0}" y="{y0}" width="{w1}" height="{h1}" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>',
        f'<text x="{x0 + w1 // 2}" y="{y0 + h1 // 2 + 6}" font-size="16" font-weight="700" fill="#f8fafc" text-anchor="middle">{cell_tl}</text>',
        # Top-Right Cell
        f'<rect x="{x0 + w1}" y="{y0}" width="{w2}" height="{h1}" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>',
        f'<text x="{x0 + w1 + w2 // 2}" y="{y0 + h1 // 2 + 6}" font-size="16" font-weight="700" fill="#94a3b8" text-anchor="middle">{cell_tr}</text>',
        # Bottom-Left Cell
        f'<rect x="{x0}" y="{y0 + h1}" width="{w1}" height="{h2}" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>',
        f'<text x="{x0 + w1 // 2}" y="{y0 + h1 + h2 // 2 + 6}" font-size="16" font-weight="700" fill="#94a3b8" text-anchor="middle">{cell_bl}</text>',
        # Bottom-Right Cell
        f'<rect x="{x0 + w1}" y="{y0 + h1}" width="{w2}" height="{h2}" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>',
        f'<text x="{x0 + w1 + w2 // 2}" y="{y0 + h1 + h2 // 2 + 6}" font-size="16" font-weight="700" fill="#facc15" text-anchor="middle">{cell_br}</text>',
        '</svg>',
    ]
    return "\n".join(elements)


def draw_factorisation_rectangle_svg(
    area_label: str,
    length_label: str,
    width_label: str,
    seed: Optional[int] = None,
    **kwargs: Any,
) -> str:
    """Renders a geometric rectangle showing known area and one side to solve for the missing side."""
    entropy = f"<!-- s:{seed} -->\n" if seed is not None else ""
    x, y, w, h = 90, 50, 320, 170
    total_w, total_h = 500, 260

    elements = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {total_w} {total_h}" width="100%" height="auto" class="rounded-lg bg-slate-900 border border-slate-700/60 p-2">',
        entropy,
        # Rectangle outline
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="#0f172a" stroke="#818cf8" stroke-width="2.5"/>',
        # Center Area Label
        f'<text x="{x + w // 2}" y="{y + h // 2 - 5}" font-size="14" font-weight="600" fill="#94a3b8" text-anchor="middle">Area:</text>',
        f'<text x="{x + w // 2}" y="{y + h // 2 + 18}" font-size="16" font-weight="700" fill="#38bdf8" text-anchor="middle">{area_label}</text>',
        # Top Length Label
        f'<text x="{x + w // 2}" y="{y - 12}" font-size="15" font-weight="700" fill="#a78bfa" text-anchor="middle">{length_label}</text>',
        # Left Width Label
        f'<text x="{x - 15}" y="{y + h // 2 + 5}" font-size="15" font-weight="700" fill="#facc15" text-anchor="end">{width_label}</text>',
        '</svg>',
    ]
    return "\n".join(elements)
