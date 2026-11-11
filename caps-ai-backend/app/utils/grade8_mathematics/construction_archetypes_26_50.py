"""Grade 8 Mathematics - Construction of Geometric Figures Archetypes (26 to 50).
Covers:
  - Centers of triangles: Incenter (angle bisectors), circumcenter (perpendicular bisectors).
  - Constructing quadrilaterals: Parallelogram, rhombus, rectangle, square, kite, trapezium.
  - Construction instruments: Ruler, compass, protractor accuracy, copying angles, parallel lines.
  - Advanced constructions: Dividing segments into n parts, inscribed/circumscribed circles, regular hexagons.
  - Scale drawings, error analysis, loci of points equidistant from points/lines.
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
# 26. Construct Angle Bisectors Incenter (ZERO LEAK TRIGGERS)
# ----------------------------------------------------------------------
def arch_26_construct_angle_bisectors_incenter(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"In a triangle \\(\\triangle ABC\\), all three interior angle bisectors are constructed:\n\n"
        f"1. Explain what is meant by **concurrent lines**.\n"
        f"2. What is the special name given to the point where the three angle bisectors meet?\n"
        f"3. What circle can be drawn with this point as its centre?"
    )
    sol = (
        f"**1. Concurrent lines:** Three or more lines that all intersect at the exact same common point.\n\n"
        f"**2. Incenter:** The point of concurrency of the three interior angle bisectors is called the **incenter** \\(I\\).\n\n"
        f"**3. Incircle:** The incenter is the centre of the **inscribed circle (incircle)**, which touches all three sides of the triangle."
    )
    ans = "1. lines intersecting at a single point; 2. incenter; 3. inscribed circle (incircle)"
    return {
        "id": f"g8_const_incenter_{rng.randint(100000, 999999)}",
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
        "subskill": "26_construct_angle_bisectors_incenter",
        "learning_objective_id": "math_g8_const_incenter",
        "hints": {
            "tier_1": "Angle bisectors meet at the incenter.",
            "tier_2": "The incenter is the center of the incircle.",
            "tier_3": "Concurrent lines; incenter; inscribed circle (incircle).",
        },
        "misconception_tags": ["confusing_incenter_with_circumcenter"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 27. Construct Perpendicular Bisectors Circumcenter (ZERO LEAK TRIGGERS)
# ----------------------------------------------------------------------
def arch_27_construct_perpendicular_bisectors_circumcenter(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"In a triangle \\(\\triangle ABC\\), the perpendicular bisectors of all three sides are constructed:\n\n"
        f"1. What is the special geometric name given to the point where the three perpendicular bisectors meet?\n"
        f"2. Explain why this point is equidistant from all three vertices \\(A\\), \\(B\\), and \\(C\\).\n"
        f"3. What circle can be drawn with this point as its centre?"
    )
    sol = (
        f"**1. Circumcenter:** The point of concurrency of the perpendicular bisectors is called the **circumcenter** \\(O\\).\n\n"
        f"**2. Equidistant explanation:** Any point on the perpendicular bisector of \\(AB\\) is equidistant from \\(A\\) and \\(B\\) (\\(OA = OB\\)). "
        f"Similarly, \\(OB = OC\\). Therefore, \\(OA = OB = OC\\).\n\n"
        f"**3. Circumscribed circle:** It is the centre of the **circumcircle**, which passes through all three vertices of the triangle."
    )
    ans = "1. circumcenter; 2. OA = OB = OC by perpendicular bisector equidistant theorem; 3. circumcircle"
    return {
        "id": f"g8_const_circumcenter_{rng.randint(100000, 999999)}",
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
        "subskill": "27_construct_perpendicular_bisectors_circumcenter",
        "learning_objective_id": "math_g8_const_circumcenter",
        "hints": {
            "tier_1": "Perpendicular bisectors meet at the circumcenter.",
            "tier_2": "The circumcenter is equidistant from the 3 vertices.",
            "tier_3": "Circumcenter; OA = OB = OC; circumcircle.",
        },
        "misconception_tags": ["confusing_circumcenter_with_orthocenter"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 28. Construct Parallelogram Given Two Sides And Angle (ZERO LEAK TRIGGERS)
# ----------------------------------------------------------------------
def arch_28_construct_parallelogram_given_two_sides_and_angle(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([7, 8, 9])
    b = rng.choice([4, 5, 6])
    ang = rng.choice([50, 60, 70])

    prompt = (
        f"To construct parallelogram \\(ABCD\\) with sides \\(AB = {a}\\) cm, \\(AD = {b}\\) cm, "
        f"and angle \\(\\hat{{A}} = {ang}^\\circ\\):\n\n"
        f"1. Describe how to locate vertices \\(B\\) and \\(D\\) from vertex \\(A\\).\n"
        f"2. Explain how compass arcs of radii **{a} cm** and **{b} cm** are used to locate the fourth vertex \\(C\\).\n"
        f"3. Which property of a parallelogram guarantees this construction works?"
    )
    sol = (
        f"**1. Locating B and D:** Draw base \\(AB = {a}\\) cm with a ruler. At \\(A\\), construct an angle of \\({ang}^\\circ\\) "
        f"and mark \\(AD = {b}\\) cm along the arm to locate \\(D\\).\n\n"
        f"**2. Locating C:** Place the compass point at \\(D\\) and swing an arc of radius \\({a}\\) cm (since \\(DC = AB = {a}\\) cm). "
        f"Place the compass at \\(B\\) and swing an arc of radius \\({b}\\) cm (since \\(BC = AD = {b}\\) cm). "
        f"The intersection of these two arcs marks vertex \\(C\\).\n\n"
        f"**3. Property:** Opposite sides of a parallelogram are equal in length (\\(AB = DC\\) and \\(AD = BC\\))."
    )
    ans = f"1. draw AB = {a} cm, construct {ang}° at A and mark AD = {b} cm; 2. arc radius {a} cm from D and {b} cm from B meet at C; 3. opposite sides are equal"
    return {
        "id": f"g8_const_parm_steps_{rng.randint(100000, 999999)}",
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
        "subskill": "28_construct_parallelogram_given_two_sides_and_angle",
        "learning_objective_id": "math_g8_const_parm_steps",
        "hints": {
            "tier_1": "Opposite sides are equal in a parallelogram.",
            "tier_2": f"Arc of {a} cm from D and arc of {b} cm from B.",
            "tier_3": "Locate B and D; compass arcs from D and B intersect at C; opposite sides equal.",
        },
        "misconception_tags": ["swinging_the_wrong_radii_from_vertices_B_and_D"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 29. Construct Rhombus Given Side And Angle (ZERO LEAK TRIGGERS)
# ----------------------------------------------------------------------
def arch_29_construct_rhombus_given_side_and_angle(rng: random.Random) -> Dict[str, Any]:
    s = rng.choice([5, 6, 7, 8])
    ang = rng.choice([45, 60, 75])

    prompt = (
        f"A rhombus \\(ABCD\\) has side length **{s} cm** and acute angle \\(\\hat{{A}} = {ang}^\\circ\\).\n\n"
        f"1. Explain why all compass arcs in this construction have the exact same radius of **{s} cm**.\n"
        f"2. Describe how vertex \\(C\\) is located using compass arcs from vertices \\(B\\) and \\(D\\)."
    )
    sol = (
        f"**1. Same radius:** All four sides of a rhombus are equal in length (\\(AB = BC = CD = DA = {s}\\) cm).\n\n"
        f"**2. Locating C:** Place the compass with radius \\({s}\\) cm at \\(B\\) and draw an arc. "
        f"With the same radius \\({s}\\) cm, place the compass at \\(D\\) and draw an intersecting arc. "
        f"Their intersection point marks vertex \\(C\\)."
    )
    ans = f"1. all 4 sides of a rhombus are equal ({s} cm); 2. arcs of radius {s} cm from B and D intersect at C"
    return {
        "id": f"g8_const_rhomb_side_ang_{rng.randint(100000, 999999)}",
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
        "subskill": "29_construct_rhombus_given_side_and_angle",
        "learning_objective_id": "math_g8_const_rhomb_side_ang",
        "hints": {
            "tier_1": "All four sides of a rhombus are equal.",
            "tier_2": f"Keep compass set to {s} cm throughout.",
            "tier_3": "All sides equal; arcs of s cm from B and D meet at C.",
        },
        "misconception_tags": ["using_different_side_lengths_in_rhombus"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 30. Construct Rhombus Given Diagonals (ZERO LEAK TRIGGERS)
# ----------------------------------------------------------------------
def arch_30_construct_rhombus_given_diagonals(rng: random.Random) -> Dict[str, Any]:
    d1 = rng.choice([8, 10, 12])
    d2 = rng.choice([6, 8, 10])

    prompt = (
        f"To construct a rhombus given its two diagonals \\(AC = {d1}\\) cm and \\(BD = {d2}\\) cm:\n\n"
        f"1. What geometric relationship between the diagonals of a rhombus makes this construction possible?\n"
        f"2. Describe the construction steps using the perpendicular bisector of diagonal \\(AC\\)."
    )
    half_d2 = d2 / 2
    h2_str = f"{int(half_d2)}" if half_d2.is_integer() else f"{half_d2}"
    sol = (
        f"**1. Relationship:** The diagonals of a rhombus bisect each other at right angles (\\(90^\\circ\\)).\n\n"
        f"**2. Construction steps:**\n"
        f"- Draw diagonal \\(AC = {d1}\\) cm with a ruler.\n"
        f"- Construct the perpendicular bisector of \\(AC\\), passing through midpoint \\(O\\).\n"
        f"- From \\(O\\), measure half of \\(BD\\) ({h2_str} cm) upwards to locate \\(B\\), "
        f"and {h2_str} cm downwards to locate \\(D\\).\n"
        f"- Connect \\(A-B-C-D-A\\) to complete the rhombus."
    )
    ans = f"1. diagonals bisect perpendicularly at 90°; 2. construct perp bisector of AC, mark {h2_str} cm above and below midpoint O"
    return {
        "id": f"g8_const_rhomb_diag_{rng.randint(100000, 999999)}",
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
        "subskill": "30_construct_rhombus_given_diagonals",
        "learning_objective_id": "math_g8_const_rhomb_diag",
        "hints": {
            "tier_1": "Diagonals of a rhombus are perpendicular bisectors of each other.",
            "tier_2": f"Construct perpendicular bisector of AC, measure {h2_str} cm on either side.",
            "tier_3": "Perpendicular bisectors; measure half of d2 above and below.",
        },
        "misconception_tags": ["measuring_full_d2_from_midpoint_instead_of_half"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 31. Construct Rectangle Given Length And Breadth (ZERO LEAK TRIGGERS)
# ----------------------------------------------------------------------
def arch_31_construct_rectangle_given_length_and_breadth(rng: random.Random) -> Dict[str, Any]:
    l = rng.choice([7, 8, 9, 10])
    b = rng.choice([4, 5, 6])

    prompt = (
        f"To construct rectangle \\(ABCD\\) with length \\(AB = {l}\\) cm and breadth \\(BC = {b}\\) cm:\n\n"
        f"1. What angle must be constructed at vertices \\(A\\) and \\(B\\)?\n"
        f"2. How are the upper vertices \\(D\\) and \\(C\\) located?"
    )
    sol = (
        f"**1. Angle:** Construct **90^\\circ** perpendicular rays at both \\(A\\) and \\(B\\).\n\n"
        f"**2. Locating D and C:** Measure along the perpendicular from \\(A\\) a length of \\({b}\\) cm to locate \\(D\\). "
        f"Measure along the perpendicular from \\(B\\) a length of \\({b}\\) cm to locate \\(C\\). "
        f"Join \\(D\\) to \\(C\\). Check that \\(DC = {l}\\) cm."
    )
    ans = f"1. 90° (right angle); 2. mark {b} cm along perpendiculars from A and B, join D to C"
    return {
        "id": f"g8_const_rect_steps_{rng.randint(100000, 999999)}",
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
        "subskill": "31_construct_rectangle_given_length_and_breadth",
        "learning_objective_id": "math_g8_const_rect_steps",
        "hints": {
            "tier_1": "All four angles of a rectangle are 90°.",
            "tier_2": f"Construct 90° at A and B, mark {b} cm on both.",
            "tier_3": "90°; measure b cm on perpendiculars and join.",
        },
        "misconception_tags": ["drawing_slanted_angles_for_rectangle"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 32. Construct Square Given Side Length (ZERO LEAK TRIGGERS)
# ----------------------------------------------------------------------
def arch_32_construct_square_given_side_length(rng: random.Random) -> Dict[str, Any]:
    s = rng.choice([5, 6, 7, 8])

    prompt = (
        f"A square \\(ABCD\\) has sides of length **{s} cm**.\n\n"
        f"1. Describe the construction of the right angle at vertex \\(A\\) on base \\(AB = {s}\\) cm.\n"
        f"2. How are vertices \\(D\\) and \\(C\\) located using a compass radius of **{s} cm**?"
    )
    sol = (
        f"**1. Right angle at A:** Construct a \\(90^\\circ\\) perpendicular ray upwards from vertex \\(A\\).\n\n"
        f"**2. Locating D and C:** With the compass set to radius \\({s}\\) cm:\n"
        f"- Place the compass at \\(A\\) and cut the perpendicular ray to locate \\(D\\).\n"
        f"- Place the compass at \\(B\\) and swing an arc upwards.\n"
        f"- Place the compass at \\(D\\) and swing an intersecting arc to locate \\(C\\).\n"
        f"- Connect \\(B-C\\) and \\(D-C\\)."
    )
    ans = f"1. construct 90° perpendicular at A; 2. cut {s} cm on perpendicular for D, intersect arcs of {s} cm from B and D for C"
    return {
        "id": f"g8_const_sq_steps_{rng.randint(100000, 999999)}",
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
        "subskill": "32_construct_square_given_side_length",
        "learning_objective_id": "math_g8_const_sq_steps",
        "hints": {
            "tier_1": "Square has four 90° angles and four equal sides.",
            "tier_2": f"Keep compass at {s} cm for all steps.",
            "tier_3": "90° perpendicular; arcs of radius s cm locate D and C.",
        },
        "misconception_tags": ["forgetting_to_construct_right_angle"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 33. Construct Kite Given Sides And Diagonal (ZERO LEAK TRIGGERS)
# ----------------------------------------------------------------------
def arch_33_construct_kite_given_sides_and_diagonal(rng: random.Random) -> Dict[str, Any]:
    diag = rng.choice([8, 10, 12])
    a = rng.choice([5, 6])
    b = rng.choice([7, 8])

    prompt = (
        f"To construct kite \\(ABCD\\) given main diagonal \\(AC = {diag}\\) cm, "
        f"top sides \\(AB = AD = {a}\\) cm, and bottom sides \\(BC = CD = {b}\\) cm:\n\n"
        f"1. Which segment is drawn first as the central axis?\n"
        f"2. How is vertex \\(B\\) located above the diagonal?\n"
        f"3. How is vertex \\(D\\) located below the diagonal?"
    )
    sol = (
        f"**1. Central axis:** Draw diagonal \\(AC = {diag}\\) cm with a ruler.\n\n"
        f"**2. Locating B:** Open the compass to \\({a}\\) cm, place at \\(A\\) and swing an arc above \\(AC\\). "
        f"Open the compass to \\({b}\\) cm, place at \\(C\\) and swing an intersecting arc above \\(AC\\). Their intersection is \\(B\\).\n\n"
        f"**3. Locating D:** Using the exact same compass settings (\\({a}\\) cm from \\(A\\) and \\({b}\\) cm from \\(C\\)), "
        f"swing intersecting arcs below line segment \\(AC\\). Their intersection is \\(D\\)."
    )
    ans = f"1. diagonal AC = {diag} cm; 2. intersecting arcs radius {a} cm from A and {b} cm from C above; 3. same arcs below"
    return {
        "id": f"g8_const_kite_steps_{rng.randint(100000, 999999)}",
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
        "subskill": "33_construct_kite_given_sides_and_diagonal",
        "learning_objective_id": "math_g8_const_kite_steps",
        "hints": {
            "tier_1": "Draw the diagonal axis first.",
            "tier_2": f"Swing arcs of {a} cm from A and {b} cm from C above and below.",
            "tier_3": "AC first; arcs of a and b above for B; arcs below for D.",
        },
        "misconception_tags": ["swinging_equal_arcs_from_the_same_vertex_instead_of_opposite_ends"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 34. Construct Trapezium Given Parallel Bases And Height (ZERO LEAK TRIGGERS)
# ----------------------------------------------------------------------
def arch_34_construct_trapezium_given_parallel_bases_and_height(rng: random.Random) -> Dict[str, Any]:
    b1 = rng.choice([8, 10, 12])
    b2 = rng.choice([4, 5, 6])
    h = rng.choice([4, 5])

    prompt = (
        f"To construct a trapezium with parallel bases \\(b_1 = {b1}\\) cm and \\(b_2 = {b2}\\) cm "
        f"and perpendicular distance (height) \\(h = {h}\\) cm:\n\n"
        f"1. Explain how to construct a parallel line at distance \\({h}\\) cm above the baseline \\(b_1\\).\n"
        f"2. How is the top base \\(b_2\\) positioned on this parallel line?"
    )
    sol = (
        f"**1. Constructing parallel line:** Erect two perpendiculars of height \\({h}\\) cm at two points along base \\(b_1\\). "
        f"Draw a straight line connecting the tops of these perpendiculars. This line is parallel to base \\(b_1\\) at distance \\({h}\\) cm.\n\n"
        f"**2. Positioning top base:** Measure off segment \\(b_2 = {b2}\\) cm along the parallel line using a ruler, "
        f"then join the endpoints to the ends of the base."
    )
    ans = f"1. erect perpendiculars of height {h} cm and connect their tops; 2. measure {b2} cm along the parallel line"
    return {
        "id": f"g8_const_trap_steps_{rng.randint(100000, 999999)}",
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
        "subskill": "34_construct_trapezium_given_parallel_bases_and_height",
        "learning_objective_id": "math_g8_const_trap_steps",
        "hints": {
            "tier_1": "Parallel lines maintain a constant perpendicular distance h.",
            "tier_2": f"Perpendiculars of {h} cm define the parallel line.",
            "tier_3": "Erect perpendiculars of h cm; mark b2 cm on parallel line.",
        },
        "misconception_tags": ["drawing_slant_side_instead_of_perpendicular_height"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 35. Ruler And Compass Safety And Accuracy Rules (ZERO LEAK TRIGGERS)
# ----------------------------------------------------------------------
def arch_35_ruler_and_compass_safety_and_accuracy_rules(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Geometric constructions require precise technical standards in South African examinations:\n\n"
        f"1. Why must the pencil lead in a pair of compasses be sharpened to a fine chisel or needle point?\n"
        f"2. Why must construction arcs NEVER be erased or rubbed out in an exam paper?\n"
        f"3. Explain what **parallax error** is when reading a ruler."
    )
    sol = (
        f"**1. Fine point:** Thick pencil lines introduce measurement inaccuracies of \\(1\\text{{ mm}}\\) or more, leading to penalties.\n\n"
        f"**2. Do not erase arcs:** Construction arcs are the visual evidence (method marks [M]) proving that instruments were used correctly and not merely guessed.\n\n"
        f"**3. Parallax error:** An apparent shift in position of an object when viewed from an angle rather than directly perpendicular (at \\(90^\\circ\\)) above the ruler scale."
    )
    ans = "1. thick lines cause measurement error; 2. arcs earn method marks proving genuine construction; 3. viewing measurement at an angle"
    return {
        "id": f"g8_const_rules_{rng.randint(100000, 999999)}",
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
        "subskill": "35_ruler_and_compass_safety_and_accuracy_rules",
        "learning_objective_id": "math_g8_const_rules",
        "hints": {
            "tier_1": "Never erase construction marks; they earn marks.",
            "tier_2": "Parallax error comes from viewing from an angle.",
            "tier_3": "Fine point avoids error; arcs show method; parallax is angle view error.",
        },
        "misconception_tags": ["erasing_construction_arcs_thinking_it_looks_neater"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 36. Measure And Verify Angles With Protractor (ZERO LEAK TRIGGERS)
# ----------------------------------------------------------------------
def arch_36_measure_and_verify_angles_with_protractor(rng: random.Random) -> Dict[str, Any]:
    ang = rng.choice([35, 48, 62, 75, 115, 130])
    supp = 180 - ang

    prompt = (
        f"A learner constructs an angle and verifies it with a protractor:\n\n"
        f"1. Explain how to decide whether to read the **inner scale** or the **outer scale** of a protractor.\n"
        f"2. If the learner mistakenly reads the wrong scale and records **{supp}^\\circ**, what is the true angle measure?"
    )
    sol = (
        f"**1. Inner vs outer scale:** Align the protractor origin at the vertex and the baseline along the zero line. "
        f"Read whichever scale starts at \\(0^\\circ\\) on the side where the base arm points.\n\n"
        f"**2. True measure:** The two scales on a protractor sum to \\(180^\\circ\\):\n"
        f"\\[ \\text{{True angle}} = 180^\\circ - {supp}^\\circ = {ang}^\\circ \\]"
    )
    ans = f"1. follow scale starting at 0° on the base arm; 2. {ang}°"
    return {
        "id": f"g8_const_protr_read_{rng.randint(100000, 999999)}",
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
        "subskill": "36_measure_and_verify_angles_with_protractor",
        "learning_objective_id": "math_g8_const_protr_read",
        "hints": {
            "tier_1": "The scale that starts at 0° on the arm must be followed.",
            "tier_2": f"180° - {supp}° = {ang}°.",
            "tier_3": f"Scale starting at 0°; true angle is {ang}°.",
        },
        "misconception_tags": ["reading_inner_scale_instead_of_outer_scale"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 37. Measure And Verify Segments With Ruler (ZERO LEAK TRIGGERS)
# ----------------------------------------------------------------------
def arch_37_measure_and_verify_segments_with_ruler(rng: random.Random) -> Dict[str, Any]:
    cm_val = rng.choice([4.6, 5.8, 7.3, 8.4, 11.2])
    mm_val = int(cm_val * 10)

    prompt = (
        f"A line segment is measured with a transparent millimeter ruler:\n\n"
        f"1. Explain why measurement must begin at the **0 mark** and not at the physical edge of the plastic ruler.\n"
        f"2. If the measurement is recorded as **{cm_val} cm**, express this length in millimeters (mm)."
    )
    sol = (
        f"**1. Zero mark:** Most rulers have a small blank gap before the \\(0\\) line. Starting at the plastic edge introduces an error equal to the gap width.\n\n"
        f"**2. Millimeters:** Multiply by 10:\n"
        f"\\[ {cm_val} \\times 10 = {mm_val} \\text{{ mm}} \\]"
    )
    ans = f"1. plastic edge has a blank gap before 0; 2. {mm_val} mm"
    return {
        "id": f"g8_const_ruler_meas_{rng.randint(100000, 999999)}",
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
        "subskill": "37_measure_and_verify_segments_with_ruler",
        "learning_objective_id": "math_g8_const_ruler_meas",
        "hints": {
            "tier_1": "Rulers have a space before the 0 mark.",
            "tier_2": f"{cm_val} × 10.",
            "tier_3": f"Edge has gap; {mm_val} mm.",
        },
        "misconception_tags": ["starting_measurement_at_the_end_of_the_ruler"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 38. Parallel Line Construction Alternate Angle Method (ZERO LEAK TRIGGERS)
# ----------------------------------------------------------------------
def arch_38_parallel_line_construction_alternate_angle_method(rng: random.Random) -> Dict[str, Any]:
    ang = rng.choice([40, 50, 60, 70])

    prompt = (
        f"To construct a line through point \\(P\\) parallel to a given line \\(AB\\) using the alternate angle method:\n\n"
        f"1. Draw a transversal line through \\(P\\) intersecting line \\(AB\\) at angle **{ang}^\\circ**.\n"
        f"2. Explain how copying an alternate angle of \\({ang}^\\circ\\) at point \\(P\\) guarantees that the new line is parallel to \\(AB\\)."
    )
    sol = (
        f"**1. Transversal:** Draw any transversal line passing through point \\(P\\) and intersecting line \\(AB\\) at point \\(Q\\).\n\n"
        f"**2. Alternate angle theorem:** By constructing an angle of \\({ang}^\\circ\\) at \\(P\\) on the alternate side of the transversal "
        f"equal to the interior angle at \\(Q\\), the converse alternate angle theorem guarantees that the two lines must be parallel "
        f"(\\(\\text{{alt. }}\\angle\\text{{s are equal}} \\implies \\text{{lines are parallel}}\\))."
    )
    ans = f"1. draw transversal through P; 2. converse alternate angle theorem (equal alternate angles mean lines are parallel)"
    return {
        "id": f"g8_const_par_alt_ang_{rng.randint(100000, 999999)}",
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
        "subskill": "38_parallel_line_construction_alternate_angle_method",
        "learning_objective_id": "math_g8_const_par_alt_ang",
        "hints": {
            "tier_1": "Equal alternate angles prove lines are parallel.",
            "tier_2": "Copy the angle to the alternate position at P.",
            "tier_3": "Draw transversal; converse alternate angle theorem guarantees parallel lines.",
        },
        "misconception_tags": ["copying_angle_to_cointerior_position_without_supplementing"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 39. Copy Given Angle Construction Steps (ZERO LEAK TRIGGERS)
# ----------------------------------------------------------------------
def arch_39_copy_given_angle_construction_steps(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Explain how to **copy an existing angle** \\(\\angle ABC\\) onto a new baseline without measuring with a protractor:\n\n"
        f"1. Describe the arc drawn across the original angle arms.\n"
        f"2. How is that arc replicated on the new baseline?\n"
        f"3. How is the compass used to measure the width between the arms?"
    )
    sol = (
        f"**1. Original arc:** Place compass at vertex \\(B\\) and draw an arc cutting both arms at points \\(X\\) and \\(Y\\).\n\n"
        f"**2. Replicating on baseline:** With the *same* compass radius, place the compass at the new vertex and draw a similar arc cutting the new baseline at point \\(X'\\).\n\n"
        f"**3. Width between arms:** Place compass point at \\(X\\) and open it to touch \\(Y\\) (measuring chord distance \\(XY\\)). "
        f"Then place compass at \\(X'\\) and draw an arc intersecting the first arc at \\(Y'\\). Connect the new vertex through \\(Y'\\)."
    )
    ans = "1. swing arc from vertex cutting both arms; 2. swing same radius arc on new baseline; 3. compass measures distance between arm intersections"
    return {
        "id": f"g8_const_copy_ang_{rng.randint(100000, 999999)}",
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
        "subskill": "39_copy_given_angle_construction_steps",
        "learning_objective_id": "math_g8_const_copy_ang",
        "hints": {
            "tier_1": "Draw an arc across both arms, then measure the distance across.",
            "tier_2": "Replicate the same radius and width on the new line.",
            "tier_3": "Arc cuts arms; same arc on new line; compass measures width between cuts.",
        },
        "misconception_tags": ["changing_radius_while_transferring_the_arc"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 40. Divide Line Segment Into N Equal Parts (ZERO LEAK TRIGGERS)
# ----------------------------------------------------------------------
def arch_40_divide_line_segment_into_n_equal_parts(rng: random.Random) -> Dict[str, Any]:
    n = rng.choice([3, 4, 5])
    tot_len = rng.choice([12, 15, 20])
    each_part = tot_len / n
    part_str = f"{int(each_part)}" if each_part.is_integer() else f"{each_part:.1f}"

    prompt = (
        f"To divide a line segment \\(AB = {tot_len}\\) cm into **{n} equal parts** using ruler and compass:\n\n"
        f"1. Describe the auxiliary ray drawn from vertex \\(A\\).\n"
        f"2. How are {n} equal segments stepped off along this auxiliary ray?\n"
        f"3. What geometric theorem allows parallel lines drawn to line \\(AB\\) to divide \\(AB\\) into equal parts?"
    )
    sol = (
        f"**1. Auxiliary ray:** Draw a ray from \\(A\\) at any acute angle to \\(AB\\).\n\n"
        f"**2. Stepping off:** Using any fixed compass radius, step off \\({n}\\) equal consecutive marks along the ray: \\(A_1, A_2, \\dots, A_{n}\\).\n\n"
        f"**3. Parallel lines theorem:** Join \\(A_{n}\\) to \\(B\\), then draw parallel lines through each intermediate point to cut \\(AB\\). "
        f"By the proportional intercept theorem (intercepts on parallel lines), segment \\(AB\\) is divided into \\({n}\\) equal parts of \\({part_str}\\) cm each."
    )
    ans = f"1. draw acute auxiliary ray from A; 2. step off {n} equal compass marks; 3. parallel lines divide transversals proportionally"
    return {
        "id": f"g8_const_div_n_parts_{rng.randint(100000, 999999)}",
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
        "subskill": "40_divide_line_segment_into_n_equal_parts",
        "learning_objective_id": "math_g8_const_div_n_parts",
        "hints": {
            "tier_1": "Draw an acute ray and mark n equal steps with a compass.",
            "tier_2": "Connect the last mark to B and draw parallel lines.",
            "tier_3": f"Acute ray; {n} equal marks; parallel lines theorem.",
        },
        "misconception_tags": ["dividing_by_ruler_measurement_only"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 41. Circumscribed Circle About Triangle (ZERO LEAK TRIGGERS)
# ----------------------------------------------------------------------
def arch_41_circumscribed_circle_about_triangle(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"To construct the **circumscribed circle (circumcircle)** about a triangle \\(\\triangle ABC\\):\n\n"
        f"1. Which lines of the triangle must be constructed to find the circumcenter?\n"
        f"2. How many of these lines need to be constructed at minimum?\n"
        f"3. What radius is set on the compass to draw the circle?"
    )
    sol = (
        f"**1. Lines:** The perpendicular bisectors of the sides of the triangle.\n\n"
        f"**2. Minimum:** Only **2** perpendicular bisectors are needed (their intersection uniquely determines the center; the third will automatically pass through it).\n\n"
        f"**3. Compass radius:** Set the radius equal to the distance from the circumcenter to any vertex (\\(R = OA = OB = OC\\))."
    )
    ans = "1. perpendicular bisectors of sides; 2. 2 bisectors; 3. distance from center to any vertex (OA)"
    return {
        "id": f"g8_const_circumcircle_{rng.randint(100000, 999999)}",
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
        "subskill": "41_circumscribed_circle_about_triangle",
        "learning_objective_id": "math_g8_const_circumcircle",
        "hints": {
            "tier_1": "Perpendicular bisectors of the sides find the circumcenter.",
            "tier_2": "Two bisectors are enough to locate the intersection.",
            "tier_3": "Perpendicular bisectors; minimum 2; radius = distance to vertex.",
        },
        "misconception_tags": ["using_angle_bisectors_for_circumcircle"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 42. Inscribed Circle Inside Triangle (ZERO LEAK TRIGGERS)
# ----------------------------------------------------------------------
def arch_42_inscribed_circle_inside_triangle(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"To construct the **inscribed circle (incircle)** inside a triangle \\(\\triangle ABC\\):\n\n"
        f"1. Which lines of the triangle are constructed to find the incenter \\(I\\)?\n"
        f"2. How is the radius of the incircle found from the incenter \\(I\\)?\n"
        f"3. Does the incircle touch or cross the sides of the triangle?"
    )
    sol = (
        f"**1. Lines:** The interior angle bisectors of the triangle.\n\n"
        f"**2. Radius:** Construct a perpendicular line from \\(I\\) to any one side of the triangle. "
        f"The perpendicular distance from \\(I\\) to the side is the radius \\(r\\).\n\n"
        f"**3. Touching sides:** The incircle is tangent to (touches at exactly one point) all three sides; it does not cross outside."
    )
    ans = "1. angle bisectors; 2. perpendicular distance from incenter to a side; 3. touches (tangent to) all 3 sides"
    return {
        "id": f"g8_const_incircle_{rng.randint(100000, 999999)}",
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
        "subskill": "42_inscribed_circle_inside_triangle",
        "learning_objective_id": "math_g8_const_incircle",
        "hints": {
            "tier_1": "Angle bisectors locate the incenter.",
            "tier_2": "Radius is perpendicular to any side.",
            "tier_3": "Angle bisectors; perpendicular distance to side; touches all 3 sides.",
        },
        "misconception_tags": ["using_distance_to_vertex_as_incircle_radius"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 43. Regular Hexagon Inscribed In Circle (ZERO LEAK TRIGGERS)
# ----------------------------------------------------------------------
def arch_43_regular_hexagon_inscribed_in_circle(rng: random.Random) -> Dict[str, Any]:
    r = rng.choice([4, 5, 6, 7])

    prompt = (
        f"To inscribe a regular hexagon in a circle of radius \\(r = {r}\\) cm:\n\n"
        f"1. Explain why the side length of a regular hexagon inscribed in a circle is exactly equal to the radius \\(r = {r}\\) cm.\n"
        f"2. How many times is the compass radius stepped along the circumference to locate the 6 vertices?"
    )
    sol = (
        f"**1. Equal to radius:** A regular hexagon can be divided from its centre into 6 equilateral triangles. "
        f"In each equilateral triangle, the side length equals the radius of the circumscribed circle (\\(s = r = {r}\\) cm).\n\n"
        f"**2. Stepping off:** Exactly **6 times** around the circumference."
    )
    ans = f"1. hexagon is made of 6 equilateral triangles where side = radius ({r} cm); 2. 6 times"
    return {
        "id": f"g8_const_hex_in_circ_{rng.randint(100000, 999999)}",
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
        "subskill": "43_regular_hexagon_inscribed_in_circle",
        "learning_objective_id": "math_g8_const_hex_in_circ",
        "hints": {
            "tier_1": "A regular hexagon consists of 6 equilateral triangles.",
            "tier_2": f"Each side is equal to radius {r} cm.",
            "tier_3": "Side equals radius; step 6 times.",
        },
        "misconception_tags": ["changing_the_compass_radius_when_stepping_around_circle"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 44. Scale Drawing Interpretation And Ratio (ZERO LEAK TRIGGERS)
# ----------------------------------------------------------------------
def arch_44_scale_drawing_interpretation_and_ratio(rng: random.Random) -> Dict[str, Any]:
    scale_val = rng.choice([50, 100, 200])  # 1 : scale_val
    draw_cm = rng.choice([4, 6, 8, 10])
    real_cm = draw_cm * scale_val
    real_m = real_cm / 100
    m_str = f"{int(real_m)}" if real_m.is_integer() else f"{real_m:.1f}"

    prompt = (
        f"A building model uses a scale ratio of **1 : {scale_val}**.\n"
        f"A classroom wall has a scaled length of **{draw_cm} cm**.\n\n"
        f"1. Explain what the scale ratio 1 : {scale_val} signifies.\n"
        f"2. Calculate the actual real-world length of the classroom wall in meters."
    )
    sol = (
        f"**1. Scale meaning:** Every \\(1\\text{{ cm}}\\) on the drawing represents \\({scale_val}\\text{{ cm}}\\) in real life.\n\n"
        f"**2. Real-world length:**\n"
        f"\\[ \\text{{Real length}} = {draw_cm} \\times {scale_val} = {real_cm} \\text{{ cm}} \\]\n"
        f"\\[ \\frac{{{real_cm}}}{{100}} = {m_str} \\text{{ m}} \\]"
    )
    ans = f"1. 1 cm on drawing represents {scale_val} cm in reality; 2. {m_str} m"
    return {
        "id": f"g8_scale_draw_interp_{rng.randint(100000, 999999)}",
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
        "subskill": "44_scale_drawing_interpretation_and_ratio",
        "learning_objective_id": "math_g8_scale_draw_interp",
        "hints": {
            "tier_1": f"Multiply drawing measurement by {scale_val}.",
            "tier_2": f"{draw_cm} × {scale_val} cm, then divide by 100 to get meters.",
            "tier_3": f"{m_str} m.",
        },
        "misconception_tags": ["dividing_by_scale_factor_instead_of_multiplying"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 45. Scale Drawing Construct Plan Dimensions (ZERO LEAK TRIGGERS)
# ----------------------------------------------------------------------
def arch_45_scale_drawing_construct_plan_dimensions(rng: random.Random) -> Dict[str, Any]:
    scale_val = rng.choice([50, 100])
    real_m = rng.choice([6, 8, 12, 15])
    real_cm = real_m * 100
    draw_cm = real_cm / scale_val
    cm_str = f"{int(draw_cm)}" if draw_cm.is_integer() else f"{draw_cm:.1f}"

    prompt = (
        f"An architect designs a swimming pool with an actual length of **{real_m} m** "
        f"using a scale ratio of **1 : {scale_val}**.\n\n"
        f"1. Convert the actual length from meters to centimeters.\n"
        f"2. Calculate the scaled length in centimeters representing this pool."
    )
    sol = (
        f"**Step 1: Meters to cm**\n"
        f"\\[ {real_m} \\times 100 = {real_cm} \\text{{ cm}} \\]\n\n"
        f"**Step 2: Drawing length**\n"
        f"\\[ \\text{{Drawing length}} = \\frac{{{real_cm}}}{{{scale_val}}} = {cm_str} \\text{{ cm}} \\]"
    )
    ans = f"1. {real_cm} cm; 2. {cm_str} cm"
    return {
        "id": f"g8_scale_draw_plan_{rng.randint(100000, 999999)}",
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
        "subskill": "45_scale_drawing_construct_plan_dimensions",
        "learning_objective_id": "math_g8_scale_draw_plan",
        "hints": {
            "tier_1": "Convert meters to cm first (× 100), then divide by scale factor.",
            "tier_2": f"{real_cm} ÷ {scale_val}.",
            "tier_3": f"{cm_str} cm.",
        },
        "misconception_tags": ["dividing_meters_directly_by_scale_without_converting_to_cm"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 46. Congruency Verification Through Construction (ZERO LEAK TRIGGERS)
# ----------------------------------------------------------------------
def arch_46_congruency_verification_through_construction(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Two learners each independently construct a triangle using the same given specifications: "
        f"sides **6 cm**, **7 cm**, and **9 cm**:\n\n"
        f"1. State whether their resulting triangles must be identical in shape and size (congruent).\n"
        f"2. What congruency condition guarantees this?\n"
        f"3. Would the triangles necessarily be congruent if only given angles 40°, 60°, and 80°? Explain."
    )
    sol = (
        f"**1. Congruency:** Yes, they must be congruent.\n\n"
        f"**2. Condition:** SSS (Side-Side-Side).\n\n"
        f"**3. Angles only (AAA):** No. Triangles with the same angles are similar (same shape), "
        f"but they can be drawn at different scales and sizes without being congruent."
    )
    ans = "1. Yes; 2. SSS; 3. No, AAA only guarantees similarity, not congruence"
    return {
        "id": f"g8_const_cong_verif_{rng.randint(100000, 999999)}",
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
        "subskill": "46_congruency_verification_through_construction",
        "learning_objective_id": "math_g8_const_cong_verif",
        "hints": {
            "tier_1": "Three given sides uniquely determine a triangle (SSS).",
            "tier_2": "Three given angles only determine shape, not size.",
            "tier_3": "Yes (SSS); No (AAA is similar, not congruent).",
        },
        "misconception_tags": ["assuming_aaa_forces_congruence"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 47. Error Analysis Identifying Flawed Construction Step (ZERO LEAK TRIGGERS)
# ----------------------------------------------------------------------
def arch_47_error_analysis_identifying_flawed_construction_step(rng: random.Random) -> Dict[str, Any]:
    mistakes = [
        ("A learner trying to construct the perpendicular bisector of segment AB set the compass radius to less than half of AB.",
         "The arcs did not intersect above or below the line, making it impossible to locate the bisector line."),
        ("A learner constructing a 60° angle changed the compass radius after drawing the initial baseline arc.",
         "The resulting angle was not 60° because an equilateral triangle requires all sides and radii to be identical."),
        ("A learner bisecting an angle used two completely different compass radii for the two interior arcs.",
         "The ray drawn did not bisect the angle equally because the intersection was shifted closer to one arm."),
    ]
    st, expl = rng.choice(mistakes)

    prompt = (
        f"Read the following description of a student's geometric construction attempt:\n"
        f"'{st}'\n\n"
        f"1. Identify the geometrical error in the student's procedure.\n"
        f"2. Explain what consequence this error had on the final construction."
    )
    sol = (
        f"**1. Error:** The student failed to keep compass radii consistent or above the required threshold.\n\n"
        f"**2. Consequence:** {expl}"
    )
    ans = f"1. improper compass setting; 2. {expl}"
    return {
        "id": f"g8_const_error_anal_{rng.randint(100000, 999999)}",
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
        "subskill": "47_error_analysis_identifying_flawed_construction_step",
        "learning_objective_id": "math_g8_const_error_anal",
        "hints": {
            "tier_1": "Compass radii must remain constant during arc pairs.",
            "tier_2": "Radius must exceed half for perpendicular bisectors.",
            "tier_3": f"{expl}",
        },
        "misconception_tags": ["overlooking_radius_constancy"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 48. Composite Construction House Gable Profile (ZERO LEAK TRIGGERS)
# ----------------------------------------------------------------------
def arch_48_composite_construction_house_gable_profile(rng: random.Random) -> Dict[str, Any]:
    w = rng.choice([8, 10, 12])
    h = rng.choice([4, 5, 6])
    roof_ang = rng.choice([45, 60])

    prompt = (
        f"To construct the profile of a house gable end consisting of a rectangular base wall and an equilateral or pitched roof:\n"
        f"- The rectangular base has width \\(w = {w}\\) cm and height \\(h = {h}\\) cm.\n"
        f"- The triangular roof has pitch angles of **{roof_ang}^\\circ** at both eaves.\n\n"
        f"1. What instrument construction is used to erect the vertical wall sides?\n"
        f"2. How are the two {roof_ang}° roof pitch angles constructed from the tops of the walls without a protractor?\n"
        f"3. Where does the apex of the roof form?"
    )
    sol = (
        f"**1. Vertical walls:** Construct \\(90^\\circ\\) perpendicular rays at both ends of the base line.\n\n"
        f"**2. Roof pitch angles:** At the top corners of the walls, construct \\({roof_ang}^\\circ\\) angles "
        f"(using equilateral triangle arcs for \\(60^\\circ\\) or bisecting \\(90^\\circ\\) for \\(45^\\circ\\)).\n\n"
        f"**3. Apex:** The apex forms at the intersection of the two upward sloping roof rays directly above the midpoint of the house."
    )
    ans = f"1. 90° perpendiculars; 2. construct {roof_ang}° angles; 3. at the intersection of the two roof rays"
    return {
        "id": f"g8_const_gable_prof_{rng.randint(100000, 999999)}",
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
        "subskill": "48_composite_construction_house_gable_profile",
        "learning_objective_id": "math_g8_const_gable_prof",
        "hints": {
            "tier_1": "Combine 90° perpendiculars for walls with special angles for roof.",
            "tier_2": "The roof rays intersect at the apex.",
            "tier_3": "90° perpendiculars; special angle construction; apex at ray intersection.",
        },
        "misconception_tags": ["measuring_roof_height_before_constructing_pitch_angles"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 49. Geometric Locus Points Equidistant From Two Lines (ZERO LEAK TRIGGERS)
# ----------------------------------------------------------------------
def arch_49_geometric_locus_points_equidistant_from_two_lines(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"In geometry, a **locus** is the path or set of all points satisfying a given condition:\n\n"
        f"1. What geometric line represents the locus of all points that are equidistant from two intersecting straight lines \\(AB\\) and \\(BC\\)?\n"
        f"2. Explain why any point on this line is at equal perpendicular distance from both lines."
    )
    sol = (
        f"**1. Geometric line:** The **angle bisector** of the angle formed between the two lines.\n\n"
        f"**2. Explanation:** By constructing congruent right-angled triangles from any point \\(P\\) on the angle bisector "
        f"to the two arms (AAS congruency), the perpendicular distances to the arms are proved to be exactly equal."
    )
    ans = "1. angle bisector; 2. right-angled triangles formed with the arms are congruent (AAS)"
    return {
        "id": f"g8_const_locus_lines_{rng.randint(100000, 999999)}",
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
        "subskill": "49_geometric_locus_points_equidistant_from_two_lines",
        "learning_objective_id": "math_g8_const_locus_lines",
        "hints": {
            "tier_1": "Points equidistant from two intersecting lines lie on the angle bisector.",
            "tier_2": "Triangles dropped to each arm are congruent.",
            "tier_3": "Angle bisector; congruent triangles prove equal distances.",
        },
        "misconception_tags": ["confusing_locus_of_two_lines_with_locus_of_two_points"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 50. Geometric Locus Points Equidistant From Two Points (ZERO LEAK TRIGGERS)
# ----------------------------------------------------------------------
def arch_50_geometric_locus_points_equidistant_from_two_points(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Consider two fixed points \\(A\\) and \\(B\\) located in a plane:\n\n"
        f"1. What geometric line represents the locus of all points that are equidistant from point \\(A\\) and point \\(B\\)?\n"
        f"2. State the two essential geometric characteristics of this locus line relative to line segment \\(AB\\)."
    )
    sol = (
        f"**1. Geometric line:** The **perpendicular bisector** of line segment \\(AB\\).\n\n"
        f"**2. Two characteristics:**\n"
        f"1. It passes through the **midpoint** of \\(AB\\) (bisects segment \\(AB\\)).\n"
        f"2. It is **perpendicular** to \\(AB\\) (intersects at \\(90^\\circ\\))."
    )
    ans = "1. perpendicular bisector of segment AB; 2. bisects AB at midpoint and perpendicular at 90°"
    return {
        "id": f"g8_const_locus_pts_{rng.randint(100000, 999999)}",
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
        "subskill": "50_geometric_locus_points_equidistant_from_two_points",
        "learning_objective_id": "math_g8_const_locus_pts",
        "hints": {
            "tier_1": "Points equidistant from two endpoints lie on their perpendicular bisector.",
            "tier_2": "It cuts the segment in half at right angles.",
            "tier_3": "Perpendicular bisector; passes through midpoint and perpendicular (90°).",
        },
        "misconception_tags": ["thinking_the_locus_is_a_circle_instead_of_a_straight_line"],
        "diagram_spec": None,
    }
