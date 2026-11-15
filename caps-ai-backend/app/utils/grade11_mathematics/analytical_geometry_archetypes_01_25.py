"""Grade 11 Mathematics — Analytical Geometry Archetypes 01–25.
Grounded in South African National Curriculum Standards for Grade 11 Mathematics (Term 2).
Covers:
- Distance formula and missing coordinates
- Midpoint formula and finding endpoints
- Gradients: two points, horizontal/vertical lines, parallel lines (m1 = m2), perpendicular lines (m1 * m2 = -1)
- Collinear points proofs and solving for unknown coordinates
- Equations of straight lines: gradient-intercept, point-gradient, two-point, parallel/perpendicular lines
- Angle of inclination: acute (m > 0), obtuse (m < 0), angle between lines, inclination from two points
- Triangle coordinate geometry: right-angled, isosceles, equilateral, medians, altitudes with inline_svg
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional, Tuple
import sympy as sp

from app.utils.grade11_mathematics._math_common import (
    make_math_question,
    step,
    solution_graph,
    num,
)

TOPIC = "Analytical geometry"
LO_PREFIX = "math11_analgeo"


def _cartesian_geometry_svg(
    points: List[Tuple[float, float, str]],
    segments: Optional[List[Tuple[int, int]]] = None,
    right_angle_at: Optional[int] = None,
) -> Dict[str, Any]:
    """Generates an inline SVG showing Cartesian plane with plotted points and connecting line segments."""
    ox, oy = 210, 150
    scale = 16.0

    svg_elements = []

    # Draw segments first (behind points)
    if segments:
        for idx1, idx2 in segments:
            if 0 <= idx1 < len(points) and 0 <= idx2 < len(points):
                x1, y1, _ = points[idx1]
                x2, y2, _ = points[idx2]
                sx1 = ox + x1 * scale
                sy1 = oy - y1 * scale
                sx2 = ox + x2 * scale
                sy2 = oy - y2 * scale
                svg_elements.append(
                    f'<line x1="{sx1:.1f}" y1="{sy1:.1f}" x2="{sx2:.1f}" y2="{sy2:.1f}" stroke="#2563eb" stroke-width="2"/>'
                )

    # Draw points and labels
    for x, y, lbl in points:
        sx = ox + x * scale
        sy = oy - y * scale
        svg_elements.append(f'<circle cx="{sx:.1f}" cy="{sy:.1f}" r="4" fill="#dc2626"/>')
        x_int = int(x) if isinstance(x, (int, float)) and float(x).is_integer() else x
        y_int = int(y) if isinstance(y, (int, float)) and float(y).is_integer() else y
        coord_txt = f"{lbl}({x_int}; {y_int})" if lbl else f"({x_int}; {y_int})"
        svg_elements.append(
            f'<text x="{sx + 6:.1f}" y="{sy - 6:.1f}" font-size="12" fill="#1e293b" font-weight="bold">{coord_txt}</text>'
        )

    content = "".join(svg_elements)

    svg = (
        f'<svg viewBox="0 0 420 300" width="100%" height="250" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="420" height="300" fill="#f8fafc" rx="8"/>'
        f'<line x1="20" y1="{oy}" x2="400" y2="{oy}" stroke="#94a3b8" stroke-width="1.8"/>'
        f'<line x1="{ox}" y1="280" x2="{ox}" y2="20" stroke="#94a3b8" stroke-width="1.8"/>'
        f'<text x="405" y="{oy + 4}" font-size="13" fill="#334155" font-weight="bold">x</text>'
        f'<text x="{ox - 5}" y="15" font-size="13" fill="#334155" font-weight="bold">y</text>'
        f'{content}'
        f'</svg>'
    )
    return {
        "kind": "inline_svg",
        "svg": svg,
        "diagram_role": "context",
        "points_count": len(points),
    }


# ---------------------------------------------------------------------------
# 01. Distance Between Two Points Direct
# ---------------------------------------------------------------------------
def build_01_distance_between_two_points_direct(r: random.Random) -> Dict[str, Any]:
    triples = [(3, 4, 5), (6, 8, 10), (5, 12, 13), (8, 15, 17)]
    dx, dy, dist = r.choice(triples)
    x1 = r.randint(-5, 3)
    y1 = r.randint(-4, 4)
    x2 = x1 + dx
    y2 = y1 + dy

    prompt = (
        f"Calculate the distance between the points $A({x1}; {y1})$ and $B({x2}; {y2})$. "
        f"Give your answer in simplest surd or integer form."
    )
    ans_latex = f"{dist} \\text{{ units}}"
    sample = (
        rf"d = \sqrt{{(x_2 - x_1)^2 + (y_2 - y_1)^2}}\\"
        rf"d = \sqrt{{({x2} - ({x1}))^2 + ({y2} - ({y1}))^2}}\\"
        rf"d = \sqrt{{({dx})^2 + ({dy})^2}} = \sqrt{{{dx*dx} + {dy*dy}}} = \sqrt{{{dist*dist}}} = {dist}\text{{ units}}"
    )

    return make_math_question(
        prefix="analgeo_01",
        topic=TOPIC,
        subskill="01_distance_between_two_points_direct",
        learning_objective_id=f"{LO_PREFIX}_dist_direct",
        prompt=prompt,
        prompt_latex=rf"A({x1}; {y1}), \; B({x2}; {y2})",
        answer_latex=ans_latex,
        answer_sympy=str(dist),
        sample_answer=sample,
        marking_schema={
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Correct distance formula substitution", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Correct distance: {dist} units", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        hints={
            "1_nudge": "Use the distance formula: $d = \\sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$.",
            "2_concept": "Substitute $(x_1; y_1)$ and $(x_2; y_2)$ into the formula.",
            "3_breakdown": f"Distance is $\\sqrt{{{dx}^2 + {dy}^2}} = {dist}$ units.",
        },
        misconception_tags=["sign_error_subtracting_negative_coordinates"],
        keywords=["distance formula", "Cartesian plane", "length of segment"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=2,
        mode="01_distance_between_two_points_direct",
        difficulty="easy",
    )


# ---------------------------------------------------------------------------
# 02. Distance Formula: Missing Coordinate
# ---------------------------------------------------------------------------
def build_02_distance_formula_missing_coordinate(r: random.Random) -> Dict[str, Any]:
    dx, dy, dist = 3, 4, 5
    x1, y1 = 1, 2
    # B(x; y2) where y2 = y1 + dy = 6, and dx = 3 => x - 1 = +-3 => x = 4 or x = -2
    y2 = y1 + dy
    prompt = (
        f"The distance between the points $A({x1}; {y1})$ and $B(x; {y2})$ is {dist} units.\n\n"
        f"Determine the possible values of $x$."
    )
    ans_latex = r"x = 4 \quad \text{or} \quad x = -2"
    sample = (
        rf"AB^2 = (x - x_1)^2 + (y_2 - y_1)^2\\"
        rf"{dist}^2 = (x - {x1})^2 + ({y2} - {y1})^2\\"
        rf"25 = (x - 1)^2 + 16 \implies (x - 1)^2 = 9\\"
        rf"x - 1 = \pm 3 \implies x = 4 \text{{ or }} x = -2"
    )

    return make_math_question(
        prefix="analgeo_02",
        topic=TOPIC,
        subskill="02_distance_formula_missing_coordinate",
        learning_objective_id=f"{LO_PREFIX}_dist_missing_coord",
        prompt=prompt,
        prompt_latex=rf"A({x1}; {y1}), \; B(x; {y2}), \; d = {dist}",
        answer_latex=ans_latex,
        answer_sympy="4, -2",
        sample_answer=sample,
        marking_schema={
            "total_marks": 4,
            "marking_points": [
                {"id": "mp1", "desc": "Setup distance equation squared", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Simplified to (x - 1)^2 = 9", "marks": 1, "editable": True},
                {"id": "mp3", "desc": "Positive root x = 4", "marks": 1, "editable": True},
                {"id": "mp4", "desc": "Negative root x = -2", "marks": 1, "editable": True},
            ],
            "deductions": [{"rule": "omitted_negative_square_root", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
        hints={
            "1_nudge": "Square both sides: $(x - x_1)^2 + (y_2 - y_1)^2 = d^2$.",
            "2_concept": "Remember that taking the square root yields both positive and negative solutions: $\\pm \\sqrt{9}$.",
            "3_breakdown": "$x = 4$ or $x = -2$.",
        },
        misconception_tags=["omitted_negative_root_distance"],
        keywords=["distance formula", "missing coordinate", "quadratic equation"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=3,
        mode="02_distance_formula_missing_coordinate",
        difficulty="medium",
    )


# ---------------------------------------------------------------------------
# 03. Midpoint of a Line Segment
# ---------------------------------------------------------------------------
def build_03_midpoint_of_line_segment(r: random.Random) -> Dict[str, Any]:
    mx = r.randint(-3, 4)
    my = r.randint(-3, 4)
    dx = r.choice([2, 4, 6])
    dy = r.choice([2, 4, 6])

    x1 = mx - dx // 2
    x2 = mx + dx // 2
    y1 = my - dy // 2
    y2 = my + dy // 2

    prompt = f"Calculate the coordinates of the midpoint $M$ of the segment joining $A({x1}; {y1})$ and $B({x2}; {y2})$."
    ans_latex = rf"M({mx}; {my})"
    sample = (
        rf"M\left(\frac{{x_1 + x_2}}{{2}}; \frac{{y_1 + y_2}}{{2}}\right)\\"
        rf"= M\left(\frac{{{x1} + ({x2})}}{{2}}; \frac{{{y1} + ({y2})}}{{2}}\right)\\"
        rf"= M\left(\frac{{{x1 + x2}}}{{2}}; \frac{{{y1 + y2}}}{{2}}\right) = M({mx}; {my})"
    )

    return make_math_question(
        prefix="analgeo_03",
        topic=TOPIC,
        subskill="03_midpoint_of_line_segment",
        learning_objective_id=f"{LO_PREFIX}_midpoint",
        prompt=prompt,
        prompt_latex=rf"A({x1}; {y1}), \; B({x2}; {y2})",
        answer_latex=ans_latex,
        answer_sympy=f"({mx}, {my})",
        sample_answer=sample,
        marking_schema={
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Substituted into midpoint formula", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Correct midpoint coordinates: M({mx}; {my})", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        hints={
            "1_nudge": "The midpoint formula is $M\\left(\\frac{x_1 + x_2}{2}; \\frac{y_1 + y_2}{2}\\right)$.",
            "2_concept": "Average the two $x$-coordinates and average the two $y$-coordinates.",
            "3_breakdown": f"Midpoint is $M({mx}; {my})$.",
        },
        misconception_tags=["subtracted_coordinates_in_midpoint"],
        keywords=["midpoint formula", "line segment", "averaging coordinates"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=2,
        mode="03_midpoint_of_line_segment",
        difficulty="easy",
    )


# ---------------------------------------------------------------------------
# 04. Endpoint from Midpoint and One Endpoint
# ---------------------------------------------------------------------------
def build_04_endpoint_from_midpoint_and_one_endpoint(r: random.Random) -> Dict[str, Any]:
    mx = r.randint(-2, 3)
    my = r.randint(-2, 3)
    x1 = r.randint(-5, 1)
    y1 = r.randint(-4, 2)
    # mx = (x1 + x2)/2 => x2 = 2*mx - x1
    x2 = 2 * mx - x1
    y2 = 2 * my - y1

    prompt = (
        f"The midpoint of segment $AB$ is $M({mx}; {my})$. Given that point $A$ has coordinates "
        f"$({x1}; {y1})$, determine the coordinates of endpoint $B$."
    )
    ans_latex = rf"B({x2}; {y2})"
    sample = (
        rf"x_M = \frac{{x_A + x_B}}{{2}} \implies {mx} = \frac{{{x1} + x_B}}{{2}} \implies {x1} + x_B = {2*mx} \implies x_B = {x2}\\"
        rf"y_M = \frac{{y_A + y_B}}{{2}} \implies {my} = \frac{{{y1} + y_B}}{{2}} \implies {y1} + y_B = {2*my} \implies y_B = {y2}\\"
        rf"\therefore B({x2}; {y2})"
    )

    return make_math_question(
        prefix="analgeo_04",
        topic=TOPIC,
        subskill="04_endpoint_from_midpoint_and_one_endpoint",
        learning_objective_id=f"{LO_PREFIX}_endpoint_from_midpoint",
        prompt=prompt,
        prompt_latex=rf"M({mx}; {my}), \; A({x1}; {y1})",
        answer_latex=ans_latex,
        answer_sympy=f"({x2}, {y2})",
        sample_answer=sample,
        marking_schema={
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": "Setup midpoint equation for x and y", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Solved x_B = {x2}", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Solved y_B = {y2}", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        hints={
            "1_nudge": "Set up separate equations for $x$ and $y$: $\\frac{x_1 + x_2}{2} = x_M$.",
            "2_concept": "Multiply $x_M$ and $y_M$ by 2, then subtract the coordinates of $A$.",
            "3_breakdown": f"Endpoint is $B({x2}; {y2})$.",
        },
        misconception_tags=["calculated_midpoint_of_M_and_A"],
        keywords=["endpoint from midpoint", "midpoint formula", "coordinate algebra"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=2,
        mode="04_endpoint_from_midpoint_and_one_endpoint",
        difficulty="medium",
    )


# ---------------------------------------------------------------------------
# 05. Gradient Between Two Points
# ---------------------------------------------------------------------------
def build_05_gradient_between_two_points(r: random.Random) -> Dict[str, Any]:
    dx = r.choice([-3, -2, -1, 1, 2, 3])
    dy = r.choice([-4, -2, 2, 4, 6])
    x1 = r.randint(-4, 2)
    y1 = r.randint(-3, 3)
    x2 = x1 + dx
    y2 = y1 + dy

    m_frac = sp.Rational(dy, dx)
    ans_latex = sp.latex(m_frac)

    prompt = f"Calculate the gradient of the line passing through the points $A({x1}; {y1})$ and $B({x2}; {y2})$."
    sample = (
        rf"m = \frac{{y_2 - y_1}}{{x_2 - x_1}} = \frac{{{y2} - ({y1})}}{{{x2} - ({x1})}} = \frac{{{dy}}}{{{dx}}} = {ans_latex}"
    )

    return make_math_question(
        prefix="analgeo_05",
        topic=TOPIC,
        subskill="05_gradient_between_two_points",
        learning_objective_id=f"{LO_PREFIX}_gradient_direct",
        prompt=prompt,
        prompt_latex=rf"A({x1}; {y1}), \; B({x2}; {y2})",
        answer_latex=ans_latex,
        answer_sympy=str(m_frac),
        sample_answer=sample,
        marking_schema={
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Substituted into gradient formula", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Correct simplified gradient: {ans_latex}", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        hints={
            "1_nudge": "Use the gradient formula: $m = \\frac{y_2 - y_1}{x_2 - x_1}$.",
            "2_concept": "Remember: change in $y$ on top, change in $x$ on the bottom.",
            "3_breakdown": f"Gradient is ${ans_latex}$.",
        },
        misconception_tags=["inverted_gradient_fraction"],
        keywords=["gradient", "slope", "rate of change"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=2,
        mode="05_gradient_between_two_points",
        difficulty="easy",
    )


# ---------------------------------------------------------------------------
# 06. Gradient of Horizontal and Vertical Lines
# ---------------------------------------------------------------------------
def build_06_gradient_of_horizontal_and_vertical_lines(r: random.Random) -> Dict[str, Any]:
    line_type = r.choice(["horizontal", "vertical"])
    c = r.randint(-5, 5)

    if line_type == "horizontal":
        eq_latex = rf"y = {c}"
        ans_latex = "0"
        expl = "Horizontal lines have a constant $y$-value, so $\\Delta y = 0$. Gradient is $0$."
    else:
        eq_latex = rf"x = {c}"
        ans_latex = r"\text{undefined}"
        expl = "Vertical lines have $\\Delta x = 0$. Division by zero is undefined, so the gradient is undefined."

    prompt = f"State the gradient of the line with equation ${eq_latex}$."
    sample = expl

    return make_math_question(
        prefix="analgeo_06",
        topic=TOPIC,
        subskill="06_gradient_of_horizontal_and_vertical_lines",
        learning_objective_id=f"{LO_PREFIX}_horiz_vert_gradient",
        prompt=prompt,
        prompt_latex=eq_latex,
        answer_latex=ans_latex,
        answer_sympy=ans_latex,
        sample_answer=sample,
        marking_schema={
            "total_marks": 1,
            "marking_points": [
                {"id": "mp1", "desc": f"Correct gradient stated: {ans_latex}", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "strict",
        },
        hints={
            "1_nudge": f"Identify whether the line ${eq_latex}$ is horizontal or vertical.",
            "2_concept": "Horizontal line ($y = c$) has gradient $0$. Vertical line ($x = c$) has undefined gradient.",
            "3_breakdown": f"Gradient is {ans_latex}.",
        },
        misconception_tags=["confused_zero_and_undefined_gradient"],
        keywords=["horizontal line", "vertical line", "gradient", "undefined"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=1,
        mode="06_gradient_of_horizontal_and_vertical_lines",
        difficulty="easy",
    )


# ---------------------------------------------------------------------------
# 07. Parallel Lines: Equal Gradients
# ---------------------------------------------------------------------------
def build_07_parallel_lines_equal_gradients(r: random.Random) -> Dict[str, Any]:
    m = r.choice([-3, -2, 2, 4])
    c1 = r.randint(-4, 4)
    c2 = c1 + r.choice([2, 3])

    prompt = (
        f"A line $L_1$ has equation $y = {m}x + {c1}$. A second line $L_2$ is parallel to $L_1$ "
        f"and passes through the point $P(2; k)$ where $L_2$ has equation $y = {m}x + {c2}$.\n\n"
        f"Write down the gradient of $L_2$ and explain why."
    )
    ans_latex = rf"m = {m}"
    sample = (
        rf"\text{{Parallel lines have equal gradients: }} m_1 = m_2.\\"
        rf"\therefore \text{{Gradient of }} L_2 \text{{ is }} {m}"
    )

    return make_math_question(
        prefix="analgeo_07",
        topic=TOPIC,
        subskill="07_parallel_lines_equal_gradients",
        learning_objective_id=f"{LO_PREFIX}_parallel_gradients",
        prompt=prompt,
        prompt_latex=rf"L_1: y = {m}x + {c1}, \; L_1 \parallel L_2",
        answer_latex=ans_latex,
        answer_sympy=str(m),
        sample_answer=sample,
        marking_schema={
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": f"Correct gradient m = {m}", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Stated property: parallel lines have equal gradients", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "strict",
        },
        hints={
            "1_nudge": "What is the relationship between gradients of parallel lines?",
            "2_concept": "Parallel lines always have equal gradients ($m_1 = m_2$).",
            "3_breakdown": f"Gradient is ${m}$.",
        },
        misconception_tags=["inverted_parallel_gradient"],
        keywords=["parallel lines", "equal gradients"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=1,
        mode="07_parallel_lines_equal_gradients",
        difficulty="easy",
    )


# ---------------------------------------------------------------------------
# 08. Perpendicular Lines: Product m1 * m2 = -1
# ---------------------------------------------------------------------------
def build_08_perpendicular_lines_product_minus_one(r: random.Random) -> Dict[str, Any]:
    cases = [(2, r"-\frac{1}{2}"), (-3, r"\frac{1}{3}"), (r"\frac{3}{4}", r"-\frac{4}{3}"), (-1, "1")]
    m1_val, m2_latex = r.choice(cases)

    prompt = (
        f"Two straight lines $L_1$ and $L_2$ are perpendicular to each other ($L_1 \\perp L_2$).\n\n"
        f"If the gradient of $L_1$ is $m_1 = {m1_val}$, determine the gradient of $L_2$."
    )
    ans_latex = rf"m_2 = {m2_latex}"
    sample = (
        rf"m_1 \cdot m_2 = -1 \implies m_2 = -\frac{{1}}{{m_1}}\\"
        rf"\therefore m_2 = {m2_latex}"
    )

    return make_math_question(
        prefix="analgeo_08",
        topic=TOPIC,
        subskill="08_perpendicular_lines_product_minus_one",
        learning_objective_id=f"{LO_PREFIX}_perp_gradients",
        prompt=prompt,
        prompt_latex=rf"L_1 \perp L_2, \; m_1 = {m1_val}",
        answer_latex=ans_latex,
        answer_sympy=ans_latex,
        sample_answer=sample,
        marking_schema={
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Applied m1 * m2 = -1", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Correct negative reciprocal gradient: {m2_latex}", "marks": 1, "editable": True},
            ],
            "deductions": [{"rule": "forgot_negative_reciprocal_sign", "penalty": -1}],
            "carry_forward_rule": "strict",
        },
        hints={
            "1_nudge": "The gradients of perpendicular lines satisfy $m_1 \\cdot m_2 = -1$.",
            "2_concept": "Take the negative reciprocal: flip the fraction and change the sign.",
            "3_breakdown": f"Gradient is ${m2_latex}$.",
        },
        misconception_tags=["forgot_negative_sign_in_reciprocal"],
        keywords=["perpendicular lines", "negative reciprocal", "product minus one"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=2,
        mode="08_perpendicular_lines_product_minus_one",
        difficulty="easy",
    )


# ---------------------------------------------------------------------------
# 09. Collinear Points Proof
# ---------------------------------------------------------------------------
def build_09_collinear_points_proof(r: random.Random) -> Dict[str, Any]:
    m = r.choice([-2, 1, 2, 3])
    x1, y1 = 1, 2
    x2, y2 = 3, y1 + m * (3 - 1)
    x3, y3 = 5, y1 + m * (5 - 1)

    prompt = (
        f"Prove that the three points $A({x1}; {y1})$, $B({x2}; {y2})$, and $C({x3}; {y3})$ "
        f"are collinear by calculating the gradients $m_{{AB}}$ and $m_{{BC}}$."
    )
    ans_latex = rf"m_{{AB}} = m_{{BC}} = {m} \implies \text{{Points are collinear}}"
    sample = (
        rf"m_{{AB}} = \frac{{{y2} - {y1}}}{{{x2} - {x1}}} = \frac{{{y2 - y1}}}{{{x2 - x1}}} = {m}\\"
        rf"m_{{BC}} = \frac{{{y3} - {y2}}}{{{x3} - {x2}}} = \frac{{{y3 - y2}}}{{{x3 - x2}}} = {m}\\"
        rf"\text{{Since }} m_{{AB}} = m_{{BC}} \text{{ and point }} B \text{{ is common, }} A, B, \text{{ and }} C \text{{ are collinear.}}"
    )

    return make_math_question(
        prefix="analgeo_09",
        topic=TOPIC,
        subskill="09_collinear_points_proof",
        learning_objective_id=f"{LO_PREFIX}_collinear_proof",
        prompt=prompt,
        prompt_latex=rf"A({x1}; {y1}), \; B({x2}; {y2}), \; C({x3}; {y3})",
        answer_latex=ans_latex,
        answer_sympy=ans_latex,
        sample_answer=sample,
        marking_schema={
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": f"Calculated m_AB = {m}", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Calculated m_BC = {m}", "marks": 1, "editable": True},
                {"id": "mp3", "desc": "Concluded collinearity with common point statement", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        hints={
            "1_nudge": "Calculate the gradient of $AB$ and the gradient of $BC$.",
            "2_concept": "Points are collinear if they lie on the same straight line, meaning $m_{AB} = m_{BC}$.",
            "3_breakdown": f"Both gradients equal ${m}$, proving collinearity.",
        },
        misconception_tags=["gradient_arithmetic_error"],
        keywords=["collinear points", "equal gradients", "common point"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=3,
        mode="09_collinear_points_proof",
        difficulty="medium",
    )


# ---------------------------------------------------------------------------
# 10. Collinear Points: Find Unknown Coordinate
# ---------------------------------------------------------------------------
def build_10_collinear_points_find_unknown_coordinate(r: random.Random) -> Dict[str, Any]:
    m = 2
    # A(1; 3), B(2; 5), C(k; 9) => (9 - 3)/(k - 1) = 2 => 6 / (k - 1) = 2 => k - 1 = 3 => k = 4
    x1, y1 = 1, 3
    x2, y2 = 2, 5
    y3 = 9
    k_ans = 4

    prompt = (
        f"The points $A({x1}; {y1})$, $B({x2}; {y2})$, and $C(k; {y3})$ are collinear.\n\n"
        f"Calculate the value of $k$."
    )
    ans_latex = f"k = {k_ans}"
    sample = (
        rf"m_{{AB}} = \frac{{{y2} - {y1}}}{{{x2} - {x1}}} = \frac{{5 - 3}}{{2 - 1}} = 2\\"
        rf"\text{{Since points are collinear, }} m_{{AC}} = m_{{AB}} = 2:\\"
        rf"\frac{{{y3} - {y1}}}{{k - {x1}}} = 2 \implies \frac{{6}}{{k - 1}} = 2\\"
        rf"2(k - 1) = 6 \implies k - 1 = 3 \implies k = {k_ans}"
    )

    return make_math_question(
        prefix="analgeo_10",
        topic=TOPIC,
        subskill="10_collinear_points_find_unknown_coordinate",
        learning_objective_id=f"{LO_PREFIX}_collinear_solve",
        prompt=prompt,
        prompt_latex=rf"A({x1}; {y1}), \; B({x2}; {y2}), \; C(k; {y3})",
        answer_latex=ans_latex,
        answer_sympy=str(k_ans),
        sample_answer=sample,
        marking_schema={
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": "Calculated gradient m_AB = 2", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Setup collinearity equation (6 / (k - 1) = 2)", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Correct solution k = {k_ans}", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        hints={
            "1_nudge": "Find the gradient of $AB$ first.",
            "2_concept": "Equate the gradient of $AC$ to the gradient of $AB$ and solve for $k$.",
            "3_breakdown": f"Solving gives $k = {k_ans}$.",
        },
        misconception_tags=["algebra_error_clearing_variable_denominator"],
        keywords=["collinear", "unknown coordinate", "gradient equality"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=3,
        mode="10_collinear_points_find_unknown_coordinate",
        difficulty="medium",
    )


# ---------------------------------------------------------------------------
# 11. Equation of Straight Line: Gradient-Intercept Form
# ---------------------------------------------------------------------------
def build_11_equation_straight_line_gradient_intercept(r: random.Random) -> Dict[str, Any]:
    m = r.choice([-3, -2, -1, 2, 3])
    c = r.choice([-5, -3, 1, 4])
    c_str = f"+ {c}" if c > 0 else f"- {abs(c)}"
    res_eq = rf"y = {m}x {c_str}"

    prompt = (
        f"Write down the equation of the straight line with gradient $m = {m}$ and "
        f"$y$-intercept $(0; {c})$."
    )
    ans_latex = res_eq
    sample = (
        rf"y = mx + c \implies y = {m}x {c_str}"
    )

    return make_math_question(
        prefix="analgeo_11",
        topic=TOPIC,
        subskill="11_equation_straight_line_gradient_intercept",
        learning_objective_id=f"{LO_PREFIX}_line_gradient_intercept",
        prompt=prompt,
        prompt_latex=rf"m = {m}, \; c = {c}",
        answer_latex=ans_latex,
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
            "1_nudge": "Substitute $m$ and $c$ directly into $y = mx + c$.",
            "2_concept": "The $y$-intercept is $(0; c)$.",
            "3_breakdown": f"Result: ${res_eq}$.",
        },
        misconception_tags=["confused_gradient_and_intercept"],
        keywords=["equation of straight line", "gradient-intercept form"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=1,
        mode="11_equation_straight_line_gradient_intercept",
        difficulty="easy",
    )


# ---------------------------------------------------------------------------
# 12. Equation of Straight Line: Point and Gradient
# ---------------------------------------------------------------------------
def build_12_equation_straight_line_point_gradient(r: random.Random) -> Dict[str, Any]:
    m = r.choice([-2, 1, 2, 3])
    x1 = r.randint(-3, 3)
    y1 = r.randint(-4, 4)
    # y - y1 = m(x - x1) => y = mx - m*x1 + y1
    c = -m * x1 + y1
    c_str = f"+ {c}" if c > 0 else (f"- {abs(c)}" if c < 0 else "")
    res_eq = rf"y = {m}x {c_str}".strip()

    prompt = (
        f"Determine the equation of the line that passes through the point $P({x1}; {y1})$ "
        f"with gradient $m = {m}$."
    )
    sample = (
        rf"y - y_1 = m(x - x_1)\\"
        rf"y - ({y1}) = {m}(x - ({x1}))\\"
        rf"y - {y1} = {m}x - {m*x1}\\"
        rf"\therefore {res_eq}"
    )

    return make_math_question(
        prefix="analgeo_12",
        topic=TOPIC,
        subskill="12_equation_straight_line_point_gradient",
        learning_objective_id=f"{LO_PREFIX}_line_point_gradient",
        prompt=prompt,
        prompt_latex=rf"P({x1}; {y1}), \; m = {m}",
        answer_latex=res_eq,
        answer_sympy=res_eq,
        sample_answer=sample,
        marking_schema={
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Substituted into y - y1 = m(x - x1)", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Correct equation: {res_eq}", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        hints={
            "1_nudge": "Use the point-gradient formula: $y - y_1 = m(x - x_1)$.",
            "2_concept": "Expand and simplify into $y = mx + c$ form.",
            "3_breakdown": f"Result: ${res_eq}$.",
        },
        misconception_tags=["sign_error_in_point_gradient_expansion"],
        keywords=["equation of line", "point-gradient form"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=2,
        mode="12_equation_straight_line_point_gradient",
        difficulty="easy",
    )


# ---------------------------------------------------------------------------
# 13. Equation of Straight Line Passing Through Two Points (with inline_svg)
# ---------------------------------------------------------------------------
def build_13_equation_straight_line_two_points(r: random.Random) -> Dict[str, Any]:
    x1, y1 = 1, 2
    dx = r.choice([2, 3])
    m = r.choice([-2, 1, 2])
    x2 = x1 + dx
    y2 = y1 + m * dx

    c = -m * x1 + y1
    c_str = f"+ {c}" if c > 0 else (f"- {abs(c)}" if c < 0 else "")
    res_eq = rf"y = {m}x {c_str}".strip()

    d_spec = _cartesian_geometry_svg(
        points=[(float(x1), float(y1), "A"), (float(x2), float(y2), "B")],
        segments=[(0, 1)],
    )

    prompt = (
        f"In the accompanying diagram, line $AB$ passes through points $A({x1}; {y1})$ and $B({x2}; {y2})$.\n\n"
        f"Determine the equation of the line $AB$ in the form $y = mx + c$."
    )
    sample = (
        rf"m = \frac{{y_2 - y_1}}{{x_2 - x_1}} = \frac{{{y2} - {y1}}}{{{x2} - {x1}}} = \frac{{{y2 - y1}}}{{{dx}}} = {m}\\"
        rf"y - y_1 = m(x - x_1) \implies y - {y1} = {m}(x - {x1})\\"
        rf"\therefore {res_eq}"
    )

    return make_math_question(
        prefix="analgeo_13",
        topic=TOPIC,
        subskill="13_equation_straight_line_two_points",
        learning_objective_id=f"{LO_PREFIX}_line_two_points",
        prompt=prompt,
        prompt_latex=rf"A({x1}; {y1}), \; B({x2}; {y2})",
        answer_latex=res_eq,
        answer_sympy=res_eq,
        sample_answer=sample,
        marking_schema={
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": f"Calculated gradient m = {m}", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Substituted into point-gradient formula", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Final equation: {res_eq}", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        hints={
            "1_nudge": "Find the gradient $m = \\frac{y_2 - y_1}{x_2 - x_1}$ first.",
            "2_concept": "Then use $y - y_1 = m(x - x_1)$ with either point.",
            "3_breakdown": f"Result: ${res_eq}$.",
        },
        misconception_tags=["gradient_calculation_error"],
        keywords=["equation of line", "two points", "Cartesian plane"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=3,
        mode="13_equation_straight_line_two_points",
        difficulty="medium",
        diagram_spec=d_spec,
    )


# ---------------------------------------------------------------------------
# 14. Equation of Line Parallel Through Point
# ---------------------------------------------------------------------------
def build_14_equation_parallel_line_through_point(r: random.Random) -> Dict[str, Any]:
    m = r.choice([-3, -2, 2, 3])
    x1 = r.randint(-3, 3)
    y1 = r.randint(-4, 4)
    c = -m * x1 + y1
    c_str = f"+ {c}" if c > 0 else (f"- {abs(c)}" if c < 0 else "")
    res_eq = rf"y = {m}x {c_str}".strip()

    prompt = (
        f"Determine the equation of the line that is parallel to the line $y = {m}x + 7$ "
        f"and passes through the point $P({x1}; {y1})$."
    )
    sample = (
        rf"\text{{Since the lines are parallel, }} m = {m}:\\"
        rf"y - y_1 = m(x - x_1) \implies y - ({y1}) = {m}(x - ({x1}))\\"
        rf"\therefore {res_eq}"
    )

    return make_math_question(
        prefix="analgeo_14",
        topic=TOPIC,
        subskill="14_equation_parallel_line_through_point",
        learning_objective_id=f"{LO_PREFIX}_line_parallel",
        prompt=prompt,
        prompt_latex=rf"y = {m}x + 7, \; P({x1}; {y1})",
        answer_latex=res_eq,
        answer_sympy=res_eq,
        sample_answer=sample,
        marking_schema={
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": f"Identified parallel gradient m = {m}", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Correct equation: {res_eq}", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        hints={
            "1_nudge": "The parallel line has the exact same gradient $m = " + str(m) + "$.",
            "2_concept": "Substitute the point $P(x_1; y_1)$ and $m$ into $y - y_1 = m(x - x_1)$.",
            "3_breakdown": f"Result: ${res_eq}$.",
        },
        misconception_tags=["changed_parallel_gradient"],
        keywords=["parallel line", "equation of line", "point-slope form"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=2,
        mode="14_equation_parallel_line_through_point",
        difficulty="easy",
    )


# ---------------------------------------------------------------------------
# 15. Equation of Line Perpendicular Through Point
# ---------------------------------------------------------------------------
def build_15_equation_perpendicular_line_through_point(r: random.Random) -> Dict[str, Any]:
    m_orig = r.choice([2, 3, 4, 5])
    c_orig = r.choice([1, 2, 3, 5])
    k = r.choice([1, 2, 3])
    x1 = m_orig * k
    y1 = r.choice([1, 2, 3, 4, 5])
    c_perp = y1 + k
    res_eq = rf"y = -\frac{{1}}{{{m_orig}}}x + {c_perp}"

    prompt = (
        f"Determine the equation of the line that is perpendicular to the line $y = {m_orig}x + {c_orig}$ "
        f"and passes through the point $P({x1}; {y1})$."
    )
    ans_latex = res_eq
    sample = (
        rf"m_1 \cdot m_2 = -1 \implies {m_orig} \cdot m_2 = -1 \implies m_2 = -\frac{{1}}{{{m_orig}}}\\"
        rf"y - y_1 = m_2(x - x_1)\\"
        rf"y - {y1} = -\frac{{1}}{{{m_orig}}}(x - {x1}) = -\frac{{1}}{{{m_orig}}}x + {k}\\"
        rf"\therefore {res_eq}"
    )

    return make_math_question(
        prefix="analgeo_15",
        topic=TOPIC,
        subskill="15_equation_perpendicular_line_through_point",
        learning_objective_id=f"{LO_PREFIX}_line_perp",
        prompt=prompt,
        prompt_latex=rf"y = {m_orig}x + {c_orig}, \; P({x1}; {y1})",
        answer_latex=ans_latex,
        answer_sympy=res_eq,
        sample_answer=sample,
        marking_schema={
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": f"Calculated perpendicular gradient m = -1/{m_orig}", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Substituted into point-gradient formula", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Correct equation: {res_eq}", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        hints={
            "1_nudge": "Find the perpendicular gradient using $m_1 \\cdot m_2 = -1$.",
            "2_concept": f"The perpendicular gradient is $-\\frac{{1}}{{{m_orig}}}$.",
            "3_breakdown": f"Result: ${res_eq}$.",
        },
        misconception_tags=["sign_error_negative_reciprocal"],
        keywords=["perpendicular line", "negative reciprocal", "equation of line"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=3,
        mode="15_equation_perpendicular_line_through_point",
        difficulty="medium",
    )


# ---------------------------------------------------------------------------
# 16. Angle of Inclination: Positive Gradient (Acute)
# ---------------------------------------------------------------------------
def build_16_angle_of_inclination_positive_gradient(r: random.Random) -> Dict[str, Any]:
    cases = [(1, 45.0), (math.sqrt(3), 60.0), (1 / math.sqrt(3), 30.0)]
    m_val, theta = r.choice(cases)
    m_str = "1" if theta == 45 else (r"\sqrt{3}" if theta == 60 else r"\frac{1}{\sqrt{3}}")

    prompt = (
        f"A straight line has equation $y = {m_str}x + 3$.\n\n"
        f"Calculate the angle of inclination $\\theta$ of this line."
    )
    ans_latex = rf"\theta = {theta:.0f}^\circ"
    sample = (
        rf"\tan\theta = m = {m_str}\\"
        rf"\theta = \arctan({m_str}) = {theta:.0f}^\circ"
    )

    return make_math_question(
        prefix="analgeo_16",
        topic=TOPIC,
        subskill="16_angle_of_inclination_positive_gradient",
        learning_objective_id=f"{LO_PREFIX}_inclination_pos",
        prompt=prompt,
        prompt_latex=rf"m = {m_str}",
        answer_latex=ans_latex,
        answer_sympy=str(int(theta)),
        sample_answer=sample,
        marking_schema={
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Setup formula tan(theta) = m", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Correct angle: {theta:.0f} deg", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "strict",
        },
        hints={
            "1_nudge": "The angle of inclination satisfies $\\tan\\theta = m$.",
            "2_concept": "Since $m > 0$, the angle of inclination is an acute angle in Quadrant 1.",
            "3_breakdown": f"$\\theta = {theta:.0f}^\\circ$.",
        },
        misconception_tags=["forgot_arctan_formula"],
        keywords=["angle of inclination", "tangent", "acute angle"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=2,
        mode="16_angle_of_inclination_positive_gradient",
        difficulty="easy",
    )


# ---------------------------------------------------------------------------
# 17. Angle of Inclination: Negative Gradient (Obtuse)
# ---------------------------------------------------------------------------
def build_17_angle_of_inclination_negative_gradient(r: random.Random) -> Dict[str, Any]:
    cases = [(-1, 135.0, 45.0, "-1"), (-math.sqrt(3), 120.0, 60.0, r"-\sqrt{3}"), (-1 / math.sqrt(3), 150.0, 30.0, r"-\frac{1}{\sqrt{3}}")]
    m_val, theta, ref, m_str = r.choice(cases)

    prompt = (
        f"A straight line has gradient $m = {m_str}$.\n\n"
        f"Calculate the angle of inclination $\\theta$ of this line."
    )
    ans_latex = rf"\theta = {theta:.0f}^\circ"
    sample = (
        rf"\tan\theta = m = {m_str}\\"
        rf"\text{{Reference angle: }} \text{{ref}} = \arctan(|{m_str}|) = {ref:.0f}^\circ\\"
        rf"\text{{Since }} m < 0 \text{{, the inclination is obtuse:}}\\"
        rf"\theta = 180^\circ - {ref:.0f}^\circ = {theta:.0f}^\circ"
    )

    return make_math_question(
        prefix="analgeo_17",
        topic=TOPIC,
        subskill="17_angle_of_inclination_negative_gradient",
        learning_objective_id=f"{LO_PREFIX}_inclination_neg",
        prompt=prompt,
        prompt_latex=rf"m = {m_str}",
        answer_latex=ans_latex,
        answer_sympy=str(int(theta)),
        sample_answer=sample,
        marking_schema={
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": "Setup tan(theta) = m", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Found reference angle {ref:.0f} deg", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Correct obtuse inclination theta = 180 - ref = {theta:.0f} deg", "marks": 1, "editable": True},
            ],
            "deductions": [{"rule": "gave_negative_angle_for_inclination", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
        hints={
            "1_nudge": "The inclination angle $\\theta$ is measured from the positive $x$-axis and lies in $[0^\\circ; 180^\\circ)$.",
            "2_concept": "When $m < 0$, $\\theta = 180^\\circ - \\text{ref}$ or $\\theta = 180^\\circ + \\arctan(m)$.",
            "3_breakdown": f"$\\theta = {theta:.0f}^\\circ$.",
        },
        misconception_tags=["gave_negative_angle_for_inclination"],
        keywords=["angle of inclination", "obtuse angle", "negative gradient"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=2,
        mode="17_angle_of_inclination_negative_gradient",
        difficulty="medium",
    )


# ---------------------------------------------------------------------------
# 18. Angle Between Two Lines: Exterior Angle Theorem
# ---------------------------------------------------------------------------
def build_18_angle_between_two_lines_exterior_angle(r: random.Random) -> Dict[str, Any]:
    theta1 = r.choice([20, 25, 30, 35, 40, 45])
    diff_angle = r.choice([30, 35, 40, 45, 50, 55, 60])
    theta2 = theta1 + diff_angle

    prompt = (
        f"Two straight lines $L_1$ and $L_2$ intersect. The angle of inclination of $L_1$ is "
        f"$\\theta_1 = {theta1}^\\circ$ and the angle of inclination of $L_2$ is $\\theta_2 = {theta2}^\\circ$.\n\n"
        f"Calculate the acute angle of intersection between the two lines."
    )
    ans_latex = rf"{diff_angle}^\circ"
    sample = (
        rf"\text{{By the exterior angle of a triangle theorem:}}\\"
        rf"\theta = \theta_2 - \theta_1 = {theta2}^\circ - {theta1}^\circ = {diff_angle}^\circ"
    )

    return make_math_question(
        prefix="analgeo_18",
        topic=TOPIC,
        subskill="18_angle_between_two_lines_exterior_angle",
        learning_objective_id=f"{LO_PREFIX}_angle_between_lines",
        prompt=prompt,
        prompt_latex=rf"\theta_1 = {theta1}^\circ, \; \theta_2 = {theta2}^\circ",
        answer_latex=ans_latex,
        answer_sympy=str(diff_angle),
        sample_answer=sample,
        marking_schema={
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Subtracted inclination angles", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Correct acute angle: {diff_angle} deg", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        hints={
            "1_nudge": "The angle between two lines is the difference between their inclination angles.",
            "2_concept": "Exterior angle theorem: $\\theta = \\theta_2 - \\theta_1$.",
            "3_breakdown": f"Angle is ${diff_angle}^\\circ$.",
        },
        misconception_tags=["subtracted_angles_in_wrong_order"],
        keywords=["angle between lines", "inclination", "exterior angle theorem"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=2,
        mode="18_angle_between_two_lines_exterior_angle",
        difficulty="medium",
    )


# ---------------------------------------------------------------------------
# 19. Inclination from Two Points (with inline_svg)
# ---------------------------------------------------------------------------
def build_19_inclination_from_two_points(r: random.Random) -> Dict[str, Any]:
    x1 = r.choice([-3, -2, -1, 0, 1])
    y1 = r.choice([-2, -1, 0, 1, 2])
    span = r.choice([2, 3, 4])
    m_val = r.choice([1, -1])
    x2 = x1 + span
    y2 = y1 + m_val * span

    d_spec = _cartesian_geometry_svg(
        points=[(float(x1), float(y1), "A"), (float(x2), float(y2), "B")],
        segments=[(0, 1)],
    )

    angle_deg = 45 if m_val == 1 else 135
    ans_latex = rf"\theta = {angle_deg}^\circ"
    sample = (
        rf"m_{{AB}} = \frac{{{y2} - ({y1})}}{{{x2} - ({x1})}} = \frac{{{y2 - y1}}}{{{x2 - x1}}} = {m_val}\\"
        rf"\tan\theta = {m_val} \implies \theta = {angle_deg}^\circ"
    )

    prompt = (
        f"In the accompanying diagram, line segment $AB$ connects $A({x1}; {y1})$ and $B({x2}; {y2})$.\n\n"
        f"Calculate the angle of inclination $\\theta$ of line $AB$."
    )

    return make_math_question(
        prefix="analgeo_19",
        topic=TOPIC,
        subskill="19_inclination_from_two_points",
        learning_objective_id=f"{LO_PREFIX}_inclination_two_pts",
        prompt=prompt,
        prompt_latex=rf"A({x1}; {y1}), \; B({x2}; {y2})",
        answer_latex=ans_latex,
        answer_sympy=str(angle_deg),
        sample_answer=sample,
        marking_schema={
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": f"Calculated gradient m = {m_val}", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Setup tan(theta) = m", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Correct inclination theta = {angle_deg} deg", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        hints={
            "1_nudge": "First calculate the gradient between $A$ and $B$.",
            "2_concept": "Then apply $\\tan\\theta = m$.",
            "3_breakdown": f"$\\theta = {angle_deg}^\\circ$.",
        },
        misconception_tags=["gradient_error_in_inclination"],
        keywords=["angle of inclination", "two points", "Cartesian plane"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=3,
        mode="19_inclination_from_two_points",
        difficulty="medium",
        diagram_spec=d_spec,
    )


# ---------------------------------------------------------------------------
# 20. Gradient from Inclination Angle
# ---------------------------------------------------------------------------
def build_20_gradient_from_inclination_angle(r: random.Random) -> Dict[str, Any]:
    angle_deg = r.choice([30, 45, 60])
    if angle_deg == 30:
        ans_latex = r"\frac{1}{\sqrt{3}}"
    elif angle_deg == 45:
        ans_latex = "1"
    else:
        ans_latex = r"\sqrt{3}"

    prompt = (
        f"A straight line has an angle of inclination $\\theta = {angle_deg}^\\circ$.\n\n"
        f"Determine the exact gradient $m$ of the line without using a calculator."
    )
    sample = (
        rf"m = \tan\theta = \tan({angle_deg}^\circ) = {ans_latex}"
    )

    return make_math_question(
        prefix="analgeo_20",
        topic=TOPIC,
        subskill="20_gradient_from_inclination_angle",
        learning_objective_id=f"{LO_PREFIX}_grad_from_inclination",
        prompt=prompt,
        prompt_latex=rf"\theta = {angle_deg}^\circ",
        answer_latex=ans_latex,
        answer_sympy=ans_latex,
        sample_answer=sample,
        marking_schema={
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Setup formula m = tan(theta)", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Correct exact gradient: {ans_latex}", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "strict",
        },
        hints={
            "1_nudge": "The gradient is $m = \\tan\\theta$.",
            "2_concept": "Use special angle values for tangent.",
            "3_breakdown": f"Gradient is ${ans_latex}$.",
        },
        misconception_tags=["confused_tan_special_angles"],
        keywords=["gradient", "angle of inclination", "special angles"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=2,
        mode="20_gradient_from_inclination_angle",
        difficulty="easy",
    )


# ---------------------------------------------------------------------------
# 21. Proving Right-Angled Triangle by Gradient (with inline_svg)
# ---------------------------------------------------------------------------
def build_21_proving_right_angled_triangle_gradient(r: random.Random) -> Dict[str, Any]:
    sx = r.choice([-2, -1, 0, 1, 2])
    sy = r.choice([-2, -1, 0, 1, 2])
    A = (3 + sx, 5 + sy, "A")
    B = (1 + sx, 1 + sy, "B")
    C = (5 + sx, -1 + sy, "C")

    d_spec = _cartesian_geometry_svg(
        points=[(float(x), float(y), lbl) for x, y, lbl in [A, B, C]],
        segments=[(0, 1), (1, 2), (2, 0)],
    )

    prompt = (
        f"In the accompanying diagram, $\\triangle ABC$ has vertices $A({A[0]}; {A[1]})$, $B({B[0]}; {B[1]})$, and $C({C[0]}; {C[1]})$.\n\n"
        f"Prove that $\\triangle ABC$ is a right-angled triangle by showing that $AB \\perp BC$."
    )
    ans_latex = r"m_{AB} \cdot m_{BC} = -1 \implies \hat{B} = 90^\circ"
    sample = (
        rf"m_{{AB}} = \frac{{{A[1]} - ({B[1]})}}{{{A[0]} - ({B[0]})}} = \frac{{4}}{{2}} = 2\\"
        rf"m_{{BC}} = \frac{{{C[1]} - ({B[1]})}}{{{C[0]} - ({B[0]})}} = \frac{{-2}}{{4}} = -\frac{{1}}{{2}}\\"
        rf"m_{{AB}} \times m_{{BC}} = 2 \times \left(-\frac{{1}}{{2}}\right) = -1\\"
        rf"\therefore AB \perp BC \implies \triangle ABC \text{{ is right-angled at }} \hat{{B}}."
    )

    return make_math_question(
        prefix="analgeo_21",
        topic=TOPIC,
        subskill="21_proving_right_angled_triangle_gradient",
        learning_objective_id=f"{LO_PREFIX}_prove_right_triangle",
        prompt=prompt,
        prompt_latex=rf"A({A[0]}; {A[1]}), \; B({B[0]}; {B[1]}), \; C({C[0]}; {C[1]})",
        answer_latex=ans_latex,
        answer_sympy=ans_latex,
        sample_answer=sample,
        marking_schema={
            "total_marks": 4,
            "marking_points": [
                {"id": "mp1", "desc": "Calculated m_AB = 2", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Calculated m_BC = -1/2", "marks": 1, "editable": True},
                {"id": "mp3", "desc": "Showed m_AB * m_BC = -1", "marks": 1, "editable": True},
                {"id": "mp4", "desc": "Concluded AB perpendicular to BC and right-angled", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        hints={
            "1_nudge": "Calculate the gradients of sides $AB$ and $BC$.",
            "2_concept": "Two sides are perpendicular if the product of their gradients is $-1$.",
            "3_breakdown": "$m_{AB} \\cdot m_{BC} = 2 \\cdot (-\\frac{1}{2}) = -1 \\implies \\hat{B} = 90^\\circ$.",
        },
        misconception_tags=["perpendicular_gradient_proof_error"],
        keywords=["right-angled triangle", "perpendicular gradients", "coordinate proof"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=4,
        mode="21_proving_right_angled_triangle_gradient",
        difficulty="medium",
        diagram_spec=d_spec,
    )


# ---------------------------------------------------------------------------
# 22. Proving Isosceles Triangle by Distance (with inline_svg)
# ---------------------------------------------------------------------------
def build_22_proving_isosceles_triangle_distance(r: random.Random) -> Dict[str, Any]:
    w = r.choice([2, 3, 4])
    h = r.choice([3, 4, 5])
    sx = r.choice([-2, -1, 0, 1])
    sy = r.choice([-2, -1, 0, 1])
    B = (sx, sy, "B")
    C = (sx + 2 * w, sy, "C")
    A = (sx + w, sy + h, "A")
    dist_sq = w * w + h * h

    d_spec = _cartesian_geometry_svg(
        points=[(float(A[0]), float(A[1]), "A"), (float(B[0]), float(B[1]), "B"), (float(C[0]), float(C[1]), "C")],
        segments=[(0, 1), (1, 2), (2, 0)],
    )

    prompt = (
        f"In the accompanying diagram, $\\triangle ABC$ has vertices $A({A[0]}; {A[1]})$, $B({B[0]}; {B[1]})$, and $C({C[0]}; {C[1]})$.\n\n"
        f"Prove that $\\triangle ABC$ is an isosceles triangle by calculating the lengths of $AB$ and $AC$."
    )
    ans_latex = rf"AB = AC = \sqrt{{{dist_sq}}} \implies \triangle ABC \text{{ is isosceles}}"
    sample = (
        rf"AB = \sqrt{{({A[0]} - ({B[0]}))^2 + ({A[1]} - ({B[1]}))^2}} = \sqrt{{{w}^2 + {h}^2}} = \sqrt{{{dist_sq}}}\\"
        rf"AC = \sqrt{{({A[0]} - ({C[0]}))^2 + ({A[1]} - ({C[1]}))^2}} = \sqrt{{(-{w})^2 + {h}^2}} = \sqrt{{{dist_sq}}}\\"
        rf"\text{{Since }} AB = AC = \sqrt{{{dist_sq}}}, \; \triangle ABC \text{{ is an isosceles triangle.}}"
    )

    return make_math_question(
        prefix="analgeo_22",
        topic=TOPIC,
        subskill="22_proving_isosceles_triangle_distance",
        learning_objective_id=f"{LO_PREFIX}_prove_isosceles",
        prompt=prompt,
        prompt_latex=rf"A({A[0]}; {A[1]}), \; B({B[0]}; {B[1]}), \; C({C[0]}; {C[1]})",
        answer_latex=ans_latex,
        answer_sympy=ans_latex,
        sample_answer=sample,
        marking_schema={
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": f"Calculated AB = sqrt({dist_sq})", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Calculated AC = sqrt({dist_sq})", "marks": 1, "editable": True},
                {"id": "mp3", "desc": "Concluded AB = AC implies isosceles", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        hints={
            "1_nudge": "Use the distance formula to find the lengths of $AB$ and $AC$.",
            "2_concept": "An isosceles triangle has at least two sides of equal length.",
            "3_breakdown": f"$AB = AC = \\sqrt{{{dist_sq}}}$, so the triangle is isosceles.",
        },
        misconception_tags=["distance_calculation_error"],
        keywords=["isosceles triangle", "distance formula", "coordinate proof"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=3,
        mode="22_proving_isosceles_triangle_distance",
        difficulty="medium",
        diagram_spec=d_spec,
    )


# ---------------------------------------------------------------------------
# 23. Proving Equilateral Triangle by Distance
# ---------------------------------------------------------------------------
def build_23_proving_equilateral_triangle_distance(r: random.Random) -> Dict[str, Any]:
    prompt = (
        f"State the condition in terms of the distance formula required to prove that "
        f"$\\triangle PQR$ is an equilateral triangle in the Cartesian plane."
    )
    ans_latex = r"PQ = QR = PR"
    sample = (
        rf"\text{{All three side lengths must be calculated using the distance formula}}\\"
        rf"\text{{and proven equal: }} PQ = QR = PR"
    )

    return make_math_question(
        prefix="analgeo_23",
        topic=TOPIC,
        subskill="23_proving_equilateral_triangle_distance",
        learning_objective_id=f"{LO_PREFIX}_prove_equilateral",
        prompt=prompt,
        prompt_latex=r"PQ = QR = PR",
        answer_latex=ans_latex,
        answer_sympy=ans_latex,
        sample_answer=sample,
        marking_schema={
            "total_marks": 1,
            "marking_points": [
                {"id": "mp1", "desc": "Stated condition: PQ = QR = PR", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "strict",
        },
        hints={
            "1_nudge": "What is the defining geometric property of an equilateral triangle?",
            "2_concept": "An equilateral triangle has all three sides of equal length.",
            "3_breakdown": "$PQ = QR = PR$.",
        },
        misconception_tags=["confused_equilateral_and_isosceles"],
        keywords=["equilateral triangle", "distance formula", "properties"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=1,
        mode="23_proving_equilateral_triangle_distance",
        difficulty="easy",
    )


# ---------------------------------------------------------------------------
# 24. Triangle Median Equation (with inline_svg)
# ---------------------------------------------------------------------------
def build_24_triangle_median_equation(r: random.Random) -> Dict[str, Any]:
    sx = r.choice([-2, -1, 0, 1])
    sy = r.choice([-2, -1, 0, 1])
    A = (1 + sx, 5 + sy, "A")
    B = (0 + sx, 0 + sy, "B")
    C = (4 + sx, 2 + sy, "C")
    M = (2 + sx, 1 + sy, "M")
    c_val = 9 + 4 * sx + sy

    d_spec = _cartesian_geometry_svg(
        points=[(float(A[0]), float(A[1]), "A"), (float(B[0]), float(B[1]), "B"), (float(C[0]), float(C[1]), "C"), (float(M[0]), float(M[1]), "M")],
        segments=[(0, 1), (1, 2), (2, 0), (0, 3)],
    )

    c_str = f"+ {c_val}" if c_val >= 0 else f"- {abs(c_val)}"
    eq_str = rf"y = -4x {c_str}"
    prompt = (
        f"In $\\triangle ABC$ shown in the diagram, vertices are $A({A[0]}; {A[1]})$, $B({B[0]}; {B[1]})$, and $C({C[0]}; {C[1]})$.\n\n"
        f"1. Calculate the coordinates of $M$, the midpoint of side $BC$.\n"
        f"2. Determine the equation of the median line $AM$."
    )
    ans_latex = rf"M({M[0]}; {M[1]}), \; {eq_str}"
    sample = (
        rf"1. \text{{Midpoint }} M = \left(\frac{{{B[0]} + {C[0]}}}{{2}}; \frac{{{B[1]} + {C[1]}}}{{2}}\right) = M({M[0]}; {M[1]})\\"
        rf"2. \text{{Gradient of }} AM: m = \frac{{{M[1]} - ({A[1]})}}{{{M[0]} - ({A[0]})}} = \frac{{-4}}{{1}} = -4\\"
        rf"y - ({M[1]}) = -4(x - ({M[0]})) \implies {eq_str}"
    )

    return make_math_question(
        prefix="analgeo_24",
        topic=TOPIC,
        subskill="24_triangle_median_equation",
        learning_objective_id=f"{LO_PREFIX}_median_eq",
        prompt=prompt,
        prompt_latex=rf"A({A[0]}; {A[1]}), \; B({B[0]}; {B[1]}), \; C({C[0]}; {C[1]})",
        answer_latex=ans_latex,
        answer_sympy=ans_latex,
        sample_answer=sample,
        marking_schema={
            "total_marks": 4,
            "marking_points": [
                {"id": "mp1", "desc": f"Calculated midpoint M({M[0]}; {M[1]})", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Calculated gradient of AM = -4", "marks": 1, "editable": True},
                {"id": "mp3", "desc": "Substituted into point-gradient formula", "marks": 1, "editable": True},
                {"id": "mp4", "desc": f"Final equation: {eq_str}", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        hints={
            "1_nudge": "A median connects a vertex to the midpoint of the opposite side.",
            "2_concept": "Find midpoint $M$ of $BC$, then find the equation of the line through $A$ and $M$.",
            "3_breakdown": f"$M({M[0]}; {M[1]})$ and equation ${eq_str}$.",
        },
        misconception_tags=["confused_median_and_altitude"],
        keywords=["median", "midpoint", "triangle geometry", "equation of line"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=4,
        mode="24_triangle_median_equation",
        difficulty="hard",
        diagram_spec=d_spec,
    )


# ---------------------------------------------------------------------------
# 25. Triangle Altitude Equation (with inline_svg)
# ---------------------------------------------------------------------------
def build_25_triangle_altitude_equation(r: random.Random) -> Dict[str, Any]:
    sx = r.choice([-2, -1, 0, 1])
    sy = r.choice([-2, -1, 0, 1])
    A = (2 + sx, 6 + sy, "A")
    B = (0 + sx, 0 + sy, "B")
    C = (4 + sx, 2 + sy, "C")
    c_val = 10 + 2 * sx + sy

    d_spec = _cartesian_geometry_svg(
        points=[(float(A[0]), float(A[1]), "A"), (float(B[0]), float(B[1]), "B"), (float(C[0]), float(C[1]), "C")],
        segments=[(0, 1), (1, 2), (2, 0)],
    )

    c_str = f"+ {c_val}" if c_val >= 0 else f"- {abs(c_val)}"
    eq_str = rf"y = -2x {c_str}"
    prompt = (
        f"In $\\triangle ABC$ shown in the diagram, vertices are $A({A[0]}; {A[1]})$, $B({B[0]}; {B[1]})$, and $C({C[0]}; {C[1]})$.\n\n"
        f"Determine the equation of the altitude from vertex $A$ perpendicular to side $BC$."
    )
    ans_latex = eq_str
    sample = (
        rf"m_{{BC}} = \frac{{{C[1]} - ({B[1]})}}{{{C[0]} - ({B[0]})}} = \frac{{2}}{{4}} = \frac{{1}}{{2}}\\"
        rf"\text{{Since the altitude is perpendicular to }} BC: m_{{alt}} \times \frac{{1}}{{2}} = -1 \implies m_{{alt}} = -2\\"
        rf"\text{{Equation through }} A({A[0]}; {A[1]}):\\"
        rf"y - ({A[1]}) = -2(x - ({A[0]})) \implies {eq_str}"
    )

    return make_math_question(
        prefix="analgeo_25",
        topic=TOPIC,
        subskill="25_triangle_altitude_equation",
        learning_objective_id=f"{LO_PREFIX}_altitude_eq",
        prompt=prompt,
        prompt_latex=rf"A({A[0]}; {A[1]}), \; B({B[0]}; {B[1]}), \; C({C[0]}; {C[1]})",
        answer_latex=ans_latex,
        answer_sympy=ans_latex,
        sample_answer=sample,
        marking_schema={
            "total_marks": 4,
            "marking_points": [
                {"id": "mp1", "desc": "Calculated gradient m_BC = 1/2", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Found perpendicular gradient m = -2", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Substituted vertex A({A[0]}; {A[1]})", "marks": 1, "editable": True},
                {"id": "mp4", "desc": f"Final equation: {eq_str}", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        hints={
            "1_nudge": "An altitude passes through a vertex and is perpendicular to the opposite side.",
            "2_concept": "Calculate $m_{BC}$, find the negative reciprocal gradient, and use point $A$.",
            "3_breakdown": f"Equation is ${eq_str}$.",
        },
        misconception_tags=["confused_altitude_and_perpendicular_bisector"],
        keywords=["altitude", "perpendicular", "triangle geometry", "equation of line"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=4,
        mode="25_triangle_altitude_equation",
        difficulty="hard",
        diagram_spec=d_spec,
    )


# ---------------------------------------------------------------------------
# Registry Map of Archetypes 01–25
# ---------------------------------------------------------------------------
ARCHETYPES_01_25 = {
    "01_distance_between_two_points_direct": build_01_distance_between_two_points_direct,
    "02_distance_formula_missing_coordinate": build_02_distance_formula_missing_coordinate,
    "03_midpoint_of_line_segment": build_03_midpoint_of_line_segment,
    "04_endpoint_from_midpoint_and_one_endpoint": build_04_endpoint_from_midpoint_and_one_endpoint,
    "05_gradient_between_two_points": build_05_gradient_between_two_points,
    "06_gradient_of_horizontal_and_vertical_lines": build_06_gradient_of_horizontal_and_vertical_lines,
    "07_parallel_lines_equal_gradients": build_07_parallel_lines_equal_gradients,
    "08_perpendicular_lines_product_minus_one": build_08_perpendicular_lines_product_minus_one,
    "09_collinear_points_proof": build_09_collinear_points_proof,
    "10_collinear_points_find_unknown_coordinate": build_10_collinear_points_find_unknown_coordinate,
    "11_equation_straight_line_gradient_intercept": build_11_equation_straight_line_gradient_intercept,
    "12_equation_straight_line_point_gradient": build_12_equation_straight_line_point_gradient,
    "13_equation_straight_line_two_points": build_13_equation_straight_line_two_points,
    "14_equation_parallel_line_through_point": build_14_equation_parallel_line_through_point,
    "15_equation_perpendicular_line_through_point": build_15_equation_perpendicular_line_through_point,
    "16_angle_of_inclination_positive_gradient": build_16_angle_of_inclination_positive_gradient,
    "17_angle_of_inclination_negative_gradient": build_17_angle_of_inclination_negative_gradient,
    "18_angle_between_two_lines_exterior_angle": build_18_angle_between_two_lines_exterior_angle,
    "19_inclination_from_two_points": build_19_inclination_from_two_points,
    "20_gradient_from_inclination_angle": build_20_gradient_from_inclination_angle,
    "21_proving_right_angled_triangle_gradient": build_21_proving_right_angled_triangle_gradient,
    "22_proving_isosceles_triangle_distance": build_22_proving_isosceles_triangle_distance,
    "23_proving_equilateral_triangle_distance": build_23_proving_equilateral_triangle_distance,
    "24_triangle_median_equation": build_24_triangle_median_equation,
    "25_triangle_altitude_equation": build_25_triangle_altitude_equation,
}
