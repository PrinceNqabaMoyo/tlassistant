"""Grade 11 Mathematics — Euclidean Circle Geometry Theorems (Deterministic 6-Pillar Generator).
Covers official South African National Curriculum Standards (Paper 2 — 35 to 40 marks):
- Theorem: Angle at centre = 2 * angle at circumference (angle at centre = 2 * angle at circ)
- Theorem: Angles in the same segment are equal (angles in same seg)
- Theorem: Opposite angles of cyclic quad are supplementary (opp angles of cyclic quad)
- Theorem: Exterior angle of cyclic quad = interior opposite angle (ext angle of cyclic quad)
- Theorem: Tangent-chord theorem (tan chord theorem)
Supports full compound exam questions, atomic elementary sub-drills, and all 50 semantic archetypes.
"""

# Diagram contract: all diagrams emitted specify diagram_role: "context" | "identify"
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
from app.utils.grade11_mathematics.circle_geometry_archetypes_01_25 import (
    ARCHETYPE_BUILDERS_01_25,
    _pt_on_circle,
    circle_geo_svg,
)
from app.utils.grade11_mathematics.circle_geometry_archetypes_26_50 import (
    ARCHETYPE_BUILDERS_26_50,
)

TOPIC = "euclidean_circle_geometry"
LO = "math11_circle_geometry"


# --------------------------------------------------------------------------- #
# Sub-Drill: Angle at Centre = 2 * Angle at Circumference
# --------------------------------------------------------------------------- #
def _build_angle_at_centre(r, difficulty: str = "easy") -> Dict[str, Any]:
    angle_circ = r.randint(28, 55)
    angle_centre = 2 * angle_circ

    prompt = (
        f"In the circle with centre $O$, points $A$, $B$, and $C$ lie on the circumference. "
        f"If the inscribed angle $\\hat{{C}} = {angle_circ}^\\circ$, calculate the size of the angle "
        f"$\\hat{{O}}$ subtended by the same arc $AB$. State the complete geometric reason."
    )

    reason = r"\angle \text{ at centre } = 2\times \angle \text{ at circ}"
    sample = rf"\hat{{O}} = 2 \times \hat{{C}} = 2 \times {angle_circ}^\circ = {angle_centre}^\circ \quad ({reason})"

    pts = {
        "O": (210.0, 155.0),
        "A": _pt_on_circle(135),
        "B": _pt_on_circle(45),
        "C": _pt_on_circle(270),
    }
    diag = circle_geo_svg(
        title=f"Circle Centre O with Inscribed ∠C = {angle_circ}° Subtending Arc AB",
        points=pts,
        segments=[("O", "A"), ("O", "B"), ("C", "A"), ("C", "B")],
        callouts=[(210, 95, f"∠C = {angle_circ}°", "#1d4ed8"), (210, 182, "∠O = ?", "#dc2626")],
    )

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
                {"id": "mp2", "desc": "Correct geometric reason (angle at centre = 2 * angle at circ)", "marks": 1, "editable": True},
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
def _build_cyclic_quad(r, difficulty: str = "easy") -> Dict[str, Any]:
    angle_a = r.randint(72, 115)
    angle_c = 180 - angle_a
    ext_angle = angle_a

    pts = {
        "A": _pt_on_circle(140),
        "B": _pt_on_circle(55),
        "C": _pt_on_circle(325),
        "D": _pt_on_circle(220),
    }

    use_opp = r.random() < 0.5

    if use_opp:
        prompt = (
            f"$ABCD$ is a cyclic quadrilateral. If $\\hat{{A}} = {angle_a}^\\circ$, "
            f"calculate the size of opposite angle $\\hat{{C}}$. State the geometric reason."
        )
        ans = f"{angle_c}^\\circ"
        sample = rf"\hat{{C}} = 180^\circ - {angle_a}^\circ = {angle_c}^\circ \quad (\text{{opp }} \angle\text{{s of cyclic quad}})"
        reason = "opp angles of cyclic quad"
        segs = [("A", "B"), ("B", "C"), ("C", "D"), ("D", "A")]
        cap = f"Cyclic Quadrilateral ABCD with ∠A = {angle_a}°"
    else:
        prompt = (
            f"In cyclic quadrilateral $ABCD$, side $BC$ is produced to point $P$. "
            f"If $\\hat{{A}} = {angle_a}^\\circ$, determine the size of exterior angle $D\\hat{{C}}P$. State the geometric reason."
        )
        ans = f"{ext_angle}^\\circ"
        sample = rf"D\hat{{C}}P = \hat{{A}} = {angle_a}^\circ \quad (\text{{ext }} \angle \text{{ of cyclic quad}})"
        reason = "ext angle of cyclic quad"
        pts["P"] = (355.0, 62.0)
        segs = [("A", "B"), ("B", "C"), ("C", "D"), ("D", "A"), ("C", "P")]
        cap = f"Cyclic Quadrilateral ABCD with BC Produced to P and ∠A = {angle_a}°"

    diag = circle_geo_svg(
        title=cap,
        points=pts,
        segments=segs,
        show_center=False,
        callouts=[(162, 198, f"∠A={angle_a}°", "#1d4ed8")],
    )

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
def _build_tan_chord(r, difficulty: str = "easy") -> Dict[str, Any]:
    angle_alt = r.randint(34, 68)

    prompt = (
        f"In the circle, line $PT$ is a tangent to the circle at point $A$. Chord $AB$ is drawn. "
        f"Point $C$ lies on the major arc such that $\\hat{{C}} = {angle_alt}^\\circ$. "
        f"Determine the size of angle $T\\hat{{A}}B$ between the tangent and the chord. Give the complete reason."
    )

    ans = f"{angle_alt}^\\circ"
    sample = rf"T\hat{{A}}B = \hat{{C}} = {angle_alt}^\circ \quad (\text{{tan chord theorem}})"

    pts = {
        "A": (210.0, 247.0),
        "P": (95.0, 247.0),
        "T": (325.0, 247.0),
        "B": _pt_on_circle(25),
        "C": _pt_on_circle(215),
    }
    diag = circle_geo_svg(
        title=f"Tangent PT at A, Chord AB, and Inscribed ∠C = {angle_alt}°",
        points=pts,
        segments=[("P", "T"), ("A", "B"), ("B", "C"), ("C", "A")],
        show_center=False,
        callouts=[(162, 115, f"∠C={angle_alt}°", "#1d4ed8"), (265, 238, "∠TAB=?", "#dc2626")],
    )

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
                {"id": "mp2", "desc": "Correct geometric reason (tan chord theorem)", "marks": 1, "editable": True},
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
def _build_compound_circle_rider(r, difficulty: str = "hard") -> Dict[str, Any]:
    ang_d = r.randint(35, 48)
    ang_centre = 2 * ang_d
    ang_b = 180 - ang_d
    ang_tanchord = ang_d

    prompt = (
        f"In the diagram, circle with centre $O$ passes through points $A$, $B$, $C$, and $D$.\n"
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
            {"id": "mp7", "desc": "All reasons mathematically correct using standard geometric nomenclature", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "omitted_or_incorrect_reasons", "penalty": -2}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "nudge": "Apply the angle at centre theorem for $\\hat{O}_1$, cyclic quad opposite angles for $\\hat{B}$, and the tan-chord theorem for $P\\hat{A}C$.",
        "concept": "Every statement in Euclidean circle geometry must have an accepted geometric reason.",
        "breakdown": (
            f"1. $\\hat{{O}}_1 = 2({ang_d}^\\circ) = {ang_centre}^\\circ$ ($\\angle$ at centre $= 2\\angle$ at circ).\n"
            f"2. $\\hat{{B}} = 180^\\circ - {ang_d}^\\circ = {ang_b}^\\circ$ (opp $\\angle$s of cyclic quad).\n"
            f"3. $P\\hat{{A}}C = {ang_d}^\\circ$ (tan chord theorem)."
        ),
    }

    pts = {
        "O": (210.0, 155.0),
        "A": (210.0, 247.0),
        "P": (95.0, 247.0),
        "T": (325.0, 247.0),
        "B": _pt_on_circle(25),
        "C": _pt_on_circle(315),
        "D": _pt_on_circle(215),
    }
    diag = circle_geo_svg(
        title=f"Circle Centre O, Cyclic Quad ABCD, and Tangent PT at A (∠D = {ang_d}°)",
        points=pts,
        segments=[("P", "T"), ("O", "A"), ("O", "C"), ("A", "C"), ("A", "B"), ("B", "C"), ("C", "D"), ("D", "A")],
        callouts=[(162, 112, f"∠D={ang_d}°", "#1d4ed8"), (210, 292, "Find ∠O1, ∠B, and ∠PAC", "#dc2626")],
    )

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
# Public Dispatcher (50-Archetype Contract)
# --------------------------------------------------------------------------- #
ARCHETYPE_BUILDERS = {
    **ARCHETYPE_BUILDERS_01_25,
    **ARCHETYPE_BUILDERS_26_50,
}
ORDERED_SUBSKILLS = sorted(ARCHETYPE_BUILDERS.keys())
SUBSKILLS = ORDERED_SUBSKILLS

