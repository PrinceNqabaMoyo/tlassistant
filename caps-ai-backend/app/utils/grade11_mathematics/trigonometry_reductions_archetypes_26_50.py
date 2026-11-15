"""Grade 11 Mathematics — Trigonometry Archetypes 26–50.
Grounded in South African National Curriculum Standards for Grade 11 Mathematics.
Covers:
- Quotient and square Pythagorean identities
- Proving identities (LHS = RHS, common denominator, factoring, undefined restrictions)
- General solutions: sin, cos, tan, coefficient arguments, co-ratio equations, tan substitution, common factor, quadratics
- Solutions in specific restricted intervals
- 2D Triangle trigonometry: Area Rule, Sine Rule, Cosine Rule with parameterized inline_svg diagrams
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional
import sympy as sp

from app.utils.grade11_mathematics._math_common import (
    make_math_question,
    step,
    solution_graph,
    num,
)

TOPIC = "Trigonometry"
LO_PREFIX = "math11_trig"


def _triangle_svg(
    side_a: float,
    side_b: float,
    side_c: float,
    angle_c_deg: float,
    label_a: str = "",
    label_b: str = "",
    label_c: str = "",
    angle_label: str = "",
) -> Dict[str, Any]:
    """Generates an inline SVG showing triangle ABC with side and angle labels."""
    # Place C at origin (80, 200)
    # Side CB along horizontal axis to B
    # Side CA at angle_c_deg to A
    cx, cy = 80.0, 210.0
    # normalize base length to fit 240px
    max_dim = max(side_a, side_b, side_c, 1.0)
    scale = 200.0 / max_dim

    bx = cx + side_a * scale
    by = cy

    rad = math.radians(min(max(angle_c_deg, 20.0), 150.0))
    ax = cx + side_b * scale * math.cos(rad)
    ay = cy - side_b * scale * math.sin(rad)

    # Arc at vertex C
    r_arc = 24.0
    arc_x = cx + r_arc * math.cos(rad)
    arc_y = cy - r_arc * math.sin(rad)
    arc_path = f"M {cx + r_arc} {cy} A {r_arc} {r_arc} 0 0 0 {arc_x:.1f} {arc_y:.1f}"

    svg = (
        f'<svg viewBox="0 0 420 280" width="100%" height="240" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="420" height="280" fill="#f8fafc" rx="8"/>'
        # Triangle polygon
        f'<polygon points="{ax:.1f},{ay:.1f} {bx:.1f},{by:.1f} {cx:.1f},{cy:.1f}" '
        f'fill="#eff6ff" stroke="#1e40af" stroke-width="2.5" stroke-linejoin="round"/>'
        # Angle arc at C
        f'<path d="{arc_path}" fill="none" stroke="#f59e0b" stroke-width="2"/>'
        # Vertices labels
        f'<text x="{ax - 6:.1f}" y="{ay - 10:.1f}" font-size="14" fill="#1e293b" font-weight="bold">A</text>'
        f'<text x="{bx + 8:.1f}" y="{by + 5:.1f}" font-size="14" fill="#1e293b" font-weight="bold">B</text>'
        f'<text x="{cx - 16:.1f}" y="{cy + 16:.1f}" font-size="14" fill="#1e293b" font-weight="bold">C</text>'
        # Side labels
        f'<text x="{(cx + bx) / 2:.1f}" y="{cy + 18:.1f}" font-size="13" fill="#334155" text-anchor="middle">{label_a}</text>'
        f'<text x="{(cx + ax) / 2 - 14:.1f}" y="{(cy + ay) / 2:.1f}" font-size="13" fill="#334155">{label_b}</text>'
        f'<text x="{(ax + bx) / 2 + 10:.1f}" y="{(ay + by) / 2 - 6:.1f}" font-size="13" fill="#334155">{label_c}</text>'
        # Angle label at C
        f'<text x="{cx + 30:.1f}" y="{cy - 8:.1f}" font-size="12" fill="#d97706" font-weight="bold">{angle_label}</text>'
        f'</svg>'
    )
    return {
        "kind": "inline_svg",
        "svg": svg,
        "diagram_role": "context",
        "side_a": side_a,
        "side_b": side_b,
        "angle_c_deg": angle_c_deg,
    }


# ---------------------------------------------------------------------------
# 26. Quotient Identity: tan θ = sin θ / cos θ
# ---------------------------------------------------------------------------
def build_26_quotient_identity_substitution(r: random.Random) -> Dict[str, Any]:
    coef = r.choice([1, 2, 3, 4])
    coef_str = f"{coef}" if coef > 1 else ""
    prompt = (
        f"Simplify the trigonometric expression by using the quotient identity:\n\n"
        f"$${coef_str}\\tan\\theta \\cdot \\cos\\theta$$"
    )
    ans_latex = rf"{coef_str}\sin\theta"
    sample = (
        rf"\text{{Apply quotient identity }}\tan\theta = \frac{{\sin\theta}}{{\cos\theta}}:\\"
        rf"{coef_str}\left(\frac{{\sin\theta}}{{\cos\theta}}\right)\cos\theta = {ans_latex}"
    )
    return make_math_question(
        prefix="trig_26",
        topic=TOPIC,
        subskill="26_quotient_identity_substitution",
        learning_objective_id=f"{LO_PREFIX}_quotient_identity",
        prompt=prompt,
        prompt_latex=rf"{coef_str}\tan\theta \cdot \cos\theta",
        answer_latex=ans_latex,
        answer_sympy=f"{coef}*sin(theta)",
        sample_answer=sample,
        marking_schema={
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Substituted tan(theta) = sin(theta)/cos(theta)", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Cancelled cos(theta) to obtain {ans_latex}", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        hints={
            "1_nudge": "Replace $\\tan\\theta$ with its definition in terms of sine and cosine.",
            "2_concept": "The quotient identity is $\\tan\\theta = \\frac{\\sin\\theta}{\\cos\\theta}$ where $\\cos\\theta \\ne 0$.",
            "3_breakdown": f"${coef_str}\\left(\\frac{{\\sin\\theta}}{{\\cos\\theta}}\\right)\\cos\\theta = {ans_latex}$.",
        },
        misconception_tags=["inverted_quotient_identity"],
        keywords=["quotient identity", "tangent", "simplification"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=2,
        mode="26_quotient_identity_substitution",
        difficulty="easy",
    )


# ---------------------------------------------------------------------------
# 27. Square Pythagorean Identity: sin²θ + cos²θ = 1
# ---------------------------------------------------------------------------
def build_27_square_identity_pythagorean(r: random.Random) -> Dict[str, Any]:
    coef = r.choice([2, 3, 5, 7])
    prompt = (
        f"Simplify the trigonometric expression to a single numerical value:\n\n"
        f"$${coef}\\sin^2\\theta + {coef}\\cos^2\\theta$$"
    )
    ans_latex = str(coef)
    sample = (
        rf"\text{{Factor out the common factor }}{coef}:\\"
        rf"{coef}(\sin^2\theta + \cos^2\theta)\\"
        rf"\text{{Since }}\sin^2\theta + \cos^2\theta = 1:\\"
        rf"= {coef}(1) = {coef}"
    )
    return make_math_question(
        prefix="trig_27",
        topic=TOPIC,
        subskill="27_square_identity_pythagorean",
        learning_objective_id=f"{LO_PREFIX}_square_identity",
        prompt=prompt,
        prompt_latex=rf"{coef}\sin^2\theta + {coef}\cos^2\theta",
        answer_latex=ans_latex,
        answer_sympy=ans_latex,
        sample_answer=sample,
        marking_schema={
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": f"Factored out {coef}", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Applied sin^2(theta) + cos^2(theta) = 1 to get {ans_latex}", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "strict",
        },
        hints={
            "1_nudge": f"Notice that {coef} is a common factor.",
            "2_concept": "The fundamental Pythagorean identity states that $\\sin^2\\theta + \\cos^2\\theta = 1$ for all $\\theta$.",
            "3_breakdown": f"${coef}(\\sin^2\\theta + \\cos^2\\theta) = {coef}(1) = {coef}$.",
        },
        misconception_tags=["misapplied_pythagorean_identity"],
        keywords=["square identity", "Pythagorean identity", "factoring"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=2,
        mode="27_square_identity_pythagorean",
        difficulty="easy",
    )


# ---------------------------------------------------------------------------
# 28. Rearranged Square Identity (1 - sin²θ or 1 - cos²θ)
# ---------------------------------------------------------------------------
def build_28_square_identity_rearranged(r: random.Random) -> Dict[str, Any]:
    choice = r.choice(["sin_to_cos", "cos_to_sin"])
    if choice == "sin_to_cos":
        expr_latex = r"\frac{1 - \sin^2\theta}{\cos\theta}"
        ans_latex = r"\cos\theta"
        sample = (
            rf"\text{{Use rearranged square identity }} 1 - \sin^2\theta = \cos^2\theta:\\"
            rf"\frac{{\cos^2\theta}}{{\cos\theta}} = \cos\theta"
        )
    else:
        expr_latex = r"\frac{1 - \cos^2\theta}{\sin\theta}"
        ans_latex = r"\sin\theta"
        sample = (
            rf"\text{{Use rearranged square identity }} 1 - \cos^2\theta = \sin^2\theta:\\"
            rf"\frac{{\sin^2\theta}}{{\sin\theta}} = \sin\theta"
        )

    prompt = f"Simplify the trigonometric expression to a single ratio:\n\n$${expr_latex}$$"

    return make_math_question(
        prefix="trig_28",
        topic=TOPIC,
        subskill="28_square_identity_rearranged",
        learning_objective_id=f"{LO_PREFIX}_rearranged_square",
        prompt=prompt,
        prompt_latex=expr_latex,
        answer_latex=ans_latex,
        answer_sympy=ans_latex,
        sample_answer=sample,
        marking_schema={
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Substituted rearranged square identity in numerator", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Cancelled common factor to get {ans_latex}", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        hints={
            "1_nudge": "Rearrange $\\sin^2\\theta + \\cos^2\\theta = 1$ to replace the numerator.",
            "2_concept": "$1 - \\sin^2\\theta = \\cos^2\\theta$ and $1 - \\cos^2\\theta = \\sin^2\\theta$.",
            "3_breakdown": f"Divide the squared term by the denominator to get ${ans_latex}$.",
        },
        misconception_tags=["sign_error_square_rearrangement"],
        keywords=["square identity", "simplification", "Pythagorean"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=2,
        mode="28_square_identity_rearranged",
        difficulty="easy",
    )


# ---------------------------------------------------------------------------
# 29. Compound Algebraic Reduction Fraction
# ---------------------------------------------------------------------------
def build_29_compound_algebraic_reduction_fraction(r: random.Random) -> Dict[str, Any]:
    # Variants of multi-factor reduction fractions
    num_str = r"\sin(180^\circ - \theta) \cdot \cos(90^\circ - \theta)"
    den_str = r"\cos(360^\circ - \theta) \cdot \tan(180^\circ + \theta)"
    expr_str = rf"\frac{{{num_str}}}{{{den_str}}}"

    prompt = (
        f"Simplify the trigonometric expression to a single trigonometric ratio without using a calculator. "
        f"Show ALL reduction steps:\n\n$${expr_str}$$"
    )
    ans_latex = r"\sin\theta"
    sample = (
        rf"\text{{Reduce each factor:}}\\"
        rf"\sin(180^\circ - \theta) = \sin\theta\\"
        rf"\cos(90^\circ - \theta) = \sin\theta\\"
        rf"\cos(360^\circ - \theta) = \cos\theta\\"
        rf"\tan(180^\circ + \theta) = \tan\theta = \frac{{\sin\theta}}{{\cos\theta}}\\"
        rf"\text{{Substitute into the fraction:}}\\"
        rf"\frac{{\sin\theta \cdot \sin\theta}}{{\cos\theta \cdot \left(\frac{{\sin\theta}}{{\cos\theta}}\right)}} = \frac{{\sin^2\theta}}{{\sin\theta}} = \sin\theta"
    )

    return make_math_question(
        prefix="trig_29",
        topic=TOPIC,
        subskill="29_compound_algebraic_reduction_fraction",
        learning_objective_id=f"{LO_PREFIX}_compound_reduction",
        prompt=prompt,
        prompt_latex=expr_str,
        answer_latex=ans_latex,
        answer_sympy="sin(theta)",
        sample_answer=sample,
        marking_schema={
            "total_marks": 5,
            "marking_points": [
                {"id": "mp1", "desc": "sin(180 - theta) = sin(theta)", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "cos(90 - theta) = sin(theta)", "marks": 1, "editable": True},
                {"id": "mp3", "desc": "cos(360 - theta) = cos(theta)", "marks": 1, "editable": True},
                {"id": "mp4", "desc": "tan(180 + theta) = tan(theta) = sin/cos", "marks": 1, "editable": True},
                {"id": "mp5", "desc": "Final simplified ratio: sin(theta)", "marks": 1, "editable": True},
            ],
            "deductions": [{"rule": "sign_error_in_reduction", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
        hints={
            "1_nudge": "Apply the CAST diagram and co-ratio rules to each factor before combining.",
            "2_concept": "$\\cos(90^\\circ - \\theta) = \\sin\\theta$, $\\cos(360^\\circ - \\theta) = \\cos\\theta$, $\\tan(180^\\circ + \\theta) = \\frac{\\sin\\theta}{\\cos\\theta}$.",
            "3_breakdown": "Numerator = $\\sin^2\\theta$. Denominator = $\\cos\\theta \\cdot \\frac{\\sin\\theta}{\\cos\\theta} = \\sin\\theta$. Final result = $\\sin\\theta$.",
        },
        misconception_tags=["sign_error_in_reduction", "confused_co_ratio"],
        keywords=["reduction formula", "identities", "simplification"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=5,
        mode="29_compound_algebraic_reduction_fraction",
        difficulty="hard",
    )


# ---------------------------------------------------------------------------
# 30. Compound Reduction with Squared Factors
# ---------------------------------------------------------------------------
def build_30_compound_reduction_with_powers(r: random.Random) -> Dict[str, Any]:
    expr_str = r"\sin^2(180^\circ + \theta) + \cos^2(360^\circ - \theta) + \cos(180^\circ - \theta) \cdot \cos(-\theta)"
    ans_latex = r"1 - \cos^2\theta = \sin^2\theta"
    prompt = (
        f"Simplify the trigonometric expression fully:\n\n"
        f"$${expr_str}$$"
    )
    sample = (
        rf"\sin(180^\circ + \theta) = -\sin\theta \implies \sin^2(180^\circ + \theta) = (-\sin\theta)^2 = \sin^2\theta\\"
        rf"\cos(360^\circ - \theta) = \cos\theta \implies \cos^2(360^\circ - \theta) = \cos^2\theta\\"
        rf"\cos(180^\circ - \theta) = -\cos\theta \text{{ and }} \cos(-\theta) = \cos\theta\\"
        rf"\therefore \sin^2\theta + \cos^2\theta + (-\cos\theta)(\cos\theta) = 1 - \cos^2\theta = \sin^2\theta"
    )

    return make_math_question(
        prefix="trig_30",
        topic=TOPIC,
        subskill="30_compound_reduction_with_powers",
        learning_objective_id=f"{LO_PREFIX}_reduction_powers",
        prompt=prompt,
        prompt_latex=expr_str,
        answer_latex=r"\sin^2\theta",
        answer_sympy="sin(theta)**2",
        sample_answer=sample,
        marking_schema={
            "total_marks": 5,
            "marking_points": [
                {"id": "mp1", "desc": "sin^2(180 + theta) = sin^2(theta)", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "cos^2(360 - theta) = cos^2(theta)", "marks": 1, "editable": True},
                {"id": "mp3", "desc": "cos(180 - theta)cos(-theta) = -cos^2(theta)", "marks": 1, "editable": True},
                {"id": "mp4", "desc": "Applied sin^2(theta) + cos^2(theta) = 1", "marks": 1, "editable": True},
                {"id": "mp5", "desc": "Final simplified form: sin^2(theta)", "marks": 1, "editable": True},
            ],
            "deductions": [{"rule": "sign_error_squaring", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
        hints={
            "1_nudge": "Remember that $(-\\sin\\theta)^2 = +\\sin^2\\theta$.",
            "2_concept": "Square of a negative ratio is always positive. Then look for the Pythagorean identity.",
            "3_breakdown": "$\\sin^2\\theta + \\cos^2\\theta - \\cos^2\\theta = \\sin^2\\theta$.",
        },
        misconception_tags=["sign_error_squaring_negative", "forgot_pythagorean_identity"],
        keywords=["squared reduction", "Pythagorean identity", "simplification"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=5,
        mode="30_compound_reduction_with_powers",
        difficulty="hard",
    )


# ---------------------------------------------------------------------------
# 31. Proving Identity: Common Denominator
# ---------------------------------------------------------------------------
def build_31_prove_identity_single_fraction(r: random.Random) -> Dict[str, Any]:
    lhs_str = r"\frac{1}{\cos\theta} - \frac{\cos\theta}{1 + \sin\theta}"
    rhs_str = r"\tan\theta"
    prompt = (
        f"Prove the following trigonometric identity for all valid values of $\\theta$:\n\n"
        f"$${lhs_str} = {rhs_str}$$"
    )
    sample = (
        rf"\text{{LHS}} = \frac{{1(1 + \sin\theta) - \cos^2\theta}}{{\cos\theta(1 + \sin\theta)}}\\"
        rf"= \frac{{1 - \cos^2\theta + \sin\theta}}{{\cos\theta(1 + \sin\theta)}}\\"
        rf"= \frac{{\sin^2\theta + \sin\theta}}{{\cos\theta(1 + \sin\theta)}}\\"
        rf"= \frac{{\sin\theta(\sin\theta + 1)}}{{\cos\theta(1 + \sin\theta)}}\\"
        rf"= \frac{{\sin\theta}}{{\cos\theta}} = \tan\theta = \text{{RHS}}"
    )
    return make_math_question(
        prefix="trig_31",
        topic=TOPIC,
        subskill="31_prove_identity_single_fraction",
        learning_objective_id=f"{LO_PREFIX}_prove_identity_lcd",
        prompt=prompt,
        prompt_latex=rf"{lhs_str} = {rhs_str}",
        answer_latex=rhs_str,
        answer_sympy="tan(theta)",
        sample_answer=sample,
        marking_schema={
            "total_marks": 4,
            "marking_points": [
                {"id": "mp1", "desc": "Common denominator cos(theta)(1 + sin(theta))", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Applied 1 - cos^2(theta) = sin^2(theta)", "marks": 1, "editable": True},
                {"id": "mp3", "desc": "Factored numerator sin(theta)(sin(theta) + 1)", "marks": 1, "editable": True},
                {"id": "mp4", "desc": "Cancelled factor and concluded LHS = RHS", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        hints={
            "1_nudge": "Find a common denominator on the left-hand side.",
            "2_concept": "Common denominator is $\\cos\\theta(1 + \\sin\\theta)$. Then replace $1 - \\cos^2\\theta$ with $\\sin^2\\theta$.",
            "3_breakdown": "Numerator becomes $\\sin^2\\theta + \\sin\\theta = \\sin\\theta(1 + \\sin\\theta)$. Cancel $(1 + \\sin\\theta)$ to get $\\tan\\theta$.",
        },
        misconception_tags=["lcd_algebra_error", "cancelled_across_addition"],
        keywords=["prove identity", "common denominator", "factoring", "Pythagorean"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=6,
        mode="31_prove_identity_single_fraction",
        difficulty="hard",
    )


# ---------------------------------------------------------------------------
# 32. Proving Identity: Factoring Difference of Squares
# ---------------------------------------------------------------------------
def build_32_prove_identity_factoring(r: random.Random) -> Dict[str, Any]:
    lhs_str = r"\frac{\sin^4\theta - \cos^4\theta}{\sin^2\theta - \cos^2\theta}"
    rhs_str = "1"
    prompt = (
        f"Prove that the following identity holds true for all defined values of $\\theta$:\n\n"
        f"$${lhs_str} = {rhs_str}$$"
    )
    sample = (
        rf"\text{{LHS}} = \frac{{(\sin^2\theta - \cos^2\theta)(\sin^2\theta + \cos^2\theta)}}{{\sin^2\theta - \cos^2\theta}}\\"
        rf"= \sin^2\theta + \cos^2\theta\\"
        rf"= 1 = \text{{RHS}}"
    )
    return make_math_question(
        prefix="trig_32",
        topic=TOPIC,
        subskill="32_prove_identity_factoring",
        learning_objective_id=f"{LO_PREFIX}_prove_identity_diff_squares",
        prompt=prompt,
        prompt_latex=rf"{lhs_str} = {rhs_str}",
        answer_latex="1",
        answer_sympy="1",
        sample_answer=sample,
        marking_schema={
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": "Factored numerator as difference of two squares", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Cancelled (sin^2 - cos^2) factor", "marks": 1, "editable": True},
                {"id": "mp3", "desc": "Applied sin^2 + cos^2 = 1 to conclude", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        hints={
            "1_nudge": "Factor the numerator as a difference of two squares: $a^4 - b^4 = (a^2 - b^2)(a^2 + b^2)$.",
            "2_concept": "$\\sin^4\\theta - \\cos^4\\theta = (\\sin^2\\theta - \\cos^2\\theta)(\\sin^2\\theta + \\cos^2\\theta)$.",
            "3_breakdown": "Cancel $(\\sin^2\\theta - \\cos^2\\theta)$, leaving $\\sin^2\\theta + \\cos^2\\theta = 1$.",
        },
        misconception_tags=["factoring_difference_of_squares_error"],
        keywords=["prove identity", "difference of two squares", "factoring"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=4,
        mode="32_prove_identity_factoring",
        difficulty="medium",
    )


# ---------------------------------------------------------------------------
# 33. Undefined Values of a Trigonometric Identity
# ---------------------------------------------------------------------------
def build_33_prove_identity_undefined_values(r: random.Random) -> Dict[str, Any]:
    choice = r.choice(["tan", "cos_denom"])
    if choice == "tan":
        expr_latex = r"\tan\theta"
        ans_latex = r"\theta = 90^\circ + k \cdot 180^\circ, \; k \in \mathbb{Z}"
        sample = (
            rf"\tan\theta = \frac{{\sin\theta}}{{\cos\theta}} \text{{ is undefined when }}\cos\theta = 0.\\"
            rf"\therefore \theta = 90^\circ + k \cdot 180^\circ, \; k \in \mathbb{{Z}}"
        )
    else:
        expr_latex = r"\frac{1}{1 - \cos\theta}"
        ans_latex = r"\theta = k \cdot 360^\circ, \; k \in \mathbb{Z}"
        sample = (
            rf"\text{{The expression is undefined when the denominator is zero:}}\\"
            rf"1 - \cos\theta = 0 \implies \cos\theta = 1\\"
            rf"\therefore \theta = 0^\circ + k \cdot 360^\circ = k \cdot 360^\circ, \; k \in \mathbb{{Z}}"
        )

    prompt = (
        f"Determine the general condition for which the trigonometric expression is undefined:\n\n"
        f"$${expr_latex}$$"
    )

    return make_math_question(
        prefix="trig_33",
        topic=TOPIC,
        subskill="33_prove_identity_undefined_values",
        learning_objective_id=f"{LO_PREFIX}_undefined_values",
        prompt=prompt,
        prompt_latex=expr_latex,
        answer_latex=ans_latex,
        answer_sympy=ans_latex,
        sample_answer=sample,
        marking_schema={
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": "Set denominator equal to zero", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Identified base angle", "marks": 1, "editable": True},
                {"id": "mp3", "desc": "Correct general solution with k in Z", "marks": 1, "editable": True},
            ],
            "deductions": [{"rule": "omitted_k_in_Z", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
        hints={
            "1_nudge": "An expression is undefined when division by zero occurs.",
            "2_concept": "$\\tan\\theta$ is undefined where $\\cos\\theta = 0$, occurring at $90^\\circ$ and every $180^\\circ$ thereafter.",
            "3_breakdown": f"Condition: ${ans_latex}$.",
        },
        misconception_tags=["forgot_tan_undefined_asymptote", "omitted_k_in_Z"],
        keywords=["undefined values", "asymptotes", "restrictions", "general solution"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=3,
        mode="33_prove_identity_undefined_values",
        difficulty="medium",
    )


# ---------------------------------------------------------------------------
# 34. General Solution: sin θ = k (Basic)
# ---------------------------------------------------------------------------
def build_34_general_solution_sin_basic(r: random.Random) -> Dict[str, Any]:
    cases = [
        (r"\frac{1}{2}", 30, 150),
        (r"\frac{\sqrt{3}}{2}", 60, 120),
        (r"\frac{\sqrt{2}}{2}", 45, 135),
    ]
    val_str, ref, q2 = r.choice(cases)
    prompt = f"Determine the general solution of the trigonometric equation:\n\n$$\\sin\\theta = {val_str}$$"
    ans_latex = rf"\theta = {ref}^\circ + k \cdot 360^\circ \quad \text{{or}} \quad \theta = {q2}^\circ + k \cdot 360^\circ, \; k \in \mathbb{{Z}}"
    sample = (
        rf"\text{{Reference angle: }} \text{{ref}} = {ref}^\circ\\"
        rf"\text{{Quadrant 1: }} \theta = {ref}^\circ + k \cdot 360^\circ, \; k \in \mathbb{{Z}}\\"
        rf"\text{{Quadrant 2: }} \theta = 180^\circ - {ref}^\circ + k \cdot 360^\circ = {q2}^\circ + k \cdot 360^\circ, \; k \in \mathbb{{Z}}"
    )
    return make_math_question(
        prefix="trig_34",
        topic=TOPIC,
        subskill="34_general_solution_sin_basic",
        learning_objective_id=f"{LO_PREFIX}_gensol_sin",
        prompt=prompt,
        prompt_latex=rf"\sin\theta = {val_str}",
        answer_latex=ans_latex,
        answer_sympy=ans_latex,
        sample_answer=sample,
        marking_schema={
            "total_marks": 4,
            "marking_points": [
                {"id": "mp1", "desc": f"Correct reference angle {ref} deg", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Quadrant 1 solution with + k.360", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Quadrant 2 solution ({q2} deg) with + k.360", "marks": 1, "editable": True},
                {"id": "mp4", "desc": "Statement k in Z", "marks": 1, "editable": True},
            ],
            "deductions": [{"rule": "omitted_k_in_Z", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
        hints={
            "1_nudge": "Find the reference angle in Quadrant 1 using special angles.",
            "2_concept": "Sine is positive in Quadrants 1 and 2. Use period $k \\cdot 360^\\circ$ and state $k \\in \\mathbb{Z}$.",
            "3_breakdown": f"$\\theta = {ref}^\\circ + k \\cdot 360^\\circ$ or $\\theta = {q2}^\\circ + k \\cdot 360^\\circ$.",
        },
        misconception_tags=["omitted_second_branch", "used_180_period_for_sine", "omitted_k_in_Z"],
        keywords=["general solution", "sine equation", "periodicity"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=4,
        mode="34_general_solution_sin_basic",
        difficulty="medium",
    )


# ---------------------------------------------------------------------------
# 35. General Solution: cos θ = k (Basic)
# ---------------------------------------------------------------------------
def build_35_general_solution_cos_basic(r: random.Random) -> Dict[str, Any]:
    cases = [
        (r"\frac{1}{2}", 60),
        (r"\frac{\sqrt{3}}{2}", 30),
        (r"\frac{\sqrt{2}}{2}", 45),
    ]
    val_str, ref = r.choice(cases)
    prompt = f"Determine the general solution of the trigonometric equation:\n\n$$\\cos\\theta = {val_str}$$"
    ans_latex = rf"\theta = \pm {ref}^\circ + k \cdot 360^\circ, \; k \in \mathbb{{Z}}"
    sample = (
        rf"\text{{Reference angle: }} \text{{ref}} = {ref}^\circ\\"
        rf"\text{{Since cosine is positive in Q1 and Q4:}}\\"
        rf"\theta = \pm {ref}^\circ + k \cdot 360^\circ, \; k \in \mathbb{{Z}}"
    )
    return make_math_question(
        prefix="trig_35",
        topic=TOPIC,
        subskill="35_general_solution_cos_basic",
        learning_objective_id=f"{LO_PREFIX}_gensol_cos",
        prompt=prompt,
        prompt_latex=rf"\cos\theta = {val_str}",
        answer_latex=ans_latex,
        answer_sympy=ans_latex,
        sample_answer=sample,
        marking_schema={
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": f"Correct reference angle {ref} deg", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Correct plus-minus solution with + k.360", "marks": 1, "editable": True},
                {"id": "mp3", "desc": "Statement k in Z", "marks": 1, "editable": True},
            ],
            "deductions": [{"rule": "omitted_k_in_Z", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
        hints={
            "1_nudge": "Find the reference angle from special angles.",
            "2_concept": "For cosine, the general solution is simply $\\theta = \\pm \\text{ref} + k \\cdot 360^\\circ, \\; k \\in \\mathbb{Z}$.",
            "3_breakdown": f"$\\theta = \\pm {ref}^\\circ + k \\cdot 360^\\circ$.",
        },
        misconception_tags=["forgot_plus_minus_cos", "omitted_k_in_Z"],
        keywords=["general solution", "cosine equation", "periodicity"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=4,
        mode="35_general_solution_cos_basic",
        difficulty="medium",
    )


# ---------------------------------------------------------------------------
# 36. General Solution: tan θ = k (Basic)
# ---------------------------------------------------------------------------
def build_36_general_solution_tan_basic(r: random.Random) -> Dict[str, Any]:
    cases = [
        ("1", 45),
        (r"\sqrt{3}", 60),
        (r"\frac{1}{\sqrt{3}}", 30),
    ]
    val_str, ref = r.choice(cases)
    prompt = f"Determine the general solution of the trigonometric equation:\n\n$$\\tan\\theta = {val_str}$$"
    ans_latex = rf"\theta = {ref}^\circ + k \cdot 180^\circ, \; k \in \mathbb{{Z}}"
    sample = (
        rf"\text{{Reference angle: }} \text{{ref}} = {ref}^\circ\\"
        rf"\text{{Tangent has a period of }} 180^\circ:\\"
        rf"\theta = {ref}^\circ + k \cdot 180^\circ, \; k \in \mathbb{{Z}}"
    )
    return make_math_question(
        prefix="trig_36",
        topic=TOPIC,
        subskill="36_general_solution_tan_basic",
        learning_objective_id=f"{LO_PREFIX}_gensol_tan",
        prompt=prompt,
        prompt_latex=rf"\tan\theta = {val_str}",
        answer_latex=ans_latex,
        answer_sympy=ans_latex,
        sample_answer=sample,
        marking_schema={
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": f"Correct reference angle {ref} deg", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Period of k.180 for tangent", "marks": 1, "editable": True},
                {"id": "mp3", "desc": "Statement k in Z", "marks": 1, "editable": True},
            ],
            "deductions": [{"rule": "used_360_for_tan", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
        hints={
            "1_nudge": "Find the reference angle from special angles.",
            "2_concept": "Remember that tangent repeats every $180^\\circ$, not $360^\\circ$. Period is $k \\cdot 180^\\circ$.",
            "3_breakdown": f"$\\theta = {ref}^\\circ + k \\cdot 180^\\circ, \\; k \\in \\mathbb{{Z}}$.",
        },
        misconception_tags=["used_360_for_tan_period", "omitted_k_in_Z"],
        keywords=["general solution", "tangent equation", "periodicity 180"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=3,
        mode="36_general_solution_tan_basic",
        difficulty="medium",
    )


# ---------------------------------------------------------------------------
# 37. General Solution: Multiple Argument sin(kθ) or cos(kθ)
# ---------------------------------------------------------------------------
def build_37_general_solution_coefficient_argument(r: random.Random) -> Dict[str, Any]:
    k = r.choice([2, 3])
    fn = r.choice(["sin", "cos"])
    ref = 30 if fn == "sin" else 60
    val_str = r"\frac{1}{2}"
    prompt = f"Solve for the general solution of the equation:\n\n$$\\{fn}({k}\\theta) = {val_str}$$"

    if fn == "sin":
        q2 = 180 - ref
        div_ref = ref / k
        div_q2 = q2 / k
        div_p = 360 / k
        ans_latex = (
            rf"\theta = {div_ref:.0f}^\circ + k \cdot {div_p:.0f}^\circ \quad \text{{or}} \quad "
            rf"\theta = {div_q2:.0f}^\circ + k \cdot {div_p:.0f}^\circ, \; k \in \mathbb{{Z}}"
        )
        sample = (
            rf"{k}\theta = {ref}^\circ + k \cdot 360^\circ \implies \theta = {div_ref:.0f}^\circ + k \cdot {div_p:.0f}^\circ\\"
            rf"\text{{or }} {k}\theta = {q2}^\circ + k \cdot 360^\circ \implies \theta = {div_q2:.0f}^\circ + k \cdot {div_p:.0f}^\circ, \; k \in \mathbb{{Z}}"
        )
    else:
        div_ref = ref / k
        div_p = 360 / k
        ans_latex = rf"\theta = \pm {div_ref:.0f}^\circ + k \cdot {div_p:.0f}^\circ, \; k \in \mathbb{{Z}}"
        sample = (
            rf"{k}\theta = \pm {ref}^\circ + k \cdot 360^\circ\\"
            rf"\text{{Divide all terms by }}{k}:\\"
            rf"\theta = \pm {div_ref:.0f}^\circ + k \cdot {div_p:.0f}^\circ, \; k \in \mathbb{{Z}}"
        )

    return make_math_question(
        prefix="trig_37",
        topic=TOPIC,
        subskill="37_general_solution_coefficient_argument",
        learning_objective_id=f"{LO_PREFIX}_gensol_mult_angle",
        prompt=prompt,
        prompt_latex=rf"\{fn}({k}\theta) = {val_str}",
        answer_latex=ans_latex,
        answer_sympy=ans_latex,
        sample_answer=sample,
        marking_schema={
            "total_marks": 4,
            "marking_points": [
                {"id": "mp1", "desc": "Reference angle found for compound argument", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Set up equation before dividing by {k}", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Divided both the angle and the period by {k}", "marks": 1, "editable": True},
                {"id": "mp4", "desc": "Statement k in Z", "marks": 1, "editable": True},
            ],
            "deductions": [{"rule": "forgot_to_divide_period", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
        hints={
            "1_nudge": f"Write down the general solution for ${k}\\theta$ first, including $+ k \\cdot 360^\\circ$.",
            "2_concept": f"CRITICAL: Divide EVERYTHING (including the period $k \\cdot 360^\\circ$) by {k}.",
            "3_breakdown": f"Solution: ${ans_latex}$.",
        },
        misconception_tags=["forgot_to_divide_period_by_k"],
        keywords=["multiple angles", "general solution", "period adjustment"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=4,
        mode="37_general_solution_coefficient_argument",
        difficulty="hard",
    )


# ---------------------------------------------------------------------------
# 38. General Solution: sin θ = cos(θ + α) (Co-ratio Equation)
# ---------------------------------------------------------------------------
def build_38_general_solution_sin_equals_cos_coratio(r: random.Random) -> Dict[str, Any]:
    shift = r.choice([20, 30, 40])
    prompt = (
        f"Determine the general solution for the trigonometric equation using co-ratios:\n\n"
        f"$$\\sin\\theta = \\cos(\\theta + {shift}^\\circ)$$"
    )
    # sin(theta) = cos(90 - theta)
    # cos(90 - theta) = cos(theta + shift)
    # 90 - theta = +-(theta + shift) + k*360
    # Case 1: 90 - theta = theta + shift + k*360 => 2*theta = 90 - shift - k*360
    b1_deg = (90 - shift) / 2
    ans_latex = rf"\theta = {b1_deg:.0f}^\circ + k \cdot 180^\circ, \; k \in \mathbb{{Z}}"
    sample = (
        rf"\text{{Convert sine to cosine using co-ratio: }}\sin\theta = \cos(90^\circ - \theta)\\"
        rf"\cos(90^\circ - \theta) = \cos(\theta + {shift}^\circ)\\"
        rf"90^\circ - \theta = (\theta + {shift}^\circ) + k \cdot 360^\circ\\"
        rf"2\theta = {90 - shift}^\circ - k \cdot 360^\circ\\"
        rf"\theta = {b1_deg:.0f}^\circ + k \cdot 180^\circ, \; k \in \mathbb{{Z}}"
    )
    return make_math_question(
        prefix="trig_38",
        topic=TOPIC,
        subskill="38_general_solution_sin_equals_cos_coratio",
        learning_objective_id=f"{LO_PREFIX}_gensol_coratio_eq",
        prompt=prompt,
        prompt_latex=rf"\sin\theta = \cos(\theta + {shift}^\circ)",
        answer_latex=ans_latex,
        answer_sympy=ans_latex,
        sample_answer=sample,
        marking_schema={
            "total_marks": 4,
            "marking_points": [
                {"id": "mp1", "desc": "Converted sin(theta) to cos(90 - theta)", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Equated arguments with period k.360", "marks": 1, "editable": True},
                {"id": "mp3", "desc": "Solved for theta correctly", "marks": 1, "editable": True},
                {"id": "mp4", "desc": "Statement k in Z", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        hints={
            "1_nudge": "Change $\\sin\\theta$ to $\\cos(90^\\circ - \\theta)$ so both sides have the same trigonometric function.",
            "2_concept": "When $\\cos A = \\cos B$, then $A = \\pm B + k \\cdot 360^\\circ$.",
            "3_breakdown": f"Result: ${ans_latex}$.",
        },
        misconception_tags=["failed_to_apply_co_ratio_equation"],
        keywords=["co-ratios", "general solution", "equating trig arguments"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=5,
        mode="38_general_solution_sin_equals_cos_coratio",
        difficulty="hard",
    )


# ---------------------------------------------------------------------------
# 39. General Solution: a sin θ = b cos θ (Tangent Substitution)
# ---------------------------------------------------------------------------
def build_39_general_solution_sin_equals_cos_tan(r: random.Random) -> Dict[str, Any]:
    cases = [(1, 1, 45, r"\sin\theta = \cos\theta"), (1, r"\sqrt{3}", 60, r"\sin\theta = \sqrt{3}\cos\theta"), (r"\sqrt{3}", 1, 30, r"\sqrt{3}\sin\theta = \cos\theta")]
    c1, c2, ref, eq_latex = r.choice(cases)
    prompt = f"Solve for the general solution of the equation by dividing through by $\\cos\\theta$:\n\n$${eq_latex}$$"
    ans_latex = rf"\theta = {ref}^\circ + k \cdot 180^\circ, \; k \in \mathbb{{Z}}"
    sample = (
        rf"\text{{Divide both sides by }}\cos\theta \quad (\cos\theta \ne 0):\\"
        rf"\tan\theta = \frac{{\text{{coef}}_2}}{{\text{{coef}}_1}}\\"
        rf"\text{{Reference angle: }} \text{{ref}} = {ref}^\circ\\"
        rf"\theta = {ref}^\circ + k \cdot 180^\circ, \; k \in \mathbb{{Z}}"
    )
    return make_math_question(
        prefix="trig_39",
        topic=TOPIC,
        subskill="39_general_solution_sin_equals_cos_tan",
        learning_objective_id=f"{LO_PREFIX}_gensol_sin_cos_tan",
        prompt=prompt,
        prompt_latex=eq_latex,
        answer_latex=ans_latex,
        answer_sympy=ans_latex,
        sample_answer=sample,
        marking_schema={
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": "Divided by cos(theta) to obtain tan(theta)", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Correct reference angle {ref} deg", "marks": 1, "editable": True},
                {"id": "mp3", "desc": "Period k.180 and k in Z", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        hints={
            "1_nudge": "Divide both sides by $\\cos\\theta$ to create a $\\tan\\theta$ equation.",
            "2_concept": "$\\frac{\\sin\\theta}{\\cos\\theta} = \\tan\\theta$. Tangent has period $k \\cdot 180^\\circ$.",
            "3_breakdown": f"$\\theta = {ref}^\\circ + k \\cdot 180^\\circ, \\; k \\in \\mathbb{{Z}}$.",
        },
        misconception_tags=["divided_by_sin_inversion", "used_360_for_tan"],
        keywords=["tangent substitution", "general solution", "linear trig equation"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=3,
        mode="39_general_solution_sin_equals_cos_tan",
        difficulty="medium",
    )


# ---------------------------------------------------------------------------
# 40. General Solution by Factoring Common Factor
# ---------------------------------------------------------------------------
def build_40_general_solution_common_factor(r: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Determine the general solution of the equation by taking out a common factor:\n\n"
        f"$$2\\sin\\theta \\cos\\theta - \\sin\\theta = 0$$"
    )
    ans_latex = r"\theta = k \cdot 180^\circ \quad \text{or} \quad \theta = \pm 60^\circ + k \cdot 360^\circ, \; k \in \mathbb{Z}"
    sample = (
        rf"\sin\theta(2\cos\theta - 1) = 0\\"
        rf"\sin\theta = 0 \implies \theta = 0^\circ + k \cdot 180^\circ = k \cdot 180^\circ, \; k \in \mathbb{{Z}}\\"
        rf"\text{{or }} 2\cos\theta - 1 = 0 \implies \cos\theta = \frac{{1}}{{2}} \implies \theta = \pm 60^\circ + k \cdot 360^\circ, \; k \in \mathbb{{Z}}"
    )
    return make_math_question(
        prefix="trig_40",
        topic=TOPIC,
        subskill="40_general_solution_common_factor",
        learning_objective_id=f"{LO_PREFIX}_gensol_common_factor",
        prompt=prompt,
        prompt_latex=r"2\sin\theta\cos\theta - \sin\theta = 0",
        answer_latex=ans_latex,
        answer_sympy=ans_latex,
        sample_answer=sample,
        marking_schema={
            "total_marks": 5,
            "marking_points": [
                {"id": "mp1", "desc": "Factored out sin(theta)", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Branch 1: sin(theta) = 0 -> theta = k.180", "marks": 1, "editable": True},
                {"id": "mp3", "desc": "Branch 2: cos(theta) = 1/2", "marks": 1, "editable": True},
                {"id": "mp4", "desc": "Branch 2 solution: +-60 + k.360", "marks": 1, "editable": True},
                {"id": "mp5", "desc": "Statement k in Z", "marks": 1, "editable": True},
            ],
            "deductions": [{"rule": "divided_out_variable_factor", "penalty": -2}],
            "carry_forward_rule": "consequential_accuracy",
        },
        hints={
            "1_nudge": "DO NOT divide by $\\sin\\theta$! Take it out as a common factor instead.",
            "2_concept": "Dividing by $\\sin\\theta$ loses roots where $\\sin\\theta = 0$.",
            "3_breakdown": "Factoring gives $\\sin\\theta(2\\cos\\theta - 1) = 0$, leading to two branches.",
        },
        misconception_tags=["divided_by_variable_losing_roots", "omitted_k_in_Z"],
        keywords=["factoring", "common factor", "general solution", "two branches"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=5,
        mode="40_general_solution_common_factor",
        difficulty="hard",
    )


# ---------------------------------------------------------------------------
# 41. General Solution: Quadratic Trigonometric Equation
# ---------------------------------------------------------------------------
def build_41_general_solution_quadratic_trig(r: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Solve for the general solution of the quadratic trigonometric equation:\n\n"
        f"$$2\\sin^2\\theta + \\sin\\theta - 1 = 0$$"
    )
    ans_latex = r"\theta = 30^\circ + k \cdot 360^\circ, \; \theta = 150^\circ + k \cdot 360^\circ \quad \text{or} \quad \theta = 270^\circ + k \cdot 360^\circ, \; k \in \mathbb{Z}"
    sample = (
        rf"\text{{Factor as a quadratic in }}\sin\theta:\\"
        rf"(2\sin\theta - 1)(\sin\theta + 1) = 0\\"
        rf"\sin\theta = \frac{{1}}{{2}} \implies \theta = 30^\circ + k \cdot 360^\circ \text{{ or }} \theta = 150^\circ + k \cdot 360^\circ\\"
        rf"\sin\theta = -1 \implies \theta = 270^\circ + k \cdot 360^\circ, \; k \in \mathbb{{Z}}"
    )
    return make_math_question(
        prefix="trig_41",
        topic=TOPIC,
        subskill="41_general_solution_quadratic_trig",
        learning_objective_id=f"{LO_PREFIX}_gensol_quadratic",
        prompt=prompt,
        prompt_latex=r"2\sin^2\theta + \sin\theta - 1 = 0",
        answer_latex=ans_latex,
        answer_sympy=ans_latex,
        sample_answer=sample,
        marking_schema={
            "total_marks": 5,
            "marking_points": [
                {"id": "mp1", "desc": "Factored quadratic into (2sin - 1)(sin + 1) = 0", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Both factors equated to zero (sin = 1/2 and sin = -1)", "marks": 1, "editable": True},
                {"id": "mp3", "desc": "Solutions for sin(theta) = 1/2", "marks": 1, "editable": True},
                {"id": "mp4", "desc": "Solution for sin(theta) = -1", "marks": 1, "editable": True},
                {"id": "mp5", "desc": "Statement k in Z", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        hints={
            "1_nudge": "Let $u = \\sin\\theta$ and factor $2u^2 + u - 1 = 0$.",
            "2_concept": "Factors are $(2\\sin\\theta - 1)(\\sin\\theta + 1) = 0$.",
            "3_breakdown": "Solve both linear equations for general solutions.",
        },
        misconception_tags=["quadratic_factoring_error", "omitted_k_in_Z"],
        keywords=["quadratic trig equation", "factoring", "general solution"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=6,
        mode="41_general_solution_quadratic_trig",
        difficulty="hard",
    )


# ---------------------------------------------------------------------------
# 42. Specific Interval Solution: Sine
# ---------------------------------------------------------------------------
def build_42_specific_interval_solution_sin(r: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Determine all values of $\\theta$ in the interval $\\theta \\in [0^\\circ; 360^\\circ]$ that satisfy:\n\n"
        f"$$\\sin\\theta = \\frac{1}{2}$$"
    )
    ans_latex = r"\theta \in \{30^\circ; 150^\circ\}"
    sample = (
        r"\text{Reference angle: } 30^\circ\\"
        r"\text{Sine is positive in Quadrants 1 and 2:}\\"
        r"\text{Quadrant 1: } \theta = 30^\circ\\"
        r"\text{Quadrant 2: } \theta = 180^\circ - 30^\circ = 150^\circ\\"
        r"\therefore \theta \in \{30^\circ; 150^\circ\}"
    )
    return make_math_question(
        prefix="trig_42",
        topic=TOPIC,
        subskill="42_specific_interval_solution_sin",
        learning_objective_id=f"{LO_PREFIX}_interval_sin",
        prompt=prompt,
        prompt_latex=r"\sin\theta = \frac{1}{2}, \; \theta \in [0^\circ; 360^\circ]",
        answer_latex=ans_latex,
        answer_sympy="30, 150",
        sample_answer=sample,
        marking_schema={
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": "Reference angle 30 deg", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Correct Quadrant 1 value (30 deg)", "marks": 1, "editable": True},
                {"id": "mp3", "desc": "Correct Quadrant 2 value (150 deg)", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        hints={
            "1_nudge": "Find the reference angle and identify which quadrants sine is positive in.",
            "2_concept": "Within $[0^\\circ; 360^\\circ]$, $\\sin\\theta > 0$ in Q1 and Q2 only.",
            "3_breakdown": "Solutions are $30^\\circ$ and $180^\\circ - 30^\\circ = 150^\\circ$.",
        },
        misconception_tags=["included_solutions_outside_interval"],
        keywords=["specific interval", "sine equation", "domain restrictions"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=3,
        mode="42_specific_interval_solution_sin",
        difficulty="medium",
    )


# ---------------------------------------------------------------------------
# 43. Specific Interval Solution: Cosine
# ---------------------------------------------------------------------------
def build_43_specific_interval_solution_cos(r: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Find all solutions for $\\theta \\in [-180^\\circ; 180^\\circ]$ satisfying:\n\n"
        f"$$\\cos\\theta = -\\frac{1}{2}$$"
    )
    ans_latex = r"\theta \in \{-120^\circ; 120^\circ\}"
    sample = (
        r"\text{Reference angle: } \text{ref} = 60^\circ\\"
        r"\text{Cosine is negative in Quadrants 2 and 3:}\\"
        r"\text{Quadrant 2: } \theta = 180^\circ - 60^\circ = 120^\circ\\"
        r"\text{Quadrant 3 (in range } [-180^\circ; 180^\circ]\text{): } \theta = -180^\circ + 60^\circ = -120^\circ\\"
        r"\therefore \theta \in \{-120^\circ; 120^\circ\}"
    )
    return make_math_question(
        prefix="trig_43",
        topic=TOPIC,
        subskill="43_specific_interval_solution_cos",
        learning_objective_id=f"{LO_PREFIX}_interval_cos",
        prompt=prompt,
        prompt_latex=r"\cos\theta = -\frac{1}{2}, \; \theta \in [-180^\circ; 180^\circ]",
        answer_latex=ans_latex,
        answer_sympy="-120, 120",
        sample_answer=sample,
        marking_schema={
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": "Reference angle 60 deg", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Positive solution 120 deg", "marks": 1, "editable": True},
                {"id": "mp3", "desc": "Negative solution -120 deg within interval", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        hints={
            "1_nudge": "Find the reference angle from $\\cos(\\text{ref}) = \\frac{1}{2}$.",
            "2_concept": "Cosine is negative in Q2 and Q3. Convert angles to the range $[-180^\\circ; 180^\\circ]$.",
            "3_breakdown": "Solutions are $120^\\circ$ and $-120^\\circ$.",
        },
        misconception_tags=["negative_angle_interval_error"],
        keywords=["specific interval", "cosine equation", "negative range"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=4,
        mode="43_specific_interval_solution_cos",
        difficulty="medium",
    )


# ---------------------------------------------------------------------------
# 44. Specific Interval Solution: Quadratic Trig
# ---------------------------------------------------------------------------
def build_44_specific_interval_solution_quadratic(r: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Solve for $\\theta \\in [0^\\circ; 360^\\circ]$:\n\n"
        f"$$2\\cos^2\\theta - \\cos\\theta = 0$$"
    )
    ans_latex = r"\theta \in \{60^\circ; 90^\circ; 270^\circ; 300^\circ\}"
    sample = (
        r"\cos\theta(2\cos\theta - 1) = 0\\"
        r"\cos\theta = 0 \implies \theta = 90^\circ, 270^\circ\\"
        r"\cos\theta = \frac{1}{2} \implies \theta = 60^\circ, 300^\circ\\"
        r"\therefore \theta \in \{60^\circ; 90^\circ; 270^\circ; 300^\circ\}"
    )
    return make_math_question(
        prefix="trig_44",
        topic=TOPIC,
        subskill="44_specific_interval_solution_quadratic",
        learning_objective_id=f"{LO_PREFIX}_interval_quad",
        prompt=prompt,
        prompt_latex=r"2\cos^2\theta - \\cos\theta = 0",
        answer_latex=ans_latex,
        answer_sympy="60, 90, 270, 300",
        sample_answer=sample,
        marking_schema={
            "total_marks": 4,
            "marking_points": [
                {"id": "mp1", "desc": "Factored out cos(theta)", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Solutions for cos(theta) = 0 (90, 270)", "marks": 1, "editable": True},
                {"id": "mp3", "desc": "Solutions for cos(theta) = 1/2 (60, 300)", "marks": 1, "editable": True},
                {"id": "mp4", "desc": "Full set of 4 angles listed", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        hints={
            "1_nudge": "Factor out $\\cos\\theta$.",
            "2_concept": "Each factor yields roots in the interval $[0^\\circ; 360^\\circ]$.",
            "3_breakdown": "$\\theta = 60^\\circ, 90^\\circ, 270^\\circ, 300^\\circ$.",
        },
        misconception_tags=["omitted_roots_in_interval"],
        keywords=["specific interval", "quadratic equation", "factoring"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=4,
        mode="44_specific_interval_solution_quadratic",
        difficulty="hard",
    )


# ---------------------------------------------------------------------------
# 45. Area Rule: Direct Calculation (with inline_svg)
# ---------------------------------------------------------------------------
def build_45_area_rule_direct_calculation(r: random.Random) -> Dict[str, Any]:
    a = r.randint(6, 14)
    b = r.randint(7, 16)
    c_side = math.sqrt(a*a + b*b - 2*a*b*math.cos(math.radians(50)))
    angle_c = r.choice([30, 45, 60])

    sin_c = math.sin(math.radians(angle_c))
    area_val = 0.5 * a * b * sin_c
    area_str = num(round(area_val, 2))

    d_spec = _triangle_svg(
        side_a=float(a),
        side_b=float(b),
        side_c=c_side,
        angle_c_deg=float(angle_c),
        label_a=f"a = {a}",
        label_b=f"b = {b}",
        angle_label=rf"{angle_c}^\circ",
    )

    prompt = (
        f"In $\\triangle ABC$ shown in the diagram, side $a = {a}\\text{{ cm}}$, side $b = {b}\\text{{ cm}}$, "
        f"and $\\hat{{C}} = {angle_c}^\\circ$.\n\n"
        f"Calculate the area of $\\triangle ABC$. Round your answer to two decimal places where necessary."
    )
    sample = (
        rf"\text{{Area}} = \frac{{1}}{{2}}ab \sin C\\"
        rf"= \frac{{1}}{{2}}({a})({b}) \sin({angle_c}^\circ)\\"
        rf"= {0.5 * a * b:.1f} \times \sin({angle_c}^\circ) \approx {area_str}\text{{ cm}}^2"
    )

    return make_math_question(
        prefix="trig_45",
        topic=TOPIC,
        subskill="45_area_rule_direct_calculation",
        learning_objective_id=f"{LO_PREFIX}_area_rule",
        prompt=prompt,
        prompt_latex=rf"\text{{Area of }} \triangle ABC, \; a = {a}, \; b = {b}, \; \hat{{C}} = {angle_c}^\circ",
        answer_latex=rf"{area_str}\text{{ cm}}^2",
        answer_sympy=f"{area_val:.2f}",
        sample_answer=sample,
        marking_schema={
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": "Correct Area rule formula: (1/2)ab sin C", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Correct substitution of values", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Correct calculated area: {area_str} cm^2", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        hints={
            "1_nudge": "Use the Area Rule: $\\text{Area} = \\frac{1}{2}ab \\sin C$.",
            "2_concept": "The angle used in the Area rule must be the included angle between the two given sides.",
            "3_breakdown": f"$\\text{{Area}} = \\frac{{1}}{{2}}({a})({b}) \\sin {angle_c}^\\circ = {area_str}\\text{{ cm}}^2$.",
        },
        misconception_tags=["wrong_area_formula", "wrong_included_angle"],
        keywords=["area rule", "2D triangle", "trigonometry"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=3,
        mode="45_area_rule_direct_calculation",
        difficulty="medium",
        diagram_spec=d_spec,
    )


# ---------------------------------------------------------------------------
# 46. Area Rule: Find Included Angle (with inline_svg)
# ---------------------------------------------------------------------------
def build_46_area_rule_find_included_angle(r: random.Random) -> Dict[str, Any]:
    a = r.randint(8, 14)
    b = r.randint(10, 16)
    angle_c = r.choice([30, 45, 60])
    c_side = math.sqrt(a*a + b*b - 2*a*b*math.cos(math.radians(angle_c)))
    area_val = 0.5 * a * b * math.sin(math.radians(angle_c))
    area_str = num(round(area_val, 2))

    d_spec = _triangle_svg(
        side_a=float(a),
        side_b=float(b),
        side_c=c_side,
        angle_c_deg=float(angle_c),
        label_a=f"a = {a}",
        label_b=f"b = {b}",
        angle_label=r"\hat{C}",
    )

    prompt = (
        f"In $\\triangle ABC$ shown in the diagram, side $a = {a}\\text{{ cm}}$, side $b = {b}\\text{{ cm}}$, "
        f"and the area of the triangle is ${area_str}\\text{{ cm}}^2$.\n\n"
        f"Given that $\\hat{{C}}$ is an acute angle, calculate the magnitude of $\\hat{{C}}$."
    )
    sample = (
        rf"\text{{Area}} = \frac{{1}}{{2}}ab \sin C\\"
        rf"{area_str} = \frac{{1}}{{2}}({a})({b}) \sin C = {0.5 * a * b:.1f} \sin C\\"
        rf"\sin C = \frac{{{area_str}}}{{{0.5 * a * b:.1f}}} = {math.sin(math.radians(angle_c)):.3f}\\"
        rf"\therefore \hat{{C}} = {angle_c}^\circ"
    )

    return make_math_question(
        prefix="trig_46",
        topic=TOPIC,
        subskill="46_area_rule_find_included_angle",
        learning_objective_id=f"{LO_PREFIX}_area_find_angle",
        prompt=prompt,
        prompt_latex=rf"\text{{Area}} = {area_str}, \; a = {a}, \; b = {b}",
        answer_latex=rf"{angle_c}^\circ",
        answer_sympy=str(angle_c),
        sample_answer=sample,
        marking_schema={
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": "Correct substitution into Area formula", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Solved for sin C", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Correct acute angle: {angle_c} deg", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        hints={
            "1_nudge": "Substitute the given area and sides into $\\text{Area} = \\frac{1}{2}ab \\sin C$.",
            "2_concept": "Rearrange to make $\\sin C$ the subject, then apply $\\arcsin$.",
            "3_breakdown": f"$\\sin C = \\frac{{{area_str}}}{{{0.5 * a * b:.1f}}}$, giving $\\hat{{C}} = {angle_c}^\\circ$.",
        },
        misconception_tags=["inverted_area_equation"],
        keywords=["area rule", "included angle", "inverse sine"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=3,
        mode="46_area_rule_find_included_angle",
        difficulty="medium",
        diagram_spec=d_spec,
    )


# ---------------------------------------------------------------------------
# 47. Sine Rule: Calculate Side Length (with inline_svg)
# ---------------------------------------------------------------------------
def build_47_sine_rule_calculate_side(r: random.Random) -> Dict[str, Any]:
    angle_a = r.choice([40, 50, 65])
    angle_b = r.choice([45, 60, 70])
    side_b = r.randint(10, 20)

    # a / sin A = b / sin B => a = b * sin A / sin B
    side_a = side_b * math.sin(math.radians(angle_a)) / math.sin(math.radians(angle_b))
    side_a_str = num(round(side_a, 2))
    angle_c = 180 - angle_a - angle_b
    side_c = side_b * math.sin(math.radians(angle_c)) / math.sin(math.radians(angle_b))

    d_spec = _triangle_svg(
        side_a=side_a,
        side_b=float(side_b),
        side_c=side_c,
        angle_c_deg=float(angle_c),
        label_a="a = ?",
        label_b=f"b = {side_b}",
        angle_label=rf"{angle_c}^\circ",
    )

    prompt = (
        f"In $\\triangle ABC$ shown in the diagram, $\\hat{{A}} = {angle_a}^\\circ$, "
        f"$\\hat{{B}} = {angle_b}^\\circ$, and side $b = {side_b}\\text{{ cm}}$.\n\n"
        f"Calculate the length of side $a$ using the Sine Rule. Round your answer to two decimal places."
    )
    sample = (
        rf"\frac{{a}}{{\sin A}} = \frac{{b}}{{\sin B}}\\"
        rf"\frac{{a}}{{\sin({angle_a}^\circ)}} = \frac{{{side_b}}}{{\sin({angle_b}^\circ)}}\\"
        rf"a = \frac{{{side_b} \times \sin({angle_a}^\circ)}}{{\sin({angle_b}^\circ)}} \approx {side_a_str}\text{{ cm}}"
    )

    return make_math_question(
        prefix="trig_47",
        topic=TOPIC,
        subskill="47_sine_rule_calculate_side",
        learning_objective_id=f"{LO_PREFIX}_sine_rule_side",
        prompt=prompt,
        prompt_latex=rf"\hat{{A}} = {angle_a}^\circ, \; \hat{{B}} = {angle_b}^\circ, \; b = {side_b}",
        answer_latex=rf"{side_a_str}\text{{ cm}}",
        answer_sympy=f"{side_a:.2f}",
        sample_answer=sample,
        marking_schema={
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": "Correct Sine Rule formula applied", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Correct substitution of values", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Correct calculated length: {side_a_str} cm", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        hints={
            "1_nudge": "Use the Sine Rule: $\\frac{a}{\\sin A} = \\frac{b}{\\sin B}$.",
            "2_concept": "Cross-multiply to isolate side $a = \\frac{b \\sin A}{\\sin B}$.",
            "3_breakdown": f"$a = \\frac{{{side_b} \\sin({angle_a}^\\circ)}}{{\\sin({angle_b}^\\circ)}} = {side_a_str}\\text{{ cm}}$.",
        },
        misconception_tags=["inverted_sine_rule", "paired_wrong_side_and_angle"],
        keywords=["sine rule", "side calculation", "2D triangles"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=3,
        mode="47_sine_rule_calculate_side",
        difficulty="medium",
        diagram_spec=d_spec,
    )


# ---------------------------------------------------------------------------
# 48. Sine Rule: Calculate Angle (with inline_svg)
# ---------------------------------------------------------------------------
def build_48_sine_rule_calculate_angle(r: random.Random) -> Dict[str, Any]:
    angle_b = r.choice([35, 42, 50])
    side_b = r.randint(12, 18)
    side_a = r.randint(8, side_b - 1)  # ensure side_a < side_b so angle_a is unambiguously acute

    sin_a = (side_a * math.sin(math.radians(angle_b))) / side_b
    angle_a = math.degrees(math.asin(sin_a))
    angle_a_str = num(round(angle_a, 1))

    angle_c = 180 - angle_a - angle_b
    side_c = math.sqrt(side_a**2 + side_b**2 - 2*side_a*side_b*math.cos(math.radians(angle_c)))

    d_spec = _triangle_svg(
        side_a=float(side_a),
        side_b=float(side_b),
        side_c=side_c,
        angle_c_deg=angle_c,
        label_a=f"a = {side_a}",
        label_b=f"b = {side_b}",
        angle_label=r"\hat{C}",
    )

    prompt = (
        f"In $\\triangle ABC$ shown in the diagram, side $a = {side_a}\\text{{ cm}}$, "
        f"side $b = {side_b}\\text{{ cm}}$, and $\\hat{{B}} = {angle_b}^\\circ$.\n\n"
        f"Calculate the size of acute angle $\\hat{{A}}$ using the Sine Rule. "
        f"Round your answer to one decimal place."
    )
    sample = (
        rf"\frac{{\sin A}}{{a}} = \frac{{\sin B}}{{b}}\\"
        rf"\frac{{\sin A}}{{{side_a}}} = \frac{{\sin({angle_b}^\circ)}}{{{side_b}}}\\"
        rf"\sin A = \frac{{{side_a} \times \sin({angle_b}^\circ)}}{{{side_b}}} = {sin_a:.4f}\\"
        rf"\hat{{A}} = \arcsin({sin_a:.4f}) \approx {angle_a_str}^\circ"
    )

    return make_math_question(
        prefix="trig_48",
        topic=TOPIC,
        subskill="48_sine_rule_calculate_angle",
        learning_objective_id=f"{LO_PREFIX}_sine_rule_angle",
        prompt=prompt,
        prompt_latex=rf"a = {side_a}, \; b = {side_b}, \; \hat{{B}} = {angle_b}^\circ",
        answer_latex=rf"{angle_a_str}^\circ",
        answer_sympy=f"{angle_a:.1f}",
        sample_answer=sample,
        marking_schema={
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": "Correct Sine Rule setup for angle", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Correct calculation of sin A", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Correct acute angle: {angle_a_str} deg", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        hints={
            "1_nudge": "Use the Sine Rule with angles on top: $\\frac{\\sin A}{a} = \\frac{\\sin B}{b}$.",
            "2_concept": "Solve for $\\sin A = \\frac{a \\sin B}{b}$, then take $\\arcsin$.",
            "3_breakdown": f"$\\hat{{A}} = \\arcsin\\left(\\frac{{{side_a} \\sin({angle_b}^\\circ)}}{{{side_b}}}\\right) = {angle_a_str}^\\circ$.",
        },
        misconception_tags=["inverted_sine_rule_angle"],
        keywords=["sine rule", "angle calculation", "2D triangles"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=3,
        mode="48_sine_rule_calculate_angle",
        difficulty="medium",
        diagram_spec=d_spec,
    )


# ---------------------------------------------------------------------------
# 49. Cosine Rule: Calculate Side Length (with inline_svg)
# ---------------------------------------------------------------------------
def build_49_cosine_rule_calculate_side(r: random.Random) -> Dict[str, Any]:
    b = r.randint(6, 12)
    c = r.randint(7, 14)
    angle_a = r.choice([38, 52, 65, 80, 105])

    # a^2 = b^2 + c^2 - 2bc cos A
    a_sq = b*b + c*c - 2*b*c*math.cos(math.radians(angle_a))
    a_val = math.sqrt(a_sq)
    a_str = num(round(a_val, 2))

    d_spec = _triangle_svg(
        side_a=a_val,
        side_b=float(b),
        side_c=float(c),
        angle_c_deg=float(angle_a),
        label_a="a = ?",
        label_b=f"b = {b}",
        label_c=f"c = {c}",
        angle_label=rf"{angle_a}^\circ",
    )

    prompt = (
        f"In $\\triangle ABC$ shown in the diagram, side $b = {b}\\text{{ cm}}$, "
        f"side $c = {c}\\text{{ cm}}$, and $\\hat{{A}} = {angle_a}^\\circ$.\n\n"
        f"Calculate the length of side $a$ using the Cosine Rule. Round your answer to two decimal places."
    )
    sample = (
        rf"a^2 = b^2 + c^2 - 2bc \cos A\\"
        rf"a^2 = ({b})^2 + ({c})^2 - 2({b})({c}) \cos({angle_a}^\circ)\\"
        rf"a^2 = {b*b} + {c*c} - {2*b*c} \cos({angle_a}^\circ) = {a_sq:.2f}\\"
        rf"a = \sqrt{{{a_sq:.2f}}} \approx {a_str}\text{{ cm}}"
    )

    return make_math_question(
        prefix="trig_49",
        topic=TOPIC,
        subskill="49_cosine_rule_calculate_side",
        learning_objective_id=f"{LO_PREFIX}_cosine_rule_side",
        prompt=prompt,
        prompt_latex=rf"b = {b}, \; c = {c}, \; \hat{{A}} = {angle_a}^\circ",
        answer_latex=rf"{a_str}\text{{ cm}}",
        answer_sympy=f"{a_val:.2f}",
        sample_answer=sample,
        marking_schema={
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": "Correct Cosine Rule formula setup", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Correct substitution into formula", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Correct calculated length: {a_str} cm", "marks": 1, "editable": True},
            ],
            "deductions": [{"rule": "order_of_operations_error", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
        hints={
            "1_nudge": "Apply the Cosine Rule for an unknown opposite side: $a^2 = b^2 + c^2 - 2bc \\cos A$.",
            "2_concept": "Beware of order of operations: compute $b^2 + c^2$ and $2bc \\cos A$ before subtracting.",
            "3_breakdown": f"$a = \\sqrt{{{b}^2 + {c}^2 - 2({b})({c})\\cos({angle_a}^\\circ)}} = {a_str}\\text{{ cm}}$.",
        },
        misconception_tags=["order_of_operations_in_cosine_rule"],
        keywords=["cosine rule", "side calculation", "2D triangles"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=4,
        mode="49_cosine_rule_calculate_side",
        difficulty="medium",
        diagram_spec=d_spec,
    )


# ---------------------------------------------------------------------------
# 50. Cosine Rule: Calculate Angle (with inline_svg)
# ---------------------------------------------------------------------------
def build_50_cosine_rule_calculate_angle(r: random.Random) -> Dict[str, Any]:
    # Form valid triangle sides
    a = r.randint(7, 12)
    b = r.randint(8, 14)
    c = r.randint(max(a - b + 2, 6), a + b - 2)

    # cos A = (b^2 + c^2 - a^2) / (2bc)
    num_val = b*b + c*c - a*a
    den_val = 2*b*c
    cos_a = num_val / den_val
    angle_a = math.degrees(math.acos(cos_a))
    angle_a_str = num(round(angle_a, 1))

    d_spec = _triangle_svg(
        side_a=float(a),
        side_b=float(b),
        side_c=float(c),
        angle_c_deg=angle_a,
        label_a=f"a = {a}",
        label_b=f"b = {b}",
        label_c=f"c = {c}",
        angle_label=r"\hat{A}",
    )

    prompt = (
        f"In $\\triangle ABC$ shown in the diagram, side lengths are $a = {a}\\text{{ cm}}$, "
        f"side $b = {b}\\text{{ cm}}$, and side $c = {c}\\text{{ cm}}$.\n\n"
        f"Calculate the size of angle $\\hat{{A}}$ using the Cosine Rule. Round your answer to one decimal place."
    )
    sample = (
        rf"\cos A = \frac{{b^2 + c^2 - a^2}}{{2bc}}\\"
        rf"\cos A = \frac{{({b})^2 + ({c})^2 - ({a})^2}}{{2({b})({c})}}\\"
        rf"\cos A = \frac{{{b*b} + {c*c} - {a*a}}}{{{2*b*c}}} = \frac{{{num_val}}}{{{den_val}}} = {cos_a:.4f}\\"
        rf"\hat{{A}} = \arccos({cos_a:.4f}) \approx {angle_a_str}^\circ"
    )

    return make_math_question(
        prefix="trig_50",
        topic=TOPIC,
        subskill="50_cosine_rule_calculate_angle",
        learning_objective_id=f"{LO_PREFIX}_cosine_rule_angle",
        prompt=prompt,
        prompt_latex=rf"a = {a}, \; b = {b}, \; c = {c}",
        answer_latex=rf"{angle_a_str}^\circ",
        answer_sympy=f"{angle_a:.1f}",
        sample_answer=sample,
        marking_schema={
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": "Correct Cosine Rule formula rearranged for cos A", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Correct substitution of side lengths", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Correct calculated angle: {angle_a_str} deg", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        hints={
            "1_nudge": "Rearrange the Cosine Rule to solve for $\\cos A$: $\\cos A = \\frac{b^2 + c^2 - a^2}{2bc}$.",
            "2_concept": "The subtracted squared side must be the side opposite angle $A$ (side $a$).",
            "3_breakdown": f"$\\cos A = \\frac{{{b}^2 + {c}^2 - {a}^2}}{{2({b})({c})}} = {cos_a:.4f}$, giving $\\hat{{A}} = {angle_a_str}^\\circ$.",
        },
        misconception_tags=["subtracted_wrong_side_in_cosine_angle"],
        keywords=["cosine rule", "angle calculation", "2D triangles"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=4,
        mode="50_cosine_rule_calculate_angle",
        difficulty="medium",
        diagram_spec=d_spec,
    )


# ---------------------------------------------------------------------------
# Registry Map of Archetypes 26–50
# ---------------------------------------------------------------------------
ARCHETYPES_26_50 = {
    "26_quotient_identity_substitution": build_26_quotient_identity_substitution,
    "27_square_identity_pythagorean": build_27_square_identity_pythagorean,
    "28_square_identity_rearranged": build_28_square_identity_rearranged,
    "29_compound_algebraic_reduction_fraction": build_29_compound_algebraic_reduction_fraction,
    "30_compound_reduction_with_powers": build_30_compound_reduction_with_powers,
    "31_prove_identity_single_fraction": build_31_prove_identity_single_fraction,
    "32_prove_identity_factoring": build_32_prove_identity_factoring,
    "33_prove_identity_undefined_values": build_33_prove_identity_undefined_values,
    "34_general_solution_sin_basic": build_34_general_solution_sin_basic,
    "35_general_solution_cos_basic": build_35_general_solution_cos_basic,
    "36_general_solution_tan_basic": build_36_general_solution_tan_basic,
    "37_general_solution_coefficient_argument": build_37_general_solution_coefficient_argument,
    "38_general_solution_sin_equals_cos_coratio": build_38_general_solution_sin_equals_cos_coratio,
    "39_general_solution_sin_equals_cos_tan": build_39_general_solution_sin_equals_cos_tan,
    "40_general_solution_common_factor": build_40_general_solution_common_factor,
    "41_general_solution_quadratic_trig": build_41_general_solution_quadratic_trig,
    "42_specific_interval_solution_sin": build_42_specific_interval_solution_sin,
    "43_specific_interval_solution_cos": build_43_specific_interval_solution_cos,
    "44_specific_interval_solution_quadratic": build_44_specific_interval_solution_quadratic,
    "45_area_rule_direct_calculation": build_45_area_rule_direct_calculation,
    "46_area_rule_find_included_angle": build_46_area_rule_find_included_angle,
    "47_sine_rule_calculate_side": build_47_sine_rule_calculate_side,
    "48_sine_rule_calculate_angle": build_48_sine_rule_calculate_angle,
    "49_cosine_rule_calculate_side": build_49_cosine_rule_calculate_side,
    "50_cosine_rule_calculate_angle": build_50_cosine_rule_calculate_angle,
}
