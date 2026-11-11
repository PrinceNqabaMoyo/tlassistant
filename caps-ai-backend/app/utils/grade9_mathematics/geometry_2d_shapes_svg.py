"""Grade 9 Mathematics - Geometry of 2D Shapes SVG Diagrams.
Publication-grade SVG renderers for triangles with angle arcs and side tick marks,
exterior angle extensions, congruent and similar triangle pairs,
quadrilaterals (parallelogram, rectangle, rhombus, square, trapezium, kite) with geometric markers,
and regular polygons.
"""
from __future__ import annotations

import math
from typing import Any, Dict, List, Optional, Tuple


def draw_triangle_angles_svg(
    angles: Tuple[int, int, int] = (60, 60, 60),
    labels: Tuple[str, str, str] = ("A", "B", "C"),
    angle_texts: Tuple[str, str, str] = ("", "", ""),
    side_ticks: Tuple[bool, bool, bool] = (False, False, False),
    seed: Optional[int] = None,
    **kwargs: Any,
) -> str:
    """Draws a triangle with vertices, optional angle arc text, and side tick marks."""
    entropy_comment = f"<!-- s:{seed} -->\n" if seed is not None else ""
    width = 380
    height = 260
    pad_x = 40
    pad_y = 35

    # Coordinates for triangle: B at bottom-left, C at bottom-right, A at top
    bx, by = pad_x, height - pad_y
    cx, cy = width - pad_x, height - pad_y

    ang_b, ang_c = angles[1], angles[2]
    # Estimate top vertex A position using angles
    base_len = cx - bx
    rad_b = math.radians(max(20, min(85, ang_b)))
    rad_c = math.radians(max(20, min(85, ang_c)))
    rad_a = math.pi - rad_b - rad_c
    if rad_a <= 0:
        rad_b = math.radians(55)
        rad_c = math.radians(65)
        rad_a = math.pi - rad_b - rad_c

    side_c = (base_len * math.sin(rad_c)) / math.sin(rad_a)
    ax = bx + side_c * math.cos(rad_b)
    ay = by - side_c * math.sin(rad_b)

    # Scale/clamp if too high or low
    if ay < 30:
        scale = (by - 35) / (by - ay)
        ax = bx + (ax - bx) * scale
        ay = by - (by - ay) * scale

    poly_pts = f"{ax:.1f},{ay:.1f} {bx:.1f},{by:.1f} {cx:.1f},{cy:.1f}"

    elements = []
    # Triangle body
    elements.append(
        f'<polygon points="{poly_pts}" fill="#EFF6FF" stroke="#1E3A8A" stroke-width="2.5" stroke-linejoin="round"/>'
    )

    # Vertex labels
    elements.append(f'<text x="{ax:.1f}" y="{ay - 10:.1f}" text-anchor="middle" font-size="14" font-weight="700" fill="#0F172A">{labels[0]}</text>')
    elements.append(f'<text x="{bx - 12:.1f}" y="{by + 16:.1f}" text-anchor="middle" font-size="14" font-weight="700" fill="#0F172A">{labels[1]}</text>')
    elements.append(f'<text x="{cx + 12:.1f}" y="{cy + 16:.1f}" text-anchor="middle" font-size="14" font-weight="700" fill="#0F172A">{labels[2]}</text>')

    # Angle texts if provided
    if angle_texts[0]:
        elements.append(f'<text x="{ax:.1f}" y="{ay + 25:.1f}" text-anchor="middle" font-size="12" font-weight="600" fill="#2563EB">{angle_texts[0]}</text>')
    if angle_texts[1]:
        elements.append(f'<text x="{bx + 35:.1f}" y="{by - 12:.1f}" text-anchor="middle" font-size="12" font-weight="600" fill="#2563EB">{angle_texts[1]}</text>')
    if angle_texts[2]:
        elements.append(f'<text x="{cx - 35:.1f}" y="{cy - 12:.1f}" text-anchor="middle" font-size="12" font-weight="600" fill="#2563EB">{angle_texts[2]}</text>')

    # Side ticks (AB, BC, CA)
    # AB tick
    if side_ticks[0]:
        mx, my = (ax + bx) / 2, (ay + by) / 2
        elements.append(f'<line x1="{mx - 5:.1f}" y1="{my - 5:.1f}" x2="{mx + 5:.1f}" y2="{my + 5:.1f}" stroke="#DC2626" stroke-width="2"/>')
    # BC tick
    if side_ticks[1]:
        mx, my = (bx + cx) / 2, (by + cy) / 2
        elements.append(f'<line x1="{mx:.1f}" y1="{my - 6:.1f}" x2="{mx:.1f}" y2="{my + 6:.1f}" stroke="#DC2626" stroke-width="2"/>')
    # CA tick
    if side_ticks[2]:
        mx, my = (cx + ax) / 2, (cy + ay) / 2
        elements.append(f'<line x1="{mx - 5:.1f}" y1="{my + 5:.1f}" x2="{mx + 5:.1f}" y2="{my - 5:.1f}" stroke="#DC2626" stroke-width="2"/>')

    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
        f'width="{width}" height="{height}" class="mx-auto block" style="background:#FFFFFF;border-radius:8px;border:1px solid #E2E8F0;">\n'
        f"{entropy_comment}"
        f'  <g id="triangle_angles">\n'
        f"    {''.join(elements)}\n"
        f'  </g>\n'
        f'</svg>'
    )


