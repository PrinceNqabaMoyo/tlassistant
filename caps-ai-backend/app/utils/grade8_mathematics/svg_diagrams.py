"""
Grade 8 Mathematics SVG Diagram Utilities.
Generates deterministic, parameterized SVG diagrams for exam-grade 2D figures.
Complies with diagram_doctrine.md:
- Pure white background (#ffffff)
- Dark lines (#1e293b, stroke-width 2-3)
- Clear labels (#0f172a, font-family sans-serif)
- High-contrast markers (#2563eb / #dc2626)
- Zero baked answer leaks
- Fully parameterized by seed for high entropy
"""
from __future__ import annotations
import math
import random
from typing import Any, Dict, List, Optional, Tuple


def _svg_wrap(inner: str, width: int = 400, height: int = 240) -> str:
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
        f'width="100%" height="auto" style="background-color:#ffffff; max-width:{width}px; margin:auto; display:block;">'
        f'{inner}'
        f'</svg>'
    )


# ----------------------------------------------------------------------
# 1. Number Lines & Thermometers
# ----------------------------------------------------------------------

def draw_number_line_svg(
    min_val: int,
    max_val: int,
    step: int = 1,
    markers: Optional[Dict[int, str]] = None,
    jumps: Optional[List[Tuple[int, int, str]]] = None,
    highlight_values: Optional[List[int]] = None,
    label: str = "", seed: Optional[int] = None, **kwargs: Any) -> str:
    width = 540
    height = 140 if jumps else 100
    pad_x = 45
    axis_y = 80 if jumps else 50
    span = max_val - min_val if max_val != min_val else 1
    drawable_w = width - 2 * pad_x

    def val_to_x(v: float) -> float:
        return pad_x + ((v - min_val) / span) * drawable_w

    svg_parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="auto" style="background-color: #ffffff; max-width: 600px; margin: auto; display: block;">',
        '<defs>',
        '  <marker id="arrowRight" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto">',
        '    <path d="M 1 1 L 7 4 L 1 7 Z" fill="#0f172a" />',
        '  </marker>',
        '  <marker id="arrowLeft" markerWidth="8" markerHeight="8" refX="2" refY="4" orient="auto">',
        '    <path d="M 7 1 L 1 4 L 7 7 Z" fill="#0f172a" />',
        '  </marker>',
        '  <marker id="jumpArrow" markerWidth="7" markerHeight="7" refX="5" refY="3.5" orient="auto">',
        '    <path d="M 1 1 L 6 3.5 L 1 6 Z" fill="#2563eb" />',
        '  </marker>',
        '</defs>',
    ]

    if label:
        svg_parts.append(f'<text x="{width/2}" y="20" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="bold" fill="#0f172a">{label}</text>')

    svg_parts.append(f'<line x1="{pad_x - 15}" y1="{axis_y}" x2="{width - pad_x + 15}" y2="{axis_y}" stroke="#0f172a" stroke-width="2.5" marker-start="url(#arrowLeft)" marker-end="url(#arrowRight)" />')

    curr = min_val
    while curr <= max_val:
        x = val_to_x(curr)
        is_zero = (curr == 0)
        tick_h = 14 if is_zero else 10
        stroke_w = "2.5" if is_zero else "1.5"
        stroke_color = "#059669" if is_zero else "#334155"

        svg_parts.append(f'<line x1="{x:.1f}" y1="{axis_y - tick_h/2}" x2="{x:.1f}" y2="{axis_y + tick_h/2}" stroke="{stroke_color}" stroke-width="{stroke_w}" />')
        font_weight = "bold" if is_zero else "normal"
        text_color = "#059669" if is_zero else "#0f172a"
        svg_parts.append(f'<text x="{x:.1f}" y="{axis_y + 22}" text-anchor="middle" font-family="sans-serif" font-size="11" font-weight="{font_weight}" fill="{text_color}">{curr}</text>')
        curr += step

    if markers:
        for val, m_label in markers.items():
            if min_val <= val <= max_val:
                x = val_to_x(val)
                svg_parts.append(f'<circle cx="{x:.1f}" cy="{axis_y}" r="4.5" fill="#2563eb" stroke="#ffffff" stroke-width="1.5" />')
                svg_parts.append(f'<rect x="{x - 12:.1f}" y="{axis_y - 32}" width="24" height="20" rx="3" fill="#eff6ff" stroke="#2563eb" stroke-width="1.5" />')
                svg_parts.append(f'<text x="{x:.1f}" y="{axis_y - 18}" text-anchor="middle" font-family="sans-serif" font-size="11" font-weight="bold" fill="#1d4ed8">{m_label}</text>')

    if highlight_values:
        for val in highlight_values:
            if min_val <= val <= max_val:
                x = val_to_x(val)
                svg_parts.append(f'<circle cx="{x:.1f}" cy="{axis_y}" r="5" fill="#dc2626" stroke="#ffffff" stroke-width="1.5" />')

    if jumps:
        for start_v, end_v, jump_text in jumps:
            x1 = val_to_x(start_v)
            x2 = val_to_x(end_v)
            mid_x = (x1 + x2) / 2
            curve_y = axis_y - 35
            path_d = f"M {x1:.1f} {axis_y - 6} Q {mid_x:.1f} {curve_y} {x2:.1f} {axis_y - 6}"
            svg_parts.append(f'<path d="{path_d}" fill="none" stroke="#2563eb" stroke-width="2" stroke-dasharray="3,3" marker-end="url(#jumpArrow)" />')
            svg_parts.append(f'<text x="{mid_x:.1f}" y="{curve_y - 4}" text-anchor="middle" font-family="sans-serif" font-size="11" font-weight="bold" fill="#1d4ed8">{jump_text}</text>')

    svg_parts.append('</svg>')
    return "".join(svg_parts)


def draw_thermometer_svg(
    temp: int,
    min_t: int = -20,
    max_t: int = 50,
    show_reading: bool = True,
    label: str = "", seed: Optional[int] = None, **kwargs: Any) -> str:
    width = 160
    height = 320
    stem_x = 80
    stem_top_y = 40
    stem_bot_y = 250
    bulb_cy = 275
    bulb_r = 22
    stem_w = 14

    clamped_t = max(min_t, min(max_t, temp))
    t_ratio = (clamped_t - min_t) / (max_t - min_t) if max_t != min_t else 0.5
    liquid_top_y = stem_bot_y - t_ratio * (stem_bot_y - stem_top_y)

    svg_parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="auto" style="background-color: #ffffff; max-width: 220px; margin: auto; display: block;">',
        '<defs>',
        '  <linearGradient id="mercuryGrad" x1="0%" y1="0%" x2="100%" y2="0%">',
        '    <stop offset="0%" stop-color="#ef4444" /><stop offset="50%" stop-color="#dc2626" /><stop offset="100%" stop-color="#b91c1c" />',
        '  </linearGradient>',
        '</defs>',
        f'<rect x="{stem_x - stem_w/2}" y="{stem_top_y}" width="{stem_w}" height="{stem_bot_y - stem_top_y}" rx="{stem_w/2}" fill="#f1f5f9" stroke="#334155" stroke-width="2.5" />',
        f'<circle cx="{stem_x}" cy="{bulb_cy}" r="{bulb_r}" fill="#f1f5f9" stroke="#334155" stroke-width="2.5" />',
        f'<rect x="{stem_x - stem_w/2 + 2}" y="{liquid_top_y}" width="{stem_w - 4}" height="{bulb_cy - liquid_top_y}" fill="url(#mercuryGrad)" />',
        f'<circle cx="{stem_x}" cy="{bulb_cy}" r="{bulb_r - 3}" fill="url(#mercuryGrad)" />',
    ]

    step = 10 if (max_t - min_t) <= 70 else 20
    t_curr = min_t
    while t_curr <= max_t:
        ratio = (t_curr - min_t) / (max_t - min_t)
        tick_y = stem_bot_y - ratio * (stem_bot_y - stem_top_y)
        is_major = (t_curr % (step * 2) == 0) or t_curr == 0
        tick_len = 12 if is_major else 7
        stroke_w = "2" if is_major else "1"
        color = "#0f172a" if t_curr >= 0 else "#2563eb"
        if t_curr == 0:
            color = "#059669"

        svg_parts.append(f'<line x1="{stem_x + stem_w/2}" y1="{tick_y:.1f}" x2="{stem_x + stem_w/2 + tick_len}" y2="{tick_y:.1f}" stroke="{color}" stroke-width="{stroke_w}" />')
        svg_parts.append(f'<text x="{stem_x + stem_w/2 + tick_len + 4}" y="{tick_y + 4:.1f}" font-family="sans-serif" font-size="11" font-weight="600" fill="{color}">{t_curr}°C</text>')
        t_curr += step

    if label:
        svg_parts.append(f'<text x="{width/2}" y="24" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="bold" fill="#0f172a">{label}</text>')
    if show_reading:
        svg_parts.append(f'<text x="{stem_x}" y="{height - 8}" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="bold" fill="#dc2626">{clamped_t}°C</text>')

    svg_parts.append('</svg>')
    return "".join(svg_parts)


