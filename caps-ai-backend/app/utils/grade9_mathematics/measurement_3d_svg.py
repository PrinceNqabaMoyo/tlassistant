"""Grade 9 Mathematics - Measurement of 3D Objects SVG Builders (CAPS Term 4).
Renders publication-grade dimensioned 3D solids and nets for surface area, volume, and capacity.
Zero LLM calls, deterministic seed entropy.
"""
from __future__ import annotations

import math
from typing import Any, Dict, List, Optional


def draw_dimensioned_cube_svg(
    side: float | int,
    unit: str = "cm",
    seed: Optional[int] = None,
    width: int = 420,
    height: int = 360,
) -> str:
    s_tag = f"<!-- s:{seed} -->\n" if seed is not None else ""
    blender_plate = "/diagrams/blender_3d_cube_exam_stipple.jpg"
    blender_glb = "/models/blender_3d_cube.glb"
    w, h = float(width), float(height)
    cx, cy = w / 2.0, h / 2.0 + 10.0
    s_px = 110.0
    sx, sy = 60.0, -38.0

    ax, ay = cx - s_px / 2.0 - 25.0, cy + s_px / 2.0
    bx, by = ax + s_px, ay
    c_pt_x, c_pt_y = bx, ay - s_px
    dx, dy = ax, c_pt_y

    dim_str = f"{side} {unit}"

    return (
        f'{s_tag}<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
        f'width="{width}" height="{height}" data-blender-plate="{blender_plate}" data-model-glb="{blender_glb}" '
        f'style="background:#ffffff; font-family:system-ui,-apple-system,sans-serif;">\n'
        f'  <rect x="0" y="0" width="{width}" height="{height}" fill="#ffffff"/>\n'
        f'  <defs>\n'
        f'    <linearGradient id="c-top" x1="0%" y1="0%" x2="100%" y2="100%">\n'
        f'      <stop offset="0%" stop-color="#bfdbfe" stop-opacity="0.5"/>\n'
        f'      <stop offset="100%" stop-color="#93c5fd" stop-opacity="0.3"/>\n'
        f'    </linearGradient>\n'
        f'    <linearGradient id="c-side" x1="0%" y1="0%" x2="100%" y2="100%">\n'
        f'      <stop offset="0%" stop-color="#3b82f6" stop-opacity="0.35"/>\n'
        f'      <stop offset="100%" stop-color="#1d4ed8" stop-opacity="0.5"/>\n'
        f'    </linearGradient>\n'
        f'    <linearGradient id="c-front" x1="0%" y1="0%" x2="100%" y2="100%">\n'
        f'      <stop offset="0%" stop-color="#60a5fa" stop-opacity="0.3"/>\n'
        f'      <stop offset="100%" stop-color="#2563eb" stop-opacity="0.4"/>\n'
        f'    </linearGradient>\n'
        f'  </defs>\n'
        f'  <!-- Hidden edges -->\n'
        f'  <line x1="{ax}" y1="{ay}" x2="{ax + sx}" y2="{ay + sy}" stroke="#94a3b8" stroke-width="1.8" stroke-dasharray="4,4"/>\n'
        f'  <line x1="{ax + sx}" y1="{ay + sy}" x2="{bx + sx}" y2="{by + sy}" stroke="#94a3b8" stroke-width="1.8" stroke-dasharray="4,4"/>\n'
        f'  <line x1="{ax + sx}" y1="{ay + sy}" x2="{dx + sx}" y2="{dy + sy}" stroke="#94a3b8" stroke-width="1.8" stroke-dasharray="4,4"/>\n'
        f'  <!-- Visible faces -->\n'
        f'  <polygon points="{dx},{dy} {c_pt_x},{c_pt_y} {c_pt_x + sx},{c_pt_y + sy} {dx + sx},{dy + sy}" fill="url(#c-top)" stroke="#1e293b" stroke-width="2"/>\n'
        f'  <polygon points="{bx},{by} {c_pt_x},{c_pt_y} {c_pt_x + sx},{c_pt_y + sy} {bx + sx},{by + sy}" fill="url(#c-side)" stroke="#1e293b" stroke-width="2"/>\n'
        f'  <polygon points="{ax},{ay} {bx},{by} {c_pt_x},{c_pt_y} {dx},{dy}" fill="url(#c-front)" stroke="#1e293b" stroke-width="2"/>\n'
        f'  <!-- Dimension labels -->\n'
        f'  <text x="{(ax + bx)/2}" y="{ay + 22}" font-size="13" font-weight="bold" text-anchor="middle" fill="#0f172a">{dim_str}</text>\n'
        f'  <text x="{bx + sx/2 + 14}" y="{(by + by + sy)/2 + 14}" font-size="12" font-weight="bold" fill="#0f172a">{dim_str}</text>\n'
        f'  <text x="{dx - 14}" y="{(ay + dy)/2}" font-size="13" font-weight="bold" text-anchor="end" fill="#0f172a">{dim_str}</text>\n'
        f'  <text x="{cx}" y="26" font-size="14" font-weight="bold" text-anchor="middle" fill="#1e3a8a">Cube (All sides = {dim_str})</text>\n'
        f'</svg>'
    )


