"""
Grade 7 Mathematics SVG Diagram Utilities.
Generates deterministic, parameterized SVG diagrams for exam-grade 2D figures.
Complies with diagram_doctrine.md: pure white background (#ffffff), dark lines (#1e293b),
clear labels (#0f172a), high-contrast markers (#2563eb / #dc2626), zero baked answer leaks.
"""
from __future__ import annotations
import math
from typing import Any, Dict, List, Optional, Tuple


def draw_thermometer_svg(
    temp: int,
    min_t: int = -20,
    max_t: int = 50,
    show_reading: bool = True,
    label: str = ""
) -> str:
    """Renders a vertical laboratory thermometer with bulb, calibrated scale, and liquid column."""
    width = 160
    height = 340
    stem_x = 80
    stem_top_y = 40
    stem_bot_y = 260
    bulb_cy = 285
    bulb_r = 24
    stem_w = 14

    clamped_t = max(min_t, min(max_t, temp))
    t_ratio = (clamped_t - min_t) / (max_t - min_t) if max_t != min_t else 0.5
    liquid_top_y = stem_bot_y - t_ratio * (stem_bot_y - stem_top_y)

    svg_parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%" style="background-color: #ffffff; max-width: 240px; margin: auto; display: block;">',
        '<defs>',
        '  <linearGradient id="mercuryGrad" x1="0%" y1="0%" x2="100%" y2="0%">',
        '    <stop offset="0%" stop-color="#ef4444" />',
        '    <stop offset="50%" stop-color="#dc2626" />',
        '    <stop offset="100%" stop-color="#b91c1c" />',
        '  </linearGradient>',
        '</defs>',
        # Thermometer glass outline
        f'<rect x="{stem_x - stem_w/2}" y="{stem_top_y}" width="{stem_w}" height="{stem_bot_y - stem_top_y}" rx="{stem_w/2}" fill="#f1f5f9" stroke="#334155" stroke-width="2.5" />',
        f'<circle cx="{stem_x}" cy="{bulb_cy}" r="{bulb_r}" fill="#f1f5f9" stroke="#334155" stroke-width="2.5" />',
        # Liquid column & bulb
        f'<rect x="{stem_x - stem_w/2 + 2}" y="{liquid_top_y}" width="{stem_w - 4}" height="{bulb_cy - liquid_top_y}" fill="url(#mercuryGrad)" />',
        f'<circle cx="{stem_x}" cy="{bulb_cy}" r="{bulb_r - 3}" fill="url(#mercuryGrad)" />',
    ]

    # Calibration scale ticks
    step = 10 if (max_t - min_t) <= 70 else 20
    t_curr = min_t
    while t_curr <= max_t:
        ratio = (t_curr - min_t) / (max_t - min_t)
        tick_y = stem_bot_y - ratio * (stem_bot_y - stem_top_y)
        is_major = (t_curr % (step * 2) == 0) or t_curr == 0
        tick_len = 14 if is_major else 8
        stroke_w = "2" if is_major else "1"
        color = "#0f172a" if t_curr >= 0 else "#2563eb"
        if t_curr == 0:
            color = "#059669"

        # Right tick and label
        svg_parts.append(f'<line x1="{stem_x + stem_w/2}" y1="{tick_y:.1f}" x2="{stem_x + stem_w/2 + tick_len}" y2="{tick_y:.1f}" stroke="{color}" stroke-width="{stroke_w}" />')
        svg_parts.append(f'<text x="{stem_x + stem_w/2 + tick_len + 4}" y="{tick_y + 4:.1f}" font-family="sans-serif" font-size="11" font-weight="600" fill="{color}">{t_curr}°C</text>')

        # Minor subdivisions (steps of 5 or 2)
        sub_step = step / 2
        sub_t = t_curr + sub_step
        if sub_t < max_t:
            sub_ratio = (sub_t - min_t) / (max_t - min_t)
            sub_y = stem_bot_y - sub_ratio * (stem_bot_y - stem_top_y)
            svg_parts.append(f'<line x1="{stem_x + stem_w/2}" y1="{sub_y:.1f}" x2="{stem_x + stem_w/2 + 6}" y2="{sub_y:.1f}" stroke="#64748b" stroke-width="1" />')

        t_curr += step

    if label:
        svg_parts.append(f'<text x="{width/2}" y="24" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="bold" fill="#0f172a">{label}</text>')
    if show_reading:
        svg_parts.append(f'<text x="{stem_x}" y="{height - 8}" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="bold" fill="#dc2626">{clamped_t}°C</text>')

    svg_parts.append('</svg>')
    return "".join(svg_parts)


