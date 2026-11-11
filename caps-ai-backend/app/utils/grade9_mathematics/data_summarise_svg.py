"""Grade 9 Mathematics - Collect, Organise & Summarise Data SVG Diagram Renderers.
================================================================================
Provides deterministic SVG generators for:
  - Tally charts with bundles of 5
  - Ungrouped and grouped frequency tables
  - Dot plots on number lines
  - Stem-and-leaf diagrams with keys

All SVGs inject <!-- s:{seed} --> for referee audit tracking and 100% AST purity.
"""
from __future__ import annotations

import math
import random
from typing import Dict, List, Optional, Tuple


def _render_tally_bundle(count: int, x: float, y: float) -> List[str]:
    """Draws SVG tally marks for a given count at position (x, y)."""
    svg_elements: List[str] = []
    curr_x = x
    rem = count

    while rem > 0:
        group = min(rem, 5)
        # Vertical lines
        lines_in_bundle = min(group, 4)
        for i in range(lines_in_bundle):
            lx = curr_x + i * 5
            svg_elements.append(f'<line x1="{lx}" y1="{y - 12}" x2="{lx}" y2="{y + 4}" stroke="#1e293b" stroke-width="2" stroke-linecap="round"/>')
        # Diagonal slash if 5
        if group == 5:
            svg_elements.append(f'<line x1="{curr_x - 3}" y1="{y + 2}" x2="{curr_x + 18}" y2="{y - 10}" stroke="#dc2626" stroke-width="2" stroke-linecap="round"/>')
            curr_x += 28
        else:
            curr_x += lines_in_bundle * 5 + 8
        rem -= group

    return svg_elements


def draw_tally_chart_svg(
    rows: List[Tuple[str, int]],
    title: str = "Tally Chart",
    col1_label: str = "Category",
    seed: Optional[int] = None,
) -> str:
    """Renders a clean SVG tally chart table."""
    width = 420
    row_height = 32
    header_height = 40
    height = header_height + (len(rows) + 1) * row_height + 40

    svg_parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="auto">',
        f"<!-- s:{seed} -->",
        '<rect width="100%" height="100%" fill="#f8fafc" rx="8"/>',
        f'<text x="{width / 2}" y="24" font-family="Arial, sans-serif" font-size="15" font-weight="bold" fill="#0f172a" text-anchor="middle">{title}</text>',
    ]

    # Table Header
    y_hdr = 50
    svg_parts.append(f'<rect x="25" y="{y_hdr}" width="{width - 50}" height="{row_height}" fill="#e2e8f0" rx="4"/>')
    svg_parts.append(f'<text x="45" y="{y_hdr + 21}" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="#1e293b">{col1_label}</text>')
    svg_parts.append(f'<text x="210" y="{y_hdr + 21}" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="#1e293b">Tally Marks</text>')
    svg_parts.append(f'<text x="350" y="{y_hdr + 21}" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="#1e293b" text-anchor="middle">Frequency (f)</text>')

    # Rows
    y = y_hdr + row_height
    tot = 0
    for idx, (label, count) in enumerate(rows):
        tot += count
        bg_fill = "#ffffff" if idx % 2 == 0 else "#f1f5f9"
        svg_parts.append(f'<rect x="25" y="{y}" width="{width - 50}" height="{row_height}" fill="{bg_fill}"/>')
        svg_parts.append(f'<line x1="25" y1="{y + row_height}" x2="{width - 25}" y2="{y + row_height}" stroke="#cbd5e1" stroke-width="1"/>')
        svg_parts.append(f'<text x="45" y="{y + 21}" font-family="Arial, sans-serif" font-size="13" fill="#0f172a">{label}</text>')
        # Tally marks
        svg_parts.extend(_render_tally_bundle(count, 175, y + 17))
        svg_parts.append(f'<text x="350" y="{y + 21}" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="middle">{count}</text>')
        y += row_height

    # Total Row
    svg_parts.append(f'<rect x="25" y="{y}" width="{width - 50}" height="{row_height}" fill="#e2e8f0" rx="4"/>')
    svg_parts.append(f'<text x="45" y="{y + 21}" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="#1e293b">Total (n)</text>')
    svg_parts.append(f'<text x="350" y="{y + 21}" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="middle">{tot}</text>')

    # Outer table border
    svg_parts.append(f'<rect x="25" y="{y_hdr}" width="{width - 50}" height="{y + row_height - y_hdr}" fill="none" stroke="#94a3b8" stroke-width="1.5" rx="4"/>')
    svg_parts.append("</svg>")
    return "\n".join(svg_parts)


