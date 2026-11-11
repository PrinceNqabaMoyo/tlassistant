"""Grade 9 Mathematics - Geometry of Straight Lines SVG Helpers.
Generates deterministic, accessible SVG diagrams for:
  - Two intersecting straight lines (vertically opposite & adjacent angles)
  - Straight line with adjacent angles (rays from baseline)
  - Angles around a point (revolution)
  - Two parallel lines cut by a transversal with parallel arrows
  - Zigzag parallel lines with intermediate vertex (auxiliary line)

All helpers accept `seed: Optional[int] = None, **kwargs: Any` and inject entropy comments <!-- s:{seed} -->.
"""
from __future__ import annotations

import math
from typing import Any, Dict, List, Optional, Tuple


def draw_intersecting_lines_svg(
    angle_labels: Dict[str, str],
    center_label: str = "O",
    seed: Optional[int] = None,
    **kwargs: Any,
) -> str:
    """Renders two intersecting straight lines forming 4 angles.
    angle_labels can contain keys 'O1', 'O2', 'O3', 'O4' or 'top', 'right', 'bottom', 'left'.
    """
    entropy = f"<!-- s:{seed} -->\n" if seed is not None else ""
    w, h = 480, 300
    cx, cy = 240, 150
    length = 190

    # Line 1: from top-left to bottom-right (~35 deg slant)
    # Line 2: from bottom-left to top-right (~145 deg slant)
    rad1 = math.radians(35)
    rad2 = math.radians(145)

    x1a, y1a = cx - length * math.cos(rad1), cy + length * math.sin(rad1)
    x1b, y1b = cx + length * math.cos(rad1), cy - length * math.sin(rad1)

    x2a, y2a = cx - length * math.cos(rad2), cy + length * math.sin(rad2)
    x2b, y2b = cx + length * math.cos(rad2), cy - length * math.sin(rad2)

    top_label = angle_labels.get("O1") or angle_labels.get("top", "")
    right_label = angle_labels.get("O2") or angle_labels.get("right", "")
    bottom_label = angle_labels.get("O3") or angle_labels.get("bottom", "")
    left_label = angle_labels.get("O4") or angle_labels.get("left", "")

    elements = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" height="auto" class="rounded-lg bg-slate-900 border border-slate-700/60 p-2">',
        entropy,
        # Line AB
        f'<line x1="{x1a:.1f}" y1="{y1a:.1f}" x2="{x1b:.1f}" y2="{y1b:.1f}" stroke="#94a3b8" stroke-width="2.5" stroke-linecap="round"/>',
        f'<text x="{x1a - 15:.1f}" y="{y1a + 15:.1f}" font-size="14" font-weight="700" fill="#94a3b8">A</text>',
        f'<text x="{x1b + 10:.1f}" y="{y1b - 5:.1f}" font-size="14" font-weight="700" fill="#94a3b8">B</text>',
        # Line CD
        f'<line x1="{x2a:.1f}" y1="{y2a:.1f}" x2="{x2b:.1f}" y2="{y2b:.1f}" stroke="#94a3b8" stroke-width="2.5" stroke-linecap="round"/>',
        f'<text x="{x2a + 10:.1f}" y="{y2a + 15:.1f}" font-size="14" font-weight="700" fill="#94a3b8">D</text>',
        f'<text x="{x2b - 15:.1f}" y="{y2b - 5:.1f}" font-size="14" font-weight="700" fill="#94a3b8">C</text>',
        # Center vertex O
        f'<circle cx="{cx}" cy="{cy}" r="4" fill="#38bdf8"/>',
        f'<text x="{cx + 12}" y="{cy + 16}" font-size="13" font-weight="700" fill="#cbd5e1">{center_label}</text>',
    ]

    # Arcs and labels
    if top_label:
        elements.append(f'<path d="M {cx - 24} {cy - 14} Q {cx} {cy - 32} {cx + 24} {cy - 14}" fill="none" stroke="#38bdf8" stroke-width="2"/>')
        elements.append(f'<text x="{cx}" y="{cy - 38}" font-size="14" font-weight="700" fill="#38bdf8" text-anchor="middle">{top_label}</text>')
    if bottom_label:
        elements.append(f'<path d="M {cx - 24} {cy + 14} Q {cx} {cy + 32} {cx + 24} {cy + 14}" fill="none" stroke="#38bdf8" stroke-width="2"/>')
        elements.append(f'<text x="{cx}" y="{cy + 48}" font-size="14" font-weight="700" fill="#38bdf8" text-anchor="middle">{bottom_label}</text>')
    if right_label:
        elements.append(f'<path d="M {cx + 20} {cy - 18} Q {cx + 36} {cy} {cx + 20} {cy + 18}" fill="none" stroke="#facc15" stroke-width="2"/>')
        elements.append(f'<text x="{cx + 56}" y="{cy + 5}" font-size="14" font-weight="700" fill="#facc15" text-anchor="start">{right_label}</text>')
    if left_label:
        elements.append(f'<path d="M {cx - 20} {cy - 18} Q {cx - 36} {cy} {cx - 20} {cy + 18}" fill="none" stroke="#facc15" stroke-width="2"/>')
        elements.append(f'<text x="{cx - 56}" y="{cy + 5}" font-size="14" font-weight="700" fill="#facc15" text-anchor="end">{left_label}</text>')

    elements.append("</svg>")
    return "\n".join(elements)


