"""Geometry of 3D Objects SVG Diagram Builders for Grade 9 Mathematics (CAPS Term 4).
Provides crisp, publication-grade SVG figures for 3D polyhedra and curved solids:
- 3D isometric/perspective wireframes with translucent faces and dashed hidden edges
- 2D unfolded geometric nets (cube, rectangular prism, triangular prism, pyramid, cylinder)
- 3D cross-sections showing cutting planes and resulting 2D cross-sectional shapes
Dynamic entropy tag: <!-- s:{seed} -->
"""
from __future__ import annotations

import math
from typing import Any, List, Optional, Tuple


def draw_polyhedron_3d_svg(
    solid_type: str,  # 'cube', 'rectangular_prism', 'triangular_prism', 'square_pyramid', 'tetrahedron', 'cylinder', 'cone', 'octahedron', 'hexagonal_prism'
    labels: Optional[List[str]] = None,
    highlight_part: Optional[str] = None,  # 'face', 'edge', 'vertex', 'apex', 'base'
    seed: Optional[int] = None,
    width: int = 420,
    height: int = 380,
    title: str = "",
) -> str:
    """Generate SVG depicting a 3D solid with dashed hidden edges and shading."""
    s_tag = f"<!-- s:{seed} -->\n" if seed is not None else ""
    w = float(width)
    h = float(height)
    cx = w / 2.0
    cy = h / 2.0 + 10.0

    canonical_blender_key = solid_type if solid_type in (
        "cube", "rectangular_prism", "triangular_prism", "hexagonal_prism",
        "cylinder", "square_pyramid", "triangular_pyramid", "tetrahedron",
        "hexagonal_pyramid", "cone", "sphere", "octahedron", "dodecahedron", "icosahedron"
    ) else "hexagonal_prism"
    blender_exam_plate = f"/diagrams/blender_3d_{canonical_blender_key}_exam_stipple.jpg"
    blender_textbook_plate = f"/diagrams/blender_3d_{canonical_blender_key}_textbook.jpg"
    blender_glb_model = f"/models/blender_3d_{canonical_blender_key}.glb"

    svg_lines = [
        s_tag + f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
        f'width="{width}" height="{height}" '
        f'data-blender-plate="{blender_exam_plate}" '
        f'data-blender-textbook="{blender_textbook_plate}" '
        f'data-model-glb="{blender_glb_model}" '
        f'style="background:#ffffff; font-family:system-ui,-apple-system,sans-serif;">',
        '  <defs>',
        '    <linearGradient id="front-grad" x1="0%" y1="0%" x2="100%" y2="100%">',
        '      <stop offset="0%" stop-color="#3b82f6" stop-opacity="0.22"/>',
        '      <stop offset="100%" stop-color="#1d4ed8" stop-opacity="0.32"/>',
        '    </linearGradient>',
        '    <linearGradient id="top-grad" x1="0%" y1="0%" x2="100%" y2="100%">',
        '      <stop offset="0%" stop-color="#60a5fa" stop-opacity="0.25"/>',
        '      <stop offset="100%" stop-color="#93c5fd" stop-opacity="0.18"/>',
        '    </linearGradient>',
        '    <linearGradient id="side-grad" x1="0%" y1="0%" x2="100%" y2="100%">',
        '      <stop offset="0%" stop-color="#1e40af" stop-opacity="0.25"/>',
        '      <stop offset="100%" stop-color="#1e3a8a" stop-opacity="0.38"/>',
        '    </linearGradient>',
        '    <linearGradient id="pyr-front" x1="0%" y1="0%" x2="100%" y2="100%">',
        '      <stop offset="0%" stop-color="#f59e0b" stop-opacity="0.25"/>',
        '      <stop offset="100%" stop-color="#d97706" stop-opacity="0.38"/>',
        '    </linearGradient>',
        '    <linearGradient id="pyr-side" x1="0%" y1="0%" x2="100%" y2="100%">',
        '      <stop offset="0%" stop-color="#b45309" stop-opacity="0.25"/>',
        '      <stop offset="100%" stop-color="#78350f" stop-opacity="0.38"/>',
        '    </linearGradient>',
        '  </defs>',
        f'  <rect x="0" y="0" width="{width}" height="{height}" fill="#ffffff"/>',
        f'  <image href="{blender_exam_plate}" x="20" y="34" width="{width - 40}" height="{height - 48}" preserveAspectRatio="xMidYMid meet" opacity="0.92"/>',
    ]

    stroke_solid = "#1e293b"
    stroke_dash = "#94a3b8"

    if solid_type in ("cube", "rectangular_prism"):
        dx = 110.0 if solid_type == "rectangular_prism" else 80.0
        dy = 70.0 if solid_type == "rectangular_prism" else 80.0
        slant_x = 55.0
        slant_y = -35.0

        # Front face: A(bottom-left), B(bottom-right), C(top-right), D(top-left)
        ax, ay = cx - dx / 2 - 20, cy + dy / 2
        bx, by = ax + dx, ay
        cx_pt, cy_pt = bx, ay - dy
        dx_pt, dy_pt = ax, cy_pt

        # Back face: A', B', C', D'
        ax_b, ay_b = ax + slant_x, ay + slant_y
        bx_b, by_b = bx + slant_x, by + slant_y
        cx_b, cy_b = cx_pt + slant_x, cy_pt + slant_y
        dx_b, dy_b = dx_pt + slant_x, dy_pt + slant_y

        # Hidden back edges (dashed)
        svg_lines.append(f'  <line x1="{ax}" y1="{ay}" x2="{ax_b}" y2="{ay_b}" stroke="{stroke_dash}" stroke-width="1.8" stroke-dasharray="5,4"/>')
        svg_lines.append(f'  <line x1="{ax_b}" y1="{ay_b}" x2="{bx_b}" y2="{by_b}" stroke="{stroke_dash}" stroke-width="1.8" stroke-dasharray="5,4"/>')
        svg_lines.append(f'  <line x1="{ax_b}" y1="{ay_b}" x2="{dx_b}" y2="{dy_b}" stroke="{stroke_dash}" stroke-width="1.8" stroke-dasharray="5,4"/>')

        # Top face polygon
        top_pts = f"{dx_pt},{dy_pt} {cx_pt},{cy_pt} {cx_b},{cy_b} {dx_b},{dy_b}"
        svg_lines.append(f'  <polygon points="{top_pts}" fill="url(#top-grad)" stroke="{stroke_solid}" stroke-width="2"/>')

        # Right side face polygon
        side_pts = f"{bx},{by} {cx_pt},{cy_pt} {cx_b},{cy_b} {bx_b},{by_b}"
        svg_lines.append(f'  <polygon points="{side_pts}" fill="url(#side-grad)" stroke="{stroke_solid}" stroke-width="2"/>')

        # Front face polygon
        front_pts = f"{ax},{ay} {bx},{by} {cx_pt},{cy_pt} {dx_pt},{dy_pt}"
        svg_lines.append(f'  <polygon points="{front_pts}" fill="url(#front-grad)" stroke="{stroke_solid}" stroke-width="2"/>')

        # Draw vertices dots
        for px, py in [(ax, ay), (bx, by), (cx_pt, cy_pt), (dx_pt, dy_pt), (bx_b, by_b), (cx_b, cy_b), (dx_b, dy_b)]:
            svg_lines.append(f'  <circle cx="{px}" cy="{py}" r="3" fill="#1e293b"/>')
        svg_lines.append(f'  <circle cx="{ax_b}" cy="{ay_b}" r="3" fill="#94a3b8"/>')

    elif solid_type == "triangular_prism":
        # Triangular base on left/front, extruded back-right
        ax, ay = cx - 90, cy + 60
        bx, by = cx + 20, cy + 60
        tx, ty = cx - 35, cy - 50

        sx, sy = 90, -40
        ax_b, ay_b = ax + sx, ay + sy
        bx_b, by_b = bx + sx, by + sy
        tx_b, ty_b = tx + sx, ty + sy

        # Hidden back edges
        svg_lines.append(f'  <line x1="{ax}" y1="{ay}" x2="{ax_b}" y2="{ay_b}" stroke="{stroke_dash}" stroke-width="1.8" stroke-dasharray="5,4"/>')
        svg_lines.append(f'  <line x1="{ax_b}" y1="{ay_b}" x2="{bx_b}" y2="{by_b}" stroke="{stroke_dash}" stroke-width="1.8" stroke-dasharray="5,4"/>')
        svg_lines.append(f'  <line x1="{ax_b}" y1="{ay_b}" x2="{tx_b}" y2="{ty_b}" stroke="{stroke_dash}" stroke-width="1.8" stroke-dasharray="5,4"/>')

        # Bottom/Back side face
        side_pts = f"{bx},{by} {tx},{ty} {tx_b},{ty_b} {bx_b},{by_b}"
        svg_lines.append(f'  <polygon points="{side_pts}" fill="url(#side-grad)" stroke="{stroke_solid}" stroke-width="2"/>')

        # Front triangular face
        front_tri = f"{ax},{ay} {bx},{by} {tx},{ty}"
        svg_lines.append(f'  <polygon points="{front_tri}" fill="url(#front-grad)" stroke="{stroke_solid}" stroke-width="2"/>')

        # Back triangle visible edges
        svg_lines.append(f'  <line x1="{bx_b}" y1="{by_b}" x2="{tx_b}" y2="{ty_b}" stroke="{stroke_solid}" stroke-width="2"/>')

        # Slanted top-left face
        top_pts = f"{ax},{ay} {tx},{ty} {tx_b},{ty_b} {ax_b},{ay_b}"
        svg_lines.append(f'  <polygon points="{top_pts}" fill="url(#top-grad)" stroke="{stroke_solid}" stroke-width="2"/>')

    elif solid_type == "square_pyramid":
        # Base: A, B, C, D (D is rear-left hidden)
        ax, ay = cx - 90, cy + 40
        bx, by = cx + 40, cy + 40
        cx_pt, cy_pt = cx + 90, cy + 5
        dx_pt, dy_pt = cx - 40, cy + 5  # hidden rear vertex
        apex_x, apex_y = cx, cy - 90

        # Hidden rear edges
        svg_lines.append(f'  <line x1="{ax}" y1="{ay}" x2="{dx_pt}" y2="{dy_pt}" stroke="{stroke_dash}" stroke-width="1.8" stroke-dasharray="5,4"/>')
        svg_lines.append(f'  <line x1="{dx_pt}" y1="{dy_pt}" x2="{cx_pt}" y2="{cy_pt}" stroke="{stroke_dash}" stroke-width="1.8" stroke-dasharray="5,4"/>')
        svg_lines.append(f'  <line x1="{dx_pt}" y1="{dy_pt}" x2="{apex_x}" y2="{apex_y}" stroke="{stroke_dash}" stroke-width="1.8" stroke-dasharray="5,4"/>')

        # Base visible edges
        svg_lines.append(f'  <line x1="{ax}" y1="{ay}" x2="{bx}" y2="{by}" stroke="{stroke_solid}" stroke-width="2"/>')
        svg_lines.append(f'  <line x1="{bx}" y1="{by}" x2="{cx_pt}" y2="{cy_pt}" stroke="{stroke_solid}" stroke-width="2"/>')

        # Right lateral triangular face
        right_tri = f"{bx},{by} {cx_pt},{cy_pt} {apex_x},{apex_y}"
        svg_lines.append(f'  <polygon points="{right_tri}" fill="url(#pyr-side)" stroke="{stroke_solid}" stroke-width="2"/>')

        # Front lateral triangular face
        front_tri = f"{ax},{ay} {bx},{by} {apex_x},{apex_y}"
        svg_lines.append(f'  <polygon points="{front_tri}" fill="url(#pyr-front)" stroke="{stroke_solid}" stroke-width="2"/>')

        # Highlight apex
        svg_lines.append(f'  <circle cx="{apex_x}" cy="{apex_y}" r="4" fill="#dc2626"/>')
        svg_lines.append(f'  <text x="{apex_x + 8}" y="{apex_y - 6}" font-size="12" font-weight="bold" fill="#dc2626">Apex</text>')

    elif solid_type == "tetrahedron":
        # Triangular pyramid (all equilateral triangles)
        ax, ay = cx - 85, cy + 45
        bx, by = cx + 75, cy + 45
        cx_pt, cy_pt = cx + 10, cy + 5  # internal/rear vertex
        apex_x, apex_y = cx - 5, cy - 80

        # Hidden rear edges
        svg_lines.append(f'  <line x1="{ax}" y1="{ay}" x2="{cx_pt}" y2="{cy_pt}" stroke="{stroke_dash}" stroke-width="1.8" stroke-dasharray="5,4"/>')
        svg_lines.append(f'  <line x1="{cx_pt}" y1="{cy_pt}" x2="{bx}" y2="{by}" stroke="{stroke_dash}" stroke-width="1.8" stroke-dasharray="5,4"/>')
        svg_lines.append(f'  <line x1="{cx_pt}" y1="{cy_pt}" x2="{apex_x}" y2="{apex_y}" stroke="{stroke_dash}" stroke-width="1.8" stroke-dasharray="5,4"/>')

        # Front base edge
        svg_lines.append(f'  <line x1="{ax}" y1="{ay}" x2="{bx}" y2="{by}" stroke="{stroke_solid}" stroke-width="2"/>')

        # Right face
        r_tri = f"{bx},{by} {apex_x},{apex_y} {cx_pt},{cy_pt}"
        svg_lines.append(f'  <polygon points="{r_tri}" fill="url(#pyr-side)" stroke="{stroke_solid}" stroke-width="2"/>')

        # Front face
        f_tri = f"{ax},{ay} {bx},{by} {apex_x},{apex_y}"
        svg_lines.append(f'  <polygon points="{f_tri}" fill="url(#pyr-front)" stroke="{stroke_solid}" stroke-width="2"/>')

        # Apex dot
        svg_lines.append(f'  <circle cx="{apex_x}" cy="{apex_y}" r="4" fill="#1e293b"/>')

    elif solid_type == "cylinder":
        rx = 70.0
        ry = 22.0
        cyl_h = 130.0
        top_y = cy - cyl_h / 2
        bot_y = cy + cyl_h / 2

        # Cylinder body gradient
        svg_lines.append('  <defs><linearGradient id="cyl-body" x1="0%" y1="0%" x2="100%" y2="0%">'
                         '<stop offset="0%" stop-color="#93c5fd" stop-opacity="0.3"/>'
                         '<stop offset="50%" stop-color="#3b82f6" stop-opacity="0.4"/>'
                         '<stop offset="100%" stop-color="#1d4ed8" stop-opacity="0.6"/>'
                         '</linearGradient></defs>')

        # Body rectangle between ellipses
        svg_lines.append(f'  <rect x="{cx - rx}" y="{top_y}" width="{2*rx}" height="{cyl_h}" fill="url(#cyl-body)"/>')

        # Bottom ellipse: rear half dashed, front half solid
        svg_lines.append(f'  <path d="M {cx - rx} {bot_y} A {rx} {ry} 0 0 1 {cx + rx} {bot_y}" fill="none" stroke="{stroke_dash}" stroke-width="1.8" stroke-dasharray="5,4"/>')
        svg_lines.append(f'  <path d="M {cx - rx} {bot_y} A {rx} {ry} 0 0 0 {cx + rx} {bot_y}" fill="none" stroke="{stroke_solid}" stroke-width="2"/>')

        # Vertical sides
        svg_lines.append(f'  <line x1="{cx - rx}" y1="{top_y}" x2="{cx - rx}" y2="{bot_y}" stroke="{stroke_solid}" stroke-width="2"/>')
        svg_lines.append(f'  <line x1="{cx + rx}" y1="{top_y}" x2="{cx + rx}" y2="{bot_y}" stroke="{stroke_solid}" stroke-width="2"/>')

        # Top ellipse (fully visible)
        svg_lines.append(f'  <ellipse cx="{cx}" cy="{top_y}" rx="{rx}" ry="{ry}" fill="#bfdbfe" stroke="{stroke_solid}" stroke-width="2"/>')

    elif solid_type == "cone":
        rx = 70.0
        ry = 22.0
        cone_h = 140.0
        bot_y = cy + 45
        apex_y = bot_y - cone_h

        # Body fill
        svg_lines.append('  <defs><linearGradient id="cone-body" x1="0%" y1="0%" x2="100%" y2="0%">'
                         '<stop offset="0%" stop-color="#fde68a" stop-opacity="0.4"/>'
                         '<stop offset="60%" stop-color="#f59e0b" stop-opacity="0.5"/>'
                         '<stop offset="100%" stop-color="#b45309" stop-opacity="0.65"/>'
                         '</linearGradient></defs>')
        body_pts = f"{cx - rx},{bot_y} {cx + rx},{bot_y} {cx},{apex_y}"
        svg_lines.append(f'  <polygon points="{body_pts}" fill="url(#cone-body)"/>')

        # Bottom ellipse rear dashed, front solid
        svg_lines.append(f'  <path d="M {cx - rx} {bot_y} A {rx} {ry} 0 0 1 {cx + rx} {bot_y}" fill="none" stroke="{stroke_dash}" stroke-width="1.8" stroke-dasharray="5,4"/>')
        svg_lines.append(f'  <path d="M {cx - rx} {bot_y} A {rx} {ry} 0 0 0 {cx + rx} {bot_y}" fill="none" stroke="{stroke_solid}" stroke-width="2"/>')

        # Lateral sides to apex
        svg_lines.append(f'  <line x1="{cx - rx}" y1="{bot_y}" x2="{cx}" y2="{apex_y}" stroke="{stroke_solid}" stroke-width="2"/>')
        svg_lines.append(f'  <line x1="{cx + rx}" y1="{bot_y}" x2="{cx}" y2="{apex_y}" stroke="{stroke_solid}" stroke-width="2"/>')
        svg_lines.append(f'  <circle cx="{cx}" cy="{apex_y}" r="4" fill="#dc2626"/>')
        svg_lines.append(f'  <text x="{cx + 8}" y="{apex_y - 6}" font-size="12" font-weight="bold" fill="#dc2626">Apex</text>')

    elif solid_type == "octahedron":
        # 8 triangular faces (bipyramid with square equator)
        ax, ay = cx - 80, cy
        bx, by = cx, cy + 25
        cx_pt, cy_pt = cx + 80, cy
        dx_pt, dy_pt = cx, cy - 25  # rear equator vertex
        top_x, top_y = cx, cy - 85
        bot_x, bot_y = cx, cy + 85

        # Hidden rear edges
        svg_lines.append(f'  <line x1="{ax}" y1="{ay}" x2="{dx_pt}" y2="{dy_pt}" stroke="{stroke_dash}" stroke-width="1.8" stroke-dasharray="5,4"/>')
        svg_lines.append(f'  <line x1="{dx_pt}" y1="{dy_pt}" x2="{cx_pt}" y2="{cy_pt}" stroke="{stroke_dash}" stroke-width="1.8" stroke-dasharray="5,4"/>')
        svg_lines.append(f'  <line x1="{dx_pt}" y1="{dy_pt}" x2="{top_x}" y2="{top_y}" stroke="{stroke_dash}" stroke-width="1.8" stroke-dasharray="5,4"/>')
        svg_lines.append(f'  <line x1="{dx_pt}" y1="{dy_pt}" x2="{bot_x}" y2="{bot_y}" stroke="{stroke_dash}" stroke-width="1.8" stroke-dasharray="5,4"/>')

        # Front equatorial edges
        svg_lines.append(f'  <line x1="{ax}" y1="{ay}" x2="{bx}" y2="{by}" stroke="{stroke_solid}" stroke-width="2"/>')
        svg_lines.append(f'  <line x1="{bx}" y1="{by}" x2="{cx_pt}" y2="{cy_pt}" stroke="{stroke_solid}" stroke-width="2"/>')

        # Front top-left face
        f_tl = f"{ax},{ay} {bx},{by} {top_x},{top_y}"
        svg_lines.append(f'  <polygon points="{f_tl}" fill="url(#front-grad)" stroke="{stroke_solid}" stroke-width="2"/>')

        # Front top-right face
        f_tr = f"{bx},{by} {cx_pt},{cy_pt} {top_x},{top_y}"
        svg_lines.append(f'  <polygon points="{f_tr}" fill="url(#side-grad)" stroke="{stroke_solid}" stroke-width="2"/>')

        # Front bottom-left face
        f_bl = f"{ax},{ay} {bx},{by} {bot_x},{bot_y}"
        svg_lines.append(f'  <polygon points="{f_bl}" fill="url(#front-grad)" stroke="{stroke_solid}" stroke-width="2"/>')

        # Front bottom-right face
        f_br = f"{bx},{by} {cx_pt},{cy_pt} {bot_x},{bot_y}"
        svg_lines.append(f'  <polygon points="{f_br}" fill="url(#side-grad)" stroke="{stroke_solid}" stroke-width="2"/>')

    else:  # hexagonal_prism or default
        r = 60.0
        slant_x, slant_y = 60.0, -35.0
        # Hexagon vertices
        pts_front = []
        for i in range(6):
            ang = math.pi / 6 + i * math.pi / 3
            pts_front.append((cx - 30 + r * math.cos(ang), cy + 30 + 0.6 * r * math.sin(ang)))
        pts_back = [(px + slant_x, py + slant_y) for (px, py) in pts_front]

        # Connect back hexagon
        front_str = " ".join(f"{round(px,1)},{round(py,1)}" for (px, py) in pts_front)
        back_str = " ".join(f"{round(px,1)},{round(py,1)}" for (px, py) in pts_back)

        svg_lines.append(f'  <polygon points="{back_str}" fill="url(#top-grad)" stroke="{stroke_dash}" stroke-width="1.8" stroke-dasharray="5,4"/>')
        for (p1, p2) in zip(pts_front, pts_back):
            svg_lines.append(f'  <line x1="{p1[0]}" y1="{p1[1]}" x2="{p2[0]}" y2="{p2[1]}" stroke="{stroke_solid}" stroke-width="2"/>')
        svg_lines.append(f'  <polygon points="{front_str}" fill="url(#front-grad)" stroke="{stroke_solid}" stroke-width="2"/>')

    # Title label
    clean_name = title or solid_type.replace("_", " ").title()
    svg_lines.append(f'  <text x="{cx}" y="28" font-size="14" font-weight="bold" text-anchor="middle" fill="#0f172a">{clean_name}</text>')

    svg_lines.append('</svg>')
    return "\n".join(svg_lines)


