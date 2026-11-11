"""Grade 9 Mathematics - Decimal Notation SVG Diagrams.
Publication-grade SVG renderers for decimal place value, 10x10 hundredths grid,
zoomed decimal number lines, and Olympic timing scoreboards.
"""
from __future__ import annotations

from typing import Any, List, Optional, Tuple


def draw_hundredths_grid_svg(
    shaded_count: int,
    total: int = 100,
    seed: Optional[int] = None,
    **kwargs: Any,
) -> str:
    """Draws a 10x10 square grid with `shaded_count` cells highlighted."""
    entropy_comment = f"<!-- s:{seed} -->\n" if seed is not None else ""
    width = 320
    height = 320
    padding = 20
    grid_size = 280
    cell_size = grid_size / 10

    cells_svg = []
    current_shaded = 0

    for row in range(10):
        for col in range(10):
            x = padding + col * cell_size
            y = padding + row * cell_size
            if current_shaded < shaded_count:
                fill = "#2563EB"
                fill_opacity = "0.75"
                current_shaded += 1
            else:
                fill = "#FFFFFF"
                fill_opacity = "1.0"
            cells_svg.append(
                f'<rect x="{x:.1f}" y="{y:.1f}" width="{cell_size:.1f}" height="{cell_size:.1f}" '
                f'fill="{fill}" fill-opacity="{fill_opacity}" stroke="#475569" stroke-width="1"/>'
            )

    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
        f'width="{width}" height="{height}" class="mx-auto block" style="background:#F8FAFC;border-radius:8px;">\n'
        f"{entropy_comment}"
        f'  <g id="hundredths_grid">\n'
        f"    {''.join(cells_svg)}\n"
        f'    <rect x="{padding}" y="{padding}" width="{grid_size}" height="{grid_size}" '
        f'fill="none" stroke="#0F172A" stroke-width="2.5"/>\n'
        f'    <text x="{width/2}" y="{height - 4}" text-anchor="middle" font-size="12" '
        f'font-family="sans-serif" fill="#334155" font-weight="600">'
        f'10 × 10 Grid ({shaded_count} of 100 shaded)</text>\n'
        f'  </g>\n'
        f'</svg>'
    )


def draw_decimal_number_line_svg(
    start: float,
    end: float,
    step: float,
    marked_points: List[Tuple[float, str]],
    seed: Optional[int] = None,
    **kwargs: Any,
) -> str:
    """Draws a zoomed decimal number line with labeled ticks and points."""
    entropy_comment = f"<!-- s:{seed} -->\n" if seed is not None else ""
    width = 540
    height = 120
    pad_x = 45
    pad_y = 65
    line_w = width - 2 * pad_x

    span = end - start
    if span <= 0:
        span = 1.0

    ticks_svg = []
    cur = start
    while cur <= end + (step / 10):
        t_pos = (cur - start) / span
        x = pad_x + t_pos * line_w
        val_str = f"{cur:.2f}".rstrip("0").rstrip(".").replace(".", ",")
        ticks_svg.append(
            f'<line x1="{x:.1f}" y1="{pad_y - 8}" x2="{x:.1f}" y2="{pad_y + 8}" stroke="#334155" stroke-width="2"/>'
            f'<text x="{x:.1f}" y="{pad_y + 24}" text-anchor="middle" font-size="12" font-family="sans-serif" fill="#1E293B">{val_str}</text>'
        )
        cur += step

    points_svg = []
    colors = ["#DC2626", "#2563EB", "#059669", "#D97706"]
    for idx, (p_val, label) in enumerate(marked_points):
        p_pos = (p_val - start) / span
        px = pad_x + p_pos * line_w
        color = colors[idx % len(colors)]
        points_svg.append(
            f'<circle cx="{px:.1f}" cy="{pad_y}" r="6" fill="{color}" stroke="#FFFFFF" stroke-width="2"/>'
            f'<line x1="{px:.1f}" y1="{pad_y - 6}" x2="{px:.1f}" y2="{pad_y - 25}" stroke="{color}" stroke-width="2" stroke-dasharray="3,2"/>'
            f'<rect x="{px - 14:.1f}" y="{pad_y - 42}" width="28" height="18" rx="4" fill="{color}"/>'
            f'<text x="{px:.1f}" y="{pad_y - 29}" text-anchor="middle" font-size="11" font-weight="bold" font-family="sans-serif" fill="#FFFFFF">{label}</text>'
        )

    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
        f'width="{width}" height="{height}" class="mx-auto block" style="background:#F8FAFC;border-radius:8px;">\n'
        f"{entropy_comment}"
        f'  <defs>\n'
        f'    <marker id="arrow" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">\n'
        f'      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#334155"/>\n'
        f'    </marker>\n'
        f'  </defs>\n'
        f'  <line x1="{pad_x - 15}" y1="{pad_y}" x2="{width - pad_x + 15}" y2="{pad_y}" stroke="#334155" stroke-width="2.5" marker-start="url(#arrow)" marker-end="url(#arrow)"/>\n'
        f"  {''.join(ticks_svg)}\n"
        f"  {''.join(points_svg)}\n"
        f'</svg>'
    )


