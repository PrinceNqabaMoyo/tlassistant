"""Grade 12 Mathematics — Analytical Geometry: Circles (Deterministic 6-Pillar Generator).
Covers official CAPS Examination standards (Level 3 & Level 4: 40 marks in NSC Paper 2).
Supports full compound exam questions and atomic elementary sub-drills for adaptive deconstruction.
"""
from __future__ import annotations

import math
from typing import Any, Dict, List, Optional
import sympy as sp

from app.utils.grade12_mathematics._math_common import (
    make_id,
    make_math_question,
    nonzero,
    num,
    rng,
    solution_graph,
    step,
    to_latex,
)

TOPIC = "analytical_geometry_circles"
LO = "math12_analytical_circles"
x = sp.Symbol("x")
y = sp.Symbol("y")


# --------------------------------------------------------------------------- #
# Sub-Drill: Completing the Square to find Center and Radius
# --------------------------------------------------------------------------- #
def _build_completing_square(r, difficulty: str) -> Dict[str, Any]:
    a = nonzero(r, -5, 5)
    b = nonzero(r, -5, 5)
    radius_int = r.randint(3, 7)
    r_sq = radius_int**2

    # (x - a)^2 + (y - b)^2 = r_sq
    # x^2 - 2ax + y^2 - 2by + (a^2 + b^2 - r_sq) = 0
    D = -2 * a
    E = -2 * b
    F = a**2 + b**2 - r_sq

    expanded_eq_str = f"x^2 + y^2 {'+' if D >= 0 else ''}{D}x {'+' if E >= 0 else ''}{E}y {'+' if F >= 0 else ''}{F} = 0"

    steps = [
        step(
            from_latex=expanded_eq_str,
            to_latex_str=f"(x^2 {'+' if D >= 0 else ''}{D}x) + (y^2 {'+' if E >= 0 else ''}{E}y) = {-F}",
            op="group x and y terms and move constant to right",
            rule="algebraic rearrangement",
        ),
        step(
            from_latex=f"(x^2 {'+' if D >= 0 else ''}{D}x) + (y^2 {'+' if E >= 0 else ''}{E}y) = {-F}",
            to_latex_str=f"(x^2 {'+' if D >= 0 else ''}{D}x + {a**2}) + (y^2 {'+' if E >= 0 else ''}{E}y + {b**2}) = {-F} + {a**2} + {b**2}",
            op="complete the square by adding (half coefficient)^2 to both sides",
            rule="completing the square",
            common_errors=["forgot_add_both_sides", "halving_coefficient_error"],
        ),
        step(
            from_latex=f"(x {'-' if a >= 0 else '+'}{abs(a)})^2 + (y {'-' if b >= 0 else '+'}{abs(b)})^2 = {r_sq}",
            to_latex_str=f"\\text{{Centre }} M({a}; {b}), \\quad \\text{{Radius }} r = \\sqrt{{{r_sq}}} = {radius_int}",
            op="identify center and radius from standard form (x-a)^2 + (y-b)^2 = r^2",
            rule="standard circle equation",
        ),
    ]

    canonical = solution_graph(
        goal="determine centre and radius of circle by completing the square",
        steps=steps,
        final_latex=f"\\text{{Centre }} ({a}; {b}), \\quad r = {radius_int}",
    )

    marking_schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": "Grouping terms and adding (D/2)^2 and (E/2)^2 to both sides", "marks": 2, "editable": True},
            {"id": "mp2", "desc": "Correct centre coordinates (a; b)", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Correct radius r", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "sign_inversion_of_center", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "nudge": "Group the $x$ terms and $y$ terms, then complete the square for both variables.",
        "concept": "Take half of the coefficient of $x$, square it, and add it to BOTH sides of the equation. Do the same for $y$.",
        "breakdown": f"Add $(\\frac{{{D}}}{{2}})^2 = {a**2}$ and $(\\frac{{{E}}}{{2}})^2 = {b**2}$ to both sides. The equation becomes $(x - ({a}))^2 + (y - ({b}))^2 = {r_sq}$. Centre: $({a}; {b})$, radius: $r = {radius_int}$.",
    }

    return make_math_question(
        prefix="geo_csq",
        topic=TOPIC,
        subskill="elementary_completing_square_radius",
        learning_objective_id=f"{LO}_completing_square",
        prompt=f"A circle has the equation ${expanded_eq_str}$. Determine the coordinates of its centre and the length of its radius.",
        prompt_latex=expanded_eq_str,
        answer_latex=f"\\text{{Centre }} ({a}; {b}), \\quad r = {radius_int}",
        answer_sympy=f"Centre=({a},{b}), r={radius_int}",
        canonical_solution=canonical,
        marking_schema=marking_schema,
        hints=hints,
        misconception_tags=["sign_inversion_of_center", "forgot_to_square_root_radius", "forgot_add_both_sides"],
        keywords=["circle", "completing the square", "centre", "radius", "analytical geometry"],
        mode="elementary_completing_square_radius",
        difficulty="medium",
    )


