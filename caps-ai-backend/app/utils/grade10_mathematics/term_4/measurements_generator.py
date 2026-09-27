"""Grade 10 & 11 Mathematics — Measurements: Surface Area, Volume & Dimensional Scaling (k-factor).
Deterministic 6-Pillar Generator conforming to CAPS curriculum standards.
Reference curriculum: curriculum_docs_auto/Mathematics_Gr10/Term 4/01. Measurements.md

Covers:
- Right prisms, right circular cylinders
- Right pyramids, right circular cones, spheres, hemispheres
- Total Surface Area (TSA) and Volume (V)
- Effect of multiplying one or more dimensions by factor k:
  * Linear scaling: perimeter/radius/height * k
  * Area scaling: Area * k^2 (if all dimensions scaled by k)
  * Volume scaling: Volume * k^3 (if all dimensions scaled by k)
- South African comma decimals convention (e.g. 15{,}5 cm^3)
- SymPy symbolic calculation with exact and rounded decimal equivalents.

Supports compound (10 marks) and elementary sub-drills:
- elementary_surface_area (3 marks)
- elementary_volume (3 marks)
- elementary_scaling_k (4 marks)
"""
from __future__ import annotations

import math
import random
import uuid
from typing import Any, Dict, List, Optional

import sympy as sp

from .._math_common import make_id, num, rng


def _make_step(from_latex: str, to_latex_str: str, op: str, rule: str = "") -> Dict[str, Any]:
    return {
        "from_latex": from_latex,
        "to_latex": to_latex_str,
        "from_sympy": "",
        "to_sympy": "",
        "op": op,
        "rule": rule,
        "common_errors": [],
    }


def _fmt_dec(val: float, decimals: int = 2) -> str:
    """Format float using South African comma decimal separator."""
    rounded = round(val, decimals)
    s = f"{rounded:.{decimals}f}".rstrip("0").rstrip(".") if decimals > 0 and "." in f"{rounded:.{decimals}f}" else f"{int(rounded)}"
    return s.replace(".", "{,}")


