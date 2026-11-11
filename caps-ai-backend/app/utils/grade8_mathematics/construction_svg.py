"""Reusable SVG drawing helpers for Grade 8 Mathematics - Construction of Geometric Figures.
Produces publication-grade, crisp vector construction diagrams showing authentic compass arc marks.
"""
from __future__ import annotations

import math
import random
from typing import Dict, List, Optional, Tuple


def draw_perp_bisector_svg(
    seg_name: str = "AB",
    length_lbl: Optional[str] = None,
    seed: Optional[int] = None,
) -> str:
    """Draw a horizontal segment AB with compass construction arcs above and below and perpendicular bisector line."""
    w, h = 420, 260
    salt = f"<!-- seed:{seed if seed is not None else random.randint(100, 999999)} -->\n"

    ax, ay = 80, 130
    bx, by = 340, 130
    mx, my = (ax + bx) / 2, (ay + by) / 2

    v1, v2 = seg_name[0], seg_name[1] if len(seg_name) > 1 else "B"

    len_svg = ""
    if length_lbl:
        len_svg = f'<text x="{mx}" y="{my + 22}" text-anchor="middle" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#1e293b">{length_lbl}</text>'

    return f"""{salt}<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" height="100%">
  <rect width="{w}" height="{h}" fill="#f8fafc" rx="8"/>
  <!-- Base segment AB -->
  <line x1="{ax}" y1="{ay}" x2="{bx}" y2="{by}" stroke="#0f172a" stroke-width="2.5"/>
  <circle cx="{ax}" cy="{ay}" r="4" fill="#0f172a"/>
  <circle cx="{bx}" cy="{by}" r="4" fill="#0f172a"/>
  <text x="{ax - 14}" y="{ay + 5}" font-family="system-ui, sans-serif" font-size="14" font-weight="700" fill="#0f172a">{v1}</text>
  <text x="{bx + 8}" y="{ay + 5}" font-family="system-ui, sans-serif" font-size="14" font-weight="700" fill="#0f172a">{v2}</text>
  {len_svg}

  <!-- Construction arcs top intersection -->
  <path d="M {mx - 25} 35 A 160 160 0 0 1 {mx + 25} 55" fill="none" stroke="#2563eb" stroke-width="1.8" stroke-dasharray="2,2"/>
  <path d="M {mx + 25} 35 A 160 160 0 0 0 {mx - 25} 55" fill="none" stroke="#2563eb" stroke-width="1.8" stroke-dasharray="2,2"/>
  <circle cx="{mx}" cy="45" r="3" fill="#2563eb"/>
  <text x="{mx + 8}" y="42" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#2563eb">P</text>

  <!-- Construction arcs bottom intersection -->
  <path d="M {mx - 25} 225 A 160 160 0 0 0 {mx + 25} 205" fill="none" stroke="#2563eb" stroke-width="1.8" stroke-dasharray="2,2"/>
  <path d="M {mx + 25} 225 A 160 160 0 0 1 {mx - 25} 205" fill="none" stroke="#2563eb" stroke-width="1.8" stroke-dasharray="2,2"/>
  <circle cx="{mx}" cy="215" r="3" fill="#2563eb"/>
  <text x="{mx + 8}" y="222" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#2563eb">Q</text>

  <!-- Perpendicular bisector line through P and Q -->
  <line x1="{mx}" y1="20" x2="{mx}" y2="240" stroke="#dc2626" stroke-width="2"/>
  <rect x="{mx}" y="{my - 12}" width="12" height="12" fill="none" stroke="#dc2626" stroke-width="1.5"/>
</svg>"""


