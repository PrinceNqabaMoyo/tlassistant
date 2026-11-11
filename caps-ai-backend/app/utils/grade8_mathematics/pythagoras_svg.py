"""Grade 8 Mathematics — Pythagoras SVG Diagram Generators.
Crisp vector SVG illustrations:
  - Right-angled triangle with right-angle corner symbol, vertex labels, and side dimensions.
  - Proof illustration with square areas constructed on each of the 3 sides (a², b², c²).
  - Contextual real-world models (ladder against wall, diagonal of rectangle, isosceles altitude).

Strictly deterministic, parameter-driven SVG rendering for exam and visual companion views.
"""
from __future__ import annotations

import random
from typing import Optional


def draw_pythagoras_triangle_svg(
    a_val: float | int,
    b_val: float | int,
    c_val: float | int,
    v_bottom_left: str = "B",
    v_right: str = "C",
    v_top: str = "A",
    unknown: str = "c",  # 'a', 'b', or 'c'
    seed: int = 101,
) -> str:
    """Renders a standard right-angled triangle with right angle at bottom-left vertex."""
    rng = random.Random(seed)
    w, h = 360, 260

    dx = rng.choice([-10, -5, 0, 5, 10])
    dy = rng.choice([-6, -3, 0, 3, 6])

    bx, by = 80 + dx, 200 + dy
    cx_pt, cy_pt = 270 + dx, 200 + dy
    ax, ay = 80 + dx, 50 + dy

    # Labels for sides
    a_str = "?" if unknown == "a" else f"{a_val} cm"
    b_str = "?" if unknown == "b" else f"{b_val} cm"
    c_str = "?" if unknown == "c" else f"{c_val} cm"

    sq_size = 16

    lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" height="100%" style="background:#ffffff; font-family:sans-serif;">',
        f'  <!-- seed: {seed} -->',
        f'  <polyline points="{bx},{by-sq_size} {bx+sq_size},{by-sq_size} {bx+sq_size},{by}" fill="none" stroke="#2563eb" stroke-width="2"/>',
        f'  <polygon points="{bx},{by} {cx_pt},{cy_pt} {ax},{ay}" fill="rgba(37, 99, 235, 0.08)" stroke="#1e293b" stroke-width="2.5"/>',
        f'  <text x="{bx-18}" y="{by+16}" font-size="14" font-weight="bold" fill="#1e3a8a">{v_bottom_left}</text>',
        f'  <text x="{cx_pt+10}" y="{cy_pt+6}" font-size="14" font-weight="bold" fill="#1e3a8a">{v_right}</text>',
        f'  <text x="{ax-18}" y="{ay+6}" font-size="14" font-weight="bold" fill="#1e3a8a">{v_top}</text>',
        f'  <text x="{bx-15}" y="{(ay+by)/2 + 5}" font-size="12" font-weight="bold" fill="#b91c1c" text-anchor="end">{a_str}</text>',
        f'  <text x="{(bx+cx_pt)/2}" y="{by+22}" font-size="12" font-weight="bold" fill="#15803d" text-anchor="middle">{b_str}</text>',
        f'  <text x="{(ax+cx_pt)/2 + 15}" y="{(ay+cy_pt)/2 - 8}" font-size="13" font-weight="bold" fill="#4338ca">{c_str}</text>',
        f'  <text x="{w/2}" y="{h-10}" font-size="11" font-weight="bold" fill="#64748b" text-anchor="middle">Right-angled at vertex {v_bottom_left} (90°)</text>',
        '</svg>',
    ]
    return "\n".join(lines)