# --------------------------------------------------------------------------- #
# Sub-Drill: Tangent Line Equation via Perpendicular Radius
# --------------------------------------------------------------------------- #
def _build_tangent_line(r, difficulty: str) -> Dict[str, Any]:
    # Pick clean Pythagorean triples for radius so slope is nice
    # Let center be M(0, 0) or M(a, b)
    a = r.randint(-3, 3)
    b = r.randint(-3, 3)
    dx, dy = r.choice([(3, 4), (4, 3), (-3, 4), (4, -3), (5, 12), (12, 5)])
    px = a + dx
    py = b + dy
    r_sq = dx**2 + dy**2
    radius_val = int(math.isqrt(r_sq))

    m_rad = sp.Rational(dy, dx)
    m_tan = -1 / m_rad
    c_tan = py - m_tan * px
    tan_eq = m_tan * x + c_tan

    steps = [
        step(
            from_latex=f"M({a}; {b}), \\quad P({px}; {py})",
            to_latex_str=f"m_{{\\text{{radius}}}} = \\frac{{{py} - ({b})}}{{{px} - ({a})}} = \\frac{{{dy}}}{{{dx}}} = {to_latex(m_rad)}",
            op="calculate gradient of radius MP",
            rule="gradient formula",
        ),
        step(
            from_latex=f"m_{{\\text{{radius}}}} \\times m_{{\\text{{tangent}}}} = -1",
            to_latex_str=f"m_{{\\text{{tangent}}}} = -\\frac{{1}}{{{to_latex(m_rad)}}} = {to_latex(m_tan)}",
            op="use radius perpendicular to tangent at point of contact",
            rule="tangent perpendicular to radius",
        ),
        step(
            from_latex=f"y - y_1 = m(x - x_1)",
            to_latex_str=f"y - ({py}) = {to_latex(m_tan)}(x - ({px})) \\implies y = {to_latex(tan_eq)}",
            op="form equation of tangent line",
            rule="straight line equation",
        ),
    ]

    canonical = solution_graph(
        goal="determine equation of tangent to circle at given point",
        steps=steps,
        final_expr=tan_eq,
        final_latex=f"y = {to_latex(tan_eq)}",
    )

    marking_schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": "Gradient of radius MP", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Gradient of tangent using m1 * m2 = -1", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Substitution of point P and m into straight line formula", "marks": 1, "editable": True},
            {"id": "mp4", "desc": "Final tangent equation in form y = mx + c", "marks": 1, "editable": True},
        ],
        "deductions": [],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "nudge": "First find the gradient of the radius connecting the centre to the point of contact.",
        "concept": "A tangent to a circle is perpendicular to the radius at the point of contact ($m_{\\text{rad}} \\times m_{\\text{tan}} = -1$).",
        "breakdown": f"Radius gradient is $m_{{\\text{{rad}}}} = {to_latex(m_rad)}$. Thus $m_{{\\text{{tan}}}} = {to_latex(m_tan)}$. Substituting $P({px}; {py})$ gives $y = {to_latex(tan_eq)}$.",
    }

    return make_math_question(
        prefix="geo_tan",
        topic=TOPIC,
        subskill="elementary_tangent_line_eq",
        learning_objective_id=f"{LO}_tangent_line",
        prompt=f"A circle with centre $M({a}; {b})$ has a point $P({px}; {py})$ on its circumference. Determine the equation of the tangent to the circle at point $P$.",
        prompt_latex=f"M({a}; {b}),\\quad P({px}; {py})",
        answer_latex=f"y = {to_latex(tan_eq)}",
        answer_sympy=sp.srepr(tan_eq),
        canonical_solution=canonical,
        marking_schema=marking_schema,
        hints=hints,
        misconception_tags=["used_tangent_instead_of_perpendicular", "sign_error_gradient_inversion"],
        keywords=["circle tangent", "perpendicular gradient", "point of contact", "radius"],
        mode="elementary_tangent_line_eq",
        difficulty="medium",
    )