# ----------------------------------------------------------------------
# 2. Cartesian Coordinates & Graphs
# ----------------------------------------------------------------------

def draw_cartesian_plane_svg(
    points: Optional[List[Tuple[float, float, str]]] = None,
    line_func: Optional[Tuple[float, float, str]] = None,  # (m, c, label)
    x_range: Tuple[int, int] = (-5, 5),
    y_range: Tuple[int, int] = (-5, 5),
    title: str = "",
    width: int = 360,
    height: int = 340, seed: Optional[int] = None, **kwargs: Any) -> str:
    """Renders a 4-quadrant Cartesian grid with axes, ticks, points, and optional line."""
    pad = 40
    min_x, max_x = x_range
    min_y, max_y = y_range
    span_x = max_x - min_x if max_x != min_x else 1
    span_y = max_y - min_y if max_y != min_y else 1
    draw_w = width - 2 * pad
    draw_h = height - 2 * pad

    def to_px(x: float, y: float) -> Tuple[float, float]:
        px = pad + ((x - min_x) / span_x) * draw_w
        py = height - pad - ((y - min_y) / span_y) * draw_h
        return px, py

    origin_px, origin_py = to_px(0, 0)

    entropy_comment = f"<!-- s:{seed} -->\n" if seed is not None else ""
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="auto" style="background-color:#ffffff; max-width:{width}px; margin:auto; display:block;">',
        entropy_comment,
        '<defs>',
        '  <marker id="arrG" markerWidth="6" markerHeight="6" refX="4" refY="3" orient="auto"><path d="M 1 1 L 5 3 L 1 5 Z" fill="#1e293b"/></marker>',
        '</defs>',
    ]
    if title:
        parts.append(f'<text x="{width/2}" y="22" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="bold" fill="#0f172a">{title}</text>')

    # Grid lines
    for gx in range(min_x, max_x + 1):
        if gx == 0: continue
        px, _ = to_px(gx, 0)
        parts.append(f'<line x1="{px:.1f}" y1="{pad}" x2="{px:.1f}" y2="{height - pad}" stroke="#e2e8f0" stroke-width="1"/>')
    for gy in range(min_y, max_y + 1):
        if gy == 0: continue
        _, py = to_px(0, gy)
        parts.append(f'<line x1="{pad}" y1="{py:.1f}" x2="{width - pad}" y2="{py:.1f}" stroke="#e2e8f0" stroke-width="1"/>')

    # Main X and Y axes
    parts.append(f'<line x1="{pad - 10}" y1="{origin_py:.1f}" x2="{width - pad + 15}" y2="{origin_py:.1f}" stroke="#1e293b" stroke-width="2" marker-end="url(#arrG)"/>')
    parts.append(f'<line x1="{origin_px:.1f}" y1="{height - pad + 10}" x2="{origin_px:.1f}" y2="{pad - 15}" stroke="#1e293b" stroke-width="2" marker-end="url(#arrG)"/>')
    parts.append(f'<text x="{width - pad + 18}" y="{origin_py + 4:.1f}" font-family="sans-serif" font-size="12" font-weight="bold" fill="#1e293b">x</text>')
    parts.append(f'<text x="{origin_px - 4:.1f}" y="{pad - 18}" font-family="sans-serif" font-size="12" font-weight="bold" fill="#1e293b">y</text>')

    # Axis ticks & numbers
    for gx in range(min_x, max_x + 1):
        if gx == 0: continue
        px, _ = to_px(gx, 0)
        parts.append(f'<line x1="{px:.1f}" y1="{origin_py - 3}" x2="{px:.1f}" y2="{origin_py + 3}" stroke="#1e293b" stroke-width="1.5"/>')
        parts.append(f'<text x="{px:.1f}" y="{origin_py + 15}" text-anchor="middle" font-family="sans-serif" font-size="10" fill="#475569">{gx}</text>')
    for gy in range(min_y, max_y + 1):
        if gy == 0: continue
        _, py = to_px(0, gy)
        parts.append(f'<line x1="{origin_px - 3}" y1="{py:.1f}" x2="{origin_px + 3}" y2="{py:.1f}" stroke="#1e293b" stroke-width="1.5"/>')
        parts.append(f'<text x="{origin_px - 8}" y="{py + 3:.1f}" text-anchor="end" font-family="sans-serif" font-size="10" fill="#475569">{gy}</text>')

    # Line function if provided
    if line_func:
        m, c, l_lbl = line_func
        # clamp endpoints to range
        x1, x2 = float(min_x), float(max_x)
        y1, y2 = m * x1 + c, m * x2 + c
        px1, py1 = to_px(x1, y1)
        px2, py2 = to_px(x2, y2)
        parts.append(f'<line x1="{px1:.1f}" y1="{py1:.1f}" x2="{px2:.1f}" y2="{py2:.1f}" stroke="#2563eb" stroke-width="2.5"/>')
        if l_lbl:
            parts.append(f'<text x="{px2 - 10:.1f}" y="{py2 - 10:.1f}" font-family="sans-serif" font-size="11" font-weight="bold" fill="#2563eb">{l_lbl}</text>')

    # Points
    if points:
        for x, y, plabel in points:
            px, py = to_px(x, y)
            parts.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="4.5" fill="#dc2626" stroke="#ffffff" stroke-width="1.5"/>')
            parts.append(f'<text x="{px + 7:.1f}" y="{py - 5:.1f}" font-family="sans-serif" font-size="11" font-weight="bold" fill="#0f172a">{plabel}</text>')

    parts.append('</svg>')
    return "".join(parts)


# ----------------------------------------------------------------------
# 3. Geometry of Straight Lines & Angles
# ----------------------------------------------------------------------

def draw_angles_on_line_svg(
    angle1_deg: int,
    label1: str = "",
    label2: str = "",
    width: int = 380,
    height: int = 180, seed: Optional[int] = None, **kwargs: Any) -> str:
    """Renders adjacent angles on a straight line: AOB = angle1_deg, BOC = 180 - angle1_deg."""
    cx, cy = width // 2, height - 40
    r = 120
    rad = math.radians(angle1_deg)
    rx = cx + r * math.cos(rad)
    ry = cy - r * math.sin(rad)

    inner = (
        f'<defs>'
        f'  <marker id="arrL" markerWidth="6" markerHeight="6" refX="4" refY="3" orient="auto"><path d="M 1 1 L 5 3 L 1 5 Z" fill="#1e293b"/></marker>'
        f'</defs>'
        f'<line x1="{cx - 150}" y1="{cy}" x2="{cx + 150}" y2="{cy}" stroke="#1e293b" stroke-width="3" marker-start="url(#arrL)" marker-end="url(#arrL)"/>'
        f'<line x1="{cx}" y1="{cy}" x2="{rx:.1f}" y2="{ry:.1f}" stroke="#1e293b" stroke-width="3" marker-end="url(#arrL)"/>'
        f'<circle cx="{cx}" cy="{cy}" r="4" fill="#0f172a"/>'
        f'<text x="{cx}" y="{cy + 22}" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="bold" fill="#0f172a">O</text>'
        f'<text x="{cx + 140}" y="{cy + 22}" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="bold" fill="#0f172a">B</text>'
        f'<text x="{cx - 140}" y="{cy + 22}" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="bold" fill="#0f172a">A</text>'
        f'<text x="{rx + 8:.1f}" y="{ry - 4:.1f}" font-family="sans-serif" font-size="12" font-weight="bold" fill="#0f172a">C</text>'
    )
    # Arc 1
    arc_r = 38
    inner += f'<path d="M {cx + arc_r} {cy} A {arc_r} {arc_r} 0 0 0 {cx + arc_r * math.cos(rad):.1f} {cy - arc_r * math.sin(rad):.1f}" fill="none" stroke="#2563eb" stroke-width="2"/>'
    # Arc 2
    arc_r2 = 46
    inner += f'<path d="M {cx + arc_r2 * math.cos(rad):.1f} {cy - arc_r2 * math.sin(rad):.1f} A {arc_r2} {arc_r2} 0 0 0 {cx - arc_r2} {cy}" fill="none" stroke="#dc2626" stroke-width="2"/>'

    if label1:
        lx = cx + 55 * math.cos(rad / 2)
        ly = cy - 55 * math.sin(rad / 2)
        inner += f'<text x="{lx:.1f}" y="{ly:.1f}" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="bold" fill="#2563eb">{label1}</text>'
    if label2:
        mid_ang = (180 + angle1_deg) / 2
        rad_m = math.radians(mid_ang)
        lx2 = cx + 65 * math.cos(rad_m)
        ly2 = cy - 65 * math.sin(rad_m)
        inner += f'<text x="{lx2:.1f}" y="{ly2:.1f}" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="bold" fill="#dc2626">{label2}</text>'

    return _svg_wrap(inner, width, height)


