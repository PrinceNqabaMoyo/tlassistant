"""Grade 11 Mathematics — Trigonometry Archetypes 01–25.
Grounded in South African National Curriculum Standards for Grade 11 Mathematics.
Covers:
- Signs and CAST quadrant identification
- Reduction formulas: 180° ± θ, 360° - θ, negative angles, 90° ± θ (co-ratios)
- Angles > 360°
- Special angles (0°, 30°, 45°, 60°, 90°, 180°, 270°, 360°) exact values
- Numerical reductions without a calculator
- Cartesian plane terminal arms and right-angled triangle definitions (r = sqrt(x^2+y^2)) with inline_svg diagrams
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


def _cartesian_terminal_svg(x: int, y: int, pt_label: str = "P", angle_label: str = r"\theta") -> Dict[str, Any]:
    """Generates an inline SVG showing Cartesian plane with terminal arm to point (x, y)."""
    # SVG canvas 400x320, origin at (200, 160)
    ox, oy = 200, 160
    scale = 14
    px = ox + x * scale
    py = oy - y * scale

    # Angle arc
    angle_rad = math.atan2(y, x)
    if angle_rad < 0:
        angle_rad += 2 * math.pi
    angle_deg = math.degrees(angle_rad)

    # Arc path from positive x-axis
    r_arc = 28
    arc_ex = ox + r_arc * math.cos(math.radians(min(angle_deg, 359)))
    arc_ey = oy - r_arc * math.sin(math.radians(min(angle_deg, 359)))
    large_arc = 1 if angle_deg > 180 else 0
    arc_path = f"M {ox + r_arc} {oy} A {r_arc} {r_arc} 0 {large_arc} 0 {arc_ex:.1f} {arc_ey:.1f}"

    svg = (
        f'<svg viewBox="0 0 400 320" width="100%" height="260" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="400" height="320" fill="#f8fafc" rx="8"/>'
        f'<line x1="30" y1="{oy}" x2="370" y2="{oy}" stroke="#64748b" stroke-width="2"/>'
        f'<line x1="{ox}" y1="290" x2="{ox}" y2="30" stroke="#64748b" stroke-width="2"/>'
        f'<text x="375" y="{oy + 5}" font-size="14" fill="#334155" font-weight="bold">x</text>'
        f'<text x="{ox - 5}" y="22" font-size="14" fill="#334155" font-weight="bold">y</text>'
        f'<text x="{ox - 14}" y="{oy + 16}" font-size="12" fill="#64748b">O</text>'
        # Terminal arm line
        f'<line x1="{ox}" y1="{oy}" x2="{px}" y2="{py}" stroke="#2563eb" stroke-width="3"/>'
        # Point P
        f'<circle cx="{px}" cy="{py}" r="5" fill="#ef4444"/>'
        f'<text x="{px + 8}" y="{py - 6}" font-size="13" fill="#1e293b" font-weight="bold">{pt_label}({x}; {y})</text>'
        # Reference right-triangle dashed lines
        f'<line x1="{px}" y1="{oy}" x2="{px}" y2="{py}" stroke="#94a3b8" stroke-dasharray="4,4" stroke-width="1.5"/>'
        # Angle arc
        f'<path d="{arc_path}" fill="none" stroke="#f59e0b" stroke-width="2"/>'
        f'<text x="{ox + 34}" y="{oy - 10 if y >= 0 else oy + 24}" font-size="13" fill="#d97706" font-weight="bold">{angle_label}</text>'
        f'</svg>'
    )
    return {
        "kind": "inline_svg",
        "svg": svg,
        "diagram_role": "context",
        "point_x": x,
        "point_y": y,
    }


# ---------------------------------------------------------------------------
# 01. Quadrant Identification & CAST Rule Sign
# ---------------------------------------------------------------------------
def build_01_quadrant_identification_sign_cast(r: random.Random) -> Dict[str, Any]:
    angle_base = r.choice([35, 48, 65, 72, 80])
    quad = r.choice([2, 3, 4])
    fn = r.choice(["sin", "cos", "tan"])
    
    if quad == 2:
        angle = 180 - angle_base
        quad_str = "second quadrant ($90^\\circ < \\theta < 180^\\circ$)"
        expected_sign = "positive" if fn == "sin" else "negative"
    elif quad == 3:
        angle = 180 + angle_base
        quad_str = "third quadrant ($180^\\circ < \\theta < 270^\\circ$)"
        expected_sign = "positive" if fn == "tan" else "negative"
    else:
        angle = 360 - angle_base
        quad_str = "fourth quadrant ($270^\\circ < \\theta < 360^\\circ$)"
        expected_sign = "positive" if fn == "cos" else "negative"

    sign_sym = "+" if expected_sign == "positive" else "-"

    prompt = (
        f"State whether the trigonometric ratio $\\{fn}({angle}^\\circ)$ is positive or negative. "
        f"Give a clear reason based on the CAST quadrant rule."
    )
    sample_answer = (
        f"The angle ${angle}^\\circ$ lies in the {quad_str}.\n"
        f"In this quadrant, $\\{fn}$ is {expected_sign} ({sign_sym})."
    )

    return make_math_question(
        prefix="trig_01",
        topic=TOPIC,
        subskill="01_quadrant_identification_sign_cast",
        learning_objective_id=f"{LO_PREFIX}_cast_signs",
        prompt=prompt,
        prompt_latex=rf"\{fn}({angle}^\circ)",
        answer_latex=expected_sign,
        answer_sympy=expected_sign,
        sample_answer=sample_answer,
        marking_schema={
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": f"Correct quadrant identified ({quad_str})", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Correct sign stated: {expected_sign}", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "strict",
        },
        hints={
            "1_nudge": f"Locate which quadrant ${angle}^\\circ$ lies in: between $0^\\circ$, $90^\\circ$, $180^\\circ$, $270^\\circ$, or $360^\\circ$.",
            "2_concept": "CAST rule: Quadrant 1 (All positive), Quadrant 2 (Sine positive), Quadrant 3 (Tan positive), Quadrant 4 (Cos positive).",
            "3_breakdown": f"Since ${angle}^\\circ$ is in Quadrant {quad}, $\\{fn}({angle}^\\circ)$ is {expected_sign}.",
        },
        misconception_tags=["wrong_quadrant_identification", "forgot_cast_rule"],
        keywords=["CAST rule", "quadrants", "signs", "trigonometry"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=2,
        mode="01_quadrant_identification_sign_cast",
        difficulty="easy",
    )


# ---------------------------------------------------------------------------
# 02. Reduction Quadrant 2: sin(180° - θ)
# ---------------------------------------------------------------------------
def build_02_reduction_quadrant_2_sin(r: random.Random) -> Dict[str, Any]:
    coef = r.choice([1, 2, 3, 5])
    coef_str = f"{coef}" if coef > 1 else ""
    prompt = f"Simplify the trigonometric expression to a single ratio of $\\theta$:\n\n$${coef_str}\\sin(180^\\circ - \\theta)$$"
    ans_latex = rf"{coef_str}\sin\theta"
    sample = (
        rf"\text{{In Quadrant 2, sine is positive:}}\\"
        rf"\sin(180^\circ - \theta) = \sin\theta\\"
        rf"\therefore {coef_str}\sin(180^\circ - \theta) = {ans_latex}"
    )
    return make_math_question(
        prefix="trig_02",
        topic=TOPIC,
        subskill="02_reduction_quadrant_2_sin",
        learning_objective_id=f"{LO_PREFIX}_red_quad2_sin",
        prompt=prompt,
        prompt_latex=rf"{coef_str}\sin(180^\circ - \theta)",
        answer_latex=ans_latex,
        answer_sympy=f"{coef}*sin(theta)",
        sample_answer=sample,
        marking_schema={
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Correct sign (+)", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Correct reduced ratio: {ans_latex}", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "strict",
        },
        hints={
            "1_nudge": "$180^\\circ - \\theta$ is in the second quadrant.",
            "2_concept": "In the second quadrant, $\\sin(180^\\circ - \\theta) = +\\sin\\theta$.",
            "3_breakdown": f"Multiply by the coefficient {coef_str if coef_str else '1'} to obtain ${ans_latex}$.",
        },
        misconception_tags=["sign_error_sin_quad2"],
        keywords=["reduction formula", "quadrant 2", "sine"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=2,
        mode="02_reduction_quadrant_2_sin",
        difficulty="easy",
    )


# ---------------------------------------------------------------------------
# 03. Reduction Quadrant 2: cos(180° - θ)
# ---------------------------------------------------------------------------
def build_03_reduction_quadrant_2_cos(r: random.Random) -> Dict[str, Any]:
    coef = r.choice([1, 2, 4, 7])
    coef_str = f"{coef}" if coef > 1 else ""
    prompt = f"Simplify the trigonometric expression to a single ratio of $\\theta$:\n\n$${coef_str}\\cos(180^\\circ - \\theta)$$"
    ans_latex = rf"-{coef_str}\cos\theta"
    sample = (
        rf"\text{{In Quadrant 2, cosine is negative:}}\\"
        rf"\cos(180^\circ - \theta) = -\cos\theta\\"
        rf"\therefore {coef_str}\cos(180^\circ - \theta) = {ans_latex}"
    )
    return make_math_question(
        prefix="trig_03",
        topic=TOPIC,
        subskill="03_reduction_quadrant_2_cos",
        learning_objective_id=f"{LO_PREFIX}_red_quad2_cos",
        prompt=prompt,
        prompt_latex=rf"{coef_str}\cos(180^\circ - \theta)",
        answer_latex=ans_latex,
        answer_sympy=f"-{coef}*cos(theta)",
        sample_answer=sample,
        marking_schema={
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Correct negative sign", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Correct reduced expression: {ans_latex}", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "strict",
        },
        hints={
            "1_nudge": "$180^\\circ - \\theta$ is in Quadrant 2.",
            "2_concept": "Cosine is negative in Quadrant 2: $\\cos(180^\\circ - \\theta) = -\\cos\\theta$.",
            "3_breakdown": f"Multiply by {coef_str if coef_str else '1'} giving ${ans_latex}$.",
        },
        misconception_tags=["sign_error_cos_quad2"],
        keywords=["reduction formula", "quadrant 2", "cosine"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=2,
        mode="03_reduction_quadrant_2_cos",
        difficulty="easy",
    )


# ---------------------------------------------------------------------------
# 04. Reduction Quadrant 2: tan(180° - θ)
# ---------------------------------------------------------------------------
def build_04_reduction_quadrant_2_tan(r: random.Random) -> Dict[str, Any]:
    coef = r.choice([1, 3, 5])
    coef_str = f"{coef}" if coef > 1 else ""
    prompt = f"Simplify the trigonometric expression to a single ratio of $\\theta$:\n\n$${coef_str}\\tan(180^\\circ - \\theta)$$"
    ans_latex = rf"-{coef_str}\tan\theta"
    sample = (
        rf"\text{{In Quadrant 2, tangent is negative:}}\\"
        rf"\tan(180^\circ - \theta) = -\tan\theta\\"
        rf"\therefore {coef_str}\tan(180^\circ - \theta) = {ans_latex}"
    )
    return make_math_question(
        prefix="trig_04",
        topic=TOPIC,
        subskill="04_reduction_quadrant_2_tan",
        learning_objective_id=f"{LO_PREFIX}_red_quad2_tan",
        prompt=prompt,
        prompt_latex=rf"{coef_str}\tan(180^\circ - \theta)",
        answer_latex=ans_latex,
        answer_sympy=f"-{coef}*tan(theta)",
        sample_answer=sample,
        marking_schema={
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Negative sign for tangent in Q2", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Correct reduced ratio: {ans_latex}", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "strict",
        },
        hints={
            "1_nudge": "In Quadrant 2, only sine is positive.",
            "2_concept": "$\\tan(180^\\circ - \\theta) = -\\tan\\theta$.",
            "3_breakdown": f"Multiply by {coef_str if coef_str else '1'} giving ${ans_latex}$.",
        },
        misconception_tags=["sign_error_tan_quad2"],
        keywords=["reduction formula", "quadrant 2", "tangent"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=2,
        mode="04_reduction_quadrant_2_tan",
        difficulty="easy",
    )


# ---------------------------------------------------------------------------
# 05. Reduction Quadrant 3: sin(180° + θ)
# ---------------------------------------------------------------------------
def build_05_reduction_quadrant_3_sin(r: random.Random) -> Dict[str, Any]:
    coef = r.choice([1, 2, 4, 6])
    coef_str = f"{coef}" if coef > 1 else ""
    prompt = f"Simplify the trigonometric expression to a single ratio of $\\theta$:\n\n$${coef_str}\\sin(180^\\circ + \\theta)$$"
    ans_latex = rf"-{coef_str}\sin\theta"
    sample = (
        rf"\text{{In Quadrant 3, sine is negative:}}\\"
        rf"\sin(180^\circ + \theta) = -\sin\theta\\"
        rf"\therefore {coef_str}\sin(180^\circ + \theta) = {ans_latex}"
    )
    return make_math_question(
        prefix="trig_05",
        topic=TOPIC,
        subskill="05_reduction_quadrant_3_sin",
        learning_objective_id=f"{LO_PREFIX}_red_quad3_sin",
        prompt=prompt,
        prompt_latex=rf"{coef_str}\sin(180^\circ + \theta)",
        answer_latex=ans_latex,
        answer_sympy=f"-{coef}*sin(theta)",
        sample_answer=sample,
        marking_schema={
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Negative sign for sine in Q3", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Correct reduced ratio: {ans_latex}", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "strict",
        },
        hints={
            "1_nudge": "$180^\\circ + \\theta$ is in Quadrant 3.",
            "2_concept": "In Quadrant 3, only tangent is positive; sine is negative: $\\sin(180^\\circ + \\theta) = -\\sin\\theta$.",
            "3_breakdown": f"Multiply by {coef_str if coef_str else '1'} giving ${ans_latex}$.",
        },
        misconception_tags=["sign_error_sin_quad3"],
        keywords=["reduction formula", "quadrant 3", "sine"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=2,
        mode="05_reduction_quadrant_3_sin",
        difficulty="easy",
    )


# ---------------------------------------------------------------------------
# 06. Reduction Quadrant 3: cos(180° + θ)
# ---------------------------------------------------------------------------
def build_06_reduction_quadrant_3_cos(r: random.Random) -> Dict[str, Any]:
    coef = r.choice([1, 3, 5])
    coef_str = f"{coef}" if coef > 1 else ""
    prompt = f"Simplify the trigonometric expression to a single ratio of $\\theta$:\n\n$${coef_str}\\cos(180^\\circ + \\theta)$$"
    ans_latex = rf"-{coef_str}\cos\theta"
    sample = (
        rf"\text{{In Quadrant 3, cosine is negative:}}\\"
        rf"\cos(180^\circ + \theta) = -\cos\theta\\"
        rf"\therefore {coef_str}\cos(180^\circ + \theta) = {ans_latex}"
    )
    return make_math_question(
        prefix="trig_06",
        topic=TOPIC,
        subskill="06_reduction_quadrant_3_cos",
        learning_objective_id=f"{LO_PREFIX}_red_quad3_cos",
        prompt=prompt,
        prompt_latex=rf"{coef_str}\cos(180^\circ + \theta)",
        answer_latex=ans_latex,
        answer_sympy=f"-{coef}*cos(theta)",
        sample_answer=sample,
        marking_schema={
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Negative sign for cosine in Q3", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Correct reduced ratio: {ans_latex}", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "strict",
        },
        hints={
            "1_nudge": "$180^\\circ + \\theta$ is in Quadrant 3.",
            "2_concept": "Cosine is negative in Quadrant 3: $\\cos(180^\\circ + \\theta) = -\\cos\\theta$.",
            "3_breakdown": f"Multiply by {coef_str if coef_str else '1'} giving ${ans_latex}$.",
        },
        misconception_tags=["sign_error_cos_quad3"],
        keywords=["reduction formula", "quadrant 3", "cosine"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=2,
        mode="06_reduction_quadrant_3_cos",
        difficulty="easy",
    )


# ---------------------------------------------------------------------------
# 07. Reduction Quadrant 3: tan(180° + θ)
# ---------------------------------------------------------------------------
def build_07_reduction_quadrant_3_tan(r: random.Random) -> Dict[str, Any]:
    coef = r.choice([1, 2, 4])
    coef_str = f"{coef}" if coef > 1 else ""
    prompt = f"Simplify the trigonometric expression to a single ratio of $\\theta$:\n\n$${coef_str}\\tan(180^\\circ + \\theta)$$"
    ans_latex = rf"{coef_str}\tan\theta"
    sample = (
        rf"\text{{In Quadrant 3, tangent is positive:}}\\"
        rf"\tan(180^\circ + \theta) = \tan\theta\\"
        rf"\therefore {coef_str}\tan(180^\circ + \theta) = {ans_latex}"
    )
    return make_math_question(
        prefix="trig_07",
        topic=TOPIC,
        subskill="07_reduction_quadrant_3_tan",
        learning_objective_id=f"{LO_PREFIX}_red_quad3_tan",
        prompt=prompt,
        prompt_latex=rf"{coef_str}\tan(180^\circ + \theta)",
        answer_latex=ans_latex,
        answer_sympy=f"{coef}*tan(theta)",
        sample_answer=sample,
        marking_schema={
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Positive sign for tangent in Q3", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Correct reduced ratio: {ans_latex}", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "strict",
        },
        hints={
            "1_nudge": "$180^\\circ + \\theta$ is in Quadrant 3.",
            "2_concept": "Tangent is positive in Quadrant 3: $\\tan(180^\\circ + \\theta) = +\\tan\\theta$.",
            "3_breakdown": f"Multiply by {coef_str if coef_str else '1'} to get ${ans_latex}$.",
        },
        misconception_tags=["sign_error_tan_quad3"],
        keywords=["reduction formula", "quadrant 3", "tangent"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=2,
        mode="07_reduction_quadrant_3_tan",
        difficulty="easy",
    )


# ---------------------------------------------------------------------------
# 08. Reduction Quadrant 4: sin(360° - θ)
# ---------------------------------------------------------------------------
def build_08_reduction_quadrant_4_sin(r: random.Random) -> Dict[str, Any]:
    coef = r.choice([1, 2, 3])
    coef_str = f"{coef}" if coef > 1 else ""
    prompt = f"Simplify the trigonometric expression to a single ratio of $\\theta$:\n\n$${coef_str}\\sin(360^\\circ - \\theta)$$"
    ans_latex = rf"-{coef_str}\sin\theta"
    sample = (
        rf"\text{{In Quadrant 4, sine is negative:}}\\"
        rf"\sin(360^\circ - \theta) = -\sin\theta\\"
        rf"\therefore {coef_str}\sin(360^\circ - \theta) = {ans_latex}"
    )
    return make_math_question(
        prefix="trig_08",
        topic=TOPIC,
        subskill="08_reduction_quadrant_4_sin",
        learning_objective_id=f"{LO_PREFIX}_red_quad4_sin",
        prompt=prompt,
        prompt_latex=rf"{coef_str}\sin(360^\circ - \theta)",
        answer_latex=ans_latex,
        answer_sympy=f"-{coef}*sin(theta)",
        sample_answer=sample,
        marking_schema={
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Negative sign for sine in Q4", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Correct reduced ratio: {ans_latex}", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "strict",
        },
        hints={
            "1_nudge": "$360^\\circ - \\theta$ is in Quadrant 4.",
            "2_concept": "Sine is negative in Quadrant 4: $\\sin(360^\\circ - \\theta) = -\\sin\\theta$.",
            "3_breakdown": f"Result is ${ans_latex}$.",
        },
        misconception_tags=["sign_error_sin_quad4"],
        keywords=["reduction formula", "quadrant 4", "sine"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=2,
        mode="08_reduction_quadrant_4_sin",
        difficulty="easy",
    )


# ---------------------------------------------------------------------------
# 09. Reduction Quadrant 4: cos(360° - θ)
# ---------------------------------------------------------------------------
def build_09_reduction_quadrant_4_cos(r: random.Random) -> Dict[str, Any]:
    coef = r.choice([1, 4, 5])
    coef_str = f"{coef}" if coef > 1 else ""
    prompt = f"Simplify the trigonometric expression to a single ratio of $\\theta$:\n\n$${coef_str}\\cos(360^\\circ - \\theta)$$"
    ans_latex = rf"{coef_str}\cos\theta"
    sample = (
        rf"\text{{In Quadrant 4, cosine is positive:}}\\"
        rf"\cos(360^\circ - \theta) = \cos\theta\\"
        rf"\therefore {coef_str}\cos(360^\circ - \theta) = {ans_latex}"
    )
    return make_math_question(
        prefix="trig_09",
        topic=TOPIC,
        subskill="09_reduction_quadrant_4_cos",
        learning_objective_id=f"{LO_PREFIX}_red_quad4_cos",
        prompt=prompt,
        prompt_latex=rf"{coef_str}\cos(360^\circ - \theta)",
        answer_latex=ans_latex,
        answer_sympy=f"{coef}*cos(theta)",
        sample_answer=sample,
        marking_schema={
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Positive sign for cosine in Q4", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Correct reduced ratio: {ans_latex}", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "strict",
        },
        hints={
            "1_nudge": "$360^\\circ - \\theta$ is in Quadrant 4.",
            "2_concept": "Cosine is positive in Quadrant 4: $\\cos(360^\\circ - \\theta) = +\\cos\\theta$.",
            "3_breakdown": f"Result is ${ans_latex}$.",
        },
        misconception_tags=["sign_error_cos_quad4"],
        keywords=["reduction formula", "quadrant 4", "cosine"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=2,
        mode="09_reduction_quadrant_4_cos",
        difficulty="easy",
    )


# ---------------------------------------------------------------------------
# 10. Reduction Quadrant 4: tan(360° - θ)
# ---------------------------------------------------------------------------
def build_10_reduction_quadrant_4_tan(r: random.Random) -> Dict[str, Any]:
    coef = r.choice([1, 2, 5])
    coef_str = f"{coef}" if coef > 1 else ""
    prompt = f"Simplify the trigonometric expression to a single ratio of $\\theta$:\n\n$${coef_str}\\tan(360^\\circ - \\theta)$$"
    ans_latex = rf"-{coef_str}\tan\theta"
    sample = (
        rf"\text{{In Quadrant 4, tangent is negative:}}\\"
        rf"\tan(360^\circ - \theta) = -\tan\theta\\"
        rf"\therefore {coef_str}\tan(360^\circ - \theta) = {ans_latex}"
    )
    return make_math_question(
        prefix="trig_10",
        topic=TOPIC,
        subskill="10_reduction_quadrant_4_tan",
        learning_objective_id=f"{LO_PREFIX}_red_quad4_tan",
        prompt=prompt,
        prompt_latex=rf"{coef_str}\tan(360^\circ - \theta)",
        answer_latex=ans_latex,
        answer_sympy=f"-{coef}*tan(theta)",
        sample_answer=sample,
        marking_schema={
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Negative sign for tangent in Q4", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Correct reduced ratio: {ans_latex}", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "strict",
        },
        hints={
            "1_nudge": "$360^\\circ - \\theta$ is in Quadrant 4.",
            "2_concept": "Tangent is negative in Quadrant 4: $\\tan(360^\\circ - \\theta) = -\\tan\\theta$.",
            "3_breakdown": f"Result is ${ans_latex}$.",
        },
        misconception_tags=["sign_error_tan_quad4"],
        keywords=["reduction formula", "quadrant 4", "tangent"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=2,
        mode="10_reduction_quadrant_4_tan",
        difficulty="easy",
    )


# ---------------------------------------------------------------------------
# 11. Negative Angles: cos(-θ)
# ---------------------------------------------------------------------------
def build_11_negative_angle_cos(r: random.Random) -> Dict[str, Any]:
    coef = r.choice([1, 3, 6])
    coef_str = f"{coef}" if coef > 1 else ""
    prompt = f"Simplify the trigonometric expression involving a negative angle:\n\n$${coef_str}\\cos(-\\theta)$$"
    ans_latex = rf"{coef_str}\cos\theta"
    sample = (
        rf"\text{{Cosine is an even function: }}\cos(-\theta) = \cos\theta\\"
        rf"\therefore {coef_str}\cos(-\theta) = {ans_latex}"
    )
    return make_math_question(
        prefix="trig_11",
        topic=TOPIC,
        subskill="11_negative_angle_cos",
        learning_objective_id=f"{LO_PREFIX}_neg_angle_cos",
        prompt=prompt,
        prompt_latex=rf"{coef_str}\cos(-\theta)",
        answer_latex=ans_latex,
        answer_sympy=f"{coef}*cos(theta)",
        sample_answer=sample,
        marking_schema={
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Recognition that cos(-theta) = cos(theta)", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Correct simplified form: {ans_latex}", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "strict",
        },
        hints={
            "1_nudge": "$-\\theta$ lies in Quadrant 4 where cosine is positive.",
            "2_concept": "$\\cos(-\\theta) = \\cos\\theta$ because cosine is an even function.",
            "3_breakdown": f"Result is ${ans_latex}$.",
        },
        misconception_tags=["confused_even_odd_trig"],
        keywords=["negative angles", "even function", "cosine"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=2,
        mode="11_negative_angle_cos",
        difficulty="easy",
    )


# ---------------------------------------------------------------------------
# 12. Negative Angles: sin(-θ) and tan(-θ)
# ---------------------------------------------------------------------------
def build_12_negative_angle_sin_tan(r: random.Random) -> Dict[str, Any]:
    fn = r.choice(["sin", "tan"])
    coef = r.choice([1, 2, 4])
    coef_str = f"{coef}" if coef > 1 else ""
    prompt = f"Simplify the trigonometric expression involving a negative angle:\n\n$${coef_str}\\{fn}(-\\theta)$$"
    ans_latex = rf"-{coef_str}\{fn}\theta"
    sample = (
        rf"\text{{{fn.capitalize()} is an odd function: }}\{fn}(-\theta) = -\{fn}\theta\\"
        rf"\therefore {coef_str}\{fn}(-\theta) = {ans_latex}"
    )
    return make_math_question(
        prefix="trig_12",
        topic=TOPIC,
        subskill="12_negative_angle_sin_tan",
        learning_objective_id=f"{LO_PREFIX}_neg_angle_sin_tan",
        prompt=prompt,
        prompt_latex=rf"{coef_str}\{fn}(-\theta)",
        answer_latex=ans_latex,
        answer_sympy=f"-{coef}*{fn}(theta)",
        sample_answer=sample,
        marking_schema={
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": f"Correct sign (- for {fn}(-theta))", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Correct simplified form: {ans_latex}", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "strict",
        },
        hints={
            "1_nudge": "$-\\theta$ lies in Quadrant 4.",
            "2_concept": f"Both sine and tangent are odd functions: $\\{fn}(-\\theta) = -\\{fn}\\theta$.",
            "3_breakdown": f"Result is ${ans_latex}$.",
        },
        misconception_tags=["confused_even_odd_trig"],
        keywords=["negative angles", "odd function", "sine", "tangent"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=2,
        mode="12_negative_angle_sin_tan",
        difficulty="easy",
    )


# ---------------------------------------------------------------------------
# 13. Co-Ratio: 90° - θ
# ---------------------------------------------------------------------------
def build_13_coratio_90_minus_theta(r: random.Random) -> Dict[str, Any]:
    fn, other_fn = r.choice([("sin", "cos"), ("cos", "sin")])
    coef = r.choice([1, 2, 5])
    coef_str = f"{coef}" if coef > 1 else ""
    prompt = f"Simplify the trigonometric co-ratio expression to a single ratio of $\\theta$:\n\n$${coef_str}\\{fn}(90^\\circ - \\theta)$$"
    ans_latex = rf"{coef_str}\{other_fn}\theta"
    sample = (
        rf"\text{{Co-ratio in Quadrant 1: }}\{fn}(90^\circ - \theta) = \{other_fn}\theta\\"
        rf"\therefore {coef_str}\{fn}(90^\circ - \theta) = {ans_latex}"
    )
    return make_math_question(
        prefix="trig_13",
        topic=TOPIC,
        subskill="13_coratio_90_minus_theta",
        learning_objective_id=f"{LO_PREFIX}_coratio_90_minus",
        prompt=prompt,
        prompt_latex=rf"{coef_str}\{fn}(90^\circ - \theta)",
        answer_latex=ans_latex,
        answer_sympy=f"{coef}*{other_fn}(theta)",
        sample_answer=sample,
        marking_schema={
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": f"Correct co-ratio transformation ({fn} -> {other_fn})", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Correct reduced ratio: {ans_latex}", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "strict",
        },
        hints={
            "1_nudge": "$90^\\circ - \\theta$ is in Quadrant 1, where all ratios are positive.",
            "2_concept": "Angles involving $90^\\circ$ change the function: $\\sin(90^\\circ - \\theta) = \\cos\\theta$ and $\\cos(90^\\circ - \\theta) = \\sin\\theta$.",
            "3_breakdown": f"Result is ${ans_latex}$.",
        },
        misconception_tags=["forgot_co_ratio_change"],
        keywords=["co-ratios", "complementary angles", "90 minus theta"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=2,
        mode="13_coratio_90_minus_theta",
        difficulty="easy",
    )


# ---------------------------------------------------------------------------
# 14. Co-Ratio: 90° + θ
# ---------------------------------------------------------------------------
def build_14_coratio_90_plus_theta(r: random.Random) -> Dict[str, Any]:
    fn, other_fn, sign_str = r.choice([("sin", "cos", "+"), ("cos", "sin", "-")])
    coef = r.choice([1, 3, 4])
    coef_str = f"{coef}" if coef > 1 else ""
    prompt = f"Simplify the trigonometric co-ratio expression to a single ratio of $\\theta$:\n\n$${coef_str}\\{fn}(90^\\circ + \\theta)$$"
    
    if sign_str == "-":
        ans_latex = rf"-{coef_str}\{other_fn}\theta"
        sample_sign_expl = "In Quadrant 2, cosine is negative, so $\\cos(90^\\circ + \\theta) = -\\sin\\theta$."
    else:
        ans_latex = rf"{coef_str}\{other_fn}\theta"
        sample_sign_expl = "In Quadrant 2, sine is positive, so $\\sin(90^\\circ + \\theta) = +\\cos\\theta$."

    sample = (
        rf"\text{{{sample_sign_expl}}}\\"
        rf"\therefore {coef_str}\{fn}(90^\circ + \\theta) = {ans_latex}"
    )

    return make_math_question(
        prefix="trig_14",
        topic=TOPIC,
        subskill="14_coratio_90_plus_theta",
        learning_objective_id=f"{LO_PREFIX}_coratio_90_plus",
        prompt=prompt,
        prompt_latex=rf"{coef_str}\{fn}(90^\circ + \theta)",
        answer_latex=ans_latex,
        answer_sympy=f"{'-' if sign_str == '-' else ''}{coef}*{other_fn}(theta)",
        sample_answer=sample,
        marking_schema={
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": f"Correct co-ratio transformation ({fn} -> {other_fn})", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Correct sign in Quadrant 2: {ans_latex}", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "strict",
        },
        hints={
            "1_nudge": "$90^\\circ + \\theta$ is in Quadrant 2.",
            "2_concept": "Check original function's sign in Q2: sine is positive, cosine is negative. $\\sin(90^\\circ + \\theta) = \\cos\\theta$, $\\cos(90^\\circ + \\theta) = -\\sin\\theta$.",
            "3_breakdown": f"Result is ${ans_latex}$.",
        },
        misconception_tags=["sign_error_coratio_quad2", "checked_new_function_sign"],
        keywords=["co-ratios", "quadrant 2", "90 plus theta"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=2,
        mode="14_coratio_90_plus_theta",
        difficulty="medium",
    )


# ---------------------------------------------------------------------------
# 15. Angles Greater than 360°
# ---------------------------------------------------------------------------
def build_15_angles_greater_than_360(r: random.Random) -> Dict[str, Any]:
    fn = r.choice(["sin", "cos", "tan"])
    revolutions = r.choice([1, 2, 3])
    k_deg = revolutions * 360
    base_op = r.choice(["+", "-"])

    if base_op == "+":
        expr_latex = rf"\{fn}(\theta + {k_deg}^\circ)"
        ans_latex = rf"\{fn}\theta"
        sample = (
            rf"\text{{Trigonometric functions have period }} 360^\circ \text{{ (or }} 180^\circ \text{{ for tan)}}:\\"
            rf"\{fn}(\theta + {revolutions} \times 360^\circ) = \{fn}\theta"
        )
    else:
        expr_latex = rf"\{fn}({k_deg}^\circ - \theta)"
        if fn == "cos":
            ans_latex = r"\cos\theta"
        else:
            ans_latex = rf"-\{fn}\theta"
        sample = (
            rf"\{fn}({revolutions} \times 360^\circ - \theta) = \{fn}(-\theta)\\"
            rf"\text{{Since }}\{fn}(-\theta) = {ans_latex}, \text{{ the expression reduces to }}{ans_latex}"
        )

    prompt = f"Simplify the trigonometric expression involving an angle greater than $360^\\circ$:\n\n$${expr_latex}$$"

    return make_math_question(
        prefix="trig_15",
        topic=TOPIC,
        subskill="15_angles_greater_than_360",
        learning_objective_id=f"{LO_PREFIX}_angles_gt_360",
        prompt=prompt,
        prompt_latex=expr_latex,
        answer_latex=ans_latex,
        answer_sympy=ans_latex,
        sample_answer=sample,
        marking_schema={
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": f"Subtracting multiples of 360 deg ({k_deg} deg)", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Final reduced ratio: {ans_latex}", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "strict",
        },
        hints={
            "1_nudge": f"Subtract complete revolutions of $360^\\circ$ from ${k_deg}^\\circ$.",
            "2_concept": "Adding or subtracting $k \\times 360^\\circ$ leaves the value of any trigonometric function unchanged.",
            "3_breakdown": f"Reducing ${expr_latex}$ yields ${ans_latex}$.",
        },
        misconception_tags=["periodicity_revolution_error"],
        keywords=["periodicity", "angles greater than 360", "revolutions"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=2,
        mode="15_angles_greater_than_360",
        difficulty="medium",
    )


# ---------------------------------------------------------------------------
# 16. Special Angle 30° Exact Values
# ---------------------------------------------------------------------------
def build_16_special_angle_30_exact(r: random.Random) -> Dict[str, Any]:
    fn = r.choice(["sin", "cos", "tan"])
    if fn == "sin":
        val_latex = r"\frac{1}{2}"
        val_sympy = "1/2"
    elif fn == "cos":
        val_latex = r"\frac{\sqrt{3}}{2}"
        val_sympy = "sqrt(3)/2"
    else:
        val_latex = r"\frac{1}{\sqrt{3}}"
        val_sympy = "1/sqrt(3)"

    prompt = f"Without using a calculator, write down the exact value of:\n\n$$\\{fn}(30^\\circ)$$"
    sample = (
        rf"\text{{From the standard }} 30^\circ\text{{-}}60^\circ\text{{-}}90^\circ \text{{ special triangle:}}\\"
        rf"\text{{opposite}} = 1, \; \text{{adjacent}} = \sqrt{{3}}, \; \text{{hypotenuse}} = 2\\"
        rf"\{fn}(30^\circ) = {val_latex}"
    )

    return make_math_question(
        prefix="trig_16",
        topic=TOPIC,
        subskill="16_special_angle_30_exact",
        learning_objective_id=f"{LO_PREFIX}_special_30",
        prompt=prompt,
        prompt_latex=rf"\{fn}(30^\circ)",
        answer_latex=val_latex,
        answer_sympy=val_sympy,
        sample_answer=sample,
        marking_schema={
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Reference to 30-60-90 special triangle or unit circle", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Correct exact value: {val_latex}", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "strict",
        },
        hints={
            "1_nudge": "Recall the equilateral triangle with side length 2 bisected into two $30^\\circ$-$60^\\circ$-$90^\\circ$ triangles.",
            "2_concept": "For $30^\\circ$: $\\text{opp} = 1$, $\\text{adj} = \\sqrt{3}$, $\\text{hyp} = 2$.",
            "3_breakdown": f"$\\{fn}(30^\\circ) = {val_latex}$.",
        },
        misconception_tags=["confused_30_60_special_values"],
        keywords=["special angles", "30 degrees", "exact value"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=2,
        mode="16_special_angle_30_exact",
        difficulty="easy",
    )


# ---------------------------------------------------------------------------
# 17. Special Angle 45° Exact Values
# ---------------------------------------------------------------------------
def build_17_special_angle_45_exact(r: random.Random) -> Dict[str, Any]:
    fn = r.choice(["sin", "cos", "tan"])
    if fn == "tan":
        val_latex = "1"
        val_sympy = "1"
    else:
        val_latex = r"\frac{\sqrt{2}}{2}"
        val_sympy = "sqrt(2)/2"

    prompt = f"Without using a calculator, write down the exact value of:\n\n$$\\{fn}(45^\\circ)$$"
    sample = (
        rf"\text{{From the isosceles right-angled }} 45^\circ\text{{-}}45^\circ\text{{-}}90^\circ \text{{ triangle:}}\\"
        rf"\text{{opposite}} = 1, \; \text{{adjacent}} = 1, \; \text{{hypotenuse}} = \sqrt{{2}}\\"
        rf"\{fn}(45^\circ) = {val_latex}"
    )

    return make_math_question(
        prefix="trig_17",
        topic=TOPIC,
        subskill="17_special_angle_45_exact",
        learning_objective_id=f"{LO_PREFIX}_special_45",
        prompt=prompt,
        prompt_latex=rf"\{fn}(45^\circ)",
        answer_latex=val_latex,
        answer_sympy=val_sympy,
        sample_answer=sample,
        marking_schema={
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Reference to 45-45-90 special triangle", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Correct exact value: {val_latex}", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "strict",
        },
        hints={
            "1_nudge": "Recall an isosceles right triangle with sides $1$, $1$, $\\sqrt{2}$.",
            "2_concept": "For $45^\\circ$: $\\sin 45^\\circ = \\cos 45^\\circ = \\frac{1}{\\sqrt{2}} = \\frac{\\sqrt{2}}{2}$, $\\tan 45^\\circ = 1$.",
            "3_breakdown": f"$\\{fn}(45^\\circ) = {val_latex}$.",
        },
        misconception_tags=["confused_45_special_values"],
        keywords=["special angles", "45 degrees", "exact value"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=2,
        mode="17_special_angle_45_exact",
        difficulty="easy",
    )


# ---------------------------------------------------------------------------
# 18. Special Angle 60° Exact Values
# ---------------------------------------------------------------------------
def build_18_special_angle_60_exact(r: random.Random) -> Dict[str, Any]:
    fn = r.choice(["sin", "cos", "tan"])
    if fn == "sin":
        val_latex = r"\frac{\sqrt{3}}{2}"
        val_sympy = "sqrt(3)/2"
    elif fn == "cos":
        val_latex = r"\frac{1}{2}"
        val_sympy = "1/2"
    else:
        val_latex = r"\sqrt{3}"
        val_sympy = "sqrt(3)"

    prompt = f"Without using a calculator, determine the exact value of:\n\n$$\\{fn}(60^\\circ)$$"
    sample = (
        rf"\text{{From the standard }} 30^\circ\text{{-}}60^\circ\text{{-}}90^\circ \text{{ triangle:}}\\"
        rf"\text{{opposite}} = \sqrt{{3}}, \; \text{{adjacent}} = 1, \; \text{{hypotenuse}} = 2\\"
        rf"\{fn}(60^\circ) = {val_latex}"
    )

    return make_math_question(
        prefix="trig_18",
        topic=TOPIC,
        subskill="18_special_angle_60_exact",
        learning_objective_id=f"{LO_PREFIX}_special_60",
        prompt=prompt,
        prompt_latex=rf"\{fn}(60^\circ)",
        answer_latex=val_latex,
        answer_sympy=val_sympy,
        sample_answer=sample,
        marking_schema={
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Identification of special triangle sides for 60 deg", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Correct exact value: {val_latex}", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "strict",
        },
        hints={
            "1_nudge": "In a $30^\\circ$-$60^\\circ$-$90^\\circ$ triangle, the side opposite $60^\\circ$ is $\\sqrt{3}$.",
            "2_concept": "$\\sin 60^\\circ = \\frac{\\sqrt{3}}{2}$, $\\cos 60^\\circ = \\frac{1}{2}$, $\\tan 60^\\circ = \\sqrt{3}$.",
            "3_breakdown": f"$\\{fn}(60^\\circ) = {val_latex}$.",
        },
        misconception_tags=["inverted_sin_cos_60"],
        keywords=["special angles", "60 degrees", "exact value"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=2,
        mode="18_special_angle_60_exact",
        difficulty="easy",
    )


# ---------------------------------------------------------------------------
# 19. Quadrantal Angles (0°, 90°, 180°, 270°, 360°)
# ---------------------------------------------------------------------------
def build_19_special_angle_quadrantal_0_90_180(r: random.Random) -> Dict[str, Any]:
    cases = [
        ("sin", 0, "0"),
        ("cos", 0, "1"),
        ("sin", 90, "1"),
        ("cos", 90, "0"),
        ("sin", 180, "0"),
        ("cos", 180, "-1"),
        ("sin", 270, "-1"),
        ("cos", 270, "0"),
        ("sin", 360, "0"),
        ("cos", 360, "1"),
    ]
    fn, angle_deg, expected_val = r.choice(cases)
    prompt = f"Without using a calculator, determine the value of the quadrantal trigonometric ratio:\n\n$$\\{fn}({angle_deg}^\\circ)$$"
    sample = (
        rf"\text{{On the unit circle where }} x = \cos\theta \text{{ and }} y = \sin\theta:\\"
        rf"\text{{At }} \theta = {angle_deg}^\circ, \; \{fn}({angle_deg}^\circ) = {expected_val}"
    )

    return make_math_question(
        prefix="trig_19",
        topic=TOPIC,
        subskill="19_special_angle_quadrantal_0_90_180",
        learning_objective_id=f"{LO_PREFIX}_quadrantal_angles",
        prompt=prompt,
        prompt_latex=rf"\{fn}({angle_deg}^\circ)",
        answer_latex=expected_val,
        answer_sympy=expected_val,
        sample_answer=sample,
        marking_schema={
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Reference to coordinates on the unit circle", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Correct value: {expected_val}", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "strict",
        },
        hints={
            "1_nudge": f"Think of the unit circle coordinates $(x, y) = (\\cos\\theta, \\sin\\theta)$ at ${angle_deg}^\\circ$.",
            "2_concept": "Coordinates at axis intercepts: $(1; 0)$ at $0^\\circ$, $(0; 1)$ at $90^\\circ$, $(-1; 0)$ at $180^\\circ$, $(0; -1)$ at $270^\\circ$.",
            "3_breakdown": f"$\\{fn}({angle_deg}^\\circ) = {expected_val}$.",
        },
        misconception_tags=["confused_unit_circle_coordinates"],
        keywords=["quadrantal angles", "unit circle", "exact value"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=2,
        mode="19_special_angle_quadrantal_0_90_180",
        difficulty="easy",
    )


# ---------------------------------------------------------------------------
# 20. Numerical Reduction in Quadrant 2
# ---------------------------------------------------------------------------
def build_20_numerical_reduction_quad2(r: random.Random) -> Dict[str, Any]:
    cases = [
        ("sin", 120, 60, r"\sin 60^\circ", r"\frac{\sqrt{3}}{2}"),
        ("cos", 120, 60, r"-\cos 60^\circ", r"-\frac{1}{2}"),
        ("tan", 120, 60, r"-\tan 60^\circ", r"-\sqrt{3}"),
        ("sin", 135, 45, r"\sin 45^\circ", r"\frac{\sqrt{2}}{2}"),
        ("cos", 135, 45, r"-\cos 45^\circ", r"-\frac{\sqrt{2}}{2}"),
        ("tan", 135, 45, r"-\tan 45^\circ", "-1"),
        ("sin", 150, 30, r"\sin 30^\circ", r"\frac{1}{2}"),
        ("cos", 150, 30, r"-\cos 30^\circ", r"-\frac{\sqrt{3}}{2}"),
        ("tan", 150, 30, r"-\tan 30^\circ", r"-\frac{1}{\sqrt{3}}"),
    ]
    fn, angle_deg, ref_deg, red_latex, ans_latex = r.choice(cases)

    prompt = (
        f"Without using a calculator, evaluate the exact value of the following expression. "
        f"Show the reduction formula step:\n\n$$\\{fn}({angle_deg}^\\circ)$$"
    )
    sample = (
        rf"\{fn}({angle_deg}^\circ) = \{fn}(180^\circ - {ref_deg}^\circ)\\"
        rf"= {red_latex}\\"
        rf"= {ans_latex}"
    )

    return make_math_question(
        prefix="trig_20",
        topic=TOPIC,
        subskill="20_numerical_reduction_quad2",
        learning_objective_id=f"{LO_PREFIX}_num_red_quad2",
        prompt=prompt,
        prompt_latex=rf"\{fn}({angle_deg}^\circ)",
        answer_latex=ans_latex,
        answer_sympy=ans_latex,
        sample_answer=sample,
        marking_schema={
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": f"Correct reduction form: {fn}(180 - {ref_deg})", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Correct ratio with sign: {red_latex}", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Correct exact special value: {ans_latex}", "marks": 1, "editable": True},
            ],
            "deductions": [{"rule": "sign_error", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
        hints={
            "1_nudge": f"Rewrite ${angle_deg}^\\circ$ as $(180^\\circ - {ref_deg}^\\circ)$.",
            "2_concept": "Apply Quadrant 2 reduction, noting the sign for this function.",
            "3_breakdown": f"$\\{fn}({angle_deg}^\\circ) = {red_latex} = {ans_latex}$.",
        },
        misconception_tags=["sign_error_in_reduction", "wrong_special_angle_value"],
        keywords=["numerical reduction", "quadrant 2", "special angles"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=3,
        mode="20_numerical_reduction_quad2",
        difficulty="medium",
    )


# ---------------------------------------------------------------------------
# 21. Numerical Reduction in Quadrant 3
# ---------------------------------------------------------------------------
def build_21_numerical_reduction_quad3(r: random.Random) -> Dict[str, Any]:
    cases = [
        ("sin", 210, 30, r"-\sin 30^\circ", r"-\frac{1}{2}"),
        ("cos", 210, 30, r"-\cos 30^\circ", r"-\frac{\sqrt{3}}{2}"),
        ("tan", 210, 30, r"\tan 30^\circ", r"\frac{1}{\sqrt{3}}"),
        ("sin", 225, 45, r"-\sin 45^\circ", r"-\frac{\sqrt{2}}{2}"),
        ("cos", 225, 45, r"-\cos 45^\circ", r"-\frac{\sqrt{2}}{2}"),
        ("tan", 225, 45, r"\tan 45^\circ", "1"),
        ("sin", 240, 60, r"-\sin 60^\circ", r"-\frac{\sqrt{3}}{2}"),
        ("cos", 240, 60, r"-\cos 60^\circ", r"-\frac{1}{2}"),
        ("tan", 240, 60, r"\tan 60^\circ", r"\sqrt{3}"),
    ]
    fn, angle_deg, ref_deg, red_latex, ans_latex = r.choice(cases)

    prompt = (
        f"Without using a calculator, determine the exact value of the following expression. "
        f"Show your reduction steps clearly:\n\n$$\\{fn}({angle_deg}^\\circ)$$"
    )
    sample = (
        rf"\{fn}({angle_deg}^\circ) = \{fn}(180^\circ + {ref_deg}^\circ)\\"
        rf"= {red_latex}\\"
        rf"= {ans_latex}"
    )

    return make_math_question(
        prefix="trig_21",
        topic=TOPIC,
        subskill="21_numerical_reduction_quad3",
        learning_objective_id=f"{LO_PREFIX}_num_red_quad3",
        prompt=prompt,
        prompt_latex=rf"\{fn}({angle_deg}^\circ)",
        answer_latex=ans_latex,
        answer_sympy=ans_latex,
        sample_answer=sample,
        marking_schema={
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": f"Correct reduction form: {fn}(180 + {ref_deg})", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Correct ratio with sign: {red_latex}", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Correct exact special value: {ans_latex}", "marks": 1, "editable": True},
            ],
            "deductions": [{"rule": "sign_error", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
        hints={
            "1_nudge": f"Write ${angle_deg}^\\circ$ as $(180^\\circ + {ref_deg}^\\circ)$.",
            "2_concept": "In Quadrant 3, tangent is positive while sine and cosine are negative.",
            "3_breakdown": f"$\\{fn}({angle_deg}^\\circ) = {red_latex} = {ans_latex}$.",
        },
        misconception_tags=["sign_error_in_reduction", "wrong_special_angle_value"],
        keywords=["numerical reduction", "quadrant 3", "special angles"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=3,
        mode="21_numerical_reduction_quad3",
        difficulty="medium",
    )


# ---------------------------------------------------------------------------
# 22. Numerical Reduction in Quadrant 4
# ---------------------------------------------------------------------------
def build_22_numerical_reduction_quad4(r: random.Random) -> Dict[str, Any]:
    cases = [
        ("sin", 300, 60, r"-\sin 60^\circ", r"-\frac{\sqrt{3}}{2}"),
        ("cos", 300, 60, r"\cos 60^\circ", r"\frac{1}{2}"),
        ("tan", 300, 60, r"-\tan 60^\circ", r"-\sqrt{3}"),
        ("sin", 315, 45, r"-\sin 45^\circ", r"-\frac{\sqrt{2}}{2}"),
        ("cos", 315, 45, r"\cos 45^\circ", r"\frac{\sqrt{2}}{2}"),
        ("tan", 315, 45, r"-\tan 45^\circ", "-1"),
        ("sin", 330, 30, r"-\sin 30^\circ", r"-\frac{1}{2}"),
        ("cos", 330, 30, r"\cos 30^\circ", r"\frac{\sqrt{3}}{2}"),
        ("tan", 330, 30, r"-\tan 30^\circ", r"-\frac{1}{\sqrt{3}}"),
    ]
    fn, angle_deg, ref_deg, red_latex, ans_latex = r.choice(cases)

    prompt = (
        f"Without using a calculator, determine the exact value of the following expression. "
        f"Show all working:\n\n$$\\{fn}({angle_deg}^\\circ)$$"
    )
    sample = (
        rf"\{fn}({angle_deg}^\circ) = \{fn}(360^\circ - {ref_deg}^\circ)\\"
        rf"= {red_latex}\\"
        rf"= {ans_latex}"
    )

    return make_math_question(
        prefix="trig_22",
        topic=TOPIC,
        subskill="22_numerical_reduction_quad4",
        learning_objective_id=f"{LO_PREFIX}_num_red_quad4",
        prompt=prompt,
        prompt_latex=rf"\{fn}({angle_deg}^\circ)",
        answer_latex=ans_latex,
        answer_sympy=ans_latex,
        sample_answer=sample,
        marking_schema={
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": f"Correct reduction form: {fn}(360 - {ref_deg})", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Correct ratio with sign: {red_latex}", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Correct exact special value: {ans_latex}", "marks": 1, "editable": True},
            ],
            "deductions": [{"rule": "sign_error", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
        hints={
            "1_nudge": f"Write ${angle_deg}^\\circ$ as $(360^\\circ - {ref_deg}^\\circ)$.",
            "2_concept": "In Quadrant 4, cosine is positive while sine and tangent are negative.",
            "3_breakdown": f"$\\{fn}({angle_deg}^\\circ) = {red_latex} = {ans_latex}$.",
        },
        misconception_tags=["sign_error_in_reduction", "wrong_special_angle_value"],
        keywords=["numerical reduction", "quadrant 4", "special angles"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=3,
        mode="22_numerical_reduction_quad4",
        difficulty="medium",
    )


# ---------------------------------------------------------------------------
# 23. Numerical Reduction with Negative Angles
# ---------------------------------------------------------------------------
def build_23_numerical_reduction_negative_special(r: random.Random) -> Dict[str, Any]:
    cases = [
        ("cos", 30, r"\cos 30^\circ", r"\frac{\sqrt{3}}{2}"),
        ("sin", 30, r"-\sin 30^\circ", r"-\frac{1}{2}"),
        ("tan", 30, r"-\tan 30^\circ", r"-\frac{1}{\sqrt{3}}"),
        ("cos", 45, r"\cos 45^\circ", r"\frac{\sqrt{2}}{2}"),
        ("sin", 45, r"-\sin 45^\circ", r"-\frac{\sqrt{2}}{2}"),
        ("tan", 45, r"-\tan 45^\circ", "-1"),
        ("cos", 60, r"\cos 60^\circ", r"\frac{1}{2}"),
        ("sin", 60, r"-\sin 60^\circ", r"-\frac{\sqrt{3}}{2}"),
        ("tan", 60, r"-\tan 60^\circ", r"-\sqrt{3}"),
    ]
    fn, angle_deg, red_latex, ans_latex = r.choice(cases)

    prompt = (
        f"Without using a calculator, evaluate the exact value of the expression involving a negative angle:\n\n"
        f"$$\\{fn}(-{angle_deg}^\\circ)$$"
    )
    sample = (
        rf"\text{{Apply negative angle rule: }}\{fn}(-{angle_deg}^\circ) = {red_latex}\\"
        rf"= {ans_latex}"
    )

    return make_math_question(
        prefix="trig_23",
        topic=TOPIC,
        subskill="23_numerical_reduction_negative_special",
        learning_objective_id=f"{LO_PREFIX}_num_red_neg",
        prompt=prompt,
        prompt_latex=rf"\{fn}(-{angle_deg}^\circ)",
        answer_latex=ans_latex,
        answer_sympy=ans_latex,
        sample_answer=sample,
        marking_schema={
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": f"Correct negative angle reduction: {red_latex}", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Correct exact value: {ans_latex}", "marks": 1, "editable": True},
            ],
            "deductions": [{"rule": "sign_error", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
        hints={
            "1_nudge": f"Determine whether $\\{fn}$ is an even or odd function.",
            "2_concept": "$\\cos(-\\theta) = \\cos\\theta$, but $\\sin(-\\theta) = -\\sin\\theta$ and $\\tan(-\\theta) = -\\tan\\theta$.",
            "3_breakdown": f"$\\{fn}(-{angle_deg}^\\circ) = {red_latex} = {ans_latex}$.",
        },
        misconception_tags=["confused_even_odd_trig", "sign_error_in_reduction"],
        keywords=["negative angles", "numerical reduction", "special angles"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=2,
        mode="23_numerical_reduction_negative_special",
        difficulty="medium",
    )


# ---------------------------------------------------------------------------
# 24. Cartesian Plane Terminal Arm: Point in Quadrant 1 (with inline_svg)
# ---------------------------------------------------------------------------
def build_24_cartesian_plane_terminal_arm_quad1(r: random.Random) -> Dict[str, Any]:
    triples = [(3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25)]
    x, y, hyp = r.choice(triples)
    ratio_choice = r.choice(["sin", "cos", "tan"])

    if ratio_choice == "sin":
        ans_latex = rf"\frac{{{y}}}{{{hyp}}}"
        ratio_calc = rf"\sin\theta = \frac{{y}}{{r}} = \frac{{{y}}}{{{hyp}}}"
    elif ratio_choice == "cos":
        ans_latex = rf"\frac{{{x}}}{{{hyp}}}"
        ratio_calc = rf"\cos\theta = \frac{{x}}{{r}} = \frac{{{x}}}{{{hyp}}}"
    else:
        ans_latex = rf"\frac{{{y}}}{{{x}}}"
        ratio_calc = rf"\tan\theta = \frac{{y}}{{x}} = \frac{{{y}}}{{{x}}}"

    d_spec = _cartesian_terminal_svg(x, y, pt_label="P", angle_label=r"\theta")

    prompt = (
        f"In the Cartesian plane diagram shown, the terminal arm of angle $\\theta$ in standard position "
        f"passes through the point $P({x}; {y})$.\n\n"
        f"Calculate the value of $r$ (the distance $OP$) and determine the exact value of $\\{ratio_choice}\\theta$."
    )
    sample = (
        rf"r^2 = x^2 + y^2 = ({x})^2 + ({y})^2 = {x*x} + {y*y} = {hyp*hyp}\\"
        rf"\therefore r = {hyp} \quad (r > 0)\\"
        rf"{ratio_calc}"
    )

    return make_math_question(
        prefix="trig_24",
        topic=TOPIC,
        subskill="24_cartesian_plane_terminal_arm_quad1",
        learning_objective_id=f"{LO_PREFIX}_cartesian_quad1",
        prompt=prompt,
        prompt_latex=rf"P({x}; {y}), \; \{ratio_choice}\theta",
        answer_latex=ans_latex,
        answer_sympy=f"{y}/{hyp}" if ratio_choice == "sin" else (f"{x}/{hyp}" if ratio_choice == "cos" else f"{y}/{x}"),
        sample_answer=sample,
        marking_schema={
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": f"Correct application of Pythagoras to find r = {hyp}", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Correct ratio definition for {ratio_choice}", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Correct final fraction: {ans_latex}", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        hints={
            "1_nudge": "Use Pythagoras to calculate the distance $r = \\sqrt{x^2 + y^2}$.",
            "2_concept": "In standard position: $\\sin\\theta = \\frac{y}{r}$, $\\cos\\theta = \\frac{x}{r}$, and $\\tan\\theta = \\frac{y}{x}$.",
            "3_breakdown": f"$r = \\sqrt{{{x}^2 + {y}^2}} = {hyp}$. Therefore $\\{ratio_choice}\\theta = {ans_latex}$.",
        },
        misconception_tags=["inverted_trig_ratio", "negative_radius_error"],
        keywords=["Cartesian plane", "terminal arm", "Pythagoras", "trigonometric definitions"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=3,
        mode="24_cartesian_plane_terminal_arm_quad1",
        difficulty="medium",
        diagram_spec=d_spec,
    )


# ---------------------------------------------------------------------------
# 25. Cartesian Plane Terminal Arm: Quadrants 2, 3, 4 (with inline_svg)
# ---------------------------------------------------------------------------
def build_25_cartesian_plane_terminal_arm_quad2_3_4(r: random.Random) -> Dict[str, Any]:
    triples = [(3, 4, 5), (5, 12, 13), (8, 15, 17)]
    base_x, base_y, hyp = r.choice(triples)
    quad = r.choice([2, 3, 4])

    if quad == 2:
        x = -base_x
        y = base_y
        quad_cond = r"\sin\theta > 0 \text{ and } \theta \in [90^\circ; 270^\circ]"
    elif quad == 3:
        x = -base_x
        y = -base_y
        quad_cond = r"\tan\theta > 0 \text{ and } \cos\theta < 0"
    else:
        x = base_x
        y = -base_y
        quad_cond = r"\cos\theta > 0 \text{ and } \sin\theta < 0"

    d_spec = _cartesian_terminal_svg(x, y, pt_label="P", angle_label=r"\theta")

    # Question evaluates an expression like sin^2(theta) + cos(theta) or similar
    prompt = (
        f"In the Cartesian plane diagram shown, the point $P({x}; {y})$ lies on the terminal arm of angle $\\theta$.\n\n"
        f"Given that {quad_cond}, calculate without the use of a calculator the value of $\\sin\\theta$."
    )
    ans_latex = rf"\frac{{{y}}}{{{hyp}}}"
    sample = (
        rf"\text{{Calculate the radius }} r:\\"
        rf"r = \sqrt{{({x})^2 + ({y})^2}} = \sqrt{{{x*x + y*y}}} = {hyp}\\"
        rf"\sin\theta = \frac{{y}}{{r}} = \frac{{{y}}}{{{hyp}}}"
    )

    return make_math_question(
        prefix="trig_25",
        topic=TOPIC,
        subskill="25_cartesian_plane_terminal_arm_quad2_3_4",
        learning_objective_id=f"{LO_PREFIX}_cartesian_quad234",
        prompt=prompt,
        prompt_latex=rf"P({x}; {y}), \; \sin\theta",
        answer_latex=ans_latex,
        answer_sympy=f"{y}/{hyp}",
        sample_answer=sample,
        marking_schema={
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": f"Correct calculation of r = {hyp}", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Correct sign for y in Quadrant {quad}", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Correct exact ratio: {ans_latex}", "marks": 1, "editable": True},
            ],
            "deductions": [{"rule": "sign_error", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
        hints={
            "1_nudge": f"Identify the quadrant from $P({x}; {y})$ and calculate $r = \\sqrt{{x^2 + y^2}}$.",
            "2_concept": "Radius $r$ is always positive ($r > 0$). The ratio is $\\sin\\theta = \\frac{y}{r}$.",
            "3_breakdown": f"$r = {hyp}$, $y = {y}$, so $\\sin\\theta = {ans_latex}$.",
        },
        misconception_tags=["sign_error_in_cartesian_coordinates", "wrong_quadrant_identification"],
        keywords=["Cartesian plane", "quadrants", "CAST diagram", "exact ratio"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=3,
        mode="25_cartesian_plane_terminal_arm_quad2_3_4",
        difficulty="medium",
        diagram_spec=d_spec,
    )


# ---------------------------------------------------------------------------
# Registry Map of Archetypes 01–25
# ---------------------------------------------------------------------------
ARCHETYPES_01_25 = {
    "01_quadrant_identification_sign_cast": build_01_quadrant_identification_sign_cast,
    "02_reduction_quadrant_2_sin": build_02_reduction_quadrant_2_sin,
    "03_reduction_quadrant_2_cos": build_03_reduction_quadrant_2_cos,
    "04_reduction_quadrant_2_tan": build_04_reduction_quadrant_2_tan,
    "05_reduction_quadrant_3_sin": build_05_reduction_quadrant_3_sin,
    "06_reduction_quadrant_3_cos": build_06_reduction_quadrant_3_cos,
    "07_reduction_quadrant_3_tan": build_07_reduction_quadrant_3_tan,
    "08_reduction_quadrant_4_sin": build_08_reduction_quadrant_4_sin,
    "09_reduction_quadrant_4_cos": build_09_reduction_quadrant_4_cos,
    "10_reduction_quadrant_4_tan": build_10_reduction_quadrant_4_tan,
    "11_negative_angle_cos": build_11_negative_angle_cos,
    "12_negative_angle_sin_tan": build_12_negative_angle_sin_tan,
    "13_coratio_90_minus_theta": build_13_coratio_90_minus_theta,
    "14_coratio_90_plus_theta": build_14_coratio_90_plus_theta,
    "15_angles_greater_than_360": build_15_angles_greater_than_360,
    "16_special_angle_30_exact": build_16_special_angle_30_exact,
    "17_special_angle_45_exact": build_17_special_angle_45_exact,
    "18_special_angle_60_exact": build_18_special_angle_60_exact,
    "19_special_angle_quadrantal_0_90_180": build_19_special_angle_quadrantal_0_90_180,
    "20_numerical_reduction_quad2": build_20_numerical_reduction_quad2,
    "21_numerical_reduction_quad3": build_21_numerical_reduction_quad3,
    "22_numerical_reduction_quad4": build_22_numerical_reduction_quad4,
    "23_numerical_reduction_negative_special": build_23_numerical_reduction_negative_special,
    "24_cartesian_plane_terminal_arm_quad1": build_24_cartesian_plane_terminal_arm_quad1,
    "25_cartesian_plane_terminal_arm_quad2_3_4": build_25_cartesian_plane_terminal_arm_quad2_3_4,
}
