"""SVG diagram helpers for Grade 9 Whole Numbers & Financial Mathematics.
Produces clean, accessible, publication-grade vector graphics.
Always emits <!-- s:{seed} --> for guaranteed entropy across seeds.
"""
from __future__ import annotations

import math
from typing import Any, Dict, List, Optional, Tuple


def draw_number_system_hierarchy_svg(
    highlight_set: str = "Rational",
    seed: Optional[int] = None,
    **kwargs: Any,
) -> str:
    """Draws a Venn diagram / nested box diagram of Real numbers."""
    width = 440
    height = 240
    entropy_comment = f"<!-- s:{seed} -->\n" if seed is not None else ""

    hl = highlight_set.lower()
    c_real = "#2563eb"
    c_rat = "#059669"
    c_irrat = "#d97706"
    c_int = "#7c3aed"
    c_whole = "#db2777"
    c_nat = "#ea580c"

    svg_parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="auto" style="background-color:#ffffff; max-width:{width}px; margin:auto; display:block;">\n',
        entropy_comment,
        f'<rect x="10" y="10" width="420" height="220" rx="10" fill="#f8fafc" stroke="{c_real}" stroke-width="2.5" />\n',
        f'<text x="25" y="32" font-family="sans-serif" font-size="13" font-weight="bold" fill="{c_real}">Real Numbers (ℝ)</text>\n',
        # Left side: Rational hierarchy
        f'<rect x="25" y="45" width="270" height="175" rx="8" fill="#f0fdf4" stroke="{c_rat}" stroke-width="2" />\n',
        f'<text x="40" y="65" font-family="sans-serif" font-size="12" font-weight="bold" fill="{c_rat}">Rational Numbers (ℚ)</text>\n',
        f'<text x="210" y="65" font-family="sans-serif" font-size="10" fill="#166534">½, -¾, 0.375, 0.3̇</text>\n',
        # Integers inside Rational
        f'<rect x="40" y="78" width="240" height="132" rx="6" fill="#faf5ff" stroke="{c_int}" stroke-width="1.8" />\n',
        f'<text x="52" y="98" font-family="sans-serif" font-size="11" font-weight="bold" fill="{c_int}">Integers (ℤ)</text>\n',
        f'<text x="200" y="98" font-family="sans-serif" font-size="10" fill="#6b21a8">-5, -2, -1</text>\n',
        # Whole numbers inside Integers
        f'<rect x="52" y="110" width="216" height="90" rx="5" fill="#fdf2f8" stroke="{c_whole}" stroke-width="1.6" />\n',
        f'<text x="64" y="130" font-family="sans-serif" font-size="11" font-weight="bold" fill="{c_whole}">Whole Numbers (ℕ₀)</text>\n',
        f'<text x="220" y="130" font-family="sans-serif" font-size="10" fill="#9d174d">0</text>\n',
        # Natural numbers inside Whole
        f'<rect x="64" y="142" width="192" height="50" rx="4" fill="#fff7ed" stroke="{c_nat}" stroke-width="1.5" />\n',
        f'<text x="76" y="162" font-family="sans-serif" font-size="11" font-weight="bold" fill="{c_nat}">Natural (ℕ)</text>\n',
        f'<text x="76" y="180" font-family="sans-serif" font-size="10" fill="#9a3412">1, 2, 3, 4, 15, 100...</text>\n',
        # Right side: Irrational numbers
        f'<rect x="305" y="45" width="115" height="175" rx="8" fill="#fffbeb" stroke="{c_irrat}" stroke-width="2" />\n',
        f'<text x="315" y="65" font-family="sans-serif" font-size="12" font-weight="bold" fill="{c_irrat}">Irrational (ℚ\')</text>\n',
        f'<text x="325" y="95" font-family="sans-serif" font-size="11" fill="#92400e">√2, √3, √7</text>\n',
        f'<text x="325" y="125" font-family="sans-serif" font-size="11" fill="#92400e">π ≈ 3.14159...</text>\n',
        f'<text x="325" y="155" font-family="sans-serif" font-size="10" fill="#92400e">non-recurring</text>\n',
        f'<text x="325" y="170" font-family="sans-serif" font-size="10" fill="#92400e">non-terminating</text>\n',
        '</svg>\n',
    ]
    return "".join(svg_parts)


