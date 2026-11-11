"""Grade 9 Mathematics - Algebraic Expressions SVG Helpers.
Generates deterministic, accessible SVG figures for flow diagrams and geometric representations of algebraic expressions.
All helpers accept `seed: Optional[int] = None, **kwargs: Any` and inject entropy comments to vary across seeds.
"""
from __future__ import annotations

from typing import Any, List, Optional


def draw_algebraic_flow_diagram_svg(
    operations: List[str],
    input_label: str = "x",
    output_label: str = "Output",
    seed: Optional[int] = None,
    **kwargs: Any,
) -> str:
    """Renders a clean horizontal flow diagram showing sequential algebraic operations."""
    entropy = f"<!-- s:{seed} -->\n" if seed is not None else ""
    num_ops = len(operations)
    box_w, box_h = 100, 50
    spacing = 70
    start_x = 70
    total_w = start_x + num_ops * (box_w + spacing) + 80
    total_h = 130
    mid_y = 65

    elements = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {total_w} {total_h}" width="100%" height="auto" class="rounded-lg bg-slate-900 border border-slate-700/60 p-2">',
        entropy,
        '<defs>',
        '  <marker id="arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">',
        '    <path d="M 0 1 L 10 5 L 0 9 z" fill="#38bdf8"/>',
        '  </marker>',
        '</defs>',
        # Input label
        f'<text x="{start_x - 35}" y="{mid_y + 6}" font-size="16" font-weight="700" fill="#f8fafc" text-anchor="middle">{input_label}</text>',
        f'<line x1="{start_x - 20}" y1="{mid_y}" x2="{start_x}" y2="{mid_y}" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#arrow)"/>',
    ]

    curr_x = start_x
    for i, op in enumerate(operations):
        # Operation box
        elements.append(
            f'<rect x="{curr_x}" y="{mid_y - box_h // 2}" width="{box_w}" height="{box_h}" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>'
        )
        elements.append(
            f'<text x="{curr_x + box_w // 2}" y="{mid_y + 6}" font-size="15" font-weight="700" fill="#38bdf8" text-anchor="middle">{op}</text>'
        )

        next_x = curr_x + box_w
        if i < num_ops - 1:
            elements.append(
                f'<line x1="{next_x}" y1="{mid_y}" x2="{next_x + spacing}" y2="{mid_y}" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#arrow)"/>'
            )
            curr_x = next_x + spacing
        else:
            # Final arrow to output
            elements.append(
                f'<line x1="{next_x}" y1="{mid_y}" x2="{next_x + 50}" y2="{mid_y}" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#arrow)"/>'
            )
            elements.append(
                f'<text x="{next_x + 65}" y="{mid_y + 6}" font-size="15" font-weight="700" fill="#facc15" text-anchor="start">{output_label}</text>'
            )

    elements.append('</svg>')
    return "\n".join(elements)


def draw_algebraic_rectangle_svg(
    length_label: str,
    width_label: str,
    seed: Optional[int] = None,
    **kwargs: Any,
) -> str:
    """Renders a 2D geometric rectangle with algebraic expressions for length and breadth."""
    entropy = f"<!-- s:{seed} -->\n" if seed is not None else ""
    x, y, w, h = 100, 50, 320, 180
    total_w, total_h = 520, 270

    elements = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {total_w} {total_h}" width="100%" height="auto" class="rounded-lg bg-slate-900 border border-slate-700/60 p-2">',
        entropy,
        # Rectangle
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="4" fill="#0f172a" stroke="#818cf8" stroke-width="2.5"/>',
        # Right angle marker at bottom-left
        f'<path d="M {x} {y + h - 16} L {x + 16} {y + h - 16} L {x + 16} {y + h}" fill="none" stroke="#94a3b8" stroke-width="1.5"/>',
        # Top Length Label
        f'<text x="{x + w // 2}" y="{y - 14}" font-size="16" font-weight="700" fill="#38bdf8" text-anchor="middle">{length_label}</text>',
        # Left Width Label
        f'<text x="{x - 16}" y="{y + h // 2 + 5}" font-size="16" font-weight="700" fill="#facc15" text-anchor="end">{width_label}</text>',
        '</svg>',
    ]
    return "\n".join(elements)


def draw_algebraic_triangle_svg(
    side_a: str,
    side_b: str,
    side_c: str,
    seed: Optional[int] = None,
    **kwargs: Any,
) -> str:
    """Renders a triangle with algebraic expressions labeling its three sides."""
    entropy = f"<!-- s:{seed} -->\n" if seed is not None else ""
    p1 = (250, 40)
    p2 = (80, 230)
    p3 = (420, 230)
    total_w, total_h = 500, 270

    elements = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {total_w} {total_h}" width="100%" height="auto" class="rounded-lg bg-slate-900 border border-slate-700/60 p-2">',
        entropy,
        # Triangle polygon
        f'<polygon points="{p1[0]},{p1[1]} {p2[0]},{p2[1]} {p3[0]},{p3[1]}" fill="#0f172a" stroke="#34d399" stroke-width="2.5"/>',
        # Left side label (p1 to p2)
        f'<text x="{(p1[0] + p2[0]) // 2 - 20}" y="{(p1[1] + p2[1]) // 2}" font-size="15" font-weight="700" fill="#38bdf8" text-anchor="end">{side_a}</text>',
        # Right side label (p1 to p3)
        f'<text x="{(p1[0] + p3[0]) // 2 + 20}" y="{(p1[1] + p3[1]) // 2}" font-size="15" font-weight="700" fill="#facc15" text-anchor="start">{side_b}</text>',
        # Bottom side label (p2 to p3)
        f'<text x="{(p2[0] + p3[0]) // 2}" y="{p2[1] + 25}" font-size="15" font-weight="700" fill="#fb923c" text-anchor="middle">{side_c}</text>',
        '</svg>',
    ]
    return "\n".join(elements)
