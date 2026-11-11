"""Reusable SVG drawing helpers for Grade 8 Mathematics - Perimeter and Area of 2D Shapes.
Produces crisp, publication-grade, accessible SVG diagrams parameterized by dimensions and seed.
"""
from __future__ import annotations

import math
import random
from typing import Dict, Optional, Tuple


def draw_labeled_rect_svg(
    length_lbl: str,
    breadth_lbl: str,
    seed: Optional[int] = None,
) -> str:
    """Draw a rectangle with length and breadth labels."""
    w, h = 380, 240
    salt = f"<!-- seed:{seed if seed is not None else random.randint(100, 999999)} -->\n"
    rx, ry, rw, rh = 50, 40, 280, 150

    return f"""{salt}<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" height="100%">
  <rect width="{w}" height="{h}" fill="#f8fafc" rx="8"/>
  <rect x="{rx}" y="{ry}" width="{rw}" height="{rh}" fill="#eff6ff" stroke="#2563eb" stroke-width="2.5" rx="4"/>
  <text x="{rx + rw/2}" y="{ry - 12}" text-anchor="middle" font-family="system-ui, sans-serif" font-size="13" font-weight="700" fill="#1e293b">{length_lbl}</text>
  <text x="{rx + rw + 15}" y="{ry + rh/2 + 5}" font-family="system-ui, sans-serif" font-size="13" font-weight="700" fill="#1e293b">{breadth_lbl}</text>
  <!-- Right angle symbols -->
  <rect x="{rx}" y="{ry}" width="12" height="12" fill="none" stroke="#2563eb" stroke-width="1.5"/>
  <rect x="{rx + rw - 12}" y="{ry}" width="12" height="12" fill="none" stroke="#2563eb" stroke-width="1.5"/>
  <rect x="{rx}" y="{ry + rh - 12}" width="12" height="12" fill="none" stroke="#2563eb" stroke-width="1.5"/>
  <rect x="{rx + rw - 12}" y="{ry + rh - 12}" width="12" height="12" fill="none" stroke="#2563eb" stroke-width="1.5"/>
</svg>"""


def draw_triangle_with_height_svg(
    base_lbl: str,
    height_lbl: str,
    side_lbl: Optional[str] = None,
    seed: Optional[int] = None,
) -> str:
    """Draw a triangle with a dashed interior perpendicular height and right-angle box."""
    w, h = 380, 250
    salt = f"<!-- seed:{seed if seed is not None else random.randint(100, 999999)} -->\n"

    ax, ay = 170, 40
    bx, by = 50, 200
    cx, cy = 330, 200
    hx, hy = ax, by

    side_svg = ""
    if side_lbl:
        side_svg = f'<text x="{(ax+bx)/2 - 20}" y="{(ay+by)/2}" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#059669">{side_lbl}</text>'

    return f"""{salt}<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" height="100%">
  <rect width="{w}" height="{h}" fill="#f8fafc" rx="8"/>
  <polygon points="{ax},{ay} {bx},{by} {cx},{cy}" fill="#ecfdf5" stroke="#059669" stroke-width="2.5" stroke-linejoin="round"/>
  <!-- Height dashed line -->
  <line x1="{ax}" y1="{ay}" x2="{hx}" y2="{hy}" stroke="#dc2626" stroke-width="2" stroke-dasharray="4,4"/>
  <rect x="{hx}" y="{hy - 12}" width="12" height="12" fill="none" stroke="#dc2626" stroke-width="1.5"/>
  <!-- Labels -->
  <text x="{hx + 10}" y="{(ay + hy)/2}" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#dc2626">h = {height_lbl}</text>
  <text x="{(bx + cx)/2}" y="{by + 22}" text-anchor="middle" font-family="system-ui, sans-serif" font-size="13" font-weight="700" fill="#1e293b">b = {base_lbl}</text>
  {side_svg}
</svg>"""


