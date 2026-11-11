"""Grade 8 Transformation Geometry SVG Generators.
Provides crisp, vector Cartesian coordinate grids and shapes illustrating:
  - Coordinate grid with original point/triangle and reflected image.
  - Coordinate grid with translated point/triangle and direction vectors.
  - Coordinate grid with rotated shape about origin.
  - Enlargement/reduction comparison on grid.

Strictly deterministic, parameter-driven SVG rendering for exam and visual companion views.
"""
from __future__ import annotations

import random
from typing import List, Tuple, Optional


def draw_transformation_grid_svg(
    orig_points: List[Tuple[float, float]],
    trans_points: Optional[List[Tuple[float, float]]] = None,
    orig_label: str = "A",
    trans_label: str = "A'",
    line_of_reflection: Optional[str] = None,
    show_vector: bool = False,
    seed: int = 101,
) -> str:
    """Renders a 10x10 Cartesian coordinate grid (-5 to 5 or -6 to 6) with points/polygons."""
    rng = random.Random(seed)
    w, h = 420, 420
    cx, cy = 210, 210
    scale = 32  # 32 px per unit, range -6 to 6

    def to_svg(x: float, y: float) -> Tuple[float, float]:
        return cx + x * scale, cy - y * scale

    lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" height="100%" style="background:#ffffff; font-family:sans-serif;">',
        '  <defs>',
        '    <marker id="arrow" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">',
        '      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#1e40af" />',
        '    </marker>',
        '    <marker id="trans_arrow" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">',
        '      <path d="M 0 2 L 6 5 L 0 8 z" fill="#b91c1c" />',
        '    </marker>',
        '  </defs>',
    ]

    # Grid lines (-6 to 6)
    for u in range(-6, 7):
        gx, _ = to_svg(u, 0)
        _, gy = to_svg(0, u)
        stroke_color = "#e2e8f0" if u != 0 else "#94a3b8"
        stroke_width = "1" if u != 0 else "1.5"
        lines.append(f'  <line x1="{gx}" y1="10" x2="{gx}" y2="{h-10}" stroke="{stroke_color}" stroke-width="{stroke_width}"/>')
        lines.append(f'  <line x1="10" y1="{gy}" x2="{w-10}" y2="{gy}" stroke="{stroke_color}" stroke-width="{stroke_width}"/>')
        # Ticks and numbers
        if u != 0 and abs(u) % 2 == 0:
            lines.append(f'  <text x="{gx}" y="{cy + 14}" font-size="10" fill="#64748b" text-anchor="middle">{u}</text>')
            lines.append(f'  <text x="{cx - 10}" y="{gy + 4}" font-size="10" fill="#64748b" text-anchor="end">{u}</text>')

    # Main Axes with arrows
    lines.append(f'  <line x1="10" y1="{cy}" x2="{w-10}" y2="{cy}" stroke="#1e293b" stroke-width="2" marker-end="url(#arrow)"/>')
    lines.append(f'  <line x1="{cx}" y1="{h-10}" x2="{cx}" y2="10" stroke="#1e293b" stroke-width="2" marker-end="url(#arrow)"/>')
    lines.append(f'  <text x="{w-15}" y="{cy-8}" font-size="12" font-weight="bold" fill="#1e293b">x</text>')
    lines.append(f'  <text x="{cx+8}" y="20" font-size="12" font-weight="bold" fill="#1e293b">y</text>')
    lines.append(f'  <text x="{cx-8}" y="{cy+14}" font-size="10" fill="#64748b">O</text>')

    # Optional Line of reflection
    if line_of_reflection == "x-axis":
        lines.append(f'  <line x1="10" y1="{cy}" x2="{w-10}" y2="{cy}" stroke="#dc2626" stroke-width="2" stroke-dasharray="4,4"/>')
        lines.append(f'  <text x="{w-55}" y="{cy-12}" font-size="11" font-weight="bold" fill="#dc2626">Mirror (x-axis)</text>')
    elif line_of_reflection == "y-axis":
        lines.append(f'  <line x1="{cx}" y1="10" x2="{cx}" y2="{h-10}" stroke="#dc2626" stroke-width="2" stroke-dasharray="4,4"/>')
        lines.append(f'  <text x="{cx+12}" y="35" font-size="11" font-weight="bold" fill="#dc2626">Mirror (y-axis)</text>')
    elif line_of_reflection == "y=x":
        p1 = to_svg(-5.5, -5.5)
        p2 = to_svg(5.5, 5.5)
        lines.append(f'  <line x1="{p1[0]}" y1="{p1[1]}" x2="{p2[0]}" y2="{p2[1]}" stroke="#dc2626" stroke-width="2" stroke-dasharray="4,4"/>')
        lines.append(f'  <text x="{p2[0]-45}" y="{p2[1]+15}" font-size="11" font-weight="bold" fill="#dc2626">Line y = x</text>')

    # Draw original figure
    if len(orig_points) == 1:
        ox, oy = to_svg(orig_points[0][0], orig_points[0][1])
        lines.append(f'  <circle cx="{ox}" cy="{oy}" r="5" fill="#2563eb" stroke="#1e40af" stroke-width="1.5"/>')
        lines.append(f'  <text x="{ox+8}" y="{oy-8}" font-size="12" font-weight="bold" fill="#1e40af">{orig_label}({orig_points[0][0]:.0f}, {orig_points[0][1]:.0f})</text>')
    elif len(orig_points) > 1:
        pts_str = " ".join(f"{to_svg(px, py)[0]},{to_svg(px, py)[1]}" for px, py in orig_points)
        lines.append(f'  <polygon points="{pts_str}" fill="rgba(37, 99, 235, 0.15)" stroke="#2563eb" stroke-width="2"/>')
        labels = ["A", "B", "C", "D"]
        for i, (px, py) in enumerate(orig_points):
            sx, sy = to_svg(px, py)
            lbl = labels[i] if i < len(labels) else f"P{i+1}"
            lines.append(f'  <circle cx="{sx}" cy="{sy}" r="4" fill="#2563eb"/>')
            lines.append(f'  <text x="{sx+6}" y="{sy-6}" font-size="11" font-weight="bold" fill="#1e40af">{lbl}({px:.0f},{py:.0f})</text>')

    # Draw transformed figure
    if trans_points:
        if len(trans_points) == 1:
            tx, ty = to_svg(trans_points[0][0], trans_points[0][1])
            lines.append(f'  <circle cx="{tx}" cy="{ty}" r="5" fill="#16a34a" stroke="#15803d" stroke-width="1.5"/>')
            lines.append(f'  <text x="{tx+8}" y="{ty-8}" font-size="12" font-weight="bold" fill="#15803d">{trans_label}({trans_points[0][0]:.0f}, {trans_points[0][1]:.0f})</text>')
            if show_vector and len(orig_points) == 1:
                ox, oy = to_svg(orig_points[0][0], orig_points[0][1])
                lines.append(f'  <line x1="{ox}" y1="{oy}" x2="{tx}" y2="{ty}" stroke="#b91c1c" stroke-width="1.5" stroke-dasharray="3,3" marker-end="url(#trans_arrow)"/>')
        elif len(trans_points) > 1:
            pts_str = " ".join(f"{to_svg(px, py)[0]},{to_svg(px, py)[1]}" for px, py in trans_points)
            lines.append(f'  <polygon points="{pts_str}" fill="rgba(22, 163, 74, 0.15)" stroke="#16a34a" stroke-width="2"/>')
            labels = ["A'", "B'", "C'", "D'"]
            for i, (px, py) in enumerate(trans_points):
                sx, sy = to_svg(px, py)
                lbl = labels[i] if i < len(labels) else f"P'{i+1}"
                lines.append(f'  <circle cx="{sx}" cy="{sy}" r="4" fill="#16a34a"/>')
                lines.append(f'  <text x="{sx+6}" y="{sy-6}" font-size="11" font-weight="bold" fill="#15803d">{lbl}({px:.0f},{py:.0f})</text>')
            if show_vector and len(orig_points) == len(trans_points):
                # vector from first vertex to first transformed vertex
                ox, oy = to_svg(orig_points[0][0], orig_points[0][1])
                tx, ty = to_svg(trans_points[0][0], trans_points[0][1])
                lines.append(f'  <line x1="{ox}" y1="{oy}" x2="{tx}" y2="{ty}" stroke="#b91c1c" stroke-width="1.5" stroke-dasharray="3,3" marker-end="url(#trans_arrow)"/>')

    lines.append('</svg>')
    return "\n".join(lines)


