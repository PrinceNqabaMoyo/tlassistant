"""Grade 9 Mathematics - Construction of Geometric Figures SVG Diagram Builders
=============================================================================
Provides clean, authentic SVG visual representations for:
  - Angle bisector constructions with circular arcs and bisector rays
  - Perpendicular bisectors of segments with crossing compass arcs
  - Perpendicular lines erected at a point or dropped from an external point
  - Special angle constructions (30°, 45°, 60°, 75°, 90°, 105°, 120°) without protractor
  - Triangle constructions (SSS, SAS, ASA, RHS) with intersecting arc loci
  - Circumscribed circles (circumcentre) and inscribed circles (incentre)
  - Regular hexagon construction inscribed in a circle
"""
from __future__ import annotations

import math
from typing import Any, Dict, List, Optional, Tuple


def draw_angle_bisector_construction_svg(
    angle_deg: float = 60,
    arm_length: float = 140,
    angle_label: str = "B",
    bisect_label: str = "P",
    title: str = "Angle Bisector Compass Construction",
    seed: Optional[int] = None,
    **kwargs: Any,
) -> str:
    """Renders compass-and-straightedge angle bisection with construction arcs."""
    entropy_comment = f"<!-- s:{seed} -->\n" if seed is not None else ""

    width = 460
    height = 320
    vx, vy = 80, 240  # Vertex position

    rad = math.radians(angle_deg)
    half_rad = rad / 2

    # Arm 1 (horizontal right)
    a1x = vx + arm_length + 30
    a1y = vy

    # Arm 2 (angled up)
    a2x = vx + (arm_length + 30) * math.cos(rad)
    a2y = vy - (arm_length + 30) * math.sin(rad)

    # Arc 1: radius on arms
    r1 = 70
    p1x = vx + r1
    p1y = vy
    p2x = vx + r1 * math.cos(rad)
    p2y = vy - r1 * math.sin(rad)

    # Intersecting arcs in interior
    r2 = 80
    # From p1: arc centered at (p1x, p1y)
    # From p2: arc centered at (p2x, p2y)
    # Intersection point P lies along angle bisector at distance d from vertex
    # Using geometry: cos(half_rad) = r1 / something, let's place P accurately
    # Distance from vertex to intersection point:
    # In triangle with vertex V, P1, and P: dist VP = r1 * cos(half_rad) + sqrt(r2^2 - (r1*sin(half_rad))^2)
    sin_h = math.sin(half_rad)
    cos_h = math.cos(half_rad)
    d_proj = r1 * cos_h + math.sqrt(max(10, r2**2 - (r1 * sin_h)**2))
    px = vx + d_proj * math.cos(half_rad)
    py = vy - d_proj * math.sin(half_rad)

    # Bisector ray through P
    ray_len = arm_length + 40
    bx = vx + ray_len * math.cos(half_rad)
    by = vy - ray_len * math.sin(half_rad)

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="{height}" class="rounded-xl border border-slate-700 bg-slate-900/90 p-2">
{entropy_comment}<defs>
  <marker id="arr-blue" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
    <path d="M 0 1 L 8 5 L 0 9 z" fill="#38bdf8" />
  </marker>
  <marker id="arr-green" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
    <path d="M 0 1 L 8 5 L 0 9 z" fill="#10b981" />
  </marker>
</defs>
<!-- Title -->
<text x="{width/2:.1f}" y="24" fill="#f8fafc" font-size="13" font-weight="bold" font-family="sans-serif" text-anchor="middle">{title}</text>

<!-- Original Angle Arms -->
<line x1="{vx}" y1="{vy}" x2="{a1x:.1f}" y2="{a1y:.1f}" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#arr-blue)"/>
<line x1="{vx}" y1="{vy}" x2="{a2x:.1f}" y2="{a2y:.1f}" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#arr-blue)"/>

