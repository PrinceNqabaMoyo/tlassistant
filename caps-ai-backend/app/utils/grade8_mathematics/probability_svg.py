"""Grade 8 Mathematics — Probability SVG Visualizations.
Crisp vector SVG illustrations:
  - Probability scale (0 to 1) with descriptive milestones (impossible, unlikely, even, likely, certain).
  - Circular spinner with equal or unequal colored/numbered sectors and pointer.
  - Tree diagram illustrating 2-stage compound events (e.g. tossing two coins or coin + dice).
  - Jar/bag of colored marbles.

Deterministic, parameter-driven SVG rendering conforming to 5D Diagram referee standards.
"""
from __future__ import annotations

import math
import random
from typing import List, Optional, Tuple


def draw_probability_scale_svg(marker_val: float = 0.5, marker_label: str = "Even chance", seed: int = 101) -> str:
    """Renders a horizontal probability scale from 0 to 1 with milestones and an indicator marker."""
    rng = random.Random(seed)
    w, h = 380, 140
    dx = rng.choice([-4, 0, 4])
    x_start = 40 + dx
    x_end = 340 + dx
    line_y = 65

    # Milestone positions
    # 0 = impossible, 0.25 = unlikely, 0.5 = even, 0.75 = likely, 1.0 = certain
    marker_x = x_start + marker_val * (x_end - x_start)

    lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" height="100%" style="background:#ffffff; font-family:sans-serif;">',
        f'  <!-- seed: {seed} -->',
        f'  <defs>',
        f'    <linearGradient id="probGrad" x1="0%" y1="0%" x2="100%" y2="0%">',
        f'      <stop offset="0%" stop-color="#ef4444" stop-opacity="0.4"/>',
        f'      <stop offset="50%" stop-color="#f59e0b" stop-opacity="0.4"/>',
        f'      <stop offset="100%" stop-color="#22c55e" stop-opacity="0.4"/>',
        f'    </linearGradient>',
        f'  </defs>',
        f'  <rect x="{x_start}" y="{line_y-6}" width="{x_end-x_start}" height="12" rx="6" fill="url(#probGrad)"/>',
        f'  <line x1="{x_start}" y1="{line_y}" x2="{x_end}" y2="{line_y}" stroke="#1e293b" stroke-width="2"/>',
        f'  <!-- Ticks -->',
        f'  <line x1="{x_start}" y1="{line_y-10}" x2="{x_start}" y2="{line_y+10}" stroke="#0f172a" stroke-width="2"/>',
        f'  <line x1="{(x_start+x_end)/2}" y1="{line_y-8}" x2="{(x_start+x_end)/2}" y2="{line_y+8}" stroke="#0f172a" stroke-width="2"/>',
        f'  <line x1="{x_end}" y1="{line_y-10}" x2="{x_end}" y2="{line_y+10}" stroke="#0f172a" stroke-width="2"/>',
        f'  <!-- Labels -->',
        f'  <text x="{x_start}" y="{line_y+26}" font-size="11" font-weight="bold" fill="#b91c1c" text-anchor="middle">0 (Impossible)</text>',
        f'  <text x="{(x_start+x_end)/2}" y="{line_y+26}" font-size="11" font-weight="bold" fill="#b45309" text-anchor="middle">0,5 (Even)</text>',
        f'  <text x="{x_end}" y="{line_y+26}" font-size="11" font-weight="bold" fill="#15803d" text-anchor="middle">1 (Certain)</text>',
        f'  <!-- Indicator pin -->',
        f'  <polygon points="{marker_x},{line_y-8} {marker_x-6},{line_y-20} {marker_x+6},{line_y-20}" fill="#2563eb"/>',
        f'  <circle cx="{marker_x}" cy="{line_y-25}" r="5" fill="#2563eb"/>',
        f'  <text x="{marker_x}" y="{line_y-34}" font-size="11" font-weight="bold" fill="#1d4ed8" text-anchor="middle">{marker_label}</text>',
        f'  <text x="{w/2}" y="{h-8}" font-size="11" fill="#64748b" text-anchor="middle">The Probability Scale (0 to 1)</text>',
        '</svg>',
    ]
    return "\n".join(lines)