def draw_dimensioned_rectangular_prism_svg(
    length: float | int,
    width_val: float | int,
    height_val: float | int,
    unit: str = "cm",
    seed: Optional[int] = None,
    width: int = 440,
    height: int = 360,
) -> str:
    s_tag = f"<!-- s:{seed} -->\n" if seed is not None else ""
    blender_plate = "/diagrams/blender_3d_rectangular_prism_exam_stipple.jpg"
    blender_glb = "/models/blender_3d_rectangular_prism.glb"
    w, h = float(width), float(height)
    cx, cy = w / 2.0, h / 2.0 + 10.0
    l_px = 150.0
    h_px = 90.0
    sx, sy = 60.0, -36.0

    ax, ay = cx - l_px / 2.0 - 25.0, cy + h_px / 2.0
    bx, by = ax + l_px, ay
    c_pt_x, c_pt_y = bx, ay - h_px
    dx, dy = ax, c_pt_y

    return (
        f'{s_tag}<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
        f'width="{width}" height="{height}" data-blender-plate="{blender_plate}" data-model-glb="{blender_glb}" '
        f'style="background:#ffffff; font-family:system-ui,-apple-system,sans-serif;">\n'
        f'  <rect x="0" y="0" width="{width}" height="{height}" fill="#ffffff"/>\n'
        f'  <defs>\n'
        f'    <linearGradient id="rp-top" x1="0%" y1="0%" x2="100%" y2="100%">\n'
        f'      <stop offset="0%" stop-color="#fed7aa" stop-opacity="0.45"/>\n'
        f'      <stop offset="100%" stop-color="#fdba74" stop-opacity="0.3"/>\n'
        f'    </linearGradient>\n'
        f'    <linearGradient id="rp-side" x1="0%" y1="0%" x2="100%" y2="100%">\n'
        f'      <stop offset="0%" stop-color="#f97316" stop-opacity="0.35"/>\n'
        f'      <stop offset="100%" stop-color="#c2410c" stop-opacity="0.5"/>\n'
        f'    </linearGradient>\n'
        f'    <linearGradient id="rp-front" x1="0%" y1="0%" x2="100%" y2="100%">\n'
        f'      <stop offset="0%" stop-color="#fb923c" stop-opacity="0.35"/>\n'
        f'      <stop offset="100%" stop-color="#ea580c" stop-opacity="0.45"/>\n'
        f'    </linearGradient>\n'
        f'  </defs>\n'
        f'  <!-- Hidden edges -->\n'
        f'  <line x1="{ax}" y1="{ay}" x2="{ax + sx}" y2="{ay + sy}" stroke="#94a3b8" stroke-width="1.8" stroke-dasharray="4,4"/>\n'
        f'  <line x1="{ax + sx}" y1="{ay + sy}" x2="{bx + sx}" y2="{by + sy}" stroke="#94a3b8" stroke-width="1.8" stroke-dasharray="4,4"/>\n'
        f'  <line x1="{ax + sx}" y1="{ay + sy}" x2="{dx + sx}" y2="{dy + sy}" stroke="#94a3b8" stroke-width="1.8" stroke-dasharray="4,4"/>\n'
        f'  <!-- Faces -->\n'
        f'  <polygon points="{dx},{dy} {c_pt_x},{c_pt_y} {c_pt_x + sx},{c_pt_y + sy} {dx + sx},{dy + sy}" fill="url(#rp-top)" stroke="#1e293b" stroke-width="2"/>\n'
        f'  <polygon points="{bx},{by} {c_pt_x},{c_pt_y} {c_pt_x + sx},{c_pt_y + sy} {bx + sx},{by + sy}" fill="url(#rp-side)" stroke="#1e293b" stroke-width="2"/>\n'
        f'  <polygon points="{ax},{ay} {bx},{by} {c_pt_x},{c_pt_y} {dx},{dy}" fill="url(#rp-front)" stroke="#1e293b" stroke-width="2"/>\n'
        f'  <!-- Dimensions -->\n'
        f'  <text x="{(ax + bx)/2}" y="{ay + 22}" font-size="13" font-weight="bold" text-anchor="middle" fill="#0f172a">l = {length} {unit}</text>\n'
        f'  <text x="{bx + sx/2 + 12}" y="{(by + by + sy)/2 + 14}" font-size="12" font-weight="bold" fill="#0f172a">b = {width_val} {unit}</text>\n'
        f'  <text x="{dx - 12}" y="{(ay + dy)/2}" font-size="13" font-weight="bold" text-anchor="end" fill="#0f172a">h = {height_val} {unit}</text>\n'
        f'  <text x="{cx}" y="26" font-size="14" font-weight="bold" text-anchor="middle" fill="#9a3412">Rectangular Prism ({length} × {width_val} × {height_val} {unit})</text>\n'
        f'</svg>'
    )