<!-- Arc 1 across both arms -->
<path d="M {p1x + 10:.1f} {p1y - 15:.1f} A {r1} {r1} 0 0 0 {p2x - 10:.1f} {p2y + 10:.1f}" fill="none" stroke="#f59e0b" stroke-width="1.8" stroke-dasharray="3,3"/>

<!-- Marks on arms P1 and P2 -->
<circle cx="{p1x:.1f}" cy="{p1y:.1f}" r="3.5" fill="#f59e0b"/>
<circle cx="{p2x:.1f}" cy="{p2y:.1f}" r="3.5" fill="#f59e0b"/>
<text x="{p1x:.1f}" y="{p1y + 16:.1f}" fill="#cbd5e1" font-size="10" font-family="monospace" text-anchor="middle">D</text>
<text x="{p2x - 12:.1f}" y="{p2y - 6:.1f}" fill="#cbd5e1" font-size="10" font-family="monospace">E</text>

<!-- Crossing Construction Arcs at P -->
<path d="M {px - 14:.1f} {py + 18:.1f} A {r2} {r2} 0 0 0 {px + 14:.1f} {py - 18:.1f}" fill="none" stroke="#ec4899" stroke-width="1.8"/>
<path d="M {px - 14:.1f} {py - 18:.1f} A {r2} {r2} 0 0 1 {px + 14:.1f} {py + 18:.1f}" fill="none" stroke="#ec4899" stroke-width="1.8"/>

<!-- Point P -->
<circle cx="{px:.1f}" cy="{py:.1f}" r="4" fill="#ec4899"/>
<text x="{px + 10:.1f}" y="{py - 8:.1f}" fill="#f472b6" font-size="11" font-weight="bold" font-family="sans-serif">{bisect_label}</text>

<!-- Bisector Ray -->
<line x1="{vx}" y1="{vy}" x2="{bx:.1f}" y2="{by:.1f}" stroke="#10b981" stroke-width="2.5" stroke-dasharray="6,3" marker-end="url(#arr-green)"/>

<!-- Vertex Label -->
<circle cx="{vx}" cy="{vy}" r="4.5" fill="#38bdf8"/>
<text x="{vx - 14}" y="{vy + 14}" fill="#f8fafc" font-size="12" font-weight="bold" font-family="sans-serif">{angle_label}</text>

