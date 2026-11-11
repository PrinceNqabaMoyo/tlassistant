"""Transformation Geometry SVG Diagram Builders for Grade 9 Mathematics (CAPS Term 3).
Provides crisp, responsive SVG figures on Cartesian grids and geometric shapes:
- Cartesian grids with axes, tick marks, and integer coordinates
- Pre-image and image polygons (points, line segments, triangles, quadrilaterals)
- Dedicated transformation visual cues:
  * Translation vectors with arrowheads
  * Reflection mirror lines with perpendicular projection dashed segments
  * Rotation center, radial lines, and angular rotation arcs
  * Enlargement/reduction projection rays from center of dilation
  * Lines of symmetry and rotational symmetry centers for 2D polygons
Dynamic entropy tag: <!-- s:{seed} -->
"""
from __future__ import annotations

import math
from typing import Any, List, Optional, Tuple


def _to_screen(
    x: float, y: float,
    x_min: float, x_max: float,
    y_min: float, y_max: float,
    w: float, h: float, pad: float
) -> Tuple[float, float]:
    """Map Cartesian coordinates (x, y) to SVG screen coordinates (sx, sy)."""
    sx = pad + (x - x_min) / (x_max - x_min) * (w - 2 * pad)
    sy = h - pad - (y - y_min) / (y_max - y_min) * (h - 2 * pad)
    return round(sx, 2), round(sy, 2)