def draw_parallelogram_with_height_svg(
    base_lbl: str,
    height_lbl: str,
    slant_lbl: Optional[str] = None,
    seed: Optional[int] = None,
) -> str:
    """Draw a parallelogram with an interior perpendicular height."""
    w, h = 400, 250
    salt = f"<!-- seed:{seed if seed is not None else random.randint(100, 999999)} -->\n"

    pA = (120, 50)
    pB = (340, 50)
    pC = (280, 200)
    pD = (60, 200)

    slant_svg = ""
    if slant_lbl:
        slant_svg = f'<text x="{(pA[0]+pD[0])/2 - 25}" y="{(pA[1]+pD[1])/2}" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#059669">{slant_lbl}</text>'

    return f"""{salt}<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" height="100%">
  <rect width="{w}" height="{h}" fill="#f8fafc" rx="8"/>
  <polygon points="{pA[0]},{pA[1]} {pB[0]},{pB[1]} {pC[0]},{pC[1]} {pD[0]},{pD[1]}" fill="#f0fdf4" stroke="#16a34a" stroke-width="2.5" stroke-linejoin="round"/>
  <!-- Height line from pA down to base -->
  <line x1="{pA[0]}" y1="{pA[1]}" x2="{pA[0]}" y2="{pD[1]}" stroke="#dc2626" stroke-width="2" stroke-dasharray="4,4"/>
  <rect x="{pA[0]}" y="{pD[1] - 12}" width="12" height="12" fill="none" stroke="#dc2626" stroke-width="1.5"/>
  <text x="{pA[0] + 8}" y="{(pA[1]+pD[1])/2}" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#dc2626">h = {height_lbl}</text>
  <text x="{(pD[0]+pC[0])/2}" y="{pD[1] + 24}" text-anchor="middle" font-family="system-ui, sans-serif" font-size="13" font-weight="700" fill="#1e293b">base = {base_lbl}</text>
  {slant_svg}
</svg>"""


def draw_trapezium_with_height_svg(
    top_lbl: str,
    bottom_lbl: str,
    height_lbl: str,
    seed: Optional[int] = None,
) -> str:
    """Draw a trapezium with top base, bottom base, and perpendicular height."""
    w, h = 400, 250
    salt = f"<!-- seed:{seed if seed is not None else random.randint(100, 999999)} -->\n"

    pA = (130, 50)
    pB = (270, 50)
    pC = (350, 200)
    pD = (50, 200)

    return f"""{salt}<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" height="100%">
  <rect width="{w}" height="{h}" fill="#f8fafc" rx="8"/>
  <polygon points="{pA[0]},{pA[1]} {pB[0]},{pB[1]} {pC[0]},{pC[1]} {pD[0]},{pD[1]}" fill="#fefce8" stroke="#ca8a04" stroke-width="2.5" stroke-linejoin="round"/>
  <!-- Height line -->
  <line x1="{pA[0]}" y1="{pA[1]}" x2="{pA[0]}" y2="{pD[1]}" stroke="#dc2626" stroke-width="2" stroke-dasharray="4,4"/>
  <rect x="{pA[0]}" y="{pD[1] - 12}" width="12" height="12" fill="none" stroke="#dc2626" stroke-width="1.5"/>
  <text x="{pA[0] + 8}" y="{(pA[1]+pD[1])/2}" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#dc2626">h = {height_lbl}</text>
  <text x="{(pA[0]+pB[0])/2}" y="{pA[1] - 12}" text-anchor="middle" font-family="system-ui, sans-serif" font-size="13" font-weight="700" fill="#1e293b">a = {top_lbl}</text>
  <text x="{(pD[0]+pC[0])/2}" y="{pD[1] + 24}" text-anchor="middle" font-family="system-ui, sans-serif" font-size="13" font-weight="700" fill="#1e293b">b = {bottom_lbl}</text>
</svg>"""