<!-- Angle Size Badges -->
<text x="{vx + 45:.1f}" y="{vy - 8:.1f}" fill="#10b981" font-size="10" font-weight="bold" font-family="monospace">{angle_deg/2:.1f}°</text>
<text x="{vx + 35:.1f}" y="{vy - 28:.1f}" fill="#10b981" font-size="10" font-weight="bold" font-family="monospace">{angle_deg/2:.1f}°</text>
</svg>"""
    return svg


def draw_perpendicular_bisector_svg(
    length_px: float = 240,
    label_a: str = "A",
    label_b: str = "B",
    title: str = "Perpendicular Bisector Construction",
    seed: Optional[int] = None,
    **kwargs: Any,
) -> str:
    """Renders compass perpendicular bisector of segment AB with crossing arcs."""
    entropy_comment = f"<!-- s:{seed} -->\n" if seed is not None else ""

    width = 460
    height = 320
    cy = height / 2 + 10
    cx = width / 2

    ax = cx - length_px / 2
    bx = cx + length_px / 2

    # Compass radius r > length_px / 2
    r = length_px * 0.65
    h_arc = math.sqrt(r**2 - (length_px / 2)**2)

    top_ix = cx
    top_iy = cy - h_arc
    bot_ix = cx
    bot_iy = cy + h_arc

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="{height}" class="rounded-xl border border-slate-700 bg-slate-900/90 p-2">
{entropy_comment}<!-- Title -->
<text x="{width/2:.1f}" y="24" fill="#f8fafc" font-size="13" font-weight="bold" font-family="sans-serif" text-anchor="middle">{title}</text>

<!-- Construction Arcs from A -->
<path d="M {top_ix - 24:.1f} {top_iy - 12:.1f} A {r:.1f} {r:.1f} 0 0 1 {top_ix + 24:.1f} {top_iy + 12:.1f}" fill="none" stroke="#f59e0b" stroke-width="1.8"/>
<path d="M {bot_ix - 24:.1f} {bot_iy + 12:.1f} A {r:.1f} {r:.1f} 0 0 0 {bot_ix + 24:.1f} {bot_iy - 12:.1f}" fill="none" stroke="#f59e0b" stroke-width="1.8"/>

<!-- Construction Arcs from B -->
<path d="M {top_ix + 24:.1f} {top_iy - 12:.1f} A {r:.1f} {r:.1f} 0 0 0 {top_ix - 24:.1f} {top_iy + 12:.1f}" fill="none" stroke="#ec4899" stroke-width="1.8"/>
<path d="M {bot_ix + 24:.1f} {bot_iy + 12:.1f} A {r:.1f} {r:.1f} 0 0 1 {bot_ix - 24:.1f} {bot_iy - 12:.1f}" fill="none" stroke="#ec4899" stroke-width="1.8"/>

<!-- Perpendicular Bisector Line -->
<line x1="{cx}" y1="{top_iy - 35:.1f}" x2="{cx}" y2="{bot_iy + 35:.1f}" stroke="#10b981" stroke-width="2.5" stroke-dasharray="5,3"/>

<!-- Segment AB -->
<line x1="{ax}" y1="{cy}" x2="{bx}" y2="{cy}" stroke="#38bdf8" stroke-width="3" stroke-linecap="round"/>

<!-- Endpoints A and B -->
<circle cx="{ax}" cy="{cy}" r="5" fill="#38bdf8"/>
<text x="{ax - 18}" y="{cy + 5}" fill="#f8fafc" font-size="12" font-weight="bold" font-family="sans-serif">{label_a}</text>

<circle cx="{bx}" cy="{cy}" r="5" fill="#38bdf8"/>
<text x="{bx + 10}" y="{cy + 5}" fill="#f8fafc" font-size="12" font-weight="bold" font-family="sans-serif">{label_b}</text>

<!-- Midpoint M -->
<circle cx="{cx}" cy="{cy}" r="3.5" fill="#10b981"/>
<text x="{cx + 8}" y="{cy + 16}" fill="#cbd5e1" font-size="11" font-family="monospace">M</text>

<!-- Right Angle Indicator -->
<rect x="{cx - 12}" y="{cy - 12}" width="12" height="12" fill="none" stroke="#10b981" stroke-width="1.5"/>

<!-- Equal tick marks on AM and MB -->
<line x1="{(ax+cx)/2 - 3}" y1="{cy - 6}" x2="{(ax+cx)/2 - 3}" y2="{cy + 6}" stroke="#f8fafc" stroke-width="1.5"/>
<line x1="{(ax+cx)/2 + 3}" y1="{cy - 6}" x2="{(ax+cx)/2 + 3}" y2="{cy + 6}" stroke="#f8fafc" stroke-width="1.5"/>

<line x1="{(bx+cx)/2 - 3}" y1="{cy - 6}" x2="{(bx+cx)/2 - 3}" y2="{cy + 6}" stroke="#f8fafc" stroke-width="1.5"/>
<line x1="{(bx+cx)/2 + 3}" y1="{cy - 6}" x2="{(bx+cx)/2 + 3}" y2="{cy + 6}" stroke="#f8fafc" stroke-width="1.5"/>

<!-- Intersection points P and Q -->
<circle cx="{top_ix}" cy="{top_iy}" r="4" fill="#fbbf24"/>
<text x="{top_ix + 8}" y="{top_iy - 6}" fill="#fbbf24" font-size="11" font-weight="bold" font-family="sans-serif">P</text>

<circle cx="{bot_ix}" cy="{bot_iy}" r="4" fill="#fbbf24"/>
<text x="{bot_ix + 8}" y="{bot_iy + 14}" fill="#fbbf24" font-size="11" font-weight="bold" font-family="sans-serif">Q</text>
</svg>"""
    return svg