def draw_triangle_exterior_angle_svg(
    int_a: str = "A",
    int_b: str = "B",
    ext_c: str = "x",
    seed: Optional[int] = None,
    **kwargs: Any,
) -> str:
    """Draws a triangle with side BC extended to point D, showing exterior angle ACD."""
    entropy_comment = f"<!-- s:{seed} -->\n" if seed is not None else ""
    width = 420
    height = 240
    bx, by = 40.0, 190.0
    cx, cy = 290.0, 190.0
    dx = 380.0
    ax, ay = 170.0, 45.0

    elements = []
    # Extended base line BD
    elements.append(f'<line x1="{bx}" y1="{by}" x2="{dx}" y2="{by}" stroke="#1E3A8A" stroke-width="2.5"/>')
    # Triangle sides AB and AC
    elements.append(f'<line x1="{bx}" y1="{by}" x2="{ax}" y2="{ay}" stroke="#1E3A8A" stroke-width="2.5"/>')
    elements.append(f'<line x1="{cx}" y1="{cy}" x2="{ax}" y2="{ay}" stroke="#1E3A8A" stroke-width="2.5"/>')
    # Shading inside triangle
    elements.append(f'<polygon points="{ax},{ay} {bx},{by} {cx},{cy}" fill="#EFF6FF" opacity="0.7"/>')

    # Vertices
    elements.append(f'<text x="{ax}" y="{ay - 10}" text-anchor="middle" font-size="14" font-weight="700" fill="#0F172A">A</text>')
    elements.append(f'<text x="{bx - 12}" y="{by + 16}" text-anchor="middle" font-size="14" font-weight="700" fill="#0F172A">B</text>')
    elements.append(f'<text x="{cx}" y="{cy + 20}" text-anchor="middle" font-size="14" font-weight="700" fill="#0F172A">C</text>')
    elements.append(f'<text x="{dx + 12}" y="{by + 16}" text-anchor="middle" font-size="14" font-weight="700" fill="#0F172A">D</text>')

    # Angle labels
    elements.append(f'<text x="{ax}" y="{ay + 30}" text-anchor="middle" font-size="13" font-weight="600" fill="#2563EB">{int_a}</text>')
    elements.append(f'<text x="{bx + 35}" y="{by - 12}" text-anchor="middle" font-size="13" font-weight="600" fill="#2563EB">{int_b}</text>')
    # Exterior angle arc at C
    elements.append(f'<path d="M {cx + 25} {cy} A 25 25 0 0 0 {cx + 15} {cy - 20}" fill="none" stroke="#DC2626" stroke-width="2"/>')
    elements.append(f'<text x="{cx + 38}" y="{cy - 14}" text-anchor="middle" font-size="13" font-weight="700" fill="#DC2626">{ext_c}</text>')

    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
        f'width="{width}" height="{height}" class="mx-auto block" style="background:#FFFFFF;border-radius:8px;border:1px solid #E2E8F0;">\n'
        f"{entropy_comment}"
        f'  <g id="triangle_exterior">\n'
        f"    {''.join(elements)}\n"
        f'  </g>\n'
        f'</svg>'
    )


