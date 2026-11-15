"""Grade 10 & 11 Mathematics — Term 4 — Measurements Archetypes 26–50.
Grounded in South African National Curriculum Standards:
- curriculum_docs_auto/Mathematics_Gr10/Term 4/01. Measurements.md
- curriculum_docs_auto/Mathematics_Gr11/Term 4/02. Measurement.md
Covers:
- Right Pyramids: Volume, Slant height via Pythagoras, Total Surface Area, Rectangular-base pyramid
- Right Circular Cones: Volume, Slant height via Pythagoras, Closed TSA, Open curved SA, Finding height/radius
- Spheres & Hemispheres: Volume, Surface Area, Closed vs Open hemisphere SA, Finding radius from V or SA
- Composite 3D Solids: Cylinder + Cone (grain silo), Cylinder + Hemisphere (storage tank), Cube + Pyramid
- Dimensional Scaling (factor k): Effect on Surface Area (k^2), Effect on Volume (k^3), Radius vs Height scaling, Ratio of volumes from ratio of surface areas
- Unit conversions (cm^3, m^3, litres), Material cost applications, and Diagnostic misconception autopsy.
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional


def _fmt(val: float, decimals: int = 2) -> str:
    rounded = round(val, decimals)
    if decimals == 0 or rounded.is_integer():
        return str(int(rounded))
    return f"{rounded:.{decimals}f}".replace(".", "{,}")


def _make_q(
    r: random.Random,
    subskill: str,
    idx: int,
    prompt: str,
    ans: str,
    sol: str,
    marks: int,
    tags: List[str],
    schema: List[Dict[str, Any]],
    hints: Dict[str, str],
    diagram_spec: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    q: Dict[str, Any] = {
        "id": f"meas_g10_11_{idx:02d}_{r.randint(100000, 999999)}",
        "subskill": subskill,
        "question_type": "short_answer",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": marks,
        "learning_objective_id": f"math_meas_{idx:02d}",
        "misconception_tags": tags,
        "marking_schema": schema,
        "hints": hints,
        "topic": "Measurements",
        "grade": "11",
        "subject": "Mathematics",
        "term": 4,
        "caps_weight_percent": 15,
        "suggested_duration_mins": marks,
        "mode": f"elementary_{subskill}",
    }
    if diagram_spec is not None:
        q["diagram_spec"] = diagram_spec
    return q


def _svg_pyramid_cone_sphere(solid: str, p1: float, p2: float = 0, p3: float = 0, label: str = "") -> Dict[str, Any]:
    """Generate a seed-varied inline SVG for pyramids, cones, spheres, hemispheres, and composite silos."""
    if solid == "pyramid":
        svg = (
            f'<svg viewBox="0 0 380 215" width="100%" height="195" xmlns="http://www.w3.org/2000/svg">'
            f'<rect width="380" height="215" fill="#f8fafc" rx="8"/>'
            f'<polygon points="85,165 245,165 295,125 135,125" fill="#eff6ff" stroke="#1d4ed8" stroke-width="2"/>'
            f'<polygon points="85,165 245,165 190,35" fill="#dbeafe" fill-opacity="0.75" stroke="#1d4ed8" stroke-width="2.2"/>'
            f'<polygon points="245,165 295,125 190,35" fill="#bfdbfe" fill-opacity="0.75" stroke="#1d4ed8" stroke-width="2"/>'
            f'<line x1="190" y1="35" x2="190" y2="145" stroke="#dc2626" stroke-dasharray="4,3" stroke-width="2"/>'
            f'<text x="165" y="185" font-size="12" font-weight="bold" fill="#0f172a" text-anchor="middle">b = {p1:g} cm</text>'
            f'<text x="198" y="105" font-size="12" font-weight="bold" fill="#dc2626">{label or f"H = {p2:g} cm"}</text>'
            f'</svg>'
        )
    elif solid == "cone":
        svg = (
            f'<svg viewBox="0 0 380 215" width="100%" height="195" xmlns="http://www.w3.org/2000/svg">'
            f'<rect width="380" height="215" fill="#f8fafc" rx="8"/>'
            f'<polygon points="110,160 270,160 190,35" fill="#dbeafe" stroke="#1d4ed8" stroke-width="2.2"/>'
            f'<ellipse cx="190" cy="160" rx="80" ry="22" fill="#bfdbfe" stroke="#1d4ed8" stroke-width="2"/>'
            f'<line x1="190" y1="35" x2="190" y2="160" stroke="#dc2626" stroke-dasharray="4,3" stroke-width="2"/>'
            f'<line x1="190" y1="160" x2="270" y2="160" stroke="#0f172a" stroke-width="2"/>'
            f'<text x="230" y="154" font-size="12" font-weight="bold" fill="#0f172a" text-anchor="middle">r = {p1:g} cm</text>'
            f'<text x="198" y="105" font-size="12" font-weight="bold" fill="#dc2626">{label or f"H = {p2:g} cm"}</text>'
            f'</svg>'
        )
    elif solid == "sphere":
        svg = (
            f'<svg viewBox="0 0 360 205" width="100%" height="190" xmlns="http://www.w3.org/2000/svg">'
            f'<rect width="360" height="205" fill="#f8fafc" rx="8"/>'
            f'<circle cx="180" cy="102" r="72" fill="#dbeafe" stroke="#1d4ed8" stroke-width="2.5"/>'
            f'<ellipse cx="180" cy="102" rx="72" ry="22" fill="none" stroke="#2563eb" stroke-dasharray="4,3" stroke-width="1.8"/>'
            f'<line x1="180" y1="102" x2="252" y2="102" stroke="#dc2626" stroke-width="2.2"/>'
            f'<circle cx="180" cy="102" r="3.5" fill="#0f172a"/>'
            f'<text x="216" y="94" font-size="12" font-weight="bold" fill="#dc2626" text-anchor="middle">r = {p1:g} cm</text>'
            f'</svg>'
        )
    elif solid == "hemisphere":
        svg = (
            f'<svg viewBox="0 0 360 195" width="100%" height="185" xmlns="http://www.w3.org/2000/svg">'
            f'<rect width="360" height="195" fill="#f8fafc" rx="8"/>'
            f'<path d="M 100 140 A 80 80 0 0 1 260 140 Z" fill="#dbeafe" stroke="#1d4ed8" stroke-width="2.2"/>'
            f'<ellipse cx="180" cy="140" rx="80" ry="20" fill="#bfdbfe" stroke="#1d4ed8" stroke-width="2"/>'
            f'<line x1="180" y1="140" x2="260" y2="140" stroke="#dc2626" stroke-width="2"/>'
            f'<text x="220" y="135" font-size="12" font-weight="bold" fill="#dc2626" text-anchor="middle">r = {p1:g} cm</text>'
            f'<text x="180" y="178" font-size="12" font-weight="bold" fill="#0f172a" text-anchor="middle">{label or "Hemisphere"}</text>'
            f'</svg>'
        )
    else:  # composite_silo
        svg = (
            f'<svg viewBox="0 0 380 225" width="100%" height="205" xmlns="http://www.w3.org/2000/svg">'
            f'<rect width="380" height="225" fill="#f8fafc" rx="8"/>'
            f'<rect x="120" y="90" width="130" height="95" fill="#dbeafe" stroke="#1d4ed8" stroke-width="2"/>'
            f'<polygon points="120,90 250,90 185,30" fill="#bfdbfe" stroke="#1d4ed8" stroke-width="2"/>'
            f'<ellipse cx="185" cy="185" rx="65" ry="16" fill="#93c5fd" stroke="#1d4ed8" stroke-width="2"/>'
            f'<text x="185" y="215" font-size="12" font-weight="bold" fill="#0f172a" text-anchor="middle">r = {p1:g} m, h_cyl = {p2:g} m, top = {p3:g} m</text>'
            f'</svg>'
        )
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "p1": p1, "p2": p2, "p3": p3, "label": label}


# 26. Volume of right square pyramid (with inline_svg)
def build_26_volume_of_right_square_pyramid_svg(r: random.Random) -> Dict[str, Any]:
    b_v = r.choice([6, 9, 12, 15])
    h_v = r.randint(7, 20)
    vol = ((b_v ** 2) * h_v) // 3
    diag = _svg_pyramid_cone_sphere("pyramid", b_v, h_v)
    prompt = (
        f"Refer to the right square pyramid with base side length $b = {b_v}\\text{{ cm}}$ "
        f"and perpendicular height $H = {h_v}\\text{{ cm}}$.\n\n"
        f"Calculate the **volume** ($V$) of the pyramid."
    )
    ans = f"{vol}\\text{{ cm}}^3"
    sol = f"$V = \\frac{{1}}{{3}} \\times \\text{{Area of base}} \\times H = \\frac{{1}}{{3}}({b_v})^2({h_v}) = {vol}\\text{{ cm}}^3$."
    return _make_q(
        r, "26_volume_of_right_square_pyramid_svg", 26, prompt, ans, sol, 2,
        ["forgot_one_third_factor_in_pyramid_volume"],
        [{"step": 1, "criterion": f"1/3 * {b_v}^2 * {h_v}", "marks": 1}, {"step": 2, "criterion": f"{vol} cm^3", "marks": 1}],
        {"tier_1": "Volume of any pyramid is 1/3 * Area of base * perpendicular height.", "tier_2": f"1/3 * {b_v**2} * {h_v}", "tier_3": ans},
        diag,
    )


# 27. Slant height of square pyramid via Pythagoras (with inline_svg)
def build_27_slant_height_of_square_pyramid_via_pythagoras_svg(r: random.Random) -> Dict[str, Any]:
    half_b, h_v, h_s = r.choice([(3, 4, 5), (5, 12, 13), (6, 8, 10), (8, 15, 17), (9, 12, 15)])
    b_v = 2 * half_b
    diag = _svg_pyramid_cone_sphere("pyramid", b_v, h_v, label=f"H={h_v}, hs=?")
    prompt = (
        f"Refer to the right square pyramid with base side $b = {b_v}\\text{{ cm}}$ and perpendicular height $H = {h_v}\\text{{ cm}}$.\n\n"
        f"Calculate the **slant height** ($h_s$) of a triangular face."
    )
    ans = f"{h_s}\\text{{ cm}}"
    sol = f"Half of the base side is $\\frac{{{b_v}}}{{2}} = {half_b}\\text{{ cm}}$. By Pythagoras, $h_s = \\sqrt{{H^2 + (b/2)^2}} = \\sqrt{{{h_v}^2 + {half_b}^2}} = {h_s}\\text{{ cm}}$."
    return _make_q(
        r, "27_slant_height_of_square_pyramid_via_pythagoras_svg", 27, prompt, ans, sol, 2,
        ["used_full_base_side_instead_of_half_base_in_pythagoras"],
        [{"step": 1, "criterion": f"Use half-base = {half_b} cm", "marks": 1}, {"step": 2, "criterion": f"h_s = {h_s} cm", "marks": 1}],
        {"tier_1": f"The right triangle inside the pyramid has legs H = {h_v} and b/2 = {half_b}.", "tier_2": f"h_s = sqrt({h_v}^2 + {half_b}^2).", "tier_3": ans},
        diag,
    )


# 28. Total surface area right square pyramid (with inline_svg)
def build_28_total_surface_area_right_square_pyramid_svg(r: random.Random) -> Dict[str, Any]:
    half_b, h_v, h_s = r.choice([(3, 4, 5), (5, 12, 13), (6, 8, 10), (8, 15, 17), (9, 12, 15)])
    b_v = 2 * half_b
    base_area = b_v ** 2
    four_tri = 2 * b_v * h_s
    tsa = base_area + four_tri
    diag = _svg_pyramid_cone_sphere("pyramid", b_v, h_v, label=f"hs = {h_s} cm")
    prompt = (
        f"Refer to the right square pyramid with base side $b = {b_v}\\text{{ cm}}$ and slant height $h_s = {h_s}\\text{{ cm}}$.\n\n"
        f"Calculate the **Total Surface Area** ($TSA = b^2 + 4 \\times \\frac{{1}}{{2}} b h_s$)."
    )
    ans = f"{tsa}\\text{{ cm}}^2"
    sol = f"$A_{{\\text{{base}}}} = {b_v}^2 = {base_area}\\text{{ cm}}^2$. Four triangles $= 4 \\times \\frac{{1}}{{2}}({b_v})({h_s}) = {four_tri}\\text{{ cm}}^2$. $TSA = {tsa}\\text{{ cm}}^2$."
    return _make_q(
        r, "28_total_surface_area_right_square_pyramid_svg", 28, prompt, ans, sol, 3,
        ["used_perpendicular_height_instead_of_slant_height_for_tsa"],
        [{"step": 1, "criterion": f"Base = {base_area} cm^2", "marks": 1}, {"step": 2, "criterion": f"4 triangles = {four_tri} cm^2", "marks": 1}, {"step": 3, "criterion": f"TSA = {tsa} cm^2", "marks": 1}],
        {"tier_1": "Add the square base area (b^2) and 4 identical triangular faces (4 * 0,5 * b * h_s).", "tier_2": f"{base_area} + {four_tri}", "tier_3": ans},
        diag,
    )


# 29. Volume of right rectangular pyramid
def build_29_volume_of_right_rectangular_pyramid(r: random.Random) -> Dict[str, Any]:
    l_v = r.choice([6, 9, 12, 15])
    w_v = r.randint(5, 11)
    h_v = r.randint(7, 16)
    vol = (l_v * w_v * h_v) // 3
    prompt = (
        f"A right pyramid has a rectangular base of length $l = {l_v}\\text{{ cm}}$ and width $w = {w_v}\\text{{ cm}}$, "
        f"and a perpendicular height of $H = {h_v}\\text{{ cm}}$.\n\n"
        f"Calculate the **volume** of the pyramid."
    )
    ans = f"{vol}\\text{{ cm}}^3"
    sol = f"$V = \\frac{{1}}{{3}}(l \\times w)H = \\frac{{1}}{{3}}({l_v})({w_v})({h_v}) = {vol}\\text{{ cm}}^3$."
    return _make_q(
        r, "29_volume_of_right_rectangular_pyramid", 29, prompt, ans, sol, 2,
        ["omitted_one_third_in_rectangular_pyramid_volume"],
        [{"step": 1, "criterion": f"Base area = {l_v*w_v} cm^2", "marks": 1}, {"step": 2, "criterion": f"Volume = {vol} cm^3", "marks": 1}],
        {"tier_1": "V = 1/3 * (l * w) * H.", "tier_2": f"1/3 * {l_v} * {w_v} * {h_v}", "tier_3": ans},
    )


# 30. Volume of right circular cone (with inline_svg)
def build_30_volume_of_right_circular_cone_svg(r: random.Random) -> Dict[str, Any]:
    rad = r.choice([3, 6, 9, 12])
    h_v = r.randint(7, 20)
    k_pi = ((rad ** 2) * h_v) // 3
    vol_s = _fmt(math.pi * k_pi, 2)
    diag = _svg_pyramid_cone_sphere("cone", rad, h_v)
    prompt = (
        f"Refer to the right circular cone with base radius $r = {rad}\\text{{ cm}}$ and perpendicular height $H = {h_v}\\text{{ cm}}$.\n\n"
        f"Calculate its **volume** ($V = \\frac{{1}}{{3}}\\pi r^2 H$), both in terms of $\\pi$ and rounded to two decimal places."
    )
    ans = f"{k_pi}\\pi \\approx {vol_s}\\text{{ cm}}^3"
    sol = f"$V = \\frac{{1}}{{3}}\\pi({rad})^2({h_v}) = {k_pi}\\pi \\approx {vol_s}\\text{{ cm}}^3$."
    return _make_q(
        r, "30_volume_of_right_circular_cone_svg", 30, prompt, ans, sol, 3,
        ["forgot_one_third_in_cone_volume"],
        [{"step": 1, "criterion": f"Exact = {k_pi}*pi", "marks": 2}, {"step": 2, "criterion": f"{vol_s} cm^3", "marks": 1}],
        {"tier_1": "Volume of a cone is 1/3 * pi * r^2 * H.", "tier_2": f"1/3 * pi * {rad}^2 * {h_v} = {k_pi}*pi.", "tier_3": ans},
        diag,
    )


# 31. Slant height of cone via Pythagoras (with inline_svg)
def build_31_slant_height_of_cone_via_pythagoras_svg(r: random.Random) -> Dict[str, Any]:
    rad, h_v, slant = r.choice([(3, 4, 5), (5, 12, 13), (6, 8, 10), (8, 15, 17), (9, 12, 15), (7, 24, 25)])
    diag = _svg_pyramid_cone_sphere("cone", rad, h_v, label=f"H={h_v}, l=?")
    prompt = (
        f"Refer to the right circular cone with base radius $r = {rad}\\text{{ cm}}$ and perpendicular height $H = {h_v}\\text{{ cm}}$.\n\n"
        f"Calculate the **slant height** ($l$) of the cone."
    )
    ans = f"{slant}\\text{{ cm}}"
    sol = f"By Pythagoras, $l = \\sqrt{{r^2 + H^2}} = \\sqrt{{{rad}^2 + {h_v}^2}} = {slant}\\text{{ cm}}$."
    return _make_q(
        r, "31_slant_height_of_cone_via_pythagoras_svg", 31, prompt, ans, sol, 2,
        ["added_r_and_H_without_pythagoras"],
        [{"step": 1, "criterion": f"l^2 = {rad}^2 + {h_v}^2", "marks": 1}, {"step": 2, "criterion": f"l = {slant} cm", "marks": 1}],
        {"tier_1": "Use Pythagoras on the right triangle formed by r, H, and slant height l.", "tier_2": f"l = sqrt({rad}^2 + {h_v}^2).", "tier_3": ans},
        diag,
    )


# 32. Total surface area closed cone (with inline_svg)
def build_32_total_surface_area_closed_cone_svg(r: random.Random) -> Dict[str, Any]:
    rad, h_v, slant = r.choice([(3, 4, 5), (5, 12, 13), (6, 8, 10), (8, 15, 17), (9, 12, 15)])
    k_pi = (rad ** 2) + rad * slant
    tsa_s = _fmt(math.pi * k_pi, 2)
    diag = _svg_pyramid_cone_sphere("cone", rad, h_v, label=f"l = {slant} cm")
    prompt = (
        f"Refer to the closed right circular cone with base radius $r = {rad}\\text{{ cm}}$ and slant height $l = {slant}\\text{{ cm}}$.\n\n"
        f"Calculate its **Total Surface Area** ($TSA = \\pi r^2 + \\pi r l$), correct to two decimal places."
    )
    ans = f"{k_pi}\\pi \\approx {tsa_s}\\text{{ cm}}^2"
    sol = f"$TSA = \\pi({rad})^2 + \\pi({rad})({slant}) = {rad**2}\\pi + {rad*slant}\\pi = {k_pi}\\pi \\approx {tsa_s}\\text{{ cm}}^2$."
    return _make_q(
        r, "32_total_surface_area_closed_cone_svg", 32, prompt, ans, sol, 3,
        ["used_perpendicular_height_instead_of_slant_height_in_cone_tsa"],
        [{"step": 1, "criterion": f"Base = {rad**2}*pi", "marks": 1}, {"step": 2, "criterion": f"Curved = {rad*slant}*pi", "marks": 1}, {"step": 3, "criterion": f"{tsa_s} cm^2", "marks": 1}],
        {"tier_1": "TSA of a closed cone = circular base (pi*r^2) + curved surface (pi*r*l).", "tier_2": f"{rad**2}*pi + {rad*slant}*pi = {k_pi}*pi.", "tier_3": ans},
        diag,
    )


# 33. Curved surface area open cone hat
def build_33_curved_surface_area_open_cone_hat(r: random.Random) -> Dict[str, Any]:
    rad, h_v, slant = r.choice([(6, 8, 10), (5, 12, 13), (8, 15, 17), (9, 12, 15), (12, 16, 20)])
    k_pi = rad * slant
    sa_s = _fmt(math.pi * k_pi, 2)
    prompt = (
        f"A conical party hat (open at the circular base) has a radius of $r = {rad}\\text{{ cm}}$ "
        f"and a perpendicular height of $H = {h_v}\\text{{ cm}}$.\n\n"
        f"Calculate the slant height $l$ and the **area of cardboard** ($\\pi r l$) needed to make the hat, correct to two decimal places."
    )
    ans = f"l = {slant}\\text{{ cm}}, SA = {k_pi}\\pi \\approx {sa_s}\\text{{ cm}}^2"
    sol = f"$l = \\sqrt{{{rad}^2 + {h_v}^2}} = {slant}\\text{{ cm}}$. Curved surface area $= \\pi r l = \\pi({rad})({slant}) = {k_pi}\\pi \\approx {sa_s}\\text{{ cm}}^2$."
    return _make_q(
        r, "33_curved_surface_area_open_cone_hat", 33, prompt, ans, sol, 3,
        ["included_circular_base_for_open_cone_hat"],
        [{"step": 1, "criterion": f"Slant height l = {slant} cm", "marks": 1}, {"step": 2, "criterion": f"pi*r*l = {k_pi}*pi ≈ {sa_s} cm^2", "marks": 2}],
        {"tier_1": "First find l using Pythagoras, then compute pi * r * l (no base circle for a hat!).", "tier_2": f"l = {slant}; SA = pi * {rad} * {slant}.", "tier_3": ans},
    )


# 34. Find height or radius from cone volume
def build_34_find_height_or_radius_from_cone_volume(r: random.Random) -> Dict[str, Any]:
    rad = r.randint(3, 9)
    h_v = r.choice([6, 9, 12, 15, 18, 21])
    vol_coeff = ((rad ** 2) * h_v) // 3
    prompt = (
        f"A right circular cone has a volume of ${vol_coeff}\\pi\\text{{ cm}}^3$ and a base radius of $r = {rad}\\text{{ cm}}$.\n\n"
        f"Calculate the perpendicular **height** ($H$) of the cone."
    )
    ans = f"{h_v}\\text{{ cm}}"
    sol = f"$\\frac{{1}}{{3}}\\pi({rad})^2 H = {vol_coeff}\\pi \\implies {rad**2}H = {3*vol_coeff} \\implies H = {h_v}\\text{{ cm}}$."
    return _make_q(
        r, "34_find_height_or_radius_from_cone_volume", 34, prompt, ans, sol, 2,
        ["forgot_to_multiply_by_3_when_solving_cone_volume"],
        [{"step": 1, "criterion": f"1/3 * {rad**2} * H = {vol_coeff}", "marks": 1}, {"step": 2, "criterion": f"H = {h_v} cm", "marks": 1}],
        {"tier_1": f"Set 1/3 * pi * {rad}^2 * H = {vol_coeff} * pi.", "tier_2": f"H = (3 * {vol_coeff}) / {rad**2}.", "tier_3": ans},
    )


# 35. Volume of sphere (with inline_svg)
def build_35_volume_of_sphere_svg(r: random.Random) -> Dict[str, Any]:
    rad = r.choice([3, 6, 9, 12, 15])
    k_pi = (4 * (rad ** 3)) // 3
    vol_s = _fmt(math.pi * k_pi, 2)
    diag = _svg_pyramid_cone_sphere("sphere", rad)
    prompt = (
        f"Refer to the sphere with radius $r = {rad}\\text{{ cm}}$.\n\n"
        f"Calculate its **volume** ($V = \\frac{{4}}{{3}}\\pi r^3$), both in terms of $\\pi$ and rounded to two decimal places."
    )
    ans = f"{k_pi}\\pi \\approx {vol_s}\\text{{ cm}}^3"
    sol = f"$V = \\frac{{4}}{{3}}\\pi({rad})^3 = {k_pi}\\pi \\approx {vol_s}\\text{{ cm}}^3$."
    return _make_q(
        r, "35_volume_of_sphere_svg", 35, prompt, ans, sol, 3,
        ["squared_radius_instead_of_cubing_in_sphere_volume"],
        [{"step": 1, "criterion": f"Exact = {k_pi}*pi", "marks": 2}, {"step": 2, "criterion": f"{vol_s} cm^3", "marks": 1}],
        {"tier_1": "Use V = 4/3 * pi * r^3.", "tier_2": f"4/3 * pi * {rad}^3 = {k_pi}*pi.", "tier_3": ans},
        diag,
    )


# 36. Surface area of sphere (with inline_svg)
def build_36_surface_area_of_sphere_svg(r: random.Random) -> Dict[str, Any]:
    rad = r.randint(4, 16)
    k_pi = 4 * (rad ** 2)
    sa_s = _fmt(math.pi * k_pi, 2)
    diag = _svg_pyramid_cone_sphere("sphere", rad)
    prompt = (
        f"Refer to the sphere with radius $r = {rad}\\text{{ cm}}$.\n\n"
        f"Calculate its **surface area** ($A = 4\\pi r^2$), both in terms of $\\pi$ and rounded to two decimal places."
    )
    ans = f"{k_pi}\\pi \\approx {sa_s}\\text{{ cm}}^2"
    sol = f"$A = 4\\pi({rad})^2 = {k_pi}\\pi \\approx {sa_s}\\text{{ cm}}^2$."
    return _make_q(
        r, "36_surface_area_of_sphere_svg", 36, prompt, ans, sol, 2,
        ["used_pi_r2_instead_of_4_pi_r2_for_sphere"],
        [{"step": 1, "criterion": f"Exact = {k_pi}*pi", "marks": 1}, {"step": 2, "criterion": f"{sa_s} cm^2", "marks": 1}],
        {"tier_1": "Surface area of a sphere is 4 * pi * r^2.", "tier_2": f"4 * pi * {rad}^2 = {k_pi}*pi.", "tier_3": ans},
        diag,
    )


# 37. Find radius from sphere volume or surface area
def build_37_find_radius_from_sphere_volume_or_surface_area(r: random.Random) -> Dict[str, Any]:
    rad = r.randint(3, 14)
    sa_coeff = 4 * (rad ** 2)
    prompt = (
        f"A sphere has a surface area of ${sa_coeff}\\pi\\text{{ cm}}^2$.\n\n"
        f"Calculate the **radius** ($r$) of the sphere."
    )
    ans = f"{rad}\\text{{ cm}}"
    sol = f"$4\\pi r^2 = {sa_coeff}\\pi \\implies r^2 = {rad**2} \\implies r = {rad}\\text{{ cm}}$."
    return _make_q(
        r, "37_find_radius_from_sphere_volume_or_surface_area", 37, prompt, ans, sol, 2,
        ["divided_by_2_instead_of_taking_square_root"],
        [{"step": 1, "criterion": f"r^2 = {rad**2}", "marks": 1}, {"step": 2, "criterion": f"r = {rad} cm", "marks": 1}],
        {"tier_1": f"Equate 4*pi*r^2 = {sa_coeff}*pi and divide by 4*pi.", "tier_2": f"r = sqrt({rad**2}) = {rad} cm.", "tier_3": ans},
    )


# 38. Volume of hemisphere (with inline_svg)
def build_38_volume_of_hemisphere_svg(r: random.Random) -> Dict[str, Any]:
    rad = r.choice([3, 6, 9, 12, 15])
    k_pi = (2 * (rad ** 3)) // 3
    vol_s = _fmt(math.pi * k_pi, 2)
    diag = _svg_pyramid_cone_sphere("hemisphere", rad, label="Hemisphere Volume")
    prompt = (
        f"Refer to the hemisphere of radius $r = {rad}\\text{{ cm}}$.\n\n"
        f"Calculate its **volume** ($V = \\frac{{2}}{{3}}\\pi r^3$), both in terms of $\\pi$ and rounded to two decimal places."
    )
    ans = f"{k_pi}\\pi \\approx {vol_s}\\text{{ cm}}^3"
    sol = f"$V = \\frac{{2}}{{3}}\\pi({rad})^3 = {k_pi}\\pi \\approx {vol_s}\\text{{ cm}}^3$."
    return _make_q(
        r, "38_volume_of_hemisphere_svg", 38, prompt, ans, sol, 2,
        ["used_full_sphere_4_3_factor_for_hemisphere"],
        [{"step": 1, "criterion": f"Exact = {k_pi}*pi", "marks": 1}, {"step": 2, "criterion": f"{vol_s} cm^3", "marks": 1}],
        {"tier_1": "A hemisphere has half the volume of a sphere: V = 2/3 * pi * r^3.", "tier_2": f"2/3 * pi * {rad}^3 = {k_pi}*pi.", "tier_3": ans},
        diag,
    )


# 39. Surface area closed vs open hemisphere (with inline_svg)
def build_39_surface_area_closed_vs_open_hemisphere_svg(r: random.Random) -> Dict[str, Any]:
    rad = r.randint(4, 14)
    closed_k = 3 * (rad ** 2)
    open_k = 2 * (rad ** 2)
    diag = _svg_pyramid_cone_sphere("hemisphere", rad, label="Solid Closed Hemisphere")
    prompt = (
        f"Refer to the hemisphere of radius $r = {rad}\\text{{ cm}}$.\n\n"
        f"Write down in terms of $\\pi$:\n"
        f"1. The curved surface area of an **open** hemispherical bowl ($2\\pi r^2$).\n"
        f"2. The **Total Surface Area** of a **closed solid** hemisphere ($3\\pi r^2$, including the flat circular base)."
    )
    ans = f"\\text{{Open}} = {open_k}\\pi\\text{{ cm}}^2, \\text{{Closed}} = {closed_k}\\pi\\text{{ cm}}^2"
    sol = f"Open bowl $= 2\\pi({rad})^2 = {open_k}\\pi\\text{{ cm}}^2$. Closed solid hemisphere $= 2\\pi r^2 + \\pi r^2 = 3\\pi({rad})^2 = {closed_k}\\pi\\text{{ cm}}^2$."
    return _make_q(
        r, "39_surface_area_closed_vs_open_hemisphere_svg", 39, prompt, ans, sol, 2,
        ["used_2_pi_r2_for_closed_solid_hemisphere"],
        [{"step": 1, "criterion": f"Open = {open_k}*pi", "marks": 1}, {"step": 2, "criterion": f"Closed = {closed_k}*pi", "marks": 1}],
        {"tier_1": "A closed solid hemisphere has the curved dome (2*pi*r^2) PLUS the flat circular base (pi*r^2).", "tier_2": f"Open = {open_k}*pi, Closed = {closed_k}*pi.", "tier_3": ans},
        diag,
    )


# 40. Composite volume cylinder with cone roof silo (with inline_svg)
def build_40_composite_volume_cylinder_with_cone_roof_silo_svg(r: random.Random) -> Dict[str, Any]:
    rad = r.choice([3, 6, 9])
    h_cyl = r.randint(8, 16)
    h_cone = r.choice([3, 6, 9])
    v_cyl_k = (rad ** 2) * h_cyl
    v_cone_k = ((rad ** 2) * h_cone) // 3
    tot_k = v_cyl_k + v_cone_k
    vol_s = _fmt(math.pi * tot_k, 2)
    diag = _svg_pyramid_cone_sphere("silo", rad, h_cyl, h_cone)
    prompt = (
        f"Refer to the grain silo consisting of a right circular cylinder of radius $r = {rad}\\text{{ m}}$ and height $h_{{\\text{{cyl}}}} = {h_cyl}\\text{{ m}}$, "
        f"topped by a right circular cone of perpendicular height $h_{{\\text{{cone}}}} = {h_cone}\\text{{ m}}$.\n\n"
        f"Calculate the **total volume** of the silo, both in terms of $\\pi$ and rounded to two decimal places."
    )
    ans = f"{tot_k}\\pi \\approx {vol_s}\\text{{ m}}^3"
    sol = f"$V_{{\\text{{cyl}}}} = \\pi({rad})^2({h_cyl}) = {v_cyl_k}\\pi$. $V_{{\\text{{cone}}}} = \\frac{{1}}{{3}}\\pi({rad})^2({h_cone}) = {v_cone_k}\\pi$. Total $= {tot_k}\\pi \\approx {vol_s}\\text{{ m}}^3$."
    return _make_q(
        r, "40_composite_volume_cylinder_with_cone_roof_silo_svg", 40, prompt, ans, sol, 3,
        ["forgot_one_third_on_conical_roof"],
        [{"step": 1, "criterion": f"V_cyl = {v_cyl_k}*pi", "marks": 1}, {"step": 2, "criterion": f"V_cone = {v_cone_k}*pi", "marks": 1}, {"step": 3, "criterion": f"Total = {vol_s} m^3", "marks": 1}],
        {"tier_1": "Add the cylinder volume (pi*r^2*h_cyl) and the cone volume (1/3*pi*r^2*h_cone).", "tier_2": f"{v_cyl_k}*pi + {v_cone_k}*pi = {tot_k}*pi.", "tier_3": ans},
        diag,
    )


# 41. Composite volume cylinder with hemisphere top (with inline_svg)
def build_41_composite_volume_cylinder_with_hemisphere_top_svg(r: random.Random) -> Dict[str, Any]:
    rad = r.choice([3, 6, 9])
    h_cyl = r.randint(7, 15)
    v_cyl_k = (rad ** 2) * h_cyl
    v_hemi_k = (2 * (rad ** 3)) // 3
    tot_k = v_cyl_k + v_hemi_k
    vol_s = _fmt(math.pi * tot_k, 2)
    diag = _svg_pyramid_cone_sphere("silo", rad, h_cyl, rad)
    prompt = (
        f"A storage tank consists of a cylinder of radius $r = {rad}\\text{{ m}}$ and height $h = {h_cyl}\\text{{ m}}$, "
        f"capped by a hemispherical dome of the same radius $r = {rad}\\text{{ m}}$.\n\n"
        f"Calculate the **total volume** of the tank in terms of $\\pi$ and rounded to two decimal places."
    )
    ans = f"{tot_k}\\pi \\approx {vol_s}\\text{{ m}}^3"
    sol = f"$V = \\pi({rad})^2({h_cyl}) + \\frac{{2}}{{3}}\\pi({rad})^3 = {v_cyl_k}\\pi + {v_hemi_k}\\pi = {tot_k}\\pi \\approx {vol_s}\\text{{ m}}^3$."
    return _make_q(
        r, "41_composite_volume_cylinder_with_hemisphere_top_svg", 41, prompt, ans, sol, 3,
        ["used_4_3_instead_of_2_3_for_hemisphere_dome"],
        [{"step": 1, "criterion": f"V_cyl = {v_cyl_k}*pi", "marks": 1}, {"step": 2, "criterion": f"V_hemi = {v_hemi_k}*pi", "marks": 1}, {"step": 3, "criterion": f"Total = {vol_s} m^3", "marks": 1}],
        {"tier_1": "Add V_cylinder = pi*r^2*h and V_hemisphere = 2/3*pi*r^3.", "tier_2": f"{v_cyl_k}*pi + {v_hemi_k}*pi = {tot_k}*pi.", "tier_3": ans},
        diag,
    )


# 42. Composite surface area cylinder plus hemisphere (with inline_svg)
def build_42_composite_surface_area_cylinder_plus_hemisphere_svg(r: random.Random) -> Dict[str, Any]:
    rad = r.randint(3, 10)
    h_cyl = r.randint(8, 18)
    # Closed base (pi*r^2) + curved cylinder (2*pi*r*h) + curved hemisphere (2*pi*r^2) = 3*pi*r^2 + 2*pi*r*h
    tot_k = 3 * (rad ** 2) + 2 * rad * h_cyl
    sa_s = _fmt(math.pi * tot_k, 2)
    diag = _svg_pyramid_cone_sphere("silo", rad, h_cyl, rad)
    prompt = (
        f"A closed solid monument consists of a cylinder of radius $r = {rad}\\text{{ m}}$ and height $h = {h_cyl}\\text{{ m}}$ "
        f"resting on the ground (including its circular base) and topped by a hemisphere of radius $r = {rad}\\text{{ m}}$.\n\n"
        f"Calculate the **total exposed outer surface area** ($\\pi r^2 + 2\\pi r h + 2\\pi r^2$), in terms of $\\pi$ and to two decimal places."
    )
    ans = f"{tot_k}\\pi \\approx {sa_s}\\text{{ m}}^2"
    sol = f"Circular base $= {rad**2}\\pi$. Cylinder wall $= {2*rad*h_cyl}\\pi$. Hemisphere dome $= {2*rad**2}\\pi$. Total $= {tot_k}\\pi \\approx {sa_s}\\text{{ m}}^2$."
    return _make_q(
        r, "42_composite_surface_area_cylinder_plus_hemisphere_svg", 42, prompt, ans, sol, 3,
        ["included_internal_joined_circle_in_composite_surface_area"],
        [{"step": 1, "criterion": f"Exclude internal join; 3*pi*r^2 = {3*rad**2}*pi", "marks": 2}, {"step": 2, "criterion": f"Total = {tot_k}*pi ≈ {sa_s} m^2", "marks": 1}],
        {"tier_1": "Do not count the internal circle where the hemisphere meets the top of the cylinder!", "tier_2": f"SA = pi*r^2 + 2*pi*r*h + 2*pi*r^2 = {tot_k}*pi.", "tier_3": ans},
        diag,
    )


# 43. Composite volume cube with square pyramid roof
def build_43_composite_volume_cube_with_square_pyramid_roof(r: random.Random) -> Dict[str, Any]:
    s_v = r.choice([6, 9, 12])
    h_pyr = r.choice([4, 6, 8, 9, 12])
    v_cube = s_v ** 3
    v_pyr = ((s_v ** 2) * h_pyr) // 3
    tot_v = v_cube + v_pyr
    prompt = (
        f"A concrete pillar consists of a cube of side length $s = {s_v}\\text{{ cm}}$ topped by a right square pyramid "
        f"of the same base side $s = {s_v}\\text{{ cm}}$ and perpendicular height $H = {h_pyr}\\text{{ cm}}$.\n\n"
        f"Calculate the **total volume** of the pillar."
    )
    ans = f"{tot_v}\\text{{ cm}}^3"
    sol = f"$V_{{\\text{{cube}}}} = {s_v}^3 = {v_cube}\\text{{ cm}}^3$. $V_{{\\text{{pyramid}}}} = \\frac{{1}}{{3}}({s_v})^2({h_pyr}) = {v_pyr}\\text{{ cm}}^3$. Total $= {tot_v}\\text{{ cm}}^3$."
    return _make_q(
        r, "43_composite_volume_cube_with_square_pyramid_roof", 43, prompt, ans, sol, 3,
        ["omitted_one_third_in_pyramid_top"],
        [{"step": 1, "criterion": f"V_cube = {v_cube}", "marks": 1}, {"step": 2, "criterion": f"V_pyr = {v_pyr}", "marks": 1}, {"step": 3, "criterion": f"Total = {tot_v} cm^3", "marks": 1}],
        {"tier_1": "Add the volume of the cube (s^3) and the volume of the pyramid (1/3 * s^2 * H).", "tier_2": f"{v_cube} + {v_pyr}", "tier_3": ans},
    )


# 44. Scaling all dimensions by k effect on surface area
def build_44_scaling_all_dimensions_by_k_effect_on_surface_area(r: random.Random) -> Dict[str, Any]:
    a0 = r.randint(25, 80)
    k = r.choice([2, 3, 4, 5])
    new_a = a0 * (k ** 2)
    prompt = (
        f"A right prism has a total surface area of ${a0}\\text{{ cm}}^2$.\n\n"
        f"If **all linear dimensions** of the prism are multiplied by a scale factor of $k = {k}$, "
        f"calculate the **new total surface area**."
    )
    ans = f"{new_a}\\text{{ cm}}^2"
    sol = f"Scaling all linear dimensions by $k = {k}$ multiplies surface area by $k^2 = {k}^2 = {k**2}$. New $TSA = {a0} \\times {k**2} = {new_a}\\text{{ cm}}^2$."
    return _make_q(
        r, "44_scaling_all_dimensions_by_k_effect_on_surface_area", 44, prompt, ans, sol, 2,
        ["multiplied_surface_area_by_k_instead_of_k_squared"],
        [{"step": 1, "criterion": f"Scale factor k^2 = {k**2}", "marks": 1}, {"step": 2, "criterion": f"New SA = {new_a} cm^2", "marks": 1}],
        {"tier_1": "Surface area is 2-dimensional, so it scales by k^2.", "tier_2": f"{a0} * {k}^2 = {new_a}.", "tier_3": ans},
    )


# 45. Scaling all dimensions by k effect on volume
def build_45_scaling_all_dimensions_by_k_effect_on_volume(r: random.Random) -> Dict[str, Any]:
    v0 = r.randint(15, 60)
    k = r.choice([2, 3, 4])
    new_v = v0 * (k ** 3)
    prompt = (
        f"A solid cylinder has a volume of ${v0}\\text{{ cm}}^3$.\n\n"
        f"If both the radius and the height are multiplied by $k = {k}$, calculate the **new volume** of the cylinder."
    )
    ans = f"{new_v}\\text{{ cm}}^3"
    sol = f"Scaling all three dimensions by $k = {k}$ multiplies volume by $k^3 = {k}^3 = {k**3}$. New Volume $= {v0} \\times {k**3} = {new_v}\\text{{ cm}}^3$."
    return _make_q(
        r, "45_scaling_all_dimensions_by_k_effect_on_volume", 45, prompt, ans, sol, 2,
        ["multiplied_volume_by_k_or_k2_instead_of_k3"],
        [{"step": 1, "criterion": f"Scale factor k^3 = {k**3}", "marks": 1}, {"step": 2, "criterion": f"New Volume = {new_v} cm^3", "marks": 1}],
        {"tier_1": "Volume is 3-dimensional, so scaling all dimensions by k multiplies volume by k^3.", "tier_2": f"{v0} * {k}^3 = {new_v}.", "tier_3": ans},
    )


# 46. Scaling radius only vs height only in cylinder
def build_46_scaling_radius_only_vs_height_only_in_cylinder(r: random.Random) -> Dict[str, Any]:
    v0 = r.randint(20, 75)
    k = r.choice([2, 3, 4])
    v_rad = v0 * (k ** 2)
    v_h = v0 * k
    prompt = (
        f"A cylinder has an original volume of $V = {v0}\\text{{ cm}}^3$.\n\n"
        f"Determine the new volume if:\n"
        f"1. **Only the radius** is multiplied by ${k}$ (height unchanged).\n"
        f"2. **Only the height** is multiplied by ${k}$ (radius unchanged)."
    )
    ans = f"1.\\ {v_rad}\\text{{ cm}}^3,\\quad 2.\\ {v_h}\\text{{ cm}}^3"
    sol = f"Since $V = \\pi r^2 h$: (1) scaling $r$ by ${k}$ multiplies $V$ by ${k}^2 = {k**2} \\implies {v_rad}\\text{{ cm}}^3$; (2) scaling $h$ by ${k}$ multiplies $V$ by ${k} \\implies {v_h}\\text{{ cm}}^3$."
    return _make_q(
        r, "46_scaling_radius_only_vs_height_only_in_cylinder", 46, prompt, ans, sol, 2,
        ["used_k3_when_only_radius_was_scaled"],
        [{"step": 1, "criterion": f"Radius scaled: {k**2} * {v0} = {v_rad}", "marks": 1}, {"step": 2, "criterion": f"Height scaled: {k} * {v0} = {v_h}", "marks": 1}],
        {"tier_1": "Look at the exponents in V = pi * r^2 * h: r is squared, whereas h is to the power 1.", "tier_2": f"1. {k}^2 * {v0} = {v_rad}; 2. {k} * {v0} = {v_h}.", "tier_3": ans},
    )


# 47. Ratio of volumes from ratio of surface areas
def build_47_ratio_of_volumes_from_ratio_of_surface_areas(r: random.Random) -> Dict[str, Any]:
    a, b = r.choice([(1, 2), (2, 3), (3, 4), (2, 5), (3, 5)])
    sa1, sa2 = a ** 2, b ** 2
    v1, v2 = a ** 3, b ** 3
    prompt = (
        f"Two geometrically similar solids have surface areas in the ratio ${sa1} : {sa2}$.\n\n"
        f"Determine the ratio of their linear dimensions and the **ratio of their volumes**."
    )
    ans = f"\\text{{Linear}} = {a}:{b}, \\text{{Volume}} = {v1}:{v2}"
    sol = f"Linear ratio $= \\sqrt{{{sa1}}} : \\sqrt{{{sa2}}} = {a} : {b}$. Volume ratio $= {a}^3 : {b}^3 = {v1} : {v2}$."
    return _make_q(
        r, "47_ratio_of_volumes_from_ratio_of_surface_areas", 47, prompt, ans, sol, 3,
        ["cubed_area_ratio_directly_without_taking_square_root_first"],
        [{"step": 1, "criterion": f"Linear ratio {a}:{b}", "marks": 1}, {"step": 2, "criterion": f"Volume ratio {v1}:{v2}", "marks": 2}],
        {"tier_1": "Take the square root of the area ratio to get the linear scale ratio a : b first, then cube it!", "tier_2": f"Linear = {a}:{b} => Volume = {a}^3 : {b}^3.", "tier_3": ans},
    )


# 48. Unit conversion cm3 to litres and m3 capacity
def build_48_unit_conversion_cm3_to_litres_and_m3_capacity(r: random.Random) -> Dict[str, Any]:
    litres = r.randint(12, 85)
    cm3 = litres * 1000
    m3_val = r.choice([2, 3, 4, 5, 6, 8])
    m3_litres = m3_val * 1000
    prompt = (
        f"Convert the following volumes into **litres** ($\\text{{L}}$):\n"
        f"1. ${cm3}\\text{{ cm}}^3$\n"
        f"2. ${m3_val}\\text{{ m}}^3$"
    )
    ans = f"1.\\ {litres}\\text{{ L}},\\quad 2.\\ {m3_litres}\\text{{ L}}"
    sol = f"Since $1\\text{{ L}} = 1000\\text{{ cm}}^3$, ${cm3}\\text{{ cm}}^3 = {litres}\\text{{ L}}$. Since $1\\text{{ m}}^3 = 1000\\text{{ L}}$, ${m3_val}\\text{{ m}}^3 = {m3_litres}\\text{{ L}}$."
    return _make_q(
        r, "48_unit_conversion_cm3_to_litres_and_m3_capacity", 48, prompt, ans, sol, 2,
        ["divided_cm3_by_100_instead_of_1000"],
        [{"step": 1, "criterion": f"{litres} L", "marks": 1}, {"step": 2, "criterion": f"{m3_litres} L", "marks": 1}],
        {"tier_1": "Remember: 1 L = 1 000 cm^3 and 1 m^3 = 1 000 L.", "tier_2": f"{cm3}/1000 = {litres} L; {m3_val}*1000 = {m3_litres} L.", "tier_3": ans},
    )


# 49. Material cost painting surface area application
def build_49_material_cost_painting_surface_area_application(r: random.Random) -> Dict[str, Any]:
    l_v = r.randint(4, 8)
    b_v = r.randint(3, 6)
    h_v = r.randint(3, 5)
    wall_area = 2 * (l_v + b_v) * h_v
    rate = r.choice([40, 50, 60, 75, 80])
    cost = wall_area * rate
    prompt = (
        f"The four vertical interior walls of a rectangular room of length $l = {l_v}\\text{{ m}}$, width $b = {b_v}\\text{{ m}}$, "
        f"and height $h = {h_v}\\text{{ m}}$ are to be painted (excluding floor and ceiling).\n\n"
        f"If paint costs $\\text{{R }}{rate}$ per $\\text{{m}}^2$, calculate the total wall area and the **total cost**."
    )
    ans = f"\\text{{Area}} = {wall_area}\\text{{ m}}^2, \\text{{Cost}} = \\text{{R }}{cost}"
    sol = f"Four walls area $= 2(l + b)h = 2({l_v} + {b_v})({h_v}) = {wall_area}\\text{{ m}}^2$. Total cost $= {wall_area} \\times {rate} = \\text{{R }}{cost}$."
    return _make_q(
        r, "49_material_cost_painting_surface_area_application", 49, prompt, ans, sol, 3,
        ["included_floor_and_ceiling_in_four_walls_area"],
        [{"step": 1, "criterion": f"Wall area = {wall_area} m^2", "marks": 2}, {"step": 2, "criterion": f"Cost = R {cost}", "marks": 1}],
        {"tier_1": "The 4 vertical walls have area 2*(l + b)*h.", "tier_2": f"Area = {wall_area} m^2, then multiply by R {rate}.", "tier_3": ans},
    )


# 50. Measurements diagnostic autopsy and misconception repair
def build_50_measurements_diagnostic_autopsy_and_misconception_repair(r: random.Random) -> Dict[str, Any]:
    rad, h_perp, slant = r.choice([(3, 4, 5), (6, 8, 10), (5, 12, 13), (8, 15, 17)])
    wrong_k = (rad ** 2) + rad * h_perp
    corr_k = (rad ** 2) + rad * slant
    prompt = (
        f"A learner is asked to calculate the Total Surface Area of a closed right circular cone with radius $r = {rad}\\text{{ cm}}$ "
        f"and perpendicular height $H = {h_perp}\\text{{ cm}}$.\n"
        f"The learner writes: $TSA = \\pi({rad})^2 + \\pi({rad})({h_perp}) = {wrong_k}\\pi\\text{{ cm}}^2$.\n\n"
        f"Identify the misconception in the learner's working and calculate the **correct Total Surface Area** in terms of $\\pi$."
    )
    ans = f"\\text{{Used }} H={h_perp} \\text{{ instead of slant height }} l={slant}; \\text{{Correct }} TSA = {corr_k}\\pi\\text{{ cm}}^2"
    sol = (
        f"The learner used the perpendicular height $H = {h_perp}\\text{{ cm}}$ instead of the slant height $l = \\sqrt{{{rad}^2 + {h_perp}^2}} = {slant}\\text{{ cm}}$. "
        f"Correct $TSA = \\pi({rad})^2 + \\pi({rad})({slant}) = {corr_k}\\pi\\text{{ cm}}^2$."
    )
    return _make_q(
        r, "50_measurements_diagnostic_autopsy_and_misconception_repair", 50, prompt, ans, sol, 3,
        ["used_perpendicular_height_instead_of_slant_height_in_cone_tsa"],
        [{"step": 1, "criterion": "Identify error: used perpendicular height instead of slant height", "marks": 1}, {"step": 2, "criterion": f"Find slant height l = {slant} cm", "marks": 1}, {"step": 3, "criterion": f"Correct TSA = {corr_k}*pi cm^2", "marks": 1}],
        {"tier_1": "The formula TSA = pi*r^2 + pi*r*l requires the SLANT height l, not the perpendicular height H!", "tier_2": f"l = sqrt({rad}^2 + {h_perp}^2) = {slant} cm.", "tier_3": ans},
    )


ARCHETYPES_26_50 = {
    "26_volume_of_right_square_pyramid_svg": build_26_volume_of_right_square_pyramid_svg,
    "27_slant_height_of_square_pyramid_via_pythagoras_svg": build_27_slant_height_of_square_pyramid_via_pythagoras_svg,
    "28_total_surface_area_right_square_pyramid_svg": build_28_total_surface_area_right_square_pyramid_svg,
    "29_volume_of_right_rectangular_pyramid": build_29_volume_of_right_rectangular_pyramid,
    "30_volume_of_right_circular_cone_svg": build_30_volume_of_right_circular_cone_svg,
    "31_slant_height_of_cone_via_pythagoras_svg": build_31_slant_height_of_cone_via_pythagoras_svg,
    "32_total_surface_area_closed_cone_svg": build_32_total_surface_area_closed_cone_svg,
    "33_curved_surface_area_open_cone_hat": build_33_curved_surface_area_open_cone_hat,
    "34_find_height_or_radius_from_cone_volume": build_34_find_height_or_radius_from_cone_volume,
    "35_volume_of_sphere_svg": build_35_volume_of_sphere_svg,
    "36_surface_area_of_sphere_svg": build_36_surface_area_of_sphere_svg,
    "37_find_radius_from_sphere_volume_or_surface_area": build_37_find_radius_from_sphere_volume_or_surface_area,
    "38_volume_of_hemisphere_svg": build_38_volume_of_hemisphere_svg,
    "39_surface_area_closed_vs_open_hemisphere_svg": build_39_surface_area_closed_vs_open_hemisphere_svg,
    "40_composite_volume_cylinder_with_cone_roof_silo_svg": build_40_composite_volume_cylinder_with_cone_roof_silo_svg,
    "41_composite_volume_cylinder_with_hemisphere_top_svg": build_41_composite_volume_cylinder_with_hemisphere_top_svg,
    "42_composite_surface_area_cylinder_plus_hemisphere_svg": build_42_composite_surface_area_cylinder_plus_hemisphere_svg,
    "43_composite_volume_cube_with_square_pyramid_roof": build_43_composite_volume_cube_with_square_pyramid_roof,
    "44_scaling_all_dimensions_by_k_effect_on_surface_area": build_44_scaling_all_dimensions_by_k_effect_on_surface_area,
    "45_scaling_all_dimensions_by_k_effect_on_volume": build_45_scaling_all_dimensions_by_k_effect_on_volume,
    "46_scaling_radius_only_vs_height_only_in_cylinder": build_46_scaling_radius_only_vs_height_only_in_cylinder,
    "47_ratio_of_volumes_from_ratio_of_surface_areas": build_47_ratio_of_volumes_from_ratio_of_surface_areas,
    "48_unit_conversion_cm3_to_litres_and_m3_capacity": build_48_unit_conversion_cm3_to_litres_and_m3_capacity,
    "49_material_cost_painting_surface_area_application": build_49_material_cost_painting_surface_area_application,
    "50_measurements_diagnostic_autopsy_and_misconception_repair": build_50_measurements_diagnostic_autopsy_and_misconception_repair,
}
