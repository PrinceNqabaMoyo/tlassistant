"""Grade 9 Mathematics - Equations 2 (Fractions & Quadratics) SVG Helpers.
Generates deterministic, accessible SVG diagrams for:
  - Balance scale with fractional algebraic terms
  - Geometric rectangle with fractional side lengths and perimeter
  - Geometric rectangle with algebraic binomial dimensions and given area

All helpers accept `seed: Optional[int] = None, **kwargs: Any` and inject entropy comments <!-- s:{seed} -->.
"""
from __future__ import annotations

from typing import Any, Optional


def draw_fraction_balance_scale_svg(
    left_label: str,
    right_label: str,
    seed: Optional[int] = None,
    **kwargs: Any,
) -> str:
    """Renders a balanced beam scale illustrating an equation with algebraic fractions."""
    entropy = f"<!-- s:{seed} -->\n" if seed is not None else ""
    total_w, total_h = 520, 260
    cx, fulcrum_y = 260, 160
    beam_w = 360
    y_beam = 90

    elements = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {total_w} {total_h}" width="100%" height="auto" class="rounded-lg bg-slate-900 border border-slate-700/60 p-2">',
        entropy,
        # Base and Fulcrum
        f'<polygon points="{cx - 30},{fulcrum_y + 70} {cx + 30},{fulcrum_y + 70} {cx},{fulcrum_y}" fill="#334155" stroke="#64748b" stroke-width="2"/>',
        f'<rect x="{cx - 65}" y="{fulcrum_y + 70}" width="130" height="15" rx="3" fill="#1e293b" stroke="#64748b" stroke-width="2"/>',
        # Vertical Pillar
        f'<line x1="{cx}" y1="{fulcrum_y}" x2="{cx}" y2="{y_beam}" stroke="#94a3b8" stroke-width="4"/>',
        # Horizontal Beam
        f'<line x1="{cx - beam_w // 2}" y1="{y_beam}" x2="{cx + beam_w // 2}" y2="{y_beam}" stroke="#38bdf8" stroke-width="5" stroke-linecap="round"/>',
        # Center pivot
        f'<circle cx="{cx}" cy="{y_beam}" r="6" fill="#facc15"/>',
        # Left Pan strings
        f'<line x1="{cx - beam_w // 2}" y1="{y_beam}" x2="{cx - beam_w // 2 - 35}" y2="{y_beam + 65}" stroke="#94a3b8" stroke-width="1.5"/>',
        f'<line x1="{cx - beam_w // 2}" y1="{y_beam}" x2="{cx - beam_w // 2 + 35}" y2="{y_beam + 65}" stroke="#94a3b8" stroke-width="1.5"/>',
        # Left Pan
        f'<path d="M {cx - beam_w // 2 - 45} {y_beam + 65} Q {cx - beam_w // 2} {y_beam + 80} {cx - beam_w // 2 + 45} {y_beam + 65} Z" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>',
        f'<text x="{cx - beam_w // 2}" y="{y_beam + 52}" font-size="15" font-weight="700" fill="#38bdf8" text-anchor="middle">{left_label}</text>',
        # Right Pan strings
        f'<line x1="{cx + beam_w // 2}" y1="{y_beam}" x2="{cx + beam_w // 2 - 35}" y2="{y_beam + 65}" stroke="#94a3b8" stroke-width="1.5"/>',
        f'<line x1="{cx + beam_w // 2}" y1="{y_beam}" x2="{cx + beam_w // 2 + 35}" y2="{y_beam + 65}" stroke="#94a3b8" stroke-width="1.5"/>',
        # Right Pan
        f'<path d="M {cx + beam_w // 2 - 45} {y_beam + 65} Q {cx + beam_w // 2} {y_beam + 80} {cx + beam_w // 2 + 45} {y_beam + 65} Z" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>',
        f'<text x="{cx + beam_w // 2}" y="{y_beam + 52}" font-size="15" font-weight="700" fill="#facc15" text-anchor="middle">{right_label}</text>',
        # Balanced indicator badge
        f'<text x="{cx}" y="{fulcrum_y + 45}" font-size="13" font-weight="700" fill="#34d399" text-anchor="middle">BALANCED (=)</text>',
        '</svg>',
    ]
    return "\n".join(elements)


