"""Grade 9 Mathematics - Algebraic Equations 1 SVG Helpers.
Generates deterministic, accessible SVG diagrams for equation models: balance scale, supplementary angles, and triangle angle equations.
All helpers accept `seed: Optional[int] = None, **kwargs: Any` and inject entropy comments to vary across seeds.
"""
from __future__ import annotations

from typing import Any, Optional


def draw_balance_scale_svg(
    left_label: str,
    right_label: str,
    seed: Optional[int] = None,
    **kwargs: Any,
) -> str:
    """Renders a balanced beam scale illustrating algebraic equality (LHS = RHS)."""
    entropy = f"<!-- s:{seed} -->\n" if seed is not None else ""
    total_w, total_h = 500, 260
    cx, fulcrum_y = 250, 160
    beam_w = 340
    y_beam = 90

    elements = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {total_w} {total_h}" width="100%" height="auto" class="rounded-lg bg-slate-900 border border-slate-700/60 p-2">',
        entropy,
        # Base and Fulcrum
        f'<polygon points="{cx - 30},{fulcrum_y + 70} {cx + 30},{fulcrum_y + 70} {cx},{fulcrum_y}" fill="#334155" stroke="#64748b" stroke-width="2"/>',
        f'<rect x="{cx - 60}" y="{fulcrum_y + 70}" width="120" height="15" rx="3" fill="#1e293b" stroke="#64748b" stroke-width="2"/>',
        # Vertical Pillar
        f'<line x1="{cx}" y1="{fulcrum_y}" x2="{cx}" y2="{y_beam}" stroke="#94a3b8" stroke-width="4"/>',
        # Horizontal Beam
        f'<line x1="{cx - beam_w // 2}" y1="{y_beam}" x2="{cx + beam_w // 2}" y2="{y_beam}" stroke="#38bdf8" stroke-width="5" stroke-linecap="round"/>',
        # Center pivot
        f'<circle cx="{cx}" cy="{y_beam}" r="6" fill="#facc15"/>',
        # Left Pan strings
        f'<line x1="{cx - beam_w // 2}" y1="{y_beam}" x2="{cx - beam_w // 2 - 30}" y2="{y_beam + 60}" stroke="#94a3b8" stroke-width="1.5"/>',
        f'<line x1="{cx - beam_w // 2}" y1="{y_beam}" x2="{cx - beam_w // 2 + 30}" y2="{y_beam + 60}" stroke="#94a3b8" stroke-width="1.5"/>',
        # Left Pan
        f'<path d="M {cx - beam_w // 2 - 40} {y_beam + 60} Q {cx - beam_w // 2} {y_beam + 75} {cx - beam_w // 2 + 40} {y_beam + 60} Z" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>',
        f'<text x="{cx - beam_w // 2}" y="{y_beam + 50}" font-size="16" font-weight="700" fill="#38bdf8" text-anchor="middle">{left_label}</text>',
        # Right Pan strings
        f'<line x1="{cx + beam_w // 2}" y1="{y_beam}" x2="{cx + beam_w // 2 - 30}" y2="{y_beam + 60}" stroke="#94a3b8" stroke-width="1.5"/>',
        f'<line x1="{cx + beam_w // 2}" y1="{y_beam}" x2="{cx + beam_w // 2 + 30}" y2="{y_beam + 60}" stroke="#94a3b8" stroke-width="1.5"/>',
        # Right Pan
        f'<path d="M {cx + beam_w // 2 - 40} {y_beam + 60} Q {cx + beam_w // 2} {y_beam + 75} {cx + beam_w // 2 + 40} {y_beam + 60} Z" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>',
        f'<text x="{cx + beam_w // 2}" y="{y_beam + 50}" font-size="16" font-weight="700" fill="#facc15" text-anchor="middle">{right_label}</text>',
        # Balanced indicator badge
        f'<text x="{cx}" y="{fulcrum_y + 45}" font-size="13" font-weight="700" fill="#34d399" text-anchor="middle">BALANCED (=)</text>',
        '</svg>',
    ]
    return "\n".join(elements)


def draw_geometric_equation_straight_line_angles_svg(
    angle_1: str,
    angle_2: str,
    seed: Optional[int] = None,
    **kwargs: Any,
) -> str:
    """Renders two supplementary adjacent angles on a straight line."""
    entropy = f"<!-- s:{seed} -->\n" if seed is not None else ""
    total_w, total_h = 500, 240
    bx, by = 250, 180
    ray_len = 130

    elements = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {total_w} {total_h}" width="100%" height="auto" class="rounded-lg bg-slate-900 border border-slate-700/60 p-2">',
        entropy,
        # Straight baseline
        f'<line x1="50" y1="{by}" x2="450" y2="{by}" stroke="#94a3b8" stroke-width="2.5"/>',
        # Vertices labels
        f'<text x="45" y="{by + 20}" font-size="14" font-weight="700" fill="#94a3b8">A</text>',
        f'<text x="{bx}" y="{by + 25}" font-size="14" font-weight="700" fill="#94a3b8" text-anchor="middle">M</text>',
        f'<text x="455" y="{by + 20}" font-size="14" font-weight="700" fill="#94a3b8">B</text>',
        # Transversal ray at ~60 degrees
        f'<line x1="{bx}" y1="{by}" x2="{bx - 70}" y2="{by - 120}" stroke="#38bdf8" stroke-width="2.5"/>',
        f'<text x="{bx - 80}" y="{by - 125}" font-size="14" font-weight="700" fill="#94a3b8">C</text>',
        # Arc for angle 1 (left)
        f'<path d="M {bx - 35} {by} A 35 35 0 0 0 {bx - 20} {by - 30}" fill="none" stroke="#38bdf8" stroke-width="2"/>',
        f'<text x="{bx - 55}" y="{by - 25}" font-size="14" font-weight="700" fill="#38bdf8">{angle_1}</text>',
        # Arc for angle 2 (right)
        f'<path d="M {bx - 18} {by - 32} A 35 35 0 0 0 {bx + 35} {by}" fill="none" stroke="#facc15" stroke-width="2"/>',
        f'<text x="{bx + 35}" y="{by - 25}" font-size="14" font-weight="700" fill="#facc15">{angle_2}</text>',
        '</svg>',
    ]
    return "\n".join(elements)