def draw_congruent_triangles_pair_svg(
    t1_labels: Tuple[str, str, str] = ("A", "B", "C"),
    t2_labels: Tuple[str, str, str] = ("D", "E", "F"),
    condition: str = "SAS",
    seed: Optional[int] = None,
    **kwargs: Any,
) -> str:
    """Draws two triangles side-by-side with congruency markers (SSS, SAS, AAS, or RHS)."""
    entropy_comment = f"<!-- s:{seed} -->\n" if seed is not None else ""
    width = 460
    height = 220

    # Triangle 1 (left)
    ax, ay = 90.0, 45.0
    bx, by = 35.0, 175.0
    cx, cy = 185.0, 175.0

    # Triangle 2 (right)
    dx, dy = 325.0, 45.0
    ex, ey = 270.0, 175.0
    fx, fy = 420.0, 175.0

    elements = []
    # Triangles
    elements.append(f'<polygon points="{ax},{ay} {bx},{by} {cx},{cy}" fill="#F0FDF4" stroke="#15803D" stroke-width="2.2"/>')
    elements.append(f'<polygon points="{dx},{dy} {ex},{ey} {fx},{fy}" fill="#EFF6FF" stroke="#1D4ED8" stroke-width="2.2"/>')

    # Vertex labels
    elements.append(f'<text x="{ax}" y="{ay - 10}" text-anchor="middle" font-size="14" font-weight="700" fill="#0F172A">{t1_labels[0]}</text>')
    elements.append(f'<text x="{bx - 12}" y="{by + 16}" text-anchor="middle" font-size="14" font-weight="700" fill="#0F172A">{t1_labels[1]}</text>')
    elements.append(f'<text x="{cx + 12}" y="{cy + 16}" text-anchor="middle" font-size="14" font-weight="700" fill="#0F172A">{t1_labels[2]}</text>')

    elements.append(f'<text x="{dx}" y="{dy - 10}" text-anchor="middle" font-size="14" font-weight="700" fill="#0F172A">{t2_labels[0]}</text>')
    elements.append(f'<text x="{ex - 12}" y="{ey + 16}" text-anchor="middle" font-size="14" font-weight="700" fill="#0F172A">{t2_labels[1]}</text>')
    elements.append(f'<text x="{fx + 12}" y="{fy + 16}" text-anchor="middle" font-size="14" font-weight="700" fill="#0F172A">{t2_labels[2]}</text>')

    # Congruence markings based on condition
    if condition in ("SSS", "SAS", "RHS"):
        # Single tick on AB and DE
        elements.append(f'<line x1="58" y1="105" x2="68" y2="115" stroke="#DC2626" stroke-width="2"/>')
        elements.append(f'<line x1="293" y1="105" x2="303" y2="115" stroke="#DC2626" stroke-width="2"/>')
    if condition in ("SSS", "SAS"):
        # Double tick on BC and EF
        elements.append(f'<line x1="107" y1="170" x2="107" y2="180" stroke="#DC2626" stroke-width="2"/>')
        elements.append(f'<line x1="113" y1="170" x2="113" y2="180" stroke="#DC2626" stroke-width="2"/>')
        elements.append(f'<line x1="342" y1="170" x2="342" y2="180" stroke="#DC2626" stroke-width="2"/>')
        elements.append(f'<line x1="348" y1="170" x2="348" y2="180" stroke="#DC2626" stroke-width="2"/>')
    if condition == "SSS":
        # Triple tick on AC and DF
        for off in [-4, 0, 4]:
            elements.append(f'<line x1="{137 + off}" y1="{115 - off}" x2="{145 + off}" y2="{105 - off}" stroke="#DC2626" stroke-width="1.8"/>')
            elements.append(f'<line x1="{372 + off}" y1="{115 - off}" x2="{380 + off}" y2="{105 - off}" stroke="#DC2626" stroke-width="1.8"/>')

    if condition == "SAS":
        # Included angle at B and E
        elements.append(f'<path d="M 55 175 A 20 20 0 0 0 50 158" fill="none" stroke="#2563EB" stroke-width="2"/>')
        elements.append(f'<path d="M 290 175 A 20 20 0 0 0 285 158" fill="none" stroke="#2563EB" stroke-width="2"/>')

    if condition == "AAS":
        # Angle B = Angle E
        elements.append(f'<path d="M 55 175 A 20 20 0 0 0 50 158" fill="none" stroke="#2563EB" stroke-width="2"/>')
        elements.append(f'<path d="M 290 175 A 20 20 0 0 0 285 158" fill="none" stroke="#2563EB" stroke-width="2"/>')
        # Angle C = Angle F
        elements.append(f'<path d="M 165 175 A 20 20 0 0 1 170 158" fill="none" stroke="#D97706" stroke-width="2"/>')
        elements.append(f'<path d="M 400 175 A 20 20 0 0 1 405 158" fill="none" stroke="#D97706" stroke-width="2"/>')
        # Side AB = DE
        elements.append(f'<line x1="58" y1="105" x2="68" y2="115" stroke="#DC2626" stroke-width="2"/>')
        elements.append(f'<line x1="293" y1="105" x2="303" y2="115" stroke="#DC2626" stroke-width="2"/>')

    if condition == "RHS":
        # Right angle square at B and E
        elements.append(f'<rect x="35" y="160" width="15" height="15" fill="none" stroke="#0F172A" stroke-width="1.5"/>')
        elements.append(f'<rect x="270" y="160" width="15" height="15" fill="none" stroke="#0F172A" stroke-width="1.5"/>')
        # Hypotenuse AC = DF (double tick)
        elements.append(f'<line x1="135" y1="113" x2="143" y2="105" stroke="#2563EB" stroke-width="2"/>')
        elements.append(f'<line x1="140" y1="117" x2="148" y2="109" stroke="#2563EB" stroke-width="2"/>')
        elements.append(f'<line x1="370" y1="113" x2="378" y2="105" stroke="#2563EB" stroke-width="2"/>')
        elements.append(f'<line x1="375" y1="117" x2="383" y2="109" stroke="#2563EB" stroke-width="2"/>')

    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
        f'width="{width}" height="{height}" class="mx-auto block" style="background:#FFFFFF;border-radius:8px;border:1px solid #E2E8F0;">\n'
        f"{entropy_comment}"
        f'  <g id="congruent_triangles">\n'
        f"    {''.join(elements)}\n"
        f'  </g>\n'
        f'</svg>'
    )


