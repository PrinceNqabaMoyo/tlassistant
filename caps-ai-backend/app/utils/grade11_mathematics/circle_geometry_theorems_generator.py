"""Grade 11 Mathematics — Euclidean Circle Geometry Theorems (Deterministic 6-Pillar Generator).
Covers official CAPS Examination standards (Paper 2 — 35 to 40 marks):
- Theorem: Angle at centre = 2 * angle at circumference (angle at centre = 2 * angle at circ)
- Theorem: Angles in the same segment are equal (angles in same seg)
- Theorem: Opposite angles of cyclic quad are supplementary (opp angles of cyclic quad)
- Theorem: Exterior angle of cyclic quad = interior opposite angle (ext angle of cyclic quad)
- Theorem: Tangent-chord theorem (tan chord theorem)
Supports full compound exam questions and atomic elementary sub-drills for adaptive deconstruction.
"""
from __future__ import annotations

import math
from typing import Any, Dict, List, Optional

from app.utils.grade11_mathematics._math_common import (
    make_id,
    make_math_question,
    nonzero,
    rng,
    solution_graph,
    step,
)

TOPIC = "euclidean_circle_geometry"
LO = "math11_circle_geometry"


# --------------------------------------------------------------------------- #
# Sub-Drill: Angle at Centre = 2 * Angle at Circumference
# --------------------------------------------------------------------------- #
def _build_angle_at_centre(r, difficulty: str) -> Dict[str, Any]:
    angle_circ = r.randint(28, 55)
    angle_centre = 2 * angle_circ

    prompt = (
        f"In the circle with centre $O$, points $A$, $B$, and $C$ lie on the circumference. "
        f"If the inscribed angle $\\hat{{C}} = {angle_circ}^\\circ$, calculate the size of the reflex or obtuse angle "
        f"$\\hat{{O}}$ subtended by the same arc $AB$. State the complete geometric reason."
    )

    reason = r"\angle \text{ at centre } = 2\times \angle \text{ at circ}"
    sample = rf"\hat{{O}} = 2 \times \hat{{C}} = 2 \times {angle_circ}^\circ = {angle_centre}^\circ \quad ({reason})"

    rad_span = math.radians(angle_centre / 2)
    a_x = round(3.0 * math.sin(-rad_span), 2)
    a_y = round(-3.0 * math.cos(-rad_span), 2)
    b_x = round(3.0 * math.sin(rad_span), 2)
    b_y = round(-3.0 * math.cos(rad_span), 2)
    diag = {
        "kind": "circle_subtended_angle",
        "center": "O",
        "radius": 3.0,
        "points": {
            "O": [0.0, 0.0],
            "A": [a_x, a_y],
            "B": [b_x, b_y],
            "C": [0.0, 3.0],
        },
        "lines": [["O", "A"], ["O", "B"], ["C", "A"], ["C", "B"]],
        "angles": [
            {"arms": ["A", "C", "B"], "label": f"{angle_circ}°", "radius": 0.8},
            {"arms": ["A", "O", "B"], "label": "O", "radius": 0.6},
        ],
        "vertex_labels": {"O": "O", "A": "A", "B": "B", "C": "C"},
        "caption": f"Circle with centre O and inscribed angle C = {angle_circ}° subtending arc AB",
    }

    return make_math_question(
        prefix="geo_cent",
        topic=TOPIC,
        subskill="elementary_angle_at_centre",
        learning_objective_id=f"{LO}_angle_at_centre",
        prompt=prompt,
        prompt_latex=prompt,
        answer_latex=f"{angle_centre}^\\circ",
        answer_sympy=str(angle_centre),
        sample_answer=sample,
        diagram_spec=diag,
        marking_schema={
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": f"Correct value of angle: {angle_centre} deg", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Correct CAPS reason (angle at centre = 2 * angle at circ)", "marks": 1, "editable": True},
            ],
            "deductions": [{"rule": "omitted_geometric_reason", "penalty": -1}],
            "carry_forward_rule": "strict",
        },
        hints={
            "1_nudge": "The angle subtended by an arc at the centre is twice the angle subtended by the same arc at the circumference.",
            "2_concept": "$\\hat{O} = 2\\hat{C}$ with reason $(\\angle \\text{ at centre } = 2\\angle \\text{ at circ})$.",
            "3_breakdown": f"$\\hat{{O}} = 2 \\times {angle_circ}^\\circ = {angle_centre}^\\circ$.",
        },
        misconception_tags=["divided_by_two_instead_of_multiplying", "omitted_geometric_reason"],
        keywords=["circle geometry", "angle at centre", "subtended arc"],
        term=3,
        caps_weight_percent=35,
        suggested_duration_mins=3,
        mode="elementary_angle_at_centre",
        difficulty="easy",
    )