def draw_dimensioned_triangular_prism_svg(
    base: float | int,
    tri_height: float | int,
    prism_length: float | int,
    hypotenuse: Optional[float | int] = None,
    unit: str = "cm",
    seed: Optional[int] = None,
    width: int = 440,
    height: int = 360,
) -> str:
    s_tag = f"<!-- s:{seed} -->\n" if seed is not None else ""
    blender_plate = "/diagrams/blender_3d_triangular_prism_exam_stipple.jpg"
    blender_glb = "/models/blender_3d_triangular_prism.glb"
    w, h = float(width), float(height)
    cx, cy = w / 2.0, h / 2.0 + 15.0

    b_px = 120.0
    h_px = 80.0
    sx, sy = 120.0, -45.0

    ax, ay = cx - b_px / 2.0 - 50.0, cy + 30.0
    bx, by = ax + b_px, ay
    tx, ty = ax, ay - h_px  # right-angled triangle at A

    ax_b, ay_b = ax + sx, ay + sy
    bx_b, by_b = bx + sx, by + sy
    tx_b, ty_b = tx + sx, ty + sy

    hyp_label = f"c = {hypotenuse} {unit}" if hypotenuse else ""

    return (
        f'{s_tag}<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
        f'width="{width}" height="{height}" data-blender-plate="{blender_plate}" data-model-glb="{blender_glb}" '
        f'style="background:#ffffff; font-family:system-ui,-apple-system,sans-serif;">\n'
        f'  <rect x="0" y="0" width="{width}" height="{height}" fill="#ffffff"/>\n'
        f'  <defs>\n'
        f'    <linearGradient id="tp-slant" x1="0%" y1="0%" x2="100%" y2="100%">\n'
        f'      <stop offset="0%" stop-color="#a7f3d0" stop-opacity="0.45"/>\n'
        f'      <stop offset="100%" stop-color="#34d399" stop-opacity="0.35"/>\n'
        f'    </linearGradient>\n'
        f'    <linearGradient id="tp-front" x1="0%" y1="0%" x2="100%" y2="100%">\n'
        f'      <stop offset="0%" stop-color="#10b981" stop-opacity="0.3"/>\n'
        f'      <stop offset="100%" stop-color="#059669" stop-opacity="0.45"/>\n'
        f'    </linearGradient>\n'
        f'  </defs>\n'
        f'  <!-- Hidden edges -->\n'
        f'  <line x1="{ax}" y1="{ay}" x2="{ax_b}" y2="{ay_b}" stroke="#94a3b8" stroke-width="1.8" stroke-dasharray="4,4"/>\n'
        f'  <line x1="{ax_b}" y1="{ay_b}" x2="{bx_b}" y2="{by_b}" stroke="#94a3b8" stroke-width="1.8" stroke-dasharray="4,4"/>\n'
        f'  <line x1="{ax_b}" y1="{ay_b}" x2="{tx_b}" y2="{ty_b}" stroke="#94a3b8" stroke-width="1.8" stroke-dasharray="4,4"/>\n'
        f'  <!-- Back triangle hypotenuse -->\n'
        f'  <line x1="{tx_b}" y1="{ty_b}" x2="{bx_b}" y2="{by_b}" stroke="#1e293b" stroke-width="2"/>\n'
        f'  <!-- Slanted rectangular face -->\n'
        f'  <polygon points="{tx},{ty} {bx},{by} {bx_b},{by_b} {tx_b},{ty_b}" fill="url(#tp-slant)" stroke="#1e293b" stroke-width="2"/>\n'
        f'  <!-- Front triangle -->\n'
        f'  <polygon points="{ax},{ay} {bx},{by} {tx},{ty}" fill="url(#tp-front)" stroke="#1e293b" stroke-width="2"/>\n'
        f'  <!-- Right angle marker at A -->\n'
        f'  <polyline points="{ax + 14},{ay} {ax + 14},{ay - 14} {ax},{ay - 14}" fill="none" stroke="#047857" stroke-width="1.8"/>\n'
        f'  <!-- Dimension labels -->\n'
        f'  <text x="{(ax + bx)/2}" y="{ay + 20}" font-size="13" font-weight="bold" text-anchor="middle" fill="#0f172a">b = {base} {unit}</text>\n'
        f'  <text x="{ax - 12}" y="{(ay + ty)/2}" font-size="13" font-weight="bold" text-anchor="end" fill="#0f172a">h = {tri_height} {unit}</text>\n'
        f'  <text x="{(bx + bx_b)/2 + 14}" y="{(by + by_b)/2 + 16}" font-size="12" font-weight="bold" fill="#0f172a">L = {prism_length} {unit}</text>\n'
        f'  <text x="{cx}" y="24" font-size="14" font-weight="bold" text-anchor="middle" fill="#047857">Right Triangular Prism</text>\n'
        f'</svg>'
    )


