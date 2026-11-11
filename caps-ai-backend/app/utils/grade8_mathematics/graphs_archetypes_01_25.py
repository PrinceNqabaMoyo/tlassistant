"""
Grade 8 Mathematics - Graphs Archetypes (01 to 25).
100% CAPS-aligned deterministic question generators.
Adheres strictly to the 6-Pillar Generator Contract and Zero-Meta-Curriculum Invariant.
Grounded in curriculum_docs_auto/Mathematics_Gr8/Term 1/02. Graphs.md.
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional

from .svg_diagrams import draw_cartesian_plane_svg


def arch_01_identifying_quadrant_from_coordinates(rng: random.Random) -> Dict[str, Any]:
    quad = rng.choice([1, 2, 3, 4])
    if quad == 1:
        x = rng.randint(2, 8)
        y = rng.randint(2, 8)
        signs = "both x > 0 and y > 0"
    elif quad == 2:
        x = -rng.randint(2, 8)
        y = rng.randint(2, 8)
        signs = "x < 0 and y > 0"
    elif quad == 3:
        x = -rng.randint(2, 8)
        y = -rng.randint(2, 8)
        signs = "both x < 0 and y < 0"
    else:
        x = rng.randint(2, 8)
        y = -rng.randint(2, 8)
        signs = "x > 0 and y < 0"

    pt_name = rng.choice(["P", "Q", "R", "T"])

    return {
        "title": "Identifying Quadrant from Coordinates",
        "topic": "Graphs",
        "grade": 8,
        "term": 1,
        "subskill": "01_identifying_quadrant_from_coordinates",
        "difficulty": "easy",
        "question_text": (
            f"Consider the point **${pt_name}({x}; {y})$** on the Cartesian coordinate plane.\n\n"
            f"In which quadrant (Quadrant 1, 2, 3, or 4) does point ${pt_name}$ lie?"
        ),
        "correct_answer": f"Quadrant {quad}",
        "marking_schema": [
            f"Identify Quadrant {quad} based on signs: {x} and {y} (1 mark)",
        ],
        "hints": [
            "Remember quadrant signs: Q1 (+, +), Q2 (-, +), Q3 (-, -), Q4 (+, -).",
            f"For point ${pt_name}({x}; {y})$, {signs}.",
            f"Point ${pt_name}$ lies in Quadrant {quad}.",
        ],
        "misconception_tags": ["inverting_quadrant_numbering_order"],
        "diagram_spec": None,
    }


def arch_02_identifying_points_on_axes(rng: random.Random) -> Dict[str, Any]:
    axis_choice = rng.choice(["x_axis", "y_axis", "origin"])
    if axis_choice == "x_axis":
        x = rng.choice([-6, -4, -2, 3, 5, 7])
        y = 0
        ans = "x-axis"
        reason = "its y-coordinate is 0"
    elif axis_choice == "y_axis":
        x = 0
        y = rng.choice([-7, -5, -3, 2, 4, 6])
        ans = "y-axis"
        reason = "its x-coordinate is 0"
    else:
        x = 0
        y = 0
        ans = "origin"
        reason = "both coordinates are (0; 0)"

    return {
        "title": "Points on Axes and the Origin",
        "topic": "Graphs",
        "grade": 8,
        "term": 1,
        "subskill": "02_identifying_points_on_axes",
        "difficulty": "easy",
        "question_text": (
            f"State whether the point **$({x}; {y})$** lies on the **x-axis**, the **y-axis**, or at the **origin**."
        ),
        "correct_answer": ans,
        "marking_schema": [
            f"Identify axis location: '{ans}' (1 mark)",
        ],
        "hints": [
            "Any point where y = 0 lies on the x-axis.",
            "Any point where x = 0 lies on the y-axis.",
            f"Since {reason}, the point lies on the {ans}.",
        ],
        "misconception_tags": ["axis_coordinate_zero_inversion"],
        "diagram_spec": None,
    }


def arch_03_reading_coordinates_from_cartesian_plane_diagram(rng: random.Random) -> Dict[str, Any]:
    x = rng.choice([-4, -3, -2, 2, 3, 4])
    y = rng.choice([-4, -3, -1, 1, 3, 4])
    pt_label = rng.choice(["A", "B", "C", "D"])

    seed_val = rng.randint(1, 1000000)
    svg = draw_cartesian_plane_svg(
        points=[(float(x), float(y), pt_label)],
        x_range=(-5, 5),
        y_range=(-5, 5),
        title="Cartesian Plane",
        seed=seed_val,
    )

    ans = f"({x}; {y})"

    return {
        "title": "Reading Coordinates from a Cartesian Plane",
        "topic": "Graphs",
        "grade": 8,
        "term": 1,
        "subskill": "03_reading_coordinates_from_cartesian_plane_diagram",
        "difficulty": "medium",
        "question_text": (
            "Refer to the Cartesian coordinate plane below.\n\n"
            f"Write down the coordinates of point **{pt_label}** in the standard format $(x; y)$."
        ),
        "correct_answer": ans,
        "marking_schema": [
            f"Read x-coordinate {x} [1M]",
            f"Read y-coordinate {y} and write ordered pair {ans} [1A]",
        ],
        "hints": [
            "Coordinates are always written in the order (x; y).",
            f"Look vertically down or up to the horizontal x-axis: x = {x}.",
            f"Look horizontally to the vertical y-axis: y = {y}. The coordinates are {ans}.",
        ],
        "misconception_tags": ["cartesian_x_y_coordinate_transposition"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


def arch_04_identifying_letter_for_given_coordinate_pair(rng: random.Random) -> Dict[str, Any]:
    pts = [
        (-3, 3, "A"),
        (4, 2, "B"),
        (-2, -4, "C"),
        (3, -3, "D"),
    ]
    target_x, target_y, target_letter = rng.choice(pts)

    seed_val = rng.randint(1, 1000000)
    svg = draw_cartesian_plane_svg(
        points=[(float(x), float(y), lbl) for x, y, lbl in pts],
        x_range=(-5, 5),
        y_range=(-5, 5),
        title="Cartesian Coordinate Grid",
        seed=seed_val,
    )

    return {
        "title": "Locating a Point on a Cartesian Grid",
        "topic": "Graphs",
        "grade": 8,
        "term": 1,
        "subskill": "04_identifying_letter_for_given_coordinate_pair",
        "difficulty": "medium",
        "question_text": (
            "Look at the Cartesian grid below with marked points A, B, C, and D.\n\n"
            f"Which letter represents the coordinates **$({target_x}; {target_y})$**?"
        ),
        "correct_answer": target_letter,
        "marking_schema": [
            f"Identify marked point: {target_letter} (1 mark)",
        ],
        "hints": [
            f"Start at the origin (0; 0). Move along the x-axis to {target_x}.",
            f"From there, move parallel to the y-axis to {target_y}.",
            f"The point at $({target_x}; {target_y})$ is marked with letter {target_letter}.",
        ],
        "misconception_tags": ["cartesian_x_y_coordinate_transposition"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


def arch_05_plotting_reflection_in_x_axis(rng: random.Random) -> Dict[str, Any]:
    x = rng.choice([-5, -3, 2, 4, 6])
    y = rng.choice([-4, -2, 3, 5])
    refl_x = x
    refl_y = -y

    return {
        "title": "Reflection of a Coordinate in the x-axis",
        "topic": "Graphs",
        "grade": 8,
        "term": 1,
        "subskill": "05_plotting_reflection_in_x_axis",
        "difficulty": "easy",
        "question_text": (
            f"A point has coordinates **$P({x}; {y})$**.\n\n"
            f"Determine the coordinates of the reflected point $P'$ after a reflection across the **x-axis**."
        ),
        "correct_answer": f"({refl_x}; {refl_y})",
        "marking_schema": [
            f"Apply reflection rule across x-axis: (x; y) -> (x; -y) => ({refl_x}; {refl_y}) (1 mark)",
        ],
        "hints": [
            "Under reflection in the x-axis, the x-coordinate stays the same and the y-coordinate changes sign.",
            f"Rule: $(x; y) \\longrightarrow (x; -y)$.",
            f"Image $P'$ is $({refl_x}; {refl_y})$.",
        ],
        "misconception_tags": ["reflection_axis_sign_change_confusion"],
        "diagram_spec": None,
    }


def arch_06_plotting_reflection_in_y_axis(rng: random.Random) -> Dict[str, Any]:
    x = rng.choice([-6, -3, 2, 5])
    y = rng.choice([-5, -1, 3, 4])
    refl_x = -x
    refl_y = y

    return {
        "title": "Reflection of a Coordinate in the y-axis",
        "topic": "Graphs",
        "grade": 8,
        "term": 1,
        "subskill": "06_plotting_reflection_in_y_axis",
        "difficulty": "easy",
        "question_text": (
            f"A point has coordinates **$A({x}; {y})$**.\n\n"
            f"Determine the coordinates of the reflected point $A'$ after a reflection across the **y-axis**."
        ),
        "correct_answer": f"({refl_x}; {refl_y})",
        "marking_schema": [
            f"Apply reflection rule across y-axis: (x; y) -> (-x; y) => ({refl_x}; {refl_y}) (1 mark)",
        ],
        "hints": [
            "Under reflection in the y-axis, the y-coordinate stays the same and the x-coordinate changes sign.",
            f"Rule: $(x; y) \\longrightarrow (-x; y)$.",
            f"Image $A'$ is $({refl_x}; {refl_y})$.",
        ],
        "misconception_tags": ["reflection_axis_sign_change_confusion"],
        "diagram_spec": None,
    }


def arch_07_identifying_independent_and_dependent_variables(rng: random.Random) -> Dict[str, Any]:
    scenarios = [
        ("The height of a sunflower measured daily over several weeks", "time (days)", "height of sunflower"),
        ("The total cost of purchasing petrol as the number of litres increases", "litres of petrol", "total cost"),
        ("The temperature of a cup of tea cooling over time", "time (minutes)", "temperature"),
        ("The distance covered by a cyclist riding at constant speed over several hours", "time (hours)", "distance covered"),
    ]
    desc, indep, dep = rng.choice(scenarios)
    target = rng.choice(["independent", "dependent"])
    ans = indep if target == "independent" else dep

    return {
        "title": "Independent vs Dependent Variables",
        "topic": "Graphs",
        "grade": 8,
        "term": 1,
        "subskill": "07_identifying_independent_and_dependent_variables",
        "difficulty": "easy",
        "question_text": (
            f"Consider the following real-world scenario:\n\n"
            f"**\"{desc}\"**\n\n"
            f"Identify the **{target} variable** in this relationship."
        ),
        "correct_answer": ans,
        "marking_schema": [
            f"Identify {target} variable: '{ans}' (1 mark)",
        ],
        "hints": [
            "The independent variable is the input (usually plotted on the horizontal x-axis).",
            "The dependent variable changes in response to the independent variable (vertical y-axis).",
            f"The {target} variable is {ans}.",
        ],
        "misconception_tags": ["independent_dependent_variable_inversion"],
        "diagram_spec": None,
    }


def arch_08_discrete_vs_continuous_data_identification(rng: random.Random) -> Dict[str, Any]:
    cases = [
        ("The number of learners attending school each day", "discrete", "Learners cannot be counted in fractions; they are whole separate units represented by distinct dots."),
        ("The mass of a growing puppy measured each week", "continuous", "Mass increases continuously through all fractional and decimal values, represented by an unbroken curve."),
        ("The temperature inside a refrigerator recorded throughout the afternoon", "continuous", "Temperature changes continuously without jumps."),
        ("The number of goals scored in soccer matches", "discrete", "Goals are counted in whole numbers only."),
    ]
    context, classification, reason = rng.choice(cases)

    return {
        "title": "Discrete vs Continuous Data",
        "topic": "Graphs",
        "grade": 8,
        "term": 1,
        "subskill": "08_discrete_vs_continuous_data_identification",
        "difficulty": "medium",
        "question_text": (
            f"Consider the following scenario: **\"{context}\"**.\n\n"
            f"State whether this data represents a **discrete** or **continuous** relationship on a graph."
        ),
        "correct_answer": classification,
        "marking_schema": [
            f"Classify data type: '{classification}' (1 mark)",
        ],
        "hints": [
            "Discrete data can only take specific separate values (usually counted in whole numbers) and is plotted as separate points.",
            "Continuous data can take any value within a range (measurements like time, mass, temperature) and forms an unbroken line.",
            f"Answer: {classification}.",
        ],
        "misconception_tags": ["discrete_continuous_data_confusion"],
        "diagram_spec": None,
    }


def arch_09_reading_distance_between_points_on_same_horizontal_line(rng: random.Random) -> Dict[str, Any]:
    y_common = rng.choice([-3, -1, 2, 4])
    x1 = rng.randint(-5, 0)
    dist = rng.randint(4, 9)
    x2 = x1 + dist

    return {
        "title": "Distance on Horizontal Line",
        "topic": "Graphs",
        "grade": 8,
        "term": 1,
        "subskill": "09_reading_distance_between_points_on_same_horizontal_line",
        "difficulty": "easy",
        "question_text": (
            f"Two points have coordinates **$A({x1}; {y_common})$** and **$B({x2}; {y_common})$**.\n\n"
            f"Calculate the horizontal distance between point $A$ and point $B$."
        ),
        "correct_answer": f"{dist} units",
        "marking_schema": [
            f"Subtract x-coordinates: {x2} - ({x1}) = {dist} units (1 mark)",
        ],
        "hints": [
            "Because both points have the same y-coordinate, the segment is horizontal.",
            f"Distance = $x_2 - x_1 = {x2} - ({x1})$.",
            f"Distance = {dist} units.",
        ],
        "misconception_tags": ["horizontal_distance_negative_sign_slip"],
        "diagram_spec": None,
    }


def arch_10_reading_distance_between_points_on_same_vertical_line(rng: random.Random) -> Dict[str, Any]:
    x_common = rng.choice([-4, -2, 1, 3, 5])
    y1 = rng.randint(-5, 0)
    dist = rng.randint(4, 9)
    y2 = y1 + dist

    return {
        "title": "Distance on Vertical Line",
        "topic": "Graphs",
        "grade": 8,
        "term": 1,
        "subskill": "10_reading_distance_between_points_on_same_vertical_line",
        "difficulty": "easy",
        "question_text": (
            f"Two points have coordinates **$P({x_common}; {y1})$** and **$Q({x_common}; {y2})$**.\n\n"
            f"Calculate the vertical distance between point $P$ and point $Q$."
        ),
        "correct_answer": f"{dist} units",
        "marking_schema": [
            f"Subtract y-coordinates: {y2} - ({y1}) = {dist} units (1 mark)",
        ],
        "hints": [
            "Because both points share the same x-coordinate, the segment is vertical.",
            f"Distance = $y_2 - y_1 = {y2} - ({y1})$.",
            f"Distance = {dist} units.",
        ],
        "misconception_tags": ["vertical_distance_sign_slip"],
        "diagram_spec": None,
    }


def arch_11_midpoint_of_horizontal_or_vertical_segment(rng: random.Random) -> Dict[str, Any]:
    x = rng.choice([-4, -2, 2, 4])
    y1 = rng.choice([-4, -2, 0])
    y2 = y1 + rng.choice([4, 6, 8])
    mid_y = (y1 + y2) // 2

    return {
        "title": "Midpoint of Vertical Line Segment",
        "topic": "Graphs",
        "grade": 8,
        "term": 1,
        "subskill": "11_midpoint_of_horizontal_or_vertical_segment",
        "difficulty": "medium",
        "question_text": (
            f"Find the coordinates of the midpoint $M$ of the segment connecting **$A({x}; {y1})$** and **$B({x}; {y2})$**."
        ),
        "correct_answer": f"({x}; {mid_y})",
        "marking_schema": [
            f"Calculate midpoint y-coordinate: ({y1} + {y2})/2 = {mid_y} [1M]",
            f"Ordered pair: ({x}; {mid_y}) [1A]",
        ],
        "hints": [
            "The x-coordinate is constant at x.",
            f"Calculate average of y-coordinates: $\\frac{{{y1} + {y2}}}{{2}} = {mid_y}$.",
            f"Midpoint = $({x}; {mid_y})$.",
        ],
        "misconception_tags": ["midpoint_averaging_subtraction_error"],
        "diagram_spec": None,
    }


def arch_12_cartesian_coordinates_collinear_points(rng: random.Random) -> Dict[str, Any]:
    m = rng.choice([-2, -1, 1, 2, 3])
    c = rng.choice([-3, 0, 2])
    x1, x2, x3 = 1, 2, 3
    y1 = m * x1 + c
    y2 = m * x2 + c
    is_collinear = rng.choice([True, False])
    if is_collinear:
        y3 = m * x3 + c
        ans = "Yes"
        reason = f"all points have constant gradient m = {m}"
    else:
        y3 = m * x3 + c + rng.choice([-2, 2])
        ans = "No"
        reason = "the gradients between the points are not equal"

    return {
        "title": "Collinear Points on Cartesian Plane",
        "topic": "Graphs",
        "grade": 8,
        "term": 1,
        "subskill": "12_cartesian_coordinates_collinear_points",
        "difficulty": "hard",
        "question_text": (
            f"Determine whether the three points **$A({x1}; {y1})$**, **$B({x2}; {y2})$**, and **$C({x3}; {y3})$** lie on the same straight line (collinear)."
        ),
        "correct_answer": ans,
        "marking_schema": [
            f"Compute gradients m_AB and m_BC and state {ans}: 2 marks",
        ],
        "hints": [
            "Three points are collinear if the gradient of AB equals the gradient of BC.",
            f"Gradient AB = $\\frac{{{y2} - ({y1})}}{{{x2} - {x1}}} = {y2 - y1}$.",
            f"Answer: {ans} ({reason}).",
        ],
        "misconception_tags": ["collinear_gradient_comparison_error"],
        "diagram_spec": None,
    }


def arch_13_completing_table_of_values_for_linear_graph(rng: random.Random) -> Dict[str, Any]:
    m = rng.choice([2, 3, -2])
    c = rng.randint(-3, 4)
    x_test = rng.choice([4, 5])
    y_test = m * x_test + c

    sign = "+" if c >= 0 else "-"
    abs_c = abs(c)

    return {
        "title": "Table of Values for Linear Function",
        "topic": "Graphs",
        "grade": 8,
        "term": 1,
        "subskill": "13_completing_table_of_values_for_linear_graph",
        "difficulty": "medium",
        "question_text": (
            f"A straight-line graph is defined by the formula **$y = {m}x {sign} {abs_c}$**.\n\n"
            f"Calculate the value of $y$ when **$x = {x_test}$**."
        ),
        "correct_answer": str(y_test),
        "marking_schema": [
            f"Substitute x = {x_test}: y = {m}({x_test}) {sign} {abs_c} = {y_test} (1 mark)",
        ],
        "hints": [
            f"Substitute ${x_test}$ in place of $x$ in the equation.",
            f"$y = {m}({x_test}) {sign} {abs_c} = {m * x_test} {sign} {abs_c}$.",
            f"$y = {y_test}$.",
        ],
        "misconception_tags": ["substitution_negative_multiplication_error"],
        "diagram_spec": None,
    }


def arch_14_matching_table_of_values_to_correct_linear_equation(rng: random.Random) -> Dict[str, Any]:
    m = rng.choice([2, 3, 4])
    c = rng.choice([1, 2, -1, -2])
    sign = "+" if c > 0 else "-"
    abs_c = abs(c)
    correct_eq = f"y = {m}x {sign} {abs_c}"

    p1 = (1, m * 1 + c)
    p2 = (2, m * 2 + c)
    p3 = (3, m * 3 + c)

    return {
        "title": "Matching Table of Values to Linear Equation",
        "topic": "Graphs",
        "grade": 8,
        "term": 1,
        "subskill": "14_matching_table_of_values_to_correct_linear_equation",
        "difficulty": "medium",
        "question_text": (
            f"A table of coordinates gives the following input-output pairs:\n\n"
            f"$$\\begin{{array}}{{|c|c|c|c|}} \\hline x & 1 & 2 & 3 \\\\ \\hline y & {p1[1]} & {p2[1]} & {p3[1]} \\\\ \\hline \\end{{array}}$$\n\n"
            f"Find the linear equation in the form $y = mx + c$ that describes this relation."
        ),
        "correct_answer": correct_eq,
        "marking_schema": [
            f"Determine gradient m = {m} and y-intercept c = {c} [1M]",
            f"Equation: {correct_eq} [1A]",
        ],
        "hints": [
            f"Find the constant difference in y: ${p2[1]} - {p1[1]} = {m}$. Thus $m = {m}$.",
            f"Find $c$ by substituting $x = 1$: ${p1[1]} = {m}(1) + c \\implies c = {c}$.",
            f"Equation: ${correct_eq}$.",
        ],
        "misconception_tags": ["gradient_intercept_equation_construction_error"],
        "diagram_spec": None,
    }


def arch_15_identifying_quadrant_signs_rule(rng: random.Random) -> Dict[str, Any]:
    q_target = rng.choice([1, 2, 3, 4])
    rules = {
        1: "(positive; positive) or (+; +)",
        2: "(negative; positive) or (-; +)",
        3: "(negative; negative) or (-; -)",
        4: "(positive; negative) or (+; -)",
    }
    ans = rules[q_target]

    return {
        "title": "Quadrant Sign Pattern Rules",
        "topic": "Graphs",
        "grade": 8,
        "term": 1,
        "subskill": "15_identifying_quadrant_signs_rule",
        "difficulty": "easy",
        "question_text": (
            f"State the signs of the $x$-coordinate and $y$-coordinate for any point situated in **Quadrant {q_target}**."
        ),
        "correct_answer": ans,
        "marking_schema": [
            f"State signs for Quadrant {q_target}: {ans} (1 mark)",
        ],
        "hints": [
            "In Q1, x > 0 and y > 0. In Q2, x < 0 and y > 0. In Q3, x < 0 and y < 0. In Q4, x > 0 and y < 0.",
            f"Quadrant {q_target} sign rule is {ans}.",
        ],
        "misconception_tags": ["quadrant_signs_inversion"],
        "diagram_spec": None,
    }


def arch_16_calculating_gradient_from_two_positive_points(rng: random.Random) -> Dict[str, Any]:
    m = rng.choice([2, 3, 4, 5])
    x1 = rng.randint(1, 3)
    dx = rng.choice([1, 2, 3])
    x2 = x1 + dx
    y1 = rng.randint(2, 6)
    y2 = y1 + m * dx

    return {
        "title": "Calculating Gradient from Positive Points",
        "topic": "Graphs",
        "grade": 8,
        "term": 1,
        "subskill": "16_calculating_gradient_from_two_positive_points",
        "difficulty": "easy",
        "question_text": (
            f"Calculate the gradient ($m$) of the line passing through the points:\n\n"
            f"$$A({x1}; {y1}) \\quad \\text{{and}} \\quad B({x2}; {y2})$$"
        ),
        "correct_answer": str(m),
        "marking_schema": [
            f"Apply formula m = (y2 - y1)/(x2 - x1): ({y2} - {y1})/({x2} - {x1}) = {m * dx}/{dx} = {m} (2 marks)",
        ],
        "hints": [
            "Gradient formula: $m = \\frac{y_2 - y_1}{x_2 - x_1}$.",
            f"Substitute: $m = \\frac{{{y2} - {y1}}}{{{x2} - {x1}}} = \\frac{{{m * dx}}}{{{dx}}}$.",
            f"Gradient $m = {m}$.",
        ],
        "misconception_tags": ["gradient_run_over_rise_inversion"],
        "diagram_spec": None,
    }


def arch_17_calculating_gradient_with_negative_coordinates(rng: random.Random) -> Dict[str, Any]:
    m = rng.choice([2, 3])
    x1 = -rng.randint(2, 5)
    dx = rng.choice([2, 3])
    x2 = x1 + dx
    y1 = -rng.randint(3, 8)
    y2 = y1 + m * dx

    return {
        "title": "Gradient with Negative Coordinates",
        "topic": "Graphs",
        "grade": 8,
        "term": 1,
        "subskill": "17_calculating_gradient_with_negative_coordinates",
        "difficulty": "medium",
        "question_text": (
            f"Calculate the slope $m$ of the straight line passing through:\n\n"
            f"$$P({x1}; {y1}) \\quad \\text{{and}} \\quad Q({x2}; {y2})$$"
        ),
        "correct_answer": str(m),
        "marking_schema": [
            f"Substitute into m = (y2 - y1)/(x2 - x1) with negative signs: {m} (2 marks)",
        ],
        "hints": [
            "Be careful with double negatives: $y_2 - y_1 = y_2 - (-y_1)$.",
            f"$m = \\frac{{{y2} - ({y1})}}{{{x2} - ({x1})}} = \\frac{{{y2 - y1}}}{{{x2 - x1}}}$.",
            f"Slope $m = {m}$.",
        ],
        "misconception_tags": ["gradient_double_negative_subtraction_slip"],
        "diagram_spec": None,
    }


def arch_18_calculating_negative_gradient_from_coordinates(rng: random.Random) -> Dict[str, Any]:
    m = -rng.choice([1, 2, 3])
    x1 = rng.randint(1, 3)
    dx = rng.choice([1, 2, 4])
    x2 = x1 + dx
    y1 = rng.randint(8, 14)
    y2 = y1 + m * dx

    return {
        "title": "Calculating a Negative Gradient",
        "topic": "Graphs",
        "grade": 8,
        "term": 1,
        "subskill": "18_calculating_negative_gradient_from_coordinates",
        "difficulty": "medium",
        "question_text": (
            f"Calculate the gradient $m$ of the downward-sloping line connecting:\n\n"
            f"$$C({x1}; {y1}) \\quad \\text{{and}} \\quad D({x2}; {y2})$$"
        ),
        "correct_answer": str(m),
        "marking_schema": [
            f"Calculate negative gradient: ({y2} - {y1})/({x2} - {x1}) = {m} (2 marks)",
        ],
        "hints": [
            "Since the line slopes downwards from left to right, its gradient must be negative.",
            f"$m = \\frac{{{y2} - {y1}}}{{{x2} - {x1}}} = \\frac{{{y2 - y1}}}{{{dx}}}$.",
            f"Gradient = {m}.",
        ],
        "misconception_tags": ["negative_gradient_sign_drop"],
        "diagram_spec": None,
    }


def arch_19_gradient_of_horizontal_line_zero(rng: random.Random) -> Dict[str, Any]:
    k = rng.choice([-4, -2, 3, 5])

    return {
        "title": "Gradient of a Horizontal Line",
        "topic": "Graphs",
        "grade": 8,
        "term": 1,
        "subskill": "19_gradient_of_horizontal_line_zero",
        "difficulty": "easy",
        "question_text": (
            f"Consider the horizontal line defined by the equation **$y = {k}$**.\n\n"
            f"State the numerical value of its gradient ($m$)."
        ),
        "correct_answer": "0",
        "marking_schema": [
            "Horizontal line has gradient m = 0: 1 mark",
        ],
        "hints": [
            "A horizontal line has zero vertical change (rise = 0).",
            "$m = \\frac{\\text{rise}}{\\text{run}} = \\frac{0}{\\text{run}} = 0$.",
            "The gradient is 0.",
        ],
        "misconception_tags": ["zero_gradient_vs_undefined_confusion"],
        "diagram_spec": None,
    }


def arch_20_gradient_of_vertical_line_undefined(rng: random.Random) -> Dict[str, Any]:
    k = rng.choice([-3, -1, 2, 4])

    return {
        "title": "Gradient of a Vertical Line",
        "topic": "Graphs",
        "grade": 8,
        "term": 1,
        "subskill": "20_gradient_of_vertical_line_undefined",
        "difficulty": "easy",
        "question_text": (
            f"Consider the vertical line with equation **$x = {k}$**.\n\n"
            f"State whether its gradient is zero, positive, negative, or **undefined**."
        ),
        "correct_answer": "undefined",
        "marking_schema": [
            "State gradient of vertical line is undefined: 1 mark",
        ],
        "hints": [
            "A vertical line has no horizontal change (run = 0).",
            "Division by zero is undefined in mathematics.",
            "The gradient is undefined.",
        ],
        "misconception_tags": ["zero_gradient_vs_undefined_confusion"],
        "diagram_spec": None,
    }


def arch_21_reading_gradient_directly_from_y_equals_mx_plus_c(rng: random.Random) -> Dict[str, Any]:
    m = rng.choice([-5, -4, -3, -2, 2, 3, 4, 7])
    c = rng.choice([-6, -1, 3, 5])
    sign = "+" if c > 0 else "-"
    abs_c = abs(c)

    return {
        "title": "Reading Gradient from Linear Equation",
        "topic": "Graphs",
        "grade": 8,
        "term": 1,
        "subskill": "21_reading_gradient_directly_from_y_equals_mx_plus_c",
        "difficulty": "easy",
        "question_text": (
            f"A straight line has the equation **$y = {m}x {sign} {abs_c}$**.\n\n"
            f"Identify the gradient ($m$) of this line."
        ),
        "correct_answer": str(m),
        "marking_schema": [
            f"Identify coefficient of x as gradient: m = {m} (1 mark)",
        ],
        "hints": [
            "In the standard form $y = mx + c$, $m$ is the coefficient of $x$ representing the gradient.",
            f"The number multiplying $x$ is {m}.",
            f"Gradient $m = {m}$.",
        ],
        "misconception_tags": ["reading_c_instead_of_m_as_gradient"],
        "diagram_spec": None,
    }


def arch_22_reading_y_intercept_from_equation(rng: random.Random) -> Dict[str, Any]:
    m = rng.choice([-3, 2, 4])
    c = rng.choice([-7, -4, -2, 3, 5, 8])
    sign = "+" if c > 0 else "-"
    abs_c = abs(c)

    return {
        "title": "Reading y-intercept from Equation",
        "topic": "Graphs",
        "grade": 8,
        "term": 1,
        "subskill": "22_reading_y_intercept_from_equation",
        "difficulty": "easy",
        "question_text": (
            f"For the straight line **$y = {m}x {sign} {abs_c}$**, write down the coordinates of its **y-intercept**."
        ),
        "correct_answer": f"(0; {c})",
        "marking_schema": [
            f"State y-intercept as coordinate pair: (0; {c}) (1 mark)",
        ],
        "hints": [
            "The y-intercept occurs where the line crosses the y-axis (where x = 0).",
            f"Substitute $x = 0$: $y = {m}(0) {sign} {abs_c} = {c}$.",
            f"Coordinates: $(0; {c})$.",
        ],
        "misconception_tags": ["y_intercept_coordinate_inversion_error"],
        "diagram_spec": None,
    }


def arch_23_finding_x_intercept_of_linear_graph(rng: random.Random) -> Dict[str, Any]:
    m = rng.choice([2, 3, 4, 5])
    x_int = rng.choice([-4, -3, -2, 1, 2, 3, 4])
    # y = m*x + c => 0 = m*x_int + c => c = -m*x_int
    c = -m * x_int
    sign = "+" if c >= 0 else "-"
    abs_c = abs(c)

    return {
        "title": "Finding the x-intercept of a Linear Graph",
        "topic": "Graphs",
        "grade": 8,
        "term": 1,
        "subskill": "23_finding_x_intercept_of_linear_graph",
        "difficulty": "medium",
        "question_text": (
            f"Find the coordinates of the **x-intercept** of the straight line:\n\n"
            f"$$y = {m}x {sign} {abs_c}$$"
        ),
        "correct_answer": f"({x_int}; 0)",
        "marking_schema": [
            f"Set y = 0 and solve {m}x {sign} {abs_c} = 0 => x = {x_int} [1M]",
            f"State coordinate: ({x_int}; 0) [1A]",
        ],
        "hints": [
            "The x-intercept occurs where the graph crosses the x-axis, so set $y = 0$.",
            f"$0 = {m}x {sign} {abs_c} \\implies {m}x = {-c} \\implies x = {x_int}$.",
            f"Coordinates: $({x_int}; 0)$.",
        ],
        "misconception_tags": ["x_intercept_y_value_omission_slip"],
        "diagram_spec": None,
    }


def arch_24_writing_equation_from_gradient_and_y_intercept(rng: random.Random) -> Dict[str, Any]:
    m = rng.choice([-3, -2, 2, 4, 5])
    c = rng.choice([-5, -2, 1, 3, 6])
    sign = "+" if c > 0 else "-"
    abs_c = abs(c)
    eq = f"y = {m}x {sign} {abs_c}"

    return {
        "title": "Writing Equation from Gradient and y-intercept",
        "topic": "Graphs",
        "grade": 8,
        "term": 1,
        "subskill": "24_writing_equation_from_gradient_and_y_intercept",
        "difficulty": "easy",
        "question_text": (
            f"A straight line has a gradient of **$m = {m}$** and a $y$-intercept of **$c = {c}$**.\n\n"
            f"Write down the equation of this line in standard form $y = mx + c$."
        ),
        "correct_answer": eq,
        "marking_schema": [
            f"Substitute m and c: {eq} (1 mark)",
        ],
        "hints": [
            "Use the standard gradient-intercept form: $y = mx + c$.",
            f"Substitute $m = {m}$ and $c = {c}$.",
            f"Equation: ${eq}$.",
        ],
        "misconception_tags": ["linear_equation_variable_placement_error"],
        "diagram_spec": None,
    }


def arch_25_reading_gradient_and_intercept_from_cartesian_diagram(rng: random.Random) -> Dict[str, Any]:
    m = rng.choice([1, 2, -1])
    c = rng.choice([-2, 0, 1, 2])
    seed_val = rng.randint(1, 1000000)

    svg = draw_cartesian_plane_svg(
        line_func=(float(m), float(c), "Line L"),
        x_range=(-5, 5),
        y_range=(-5, 5),
        title="Graph of Straight Line",
        seed=seed_val,
    )

    sign = "+" if c >= 0 else "-"
    abs_c = abs(c)

    return {
        "title": "Reading Equation from a Line Graph",
        "topic": "Graphs",
        "grade": 8,
        "term": 1,
        "subskill": "25_reading_gradient_and_intercept_from_cartesian_diagram",
        "difficulty": "hard",
        "question_text": (
            "Refer to the straight-line graph shown on the Cartesian grid below.\n\n"
            "Determine the equation of the line in the form $y = mx + c$."
        ),
        "correct_answer": f"y = {m}x {sign} {abs_c}" if c != 0 else f"y = {m}x",
        "marking_schema": [
            f"Read y-intercept (0; {c}) [1M]",
            f"Calculate rise/run m = {m} and write equation [1A]",
        ],
        "hints": [
            f"First find where the line crosses the y-axis: $c = {c}$.",
            f"Find the gradient by picking two points and dividing rise by run: $m = {m}$.",
            f"Equation: $y = {m}x {sign} {abs_c}$.",
        ],
        "misconception_tags": ["reading_graph_rise_run_scale_error"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


BUILDERS_01_25 = [
    arch_01_identifying_quadrant_from_coordinates,
    arch_02_identifying_points_on_axes,
    arch_03_reading_coordinates_from_cartesian_plane_diagram,
    arch_04_identifying_letter_for_given_coordinate_pair,
    arch_05_plotting_reflection_in_x_axis,
    arch_06_plotting_reflection_in_y_axis,
    arch_07_identifying_independent_and_dependent_variables,
    arch_08_discrete_vs_continuous_data_identification,
    arch_09_reading_distance_between_points_on_same_horizontal_line,
    arch_10_reading_distance_between_points_on_same_vertical_line,
    arch_11_midpoint_of_horizontal_or_vertical_segment,
    arch_12_cartesian_coordinates_collinear_points,
    arch_13_completing_table_of_values_for_linear_graph,
    arch_14_matching_table_of_values_to_correct_linear_equation,
    arch_15_identifying_quadrant_signs_rule,
    arch_16_calculating_gradient_from_two_positive_points,
    arch_17_calculating_gradient_with_negative_coordinates,
    arch_18_calculating_negative_gradient_from_coordinates,
    arch_19_gradient_of_horizontal_line_zero,
    arch_20_gradient_of_vertical_line_undefined,
    arch_21_reading_gradient_directly_from_y_equals_mx_plus_c,
    arch_22_reading_y_intercept_from_equation,
    arch_23_finding_x_intercept_of_linear_graph,
    arch_24_writing_equation_from_gradient_and_y_intercept,
    arch_25_reading_gradient_and_intercept_from_cartesian_diagram,
]