# --------------------------------------------------------------------------- #
# Sub-Drill: Cyclic Quadrilateral Theorems
# --------------------------------------------------------------------------- #
def _build_cyclic_quad(r, difficulty: str) -> Dict[str, Any]:
    angle_a = r.randint(72, 115)
    angle_c = 180 - angle_a
    ext_angle = angle_a # exterior angle equals interior opposite angle

    pts = {
        "O": [0.0, 0.0],
        "A": [-2.12, 2.12],   # 135 deg
        "B": [-2.30, -1.93],  # 220 deg
        "C": [1.93, -2.30],   # 310 deg
        "D": [2.12, 2.12],    # 45 deg
    }
    v_labels = {"O": "O", "A": "A", "B": "B", "C": "C", "D": "D"}
    use_opp = r.random() < 0.5

    if use_opp:
        prompt = (
            f"$ABCD$ is a cyclic quadrilateral. If $\\hat{{A}} = {angle_a}^\\circ$, "
            f"calculate the size of opposite angle $\\hat{{C}}$. State the geometric reason."
        )
        ans = f"{angle_c}^\\circ"
        sample = rf"\hat{{C}} = 180^\circ - {angle_a}^\circ = {angle_c}^\circ \quad (\text{{opp }} \angle\text{{s of cyclic quad}})"
        reason = "opp angles of cyclic quad"
        lines = [["A", "B"], ["B", "C"], ["C", "D"], ["D", "A"]]
        angles = [
            {"arms": ["B", "A", "D"], "label": f"{angle_a}°", "radius": 0.7},
            {"arms": ["D", "C", "B"], "label": "C", "radius": 0.7},
        ]
        cap = f"Cyclic quadrilateral ABCD with angle A = {angle_a}°"
    else:
        prompt = (
            f"In cyclic quadrilateral $ABCD$, side $BC$ is produced to point $P$. "
            f"If $\\hat{{A}} = {angle_a}^\\circ$, determine the size of exterior angle $D\\hat{{C}}P$. State the geometric reason."
        )
        ans = f"{ext_angle}^\\circ"
        sample = rf"D\hat{{C}}P = \hat{{A}} = {angle_a}^\circ \quad (\text{{ext }} \angle \text{{ of cyclic quad}})"
        reason = "ext angle of cyclic quad"
        p_x = round(1.93 + 0.5 * (1.93 - (-2.30)), 2)
        p_y = round(-2.30 + 0.5 * (-2.30 - (-1.93)), 2)
        pts["P"] = [p_x, p_y]
        v_labels["P"] = "P"
        lines = [["A", "B"], ["B", "C"], ["C", "D"], ["D", "A"], ["C", "P"]]
        angles = [
            {"arms": ["B", "A", "D"], "label": f"{angle_a}°", "radius": 0.7},
            {"arms": ["P", "C", "D"], "label": "DCP", "radius": 0.7},
        ]
        cap = f"Cyclic quadrilateral ABCD with BC produced to P and angle A = {angle_a}°"

    diag = {
        "kind": "circle_cyclic_quad",
        "center": "O",
        "radius": 3.0,
        "points": pts,
        "lines": lines,
        "angles": angles,
        "vertex_labels": v_labels,
        "caption": cap,
    }

    return make_math_question(
        prefix="geo_cyc",
        topic=TOPIC,
        subskill="elementary_cyclic_quad",
        learning_objective_id=f"{LO}_cyclic_quad",
        prompt=prompt,
        prompt_latex=prompt,
        answer_latex=ans,
        answer_sympy=str(angle_c if use_opp else ext_angle),
        sample_answer=sample,
        diagram_spec=diag,
        marking_schema={
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": f"Correct angle size: {ans}", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Correct geometric reason ({reason})", "marks": 1, "editable": True},
            ],
            "deductions": [{"rule": "omitted_geometric_reason", "penalty": -1}],
            "carry_forward_rule": "strict",
        },
        hints={
            "1_nudge": "Opposite angles of a cyclic quad sum to 180°, and the exterior angle equals the interior opposite angle.",
            "2_concept": f"Apply: {reason}.",
            "3_breakdown": sample,
        },
        misconception_tags=["confused_cyclic_quad_with_parallelogram", "omitted_geometric_reason"],
        keywords=["cyclic quad", "opposite angles", "exterior angle", "circle geometry"],
        term=3,
        caps_weight_percent=35,
        suggested_duration_mins=3,
        mode="elementary_cyclic_quad",
        difficulty="easy",
    )