def draw_dimensioned_cylinder_svg(
    radius: float | int,
    height_val: float | int,
    unit: str = "cm",
    is_open_top: bool = False,
    seed: Optional[int] = None,
    width: int = 420,
    height: int = 360,
) -> str:
    s_tag = f"<!-- s:{seed} -->\n" if seed is not None else ""
    blender_plate = "/diagrams/blender_3d_cylinder_exam_stipple.jpg"
    blender_glb = "/models/blender_3d_cylinder.glb"
    w, h = float(width), float(height)
    cx, cy = w / 2.0, h / 2.0 + 8.0

    rx = 75.0
    ry = 22.0
    cyl_h = 140.0
    top_y = cy - cyl_h / 2.0
    bot_y = cy + cyl_h / 2.0

    top_fill = "#f1f5f9" if is_open_top else "#bfdbfe"
    top_stroke = "#64748b" if is_open_top else "#1d4ed8"
    tag_str = "Open at top" if is_open_top else "Closed cylinder"

    return (
        f'{s_tag}<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
        f'width="{width}" height="{height}" data-blender-plate="{blender_plate}" data-model-glb="{blender_glb}" '
        f'style="background:#ffffff; font-family:system-ui,-apple-system,sans-serif;">\n'
        f'  <rect x="0" y="0" width="{width}" height="{height}" fill="#ffffff"/>\n'
        f'  <defs>\n'
        f'    <linearGradient id="cyl-body" x1="0%" y1="0%" x2="100%" y2="0%">\n'
        f'      <stop offset="0%" stop-color="#93c5fd" stop-opacity="0.3"/>\n'
        f'      <stop offset="50%" stop-color="#3b82f6" stop-opacity="0.45"/>\n'
        f'      <stop offset="100%" stop-color="#1d4ed8" stop-opacity="0.6"/>\n'
        f'    </linearGradient>\n'
        f'  </defs>\n'
        f'  <!-- Body rectangle -->\n'
        f'  <rect x="{cx - rx}" y="{top_y}" width="{2*rx}" height="{cyl_h}" fill="url(#cyl-body)"/>\n'
        f'  <!-- Bottom ellipse: rear dashed, front solid -->\n'
        f'  <path d="M {cx - rx} {bot_y} A {rx} {ry} 0 0 1 {cx + rx} {bot_y}" fill="none" stroke="#94a3b8" stroke-width="1.8" stroke-dasharray="4,4"/>\n'
        f'  <path d="M {cx - rx} {bot_y} A {rx} {ry} 0 0 0 {cx + rx} {bot_y}" fill="none" stroke="#1e293b" stroke-width="2"/>\n'
        f'  <!-- Lateral sides -->\n'
        f'  <line x1="{cx - rx}" y1="{top_y}" x2="{cx - rx}" y2="{bot_y}" stroke="#1e293b" stroke-width="2"/>\n'
        f'  <line x1="{cx + rx}" y1="{top_y}" x2="{cx + rx}" y2="{bot_y}" stroke="#1e293b" stroke-width="2"/>\n'
        f'  <!-- Top ellipse -->\n'
        f'  <ellipse cx="{cx}" cy="{top_y}" rx="{rx}" ry="{ry}" fill="{top_fill}" stroke="{top_stroke}" stroke-width="2"/>\n'
        f'  <!-- Center dot and radius line on top -->\n'
        f'  <circle cx="{cx}" cy="{top_y}" r="3" fill="#dc2626"/>\n'
        f'  <line x1="{cx}" y1="{top_y}" x2="{cx + rx}" y2="{top_y}" stroke="#dc2626" stroke-width="2" stroke-dasharray="3,2"/>\n'
        f'  <text x="{cx + rx/2}" y="{top_y - 8}" font-size="12" font-weight="bold" fill="#dc2626">r = {radius} {unit}</text>\n'
        f'  <!-- Height dimension line on left -->\n'
        f'  <line x1="{cx - rx - 20}" y1="{top_y}" x2="{cx - rx - 20}" y2="{bot_y}" stroke="#0f172a" stroke-width="1.8"/>\n'
        f'  <polyline points="{cx - rx - 24},{top_y + 8} {cx - rx - 20},{top_y} {cx - rx - 16},{top_y + 8}" fill="none" stroke="#0f172a" stroke-width="1.8"/>\n'
        f'  <polyline points="{cx - rx - 24},{bot_y - 8} {cx - rx - 20},{bot_y} {cx - rx - 16},{bot_y - 8}" fill="none" stroke="#0f172a" stroke-width="1.8"/>\n'
        f'  <text x="{cx - rx - 28}" y="{(top_y + bot_y)/2}" font-size="13" font-weight="bold" text-anchor="end" fill="#0f172a">h = {height_val} {unit}</text>\n'
        f'  <text x="{cx}" y="26" font-size="14" font-weight="bold" text-anchor="middle" fill="#1e40af">Right Cylinder ({tag_str})</text>\n'
        f'</svg>'
    )
