"""Grade 8 Mathematics — Surface Area & Volume of 3D Objects SVG Visualizations.
Crisp vector SVG isometric/oblique 3D renderings:
  - Cube with side length s and right-prism geometry.
  - Rectangular prism (cuboid) with length, breadth, and height.
  - Triangular prism with triangular cross-section (base, height) and prism length.
  - Liquid container / fish tank with water level.
  - Composite 3D object (cube mounted on top of rectangular prism).

All renderings deterministic and parameter-driven, conforming strictly to 5D Diagram referee standards.
"""
from __future__ import annotations

import random
from typing import Optional


def draw_cube_3d_svg(s: float | int, seed: int = 101) -> str:
    """Renders an isometric-style 3D cube with edge length s."""
    rng = random.Random(seed)
    w, h = 320, 240
    dx = rng.choice([-6, 0, 6])
    dy = rng.choice([-4, 0, 4])

    ox, oy = 110 + dx, 150 + dy
    size = 90
    iso_x = 45
    iso_y = 26

    # Front face: (ox, oy), (ox+size, oy), (ox+size, oy-size), (ox, oy-size)
    f_bl = (ox, oy)
    f_br = (ox + size, oy)
    f_tr = (ox + size, oy - size)
    f_tl = (ox, oy - size)

    # Top face corners
    t_bl = f_tl
    t_br = f_tr
    t_tr = (f_tr[0] + iso_x, f_tr[1] - iso_y)
    t_tl = (f_tl[0] + iso_x, f_tl[1] - iso_y)

    # Right face corners
    r_tl = f_tr
    r_tr = t_tr
    r_br = (f_br[0] + iso_x, f_br[1] - iso_y)
    r_bl = f_br

    lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" height="100%" style="background:#ffffff; font-family:sans-serif;">',
        f'  <!-- seed: {seed} -->',
        f'  <!-- Front face -->',
        f'  <polygon points="{f_bl[0]},{f_bl[1]} {f_br[0]},{f_br[1]} {f_tr[0]},{f_tr[1]} {f_tl[0]},{f_tl[1]}" fill="#93c5fd" fill-opacity="0.5" stroke="#1e3a8a" stroke-width="2"/>',
        f'  <!-- Top face -->',
        f'  <polygon points="{t_bl[0]},{t_bl[1]} {t_br[0]},{t_br[1]} {t_tr[0]},{t_tr[1]} {t_tl[0]},{t_tl[1]}" fill="#bfdbfe" fill-opacity="0.6" stroke="#1e3a8a" stroke-width="2"/>',
        f'  <!-- Right face -->',
        f'  <polygon points="{r_tl[0]},{r_tl[1]} {r_tr[0]},{r_tr[1]} {r_br[0]},{r_br[1]} {r_bl[0]},{r_bl[1]}" fill="#60a5fa" fill-opacity="0.4" stroke="#1e3a8a" stroke-width="2"/>',
        f'  <!-- Dimension labels -->',
        f'  <text x="{(f_bl[0]+f_br[0])/2}" y="{f_bl[1]+20}" font-size="12" font-weight="bold" fill="#1e3a8a" text-anchor="middle">s = {s} cm</text>',
        f'  <text x="{f_bl[0]-12}" y="{(f_bl[1]+f_tl[1])/2}" font-size="12" font-weight="bold" fill="#1e3a8a" text-anchor="end">s = {s} cm</text>',
        f'  <text x="{(r_tr[0]+r_br[0])/2+15}" y="{(r_tr[1]+r_br[1])/2}" font-size="12" font-weight="bold" fill="#1e3a8a">s = {s} cm</text>',
        f'  <text x="{w/2}" y="{h-8}" font-size="11" fill="#475569" text-anchor="middle">Cube (all 6 faces are congruent squares of side {s} cm)</text>',
        '</svg>',
    ]
    return "\n".join(lines)