# --------------------------------------------------------------------------- #
# Compound Level 3 & 4 Exam Question: Complete Circle Geometry Synthesis
# --------------------------------------------------------------------------- #
def _build_compound_circle(r, difficulty: str) -> Dict[str, Any]:
    a = nonzero(r, -3, 3)
    b = nonzero(r, -3, 3)
    dx, dy = r.choice([(3, 4), (-4, 3), (4, 3), (3, -4)])
    px = a + dx
    py = b + dy
    r_sq = dx**2 + dy**2
    radius_val = 5

    m_rad = sp.Rational(dy, dx)
    m_tan = -1 / m_rad
    c_tan = py - m_tan * px
    tan_eq = m_tan * x + c_tan

    # Intersecting line: y-intercept of the tangent line
    # When x = 0: y = c_tan
    y_int = c_tan

    circle_std_str = f"(x {'-' if a >= 0 else '+'}{abs(a)})^2 + (y {'-' if b >= 0 else '+'}{abs(b)})^2 = {r_sq}"

    steps = [
        step(
            from_latex=f"\\text{{Circle: }} {circle_std_str}",
            to_latex_str=f"\\text{{Centre }} M({a}; {b}), \\quad r = {radius_val}",
            op="read centre and radius",
            rule="circle standard form",
        ),
        step(
            from_latex=f"M({a}; {b}), P({px}; {py})",
            to_latex_str=f"m_{{\\text{{MP}}}} = \\frac{{{py} - ({b})}}{{{px} - ({a})}} = {to_latex(m_rad)} \\implies m_{{\\text{{tangent}}}} = {to_latex(m_tan)}",
            op="find perpendicular gradient",
            rule="tangent perpendicular to radius",
        ),
        step(
            from_latex=f"y - {py} = {to_latex(m_tan)}(x - {px})",
            to_latex_str=f"y = {to_latex(tan_eq)}",
            op="form tangent equation",
            rule="point-slope formula",
        ),
        step(
            from_latex=f"y = {to_latex(tan_eq)}, \\quad x = 0",
            to_latex_str=f"T(0; {to_latex(y_int)})",
            op="find y-intercept of tangent",
            rule="axes intercept",
        ),
    ]

    canonical = solution_graph(
        goal="complete circle analysis: centre, radius, tangent equation, and axis intercept",
        steps=steps,
        final_expr=tan_eq,
        final_latex=f"\\text{{Tangent: }} y = {to_latex(tan_eq)}; \\quad T(0; {to_latex(y_int)})",
    )

    marking_schema = {
        "total_marks": 9,
        "marking_points": [
            {"id": "mp1", "desc": "Coordinates of centre M and radius", "marks": 2, "editable": True},
            {"id": "mp2", "desc": "Gradient of radius MP", "marks": 2, "editable": True},
            {"id": "mp3", "desc": "Gradient of tangent line", "marks": 1, "editable": True},
            {"id": "mp4", "desc": "Equation of tangent line", "marks": 2, "editable": True},
            {"id": "mp5", "desc": "Coordinates of y-intercept T", "marks": 2, "editable": True},
        ],
        "deductions": [],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "nudge": "Extract the centre $M$, find the gradient of the radius $MP$, then deduce the perpendicular tangent gradient.",
        "concept": "The tangent touches the circle at $P({px}; {py})$. Its gradient satisfies $m_{\\text{tan}} = -1 / m_{\\text{MP}}$.",
        "breakdown": f"Radius gradient is ${to_latex(m_rad)}$. Tangent gradient is ${to_latex(m_tan)}$. Tangent equation is $y = {to_latex(tan_eq)}$. The $y$-intercept is at $(0; {to_latex(y_int)})$.",
    }

    return make_math_question(
        prefix="geo_circle_compound",
        topic=TOPIC,
        subskill="circle_tangent_synthesis",
        learning_objective_id=f"{LO}_compound_circles",
        prompt=(
            f"The equation of a circle is given by ${circle_std_str}$.\n\n"
            f"1. Write down the coordinates of the centre $M$ and the radius of the circle.\n"
            f"2. Verify that the point $P({px}; {py})$ lies on the circle.\n"
            f"3. Determine the equation of the tangent to the circle at point $P$.\n"
            f"4. The tangent intersects the $y$-axis at point $T$. Determine the coordinates of $T$."
        ),
        prompt_latex=circle_std_str,
        answer_latex=f"M({a}; {b}), r = {radius_val}; \\quad \\text{{Tangent: }} y = {to_latex(tan_eq)}; \\quad T(0; {to_latex(y_int)})",
        answer_sympy=sp.srepr(tan_eq),
        canonical_solution=canonical,
        marking_schema=marking_schema,
        hints=hints,
        misconception_tags=["sign_inversion_of_center", "used_tangent_instead_of_perpendicular", "intercept_coordinate_confusion"],
        keywords=["circle", "tangent line", "perpendicular gradient", "intercepts", "analytical geometry"],
        term=2,
        caps_weight_percent=25,
        suggested_duration_mins=12,
        mode="compound",
        difficulty="hard",
    )


# --------------------------------------------------------------------------- #
# Public Generator Dispatcher
# --------------------------------------------------------------------------- #
BUILDERS = {
    "compound": _build_compound_circle,
    "elementary_completing_square_radius": _build_completing_square,
    "elementary_tangent_line_eq": _build_tangent_line,
}


def generate(
    subskill: Optional[str] = None,
    difficulty: str = "hard",
    count: int = 1,
    seed: Optional[int] = None,
    mode: str = "compound",
    **kwargs: Any,
) -> Dict[str, Any]:
    """Generates deterministic Grade 12 Analytical Geometry (Circles) questions."""
    base_seed = 42 if seed is None else int(seed)
    chosen_mode = mode if mode in BUILDERS else ("compound" if subskill is None else subskill)
    builder = BUILDERS.get(chosen_mode, _build_compound_circle)

    questions = []
    for i in range(max(1, count)):
        r = rng(base_seed * 1000 + i)
        q = builder(r, difficulty)
        q["seed"] = base_seed * 1000 + i
        questions.append(q)

    return {"questions": questions}
