"""
Grade 8 Mathematics - Graphs Archetypes (26 to 50).
100% CAPS-aligned deterministic question generators.
Adheres strictly to the 6-Pillar Generator Contract and Zero-Meta-Curriculum Invariant.
Grounded in curriculum_docs_auto/Mathematics_Gr8/Term 1/02. Graphs.md.
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional

from .svg_diagrams import draw_real_world_line_graph_svg


def arch_26_identifying_parallel_lines_equal_gradients(rng: random.Random) -> Dict[str, Any]:
    m = rng.choice([-3, -2, 2, 4, 5])
    c1 = rng.choice([1, 2, 3])
    c2 = c1 + rng.choice([2, 3, 4])
    is_parallel = rng.choice([True, False])

    if is_parallel:
        eq1 = f"y = {m}x + {c1}"
        eq2 = f"y = {m}x + {c2}"
        ans = "Yes"
        reason = f"both lines have identical gradient m = {m}"
    else:
        m2 = m + rng.choice([-1, 1])
        eq1 = f"y = {m}x + {c1}"
        eq2 = f"y = {m2}x + {c2}"
        ans = "No"
        reason = f"their gradients are different (m1 = {m} while m2 = {m2})"

    return {
        "title": "Parallel Lines and Gradients",
        "topic": "Graphs",
        "grade": 8,
        "term": 1,
        "subskill": "26_identifying_parallel_lines_equal_gradients",
        "difficulty": "medium",
        "question_text": (
            f"Consider the two straight-line equations:\n\n"
            f"$$\\text{{Line 1: }} {eq1} \\quad \\text{{and}} \\quad \\text{{Line 2: }} {eq2}$$\n\n"
            f"Are these two lines **parallel** to each other? Give a reason."
        ),
        "correct_answer": f"{ans}, because {reason}",
        "marking_schema": [
            f"Compare gradients and state {ans}: 2 marks",
        ],
        "hints": [
            "Two lines on a Cartesian plane are parallel if and only if their gradients are equal ($m_1 = m_2$).",
            f"Check the coefficient of x for each equation.",
            f"Answer: {ans} ({reason}).",
        ],
        "misconception_tags": ["parallel_lines_gradient_comparison_error"],
        "diagram_spec": None,
    }


def arch_27_determining_direction_of_line_from_gradient_sign(rng: random.Random) -> Dict[str, Any]:
    choice_type = rng.choice(["positive", "negative", "zero"])
    if choice_type == "positive":
        m = rng.choice([2, 3, 5])
        c = rng.randint(-4, 4)
        direction = "rises from left to right"
        ans = "rises"
    elif choice_type == "negative":
        m = -rng.choice([1, 2, 4])
        c = rng.randint(-4, 4)
        direction = "falls from left to right"
        ans = "falls"
    else:
        m = 0
        c = rng.choice([-3, 2, 5])
        direction = "is horizontal"
        ans = "horizontal"

    eq = f"y = {m}x + {c}" if m != 0 else f"y = {c}"

    return {
        "title": "Direction of Line from Gradient Sign",
        "topic": "Graphs",
        "grade": 8,
        "term": 1,
        "subskill": "27_determining_direction_of_line_from_gradient_sign",
        "difficulty": "easy",
        "question_text": (
            f"Consider the straight-line equation **${eq}$**.\n\n"
            f"State whether this line **rises**, **falls**, or is **horizontal** as you move from left to right."
        ),
        "correct_answer": ans,
        "marking_schema": [
            f"State line direction: '{ans}' (1 mark)",
        ],
        "hints": [
            "If m > 0, the line rises. If m < 0, the line falls. If m = 0, the line is horizontal.",
            f"Here the gradient is m = {m}.",
            f"The line {direction}.",
        ],
        "misconception_tags": ["gradient_sign_direction_confusion"],
        "diagram_spec": None,
    }


def arch_28_comparing_steepness_of_two_lines(rng: random.Random) -> Dict[str, Any]:
    m1 = rng.choice([2, 3])
    m2 = m1 + rng.choice([2, 3, 4])
    line_a = f"y = {m1}x + 1"
    line_b = f"y = {m2}x - 3"

    return {
        "title": "Comparing Steepness of Two Lines",
        "topic": "Graphs",
        "grade": 8,
        "term": 1,
        "subskill": "28_comparing_steepness_of_two_lines",
        "difficulty": "easy",
        "question_text": (
            f"Consider the two lines:\n\n"
            f"$$\\text{{Line A: }} {line_a} \\quad \\text{{and}} \\quad \\text{{Line B: }} {line_b}$$\n\n"
            f"Which line is **steeper**? Explain by comparing their gradients."
        ),
        "correct_answer": "Line B",
        "marking_schema": [
            f"Compare |{m2}| > |{m1}| and identify Line B: 1 mark",
        ],
        "hints": [
            "Steepness depends on the absolute value (magnitude) of the gradient $|m|$.",
            f"Line A has gradient {m1}, while Line B has gradient {m2}.",
            f"Since {m2} > {m1}, Line B is steeper.",
        ],
        "misconception_tags": ["steepness_intercept_influence_misconception"],
        "diagram_spec": None,
    }


def arch_29_finding_missing_coordinate_given_gradient(rng: random.Random) -> Dict[str, Any]:
    m = rng.choice([2, 3, 4])
    x1 = 1
    x2 = x1 + rng.choice([2, 3])
    y1 = rng.randint(2, 6)
    y2 = y1 + m * (x2 - x1)

    return {
        "title": "Finding Missing Coordinate Given Gradient",
        "topic": "Graphs",
        "grade": 8,
        "term": 1,
        "subskill": "29_finding_missing_coordinate_given_gradient",
        "difficulty": "hard",
        "question_text": (
            f"A straight line with gradient **$m = {m}$** passes through the points **$A({x1}; {y1})$** and **$B({x2}; y)$**.\n\n"
            f"Calculate the unknown coordinate **$y$**."
        ),
        "correct_answer": str(y2),
        "marking_schema": [
            f"Set up gradient formula: (y - {y1})/({x2} - {x1}) = {m} [1M]",
            f"Solve for y = {y2} [1A]",
        ],
        "hints": [
            f"Substitute into the gradient formula: $\\frac{{y - {y1}}}{{{x2} - {x1}}} = {m}$.",
            f"$\\frac{{y - {y1}}}{{{x2 - x1}}} = {m} \\implies y - {y1} = {m * (x2 - x1)}$.",
            f"$y = {y1} + {m * (x2 - x1)} = {y2}$.",
        ],
        "misconception_tags": ["algebraic_gradient_equation_solving_error"],
        "diagram_spec": None,
    }


def arch_30_point_lies_on_line_verification(rng: random.Random) -> Dict[str, Any]:
    m = rng.choice([2, 3, 4])
    c = rng.choice([-3, -1, 2, 5])
    x_test = rng.choice([2, 3, 4])
    sign = "+" if c >= 0 else "-"
    abs_c = abs(c)

    lies_on_line = rng.choice([True, False])
    if lies_on_line:
        y_test = m * x_test + c
        ans = "Yes"
        reason = f"{m}({x_test}) {sign} {abs_c} = {y_test}"
    else:
        y_test = m * x_test + c + rng.choice([-3, 3])
        ans = "No"
        reason = f"{m}({x_test}) {sign} {abs_c} = {m * x_test + c} != {y_test}"

    return {
        "title": "Verifying Point on a Straight Line",
        "topic": "Graphs",
        "grade": 8,
        "term": 1,
        "subskill": "30_point_lies_on_line_verification",
        "difficulty": "medium",
        "question_text": (
            f"Determine whether the point **$P({x_test}; {y_test})$** lies on the straight line **$y = {m}x {sign} {abs_c}$**."
        ),
        "correct_answer": ans,
        "marking_schema": [
            f"Substitute x = {x_test} into equation and verify: {ans} (2 marks)",
        ],
        "hints": [
            f"Substitute $x = {x_test}$ into the right-hand side of the equation.",
            f"${m}({x_test}) {sign} {abs_c} = {m * x_test + c}$.",
            f"Comparing with y = {y_test}: {ans} ({reason}).",
        ],
        "misconception_tags": ["point_line_substitution_arithmetic_slip"],
        "diagram_spec": None,
    }


def arch_31_distance_time_graph_reading_distance_at_time(rng: random.Random) -> Dict[str, Any]:
    t1 = rng.choice([1, 2, 3])
    speed = rng.choice([40, 50, 60])
    d1 = t1 * speed
    waypoints = [
        (0.0, 0.0, "O"),
        (float(t1), float(d1), "A"),
        (float(t1 + 1), float(d1), "B"),
        (float(t1 + 3), float(d1 + 80), "C"),
    ]

    seed_val = rng.randint(1, 1000000)
    svg = draw_real_world_line_graph_svg(
        waypoints=waypoints,
        x_label="Time (hours)",
        y_label="Distance (km)",
        max_x=6.0,
        max_y=240.0,
        title="Cyclist Journey Graph",
        seed=seed_val,
    )

    return {
        "title": "Reading Distance from Distance-Time Graph",
        "topic": "Graphs",
        "grade": 8,
        "term": 1,
        "subskill": "31_distance_time_graph_reading_distance_at_time",
        "difficulty": "medium",
        "question_text": (
            "Refer to the distance-time graph below representing a cyclist's journey.\n\n"
            f"Determine the distance covered by the cyclist at **$t = {t1}\\text{{ hours}}$**."
        ),
        "correct_answer": f"{d1} km",
        "marking_schema": [
            f"Read vertical coordinate at t = {t1}: {d1} km (1 mark)",
        ],
        "hints": [
            f"Locate {t1} on the horizontal time axis.",
            f"Trace vertically upwards to the graph at point A, then horizontally to the distance axis.",
            f"Distance = {d1} km.",
        ],
        "misconception_tags": ["distance_time_axis_reading_slip"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


def arch_32_distance_time_graph_reading_time_at_distance(rng: random.Random) -> Dict[str, Any]:
    speed = rng.choice([30, 40, 50])
    t_target = rng.choice([2, 3])
    d_target = speed * t_target

    waypoints = [
        (0.0, 0.0, "Start"),
        (float(t_target), float(d_target), "P"),
        (float(t_target + 2), float(d_target + 60), "End"),
    ]

    seed_val = rng.randint(1, 1000000)
    svg = draw_real_world_line_graph_svg(
        waypoints=waypoints,
        x_label="Time (hours)",
        y_label="Distance (km)",
        max_x=6.0,
        max_y=200.0,
        title="Delivery Van Journey",
        seed=seed_val,
    )

    return {
        "title": "Finding Time for Given Distance on Graph",
        "topic": "Graphs",
        "grade": 8,
        "term": 1,
        "subskill": "32_distance_time_graph_reading_time_at_distance",
        "difficulty": "medium",
        "question_text": (
            "Refer to the distance-time graph below.\n\n"
            f"How many hours did it take the van to travel a distance of **{d_target} km**?"
        ),
        "correct_answer": f"{t_target} hours",
        "marking_schema": [
            f"Read horizontal time coordinate at distance {d_target} km: {t_target} hours (1 mark)",
        ],
        "hints": [
            f"Locate {d_target} km on the vertical axis.",
            "Trace across horizontally to the line graph, then down to the horizontal time axis.",
            f"Time = {t_target} hours.",
        ],
        "misconception_tags": ["distance_time_inverse_lookup_error"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


def arch_33_distance_time_graph_identifying_rest_or_stopped_period(rng: random.Random) -> Dict[str, Any]:
    t_start_rest = rng.choice([1.0, 2.0])
    rest_duration = rng.choice([1.0, 1.5, 2.0])
    t_end_rest = t_start_rest + rest_duration
    d_level = rng.choice([40.0, 60.0, 80.0])

    waypoints = [
        (0.0, 0.0, "O"),
        (t_start_rest, d_level, "A"),
        (t_end_rest, d_level, "B"),
        (t_end_rest + 1.5, d_level + 50.0, "C"),
    ]

    seed_val = rng.randint(1, 1000000)
    svg = draw_real_world_line_graph_svg(
        waypoints=waypoints,
        x_label="Time (hours)",
        y_label="Distance (km)",
        max_x=6.0,
        max_y=160.0,
        title="Hiker Trip Distance-Time",
        seed=seed_val,
    )

    ans_str = f"{rest_duration:.1f}".rstrip("0").rstrip(".").replace(".", ",")

    return {
        "title": "Identifying Stationary Rest Period on Graph",
        "topic": "Graphs",
        "grade": 8,
        "term": 1,
        "subskill": "33_distance_time_graph_identifying_rest_or_stopped_period",
        "difficulty": "medium",
        "question_text": (
            "Refer to the distance-time graph below.\n\n"
            "For how many hours was the hiker stationary (stopped for rest) between points A and B?"
        ),
        "correct_answer": f"{ans_str} hours",
        "marking_schema": [
            f"Subtract rest interval times: {t_end_rest} - {t_start_rest} = {ans_str} hours (1 mark)",
        ],
        "hints": [
            "A horizontal section on a distance-time graph indicates zero speed (stationary / resting).",
            f"The rest period starts at $t = {t_start_rest}$ and ends at $t = {t_end_rest}$.",
            f"Duration = ${t_end_rest} - {t_start_rest} = {ans_str}\\text{{ hours}}$.",
        ],
        "misconception_tags": ["stationary_graph_interval_duration_error"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


def arch_34_distance_time_graph_calculating_speed_for_segment(rng: random.Random) -> Dict[str, Any]:
    hours = rng.choice([2, 3])
    speed = rng.choice([50, 60, 70])
    dist = hours * speed

    waypoints = [
        (0.0, 0.0, "O"),
        (float(hours), float(dist), "A"),
        (float(hours + 2), float(dist + 60), "B"),
    ]

    seed_val = rng.randint(1, 1000000)
    svg = draw_real_world_line_graph_svg(
        waypoints=waypoints,
        x_label="Time (hours)",
        y_label="Distance (km)",
        max_x=6.0,
        max_y=240.0,
        title="Vehicle Journey Speed",
        seed=seed_val,
    )

    return {
        "title": "Calculating Speed from Distance-Time Graph",
        "topic": "Graphs",
        "grade": 8,
        "term": 1,
        "subskill": "34_distance_time_graph_calculating_speed_for_segment",
        "difficulty": "medium",
        "question_text": (
            "Refer to the distance-time graph below.\n\n"
            "Calculate the speed (in km/h) of the vehicle during the first stage from **O to A**."
        ),
        "correct_answer": f"{speed} km/h",
        "marking_schema": [
            f"Speed = distance/time = {dist}/{hours} = {speed} km/h (2 marks)",
        ],
        "hints": [
            "Speed is given by the gradient of the distance-time graph: $\\text{Speed} = \\frac{\\Delta \\text{Distance}}{\\Delta \\text{Time}}$.",
            f"Distance covered = {dist} km; Time taken = {hours} hours.",
            f"Speed = $\\frac{{{dist}}}{{{hours}}} = {speed}\\text{{ km/h}}$.",
        ],
        "misconception_tags": ["speed_formula_time_over_distance_inversion"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


def arch_35_distance_time_graph_identifying_fastest_segment(rng: random.Random) -> Dict[str, Any]:
    # Stage 1: 1 hr, 30 km -> 30 km/h
    # Stage 2: 1 hr, 60 km -> 60 km/h (fastest)
    # Stage 3: 2 hrs, 40 km -> 20 km/h
    waypoints = [
        (0.0, 0.0, "O"),
        (1.0, 30.0, "A"),
        (2.0, 90.0, "B"),
        (4.0, 130.0, "C"),
    ]

    seed_val = rng.randint(1, 1000000)
    svg = draw_real_world_line_graph_svg(
        waypoints=waypoints,
        x_label="Time (hours)",
        y_label="Distance (km)",
        max_x=5.0,
        max_y=150.0,
        title="Multi-Stage Trip",
        seed=seed_val,
    )

    return {
        "title": "Identifying the Fastest Stage of a Journey",
        "topic": "Graphs",
        "grade": 8,
        "term": 1,
        "subskill": "35_distance_time_graph_identifying_fastest_segment",
        "difficulty": "medium",
        "question_text": (
            "Refer to the multi-stage distance-time graph below.\n\n"
            "Which stage of the journey (**OA**, **AB**, or **BC**) was traveled at the **greatest speed**?"
        ),
        "correct_answer": "AB",
        "marking_schema": [
            "Identify segment with steepest gradient: AB (60 km/h) (1 mark)",
        ],
        "hints": [
            "On a distance-time graph, the steepest line segment corresponds to the greatest speed.",
            "Calculate slopes: OA = 30 km/h, AB = (90 - 30)/1 = 60 km/h, BC = (130 - 90)/2 = 20 km/h.",
            "Stage AB has the steepest gradient and highest speed.",
        ],
        "misconception_tags": ["steepest_segment_speed_misinterpretation"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


def arch_36_distance_time_graph_return_journey_analysis(rng: random.Random) -> Dict[str, Any]:
    d_max = rng.choice([60.0, 80.0, 100.0])
    t_out = 2.0
    t_ret = t_out + rng.choice([1.0, 2.0])

    waypoints = [
        (0.0, 0.0, "Home"),
        (t_out, d_max, "Destination"),
        (t_ret, 0.0, "Back Home"),
    ]

    seed_val = rng.randint(1, 1000000)
    svg = draw_real_world_line_graph_svg(
        waypoints=waypoints,
        x_label="Time (hours)",
        y_label="Distance from Home (km)",
        max_x=5.0,
        max_y=120.0,
        title="Round Trip Distance-Time",
        seed=seed_val,
    )

    ret_hrs = t_ret - t_out
    ret_speed = int(d_max / ret_hrs)

    return {
        "title": "Return Journey Speed Analysis",
        "topic": "Graphs",
        "grade": 8,
        "term": 1,
        "subskill": "36_distance_time_graph_return_journey_analysis",
        "difficulty": "hard",
        "question_text": (
            "Refer to the round-trip distance-time graph below.\n\n"
            "Calculate the speed (in km/h) during the **return journey** from the Destination back Home."
        ),
        "correct_answer": f"{ret_speed} km/h",
        "marking_schema": [
            f"Return time = {t_ret} - {t_out} = {ret_hrs} hrs [1M]",
            f"Return speed = {int(d_max)} / {ret_hrs} = {ret_speed} km/h [1A]",
        ],
        "hints": [
            f"The traveler leaves Destination at $t = {t_out}$ and arrives Home at $t = {t_ret}$.",
            f"Return duration = ${ret_hrs}\\text{{ hours}}$; distance returned = ${int(d_max)}\\text{{ km}}$.",
            f"Return speed = $\\frac{{{int(d_max)}}}{{{ret_hrs}}} = {ret_speed}\\text{{ km/h}}$.",
        ],
        "misconception_tags": ["negative_slope_speed_as_negative_fallacy"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


def arch_37_distance_time_graph_average_speed_entire_journey(rng: random.Random) -> Dict[str, Any]:
    tot_hrs = rng.choice([3, 4, 5])
    avg_speed = rng.choice([40, 50, 60])
    tot_dist = tot_hrs * avg_speed

    waypoints = [
        (0.0, 0.0, "O"),
        (1.0, float(avg_speed - 10), "A"),
        (2.0, float(avg_speed + 20), "B"),
        (float(tot_hrs), float(tot_dist), "C"),
    ]

    seed_val = rng.randint(1, 1000000)
    svg = draw_real_world_line_graph_svg(
        waypoints=waypoints,
        x_label="Time (hours)",
        y_label="Total Distance (km)",
        max_x=float(tot_hrs + 1),
        max_y=float(tot_dist + 50),
        title="Complete Journey",
        seed=seed_val,
    )

    return {
        "title": "Average Speed for Entire Journey",
        "topic": "Graphs",
        "grade": 8,
        "term": 1,
        "subskill": "37_distance_time_graph_average_speed_entire_journey",
        "difficulty": "medium",
        "question_text": (
            "Refer to the distance-time graph below.\n\n"
            "Calculate the **average speed** (in km/h) across the entire journey from O to C."
        ),
        "correct_answer": f"{avg_speed} km/h",
        "marking_schema": [
            f"Average speed = total distance / total time = {tot_dist} / {tot_hrs} = {avg_speed} km/h (2 marks)",
        ],
        "hints": [
            "Average speed is calculated as: $\\text{Average Speed} = \\frac{\\text{Total Distance}}{\\text{Total Time}}$.",
            f"Total distance = {tot_dist} km; Total time = {tot_hrs} hours.",
            f"Average speed = $\\frac{{{tot_dist}}}{{{tot_hrs}}} = {avg_speed}\\text{{ km/h}}$.",
        ],
        "misconception_tags": ["average_speed_segment_mean_fallacy"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


def arch_38_comparing_two_travelers_on_same_distance_time_graph(rng: random.Random) -> Dict[str, Any]:
    # Traveler A starts at t=0, speed=40 km/h -> at t=2 d=80
    # Traveler B starts at t=1, speed=80 km/h -> at t=2 d=80 (overtakes!)
    waypoints = [
        (0.0, 0.0, "A start"),
        (1.0, 40.0, "B start (d=0)"),
        (2.0, 80.0, "Overtake (d=80)"),
        (3.0, 120.0, "A end"),
    ]

    seed_val = rng.randint(1, 1000000)
    svg = draw_real_world_line_graph_svg(
        waypoints=waypoints,
        x_label="Time (hours)",
        y_label="Distance (km)",
        max_x=4.0,
        max_y=160.0,
        title="Two Cyclists Journey Comparison",
        seed=seed_val,
    )

    return {
        "title": "Comparing Two Travelers on a Distance-Time Graph",
        "topic": "Graphs",
        "grade": 8,
        "term": 1,
        "subskill": "38_comparing_two_travelers_on_same_distance_time_graph",
        "difficulty": "hard",
        "question_text": (
            "Refer to the distance-time graph below showing two travelers.\n\n"
            "At what time ($t$ in hours) do the two travelers meet / cross each other?"
        ),
        "correct_answer": "2 hours",
        "marking_schema": [
            "Read intersection time t = 2 hours: 1 mark",
        ],
        "hints": [
            "Travelers meet at the point where their graphs intersect.",
            "Locate the intersection point (2; 80).",
            "They meet at $t = 2\\text{ hours}$.",
        ],
        "misconception_tags": ["intersection_time_distance_confusion"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


def arch_39_speed_time_graph_identifying_constant_speed_acceleration(rng: random.Random) -> Dict[str, Any]:
    target = rng.choice(["constant speed", "constant acceleration", "deceleration"])
    if target == "constant speed":
        ans = "horizontal line segment"
        reason = "speed remains unchanged as time passes"
    elif target == "constant acceleration":
        ans = "upward sloping straight line"
        reason = "speed increases at a steady constant rate"
    else:
        ans = "downward sloping straight line"
        reason = "speed decreases steadily towards zero"

    return {
        "title": "Speed-Time Graph Segment Characteristics",
        "topic": "Graphs",
        "grade": 8,
        "term": 1,
        "subskill": "39_speed_time_graph_identifying_constant_speed_acceleration",
        "difficulty": "medium",
        "question_text": (
            f"On a **speed-time graph**, how is **{target}** represented graphically?\n\n"
            f"Choose: (upward sloping straight line / horizontal line segment / downward sloping straight line)."
        ),
        "correct_answer": ans,
        "marking_schema": [
            f"State graphic representation for {target}: '{ans}' (1 mark)",
        ],
        "hints": [
            "On a speed-time graph, the gradient represents acceleration.",
            f"For {target}, {reason}.",
            f"Representation: {ans}.",
        ],
        "misconception_tags": ["speed_time_vs_distance_time_graph_confusion"],
        "diagram_spec": None,
    }


def arch_40_speed_time_graph_calculating_acceleration(rng: random.Random) -> Dict[str, Any]:
    t = rng.choice([4, 5, 8, 10])
    acc = rng.choice([2, 3, 4])
    v_final = acc * t

    return {
        "title": "Calculating Acceleration from Speed-Time Graph",
        "topic": "Graphs",
        "grade": 8,
        "term": 1,
        "subskill": "40_speed_time_graph_calculating_acceleration",
        "difficulty": "hard",
        "question_text": (
            f"A car accelerates uniformly from rest ($0\\text{{ m/s}}$) to a speed of **{v_final} m/s** over **{t} seconds**.\n\n"
            f"Calculate the acceleration in $\\text{{m/s}}^2$ (the gradient of the speed-time graph)."
        ),
        "correct_answer": f"{acc} m/s^2",
        "marking_schema": [
            f"Acceleration = change in speed / time = {v_final} / {t} = {acc} m/s^2 (2 marks)",
        ],
        "hints": [
            "Acceleration = $\\frac{v - u}{t} = \\frac{\\Delta v}{\\Delta t}$.",
            f"$\\text{{Acceleration}} = \\frac{{{v_final} - 0}}{{{t}}} = {acc}\\text{{ m/s}}^2$.",
            f"Answer: {acc} $\\text{{m/s}}^2$.",
        ],
        "misconception_tags": ["acceleration_formula_units_slip"],
        "diagram_spec": None,
    }


def arch_41_story_graph_water_level_in_uniform_cylinder(rng: random.Random) -> Dict[str, Any]:
    return {
        "title": "Water Level in Uniform Cylinder",
        "topic": "Graphs",
        "grade": 8,
        "term": 1,
        "subskill": "41_story_graph_water_level_in_uniform_cylinder",
        "difficulty": "easy",
        "question_text": (
            "Water is poured at a constant rate into a container that has straight vertical sides (a uniform cylinder).\n\n"
            "Will the plot of water height against time produce a **straight line** or a **curved line**? Give a reason."
        ),
        "correct_answer": "Straight line, because the cross-sectional area is constant so height increases at a constant rate.",
        "marking_schema": [
            "State straight line with constant rate justification: 1 mark",
        ],
        "hints": [
            "When the cross-sectional area of a container is uniform, equal volumes of water increase the height by equal amounts.",
            "A constant rate of change produces a straight-line linear graph.",
            "Answer: Straight line.",
        ],
        "misconception_tags": ["container_filling_graph_shape_error"],
        "diagram_spec": None,
    }


def arch_42_story_graph_water_level_in_conical_or_stepped_flask(rng: random.Random) -> Dict[str, Any]:
    return {
        "title": "Water Level in Widening Conical Flask",
        "topic": "Graphs",
        "grade": 8,
        "term": 1,
        "subskill": "42_story_graph_water_level_in_conical_or_stepped_flask",
        "difficulty": "medium",
        "question_text": (
            "A beaker widens as it goes up (narrow at the bottom, wider at the top). Water is added at a constant flow rate.\n\n"
            "As time passes, does the water level rise **faster**, **slower**, or at a **constant speed**?"
        ),
        "correct_answer": "Slower",
        "marking_schema": [
            "State slower because greater width requires more water per cm of height: 1 mark",
        ],
        "hints": [
            "As the container gets wider, each centimeter of height requires more volume of water.",
            "Since water enters at a constant rate, it takes longer to gain each additional centimeter.",
            "The water level rises slower (the graph becomes less steep).",
        ],
        "misconception_tags": ["conical_flask_rate_of_rise_inversion"],
        "diagram_spec": None,
    }


def arch_43_temperature_time_graph_cooling_rate(rng: random.Random) -> Dict[str, Any]:
    t_start = 85
    hrs = rng.choice([2, 3, 4])
    drop = hrs * rng.choice([8, 10, 12])
    t_end = t_start - drop
    rate = drop // hrs

    return {
        "title": "Rate of Cooling from Temperature Graph",
        "topic": "Graphs",
        "grade": 8,
        "term": 1,
        "subskill": "43_temperature_time_graph_cooling_rate",
        "difficulty": "medium",
        "question_text": (
            f"A hot liquid cools linearly from an initial temperature of **{t_start}°C** down to **{t_end}°C** over **{hrs} hours**.\n\n"
            f"Calculate the average rate of cooling in **°C per hour**."
        ),
        "correct_answer": f"{rate} °C/hour",
        "marking_schema": [
            f"Calculate temperature drop: {t_start} - {t_end} = {drop} °C [1M]",
            f"Divide by time: {drop} / {hrs} = {rate} °C/hour [1A]",
        ],
        "hints": [
            f"Temperature decrease = ${t_start} - {t_end} = {drop}^\\circ\\text{{C}}$.",
            f"Rate of cooling = $\\frac{{{drop}}}{{{hrs}}} = {rate}^\\circ\\text{{C per hour}}$.",
            f"Answer: {rate} °C/hour.",
        ],
        "misconception_tags": ["rate_of_change_sign_inversion"],
        "diagram_spec": None,
    }


def arch_44_conversion_graph_currency_rand_to_foreign(rng: random.Random) -> Dict[str, Any]:
    rate = rng.choice([18, 19, 20])
    usd = rng.choice([10, 20, 50])
    rand_val = usd * rate

    return {
        "title": "Currency Conversion Graph Analysis",
        "topic": "Graphs",
        "grade": 8,
        "term": 1,
        "subskill": "44_conversion_graph_currency_rand_to_foreign",
        "difficulty": "easy",
        "question_text": (
            f"On a currency conversion graph, **$1\\text{{ USD}}$** corresponds to **$\\text{{R}}{rate}$**.\n\n"
            f"Use this conversion rate to determine the value in South African Rand of **${usd} USD**."
        ),
        "correct_answer": f"R{rand_val}",
        "marking_schema": [
            f"Multiply {usd} * R{rate} = R{rand_val} (1 mark)",
        ],
        "hints": [
            f"The gradient of this conversion line is {rate} Rand per US Dollar.",
            f"Multiply: ${usd} \\times \\text{{R}}{rate} = \\text{{R}}{rand_val}$.",
            f"Value = R{rand_val}.",
        ],
        "misconception_tags": ["currency_conversion_operation_inversion"],
        "diagram_spec": None,
    }


def arch_45_conversion_graph_metric_to_imperial_units(rng: random.Random) -> Dict[str, Any]:
    # 5 miles approx 8 km
    miles = rng.choice([10, 15, 20, 25])
    km = int((miles * 8) / 5)

    return {
        "title": "Unit Conversion Graph (Miles to km)",
        "topic": "Graphs",
        "grade": 8,
        "term": 1,
        "subskill": "45_conversion_graph_metric_to_imperial_units",
        "difficulty": "medium",
        "question_text": (
            f"A distance conversion graph shows that **5 miles** is approximately equal to **8 km**.\n\n"
            f"How many kilometers are approximately equal to **{miles} miles**?"
        ),
        "correct_answer": f"{km} km",
        "marking_schema": [
            f"Scale conversion: ({miles}/5) * 8 = {km} km (1 mark)",
        ],
        "hints": [
            f"Find how many 5-mile units there are: ${miles} \\div 5 = {miles // 5}$.",
            f"Multiply by 8 km: ${miles // 5} \\times 8 = {km}\\text{{ km}}$.",
            f"Answer: {km} km.",
        ],
        "misconception_tags": ["conversion_ratio_scaling_error"],
        "diagram_spec": None,
    }


def arch_46_direct_proportion_graph_passes_through_origin(rng: random.Random) -> Dict[str, Any]:
    return {
        "title": "Direct Proportion Characteristics",
        "topic": "Graphs",
        "grade": 8,
        "term": 1,
        "subskill": "46_direct_proportion_graph_passes_through_origin",
        "difficulty": "easy",
        "question_text": (
            "Name the **two essential graphical characteristics** of a direct proportion relationship on a Cartesian plane."
        ),
        "correct_answer": "It is a straight line and it passes through the origin (0; 0).",
        "marking_schema": [
            "State straight line [1 mark] and passes through the origin (0; 0) [1 mark]",
        ],
        "hints": [
            "Direct proportion means y = kx.",
            "Because y = k(0) = 0, the graph must always pass through the origin (0; 0).",
            "Because the rate k is constant, it must be a straight line.",
        ],
        "misconception_tags": ["direct_proportion_origin_property_omission"],
        "diagram_spec": None,
    }


def arch_47_inverse_proportion_graph_hyperbola_shape(rng: random.Random) -> Dict[str, Any]:
    return {
        "title": "Inverse Proportion Graph Shape",
        "topic": "Graphs",
        "grade": 8,
        "term": 1,
        "subskill": "47_inverse_proportion_graph_hyperbola_shape",
        "difficulty": "medium",
        "question_text": (
            "As the number of workers on a project increases, the time required to complete the task decreases proportionally ($xy = k$).\n\n"
            "Does this relationship form a **straight line** or a **curved hyperbola**?"
        ),
        "correct_answer": "Curved hyperbola",
        "marking_schema": [
            "State curved hyperbola / curve: 1 mark",
        ],
        "hints": [
            "Inverse proportion is modeled by $y = \\frac{k}{x}$.",
            "As x becomes very large, y approaches zero but never touches the axis.",
            "The graph is a curved hyperbola.",
        ],
        "misconception_tags": ["inverse_proportion_linear_misconception"],
        "diagram_spec": None,
    }


def arch_48_mobile_phone_call_cost_linear_tariff_graph(rng: random.Random) -> Dict[str, Any]:
    fixed = rng.choice([20, 30, 50])
    rate = rng.choice([1.5, 2.0, 2.5])
    mins = rng.choice([20, 40, 60])
    total = fixed + int(rate * mins)

    return {
        "title": "Interpreting Linear Tariff Cost Graph",
        "topic": "Graphs",
        "grade": 8,
        "term": 1,
        "subskill": "48_mobile_phone_call_cost_linear_tariff_graph",
        "difficulty": "medium",
        "question_text": (
            f"A cell phone contract graph has a vertical intercept at **R{fixed}** (monthly subscription) and increases at **R{rate:.2f} per minute** of calls.\n\n"
            f"Calculate the total cost in Rand for a month with **{mins} minutes** of calls."
        ),
        "correct_answer": f"R{total}",
        "marking_schema": [
            f"Calculate total = {fixed} + ({rate} * {mins}) = R{total} (2 marks)",
        ],
        "hints": [
            f"Use the linear equation: $\\text{{Cost}} = \\text{{R}}{fixed} + {rate}m$.",
            f"Multiply: ${rate} \\times {mins} = \\text{{R}}{int(rate * mins)}$.",
            f"Add fixed fee: $\\text{{R}}{fixed} + \\text{{R}}{int(rate * mins)} = \\text{{R}}{total}$.",
        ],
        "misconception_tags": ["tariff_fixed_charge_omission_slip"],
        "diagram_spec": None,
    }


def arch_49_break_even_point_identification_on_cost_revenue_graph(rng: random.Random) -> Dict[str, Any]:
    be_units = rng.choice([50, 100, 150, 200])
    be_rand = be_units * rng.choice([15, 20, 25])

    return {
        "title": "Break-Even Point on Financial Graph",
        "topic": "Graphs",
        "grade": 8,
        "term": 1,
        "subskill": "49_break_even_point_identification_on_cost_revenue_graph",
        "difficulty": "medium",
        "question_text": (
            f"A business graph shows that the Total Cost line and Total Revenue line intersect at **$({be_units}; {be_rand})$**.\n\n"
            f"1. How many units must the business sell to break even?\n"
            f"2. What is the value of revenue at the break-even point in Rand?"
        ),
        "correct_answer": f"1. {be_units} units; 2. R{be_rand}",
        "marking_schema": [
            f"Identify break-even quantity {be_units} units [1 mark] and revenue R{be_rand} [1 mark]",
        ],
        "hints": [
            "The break-even point is the intersection where Total Cost = Total Revenue.",
            f"The x-coordinate gives the number of units: {be_units}.",
            f"The y-coordinate gives the monetary value: R{be_rand}.",
        ],
        "misconception_tags": ["break_even_x_y_value_inversion"],
        "diagram_spec": None,
    }


def arch_50_matching_verbal_story_to_correct_graph_shape(rng: random.Random) -> Dict[str, Any]:
    stories = [
        ("A cyclist accelerates from rest, rides at a constant high speed, and then brakes steadily to a stop.", "Graph B (rising line, horizontal flat top, falling line)"),
        ("A learner walks to school at a steady pace, stops to chat with a friend, and then runs fast to make the bell.", "Graph A (steady rising slope, horizontal rest segment, steeper rising slope)"),
        ("A car travels at a steady speed on a highway, encounters heavy stop-and-go traffic, and resumes steady cruising.", "Graph C (rising line, oscillating wavy segment, rising line)"),
    ]
    story, correct_desc = rng.choice(stories)

    return {
        "title": "Matching Verbal Story to Graph Progression",
        "topic": "Graphs",
        "grade": 8,
        "term": 1,
        "subskill": "50_matching_verbal_story_to_correct_graph_shape",
        "difficulty": "hard",
        "question_text": (
            f"Consider this narrative: **\"{story}\"**\n\n"
            "Describe the shapes and slope changes of the corresponding distance-time graph across the three stages."
        ),
        "correct_answer": correct_desc,
        "marking_schema": [
            f"Accurately describe each stage's gradient and shape: {correct_desc} (2 marks)",
        ],
        "hints": [
            "Steady walking/cycling corresponds to a constant positive gradient.",
            "Stopping corresponds to a flat horizontal line (zero gradient).",
            "Moving faster corresponds to a steeper line with greater slope.",
        ],
        "misconception_tags": ["narrative_graph_speed_slope_confusion"],
        "diagram_spec": None,
    }


BUILDERS_26_50 = [
    arch_26_identifying_parallel_lines_equal_gradients,
    arch_27_determining_direction_of_line_from_gradient_sign,
    arch_28_comparing_steepness_of_two_lines,
    arch_29_finding_missing_coordinate_given_gradient,
    arch_30_point_lies_on_line_verification,
    arch_31_distance_time_graph_reading_distance_at_time,
    arch_32_distance_time_graph_reading_time_at_distance,
    arch_33_distance_time_graph_identifying_rest_or_stopped_period,
    arch_34_distance_time_graph_calculating_speed_for_segment,
    arch_35_distance_time_graph_identifying_fastest_segment,
    arch_36_distance_time_graph_return_journey_analysis,
    arch_37_distance_time_graph_average_speed_entire_journey,
    arch_38_comparing_two_travelers_on_same_distance_time_graph,
    arch_39_speed_time_graph_identifying_constant_speed_acceleration,
    arch_40_speed_time_graph_calculating_acceleration,
    arch_41_story_graph_water_level_in_uniform_cylinder,
    arch_42_story_graph_water_level_in_conical_or_stepped_flask,
    arch_43_temperature_time_graph_cooling_rate,
    arch_44_conversion_graph_currency_rand_to_foreign,
    arch_45_conversion_graph_metric_to_imperial_units,
    arch_46_direct_proportion_graph_passes_through_origin,
    arch_47_inverse_proportion_graph_hyperbola_shape,
    arch_48_mobile_phone_call_cost_linear_tariff_graph,
    arch_49_break_even_point_identification_on_cost_revenue_graph,
    arch_50_matching_verbal_story_to_correct_graph_shape,
]
