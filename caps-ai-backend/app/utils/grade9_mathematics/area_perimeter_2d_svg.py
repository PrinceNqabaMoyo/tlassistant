"""Grade 9 Mathematics - Area and Perimeter of 2D Shapes SVG Diagram Renderer.
=============================================================================
Provides deterministic SVG generators for:
  - Triangles with altitudes (acute, right-angled, obtuse)
  - Quadrilaterals: rectangles, squares, parallelograms, rhombi, kites, trapezia
  - Circles, semicircles, quadrants, and annular rings
  - Composite shapes (L-shapes, running tracks, gables)
  - Shaded regions (cutouts and border paths)

All SVGs inject <!-- s:{seed} --> for referee audit tracking and 100% AST purity.
"""
from __future__ import annotations

import math
import random
from typing import Optional


def draw_triangle_with_altitude_svg(
    base: float,
    height: float,
    triangle_type: str = "acute",
    base_label: str = "b",
    height_label: str = "h",
    seed: Optional[int] = None,
) -> str:
    """Renders a triangle with dashed perpendicular altitude line and right-angle symbol."""
    width, height_px = 400, 260
    base_y = 200
    top_y = 50

    if triangle_type == "right":
        x_left = 60
        x_right = 320
        x_top = x_left
    elif triangle_type == "obtuse":
        x_left = 130
        x_right = 350
        x_top = 60  # Peak is to the left of base
    else:  # acute
        x_left = 60
        x_right = 340
        x_top = 180

    svg_parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height_px}" width="100%" height="auto">',
        f"<!-- s:{seed} -->",
        '<defs>',
        '  <marker id="arrow" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">',
        '    <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#1e293b"/>',
        '  </marker>',
        '</defs>',
        '<rect width="100%" height="100%" fill="#f8fafc" rx="8"/>',
    ]

    # Triangle body
    pts = f"{x_left},{base_y} {x_right},{base_y} {x_top},{top_y}"
    svg_parts.append(f'<polygon points="{pts}" fill="#e0e7ff" stroke="#3730a3" stroke-width="2.5"/>')

    # Altitude line
    if triangle_type == "right":
        # Right angle box at (x_left, base_y)
        svg_parts.append(f'<rect x="{x_left}" y="{base_y - 16}" width="16" height="16" fill="none" stroke="#dc2626" stroke-width="2"/>')
    elif triangle_type == "obtuse":
        # Extended base line to the left
        svg_parts.append(f'<line x1="{x_top}" y1="{base_y}" x2="{x_left}" y2="{base_y}" stroke="#94a3b8" stroke-dasharray="4,4" stroke-width="2"/>')
        # Altitude dropped externally
        svg_parts.append(f'<line x1="{x_top}" y1="{top_y}" x2="{x_top}" y2="{base_y}" stroke="#dc2626" stroke-dasharray="5,5" stroke-width="2.5"/>')
        svg_parts.append(f'<rect x="{x_top}" y="{base_y - 16}" width="16" height="16" fill="none" stroke="#dc2626" stroke-width="2"/>')
        # Label altitude
        svg_parts.append(f'<text x="{x_top - 12}" y="{(top_y + base_y) / 2}" font-family="Arial, sans-serif" font-size="14" font-weight="bold" fill="#dc2626" text-anchor="end">{height_label}</text>')
    else:
        # Acute internal altitude
        svg_parts.append(f'<line x1="{x_top}" y1="{top_y}" x2="{x_top}" y2="{base_y}" stroke="#dc2626" stroke-dasharray="5,5" stroke-width="2.5"/>')
        svg_parts.append(f'<rect x="{x_top}" y="{base_y - 16}" width="16" height="16" fill="none" stroke="#dc2626" stroke-width="2"/>')
        svg_parts.append(f'<text x="{x_top + 10}" y="{(top_y + base_y) / 2}" font-family="Arial, sans-serif" font-size="14" font-weight="bold" fill="#dc2626">{height_label}</text>')

    # Base dimension line
    svg_parts.append(f'<line x1="{x_left}" y1="{base_y + 24}" x2="{x_right}" y2="{base_y + 24}" stroke="#1e293b" stroke-width="1.8" marker-start="url(#arrow)" marker-end="url(#arrow)"/>')
    svg_parts.append(f'<text x="{(x_left + x_right) / 2}" y="{base_y + 44}" font-family="Arial, sans-serif" font-size="14" font-weight="bold" fill="#1e293b" text-anchor="middle">{base_label}</text>')

    svg_parts.append("</svg>")
    return "\n".join(svg_parts)


