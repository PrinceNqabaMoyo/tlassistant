"""Grade 9 Mathematics - Probability SVG Builders (CAPS Term 4).
Generates deterministic SVG figures for circular probability spinners,
tree diagrams, and Venn diagrams.
Zero LLM calls, deterministic seed entropy.
"""
from __future__ import annotations

import math
from typing import Any, Dict, List, Optional, Tuple


def draw_probability_spinner_svg(
    labels: List[str],
    weights: List[int],
    colors: Optional[List[str]] = None,
    title: str = "Probability Spinner",
    seed: Optional[int] = None,
    size: int = 360,
) -> str:
    s_tag = f"<!-- s:{seed} -->\n" if seed is not None else ""
    cx, cy = size / 2.0, size / 2.0
    r = (size / 2.0) - 40.0
    total_w = sum(weights) if sum(weights) > 0 else 1

    default_colors = ["#ef4444", "#3b82f6", "#10b981", "#f59e0b", "#8b5cf6", "#ec4899", "#06b6d4"]
    palette = colors or default_colors

    svg_lines = [
        f'{s_tag}<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {size} {size}" '
        f'width="{size}" height="{size}" style="background:#ffffff; font-family:system-ui,-apple-system,sans-serif;">',
        f'  <rect x="0" y="0" width="{size}" height="{size}" fill="#ffffff"/>',
        f'  <text x="{cx}" y="24" font-size="14" font-weight="bold" text-anchor="middle" fill="#0f172a">{title}</text>',
    ]

    current_angle = -90.0  # Start at 12 o'clock
    for i, (label, w) in enumerate(zip(labels, weights)):
        sweep = (w / total_w) * 360.0
        start_rad = math.radians(current_angle)
        end_rad = math.radians(current_angle + sweep)

        x1 = cx + r * math.cos(start_rad)
        y1 = cy + r * math.sin(start_rad)
        x2 = cx + r * math.cos(end_rad)
        y2 = cy + r * math.sin(end_rad)

        large_arc = 1 if sweep > 180.0 else 0
        fill_col = palette[i % len(palette)]

        # Path wedge
        path_d = f"M {cx:.1f} {cy:.1f} L {x1:.1f} {y1:.1f} A {r:.1f} {r:.1f} 0 {large_arc} 1 {x2:.1f} {y2:.1f} Z"
        svg_lines.append(f'  <path d="{path_d}" fill="{fill_col}" stroke="#334155" stroke-width="1.5" opacity="0.85"/>')

        # Label position
        mid_rad = math.radians(current_angle + sweep / 2.0)
        lx = cx + (r * 0.65) * math.cos(mid_rad)
        ly = cy + (r * 0.65) * math.sin(mid_rad) + 4
        svg_lines.append(f'  <text x="{lx:.1f}" y="{ly:.1f}" font-size="12" font-weight="bold" text-anchor="middle" fill="#ffffff">{label}</text>')

        current_angle += sweep

    # Center pin and pointer arrow
    svg_lines.append(f'  <circle cx="{cx}" cy="{cy}" r="8" fill="#1e293b"/>')
    svg_lines.append(f'  <line x1="{cx}" y1="{cy}" x2="{cx}" y2="{cy - r + 15}" stroke="#0f172a" stroke-width="3" stroke-linecap="round"/>')
    svg_lines.append(f'  <polygon points="{cx},{cy - r + 5} {cx - 6},{cy - r + 20} {cx + 6},{cy - r + 20}" fill="#0f172a"/>')
    svg_lines.append('</svg>')
    return "\n".join(svg_lines)


def draw_two_stage_tree_diagram_svg(
    stage1_labels: List[str],
    stage1_probs: List[str],
    stage2_labels: List[List[str]],
    stage2_probs: List[List[str]],
    title: str = "Tree Diagram",
    seed: Optional[int] = None,
    width: int = 500,
    height: int = 340,
) -> str:
    s_tag = f"<!-- s:{seed} -->\n" if seed is not None else ""
    svg_lines = [
        f'{s_tag}<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
        f'width="{width}" height="{height}" style="background:#ffffff; font-family:system-ui,-apple-system,sans-serif;">',
        f'  <rect x="0" y="0" width="{width}" height="{height}" fill="#ffffff"/>',
        f'  <text x="{width/2}" y="24" font-size="14" font-weight="bold" text-anchor="middle" fill="#0f172a">{title}</text>',
    ]

    root_x, root_y = 50.0, height / 2.0
    n1 = len(stage1_labels)
    s1_x = 200.0
    s2_x = 380.0

    y_spacing1 = (height - 80) / n1
    for i, (l1, p1) in enumerate(zip(stage1_labels, stage1_probs)):
        node1_y = 50 + (i + 0.5) * y_spacing1

        # Root to stage 1 branch
        svg_lines.append(f'  <line x1="{root_x}" y1="{root_y}" x2="{s1_x}" y2="{node1_y}" stroke="#475569" stroke-width="2"/>')
        mid1_x = (root_x + s1_x) / 2
        mid1_y = (root_y + node1_y) / 2 - 8
        svg_lines.append(f'  <text x="{mid1_x}" y="{mid1_y}" font-size="11" font-weight="bold" fill="#0284c7" text-anchor="middle">{p1}</text>')
        svg_lines.append(f'  <circle cx="{s1_x}" cy="{node1_y}" r="14" fill="#e0f2fe" stroke="#0284c7" stroke-width="1.5"/>')
        svg_lines.append(f'  <text x="{s1_x}" y="{node1_y + 4}" font-size="11" font-weight="bold" fill="#0369a1" text-anchor="middle">{l1}</text>')

        # Stage 1 to stage 2 branches
        sub_labels = stage2_labels[i]
        sub_probs = stage2_probs[i]
        n2 = len(sub_labels)
        y_spacing2 = y_spacing1 / n2
        for j, (l2, p2) in enumerate(zip(sub_labels, sub_probs)):
            node2_y = (50 + i * y_spacing1) + (j + 0.5) * y_spacing2
            svg_lines.append(f'  <line x1="{s1_x + 14}" y1="{node1_y}" x2="{s2_x}" y2="{node2_y}" stroke="#64748b" stroke-width="1.5"/>')
            mid2_x = (s1_x + s2_x) / 2
            mid2_y = (node1_y + node2_y) / 2 - 6
            svg_lines.append(f'  <text x="{mid2_x}" y="{mid2_y}" font-size="10" fill="#059669" text-anchor="middle">{p2}</text>')
            svg_lines.append(f'  <circle cx="{s2_x}" cy="{node2_y}" r="12" fill="#d1fae5" stroke="#059669" stroke-width="1.5"/>')
            svg_lines.append(f'  <text x="{s2_x}" y="{node2_y + 4}" font-size="10" font-weight="bold" fill="#047857" text-anchor="middle">{l2}</text>')
            # Outcome label at end
            svg_lines.append(f'  <text x="{s2_x + 22}" y="{node2_y + 4}" font-size="11" fill="#334155">({l1}, {l2})</text>')

    svg_lines.append('</svg>')
    return "\n".join(svg_lines)