DISPATCH_TABLE = dict(ARCHETYPE_BUILDERS)
DISPATCH_TABLE["compound"] = _build_compound_circle_rider
DISPATCH_TABLE["elementary_angle_at_centre"] = _build_angle_at_centre
DISPATCH_TABLE["elementary_cyclic_quad"] = _build_cyclic_quad
DISPATCH_TABLE["elementary_tan_chord"] = _build_tan_chord

BUILDERS = DISPATCH_TABLE
SUBSKILL_BUILDERS = DISPATCH_TABLE


def get_subskills() -> List[str]:
    """Returns the ordered list of all 50 semantic subskills."""
    return list(ORDERED_SUBSKILLS)


def generate(
    subskill: Optional[str] = None,
    difficulty: str = "hard",
    count: int = 1,
    seed: Optional[int] = None,
    mode: Optional[str] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    """Generates deterministic Grade 11 Circle Geometry questions."""
    base_seed = 42 if seed is None else int(seed)
    target = subskill or mode
    if not target or target not in DISPATCH_TABLE:
        target = ORDERED_SUBSKILLS[base_seed % len(ORDERED_SUBSKILLS)] if ORDERED_SUBSKILLS else "compound"
    builder = DISPATCH_TABLE.get(target, _build_compound_circle_rider)

    questions = []
    for i in range(max(1, count)):
        run_seed = base_seed * 1000 + i
        r = rng(run_seed)
        q = builder(r, difficulty)
        q["seed"] = run_seed
        questions.append(q)

    return {"questions": questions}