def draw_surd_number_line_svg(
    val: float,
    surd_label: str,
    lower_int: int,
    upper_int: int,
    seed: Optional[int] = None,
    **kwargs: Any,
) -> str:
    """Draws a calibrated number line showing between which two integers a surd lies."""
    width = 440
    height = 110
    entropy_comment = f"<!-- s:{seed} -->\n" if seed is not None else ""
    pad_x = 50
    axis_y = 55
    draw_w = width - 2 * pad_x

    min_val = lower_int - 1
    max_val = upper_int + 1
    span = max_val - min_val

    def to_px(v: float) -> float:
        return pad_x + ((v - min_val) / span) * draw_w

    surd_px = to_px(val)

    svg_parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="auto" style="background-color:#ffffff; max-width:{width}px; margin:auto; display:block;">\n',
        entropy_comment,
        '<defs>\n',
        '  <marker id="arrR" markerWidth="6" markerHeight="6" refX="4" refY="3" orient="auto"><path d="M 1 1 L 5 3 L 1 5 Z" fill="#1e293b"/></marker>\n',
        '  <marker id="arrL" markerWidth="6" markerHeight="6" refX="2" refY="3" orient="auto"><path d="M 5 1 L 1 3 L 5 5 Z" fill="#1e293b"/></marker>\n',
        '</defs>\n',
        f'<text x="{width/2}" y="18" text-anchor="middle" font-family="sans-serif" font-size="11" font-weight="bold" fill="#0f172a">Position of {surd_label} on Real Number Line</text>\n',
        f'<line x1="{pad_x - 15}" y1="{axis_y}" x2="{width - pad_x + 15}" y2="{axis_y}" stroke="#1e293b" stroke-width="2.5" marker-start="url(#arrL)" marker-end="url(#arrR)" />\n',
    ]

    for iv in range(min_val, max_val + 1):
        x = to_px(iv)
        is_bound = iv in (lower_int, upper_int)
        col = "#2563eb" if is_bound else "#64748b"
        sw = 2.5 if is_bound else 1.5
        svg_parts.append(f'<line x1="{x:.1f}" y1="{axis_y - 8}" x2="{x:.1f}" y2="{axis_y + 8}" stroke="{col}" stroke-width="{sw}" />\n')
        svg_parts.append(f'<text x="{x:.1f}" y="{axis_y + 24}" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="bold" fill="{col}">{iv}</text>\n')

    # Draw surd marker
    svg_parts.append(f'<circle cx="{surd_px:.1f}" cy="{axis_y}" r="5" fill="#dc2626" />\n')
    svg_parts.append(f'<line x1="{surd_px:.1f}" y1="{axis_y - 20}" x2="{surd_px:.1f}" y2="{axis_y - 5}" stroke="#dc2626" stroke-width="2" />\n')
    svg_parts.append(f'<text x="{surd_px:.1f}" y="{axis_y - 24}" text-anchor="middle" font-family="sans-serif" font-size="11" font-weight="bold" fill="#dc2626">{surd_label}</text>\n')

    svg_parts.append('</svg>\n')
    return "".join(svg_parts)


def draw_factor_tree_svg(
    num: int,
    factors: List[Tuple[int, int]],
    seed: Optional[int] = None,
    **kwargs: Any,
) -> str:
    """Draws a factor tree branch showing prime factorization."""
    width = 320
    height = 180
    entropy_comment = f"<!-- s:{seed} -->\n" if seed is not None else ""

    svg_parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="auto" style="background-color:#ffffff; max-width:{width}px; margin:auto; display:block;">\n',
        entropy_comment,
        f'<text x="{width/2}" y="18" text-anchor="middle" font-family="sans-serif" font-size="11" font-weight="bold" fill="#0f172a">Prime Factor Tree: {num}</text>\n',
        # Root node
        f'<circle cx="160" cy="45" r="18" fill="#eff6ff" stroke="#2563eb" stroke-width="2"/>\n',
        f'<text x="160" y="50" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="bold" fill="#1e40af">{num}</text>\n',
        # Branches
        f'<line x1="145" y1="60" x2="100" y2="105" stroke="#64748b" stroke-width="1.8"/>\n',
        f'<line x1="175" y1="60" x2="220" y2="105" stroke="#64748b" stroke-width="1.8"/>\n',
    ]

    f1 = factors[0][0] if factors else 2
    f2 = num // f1 if factors else num // 2
    svg_parts.append(f'<circle cx="100" cy="115" r="16" fill="#f0fdf4" stroke="#16a34a" stroke-width="2"/>\n')
    svg_parts.append(f'<text x="100" y="120" text-anchor="middle" font-family="sans-serif" font-size="11" font-weight="bold" fill="#166534">{f1}</text>\n')
    svg_parts.append(f'<circle cx="220" cy="115" r="16" fill="#eff6ff" stroke="#2563eb" stroke-width="2"/>\n')
    svg_parts.append(f'<text x="220" y="120" text-anchor="middle" font-family="sans-serif" font-size="11" font-weight="bold" fill="#1e40af">{f2}</text>\n')

    svg_parts.append('</svg>\n')
    return "".join(svg_parts)


