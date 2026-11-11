"""Grade 9 Mathematics - Patterns SVG Diagrams.
Publication-grade SVG renderers for matchstick patterns, tile paving borders,
inverse proportion hyperbolas, and table/chair seating layouts.
"""
from __future__ import annotations

from typing import Any, List, Optional, Tuple


def draw_matchstick_squares_svg(
    stages: int = 3,
    seed: Optional[int] = None,
    **kwargs: Any,
) -> str:
    """Draws stages 1, 2, and 3 of linked matchstick squares (4, 7, 10 sticks)."""
    entropy_comment = f"<!-- s:{seed} -->\n" if seed is not None else ""
    width = 480
    height = 140

    sticks_svg = []
    labels_svg = []

    stage_configs = [(1, 30, 4), (2, 130, 7), (3, 270, 10)]

    sq_size = 28

    for stage_num, start_x, total_sticks in stage_configs:
        y_top = 45
        y_bot = y_top + sq_size

        # Draw squares for this stage
        for i in range(stage_num):
            x_left = start_x + i * sq_size
            x_right = x_left + sq_size

            # Top stick
            sticks_svg.append(f'<line x1="{x_left}" y1="{y_top}" x2="{x_right}" y2="{y_top}" stroke="#D97706" stroke-width="3" stroke-linecap="round"/>')
            # Bottom stick
            sticks_svg.append(f'<line x1="{x_left}" y1="{y_bot}" x2="{x_right}" y2="{y_bot}" stroke="#D97706" stroke-width="3" stroke-linecap="round"/>')
            # Left stick (only for first square)
            if i == 0:
                sticks_svg.append(f'<line x1="{x_left}" y1="{y_top}" x2="{x_left}" y2="{y_bot}" stroke="#DC2626" stroke-width="3" stroke-linecap="round"/>')
            # Right stick
            sticks_svg.append(f'<line x1="{x_right}" y1="{y_top}" x2="{x_right}" y2="{y_bot}" stroke="#DC2626" stroke-width="3" stroke-linecap="round"/>')

        mid_x = start_x + (stage_num * sq_size) / 2
        labels_svg.append(
            f'<text x="{mid_x}" y="{y_bot + 24}" text-anchor="middle" font-size="12" font-weight="600" font-family="sans-serif" fill="#1E293B">'
            f'Stage {stage_num}</text>'
        )
        labels_svg.append(
            f'<text x="{mid_x}" y="{y_bot + 40}" text-anchor="middle" font-size="11" font-family="sans-serif" fill="#64748B">'
            f'({total_sticks} sticks)</text>'
        )

    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
        f'width="{width}" height="{height}" class="mx-auto block" style="background:#F8FAFC;border-radius:8px;">\n'
        f"{entropy_comment}"
        f'  <g id="matchstick_squares">\n'
        f"    {''.join(sticks_svg)}\n"
        f"    {''.join(labels_svg)}\n"
        f'  </g>\n'
        f'</svg>'
    )