def draw_spinner_svg(sectors: List[Tuple[str, str, float]], seed: int = 101) -> str:
    """Renders a circular spinner with sectors given as (label, hex_color, fraction_of_circle)."""
    rng = random.Random(seed)
    w, h = 260, 260
    cx, cy = 130, 125
    r = 85

    dx = rng.choice([-4, 0, 4])
    dy = rng.choice([-3, 0, 3])
    cx += dx
    cy += dy

    lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" height="100%" style="background:#ffffff; font-family:sans-serif;">',
        f'  <!-- seed: {seed} -->',
    ]

    current_angle = -90.0  # Start at top
    for label, col, frac in sectors:
        span_deg = frac * 360.0
        rad1 = math.radians(current_angle)
        rad2 = math.radians(current_angle + span_deg)

        x1 = cx + r * math.cos(rad1)
        y1 = cy + r * math.sin(rad1)
        x2 = cx + r * math.cos(rad2)
        y2 = cy + r * math.sin(rad2)

        large_arc = 1 if span_deg > 180 else 0
        path_d = f"M {cx},{cy} L {x1:.1f},{y1:.1f} A {r},{r} 0 {large_arc},1 {x2:.1f},{y2:.1f} Z"
        lines.append(f'  <path d="{path_d}" fill="{col}" stroke="#1e293b" stroke-width="2"/>')

        # Sector label
        mid_rad = math.radians(current_angle + span_deg / 2)
        lx = cx + 0.6 * r * math.cos(mid_rad)
        ly = cy + 0.6 * r * math.sin(mid_rad) + 4
        lines.append(f'  <text x="{lx:.1f}" y="{ly:.1f}" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="middle">{label}</text>')

        current_angle += span_deg

    # Pointer arrow at center pointing right-up
    ptr_angle = rng.choice([25, 45, 60, 75, 110, 135])
    p_rad = math.radians(ptr_angle)
    px = cx + 55 * math.cos(p_rad)
    py = cy + 55 * math.sin(p_rad)

    lines.extend([
        f'  <!-- Center pin & Pointer arrow -->',
        f'  <circle cx="{cx}" cy="{cy}" r="7" fill="#0f172a"/>',
        f'  <line x1="{cx}" y1="{cy}" x2="{px:.1f}" y2="{py:.1f}" stroke="#dc2626" stroke-width="3.5" stroke-linecap="round"/>',
        f'  <polygon points="{px:.1f},{py:.1f} {px-8*math.cos(p_rad-0.5):.1f},{py-8*math.sin(p_rad-0.5):.1f} {px-8*math.cos(p_rad+0.5):.1f},{py-8*math.sin(p_rad+0.5):.1f}" fill="#dc2626"/>',
        f'  <text x="{w/2}" y="{h-8}" font-size="11" fill="#64748b" text-anchor="middle">Fair Spinner with Pointer</text>',
        '</svg>',
    ])
    return "\n".join(lines)


def draw_tree_diagram_two_coins_svg(seed: int = 101) -> str:
    """Renders a tree diagram for tossing two fair coins."""
    rng = random.Random(seed)
    w, h = 340, 220
    dx = rng.choice([-4, 0, 4])
    ox, oy = 40 + dx, 110

    # Branch 1 (Coin 1): H at (130, 60), T at (130, 160)
    c1_h = (130 + dx, 60)
    c1_t = (130 + dx, 160)

    # Branch 2 (Coin 2):
    # From H: H at (230, 35), T at (230, 85)
    c2_hh = (230 + dx, 35)
    c2_ht = (230 + dx, 85)
    # From T: H at (230, 135), T at (230, 185)
    c2_th = (230 + dx, 135)
    c2_tt = (230 + dx, 185)

    lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" height="100%" style="background:#ffffff; font-family:sans-serif;">',
        f'  <!-- seed: {seed} -->',
        f'  <!-- Stage 1 branches -->',
        f'  <line x1="{ox}" y1="{oy}" x2="{c1_h[0]}" y2="{c1_h[1]}" stroke="#2563eb" stroke-width="2"/>',
        f'  <line x1="{ox}" y1="{oy}" x2="{c1_t[0]}" y2="{c1_t[1]}" stroke="#2563eb" stroke-width="2"/>',
        f'  <text x="{(ox+c1_h[0])/2 - 5}" y="{(oy+c1_h[1])/2 - 4}" font-size="11" fill="#1d4ed8">1/2</text>',
        f'  <text x="{(ox+c1_t[0])/2 - 5}" y="{(oy+c1_t[1])/2 + 14}" font-size="11" fill="#1d4ed8">1/2</text>',
        f'  <!-- Node 1 labels -->',
        f'  <circle cx="{c1_h[0]}" cy="{c1_h[1]}" r="12" fill="#bfdbfe" stroke="#1e40af" stroke-width="1.5"/>',
        f'  <text x="{c1_h[0]}" y="{c1_h[1]+4}" font-size="12" font-weight="bold" fill="#1e3a8a" text-anchor="middle">H</text>',
        f'  <circle cx="{c1_t[0]}" cy="{c1_t[1]}" r="12" fill="#fecaca" stroke="#991b1b" stroke-width="1.5"/>',
        f'  <text x="{c1_t[0]}" y="{c1_t[1]+4}" font-size="12" font-weight="bold" fill="#7f1d1d" text-anchor="middle">T</text>',
        f'  <!-- Stage 2 branches from H -->',
        f'  <line x1="{c1_h[0]}" y1="{c1_h[1]}" x2="{c2_hh[0]}" y2="{c2_hh[1]}" stroke="#64748b" stroke-width="1.5"/>',
        f'  <line x1="{c1_h[0]}" y1="{c1_h[1]}" x2="{c2_ht[0]}" y2="{c2_ht[1]}" stroke="#64748b" stroke-width="1.5"/>',
        f'  <!-- Stage 2 branches from T -->',
        f'  <line x1="{c1_t[0]}" y1="{c1_t[1]}" x2="{c2_th[0]}" y2="{c2_th[1]}" stroke="#64748b" stroke-width="1.5"/>',
        f'  <line x1="{c1_t[0]}" y1="{c1_t[1]}" x2="{c2_tt[0]}" y2="{c2_tt[1]}" stroke="#64748b" stroke-width="1.5"/>',
        f'  <!-- Node 2 labels -->',
        f'  <text x="{c2_hh[0]}" y="{c2_hh[1]+4}" font-size="11" font-weight="bold" fill="#0f172a">H → (H, H)</text>',
        f'  <text x="{c2_ht[0]}" y="{c2_ht[1]+4}" font-size="11" font-weight="bold" fill="#0f172a">T → (H, T)</text>',
        f'  <text x="{c2_th[0]}" y="{c2_th[1]+4}" font-size="11" font-weight="bold" fill="#0f172a">H → (T, H)</text>',
        f'  <text x="{c2_tt[0]}" y="{c2_tt[1]+4}" font-size="11" font-weight="bold" fill="#0f172a">T → (T, T)</text>',
        f'  <!-- Stage headings -->',
        f'  <text x="{c1_h[0]}" y="20" font-size="11" font-weight="bold" fill="#475569" text-anchor="middle">Coin 1</text>',
        f'  <text x="{c2_hh[0]+15}" y="20" font-size="11" font-weight="bold" fill="#475569" text-anchor="middle">Coin 2 &amp; Outcomes</text>',
        f'  <text x="{w/2}" y="{h-6}" font-size="10" fill="#64748b" text-anchor="middle">Tree Diagram: 4 Equally Likely Outcomes (P = 1/4 each)</text>',
        '</svg>',
    ]
    return "\n".join(lines)


