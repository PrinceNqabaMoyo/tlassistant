"""Grade 9 Mathematics - Representing Data SVG Builders (CAPS Term 4).
Generates deterministic SVG figures for bar charts, double bar graphs, histograms,
pie charts, broken line graphs, scatter plots, and stem-and-leaf diagrams.
Zero LLM calls, deterministic seed entropy.
"""
from __future__ import annotations

import math
from typing import Any, Dict, List, Optional, Tuple


def draw_bar_chart_svg(
    categories: List[str],
    values: List[float | int],
    title: str = "Bar Graph",
    y_label: str = "Frequency",
    seed: Optional[int] = None,
    width: int = 460,
    height: int = 340,
) -> str:
    s_tag = f"<!-- s:{seed} -->\n" if seed is not None else ""
    w, h = float(width), float(height)
    pad_l, pad_r, pad_t, pad_b = 60.0, 30.0, 50.0, 60.0

    plot_w = w - pad_l - pad_r
    plot_h = h - pad_t - pad_b
    max_v = max(values) if values else 10
    y_max = math.ceil(max_v * 1.2) if max_v > 0 else 10

    n = len(categories)
    slot_w = plot_w / n if n > 0 else plot_w
    bar_w = slot_w * 0.65

    svg_lines = [
        f'{s_tag}<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
        f'width="{width}" height="{height}" style="background:#ffffff; font-family:system-ui,-apple-system,sans-serif;">',
        f'  <rect x="0" y="0" width="{width}" height="{height}" fill="#ffffff"/>',
        f'  <!-- Title -->',
        f'  <text x="{w/2}" y="28" font-size="14" font-weight="bold" text-anchor="middle" fill="#0f172a">{title}</text>',
        f'  <!-- Y-axis -->',
        f'  <line x1="{pad_l}" y1="{pad_t}" x2="{pad_l}" y2="{pad_t + plot_h}" stroke="#334155" stroke-width="2"/>',
        f'  <!-- X-axis -->',
        f'  <line x1="{pad_l}" y1="{pad_t + plot_h}" x2="{w - pad_r}" y2="{pad_t + plot_h}" stroke="#334155" stroke-width="2"/>',
        f'  <text x="20" y="{pad_t + plot_h/2}" font-size="12" font-weight="bold" fill="#475569" transform="rotate(-90,20,{pad_t + plot_h/2})" text-anchor="middle">{y_label}</text>',
    ]

    # Grid lines and Y ticks
    num_ticks = 5
    for i in range(num_ticks + 1):
        v = (y_max / num_ticks) * i
        y_pos = pad_t + plot_h - (v / y_max) * plot_h
        svg_lines.append(f'  <line x1="{pad_l}" y1="{y_pos}" x2="{w - pad_r}" y2="{y_pos}" stroke="#e2e8f0" stroke-width="1"/>')
        svg_lines.append(f'  <text x="{pad_l - 8}" y="{y_pos + 4}" font-size="11" text-anchor="end" fill="#64748b">{round(v, 1) if v % 1 else int(v)}</text>')

    # Bars
    colors = ["#3b82f6", "#10b981", "#f59e0b", "#8b5cf6", "#ec4899", "#06b6d4"]
    for i, (cat, val) in enumerate(zip(categories, values)):
        bx = pad_l + i * slot_w + (slot_w - bar_w) / 2.0
        bar_len = (val / y_max) * plot_h
        by = pad_t + plot_h - bar_len
        col = colors[i % len(colors)]
        svg_lines.append(f'  <rect x="{bx}" y="{by}" width="{bar_w}" height="{bar_len}" fill="{col}" rx="2" stroke="#1e293b" stroke-width="1.2"/>')
        # Bar top value
        svg_lines.append(f'  <text x="{bx + bar_w/2}" y="{by - 6}" font-size="11" font-weight="bold" text-anchor="middle" fill="#0f172a">{val}</text>')
        # X label
        svg_lines.append(f'  <text x="{bx + bar_w/2}" y="{pad_t + plot_h + 20}" font-size="11" text-anchor="middle" fill="#1e293b">{cat}</text>')

    svg_lines.append('</svg>')
    return "\n".join(svg_lines)


