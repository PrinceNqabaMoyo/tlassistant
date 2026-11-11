"""Grade 9 Mathematics - Graphs & Linear Functions Archetypes 01 to 25
====================================================================
Grounded strictly in:
  - CAPS Grade 9 Mathematics: Term 2 Topic: Graphs & Linear Functions
  - curriculum_docs_auto/Mathematics_Gr9/Term 2/02. Graphs.md
  - Chapter 15: Interpreting graphs, rate of change, gradient m, intercepts, y = mx + c

Covers Archetypes 01 - 25:
  01: Linear vs non-linear graph classification
  02: Increasing, decreasing, and constant intervals
  03: Reading coordinates from Cartesian plane
  04: Determining quadrant of a coordinate point
  05: Distinguishing discrete vs continuous graphs
  06: Interpreting maximum / turning points in context
  07: Distance-time graph constant speed & stationary intervals
  08: Calculating positive integer gradient from points
  09: Calculating negative integer gradient from points
  10: Calculating fractional gradient from points
  11: Calculating gradient from graph slope triangle (rise / run)
  12: Determining gradient of horizontal line (m = 0)
  13: Determining gradient of vertical line (undefined)
  14: Comparing steepness of two straight lines
  15: Finding y-intercept from linear equation
  16: Finding x-intercept by setting y = 0
  17: Reading x and y intercepts from plotted graph
  18: Dual-intercept method calculation & sketch matching
  19: Deriving line equation from both intercepts
  20: Converting general form ax + by = c to standard y = mx + c
  21: Equation of straight line given gradient m and y-intercept c
  22: Finding equation given positive gradient m and point (x1, y1)
  23: Finding equation given negative gradient m and point (x1, y1)
  24: Horizontal line equation y = k through point
  25: Vertical line equation x = k through point
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional

from app.utils.grade9_mathematics.graphs_svg import (
    draw_cartesian_plane_svg,
    draw_dual_intercept_svg,
    draw_slope_triangle_svg,
    draw_rate_context_graph_svg,
)


def arch_01_identify_linear_vs_non_linear_from_graph(rng: random.Random) -> Dict[str, Any]:
    """Classify graph as linear (constant rate) vs non-linear (changing rate)."""
    is_linear = rng.choice([True, False])
    seed_val = rng.randint(1000, 999999)

    if is_linear:
        m = rng.choice([-2, -1, 1, 2, 3])
        c = rng.choice([-2, -1, 0, 1, 2])
        lines = [{"m": m, "c": c, "color": "#38bdf8", "stroke_width": 2.5, "label": "Graph G"}]
        svg = draw_cartesian_plane_svg(lines=lines, title="Function Graph G", seed=seed_val)
        ans = "linear"
        reason = "the graph forms a single straight line with a constant rate of change (constant gradient)"
        other = "non-linear"
    else:
        # Approximate parabola or cubic points
        pts = [(-3, 5), (-2, 0), (-1, -3), (0, -4), (1, -3), (2, 0), (3, 5)]
        lines = []
        for i in range(len(pts) - 1):
            lines.append({"p1": pts[i], "p2": pts[i + 1], "color": "#f43f5e", "stroke_width": 2.5})
        svg = draw_cartesian_plane_svg(lines=lines, title="Function Graph G", seed=seed_val)
        ans = "non-linear"
        reason = "the graph is curved and the rate of change is not constant"
        other = "linear"

    prompt = (
        f"Examine the graph **Graph G** shown on the Cartesian plane below:\n\n"
        f"Classify whether the graph represents a **linear** or **non-linear** relationship."
    )

    return {
        "subskill": "01_identify_linear_vs_non_linear_from_graph",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": ans,
        "sample_answer": ans,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Identify that {reason}", "marks": 1},
            {"step": f"Conclude relationship is {ans}", "marks": 1},
        ],
        "hints": [
            "A linear graph has a constant rate of change and forms a perfectly straight line.",
            "A non-linear graph has a changing rate of change and curves.",
            f"Graph G is {ans} because {reason}.",
        ],
        "misconception_tags": ["linear_vs_nonlinear_confusion", "graph_curvature_interpretation"],
    }


def arch_02_identify_increasing_decreasing_constant_intervals(rng: random.Random) -> Dict[str, Any]:
    """Identify whether a plotted line is increasing, decreasing, or constant."""
    trend = rng.choice(["increasing", "decreasing", "constant"])
    seed_val = rng.randint(1000, 999999)

    if trend == "increasing":
        m = rng.choice([1, 2, 3])
        c = rng.randint(-3, 2)
        lines = [{"m": m, "c": c, "color": "#10b981", "stroke_width": 2.5, "label": "Line L"}]
        explanation = "as x increases from left to right, y increases (positive gradient m > 0)"
    elif trend == "decreasing":
        m = rng.choice([-3, -2, -1])
        c = rng.randint(-2, 3)
        lines = [{"m": m, "c": c, "color": "#f43f5e", "stroke_width": 2.5, "label": "Line L"}]
        explanation = "as x increases from left to right, y decreases (negative gradient m < 0)"
    else:
        k = rng.choice([-3, -2, 1, 2, 3])
        lines = [{"is_horizontal": True, "y_val": k, "color": "#38bdf8", "stroke_width": 2.5, "label": f"y = {k}"}]
        explanation = "the output value y remains unchanged for all values of x (gradient m = 0)"

    svg = draw_cartesian_plane_svg(lines=lines, title="Straight Line L", seed=seed_val)

    prompt = (
        f"Observe **Line L** on the Cartesian plane below.\n\n"
        f"State whether the line is **increasing**, **decreasing**, or **constant** from left to right."
    )

    return {
        "subskill": "02_identify_increasing_decreasing_constant_intervals",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": trend,
        "sample_answer": trend,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Observe slope direction from left to right: {explanation}", "marks": 1},
            {"step": f"Conclude line is {trend}", "marks": 1},
        ],
        "hints": [
            "Read the graph from left to right as $x$ increases.",
            "If the line slants upwards $/$, it is increasing. If downwards $\\$, it is decreasing. If horizontal $-$, it is constant.",
            f"Line L is {trend}.",
        ],
        "misconception_tags": ["graph_direction_confusion", "increasing_decreasing_misidentification"],
    }


def arch_03_read_coordinates_from_cartesian_plane(rng: random.Random) -> Dict[str, Any]:
    """Read coordinate landmark (x; y) plotted on a Cartesian plane."""
    x = rng.choice([-4, -3, -2, -1, 1, 2, 3, 4])
    y = rng.choice([-4, -3, -2, -1, 1, 2, 3, 4])
    seed_val = rng.randint(1000, 999999)

    points = [
        {"x": x, "y": y, "label": "P", "color": "#fbbf24", "fill": "#fbbf24", "highlight": True, "offset_x": 10, "offset_y": -10}
    ]
    svg = draw_cartesian_plane_svg(points=points, title="Point P on Cartesian Plane", seed=seed_val)

    ans_str = f"({x}; {y})"
    prompt = (
        f"Point **P** is plotted on the Cartesian plane below.\n\n"
        f"Write down the coordinates of point **P** in standard South African notation $(x;\\ y)$."
    )

    return {
        "subskill": "03_read_coordinates_from_cartesian_plane",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": ans_str,
        "sample_answer": ans_str,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Read x-coordinate on horizontal axis: x = {x}", "marks": 1},
            {"step": f"Read y-coordinate on vertical axis: y = {y}", "marks": 1},
            {"step": f"Write coordinate pair P({x}; {y})", "marks": 1},
        ],
        "hints": [
            "Always state the horizontal $x$-value first, followed by the vertical $y$-value.",
            f"Follow the vertical line down/up to the x-axis to get $x = {x}$, and horizontally to the y-axis to get $y = {y}$.",
            f"Coordinates: $P({x};\\ {y})$.",
        ],
        "misconception_tags": ["reversed_coordinates_yx", "cartesian_sign_error"],
    }


def arch_04_determine_quadrant_of_point(rng: random.Random) -> Dict[str, Any]:
    """Determine which quadrant (I, II, III, IV) a coordinate point lies in."""
    q_num = rng.choice([1, 2, 3, 4])
    if q_num == 1:
        x, y = rng.randint(1, 5), rng.randint(1, 5)
        quad_str = "Quadrant I"
    elif q_num == 2:
        x, y = rng.randint(-5, -1), rng.randint(1, 5)
        quad_str = "Quadrant II"
    elif q_num == 3:
        x, y = rng.randint(-5, -1), rng.randint(-5, -1)
        quad_str = "Quadrant III"
    else:
        x, y = rng.randint(1, 5), rng.randint(-5, -1)
        quad_str = "Quadrant IV"

    seed_val = rng.randint(1000, 999999)
    points = [{"x": x, "y": y, "label": f"({x}; {y})", "color": "#38bdf8", "fill": "#38bdf8", "highlight": True}]
    svg = draw_cartesian_plane_svg(points=points, title=f"Location of Point ({x}; {y})", seed=seed_val)

    prompt = (
        f"Consider the point **$({x};\\ {y})$** shown on the Cartesian plane.\n\n"
        f"In which quadrant does this point lie? (State: **Quadrant I**, **Quadrant II**, **Quadrant III**, or **Quadrant IV**)."
    )

    return {
        "subskill": "04_determine_quadrant_of_point",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": quad_str,
        "sample_answer": quad_str,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Inspect signs: x = {x} ({'positive' if x>0 else 'negative'}), y = {y} ({'positive' if y>0 else 'negative'})", "marks": 1},
            {"step": f"Identify quadrant as {quad_str}", "marks": 1},
        ],
        "hints": [
            "Quadrant I is top-right (+, +). Quadrant II is top-left (-, +).",
            "Quadrant III is bottom-left (-, -). Quadrant IV is bottom-right (+, -).",
            f"The point $({x};\\ {y})$ lies in {quad_str}.",
        ],
        "misconception_tags": ["quadrant_numbering_confusion", "clockwise_quadrant_error"],
    }


def arch_05_distinguish_discrete_vs_continuous_graph(rng: random.Random) -> Dict[str, Any]:
    """Identify whether a real-world scenario produces a discrete or continuous graph."""
    scenarios = [
        {
            "desc": "The number of soccer match tickets sold ($x$) and total gate income in rands ($y$).",
            "ans": "discrete",
            "reason": "tickets can only be purchased in whole numbers (you cannot buy 2,5 tickets); the data points are separate and isolated",
        },
        {
            "desc": "The depth of water in metres ($y$) inside a swimming pool measured continuously over hours ($x$).",
            "ans": "continuous",
            "reason": "both time and water depth can take any fractional value along an unbroken range; represented by an unbroken curve or line",
        },
        {
            "desc": "The number of learners in a class ($x$) and the number of textbooks issued ($y$).",
            "ans": "discrete",
            "reason": "learners and textbooks can only exist as whole countable entities",
        },
        {
            "desc": "The temperature in degrees Celsius ($y$) of an oven recorded every minute ($x$).",
            "ans": "continuous",
            "reason": "temperature and time change continuously and take every intermediate real value",
        },
    ]
    sc = rng.choice(scenarios)

    prompt = (
        f"Consider the following real-world relationship:\n"
        f"**\"{sc['desc']}\"**\n\n"
        f"Is the graph of this relationship **discrete** or **continuous**?"
    )

    return {
        "subskill": "05_distinguish_discrete_vs_continuous_graph",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": sc["ans"],
        "sample_answer": sc["ans"],
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Analyse variable measurability: {sc['reason']}", "marks": 1},
            {"step": f"Classify as {sc['ans']}", "marks": 1},
        ],
        "hints": [
            "Discrete data consists of separate, distinct values (usually whole counting numbers) plotted as individual dots.",
            "Continuous data can take any real value on an interval (like time, temperature, mass, distance) connected by an unbroken line.",
            f"This relationship is {sc['ans']}.",
        ],
        "misconception_tags": ["discrete_continuous_confusion", "measurement_scale_misunderstanding"],
    }


def arch_06_interpret_maximum_minimum_turning_points_context(rng: random.Random) -> Dict[str, Any]:
    """Read peak or maximum value from a contextual graph."""
    max_t = rng.choice([13, 14, 15, 16])
    max_temp = rng.choice([28, 30, 32, 34])
    seed_val = rng.randint(1000, 999999)

    # 5 key points: 06:00 (14), 10:00 (22), max_t (max_temp), 18:00 (24), 22:00 (16)
    pts = [(6, 14), (10, 22), (max_t, max_temp), (18, 24), (22, 16)]
    segments = [{"points": pts, "color": "#f97316", "label": "Temp (°C)"}]
    svg = draw_rate_context_graph_svg(
        segments=segments,
        x_label="Time of Day (hours)",
        y_label="Temperature (°C)",
        title="Daily Ambient Temperature in Polokwane",
        x_max=24,
        y_max=40,
        seed=seed_val,
    )

    prompt = (
        f"The graph below illustrates the ambient temperature in Polokwane over a 24-hour cycle.\n\n"
        f"What was the **maximum temperature** recorded during the day, in degrees Celsius (°C)?"
    )

    return {
        "subskill": "06_interpret_maximum_minimum_turning_points_context",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": str(max_temp),
        "sample_answer": f"{max_temp} °C",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Locate the highest peak (turning point) on the temperature graph", "marks": 1},
            {"step": f"Read vertical value on y-axis: {max_temp} °C", "marks": 1},
        ],
        "hints": [
            "Find the highest point (crest/peak) of the curve.",
            "Look across horizontally to the vertical axis (Temperature in °C) to read the value.",
            f"The maximum temperature is {max_temp} °C.",
        ],
        "misconception_tags": ["peak_reading_error", "axis_swapping_error"],
    }


def arch_07_interpret_constant_speed_from_distance_time_graph(rng: random.Random) -> Dict[str, Any]:
    """Interpret horizontal flat segment (stationary/stopped) on a distance-time graph."""
    t_stop_start = rng.choice([2, 3])
    duration = rng.choice([1, 2, 3])
    t_stop_end = t_stop_start + duration
    dist_at_stop = rng.choice([80, 100, 120])
    final_dist = dist_at_stop + 60
    final_t = t_stop_end + 2
    seed_val = rng.randint(1000, 999999)

    pts = [(0, 0), (t_stop_start, dist_at_stop), (t_stop_end, dist_at_stop), (final_t, final_dist)]
    segments = [{"points": pts, "color": "#38bdf8", "label": "Journey"}]
    svg = draw_rate_context_graph_svg(
        segments=segments,
        x_label="Time (hours)",
        y_label="Distance from Home (km)",
        title="Car Journey with Rest Stop",
        x_max=10,
        y_max=200,
        seed=seed_val,
    )

    prompt = (
        f"The distance-time graph below represents a car journey.\n\n"
        f"For how many hours was the vehicle **stationary (stopped)** at the rest stop?"
    )

    return {
        "subskill": "07_interpret_constant_speed_from_distance_time_graph",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": str(duration),
        "sample_answer": f"{duration} hours",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Identify horizontal segment where distance does not change: from t = {t_stop_start} to t = {t_stop_end}", "marks": 1},
            {"step": f"Calculate duration: {t_stop_end} - {t_stop_start} = {duration} hours", "marks": 1},
        ],
        "hints": [
            "A horizontal flat line on a distance-time graph indicates zero change in distance (speed = 0 km/h, vehicle is stopped).",
            f"The flat segment starts at $t = {t_stop_start}$ and ends at $t = {t_stop_end}$.",
            f"Duration stopped = ${t_stop_end} - {t_stop_start} = {duration}$ hours.",
        ],
        "misconception_tags": ["distance_time_flat_segment_confusion", "rate_interpretation_error"],
    }


def arch_08_calculate_gradient_positive_integer_from_points(rng: random.Random) -> Dict[str, Any]:
    """Calculate gradient m = (y2 - y1) / (x2 - x1) with positive integer result."""
    m = rng.choice([1, 2, 3, 4])
    x1 = rng.randint(-3, 1)
    dx = rng.choice([1, 2, 3])
    x2 = x1 + dx
    c = rng.randint(-3, 3)
    y1 = m * x1 + c
    y2 = m * x2 + c

    seed_val = rng.randint(1000, 999999)
    svg = draw_slope_triangle_svg((x1, y1), (x2, y2), line_label=f"Line AB", seed=seed_val)

    prompt = (
        f"Calculate the **gradient ($m$)** of the straight line passing through points "
        f"**$A({x1};\\ {y1})$** and **$B({x2};\\ {y2})$**."
    )

    return {
        "subskill": "08_calculate_gradient_positive_integer_from_points",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": str(m),
        "sample_answer": str(m),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "State gradient formula: m = (y2 - y1) / (x2 - x1)", "marks": 1},
            {"step": f"Substitute coordinates: m = ({y2} - ({y1})) / ({x2} - ({x1})) = {y2 - y1} / {x2 - x1}", "marks": 1},
            {"step": f"Simplify to obtain m = {m}", "marks": 1},
        ],
        "hints": [
            "Use the standard gradient formula: $m = \\frac{y_2 - y_1}{x_2 - x_1}$.",
            f"Substitute: $m = \\frac{{{y2} - ({y1})}}{{{x2} - ({x1})}} = \\frac{{{y2 - y1}}}{{{x2 - x1}}}$.",
            f"Gradient $m = {m}$.",
        ],
        "misconception_tags": ["gradient_formula_inverted", "subtraction_sign_error"],
    }


def arch_09_calculate_gradient_negative_integer_from_points(rng: random.Random) -> Dict[str, Any]:
    """Calculate gradient m = (y2 - y1) / (x2 - x1) with negative integer result."""
    m = rng.choice([-3, -2, -1])
    x1 = rng.randint(-4, 0)
    dx = rng.choice([1, 2, 3])
    x2 = x1 + dx
    c = rng.randint(-2, 3)
    y1 = m * x1 + c
    y2 = m * x2 + c

    seed_val = rng.randint(1000, 999999)
    svg = draw_slope_triangle_svg((x1, y1), (x2, y2), line_label="Line AB", seed=seed_val)

    prompt = (
        f"Determine the **gradient ($m$)** of the line passing through points "
        f"**$A({x1};\\ {y1})$** and **$B({x2};\\ {y2})$**."
    )

    return {
        "subskill": "09_calculate_gradient_negative_integer_from_points",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": str(m),
        "sample_answer": str(m),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "State gradient formula: m = (y2 - y1) / (x2 - x1)", "marks": 1},
            {"step": f"Substitute: m = ({y2} - ({y1})) / ({x2} - ({x1})) = {y2 - y1} / {x2 - x1}", "marks": 1},
            {"step": f"Simplify: m = {m}", "marks": 1},
        ],
        "hints": [
            "Formula: $m = \\frac{y_2 - y_1}{x_2 - x_1}$.",
            f"Substitute: $m = \\frac{{{y2} - ({y1})}}{{{x2} - ({x1})}} = \\frac{{{y2 - y1}}}{{{x2 - x1}}}$.",
            f"Notice the line slopes downwards; $m = {m}$.",
        ],
        "misconception_tags": ["negative_gradient_lost_sign", "subtraction_with_negatives_error"],
    }


def arch_10_calculate_gradient_fractional_slope_from_points(rng: random.Random) -> Dict[str, Any]:
    """Calculate simplified fractional gradient from coordinates."""
    frac_options = [
        (1, 2, "1/2"),
        (-1, 2, "-1/2"),
        (2, 3, "2/3"),
        (-2, 3, "-2/3"),
        (3, 4, "3/4"),
        (-3, 4, "-3/4"),
    ]
    num, den, ans_str = rng.choice(frac_options)
    x1 = rng.randint(-3, 0)
    x2 = x1 + den
    y1 = rng.randint(-3, 2)
    y2 = y1 + num

    seed_val = rng.randint(1000, 999999)
    svg = draw_slope_triangle_svg((x1, y1), (x2, y2), line_label=f"m = {ans_str}", seed=seed_val)

    prompt = (
        f"Calculate the **gradient ($m$)** of the straight line passing through "
        f"**$A({x1};\\ {y1})$** and **$B({x2};\\ {y2})$**.\n\n"
        f"Give your answer as a simplified common fraction (e.g. `1/2` or `-2/3`)."
    )

    return {
        "subskill": "10_calculate_gradient_fractional_slope_from_points",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": ans_str,
        "sample_answer": ans_str,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "State formula: m = (y2 - y1) / (x2 - x1)", "marks": 1},
            {"step": f"Substitute: m = ({y2} - {y1}) / ({x2} - {x1}) = {num} / {den}", "marks": 1},
            {"step": f"Express as simplified fraction: m = {ans_str}", "marks": 1},
        ],
        "hints": [
            "Use $m = \\frac{\\text{vertical change}}{\\text{horizontal change}} = \\frac{y_2 - y_1}{x_2 - x_1}$.",
            f"Numerator: ${y2} - ({y1}) = {num}$. Denominator: ${x2} - ({x1}) = {den}$.",
            f"Gradient $m = {ans_str}$.",
        ],
        "misconception_tags": ["fractional_gradient_inversion", "fraction_simplification_error"],
    }


def arch_11_calculate_gradient_from_graph_slope_triangle(rng: random.Random) -> Dict[str, Any]:
    """Calculate gradient from shaded rise/run triangle on Cartesian grid."""
    run = rng.choice([2, 3, 4])
    rise = rng.choice([2, 4, 6, 8])
    m = rise // run if rise % run == 0 else 2
    actual_rise = m * run

    x1 = rng.randint(-3, 0)
    y1 = rng.randint(-3, 0)
    x2 = x1 + run
    y2 = y1 + actual_rise

    seed_val = rng.randint(1000, 999999)
    svg = draw_slope_triangle_svg((x1, y1), (x2, y2), line_label="Line L", seed=seed_val)

    prompt = (
        f"Refer to the slope triangle constructed on **Line L** in the diagram below:\n\n"
        f"Using the vertical change ($\\Delta y = {actual_rise}$) and horizontal change ($\\Delta x = {run}$), "
        f"calculate the **gradient ($m$)** of the line."
    )

    return {
        "subskill": "11_calculate_gradient_from_graph_slope_triangle",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": str(m),
        "sample_answer": str(m),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "State gradient definition: m = rise / run = Δy / Δx", "marks": 1},
            {"step": f"Substitute values: m = {actual_rise} / {run} = {m}", "marks": 1},
        ],
        "hints": [
            "Gradient is the ratio of vertical change (rise) to horizontal change (run).",
            f"Calculate $m = \\frac{{\\text{{rise}}}}{{\\text{{run}}}} = \\frac{{{actual_rise}}}{{{run}}}$.",
            f"Gradient $m = {m}$.",
        ],
        "misconception_tags": ["run_over_rise_inversion", "slope_triangle_ratio_error"],
    }


def arch_12_determine_gradient_horizontal_line_zero(rng: random.Random) -> Dict[str, Any]:
    """Identify that a horizontal line y = k has gradient m = 0."""
    k = rng.choice([-4, -3, -2, 2, 3, 4])
    seed_val = rng.randint(1000, 999999)

    lines = [{"is_horizontal": True, "y_val": k, "color": "#38bdf8", "stroke_width": 2.5, "label": f"y = {k}"}]
    svg = draw_cartesian_plane_svg(lines=lines, title=f"Horizontal Line y = {k}", seed=seed_val)

    prompt = (
        f"The horizontal straight line **$y = {k}$** is plotted below.\n\n"
        f"What is the **gradient ($m$)** of this horizontal line?"
    )

    return {
        "subskill": "12_determine_gradient_horizontal_line_zero",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": "0",
        "sample_answer": "0",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Observe that vertical change Δy = y2 - y1 = 0", "marks": 1},
            {"step": "Conclude gradient m = 0 / Δx = 0", "marks": 1},
        ],
        "hints": [
            "For any two points on a horizontal line, the $y$-coordinates are equal, so $y_2 - y_1 = 0$.",
            "Dividing zero by any non-zero run gives zero: $m = \\frac{0}{\\Delta x} = 0$.",
            "The gradient of any horizontal line is **0**.",
        ],
        "misconception_tags": ["horizontal_gradient_undefined_confusion", "zero_gradient_misunderstanding"],
    }


def arch_13_determine_gradient_vertical_line_undefined(rng: random.Random) -> Dict[str, Any]:
    """Identify that a vertical line x = k has undefined gradient."""
    k = rng.choice([-4, -3, -2, 2, 3, 4])
    seed_val = rng.randint(1000, 999999)

    lines = [{"is_vertical": True, "x_val": k, "color": "#f43f5e", "stroke_width": 2.5, "label": f"x = {k}"}]
    svg = draw_cartesian_plane_svg(lines=lines, title=f"Vertical Line x = {k}", seed=seed_val)

    prompt = (
        f"The vertical straight line **$x = {k}$** is plotted on the Cartesian plane below.\n\n"
        f"State the **gradient ($m$)** of this vertical line (write **undefined**)."
    )

    return {
        "subskill": "13_determine_gradient_vertical_line_undefined",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": "undefined",
        "sample_answer": "undefined",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Observe horizontal change Δx = x2 - x1 = 0", "marks": 1},
            {"step": "Division by zero is undefined in mathematics, so gradient is undefined", "marks": 1},
        ],
        "hints": [
            "On a vertical line, all points have the same $x$-coordinate, so $\\Delta x = 0$.",
            "Calculating gradient requires division by horizontal run: $m = \\frac{\\Delta y}{0}$, which is undefined.",
            "The gradient of any vertical line is **undefined**.",
        ],
        "misconception_tags": ["vertical_gradient_zero_confusion", "division_by_zero_concept"],
    }


def arch_14_compare_steepness_of_two_lines(rng: random.Random) -> Dict[str, Any]:
    """Compare steepness (|m1| vs |m2|) of two plotted straight lines."""
    m1 = rng.choice([1, 2])
    m2 = rng.choice([3, 4, 5])
    # Randomly assign which is Line 1 and Line 2
    if rng.random() > 0.5:
        line1_m, line2_m = m1, m2
        steeper = "Line 2"
    else:
        line1_m, line2_m = m2, m1
        steeper = "Line 1"

    seed_val = rng.randint(1000, 999999)
    lines = [
        {"m": line1_m, "c": 0, "color": "#38bdf8", "stroke_width": 2.5, "label": "Line 1"},
        {"m": line2_m, "c": 0, "color": "#ec4899", "stroke_width": 2.5, "label": "Line 2"},
    ]
    svg = draw_cartesian_plane_svg(lines=lines, title="Comparing Steepness of Two Lines", seed=seed_val)

    prompt = (
        f"Two straight lines passing through the origin are plotted below:\n"
        f"- **Line 1:** Gradient $m_1 = {line1_m}$\n"
        f"- **Line 2:** Gradient $m_2 = {line2_m}$\n\n"
        f"Which line is **steeper**? (Answer: **Line 1** or **Line 2**)."
    )

    return {
        "subskill": "14_compare_steepness_of_two_lines",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": steeper,
        "sample_answer": steeper,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Compare absolute values of gradients: |m1| = {abs(line1_m)} vs |m2| = {abs(line2_m)}", "marks": 1},
            {"step": f"Conclude {steeper} is steeper because it has a greater rate of change", "marks": 1},
        ],
        "hints": [
            "Steepness is determined by the magnitude (absolute value) of the gradient.",
            f"Here, $|{line1_m}| = {abs(line1_m)}$ and $|{line2_m}| = {abs(line2_m)}$.",
            f"The line with the larger gradient magnitude is {steeper}.",
        ],
        "misconception_tags": ["steepness_vs_gradient_confusion", "gradient_magnitude_comparison"],
    }


def arch_15_find_y_intercept_from_equation(rng: random.Random) -> Dict[str, Any]:
    """Find y-intercept value c from equation y = mx + c."""
    m = rng.choice([-4, -3, -2, 2, 3, 4])
    c = rng.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])
    op = "+" if c > 0 else "-"

    prompt = (
        f"A straight line has the equation:\n"
        f"$$y = {m}x {op} {abs(c)}$$\n\n"
        f"Determine the **$y$-intercept** of this line (state the numerical value of $c$)."
    )

    return {
        "subskill": "15_find_y_intercept_from_equation",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": str(c),
        "sample_answer": str(c),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Identify that the standard equation of a straight line is y = mx + c", "marks": 1},
            {"step": f"At the y-intercept, x = 0, so y = {m}(0) + ({c}) = {c}", "marks": 1},
        ],
        "hints": [
            "In standard form $y = mx + c$, $m$ is the gradient and $c$ is the $y$-intercept.",
            "Alternatively, set $x = 0$ in the equation and calculate $y$.",
            f"The $y$-intercept is $c = {c}$ (coordinates $(0;\\ {c})$).",
        ],
        "misconception_tags": ["y_intercept_sign_confusion", "swapping_m_and_c"],
    }


def arch_16_find_x_intercept_from_equation(rng: random.Random) -> Dict[str, Any]:
    """Determine x-intercept by setting y = 0 and solving for x."""
    m = rng.choice([-3, -2, 2, 3])
    x_int = rng.choice([-5, -4, -3, -2, 2, 3, 4, 5])
    # 0 = m * x_int + c => c = -m * x_int
    c = -m * x_int
    op = "+" if c > 0 else "-"

    prompt = (
        f"Consider the linear function:\n"
        f"$$y = {m}x {op} {abs(c)}$$\n\n"
        f"Calculate the **$x$-intercept** of the graph (state the numerical value of $x$)."
    )

    return {
        "subskill": "16_find_x_intercept_from_equation",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": str(x_int),
        "sample_answer": str(x_int),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Set y = 0 to find x-intercept: 0 = mx + c", "marks": 1},
            {"step": f"Substitute: 0 = {m}x {op} {abs(c)} => {m}x = {-c}", "marks": 1},
            {"step": f"Solve for x: x = {-c} / {m} = {x_int}", "marks": 1},
        ],
        "hints": [
            "At the $x$-intercept, the graph crosses the horizontal axis where $y = 0$.",
            f"Substitute $y = 0$: $0 = {m}x {op} {abs(c)}$.",
            f"Subtract or add ${abs(c)}$ and divide by ${m}$: $x = {x_int}$.",
        ],
        "misconception_tags": ["x_intercept_set_x_zero_error", "algebraic_transposition_error"],
    }


def arch_17_read_x_and_y_intercepts_from_graph(rng: random.Random) -> Dict[str, Any]:
    """Read coordinate pairs of intercepts from a plotted Cartesian graph."""
    x_int = rng.choice([-4, -3, -2, 2, 3, 4])
    y_int = rng.choice([-4, -3, -2, 2, 3, 4])
    seed_val = rng.randint(1000, 999999)

    svg = draw_dual_intercept_svg(x_int=x_int, y_int=y_int, line_label="Line L", seed=seed_val)

    ask_which = rng.choice(["x-intercept", "y-intercept"])
    if ask_which == "x-intercept":
        ans = str(x_int)
        coord = f"({x_int}; 0)"
        axis = "x-axis"
    else:
        ans = str(y_int)
        coord = f"(0; {y_int})"
        axis = "y-axis"

    prompt = (
        f"Refer to **Line L** plotted on the Cartesian plane below:\n\n"
        f"Read off the value of the **{ask_which}** where the line cuts the {axis}."
    )

    return {
        "subskill": "17_read_x_and_y_intercepts_from_graph",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": ans,
        "sample_answer": ans,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Locate point where Line L cuts {axis}: {coord}", "marks": 1},
            {"step": f"State {ask_which} value: {ans}", "marks": 1},
        ],
        "hints": [
            f"The {ask_which} is the point where the line crosses the {axis}.",
            f"Looking at the graph, the line crosses at ${ans}$.",
            f"Answer: {ans}.",
        ],
        "misconception_tags": ["intercept_axis_confusion", "reading_wrong_intercept"],
    }


def arch_18_dual_intercept_method_sketch_matching(rng: random.Random) -> Dict[str, Any]:
    """Calculate both intercepts (x_int and y_int) and find their sum."""
    m = rng.choice([-2, 2])
    x_int = rng.choice([-3, -2, 2, 3])
    c = -m * x_int
    op = "+" if c > 0 else "-"
    sum_val = x_int + c

    prompt = (
        f"A straight line has the equation:\n"
        f"$$y = {m}x {op} {abs(c)}$$\n\n"
        f"1. Determine the $x$-intercept (where $y = 0$).\n"
        f"2. Determine the $y$-intercept (where $x = 0$).\n\n"
        f"Calculate the **sum of the $x$-intercept and the $y$-intercept** ($x_{{\\text{{int}}}} + y_{{\\text{{int}}}}$)."
    )

    return {
        "subskill": "18_dual_intercept_method_sketch_matching",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": str(sum_val),
        "sample_answer": str(sum_val),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Set y = 0: 0 = {m}x {op} {abs(c)} => x_int = {x_int}", "marks": 1},
            {"step": f"Set x = 0: y_int = {c}", "marks": 1},
            {"step": f"Calculate sum: {x_int} + ({c}) = {sum_val}", "marks": 1},
        ],
        "hints": [
            f"Find the $x$-intercept by setting $y = 0$: $x_{{\\text{{int}}}} = {x_int}$.",
            f"Find the $y$-intercept by setting $x = 0$: $y_{{\\text{{int}}}} = {c}$.",
            f"Sum = ${x_int} + ({c}) = {sum_val}$.",
        ],
        "misconception_tags": ["dual_intercept_substitution_error", "addition_of_integers_error"],
    }


def arch_19_dual_intercept_equation_from_both_intercepts(rng: random.Random) -> Dict[str, Any]:
    """Determine line gradient m from x-intercept and y-intercept."""
    x_int = rng.choice([-4, -3, -2, 2, 3, 4])
    m_val = rng.choice([-3, -2, -1, 1, 2, 3])
    # 0 = m_val * x_int + c => c = -m_val * x_int
    y_int = -m_val * x_int

    seed_val = rng.randint(1000, 999999)
    svg = draw_dual_intercept_svg(x_int=x_int, y_int=y_int, line_label="Line L", seed=seed_val)

    prompt = (
        f"A straight line cuts the axes at:\n"
        f"- $x$-intercept: **$({x_int};\\ 0)$**\n"
        f"- $y$-intercept: **$(0;\\ {y_int})$**\n\n"
        f"Calculate the **gradient ($m$)** of this straight line."
    )

    return {
        "subskill": "19_dual_intercept_equation_from_both_intercepts",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": str(m_val),
        "sample_answer": str(m_val),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "State gradient formula with intercepts: m = (y2 - y1) / (x2 - x1) = (y_int - 0) / (0 - x_int)", "marks": 1},
            {"step": f"Substitute: m = ({y_int} - 0) / (0 - ({x_int})) = {y_int} / {-x_int} = {m_val}", "marks": 1},
        ],
        "hints": [
            "Use the two points $(x_1; y_1) = ({x_int}; 0)$ and $(x_2; y_2) = (0; {y_int})$.",
            f"Gradient $m = \\frac{{{y_int} - 0}}{{0 - ({x_int})}} = \\frac{{{y_int}}}{{{-x_int}}}$.",
            f"Gradient $m = {m_val}$.",
        ],
        "misconception_tags": ["gradient_from_intercepts_sign_error", "intercept_ratio_inversion"],
    }


def arch_20_convert_general_form_to_standard_form(rng: random.Random) -> Dict[str, Any]:
    """Convert ax + by = c to standard form y = mx + c and identify gradient."""
    # 2x + y = 6 => y = -2x + 6 (m = -2)
    # -3x + y = 4 => y = 3x + 4 (m = 3)
    a = rng.choice([-3, -2, 2, 3])
    c = rng.randint(-6, 6)
    # Equation: ax + y = c => y = -ax + c, so gradient m = -a
    m = -a
    a_str = f"{a}x" if a != 1 else "x"
    if a == -1:
        a_str = "-x"

    prompt = (
        f"The equation of a straight line is given in general form:\n"
        f"$${a_str} + y = {c}$$\n\n"
        f"1. Make $y$ the subject of the formula to write the equation in standard form $y = mx + c$.\n"
        f"2. State the **gradient ($m$)** of the line."
    )

    return {
        "subskill": "20_convert_general_form_to_standard_form",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": str(m),
        "sample_answer": str(m),
        "tolerance": 0.0,
        "marking_schema": [
            {f"step": f"Transpose {a_str} to RHS: y = {-a}x + {c}", "marks": 1},
            {"step": f"Identify gradient m = {m}", "marks": 1},
        ],
        "hints": [
            "To isolate $y$, subtract the $x$-term from both sides.",
            f"Subtracting ${a_str}$ gives: $y = {-a}x + {c}$.",
            f"Comparing with $y = mx + c$, the gradient is $m = {m}$.",
        ],
        "misconception_tags": ["general_form_gradient_sign_error", "subject_of_formula_transposition"],
    }


def arch_21_equation_from_gradient_and_y_intercept(rng: random.Random) -> Dict[str, Any]:
    """Given gradient m and y-intercept c, evaluate y for a specific input x."""
    m = rng.choice([-3, -2, 2, 3])
    c = rng.choice([-4, -2, 1, 3, 5])
    x_eval = rng.choice([2, 3, 4])
    y_eval = m * x_eval + c
    op = "+" if c > 0 else "-"

    prompt = (
        f"A straight line has gradient **$m = {m}$** and $y$-intercept **$c = {c}$**.\n\n"
        f"1. Write down its equation in the form $y = mx + c$.\n"
        f"2. Determine the value of **$y$** when **$x = {x_eval}$**."
    )

    return {
        "subskill": "21_equation_from_gradient_and_y_intercept",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": str(y_eval),
        "sample_answer": str(y_eval),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Write equation: y = {m}x {op} {abs(c)}", "marks": 1},
            {"step": f"Substitute x = {x_eval}: y = {m}({x_eval}) {op} {abs(c)} = {m * x_eval} {op} {abs(c)} = {y_eval}", "marks": 1},
        ],
        "hints": [
            f"Substitute $m = {m}$ and $c = {c}$ into $y = mx + c$: $y = {m}x {op} {abs(c)}$.",
            f"Substitute $x = {x_eval}$: $y = {m}({x_eval}) + ({c})$.",
            f"Result: $y = {y_eval}$.",
        ],
        "misconception_tags": ["order_of_operations_linear_eval", "substitution_arithmetic_error"],
    }


def arch_22_equation_from_gradient_and_point_positive_m(rng: random.Random) -> Dict[str, Any]:
    """Find y-intercept c given gradient m > 0 and point (x1, y1)."""
    m = rng.choice([2, 3, 4])
    x1 = rng.randint(1, 4)
    c = rng.randint(-5, 5)
    y1 = m * x1 + c

    prompt = (
        f"A straight line with gradient **$m = {m}$** passes through the point **$A({x1};\\ {y1})$**.\n\n"
        f"Calculate the **$y$-intercept ($c$)** of this line."
    )

    return {
        "subskill": "22_equation_from_gradient_and_point_positive_m",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": str(c),
        "sample_answer": str(c),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "State standard equation: y = mx + c", "marks": 1},
            {"step": f"Substitute m = {m}, x = {x1}, y = {y1}: {y1} = {m}({x1}) + c", "marks": 1},
            {"step": f"Solve for c: c = {y1} - {m * x1} = {c}", "marks": 1},
        ],
        "hints": [
            "Use the equation $y = mx + c$ and substitute the known gradient and point coordinates.",
            f"${y1} = ({m})({x1}) + c \\implies {y1} = {m * x1} + c$.",
            f"Subtract ${m * x1}$ from ${y1}$: $c = {c}$.",
        ],
        "misconception_tags": ["point_substitution_swapped_xy", "algebraic_isolation_error"],
    }


def arch_23_equation_from_gradient_and_point_negative_m(rng: random.Random) -> Dict[str, Any]:
    """Find y-intercept c given negative gradient m < 0 and point (x1, y1)."""
    m = rng.choice([-3, -2, -1])
    x1 = rng.randint(-3, -1)
    c = rng.randint(-4, 4)
    y1 = m * x1 + c

    prompt = (
        f"A straight line has gradient **$m = {m}$** and passes through the point **$P({x1};\\ {y1})$**.\n\n"
        f"Determine the **$y$-intercept ($c$)** of the line."
    )

    return {
        "subskill": "23_equation_from_gradient_and_point_negative_m",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": str(c),
        "sample_answer": str(c),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Substitute into y = mx + c", "marks": 1},
            {"step": f"Substitute: {y1} = ({m})({x1}) + c => {y1} = {m * x1} + c", "marks": 1},
            {"step": f"Solve for c: c = {y1} - {m * x1} = {c}", "marks": 1},
        ],
        "hints": [
            "Substitute into $y = mx + c$: $y = {y1}$, $m = {m}$, $x = {x1}$.",
            f"${y1} = ({m})({x1}) + c \\implies {y1} = {m * x1} + c$.",
            f"$c = {y1} - ({m * x1}) = {c}$.",
        ],
        "misconception_tags": ["negative_product_sign_error", "subtraction_with_negatives"],
    }


def arch_24_horizontal_line_equation_through_point(rng: random.Random) -> Dict[str, Any]:
    """Horizontal line equation y = k passing through (x1, y1)."""
    x1 = rng.randint(-5, 5)
    y1 = rng.choice([-4, -3, -2, 1, 2, 3, 4])
    seed_val = rng.randint(1000, 999999)

    lines = [{"is_horizontal": True, "y_val": y1, "color": "#38bdf8", "stroke_width": 2.5, "label": f"y = {y1}"}]
    points = [{"x": x1, "y": y1, "label": f"P({x1}; {y1})", "color": "#fbbf24", "fill": "#fbbf24", "highlight": True}]
    svg = draw_cartesian_plane_svg(lines=lines, points=points, title=f"Horizontal Line Through P({x1}; {y1})", seed=seed_val)

    prompt = (
        f"A straight line is **horizontal** and passes through the point **$P({x1};\\ {y1})$**.\n\n"
        f"State the equation of this line in the form $y = k$ (state the value of $k$)."
    )

    return {
        "subskill": "24_horizontal_line_equation_through_point",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": str(y1),
        "sample_answer": f"y = {y1} (k = {y1})",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Recall that all points on a horizontal line share the same y-value", "marks": 1},
            {"step": f"The y-coordinate of P is {y1}, so the equation is y = {y1} (k = {y1})", "marks": 1},
        ],
        "hints": [
            "A horizontal line has zero gradient ($m = 0$), so $y = 0x + c \\implies y = c$.",
            f"Since it passes through $P({x1};\\ {y1})$, $y$ must always equal ${y1}$.",
            f"The equation is $y = {y1}$, so $k = {y1}$.",
        ],
        "misconception_tags": ["horizontal_equation_x_equals_k_confusion", "coordinate_component_swap"],
    }


def arch_25_vertical_line_equation_through_point(rng: random.Random) -> Dict[str, Any]:
    """Vertical line equation x = k passing through (x1, y1)."""
    x1 = rng.choice([-4, -3, -2, 1, 2, 3, 4])
    y1 = rng.randint(-5, 5)
    seed_val = rng.randint(1000, 999999)

    lines = [{"is_vertical": True, "x_val": x1, "color": "#f43f5e", "stroke_width": 2.5, "label": f"x = {x1}"}]
    points = [{"x": x1, "y": y1, "label": f"Q({x1}; {y1})", "color": "#fbbf24", "fill": "#fbbf24", "highlight": True}]
    svg = draw_cartesian_plane_svg(lines=lines, points=points, title=f"Vertical Line Through Q({x1}; {y1})", seed=seed_val)

    prompt = (
        f"A straight line is **vertical** and passes through the point **$Q({x1};\\ {y1})$**.\n\n"
        f"State the equation of this line in the form $x = k$ (state the value of $k$)."
    )

    return {
        "subskill": "25_vertical_line_equation_through_point",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": str(x1),
        "sample_answer": f"x = {x1} (k = {x1})",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Recall that all points on a vertical line share the same x-value", "marks": 1},
            {"step": f"The x-coordinate of Q is {x1}, so the equation is x = {x1} (k = {x1})", "marks": 1},
        ],
        "hints": [
            "A vertical line has undefined gradient and is parallel to the $y$-axis.",
            f"Every point on this vertical line has an $x$-coordinate of ${x1}$.",
            f"The equation is $x = {x1}$, so $k = {x1}$.",
        ],
        "misconception_tags": ["vertical_equation_y_equals_k_confusion", "coordinate_component_swap"],
    }
