"""Reusable SVG drawing helpers for Grade 8 Mathematics - Geometry of 2D Shapes.
Produces crisp, publication-grade, accessible SVG diagrams parameterized by geometry and seed.
"""
from __future__ import annotations

import math
import random
from typing import Dict, List, Optional, Tuple


def draw_triangle_svg(
    ang_a: float,
    ang_b: float,
    ang_c: float,
    vertex_labels: Tuple[str, str, str] = ("A", "B", "C"),
    angle_labels: Optional[Dict[str, str]] = None,
    side_labels: Optional[Dict[str, str]] = None,
    ext_angle: Optional[Tuple[str, str]] = None,  # e.g. ("B", "4x + 10°")
    seed: Optional[int] = None,
) -> str:
    """Draw a triangle with base along bottom, vertex A at top, B at bottom-left, C at bottom-right."""
    w, h = 420, 280
    salt = f"<!-- seed:{seed if seed is not None else random.randint(100, 999999)} -->\n"

    # Vertices
    # B at bottom-left, C at bottom-right
    bx, by = 60, 220
    cx, cy = 340, 220
    base_len = cx - bx

    # Triangle angles: ang_b at B, ang_c at C, ang_a at A
    rad_b = math.radians(ang_b)
    rad_c = math.radians(ang_c)
    # Using sine rule: side_c / sin(C) = base / sin(A) -> side_c = base * sin(C) / sin(A)
    rad_a = math.radians(ang_a)
    sin_a = max(0.01, math.sin(rad_a))
    side_c = base_len * math.sin(rad_c) / sin_a

    ax = bx + side_c * math.cos(rad_b)
    ay = by - side_c * math.sin(rad_b)

    # Ensure A is clamped comfortably inside the canvas
    ax = max(40, min(380, ax))
    ay = max(40, min(140, ay))

    va, vb, vc = vertex_labels

    # Extra line for exterior angle if requested at B or C
    ext_path = ""
    if ext_angle:
        v_ext, ext_text = ext_angle
        if v_ext == "C":
            # Extend BC to D
            dx, dy = cx + 60, cy
            ext_path = f'<line x1="{cx}" y1="{cy}" x2="{dx}" y2="{dy}" stroke="#0f172a" stroke-width="2" stroke-dasharray="4,4"/>'
            ext_path += f'<text x="{dx + 5}" y="{dy + 5}" font-family="system-ui, sans-serif" font-size="12" font-weight="600" fill="#0f172a">D</text>'
            ext_path += f'<text x="{cx + 15}" y="{cy - 12}" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#2563eb">{ext_text}</text>'

    # Angle labels
    ang_svg = ""
    if angle_labels:
        if va in angle_labels:
            ang_svg += f'<text x="{ax}" y="{ay + 25}" text-anchor="middle" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#2563eb">{angle_labels[va]}</text>'
        if vb in angle_labels:
            ang_svg += f'<text x="{bx + 30}" y="{by - 10}" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#2563eb">{angle_labels[vb]}</text>'
        if vc in angle_labels:
            ang_svg += f'<text x="{cx - 30}" y="{cy - 10}" text-anchor="end" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#2563eb">{angle_labels[vc]}</text>'

    # Side labels
    side_svg = ""
    if side_labels:
        if "c" in side_labels or "AB" in side_labels:
            txt = side_labels.get("c") or side_labels.get("AB")
            mx, my = (ax + bx) / 2 - 15, (ay + by) / 2
            side_svg += f'<text x="{mx}" y="{my}" font-family="system-ui, sans-serif" font-size="12" font-weight="600" fill="#059669">{txt}</text>'
        if "b" in side_labels or "AC" in side_labels:
            txt = side_labels.get("b") or side_labels.get("AC")
            mx, my = (ax + cx) / 2 + 10, (ay + cy) / 2
            side_svg += f'<text x="{mx}" y="{my}" font-family="system-ui, sans-serif" font-size="12" font-weight="600" fill="#059669">{txt}</text>'
        if "a" in side_labels or "BC" in side_labels:
            txt = side_labels.get("a") or side_labels.get("BC")
            mx, my = (bx + cx) / 2, by + 18
            side_svg += f'<text x="{mx}" y="{my}" text-anchor="middle" font-family="system-ui, sans-serif" font-size="12" font-weight="600" fill="#059669">{txt}</text>'

    svg = f"""{salt}<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" height="100%">
  <rect width="{w}" height="{h}" fill="#f8fafc" rx="8"/>
  {ext_path}
  <polygon points="{ax:.1f},{ay:.1f} {bx:.1f},{by:.1f} {cx:.1f},{cy:.1f}" fill="#eff6ff" stroke="#1e293b" stroke-width="2.5" stroke-linejoin="round"/>
  <!-- Vertices -->
  <circle cx="{ax:.1f}" cy="{ay:.1f}" r="4" fill="#0f172a"/>
  <circle cx="{bx:.1f}" cy="{by:.1f}" r="4" fill="#0f172a"/>
  <circle cx="{cx:.1f}" cy="{cy:.1f}" r="4" fill="#0f172a"/>
  <text x="{ax:.1f}" y="{ay - 10:.1f}" text-anchor="middle" font-family="system-ui, sans-serif" font-size="14" font-weight="700" fill="#0f172a">{va}</text>
  <text x="{bx - 12:.1f}" y="{by + 16:.1f}" font-family="system-ui, sans-serif" font-size="14" font-weight="700" fill="#0f172a">{vb}</text>
  <text x="{cx + 12:.1f}" y="{cy + 16:.1f}" font-family="system-ui, sans-serif" font-size="14" font-weight="700" fill="#0f172a">{vc}</text>
  {ang_svg}
  {side_svg}
</svg>"""
    return svg