def draw_histogram_svg(
    bin_labels: List[str],
    counts: List[int],
    title: str = "Histogram",
    x_label: str = "Class Interval",
    y_label: str = "Frequency",
    seed: Optional[int] = None,
    width: int = 460,
    height: int = 340,
) -> str:
    s_tag = f"<!-- s:{seed} -->\n" if seed is not None else ""
    w, h = float(width), float(height)
    pad_l, pad_r, pad_t, pad_b = 60.0, 30.0, 50.0, 60.0
    plot_w = w - pad_l - pad_r
    plot_h = h - pad_t - pad_b
    max_c = max(counts) if counts else 10
    y_max = math.ceil(max_c * 1.25)

    n = len(bin_labels)
    bar_w = plot_w / n if n > 0 else plot_w  # No gap between bars in a histogram

    svg_lines = [
        f'{s_tag}<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
        f'width="{width}" height="{height}" style="background:#ffffff; font-family:system-ui,-apple-system,sans-serif;">',
        f'  <rect x="0" y="0" width="{width}" height="{height}" fill="#ffffff"/>',
        f'  <text x="{w/2}" y="28" font-size="14" font-weight="bold" text-anchor="middle" fill="#0f172a">{title}</text>',
        f'  <line x1="{pad_l}" y1="{pad_t}" x2="{pad_l}" y2="{pad_t + plot_h}" stroke="#334155" stroke-width="2"/>',
        f'  <line x1="{pad_l}" y1="{pad_t + plot_h}" x2="{w - pad_r}" y2="{pad_t + plot_h}" stroke="#334155" stroke-width="2"/>',
        f'  <text x="20" y="{pad_t + plot_h/2}" font-size="12" font-weight="bold" fill="#475569" transform="rotate(-90,20,{pad_t + plot_h/2})" text-anchor="middle">{y_label}</text>',
    ]

    for i in range(5):
        v = (y_max / 4) * i
        y_pos = pad_t + plot_h - (v / y_max) * plot_h
        svg_lines.append(f'  <line x1="{pad_l}" y1="{y_pos}" x2="{w - pad_r}" y2="{y_pos}" stroke="#e2e8f0" stroke-width="1"/>')
        svg_lines.append(f'  <text x="{pad_l - 8}" y="{y_pos + 4}" font-size="11" text-anchor="end" fill="#64748b">{int(v)}</text>')

    for i, (bin_l, c) in enumerate(zip(bin_labels, counts)):
        bx = pad_l + i * bar_w
        bar_len = (c / y_max) * plot_h
        by = pad_t + plot_h - bar_len
        svg_lines.append(f'  <rect x="{bx}" y="{by}" width="{bar_w}" height="{bar_len}" fill="#3b82f6" fill-opacity="0.75" stroke="#1d4ed8" stroke-width="1.5"/>')
        svg_lines.append(f'  <text x="{bx + bar_w/2}" y="{by - 6}" font-size="11" font-weight="bold" text-anchor="middle" fill="#1e3a8a">{c}</text>')
        svg_lines.append(f'  <text x="{bx + bar_w/2}" y="{pad_t + plot_h + 20}" font-size="10" text-anchor="middle" fill="#1e293b">{bin_l}</text>')

    svg_lines.append(f'  <text x="{pad_l + plot_w/2}" y="{h - 10}" font-size="12" font-weight="bold" text-anchor="middle" fill="#475569">{x_label}</text>')
    svg_lines.append('</svg>')
    return "\n".join(svg_lines)


def draw_pie_chart_svg(
    slices: List[Tuple[str, float | int]],  # [(label, value), ...]
    title: str = "Pie Chart",
    seed: Optional[int] = None,
    width: int = 460,
    height: int = 340,
) -> str:
    s_tag = f"<!-- s:{seed} -->\n" if seed is not None else ""
    w, h = float(width), float(height)
    cx, cy = w / 2.0 - 50.0, h / 2.0 + 10.0
    r = 110.0

    total = sum(v for _, v in slices) if slices else 1
    colors = ["#3b82f6", "#10b981", "#f59e0b", "#ef4444", "#8b5cf6", "#06b6d4"]

    svg_lines = [
        f'{s_tag}<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
        f'width="{width}" height="{height}" style="background:#ffffff; font-family:system-ui,-apple-system,sans-serif;">',
        f'  <rect x="0" y="0" width="{width}" height="{height}" fill="#ffffff"/>',
        f'  <text x="{w/2}" y="28" font-size="14" font-weight="bold" text-anchor="middle" fill="#0f172a">{title}</text>',
    ]

    cur_ang = -math.pi / 2.0  # Start from top
    legend_y = 60.0

    for idx, (lbl, val) in enumerate(slices):
        pct = (val / total) * 100.0
        deg = (val / total) * 360.0
        ang = (val / total) * 2.0 * math.pi
        next_ang = cur_ang + ang

        x1 = cx + r * math.cos(cur_ang)
        y1 = cy + r * math.sin(cur_ang)
        x2 = cx + r * math.cos(next_ang)
        y2 = cy + r * math.sin(next_ang)
        large_arc = 1 if ang > math.pi else 0

        col = colors[idx % len(colors)]
        svg_lines.append(
            f'  <path d="M {cx} {cy} L {x1:.2f} {y1:.2f} A {r} {r} 0 {large_arc} 1 {x2:.2f} {y2:.2f} Z" '
            f'fill="{col}" fill-opacity="0.85" stroke="#ffffff" stroke-width="2"/>'
        )

        # Label inside slice if wide enough
        mid_ang = cur_ang + ang / 2.0
        lx = cx + (r * 0.65) * math.cos(mid_ang)
        ly = cy + (r * 0.65) * math.sin(mid_ang)
        svg_lines.append(f'  <text x="{lx:.1f}" y="{ly + 4:.1f}" font-size="11" font-weight="bold" text-anchor="middle" fill="#ffffff">{round(pct)}%</text>')

        # Legend entry on right
        leg_x = w - 140.0
        svg_lines.append(f'  <rect x="{leg_x}" y="{legend_y}" width="14" height="14" fill="{col}" rx="2"/>')
        svg_lines.append(f'  <text x="{leg_x + 22}" y="{legend_y + 11}" font-size="11" fill="#1e293b">{lbl} ({val})</text>')
        legend_y += 24.0
        cur_ang = next_ang

    svg_lines.append('</svg>')
    return "\n".join(svg_lines)