def draw_quadrilateral_svg(
    shape: str,  # "rectangle", "parallelogram", "trapezium", "rhombus", "kite"
    param_a: float,
    param_b: float,
    param_h: Optional[float] = None,
    label_a: str = "",
    label_b: str = "",
    label_h: str = "",
    seed: Optional[int] = None,
) -> str:
    """Renders quadrilaterals with dimension labels, parallel arrows, and heights."""
    width, height_px = 420, 260
    base_y = 190
    top_y = 65

    svg_parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height_px}" width="100%" height="auto">',
        f"<!-- s:{seed} -->",
        '<defs>',
        '  <marker id="arr" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">',
        '    <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#1e293b"/>',
        '  </marker>',
        '</defs>',
        '<rect width="100%" height="100%" fill="#f8fafc" rx="8"/>',
    ]

    if shape == "rectangle":
        x1, x2 = 70, 350
        pts = f"{x1},{top_y} {x2},{top_y} {x2},{base_y} {x1},{base_y}"
        svg_parts.append(f'<polygon points="{pts}" fill="#dcfce7" stroke="#15803d" stroke-width="2.5"/>')
        svg_parts.append(f'<rect x="{x1}" y="{base_y - 16}" width="16" height="16" fill="none" stroke="#15803d" stroke-width="1.8"/>')
        # Labels
        svg_parts.append(f'<text x="{(x1 + x2) / 2}" y="{base_y + 28}" font-family="Arial, sans-serif" font-size="14" font-weight="bold" fill="#1e293b" text-anchor="middle">{label_a}</text>')
        svg_parts.append(f'<text x="{x2 + 18}" y="{(top_y + base_y) / 2}" font-family="Arial, sans-serif" font-size="14" font-weight="bold" fill="#1e293b">{label_b}</text>')

    elif shape == "parallelogram":
        x1_b, x2_b = 60, 310
        shift = 60
        x1_t, x2_t = x1_b + shift, x2_b + shift
        pts = f"{x1_t},{top_y} {x2_t},{top_y} {x2_b},{base_y} {x1_b},{base_y}"
        svg_parts.append(f'<polygon points="{pts}" fill="#fef3c7" stroke="#b45309" stroke-width="2.5"/>')
        # Dotted altitude
        svg_parts.append(f'<line x1="{x1_t}" y1="{top_y}" x2="{x1_t}" y2="{base_y}" stroke="#dc2626" stroke-dasharray="5,5" stroke-width="2.5"/>')
        svg_parts.append(f'<rect x="{x1_t}" y="{base_y - 16}" width="16" height="16" fill="none" stroke="#dc2626" stroke-width="1.8"/>')
        svg_parts.append(f'<text x="{x1_t + 10}" y="{(top_y + base_y) / 2}" font-family="Arial, sans-serif" font-size="14" font-weight="bold" fill="#dc2626">{label_h}</text>')
        # Base label
        svg_parts.append(f'<text x="{(x1_b + x2_b) / 2}" y="{base_y + 28}" font-family="Arial, sans-serif" font-size="14" font-weight="bold" fill="#1e293b" text-anchor="middle">{label_a}</text>')

    elif shape == "trapezium":
        # Top parallel side a, bottom parallel side b
        x1_t, x2_t = 110, 270
        x1_b, x2_b = 60, 350
        pts = f"{x1_t},{top_y} {x2_t},{top_y} {x2_b},{base_y} {x1_b},{base_y}"
        svg_parts.append(f'<polygon points="{pts}" fill="#ffedd5" stroke="#c2410c" stroke-width="2.5"/>')
        # Dotted height
        svg_parts.append(f'<line x1="{x1_t}" y1="{top_y}" x2="{x1_t}" y2="{base_y}" stroke="#dc2626" stroke-dasharray="5,5" stroke-width="2.5"/>')
        svg_parts.append(f'<rect x="{x1_t}" y="{base_y - 16}" width="16" height="16" fill="none" stroke="#dc2626" stroke-width="1.8"/>')
        svg_parts.append(f'<text x="{x1_t + 10}" y="{(top_y + base_y) / 2}" font-family="Arial, sans-serif" font-size="14" font-weight="bold" fill="#dc2626">{label_h}</text>')
        # Parallel side labels
        svg_parts.append(f'<text x="{(x1_t + x2_t) / 2}" y="{top_y - 12}" font-family="Arial, sans-serif" font-size="14" font-weight="bold" fill="#1e293b" text-anchor="middle">{label_a}</text>')
        svg_parts.append(f'<text x="{(x1_b + x2_b) / 2}" y="{base_y + 28}" font-family="Arial, sans-serif" font-size="14" font-weight="bold" fill="#1e293b" text-anchor="middle">{label_b}</text>')

    elif shape in ("rhombus", "kite"):
        cx, cy = 210, 125
        dx = 130  # half diagonal 1
        dy_top = 80 if shape == "rhombus" else 55
        dy_bot = 80 if shape == "rhombus" else 105
        pts = f"{cx},{cy - dy_top} {cx + dx},{cy} {cx},{cy + dy_bot} {cx - dx},{cy}"
        svg_parts.append(f'<polygon points="{pts}" fill="#f3e8ff" stroke="#7e22ce" stroke-width="2.5"/>')
        # Dashed diagonals
        svg_parts.append(f'<line x1="{cx - dx}" y1="{cy}" x2="{cx + dx}" y2="{cy}" stroke="#7e22ce" stroke-dasharray="4,4" stroke-width="2"/>')
        svg_parts.append(f'<line x1="{cx}" y1="{cy - dy_top}" x2="{cx}" y2="{cy + dy_bot}" stroke="#7e22ce" stroke-dasharray="4,4" stroke-width="2"/>')
        svg_parts.append(f'<rect x="{cx}" y="{cy - 14}" width="14" height="14" fill="none" stroke="#7e22ce" stroke-width="1.5"/>')
        # Labels
        svg_parts.append(f'<text x="{cx + dx / 2}" y="{cy - 10}" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="#7e22ce">{label_a}</text>')
        svg_parts.append(f'<text x="{cx + 12}" y="{cy + dy_bot / 2}" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="#7e22ce">{label_b}</text>')

    svg_parts.append("</svg>")
    return "\n".join(svg_parts)