def draw_straight_line_adjacent_angles_svg(
    angle_1: str,
    angle_2: str,
    angle_3: Optional[str] = None,
    ray_angle_deg: float = 60.0,
    seed: Optional[int] = None,
    **kwargs: Any,
) -> str:
    """Renders a straight baseline with one or two rays originating from point M."""
    entropy = f"<!-- s:{seed} -->\n" if seed is not None else ""
    w, h = 480, 240
    bx, by = 240, 175
    line_w = 180

    elements = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" height="auto" class="rounded-lg bg-slate-900 border border-slate-700/60 p-2">',
        entropy,
        # Baseline AB
        f'<line x1="{bx - line_w}" y1="{by}" x2="{bx + line_w}" y2="{by}" stroke="#94a3b8" stroke-width="2.5" stroke-linecap="round"/>',
        f'<text x="{bx - line_w - 15}" y="{by + 5}" font-size="14" font-weight="700" fill="#94a3b8">A</text>',
        f'<text x="{bx}" y="{by + 22}" font-size="13" font-weight="700" fill="#cbd5e1" text-anchor="middle">M</text>',
        f'<text x="{bx + line_w + 15}" y="{by + 5}" font-size="14" font-weight="700" fill="#94a3b8">B</text>',
        f'<circle cx="{bx}" cy="{by}" r="4" fill="#38bdf8"/>',
    ]

    if angle_3 is None:
        # Single ray MC
        rad = math.radians(ray_angle_deg)
        ray_len = 120
        rx, ry = bx + ray_len * math.cos(math.pi - rad), by - ray_len * math.sin(rad)
        elements.extend([
            f'<line x1="{bx}" y1="{by}" x2="{rx:.1f}" y2="{ry:.1f}" stroke="#38bdf8" stroke-width="2.5" stroke-linecap="round"/>',
            f'<text x="{rx:.1f}" y="{ry - 8:.1f}" font-size="14" font-weight="700" fill="#38bdf8" text-anchor="middle">C</text>',
            # Left arc (angle_1)
            f'<path d="M {bx - 36} {by} A 36 36 0 0 0 {bx + 36 * math.cos(math.pi - rad):.1f} {by - 36 * math.sin(rad):.1f}" fill="none" stroke="#38bdf8" stroke-width="2"/>',
            f'<text x="{bx - 55}" y="{by - 25}" font-size="14" font-weight="700" fill="#38bdf8" text-anchor="middle">{angle_1}</text>',
            # Right arc (angle_2)
            f'<path d="M {bx + 36 * math.cos(math.pi - rad):.1f} {by - 36 * math.sin(rad):.1f} A 36 36 0 0 0 {bx + 36} {by}" fill="none" stroke="#facc15" stroke-width="2"/>',
            f'<text x="{bx + 55}" y="{by - 25}" font-size="14" font-weight="700" fill="#facc15" text-anchor="middle">{angle_2}</text>',
        ])
    else:
        # Two rays: C at 120 deg, D at 55 deg
        rad1, rad2 = math.radians(120), math.radians(55)
        ray_len = 115
        r1x, r1y = bx + ray_len * math.cos(math.pi - rad1), by - ray_len * math.sin(rad1)
        r2x, r2y = bx + ray_len * math.cos(math.pi - rad2), by - ray_len * math.sin(rad2)
        elements.extend([
            f'<line x1="{bx}" y1="{by}" x2="{r1x:.1f}" y2="{r1y:.1f}" stroke="#38bdf8" stroke-width="2" stroke-linecap="round"/>',
            f'<text x="{r1x - 5:.1f}" y="{r1y - 8:.1f}" font-size="13" font-weight="700" fill="#38bdf8">C</text>',
            f'<line x1="{bx}" y1="{by}" x2="{r2x:.1f}" y2="{r2y:.1f}" stroke="#a78bfa" stroke-width="2" stroke-linecap="round"/>',
            f'<text x="{r2x + 5:.1f}" y="{r2y - 8:.1f}" font-size="13" font-weight="700" fill="#a78bfa">D</text>',
            # Arc 1
            f'<text x="{bx - 60}" y="{by - 18}" font-size="13" font-weight="700" fill="#38bdf8">{angle_1}</text>',
            # Arc 2 (middle)
            f'<text x="{bx}" y="{by - 55}" font-size="13" font-weight="700" fill="#facc15" text-anchor="middle">{angle_2}</text>',
            # Arc 3 (right)
            f'<text x="{bx + 60}" y="{by - 18}" font-size="13" font-weight="700" fill="#34d399">{angle_3}</text>',
        ])

    elements.append("</svg>")
    return "\n".join(elements)