def draw_coin_and_dice_tree_svg(seed: int = 101) -> str:
    """Renders a tree diagram for tossing a coin then rolling a 6-sided dice."""
    rng = random.Random(seed)
    w, h = 360, 240
    dx = rng.choice([-4, 0, 4])
    ox, oy = 40 + dx, 120

    c_h = (130 + dx, 65)
    c_t = (130 + dx, 175)

    lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" height="100%" style="background:#ffffff; font-family:sans-serif;">',
        f'  <!-- seed: {seed} -->',
        f'  <line x1="{ox}" y1="{oy}" x2="{c_h[0]}" y2="{c_h[1]}" stroke="#2563eb" stroke-width="2"/>',
        f'  <line x1="{ox}" y1="{oy}" x2="{c_t[0]}" y2="{c_t[1]}" stroke="#2563eb" stroke-width="2"/>',
        f'  <text x="{(ox+c_h[0])/2 - 5}" y="{(oy+c_h[1])/2 - 4}" font-size="10" fill="#1d4ed8">1/2</text>',
        f'  <text x="{(ox+c_t[0])/2 - 5}" y="{(oy+c_t[1])/2 + 12}" font-size="10" fill="#1d4ed8">1/2</text>',
        f'  <circle cx="{c_h[0]}" cy="{c_h[1]}" r="12" fill="#bfdbfe" stroke="#1e40af" stroke-width="1.5"/>',
        f'  <text x="{c_h[0]}" y="{c_h[1]+4}" font-size="11" font-weight="bold" fill="#1e3a8a" text-anchor="middle">H</text>',
        f'  <circle cx="{c_t[0]}" cy="{c_t[1]}" r="12" fill="#fecaca" stroke="#991b1b" stroke-width="1.5"/>',
        f'  <text x="{c_t[0]}" y="{c_t[1]+4}" font-size="11" font-weight="bold" fill="#7f1d1d" text-anchor="middle">T</text>',
    ]

    # Sub-branches for 1..6
    for i in range(1, 7):
        # From H: y from 25 to 105 in 16px increments
        y_h = 22 + (i - 1) * 16
        lines.append(f'  <line x1="{c_h[0]}" y1="{c_h[1]}" x2="{240+dx}" y2="{y_h}" stroke="#94a3b8" stroke-width="1"/>')
        lines.append(f'  <text x="{245+dx}" y="{y_h+4}" font-size="10" font-weight="bold" fill="#0f172a">{i} → H{i}</text>')

        # From T: y from 135 to 215 in 16px increments
        y_t = 132 + (i - 1) * 16
        lines.append(f'  <line x1="{c_t[0]}" y1="{c_t[1]}" x2="{240+dx}" y2="{y_t}" stroke="#94a3b8" stroke-width="1"/>')
        lines.append(f'  <text x="{245+dx}" y="{y_t+4}" font-size="10" font-weight="bold" fill="#0f172a">{i} → T{i}</text>')

    lines.extend([
        f'  <text x="{c_h[0]}" y="14" font-size="11" font-weight="bold" fill="#475569" text-anchor="middle">Coin</text>',
        f'  <text x="{265+dx}" y="14" font-size="11" font-weight="bold" fill="#475569" text-anchor="middle">Dice &amp; Outcomes</text>',
        f'  <text x="{w/2}" y="{h-4}" font-size="10" fill="#64748b" text-anchor="middle">Total Sample Space: 12 Combined Outcomes (P = 1/12 each)</text>',
        '</svg>',
    ])
    return "\n".join(lines)
