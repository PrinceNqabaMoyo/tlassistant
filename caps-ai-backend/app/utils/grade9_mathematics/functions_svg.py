"""
Grade 9 Mathematics - Functions and Relationships SVG Diagram Builders
======================================================================
Provides clean, authentic SVG visual representations for:
  - 2-step algebraic flow diagrams (boxes with operator bubbles and arrows)
  - Function input/output tables with styled headers
  - Linear rate context visualisations (tanks, taxi rates, graphs)
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


def draw_function_flow_diagram_svg(
    op1_str: str,
    op2_str: str,
    input_str: str = "x",
    output_str: str = "y",
    seed: Optional[int] = None,
    **kwargs: Any,
) -> str:
    """Renders a 2-stage algebraic flow diagram with clean geometric blocks."""
    entropy_comment = f"<!-- s:{seed} -->\n" if seed is not None else ""

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 560 140" width="100%" height="140" class="rounded-xl border border-slate-700 bg-slate-900/60 p-2">
{entropy_comment}<defs>
  <marker id="arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
    <path d="M 0 1 L 8 5 L 0 9 z" fill="#38bdf8" />
  </marker>
</defs>

<!-- Input Node -->
<rect x="20" y="45" width="70" height="50" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
<text x="55" y="75" fill="#f8fafc" font-size="16" font-weight="bold" font-family="monospace" text-anchor="middle">{input_str}</text>
<text x="55" y="32" fill="#94a3b8" font-size="11" font-family="sans-serif" text-anchor="middle">Input (x)</text>

<!-- Arrow 1 -->
<line x1="90" y1="70" x2="140" y2="70" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#arrow)" />

<!-- Operator 1 Node -->
<circle cx="185" cy="70" r="38" fill="#0f172a" stroke="#818cf8" stroke-width="2.5"/>
<text x="185" y="76" fill="#c7d2fe" font-size="15" font-weight="bold" font-family="monospace" text-anchor="middle">{op1_str}</text>
<text x="185" y="24" fill="#a5b4fc" font-size="11" font-family="sans-serif" text-anchor="middle">Step 1</text>

<!-- Arrow 2 -->
<line x1="225" y1="70" x2="275" y2="70" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#arrow)" />

<!-- Operator 2 Node -->
<circle cx="320" cy="70" r="38" fill="#0f172a" stroke="#ec4899" stroke-width="2.5"/>
<text x="320" y="76" fill="#fbcfe8" font-size="15" font-weight="bold" font-family="monospace" text-anchor="middle">{op2_str}</text>
<text x="320" y="24" fill="#f472b6" font-size="11" font-family="sans-serif" text-anchor="middle">Step 2</text>

<!-- Arrow 3 -->
<line x1="360" y1="70" x2="415" y2="70" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#arrow)" />

<!-- Output Node -->
<rect x="425" y="45" width="85" height="50" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="2"/>
<text x="467" y="75" fill="#f8fafc" font-size="16" font-weight="bold" font-family="monospace" text-anchor="middle">{output_str}</text>
<text x="467" y="32" fill="#86efac" font-size="11" font-family="sans-serif" text-anchor="middle">Output (y)</text>
</svg>"""
    return svg