def draw_quadrilateral_svg(
    quad_type: str = "parallelogram",
    labels: Tuple[str, str, str, str] = ("A", "B", "C", "D"),
    show_diagonals: bool = False,
    extra_text: str = "",
    seed: Optional[int] = None,
    **kwargs: Any,
) -> str:
    """Draws a quadrilateral with accurate geometric properties."""
    entropy_comment = f"<!-- s:{seed} -->\n" if seed is not None else ""
    width = 380
    height = 230

    if quad_type == "parallelogram":
        ax, ay = 95.0, 45.0
        bx, by = 315.0, 45.0
        cx, cy = 265.0, 185.0
        dx, dy = 45.0, 185.0
    elif quad_type == "rectangle":
        ax, ay = 55.0, 50.0
        bx, by = 325.0, 50.0
        cx, cy = 325.0, 180.0
        dx, dy = 55.0, 180.0
    elif quad_type == "rhombus":
        ax, ay = 190.0, 35.0
        bx, by = 310.0, 115.0
        cx, cy = 190.0, 195.0
        dx, dy = 70.0, 115.0
    elif quad_type == "square":
        ax, ay = 115.0, 40.0
        bx, by = 265.0, 40.0
        cx, cy = 265.0, 190.0
        dx, dy = 115.0, 190.0
    elif quad_type == "trapezium":
        ax, ay = 105.0, 50.0
        bx, by = 275.0, 50.0
        cx, cy = 335.0, 180.0
        dx, dy = 45.0, 180.0
    else:  # kite
        ax, ay = 190.0, 30.0
        bx, by = 295.0, 100.0
        cx, cy = 190.0, 200.0
        dx, dy = 85.0, 100.0

    poly_pts = f"{ax},{ay} {bx},{by} {cx},{cy} {dx},{dy}"

    elements = []
    # Fill & boundary
    elements.append(
        f'<polygon points="{poly_pts}" fill="#F8FAFC" stroke="#0F172A" stroke-width="2.5" stroke-linejoin="round"/>'
    )

    # Diagonals if requested
    if show_diagonals:
        elements.append(f'<line x1="{ax}" y1="{ay}" x2="{cx}" y2="{cy}" stroke="#2563EB" stroke-width="1.8" stroke-dasharray="4,3"/>')
        elements.append(f'<line x1="{bx}" y1="{by}" x2="{dx}" y2="{dy}" stroke="#2563EB" stroke-width="1.8" stroke-dasharray="4,3"/>')

    # Vertices
    elements.append(f'<text x="{ax - 10}" y="{ay - 8}" font-size="14" font-weight="700" fill="#0F172A">{labels[0]}</text>')
    elements.append(f'<text x="{bx + 8}" y="{by - 8}" font-size="14" font-weight="700" fill="#0F172A">{labels[1]}</text>')
    elements.append(f'<text x="{cx + 8}" y="{cy + 16}" font-size="14" font-weight="700" fill="#0F172A">{labels[2]}</text>')
    elements.append(f'<text x="{dx - 12}" y="{cy + 16}" font-size="14" font-weight="700" fill="#0F172A">{labels[3]}</text>')

    # Type-specific indicators
    if quad_type in ("rectangle", "square"):
        # Right angle squares
        elements.append(f'<rect x="{dx}" y="{dy - 15}" width="15" height="15" fill="none" stroke="#475569" stroke-width="1.5"/>')
        elements.append(f'<rect x="{cx - 15}" y="{cy - 15}" width="15" height="15" fill="none" stroke="#475569" stroke-width="1.5"/>')
    elif quad_type == "parallelogram":
        # Parallel arrows on AB and DC (horizontal)
        elements.append(f'<polygon points="205,42 212,45 205,48" fill="#DC2626"/>')
        elements.append(f'<polygon points="155,182 162,185 155,188" fill="#DC2626"/>')

    if extra_text:
        elements.append(
            f'<text x="{width/2}" y="{height - 8}" text-anchor="middle" font-size="12" font-family="sans-serif" font-weight="600" fill="#475569">{extra_text}</text>'
        )

    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
        f'width="{width}" height="{height}" class="mx-auto block" style="background:#FFFFFF;border-radius:8px;border:1px solid #E2E8F0;">\n'
        f"{entropy_comment}"
        f'  <g id="quadrilateral">\n'
        f"    {''.join(elements)}\n"
        f'  </g>\n'
        f'</svg>'
    )


