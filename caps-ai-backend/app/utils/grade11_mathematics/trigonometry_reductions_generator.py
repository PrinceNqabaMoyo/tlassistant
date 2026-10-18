"""Grade 11 Mathematics — Trigonometric Reductions, Identities & General Solutions (Deterministic 6-Pillar Generator).
Covers official CAPS Examination standards (Paper 2 — 40 to 50 marks):
- Quadrant reduction formulas (180° ± θ, 360° - θ, negative angles, co-ratios 90° - θ).
- Quotient (tan θ = sin θ / cos θ) and Pythagorean square identities (sin² θ + cos² θ = 1).
- General solutions for sine, cosine, and tangent equations.
Supports full compound exam questions and atomic elementary sub-drills for adaptive deconstruction.
"""
from __future__ import annotations

import math
from typing import Any, Dict, List, Optional
import sympy as sp

from app.utils.grade11_mathematics._math_common import (
    make_id,
    make_math_question,
    nonzero,
    rng,
    solution_graph,
    step,
)

TOPIC = "trigonometry_reductions_identities"
LO = "math11_trig_reductions"
theta = sp.Symbol("theta")


# --------------------------------------------------------------------------- #
# Sub-Drill: Single Quadrant Reduction
# --------------------------------------------------------------------------- #
def _build_reduction_drill(r, difficulty: str) -> Dict[str, Any]:
    cases = [
        (r"\sin(180^\circ - \theta)", r"\sin\theta", "Quadrant 2: sine is positive", ["forgot_sign_reduction"]),
        (r"\cos(180^\circ - \theta)", r"-\cos\theta", "Quadrant 2: cosine is negative", ["sign_error_cos_quad2"]),
        (r"\tan(180^\circ - \theta)", r"-\tan\theta", "Quadrant 2: tangent is negative", ["sign_error_tan_quad2"]),
        (r"\sin(180^\circ + \theta)", r"-\sin\theta", "Quadrant 3: sine is negative", ["sign_error_sin_quad3"]),
        (r"\cos(180^\circ + \theta)", r"-\cos\theta", "Quadrant 3: cosine is negative", ["sign_error_cos_quad3"]),
        (r"\tan(180^\circ + \theta)", r"\tan\theta", "Quadrant 3: tangent is positive", ["forgot_tan_positive_quad3"]),
        (r"\sin(360^\circ - \theta)", r"-\sin\theta", "Quadrant 4: sine is negative", ["sign_error_sin_quad4"]),
        (r"\cos(360^\circ - \theta)", r"\cos\theta", "Quadrant 4: cosine is positive", ["forgot_cos_positive_quad4"]),
        (r"\cos(-\theta)", r"\cos\theta", "Negative angle: cosine is an even function", ["sign_error_cos_negative"]),
        (r"\sin(-\theta)", r"-\sin\theta", "Negative angle: sine is an odd function", ["forgot_negative_sin_odd"]),
        (r"\sin(90^\circ - \theta)", r"\cos\theta", "Co-ratio: sin(90° - θ) = cos θ", ["confused_co_ratio"]),
        (r"\cos(90^\circ - \theta)", r"\sin\theta", "Co-ratio: cos(90° - θ) = sin θ", ["confused_co_ratio"]),
    ]

    target_expr, target_ans, target_rule, misc = r.choice(cases)

    prompt = f"Simplify the trigonometric expression to a single trigonometric ratio of $\\theta$:\n\n$${target_expr}$$"

    return make_math_question(
        prefix="trig_red_single",
        topic=TOPIC,
        subskill="elementary_reduction_quadrant",
        learning_objective_id=f"{LO}_reduction_quadrant",
        prompt=prompt,
        prompt_latex=target_expr,
        answer_latex=target_ans,
        answer_sympy=target_ans,
        sample_answer=f"{target_expr} = {target_ans} \\quad ({target_rule})",
        marking_schema={
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": f"Correct sign (+ or -)", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Correct trigonometric function: {target_ans}", "marks": 1, "editable": True},
            ],
            "deductions": [{"rule": "sign_error_quadrant", "penalty": -1}],
            "carry_forward_rule": "strict",
        },
        hints={
            "1_nudge": "Identify which quadrant the angle lies in using the CAST diagram.",
            "2_concept": f"Rule: {target_rule}.",
            "3_breakdown": f"{target_expr} = {target_ans}.",
        },
        misconception_tags=misc,
        keywords=["reduction formula", "CAST diagram", "quadrants", "trigonometry"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=3,
        mode="elementary_reduction_quadrant",
        difficulty="easy",
    )


