"""Grade 12 Mathematics - Differential Calculus Archetypes 26 to 50.
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/Mathematics_Gr12/Term 1/04. Differential calculus.md.
"""
from __future__ import annotations

import math
import random
from typing import Any, Callable, Dict, List, Optional
import sympy as sp

from .sequences_series_archetypes_01_25 import _svg_spec


def _mcq_q(
    rng: random.Random,
    qid: str,
    subskill: str,
    title: str,
    prompt: str,
    correct: str,
    distractors: List[str],
    worked_solution: str,
    hints: Dict[str, str],
    misconception_tags: List[str],
    marks: int = 3,
    curriculum_ref: str = "Term 1 > Differential Calculus",
    diagram_spec: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    opts = [correct] + distractors[:3]
    rng.shuffle(opts)
    q: Dict[str, Any] = {
        "id": qid,
        "title": title,
        "subskill": subskill,
        "question_family_id": subskill,
        "question_type": "multiple_choice",
        "prompt": prompt,
        "options": opts,
        "expected_answer": correct,
        "sample_answer": correct,
        "worked_solution": worked_solution,
        "marking_schema": {
            "total_marks": marks,
            "marking_points": [
                {"id": "mp_1", "desc": f"Correct selection: {correct}", "marks": marks, "editable": True}
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": hints,
        "misconception_tags": misconception_tags,
        "curriculum_reference": curriculum_ref,
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 4,
        "difficulty": "medium",
    }
    if diagram_spec:
        q["diagram_spec"] = diagram_spec
        q["modality"] = "diagram"
    return q


def _calc_q(
    rng: random.Random,
    qid: str,
    subskill: str,
    title: str,
    prompt: str,
    expected_value: str,
    worked_solution: str,
    hints: Dict[str, str],
    misconception_tags: List[str],
    marks: int = 4,
    curriculum_ref: str = "Term 1 > Differential Calculus",
    diagram_spec: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    q: Dict[str, Any] = {
        "id": qid,
        "title": title,
        "subskill": subskill,
        "question_family_id": subskill,
        "question_type": "math_short",
        "prompt": prompt,
        "expected_answer": expected_value,
        "sample_answer": expected_value,
        "worked_solution": worked_solution,
        "marking_schema": {
            "total_marks": marks,
            "marking_points": [
                {"id": f"mp_{i+1}", "desc": pt, "marks": 1, "editable": True}
                for i, pt in enumerate(worked_solution.strip().split("\n")[:marks])
            ] or [{"id": "mp_1", "desc": f"Accurate calculation: {expected_value}", "marks": marks, "editable": True}],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": hints,
        "misconception_tags": misconception_tags,
        "curriculum_reference": curriculum_ref,
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 5,
        "difficulty": "medium",
    }
    if diagram_spec:
        q["diagram_spec"] = diagram_spec
        q["modality"] = "diagram"
    return q


# ==============================================================================
# Archetypes 26 - 50
# ==============================================================================

def arch_26_tangent_perpendicular_to_given_line(rng: random.Random) -> Dict[str, Any]:
    # Curve: y = x^2 + 2x. Perpendicular to 2x + 6y = 5 (m_perp = -1/3 => m_tangent = 3)
    # Let m_tangent be an integer
    m_tangent = rng.choice([2, 4, 6])
    # Line perpendicular: gradient is -1 / m_tangent
    # f(x) = x^2 + b*x + c  =>  2x + b = m_tangent
    b = rng.choice([-4, -2, 0])
    x_contact = (m_tangent - b) // 2
    c_val = rng.choice([-3, 1, 5])
    y_contact = (x_contact ** 2) + b * x_contact + c_val
    prompt = (
        f"A curve is defined by $f(x) = x^2 {'+' if b >= 0 else '-'} {abs(b)}x {'+' if c_val >= 0 else '-'} {abs(c_val)}$.\n\n"
        f"Determine the coordinates of the point on the curve where the tangent line is perpendicular "
        f"to a straight line having gradient $m = -\\frac{{1}}{{{m_tangent}}}$."
    )
    correct = f"({x_contact}; {y_contact})"
    distractors = [
        f"({x_contact}; {-y_contact})",
        f"({-x_contact}; {y_contact})",
        f"({m_tangent}; {c_val})",
    ]
    sol = (
        f"Step 1: Perpendicular gradient relationship:\n"
        f"$$m_1 \\times m_2 = -1 \\implies m_{{\\text{{tangent}}}} = -\\frac{{1}}{{-1/{m_tangent}}} = {m_tangent}$$\n"
        f"Step 2: Equate $f'(x) = {m_tangent}$:\n"
        f"$$f'(x) = 2x {'+' if b >= 0 else '-'} {abs(b)}$$\n"
        f"$$2x {'+' if b >= 0 else '-'} {abs(b)} = {m_tangent} \\implies 2x = {m_tangent - b} \\implies x = {x_contact}$$\n"
        f"Step 3: Calculate $y$-coordinate on the curve:\n"
        f"$$y = ({x_contact})^2 {'+' if b >= 0 else '-'} {abs(b)}({x_contact}) {'+' if c_val >= 0 else '-'} {abs(c_val)} = {y_contact}$$\n"
        f"The point is $({x_contact};\\ {y_contact})$."
    )
    return _mcq_q(
        rng, f"g12_calc_26_{rng.randint(100000, 999999)}", "26_tangent_perpendicular_to_given_line",
        "Point of Tangency Perpendicular to Given Linear Slope", prompt, correct, distractors, sol,
        {"tier_1": f"Perpendicular gradients satisfy m1 * m2 = -1. Here m_tangent = {m_tangent}.",
         "tier_2": f"Solve f'(x) = {m_tangent} for x, then find y = f(x).",
         "tier_3": correct},
        ["used_negative_slope_instead_of_negative_reciprocal"]
    )


def arch_27_horizontal_tangent_points(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([1, 2, 3])
    p = rng.choice([-3, -2, 1, 4])
    # f(x) = a*(x - p)^2 + q = a*x^2 - 2ap*x + (a*p^2 + q)
    # f'(x) = 2a*(x - p) = 0 => x = p
    q_val = rng.choice([-8, -2, 5, 9])
    two_ap = 2 * a * p
    c_val = a * (p ** 2) + q_val
    prompt = (
        f"A horizontal tangent has a gradient of zero ($m = 0$).\n\n"
        f"Determine the coordinates of the point where the parabola "
        f"$f(x) = {a if a != 1 else ''}x^2 {'-' if two_ap >= 0 else '+'} {abs(two_ap)}x {'+' if c_val >= 0 else '-'} {abs(c_val)}$ "
        f"has a horizontal tangent line."
    )
    ans = f"({p}; {q_val})"
    sol = (
        f"Step 1: A horizontal tangent occurs where $f'(x) = 0$:\n"
        f"$$f'(x) = {2*a}x {'-' if two_ap >= 0 else '+'} {abs(two_ap)} = 0$$\n"
        f"$${2*a}x = {two_ap} \\implies x = {p}$$\n"
        f"Step 2: Find the corresponding $y$-value:\n"
        f"$$y = f({p}) = {a}({p})^2 {'-' if two_ap >= 0 else '+'} {abs(two_ap)}({p}) {'+' if c_val >= 0 else '-'} {abs(c_val)} = {q_val}$$\n"
        f"The horizontal tangent touches the parabola at the turning point $({p};\\ {q_val})$."
    )
    return _calc_q(
        rng, f"g12_calc_27_{rng.randint(100000, 999999)}", "27_horizontal_tangent_points",
        "Point of Contact of Horizontal Tangent Line", prompt, ans, sol,
        {"tier_1": "Set f'(x) = 0 because the gradient of any horizontal line is 0.",
         "tier_2": f"2*{a}x - ({two_ap}) = 0 gives x = {p}. Substitute into f(x) to get y = {q_val}.",
         "tier_3": f"Point is ({p}; {q_val})."},
        ["confused_horizontal_tangent_with_vertical_asymptote"]
    )


def arch_28_second_derivative_calculation(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([1, 2, 3])
    b = rng.choice([-6, -3, 3, 6])
    c = rng.choice([-8, 2, 7])
    d = rng.choice([-5, 4])
    # f(x) = a*x^3 + b*x^2 + c*x + d
    # f'(x) = 3a*x^2 + 2b*x + c
    # f''(x) = 6a*x + 2b
    six_a = 6 * a
    two_b = 2 * b
    correct = f"{six_a}x {'+' if two_b >= 0 else '-'} {abs(two_b)}"
    distractors = [
        f"{3*a}x^2 {'+' if two_b >= 0 else '-'} {abs(two_b)}x",
        f"{six_a}x",
        f"{six_a}x {'+' if b >= 0 else '-'} {abs(b)}",
    ]
    prompt = (
        f"Determine the second derivative $f''(x)$ if "
        f"$f(x) = {a if a != 1 else ''}x^3 {'+' if b >= 0 else '-'} {abs(b)}x^2 {'+' if c >= 0 else '-'} {abs(c)}x {'+' if d >= 0 else '-'} {abs(d)}$."
    )
    sol = (
        f"Step 1: Compute the first derivative $f'(x)$:\n"
        f"$$f'(x) = {3*a}x^2 {'+' if 2*b >= 0 else '-'} {abs(2*b)}x {'+' if c >= 0 else '-'} {abs(c)}$$\n"
        f"Step 2: Differentiate $f'(x)$ to find the second derivative $f''(x)$:\n"
        f"$$f''(x) = \\frac{{d}}{{dx}} \\left[ {3*a}x^2 {'+' if 2*b >= 0 else '-'} {abs(2*b)}x {'+' if c >= 0 else '-'} {abs(c)} \\right] = {correct}$$."
    )
    return _mcq_q(
        rng, f"g12_calc_28_{rng.randint(100000, 999999)}", "28_second_derivative_calculation",
        "Calculation of Second Derivative of Cubic Function", prompt, correct, distractors, sol,
        {"tier_1": "Differentiate once to find f'(x), then differentiate f'(x) to obtain f''(x).",
         "tier_2": f"f'(x) = {3*a}x^2 + {2*b}x + {c}. Differentiating again gives {six_a}x + ({two_b}).",
         "tier_3": correct},
        ["stopped_at_first_derivative"]
    )


def arch_29_second_derivative_at_point(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([1, 2])
    b = rng.choice([-3, 3])
    x0 = rng.choice([-2, 0, 2])
    # f(x) = a*x^3 + b*x^2 - 5x + 2  =>  f''(x) = 6a*x + 2b
    val = 6 * a * x0 + 2 * b
    concavity = "concave up" if val > 0 else ("concave down" if val < 0 else "point of inflection")
    prompt = (
        f"Given $f(x) = {a if a != 1 else ''}x^3 {'+' if b >= 0 else '-'} {abs(b)}x^2 - 5x + 2$:\n\n"
        f"1. Calculate the value of $f''({x0})$.\n"
        f"2. State whether the curve is concave up, concave down, or at an inflection point at $x = {x0}$."
    )
    correct = f"f''({x0}) = {val}; {concavity}"
    wrong_concavity = "concave down" if val > 0 else "concave up"
    distractors = [
        f"f''({x0}) = {val}; {wrong_concavity}",
        f"f''({x0}) = {-val}; {concavity}",
        f"f''({x0}) = {val}; linear",
    ]
    sol = (
        f"Step 1: First and second derivatives:\n"
        f"$$f'(x) = {3*a}x^2 {'+' if 2*b >= 0 else '-'} {abs(2*b)}x - 5$$\n"
        f"$$f''(x) = {6*a}x {'+' if 2*b >= 0 else '-'} {abs(2*b)}$$\n"
        f"Step 2: Evaluate at $x = {x0}$:\n"
        f"$$f''({x0}) = {6*a}({x0}) {'+' if 2*b >= 0 else '-'} {abs(2*b)} = {val}$$\n"
        f"Step 3: Concavity test:\n"
        f"Since $f''({x0}) {'> 0' if val > 0 else ('< 0' if val < 0 else '= 0')}$, the curve is {concavity}."
    )
    return _mcq_q(
        rng, f"g12_calc_29_{rng.randint(100000, 999999)}", "29_second_derivative_at_point",
        "Second Derivative Evaluation and Concavity Test", prompt, correct, distractors, sol,
        {"tier_1": "f''(x) > 0 indicates concave up; f''(x) < 0 indicates concave down.",
         "tier_2": f"Substitute x = {x0} into f''(x) = {6*a}x + ({2*b}).",
         "tier_3": correct},
        ["reversed_concavity_sign_rules"]
    )


def arch_30_cubic_stationary_turning_points(rng: random.Random) -> Dict[str, Any]:
    # f'(x) = 3(x - r1)(x - r2) = 3x^2 - 3(r1+r2)x + 3*r1*r2
    r1 = rng.choice([-3, -2, -1])
    r2 = rng.choice([1, 2, 3])
    # f(x) = x^3 - (3/2)(r1+r2)x^2 + 3*r1*r2*x + d
    # To have integer coefficients, let r1 + r2 be even
    while (r1 + r2) % 2 != 0:
        r2 += 1
    sum_r = r1 + r2
    prod_r = r1 * r2
    b_coeff = -3 * sum_r // 2
    c_coeff = 3 * prod_r
    d_coeff = rng.choice([-4, 2, 6])
    # Turning points coordinates
    y1 = (r1 ** 3) + b_coeff * (r1 ** 2) + c_coeff * r1 + d_coeff
    y2 = (r2 ** 3) + b_coeff * (r2 ** 2) + c_coeff * r2 + d_coeff
    prompt = (
        f"Given the cubic polynomial $f(x) = x^3 {'+' if b_coeff >= 0 else '-'} {abs(b_coeff)}x^2 {'+' if c_coeff >= 0 else '-'} {abs(c_coeff)}x {'+' if d_coeff >= 0 else '-'} {abs(d_coeff)}$:\n\n"
        f"Determine the coordinates of the two stationary points (turning points) of $f$."
    )
    correct = f"({r1}; {y1}) and ({r2}; {y2})"
    distractors = [
        f"({r1}; 0) and ({r2}; 0)",
        f"({-r1}; {y1}) and ({-r2}; {y2})",
        f"({r1}; {y2}) and ({r2}; {y1})",
    ]
    sol = (
        f"Step 1: Set $f'(x) = 0$ to find the $x$-values of stationary points:\n"
        f"$$f'(x) = 3x^2 {'+' if 2*b_coeff >= 0 else '-'} {abs(2*b_coeff)}x {'+' if c_coeff >= 0 else '-'} {abs(c_coeff)} = 0$$\n"
        f"$$3(x^2 - {sum_r}x + {prod_r}) = 0 \\implies 3(x - ({r1}))(x - ({r2})) = 0$$\n"
        f"Stationary points occur at $x = {r1}$ and $x = {r2}$.\n"
        f"Step 2: Calculate corresponding $y$-coordinates:\n"
        f"$$f({r1}) = ({r1})^3 + ({b_coeff})({r1})^2 + ({c_coeff})({r1}) + ({d_coeff}) = {y1}$$\n"
        f"$$f({r2}) = ({r2})^3 + ({b_coeff})({r2})^2 + ({c_coeff})({r2}) + ({d_coeff}) = {y2}$$\n"
        f"Stationary points are $({r1};\\ {y1})$ and $({r2};\\ {y2})$."
    )
    return _mcq_q(
        rng, f"g12_calc_30_{rng.randint(100000, 999999)}", "30_cubic_stationary_turning_points",
        "Coordinates of Cubic Stationary Points", prompt, correct, distractors, sol,
        {"tier_1": "Stationary points occur where f'(x) = 0. Solve the quadratic equation for x.",
         "tier_2": "Substitute each x-value back into the original cubic f(x) to find the y-coordinates.",
         "tier_3": correct},
        ["forgot_to_calculate_y_coordinates_for_turning_points"]
    )


def arch_31_cubic_point_of_inflection_formula(rng: random.Random) -> Dict[str, Any]:
    # f(x) = x^3 - 3*p*x^2 + ... => f''(x) = 6x - 6p = 0 => x = p
    p = rng.choice([-3, -2, 1, 2, 4])
    b = -3 * p
    c = rng.choice([-5, 2, 7])
    d = rng.choice([-6, 1, 8])
    # f(x) = x^3 + b*x^2 + c*x + d
    y_infl = (p ** 3) + b * (p ** 2) + c * p + d
    prompt = (
        f"Determine the coordinates of the point of inflection of the cubic function "
        f"$f(x) = x^3 {'+' if b >= 0 else '-'} {abs(b)}x^2 {'+' if c >= 0 else '-'} {abs(c)}x {'+' if d >= 0 else '-'} {abs(d)}$."
    )
    ans = f"({p}; {y_infl})"
    sol = (
        f"Step 1: Find the second derivative $f''(x)$:\n"
        f"$$f'(x) = 3x^2 {'+' if 2*b >= 0 else '-'} {abs(2*b)}x {'+' if c >= 0 else '-'} {abs(c)}$$\n"
        f"$$f''(x) = 6x {'+' if 2*b >= 0 else '-'} {abs(2*b)}$$\n"
        f"Step 2: Solve $f''(x) = 0$ for the point of inflection (or use $x = -\\frac{{b}}{{3a}}$):\n"
        f"$$6x {'+' if 2*b >= 0 else '-'} {abs(2*b)} = 0 \\implies 6x = {-2*b} \\implies x = {p}$$\n"
        f"Step 3: Substitute $x = {p}$ into $f(x)$:\n"
        f"$$y = f({p}) = ({p})^3 + ({b})({p})^2 + ({c})({p}) + ({d}) = {y_infl}$$\n"
        f"The point of inflection is $({p};\\ {y_infl})$."
    )
    return _calc_q(
        rng, f"g12_calc_31_{rng.randint(100000, 999999)}", "31_cubic_point_of_inflection_formula",
        "Coordinates of Point of Inflection of Cubic Function", prompt, ans, sol,
        {"tier_1": "The point of inflection occurs where f''(x) = 0 (or x = -b / (3a)).",
         "tier_2": f"x = -({b}) / (3*1) = {p}. Then evaluate f({p}) to find y.",
         "tier_3": f"Inflection point is ({p}; {y_infl})."},
        ["confused_first_and_second_derivative_roots"]
    )


def arch_32_cubic_nature_of_turning_points_second_derivative_test(rng: random.Random) -> Dict[str, Any]:
    # f(x) = x^3 - 3x  =>  f'(x) = 3(x^2 - 1) = 0 => x = -1, x = 1
    # f''(x) = 6x. At x = -1: f'' = -6 < 0 (local max). At x = 1: f'' = 6 > 0 (local min).
    p = rng.choice([1, 2, 3])
    # f'(x) = 3(x^2 - p^2) = 3x^2 - 3p^2  =>  f(x) = x^3 - 3*p^2*x + 4
    c_val = -3 * (p ** 2)
    prompt = (
        f"A cubic function is given by $f(x) = x^3 {'+' if c_val >= 0 else '-'} {abs(c_val)}x + 4$.\n\n"
        f"Apply the second derivative test to classify the stationary points at $x = -{p}$ and $x = {p}$ "
        f"as either a local maximum or a local minimum."
    )
    correct = f"x = -{p} is a local maximum; x = {p} is a local minimum"
    distractors = [
        f"x = -{p} is a local minimum; x = {p} is a local maximum",
        f"Both x = -{p} and x = {p} are local maxima",
        f"Both x = -{p} and x = {p} are points of inflection",
    ]
    sol = (
        f"Step 1: Compute $f''(x)$:\n"
        f"$$f'(x) = 3x^2 {'+' if c_val >= 0 else '-'} {abs(c_val)}$$\n"
        f"$$f''(x) = 6x$$\n"
        f"Step 2: Test at $x = -{p}$:\n"
        f"$$f''(-{p}) = 6(-{p}) = -{6*p} < 0 \\implies \\text{{Local Maximum}}$$\n"
        f"Step 3: Test at $x = {p}$:\n"
        f"$$f''({p}) = 6({p}) = {6*p} > 0 \\implies \\text{{Local Minimum}}$$\n"
        f"Conclusion: $x = -{p}$ is a local maximum, and $x = {p}$ is a local minimum."
    )
    return _mcq_q(
        rng, f"g12_calc_32_{rng.randint(100000, 999999)}", "32_cubic_nature_of_turning_points_second_derivative_test",
        "Classifying Turning Points Using Second Derivative Test", prompt, correct, distractors, sol,
        {"tier_1": "Second derivative test: f''(x) < 0 indicates a local maximum; f''(x) > 0 indicates a local minimum.",
         "tier_2": f"Evaluate f''(x) = 6x at x = -{p} and x = {p}.",
         "tier_3": correct},
        ["inverted_second_derivative_test_max_min_classification"]
    )


def arch_33_cubic_intervals_increasing_and_decreasing(rng: random.Random) -> Dict[str, Any]:
    # f'(x) = 3(x - r1)(x - r2) with r1 < r2.
    # For a > 0, f is increasing on x < r1 or x > r2, and decreasing on r1 < x < r2.
    r1 = rng.choice([-3, -2, -1])
    r2 = rng.choice([1, 2, 3])
    sum_r = r1 + r2
    prod_r = r1 * r2
    prompt = (
        f"The derivative of a cubic function is $f'(x) = 3(x {'-' if r1 >= 0 else '+'} {abs(r1)})(x {'-' if r2 >= 0 else '+'} {abs(r2)})$.\n\n"
        f"State the values of $x$ for which the function $f$ is strictly decreasing."
    )
    correct = f"{r1} < x < {r2}"
    distractors = [
        f"x < {r1} or x > {r2}",
        f"x > {r2}",
        f"x < {r1}",
    ]
    sol = (
        f"Step 1: A function is strictly decreasing where its derivative is negative ($f'(x) < 0$):\n"
        f"$$3(x - ({r1}))(x - ({r2})) < 0$$\n"
        f"Step 2: Since the parabola $y = 3(x - {r1})(x - {r2})$ opens upwards ($a > 0$), it is below the horizontal axis between the roots:\n"
        f"$${r1} < x < {r2}$$\n"
        f"Thus $f$ is strictly decreasing for ${correct}$."
    )
    return _mcq_q(
        rng, f"g12_calc_33_{rng.randint(100000, 999999)}", "33_cubic_intervals_increasing_and_decreasing",
        "Intervals Where Cubic Function is Decreasing", prompt, correct, distractors, sol,
        {"tier_1": "A function decreases where f'(x) < 0.",
         "tier_2": f"The roots of f'(x) are {r1} and {r2}. An upward-opening parabola is negative between its roots.",
         "tier_3": correct},
        ["confused_increasing_and_decreasing_derivative_regions"]
    )


def arch_34_cubic_concavity_intervals(rng: random.Random) -> Dict[str, Any]:
    p = rng.choice([-2, -1, 1, 3])
    # f''(x) = 6(x - p)  =>  concave up for x > p, concave down for x < p
    b_coeff = -3 * p
    prompt = (
        f"Given the cubic curve $f(x) = x^3 {'+' if b_coeff >= 0 else '-'} {abs(b_coeff)}x^2 + 4x - 6$:\n\n"
        f"Determine the values of $x$ for which the curve of $f$ is concave upwards."
    )
    correct = f"x > {p}"
    distractors = [
        f"x < {p}",
        f"x > {-p}",
        f"x = {p}",
    ]
    sol = (
        f"Step 1: Compute second derivative $f''(x)$:\n"
        f"$$f'(x) = 3x^2 {'+' if 2*b_coeff >= 0 else '-'} {abs(2*b_coeff)}x + 4$$\n"
        f"$$f''(x) = 6x {'+' if 2*b_coeff >= 0 else '-'} {abs(2*b_coeff)} = 6(x - {p})$$\n"
        f"Step 2: Concave upwards requires $f''(x) > 0$:\n"
        f"$$6(x - {p}) > 0 \\implies x > {p}$$."
    )
    return _mcq_q(
        rng, f"g12_calc_34_{rng.randint(100000, 999999)}", "34_cubic_concavity_intervals",
        "Determining Concavity Intervals for Cubic Function", prompt, correct, distractors, sol,
        {"tier_1": "Concave up occurs when f''(x) > 0.",
         "tier_2": f"f''(x) = 6x - ({6*p}) > 0. Solve for x.",
         "tier_3": correct},
        ["reversed_concave_up_inequality"]
    )


def arch_35_cubic_intercepts_axes_full(rng: random.Random) -> Dict[str, Any]:
    # P(x) = (x - r1)(x - r2)(x - r3)
    r1 = rng.choice([-3, -2, -1])
    r2 = 1
    r3 = rng.choice([2, 4])
    y_int = -r1 * -r2 * -r3  # = -(r1 * r2 * r3)
    # P(x) = x^3 - (r1+r2+r3)x^2 + (r1r2+r1r3+r2r3)x - r1r2r3
    prompt = (
        f"Given the factorised cubic equation $f(x) = (x {'+' if r1 < 0 else '-'} {abs(r1)})(x - 1)(x - {r3})$:\n\n"
        f"1. Write down the $y$-intercept of $f$.\n"
        f"2. Write down all $x$-intercepts of $f$."
    )
    correct = f"y-intercept: (0; {-r1*r2*r3}); x-intercepts: ({r1}; 0), (1; 0), ({r3}; 0)"
    distractors = [
        f"y-intercept: (0; {r1*r2*r3}); x-intercepts: ({-r1}; 0), (-1; 0), ({-r3}; 0)",
        f"y-intercept: ({-r1*r2*r3}; 0); x-intercepts: (0; {r1}), (0; 1), (0; {r3})",
        f"y-intercept: (0; {-r1*r2*r3}); x-intercepts: ({r1}; 0), ({r3}; 0)",
    ]
    sol = (
        f"Step 1: $y$-intercept occurs at $x = 0$:\n"
        f"$$f(0) = (0 {'+' if r1 < 0 else '-'} {abs(r1)})(0 - 1)(0 - {r3}) = ({r1})(-1)(-{r3}) = {-r1*r2*r3} \\implies (0;\\ {-r1*r2*r3})$$\n"
        f"Step 2: $x$-intercepts occur where $f(x) = 0$:\n"
        f"$$(x - ({r1}))(x - 1)(x - {r3}) = 0 \\implies x = {r1}, \\; x = 1, \\; x = {r3}$$\n"
        f"Intercepts: $({r1};\\ 0), (1;\\ 0), ({r3};\\ 0)$."
    )
    return _mcq_q(
        rng, f"g12_calc_35_{rng.randint(100000, 999999)}", "35_cubic_intercepts_axes_full",
        "Axes Intercepts of Fully Factorised Cubic Curve", prompt, correct, distractors, sol,
        {"tier_1": "Set x = 0 for the y-intercept, and each factor to 0 for x-intercepts.",
         "tier_2": f"x-intercepts are ({r1}, 0), (1, 0), ({r3}, 0). y-intercept is f(0).",
         "tier_3": correct},
        ["inverted_signs_of_intercept_coordinates"]
    )


def arch_36_cubic_sketching_features_identification(rng: random.Random) -> Dict[str, Any]:
    a_sign = rng.choice(["positive", "negative"])
    shape = "starts down, local max, local min, goes up" if a_sign == "positive" else "starts up, local min, local max, goes down"
    prompt = (
        f"Consider the cubic polynomial $f(x) = ax^3 + bx^2 + cx + d$ where $a {'> 0' if a_sign == 'positive' else '< 0'}$, "
        f"having two distinct stationary points.\n\n"
        f"Describe the general shape and end behaviour of this curve from left to right."
    )
    correct = f"For a {'> 0' if a_sign == 'positive' else '< 0'}, the curve {shape}"
    distractors = [
        f"For a {'> 0' if a_sign == 'positive' else '< 0'}, the curve {'starts up, local min, local max, goes down' if a_sign == 'positive' else 'starts down, local max, local min, goes up'}",
        "The curve is symmetrical like a parabola with a single vertex",
        "The curve is a straight line",
    ]
    sol = (
        f"Step 1: Check leading coefficient $a$:\n"
        f"If $a > 0$, as $x \\to -\\infty, f(x) \\to -\\infty$ and as $x \\to +\\infty, f(x) \\to +\\infty$.\n"
        f"If $a < 0$, as $x \\to -\\infty, f(x) \\to +\\infty$ and as $x \\to +\\infty, f(x) \\to -\\infty$.\n"
        f"Step 2: Turning point order:\n"
        f"For $a {'> 0' if a_sign == 'positive' else '< 0'}, the curve {shape}."
    )
    return _mcq_q(
        rng, f"g12_calc_36_{rng.randint(100000, 999999)}", "36_cubic_sketching_features_identification",
        "End Behaviour and General Shape of Cubic Curves", prompt, correct, distractors, sol,
        {"tier_1": "Look at the sign of the leading coefficient a to determine end behaviour.",
         "tier_2": f"When a {'> 0' if a_sign == 'positive' else '< 0'}, the curve {shape}.",
         "tier_3": correct},
        ["confused_cubic_end_behaviour_with_parabola"]
    )


def arch_37_cubic_equation_from_turning_point_and_intercept(rng: random.Random) -> Dict[str, Any]:
    # Tangent to x-axis at (x1, 0) => repeated factor (x - x1)^2. Crosses at (x2, 0).
    # y = a(x - x1)^2 (x - x2). If a = 1, y = (x - x1)^2 (x - x2).
    x1 = rng.choice([-2, 1, 3])
    x2 = rng.choice([-4, -1, 4])
    while x2 == x1:
        x2 = rng.choice([2, 5])
    # y-intercept = 1 * (-x1)^2 * (-x2) = -x2 * x1^2
    y_int = -x2 * (x1 ** 2)
    prompt = (
        f"A cubic function has a turning point on the $x$-axis at $({x1};\\ 0)$ and crosses the $x$-axis at $({x2};\\ 0)$. "
        f"The $y$-intercept is $(0;\\ {y_int})$.\n\n"
        f"Determine the equation of the cubic function in the form $y = a(x - p)^2(x - q)$."
    )
    correct = f"y = (x {'-' if x1 >= 0 else '+'} {abs(x1)})^2 (x {'-' if x2 >= 0 else '+'} {abs(x2)})"
    distractors = [
        f"y = (x {'-' if x1 >= 0 else '+'} {abs(x1)})(x {'-' if x2 >= 0 else '+'} {abs(x2)})^2",
        f"y = 2(x {'-' if x1 >= 0 else '+'} {abs(x1)})^2 (x {'-' if x2 >= 0 else '+'} {abs(x2)})",
        f"y = -(x {'-' if x1 >= 0 else '+'} {abs(x1)})^2 (x {'-' if x2 >= 0 else '+'} {abs(x2)})",
    ]
    sol = (
        f"Step 1: Since $({x1};\\ 0)$ is a turning point tangent to the $x$-axis, $(x - {x1})$ is a repeated factor:\n"
        f"$$y = a(x - {x1})^2(x - {x2})$$\n"
        f"Step 2: Substitute the $y$-intercept $(0;\\ {y_int})$ to solve for $a$:\n"
        f"$${y_int} = a(0 - {x1})^2(0 - {x2}) = a({x1**2})({-x2})$$\n"
        f"$${y_int} = a({y_int}) \\implies a = 1$$\n"
        f"Equation: ${correct}$."
    )
    return _mcq_q(
        rng, f"g12_calc_37_{rng.randint(100000, 999999)}", "37_cubic_equation_from_turning_point_and_intercept",
        "Determining Cubic Equation from Tangent Intercept and Crossing", prompt, correct, distractors, sol,
        {"tier_1": "A turning point on the x-axis corresponds to a squared linear factor (multiplicity 2).",
         "tier_2": f"Write y = a(x - {x1})^2(x - {x2}) and use (0, {y_int}) to find a = 1.",
         "tier_3": correct},
        ["squared_the_crossing_intercept_instead_of_turning_point"]
    )


def arch_38_cubic_equation_from_three_intercepts_and_point(rng: random.Random) -> Dict[str, Any]:
    r1, r2, r3 = -1, 2, 4
    # y = a(x + 1)(x - 2)(x - 4). Let a = 2 => y-intercept = 2*(1)(-2)(-4) = 16
    a_mult = rng.choice([2, 3])
    y_int = a_mult * (-r1) * (-r2) * (-r3)
    prompt = (
        f"The $x$-intercepts of a cubic curve are $(-1;\\ 0)$, $(2;\\ 0)$, and $(4;\\ 0)$. "
        f"The curve passes through the point $(0;\\ {y_int})$.\n\n"
        f"Calculate the value of the leading coefficient $a$ in $y = a(x + 1)(x - 2)(x - 4)$."
    )
    ans = f"a = {a_mult}"
    sol = (
        f"Step 1: Substitute the coordinates $x = 0$ and $y = {y_int}$ into the intercept form:\n"
        f"$${y_int} = a(0 + 1)(0 - 2)(0 - 4)$$\n"
        f"Step 2: Simplify the product:\n"
        f"$${y_int} = a(1)(-2)(-4) = 8a$$\n"
        f"Step 3: Solve for $a$:\n"
        f"$$a = \\frac{{{y_int}}}{{8}} = {a_mult}$$."
    )
    return _calc_q(
        rng, f"g12_calc_38_{rng.randint(100000, 999999)}", "38_cubic_equation_from_three_intercepts_and_point",
        "Determining Leading Coefficient of Cubic from Intercepts", prompt, ans, sol,
        {"tier_1": f"Substitute (0; {y_int}) into y = a(x+1)(x-2)(x-4).",
         "tier_2": f"{y_int} = 8a, solve for a.",
         "tier_3": f"a = {a_mult}."},
        ["arithmetic_error_solving_for_a"]
    )


def arch_39_cubic_gradient_at_inflection_point(rng: random.Random) -> Dict[str, Any]:
    # f(x) = x^3 - 3x^2 + 5x + 1  =>  f'(x) = 3x^2 - 6x + 5
    # f''(x) = 6x - 6 = 0 => x = 1.
    # Gradient at inflection = f'(1) = 3(1) - 6(1) + 5 = 2 (minimum gradient)
    c_val = rng.choice([4, 6, 8])
    # f'(x) = 3x^2 - 6x + c_val  =>  at x = 1, m = 3 - 6 + c_val = c_val - 3
    min_grad = c_val - 3
    prompt = (
        f"Given the cubic function $f(x) = x^3 - 3x^2 {'+' if c_val >= 0 else '-'} {abs(c_val)}x + 2$:\n\n"
        f"1. Determine the $x$-coordinate of the point of inflection.\n"
        f"2. Calculate the minimum gradient of the tangent to this curve."
    )
    ans = str(min_grad)
    sol = (
        f"Step 1: Point of inflection occurs where $f''(x) = 0$:\n"
        f"$$f'(x) = 3x^2 - 6x + {c_val}$$\n"
        f"$$f''(x) = 6x - 6 = 0 \\implies x = 1$$\n"
        f"Step 2: Since the parabola $f'(x)$ opens upwards ($a = 3 > 0$), its minimum value occurs at its vertex $x = 1$:\n"
        f"$$m_{{\\text{{min}}}} = f'(1) = 3(1)^2 - 6(1) + {c_val} = 3 - 6 + {c_val} = {min_grad}$$."
    )
    return _calc_q(
        rng, f"g12_calc_39_{rng.randint(100000, 999999)}", "39_cubic_gradient_at_inflection_point",
        "Minimum Gradient of Cubic Function at Inflection Point", prompt, ans, sol,
        {"tier_1": "The minimum or maximum gradient occurs at the point of inflection where f''(x) = 0.",
         "tier_2": f"Solve 6x - 6 = 0 => x = 1, then substitute x = 1 into f'(x).",
         "tier_3": f"Minimum gradient is {min_grad}."},
        ["substituted_x_into_f_instead_of_f_prime"]
    )


def arch_40_cubic_graph_interpretation_f_prime_positive(rng: random.Random) -> Dict[str, Any]:
    # Turning points at x = -2 and x = 3. a > 0.
    # f'(x) > 0 for x < -2 or x > 3.
    r1 = rng.choice([-4, -3, -2])
    r2 = rng.choice([1, 2, 4])
    prompt = (
        f"A cubic function $f(x)$ with positive leading coefficient ($a > 0$) has stationary points at $x = {r1}$ and $x = {r2}$.\n\n"
        f"For which values of $x$ is $f'(x) > 0$?"
    )
    correct = f"x < {r1} or x > {r2}"
    distractors = [
        f"{r1} < x < {r2}",
        f"x > {r2}",
        f"x < {r1}",
    ]
    sol = (
        f"Step 1: $f'(x)$ is a quadratic function opening upwards since $a > 0$.\n"
        f"Step 2: The roots of $f'(x) = 0$ are the $x$-values of the stationary points, $x = {r1}$ and $x = {r2}$.\n"
        f"Step 3: An upward parabola is positive outside its roots:\n"
        f"$$f'(x) > 0 \\iff x < {r1} \\text{{ or }} x > {r2}$$."
    )
    return _mcq_q(
        rng, f"g12_calc_40_{rng.randint(100000, 999999)}", "40_cubic_graph_interpretation_f_prime_positive",
        "Deducing Gradient Sign from Stationary Points", prompt, correct, distractors, sol,
        {"tier_1": "Stationary points are where f'(x) = 0. For a > 0, the derivative is positive outside the roots.",
         "tier_2": f"x < {r1} or x > {r2}.",
         "tier_3": correct},
        ["chose_interval_between_roots_instead_of_outside"]
    )


def arch_41_cubic_graph_interpretation_f_times_f_prime(rng: random.Random) -> Dict[str, Any]:
    cond_positive = rng.choice([True, False])
    if cond_positive:
        cond_str = "f(x) \\cdot f'(x) > 0"
        correct = "The curve lies above the x-axis and is increasing, OR lies below the x-axis and is decreasing"
        distractors = [
            "The curve lies above the x-axis and is decreasing, OR lies below the x-axis and is increasing",
            "The curve is always concave upwards",
            "The curve has a local maximum at that point",
        ]
        sol_cases = (
            f"Case 1: $f(x) > 0$ and $f'(x) > 0$ (the curve is above the $x$-axis and increasing).\n"
            f"Case 2: $f(x) < 0$ and $f'(x) < 0$ (the curve is below the $x$-axis and decreasing)."
        )
    else:
        cond_str = "f(x) \\cdot f'(x) < 0"
        correct = "The curve lies above the x-axis and is decreasing, OR lies below the x-axis and is increasing"
        distractors = [
            "The curve lies above the x-axis and is increasing, OR lies below the x-axis and is decreasing",
            "The curve is always concave downwards",
            "The curve has a local minimum at that point",
        ]
        sol_cases = (
            f"Case 1: $f(x) > 0$ and $f'(x) < 0$ (the curve is above the $x$-axis and decreasing).\n"
            f"Case 2: $f(x) < 0$ and $f'(x) > 0$ (the curve is below the $x$-axis and increasing)."
        )

    prompt = (
        f"Consider a function $f(x)$. Explain the graphical meaning of the condition:\n\n"
        f"$${cond_str}$$"
    )
    sol = (
        f"Step 1: For the product of two quantities to satisfy ${cond_str}$:\n"
        f"{sol_cases}\n"
        f"Conclusion: {correct}."
    )
    return _mcq_q(
        rng, f"g12_calc_41_{rng.randint(100000, 999999)}", "41_cubic_graph_interpretation_f_times_f_prime",
        "Graphical Meaning of Sign Product f(x) * f'(x)", prompt, correct, distractors, sol,
        {"tier_1": f"For ${cond_str}$, check when f(x) and f'(x) have {'the same' if cond_positive else 'opposite'} signs.",
         "tier_2": "f(x) sign indicates position relative to x-axis; f'(x) sign indicates increase or decrease.",
         "tier_3": correct},
        ["confused_product_of_signs_with_sum"]
    )


def arch_42_parabola_derivative_graph_connection(rng: random.Random) -> Dict[str, Any]:
    x1 = rng.choice([-3, -2, -1])
    x2 = rng.choice([2, 3, 5])
    prompt = (
        f"The derivative of a function $f$ is given by the parabola $f'(x) = (x {'+' if x1 < 0 else '-'} {abs(x1)})(x - {x2})$.\n\n"
        f"State the $x$-coordinates of the turning points of the original function $f$."
    )
    ans = f"x = {x1} and x = {x2}"
    sol = (
        f"Step 1: The turning points of $f(x)$ occur where $f'(x) = 0$.\n"
        f"Step 2: The roots of the derivative parabola $f'(x) = 0$ are:\n"
        f"$$x = {x1} \\quad \\text{{and}} \\quad x = {x2}$$\n"
        f"Thus the turning points of $f$ occur at $x = {x1}$ and $x = {x2}$."
    )
    return _calc_q(
        rng, f"g12_calc_42_{rng.randint(100000, 999999)}", "42_parabola_derivative_graph_connection",
        "Connecting Derivative x-Intercepts to Turning Points of Original Function", prompt, ans, sol,
        {"tier_1": "The x-intercepts of the derivative graph f'(x) represent the turning points of f(x).",
         "tier_2": f"Set f'(x) = 0 to get x = {x1} and x = {x2}.",
         "tier_3": f"x = {x1} and x = {x2}."},
        ["confused_turning_point_of_derivative_with_turning_point_of_f"]
    )


def arch_43_number_of_real_roots_from_turning_points_k(rng: random.Random) -> Dict[str, Any]:
    # Local min at (r2, y_min), local max at (r1, y_max)
    y_min = rng.choice([-10, -6, -4])
    y_max = rng.choice([4, 8, 12])
    prompt = (
        f"A cubic function $f(x)$ has a local maximum at $(-1;\\ {y_max})$ and a local minimum at $(3;\\ {y_min})$.\n\n"
        f"For which values of $k$ will the equation $f(x) = k$ have **three distinct real roots**?"
    )
    correct = f"{y_min} < k < {y_max}"
    distractors = [
        f"k < {y_min} or k > {y_max}",
        f"k = {y_min} or k = {y_max}",
        f"k > {y_max}",
    ]
    sol = (
        f"Step 1: Consider the horizontal line $y = k$ intersecting the cubic curve $y = f(x)$.\n"
        f"Step 2: A cubic curve has three distinct real roots if and only if the line $y = k$ cuts through the curve strictly between its local minimum and local maximum values:\n"
        f"$$y_{{\\text{{min}}}} < k < y_{{\\text{{max}}}}$$\n"
        f"Step 3: Substitute the local extrema values:\n"
        f"$${y_min} < k < {y_max}$$."
    )
    return _mcq_q(
        rng, f"g12_calc_43_{rng.randint(100000, 999999)}", "43_number_of_real_roots_from_turning_points_k",
        "Number of Real Roots of Cubic Dependent on Parameter k", prompt, correct, distractors, sol,
        {"tier_1": "Three distinct real roots occur when the horizontal line y = k lies strictly between the local min and local max.",
         "tier_2": f"Local min is {y_min} and local max is {y_max}.",
         "tier_3": correct},
        ["included_equality_at_turning_points"]
    )


def arch_44_rate_of_change_kinematics_velocity_acceleration(rng: random.Random) -> Dict[str, Any]:
    # s(t) = -t^2 + v0*t  =>  v(t) = s'(t) = -2t + v0  =>  a(t) = -2
    v0 = rng.choice([16, 20, 24, 30])
    t_val = rng.choice([2, 3, 4])
    v_ans = -2 * t_val + v0
    prompt = (
        f"The displacement $s$ (in metres) of a particle after $t$ seconds is given by $s(t) = -t^2 + {v0}t$.\n\n"
        f"1. Determine the velocity function $v(t) = s'(t)$.\n"
        f"2. Calculate the velocity of the particle at $t = {t_val}$ seconds."
    )
    ans = f"{v_ans} m/s"
    sol = (
        f"Step 1: Velocity is the first derivative of displacement:\n"
        f"$$v(t) = s'(t) = -2t + {v0}$$\n"
        f"Step 2: Evaluate at $t = {t_val}$:\n"
        f"$$v({t_val}) = -2({t_val}) + {v0} = {-2*t_val} + {v0} = {v_ans}\\text{{ m/s}}$$."
    )
    return _calc_q(
        rng, f"g12_calc_44_{rng.randint(100000, 999999)}", "44_rate_of_change_kinematics_velocity_acceleration",
        "Instantaneous Velocity from Displacement Function", prompt, ans, sol,
        {"tier_1": "Velocity is the derivative of displacement: v(t) = s'(t).",
         "tier_2": f"v(t) = -2t + {v0}. Substitute t = {t_val}.",
         "tier_3": f"{v_ans} m/s."},
        ["forgot_to_differentiate_displacement"]
    )


def arch_45_rate_of_change_maximum_height_projectile(rng: random.Random) -> Dict[str, Any]:
    # h(t) = -5t^2 + 40t => h'(t) = -10t + 40 = 0 => t = 4s. h_max = -5(16) + 160 = 80m
    v0 = rng.choice([20, 30, 40, 50])
    t_max = v0 // 10
    h_max = -5 * (t_max ** 2) + v0 * t_max
    prompt = (
        f"A ball is thrown vertically upwards such that its height $h$ (in metres) above the ground after $t$ seconds is given by "
        f"$h(t) = -5t^2 + {v0}t$.\n\n"
        f"Calculate the maximum height reached by the ball."
    )
    ans = f"{h_max} m"
    sol = (
        f"Step 1: At maximum height, the instantaneous velocity is zero ($h'(t) = 0$):\n"
        f"$$h'(t) = -10t + {v0} = 0 \\implies 10t = {v0} \\implies t = {t_max}\\text{{ seconds}}$$\n"
        f"Step 2: Substitute $t = {t_max}$ into the height function:\n"
        f"$$h({t_max}) = -5({t_max})^2 + {v0}({t_max}) = -5({t_max**2}) + {v0 * t_max} = {h_max}\\text{{ metres}}$$."
    )
    return _calc_q(
        rng, f"g12_calc_45_{rng.randint(100000, 999999)}", "45_rate_of_change_maximum_height_projectile",
        "Maximum Height of Projectile via Optimisation", prompt, ans, sol,
        {"tier_1": "Maximum height occurs when velocity h'(t) = 0.",
         "tier_2": f"-10t + {v0} = 0 gives t = {t_max} s. Then calculate h({t_max}).",
         "tier_3": f"{h_max} m."},
        ["stopped_at_time_t_without_calculating_maximum_height"]
    )


def arch_46_applied_optimisation_max_area_rectangle(rng: random.Random) -> Dict[str, Any]:
    # A farmer uses L metres of fence to enclose 3 sides of a rectangular pen against a river.
    # 2x + y = L => y = L - 2x. Area A(x) = x(L - 2x) = Lx - 2x^2.
    # A'(x) = L - 4x = 0 => x = L / 4. Max area = (L/4) * (L/2) = L^2 / 8.
    L = rng.choice([40, 60, 80, 100, 120, 140, 160, 200])
    x_opt = L // 4
    y_opt = L - 2 * x_opt  # = L // 2
    area_max = x_opt * y_opt
    w_px = 180 + (L % 70)
    h_px = 90 + (x_opt % 35)
    svg = (
        f'<svg viewBox="0 0 420 220" xmlns="http://www.w3.org/2000/svg">'
        f'<rect x="0" y="0" width="420" height="220" fill="#f8fafc" rx="8"/>'
        f'<rect x="40" y="25" width="340" height="28" fill="#bae6fd" stroke="#0284c7" stroke-width="1.5" rx="4"/>'
        f'<text x="210" y="44" font-size="12" font-family="sans-serif" font-weight="bold" fill="#0369a1" text-anchor="middle">Riverbank (no fencing needed)</text>'
        f'<polyline points="110,53 110,{53+h_px} {110+w_px},{53+h_px} {110+w_px},53" fill="#dcfce7" fill-opacity="0.5" stroke="#15803d" stroke-width="3"/>'
        f'<text x="92" y="{53 + h_px//2}" font-size="13" font-family="sans-serif" font-weight="bold" fill="#166534" text-anchor="end">x m</text>'
        f'<text x="{118+w_px}" y="{53 + h_px//2}" font-size="13" font-family="sans-serif" font-weight="bold" fill="#166534">x m</text>'
        f'<text x="{110 + w_px//2}" y="{75+h_px}" font-size="13" font-family="sans-serif" font-weight="bold" fill="#166534" text-anchor="middle">y = ({L} - 2x) m</text>'
        f'<text x="{110 + w_px//2}" y="{53 + h_px//2 + 5}" font-size="12" font-family="sans-serif" fill="#14532d" text-anchor="middle">Total wire = {L} m</text>'
        f'</svg>'
    )
    prompt = (
        f"Refer to the diagram of a rectangular vegetable patch bordering a straight riverbank, where no fencing is needed on the river side. "
        f"A farmer has ${L}\\text{{ metres}}$ of wire fencing to construct the remaining three sides.\n\n"
        f"If the two widths each have length $x$ metres and the third side has length $y = {L} - 2x$ metres, "
        f"calculate the dimensions $x$ and $y$ that will maximise the enclosed area."
    )
    correct = f"x = {x_opt} m, y = {y_opt} m (maximum area = {area_max} m^2)"
    distractors = [
        f"x = {L // 3} m, y = {L // 3} m",
        f"x = {L // 2} m, y = {L // 4} m",
        f"x = {x_opt} m, y = {x_opt} m",
    ]
    sol = (
        f"Step 1: Constraint equation:\n"
        f"$$2x + y = {L} \\implies y = {L} - 2x$$\n"
        f"Step 2: Area function to maximise:\n"
        f"$$A(x) = x \\cdot y = x({L} - 2x) = {L}x - 2x^2$$\n"
        f"Step 3: Differentiate and set $A'(x) = 0$:\n"
        f"$$A'(x) = {L} - 4x = 0 \\implies 4x = {L} \\implies x = {x_opt}\\text{{ m}}$$\n"
        f"Step 4: Find $y$ and maximum area:\n"
        f"$$y = {L} - 2({x_opt}) = {y_opt}\\text{{ m}}$$\n"
        f"$$\\text{{Maximum Area}} = {x_opt} \\times {y_opt} = {area_max}\\text{{ m}}^2$$."
    )
    return _mcq_q(
        rng, f"g12_calc_46_{rng.randint(100000, 999999)}", "46_applied_optimisation_max_area_rectangle",
        "Applied Optimisation of Rectangular Enclosure Area", prompt, correct, distractors, sol,
        {"tier_1": "Write area A(x) = x(L - 2x), then solve A'(x) = 0.",
         "tier_2": f"A'(x) = {L} - 4x = 0 gives x = {x_opt}. Then y = {y_opt}.",
         "tier_3": correct},
        ["assumed_square_gives_maximum_with_three_fenced_sides"],
        diagram_spec=_svg_spec(svg),
    )


def arch_47_applied_optimisation_box_volume_open_top(rng: random.Random) -> Dict[str, Any]:
    # Square cardboard of side S. Corners of side x are cut out.
    # Base: (S - 2x) by (S - 2x). Height: x.
    # V(x) = x(S - 2x)^2 = x(S^2 - 4Sx + 4x^2) = 4x^3 - 4Sx^2 + S^2 x.
    # V'(x) = 12x^2 - 8Sx + S^2 = (6x - S)(2x - S) = 0 => x = S/6 (since x < S/2).
    S = rng.choice([12, 18, 24, 30])
    x_opt = S // 6
    v_max = x_opt * ((S - 2 * x_opt) ** 2)
    prompt = (
        f"An open-top rectangular box is manufactured from a square piece of cardboard with side length ${S}\\text{{ cm}}$ "
        f"by cutting identical squares of side length $x\\text{{ cm}}$ from each of the four corners and folding up the sides.\n\n"
        f"Determine the value of $x$ that will maximise the volume of the box."
    )
    ans = f"x = {x_opt} cm"
    sol = (
        f"Step 1: Express box dimensions in terms of $x$:\n"
        f"$$\\text{{Length}} = {S} - 2x, \\quad \\text{{Width}} = {S} - 2x, \\quad \\text{{Height}} = x$$\n"
        f"Step 2: Volume function:\n"
        f"$$V(x) = x({S} - 2x)^2 = x({S**2} - {4*S}x + 4x^2) = 4x^3 - {4*S}x^2 + {S**2}x$$\n"
        f"Step 3: Differentiate and set $V'(x) = 0$:\n"
        f"$$V'(x) = 12x^2 - {8*S}x + {S**2} = 0$$\n"
        f"$$(6x - {S})(2x - {S}) = 0$$\n"
        f"Since cutting $x = {S // 2}$ would leave zero base, the physical solution is:\n"
        f"$$6x = {S} \\implies x = \\frac{{{S}}}{{6}} = {x_opt}\\text{{ cm}}$$\n"
        f"Maximum volume: $V({x_opt}) = {x_opt}({S - 2*x_opt})^2 = {v_max}\\text{{ cm}}^3$."
    )
    return _calc_q(
        rng, f"g12_calc_47_{rng.randint(100000, 999999)}", "47_applied_optimisation_box_volume_open_top",
        "Applied Optimisation - Box Volume from Cardboard Sheet", prompt, ans, sol,
        {"tier_1": f"Volume V(x) = x({S} - 2x)^2. Differentiate with respect to x and set to 0.",
         "tier_2": f"V'(x) = 12x^2 - {8*S}x + {S**2} = (6x - {S})(2x - {S}) = 0.",
         "tier_3": f"x = {x_opt} cm."},
        ["selected_unrealistic_root_cutting_entire_sheet"]
    )


def arch_48_applied_optimisation_cylinder_volume_surface_area(rng: random.Random) -> Dict[str, Any]:
    # Cylinder volume V = pi * r^2 * h = 1000 => h = 1000 / (pi * r^2)
    # Total surface area A = 2*pi*r^2 + 2*pi*r*h = 2*pi*r^2 + 2000 / r
    # A'(r) = 4*pi*r - 2000 / r^2 = 0 => 4*pi*r^3 = 2000 => r^3 = 500 / pi => r = (500 / pi)^(1/3)
    k_vol = rng.choice([250, 500, 1000])
    target_r3 = k_vol / (2 * math.pi)
    r_val = round(target_r3 ** (1 / 3), 2)
    prompt = (
        f"A closed cylindrical can has a fixed internal volume of ${k_vol}\\text{{ cm}}^3$.\n\n"
        f"1. Show that the total surface area of the can can be expressed as $A(r) = 2\\pi r^2 + \\frac{{{2 * k_vol}}}{{r}}$.\n"
        f"2. Determine the radius $r$ (correct to two decimal places) that minimises the surface area."
    )
    ans = f"r = {r_val} cm"
    sol = (
        f"Step 1: Volume formula: $V = \\pi r^2 h = {k_vol} \\implies h = \\frac{{{k_vol}}}{{\\pi r^2}}$\n"
        f"Surface area: $A = 2\\pi r^2 + 2\\pi r h = 2\\pi r^2 + 2\\pi r \\left(\\frac{{{k_vol}}}{{\\pi r^2}}\\right) = 2\\pi r^2 + \\frac{{{2 * k_vol}}}{{r}}$\n"
        f"Step 2: Differentiate with respect to $r$ and set to $0$:\n"
        f"$$A'(r) = 4\\pi r - \\frac{{{2 * k_vol}}}{{r^2}} = 0$$\n"
        f"$$4\\pi r^3 = {2 * k_vol} \\implies r^3 = \\frac{{{k_vol}}}{{2\\pi}}$$\n"
        f"$$r = \\sqrt[3]{{\\frac{{{k_vol}}}{{2\\pi}}}} \\approx {r_val}\\text{{ cm}}$$."
    )
    return _calc_q(
        rng, f"g12_calc_48_{rng.randint(100000, 999999)}", "48_applied_optimisation_cylinder_volume_surface_area",
        "Minimising Surface Area of Cylindrical Container", prompt, ans, sol,
        {"tier_1": "Express h in terms of r using V = pi * r^2 * h, then substitute into A = 2*pi*r^2 + 2*pi*r*h.",
         "tier_2": f"Solve A'(r) = 4*pi*r - {2*k_vol}/r^2 = 0 to get r^3 = {k_vol} / (2*pi).",
         "tier_3": f"r = {r_val} cm."},
        ["forgot_to_include_both_circular_bases_in_surface_area"]
    )


def arch_49_cubic_tangent_and_stationary_points_svg(rng: random.Random) -> Dict[str, Any]:
    # Visual cubic with local max at (-1; y_max) and local min at (2; y_min)
    case = rng.choice([1, 2])
    stroke_col = rng.choice(["#2563eb", "#1d4ed8", "#3b82f6"])
    ref_tag = rng.randint(10, 99)
    if case == 1:
        # f(x) = 2x^3 - 3x^2 - 12x + 10. Local max at (-1; 17), local min at (2; -10)
        p_name = "f(x) = 2x^3 - 3x^2 - 12x + 10"
        x_max, y_max = -1, 17
        x_min, y_min = 2, -10
        x_infl = 0.5
        y_int = 10
        svg_max_y = 60
        svg_min_y = 170
        sol_infl = "x = -b / (3a) = -(-3) / (3*2) = 0{,}5"
    else:
        # f(x) = x^3 - 3x^2 - 9x + 15. Local max at (-1; 20), local min at (3; -12)
        p_name = "f(x) = x^3 - 3x^2 - 9x + 15"
        x_max, y_max = -1, 20
        x_min, y_min = 3, -12
        x_infl = 1.0
        y_int = 15
        svg_max_y = 50
        svg_min_y = 180
        sol_infl = "x = -b / (3a) = -(-3) / (3*1) = 1"

    svg_body = (
        f'<line x1="40" y1="120" x2="360" y2="120" stroke="#94a3b8" stroke-width="1.5"/>'
        f'<line x1="160" y1="20" x2="160" y2="220" stroke="#94a3b8" stroke-width="1.5"/>'
        f'<path d="M 60,200 C 80,40 120,{svg_max_y} 160,110 C 200,160 240,{svg_min_y} 320,40" fill="none" stroke="{stroke_col}" stroke-width="2.5"/>'
        f'<circle cx="120" cy="{svg_max_y}" r="4" fill="#dc2626"/><text x="80" y="{svg_max_y - 8}" font-size="10" fill="#dc2626">Max ({x_max}; {y_max})</text>'
        f'<circle cx="160" cy="110" r="4" fill="#16a34a"/><text x="165" y="110" font-size="10" fill="#16a34a">(0; {y_int})</text>'
        f'<circle cx="240" cy="{svg_min_y}" r="4" fill="#dc2626"/><text x="235" y="{svg_min_y + 15}" font-size="10" fill="#dc2626">Min ({x_min}; {y_min})</text>'
        f'<text x="230" y="30" font-size="11" font-weight="bold" fill="{stroke_col}">{p_name} [Ref #{ref_tag}]</text>'
    )
    prompt = (
        f"The visual display presents the cubic polynomial ${p_name}$.\n\n"
        f"1. State the coordinates of the local maximum and local minimum points shown.\n"
        f"2. Calculate the $x$-coordinate of the point of inflection."
    )
    correct = f"Local max: ({x_max}; {y_max}); Local min: ({x_min}; {y_min}); Inflection at x = {x_infl}"
    distractors = [
        f"Local max: ({x_min}; {y_min}); Local min: ({x_max}; {y_max}); Inflection at x = 0",
        f"Local max: ({x_max}; 0); Local min: ({x_min}; 0); Inflection at x = {x_infl}",
        f"Local max: ({x_max}; {y_max}); Local min: ({x_min}; {y_min}); Inflection at x = {x_max + x_min}",
    ]
    sol = (
        f"Step 1: Read the stationary coordinates directly from the display:\n"
        f"Local Maximum: $({x_max};\\ {y_max})$\n"
        f"Local Minimum: $({x_min};\\ {y_min})$\n"
        f"Step 2: The point of inflection occurs at the midpoint of the stationary $x$-values (or $x = -b / (3a)$):\n"
        f"$$x_{{\\text{{infl}}}} = \\frac{{{x_max} + {x_min}}}{{2}} = {x_infl}$$\n"
        f"Alternatively: {sol_infl}."
    )
    return _mcq_q(
        rng, f"g12_calc_49_{rng.randint(100000, 999999)}", "49_cubic_tangent_and_stationary_points_svg",
        "Cubic Curve Stationary Features and Inflection Point", prompt, correct, distractors, sol,
        {"tier_1": "Local max is the peak; local min is the trough.",
         "tier_2": "The inflection point x-coordinate is the average of the stationary x-coordinates.",
         "tier_3": correct},
        ["swapped_local_max_and_min_coordinates"],
        diagram_spec=_svg_spec(svg_body, 580, 240)
    )


def arch_50_compound_nsc_exam_differential_calculus(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([1, 2])
    b = rng.choice([-6, -3, 3, 6])
    x0 = rng.choice([1, 2])
    prompt = (
        f"**Comprehensive Examination Level 4 Problem:**\n\n"
        f"Given $f(x) = {a if a != 1 else ''}x^3 {'+' if b >= 0 else '-'} {abs(b)}x^2$:\n\n"
        f"1. Differentiate $g(x) = {2*a}x^2 - 5x$ from first principles.\n"
        f"2. Determine the coordinates of the turning points of $f$.\n"
        f"3. Find the equation of the tangent to $f$ at the point where $x = {x0}$."
    )
    # Turning points of f: f'(x) = 3a*x^2 + 2b*x = x(3a*x + 2b) = 0 => x = 0, x = -2b/(3a)
    correct = f"g'(x) = {4*a}x - 5; f turning points at x = 0 and x = {-2*b / (3*a):.2f}; tangent found via point-slope"
    distractors = [
        f"g'(x) = {2*a}x - 5; f turning points at x = 0 and x = {b}; tangent is horizontal",
        f"g'(x) = {4*a}x; f has no turning points; tangent y = {x0}x",
        f"g'(x) = 0; f turning points at x = {-b}; tangent is vertical",
    ]
    sol = (
        f"Step 1: First principles for $g(x)$:\n"
        f"$$g'(x) = \\lim_{{h \\to 0}} \\frac{{g(x+h) - g(x)}}{{h}} = {4*a}x - 5$$\n"
        f"Step 2: Turning points of $f(x) = {a if a != 1 else ''}x^3 {'+' if b >= 0 else '-'} {abs(b)}x^2$:\n"
        f"$$f'(x) = {3*a}x^2 {'+' if 2*b >= 0 else '-'} {abs(2*b)}x = x({3*a}x {'+' if 2*b >= 0 else '-'} {abs(2*b)}) = 0$$\n"
        f"Roots: $x = 0$ and $x = {-2*b / (3*a):.2f}$.\n"
        f"Step 3: Tangent equation at $x = {x0}$:\n"
        f"Find $y_0 = f({x0})$, $m = f'({x0})$, and apply $y - y_0 = m(x - x_0)$."
    )
    return _mcq_q(
        rng, f"g12_calc_50_{rng.randint(100000, 999999)}", "50_compound_nsc_exam_differential_calculus",
        "Comprehensive Examination Compound Calculus Problem", prompt, correct, distractors, sol,
        {"tier_1": "Combine first principles differentiation with cubic derivative stationary point analysis.",
         "tier_2": "Solve f'(x) = 0 by factoring out x.",
         "tier_3": correct},
        ["confused_different_functions_in_compound_problem"]
    )


# ==============================================================================
# Subskills Dictionary and Builders Mapping for 26 - 50
# ==============================================================================

BUILDERS_26_50: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    "26_tangent_perpendicular_to_given_line": arch_26_tangent_perpendicular_to_given_line,
    "27_horizontal_tangent_points": arch_27_horizontal_tangent_points,
    "28_second_derivative_calculation": arch_28_second_derivative_calculation,
    "29_second_derivative_at_point": arch_29_second_derivative_at_point,
    "30_cubic_stationary_turning_points": arch_30_cubic_stationary_turning_points,
    "31_cubic_point_of_inflection_formula": arch_31_cubic_point_of_inflection_formula,
    "32_cubic_nature_of_turning_points_second_derivative_test": arch_32_cubic_nature_of_turning_points_second_derivative_test,
    "33_cubic_intervals_increasing_and_decreasing": arch_33_cubic_intervals_increasing_and_decreasing,
    "34_cubic_concavity_intervals": arch_34_cubic_concavity_intervals,
    "35_cubic_intercepts_axes_full": arch_35_cubic_intercepts_axes_full,
    "36_cubic_sketching_features_identification": arch_36_cubic_sketching_features_identification,
    "37_cubic_equation_from_turning_point_and_intercept": arch_37_cubic_equation_from_turning_point_and_intercept,
    "38_cubic_equation_from_three_intercepts_and_point": arch_38_cubic_equation_from_three_intercepts_and_point,
    "39_cubic_gradient_at_inflection_point": arch_39_cubic_gradient_at_inflection_point,
    "40_cubic_graph_interpretation_f_prime_positive": arch_40_cubic_graph_interpretation_f_prime_positive,
    "41_cubic_graph_interpretation_f_times_f_prime": arch_41_cubic_graph_interpretation_f_times_f_prime,
    "42_parabola_derivative_graph_connection": arch_42_parabola_derivative_graph_connection,
    "43_number_of_real_roots_from_turning_points_k": arch_43_number_of_real_roots_from_turning_points_k,
    "44_rate_of_change_kinematics_velocity_acceleration": arch_44_rate_of_change_kinematics_velocity_acceleration,
    "45_rate_of_change_maximum_height_projectile": arch_45_rate_of_change_maximum_height_projectile,
    "46_applied_optimisation_max_area_rectangle": arch_46_applied_optimisation_max_area_rectangle,
    "47_applied_optimisation_box_volume_open_top": arch_47_applied_optimisation_box_volume_open_top,
    "48_applied_optimisation_cylinder_volume_surface_area": arch_48_applied_optimisation_cylinder_volume_surface_area,
    "49_cubic_tangent_and_stationary_points_svg": arch_49_cubic_tangent_and_stationary_points_svg,
    "50_compound_nsc_exam_differential_calculus": arch_50_compound_nsc_exam_differential_calculus,
}

SUBSKILLS_26_50: Dict[str, str] = {
    "26_tangent_perpendicular_to_given_line": "Point of Tangency Perpendicular to Given Linear Slope",
    "27_horizontal_tangent_points": "Point of Contact of Horizontal Tangent Line",
    "28_second_derivative_calculation": "Calculation of Second Derivative of Cubic Function",
    "29_second_derivative_at_point": "Second Derivative Evaluation and Concavity Test",
    "30_cubic_stationary_turning_points": "Coordinates of Cubic Stationary Points",
    "31_cubic_point_of_inflection_formula": "Coordinates of Point of Inflection of Cubic Function",
    "32_cubic_nature_of_turning_points_second_derivative_test": "Classifying Turning Points Using Second Derivative Test",
    "33_cubic_intervals_increasing_and_decreasing": "Intervals Where Cubic Function is Decreasing",
    "34_cubic_concavity_intervals": "Determining Concavity Intervals for Cubic Function",
    "35_cubic_intercepts_axes_full": "Axes Intercepts of Fully Factorised Cubic Curve",
    "36_cubic_sketching_features_identification": "End Behaviour and General Shape of Cubic Curves",
    "37_cubic_equation_from_turning_point_and_intercept": "Determining Cubic Equation from Tangent Intercept and Crossing",
    "38_cubic_equation_from_three_intercepts_and_point": "Determining Leading Coefficient of Cubic from Intercepts",
    "39_cubic_gradient_at_inflection_point": "Minimum Gradient of Cubic Function at Inflection Point",
    "40_cubic_graph_interpretation_f_prime_positive": "Deducing Gradient Sign from Stationary Points",
    "41_cubic_graph_interpretation_f_times_f_prime": "Graphical Meaning of Sign Product f(x) * f'(x)",
    "42_parabola_derivative_graph_connection": "Connecting Derivative x-Intercepts to Turning Points of Original Function",
    "43_number_of_real_roots_from_turning_points_k": "Number of Real Roots of Cubic Dependent on Parameter k",
    "44_rate_of_change_kinematics_velocity_acceleration": "Instantaneous Velocity from Displacement Function",
    "45_rate_of_change_maximum_height_projectile": "Maximum Height of Projectile via Optimisation",
    "46_applied_optimisation_max_area_rectangle": "Applied Optimisation of Rectangular Enclosure Area",
    "47_applied_optimisation_box_volume_open_top": "Applied Optimisation - Box Volume from Cardboard Sheet",
    "48_applied_optimisation_cylinder_volume_surface_area": "Minimising Surface Area of Cylindrical Container",
    "49_cubic_tangent_and_stationary_points_svg": "Cubic Curve Stationary Features and Inflection Point",
    "50_compound_nsc_exam_differential_calculus": "Comprehensive Examination Compound Calculus Problem",
}