def draw_angle_bisector_svg(
    angle_deg: int = 60,
    vertex_lbl: str = "B",
    arm1_lbl: str = "A",
    arm2_lbl: str = "C",
    seed: Optional[int] = None,
) -> str:
    """Draw an angle with arc on arms and intersecting secondary arcs showing bisector ray."""
    w, h = 400, 260
    salt = f"<!-- seed:{seed if seed is not None else random.randint(100, 999999)} -->\n"

    vx, vy = 80, 200
    arm_len = 240
    # Base arm horizontal
    c_x, c_y = vx + arm_len, vy
    # Upper arm at angle_deg
    rad = math.radians(angle_deg)
    a_x = vx + arm_len * math.cos(rad)
    a_y = vy - arm_len * math.sin(rad)

    # Bisector ray at angle_deg / 2
    bis_rad = math.radians(angle_deg / 2)
    bis_x = vx + (arm_len + 20) * math.cos(bis_rad)
    bis_y = vy - (arm_len + 20) * math.sin(bis_rad)

    # Arc across arms at r=90
    arc_r = 90
    arc_x1 = vx + arc_r
    arc_y1 = vy
    arc_x2 = vx + arc_r * math.cos(rad)
    arc_y2 = vy - arc_r * math.sin(rad)

    # Intersecting arcs center at (bis_r * cos, bis_r * sin)
    ix = vx + 160 * math.cos(bis_rad)
    iy = vy - 160 * math.sin(bis_rad)

    return f"""{salt}<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" height="100%">
  <rect width="{w}" height="{h}" fill="#f8fafc" rx="8"/>
  <!-- Arms of angle -->
  <line x1="{vx}" y1="{vy}" x2="{c_x}" y2="{c_y}" stroke="#0f172a" stroke-width="2.5"/>
  <line x1="{vx}" y1="{vy}" x2="{a_x}" y2="{a_y}" stroke="#0f172a" stroke-width="2.5"/>
  <circle cx="{vx}" cy="{vy}" r="4" fill="#0f172a"/>
  <text x="{vx - 16}" y="{vy + 6}" font-family="system-ui, sans-serif" font-size="14" font-weight="700" fill="#0f172a">{vertex_lbl}</text>
  <text x="{c_x + 8}" y="{c_y + 5}" font-family="system-ui, sans-serif" font-size="14" font-weight="700" fill="#0f172a">{arm2_lbl}</text>
  <text x="{a_x + 4}" y="{a_y - 6}" font-family="system-ui, sans-serif" font-size="14" font-weight="700" fill="#0f172a">{arm1_lbl}</text>

  <!-- Initial arc crossing arms -->
  <path d="M {arc_x1} {arc_y1} A {arc_r} {arc_r} 0 0 0 {arc_x2:.1f} {arc_y2:.1f}" fill="none" stroke="#2563eb" stroke-width="1.8" stroke-dasharray="3,3"/>
  <circle cx="{arc_x1}" cy="{arc_y1}" r="3" fill="#2563eb"/>
  <circle cx="{arc_x2:.1f}" cy="{arc_y2:.1f}" r="3" fill="#2563eb"/>

  <!-- Construction arcs intersection in the interior -->
  <circle cx="{ix:.1f}" cy="{iy:.1f}" r="3.5" fill="#dc2626"/>
  <text x="{ix + 8:.1f}" y="{iy - 6:.1f}" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#dc2626">D</text>

  <!-- Angle bisector ray -->
  <line x1="{vx}" y1="{vy}" x2="{bis_x:.1f}" y2="{bis_y:.1f}" stroke="#dc2626" stroke-width="2"/>
  <text x="{vx + 70}" y="{vy - 12}" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#dc2626">{angle_deg // 2}°</text>
  <text x="{vx + 50}" y="{vy - 45}" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#dc2626">{angle_deg // 2}°</text>
</svg>"""