def draw_function_table_svg(
    x_values: List[Any],
    y_values: List[Any],
    rule_label: str = "y = mx + c",
    seed: Optional[int] = None,
    **kwargs: Any,
) -> str:
    """Renders a tabular input/output representation with styled cells."""
    entropy_comment = f"<!-- s:{seed} -->\n" if seed is not None else ""

    col_count = len(x_values)
    cell_w = min(56, 420 // max(col_count, 1))
    header_w = 90
    total_w = header_w + col_count * cell_w + 30

    cells_x = []
    cells_y = []

    for i in range(col_count):
        cx = header_w + i * cell_w
        x_val = str(x_values[i])
        y_val = str(y_values[i])
        
        # cell background & text
        cells_x.append(
            f'<rect x="{cx}" y="45" width="{cell_w-2}" height="32" fill="#1e293b" stroke="#475569" stroke-width="1" rx="4"/>'
            f'<text x="{cx + cell_w//2 - 1}" y="66" fill="#f8fafc" font-size="13" font-family="monospace" text-anchor="middle">{x_val}</text>'
        )
        cells_y.append(
            f'<rect x="{cx}" y="82" width="{cell_w-2}" height="32" fill="#0f172a" stroke="#475569" stroke-width="1" rx="4"/>'
            f'<text x="{cx + cell_w//2 - 1}" y="103" fill="#38bdf8" font-size="13" font-family="monospace" text-anchor="middle">{y_val}</text>'
        )

    cells_x_str = "\n".join(cells_x)
    cells_y_str = "\n".join(cells_y)

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {total_w} 140" width="100%" height="140" class="rounded-xl border border-slate-700 bg-slate-900/60 p-2">
{entropy_comment}<!-- Title / Rule badge -->
<text x="15" y="25" fill="#94a3b8" font-size="12" font-family="sans-serif">Function Rule: <tspan fill="#38bdf8" font-weight="bold">{rule_label}</tspan></text>

<!-- Row Labels -->
<rect x="15" y="45" width="{header_w - 20}" height="32" fill="#334155" rx="4"/>
<text x="{15 + (header_w - 20)//2}" y="66" fill="#e2e8f0" font-size="13" font-weight="bold" font-family="sans-serif" text-anchor="middle">Input (x)</text>

<rect x="15" y="82" width="{header_w - 20}" height="32" fill="#1e293b" rx="4"/>
<text x="{15 + (header_w - 20)//2}" y="103" fill="#a5f3fc" font-size="13" font-weight="bold" font-family="sans-serif" text-anchor="middle">Output (y)</text>

<!-- Columns -->
{cells_x_str}
{cells_y_str}
</svg>"""
    return svg


def draw_rate_context_graph_svg(
    initial_val: float,
    rate: float,
    max_x: int = 10,
    x_label: str = "Hours (t)",
    y_label: str = "Volume (L)",
    context_title: str = "Water Tank Level",
    seed: Optional[int] = None,
    **kwargs: Any,
) -> str:
    """Renders a simple Cartesian first-quadrant graph representing a linear rate context."""
    entropy_comment = f"<!-- s:{seed} -->\n" if seed is not None else ""

    # SVG canvas coordinates: plot area (60, 30) to (360, 150)
    ox, oy = 60, 150
    pw, ph = 300, 110
    
    y0 = initial_val
    y_end = initial_val + rate * max_x
    max_y = max(y0, y_end, 1) * 1.15

    def to_svg(x: float, y: float):
        sx = ox + (x / max_x) * pw
        sy = oy - (y / max_y) * ph
        return sx, sy

    x1, y1 = to_svg(0, y0)
    x2, y2 = to_svg(max_x, y_end)

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 420 180" width="100%" height="180" class="rounded-xl border border-slate-700 bg-slate-900/60 p-2">
{entropy_comment}<!-- Title -->
<text x="210" y="20" fill="#f8fafc" font-size="13" font-weight="bold" font-family="sans-serif" text-anchor="middle">{context_title}</text>

<!-- Grid Axes -->
<line x1="{ox}" y1="{oy}" x2="{ox + pw}" y2="{oy}" stroke="#64748b" stroke-width="2"/>
<line x1="{ox}" y1="{oy}" x2="{ox}" y2="{oy - ph}" stroke="#64748b" stroke-width="2"/>

<!-- Axis Labels -->
<text x="{ox + pw // 2}" y="{oy + 24}" fill="#94a3b8" font-size="11" font-family="sans-serif" text-anchor="middle">{x_label}</text>
<text x="{ox - 10}" y="{oy - ph // 2}" fill="#94a3b8" font-size="11" font-family="sans-serif" text-anchor="end">{y_label}</text>

<!-- Initial and End Tick values -->
<text x="{ox - 8}" y="{y1 + 4}" fill="#38bdf8" font-size="10" font-family="monospace" text-anchor="end">{int(y0)}</text>
<text x="{ox + pw}" y="{oy + 15}" fill="#94a3b8" font-size="10" font-family="monospace" text-anchor="middle">{max_x}</text>

<!-- Function Line -->
<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#38bdf8" stroke-width="3" stroke-linecap="round"/>
<circle cx="{x1}" cy="{y1}" r="4" fill="#38bdf8"/>
<circle cx="{x2}" cy="{y2}" r="4" fill="#38bdf8"/>
</svg>"""
    return svg
