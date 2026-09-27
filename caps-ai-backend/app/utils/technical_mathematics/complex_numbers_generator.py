"""Grade 10–12 Technical Mathematics — Complex Numbers & Polar Form (Deterministic 6-Pillar Generator).
Covers modulus, argument, rectangular to polar conversion, Argand plane coordinates,
and polar multiplication/division (de Moivre's operations) for Paper 1 (Term 1).
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional
import sympy as sp


def _rng(seed: Optional[int] = None) -> random.Random:
    r = random.Random()
    if seed is not None:
        r.seed(int(seed))
    return r


def _fmt_sa(val: float | int, places: int = 1) -> str:
    if isinstance(val, int) or (isinstance(val, float) and val.is_integer()):
        return str(int(val))
    s = f"{val:.{places}f}".rstrip("0").rstrip(".")
    return s.replace(".", "{,}")


# --------------------------------------------------------------------------- #
# Sub-Drill: Modulus Calculation (|z|)
# --------------------------------------------------------------------------- #
def _build_modulus_drill(r: random.Random) -> Dict[str, Any]:
    a = r.choice([-8, -6, -5, -4, -3, 3, 4, 5, 6, 8])
    b = r.choice([-8, -6, -5, -4, -3, 3, 4, 5, 6, 8])
    r_sq = a**2 + b**2
    r_surd = sp.sqrt(r_sq)

    sign_b = "+" if b > 0 else "-"
    abs_b = abs(b)
    z_str = f"{a} {sign_b} {abs_b}i"

    prompt = (
        f"Given the complex number $z = {z_str}$.\n\n"
        f"Calculate the modulus $|z|$ (or $r$). Leave your answer in simplest surd form."
    )

    ans_latex = rf"|z| = \sqrt{{({a})^2 + ({b})^2}} = \sqrt{{{r_sq}}} = {sp.latex(r_surd)}"

    marking_schema = {
        "total_marks": 2,
        "marking_points": [
            {"id": "mp1", "desc": rf"Formula substitution: \sqrt{{({a})^2 + ({b})^2}}", "marks": 1, "editable": True},
            {"id": "mp2", "desc": rf"Simplest surd value: {sp.latex(r_surd)}", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "squared_imaginary_unit_i", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Recall the modulus formula: $|z| = \\sqrt{a^2 + b^2}$.",
        "tier_2": f"Here $a = {a}$ and $b = {b}$. Do NOT include $i$ inside the square.",
        "tier_3": f"Calculation: $|z| = \\sqrt{{{a}^2 + ({b})^2}} = \\sqrt{{{r_sq}}} = {sp.latex(r_surd)}$.",
    }

    return {
        "id": f"tech_cplx_mod_{r.randint(100000, 999999)}",
        "question_id": f"tech_cplx_mod_{r.randint(100000, 999999)}",
        "topic": "technical_mathematics_complex_numbers",
        "subskill": "complex_modulus_elementary",
        "learning_objective_id": "techmath_complex_modulus",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["squared_imaginary_unit_i", "forgot_square_root_in_modulus"],
        "keywords": ["complex numbers", "modulus", "magnitude", "surd form"],
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 3,
        "mode": "elementary_modulus_calc",
        "difficulty": "medium",
        "marks": 2,
    }


# --------------------------------------------------------------------------- #
# Sub-Drill: Argument Calculation (theta in degrees)
# --------------------------------------------------------------------------- #
def _build_argument_drill(r: random.Random) -> Dict[str, Any]:
    # Select coordinates with clean or nice arguments
    coords = [
        (1, 1, 1, 45.0),
        (-1, 1, 2, 135.0),
        (-1, -1, 3, 225.0),
        (1, -1, 4, 315.0),
        (3, 4, 1, 53.1),
        (-3, 4, 2, 126.9),
        (-3, -4, 3, 233.1),
        (3, -4, 4, 306.9),
    ]
    a, b, quad, deg = r.choice(coords)

    sign_b = "+" if b > 0 else "-"
    abs_b = abs(b)
    z_str = f"{a} {sign_b} {abs_b}i"
    ref_angle = round(math.degrees(math.atan(abs(b) / abs(a))), 1)

    prompt = (
        f"Given the complex number $z = {z_str}$.\n\n"
        f"1. Identify the Cartesian quadrant in which $z$ lies on the Argand diagram.\n"
        f"2. Calculate the argument $\\theta$ in degrees, where $0^\\circ \\le \\theta < 360^\\circ$."
    )

    sample_answer = (
        f"1. Quadrant: Since $a = {a}$ (real axis) and $b = {b}$ (imaginary axis), $z$ lies in **Quadrant {quad}**.\n"
        f"2. Reference angle: $\\alpha = \\tan^{{-1}}\\left(\\frac{{{abs_b}}}{{{abs(a)}}}\\right) = {_fmt_sa(ref_angle)}^\\circ$.\n"
        f"   Quadrant {quad} adjustment: $\\theta = {_fmt_sa(deg)}^\\circ$."
    )

    ans_latex = rf"\text{{Quadrant }} {quad}, \quad \theta = {_fmt_sa(deg)}^\circ"

    marking_schema = {
        "total_marks": 3,
        "marking_points": [
            {"id": "mp1", "desc": f"Correct quadrant identification (Quadrant {quad})", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Reference angle calculation: alpha = {_fmt_sa(ref_angle)} deg", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Quadrant adjustment to argument: theta = {_fmt_sa(deg)} deg", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "wrong_quadrant_adjustment", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Plot the point $(a, b)$ on the Argand plane to determine the quadrant.",
        "tier_2": "Calculate the reference angle $\\alpha = \\tan^{-1}(|b| / |a|)$. Then adjust: Quad 2 is $180^\\circ - \\alpha$, Quad 3 is $180^\\circ + \\alpha$, Quad 4 is $360^\\circ - \\alpha$.",
        "tier_3": f"Quadrant {quad}: $\\theta = {_fmt_sa(deg)}^\\circ$.",
    }

    return {
        "id": f"tech_cplx_arg_{r.randint(100000, 999999)}",
        "question_id": f"tech_cplx_arg_{r.randint(100000, 999999)}",
        "topic": "technical_mathematics_complex_numbers",
        "subskill": "complex_argument_elementary",
        "learning_objective_id": "techmath_complex_argument",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": sample_answer,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["forgot_quadrant_correction_argument", "inverted_tan_ratio"],
        "keywords": ["complex numbers", "argument", "Argand diagram", "quadrant", "degrees"],
        "term": 1,
        "caps_weight_percent": 20,
        "suggested_duration_mins": 3,
        "mode": "elementary_argument_quadrant",
        "difficulty": "medium",
        "marks": 3,
    }


# --------------------------------------------------------------------------- #
# Sub-Drill: Polar Form Conversion (z = r cis theta)
# --------------------------------------------------------------------------- #
def _build_polar_conversion_drill(r: random.Random) -> Dict[str, Any]:
    a = r.choice([-4, -3, -2, -1, 1, 2, 3, 4])
    b = r.choice([-4, -3, -2, -1, 1, 2, 3, 4])

    r_sq = a**2 + b**2
    r_exact = sp.sqrt(r_sq)
    rad = math.atan2(b, a)
    deg = round(math.degrees(rad) % 360, 1)

    sign_b = "+" if b > 0 else "-"
    abs_b = abs(b)
    z_str = f"{a} {sign_b} {abs_b}i"

    prompt = (
        f"Convert the complex number $z = {z_str}$ from rectangular form to polar form: "
        f"$z = r\\operatorname{{cis}}\\theta$ (where $0^\\circ \\le \\theta < 360^\\circ$)."
    )

    ans_latex = rf"z = {sp.latex(r_exact)}\operatorname{{cis}}({_fmt_sa(deg)}^\circ)"

    sample_answer = (
        f"1. Modulus: $r = \\sqrt{{{a}^2 + ({b})^2}} = \\sqrt{{{r_sq}}} = {sp.latex(r_exact)}$\n"
        f"2. Argument: $\\theta = \\text{{atan2}}({b}, {a}) = {_fmt_sa(deg)}^\\circ$\n"
        f"3. Polar form: $z = {sp.latex(r_exact)}\\operatorname{{cis}}({_fmt_sa(deg)}^\\circ)$"
    )

    marking_schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": f"Modulus r = {sp.latex(r_exact)}", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Reference angle calculation", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Argument theta = {_fmt_sa(deg)} deg with quadrant adjustment", "marks": 1, "editable": True},
            {"id": "mp4", "desc": f"Final polar expression: z = {sp.latex(r_exact)} cis {_fmt_sa(deg)} deg", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "wrong_quadrant", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Calculate $r = \\sqrt{a^2 + b^2}$ and $\\theta = \\arctan(b/a)$ adjusted for quadrant.",
        "tier_2": "The polar form is written as $z = r(\\cos\\theta + i\\sin\\theta) = r\\operatorname{cis}\\theta$.",
        "tier_3": f"Final answer: $z = {sp.latex(r_exact)}\\operatorname{{cis}}({_fmt_sa(deg)}^\\circ)$.",
    }

    return {
        "id": f"tech_cplx_pol_{r.randint(100000, 999999)}",
        "question_id": f"tech_cplx_pol_{r.randint(100000, 999999)}",
        "topic": "technical_mathematics_complex_numbers",
        "subskill": "polar_form_elementary",
        "learning_objective_id": "techmath_polar_conversion",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": sample_answer,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["confused_sin_cos_in_polar", "forgot_quadrant_correction_argument"],
        "keywords": ["polar form", "cis notation", "modulus", "argument", "complex conversion"],
        "term": 1,
        "caps_weight_percent": 25,
        "suggested_duration_mins": 5,
        "mode": "elementary_polar_conversion",
        "difficulty": "medium",
        "marks": 4,
    }


# --------------------------------------------------------------------------- #
# Compound: Polar Multiplication & Division Operations (8 Marks Exam Standard)
# --------------------------------------------------------------------------- #
def _build_compound_polar_operations(r: random.Random) -> Dict[str, Any]:
    # Nice angles: 30, 45, 60, 90, 120, 135, 150, 180, 210, 225, 240, 270, 300, 315, 330
    theta1 = r.choice([30, 45, 60, 90, 120, 135, 150])
    theta2 = r.choice([30, 45, 60, 90, 120])
    r1 = r.choice([2, 3, 4, 6])
    r2 = r.choice([2, 3, 4])

    op = r.choice(["multiply", "divide"])

    if op == "multiply":
        r_res = r1 * r2
        theta_res = (theta1 + theta2) % 360
        op_sym = r"\times"
        formula_note = r"r_1 r_2 \operatorname{cis}(\theta_1 + \theta_2)"
        prompt = (
            f"Given two complex numbers in polar form:\n"
            f"$$z_1 = {r1}\\operatorname{{cis}}({theta1}^\\circ) \\quad \\text{{and}} \\quad "
            f"z_2 = {r2}\\operatorname{{cis}}({theta2}^\\circ)$$\n\n"
            f"1. Calculate the product $z_1 \\cdot z_2$ in polar form $r\\operatorname{{cis}}\\theta$.\n"
            f"2. Convert the resulting complex number into rectangular form $a + bi$.\n"
            f"3. State the quadrant of the Argand plane in which $z_1 \\cdot z_2$ lies."
        )
    else:
        # ensure r1 is a multiple of r2
        r1_mult = r1 * r2
        r_res = r1
        theta_res = (theta1 - theta2) % 360
        op_sym = r"\div"
        formula_note = r"\frac{r_1}{r_2} \operatorname{cis}(\theta_1 - \theta_2)"
        prompt = (
            f"Given two complex numbers in polar form:\n"
            f"$$z_1 = {r1_mult}\\operatorname{{cis}}({theta1}^\\circ) \\quad \\text{{and}} \\quad "
            f"z_2 = {r2}\\operatorname{{cis}}({theta2}^\\circ)$$\n\n"
            f"1. Calculate the quotient $\\frac{{z_1}}{{z_2}}$ in polar form $r\\operatorname{{cis}}\\theta$.\n"
            f"2. Convert the resulting complex number into rectangular form $a + bi$.\n"
            f"3. State the quadrant of the Argand plane in which $\\frac{{z_1}}{{z_2}}$ lies."
        )

    # Convert to rectangular
    rad = math.radians(theta_res)
    a_val = round(r_res * math.cos(rad), 2)
    b_val = round(r_res * math.sin(rad), 2)

    quad = 1 if (a_val >= 0 and b_val >= 0) else (2 if a_val < 0 and b_val >= 0 else (3 if a_val < 0 and b_val < 0 else 4))
    sign_b = "+" if b_val >= 0 else "-"
    abs_b = abs(b_val)
    rect_str = f"{_fmt_sa(a_val)} {sign_b} {_fmt_sa(abs_b)}i"

    ans_latex = (
        rf"\text{{Polar: }} {r_res}\operatorname{{cis}}({theta_res}^\circ), \quad "
        rf"\text{{Rectangular: }} {rect_str}, \quad \text{{Quadrant: }} {quad}"
    )

    sample_answer = (
        f"1. Polar Operation ({formula_note}):\n"
        f"   Modulus: $r = {r_res}$\n"
        f"   Argument: $\\theta = {theta_res}^\\circ$\n"
        f"   Result in Polar Form: $z = {r_res}\\operatorname{{cis}}({theta_res}^\\circ)$\n\n"
        f"2. Conversion to Rectangular Form ($a = r\\cos\\theta, b = r\\sin\\theta$):\n"
        f"   $a = {r_res}\\cos({theta_res}^\\circ) = {_fmt_sa(a_val)}$\n"
        f"   $b = {r_res}\\sin({theta_res}^\\circ) = {_fmt_sa(b_val)}$\n"
        f"   Rectangular Form: $z = {rect_str}$\n\n"
        f"3. Argand Quadrant:\n"
        f"   Since $a = {_fmt_sa(a_val)}$ and $b = {_fmt_sa(b_val)}$, $z$ lies in **Quadrant {quad}**."
    )

    marking_schema = {
        "total_marks": 8,
        "marking_points": [
            {"id": "mp1", "desc": "Multiply/divide moduli correctly", "marks": 2, "editable": True},
            {"id": "mp2", "desc": "Add/subtract arguments correctly", "marks": 2, "editable": True},
            {"id": "mp3", "desc": f"Correct polar result: {r_res} cis({theta_res} deg)", "marks": 1, "editable": True},
            {"id": "mp4", "desc": f"Real part conversion a = {r_res} cos({theta_res}) = {_fmt_sa(a_val)}", "marks": 1, "editable": True},
            {"id": "mp5", "desc": f"Imaginary part conversion b = {r_res} sin({theta_res}) = {_fmt_sa(b_val)}", "marks": 1, "editable": True},
            {"id": "mp6", "desc": f"Correct quadrant identification (Quadrant {quad})", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "subtracted_instead_of_added_arguments", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Recall: For multiplication, multiply the moduli ($r_1 \\times r_2$) and add the arguments ($\\theta_1 + \\theta_2$). For division, divide moduli ($r_1 / r_2$) and subtract arguments ($\\theta_1 - \\theta_2$).",
        "tier_2": "To convert back to rectangular form, use $a = r\\cos\\theta$ and $b = r\\sin\\theta$.",
        "tier_3": f"Polar result: ${r_res}\\operatorname{{cis}}({theta_res}^\\circ)$. Rectangular: ${rect_str}$. Quadrant: {quad}.",
    }

    return {
        "id": f"tech_cplx_comp_{r.randint(100000, 999999)}",
        "question_id": f"tech_cplx_comp_{r.randint(100000, 999999)}",
        "topic": "technical_mathematics_complex_numbers",
        "subskill": "complex_polar_operations_compound",
        "learning_objective_id": "techmath_polar_operations",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": sample_answer,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": [
            "multiplied_arguments_instead_of_adding",
            "divided_arguments_instead_of_subtracting",
            "confused_sin_cos_in_polar",
        ],
        "keywords": ["complex numbers", "polar multiplication", "polar division", "de Moivre", "Argand diagram", "cis"],
        "term": 1,
        "caps_weight_percent": 35,
        "suggested_duration_mins": 12,
        "mode": "compound",
        "difficulty": "hard",
        "marks": 8,
    }


# --------------------------------------------------------------------------- #
# Public Dispatcher
# --------------------------------------------------------------------------- #
BUILDERS = {
    "compound": _build_compound_polar_operations,
    "elementary_modulus_calc": _build_modulus_drill,
    "elementary_argument_quadrant": _build_argument_drill,
    "elementary_polar_conversion": _build_polar_conversion_drill,
}


def generate(
    subskill: Optional[str] = None,
    difficulty: str = "hard",
    count: int = 1,
    seed: Optional[int] = None,
    mode: str = "compound",
    **kwargs: Any,
) -> Dict[str, Any]:
    """Generates deterministic Grade 10-12 Technical Mathematics Complex Numbers questions."""
    base_seed = 42 if seed is None else int(seed)
    chosen_mode = mode if mode in BUILDERS else ("compound" if subskill is None else subskill)
    builder = BUILDERS.get(chosen_mode, _build_compound_polar_operations)

    questions = []
    for i in range(max(1, count)):
        r = _rng(base_seed * 1000 + i)
        q = builder(r)
        q["seed"] = base_seed * 1000 + i
        questions.append(q)

    return {"questions": questions}