def draw_olympic_timing_board_svg(
    event_title: str,
    competitors: List[Tuple[str, str, float]],
    seed: Optional[int] = None,
    **kwargs: Any,
) -> str:
    """Draws a high-precision race timing scoreboard."""
    entropy_comment = f"<!-- s:{seed} -->\n" if seed is not None else ""
    width = 480
    row_h = 32
    header_h = 45
    height = header_h + len(competitors) * row_h + 15

    rows_svg = []
    for idx, (lane, name, time_val) in enumerate(competitors, 1):
        y = header_h + (idx - 1) * row_h
        bg_col = "#1E293B" if idx % 2 == 1 else "#0F172A"
        time_str = f"{time_val:.2f}".replace(".", ",") + " s"
        rank_badge = "#F59E0B" if idx == 1 else ("#94A3B8" if idx == 2 else ("#B45309" if idx == 3 else "#475569"))
        rows_svg.append(
            f'<rect x="15" y="{y}" width="{width - 30}" height="{row_h}" fill="{bg_col}"/>'
            f'<circle cx="35" cy="{y + row_h/2}" r="9" fill="{rank_badge}"/>'
            f'<text x="35" y="{y + row_h/2 + 4}" text-anchor="middle" font-size="11" font-weight="bold" font-family="sans-serif" fill="#FFFFFF">{idx}</text>'
            f'<text x="65" y="{y + row_h/2 + 4}" font-size="12" font-family="monospace" fill="#94A3B8">Lane {lane}</text>'
            f'<text x="145" y="{y + row_h/2 + 4}" font-size="12" font-weight="600" font-family="sans-serif" fill="#F8FAFC">{name}</text>'
            f'<text x="{width - 35}" y="{y + row_h/2 + 4}" text-anchor="end" font-size="13" font-weight="bold" font-family="monospace" fill="#38BDF8">{time_str}</text>'
        )

    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
        f'width="{width}" height="{height}" class="mx-auto block" style="background:#020617;border-radius:8px;">\n'
        f"{entropy_comment}"
        f'  <rect x="0" y="0" width="{width}" height="{header_h}" fill="#0F172A"/>'
        f'  <text x="{width/2}" y="28" text-anchor="middle" font-size="14" font-weight="bold" font-family="sans-serif" fill="#F8FAFC" letter-spacing="1">{event_title.upper()}</text>'
        f"  {''.join(rows_svg)}\n"
        f'  <rect x="15" y="10" width="{width - 30}" height="{height - 20}" fill="none" stroke="#334155" stroke-width="1.5" rx="4"/>'
        f'</svg>'
    )