def draw_l_shaped_polygon_svg(
    w_tot: str,
    h_tot: str,
    w_cut: str,
    h_cut: str,
    seed: Optional[int] = None,
) -> str:
    """Draw an L-shaped composite polygon with boundary dimension labels."""
    w, h = 380, 280
    salt = f"<!-- seed:{seed if seed is not None else random.randint(100, 999999)} -->\n"

    # L-shape vertices
    # (60, 40) -> (180, 40) -> (180, 140) -> (320, 140) -> (320, 230) -> (60, 230)
    pts = "60,40 180,40 180,140 320,140 320,230 60,230"

    return f"""{salt}<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" height="100%">
  <rect width="{w}" height="{h}" fill="#f8fafc" rx="8"/>
  <polygon points="{pts}" fill="#f5f3ff" stroke="#7c3aed" stroke-width="2.5" stroke-linejoin="round"/>
  <!-- Dimensions -->
  <text x="35" y="135" text-anchor="middle" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#1e293b">{h_tot}</text>
  <text x="190" y="250" text-anchor="middle" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#1e293b">{w_tot}</text>
  <text x="120" y="30" text-anchor="middle" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#1e293b">{w_cut}</text>
  <text x="340" y="185" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#1e293b">{h_cut}</text>
</svg>"""


def draw_shaded_square_circle_svg(
    side_lbl: str,
    rad_lbl: str,
    seed: Optional[int] = None,
) -> str:
    """Draw a square with an inscribed circle; shaded region between them."""
    w, h = 340, 280
    salt = f"<!-- seed:{seed if seed is not None else random.randint(100, 999999)} -->\n"
    sq_x, sq_y, s = 60, 30, 200
    cx, cy, r = sq_x + s / 2, sq_y + s / 2, s / 2

    return f"""{salt}<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" height="100%">
  <rect width="{w}" height="{h}" fill="#f8fafc" rx="8"/>
  <!-- Shaded outer square -->
  <rect x="{sq_x}" y="{sq_y}" width="{s}" height="{s}" fill="#fed7aa" stroke="#ea580c" stroke-width="2.5"/>
  <!-- Unshaded inner circle -->
  <circle cx="{cx}" cy="{cy}" r="{r}" fill="#ffffff" stroke="#ea580c" stroke-width="2.5"/>
  <!-- Center dot and radius -->
  <circle cx="{cx}" cy="{cy}" r="3.5" fill="#0f172a"/>
  <line x1="{cx}" y1="{cy}" x2="{cx + r}" y2="{cy}" stroke="#2563eb" stroke-width="2"/>
  <text x="{cx + r/2}" y="{cy - 8}" text-anchor="middle" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#2563eb">r = {rad_lbl}</text>
  <text x="{sq_x + s/2}" y="{sq_y + s + 22}" text-anchor="middle" font-family="system-ui, sans-serif" font-size="13" font-weight="700" fill="#1e293b">side = {side_lbl}</text>
</svg>"""


def draw_annulus_ring_svg(
    big_r_lbl: str,
    small_r_lbl: str,
    seed: Optional[int] = None,
) -> str:
    """Draw an annulus (ring between two concentric circles)."""
    w, h = 340, 260
    salt = f"<!-- seed:{seed if seed is not None else random.randint(100, 999999)} -->\n"
    cx, cy = 170, 130
    R, r = 90, 50

    return f"""{salt}<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" height="100%">
  <rect width="{w}" height="{h}" fill="#f8fafc" rx="8"/>
  <!-- Outer circle shaded -->
  <circle cx="{cx}" cy="{cy}" r="{R}" fill="#e0e7ff" stroke="#4338ca" stroke-width="2.5"/>
  <!-- Inner circle white -->
  <circle cx="{cx}" cy="{cy}" r="{r}" fill="#ffffff" stroke="#4338ca" stroke-width="2"/>
  <circle cx="{cx}" cy="{cy}" r="3.5" fill="#0f172a"/>
  <!-- Radii lines -->
  <line x1="{cx}" y1="{cy}" x2="{cx + r}" y2="{cy}" stroke="#dc2626" stroke-width="2"/>
  <line x1="{cx}" y1="{cy}" x2="{cx}" y2="{cy - R}" stroke="#2563eb" stroke-width="2"/>
  <text x="{cx + r/2}" y="{cy + 16}" text-anchor="middle" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#dc2626">r = {small_r_lbl}</text>
  <text x="{cx - 15}" y="{cy - R/2}" text-anchor="end" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#2563eb">R = {big_r_lbl}</text>
</svg>"""