def draw_transformation_grid_svg(
    pre_image: List[Tuple[float, float]],
    image: Optional[List[Tuple[float, float]]] = None,
    pre_labels: Optional[List[str]] = None,
    image_labels: Optional[List[str]] = None,
    transformation_type: str = "none",  # 'translation', 'reflection', 'rotation', 'enlargement', 'none'
    mirror_line: Optional[str] = None,  # 'x_axis', 'y_axis', 'y=x', 'y=-x', 'x=c', 'y=c'
    mirror_c: float = 0,
    rotation_center: Tuple[float, float] = (0, 0),
    rotation_angle_deg: float = 90,
    dilation_center: Tuple[float, float] = (0, 0),
    scale_factor: float = 1.0,
    seed: Optional[int] = None,
    grid_extent: int = 6,
    width: int = 480,
    height: int = 480,
    title: str = "",
) -> str:
    """Generate Cartesian grid SVG with pre-image, image, and transformation guides."""
    s_tag = f"<!-- s:{seed} -->\n" if seed is not None else ""
    pad = 40.0
    w = float(width)
    h = float(height)

    # Determine bounding box
    all_pts = list(pre_image)
    if image:
        all_pts.extend(image)
    
    max_coord = max([abs(p[0]) for p in all_pts] + [abs(p[1]) for p in all_pts] + [grid_extent])
    ext = int(math.ceil(max_coord)) + 1
    ext = max(ext, 5)
    x_min, x_max = -ext, ext
    y_min, y_max = -ext, ext

    # Coordinate mapping closure
    def pt(coord: Tuple[float, float]) -> Tuple[float, float]:
        return _to_screen(coord[0], coord[1], x_min, x_max, y_min, y_max, w, h, pad)

    svg_lines = [
        s_tag + f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
        f'width="{width}" height="{height}" style="background:#ffffff; font-family:system-ui,-apple-system,sans-serif;">',
        '  <defs>',
        '    <marker id="arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">',
        '      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#1e293b"/>',
        '    </marker>',
        '    <marker id="trans-arrow" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">',
        '      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#f59e0b"/>',
        '    </marker>',
        '    <marker id="rot-arrow" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">',
        '      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#8b5cf6"/>',
        '    </marker>',
        '  </defs>',
    ]

    # Grid background rect
    svg_lines.append(f'  <rect x="0" y="0" width="{width}" height="{height}" fill="#fafbfc"/>')

    # Grid lines
    for i in range(x_min, x_max + 1):
        if i == 0:
            continue
        sx1, sy1 = pt((i, y_min))
        sx2, sy2 = pt((i, y_max))
        svg_lines.append(f'  <line x1="{sx1}" y1="{sy1}" x2="{sx2}" y2="{sy2}" stroke="#e2e8f0" stroke-width="1"/>')
    for j in range(y_min, y_max + 1):
        if j == 0:
            continue
        sx1, sy1 = pt((x_min, j))
        sx2, sy2 = pt((x_max, j))
        svg_lines.append(f'  <line x1="{sx1}" y1="{sy1}" x2="{sx2}" y2="{sy2}" stroke="#e2e8f0" stroke-width="1"/>')

    # Main Axes
    ox, oy = pt((0, 0))
    ax_x1, ax_y1 = pt((x_min, 0))
    ax_x2, ax_y2 = pt((x_max, 0))
    ay_x1, ay_y1 = pt((0, y_min))
    ay_x2, ay_y2 = pt((0, y_max))

    # X-axis
    svg_lines.append(f'  <line x1="{ax_x1}" y1="{ax_y1}" x2="{ax_x2}" y2="{ax_y2}" stroke="#1e293b" stroke-width="2" marker-end="url(#arrow)"/>')
    svg_lines.append(f'  <text x="{ax_x2 - 12}" y="{ax_y2 - 10}" font-size="14" font-weight="600" fill="#1e293b">x</text>')

    # Y-axis
    svg_lines.append(f'  <line x1="{ay_x1}" y1="{ay_y1}" x2="{ay_x2}" y2="{ay_y2}" stroke="#1e293b" stroke-width="2" marker-end="url(#arrow)"/>')
    svg_lines.append(f'  <text x="{ay_x2 + 10}" y="{ay_y2 + 14}" font-size="14" font-weight="600" fill="#1e293b">y</text>')

    # Axis Numbers and Ticks
    for i in range(x_min + 1, x_max):
        if i == 0:
            continue
        tx, ty = pt((i, 0))
        svg_lines.append(f'  <line x1="{tx}" y1="{ty - 3}" x2="{tx}" y2="{ty + 3}" stroke="#475569" stroke-width="1.5"/>')
        svg_lines.append(f'  <text x="{tx}" y="{ty + 15}" font-size="10" text-anchor="middle" fill="#64748b">{i}</text>')

    for j in range(y_min + 1, y_max):
        if j == 0:
            continue
        tx, ty = pt((0, j))
        svg_lines.append(f'  <line x1="{tx - 3}" y1="{ty}" x2="{tx + 3}" y2="{ty}" stroke="#475569" stroke-width="1.5"/>')
        svg_lines.append(f'  <text x="{tx - 8}" y="{ty + 3}" font-size="10" text-anchor="end" fill="#64748b">{j}</text>')

    # Origin label
    svg_lines.append(f'  <text x="{ox - 8}" y="{oy + 14}" font-size="11" font-weight="600" fill="#475569">O</text>')

    # Transformation guides
    if transformation_type == "reflection" and mirror_line:
        # Draw mirror line
        if mirror_line == "x_axis":
            svg_lines.append(f'  <line x1="{ax_x1}" y1="{ax_y1}" x2="{ax_x2}" y2="{ax_y2}" stroke="#dc2626" stroke-width="2.5" stroke-dasharray="6,4"/>')
            svg_lines.append(f'  <text x="{ax_x2 - 80}" y="{ax_y2 + 18}" font-size="11" font-weight="bold" fill="#dc2626">Mirror: x-axis</text>')
        elif mirror_line == "y_axis":
            svg_lines.append(f'  <line x1="{ay_x1}" y1="{ay_y1}" x2="{ay_x2}" y2="{ay_y2}" stroke="#dc2626" stroke-width="2.5" stroke-dasharray="6,4"/>')
            svg_lines.append(f'  <text x="{ay_x1 + 10}" y="{ay_y1 - 10}" font-size="11" font-weight="bold" fill="#dc2626">Mirror: y-axis</text>')
        elif mirror_line == "y=x":
            mx1, my1 = pt((x_min, x_min))
            mx2, my2 = pt((x_max, x_max))
            svg_lines.append(f'  <line x1="{mx1}" y1="{my1}" x2="{mx2}" y2="{my2}" stroke="#9333ea" stroke-width="2.5" stroke-dasharray="6,4"/>')
            svg_lines.append(f'  <text x="{mx2 - 40}" y="{my2 + 16}" font-size="11" font-weight="bold" fill="#9333ea">y = x</text>')
        elif mirror_line == "y=-x":
            mx1, my1 = pt((x_min, -x_min))
            mx2, my2 = pt((x_max, -x_max))
            svg_lines.append(f'  <line x1="{mx1}" y1="{my1}" x2="{mx2}" y2="{my2}" stroke="#9333ea" stroke-width="2.5" stroke-dasharray="6,4"/>')
            svg_lines.append(f'  <text x="{mx2 - 40}" y="{my2 + 16}" font-size="11" font-weight="bold" fill="#9333ea">y = -x</text>')
        elif mirror_line == "x=c":
            mx1, my1 = pt((mirror_c, y_min))
            mx2, my2 = pt((mirror_c, y_max))
            svg_lines.append(f'  <line x1="{mx1}" y1="{my1}" x2="{mx2}" y2="{my2}" stroke="#dc2626" stroke-width="2.5" stroke-dasharray="6,4"/>')
            svg_lines.append(f'  <text x="{mx2 + 6}" y="{my2 + 14}" font-size="11" font-weight="bold" fill="#dc2626">x = {int(mirror_c)}</text>')
        elif mirror_line == "y=c":
            mx1, my1 = pt((x_min, mirror_c))
            mx2, my2 = pt((x_max, mirror_c))
            svg_lines.append(f'  <line x1="{mx1}" y1="{my1}" x2="{mx2}" y2="{my2}" stroke="#dc2626" stroke-width="2.5" stroke-dasharray="6,4"/>')
            svg_lines.append(f'  <text x="{mx2 - 60}" y="{my2 - 6}" font-size="11" font-weight="bold" fill="#dc2626">y = {int(mirror_c)}</text>')

        # Dashed perpendicular connectors between corresponding vertices
        if image and len(image) == len(pre_image):
            for p1, p2 in zip(pre_image, image):
                sx1, sy1 = pt(p1)
                sx2, sy2 = pt(p2)
                svg_lines.append(f'  <line x1="{sx1}" y1="{sy1}" x2="{sx2}" y2="{sy2}" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="3,3"/>')

    elif transformation_type == "translation" and image and len(image) == len(pre_image):
        # Dashed translation vector arrows
        for p1, p2 in zip(pre_image, image):
            sx1, sy1 = pt(p1)
            sx2, sy2 = pt(p2)
            svg_lines.append(f'  <line x1="{sx1}" y1="{sy1}" x2="{sx2}" y2="{sy2}" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="4,3" marker-end="url(#trans-arrow)"/>')

    elif transformation_type == "rotation":
        cx, cy = pt(rotation_center)
        # Highlight rotation center
        svg_lines.append(f'  <circle cx="{cx}" cy="{cy}" r="4" fill="#8b5cf6" stroke="#ffffff" stroke-width="1.5"/>')
        svg_lines.append(f'  <text x="{cx + 6}" y="{cy - 6}" font-size="11" font-weight="bold" fill="#8b5cf6">Center</text>')
        if image and len(image) == len(pre_image) and len(pre_image) > 0:
            # Draw rotation guide for the first vertex
            p1 = pre_image[0]
            p2 = image[0]
            sx1, sy1 = pt(p1)
            sx2, sy2 = pt(p2)
            svg_lines.append(f'  <line x1="{cx}" y1="{cy}" x2="{sx1}" y2="{sy1}" stroke="#8b5cf6" stroke-width="1" stroke-dasharray="3,3"/>')
            svg_lines.append(f'  <line x1="{cx}" y1="{cy}" x2="{sx2}" y2="{sy2}" stroke="#8b5cf6" stroke-width="1" stroke-dasharray="3,3"/>')

    elif transformation_type == "enlargement":
        cx, cy = pt(dilation_center)
        svg_lines.append(f'  <circle cx="{cx}" cy="{cy}" r="4" fill="#0284c7" stroke="#ffffff" stroke-width="1.5"/>')
        svg_lines.append(f'  <text x="{cx + 6}" y="{cy - 6}" font-size="11" font-weight="bold" fill="#0284c7">Center O</text>')
        if image and len(image) == len(pre_image):
            # Projection rays from dilation center through vertices
            for p1, p2 in zip(pre_image, image):
                sx1, sy1 = pt(p1)
                sx2, sy2 = pt(p2)
                # Extend ray slightly past image
                svg_lines.append(f'  <line x1="{cx}" y1="{cy}" x2="{sx2}" y2="{sy2}" stroke="#38bdf8" stroke-width="1" stroke-dasharray="4,3"/>')

    # Draw Pre-image polygon/points
    if len(pre_image) == 1:
        sx, sy = pt(pre_image[0])
        svg_lines.append(f'  <circle cx="{sx}" cy="{sy}" r="5" fill="#2563eb" stroke="#ffffff" stroke-width="1.5"/>')
        lbl = pre_labels[0] if pre_labels else f"P({pre_image[0][0]}; {pre_image[0][1]})"
        svg_lines.append(f'  <text x="{sx + 8}" y="{sy - 8}" font-size="12" font-weight="bold" fill="#1d4ed8">{lbl}</text>')
    elif len(pre_image) == 2:
        sx1, sy1 = pt(pre_image[0])
        sx2, sy2 = pt(pre_image[1])
        svg_lines.append(f'  <line x1="{sx1}" y1="{sy1}" x2="{sx2}" y2="{sy2}" stroke="#2563eb" stroke-width="2.5"/>')
        for idx, (px, py) in enumerate(pre_image):
            sx, sy = pt((px, py))
            svg_lines.append(f'  <circle cx="{sx}" cy="{sy}" r="4" fill="#2563eb"/>')
            lbl = pre_labels[idx] if pre_labels and idx < len(pre_labels) else f"P{idx+1}({px}; {py})"
            svg_lines.append(f'  <text x="{sx + 6}" y="{sy - 6}" font-size="11" font-weight="bold" fill="#1d4ed8">{lbl}</text>')
    else:
        # Polygon (triangle or quadrilateral)
        pts_str = " ".join(f"{pt(p)[0]},{pt(p)[1]}" for p in pre_image)
        svg_lines.append(f'  <polygon points="{pts_str}" fill="rgba(37, 99, 235, 0.2)" stroke="#2563eb" stroke-width="2.2"/>')
        for idx, (px, py) in enumerate(pre_image):
            sx, sy = pt((px, py))
            svg_lines.append(f'  <circle cx="{sx}" cy="{sy}" r="4" fill="#2563eb"/>')
            lbl = pre_labels[idx] if pre_labels and idx < len(pre_labels) else f"{chr(65+idx)}({px}; {py})"
            svg_lines.append(f'  <text x="{sx + 6}" y="{sy - 6}" font-size="11" font-weight="bold" fill="#1d4ed8">{lbl}</text>')

    # Draw Image polygon/points (if provided)
    if image:
        if len(image) == 1:
            sx, sy = pt(image[0])
            svg_lines.append(f'  <circle cx="{sx}" cy="{sy}" r="5" fill="#059669" stroke="#ffffff" stroke-width="1.5"/>')
            lbl = image_labels[0] if image_labels else f"P'({image[0][0]}; {image[0][1]})"
            svg_lines.append(f'  <text x="{sx + 8}" y="{sy - 8}" font-size="12" font-weight="bold" fill="#047857">{lbl}</text>')
        elif len(image) == 2:
            sx1, sy1 = pt(image[0])
            sx2, sy2 = pt(image[1])
            svg_lines.append(f'  <line x1="{sx1}" y1="{sy1}" x2="{sx2}" y2="{sy2}" stroke="#059669" stroke-width="2.5"/>')
            for idx, (px, py) in enumerate(image):
                sx, sy = pt((px, py))
                svg_lines.append(f'  <circle cx="{sx}" cy="{sy}" r="4" fill="#059669"/>')
                lbl = image_labels[idx] if image_labels and idx < len(image_labels) else f"P'{idx+1}({px}; {py})"
                svg_lines.append(f'  <text x="{sx + 6}" y="{sy - 6}" font-size="11" font-weight="bold" fill="#047857">{lbl}</text>')
        else:
            pts_str = " ".join(f"{pt(p)[0]},{pt(p)[1]}" for p in image)
            svg_lines.append(f'  <polygon points="{pts_str}" fill="rgba(5, 150, 105, 0.2)" stroke="#059669" stroke-width="2.2"/>')
            for idx, (px, py) in enumerate(image):
                sx, sy = pt((px, py))
                svg_lines.append(f'  <circle cx="{sx}" cy="{sy}" r="4" fill="#059669"/>')
                lbl = image_labels[idx] if image_labels and idx < len(image_labels) else f"{chr(65+idx)}'({px}; {py})"
                svg_lines.append(f'  <text x="{sx + 6}" y="{sy - 6}" font-size="11" font-weight="bold" fill="#047857">{lbl}</text>')

    # Legend / Title
    if title:
        svg_lines.append(f'  <text x="{w/2}" y="22" font-size="13" font-weight="bold" text-anchor="middle" fill="#0f172a">{title}</text>')

    # Legend box
    if image:
        svg_lines.append('  <g transform="translate(15, 38)">')
        svg_lines.append('    <rect x="0" y="0" width="165" height="42" rx="4" fill="rgba(255,255,255,0.92)" stroke="#cbd5e1" stroke-width="1"/>')
        svg_lines.append('    <line x1="8" y1="14" x2="28" y2="14" stroke="#2563eb" stroke-width="2.5"/>')
        svg_lines.append('    <text x="34" y="17" font-size="11" fill="#1e293b">Pre-image</text>')
        svg_lines.append('    <line x1="8" y1="30" x2="28" y2="30" stroke="#059669" stroke-width="2.5"/>')
        svg_lines.append('    <text x="34" y="33" font-size="11" fill="#1e293b">Image</text>')
        svg_lines.append('  </g>')

    svg_lines.append('</svg>')
    return "\n".join(svg_lines)


