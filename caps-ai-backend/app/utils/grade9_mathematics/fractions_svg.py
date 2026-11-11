"""Grade 9 Mathematics - Common Fractions SVG Diagrams.
Publication-grade SVG renderers for fraction strips, fraction number lines,
pie/circle fraction models, and liquid tank gauges.
"""
from __future__ import annotations

import math
from typing import Any, List, Optional, Tuple


def draw_fraction_strip_svg(
    numerator: int,
    denominator: int,
    label: str = "Fraction Bar",
    seed: Optional[int] = None,
    **kwargs: Any,
) -> str:
    """Draws a rectangular fraction strip divided into `denominator` equal parts,

    with `numerator` parts shaded.
    """
    entropy_comment = f"<!-- s:{seed} -->\n" if seed is not None else ""
    width = 460
    height = 110
    pad_x = 30
    pad_y = 25
    strip_w = width - 2 * pad_x
    strip_h = 45

    part_w = strip_w / max(1, denominator)

    parts_svg = []
    for i in range(denominator):
        x = pad_x + i * part_w
        if i < numerator:
            fill = "#2563EB"
            fill_opacity = "0.85"
            stroke_col = "#1E40AF"
        else:
            fill = "#F8FAFC"
            fill_opacity = "1.0"
            stroke_col = "#64748B"

        parts_svg.append(
            f'<rect x="{x:.1f}" y="{pad_y:.1f}" width="{part_w:.1f}" height="{strip_h:.1f}" '
            f'fill="{fill}" fill-opacity="{fill_opacity}" stroke="{stroke_col}" stroke-width="1.5"/>'
        )

    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
        f'width="{width}" height="{height}" class="mx-auto block" style="background:#FFFFFF;border-radius:8px;border:1px solid #E2E8F0;">\n'
        f"{entropy_comment}"
        f'  <g id="fraction_strip">\n'
        f"    {''.join(parts_svg)}\n"
        f'    <rect x="{pad_x}" y="{pad_y}" width="{strip_w}" height="{strip_h}" '
        f'fill="none" stroke="#0F172A" stroke-width="2.5" rx="2"/>\n'
        f'    <text x="{width/2}" y="{pad_y + strip_h + 24}" text-anchor="middle" font-size="13" '
        f'font-family="sans-serif" fill="#334155" font-weight="600">{label} ({denominator} equal parts)</text>\n'
        f'  </g>\n'
        f'</svg>'
    )


def draw_fraction_number_line_svg(
    start_int: int,
    end_int: int,
    denominator: int,
    marked_points: List[Tuple[float, str]],
    seed: Optional[int] = None,
    **kwargs: Any,
) -> str:
    """Draws a number line between integers with fractional tick subdivisions

    and labeled points.
    """
    entropy_comment = f"<!-- s:{seed} -->\n" if seed is not None else ""
    width = 540
    height = 130
    pad_x = 45
    pad_y = 65
    line_w = width - 2 * pad_x

    span = end_int - start_int
    if span <= 0:
        span = 1

    total_subdivisions = span * denominator
    sub_step = span / total_subdivisions

    ticks_svg = []
    # Main baseline
    ticks_svg.append(
        f'<line x1="{pad_x - 15}" y1="{pad_y}" x2="{pad_x + line_w + 15}" y2="{pad_y}" stroke="#0F172A" stroke-width="2.5"/>'
    )
    # Arrow heads
    ticks_svg.append(
        f'<polygon points="{pad_x - 18},{pad_y} {pad_x - 10},{pad_y - 5} {pad_x - 10},{pad_y + 5}" fill="#0F172A"/>'
    )
    ticks_svg.append(
        f'<polygon points="{pad_x + line_w + 18},{pad_y} {pad_x + line_w + 10},{pad_y - 5} {pad_x + line_w + 10},{pad_y + 5}" fill="#0F172A"/>'
    )

    # Subdivisions
    for step_i in range(total_subdivisions + 1):
        cur_val = start_int + step_i * sub_step
        pos_ratio = (cur_val - start_int) / span
        x = pad_x + pos_ratio * line_w

        is_integer = (step_i % denominator) == 0
        tick_len = 12 if is_integer else 6
        stroke_w = 2.0 if is_integer else 1.2
        stroke_c = "#0F172A" if is_integer else "#64748B"

        ticks_svg.append(
            f'<line x1="{x:.1f}" y1="{pad_y - tick_len}" x2="{x:.1f}" y2="{pad_y + tick_len}" stroke="{stroke_c}" stroke-width="{stroke_w}"/>'
        )

        if is_integer:
            int_val = int(round(cur_val))
            ticks_svg.append(
                f'<text x="{x:.1f}" y="{pad_y + 26}" text-anchor="middle" font-size="14" font-weight="700" font-family="sans-serif" fill="#0F172A">{int_val}</text>'
            )

    points_svg = []
    colors = ["#DC2626", "#2563EB", "#059669", "#D97706"]
    for idx, (p_val, label) in enumerate(marked_points):
        pos_ratio = (p_val - start_int) / span
        px = pad_x + pos_ratio * line_w
        color = colors[idx % len(colors)]
        points_svg.append(
            f'<circle cx="{px:.1f}" cy="{pad_y}" r="6.5" fill="{color}" stroke="#FFFFFF" stroke-width="2"/>'
        )
        points_svg.append(
            f'<line x1="{px:.1f}" y1="{pad_y - 7}" x2="{px:.1f}" y2="{pad_y - 24}" stroke="{color}" stroke-width="2" stroke-dasharray="3,2"/>'
        )
        points_svg.append(
            f'<rect x="{px - 14:.1f}" y="{pad_y - 42}" width="28" height="18" rx="4" fill="{color}"/>'
        )
        points_svg.append(
            f'<text x="{px:.1f}" y="{pad_y - 29}" text-anchor="middle" font-size="12" font-weight="700" font-family="sans-serif" fill="#FFFFFF">{label}</text>'
        )

    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
        f'width="{width}" height="{height}" class="mx-auto block" style="background:#FFFFFF;border-radius:8px;border:1px solid #E2E8F0;">\n'
        f"{entropy_comment}"
        f'  <g id="fraction_number_line">\n'
        f"    {''.join(ticks_svg)}\n"
        f"    {''.join(points_svg)}\n"
        f'  </g>\n'
        f'</svg>'
    )