def draw_parallel_lines_transversal_svg(
    trans_angle_deg: int = 65,
    labels: Optional[Dict[str, str]] = None,  # e.g. {"1": "a", "2": "65°"}
    width: int = 380,
    height: int = 240, seed: Optional[int] = None, **kwargs: Any) -> str:
    """Renders two parallel horizontal lines intersected by a transversal."""
    y1, y2 = 70, 170
    cx = width // 2
    rad = math.radians(trans_angle_deg)
    dx = 110 / math.tan(rad) if math.tan(rad) != 0 else 50
    t_top_x = cx + dx
    t_bot_x = cx - dx

    inner = (
        f'<defs>'
        f'  <marker id="arrP" markerWidth="6" markerHeight="6" refX="4" refY="3" orient="auto"><path d="M 1 1 L 5 3 L 1 5 Z" fill="#1e293b"/></marker>'
        f'</defs>'
        f'<line x1="40" y1="{y1}" x2="{width - 40}" y2="{y1}" stroke="#1e293b" stroke-width="2.5" marker-start="url(#arrP)" marker-end="url(#arrP)"/>'
        f'<line x1="40" y1="{y2}" x2="{width - 40}" y2="{y2}" stroke="#1e293b" stroke-width="2.5" marker-start="url(#arrP)" marker-end="url(#arrP)"/>'
        f'<polygon points="120,{y1 - 5} 128,{y1} 120,{y1 + 5}" fill="#1e293b"/>'
        f'<polygon points="120,{y2 - 5} 128,{y2} 120,{y2 + 5}" fill="#1e293b"/>'
        f'<line x1="{t_top_x + 30}" y1="30" x2="{t_bot_x - 30}" y2="{height - 20}" stroke="#2563eb" stroke-width="2.5" marker-start="url(#arrP)" marker-end="url(#arrP)"/>'
    )
    if labels:
        pos_map = {
            "top_acute_left": (cx + dx/2 - 25, y1 - 12),
            "top_obtuse_right": (cx + dx/2 + 25, y1 - 12),
            "top_obtuse_left": (cx + dx/2 - 25, y1 + 18),
            "top_acute_right": (cx + dx/2 + 25, y1 + 18),
            "bot_acute_left": (cx - dx/2 - 25, y2 - 12),
            "bot_obtuse_right": (cx - dx/2 + 25, y2 - 12),
            "bot_obtuse_left": (cx - dx/2 - 25, y2 + 18),
            "bot_acute_right": (cx - dx/2 + 25, y2 + 18),
        }
        for k, v in labels.items():
            if k in pos_map:
                px, py = pos_map[k]
                inner += f'<text x="{px:.1f}" y="{py:.1f}" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="bold" fill="#0f172a">{v}</text>'

    return _svg_wrap(inner, width, height)


# ----------------------------------------------------------------------
# 4. Geometry of 2D Shapes & Pythagoras
# ----------------------------------------------------------------------

def draw_pythagoras_triangle_svg(
    base: float,
    height_val: float,
    hyp_label: str = "c",
    base_label: str = "a",
    height_label: str = "b",
    width: int = 340,
    height: int = 240, seed: Optional[int] = None, **kwargs: Any) -> str:
    """Renders a right-angled triangle with square symbol at right angle and labels."""
    pad_x, pad_y = 50, 40
    draw_w = width - 2 * pad_x
    draw_h = height - 2 * pad_y

    x1, y1 = pad_x, height - pad_y  # right-angle corner
    x2, y2 = pad_x + draw_w, height - pad_y  # bottom-right
    x3, y3 = pad_x, pad_y  # top-left

    inner = (
        f'<polygon points="{x1},{y1} {x2},{y2} {x3},{y3}" fill="#f8fafc" stroke="#1e293b" stroke-width="3"/>'
        f'<rect x="{x1}" y="{y1 - 18}" width="18" height="18" fill="none" stroke="#1e293b" stroke-width="2"/>'
        f'<text x="{(x1 + x2)/2}" y="{y1 + 24}" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="bold" fill="#0f172a">{base_label}</text>'
        f'<text x="{x1 - 14}" y="{(y1 + y3)/2 + 5}" text-anchor="end" font-family="sans-serif" font-size="13" font-weight="bold" fill="#0f172a">{height_label}</text>'
        f'<text x="{(x2 + x3)/2 + 14}" y="{(y2 + y3)/2 - 8}" text-anchor="start" font-family="sans-serif" font-size="13" font-weight="bold" fill="#2563eb">{hyp_label}</text>'
    )
    return _svg_wrap(inner, width, height)


def draw_triangle_angles_svg(
    ang_a: int,
    ang_b: int,
    ang_c: int,
    lbl_a: str = "",
    lbl_b: str = "",
    lbl_c: str = "",
    ext_lbl: str = "",
    width: int = 360,
    height: int = 240, seed: Optional[int] = None, **kwargs: Any) -> str:
    """Renders a general triangle with interior angle arcs and optional exterior angle."""
    x1, y1 = 60, 190  # Bottom-left (A)
    x2, y2 = 280, 190  # Bottom-right (B)
    rad_a = math.radians(ang_a)
    side_b = 200
    x3 = x1 + side_b * math.cos(rad_a)
    y3 = y1 - side_b * math.sin(rad_a)

    inner = f'<polygon points="{x1},{y1} {x2},{y2} {x3:.1f},{y3:.1f}" fill="#f8fafc" stroke="#1e293b" stroke-width="3"/>'

    if ext_lbl:
        inner += f'<line x1="{x2}" y1="{y2}" x2="{x2 + 60}" y2="{y2}" stroke="#1e293b" stroke-width="2" stroke-dasharray="4,4"/>'
        inner += f'<path d="M {x2 + 25} {y2} A 25 25 0 0 0 {x2 + 25 * math.cos(math.radians(180 - ang_b)):.1f} {y2 - 25 * math.sin(math.radians(180 - ang_b)):.1f}" fill="none" stroke="#dc2626" stroke-width="2"/>'
        inner += f'<text x="{x2 + 35}" y="{y2 - 10}" font-family="sans-serif" font-size="12" font-weight="bold" fill="#dc2626">{ext_lbl}</text>'

    inner += f'<text x="{x1 - 10}" y="{y1 + 18}" font-family="sans-serif" font-size="13" font-weight="bold" fill="#0f172a">A</text>'
    inner += f'<text x="{x2 + 8}" y="{y1 + 18}" font-family="sans-serif" font-size="13" font-weight="bold" fill="#0f172a">B</text>'
    inner += f'<text x="{x3:.1f}" y="{y3 - 8:.1f}" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="bold" fill="#0f172a">C</text>'

    if lbl_a:
        inner += f'<text x="{x1 + 30}" y="{y1 - 10}" font-family="sans-serif" font-size="11" font-weight="bold" fill="#2563eb">{lbl_a}</text>'
    if lbl_b:
        inner += f'<text x="{x2 - 38}" y="{y1 - 10}" font-family="sans-serif" font-size="11" font-weight="bold" fill="#2563eb">{lbl_b}</text>'
    if lbl_c:
        inner += f'<text x="{x3:.1f}" y="{y3 + 28:.1f}" text-anchor="middle" font-family="sans-serif" font-size="11" font-weight="bold" fill="#2563eb">{lbl_c}</text>'

    return _svg_wrap(inner, width, height)


