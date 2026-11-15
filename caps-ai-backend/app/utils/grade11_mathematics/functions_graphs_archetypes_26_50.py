"""Grade 11 Mathematics — Functions and Graphs Archetypes 26–50.
Grounded in South African National Curriculum Standards for Grade 11 Mathematics (Term 2).
Covers:
- Exponential functions: y = a * b^(x + p) + q (asymptotes, intercepts, domain, range, growth vs decay)
- Determining exponential equation with inline_svg
- Trigonometric graphs: y = a sin(kx) + q, y = a cos(kx) + q, y = a tan(kx) + q
- Amplitude, period, range, vertical shift, phase shifts
- Determining trig graph equations with inline_svg
- Interpretations: intervals where f(x) > 0, f(x).g(x) <= 0, f(x) >= g(x)
- Vertical distances and maximum lengths
- Translations and reflections
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
from app.utils.grade11_mathematics.functions_graphs_archetypes_01_25 import (
    _cartesian_parabola_svg,
)

TOPIC = "Functions and graphs"
LO_PREFIX = "math11_func"


def _exponential_svg(
    a: float,
    b: float,
    q: float,
    pt_x: Optional[float] = None,
    pt_y: Optional[float] = None,
) -> Dict[str, Any]:
    """Generates an inline SVG showing exponential curve y = a * b^x + q with asymptote y = q."""
    ox, oy = 200, 160
    scale_x, scale_y = 30.0, 15.0

    asymp_y_screen = oy - q * scale_y

    pts = []
    for step_i in range(-30, 25):
        x_val = step_i * 0.15
        try:
            y_val = a * (b ** x_val) + q
        except (ValueError, OverflowError):
            continue
        sx = ox + x_val * scale_x
        sy = oy - y_val * scale_y
        if 20 <= sx <= 400 and 20 <= sy <= 270:
            pts.append(f"{sx:.1f},{sy:.1f}")

    polyline = " ".join(pts) if pts else f"{ox},{oy}"

    extra_point = ""
    if pt_x is not None and pt_y is not None:
        px = ox + pt_x * scale_x
        py = oy - pt_y * scale_y
        extra_point = (
            f'<circle cx="{px:.1f}" cy="{py:.1f}" r="4" fill="#059669"/>'
            f'<text x="{px + 6:.1f}" y="{py - 6:.1f}" font-size="12" fill="#065f46" font-weight="bold">({int(pt_x) if pt_x.is_integer() else pt_x}; {int(pt_y) if pt_y.is_integer() else pt_y})</text>'
        )

    svg = (
        f'<svg viewBox="0 0 420 290" width="100%" height="240" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="420" height="290" fill="#f8fafc" rx="8"/>'
        f'<line x1="20" y1="{oy}" x2="400" y2="{oy}" stroke="#64748b" stroke-width="2"/>'
        f'<line x1="{ox}" y1="270" x2="{ox}" y2="20" stroke="#64748b" stroke-width="2"/>'
        f'<text x="405" y="{oy + 4}" font-size="13" fill="#334155" font-weight="bold">x</text>'
        f'<text x="{ox - 5}" y="15" font-size="13" fill="#334155" font-weight="bold">y</text>'
        f'<line x1="20" y1="{asymp_y_screen:.1f}" x2="400" y2="{asymp_y_screen:.1f}" stroke="#f59e0b" stroke-width="1.8" stroke-dasharray="5,4"/>'
        f'<text x="25" y="{asymp_y_screen - 6:.1f}" font-size="11" fill="#d97706">y = {q}</text>'
        f'<polyline points="{polyline}" fill="none" stroke="#2563eb" stroke-width="2.5"/>'
        f'{extra_point}'
        f'</svg>'
    )
    return {
        "kind": "inline_svg",
        "svg": svg,
        "diagram_role": "context",
        "asymptote_y": q,
    }


def _trig_wave_svg(
    a: float,
    k: float,
    q: float,
    fn: str = "sin",
) -> Dict[str, Any]:
    """Generates an inline SVG showing trig wave y = a * fn(k * x) + q over 0 to 360 degrees."""
    ox, oy = 50, 140
    # 0 to 360 mapped to 320 px (ox to ox+320)
    scale_x = 320.0 / 360.0
    scale_y = 25.0

    pts = []
    for deg in range(0, 361, 5):
        rad = math.radians(k * deg)
        val = a * math.sin(rad) + q if fn == "sin" else a * math.cos(rad) + q
        sx = ox + deg * scale_x
        sy = oy - val * scale_y
        pts.append(f"{sx:.1f},{sy:.1f}")

    polyline = " ".join(pts)

    svg = (
        f'<svg viewBox="0 0 420 280" width="100%" height="240" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="420" height="280" fill="#f8fafc" rx="8"/>'
        f'<line x1="30" y1="{oy}" x2="390" y2="{oy}" stroke="#64748b" stroke-width="2"/>'
        f'<line x1="{ox}" y1="260" x2="{ox}" y2="20" stroke="#64748b" stroke-width="2"/>'
        f'<text x="395" y="{oy + 4}" font-size="13" fill="#334155" font-weight="bold">x</text>'
        f'<text x="{ox - 5}" y="15" font-size="13" fill="#334155" font-weight="bold">y</text>'
        # Degree tick marks
        f'<text x="{ox + 90 * scale_x:.1f}" y="{oy + 16}" font-size="11" fill="#64748b" text-anchor="middle">90°</text>'
        f'<text x="{ox + 180 * scale_x:.1f}" y="{oy + 16}" font-size="11" fill="#64748b" text-anchor="middle">180°</text>'
        f'<text x="{ox + 270 * scale_x:.1f}" y="{oy + 16}" font-size="11" fill="#64748b" text-anchor="middle">270°</text>'
        f'<text x="{ox + 360 * scale_x:.1f}" y="{oy + 16}" font-size="11" fill="#64748b" text-anchor="middle">360°</text>'
        f'<polyline points="{polyline}" fill="none" stroke="#2563eb" stroke-width="2.5"/>'
        f'</svg>'
    )
    return {
        "kind": "inline_svg",
        "svg": svg,
        "diagram_role": "context",
        "amplitude": abs(a),
        "period": 360.0 / k,
    }


# ---------------------------------------------------------------------------
# 26. Exponential: Horizontal Asymptote
# ---------------------------------------------------------------------------
def build_26_exponential_horizontal_asymptote(r: random.Random) -> Dict[str, Any]:
    b = r.choice([2, 3, 5])
    q = r.choice([-5, -3, -1, 1, 2, 4])
    q_str = f"+ {q}" if q > 0 else f"- {abs(q)}"
    eq_latex = rf"f(x) = {b}^x {q_str}"

    prompt = f"Write down the equation of the horizontal asymptote of the exponential function ${eq_latex}$."
    ans_latex = rf"y = {q}"
    sample = (
        rf"\text{{As }} x \to -\infty, \; {b}^x \to 0.\\"
        rf"\therefore \text{{Horizontal asymptote: }} y = {q}"
    )

    return make_math_question(
        prefix="func_26",
        topic=TOPIC,
        subskill="26_exponential_horizontal_asymptote",
        learning_objective_id=f"{LO_PREFIX}_exp_asymp",
        prompt=prompt,
        prompt_latex=eq_latex,
        answer_latex=ans_latex,
        answer_sympy=f"y = {q}",
        sample_answer=sample,
        marking_schema={
            "total_marks": 1,
            "marking_points": [
                {"id": "mp1", "desc": f"Correct asymptote equation y = {q}", "marks": 1, "editable": True},
            ],
            "deductions": [{"rule": "omitted_y_equals", "penalty": -1}],
            "carry_forward_rule": "strict",
        },
        hints={
            "1_nudge": "The horizontal asymptote corresponds to the vertical translation $q$.",
            "2_concept": "Since $b^x > 0$ for all $x$, $b^x$ cannot equal 0, so $y$ cannot equal $q$.",
            "3_breakdown": f"Asymptote: $y = {q}$.",
        },
        misconception_tags=["wrote_x_for_horizontal_asymptote"],
        keywords=["exponential", "horizontal asymptote"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=1,
        mode="26_exponential_horizontal_asymptote",
        difficulty="easy",
    )


# ---------------------------------------------------------------------------
# 27. Exponential: y-intercept
# ---------------------------------------------------------------------------
def build_27_exponential_y_intercept(r: random.Random) -> Dict[str, Any]:
    a = r.choice([1, 2, 3])
    b = r.choice([2, 3])
    q = r.choice([-4, -2, 1, 3])

    y_val = a * (b ** 0) + q
    a_str = f"{a} \\cdot " if a > 1 else ""
    q_str = f"+ {q}" if q > 0 else f"- {abs(q)}"
    eq_latex = rf"g(x) = {a_str}{b}^x {q_str}"

    prompt = f"Calculate the coordinates of the $y$-intercept of the exponential function ${eq_latex}$."
    ans_latex = rf"(0; {y_val})"
    sample = (
        rf"\text{{Substitute }} x = 0:\\"
        rf"g(0) = {a_str}{b}^0 {q_str} = {a}(1) {q_str} = {y_val}\\"
        rf"\therefore (0; {y_val})"
    )

    return make_math_question(
        prefix="func_27",
        topic=TOPIC,
        subskill="27_exponential_y_intercept",
        learning_objective_id=f"{LO_PREFIX}_exp_y_int",
        prompt=prompt,
        prompt_latex=eq_latex,
        answer_latex=ans_latex,
        answer_sympy=f"(0, {y_val})",
        sample_answer=sample,
        marking_schema={
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Substituted x = 0 noting b^0 = 1", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Correct coordinates: (0; {y_val})", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        hints={
            "1_nudge": "Substitute $x = 0$ into the expression.",
            "2_concept": "Remember that any non-zero base raised to the power 0 equals 1 ($b^0 = 1$).",
            "3_breakdown": f"$g(0) = {y_val} \\implies (0; {y_val})$.",
        },
        misconception_tags=["assumed_b_power_zero_is_zero"],
        keywords=["exponential", "y-intercept", "zero exponent"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=2,
        mode="27_exponential_y_intercept",
        difficulty="easy",
    )


# ---------------------------------------------------------------------------
# 28. Exponential: Domain and Range
# ---------------------------------------------------------------------------
def build_28_exponential_domain_and_range(r: random.Random) -> Dict[str, Any]:
    a_sign = r.choice([1, -1])
    b = r.choice([2, 3])
    q = r.choice([-3, 1, 4])

    a_str = "-" if a_sign == -1 else ""
    q_str = f"+ {q}" if q > 0 else f"- {abs(q)}"
    eq_latex = rf"f(x) = {a_str}{b}^x {q_str}"

    if a_sign == 1:
        range_str = rf"y > {q}"
    else:
        range_str = rf"y < {q}"

    prompt = f"Write down the domain and the range of the exponential function ${eq_latex}$."
    ans_latex = rf"\text{{Domain: }} x \in \mathbb{{R}}, \; \text{{Range: }} {range_str}"
    sample = (
        rf"\text{{Domain: }} x \in \mathbb{{R}}\\"
        rf"\text{{Since }}{b}^x > 0 \text{{ for all }} x:\\"
        rf"\text{{Range: }} {range_str}"
    )

    return make_math_question(
        prefix="func_28",
        topic=TOPIC,
        subskill="28_exponential_domain_and_range",
        learning_objective_id=f"{LO_PREFIX}_exp_domain_range",
        prompt=prompt,
        prompt_latex=eq_latex,
        answer_latex=ans_latex,
        answer_sympy=ans_latex,
        sample_answer=sample,
        marking_schema={
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Domain: x in R", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Range: {range_str}", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "strict",
        },
        hints={
            "1_nudge": "The domain is all real numbers $x \\in \\mathbb{R}$.",
            "2_concept": "Check whether the exponential curve lies above ($y > q$) or below ($y < q$) the asymptote.",
            "3_breakdown": f"Range is ${range_str}$.",
        },
        misconception_tags=["included_asymptote_in_range_inequality"],
        keywords=["exponential", "domain", "range", "strict inequality"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=2,
        mode="28_exponential_domain_and_range",
        difficulty="easy",
    )


# ---------------------------------------------------------------------------
# 29. Exponential: Growth vs Decay
# ---------------------------------------------------------------------------
def build_29_exponential_growth_vs_decay(r: random.Random) -> Dict[str, Any]:
    case = r.choice(["growth", "decay"])
    if case == "growth":
        b_str = r"2^x"
        expl = "Since the base $2 > 1$, the function increases as $x$ increases."
    else:
        b_str = r"\left(\frac{1}{2}\right)^x"
        expl = r"Since the base $0 < \frac{1}{2} < 1$, the function decreases as $x$ increases."

    prompt = (
        f"Classify the function $f(x) = {b_str}$ as representing exponential growth or exponential decay, "
        f"and provide a reason based on the value of the base $b$."
    )
    ans_latex = f"Exponential {case}"
    sample = f"Classification: Exponential {case}\nReason: {expl}"

    return make_math_question(
        prefix="func_29",
        topic=TOPIC,
        subskill="29_exponential_growth_vs_decay",
        learning_objective_id=f"{LO_PREFIX}_growth_decay",
        prompt=prompt,
        prompt_latex=rf"f(x) = {b_str}",
        answer_latex=ans_latex,
        answer_sympy=case,
        sample_answer=sample,
        marking_schema={
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": f"Correct classification: Exponential {case}", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Valid reason regarding base b", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "strict",
        },
        hints={
            "1_nudge": "Examine the base $b$: is it greater than 1, or between 0 and 1?",
            "2_concept": "$b > 1$ gives growth (increasing), while $0 < b < 1$ gives decay (decreasing).",
            "3_breakdown": f"Result: Exponential {case}.",
        },
        misconception_tags=["confused_growth_and_decay_bases"],
        keywords=["exponential growth", "exponential decay", "base"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=2,
        mode="29_exponential_growth_vs_decay",
        difficulty="easy",
    )


# ---------------------------------------------------------------------------
# 30. Exponential: Determine Equation from Asymptote and Point (with inline_svg)
# ---------------------------------------------------------------------------
def build_30_exponential_equation_from_asymptote_and_point(r: random.Random) -> Dict[str, Any]:
    q = r.choice([-4, -2, 1, 3])
    b = r.choice([2, 3])
    # y = b^x + q => passes through (1, b + q)
    pt_x = 1
    pt_y = b + q

    d_spec = _exponential_svg(
        a=1.0,
        b=float(b),
        q=float(q),
        pt_x=float(pt_x),
        pt_y=float(pt_y),
    )

    q_str = f"+ {q}" if q > 0 else f"- {abs(q)}"
    res_eq = rf"y = {b}^x {q_str}"

    prompt = (
        f"In the graph shown, the exponential curve has horizontal asymptote $y = {q}$ "
        f"and passes through the point $P({pt_x}; {pt_y})$.\n\n"
        f"Determine the equation of the function in the form $y = b^x + q$."
    )
    sample = (
        rf"y = b^x + q \implies y = b^x {q_str}\\"
        rf"\text{{Substitute }} P({pt_x}; {pt_y}):\\"
        rf"{pt_y} = b^{pt_x} {q_str} = b {q_str}\\"
        rf"b = {pt_y} - ({q}) = {b}\\"
        rf"\therefore {res_eq}"
    )

    return make_math_question(
        prefix="func_30",
        topic=TOPIC,
        subskill="30_exponential_equation_from_asymptote_and_point",
        learning_objective_id=f"{LO_PREFIX}_exp_eq_from_graph",
        prompt=prompt,
        prompt_latex=rf"y = {q}, \; P({pt_x}; {pt_y})",
        answer_latex=res_eq,
        answer_sympy=res_eq,
        sample_answer=sample,
        marking_schema={
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": "Substituted horizontal asymptote q", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Substituted point P and solved for b = {b}", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Final equation: {res_eq}", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        hints={
            "1_nudge": "The horizontal asymptote gives the value of $q$ directly.",
            "2_concept": "Substitute the point $(1; y)$ to solve for the base $b$.",
            "3_breakdown": f"Result: ${res_eq}$.",
        },
        misconception_tags=["algebra_error_solving_exponential_base"],
        keywords=["exponential", "determine equation", "asymptote", "base"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=3,
        mode="30_exponential_equation_from_asymptote_and_point",
        difficulty="medium",
        diagram_spec=d_spec,
    )


# ---------------------------------------------------------------------------
# 31. Exponential: Reflection in x-axis
# ---------------------------------------------------------------------------
def build_31_exponential_reflection_in_x_axis(r: random.Random) -> Dict[str, Any]:
    b = r.choice([2, 3])
    q = r.choice([-3, 2, 5])
    q_str = f"+ {q}" if q > 0 else f"- {abs(q)}"
    neg_q = -q
    neg_q_str = f"+ {neg_q}" if neg_q > 0 else f"- {abs(neg_q)}"
    res_eq = rf"y = -{b}^x {neg_q_str}"

    prompt = (
        f"Write down the equation of the function obtained when $f(x) = {b}^x {q_str}$ "
        f"is reflected across the $x$-axis."
    )
    ans_latex = res_eq
    sample = (
        rf"\text{{Reflection across the }} x\text{{-axis is }} y = -f(x):\\"
        rf"y = -({b}^x {q_str}) = -{b}^x {neg_q_str}"
    )

    return make_math_question(
        prefix="func_31",
        topic=TOPIC,
        subskill="31_exponential_reflection_in_x_axis",
        learning_objective_id=f"{LO_PREFIX}_exp_refl_x",
        prompt=prompt,
        prompt_latex=rf"f(x) = {b}^x {q_str}",
        answer_latex=ans_latex,
        answer_sympy=res_eq,
        sample_answer=sample,
        marking_schema={
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Multiplied entire function by -1", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Correct equation: {res_eq}", "marks": 1, "editable": True},
            ],
            "deductions": [{"rule": "forgot_to_reflect_asymptote", "penalty": -1}],
            "carry_forward_rule": "strict",
        },
        hints={
            "1_nudge": "Reflection in the $x$-axis replaces $y$ with $-y$, meaning $y = -f(x)$.",
            "2_concept": "Ensure you negate both the exponential term AND the vertical shift $q$.",
            "3_breakdown": f"Result: ${res_eq}$.",
        },
        misconception_tags=["forgot_to_distribute_negative_to_asymptote"],
        keywords=["exponential", "reflection", "x-axis"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=2,
        mode="31_exponential_reflection_in_x_axis",
        difficulty="medium",
    )


# ---------------------------------------------------------------------------
# 32. Exponential: Reflection in y-axis
# ---------------------------------------------------------------------------
def build_32_exponential_reflection_in_y_axis(r: random.Random) -> Dict[str, Any]:
    b = r.choice([2, 3])
    q = r.choice([-4, 1, 3])
    q_str = f"+ {q}" if q > 0 else f"- {abs(q)}"
    res_eq = rf"y = {b}^{{-x}} {q_str}"

    prompt = (
        f"Write down the equation of the function obtained when $f(x) = {b}^x {q_str}$ "
        f"is reflected across the $y$-axis."
    )
    ans_latex = res_eq
    sample = (
        rf"\text{{Reflection across the }} y\text{{-axis is }} y = f(-x):\\"
        rf"y = {b}^{{-x}} {q_str} \quad \text{{or}} \quad y = \left(\frac{{1}}{{{b}}}\right)^x {q_str}"
    )

    return make_math_question(
        prefix="func_32",
        topic=TOPIC,
        subskill="32_exponential_reflection_in_y_axis",
        learning_objective_id=f"{LO_PREFIX}_exp_refl_y",
        prompt=prompt,
        prompt_latex=rf"f(x) = {b}^x {q_str}",
        answer_latex=ans_latex,
        answer_sympy=res_eq,
        sample_answer=sample,
        marking_schema={
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Replaced x with -x", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Correct equation: {res_eq}", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "strict",
        },
        hints={
            "1_nudge": "Reflection in the $y$-axis replaces $x$ with $-x$.",
            "2_concept": "$f(-x) = b^{-x} + q$.",
            "3_breakdown": f"Result: ${res_eq}$.",
        },
        misconception_tags=["confused_reflection_in_axes"],
        keywords=["exponential", "reflection", "y-axis"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=2,
        mode="32_exponential_reflection_in_y_axis",
        difficulty="medium",
    )


# ---------------------------------------------------------------------------
# 33. Trig Graph: Sine Amplitude
# ---------------------------------------------------------------------------
def build_33_trig_graph_sine_amplitude(r: random.Random) -> Dict[str, Any]:
    a = r.choice([-3, -2, 2, 4])
    k = r.choice([1, 2, 3])
    k_str = f"{k}" if k > 1 else ""
    eq_latex = rf"y = {a}\sin({k_str}x)"

    prompt = f"State the amplitude of the trigonometric function ${eq_latex}$."
    ans_latex = str(abs(a))
    sample = (
        rf"\text{{The amplitude is }} |a| = |{a}| = {abs(a)}.\\"
        rf"\text{{Amplitude is always a positive distance.}}"
    )

    return make_math_question(
        prefix="func_33",
        topic=TOPIC,
        subskill="33_trig_graph_sine_amplitude",
        learning_objective_id=f"{LO_PREFIX}_sine_amp",
        prompt=prompt,
        prompt_latex=eq_latex,
        answer_latex=ans_latex,
        answer_sympy=str(abs(a)),
        sample_answer=sample,
        marking_schema={
            "total_marks": 1,
            "marking_points": [
                {"id": "mp1", "desc": f"Correct positive amplitude: {abs(a)}", "marks": 1, "editable": True},
            ],
            "deductions": [{"rule": "negative_amplitude_error", "penalty": -1}],
            "carry_forward_rule": "strict",
        },
        hints={
            "1_nudge": "Amplitude is the distance from the centerline to the crest.",
            "2_concept": "Amplitude is always positive: $\\text{Amplitude} = |a|$.",
            "3_breakdown": f"Amplitude is $|{a}| = {abs(a)}$.",
        },
        misconception_tags=["negative_amplitude"],
        keywords=["trigonometric graphs", "sine", "amplitude"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=1,
        mode="33_trig_graph_sine_amplitude",
        difficulty="easy",
    )


# ---------------------------------------------------------------------------
# 34. Trig Graph: Sine Period
# ---------------------------------------------------------------------------
def build_34_trig_graph_sine_period(r: random.Random) -> Dict[str, Any]:
    k = r.choice([2, 3, 4])
    a = r.choice([1, 2, 3])
    period = 360 // k
    eq_latex = rf"y = {a}\sin({k}x)"

    prompt = f"Calculate the period of the trigonometric function ${eq_latex}$."
    ans_latex = rf"{period}^\circ"
    sample = (
        rf"\text{{Period of sine is }} \frac{{360^\circ}}{{k}}:\\"
        rf"\text{{Period}} = \frac{{360^\circ}}{{{k}}} = {period}^\circ"
    )

    return make_math_question(
        prefix="func_34",
        topic=TOPIC,
        subskill="34_trig_graph_sine_period",
        learning_objective_id=f"{LO_PREFIX}_sine_period",
        prompt=prompt,
        prompt_latex=eq_latex,
        answer_latex=ans_latex,
        answer_sympy=str(period),
        sample_answer=sample,
        marking_schema={
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Formula: Period = 360 / k", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Correct period: {period} deg", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "strict",
        },
        hints={
            "1_nudge": "The mother sine graph has period $360^\\circ$. Divide by the coefficient of $x$.",
            "2_concept": "$\\text{Period} = \\frac{360^\\circ}{k}$.",
            "3_breakdown": f"$\\text{{Period}} = \\frac{{360^\\circ}}{{{k}}} = {period}^\\circ$.",
        },
        misconception_tags=["multiplied_by_k_instead_of_dividing"],
        keywords=["trigonometric graphs", "sine", "period"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=2,
        mode="34_trig_graph_sine_period",
        difficulty="easy",
    )


# ---------------------------------------------------------------------------
# 35. Trig Graph: Cosine Amplitude
# ---------------------------------------------------------------------------
def build_35_trig_graph_cosine_amplitude(r: random.Random) -> Dict[str, Any]:
    a = r.choice([-4, -3, 2, 5])
    eq_latex = rf"y = {a}\cos(x)"

    prompt = f"State the amplitude of the function ${eq_latex}$."
    ans_latex = str(abs(a))
    sample = (
        rf"\text{{Amplitude is }} |a| = |{a}| = {abs(a)}"
    )

    return make_math_question(
        prefix="func_35",
        topic=TOPIC,
        subskill="35_trig_graph_cosine_amplitude",
        learning_objective_id=f"{LO_PREFIX}_cos_amp",
        prompt=prompt,
        prompt_latex=eq_latex,
        answer_latex=ans_latex,
        answer_sympy=str(abs(a)),
        sample_answer=sample,
        marking_schema={
            "total_marks": 1,
            "marking_points": [
                {"id": "mp1", "desc": f"Correct amplitude: {abs(a)}", "marks": 1, "editable": True},
            ],
            "deductions": [{"rule": "negative_amplitude_error", "penalty": -1}],
            "carry_forward_rule": "strict",
        },
        hints={
            "1_nudge": "Amplitude must always be a non-negative number.",
            "2_concept": "$\\text{Amplitude} = |a|$.",
            "3_breakdown": f"Amplitude is ${abs(a)}$.",
        },
        misconception_tags=["negative_amplitude"],
        keywords=["trigonometric graphs", "cosine", "amplitude"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=1,
        mode="35_trig_graph_cosine_amplitude",
        difficulty="easy",
    )


# ---------------------------------------------------------------------------
# 36. Trig Graph: Cosine Period
# ---------------------------------------------------------------------------
def build_36_trig_graph_cosine_period(r: random.Random) -> Dict[str, Any]:
    k = r.choice([2, 3, 6])
    period = 360 // k
    eq_latex = rf"y = \cos({k}x)"

    prompt = f"Calculate the period of the cosine function ${eq_latex}$."
    ans_latex = rf"{period}^\circ"
    sample = (
        rf"\text{{Period}} = \frac{{360^\circ}}{{{k}}} = {period}^\circ"
    )

    return make_math_question(
        prefix="func_36",
        topic=TOPIC,
        subskill="36_trig_graph_cosine_period",
        learning_objective_id=f"{LO_PREFIX}_cos_period",
        prompt=prompt,
        prompt_latex=eq_latex,
        answer_latex=ans_latex,
        answer_sympy=str(period),
        sample_answer=sample,
        marking_schema={
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Setup 360 / k", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Correct period: {period} deg", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "strict",
        },
        hints={
            "1_nudge": "Use $\\text{Period} = \\frac{360^\\circ}{k}$.",
            "2_concept": "The coefficient of $x$ is $k = " + str(k) + "$.",
            "3_breakdown": f"Period is ${period}^\\circ$.",
        },
        misconception_tags=["confused_period_formula"],
        keywords=["trigonometric graphs", "cosine", "period"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=2,
        mode="36_trig_graph_cosine_period",
        difficulty="easy",
    )


# ---------------------------------------------------------------------------
# 37. Trig Graph: Tangent Period
# ---------------------------------------------------------------------------
def build_37_trig_graph_tangent_period(r: random.Random) -> Dict[str, Any]:
    k = r.choice([2, 3])
    period = 180 // k
    eq_latex = rf"y = \tan({k}x)"

    prompt = f"Calculate the period of the tangent function ${eq_latex}$."
    ans_latex = rf"{period}^\circ"
    sample = (
        rf"\text{{The mother tangent graph has period }} 180^\circ:\\"
        rf"\text{{Period}} = \frac{{180^\circ}}{{{k}}} = {period}^\circ"
    )

    return make_math_question(
        prefix="func_37",
        topic=TOPIC,
        subskill="37_trig_graph_tangent_period",
        learning_objective_id=f"{LO_PREFIX}_tan_period",
        prompt=prompt,
        prompt_latex=eq_latex,
        answer_latex=ans_latex,
        answer_sympy=str(period),
        sample_answer=sample,
        marking_schema={
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Used 180 deg base period for tangent", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Correct period: {period} deg", "marks": 1, "editable": True},
            ],
            "deductions": [{"rule": "used_360_for_tan_period", "penalty": -1}],
            "carry_forward_rule": "strict",
        },
        hints={
            "1_nudge": "WARNING: Tangent has a base period of $180^\\circ$, not $360^\\circ$!",
            "2_concept": "$\\text{Period} = \\frac{180^\\circ}{k}$.",
            "3_breakdown": f"$\\text{{Period}} = \\frac{{180^\\circ}}{{{k}}} = {period}^\\circ$.",
        },
        misconception_tags=["used_360_for_tan_period"],
        keywords=["trigonometric graphs", "tangent", "period"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=2,
        mode="37_trig_graph_tangent_period",
        difficulty="easy",
    )


# ---------------------------------------------------------------------------
# 38. Trig Graph: Range of Sine and Cosine
# ---------------------------------------------------------------------------
def build_38_trig_graph_range_sine_cosine(r: random.Random) -> Dict[str, Any]:
    a = r.choice([2, 3, 4])
    q = r.choice([-2, -1, 1, 2])
    min_val = q - a
    max_val = q + a
    q_str = f"+ {q}" if q > 0 else f"- {abs(q)}"
    eq_latex = rf"f(x) = {a}\sin x {q_str}"

    prompt = f"Determine the range of the trigonometric function ${eq_latex}$."
    ans_latex = rf"y \in [{min_val}; {max_val}]"
    sample = (
        rf"\text{{Since }} -1 \le \sin x \le 1:\\"
        rf"-{a} \le {a}\sin x \le {a}\\"
        rf"-{a} {q_str} \le {a}\sin x {q_str} \le {a} {q_str}\\"
        rf"{min_val} \le y \le {max_val}\\"
        rf"\therefore \text{{Range: }} y \in [{min_val}; {max_val}]"
    )

    return make_math_question(
        prefix="func_38",
        topic=TOPIC,
        subskill="38_trig_graph_range_sine_cosine",
        learning_objective_id=f"{LO_PREFIX}_trig_range",
        prompt=prompt,
        prompt_latex=eq_latex,
        answer_latex=ans_latex,
        answer_sympy=ans_latex,
        sample_answer=sample,
        marking_schema={
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": f"Minimum value: {min_val}", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Maximum value: {max_val}", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "strict",
        },
        hints={
            "1_nudge": "The mother sine wave ranges from $-1$ to $1$. Multiply by amplitude and shift by $q$.",
            "2_concept": "$\\text{Range} = [q - a; q + a]$.",
            "3_breakdown": f"Range: $[{min_val}; {max_val}]$.",
        },
        misconception_tags=["omitted_vertical_shift_in_range"],
        keywords=["trigonometric graphs", "range", "amplitude", "vertical shift"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=2,
        mode="38_trig_graph_range_sine_cosine",
        difficulty="medium",
    )


# ---------------------------------------------------------------------------
# 39. Trig Graph: Vertical Shift
# ---------------------------------------------------------------------------
def build_39_trig_graph_vertical_shift(r: random.Random) -> Dict[str, Any]:
    a = r.choice([2, 3])
    q = r.choice([-3, -1, 1, 3])
    q_str = f"+ {q}" if q > 0 else f"- {abs(q)}"
    eq_latex = rf"g(x) = {a}\cos x {q_str}"

    prompt = f"Write down the equation of the central axis (line of oscillation) for ${eq_latex}$."
    ans_latex = rf"y = {q}"
    sample = (
        rf"\text{{The central axis is given by the vertical shift: }} y = q\\ "
        rf"\therefore y = {q}"
    )

    return make_math_question(
        prefix="func_39",
        topic=TOPIC,
        subskill="39_trig_graph_vertical_shift",
        learning_objective_id=f"{LO_PREFIX}_central_axis",
        prompt=prompt,
        prompt_latex=eq_latex,
        answer_latex=ans_latex,
        answer_sympy=f"y = {q}",
        sample_answer=sample,
        marking_schema={
            "total_marks": 1,
            "marking_points": [
                {"id": "mp1", "desc": f"Correct equation: y = {q}", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "strict",
        },
        hints={
            "1_nudge": "The line midway between the crests and troughs is the central line $y = q$.",
            "2_concept": "Central axis equation is $y = q$.",
            "3_breakdown": f"Equation: $y = {q}$.",
        },
        misconception_tags=["wrote_x_for_central_axis"],
        keywords=["trigonometric graphs", "central axis", "vertical shift"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=1,
        mode="39_trig_graph_vertical_shift",
        difficulty="easy",
    )


# ---------------------------------------------------------------------------
# 40. Trig Graph: Determine Equation of Sine from Graph (with inline_svg)
# ---------------------------------------------------------------------------
def build_40_trig_graph_determine_equation_sine(r: random.Random) -> Dict[str, Any]:
    a = r.choice([2, 3])
    q = r.choice([-1, 0, 1])

    d_spec = _trig_wave_svg(a=float(a), k=1.0, q=float(q), fn="sin")
    q_str = f"+ {q}" if q > 0 else (f"- {abs(q)}" if q < 0 else "")
    res_eq = rf"y = {a}\sin x {q_str}".strip()

    prompt = (
        f"In the graph shown, a sine curve has maximum value ${q + a}$ and minimum value ${q - a}$. "
        f"The period is $360^\\circ$.\n\n"
        f"Determine the values of $a$ and $q$ in the equation $y = a\\sin x + q$."
    )
    sample = (
        rf"a = \frac{{\text{{max}} - \text{{min}}}}{{2}} = \frac{{{q + a} - ({q - a})}}{{2}} = \frac{{{2*a}}}{{2}} = {a}\\"
        rf"q = \frac{{\text{{max}} + \text{{min}}}}{{2}} = \frac{{{q + a} + ({q - a})}}{{2}} = {q}\\"
        rf"\therefore a = {a}, \; q = {q}"
    )

    return make_math_question(
        prefix="func_40",
        topic=TOPIC,
        subskill="40_trig_graph_determine_equation_sine",
        learning_objective_id=f"{LO_PREFIX}_sine_eq_graph",
        prompt=prompt,
        prompt_latex=rf"\text{{max}} = {q + a}, \; \text{{min}} = {q - a}",
        answer_latex=rf"a = {a}, \; q = {q}",
        answer_sympy=f"a = {a}, q = {q}",
        sample_answer=sample,
        marking_schema={
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": f"Calculated amplitude a = {a}", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Calculated vertical shift q = {q}", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Full statement a = {a}, q = {q}", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        hints={
            "1_nudge": "Use the formulas: $a = \\frac{\\text{max} - \\text{min}}{2}$ and $q = \\frac{\\text{max} + \\text{min}}{2}$.",
            "2_concept": "Amplitude is half the total height.",
            "3_breakdown": f"$a = {a}$, $q = {q}$.",
        },
        misconception_tags=["amplitude_calculation_error"],
        keywords=["trigonometric graphs", "determine equation", "sine"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=3,
        mode="40_trig_graph_determine_equation_sine",
        difficulty="medium",
        diagram_spec=d_spec,
    )


# ---------------------------------------------------------------------------
# 41. Trig Graph: Determine Equation of Cosine from Graph (with inline_svg)
# ---------------------------------------------------------------------------
def build_41_trig_graph_determine_equation_cosine(r: random.Random) -> Dict[str, Any]:
    a = r.choice([2, 4])
    q = r.choice([-2, 0, 2])

    d_spec = _trig_wave_svg(a=float(a), k=1.0, q=float(q), fn="cos")
    prompt = (
        f"In the graph shown, a cosine curve has maximum value ${q + a}$ and minimum value ${q - a}$. "
        f"The curve intersects the $y$-axis at $(0; {q + a})$.\n\n"
        f"Determine the values of $a$ and $q$ in $y = a\\cos x + q$."
    )
    ans_latex = rf"a = {a}, \; q = {q}"
    sample = (
        rf"a = \frac{{{q + a} - ({q - a})}}{{2}} = {a}\\"
        rf"q = \frac{{{q + a} + ({q - a})}}{{2}} = {q}\\"
        rf"\therefore a = {a}, \; q = {q}"
    )

    return make_math_question(
        prefix="func_41",
        topic=TOPIC,
        subskill="41_trig_graph_determine_equation_cosine",
        learning_objective_id=f"{LO_PREFIX}_cos_eq_graph",
        prompt=prompt,
        prompt_latex=rf"\text{{max}} = {q + a}, \; \text{{min}} = {q - a}",
        answer_latex=ans_latex,
        answer_sympy=f"a = {a}, q = {q}",
        sample_answer=sample,
        marking_schema={
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": f"Calculated amplitude a = {a}", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Calculated vertical shift q = {q}", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Stated a = {a}, q = {q}", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        hints={
            "1_nudge": "Amplitude is half the vertical distance between maximum and minimum.",
            "2_concept": "Vertical shift is the midpoint between maximum and minimum.",
            "3_breakdown": f"$a = {a}$, $q = {q}$.",
        },
        misconception_tags=["amplitude_calculation_error"],
        keywords=["trigonometric graphs", "determine equation", "cosine"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=3,
        mode="41_trig_graph_determine_equation_cosine",
        difficulty="medium",
        diagram_spec=d_spec,
    )


# ---------------------------------------------------------------------------
# 42. Trig Graph: Phase Shift Horizontal
# ---------------------------------------------------------------------------
def build_42_trig_graph_phase_shift_horizontal(r: random.Random) -> Dict[str, Any]:
    p_deg = r.choice([30, 45, 60])
    sign = r.choice(["+", "-"])
    dir_str = "left" if sign == "+" else "right"
    eq_latex = rf"y = \sin(x {sign} {p_deg}^\circ)"

    prompt = (
        f"Describe the horizontal phase shift that transforms $y = \\sin x$ onto "
        f"${eq_latex}$."
    )
    ans_latex = rf"\text{{Shifted }} {p_deg}^\circ \text{{ to the {dir_str}}}"
    sample = (
        rf"\text{{The argument }} (x {sign} {p_deg}^\circ) \text{{ indicates a horizontal phase shift of }}\\"
        rf"{p_deg}^\circ \text{{ to the {dir_str}.}}"
    )

    return make_math_question(
        prefix="func_42",
        topic=TOPIC,
        subskill="42_trig_graph_phase_shift_horizontal",
        learning_objective_id=f"{LO_PREFIX}_phase_shift",
        prompt=prompt,
        prompt_latex=eq_latex,
        answer_latex=ans_latex,
        answer_sympy=ans_latex,
        sample_answer=sample,
        marking_schema={
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": f"Correct magnitude: {p_deg} deg", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Correct direction: {dir_str}", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "strict",
        },
        hints={
            "1_nudge": "$(x + p)$ shifts the graph to the left; $(x - p)$ shifts it to the right.",
            "2_concept": "Set $x \\pm p = 0$ to find where the origin shifts.",
            "3_breakdown": f"Shifted {p_deg}$^\\circ$ to the {dir_str}.",
        },
        misconception_tags=["inverted_phase_shift_direction"],
        keywords=["trigonometric graphs", "phase shift", "horizontal translation"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=2,
        mode="42_trig_graph_phase_shift_horizontal",
        difficulty="easy",
    )


# ---------------------------------------------------------------------------
# 43. Graph Interpretation: f(x) > 0
# ---------------------------------------------------------------------------
def build_43_graph_interpretation_f_greater_than_zero(r: random.Random) -> Dict[str, Any]:
    # Parabola opening down with roots at -3 and 2: f(x) = -(x+3)(x-2) = -x^2 - x + 6
    # f(x) > 0 between the roots: -3 < x < 2
    r1, r2 = -3, 2
    prompt = (
        f"Given the parabola $f(x) = -x^2 - x + 6$, determine the values of $x$ for which "
        f"$f(x) > 0$."
    )
    ans_latex = rf"-3 < x < 2 \quad \text{{or}} \quad x \in (-3; 2)"
    sample = (
        rf"\text{{Find the roots: }} -x^2 - x + 6 = 0 \implies x^2 + x - 6 = 0\\"
        rf"(x + 3)(x - 2) = 0 \implies x = -3 \text{{ or }} x = 2\\"
        rf"\text{{Since the parabola opens downwards (a < 0), the graph lies above the }} x\text{{-axis between the roots:}}\\"
        rf"\therefore -3 < x < 2"
    )

    return make_math_question(
        prefix="func_43",
        topic=TOPIC,
        subskill="43_graph_interpretation_f_greater_than_zero",
        learning_objective_id=f"{LO_PREFIX}_f_gt_zero",
        prompt=prompt,
        prompt_latex=r"f(x) = -x^2 - x + 6, \; f(x) > 0",
        answer_latex=ans_latex,
        answer_sympy="-3 < x < 2",
        sample_answer=sample,
        marking_schema={
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": "Calculated roots x = -3 and x = 2", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Identified downward concavity", "marks": 1, "editable": True},
                {"id": "mp3", "desc": "Correct interval: -3 < x < 2", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        hints={
            "1_nudge": "Find where $f(x) = 0$ first to get the critical values.",
            "2_concept": "Since $a = -1 < 0$, the parabola is concave down, so it is positive between the two roots.",
            "3_breakdown": "Interval is $-3 < x < 2$.",
        },
        misconception_tags=["inverted_inequality_interval"],
        keywords=["graph interpretation", "inequalities", "roots"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=3,
        mode="43_graph_interpretation_f_greater_than_zero",
        difficulty="medium",
    )


# ---------------------------------------------------------------------------
# 44. Graph Interpretation: f(x) * g(x) <= 0
# ---------------------------------------------------------------------------
def build_44_graph_interpretation_f_times_g_nonpositive(r: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Consider two functions $f$ and $g$ where $f(x) \\ge 0$ for $x \\in [-2; 4]$ and "
        f"$g(x) \\ge 0$ for $x \\ge 1$.\n\n"
        f"Determine the values of $x$ for which $f(x) \\cdot g(x) \\le 0$."
    )
    ans_latex = r"x \in [-2; 1] \cup [4; \infty)"
    sample = (
        rf"\text{{The product }} f(x) \cdot g(x) \le 0 \text{{ when }} f \text{{ and }} g \text{{ have opposite signs (or zero):}}\\"
        rf"\text{{Case 1: }} f(x) \ge 0 \text{{ and }} g(x) \le 0 \implies x \in [-2; 4] \cap x \le 1 = [-2; 1]\\"
        rf"\text{{Case 2: }} f(x) \le 0 \text{{ and }} g(x) \ge 0 \implies (x \le -2 \text{{ or }} x \ge 4) \cap x \ge 1 = [4; \infty)\\"
        rf"\therefore x \in [-2; 1] \cup [4; \infty)"
    )

    return make_math_question(
        prefix="func_44",
        topic=TOPIC,
        subskill="44_graph_interpretation_f_times_g_nonpositive",
        learning_objective_id=f"{LO_PREFIX}_f_times_g",
        prompt=prompt,
        prompt_latex=r"f(x) \cdot g(x) \le 0",
        answer_latex=ans_latex,
        answer_sympy=ans_latex,
        sample_answer=sample,
        marking_schema={
            "total_marks": 4,
            "marking_points": [
                {"id": "mp1", "desc": "Identified condition: opposite signs or zero", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Branch 1: [-2; 1]", "marks": 1, "editable": True},
                {"id": "mp3", "desc": "Branch 2: [4; inf)", "marks": 1, "editable": True},
                {"id": "mp4", "desc": "Combined solution with correct bracket notation", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        hints={
            "1_nudge": "A product of two numbers is negative when one is positive and the other is negative.",
            "2_concept": "Check where one graph is on/above the $x$-axis while the other is on/below the $x$-axis.",
            "3_breakdown": "Solutions: $[-2; 1] \\cup [4; \\infty)$.",
        },
        misconception_tags=["sign_chart_error"],
        keywords=["product of functions", "graph interpretation", "intervals"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=4,
        mode="44_graph_interpretation_f_times_g_nonpositive",
        difficulty="hard",
    )


# ---------------------------------------------------------------------------
# 45. Graph Interpretation: f(x) >= g(x)
# ---------------------------------------------------------------------------
def build_45_graph_interpretation_f_greater_than_g(r: random.Random) -> Dict[str, Any]:
    # f(x) = -x^2 + 4, g(x) = x + 2
    # -x^2 + 4 = x + 2 => x^2 + x - 2 = 0 => (x + 2)(x - 1) = 0 => x = -2, 1
    prompt = (
        f"For the parabola $f(x) = -x^2 + 4$ and the line $g(x) = x + 2$, "
        f"determine the values of $x$ for which $f(x) \\ge g(x)$."
    )
    ans_latex = r"-2 \le x \le 1 \quad \text{or} \quad x \in [-2; 1]"
    sample = (
        rf"\text{{Find points of intersection: }}\\"
        rf"-x^2 + 4 = x + 2 \implies x^2 + x - 2 = 0\\"
        rf"(x + 2)(x - 1) = 0 \implies x = -2 \text{{ or }} x = 1\\"
        rf"\text{{Between }} x = -2 \text{{ and }} x = 1 \text{{, the parabola lies above the line.}}\\"
        rf"\therefore -2 \le x \le 1"
    )

    return make_math_question(
        prefix="func_45",
        topic=TOPIC,
        subskill="45_graph_interpretation_f_greater_than_g",
        learning_objective_id=f"{LO_PREFIX}_f_ge_g",
        prompt=prompt,
        prompt_latex=r"f(x) \ge g(x)",
        answer_latex=ans_latex,
        answer_sympy="-2 <= x <= 1",
        sample_answer=sample,
        marking_schema={
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": "Found intersection points x = -2 and x = 1", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Determined parabola is above line", "marks": 1, "editable": True},
                {"id": "mp3", "desc": "Correct inclusive inequality: -2 <= x <= 1", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        hints={
            "1_nudge": "Find the intersection points of $f(x)$ and $g(x)$ first.",
            "2_concept": "$f(x) \\ge g(x)$ means the graph of $f$ is on or above the graph of $g$.",
            "3_breakdown": "Interval is $[-2; 1]$.",
        },
        misconception_tags=["inverted_comparison_interval"],
        keywords=["graph comparison", "inequalities", "intersection"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=3,
        mode="45_graph_interpretation_f_greater_than_g",
        difficulty="medium",
    )


# ---------------------------------------------------------------------------
# 46. Graph Interpretation: Length of Vertical Distance
# ---------------------------------------------------------------------------
def build_46_graph_interpretation_length_vertical_distance(r: random.Random) -> Dict[str, Any]:
    x_val = r.choice([0, 1])
    # f(x) = -x^2 + 5, g(x) = 2x - 1
    f_val = -x_val**2 + 5
    g_val = 2 * x_val - 1
    dist = f_val - g_val

    prompt = (
        f"A vertical line $x = {x_val}$ intersects the parabola $f(x) = -x^2 + 5$ at point $A$ "
        f"and the straight line $g(x) = 2x - 1$ at point $B$.\n\n"
        f"Calculate the length of the segment $AB$."
    )
    ans_latex = rf"{dist} \text{{ units}}"
    sample = (
        rf"y_A = f({x_val}) = -({x_val})^2 + 5 = {f_val}\\"
        rf"y_B = g({x_val}) = 2({x_val}) - 1 = {g_val}\\"
        rf"AB = y_A - y_B = {f_val} - ({g_val}) = {dist}\text{{ units}}"
    )

    return make_math_question(
        prefix="func_46",
        topic=TOPIC,
        subskill="46_graph_interpretation_length_vertical_distance",
        learning_objective_id=f"{LO_PREFIX}_vert_distance",
        prompt=prompt,
        prompt_latex=rf"x = {x_val}, \; AB = f({x_val}) - g({x_val})",
        answer_latex=ans_latex,
        answer_sympy=str(dist),
        sample_answer=sample,
        marking_schema={
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": f"Calculated y_A = {f_val}", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Calculated y_B = {g_val}", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Length AB = {dist} units", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        hints={
            "1_nudge": "Find the $y$-value on each graph at the given $x$-coordinate.",
            "2_concept": "Vertical distance is $\\text{top } y - \\text{bottom } y$.",
            "3_breakdown": f"$AB = {f_val} - ({g_val}) = {dist}$ units.",
        },
        misconception_tags=["subtracted_in_reverse_giving_negative_length"],
        keywords=["vertical distance", "length of segment", "functions"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=3,
        mode="46_graph_interpretation_length_vertical_distance",
        difficulty="medium",
    )


# ---------------------------------------------------------------------------
# 47. Graph Interpretation: Maximum Vertical Distance
# ---------------------------------------------------------------------------
def build_47_graph_interpretation_maximum_vertical_distance(r: random.Random) -> Dict[str, Any]:
    # f(x) = -x^2 + 4, g(x) = -2x - 1
    # D(x) = f(x) - g(x) = -x^2 + 4 - (-2x - 1) = -x^2 + 2x + 5
    # Max at x = -b/(2a) = -2 / (-2) = 1
    # Max D(1) = -(1)^2 + 2(1) + 5 = 6
    prompt = (
        f"A vertical line parallel to the $y$-axis cuts the parabola $f(x) = -x^2 + 4$ at point $A$ "
        f"and the line $g(x) = -2x - 1$ at point $B$, where $A$ lies above $B$.\n\n"
        f"Calculate the maximum length of segment $AB$."
    )
    ans_latex = r"6 \text{ units (at } x = 1\text{)}"
    sample = (
        rf"AB(x) = f(x) - g(x) = (-x^2 + 4) - (-2x - 1) = -x^2 + 2x + 5\\"
        rf"\text{{Maximum occurs at the turning point of }} AB(x):\\"
        rf"x = -\frac{{b}}{{2a}} = -\frac{{2}}{{2(-1)}} = 1\\"
        rf"\text{{Maximum length}} = -(1)^2 + 2(1) + 5 = 6\text{{ units}}"
    )

    return make_math_question(
        prefix="func_47",
        topic=TOPIC,
        subskill="47_graph_interpretation_maximum_vertical_distance",
        learning_objective_id=f"{LO_PREFIX}_max_vert_dist",
        prompt=prompt,
        prompt_latex=r"AB(x) = f(x) - g(x)",
        answer_latex=ans_latex,
        answer_sympy="6",
        sample_answer=sample,
        marking_schema={
            "total_marks": 4,
            "marking_points": [
                {"id": "mp1", "desc": "Subtracted g(x) from f(x) to form -x^2 + 2x + 5", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Found x = 1 using x = -b/(2a)", "marks": 1, "editable": True},
                {"id": "mp3", "desc": "Substituted x = 1 into expression", "marks": 1, "editable": True},
                {"id": "mp4", "desc": "Maximum length = 6 units", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        hints={
            "1_nudge": "Create a new function $D(x) = f(x) - g(x)$ for the vertical distance.",
            "2_concept": "Find the maximum of this quadratic function using the turning point formula $x = -\\frac{b}{2a}$.",
            "3_breakdown": "Max distance is $6$ units at $x = 1$.",
        },
        misconception_tags=["sign_error_subtracting_linear_equation"],
        keywords=["maximum distance", "optimization", "vertical segment", "turning point"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=4,
        mode="47_graph_interpretation_maximum_vertical_distance",
        difficulty="hard",
    )


# ---------------------------------------------------------------------------
# 48. Graph Translation: Vertical Shift f(x) + c
# ---------------------------------------------------------------------------
def build_48_graph_translation_vertical(r: random.Random) -> Dict[str, Any]:
    c = r.choice([2, 3, 4])
    prompt = (
        f"If $f(x) = 2x^2 - 3$, write down the equation of $h(x) = f(x) + {c}$ in simplified form."
    )
    new_c = -3 + c
    c_str = f"+ {new_c}" if new_c > 0 else (f"- {abs(new_c)}" if new_c < 0 else "")
    res_eq = rf"h(x) = 2x^2 {c_str}".strip()

    ans_latex = res_eq
    sample = (
        rf"h(x) = f(x) + {c} = (2x^2 - 3) + {c} = {res_eq}"
    )

    return make_math_question(
        prefix="func_48",
        topic=TOPIC,
        subskill="48_graph_translation_vertical",
        learning_objective_id=f"{LO_PREFIX}_trans_vert",
        prompt=prompt,
        prompt_latex=rf"f(x) = 2x^2 - 3, \; h(x) = f(x) + {c}",
        answer_latex=ans_latex,
        answer_sympy=res_eq,
        sample_answer=sample,
        marking_schema={
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": f"Added {c} to the expression", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Correct simplified equation: {res_eq}", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "strict",
        },
        hints={
            "1_nudge": f"Add {c} to the entire expression for $f(x)$.",
            "2_concept": "Vertical translation: $f(x) + c$ shifts the curve up by $c$ units.",
            "3_breakdown": f"Result: ${res_eq}$.",
        },
        misconception_tags=["arithmetic_error_combining_constants"],
        keywords=["translation", "vertical shift", "algebraic transformation"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=2,
        mode="48_graph_translation_vertical",
        difficulty="easy",
    )


# ---------------------------------------------------------------------------
# 49. Graph Translation: Horizontal Shift f(x - d)
# ---------------------------------------------------------------------------
def build_49_graph_translation_horizontal(r: random.Random) -> Dict[str, Any]:
    d = r.choice([1, 2, 3])
    prompt = (
        f"If $f(x) = x^2$, write down the equation of $g(x) = f(x - {d})$."
    )
    res_eq = rf"g(x) = (x - {d})^2"
    sample = (
        rf"g(x) = f(x - {d}) = (x - {d})^2"
    )

    return make_math_question(
        prefix="func_49",
        topic=TOPIC,
        subskill="49_graph_translation_horizontal",
        learning_objective_id=f"{LO_PREFIX}_trans_horiz",
        prompt=prompt,
        prompt_latex=rf"f(x) = x^2, \; g(x) = f(x - {d})",
        answer_latex=res_eq,
        answer_sympy=res_eq,
        sample_answer=sample,
        marking_schema={
            "total_marks": 1,
            "marking_points": [
                {"id": "mp1", "desc": f"Correct equation: {res_eq}", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "strict",
        },
        hints={
            "1_nudge": "Replace every $x$ in the equation with $(x - d)$.",
            "2_concept": "A horizontal shift replaces $x$ with $(x - d)$.",
            "3_breakdown": f"Result: ${res_eq}$.",
        },
        misconception_tags=["subtracted_d_outside_square"],
        keywords=["translation", "horizontal shift", "algebraic transformation"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=1,
        mode="49_graph_translation_horizontal",
        difficulty="easy",
    )


# ---------------------------------------------------------------------------
# 50. Composite Graph Interpretation Summary (with inline_svg)
# ---------------------------------------------------------------------------
def build_50_composite_graph_interpretation_summary(r: random.Random) -> Dict[str, Any]:
    h = r.choice([-2, -1, 1, 2])
    dist = r.choice([2, 3])
    k = dist * dist
    a = -1
    x1 = h - dist
    x2 = h + dist
    y_int = k - h * h

    d_spec = _cartesian_parabola_svg(
        a=float(a),
        h=float(h),
        k=float(k),
        tp_label="T",
        pt_x=0.0,
        pt_y=float(y_int),
    )
    h_str = f"+ {abs(h)}" if h < 0 else f"- {h}"
    eq_str = rf"f(x) = -(x {h_str})^2 + {k}"
    prompt = (
        f"In the accompanying graph, the parabola ${eq_str}$ has turning point $T({h}; {k})$ "
        f"and $y$-intercept at $(0; {y_int})$.\n\n"
        f"1. Write down the range of $f$.\n"
        f"2. Determine the coordinates of the $x$-intercepts of $f$."
    )
    ans_latex = rf"y \le {k}, \; ({x1}; 0) \text{{ and }} ({x2}; 0)"
    sample = (
        rf"1. \text{{Range: Since }} a = -1 < 0, \; y \le {k}\\"
        rf"2. \text{{x-intercepts: }} -(x {h_str})^2 + {k} = 0 \implies (x {h_str})^2 = {k}\\"
        rf"x {h_str} = \pm {dist} \implies x = {x2} \text{{ or }} x = {x1}\\"
        rf"\therefore ({x1}; 0) \text{{ and }} ({x2}; 0)"
    )

    return make_math_question(
        prefix="func_50",
        topic=TOPIC,
        subskill="50_composite_graph_interpretation_summary",
        learning_objective_id=f"{LO_PREFIX}_summary_composite",
        prompt=prompt,
        prompt_latex=eq_str,
        answer_latex=ans_latex,
        answer_sympy=ans_latex,
        sample_answer=sample,
        marking_schema={
            "total_marks": 4,
            "marking_points": [
                {"id": "mp1", "desc": f"Range: y <= {k}", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Set equation equal to zero", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Solved for x-intercept 1: ({x1}; 0)", "marks": 1, "editable": True},
                {"id": "mp4", "desc": f"Solved for x-intercept 2: ({x2}; 0)", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        hints={
            "1_nudge": "The maximum $y$-value gives the range.",
            "2_concept": f"Solve $-({f'x {h_str}'})^2 + {k} = 0$ by taking square roots.",
            "3_breakdown": f"Range is $y \\le {k}$, $x$-intercepts are $({x1}; 0)$ and $({x2}; 0)$.",
        },
        misconception_tags=["sign_error_square_root_roots"],
        keywords=["parabola", "comprehensive interpretation", "range", "x-intercepts"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=4,
        mode="50_composite_graph_interpretation_summary",
        difficulty="hard",
        diagram_spec=d_spec,
    )


# ---------------------------------------------------------------------------
# Registry Map of Archetypes 26–50
# ---------------------------------------------------------------------------
ARCHETYPES_26_50 = {
    "26_exponential_horizontal_asymptote": build_26_exponential_horizontal_asymptote,
    "27_exponential_y_intercept": build_27_exponential_y_intercept,
    "28_exponential_domain_and_range": build_28_exponential_domain_and_range,
    "29_exponential_growth_vs_decay": build_29_exponential_growth_vs_decay,
    "30_exponential_equation_from_asymptote_and_point": build_30_exponential_equation_from_asymptote_and_point,
    "31_exponential_reflection_in_x_axis": build_31_exponential_reflection_in_x_axis,
    "32_exponential_reflection_in_y_axis": build_32_exponential_reflection_in_y_axis,
    "33_trig_graph_sine_amplitude": build_33_trig_graph_sine_amplitude,
    "34_trig_graph_sine_period": build_34_trig_graph_sine_period,
    "35_trig_graph_cosine_amplitude": build_35_trig_graph_cosine_amplitude,
    "36_trig_graph_cosine_period": build_36_trig_graph_cosine_period,
    "37_trig_graph_tangent_period": build_37_trig_graph_tangent_period,
    "38_trig_graph_range_sine_cosine": build_38_trig_graph_range_sine_cosine,
    "39_trig_graph_vertical_shift": build_39_trig_graph_vertical_shift,
    "40_trig_graph_determine_equation_sine": build_40_trig_graph_determine_equation_sine,
    "41_trig_graph_determine_equation_cosine": build_41_trig_graph_determine_equation_cosine,
    "42_trig_graph_phase_shift_horizontal": build_42_trig_graph_phase_shift_horizontal,
    "43_graph_interpretation_f_greater_than_zero": build_43_graph_interpretation_f_greater_than_zero,
    "44_graph_interpretation_f_times_g_nonpositive": build_44_graph_interpretation_f_times_g_nonpositive,
    "45_graph_interpretation_f_greater_than_g": build_45_graph_interpretation_f_greater_than_g,
    "46_graph_interpretation_length_vertical_distance": build_46_graph_interpretation_length_vertical_distance,
    "47_graph_interpretation_maximum_vertical_distance": build_47_graph_interpretation_maximum_vertical_distance,
    "48_graph_translation_vertical": build_48_graph_translation_vertical,
    "49_graph_translation_horizontal": build_49_graph_translation_horizontal,
    "50_composite_graph_interpretation_summary": build_50_composite_graph_interpretation_summary,
}