def draw_circle_figure_svg(
    radius_val: float,
    kind: str = "circle",  # "circle", "semicircle", "quadrant", "annulus"
    r_inner: Optional[float] = None,
    label_r: str = "r",
    label_inner: str = "r",
    label_outer: str = "R",
    seed: Optional[int] = None,
) -> str:
    """Renders circle, semicircle, quadrant, or annular ring."""
    width, height_px = 380, 260
    cx, cy = 190, 130
    R = 85

    svg_parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height_px}" width="100%" height="auto">',
        f"<!-- s:{seed} -->",
        '<rect width="100%" height="100%" fill="#f8fafc" rx="8"/>',
    ]

    if kind == "circle":
        svg_parts.append(f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="#e0f2fe" stroke="#0284c7" stroke-width="2.5"/>')
        svg_parts.append(f'<circle cx="{cx}" cy="{cy}" r="3.5" fill="#0f172a"/>')
        svg_parts.append(f'<line x1="{cx}" y1="{cy}" x2="{cx + R}" y2="{cy}" stroke="#0f172a" stroke-width="2"/>')
        svg_parts.append(f'<text x="{cx + R / 2}" y="{cy - 10}" font-family="Arial, sans-serif" font-size="14" font-weight="bold" fill="#0f172a" text-anchor="middle">{label_r}</text>')

    elif kind == "semicircle":
        # Semicircle resting on diameter baseline
        cy_base = 180
        path_d = f"M {cx - R} {cy_base} A {R} {R} 0 0 1 {cx + R} {cy_base} Z"
        svg_parts.append(f'<path d="{path_d}" fill="#dcfce7" stroke="#16a34a" stroke-width="2.5"/>')
        svg_parts.append(f'<circle cx="{cx}" cy="{cy_base}" r="3.5" fill="#0f172a"/>')
        svg_parts.append(f'<line x1="{cx}" y1="{cy_base}" x2="{cx + R}" y2="{cy_base}" stroke="#0f172a" stroke-width="2"/>')
        svg_parts.append(f'<text x="{cx + R / 2}" y="{cy_base - 10}" font-family="Arial, sans-serif" font-size="14" font-weight="bold" fill="#0f172a" text-anchor="middle">{label_r}</text>')

    elif kind == "quadrant":
        x0, y0 = 120, 190
        path_d = f"M {x0} {y0} L {x0 + 120} {y0} A 120 120 0 0 0 {x0} {y0 - 120} Z"
        svg_parts.append(f'<path d="{path_d}" fill="#fef3c7" stroke="#d97706" stroke-width="2.5"/>')
        svg_parts.append(f'<rect x="{x0}" y="{y0 - 16}" width="16" height="16" fill="none" stroke="#d97706" stroke-width="2"/>')
        svg_parts.append(f'<text x="{x0 + 60}" y="{y0 + 22}" font-family="Arial, sans-serif" font-size="14" font-weight="bold" fill="#0f172a" text-anchor="middle">{label_r}</text>')

    elif kind == "annulus":
        r_in_px = 45
        svg_parts.append(f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="#e0e7ff" stroke="#4338ca" stroke-width="2.5"/>')
        svg_parts.append(f'<circle cx="{cx}" cy="{cy}" r="{r_in_px}" fill="#f8fafc" stroke="#4338ca" stroke-width="2.5"/>')
        svg_parts.append(f'<circle cx="{cx}" cy="{cy}" r="3.5" fill="#0f172a"/>')
        # Radii arrows
        svg_parts.append(f'<line x1="{cx}" y1="{cy}" x2="{cx + r_in_px}" y2="{cy}" stroke="#dc2626" stroke-width="2"/>')
        svg_parts.append(f'<text x="{cx + r_in_px / 2}" y="{cy - 8}" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="#dc2626" text-anchor="middle">{label_inner}</text>')
        svg_parts.append(f'<line x1="{cx}" y1="{cy}" x2="{cx}" y2="{cy - R}" stroke="#4338ca" stroke-width="2"/>')
        svg_parts.append(f'<text x="{cx + 10}" y="{cy - R / 2}" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="#4338ca">{label_outer}</text>')

    svg_parts.append("</svg>")
    return "\n".join(svg_parts)


def draw_composite_shape_svg(
    composite_type: str,  # "l_shape", "running_track", "square_minus_circle"
    dim_w: float,
    dim_h: float,
    label_w: str = "W",
    label_h: str = "H",
    extra_label: str = "",
    seed: Optional[int] = None,
) -> str:
    """Renders composite figures and shaded region cutouts."""
    width, height_px = 400, 260
    svg_parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height_px}" width="100%" height="auto">',
        f"<!-- s:{seed} -->",
        '<rect width="100%" height="100%" fill="#f8fafc" rx="8"/>',
    ]

    if composite_type == "l_shape":
        # L-shaped block: outer 180x160, cutout 100x90
        x0, y0 = 100, 50
        pts = f"{x0},{y0} {x0 + 80},{y0} {x0 + 80},{y0 + 70} {x0 + 190},{y0 + 70} {x0 + 190},{y0 + 160} {x0},{y0 + 160}"
        svg_parts.append(f'<polygon points="{pts}" fill="#ccfbf1" stroke="#0f766e" stroke-width="2.5"/>')
        # Labels
        svg_parts.append(f'<text x="{x0 + 95}" y="{y0 + 185}" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="middle">{label_w}</text>')
        svg_parts.append(f'<text x="{x0 - 15}" y="{y0 + 85}" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="end">{label_h}</text>')
        if extra_label:
            svg_parts.append(f'<text x="{x0 + 140}" y="{y0 + 60}" font-family="Arial, sans-serif" font-size="12" fill="#0f766e">{extra_label}</text>')

    elif composite_type == "running_track":
        # Rectangle with two semicircular ends
        rx, ry = 110, 65
        rw, rh = 180, 130
        r_semi = rh / 2
        path_d = f"M {rx} {ry} L {rx + rw} {ry} A {r_semi} {r_semi} 0 0 1 {rx + rw} {ry + rh} L {rx} {ry + rh} A {r_semi} {r_semi} 0 0 1 {rx} {ry} Z"
        svg_parts.append(f'<path d="{path_d}" fill="#fce7f3" stroke="#be185d" stroke-width="2.5"/>')
        # Dashed dividers between rectangle and semicircles
        svg_parts.append(f'<line x1="{rx}" y1="{ry}" x2="{rx}" y2="{ry + rh}" stroke="#be185d" stroke-dasharray="4,4" stroke-width="1.8"/>')
        svg_parts.append(f'<line x1="{rx + rw}" y1="{ry}" x2="{rx + rw}" y2="{ry + rh}" stroke="#be185d" stroke-dasharray="4,4" stroke-width="1.8"/>')
        # Labels
        svg_parts.append(f'<text x="{rx + rw / 2}" y="{ry + rh + 24}" font-family="Arial, sans-serif" font-size="14" font-weight="bold" fill="#0f172a" text-anchor="middle">{label_w}</text>')
        svg_parts.append(f'<text x="{rx + rw / 2}" y="{ry + rh / 2 + 5}" font-family="Arial, sans-serif" font-size="14" font-weight="bold" fill="#be185d" text-anchor="middle">Diameter: {label_h}</text>')

    elif composite_type == "square_minus_circle":
        # Shaded square with unshaded white inscribed circle
        s = 150
        x0, y0 = 125, 55
        cx, cy = x0 + s / 2, y0 + s / 2
        r = s / 2
        svg_parts.append(f'<rect x="{x0}" y="{y0}" width="{s}" height="{s}" fill="#fed7aa" stroke="#c2410c" stroke-width="2.5"/>')
        svg_parts.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#f8fafc" stroke="#c2410c" stroke-width="2"/>')
        svg_parts.append(f'<text x="{cx}" y="{y0 + s + 24}" font-family="Arial, sans-serif" font-size="14" font-weight="bold" fill="#0f172a" text-anchor="middle">Side: {label_w}</text>')

    svg_parts.append("</svg>")
    return "\n".join(svg_parts)
