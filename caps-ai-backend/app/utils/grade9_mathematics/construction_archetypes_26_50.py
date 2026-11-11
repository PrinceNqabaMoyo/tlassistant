"""Grade 9 Mathematics - Construction of Geometric Figures Archetypes 26 to 50
=============================================================================
Grounded strictly in:
  - CAPS Grade 9 Mathematics: Term 3 Topic: Construction of geometric figures
  - curriculum_docs_auto/Mathematics_Gr9/Term 3/01. Construction of geometric figures.md
  - Chapter 4: Triangle constructions (SAS, ASA, RHS), quadrilateral constructions,
    triangle centers (circumcentre, incentre, centroid, orthocentre), circle tangents,
    scale drawings, bearings, and diagnostic error analysis

Covers Archetypes 26 - 50:
  26: Triangle construction given SAS (two sides and included angle)
  27: Triangle construction given ASA (two angles and included side)
  28: Constructing right-angled triangle given RHS (hypotenuse and leg)
  29: Constructing equilateral triangle given side length
  30: Constructing a square given side length
  31: Constructing a rectangle given length and breadth
  32: Constructing a parallelogram given two adjacent sides and an angle
  33: Constructing a rhombus given side length and diagonal
  34: Constructing a regular hexagon inscribed in a circle
  35: Circumcentre and circumscribed circle of a triangle
  36: Incentre and inscribed circle of a triangle
  37: Centroid as intersection of medians (2:1 ratio)
  38: Orthocentre as intersection of altitudes
  39: Location of circumcentre in acute, right, and obtuse triangles
  40: Tangent to a circle perpendicular to radius at point of contact
  41: Equal lengths of tangents drawn from an external point
  42: Common chord of two intersecting circles
  43: Scale drawing of triangle to determine actual real-world distance
  44: Three-figure navigational bearing and back-bearing calculation
  45: Diagnostic error analysis: non-intersecting construction arcs
  46: Diagnostic error analysis: protractor inner vs outer scale misreading
  47: Diagnostic error analysis: why SSA is not a congruency condition
  48: Dividing a line segment into n equal parts using parallel rays
  49: Geometric locus equidistant from two intersecting straight lines
  50: Compound multi-step geometric construction synthesis challenge
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional

from app.utils.grade9_mathematics.construction_svg import (
    draw_triangle_construction_svg,
    draw_circumcircle_or_incircle_svg,
    draw_perpendicular_bisector_svg,
)


def arch_26_construct_triangle_sas_two_sides_included_angle(rng: random.Random) -> Dict[str, Any]:
    """Triangle given SAS: two sides b, c and included right angle (90 deg)."""
    # Use Pythagorean triple for clean integer hypotenuse
    b, c, a = rng.choice([(3, 4, 5), (6, 8, 10), (5, 12, 13)])

    prompt = (
        f"A triangle $\\triangle ABC$ is constructed using a compass and straightedge with:\n"
        f"- Side $AB = {c}\\text{{ cm}}$\n"
        f"- Included angle $\\angle A = 90^\\circ$\n"
        f"- Side $AC = {b}\\text{{ cm}}$\n\n"
        f"Using the Theorem of Pythagoras, calculate the length of the third side **$BC$** in centimetres."
    )

    return {
        "subskill": "26_construct_triangle_sas_two_sides_included_angle",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": str(a),
        "sample_answer": f"{a} cm",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Apply Pythagoras for right-angled triangle at A: BC^2 = AB^2 + AC^2 = {c}^2 + {b}^2", "marks": 1},
            {"step": f"Calculate: BC = √({c**2} + {b**2}) = √({a**2}) = {a} cm", "marks": 1},
        ],
        "hints": [
            "Because the included angle is $90^\\circ$, this is a right-angled triangle.",
            f"Use Pythagoras: $BC = \\sqrt{{{c}^2 + {b}^2}}$.",
            f"$BC = {a}\\text{{ cm}}$.",
        ],
        "misconception_tags": ["sas_construction_properties", "pythagoras_hypotenuse_calculation"],
    }


def arch_27_construct_triangle_asa_two_angles_one_side(rng: random.Random) -> Dict[str, Any]:
    """Triangle given ASA: calculate third angle using angle sum of triangle (180 deg)."""
    a1 = rng.choice([40, 45, 50, 55, 60, 65, 70])
    a2 = rng.choice([45, 50, 55, 60, 65, 70])
    while a1 + a2 >= 160:
        a2 -= 10
    a3 = 180 - (a1 + a2)
    side_len = rng.randint(6, 12)

    prompt = (
        f"To construct triangle $\\triangle ABC$, the following measurements are provided:\n"
        f"- Side $AB = {side_len}\\text{{ cm}}$\n"
        f"- Angle $\\angle A = {a1}^\\circ$\n"
        f"- Angle $\\angle B = {a2}^\\circ$\n\n"
        f"Before constructing the triangle, calculate the size of the third angle **$\\angle C$** in degrees."
    )

    return {
        "subskill": "27_construct_triangle_asa_two_angles_one_side",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": str(a3),
        "sample_answer": f"{a3}°",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "State that the interior angles of a triangle sum to 180°", "marks": 1},
            {"step": f"Calculate: ∠C = 180° - ({a1}° + {a2}°) = 180° - {a1 + a2}° = {a3}°", "marks": 1},
        ],
        "hints": [
            "The sum of interior angles in any triangle is always $180^\\circ$.",
            f"$\\angle C = 180^\\circ - ({a1}^\\circ + {a2}^\\circ)$.",
            f"$\\angle C = {a3}^\\circ$.",
        ],
        "misconception_tags": ["triangle_interior_angle_sum_error", "asa_angle_calculation_error"],
    }


def arch_28_construct_right_angled_triangle_rhs(rng: random.Random) -> Dict[str, Any]:
    """Construct RHS right-angled triangle; find other leg using Pythagoras."""
    leg, other_leg, hyp = rng.choice([(3, 4, 5), (4, 3, 5), (6, 8, 10), (8, 6, 10), (5, 12, 13)])

    prompt = (
        f"A right-angled triangle is constructed with a right angle ($90^\\circ$), a hypotenuse of **${hyp}\\text{{ cm}}$**, "
        f"and one leg of **${leg}\\text{{ cm}}$** (RHS condition).\n\n"
        f"Calculate the length of the **second leg** in centimetres."
    )

    return {
        "subskill": "28_construct_right_angled_triangle_rhs",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": str(other_leg),
        "sample_answer": f"{other_leg} cm",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "State Pythagoras theorem: leg^2 = hyp^2 - given_leg^2", "marks": 1},
            {"step": f"Calculate: leg = √({hyp}^2 - {leg}^2) = √({hyp**2 - leg**2}) = {other_leg} cm", "marks": 1},
        ],
        "hints": [
            "In a right-angled triangle, $a^2 + b^2 = c^2$.",
            f"Second leg $= \\sqrt{{{hyp}^2 - {leg}^2}} = \\sqrt{{{hyp**2} - {leg**2}}}$.",
            f"Length $= {other_leg}\\text{{ cm}}$.",
        ],
        "misconception_tags": ["pythagoras_subtraction_order_error", "rhs_construction_leg_calculation"],
    }


def arch_29_construct_equilateral_triangle_given_side(rng: random.Random) -> Dict[str, Any]:
    """Construct equilateral triangle given side length s; find perimeter."""
    s = rng.choice([5, 6, 7, 8, 9, 10])
    perimeter = 3 * s

    prompt = (
        f"An equilateral triangle $\\triangle PQR$ is constructed using a compass and straightedge.\n"
        f"Each side measures **${s}\\text{{ cm}}$**.\n\n"
        f"Calculate the **perimeter** of the constructed triangle in centimetres."
    )

    return {
        "subskill": "29_construct_equilateral_triangle_given_side",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": str(perimeter),
        "sample_answer": f"{perimeter} cm (each angle = 60°)",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Recall that an equilateral triangle has 3 equal sides", "marks": 1},
            {"step": f"Calculate perimeter: 3 * {s} = {perimeter} cm", "marks": 1},
        ],
        "hints": [
            "An equilateral triangle has three sides of equal length.",
            f"Multiply side length by $3$: $3 \\times {s} = {perimeter}\\text{{ cm}}$.",
            f"Perimeter $= {perimeter}\\text{{ cm}}$.",
        ],
        "misconception_tags": ["equilateral_triangle_properties", "equilateral_perimeter_calculation"],
    }


def arch_30_construct_square_given_side_length(rng: random.Random) -> Dict[str, Any]:
    """Construct a square given side length s; calculate area."""
    s = rng.choice([4, 5, 6, 7, 8, 9, 10])
    area = s * s

    prompt = (
        f"A square $ABCD$ is constructed with four right angles and side lengths of **${s}\\text{{ cm}}$**.\n\n"
        f"Calculate the **area** of the constructed square in square centimetres ($\\text{{cm}}^2$)."
    )

    return {
        "subskill": "30_construct_square_given_side_length",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": str(area),
        "sample_answer": f"{area} cm²",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "State area formula for a square: Area = side^2", "marks": 1},
            {"step": f"Calculate: {s}^2 = {area} cm^2", "marks": 1},
        ],
        "hints": [
            "The area of a square is given by $\\text{side} \\times \\text{side}$.",
            f"Calculate ${s}^2 = {area}$.",
            f"Area $= {area}\\text{{ cm}}^2$.",
        ],
        "misconception_tags": ["square_area_vs_perimeter_confusion", "squaring_calculation_error"],
    }


def arch_31_construct_rectangle_given_length_and_breadth(rng: random.Random) -> Dict[str, Any]:
    """Construct rectangle with length L and breadth B; find diagonal length using Pythagoras."""
    b, l, d = rng.choice([(3, 4, 5), (6, 8, 10), (5, 12, 13), (8, 15, 17)])

    prompt = (
        f"A rectangle is constructed with length **${l}\\text{{ cm}}$** and breadth **${b}\\text{{ cm}}$**.\n\n"
        f"Using the Theorem of Pythagoras, calculate the length of the **diagonal** of the rectangle in centimetres."
    )

    return {
        "subskill": "31_construct_rectangle_given_length_and_breadth",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": str(d),
        "sample_answer": f"{d} cm",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Recall that adjacent sides of a rectangle meet at 90°, forming right-angled triangles with the diagonal", "marks": 1},
            {"step": f"Apply Pythagoras: diagonal = √({l}^2 + {b}^2) = √({l**2 + b**2}) = {d} cm", "marks": 1},
        ],
        "hints": [
            "The diagonal splits the rectangle into two congruent right-angled triangles.",
            f"Diagonal $= \\sqrt{{{l}^2 + {b}^2}} = \\sqrt{{{l**2 + b**2}}}$.",
            f"Length $= {d}\\text{{ cm}}$.",
        ],
        "misconception_tags": ["rectangle_diagonal_pythagoras_error", "hypotenuse_arithmetic_error"],
    }


def arch_32_construct_parallelogram_given_two_sides_and_angle(rng: random.Random) -> Dict[str, Any]:
    """Construct parallelogram; calculate adjacent co-interior angle."""
    acute_deg = rng.choice([50, 55, 60, 65, 70, 75, 80])
    obtuse_deg = 180 - acute_deg

    prompt = (
        f"In constructing a parallelogram $ABCD$, one interior angle is constructed as **${acute_deg}^\\circ$**.\n\n"
        f"Because adjacent interior angles between parallel lines are co-interior (supplementary), "
        f"calculate the size of the adjacent obtuse angle in degrees ($^\\circ$)."
    )

    return {
        "subskill": "32_construct_parallelogram_given_two_sides_and_angle",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": str(obtuse_deg),
        "sample_answer": f"{obtuse_deg}°",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "State that consecutive adjacent angles in a parallelogram are supplementary (sum to 180°)", "marks": 1},
            {"step": f"Calculate: 180° - {acute_deg}° = {obtuse_deg}°", "marks": 1},
        ],
        "hints": [
            "Adjacent angles between parallel sides sum to $180^\\circ$ (co-interior angles).",
            f"Subtract ${acute_deg}^\\circ$ from $180^\\circ$.",
            f"Adjacent angle $= {obtuse_deg}^\\circ$.",
        ],
        "misconception_tags": ["parallelogram_cointerior_angles_error", "opposite_vs_adjacent_angles_confusion"],
    }


def arch_33_construct_rhombus_given_side_and_diagonal(rng: random.Random) -> Dict[str, Any]:
    """Properties of rhombus diagonals (perpendicular bisectors)."""
    side = rng.choice([5, 10, 13])
    if side == 5:
        d1, d2 = 6, 8
    elif side == 10:
        d1, d2 = 12, 16
    else:
        d1, d2 = 10, 24

    prompt = (
        f"A rhombus $PQRS$ is constructed with side length **${side}\\text{{ cm}}$** and one diagonal "
        f"measuring **${d1}\\text{{ cm}}$**.\n\n"
        f"1. At what angle do the two diagonals of a rhombus intersect each other?\n"
        f"2. Using the fact that diagonals bisect each other at right angles, calculate the length of the "
        f"**second diagonal** in centimetres."
    )

    return {
        "subskill": "33_construct_rhombus_given_side_and_diagonal",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": str(d2),
        "sample_answer": f"{d2} cm (diagonals intersect at 90°)",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Identify half-diagonal: d1 / 2 = {d1 // 2} cm", "marks": 1},
            {"step": f"Apply Pythagoras to right triangle: (d2 / 2)^2 = {side}^2 - {d1 // 2}^2 = {side**2 - (d1//2)**2}", "marks": 1},
            {"step": f"Calculate full diagonal: d2 = 2 * {d2 // 2} = {d2} cm", "marks": 1},
        ],
        "hints": [
            "The diagonals of a rhombus bisect each other perpendicularly at $90^\\circ$.",
            f"Each quadrant is a right-angled triangle with hypotenuse ${side}$ and one leg ${d1 // 2}$.",
            f"The other half-diagonal is $\\sqrt{{{side}^2 - {d1 // 2}^2}} = {d2 // 2}$, so the full diagonal is ${d2}\\text{{ cm}}$.",
        ],
        "misconception_tags": ["rhombus_diagonal_properties", "forgot_to_double_half_diagonal"],
    }


def arch_34_construct_regular_hexagon_inscribed_in_circle(rng: random.Random) -> Dict[str, Any]:
    """Construct regular hexagon inscribed in circle of radius r; perimeter = 6r."""
    r = rng.choice([3, 4, 5, 6, 7, 8])
    perimeter = 6 * r

    prompt = (
        f"A regular hexagon is constructed by drawing a circle of radius **${r}\\text{{ cm}}$** and stepping "
        f"off the exact same radius with the compass around the circumference six times.\n\n"
        f"Calculate the **perimeter** of the regular hexagon in centimetres."
    )

    return {
        "subskill": "34_construct_regular_hexagon_inscribed_in_circle",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": str(perimeter),
        "sample_answer": f"{perimeter} cm",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Recognize that each side of an inscribed regular hexagon equals the circle radius (s = r = {r} cm)", "marks": 1},
            {"step": f"Calculate perimeter: 6 * {r} = {perimeter} cm", "marks": 1},
        ],
        "hints": [
            f"A regular hexagon is composed of $6$ equilateral triangles meeting at the center, so side length $= r = {r}\\text{{ cm}}$.",
            f"Perimeter $= 6 \\times {r} = {perimeter}\\text{{ cm}}$.",
            f"Answer: **{perimeter}**.",
        ],
        "misconception_tags": ["regular_hexagon_radius_equality", "hexagon_perimeter_formula"],
    }


def arch_35_circumcentre_and_circumscribed_circle(rng: random.Random) -> Dict[str, Any]:
    """Circumcentre definition: concurrency of perpendicular bisectors."""
    seed_val = rng.randint(1000, 999999)
    svg = draw_circumcircle_or_incircle_svg(is_incircle=False, seed=seed_val)

    prompt = (
        f"Refer to the geometric construction of a circumscribed circle (circumcircle) shown below:\n\n"
        f"The **circumcentre** of a triangle is constructed at the point of concurrency of the:\n"
        f"Answer: **perpendicular bisectors of the sides**"
    )

    return {
        "subskill": "35_circumcentre_and_circumscribed_circle",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": "perpendicular bisectors of the sides",
        "sample_answer": "perpendicular bisectors of the sides",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "State that the circumcentre is the intersection point of the perpendicular bisectors of the 3 sides", "marks": 1},
            {"step": "Recall that this point is equidistant from all three vertices (OA = OB = OC = R)", "marks": 1},
        ],
        "hints": [
            "The circumcircle passes through all three vertices of the triangle.",
            "Its center (circumcentre) is equidistant from the vertices.",
            "Answer: **perpendicular bisectors of the sides**.",
        ],
        "misconception_tags": ["circumcentre_vs_incentre_confusion", "perpendicular_bisectors_concurrency"],
    }


def arch_36_incentre_and_inscribed_circle(rng: random.Random) -> Dict[str, Any]:
    """Incentre definition: concurrency of angle bisectors."""
    seed_val = rng.randint(1000, 999999)
    svg = draw_circumcircle_or_incircle_svg(is_incircle=True, seed=seed_val)

    prompt = (
        f"Refer to the inscribed circle (incircle) construction shown below:\n\n"
        f"The **incentre** of a triangle is constructed at the point of concurrency of the:\n"
        f"Answer: **angle bisectors**"
    )

    return {
        "subskill": "36_incentre_and_inscribed_circle",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": "angle bisectors",
        "sample_answer": "angle bisectors",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "State that the incentre is the intersection point of the three interior angle bisectors", "marks": 1},
            {"step": "Recall that the incentre is equidistant from the three sides (radius r to all sides)", "marks": 1},
        ],
        "hints": [
            "The incircle lies entirely inside the triangle and touches all three sides.",
            "Its center is found by bisecting the three interior angles.",
            "Answer: **angle bisectors**.",
        ],
        "misconception_tags": ["incentre_definition_error", "angle_bisectors_concurrency"],
    }


def arch_37_centroid_intersection_of_medians(rng: random.Random) -> Dict[str, Any]:
    """Centroid divides median in 2:1 ratio from vertex to midpoint."""
    # Total median M = 3 * k
    k = rng.choice([3, 4, 5, 6, 7])
    m_total = 3 * k
    dist_vertex_to_centroid = 2 * k
    dist_centroid_to_base = k

    prompt = (
        f"In triangle $\\triangle ABC$, the three medians intersect at the **centroid ($G$)**.\n"
        f"A median drawn from vertex $A$ to the midpoint of opposite side $BC$ has a total length of **${m_total}\\text{{ cm}}$**.\n\n"
        f"Because the centroid divides every median in a **$2 : 1$ ratio** from the vertex, calculate the "
        f"distance from vertex $A$ to the centroid ($AG$) in centimetres."
    )

    return {
        "subskill": "37_centroid_intersection_of_medians",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": str(dist_vertex_to_centroid),
        "sample_answer": f"{dist_vertex_to_centroid} cm",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "State that the centroid divides a median in a 2:1 ratio (vertex distance = 2/3 of total length)", "marks": 1},
            {"step": f"Calculate AG = (2/3) * {m_total} = {dist_vertex_to_centroid} cm", "marks": 1},
        ],
        "hints": [
            "The centroid divides the median into 3 equal units: 2 units from the vertex and 1 unit to the base.",
            f"One unit $= {m_total} \\div 3 = {k}\\text{{ cm}}$.",
            f"Distance from vertex $= 2 \\times {k} = {dist_vertex_to_centroid}\\text{{ cm}}$.",
        ],
        "misconception_tags": ["centroid_ratio_inversion", "median_division_arithmetic_error"],
    }


def arch_38_orthocentre_intersection_of_altitudes(rng: random.Random) -> Dict[str, Any]:
    """Orthocentre definition and right-angled triangle property."""
    prompt = (
        f"The **orthocentre** of a triangle is the point where the three **altitudes** (perpendicular heights from "
        f"vertices to opposite sides) intersect.\n\n"
        f"For a **right-angled triangle**, where is the orthocentre located?\n"
        f"State: **at the right-angle vertex**"
    )

    return {
        "subskill": "38_orthocentre_intersection_of_altitudes",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": "at the right-angle vertex",
        "sample_answer": "at the right-angle vertex",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Identify that the two legs of a right-angled triangle serve as altitudes to each other", "marks": 1},
            {"step": "Conclude that all three altitudes meet at the vertex containing the 90° right angle", "marks": 1},
        ],
        "hints": [
            "The two legs of a right triangle are already perpendicular to each other, so they are altitudes.",
            "They meet at the right angle vertex.",
            "Answer: **at the right-angle vertex**.",
        ],
        "misconception_tags": ["orthocentre_location_confusion", "altitude_properties_in_right_triangle"],
    }


def arch_39_circumcentre_location_acute_right_obtuse(rng: random.Random) -> Dict[str, Any]:
    """Location of circumcentre based on triangle type."""
    t_type = rng.choice(["acute", "right-angled", "obtuse"])
    if t_type == "acute":
        location = "inside the triangle"
    elif t_type == "right-angled":
        location = "on the hypotenuse midpoint"
    else:
        location = "outside the triangle"

    prompt = (
        f"Consider a constructed **{t_type} triangle**.\n\n"
        f"Where is its **circumcentre** located?\n"
        f"State: **{location}**"
    )

    return {
        "subskill": "39_circumcentre_location_acute_right_obtuse",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": location,
        "sample_answer": location,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Recall geometric theorem: for a {t_type} triangle, the circumcentre lies {location}", "marks": 1},
        ],
        "hints": [
            "Acute triangles have the circumcentre inside.",
            "Right-angled triangles have the circumcentre on the midpoint of the hypotenuse.",
            "Obtuse triangles have the circumcentre outside.",
            f"Answer: **{location}**.",
        ],
        "misconception_tags": ["circumcentre_triangle_type_location", "geometric_center_exterior_locus"],
    }


def arch_40_tangent_to_a_circle_perpendicular_to_radius(rng: random.Random) -> Dict[str, Any]:
    """Tangent to circle is perpendicular to radius at point of contact (calculate tangent length)."""
    # Right-angled triangle: radius r, tangent length t, hypotenuse OP
    r, t, op = rng.choice([(3, 4, 5), (6, 8, 10), (5, 12, 13), (8, 15, 17)])

    prompt = (
        f"A circle has a radius of **${r}\\text{{ cm}}$** and center $O$.\n"
        f"A tangent line is constructed from an external point $P$ touching the circle at point $T$.\n"
        f"The distance from $O$ to $P$ is **${op}\\text{{ cm}}$**.\n\n"
        f"Because the tangent is perpendicular to the radius ($OT \\perp PT$), use the Theorem of Pythagoras "
        f"to calculate the **length of tangent segment $PT$** in centimetres."
    )

    return {
        "subskill": "40_tangent_to_a_circle_perpendicular_to_radius",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": str(t),
        "sample_answer": f"{t} cm (angle OTP = 90°)",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "State tangent theorem: tangent is perpendicular to radius at point of contact (∠OTP = 90°)", "marks": 1},
            {"step": f"Apply Pythagoras: PT = √(OP^2 - OT^2) = √({op}^2 - {r}^2) = {t} cm", "marks": 1},
        ],
        "hints": [
            "The radius $OT$ and tangent $PT$ form a $90^\\circ$ right angle at $T$.",
            f"$PT = \\sqrt{{{op}^2 - {r}^2}} = \\sqrt{{{op**2} - {r**2}}}$.",
            f"Tangent length $PT = {t}\\text{{ cm}}$.",
        ],
        "misconception_tags": ["tangent_radius_perpendicular_theorem", "pythagoras_tangent_calculation"],
    }


def arch_41_tangents_from_external_point_equal_length(rng: random.Random) -> Dict[str, Any]:
    """Two tangents from an external point are equal in length (solve algebraic equation)."""
    # PT1 = ax + b, PT2 = cx + d => PT1 = PT2
    x_val = rng.choice([3, 4, 5, 6])
    c = rng.choice([1, 2])
    a = c + rng.choice([1, 2])
    b = rng.randint(2, 6)
    d = (a - c) * x_val + b
    tangent_len = a * x_val + b

    prompt = (
        f"Two tangents are constructed from an external point $P$ to a circle, touching the circle at $T_1$ and $T_2$.\n"
        f"Their lengths are given algebraically as:\n"
        f"- $PT_1 = {a}x + {b}\\text{{ cm}}$\n"
        f"- $PT_2 = {c}x + {d}\\text{{ cm}}$\n\n"
        f"1. State the relationship between two tangents drawn from the same external point.\n"
        f"2. Solve for $x$ and calculate the **length of tangent $PT_1$** in centimetres."
    )

    return {
        "subskill": "41_tangents_from_external_point_equal_length",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": str(tangent_len),
        "sample_answer": f"{tangent_len} cm (x = {x_val})",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "State theorem: tangents drawn to a circle from the same external point are equal in length (PT1 = PT2)", "marks": 1},
            {"step": f"Solve equation: {a}x + {b} = {c}x + {d} => x = {x_val}", "marks": 1},
            {"step": f"Calculate PT1 = {a}({x_val}) + {b} = {tangent_len} cm", "marks": 1},
        ],
        "hints": [
            "Tangents from the same external point to a circle are equal in length ($PT_1 = PT_2$).",
            f"Set ${a}x + {b} = {c}x + {d}$ and solve for $x = {x_val}$.",
            f"Substitute $x = {x_val}$: $PT_1 = {tangent_len}\\text{{ cm}}$.",
        ],
        "misconception_tags": ["tangents_from_external_point_theorem", "equating_tangent_lengths_error"],
    }


def arch_42_common_chord_of_two_intersecting_circles(rng: random.Random) -> Dict[str, Any]:
    """Common chord of two intersecting circles perpendicularly bisected by line of centers."""
    # Distance from center to chord = d, half chord = y, radius = r
    # (3, 4, 5) or (6, 8, 10)
    d, half_chord, r = rng.choice([(3, 4, 5), (4, 3, 5), (6, 8, 10), (8, 6, 10)])
    full_chord = 2 * half_chord

    prompt = (
        f"Two congruent circles with radius **${r}\\text{{ cm}}$** intersect at two points, forming a common chord.\n"
        f"The line connecting the centers of the two circles is perpendicular to the common chord and passes "
        f"**${d}\\text{{ cm}}$** from the center of either circle.\n\n"
        f"Calculate the **total length of the common chord** in centimetres."
    )

    return {
        "subskill": "42_common_chord_of_two_intersecting_circles",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": str(full_chord),
        "sample_answer": f"{full_chord} cm",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Apply Pythagoras to find half-chord: y = √({r}^2 - {d}^2) = {half_chord} cm", "marks": 1},
            {"step": f"Double to get full common chord: 2 * {half_chord} = {full_chord} cm", "marks": 1},
        ],
        "hints": [
            f"The line of centers bisects the common chord perpendicularly.",
            f"Half-chord $= \\sqrt{{{r}^2 - {d}^2}} = {half_chord}\\text{{ cm}}$.",
            f"Total length $= 2 \\times {half_chord} = {full_chord}\\text{{ cm}}$.",
        ],
        "misconception_tags": ["common_chord_bisector_theorem", "forgot_to_double_half_chord"],
    }


def arch_43_scale_drawing_triangle_actual_distance(rng: random.Random) -> Dict[str, Any]:
    """Scale drawing: convert paper construction cm to real-world metres."""
    scale_factor = rng.choice([5, 10, 20, 50])  # 1 cm = scale_factor metres
    paper_cm = rng.choice([6, 7, 8, 9, 11, 12])
    real_metres = paper_cm * scale_factor

    prompt = (
        f"A surveyor draws an accurate scale construction of a triangular plot of land.\n"
        f"The scale is **$1\\text{{ cm}} : {scale_factor}\\text{{ metres}}$**.\n"
        f"On the drawing, the length of the fence boundary is measured as **${paper_cm}\\text{{ cm}}$**.\n\n"
        f"Calculate the **actual length** of the boundary in metres."
    )

    return {
        "subskill": "43_scale_drawing_triangle_actual_distance",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": str(real_metres),
        "sample_answer": f"{real_metres} m",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Apply scale ratio: actual length = paper length * scale factor", "marks": 1},
            {"step": f"Calculate: {paper_cm} cm * {scale_factor} m/cm = {real_metres} metres", "marks": 1},
        ],
        "hints": [
            f"Every $1\\text{{ cm}}$ on paper equals ${scale_factor}\\text{{ metres}}$ in real life.",
            f"Multiply: ${paper_cm} \\times {scale_factor}$.",
            f"Actual distance $= {real_metres}\\text{{ metres}}$.",
        ],
        "misconception_tags": ["scale_ratio_division_instead_of_multiplication", "scale_unit_conversion_error"],
    }


def arch_44_three_figure_bearing_construction(rng: random.Random) -> Dict[str, Any]:
    """Calculate back bearing (opposite direction) for three-figure bearing."""
    forward_deg = rng.choice([40, 65, 80, 115, 130])
    back_bearing = forward_deg + 180
    forward_str = f"{forward_deg:03d}°"
    back_str = f"{back_bearing:03d}°"

    prompt = (
        f"A ship sails from port $A$ to lighthouse $B$ on a three-figure bearing of **${forward_str}$**.\n\n"
        f"Calculate the **back bearing** from lighthouse $B$ to port $A$ in degrees ($^\\circ$)."
    )

    return {
        "subskill": "44_three_figure_bearing_construction",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": str(back_bearing),
        "sample_answer": back_str,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "State back bearing rule: if bearing < 180°, back bearing = bearing + 180°", "marks": 1},
            {"step": f"Calculate: {forward_deg}° + 180° = {back_bearing}°", "marks": 1},
        ],
        "hints": [
            "The back bearing is in the exact opposite direction ($180^\\circ$ reverse).",
            f"Add $180^\\circ$: ${forward_deg}^\\circ + 180^\\circ = {back_bearing}^\\circ$.",
            f"Back bearing is **{back_str}**.",
        ],
        "misconception_tags": ["three_figure_bearing_convention", "back_bearing_calculation_error"],
    }


def arch_45_compass_radius_error_non_intersecting_arcs(rng: random.Random) -> Dict[str, Any]:
    """Diagnose why construction arcs fail to intersect when compass radius is too small."""
    ab_len = rng.choice([10, 12, 14, 16])
    half_len = ab_len // 2
    small_r = half_len - 1

    prompt = (
        f"A learner attempts to construct the perpendicular bisector of a line segment $AB = {ab_len}\\text{{ cm}}$.\n"
        f"The learner sets the compass radius to **${small_r}\\text{{ cm}}$** and draws arcs from $A$ and $B$, "
        f"but the arcs do not cross or intersect at all.\n\n"
        f"1. Explain why the arcs failed to intersect.\n"
        f"2. What is the **strict mathematical condition** for the compass radius $r$ relative to length $AB$?\n"
        f"State: **r > {half_len} cm** (strictly greater than half the segment length)"
    )

    return {
        "subskill": "45_compass_radius_error_non_intersecting_arcs",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": f"r > {half_len} cm",
        "sample_answer": f"r > {half_len} cm",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Diagnose error: compass radius {small_r} cm is less than half the segment length ({half_len} cm)", "marks": 1},
            {"step": f"State condition: r must be strictly greater than AB / 2 (r > {half_len} cm)", "marks": 1},
        ],
        "hints": [
            f"Half of segment $AB$ is ${half_len}\\text{{ cm}}$.",
            f"If radius is ${small_r}\\text{{ cm}}$, the two arcs cannot reach each other across the gap.",
            f"The radius must satisfy $r > \\frac{{AB}}{{2}}$, meaning **r > {half_len} cm**.",
        ],
        "misconception_tags": ["compass_radius_insufficient_error", "arc_intersection_geometric_condition"],
    }


def arch_46_error_analysis_protractor_inner_vs_outer_scale(rng: random.Random) -> Dict[str, Any]:
    """Diagnose protractor inner vs outer scale misreading for an obtuse angle."""
    acute_read = rng.choice([40, 50, 60, 70])
    correct_obtuse = 180 - acute_read

    prompt = (
        f"A learner measures an **obtuse angle** using a protractor and records the measurement as **${acute_read}^\\circ$**.\n\n"
        f"1. What error did the learner make regarding the protractor scales?\n"
        f"2. What is the **correct actual size** of this obtuse angle in degrees ($^\\circ$)?"
    )

    return {
        "subskill": "46_error_analysis_protractor_inner_vs_outer_scale",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": str(correct_obtuse),
        "sample_answer": f"{correct_obtuse}°",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Diagnose error: learner read the wrong scale (inner acute scale instead of outer obtuse scale)", "marks": 1},
            {"step": f"Calculate correct angle: 180° - {acute_read}° = {correct_obtuse}°", "marks": 1},
        ],
        "hints": [
            "An obtuse angle must be strictly greater than $90^\\circ$.",
            f"The learner read ${acute_read}^\\circ$ on the complementary scale.",
            f"Correct measurement $= 180^\\circ - {acute_read}^\\circ = {correct_obtuse}^\\circ$.",
        ],
        "misconception_tags": ["protractor_inner_outer_scale_confusion", "obtuse_angle_reading_error"],
    }


def arch_47_error_analysis_ambiguous_triangle_ssa_not_congruent(rng: random.Random) -> Dict[str, Any]:
    """Explain why Side-Side-Angle (SSA) does not guarantee a unique triangle."""
    prompt = (
        f"In Euclidean geometry, four conditions prove triangle congruency: SSS, SAS, ASA/AAS, and RHS.\n\n"
        f"Why is **Side-Side-Angle (SSA)** (two sides and a non-included angle) NOT a valid congruency condition?\n"
        f"State: **it can form two different triangles (ambiguous case)**"
    )

    return {
        "subskill": "47_error_analysis_ambiguous_triangle_ssa_not_congruent",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": "it can form two different triangles (ambiguous case)",
        "sample_answer": "it can form two different triangles (ambiguous case)",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Explain that swinging the opposite side with a compass can intersect the base in two different locations", "marks": 1},
            {"step": "Conclude that two non-congruent triangles (one acute, one obtuse) can share the same SSA data", "marks": 1},
        ],
        "hints": [
            "When the angle is not included between the sides, the swinging side can create two different triangles.",
            "This is known as the ambiguous case.",
            "Answer: **it can form two different triangles (ambiguous case)**.",
        ],
        "misconception_tags": ["ssa_ambiguous_case_misconception", "congruency_conditions_rigor"],
    }


def arch_48_dividing_line_segment_into_n_equal_parts(rng: random.Random) -> Dict[str, Any]:
    """Dividing line segment into n equal parts using parallel construction rays."""
    n = rng.choice([3, 4, 5])
    total_len = n * rng.choice([3, 4, 5])
    each_part = total_len // n

    prompt = (
        f"A line segment $AB = {total_len}\\text{{ cm}}$ is divided into **${n}$ equal parts** using an auxiliary ray "
        f"and parallel line constructions with a compass and straightedge.\n\n"
        f"Calculate the length of each equal subdivision in centimetres."
    )

    return {
        "subskill": "48_dividing_line_segment_into_n_equal_parts",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": str(each_part),
        "sample_answer": f"{each_part} cm",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Apply equal subdivision: length of each part = total length / n", "marks": 1},
            {"step": f"Calculate: {total_len} cm / {n} = {each_part} cm", "marks": 1},
        ],
        "hints": [
            f"The segment of length ${total_len}\\text{{ cm}}$ is divided into ${n}$ equal pieces.",
            f"Divide: ${total_len} \\div {n} = {each_part}\\text{{ cm}}$.",
            f"Answer: **{each_part}**.",
        ],
        "misconception_tags": ["segment_subdivision_arithmetic_error", "parallel_ray_division_properties"],
    }


def arch_49_geometric_locus_equidistant_from_two_intersecting_lines(rng: random.Random) -> Dict[str, Any]:
    """Locus of points equidistant from two intersecting lines is the angle bisectors."""
    prompt = (
        f"Two roads cross each other at an angle $\\theta$.\n\n"
        f"What geometric construction represents the locus of all points that are **equidistant** from both roads?\n"
        f"State: **the angle bisectors**"
    )

    return {
        "subskill": "49_geometric_locus_equidistant_from_two_intersecting_lines",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": "the angle bisectors",
        "sample_answer": "the angle bisectors",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "State locus definition: points equidistant from two intersecting lines lie along the bisectors of the angles between them", "marks": 1},
        ],
        "hints": [
            "Any point on an angle bisector is the exact same distance from both arms.",
            "For two intersecting lines, there are two perpendicular bisector lines (bisecting the acute and obtuse angles).",
            "Answer: **the angle bisectors**.",
        ],
        "misconception_tags": ["locus_from_lines_vs_points_confusion", "angle_bisector_as_equidistant_locus"],
    }


def arch_50_compound_multi_step_geometric_construction_synthesis(rng: random.Random) -> Dict[str, Any]:
    """Right-angled triangle circumradius R = hypotenuse / 2."""
    a, b, c = rng.choice([(6, 8, 10), (8, 6, 10), (5, 12, 13), (12, 5, 13)])
    # Circumradius of right-angled triangle is c / 2
    r_circum = c / 2
    ans_str = f"{r_circum:.1f}".rstrip("0").rstrip(".")

    prompt = (
        f"A right-angled triangle $\\triangle ABC$ with right angle at $B$ has sides:\n"
        f"- $AB = {a}\\text{{ cm}}$\n"
        f"- $BC = {b}\\text{{ cm}}$\n"
        f"- Hypotenuse $AC = {c}\\text{{ cm}}$\n\n"
        f"A circumscribed circle is constructed around this triangle:\n"
        f"1. Identify the location of the circumcentre.\n"
        f"2. Calculate the **radius of the circumcircle** in centimetres."
    )

    return {
        "subskill": "50_compound_multi_step_geometric_construction_synthesis",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": ans_str,
        "sample_answer": f"{ans_str} cm (circumcentre is at the midpoint of hypotenuse AC)",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Recall that for a right-angled triangle, the hypotenuse is the diameter of the circumcircle", "marks": 1},
            {"step": f"Calculate circumradius: R = hypotenuse / 2 = {c} / 2 = {ans_str} cm", "marks": 1},
        ],
        "hints": [
            "In any right-angled triangle, the circumcentre lies exactly at the midpoint of the hypotenuse.",
            "The hypotenuse is the diameter of the circumscribed circle.",
            f"Radius $= \\frac{{{c}}}{{2}} = {ans_str}\\text{{ cm}}$.",
        ],
        "misconception_tags": ["right_triangle_circumradius_theorem", "hypotenuse_as_circumdiameter"],
    }
