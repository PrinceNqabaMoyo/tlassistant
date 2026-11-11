"""Grade 9 Mathematics - Graphs & Linear Functions SVG Diagram Builders
======================================================================
Provides clean, authentic SVG visual representations for:
  - Cartesian coordinate planes with grid, axes, ticks, and plotted lines
  - Dual-intercept illustrations highlighting (x_int, 0) and (0, y_int)
  - Slope triangles showing rise (dy) and run (dx) on Cartesian grids
  - Intersecting lines with perpendicular or parallel annotations
  - Rate of change contextual graphs (water tanks, distance-time, tariffs, break-even)
"""
from __future__ import annotations

import math
from typing import Any, Dict, List, Optional, Tuple


def draw_cartesian_plane_svg(
    lines: Optional[List[Dict[str, Any]]] = None,
    points: Optional[List[Dict[str, Any]]] = None,
    slope_triangles: Optional[List[Dict[str, Any]]] = None,
    x_range: Tuple[float, float] = (-6, 6),
    y_range: Tuple[float, float] = (-6, 6),
    title: Optional[str] = None,
    width: int = 500,
    height: int = 400,
    seed: Optional[int] = None,
    **kwargs: Any,
) -> str:
    """Renders a fully-featured Cartesian coordinate plane with plotted lines,
    points, and optional slope triangles.
    """
    entropy_comment = f"<!-- s:{seed} -->\n" if seed is not None else ""

    x_min, x_max = x_range
    y_min, y_max = y_range

    pad_left = 48
    pad_right = 32
    pad_top = 36 if title else 24
    pad_bottom = 36

    pw = width - pad_left - pad_right
    ph = height - pad_top - pad_bottom

    def to_svg(x: float, y: float) -> Tuple[float, float]:
        sx = pad_left + ((x - x_min) / (x_max - x_min)) * pw
        sy = pad_top + ((y_max - y) / (y_max - y_min)) * ph
        return sx, sy

    # Origin coordinates in SVG space
    ox, oy = to_svg(0, 0)
    # Clamp axis visual lines if origin is outside range
    ox_clamped = max(pad_left, min(pad_left + pw, ox))
    oy_clamped = max(pad_top, min(pad_top + ph, oy))

    grid_elements: List[str] = []

    # Grid step: integer steps if range <= 16, else 2 or 5
    span_x = x_max - x_min
    span_y = y_max - y_min
    step_x = 1 if span_x <= 16 else (2 if span_x <= 30 else 5)
    step_y = 1 if span_y <= 16 else (2 if span_y <= 30 else 5)

    # Vertical grid lines & X-ticks
    curr_x = math.ceil(x_min / step_x) * step_x
    while curr_x <= x_max:
        sx, _ = to_svg(curr_x, 0)
        # Grid line
        grid_elements.append(
            f'<line x1="{sx:.1f}" y1="{pad_top}" x2="{sx:.1f}" y2="{pad_top + ph}" stroke="#334155" stroke-width="0.8" stroke-dasharray="2,2"/>'
        )
        # Tick and label on X axis
        if curr_x != 0 and (pad_top <= oy <= pad_top + ph):
            grid_elements.append(
                f'<line x1="{sx:.1f}" y1="{oy - 4:.1f}" x2="{sx:.1f}" y2="{oy + 4:.1f}" stroke="#64748b" stroke-width="1.2"/>'
            )
            grid_elements.append(
                f'<text x="{sx:.1f}" y="{oy + 16:.1f}" fill="#94a3b8" font-size="10" font-family="monospace" text-anchor="middle">{int(curr_x) if curr_x == int(curr_x) else curr_x}</text>'
            )
        curr_x += step_x

    # Horizontal grid lines & Y-ticks
    curr_y = math.ceil(y_min / step_y) * step_y
    while curr_y <= y_max:
        _, sy = to_svg(0, curr_y)
        # Grid line
        grid_elements.append(
            f'<line x1="{pad_left}" y1="{sy:.1f}" x2="{pad_left + pw}" y2="{sy:.1f}" stroke="#334155" stroke-width="0.8" stroke-dasharray="2,2"/>'
        )
        # Tick and label on Y axis
        if curr_y != 0 and (pad_left <= ox <= pad_left + pw):
            grid_elements.append(
                f'<line x1="{ox - 4:.1f}" y1="{sy:.1f}" x2="{ox + 4:.1f}" y2="{sy:.1f}" stroke="#64748b" stroke-width="1.2"/>'
            )
            grid_elements.append(
                f'<text x="{ox - 7:.1f}" y="{sy + 3:.1f}" fill="#94a3b8" font-size="10" font-family="monospace" text-anchor="end">{int(curr_y) if curr_y == int(curr_y) else curr_y}</text>'
            )
        curr_y += step_y

    # Main Axes
    axis_elements: List[str] = []
    # X-axis
    if pad_top <= oy <= pad_top + ph:
        axis_elements.append(
            f'<line x1="{pad_left - 8}" y1="{oy:.1f}" x2="{pad_left + pw + 12}" y2="{oy:.1f}" stroke="#94a3b8" stroke-width="1.8" marker-end="url(#arrow-head)" />'
        )
        axis_elements.append(
            f'<text x="{pad_left + pw + 20}" y="{oy + 4:.1f}" fill="#f8fafc" font-size="12" font-weight="bold" font-family="sans-serif">x</text>'
        )
    # Y-axis
    if pad_left <= ox <= pad_left + pw:
        axis_elements.append(
            f'<line x1="{ox:.1f}" y1="{pad_top + ph + 8}" x2="{ox:.1f}" y2="{pad_top - 12}" stroke="#94a3b8" stroke-width="1.8" marker-end="url(#arrow-head)" />'
        )
        axis_elements.append(
            f'<text x="{ox:.1f}" y="{pad_top - 18}" fill="#f8fafc" font-size="12" font-weight="bold" font-family="sans-serif" text-anchor="middle">y</text>'
        )

    # Origin 0 label
    if pad_left <= ox <= pad_left + pw and pad_top <= oy <= pad_top + ph:
        axis_elements.append(
            f'<text x="{ox - 6:.1f}" y="{oy + 14:.1f}" fill="#94a3b8" font-size="10" font-family="monospace" text-anchor="end">0</text>'
        )

    # Slope Triangles
    triangle_elements: List[str] = []
    if slope_triangles:
        for st in slope_triangles:
            x1, y1 = st["x1"], st["y1"]
            x2, y2 = st["x2"], st["y2"]
            sx1, sy1 = to_svg(x1, y1)
            sx2, sy2 = to_svg(x2, y2)
            corner_sx, corner_sy = to_svg(x2, y1)
            color = st.get("color", "#f59e0b")
            fill_op = st.get("fill_opacity", 0.18)

            triangle_elements.append(
                f'<polygon points="{sx1:.1f},{sy1:.1f} {corner_sx:.1f},{corner_sy:.1f} {sx2:.1f},{sy2:.1f}" fill="{color}" fill-opacity="{fill_op}" stroke="{color}" stroke-width="1.5" stroke-dasharray="3,3"/>'
            )
            # Labels for rise and run
            run_label = st.get("run_label", f"run = {abs(x2 - x1)}")
            rise_label = st.get("rise_label", f"rise = {abs(y2 - y1)}")
            mid_run_x = (sx1 + corner_sx) / 2
            mid_rise_y = (corner_sy + sy2) / 2

            triangle_elements.append(
                f'<rect x="{mid_run_x - 30:.1f}" y="{corner_sy + 4:.1f}" width="60" height="16" rx="3" fill="#0f172a" fill-opacity="0.85"/>'
                f'<text x="{mid_run_x:.1f}" y="{corner_sy + 16:.1f}" fill="{color}" font-size="10" font-weight="bold" font-family="monospace" text-anchor="middle">{run_label}</text>'
            )
            triangle_elements.append(
                f'<rect x="{corner_sx + 4:.1f}" y="{mid_rise_y - 8:.1f}" width="60" height="16" rx="3" fill="#0f172a" fill-opacity="0.85"/>'
                f'<text x="{corner_sx + 34:.1f}" y="{mid_rise_y + 4:.1f}" fill="{color}" font-size="10" font-weight="bold" font-family="monospace" text-anchor="middle">{rise_label}</text>'
            )

    # Plotted Lines
    line_elements: List[str] = []
    if lines:
        for idx, l in enumerate(lines):
            color = l.get("color", "#38bdf8" if idx == 0 else "#f43f5e")
            stroke_w = l.get("stroke_width", 2.5)
            dashed = 'stroke-dasharray="4,4"' if l.get("dashed") else ""

            if l.get("is_vertical"):
                x_val = float(l.get("x_val", 0))
                lx1, ly1 = to_svg(x_val, y_min)
                lx2, ly2 = to_svg(x_val, y_max)
            elif l.get("is_horizontal"):
                y_val = float(l.get("y_val", 0))
                lx1, ly1 = to_svg(x_min, y_val)
                lx2, ly2 = to_svg(x_max, y_val)
            elif "m" in l and "c" in l:
                m = float(l["m"])
                c = float(l["c"])
                # Compute intersection with boundaries [x_min, x_max] and [y_min, y_max]
                pts = []
                # At x = x_min
                y_at_xmin = m * x_min + c
                if y_min <= y_at_xmin <= y_max:
                    pts.append((x_min, y_at_xmin))
                # At x = x_max
                y_at_xmax = m * x_max + c
                if y_min <= y_at_xmax <= y_max:
                    pts.append((x_max, y_at_xmax))
                # At y = y_min (if m != 0)
                if abs(m) > 1e-7:
                    x_at_ymin = (y_min - c) / m
                    if x_min <= x_at_ymin <= x_max and (x_at_ymin, y_min) not in pts:
                        pts.append((x_at_ymin, y_min))
                    x_at_ymax = (y_max - c) / m
                    if x_min <= x_at_ymax <= x_max and (x_at_ymax, y_max) not in pts:
                        pts.append((x_at_ymax, y_max))

                if len(pts) >= 2:
                    p_start = min(pts, key=lambda p: p[0])
                    p_end = max(pts, key=lambda p: p[0])
                    lx1, ly1 = to_svg(p_start[0], p_start[1])
                    lx2, ly2 = to_svg(p_end[0], p_end[1])
                else:
                    lx1, ly1 = to_svg(x_min, m * x_min + c)
                    lx2, ly2 = to_svg(x_max, m * x_max + c)
            elif "p1" in l and "p2" in l:
                p1, p2 = l["p1"], l["p2"]
                lx1, ly1 = to_svg(p1[0], p1[1])
                lx2, ly2 = to_svg(p2[0], p2[1])
            else:
                continue

            line_elements.append(
                f'<line x1="{lx1:.1f}" y1="{ly1:.1f}" x2="{lx2:.1f}" y2="{ly2:.1f}" stroke="{color}" stroke-width="{stroke_w}" {dashed} stroke-linecap="round"/>'
            )

            # Optional Line Label
            if l.get("label"):
                lbl = str(l["label"])
                # Place near positive end
                lbl_x = (lx1 + lx2 * 2) / 3
                lbl_y = (ly1 + ly2 * 2) / 3 - 8
                lbl_w = max(50, len(lbl) * 8 + 12)
                line_elements.append(
                    f'<rect x="{lbl_x - lbl_w/2:.1f}" y="{lbl_y - 12:.1f}" width="{lbl_w}" height="18" rx="4" fill="#0f172a" fill-opacity="0.9" stroke="{color}" stroke-width="1"/>'
                    f'<text x="{lbl_x:.1f}" y="{lbl_y + 1:.1f}" fill="{color}" font-size="11" font-weight="bold" font-family="monospace" text-anchor="middle">{lbl}</text>'
                )

    # Plotted Points & Coordinates
    point_elements: List[str] = []
    if points:
        for pt in points:
            px, py = float(pt["x"]), float(pt["y"])
            spx, spy = to_svg(px, py)
            p_color = pt.get("color", "#38bdf8")
            r = pt.get("r", 5)

            # Halo/Highlight if selected
            if pt.get("highlight"):
                point_elements.append(
                    f'<circle cx="{spx:.1f}" cy="{spy:.1f}" r="{r + 4}" fill="{p_color}" fill-opacity="0.25"/>'
                )

            point_elements.append(
                f'<circle cx="{spx:.1f}" cy="{spy:.1f}" r="{r}" fill="{pt.get("fill", "#0f172a")}" stroke="{p_color}" stroke-width="2"/>'
            )

            if pt.get("label"):
                lbl = str(pt["label"])
                offset_x = pt.get("offset_x", 10)
                offset_y = pt.get("offset_y", -10)
                lbl_anchor = "start" if offset_x >= 0 else "end"
                point_elements.append(
                    f'<rect x="{spx + offset_x - (0 if offset_x >= 0 else len(lbl)*7 + 8):.1f}" y="{spy + offset_y - 12:.1f}" width="{len(lbl)*7 + 10}" height="16" rx="3" fill="#0f172a" fill-opacity="0.85"/>'
                    f'<text x="{spx + offset_x:.1f}" y="{spy + offset_y:.1f}" fill="#f8fafc" font-size="11" font-weight="bold" font-family="monospace" text-anchor="{lbl_anchor}">{lbl}</text>'
                )

    title_elem = ""
    if title:
        title_elem = f'<text x="{width / 2:.1f}" y="20" fill="#f8fafc" font-size="13" font-weight="bold" font-family="sans-serif" text-anchor="middle">{title}</text>'

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="{height}" class="rounded-xl border border-slate-700 bg-slate-900/90 p-2">
{entropy_comment}<defs>
  <marker id="arrow-head" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
    <path d="M 0 1 L 8 5 L 0 9 z" fill="#94a3b8" />
  </marker>