def draw_broken_line_graph_svg(
    x_points: List[str],
    y_points: List[float | int],
    title: str = "Line Graph",
    x_label: str = "Time",
    y_label: str = "Value",
    seed: Optional[int] = None,
    width: int = 460,
    height: int = 340,
) -> str:
    s_tag = f"<!-- s:{seed} -->\n" if seed is not None else ""
    w, h = float(width), float(height)
    pad_l, pad_r, pad_t, pad_b = 60.0, 30.0, 50.0, 60.0
    plot_w = w - pad_l - pad_r
    plot_h = h - pad_t - pad_b
    max_y = max(y_points) if y_points else 10
    y_max = math.ceil(max_y * 1.25)

    n = len(x_points)
    step_x = plot_w / (n - 1) if n > 1 else plot_w

    svg_lines = [
        f'{s_tag}<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
        f'width="{width}" height="{height}" style="background:#ffffff; font-family:system-ui,-apple-system,sans-serif;">',
        f'  <rect x="0" y="0" width="{width}" height="{height}" fill="#ffffff"/>',
        f'  <text x="{w/2}" y="28" font-size="14" font-weight="bold" text-anchor="middle" fill="#0f172a">{title}</text>',
        f'  <line x1="{pad_l}" y1="{pad_t}" x2="{pad_l}" y2="{pad_t + plot_h}" stroke="#334155" stroke-width="2"/>',
        f'  <line x1="{pad_l}" y1="{pad_t + plot_h}" x2="{w - pad_r}" y2="{pad_t + plot_h}" stroke="#334155" stroke-width="2"/>',
        f'  <text x="20" y="{pad_t + plot_h/2}" font-size="12" font-weight="bold" fill="#475569" transform="rotate(-90,20,{pad_t + plot_h/2})" text-anchor="middle">{y_label}</text>',
    ]

    for i in range(5):
        v = (y_max / 4) * i
        y_pos = pad_t + plot_h - (v / y_max) * plot_h
        svg_lines.append(f'  <line x1="{pad_l}" y1="{y_pos}" x2="{w - pad_r}" y2="{y_pos}" stroke="#e2e8f0" stroke-width="1"/>')
        svg_lines.append(f'  <text x="{pad_l - 8}" y="{y_pos + 4}" font-size="11" text-anchor="end" fill="#64748b">{round(v, 1) if v % 1 else int(v)}</text>')

    coords = []
    for i, (xp, yp) in enumerate(zip(x_points, y_points)):
        cx_pt = pad_l + i * step_x
        cy_pt = pad_t + plot_h - (yp / y_max) * plot_h
        coords.append((cx_pt, cy_pt))
        svg_lines.append(f'  <text x="{cx_pt}" y="{pad_t + plot_h + 20}" font-size="10" text-anchor="middle" fill="#1e293b">{xp}</text>')

    # Polyline
    pts_str = " ".join(f"{x:.1f},{y:.1f}" for x, y in coords)
    svg_lines.append(f'  <polyline points="{pts_str}" fill="none" stroke="#2563eb" stroke-width="2.5"/>')
    for cx_pt, cy_pt in coords:
        svg_lines.append(f'  <circle cx="{cx_pt:.1f}" cy="{cy_pt:.1f}" r="4.5" fill="#1d4ed8" stroke="#ffffff" stroke-width="1.5"/>')

    svg_lines.append(f'  <text x="{pad_l + plot_w/2}" y="{h - 10}" font-size="12" font-weight="bold" text-anchor="middle" fill="#475569">{x_label}</text>')
    svg_lines.append('</svg>')
    return "\n".join(svg_lines)