def draw_rectangular_prism_3d_svg(
    l: float | int,
    b: float | int,
    h_val: float | int,
    unit: str = "cm",
    seed: int = 101,
) -> str:
    """Renders a 3D rectangular prism (cuboid) with length, breadth, and height."""
    rng = random.Random(seed)
    w, h = 340, 240
    dx = rng.choice([-8, 0, 8])
    dy = rng.choice([-5, 0, 5])

    ox, oy = 75 + dx, 165 + dy
    pw = 140
    ph = 70
    iso_x = 55
    iso_y = 30

    f_bl = (ox, oy)
    f_br = (ox + pw, oy)
    f_tr = (ox + pw, oy - ph)
    f_tl = (ox, oy - ph)

    t_bl = f_tl
    t_br = f_tr
    t_tr = (f_tr[0] + iso_x, f_tr[1] - iso_y)
    t_tl = (f_tl[0] + iso_x, f_tl[1] - iso_y)

    r_tl = f_tr
    r_tr = t_tr
    r_br = (f_br[0] + iso_x, f_br[1] - iso_y)
    r_bl = f_br

    lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" height="100%" style="background:#ffffff; font-family:sans-serif;">',
        f'  <!-- seed: {seed} -->',
        f'  <!-- Front face (l x h) -->',
        f'  <polygon points="{f_bl[0]},{f_bl[1]} {f_br[0]},{f_br[1]} {f_tr[0]},{f_tr[1]} {f_tl[0]},{f_tl[1]}" fill="#fed7aa" fill-opacity="0.5" stroke="#c2410c" stroke-width="2"/>',
        f'  <!-- Top face (l x b) -->',
        f'  <polygon points="{t_bl[0]},{t_bl[1]} {t_br[0]},{t_br[1]} {t_tr[0]},{t_tr[1]} {t_tl[0]},{t_tl[1]}" fill="#ffedd5" fill-opacity="0.7" stroke="#c2410c" stroke-width="2"/>',
        f'  <!-- Right face (b x h) -->',
        f'  <polygon points="{r_tl[0]},{r_tl[1]} {r_tr[0]},{r_tr[1]} {r_br[0]},{r_br[1]} {r_bl[0]},{r_bl[1]}" fill="#fdba74" fill-opacity="0.4" stroke="#c2410c" stroke-width="2"/>',
        f'  <!-- Dimension labels -->',
        f'  <text x="{(f_bl[0]+f_br[0])/2}" y="{f_bl[1]+18}" font-size="12" font-weight="bold" fill="#9a3412" text-anchor="middle">length = {l} {unit}</text>',
        f'  <text x="{f_bl[0]-10}" y="{(f_bl[1]+f_tl[1])/2}" font-size="12" font-weight="bold" fill="#9a3412" text-anchor="end">height = {h_val} {unit}</text>',
        f'  <text x="{(r_br[0]+f_br[0])/2+12}" y="{(r_br[1]+f_br[1])/2+14}" font-size="12" font-weight="bold" fill="#9a3412">breadth = {b} {unit}</text>',
        f'  <text x="{w/2}" y="{h-8}" font-size="11" fill="#475569" text-anchor="middle">Rectangular Prism ({l} × {b} × {h_val} {unit})</text>',
        '</svg>',
    ]
    return "\n".join(lines)


def draw_triangular_prism_3d_svg(
    b_tri: float | int,
    h_tri: float | int,
    hyp_tri: float | int,
    l_prism: float | int,
    unit: str = "cm",
    seed: int = 101,
) -> str:
    """Renders a right triangular prism with triangular cross-section."""
    rng = random.Random(seed)
    w, h = 340, 240
    dx = rng.choice([-8, 0, 8])
    dy = rng.choice([-5, 0, 5])

    ox, oy = 80 + dx, 170 + dy
    tw = 90
    th = 75
    ext_x = 110
    ext_y = 45

    # Front triangle: right angle at (ox, oy)
    p_b = (ox, oy)
    p_c = (ox + tw, oy)
    p_a = (ox, oy - th)

    # Back triangle
    p_b_back = (p_b[0] + ext_x, p_b[1] - ext_y)
    p_c_back = (p_c[0] + ext_x, p_c[1] - ext_y)
    p_a_back = (p_a[0] + ext_x, p_a[1] - ext_y)

    lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" height="100%" style="background:#ffffff; font-family:sans-serif;">',
        f'  <!-- seed: {seed} -->',
        f'  <!-- Slanted rectangular top/hypotenuse face -->',
        f'  <polygon points="{p_a[0]},{p_a[1]} {p_c[0]},{p_c[1]} {p_c_back[0]},{p_c_back[1]} {p_a_back[0]},{p_a_back[1]}" fill="#bbf7d0" fill-opacity="0.5" stroke="#15803d" stroke-width="2"/>',
        f'  <!-- Front triangular face -->',
        f'  <polygon points="{p_b[0]},{p_b[1]} {p_c[0]},{p_c[1]} {p_a[0]},{p_a[1]}" fill="#86efac" fill-opacity="0.7" stroke="#15803d" stroke-width="2"/>',
        f'  <!-- Right angle marker at (p_b) -->',
        f'  <polyline points="{p_b[0]},{p_b[1]-12} {p_b[0]+12},{p_b[1]-12} {p_b[0]+12},{p_b[1]}" fill="none" stroke="#166534" stroke-width="1.5"/>',
        f'  <!-- Bottom edge & Back triangular outline -->',
        f'  <line x1="{p_c[0]}" y1="{p_c[1]}" x2="{p_c_back[0]}" y2="{p_c_back[1]}" stroke="#15803d" stroke-width="2"/>',
        f'  <line x1="{p_c_back[0]}" y1="{p_c_back[1]}" x2="{p_a_back[0]}" y2="{p_a_back[1]}" stroke="#15803d" stroke-width="1.5" stroke-dasharray="3,3"/>',
        f'  <!-- Labels -->',
        f'  <text x="{(p_b[0]+p_c[0])/2}" y="{p_b[1]+18}" font-size="12" font-weight="bold" fill="#14532d" text-anchor="middle">base = {b_tri} {unit}</text>',
        f'  <text x="{p_b[0]-10}" y="{(p_b[1]+p_a[1])/2}" font-size="12" font-weight="bold" fill="#14532d" text-anchor="end">height = {h_tri} {unit}</text>',
        f'  <text x="{(p_c[0]+p_c_back[0])/2+15}" y="{(p_c[1]+p_c_back[1])/2+12}" font-size="12" font-weight="bold" fill="#14532d">length = {l_prism} {unit}</text>',
        f'  <text x="{(p_a[0]+p_c[0])/2-8}" y="{(p_a[1]+p_c[1])/2-6}" font-size="11" font-weight="bold" fill="#166534">{hyp_tri} {unit}</text>',
        f'  <text x="{w/2}" y="{h-8}" font-size="11" fill="#475569" text-anchor="middle">Right Triangular Prism (Triangular base: {b_tri} × {h_tri} {unit}, Prism length: {l_prism} {unit})</text>',
        '</svg>',
    ]
    return "\n".join(lines)