def draw_frequency_table_svg(
    values: List[int],
    frequencies: List[int],
    val_label: str = "Score (x)",
    title: str = "Frequency Distribution Table",
    include_fx: bool = False,
    seed: Optional[int] = None,
) -> str:
    """Renders a standard frequency distribution table."""
    width = 440
    row_height = 30
    header_height = 42
    height = header_height + (len(values) + 2) * row_height + 40

    svg_parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="auto">',
        f"<!-- s:{seed} -->",
        '<rect width="100%" height="100%" fill="#f8fafc" rx="8"/>',
        f'<text x="{width / 2}" y="24" font-family="Arial, sans-serif" font-size="15" font-weight="bold" fill="#0f172a" text-anchor="middle">{title}</text>',
    ]

    y_hdr = 48
    svg_parts.append(f'<rect x="30" y="{y_hdr}" width="{width - 60}" height="{row_height}" fill="#e2e8f0" rx="4"/>')

    if include_fx:
        col_x = [60, 190, 310]
        svg_parts.append(f'<text x="{col_x[0]}" y="{y_hdr + 20}" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="#1e293b">{val_label}</text>')
        svg_parts.append(f'<text x="{col_x[1]}" y="{y_hdr + 20}" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="#1e293b" text-anchor="middle">Frequency (f)</text>')
        svg_parts.append(f'<text x="{col_x[2]}" y="{y_hdr + 20}" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="#1e293b" text-anchor="middle">f × x</text>')
    else:
        col_x = [90, 290]
        svg_parts.append(f'<text x="{col_x[0]}" y="{y_hdr + 20}" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="#1e293b">{val_label}</text>')
        svg_parts.append(f'<text x="{col_x[1]}" y="{y_hdr + 20}" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="#1e293b" text-anchor="middle">Frequency (f)</text>')

    y = y_hdr + row_height
    tot_f = sum(frequencies)
    tot_fx = sum(v * f for v, f in zip(values, frequencies))

    for idx, (v, f) in enumerate(zip(values, frequencies)):
        bg_fill = "#ffffff" if idx % 2 == 0 else "#f8fafc"
        svg_parts.append(f'<rect x="30" y="{y}" width="{width - 60}" height="{row_height}" fill="{bg_fill}"/>')
        svg_parts.append(f'<line x1="30" y1="{y + row_height}" x2="{width - 30}" y2="{y + row_height}" stroke="#e2e8f0" stroke-width="1"/>')
        if include_fx:
            svg_parts.append(f'<text x="{col_x[0]}" y="{y + 20}" font-family="Arial, sans-serif" font-size="13" fill="#0f172a">{v}</text>')
            svg_parts.append(f'<text x="{col_x[1]}" y="{y + 20}" font-family="Arial, sans-serif" font-size="13" fill="#0f172a" text-anchor="middle">{f}</text>')
            svg_parts.append(f'<text x="{col_x[2]}" y="{y + 20}" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="middle">{v * f}</text>')
        else:
            svg_parts.append(f'<text x="{col_x[0]}" y="{y + 20}" font-family="Arial, sans-serif" font-size="13" fill="#0f172a">{v}</text>')
            svg_parts.append(f'<text x="{col_x[1]}" y="{y + 20}" font-family="Arial, sans-serif" font-size="13" fill="#0f172a" text-anchor="middle">{f}</text>')
        y += row_height

    # Total row
    svg_parts.append(f'<rect x="30" y="{y}" width="{width - 60}" height="{row_height}" fill="#e2e8f0" rx="4"/>')
    if include_fx:
        svg_parts.append(f'<text x="{col_x[0]}" y="{y + 20}" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="#1e293b">Total</text>')
        svg_parts.append(f'<text x="{col_x[1]}" y="{y + 20}" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="middle">Σf = {tot_f}</text>')
        svg_parts.append(f'<text x="{col_x[2]}" y="{y + 20}" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="middle">Σ(f·x) = {tot_fx}</text>')
    else:
        svg_parts.append(f'<text x="{col_x[0]}" y="{y + 20}" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="#1e293b">Total</text>')
        svg_parts.append(f'<text x="{col_x[1]}" y="{y + 20}" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="middle">Σf = {tot_f}</text>')

    svg_parts.append(f'<rect x="30" y="{y_hdr}" width="{width - 60}" height="{y + row_height - y_hdr}" fill="none" stroke="#94a3b8" stroke-width="1.5" rx="4"/>')
    svg_parts.append("</svg>")
    return "\n".join(svg_parts)


