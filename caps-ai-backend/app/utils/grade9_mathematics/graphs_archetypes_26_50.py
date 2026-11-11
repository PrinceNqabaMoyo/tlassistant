"""Grade 9 Mathematics - Graphs & Linear Functions Archetypes 26 to 50
====================================================================
Grounded strictly in:
  - CAPS Grade 9 Mathematics: Term 2 Topic: Graphs & Linear Functions
  - curriculum_docs_auto/Mathematics_Gr9/Term 2/02. Graphs.md
  - Chapter 15: Equations of straight lines, parallel and perpendicular lines,
    points of intersection, and real-world rate of change applications

Covers Archetypes 26 - 50:
  26: Equation from two points with positive slope
  27: Equation from two points with negative slope
  28: Equation from two points with fractional gradient
  29: Determining equation from a plotted line on Cartesian grid
  30: Testing if a point lies on a line (collinearity / substitution)
  31: Finding missing coordinate of a point lying on a line
  32: Distance between two axis intercepts using Pythagoras
  33: Identifying parallel lines from equations (m1 = m2)
  34: Equation of a parallel line through a given point
  35: Identifying perpendicular lines from equations (m1 * m2 = -1)
  36: Determining perpendicular gradient (negative reciprocal)
  37: Equation of a perpendicular line through a given point
  38: Classifying geometric relationships of line pairs
  39: Reading point of intersection from a Cartesian graph
  40: Solving point of intersection algebraically
  41: Intersection of a line with a horizontal or vertical line
  42: Area of right-angled triangle formed by line and coordinate axes
  43: Rate of change in water tank filling context
  44: Rate of change in water tank draining context
  45: Average speed calculation from distance-time graph
  46: Interpreting multi-stage distance-time journey graph
  47: Tariff / phone plan comparison and break-even point
  48: Business break-even analysis (Income vs Expenses)
  49: Error analysis: inverted gradient formula (dx / dy error)
  50: Compound multi-step graph analysis synthesis challenge
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional

from app.utils.grade9_mathematics.graphs_svg import (
    draw_cartesian_plane_svg,
    draw_dual_intercept_svg,
    draw_slope_triangle_svg,
    draw_intersecting_lines_svg,
    draw_rate_context_graph_svg,
)


def arch_26_equation_from_two_points_positive_slope(rng: random.Random) -> Dict[str, Any]:
    """Find line equation y = mx + c given two points with positive slope."""
    m = rng.choice([1, 2, 3, 4])
    x1 = rng.randint(-3, 1)
    dx = rng.choice([1, 2, 3])
    x2 = x1 + dx
    c = rng.randint(-3, 4)
    y1 = m * x1 + c
    y2 = m * x2 + c

    seed_val = rng.randint(1000, 999999)
    lines = [{"m": m, "c": c, "color": "#38bdf8", "stroke_width": 2.5, "label": "Line AB"}]
    points = [
        {"x": x1, "y": y1, "label": f"A({x1}; {y1})", "color": "#38bdf8", "fill": "#38bdf8", "highlight": True},
        {"x": x2, "y": y2, "label": f"B({x2}; {y2})", "color": "#38bdf8", "fill": "#38bdf8", "highlight": True},
    ]
    svg = draw_cartesian_plane_svg(lines=lines, points=points, title="Line Through Two Points", seed=seed_val)

    prompt = (
        f"A straight line passes through the points **$A({x1};\\ {y1})$** and **$B({x2};\\ {y2})$**.\n\n"
        f"1. Calculate the gradient ($m$).\n"
        f"2. Determine the $y$-intercept ($c$).\n\n"
        f"State the value of the **$y$-intercept ($c$)**."
    )

    return {
        "subskill": "26_equation_from_two_points_positive_slope",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": str(c),
        "sample_answer": str(c),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Calculate gradient: m = ({y2} - {y1}) / ({x2} - {x1}) = {y2 - y1} / {x2 - x1} = {m}", "marks": 1},
            {"step": f"Substitute point A({x1}; {y1}) into y = mx + c: {y1} = {m}({x1}) + c", "marks": 1},
            {"step": f"Solve for c: c = {y1} - {m * x1} = {c}", "marks": 1},
        ],
        "hints": [
            f"Step 1: Calculate $m = \\frac{{{y2} - ({y1})}}{{{x2} - ({x1})}} = {m}$.",
            f"Step 2: Substitute $m = {m}$ and point $A({x1};\\ {y1})$ into $y = mx + c$.",
            f"${y1} = {m}({x1}) + c \\implies c = {c}$.",
        ],
        "misconception_tags": ["two_points_gradient_error", "intercept_substitution_error"],
    }


def arch_27_equation_from_two_points_negative_slope(rng: random.Random) -> Dict[str, Any]:
    """Find line equation given two points with negative slope."""
    m = rng.choice([-3, -2, -1])
    x1 = rng.randint(-3, 0)
    dx = rng.choice([1, 2, 3])
    x2 = x1 + dx
    c = rng.randint(-3, 3)
    y1 = m * x1 + c
    y2 = m * x2 + c

    seed_val = rng.randint(1000, 999999)
    lines = [{"m": m, "c": c, "color": "#f43f5e", "stroke_width": 2.5, "label": "Line CD"}]
    points = [
        {"x": x1, "y": y1, "label": f"C({x1}; {y1})", "color": "#f43f5e", "fill": "#f43f5e", "highlight": True},
        {"x": x2, "y": y2, "label": f"D({x2}; {y2})", "color": "#f43f5e", "fill": "#f43f5e", "highlight": True},
    ]
    svg = draw_cartesian_plane_svg(lines=lines, points=points, title="Line with Negative Slope", seed=seed_val)

    prompt = (
        f"A straight line passes through **$C({x1};\\ {y1})$** and **$D({x2};\\ {y2})$**.\n\n"
        f"Calculate the **gradient ($m$)** of the line."
    )

    return {
        "subskill": "27_equation_from_two_points_negative_slope",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": str(m),
        "sample_answer": str(m),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "State gradient formula: m = (y2 - y1) / (x2 - x1)", "marks": 1},
            {"step": f"Substitute: m = ({y2} - ({y1})) / ({x2} - ({x1})) = {y2 - y1} / {x2 - x1} = {m}", "marks": 1},
        ],
        "hints": [
            "Use the standard gradient formula: $m = \\frac{y_2 - y_1}{x_2 - x_1}$.",
            f"Be careful with negative signs: $m = \\frac{{{y2} - ({y1})}}{{{x2} - ({x1})}} = \\frac{{{y2 - y1}}}{{{x2 - x1}}}$.",
            f"The gradient is $m = {m}$.",
        ],
        "misconception_tags": ["negative_slope_sign_loss", "coordinates_subtraction_order_error"],
    }


def arch_28_equation_from_two_points_fractional_gradient(rng: random.Random) -> Dict[str, Any]:
    """Line with fractional gradient; find value of y at given integer x."""
    num, den = rng.choice([(1, 2), (-1, 2), (1, 3), (2, 3)])
    c = rng.randint(-3, 3)
    x1 = 0
    y1 = c
    x2 = den * 2
    y2 = c + num * 2

    x_test = den * 3
    y_test = c + num * 3

    prompt = (
        f"A straight line passes through the points **$(0;\\ {c})$** and **$({x2};\\ {y2})$**.\n\n"
        f"1. Determine the equation of the line in the form $y = mx + c$.\n"
        f"2. Calculate the value of **$y$** when **$x = {x_test}$**."
    )

    return {
        "subskill": "28_equation_from_two_points_fractional_gradient",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": str(y_test),
        "sample_answer": str(y_test),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Identify y-intercept c = {c} from point (0; {c})", "marks": 1},
            {"step": f"Calculate gradient: m = ({y2} - {c}) / ({x2} - 0) = {num * 2} / {den * 2} = {num}/{den}", "marks": 1},
            {"step": f"Substitute x = {x_test}: y = ({num}/{den})({x_test}) + ({c}) = {y_test}", "marks": 1},
        ],
        "hints": [
            f"Since the line passes through $(0;\\ {c})$, the $y$-intercept is $c = {c}$.",
            f"Gradient $m = \\frac{{{y2} - {c}}}{{{x2} - 0}} = \\frac{{{num}}}{{{den}}}$.",
            f"Substitute $x = {x_test}$: $y = \\frac{{{num}}}{{{den}}}({x_test}) + ({c}) = {y_test}$.",
        ],
        "misconception_tags": ["fractional_multiplication_error", "substituting_fraction_into_linear_rule"],
    }


def arch_29_determine_equation_from_plotted_line_graph(rng: random.Random) -> Dict[str, Any]:
    """Read two clean integer points from a plotted line and state gradient m."""
    m = rng.choice([-3, -2, -1, 1, 2, 3])
    c = rng.choice([-3, -2, -1, 0, 1, 2, 3])
    x1 = -1
    y1 = m * x1 + c
    x2 = 2
    y2 = m * x2 + c

    seed_val = rng.randint(1000, 999999)
    lines = [{"m": m, "c": c, "color": "#38bdf8", "stroke_width": 2.5, "label": "Line k"}]
    points = [
        {"x": x1, "y": y1, "label": f"({x1}; {y1})", "color": "#fbbf24", "fill": "#fbbf24", "highlight": True},
        {"x": x2, "y": y2, "label": f"({x2}; {y2})", "color": "#fbbf24", "fill": "#fbbf24", "highlight": True},
    ]
    svg = draw_cartesian_plane_svg(lines=lines, points=points, title="Line k on Cartesian Grid", seed=seed_val)

    prompt = (
        f"Refer to **Line k** plotted on the Cartesian plane below, passing through marked points "
        f"**$({x1};\\ {y1})$** and **$({x2};\\ {y2})$**:\n\n"
        f"Calculate the **gradient ($m$)** of Line k."
    )

    return {
        "subskill": "29_determine_equation_from_plotted_line_graph",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": str(m),
        "sample_answer": str(m),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Identify coordinates of two marked grid points", "marks": 1},
            {"step": f"Calculate gradient: m = ({y2} - ({y1})) / ({x2} - ({x1})) = {m}", "marks": 1},
        ],
        "hints": [
            "Use the marked points to find the vertical change $\\Delta y$ and horizontal change $\\Delta x$.",
            f"$\\Delta y = {y2} - ({y1}) = {y2 - y1}$ and $\\Delta x = {x2} - ({x1}) = {x2 - x1}$.",
            f"Gradient $m = \\frac{{{y2 - y1}}}{{{x2 - x1}}} = {m}$.",
        ],
        "misconception_tags": ["reading_grid_points_error", "gradient_calculation_from_graph"],
    }


def arch_30_point_lies_on_line_test_collinearity(rng: random.Random) -> Dict[str, Any]:
    """Test whether a given coordinate point lies on the line y = mx + c (LHS = RHS)."""
    m = rng.choice([-3, -2, 2, 3])
    c = rng.randint(-4, 4)
    x_test = rng.choice([-3, -2, -1, 1, 2, 3])
    lies_on_line = rng.choice([True, False])

    if lies_on_line:
        y_test = m * x_test + c
        ans = "yes"
        reason = f"LHS = {y_test} and RHS = {m}({x_test}) + ({c}) = {y_test}, so LHS = RHS"
    else:
        offset = rng.choice([-3, -2, -1, 1, 2, 3])
        y_test = m * x_test + c + offset
        ans = "no"
        reason = f"LHS = {y_test} but RHS = {m}({x_test}) + ({c}) = {m * x_test + c}, so LHS ≠ RHS"

    op = "+" if c >= 0 else "-"

    prompt = (
        f"Consider the straight-line equation:\n"
        f"$$y = {m}x {op} {abs(c)}$$\n\n"
        f"Does the point **$P({x_test};\\ {y_test})$** lie on this straight line? (Answer: **yes** or **no**)."
    )

    return {
        "subskill": "30_point_lies_on_line_test_collinearity",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": ans,
        "sample_answer": ans,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Substitute x = {x_test} and y = {y_test} into the equation", "marks": 1},
            {"step": f"Evaluate LHS and RHS: {reason}", "marks": 1},
            {"step": f"State conclusion: {ans}", "marks": 1},
        ],
        "hints": [
            "Substitute the $x$-coordinate into the right-hand side of the equation.",
            f"RHS $= {m}({x_test}) + ({c}) = {m * x_test + c}$.",
            f"Comparing with the given $y$-value (${y_test}$), {ans}.",
        ],
        "misconception_tags": ["point_on_line_verification_error", "lhs_rhs_substitution_error"],
    }


def arch_31_find_missing_coordinate_on_line(rng: random.Random) -> Dict[str, Any]:
    """Find unknown coordinate k for a point lying on the line."""
    m = rng.choice([-3, -2, 2, 3])
    c = rng.randint(-4, 4)
    x_val = rng.randint(-4, 4)
    y_val = m * x_val + c
    op = "+" if c >= 0 else "-"

    find_x = rng.choice([True, False])
    if find_x:
        prompt = (
            f"The point **$A(k;\\ {y_val})$** lies on the straight line:\n"
            f"$$y = {m}x {op} {abs(c)}$$\n\n"
            f"Solve for the unknown coordinate **$k$**."
        )
        ans = str(x_val)
        calc_step = f"Substitute y = {y_val}: {y_val} = {m}k {op} {abs(c)} => {m}k = {y_val - c} => k = {x_val}"
    else:
        prompt = (
            f"The point **$B({x_val};\\ k)$** lies on the straight line:\n"
            f"$$y = {m}x {op} {abs(c)}$$\n\n"
            f"Calculate the value of **$k$**."
        )
        ans = str(y_val)
        calc_step = f"Substitute x = {x_val}: k = {m}({x_val}) {op} {abs(c)} = {y_val}"

    return {
        "subskill": "31_find_missing_coordinate_on_line",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": ans,
        "sample_answer": ans,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Substitute given coordinate into line equation", "marks": 1},
            {"step": calc_step, "marks": 1},
        ],
        "hints": [
            "A point lies on a line if its coordinates satisfy the line's equation.",
            "Substitute the known value and solve the resulting simple linear equation for $k$.",
            f"Answer: $k = {ans}$.",
        ],
        "misconception_tags": ["missing_coordinate_algebraic_error", "swapping_x_and_y_in_substitution"],
    }


def arch_32_find_distance_between_two_axis_intercepts(rng: random.Random) -> Dict[str, Any]:
    """Distance between x and y intercepts using Pythagoras (clean Pythagorean triples)."""
    # Pythagorean triples: (3, 4, 5), (6, 8, 10), (5, 12, 13)
    triple = rng.choice([(3, 4, 5), (4, 3, 5), (6, 8, 10), (8, 6, 10)])
    a, c_val, hyp = triple
    sign_a = rng.choice([-1, 1])
    sign_c = rng.choice([-1, 1])
    x_int = a * sign_a
    y_int = c_val * sign_c

    # Line passing through (x_int, 0) and (0, y_int)
    # m = -y_int / x_int
    seed_val = rng.randint(1000, 999999)
    svg = draw_dual_intercept_svg(x_int=x_int, y_int=y_int, line_label=f"Distance = {hyp}", seed=seed_val)

    prompt = (
        f"A straight line cuts the axes at:\n"
        f"- $x$-intercept: **$A({x_int};\\ 0)$**\n"
        f"- $y$-intercept: **$B(0;\\ {y_int})$**\n\n"
        f"Using the **Theorem of Pythagoras**, calculate the distance between the two intercepts (the length of line segment $AB$)."
    )

    return {
        "subskill": "32_find_distance_between_two_axis_intercepts",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": str(hyp),
        "sample_answer": f"{hyp} units",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Identify lengths of the two legs: OA = |{x_int}| = {a}, OB = |{y_int}| = {c_val}", "marks": 1},
            {"step": f"Apply Pythagoras: AB^2 = OA^2 + OB^2 = {a}^2 + {c_val}^2 = {a**2} + {c_val**2} = {hyp**2}", "marks": 1},
            {"step": f"Calculate AB = √({hyp**2}) = {hyp}", "marks": 1},
        ],
        "hints": [
            "The coordinate axes are perpendicular ($90^\\circ$), forming right-angled triangle $\\triangle AOB$.",
            f"Leg lengths: $OA = {a}$ and $OB = {c_val}$.",
            f"Distance $AB = \\sqrt{{{a}^2 + {c_val}^2}} = \\sqrt{{{hyp**2}}} = {hyp}$.",
        ],
        "misconception_tags": ["pythagoras_sign_error_with_negative_intercepts", "distance_formula_arithmetic_error"],
    }


def arch_33_identify_parallel_lines_from_equations(rng: random.Random) -> Dict[str, Any]:
    """Determine whether two equations represent parallel lines (m1 = m2)."""
    m1 = rng.choice([-3, -2, 2, 3])
    c1 = rng.randint(-4, 0)
    c2 = rng.randint(1, 5)

    is_parallel = rng.choice([True, False])
    if is_parallel:
        m2 = m1
        ans = "parallel"
        reason = f"both lines have identical gradients m1 = m2 = {m1}"
    else:
        m2 = -m1 if m1 != -m1 else m1 + 1
        ans = "not parallel"
        reason = f"their gradients are different (m1 = {m1} while m2 = {m2})"

    op1 = "+" if c1 >= 0 else "-"
    op2 = "+" if c2 >= 0 else "-"

    prompt = (
        f"Consider the equations of two straight lines:\n"
        f"- **Line 1:** $y = {m1}x {op1} {abs(c1)}$\n"
        f"- **Line 2:** $y = {m2}x {op2} {abs(c2)}$\n\n"
        f"Are these two lines **parallel** or **not parallel**?"
    )

    return {
        "subskill": "33_identify_parallel_lines_from_equations",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": ans,
        "sample_answer": ans,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"State gradient of Line 1: m1 = {m1}", "marks": 1},
            {"step": f"State gradient of Line 2: m2 = {m2}", "marks": 1},
            {"step": f"Conclude lines are {ans} because {reason}", "marks": 1},
        ],
        "hints": [
            "Two lines are parallel if and only if they have the exact same gradient ($m_1 = m_2$).",
            f"Here, $m_1 = {m1}$ and $m_2 = {m2}$.",
            f"Since their gradients are {'equal' if is_parallel else 'not equal'}, they are {ans}.",
        ],
        "misconception_tags": ["parallel_gradient_condition_confusion", "comparing_intercepts_instead_of_gradients"],
    }


def arch_34_equation_of_parallel_line_through_given_point(rng: random.Random) -> Dict[str, Any]:
    """Find y-intercept c of a line parallel to y = mx + k passing through (x1, y1)."""
    m = rng.choice([-3, -2, 2, 3])
    c_orig = rng.randint(-5, 5)
    x1 = rng.randint(-3, 3)
    c_new = rng.choice([k for k in range(-6, 7) if k != c_orig])
    y1 = m * x1 + c_new
    op = "+" if c_orig >= 0 else "-"

    prompt = (
        f"A line $L_2$ is **parallel** to the line $L_1: y = {m}x {op} {abs(c_orig)}$ and passes through "
        f"the point **$P({x1};\\ {y1})$**.\n\n"
        f"Calculate the **$y$-intercept ($c$)** of line $L_2$."
    )

    return {
        "subskill": "34_equation_of_parallel_line_through_given_point",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": str(c_new),
        "sample_answer": str(c_new),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Parallel lines share equal gradients, so m2 = m1 = {m}", "marks": 1},
            {"step": f"Substitute P({x1}; {y1}) into y = {m}x + c: {y1} = {m}({x1}) + c", "marks": 1},
            {"step": f"Solve for c: c = {y1} - {m * x1} = {c_new}", "marks": 1},
        ],
        "hints": [
            f"Because $L_2$ is parallel to $L_1$, its gradient is also $m = {m}$.",
            f"Substitute $m = {m}$ and point $P({x1};\\ {y1})$ into $y = mx + c$.",
            f"${y1} = ({m})({x1}) + c \\implies c = {c_new}$.",
        ],
        "misconception_tags": ["parallel_slope_inversion", "parallel_line_intercept_reuse"],
    }


def arch_35_identify_perpendicular_lines_from_equations(rng: random.Random) -> Dict[str, Any]:
    """Identify if two lines are perpendicular by checking m1 * m2 = -1."""
    m_int = rng.choice([2, 3, 4])
    is_perp = rng.choice([True, False])

    if is_perp:
        m1 = m_int
        m2_str = f"-1/{m_int}"
        ans = "perpendicular"
        reason = f"m1 * m2 = ({m_int}) * (-1/{m_int}) = -1"
    else:
        m1 = m_int
        m2_str = f"1/{m_int}"
        ans = "not perpendicular"
        reason = f"m1 * m2 = ({m_int}) * (1/{m_int}) = 1 ≠ -1 (they are reciprocals but have the same sign)"

    c1 = rng.randint(-3, 3)
    c2 = rng.randint(-3, 3)

    prompt = (
        f"Two straight lines have the following equations:\n"
        f"- **Line 1:** $y = {m1}x + {c1}$\n"
        f"- **Line 2:** $y = {m2_str}x + {c2}$\n\n"
        f"Are these two lines **perpendicular** or **not perpendicular**?"
    )

    return {
        "subskill": "35_identify_perpendicular_lines_from_equations",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": ans,
        "sample_answer": ans,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Determine product of gradients: m1 * m2 = {reason}", "marks": 1},
            {"step": f"State conclusion: {ans}", "marks": 1},
        ],
        "hints": [
            "Two lines are perpendicular if the product of their gradients is $-1$ ($m_1 \\times m_2 = -1$).",
            f"Multiply: $({m1}) \\times ({m2_str})$.",
            f"Since the product is {'$-1$' if is_perp else 'not $-1$'}, the lines are {ans}.",
        ],
        "misconception_tags": ["perpendicular_gradient_sign_error", "reciprocal_without_sign_change_error"],
    }


def arch_36_determine_perpendicular_gradient(rng: random.Random) -> Dict[str, Any]:
    """Calculate perpendicular gradient m_perp = -1/m."""
    options = [
        (2, "-1/2"),
        (-2, "1/2"),
        (3, "-1/3"),
        (-3, "1/3"),
        (4, "-1/4"),
        (-4, "1/4"),
        (1, "-1"),
        (-1, "1"),
    ]
    m_given, ans_str = rng.choice(options)

    prompt = (
        f"A straight line has a gradient of **$m = {m_given}$**.\n\n"
        f"What is the gradient ($m_\\perp$) of any straight line that is **perpendicular** to this line?\n"
        f"(Express your answer as a simplified integer or fraction, e.g. `-1/2` or `1/3`)."
    )

    return {
        "subskill": "36_determine_perpendicular_gradient",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": ans_str,
        "sample_answer": ans_str,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "State perpendicular gradient rule: m1 * m2 = -1 => m_perp = -1 / m", "marks": 1},
            {"step": f"Calculate m_perp = -1 / ({m_given}) = {ans_str}", "marks": 1},
        ],
        "hints": [
            "The perpendicular gradient is the negative reciprocal: $m_\\perp = -\\frac{1}{m}$.",
            f"Take the reciprocal of ${m_given}$ and change its sign.",
            f"Perpendicular gradient $m_\\perp = {ans_str}$.",
        ],
        "misconception_tags": ["perpendicular_gradient_forgot_negative", "reciprocal_arithmetic_confusion"],
    }


def arch_37_equation_of_perpendicular_line_through_given_point(rng: random.Random) -> Dict[str, Any]:
    """Equation of line perpendicular to y = -x + c passing through (x1, y1)."""
    # Use m1 = -1 => m2 = 1, or m1 = 1 => m2 = -1 for clean integer arithmetic
    m1 = rng.choice([-1, 1])
    m2 = -1 // m1
    c1 = rng.randint(-4, 4)
    x1 = rng.randint(-4, 4)
    c2 = rng.randint(-4, 4)
    y1 = m2 * x1 + c2

    m1_str = "x" if m1 == 1 else "-x"
    op1 = "+" if c1 >= 0 else "-"

    prompt = (
        f"Line $L_1$ has equation $y = {m1_str} {op1} {abs(c1)}$.\n"
        f"Line $L_2$ is **perpendicular** to line $L_1$ and passes through the point **$P({x1};\\ {y1})$**.\n\n"
        f"Calculate the **$y$-intercept ($c$)** of line $L_2$."
    )

    return {
        "subskill": "37_equation_of_perpendicular_line_through_given_point",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": str(c2),
        "sample_answer": str(c2),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Calculate perpendicular gradient: m2 = -1 / ({m1}) = {m2}", "marks": 1},
            {"step": f"Substitute P({x1}; {y1}) into y = {m2}x + c: {y1} = {m2}({x1}) + c", "marks": 1},
            {"step": f"Solve for c: c = {y1} - {m2 * x1} = {c2}", "marks": 1},
        ],
        "hints": [
            f"Gradient of $L_1$ is $m_1 = {m1}$. Since $L_2 \\perp L_1$, $m_2 = -\\frac{{1}}{{{m1}}} = {m2}$.",
            f"Substitute $m = {m2}$ and $P({x1};\\ {y1})$ into $y = mx + c$.",
            f"${y1} = ({m2})({x1}) + c \\implies c = {c2}$.",
        ],
        "misconception_tags": ["perpendicular_equation_wrong_slope", "perpendicular_intercept_calculation_error"],
    }


def arch_38_parallel_and_perpendicular_geometric_classification(rng: random.Random) -> Dict[str, Any]:
    """Classify geometric relationship of two lines (parallel, perpendicular, or neither)."""
    rel = rng.choice(["parallel", "perpendicular", "neither"])
    seed_val = rng.randint(1000, 999999)

    if rel == "parallel":
        m1 = 2
        m2 = 2
        c1, c2 = -3, 2
        lines = [
            {"m": m1, "c": c1, "color": "#38bdf8", "stroke_width": 2.5, "label": "L1: y = 2x - 3"},
            {"m": m2, "c": c2, "color": "#10b981", "stroke_width": 2.5, "label": "L2: y = 2x + 2"},
        ]
        explanation = "they have the same gradient (m1 = m2 = 2)"
    elif rel == "perpendicular":
        m1 = 1
        m2 = -1
        c1, c2 = -1, 3
        lines = [
            {"m": m1, "c": c1, "color": "#38bdf8", "stroke_width": 2.5, "label": "L1: y = x - 1"},
            {"m": m2, "c": c2, "color": "#f43f5e", "stroke_width": 2.5, "label": "L2: y = -x + 3"},
        ]
        explanation = "the product of their gradients is m1 * m2 = (1)(-1) = -1"
    else:
        m1 = 2
        m2 = 1
        c1, c2 = -2, 1
        lines = [
            {"m": m1, "c": c1, "color": "#38bdf8", "stroke_width": 2.5, "label": "L1: y = 2x - 2"},
            {"m": m2, "c": c2, "color": "#ec4899", "stroke_width": 2.5, "label": "L2: y = x + 1"},
        ]
        explanation = "their gradients are neither equal nor negative reciprocals (m1 = 2, m2 = 1, product = 2)"

    svg = draw_cartesian_plane_svg(lines=lines, title="Geometric Relationship of Line Pair", seed=seed_val)

    prompt = (
        f"Examine the two plotted straight lines $L_1$ and $L_2$ on the Cartesian plane below.\n\n"
        f"Are the lines **parallel**, **perpendicular**, or **neither**?"
    )

    return {
        "subskill": "38_parallel_and_perpendicular_geometric_classification",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": rel,
        "sample_answer": rel,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Inspect and compare gradients of both lines: {explanation}", "marks": 1},
            {"step": f"Conclude relationship is {rel}", "marks": 1},
        ],
        "hints": [
            "Check if $m_1 = m_2$ (parallel).",
            "Check if $m_1 \\times m_2 = -1$ (perpendicular).",
            f"The lines are {rel}.",
        ],
        "misconception_tags": ["parallel_perpendicular_neither_confusion", "visual_misjudgment_of_lines"],
    }


def arch_39_point_of_intersection_from_graph(rng: random.Random) -> Dict[str, Any]:
    """Read point of intersection (x; y) of two lines from a plotted graph."""
    ix = rng.choice([-3, -2, -1, 1, 2, 3])
    iy = rng.choice([-3, -2, -1, 1, 2, 3])
    seed_val = rng.randint(1000, 999999)

    # Line 1: m1 = 1 => c1 = iy - ix
    # Line 2: m2 = -1 => c2 = iy + ix
    m1, c1 = 1, iy - ix
    m2, c2 = -1, iy + ix

    line1 = {"m": m1, "c": c1, "color": "#38bdf8", "stroke_width": 2.5, "label": "Line 1"}
    line2 = {"m": m2, "c": c2, "color": "#f43f5e", "stroke_width": 2.5, "label": "Line 2"}

    svg = draw_intersecting_lines_svg(line1, line2, (ix, iy), seed=seed_val)
    ans_str = f"({ix}; {iy})"

    prompt = (
        f"Two straight lines intersect at point **P** on the Cartesian plane below.\n\n"
        f"Read off the coordinates of the **point of intersection P** in the form $(x;\\ y)$."
    )

    return {
        "subskill": "39_point_of_intersection_from_graph",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": ans_str,
        "sample_answer": ans_str,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Read x-coordinate of intersection: x = {ix}", "marks": 1},
            {"step": f"Read y-coordinate of intersection: y = {iy}", "marks": 1},
            {"step": f"State coordinate pair: P({ix}; {iy})", "marks": 1},
        ],
        "hints": [
            "Follow the vertical guideline from point P down to the horizontal $x$-axis.",
            "Follow the horizontal guideline from point P across to the vertical $y$-axis.",
            f"The intersection point is $P({ix};\\ {iy})$.",
        ],
        "misconception_tags": ["reading_intersection_coordinates_error", "swapping_intersection_x_and_y"],
    }


def arch_40_solve_point_of_intersection_algebraically_integer(rng: random.Random) -> Dict[str, Any]:
    """Solve for point of intersection of two lines algebraically."""
    # Line 1: y = 2x + c1
    # Line 2: y = -x + c2
    # At intersection: 2x + c1 = -x + c2 => 3x = c2 - c1 => x = (c2 - c1)/3
    x_int = rng.choice([-3, -2, -1, 1, 2, 3])
    m1, m2 = 2, -1
    c1 = rng.randint(-3, 3)
    # y = 2 * x_int + c1
    y_int = m1 * x_int + c1
    # c2 = y_int - m2 * x_int = y_int + x_int
    c2 = y_int - m2 * x_int

    op1 = "+" if c1 >= 0 else "-"
    op2 = "+" if c2 >= 0 else "-"

    prompt = (
        f"Find the coordinates of the point of intersection of the two lines:\n"
        f"1. $y = {m1}x {op1} {abs(c1)}$\n"
        f"2. $y = -x {op2} {abs(c2)}$\n\n"
        f"Calculate the **$x$-coordinate** of the intersection point."
    )

    return {
        "subskill": "40_solve_point_of_intersection_algebraically_integer",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": str(x_int),
        "sample_answer": str(x_int),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Equate expressions for y: {m1}x {op1} {abs(c1)} = -x {op2} {abs(c2)}", "marks": 1},
            {"step": f"Group terms: 3x = {c2 - c1}", "marks": 1},
            {"step": f"Solve for x: x = {x_int}", "marks": 1},
        ],
        "hints": [
            "At the point of intersection, the two lines have the same $y$-value: set $y_1 = y_2$.",
            f"${m1}x {op1} {abs(c1)} = -x {op2} {abs(c2)}$.",
            f"Add $x$ to both sides and solve: $3x = {c2 - c1} \\implies x = {x_int}$.",
        ],
        "misconception_tags": ["simultaneous_equating_error", "linear_equation_variable_grouping_error"],
    }


def arch_41_intersection_of_line_with_horizontal_or_vertical_line(rng: random.Random) -> Dict[str, Any]:
    """Intersection of straight line with a horizontal line y = k."""
    m = rng.choice([-3, -2, 2, 3])
    x_val = rng.randint(-4, 4)
    c = rng.randint(-3, 3)
    k = m * x_val + c
    op = "+" if c >= 0 else "-"

    prompt = (
        f"Line $L_1$ has equation $y = {m}x {op} {abs(c)}$.\n"
        f"Line $L_2$ is the horizontal line $y = {k}$.\n\n"
        f"Determine the **$x$-coordinate** of the point where these two lines intersect."
    )

    return {
        "subskill": "41_intersection_of_line_with_horizontal_or_vertical_line",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": str(x_val),
        "sample_answer": str(x_val),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Substitute y = {k} into the equation of L1: {k} = {m}x {op} {abs(c)}", "marks": 1},
            {"step": f"Solve for x: {m}x = {k - c} => x = {x_val}", "marks": 1},
        ],
        "hints": [
            f"Substitute $y = {k}$ directly into $y = {m}x {op} {abs(c)}$.",
            f"${k} = {m}x {op} {abs(c)} \\implies {m}x = {k - c}$.",
            f"Divide by ${m}$: $x = {x_val}$.",
        ],
        "misconception_tags": ["horizontal_line_substitution_confusion", "algebraic_isolation_error"],
    }


def arch_42_area_of_triangle_formed_by_line_and_axes(rng: random.Random) -> Dict[str, Any]:
    """Area of right-angled triangle formed by line y = mx + c and coordinate axes."""
    # Choose clean base and height
    b = rng.choice([2, 4, 6])
    h = rng.choice([3, 4, 5, 6])
    area = (b * h) // 2

    # m = -h / b, c = h
    prompt = (
        f"A straight line cuts the coordinate axes at:\n"
        f"- $x$-intercept: $A({b};\\ 0)$\n"
        f"- $y$-intercept: $B(0;\\ {h})$\n\n"
        f"Calculate the **area of triangle $\\triangle AOB$** formed by the line, the $x$-axis, and the $y$-axis "
        f"(where $O$ is the origin)."
    )

    return {
        "subskill": "42_area_of_triangle_formed_by_line_and_axes",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": str(area),
        "sample_answer": f"{area} square units",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Identify base OA = {b} and height OB = {h}", "marks": 1},
            {"step": f"Apply right-angled triangle area formula: Area = 1/2 * base * height", "marks": 1},
            {"step": f"Calculate: Area = 1/2 * {b} * {h} = {area}", "marks": 1},
        ],
        "hints": [
            "The coordinate axes are perpendicular, so $\\triangle AOB$ is a right-angled triangle.",
            f"Base $= {b}$ and height $= {h}$.",
            f"$\\text{{Area}} = \\frac{{1}}{{2}} \\times {b} \\times {h} = {area}$ square units.",
        ],
        "misconception_tags": ["triangle_area_forgot_half", "negative_dimension_in_area_error"],
    }


def arch_43_rate_of_change_water_tank_filling(rng: random.Random) -> Dict[str, Any]:
    """Interpret constant rate of change in a water tank filling context."""
    initial_vol = rng.choice([20, 50, 100])
    rate = rng.choice([10, 15, 20, 25])
    time_hrs = rng.choice([2, 3, 4, 5])
    vol_at_t = initial_vol + rate * time_hrs
    seed_val = rng.randint(1000, 999999)

    pts = [(0, initial_vol), (time_hrs, vol_at_t), (6, initial_vol + rate * 6)]
    segments = [{"points": pts, "color": "#06b6d4", "label": "Volume V(t)"}]
    svg = draw_rate_context_graph_svg(
        segments=segments,
        x_label="Time (hours)",
        y_label="Volume (litres)",
        title="Filling a Rainwater Tank",
        x_max=8,
        y_max=250,
        seed=seed_val,
    )

    prompt = (
        f"A rainwater tank is being filled at a constant rate, as shown in the graph below.\n"
        f"- At $t = 0\\text{{ hours}}$, the volume is ${initial_vol}\\text{{ litres}}$.\n"
        f"- At $t = {time_hrs}\\text{{ hours}}$, the volume reaches ${vol_at_t}\\text{{ litres}}$.\n\n"
        f"Calculate the **rate of filling (rate of change)** in litres per hour."
    )

    return {
        "subskill": "43_rate_of_change_water_tank_filling",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": str(rate),
        "sample_answer": f"{rate} litres/hour",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Calculate change in volume: ΔV = {vol_at_t} - {initial_vol} = {vol_at_t - initial_vol} litres", "marks": 1},
            {"step": f"Calculate change in time: Δt = {time_hrs} - 0 = {time_hrs} hours", "marks": 1},
            {"step": f"Rate of change = ΔV / Δt = {vol_at_t - initial_vol} / {time_hrs} = {rate} litres/hour", "marks": 1},
        ],
        "hints": [
            "Rate of change is the gradient of the graph: $\\text{Rate} = \\frac{\\Delta y}{\\Delta x}$.",
            f"Change in volume: ${vol_at_t} - {initial_vol} = {vol_at_t - initial_vol}$ litres over ${time_hrs}$ hours.",
            f"Rate $= \\frac{{{vol_at_t - initial_vol}}}{{{time_hrs}}} = {rate}$ litres/hour.",
        ],
        "misconception_tags": ["initial_value_omission_in_rate", "rate_of_change_unit_confusion"],
    }


def arch_44_rate_of_change_water_tank_draining(rng: random.Random) -> Dict[str, Any]:
    """Calculate time until a tank is empty given initial volume and constant draining rate."""
    drain_rate = rng.choice([20, 25, 40, 50])
    time_empty = rng.choice([3, 4, 5, 6])
    initial_vol = drain_rate * time_empty
    seed_val = rng.randint(1000, 999999)

    pts = [(0, initial_vol), (time_empty, 0)]
    segments = [{"points": pts, "color": "#f43f5e", "label": "Drainage"}]
    svg = draw_rate_context_graph_svg(
        segments=segments,
        x_label="Time (hours)",
        y_label="Volume (litres)",
        title="Draining a Storage Tank",
        x_max=8,
        y_max=initial_vol + 40,
        seed=seed_val,
    )

    prompt = (
        f"A tank holding an initial volume of **${initial_vol}\\text{{ litres}}$** of water is drained at a "
        f"constant rate of **${drain_rate}\\text{{ litres per hour}}$**.\n\n"
        f"How many **hours** will it take for the tank to be completely empty ($0\\text{{ litres}}$)?"
    )

    return {
        "subskill": "44_rate_of_change_water_tank_draining",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": str(time_empty),
        "sample_answer": f"{time_empty} hours",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Set volume equation: V(t) = {initial_vol} - {drain_rate}t", "marks": 1},
            {"step": f"Set V = 0: 0 = {initial_vol} - {drain_rate}t => {drain_rate}t = {initial_vol}", "marks": 1},
            {"step": f"Solve for t: t = {initial_vol} / {drain_rate} = {time_empty} hours", "marks": 1},
        ],
        "hints": [
            f"The tank loses ${drain_rate}$ litres every hour.",
            f"Divide total volume by the drainage rate: $\\frac{{{initial_vol}}}{{{drain_rate}}}$.",
            f"Time to empty $= {time_empty}$ hours.",
        ],
        "misconception_tags": ["drainage_rate_sign_confusion", "time_to_empty_arithmetic_error"],
    }


def arch_45_distance_time_graph_average_speed_calculation(rng: random.Random) -> Dict[str, Any]:
    """Calculate average speed from distance-time graph (gradient = speed)."""
    speed = rng.choice([60, 70, 80, 90, 100])
    time_hrs = rng.choice([2, 3, 4])
    total_dist = speed * time_hrs
    seed_val = rng.randint(1000, 999999)

    pts = [(0, 0), (time_hrs, total_dist)]
    segments = [{"points": pts, "color": "#10b981", "label": "Distance"}]
    svg = draw_rate_context_graph_svg(
        segments=segments,
        x_label="Time (hours)",
        y_label="Distance (km)",
        title="Highway Journey Distance-Time Graph",
        x_max=6,
        y_max=total_dist + 50,
        seed=seed_val,
    )

    prompt = (
        f"A delivery van travels from Johannesburg towards Durban. Its distance-time graph is plotted below.\n"
        f"The van covers **${total_dist}\\text{{ km}}$** in **${time_hrs}\\text{{ hours}}$** at a steady speed.\n\n"
        f"Calculate the **average speed** of the van in $\\text{{km/h}}$."
    )

    return {
        "subskill": "45_distance_time_graph_average_speed_calculation",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": str(speed),
        "sample_answer": f"{speed} km/h",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "State speed formula: Speed = Distance / Time (gradient of graph)", "marks": 1},
            {"step": f"Substitute values: Speed = {total_dist} km / {time_hrs} h = {speed} km/h", "marks": 1},
        ],
        "hints": [
            "On a distance-time graph, the gradient represents speed: $\\text{Speed} = \\frac{\\Delta d}{\\Delta t}$.",
            f"Calculate: $\\frac{{{total_dist}}}{{{time_hrs}}}$.",
            f"Average speed $= {speed}\\text{{ km/h}}$.",
        ],
        "misconception_tags": ["speed_formula_inverted", "gradient_as_physical_speed_misunderstanding"],
    }


def arch_46_distance_time_graph_multi_stage_journey(rng: random.Random) -> Dict[str, Any]:
    """Calculate speed of a specific leg in a multi-stage journey."""
    t1 = rng.choice([2, 3])
    d1 = t1 * 60
    rest_duration = rng.choice([1, 2])
    t2 = t1 + rest_duration
    speed_leg2 = rng.choice([80, 100])
    t3 = t2 + 2
    d2 = d1 + speed_leg2 * 2
    seed_val = rng.randint(1000, 999999)

    pts = [(0, 0), (t1, d1), (t2, d1), (t3, d2)]
    segments = [{"points": pts, "color": "#38bdf8", "label": "Multi-leg Trip"}]
    svg = draw_rate_context_graph_svg(
        segments=segments,
        x_label="Time (hours)",
        y_label="Distance from Start (km)",
        title="Three-Stage Journey",
        x_max=8,
        y_max=d2 + 40,
        seed=seed_val,
    )

    prompt = (
        f"A multi-stage journey is represented in the distance-time graph below:\n"
        f"- **Stage 1 (0 to {t1} h):** Vehicle travels ${d1}\\text{{ km}}$.\n"
        f"- **Stage 2 ({t1} to {t2} h):** Vehicle rests.\n"
        f"- **Stage 3 ({t2} to {t3} h):** Vehicle resumes and reaches ${d2}\\text{{ km}}$.\n\n"
        f"Calculate the **speed during Stage 3** in $\\text{{km/h}}$."
    )

    return {
        "subskill": "46_distance_time_graph_multi_stage_journey",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": str(speed_leg2),
        "sample_answer": f"{speed_leg2} km/h",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Calculate distance covered in Stage 3: Δd = {d2} - {d1} = {d2 - d1} km", "marks": 1},
            {"step": f"Calculate time taken in Stage 3: Δt = {t3} - {t2} = {t3 - t2} hours", "marks": 1},
            {"step": f"Speed = Δd / Δt = {d2 - d1} / {t3 - t2} = {speed_leg2} km/h", "marks": 1},
        ],
        "hints": [
            f"Focus only on Stage 3 from $t = {t2}$ to $t = {t3}$.",
            f"Distance gained: ${d2} - {d1} = {d2 - d1}\\text{{ km}}$ over ${t3 - t2}\\text{{ hours}}$.",
            f"Speed $= \\frac{{{d2 - d1}}}{{{t3 - t2}}} = {speed_leg2}\\text{{ km/h}}$.",
        ],
        "misconception_tags": ["multi_stage_total_average_confusion", "segment_interval_time_calculation_error"],
    }


def arch_47_cellphone_tariff_or_taxi_fare_comparison(rng: random.Random) -> Dict[str, Any]:
    """Find break-even usage where two pricing plans cost the exact same."""
    # Plan A: No monthly fee, R3 per minute => y = 3x
    # Plan B: Monthly fee R100, R1 per minute => y = x + 100
    # Break even: 3x = x + 100 => 2x = 100 => x = 50 minutes
    r_a = rng.choice([3, 4])
    r_b = rng.choice([1, 2])
    base_b = rng.choice([60, 80, 100, 120])
    while base_b % (r_a - r_b) != 0:
        base_b += 10
    break_even_mins = base_b // (r_a - r_b)

    prompt = (
        f"Two mobile network calling plans are offered:\n"
        f"- **Plan A:** No monthly fee, but charges **$\\text{{R}}{r_a}$ per minute** ($y = {r_a}x$).\n"
        f"- **Plan B:** Monthly subscription fee of **$\\text{{R}}{base_b}$** plus **$\\text{{R}}{r_b}$ per minute** ($y = {r_b}x + {base_b}$).\n\n"
        f"For how many call minutes ($x$) will the two plans cost the **exact same total amount**?"
    )

    return {
        "subskill": "47_cellphone_tariff_or_taxi_fare_comparison",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": str(break_even_mins),
        "sample_answer": f"{break_even_mins} minutes",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Set Plan A cost equal to Plan B cost: {r_a}x = {r_b}x + {base_b}", "marks": 1},
            {"step": f"Subtract {r_b}x from both sides: {r_a - r_b}x = {base_b}", "marks": 1},
            {"step": f"Solve for x: x = {base_b} / {r_a - r_b} = {break_even_mins} minutes", "marks": 1},
        ],
        "hints": [
            "Set the two cost equations equal to each other.",
            f"${r_a}x = {r_b}x + {base_b}$.",
            f"Subtract ${r_b}x$: ${r_a - r_b}x = {base_b} \\implies x = {break_even_mins}$ minutes.",
        ],
        "misconception_tags": ["tariff_comparison_equating_error", "break_even_calculation_error"],
    }


def arch_48_business_break_even_income_vs_expenses(rng: random.Random) -> Dict[str, Any]:
    """Identify break-even production quantity (Income = Expenses)."""
    fixed_costs = rng.choice([400, 600, 800, 1000])
    variable_cost = rng.choice([10, 15, 20])
    selling_price = variable_cost + rng.choice([10, 20, 25])
    profit_per_unit = selling_price - variable_cost
    while fixed_costs % profit_per_unit != 0:
        fixed_costs += 50
    break_even_units = fixed_costs // profit_per_unit

    prompt = (
        f"A Grade 9 Market Day entrepreneur produces handmade beaded bracelets:\n"
        f"- **Total Production Cost:** $C(x) = {variable_cost}x + {fixed_costs}$ (where $x$ is bracelets made).\n"
        f"- **Total Income / Revenue:** $R(x) = {selling_price}x$.\n\n"
        f"Calculate the **break-even quantity** (number of bracelets that must be sold so Income equals Expenses)."
    )

    return {
        "subskill": "48_business_break_even_income_vs_expenses",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": str(break_even_units),
        "sample_answer": f"{break_even_units} bracelets",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Set Revenue equal to Cost: {selling_price}x = {variable_cost}x + {fixed_costs}", "marks": 1},
            {"step": f"Subtract variable cost: {profit_per_unit}x = {fixed_costs}", "marks": 1},
            {"step": f"Solve for x: x = {fixed_costs} / {profit_per_unit} = {break_even_units}", "marks": 1},
        ],
        "hints": [
            "At break-even, Total Revenue equals Total Cost: $R(x) = C(x)$.",
            f"${selling_price}x = {variable_cost}x + {fixed_costs}$.",
            f"${profit_per_unit}x = {fixed_costs} \\implies x = {break_even_units}$.",
        ],
        "misconception_tags": ["break_even_fixed_costs_omission", "revenue_cost_algebraic_error"],
    }


def arch_49_error_analysis_inverted_gradient_formula(rng: random.Random) -> Dict[str, Any]:
    """Diagnose inverted gradient formula error (student did dx / dy instead of dy / dx)."""
    dx = rng.choice([2, 4])
    dy = rng.choice([6, 8, 10, 12])
    while dy % dx != 0:
        dy += 2
    correct_m = dy // dx

    prompt = (
        f"A learner was asked to calculate the gradient of a straight line passing through "
        f"two points where the vertical change is $\\Delta y = {dy}$ and the horizontal change is $\\Delta x = {dx}$.\n\n"
        f"The learner wrote:\n"
        f"$$\\text{{Gradient}} = \\frac{{{dx}}}{{{dy}}} = \\frac{{1}}{{{dy // dx}}}$$\n\n"
        f"1. What fundamental mistake did the learner make?\n"
        f"2. What is the **correct gradient ($m$)** of the line?"
    )

    return {
        "subskill": "49_error_analysis_inverted_gradient_formula",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": str(correct_m),
        "sample_answer": str(correct_m),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Diagnose that learner inverted the formula by dividing run by rise (Δx / Δy) instead of rise by run (Δy / Δx)", "marks": 1},
            {"step": f"Apply correct formula: m = Δy / Δx = {dy} / {dx} = {correct_m}", "marks": 1},
        ],
        "hints": [
            "Gradient is always vertical change divided by horizontal change: $m = \\frac{\\text{rise}}{\\text{run}} = \\frac{\\Delta y}{\\Delta x}$.",
            f"The learner calculated $\\frac{{\\Delta x}}{{\\Delta y}}$ by mistake.",
            f"Correct gradient $m = \\frac{{{dy}}}{{{dx}}} = {correct_m}$.",
        ],
        "misconception_tags": ["gradient_formula_inversion_error", "run_over_rise_error"],
    }


def arch_50_compound_multi_step_graph_analysis(rng: random.Random) -> Dict[str, Any]:
    """Compound synthesis: Given line on Cartesian plane, determine m, c, and evaluate y at x = 5."""
    m = rng.choice([2, 3])
    c = rng.choice([-3, -2, -1, 1, 2])
    x1 = 0
    y1 = c
    x2 = 2
    y2 = m * 2 + c
    x_eval = 5
    y_eval = m * x_eval + c

    seed_val = rng.randint(1000, 999999)
    lines = [{"m": m, "c": c, "color": "#38bdf8", "stroke_width": 2.5, "label": "Line L"}]
    points = [
        {"x": x1, "y": y1, "label": f"(0; {c})", "color": "#34d399", "fill": "#34d399", "highlight": True},
        {"x": x2, "y": y2, "label": f"({x2}; {y2})", "color": "#fbbf24", "fill": "#fbbf24", "highlight": True},
    ]
    svg = draw_cartesian_plane_svg(lines=lines, points=points, title="Comprehensive Analysis of Line L", seed=seed_val)

    prompt = (
        f"Refer to **Line L** plotted on the Cartesian plane below, passing through "
        f"**$(0;\\ {c})$** and **$({x2};\\ {y2})$**:\n\n"
        f"1. Determine the gradient ($m$) of Line L.\n"
        f"2. Write down the equation in standard form $y = mx + c$.\n"
        f"3. Use your equation to calculate the value of **$y$** when **$x = {x_eval}$**."
    )

    return {
        "subskill": "50_compound_multi_step_graph_analysis",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": str(y_eval),
        "sample_answer": str(y_eval),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Calculate gradient: m = ({y2} - {c}) / ({x2} - 0) = {y2 - c} / {x2} = {m}", "marks": 1},
            {"step": f"Form equation: y = {m}x + ({c})", "marks": 1},
            {"step": f"Substitute x = {x_eval}: y = {m}({x_eval}) + ({c}) = {y_eval}", "marks": 1},
        ],
        "hints": [
            f"Gradient $m = \\frac{{{y2} - {c}}}{{{x2} - 0}} = {m}$.",
            f"The $y$-intercept is $c = {c}$, so equation is $y = {m}x + ({c})$.",
            f"When $x = {x_eval}$, $y = {m}({x_eval}) + ({c}) = {y_eval}$.",
        ],
        "misconception_tags": ["compound_graph_analysis_error", "linear_extrapolation_error"],
    }