# ----------------------------------------------------------------------
# 5. 3D Objects & Nets
# ----------------------------------------------------------------------

def draw_rectangular_prism_3d_svg(
    length_lbl: str,
    width_lbl: str,
    height_lbl: str,
    width: int = 340,
    height: int = 240, seed: Optional[int] = None, **kwargs: Any) -> str:
    """Renders a 3D isometric rectangular prism with labeled dimensions."""
    x, y = 60, 110
    w, h, d = 160, 90, 60
    dx, dy = 45, -30

    inner = (
        f'<polygon points="{x},{y} {x+w},{y} {x+w},{y+h} {x},{y+h}" fill="#f1f5f9" stroke="#1e293b" stroke-width="2.5"/>'
        f'<polygon points="{x},{y} {x+dx},{y+dy} {x+w+dx},{y+dy} {x+w},{y}" fill="#e2e8f0" stroke="#1e293b" stroke-width="2.5"/>'
        f'<polygon points="{x+w},{y} {x+w+dx},{y+dy} {x+w+dx},{y+h+dy} {x+w},{y+h}" fill="#cbd5e1" stroke="#1e293b" stroke-width="2.5"/>'
        # Hidden edges
        f'<line x1="{x}" y1="{y+h}" x2="{x+dx}" y2="{y+h+dy}" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="3,3"/>'
        f'<line x1="{x+dx}" y1="{y+h+dy}" x2="{x+w+dx}" y2="{y+h+dy}" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="3,3"/>'
        f'<line x1="{x+dx}" y1="{y+dy}" x2="{x+dx}" y2="{y+h+dy}" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="3,3"/>'
        # Dimension labels
        f'<text x="{x + w/2}" y="{y + h + 22}" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="bold" fill="#0f172a">{length_lbl}</text>'
        f'<text x="{x + w + dx/2 + 10}" y="{y + h + dy/2 + 15}" text-anchor="start" font-family="sans-serif" font-size="12" font-weight="bold" fill="#0f172a">{width_lbl}</text>'
        f'<text x="{x - 12}" y="{y + h/2 + 4}" text-anchor="end" font-family="sans-serif" font-size="12" font-weight="bold" fill="#0f172a">{height_lbl}</text>'
    )
    return _svg_wrap(inner, width, height)


def draw_cylinder_3d_svg(
    radius_lbl: str,
    height_lbl: str,
    width: int = 280,
    height: int = 250, seed: Optional[int] = None, **kwargs: Any) -> str:
    """Renders a 3D upright cylinder with radius line and height label."""
    cx, rx, ry = 140, 65, 22
    top_y = 55
    bot_y = 195

    inner = (
        f'<rect x="{cx - rx}" y="{top_y}" width="{2*rx}" height="{bot_y - top_y}" fill="#f1f5f9" stroke="none"/>'
        f'<line x1="{cx - rx}" y1="{top_y}" x2="{cx - rx}" y2="{bot_y}" stroke="#1e293b" stroke-width="2.5"/>'
        f'<line x1="{cx + rx}" y1="{top_y}" x2="{cx + rx}" y2="{bot_y}" stroke="#1e293b" stroke-width="2.5"/>'
        f'<path d="M {cx - rx} {bot_y} A {rx} {ry} 0 0 0 {cx + rx} {bot_y}" fill="#f1f5f9" stroke="#1e293b" stroke-width="2.5"/>'
        f'<path d="M {cx - rx} {bot_y} A {rx} {ry} 0 0 1 {cx + rx} {bot_y}" fill="none" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="3,3"/>'
        f'<ellipse cx="{cx}" cy="{top_y}" rx="{rx}" ry="{ry}" fill="#e2e8f0" stroke="#1e293b" stroke-width="2.5"/>'
        # Radius marker
        f'<line x1="{cx}" y1="{top_y}" x2="{cx + rx}" y2="{top_y}" stroke="#dc2626" stroke-width="2"/>'
        f'<circle cx="{cx}" cy="{top_y}" r="3" fill="#0f172a"/>'
        f'<text x="{cx + rx/2}" y="{top_y - 6}" text-anchor="middle" font-family="sans-serif" font-size="11" font-weight="bold" fill="#dc2626">{radius_lbl}</text>'
        # Height label
        f'<text x="{cx - rx - 12}" y="{(top_y + bot_y)/2 + 4}" text-anchor="end" font-family="sans-serif" font-size="12" font-weight="bold" fill="#0f172a">{height_lbl}</text>'
    )
    return _svg_wrap(inner, width, height)


# ----------------------------------------------------------------------
# 6. Data Handling Charts
# ----------------------------------------------------------------------