def draw_angles_around_point_svg(
    angles: List[str],
    center_label: str = "O",
    seed: Optional[int] = None,
    **kwargs: Any,
) -> str:
    """Renders 3 or 4 angles around a point summing to 360 degrees."""
    entropy = f"<!-- s:{seed} -->\n" if seed is not None else ""
    w, h = 420, 300
    cx, cy = 210, 150
    ray_len = 105

    n = len(angles)
    step_deg = 360.0 / n
    colors = ["#38bdf8", "#facc15", "#34d399", "#f43f5e"]

    elements = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" height="auto" class="rounded-lg bg-slate-900 border border-slate-700/60 p-2">',
        entropy,
        f'<circle cx="{cx}" cy="{cy}" r="4" fill="#cbd5e1"/>',
        f'<text x="{cx + 10}" y="{cy + 15}" font-size="13" font-weight="700" fill="#94a3b8">{center_label}</text>',
    ]

    for i in range(n):
        ang_deg = i * step_deg
        rad = math.radians(ang_deg)
        rx = cx + ray_len * math.cos(rad)
        ry = cy - ray_len * math.sin(rad)
        elements.append(f'<line x1="{cx}" y1="{cy}" x2="{rx:.1f}" y2="{ry:.1f}" stroke="#64748b" stroke-width="2"/>')

        # Mid angle for label
        mid_deg = ang_deg + step_deg / 2
        mid_rad = math.radians(mid_deg)
        lx = cx + 55 * math.cos(mid_rad)
        ly = cy - 55 * math.sin(mid_rad)
        col = colors[i % len(colors)]
        elements.append(f'<text x="{lx:.1f}" y="{ly + 5:.1f}" font-size="13" font-weight="700" fill="{col}" text-anchor="middle">{angles[i]}</text>')

    elements.append("</svg>")
    return "\n".join(elements)