def draw_pie_fraction_svg(
    slices: List[Tuple[int, str, str]],
    total_parts: int,
    seed: Optional[int] = None,
    **kwargs: Any,
) -> str:
    """Draws a pie chart partitioned into `total_parts` with colored wedge slices.

    slices is a list of (count, label, color_hex).
    """
    entropy_comment = f"<!-- s:{seed} -->\n" if seed is not None else ""
    width = 380
    height = 240
    cx = 120
    cy = 120
    r = 85

    paths_svg = []
    current_angle = -math.pi / 2  # Start at top (12 o'clock)

    for count, label, color in slices:
        sweep_angle = (count / max(1, total_parts)) * 2 * math.pi
        end_angle = current_angle + sweep_angle

        x1 = cx + r * math.cos(current_angle)
        y1 = cy + r * math.sin(current_angle)
        x2 = cx + r * math.cos(end_angle)
        y2 = cy + r * math.sin(end_angle)

        large_arc = 1 if sweep_angle > math.pi else 0

        path_d = f"M {cx} {cy} L {x1:.2f} {y1:.2f} A {r} {r} 0 {large_arc} 1 {x2:.2f} {y2:.2f} Z"
        paths_svg.append(
            f'<path d="{path_d}" fill="{color}" fill-opacity="0.85" stroke="#FFFFFF" stroke-width="2"/>'
        )

        current_angle = end_angle

    # Legend
    legend_svg = []
    leg_x = 240
    leg_y = 50
    for idx, (count, label, color) in enumerate(slices):
        y_pos = leg_y + idx * 30
        fraction_str = f"{count}/{total_parts}"
        legend_svg.append(
            f'<rect x="{leg_x}" y="{y_pos}" width="16" height="16" rx="3" fill="{color}"/>'
        )
        legend_svg.append(
            f'<text x="{leg_x + 24}" y="{y_pos + 13}" font-size="12" font-family="sans-serif" font-weight="600" fill="#1E293B">'
            f'{label} ({fraction_str})</text>'
        )

    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
        f'width="{width}" height="{height}" class="mx-auto block" style="background:#FFFFFF;border-radius:8px;border:1px solid #E2E8F0;">\n'
        f"{entropy_comment}"
        f'  <g id="pie_fraction_chart">\n'
        f"    {''.join(paths_svg)}\n"
        f'    <circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="#0F172A" stroke-width="2"/>\n'
        f"    {''.join(legend_svg)}\n"
        f'  </g>\n'
        f'</svg>'
    )


def draw_tank_gauge_svg(
    numerator: int,
    denominator: int,
    label: str = "Fuel Tank Level",
    seed: Optional[int] = None,
    **kwargs: Any,
) -> str:
    """Draws a horizontal tank / fuel container divided into `denominator` segments,

    with `numerator` segments filled with fluid.
    """
    entropy_comment = f"<!-- s:{seed} -->\n" if seed is not None else ""
    width = 460
    height = 120
    pad_x = 40
    pad_y = 30
    tank_w = width - 2 * pad_x
    tank_h = 42

    part_w = tank_w / max(1, denominator)

    segments_svg = []
    for i in range(denominator):
        x = pad_x + i * part_w
        if i < numerator:
            fill = "#059669"
            fill_opacity = "0.85"
            stroke_col = "#047857"
        else:
            fill = "#F1F5F9"
            fill_opacity = "1.0"
            stroke_col = "#94A3B8"

        segments_svg.append(
            f'<rect x="{x:.1f}" y="{pad_y:.1f}" width="{part_w:.1f}" height="{tank_h:.1f}" '
            f'fill="{fill}" fill-opacity="{fill_opacity}" stroke="{stroke_col}" stroke-width="1.5"/>'
        )

    pct = round((numerator / max(1, denominator)) * 100)

    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
        f'width="{width}" height="{height}" class="mx-auto block" style="background:#FFFFFF;border-radius:8px;border:1px solid #E2E8F0;">\n'
        f"{entropy_comment}"
        f'  <g id="tank_gauge">\n'
        f"    {''.join(segments_svg)}\n"
        f'    <rect x="{pad_x}" y="{pad_y}" width="{tank_w}" height="{tank_h}" fill="none" stroke="#0F172A" stroke-width="2.5" rx="3"/>\n'
        f'    <text x="{width/2}" y="{pad_y + tank_h + 24}" text-anchor="middle" font-size="13" '
        f'font-family="sans-serif" fill="#1E293B" font-weight="600">{label}: {numerator}/{denominator} full ({pct}%)</text>\n'
        f'  </g>\n'
        f'</svg>'
    )