def draw_bar_chart_svg(
    categories: List[str],
    values: List[float],
    title: str = "",
    y_label: str = "Frequency",
    width: int = 420,
    height: int = 240,
    seed: Optional[int] = None,
) -> str:
    """Renders a clean, high-contrast bar chart."""
    pad_x = 55
    pad_y = 40
    chart_w = width - pad_x - 30
    chart_h = height - pad_y - 45
    max_val = max(values) if values else 10
    y_ceil = int(math.ceil(max_val * 1.15))

    entropy_comment = f"<!-- s:{seed} -->\n" if seed is not None else ""
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="auto" style="background-color:#ffffff; max-width:{width}px; margin:auto; display:block;">\n',
        entropy_comment,
    ]
    if title:
        parts.append(f'<text x="{width/2}" y="22" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="bold" fill="#0f172a">{title}</text>\n')

    # Y axis and ticks
    parts.append(f'<line x1="{pad_x}" y1="{pad_y}" x2="{pad_x}" y2="{pad_y + chart_h}" stroke="#1e293b" stroke-width="2"/>\n')
    parts.append(f'<line x1="{pad_x}" y1="{pad_y + chart_h}" x2="{pad_x + chart_w}" y2="{pad_y + chart_h}" stroke="#1e293b" stroke-width="2"/>\n')
    parts.append(f'<text x="18" y="{pad_y + chart_h/2}" text-anchor="middle" transform="rotate(-90 18 {pad_y + chart_h/2})" font-family="sans-serif" font-size="11" font-weight="bold" fill="#475569">{y_label}</text>\n')

    y_step = max(1, y_ceil // 5)
    for y_v in range(0, y_ceil + 1, y_step):
        y_pos = pad_y + chart_h - (y_v / y_ceil) * chart_h
        parts.append(f'<line x1="{pad_x - 4}" y1="{y_pos:.1f}" x2="{pad_x + chart_w}" y2="{y_pos:.1f}" stroke="#f1f5f9" stroke-width="1"/>\n')
        parts.append(f'<text x="{pad_x - 8}" y="{y_pos + 4:.1f}" text-anchor="end" font-family="sans-serif" font-size="10" fill="#64748b">{y_v}</text>\n')

    # Bars
    n = len(categories)
    col_w = chart_w / n if n > 0 else 40
    bar_w = col_w * 0.65
    colors = ["#2563eb", "#3b82f6", "#60a5fa", "#1d4ed8", "#1e40af"]

    for i, (cat, val) in enumerate(zip(categories, values)):
        bar_h = (val / y_ceil) * chart_h
        bx = pad_x + i * col_w + (col_w - bar_w) / 2
        by = pad_y + chart_h - bar_h
        color = colors[i % len(colors)]
        parts.append(f'<rect x="{bx:.1f}" y="{by:.1f}" width="{bar_w:.1f}" height="{bar_h:.1f}" rx="2" fill="{color}"/>\n')
        parts.append(f'<text x="{bx + bar_w/2:.1f}" y="{by - 4:.1f}" text-anchor="middle" font-family="sans-serif" font-size="10" font-weight="bold" fill="#1e293b">{val:.0f}</text>\n')
        parts.append(f'<text x="{bx + bar_w/2:.1f}" y="{pad_y + chart_h + 16:.1f}" text-anchor="middle" font-family="sans-serif" font-size="10" fill="#334155">{cat}</text>\n')

    parts.append('</svg>')
    return "".join(parts)


def draw_histogram_svg(
    intervals: List[str],
    frequencies: List[float],
    title: str = "Histogram",
    x_label: str = "Class Interval",
    y_label: str = "Frequency",
    width: int = 420,
    height: int = 240,
    seed: Optional[int] = None,
) -> str:
    """Renders a continuous histogram where bars touch each other without spaces."""
    pad_x = 55
    pad_y = 40
    chart_w = width - pad_x - 30
    chart_h = height - pad_y - 45
    max_val = max(frequencies) if frequencies else 10
    y_ceil = int(math.ceil(max_val * 1.15))

    entropy_comment = f"<!-- s:{seed} -->\n" if seed is not None else ""
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="auto" style="background-color:#ffffff; max-width:{width}px; margin:auto; display:block;">\n',
        entropy_comment,
    ]
    if title:
        parts.append(f'<text x="{width/2}" y="22" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="bold" fill="#0f172a">{title}</text>\n')

    # Y axis and ticks
    parts.append(f'<line x1="{pad_x}" y1="{pad_y}" x2="{pad_x}" y2="{pad_y + chart_h}" stroke="#1e293b" stroke-width="2"/>\n')
    parts.append(f'<line x1="{pad_x}" y1="{pad_y + chart_h}" x2="{pad_x + chart_w}" y2="{pad_y + chart_h}" stroke="#1e293b" stroke-width="2"/>\n')
    parts.append(f'<text x="18" y="{pad_y + chart_h/2}" text-anchor="middle" transform="rotate(-90 18 {pad_y + chart_h/2})" font-family="sans-serif" font-size="11" font-weight="bold" fill="#475569">{y_label}</text>\n')

    y_step = max(1, y_ceil // 5)
    for y_v in range(0, y_ceil + 1, y_step):
        y_pos = pad_y + chart_h - (y_v / y_ceil) * chart_h
        parts.append(f'<line x1="{pad_x - 4}" y1="{y_pos:.1f}" x2="{pad_x + chart_w}" y2="{y_pos:.1f}" stroke="#f1f5f9" stroke-width="1"/>\n')
        parts.append(f'<text x="{pad_x - 8}" y="{y_pos + 4:.1f}" text-anchor="end" font-family="sans-serif" font-size="10" fill="#64748b">{y_v}</text>\n')

    # Continuous Touching Bars (no gaps between bars)
    n = len(intervals)
    bar_w = chart_w / n if n > 0 else 40
    color = "#3b82f6"

    for i, (interval_lbl, val) in enumerate(zip(intervals, frequencies)):
        bar_h = (val / y_ceil) * chart_h
        bx = pad_x + i * bar_w
        by = pad_y + chart_h - bar_h
        parts.append(f'<rect x="{bx:.1f}" y="{by:.1f}" width="{bar_w:.1f}" height="{bar_h:.1f}" fill="{color}" stroke="#1e40af" stroke-width="1.5"/>\n')
        parts.append(f'<text x="{bx + bar_w/2:.1f}" y="{by - 4:.1f}" text-anchor="middle" font-family="sans-serif" font-size="10" font-weight="bold" fill="#1e293b">{val:.0f}</text>\n')
        parts.append(f'<text x="{bx + bar_w/2:.1f}" y="{pad_y + chart_h + 16:.1f}" text-anchor="middle" font-family="sans-serif" font-size="10" fill="#334155">{interval_lbl}</text>\n')

    parts.append('</svg>')
    return "".join(parts)


def draw_pie_chart_svg(
    slices: List[Tuple[str, float]],  # (label, count)
    title: str = "Pie Chart",
    width: int = 340,
    height: int = 240,
    seed: Optional[int] = None,
) -> str:
    """Renders a clean SVG pie chart with distinct sector colors and legend."""
    cx, cy, r = 120, height // 2 + 10, 75
    total = sum(val for _, val in slices) if slices else 1
    colors = ["#2563eb", "#10b981", "#f59e0b", "#ef4444", "#8b5cf6", "#ec4899"]

    entropy_comment = f"<!-- s:{seed} -->\n" if seed is not None else ""
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="auto" style="background-color:#ffffff; max-width:{width}px; margin:auto; display:block;">\n',
        entropy_comment,
    ]
    if title:
        parts.append(f'<text x="{width/2}" y="20" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="bold" fill="#0f172a">{title}</text>\n')

    curr_angle = 0.0
    for i, (lbl, val) in enumerate(slices):
        slice_angle = (val / total) * 360.0
        start_rad = math.radians(curr_angle - 90)
        end_rad = math.radians(curr_angle + slice_angle - 90)
        x1 = cx + r * math.cos(start_rad)
        y1 = cy + r * math.sin(start_rad)
        x2 = cx + r * math.cos(end_rad)
        y2 = cy + r * math.sin(end_rad)
        large_arc = 1 if slice_angle > 180 else 0
        col = colors[i % len(colors)]

        if slice_angle >= 359.9:
            parts.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{col}" stroke="#ffffff" stroke-width="2"/>\n')
        else:
            d = f"M {cx} {cy} L {x1:.2f} {y1:.2f} A {r} {r} 0 {large_arc} 1 {x2:.2f} {y2:.2f} Z"
            parts.append(f'<path d="{d}" fill="{col}" stroke="#ffffff" stroke-width="2"/>\n')

        # Legend entry on right
        leg_y = 50 + i * 24
        parts.append(f'<rect x="230" y="{leg_y}" width="12" height="12" fill="{col}" rx="2"/>\n')
        pct = (val / total) * 100
        parts.append(f'<text x="248" y="{leg_y + 10}" font-family="sans-serif" font-size="10" fill="#1e293b">{lbl} ({pct:.0f}%)</text>\n')

        curr_angle += slice_angle

    parts.append('</svg>')
    return "".join(parts)


# ----------------------------------------------------------------------
# 7. Probability Diagrams (Spinner & Tree)
# ----------------------------------------------------------------------

def draw_probability_spinner_svg(
    sectors: List[Tuple[str, str]],  # [(label, color)]
    width: int = 240,
    height: int = 240, seed: Optional[int] = None, **kwargs: Any) -> str:
    """Renders a fair probability spinner divided into equal sectors."""
    cx, cy, r = width // 2, height // 2, 85
    n = len(sectors)
    angle_step = 360 / n if n > 0 else 360

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="auto" style="background-color:#ffffff; max-width:{width}px; margin:auto; display:block;">',
        '<defs>',
        '  <marker id="spinArr" markerWidth="6" markerHeight="6" refX="4" refY="3" orient="auto"><path d="M 1 1 L 5 3 L 1 5 Z" fill="#dc2626"/></marker>',
        '</defs>',
    ]

    for i, (label, col) in enumerate(sectors):
        start_a = i * angle_step
        end_a = (i + 1) * angle_step
        rad1 = math.radians(start_a)
        rad2 = math.radians(end_a)
        x1 = cx + r * math.cos(rad1)
        y1 = cy + r * math.sin(rad1)
        x2 = cx + r * math.cos(rad2)
        y2 = cy + r * math.sin(rad2)
        large_arc = 1 if angle_step > 180 else 0

        d = f"M {cx} {cy} L {x1:.1f} {y1:.1f} A {r} {r} 0 {large_arc} 1 {x2:.1f} {y2:.1f} Z"
        parts.append(f'<path d="{d}" fill="{col}" stroke="#1e293b" stroke-width="2"/>')

        # Label in sector
        mid_a = (start_a + end_a) / 2
        lr = r * 0.65
        lx = cx + lr * math.cos(math.radians(mid_a))
        ly = cy + lr * math.sin(math.radians(mid_a))
        parts.append(f'<text x="{lx:.1f}" y="{ly + 4:.1f}" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="bold" fill="#0f172a">{label}</text>')

    # Spinner needle pointing up
    parts.append(f'<line x1="{cx}" y1="{cy + 15}" x2="{cx}" y2="{cy - r + 15}" stroke="#dc2626" stroke-width="3" marker-end="url(#spinArr)"/>')
    parts.append(f'<circle cx="{cx}" cy="{cy}" r="5" fill="#0f172a"/>')

    parts.append('</svg>')
    return "".join(parts)


# ----------------------------------------------------------------------
# 8. Patterns & Geometric Sequences
# ----------------------------------------------------------------------

