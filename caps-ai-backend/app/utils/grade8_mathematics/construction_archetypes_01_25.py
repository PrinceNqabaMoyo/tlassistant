"""Grade 8 Mathematics - Construction of Geometric Figures Archetypes (01 to 25).
Covers:
  - Bisecting lines: Compass and ruler perpendicular bisector, equidistant property.
  - Constructing perpendiculars: At a point on a line, from an external point to a line.
  - Bisecting angles: Compass arc procedure, angle calculations.
  - Special angles without protractor: 60 deg, 30 deg, 90 deg, 45 deg, 75 deg, 105 deg, 120 deg, 135 deg, 150 deg.
  - Constructing triangles: SSS, SAS, ASA, RHS, triangle inequality existence, medians and altitudes.
Strictly zero-LLM, deterministic execution parameterized by random.Random.
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict

from .construction_svg import (
    draw_angle_bisector_svg,
    draw_constructed_triangle_arcs_svg,
    draw_perp_bisector_svg,
    draw_special_angle_construction_svg,
)


# ----------------------------------------------------------------------
# 01. Perpendicular Bisector Line Segment Steps (WITH SVG)
# ----------------------------------------------------------------------
def arch_01_perpendicular_bisector_line_segment_steps(rng: random.Random) -> Dict[str, Any]:
    length_cm = rng.choice([6, 8, 10, 12])
    half_cm = length_cm // 2
    svg = draw_perp_bisector_svg(seg_name="AB", length_lbl=f"{length_cm} cm", seed=rng.randint(100, 999999))

    prompt = (
        f"In the illustration below, line segment \\(AB = {length_cm}\\) cm is bisected perpendicularly "
        f"using a compass and straight edge.\n\n"
        f"1. Explain why the compass radius must be set to more than half the length of \\(AB\\) (more than {half_cm} cm).\n"
        f"2. Describe the two points of intersection \\(P\\) and \\(Q\\) created by the compass arcs.\n"
        f"3. State what angle the bisector line \\(PQ\\) makes with line segment \\(AB\\)."
    )
    sol = (
        f"**1. Compass radius:** If the compass radius is less than or equal to half the length ({half_cm} cm), "
        f"the arcs from endpoints \\(A\\) and \\(B\\) will not intersect to form points \\(P\\) and \\(Q\\).\n\n"
        f"**2. Points P and Q:** Arcs of equal radius drawn from \\(A\\) and \\(B\\) intersect above the segment at \\(P\\) "
        f"and below the segment at \\(Q\\).\n\n"
        f"**3. Angle:** Exactly \\(90^\\circ\\) (perpendicular)."
    )
    ans = f"1. arcs will not intersect if radius <= {half_cm} cm; 2. P and Q are arc intersections above and below; 3. 90°"
    return {
        "id": f"g8_const_perp_bisect_steps_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "subskill": "01_perpendicular_bisector_line_segment_steps",
        "learning_objective_id": "math_g8_const_perp_bisect_steps",
        "hints": {
            "tier_1": "The compass radius must be greater than half of AB.",
            "tier_2": "The line joining the arc intersections forms a 90° angle at the midpoint.",
            "tier_3": f"Compass > {half_cm} cm; P and Q are intersections; angle is 90°.",
        },
        "misconception_tags": ["setting_compass_radius_too_small_so_arcs_do_not_meet"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 02. Perpendicular Bisector Equidistant Property (WITH SVG)
# ----------------------------------------------------------------------
def arch_02_perpendicular_bisector_equidistant_property(rng: random.Random) -> Dict[str, Any]:
    pa = rng.choice([5, 7, 9, 11])
    svg = draw_perp_bisector_svg(seg_name="CD", seed=rng.randint(100, 999999))

    prompt = (
        f"A point \\(P\\) lies on the perpendicular bisector of segment \\(CD\\).\n"
        f"The distance from point \\(P\\) to endpoint \\(C\\) is **{pa} cm**.\n\n"
        f"1. State the fundamental geometric equidistant property of any point on a perpendicular bisector.\n"
        f"2. What is the distance from point \\(P\\) to endpoint \\(D\\)?"
    )
    sol = (
        f"**1. Equidistant Property:** Any point on the perpendicular bisector of a line segment is "
        f"equidistant (at an equal distance) from the two endpoints of the segment.\n\n"
        f"**2. Distance PD:** \\(PD = PC = {pa}\\) cm."
    )
    ans = f"1. equidistant from endpoints; 2. {pa} cm"
    return {
        "id": f"g8_const_equidist_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "02_perpendicular_bisector_equidistant_property",
        "learning_objective_id": "math_g8_const_equidist",
        "hints": {
            "tier_1": "Points on the perpendicular bisector are equidistant from the endpoints.",
            "tier_2": f"Distance PD must equal distance PC = {pa} cm.",
            "tier_3": f"Equidistant from endpoints; PD = {pa} cm.",
        },
        "misconception_tags": ["assuming_distances_to_endpoints_are_different"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 03. Perpendicular Line At Point On Line (ZERO LEAK TRIGGERS)
# ----------------------------------------------------------------------
def arch_03_perpendicular_line_at_point_on_line(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Consider a point \\(P\\) located directly on a straight horizontal line \\(AB\\):\n\n"
        f"1. Describe the first step using a compass centered at point \\(P\\).\n"
        f"2. How are the two intersection points on line \\(AB\\) then used to construct the perpendicular line?"
    )
    sol = (
        f"**Step 1:** With the compass point at \\(P\\), draw two arcs with equal radius cutting line \\(AB\\) on either side of \\(P\\) at points \\(X\\) and \\(Y\\).\n\n"
        f"**Step 2:** Open the compass wider than \\(PX\\). Place the compass point at \\(X\\) and draw an arc above the line. "
        f"With the same radius, place the compass at \\(Y\\) and draw an intersecting arc at point \\(Q\\). "
        f"Draw a straight line connecting \\(Q\\) to \\(P\\). Line \\(PQ \\perp AB\\)."
    )
    ans = "1. swing equal arcs on either side of P at X and Y; 2. draw intersecting arcs from X and Y, connect intersection to P"
    return {
        "id": f"g8_const_perp_at_pt_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "subskill": "03_perpendicular_line_at_point_on_line",
        "learning_objective_id": "math_g8_const_perp_at_pt",
        "hints": {
            "tier_1": "Center compass at P and mark equal distances on either side.",
            "tier_2": "Then construct the perpendicular bisector of the two marks.",
            "tier_3": "Swing arcs at X and Y, then intersect arcs above and draw line to P.",
        },
        "misconception_tags": ["using_a_protractor_when_asked_for_compass_construction"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 04. Perpendicular Line From External Point To Line (ZERO LEAK TRIGGERS)
# ----------------------------------------------------------------------
def arch_04_perpendicular_line_from_external_point_to_line(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A point \\(C\\) is given lying outside (above) a straight line \\(AB\\):\n\n"
        f"1. Explain how to use a compass centered at external point \\(C\\) to mark two points on line \\(AB\\).\n"
        f"2. How do you complete the perpendicular line from point \\(C\\) to line \\(AB\\)?"
    )
    sol = (
        f"**Step 1:** Place the compass point at external point \\(C\\). Open the compass wide enough to cut line \\(AB\\) in two distinct points \\(X\\) and \\(Y\\).\n\n"
        f"**Step 2:** From \\(X\\) and \\(Y\\), draw two intersecting arcs on the opposite side of line \\(AB\\) at point \\(D\\). "
        f"Use a straight edge to draw line \\(CD\\). Line \\(CD\\) is perpendicular to line \\(AB\\)."
    )
    ans = "1. compass at C cuts line AB at two points X and Y; 2. draw intersecting arcs below AB from X and Y, connect C to intersection"
    return {
        "id": f"g8_const_perp_ext_pt_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "subskill": "04_perpendicular_line_from_external_point_to_line",
        "learning_objective_id": "math_g8_const_perp_ext_pt",
        "hints": {
            "tier_1": "Open compass from C so it crosses AB in two places.",
            "tier_2": "Intersect arcs on the other side of line AB.",
            "tier_3": "Connect C to the arc intersection to make a 90° altitude.",
        },
        "misconception_tags": ["eyeballing_perpendicular_without_compass_arcs"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 05. Angle Bisector Construction Steps (WITH SVG)
# ----------------------------------------------------------------------
def arch_05_angle_bisector_construction_steps(rng: random.Random) -> Dict[str, Any]:
    ang = rng.choice([50, 60, 70, 80])
    svg = draw_angle_bisector_svg(angle_deg=ang, seed=rng.randint(100, 999999))

    prompt = (
        f"In the illustration below, an angle \\(\\angle ABC = {ang}^\\circ\\) is bisected by ray \\(BD\\).\n\n"
        f"1. Describe the purpose of the initial arc drawn with compass point at vertex \\(B\\).\n"
        f"2. How is point \\(D\\) constructed using compass arcs?\n"
        f"3. What is the size of each halved angle?"
    )
    half_ang = ang // 2
    sol = (
        f"**1. Initial arc:** To mark points at an equal distance from vertex \\(B\\) on both arms of the angle.\n\n"
        f"**2. Point D:** Place the compass point at the two arm intersections and draw two arcs of equal radius inside the angle. "
        f"Their intersection point is \\(D\\).\n\n"
        f"**3. Size:** Each halved angle measures \\(\\frac{{{ang}^\\circ}}{{2}} = {half_ang}^\\circ\\)."
    )
    ans = f"1. mark equal distances on arms; 2. intersecting arcs inside angle from arm points; 3. {half_ang}°"
    return {
        "id": f"g8_const_ang_bisect_steps_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "subskill": "05_angle_bisector_construction_steps",
        "learning_objective_id": "math_g8_const_ang_bisect_steps",
        "hints": {
            "tier_1": "An angle bisector divides the angle into two equal parts.",
            "tier_2": f"{ang}° ÷ 2 = {half_ang}°.",
            "tier_3": f"Initial arc marks equal arm points; arcs cross at D; each half is {half_ang}°.",
        },
        "misconception_tags": ["changing_compass_radius_between_the_two_interior_arcs"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 06. Angle Bisector Calculate Halved Angles (WITH SVG)
# ----------------------------------------------------------------------
def arch_06_angle_bisector_calculate_halved_angles(rng: random.Random) -> Dict[str, Any]:
    ang = rng.choice([48, 54, 68, 76, 84, 110])
    half = ang // 2
    svg = draw_angle_bisector_svg(angle_deg=ang, seed=rng.randint(100, 999999))

    prompt = (
        f"An angle of **{ang}^\\circ** is accurately bisected into two angles \\(x\\) and \\(y\\) using a compass construction.\n\n"
        f"1. Define what it means to **bisect** an angle.\n"
        f"2. Calculate the size of angle \\(x\\) and angle \\(y\\) in degrees."
    )
    sol = (
        f"**1. Definition:** To bisect an angle means to divide it into two exactly equal halves.\n\n"
        f"**2. Calculation:**\n"
        f"\\[ x = y = \\frac{{{ang}^\\circ}}{{2}} = {half}^\\circ \\]"
    )
    ans = f"1. divide into two equal angles; 2. x = y = {half}°"
    return {
        "id": f"g8_const_halved_ang_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "06_angle_bisector_calculate_halved_angles",
        "learning_objective_id": "math_g8_const_halved_ang",
        "hints": {
            "tier_1": "Bisecting divides an angle exactly in half.",
            "tier_2": f"{ang}° / 2.",
            "tier_3": f"{half}°.",
        },
        "misconception_tags": ["confusing_bisect_with_trisect"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 07. Construct 60 Degree Angle Without Protractor (WITH SVG)
# ----------------------------------------------------------------------
def arch_07_construct_60_degree_angle_without_protractor(rng: random.Random) -> Dict[str, Any]:
    svg = draw_special_angle_construction_svg(angle_deg=60, seed=rng.randint(100, 999999))

    prompt = (
        f"To construct an angle of **60^\\circ** without using a protractor:\n\n"
        f"1. Explain why this construction is based on the properties of an equilateral triangle.\n"
        f"2. State the key rule regarding the compass radius when drawing the second arc from the baseline."
    )
    sol = (
        f"**1. Equilateral triangle:** An equilateral triangle has three equal sides and each interior angle is \\(60^\\circ\\). "
        f"By using the same compass radius for the base and both intersecting arcs, an equilateral triangle is formed.\n\n"
        f"**2. Compass radius:** The compass radius must **remain unchanged** (the exact same radius) when drawing the arc from the baseline point."
    )
    ans = "1. forms an equilateral triangle where each angle is 60°; 2. compass radius must remain unchanged"
    return {
        "id": f"g8_const_60_deg_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "07_construct_60_degree_angle_without_protractor",
        "learning_objective_id": "math_g8_const_60_deg",
        "hints": {
            "tier_1": "All angles in an equilateral triangle are 60°.",
            "tier_2": "Keep the compass width unchanged from the initial radius.",
            "tier_3": "Equilateral triangle property; compass radius stays constant.",
        },
        "misconception_tags": ["changing_compass_radius_when_constructing_60_degrees"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 08. Construct 30 Degree Angle By Bisecting 60 (WITH SVG)
# ----------------------------------------------------------------------
def arch_08_construct_30_degree_angle_by_bisecting_60(rng: random.Random) -> Dict[str, Any]:
    svg = draw_special_angle_construction_svg(angle_deg=30, seed=rng.randint(100, 999999))

    prompt = (
        f"To construct an accurate **30^\\circ** angle with a compass and straight edge:\n\n"
        f"1. What special angle must be constructed first?\n"
        f"2. What construction procedure is applied to that initial angle to obtain \\(30^\\circ\\)?"
    )
    sol = (
        f"**1. First angle:** Construct a **60^\\circ** angle using the equilateral triangle arc method.\n\n"
        f"**2. Procedure:** Bisect the \\(60^\\circ\\) angle using the angle bisector compass construction "
        f"(\\(\\frac{{60^\\circ}}{{2}} = 30^\\circ\\))."
    )
    ans = "1. 60° angle; 2. bisect the 60° angle"
    return {
        "id": f"g8_const_30_deg_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "08_construct_30_degree_angle_by_bisecting_60",
        "learning_objective_id": "math_g8_const_30_deg",
        "hints": {
            "tier_1": "30° is half of 60°.",
            "tier_2": "Construct 60° first, then bisect it.",
            "tier_3": "Construct 60°, then bisect.",
        },
        "misconception_tags": ["trying_to_construct_30_degrees_directly_without_60"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 09. Construct 90 Degree Angle Using Perpendicular (WITH SVG)
# ----------------------------------------------------------------------
def arch_09_construct_90_degree_angle_using_perpendicular(rng: random.Random) -> Dict[str, Any]:
    svg = draw_special_angle_construction_svg(angle_deg=90, seed=rng.randint(100, 999999))

    prompt = (
        f"To construct a right angle (**90^\\circ**) without a protractor on a baseline:\n\n"
        f"1. Explain how a \\(90^\\circ\\) angle is obtained by bisecting a straight angle (\\(180^\\circ\\)).\n"
        f"2. Give another method using a perpendicular line construction."
    )
    sol = (
        f"**1. Bisecting straight angle:** A straight line forms an angle of \\(180^\\circ\\). Constructing the perpendicular "
        f"bisector at a point on the line divides \\(180^\\circ\\) into two right angles of \\(\\frac{{180^\\circ}}{{2}} = 90^\\circ\\).\n\n"
        f"**2. Alternative method:** Construct a \\(60^\\circ\\) angle, then construct the adjacent \\(60^\\circ\\) angle (total \\(120^\\circ\\)), "
        f"and bisect the second \\(60^\\circ\\) angle (\\(60^\\circ + 30^\\circ = 90^\\circ\\))."
    )
    ans = "1. bisecting 180° straight angle gives 90°; 2. 60° + bisect second 60° (60° + 30° = 90°)"
    return {
        "id": f"g8_const_90_deg_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "09_construct_90_degree_angle_using_perpendicular",
        "learning_objective_id": "math_g8_const_90_deg",
        "hints": {
            "tier_1": "180° / 2 = 90°.",
            "tier_2": "Perpendicular to straight line creates 90°.",
            "tier_3": "Bisect 180° or construct 60° + 30°.",
        },
        "misconception_tags": ["confusing_perpendicular_with_parallel"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 10. Construct 45 Degree Angle By Bisecting 90 (WITH SVG)
# ----------------------------------------------------------------------
def arch_10_construct_45_degree_angle_by_bisecting_90(rng: random.Random) -> Dict[str, Any]:
    svg = draw_special_angle_construction_svg(angle_deg=45, seed=rng.randint(100, 999999))

    prompt = (
        f"To construct an angle of **45^\\circ** without a protractor:\n\n"
        f"1. What angle must be constructed first?\n"
        f"2. Explain how to obtain \\(45^\\circ\\) from that angle."
    )
    sol = (
        f"**1. First angle:** Construct a **90^\\circ** angle (perpendicular line).\n\n"
        f"**2. Explanation:** Bisect the \\(90^\\circ\\) angle using compass arcs to obtain \\(\\frac{{90^\\circ}}{{2}} = 45^\\circ\\)."
    )
    ans = "1. 90° angle; 2. bisect the 90° angle"
    return {
        "id": f"g8_const_45_deg_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "10_construct_45_degree_angle_by_bisecting_90",
        "learning_objective_id": "math_g8_const_45_deg",
        "hints": {
            "tier_1": "45° is half of 90°.",
            "tier_2": "Construct 90° first, then bisect it.",
            "tier_3": "Construct 90°, then bisect.",
        },
        "misconception_tags": ["halving_60_instead_of_90"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 11. Construct 75 Degree Angle Composite (ZERO LEAK TRIGGERS)
# ----------------------------------------------------------------------
def arch_11_construct_75_degree_angle_composite(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Describe the geometric strategy to construct an angle of **75^\\circ** without a protractor:\n\n"
        f"1. Which two standard angles (60° and 90°) lie on either side of 75°?\n"
        f"2. Explain how bisecting the \\(30^\\circ\\) interval between \\(60^\\circ\\) and \\(90^\\circ\\) yields \\(75^\\circ\\)."
    )
    sol = (
        f"**1. Two angles:** Construct a \\(60^\\circ\\) angle and a \\(90^\\circ\\) angle on the same vertex and baseline.\n\n"
        f"**2. Bisecting the interval:** The angle between \\(60^\\circ\\) and \\(90^\\circ\\) is \\(90^\\circ - 60^\\circ = 30^\\circ\\). "
        f"Bisecting this \\(30^\\circ\\) region gives \\(15^\\circ\\). "
        f"Adding this \\(15^\\circ\\) to \\(60^\\circ\\) gives \\(60^\\circ + 15^\\circ = 75^\\circ\\)."
    )
    ans = "1. 60° and 90°; 2. bisect the 30° difference to get 15°, 60° + 15° = 75°"
    return {
        "id": f"g8_const_75_deg_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "subskill": "11_construct_75_degree_angle_composite",
        "learning_objective_id": "math_g8_const_75_deg",
        "hints": {
            "tier_1": "75° = 60° + 15°.",
            "tier_2": "15° is half of the 30° interval between 60° and 90°.",
            "tier_3": "Construct 60° and 90°, bisect between them to add 15°.",
        },
        "misconception_tags": ["adding_45_and_60"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 12. Construct 105 Degree Angle Composite (ZERO LEAK TRIGGERS)
# ----------------------------------------------------------------------
def arch_12_construct_105_degree_angle_composite(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Describe how to construct an angle of **105^\\circ** without using a protractor:\n\n"
        f"1. Express \\(105^\\circ\\) as the sum of \\(90^\\circ\\) and another angle.\n"
        f"2. Explain how that additional angle is constructed from a \\(120^\\circ\\) arc."
    )
    sol = (
        f"**1. Sum formulation:** \\(105^\\circ = 90^\\circ + 15^\\circ\\) (or \\(180^\\circ - 75^\\circ\\)).\n\n"
        f"**2. Construction:** Construct a \\(90^\\circ\\) angle and a \\(120^\\circ\\) angle on the same vertex. "
        f"The interval between \\(90^\\circ\\) and \\(120^\\circ\\) is \\(30^\\circ\\). "
        f"Bisecting this \\(30^\\circ\\) gives \\(15^\\circ\\). "
        f"\\[ 90^\\circ + 15^\\circ = 105^\\circ \\]"
    )
    ans = "1. 90° + 15°; 2. bisect the 30° interval between 90° and 120°"
    return {
        "id": f"g8_const_105_deg_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "12_construct_105_degree_angle_composite",
        "learning_objective_id": "math_g8_const_105_deg",
        "hints": {
            "tier_1": "105° = 90° + 15°.",
            "tier_2": "The 15° comes from bisecting the 30° between 90° and 120°.",
            "tier_3": "90° + 15° = 105°.",
        },
        "misconception_tags": ["confusing_105_with_115"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 13. Construct 120 Degree Angle Double Arc (ZERO LEAK TRIGGERS)
# ----------------------------------------------------------------------
def arch_13_construct_120_degree_angle_double_arc(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Explain how to construct an angle of **120^\\circ** without using a protractor:\n\n"
        f"1. Explain how two successive \\(60^\\circ\\) compass arcs along the same radius arc produce \\(120^\\circ\\).\n"
        f"2. Confirm that \\(120^\\circ\\) is the supplement of \\(60^\\circ\\)."
    )
    sol = (
        f"**1. Two successive 60° arcs:** Draw a large arc from the vertex cutting the baseline. "
        f"Keeping the same radius, step off one arc (\\(60^\\circ\\)), and from that point step off a second arc along the circle. "
        f"The second arc is \\(60^\\circ + 60^\\circ = 120^\\circ\\).\n\n"
        f"**2. Supplement:** \\(180^\\circ - 60^\\circ = 120^\\circ\\)."
    )
    ans = "1. two successive 60° arcs (60° + 60° = 120°); 2. 180° - 60° = 120°"
    return {
        "id": f"g8_const_120_deg_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "13_construct_120_degree_angle_double_arc",
        "learning_objective_id": "math_g8_const_120_deg",
        "hints": {
            "tier_1": "120° = 2 × 60°.",
            "tier_2": "Step off two 60° arcs with the compass.",
            "tier_3": "Two successive 60° arcs; 180° - 60° = 120°.",
        },
        "misconception_tags": ["changing_compass_radius_between_the_two_arcs"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 14. Construct 135 Degree Angle Composite (ZERO LEAK TRIGGERS)
# ----------------------------------------------------------------------
def arch_14_construct_135_degree_angle_composite(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"To construct an obtuse angle of **135^\\circ** without a protractor:\n\n"
        f"1. Express \\(135^\\circ\\) as \\(90^\\circ + \\dots\\)\n"
        f"2. Explain how to obtain that remaining angle by bisecting the adjacent right angle."
    )
    sol = (
        f"**1. Expression:** \\(135^\\circ = 90^\\circ + 45^\\circ\\).\n\n"
        f"**2. Explanation:** At a point on a line, erect a perpendicular (\\(90^\\circ\\)). "
        f"The other adjacent supplementary angle is also \\(90^\\circ\\). "
        f"Bisecting that second \\(90^\\circ\\) angle gives \\(45^\\circ\\). "
        f"\\[ 90^\\circ + 45^\\circ = 135^\\circ \\]"
    )
    ans = "1. 90° + 45°; 2. bisect the second adjacent 90° right angle"
    return {
        "id": f"g8_const_135_deg_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "14_construct_135_degree_angle_composite",
        "learning_objective_id": "math_g8_const_135_deg",
        "hints": {
            "tier_1": "135° = 90° + 45°.",
            "tier_2": "Bisect the supplementary 90° angle.",
            "tier_3": "90° + 45° = 135°.",
        },
        "misconception_tags": ["subtracting_45_from_90_instead_of_adding"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 15. Construct 150 Degree Angle Composite (ZERO LEAK TRIGGERS)
# ----------------------------------------------------------------------
def arch_15_construct_150_degree_angle_composite(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Describe how to construct an angle of **150^\\circ** without using a protractor:\n\n"
        f"1. What is the supplementary angle to \\(150^\\circ\\)?\n"
        f"2. Explain how constructing a \\(30^\\circ\\) angle on a straight line produces an interior \\(150^\\circ\\) angle."
    )
    sol = (
        f"**1. Supplementary angle:** \\(180^\\circ - 150^\\circ = 30^\\circ\\).\n\n"
        f"**2. Construction:** On a straight line (\\(180^\\circ\\)), construct a \\(30^\\circ\\) angle at the vertex "
        f"(by constructing \\(60^\\circ\\) and bisecting it). "
        f"The remaining obtuse angle on the straight line will measure \\(180^\\circ - 30^\\circ = 150^\\circ\\)."
    )
    ans = "1. 30°; 2. construct 30° on straight line, remaining angle is 180° - 30° = 150°"
    return {
        "id": f"g8_const_150_deg_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "15_construct_150_degree_angle_composite",
        "learning_objective_id": "math_g8_const_150_deg",
        "hints": {
            "tier_1": "150° and 30° lie on a straight line (supplementary).",
            "tier_2": "Construct 30° (half of 60°). The other angle is 150°.",
            "tier_3": "30°; 180° - 30° = 150°.",
        },
        "misconception_tags": ["adding_60_and_60_only_gets_120"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 16. Triangle Inequality Theorem Existence (ZERO LEAK TRIGGERS)
# ----------------------------------------------------------------------
def arch_16_triangle_inequality_theorem_existence(rng: random.Random) -> Dict[str, Any]:
    is_valid = rng.choice([True, False])
    if is_valid:
        a = rng.choice([5, 6, 7])
        b = rng.choice([8, 9, 10])
        c = rng.choice([10, 11, 12])
        if a + b <= c:
            c = a + b - 1
    else:
        a = rng.choice([3, 4, 5])
        b = rng.choice([4, 5, 6])
        c = a + b + rng.choice([1, 2, 3])

    prompt = (
        f"A learner attempts to construct a triangle with side lengths **{a} cm**, **{b} cm**, and **{c} cm**:\n\n"
        f"1. State the **Triangle Inequality Theorem** in words.\n"
        f"2. Can this triangle be constructed? (Answer 'Yes' or 'No')\n"
        f"3. Justify your answer using the sum of the two shorter sides."
    )
    s1, s2 = sorted([a, b, c])[:2]
    longest = max(a, b, c)
    sum_short = s1 + s2
    if is_valid:
        sol = (
            f"**1. Theorem:** In any triangle, the sum of the lengths of any two sides must be strictly greater than the third side.\n\n"
            f"**2. Can it be constructed:** Yes.\n\n"
            f"**3. Justification:** Sum of shorter sides \\({s1} + {s2} = {sum_short}\\) cm, "
            f"which is greater than longest side \\({longest}\\) cm (\\({sum_short} > {longest}\\))."
        )
        ans = f"1. sum of any two sides > third side; 2. Yes; 3. {s1} + {s2} = {sum_short} > {longest}"
    else:
        sol = (
            f"**1. Theorem:** In any triangle, the sum of the lengths of any two sides must be strictly greater than the third side.\n\n"
            f"**2. Can it be constructed:** No.\n\n"
            f"**3. Justification:** Sum of shorter sides \\({s1} + {s2} = {sum_short}\\) cm, "
            f"which is NOT greater than longest side \\({longest}\\) cm (\\({sum_short} \\le {longest}\\)). The compass arcs will not intersect."
        )
        ans = f"1. sum of any two sides > third side; 2. No; 3. {s1} + {s2} = {sum_short} <= {longest}"

    return {
        "id": f"g8_const_tri_ineq_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "subskill": "16_triangle_inequality_theorem_existence",
        "learning_objective_id": "math_g8_const_tri_ineq",
        "hints": {
            "tier_1": "Sum of the two shorter sides must be greater than the longest side.",
            "tier_2": f"Compare {s1} + {s2} = {sum_short} with {longest}.",
            "tier_3": f"{ans}.",
        },
        "misconception_tags": ["thinking_any_three_lengths_can_form_a_triangle"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 17. Construct Triangle SSS Condition (WITH SVG)
# ----------------------------------------------------------------------
def arch_17_construct_triangle_sss_condition(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([6, 7, 8])
    b = rng.choice([5, 6, 7])
    c = rng.choice([8, 9, 10])

    svg = draw_constructed_triangle_arcs_svg(f"{a} cm", f"{b} cm", f"{c} cm", seed=rng.randint(100, 999999))

    prompt = (
        f"In the illustration below, \\(\\triangle ABC\\) is constructed given three side lengths: "
        f"\\(BC = {a}\\) cm, \\(AC = {b}\\) cm, and \\(AB = {c}\\) cm.\n\n"
        f"1. Which side is best drawn first as the baseline using a ruler?\n"
        f"2. How are the compass arcs from vertices \\(B\\) and \\(C\\) used to locate vertex \\(A\\)?\n"
        f"3. State the condition of construction (SSS, SAS, or AAS)."
    )
    sol = (
        f"**1. Baseline:** Draw base \\(BC = {a}\\) cm (or any of the three sides) with a ruler.\n\n"
        f"**2. Locating vertex A:** Open the compass to radius \\({c}\\) cm and draw an arc centered at \\(B\\). "
        f"Open the compass to radius \\({b}\\) cm and draw an arc centered at \\(C\\). "
        f"Their intersection marks vertex \\(A\\).\n\n"
        f"**3. Condition:** SSS (Side-Side-Side)."
    )
    ans = f"1. BC = {a} cm; 2. arc radius {c} cm from B and arc radius {b} cm from C intersect at A; 3. SSS"
    return {
        "id": f"g8_const_tri_sss_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "subskill": "17_construct_triangle_sss_condition",
        "learning_objective_id": "math_g8_const_tri_sss",
        "hints": {
            "tier_1": "Draw the base with a ruler, then use compass arcs for the other two sides.",
            "tier_2": "Intersection of the two arcs locates the third vertex.",
            "tier_3": "Baseline first; compass arcs intersect at A; SSS.",
        },
        "misconception_tags": ["measuring_slanted_sides_with_ruler_instead_of_compass"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 18. Construct Triangle SAS Condition (ZERO LEAK TRIGGERS)
# ----------------------------------------------------------------------
def arch_18_construct_triangle_sas_condition(rng: random.Random) -> Dict[str, Any]:
    b = rng.choice([6, 7, 8])
    c = rng.choice([5, 6, 7])
    ang = rng.choice([50, 60, 70])

    prompt = (
        f"A learner constructs \\(\\triangle ABC\\) given two sides \\(AB = {c}\\) cm, \\(BC = {b}\\) cm, "
        f"and included angle \\(\\hat{{B}} = {ang}^\\circ\\):\n\n"
        f"1. What is the first step in the construction?\n"
        f"2. How is angle \\(\\hat{{B}}\\) positioned relative to the two sides?\n"
        f"3. State the condition of construction."
    )
    sol = (
        f"**1. Step 1:** Draw base line segment \\(BC = {b}\\) cm using a ruler.\n\n"
        f"**2. Angle position:** Construct an angle of \\({ang}^\\circ\\) at vertex \\(B\\), then measure along this arm a length of \\({c}\\) cm to locate vertex \\(A\\). "
        f"Finally join \\(A\\) to \\(C\\).\n\n"
        f"**3. Condition:** SAS (Side-Angle-Side; two sides and included angle)."
    )
    ans = f"1. draw base BC = {b} cm; 2. construct {ang}° at B, mark AB = {c} cm; 3. SAS"
    return {
        "id": f"g8_const_tri_sas_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "subskill": "18_construct_triangle_sas_condition",
        "learning_objective_id": "math_g8_const_tri_sas",
        "hints": {
            "tier_1": "Draw one side, construct the angle at the vertex, then mark the second side.",
            "tier_2": "The angle must be included between the two given sides.",
            "tier_3": "Base BC; angle at B; SAS.",
        },
        "misconception_tags": ["putting_the_angle_at_the_wrong_vertex"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 19. Construct Triangle ASA Condition (ZERO LEAK TRIGGERS)
# ----------------------------------------------------------------------
def arch_19_construct_triangle_asa_condition(rng: random.Random) -> Dict[str, Any]:
    base = rng.choice([7, 8, 9, 10])
    b_ang = rng.choice([40, 50, 60])
    c_ang = rng.choice([50, 60, 70])
    a_ang = 180 - (b_ang + c_ang)

    prompt = (
        f"To construct \\(\\triangle ABC\\) given base \\(BC = {base}\\) cm and base angles "
        f"\\(\\hat{{B}} = {b_ang}^\\circ\\) and \\(\\hat{{C}} = {c_ang}^\\circ\\):\n\n"
        f"1. What is the size of the third vertex angle \\(\\hat{{A}}\\)?\n"
        f"2. Explain how the intersection of the two angle rays at \\(B\\) and \\(C\\) uniquely determines vertex \\(A\\).\n"
        f"3. State the condition of construction."
    )
    sol = (
        f"**1. Third angle:**\n"
        f"\\[ \\hat{{A}} = 180^\\circ - ({b_ang}^\\circ + {c_ang}^\\circ) = {a_ang}^\\circ \\quad (\\text{{sum of }}\\angle\\text{{s in }}\\triangle) \\]\n\n"
        f"**2. Determining vertex A:** Drawing rays from \\(B\\) at \\({b_ang}^\\circ\\) and from \\(C\\) at \\({c_ang}^\\circ\\) "
        f"causes them to intersect at exactly one unique point, which is vertex \\(A\\).\n\n"
        f"**3. Condition:** ASA (Angle-Side-Angle) or AAS."
    )
    ans = f"1. A = {a_ang}°; 2. the two rays intersect at a unique point A; 3. ASA (or AAS)"
    return {
        "id": f"g8_const_tri_asa_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "subskill": "19_construct_triangle_asa_condition",
        "learning_objective_id": "math_g8_const_tri_asa",
        "hints": {
            "tier_1": "Draw the base line first, then construct the two angles at each end.",
            "tier_2": f"Third angle = 180° - ({b_ang}° + {c_ang}°) = {a_ang}°.",
            "tier_3": f"{a_ang}°; rays intersect at A; ASA.",
        },
        "misconception_tags": ["measuring_angles_from_the_wrong_direction_on_the_baseline"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 20. Construct Triangle RHS Condition (ZERO LEAK TRIGGERS)
# ----------------------------------------------------------------------
def arch_20_construct_triangle_rhs_condition(rng: random.Random) -> Dict[str, Any]:
    leg = rng.choice([6, 8])
    hyp = rng.choice([10, 12])

    prompt = (
        f"To construct right-angled \\(\\triangle PQR\\) with \\(\\hat{{Q}} = 90^\\circ\\), "
        f"leg \\(QR = {leg}\\) cm, and hypotenuse \\(PR = {hyp}\\) cm:\n\n"
        f"1. Draw base \\(QR = {leg}\\) cm and erect a perpendicular line at vertex \\(Q\\).\n"
        f"2. How is a compass used from vertex \\(R\\) to locate vertex \\(P\\) on the perpendicular ray?\n"
        f"3. State the construction condition."
    )
    sol = (
        f"**1. Step 1:** Draw \\(QR = {leg}\\) cm and construct a \\(90^\\circ\\) perpendicular ray upwards from \\(Q\\).\n\n"
        f"**2. Locating P:** Set the compass to radius \\({hyp}\\) cm (the hypotenuse). "
        f"Place the compass point at \\(R\\) and swing an arc cutting the perpendicular ray. "
        f"The intersection point is vertex \\(P\\).\n\n"
        f"**3. Condition:** RHS (Right-angle, Hypotenuse, Side)."
    )
    ans = f"1. draw QR and erect perpendicular at Q; 2. arc radius {hyp} cm from R cuts perpendicular at P; 3. RHS"
    return {
        "id": f"g8_const_tri_rhs_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "subskill": "20_construct_triangle_rhs_condition",
        "learning_objective_id": "math_g8_const_tri_rhs",
        "hints": {
            "tier_1": "Construct the 90° angle at Q first.",
            "tier_2": f"Swing compass arc of radius {hyp} cm from R.",
            "tier_3": "Perpendicular at Q; compass arc of hyp from R; RHS.",
        },
        "misconception_tags": ["swinging_the_hypotenuse_arc_from_Q_instead_of_R"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 21. Identify Construction Arcs In Diagram (WITH SVG)
# ----------------------------------------------------------------------
def arch_21_identify_construction_arcs_in_diagram(rng: random.Random) -> Dict[str, Any]:
    svg = draw_perp_bisector_svg(seg_name="XY", length_lbl="8 cm", seed=rng.randint(100, 999999))

    prompt = (
        f"Examine the construction markings in the illustration below.\n\n"
        f"1. Identify the geometric construction shown.\n"
        f"2. What two properties does line \\(PQ\\) satisfy with respect to segment \\(XY\\)?"
    )
    sol = (
        f"**1. Construction:** The perpendicular bisector of line segment \\(XY\\).\n\n"
        f"**2. Two properties:**\n"
        f"1. It is perpendicular to \\(XY\\) (forms \\(90^\\circ\\) angles).\n"
        f"2. It bisects \\(XY\\) into two equal halves at its midpoint."
    )
    ans = "1. perpendicular bisector; 2. perpendicular (90°) and bisects (cuts in half)"
    return {
        "id": f"g8_const_identify_arcs_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "21_identify_construction_arcs_in_diagram",
        "learning_objective_id": "math_g8_const_identify_arcs",
        "hints": {
            "tier_1": "Arcs above and below a segment indicate a perpendicular bisector.",
            "tier_2": "It divides the segment into two equal halves at right angles.",
            "tier_3": "Perpendicular bisector; perpendicular and bisects.",
        },
        "misconception_tags": ["calling_it_an_angle_bisector"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 22. Construct Equilateral Triangle Given One Side (WITH SVG)
# ----------------------------------------------------------------------
def arch_22_construct_equilateral_triangle_given_one_side(rng: random.Random) -> Dict[str, Any]:
    s = rng.choice([5, 6, 7, 8])
    svg = draw_constructed_triangle_arcs_svg(f"{s} cm", f"{s} cm", f"{s} cm", seed=rng.randint(100, 999999))

    prompt = (
        f"In the illustration below, an equilateral triangle \\(\\triangle ABC\\) has side length **{s} cm**.\n\n"
        f"1. Explain how a compass set to **{s} cm** is used from endpoints \\(B\\) and \\(C\\) to construct vertex \\(A\\).\n"
        f"2. What is the measured size of each interior angle in the completed triangle?"
    )
    sol = (
        f"**1. Compass procedure:** Draw base \\(BC = {s}\\) cm with a ruler. Open the compass to \\({s}\\) cm. "
        f"Draw an arc centered at \\(B\\), then with the same radius draw an arc centered at \\(C\\). "
        f"Their intersection locates vertex \\(A\\). Connect \\(A\\) to \\(B\\) and \\(C\\).\n\n"
        f"**2. Interior angles:** Each interior angle measures \\(60^\\circ\\)."
    )
    ans = f"1. draw arcs of radius {s} cm from B and C; 2. 60°"
    return {
        "id": f"g8_const_equi_tri_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "22_construct_equilateral_triangle_given_one_side",
        "learning_objective_id": "math_g8_const_equi_tri",
        "hints": {
            "tier_1": "All 3 sides equal s cm, all 3 angles equal 60°.",
            "tier_2": f"Keep compass at {s} cm for both arcs.",
            "tier_3": f"Arcs of {s} cm from B and C; angles are 60°.",
        },
        "misconception_tags": ["changing_compass_radius_between_the_two_vertices"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 23. Construct Isosceles Triangle Given Base And Equal Sides (WITH SVG)
# ----------------------------------------------------------------------
def arch_23_construct_isosceles_triangle_given_base_and_equal_sides(rng: random.Random) -> Dict[str, Any]:
    base = rng.choice([6, 8, 10])
    side = rng.choice([7, 9, 11])
    svg = draw_constructed_triangle_arcs_svg(f"{base} cm", f"{side} cm", f"{side} cm", seed=rng.randint(100, 999999))

    prompt = (
        f"In the illustration below, an isosceles triangle has base \\(BC = {base}\\) cm "
        f"and two equal legs \\(AB = AC = {side}\\) cm.\n\n"
        f"1. What radius must the compass be set to when drawing arcs from \\(B\\) and \\(C\\)?\n"
        f"2. Explain why vertex \\(A\\) lies on the perpendicular bisector of base \\(BC\\)."
    )
    sol = (
        f"**1. Compass radius:** Exactly **{side} cm**.\n\n"
        f"**2. Perpendicular bisector explanation:** Since \\(AB = AC\\), vertex \\(A\\) is equidistant from \\(B\\) and \\(C\\). "
        f"By the equidistant theorem, any point equidistant from two endpoints must lie on their perpendicular bisector."
    )
    ans = f"1. {side} cm; 2. A is equidistant from B and C (AB = AC)"
    return {
        "id": f"g8_const_iso_tri_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "23_construct_isosceles_triangle_given_base_and_equal_sides",
        "learning_objective_id": "math_g8_const_iso_tri",
        "hints": {
            "tier_1": f"The compass radius must match the leg length: {side} cm.",
            "tier_2": "Equal distances to endpoints means it lies on the perpendicular bisector.",
            "tier_3": f"{side} cm; equidistant from endpoints.",
        },
        "misconception_tags": ["setting_compass_to_base_length_instead_of_equal_legs"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 24. Construct Median Of A Triangle (ZERO LEAK TRIGGERS)
# ----------------------------------------------------------------------
def arch_24_construct_median_of_a_triangle(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"In triangle geometry, a **median** is a key line segment:\n\n"
        f"1. Define the **median** of a triangle.\n"
        f"2. Explain how to construct the midpoint of a side using a compass and straight edge.\n"
        f"3. How many medians does a triangle have?"
    )
    sol = (
        f"**1. Definition:** A median is a line segment connecting a vertex of a triangle to the midpoint of the opposite side.\n\n"
        f"**2. Midpoint construction:** Construct the perpendicular bisector of the opposite side. "
        f"The point where this bisector crosses the side is the midpoint.\n\n"
        f"**3. Number of medians:** Exactly **3** medians (one from each vertex)."
    )
    ans = "1. segment from vertex to midpoint of opposite side; 2. perpendicular bisector locates midpoint; 3. 3 medians"
    return {
        "id": f"g8_const_median_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "subskill": "24_construct_median_of_a_triangle",
        "learning_objective_id": "math_g8_const_median",
        "hints": {
            "tier_1": "Median goes from a vertex to the middle of the opposite side.",
            "tier_2": "Find the middle of the side using a perpendicular bisector.",
            "tier_3": "Vertex to midpoint; perpendicular bisector finds midpoint; 3 medians.",
        },
        "misconception_tags": ["confusing_median_with_altitude"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 25. Construct Altitude Of A Triangle (ZERO LEAK TRIGGERS)
# ----------------------------------------------------------------------
def arch_25_construct_altitude_of_a_triangle(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"In triangle geometry, an **altitude** represents the perpendicular height:\n\n"
        f"1. Define the **altitude** of a triangle.\n"
        f"2. Explain which construction method is used to construct an altitude from vertex \\(A\\) to base \\(BC\\).\n"
        f"3. Does the altitude of an obtuse triangle always lie inside the triangle? Explain."
    )
    sol = (
        f"**1. Definition:** An altitude is a perpendicular line segment drawn from a vertex to the opposite side (or extended opposite side).\n\n"
        f"**2. Construction:** Construct a perpendicular line from external point \\(A\\) to line \\(BC\\).\n\n"
        f"**3. Obtuse triangle:** No, for an obtuse-angled triangle, two of the altitudes lie completely **outside** the triangle."
    )
    ans = "1. perpendicular from vertex to opposite side; 2. perpendicular from external point; 3. No, lies outside in obtuse triangles"
    return {
        "id": f"g8_const_altitude_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "subskill": "25_construct_altitude_of_a_triangle",
        "learning_objective_id": "math_g8_const_altitude",
        "hints": {
            "tier_1": "Altitude meets the opposite side at 90°.",
            "tier_2": "It uses the construction of a perpendicular from an external point.",
            "tier_3": "Perpendicular to opposite side; perpendicular from point; lies outside for obtuse triangles.",
        },
        "misconception_tags": ["assuming_altitudes_always_bisect_the_base"],
        "diagram_spec": None,
    }