def draw_dot_plot_svg(
    data_points: List[int],
    title: str = "Dot Plot",
    x_label: str = "Values",
    seed: Optional[int] = None,
) -> str:
    """Renders a dot plot on a horizontal axis."""
    width, height = 440, 240
    min_val = min(data_points)
    max_val = max(data_points)
    span = max(1, max_val - min_val)

    # Count frequency of each integer
    counts: Dict[int, int] = {}
    for pt in data_points:
        counts[pt] = counts.get(pt, 0) + 1

    x_left = 60
    x_right = 380
    axis_y = 175

    svg_parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="auto">',
        f"<!-- s:{seed} -->",
        '<rect width="100%" height="100%" fill="#f8fafc" rx="8"/>',
        f'<text x="{width / 2}" y="25" font-family="Arial, sans-serif" font-size="15" font-weight="bold" fill="#0f172a" text-anchor="middle">{title}</text>',
        f'<line x1="{x_left - 15}" y1="{axis_y}" x2="{x_right + 15}" y2="{axis_y}" stroke="#1e293b" stroke-width="2"/>',
    ]

    for val in range(min_val, max_val + 1):
        frac = (val - min_val) / span if span > 0 else 0.5
        cx = x_left + frac * (x_right - x_left)

        # Axis tick and label
        svg_parts.append(f'<line x1="{cx}" y1="{axis_y}" x2="{cx}" y2="{axis_y + 6}" stroke="#1e293b" stroke-width="1.8"/>')
        svg_parts.append(f'<text x="{cx}" y="{axis_y + 22}" font-family="Arial, sans-serif" font-size="12" font-weight="bold" fill="#1e293b" text-anchor="middle">{val}</text>')

        # Stacked dots
        freq = counts.get(val, 0)
        for d in range(freq):
            cy = axis_y - 12 - d * 16
            svg_parts.append(f'<circle cx="{cx}" cy="{cy}" r="5.5" fill="#3b82f6" stroke="#1d4ed8" stroke-width="1.5"/>')

    svg_parts.append(f'<text x="{width / 2}" y="{axis_y + 45}" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="#475569" text-anchor="middle">{x_label}</text>')
    svg_parts.append("</svg>")
    return "\n".join(svg_parts)


def draw_stem_and_leaf_svg(
    stems_dict: Dict[int, List[int]],
    title: str = "Stem-and-Leaf Display",
    key_example: str = "4 | 2 means 42",
    seed: Optional[int] = None,
) -> str:
    """Renders a stem-and-leaf plot with central vertical rule."""
    width = 380
    row_height = 26
    stems = sorted(stems_dict.keys())
    height = 50 + len(stems) * row_height + 55

    svg_parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="auto">',
        f"<!-- s:{seed} -->",
        '<rect width="100%" height="100%" fill="#f8fafc" rx="8"/>',
        f'<text x="{width / 2}" y="24" font-family="Arial, sans-serif" font-size="15" font-weight="bold" fill="#0f172a" text-anchor="middle">{title}</text>',
    ]

    stem_x = 110
    start_y = 55
    end_y = start_y + len(stems) * row_height + 5

    # Headers
    svg_parts.append(f'<text x="{stem_x - 18}" y="{start_y - 8}" font-family="Arial, sans-serif" font-size="12" font-weight="bold" fill="#475569" text-anchor="end">Stem</text>')
    svg_parts.append(f'<text x="{stem_x + 18}" y="{start_y - 8}" font-family="Arial, sans-serif" font-size="12" font-weight="bold" fill="#475569">Leaf</text>')

    # Vertical bar
    svg_parts.append(f'<line x1="{stem_x}" y1="{start_y - 20}" x2="{stem_x}" y2="{end_y}" stroke="#334155" stroke-width="2.5"/>')

    # Rows
    y = start_y + 16
    for stem in stems:
        leaves = sorted(stems_dict[stem])
        leaves_str = "  ".join(str(lf) for lf in leaves)
        svg_parts.append(f'<text x="{stem_x - 15}" y="{y}" font-family="Courier New, monospace" font-size="15" font-weight="bold" fill="#0f172a" text-anchor="end">{stem}</text>')
        svg_parts.append(f'<text x="{stem_x + 18}" y="{y}" font-family="Courier New, monospace" font-size="15" fill="#2563eb">{leaves_str}</text>')
        y += row_height

    # Key / Legend
    svg_parts.append(f'<rect x="40" y="{y + 6}" width="{width - 80}" height="26" fill="#e0f2fe" rx="4"/>')
    svg_parts.append(f'<text x="{width / 2}" y="{y + 23}" font-family="Arial, sans-serif" font-size="12" font-weight="bold" fill="#0369a1" text-anchor="middle">Key: {key_example}</text>')

    svg_parts.append("</svg>")
    return "\n".join(svg_parts)