# --------------------------------------------------------------------------- #
# Sub-drill 1: Surface Area (3 marks)
# --------------------------------------------------------------------------- #
def _build_surface_area_drill(r: random.Random) -> Dict[str, Any]:
    solid_type = r.choice(["cylinder", "sphere", "cone", "rectangular_prism"])

    if solid_type == "cylinder":
        radius = r.randint(3, 14)
        height = r.randint(6, 25)
        # TSA = 2*pi*r^2 + 2*pi*r*h = 2*pi*r*(r + h)
        exact_tsa = 2 * math.pi * radius * (radius + height)
        ans_dec = _fmt_dec(exact_tsa, 2)
        unit = "cm^2"

        prompt = (
            f"A closed right circular cylinder has a base radius of ${radius}\\text{{ cm}}$ "
            f"and a perpendicular height of ${height}\\text{{ cm}}$.\n\n"
            f"Calculate the **Total Surface Area** of the cylinder. "
            f"Use $\\pi \\approx 3.14159$ and round your final answer to **TWO** decimal places."
        )

        steps = [
            _make_step(
                from_latex=r"A = 2\pi r^2 + 2\pi r h",
                to_latex_str=rf"A = 2\pi({radius})^2 + 2\pi({radius})({height})",
                op="Substitute given radius and height into total surface area formula",
                rule="Cylinder surface area formula",
            ),
            _make_step(
                from_latex=rf"A = 2\pi({radius**2}) + 2\pi({radius*height})",
                to_latex_str=rf"A = {2*radius**2}\pi + {2*radius*height}\pi = {2*radius*(radius+height)}\pi",
                op="Simplify algebraic terms in terms of pi",
                rule="Factorisation and addition",
            ),
            _make_step(
                from_latex=rf"A = {2*radius*(radius+height)}\pi",
                to_latex_str=rf"A \approx {ans_dec}\text{{ {unit}}}",
                op="Evaluate numerical product and round to two decimal places",
                rule="Decimal rounding with SA comma convention",
            ),
        ]

    elif solid_type == "sphere":
        radius = r.randint(4, 18)
        # TSA = 4*pi*r^2
        exact_tsa = 4 * math.pi * (radius ** 2)
        ans_dec = _fmt_dec(exact_tsa, 2)
        unit = "cm^2"

        prompt = (
            f"Calculate the total surface area of a solid sphere with radius $r = {radius}\\text{{ cm}}$.\n\n"
            f"Round off your answer to **TWO** decimal places."
        )

        steps = [
            _make_step(
                from_latex=r"A = 4\pi r^2",
                to_latex_str=rf"A = 4\pi({radius})^2 = {4 * radius**2}\pi",
                op="Substitute radius into sphere surface area formula",
                rule="Sphere surface area formula",
            ),
            _make_step(
                from_latex=rf"A = {4 * radius**2}\pi",
                to_latex_str=rf"A \approx {ans_dec}\text{{ {unit}}}",
                op="Compute numerical value and round",
                rule="Arithmetic evaluation",
            ),
        ]

    elif solid_type == "cone":
        radius = r.choice([3, 5, 6, 8, 9])
        height = r.choice([4, 12, 8, 15, 12])
        slant = int(round(math.sqrt(radius**2 + height**2)))
        exact_tsa = math.pi * radius * (radius + slant)
        ans_dec = _fmt_dec(exact_tsa, 2)
        unit = "cm^2"

        prompt = (
            f"A right circular cone has a base radius of ${radius}\\text{{ cm}}$ and a perpendicular "
            f"height of ${height}\\text{{ cm}}$.\n\n"
            f"1. Calculate the slant height $s$ using the Theorem of Pythagoras.\n"
            f"2. Calculate the Total Surface Area of the cone ($A = \\pi r^2 + \\pi r s$). "
            f"Round to TWO decimal places."
        )

        steps = [
            _make_step(
                from_latex=r"s = \sqrt{r^2 + h^2}",
                to_latex_str=rf"s = \sqrt{{{radius}^2 + {height}^2}} = \sqrt{{{radius**2 + height**2}}} = {slant}\text{{ cm}}",
                op="Calculate slant height using Pythagoras",
                rule="Pythagoras Theorem",
            ),
            _make_step(
                from_latex=r"A = \pi r^2 + \pi r s",
                to_latex_str=rf"A = \pi({radius})^2 + \pi({radius})({slant}) = {radius**2 + radius*slant}\pi \approx {ans_dec}\text{{ {unit}}}",
                op="Substitute radius and slant height into total surface area formula",
                rule="Cone surface area formula",
            ),
        ]

    else:  # rectangular_prism
        length = r.randint(5, 15)
        width = r.randint(4, 10)
        height = r.randint(3, 8)
        exact_tsa = 2 * (length * width + length * height + width * height)
        ans_dec = str(exact_tsa)
        unit = "cm^2"

        prompt = (
            f"A rectangular prism has length $l = {length}\\text{{ cm}}$, width $w = {width}\\text{{ cm}}$, "
            f"and height $h = {height}\\text{{ cm}}$.\n\n"
            f"Calculate the **Total Surface Area** of the prism."
        )

        steps = [
            _make_step(
                from_latex=r"A = 2(lb + lh + bh)",
                to_latex_str=rf"A = 2(({length})({width}) + ({length})({height}) + ({width})({height}))",
                op="Substitute dimensions into rectangular prism surface area formula",
                rule="Rectangular prism formula",
            ),
            _make_step(
                from_latex=rf"A = 2({length*width} + {length*height} + {width*height})",
                to_latex_str=rf"A = 2({length*width + length*height + width*height}) = {exact_tsa}\text{{ {unit}}}",
                op="Evaluate bracketed sums and multiply by 2",
                rule="Arithmetic multiplication",
            ),
        ]

    return {
        "id": make_id("math_sa"),
        "question_type": "math_steps",
        "question_text": prompt,
        "correct_answer": ans_dec,
        "sample_answer": f"Total Surface Area = {ans_dec} {unit}",
        "marks": 3,
        "term": 4,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 5,
        "learning_objective_id": "math_measurements_surface_area",
        "mode": "elementary_surface_area",
        "misconception_tags": ["omitted_base_area_in_surface_area", "confused_slant_with_vertical_height", "squared_dimensions_incorrectly"],
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp_1", "desc": "Correct formula selection [M]", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Accurate substitution of dimensions [M]", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "Final answer with correct rounding [A]", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "tier_1": f"Identify the solid: this is a {solid_type.replace('_', ' ')}. Recall its surface area formula.",
            "tier_2": "Substitute all known dimensions. Take care to distinguish vertical height from slant height if applicable.",
            "tier_3": f"Final answer: {ans_dec} {unit}.",
        },
    }


