"""Grade 9 Mathematics - Exponents SVG Diagrams.
Publication-grade SVG renderers for exponential branching trees,
scientific notation order of magnitude scale comparisons, and exponential curve points.
"""
from __future__ import annotations

from typing import Any, List, Optional, Tuple


def draw_power_growth_tree_svg(
    base: int = 2,
    levels: int = 3,
    seed: Optional[int] = None,
    **kwargs: Any,
) -> str:
    """Draws an exponential branching tree representing powers of a base (e.g. 2^0, 2^1, 2^2, 2^3)."""
    entropy_comment = f"<!-- s:{seed} -->\n" if seed is not None else ""
    width = 460
    height = 240

    lines_svg = []
    nodes_svg = []

    level_y = [35, 95, 155, 215][: levels + 1]

    node_coords: List[List[Tuple[float, float]]] = []

    for lvl in range(len(level_y)):
        y = level_y[lvl]
        num_nodes = base**lvl
        coords = []
        seg_w = width / (num_nodes + 1)
        for i in range(num_nodes):
            x = seg_w * (i + 1)
            coords.append((x, y))
        node_coords.append(coords)

    # Draw lines connecting parents to children
    for lvl in range(len(node_coords) - 1):
        parents = node_coords[lvl]
        children = node_coords[lvl + 1]
        for p_idx, (px, py) in enumerate(parents):
            for c_offset in range(base):
                c_idx = p_idx * base + c_offset
                if c_idx < len(children):
                    cx, cy = children[c_idx]
                    lines_svg.append(
                        f'<line x1="{px:.1f}" y1="{py}" x2="{cx:.1f}" y2="{cy}" stroke="#64748B" stroke-width="1.5"/>'
                    )

    # Draw nodes
    colors = ["#2563EB", "#7C3AED", "#DB2777", "#D97706"]
    for lvl, coords in enumerate(node_coords):
        col = colors[lvl % len(colors)]
        r = 13 if lvl < 2 else 9
        for x, y in coords:
            nodes_svg.append(
                f'<circle cx="{x:.1f}" cy="{y}" r="{r}" fill="{col}" stroke="#FFFFFF" stroke-width="2"/>'
            )
        # Label each level
        pow_val = base**lvl
        nodes_svg.append(
            f'<text x="25" y="{y + 4}" font-size="12" font-weight="bold" font-family="sans-serif" fill="#1E293B">'
            f'{base}^{lvl} = {pow_val}</text>'
        )

    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
        f'width="{width}" height="{height}" class="mx-auto block" style="background:#F8FAFC;border-radius:8px;">\n'
        f"{entropy_comment}"
        f'  <g id="power_growth_tree">\n'
        f"    {''.join(lines_svg)}\n"
        f"    {''.join(nodes_svg)}\n"
        f'  </g>\n'
        f'</svg>'
    )


def draw_scientific_scale_comparison_svg(
    items: List[Tuple[str, str, int]],
    seed: Optional[int] = None,
    **kwargs: Any,
) -> str:
    """Draws an orders-of-magnitude scale comparing powers of 10.
    items: List of (name, value_str, power_of_10)
    """
    entropy_comment = f"<!-- s:{seed} -->\n" if seed is not None else ""
    width = 520
    height = 140
    axis_y = 65
    pad_x = 40
    line_w = width - 2 * pad_x

    powers = [item[2] for item in items]
    min_p = min(powers) - 1
    max_p = max(powers) + 1
    span = max_p - min_p
    if span <= 0:
        span = 1

    ticks_svg = []
    for p in range(min_p, max_p + 1):
        pos = (p - min_p) / span
        x = pad_x + pos * line_w
        ticks_svg.append(
            f'<line x1="{x:.1f}" y1="{axis_y - 6}" x2="{x:.1f}" y2="{axis_y + 6}" stroke="#475569" stroke-width="2"/>'
            f'<text x="{x:.1f}" y="{axis_y + 22}" text-anchor="middle" font-size="11" font-family="sans-serif" fill="#334155">10^{p}</text>'
        )

    points_svg = []
    colors = ["#2563EB", "#DC2626", "#059669", "#D97706"]
    for idx, (name, val_str, p) in enumerate(items):
        pos = (p - min_p) / span
        px = pad_x + pos * line_w
        col = colors[idx % len(colors)]
        points_svg.append(
            f'<circle cx="{px:.1f}" cy="{axis_y}" r="6" fill="{col}" stroke="#FFFFFF" stroke-width="2"/>'
            f'<line x1="{px:.1f}" y1="{axis_y - 6}" x2="{px:.1f}" y2="{axis_y - 25}" stroke="{col}" stroke-width="1.5" stroke-dasharray="2,2"/>'
            f'<text x="{px:.1f}" y="{axis_y - 30}" text-anchor="middle" font-size="11" font-weight="bold" font-family="sans-serif" fill="{col}">{name}</text>'
        )

    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
        f'width="{width}" height="{height}" class="mx-auto block" style="background:#F8FAFC;border-radius:8px;">\n'
        f"{entropy_comment}"
        f'  <defs>\n'
        f'    <marker id="scale_arr" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">\n'
        f'      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#334155"/>\n'
        f'    </marker>\n'
        f'  </defs>\n'
        f'  <line x1="{pad_x - 10}" y1="{axis_y}" x2="{width - pad_x + 10}" y2="{axis_y}" stroke="#334155" stroke-width="2.5" marker-start="url(#scale_arr)" marker-end="url(#scale_arr)"/>\n'
        f"  {''.join(ticks_svg)}\n"
        f"  {''.join(points_svg)}\n"
        f'</svg>'
    )