# --------------------------------------------------------------------------- #
# Sub-Drill: General Solution for Elementary Equation
# --------------------------------------------------------------------------- #
def _build_general_solution_drill(r, difficulty: str) -> Dict[str, Any]:
    fn = r.choice(["sin", "cos", "tan"])
    
    if fn == "sin":
        ref_deg = r.choice([30, 45, 60])
        val_str = r"\frac{1}{2}" if ref_deg == 30 else (r"\frac{\sqrt{2}}{2}" if ref_deg == 45 else r"\frac{\sqrt{3}}{2}")
        quad2_deg = 180 - ref_deg
        prompt = f"Determine the general solution of the trigonometric equation:\n\n$$\\sin\\theta = {val_str}$$"
        ans_latex = rf"\theta = {ref_deg}^\circ + k \cdot 360^\circ \quad \text{{or}} \quad \theta = {quad2_deg}^\circ + k \cdot 360^\circ, \; k \in \mathbb{{Z}}"
        sample = (
            rf"\text{{Reference angle: }} \text{{ref}} = {ref_deg}^\circ\\"
            rf"\text{{Quadrant 1: }} \theta = {ref_deg}^\circ + k \cdot 360^\circ, \; k \in \mathbb{{Z}}\\"
            rf"\text{{Quadrant 2: }} \theta = 180^\circ - {ref_deg}^\circ + k \cdot 360^\circ = {quad2_deg}^\circ + k \cdot 360^\circ, \; k \in \mathbb{{Z}}"
        )
    elif fn == "cos":
        ref_deg = r.choice([30, 45, 60])
        val_str = r"\frac{\sqrt{3}}{2}" if ref_deg == 30 else (r"\frac{\sqrt{2}}{2}" if ref_deg == 45 else r"\frac{1}{2}")
        prompt = f"Determine the general solution of the trigonometric equation:\n\n$$\\cos\\theta = {val_str}$$"
        ans_latex = rf"\theta = \pm {ref_deg}^\circ + k \cdot 360^\circ, \; k \in \mathbb{{Z}}"
        sample = (
            rf"\text{{Reference angle: }} \text{{ref}} = {ref_deg}^\circ\\"
            rf"\theta = \pm {ref_deg}^\circ + k \cdot 360^\circ, \; k \in \mathbb{{Z}}"
        )
    else: # tan
        ref_deg = r.choice([30, 45, 60])
        val_str = r"\frac{1}{\sqrt{3}}" if ref_deg == 30 else ("1" if ref_deg == 45 else r"\sqrt{3}")
        prompt = f"Determine the general solution of the trigonometric equation:\n\n$$\\tan\\theta = {val_str}$$"
        ans_latex = rf"\theta = {ref_deg}^\circ + k \cdot 180^\circ, \; k \in \mathbb{{Z}}"
        sample = (
            rf"\text{{Reference angle: }} \text{{ref}} = {ref_deg}^\circ\\"
            rf"\theta = {ref_deg}^\circ + k \cdot 180^\circ, \; k \in \mathbb{{Z}}"
        )

    return make_math_question(
        prefix="trig_gensol",
        topic=TOPIC,
        subskill="elementary_general_solution",
        learning_objective_id=f"{LO}_general_solution",
        prompt=prompt,
        prompt_latex=prompt,
        answer_latex=ans_latex,
        answer_sympy=ans_latex,
        sample_answer=sample,
        marking_schema={
            "total_marks": 4,
            "marking_points": [
                {"id": "mp1", "desc": f"Correct reference angle ({ref_deg} deg)", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "First quadrant branch with correct period", "marks": 1, "editable": True},
                {"id": "mp3", "desc": "Second quadrant branch / plus-minus sign", "marks": 1, "editable": True},
                {"id": "mp4", "desc": "Statement k in Z", "marks": 1, "editable": True},
            ],
            "deductions": [{"rule": "omitted_k_in_Z", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
        hints={
            "1_nudge": "Find the acute reference angle first using special angles.",
            "2_concept": "For sine and cosine, the period is $k \\cdot 360^\\circ$. For tangent, the period is $k \\cdot 180^\\circ$. Always write $k \\in \\mathbb{Z}$.",
            "3_breakdown": sample,
        },
        misconception_tags=["used_180_period_for_sin_cos", "omitted_k_in_Z", "wrong_quadrant_branch"],
        keywords=["general solution", "reference angle", "periodicity", "special angles"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=5,
        mode="elementary_general_solution",
        difficulty="medium",
    )


# --------------------------------------------------------------------------- #
# Compound Level 3 & 4 Exam Question: Multi-Term Reduction Simplification
# --------------------------------------------------------------------------- #
def _build_compound_trig_simplification(r, difficulty: str) -> Dict[str, Any]:
    archetype_idx = r.randint(0, 4)

    if archetype_idx == 0:
        # Archetype 1: CAST Quadrant reductions -> tan(theta)
        num_str = r"\sin(180^\circ + \theta) \cdot \cos(360^\circ - \theta) \cdot \tan(180^\circ - \theta)"
        den_str = r"\cos(180^\circ - \theta) \cdot \sin(-\theta)"
        expr_str = rf"\frac{{{num_str}}}{{{den_str}}}"
        steps = [
            step(from_latex=expr_str, to_latex_str=r"\frac{(-\sin\theta)(\cos\theta)(-\tan\theta)}{(-\cos\theta)(-\sin\theta)}", op="apply quadrant reduction formulas to each factor", rule="CAST diagram reductions"),
            step(from_latex=r"\frac{(-\sin\theta)(\cos\theta)(-\tan\theta)}{(-\cos\theta)(-\sin\theta)}", to_latex_str=r"\frac{\sin\theta \cos\theta \tan\theta}{\sin\theta \cos\theta}", op="simplify signs in numerator and denominator", rule="sign multiplication"),
            step(from_latex=r"\frac{\sin\theta \cos\theta \tan\theta}{\sin\theta \cos\theta}", to_latex_str=r"\tan\theta", op="cancel common factors: sin θ and cos θ", rule="algebraic fraction cancellation"),
        ]
        ans_latex = r"\tan\theta"
        ans_sympy = "tan(theta)"
        marking_schema = {
            "total_marks": 6,
            "marking_points": [
                {"id": "mp1", "desc": "sin(180 + theta) reduced to -sin(theta)", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "cos(360 - theta) reduced to cos(theta)", "marks": 1, "editable": True},
                {"id": "mp3", "desc": "tan(180 - theta) reduced to -tan(theta)", "marks": 1, "editable": True},
                {"id": "mp4", "desc": "cos(180 - theta) reduced to -cos(theta)", "marks": 1, "editable": True},
                {"id": "mp5", "desc": "sin(-theta) reduced to -sin(theta)", "marks": 1, "editable": True},
                {"id": "mp6", "desc": "Final simplified answer: tan(theta)", "marks": 1, "editable": True},
            ],
            "deductions": [{"rule": "sign_error_in_reduction", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        }
        hints = {
            "nudge": "Reduce each trigonometric ratio individually to an acute angle before multiplying.",
            "concept": "Signs: sin(180 + th) = -sin th, cos(360 - th) = cos th, tan(180 - th) = -tan th, cos(180 - th) = -cos th, sin(-th) = -sin th.",
            "breakdown": "Numerator = (-sin th)(cos th)(-tan th) = sin th cos th tan th. Denominator = (-cos th)(-sin th) = cos th sin th. Result = tan th.",
        }

    elif archetype_idx == 1:
        # Archetype 2: Co-function and square identity -> sin^2(theta)
        num_str = r"\cos(90^\circ - \theta) \cdot \sin(180^\circ - \theta)"
        den_str = r"\cos(-\theta) \cdot \cos(360^\circ - \theta) + \sin^2(180^\circ + \theta)"
        expr_str = rf"\frac{{{num_str}}}{{{den_str}}}"
        steps = [
            step(from_latex=expr_str, to_latex_str=r"\frac{(\sin\theta)(\sin\theta)}{(\cos\theta)(\cos\theta) + (-\sin\theta)^2}", op="apply co-function and quadrant reductions", rule="co-functions and negative angles"),
            step(from_latex=r"\frac{(\sin\theta)(\sin\theta)}{(\cos\theta)(\cos\theta) + (-\sin\theta)^2}", to_latex_str=r"\frac{\sin^2\theta}{\cos^2\theta + \sin^2\theta}", op="simplify products and powers", rule="algebraic multiplication"),
            step(from_latex=r"\frac{\sin^2\theta}{\cos^2\theta + \sin^2\theta}", to_latex_str=r"\sin^2\theta", op="apply square identity cos^2 theta + sin^2 theta = 1", rule="Pythagorean identity"),
        ]
        ans_latex = r"\sin^2\theta"
        ans_sympy = "sin(theta)**2"
        marking_schema = {
            "total_marks": 6,
            "marking_points": [
                {"id": "mp1", "desc": "cos(90 - theta) reduced to sin(theta)", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "sin(180 - theta) reduced to sin(theta)", "marks": 1, "editable": True},
                {"id": "mp3", "desc": "cos(-theta) reduced to cos(theta)", "marks": 1, "editable": True},
                {"id": "mp4", "desc": "cos(360 - theta) reduced to cos(theta)", "marks": 1, "editable": True},
                {"id": "mp5", "desc": "sin^2(180 + theta) reduced to sin^2(theta)", "marks": 1, "editable": True},
                {"id": "mp6", "desc": "Application of cos^2(theta) + sin^2(theta) = 1 to get sin^2(theta)", "marks": 1, "editable": True},
            ],
            "deductions": [{"rule": "sign_error_in_reduction", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        }
        hints = {
            "nudge": "Remember that cos(90 - theta) is a co-function reduction, and cos^2(theta) + sin^2(theta) = 1.",
            "concept": "cos(90 - th) = sin th; sin(180 - th) = sin th; cos(-th) = cos th; cos^2 th + sin^2 th = 1.",
            "breakdown": "Numerator = (sin th)(sin th) = sin^2 th. Denominator = cos^2 th + sin^2 th = 1. Result = sin^2 th.",
        }

    elif archetype_idx == 2:
        # Archetype 3: Tangent quotient reduction -> sin(theta)
        num_str = r"\sin(180^\circ - \theta) \cdot \cos(90^\circ + \theta)"
        den_str = r"\tan(360^\circ - \theta) \cdot \cos(-\theta)"
        expr_str = rf"\frac{{{num_str}}}{{{den_str}}}"
        steps = [
            step(from_latex=expr_str, to_latex_str=r"\frac{(\sin\theta)(-\sin\theta)}{(-\tan\theta)(\cos\theta)}", op="apply quadrant reductions and co-function (90 + theta)", rule="CAST and co-functions"),
            step(from_latex=r"\frac{(\sin\theta)(-\sin\theta)}{(-\tan\theta)(\cos\theta)}", to_latex_str=r"\frac{-\sin^2\theta}{-\left(\frac{\sin\theta}{\cos\theta}\right)\cos\theta}", op="express tan theta as sin theta / cos theta", rule="quotient identity"),
            step(from_latex=r"\frac{-\sin^2\theta}{-\sin\theta}", to_latex_str=r"\sin\theta", op="cancel -sin theta from numerator and denominator", rule="fraction division"),
        ]
        ans_latex = r"\sin\theta"
        ans_sympy = "sin(theta)"
        marking_schema = {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp1", "desc": "sin(180 - theta) = sin(theta)", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "cos(90 + theta) = -sin(theta)", "marks": 1, "editable": True},
                {"id": "mp3", "desc": "tan(360 - theta) = -tan(theta)", "marks": 1, "editable": True},
                {"id": "mp4", "desc": "cos(-theta) = cos(theta)", "marks": 1, "editable": True},
                {"id": "mp5", "desc": "Quotient identity tan = sin/cos and final answer: sin(theta)", "marks": 1, "editable": True},
            ],
            "deductions": [{"rule": "sign_error_in_reduction", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        }
        hints = {
            "nudge": "Notice cos(90 + theta) is in Quadrant 2 where cosine is negative, so cos(90 + theta) = -sin theta.",
            "concept": "tan(360 - th) = -tan th = -sin th / cos th; cos(-th) = cos th.",
            "breakdown": "Numerator = (sin th)(-sin th) = -sin^2 th. Denominator = (-sin th / cos th)(cos th) = -sin th. Division gives sin th.",
        }

    elif archetype_idx == 3:
        # Archetype 4: Unit cancellation -> 1
        num_str = r"\cos(180^\circ + \theta) \cdot \tan(360^\circ - \theta) \cdot \sin(90^\circ - \theta)"
        den_str = r"\sin(180^\circ - \theta) \cdot \cos(-\theta)"
        expr_str = rf"\frac{{{num_str}}}{{{den_str}}}"
        steps = [
            step(from_latex=expr_str, to_latex_str=r"\frac{(-\cos\theta)(-\tan\theta)(\cos\theta)}{(\sin\theta)(\cos\theta)}", op="apply quadrant reductions and co-function", rule="CAST and co-functions"),
            step(from_latex=r"\frac{(-\cos\theta)(-\tan\theta)(\cos\theta)}{(\sin\theta)(\cos\theta)}", to_latex_str=r"\frac{\cos^2\theta \cdot \left(\frac{\sin\theta}{\cos\theta}\right)}{\sin\theta \cos\theta}", op="substitute tan theta = sin theta / cos theta", rule="quotient identity"),
            step(from_latex=r"\frac{\sin\theta \cos\theta}{\sin\theta \cos\theta}", to_latex_str=r"1", op="cancel identical numerator and denominator terms", rule="simplification"),
        ]
        ans_latex = r"1"
        ans_sympy = "1"
        marking_schema = {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp1", "desc": "cos(180 + theta) = -cos(theta)", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "tan(360 - theta) = -tan(theta)", "marks": 1, "editable": True},
                {"id": "mp3", "desc": "sin(90 - theta) = cos(theta)", "marks": 1, "editable": True},
                {"id": "mp4", "desc": "sin(180 - theta) = sin(theta) and cos(-theta) = cos(theta)", "marks": 1, "editable": True},
                {"id": "mp5", "desc": "Final simplified value: 1", "marks": 1, "editable": True},
            ],
            "deductions": [{"rule": "sign_error_in_reduction", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        }
        hints = {
            "nudge": "Convert all angles using CAST rules and rewrite tan theta as sin theta / cos theta.",
            "concept": "(-cos th)(-tan th) = + cos th (sin th / cos th) = sin th.",
            "breakdown": "Numerator = cos^2 th * (sin th / cos th) = sin th cos th. Denominator = sin th cos th. Expression simplifies to 1.",
        }

    else:
        # Archetype 5: Negative signs cancelling -> tan^2(theta)
        num_str = r"\sin(180^\circ + \theta) \cdot \cos(90^\circ - \theta)"
        den_str = r"\cos(180^\circ - \theta) \cdot \sin(90^\circ + \theta)"
        expr_str = rf"\frac{{{num_str}}}{{{den_str}}}"
        steps = [
            step(from_latex=expr_str, to_latex_str=r"\frac{(-\sin\theta)(\sin\theta)}{(-\cos\theta)(\cos\theta)}", op="apply quadrant and co-function reductions", rule="CAST reductions and co-functions"),
            step(from_latex=r"\frac{(-\sin\theta)(\sin\theta)}{(-\cos\theta)(\cos\theta)}", to_latex_str=r"\frac{-\sin^2\theta}{-\cos^2\theta}", op="simplify signs and exponents in numerator and denominator", rule="exponent and sign laws"),
            step(from_latex=r"\frac{-\sin^2\theta}{-\cos^2\theta}", to_latex_str=r"\tan^2\theta", op="apply quotient identity (sin theta / cos theta)^2 = tan^2 theta", rule="quotient identity"),
        ]
        ans_latex = r"\tan^2\theta"
        ans_sympy = "tan(theta)**2"
        marking_schema = {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp1", "desc": "sin(180 + theta) = -sin(theta)", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "cos(90 - theta) = sin(theta)", "marks": 1, "editable": True},
                {"id": "mp3", "desc": "cos(180 - theta) = -cos(theta)", "marks": 1, "editable": True},
                {"id": "mp4", "desc": "sin(90 + theta) = cos(theta)", "marks": 1, "editable": True},
                {"id": "mp5", "desc": "Final ratio: tan^2(theta)", "marks": 1, "editable": True},
            ],
            "deductions": [{"rule": "sign_error_in_reduction", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        }
        hints = {
            "nudge": "Reduce both the numerator and denominator to single trig ratios in terms of theta.",
            "concept": "sin(180 + theta) = -sin theta and sin(90 + theta) = cos theta.",
            "breakdown": "Numerator = -sin^2 theta. Denominator = -cos^2 theta. Result = tan^2 theta.",
        }

    canonical = solution_graph(
        goal="simplify trigonometric reduction expression without calculator",
        steps=steps,
        final_latex=ans_latex,
    )

    return make_math_question(
        prefix="trig_red_compound",
        topic=TOPIC,
        subskill="trigonometric_reduction_compound",
        learning_objective_id=f"{LO}_compound_reduction",
        prompt=f"Simplify the following trigonometric expression to a single trigonometric ratio or numerical value without using a calculator. Show ALL reduction steps:\n\n$${expr_str}$$",
        prompt_latex=expr_str,
        answer_latex=ans_latex,
        answer_sympy=ans_sympy,
        sample_answer=canonical["final_latex"],
        canonical_solution=canonical,
        marking_schema=marking_schema,
        hints=hints,
        misconception_tags=["sign_error_in_reduction", "confused_even_odd_trig_functions", "cancelled_terms_before_sign_simplification"],
        keywords=["trig reductions", "CAST diagram", "identities", "simplification"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=10,
        mode="compound",
        difficulty="hard",
    )


# --------------------------------------------------------------------------- #
# Public Dispatcher
# --------------------------------------------------------------------------- #
BUILDERS = {
    "compound": _build_compound_trig_simplification,
    "elementary_reduction_quadrant": _build_reduction_drill,
    "elementary_general_solution": _build_general_solution_drill,
}


def generate(
    subskill: Optional[str] = None,
    difficulty: str = "hard",
    count: int = 1,
    seed: Optional[int] = None,
    mode: str = "compound",
    **kwargs: Any,
) -> Dict[str, Any]:
    """Generates deterministic Grade 11 Trigonometry questions."""
    base_seed = 42 if seed is None else int(seed)
    chosen_mode = mode if mode in BUILDERS else ("compound" if subskill is None else subskill)
    builder = BUILDERS.get(chosen_mode, _build_compound_trig_simplification)

    questions = []
    for i in range(max(1, count)):
        r = rng(base_seed * 1000 + i)
        q = builder(r, difficulty)
        q["seed"] = base_seed * 1000 + i
        questions.append(q)

    return {"questions": questions}