# --------------------------------------------------------------------------- #
# Sub-drill 2: Volume (3 marks)
# --------------------------------------------------------------------------- #
def _build_volume_drill(r: random.Random) -> Dict[str, Any]:
    solid_type = r.choice(["cylinder", "sphere", "cone", "pyramid"])

    if solid_type == "cylinder":
        radius = r.randint(4, 12)
        height = r.randint(5, 20)
        vol = math.pi * (radius ** 2) * height
        ans_dec = _fmt_dec(vol, 2)
        unit = "cm^3"

        prompt = (
            f"Calculate the **Volume** of a right circular cylinder with radius $r = {radius}\\text{{ cm}}$ "
            f"and height $h = {height}\\text{{ cm}}$.\n\n"
            f"Round off your answer to **TWO** decimal places."
        )

        steps = [
            _make_step(
                from_latex=r"V = \pi r^2 h",
                to_latex_str=rf"V = \pi({radius})^2({height}) = {radius**2 * height}\pi",
                op="Substitute radius and height into cylinder volume formula",
                rule="Cylinder volume formula",
            ),
            _make_step(
                from_latex=rf"V = {radius**2 * height}\pi",
                to_latex_str=rf"V \approx {ans_dec}\text{{ {unit}}}",
                op="Calculate decimal equivalent",
                rule="Decimal rounding",
            ),
        ]

    elif solid_type == "sphere":
        radius = r.randint(3, 15)
        vol = (4.0 / 3.0) * math.pi * (radius ** 3)
        ans_dec = _fmt_dec(vol, 2)
        unit = "cm^3"

        prompt = (
            f"Calculate the **Volume** of a sphere with radius $r = {radius}\\text{{ cm}}$.\n\n"
            f"Use the formula $V = \\frac{{4}}{{3}}\\pi r^3$ and round off your answer to **TWO** decimal places."
        )

        steps = [
            _make_step(
                from_latex=r"V = \frac{4}{3}\pi r^3",
                to_latex_str=rf"V = \frac{{4}}{{3}}\pi({radius})^3 = \frac{{{4 * radius**3}}}{{3}}\pi",
                op="Substitute radius into sphere volume formula",
                rule="Sphere volume formula",
            ),
            _make_step(
                from_latex=rf"V = \frac{{{4 * radius**3}}}{{3}}\pi",
                to_latex_str=rf"V \approx {ans_dec}\text{{ {unit}}}",
                op="Calculate final decimal volume",
                rule="Arithmetic rounding",
            ),
        ]

    elif solid_type == "cone":
        radius = r.randint(3, 12)
        height = r.randint(6, 18)
        vol = (1.0 / 3.0) * math.pi * (radius ** 2) * height
        ans_dec = _fmt_dec(vol, 2)
        unit = "cm^3"

        prompt = (
            f"A right circular cone has base radius $r = {radius}\\text{{ cm}}$ and perpendicular "
            f"height $h = {height}\\text{{ cm}}$.\n\n"
            f"Calculate the **Volume** of the cone. Round to **TWO** decimal places."
        )

        steps = [
            _make_step(
                from_latex=r"V = \frac{1}{3}\pi r^2 h",
                to_latex_str=rf"V = \frac{{1}}{{3}}\pi({radius})^2({height})",
                op="Substitute into cone volume formula",
                rule="Cone volume formula",
            ),
            _make_step(
                from_latex=rf"V = \frac{{{radius**2 * height}}}{{3}}\pi",
                to_latex_str=rf"V \approx {ans_dec}\text{{ {unit}}}",
                op="Compute numerical value",
                rule="Decimal evaluation",
            ),
        ]

    else:  # pyramid
        base_side = r.randint(4, 14)
        height = r.randint(6, 18)
        vol = (1.0 / 3.0) * (base_side ** 2) * height
        ans_dec = _fmt_dec(vol, 2)
        unit = "cm^3"

        prompt = (
            f"A right pyramid has a square base with side length ${base_side}\\text{{ cm}}$ "
            f"and a perpendicular height of ${height}\\text{{ cm}}$.\n\n"
            f"Calculate the **Volume** of the pyramid. Round to **TWO** decimal places."
        )

        steps = [
            _make_step(
                from_latex=r"V = \frac{1}{3} \times \text{base area} \times h",
                to_latex_str=rf"V = \frac{{1}}{{3}}({base_side}^2)({height}) = \frac{{{base_side**2 * height}}}{{3}}",
                op="Substitute base area and height into pyramid volume formula",
                rule="Pyramid volume formula",
            ),
            _make_step(
                from_latex=rf"V = \frac{{{base_side**2 * height}}}{{3}}",
                to_latex_str=rf"V \approx {ans_dec}\text{{ {unit}}}",
                op="Evaluate quotient",
                rule="Arithmetic division",
            ),
        ]

    return {
        "id": make_id("math_vol"),
        "question_type": "math_steps",
        "question_text": prompt,
        "correct_answer": ans_dec,
        "sample_answer": f"Volume = {ans_dec} {unit}",
        "marks": 3,
        "term": 4,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 5,
        "learning_objective_id": "math_measurements_volume",
        "mode": "elementary_volume",
        "misconception_tags": ["forgot_one_third_in_cone_volume", "used_diameter_instead_of_radius", "cube_vs_square_units"],
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp_1", "desc": "Volume formula [M]", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Accurate substitution [M]", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "Final numerical answer [A]", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "tier_1": f"Recall the volume formula for a {solid_type.replace('_', ' ')}.",
            "tier_2": "Cylinder: V = pi * r^2 * h. Cone/Pyramid: V = (1/3) * base_area * h. Sphere: V = (4/3) * pi * r^3.",
            "tier_3": f"Volume = {ans_dec} {unit}.",
        },
    }