def draw_matchstick_triangles_svg(
    stages: int = 3,
    seed: Optional[int] = None,
    **kwargs: Any,
) -> str:
    """Draws stages 1, 2, and 3 of linked matchstick triangles (3, 5, 7 sticks)."""
    entropy_comment = f"<!-- s:{seed} -->\n" if seed is not None else ""
    width = 460
    height = 140

    sticks_svg = []
    labels_svg = []

    stage_configs = [(1, 40, 3), (2, 140, 5), (3, 270, 7)]
    base_w = 30
    tri_h = 32

    for stage_num, start_x, total_sticks in stage_configs:
        y_bot = 80
        y_top = y_bot - tri_h

        for i in range(stage_num):
            x1 = start_x + i * base_w
            x2 = x1 + base_w
            xm = (x1 + x2) / 2

            # Base stick
            sticks_svg.append(f'<line x1="{x1}" y1="{y_bot}" x2="{x2}" y2="{y_bot}" stroke="#D97706" stroke-width="3" stroke-linecap="round"/>')
            # Left diagonal stick
            if i == 0 or True:
                sticks_svg.append(f'<line x1="{x1}" y1="{y_bot}" x2="{xm}" y2="{y_top}" stroke="#2563EB" stroke-width="3" stroke-linecap="round"/>')
            # Right diagonal stick
            sticks_svg.append(f'<line x1="{xm}" y1="{y_top}" x2="{x2}" y2="{y_bot}" stroke="#2563EB" stroke-width="3" stroke-linecap="round"/>')

        mid_x = start_x + (stage_num * base_w) / 2
        labels_svg.append(
            f'<text x="{mid_x}" y="{y_bot + 24}" text-anchor="middle" font-size="12" font-weight="600" font-family="sans-serif" fill="#1E293B">'
            f'Stage {stage_num}</text>'
        )
        labels_svg.append(
            f'<text x="{mid_x}" y="{y_bot + 40}" text-anchor="middle" font-size="11" font-family="sans-serif" fill="#64748B">'
            f'({total_sticks} sticks)</text>'
        )

    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
        f'width="{width}" height="{height}" class="mx-auto block" style="background:#F8FAFC;border-radius:8px;">\n'
        f"{entropy_comment}"
        f'  <g id="matchstick_triangles">\n'
        f"    {''.join(sticks_svg)}\n"
        f"    {''.join(labels_svg)}\n"
        f'  </g>\n'
        f'</svg>'
    )


def draw_inverse_proportion_hyperbola_svg(
    k: int = 24,
    seed: Optional[int] = None,
    **kwargs: Any,
) -> str:
    """Draws a first-quadrant hyperbola y = k / x with marked points."""
    entropy_comment = f"<!-- s:{seed} -->\n" if seed is not None else ""
    width = 380
    height = 240
    ox = 50
    oy = 195
    gx_w = 300
    gy_h = 160

    max_x = 12
    max_y = 24

    # Axes
    axes_svg = [
        f'<line x1="{ox}" y1="{oy}" x2="{ox + gx_w + 15}" y2="{oy}" stroke="#334155" stroke-width="2"/>',
        f'<line x1="{ox}" y1="{oy}" x2="{ox}" y2="{oy - gy_h - 15}" stroke="#334155" stroke-width="2"/>',
        f'<text x="{ox + gx_w + 10}" y="{oy + 20}" font-size="12" font-family="sans-serif" fill="#1E293B">x</text>',
        f'<text x="{ox - 20}" y="{oy - gy_h - 10}" font-size="12" font-family="sans-serif" fill="#1E293B">y</text>',
    ]

    # Curve path points
    curve_pts = []
    x_val = 1.0
    while x_val <= max_x:
        y_val = k / x_val
        px = ox + (x_val / max_x) * gx_w
        py = oy - (y_val / max_y) * gy_h
        curve_pts.append(f"{px:.1f},{py:.1f}")
        x_val += 0.2

    path_d = "M " + " L ".join(curve_pts)
    curve_svg = f'<path d="{path_d}" fill="none" stroke="#2563EB" stroke-width="2.5"/>'

    # Marked integer points
    sample_points = [(1, 24), (2, 12), (3, 8), (4, 6), (6, 4), (8, 3)]
    pts_svg = []
    for x_i, y_i in sample_points:
        px = ox + (x_i / max_x) * gx_w
        py = oy - (y_i / max_y) * gy_h
        pts_svg.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="4.5" fill="#DC2626" stroke="#FFFFFF" stroke-width="1.5"/>')

    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
        f'width="{width}" height="{height}" class="mx-auto block" style="background:#F8FAFC;border-radius:8px;">\n'
        f"{entropy_comment}"
        f'  <g id="hyperbola_plot">\n'
        f"    {''.join(axes_svg)}\n"
        f"    {curve_svg}\n"
        f"    {''.join(pts_svg)}\n"
        f'    <text x="{width/2}" y="25" text-anchor="middle" font-size="13" font-weight="bold" font-family="sans-serif" fill="#1E293B">'
        f'Inverse Proportion: y = {k} / x (xy = {k})</text>\n'
        f'  </g>\n'
        f'</svg>'
    )
