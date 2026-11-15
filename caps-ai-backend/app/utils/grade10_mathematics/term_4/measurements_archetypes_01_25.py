"""Grade 10 & 11 Mathematics — Term 4 — Measurements Archetypes 01–25.
Grounded in South African National Curriculum Standards:
- curriculum_docs_auto/Mathematics_Gr10/Term 4/01. Measurements.md
- curriculum_docs_auto/Mathematics_Gr11/Term 4/02. Measurement.md
Covers:
- 2D Polygons & Circles: Rectangle, Square, Triangle (direct & Pythagoras), Parallelogram, Trapezium, Rhombus/Kite, Circle, Semicircle, Annulus, Composite 2D shapes, Map scale conversions
- Right Prisms & Cylinders: Rectangular prism (volume, closed TSA, open-top SA), Cube, Triangular prism (volume & TSA), Right circular cylinder (volume, lateral SA, closed TSA, open-top SA, missing dimension, hollow pipe), Trapezoidal prism.
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
        "grade": "10",
        "subject": "Mathematics",
        "term": 4,
        "caps_weight_percent": 15,
        "suggested_duration_mins": marks,
        "mode": f"elementary_{subskill}",
    }
    if diagram_spec is not None:
        q["diagram_spec"] = diagram_spec
    return q


def _svg_2d_shape(shape: str, p1: float, p2: float = 0, p3: float = 0, label: str = "") -> Dict[str, Any]:
    """Generate a seed-varied inline SVG for 2D shapes and cross-sections."""
    if shape == "rectangle":
        svg = (
            f'<svg viewBox="0 0 360 200" width="100%" height="190" xmlns="http://www.w3.org/2000/svg">'
            f'<rect width="360" height="200" fill="#f8fafc" rx="8"/>'
            f'<rect x="70" y="40" width="220" height="110" fill="#dbeafe" stroke="#1d4ed8" stroke-width="2.5"/>'
            f'<text x="180" y="172" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="middle">l = {p1:g} cm</text>'
            f'<text x="305" y="100" font-size="13" font-weight="bold" fill="#0f172a">b = {p2:g} cm</text>'
            f'</svg>'
        )
    elif shape == "triangle":
        svg = (
            f'<svg viewBox="0 0 360 200" width="100%" height="190" xmlns="http://www.w3.org/2000/svg">'
            f'<rect width="360" height="200" fill="#f8fafc" rx="8"/>'
            f'<polygon points="60,155 300,155 180,35" fill="#dbeafe" stroke="#1d4ed8" stroke-width="2.5"/>'
            f'<line x1="180" y1="35" x2="180" y2="155" stroke="#dc2626" stroke-dasharray="4,3" stroke-width="2"/>'
            f'<text x="180" y="176" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="middle">base = {p1:g} cm</text>'
            f'<text x="190" y="105" font-size="12" font-weight="bold" fill="#dc2626">{label or f"h = {p2:g} cm"}</text>'
            f'</svg>'
        )
    elif shape == "parallelogram":
        svg = (
            f'<svg viewBox="0 0 380 200" width="100%" height="190" xmlns="http://www.w3.org/2000/svg">'
            f'<rect width="380" height="200" fill="#f8fafc" rx="8"/>'
            f'<polygon points="60,155 280,155 320,45 100,45" fill="#dbeafe" stroke="#1d4ed8" stroke-width="2.5"/>'
            f'<line x1="100" y1="45" x2="100" y2="155" stroke="#dc2626" stroke-dasharray="4,3" stroke-width="2"/>'
            f'<text x="190" y="176" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="middle">base = {p1:g} cm</text>'
            f'<text x="52" y="100" font-size="12" font-weight="bold" fill="#1e293b">slant = {p2:g} cm</text>'
            f'<text x="108" y="110" font-size="12" font-weight="bold" fill="#dc2626">h = {p3:g} cm</text>'
            f'</svg>'
        )
    elif shape == "trapezium":
        svg = (
            f'<svg viewBox="0 0 380 200" width="100%" height="190" xmlns="http://www.w3.org/2000/svg">'
            f'<rect width="380" height="200" fill="#f8fafc" rx="8"/>'
            f'<polygon points="60,155 320,155 265,45 115,45" fill="#dbeafe" stroke="#1d4ed8" stroke-width="2.5"/>'
            f'<line x1="115" y1="45" x2="115" y2="155" stroke="#dc2626" stroke-dasharray="4,3" stroke-width="2"/>'
            f'<text x="190" y="36" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="middle">a = {p1:g} cm</text>'
            f'<text x="190" y="176" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="middle">b = {p2:g} cm</text>'
            f'<text x="124" y="105" font-size="12" font-weight="bold" fill="#dc2626">h = {p3:g} cm</text>'
            f'</svg>'
        )
    elif shape == "circle":
        svg = (
            f'<svg viewBox="0 0 360 200" width="100%" height="190" xmlns="http://www.w3.org/2000/svg">'
            f'<rect width="360" height="200" fill="#f8fafc" rx="8"/>'
            f'<circle cx="180" cy="100" r="68" fill="#dbeafe" stroke="#1d4ed8" stroke-width="2.5"/>'
            f'<line x1="180" y1="100" x2="248" y2="100" stroke="#dc2626" stroke-width="2.2"/>'
            f'<circle cx="180" cy="100" r="3.5" fill="#0f172a"/>'
            f'<text x="214" y="92" font-size="13" font-weight="bold" fill="#dc2626" text-anchor="middle">r = {p1:g} cm</text>'
            f'</svg>'
        )
    elif shape == "semicircle":
        svg = (
            f'<svg viewBox="0 0 360 190" width="100%" height="185" xmlns="http://www.w3.org/2000/svg">'
            f'<rect width="360" height="190" fill="#f8fafc" rx="8"/>'
            f'<path d="M 90 140 A 90 90 0 0 1 270 140 Z" fill="#dbeafe" stroke="#1d4ed8" stroke-width="2.5"/>'
            f'<text x="180" y="162" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="middle">r = {p1:g} cm (diameter = {2*p1:g} cm)</text>'
            f'</svg>'
        )
    elif shape == "annulus":
        svg = (
            f'<svg viewBox="0 0 360 200" width="100%" height="190" xmlns="http://www.w3.org/2000/svg">'
            f'<rect width="360" height="200" fill="#f8fafc" rx="8"/>'
            f'<circle cx="180" cy="100" r="74" fill="#bfdbfe" stroke="#1d4ed8" stroke-width="2.5"/>'
            f'<circle cx="180" cy="100" r="38" fill="#f8fafc" stroke="#1d4ed8" stroke-width="2"/>'
            f'<text x="180" y="188" font-size="12" font-weight="bold" fill="#0f172a" text-anchor="middle">R = {p1:g} cm, r = {p2:g} cm</text>'
            f'</svg>'
        )
    else:  # norman_window
        svg = (
            f'<svg viewBox="0 0 360 210" width="100%" height="195" xmlns="http://www.w3.org/2000/svg">'
            f'<rect width="360" height="210" fill="#f8fafc" rx="8"/>'
            f'<rect x="110" y="85" width="140" height="85" fill="#dbeafe" stroke="#1d4ed8" stroke-width="2.2"/>'
            f'<path d="M 110 85 A 70 70 0 0 1 250 85 Z" fill="#bfdbfe" stroke="#1d4ed8" stroke-width="2.2"/>'
            f'<text x="180" y="190" font-size="12" font-weight="bold" fill="#0f172a" text-anchor="middle">width = {p1:g} m, rect height = {p2:g} m</text>'
            f'</svg>'
        )
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "p1": p1, "p2": p2, "p3": p3}


def _svg_3d_prism_cyl(solid: str, d1: float, d2: float, d3: float = 0) -> Dict[str, Any]:
    """Generate a seed-varied inline SVG for 3D right prisms and cylinders."""
    if solid == "cuboid":
        svg = (
            f'<svg viewBox="0 0 380 210" width="100%" height="195" xmlns="http://www.w3.org/2000/svg">'
            f'<rect width="380" height="210" fill="#f8fafc" rx="8"/>'
            f'<polygon points="70,75 230,75 270,40 110,40" fill="#eff6ff" stroke="#1d4ed8" stroke-width="2"/>'
            f'<rect x="70" y="75" width="160" height="90" fill="#dbeafe" stroke="#1d4ed8" stroke-width="2.2"/>'
            f'<polygon points="230,75 270,40 270,130 230,165" fill="#bfdbfe" stroke="#1d4ed8" stroke-width="2"/>'
            f'<text x="150" y="185" font-size="12" font-weight="bold" fill="#0f172a" text-anchor="middle">l = {d1:g} cm</text>'
            f'<text x="262" y="158" font-size="12" font-weight="bold" fill="#0f172a">b = {d2:g} cm</text>'
            f'<text x="42" y="125" font-size="12" font-weight="bold" fill="#0f172a">h = {d3:g} cm</text>'
            f'</svg>'
        )
    elif solid == "tri_prism":
        svg = (
            f'<svg viewBox="0 0 380 210" width="100%" height="195" xmlns="http://www.w3.org/2000/svg">'
            f'<rect width="380" height="210" fill="#f8fafc" rx="8"/>'
            f'<polygon points="70,160 190,160 70,65" fill="#dbeafe" stroke="#1d4ed8" stroke-width="2.2"/>'
            f'<polygon points="70,65 190,160 290,115 170,20" fill="#bfdbfe" stroke="#1d4ed8" stroke-width="2"/>'
            f'<line x1="70" y1="65" x2="170" y2="20" stroke="#1d4ed8" stroke-width="2"/>'
            f'<text x="130" y="182" font-size="12" font-weight="bold" fill="#0f172a" text-anchor="middle">b = {d1:g} cm</text>'
            f'<text x="38" y="118" font-size="12" font-weight="bold" fill="#0f172a">h = {d2:g} cm</text>'
            f'<text x="255" y="152" font-size="12" font-weight="bold" fill="#0f172a">L = {d3:g} cm</text>'
            f'</svg>'
        )
    else:  # cylinder
        svg = (
            f'<svg viewBox="0 0 380 210" width="100%" height="195" xmlns="http://www.w3.org/2000/svg">'
            f'<rect width="380" height="210" fill="#f8fafc" rx="8"/>'
            f'<rect x="115" y="55" width="140" height="110" fill="#dbeafe" stroke="#1d4ed8" stroke-width="2"/>'
            f'<ellipse cx="185" cy="165" rx="70" ry="20" fill="#bfdbfe" stroke="#1d4ed8" stroke-width="2"/>'
            f'<ellipse cx="185" cy="55" rx="70" ry="20" fill="#eff6ff" stroke="#1d4ed8" stroke-width="2.2"/>'
            f'<line x1="185" y1="55" x2="255" y2="55" stroke="#dc2626" stroke-width="2"/>'
            f'<text x="220" y="48" font-size="12" font-weight="bold" fill="#dc2626" text-anchor="middle">r = {d1:g} cm</text>'
            f'<text x="270" y="115" font-size="12" font-weight="bold" fill="#0f172a">h = {d2:g} cm</text>'
            f'</svg>'
        )
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "d1": d1, "d2": d2, "d3": d3}


# 01. Perimeter and area of rectangle (with inline_svg)
def build_01_perimeter_and_area_of_rectangle_svg(r: random.Random) -> Dict[str, Any]:
    l_v = r.randint(12, 28)
    b_v = r.randint(6, 15)
    perim = 2 * (l_v + b_v)
    area = l_v * b_v
    diag = _svg_2d_shape("rectangle", l_v, b_v)
    prompt = (
        f"Refer to the rectangle with length $l = {l_v}\\text{{ cm}}$ and breadth $b = {b_v}\\text{{ cm}}$.\n\n"
        f"Calculate its **perimeter** ($P$) and **area** ($A$)."
    )
    ans = f"P = {perim}\\text{{ cm}}, A = {area}\\text{{ cm}}^2"
    sol = f"Perimeter $P = 2({l_v} + {b_v}) = {perim}\\text{{ cm}}$. Area $A = {l_v} \\times {b_v} = {area}\\text{{ cm}}^2$."
    return _make_q(
        r, "01_perimeter_and_area_of_rectangle_svg", 1, prompt, ans, sol, 2,
        ["confused_perimeter_and_area"],
        [{"step": 1, "criterion": f"P = {perim} cm", "marks": 1}, {"step": 2, "criterion": f"A = {area} cm^2", "marks": 1}],
        {"tier_1": "P = 2(l + b) and A = l * b.", "tier_2": f"P = 2({l_v}+{b_v}) and A = {l_v}*{b_v}.", "tier_3": ans},
        diag,
    )


# 02. Area of square from perimeter
def build_02_area_of_square_from_perimeter_or_diagonal(r: random.Random) -> Dict[str, Any]:
    s_v = r.randint(7, 22)
    perim = 4 * s_v
    area = s_v ** 2
    prompt = f"A square has a total perimeter of ${perim}\\text{{ cm}}$. Calculate the **area** of the square in $\\text{{cm}}^2$."
    ans = f"{area}\\text{{ cm}}^2"
    sol = f"Side length $s = \\frac{{{perim}}}{{4}} = {s_v}\\text{{ cm}}$. Area $A = s^2 = {s_v}^2 = {area}\\text{{ cm}}^2$."
    return _make_q(
        r, "02_area_of_square_from_perimeter_or_diagonal", 2, prompt, ans, sol, 2,
        ["squared_perimeter_instead_of_side"],
        [{"step": 1, "criterion": f"Side s = {s_v} cm", "marks": 1}, {"step": 2, "criterion": f"Area = {area} cm^2", "marks": 1}],
        {"tier_1": "Divide the perimeter by 4 to find the side length s.", "tier_2": f"s = {s_v} cm, then Area = s^2.", "tier_3": ans},
    )


# 03. Area of triangle base and perpendicular height (with inline_svg)
def build_03_area_of_triangle_base_and_perpendicular_height_svg(r: random.Random) -> Dict[str, Any]:
    b_v = r.choice([10, 12, 14, 16, 18, 20, 24])
    h_v = r.randint(7, 19)
    area = (b_v * h_v) // 2
    diag = _svg_2d_shape("triangle", b_v, h_v)
    prompt = (
        f"Refer to the triangle with base $b = {b_v}\\text{{ cm}}$ and perpendicular height $h = {h_v}\\text{{ cm}}$.\n\n"
        f"Calculate the **area** of the triangle."
    )
    ans = f"{area}\\text{{ cm}}^2"
    sol = f"$\\text{{Area}} = \\frac{{1}}{{2}} \\times b \\times h = \\frac{{1}}{{2}} \\times {b_v} \\times {h_v} = {area}\\text{{ cm}}^2$."
    return _make_q(
        r, "03_area_of_triangle_base_and_perpendicular_height_svg", 3, prompt, ans, sol, 2,
        ["forgot_half_factor_in_triangle_area"],
        [{"step": 1, "criterion": "Apply A = 1/2 * b * h", "marks": 1}, {"step": 2, "criterion": f"Area = {area} cm^2", "marks": 1}],
        {"tier_1": "Use Area = 1/2 * base * perpendicular height.", "tier_2": f"0,5 * {b_v} * {h_v}", "tier_3": ans},
        diag,
    )


# 04. Area of isosceles triangle via Pythagoras (with inline_svg)
def build_04_area_of_isosceles_triangle_via_pythagoras_svg(r: random.Random) -> Dict[str, Any]:
    half_b, h_v, slant = r.choice([(3, 4, 5), (5, 12, 13), (6, 8, 10), (8, 15, 17), (9, 12, 15)])
    base = 2 * half_b
    area = half_b * h_v
    diag = _svg_2d_shape("triangle", base, h_v, label=f"slant = {slant} cm")
    prompt = (
        f"An isosceles triangle has a base of ${base}\\text{{ cm}}$ and two equal slant sides of length ${slant}\\text{{ cm}}$ each.\n\n"
        f"Use the Theorem of Pythagoras to determine the perpendicular height $h$, and hence calculate the **area** of the triangle."
    )
    ans = f"h = {h_v}\\text{{ cm}}, \\text{{Area}} = {area}\\text{{ cm}}^2"
    sol = f"Half-base $= {half_b}\\text{{ cm}}$. By Pythagoras, $h = \\sqrt{{{slant}^2 - {half_b}^2}} = {h_v}\\text{{ cm}}$. Area $= \\frac{{1}}{{2}}({base})({h_v}) = {area}\\text{{ cm}}^2$."
    return _make_q(
        r, "04_area_of_isosceles_triangle_via_pythagoras_svg", 4, prompt, ans, sol, 3,
        ["used_slant_side_as_perpendicular_height"],
        [{"step": 1, "criterion": f"h = {h_v} cm via Pythagoras", "marks": 2}, {"step": 2, "criterion": f"Area = {area} cm^2", "marks": 1}],
        {"tier_1": f"Drop a perpendicular bisecting the base into {half_b} cm and {half_b} cm.", "tier_2": f"h = sqrt({slant}^2 - {half_b}^2) = {h_v} cm.", "tier_3": ans},
        diag,
    )


# 05. Area of parallelogram with Pythagoras height (with inline_svg)
def build_05_area_of_parallelogram_with_pythagoras_height_svg(r: random.Random) -> Dict[str, Any]:
    dx, h_v, slant = r.choice([(3, 4, 5), (6, 8, 10), (5, 12, 13), (9, 12, 15)])
    base = r.randint(12, 25)
    area = base * h_v
    diag = _svg_2d_shape("parallelogram", base, slant, h_v)
    prompt = (
        f"Refer to the parallelogram with base $b = {base}\\text{{ cm}}$, slant side ${slant}\\text{{ cm}}$, "
        f"and perpendicular height $h = {h_v}\\text{{ cm}}$.\n\n"
        f"Calculate the **area** of the parallelogram."
    )
    ans = f"{area}\\text{{ cm}}^2"
    sol = f"$\\text{{Area}} = \\text{{base}} \\times \\text{{perpendicular height}} = {base} \\times {h_v} = {area}\\text{{ cm}}^2$."
    return _make_q(
        r, "05_area_of_parallelogram_with_pythagoras_height_svg", 5, prompt, ans, sol, 2,
        ["multiplied_base_by_slant_side_instead_of_perpendicular_height"],
        [{"step": 1, "criterion": f"Use perpendicular height {h_v} cm", "marks": 1}, {"step": 2, "criterion": f"Area = {area} cm^2", "marks": 1}],
        {"tier_1": "Use the perpendicular height h, not the slant side!", "tier_2": f"Area = {base} * {h_v}.", "tier_3": ans},
        diag,
    )


# 06. Area of trapezium parallel sides (with inline_svg)
def build_06_area_of_trapezium_parallel_sides_svg(r: random.Random) -> Dict[str, Any]:
    a_v = r.randint(8, 16)
    b_v = a_v + r.choice([6, 8, 10, 12])
    h_v = r.randint(6, 15)
    area = ((a_v + b_v) * h_v) // 2
    diag = _svg_2d_shape("trapezium", a_v, b_v, h_v)
    prompt = (
        f"Refer to the trapezium with parallel sides $a = {a_v}\\text{{ cm}}$ and $b = {b_v}\\text{{ cm}}$, "
        f"and perpendicular height $h = {h_v}\\text{{ cm}}$.\n\n"
        f"Calculate the **area** of the trapezium."
    )
    ans = f"{area}\\text{{ cm}}^2"
    sol = f"$\\text{{Area}} = \\frac{{1}}{{2}}(a + b)h = \\frac{{1}}{{2}}({a_v} + {b_v}) \\times {h_v} = {area}\\text{{ cm}}^2$."
    return _make_q(
        r, "06_area_of_trapezium_parallel_sides_svg", 6, prompt, ans, sol, 2,
        ["multiplied_parallel_sides_instead_of_adding"],
        [{"step": 1, "criterion": f"1/2 * ({a_v} + {b_v}) * {h_v}", "marks": 1}, {"step": 2, "criterion": f"Area = {area} cm^2", "marks": 1}],
        {"tier_1": "Average the two parallel sides and multiply by the perpendicular height.", "tier_2": f"0,5 * ({a_v} + {b_v}) * {h_v}", "tier_3": ans},
        diag,
    )


# 07. Area of rhombus and kite from diagonals
def build_07_area_of_rhombus_and_kite_from_diagonals(r: random.Random) -> Dict[str, Any]:
    d1 = r.choice([10, 12, 14, 16, 18, 22])
    d2 = r.randint(9, 25)
    area = (d1 * d2) // 2
    shape_name = r.choice(["rhombus", "kite"])
    prompt = (
        f"A {shape_name} has perpendicular diagonals of lengths $d_1 = {d1}\\text{{ cm}}$ and $d_2 = {d2}\\text{{ cm}}$.\n\n"
        f"Calculate the **area** of the {shape_name}."
    )
    ans = f"{area}\\text{{ cm}}^2"
    sol = f"$\\text{{Area}} = \\frac{{1}}{{2}} d_1 d_2 = \\frac{{1}}{{2}} \\times {d1} \\times {d2} = {area}\\text{{ cm}}^2$."
    return _make_q(
        r, "07_area_of_rhombus_and_kite_from_diagonals", 7, prompt, ans, sol, 2,
        ["forgot_half_in_diagonal_area_formula"],
        [{"step": 1, "criterion": f"0,5 * {d1} * {d2}", "marks": 1}, {"step": 2, "criterion": f"{area} cm^2", "marks": 1}],
        {"tier_1": "The area of a rhombus or kite is half the product of its diagonals.", "tier_2": f"0,5 * {d1} * {d2}", "tier_3": ans},
    )


# 08. Circumference and area of circle (with inline_svg)
def build_08_circumference_and_area_of_circle_svg(r: random.Random) -> Dict[str, Any]:
    rad = r.randint(4, 16)
    circ_s = _fmt(2 * math.pi * rad, 2)
    area_s = _fmt(math.pi * (rad ** 2), 2)
    diag = _svg_2d_shape("circle", rad)
    prompt = (
        f"Refer to the circle with radius $r = {rad}\\text{{ cm}}$.\n\n"
        f"Calculate its **circumference** ($C$) and **area** ($A$), rounded to two decimal places."
    )
    ans = f"C = {circ_s}\\text{{ cm}}, A = {area_s}\\text{{ cm}}^2"
    sol = f"$C = 2\\pi({rad}) \\approx {circ_s}\\text{{ cm}}$. $A = \\pi({rad})^2 = {rad**2}\\pi \\approx {area_s}\\text{{ cm}}^2$."
    return _make_q(
        r, "08_circumference_and_area_of_circle_svg", 8, prompt, ans, sol, 3,
        ["swapped_circumference_and_area_formulas"],
        [{"step": 1, "criterion": f"C = {circ_s} cm", "marks": 1}, {"step": 2, "criterion": f"A = {area_s} cm^2", "marks": 2}],
        {"tier_1": "C = 2*pi*r and A = pi*r^2.", "tier_2": f"C = {2*rad}*pi, A = {rad**2}*pi.", "tier_3": ans},
        diag,
    )


# 09. Perimeter and area of semicircle (with inline_svg)
def build_09_perimeter_and_area_of_semicircle_svg(r: random.Random) -> Dict[str, Any]:
    rad = r.randint(5, 18)
    perim_s = _fmt(math.pi * rad + 2 * rad, 2)
    area_s = _fmt(0.5 * math.pi * (rad ** 2), 2)
    diag = _svg_2d_shape("semicircle", rad)
    prompt = (
        f"Refer to the closed semicircle of radius $r = {rad}\\text{{ cm}}$.\n\n"
        f"Calculate its **total perimeter** (curved arc plus straight diameter) and its **area**, correct to two decimal places."
    )
    ans = f"P = {perim_s}\\text{{ cm}}, A = {area_s}\\text{{ cm}}^2"
    sol = f"Perimeter $P = \\pi r + 2r = \\pi({rad}) + {2*rad} \\approx {perim_s}\\text{{ cm}}$. Area $A = \\frac{{1}}{{2}}\\pi({rad})^2 \\approx {area_s}\\text{{ cm}}^2$."
    return _make_q(
        r, "09_perimeter_and_area_of_semicircle_svg", 9, prompt, ans, sol, 3,
        ["omitted_straight_diameter_from_semicircle_perimeter"],
        [{"step": 1, "criterion": f"Include diameter {2*rad} in perimeter: {perim_s} cm", "marks": 2}, {"step": 2, "criterion": f"Area = {area_s} cm^2", "marks": 1}],
        {"tier_1": "Do not forget to add the straight diameter 2r to the curved arc pi*r!", "tier_2": f"P = pi*{rad} + {2*rad}; A = 0,5*pi*{rad}^2.", "tier_3": ans},
        diag,
    )


# 10. Area of annulus concentric circles (with inline_svg)
def build_10_area_of_annulus_concentric_circles_svg(r: random.Random) -> Dict[str, Any]:
    r_in = r.randint(3, 9)
    r_out = r_in + r.randint(3, 7)
    diff_sq = r_out ** 2 - r_in ** 2
    area_s = _fmt(math.pi * diff_sq, 2)
    diag = _svg_2d_shape("annulus", r_out, r_in)
    prompt = (
        f"Refer to the circular ring (annulus) with outer radius $R = {r_out}\\text{{ cm}}$ and inner radius $r = {r_in}\\text{{ cm}}$.\n\n"
        f"Calculate the shaded area both in terms of $\\pi$ and rounded to two decimal places."
    )
    ans = f"{diff_sq}\\pi \\approx {area_s}\\text{{ cm}}^2"
    sol = f"$A = \\pi(R^2 - r^2) = \\pi({r_out}^2 - {r_in}^2) = {diff_sq}\\pi \\approx {area_s}\\text{{ cm}}^2$."
    return _make_q(
        r, "10_area_of_annulus_concentric_circles_svg", 10, prompt, ans, sol, 3,
        ["computed_R_minus_r_squared_instead_of_R2_minus_r2"],
        [{"step": 1, "criterion": f"R^2 - r^2 = {diff_sq}", "marks": 1}, {"step": 2, "criterion": f"{diff_sq}*pi ≈ {area_s} cm^2", "marks": 2}],
        {"tier_1": "Subtract the inner circle area from the outer circle area: pi*(R^2 - r^2).", "tier_2": f"pi*({r_out**2} - {r_in**2}) = {diff_sq}*pi.", "tier_3": ans},
        diag,
    )


# 11. Composite 2D shape rectangle plus semicircle (with inline_svg)
def build_11_composite_2d_shape_rectangle_plus_semicircle_svg(r: random.Random) -> Dict[str, Any]:
    rad = r.randint(2, 6)
    width = 2 * rad
    rect_h = r.randint(4, 10)
    tot_area = width * rect_h + 0.5 * math.pi * (rad ** 2)
    area_s = _fmt(tot_area, 2)
    diag = _svg_2d_shape("norman", width, rect_h)
    prompt = (
        f"A window consists of a rectangle of width ${width}\\text{{ m}}$ and height ${rect_h}\\text{{ m}}$ "
        f"topped by a semicircle of radius $r = {rad}\\text{{ m}}$.\n\n"
        f"Calculate the **total area** of the window, correct to two decimal places."
    )
    ans = f"{area_s}\\text{{ m}}^2"
    sol = f"$A_{{\\text{{rect}}}} = {width} \\times {rect_h} = {width*rect_h}\\text{{ m}}^2$. $A_{{\\text{{semi}}}} = \\frac{{1}}{{2}}\\pi({rad})^2$. Total $= {area_s}\\text{{ m}}^2$."
    return _make_q(
        r, "11_composite_2d_shape_rectangle_plus_semicircle_svg", 11, prompt, ans, sol, 3,
        ["used_full_width_as_semicircle_radius"],
        [{"step": 1, "criterion": f"Rectangle area = {width*rect_h}", "marks": 1}, {"step": 2, "criterion": f"Semicircle radius = {rad} m", "marks": 1}, {"step": 3, "criterion": f"Total = {area_s} m^2", "marks": 1}],
        {"tier_1": f"The semicircle radius is half the width: r = {rad} m.", "tier_2": f"Area = {width*rect_h} + 0,5*pi*{rad}^2.", "tier_3": ans},
        diag,
    )


# 12. Map scale conversion perimeter and area
def build_12_map_scale_conversion_perimeter_and_area(r: random.Random) -> Dict[str, Any]:
    l_cm = r.randint(8, 18)
    b_cm = r.randint(5, 12)
    scale = r.choice([100, 200])
    # 1 cm on plan = scale cm = (scale/100) m
    m_per_cm = scale // 100
    l_m = l_cm * m_per_cm
    b_m = b_cm * m_per_cm
    perim_m = 2 * (l_m + b_m)
    area_m2 = l_m * b_m
    prompt = (
        f"On a building floor plan with a scale of $1 : {scale}$, a rectangular room measures ${l_cm}\\text{{ cm}}$ by ${b_cm}\\text{{ cm}}$.\n\n"
        f"Calculate the actual **perimeter** (in $\\text{{m}}$) and actual **area** (in $\\text{{m}}^2$) of the room."
    )
    ans = f"P = {perim_m}\\text{{ m}}, A = {area_m2}\\text{{ m}}^2"
    sol = f"Actual dimensions: $l = {l_m}\\text{{ m}}$ and $b = {b_m}\\text{{ m}}$. Perimeter $= 2({l_m}+{b_m}) = {perim_m}\\text{{ m}}$, Area $= {l_m} \\times {b_m} = {area_m2}\\text{{ m}}^2$."
    return _make_q(
        r, "12_map_scale_conversion_perimeter_and_area", 12, prompt, ans, sol, 3,
        ["converted_area_by_linear_factor_100_instead_of_10000"],
        [{"step": 1, "criterion": f"Actual dimensions {l_m} m by {b_m} m", "marks": 1}, {"step": 2, "criterion": f"P = {perim_m} m, A = {area_m2} m^2", "marks": 2}],
        {"tier_1": f"Convert the cm lengths into metres first using 1 cm = {m_per_cm} m.", "tier_2": f"l = {l_m} m, b = {b_m} m.", "tier_3": ans},
    )


# 13. Volume of rectangular prism cuboid (with inline_svg)
def build_13_volume_of_rectangular_prism_cuboid_svg(r: random.Random) -> Dict[str, Any]:
    l_v = r.randint(8, 18)
    b_v = r.randint(5, 11)
    h_v = r.randint(4, 10)
    vol = l_v * b_v * h_v
    diag = _svg_3d_prism_cyl("cuboid", l_v, b_v, h_v)
    prompt = (
        f"Refer to the right rectangular prism with length $l = {l_v}\\text{{ cm}}$, breadth $b = {b_v}\\text{{ cm}}$, "
        f"and height $h = {h_v}\\text{{ cm}}$.\n\n"
        f"Calculate its **volume** ($V$) in $\\text{{cm}}^3$."
    )
    ans = f"{vol}\\text{{ cm}}^3"
    sol = f"$V = l \\times b \\times h = {l_v} \\times {b_v} \\times {h_v} = {vol}\\text{{ cm}}^3$."
    return _make_q(
        r, "13_volume_of_rectangular_prism_cuboid_svg", 13, prompt, ans, sol, 2,
        ["added_dimensions_instead_of_multiplying"],
        [{"step": 1, "criterion": f"{l_v} * {b_v} * {h_v}", "marks": 1}, {"step": 2, "criterion": f"{vol} cm^3", "marks": 1}],
        {"tier_1": "Volume of a rectangular prism is length * breadth * height.", "tier_2": f"{l_v} * {b_v} * {h_v}", "tier_3": ans},
        diag,
    )


# 14. Total surface area closed rectangular prism (with inline_svg)
def build_14_total_surface_area_closed_rectangular_prism_svg(r: random.Random) -> Dict[str, Any]:
    l_v = r.randint(7, 15)
    b_v = r.randint(4, 9)
    h_v = r.randint(5, 11)
    tsa = 2 * (l_v * b_v + l_v * h_v + b_v * h_v)
    diag = _svg_3d_prism_cyl("cuboid", l_v, b_v, h_v)
    prompt = (
        f"Refer to the closed right rectangular prism with $l = {l_v}\\text{{ cm}}$, $b = {b_v}\\text{{ cm}}$, and $h = {h_v}\\text{{ cm}}$.\n\n"
        f"Calculate its **Total Surface Area** ($TSA$) in $\\text{{cm}}^2$."
    )
    ans = f"{tsa}\\text{{ cm}}^2"
    sol = f"$TSA = 2(lb + lh + bh) = 2({l_v*b_v} + {l_v*h_v} + {b_v*h_v}) = {tsa}\\text{{ cm}}^2$."
    return _make_q(
        r, "14_total_surface_area_closed_rectangular_prism_svg", 14, prompt, ans, sol, 3,
        ["forgot_to_multiply_pair_areas_by_2"],
        [{"step": 1, "criterion": "Compute 3 face pair areas", "marks": 2}, {"step": 2, "criterion": f"TSA = {tsa} cm^2", "marks": 1}],
        {"tier_1": "A closed cuboid has 3 pairs of identical rectangular faces: 2(lb + lh + bh).", "tier_2": f"2*({l_v*b_v} + {l_v*h_v} + {b_v*h_v})", "tier_3": ans},
        diag,
    )


# 15. Surface area open-top rectangular box
def build_15_surface_area_open_top_rectangular_box(r: random.Random) -> Dict[str, Any]:
    l_v = r.randint(8, 16)
    b_v = r.randint(5, 10)
    h_v = r.randint(4, 9)
    sa = l_v * b_v + 2 * l_v * h_v + 2 * b_v * h_v
    prompt = (
        f"A rectangular glass fish tank is **open at the top**. Its base has length $l = {l_v}\\text{{ dm}}$, "
        f"breadth $b = {b_v}\\text{{ dm}}$, and height $h = {h_v}\\text{{ dm}}$.\n\n"
        f"Calculate the total outer area of glass used ($1$ base + $4$ vertical sides)."
    )
    ans = f"{sa}\\text{{ dm}}^2"
    sol = f"$SA = lb + 2lh + 2bh = ({l_v})({b_v}) + 2({l_v})({h_v}) + 2({b_v})({h_v}) = {l_v*b_v} + {2*l_v*h_v} + {2*b_v*h_v} = {sa}\\text{{ dm}}^2$."
    return _make_q(
        r, "15_surface_area_open_top_rectangular_box", 15, prompt, ans, sol, 3,
        ["counted_two_bases_for_open_top_box"],
        [{"step": 1, "criterion": f"Single base area = {l_v*b_v}", "marks": 1}, {"step": 2, "criterion": f"4 vertical sides = {2*l_v*h_v + 2*b_v*h_v}", "marks": 1}, {"step": 3, "criterion": f"Total = {sa} dm^2", "marks": 1}],
        {"tier_1": "Because the tank is open at the top, count lb only once!", "tier_2": f"SA = {l_v*b_v} + 2*{l_v*h_v} + 2*{b_v*h_v}.", "tier_3": ans},
    )


# 16. Cube surface area and volume from edge
def build_16_cube_surface_area_and_volume_from_edge(r: random.Random) -> Dict[str, Any]:
    s_v = r.randint(4, 12)
    tsa = 6 * (s_v ** 2)
    vol = s_v ** 3
    prompt = (
        f"A closed cube has a total surface area of ${tsa}\\text{{ cm}}^2$.\n\n"
        f"Determine the side length $s$ of the cube and hence calculate its **volume** ($V$)."
    )
    ans = f"s = {s_v}\\text{{ cm}}, V = {vol}\\text{{ cm}}^3"
    sol = f"$6s^2 = {tsa} \\implies s^2 = {s_v**2} \\implies s = {s_v}\\text{{ cm}}$. Volume $V = s^3 = {s_v}^3 = {vol}\\text{{ cm}}^3$."
    return _make_q(
        r, "16_cube_surface_area_and_volume_from_edge", 16, prompt, ans, sol, 3,
        ["divided_cube_tsa_by_4_instead_of_6"],
        [{"step": 1, "criterion": f"s = {s_v} cm", "marks": 2}, {"step": 2, "criterion": f"V = {vol} cm^3", "marks": 1}],
        {"tier_1": "A cube has 6 equal square faces, so divide TSA by 6 first.", "tier_2": f"s = sqrt({tsa}/6) = {s_v} cm.", "tier_3": ans},
    )


# 17. Volume of right triangular prism (with inline_svg)
def build_17_volume_of_right_triangular_prism_svg(r: random.Random) -> Dict[str, Any]:
    b_v = r.choice([6, 8, 10, 12, 14])
    h_tri = r.randint(5, 12)
    len_prism = r.randint(10, 22)
    base_area = (b_v * h_tri) // 2
    vol = base_area * len_prism
    diag = _svg_3d_prism_cyl("tri_prism", b_v, h_tri, len_prism)
    prompt = (
        f"Refer to the right triangular prism whose triangular cross-section has base $b = {b_v}\\text{{ cm}}$ "
        f"and perpendicular height $h = {h_tri}\\text{{ cm}}$, with prism length $L = {len_prism}\\text{{ cm}}$.\n\n"
        f"Calculate the **volume** of the prism."
    )
    ans = f"{vol}\\text{{ cm}}^3"
    sol = f"$A_{{\\text{{base}}}} = \\frac{{1}}{{2}}({b_v})({h_tri}) = {base_area}\\text{{ cm}}^2$. Volume $V = {base_area} \\times {len_prism} = {vol}\\text{{ cm}}^3$."
    return _make_q(
        r, "17_volume_of_right_triangular_prism_svg", 17, prompt, ans, sol, 3,
        ["forgot_half_in_triangular_prism_volume"],
        [{"step": 1, "criterion": f"Base area = {base_area} cm^2", "marks": 1}, {"step": 2, "criterion": f"Volume = {vol} cm^3", "marks": 2}],
        {"tier_1": "Volume of a right prism = Area of triangular base * length.", "tier_2": f"0,5 * {b_v} * {h_tri} * {len_prism}", "tier_3": ans},
        diag,
    )


# 18. Total surface area right triangular prism (with inline_svg)
def build_18_total_surface_area_right_triangular_prism_svg(r: random.Random) -> Dict[str, Any]:
    b_v, h_tri, hyp = r.choice([(3, 4, 5), (6, 8, 10), (5, 12, 13), (9, 12, 15)])
    len_prism = r.randint(8, 20)
    two_tri = b_v * h_tri
    lat_area = (b_v + h_tri + hyp) * len_prism
    tsa = two_tri + lat_area
    diag = _svg_3d_prism_cyl("tri_prism", b_v, h_tri, len_prism)
    prompt = (
        f"Refer to the right-angled triangular prism with perpendicular base legs $b = {b_v}\\text{{ cm}}$ and $h = {h_tri}\\text{{ cm}}$, "
        f"and prism length $L = {len_prism}\\text{{ cm}}$.\n\n"
        f"Find the hypotenuse of the triangular base and calculate the **Total Surface Area** ($2$ triangles $+ 3$ rectangles)."
    )
    ans = f"{tsa}\\text{{ cm}}^2"
    sol = f"Hypotenuse $= {hyp}\\text{{ cm}}$. Two triangular ends $= {two_tri}\\text{{ cm}}^2$. Lateral area $= ({b_v}+{h_tri}+{hyp}) \\times {len_prism} = {lat_area}\\text{{ cm}}^2$. $TSA = {tsa}\\text{{ cm}}^2$."
    return _make_q(
        r, "18_total_surface_area_right_triangular_prism_svg", 18, prompt, ans, sol, 4,
        ["omitted_hypotenuse_rectangular_face"],
        [{"step": 1, "criterion": f"Hypotenuse = {hyp} cm", "marks": 1}, {"step": 2, "criterion": f"2 triangles = {two_tri}", "marks": 1}, {"step": 3, "criterion": f"3 rectangles = {lat_area}", "marks": 1}, {"step": 4, "criterion": f"TSA = {tsa} cm^2", "marks": 1}],
        {"tier_1": "Use Pythagoras to find the 3rd side of the triangle, then add the 2 triangles and 3 rectangular faces.", "tier_2": f"Hypotenuse = {hyp}; TSA = {two_tri} + ({b_v}+{h_tri}+{hyp})*{len_prism}.", "tier_3": ans},
        diag,
    )


# 19. Volume of right circular cylinder (with inline_svg)
def build_19_volume_of_right_circular_cylinder_svg(r: random.Random) -> Dict[str, Any]:
    rad = r.randint(3, 11)
    h_v = r.randint(8, 22)
    k_pi = (rad ** 2) * h_v
    vol_s = _fmt(math.pi * k_pi, 2)
    diag = _svg_3d_prism_cyl("cylinder", rad, h_v)
    prompt = (
        f"Refer to the right circular cylinder with radius $r = {rad}\\text{{ cm}}$ and height $h = {h_v}\\text{{ cm}}$.\n\n"
        f"Calculate its **volume** ($V$) both in terms of $\\pi$ and rounded to two decimal places."
    )
    ans = f"{k_pi}\\pi \\approx {vol_s}\\text{{ cm}}^3"
    sol = f"$V = \\pi r^2 h = \\pi({rad})^2({h_v}) = {k_pi}\\pi \\approx {vol_s}\\text{{ cm}}^3$."
    return _make_q(
        r, "19_volume_of_right_circular_cylinder_svg", 19, prompt, ans, sol, 3,
        ["used_2_pi_r_h_for_cylinder_volume"],
        [{"step": 1, "criterion": f"Exact volume = {k_pi}*pi", "marks": 2}, {"step": 2, "criterion": f"Rounded = {vol_s} cm^3", "marks": 1}],
        {"tier_1": "Volume of a cylinder is base area * height = pi * r^2 * h.", "tier_2": f"pi * {rad}^2 * {h_v} = {k_pi}*pi", "tier_3": ans},
        diag,
    )


# 20. Curved lateral surface area of cylinder
def build_20_curved_lateral_surface_area_of_cylinder(r: random.Random) -> Dict[str, Any]:
    rad = r.randint(4, 14)
    h_v = r.randint(10, 25)
    k_pi = 2 * rad * h_v
    area_s = _fmt(math.pi * k_pi, 2)
    prompt = (
        f"A cylindrical garden roller has a radius of $r = {rad}\\text{{ cm}}$ and a width (length) of $h = {h_v}\\text{{ cm}}$.\n\n"
        f"Calculate the **curved (lateral) surface area** that touches the ground in one complete revolution, correct to two decimal places."
    )
    ans = f"{k_pi}\\pi \\approx {area_s}\\text{{ cm}}^2"
    sol = f"$\\text{{Curved SA}} = 2\\pi r h = 2\\pi({rad})({h_v}) = {k_pi}\\pi \\approx {area_s}\\text{{ cm}}^2$."
    return _make_q(
        r, "20_curved_lateral_surface_area_of_cylinder", 20, prompt, ans, sol, 2,
        ["included_circular_ends_in_lateral_surface_area"],
        [{"step": 1, "criterion": f"2*pi*{rad}*{h_v} = {k_pi}*pi", "marks": 1}, {"step": 2, "criterion": f"{area_s} cm^2", "marks": 1}],
        {"tier_1": "The curved surface unrolls into a rectangle of length 2*pi*r and height h.", "tier_2": f"2*pi*{rad}*{h_v} = {k_pi}*pi.", "tier_3": ans},
    )


# 21. Total surface area closed cylinder (with inline_svg)
def build_21_total_surface_area_closed_cylinder_svg(r: random.Random) -> Dict[str, Any]:
    rad = r.randint(3, 12)
    h_v = r.randint(7, 20)
    k_pi = 2 * (rad ** 2) + 2 * rad * h_v
    tsa_s = _fmt(math.pi * k_pi, 2)
    diag = _svg_3d_prism_cyl("cylinder", rad, h_v)
    prompt = (
        f"Refer to the **closed** right circular cylinder with radius $r = {rad}\\text{{ cm}}$ and height $h = {h_v}\\text{{ cm}}$.\n\n"
        f"Calculate its **Total Surface Area** ($TSA = 2\\pi r^2 + 2\\pi r h$), correct to two decimal places."
    )
    ans = f"{k_pi}\\pi \\approx {tsa_s}\\text{{ cm}}^2"
    sol = f"$TSA = 2\\pi({rad})^2 + 2\\pi({rad})({h_v}) = {2*rad**2}\\pi + {2*rad*h_v}\\pi = {k_pi}\\pi \\approx {tsa_s}\\text{{ cm}}^2$."
    return _make_q(
        r, "21_total_surface_area_closed_cylinder_svg", 21, prompt, ans, sol, 3,
        ["counted_only_one_circular_end_for_closed_cylinder"],
        [{"step": 1, "criterion": f"2*pi*r^2 = {2*rad**2}*pi", "marks": 1}, {"step": 2, "criterion": f"2*pi*r*h = {2*rad*h_v}*pi", "marks": 1}, {"step": 3, "criterion": f"{tsa_s} cm^2", "marks": 1}],
        {"tier_1": "Add the two circular ends (2*pi*r^2) and the curved side (2*pi*r*h).", "tier_2": f"{2*rad**2}*pi + {2*rad*h_v}*pi = {k_pi}*pi.", "tier_3": ans},
        diag,
    )


# 22. Surface area open-top cylinder
def build_22_surface_area_open_top_cylinder(r: random.Random) -> Dict[str, Any]:
    rad = r.randint(4, 12)
    h_v = r.randint(6, 18)
    k_pi = (rad ** 2) + 2 * rad * h_v
    sa_s = _fmt(math.pi * k_pi, 2)
    prompt = (
        f"A cylindrical drinking glass (open at the top, closed at the bottom) has radius $r = {rad}\\text{{ cm}}$ and height $h = {h_v}\\text{{ cm}}$.\n\n"
        f"Calculate its outer surface area ($\\pi r^2 + 2\\pi r h$), correct to two decimal places."
    )
    ans = f"{k_pi}\\pi \\approx {sa_s}\\text{{ cm}}^2"
    sol = f"$SA = \\pi({rad})^2 + 2\\pi({rad})({h_v}) = {rad**2}\\pi + {2*rad*h_v}\\pi = {k_pi}\\pi \\approx {sa_s}\\text{{ cm}}^2$."
    return _make_q(
        r, "22_surface_area_open_top_cylinder", 22, prompt, ans, sol, 3,
        ["used_2_pi_r2_for_open_top_cylinder"],
        [{"step": 1, "criterion": f"One base = {rad**2}*pi", "marks": 1}, {"step": 2, "criterion": f"Curved side = {2*rad*h_v}*pi", "marks": 1}, {"step": 3, "criterion": f"SA = {sa_s} cm^2", "marks": 1}],
        {"tier_1": "An open-top cylinder has only ONE circular base (pi*r^2) plus the curved wall (2*pi*r*h).", "tier_2": f"{rad**2}*pi + {2*rad*h_v}*pi = {k_pi}*pi.", "tier_3": ans},
    )


# 23. Find missing height or radius from cylinder volume
def build_23_find_missing_height_or_radius_from_cylinder_volume(r: random.Random) -> Dict[str, Any]:
    rad = r.randint(3, 10)
    h_v = r.randint(7, 20)
    vol_coeff = (rad ** 2) * h_v
    prompt = (
        f"A right circular cylinder has a volume of ${vol_coeff}\\pi\\text{{ cm}}^3$ and a base radius of $r = {rad}\\text{{ cm}}$.\n\n"
        f"Calculate the perpendicular **height** ($h$) of the cylinder."
    )
    ans = f"{h_v}\\text{{ cm}}"
    sol = f"$\\pi({rad})^2 h = {vol_coeff}\\pi \\implies {rad**2}h = {vol_coeff} \\implies h = \\frac{{{vol_coeff}}}{{{rad**2}}} = {h_v}\\text{{ cm}}$."
    return _make_q(
        r, "23_find_missing_height_or_radius_from_cylinder_volume", 23, prompt, ans, sol, 2,
        ["divided_by_r_instead_of_r_squared"],
        [{"step": 1, "criterion": f"{rad**2}*h = {vol_coeff}", "marks": 1}, {"step": 2, "criterion": f"h = {h_v} cm", "marks": 1}],
        {"tier_1": f"Substitute V = {vol_coeff}*pi and r = {rad} into V = pi*r^2*h.", "tier_2": f"h = {vol_coeff} / {rad**2}.", "tier_3": ans},
    )


# 24. Volume of hollow cylindrical pipe
def build_24_volume_of_hollow_cylindrical_pipe(r: random.Random) -> Dict[str, Any]:
    r_in = r.randint(3, 8)
    r_out = r_in + r.randint(2, 5)
    h_v = r.randint(10, 30)
    k_pi = (r_out ** 2 - r_in ** 2) * h_v
    vol_s = _fmt(math.pi * k_pi, 2)
    prompt = (
        f"A hollow metal pipe has an outer radius of $R = {r_out}\\text{{ cm}}$, an inner radius of $r = {r_in}\\text{{ cm}}$, "
        f"and a length of $h = {h_v}\\text{{ cm}}$.\n\n"
        f"Calculate the **volume of metal** in the pipe, correct to two decimal places."
    )
    ans = f"{k_pi}\\pi \\approx {vol_s}\\text{{ cm}}^3"
    sol = f"$V = \\pi(R^2 - r^2)h = \\pi({r_out}^2 - {r_in}^2)({h_v}) = {k_pi}\\pi \\approx {vol_s}\\text{{ cm}}^3$."
    return _make_q(
        r, "24_volume_of_hollow_cylindrical_pipe", 24, prompt, ans, sol, 3,
        ["used_R_minus_r_squared_instead_of_R2_minus_r2"],
        [{"step": 1, "criterion": f"R^2 - r^2 = {r_out**2 - r_in**2}", "marks": 1}, {"step": 2, "criterion": f"Exact = {k_pi}*pi", "marks": 1}, {"step": 3, "criterion": f"{vol_s} cm^3", "marks": 1}],
        {"tier_1": "Subtract the inner cylinder volume from the outer cylinder volume: pi*(R^2 - r^2)*h.", "tier_2": f"pi*({r_out**2} - {r_in**2})*{h_v} = {k_pi}*pi.", "tier_3": ans},
    )


# 25. Volume of trapezoidal prism trough
def build_25_volume_of_trapezoidal_prism_trough(r: random.Random) -> Dict[str, Any]:
    a_v = r.randint(4, 10)
    b_v = a_v + r.choice([4, 6, 8])
    h_trap = r.randint(3, 8)
    len_trough = r.randint(12, 25)
    area_trap = ((a_v + b_v) * h_trap) // 2
    vol = area_trap * len_trough
    prompt = (
        f"A water trough is a right prism whose cross-section is a trapezium with parallel widths $a = {a_v}\\text{{ dm}}$ "
        f"and $b = {b_v}\\text{{ dm}}$, perpendicular depth $h = {h_trap}\\text{{ dm}}$, and length $L = {len_trough}\\text{{ dm}}$.\n\n"
        f"Calculate the **volume** of the trough in $\\text{{dm}}^3$."
    )
    ans = f"{vol}\\text{{ dm}}^3"
    sol = f"$A_{{\\text{{cross-section}}}} = \\frac{{1}}{{2}}({a_v} + {b_v})({h_trap}) = {area_trap}\\text{{ dm}}^2$. Volume $V = {area_trap} \\times {len_trough} = {vol}\\text{{ dm}}^3$."
    return _make_q(
        r, "25_volume_of_trapezoidal_prism_trough", 25, prompt, ans, sol, 3,
        ["forgot_half_in_trapezium_cross_section"],
        [{"step": 1, "criterion": f"Cross-section area = {area_trap} dm^2", "marks": 2}, {"step": 2, "criterion": f"Volume = {vol} dm^3", "marks": 1}],
        {"tier_1": "Multiply the area of the trapezoidal cross-section by the length L.", "tier_2": f"Cross-section = {area_trap} dm^2; Volume = {area_trap} * {len_trough}.", "tier_3": ans},
    )


ARCHETYPES_01_25 = {
    "01_perimeter_and_area_of_rectangle_svg": build_01_perimeter_and_area_of_rectangle_svg,
    "02_area_of_square_from_perimeter_or_diagonal": build_02_area_of_square_from_perimeter_or_diagonal,
    "03_area_of_triangle_base_and_perpendicular_height_svg": build_03_area_of_triangle_base_and_perpendicular_height_svg,
    "04_area_of_isosceles_triangle_via_pythagoras_svg": build_04_area_of_isosceles_triangle_via_pythagoras_svg,
    "05_area_of_parallelogram_with_pythagoras_height_svg": build_05_area_of_parallelogram_with_pythagoras_height_svg,
    "06_area_of_trapezium_parallel_sides_svg": build_06_area_of_trapezium_parallel_sides_svg,
    "07_area_of_rhombus_and_kite_from_diagonals": build_07_area_of_rhombus_and_kite_from_diagonals,
    "08_circumference_and_area_of_circle_svg": build_08_circumference_and_area_of_circle_svg,
    "09_perimeter_and_area_of_semicircle_svg": build_09_perimeter_and_area_of_semicircle_svg,
    "10_area_of_annulus_concentric_circles_svg": build_10_area_of_annulus_concentric_circles_svg,
    "11_composite_2d_shape_rectangle_plus_semicircle_svg": build_11_composite_2d_shape_rectangle_plus_semicircle_svg,
    "12_map_scale_conversion_perimeter_and_area": build_12_map_scale_conversion_perimeter_and_area,
    "13_volume_of_rectangular_prism_cuboid_svg": build_13_volume_of_rectangular_prism_cuboid_svg,
    "14_total_surface_area_closed_rectangular_prism_svg": build_14_total_surface_area_closed_rectangular_prism_svg,
    "15_surface_area_open_top_rectangular_box": build_15_surface_area_open_top_rectangular_box,
    "16_cube_surface_area_and_volume_from_edge": build_16_cube_surface_area_and_volume_from_edge,
    "17_volume_of_right_triangular_prism_svg": build_17_volume_of_right_triangular_prism_svg,
    "18_total_surface_area_right_triangular_prism_svg": build_18_total_surface_area_right_triangular_prism_svg,
    "19_volume_of_right_circular_cylinder_svg": build_19_volume_of_right_circular_cylinder_svg,
    "20_curved_lateral_surface_area_of_cylinder": build_20_curved_lateral_surface_area_of_cylinder,
    "21_total_surface_area_closed_cylinder_svg": build_21_total_surface_area_closed_cylinder_svg,
    "22_surface_area_open_top_cylinder": build_22_surface_area_open_top_cylinder,
    "23_find_missing_height_or_radius_from_cylinder_volume": build_23_find_missing_height_or_radius_from_cylinder_volume,
    "24_volume_of_hollow_cylindrical_pipe": build_24_volume_of_hollow_cylindrical_pipe,
    "25_volume_of_trapezoidal_prism_trough": build_25_volume_of_trapezoidal_prism_trough,
}
