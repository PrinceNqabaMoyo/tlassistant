"""Grade 11 Mathematics — Functions and Graphs Archetypes 01–25.
Grounded in South African National Curriculum Standards for Grade 11 Mathematics (Term 2).
Covers:
- Parabola: vertex form y = a(x + p)^2 + q and standard form y = ax^2 + bx + c
- Turning points, axis of symmetry, intercepts, domain, range, max/min values
- Determining equation of parabola from turning point/point or roots/point with inline_svg
- Hyperbola: y = a / (x + p) + q
- Vertical and horizontal asymptotes, center of symmetry, axes of symmetry (m = ±1)
- Hyperbola domain, range, intercepts, and equation determination with inline_svg
- Reflections, intervals of increase/decrease, intersections
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

TOPIC = "Functions and graphs"
LO_PREFIX = "math11_func"


def _cartesian_parabola_svg(
    a: float,
    h: float,
    k: float,
    tp_label: str = "T",
    pt_x: Optional[float] = None,
    pt_y: Optional[float] = None,
) -> Dict[str, Any]:
    """Generates an inline SVG showing Cartesian plane with plotted parabola y = a(x-h)^2 + k."""
    # Canvas 420x300, origin at (210, 150)
    ox, oy = 210, 150
    scale = 16.0

    # sample curve points
    pts = []
    for step_i in range(-25, 26):
        x_val = h + step_i * 0.25
        y_val = a * ((x_val - h) ** 2) + k
        sx = ox + x_val * scale
        sy = oy - y_val * scale
        if 15 <= sx <= 405 and 15 <= sy <= 285:
            pts.append(f"{sx:.1f},{sy:.1f}")

    polyline = " ".join(pts) if pts else f"{ox},{oy}"
    tpx = ox + h * scale
    tpy = oy - k * scale

    extra_point = ""
    if pt_x is not None and pt_y is not None:
        px = ox + pt_x * scale
        py = oy - pt_y * scale
        extra_point = (
            f'<circle cx="{px:.1f}" cy="{py:.1f}" r="4" fill="#059669"/>'
            f'<text x="{px + 6:.1f}" y="{py - 6:.1f}" font-size="12" fill="#065f46" font-weight="bold">({int(pt_x) if pt_x.is_integer() else pt_x}; {int(pt_y) if pt_y.is_integer() else pt_y})</text>'
        )

    svg = (
        f'<svg viewBox="0 0 420 300" width="100%" height="250" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="420" height="300" fill="#f8fafc" rx="8"/>'
        f'<line x1="20" y1="{oy}" x2="400" y2="{oy}" stroke="#64748b" stroke-width="2"/>'
        f'<line x1="{ox}" y1="280" x2="{ox}" y2="20" stroke="#64748b" stroke-width="2"/>'
        f'<text x="405" y="{oy + 4}" font-size="13" fill="#334155" font-weight="bold">x</text>'
        f'<text x="{ox - 5}" y="15" font-size="13" fill="#334155" font-weight="bold">y</text>'
        f'<polyline points="{polyline}" fill="none" stroke="#2563eb" stroke-width="2.5"/>'
        f'<circle cx="{tpx:.1f}" cy="{tpy:.1f}" r="4.5" fill="#dc2626"/>'
        f'<text x="{tpx + 7:.1f}" y="{tpy - 6:.1f}" font-size="12" fill="#991b1b" font-weight="bold">{tp_label}({int(h) if h.is_integer() else h}; {int(k) if k.is_integer() else k})</text>'
        f'{extra_point}'
        f'</svg>'
    )
    return {
        "kind": "inline_svg",
        "svg": svg,
        "diagram_role": "context",
        "vertex_x": h,
        "vertex_y": k,
    }


def _cartesian_hyperbola_svg(
    a: float,
    p: float,
    q: float,
    pt_x: Optional[float] = None,
    pt_y: Optional[float] = None,
) -> Dict[str, Any]:
    """Generates an inline SVG showing hyperbola y = a/(x+p) + q with asymptotes."""
    ox, oy = 210, 150
    scale = 14.0

    asymp_x_screen = ox - p * scale
    asymp_y_screen = oy - q * scale

    # Left and right branch polylines
    branch1_pts = []
    for step_i in range(-35, -1):
        x_val = -p + step_i * 0.2
        y_val = a / (x_val + p) + q
        sx = ox + x_val * scale
        sy = oy - y_val * scale
        if 15 <= sx <= 405 and 15 <= sy <= 285:
            branch1_pts.append(f"{sx:.1f},{sy:.1f}")

    branch2_pts = []
    for step_i in range(1, 36):
        x_val = -p + step_i * 0.2
        y_val = a / (x_val + p) + q
        sx = ox + x_val * scale
        sy = oy - y_val * scale
        if 15 <= sx <= 405 and 15 <= sy <= 285:
            branch2_pts.append(f"{sx:.1f},{sy:.1f}")

    p1 = " ".join(branch1_pts) if branch1_pts else f"{ox},{oy}"
    p2 = " ".join(branch2_pts) if branch2_pts else f"{ox},{oy}"

    extra_point = ""
    if pt_x is not None and pt_y is not None:
        px = ox + pt_x * scale
        py = oy - pt_y * scale
        extra_point = (
            f'<circle cx="{px:.1f}" cy="{py:.1f}" r="4" fill="#059669"/>'
            f'<text x="{px + 6:.1f}" y="{py - 6:.1f}" font-size="12" fill="#065f46" font-weight="bold">({int(pt_x) if pt_x.is_integer() else pt_x}; {int(pt_y) if pt_y.is_integer() else pt_y})</text>'
        )

    svg = (
        f'<svg viewBox="0 0 420 300" width="100%" height="250" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="420" height="300" fill="#f8fafc" rx="8"/>'
        # Axes
        f'<line x1="20" y1="{oy}" x2="400" y2="{oy}" stroke="#64748b" stroke-width="2"/>'
        f'<line x1="{ox}" y1="280" x2="{ox}" y2="20" stroke="#64748b" stroke-width="2"/>'
        f'<text x="405" y="{oy + 4}" font-size="13" fill="#334155" font-weight="bold">x</text>'
        f'<text x="{ox - 5}" y="15" font-size="13" fill="#334155" font-weight="bold">y</text>'
        # Vertical Asymptote x = -p
        f'<line x1="{asymp_x_screen:.1f}" y1="20" x2="{asymp_x_screen:.1f}" y2="280" stroke="#f59e0b" stroke-width="1.8" stroke-dasharray="5,4"/>'
        f'<text x="{asymp_x_screen + 4:.1f}" y="35" font-size="11" fill="#d97706">x = {-p}</text>'
        # Horizontal Asymptote y = q
        f'<line x1="20" y1="{asymp_y_screen:.1f}" x2="400" y2="{asymp_y_screen:.1f}" stroke="#f59e0b" stroke-width="1.8" stroke-dasharray="5,4"/>'
        f'<text x="25" y="{asymp_y_screen - 6:.1f}" font-size="11" fill="#d97706">y = {q}</text>'
        # Branches
        f'<polyline points="{p1}" fill="none" stroke="#2563eb" stroke-width="2.5"/>'
        f'<polyline points="{p2}" fill="none" stroke="#2563eb" stroke-width="2.5"/>'
        f'{extra_point}'
        f'</svg>'
    )
    return {
        "kind": "inline_svg",
        "svg": svg,
        "diagram_role": "context",
        "asymptote_x": -p,
        "asymptote_y": q,
    }


# ---------------------------------------------------------------------------
# 01. Parabola: Turning Point in Vertex Form y = a(x + p)^2 + q
# ---------------------------------------------------------------------------
def build_01_parabola_turning_point_vertex_form(r: random.Random) -> Dict[str, Any]:
    a = r.choice([-3, -2, -1, 1, 2, 3])
    p = r.choice([-4, -3, -2, -1, 1, 2, 3, 4])
    q = r.choice([-5, -3, -1, 2, 4, 6])

    h = -p
    k = q
    p_str = f"+ {p}" if p > 0 else f"- {abs(p)}"
    q_str = f"+ {q}" if q > 0 else f"- {abs(q)}"
    a_str = f"{a}" if abs(a) > 1 else ("-" if a == -1 else "")
    eq_latex = rf"f(x) = {a_str}(x {p_str})^2 {q_str}"

    prompt = f"Given the parabolic function ${eq_latex}$, determine the coordinates of its turning point."
    ans_latex = rf"({h}; {k})"
    sample = (
        rf"\text{{The standard vertex form is }} y = a(x - h)^2 + k \text{{ with turning point }} (h; k).\\"
        rf"\text{{Here }} x + ({p}) = 0 \implies x = {h} \text{{ and }} y = {k}.\\"
        rf"\therefore \text{{Turning point is }} ({h}; {k})"
    )

    return make_math_question(
        prefix="func_01",
        topic=TOPIC,
        subskill="01_parabola_turning_point_vertex_form",
        learning_objective_id=f"{LO_PREFIX}_tp_vertex_form",
        prompt=prompt,
        prompt_latex=eq_latex,
        answer_latex=ans_latex,
        answer_sympy=f"({h}, {k})",
        sample_answer=sample,
        marking_schema={
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": f"Correct x-coordinate ({h})", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Correct y-coordinate ({k})", "marks": 1, "editable": True},
            ],
            "deductions": [{"rule": "sign_error_in_turning_point", "penalty": -1}],
            "carry_forward_rule": "strict",
        },
        hints={
            "1_nudge": "Set the expression inside the bracket $(x + p)$ equal to zero to find the $x$-coordinate.",
            "2_concept": "For $y = a(x + p)^2 + q$, the turning point is $(-p; q)$.",
            "3_breakdown": f"Turning point: $x = -({p}) = {h}$, $y = {k} \\implies ({h}; {k})$.",
        },
        misconception_tags=["sign_error_turning_point_x"],
        keywords=["parabola", "turning point", "vertex form"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=2,
        mode="01_parabola_turning_point_vertex_form",
        difficulty="easy",
    )


# ---------------------------------------------------------------------------
# 02. Parabola: Axis of Symmetry
# ---------------------------------------------------------------------------
def build_02_parabola_axis_of_symmetry(r: random.Random) -> Dict[str, Any]:
    a = r.choice([-2, -1, 1, 2])
    p = r.choice([-5, -3, -2, 1, 3, 5])
    q = r.choice([-4, 1, 3])
    h = -p
    p_str = f"+ {p}" if p > 0 else f"- {abs(p)}"
    q_str = f"+ {q}" if q > 0 else f"- {abs(q)}"
    a_str = f"{a}" if abs(a) > 1 else ("-" if a == -1 else "")
    eq_latex = rf"g(x) = {a_str}(x {p_str})^2 {q_str}"

    prompt = f"Write down the equation of the axis of symmetry for the parabola ${eq_latex}$."
    ans_latex = rf"x = {h}"
    sample = (
        rf"\text{{The axis of symmetry passes vertically through the turning point }} x = -p:\\"
        rf"x = -({p}) \implies x = {h}"
    )

    return make_math_question(
        prefix="func_02",
        topic=TOPIC,
        subskill="02_parabola_axis_of_symmetry",
        learning_objective_id=f"{LO_PREFIX}_axis_symmetry",
        prompt=prompt,
        prompt_latex=eq_latex,
        answer_latex=ans_latex,
        answer_sympy=f"x = {h}",
        sample_answer=sample,
        marking_schema={
            "total_marks": 1,
            "marking_points": [
                {"id": "mp1", "desc": f"Correct equation x = {h}", "marks": 1, "editable": True},
            ],
            "deductions": [{"rule": "omitted_x_equals", "penalty": -1}],
            "carry_forward_rule": "strict",
        },
        hints={
            "1_nudge": "The axis of symmetry is a vertical line $x = c$.",
            "2_concept": "The line of symmetry always passes through the $x$-coordinate of the turning point.",
            "3_breakdown": f"Equation is $x = {h}$.",
        },
        misconception_tags=["wrote_y_equals_for_axis_of_symmetry", "sign_error_axis_of_symmetry"],
        keywords=["parabola", "axis of symmetry", "vertical line"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=1,
        mode="02_parabola_axis_of_symmetry",
        difficulty="easy",
    )


# ---------------------------------------------------------------------------
# 03. Parabola: y-intercept
# ---------------------------------------------------------------------------
def build_03_parabola_y_intercept(r: random.Random) -> Dict[str, Any]:
    a = r.choice([-2, -1, 1, 2])
    p = r.choice([-3, -2, -1, 1, 2, 3])
    q = r.choice([-4, -2, 1, 3, 5])
    y_int = a * (p ** 2) + q

    p_str = f"+ {p}" if p > 0 else f"- {abs(p)}"
    q_str = f"+ {q}" if q > 0 else f"- {abs(q)}"
    a_str = f"{a}" if abs(a) > 1 else ("-" if a == -1 else "")
    eq_latex = rf"f(x) = {a_str}(x {p_str})^2 {q_str}"

    prompt = f"Calculate the coordinates of the $y$-intercept of the parabola ${eq_latex}$."
    ans_latex = rf"(0; {y_int})"
    sample = (
        rf"\text{{Set }} x = 0 \text{{ to find the }} y\text{{-intercept:}}\\"
        rf"f(0) = {a_str}(0 {p_str})^2 {q_str} = {a}({p^2}) {q_str} = {y_int}\\"
        rf"\therefore \text{{Coordinates: }} (0; {y_int})"
    )

    return make_math_question(
        prefix="func_03",
        topic=TOPIC,
        subskill="03_parabola_y_intercept",
        learning_objective_id=f"{LO_PREFIX}_y_intercept",
        prompt=prompt,
        prompt_latex=eq_latex,
        answer_latex=ans_latex,
        answer_sympy=f"(0, {y_int})",
        sample_answer=sample,
        marking_schema={
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Substituted x = 0 into equation", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Correct coordinates (0; {y_int})", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        hints={
            "1_nudge": "Every $y$-intercept occurs where $x = 0$.",
            "2_concept": "Substitute $x = 0$ into the equation and simplify.",
            "3_breakdown": f"$f(0) = {y_int}$, so the point is $(0; {y_int})$.",
        },
        misconception_tags=["forgot_to_square_first", "sign_error_y_intercept"],
        keywords=["parabola", "y-intercept", "substitution"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=2,
        mode="03_parabola_y_intercept",
        difficulty="easy",
    )


# ---------------------------------------------------------------------------
# 04. Parabola: x-intercepts
# ---------------------------------------------------------------------------
def build_04_parabola_x_intercepts(r: random.Random) -> Dict[str, Any]:
    r1 = r.choice([-4, -3, -2, -1, 1, 2])
    r2 = r.choice([3, 4, 5])
    if r1 == r2:
        r2 += 1
    # y = (x - r1)(x - r2) = x^2 - (r1+r2)x + r1*r2
    b = -(r1 + r2)
    c = r1 * r2
    b_str = f"+ {b}x" if b > 0 else (f"- {abs(b)}x" if b < 0 else "")
    c_str = f"+ {c}" if c > 0 else f"- {abs(c)}"
    eq_latex = rf"f(x) = x^2 {b_str} {c_str}"

    prompt = f"Calculate the coordinates of the $x$-intercepts of the parabola ${eq_latex}$."
    ans_latex = rf"({r1}; 0) \text{{ and }} ({r2}; 0)"
    sample = (
        rf"\text{{Set }} f(x) = 0 \text{{ to find the }} x\text{{-intercepts:}}\\"
        rf"x^2 {b_str} {c_str} = 0\\"
        rf"(x - {r1})(x - {r2}) = 0\\"
        rf"x = {r1} \quad \text{{or}} \quad x = {r2}\\"
        rf"\therefore ({r1}; 0) \text{{ and }} ({r2}; 0)"
    )

    return make_math_question(
        prefix="func_04",
        topic=TOPIC,
        subskill="04_parabola_x_intercepts",
        learning_objective_id=f"{LO_PREFIX}_x_intercepts",
        prompt=prompt,
        prompt_latex=eq_latex,
        answer_latex=ans_latex,
        answer_sympy=f"({r1}, 0), ({r2}, 0)",
        sample_answer=sample,
        marking_schema={
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": "Set equation equal to zero", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Factored quadratic correctly", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Both coordinates: ({r1}; 0) and ({r2}; 0)", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        hints={
            "1_nudge": "Set $f(x) = 0$ and factor the quadratic expression.",
            "2_concept": "The $x$-intercepts are the roots of the quadratic equation.",
            "3_breakdown": f"Factors are $(x - {r1})(x - {r2}) = 0$, giving points $({r1}; 0)$ and $({r2}; 0)$.",
        },
        misconception_tags=["sign_error_in_factoring_roots"],
        keywords=["parabola", "x-intercepts", "roots", "factoring"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=3,
        mode="04_parabola_x_intercepts",
        difficulty="medium",
    )


# ---------------------------------------------------------------------------
# 05. Parabola: Domain and Range
# ---------------------------------------------------------------------------
def build_05_parabola_domain_and_range(r: random.Random) -> Dict[str, Any]:
    a = r.choice([-2, -1, 1, 2])
    p = r.choice([-3, 1, 4])
    q = r.choice([-5, -2, 3, 7])

    p_str = f"+ {p}" if p > 0 else f"- {abs(p)}"
    q_str = f"+ {q}" if q > 0 else f"- {abs(q)}"
    a_str = f"{a}" if abs(a) > 1 else ("-" if a == -1 else "")
    eq_latex = rf"y = {a_str}(x {p_str})^2 {q_str}"

    if a > 0:
        range_latex = rf"y \ge {q} \quad \text{{or}} \quad y \in [{q}; \infty)"
        concave_desc = "concave up (minimum turning point)"
    else:
        range_latex = rf"y \le {q} \quad \text{{or}} \quad y \in (-\infty; {q}]"
        concave_desc = "concave down (maximum turning point)"

    prompt = f"For the parabolic function ${eq_latex}$, write down the domain and the range."
    ans_latex = rf"\text{{Domain: }} x \in \mathbb{{R}}, \; \text{{Range: }} {range_latex}"
    sample = (
        rf"\text{{Domain: }} x \in \mathbb{{R}}\\"
        rf"\text{{Turning point is }} ({-p}; {q}). \text{{ Since }} a = {a} \text{{, the parabola is {concave_desc}.}}\\"
        rf"\therefore \text{{Range: }} {range_latex}"
    )

    return make_math_question(
        prefix="func_05",
        topic=TOPIC,
        subskill="05_parabola_domain_and_range",
        learning_objective_id=f"{LO_PREFIX}_domain_range",
        prompt=prompt,
        prompt_latex=eq_latex,
        answer_latex=ans_latex,
        answer_sympy=ans_latex,
        sample_answer=sample,
        marking_schema={
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Domain: x in R", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Range: {range_latex}", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        hints={
            "1_nudge": "The domain of any polynomial is all real numbers $x \\in \\mathbb{R}$.",
            "2_concept": "Check the sign of $a$: if $a > 0$, $y \\ge q$; if $a < 0$, $y \\le q$.",
            "3_breakdown": f"Range: ${range_latex}$.",
        },
        misconception_tags=["inverted_inequality_for_range"],
        keywords=["parabola", "domain", "range", "inequality"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=2,
        mode="05_parabola_domain_and_range",
        difficulty="easy",
    )


# ---------------------------------------------------------------------------
# 06. Parabola: Turning Point in Standard Form y = ax² + bx + c
# ---------------------------------------------------------------------------
def build_06_parabola_turning_point_standard_form(r: random.Random) -> Dict[str, Any]:
    a = r.choice([1, 2, -1, -2])
    h = r.choice([-3, -2, -1, 1, 2, 3])
    k = r.choice([-6, -4, 2, 5])
    # y = a(x - h)^2 + k = a(x^2 - 2hx + h^2) + k = ax^2 - 2ah x + ah^2 + k
    b = -2 * a * h
    c = a * (h ** 2) + k

    b_str = f"+ {b}x" if b > 0 else (f"- {abs(b)}x" if b < 0 else "")
    c_str = f"+ {c}" if c > 0 else (f"- {abs(c)}" if c < 0 else "")
    a_str = f"{a}" if abs(a) > 1 else ("-" if a == -1 else "")
    eq_latex = rf"f(x) = {a_str}x^2 {b_str} {c_str}"

    prompt = f"Calculate the coordinates of the turning point of the parabola ${eq_latex}$ using the formula $x = -\\frac{{b}}{{2a}}$."
    ans_latex = rf"({h}; {k})"
    sample = (
        rf"x = -\frac{{b}}{{2a}} = -\frac{{{b}}}{{2({a})}} = {h}\\"
        rf"y = f({h}) = {a}({h})^2 {b_str.replace('x', f'({h})')} {c_str} = {k}\\"
        rf"\therefore \text{{Turning point: }} ({h}; {k})"
    )

    return make_math_question(
        prefix="func_06",
        topic=TOPIC,
        subskill="06_parabola_turning_point_standard_form",
        learning_objective_id=f"{LO_PREFIX}_tp_standard_form",
        prompt=prompt,
        prompt_latex=eq_latex,
        answer_latex=ans_latex,
        answer_sympy=f"({h}, {k})",
        sample_answer=sample,
        marking_schema={
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": "Calculated x = -b/(2a)", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Substituted x = {h} to find y = {k}", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Correct turning point coordinates ({h}; {k})", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        hints={
            "1_nudge": "Use the formula $x = -\\frac{b}{2a}$ to find the $x$-coordinate of the turning point.",
            "2_concept": "Substitute the calculated $x$-value back into $f(x)$ to obtain the $y$-coordinate.",
            "3_breakdown": f"$x = {h}$, $y = {k} \\implies ({h}; {k})$.",
        },
        misconception_tags=["sign_error_in_vertex_formula"],
        keywords=["parabola", "turning point", "standard form"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=3,
        mode="06_parabola_turning_point_standard_form",
        difficulty="medium",
    )


# ---------------------------------------------------------------------------
# 07. Parabola: Determine Equation from Turning Point and a Point (with inline_svg)
# ---------------------------------------------------------------------------
def build_07_parabola_equation_from_turning_point_and_point(r: random.Random) -> Dict[str, Any]:
    h = r.choice([-3, -2, 1, 2])
    k = r.choice([-4, -2, 1, 3])
    a = r.choice([1, 2, -1, -2])

    dx = r.choice([1, 2])
    pt_x = h + dx
    pt_y = a * (dx ** 2) + k

    d_spec = _cartesian_parabola_svg(
        a=float(a),
        h=float(h),
        k=float(k),
        tp_label="T",
        pt_x=float(pt_x),
        pt_y=float(pt_y),
    )

    h_str = f"+ {abs(h)}" if h < 0 else f"- {h}"
    k_str = f"+ {k}" if k >= 0 else f"- {abs(k)}"
    a_str = f"{a}" if abs(a) > 1 else ("-" if a == -1 else "")
    res_eq = rf"y = {a_str}(x {h_str})^2 {k_str}"

    prompt = (
        f"In the graph shown, the parabola has its turning point at $T({h}; {k})$ and passes through the point "
        f"$P({pt_x}; {pt_y})$.\n\n"
        f"Determine the equation of the parabola in the form $y = a(x + p)^2 + q$."
    )
    sample = (
        rf"y = a(x - h)^2 + k \implies y = a(x {h_str})^2 {k_str}\\"
        rf"\text{{Substitute point }} ({pt_x}; {pt_y}):\\"
        rf"{pt_y} = a({pt_x} {h_str})^2 {k_str}\\"
        rf"{pt_y} = a({dx}^2) {k_str} = {dx*dx}a {k_str}\\"
        rf"{dx*dx}a = {pt_y - k} \implies a = {a}\\"
        rf"\therefore {res_eq}"
    )

    return make_math_question(
        prefix="func_07",
        topic=TOPIC,
        subskill="07_parabola_equation_from_turning_point_and_point",
        learning_objective_id=f"{LO_PREFIX}_eq_from_tp",
        prompt=prompt,
        prompt_latex=rf"T({h}; {k}), \; P({pt_x}; {pt_y})",
        answer_latex=res_eq,
        answer_sympy=res_eq,
        sample_answer=sample,
        marking_schema={
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": "Substituted turning point into vertex form", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Substituted point ({pt_x}; {pt_y}) and solved for a = {a}", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Final equation: {res_eq}", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        hints={
            "1_nudge": "Start with the vertex form $y = a(x - h)^2 + k$ using turning point coordinates.",
            "2_concept": "Substitute the point $P(x; y)$ to solve for the stretch factor $a$.",
            "3_breakdown": f"Substituting gives $a = {a}$. Result: ${res_eq}$.",
        },
        misconception_tags=["sign_error_in_h_substitution", "algebra_error_solving_for_a"],
        keywords=["parabola", "determine equation", "turning point", "vertex form"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=4,
        mode="07_parabola_equation_from_turning_point_and_point",
        difficulty="medium",
        diagram_spec=d_spec,
    )


# ---------------------------------------------------------------------------
# 08. Parabola: Determine Equation from Roots and a Point (with inline_svg)
# ---------------------------------------------------------------------------
def build_08_parabola_equation_from_roots_and_point(r: random.Random) -> Dict[str, Any]:
    r1 = r.choice([-3, -2, -1])
    r2 = r.choice([1, 2, 4])
    a = r.choice([1, -1, 2])

    pt_x = 0
    pt_y = a * (0 - r1) * (0 - r2)

    h = (r1 + r2) / 2.0
    k = a * (h - r1) * (h - r2)

    d_spec = _cartesian_parabola_svg(
        a=float(a),
        h=float(h),
        k=float(k),
        tp_label="T",
        pt_x=float(pt_x),
        pt_y=float(pt_y),
    )

    r1_str = f"+ {abs(r1)}" if r1 < 0 else f"- {r1}"
    r2_str = f"- {r2}" if r2 > 0 else f"+ {abs(r2)}"
    a_str = f"{a}" if abs(a) > 1 else ("-" if a == -1 else "")
    res_eq = rf"y = {a_str}(x {r1_str})(x {r2_str})"

    prompt = (
        f"In the graph shown, the parabola intersects the $x$-axis at $({r1}; 0)$ and $({r2}; 0)$ "
        f"and intersects the $y$-axis at $(0; {pt_y})$.\n\n"
        f"Determine the equation of the parabola in factored form $y = a(x - x_1)(x - x_2)$."
    )
    sample = (
        rf"y = a(x - x_1)(x - x_2) = a(x {r1_str})(x {r2_str})\\"
        rf"\text{{Substitute the }} y\text{{-intercept }} (0; {pt_y}):\\"
        rf"{pt_y} = a(0 {r1_str})(0 {r2_str}) = a({-r1})({-r2}) = {r1*r2}a\\"
        rf"a = \frac{{{pt_y}}}{{{r1*r2}}} = {a}\\"
        rf"\therefore {res_eq}"
    )

    return make_math_question(
        prefix="func_08",
        topic=TOPIC,
        subskill="08_parabola_equation_from_roots_and_point",
        learning_objective_id=f"{LO_PREFIX}_eq_from_roots",
        prompt=prompt,
        prompt_latex=rf"x_1 = {r1}, \; x_2 = {r2}, \; (0; {pt_y})",
        answer_latex=res_eq,
        answer_sympy=res_eq,
        sample_answer=sample,
        marking_schema={
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": "Substituted roots into factored form", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Substituted (0; {pt_y}) and solved for a = {a}", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Final equation: {res_eq}", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        hints={
            "1_nudge": "Use the intercept form $y = a(x - x_1)(x - x_2)$.",
            "2_concept": "Substitute $(0; y)$ to find the value of $a$.",
            "3_breakdown": f"Solving gives $a = {a}$, yielding ${res_eq}$.",
        },
        misconception_tags=["sign_error_in_intercept_factors"],
        keywords=["parabola", "factored form", "roots", "equation from graph"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=4,
        mode="08_parabola_equation_from_roots_and_point",
        difficulty="medium",
        diagram_spec=d_spec,
    )


# ---------------------------------------------------------------------------
# 09. Parabola: Maximum or Minimum Value
# ---------------------------------------------------------------------------
def build_09_parabola_maximum_or_minimum_value(r: random.Random) -> Dict[str, Any]:
    a = r.choice([-3, -2, -1, 1, 2, 3])
    p = r.choice([-4, -2, 1, 3])
    q = r.choice([-5, -1, 4, 8])

    p_str = f"+ {p}" if p > 0 else f"- {abs(p)}"
    q_str = f"+ {q}" if q > 0 else f"- {abs(q)}"
    a_str = f"{a}" if abs(a) > 1 else ("-" if a == -1 else "")
    eq_latex = rf"f(x) = {a_str}(x {p_str})^2 {q_str}"

    type_val = "minimum" if a > 0 else "maximum"
    prompt = f"State whether the parabola ${eq_latex}$ has a maximum or a minimum value, and write down this value."
    ans_latex = rf"\text{{{type_val} value is }} {q}"
    sample = (
        rf"\text{{Since }} a = {a} \text{{ is {'positive' if a > 0 else 'negative'}, the parabola opens {'upwards' if a > 0 else 'downwards'}.}}\\"
        rf"\text{{Therefore, it has a {type_val} value at its turning point: }} y = {q}"
    )

    return make_math_question(
        prefix="func_09",
        topic=TOPIC,
        subskill="09_parabola_maximum_or_minimum_value",
        learning_objective_id=f"{LO_PREFIX}_max_min",
        prompt=prompt,
        prompt_latex=eq_latex,
        answer_latex=ans_latex,
        answer_sympy=f"{type_val}, {q}",
        sample_answer=sample,
        marking_schema={
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": f"Correctly identified {type_val}", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Correct extremum value y = {q}", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "strict",
        },
        hints={
            "1_nudge": "If $a > 0$ (smiles), it has a minimum. If $a < 0$ (frowns), it has a maximum.",
            "2_concept": "The maximum or minimum value is always the $y$-value of the turning point.",
            "3_breakdown": f"It has a {type_val} value of ${q}$.",
        },
        misconception_tags=["inverted_max_min_concept", "gave_x_value_instead_of_y"],
        keywords=["parabola", "maximum", "minimum", "turning point"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=2,
        mode="09_parabola_maximum_or_minimum_value",
        difficulty="easy",
    )


# ---------------------------------------------------------------------------
# 10. Parabola: Horizontal and Vertical Shifts
# ---------------------------------------------------------------------------
def build_10_parabola_vertical_horizontal_shifts(r: random.Random) -> Dict[str, Any]:
    p = r.choice([-4, -2, 2, 5])
    q = r.choice([-6, -3, 3, 7])

    p_str = f"+ {p}" if p > 0 else f"- {abs(p)}"
    q_str = f"+ {q}" if q > 0 else f"- {abs(q)}"
    eq_latex = rf"g(x) = (x {p_str})^2 {q_str}"

    h_dir = "left" if p > 0 else "right"
    v_dir = "upwards" if q > 0 else "downwards"

    prompt = (
        f"Describe the geometric transformation that maps the basic parabola $y = x^2$ onto "
        f"${eq_latex}$."
    )
    ans_latex = rf"\text{{Shifted }} {abs(p)} \text{{ units {h_dir} and }} {abs(q)} \text{{ units {v_dir}}}"
    sample = (
        rf"\text{{The term }} (x {p_str}) \text{{ represents a horizontal shift of }} {abs(p)} \text{{ units to the {h_dir}.}}\\"
        rf"\text{{The term }} {q_str} \text{{ represents a vertical shift of }} {abs(q)} \text{{ units {v_dir}.}}"
    )

    return make_math_question(
        prefix="func_10",
        topic=TOPIC,
        subskill="10_parabola_vertical_horizontal_shifts",
        learning_objective_id=f"{LO_PREFIX}_shifts",
        prompt=prompt,
        prompt_latex=eq_latex,
        answer_latex=ans_latex,
        answer_sympy=ans_latex,
        sample_answer=sample,
        marking_schema={
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": f"Horizontal shift {abs(p)} units {h_dir}", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Vertical shift {abs(q)} units {v_dir}", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        hints={
            "1_nudge": "$(x + p)$ shifts the graph left if $p > 0$ and right if $p < 0$.",
            "2_concept": "The constant $q$ shifts the graph vertically up if $q > 0$ and down if $q < 0$.",
            "3_breakdown": f"Shifted {abs(p)} units {h_dir} and {abs(q)} units {v_dir}.",
        },
        misconception_tags=["inverted_horizontal_shift_direction"],
        keywords=["transformations", "translations", "horizontal shift", "vertical shift"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=2,
        mode="10_parabola_vertical_horizontal_shifts",
        difficulty="easy",
    )


# ---------------------------------------------------------------------------
# 11. Hyperbola: Vertical Asymptote
# ---------------------------------------------------------------------------
def build_11_hyperbola_vertical_asymptote(r: random.Random) -> Dict[str, Any]:
    a = r.choice([2, 3, 4, 6])
    p = r.choice([-5, -3, -2, 1, 2, 4])
    q = r.choice([-4, 1, 3])

    p_str = f"+ {p}" if p > 0 else f"- {abs(p)}"
    q_str = f"+ {q}" if q > 0 else f"- {abs(q)}"
    eq_latex = rf"f(x) = \frac{{{a}}}{{x {p_str}}} {q_str}"

    vert_asymp = -p
    prompt = f"Write down the equation of the vertical asymptote of the hyperbola ${eq_latex}$."
    ans_latex = rf"x = {vert_asymp}"
    sample = (
        rf"\text{{Set the denominator equal to zero:}}\\"
        rf"x {p_str} = 0 \implies x = {vert_asymp}\\"
        rf"\therefore \text{{Vertical asymptote: }} x = {vert_asymp}"
    )

    return make_math_question(
        prefix="func_11",
        topic=TOPIC,
        subskill="11_hyperbola_vertical_asymptote",
        learning_objective_id=f"{LO_PREFIX}_hyp_vert_asymp",
        prompt=prompt,
        prompt_latex=eq_latex,
        answer_latex=ans_latex,
        answer_sympy=f"x = {vert_asymp}",
        sample_answer=sample,
        marking_schema={
            "total_marks": 1,
            "marking_points": [
                {"id": "mp1", "desc": f"Correct equation x = {vert_asymp}", "marks": 1, "editable": True},
            ],
            "deductions": [{"rule": "omitted_x_equals", "penalty": -1}],
            "carry_forward_rule": "strict",
        },
        hints={
            "1_nudge": "The vertical asymptote occurs where the denominator is zero (division by zero).",
            "2_concept": "Set $x + p = 0 \\implies x = -p$.",
            "3_breakdown": f"Vertical asymptote is $x = {vert_asymp}$.",
        },
        misconception_tags=["sign_error_vertical_asymptote", "wrote_y_for_vertical_asymptote"],
        keywords=["hyperbola", "vertical asymptote", "division by zero"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=1,
        mode="11_hyperbola_vertical_asymptote",
        difficulty="easy",
    )


# ---------------------------------------------------------------------------
# 12. Hyperbola: Horizontal Asymptote
# ---------------------------------------------------------------------------
def build_12_hyperbola_horizontal_asymptote(r: random.Random) -> Dict[str, Any]:
    a = r.choice([2, 3, 5, 8])
    p = r.choice([-3, 1, 2])
    q = r.choice([-6, -4, -1, 2, 5])

    p_str = f"+ {p}" if p > 0 else f"- {abs(p)}"
    q_str = f"+ {q}" if q > 0 else f"- {abs(q)}"
    eq_latex = rf"g(x) = \frac{{{a}}}{{x {p_str}}} {q_str}"

    prompt = f"Write down the equation of the horizontal asymptote of the hyperbola ${eq_latex}$."
    ans_latex = rf"y = {q}"
    sample = (
        rf"\text{{As }} x \to \pm\infty, \; \frac{{{a}}}{{x {p_str}}} \to 0.\\"
        rf"\therefore \text{{Horizontal asymptote: }} y = {q}"
    )

    return make_math_question(
        prefix="func_12",
        topic=TOPIC,
        subskill="12_hyperbola_horizontal_asymptote",
        learning_objective_id=f"{LO_PREFIX}_hyp_horiz_asymp",
        prompt=prompt,
        prompt_latex=eq_latex,
        answer_latex=ans_latex,
        answer_sympy=f"y = {q}",
        sample_answer=sample,
        marking_schema={
            "total_marks": 1,
            "marking_points": [
                {"id": "mp1", "desc": f"Correct equation y = {q}", "marks": 1, "editable": True},
            ],
            "deductions": [{"rule": "omitted_y_equals", "penalty": -1}],
            "carry_forward_rule": "strict",
        },
        hints={
            "1_nudge": "The horizontal asymptote is the vertical shift $y = q$.",
            "2_concept": "As $x$ becomes very large, the fraction tends to 0, leaving $y = q$.",
            "3_breakdown": f"Horizontal asymptote is $y = {q}$.",
        },
        misconception_tags=["wrote_x_for_horizontal_asymptote"],
        keywords=["hyperbola", "horizontal asymptote", "limits"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=1,
        mode="12_hyperbola_horizontal_asymptote",
        difficulty="easy",
    )


# ---------------------------------------------------------------------------
# 13. Hyperbola: Center of Symmetry (Intersection of Asymptotes)
# ---------------------------------------------------------------------------
def build_13_hyperbola_center_of_symmetry(r: random.Random) -> Dict[str, Any]:
    a = r.choice([-4, -2, 2, 4])
    p = r.choice([-3, -1, 2, 4])
    q = r.choice([-5, -2, 1, 3])

    p_str = f"+ {p}" if p > 0 else f"- {abs(p)}"
    q_str = f"+ {q}" if q > 0 else f"- {abs(q)}"
    eq_latex = rf"h(x) = \frac{{{a}}}{{x {p_str}}} {q_str}"

    center_x = -p
    center_y = q
    prompt = f"Determine the point of intersection of the asymptotes for the hyperbola ${eq_latex}$."
    ans_latex = rf"({center_x}; {center_y})"
    sample = (
        rf"\text{{Vertical asymptote: }} x = {center_x}\\"
        rf"\text{{Horizontal asymptote: }} y = {center_y}\\"
        rf"\therefore \text{{Point of intersection (center of symmetry): }} ({center_x}; {center_y})"
    )

    return make_math_question(
        prefix="func_13",
        topic=TOPIC,
        subskill="13_hyperbola_center_of_symmetry",
        learning_objective_id=f"{LO_PREFIX}_hyp_center",
        prompt=prompt,
        prompt_latex=eq_latex,
        answer_latex=ans_latex,
        answer_sympy=f"({center_x}, {center_y})",
        sample_answer=sample,
        marking_schema={
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": f"Correct x-coordinate ({center_x})", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Correct y-coordinate ({center_y})", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        hints={
            "1_nudge": "Find both asymptotes first: $x = -p$ and $y = q$.",
            "2_concept": "The asymptotes intersect at the point $(-p; q)$.",
            "3_breakdown": f"Intersection point: $({center_x}; {center_y})$.",
        },
        misconception_tags=["sign_error_center_of_symmetry"],
        keywords=["hyperbola", "center of symmetry", "asymptotes intersection"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=2,
        mode="13_hyperbola_center_of_symmetry",
        difficulty="easy",
    )


# ---------------------------------------------------------------------------
# 14. Hyperbola: Axis of Symmetry with Positive Gradient (m = 1)
# ---------------------------------------------------------------------------
def build_14_hyperbola_axis_of_symmetry_positive_gradient(r: random.Random) -> Dict[str, Any]:
    a = r.choice([-3, 3, 4, 6])
    p = r.choice([-4, -2, 1, 3])
    q = r.choice([-3, 1, 2, 5])

    p_str = f"+ {p}" if p > 0 else f"- {abs(p)}"
    q_str = f"+ {q}" if q > 0 else f"- {abs(q)}"
    eq_latex = rf"f(x) = \frac{{{a}}}{{x {p_str}}} {q_str}"

    c_val = p + q
    c_str = f"+ {c_val}" if c_val > 0 else (f"- {abs(c_val)}" if c_val < 0 else "")
    res_eq = rf"y = x {c_str}".strip()

    prompt = (
        f"Determine the equation of the axis of symmetry with positive gradient ($m = 1$) "
        f"for the hyperbola ${eq_latex}$."
    )
    sample = (
        rf"\text{{The axis of symmetry with }} m = 1 \text{{ is given by }} y = (x + p) + q:\\"
        rf"y = (x {p_str}) {q_str}\\"
        rf"\therefore {res_eq}"
    )

    return make_math_question(
        prefix="func_14",
        topic=TOPIC,
        subskill="14_hyperbola_axis_of_symmetry_positive_gradient",
        learning_objective_id=f"{LO_PREFIX}_hyp_symm_pos",
        prompt=prompt,
        prompt_latex=eq_latex,
        answer_latex=res_eq,
        answer_sympy=res_eq,
        sample_answer=sample,
        marking_schema={
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Setup formula y = (x + p) + q", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Correct equation: {res_eq}", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        hints={
            "1_nudge": "The axis of symmetry with positive gradient has equation $y = (x + p) + q$.",
            "2_concept": "Alternatively, use $y - y_1 = 1(x - x_1)$ passing through $(-p; q)$.",
            "3_breakdown": f"Result: ${res_eq}$.",
        },
        misconception_tags=["sign_error_axis_of_symmetry_hyperbola"],
        keywords=["hyperbola", "axis of symmetry", "positive gradient"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=2,
        mode="14_hyperbola_axis_of_symmetry_positive_gradient",
        difficulty="medium",
    )


# ---------------------------------------------------------------------------
# 15. Hyperbola: Axis of Symmetry with Negative Gradient (m = -1)
# ---------------------------------------------------------------------------
def build_15_hyperbola_axis_of_symmetry_negative_gradient(r: random.Random) -> Dict[str, Any]:
    a = r.choice([-4, -2, 2, 5])
    p = r.choice([-3, -1, 2, 4])
    q = r.choice([-4, 1, 3, 6])

    p_str = f"+ {p}" if p > 0 else f"- {abs(p)}"
    q_str = f"+ {q}" if q > 0 else f"- {abs(q)}"
    eq_latex = rf"g(x) = \frac{{{a}}}{{x {p_str}}} {q_str}"

    c_val = -p + q
    c_str = f"+ {c_val}" if c_val > 0 else (f"- {abs(c_val)}" if c_val < 0 else "")
    res_eq = rf"y = -x {c_str}".strip()

    prompt = (
        f"Determine the equation of the axis of symmetry with negative gradient ($m = -1$) "
        f"for the hyperbola ${eq_latex}$."
    )
    sample = (
        rf"\text{{The axis of symmetry with }} m = -1 \text{{ is given by }} y = -(x + p) + q:\\"
        rf"y = -(x {p_str}) {q_str} = -x - ({p}) {q_str}\\"
        rf"\therefore {res_eq}"
    )

    return make_math_question(
        prefix="func_15",
        topic=TOPIC,
        subskill="15_hyperbola_axis_of_symmetry_negative_gradient",
        learning_objective_id=f"{LO_PREFIX}_hyp_symm_neg",
        prompt=prompt,
        prompt_latex=eq_latex,
        answer_latex=res_eq,
        answer_sympy=res_eq,
        sample_answer=sample,
        marking_schema={
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Setup formula y = -(x + p) + q", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Correct equation: {res_eq}", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        hints={
            "1_nudge": "The axis of symmetry with negative gradient has equation $y = -(x + p) + q$.",
            "2_concept": "Distribute the negative sign through $(x + p)$ and then add $q$.",
            "3_breakdown": f"Result: ${res_eq}$.",
        },
        misconception_tags=["distribution_error_negative_axis_symmetry"],
        keywords=["hyperbola", "axis of symmetry", "negative gradient"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=2,
        mode="15_hyperbola_axis_of_symmetry_negative_gradient",
        difficulty="medium",
    )


# ---------------------------------------------------------------------------
# 16. Hyperbola: Domain
# ---------------------------------------------------------------------------
def build_16_hyperbola_domain(r: random.Random) -> Dict[str, Any]:
    a = r.choice([2, 4, 6])
    p = r.choice([-5, -3, 2, 4])
    q = r.choice([-2, 1, 5])
    vert = -p

    p_str = f"+ {p}" if p > 0 else f"- {abs(p)}"
    q_str = f"+ {q}" if q > 0 else f"- {abs(q)}"
    eq_latex = rf"f(x) = \frac{{{a}}}{{x {p_str}}} {q_str}"

    prompt = f"Write down the domain of the hyperbola ${eq_latex}$."
    ans_latex = rf"x \in \mathbb{{R}}, \; x \ne {vert}"
    sample = (
        rf"\text{{The denominator cannot be zero: }} x {p_str} \ne 0 \implies x \ne {vert}\\"
        rf"\therefore \text{{Domain: }} x \in \mathbb{{R}}, \; x \ne {vert}"
    )

    return make_math_question(
        prefix="func_16",
        topic=TOPIC,
        subskill="16_hyperbola_domain",
        learning_objective_id=f"{LO_PREFIX}_hyp_domain",
        prompt=prompt,
        prompt_latex=eq_latex,
        answer_latex=ans_latex,
        answer_sympy=ans_latex,
        sample_answer=sample,
        marking_schema={
            "total_marks": 1,
            "marking_points": [
                {"id": "mp1", "desc": f"Correct domain: x in R, x != {vert}", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "strict",
        },
        hints={
            "1_nudge": "A hyperbola is defined for all real numbers except at its vertical asymptote.",
            "2_concept": "Division by zero occurs when $x = -p$.",
            "3_breakdown": f"Domain: $x \\in \\mathbb{{R}}, \\; x \\ne {vert}$.",
        },
        misconception_tags=["sign_error_domain_restriction"],
        keywords=["hyperbola", "domain", "restriction"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=1,
        mode="16_hyperbola_domain",
        difficulty="easy",
    )


# ---------------------------------------------------------------------------
# 17. Hyperbola: Range
# ---------------------------------------------------------------------------
def build_17_hyperbola_range(r: random.Random) -> Dict[str, Any]:
    a = r.choice([3, 5, 7])
    p = r.choice([-2, 1, 3])
    q = r.choice([-7, -4, 2, 6])

    p_str = f"+ {p}" if p > 0 else f"- {abs(p)}"
    q_str = f"+ {q}" if q > 0 else f"- {abs(q)}"
    eq_latex = rf"f(x) = \frac{{{a}}}{{x {p_str}}} {q_str}"

    prompt = f"Write down the range of the hyperbola ${eq_latex}$."
    ans_latex = rf"y \in \mathbb{{R}}, \; y \ne {q}"
    sample = (
        rf"\text{{Since }}\frac{{{a}}}{{x {p_str}}} \ne 0 \text{{ for any real }} x, \; y \ne {q}\\"
        rf"\therefore \text{{Range: }} y \in \mathbb{{R}}, \; y \ne {q}"
    )

    return make_math_question(
        prefix="func_17",
        topic=TOPIC,
        subskill="17_hyperbola_range",
        learning_objective_id=f"{LO_PREFIX}_hyp_range",
        prompt=prompt,
        prompt_latex=eq_latex,
        answer_latex=ans_latex,
        answer_sympy=ans_latex,
        sample_answer=sample,
        marking_schema={
            "total_marks": 1,
            "marking_points": [
                {"id": "mp1", "desc": f"Correct range: y in R, y != {q}", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "strict",
        },
        hints={
            "1_nudge": "The range excludes the value of the horizontal asymptote.",
            "2_concept": "The fraction can never equal zero, so $y$ can never equal $q$.",
            "3_breakdown": f"Range: $y \\in \\mathbb{{R}}, \\; y \\ne {q}$.",
        },
        misconception_tags=["confused_domain_and_range"],
        keywords=["hyperbola", "range", "horizontal asymptote"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=1,
        mode="17_hyperbola_range",
        difficulty="easy",
    )


# ---------------------------------------------------------------------------
# 18. Hyperbola: y-intercept
# ---------------------------------------------------------------------------
def build_18_hyperbola_y_intercept(r: random.Random) -> Dict[str, Any]:
    p = r.choice([-3, -2, -1, 1, 2, 3])
    k_mult = r.choice([1, 2, 3])
    a = p * k_mult  # ensure a/p is an integer
    q = r.choice([-4, -1, 2, 5])

    y_val = int(a / p) + q
    p_str = f"+ {p}" if p > 0 else f"- {abs(p)}"
    q_str = f"+ {q}" if q > 0 else f"- {abs(q)}"
    eq_latex = rf"g(x) = \frac{{{a}}}{{x {p_str}}} {q_str}"

    prompt = f"Calculate the coordinates of the $y$-intercept of the hyperbola ${eq_latex}$."
    ans_latex = rf"(0; {y_val})"
    sample = (
        rf"\text{{Substitute }} x = 0:\\"
        rf"g(0) = \frac{{{a}}}{{0 {p_str}}} {q_str} = \frac{{{a}}}{{{p}}} {q_str} = {int(a/p)} {q_str} = {y_val}\\"
        rf"\therefore (0; {y_val})"
    )

    return make_math_question(
        prefix="func_18",
        topic=TOPIC,
        subskill="18_hyperbola_y_intercept",
        learning_objective_id=f"{LO_PREFIX}_hyp_y_int",
        prompt=prompt,
        prompt_latex=eq_latex,
        answer_latex=ans_latex,
        answer_sympy=f"(0, {y_val})",
        sample_answer=sample,
        marking_schema={
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Substituted x = 0", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Correct coordinates: (0; {y_val})", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        hints={
            "1_nudge": "Substitute $x = 0$ into the formula.",
            "2_concept": "Simplify the fraction $\\frac{a}{p}$ and add $q$.",
            "3_breakdown": f"$g(0) = {y_val} \\implies (0; {y_val})$.",
        },
        misconception_tags=["sign_error_in_division"],
        keywords=["hyperbola", "y-intercept", "substitution"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=2,
        mode="18_hyperbola_y_intercept",
        difficulty="easy",
    )


# ---------------------------------------------------------------------------
# 19. Hyperbola: x-intercept
# ---------------------------------------------------------------------------
def build_19_hyperbola_x_intercept(r: random.Random) -> Dict[str, Any]:
    q = r.choice([-3, -2, -1, 1, 2, 3])
    k_mult = r.choice([1, 2, 3])
    a = -q * k_mult  # ensure a / (-q) is an integer
    p = r.choice([-4, -2, 1, 3])

    # a / (x + p) + q = 0 => a / (x + p) = -q => x + p = a / (-q) = k_mult => x = k_mult - p
    x_val = k_mult - p
    p_str = f"+ {p}" if p > 0 else f"- {abs(p)}"
    q_str = f"+ {q}" if q > 0 else f"- {abs(q)}"
    eq_latex = rf"f(x) = \frac{{{a}}}{{x {p_str}}} {q_str}"

    prompt = f"Calculate the coordinates of the $x$-intercept of the hyperbola ${eq_latex}$."
    ans_latex = rf"({x_val}; 0)"
    sample = (
        rf"\text{{Set }} f(x) = 0:\\"
        rf"\frac{{{a}}}{{x {p_str}}} {q_str} = 0\\"
        rf"\frac{{{a}}}{{x {p_str}}} = {-q}\\"
        rf"x {p_str} = \frac{{{a}}}{{{-q}}} = {k_mult}\\"
        rf"x = {k_mult} - ({p}) = {x_val}\\"
        rf"\therefore ({x_val}; 0)"
    )

    return make_math_question(
        prefix="func_19",
        topic=TOPIC,
        subskill="19_hyperbola_x_intercept",
        learning_objective_id=f"{LO_PREFIX}_hyp_x_int",
        prompt=prompt,
        prompt_latex=eq_latex,
        answer_latex=ans_latex,
        answer_sympy=f"({x_val}, 0)",
        sample_answer=sample,
        marking_schema={
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Set f(x) = 0 and cleared denominator", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Correct coordinates: ({x_val}; 0)", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        hints={
            "1_nudge": "Set $f(x) = 0$ to find the $x$-intercept.",
            "2_concept": "Move $q$ to the other side and solve for $(x + p)$.",
            "3_breakdown": f"Point is $({x_val}; 0)$.",
        },
        misconception_tags=["algebra_error_clearing_denominator"],
        keywords=["hyperbola", "x-intercept", "clearing fractions"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=3,
        mode="19_hyperbola_x_intercept",
        difficulty="medium",
    )


# ---------------------------------------------------------------------------
# 20. Hyperbola: Determine Equation from Asymptotes and a Point (with inline_svg)
# ---------------------------------------------------------------------------
def build_20_hyperbola_equation_from_asymptotes_and_point(r: random.Random) -> Dict[str, Any]:
    asymp_x = r.choice([-3, -2, 1, 2])
    asymp_y = r.choice([-2, 1, 3])
    a = r.choice([-6, -4, 2, 4, 6])

    p = -asymp_x
    q = asymp_y

    dx = r.choice([1, 2])
    pt_x = asymp_x + dx
    pt_y = round(a / dx + q, 1)

    d_spec = _cartesian_hyperbola_svg(
        a=float(a),
        p=float(p),
        q=float(q),
        pt_x=float(pt_x),
        pt_y=float(pt_y),
    )

    p_str = f"+ {p}" if p > 0 else f"- {abs(p)}"
    q_str = f"+ {q}" if q > 0 else f"- {abs(q)}"
    res_eq = rf"y = \frac{{{a}}}{{x {p_str}}} {q_str}"

    prompt = (
        f"In the graph shown, the hyperbola has asymptotes $x = {asymp_x}$ and $y = {asymp_y}$, "
        f"and passes through the point $P({pt_x}; {pt_y})$.\n\n"
        f"Determine the equation of the hyperbola in the form $y = \\frac{{a}}{{x + p}} + q$."
    )
    sample = (
        rf"\text{{From the asymptotes: }} p = {-asymp_x} \text{{ and }} q = {asymp_y}:\\"
        rf"y = \frac{{a}}{{x {p_str}}} {q_str}\\"
        rf"\text{{Substitute }} P({pt_x}; {pt_y}):\\"
        rf"{pt_y} = \frac{{a}}{{{pt_x} {p_str}}} {q_str} = \frac{{a}}{{{dx}}} {q_str}\\"
        rf"\frac{{a}}{{{dx}}} = {pt_y - q} \implies a = {a}\\"
        rf"\therefore {res_eq}"
    )

    return make_math_question(
        prefix="func_20",
        topic=TOPIC,
        subskill="20_hyperbola_equation_from_asymptotes_and_point",
        learning_objective_id=f"{LO_PREFIX}_hyp_eq_from_graph",
        prompt=prompt,
        prompt_latex=rf"x = {asymp_x}, \; y = {asymp_y}, \; P({pt_x}; {pt_y})",
        answer_latex=res_eq,
        answer_sympy=res_eq,
        sample_answer=sample,
        marking_schema={
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": "Substituted asymptotes into formula", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Substituted point P and solved for a = {a}", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Final equation: {res_eq}", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        hints={
            "1_nudge": "Substitute the asymptotes $p = -({asymp_x})$ and $q = {asymp_y}$ first.",
            "2_concept": "Substitute the coordinates of point $P$ to solve for $a$.",
            "3_breakdown": f"$a = {a}$, giving ${res_eq}$.",
        },
        misconception_tags=["sign_error_asymptote_substitution"],
        keywords=["hyperbola", "determine equation", "asymptotes", "substitution"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=4,
        mode="20_hyperbola_equation_from_asymptotes_and_point",
        difficulty="medium",
        diagram_spec=d_spec,
    )


# ---------------------------------------------------------------------------
# 21. Intersection: Parabola and Straight Line
# ---------------------------------------------------------------------------
def build_21_parabola_hyperbola_intersection(r: random.Random) -> Dict[str, Any]:
    # Parabola y = x^2 - 4, Line y = x - 2
    # x^2 - 4 = x - 2 => x^2 - x - 2 = 0 => (x - 2)(x + 1) = 0 => x = 2, -1
    x1, x2 = 2, -1
    y1, y2 = 0, -3
    prompt = (
        f"Calculate the coordinates of the points of intersection between the parabola "
        f"$f(x) = x^2 - 4$ and the straight line $g(x) = x - 2$."
    )
    ans_latex = rf"({x1}; {y1}) \text{{ and }} ({x2}; {y2})"
    sample = (
        rf"\text{{Set }} f(x) = g(x):\\"
        rf"x^2 - 4 = x - 2\\"
        rf"x^2 - x - 2 = 0\\"
        rf"(x - 2)(x + 1) = 0 \implies x = 2 \text{{ or }} x = -1\\"
        rf"\text{{Substitute }} x = 2 \implies y = 2 - 2 = 0 \implies (2; 0)\\"
        rf"\text{{Substitute }} x = -1 \implies y = -1 - 2 = -3 \implies (-1; -3)\\"
        rf"\therefore (2; 0) \text{{ and }} (-1; -3)"
    )

    return make_math_question(
        prefix="func_21",
        topic=TOPIC,
        subskill="21_parabola_hyperbola_intersection",
        learning_objective_id=f"{LO_PREFIX}_intersection_parab_line",
        prompt=prompt,
        prompt_latex=r"f(x) = x^2 - 4, \; g(x) = x - 2",
        answer_latex=ans_latex,
        answer_sympy=f"({x1}, {y1}), ({x2}, {y2})",
        sample_answer=sample,
        marking_schema={
            "total_marks": 4,
            "marking_points": [
                {"id": "mp1", "desc": "Equated f(x) = g(x)", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Formed quadratic equation and solved for x", "marks": 1, "editable": True},
                {"id": "mp3", "desc": "Point 1: (2; 0)", "marks": 1, "editable": True},
                {"id": "mp4", "desc": "Point 2: (-1; -3)", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        hints={
            "1_nudge": "Set $f(x) = g(x)$ and rearrange all terms to one side.",
            "2_concept": "Factor the quadratic $x^2 - x - 2 = 0$ to find both $x$-values.",
            "3_breakdown": "Substitute both $x$-values into $g(x) = x - 2$ to find the corresponding $y$-values.",
        },
        misconception_tags=["forgot_to_calculate_y_coordinates"],
        keywords=["intersection", "simultaneous equations", "parabola and line"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=4,
        mode="21_parabola_hyperbola_intersection",
        difficulty="medium",
    )


# ---------------------------------------------------------------------------
# 22. Parabola: Intervals of Increase and Decrease
# ---------------------------------------------------------------------------
def build_22_parabola_intervals_of_increase_decrease(r: random.Random) -> Dict[str, Any]:
    a = r.choice([-2, -1, 1, 2])
    h = r.choice([-4, -2, 1, 3])
    k = r.choice([-3, 2, 5])
    p = -h

    p_str = f"+ {p}" if p > 0 else f"- {abs(p)}"
    q_str = f"+ {k}" if k > 0 else f"- {abs(k)}"
    a_str = f"{a}" if abs(a) > 1 else ("-" if a == -1 else "")
    eq_latex = rf"f(x) = {a_str}(x {p_str})^2 {q_str}"

    if a > 0:
        inc_interval = rf"x > {h}"
        dec_interval = rf"x < {h}"
        expl = "opens upwards"
    else:
        inc_interval = rf"x < {h}"
        dec_interval = rf"x > {h}"
        expl = "opens downwards"

    prompt = f"For which values of $x$ is the function ${eq_latex}$ increasing?"
    ans_latex = inc_interval
    sample = (
        rf"\text{{The axis of symmetry is }} x = {h}.\\"
        rf"\text{{Since }} a = {a} \text{{, the parabola {expl}.}}\\"
        rf"\therefore \text{{The function is increasing for }} {inc_interval}"
    )

    return make_math_question(
        prefix="func_22",
        topic=TOPIC,
        subskill="22_parabola_intervals_of_increase_decrease",
        learning_objective_id=f"{LO_PREFIX}_inc_dec",
        prompt=prompt,
        prompt_latex=eq_latex,
        answer_latex=ans_latex,
        answer_sympy=ans_latex,
        sample_answer=sample,
        marking_schema={
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": f"Turning point x-value identified ({h})", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Correct inequality for increasing: {inc_interval}", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        hints={
            "1_nudge": "Find the $x$-coordinate of the turning point.",
            "2_concept": "A function is increasing where moving from left to right, the curve goes upwards.",
            "3_breakdown": f"Increasing interval: ${inc_interval}$.",
        },
        misconception_tags=["reversed_increasing_decreasing_interval"],
        keywords=["parabola", "increasing", "decreasing", "intervals"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=2,
        mode="22_parabola_intervals_of_increase_decrease",
        difficulty="medium",
    )


# ---------------------------------------------------------------------------
# 23. Hyperbola: Effect of Sign of a
# ---------------------------------------------------------------------------
def build_23_hyperbola_quadrant_branches_effect_of_a(r: random.Random) -> Dict[str, Any]:
    a_sign = r.choice(["positive", "negative"])
    a_val = 4 if a_sign == "positive" else -4

    if a_sign == "positive":
        quad_branches = "first and third quadrants (relative to the asymptotes)"
    else:
        quad_branches = "second and fourth quadrants (relative to the asymptotes)"

    prompt = (
        f"Explain in which quadrants relative to the asymptotes the branches of the hyperbola "
        f"$y = \\frac{{{a_val}}}{{x}}$ lie, and give a reason based on the value of $a$."
    )
    ans_latex = quad_branches
    sample = (
        rf"\text{{Here }} a = {a_val} \text{{ is {a_sign}.}}\\"
        rf"\text{{When }} a {'> 0' if a_sign == 'positive' else '< 0'}\text{{, the branches lie in the {quad_branches}.}}"
    )

    return make_math_question(
        prefix="func_23",
        topic=TOPIC,
        subskill="23_hyperbola_quadrant_branches_effect_of_a",
        learning_objective_id=f"{LO_PREFIX}_hyp_branches",
        prompt=prompt,
        prompt_latex=rf"y = \frac{{{a_val}}}{{x}}",
        answer_latex=ans_latex,
        answer_sympy=ans_latex,
        sample_answer=sample,
        marking_schema={
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": f"Identified sign of a ({a_sign})", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Correct quadrants: {quad_branches}", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "strict",
        },
        hints={
            "1_nudge": f"Look at the sign of $a = {a_val}$.",
            "2_concept": "If $a > 0$, branches lie in Q1 & Q3 relative to asymptotes. If $a < 0$, Q2 & Q4.",
            "3_breakdown": f"Branches lie in the {quad_branches}.",
        },
        misconception_tags=["inverted_hyperbola_quadrants"],
        keywords=["hyperbola", "branches", "effect of a"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=2,
        mode="23_hyperbola_quadrant_branches_effect_of_a",
        difficulty="easy",
    )


# ---------------------------------------------------------------------------
# 24. Parabola: Reflection in the Axes
# ---------------------------------------------------------------------------
def build_24_parabola_reflection_axes(r: random.Random) -> Dict[str, Any]:
    axis = r.choice(["x-axis", "y-axis"])
    p = r.choice([-3, 2, 4])
    q = r.choice([-5, 1, 6])

    p_str = f"+ {p}" if p > 0 else f"- {abs(p)}"
    q_str = f"+ {q}" if q > 0 else f"- {abs(q)}"
    eq_latex = rf"f(x) = (x {p_str})^2 {q_str}"

    if axis == "x-axis":
        # -f(x) = -[(x + p)^2 + q] = -(x + p)^2 - q
        neg_q = -q
        neg_q_str = f"+ {neg_q}" if neg_q > 0 else f"- {abs(neg_q)}"
        res_eq = rf"y = -(x {p_str})^2 {neg_q_str}"
        expl = rf"y = -f(x) = -[(x {p_str})^2 {q_str}] = {res_eq}"
    else:
        # f(-x) = (-x + p)^2 + q = (-(x - p))^2 + q = (x - p)^2 + q
        inv_p = -p
        inv_p_str = f"+ {inv_p}" if inv_p > 0 else f"- {abs(inv_p)}"
        res_eq = rf"y = (x {inv_p_str})^2 {q_str}"
        expl = rf"y = f(-x) = (-x {p_str})^2 {q_str} = (x {inv_p_str})^2 {q_str}"

    prompt = (
        f"Write down the equation of the function resulting from reflecting "
        f"${eq_latex}$ across the {axis}."
    )
    ans_latex = res_eq
    sample = expl

    return make_math_question(
        prefix="func_24",
        topic=TOPIC,
        subskill="24_parabola_reflection_axes",
        learning_objective_id=f"{LO_PREFIX}_reflection_parab",
        prompt=prompt,
        prompt_latex=eq_latex,
        answer_latex=ans_latex,
        answer_sympy=res_eq,
        sample_answer=sample,
        marking_schema={
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": f"Correct reflection rule applied for {axis}", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Correct final equation: {res_eq}", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        hints={
            "1_nudge": f"Reflection in the $x$-axis means $y = -f(x)$. Reflection in the $y$-axis means $y = f(-x)$.",
            "2_concept": f"Apply the rule to the entire expression.",
            "3_breakdown": f"Result: ${res_eq}$.",
        },
        misconception_tags=["confused_reflection_axes"],
        keywords=["reflection", "transformations", "x-axis", "y-axis"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=2,
        mode="24_parabola_reflection_axes",
        difficulty="medium",
    )


# ---------------------------------------------------------------------------
# 25. Parabola & Hyperbola: Graph Feature Interpretation (with inline_svg)
# ---------------------------------------------------------------------------
def build_25_parabola_hyperbola_sketch_features(r: random.Random) -> Dict[str, Any]:
    h = r.choice([-2, 1, 3])
    k = r.choice([-4, 2, 5])
    a = -1 if k > 0 else 1

    d_spec = _cartesian_parabola_svg(
        a=float(a),
        h=float(h),
        k=float(k),
        tp_label="T",
    )

    prompt = (
        f"In the accompanying graph, the parabola has its vertex at $T({h}; {k})$.\n\n"
        f"1. Write down the equation of the axis of symmetry.\n"
        f"2. Write down the range of the function."
    )
    range_str = rf"y \le {k}" if a < 0 else rf"y \ge {k}"
    ans_latex = rf"x = {h}, \; {range_str}"
    sample = (
        rf"1. \text{{Axis of symmetry: }} x = {h}\\"
        rf"2. \text{{Since }} a {'< 0' if a < 0 else '> 0'}\text{{, the range is }} {range_str}"
    )

    return make_math_question(
        prefix="func_25",
        topic=TOPIC,
        subskill="25_parabola_hyperbola_sketch_features",
        learning_objective_id=f"{LO_PREFIX}_sketch_features",
        prompt=prompt,
        prompt_latex=rf"T({h}; {k})",
        answer_latex=ans_latex,
        answer_sympy=ans_latex,
        sample_answer=sample,
        marking_schema={
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": f"Axis of symmetry x = {h}", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Range: {range_str}", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        hints={
            "1_nudge": "Read the $x$-coordinate of the turning point for the axis of symmetry.",
            "2_concept": "Read the maximum/minimum $y$-value for the range.",
            "3_breakdown": f"Axis: $x = {h}$, Range: ${range_str}$.",
        },
        misconception_tags=["read_wrong_coordinate_for_axis"],
        keywords=["parabola", "sketch interpretation", "axis of symmetry", "range"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=2,
        mode="25_parabola_hyperbola_sketch_features",
        difficulty="medium",
        diagram_spec=d_spec,
    )


# ---------------------------------------------------------------------------
# Registry Map of Archetypes 01–25
# ---------------------------------------------------------------------------
ARCHETYPES_01_25 = {
    "01_parabola_turning_point_vertex_form": build_01_parabola_turning_point_vertex_form,
    "02_parabola_axis_of_symmetry": build_02_parabola_axis_of_symmetry,
    "03_parabola_y_intercept": build_03_parabola_y_intercept,
    "04_parabola_x_intercepts": build_04_parabola_x_intercepts,
    "05_parabola_domain_and_range": build_05_parabola_domain_and_range,
    "06_parabola_turning_point_standard_form": build_06_parabola_turning_point_standard_form,
    "07_parabola_equation_from_turning_point_and_point": build_07_parabola_equation_from_turning_point_and_point,
    "08_parabola_equation_from_roots_and_point": build_08_parabola_equation_from_roots_and_point,
    "09_parabola_maximum_or_minimum_value": build_09_parabola_maximum_or_minimum_value,
    "10_parabola_vertical_horizontal_shifts": build_10_parabola_vertical_horizontal_shifts,
    "11_hyperbola_vertical_asymptote": build_11_hyperbola_vertical_asymptote,
    "12_hyperbola_horizontal_asymptote": build_12_hyperbola_horizontal_asymptote,
    "13_hyperbola_center_of_symmetry": build_13_hyperbola_center_of_symmetry,
    "14_hyperbola_axis_of_symmetry_positive_gradient": build_14_hyperbola_axis_of_symmetry_positive_gradient,
    "15_hyperbola_axis_of_symmetry_negative_gradient": build_15_hyperbola_axis_of_symmetry_negative_gradient,
    "16_hyperbola_domain": build_16_hyperbola_domain,
    "17_hyperbola_range": build_17_hyperbola_range,
    "18_hyperbola_y_intercept": build_18_hyperbola_y_intercept,
    "19_hyperbola_x_intercept": build_19_hyperbola_x_intercept,
    "20_hyperbola_equation_from_asymptotes_and_point": build_20_hyperbola_equation_from_asymptotes_and_point,
    "21_parabola_hyperbola_intersection": build_21_parabola_hyperbola_intersection,
    "22_parabola_intervals_of_increase_decrease": build_22_parabola_intervals_of_increase_decrease,
    "23_hyperbola_quadrant_branches_effect_of_a": build_23_hyperbola_quadrant_branches_effect_of_a,
    "24_parabola_reflection_axes": build_24_parabola_reflection_axes,
    "25_parabola_hyperbola_sketch_features": build_25_parabola_hyperbola_sketch_features,
}