</defs>
{title_elem}
<!-- Coordinate Grid -->
{"".join(grid_elements)}
<!-- Axes -->
{"".join(axis_elements)}
<!-- Slope Triangles -->
{"".join(triangle_elements)}
<!-- Lines -->
{"".join(line_elements)}
<!-- Points -->
{"".join(point_elements)}
</svg>"""
    return svg


def draw_dual_intercept_svg(
    x_int: float,
    y_int: float,
    line_label: str = "y = mx + c",
    seed: Optional[int] = None,
    **kwargs: Any,
) -> str:
    """Convenience helper to render a line highlighting its dual intercepts."""
    # Compute m and c:
    # (x_int, 0) and (0, y_int) => m = (0 - y_int) / (x_int - 0) = -y_int / x_int
    m = -y_int / x_int if x_int != 0 else 1
    c = y_int

    margin = max(abs(x_int), abs(y_int), 4) + 2
    x_range = (-margin, margin)
    y_range = (-margin, margin)

    lines = [{"m": m, "c": c, "color": "#38bdf8", "stroke_width": 2.5, "label": line_label}]
    points = [
        {"x": x_int, "y": 0, "label": f"({int(x_int) if x_int==int(x_int) else x_int}; 0)", "color": "#34d399", "fill": "#34d399", "highlight": True, "offset_y": 18 if y_int > 0 else -14},
        {"x": 0, "y": y_int, "label": f"(0; {int(y_int) if y_int==int(y_int) else y_int})", "color": "#f43f5e", "fill": "#f43f5e", "highlight": True, "offset_x": 12},
    ]

    return draw_cartesian_plane_svg(
        lines=lines,
        points=points,
        x_range=x_range,
        y_range=y_range,
        title="Dual-Intercept Method: Intercepts on Axes",
        seed=seed,
        **kwargs,
    )


def draw_slope_triangle_svg(
    p1: Tuple[float, float],
    p2: Tuple[float, float],
    line_label: str = "",
    seed: Optional[int] = None,
    **kwargs: Any,
) -> str:
    """Convenience helper to render a line with a prominent slope triangle."""
    x1, y1 = p1
    x2, y2 = p2
    dx = x2 - x1
    dy = y2 - y1
    m = dy / dx if dx != 0 else 1
    c = y1 - m * x1

    margin = max(abs(x1), abs(x2), abs(y1), abs(y2), 4) + 2
    x_range = (-margin, margin)
    y_range = (-margin, margin)

    lines = [{"m": m, "c": c, "color": "#38bdf8", "stroke_width": 2.5, "label": line_label}]
    points = [
        {"x": x1, "y": y1, "label": f"A({int(x1)}; {int(y1)})", "color": "#38bdf8", "fill": "#38bdf8", "highlight": True},
        {"x": x2, "y": y2, "label": f"B({int(x2)}; {int(y2)})", "color": "#38bdf8", "fill": "#38bdf8", "highlight": True},
    ]
    slope_triangles = [
        {
            "x1": x1,
            "y1": y1,
            "x2": x2,
            "y2": y2,
            "rise_label": f"Δy = {int(dy)}",
            "run_label": f"Δx = {int(dx)}",
            "color": "#f59e0b",
        }
    ]

    return draw_cartesian_plane_svg(
        lines=lines,
        points=points,
        slope_triangles=slope_triangles,
        x_range=x_range,
        y_range=y_range,
        title="Gradient Calculation: Slope Triangle (Rise / Run)",
        seed=seed,
        **kwargs,
    )


def draw_intersecting_lines_svg(
    line1: Dict[str, Any],
    line2: Dict[str, Any],
    intersection_pt: Tuple[float, float],
    title: str = "Point of Intersection of Two Lines",
    seed: Optional[int] = None,
    **kwargs: Any,
) -> str:
    """Renders two intersecting lines with highlighted point of intersection."""
    ix, iy = intersection_pt
    margin = max(abs(ix), abs(iy), 5) + 3
    x_range = (-margin, margin)
    y_range = (-margin, margin)

    points = [
        {
            "x": ix,
            "y": iy,
            "label": f"P({int(ix) if ix==int(ix) else ix}; {int(iy) if iy==int(iy) else iy})",
            "color": "#fbbf24",
            "fill": "#fbbf24",
            "highlight": True,
            "offset_x": 12,
            "offset_y": -12,
        }
    ]

    return draw_cartesian_plane_svg(
        lines=[line1, line2],
        points=points,
        x_range=x_range,
        y_range=y_range,
        title=title,
        seed=seed,
        **kwargs,
    )


def draw_rate_context_graph_svg(
    segments: List[Dict[str, Any]],
    x_label: str = "Time (hours)",
    y_label: str = "Volume (litres)",
    title: str = "Rate of Change Context Graph",
    x_max: float = 10,
    y_max: float = 100,
    seed: Optional[int] = None,
    **kwargs: Any,
) -> str:
    """Renders a first-quadrant rate context graph for distance-time,
    tank filling/emptying, or tariff comparisons.
    """
    entropy_comment = f"<!-- s:{seed} -->\n" if seed is not None else ""

    width = 480
    height = 300
    ox, oy = 60, 240
    pw, ph = 380, 180

    def to_svg(x: float, y: float) -> Tuple[float, float]:
        sx = ox + (x / x_max) * pw
        sy = oy - (y / y_max) * ph
        return sx, sy

    # Grid lines
    grid_lines = []
    x_step = x_max / 5
    y_step = y_max / 5
    for i in range(1, 6):
        gx = i * x_step
        sx, _ = to_svg(gx, 0)
        grid_lines.append(
            f'<line x1="{sx:.1f}" y1="{oy}" x2="{sx:.1f}" y2="{oy - ph}" stroke="#334155" stroke-width="0.8" stroke-dasharray="2,2"/>'
            f'<text x="{sx:.1f}" y="{oy + 16}" fill="#94a3b8" font-size="10" font-family="monospace" text-anchor="middle">{int(gx) if gx==int(gx) else f"{gx:.1f}"}</text>'
        )
        gy = i * y_step
        _, sy = to_svg(0, gy)
        grid_lines.append(
            f'<line x1="{ox}" y1="{sy:.1f}" x2="{ox + pw}" y2="{sy:.1f}" stroke="#334155" stroke-width="0.8" stroke-dasharray="2,2"/>'
            f'<text x="{ox - 8}" y="{sy + 4:.1f}" fill="#94a3b8" font-size="10" font-family="monospace" text-anchor="end">{int(gy) if gy==int(gy) else f"{gy:.1f}"}</text>'
        )

    # Segment lines and markers
    seg_elements = []
    for s in segments:
        pts = s.get("points", [])
        color = s.get("color", "#38bdf8")
        label = s.get("label", "")
        dashed = 'stroke-dasharray="4,4"' if s.get("dashed") else ""

        svg_coords = [to_svg(p[0], p[1]) for p in pts]
        for i in range(len(svg_coords) - 1):
            x1, y1 = svg_coords[i]
            x2, y2 = svg_coords[i + 1]
            seg_elements.append(
                f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{color}" stroke-width="2.8" {dashed} stroke-linecap="round"/>'
            )

        for p_idx, (p_svg, p_raw) in enumerate(zip(svg_coords, pts)):
            seg_elements.append(
                f'<circle cx="{p_svg[0]:.1f}" cy="{p_svg[1]:.1f}" r="4" fill="{color}" stroke="#0f172a" stroke-width="1.5"/>'
            )
            # Label point if requested
            if len(p_raw) >= 3 and p_raw[2]:
                seg_elements.append(
                    f'<text x="{p_svg[0]:.1f}" y="{p_svg[1] - 8:.1f}" fill="#f8fafc" font-size="10" font-weight="bold" font-family="monospace" text-anchor="middle">{p_raw[2]}</text>'
                )

        if label and svg_coords:
            lx, ly = svg_coords[-1]
            seg_elements.append(
                f'<text x="{lx + 6:.1f}" y="{ly + 4:.1f}" fill="{color}" font-size="11" font-weight="bold" font-family="sans-serif">{label}</text>'
            )

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="{height}" class="rounded-xl border border-slate-700 bg-slate-900/90 p-2">
{entropy_comment}<!-- Title -->
<text x="{width / 2:.1f}" y="24" fill="#f8fafc" font-size="13" font-weight="bold" font-family="sans-serif" text-anchor="middle">{title}</text>

<!-- Grid & Ticks -->
{"".join(grid_lines)}

<!-- Axes -->
<line x1="{ox}" y1="{oy}" x2="{ox + pw + 10}" y2="{oy}" stroke="#94a3b8" stroke-width="2"/>
<line x1="{ox}" y1="{oy}" x2="{ox}" y2="{oy - ph - 10}" stroke="#94a3b8" stroke-width="2"/>
<text x="{ox - 6}" y="{oy + 14}" fill="#94a3b8" font-size="10" font-family="monospace" text-anchor="end">0</text>

<!-- Axis Labels -->
<text x="{ox + pw / 2:.1f}" y="{oy + 34}" fill="#cbd5e1" font-size="11" font-weight="bold" font-family="sans-serif" text-anchor="middle">{x_label}</text>
<text x="{ox - 35}" y="{oy - ph / 2:.1f}" fill="#cbd5e1" font-size="11" font-weight="bold" font-family="sans-serif" text-anchor="middle" transform="rotate(-90 {ox - 35} {oy - ph / 2:.1f})">{y_label}</text>

<!-- Graph Segments -->
{"".join(seg_elements)}
</svg>"""
    return svg