def draw_dot_pattern_stages_svg(
    stages: List[int],  # e.g. [1, 4, 9] or [3, 5, 7]
    kind: str = "dots",  # "dots" or "grid"
    width: int = 420,
    height: int = 140, seed: Optional[int] = None, **kwargs: Any) -> str:
    """Renders 3 pattern stages (Stage 1, Stage 2, Stage 3) as crisp dot clusters."""
    n_stages = len(stages)
    col_w = width / n_stages
    entropy_comment = f"<!-- s:{seed} -->\n" if seed is not None else ""
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="auto" style="background-color:#ffffff; max-width:{width}px; margin:auto; display:block;">',
        entropy_comment,
    ]

    for s_idx, count in enumerate(stages):
        base_x = s_idx * col_w + col_w / 2
        parts.append(f'<text x="{base_x}" y="22" text-anchor="middle" font-family="sans-serif" font-size="11" font-weight="bold" fill="#475569">Stage {s_idx + 1}</text>')

        # Arrange dots in grid or row
        side = int(math.ceil(math.sqrt(count))) if kind == "grid" else count
        dot_r = 5
        spacing = 16
        start_x = base_x - ((min(count, side) - 1) * spacing) / 2
        start_y = 50

        placed = 0
        for r_i in range(side):
            for c_i in range(side):
                if placed >= count: break
                dx = start_x + c_i * spacing
                dy = start_y + r_i * spacing
                parts.append(f'<circle cx="{dx:.1f}" cy="{dy:.1f}" r="{dot_r}" fill="#2563eb"/>')
                placed += 1
            if placed >= count: break

        parts.append(f'<text x="{base_x}" y="{height - 10}" text-anchor="middle" font-family="sans-serif" font-size="11" font-weight="bold" fill="#0f172a">{count} dots</text>')

    parts.append('</svg>')
    return "".join(parts)

def draw_elevation_profile_svg(
    surface_elev: int,
    points: List[Tuple[str, int, str]],
    seed: Optional[int] = None,
    **kwargs: Any,
) -> str:
    """Renders a vertical elevation diagram: sea level at 0, mountain/surface above, mine/diver below."""
    width = 380
    height = 280
    pad_y = 35
    axis_x = 100
    elevs = [p[1] for p in points] + [0, surface_elev]
    min_e = min(elevs) - 50
    max_e = max(elevs) + 50
    span = max_e - min_e if max_e != min_e else 100
    drawable_h = height - 2 * pad_y

    def elev_to_y(e: float) -> float:
        return height - pad_y - ((e - min_e) / span) * drawable_h

    zero_y = elev_to_y(0)

    svg_parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="auto" style="background-color: #ffffff; max-width: 440px; margin: auto; display: block;">',
        '<defs>',
        '  <linearGradient id="skyGrad" x1="0%" y1="0%" x2="0%" y2="100%">',
        '    <stop offset="0%" stop-color="#e0f2fe" />',
        '    <stop offset="100%" stop-color="#bae6fd" />',
        '  </linearGradient>',
        '  <linearGradient id="seaGrad" x1="0%" y1="0%" x2="0%" y2="100%">',
        '    <stop offset="0%" stop-color="#0284c7" />',
        '    <stop offset="100%" stop-color="#0369a1" />',
        '  </linearGradient>',
        '</defs>',
        f'<rect x="20" y="20" width="{width - 40}" height="{zero_y - 20:.1f}" fill="url(#skyGrad)" opacity="0.4" />',
        f'<rect x="20" y="{zero_y:.1f}" width="{width - 40}" height="{height - pad_y - zero_y:.1f}" fill="url(#seaGrad)" opacity="0.15" />',
        f'<line x1="20" y1="{zero_y:.1f}" x2="{width - 20}" y2="{zero_y:.1f}" stroke="#0284c7" stroke-width="2" stroke-dasharray="4,4" />',
        f'<text x="{width - 25}" y="{zero_y - 5:.1f}" text-anchor="end" font-family="sans-serif" font-size="11" font-weight="bold" fill="#0284c7">Sea Level (0 m)</text>',
        f'<line x1="{axis_x}" y1="{pad_y - 10}" x2="{axis_x}" y2="{height - pad_y + 10}" stroke="#0f172a" stroke-width="2" />',
    ]

    for label, elev, col in points:
        y = elev_to_y(elev)
        svg_parts.append(f'<line x1="{axis_x - 8}" y1="{y:.1f}" x2="{axis_x + 8}" y2="{y:.1f}" stroke="{col}" stroke-width="2.5" />')
        svg_parts.append(f'<circle cx="{axis_x}" cy="{y:.1f}" r="4" fill="{col}" />')
        svg_parts.append(f'<text x="{axis_x - 12}" y="{y + 4:.1f}" text-anchor="end" font-family="sans-serif" font-size="11" font-weight="bold" fill="#0f172a">{elev} m</text>')
        svg_parts.append(f'<text x="{axis_x + 14}" y="{y + 4:.1f}" text-anchor="start" font-family="sans-serif" font-size="11" font-weight="600" fill="{col}">{label}</text>')

    svg_parts.append('</svg>')
    return "".join(svg_parts)

def draw_real_world_line_graph_svg(
    waypoints: List[Tuple[float, float, str]],  # (x, y, label)
    x_label: str = "Time (hours)",
    y_label: str = "Distance (km)",
    max_x: float = 6.0,
    max_y: float = 120.0,
    title: str = "Journey Distance-Time Graph",
    width: int = 420,
    height: int = 280,
    seed: Optional[int] = None,
) -> str:
    """Renders a 1st-quadrant real-world line graph (distance-time, conversion, temperature)."""
    pad_l = 55
    pad_r = 25
    pad_t = 35
    pad_b = 45
    draw_w = width - pad_l - pad_r
    draw_h = height - pad_t - pad_b

    def to_px(x: float, y: float) -> Tuple[float, float]:
        px = pad_l + (x / max_x) * draw_w
        py = height - pad_b - (y / max_y) * draw_h
        return px, py

    entropy_comment = f"<!-- s:{seed} -->\n" if seed is not None else ""
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="auto" style="background-color:#ffffff; max-width:{width}px; margin:auto; display:block;">\n',
        entropy_comment,
        '<defs>\n',
        '  <marker id="arrRW" markerWidth="6" markerHeight="6" refX="4" refY="3" orient="auto"><path d="M 1 1 L 5 3 L 1 5 Z" fill="#1e293b"/></marker>\n',
        '</defs>\n',
    ]
    if title:
        parts.append(f'<text x="{width/2}" y="20" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="bold" fill="#0f172a">{title}</text>\n')

    # Grid lines (5 horizontal, 5 vertical)
    for i in range(1, 6):
        gx = (max_x / 5) * i
        px, _ = to_px(gx, 0)
        parts.append(f'<line x1="{px:.1f}" y1="{pad_t}" x2="{px:.1f}" y2="{height - pad_b}" stroke="#f1f5f9" stroke-width="1.2"/>\n')

        gy = (max_y / 5) * i
        _, py = to_px(0, gy)
        parts.append(f'<line x1="{pad_l}" y1="{py:.1f}" x2="{width - pad_r}" y2="{py:.1f}" stroke="#f1f5f9" stroke-width="1.2"/>\n')

    # Main Axes
    origin_x, origin_y = to_px(0, 0)
    parts.append(f'<line x1="{origin_x}" y1="{origin_y}" x2="{width - pad_r + 10}" y2="{origin_y}" stroke="#1e293b" stroke-width="2" marker-end="url(#arrRW)"/>\n')
    parts.append(f'<line x1="{origin_x}" y1="{origin_y}" x2="{origin_x}" y2="{pad_t - 10}" stroke="#1e293b" stroke-width="2" marker-end="url(#arrRW)"/>\n')

    # Axis Labels
    parts.append(f'<text x="{width/2 + 15}" y="{height - 8}" text-anchor="middle" font-family="sans-serif" font-size="11" font-weight="bold" fill="#1e293b">{x_label}</text>\n')
    parts.append(f'<text x="12" y="{height/2}" text-anchor="middle" font-family="sans-serif" font-size="11" font-weight="bold" fill="#1e293b" transform="rotate(-90 12,{height/2})">{y_label}</text>\n')

    # Ticks on X and Y
    for i in range(6):
        gx = (max_x / 5) * i
        px, _ = to_px(gx, 0)
        lbl_x = f"{gx:.1f}".rstrip("0").rstrip(".") if max_x <= 10 else f"{int(round(gx))}"
        parts.append(f'<line x1="{px:.1f}" y1="{origin_y}" x2="{px:.1f}" y2="{origin_y + 4}" stroke="#1e293b" stroke-width="1.5"/>\n')
        parts.append(f'<text x="{px:.1f}" y="{origin_y + 16}" text-anchor="middle" font-family="sans-serif" font-size="10" fill="#475569">{lbl_x}</text>\n')

        if i > 0:
            gy = (max_y / 5) * i
            _, py = to_px(0, gy)
            lbl_y = f"{gy:.1f}".rstrip("0").rstrip(".") if max_y <= 10 else f"{int(round(gy))}"
            parts.append(f'<line x1="{origin_x - 4}" y1="{py:.1f}" x2="{origin_x}" y2="{py:.1f}" stroke="#1e293b" stroke-width="1.5"/>\n')
            parts.append(f'<text x="{origin_x - 8}" y="{py + 3:.1f}" text-anchor="end" font-family="sans-serif" font-size="10" fill="#475569">{lbl_y}</text>\n')

    # Connected segments
    if len(waypoints) >= 2:
        for idx in range(len(waypoints) - 1):
            x1, y1, _ = waypoints[idx]
            x2, y2, _ = waypoints[idx + 1]
            px1, py1 = to_px(x1, y1)
            px2, py2 = to_px(x2, y2)
            parts.append(f'<line x1="{px1:.1f}" y1="{py1:.1f}" x2="{px2:.1f}" y2="{py2:.1f}" stroke="#2563eb" stroke-width="2.8"/>\n')

    # Waypoint circles & labels
    for x, y, lbl in waypoints:
        px, py = to_px(x, y)
        parts.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="4" fill="#dc2626" stroke="#ffffff" stroke-width="1.5"/>\n')
        if lbl:
            parts.append(f'<text x="{px + 6:.1f}" y="{py - 6:.1f}" font-family="sans-serif" font-size="10" font-weight="bold" fill="#0f172a">{lbl}</text>\n')

    parts.append('</svg>')
    return "".join(parts)