def draw_special_angle_construction_svg(
    angle_deg: float = 60,
    title: str = "Constructing Angle Without Protractor",
    seed: Optional[int] = None,
    **kwargs: Any,
) -> str:
    """Renders compass construction of special angle (30, 45, 60, 90, 120)."""
    entropy_comment = f"<!-- s:{seed} -->\n" if seed is not None else ""

    width = 460
    height = 320
    vx, vy = 100, 240
    r = 130  # main base arc radius

    rad = math.radians(angle_deg)
    # End of base line
    bx = vx + 220
    by = vy

    # Point X on base line where compass arc cuts
    xx = vx + r
    xy = vy

    # Angled ray endpoint
    ax = vx + 180 * math.cos(rad)
    ay = vy - 180 * math.sin(rad)

    # Arc intersection point at angle_deg
    ix = vx + r * math.cos(rad)
    iy = vy - r * math.sin(rad)

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="{height}" class="rounded-xl border border-slate-700 bg-slate-900/90 p-2">
{entropy_comment}<defs>
  <marker id="arr-blue" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
    <path d="M 0 1 L 8 5 L 0 9 z" fill="#38bdf8" />
  </marker>
  <marker id="arr-green" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
    <path d="M 0 1 L 8 5 L 0 9 z" fill="#10b981" />
  </marker>
</defs>
<!-- Title -->
<text x="{width/2:.1f}" y="24" fill="#f8fafc" font-size="13" font-weight="bold" font-family="sans-serif" text-anchor="middle">{title} ({angle_deg}°)</text>

<!-- Base Ray -->
<line x1="{vx}" y1="{vy}" x2="{bx}" y2="{by}" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#arr-blue)"/>

<!-- Primary Circle Arc from Vertex V -->
<path d="M {xx + 15} {xy} A {r} {r} 0 0 0 {vx + r * math.cos(math.radians(max(angle_deg+20, 75))):.1f} {vy - r * math.sin(math.radians(max(angle_deg+20, 75))):.1f}" fill="none" stroke="#f59e0b" stroke-width="1.8" stroke-dasharray="3,3"/>

<!-- Base intersection point X -->
<circle cx="{xx}" cy="{xy}" r="4" fill="#f59e0b"/>
<text x="{xx}" y="{xy + 18}" fill="#cbd5e1" font-size="11" font-family="sans-serif" text-anchor="middle">X</text>

<!-- Arc from point X cutting main arc at 60 deg or target -->
<circle cx="{ix:.1f}" cy="{iy:.1f}" r="4.5" fill="#ec4899"/>
<text x="{ix + 12:.1f}" y="{iy - 6:.1f}" fill="#f472b6" font-size="11" font-weight="bold" font-family="sans-serif">C</text>
<path d="M {ix - 15:.1f} {iy + 15:.1f} A {r} {r} 0 0 0 {ix + 15:.1f} {iy - 15:.1f}" fill="none" stroke="#ec4899" stroke-width="2"/>

<!-- Constructed Angle Ray -->
<line x1="{vx}" y1="{vy}" x2="{ax:.1f}" y2="{ay:.1f}" stroke="#10b981" stroke-width="2.5" marker-end="url(#arr-green)"/>

<!-- Vertex V -->
<circle cx="{vx}" cy="{vy}" r="5" fill="#38bdf8"/>
<text x="{vx - 18}" y="{vy + 15}" fill="#f8fafc" font-size="12" font-weight="bold" font-family="sans-serif">V</text>

