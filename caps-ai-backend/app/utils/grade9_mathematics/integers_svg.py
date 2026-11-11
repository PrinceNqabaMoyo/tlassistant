"""SVG diagram helpers for Grade 9 Integers.
Provides number line with jumps, thermometer readings, and elevation diagrams.
Always emits <!-- s:{seed} --> for guaranteed entropy across seeds.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, Tuple


def draw_integer_number_line_svg(
    min_val: int = -8,
    max_val: int = 8,
    markers: Optional[Dict[int, str]] = None,
    jump: Optional[Tuple[int, int, str]] = None,  # (start, end, label)
    seed: Optional[int] = None,
    **kwargs: Any,
) -> str:
    """Draws an integer number line with markers and optional directional jump."""
    width = 460
    height = 120 if jump else 90
    entropy_comment = f"<!-- s:{seed} -->\n" if seed is not None else ""
    pad_x = 45
    axis_y = 70 if jump else 45
    span = max_val - min_val if max_val != min_val else 1
    drawable_w = width - 2 * pad_x

    def to_px(v: float) -> float:
        return pad_x + ((v - min_val) / span) * drawable_w

    svg_parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="auto" style="background-color:#ffffff; max-width:{width}px; margin:auto; display:block;">\n',
        entropy_comment,
        '<defs>\n',
        '  <marker id="arrR" markerWidth="6" markerHeight="6" refX="4" refY="3" orient="auto"><path d="M 1 1 L 5 3 L 1 5 Z" fill="#1e293b"/></marker>\n',
        '  <marker id="arrL" markerWidth="6" markerHeight="6" refX="2" refY="3" orient="auto"><path d="M 5 1 L 1 3 L 5 5 Z" fill="#1e293b"/></marker>\n',
        '  <marker id="jumpArr" markerWidth="6" markerHeight="6" refX="4" refY="3" orient="auto"><path d="M 1 1 L 5 3 L 1 5 Z" fill="#2563eb"/></marker>\n',
        '</defs>\n',
        f'<line x1="{pad_x - 15}" y1="{axis_y}" x2="{width - pad_x + 15}" y2="{axis_y}" stroke="#1e293b" stroke-width="2.5" marker-start="url(#arrL)" marker-end="url(#arrR)" />\n',
    ]

    for iv in range(min_val, max_val + 1):
        x = to_px(iv)
        is_zero = (iv == 0)
        tick_h = 16 if is_zero else 10
        sw = 2.5 if is_zero else 1.5
        col = "#059669" if is_zero else ("#1e293b" if iv > 0 else "#dc2626")
        svg_parts.append(f'<line x1="{x:.1f}" y1="{axis_y - tick_h/2}" x2="{x:.1f}" y2="{axis_y + tick_h/2}" stroke="{col}" stroke-width="{sw}" />\n')
        font_w = "bold" if is_zero else "normal"
        svg_parts.append(f'<text x="{x:.1f}" y="{axis_y + 22}" text-anchor="middle" font-family="sans-serif" font-size="11" font-weight="{font_w}" fill="{col}">{iv}</text>\n')

    if markers:
        for val, lbl in markers.items():
            mx = to_px(val)
            svg_parts.append(f'<circle cx="{mx:.1f}" cy="{axis_y}" r="4.5" fill="#2563eb" />\n')
            svg_parts.append(f'<text x="{mx:.1f}" y="{axis_y - 12}" text-anchor="middle" font-family="sans-serif" font-size="11" font-weight="bold" fill="#2563eb">{lbl}</text>\n')

    if jump:
        j_start, j_end, j_lbl = jump
        x1 = to_px(j_start)
        x2 = to_px(j_end)
        mid_x = (x1 + x2) / 2
        top_y = axis_y - 32
        d_str = f"M {x1:.1f} {axis_y - 4} Q {mid_x:.1f} {top_y:.1f} {x2:.1f} {axis_y - 4}"
        svg_parts.append(f'<path d="{d_str}" fill="none" stroke="#2563eb" stroke-width="2" marker-end="url(#jumpArr)" />\n')
        svg_parts.append(f'<text x="{mid_x:.1f}" y="{top_y - 4}" text-anchor="middle" font-family="sans-serif" font-size="11" font-weight="bold" fill="#2563eb">{j_lbl}</text>\n')

    svg_parts.append('</svg>\n')
    return "".join(svg_parts)


def draw_thermometer_reading_svg(
    temp_c: int = -15,
    min_t: int = -30,
    max_t: int = 40,
    title: str = "Temperature Reading",
    seed: Optional[int] = None,
    **kwargs: Any,
) -> str:
    """Draws a calibrated Celsius thermometer."""
    width = 180
    height = 280
    entropy_comment = f"<!-- s:{seed} -->\n" if seed is not None else ""

    stem_x = 90
    stem_top = 40
    stem_bot = 220
    bulb_cy = 240
    bulb_r = 20
    stem_w = 12

    clamped = max(min_t, min(max_t, temp_c))
    ratio = (clamped - min_t) / (max_t - min_t)
    liquid_y = stem_bot - ratio * (stem_bot - stem_top)

    svg_parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="auto" style="background-color:#ffffff; max-width:{width}px; margin:auto; display:block;">\n',
        entropy_comment,
        f'<text x="{width/2}" y="20" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="bold" fill="#0f172a">{title}</text>\n',
        # Stem background
        f'<rect x="{stem_x - stem_w/2}" y="{stem_top}" width="{stem_w}" height="{stem_bot - stem_top}" rx="{stem_w/2}" fill="#f1f5f9" stroke="#334155" stroke-width="2" />\n',
        f'<circle cx="{stem_x}" cy="{bulb_cy}" r="{bulb_r}" fill="#f1f5f9" stroke="#334155" stroke-width="2" />\n',
        # Liquid fill (red if >= 0, blue if < 0)
        f'<rect x="{stem_x - stem_w/2 + 2}" y="{liquid_y:.1f}" width="{stem_w - 4}" height="{bulb_cy - liquid_y:.1f}" fill="{"#dc2626" if temp_c >= 0 else "#2563eb"}" />\n',
        f'<circle cx="{stem_x}" cy="{bulb_cy}" r="{bulb_r - 2}" fill="{"#dc2626" if temp_c >= 0 else "#2563eb"}" />\n',
    ]

    # Ticks every 10 degrees
    for t in range(min_t, max_t + 1, 10):
        t_rat = (t - min_t) / (max_t - min_t)
        ty = stem_bot - t_rat * (stem_bot - stem_top)
        is_zero = (t == 0)
        col = "#059669" if is_zero else "#334155"
        t_len = 10 if is_zero else 6
        sw = 2 if is_zero else 1
        svg_parts.append(f'<line x1="{stem_x + stem_w/2}" y1="{ty:.1f}" x2="{stem_x + stem_w/2 + t_len}" y2="{ty:.1f}" stroke="{col}" stroke-width="{sw}" />\n')
        svg_parts.append(f'<text x="{stem_x + stem_w/2 + t_len + 4}" y="{ty + 4:.1f}" font-family="sans-serif" font-size="10" font-weight="{"bold" if is_zero else "normal"}" fill="{col}">{t}°C</text>\n')

    # Current reading banner
    svg_parts.append(f'<rect x="20" y="{stem_top + 10}" width="48" height="24" rx="4" fill="#eff6ff" stroke="#2563eb" stroke-width="1.5" />\n')
    svg_parts.append(f'<text x="44" y="{stem_top + 26}" text-anchor="middle" font-family="sans-serif" font-size="11" font-weight="bold" fill="#1e40af">{temp_c}°C</text>\n')

    svg_parts.append('</svg>\n')
    return "".join(svg_parts)


def draw_elevation_depth_svg(
    mountain_m: int = 1500,
    sea_level: int = 0,
    mine_m: int = -800,
    seed: Optional[int] = None,
    **kwargs: Any,
) -> str:
    """Draws an elevation profile showing mountain, sea level, and underground mine."""
    width = 380
    height = 240
    entropy_comment = f"<!-- s:{seed} -->\n" if seed is not None else ""

    sea_y = 120
    top_y = 40
    bot_y = 200

    svg_parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="auto" style="background-color:#ffffff; max-width:{width}px; margin:auto; display:block;">\n',
        entropy_comment,
        f'<text x="{width/2}" y="20" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="bold" fill="#0f172a">Elevation &amp; Depth Profile</text>\n',
        # Mountain triangle
        f'<polygon points="40,{sea_y} 120,{top_y} 200,{sea_y}" fill="#dcfce7" stroke="#16a34a" stroke-width="2" />\n',
        f'<circle cx="120" cy="{top_y}" r="4" fill="#16a34a" />\n',
        f'<text x="120" y="{top_y - 8}" text-anchor="middle" font-family="sans-serif" font-size="11" font-weight="bold" fill="#15803d">Peak (+{mountain_m} m)</text>\n',
        # Sea level line
        f'<line x1="20" y1="{sea_y}" x2="360" y2="{sea_y}" stroke="#0284c7" stroke-width="2.5" stroke-dasharray="6,4" />\n',
        f'<text x="350" y="{sea_y - 6}" text-anchor="end" font-family="sans-serif" font-size="11" font-weight="bold" fill="#0369a1">Sea Level (0 m)</text>\n',
        # Mine shaft rectangle below sea level
        f'<rect x="230" y="{sea_y}" width="90" height="{bot_y - sea_y}" fill="#f1f5f9" stroke="#64748b" stroke-width="2" />\n',
        f'<circle cx="275" cy="{bot_y}" r="4" fill="#dc2626" />\n',
        f'<text x="275" y="{bot_y + 18}" text-anchor="middle" font-family="sans-serif" font-size="11" font-weight="bold" fill="#b91c1c">Mine Shaft ({mine_m} m)</text>\n',
        '</svg>\n',
    ]
    return "".join(svg_parts)