def draw_symmetry_polygon_svg(poly_type: str = "square", seed: int = 101) -> str:
    """Renders a 2D shape with marked lines of symmetry."""
    rng = random.Random(seed)
    w, h = 320, 240
    lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" height="100%" style="background:#ffffff; font-family:sans-serif;">',
        '  <defs>',
        '    <style>',
        '      .sym-line { stroke: #dc2626; stroke-width: 1.5; stroke-dasharray: 4,3; }',
        '      .shape-stroke { stroke: #2563eb; stroke-width: 2.5; fill: rgba(37, 99, 235, 0.08); }',
        '    </style>',
        '  </defs>',
    ]

    if poly_type == "square":
        # Square 120x120 centered at (160, 120)
        lines.append('  <rect x="100" y="60" width="120" height="120" class="shape-stroke"/>')
        # 4 lines of symmetry
        lines.append('  <line x1="160" y1="40" x2="160" y2="200" class="sym-line"/>')  # vertical
        lines.append('  <line x1="80" y1="120" x2="240" y2="120" class="sym-line"/>')  # horizontal
        lines.append('  <line x1="85" y1="45" x2="235" y2="195" class="sym-line"/>')    # diagonal 1
        lines.append('  <line x1="85" y1="195" x2="235" y2="45" class="sym-line"/>')    # diagonal 2
        lines.append('  <text x="160" y="225" font-size="12" font-weight="bold" fill="#1e293b" text-anchor="middle">Square (4 Axes of Symmetry)</text>')
    elif poly_type == "rectangle":
        lines.append('  <rect x="90" y="80" width="140" height="80" class="shape-stroke"/>')
        lines.append('  <line x1="160" y1="60" x2="160" y2="180" class="sym-line"/>')  # vertical
        lines.append('  <line x1="70" y1="120" x2="250" y2="120" class="sym-line"/>')  # horizontal
        lines.append('  <text x="160" y="215" font-size="12" font-weight="bold" fill="#1e293b" text-anchor="middle">Rectangle (2 Axes of Symmetry)</text>')
    elif poly_type == "equilateral_triangle":
        lines.append('  <polygon points="160,50 90,170 230,170" class="shape-stroke"/>')
        lines.append('  <line x1="160" y1="35" x2="160" y2="185" class="sym-line"/>')
        lines.append('  <line x1="80" y1="175" x2="200" y2="105" class="sym-line"/>')
        lines.append('  <line x1="240" y1="175" x2="120" y2="105" class="sym-line"/>')
        lines.append('  <text x="160" y="215" font-size="12" font-weight="bold" fill="#1e293b" text-anchor="middle">Equilateral Triangle (3 Axes of Symmetry)</text>')
    else:  # isosceles triangle
        lines.append('  <polygon points="160,50 110,180 210,180" class="shape-stroke"/>')
        lines.append('  <line x1="160" y1="35" x2="160" y2="195" class="sym-line"/>')
        lines.append('  <text x="160" y="220" font-size="12" font-weight="bold" fill="#1e293b" text-anchor="middle">Isosceles Triangle (1 Axis of Symmetry)</text>')

    lines.append('</svg>')
    return "\n".join(lines)