def draw_pythagoras_squares_proof_svg(
    a: int = 3,
    b: int = 4,
    c: int = 5,
    seed: int = 101,
) -> str:
    """Renders a right-angled triangle with squares constructed on all three sides illustrating a² + b² = c²."""
    rng = random.Random(seed)
    w, h = 380, 320
    a2, b2, c2 = a * a, b * b, c * c
    dx = rng.choice([-5, 0, 5])
    dy = rng.choice([-3, 0, 3])

    p_b = (130 + dx, 200 + dy)
    p_c = (210 + dx, 200 + dy)
    p_a = (130 + dx, 140 + dy)

    lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" height="100%" style="background:#ffffff; font-family:sans-serif;">',
        f'  <!-- seed: {seed} -->',
        f'  <polygon points="{p_b[0]},{p_b[1]} {p_c[0]},{p_c[1]} {p_a[0]},{p_a[1]}" fill="#f8fafc" stroke="#1e293b" stroke-width="2"/>',
        f'  <polyline points="{p_b[0]},{p_b[1]-12} {p_b[0]+12},{p_b[1]-12} {p_b[0]+12},{p_b[1]}" fill="none" stroke="#2563eb" stroke-width="1.5"/>',
        f'  <rect x="{p_b[0]-60}" y="{p_a[1]}" width="60" height="60" fill="rgba(239, 68, 68, 0.15)" stroke="#dc2626" stroke-width="1.5"/>',
        f'  <text x="{p_b[0]-30}" y="{p_a[1]+35}" font-size="12" font-weight="bold" fill="#b91c1c" text-anchor="middle">a² = {a2}</text>',
        f'  <rect x="{p_b[0]}" y="{p_b[1]}" width="80" height="80" fill="rgba(34, 197, 94, 0.15)" stroke="#16a34a" stroke-width="1.5"/>',
        f'  <text x="{p_b[0]+40}" y="{p_b[1]+45}" font-size="12" font-weight="bold" fill="#15803d" text-anchor="middle">b² = {b2}</text>',
        f'  <polygon points="{p_a[0]},{p_a[1]} {p_c[0]},{p_c[1]} {p_c[0]+60},{p_c[1]-80} {p_a[0]+60},{p_a[1]-80}" fill="rgba(59, 130, 246, 0.15)" stroke="#2563eb" stroke-width="1.5"/>',
        f'  <text x="{p_b[0]+70}" y="{p_a[1]-10}" font-size="12" font-weight="bold" fill="#1d4ed8" text-anchor="middle">c² = {c2}</text>',
        f'  <text x="{w/2}" y="{h-10}" font-size="12" font-weight="bold" fill="#0f172a" text-anchor="middle">Area Proof: {a2} + {b2} = {c2} ({a}² + {b}² = {c}²)</text>',
        '</svg>',
    ]
    return "\n".join(lines)


def draw_pythagoras_ladder_context_svg(
    wall_h: float | int,
    dist: float | int,
    ladder: float | int,
    unknown: str = "ladder",
    seed: int = 101,
) -> str:
    """Renders a ladder leaning against a vertical wall on horizontal ground."""
    rng = random.Random(seed)
    w, h = 320, 240
    ladder_str = "?" if unknown == "ladder" else f"{ladder} m"
    wall_str = "?" if unknown == "wall" else f"{wall_h} m"
    dist_str = "?" if unknown == "ground" else f"{dist} m"

    dx = rng.choice([-8, -4, 0, 4, 8])
    dy = rng.choice([-5, -2, 0, 2, 5])

    wall_x = 70 + dx
    ground_y = 200 + dy
    wall_top_y = 30 + dy
    ladder_top_y = 50 + dy
    ladder_foot_x = 230 + dx

    lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" height="100%" style="background:#ffffff; font-family:sans-serif;">',
        f'  <!-- seed: {seed} -->',
        f'  <line x1="{wall_x}" y1="{wall_top_y}" x2="{wall_x}" y2="{ground_y}" stroke="#64748b" stroke-width="6"/>',
        f'  <line x1="{wall_x-20}" y1="{ground_y}" x2="{ladder_foot_x+40}" y2="{ground_y}" stroke="#334155" stroke-width="4"/>',
        f'  <polyline points="{wall_x},{ground_y-15} {wall_x+15},{ground_y-15} {wall_x+15},{ground_y}" fill="none" stroke="#dc2626" stroke-width="1.5"/>',
        f'  <line x1="{wall_x}" y1="{ladder_top_y}" x2="{ladder_foot_x}" y2="{ground_y}" stroke="#b45309" stroke-width="4"/>',
        f'  <text x="{wall_x-20}" y="{(wall_top_y+ground_y)/2}" font-size="12" font-weight="bold" fill="#1e293b" text-anchor="end">Wall: {wall_str}</text>',
        f'  <text x="{(wall_x+ladder_foot_x)/2}" y="{ground_y+22}" font-size="12" font-weight="bold" fill="#1e293b" text-anchor="middle">Ground: {dist_str}</text>',
        f'  <text x="{(wall_x+ladder_foot_x)/2 + 15}" y="{(ladder_top_y+ground_y)/2 - 5}" font-size="13" font-weight="bold" fill="#b45309">Ladder: {ladder_str}</text>',
        f'  <text x="{w/2}" y="{h-6}" font-size="11" fill="#64748b" text-anchor="middle">Wall meets ground at 90°</text>',
        '</svg>',
    ]
    return "\n".join(lines)