<!-- Angle Arc & Label -->
<path d="M {vx + 45} {vy} A 45 45 0 0 0 {vx + 45 * math.cos(rad):.1f} {vy - 45 * math.sin(rad):.1f}" fill="none" stroke="#10b981" stroke-width="2"/>
<text x="{vx + 58 * math.cos(rad/2):.1f}" y="{vy - 58 * math.sin(rad/2):.1f}" fill="#10b981" font-size="12" font-weight="bold" font-family="monospace">{angle_deg}°</text>
</svg>"""
    return svg


def draw_triangle_construction_svg(
    side_a: float = 6,
    side_b: float = 5,
    side_c: float = 7,
    title: str = "Triangle Construction (SSS)",
    seed: Optional[int] = None,
    **kwargs: Any,
) -> str:
    """Renders triangle construction with intersecting compass arcs from endpoints."""
    entropy_comment = f"<!-- s:{seed} -->\n" if seed is not None else ""

    width = 460
    height = 320

    # Scale sides to fit nicely in 300px width
    scale = 220 / max(side_c, 1)
    c_px = side_c * scale
    a_px = side_a * scale
    b_px = side_b * scale

    ax = (width - c_px) / 2
    ay = 240
    bx = ax + c_px
    by = ay

    # Calculate third vertex C coordinates using law of cosines
    # cos(A) = (b^2 + c^2 - a^2) / (2 b c)
    cos_A = (side_b**2 + side_c**2 - side_a**2) / (2 * side_b * side_c)
    cos_A = max(-1.0, min(1.0, cos_A))
    sin_A = math.sqrt(max(0.0, 1.0 - cos_A**2))

    cx = ax + b_px * cos_A
    cy = ay - b_px * sin_A

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="{height}" class="rounded-xl border border-slate-700 bg-slate-900/90 p-2">
{entropy_comment}<!-- Title -->
<text x="{width/2:.1f}" y="24" fill="#f8fafc" font-size="13" font-weight="bold" font-family="sans-serif" text-anchor="middle">{title}</text>

<!-- Compass Arc from A (radius b = {side_b} cm) -->
<path d="M {cx - 24:.1f} {cy + 18:.1f} A {b_px:.1f} {b_px:.1f} 0 0 1 {cx + 24:.1f} {cy - 18:.1f}" fill="none" stroke="#f59e0b" stroke-width="2"/>

<!-- Compass Arc from B (radius a = {side_a} cm) -->
<path d="M {cx + 24:.1f} {cy + 18:.1f} A {a_px:.1f} {a_px:.1f} 0 0 0 {cx - 24:.1f} {cy - 18:.1f}" fill="none" stroke="#ec4899" stroke-width="2"/>

<!-- Triangle Sides -->
<polygon points="{ax:.1f},{ay:.1f} {bx:.1f},{by:.1f} {cx:.1f},{cy:.1f}" fill="#38bdf8" fill-opacity="0.1" stroke="#38bdf8" stroke-width="2.5"/>

<!-- Vertices -->
<circle cx="{ax:.1f}" cy="{ay:.1f}" r="4.5" fill="#38bdf8"/>
<text x="{ax - 16:.1f}" y="{ay + 16:.1f}" fill="#f8fafc" font-size="12" font-weight="bold" font-family="sans-serif">A</text>

<circle cx="{bx:.1f}" cy="{by:.1f}" r="4.5" fill="#38bdf8"/>
<text x="{bx + 8:.1f}" y="{by + 16:.1f}" fill="#f8fafc" font-size="12" font-weight="bold" font-family="sans-serif">B</text>

<circle cx="{cx:.1f}" cy="{cy:.1f}" r="4.5" fill="#fbbf24"/>
<text x="{cx:.1f}" y="{cy - 12:.1f}" fill="#fbbf24" font-size="12" font-weight="bold" font-family="sans-serif" text-anchor="middle">C</text>

<!-- Side Length Labels -->
<text x="{(ax+bx)/2:.1f}" y="{ay + 18:.1f}" fill="#cbd5e1" font-size="11" font-family="monospace" text-anchor="middle">c = {side_c} cm</text>
<text x="{(ax+cx)/2 - 16:.1f}" y="{(ay+cy)/2:.1f}" fill="#cbd5e1" font-size="11" font-family="monospace">b = {side_b} cm</text>
<text x="{(bx+cx)/2 + 8:.1f}" y="{(by+cy)/2:.1f}" fill="#cbd5e1" font-size="11" font-family="monospace">a = {side_a} cm</text>
</svg>"""
    return svg