def draw_3d_net_svg(
    net_type: str,  # 'cube_t_net', 'cube_cross_net', 'rectangular_prism_net', 'triangular_prism_net', 'square_pyramid_net', 'cylinder_net'
    labels: Optional[List[str]] = None,
    seed: Optional[int] = None,
    width: int = 420,
    height: int = 420,
    title: str = "",
) -> str:
    """Generate SVG depicting a 2D unfolded net of a 3D solid."""
    s_tag = f"<!-- s:{seed} -->\n" if seed is not None else ""
    w = float(width)
    h = float(height)
    cx = w / 2.0
    cy = h / 2.0

    svg_lines = [
        s_tag + f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
        f'width="{width}" height="{height}" style="background:#ffffff; font-family:system-ui,-apple-system,sans-serif;">',
        f'  <rect x="0" y="0" width="{width}" height="{height}" fill="#fafbfc"/>',
    ]

    fill_color = "rgba(59, 130, 246, 0.2)"
    stroke_color = "#2563eb"
    fold_color = "#9333ea"

    if net_type in ("cube_cross_net", "cube_t_net"):
        s = 55.0  # square edge size
        # Standard cross net:
        #       [0]
        #    [1][2][3][4]
        #       [5]
        # Centers relative to center square [2] at (cx, cy)
        squares = [
            (cx, cy - s),       # 0: Top
            (cx - s, cy),       # 1: Left
            (cx, cy),           # 2: Middle (Base)
            (cx + s, cy),       # 3: Right
            (cx + 2 * s, cy),   # 4: Far Right
            (cx, cy + s),       # 5: Bottom
        ]
        lbls = labels or ["1", "2", "3", "4", "5", "6"]
        for idx, (sq_x, sq_y) in enumerate(squares):
            svg_lines.append(f'  <rect x="{sq_x - s/2}" y="{sq_y - s/2}" width="{s}" height="{s}" '
                             f'fill="{fill_color}" stroke="{stroke_color}" stroke-width="2"/>')
            lbl = lbls[idx] if idx < len(lbls) else str(idx + 1)
            svg_lines.append(f'  <text x="{sq_x}" y="{sq_y + 5}" font-size="14" font-weight="bold" '
                             f'text-anchor="middle" fill="#1e40af">{lbl}</text>')

    elif net_type == "triangular_prism_net":
        # 3 central rectangles and 2 triangular flaps on top/bottom of middle rectangle
        rw = 55.0
        rh = 90.0
        # 3 rectangles side by side: left, middle, right
        # middle rectangle at (cx, cy)
        rects = [
            (cx - rw, cy),
            (cx, cy),
            (cx + rw, cy),
        ]
        for (rx_pt, ry_pt) in rects:
            svg_lines.append(f'  <rect x="{rx_pt - rw/2}" y="{ry_pt - rh/2}" width="{rw}" height="{rh}" '
                             f'fill="{fill_color}" stroke="{stroke_color}" stroke-width="2"/>')

        # Top triangle attached to middle rectangle
        top_tri = f"{cx - rw/2},{cy - rh/2} {cx + rw/2},{cy - rh/2} {cx},{cy - rh/2 - 45}"
        svg_lines.append(f'  <polygon points="{top_tri}" fill="rgba(16, 185, 129, 0.25)" stroke="#059669" stroke-width="2"/>')

        # Bottom triangle attached to middle rectangle
        bot_tri = f"{cx - rw/2},{cy + rh/2} {cx + rw/2},{cy + rh/2} {cx},{cy + rh/2 + 45}"
        svg_lines.append(f'  <polygon points="{bot_tri}" fill="rgba(16, 185, 129, 0.25)" stroke="#059669" stroke-width="2"/>')

        svg_lines.append(f'  <text x="{cx}" y="{cy}" font-size="12" font-weight="bold" text-anchor="middle" fill="#1e40af">Base</text>')

    elif net_type == "square_pyramid_net":
        s = 80.0
        # Central square
        svg_lines.append(f'  <rect x="{cx - s/2}" y="{cy - s/2}" width="{s}" height="{s}" '
                         f'fill="rgba(245, 158, 11, 0.25)" stroke="#d97706" stroke-width="2"/>')
        svg_lines.append(f'  <text x="{cx}" y="{cy + 4}" font-size="12" font-weight="bold" text-anchor="middle" fill="#b45309">Square Base</text>')

        # 4 triangular flaps
        h_tri = 70.0
        # Top triangle
        svg_lines.append(f'  <polygon points="{cx - s/2},{cy - s/2} {cx + s/2},{cy - s/2} {cx},{cy - s/2 - h_tri}" '
                         f'fill="{fill_color}" stroke="{stroke_color}" stroke-width="2"/>')
        # Bottom triangle
        svg_lines.append(f'  <polygon points="{cx - s/2},{cy + s/2} {cx + s/2},{cy + s/2} {cx},{cy + s/2 + h_tri}" '
                         f'fill="{fill_color}" stroke="{stroke_color}" stroke-width="2"/>')
        # Left triangle
        svg_lines.append(f'  <polygon points="{cx - s/2},{cy - s/2} {cx - s/2},{cy + s/2} {cx - s/2 - h_tri},{cy}" '
                         f'fill="{fill_color}" stroke="{stroke_color}" stroke-width="2"/>')
        # Right triangle
        svg_lines.append(f'  <polygon points="{cx + s/2},{cy - s/2} {cx + s/2},{cy + s/2} {cx + s/2 + h_tri},{cy}" '
                         f'fill="{fill_color}" stroke="{stroke_color}" stroke-width="2"/>')

    elif net_type == "cylinder_net":
        # 1 central rectangle and 2 circular lids
        rw = 180.0
        rh = 90.0
        r_lid = 32.0
        svg_lines.append(f'  <rect x="{cx - rw/2}" y="{cy - rh/2}" width="{rw}" height="{rh}" '
                         f'fill="{fill_color}" stroke="{stroke_color}" stroke-width="2"/>')
        svg_lines.append(f'  <text x="{cx}" y="{cy + 4}" font-size="12" font-weight="bold" text-anchor="middle" fill="#1e40af">Curved Surface (Rectangle: 2πr × h)</text>')

        # Top circle lid
        svg_lines.append(f'  <circle cx="{cx - 30}" cy="{cy - rh/2 - r_lid}" r="{r_lid}" '
                         f'fill="rgba(16, 185, 129, 0.25)" stroke="#059669" stroke-width="2"/>')
        svg_lines.append(f'  <text x="{cx - 30}" y="{cy - rh/2 - r_lid + 4}" font-size="11" font-weight="bold" text-anchor="middle" fill="#047857">Circular Lid</text>')

        # Bottom circle lid
        svg_lines.append(f'  <circle cx="{cx + 30}" cy="{cy + rh/2 + r_lid}" r="{r_lid}" '
                         f'fill="rgba(16, 185, 129, 0.25)" stroke="#059669" stroke-width="2"/>')
        svg_lines.append(f'  <text x="{cx + 30}" y="{cy + rh/2 + r_lid + 4}" font-size="11" font-weight="bold" text-anchor="middle" fill="#047857">Circular Base</text>')

    else:  # rectangular_prism_net
        rw = 50.0
        rh = 90.0
        top_h = 40.0
        # 4 rectangular faces in row, flanked by 2 end rectangles
        rects = [
            (cx - 1.5 * rw, cy, rw, rh),
            (cx - 0.5 * rw, cy, rw, rh),
            (cx + 0.5 * rw, cy, rw, rh),
            (cx + 1.5 * rw, cy, rw, rh),
        ]
        for (rx_pt, ry_pt, w_val, h_val) in rects:
            svg_lines.append(f'  <rect x="{rx_pt - w_val/2}" y="{ry_pt - h_val/2}" width="{w_val}" height="{h_val}" '
                             f'fill="{fill_color}" stroke="{stroke_color}" stroke-width="2"/>')
        # Flaps on second rectangle
        fx = cx - 0.5 * rw
        svg_lines.append(f'  <rect x="{fx - rw/2}" y="{cy - rh/2 - top_h}" width="{rw}" height="{top_h}" '
                         f'fill="rgba(16, 185, 129, 0.25)" stroke="#059669" stroke-width="2"/>')
        svg_lines.append(f'  <rect x="{fx - rw/2}" y="{cy + rh/2}" width="{rw}" height="{top_h}" '
                         f'fill="rgba(16, 185, 129, 0.25)" stroke="#059669" stroke-width="2"/>')

    # Title
    clean_title = title or net_type.replace("_", " ").title()
    svg_lines.append(f'  <text x="{cx}" y="24" font-size="13" font-weight="bold" text-anchor="middle" fill="#0f172a">{clean_title}</text>')

    svg_lines.append('</svg>')
    return "\n".join(svg_lines)