def draw_parallel_transversal_svg(
    angle_positions: Dict[str, str],
    line1_name: str = "AB",
    line2_name: str = "CD",
    transversal_name: str = "EF",
    seed: Optional[int] = None,
    **kwargs: Any,
) -> str:
    """Renders two horizontal parallel lines with arrows cut by a transversal.
    angle_positions maps position names:
      'G1' (top-left of top line), 'G2' (top-right), 'G3' (bottom-left), 'G4' (bottom-right)
      'H1' (top-left of bottom line), 'H2' (top-right), 'H3' (bottom-left), 'H4' (bottom-right)
    """
    entropy = f"<!-- s:{seed} -->\n" if seed is not None else ""
    w, h = 520, 320
    y1, y2 = 100, 220
    x_start, x_end = 70, 450

    # Transversal line through (170, 40) and (350, 280)
    tx1, ty1 = 160, 40
    tx2, ty2 = 360, 280

    # Intersection points G (with line 1) and H (with line 2)
    # y = y1 = 100: t = (100 - 40)/(280 - 40) = 60/240 = 0.25 => gx = 160 + 0.25*(200) = 210
    gx, gy = 210, y1
    # y = y2 = 220: t = (220 - 40)/(240) = 180/240 = 0.75 => hx = 160 + 0.75*(200) = 310
    hx, hy = 310, y2

    elements = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" height="auto" class="rounded-lg bg-slate-900 border border-slate-700/60 p-2">',
        entropy,
        # Line 1 (AB)
        f'<line x1="{x_start}" y1="{y1}" x2="{x_end}" y2="{y1}" stroke="#94a3b8" stroke-width="2.5" stroke-linecap="round"/>',
        f'<text x="{x_start - 15}" y="{y1 + 5}" font-size="14" font-weight="700" fill="#94a3b8">{line1_name[0]}</text>',
        f'<text x="{x_end + 10}" y="{y1 + 5}" font-size="14" font-weight="700" fill="#94a3b8">{line1_name[1]}</text>',
        # Parallel arrow on line 1
        f'<path d="M {x_end - 60} {y1 - 6} L {x_end - 50} {y1} L {x_end - 60} {y1 + 6}" fill="none" stroke="#38bdf8" stroke-width="2.5"/>',
        # Line 2 (CD)
        f'<line x1="{x_start}" y1="{y2}" x2="{x_end}" y2="{y2}" stroke="#94a3b8" stroke-width="2.5" stroke-linecap="round"/>',
        f'<text x="{x_start - 15}" y="{y2 + 5}" font-size="14" font-weight="700" fill="#94a3b8">{line2_name[0]}</text>',
        f'<text x="{x_end + 10}" y="{y2 + 5}" font-size="14" font-weight="700" fill="#94a3b8">{line2_name[1]}</text>',
        # Parallel arrow on line 2
        f'<path d="M {x_end - 60} {y2 - 6} L {x_end - 50} {y2} L {x_end - 60} {y2 + 6}" fill="none" stroke="#38bdf8" stroke-width="2.5"/>',
        # Transversal line (EF)
        f'<line x1="{tx1}" y1="{ty1}" x2="{tx2}" y2="{ty2}" stroke="#cbd5e1" stroke-width="2" stroke-linecap="round"/>',
        f'<text x="{tx1 - 5}" y="{ty1 - 10}" font-size="14" font-weight="700" fill="#cbd5e1">{transversal_name[0]}</text>',
        f'<text x="{tx2 + 5}" y="{ty2 + 15}" font-size="14" font-weight="700" fill="#cbd5e1">{transversal_name[1]}</text>',
        # Intersection labels G and H
        f'<circle cx="{gx}" cy="{gy}" r="3.5" fill="#38bdf8"/>',
        f'<text x="{gx - 18}" y="{gy - 15}" font-size="12" font-weight="700" fill="#94a3b8">G</text>',
        f'<circle cx="{hx}" cy="{hy}" r="3.5" fill="#38bdf8"/>',
        f'<text x="{hx - 18}" y="{hy - 15}" font-size="12" font-weight="700" fill="#94a3b8">H</text>',
    ]

    # Positions around G
    pos_coords = {
        "G1": (gx - 35, gy - 16, "#38bdf8"),
        "G2": (gx + 30, gy - 16, "#facc15"),
        "G3": (gx - 30, gy + 22, "#facc15"),
        "G4": (gx + 30, gy + 22, "#38bdf8"),
        "H1": (hx - 35, hy - 16, "#38bdf8"),
        "H2": (hx + 30, hy - 16, "#facc15"),
        "H3": (hx - 30, hy + 22, "#facc15"),
        "H4": (hx + 30, hy + 22, "#38bdf8"),
    }

    for pos, label in angle_positions.items():
        if pos in pos_coords and label:
            x, y, col = pos_coords[pos]
            elements.append(f'<text x="{x}" y="{y}" font-size="14" font-weight="700" fill="{col}" text-anchor="middle">{label}</text>')

    elements.append("</svg>")
    return "\n".join(elements)


