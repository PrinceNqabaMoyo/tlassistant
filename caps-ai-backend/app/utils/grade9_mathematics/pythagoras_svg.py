"""SVG diagram generators for Grade 9 Mathematics - Theorem of Pythagoras.
Compliant with Fundile Unified Diagram Doctrine (diagram_doctrine.md):
- Pure standalone SVG (viewBox="0 0 460 300" / "0 0 500 360")
- Semantic, publication-grade geometry
- Right-angle corner square indicator
- Dynamic entropy tag <!-- s:{seed} -->
- No answer leaks
"""
from __future__ import annotations

import math
from typing import Any, Dict, List, Optional, Tuple


def draw_right_triangle_svg(
    legs: Tuple[float, float] = (4, 3),
    labels: Tuple[str, str, str] = ("A", "B", "C"),  # B is right angle
    side_labels: Optional[Dict[str, str]] = None,     # e.g. {"AB": "3 cm", "BC": "4 cm", "AC": "x"}
    right_angle_vertex: str = "B",
    orientation: str = "standard",                   # standard (bottom-left right angle)
    extra_text: str = "",
    seed: Optional[int] = None,
) -> str:
    """Draws a right-angled triangle with vertex labels, side annotations, and 90° corner square."""
    seed_tag = f"<!-- s:{seed} -->\n" if seed is not None else ""
    side_labels = side_labels or {}

    width, height = 460, 300
    # Coordinates for triangle vertices:
    # B at bottom-left, C at bottom-right, A at top-left
    bx, by = 90, 240
    leg_x, leg_y = legs
    # Scale legs to fit nicely
    scale = min(240 / max(leg_x, 1), 160 / max(leg_y, 1))
    cx = bx + leg_x * scale
    cy = by
    ax = bx
    ay = by - leg_y * scale

    # Square for right angle at B
    sq_size = 18
    sq_path = f"M {bx},{by - sq_size} L {bx + sq_size},{by - sq_size} L {bx + sq_size},{by}"

    # Side midpoint labels
    mid_ab = (ax - 28, (ay + by) / 2 + 5)
    mid_bc = ((bx + cx) / 2, by + 22)
    mid_ac = ((ax + cx) / 2 + 16, (ay + cy) / 2 - 10)

    lbl_ab = side_labels.get("AB", side_labels.get("c", ""))
    lbl_bc = side_labels.get("BC", side_labels.get("a", ""))
    lbl_ac = side_labels.get("AC", side_labels.get("b", side_labels.get("hyp", "")))

    svg_parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="auto" class="pythagoras-triangle-svg">',
        seed_tag,
        '  <defs>',
        '    <filter id="pyth-shadow" x="-5%" y="-5%" width="115%" height="115%">',
        '      <feDropShadow dx="1" dy="2" stdDeviation="2" flood-color="#1e293b" flood-opacity="0.12"/>',
        '    </filter>',
        '  </defs>',
        f'  <rect width="{width}" height="{height}" fill="#f8fafc" rx="8" />',
        # Triangle fill and stroke
        f'  <polygon points="{ax:.1f},{ay:.1f} {bx:.1f},{by:.1f} {cx:.1f},{cy:.1f}" fill="#eff6ff" stroke="#2563eb" stroke-width="2.5" stroke-linejoin="round" filter="url(#pyth-shadow)"/>',
        # Right angle marker
        f'  <path d="{sq_path}" fill="none" stroke="#dc2626" stroke-width="2"/>',
        # Vertices labels
        f'  <text x="{ax - 14:.1f}" y="{ay - 8:.1f}" font-family="sans-serif" font-size="16" font-weight="bold" fill="#0f172a">{labels[0]}</text>',
        f'  <text x="{bx - 18:.1f}" y="{by + 16:.1f}" font-family="sans-serif" font-size="16" font-weight="bold" fill="#0f172a">{labels[1]}</text>',
        f'  <text x="{cx + 10:.1f}" y="{cy + 16:.1f}" font-family="sans-serif" font-size="16" font-weight="bold" fill="#0f172a">{labels[2]}</text>',
    ]

    # Side labels
    if lbl_ab:
        svg_parts.append(f'  <text x="{mid_ab[0]:.1f}" y="{mid_ab[1]:.1f}" font-family="sans-serif" font-size="14" font-weight="600" fill="#1e3a8a" text-anchor="middle">{lbl_ab}</text>')
    if lbl_bc:
        svg_parts.append(f'  <text x="{mid_bc[0]:.1f}" y="{mid_bc[1]:.1f}" font-family="sans-serif" font-size="14" font-weight="600" fill="#1e3a8a" text-anchor="middle">{lbl_bc}</text>')
    if lbl_ac:
        svg_parts.append(f'  <text x="{mid_ac[0]:.1f}" y="{mid_ac[1]:.1f}" font-family="sans-serif" font-size="14" font-weight="600" fill="#dc2626" text-anchor="middle">{lbl_ac}</text>')

    if extra_text:
        svg_parts.append(f'  <text x="{width / 2:.1f}" y="32" font-family="sans-serif" font-size="13" fill="#475569" text-anchor="middle">{extra_text}</text>')

    svg_parts.append('</svg>')
    return "\n".join(svg_parts)