def draw_cross_section_svg(
    solid_type: str,  # 'cube', 'cylinder', 'cone', 'pyramid', 'sphere'
    cut_plane: str,    # 'horizontal', 'vertical', 'diagonal'
    result_shape: str, # 'square', 'circle', 'rectangle', 'triangle', 'ellipse'
    seed: Optional[int] = None,
    width: int = 420,
    height: int = 380,
) -> str:
    """Generate SVG depicting a 3D solid sliced by a cutting plane with the cross-section shape highlighted."""
    s_tag = f"<!-- s:{seed} -->\n" if seed is not None else ""
    w = float(width)
    h = float(height)
    cx = w / 2.0
    cy = h / 2.0

    svg_lines = [
        s_tag + f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
        f'width="{width}" height="{height}" style="background:#ffffff; font-family:system-ui,-apple-system,sans-serif;">',
        f'  <rect x="0" y="0" width="{width}" height="{height}" fill="#fafbfc"/>',
    ]

    # Draw solid outline in soft grey/blue
    if solid_type == "cylinder":
        rx, ry = 65.0, 20.0
        top_y, bot_y = cy - 65, cy + 65
        svg_lines.append(f'  <rect x="{cx - rx}" y="{top_y}" width="{2*rx}" height="130" fill="rgba(226, 232, 240, 0.5)"/>')
        svg_lines.append(f'  <ellipse cx="{cx}" cy="{top_y}" rx="{rx}" ry="{ry}" fill="#f1f5f9" stroke="#94a3b8" stroke-width="1.5"/>')
        svg_lines.append(f'  <ellipse cx="{cx}" cy="{bot_y}" rx="{rx}" ry="{ry}" fill="#f1f5f9" stroke="#94a3b8" stroke-width="1.5"/>')
        svg_lines.append(f'  <line x1="{cx - rx}" y1="{top_y}" x2="{cx - rx}" y2="{bot_y}" stroke="#94a3b8" stroke-width="1.5"/>')
        svg_lines.append(f'  <line x1="{cx + rx}" y1="{top_y}" x2="{cx + rx}" y2="{bot_y}" stroke="#94a3b8" stroke-width="1.5"/>')

        if cut_plane == "horizontal":
            # Cutting plane horizontally
            cut_y = cy
            plane_pts = f"{cx - 95},{cut_y - 12} {cx + 95},{cut_y - 12} {cx + 80},{cut_y + 16} {cx - 110},{cut_y + 16}"
            svg_lines.append(f'  <polygon points="{plane_pts}" fill="rgba(244, 63, 94, 0.2)" stroke="#f43f5e" stroke-width="1.5" stroke-dasharray="4,3"/>')
            # Highlighted circular cross-section
            svg_lines.append(f'  <ellipse cx="{cx}" cy="{cut_y}" rx="{rx}" ry="{ry}" fill="rgba(239, 68, 68, 0.45)" stroke="#dc2626" stroke-width="2.5"/>')
            svg_lines.append(f'  <text x="{cx + rx + 14}" y="{cut_y + 5}" font-size="12" font-weight="bold" fill="#dc2626">Cross-section: Circle</text>')

        else:  # vertical cut
            plane_pts = f"{cx - 15},{top_y - 20} {cx + 15},{top_y - 20} {cx + 15},{bot_y + 20} {cx - 15},{bot_y + 20}"
            svg_lines.append(f'  <polygon points="{plane_pts}" fill="rgba(244, 63, 94, 0.2)" stroke="#f43f5e" stroke-width="1.5" stroke-dasharray="4,3"/>')
            # Rectangular cross section
            svg_lines.append(f'  <rect x="{cx - 25}" y="{top_y}" width="50" height="130" fill="rgba(239, 68, 68, 0.45)" stroke="#dc2626" stroke-width="2.5"/>')
            svg_lines.append(f'  <text x="{cx + 35}" y="{cy}" font-size="12" font-weight="bold" fill="#dc2626">Cross-section: Rectangle</text>')

    elif solid_type == "cone":
        rx, ry = 65.0, 20.0
        bot_y = cy + 60
        apex_y = bot_y - 130
        body_pts = f"{cx - rx},{bot_y} {cx + rx},{bot_y} {cx},{apex_y}"
        svg_lines.append(f'  <polygon points="{body_pts}" fill="rgba(226, 232, 240, 0.5)" stroke="#94a3b8" stroke-width="1.5"/>')
        svg_lines.append(f'  <ellipse cx="{cx}" cy="{bot_y}" rx="{rx}" ry="{ry}" fill="#f1f5f9" stroke="#94a3b8" stroke-width="1.5"/>')

        if cut_plane == "horizontal":
            cut_y = cy
            scale = (cut_y - apex_y) / (bot_y - apex_y)
            c_rx, c_ry = rx * scale, ry * scale
            plane_pts = f"{cx - 85},{cut_y - 12} {cx + 85},{cut_y - 12} {cx + 70},{cut_y + 16} {cx - 100},{cut_y + 16}"
            svg_lines.append(f'  <polygon points="{plane_pts}" fill="rgba(244, 63, 94, 0.2)" stroke="#f43f5e" stroke-width="1.5" stroke-dasharray="4,3"/>')
            svg_lines.append(f'  <ellipse cx="{cx}" cy="{cut_y}" rx="{c_rx}" ry="{c_ry}" fill="rgba(239, 68, 68, 0.45)" stroke="#dc2626" stroke-width="2.5"/>')
            svg_lines.append(f'  <text x="{cx + c_rx + 14}" y="{cut_y + 5}" font-size="12" font-weight="bold" fill="#dc2626">Cross-section: Circle</text>')
        else:  # vertical cut through apex
            tri_pts = f"{cx - rx},{bot_y} {cx + rx},{bot_y} {cx},{apex_y}"
            svg_lines.append(f'  <polygon points="{tri_pts}" fill="rgba(239, 68, 68, 0.45)" stroke="#dc2626" stroke-width="2.5"/>')
            svg_lines.append(f'  <text x="{cx + 25}" y="{cy}" font-size="12" font-weight="bold" fill="#dc2626">Cross-section: Isosceles Triangle</text>')

    else:  # cube or rectangular prism
        s = 100.0
        sx, sy = 50.0, -30.0
        # Cube outline
        ax, ay = cx - s/2 - 15, cy + s/2
        bx, by = ax + s, ay
        cx_pt, cy_pt = bx, ay - s
        dx_pt, dy_pt = ax, cy_pt

        front_pts = f"{ax},{ay} {bx},{by} {cx_pt},{cy_pt} {dx_pt},{dy_pt}"
        svg_lines.append(f'  <polygon points="{front_pts}" fill="rgba(226, 232, 240, 0.4)" stroke="#94a3b8" stroke-width="1.5"/>')
        top_pts = f"{dx_pt},{dy_pt} {cx_pt},{cy_pt} {cx_pt + sx},{cy_pt + sy} {dx_pt + sx},{dy_pt + sy}"
        svg_lines.append(f'  <polygon points="{top_pts}" fill="rgba(241, 245, 249, 0.4)" stroke="#94a3b8" stroke-width="1.5"/>')
        side_pts = f"{bx},{by} {cx_pt},{cy_pt} {cx_pt + sx},{cy_pt + sy} {bx + sx},{by + sy}"
        svg_lines.append(f'  <polygon points="{side_pts}" fill="rgba(203, 213, 225, 0.4)" stroke="#94a3b8" stroke-width="1.5"/>')

        if cut_plane == "horizontal":
            cut_y = cy
            c_pts = f"{ax},{cut_y} {bx},{cut_y} {bx + sx},{cut_y + sy} {ax + sx},{cut_y + sy}"
            svg_lines.append(f'  <polygon points="{c_pts}" fill="rgba(239, 68, 68, 0.45)" stroke="#dc2626" stroke-width="2.5"/>')
            svg_lines.append(f'  <text x="{bx + sx + 10}" y="{cut_y + sy}" font-size="12" font-weight="bold" fill="#dc2626">Cross-section: Square</text>')
        else:  # diagonal cut
            c_pts = f"{ax},{ay} {bx + sx},{by + sy} {cx_pt + sx},{cy_pt + sy} {dx_pt},{dy_pt}"
            svg_lines.append(f'  <polygon points="{c_pts}" fill="rgba(239, 68, 68, 0.45)" stroke="#dc2626" stroke-width="2.5"/>')
            svg_lines.append(f'  <text x="{bx + sx + 10}" y="{cy}" font-size="12" font-weight="bold" fill="#dc2626">Cross-section: Rectangle</text>')

    title_str = f"{solid_type.title()} — {cut_plane.title()} Cross-section ({result_shape.title()})"
    svg_lines.append(f'  <text x="{cx}" y="24" font-size="13" font-weight="bold" text-anchor="middle" fill="#0f172a">{title_str}</text>')
    svg_lines.append('</svg>')
    return "\n".join(svg_lines)