def draw_quadrilateral_svg(
    kind: str = "parallelogram",
    labels: Optional[Dict[str, str]] = None,
    angles: Optional[Dict[str, str]] = None,
    vertices: Tuple[str, str, str, str] = ("A", "B", "C", "D"),
    draw_diagonals: bool = False,
    seed: Optional[int] = None,
) -> str:
    """Draw a quadrilateral (parallelogram, rectangle, rhombus, square, trapezium, kite)."""
    w, h = 420, 280
    salt = f"<!-- seed:{seed if seed is not None else random.randint(100, 999999)} -->\n"

    # Default vertex positions
    if kind == "parallelogram":
        pA = (120, 60)
        pB = (340, 60)
        pC = (280, 210)
        pD = (60, 210)
    elif kind == "rectangle":
        pA = (80, 60)
        pB = (340, 60)
        pC = (340, 210)
        pD = (80, 210)
    elif kind == "square":
        pA = (130, 60)
        pB = (280, 60)
        pC = (280, 210)
        pD = (130, 210)
    elif kind == "rhombus":
        pA = (210, 50)
        pB = (330, 135)
        pC = (210, 220)
        pD = (90, 135)
    elif kind == "trapezium":
        pA = (130, 65)
        pB = (280, 65)
        pC = (350, 210)
        pD = (60, 210)
    elif kind == "kite":
        pA = (210, 45)
        pB = (310, 115)
        pC = (210, 235)
        pD = (110, 115)
    else:
        # General quadrilateral
        pA = (110, 65)
        pB = (320, 75)
        pC = (290, 215)
        pD = (75, 200)

    vA, vB, vC, vD = vertices

    diag_svg = ""
    if draw_diagonals:
        diag_svg = f"""
  <line x1="{pA[0]}" y1="{pA[1]}" x2="{pC[0]}" y2="{pC[1]}" stroke="#64748b" stroke-width="1.8" stroke-dasharray="4,4"/>
  <line x1="{pB[0]}" y1="{pB[1]}" x2="{pD[0]}" y2="{pD[1]}" stroke="#64748b" stroke-width="1.8" stroke-dasharray="4,4"/>
"""

    side_svg = ""
    if labels:
        if "top" in labels or "AB" in labels:
            txt = labels.get("top") or labels.get("AB")
            mx, my = (pA[0] + pB[0]) / 2, (pA[1] + pB[1]) / 2 - 10
            side_svg += f'<text x="{mx}" y="{my}" text-anchor="middle" font-family="system-ui, sans-serif" font-size="12" font-weight="600" fill="#059669">{txt}</text>'
        if "bottom" in labels or "DC" in labels:
            txt = labels.get("bottom") or labels.get("DC")
            mx, my = (pD[0] + pC[0]) / 2, (pD[1] + pC[1]) / 2 + 18
            side_svg += f'<text x="{mx}" y="{my}" text-anchor="middle" font-family="system-ui, sans-serif" font-size="12" font-weight="600" fill="#059669">{txt}</text>'
        if "left" in labels or "AD" in labels:
            txt = labels.get("left") or labels.get("AD")
            mx, my = (pA[0] + pD[0]) / 2 - 16, (pA[1] + pD[1]) / 2
            side_svg += f'<text x="{mx}" y="{my}" font-family="system-ui, sans-serif" font-size="12" font-weight="600" fill="#059669">{txt}</text>'
        if "right" in labels or "BC" in labels:
            txt = labels.get("right") or labels.get("BC")
            mx, my = (pB[0] + pC[0]) / 2 + 12, (pB[1] + pC[1]) / 2
            side_svg += f'<text x="{mx}" y="{my}" font-family="system-ui, sans-serif" font-size="12" font-weight="600" fill="#059669">{txt}</text>'

    ang_svg = ""
    if angles:
        if vA in angles:
            ang_svg += f'<text x="{pA[0] + 15}" y="{pA[1] + 20}" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#2563eb">{angles[vA]}</text>'
        if vB in angles:
            ang_svg += f'<text x="{pB[0] - 25}" y="{pB[1] + 20}" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#2563eb">{angles[vB]}</text>'
        if vC in angles:
            ang_svg += f'<text x="{pC[0] - 25}" y="{pC[1] - 12}" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#2563eb">{angles[vC]}</text>'
        if vD in angles:
            ang_svg += f'<text x="{pD[0] + 18}" y="{pD[1] - 12}" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#2563eb">{angles[vD]}</text>'

    svg = f"""{salt}<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" height="100%">
  <rect width="{w}" height="{h}" fill="#f8fafc" rx="8"/>
  <polygon points="{pA[0]},{pA[1]} {pB[0]},{pB[1]} {pC[0]},{pC[1]} {pD[0]},{pD[1]}" fill="#f0fdf4" stroke="#166534" stroke-width="2.5" stroke-linejoin="round"/>
  {diag_svg}
  <circle cx="{pA[0]}" cy="{pA[1]}" r="4" fill="#0f172a"/>
  <circle cx="{pB[0]}" cy="{pB[1]}" r="4" fill="#0f172a"/>
  <circle cx="{pC[0]}" cy="{pC[1]}" r="4" fill="#0f172a"/>
  <circle cx="{pD[0]}" cy="{pD[1]}" r="4" fill="#0f172a"/>
  <text x="{pA[0] - 12}" y="{pA[1] - 8}" font-family="system-ui, sans-serif" font-size="14" font-weight="700" fill="#0f172a">{vA}</text>
  <text x="{pB[0] + 10}" y="{pB[1] - 8}" font-family="system-ui, sans-serif" font-size="14" font-weight="700" fill="#0f172a">{vB}</text>
  <text x="{pC[0] + 10}" y="{pC[1] + 16}" font-family="system-ui, sans-serif" font-size="14" font-weight="700" fill="#0f172a">{vC}</text>
  <text x="{pD[0] - 15}" y="{pD[1] + 16}" font-family="system-ui, sans-serif" font-size="14" font-weight="700" fill="#0f172a">{vD}</text>
  {ang_svg}
  {side_svg}
</svg>"""
    return svg