def draw_tank_water_svg(
    l: float | int,
    b: float | int,
    h_val: float | int,
    water_h: float | int,
    seed: int = 101,
) -> str:
    """Renders a transparent glass aquarium / tank partially filled with water."""
    rng = random.Random(seed)
    w, h = 340, 240
    dx = rng.choice([-6, 0, 6])
    dy = rng.choice([-4, 0, 4])

    ox, oy = 80 + dx, 170 + dy
    pw = 140
    ph = 90
    iso_x = 50
    iso_y = 25

    # Water fill fraction
    frac = min(1.0, max(0.1, float(water_h) / float(h_val))) if h_val > 0 else 0.5
    w_ph = ph * frac

    lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" height="100%" style="background:#ffffff; font-family:sans-serif;">',
        f'  <!-- seed: {seed} -->',
        f'  <!-- Water body -->',
        f'  <polygon points="{ox},{oy} {ox+pw},{oy} {ox+pw},{oy-w_ph} {ox},{oy-w_ph}" fill="#38bdf8" fill-opacity="0.6"/>',
        f'  <polygon points="{ox},{oy-w_ph} {ox+pw},{oy-w_ph} {ox+pw+iso_x},{oy-w_ph-iso_y} {ox+iso_x},{oy-w_ph-iso_y}" fill="#0284c7" fill-opacity="0.5"/>',
        f'  <polygon points="{ox+pw},{oy} {ox+pw+iso_x},{oy-iso_y} {ox+pw+iso_x},{oy-w_ph-iso_y} {ox+pw},{oy-w_ph}" fill="#0369a1" fill-opacity="0.5"/>',
        f'  <!-- Glass tank outer boundaries -->',
        f'  <polygon points="{ox},{oy} {ox+pw},{oy} {ox+pw},{oy-ph} {ox},{oy-ph}" fill="none" stroke="#334155" stroke-width="2"/>',
        f'  <polygon points="{ox},{oy-ph} {ox+pw},{oy-ph} {ox+pw+iso_x},{oy-ph-iso_y} {ox+iso_x},{oy-ph-iso_y}" fill="none" stroke="#334155" stroke-width="1.5"/>',
        f'  <polygon points="{ox+pw},{oy} {ox+pw+iso_x},{oy-iso_y} {ox+pw+iso_x},{oy-ph-iso_y} {ox+pw},{oy-ph}" fill="none" stroke="#334155" stroke-width="1.5"/>',
        f'  <!-- Labels -->',
        f'  <text x="{(ox+ox+pw)/2}" y="{oy+18}" font-size="12" font-weight="bold" fill="#0f172a" text-anchor="middle">Length = {l} cm</text>',
        f'  <text x="{ox-10}" y="{oy-ph/2}" font-size="12" font-weight="bold" fill="#0f172a" text-anchor="end">Tank Height = {h_val} cm</text>',
        f'  <text x="{ox+pw+iso_x+10}" y="{oy-w_ph/2}" font-size="12" font-weight="bold" fill="#0284c7">Water Depth = {water_h} cm</text>',
        f'  <text x="{w/2}" y="{h-8}" font-size="11" fill="#475569" text-anchor="middle">Fish Tank: {l} cm × {b} cm with water depth {water_h} cm</text>',
        '</svg>',
    ]
    return "\n".join(lines)