# --------------------------------------------------------------------------- #
# Sub-Drill: Tangent-Chord Theorem
# --------------------------------------------------------------------------- #
def _build_tan_chord(r, difficulty: str) -> Dict[str, Any]:
    angle_alt = r.randint(34, 68)

    prompt = (
        f"In the circle, line $PT$ is a tangent to the circle at point $A$. Chord $AB$ is drawn. "
        f"Point $C$ lies on the major arc such that $\\hat{{C}} = {angle_alt}^\\circ$. "
        f"Determine the size of angle $T\\hat{{A}}B$ between the tangent and the chord. Give the complete reason."
    )

    ans = f"{angle_alt}^\\circ"
    sample = rf"T\hat{{A}}B = \hat{{C}} = {angle_alt}^\circ \quad (\text{{tan chord theorem}})"

    rad_alt = math.radians(angle_alt)
    b_x = round(3.0 * math.sin(2 * rad_alt), 2)
    b_y = round(-3.0 * math.cos(2 * rad_alt), 2)
    diag = {
        "kind": "circle_tangent_secant",
        "center": "O",
        "radius": 3.0,
        "points": {
            "O": [0.0, 0.0],
            "A": [0.0, -3.0],
            "P": [-4.0, -3.0],
            "T": [4.0, -3.0],
            "B": [b_x, b_y],
            "C": [0.0, 3.0],
        },
        "lines": [["P", "T"], ["A", "B"], ["A", "C"], ["C", "B"]],
        "angles": [
            {"arms": ["A", "C", "B"], "label": f"{angle_alt}°", "radius": 0.8},
            {"arms": ["T", "A", "B"], "label": "TAB", "radius": 0.7},
        ],
        "vertex_labels": {"O": "O", "A": "A", "B": "B", "C": "C", "P": "P", "T": "T"},
        "caption": f"Tangent PT at A, chord AB, and inscribed angle C = {angle_alt}° (not to scale)",
    }

    return make_math_question(
        prefix="geo_tanchord",
        topic=TOPIC,
        subskill="elementary_tan_chord",
        learning_objective_id=f"{LO}_tan_chord",
        prompt=prompt,
        prompt_latex=prompt,
        answer_latex=ans,
        answer_sympy=str(angle_alt),
        sample_answer=sample,
        diagram_spec=diag,
        marking_schema={
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": f"Correct angle size: {angle_alt} deg", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Correct CAPS reason (tan chord theorem)", "marks": 1, "editable": True},
            ],
            "deductions": [{"rule": "omitted_geometric_reason", "penalty": -1}],
            "carry_forward_rule": "strict",
        },
        hints={
            "1_nudge": "The angle between a tangent and a chord equals the angle subtended by the chord in the alternate segment.",
            "2_concept": "Tan-Chord Theorem: $T\\hat{A}B = A\\hat{C}B$.",
            "3_breakdown": f"$T\\hat{{A}}B = {angle_alt}^\\circ$ (tan chord theorem).",
        },
        misconception_tags=["confused_tan_chord_with_radius_perp", "omitted_geometric_reason"],
        keywords=["tan chord theorem", "tangent", "chord", "alternate segment"],
        term=3,
        caps_weight_percent=35,
        suggested_duration_mins=3,
        mode="elementary_tan_chord",
        difficulty="easy",
    )