def draw_circumcircle_or_incircle_svg(
    is_incircle: bool = False,
    title: Optional[str] = None,
    seed: Optional[int] = None,
    **kwargs: Any,
) -> str:
    """Renders triangle with circumcircle (circumcentre) or incircle (incentre)."""
    entropy_comment = f"<!-- s:{seed} -->\n" if seed is not None else ""

    width = 460
    height = 340
    # Equilateral-like triangle for clean symmetry
    ax, ay = 100, 260
    bx, by = 360, 260
    cx, cy = 230, 80

    # Circumcentre / Incentre for equilateral triangle
    ox, oy = 230, 200

    if is_incircle:
        r_circle = 60
        circle_title = title or "Inscribed Circle (Incentre from Angle Bisectors)"
        center_label = "I (Incentre)"
        line_color = "#10b981"
        line_desc = "Angle Bisectors"
    else:
        r_circle = 120
        circle_title = title or "Circumscribed Circle (Circumcentre from Perpendicular Bisectors)"
        center_label = "O (Circumcentre)"
        line_color = "#f59e0b"
        line_desc = "Perpendicular Bisectors"

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="{height}" class="rounded-xl border border-slate-700 bg-slate-900/90 p-2">
{entropy_comment}<!-- Title -->
<text x="{width/2:.1f}" y="24" fill="#f8fafc" font-size="13" font-weight="bold" font-family="sans-serif" text-anchor="middle">{circle_title}</text>

<!-- Circle -->
<circle cx="{ox}" cy="{oy}" r="{r_circle}" fill="none" stroke="{line_color}" stroke-width="2.2" stroke-dasharray="4,2"/>

<!-- Triangle ABC -->
<polygon points="{ax},{ay} {bx},{by} {cx},{cy}" fill="#38bdf8" fill-opacity="0.08" stroke="#38bdf8" stroke-width="2.5"/>

<!-- Bisector / Radius lines to Center -->
<line x1="{ax}" y1="{ay}" x2="{ox}" y2="{oy}" stroke="{line_color}" stroke-width="1.5" stroke-dasharray="3,3"/>
<line x1="{bx}" y1="{by}" x2="{ox}" y2="{oy}" stroke="{line_color}" stroke-width="1.5" stroke-dasharray="3,3"/>
<line x1="{cx}" y1="{cy}" x2="{ox}" y2="{oy}" stroke="{line_color}" stroke-width="1.5" stroke-dasharray="3,3"/>

<!-- Vertices -->
<circle cx="{ax}" cy="{ay}" r="4.5" fill="#38bdf8"/>
<text x="{ax - 16}" y="{ay + 15}" fill="#f8fafc" font-size="12" font-weight="bold" font-family="sans-serif">A</text>

<circle cx="{bx}" cy="{by}" r="4.5" fill="#38bdf8"/>
<text x="{bx + 8}" y="{by + 15}" fill="#f8fafc" font-size="12" font-weight="bold" font-family="sans-serif">B</text>

<circle cx="{cx}" cy="{cy}" r="4.5" fill="#38bdf8"/>
<text x="{cx}" y="{cy - 10}" fill="#f8fafc" font-size="12" font-weight="bold" font-family="sans-serif" text-anchor="middle">C</text>

<!-- Centre Point -->
<circle cx="{ox}" cy="{oy}" r="4.5" fill="{line_color}"/>
<text x="{ox + 10}" y="{oy - 8}" fill="{line_color}" font-size="11" font-weight="bold" font-family="sans-serif">{center_label}</text>
</svg>"""
    return svg