def draw_number_line_svg(
    min_val: int,
    max_val: int,
    step: int = 1,
    markers: Optional[Dict[int, str]] = None,
    jumps: Optional[List[Tuple[int, int, str]]] = None,
    highlight_values: Optional[List[int]] = None,
    label: str = ""
) -> str:
    """
    Renders a crisp horizontal integer number line.
    - markers: {value: "A"} or {value: "?"}
    - jumps: [(from_val, to_val, "+4")] curved arrow jump
    - highlight_values: [3, -5] red dots at points
    """
    width = 540
    height = 140 if jumps else 100
    pad_x = 45
    axis_y = 80 if jumps else 50
    span = max_val - min_val if max_val != min_val else 1
    drawable_w = width - 2 * pad_x

    def val_to_x(v: float) -> float:
        return pad_x + ((v - min_val) / span) * drawable_w

    svg_parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%" style="background-color: #ffffff; max-width: 600px; margin: auto; display: block;">',
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

    # Axis line with arrowheads
    svg_parts.append(f'<line x1="{pad_x - 15}" y1="{axis_y}" x2="{width - pad_x + 15}" y2="{axis_y}" stroke="#0f172a" stroke-width="2.5" marker-start="url(#arrowLeft)" marker-end="url(#arrowRight)" />')

    # Tick marks & labels
    curr = min_val
    while curr <= max_val:
        x = val_to_x(curr)
        is_zero = (curr == 0)
        tick_h = 14 if is_zero else 10
        stroke_w = "2.5" if is_zero else "1.5"
        stroke_color = "#059669" if is_zero else "#334155"

        svg_parts.append(f'<line x1="{x:.1f}" y1="{axis_y - tick_h/2}" x2="{x:.1f}" y2="{axis_y + tick_h/2}" stroke="{stroke_color}" stroke-width="{stroke_w}" />')

        # Label under tick
        font_weight = "bold" if is_zero else "normal"
        text_color = "#059669" if is_zero else "#0f172a"
        svg_parts.append(f'<text x="{x:.1f}" y="{axis_y + 22}" text-anchor="middle" font-family="sans-serif" font-size="11" font-weight="{font_weight}" fill="{text_color}">{curr}</text>')

        curr += step

    # Markers (letters or boxes above axis)
    if markers:
        for val, m_label in markers.items():
            if min_val <= val <= max_val:
                x = val_to_x(val)
                svg_parts.append(f'<circle cx="{x:.1f}" cy="{axis_y}" r="4.5" fill="#2563eb" stroke="#ffffff" stroke-width="1.5" />')
                svg_parts.append(f'<rect x="{x - 12:.1f}" y="{axis_y - 32}" width="24" height="20" rx="3" fill="#eff6ff" stroke="#2563eb" stroke-width="1.5" />')
                svg_parts.append(f'<text x="{x:.1f}" y="{axis_y - 18}" text-anchor="middle" font-family="sans-serif" font-size="11" font-weight="bold" fill="#1d4ed8">{m_label}</text>')

    # Highlight points
    if highlight_values:
        for val in highlight_values:
            if min_val <= val <= max_val:
                x = val_to_x(val)
                svg_parts.append(f'<circle cx="{x:.1f}" cy="{axis_y}" r="5" fill="#dc2626" stroke="#ffffff" stroke-width="1.5" />')

    # Curved jump arrows
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


def draw_elevation_profile_svg(
    surface_elev: int,
    points: List[Tuple[str, int, str]]  # [(label, elevation_m, color)]
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
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%" style="background-color: #ffffff; max-width: 440px; margin: auto; display: block;">',
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
        # Sky and ground/water
        f'<rect x="20" y="20" width="{width - 40}" height="{zero_y - 20:.1f}" fill="url(#skyGrad)" opacity="0.4" />',
        f'<rect x="20" y="{zero_y:.1f}" width="{width - 40}" height="{height - pad_y - zero_y:.1f}" fill="url(#seaGrad)" opacity="0.15" />',
        # Sea level baseline
        f'<line x1="20" y1="{zero_y:.1f}" x2="{width - 20}" y2="{zero_y:.1f}" stroke="#0284c7" stroke-width="2" stroke-dasharray="4,4" />',
        f'<text x="{width - 25}" y="{zero_y - 5:.1f}" text-anchor="end" font-family="sans-serif" font-size="11" font-weight="bold" fill="#0284c7">Sea Level (0 m)</text>',
        # Vertical axis line
        f'<line x1="{axis_x}" y1="{pad_y - 10}" x2="{axis_x}" y2="{height - pad_y + 10}" stroke="#0f172a" stroke-width="2" />',
    ]

    # Elevation markers
    for label, elev, col in points:
        y = elev_to_y(elev)
        svg_parts.append(f'<line x1="{axis_x - 8}" y1="{y:.1f}" x2="{axis_x + 8}" y2="{y:.1f}" stroke="{col}" stroke-width="2.5" />')
        svg_parts.append(f'<circle cx="{axis_x}" cy="{y:.1f}" r="4" fill="{col}" />')
        svg_parts.append(f'<text x="{axis_x - 12}" y="{y + 4:.1f}" text-anchor="end" font-family="sans-serif" font-size="11" font-weight="bold" fill="#0f172a">{elev} m</text>')
        svg_parts.append(f'<text x="{axis_x + 14}" y="{y + 4:.1f}" text-anchor="start" font-family="sans-serif" font-size="11" font-weight="600" fill="{col}">{label}</text>')

    svg_parts.append('</svg>')
    return "".join(svg_parts)