# --------------------------------------------------------------------------- #
# Compound Level 3 & 4 Exam Question: Multi-Theorem Circle Geometry Rider
# --------------------------------------------------------------------------- #
def _build_compound_circle_rider(r, difficulty: str) -> Dict[str, Any]:
    ang_d = r.randint(35, 48)
    ang_centre = 2 * ang_d
    ang_b = 180 - ang_d
    ang_tanchord = ang_d

    prompt = (
        f"In the diagram below, circle with centre $O$ passes through points $A$, $B$, $C$, and $D$.\n"
        f"A tangent line $PT$ touches the circle at point $A$.\n"
        f"It is given that $\\hat{{D}} = {ang_d}^\\circ$.\n\n"
        f"Determine, with complete geometric reasons, the size of:\n"
        f"1. Angle at centre $\\hat{{O}}_1$ subtended by chord $AC$.\n"
        f"2. Angle $\\hat{{B}}$ of cyclic quadrilateral $ABCD$.\n"
        f"3. Angle $P\\hat{{A}}C$ between the tangent $PT$ and chord $AC$."
    )

    steps = [
        step(
            from_latex=rf"\hat{{D}} = {ang_d}^\circ",
            to_latex_str=rf"\hat{{O}}_1 = 2 \times \hat{{D}} = 2({ang_d}^\circ) = {ang_centre}^\circ \quad (\angle \text{{ at centre }} = 2\times\angle \text{{ at circ}})",
            op="apply angle at centre theorem",
            rule=r"\angle \text{ at centre } = 2\times\angle \text{ at circ}",
        ),
        step(
            from_latex=rf"\hat{{D}} = {ang_d}^\circ",
            to_latex_str=rf"\hat{{B}} = 180^\circ - {ang_d}^\circ = {ang_b}^\circ \quad (\text{{opp }} \angle\text{{s of cyclic quad}})",
            op="apply cyclic quad supplementary opposite angles",
            rule="opp angles of cyclic quad",
        ),
        step(
            from_latex=rf"\hat{{D}} = {ang_d}^\circ",
            to_latex_str=rf"P\hat{{A}}C = \hat{{D}} = {ang_tanchord}^\circ \quad (\text{{tan chord theorem}})",
            op="apply tan-chord theorem",
            rule="tan chord theorem",
        ),
    ]

    canonical = solution_graph(
        goal="determine multi-theorem circle rider angles with reasons",
        steps=steps,
        final_latex=rf"\hat{{O}}_1 = {ang_centre}^\circ, \; \hat{{B}} = {ang_b}^\circ, \; P\hat{{A}}C = {ang_tanchord}^\circ",
    )

    marking_schema = {
        "total_marks": 7,
        "marking_points": [
            {"id": "mp1", "desc": f"Angle O1 = {ang_centre} deg", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Reason for O1 (angle at centre = 2 * angle at circ)", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Angle B = {ang_b} deg", "marks": 1, "editable": True},
            {"id": "mp4", "desc": "Reason for B (opp angles of cyclic quad)", "marks": 1, "editable": True},
            {"id": "mp5", "desc": f"Angle PAC = {ang_tanchord} deg", "marks": 1, "editable": True},
            {"id": "mp6", "desc": "Reason for PAC (tan chord theorem)", "marks": 1, "editable": True},
            {"id": "mp7", "desc": "All reasons mathematically correct using CAPS nomenclature", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "omitted_or_incorrect_reasons", "penalty": -2}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "nudge": "Apply the angle at centre theorem for $\\hat{O}_1$, cyclic quad opposite angles for $\\hat{B}$, and the tan-chord theorem for $P\\hat{A}C$.",
        "concept": "Every statement in Euclidean circle geometry MUST have an accepted CAPS abbreviation reason.",
        "breakdown": (
            f"1. $\\hat{{O}}_1 = 2({ang_d}^\\circ) = {ang_centre}^\\circ$ ($\\angle$ at centre $= 2\\angle$ at circ).\n"
            f"2. $\\hat{{B}} = 180^\\circ - {ang_d}^\\circ = {ang_b}^\\circ$ (opp $\\angle$s of cyclic quad).\n"
            f"3. $P\\hat{{A}}C = {ang_d}^\\circ$ (tan chord theorem)."
        ),
    }

    rad_d = math.radians(ang_d)
    c_x = round(-3.0 * math.sin(2 * rad_d), 2)
    c_y = round(-3.0 * math.cos(2 * rad_d), 2)
    diag = {
        "kind": "circle_tangent_secant",
        "center": "O",
        "radius": 3.0,
        "points": {
            "O": [0.0, 0.0],
            "A": [0.0, -3.0],
            "P": [-4.0, -3.0],
            "T": [4.0, -3.0],
            "C": [c_x, c_y],
            "D": [0.0, 3.0],
            "B": [2.82, -1.03],
        },
        "lines": [
            ["P", "T"],
            ["A", "C"],
            ["O", "A"],
            ["O", "C"],
            ["A", "B"],
            ["B", "C"],
            ["C", "D"],
            ["D", "A"],
        ],
        "angles": [
            {"arms": ["A", "D", "C"], "label": f"{ang_d}°", "radius": 0.7},
            {"arms": ["A", "O", "C"], "label": "O1", "radius": 0.6},
            {"arms": ["A", "B", "C"], "label": "B", "radius": 0.7},
            {"arms": ["P", "A", "C"], "label": "PAC", "radius": 0.7},
        ],
        "vertex_labels": {"O": "O", "A": "A", "B": "B", "C": "C", "D": "D", "P": "P", "T": "T"},
        "caption": f"Circle with centre O, cyclic quad ABCD, chord AC, and tangent PT at A (not to scale)",
    }

    return make_math_question(
        prefix="geo_circle_rider",
        topic=TOPIC,
        subskill="circle_geometry_rider_compound",
        learning_objective_id=f"{LO}_compound_rider",
        prompt=prompt,
        prompt_latex=prompt,
        answer_latex=rf"\hat{{O}}_1 = {ang_centre}^\circ, \quad \hat{{B}} = {ang_b}^\circ, \quad P\hat{{A}}C = {ang_tanchord}^\circ",
        answer_sympy=f"O1={ang_centre}, B={ang_b}, PAC={ang_tanchord}",
        sample_answer=canonical["final_latex"],
        canonical_solution=canonical,
        diagram_spec=diag,
        marking_schema=marking_schema,
        hints=hints,
        misconception_tags=["omitted_geometric_reasons", "confused_cyclic_quad_opposite_angles", "tan_chord_misidentification"],
        keywords=["circle geometry rider", "tan chord theorem", "cyclic quad", "angle at centre", "reasons"],
        term=3,
        caps_weight_percent=35,
        suggested_duration_mins=12,
        mode="compound",
        difficulty="hard",
    )


# --------------------------------------------------------------------------- #
# Public Dispatcher
# --------------------------------------------------------------------------- #
BUILDERS = {
    "compound": _build_compound_circle_rider,
    "elementary_angle_at_centre": _build_angle_at_centre,
    "elementary_cyclic_quad": _build_cyclic_quad,
    "elementary_tan_chord": _build_tan_chord,
}


def generate(
    subskill: Optional[str] = None,
    difficulty: str = "hard",
    count: int = 1,
    seed: Optional[int] = None,
    mode: str = "compound",
    **kwargs: Any,
) -> Dict[str, Any]:
    """Generates deterministic Grade 11 Circle Geometry questions."""
    base_seed = 42 if seed is None else int(seed)
    target = subskill if (subskill and subskill in BUILDERS) else mode
    builder = BUILDERS.get(target, _build_compound_circle_rider)

    questions = []
    for i in range(max(1, count)):
        r = rng(base_seed * 1000 + i)
        q = builder(r, difficulty)
        q["seed"] = base_seed * 1000 + i
        questions.append(q)

    return {"questions": questions}