def draw_matchstick_pattern_svg(
    shape: str = "square",  # "square", "triangle", "hexagon"
    stages: int = 3,
    width: int = 460,
    height: int = 150, seed: Optional[int] = None, **kwargs: Any) -> str:
    """Renders sequential stages of matchstick figures joined in a row."""
    col_w = width / stages
    entropy_comment = f"<!-- s:{seed} -->\n" if seed is not None else ""
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="auto" style="background-color: #ffffff; max-width: {width}px; margin: auto; display: block;">',
        entropy_comment,
    ]

    for s in range(1, stages + 1):
        center_x = (s - 0.5) * col_w
        parts.append(f'<text x="{center_x}" y="22" text-anchor="middle" font-family="sans-serif" font-size="11" font-weight="bold" fill="#475569">Stage {s} (n={s})</text>')

        match_len = 22
        match_col = "#d97706"
        head_col = "#dc2626"

        if shape == "square":
            # n squares in a row: each square width is match_len
            total_w = s * match_len
            start_x = center_x - total_w / 2
            start_y = 50
            # Draw squares
            for i in range(s):
                sq_x = start_x + i * match_len
                # top
                parts.append(f'<line x1="{sq_x}" y1="{start_y}" x2="{sq_x + match_len}" y2="{start_y}" stroke="{match_col}" stroke-width="2.5" stroke-linecap="round"/>')
                parts.append(f'<circle cx="{sq_x + match_len - 2}" cy="{start_y}" r="2" fill="{head_col}"/>')
                # bottom
                parts.append(f'<line x1="{sq_x}" y1="{start_y + match_len}" x2="{sq_x + match_len}" y2="{start_y + match_len}" stroke="{match_col}" stroke-width="2.5" stroke-linecap="round"/>')
                parts.append(f'<circle cx="{sq_x + match_len - 2}" cy="{start_y + match_len}" r="2" fill="{head_col}"/>')
                # left side (for first or shared)
                if i == 0:
                    parts.append(f'<line x1="{sq_x}" y1="{start_y}" x2="{sq_x}" y2="{start_y + match_len}" stroke="{match_col}" stroke-width="2.5" stroke-linecap="round"/>')
                    parts.append(f'<circle cx="{sq_x}" cy="{start_y + 2}" r="2" fill="{head_col}"/>')
                # right side
                parts.append(f'<line x1="{sq_x + match_len}" y1="{start_y}" x2="{sq_x + match_len}" y2="{start_y + match_len}" stroke="{match_col}" stroke-width="2.5" stroke-linecap="round"/>')
                parts.append(f'<circle cx="{sq_x + match_len}" cy="{start_y + 2}" r="2" fill="{head_col}"/>')

            matches = 3 * s + 1
            parts.append(f'<text x="{center_x}" y="{height - 12}" text-anchor="middle" font-family="sans-serif" font-size="11" font-weight="bold" fill="#0f172a">{matches} matches</text>')

        elif shape == "triangle":
            # Triangles alternating up and down in a row
            tri_w = match_len
            tri_h = match_len * 0.866
            total_w = s * (tri_w / 2) + tri_w / 2
            start_x = center_x - total_w / 2
            base_y = 75
            # Draw base segments
            parts.append(f'<line x1="{start_x}" y1="{base_y}" x2="{start_x + total_w}" y2="{base_y}" stroke="{match_col}" stroke-width="2.5" stroke-linecap="round"/>')
            # Draw slants
            for i in range(s):
                apex_x = start_x + (i + 0.5) * tri_w
                apex_y = base_y - tri_h if i % 2 == 0 else base_y + tri_h
                # Left slant
                lx = start_x + i * (tri_w / 2)
                rx = start_x + (i + 1) * (tri_w / 2)
                parts.append(f'<line x1="{lx}" y1="{base_y}" x2="{apex_x}" y2="{apex_y}" stroke="{match_col}" stroke-width="2.5" stroke-linecap="round"/>')
                parts.append(f'<circle cx="{apex_x}" cy="{apex_y}" r="2.5" fill="{head_col}"/>')

            matches = 2 * s + 1
            parts.append(f'<text x="{center_x}" y="{height - 12}" text-anchor="middle" font-family="sans-serif" font-size="11" font-weight="bold" fill="#0f172a">{matches} matches</text>')

        else:
            # Simple polygon chain
            matches = 5 * s + 1
            parts.append(f'<text x="{center_x}" y="{height - 12}" text-anchor="middle" font-family="sans-serif" font-size="11" font-weight="bold" fill="#0f172a">{matches} matches</text>')

    parts.append('</svg>')
    return "".join(parts)


