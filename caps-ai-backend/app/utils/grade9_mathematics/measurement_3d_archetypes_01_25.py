"""Grade 9 Mathematics - Measurement of 3D Objects Archetypes 01-25 (CAPS Term 4).
Focus: Surface Area of Prisms, Cylinders, Nets, Paint Coverage, Scaling, and Composites.
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
# 01. Surface area of cube (integer side)
# -----------------------------------------------------------------------------
def arch_01_surface_area_cube_integer_side(r: random.Random) -> Dict[str, Any]:
    s = r.choice([3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    unit = r.choice(["cm", "m", "mm"])
    sa = 6 * (s ** 2)
    seed_val = r.randint(100, 999999)
    svg = draw_dimensioned_cube_svg(s, unit=unit, seed=seed_val)

    prompt = (
        f"A cube has side lengths $s = {s}\\text{{ {unit}}}$. "
        f"Calculate the total surface area of the cube."
    )
    ans_str = str(sa)
    sol = (
        f"$$\\text{{Total Surface Area}} = 6 \\times s^2$$\n"
        f"$$\\text{{Total Surface Area}} = 6 \\times ({s})^2 = 6 \\times {s**2} = {sa}\\text{{ {unit}}}^2$$\n"
        f"The total surface area is **{sa} {unit}²**."
    )
    return {
        "subskill": "01_surface_area_cube_integer_side",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": ans_str,
        "sample_answer": f"{ans_str} {unit}²",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Formula: SA = 6s²", "marks": 1},
            {"step": f"Substitution: 6 × ({s})²", "marks": 1},
            {"step": f"Answer: {sa}", "marks": 1},
        ],
        "hints": [
            "A cube has 6 identical square faces.",
            f"Calculate the area of one face: ${s} \\times {s} = {s**2}\\text{{ {unit}}}^2$.",
            f"Multiply by 6: $6 \\times {s**2} = {sa}\\text{{ {unit}}}^2$.",
        ],
        "misconception_tags": ["cube_surface_area_omitted_faces"],
    }


# -----------------------------------------------------------------------------
# 02. Surface area of cube (decimal side)
# -----------------------------------------------------------------------------
def arch_02_surface_area_cube_decimal_side(r: random.Random) -> Dict[str, Any]:
    s = round(r.choice([1.5, 2.4, 3.5, 4.2, 5.5, 6.4, 7.5]), 1)
    unit = "cm"
    s_sq = round(s * s, 2)
    sa = round(6 * s_sq, 2)
    seed_val = r.randint(100, 999999)
    svg = draw_dimensioned_cube_svg(s, unit=unit, seed=seed_val)

    prompt = (
        f"A small packaging box in the shape of a cube has side length $s = {_fmt(s, 1)}\\text{{ cm}}$. "
        f"Calculate the total surface area of the box in square centimetres."
    )
    ans_str = f"{sa:.2f}".rstrip("0").rstrip(".")
    sol = (
        f"$$\\text{{Total Surface Area}} = 6s^2 = 6 \\times ({_fmt(s, 1)})^2 = 6 \\times {_fmt(s_sq, 2)} = {_fmt(sa, 2)}\\text{{ cm}}^2$$"
    )
    return {
        "subskill": "02_surface_area_cube_decimal_side",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": ans_str,
        "sample_answer": f"{ans_str} cm²",
        "tolerance": 0.05,
        "marking_schema": [
            {"step": "Formula: SA = 6s²", "marks": 1},
            {"step": f"Calculation: 6 × ({s})² = {sa}", "marks": 1},
        ],
        "hints": [
            "Formula for cube surface area: $SA = 6s^2$.",
            f"Square the side: $({_fmt(s, 1)})^2 = {_fmt(s_sq, 2)}$.",
            f"Multiply by 6 to obtain {_fmt(sa, 2)} cm².",
        ],
        "misconception_tags": ["decimal_squaring_error"],
    }


# -----------------------------------------------------------------------------
# 03. Find cube edge given total surface area
# -----------------------------------------------------------------------------
def arch_03_find_cube_edge_given_total_surface_area(r: random.Random) -> Dict[str, Any]:
    s = r.choice([2, 3, 4, 5, 6, 7, 8, 9, 10])
    sa = 6 * (s ** 2)
    seed_val = r.randint(100, 999999)
    svg = draw_dimensioned_cube_svg("s", unit="cm", seed=seed_val)

    prompt = (
        f"A cube has a total surface area of ${sa}\\text{{ cm}}^2$. "
        f"Calculate the length of one side ($s$) of the cube in centimetres."
    )
    ans_str = str(s)
    sol = (
        f"$$\\text{{Surface Area}} = 6s^2 = {sa}$$\n"
        f"$$s^2 = \\frac{{{sa}}}{{6}} = {s**2}$$\n"
        f"$$s = \\sqrt{{{s**2}}} = {s}\\text{{ cm}}$$"
    )
    return {
        "subskill": "03_find_cube_edge_given_total_surface_area",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": ans_str,
        "sample_answer": f"{ans_str} cm",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Divide total surface area by 6: {sa} / 6 = {s**2}", "marks": 1},
            {"step": f"Take square root: sqrt({s**2}) = {s}", "marks": 1},
        ],
        "hints": [
            "Divide the total surface area by 6 to find the area of one face.",
            f"Area of one face: ${sa} \\div 6 = {s**2}\\text{{ cm}}^2$.",
            f"Take the square root: $\\sqrt{{{s**2}}} = {s}\\text{{ cm}}$.",
        ],
        "misconception_tags": ["forgot_to_divide_by_six"],
    }


# -----------------------------------------------------------------------------
# 04. Surface area of rectangular prism (integer dimensions)
# -----------------------------------------------------------------------------
def arch_04_surface_area_rectangular_prism_integer_dims(r: random.Random) -> Dict[str, Any]:
    l = r.choice([5, 6, 7, 8, 9, 10, 12])
    b = r.choice([3, 4, 5, 6])
    h = r.choice([2, 3, 4, 5])
    unit = "cm"
    sa = 2 * (l * b + l * h + b * h)
    seed_val = r.randint(100, 999999)
    svg = draw_dimensioned_rectangular_prism_svg(l, b, h, unit=unit, seed=seed_val)

    prompt = (
        f"A rectangular prism has length $l = {l}\\text{{ {unit}}}$, breadth $b = {b}\\text{{ {unit}}}$, "
        f"and height $h = {h}\\text{{ {unit}}}$. Calculate its total surface area."
    )
    ans_str = str(sa)
    sol = (
        f"$$\\text{{Total Surface Area}} = 2(lb + lh + bh)$$\n"
        f"$$\\text{{SA}} = 2({l}\\times{b} + {l}\\times{h} + {b}\\times{h}) = 2({l*b} + {l*h} + {b*h}) = 2({l*b + l*h + b*h}) = {sa}\\text{{ {unit}}}^2$$"
    )
    return {
        "subskill": "04_surface_area_rectangular_prism_integer_dims",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": ans_str,
        "sample_answer": f"{ans_str} {unit}²",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Formula: SA = 2(lb + lh + bh)", "marks": 1},
            {"step": f"Substitution: 2({l*b} + {l*h} + {b*h})", "marks": 1},
            {"step": f"Answer: {sa}", "marks": 1},
        ],
        "hints": [
            "A rectangular prism has 3 pairs of opposite identical rectangular faces.",
            f"Calculate the 3 face areas: $lb = {l*b}$, $lh = {l*h}$, $bh = {b*h}$.",
            f"Add them and multiply by 2: $2({l*b + l*h + b*h}) = {sa}\\text{{ {unit}}}^2$.",
        ],
        "misconception_tags": ["forgot_to_multiply_by_two"],
    }


# -----------------------------------------------------------------------------
# 05. Surface area of rectangular prism (decimal dimensions)
# -----------------------------------------------------------------------------
def arch_05_surface_area_rectangular_prism_decimal_dims(r: random.Random) -> Dict[str, Any]:
    l = round(r.choice([4.5, 5.2, 6.5, 7.4]), 1)
    b = round(r.choice([2.5, 3.2, 4.0]), 1)
    h = round(r.choice([1.5, 2.0, 3.5]), 1)
    unit = "m"
    f1 = round(l * b, 2)
    f2 = round(l * h, 2)
    f3 = round(b * h, 2)
    sa = round(2 * (f1 + f2 + f3), 2)
    seed_val = r.randint(100, 999999)
    svg = draw_dimensioned_rectangular_prism_svg(l, b, h, unit=unit, seed=seed_val)

    prompt = (
        f"A shipping container has dimensions length $l = {_fmt(l, 1)}\\text{{ m}}$, "
        f"breadth $b = {_fmt(b, 1)}\\text{{ m}}$, and height $h = {_fmt(h, 1)}\\text{{ m}}$. "
        f"Calculate its total surface area in square metres."
    )
    ans_str = f"{sa:.2f}".rstrip("0").rstrip(".")
    sol = (
        f"$$\\text{{SA}} = 2(lb + lh + bh) = 2({_fmt(f1, 2)} + {_fmt(f2, 2)} + {_fmt(f3, 2)}) = 2({_fmt(f1+f2+f3, 2)}) = {_fmt(sa, 2)}\\text{{ m}}^2$$"
    )
    return {
        "subskill": "05_surface_area_rectangular_prism_decimal_dims",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": ans_str,
        "sample_answer": f"{ans_str} m²",
        "tolerance": 0.05,
        "marking_schema": [
            {"step": "Formula: SA = 2(lb + lh + bh)", "marks": 1},
            {"step": f"Face sum: {_fmt(f1+f2+f3, 2)}", "marks": 1},
            {"step": f"Total: {sa}", "marks": 1},
        ],
        "hints": [
            "Compute each face area: $l \\times b$, $l \\times h$, and $b \\times h$.",
            f"Sum of three faces: {_fmt(f1+f2+f3, 2)} m².",
            f"Multiply by 2: {_fmt(sa, 2)} m².",
        ],
        "misconception_tags": ["decimal_precision_error"],
    }


# -----------------------------------------------------------------------------
# 06. Surface area of rectangular box without lid (open top)
# -----------------------------------------------------------------------------
def arch_06_surface_area_rectangular_box_without_lid(r: random.Random) -> Dict[str, Any]:
    l = r.choice([6, 8, 10, 12, 14])
    b = r.choice([4, 5, 6, 8])
    h = r.choice([3, 4, 5, 6])
    unit = "cm"
    # Base (1 face) + 2 front/back + 2 left/right
    sa = (l * b) + 2 * (l * h) + 2 * (b * h)
    seed_val = r.randint(100, 999999)
    svg = draw_dimensioned_rectangular_prism_svg(l, b, h, unit=unit, seed=seed_val)

    prompt = (
        f"An open-top rectangular wooden tray has length $l = {l}\\text{{ {unit}}}$, "
        f"breadth $b = {b}\\text{{ {unit}}}$, and depth $h = {h}\\text{{ {unit}}}$. "
        f"Because it has no lid, only the base and 4 sides are constructed. "
        f"Calculate the exterior surface area of the open tray."
    )
    ans_str = str(sa)
    sol = (
        f"Since the box has **no lid (open top)**, it has only 5 faces:\n"
        f"$$\\text{{SA}} = lb + 2lh + 2bh$$\n"
        f"$$\\text{{SA}} = ({l} \\times {b}) + 2({l} \\times {h}) + 2({b} \\times {h}) = {l*b} + {2*l*h} + {2*b*h} = {sa}\\text{{ {unit}}}^2$$"
    )
    return {
        "subskill": "06_surface_area_rectangular_box_without_lid",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": ans_str,
        "sample_answer": f"{ans_str} {unit}²",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Recognize only 1 base face: lb", "marks": 1},
            {"step": f"Calculate 4 walls: 2lh + 2bh = {2*l*h + 2*b*h}", "marks": 1},
            {"step": f"Total surface area: {sa}", "marks": 1},
        ],
        "hints": [
            "Be careful: The box has no lid, so include only ONE base face ($lb$).",
            f"Base area: ${l} \\times {b} = {l*b}\\text{{ {unit}}}^2$.",
            f"Add the 4 vertical walls: ${l*b} + {2*l*h} + {2*b*h} = {sa}\\text{{ {unit}}}^2$.",
        ],
        "misconception_tags": ["included_missing_lid_in_open_box"],
    }


# -----------------------------------------------------------------------------
# 07. Find rectangular prism height given surface area, length, and breadth
# -----------------------------------------------------------------------------
def arch_07_find_rectangular_prism_height_given_surface_area(r: random.Random) -> Dict[str, Any]:
    l = r.choice([6, 8, 10])
    b = r.choice([4, 5])
    h = r.choice([3, 4, 5, 7])
    sa = 2 * (l * b + l * h + b * h)
    seed_val = r.randint(100, 999999)
    svg = draw_dimensioned_rectangular_prism_svg(l, b, "h", unit="cm", seed=seed_val)

    prompt = (
        f"A rectangular prism has a length of ${l}\\text{{ cm}}$, a breadth of ${b}\\text{{ cm}}$, "
        f"and a total surface area of ${sa}\\text{{ cm}}^2$. "
        f"Calculate the height ($h$) of the prism in centimetres."
    )
    ans_str = str(h)
    sol = (
        f"$$\\text{{SA}} = 2(lb + lh + bh) = {sa}$$\n"
        f"$$lb + lh + bh = \\frac{{{sa}}}{{2}} = {sa // 2}$$\n"
        f"$${l*b} + {l}h + {b}h = {sa // 2}$$\n"
        f"$${l+b}h = {sa // 2} - {l*b} = {sa // 2 - l*b}$$\n"
        f"$$h = \\frac{{{sa // 2 - l*b}}}{{{l+b}}} = {h}\\text{{ cm}}$$"
    )
    return {
        "subskill": "07_find_rectangular_prism_height_given_surface_area",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": ans_str,
        "sample_answer": f"{ans_str} cm",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Set up equation: 2({l*b} + {l+b}h) = {sa}", "marks": 1},
            {"step": f"Solve linear equation for h: h = {h}", "marks": 1},
        ],
        "hints": [
            f"Divide the total surface area by 2: ${sa} \\div 2 = {sa // 2}$.",
            f"Subtract the base area: ${sa // 2} - {l*b} = {sa // 2 - l*b}$.",
            f"Divide by $(l + b) = {l + b}$ to get $h = {h}\\text{{ cm}}$.",
        ],
        "misconception_tags": ["algebraic_rearrangement_error"],
    }


# -----------------------------------------------------------------------------
# 08. Surface area of right triangular prism (Pythagorean triple base)
# -----------------------------------------------------------------------------
def arch_08_surface_area_right_triangular_prism_pythagoras_needed(r: random.Random) -> Dict[str, Any]:
    triples = [(3, 4, 5), (6, 8, 10), (5, 12, 13)]
    a, b_leg, c_hyp = r.choice(triples)
    prism_l = r.choice([10, 12, 15, 20])
    unit = "cm"

    base_area = (a * b_leg) // 2
    lateral_area = (a + b_leg + c_hyp) * prism_l
    total_sa = 2 * base_area + lateral_area
    seed_val = r.randint(100, 999999)
    svg = draw_dimensioned_triangular_prism_svg(b_leg, a, prism_l, hypotenuse=c_hyp, unit=unit, seed=seed_val)

    prompt = (
        f"A right-angled triangular prism has perpendicular base legs of ${a}\\text{{ {unit}}}$ and ${b_leg}\\text{{ {unit}}}$, "
        f"and the length of the prism is ${prism_l}\\text{{ {unit}}}$. "
        f"Calculate the total surface area of the prism."
    )
    ans_str = str(total_sa)
    sol = (
        f"1. **Hypotenuse of base** ($c$):\n"
        f"$$c = \\sqrt{{{a}^2 + {b_leg}^2}} = \\sqrt{{{a**2} + {b_leg**2}}} = {c_hyp}\\text{{ {unit}}}$$\n\n"
        f"2. **Area of two triangular bases**:\n"
        f"$$2 \\times \\left(\\frac{{1}}{{2}} \\times {a} \\times {b_leg}\\right) = {a} \\times {b_leg} = {2 * base_area}\\text{{ {unit}}}^2$$\n\n"
        f"3. **Lateral surface area** (3 rectangular sides):\n"
        f"$$\\text{{Perimeter of base}} \\times \\text{{Length}} = ({a} + {b_leg} + {c_hyp}) \\times {prism_l} = {a + b_leg + c_hyp} \\times {prism_l} = {lateral_area}\\text{{ {unit}}}^2$$\n\n"
        f"4. **Total Surface Area**:\n"
        f"$$\\text{{Total SA}} = {2 * base_area} + {lateral_area} = {total_sa}\\text{{ {unit}}}^2$$"
    )
    return {
        "subskill": "08_surface_area_right_triangular_prism_pythagoras_needed",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": ans_str,
        "sample_answer": f"{ans_str} {unit}²",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Find hypotenuse via Pythagoras: {c_hyp}", "marks": 1},
            {"step": f"Area of 2 triangular bases: {2 * base_area}", "marks": 1},
            {"step": f"Lateral area: {lateral_area}", "marks": 1},
            {"step": f"Total surface area: {total_sa}", "marks": 1},
        ],
        "hints": [
            f"Use Pythagoras to find the slant side (hypotenuse): $\\sqrt{{{a}^2 + {b_leg}^2}} = {c_hyp}$.",
            f"Area of 2 bases: $2 \\times (\\frac{{1}}{{2}} \\times {a} \\times {b_leg}) = {2 * base_area}$.",
            f"Lateral area is perimeter times prism length: $({a} + {b_leg} + {c_hyp}) \\times {prism_l} = {lateral_area}$.",
        ],
        "misconception_tags": ["omitted_hypotenuse_face"],
    }


# -----------------------------------------------------------------------------
# 09. Surface area of equilateral triangular prism
# -----------------------------------------------------------------------------
def arch_09_surface_area_equilateral_triangular_prism(r: random.Random) -> Dict[str, Any]:
    s = r.choice([4, 6, 8, 10])
    l_prism = r.choice([10, 15, 20])
    # Equilateral triangle height = s * sqrt(3) / 2
    h_tri = round((s * math.sqrt(3)) / 2.0, 1)
    base_area_one = 0.5 * s * h_tri
    bases_area = 2.0 * base_area_one
    lateral_area = 3.0 * s * l_prism
    total_sa = round(bases_area + lateral_area, 1)
    seed_val = r.randint(100, 999999)
    svg = draw_dimensioned_triangular_prism_svg(s, h_tri, l_prism, unit="cm", seed=seed_val)

    prompt = (
        f"An equilateral triangular prism has base edge $s = {s}\\text{{ cm}}$, "
        f"perpendicular triangle height $h = {_fmt(h_tri, 1)}\\text{{ cm}}$, "
        f"and length $L = {l_prism}\\text{{ cm}}$. Calculate the total surface area to one decimal place."
    )
    ans_str = f"{total_sa:.1f}".rstrip("0").rstrip(".")
    sol = (
        f"1. **Bases Area** (2 equilateral triangles):\n"
        f"$$2 \\times \\left(\\frac{{1}}{{2}} \\times {s} \\times {_fmt(h_tri, 1)}\\right) = {_fmt(bases_area, 1)}\\text{{ cm}}^2$$\n\n"
        f"2. **Lateral Area** (3 identical rectangles):\n"
        f"$$3 \\times ({s} \\times {l_prism}) = 3 \\times {s * l_prism} = {int(lateral_area)}\\text{{ cm}}^2$$\n\n"
        f"3. **Total Surface Area**:\n"
        f"$$\\text{{Total SA}} = {_fmt(bases_area, 1)} + {int(lateral_area)} = {_fmt(total_sa, 1)}\\text{{ cm}}^2$$"
    )
    return {
        "subskill": "09_surface_area_equilateral_triangular_prism",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": ans_str,
        "sample_answer": f"{ans_str} cm²",
        "tolerance": 0.2,
        "marking_schema": [
            {"step": f"Area of 2 bases: {_fmt(bases_area, 1)}", "marks": 1},
            {"step": f"Lateral area: {int(lateral_area)}", "marks": 1},
            {"step": f"Total: {ans_str}", "marks": 1},
        ],
        "hints": [
            "All 3 lateral faces are identical rectangles of dimensions $s \\times L$.",
            f"Lateral area: $3 \\times ({s} \\times {l_prism}) = {int(lateral_area)}$.",
            f"Add the 2 triangular ends to obtain {_fmt(total_sa, 1)} cm².",
        ],
        "misconception_tags": ["triangular_prism_face_count_error"],
    }


# -----------------------------------------------------------------------------
# 10. Surface area of isosceles triangular prism
# -----------------------------------------------------------------------------
def arch_10_surface_area_isosceles_triangular_prism(r: random.Random) -> Dict[str, Any]:
    # base b, equal sides slant, height h_tri
    # b=6, slant=5, h=4 or b=8, slant=5, h=3
    b, slant, h_tri = r.choice([(6, 5, 4), (8, 5, 3), (10, 13, 12)])
    prism_l = r.choice([10, 14, 20])
    two_bases = b * h_tri
    lateral_area = (b + 2 * slant) * prism_l
    total_sa = two_bases + lateral_area
    seed_val = r.randint(100, 999999)
    svg = draw_dimensioned_triangular_prism_svg(b, h_tri, prism_l, unit="cm", seed=seed_val)

    prompt = (
        f"An isosceles triangular prism has a triangular base with base width $b = {b}\\text{{ cm}}$, "
        f"perpendicular height $h = {h_tri}\\text{{ cm}}$, equal slant sides of ${slant}\\text{{ cm}}$, "
        f"and length $L = {prism_l}\\text{{ cm}}$. Calculate the total surface area."
    )
    ans_str = str(total_sa)
    sol = (
        f"1. **Two triangular bases**:\n"
        f"$$2 \\times \\left(\\frac{{1}}{{2}} \\times {b} \\times {h_tri}\\right) = {b} \\times {h_tri} = {two_bases}\\text{{ cm}}^2$$\n\n"
        f"2. **Three rectangular lateral faces**:\n"
        f"$$\\text{{Perimeter of triangle}} \\times L = ({b} + {slant} + {slant}) \\times {prism_l} = {b + 2*slant} \\times {prism_l} = {lateral_area}\\text{{ cm}}^2$$\n\n"
        f"3. **Total Surface Area**:\n"
        f"$$\\text{{Total SA}} = {two_bases} + {lateral_area} = {total_sa}\\text{{ cm}}^2$$"
    )
    return {
        "subskill": "10_surface_area_isosceles_triangular_prism",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": ans_str,
        "sample_answer": f"{ans_str} cm²",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Area of 2 bases: {two_bases}", "marks": 1},
            {"step": f"Lateral area: {lateral_area}", "marks": 1},
            {"step": f"Total surface area: {total_sa}", "marks": 1},
        ],
        "hints": [
            f"The triangle has sides ${b}$, ${slant}$, and ${slant}$.",
            f"Perimeter of triangle: ${b} + {slant} + {slant} = {b + 2*slant}\\text{{ cm}}$.",
            f"Total SA = Base areas (${two_bases}$) + Lateral area (${lateral_area}$) = ${total_sa}\\text{{ cm}}^2$.",
        ],
        "misconception_tags": ["isosceles_lateral_face_inequality_confusion"],
    }


# -----------------------------------------------------------------------------
# 11. Surface area of closed cylinder (given radius and height)
# -----------------------------------------------------------------------------
def arch_11_surface_area_closed_cylinder_given_radius_and_height(r: random.Random) -> Dict[str, Any]:
    radius = r.choice([3, 4, 5, 7, 10, 14])
    h = r.choice([5, 8, 10, 12, 15, 20])
    unit = "cm"
    # SA = 2*pi*r^2 + 2*pi*r*h = 2*pi*r*(r + h)
    sa = 2 * math.pi * radius * (radius + h)
    sa_round = round(sa, 2)
    seed_val = r.randint(100, 999999)
    svg = draw_dimensioned_cylinder_svg(radius, h, unit=unit, is_open_top=False, seed=seed_val)

    prompt = (
        f"A closed right cylinder has radius $r = {radius}\\text{{ {unit}}}$ and height $h = {h}\\text{{ {unit}}}$. "
        f"Calculate the total surface area of the cylinder. "
        r"Use $\pi \approx 3{,}14159$ or your calculator $\pi$ key, and round your answer to two decimal places."
    )
    ans_str = f"{sa_round:.2f}".rstrip("0").rstrip(".")
    sol = (
        f"$$\\text{{Total Surface Area}} = 2\\pi r^2 + 2\\pi rh = 2\\pi r(r + h)$$\n"
        f"$$\\text{{SA}} = 2\\pi ({radius})({radius} + {h}) = 2\\pi ({radius})({radius + h}) = {2 * radius * (radius + h)}\\pi \\approx {_fmt(sa_round, 2)}\\text{{ {unit}}}^2$$"
    )
    return {
        "subskill": "11_surface_area_closed_cylinder_given_radius_and_height",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": ans_str,
        "sample_answer": f"{ans_str} {unit}²",
        "tolerance": 0.1,
        "marking_schema": [
            {"step": "Formula: SA = 2πr² + 2πrh", "marks": 1},
            {"step": f"Substitution: 2π({radius})² + 2π({radius})({h})", "marks": 1},
            {"step": f"Answer: {ans_str}", "marks": 1},
        ],
        "hints": [
            "Formula for closed cylinder: $SA = 2\\pi r^2 + 2\\pi rh$.",
            f"Two circular ends: $2 \\times \\pi \\times {radius}^2 = {2 * radius**2}\\pi$.",
            f"Curved surface: $2 \\times \\pi \\times {radius} \\times {h} = {2 * radius * h}\\pi$.",
        ],
        "misconception_tags": ["cylinder_omitted_one_circular_lid"],
    }


# -----------------------------------------------------------------------------
# 12. Surface area of closed cylinder (given diameter and height)
# -----------------------------------------------------------------------------
def arch_12_surface_area_closed_cylinder_given_diameter_and_height(r: random.Random) -> Dict[str, Any]:
    diam = r.choice([6, 8, 10, 14, 20])
    radius = diam / 2.0
    h = r.choice([7, 10, 12, 15])
    unit = "cm"
    sa = 2 * math.pi * radius * (radius + h)
    sa_round = round(sa, 2)
    seed_val = r.randint(100, 999999)
    svg = draw_dimensioned_cylinder_svg(int(radius), h, unit=unit, is_open_top=False, seed=seed_val)

    prompt = (
        f"A tin can has a diameter of $d = {diam}\\text{{ {unit}}}$ and a height of $h = {h}\\text{{ {unit}}}$. "
        f"Calculate the total surface area of the closed tin can to two decimal places."
    )
    ans_str = f"{sa_round:.2f}".rstrip("0").rstrip(".")
    sol = (
        f"1. **Radius**: $r = \\frac{{d}}{{2}} = \\frac{{{diam}}}{{2}} = {int(radius)}\\text{{ {unit}}}$.\n\n"
        f"2. **Total Surface Area**:\n"
        f"$$\\text{{SA}} = 2\\pi r^2 + 2\\pi rh = 2\\pi ({int(radius)})^2 + 2\\pi ({int(radius)})({h}) \\approx {_fmt(sa_round, 2)}\\text{{ {unit}}}^2$$"
    )
    return {
        "subskill": "12_surface_area_closed_cylinder_given_diameter_and_height",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": ans_str,
        "sample_answer": f"{ans_str} {unit}²",
        "tolerance": 0.1,
        "marking_schema": [
            {"step": f"Halve diameter to find radius: r = {int(radius)}", "marks": 1},
            {"step": "Formula: SA = 2πr² + 2πrh", "marks": 1},
            {"step": f"Answer: {ans_str}", "marks": 1},
        ],
        "hints": [
            f"Always halve the diameter first: $r = {diam} \\div 2 = {int(radius)}\\text{{ {unit}}}$.",
            "Use the formula $SA = 2\\pi r^2 + 2\\pi rh$.",
            f"Total surface area is approximately {_fmt(sa_round, 2)} {unit}².",
        ],
        "misconception_tags": ["used_diameter_instead_of_radius"],
    }


# -----------------------------------------------------------------------------
# 13. Surface area of cylinder open at one end
# -----------------------------------------------------------------------------
def arch_13_surface_area_cylinder_open_at_one_end(r: random.Random) -> Dict[str, Any]:
    radius = r.choice([3, 4, 5, 7, 10])
    h = r.choice([6, 8, 10, 14])
    unit = "cm"
    # SA = pi*r^2 + 2*pi*r*h = pi*r*(r + 2h)
    sa = math.pi * radius * (radius + 2 * h)
    sa_round = round(sa, 2)
    seed_val = r.randint(100, 999999)
    svg = draw_dimensioned_cylinder_svg(radius, h, unit=unit, is_open_top=True, seed=seed_val)

    prompt = (
        f"A cylindrical rubbish bin is open at the top. The circular base has radius $r = {radius}\\text{{ {unit}}}$ "
        f"and the height is $h = {h}\\text{{ {unit}}}$. "
        f"Calculate the exterior surface area of the bin (base plus curved side) to two decimal places."
    )
    ans_str = f"{sa_round:.2f}".rstrip("0").rstrip(".")
    sol = (
        f"Since the cylinder is **open at one end**, it has only **one circular base** and one curved surface:\n"
        f"$$\\text{{SA}} = \\pi r^2 + 2\\pi rh = \\pi ({radius})^2 + 2\\pi ({radius})({h}) = {radius**2}\\pi + {2*radius*h}\\pi = {radius**2 + 2*radius*h}\\pi \\approx {_fmt(sa_round, 2)}\\text{{ {unit}}}^2$$"
    )
    return {
        "subskill": "13_surface_area_cylinder_open_at_one_end",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": ans_str,
        "sample_answer": f"{ans_str} {unit}²",
        "tolerance": 0.1,
        "marking_schema": [
            {"step": "Formula: SA = πr² + 2πrh (only 1 circular base)", "marks": 1},
            {"step": f"Substitution: π({radius})² + 2π({radius})({h})", "marks": 1},
            {"step": f"Answer: {ans_str}", "marks": 1},
        ],
        "hints": [
            "Because the cylinder is open at the top, only include ONE circle: $\\pi r^2$.",
            f"Base area: $\\pi \\times {radius}^2 = {radius**2}\\pi$.",
            f"Curved area: $2\\pi \\times {radius} \\times {h} = {2*radius*h}\\pi$.",
        ],
        "misconception_tags": ["included_two_bases_for_open_cylinder"],
    }


# -----------------------------------------------------------------------------
# 14. Curved lateral surface area of cylinder pipe
# -----------------------------------------------------------------------------
def arch_14_curved_lateral_surface_area_of_cylinder_pipe(r: random.Random) -> Dict[str, Any]:
    radius = r.choice([5, 7, 10, 14])
    length = r.choice([20, 30, 40, 50])
    unit = "cm"
    curved_sa = 2 * math.pi * radius * length
    sa_round = round(curved_sa, 2)
    seed_val = r.randint(100, 999999)
    svg = draw_dimensioned_cylinder_svg(radius, length, unit=unit, is_open_top=True, seed=seed_val)

    prompt = (
        f"A hollow cylindrical drainage pipe has radius $r = {radius}\\text{{ {unit}}}$ "
        f"and length $L = {length}\\text{{ {unit}}}$. Both ends are open. "
        f"Calculate the curved lateral surface area of the pipe to two decimal places."
    )
    ans_str = f"{sa_round:.2f}".rstrip("0").rstrip(".")
    sol = (
        f"For a hollow open pipe (both ends open), the surface area consists **only of the curved surface**:\n"
        f"$$\\text{{Curved SA}} = 2\\pi rh = 2\\pi ({radius})({length}) = {2 * radius * length}\\pi \\approx {_fmt(sa_round, 2)}\\text{{ {unit}}}^2$$"
    )
    return {
        "subskill": "14_curved_lateral_surface_area_of_cylinder_pipe",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": ans_str,
        "sample_answer": f"{ans_str} {unit}²",
        "tolerance": 0.1,
        "marking_schema": [
            {"step": "Formula: Curved SA = 2πrh (no circular ends)", "marks": 1},
            {"step": f"Answer: {ans_str}", "marks": 1},
        ],
        "hints": [
            "A hollow pipe has both ends open, so circular base area is 0.",
            "Use only the curved rectangle formula: $\\text{Area} = 2\\pi r h$.",
            f"Calculate $2 \\times \\pi \\times {radius} \\times {length} \\approx {_fmt(sa_round, 2)}$.",
        ],
        "misconception_tags": ["included_circle_ends_in_pipe"],
    }


# -----------------------------------------------------------------------------
# 15. Find cylinder height given curved surface area
# -----------------------------------------------------------------------------
def arch_15_find_cylinder_height_given_curved_surface_area(r: random.Random) -> Dict[str, Any]:
    radius = r.choice([3, 4, 5, 7])
    h = r.choice([6, 8, 10, 12, 15])
    curved_sa = round(2 * math.pi * radius * h, 1)
    seed_val = r.randint(100, 999999)
    svg = draw_dimensioned_cylinder_svg(radius, "h", unit="cm", is_open_top=False, seed=seed_val)

    prompt = (
        f"The curved lateral surface area of a cylinder is ${_fmt(curved_sa, 1)}\\text{{ cm}}^2$, "
        f"and the radius is $r = {radius}\\text{{ cm}}$. "
        f"Calculate the height ($h$) of the cylinder to the nearest whole centimetre."
    )
    ans_str = str(h)
    sol = (
        f"$$\\text{{Curved SA}} = 2\\pi rh = {_fmt(curved_sa, 1)}$$\n"
        f"$$h = \\frac{{\\text{{Curved SA}}}}{{2\\pi r}} = \\frac{{{_fmt(curved_sa, 1)}}}{{2\\pi \\times {radius}}} = \\frac{{{_fmt(curved_sa, 1)}}}{{{2*radius}\\pi}} \\approx {h}\\text{{ cm}}$$"
    )
    return {
        "subskill": "15_find_cylinder_height_given_curved_surface_area",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": ans_str,
        "sample_answer": f"{ans_str} cm",
        "tolerance": 0.5,
        "marking_schema": [
            {"step": f"Rearrange formula: h = Curved SA / (2πr)", "marks": 1},
            {"step": f"Calculate height: {h} cm", "marks": 1},
        ],
        "hints": [
            "Formula: $\\text{Curved SA} = 2\\pi r h$.",
            f"Circumference of base: $2\\pi r = 2 \\times \\pi \\times {radius} \\approx {_fmt(2*math.pi*radius, 2)}$.",
            f"Divide curved area by circumference: ${curved_sa} \\div {_fmt(2*math.pi*radius, 2)} \\approx {h}$.",
        ],
        "misconception_tags": ["cylinder_inverse_formula_error"],
    }


# -----------------------------------------------------------------------------
# 16. Find cylinder radius given curved surface area
# -----------------------------------------------------------------------------
def arch_16_find_cylinder_radius_given_curved_surface_area(r: random.Random) -> Dict[str, Any]:
    radius = r.choice([3, 5, 7, 8, 10])
    h = r.choice([10, 12, 14, 20])
    curved_sa = round(2 * math.pi * radius * h, 1)
    seed_val = r.randint(100, 999999)
    svg = draw_dimensioned_cylinder_svg("r", h, unit="cm", is_open_top=False, seed=seed_val)

    prompt = (
        f"A cylinder has height $h = {h}\\text{{ cm}}$ and a curved surface area of ${_fmt(curved_sa, 1)}\\text{{ cm}}^2$. "
        f"Calculate the radius ($r$) of the cylinder to the nearest whole centimetre."
    )
    ans_str = str(radius)
    sol = (
        f"$$\\text{{Curved SA}} = 2\\pi rh = {_fmt(curved_sa, 1)}$$\n"
        f"$$r = \\frac{{\\text{{Curved SA}}}}{{2\\pi h}} = \\frac{{{_fmt(curved_sa, 1)}}}{{2\\pi \\times {h}}} = \\frac{{{_fmt(curved_sa, 1)}}}{{{2*h}\\pi}} \\approx {radius}\\text{{ cm}}$$"
    )
    return {
        "subskill": "16_find_cylinder_radius_given_curved_surface_area",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": ans_str,
        "sample_answer": f"{ans_str} cm",
        "tolerance": 0.5,
        "marking_schema": [
            {"step": "Formula: r = Curved SA / (2πh)", "marks": 1},
            {"step": f"Answer: {radius} cm", "marks": 1},
        ],
        "hints": [
            "Formula: $\\text{Curved SA} = 2\\pi r h$.",
            f"Divide curved area by $2\\pi h = 2 \\times \\pi \\times {h}$.",
            f"The radius is {radius} cm.",
        ],
        "misconception_tags": ["cylinder_radius_isolation_error"],
    }


# -----------------------------------------------------------------------------
# 17. Paint coverage calculation for rectangular room or box
# -----------------------------------------------------------------------------
def arch_17_paint_coverage_calculation_for_rectangular_room_or_box(r: random.Random) -> Dict[str, Any]:
    l = r.choice([5, 6, 8])
    b = r.choice([4, 5])
    h = 3
    coverage_per_litre = r.choice([8, 10])  # m² per litre
    # 4 walls: 2lh + 2bh
    wall_area = 2 * (l * h) + 2 * (b * h)
    litres_needed = math.ceil(wall_area / coverage_per_litre)
    seed_val = r.randint(100, 999999)
    svg = draw_dimensioned_rectangular_prism_svg(l, b, h, unit="m", seed=seed_val)

    prompt = (
        f"A room has length $l = {l}\\text{{ m}}$, width $b = {b}\\text{{ m}}$, and wall height $h = {h}\\text{{ m}}$. "
        f"All 4 interior walls are to be painted (the floor and ceiling are not painted). "
        f"If 1 litre of paint covers ${coverage_per_litre}\\text{{ m}}^2$, "
        f"calculate the minimum whole number of 1-litre paint tins required."
    )
    ans_str = str(litres_needed)
    sol = (
        f"1. **Area of 4 walls**:\n"
        f"$$\\text{{Wall Area}} = 2lh + 2bh = 2({l}\\times{h}) + 2({b}\\times{h}) = {2*l*h} + {2*b*h} = {wall_area}\\text{{ m}}^2$$\n\n"
        f"2. **Litres of paint**:\n"
        f"$$\\text{{Litres}} = \\frac{{{wall_area}}}{{{coverage_per_litre}}} = {wall_area / coverage_per_litre:.2f}$$\n\n"
        f"Rounding up to the nearest whole tin gives **{litres_needed} tins**."
    )
    return {
        "subskill": "17_paint_coverage_calculation_for_rectangular_room_or_box",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": ans_str,
        "sample_answer": f"{ans_str} tins ({wall_area} m²)",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Area of 4 walls: 2lh + 2bh = {wall_area} m²", "marks": 1},
            {"step": f"Divide by coverage: {wall_area} / {coverage_per_litre}", "marks": 1},
            {"step": f"Round up to whole tins: {litres_needed}", "marks": 1},
        ],
        "hints": [
            "Calculate only the 4 vertical walls: $2lh + 2bh$ (exclude floor and ceiling).",
            f"Wall area: ${2*l*h} + ${2*b*h} = {wall_area}\\text{{ m}}^2$.",
            f"Divide by ${coverage_per_litre}$ and round UP to the nearest whole tin.",
        ],
        "misconception_tags": ["included_ceiling_or_floor_in_wall_paint"],
    }


# -----------------------------------------------------------------------------
# 18. Paint coverage calculation for cylindrical water tank
# -----------------------------------------------------------------------------
def arch_18_paint_coverage_calculation_for_cylindrical_water_tank(r: random.Random) -> Dict[str, Any]:
    radius = r.choice([2, 3])
    h = r.choice([3, 4, 5])
    coverage = 10  # m² per litre
    # Exterior curved wall + circular lid (closed tank top)
    sa = math.pi * radius * radius + 2 * math.pi * radius * h
    litres = round(sa / coverage, 2)
    seed_val = r.randint(100, 999999)
    svg = draw_dimensioned_cylinder_svg(radius, h, unit="m", is_open_top=False, seed=seed_val)

    prompt = (
        f"An outdoor cylindrical water tank with radius $r = {radius}\\text{{ m}}$ and height $h = {h}\\text{{ m}}$ "
        f"is to be painted with waterproof sealant on its exterior curved surface and top roof lid (the tank rests on the ground). "
        f"Calculate the exterior surface area to be painted to two decimal places."
    )
    ans_str = f"{sa:.2f}".rstrip("0").rstrip(".")
    sol = (
        f"$$\\text{{Area}} = \\pi r^2 + 2\\pi rh = \\pi ({radius})^2 + 2\\pi ({radius})({h}) = {radius**2}\\pi + {2*radius*h}\\pi = {radius**2 + 2*radius*h}\\pi \\approx {_fmt(sa, 2)}\\text{{ m}}^2$$"
    )
    return {
        "subskill": "18_paint_coverage_calculation_for_cylindrical_water_tank",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": ans_str,
        "sample_answer": f"{ans_str} m²",
        "tolerance": 0.1,
        "marking_schema": [
            {"step": "Formula: SA = πr² + 2πrh (exclude ground contact base)", "marks": 1},
            {"step": f"Answer: {ans_str}", "marks": 1},
        ],
        "hints": [
            "The tank rests on the ground, so only paint 1 circular top lid plus the curved side.",
            f"Top lid: $\\pi \\times {radius}^2 = {radius**2}\\pi$.",
            f"Curved side: $2\\pi \\times {radius} \\times {h} = {2*radius*h}\\pi$.",
        ],
        "misconception_tags": ["painted_underside_of_tank"],
    }


# -----------------------------------------------------------------------------
# 19. Surface area scaling effect: Doubling all dimensions
# -----------------------------------------------------------------------------
def arch_19_surface_area_scaling_effect_doubling_all_dimensions(r: random.Random) -> Dict[str, Any]:
    s = r.choice([3, 4, 5, 6])
    original_sa = 6 * (s ** 2)
    new_s = 2 * s
    new_sa = 6 * (new_s ** 2)
    factor = 4  # 2^2
    seed_val = r.randint(100, 999999)
    svg = draw_dimensioned_cube_svg(s, unit="cm", seed=seed_val)

    prompt = (
        f"A cube with side length $s = {s}\\text{{ cm}}$ has surface area ${original_sa}\\text{{ cm}}^2$. "
        f"If all of its dimensions are **doubled** ($s' = {new_s}\\text{{ cm}}$), "
        f"by what factor does the total surface area increase?"
    )
    ans_str = "4"
    sol = (
        f"Original Surface Area: $SA_1 = 6s^2 = 6({s})^2 = {original_sa}\\text{{ cm}}^2$.\n"
        f"New Surface Area: $SA_2 = 6(2s)^2 = 6(4s^2) = 4 \\times (6s^2) = 4 \\times {original_sa} = {new_sa}\\text{{ cm}}^2$.\n"
        f"The surface area increases by a factor of $2^2 = **4**$."
    )
    return {
        "subskill": "19_surface_area_scaling_effect_doubling_all_dimensions",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": ans_str,
        "sample_answer": "4 (k² = 2² = 4)",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "State scaling factor for area is k²", "marks": 1},
            {"step": "Calculate 2² = 4", "marks": 1},
        ],
        "hints": [
            "When linear dimensions are multiplied by a scale factor $k$, area increases by $k^2$.",
            "Here, $k = 2$, so area increases by $2^2 = 4$.",
            "The answer is 4.",
        ],
        "misconception_tags": ["assumed_surface_area_doubles_when_dimensions_double"],
    }


# -----------------------------------------------------------------------------
# 20. Surface area scaling effect: Factor k
# -----------------------------------------------------------------------------
def arch_20_surface_area_scaling_effect_factor_k(r: random.Random) -> Dict[str, Any]:
    k = r.choice([3, 4, 5])
    orig_sa = r.choice([20, 30, 50, 60, 100])
    new_sa = orig_sa * (k ** 2)
    seed_val = r.randint(100, 999999)
    svg = draw_dimensioned_rectangular_prism_svg(4, 3, 2, unit="cm", seed=seed_val)

    prompt = (
        f"A 3D object has an initial total surface area of ${orig_sa}\\text{{ cm}}^2$. "
        f"If all linear dimensions of the object are enlarged by a factor of $k = {k}$, "
        f"calculate the new total surface area in square centimetres."
    )
    ans_str = str(new_sa)
    sol = (
        f"When all linear dimensions of a 3D object are multiplied by $k$, "
        f"its surface area is multiplied by $k^2$:\n"
        f"$$\\text{{New SA}} = k^2 \\times \\text{{Original SA}} = ({k})^2 \\times {orig_sa} = {k**2} \\times {orig_sa} = {new_sa}\\text{{ cm}}^2$$"
    )
    return {
        "subskill": "20_surface_area_scaling_effect_factor_k",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": ans_str,
        "sample_answer": f"{ans_str} cm²",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Scale factor for area: k² = {k}² = {k**2}", "marks": 1},
            {"step": f"Multiply: {k**2} × {orig_sa} = {new_sa}", "marks": 1},
        ],
        "hints": [
            f"Square the scale factor: $k^2 = {k}^2 = {k**2}$.",
            f"Multiply the original area by ${k**2}$: ${orig_sa} \\times {k**2} = {new_sa}$.",
            f"The new surface area is {new_sa} cm².",
        ],
        "misconception_tags": ["scaled_surface_area_by_k_instead_of_k_squared"],
    }


# -----------------------------------------------------------------------------
# 21. Surface area of T-net unfolded cube
# -----------------------------------------------------------------------------
def arch_21_surface_area_of_t_net_unfolded_cube(r: random.Random) -> Dict[str, Any]:
    s = r.choice([3, 4, 5, 7, 9])
    total_sa = 6 * (s ** 2)
    seed_val = r.randint(100, 999999)
    svg = draw_dimensioned_cube_svg(s, unit="cm", seed=seed_val)

    prompt = (
        f"An unfolded net of a cube consists of 6 congruent squares, each with side $s = {s}\\text{{ cm}}$. "
        f"Calculate the total area of the net."
    )
    ans_str = str(total_sa)
    sol = (
        f"The net comprises 6 congruent squares:\n"
        f"$$\\text{{Area}} = 6 \\times (s \\times s) = 6 \\times ({s})^2 = 6 \\times {s**2} = {total_sa}\\text{{ cm}}^2$$"
    )
    return {
        "subskill": "21_surface_area_of_t_net_unfolded_cube",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": ans_str,
        "sample_answer": f"{ans_str} cm²",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Area of 1 square: {s**2}", "marks": 1},
            {"step": f"Total area of 6 squares: {total_sa}", "marks": 1},
        ],
        "hints": [
            f"Find the area of one square face: ${s} \\times {s} = {s**2}\\text{{ cm}}^2$.",
            f"Multiply by 6 to find the total net area: $6 \\times {s**2} = {total_sa}\\text{{ cm}}^2$.",
        ],
        "misconception_tags": ["net_face_count_error"],
    }


# -----------------------------------------------------------------------------
# 22. Surface area of triangular prism net
# -----------------------------------------------------------------------------
def arch_22_surface_area_of_triangular_prism_net(r: random.Random) -> Dict[str, Any]:
    b = 6
    h_tri = 4
    slant = 5
    prism_l = r.choice([8, 10, 12, 15])
    two_tri = b * h_tri  # 2 * 0.5 * 6 * 4 = 24
    rec1 = b * prism_l
    rec2 = slant * prism_l
    rec3 = slant * prism_l
    total_sa = two_tri + rec1 + rec2 + rec3
    seed_val = r.randint(100, 999999)
    svg = draw_dimensioned_triangular_prism_svg(b, h_tri, prism_l, unit="cm", seed=seed_val)

    prompt = (
        f"A net of an isosceles triangular prism unfolds into 2 triangular flaps (base $6\\text{{ cm}}$, height $4\\text{{ cm}}$) "
        f"and 3 rectangular faces of length ${prism_l}\\text{{ cm}}$ (one of width $6\\text{{ cm}}$ and two of width $5\\text{{ cm}}$). "
        f"Calculate the total surface area represented by the unfolded net."
    )
    ans_str = str(total_sa)
    sol = (
        f"1. **2 Triangular Flaps**: $2 \\times \\left(\\frac{{1}}{{2}} \\times 6 \\times 4\\right) = 24\\text{{ cm}}^2$.\n"
        f"2. **3 Rectangles**: $(6 + 5 + 5) \\times {prism_l} = 16 \\times {prism_l} = {16 * prism_l}\\text{{ cm}}^2$.\n"
        f"3. **Total Area**: $24 + {16 * prism_l} = {total_sa}\\text{{ cm}}^2$."
    )
    return {
        "subskill": "22_surface_area_of_triangular_prism_net",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": ans_str,
        "sample_answer": f"{ans_str} cm²",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Area of 2 triangles: 24", "marks": 1},
            {"step": f"Area of 3 rectangles: {16 * prism_l}", "marks": 1},
            {"step": f"Total area: {total_sa}", "marks": 1},
        ],
        "hints": [
            "Sum the area of all 5 parts of the net: 2 triangles and 3 rectangles.",
            f"Triangles: 24 cm². Rectangles: $(6 + 5 + 5) \\times {prism_l} = {16 * prism_l}\\text{{ cm}}^2$.",
            f"Total = ${24} + {16 * prism_l} = {total_sa}\\text{{ cm}}^2$.",
        ],
        "misconception_tags": ["triangular_net_missing_rectangles"],
    }


# -----------------------------------------------------------------------------
# 23. Surface area of cylinder net (rectangle plus two circles)
# -----------------------------------------------------------------------------
def arch_23_surface_area_of_cylinder_net_rectangle_plus_two_circles(r: random.Random) -> Dict[str, Any]:
    radius = r.choice([3, 7, 10])
    h = r.choice([10, 14, 20])
    unit = "cm"
    two_circles = 2 * math.pi * radius * radius
    rectangle_area = 2 * math.pi * radius * h
    total_sa = two_circles + rectangle_area
    seed_val = r.randint(100, 999999)
    svg = draw_dimensioned_cylinder_svg(radius, h, unit=unit, is_open_top=False, seed=seed_val)

    prompt = (
        f"The unfolded net of a closed cylinder consists of 2 circular lids of radius $r = {radius}\\text{{ {unit}}}$ "
        f"and 1 rectangular body sheet of height $h = {h}\\text{{ {unit}}}$. "
        f"Calculate the total area of the net to two decimal places."
    )
    ans_str = f"{total_sa:.2f}".rstrip("0").rstrip(".")
    sol = (
        f"1. **Length of rectangular sheet** = Circumference of circle = $2\\pi r = 2\\pi({radius}) = {2*radius}\\pi$.\n"
        f"2. **Area of rectangular sheet** = $2\\pi rh = {2*radius}\\pi \\times {h} = {2*radius*h}\\pi$.\n"
        f"3. **Area of two circular lids** = $2 \\times \\pi r^2 = 2\\pi ({radius}^2) = {2*radius**2}\\pi$.\n"
        f"4. **Total Area** = ${2*radius*h}\\pi + {2*radius**2}\\pi = {2*radius*(radius+h)}\\pi \\approx {_fmt(total_sa, 2)}\\text{{ {unit}}}^2$."
    )
    return {
        "subskill": "23_surface_area_of_cylinder_net_rectangle_plus_two_circles",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": ans_str,
        "sample_answer": f"{ans_str} {unit}²",
        "tolerance": 0.1,
        "marking_schema": [
            {"step": "Rectangle length = 2πr", "marks": 1},
            {"step": "Rectangle area = 2πrh", "marks": 1},
            {"step": "2 Circles area = 2πr²", "marks": 1},
            {"step": f"Total area: {ans_str}", "marks": 1},
        ],
        "hints": [
            "The length of the rectangle is the circumference of the circle: $2\\pi r$.",
            f"Rectangle area: $2\\pi \\times {radius} \\times {h} = {2*radius*h}\\pi$.",
            f"Add the 2 circular ends: $2\\pi \\times {radius}^2 = {2*radius**2}\\pi$.",
        ],
        "misconception_tags": ["cylinder_net_rectangle_width_error"],
    }


# -----------------------------------------------------------------------------
# 24. Surface area of composite solid: Cube with smaller cube on top
# -----------------------------------------------------------------------------
def arch_24_surface_area_composite_cube_with_smaller_cube_on_top(r: random.Random) -> Dict[str, Any]:
    s1 = r.choice([6, 8, 10])  # large cube
    s2 = r.choice([2, 3, 4])   # small cube on top
    # Large cube full surface area = 6 * s1^2
    # Small cube adds 4 vertical faces (its top face replaces the covered patch on the large cube)
    # Total SA = 6*s1^2 + 4*s2^2
    total_sa = 6 * (s1 ** 2) + 4 * (s2 ** 2)
    seed_val = r.randint(100, 999999)
    svg = draw_dimensioned_cube_svg(s1, unit="cm", seed=seed_val)

    prompt = (
        f"A composite solid is formed by gluing a small cube of side length $s_2 = {s2}\\text{{ cm}}$ "
        f"onto the top face of a larger cube of side length $s_1 = {s1}\\text{{ cm}}$. "
        f"Calculate the total exterior surface area of the composite solid."
    )
    ans_str = str(total_sa)
    sol = (
        f"Notice the contact patch:\n"
        f"• The top face of the small cube adds $s_2^2$ to the exterior, exactly replacing the hidden patch of $s_2^2$ covered on the large cube.\n"
        f"• Therefore, the full exterior of the large cube is accounted for: $6 \\times s_1^2 = 6 \\times ({s1})^2 = {6 * s1**2}\\text{{ cm}}^2$.\n"
        f"• The small cube adds its 4 vertical side faces: $4 \\times s_2^2 = 4 \\times ({s2})^2 = {4 * s2**2}\\text{{ cm}}^2$.\n"
        f"$$\\text{{Total SA}} = 6s_1^2 + 4s_2^2 = {6 * s1**2} + {4 * s2**2} = {total_sa}\\text{{ cm}}^2$$"
    )
    return {
        "subskill": "24_surface_area_composite_cube_with_smaller_cube_on_top",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": ans_str,
        "sample_answer": f"{ans_str} cm²",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Exterior of large cube (including replaced top patch): 6 × {s1}² = {6*s1**2}", "marks": 1},
            {"step": f"4 vertical faces of small cube: 4 × {s2}² = {4*s2**2}", "marks": 1},
            {"step": f"Total: {total_sa}", "marks": 1},
        ],
        "hints": [
            "The top face of the small cube replaces the covered area on the large cube.",
            f"So the large cube contributes all 6 faces: $6 \\times {s1}^2 = {6*s1**2}\\text{{ cm}}^2$.",
            f"Add the 4 exposed vertical sides of the small cube: $4 \\times {s2}^2 = {4*s2**2}\\text{{ cm}}^2$.",
        ],
        "misconception_tags": ["added_internal_glued_faces_in_composite"],
    }


# -----------------------------------------------------------------------------
# 25. Surface area of composite: Rectangular prism and triangular roof
# -----------------------------------------------------------------------------
def arch_25_surface_area_composite_rectangular_prism_and_triangular_roof(r: random.Random) -> Dict[str, Any]:
    l = 10
    w = 6
    h_box = 4
    # Triangular roof with base 6, height 4, slant side 5, length 10
    slant = 5
    h_roof = 4

    # Bottom box: base (l*w) + 2 front/back (2*l*h_box) + 2 left/right (2*w*h_box). Top is covered.
    box_exposed = (l * w) + 2 * (l * h_box) + 2 * (w * h_box)
    # Roof: 2 triangular ends (2 * 0.5 * 6 * 4 = 24) + 2 slanted rectangular slopes (2 * slant * l = 2 * 5 * 10 = 100)
    roof_exposed = (w * h_roof) + 2 * (slant * l)
    total_sa = box_exposed + roof_exposed
    seed_val = r.randint(100, 999999)
    svg = draw_dimensioned_rectangular_prism_svg(l, w, h_box, unit="m", seed=seed_val)

    prompt = (
        f"A small storage shed is modeled as a rectangular prism (length $10\\text{{ m}}$, width $6\\text{{ m}}$, wall height $4\\text{{ m}}$) "
        f"surmounted by an isosceles triangular roof (triangular ends with base $6\\text{{ m}}$, vertical height $4\\text{{ m}}$, "
        f"and slanted roof sides $5\\text{{ m}}$). The floor is included in the surface area. "
        f"Calculate the total exterior surface area of the shed (excluding the interior ceiling divider)."
    )
    ans_str = str(total_sa)
    sol = (
        f"1. **Rectangular Base & Walls** (5 faces, top ceiling is internal):\n"
        f"$$\\text{{Floor}} = 10 \\times 6 = 60\\text{{ m}}^2$$\n"
        f"$$\\text{{Walls}} = 2(10 \\times 4) + 2(6 \\times 4) = 80 + 48 = 128\\text{{ m}}^2$$\n"
        f"$$\\text{{Box Exposed}} = 60 + 128 = 188\\text{{ m}}^2$$\n\n"
        f"2. **Triangular Roof** (2 triangular ends + 2 sloping roof rectangles):\n"
        f"$$\\text{{2 Triangular Gables}} = 2 \\times \\left(\\frac{{1}}{{2}} \\times 6 \\times 4\\right) = 24\\text{{ m}}^2$$\n"
        f"$$\\text{{2 Slanted Roof Rectangles}} = 2 \\times (5 \\times 10) = 100\\text{{ m}}^2$$\n"
        f"$$\\text{{Roof Exposed}} = 24 + 100 = 124\\text{{ m}}^2$$\n\n"
        f"3. **Total Surface Area**:\n"
        f"$$\\text{{Total SA}} = 188 + 124 = {total_sa}\\text{{ m}}^2$$"
    )
    return {
        "subskill": "25_surface_area_composite_rectangular_prism_and_triangular_roof",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": ans_str,
        "sample_answer": f"{ans_str} m²",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Exposed box area (floor + 4 walls): 188 m²", "marks": 1},
            {"step": "Exposed roof area (2 gables + 2 roof slopes): 124 m²", "marks": 1},
            {"step": f"Total surface area: {total_sa} m²", "marks": 1},
        ],
        "hints": [
            "Do NOT include the ceiling where the roof joins the box; it is an interior wall.",
            "Box surface: floor ($60$) + 4 walls ($128$) = $188\\text{{ m}}^2$.",
            "Roof surface: 2 triangles ($24$) + 2 roof slopes ($100$) = $124\\text{{ m}}^2$.",
            f"Total = $188 + 124 = {total_sa}\\text{{ m}}^2$.",
        ],
        "misconception_tags": ["included_internal_ceiling_in_composite_shed"],
    }
