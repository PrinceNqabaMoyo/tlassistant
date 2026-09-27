"""Circle Geometry Generator (Grade 11/12 Mathematics Paper 2).

Curriculum: South African CAPS Mathematics, Grade 11 Term 3 & Grade 12 Revision.
Zero-LLM deterministic generation using SymPy and structured Diagram Specs.

Implements the Universal 6-Pillar Generator Architecture Contract:
1. Calendar & Exam Metadata (Term 3, CAPS Weight 30%, 15 mins)
2. Deconstructibility into Atomic Micro-Drills (elementary_* modes vs compound)
3. Standardized Misconception Taxonomy (subtended_arc_confusion, etc.)
4. Teacher-Editable Marking Schema (points, deductions, carry_forward_rule)
5. Deterministic 3-Tier Pre-Baked Hints (Nudge -> Geometric Rule -> Worked Step)
6. Modality-Appropriate Representation (KaTeX, South African comma decimals, JSXGraph Diagram Spec)
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional

from app.utils.grade10_mathematics import _diagram
from app.utils.grade10_mathematics._math_common import (
    build_generate,
    make_id,
    make_short,
    num,
    step,
    solution,
    with_metadata,
)

TOPIC = "grade11_math_circle_geometry"
LO = "math11_circle_geometry"

# Standard South African CAPS Exam Geometric Reasons
REASONS = {
    "center_twice_circ": "[∠ at centre = 2 × ∠ at circ]",
    "opp_cyclic_quad": "[opp ∠s of cyclic quad]",
    "ext_cyclic_quad": "[ext ∠ of cyclic quad]",
    "tan_chord": "[tan chord thm]",
    "tan_rad": "[tan ⟂ rad]",
    "semi_circle": "[∠ in semi circle]",
    "angles_same_seg": "[∠s in same seg]",
    "sum_angles_tri": "[sum of ∠s in △]",
}


def _rng(seed: Any = None) -> random.Random:
    if seed is None:
        return random.Random()
    return random.Random(seed)


# --------------------------------------------------------------------------- #
# 1. Angle at Center is Twice Angle at Circumference
# --------------------------------------------------------------------------- #
def _build_angle_at_center(r: random.Random, difficulty: str = "practice", mode: str = "compound") -> Dict[str, Any]:
    """Theorem: The angle subtended by an arc at the center is twice the angle
    subtended by the same arc at the circumference.
    """
    circ_angle = r.randint(28, 55)
    center_angle = circ_angle * 2

    # Mode variation: find center angle OR find circumference angle
    find_center = r.choice([True, False])

    if find_center:
        prompt_latex = (
            f"In the circle with centre $O$, chord $AB$ subtends $\\angle ACB = {circ_angle}^\\circ$ "
            f"at the circumference. Calculate the size of $\\angle AOB$ ($x$). Give a reason for your answer."
        )
        answer_val = str(center_angle)
        calc_step = f"x = 2 \\times {circ_angle}^\\circ = {center_angle}^\\circ"
        t1_hint = "Identify chord AB and trace the angles subtended at center O and circumference C."
        t2_hint = f"Theorem: The angle at the centre is twice the angle at the circumference {REASONS['center_twice_circ']}."
        t3_hint = f"Calculate: $x = 2 \\times {circ_angle}^\\circ = {center_angle}^\\circ$."
        angle_labels = [{"at": "C", "arms": ["A", "C", "B"], "label": f"{circ_angle}°"}, {"at": "O", "arms": ["A", "O", "B"], "label": "x"}]
    else:
        prompt_latex = (
            f"In the circle with centre $O$, $\\angle AOB = {center_angle}^\\circ$. "
            f"Calculate the size of inscribed angle $\\angle ACB$ ($x$). Give a reason for your answer."
        )
        answer_val = str(circ_angle)
        calc_step = f"x = \\frac{{{center_angle}^\\circ}}{{2}} = {circ_angle}^\\circ"
        t1_hint = "Notice that both ∠AOB and ∠ACB are subtended by the same arc AB."
        t2_hint = f"Theorem: The angle at the circumference is half the angle at the centre {REASONS['center_twice_circ']}."
        t3_hint = f"Calculate: $x = {center_angle}^\\circ / 2 = {circ_angle}^\\circ$."
        angle_labels = [{"at": "O", "arms": ["A", "O", "B"], "label": f"{center_angle}°"}, {"at": "C", "arms": ["A", "C", "B"], "label": "x"}]

    diagram = _diagram.circle_subtended_angle(
        center="O",
        radius=3.0,
        angles=angle_labels,
        show_radii=True,
        show_chord=False,
        caption="Circle with centre O and subtended angles ∠AOB and ∠ACB",
    )

    canon_sol = solution(
        goal="calculate missing subtended angle",
        chain_type="equation",
        var="x",
        steps=[
            step(
                from_expr=None,
                to_expr=None,
                from_latex="\\angle AOB = 2 \\angle ACB",
                to_latex=calc_step,
                op="apply theorem",
                rule=REASONS["center_twice_circ"],
                common_errors=["subtended_arc_confusion"],
            )
        ],
        final_expr=None,
        final_latex=f"x = {answer_val}^\\circ",
    )

    marking_schema = {
        "total_marks": 3,
        "marking_points": [
            {"id": "mp_thm", "desc": f"State theorem relationship: ∠AOB = 2∠ACB {REASONS['center_twice_circ']}", "marks": 1, "editable": True},
            {"id": "mp_calc", "desc": f"Substitution: {calc_step}", "marks": 1, "editable": True},
            {"id": "mp_ans", "desc": f"Final answer: x = {answer_val}°", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "omitted_geometric_reason", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    q = make_short(
        prefix="cg_sub",
        prompt_latex=prompt_latex,
        answer_expr=answer_val,
        answer_mode="value",
        marks=3,
        canonical_solution=canon_sol,
        explanation=f"By theorem {REASONS['center_twice_circ']}, {calc_step}.",
    )
    q["term"] = 3
    q["caps_weight_percent"] = 30
    q["suggested_duration_mins"] = 12
    q["marking_schema"] = marking_schema
    q["hint_sections"] = {"tier_1": t1_hint, "tier_2": t2_hint, "tier_3": t3_hint}

    return with_metadata(
        q,
        topic=TOPIC,
        subskill="angle_at_center",
        learning_objective_id=LO,
        misconception_tags=["subtended_arc_confusion"],
        diagram_spec=diagram,
    )


# --------------------------------------------------------------------------- #
# 2. Cyclic Quadrilateral - Opposite Angles
# --------------------------------------------------------------------------- #
def _build_cyclic_quad_opposite(r: random.Random, difficulty: str = "practice", mode: str = "compound") -> Dict[str, Any]:
    """Theorem: Opposite angles of a cyclic quadrilateral are supplementary."""
    angle_A = r.randint(75, 125)
    angle_C = 180 - angle_A
    angle_B = r.randint(70, 115)
    angle_D = 180 - angle_B

    prompt_latex = (
        f"Quadrilateral $ABCD$ is cyclic (all four vertices lie on the circle). "
        f"If $\\angle A = {angle_A}^\\circ$, calculate the size of opposite angle $\\angle C$ ($x$). "
        f"State the geometric reason."
    )
    answer_val = str(angle_C)

    diagram = _diagram.circle_cyclic_quad(
        center="O",
        radius=3.0,
        vertices=["A", "B", "C", "D"],
        angles=[
            {"arms": ["B", "A", "D"], "label": f"{angle_A}°", "radius": 0.6},
            {"arms": ["B", "C", "D"], "label": "x", "radius": 0.6},
        ],
        caption="Cyclic quadrilateral ABCD",
    )

    t1_hint = "Identify that all 4 vertices A, B, C, D touch the circle circumference, making ABCD a cyclic quadrilateral."
    t2_hint = f"Theorem: Opposite angles of a cyclic quadrilateral sum to 180° {REASONS['opp_cyclic_quad']}."
    t3_hint = f"Calculate: $\\angle A + \\angle C = 180^\\circ \\implies x = 180^\\circ - {angle_A}^\\circ = {angle_C}^\\circ$."

    canon_sol = solution(
        goal="solve for x using cyclic quad theorem",
        chain_type="equation",
        var="x",
        steps=[
            step(
                from_expr=None,
                to_expr=None,
                from_latex="\\angle A + \\angle C = 180^\\circ",
                to_latex=f"{angle_A}^\\circ + x = 180^\\circ",
                op="apply opposite angles theorem",
                rule=REASONS["opp_cyclic_quad"],
                common_errors=["opposite_angles_cyclic_quad_equality"],
            ),
            step(
                from_expr=None,
                to_expr=None,
                from_latex=f"x = 180^\\circ - {angle_A}^\\circ",
                to_latex=f"x = {angle_C}^\\circ",
                op="subtract angle",
                rule="subtraction property",
                common_errors=["sign_error"],
            ),
        ],
        final_expr=None,
        final_latex=f"x = {answer_val}^\\circ",
    )

    marking_schema = {
        "total_marks": 3,
        "marking_points": [
            {"id": "mp_stat", "desc": f"∠A + ∠C = 180° {REASONS['opp_cyclic_quad']}", "marks": 1, "editable": True},
            {"id": "mp_sub", "desc": f"x = 180° - {angle_A}°", "marks": 1, "editable": True},
            {"id": "mp_ans", "desc": f"Final answer: x = {answer_val}°", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "omitted_geometric_reason", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    q = make_short(
        prefix="cg_cycopp",
        prompt_latex=prompt_latex,
        answer_expr=answer_val,
        answer_mode="value",
        marks=3,
        canonical_solution=canon_sol,
        explanation=f"Opposite angles of cyclic quad sum to 180° {REASONS['opp_cyclic_quad']}: x = 180° - {angle_A}° = {angle_C}°.",
    )
    q["term"] = 3
    q["caps_weight_percent"] = 30
    q["suggested_duration_mins"] = 12
    q["marking_schema"] = marking_schema
    q["hint_sections"] = {"tier_1": t1_hint, "tier_2": t2_hint, "tier_3": t3_hint}

    return with_metadata(
        q,
        topic=TOPIC,
        subskill="cyclic_quad_opposite",
        learning_objective_id=LO,
        misconception_tags=["opposite_angles_cyclic_quad_equality"],
        diagram_spec=diagram,
    )


# --------------------------------------------------------------------------- #
# 3. Cyclic Quadrilateral - Exterior Angle
# --------------------------------------------------------------------------- #
def _build_cyclic_quad_exterior(r: random.Random, difficulty: str = "practice", mode: str = "compound") -> Dict[str, Any]:
    """Theorem: The exterior angle of a cyclic quad equals the interior opposite angle."""
    int_opp_angle = r.randint(70, 120)
    answer_val = str(int_opp_angle)

    # Point E extends line BC past C
    pts = {
        "O": [0.0, 0.0],
        "A": [-1.8, 2.4],
        "B": [-2.8, -1.0],
        "C": [1.5, -2.6],
        "D": [2.7, 1.3],
        "E": [3.65, -3.4],  # extension of BC
    }

    prompt_latex = (
        f"In cyclic quadrilateral $ABCD$, side $BC$ is produced to $E$. "
        f"If interior opposite angle $\\angle A = {int_opp_angle}^\\circ$, calculate the size of "
        f"exterior angle $\\angle DCE$ ($x$). State the reason."
    )

    diagram = _diagram.circle_cyclic_quad(
        center="O",
        radius=3.0,
        vertices=["A", "B", "C", "D"],
        points=pts,
        exterior_vertex="E",
        angles=[
            {"arms": ["B", "A", "D"], "label": f"{int_opp_angle}°", "radius": 0.6},
            {"arms": ["D", "C", "E"], "label": "x", "radius": 0.6},
        ],
        caption="Cyclic quadrilateral ABCD with side BC produced to E",
    )

    t1_hint = "Identify the exterior angle ∠DCE formed by producing side BC, and look at the interior angle opposite to C."
    t2_hint = f"Theorem: The exterior angle of a cyclic quadrilateral equals the interior opposite angle {REASONS['ext_cyclic_quad']}."
    t3_hint = f"Directly apply: $x = \\angle A = {int_opp_angle}^\\circ$."

    canon_sol = solution(
        goal="find exterior angle of cyclic quad",
        chain_type="equation",
        var="x",
        steps=[
            step(
                from_expr=None,
                to_expr=None,
                from_latex="\\angle DCE = \\angle BAD",
                to_latex=f"x = {int_opp_angle}^\\circ",
                op="apply exterior angle theorem",
                rule=REASONS["ext_cyclic_quad"],
                common_errors=["exterior_angle_cyclic_quad_inversion"],
            )
        ],
        final_expr=None,
        final_latex=f"x = {answer_val}^\\circ",
    )

    marking_schema = {
        "total_marks": 2,
        "marking_points": [
            {"id": "mp_stat", "desc": f"State theorem: ext ∠ = int opp ∠ {REASONS['ext_cyclic_quad']}", "marks": 1, "editable": True},
            {"id": "mp_ans", "desc": f"Final answer: x = {answer_val}°", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "omitted_geometric_reason", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    q = make_short(
        prefix="cg_cycext",
        prompt_latex=prompt_latex,
        answer_expr=answer_val,
        answer_mode="value",
        marks=2,
        canonical_solution=canon_sol,
        explanation=f"Exterior angle of cyclic quad equals interior opposite angle {REASONS['ext_cyclic_quad']}: x = {int_opp_angle}°.",
    )
    q["term"] = 3
    q["caps_weight_percent"] = 30
    q["suggested_duration_mins"] = 10
    q["marking_schema"] = marking_schema
    q["hint_sections"] = {"tier_1": t1_hint, "tier_2": t2_hint, "tier_3": t3_hint}

    return with_metadata(
        q,
        topic=TOPIC,
        subskill="cyclic_quad_exterior",
        learning_objective_id=LO,
        misconception_tags=["exterior_angle_cyclic_quad_inversion"],
        diagram_spec=diagram,
    )


# --------------------------------------------------------------------------- #
# 4. Tangent-Chord Theorem
# --------------------------------------------------------------------------- #
def _build_tangent_chord(r: random.Random, difficulty: str = "practice", mode: str = "compound") -> Dict[str, Any]:
    """Theorem: The angle between a tangent to a circle and a chord drawn from the point
    of contact is equal to the angle in the alternate segment.
    """
    tan_angle = r.randint(45, 78)
    answer_val = str(tan_angle)

    prompt_latex = (
        f"Line $PTQ$ is a tangent to the circle at point $T$. Chord $TA$ is drawn. "
        f"Point $B$ lies on the circle such that $\\angle TBA$ is in the alternate segment. "
        f"If $\\angle QTA = {tan_angle}^\\circ$, calculate the size of $\\angle TBA$ ($x$). "
        f"State the theorem used."
    )

    diagram = _diagram.circle_tangent_secant(
        center="O",
        radius=3.0,
        tangent_point="T",
        angles=[
            {"arms": ["Q", "T", "A"], "label": f"{tan_angle}°", "radius": 0.8},
            {"arms": ["T", "B", "A"], "label": "x", "radius": 0.6},
        ],
        caption="Tangent PTQ at T with inscribed triangle TAB",
    )

    t1_hint = "Identify the tangent PTQ touching at T, chord TA, and triangle TAB."
    t2_hint = f"Theorem: The angle between tangent and chord equals the angle in the alternate segment {REASONS['tan_chord']}."
    t3_hint = f"The angle in the alternate segment to ∠QTA is ∠TBA. Therefore $x = {tan_angle}^\\circ$."

    canon_sol = solution(
        goal="apply tangent chord theorem",
        chain_type="equation",
        var="x",
        steps=[
            step(
                from_expr=None,
                to_expr=None,
                from_latex="\\angle TBA = \\angle QTA",
                to_latex=f"x = {tan_angle}^\\circ",
                op="apply tangent-chord theorem",
                rule=REASONS["tan_chord"],
                common_errors=["tangent_chord_error"],
            )
        ],
        final_expr=None,
        final_latex=f"x = {answer_val}^\\circ",
    )

    marking_schema = {
        "total_marks": 2,
        "marking_points": [
            {"id": "mp_stat", "desc": f"State theorem: ∠TBA = ∠QTA {REASONS['tan_chord']}", "marks": 1, "editable": True},
            {"id": "mp_ans", "desc": f"Final answer: x = {answer_val}°", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "omitted_geometric_reason", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    q = make_short(
        prefix="cg_tanchord",
        prompt_latex=prompt_latex,
        answer_expr=answer_val,
        answer_mode="value",
        marks=2,
        canonical_solution=canon_sol,
        explanation=f"By the tangent-chord theorem {REASONS['tan_chord']}, x = ∠QTA = {tan_angle}°.",
    )
    q["term"] = 3
    q["caps_weight_percent"] = 30
    q["suggested_duration_mins"] = 10
    q["marking_schema"] = marking_schema
    q["hint_sections"] = {"tier_1": t1_hint, "tier_2": t2_hint, "tier_3": t3_hint}

    return with_metadata(
        q,
        topic=TOPIC,
        subskill="tangent_chord",
        learning_objective_id=LO,
        misconception_tags=["tangent_chord_error"],
        diagram_spec=diagram,
    )


# --------------------------------------------------------------------------- #
# 5. Tangent Perpendicular to Radius
# --------------------------------------------------------------------------- #
def _build_tangent_radius(r: random.Random, difficulty: str = "practice", mode: str = "compound") -> Dict[str, Any]:
    """Theorem: A tangent to a circle is perpendicular to the radius at the point of contact."""
    angle_pot = r.randint(25, 65)
    angle_opt = 90 - angle_pot
    answer_val = str(angle_opt)

    prompt_latex = (
        f"Line $PQ$ is a tangent to the circle at point $T$, and $OT$ is a radius from centre $O$. "
        f"Line $OP$ meets the tangent at $P$. If $\\angle POT = {angle_pot}^\\circ$, "
        f"calculate the size of $\\angle OPT$ ($x$). Give geometric reasons."
    )

    pts = {
        "O": [0.0, 0.0],
        "T": [0.0, -3.0],
        "P": [-4.5, -3.0],
        "Q": [2.0, -3.0],
    }

    diagram = _diagram.circle_tangent_secant(
        center="O",
        radius=3.0,
        tangent_point="T",
        points=pts,
        lines=[["P", "Q"], ["O", "T"], ["O", "P"]],
        angles=[
            {"arms": ["P", "O", "T"], "label": f"{angle_pot}°", "radius": 0.8},
            {"arms": ["O", "P", "T"], "label": "x", "radius": 0.8},
            {"arms": ["O", "T", "P"], "label": "90°", "radius": 0.4},
        ],
        show_radius_to_tangent=True,
        caption="Radius OT meeting tangent PQ at point of contact T",
    )

    t1_hint = "Recall the relationship between the radius OT and tangent PQ at the point of contact T."
    t2_hint = f"Theorem: A tangent is perpendicular to the radius at the point of contact {REASONS['tan_rad']}: $\\angle OTP = 90^\\circ$."
    t3_hint = f"In $\\triangle OPT$, sum of angles is 180°: $x = 180^\\circ - 90^\\circ - {angle_pot}^\\circ = {angle_opt}^\\circ$."

    canon_sol = solution(
        goal="solve for x in right triangle OPT",
        chain_type="equation",
        var="x",
        steps=[
            step(
                from_expr=None,
                to_expr=None,
                from_latex="\\angle OTP = 90^\\circ",
                to_latex="\\angle OTP = 90^\\circ",
                op="identify perpendicular radius",
                rule=REASONS["tan_rad"],
                common_errors=["tangent_radius_perpendicular_miss"],
            ),
            step(
                from_expr=None,
                to_expr=None,
                from_latex=f"x + {angle_pot}^\\circ + 90^\\circ = 180^\\circ",
                to_latex=f"x = {angle_opt}^\\circ",
                op="triangle angle sum",
                rule=REASONS["sum_angles_tri"],
                common_errors=["sign_error"],
            ),
        ],
        final_expr=None,
        final_latex=f"x = {answer_val}^\\circ",
    )

    marking_schema = {
        "total_marks": 3,
        "marking_points": [
            {"id": "mp_rad", "desc": f"∠OTP = 90° {REASONS['tan_rad']}", "marks": 1, "editable": True},
            {"id": "mp_sum", "desc": f"Sum of angles in △OPT = 180° {REASONS['sum_angles_tri']}", "marks": 1, "editable": True},
            {"id": "mp_ans", "desc": f"Final answer: x = {answer_val}°", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "omitted_geometric_reason", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    q = make_short(
        prefix="cg_tanrad",
        prompt_latex=prompt_latex,
        answer_expr=answer_val,
        answer_mode="value",
        marks=3,
        canonical_solution=canon_sol,
        explanation=f"Radius OT ⟂ tangent PQ {REASONS['tan_rad']} gives ∠OTP = 90°. In △OPT, x = 180° - 90° - {angle_pot}° = {angle_opt}°.",
    )
    q["term"] = 3
    q["caps_weight_percent"] = 30
    q["suggested_duration_mins"] = 12
    q["marking_schema"] = marking_schema
    q["hint_sections"] = {"tier_1": t1_hint, "tier_2": t2_hint, "tier_3": t3_hint}

    return with_metadata(
        q,
        topic=TOPIC,
        subskill="tangent_radius",
        learning_objective_id=LO,
        misconception_tags=["tangent_radius_perpendicular_miss"],
        diagram_spec=diagram,
    )


# --------------------------------------------------------------------------- #
# Dispatcher & Universal Generator Contract Interface
# --------------------------------------------------------------------------- #
SUBSKILL_BUILDERS = {
    "angle_at_center": _build_angle_at_center,
    "cyclic_quad_opposite": _build_cyclic_quad_opposite,
    "cyclic_quad_exterior": _build_cyclic_quad_exterior,
    "tangent_chord": _build_tangent_chord,
    "tangent_radius": _build_tangent_radius,
}


def generate(
    subskill: str = "angle_at_center",
    seed: Optional[int] = None,
    mode: str = "scaffold",
    difficulty: str = "practice",
    **kwargs: Any,
) -> List[Dict[str, Any]]:
    """Universal generator entrypoint implementing the 6-Pillar Contract."""
    r = _rng(seed)

    # Deconstructibility support: elementary_* maps directly to individual subskill
    if subskill.startswith("elementary_"):
        actual_subskill = subskill.replace("elementary_", "")
    else:
        actual_subskill = subskill

    builder = SUBSKILL_BUILDERS.get(actual_subskill, _build_angle_at_center)
    question = builder(r, difficulty=difficulty, mode=mode)
    if seed is not None:
        question["id"] = f"cg_{actual_subskill}_{seed}"
    return [question]