def draw_regular_polygon_svg(
    num_sides: int = 5,
    radius: float = 85.0,
    seed: Optional[int] = None,
    **kwargs: Any,
) -> str:
    """Draws a regular n-sided polygon with center, vertices, and interior angle indicator."""
    entropy_comment = f"<!-- s:{seed} -->\n" if seed is not None else ""
    width = 300
    height = 240
    cx = width / 2
    cy = height / 2

    pts = []
    # Start at top (-pi/2)
    for i in range(num_sides):
        angle = -math.pi / 2 + (2 * math.pi * i) / num_sides
        px = cx + radius * math.cos(angle)
        py = cy + radius * math.sin(angle)
        pts.append((px, py))

    pts_str = " ".join([f"{px:.1f},{py:.1f}" for px, py in pts])

    elements = []
    elements.append(
        f'<polygon points="{pts_str}" fill="#EFF6FF" stroke="#1E40AF" stroke-width="2.5" stroke-linejoin="round"/>'
    )

    # Label vertices
    names = ["A", "B", "C", "D", "E", "F", "G", "H"]
    for i, (px, py) in enumerate(pts):
        vx = px + 14 * math.cos(-math.pi / 2 + (2 * math.pi * i) / num_sides)
        vy = py + 14 * math.sin(-math.pi / 2 + (2 * math.pi * i) / num_sides)
        lbl = names[i % len(names)]
        elements.append(
            f'<text x="{vx:.1f}" y="{vy:.1f}" text-anchor="middle" dominant-baseline="central" font-size="13" font-weight="700" fill="#0F172A">{lbl}</text>'
        )

    # Polygon name
    names_map = {3: "Triangle", 4: "Quadrilateral", 5: "Pentagon", 6: "Hexagon", 7: "Heptagon", 8: "Octagon", 10: "Decagon"}
    p_name = names_map.get(num_sides, f"{num_sides}-gon")
    elements.append(
        f'<text x="{cx}" y="{height - 8}" text-anchor="middle" font-size="12" font-family="sans-serif" font-weight="600" fill="#334155">Regular {p_name} ({num_sides} equal sides)</text>'
    )

    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
        f'width="{width}" height="{height}" class="mx-auto block" style="background:#FFFFFF;border-radius:8px;border:1px solid #E2E8F0;">\n'
        f"{entropy_comment}"
        f'  <g id="regular_polygon">\n'
        f"    {''.join(elements)}\n"
        f'  </g>\n'
        f'</svg>'
    )