def draw_parallel_zigzag_svg(
    top_angle: str,
    mid_angle: str,
    bottom_angle: str,
    seed: Optional[int] = None,
    **kwargs: Any,
) -> str:
    """Renders parallel lines AB and CD with an internal zigzag vertex P."""
    entropy = f"<!-- s:{seed} -->\n" if seed is not None else ""
    w, h = 480, 260
    y1, y2 = 60, 200
    px, py = 200, 130

    elements = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" height="auto" class="rounded-lg bg-slate-900 border border-slate-700/60 p-2">',
        entropy,
        # Line 1 (AB)
        f'<line x1="60" y1="{y1}" x2="420" y2="{y1}" stroke="#94a3b8" stroke-width="2.5" stroke-linecap="round"/>',
        f'<text x="45" y="{y1 + 5}" font-size="14" font-weight="700" fill="#94a3b8">A</text>',
        f'<text x="430" y="{y1 + 5}" font-size="14" font-weight="700" fill="#94a3b8">B</text>',
        f'<path d="M 360 {y1 - 5} L 370 {y1} L 360 {y1 + 5}" fill="none" stroke="#38bdf8" stroke-width="2"/>',
        # Line 2 (CD)
        f'<line x1="60" y1="{y2}" x2="420" y2="{y2}" stroke="#94a3b8" stroke-width="2.5" stroke-linecap="round"/>',
        f'<text x="45" y="{y2 + 5}" font-size="14" font-weight="700" fill="#94a3b8">C</text>',
        f'<text x="430" y="{y2 + 5}" font-size="14" font-weight="700" fill="#94a3b8">D</text>',
        f'<path d="M 360 {y2 - 5} L 370 {y2} L 360 {y2 + 5}" fill="none" stroke="#38bdf8" stroke-width="2"/>',
        # Zigzag rays: from (120, y1) to P, and from P to (300, y2)
        f'<line x1="130" y1="{y1}" x2="{px}" y2="{py}" stroke="#38bdf8" stroke-width="2.5"/>',
        f'<line x1="{px}" y1="{py}" x2="300" y2="{y2}" stroke="#38bdf8" stroke-width="2.5"/>',
        f'<circle cx="{px}" cy="{py}" r="4" fill="#facc15"/>',
        f'<text x="{px - 20}" y="{py + 5}" font-size="14" font-weight="700" fill="#facc15">P</text>',
        # Auxiliary dashed parallel line through P
        f'<line x1="100" y1="{py}" x2="380" y2="{py}" stroke="#64748b" stroke-width="1.5" stroke-dasharray="4,4"/>',
        # Angle labels
        f'<text x="155" y="{y1 + 22}" font-size="13" font-weight="700" fill="#38bdf8">{top_angle}</text>',
        f'<text x="{px + 30}" y="{py + 5}" font-size="14" font-weight="700" fill="#facc15">{mid_angle}</text>',
        f'<text x="270" y="{y2 - 12}" font-size="13" font-weight="700" fill="#34d399">{bottom_angle}</text>',
        '</svg>',
    ]
    return "\n".join(elements)