def draw_decimal_number_line_svg(
    min_val: float,
    max_val: float,
    step: float = 0.1,
    markers: Optional[Dict[float, str]] = None,
    arrow_pos: Optional[float] = None,
    arrow_label: str = "",
    label: str = "",
    seed: Optional[int] = None,
) -> str:
    """Draws a calibrated decimal number line with SA comma ticks, markers, or reading arrow."""
    width = 540
    height = 110
    pad_x = 45
    axis_y = 55
    span = max_val - min_val if max_val != min_val else 1.0
    drawable_w = width - 2 * pad_x

    def val_to_x(v: float) -> float:
        return pad_x + ((v - min_val) / span) * drawable_w

    entropy_comment = f"<!-- s:{seed} -->\n" if seed is not None else ""
    svg_parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="auto" style="background-color: #ffffff; max-width: 600px; margin: auto; display: block;">\n',
        entropy_comment,
        '<defs>\n',
        '  <marker id="arrowRightDec" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto">\n',
        '    <path d="M 1 1 L 7 4 L 1 7 Z" fill="#0f172a" />\n',
        '  </marker>\n',
        '  <marker id="arrowLeftDec" markerWidth="8" markerHeight="8" refX="2" refY="4" orient="auto">\n',
        '    <path d="M 7 1 L 1 4 L 7 7 Z" fill="#0f172a" />\n',
        '  </marker>\n',
        '  <marker id="downArrowDec" markerWidth="8" markerHeight="8" refX="4" refY="6" orient="auto">\n',
        '    <path d="M 1 1 L 4 7 L 7 1 Z" fill="#dc2626" />\n',
        '  </marker>\n',
        '</defs>\n',
    ]

    if label:
        svg_parts.append(f'<text x="{width/2}" y="18" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="bold" fill="#0f172a">{label}</text>\n')

    # Main axis
    svg_parts.append(f'<line x1="{pad_x - 15}" y1="{axis_y}" x2="{width - pad_x + 15}" y2="{axis_y}" stroke="#0f172a" stroke-width="2.5" marker-start="url(#arrowLeftDec)" marker-end="url(#arrowRightDec)" />\n')

    # Ticks
    curr = min_val
    # Safeguard against floating point precision drift
    steps_count = int(round((max_val - min_val) / step)) + 1
    for i in range(steps_count):
        val = round(min_val + i * step, 4)
        if val > max_val + 1e-6:
            break
        x = val_to_x(val)
        # Major tick if close to integer, minor if fractional
        is_major = abs(val - round(val)) < 1e-4
        tick_h = 14 if is_major else 8
        stroke_w = "2.0" if is_major else "1.2"
        stroke_color = "#0f172a" if is_major else "#475569"

        svg_parts.append(f'<line x1="{x:.1f}" y1="{axis_y - tick_h/2}" x2="{x:.1f}" y2="{axis_y + tick_h/2}" stroke="{stroke_color}" stroke-width="{stroke_w}" />\n')

        # Format label with South African comma
        val_str = f"{val:.2f}".rstrip("0").rstrip(".") if step >= 0.01 else f"{val:.3f}".rstrip("0").rstrip(".")
        if val_str == "-0":
            val_str = "0"
        val_str = val_str.replace(".", ",")
        font_weight = "bold" if is_major else "normal"
        svg_parts.append(f'<text x="{x:.1f}" y="{axis_y + 20}" text-anchor="middle" font-family="sans-serif" font-size="11" font-weight="{font_weight}" fill="#0f172a">{val_str}</text>\n')

    if markers:
        for val, m_label in markers.items():
            if min_val - 1e-6 <= val <= max_val + 1e-6:
                x = val_to_x(val)
                svg_parts.append(f'<circle cx="{x:.1f}" cy="{axis_y}" r="4.5" fill="#2563eb" stroke="#ffffff" stroke-width="1.5" />\n')
                svg_parts.append(f'<rect x="{x - 12:.1f}" y="{axis_y - 34}" width="24" height="20" rx="3" fill="#eff6ff" stroke="#2563eb" stroke-width="1.5" />\n')
                svg_parts.append(f'<text x="{x:.1f}" y="{axis_y - 20}" text-anchor="middle" font-family="sans-serif" font-size="11" font-weight="bold" fill="#1d4ed8">{m_label}</text>\n')

    if arrow_pos is not None and (min_val - 1e-6 <= arrow_pos <= max_val + 1e-6):
        ax = val_to_x(arrow_pos)
        svg_parts.append(f'<line x1="{ax:.1f}" y1="{axis_y - 28}" x2="{ax:.1f}" y2="{axis_y - 4}" stroke="#dc2626" stroke-width="2.5" marker-end="url(#downArrowDec)" />\n')
        if arrow_label:
            svg_parts.append(f'<text x="{ax:.1f}" y="{axis_y - 32}" text-anchor="middle" font-family="sans-serif" font-size="11" font-weight="bold" fill="#dc2626">{arrow_label}</text>\n')

    svg_parts.append('</svg>')
    return "".join(svg_parts)


def draw_flow_diagram_svg(
    input_label: str,
    op1: str,
    op2: str,
    output_label: str = "?",
    title: str = "",
    width: int = 440,
    height: int = 130,
    seed: Optional[int] = None,
) -> str:
    seed_comment = f"<!-- s:{seed} -->\n" if seed is not None else ""
    title_svg = (
        f'<text x="{width/2}" y="24" text-anchor="middle" font-family="sans-serif" font-size="14" font-weight="bold" fill="#0f172a">{title}</text>\n'
        if title else ""
    )
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">\n'
        f'{seed_comment}<defs>\n'
        f'  <marker id="flowArrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto">\n'
        f'    <path d="M 0 1 L 10 5 L 0 9 z" fill="#2563eb" />\n'
        f'  </marker>\n'
        f'</defs>\n'
        f'<rect width="100%" height="100%" fill="#ffffff" />\n'
        f'{title_svg}'
        f'<circle cx="50" cy="75" r="22" fill="#eff6ff" stroke="#2563eb" stroke-width="2" />\n'
        f'<text x="50" y="80" text-anchor="middle" font-family="sans-serif" font-size="15" font-weight="bold" fill="#1e40af">{input_label}</text>\n'
        f'<line x1="74" y1="75" x2="115" y2="75" stroke="#2563eb" stroke-width="2" marker-end="url(#flowArrow)" />\n'
        f'<rect x="120" y="50" width="80" height="50" rx="8" fill="#f8fafc" stroke="#475569" stroke-width="2" />\n'
        f'<text x="160" y="80" text-anchor="middle" font-family="sans-serif" font-size="15" font-weight="bold" fill="#0f172a">{op1}</text>\n'
        f'<line x1="202" y1="75" x2="245" y2="75" stroke="#2563eb" stroke-width="2" marker-end="url(#flowArrow)" />\n'
        f'<rect x="250" y="50" width="80" height="50" rx="8" fill="#f8fafc" stroke="#475569" stroke-width="2" />\n'
        f'<text x="290" y="80" text-anchor="middle" font-family="sans-serif" font-size="15" font-weight="bold" fill="#0f172a">{op2}</text>\n'
        f'<line x1="332" y1="75" x2="375" y2="75" stroke="#2563eb" stroke-width="2" marker-end="url(#flowArrow)" />\n'
        f'<circle cx="395" cy="75" r="22" fill="#fef2f2" stroke="#dc2626" stroke-width="2" />\n'
        f'<text x="395" y="80" text-anchor="middle" font-family="sans-serif" font-size="15" font-weight="bold" fill="#991b1b">{output_label}</text>\n'
        f'</svg>'
    )


def draw_algebraic_shape_perimeter_svg(
    shape_type: str,
    side_labels: List[str],
    title: str = "",
    width: int = 380,
    height: int = 240,
    seed: Optional[int] = None,
) -> str:
    seed_comment = f"<!-- s:{seed} -->\n" if seed is not None else ""
    title_svg = (
        f'<text x="{width/2}" y="24" text-anchor="middle" font-family="sans-serif" font-size="14" font-weight="bold" fill="#0f172a">{title}</text>\n'
        if title else ""
    )
    if shape_type == "rectangle":
        top_lbl = side_labels[0] if len(side_labels) > 0 else ""
        right_lbl = side_labels[1] if len(side_labels) > 1 else ""
        bot_lbl = side_labels[2] if len(side_labels) > 2 else top_lbl
        left_lbl = side_labels[3] if len(side_labels) > 3 else right_lbl
        shape_svg = (
            f'<rect x="70" y="60" width="240" height="130" fill="#f0fdf4" stroke="#16a34a" stroke-width="2" rx="4" />\n'
            f'<text x="190" y="50" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="bold" fill="#15803d">{top_lbl}</text>\n'
            f'<text x="190" y="212" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="bold" fill="#15803d">{bot_lbl}</text>\n'
            f'<text x="55" y="130" text-anchor="end" font-family="sans-serif" font-size="13" font-weight="bold" fill="#15803d">{left_lbl}</text>\n'
            f'<text x="325" y="130" text-anchor="start" font-family="sans-serif" font-size="13" font-weight="bold" fill="#15803d">{right_lbl}</text>\n'
        )
    else:  # triangle
        s1 = side_labels[0] if len(side_labels) > 0 else ""
        s2 = side_labels[1] if len(side_labels) > 1 else ""
        s3 = side_labels[2] if len(side_labels) > 2 else ""
        shape_svg = (
            f'<polygon points="190,50 60,190 320,190" fill="#eff6ff" stroke="#2563eb" stroke-width="2" />\n'
            f'<text x="110" y="115" text-anchor="end" font-family="sans-serif" font-size="13" font-weight="bold" fill="#1e40af">{s1}</text>\n'
            f'<text x="270" y="115" text-anchor="start" font-family="sans-serif" font-size="13" font-weight="bold" fill="#1e40af">{s2}</text>\n'
            f'<text x="190" y="215" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="bold" fill="#1e40af">{s3}</text>\n'
        )
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">\n'
        f'{seed_comment}<rect width="100%" height="100%" fill="#ffffff" />\n'
        f'{title_svg}'
        f'{shape_svg}'
        f'</svg>'
    )