def draw_circle_svg(
    radius_val: Optional[float] = None,
    diameter_val: Optional[float] = None,
    highlight: str = "radius",  # 'radius', 'diameter', 'chord', 'tangent', 'sector'
    seed: Optional[int] = None,
) -> str:
    """Draw a circle highlighting a specific feature (radius, diameter, chord, tangent)."""
    w, h = 360, 260
    salt = f"<!-- seed:{seed if seed is not None else random.randint(100, 999999)} -->\n"
    cx, cy, r = 180, 130, 90

    feature_svg = ""
    label_txt = ""

    if highlight == "radius":
        rad_label = f"r = {radius_val} cm" if radius_val else "Radius (r)"
        feature_svg = f"""
  <line x1="{cx}" y1="{cy}" x2="{cx + r}" y2="{cy}" stroke="#2563eb" stroke-width="3"/>
  <circle cx="{cx + r}" cy="{cy}" r="3.5" fill="#2563eb"/>
  <text x="{cx + r/2}" y="{cy - 8}" text-anchor="middle" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#2563eb">{rad_label}</text>
"""
    elif highlight == "diameter":
        dia_label = f"d = {diameter_val} cm" if diameter_val else "Diameter (d)"
        feature_svg = f"""
  <line x1="{cx - r}" y1="{cy}" x2="{cx + r}" y2="{cy}" stroke="#dc2626" stroke-width="3"/>
  <circle cx="{cx - r}" cy="{cy}" r="3.5" fill="#dc2626"/>
  <circle cx="{cx + r}" cy="{cy}" r="3.5" fill="#dc2626"/>
  <text x="{cx}" y="{cy - 10}" text-anchor="middle" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#dc2626">{dia_label}</text>
"""
    elif highlight == "chord":
        # Chord from 10 o'clock to 2 o'clock
        x1, y1 = cx - 65, cy - 62
        x2, y2 = cx + 75, cy - 50
        feature_svg = f"""
  <line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#7c3aed" stroke-width="3"/>
  <circle cx="{x1}" cy="{y1}" r="3.5" fill="#7c3aed"/>
  <circle cx="{x2}" cy="{y2}" r="3.5" fill="#7c3aed"/>
  <text x="{(x1+x2)/2}" y="{((y1+y2)/2) - 8}" text-anchor="middle" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#7c3aed">Chord</text>
"""
    elif highlight == "tangent":
        # Tangent at top of circle (0, -r)
        tx, ty = cx, cy - r
        feature_svg = f"""
  <line x1="{tx - 100}" y1="{ty}" x2="{tx + 100}" y2="{ty}" stroke="#d97706" stroke-width="3"/>
  <circle cx="{tx}" cy="{ty}" r="4" fill="#d97706"/>
  <line x1="{cx}" y1="{cy}" x2="{tx}" y2="{ty}" stroke="#64748b" stroke-width="1.8" stroke-dasharray="3,3"/>
  <text x="{tx + 40}" y="{ty - 10}" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#d97706">Tangent line</text>
  <rect x="{tx}" y="{ty}" width="10" height="10" fill="none" stroke="#0f172a" stroke-width="1.5"/>
"""
    elif highlight == "sector":
        # Sector with central angle 60 deg
        p1x = cx + r * math.cos(math.radians(-30))
        p1y = cy + r * math.sin(math.radians(-30))
        p2x = cx + r * math.cos(math.radians(30))
        p2y = cy + r * math.sin(math.radians(30))
        feature_svg = f"""
  <path d="M {cx} {cy} L {p1x:.1f} {p1y:.1f} A {r} {r} 0 0 1 {p2x:.1f} {p2y:.1f} Z" fill="#fed7aa" stroke="#ea580c" stroke-width="2"/>
  <text x="{cx + 40}" y="{cy + 5}" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#c2410c">Sector</text>
"""

    svg = f"""{salt}<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" height="100%">
  <rect width="{w}" height="{h}" fill="#f8fafc" rx="8"/>
  <circle cx="{cx}" cy="{cy}" r="{r}" fill="#f1f5f9" stroke="#334155" stroke-width="2.5"/>
  <circle cx="{cx}" cy="{cy}" r="4" fill="#0f172a"/>
  <text x="{cx - 8}" y="{cy + 16}" font-family="system-ui, sans-serif" font-size="13" font-weight="700" fill="#0f172a">O</text>
  {feature_svg}
</svg>"""
    return svg


