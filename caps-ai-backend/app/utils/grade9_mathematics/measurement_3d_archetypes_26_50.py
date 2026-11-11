"""Grade 9 Mathematics - Measurement of 3D Objects Archetypes 26-50 (CAPS Term 4).
Focus: Volume of Prisms & Cylinders, Capacity, Unit Conversions, Rate of Flow, Scaling, and Synthesis.
100% deterministic, zero LLM calls.
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional

from app.utils.grade9_mathematics.measurement_3d_svg import (
    draw_dimensioned_cube_svg,
    draw_dimensioned_cylinder_svg,
    draw_dimensioned_rectangular_prism_svg,
    draw_dimensioned_triangular_prism_svg,
)


def _fmt(val: float, decimals: int = 2) -> str:
    s = f"{val:.{decimals}f}"
    return s.replace(".", "{,}")


# -----------------------------------------------------------------------------
# 26. Volume of cube (integer edge)
# -----------------------------------------------------------------------------
def arch_26_volume_of_cube_integer_edge(r: random.Random) -> Dict[str, Any]:
    s = r.choice([3, 4, 5, 6, 7, 8, 9, 10, 12])
    unit = r.choice(["cm", "m", "mm"])
    vol = s ** 3
    seed_val = r.randint(100, 999999)
    svg = draw_dimensioned_cube_svg(s, unit=unit, seed=seed_val)

    prompt = (
        f"A cube has edge length $s = {s}\\text{{ {unit}}}$. "
        f"Calculate the volume of the cube."
    )
    ans_str = str(vol)
    sol = (
        f"$$\\text{{Volume}} = s^3 = ({s})^3 = {s} \\times {s} \\times {s} = {vol}\\text{{ {unit}}}^3$$"
    )
    return {
        "subskill": "26_volume_of_cube_integer_edge",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": ans_str,
        "sample_answer": f"{ans_str} {unit}³",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Formula: V = s³", "marks": 1},
            {"step": f"Answer: {vol}", "marks": 1},
        ],
        "hints": [
            "Volume of a cube is the edge length cubed: $V = s^3$.",
            f"Calculate ${s} \\times {s} \\times {s} = {vol}$.",
        ],
        "misconception_tags": ["cube_volume_multiplied_by_six_instead_of_cubing"],
    }


# -----------------------------------------------------------------------------
# 27. Volume of cube (decimal edge)
# -----------------------------------------------------------------------------
def arch_27_volume_of_cube_decimal_edge(r: random.Random) -> Dict[str, Any]:
    s = round(r.choice([1.5, 2.5, 3.2, 4.5]), 1)
    vol = round(s ** 3, 2)
    seed_val = r.randint(100, 999999)
    svg = draw_dimensioned_cube_svg(s, unit="cm", seed=seed_val)

    prompt = (
        f"A cube has side length $s = {_fmt(s, 1)}\\text{{ cm}}$. "
        f"Calculate its volume in cubic centimetres to two decimal places."
    )
    ans_str = f"{vol:.2f}".rstrip("0").rstrip(".")
    sol = (
        f"$$\\text{{Volume}} = s^3 = ({_fmt(s, 1)})^3 = {_fmt(vol, 2)}\\text{{ cm}}^3$$"
    )
    return {
        "subskill": "27_volume_of_cube_decimal_edge",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": ans_str,
        "sample_answer": f"{ans_str} cm³",
        "tolerance": 0.05,
        "marking_schema": [
            {"step": "Formula: V = s³", "marks": 1},
            {"step": f"Answer: {ans_str}", "marks": 1},
        ],
        "hints": [
            f"Cube the side length: $({_fmt(s, 1)})^3 = {_fmt(vol, 2)}$.",
        ],
        "misconception_tags": ["decimal_cubing_error"],
    }


# -----------------------------------------------------------------------------
# 28. Find cube edge given volume
# -----------------------------------------------------------------------------
def arch_28_find_cube_edge_given_volume(r: random.Random) -> Dict[str, Any]:
    s = r.choice([2, 3, 4, 5, 6, 7, 8, 9, 10])
    vol = s ** 3
    seed_val = r.randint(100, 999999)
    svg = draw_dimensioned_cube_svg("s", unit="cm", seed=seed_val)

    prompt = (
        f"A cube has a volume of ${vol}\\text{{ cm}}^3$. "
        f"Calculate the edge length ($s$) of the cube in centimetres."
    )
    ans_str = str(s)
    sol = (
        f"$$V = s^3 = {vol}$$\n"
        f"$$s = \\sqrt[3]{{{vol}}} = {s}\\text{{ cm}}$$"
    )
    return {
        "subskill": "28_find_cube_edge_given_volume",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": ans_str,
        "sample_answer": f"{ans_str} cm",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Cube root of volume: cbrt({vol})", "marks": 1},
            {"step": f"Answer: {s}", "marks": 1},
        ],
        "hints": [
            "To find the side of a cube from its volume, take the cube root ($\\sqrt[3]{V}$).",
            f"$\\sqrt[3]{{{vol}}} = {s}\\text{{ cm}}$.",
        ],
        "misconception_tags": ["took_square_root_instead_of_cube_root"],
    }


# -----------------------------------------------------------------------------
# 29. Volume of rectangular prism (integer dimensions)
# -----------------------------------------------------------------------------
def arch_29_volume_of_rectangular_prism_integer_dims(r: random.Random) -> Dict[str, Any]:
    l = r.choice([5, 6, 8, 10, 12])
    b = r.choice([3, 4, 5, 6])
    h = r.choice([2, 3, 4, 5, 8])
    unit = "cm"
    vol = l * b * h
    seed_val = r.randint(100, 999999)
    svg = draw_dimensioned_rectangular_prism_svg(l, b, h, unit=unit, seed=seed_val)

    prompt = (
        f"A rectangular prism has length $l = {l}\\text{{ {unit}}}$, breadth $b = {b}\\text{{ {unit}}}$, "
        f"and height $h = {h}\\text{{ {unit}}}$. Calculate its volume."
    )
    ans_str = str(vol)
    sol = (
        f"$$\\text{{Volume}} = l \\times b \\times h = {l} \\times {b} \\times {h} = {vol}\\text{{ {unit}}}^3$$"
    )
    return {
        "subskill": "29_volume_of_rectangular_prism_integer_dims",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": ans_str,
        "sample_answer": f"{ans_str} {unit}³",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Formula: V = l × b × h", "marks": 1},
            {"step": f"Answer: {vol}", "marks": 1},
        ],
        "hints": [
            "Multiply length by breadth by height.",
            f"${l} \\times {b} \\times {h} = {vol}\\text{{ {unit}}}^3$.",
        ],
        "misconception_tags": ["prism_volume_formula_error"],
    }


# -----------------------------------------------------------------------------
# 30. Volume of rectangular prism (decimal dimensions)
# -----------------------------------------------------------------------------
def arch_30_volume_of_rectangular_prism_decimal_dims(r: random.Random) -> Dict[str, Any]:
    l = round(r.choice([4.5, 5.2, 6.0]), 1)
    b = round(r.choice([2.5, 3.0, 3.5]), 1)
    h = round(r.choice([1.2, 1.8, 2.4]), 1)
    unit = "m"
    vol = round(l * b * h, 2)
    seed_val = r.randint(100, 999999)
    svg = draw_dimensioned_rectangular_prism_svg(l, b, h, unit=unit, seed=seed_val)

    prompt = (
        f"A rectangular concrete pillar has length $l = {_fmt(l, 1)}\\text{{ m}}$, "
        f"breadth $b = {_fmt(b, 1)}\\text{{ m}}$, and height $h = {_fmt(h, 1)}\\text{{ m}}$. "
        f"Calculate the volume of concrete required in cubic metres."
    )
    ans_str = f"{vol:.2f}".rstrip("0").rstrip(".")
    sol = (
        f"$$\\text{{Volume}} = l \\times b \\times h = {_fmt(l, 1)} \\times {_fmt(b, 1)} \\times {_fmt(h, 1)} = {_fmt(vol, 2)}\\text{{ m}}^3$$"
    )
    return {
        "subskill": "30_volume_of_rectangular_prism_decimal_dims",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": ans_str,
        "sample_answer": f"{ans_str} m³",
        "tolerance": 0.05,
        "marking_schema": [
            {"step": "Formula: V = l × b × h", "marks": 1},
            {"step": f"Answer: {ans_str}", "marks": 1},
        ],
        "hints": [
            f"Multiply the three dimensions: ${_fmt(l, 1)} \\times {_fmt(b, 1)} \\times {_fmt(h, 1)}$.",
            f"The volume is {_fmt(vol, 2)} m³.",
        ],
        "misconception_tags": ["decimal_multiplication_error"],
    }


# -----------------------------------------------------------------------------
# 31. Find rectangular prism missing dimension given volume
# -----------------------------------------------------------------------------
def arch_31_find_rectangular_prism_missing_dimension_given_volume(r: random.Random) -> Dict[str, Any]:
    l = r.choice([6, 8, 10, 12])
    b = r.choice([4, 5, 6])
    h = r.choice([3, 5, 7])
    vol = l * b * h
    seed_val = r.randint(100, 999999)
    svg = draw_dimensioned_rectangular_prism_svg(l, b, "h", unit="cm", seed=seed_val)

    prompt = (
        f"A rectangular carton has a volume of ${vol}\\text{{ cm}}^3$, length $l = {l}\\text{{ cm}}$, "
        f"and breadth $b = {b}\\text{{ cm}}$. Calculate the height ($h$) of the carton."
    )
    ans_str = str(h)
    sol = (
        f"$$\\text{{Volume}} = l \\times b \\times h = {vol}$$\n"
        f"$$h = \\frac{{V}}{{l \\times b}} = \\frac{{{vol}}}{{{l} \\times {b}}} = \\frac{{{vol}}}{{{l*b}}} = {h}\\text{{ cm}}$$"
    )
    return {
        "subskill": "31_find_rectangular_prism_missing_dimension_given_volume",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": ans_str,
        "sample_answer": f"{ans_str} cm",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Base area: {l} × {b} = {l*b}", "marks": 1},
            {"step": f"Height: {vol} / {l*b} = {h}", "marks": 1},
        ],
        "hints": [
            f"Divide volume by the base area ($l \\times b = {l*b}$).",
            f"${vol} \\div {l*b} = {h}\\text{{ cm}}$.",
        ],
        "misconception_tags": ["divided_by_only_one_dimension"],
    }


# -----------------------------------------------------------------------------
# 32. Volume of right triangular prism
# -----------------------------------------------------------------------------
def arch_32_volume_of_right_triangular_prism(r: random.Random) -> Dict[str, Any]:
    a = r.choice([3, 4, 6, 8])
    b = r.choice([4, 5, 8, 10])
    l_prism = r.choice([10, 12, 15, 20])
    unit = "cm"
    base_area = 0.5 * a * b
    vol = int(base_area * l_prism)
    seed_val = r.randint(100, 999999)
    svg = draw_dimensioned_triangular_prism_svg(b, a, l_prism, unit=unit, seed=seed_val)

    prompt = (
        f"A right-angled triangular prism has triangular base perpendicular legs $a = {a}\\text{{ {unit}}}$ "
        f"and $b = {b}\\text{{ {unit}}}$, and length $L = {l_prism}\\text{{ {unit}}}$. "
        f"Calculate the volume of the prism."
    )
    ans_str = str(vol)
    sol = (
        f"$$\\text{{Base Area}} = \\frac{{1}}{{2}} \\times a \\times b = \\frac{{1}}{{2}} \\times {a} \\times {b} = {int(base_area)}\\text{{ {unit}}}^2$$\n"
        f"$$\\text{{Volume}} = \\text{{Base Area}} \\times \\text{{Length}} = {int(base_area)} \\times {l_prism} = {vol}\\text{{ {unit}}}^3$$"
    )
    return {
        "subskill": "32_volume_of_right_triangular_prism",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": ans_str,
        "sample_answer": f"{ans_str} {unit}³",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Base area: 1/2 × {a} × {b} = {int(base_area)}", "marks": 1},
            {"step": f"Volume: {int(base_area)} × {l_prism} = {vol}", "marks": 1},
        ],
        "hints": [
            "Formula for triangular prism: $V = \\text{Area of triangular base} \\times \\text{Length}$.",
            f"Triangular base area: $\\frac{{1}}{{2}} \\times {a} \\times {b} = {int(base_area)}$.",
            f"Multiply by length: ${int(base_area)} \\times {l_prism} = {vol}$.",
        ],
        "misconception_tags": ["forgot_half_in_triangle_base_area"],
    }


# -----------------------------------------------------------------------------
# 33. Volume of isosceles triangular prism
# -----------------------------------------------------------------------------
def arch_33_volume_of_isosceles_triangular_prism(r: random.Random) -> Dict[str, Any]:
    b = r.choice([6, 8, 10, 12])
    h_tri = r.choice([4, 5, 8])
    l_prism = r.choice([10, 15, 20])
    base_area = 0.5 * b * h_tri
    vol = int(base_area * l_prism)
    seed_val = r.randint(100, 999999)
    svg = draw_dimensioned_triangular_prism_svg(b, h_tri, l_prism, unit="cm", seed=seed_val)

    prompt = (
        f"An isosceles triangular prism has a base of width $b = {b}\\text{{ cm}}$, "
        f"perpendicular height $h = {h_tri}\\text{{ cm}}$, and length $L = {l_prism}\\text{{ cm}}$. "
        f"Calculate the volume of the prism."
    )
    ans_str = str(vol)
    sol = (
        f"$$\\text{{Base Area}} = \\frac{{1}}{{2}} \\times b \\times h = \\frac{{1}}{{2}} \\times {b} \\times {h_tri} = {int(base_area)}\\text{{ cm}}^2$$\n"
        f"$$\\text{{Volume}} = \\text{{Base Area}} \\times L = {int(base_area)} \\times {l_prism} = {vol}\\text{{ cm}}^3$$"
    )
    return {
        "subskill": "33_volume_of_isosceles_triangular_prism",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": ans_str,
        "sample_answer": f"{ans_str} cm³",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Base area: {int(base_area)}", "marks": 1},
            {"step": f"Volume: {vol}", "marks": 1},
        ],
        "hints": [
            f"Triangular base area: $\\frac{{1}}{{2}} \\times {b} \\times {h_tri} = {int(base_area)}$.",
            f"Multiply by length: ${int(base_area)} \\times {l_prism} = {vol}\\text{{ cm}}^3$.",
        ],
        "misconception_tags": ["triangular_prism_volume_error"],
    }


# -----------------------------------------------------------------------------
# 34. Find triangular prism length given volume and base area
# -----------------------------------------------------------------------------
def arch_34_find_triangular_prism_length_given_volume_and_base_area(r: random.Random) -> Dict[str, Any]:
    b = 8
    h_tri = 6
    base_area = int(0.5 * b * h_tri)  # 24
    l_prism = r.choice([10, 12, 15, 18, 20])
    vol = base_area * l_prism
    seed_val = r.randint(100, 999999)
    svg = draw_dimensioned_triangular_prism_svg(b, h_tri, "L", unit="cm", seed=seed_val)

    prompt = (
        f"A triangular prism has a volume of ${vol}\\text{{ cm}}^3$ and a triangular cross-sectional base "
        f"with base $8\\text{{ cm}}$ and height $6\\text{{ cm}}$. "
        f"Calculate the length ($L$) of the prism."
    )
    ans_str = str(l_prism)
    sol = (
        f"$$\\text{{Base Area}} = \\frac{{1}}{{2}} \\times 8 \\times 6 = {base_area}\\text{{ cm}}^2$$\n"
        f"$$L = \\frac{{\\text{{Volume}}}}{{\\text{{Base Area}}}} = \\frac{{{vol}}}{{{base_area}}} = {l_prism}\\text{{ cm}}$$"
    )
    return {
        "subskill": "34_find_triangular_prism_length_given_volume_and_base_area",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": ans_str,
        "sample_answer": f"{ans_str} cm",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Base area: 1/2 × 8 × 6 = {base_area}", "marks": 1},
            {"step": f"Length: {vol} / {base_area} = {l_prism}", "marks": 1},
        ],
        "hints": [
            f"Find the base area: $\\frac{{1}}{{2}} \\times 8 \\times 6 = {base_area}$.",
            f"Divide volume by base area: ${vol} \\div {base_area} = {l_prism}\\text{{ cm}}$.",
        ],
        "misconception_tags": ["triangular_prism_length_rearrangement_error"],
    }


# -----------------------------------------------------------------------------
# 35. Volume of cylinder given radius and height
# -----------------------------------------------------------------------------
def arch_35_volume_of_cylinder_given_radius_and_height(r: random.Random) -> Dict[str, Any]:
    radius = r.choice([3, 4, 5, 7, 10])
    h = r.choice([6, 8, 10, 14, 20])
    unit = "cm"
    vol = math.pi * (radius ** 2) * h
    vol_round = round(vol, 2)
    seed_val = r.randint(100, 999999)
    svg = draw_dimensioned_cylinder_svg(radius, h, unit=unit, is_open_top=False, seed=seed_val)

    prompt = (
        f"A cylinder has radius $r = {radius}\\text{{ {unit}}}$ and height $h = {h}\\text{{ {unit}}}$. "
        f"Calculate the volume of the cylinder to two decimal places."
    )
    ans_str = f"{vol_round:.2f}".rstrip("0").rstrip(".")
    sol = (
        f"$$\\text{{Volume}} = \\pi r^2 h = \\pi ({radius})^2 ({h}) = {radius**2}\\pi \\times {h} = {radius**2 * h}\\pi \\approx {_fmt(vol_round, 2)}\\text{{ {unit}}}^3$$"
    )
    return {
        "subskill": "35_volume_of_cylinder_given_radius_and_height",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": ans_str,
        "sample_answer": f"{ans_str} {unit}³",
        "tolerance": 0.1,
        "marking_schema": [
            {"step": "Formula: V = πr²h", "marks": 1},
            {"step": f"Substitution: π({radius})²({h})", "marks": 1},
            {"step": f"Answer: {ans_str}", "marks": 1},
        ],
        "hints": [
            "Formula for cylinder volume: $V = \\pi r^2 h$.",
            f"Base area: $\\pi \\times {radius}^2 = {radius**2}\\pi$.",
            f"Multiply by height: ${radius**2}\\pi \\times {h} \\approx {_fmt(vol_round, 2)}$.",
        ],
        "misconception_tags": ["used_2_pi_r_instead_of_pi_r_squared"],
    }


# -----------------------------------------------------------------------------
# 36. Volume of cylinder given diameter and height
# -----------------------------------------------------------------------------
def arch_36_volume_of_cylinder_given_diameter_and_height(r: random.Random) -> Dict[str, Any]:
    diam = r.choice([6, 8, 10, 14, 20])
    radius = diam / 2.0
    h = r.choice([10, 12, 15, 20])
    unit = "cm"
    vol = math.pi * (radius ** 2) * h
    vol_round = round(vol, 2)
    seed_val = r.randint(100, 999999)
    svg = draw_dimensioned_cylinder_svg(int(radius), h, unit=unit, is_open_top=False, seed=seed_val)

    prompt = (
        f"A cylindrical storage silo has diameter $d = {diam}\\text{{ {unit}}}$ and height $h = {h}\\text{{ {unit}}}$. "
        f"Calculate its volume in cubic {unit} to two decimal places."
    )
    ans_str = f"{vol_round:.2f}".rstrip("0").rstrip(".")
    sol = (
        f"1. **Radius**: $r = \\frac{{{diam}}}{{2}} = {int(radius)}\\text{{ {unit}}}$.\n\n"
        f"2. **Volume**:\n"
        f"$$V = \\pi r^2 h = \\pi ({int(radius)})^2 ({h}) = {int(radius**2 * h)}\\pi \\approx {_fmt(vol_round, 2)}\\text{{ {unit}}}^3$$"
    )
    return {
        "subskill": "36_volume_of_cylinder_given_diameter_and_height",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": ans_str,
        "sample_answer": f"{ans_str} {unit}³",
        "tolerance": 0.1,
        "marking_schema": [
            {"step": f"Radius: r = {diam}/2 = {int(radius)}", "marks": 1},
            {"step": "Formula: V = πr²h", "marks": 1},
            {"step": f"Answer: {ans_str}", "marks": 1},
        ],
        "hints": [
            f"Halve diameter first: $r = {diam} \\div 2 = {int(radius)}$.",
            f"Use $V = \\pi r^2 h = \\pi \\times {int(radius)}^2 \\times {h}$.",
        ],
        "misconception_tags": ["used_diameter_in_volume_formula"],
    }


# -----------------------------------------------------------------------------
# 37. Find cylinder height given volume and radius
# -----------------------------------------------------------------------------
def arch_37_find_cylinder_height_given_volume_and_radius(r: random.Random) -> Dict[str, Any]:
    radius = r.choice([3, 4, 5, 7])
    h = r.choice([5, 8, 10, 12, 15])
    vol = round(math.pi * (radius ** 2) * h, 1)
    seed_val = r.randint(100, 999999)
    svg = draw_dimensioned_cylinder_svg(radius, "h", unit="cm", is_open_top=False, seed=seed_val)

    prompt = (
        f"A cylinder with radius $r = {radius}\\text{{ cm}}$ has a volume of ${_fmt(vol, 1)}\\text{{ cm}}^3$. "
        f"Calculate the height ($h$) of the cylinder to the nearest whole centimetre."
    )
    ans_str = str(h)
    sol = (
        f"$$V = \\pi r^2 h = {_fmt(vol, 1)}$$\n"
        f"$$h = \\frac{{V}}{{\\pi r^2}} = \\frac{{{_fmt(vol, 1)}}}{{\\pi \\times {radius}^2}} = \\frac{{{_fmt(vol, 1)}}}{{{radius**2}\\pi}} \\approx {h}\\text{{ cm}}$$"
    )
    return {
        "subskill": "37_find_cylinder_height_given_volume_and_radius",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": ans_str,
        "sample_answer": f"{ans_str} cm",
        "tolerance": 0.5,
        "marking_schema": [
            {"step": f"Base area: π × {radius}² = {radius**2}π", "marks": 1},
            {"step": f"Height: {vol} / ({radius**2}π) = {h}", "marks": 1},
        ],
        "hints": [
            f"Base area = $\\pi \\times {radius}^2 = {radius**2}\\pi \\approx {_fmt(math.pi * radius**2, 2)}$.",
            f"Divide volume by base area: ${vol} \\div {_fmt(math.pi * radius**2, 2)} \\approx {h}$.",
        ],
        "misconception_tags": ["cylinder_height_rearrangement_error"],
    }


# -----------------------------------------------------------------------------
# 38. Find cylinder radius given volume and height
# -----------------------------------------------------------------------------
def arch_38_find_cylinder_radius_given_volume_and_height(r: random.Random) -> Dict[str, Any]:
    radius = r.choice([3, 4, 5, 7, 10])
    h = r.choice([8, 10, 12, 14])
    vol = round(math.pi * (radius ** 2) * h, 1)
    seed_val = r.randint(100, 999999)
    svg = draw_dimensioned_cylinder_svg("r", h, unit="cm", is_open_top=False, seed=seed_val)

    prompt = (
        f"A cylindrical tank has height $h = {h}\\text{{ cm}}$ and a volume of ${_fmt(vol, 1)}\\text{{ cm}}^3$. "
        f"Calculate the radius ($r$) of the tank to the nearest whole centimetre."
    )
    ans_str = str(radius)
    sol = (
        f"$$V = \\pi r^2 h = {_fmt(vol, 1)}$$\n"
        f"$$r^2 = \\frac{{V}}{{\\pi h}} = \\frac{{{_fmt(vol, 1)}}}{{\\pi \\times {h}}} \\approx {radius**2}$$\n"
        f"$$r = \\sqrt{{{radius**2}}} = {radius}\\text{{ cm}}$$"
    )
    return {
        "subskill": "38_find_cylinder_radius_given_volume_and_height",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": ans_str,
        "sample_answer": f"{ans_str} cm",
        "tolerance": 0.5,
        "marking_schema": [
            {"step": f"Divide volume by πh: {vol} / ({h}π) = {radius**2}", "marks": 1},
            {"step": f"Take square root: sqrt({radius**2}) = {radius}", "marks": 1},
        ],
        "hints": [
            f"Divide volume by $(\\pi \\times {h})$ to find $r^2$.",
            f"Take the square root of $r^2$ to find $r = {radius}\\text{{ cm}}$.",
        ],
        "misconception_tags": ["forgot_square_root_in_cylinder_radius"],
    }


# -----------------------------------------------------------------------------
# 39. Capacity conversion: cm³ to millilitres
# -----------------------------------------------------------------------------
def arch_39_capacity_conversion_cm3_to_millilitres(r: random.Random) -> Dict[str, Any]:
    cm3 = r.choice([250, 330, 500, 750, 1200, 2500])
    ml = cm3  # 1 cm³ = 1 ml
    prompt = (
        f"A juice box has an interior volume of ${cm3}\\text{{ cm}}^3$. "
        f"Convert this volume to capacity in millilitres ($\\text{{ml}}$)."
    )
    ans_str = str(ml)
    sol = (
        f"By curriculum definition:\n"
        f"$$1\\text{{ cm}}^3 = 1\\text{{ ml}}$$\n"
        f"Therefore, ${cm3}\\text{{ cm}}^3 = **{ml}\\text{{ ml}}**$."
    )
    return {
        "subskill": "39_capacity_conversion_cm3_to_millilitres",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": ans_str,
        "sample_answer": f"{ans_str} ml",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "State 1 cm³ = 1 ml", "marks": 1},
            {"step": f"Answer: {ml} ml", "marks": 1},
        ],
        "hints": [
            "Remember the fundamental conversion: $1\\text{ cm}^3 = 1\\text{ ml}$.",
            f"So ${cm3}\\text{{ cm}}^3 = {ml}\\text{{ ml}}$.",
        ],
        "misconception_tags": ["cm3_to_ml_conversion_factor_confusion"],
    }


# -----------------------------------------------------------------------------
# 40. Capacity conversion: cm³ to litres
# -----------------------------------------------------------------------------
def arch_40_capacity_conversion_cm3_to_litres(r: random.Random) -> Dict[str, Any]:
    litres = round(r.choice([1.5, 2.0, 2.5, 3.2, 5.0, 8.5]), 1)
    cm3 = int(litres * 1000)
    prompt = (
        f"A milk carton has a volume of ${cm3}\\text{{ cm}}^3$. "
        f"Convert this volume to capacity in litres ($\\text{{L}}$)."
    )
    ans_str = f"{litres:.1f}".rstrip("0").rstrip(".")
    sol = (
        f"Since $1\\text{{ L}} = 1\\,000\\text{{ cm}}^3$:\n"
        f"$$\\text{{Capacity}} = \\frac{{{cm3}}}{{1\\,000}} = {_fmt(litres, 1)}\\text{{ L}}$$"
    )
    return {
        "subskill": "40_capacity_conversion_cm3_to_litres",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": ans_str,
        "sample_answer": f"{ans_str} L",
        "tolerance": 0.01,
        "marking_schema": [
            {"step": f"Divide by 1000: {cm3} / 1000", "marks": 1},
            {"step": f"Answer: {ans_str} L", "marks": 1},
        ],
        "hints": [
            "$1\\text{ litre} = 1\\,000\\text{ cm}^3$.",
            f"Divide by 1000: ${cm3} \\div 1\\,000 = {_fmt(litres, 1)}\\text{{ L}}$.",
        ],
        "misconception_tags": ["multiplied_by_1000_instead_of_dividing"],
    }


# -----------------------------------------------------------------------------
# 41. Capacity conversion: m³ to kilolitres / litres
# -----------------------------------------------------------------------------
def arch_41_capacity_conversion_m3_to_kilolitres(r: random.Random) -> Dict[str, Any]:
    m3 = r.choice([3, 5, 8, 12, 15, 25])
    litres = m3 * 1000  # 1 m³ = 1000 L = 1 kL
    prompt = (
        f"A municipal swimming pool holds ${m3}\\text{{ m}}^3$ of water. "
        f"Calculate the capacity of the pool in litres ($\\text{{L}}$)."
    )
    ans_str = str(litres)
    sol = (
        f"Since $1\\text{{ m}}^3 = 1\\,000\\text{{ L}} = 1\\text{{ kL}}$:\n"
        f"$$\\text{{Capacity}} = {m3} \\times 1\\,000 = {litres}\\text{{ L}}$$"
    )
    return {
        "subskill": "41_capacity_conversion_m3_to_kilolitres",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": ans_str,
        "sample_answer": f"{ans_str} L ({m3} kL)",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "State 1 m³ = 1000 L", "marks": 1},
            {"step": f"Multiply by 1000: {m3} × 1000 = {litres}", "marks": 1},
        ],
        "hints": [
            "Remember: $1\\text{ cubic metre} = 1\\,000\\text{ litres}$.",
            f"Multiply by 1000: ${m3} \\times 1\\,000 = {litres}\\text{{ L}}$.",
        ],
        "misconception_tags": ["m3_to_litres_conversion_confusion"],
    }


# -----------------------------------------------------------------------------
# 42. Capacity conversion: litres to m³
# -----------------------------------------------------------------------------
def arch_42_capacity_conversion_litres_to_m3(r: random.Random) -> Dict[str, Any]:
    m3 = round(r.choice([2.5, 4.0, 7.5, 10.0, 15.5]), 1)
    litres = int(m3 * 1000)
    prompt = (
        f"A JoJo rainwater harvesting tank contains ${litres}\\text{{ litres}}$ of water. "
        f"Express this volume in cubic metres ($\\text{{m}}^3$)."
    )
    ans_str = f"{m3:.1f}".rstrip("0").rstrip(".")
    sol = (
        f"Since $1\\,000\\text{{ L}} = 1\\text{{ m}}^3$:\n"
        f"$$\\text{{Volume}} = \\frac{{{litres}}}{{1\\,000}} = {_fmt(m3, 1)}\\text{{ m}}^3$$"
    )
    return {
        "subskill": "42_capacity_conversion_litres_to_m3",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": ans_str,
        "sample_answer": f"{ans_str} m³",
        "tolerance": 0.05,
        "marking_schema": [
            {"step": f"Divide by 1000: {litres} / 1000", "marks": 1},
            {"step": f"Answer: {ans_str} m³", "marks": 1},
        ],
        "hints": [
            "To convert litres to cubic metres, divide by 1000.",
            f"${litres} \\div 1\\,000 = {_fmt(m3, 1)}\\text{{ m}}^3$.",
        ],
        "misconception_tags": ["litres_to_m3_division_error"],
    }


# -----------------------------------------------------------------------------
# 43. Liquid volume in partially filled rectangular tank
# -----------------------------------------------------------------------------
def arch_43_liquid_volume_in_partially_filled_rectangular_tank(r: random.Random) -> Dict[str, Any]:
    l = r.choice([2, 3, 4])  # m
    b = 2  # m
    h_total = 3  # m
    h_water = r.choice([1.5, 2.0, 2.5])  # water level depth
    vol_m3 = round(l * b * h_water, 2)
    litres = int(vol_m3 * 1000)
    seed_val = r.randint(100, 999999)
    svg = draw_dimensioned_rectangular_prism_svg(l, b, h_total, unit="m", seed=seed_val)

    prompt = (
        f"A rectangular water reservoir has length $l = {l}\\text{{ m}}$ and width $b = {b}\\text{{ m}}$. "
        f"The reservoir is filled with water to a depth of $d = {_fmt(h_water, 1)}\\text{{ m}}$. "
        f"Calculate the volume of water in the reservoir in litres ($\\text{{L}}$)."
    )
    ans_str = str(litres)
    sol = (
        f"1. **Volume of water in $\\text{{m}}^3$**:\n"
        f"$$V = l \\times b \\times d = {l} \\times {b} \\times {_fmt(h_water, 1)} = {_fmt(vol_m3, 1)}\\text{{ m}}^3$$\n\n"
        f"2. **Convert to litres** ($1\\text{{ m}}^3 = 1\\,000\\text{{ L}}$):\n"
        f"$$\\text{{Litres}} = {_fmt(vol_m3, 1)} \\times 1\\,000 = {litres}\\text{{ L}}$$"
    )
    return {
        "subskill": "43_liquid_volume_in_partially_filled_rectangular_tank",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": ans_str,
        "sample_answer": f"{ans_str} L",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Water volume in m³: {l} × {b} × {h_water} = {vol_m3}", "marks": 1},
            {"step": f"Convert to litres: {vol_m3} × 1000 = {litres}", "marks": 1},
        ],
        "hints": [
            "Use the depth of the water (not the total height of the tank) to calculate water volume.",
            f"Volume in $\\text{{m}}^3$: ${l} \\times {b} \\times {_fmt(h_water, 1)} = {_fmt(vol_m3, 1)}\\text{{ m}}^3$.",
            f"Multiply by 1000 to get litres: {litres} L.",
        ],
        "misconception_tags": ["used_tank_total_height_instead_of_water_depth"],
    }


# -----------------------------------------------------------------------------
# 44. Liquid volume in partially filled cylindrical JoJo tank
# -----------------------------------------------------------------------------
def arch_44_liquid_volume_in_partially_filled_cylindrical_jojo_tank(r: random.Random) -> Dict[str, Any]:
    radius = 1  # 1 m
    depth = r.choice([1.2, 1.5, 1.8, 2.0])  # m
    vol_m3 = math.pi * (radius ** 2) * depth
    litres = round(vol_m3 * 1000)
    seed_val = r.randint(100, 999999)
    svg = draw_dimensioned_cylinder_svg(radius, 2.5, unit="m", is_open_top=False, seed=seed_val)

    prompt = (
        f"A cylindrical JoJo tank has radius $r = 1\\text{{ m}}$. "
        f"Water is filled to a depth of $h = {_fmt(depth, 1)}\\text{{ m}}$. "
        f"Calculate the volume of water in litres to the nearest whole litre."
    )
    ans_str = str(litres)
    sol = (
        f"$$V = \\pi r^2 h = \\pi (1)^2 ({_fmt(depth, 1)}) = {_fmt(depth, 1)}\\pi \\approx {_fmt(vol_m3, 3)}\\text{{ m}}^3$$\n"
        f"$$\\text{{Litres}} = {_fmt(vol_m3, 3)} \\times 1\\,000 \\approx {litres}\\text{{ L}}$$"
    )
    return {
        "subskill": "44_liquid_volume_in_partially_filled_cylindrical_jojo_tank",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": ans_str,
        "sample_answer": f"{ans_str} L",
        "tolerance": 5.0,
        "marking_schema": [
            {"step": "Formula: V = πr²h (in m³)", "marks": 1},
            {"step": "Multiply by 1000 for litres", "marks": 1},
            {"step": f"Answer: {litres} L", "marks": 1},
        ],
        "hints": [
            f"Volume in $\\text{{m}}^3$: $\\pi \\times 1^2 \\times {_fmt(depth, 1)} \\approx {_fmt(vol_m3, 3)}\\text{{ m}}^3$.",
            f"Multiply by 1000 to convert to litres: ${litres}\\text{{ L}}$.",
        ],
        "misconception_tags": ["jojo_tank_capacity_conversion_error"],
    }


# -----------------------------------------------------------------------------
# 45. Rate of flow: Time to fill tank
# -----------------------------------------------------------------------------
def arch_45_rate_of_flow_time_to_fill_rectangular_or_cylindrical_tank(r: random.Random) -> Dict[str, Any]:
    flow_rate = r.choice([20, 25, 50])  # litres per minute
    time_min = r.choice([30, 40, 60, 90, 120])
    total_litres = flow_rate * time_min
    prompt = (
        f"A garden hose delivers water into an empty storage tank at a constant rate of ${flow_rate}\\text{{ litres per minute}}$. "
        f"If the capacity of the tank is ${total_litres}\\text{{ litres}}$, "
        f"calculate how many minutes it will take to fill the tank completely."
    )
    ans_str = str(time_min)
    sol = (
        f"$$\\text{{Time}} = \\frac{{\\text{{Capacity}}}}{{\\text{{Rate of Flow}}}} = \\frac{{{total_litres}\\text{{ L}}}}{{{flow_rate}\\text{{ L/min}}}} = {time_min}\\text{{ minutes}}$$"
    )
    return {
        "subskill": "45_rate_of_flow_time_to_fill_rectangular_or_cylindrical_tank",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": ans_str,
        "sample_answer": f"{ans_str} minutes",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Divide total litres by flow rate: {total_litres} / {flow_rate}", "marks": 1},
            {"step": f"Answer: {time_min} minutes", "marks": 1},
        ],
        "hints": [
            "Time = Total Volume ÷ Rate of Flow.",
            f"${total_litres} \\div {flow_rate} = {time_min}\\text{{ minutes}}$.",
        ],
        "misconception_tags": ["rate_of_flow_inversion_error"],
    }


# -----------------------------------------------------------------------------
# 46. Volume scaling effect: Doubling all dimensions
# -----------------------------------------------------------------------------
def arch_46_volume_scaling_effect_doubling_all_dimensions(r: random.Random) -> Dict[str, Any]:
    orig_v = r.choice([10, 15, 20, 25, 40])
    factor = 8  # 2^3
    new_v = orig_v * factor
    prompt = (
        f"A 3D prism has an original volume of ${orig_v}\\text{{ cm}}^3$. "
        f"If all linear dimensions (length, breadth, and height) are **doubled**, "
        f"calculate the new volume of the prism in cubic centimetres."
    )
    ans_str = str(new_v)
    sol = (
        f"When all linear dimensions are multiplied by scale factor $k = 2$, "
        f"the volume increases by a factor of $k^3 = 2^3 = 8$:\n"
        f"$$\\text{{New Volume}} = 2^3 \\times \\text{{Original Volume}} = 8 \\times {orig_v} = {new_v}\\text{{ cm}}^3$$"
    )
    return {
        "subskill": "46_volume_scaling_effect_doubling_all_dimensions",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": ans_str,
        "sample_answer": f"{ans_str} cm³ (factor of 8)",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "State scaling factor for volume is k³ = 2³ = 8", "marks": 1},
            {"step": f"Calculate: 8 × {orig_v} = {new_v}", "marks": 1},
        ],
        "hints": [
            "When linear dimensions are doubled ($k = 2$), volume is multiplied by $2^3 = 8$.",
            f"Multiply: $8 \\times {orig_v} = {new_v}\\text{{ cm}}^3$.",
        ],
        "misconception_tags": ["scaled_volume_by_2_or_4_instead_of_8"],
    }


# -----------------------------------------------------------------------------
# 47. Volume scaling effect: Tripling or factor k
# -----------------------------------------------------------------------------
def arch_47_volume_scaling_effect_tripling_or_factor_k(r: random.Random) -> Dict[str, Any]:
    k = r.choice([3, 4, 5])
    orig_v = r.choice([5, 8, 10, 12])
    k_cubed = k ** 3
    new_v = orig_v * k_cubed
    prompt = (
        f"A solid object has volume $V = {orig_v}\\text{{ cm}}^3$. "
        f"If all linear dimensions are enlarged by a factor of $k = {k}$, "
        f"calculate the enlarged volume in cubic centimetres."
    )
    ans_str = str(new_v)
    sol = (
        f"$$\\text{{Volume Scale Factor}} = k^3 = {k}^3 = {k_cubed}$$\n"
        f"$$\\text{{New Volume}} = {k_cubed} \\times {orig_v} = {new_v}\\text{{ cm}}^3$$"
    )
    return {
        "subskill": "47_volume_scaling_effect_tripling_or_factor_k",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": ans_str,
        "sample_answer": f"{ans_str} cm³",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Volume scale factor k³ = {k}³ = {k_cubed}", "marks": 1},
            {"step": f"Answer: {new_v}", "marks": 1},
        ],
        "hints": [
            f"Cube the scale factor: ${k}^3 = {k_cubed}$.",
            f"Multiply original volume by ${k_cubed}$: ${orig_v} \\times {k_cubed} = {new_v}\\text{{ cm}}^3$.",
        ],
        "misconception_tags": ["scaled_volume_by_k_squared_instead_of_cubed"],
    }


# -----------------------------------------------------------------------------
# 48. Volume of composite L-shaped prism
# -----------------------------------------------------------------------------
def arch_48_volume_of_composite_l_shaped_prism(r: random.Random) -> Dict[str, Any]:
    w1, h1 = 4, 8
    w2, h2 = 6, 3
    length = r.choice([10, 12, 15, 20])
    base_area = (w1 * h1) + (w2 * h2)  # 32 + 18 = 50
    vol = base_area * length
    seed_val = r.randint(100, 999999)
    svg = draw_dimensioned_rectangular_prism_svg(w1 + w2, length, h1, unit="cm", seed=seed_val)

    prompt = (
        f"An L-shaped concrete beam has a cross-sectional face composed of two joined rectangles: "
        f"one of $4\\text{{ cm}} \\times 8\\text{{ cm}}$ and another of $6\\text{{ cm}} \\times 3\\text{{ cm}}$. "
        f"The length of the beam is ${length}\\text{{ cm}}$. "
        f"Calculate the total volume of the beam."
    )
    ans_str = str(vol)
    sol = (
        f"1. **Cross-sectional Base Area**:\n"
        f"$$\\text{{Area}} = (4 \\times 8) + (6 \\times 3) = 32 + 18 = {base_area}\\text{{ cm}}^2$$\n\n"
        f"2. **Total Volume**:\n"
        f"$$\\text{{Volume}} = \\text{{Base Area}} \\times \\text{{Length}} = {base_area} \\times {length} = {vol}\\text{{ cm}}^3$$"
    )
    return {
        "subskill": "48_volume_of_composite_l_shaped_prism",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": ans_str,
        "sample_answer": f"{ans_str} cm³",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Cross-sectional area: 32 + 18 = {base_area}", "marks": 1},
            {"step": f"Volume: {base_area} × {length} = {vol}", "marks": 1},
        ],
        "hints": [
            f"Split the L-shaped face into two rectangles: $4 \\times 8 = 32$ and $6 \\times 3 = 18$.",
            f"Total base area: $32 + 18 = {base_area}\\text{{ cm}}^2$.",
            f"Multiply by length: ${base_area} \\times {length} = {vol}\\text{{ cm}}^3$.",
        ],
        "misconception_tags": ["l_shaped_cross_section_decomposition_error"],
    }


# -----------------------------------------------------------------------------
# 49. Volume of hollow cylindrical pipe
# -----------------------------------------------------------------------------
def arch_49_volume_of_hollow_cylindrical_pipe(r: random.Random) -> Dict[str, Any]:
    r_outer = 5
    r_inner = 3
    length = r.choice([20, 30, 40, 50])
    unit = "cm"
    # Annulus area = pi * (R^2 - r^2)
    # V = pi * (25 - 9) * length = 16 * pi * length
    diff_sq = r_outer ** 2 - r_inner ** 2  # 16
    vol = round(math.pi * diff_sq * length, 2)
    seed_val = r.randint(100, 999999)
    svg = draw_dimensioned_cylinder_svg(r_outer, length, unit=unit, is_open_top=True, seed=seed_val)

    prompt = (
        f"A hollow cylindrical metal pipe has outer radius $R = {r_outer}\\text{{ {unit}}}$, "
        f"inner radius $r = {r_inner}\\text{{ {unit}}}$, and length $L = {length}\\text{{ {unit}}}$. "
        f"Calculate the volume of metal in the pipe to two decimal places."
    )
    ans_str = f"{vol:.2f}".rstrip("0").rstrip(".")
    sol = (
        f"$$\\text{{Volume of metal}} = \\pi (R^2 - r^2) \\times L$$\n"
        f"$$V = \\pi ({r_outer}^2 - {r_inner}^2) \\times {length} = \\pi ({r_outer**2} - {r_inner**2}) \\times {length} = {diff_sq}\\pi \\times {length} = {diff_sq * length}\\pi \\approx {_fmt(vol, 2)}\\text{{ {unit}}}^3$$"
    )
    return {
        "subskill": "49_volume_of_hollow_cylindrical_pipe",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": ans_str,
        "sample_answer": f"{ans_str} {unit}³",
        "tolerance": 0.1,
        "marking_schema": [
            {"step": f"Area of annulus: π(R² - r²) = {diff_sq}π", "marks": 1},
            {"step": f"Volume: {diff_sq * length}π ≈ {ans_str}", "marks": 1},
        ],
        "hints": [
            "Subtract the inner cylinder volume from the outer cylinder volume.",
            f"Formula: $V = \\pi (R^2 - r^2) \\times L = \\pi ({r_outer**2} - {r_inner**2}) \\times {length}$.",
            f"The metal volume is approximately {_fmt(vol, 2)} {unit}³.",
        ],
        "misconception_tags": ["subtracted_radii_before_squaring"],
    }


# -----------------------------------------------------------------------------
# 50. Compound multi-stage 3D mensuration, costing, and capacity synthesis
# -----------------------------------------------------------------------------
def arch_50_compound_multi_stage_3d_mensuration_costing_and_capacity_synthesis(r: random.Random) -> Dict[str, Any]:
    l = 4  # m
    b = 3  # m
    h = 2  # m
    cost_per_m2 = 45  # R45 per m² of sealant
    water_litres_per_m3 = 1000

    vol_m3 = l * b * h  # 24 m³
    capacity_litres = vol_m3 * water_litres_per_m3  # 24 000 litres
    # Sealant for interior: floor + 4 walls = lb + 2lh + 2bh
    interior_sa = (l * b) + 2 * (l * h) + 2 * (b * h)  # 12 + 16 + 12 = 40 m²
    total_cost = interior_sa * cost_per_m2  # 40 * 45 = R1800

    seed_val = r.randint(100, 999999)
    svg = draw_dimensioned_rectangular_prism_svg(l, b, h, unit="m", seed=seed_val)

    prompt = (
        f"A concrete reservoir has internal dimensions: length $l = {l}\\text{{ m}}$, width $b = {b}\\text{{ m}}$, "
        f"and depth $h = {h}\\text{{ m}}$.\n"
        f"1. Calculate the full water capacity of the reservoir in litres.\n"
        f"2. The floor and 4 interior walls are treated with waterproof sealant at a cost of $\\text{{R}}{cost_per_m2}$ per square metre.\n\n"
        f"Calculate the **total cost (in Rand)** to apply the sealant."
    )
    ans_str = str(total_cost)
    sol = (
        f"1. **Capacity**:\n"
        f"$$V = l \\times b \\times h = {l} \\times {b} \\times {h} = {vol_m3}\\text{{ m}}^3$$\n"
        f"$$\\text{{Capacity}} = {vol_m3} \\times 1\\,000 = {capacity_litres}\\text{{ litres}}$$\n\n"
        f"2. **Interior Surface Area** (floor + 4 walls, no ceiling):\n"
        f"$$\\text{{SA}} = lb + 2lh + 2bh = ({l}\\times{b}) + 2({l}\\times{h}) + 2({b}\\times{h}) = {l*b} + {2*l*h} + {2*b*h} = {interior_sa}\\text{{ m}}^2$$\n\n"
        f"3. **Total Cost**:\n"
        f"$$\\text{{Cost}} = {interior_sa}\\text{{ m}}^2 \\times \\text{{R}}{cost_per_m2}/\\text{{m}}^2 = \\text{{R}}{total_cost}$$\n"
        f"The total cost is **R{total_cost}**."
    )
    return {
        "subskill": "50_compound_multi_stage_3d_mensuration_costing_and_capacity_synthesis",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": ans_str,
        "sample_answer": f"R{ans_str} ({interior_sa} m², {capacity_litres} L)",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Calculate capacity: {vol_m3} m³ = {capacity_litres} L", "marks": 1},
            {"step": f"Interior surface area (floor + 4 walls): {interior_sa} m²", "marks": 1},
            {"step": f"Total cost: {interior_sa} × R{cost_per_m2} = R{total_cost}", "marks": 1},
        ],
        "hints": [
            f"Volume in cubic metres: ${l} \\times {b} \\times {h} = {vol_m3}\\text{{ m}}^3$ ({capacity_litres} litres).",
            f"Interior area to seal (floor + 4 walls): ${interior_sa}\\text{{ m}}^2$.",
            f"Multiply by rate: ${interior_sa} \\times {cost_per_m2} = \\text{{R}}{total_cost}$.",
        ],
        "misconception_tags": ["compound_mensuration_costing_error"],
    }