def draw_symmetry_polygon_svg(
    polygon_type: str,  # 'equilateral_triangle', 'square', 'regular_pentagon', 'regular_hexagon', 'rectangle', 'rhombus', 'kite', 'parallelogram'
    show_lines: bool = True,
    seed: Optional[int] = None,
    width: int = 420,
    height: int = 420,
) -> str:
    """Generate SVG depicting a polygon and its lines of symmetry / rotational symmetry."""
    s_tag = f"<!-- s:{seed} -->\n" if seed is not None else ""
    w = float(width)
    h = float(height)
    cx = w / 2.0
    cy = h / 2.0
    r = 140.0

    svg_lines = [
        s_tag + f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
        f'width="{width}" height="{height}" style="background:#ffffff; font-family:system-ui,-apple-system,sans-serif;">',
        '  <defs>',
        '    <linearGradient id="poly-grad" x1="0%" y1="0%" x2="100%" y2="100%">',
        '      <stop offset="0%" stop-color="#eff6ff"/>',
        '      <stop offset="100%" stop-color="#dbeafe"/>',
        '    </linearGradient>',
        '  </defs>',
        f'  <rect x="0" y="0" width="{width}" height="{height}" fill="#fafbfc"/>',
    ]

    sym_lines: List[Tuple[float, float, float, float]] = []
    pts: List[Tuple[float, float]] = []

    if polygon_type == "equilateral_triangle":
        # 3 vertices
        for k in range(3):
            angle = -math.pi / 2 + k * 2 * math.pi / 3
            pts.append((cx + r * math.cos(angle), cy + r * math.sin(angle)))
        if show_lines:
            for k in range(3):
                p_opp = pts[k]
                mid_x = (pts[(k+1)%3][0] + pts[(k+2)%3][0]) / 2
                mid_y = (pts[(k+1)%3][1] + pts[(k+2)%3][1]) / 2
                # Extend line
                dx = mid_x - p_opp[0]
                dy = mid_y - p_opp[1]
                sym_lines.append((p_opp[0] - 0.2 * dx, p_opp[1] - 0.2 * dy, mid_x + 0.3 * dx, mid_y + 0.3 * dy))

    elif polygon_type == "square":
        # 4 vertices rotated 45 deg
        for k in range(4):
            angle = -math.pi / 4 + k * math.pi / 2
            pts.append((cx + r * math.cos(angle), cy + r * math.sin(angle)))
        if show_lines:
            # 2 diagonals
            sym_lines.append((pts[0][0], pts[0][1], pts[2][0], pts[2][1]))
            sym_lines.append((pts[1][0], pts[1][1], pts[3][0], pts[3][1]))
            # 2 edge bisectors
            sym_lines.append(((pts[0][0]+pts[1][0])/2, (pts[0][1]+pts[1][1])/2, (pts[2][0]+pts[3][0])/2, (pts[2][1]+pts[3][1])/2))
            sym_lines.append(((pts[1][0]+pts[2][0])/2, (pts[1][1]+pts[2][1])/2, (pts[3][0]+pts[0][0])/2, (pts[3][1]+pts[0][1])/2))

    elif polygon_type == "regular_pentagon":
        for k in range(5):
            angle = -math.pi / 2 + k * 2 * math.pi / 5
            pts.append((cx + r * math.cos(angle), cy + r * math.sin(angle)))
        if show_lines:
            for k in range(5):
                p_opp = pts[k]
                mid_x = (pts[(k+2)%5][0] + pts[(k+3)%5][0]) / 2
                mid_y = (pts[(k+2)%5][1] + pts[(k+3)%5][1]) / 2
                dx = mid_x - p_opp[0]
                dy = mid_y - p_opp[1]
                sym_lines.append((p_opp[0] - 0.15 * dx, p_opp[1] - 0.15 * dy, mid_x + 0.25 * dx, mid_y + 0.25 * dy))

    elif polygon_type == "regular_hexagon":
        for k in range(6):
            angle = k * math.pi / 3
            pts.append((cx + r * math.cos(angle), cy + r * math.sin(angle)))
        if show_lines:
            # 3 vertex diagonals
            for k in range(3):
                sym_lines.append((pts[k][0], pts[k][1], pts[k+3][0], pts[k+3][1]))
            # 3 edge bisectors
            for k in range(3):
                m1x = (pts[k][0] + pts[k+1][0]) / 2
                m1y = (pts[k][1] + pts[k+1][1]) / 2
                m2x = (pts[k+3][0] + pts[(k+4)%6][0]) / 2
                m2y = (pts[k+3][1] + pts[(k+4)%6][1]) / 2
                sym_lines.append((m1x, m1y, m2x, m2y))

    elif polygon_type == "rectangle":
        rw = 160.0
        rh = 90.0
        pts = [(cx - rw, cy - rh), (cx + rw, cy - rh), (cx + rw, cy + rh), (cx - rw, cy + rh)]
        if show_lines:
            # 2 perpendicular bisectors of opposite sides
            sym_lines.append((cx - rw - 20, cy, cx + rw + 20, cy))
            sym_lines.append((cx, cy - rh - 20, cx, cy + rh + 20))

    elif polygon_type == "rhombus":
        rw = 130.0
        rh = 80.0
        pts = [(cx, cy - rh), (cx + rw, cy), (cx, cy + rh), (cx - rw, cy)]
        if show_lines:
            # 2 diagonals
            sym_lines.append((cx, cy - rh - 25, cx, cy + rh + 25))
            sym_lines.append((cx - rw - 25, cy, cx + rw + 25, cy))

    elif polygon_type == "kite":
        pts = [(cx, cy - 130), (cx + 80, cy - 30), (cx, cy + 110), (cx - 80, cy - 30)]
        if show_lines:
            # Main diagonal only
            sym_lines.append((cx, cy - 150, cx, cy + 130))

    else:  # parallelogram
        pts = [(cx - 120, cy + 60), (cx + 60, cy + 60), (cx + 120, cy - 60), (cx - 60, cy - 60)]
        # 0 lines of symmetry

    # Draw shape
    pts_str = " ".join(f"{round(p[0], 1)},{round(p[1], 1)}" for p in pts)
    svg_lines.append(f'  <polygon points="{pts_str}" fill="url(#poly-grad)" stroke="#1e40af" stroke-width="2.5"/>')

    # Draw vertices
    for idx, p in enumerate(pts):
        svg_lines.append(f'  <circle cx="{p[0]}" cy="{p[1]}" r="4" fill="#1e40af"/>')

    # Draw lines of symmetry
    if show_lines:
        for idx, (x1, y1, x2, y2) in enumerate(sym_lines, 1):
            svg_lines.append(f'  <line x1="{round(x1, 1)}" y1="{round(y1, 1)}" x2="{round(x2, 1)}" y2="{round(y2, 1)}" stroke="#ef4444" stroke-width="2" stroke-dasharray="5,4"/>')

    # Label shape name
    name_clean = polygon_type.replace("_", " ").title()
    svg_lines.append(f'  <text x="{cx}" y="{h - 18}" font-size="14" font-weight="bold" text-anchor="middle" fill="#0f172a">{name_clean}</text>')

    svg_lines.append('</svg>')
    return "\n".join(svg_lines)