def draw_fraction_rectangle_perimeter_svg(
    length_label: str,
    width_label: str,
    perimeter_label: str,
    seed: Optional[int] = None,
    **kwargs: Any,
) -> str:
    """Renders a rectangle with algebraic dimensions and indicated perimeter."""
    entropy = f"<!-- s:{seed} -->\n" if seed is not None else ""
    w, h = 480, 240
    rx, ry = 90, 50
    rw, rh = 300, 140

    elements = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" height="auto" class="rounded-lg bg-slate-900 border border-slate-700/60 p-2">',
        entropy,
        # Rectangle outline
        f'<rect x="{rx}" y="{ry}" width="{rw}" height="{rh}" rx="4" fill="#1e293b" stroke="#38bdf8" stroke-width="2.5"/>',
        # Right angle indicators
        f'<path d="M {rx} {ry + 15} L {rx + 15} {ry + 15} L {rx + 15} {ry}" fill="none" stroke="#64748b" stroke-width="1.5"/>',
        f'<path d="M {rx + rw - 15} {ry} L {rx + rw - 15} {ry + 15} L {rx + rw} {ry + 15}" fill="none" stroke="#64748b" stroke-width="1.5"/>',
        # Length label (top)
        f'<text x="{rx + rw // 2}" y="{ry - 14}" font-size="15" font-weight="700" fill="#38bdf8" text-anchor="middle">Length = {length_label}</text>',
        # Width label (left)
        f'<text x="{rx - 15}" y="{ry + rh // 2 + 5}" font-size="15" font-weight="700" fill="#38bdf8" text-anchor="end">Width = {width_label}</text>',
        # Center badge: Perimeter
        f'<rect x="{rx + rw // 2 - 70}" y="{ry + rh // 2 - 18}" width="140" height="34" rx="6" fill="#0f172a" stroke="#facc15" stroke-width="1.5"/>',
        f'<text x="{rx + rw // 2}" y="{ry + rh // 2 + 5}" font-size="14" font-weight="700" fill="#facc15" text-anchor="middle">Perimeter = {perimeter_label}</text>',
        '</svg>',
    ]
    return "\n".join(elements)


def draw_quadratic_rectangle_area_svg(
    length_label: str,
    width_label: str,
    area_label: str,
    seed: Optional[int] = None,
    **kwargs: Any,
) -> str:
    """Renders a geometric rectangle illustrating an algebraic quadratic area problem."""
    entropy = f"<!-- s:{seed} -->\n" if seed is not None else ""
    w, h = 480, 240
    rx, ry = 90, 50
    rw, rh = 300, 140

    elements = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" height="auto" class="rounded-lg bg-slate-900 border border-slate-700/60 p-2">',
        entropy,
        # Rectangle outline
        f'<rect x="{rx}" y="{ry}" width="{rw}" height="{rh}" rx="4" fill="#1e293b" stroke="#34d399" stroke-width="2.5"/>',
        # Dimensions labels
        f'<text x="{rx + rw // 2}" y="{ry - 14}" font-size="15" font-weight="700" fill="#38bdf8" text-anchor="middle">{length_label}</text>',
        f'<text x="{rx - 15}" y="{ry + rh // 2 + 5}" font-size="15" font-weight="700" fill="#38bdf8" text-anchor="end">{width_label}</text>',
        # Interior Area badge
        f'<rect x="{rx + rw // 2 - 60}" y="{ry + rh // 2 - 18}" width="120" height="34" rx="6" fill="#0f172a" stroke="#34d399" stroke-width="1.5"/>',
        f'<text x="{rx + rw // 2}" y="{ry + rh // 2 + 5}" font-size="14" font-weight="700" fill="#34d399" text-anchor="middle">Area = {area_label}</text>',
        '</svg>',
    ]
    return "\n".join(elements)