def draw_regular_polygon_svg(
    n_sides: int = 5,
    side_len: Optional[str] = None,
    interior_angle: Optional[str] = None,
    seed: Optional[int] = None,
) -> str:
    """Draw a regular polygon (pentagon, hexagon, octagon, etc.)."""
    w, h = 360, 280
    salt = f"<!-- seed:{seed if seed is not None else random.randint(100, 999999)} -->\n"
    cx, cy, r = 180, 140, 95

    points = []
    # Rotate so a flat base or apex is aesthetic
    start_ang = -90 if n_sides % 2 != 0 else -90 + (180 / n_sides)
    for i in range(n_sides):
        ang = math.radians(start_ang + i * (360 / n_sides))
        px = cx + r * math.cos(ang)
        py = cy + r * math.sin(ang)
        points.append(f"{px:.1f},{py:.1f}")

    poly_pts = " ".join(points)
    info_svg = ""
    if interior_angle:
        info_svg += f'<text x="{cx}" y="{cy}" text-anchor="middle" font-family="system-ui, sans-serif" font-size="13" font-weight="700" fill="#1e40af">{interior_angle}</text>'
    if side_len:
        info_svg += f'<text x="{cx}" y="{cy + 115}" text-anchor="middle" font-family="system-ui, sans-serif" font-size="12" font-weight="600" fill="#059669">{side_len}</text>'

    svg = f"""{salt}<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" height="100%">
  <rect width="{w}" height="{h}" fill="#f8fafc" rx="8"/>
  <polygon points="{poly_pts}" fill="#e0e7ff" stroke="#4338ca" stroke-width="2.5" stroke-linejoin="round"/>
  {info_svg}
</svg>"""
    return svg