def draw_interest_comparison_bar_chart_svg(
    principal: float,
    rate_pct: float,
    years: int,
    si_amount: float,
    ci_amount: float,
    seed: Optional[int] = None,
    **kwargs: Any,
) -> str:
    """Draws a comparison bar chart between Simple Interest and Compound Interest."""
    width = 420
    height = 200
    entropy_comment = f"<!-- s:{seed} -->\n" if seed is not None else ""

    max_amt = max(si_amount, ci_amount) * 1.15
    chart_h = 130
    pad_b = 40
    pad_l = 80

    def val_to_h(v: float) -> float:
        return (v / max_amt) * chart_h

    h_p = val_to_h(principal)
    h_si = val_to_h(si_amount)
    h_ci = val_to_h(ci_amount)

    y_p = height - pad_b - h_p
    y_si = height - pad_b - h_si
    y_ci = height - pad_b - h_ci

    svg_parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="auto" style="background-color:#ffffff; max-width:{width}px; margin:auto; display:block;">\n',
        entropy_comment,
        f'<text x="{width/2}" y="20" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="bold" fill="#0f172a">Growth Comparison: {years} Years @ {rate_pct}%</text>\n',
        f'<line x1="{pad_l}" y1="{height - pad_b}" x2="{width - 30}" y2="{height - pad_b}" stroke="#334155" stroke-width="2"/>\n',
        # Principal Bar
        f'<rect x="{pad_l + 20}" y="{y_p:.1f}" width="60" height="{h_p:.1f}" fill="#94a3b8" rx="3"/>\n',
        f'<text x="{pad_l + 50}" y="{y_p - 6:.1f}" text-anchor="middle" font-family="sans-serif" font-size="10" font-weight="bold" fill="#475569">R {int(principal)}</text>\n',
        f'<text x="{pad_l + 50}" y="{height - pad_b + 18}" text-anchor="middle" font-family="sans-serif" font-size="11" font-weight="bold" fill="#334155">Principal</text>\n',
        # Simple Interest Bar
        f'<rect x="{pad_l + 115}" y="{y_si:.1f}" width="60" height="{h_si:.1f}" fill="#3b82f6" rx="3"/>\n',
        f'<text x="{pad_l + 145}" y="{y_si - 6:.1f}" text-anchor="middle" font-family="sans-serif" font-size="10" font-weight="bold" fill="#1d4ed8">R {int(si_amount)}</text>\n',
        f'<text x="{pad_l + 145}" y="{height - pad_b + 18}" text-anchor="middle" font-family="sans-serif" font-size="11" font-weight="bold" fill="#1d4ed8">Simple (A)</text>\n',
        # Compound Interest Bar
        f'<rect x="{pad_l + 210}" y="{y_ci:.1f}" width="60" height="{h_ci:.1f}" fill="#10b981" rx="3"/>\n',
        f'<text x="{pad_l + 240}" y="{y_ci - 6:.1f}" text-anchor="middle" font-family="sans-serif" font-size="10" font-weight="bold" fill="#047857">R {int(ci_amount)}</text>\n',
        f'<text x="{pad_l + 240}" y="{height - pad_b + 18}" text-anchor="middle" font-family="sans-serif" font-size="11" font-weight="bold" fill="#047857">Compound (A)</text>\n',
        '</svg>\n',
    ]
    return "".join(svg_parts)