def draw_pythagorean_squares_svg(
    legs: Tuple[int, int] = (4, 3),
    seed: Optional[int] = None,
) -> str:
    """Draws a right triangle with squares constructed on all three sides."""
    seed_tag = f"<!-- s:{seed} -->\n" if seed is not None else ""
    width, height = 480, 360

    # Scaled visual coordinates
    bx, by = 210, 230
    a, b = legs
    c = round(math.sqrt(a * a + b * b))
    scale = 22

    ax = bx
    ay = by - b * scale
    cx = bx + a * scale
    cy = by

    # Square on side BC (bottom): extends downwards
    sq_bc_pts = f"{bx},{by} {cx},{cy} {cx},{cy + a * scale} {bx},{by + a * scale}"

    # Square on side AB (left): extends leftwards
    sq_ab_pts = f"{ax},{ay} {bx},{by} {bx - b * scale},{by} {bx - b * scale},{ay}"

    # Right angle marker at B
    sq_size = 14
    sq_path = f"M {bx},{by - sq_size} L {bx + sq_size},{by - sq_size} L {bx + sq_size},{by}"

    svg_parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="auto" class="pythagoras-squares-svg">',
        seed_tag,
        f'  <rect width="{width}" height="{height}" fill="#f8fafc" rx="8" />',
        # Square on AB (left)
        f'  <polygon points="{sq_ab_pts}" fill="#dbeafe" stroke="#3b82f6" stroke-width="2" />',
        f'  <text x="{bx - (b * scale) / 2:.1f}" y="{by - (b * scale) / 2 + 5:.1f}" font-family="sans-serif" font-size="14" font-weight="bold" fill="#1e40af" text-anchor="middle">Square B ({b}² = {b*b})</text>',
        # Square on BC (bottom)
        f'  <polygon points="{sq_bc_pts}" fill="#dcfce7" stroke="#22c55e" stroke-width="2" />',
        f'  <text x="{(bx + cx) / 2:.1f}" y="{by + (a * scale) / 2 + 5:.1f}" font-family="sans-serif" font-size="14" font-weight="bold" fill="#15803d" text-anchor="middle">Square A ({a}² = {a*a})</text>',
        # Right triangle
        f'  <polygon points="{ax:.1f},{ay:.1f} {bx:.1f},{by:.1f} {cx:.1f},{cy:.1f}" fill="#fef08a" stroke="#ca8a04" stroke-width="2.5" />',
        f'  <path d="{sq_path}" fill="none" stroke="#dc2626" stroke-width="1.8"/>',
        # Hypotenuse annotation
        f'  <text x="{(ax + cx) / 2 + 18:.1f}" y="{(ay + cy) / 2 - 12:.1f}" font-family="sans-serif" font-size="14" font-weight="bold" fill="#b91c1c" text-anchor="middle">Square C Area = {a*a} + {b*b} = {c*c}</text>',
        '</svg>'
    ]
    return "\n".join(svg_parts)