# --------------------------------------------------------------------------- #
# Sub-drill 3: Dimensional Scaling by Factor k (4 marks)
# --------------------------------------------------------------------------- #
def _build_scaling_drill(r: random.Random) -> Dict[str, Any]:
    k = r.choice([2, 3, 4, 5, 0.5])
    k_str = str(int(k)) if k == int(k) else "0{,}5"
    k_sq = k ** 2
    k_sq_str = str(int(k_sq)) if k_sq == int(k_sq) else "0{,}25"
    k_cb = k ** 3
    k_cb_str = str(int(k_cb)) if k_cb == int(k_cb) else "0{,}125"

    initial_vol = r.randint(10, 50) * 10
    scaled_vol = initial_vol * k_cb
    scaled_vol_str = _fmt_dec(scaled_vol, 2)

    prompt = (
        f"A 3D solid has an initial volume of ${initial_vol}\\text{{ cm}}^3$ and an initial "
        f"total surface area of $A$.\n\n"
        f"All linear dimensions of the solid are multiplied by a factor of $k = {k_str}$.\n\n"
        f"**Required:**\n"
        f"1. By what factor does the **Total Surface Area** increase? Express in terms of $k$.\n"
        f"2. By what factor does the **Volume** increase? Express in terms of $k$.\n"
        f"3. Calculate the new volume of the solid after scaling."
    )

    correct = {
        "area_factor": f"k^2 = {k_sq_str}",
        "volume_factor": f"k^3 = {k_cb_str}",
        "new_volume": f"{scaled_vol_str} cm^3",
    }

    return {
        "id": make_id("math_scale_k"),
        "question_type": "structured",
        "question_text": prompt,
        "correct_answer": correct,
        "sample_answer": f"Area: multiplied by {k_sq_str}; Volume: multiplied by {k_cb_str} (New V = {scaled_vol_str} cm^3)",
        "marks": 4,
        "term": 4,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 6,
        "learning_objective_id": "math_measurements_factor_k",
        "mode": "elementary_scaling_k",
        "misconception_tags": ["linear_factor_applied_to_volume", "multiplied_volume_by_k_instead_of_k_cubed"],
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp_1", "desc": "Surface area scales by factor k^2 [M]", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Volume scales by factor k^3 [M]", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "Calculation of k^3 numerical value [A]", "marks": 1, "editable": True},
                {"id": "mp_4", "desc": "New volume calculation [CA]", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "tier_1": "Linear dimension: * k. Two dimensions (Area): * k^2. Three dimensions (Volume): * k^3.",
            "tier_2": f"Area increases by k^2 = ({k_str})^2 = {k_sq_str}. Volume increases by k^3 = ({k_str})^3 = {k_cb_str}.",
            "tier_3": f"New volume = {initial_vol} * {k_cb_str} = {scaled_vol_str} cm^3.",
        },
    }


# --------------------------------------------------------------------------- #
# COMPOUND: Full Measurements Exam Question (10 marks)
# --------------------------------------------------------------------------- #
def _build_compound(r: random.Random) -> List[Dict[str, Any]]:
    return [
        _build_surface_area_drill(r),
        _build_volume_drill(r),
        _build_scaling_drill(r),
    ]


# --------------------------------------------------------------------------- #
# PUBLIC API
# --------------------------------------------------------------------------- #
def generate(
    seed: Optional[int] = None,
    count: int = 1,
    mode: str = "compound",
    subskill: str = "mixed",
    difficulty: str = "medium",
    **kwargs,
) -> List[Dict[str, Any]]:
    r = rng(seed)
    questions: List[Dict[str, Any]] = []

    builders = {
        "elementary_surface_area": _build_surface_area_drill,
        "elementary_volume": _build_volume_drill,
        "elementary_scaling_k": _build_scaling_drill,
    }

    for _ in range(count):
        sub_r = rng(r.randint(1, 1_000_000_000))
        if mode == "compound":
            questions.extend(_build_compound(sub_r))
        elif mode in builders:
            questions.append(builders[mode](sub_r))
        else:
            questions.extend(_build_compound(sub_r))

    return questions