def draw_composite_prism_svg(
    base_l: float | int,
    base_b: float | int,
    base_h: float | int,
    cube_s: float | int,
    seed: int = 101,
) -> str:
    """Renders a composite solid: a small cube glued centered on top of a larger rectangular prism."""
    rng = random.Random(seed)
    w, h = 340, 250
    dx = rng.choice([-6, 0, 6])
    dy = rng.choice([-4, 0, 4])

    ox, oy = 80 + dx, 185 + dy
    pw = 140
    ph = 55
    iso_x = 45
    iso_y = 22

    # Bottom rectangular prism
    b_fl = (ox, oy)
    b_fr = (ox + pw, oy)
    b_tr = (ox + pw, oy - ph)
    b_tl = (ox, oy - ph)

    # Top cube dimensions
    cs = 45
    c_ox = ox + (pw - cs) / 2
    c_oy = oy - ph

    c_fl = (c_ox, c_oy)
    c_fr = (c_ox + cs, c_oy)
    c_tr = (c_ox + cs, c_oy - cs)
    c_tl = (c_ox, c_oy - cs)

    c_iso_x = 24
    c_iso_y = 12

    lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" height="100%" style="background:#ffffff; font-family:sans-serif;">',
        f'  <!-- seed: {seed} -->',
        f'  <!-- Base rectangular prism front -->',
        f'  <polygon points="{b_fl[0]},{b_fl[1]} {b_fr[0]},{b_fr[1]} {b_tr[0]},{b_tr[1]} {b_tl[0]},{b_tl[1]}" fill="#cbd5e1" stroke="#334155" stroke-width="2"/>',
        f'  <!-- Base top face -->',
        f'  <polygon points="{b_tl[0]},{b_tl[1]} {b_tr[0]},{b_tr[1]} {b_tr[0]+iso_x},{b_tr[1]-iso_y} {b_tl[0]+iso_x},{b_tl[1]-iso_y}" fill="#e2e8f0" stroke="#334155" stroke-width="2"/>',
        f'  <!-- Base right face -->',
        f'  <polygon points="{b_tr[0]},{b_tr[1]} {b_tr[0]+iso_x},{b_tr[1]-iso_y} {b_fr[0]+iso_x},{b_fr[1]-iso_y} {b_fr[0]},{b_fr[1]}" fill="#94a3b8" stroke="#334155" stroke-width="2"/>',
        f'  <!-- Cube on top front -->',
        f'  <polygon points="{c_fl[0]},{c_fl[1]} {c_fr[0]},{c_fr[1]} {c_tr[0]},{c_tr[1]} {c_tl[0]},{c_tl[1]}" fill="#fbcfe8" stroke="#be185d" stroke-width="2"/>',
        f'  <!-- Cube top -->',
        f'  <polygon points="{c_tl[0]},{c_tl[1]} {c_tr[0]},{c_tr[1]} {c_tr[0]+c_iso_x},{c_tr[1]-c_iso_y} {c_tl[0]+c_iso_x},{c_tl[1]-c_iso_y}" fill="#fdf2f8" stroke="#be185d" stroke-width="2"/>',
        f'  <!-- Cube right -->',
        f'  <polygon points="{c_tr[0]},{c_tr[1]} {c_tr[0]+c_iso_x},{c_tr[1]-c_iso_y} {c_fr[0]+c_iso_x},{c_fr[1]-c_iso_y} {c_fr[0]},{c_fr[1]}" fill="#f472b6" stroke="#be185d" stroke-width="2"/>',
        f'  <!-- Labels -->',
        f'  <text x="{(b_fl[0]+b_fr[0])/2}" y="{b_fl[1]+18}" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">Base: {base_l} × {base_b} × {base_h} cm</text>',
        f'  <text x="{c_fl[0]-10}" y="{(c_fl[1]+c_tl[1])/2}" font-size="11" font-weight="bold" fill="#be185d" text-anchor="end">Cube: side {cube_s} cm</text>',
        f'  <text x="{w/2}" y="{h-8}" font-size="11" fill="#475569" text-anchor="middle">Composite Object: Cube glued on top of rectangular prism</text>',
        '</svg>',
    ]
    return "\n".join(lines)
