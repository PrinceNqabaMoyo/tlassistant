"""Grade 11 Mathematics — Analytical Geometry Archetypes 26–50.
Grounded in South African National Curriculum Standards for Grade 11 Mathematics (Term 2).
Covers:
- Perpendicular bisector of a segment with inline_svg
- Properties and proofs of quadrilaterals: Parallelogram, Rhombus, Rectangle, Square, Trapezium, Kite
- Finding fourth vertex of parallelogram using midpoint formula
- Areas of triangles and quadrilaterals in coordinate plane
- Intersection of straight lines, intercepts, distance from origin
- Coordinate proof of the Midpoint Theorem with inline_svg
- Centroid of triangle, reflections across axes and y = x
- Comprehensive multi-step examination analysis of geometric figures with inline_svg
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
from app.utils.grade11_mathematics.analytical_geometry_archetypes_01_25 import (
    _cartesian_geometry_svg,
)

TOPIC = "Analytical geometry"
LO_PREFIX = "math11_analgeo"


# ---------------------------------------------------------------------------
# 26. Perpendicular Bisector of a Segment (with inline_svg)
# ---------------------------------------------------------------------------
def build_26_perpendicular_bisector_of_segment(r: random.Random) -> Dict[str, Any]:
    sx = r.choice([-2, -1, 0, 1])
    sy = r.choice([-2, -1, 0, 1])
    A = (0 + sx, 0 + sy, "A")
    B = (4 + sx, 2 + sy, "B")
    M = (2 + sx, 1 + sy, "M")
    c_val = 5 + 2 * sx + sy

    d_spec = _cartesian_geometry_svg(
        points=[(float(A[0]), float(A[1]), "A"), (float(B[0]), float(B[1]), "B"), (float(M[0]), float(M[1]), "M")],
        segments=[(0, 1)],
    )

    c_str = f"+ {c_val}" if c_val >= 0 else f"- {abs(c_val)}"
    eq_str = rf"y = -2x {c_str}"
    prompt = (
        f"In the accompanying diagram, segment $AB$ connects $A({A[0]}; {A[1]})$ and $B({B[0]}; {B[1]})$.\n\n"
        f"Determine the equation of the perpendicular bisector of $AB$ in the form $y = mx + c$."
    )
    ans_latex = eq_str
    sample = (
        rf"1. \text{{Midpoint }} M = \left(\frac{{{A[0]} + {B[0]}}}{{2}}; \frac{{{A[1]} + {B[1]}}}{{2}}\right) = M({M[0]}; {M[1]})\\"
        rf"2. \text{{Gradient }} m_{{AB}} = \frac{{{B[1]} - ({A[1]})}}{{{B[0]} - ({A[0]})}} = \frac{{2}}{{4}} = \frac{{1}}{{2}}\\"
        rf"3. \text{{Perpendicular gradient: }} m_{{\perp}} = -\frac{{1}}{{1/2}} = -2\\"
        rf"4. \text{{Equation through }} M({M[0]}; {M[1]}):\\"
        rf"y - ({M[1]}) = -2(x - ({M[0]})) \implies {eq_str}"
    )

    return make_math_question(
        prefix="analgeo_26",
        topic=TOPIC,
        subskill="26_perpendicular_bisector_of_segment",
        learning_objective_id=f"{LO_PREFIX}_perp_bisector",
        prompt=prompt,
        prompt_latex=rf"A({A[0]}; {A[1]}), \; B({B[0]}; {B[1]})",
        answer_latex=ans_latex,
        answer_sympy=ans_latex,
        sample_answer=sample,
        marking_schema={
            "total_marks": 4,
            "marking_points": [
                {"id": "mp1", "desc": f"Calculated midpoint M({M[0]}; {M[1]})", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Calculated gradient m_AB = 1/2", "marks": 1, "editable": True},
                {"id": "mp3", "desc": "Found perpendicular gradient m = -2", "marks": 1, "editable": True},
                {"id": "mp4", "desc": f"Final equation: {eq_str}", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        hints={
            "1_nudge": "Find the midpoint of $AB$ first: the bisector passes through this point.",
            "2_concept": "The perpendicular bisector has gradient $m = -\\frac{1}{m_{AB}}$.",
            "3_breakdown": f"Equation is ${eq_str}$.",
        },
        misconception_tags=["used_endpoint_instead_of_midpoint_for_bisector"],
        keywords=["perpendicular bisector", "midpoint", "perpendicular gradient"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=4,
        mode="26_perpendicular_bisector_of_segment",
        difficulty="hard",
        diagram_spec=d_spec,
    )


# ---------------------------------------------------------------------------
# 27. Parallelogram: Diagonals Bisect Proof (with inline_svg)
# ---------------------------------------------------------------------------
def build_27_parallelogram_diagonals_bisect_property(r: random.Random) -> Dict[str, Any]:
    sx = r.choice([-2, -1, 0, 1])
    sy = r.choice([-2, -1, 0, 1])
    A = (1 + sx, 1 + sy, "A")
    B = (4 + sx, 2 + sy, "B")
    C = (5 + sx, 5 + sy, "C")
    D = (2 + sx, 4 + sy, "D")
    mx = 3 + sx
    my = 3 + sy

    d_spec = _cartesian_geometry_svg(
        points=[(float(A[0]), float(A[1]), "A"), (float(B[0]), float(B[1]), "B"), (float(C[0]), float(C[1]), "C"), (float(D[0]), float(D[1]), "D")],
        segments=[(0, 1), (1, 2), (2, 3), (3, 0), (0, 2), (1, 3)],
    )

    prompt = (
        f"In the accompanying diagram, quadrilateral $ABCD$ has vertices $A({A[0]}; {A[1]})$, $B({B[0]}; {B[1]})$, "
        f"$C({C[0]}; {C[1]})$, and $D({D[0]}; {D[1]})$.\n\n"
        f"Prove that $ABCD$ is a parallelogram by showing that its diagonals bisect each other."
    )
    ans_latex = rf"\text{{Midpoint of }} AC = \text{{Midpoint of }} BD = ({mx}; {my}) \implies ABCD \text{{ is a parallelogram}}"
    sample = (
        rf"\text{{Midpoint of diagonal }} AC = \left(\frac{{{A[0]} + {C[0]}}}{{2}}; \frac{{{A[1]} + {C[1]}}}{{2}}\right) = ({mx}; {my})\\"
        rf"\text{{Midpoint of diagonal }} BD = \left(\frac{{{B[0]} + {D[0]}}}{{2}}; \frac{{{B[1]} + {D[1]}}}{{2}}\right) = ({mx}; {my})\\"
        rf"\text{{Since the midpoints of diagonals }} AC \text{{ and }} BD \text{{ coincide, the diagonals bisect each other.}}\\"
        rf"\therefore ABCD \text{{ is a parallelogram.}}"
    )

    return make_math_question(
        prefix="analgeo_27",
        topic=TOPIC,
        subskill="27_parallelogram_diagonals_bisect_property",
        learning_objective_id=f"{LO_PREFIX}_diagonals_bisect",
        prompt=prompt,
        prompt_latex=rf"A({A[0]}; {A[1]}), \; B({B[0]}; {B[1]}), \; C({C[0]}; {C[1]}), \; D({D[0]}; {D[1]})",
        answer_latex=ans_latex,
        answer_sympy=ans_latex,
        sample_answer=sample,
        marking_schema={
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": f"Calculated midpoint of diagonal AC = ({mx}; {my})", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Calculated midpoint of diagonal BD = ({mx}; {my})", "marks": 1, "editable": True},
                {"id": "mp3", "desc": "Concluded parallelogram due to coinciding midpoints", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        hints={
            "1_nudge": "Calculate the midpoint of diagonal $AC$ and diagonal $BD$.",
            "2_concept": "A quadrilateral whose diagonals bisect each other is a parallelogram.",
            "3_breakdown": f"Both midpoints are $({mx}; {my})$, proving $ABCD$ is a parallelogram.",
        },
        misconception_tags=["paired_adjacent_points_as_diagonals"],
        keywords=["parallelogram", "diagonals bisect", "midpoint proof"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=3,
        mode="27_parallelogram_diagonals_bisect_property",
        difficulty="medium",
        diagram_spec=d_spec,
    )


# ---------------------------------------------------------------------------
# 28. Parallelogram: Find Fourth Vertex
# ---------------------------------------------------------------------------
def build_28_parallelogram_find_fourth_vertex(r: random.Random) -> Dict[str, Any]:
    xA = r.choice([1, 2, 3])
    yA = r.choice([1, 2, 3])
    dx1 = r.choice([4, 6])
    dy1 = r.choice([2, 4])
    dx2 = r.choice([2, 4])
    dy2 = r.choice([4, 6])
    xB, yB = xA + dx1, yA + dy1
    xD, yD = xA + dx2, yA + dy2
    xC, yC = xB + dx2, yB + dy2
    mx = (xA + xC) // 2
    my = (yA + yC) // 2

    prompt = (
        f"The points $A({xA}; {yA})$, $B({xB}; {yB})$, and $C({xC}; {yC})$ are three vertices of parallelogram $ABCD$.\n\n"
        f"Determine the coordinates of the fourth vertex $D$."
    )
    ans_latex = rf"D({xD}; {yD})"
    sample = (
        rf"\text{{In parallelogram }} ABCD \text{{, the diagonals }} AC \text{{ and }} BD \text{{ have the same midpoint:}}\\"
        rf"\text{{Midpoint of }} AC = \left(\frac{{{xA} + {xC}}}{{2}}; \frac{{{yA} + {yC}}}{{2}}\right) = ({mx}; {my})\\"
        rf"\frac{{x_B + x_D}}{{2}} = {mx} \implies {xB} + x_D = {2*mx} \implies x_D = {xD}\\"
        rf"\frac{{y_B + y_D}}{{2}} = {my} \implies {yB} + y_D = {2*my} \implies y_D = {yD}\\"
        rf"\therefore D({xD}; {yD})"
    )

    return make_math_question(
        prefix="analgeo_28",
        topic=TOPIC,
        subskill="28_parallelogram_find_fourth_vertex",
        learning_objective_id=f"{LO_PREFIX}_find_fourth_vertex",
        prompt=prompt,
        prompt_latex=rf"A({xA}; {yA}), \; B({xB}; {yB}), \; C({xC}; {yC})",
        answer_latex=ans_latex,
        answer_sympy=f"({xD}, {yD})",
        sample_answer=sample,
        marking_schema={
            "total_marks": 4,
            "marking_points": [
                {"id": "mp1", "desc": "Calculated midpoint of diagonal AC", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Equated to midpoint of diagonal BD", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Solved x_D = {xD}", "marks": 1, "editable": True},
                {"id": "mp4", "desc": f"Solved y_D = {yD}", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        hints={
            "1_nudge": "Use the fact that diagonals $AC$ and $BD$ share the exact same midpoint.",
            "2_concept": "Alternatively, use the translation vector: from $B$ to $A$ is the same shift as from $C$ to $D$.",
            "3_breakdown": f"Vertex is $D({xD}; {yD})$.",
        },
        misconception_tags=["paired_wrong_diagonals_for_fourth_vertex"],
        keywords=["parallelogram", "fourth vertex", "midpoint formula"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=3,
        mode="28_parallelogram_find_fourth_vertex",
        difficulty="medium",
    )


# ---------------------------------------------------------------------------
# 29. Rhombus: Perpendicular Diagonals Proof
# ---------------------------------------------------------------------------
def build_29_rhombus_perpendicular_diagonals_proof(r: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A quadrilateral $ABCD$ is already proven to be a parallelogram. What single additional "
        f"calculation regarding its diagonals $AC$ and $BD$ will prove that $ABCD$ is a rhombus?"
    )
    ans_latex = r"m_{AC} \cdot m_{BD} = -1 \text{ (diagonals are perpendicular)}"
    sample = (
        rf"\text{{Calculate the gradients of the diagonals }} AC \text{{ and }} BD.\\"
        rf"\text{{If }} m_{{AC}} \times m_{{BD}} = -1 \text{{, the diagonals intersect at right angles (}} AC \perp BD \text{{),}}\\"
        rf"\text{{which proves the parallelogram is a rhombus.}}"
    )

    return make_math_question(
        prefix="analgeo_29",
        topic=TOPIC,
        subskill="29_rhombus_perpendicular_diagonals_proof",
        learning_objective_id=f"{LO_PREFIX}_rhombus_perp_diags",
        prompt=prompt,
        prompt_latex=r"m_{AC} \cdot m_{BD} = -1",
        answer_latex=ans_latex,
        answer_sympy=ans_latex,
        sample_answer=sample,
        marking_schema={
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Stated property: diagonals are perpendicular", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Coordinate condition: m_AC * m_BD = -1", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "strict",
        },
        hints={
            "1_nudge": "Think about the unique diagonal property of a rhombus compared to a general parallelogram.",
            "2_concept": "The diagonals of a rhombus bisect each other at right angles ($90^\\circ$).",
            "3_breakdown": "Show $m_{AC} \\cdot m_{BD} = -1$.",
        },
        misconception_tags=["confused_rhombus_and_rectangle_diagonal_properties"],
        keywords=["rhombus", "perpendicular diagonals", "coordinate proof"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=2,
        mode="29_rhombus_perpendicular_diagonals_proof",
        difficulty="easy",
    )


# ---------------------------------------------------------------------------
# 30. Rhombus: Equal Adjacent Sides
# ---------------------------------------------------------------------------
def build_30_rhombus_equal_adjacent_sides(r: random.Random) -> Dict[str, Any]:
    prompt = (
        f"State the side length condition required to prove that a parallelogram $ABCD$ is a rhombus."
    )
    ans_latex = r"AB = BC \text{ (adjacent sides are equal in length)}"
    sample = (
        rf"\text{{Prove that a pair of adjacent sides has equal length: }}\\"
        rf"AB = BC \quad (\text{{or }} BC = CD)"
    )

    return make_math_question(
        prefix="analgeo_30",
        topic=TOPIC,
        subskill="30_rhombus_equal_adjacent_sides",
        learning_objective_id=f"{LO_PREFIX}_rhombus_adjacent_sides",
        prompt=prompt,
        prompt_latex=r"AB = BC",
        answer_latex=ans_latex,
        answer_sympy=ans_latex,
        sample_answer=sample,
        marking_schema={
            "total_marks": 1,
            "marking_points": [
                {"id": "mp1", "desc": "Stated adjacent sides are equal (AB = BC)", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "strict",
        },
        hints={
            "1_nudge": "In a parallelogram opposite sides are already equal.",
            "2_concept": "To be a rhombus, adjacent sides must also be equal.",
            "3_breakdown": "$AB = BC$.",
        },
        misconception_tags=["stated_opposite_sides_equal"],
        keywords=["rhombus", "adjacent sides", "distance formula"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=1,
        mode="30_rhombus_equal_adjacent_sides",
        difficulty="easy",
    )


# ---------------------------------------------------------------------------
# 31. Rectangle: Equal Diagonals Proof
# ---------------------------------------------------------------------------
def build_31_rectangle_equal_diagonals_proof(r: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A quadrilateral $ABCD$ is a parallelogram. Describe how the distance formula can be used "
        f"to prove that $ABCD$ is a rectangle."
    )
    ans_latex = r"AC = BD \text{ (diagonals are equal in length)}"
    sample = (
        rf"\text{{Calculate the lengths of both diagonals }} AC \text{{ and }} BD \text{{ using the distance formula.}}\\"
        rf"\text{{If }} AC = BD \text{{, the parallelogram is a rectangle.}}"
    )

    return make_math_question(
        prefix="analgeo_31",
        topic=TOPIC,
        subskill="31_rectangle_equal_diagonals_proof",
        learning_objective_id=f"{LO_PREFIX}_rect_equal_diags",
        prompt=prompt,
        prompt_latex=r"AC = BD",
        answer_latex=ans_latex,
        answer_sympy=ans_latex,
        sample_answer=sample,
        marking_schema={
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Calculated diagonal lengths AC and BD", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Stated AC = BD proves rectangle", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "strict",
        },
        hints={
            "1_nudge": "What distinguishes the diagonals of a rectangle from those of a standard parallelogram?",
            "2_concept": "The diagonals of a rectangle are equal in length ($AC = BD$).",
            "3_breakdown": "$AC = BD$.",
        },
        misconception_tags=["confused_equal_diagonals_with_perpendicular"],
        keywords=["rectangle", "equal diagonals", "distance formula"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=2,
        mode="31_rectangle_equal_diagonals_proof",
        difficulty="easy",
    )


# ---------------------------------------------------------------------------
# 32. Rectangle: Right Angle Vertex Proof
# ---------------------------------------------------------------------------
def build_32_rectangle_right_angle_vertex_proof(r: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A parallelogram $ABCD$ has adjacent sides $AB$ and $BC$. Describe how gradients can be used "
        f"to prove that $ABCD$ is a rectangle."
    )
    ans_latex = r"m_{AB} \cdot m_{BC} = -1 \text{ (adjacent sides are perpendicular)}"
    sample = (
        rf"\text{{Calculate gradients }} m_{{AB}} \text{{ and }} m_{{BC}}.\\"
        rf"\text{{If }} m_{{AB}} \times m_{{BC}} = -1 \text{{, then }} AB \perp BC \text{{ (internal angle is }} 90^\circ\text{{),}}\\"
        rf"\text{{which proves the parallelogram is a rectangle.}}"
    )

    return make_math_question(
        prefix="analgeo_32",
        topic=TOPIC,
        subskill="32_rectangle_right_angle_vertex_proof",
        learning_objective_id=f"{LO_PREFIX}_rect_right_angle",
        prompt=prompt,
        prompt_latex=r"m_{AB} \cdot m_{BC} = -1",
        answer_latex=ans_latex,
        answer_sympy=ans_latex,
        sample_answer=sample,
        marking_schema={
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Calculated adjacent gradients m_AB and m_BC", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Showed m_AB * m_BC = -1 proves internal angle 90 deg", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "strict",
        },
        hints={
            "1_nudge": "A rectangle is a parallelogram with a right angle ($90^\\circ$).",
            "2_concept": "Prove that two adjacent sides are perpendicular: $m_{AB} \\cdot m_{BC} = -1$.",
            "3_breakdown": "$m_{AB} \\cdot m_{BC} = -1$.",
        },
        misconception_tags=["checked_opposite_sides_perpendicular"],
        keywords=["rectangle", "right angle", "perpendicular gradients"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=2,
        mode="32_rectangle_right_angle_vertex_proof",
        difficulty="easy",
    )


# ---------------------------------------------------------------------------
# 33. Square: Coordinate Proof
# ---------------------------------------------------------------------------
def build_33_square_coordinate_proof(r: random.Random) -> Dict[str, Any]:
    prompt = (
        f"List the two distinct properties beyond being a parallelogram required to prove that "
        f"quadrilateral $ABCD$ is a square."
    )
    ans_latex = r"1. \text{Adjacent sides equal (Rhombus property)}, \; 2. \text{Right-angled corner or equal diagonals (Rectangle property)}"
    sample = (
        rf"1. \text{{Prove }} ABCD \text{{ is a rhombus (e.g. }} AB = BC \text{{ or }} AC \perp BD\text{{)}}\\"
        rf"2. \text{{Prove }} ABCD \text{{ is a rectangle (e.g. }} AB \perp BC \text{{ or }} AC = BD\text{{)}}\\"
        rf"\therefore ABCD \text{{ is both a rhombus and a rectangle, hence a square.}}"
    )

    return make_math_question(
        prefix="analgeo_33",
        topic=TOPIC,
        subskill="33_square_coordinate_proof",
        learning_objective_id=f"{LO_PREFIX}_square_proof",
        prompt=prompt,
        prompt_latex=r"\text{Rhombus + Rectangle properties}",
        answer_latex=ans_latex,
        answer_sympy=ans_latex,
        sample_answer=sample,
        marking_schema={
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Rhombus property (equal adjacent sides or perp diags)", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Rectangle property (90 deg vertex or equal diags)", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "strict",
        },
        hints={
            "1_nudge": "A square is both a rhombus and a rectangle.",
            "2_concept": "You need one property of a rhombus and one property of a rectangle.",
            "3_breakdown": "Equal sides and a $90^\\circ$ angle.",
        },
        misconception_tags=["proved_only_rhombus_for_square"],
        keywords=["square", "coordinate proof", "rhombus and rectangle"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=2,
        mode="33_square_coordinate_proof",
        difficulty="easy",
    )


# ---------------------------------------------------------------------------
# 34. Trapezium: One Pair of Parallel Sides
# ---------------------------------------------------------------------------
def build_34_trapezium_one_pair_parallel_sides(r: random.Random) -> Dict[str, Any]:
    prompt = (
        f"State the gradient conditions required to prove that quadrilateral $ABCD$ is a trapezium "
        f"and NOT a parallelogram."
    )
    ans_latex = r"m_{AB} = m_{CD} \quad \text{and} \quad m_{BC} \ne m_{AD}"
    sample = (
        rf"1. \text{{One pair of opposite sides is parallel: }} m_{{AB}} = m_{{CD}}\\"
        rf"2. \text{{The other pair is NOT parallel: }} m_{{BC}} \ne m_{{AD}}\\"
        rf"\therefore ABCD \text{{ is a trapezium.}}"
    )

    return make_math_question(
        prefix="analgeo_34",
        topic=TOPIC,
        subskill="34_trapezium_one_pair_parallel_sides",
        learning_objective_id=f"{LO_PREFIX}_trapezium_proof",
        prompt=prompt,
        prompt_latex=r"m_{AB} = m_{CD} \text{ and } m_{BC} \ne m_{AD}",
        answer_latex=ans_latex,
        answer_sympy=ans_latex,
        sample_answer=sample,
        marking_schema={
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "One pair of opposite sides parallel (equal gradients)", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Other pair not parallel (unequal gradients)", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "strict",
        },
        hints={
            "1_nudge": "A trapezium has EXACTLY one pair of parallel sides.",
            "2_concept": "Check that one pair has equal gradients, but the other pair does not.",
            "3_breakdown": "$m_{AB} = m_{CD}$ and $m_{BC} \\ne m_{AD}$.",
        },
        misconception_tags=["forgot_to_check_non_parallel_pair"],
        keywords=["trapezium", "parallel sides", "gradient proof"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=2,
        mode="34_trapezium_one_pair_parallel_sides",
        difficulty="easy",
    )


# ---------------------------------------------------------------------------
# 35. Kite: Coordinate Properties
# ---------------------------------------------------------------------------
def build_35_kite_coordinate_properties(r: random.Random) -> Dict[str, Any]:
    prompt = (
        f"State two coordinate geometry properties concerning the diagonals of a kite $ABCD$."
    )
    ans_latex = r"1. \text{Diagonals are perpendicular } (m_{AC} \cdot m_{BD} = -1), \; 2. \text{One diagonal bisects the other}"
    sample = (
        rf"1. \text{{The diagonals are perpendicular: }} AC \perp BD \implies m_{{AC}} \times m_{{BD}} = -1\\"
        rf"2. \text{{The main diagonal bisects the other diagonal (midpoint of one diagonal lies on the other)}}"
    )

    return make_math_question(
        prefix="analgeo_35",
        topic=TOPIC,
        subskill="35_kite_coordinate_properties",
        learning_objective_id=f"{LO_PREFIX}_kite_properties",
        prompt=prompt,
        prompt_latex=r"AC \perp BD",
        answer_latex=ans_latex,
        answer_sympy=ans_latex,
        sample_answer=sample,
        marking_schema={
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Diagonals perpendicular (m1 * m2 = -1)", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "One diagonal bisects the other", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "strict",
        },
        hints={
            "1_nudge": "Recall how the diagonals of a kite intersect.",
            "2_concept": "They intersect at $90^\\circ$, and the line of symmetry bisects the other diagonal.",
            "3_breakdown": "Perpendicular diagonals and one diagonal bisected.",
        },
        misconception_tags=["stated_both_diagonals_bisect"],
        keywords=["kite", "diagonals perpendicular", "bisection"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=2,
        mode="35_kite_coordinate_properties",
        difficulty="easy",
    )


# ---------------------------------------------------------------------------
# 36. Area of Triangle: Coordinate Box Method
# ---------------------------------------------------------------------------
def build_36_area_of_triangle_box_method(r: random.Random) -> Dict[str, Any]:
    base = r.choice([4, 6, 8, 10])
    height = r.choice([3, 4, 5, 6, 7])
    xC = r.choice([1, 2, 3])
    area = (base * height) // 2

    prompt = (
        f"Calculate the area of $\\triangle ABC$ with vertices $A(0; 0)$, $B({base}; 0)$, and $C({xC}; {height})$."
    )
    ans_latex = rf"{area} \text{{ square units}}"
    sample = (
        rf"\text{{Base }} AB = {base} - 0 = {base}\text{{ units}}\\"
        rf"\text{{Perpendicular height }} h = y_C - 0 = {height}\text{{ units}}\\"
        rf"\text{{Area}} = \frac{{1}}{{2}} \times \text{{base}} \times \text{{height}} = \frac{{1}}{{2}} \times {base} \times {height} = {area}\text{{ square units}}"
    )

    return make_math_question(
        prefix="analgeo_36",
        topic=TOPIC,
        subskill="36_area_of_triangle_box_method",
        learning_objective_id=f"{LO_PREFIX}_triangle_area",
        prompt=prompt,
        prompt_latex=rf"A(0; 0), \; B({base}; 0), \; C({xC}; {height})",
        answer_latex=ans_latex,
        answer_sympy=str(area),
        sample_answer=sample,
        marking_schema={
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": f"Identified base = {base} and height = {height}", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Calculated area = {area} sq units", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        hints={
            "1_nudge": f"Side $AB$ lies on the $x$-axis, so its length is simply ${base} - 0 = {base}$.",
            "2_concept": f"The height is the vertical distance from $C$ to the $x$-axis ($y_C = {height}$).",
            "3_breakdown": f"Area is $\\frac{{1}}{{2}} \\times {base} \\times {height} = {area}$ square units.",
        },
        misconception_tags=["area_formula_arithmetic_error"],
        keywords=["area of triangle", "base and height", "coordinate area"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=2,
        mode="36_area_of_triangle_box_method",
        difficulty="easy",
    )


# ---------------------------------------------------------------------------
# 37. Area of Right-Angled Triangle
# ---------------------------------------------------------------------------
def build_37_area_of_right_angled_triangle(r: random.Random) -> Dict[str, Any]:
    xB = r.choice([1, 2, 3])
    yB = r.choice([1, 2, 3])
    leg_v = r.choice([4, 6, 8])
    leg_h = r.choice([3, 5, 7, 9])
    xA, yA = xB, yB + leg_v
    xC, yC = xB + leg_h, yB
    area = (leg_v * leg_h) // 2

    prompt = (
        f"A right-angled triangle $ABC$ has vertices $A({xA}; {yA})$, $B({xB}; {yB})$, and $C({xC}; {yC})$, "
        f"with the right angle at $B$.\n\n"
        f"Calculate the area of $\\triangle ABC$."
    )
    ans_latex = rf"{area} \text{{ square units}}"
    sample = (
        rf"AB = |{yA} - {yB}| = {leg_v}\text{{ units}}\\"
        rf"BC = |{xC} - {xB}| = {leg_h}\text{{ units}}\\"
        rf"\text{{Area}} = \frac{{1}}{{2}} \times AB \times BC = \frac{{1}}{{2}} \times {leg_v} \times {leg_h} = {area}\text{{ square units}}"
    )

    return make_math_question(
        prefix="analgeo_37",
        topic=TOPIC,
        subskill="37_area_of_right_angled_triangle",
        learning_objective_id=f"{LO_PREFIX}_right_triangle_area",
        prompt=prompt,
        prompt_latex=rf"A({xA}; {yA}), \; B({xB}; {yB}), \; C({xC}; {yC})",
        answer_latex=ans_latex,
        answer_sympy=str(area),
        sample_answer=sample,
        marking_schema={
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": f"Calculated perpendicular side lengths {leg_v} and {leg_h}", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Calculated area = {area} sq units", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        hints={
            "1_nudge": "In a right triangle, the two legs perpendicular to each other serve as base and height.",
            "2_concept": "$\\text{Area} = \\frac{1}{2} \\times AB \\times BC$.",
            "3_breakdown": f"Area is ${area}$ square units.",
        },
        misconception_tags=["hypotenuse_used_as_base_error"],
        keywords=["right-angled triangle", "area", "perpendicular legs"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=2,
        mode="37_area_of_right_angled_triangle",
        difficulty="easy",
    )


# ---------------------------------------------------------------------------
# 38. Area of Parallelogram Base and Height
# ---------------------------------------------------------------------------
def build_38_area_of_parallelogram_base_height(r: random.Random) -> Dict[str, Any]:
    # Parallelogram with base on x-axis: A(0, 0), B(5, 0), C(7, 4), D(2, 4)
    # Base = 5, Height = 4 => Area = 20
    b = r.choice([4, 5, 6, 8])
    h = r.choice([3, 4, 5])
    area = b * h

    prompt = (
        f"A parallelogram $ABCD$ has a horizontal base $AB$ of length {b} units lying on the $x$-axis. "
        f"The opposite side $CD$ lies on the line $y = {h}$.\n\n"
        f"Calculate the area of parallelogram $ABCD$."
    )
    ans_latex = rf"{area} \text{{ square units}}"
    sample = (
        rf"\text{{Area of parallelogram}} = \text{{base}} \times \text{{height}}\\"
        rf"= {b} \times {h} = {area}\text{{ square units}}"
    )

    return make_math_question(
        prefix="analgeo_38",
        topic=TOPIC,
        subskill="38_area_of_parallelogram_base_height",
        learning_objective_id=f"{LO_PREFIX}_parallelogram_area",
        prompt=prompt,
        prompt_latex=rf"\text{{base}} = {b}, \; \text{{height}} = {h}",
        answer_latex=ans_latex,
        answer_sympy=str(area),
        sample_answer=sample,
        marking_schema={
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Setup formula: base * height", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Correct area: {area} sq units", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        hints={
            "1_nudge": "The area of a parallelogram is $\\text{base} \\times \\text{perpendicular height}$.",
            "2_concept": "Multiply base length by the vertical distance between the parallel lines.",
            "3_breakdown": f"Area is ${area}$ square units.",
        },
        misconception_tags=["divided_by_two_for_parallelogram"],
        keywords=["parallelogram", "area", "base and height"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=2,
        mode="38_area_of_parallelogram_base_height",
        difficulty="easy",
    )


# ---------------------------------------------------------------------------
# 39. Point of Intersection of Two Lines
# ---------------------------------------------------------------------------
def build_39_point_of_intersection_two_lines(r: random.Random) -> Dict[str, Any]:
    x_int = r.choice([1, 2, 3, 4, 5])
    y_int = r.choice([2, 3, 4, 5, 6, 7])
    m1 = r.choice([2, 3, 4])
    c1 = y_int - m1 * x_int
    c2 = y_int + x_int
    c1_str = f"+ {c1}" if c1 >= 0 else f"- {abs(c1)}"

    prompt = (
        f"Calculate the coordinates of the point of intersection between the two straight lines:\n\n"
        f"$$L_1: y = {m1}x {c1_str} \\quad \\text{{and}} \\quad L_2: y = -x + {c2}$$"
    )
    ans_latex = rf"({x_int}; {y_int})"
    sample = (
        rf"\text{{Equate the two equations:}}\\"
        rf"{m1}x {c1_str} = -x + {c2}\\"
        rf"{m1 + 1}x = {c2 - c1} \implies x = {x_int}\\"
        rf"y = -{x_int} + {c2} = {y_int}\\"
        rf"\therefore \text{{Point of intersection is }} ({x_int}; {y_int})"
    )

    return make_math_question(
        prefix="analgeo_39",
        topic=TOPIC,
        subskill="39_point_of_intersection_two_lines",
        learning_objective_id=f"{LO_PREFIX}_line_intersection",
        prompt=prompt,
        prompt_latex=rf"y = {m1}x {c1_str}, \; y = -x + {c2}",
        answer_latex=ans_latex,
        answer_sympy=f"({x_int}, {y_int})",
        sample_answer=sample,
        marking_schema={
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": f"Equated equations to solve for x = {x_int}", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Substituted x to find y = {y_int}", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Stated intersection point ({x_int}; {y_int})", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        hints={
            "1_nudge": "Equate the expressions for $y$ and solve for $x$.",
            "2_concept": "Substitute the found $x$-value back into either equation to get $y$.",
            "3_breakdown": f"Point is $({x_int}; {y_int})$.",
        },
        misconception_tags=["algebra_error_simultaneous_equations"],
        keywords=["intersection of lines", "simultaneous equations"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=3,
        mode="39_point_of_intersection_two_lines",
        difficulty="medium",
    )


# ---------------------------------------------------------------------------
# 40. x- and y-intercepts of Line
# ---------------------------------------------------------------------------
def build_40_x_and_y_intercepts_of_line(r: random.Random) -> Dict[str, Any]:
    a_int, b_int = r.choice([(3, 2), (4, 3), (5, 2), (6, 5), (4, 5), (3, 5), (7, 2)])
    A_coeff = b_int
    B_coeff = a_int
    C_val = a_int * b_int

    prompt = (
        f"Calculate the coordinates of the $x$-intercept and the $y$-intercept of the line "
        f"${A_coeff}x + {B_coeff}y = {C_val}$."
    )
    ans_latex = rf"\text{{$x$-intercept: }} ({a_int}; 0), \; \text{{$y$-intercept: }} (0; {b_int})"
    sample = (
        rf"\text{{For }} x\text{{-intercept, set }} y = 0:\\"
        rf"{A_coeff}x + {B_coeff}(0) = {C_val} \implies {A_coeff}x = {C_val} \implies x = {a_int} \implies ({a_int}; 0)\\"
        rf"\text{{For }} y\text{{-intercept, set }} x = 0:\\"
        rf"{A_coeff}(0) + {B_coeff}y = {C_val} \implies {B_coeff}y = {C_val} \implies y = {b_int} \implies (0; {b_int})"
    )

    return make_math_question(
        prefix="analgeo_40",
        topic=TOPIC,
        subskill="40_x_and_y_intercepts_of_line",
        learning_objective_id=f"{LO_PREFIX}_line_intercepts",
        prompt=prompt,
        prompt_latex=rf"{A_coeff}x + {B_coeff}y = {C_val}",
        answer_latex=ans_latex,
        answer_sympy=f"({a_int}, 0), (0, {b_int})",
        sample_answer=sample,
        marking_schema={
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": f"Calculated x-intercept ({a_int}; 0)", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Calculated y-intercept (0; {b_int})", "marks": 1, "editable": True},
                {"id": "mp3", "desc": "Stated both intercept coordinates", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        hints={
            "1_nudge": "Set $y = 0$ to find the $x$-intercept; set $x = 0$ to find the $y$-intercept.",
            "2_concept": "Every intercept has one coordinate equal to zero.",
            "3_breakdown": f"$({a_int}; 0)$ and $(0; {b_int})$.",
        },
        misconception_tags=["swapped_intercept_coordinates"],
        keywords=["intercepts", "standard form", "coordinate axes"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=2,
        mode="40_x_and_y_intercepts_of_line",
        difficulty="easy",
    )


# ---------------------------------------------------------------------------
# 41. Distance from Origin to Point
# ---------------------------------------------------------------------------
def build_41_distance_from_origin_to_point(r: random.Random) -> Dict[str, Any]:
    triples = [(3, 4, 5), (6, 8, 10), (5, 12, 13), (8, 15, 17)]
    x, y, dist = r.choice(triples)
    sx = r.choice([1, -1]) * x
    sy = r.choice([1, -1]) * y

    prompt = (
        f"Calculate the distance from the origin $O(0; 0)$ to the point $P({sx}; {sy})$."
    )
    ans_latex = f"{dist} \\text{{ units}}"
    sample = (
        rf"OP = \sqrt{{x^2 + y^2}} = \sqrt{{({sx})^2 + ({sy})^2}} = \sqrt{{{x*x + y*y}}} = {dist}\text{{ units}}"
    )

    return make_math_question(
        prefix="analgeo_41",
        topic=TOPIC,
        subskill="41_distance_from_origin_to_point",
        learning_objective_id=f"{LO_PREFIX}_origin_distance",
        prompt=prompt,
        prompt_latex=rf"O(0; 0), \; P({sx}; {sy})",
        answer_latex=ans_latex,
        answer_sympy=str(dist),
        sample_answer=sample,
        marking_schema={
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Setup Pythagoras sqrt(x^2 + y^2)", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Correct distance: {dist} units", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        hints={
            "1_nudge": "The distance from the origin is $d = \\sqrt{x^2 + y^2}$.",
            "2_concept": "Squaring a negative coordinate always gives a positive result.",
            "3_breakdown": f"Distance is ${dist}$ units.",
        },
        misconception_tags=["sign_error_squaring_negative_in_pythagoras"],
        keywords=["distance from origin", "Pythagoras", "radial distance"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=2,
        mode="41_distance_from_origin_to_point",
        difficulty="easy",
    )


# ---------------------------------------------------------------------------
# 42. Collinearity with Origin
# ---------------------------------------------------------------------------
def build_42_collinearity_with_origin(r: random.Random) -> Dict[str, Any]:
    m = r.choice([2, 3, 4, 5, -2, -3])
    xA = r.choice([1, 2, 3])
    xB = xA + r.choice([2, 3, 4])
    yA = m * xA
    yB = m * xB

    prompt = (
        f"Determine whether the origin $O(0; 0)$, point $A({xA}; {yA})$, and point $B({xB}; {yB})$ are collinear."
    )
    ans_latex = rf"\text{{Collinear: }} m_{{OA}} = m_{{AB}} = {m}"
    sample = (
        rf"m_{{OA}} = \frac{{{yA} - 0}}{{{xA} - 0}} = {m}\\"
        rf"m_{{AB}} = \frac{{{yB} - ({yA})}}{{{xB} - {xA}}} = {m}\\"
        rf"\text{{Since }} m_{{OA}} = m_{{AB}} \text{{ and point }} A \text{{ is common, the origin and points }} A \text{{ and }} B \text{{ are collinear.}}"
    )

    return make_math_question(
        prefix="analgeo_42",
        topic=TOPIC,
        subskill="42_collinearity_with_origin",
        learning_objective_id=f"{LO_PREFIX}_origin_collinear",
        prompt=prompt,
        prompt_latex=rf"O(0; 0), \; A({xA}; {yA}), \; B({xB}; {yB})",
        answer_latex=ans_latex,
        answer_sympy=ans_latex,
        sample_answer=sample,
        marking_schema={
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": f"Calculated both gradients equal {m}", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Concluded points are collinear", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        hints={
            "1_nudge": "Find the gradient from $O$ to $A$ and from $A$ to $B$.",
            "2_concept": "If the gradients are equal, the points lie on the same straight line.",
            "3_breakdown": f"$m_{{OA}} = m_{{AB}} = {m} \\implies$ collinear.",
        },
        misconception_tags=["gradient_comparison_error"],
        keywords=["collinear", "origin", "gradient"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=2,
        mode="42_collinearity_with_origin",
        difficulty="easy",
    )


# ---------------------------------------------------------------------------
# 43. Equidistant Point on Axis
# ---------------------------------------------------------------------------
def build_43_equidistant_point_on_axis(r: random.Random) -> Dict[str, Any]:
    k = r.choice([1, 2, 3, 4])
    xA = -k
    xB = k + 2
    yA = r.choice([1, 2, 3, 4])
    yB = yA + 2
    y_ans = k + yA + 2
    c_lhs = xA * xA + yA * yA
    c_rhs = xB * xB + yB * yB

    prompt = (
        f"A point $P(0; y)$ lies on the $y$-axis and is equidistant from $A({xA}; {yA})$ and $B({xB}; {yB})$.\n\n"
        f"Calculate the coordinates of point $P$."
    )
    ans_latex = rf"P(0; {y_ans})"
    sample = (
        rf"PA^2 = PB^2\\"
        rf"(0 - ({xA}))^2 + (y - {yA})^2 = (0 - {xB})^2 + (y - {yB})^2\\"
        rf"{xA*xA} + y^2 - {2*yA}y + {yA*yA} = {xB*xB} + y^2 - {2*yB}y + {yB*yB}\\"
        rf"-{2*yA}y + {c_lhs} = -{2*yB}y + {c_rhs}\\"
        rf"4y = {c_rhs - c_lhs} \implies y = {y_ans}\\"
        rf"\therefore P(0; {y_ans})"
    )

    return make_math_question(
        prefix="analgeo_43",
        topic=TOPIC,
        subskill="43_equidistant_point_on_axis",
        learning_objective_id=f"{LO_PREFIX}_equidistant_axis",
        prompt=prompt,
        prompt_latex=rf"P(0; y), \; A({xA}; {yA}), \; B({xB}; {yB})",
        answer_latex=ans_latex,
        answer_sympy=f"(0, {y_ans})",
        sample_answer=sample,
        marking_schema={
            "total_marks": 4,
            "marking_points": [
                {"id": "mp1", "desc": "Setup equation PA^2 = PB^2", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Expanded binomials correctly", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Solved for y = {y_ans}", "marks": 1, "editable": True},
                {"id": "mp4", "desc": f"Final coordinates P(0; {y_ans})", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        hints={
            "1_nudge": "Set $PA^2 = PB^2$ using the distance formula.",
            "2_concept": "The $y^2$ terms will cancel on both sides, leaving a linear equation in $y$.",
            "3_breakdown": f"$P(0; {y_ans})$.",
        },
        misconception_tags=["binomial_expansion_error_in_distance"],
        keywords=["equidistant", "y-axis", "distance equation"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=4,
        mode="43_equidistant_point_on_axis",
        difficulty="hard",
    )


# ---------------------------------------------------------------------------
# 44. Midpoint Theorem Coordinate Proof (with inline_svg)
# ---------------------------------------------------------------------------
def build_44_midpoint_theorem_coordinate_proof(r: random.Random) -> Dict[str, Any]:
    w = r.choice([3, 4, 5])
    h = r.choice([2, 3, 4])
    sx = r.choice([-2, -1, 0, 1])
    sy = r.choice([-2, -1, 0, 1])
    B = (sx, sy, "B")
    A = (sx, sy + 2 * h, "A")
    C = (sx + 2 * w, sy, "C")
    D = (sx, sy + h, "D")
    E = (sx + w, sy + h, "E")

    d_spec = _cartesian_geometry_svg(
        points=[(float(A[0]), float(A[1]), "A"), (float(B[0]), float(B[1]), "B"), (float(C[0]), float(C[1]), "C"), (float(D[0]), float(D[1]), "D"), (float(E[0]), float(E[1]), "E")],
        segments=[(0, 1), (1, 2), (2, 0), (3, 4)],
    )

    prompt = (
        f"In the accompanying diagram, $\\triangle ABC$ has vertices $A({A[0]}; {A[1]})$, $B({B[0]}; {B[1]})$, and $C({C[0]}; {C[1]})$. "
        f"Point $D$ is the midpoint of $AB$ and point $E$ is the midpoint of $AC$.\n\n"
        f"1. Show that $DE \\parallel BC$.\n"
        f"2. Show that $DE = \\frac{1}{2}BC$."
    )
    ans_latex = rf"m_{{DE}} = m_{{BC}} = 0 \implies DE \parallel BC, \text{{ and }} DE = {w} = \frac{{1}}{{2}}({2*w}) = \frac{{1}}{{2}}BC"
    sample = (
        rf"D = ({D[0]}; {D[1]}), \; E = ({E[0]}; {E[1]})\\"
        rf"1. \text{{Gradients: }} m_{{DE}} = \frac{{{E[1]} - {D[1]}}}{{{E[0]} - {D[0]}}} = 0 \text{{ and }} m_{{BC}} = \frac{{{C[1]} - {B[1]}}}{{{C[0]} - {B[0]}}} = 0 \implies DE \parallel BC\\"
        rf"2. \text{{Lengths: }} DE = {E[0]} - ({D[0]}) = {w}, \; BC = {C[0]} - ({B[0]}) = {2*w} \implies DE = \frac{{1}}{{2}}BC"
    )

    return make_math_question(
        prefix="analgeo_44",
        topic=TOPIC,
        subskill="44_midpoint_theorem_coordinate_proof",
        learning_objective_id=f"{LO_PREFIX}_midpoint_theorem_proof",
        prompt=prompt,
        prompt_latex=rf"A({A[0]}; {A[1]}), \; B({B[0]}; {B[1]}), \; C({C[0]}; {C[1]})",
        answer_latex=ans_latex,
        answer_sympy=ans_latex,
        sample_answer=sample,
        marking_schema={
            "total_marks": 4,
            "marking_points": [
                {"id": "mp1", "desc": f"Calculated midpoints D({D[0]}; {D[1]}) and E({E[0]}; {E[1]})", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Showed m_DE = m_BC = 0 proves parallel", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Calculated lengths DE = {w} and BC = {2*w}", "marks": 1, "editable": True},
                {"id": "mp4", "desc": "Concluded DE = 1/2 BC", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        hints={
            "1_nudge": "Find coordinates of $D$ and $E$ using the midpoint formula.",
            "2_concept": "Prove parallel by equal gradients, and half length by comparing distances.",
            "3_breakdown": f"$m_{{DE}} = m_{{BC}} = 0$ and $DE = {w} = \\frac{{1}}{{2}}({2*w})$.",
        },
        misconception_tags=["midpoint_theorem_proof_omission"],
        keywords=["midpoint theorem", "coordinate geometry", "proof"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=4,
        mode="44_midpoint_theorem_coordinate_proof",
        difficulty="hard",
        diagram_spec=d_spec,
    )


# ---------------------------------------------------------------------------
# 45. Centroid of a Triangle
# ---------------------------------------------------------------------------
def build_45_centroid_of_triangle(r: random.Random) -> Dict[str, Any]:
    gx = r.choice([2, 3, 4, 5, -2])
    gy = r.choice([2, 3, 4, 5, -1])
    dx = r.choice([2, 3, 4])
    dy = r.choice([3, 4, 5])
    xA, xB, xC = gx - dx, gx, gx + dx
    yA, yB, yC = gy - dy + 1, gy + dy, gy - 1

    prompt = (
        f"Calculate the coordinates of the centroid $G$ of $\\triangle ABC$ with vertices "
        f"$A({xA}; {yA})$, $B({xB}; {yB})$, and $C({xC}; {yC})$."
    )
    ans_latex = rf"G({gx}; {gy})"
    sample = (
        rf"G = \left(\frac{{x_1 + x_2 + x_3}}{{3}}; \frac{{y_1 + y_2 + y_3}}{{3}}\right)\\"
        rf"G = \left(\frac{{{xA} + {xB} + {xC}}}{{3}}; \frac{{{yA} + {yB} + ({yC})}}{{3}}\right) = \left(\frac{{{3*gx}}}{{3}}; \frac{{{3*gy}}}{{3}}\right) = G({gx}; {gy})"
    )

    return make_math_question(
        prefix="analgeo_45",
        topic=TOPIC,
        subskill="45_centroid_of_triangle",
        learning_objective_id=f"{LO_PREFIX}_centroid",
        prompt=prompt,
        prompt_latex=rf"A({xA}; {yA}), \; B({xB}; {yB}), \; C({xC}; {yC})",
        answer_latex=ans_latex,
        answer_sympy=f"({gx}, {gy})",
        sample_answer=sample,
        marking_schema={
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Setup centroid formula averaging coordinates by 3", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Correct centroid coordinates G({gx}; {gy})", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "strict",
        },
        hints={
            "1_nudge": "The centroid is the average of all three vertices: $G\\left(\\frac{x_1+x_2+x_3}{3}; \\frac{y_1+y_2+y_3}{3}\\right)$.",
            "2_concept": "Add the three $x$-coordinates and divide by 3; repeat for $y$.",
            "3_breakdown": f"$G({gx}; {gy})$.",
        },
        misconception_tags=["divided_by_two_instead_of_three_for_centroid"],
        keywords=["centroid", "medians intersection", "average coordinates"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=2,
        mode="45_centroid_of_triangle",
        difficulty="easy",
    )


# ---------------------------------------------------------------------------
# 46. Angle of Inclination: Horizontal Line
# ---------------------------------------------------------------------------
def build_46_angle_of_inclination_horizontal_line(r: random.Random) -> Dict[str, Any]:
    prompt = (
        f"State the angle of inclination $\\theta$ of a horizontal straight line parallel to the $x$-axis."
    )
    ans_latex = r"\theta = 0^\circ"
    sample = (
        rf"\text{{A horizontal line has gradient }} m = 0.\\"
        rf"\tan\theta = 0 \implies \theta = 0^\circ"
    )

    return make_math_question(
        prefix="analgeo_46",
        topic=TOPIC,
        subskill="46_angle_of_inclination_horizontal_line",
        learning_objective_id=f"{LO_PREFIX}_horiz_inclination",
        prompt=prompt,
        prompt_latex=r"\tan\theta = 0",
        answer_latex=ans_latex,
        answer_sympy="0",
        sample_answer=sample,
        marking_schema={
            "total_marks": 1,
            "marking_points": [
                {"id": "mp1", "desc": "Correct angle 0 deg", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "strict",
        },
        hints={
            "1_nudge": "The inclination angle of a line is measured from the positive $x$-axis.",
            "2_concept": "A line parallel to the $x$-axis does not incline from it: $\\theta = 0^\\circ$.",
            "3_breakdown": "$\\theta = 0^\\circ$.",
        },
        misconception_tags=["confused_0_and_180_for_horizontal_inclination"],
        keywords=["horizontal line", "angle of inclination", "zero gradient"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=1,
        mode="46_angle_of_inclination_horizontal_line",
        difficulty="easy",
    )


# ---------------------------------------------------------------------------
# 47. Equation of Line: Standard Form Ax + By + C = 0
# ---------------------------------------------------------------------------
def build_47_equation_of_line_standard_form_Ax_By_C(r: random.Random) -> Dict[str, Any]:
    p_num, q_den = r.choice([(2, 3), (3, 4), (4, 5), (2, 5), (3, 5), (5, 6)])
    c_int = r.choice([2, 3, 4, 5, 6])
    C_const = q_den * c_int

    prompt = (
        f"Rewrite the equation $y = \\frac{{{p_num}}}{{{q_den}}}x - {c_int}$ in standard form $Ax + By + C = 0$, "
        f"where $A$, $B$, and $C$ are integers and $A > 0$."
    )
    ans_latex = rf"{p_num}x - {q_den}y - {C_const} = 0"
    sample = (
        rf"y = \frac{{{p_num}}}{{{q_den}}}x - {c_int}\\"
        rf"\text{{Multiply through by }} {q_den}: {q_den}y = {p_num}x - {C_const}\\"
        rf"\text{{Rearrange to standard form: }} {p_num}x - {q_den}y - {C_const} = 0"
    )

    return make_math_question(
        prefix="analgeo_47",
        topic=TOPIC,
        subskill="47_equation_of_line_standard_form_Ax_By_C",
        learning_objective_id=f"{LO_PREFIX}_standard_form",
        prompt=prompt,
        prompt_latex=rf"y = \frac{{{p_num}}}{{{q_den}}}x - {c_int}",
        answer_latex=ans_latex,
        answer_sympy=ans_latex,
        sample_answer=sample,
        marking_schema={
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": f"Cleared fractions by multiplying by {q_den}", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Standard form: {p_num}x - {q_den}y - {C_const} = 0", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        hints={
            "1_nudge": f"Multiply every term by {q_den} to eliminate the fraction.",
            "2_concept": "Rearrange so that all terms are on one side with the $x$-coefficient positive.",
            "3_breakdown": f"${p_num}x - {q_den}y - {C_const} = 0$.",
        },
        misconception_tags=["forgot_to_multiply_constant_by_denominator"],
        keywords=["standard form", "linear equation", "clearing fractions"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=2,
        mode="47_equation_of_line_standard_form_Ax_By_C",
        difficulty="easy",
    )


# ---------------------------------------------------------------------------
# 48. Reflection of Point Across Line y = x
# ---------------------------------------------------------------------------
def build_48_reflection_of_point_across_line_y_equals_x(r: random.Random) -> Dict[str, Any]:
    x = r.choice([-5, -3, 2, 4])
    y = r.choice([-4, 1, 3, 6])

    prompt = (
        f"Determine the coordinates of point $P'$ when $P({x}; {y})$ is reflected "
        f"across the line $y = x$."
    )
    ans_latex = rf"P'({y}; {x})"
    sample = (
        rf"\text{{Reflection across the line }} y = x \text{{ swaps the coordinates: }} (x; y) \to (y; x)\\"
        rf"\therefore P'({y}; {x})"
    )

    return make_math_question(
        prefix="analgeo_48",
        topic=TOPIC,
        subskill="48_reflection_of_point_across_line_y_equals_x",
        learning_objective_id=f"{LO_PREFIX}_refl_line_y_x",
        prompt=prompt,
        prompt_latex=rf"P({x}; {y}), \; y = x",
        answer_latex=ans_latex,
        answer_sympy=f"({y}, {x})",
        sample_answer=sample,
        marking_schema={
            "total_marks": 1,
            "marking_points": [
                {"id": "mp1", "desc": f"Swapped coordinates: ({y}; {x})", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "strict",
        },
        hints={
            "1_nudge": "Reflection in $y = x$ interchanges the $x$ and $y$ values.",
            "2_concept": "$(x; y) \\to (y; x)$.",
            "3_breakdown": f"Point is $P'({y}; {x})$.",
        },
        misconception_tags=["negated_coordinates_instead_of_swapping"],
        keywords=["reflection", "line y = x", "transformations"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=1,
        mode="48_reflection_of_point_across_line_y_equals_x",
        difficulty="easy",
    )


# ---------------------------------------------------------------------------
# 49. Reflection of Point Across Axes
# ---------------------------------------------------------------------------
def build_49_reflection_of_point_across_axes(r: random.Random) -> Dict[str, Any]:
    axis = r.choice(["x-axis", "y-axis"])
    x = r.choice([-4, -2, 3, 5])
    y = r.choice([-3, 1, 4, 7])

    if axis == "x-axis":
        ans_pt = f"({x}; {-y})"
        rule = r"(x; y) \to (x; -y)"
    else:
        ans_pt = f"({-x}; {y})"
        rule = r"(x; y) \to (-x; y)"

    prompt = (
        f"Determine the coordinates of point $P({x}; {y})$ after reflection across the {axis}."
    )
    ans_latex = rf"P'{ans_pt}"
    sample = (
        rf"\text{{Reflection across the {axis}: }} {rule}\\"
        rf"\therefore P'{ans_pt}"
    )

    return make_math_question(
        prefix="analgeo_49",
        topic=TOPIC,
        subskill="49_reflection_of_point_across_axes",
        learning_objective_id=f"{LO_PREFIX}_refl_axes",
        prompt=prompt,
        prompt_latex=rf"P({x}; {y}), \; \text{{{axis}}}",
        answer_latex=ans_latex,
        answer_sympy=ans_pt,
        sample_answer=sample,
        marking_schema={
            "total_marks": 1,
            "marking_points": [
                {"id": "mp1", "desc": f"Correct reflected point: {ans_pt}", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "strict",
        },
        hints={
            "1_nudge": f"Reflecting across {axis} negates the opposite coordinate.",
            "2_concept": "Reflection in $x$-axis: $(x; -y)$. Reflection in $y$-axis: $(-x; y)$.",
            "3_breakdown": f"Point is {ans_pt}.",
        },
        misconception_tags=["negated_wrong_coordinate"],
        keywords=["reflection", "axes", "transformations"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=1,
        mode="49_reflection_of_point_across_axes",
        difficulty="easy",
    )


# ---------------------------------------------------------------------------
# 50. Comprehensive Geometric Quadrilateral Analysis (with inline_svg)
# ---------------------------------------------------------------------------
def build_50_comprehensive_geometric_quadrilateral_analysis(r: random.Random) -> Dict[str, Any]:
    sx = r.choice([-2, -1, 0, 1])
    sy = r.choice([-2, -1, 0, 1])
    A = (-1 + sx, 1 + sy, "A")
    B = (3 + sx, -1 + sy, "B")
    C = (5 + sx, 3 + sy, "C")
    D = (1 + sx, 5 + sy, "D")

    d_spec = _cartesian_geometry_svg(
        points=[(float(A[0]), float(A[1]), "A"), (float(B[0]), float(B[1]), "B"), (float(C[0]), float(C[1]), "C"), (float(D[0]), float(D[1]), "D")],
        segments=[(0, 1), (1, 2), (2, 3), (3, 0), (0, 2), (1, 3)],
    )

    prompt = (
        f"In the accompanying diagram, quadrilateral $ABCD$ has vertices $A({A[0]}; {A[1]})$, $B({B[0]}; {B[1]})$, "
        f"$C({C[0]}; {C[1]})$, and $D({D[0]}; {D[1]})$.\n\n"
        f"1. Calculate the gradients $m_{{AB}}$ and $m_{{BC}}$.\n"
        f"2. Hence, prove that $AB \\perp BC$ and classify $ABCD$ specifically."
    )
    ans_latex = r"m_{AB} = -\frac{1}{2}, \; m_{BC} = 2 \implies AB \perp BC, \; ABCD \text{ is a square}"
    sample = (
        rf"1. \text{{Gradients: }}\\"
        rf"m_{{AB}} = \frac{{{B[1]} - ({A[1]})}}{{{B[0]} - ({A[0]})}} = \frac{{-2}}{{4}} = -\frac{{1}}{{2}}\\"
        rf"m_{{BC}} = \frac{{{C[1]} - ({B[1]})}}{{{C[0]} - ({B[0]})}} = \frac{{4}}{{2}} = 2\\"
        rf"2. m_{{AB}} \times m_{{BC}} = -\frac{{1}}{{2}} \times 2 = -1 \implies AB \perp BC\\"
        rf"\text{{Also }} AB = \sqrt{{20}} \text{{ and }} BC = \sqrt{{20}} \implies AB = BC\\"
        rf"\therefore ABCD \text{{ is a square (rectangle with equal adjacent sides).}}"
    )

    return make_math_question(
        prefix="analgeo_50",
        topic=TOPIC,
        subskill="50_comprehensive_geometric_quadrilateral_analysis",
        learning_objective_id=f"{LO_PREFIX}_summary_quadrilateral",
        prompt=prompt,
        prompt_latex=rf"A({A[0]}; {A[1]}), \; B({B[0]}; {B[1]}), \; C({C[0]}; {C[1]}), \; D({D[0]}; {D[1]})",
        answer_latex=ans_latex,
        answer_sympy=ans_latex,
        sample_answer=sample,
        marking_schema={
            "total_marks": 5,
            "marking_points": [
                {"id": "mp1", "desc": "Calculated m_AB = -1/2", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Calculated m_BC = 2", "marks": 1, "editable": True},
                {"id": "mp3", "desc": "Showed m_AB * m_BC = -1 implies perpendicular", "marks": 1, "editable": True},
                {"id": "mp4", "desc": "Showed side lengths AB = BC = sqrt(20)", "marks": 1, "editable": True},
                {"id": "mp5", "desc": "Classified as a square", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        hints={
            "1_nudge": "Find both gradients and test if their product is $-1$.",
            "2_concept": "Check side lengths to distinguish between a rectangle and a square.",
            "3_breakdown": "$m_{AB} = -\\frac{1}{2}$, $m_{BC} = 2$, proving $ABCD$ is a square.",
        },
        misconception_tags=["classified_square_only_as_rectangle"],
        keywords=["quadrilateral analysis", "square", "perpendicular", "gradients"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=5,
        mode="50_comprehensive_geometric_quadrilateral_analysis",
        difficulty="hard",
        diagram_spec=d_spec,
    )


# ---------------------------------------------------------------------------
# Registry Map of Archetypes 26–50
# ---------------------------------------------------------------------------
ARCHETYPES_26_50 = {
    "26_perpendicular_bisector_of_segment": build_26_perpendicular_bisector_of_segment,
    "27_parallelogram_diagonals_bisect_property": build_27_parallelogram_diagonals_bisect_property,
    "28_parallelogram_find_fourth_vertex": build_28_parallelogram_find_fourth_vertex,
    "29_rhombus_perpendicular_diagonals_proof": build_29_rhombus_perpendicular_diagonals_proof,
    "30_rhombus_equal_adjacent_sides": build_30_rhombus_equal_adjacent_sides,
    "31_rectangle_equal_diagonals_proof": build_31_rectangle_equal_diagonals_proof,
    "32_rectangle_right_angle_vertex_proof": build_32_rectangle_right_angle_vertex_proof,
    "33_square_coordinate_proof": build_33_square_coordinate_proof,
    "34_trapezium_one_pair_parallel_sides": build_34_trapezium_one_pair_parallel_sides,
    "35_kite_coordinate_properties": build_35_kite_coordinate_properties,
    "36_area_of_triangle_box_method": build_36_area_of_triangle_box_method,
    "37_area_of_right_angled_triangle": build_37_area_of_right_angled_triangle,
    "38_area_of_parallelogram_base_height": build_38_area_of_parallelogram_base_height,
    "39_point_of_intersection_two_lines": build_39_point_of_intersection_two_lines,
    "40_x_and_y_intercepts_of_line": build_40_x_and_y_intercepts_of_line,
    "41_distance_from_origin_to_point": build_41_distance_from_origin_to_point,
    "42_collinearity_with_origin": build_42_collinearity_with_origin,
    "43_equidistant_point_on_axis": build_43_equidistant_point_on_axis,
    "44_midpoint_theorem_coordinate_proof": build_44_midpoint_theorem_coordinate_proof,
    "45_centroid_of_triangle": build_45_centroid_of_triangle,
    "46_angle_of_inclination_horizontal_line": build_46_angle_of_inclination_horizontal_line,
    "47_equation_of_line_standard_form_Ax_By_C": build_47_equation_of_line_standard_form_Ax_By_C,
    "48_reflection_of_point_across_line_y_equals_x": build_48_reflection_of_point_across_line_y_equals_x,
    "49_reflection_of_point_across_axes": build_49_reflection_of_point_across_axes,
    "50_comprehensive_geometric_quadrilateral_analysis": build_50_comprehensive_geometric_quadrilateral_analysis,
}
