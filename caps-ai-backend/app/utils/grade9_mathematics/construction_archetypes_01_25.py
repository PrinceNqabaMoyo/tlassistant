"""Grade 9 Mathematics - Construction of Geometric Figures Archetypes 01 to 25
=============================================================================
Grounded strictly in:
  - CAPS Grade 9 Mathematics: Term 3 Topic: Construction of geometric figures
  - curriculum_docs_auto/Mathematics_Gr9/Term 3/01. Construction of geometric figures.md
  - Chapter 4: Compass and straightedge constructions, angle bisection, perpendicular
    bisectors, special angle constructions (30°, 45°, 60°, 75°, 90°, 105°, 120°),
    and triangle construction foundations

Covers Archetypes 01 - 25:
  01: Angle classification and measurement
  02: Angle bisector concept and definition
  03: Angle bisector algebraic equation solving
  04: Identifying angle bisector compass construction arcs
  05: Bisecting obtuse and reflex angles
  06: Bisectors of adjacent supplementary angles form a right angle (90°)
  07: Repeated angle bisection (powers of 2)
  08: Perpendicular bisector definition and midpoint calculation
  09: Perpendicular bisector equidistance property (PA = PB)
  10: Minimum compass radius condition for perpendicular bisector (r > L/2)
  11: Constructing a perpendicular line through a point on a line
  12: Constructing a perpendicular from an external point to a line
  13: Shortest distance from a point to a line (perpendicular segment)
  14: Equidistant locus between two parallel lines
  15: Constructing 60° angle using equilateral triangle arc
  16: Constructing 30° angle by bisecting 60°
  17: Constructing 90° angle using perpendicular line construction
  18: Constructing 45° angle by bisecting 90°
  19: Constructing 15° angle by bisecting 30°
  20: Constructing 75° angle as 60° + 15° combination
  21: Constructing 105° angle as 90° + 15° combination
  22: Constructing 120° and 135° angles without protractor
  23: Triangle Inequality Theorem validity check (a + b > c)
  24: Valid integer range for the third side of a triangle
  25: Constructing triangle given three side lengths (SSS)
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional

from app.utils.grade9_mathematics.construction_svg import (
    draw_angle_bisector_construction_svg,
    draw_perpendicular_bisector_svg,
    draw_special_angle_construction_svg,
    draw_triangle_construction_svg,
)


def arch_01_angle_classification_and_measurement(rng: random.Random) -> Dict[str, Any]:
    """Classify an angle by its size in degrees."""
    angle_types = [
        (rng.randint(25, 80), "acute angle", "it is strictly between 0° and 90°"),
        (90, "right angle", "it is exactly equal to 90°"),
        (rng.randint(95, 170), "obtuse angle", "it is strictly between 90° and 180°"),
        (180, "straight angle", "it is exactly equal to 180°"),
        (rng.randint(190, 340), "reflex angle", "it is strictly between 180° and 360°"),
    ]
    deg, name, reason = rng.choice(angle_types)

    prompt = (
        f"An angle measures **${deg}^\\circ$**.\n\n"
        f"Classify this angle according to its size (state: **acute angle**, **right angle**, "
        f"**obtuse angle**, **straight angle**, or **reflex angle**)."
    )

    return {
        "subskill": "01_angle_classification_and_measurement",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": name,
        "sample_answer": name,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Identify angle interval: {deg}° ({reason})", "marks": 1},
            {"step": f"Classify as {name}", "marks": 1},
        ],
        "hints": [
            "Acute: $0^\\circ < \\theta < 90^\\circ$. Right: $90^\\circ$. Obtuse: $90^\\circ < \\theta < 180^\\circ$.",
            "Straight: $180^\\circ$. Reflex: $180^\\circ < \\theta < 360^\\circ$.",
            f"An angle of ${deg}^\\circ$ is a {name}.",
        ],
        "misconception_tags": ["angle_classification_error", "reflex_vs_obtuse_confusion"],
    }


def arch_02_angle_bisector_concept_and_definition(rng: random.Random) -> Dict[str, Any]:
    """Calculate the size of each half of a bisected angle."""
    full_angle = rng.choice([48, 64, 76, 88, 110, 124, 136, 150])
    half_angle = full_angle // 2
    seed_val = rng.randint(1000, 999999)

    svg = draw_angle_bisector_construction_svg(
        angle_deg=full_angle,
        title="Angle Bisection Construction",
        seed=seed_val,
    )

    prompt = (
        f"In the geometric construction below, ray $BP$ is the **angle bisector** of $\\angle ABC = {full_angle}^\\circ$:\n\n"
        f"Calculate the size of angle $\\angle PBC$ in degrees ($^\\circ$)."
    )

    return {
        "subskill": "02_angle_bisector_concept_and_definition",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": str(half_angle),
        "sample_answer": f"{half_angle}°",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "State that an angle bisector divides an angle into two equal halves", "marks": 1},
            {"step": f"Calculate: {full_angle}° / 2 = {half_angle}°", "marks": 1},
        ],
        "hints": [
            "An angle bisector divides an angle into two equal halves.",
            f"Divide ${full_angle}^\\circ$ by $2$.",
            f"Each bisected angle is ${half_angle}^\\circ$.",
        ],
        "misconception_tags": ["angle_bisector_definition_error", "halving_arithmetic_error"],
    }


def arch_03_angle_bisector_algebraic_equation(rng: random.Random) -> Dict[str, Any]:
    """Solve for x when two bisected halves are given as algebraic expressions."""
    # Ray BP bisects angle ABC => Angle 1 = Angle 2
    # ax + b = cx + d => (a - c)x = d - b
    x_val = rng.choice([4, 5, 6, 7, 8])
    c = rng.choice([2, 3])
    a = c + rng.choice([1, 2])
    b = rng.randint(5, 15)
    d = (a - c) * x_val + b
    half_deg = a * x_val + b
    full_deg = half_deg * 2

    prompt = (
        f"Ray $BD$ bisects angle $\\angle ABC$.\n"
        f"The two bisected halves are given by:\n"
        f"- $\\angle ABD = {a}x + {b}^\\circ$\n"
        f"- $\\angle DBC = {c}x + {d}^\\circ$\n\n"
        f"1. Set up an equation and solve for **$x$**.\n"
        f"2. Calculate the size of the full angle **$\\angle ABC$** in degrees."
    )

    return {
        "subskill": "03_angle_bisector_algebraic_equation",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": str(full_deg),
        "sample_answer": f"{full_deg}° (x = {x_val})",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Equate halves: {a}x + {b} = {c}x + {d}", "marks": 1},
            {"step": f"Solve for x: {a - c}x = {d - b} => x = {x_val}", "marks": 1},
            {"step": f"Calculate full angle: 2 * ({a}({x_val}) + {b}) = 2 * {half_deg} = {full_deg}°", "marks": 1},
        ],
        "hints": [
            "Because $BD$ bisects $\\angle ABC$, $\\angle ABD = \\angle DBC$.",
            f"Set ${a}x + {b} = {c}x + {d}$ and solve for $x = {x_val}$.",
            f"Each half is ${half_deg}^\\circ$, so the full angle is $2 \\times {half_deg}^\\circ = {full_deg}^\\circ$.",
        ],
        "misconception_tags": ["angle_bisector_algebraic_equating_error", "forgot_to_double_for_full_angle"],
    }


def arch_04_identify_angle_bisector_compass_arcs(rng: random.Random) -> Dict[str, Any]:
    """Identify the fundamental geometric condition for constructing an angle bisector."""
    correct_desc = "drawing arcs of equal radius from points on the arms so the intersection point is equidistant from both arms"
    
    prompt = (
        f"When using a compass and straightedge to bisect an angle $\\angle ABC$ at vertex $B$:\n\n"
        f"What geometric principle ensures that the constructed ray $BP$ cuts the angle into two equal parts?\n"
        f"Answer: **equidistant** (the points and intersection arc are equidistant from the arms)."
    )

    return {
        "subskill": "04_identify_angle_bisector_compass_arcs",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": "equidistant",
        "sample_answer": "equidistant",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "State that the construction creates congruent triangles by establishing points equidistant from the vertex and arms", "marks": 1},
            {"step": "Conclude that any point on the bisector is equidistant from the arms", "marks": 1},
        ],
        "hints": [
            "The compass arcs create congruent triangles (SSS) on either side of the bisector.",
            "Every point along an angle bisector is the exact same distance from both arms of the angle.",
            "Answer: **equidistant**.",
        ],
        "misconception_tags": ["equidistant_locus_concept", "compass_arc_justification_error"],
    }


def arch_05_bisect_obtuse_or_reflex_angle(rng: random.Random) -> Dict[str, Any]:
    """Calculate the bisector of a reflex angle."""
    interior_acute = rng.choice([50, 60, 70, 80, 100])
    reflex_deg = 360 - interior_acute
    half_reflex = reflex_deg // 2

    prompt = (
        f"A reflex angle measures **${reflex_deg}^\\circ$**.\n\n"
        f"If a compass is used to bisect this reflex angle, what will be the size of each "
        f"bisected half in degrees ($^\\circ$)?"
    )

    return {
        "subskill": "05_bisect_obtuse_or_reflex_angle",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": str(half_reflex),
        "sample_answer": f"{half_reflex}°",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Apply bisection: divide reflex angle by 2", "marks": 1},
            {"step": f"Calculate: {reflex_deg}° / 2 = {half_reflex}°", "marks": 1},
        ],
        "hints": [
            "Bisection divides any angle into two equal parts, regardless of whether it is acute, obtuse, or reflex.",
            f"Divide ${reflex_deg}^\\circ$ by $2$.",
            f"Each half is ${half_reflex}^\\circ$.",
        ],
        "misconception_tags": ["reflex_angle_bisection_confusion", "halving_angles_greater_than_180"],
    }


def arch_06_adjacent_supplementary_angle_bisectors_perpendicular(rng: random.Random) -> Dict[str, Any]:
    """Prove that the bisectors of two adjacent supplementary angles form 90 degrees."""
    theta = rng.choice([40, 50, 60, 70, 80, 110, 120])
    supp = 180 - theta

    prompt = (
        f"Two adjacent angles lie on a straight line, measuring **${theta}^\\circ$** and **${supp}^\\circ$**.\n\n"
        f"A compass is used to construct the angle bisector of each of the two angles.\n"
        f"Calculate the angle formed between the two bisectors in degrees ($^\\circ$)."
    )

    return {
        "subskill": "06_adjacent_supplementary_angle_bisectors_perpendicular",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": "90",
        "sample_answer": "90°",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Calculate first half: {theta}° / 2 = {theta / 2}°", "marks": 1},
            {"step": f"Calculate second half: {supp}° / 2 = {supp / 2}°", "marks": 1},
            {"step": f"Add the two halves: {theta / 2}° + {supp / 2}° = 90° (perpendicular)", "marks": 1},
        ],
        "hints": [
            f"The bisector of ${theta}^\\circ$ gives ${theta / 2}^\\circ$.",
            f"The bisector of ${supp}^\\circ$ gives ${supp / 2}^\\circ$.",
            f"Sum between the two bisectors $= {theta / 2}^\\circ + {supp / 2}^\\circ = 90^\\circ$.",
        ],
        "misconception_tags": ["supplementary_angle_bisectors_concept", "perpendicular_bisectors_of_angles"],
    }


def arch_07_angle_trisection_vs_bisection_concepts(rng: random.Random) -> Dict[str, Any]:
    """Calculate size of each angle when an angle is bisected repeatedly n times."""
    n = rng.choice([2, 3])
    parts = 2**n  # 4 or 8
    base_angle = rng.choice([96, 128, 160])
    each_part = base_angle // parts

    prompt = (
        f"An angle of **${base_angle}^\\circ$** is bisected with a compass. Each resulting half is then "
        f"bisected again (a total of **${n}$ successive bisections**).\n\n"
        f"Calculate the size of each resulting small angle in degrees ($^\\circ$)."
    )

    return {
        "subskill": "07_angle_trisection_vs_bisection_concepts",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": str(each_part),
        "sample_answer": f"{each_part}°",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Identify that {n} successive bisections divide the angle into 2^{n} = {parts} equal parts", "marks": 1},
            {"step": f"Calculate: {base_angle}° / {parts} = {each_part}°", "marks": 1},
        ],
        "hints": [
            f"Each bisection doubles the number of equal divisions: $2^{n} = {parts}$ equal parts.",
            f"Divide the original angle ${base_angle}^\\circ$ by ${parts}$.",
            f"Each angle measures ${each_part}^\\circ$.",
        ],
        "misconception_tags": ["repeated_bisection_powers_of_two", "division_in_successive_halving"],
    }


def arch_08_perpendicular_bisector_definition_and_midpoint(rng: random.Random) -> Dict[str, Any]:
    """Calculate midpoint distance AM from length of segment AB."""
    ab_len = rng.choice([8, 10, 12, 14, 16, 18, 20])
    am_len = ab_len // 2
    seed_val = rng.randint(1000, 999999)

    svg = draw_perpendicular_bisector_svg(length_px=220, label_a="A", label_b="B", seed=seed_val)

    prompt = (
        f"A line segment $AB$ has a length of **${ab_len}\\text{{ cm}}$**.\n"
        f"The perpendicular bisector of $AB$ intersects $AB$ at point $M$.\n\n"
        f"1. What is the angle formed between the bisector and segment $AB$?\n"
        f"2. Calculate the length of segment **$AM$** in centimetres."
    )

    return {
        "subskill": "08_perpendicular_bisector_definition_and_midpoint",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": str(am_len),
        "sample_answer": f"{am_len} cm (angle = 90°)",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "State that a perpendicular bisector intersects at 90° and cuts the segment in half", "marks": 1},
            {"step": f"Calculate AM = AB / 2 = {ab_len} / 2 = {am_len} cm", "marks": 1},
        ],
        "hints": [
            "Perpendicular means the lines meet at $90^\\circ$.",
            "Bisector means it divides the segment into two equal halves at the midpoint.",
            f"$AM = \\frac{{{ab_len}}}{{2}} = {am_len}\\text{{ cm}}$.",
        ],
        "misconception_tags": ["perpendicular_bisector_properties", "midpoint_distance_calculation"],
    }


def arch_09_perpendicular_bisector_equidistance_property(rng: random.Random) -> Dict[str, Any]:
    """Solve for unknown side length using equidistance property PA = PB."""
    # Point P lies on perpendicular bisector of AB => PA = PB
    # PA = ax + b, PB = cx + d => solve for x and find PA
    x_val = rng.choice([3, 4, 5, 6])
    c = rng.choice([1, 2])
    a = c + rng.choice([1, 2])
    b = rng.randint(2, 8)
    d = (a - c) * x_val + b
    pa_len = a * x_val + b

    prompt = (
        f"Point $P$ lies on the **perpendicular bisector** of line segment $AB$.\n"
        f"The distances from $P$ to the endpoints are given as:\n"
        f"- $PA = {a}x + {b}\\text{{ cm}}$\n"
        f"- $PB = {c}x + {d}\\text{{ cm}}$\n\n"
        f"1. State the relationship between $PA$ and $PB$.\n"
        f"2. Solve for $x$ and calculate the **length of $PA$** in centimetres."
    )

    return {
        "subskill": "09_perpendicular_bisector_equidistance_property",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": str(pa_len),
        "sample_answer": f"{pa_len} cm (x = {x_val})",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "State equidistance property: any point on the perpendicular bisector is equidistant from endpoints (PA = PB)", "marks": 1},
            {"step": f"Set up equation: {a}x + {b} = {c}x + {d} => x = {x_val}", "marks": 1},
            {"step": f"Calculate PA: {a}({x_val}) + {b} = {pa_len} cm", "marks": 1},
        ],
        "hints": [
            "Any point on the perpendicular bisector of $AB$ is equidistant from $A$ and $B$: $PA = PB$.",
            f"Set ${a}x + {b} = {c}x + {d}$ and solve: $x = {x_val}$.",
            f"Substitute $x = {x_val}$ into $PA$: ${a}({x_val}) + {b} = {pa_len}\\text{{ cm}}$.",
        ],
        "misconception_tags": ["perpendicular_bisector_equidistance_error", "linear_equation_equidistance"],
    }


def arch_10_perpendicular_bisector_compass_radius_condition(rng: random.Random) -> Dict[str, Any]:
    """Minimum compass radius condition for perpendicular bisector (r > L/2)."""
    ab_len = rng.choice([6, 8, 10, 12, 14])
    half_len = ab_len // 2
    min_int_r = half_len + 1

    prompt = (
        f"You need to construct the perpendicular bisector of a line segment $AB$ measuring **${ab_len}\\text{{ cm}}$** "
        f"using a compass and straightedge.\n\n"
        f"What is the **minimum whole number (integer) radius** in centimetres to which the compass must be set "
        f"so that the construction arcs drawn from $A$ and $B$ will intersect?"
    )

    return {
        "subskill": "10_perpendicular_bisector_compass_radius_condition",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": str(min_int_r),
        "sample_answer": f"{min_int_r} cm (must be strictly greater than {half_len} cm)",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"State condition: compass radius must be strictly greater than half the segment length (r > AB / 2 = {half_len} cm)", "marks": 1},
            {"step": f"Identify smallest integer strictly greater than {half_len} cm: {min_int_r} cm", "marks": 1},
        ],
        "hints": [
            f"If the compass radius is less than or equal to half the length ($\\le {half_len}\\text{{ cm}}$), the arcs will never cross.",
            f"The radius must be strictly greater than half the length ($r > {half_len}\\text{{ cm}}$).",
            f"The smallest whole number greater than ${half_len}$ is **${min_int_r}\\text{{ cm}}$**.",
        ],
        "misconception_tags": ["compass_radius_condition_error", "arcs_not_intersecting_error"],
    }


def arch_11_perpendicular_line_through_point_on_line(rng: random.Random) -> Dict[str, Any]:
    """Identify the angle and steps for constructing a perpendicular at a point on a line."""
    prompt = (
        f"A point $P$ lies on a straight line $L$.\n"
        f"Using a compass, equal arcs are drawn on line $L$ on either side of $P$ at points $A$ and $B$.\n"
        f"Intersecting arcs are then drawn from $A$ and $B$ above the line meeting at point $Q$.\n\n"
        f"What is the size of the angle formed between line $L$ and line $PQ$ in degrees ($^\\circ$)?"
    )

    return {
        "subskill": "11_perpendicular_line_through_point_on_line",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": "90",
        "sample_answer": "90°",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Recognize standard construction of a perpendicular at a point on a line", "marks": 1},
            {"step": "State resulting angle is 90°", "marks": 1},
        ],
        "hints": [
            "This construction erects a perpendicular line to $L$ at point $P$.",
            "Perpendicular lines intersect at a right angle.",
            "The angle is **90°**.",
        ],
        "misconception_tags": ["perpendicular_construction_identification", "right_angle_verification"],
    }


def arch_12_perpendicular_line_from_external_point_to_line(rng: random.Random) -> Dict[str, Any]:
    """Identify the construction steps for dropping a perpendicular from an external point."""
    prompt = (
        f"To construct a perpendicular line from an external point $P$ (not on line $L$) to line $L$:\n\n"
        f"What is the first step?\n"
        f"State: **swing an arc from P cutting line L at two points**"
    )

    return {
        "subskill": "12_perpendicular_line_from_external_point_to_line",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": "swing an arc from P cutting line L at two points",
        "sample_answer": "swing an arc from P cutting line L at two points",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Identify that the compass needle is placed at P to draw an arc intersecting line L in two distinct points", "marks": 1},
            {"step": "These two points become the centres for the next intersecting arcs", "marks": 1},
        ],
        "hints": [
            "First place the compass point at the external point $P$.",
            "Adjust the radius so it is wide enough to cross line $L$ in two places.",
            "Answer: **swing an arc from P cutting line L at two points**.",
        ],
        "misconception_tags": ["external_perpendicular_construction_steps", "compass_origin_placement_error"],
    }


def arch_13_shortest_distance_from_point_to_line(rng: random.Random) -> Dict[str, Any]:
    """Calculate shortest distance from external point to line using Pythagoras."""
    # Right-angled triangle: hypotenuse, base on line, perpendicular distance h
    # Triple: (3, 4, 5) or (6, 8, 10) or (5, 12, 13)
    base, h, hyp = rng.choice([(3, 4, 5), (4, 3, 5), (6, 8, 10), (8, 6, 10), (5, 12, 13)])

    prompt = (
        f"Point $P$ is an external point located near line $L$.\n"
        f"The line segment from $P$ meeting line $L$ at an angle has a length of **${hyp}\\text{{ cm}}$**, "
        f"meeting the line **${base}\\text{{ cm}}$** away from the foot of the perpendicular.\n\n"
        f"Using the Theorem of Pythagoras, calculate the **shortest distance** from point $P$ to line $L$ "
        f"(the perpendicular distance $h$) in centimetres."
    )

    return {
        "subskill": "13_shortest_distance_from_point_to_line",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": str(h),
        "sample_answer": f"{h} cm",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Recognize that the shortest distance is the perpendicular height h", "marks": 1},
            {"step": f"Apply Pythagoras: h^2 = {hyp}^2 - {base}^2 = {hyp**2} - {base**2} = {h**2}", "marks": 1},
            {"step": f"Calculate h = √({h**2}) = {h} cm", "marks": 1},
        ],
        "hints": [
            "The shortest distance from a point to a line is the perpendicular segment.",
            f"Use Pythagoras: $h = \\sqrt{{{hyp}^2 - {base}^2}}$.",
            f"Shortest distance $= {h}\\text{{ cm}}$.",
        ],
        "misconception_tags": ["shortest_distance_perpendicular_concept", "pythagoras_leg_calculation_error"],
    }


def arch_14_equidistant_locus_of_two_parallel_lines(rng: random.Random) -> Dict[str, Any]:
    """Identify distance to equidistant parallel line midway between two parallel lines."""
    total_dist = rng.choice([6, 8, 10, 12, 16])
    mid_dist = total_dist // 2

    prompt = (
        f"Two parallel railway tracks are separated by a constant perpendicular distance of **${total_dist}\\text{{ metres}}$**.\n\n"
        f"A maintenance cable is constructed along the locus of all points that are **equidistant** from both tracks.\n"
        f"What is the distance from this cable to either track in metres?"
    )

    return {
        "subskill": "14_equidistant_locus_of_two_parallel_lines",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": str(mid_dist),
        "sample_answer": f"{mid_dist} m",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Identify that the locus of points equidistant from two parallel lines is a parallel line midway between them", "marks": 1},
            {"step": f"Calculate distance: {total_dist} / 2 = {mid_dist} metres", "marks": 1},
        ],
        "hints": [
            "Points equidistant from two parallel lines form a parallel line running straight down the middle.",
            f"Divide the total separation ${total_dist}\\text{{ m}}$ by $2$.",
            f"Distance $= {mid_dist}\\text{{ metres}}$.",
        ],
        "misconception_tags": ["parallel_locus_concept", "halving_parallel_separation"],
    }


def arch_15_construct_60_degree_angle_equilateral_triangle(rng: random.Random) -> Dict[str, Any]:
    """Identify the size of the angle constructed by swinging equal radius arcs from base."""
    seed_val = rng.randint(1000, 999999)
    svg = draw_special_angle_construction_svg(angle_deg=60, title="Equilateral Arc Construction", seed=seed_val)

    prompt = (
        f"Refer to the compass construction below where an arc of radius $R$ is drawn from vertex $V$, "
        f"and another arc of the exact same radius $R$ is drawn from point $X$ on the baseline cutting the first arc at $C$:\n\n"
        f"What is the size of the constructed angle $\\angle XVC$ in degrees ($^\\circ$)?"
    )

    return {
        "subskill": "15_construct_60_degree_angle_equilateral_triangle",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": "60",
        "sample_answer": "60°",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Recognize that equal radius arcs construct an equilateral triangle with 3 equal sides of length R", "marks": 1},
            {"step": "All angles in an equilateral triangle measure 180° / 3 = 60°", "marks": 1},
        ],
        "hints": [
            "Because all three radii are identical ($VX = XC = CV = R$), $\\triangle VXC$ is an equilateral triangle.",
            "Every interior angle of an equilateral triangle is $60^\\circ$.",
            "The angle is **60°**.",
        ],
        "misconception_tags": ["60_degree_construction_theory", "equilateral_triangle_arc_concept"],
    }


def arch_16_construct_30_degree_angle_by_bisecting_60(rng: random.Random) -> Dict[str, Any]:
    """Constructing a 30° angle by bisecting a 60° angle."""
    prompt = (
        f"To construct an angle of **$30^\\circ$** using only a compass and straightedge:\n\n"
        f"1. First construct a **$60^\\circ$** angle using equal radius arcs.\n"
        f"2. Then construct the **angle bisector** of the $60^\\circ$ angle.\n\n"
        f"State the size of each resulting angle in degrees ($^\\circ$)."
    )

    return {
        "subskill": "16_construct_30_degree_angle_by_bisecting_60",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": "30",
        "sample_answer": "30°",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "State that bisecting 60° yields 60° / 2 = 30°", "marks": 1},
        ],
        "hints": [
            "Bisecting an angle divides it into two equal halves.",
            "$60^\\circ \\div 2 = 30^\\circ$.",
            "Answer: **30°**.",
        ],
        "misconception_tags": ["30_degree_construction_process", "bisection_of_special_angles"],
    }


def arch_17_construct_90_degree_angle_perpendicular(rng: random.Random) -> Dict[str, Any]:
    """Constructing a 90° angle by erecting a perpendicular."""
    seed_val = rng.randint(1000, 999999)
    svg = draw_special_angle_construction_svg(angle_deg=90, title="90° Angle Construction", seed=seed_val)

    prompt = (
        f"When a straight angle of **$180^\\circ$** is bisected using a compass and straightedge, "
        f"a perpendicular line is formed.\n\n"
        f"What is the size of the constructed right angle in degrees ($^\\circ$)?"
    )

    return {
        "subskill": "17_construct_90_degree_angle_perpendicular",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": "90",
        "sample_answer": "90°",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Bisecting 180° yields 180° / 2 = 90°", "marks": 1},
        ],
        "hints": [
            "A straight line measures $180^\\circ$.",
            "Bisecting $180^\\circ$ gives $90^\\circ$.",
            "Answer: **90°**.",
        ],
        "misconception_tags": ["90_degree_construction_concept", "right_angle_bisection"],
    }


def arch_18_construct_45_degree_angle_by_bisecting_90(rng: random.Random) -> Dict[str, Any]:
    """Constructing a 45° angle by bisecting a 90° right angle."""
    prompt = (
        f"A learner constructs a **$90^\\circ$** right angle using a compass and straightedge, and then "
        f"bisects this right angle.\n\n"
        f"What is the size of the resulting angle in degrees ($^\\circ$)?"
    )

    return {
        "subskill": "18_construct_45_degree_angle_by_bisecting_90",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": "45",
        "sample_answer": "45°",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Bisecting 90° yields 90° / 2 = 45°", "marks": 1},
        ],
        "hints": [
            "Half of $90^\\circ$ is $45^\\circ$.",
            "Answer: **45°**.",
        ],
        "misconception_tags": ["45_degree_construction_step", "bisection_of_right_angle"],
    }


def arch_19_construct_15_degree_angle_by_bisecting_30(rng: random.Random) -> Dict[str, Any]:
    """Constructing a 15° angle by bisecting a 30° angle."""
    prompt = (
        f"To construct a **$15^\\circ$** angle without using a protractor:\n"
        f"1. Construct a $60^\\circ$ angle using equilateral triangle arcs.\n"
        f"2. Bisect $60^\\circ$ to obtain $30^\\circ$.\n"
        f"3. Bisect the $30^\\circ$ angle.\n\n"
        f"What is the size of each resulting angle in degrees ($^\\circ$)?"
    )

    return {
        "subskill": "19_construct_15_degree_angle_by_bisecting_30",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": "15",
        "sample_answer": "15°",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Bisecting 30° yields 30° / 2 = 15°", "marks": 1},
        ],
        "hints": [
            "Half of $30^\\circ$ is $15^\\circ$.",
            "Answer: **15°**.",
        ],
        "misconception_tags": ["15_degree_construction_chain", "multistep_bisection_error"],
    }


def arch_20_construct_75_degree_angle_combination(rng: random.Random) -> Dict[str, Any]:
    """Constructing 75° as 60° + 15° or 45° + 30°."""
    prompt = (
        f"A learner constructs an angle of **$75^\\circ$** using only a compass and straightedge.\n\n"
        f"Which combination of special constructed angles sums to $75^\\circ$?\n"
        f"Complete the addition: $60^\\circ + \\text{{?}}^\\circ = 75^\\circ$ (state the missing angle size)."
    )

    return {
        "subskill": "20_construct_75_degree_angle_combination",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": "15",
        "sample_answer": "15° (60° + 15° = 75°)",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Calculate missing angle: 75° - 60° = 15°", "marks": 1},
        ],
        "hints": [
            "Subtract $60^\\circ$ from $75^\\circ$.",
            "$75^\\circ - 60^\\circ = 15^\\circ$.",
            "Answer: **15**.",
        ],
        "misconception_tags": ["angle_combination_subtraction_error", "75_degree_construction_concept"],
    }


def arch_21_construct_105_degree_angle_combination(rng: random.Random) -> Dict[str, Any]:
    """Constructing 105° as 90° + 15° or 60° + 45°."""
    prompt = (
        f"An angle of **$105^\\circ$** can be constructed by combining a right angle ($90^\\circ$) with a "
        f"constructed $15^\\circ$ angle.\n\n"
        f"Calculate the sum: $90^\\circ + 15^\\circ = \\text{{?}}^\\circ$ (state the resulting angle size)."
    )

    return {
        "subskill": "21_construct_105_degree_angle_combination",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": "105",
        "sample_answer": "105°",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Sum special angles: 90° + 15° = 105°", "marks": 1},
        ],
        "hints": [
            "Add $90^\\circ$ and $15^\\circ$.",
            "$90^\\circ + 15^\\circ = 105^\\circ$.",
            "Answer: **105**.",
        ],
        "misconception_tags": ["105_degree_angle_combination", "obtuse_angle_construction_arithmetic"],
    }


def arch_22_construct_120_and_135_degree_angles(rng: random.Random) -> Dict[str, Any]:
    """Constructing 120° (2 x 60°) or 135° (90° + 45°)."""
    target = rng.choice([120, 135])
    if target == 120:
        desc = "stepping off two consecutive 60° equilateral arcs ($2 \\times 60^\\circ$)"
        ans = "120"
    else:
        desc = "adding a bisected 45° angle to a 90° right angle ($90^\\circ + 45^\\circ$)"
        ans = "135"

    prompt = (
        f"A learner constructs an angle without a protractor by {desc}.\n\n"
        f"What is the size of the constructed angle in degrees ($^\\circ$)?"
    )

    return {
        "subskill": "22_construct_120_and_135_degree_angles",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": ans,
        "sample_answer": f"{ans}°",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Calculate angle from construction description: {desc} = {ans}°", "marks": 1},
        ],
        "hints": [
            f"For 120°: $60^\\circ + 60^\\circ = 120^\\circ$.",
            f"For 135°: $90^\\circ + 45^\\circ = 135^\\circ$.",
            f"Answer: **{ans}**.",
        ],
        "misconception_tags": ["special_angle_additive_construction", "120_135_degree_construction_error"],
    }


def arch_23_triangle_inequality_theorem_validity(rng: random.Random) -> Dict[str, Any]:
    """Test whether three given side lengths can form a triangle (a + b > c)."""
    is_valid = rng.choice([True, False])
    if is_valid:
        a = rng.randint(4, 8)
        b = rng.randint(4, 8)
        # c must be between |a-b|+1 and a+b-1
        c = rng.randint(abs(a - b) + 1, a + b - 1)
        ans = "yes"
        reason = f"the sum of any two sides is strictly greater than the third side ({min(a,b)} + {max(a,b)} = {a+b} > {c})"
    else:
        a = rng.randint(2, 5)
        b = rng.randint(2, 5)
        # Violate triangle inequality: c >= a + b
        c = a + b + rng.randint(0, 3)
        ans = "no"
        reason = f"the sum of the two shorter sides ({a} + {b} = {a+b}) is not strictly greater than the longest side ({c})"

    sides = sorted([a, b, c])

    prompt = (
        f"Can a triangle be constructed with side lengths **${sides[0]}\\text{{ cm}}$**, "
        f"**${sides[1]}\\text{{ cm}}$**, and **${sides[2]}\\text{{ cm}}$**?\n\n"
        f"Answer: **yes** or **no**."
    )

    return {
        "subskill": "23_triangle_inequality_theorem_validity",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": ans,
        "sample_answer": ans,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "State Triangle Inequality Theorem: the sum of the lengths of any two sides must be strictly greater than the third side", "marks": 1},
            {"step": f"Test shorter sides: {sides[0]} + {sides[1]} = {sides[0] + sides[1]} vs {sides[2]} ({reason})", "marks": 1},
            {"step": f"State conclusion: {ans}", "marks": 1},
        ],
        "hints": [
            "According to the Triangle Inequality Theorem, $a + b > c$ for any three sides.",
            f"Add the two shorter sides: ${sides[0]} + {sides[1]} = {sides[0] + sides[1]}$.",
            f"Is ${sides[0] + sides[1]} > {sides[2]}$? {'Yes' if is_valid else 'No'}.",
        ],
        "misconception_tags": ["triangle_inequality_theorem_violation", "equal_sum_collinear_failure"],
    }


def arch_24_triangle_inequality_range_of_third_side(rng: random.Random) -> Dict[str, Any]:
    """Calculate the valid range of integer lengths for the third side of a triangle."""
    a = rng.randint(5, 9)
    b = rng.randint(10, 16)
    # Range for third side c: (b - a) < c < (b + a)
    min_c = b - a + 1
    max_c = b + a - 1
    num_possibilities = max_c - min_c + 1

    prompt = (
        f"A triangle has two sides of length **${a}\\text{{ cm}}$** and **${b}\\text{{ cm}}$**.\n\n"
        f"1. According to the Triangle Inequality Theorem, what is the **maximum possible whole number (integer) length** "
        f"for the third side in centimetres?\n"
        f"(State the maximum integer value)."
    )

    return {
        "subskill": "24_triangle_inequality_range_of_third_side",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": str(max_c),
        "sample_answer": f"{max_c} cm (range: {b - a} < c < {b + a})",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"State inequality for upper bound: third side c < {a} + {b} = {a + b} cm", "marks": 1},
            {"step": f"Identify largest integer strictly less than {a + b}: {max_c} cm", "marks": 1},
        ],
        "hints": [
            f"The third side must be strictly less than the sum of the other two sides: $c < {a} + {b} = {a + b}$.",
            f"The largest whole number strictly less than ${a + b}$ is ${max_c}$.",
            f"Maximum integer length $= {max_c}\\text{{ cm}}$.",
        ],
        "misconception_tags": ["triangle_inequality_upper_bound_inclusive_error", "strict_inequality_boundary_error"],
    }


def arch_25_construct_triangle_sss_three_sides(rng: random.Random) -> Dict[str, Any]:
    """Construct triangle given three side lengths (SSS) and calculate perimeter."""
    a = rng.choice([5, 6, 7])
    b = rng.choice([6, 7, 8])
    c = rng.choice([7, 8, 9])
    perimeter = a + b + c
    seed_val = rng.randint(1000, 999999)

    svg = draw_triangle_construction_svg(side_a=a, side_b=b, side_c=c, title="SSS Triangle Construction", seed=seed_val)

    prompt = (
        f"A triangle $\\triangle ABC$ is constructed with a compass and ruler using side lengths:\n"
        f"- $AB = {c}\\text{{ cm}}$\n"
        f"- $BC = {a}\\text{{ cm}}$\n"
        f"- $AC = {b}\\text{{ cm}}$\n\n"
        f"Calculate the **perimeter** of the constructed triangle in centimetres."
    )

    return {
        "subskill": "25_construct_triangle_sss_three_sides",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": str(perimeter),
        "sample_answer": f"{perimeter} cm",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"State perimeter formula: Perimeter = a + b + c", "marks": 1},
            {"step": f"Calculate: {a} + {b} + {c} = {perimeter} cm", "marks": 1},
        ],
        "hints": [
            "The perimeter is the sum of the lengths of all three sides.",
            f"Add: ${a} + {b} + {c} = {perimeter}\\text{{ cm}}$.",
            f"Perimeter $= {perimeter}\\text{{ cm}}$.",
        ],
        "misconception_tags": ["triangle_perimeter_sum_error", "sss_construction_properties"],
    }