def draw_constructed_triangle_arcs_svg(
    a_len: str,
    b_len: str,
    c_len: str,
    seed: Optional[int] = None,
) -> str:
    """Draw a triangle ABC constructed with ruler base BC and compass arcs from B and C intersecting at A."""
    w, h = 400, 260
    salt = f"<!-- seed:{seed if seed is not None else random.randint(100, 999999)} -->\n"

    bx, by = 70, 200
    cx, cy = 330, 200
    ax, ay = 180, 60

    return f"""{salt}<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" height="100%">
  <rect width="{w}" height="{h}" fill="#f8fafc" rx="8"/>
  <!-- Triangle sides -->
  <polygon points="{ax},{ay} {bx},{by} {cx},{cy}" fill="#eff6ff" stroke="#1d4ed8" stroke-width="2.2" stroke-linejoin="round"/>
  <!-- Compass arcs intersecting at A -->
  <path d="M {ax - 30} {ay + 15} A 180 180 0 0 1 {ax + 20} {ay - 20}" fill="none" stroke="#dc2626" stroke-width="1.8" stroke-dasharray="3,3"/>
  <path d="M {ax + 30} {ay + 15} A 190 190 0 0 0 {ax - 20} {ay - 20}" fill="none" stroke="#2563eb" stroke-width="1.8" stroke-dasharray="3,3"/>

  <!-- Vertices -->
  <circle cx="{ax}" cy="{ay}" r="4" fill="#0f172a"/>
  <circle cx="{bx}" cy="{by}" r="4" fill="#0f172a"/>
  <circle cx="{cx}" cy="{cy}" r="4" fill="#0f172a"/>
  <text x="{ax}" y="{ay - 12}" text-anchor="middle" font-family="system-ui, sans-serif" font-size="14" font-weight="700" fill="#0f172a">A</text>
  <text x="{bx - 12}" y="{by + 16}" font-family="system-ui, sans-serif" font-size="14" font-weight="700" fill="#0f172a">B</text>
  <text x="{cx + 12}" y="{cy + 16}" font-family="system-ui, sans-serif" font-size="14" font-weight="700" fill="#0f172a">C</text>

  <!-- Side labels -->
  <text x="{(bx + cx)/2}" y="{by + 20}" text-anchor="middle" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#059669">{a_len}</text>
  <text x="{(ax + bx)/2 - 18}" y="{(ay + by)/2}" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#059669">{c_len}</text>
  <text x="{(ax + cx)/2 + 15}" y="{(ay + cy)/2}" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#059669">{b_len}</text>
</svg>"""


def draw_special_angle_construction_svg(
    angle_deg: int = 60,
    seed: Optional[int] = None,
) -> str:
    """Draw a special angle (60°, 90°, 45°, 30°) construction on horizontal baseline with compass arc."""
    w, h = 380, 240
    salt = f"<!-- seed:{seed if seed is not None else random.randint(100, 999999)} -->\n"

    vx, vy = 80, 190
    base_x, base_y = 330, 190
    rad = math.radians(angle_deg)
    ray_len = 190
    ray_x = vx + ray_len * math.cos(rad)
    ray_y = vy - ray_len * math.sin(rad)

    arc_r = 100
    p1x = vx + arc_r
    p1y = vy

    # For 60 deg, second arc centered at p1 with radius arc_r intersects base arc at (vx + arc_r*cos60, vy - arc_r*sin60)
    ix = vx + arc_r * math.cos(rad)
    iy = vy - arc_r * math.sin(rad)

    return f"""{salt}<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" height="100%">
  <rect width="{w}" height="{h}" fill="#f8fafc" rx="8"/>
  <line x1="{vx}" y1="{vy}" x2="{base_x}" y2="{base_y}" stroke="#0f172a" stroke-width="2.5"/>
  <line x1="{vx}" y1="{vy}" x2="{ray_x:.1f}" y2="{ray_y:.1f}" stroke="#2563eb" stroke-width="2.5"/>
  <circle cx="{vx}" cy="{vy}" r="4" fill="#0f172a"/>
  <!-- Arcs -->
  <path d="M {p1x} {p1y} A {arc_r} {arc_r} 0 0 0 {vx + arc_r*math.cos(math.radians(max(angle_deg+20, 80))):.1f} {vy - arc_r*math.sin(math.radians(max(angle_deg+20, 80))):.1f}" fill="none" stroke="#64748b" stroke-width="1.8" stroke-dasharray="3,3"/>
  <circle cx="{ix:.1f}" cy="{iy:.1f}" r="3.5" fill="#dc2626"/>
  <!-- Label -->
  <text x="{vx - 14}" y="{vy + 6}" font-family="system-ui, sans-serif" font-size="14" font-weight="700" fill="#0f172a">O</text>
  <text x="{base_x + 8}" y="{base_y + 5}" font-family="system-ui, sans-serif" font-size="14" font-weight="700" fill="#0f172a">X</text>
  <text x="{ray_x + 6:.1f}" y="{ray_y - 6:.1f}" font-family="system-ui, sans-serif" font-size="14" font-weight="700" fill="#2563eb">Y</text>
  <text x="{vx + 45}" y="{vy - 16}" font-family="system-ui, sans-serif" font-size="13" font-weight="700" fill="#2563eb">{angle_deg}°</text>
</svg>"""