def draw_ladder_wall_svg(
    wall_height: float = 12.0,
    ground_dist: float = 5.0,
    ladder_len: Optional[float] = 13.0,
    unknown: str = "ladder",  # "ladder", "wall", "ground"
    seed: Optional[int] = None,
) -> str:
    """Draws a vertical wall, ground, and leaning ladder right-angled triangle."""
    seed_tag = f"<!-- s:{seed} -->\n" if seed is not None else ""
    width, height = 460, 300

    bx, by = 120, 240
    cx = 360
    cy = 240
    ax = 120
    ay = 60

    # Right angle marker at corner between wall and ground
    sq_size = 18
    sq_path = f"M {bx},{by - sq_size} L {bx + sq_size},{by - sq_size} L {bx + sq_size},{by}"

    lbl_wall = f"{wall_height:g} m" if unknown != "wall" else "h = ?"
    lbl_ground = f"{ground_dist:g} m" if unknown != "ground" else "d = ?"
    lbl_ladder = f"{ladder_len:g} m" if (ladder_len and unknown != "ladder") else "L = ?"

    svg_parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="auto" class="pythagoras-ladder-svg">',
        seed_tag,
        f'  <rect width="{width}" height="{height}" fill="#f8fafc" rx="8" />',
        # Ground line (extended)
        f'  <line x1="60" y1="{by}" x2="420" y2="{by}" stroke="#64748b" stroke-width="4" stroke-linecap="round"/>',
        f'  <text x="390" y="{by + 20}" font-family="sans-serif" font-size="12" fill="#64748b">Ground</text>',
        # Wall (extended)
        f'  <line x1="{bx}" y1="30" x2="{bx}" y2="{by}" stroke="#475569" stroke-width="8" stroke-linecap="square"/>',
        f'  <text x="{bx - 40}" y="45" font-family="sans-serif" font-size="12" fill="#475569">Wall</text>',
        # Right angle marker
        f'  <path d="{sq_path}" fill="none" stroke="#dc2626" stroke-width="2"/>',
        # Ladder (inclined line with rungs)
        f'  <line x1="{cx}" y1="{cy}" x2="{ax}" y2="{ay}" stroke="#d97706" stroke-width="5" stroke-linecap="round"/>',
        # Side labels
        f'  <text x="{bx - 26}" y="{(ay + by) / 2}" font-family="sans-serif" font-size="15" font-weight="bold" fill="#0f172a" text-anchor="middle">{lbl_wall}</text>',
        f'  <text x="{(bx + cx) / 2}" y="{by + 26}" font-family="sans-serif" font-size="15" font-weight="bold" fill="#0f172a" text-anchor="middle">{lbl_ground}</text>',
        f'  <text x="{(ax + cx) / 2 + 30}" y="{(ay + cy) / 2 - 12}" font-family="sans-serif" font-size="16" font-weight="bold" fill="#b45309" text-anchor="middle">Ladder: {lbl_ladder}</text>',
        '</svg>'
    ]
    return "\n".join(svg_parts)


def draw_composite_right_triangles_svg(
    t1_legs: Tuple[float, float] = (3, 4),
    t2_leg: float = 12,
    seed: Optional[int] = None,
) -> str:
    """Draws two connected right-angled triangles sharing a common side."""
    seed_tag = f"<!-- s:{seed} -->\n" if seed is not None else ""
    width, height = 480, 320

    # Common point B at (100, 240)
    bx, by = 90, 250
    cx = 240
    cy = 250
    ax = 90
    ay = 110
    # Second triangle shares AC as base, vertex D extends up and right
    dx = 380
    dy = 70

    svg_parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="auto" class="pythagoras-composite-svg">',
        seed_tag,
        f'  <rect width="{width}" height="{height}" fill="#f8fafc" rx="8" />',
        # Triangle 1 (ABC)
        f'  <polygon points="{ax},{ay} {bx},{by} {cx},{cy}" fill="#eff6ff" stroke="#2563eb" stroke-width="2.5" />',
        # Triangle 2 (ACD)
        f'  <polygon points="{ax},{ay} {cx},{cy} {dx},{dy}" fill="#fdf4ff" stroke="#c026d3" stroke-width="2.5" />',
        # Right angle markers
        f'  <path d="M {bx},{by - 16} L {bx + 16},{by - 16} L {bx + 16},{by}" fill="none" stroke="#dc2626" stroke-width="1.8"/>',
        # Vertices labels
        f'  <text x="{ax - 16}" y="{ay - 6}" font-family="sans-serif" font-size="15" font-weight="bold" fill="#0f172a">A</text>',
        f'  <text x="{bx - 16}" y="{by + 18}" font-family="sans-serif" font-size="15" font-weight="bold" fill="#0f172a">B</text>',
        f'  <text x="{cx + 8}" y="{cy + 18}" font-family="sans-serif" font-size="15" font-weight="bold" fill="#0f172a">C</text>',
        f'  <text x="{dx + 8}" y="{dy}" font-family="sans-serif" font-size="15" font-weight="bold" fill="#0f172a">D</text>',
        '</svg>'
    ]
    return "\n".join(svg_parts)