def draw_similar_triangles_svg(
    scale: float = 1.5,
    labels1: Optional[Dict[str, str]] = None,
    labels2: Optional[Dict[str, str]] = None,
    v1: Tuple[str, str, str] = ("A", "B", "C"),
    v2: Tuple[str, str, str] = ("D", "E", "F"),
    seed: Optional[int] = None,
) -> str:
    """Draw two similar triangles side by side."""
    w, h = 500, 260
    salt = f"<!-- seed:{seed if seed is not None else random.randint(100, 999999)} -->\n"

    # Small triangle on left
    t1_A = (80, 70)
    t1_B = (40, 200)
    t1_C = (160, 200)

    # Large triangle on right
    # Scaled
    dx = 280
    t2_A = (dx + 80 * scale * 0.7, 50)
    t2_B = (dx, 220)
    t2_C = (dx + 160 * scale * 0.7, 220)

    lbl_svg1 = ""
    if labels1:
        if "base" in labels1:
            lbl_svg1 += f'<text x="{(t1_B[0]+t1_C[0])/2}" y="{t1_B[1]+16}" text-anchor="middle" font-size="11" font-weight="700" fill="#059669">{labels1["base"]}</text>'
        if "left" in labels1:
            lbl_svg1 += f'<text x="{(t1_A[0]+t1_B[0])/2 - 12}" y="{(t1_A[1]+t1_B[1])/2}" font-size="11" font-weight="700" fill="#059669">{labels1["left"]}</text>'
        if "right" in labels1:
            lbl_svg1 += f'<text x="{(t1_A[0]+t1_C[0])/2 + 10}" y="{(t1_A[1]+t1_C[1])/2}" font-size="11" font-weight="700" fill="#059669">{labels1["right"]}</text>'

    lbl_svg2 = ""
    if labels2:
        if "base" in labels2:
            lbl_svg2 += f'<text x="{(t2_B[0]+t2_C[0])/2}" y="{t2_B[1]+18}" text-anchor="middle" font-size="12" font-weight="700" fill="#2563eb">{labels2["base"]}</text>'
        if "left" in labels2:
            lbl_svg2 += f'<text x="{(t2_A[0]+t2_B[0])/2 - 15}" y="{(t2_A[1]+t2_B[1])/2}" font-size="12" font-weight="700" fill="#2563eb">{labels2["left"]}</text>'
        if "right" in labels2:
            lbl_svg2 += f'<text x="{(t2_A[0]+t2_C[0])/2 + 12}" y="{(t2_A[1]+t2_C[1])/2}" font-size="12" font-weight="700" fill="#2563eb">{labels2["right"]}</text>'

    svg = f"""{salt}<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" height="100%">
  <rect width="{w}" height="{h}" fill="#f8fafc" rx="8"/>
  <!-- Triangle 1 -->
  <polygon points="{t1_A[0]},{t1_A[1]} {t1_B[0]},{t1_B[1]} {t1_C[0]},{t1_C[1]}" fill="#eff6ff" stroke="#1d4ed8" stroke-width="2.2" stroke-linejoin="round"/>
  <text x="{t1_A[0]}" y="{t1_A[1]-8}" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a">{v1[0]}</text>
  <text x="{t1_B[0]-10}" y="{t1_B[1]+14}" font-size="13" font-weight="700" fill="#0f172a">{v1[1]}</text>
  <text x="{t1_C[0]+10}" y="{t1_C[1]+14}" font-size="13" font-weight="700" fill="#0f172a">{v1[2]}</text>
  {lbl_svg1}

  <!-- Triangle 2 -->
  <polygon points="{t2_A[0]:.1f},{t2_A[1]:.1f} {t2_B[0]:.1f},{t2_B[1]:.1f} {t2_C[0]:.1f},{t2_C[1]:.1f}" fill="#fdf2f8" stroke="#be185d" stroke-width="2.5" stroke-linejoin="round"/>
  <text x="{t2_A[0]:.1f}" y="{t2_A[1]-8:.1f}" text-anchor="middle" font-size="14" font-weight="700" fill="#0f172a">{v2[0]}</text>
  <text x="{t2_B[0]-12:.1f}" y="{t2_B[1]+16:.1f}" font-size="14" font-weight="700" fill="#0f172a">{v2[1]}</text>
  <text x="{t2_C[0]+12:.1f}" y="{t2_C[1]+16:.1f}" font-size="14" font-weight="700" fill="#0f172a">{v2[2]}</text>
  {lbl_svg2}
</svg>"""
    return svg
