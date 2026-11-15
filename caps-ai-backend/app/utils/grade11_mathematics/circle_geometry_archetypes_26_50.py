"""Grade 11 Mathematics — Euclidean Geometry (Circle Geometry): Archetypes 26 to 50.

Grounded strictly in:
- curriculum_docs/Mathematics_Gr11/Term_3/Euclidean geometry.md
- curriculum_docs_auto/Mathematics_Gr11/Term 3/03. Euclidean geometry.md
- Official South African National Curriculum Standards for Grade 11 Mathematics Paper 2.

Zero-LLM, 100% deterministic Python & SymPy calculations with South African comma decimals ({,})
and dynamic seed-varied inline SVG circle geometry figures.
"""
from __future__ import annotations

import math
import random
from typing import Any, Callable, Dict, List, Optional, Tuple

from app.utils.grade11_mathematics._math_common import (
    make_id,
    make_math_question,
    nonzero,
    num,
    rng,
    solution_graph,
    step,
    to_latex,
)
from app.utils.grade11_mathematics.circle_geometry_archetypes_01_25 import (
    LEARNING_OBJECTIVE_ID,
    TOPIC_NAME,
    _pt_on_circle,
    circle_geo_svg,
)

# 26. Cyclic Quadrilateral — Opposite Angles Supplementary
def arch_26_cyclic_quad_opposite_angles_supplementary(r: random.Random, difficulty: str = "easy") -> Dict[str, Any]:
    ang_a = r.randint(68, 128)
    ang_c = 180 - ang_a

    pts = {
        "A": _pt_on_circle(140),
        "B": _pt_on_circle(55),
        "C": _pt_on_circle(325),
        "D": _pt_on_circle(220),
    }

    prompt = (
        f"In the circle, $ABCD$ is a cyclic quadrilateral. "
        f"If $\\hat{{A}} = {ang_a}^\\circ$, calculate the size of opposite angle $\\hat{{C}}$ "
        f"and state the geometric reason."
    )

    diag = circle_geo_svg(
        title=f"Cyclic Quadrilateral ABCD: ∠A = {ang_a}° — Find ∠C",
        points=pts,
        segments=[("A", "B"), ("B", "C"), ("C", "D"), ("D", "A")],
        show_center=False,
        callouts=[(162, 200, f"∠A={ang_a}°", "#1d4ed8"), (260, 118, "∠C=?", "#dc2626")],
    )

    steps = [
        step(from_latex=rf"\hat{{A}} + \hat{{C}} = 180^\circ", to_latex_str=rf"\hat{{C}} = 180^\circ - {ang_a}^\circ = {ang_c}^\circ \quad (\text{{opp }}\angle\text{{s of cyclic quad}})", op="apply supplementary opposite angles of a cyclic quad", rule="opposite angles of cyclic quadrilateral",),
    ]
    canonical = solution_graph(goal="find opposite angle C of cyclic quad", steps=steps, final_latex=rf"{ang_c}^\circ")

    return make_math_question(
        prefix="g11_cg_26",
        topic=TOPIC_NAME,
        subskill="26_cyclic_quad_opposite_angles_supplementary",
        learning_objective_id=f"{LEARNING_OBJECTIVE_ID}_26",
        prompt=prompt,
        prompt_latex=prompt,
        answer_latex=rf"{ang_c}^\circ",
        answer_sympy=str(ang_c),
        sample_answer=rf"\hat{{C}} = 180^\circ - {ang_a}^\circ = {ang_c}^\circ \quad (\text{{opp }}\angle\text{{s of cyclic quad}})",
        canonical_solution=canonical,
        diagram_spec=diag,
        marking_schema={
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": f"Angle C = {ang_c} deg", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Reason: opp angles of cyclic quad", "marks": 1, "editable": True},
            ],
        },
        hints={
            "1_nudge": "All four vertices $A, B, C, D$ lie on the circumference, so $ABCD$ is a cyclic quadrilateral.",
            "2_concept": "Opposite angles of a cyclic quadrilateral are supplementary: $\\hat{A} + \\hat{C} = 180^\\circ$ (opp $\\angle$s of cyclic quad).",
            "3_breakdown": f"$\\hat{{C}} = 180^\\circ - {ang_a}^\\circ = {ang_c}^\\circ$.",
        },
        misconception_tags=["opposite_angles_cyclic_quad_equality", "omitted_geometric_reason"],
        keywords=["circle geometry", "cyclic quadrilateral", "supplementary opposite angles"],
        term=3,
        caps_weight_percent=35,
        suggested_duration_mins=2,
        mode="elementary_26_cyclic_quad_opposite_angles_supplementary",
        difficulty=difficulty,
    )

# 27. Cyclic Quadrilateral — Algebraic Opposite Angles
def arch_27_cyclic_quad_opposite_angles_algebraic_x(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    x_val = r.randint(24, 38)
    a_val = r.randint(4, 16)
    ang_a = 2 * x_val + a_val
    ang_c = 180 - ang_a
    b_val = ang_c - 3 * x_val
    b_str = f"+ {b_val}^\\circ" if b_val >= 0 else f"- {abs(b_val)}^\\circ"

    pts = {
        "A": _pt_on_circle(140),
        "B": _pt_on_circle(55),
        "C": _pt_on_circle(325),
        "D": _pt_on_circle(220),
    }

    prompt = (
        f"In cyclic quadrilateral $ABCD$, $\\hat{{A}} = (2x + {a_val}^\\circ)$ and $\\hat{{C}} = (3x {b_str})$. "
        f"Calculate the value of $x$ and state the geometric reason."
    )

    diag = circle_geo_svg(
        title=f"Algebraic Cyclic Quad: ∠A = 2x + {a_val}°, ∠C = 3x {b_str.replace('^\\circ', '°')}",
        points=pts,
        segments=[("A", "B"), ("B", "C"), ("C", "D"), ("D", "A")],
        show_center=False,
        callouts=[(162, 200, f"2x+{a_val}°", "#1d4ed8"), (260, 118, f"3x{b_str.replace('^\\circ', '°')}", "#dc2626")],
    )

    steps = [
        step(from_latex=r"\hat{A} + \hat{C} = 180^\circ", to_latex_str=rf"(2x + {a_val}^\circ) + (3x {b_str}) = 180^\circ \quad (\text{{opp }}\angle\text{{s of cyclic quad}})", op="sum opposite angles of cyclic quad to 180 degrees", rule="opposite angles of cyclic quadrilateral",),
        step(from_latex=rf"5x = {5*x_val}^\circ", to_latex_str=rf"x = {x_val}^\circ", op="solve linear equation for x", rule="linear equation",),
    ]
    canonical = solution_graph(goal="solve for x in cyclic quad", steps=steps, final_latex=rf"{x_val}^\circ")

    return make_math_question(
        prefix="g11_cg_27",
        topic=TOPIC_NAME,
        subskill="27_cyclic_quad_opposite_angles_algebraic_x",
        learning_objective_id=f"{LEARNING_OBJECTIVE_ID}_27",
        prompt=prompt,
        prompt_latex=prompt,
        answer_latex=rf"{x_val}^\circ",
        answer_sympy=str(x_val),
        sample_answer=rf"(2x + {a_val}^\circ) + (3x {b_str}) = 180^\circ \implies 5x = {5*x_val}^\circ \implies x = {x_val}^\circ \quad (\text{{opp }}\angle\text{{s of cyclic quad}})",
        canonical_solution=canonical,
        diagram_spec=diag,
        marking_schema={
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": "Sum of opposite angles equated to 180 deg", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Reason: opp angles of cyclic quad", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"x = {x_val} deg", "marks": 1, "editable": True},
            ],
        },
        hints={
            "1_nudge": "Do not equate opposite angles of a cyclic quad—add them to $180^\\circ$.",
            "2_concept": "$\\hat{A} + \\hat{C} = 180^\\circ$ (opp $\\angle$s of cyclic quad).",
            "3_breakdown": f"$5x = {5*x_val}^\\circ \\implies x = {x_val}^\\circ$.",
        },
        misconception_tags=["opposite_angles_cyclic_quad_equality", "omitted_geometric_reason"],
        keywords=["circle geometry", "cyclic quad", "algebraic"],
        term=3,
        caps_weight_percent=35,
        suggested_duration_mins=3,
        mode="elementary_27_cyclic_quad_opposite_angles_algebraic_x",
        difficulty=difficulty,
    )

# 28. Cyclic Quadrilateral with Parallel Sides (Isosceles Cyclic Trapezium)
def arch_28_cyclic_quad_with_parallel_sides(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    ang_a = r.randint(68, 118)
    ang_d = 180 - ang_a
    ang_c = ang_d
    ang_b = ang_a

    pts = {
        "A": _pt_on_circle(145),
        "B": _pt_on_circle(35),
        "C": _pt_on_circle(325),
        "D": _pt_on_circle(215),
    }

    prompt = (
        f"$ABCD$ is a cyclic quadrilateral in which $AB \\parallel DC$. "
        f"If $\\hat{{A}} = {ang_a}^\\circ$, determine the size of $\\hat{{B}}$, "
        f"stating all geometric reasons."
    )

    diag = circle_geo_svg(
        title=f"Cyclic Quad ABCD with AB ∥ DC: ∠A = {ang_a}° — Find ∠B",
        points=pts,
        segments=[("A", "B"), ("B", "C"), ("C", "D"), ("D", "A")],
        show_center=False,
        callouts=[(162, 198, f"∠A={ang_a}°", "#1d4ed8"), (260, 198, "∠B=?", "#dc2626"), (210, 290, "AB ∥ DC", "#0f172a")],
    )

    steps = [
        step(from_latex=rf"\hat{{A}} = {ang_a}^\circ", to_latex_str=rf"\hat{{C}} = 180^\circ - {ang_a}^\circ = {ang_c}^\circ \quad (\text{{opp }}\angle\text{{s of cyclic quad}})", op="find opposite angle C", rule="opposite angles of cyclic quadrilateral",),
        step(from_latex=rf"AB \parallel DC, \; \hat{{C}} = {ang_c}^\circ", to_latex_str=rf"\hat{{B}} = 180^\circ - {ang_c}^\circ = {ang_b}^\circ \quad (\text{{co-int }}\angle\text{{s, }} AB \parallel DC)", op="use co-interior angles to find angle B", rule="co-interior angles on parallel lines",),
    ]
    canonical = solution_graph(goal="find angle B in cyclic quad with parallel sides", steps=steps, final_latex=rf"{ang_b}^\circ")

    return make_math_question(
        prefix="g11_cg_28",
        topic=TOPIC_NAME,
        subskill="28_cyclic_quad_with_parallel_sides",
        learning_objective_id=f"{LEARNING_OBJECTIVE_ID}_28",
        prompt=prompt,
        prompt_latex=prompt,
        answer_latex=rf"{ang_b}^\circ",
        answer_sympy=str(ang_b),
        sample_answer=rf"\hat{{C}} = 180^\circ - {ang_a}^\circ = {ang_c}^\circ \text{{ (opp }}\angle\text{{s of cyclic quad)}}; \; \hat{{B}} = 180^\circ - {ang_c}^\circ = {ang_b}^\circ \text{{ (co-int }}\angle\text{{s, }} AB \parallel DC\text{{)}}",
        canonical_solution=canonical,
        diagram_spec=diag,
        marking_schema={
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": f"Angle C = {ang_c} deg (opp angles of cyclic quad)", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Reason: co-int angles, AB || DC", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Angle B = {ang_b} deg", "marks": 1, "editable": True},
            ],
        },
        hints={
            "1_nudge": "First find $\\hat{C}$ using opposite angles of a cyclic quad, then use co-interior angles between $AB \\parallel DC$.",
            "2_concept": "$\\hat{C} = 180^\\circ - \\hat{A}$ (opp $\\angle$s of cyclic quad) and $\\hat{B} = 180^\\circ - \\hat{C}$ (co-int $\\angle$s, $AB \\parallel DC$).",
            "3_breakdown": f"$\\hat{{C}} = {ang_c}^\\circ \\implies \\hat{{B}} = 180^\\circ - {ang_c}^\\circ = {ang_b}^\\circ$.",
        },
        misconception_tags=["omitted_parallel_line_reason", "co_interior_angles_error"],
        keywords=["circle geometry", "cyclic quad", "parallel lines"],
        term=3,
        caps_weight_percent=35,
        suggested_duration_mins=4,
        mode="elementary_28_cyclic_quad_with_parallel_sides",
        difficulty=difficulty,
    )

# 29. Exterior Angle of a Cyclic Quadrilateral
def arch_29_cyclic_quad_exterior_angle_basic(r: random.Random, difficulty: str = "easy") -> Dict[str, Any]:
    ang_a = r.randint(68, 126)

    pts = {
        "A": _pt_on_circle(145),
        "B": _pt_on_circle(55),
        "C": _pt_on_circle(330),
        "D": _pt_on_circle(220),
        "E": (355.0, 62.0),
    }

    prompt = (
        f"In cyclic quadrilateral $ABCD$, side $BC$ is produced to point $E$. "
        f"If the interior opposite angle $\\hat{{A}} = {ang_a}^\\circ$, determine the size of the exterior angle "
        f"$D\\hat{{C}}E$ and state the geometric reason."
    )

    diag = circle_geo_svg(
        title=f"Exterior Angle of Cyclic Quad: ∠A = {ang_a}° — Find ∠DCE",
        points=pts,
        segments=[("A", "B"), ("B", "C"), ("C", "D"), ("D", "A"), ("C", "E")],
        show_center=False,
        callouts=[(162, 198, f"∠A={ang_a}°", "#1d4ed8"), (310, 95, "∠DCE=?", "#dc2626")],
    )

    steps = [
        step(from_latex=rf"\hat{{A}} = {ang_a}^\circ", to_latex_str=rf"D\hat{{C}}E = \hat{{A}} = {ang_a}^\circ \quad (\text{{ext }}\angle\text{{ of cyclic quad}})", op="apply exterior angle of cyclic quadrilateral theorem", rule="exterior angle of cyclic quadrilateral",),
    ]
    canonical = solution_graph(goal="find exterior angle DCE", steps=steps, final_latex=rf"{ang_a}^\circ")

    return make_math_question(
        prefix="g11_cg_29",
        topic=TOPIC_NAME,
        subskill="29_cyclic_quad_exterior_angle_basic",
        learning_objective_id=f"{LEARNING_OBJECTIVE_ID}_29",
        prompt=prompt,
        prompt_latex=prompt,
        answer_latex=rf"{ang_a}^\circ",
        answer_sympy=str(ang_a),
        sample_answer=rf"D\hat{{C}}E = \hat{{A}} = {ang_a}^\circ \quad (\text{{ext }}\angle\text{{ of cyclic quad}})",
        canonical_solution=canonical,
        diagram_spec=diag,
        marking_schema={
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": f"Angle DCE = {ang_a} deg", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Reason: ext angle of cyclic quad", "marks": 1, "editable": True},
            ],
        },
        hints={
            "1_nudge": "Recall the relationship between the exterior angle of a cyclic quad and its interior opposite angle.",
            "2_concept": "$D\\hat{C}E = \\hat{A}$ (ext $\\angle$ of cyclic quad).",
            "3_breakdown": f"$D\\hat{{C}}E = {ang_a}^\\circ$ (ext $\\angle$ of cyclic quad).",
        },
        misconception_tags=["subtracted_from_180_instead_of_equating_exterior", "omitted_geometric_reason"],
        keywords=["circle geometry", "exterior angle of cyclic quad"],
        term=3,
        caps_weight_percent=35,
        suggested_duration_mins=2,
        mode="elementary_29_cyclic_quad_exterior_angle_basic",
        difficulty=difficulty,
    )

# 30. Algebraic Exterior Angle of a Cyclic Quadrilateral
def arch_30_cyclic_quad_exterior_angle_algebraic(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    x_val = r.randint(18, 36)
    a_val = r.randint(5, 22)
    ext_val = 3 * x_val - a_val
    b_val = ext_val - 2 * x_val

    pts = {
        "A": _pt_on_circle(145),
        "B": _pt_on_circle(55),
        "C": _pt_on_circle(330),
        "D": _pt_on_circle(220),
        "E": (355.0, 62.0),
    }

    prompt = (
        f"In cyclic quadrilateral $ABCD$, side $BC$ is produced to $E$. "
        f"If $\\hat{{A}} = (2x + {b_val}^\\circ)$ and exterior angle $D\\hat{{C}}E = (3x - {a_val}^\\circ)$, "
        f"solve for $x$ and state the geometric reason."
    )

    diag = circle_geo_svg(
        title=f"Algebraic Exterior Angle: ∠A = 2x + {b_val}°, ∠DCE = 3x - {a_val}°",
        points=pts,
        segments=[("A", "B"), ("B", "C"), ("C", "D"), ("D", "A"), ("C", "E")],
        show_center=False,
        callouts=[(162, 198, f"2x+{b_val}°", "#1d4ed8"), (318, 95, f"3x-{a_val}°", "#dc2626")],
    )

    steps = [
        step(from_latex=r"D\hat{C}E = \hat{A}", to_latex_str=rf"3x - {a_val}^\circ = 2x + {b_val}^\circ \quad (\text{{ext }}\angle\text{{ of cyclic quad}})", op="equate exterior angle to interior opposite angle", rule="exterior angle of cyclic quadrilateral",),
        step(from_latex=rf"3x - 2x = {b_val}^\circ + {a_val}^\circ", to_latex_str=rf"x = {x_val}^\circ", op="solve linear equation for x", rule="linear equation",),
    ]
    canonical = solution_graph(goal="solve for x using exterior angle of cyclic quad", steps=steps, final_latex=rf"{x_val}^\circ")

    return make_math_question(
        prefix="g11_cg_30",
        topic=TOPIC_NAME,
        subskill="30_cyclic_quad_exterior_angle_algebraic",
        learning_objective_id=f"{LEARNING_OBJECTIVE_ID}_30",
        prompt=prompt,
        prompt_latex=prompt,
        answer_latex=rf"{x_val}^\circ",
        answer_sympy=str(x_val),
        sample_answer=rf"3x - {a_val}^\circ = 2x + {b_val}^\circ \implies x = {x_val}^\circ \quad (\text{{ext }}\angle\text{{ of cyclic quad}})",
        canonical_solution=canonical,
        diagram_spec=diag,
        marking_schema={
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": f"Equate 3x - {a_val} = 2x + {b_val}", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Reason: ext angle of cyclic quad", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"x = {x_val} deg", "marks": 1, "editable": True},
            ],
        },
        hints={
            "1_nudge": "Equate the exterior angle $D\\hat{C}E$ to the interior opposite angle $\\hat{A}$.",
            "2_concept": "$3x - {a_val}^\\circ = 2x + {b_val}^\\circ$ (ext $\\angle$ of cyclic quad).",
            "3_breakdown": f"$x = {b_val}^\\circ + {a_val}^\\circ = {x_val}^\\circ$.",
        },
        misconception_tags=["added_exterior_and_interior_opposite_to_180", "omitted_geometric_reason"],
        keywords=["circle geometry", "exterior angle of cyclic quad", "algebraic"],
        term=3,
        caps_weight_percent=35,
        suggested_duration_mins=3,
        mode="elementary_30_cyclic_quad_exterior_angle_algebraic",
        difficulty=difficulty,
    )

# 31. Combined Angle at Centre & Opposite Angle of Cyclic Quad
def arch_31_cyclic_quad_combined_centre_and_opposite(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    ang_b = r.randint(48, 76)
    ang_o = 2 * ang_b
    ang_d = 180 - ang_b

    pts = {
        "O": (210.0, 155.0),
        "A": _pt_on_circle(150),
        "C": _pt_on_circle(30),
        "B": _pt_on_circle(270),
        "D": _pt_on_circle(90),
    }

    prompt = (
        f"In the circle with centre $O$, points $A, B, C,$ and $D$ lie on the circumference. "
        f"Radii $OA$ and $OC$ are drawn such that $A\\hat{{O}}C = {ang_o}^\\circ$. "
        f"Calculate the size of obtuse angle $A\\hat{{D}}C$, giving all geometric reasons."
    )

    diag = circle_geo_svg(
        title=f"Centre & Cyclic Quad ABCD: ∠AOC = {ang_o}° — Find ∠ADC",
        points=pts,
        segments=[("O", "A"), ("O", "C"), ("A", "B"), ("B", "C"), ("C", "D"), ("D", "A")],
        callouts=[(210, 140, f"∠O={ang_o}°", "#dc2626"), (210, 225, "∠D=?", "#1d4ed8")],
    )

    steps = [
        step(from_latex=rf"A\hat{{O}}C = {ang_o}^\circ", to_latex_str=rf"\hat{{B}} = \frac{{1}}{{2}}({ang_o}^\circ) = {ang_b}^\circ \quad (\angle \text{{ at centre }} = 2\times\angle \text{{ at circ}})", op="find angle B at the circumference", rule="angle at centre = 2 x angle at circumference",),
        step(from_latex=rf"\hat{{B}} = {ang_b}^\circ", to_latex_str=rf"\hat{{D}} = 180^\circ - {ang_b}^\circ = {ang_d}^\circ \quad (\text{{opp }}\angle\text{{s of cyclic quad}})", op="find opposite angle D of cyclic quad ABCD", rule="opposite angles of cyclic quadrilateral",),
    ]
    canonical = solution_graph(goal="find angle ADC using angle at centre and cyclic quad", steps=steps, final_latex=rf"{ang_d}^\circ")

    return make_math_question(
        prefix="g11_cg_31",
        topic=TOPIC_NAME,
        subskill="31_cyclic_quad_combined_centre_and_opposite",
        learning_objective_id=f"{LEARNING_OBJECTIVE_ID}_31",
        prompt=prompt,
        prompt_latex=prompt,
        answer_latex=rf"{ang_d}^\circ",
        answer_sympy=str(ang_d),
        sample_answer=rf"\hat{{B}} = {ang_b}^\circ \text{{ (}}\angle\text{{ at centre }} = 2\angle\text{{ at circ)}}; \; \hat{{D}} = 180^\circ - {ang_b}^\circ = {ang_d}^\circ \text{{ (opp }}\angle\text{{s of cyclic quad)}}",
        canonical_solution=canonical,
        diagram_spec=diag,
        marking_schema={
            "total_marks": 4,
            "marking_points": [
                {"id": "mp1", "desc": f"Angle B = {ang_b} deg", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Reason: angle at centre = 2 x angle at circ", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Angle D = {ang_d} deg", "marks": 1, "editable": True},
                {"id": "mp4", "desc": "Reason: opp angles of cyclic quad", "marks": 1, "editable": True},
            ],
        },
        hints={
            "1_nudge": "Do NOT treat $OADC$ as a cyclic quadrilateral ($O$ is at the centre, not on the circumference)! First find $\\hat{B}$.",
            "2_concept": "$\\hat{B} = \\frac{1}{2}A\\hat{O}C$ ($\\angle$ at centre $= 2\\angle$ at circ), then $\\hat{D} = 180^\\circ - \\hat{B}$ (opp $\\angle$s of cyclic quad $ABCD$).",
            "3_breakdown": f"$\\hat{{B}} = {ang_b}^\\circ \\implies \\hat{{D}} = 180^\\circ - {ang_b}^\\circ = {ang_d}^\\circ$.",
        },
        misconception_tags=["treated_o_as_circumference_vertex", "omitted_geometric_reason"],
        keywords=["circle geometry", "cyclic quad", "angle at centre"],
        term=3,
        caps_weight_percent=35,
        suggested_duration_mins=4,
        mode="elementary_31_cyclic_quad_combined_centre_and_opposite",
        difficulty=difficulty,
    )

# 32. Converse of Cyclic Quad: Prove Quad is Cyclic (Opposite Angles Sum to 180°)
def arch_32_converse_cyclic_quad_opp_angles_supplementary(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    ang_a = r.randint(72, 118)
    ang_c = 180 - ang_a
    sum_ac = 180

    pts = {
        "A": _pt_on_circle(140),
        "B": _pt_on_circle(55),
        "C": _pt_on_circle(325),
        "D": _pt_on_circle(220),
    }

    prompt = (
        f"In quadrilateral $ABCD$, $\\hat{{A}} = {ang_a}^\\circ$ and $\\hat{{C}} = {ang_c}^\\circ$. "
        f"Calculate $\\hat{{A}} + \\hat{{C}}$ and state the converse geometric reason that proves "
        f"$ABCD$ is a cyclic quadrilateral."
    )

    diag = circle_geo_svg(
        title=f"Prove ABCD is Cyclic: ∠A = {ang_a}°, ∠C = {ang_c}°",
        points=pts,
        segments=[("A", "B"), ("B", "C"), ("C", "D"), ("D", "A")],
        show_center=False,
        callouts=[(162, 198, f"∠A={ang_a}°", "#1d4ed8"), (260, 118, f"∠C={ang_c}°", "#dc2626"), (210, 290, "Prove ABCD is cyclic", "#0f172a")],
    )

    steps = [
        step(from_latex=rf"\hat{{A}} = {ang_a}^\circ, \; \hat{{C}} = {ang_c}^\circ", to_latex_str=rf"\hat{{A}} + \hat{{C}} = {ang_a}^\circ + {ang_c}^\circ = 180^\circ", op="sum opposite angles A and C", rule="addition",),
        step(from_latex=r"\hat{A} + \hat{C} = 180^\circ", to_latex_str=r"ABCD \text{ is a cyclic quad} \quad (\text{opp }\angle\text{s quad sup / converse opp }\angle\text{s of cyclic quad})", op="conclude ABCD is cyclic by converse theorem", rule="converse opposite angles of cyclic quad",),
    ]
    canonical = solution_graph(goal="prove ABCD is cyclic", steps=steps, final_latex=r"180^\circ")

    return make_math_question(
        prefix="g11_cg_32",
        topic=TOPIC_NAME,
        subskill="32_converse_cyclic_quad_opp_angles_supplementary",
        learning_objective_id=f"{LEARNING_OBJECTIVE_ID}_32",
        prompt=prompt,
        prompt_latex=prompt,
        answer_latex=r"180^\circ",
        answer_sympy=str(sum_ac),
        sample_answer=rf"\hat{{A}} + \hat{{C}} = {ang_a}^\circ + {ang_c}^\circ = 180^\circ \implies ABCD \text{{ is cyclic (opp }}\angle\text{{s quad sup)}}",
        canonical_solution=canonical,
        diagram_spec=diag,
        marking_schema={
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": f"Show A + C = {ang_a} + {ang_c} = 180 deg", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Converse reason: opp angles quad sup / converse opp angles of cyclic quad", "marks": 1, "editable": True},
            ],
        },
        hints={
            "1_nudge": "Add the two opposite interior angles $\\hat{A}$ and $\\hat{C}$.",
            "2_concept": "If the opposite angles of a quadrilateral are supplementary ($180^\\circ$), the quadrilateral is cyclic (opp $\\angle$s quad sup).",
            "3_breakdown": f"$\\hat{{A}} + \\hat{{C}} = {ang_a}^\\circ + {ang_c}^\\circ = 180^\\circ$ (opp $\\angle$s quad sup).",
        },
        misconception_tags=["used_forward_reason_instead_of_converse", "omitted_geometric_reason"],
        keywords=["circle geometry", "converse cyclic quad", "supplementary opposite angles"],
        term=3,
        caps_weight_percent=35,
        suggested_duration_mins=3,
        mode="elementary_32_converse_cyclic_quad_opp_angles_supplementary",
        difficulty=difficulty,
    )

# 33. Converse of Cyclic Quad: Exterior Angle = Interior Opposite Angle
def arch_33_converse_cyclic_quad_exterior_equals_interior(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    ang_b = r.randint(45, 72)
    ang_f = r.randint(35, 55)
    ang_a = ang_b + ang_f

    pts = {
        "A": _pt_on_circle(145),
        "B": _pt_on_circle(55),
        "C": _pt_on_circle(330),
        "D": _pt_on_circle(220),
        "E": (355.0, 62.0),
    }

    prompt = (
        f"In quadrilateral $ABCD$, side $BC$ is produced to $E$. In an adjacent triangle, it is found that "
        f"$D\\hat{{C}}E = {ang_b}^\\circ + {ang_f}^\\circ = {ang_a}^\\circ$, while interior opposite angle $\\hat{{A}} = {ang_a}^\\circ$. "
        f"State the value of $D\\hat{{C}}E$ and the converse geometric reason proving $ABCD$ is a cyclic quadrilateral."
    )

    diag = circle_geo_svg(
        title=f"Prove Concyclic via Exterior Angle: ∠A = ∠DCE = {ang_a}°",
        points=pts,
        segments=[("A", "B"), ("B", "C"), ("C", "D"), ("D", "A"), ("C", "E")],
        show_center=False,
        callouts=[(162, 198, f"∠A={ang_a}°", "#1d4ed8"), (312, 95, f"∠DCE={ang_a}°", "#dc2626")],
    )

    steps = [
        step(from_latex=rf"D\hat{{C}}E = {ang_a}^\circ \quad \text{{and}} \quad \hat{{A}} = {ang_a}^\circ", to_latex_str=r"D\hat{C}E = \hat{A} \implies ABCD \text{ is cyclic} \quad (\text{ext }\angle\text{ of quad } = \text{ int opp }\angle)", op="apply converse of exterior angle of cyclic quad", rule="converse exterior angle of cyclic quad",),
    ]
    canonical = solution_graph(goal="prove ABCD is cyclic using exterior angle converse", steps=steps, final_latex=rf"{ang_a}^\circ")

    return make_math_question(
        prefix="g11_cg_33",
        topic=TOPIC_NAME,
        subskill="33_converse_cyclic_quad_exterior_equals_interior",
        learning_objective_id=f"{LEARNING_OBJECTIVE_ID}_33",
        prompt=prompt,
        prompt_latex=prompt,
        answer_latex=rf"{ang_a}^\circ",
        answer_sympy=str(ang_a),
        sample_answer=rf"D\hat{{C}}E = \hat{{A}} = {ang_a}^\circ \implies ABCD \text{{ is cyclic (ext }}\angle\text{{ of quad }} = \text{{ int opp }}\angle\text{{)}}",
        canonical_solution=canonical,
        diagram_spec=diag,
        marking_schema={
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": f"Show DCE = A = {ang_a} deg", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Converse reason: ext angle of quad = int opp angle", "marks": 1, "editable": True},
            ],
        },
        hints={
            "1_nudge": "Compare exterior angle $D\\hat{C}E$ with interior opposite angle $\\hat{A}$.",
            "2_concept": "If the exterior angle of a quadrilateral equals the interior opposite angle, the quadrilateral is cyclic (ext $\\angle$ of quad $=$ int opp $\\angle$).",
            "3_breakdown": f"$D\\hat{{C}}E = \\hat{{A}} = {ang_a}^\\circ$, so $ABCD$ is cyclic (ext $\\angle$ of quad $=$ int opp $\\angle$).",
        },
        misconception_tags=["used_forward_reason_instead_of_converse", "omitted_geometric_reason"],
        keywords=["circle geometry", "converse exterior angle cyclic quad"],
        term=3,
        caps_weight_percent=35,
        suggested_duration_mins=3,
        mode="elementary_33_converse_cyclic_quad_exterior_equals_interior",
        difficulty=difficulty,
    )

# 34. Converse of Same Segment: Line Subtends Equal Angles on Same Side
def arch_34_converse_cyclic_quad_line_subtends_equal_angles(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    ang_val = r.randint(32, 68)

    pts = {
        "A": _pt_on_circle(145),
        "B": _pt_on_circle(35),
        "C": _pt_on_circle(235),
        "D": _pt_on_circle(305),
    }

    prompt = (
        f"Points $C$ and $D$ lie on the same side of line segment $AB$. "
        f"In $\\triangle ABC$ and $\\triangle ABD$, it is given that $A\\hat{{C}}B = {ang_val}^\\circ$ "
        f"and $A\\hat{{D}}B = {ang_val}^\\circ$. State the size of the equal subtended angles and the "
        f"converse geometric reason proving that $A, B, D, C$ are concyclic."
    )

    diag = circle_geo_svg(
        title=f"Prove Concyclic Points: AB Subtends ∠C = ∠D = {ang_val}°",
        points=pts,
        segments=[("A", "B"), ("A", "C"), ("B", "C"), ("A", "D"), ("B", "D")],
        show_center=False,
        callouts=[(160, 108, f"∠C={ang_val}°", "#1d4ed8"), (260, 108, f"∠D={ang_val}°", "#dc2626")],
    )

    steps = [
        step(from_latex=rf"A\hat{{C}}B = A\hat{{D}}B = {ang_val}^\circ", to_latex_str=r"ABDC \text{ is a cyclic quad} \quad (\text{line subtends equal }\angle\text{s / converse }\angle\text{s in same seg})", op="apply converse of angles in the same segment", rule="line subtends equal angles on the same side",),
    ]
    canonical = solution_graph(goal="prove points are concyclic using equal subtended angles", steps=steps, final_latex=rf"{ang_val}^\circ")

    return make_math_question(
        prefix="g11_cg_34",
        topic=TOPIC_NAME,
        subskill="34_converse_cyclic_quad_line_subtends_equal_angles",
        learning_objective_id=f"{LEARNING_OBJECTIVE_ID}_34",
        prompt=prompt,
        prompt_latex=prompt,
        answer_latex=rf"{ang_val}^\circ",
        answer_sympy=str(ang_val),
        sample_answer=rf"A\hat{{C}}B = A\hat{{D}}B = {ang_val}^\circ \implies A, B, D, C \text{{ are concyclic (line subtends equal }}\angle\text{{s)}}",
        canonical_solution=canonical,
        diagram_spec=diag,
        marking_schema={
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": f"Identify ACB = ADB = {ang_val} deg subtended by AB", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Converse reason: line subtends equal angles / converse angles in same seg", "marks": 1, "editable": True},
            ],
        },
        hints={
            "1_nudge": "Notice that segment $AB$ subtends equal angles at $C$ and $D$ on the same side of $AB$.",
            "2_concept": "If a line segment subtends equal angles at two points on the same side of it, the four points are concyclic (line subtends equal $\\angle$s).",
            "3_breakdown": f"$A\\hat{{C}}B = A\\hat{{D}}B = {ang_val}^\\circ$, so $ABDC$ is cyclic (line subtends equal $\\angle$s).",
        },
        misconception_tags=["used_forward_reason_instead_of_converse", "omitted_geometric_reason"],
        keywords=["circle geometry", "concyclic points", "line subtends equal angles"],
        term=3,
        caps_weight_percent=35,
        suggested_duration_mins=3,
        mode="elementary_34_converse_cyclic_quad_line_subtends_equal_angles",
        difficulty=difficulty,
    )

# 35. Tangent Perpendicular to Radius (Angle Calculation)
def arch_35_tangent_perp_radius_basic(r: random.Random, difficulty: str = "easy") -> Dict[str, Any]:
    ang_pot = r.randint(24, 68)
    ang_opt = 90 - ang_pot

    pts = {
        "O": (210.0, 155.0),
        "T": (210.0, 247.0),
        "P": (95.0, 247.0),
        "Q": (325.0, 247.0),
    }

    prompt = (
        f"Line $PQ$ is a tangent to the circle with centre $O$ at point $T$. "
        f"Radius $OT$ and secant line $OP$ are drawn. If $P\\hat{{O}}T = {ang_pot}^\\circ$, "
        f"calculate the size of $O\\hat{{P}}T$, giving complete geometric reasons."
    )

    diag = circle_geo_svg(
        title=f"Tangent PQ ⊥ Radius OT at T: ∠POT = {ang_pot}° — Find ∠OPT",
        points=pts,
        segments=[("P", "Q"), ("O", "T"), ("O", "P")],
        right_angle_at=pts["T"],
        callouts=[(192, 185, f"∠O={ang_pot}°", "#dc2626"), (135, 238, "∠P=?", "#1d4ed8")],
    )

    steps = [
        step(from_latex=r"\text{Tangent } PQ \text{ and radius } OT", to_latex_str=r"O\hat{T}P = 90^\circ \quad (\tan \perp \text{rad})", op="apply tangent perpendicular to radius theorem", rule="tangent perpendicular to radius",),
        step(from_latex=rf"O\hat{{P}}T + {ang_pot}^\circ + 90^\circ = 180^\circ", to_latex_str=rf"O\hat{{P}}T = 90^\circ - {ang_pot}^\circ = {ang_opt}^\circ \quad (\text{{sum of }}\angle\text{{s in }}\triangle)", op="calculate angle OPT in right-angled triangle OTP", rule="sum of angles in triangle",),
    ]
    canonical = solution_graph(goal="find angle OPT using tan perp rad", steps=steps, final_latex=rf"{ang_opt}^\circ")

    return make_math_question(
        prefix="g11_cg_35",
        topic=TOPIC_NAME,
        subskill="35_tangent_perp_radius_basic",
        learning_objective_id=f"{LEARNING_OBJECTIVE_ID}_35",
        prompt=prompt,
        prompt_latex=prompt,
        answer_latex=rf"{ang_opt}^\circ",
        answer_sympy=str(ang_opt),
        sample_answer=rf"O\hat{{T}}P = 90^\circ \text{{ (}}\tan\perp\text{{rad)}}; \; O\hat{{P}}T = 90^\circ - {ang_pot}^\circ = {ang_opt}^\circ \text{{ (sum of }}\angle\text{{s in }}\triangle\text{{)}}",
        canonical_solution=canonical,
        diagram_spec=diag,
        marking_schema={
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": "Angle OTP = 90 deg", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Reason: tan perp rad", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Angle OPT = {ang_opt} deg", "marks": 1, "editable": True},
            ],
        },
        hints={
            "1_nudge": "What angle does a radius make with a tangent at the point of contact?",
            "2_concept": "$O\\hat{T}P = 90^\\circ$ ($\\tan \\perp \\text{rad}$), then use the sum of angles in $\\triangle OTP$.",
            "3_breakdown": f"$O\\hat{{P}}T = 180^\\circ - 90^\\circ - {ang_pot}^\\circ = {ang_opt}^\\circ$.",
        },
        misconception_tags=["tangent_radius_perpendicular_miss", "omitted_geometric_reason"],
        keywords=["circle geometry", "tangent perpendicular to radius"],
        term=3,
        caps_weight_percent=35,
        suggested_duration_mins=3,
        mode="elementary_35_tangent_perp_radius_basic",
        difficulty=difficulty,
    )

# 36. Tangent Perpendicular to Radius + Pythagoras Length Calculation
def arch_36_tangent_perp_radius_pythagoras_length(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    triples = [(3, 4, 5), (5, 12, 13), (6, 8, 10), (8, 15, 17), (9, 12, 15), (7, 24, 25)]
    rad_len, tan_len, op_hyp = r.choice(triples)
    scale = r.choice([1, 2])
    rad_len *= scale
    tan_len *= scale
    op_hyp *= scale

    pts = {
        "O": (210.0, 155.0),
        "T": (210.0, 247.0),
        "P": (95.0, 247.0),
    }

    prompt = (
        f"From an external point $P$, a tangent $PT$ of length ${tan_len}\\text{{ cm}}$ is drawn to a circle "
        f"with centre $O$ and radius $OT = {rad_len}\\text{{ cm}}$. "
        f"Calculate the distance $OP$ from the centre of the circle to point $P$, stating all geometric reasons."
    )

    diag = circle_geo_svg(
        title=f"Tangent & Pythagoras: OT = {rad_len} cm, PT = {tan_len} cm — Find OP",
        points=pts,
        segments=[("P", "T"), ("O", "T"), ("O", "P")],
        right_angle_at=pts["T"],
        callouts=[(232, 205, f"OT={rad_len}", "#dc2626"), (155, 265, f"PT={tan_len}", "#1d4ed8"), (140, 195, "OP=?", "#0f172a")],
    )

    steps = [
        step(from_latex=r"OT \perp PT", to_latex_str=r"O\hat{T}P = 90^\circ \quad (\tan \perp \text{rad})", op="identify right angle between radius and tangent", rule="tangent perpendicular to radius",),
        step(from_latex=r"OP^2 = OT^2 + PT^2", to_latex_str=rf"OP = \sqrt{{{rad_len}^2 + {tan_len}^2}} = {op_hyp}\text{{ cm}} \quad (\text{{Pythagoras}})", op="calculate hypotenuse OP using Pythagoras", rule="Pythagoras",),
    ]
    canonical = solution_graph(goal="find distance OP using tan perp rad and Pythagoras", steps=steps, final_latex=rf"{op_hyp}\text{{ cm}}")

    return make_math_question(
        prefix="g11_cg_36",
        topic=TOPIC_NAME,
        subskill="36_tangent_perp_radius_pythagoras_length",
        learning_objective_id=f"{LEARNING_OBJECTIVE_ID}_36",
        prompt=prompt,
        prompt_latex=prompt,
        answer_latex=rf"{op_hyp}\text{{ cm}}",
        answer_sympy=str(op_hyp),
        sample_answer=rf"O\hat{{T}}P = 90^\circ \text{{ (}}\tan\perp\text{{rad)}}; \; OP = \sqrt{{{rad_len}^2 + {tan_len}^2}} = {op_hyp}\text{{ cm (Pythagoras)}}",
        canonical_solution=canonical,
        diagram_spec=diag,
        marking_schema={
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": "Angle OTP = 90 deg (tan perp rad)", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Pythagoras substitution OP^2 = {rad_len}^2 + {tan_len}^2", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"OP = {op_hyp} cm", "marks": 1, "editable": True},
            ],
        },
        hints={
            "1_nudge": "Since $OT \\perp PT$ ($\\tan \\perp \\text{rad}$), which side of right-angled $\\triangle OTP$ is the hypotenuse?",
            "2_concept": "$OP$ is opposite the $90^\\circ$ angle at $T$, so $OP^2 = OT^2 + PT^2$ (Pythagoras).",
            "3_breakdown": f"$OP = \\sqrt{{{rad_len}^2 + {tan_len}^2}} = {op_hyp}\\text{{ cm}}$.",
        },
        misconception_tags=["treated_tangent_as_hypotenuse", "omitted_geometric_reason"],
        keywords=["circle geometry", "tangent", "radius", "Pythagoras"],
        term=3,
        caps_weight_percent=35,
        suggested_duration_mins=3,
        mode="elementary_36_tangent_perp_radius_pythagoras_length",
        difficulty=difficulty,
    )

# 37. Two Tangents from a Common External Point (Isosceles Triangle PAB)
def arch_37_two_tangents_from_common_point_isosceles(r: random.Random, difficulty: str = "easy") -> Dict[str, Any]:
    ang_pab = r.randint(48, 76)
    ang_p = 180 - 2 * ang_pab

    pts = {
        "O": (175.0, 155.0),
        "A": (175.0 + 92 * math.cos(math.radians(-55)), 155.0 + 92 * math.sin(math.radians(-55))),
        "B": (175.0 + 92 * math.cos(math.radians(55)), 155.0 + 92 * math.sin(math.radians(55))),
        "P": (355.0, 155.0),
    }
    pts["A"] = (round(pts["A"][0], 1), round(pts["A"][1], 1))
    pts["B"] = (round(pts["B"][0], 1), round(pts["B"][1], 1))

    prompt = (
        f"Tangents $PA$ and $PB$ are drawn from an external point $P$ to touch the circle at $A$ and $B$ respectively. "
        f"Chord $AB$ is drawn. If $\\hat{{P}} = {ang_p}^\\circ$, calculate the size of $P\\hat{{A}}B$, "
        f"stating all geometric reasons."
    )

    diag = circle_geo_svg(
        title=f"Two Tangents from Common Point P: ∠P = {ang_p}° — Find ∠PAB",
        points=pts,
        segments=[("P", "A"), ("P", "B"), ("A", "B")],
        show_center=False,
        callouts=[(315, 158, f"∠P={ang_p}°", "#dc2626"), (210, 290, "PA and PB are tangents — Find ∠PAB", "#1d4ed8")],
    )

    steps = [
        step(from_latex=r"\text{Tangents } PA \text{ and } PB \text{ from } P", to_latex_str=r"PA = PB \quad (\text{tans from same pt})", op="apply equal tangents theorem", rule="tangents from a common point are equal",),
        step(from_latex=rf"P\hat{{A}}B = P\hat{{B}}A \quad (\angle\text{{s opp equal sides}})", to_latex_str=rf"P\hat{{A}}B = \frac{{180^\circ - {ang_p}^\circ}}{{2}} = {ang_pab}^\circ \quad (\text{{sum of }}\angle\text{{s in }}\triangle)", op="calculate base angle PAB of isosceles triangle PAB", rule="angles opposite equal sides and triangle sum",),
    ]
    canonical = solution_graph(goal="find angle PAB using equal tangents", steps=steps, final_latex=rf"{ang_pab}^\circ")

    return make_math_question(
        prefix="g11_cg_37",
        topic=TOPIC_NAME,
        subskill="37_two_tangents_from_common_point_isosceles",
        learning_objective_id=f"{LEARNING_OBJECTIVE_ID}_37",
        prompt=prompt,
        prompt_latex=prompt,
        answer_latex=rf"{ang_pab}^\circ",
        answer_sympy=str(ang_pab),
        sample_answer=rf"PA = PB \text{{ (tans from same pt)}} \implies P\hat{{A}}B = \frac{{180^\circ - {ang_p}^\circ}}{{2}} = {ang_pab}^\circ \text{{ (}}\angle\text{{s opp equal sides)}}",
        canonical_solution=canonical,
        diagram_spec=diag,
        marking_schema={
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": "PA = PB (tans from same pt)", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Angle PAB = Angle PBA (angles opp equal sides)", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Angle PAB = {ang_pab} deg", "marks": 1, "editable": True},
            ],
        },
        hints={
            "1_nudge": "What do you know about the lengths of two tangents drawn to a circle from the same external point $P$?",
            "2_concept": "$PA = PB$ (tans from same pt), making $\\triangle PAB$ isosceles with $P\\hat{A}B = P\\hat{B}A$.",
            "3_breakdown": f"$P\\hat{{A}}B = \\frac{{180^\\circ - {ang_p}^\\circ}}{{2}} = {ang_pab}^\\circ$.",
        },
        misconception_tags=["omitted_geometric_reason", "failed_to_identify_equal_tangents"],
        keywords=["circle geometry", "tangents from common point", "isosceles triangle"],
        term=3,
        caps_weight_percent=35,
        suggested_duration_mins=3,
        mode="elementary_37_two_tangents_from_common_point_isosceles",
        difficulty=difficulty,
    )

# 38. Two Tangents & Two Radii Kite OAPB
def arch_38_two_tangents_and_centre_kite(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    ang_p = r.randint(36, 78)
    ang_aob = 180 - ang_p

    pts = {
        "O": (210.0, 155.0),
        "A": _pt_on_circle(-50),
        "B": _pt_on_circle(50),
        "P": (375.0, 155.0),
    }

    prompt = (
        f"Tangents $PA$ and $PB$ are drawn from external point $P$ to a circle with centre $O$, touching "
        f"the circle at $A$ and $B$. Radii $OA$ and $OB$ are drawn. If $A\\hat{{P}}B = {ang_p}^\\circ$, "
        f"calculate the size of $A\\hat{{O}}B$, giving all geometric reasons."
    )

    diag = circle_geo_svg(
        title=f"Tangent-Radius Kite OAPB: ∠APB = {ang_p}° — Find ∠AOB",
        points=pts,
        segments=[("O", "A"), ("O", "B"), ("P", "A"), ("P", "B")],
        callouts=[(332, 158, f"∠P={ang_p}°", "#1d4ed8"), (175, 158, "∠AOB=?", "#dc2626")],
    )

    steps = [
        step(from_latex=r"\text{Radii } OA, OB \text{ and tangents } PA, PB", to_latex_str=r"O\hat{A}P = 90^\circ \text{ and } O\hat{B}P = 90^\circ \quad (\tan \perp \text{rad})", op="identify right angles at points of contact A and B", rule="tangent perpendicular to radius",),
        step(from_latex=rf"A\hat{{O}}B + 90^\circ + 90^\circ + {ang_p}^\circ = 360^\circ", to_latex_str=rf"A\hat{{O}}B = 180^\circ - {ang_p}^\circ = {ang_aob}^\circ \quad (\text{{sum of }}\angle\text{{s in quad}})", op="use interior angle sum of quadrilateral OAPB", rule="sum of angles in quadrilateral",),
    ]
    canonical = solution_graph(goal="find angle AOB in tangent-radius kite OAPB", steps=steps, final_latex=rf"{ang_aob}^\circ")

    return make_math_question(
        prefix="g11_cg_38",
        topic=TOPIC_NAME,
        subskill="38_two_tangents_and_centre_kite",
        learning_objective_id=f"{LEARNING_OBJECTIVE_ID}_38",
        prompt=prompt,
        prompt_latex=prompt,
        answer_latex=rf"{ang_aob}^\circ",
        answer_sympy=str(ang_aob),
        sample_answer=rf"O\hat{{A}}P = O\hat{{B}}P = 90^\circ \text{{ (}}\tan\perp\text{{rad)}}; \; A\hat{{O}}B = 180^\circ - {ang_p}^\circ = {ang_aob}^\circ \text{{ (sum of }}\angle\text{{s in quad)}}",
        canonical_solution=canonical,
        diagram_spec=diag,
        marking_schema={
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": "OAP = OBP = 90 deg (tan perp rad)", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Sum of angles in quad OAPB = 360 deg", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Angle AOB = {ang_aob} deg", "marks": 1, "editable": True},
            ],
        },
        hints={
            "1_nudge": "Find the angles $O\\hat{A}P$ and $O\\hat{B}P$ where the radii meet the tangents.",
            "2_concept": "$O\\hat{A}P = O\\hat{B}P = 90^\\circ$ ($\\tan \\perp \\text{rad}$), so in quadrilateral $OAPB$, $A\\hat{O}B + \\hat{P} = 180^\\circ$.",
            "3_breakdown": f"$A\\hat{{O}}B = 360^\\circ - (90^\\circ + 90^\\circ + {ang_p}^\\circ) = {ang_aob}^\\circ$.",
        },
        misconception_tags=["tangent_radius_perpendicular_miss", "omitted_geometric_reason"],
        keywords=["circle geometry", "tangent kite", "tangent perp radius"],
        term=3,
        caps_weight_percent=35,
        suggested_duration_mins=3,
        mode="elementary_38_two_tangents_and_centre_kite",
        difficulty=difficulty,
    )

# 39. Circumscribed Triangle — Equal Tangent Segments & Perimeter
def arch_39_two_tangents_perimeter_triangle(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    ad_len = r.randint(4, 11)
    be_len = r.randint(5, 13)
    cf_len = r.randint(6, 14)
    perim = 2 * (ad_len + be_len + cf_len)

    pts = {
        "O": (210.0, 155.0),
        "D": _pt_on_circle(210),
        "E": _pt_on_circle(90),
        "F": _pt_on_circle(330),
        "A": (210.0, 32.0),
        "B": (82.0, 247.0),
        "C": (338.0, 247.0),
    }

    prompt = (
        f"A circle is inscribed inside $\\triangle ABC$, touching side $AB$ at $D$, side $BC$ at $E$, "
        f"and side $AC$ at $F$. If $AD = {ad_len}\\text{{ cm}}$, $BE = {be_len}\\text{{ cm}}$, and "
        f"$CF = {cf_len}\\text{{ cm}}$, calculate the total perimeter of $\\triangle ABC$, stating your geometric reason."
    )

    diag = circle_geo_svg(
        title=f"Inscribed Circle Tangents: AD={ad_len}, BE={be_len}, CF={cf_len} cm",
        points=pts,
        segments=[("A", "B"), ("B", "C"), ("C", "A")],
        show_center=False,
        callouts=[(210, 292, f"AD={ad_len} cm, BE={be_len} cm, CF={cf_len} cm — Find Perimeter", "#1d4ed8")],
    )

    steps = [
        step(from_latex=rf"AD = {ad_len}, \; BE = {be_len}, \; CF = {cf_len}", to_latex_str=rf"AF = AD = {ad_len}, \; BD = BE = {be_len}, \; CE = CF = {cf_len} \quad (\text{{tans from same pt}})", op="equate tangent segments from each vertex A, B, and C", rule="tangents from a common point are equal",),
        step(from_latex=r"\text{Perimeter} = 2(AD + BE + CF)", to_latex_str=rf"\text{{Perimeter}} = 2({ad_len} + {be_len} + {cf_len}) = {perim}\text{{ cm}}", op="sum all six tangent segments", rule="perimeter of triangle",),
    ]
    canonical = solution_graph(goal="find perimeter of circumscribed triangle ABC", steps=steps, final_latex=rf"{perim}\text{{ cm}}")

    return make_math_question(
        prefix="g11_cg_39",
        topic=TOPIC_NAME,
        subskill="39_two_tangents_perimeter_triangle",
        learning_objective_id=f"{LEARNING_OBJECTIVE_ID}_39",
        prompt=prompt,
        prompt_latex=prompt,
        answer_latex=rf"{perim}\text{{ cm}}",
        answer_sympy=str(perim),
        sample_answer=rf"AF = {ad_len}, \; BD = {be_len}, \; CE = {cf_len} \text{{ (tans from same pt)}}; \; \text{{Perimeter}} = 2({ad_len}+{be_len}+{cf_len}) = {perim}\text{{ cm}}",
        canonical_solution=canonical,
        diagram_spec=diag,
        marking_schema={
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": f"AF = {ad_len}, BD = {be_len}, CE = {cf_len}", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Reason: tans from same pt", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Perimeter = {perim} cm", "marks": 1, "editable": True},
            ],
        },
        hints={
            "1_nudge": "From each vertex ($A$, $B$, and $C$), the two tangent segments to the points of contact are equal.",
            "2_concept": "$AF = AD$, $BD = BE$, and $CE = CF$ (tans from same pt).",
            "3_breakdown": f"$\\text{{Perimeter}} = 2({ad_len} + {be_len} + {cf_len}) = {perim}\\text{{ cm}}$.",
        },
        misconception_tags=["forgot_to_double_tangent_segments", "omitted_geometric_reason"],
        keywords=["circle geometry", "inscribed circle", "tangents from common point"],
        term=3,
        caps_weight_percent=35,
        suggested_duration_mins=3,
        mode="elementary_39_two_tangents_perimeter_triangle",
        difficulty=difficulty,
    )

# 40. Tangent-Chord Theorem (Basic Direct Application)
def arch_40_tan_chord_theorem_basic(r: random.Random, difficulty: str = "easy") -> Dict[str, Any]:
    ang_alt = r.randint(32, 74)

    pts = {
        "A": (210.0, 247.0),
        "P": (95.0, 247.0),
        "T": (325.0, 247.0),
        "B": _pt_on_circle(25),
        "C": _pt_on_circle(215),
    }

    prompt = (
        f"In the diagram, line $PT$ is a tangent to the circle at point $A$. "
        f"Chords $AB$, $BC$, and $AC$ are drawn. If $A\\hat{{C}}B = {ang_alt}^\\circ$, "
        f"determine the size of angle $T\\hat{{A}}B$ and state the geometric reason."
    )

    diag = circle_geo_svg(
        title=f"Tan-Chord Theorem: Tangent PT at A, ∠ACB = {ang_alt}° — Find ∠TAB",
        points=pts,
        segments=[("P", "T"), ("A", "B"), ("B", "C"), ("C", "A")],
        show_center=False,
        callouts=[(162, 115, f"∠C={ang_alt}°", "#1d4ed8"), (265, 238, "∠TAB=?", "#dc2626")],
    )

    steps = [
        step(from_latex=rf"A\hat{{C}}B = {ang_alt}^\circ", to_latex_str=rf"T\hat{{A}}B = A\hat{{C}}B = {ang_alt}^\circ \quad (\text{{tan chord theorem}})", op="apply tangent-chord theorem", rule="tan-chord theorem",),
    ]
    canonical = solution_graph(goal="find angle TAB using tan-chord theorem", steps=steps, final_latex=rf"{ang_alt}^\circ")

    return make_math_question(
        prefix="g11_cg_40",
        topic=TOPIC_NAME,
        subskill="40_tan_chord_theorem_basic",
        learning_objective_id=f"{LEARNING_OBJECTIVE_ID}_40",
        prompt=prompt,
        prompt_latex=prompt,
        answer_latex=rf"{ang_alt}^\circ",
        answer_sympy=str(ang_alt),
        sample_answer=rf"T\hat{{A}}B = A\hat{{C}}B = {ang_alt}^\circ \quad (\text{{tan chord theorem}})",
        canonical_solution=canonical,
        diagram_spec=diag,
        marking_schema={
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": f"Angle TAB = {ang_alt} deg", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Reason: tan chord theorem", "marks": 1, "editable": True},
            ],
        },
        hints={
            "1_nudge": "Look at the angle between tangent $AT$ and chord $AB$, and the angle subtended by chord $AB$ in the alternate segment.",
            "2_concept": "$T\\hat{A}B = A\\hat{C}B$ (tan chord theorem).",
            "3_breakdown": f"$T\\hat{{A}}B = {ang_alt}^\\circ$ (tan chord theorem).",
        },
        misconception_tags=["tangent_chord_error", "omitted_geometric_reason"],
        keywords=["circle geometry", "tan chord theorem", "alternate segment"],
        term=3,
        caps_weight_percent=35,
        suggested_duration_mins=2,
        mode="elementary_40_tan_chord_theorem_basic",
        difficulty=difficulty,
    )

# 41. Tan-Chord Theorem with Isosceles Inscribed Triangle (AB = AC)
def arch_41_tan_chord_with_isosceles_chord_triangle(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    ang_tab = r.randint(48, 74)
    ang_c = ang_tab
    ang_b = ang_c
    ang_bac = 180 - 2 * ang_c

    pts = {
        "A": (210.0, 247.0),
        "P": (95.0, 247.0),
        "T": (325.0, 247.0),
        "B": _pt_on_circle(25),
        "C": _pt_on_circle(215),
    }

    prompt = (
        f"Line $PT$ is a tangent to the circle at $A$. In inscribed $\\triangle ABC$, chord $AB =$ chord $AC$. "
        f"If $T\\hat{{A}}B = {ang_tab}^\\circ$, calculate the size of $B\\hat{{A}}C$, giving all geometric reasons."
    )

    diag = circle_geo_svg(
        title=f"Tan-Chord & Isosceles △ABC (AB = AC): ∠TAB = {ang_tab}°",
        points=pts,
        segments=[("P", "T"), ("A", "B"), ("B", "C"), ("C", "A")],
        show_center=False,
        callouts=[(265, 238, f"∠TAB={ang_tab}°", "#1d4ed8"), (210, 292, "AB = AC, Find ∠BAC", "#dc2626")],
    )

    steps = [
        step(from_latex=rf"T\hat{{A}}B = {ang_tab}^\circ", to_latex_str=rf"\hat{{C}} = T\hat{{A}}B = {ang_c}^\circ \quad (\text{{tan chord theorem}})", op="find angle C using tan-chord theorem", rule="tan-chord theorem",),
        step(from_latex=rf"AB = AC \implies \hat{{B}} = \hat{{C}} = {ang_b}^\circ \quad (\angle\text{{s opp equal sides}})", to_latex_str=rf"B\hat{{A}}C = 180^\circ - 2({ang_c}^\circ) = {ang_bac}^\circ \quad (\text{{sum of }}\angle\text{{s in }}\triangle)", op="calculate vertex angle BAC of isosceles triangle ABC", rule="angles opposite equal sides and triangle sum",),
    ]
    canonical = solution_graph(goal="find angle BAC using tan-chord and isosceles triangle", steps=steps, final_latex=rf"{ang_bac}^\circ")

    return make_math_question(
        prefix="g11_cg_41",
        topic=TOPIC_NAME,
        subskill="41_tan_chord_with_isosceles_chord_triangle",
        learning_objective_id=f"{LEARNING_OBJECTIVE_ID}_41",
        prompt=prompt,
        prompt_latex=prompt,
        answer_latex=rf"{ang_bac}^\circ",
        answer_sympy=str(ang_bac),
        sample_answer=rf"\hat{{C}} = {ang_c}^\circ \text{{ (tan chord theorem)}}; \; \hat{{B}} = {ang_b}^\circ \text{{ (}}\angle\text{{s opp equal sides)}}; \; B\hat{{A}}C = 180^\circ - 2({ang_c}^\circ) = {ang_bac}^\circ",
        canonical_solution=canonical,
        diagram_spec=diag,
        marking_schema={
            "total_marks": 4,
            "marking_points": [
                {"id": "mp1", "desc": f"Angle C = {ang_c} deg (tan chord theorem)", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Angle B = {ang_b} deg (angles opp equal sides)", "marks": 1, "editable": True},
                {"id": "mp3", "desc": "Sum of angles in triangle ABC = 180 deg", "marks": 1, "editable": True},
                {"id": "mp4", "desc": f"Angle BAC = {ang_bac} deg", "marks": 1, "editable": True},
            ],
        },
        hints={
            "1_nudge": "First find $\\hat{C}$ using the tan-chord theorem, then use $AB = AC$ in $\\triangle ABC$.",
            "2_concept": "$\\hat{C} = T\\hat{A}B = {ang_tab}^\\circ$ (tan chord theorem) and $\\hat{B} = \\hat{C}$ ($\\angle$s opp equal sides).",
            "3_breakdown": f"$B\\hat{{A}}C = 180^\\circ - 2({ang_tab}^\\circ) = {ang_bac}^\\circ$.",
        },
        misconception_tags=["tangent_chord_error", "omitted_geometric_reason"],
        keywords=["circle geometry", "tan chord theorem", "isosceles triangle"],
        term=3,
        caps_weight_percent=35,
        suggested_duration_mins=4,
        mode="elementary_41_tan_chord_with_isosceles_chord_triangle",
        difficulty=difficulty,
    )

# 42. Tangent Parallel to Chord (PT ∥ BC)
def arch_42_tan_chord_and_parallel_tangent(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    ang_tab = r.randint(46, 72)
    ang_b = ang_tab
    ang_c = ang_tab
    ang_bac = 180 - 2 * ang_tab

    pts = {
        "A": (210.0, 247.0),
        "P": (95.0, 247.0),
        "T": (325.0, 247.0),
        "B": _pt_on_circle(325),
        "C": _pt_on_circle(215),
    }

    prompt = (
        f"Line $PT$ is a tangent to the circle at $A$, and chord $BC$ is parallel to $PT$ ($PT \\parallel BC$). "
        f"If $T\\hat{{A}}B = {ang_tab}^\\circ$, calculate the size of $\\hat{{B}}$ and $\\hat{{C}}$ and hence determine $B\\hat{{A}}C$. "
        f"State all geometric reasons."
    )

    diag = circle_geo_svg(
        title=f"Tangent PT ∥ Chord BC: ∠TAB = {ang_tab}° — Find ∠BAC",
        points=pts,
        segments=[("P", "T"), ("A", "B"), ("B", "C"), ("C", "A")],
        show_center=False,
        callouts=[(265, 238, f"∠TAB={ang_tab}°", "#1d4ed8"), (210, 292, "PT ∥ BC — Find ∠BAC", "#dc2626")],
    )

    steps = [
        step(from_latex=rf"T\hat{{A}}B = {ang_tab}^\circ", to_latex_str=rf"\hat{{C}} = T\hat{{A}}B = {ang_c}^\circ \quad (\text{{tan chord theorem}})", op="find angle C using tan-chord theorem", rule="tan-chord theorem",),
        step(from_latex=rf"PT \parallel BC", to_latex_str=rf"\hat{{B}} = T\hat{{A}}B = {ang_b}^\circ \quad (\text{{alt }}\angle\text{{s, }} PT \parallel BC)", op="find angle B using alternate angles", rule="alternate angles on parallel lines",),
        step(from_latex=rf"B\hat{{A}}C + {ang_b}^\circ + {ang_c}^\circ = 180^\circ", to_latex_str=rf"B\hat{{A}}C = 180^\circ - 2({ang_tab}^\circ) = {ang_bac}^\circ \quad (\text{{sum of }}\angle\text{{s in }}\triangle)", op="calculate angle BAC in triangle ABC", rule="sum of angles in triangle",),
    ]
    canonical = solution_graph(goal="find angle BAC when tangent PT is parallel to chord BC", steps=steps, final_latex=rf"{ang_bac}^\circ")

    return make_math_question(
        prefix="g11_cg_42",
        topic=TOPIC_NAME,
        subskill="42_tan_chord_and_parallel_tangent",
        learning_objective_id=f"{LEARNING_OBJECTIVE_ID}_42",
        prompt=prompt,
        prompt_latex=prompt,
        answer_latex=rf"{ang_bac}^\circ",
        answer_sympy=str(ang_bac),
        sample_answer=rf"\hat{{C}} = {ang_c}^\circ \text{{ (tan chord theorem)}}; \; \hat{{B}} = {ang_b}^\circ \text{{ (alt }}\angle\text{{s, }} PT \parallel BC\text{{)}}; \; B\hat{{A}}C = {ang_bac}^\circ",
        canonical_solution=canonical,
        diagram_spec=diag,
        marking_schema={
            "total_marks": 4,
            "marking_points": [
                {"id": "mp1", "desc": f"Angle C = {ang_c} deg (tan chord theorem)", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Angle B = {ang_b} deg (alt angles, PT || BC)", "marks": 1, "editable": True},
                {"id": "mp3", "desc": "Sum of angles in triangle ABC = 180 deg", "marks": 1, "editable": True},
                {"id": "mp4", "desc": f"Angle BAC = {ang_bac} deg", "marks": 1, "editable": True},
            ],
        },
        hints={
            "1_nudge": "Use the tan-chord theorem to find $\\hat{C}$, and use alternate angles ($PT \\parallel BC$) to find $\\hat{B}$.",
            "2_concept": "$\\hat{C} = T\\hat{A}B$ (tan chord theorem) and $\\hat{B} = T\\hat{A}B$ (alt $\\angle$s, $PT \\parallel BC$).",
            "3_breakdown": f"$\\hat{{B}} = \\hat{{C}} = {ang_tab}^\\circ \\implies B\\hat{{A}}C = 180^\\circ - 2({ang_tab}^\\circ) = {ang_bac}^\\circ$.",
        },
        misconception_tags=["omitted_parallel_line_reason", "tangent_chord_error"],
        keywords=["circle geometry", "tan chord theorem", "parallel tangent and chord"],
        term=3,
        caps_weight_percent=35,
        suggested_duration_mins=4,
        mode="elementary_42_tan_chord_and_parallel_tangent",
        difficulty=difficulty,
    )

# 43. Algebraic Tan-Chord Theorem Equation
def arch_43_tan_chord_algebraic_x(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    x_val = r.randint(16, 34)
    a_val = r.randint(5, 18)
    ang_val = 2 * x_val + a_val
    b_val = ang_val - x_val

    pts = {
        "A": (210.0, 247.0),
        "P": (95.0, 247.0),
        "T": (325.0, 247.0),
        "B": _pt_on_circle(25),
        "C": _pt_on_circle(215),
    }

    prompt = (
        f"Line $PT$ is a tangent to the circle at $A$. Chord $AB$ subtends $\\hat{{C}} = (x + {b_val}^\\circ)$ "
        f"in the alternate segment, and $T\\hat{{A}}B = (2x + {a_val}^\\circ)$. "
        f"Determine the value of $x$ and state the geometric reason."
    )

    diag = circle_geo_svg(
        title=f"Algebraic Tan-Chord: ∠TAB = 2x + {a_val}°, ∠C = x + {b_val}°",
        points=pts,
        segments=[("P", "T"), ("A", "B"), ("B", "C"), ("C", "A")],
        show_center=False,
        callouts=[(162, 115, f"x+{b_val}°", "#1d4ed8"), (265, 238, f"2x+{a_val}°", "#dc2626")],
    )

    steps = [
        step(from_latex=r"T\hat{A}B = \hat{C}", to_latex_str=rf"2x + {a_val}^\circ = x + {b_val}^\circ \quad (\text{{tan chord theorem}})", op="equate angle between tangent and chord to angle in alternate segment", rule="tan-chord theorem",),
        step(from_latex=rf"2x - x = {b_val}^\circ - {a_val}^\circ", to_latex_str=rf"x = {x_val}^\circ", op="solve linear equation for x", rule="linear equation",),
    ]
    canonical = solution_graph(goal="solve for x using tan-chord theorem", steps=steps, final_latex=rf"{x_val}^\circ")

    return make_math_question(
        prefix="g11_cg_43",
        topic=TOPIC_NAME,
        subskill="43_tan_chord_algebraic_x",
        learning_objective_id=f"{LEARNING_OBJECTIVE_ID}_43",
        prompt=prompt,
        prompt_latex=prompt,
        answer_latex=rf"{x_val}^\circ",
        answer_sympy=str(x_val),
        sample_answer=rf"2x + {a_val}^\circ = x + {b_val}^\circ \implies x = {x_val}^\circ \quad (\text{{tan chord theorem}})",
        canonical_solution=canonical,
        diagram_spec=diag,
        marking_schema={
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": f"Equate 2x + {a_val} = x + {b_val}", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Reason: tan chord theorem", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"x = {x_val} deg", "marks": 1, "editable": True},
            ],
        },
        hints={
            "1_nudge": "By the tan-chord theorem, $T\\hat{A}B = \\hat{C}$.",
            "2_concept": "$2x + {a_val}^\\circ = x + {b_val}^\\circ$ (tan chord theorem).",
            "3_breakdown": f"$x = {b_val}^\\circ - {a_val}^\\circ = {x_val}^\\circ$.",
        },
        misconception_tags=["tangent_chord_error", "omitted_geometric_reason"],
        keywords=["circle geometry", "tan chord theorem", "algebraic"],
        term=3,
        caps_weight_percent=35,
        suggested_duration_mins=3,
        mode="elementary_43_tan_chord_algebraic_x",
        difficulty=difficulty,
    )

# 44. Converse of Tan-Chord Theorem — Prove Line is a Tangent
def arch_44_converse_tan_chord_prove_tangent(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    ang_c = r.randint(34, 68)
    ang_b = r.randint(45, 70)
    ang_bac = 180 - (ang_c + ang_b)

    pts = {
        "A": (210.0, 247.0),
        "P": (95.0, 247.0),
        "T": (325.0, 247.0),
        "B": _pt_on_circle(25),
        "C": _pt_on_circle(215),
    }

    prompt = (
        f"Points $A$, $B$, and $C$ lie on a circle, and line $PT$ passes through $A$. "
        f"In $\\triangle ABC$, $\\hat{{B}} = {ang_b}^\\circ$ and $B\\hat{{A}}C = {ang_bac}^\\circ$. "
        f"It is also given that $T\\hat{{A}}B = {ang_c}^\\circ$. "
        f"Calculate $\\hat{{C}}$ and state the converse geometric reason proving that $PT$ is a tangent to the circle at $A$."
    )

    diag = circle_geo_svg(
        title=f"Prove PT is a Tangent to Circle ABC at A (∠TAB = {ang_c}°)",
        points=pts,
        segments=[("P", "T"), ("A", "B"), ("B", "C"), ("C", "A")],
        show_center=False,
        callouts=[(265, 238, f"∠TAB={ang_c}°", "#1d4ed8"), (210, 292, f"∠B = {ang_b}°, ∠BAC = {ang_bac}° — Prove PT is tangent", "#dc2626")],
    )

    steps = [
        step(from_latex=rf"\hat{{B}} = {ang_b}^\circ, \; B\hat{{A}}C = {ang_bac}^\circ", to_latex_str=rf"\hat{{C}} = 180^\circ - ({ang_b}^\circ + {ang_bac}^\circ) = {ang_c}^\circ \quad (\text{{sum of }}\angle\text{{s in }}\triangle)", op="calculate angle C in triangle ABC", rule="sum of angles in triangle",),
        step(from_latex=rf"T\hat{{A}}B = \hat{{C}} = {ang_c}^\circ", to_latex_str=r"PT \text{ is a tangent at } A \quad (\text{converse tan chord theorem / }\angle\text{ between line and chord})", op="conclude PT is a tangent by converse tan-chord theorem", rule="converse tan-chord theorem",),
    ]
    canonical = solution_graph(goal="prove PT is a tangent using converse tan-chord theorem", steps=steps, final_latex=rf"{ang_c}^\circ")

    return make_math_question(
        prefix="g11_cg_44",
        topic=TOPIC_NAME,
        subskill="44_converse_tan_chord_prove_tangent",
        learning_objective_id=f"{LEARNING_OBJECTIVE_ID}_44",
        prompt=prompt,
        prompt_latex=prompt,
        answer_latex=rf"{ang_c}^\circ",
        answer_sympy=str(ang_c),
        sample_answer=rf"\hat{{C}} = 180^\circ - ({ang_b}^\circ + {ang_bac}^\circ) = {ang_c}^\circ = T\hat{{A}}B \implies PT \text{{ is a tangent (converse tan chord theorem)}}",
        canonical_solution=canonical,
        diagram_spec=diag,
        marking_schema={
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": f"Calculate C = {ang_c} deg (sum of angles in triangle)", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Show TAB = C = {ang_c} deg", "marks": 1, "editable": True},
                {"id": "mp3", "desc": "Converse reason: converse tan chord theorem / angle between line and chord", "marks": 1, "editable": True},
            ],
        },
        hints={
            "1_nudge": "First calculate $\\hat{C}$ in $\\triangle ABC$ and compare it with $T\\hat{A}B$.",
            "2_concept": "If the angle between a line $PT$ and chord $AB$ equals the angle subtended by $AB$ in the alternate segment ($\\hat{C}$), then $PT$ is a tangent (converse tan chord theorem).",
            "3_breakdown": f"$\\hat{{C}} = 180^\\circ - ({ang_b}^\\circ + {ang_bac}^\\circ) = {ang_c}^\\circ = T\\hat{{A}}B$, so $PT$ is a tangent.",
        },
        misconception_tags=["used_forward_reason_instead_of_converse", "omitted_geometric_reason"],
        keywords=["circle geometry", "converse tan chord theorem", "prove tangent"],
        term=3,
        caps_weight_percent=35,
        suggested_duration_mins=4,
        mode="elementary_44_converse_tan_chord_prove_tangent",
        difficulty=difficulty,
    )

# 45. Multi-Step Rider: Two Equal Tangents + Tan-Chord Theorem
def arch_45_rider_two_tangents_and_tan_chord(r: random.Random, difficulty: str = "hard") -> Dict[str, Any]:
    ang_c = r.randint(52, 74)
    ang_pab = ang_c
    ang_p = 180 - 2 * ang_pab

    pts = {
        "A": _pt_on_circle(-55),
        "B": _pt_on_circle(55),
        "C": _pt_on_circle(180),
        "P": (365.0, 155.0),
    }

    prompt = (
        f"From external point $P$, two tangents $PA$ and $PB$ are drawn to touch the circle at $A$ and $B$. "
        f"Point $C$ lies on the major arc $AB$, and chords $AB$, $AC$, and $BC$ are drawn. "
        f"If $\\hat{{P}} = {ang_p}^\\circ$, calculate the size of $A\\hat{{C}}B$, stating all geometric reasons."
    )

    diag = circle_geo_svg(
        title=f"Two Tangents & Tan-Chord Rider: ∠P = {ang_p}° — Find ∠ACB",
        points=pts,
        segments=[("P", "A"), ("P", "B"), ("A", "B"), ("A", "C"), ("B", "C")],
        show_center=False,
        callouts=[(322, 158, f"∠P={ang_p}°", "#dc2626"), (145, 158, "∠ACB=?", "#1d4ed8")],
    )

    steps = [
        step(from_latex=r"PA = PB \quad (\text{tans from same pt})", to_latex_str=rf"P\hat{{A}}B = P\hat{{B}}A = \frac{{180^\circ - {ang_p}^\circ}}{{2}} = {ang_pab}^\circ \quad (\angle\text{{s opp equal sides}})", op="calculate base angle PAB in isosceles triangle PAB", rule="tangents from a common point are equal",),
        step(from_latex=rf"P\hat{{A}}B = {ang_pab}^\circ", to_latex_str=rf"A\hat{{C}}B = P\hat{{A}}B = {ang_c}^\circ \quad (\text{{tan chord theorem}})", op="apply tan-chord theorem to find angle ACB", rule="tan-chord theorem",),
    ]
    canonical = solution_graph(goal="find angle ACB from external tangent angle P", steps=steps, final_latex=rf"{ang_c}^\circ")

    return make_math_question(
        prefix="g11_cg_45",
        topic=TOPIC_NAME,
        subskill="45_rider_two_tangents_and_tan_chord",
        learning_objective_id=f"{LEARNING_OBJECTIVE_ID}_45",
        prompt=prompt,
        prompt_latex=prompt,
        answer_latex=rf"{ang_c}^\circ",
        answer_sympy=str(ang_c),
        sample_answer=rf"P\hat{{A}}B = \frac{{180^\circ - {ang_p}^\circ}}{{2}} = {ang_pab}^\circ \text{{ (tans from same pt)}}; \; A\hat{{C}}B = P\hat{{A}}B = {ang_c}^\circ \text{{ (tan chord theorem)}}",
        canonical_solution=canonical,
        diagram_spec=diag,
        marking_schema={
            "total_marks": 4,
            "marking_points": [
                {"id": "mp1", "desc": "PA = PB (tans from same pt)", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Angle PAB = {ang_pab} deg", "marks": 1, "editable": True},
                {"id": "mp3", "desc": "Reason: tan chord theorem", "marks": 1, "editable": True},
                {"id": "mp4", "desc": f"Angle ACB = {ang_c} deg", "marks": 1, "editable": True},
            ],
        },
        hints={
            "1_nudge": "First use $\\triangle PAB$ ($PA = PB$) to find $P\\hat{A}B$, then apply the tan-chord theorem.",
            "2_concept": "$P\\hat{A}B = \\frac{180^\\circ - \\hat{P}}{2}$ (tans from same pt) and $A\\hat{C}B = P\\hat{A}B$ (tan chord theorem).",
            "3_breakdown": f"$P\\hat{{A}}B = {ang_pab}^\\circ \\implies A\\hat{{C}}B = {ang_c}^\\circ$.",
        },
        misconception_tags=["omitted_geometric_reason", "treated_pacb_as_cyclic_quad"],
        keywords=["circle geometry", "rider", "two tangents", "tan chord theorem"],
        term=3,
        caps_weight_percent=35,
        suggested_duration_mins=5,
        mode="elementary_45_rider_two_tangents_and_tan_chord",
        difficulty=difficulty,
    )

# 46. Multi-Step Rider: Diameter + Tangent + Secant
def arch_46_rider_diameter_and_tan_chord(r: random.Random, difficulty: str = "hard") -> Dict[str, Any]:
    ang_a = r.randint(25, 62)
    ang_abc = 90 - ang_a
    ang_tbc = ang_a

    pts = {
        "O": (210.0, 155.0),
        "A": _pt_on_circle(180),
        "B": _pt_on_circle(0),
        "C": _pt_on_circle(245),
        "T": (302.0, 245.0),
    }

    prompt = (
        f"In the circle with centre $O$, $AB$ is a diameter and $BT$ is a tangent to the circle at $B$. "
        f"Point $C$ lies on the circumference and chords $AC$ and $BC$ are drawn. "
        f"If $\\hat{{A}} = {ang_a}^\\circ$, calculate the size of $A\\hat{{B}}C$ and $C\\hat{{B}}T$, "
        f"giving complete geometric reasons."
    )

    diag = circle_geo_svg(
        title=f"Diameter AB & Tangent BT at B: ∠A = {ang_a}° — Find ∠CBT",
        points=pts,
        segments=[("A", "B"), ("A", "C"), ("B", "C"), ("B", "T")],
        callouts=[(145, 148, f"∠A={ang_a}°", "#1d4ed8"), (285, 210, "∠CBT=?", "#dc2626")],
    )

    steps = [
        step(from_latex=r"\text{Diameter } AB", to_latex_str=rf"A\hat{{C}}B = 90^\circ \quad (\angle \text{{ in semi-circle}}) \implies A\hat{{B}}C = 90^\circ - {ang_a}^\circ = {ang_abc}^\circ", op="find angle ABC using angle in semi-circle", rule="angle in semi-circle",),
        step(from_latex=r"AB \perp BT \quad (\tan \perp \text{rad}) \quad \text{or tan-chord theorem}", to_latex_str=rf"C\hat{{B}}T = \hat{{A}} = {ang_tbc}^\circ \quad (\text{{tan chord theorem}})", op="find angle CBT between tangent BT and chord BC", rule="tan-chord theorem",),
    ]
    canonical = solution_graph(goal="find angle CBT", steps=steps, final_latex=rf"{ang_tbc}^\circ")

    return make_math_question(
        prefix="g11_cg_46",
        topic=TOPIC_NAME,
        subskill="46_rider_diameter_and_tan_chord",
        learning_objective_id=f"{LEARNING_OBJECTIVE_ID}_46",
        prompt=prompt,
        prompt_latex=prompt,
        answer_latex=rf"{ang_tbc}^\circ",
        answer_sympy=str(ang_tbc),
        sample_answer=rf"A\hat{{C}}B = 90^\circ \text{{ (}}\angle\text{{ in semi-circle)}}; \; A\hat{{B}}C = {ang_abc}^\circ; \; C\hat{{B}}T = {ang_tbc}^\circ \text{{ (tan chord theorem or }}\tan\perp\text{{rad)}}",
        canonical_solution=canonical,
        diagram_spec=diag,
        marking_schema={
            "total_marks": 4,
            "marking_points": [
                {"id": "mp1", "desc": "Angle ACB = 90 deg (angle in semi-circle)", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Angle ABC = {ang_abc} deg", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Angle CBT = {ang_tbc} deg", "marks": 1, "editable": True},
                {"id": "mp4", "desc": "Reason: tan chord theorem or tan perp rad", "marks": 1, "editable": True},
            ],
        },
        hints={
            "1_nudge": "Use $\\hat{C} = 90^\\circ$ ($\\angle$ in semi-circle) to find $A\\hat{B}C$, and use either $\\tan \\perp \\text{rad}$ or the tan-chord theorem for $C\\hat{B}T$.",
            "2_concept": "$A\\hat{B}T = 90^\\circ$ ($\\tan \\perp \\text{rad}$) and $C\\hat{B}T = \\hat{A}$ (tan chord theorem).",
            "3_breakdown": f"$A\\hat{{B}}C = {ang_abc}^\\circ$ and $C\\hat{{B}}T = {ang_tbc}^\\circ$.",
        },
        misconception_tags=["tangent_radius_perpendicular_miss", "omitted_geometric_reason"],
        keywords=["circle geometry", "semi-circle", "tan chord theorem"],
        term=3,
        caps_weight_percent=35,
        suggested_duration_mins=4,
        mode="elementary_46_rider_diameter_and_tan_chord",
        difficulty=difficulty,
    )

# 47. Multi-Step Rider: Cyclic Quad + Tan-Chord Theorem
def arch_47_rider_cyclic_quad_and_tan_chord(r: random.Random, difficulty: str = "hard") -> Dict[str, Any]:
    ang_tab = r.randint(36, 54)
    ang_dca = ang_tab + r.randint(12, 24)
    ang_acb = ang_tab
    ang_bcd = ang_acb + ang_dca
    ang_bad = 180 - ang_bcd

    pts = {
        "A": (210.0, 247.0),
        "P": (95.0, 247.0),
        "T": (325.0, 247.0),
        "B": _pt_on_circle(20),
        "C": _pt_on_circle(250),
        "D": _pt_on_circle(160),
    }

    prompt = (
        f"$ABCD$ is a cyclic quadrilateral and $PT$ is a tangent to the circle at $A$. "
        f"Diagonal $AC$ is drawn. It is given that $T\\hat{{A}}B = {ang_tab}^\\circ$ and "
        f"$D\\hat{{C}}A = {ang_dca}^\\circ$. Calculate the size of $B\\hat{{A}}D$, "
        f"stating all geometric reasons."
    )

    diag = circle_geo_svg(
        title=f"Cyclic Quad & Tan-Chord Rider: ∠TAB={ang_tab}°, ∠DCA={ang_dca}°",
        points=pts,
        segments=[("P", "T"), ("A", "B"), ("B", "C"), ("C", "D"), ("D", "A"), ("A", "C")],
        show_center=False,
        callouts=[(265, 238, f"∠TAB={ang_tab}°", "#1d4ed8"), (175, 92, f"∠DCA={ang_dca}°", "#1d4ed8"), (210, 292, "Find ∠BAD", "#dc2626")],
    )

    steps = [
        step(from_latex=rf"T\hat{{A}}B = {ang_tab}^\circ", to_latex_str=rf"A\hat{{C}}B = T\hat{{A}}B = {ang_acb}^\circ \quad (\text{{tan chord theorem}})", op="find angle ACB using tan-chord theorem", rule="tan-chord theorem",),
        step(from_latex=rf"B\hat{{C}}D = A\hat{{C}}B + D\hat{{C}}A = {ang_acb}^\circ + {ang_dca}^\circ = {ang_bcd}^\circ", to_latex_str=rf"B\hat{{A}}D = 180^\circ - {ang_bcd}^\circ = {ang_bad}^\circ \quad (\text{{opp }}\angle\text{{s of cyclic quad}})", op="use opposite angles of cyclic quad ABCD to find angle BAD", rule="opposite angles of cyclic quadrilateral",),
    ]
    canonical = solution_graph(goal="find angle BAD using tan-chord and cyclic quad theorems", steps=steps, final_latex=rf"{ang_bad}^\circ")

    return make_math_question(
        prefix="g11_cg_47",
        topic=TOPIC_NAME,
        subskill="47_rider_cyclic_quad_and_tan_chord",
        learning_objective_id=f"{LEARNING_OBJECTIVE_ID}_47",
        prompt=prompt,
        prompt_latex=prompt,
        answer_latex=rf"{ang_bad}^\circ",
        answer_sympy=str(ang_bad),
        sample_answer=rf"A\hat{{C}}B = {ang_acb}^\circ \text{{ (tan chord theorem)}}; \; B\hat{{C}}D = {ang_bcd}^\circ; \; B\hat{{A}}D = 180^\circ - {ang_bcd}^\circ = {ang_bad}^\circ \text{{ (opp }}\angle\text{{s of cyclic quad)}}",
        canonical_solution=canonical,
        diagram_spec=diag,
        marking_schema={
            "total_marks": 4,
            "marking_points": [
                {"id": "mp1", "desc": f"Angle ACB = {ang_acb} deg (tan chord theorem)", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Angle BCD = {ang_bcd} deg", "marks": 1, "editable": True},
                {"id": "mp3", "desc": "Reason: opp angles of cyclic quad", "marks": 1, "editable": True},
                {"id": "mp4", "desc": f"Angle BAD = {ang_bad} deg", "marks": 1, "editable": True},
            ],
        },
        hints={
            "1_nudge": "First find $A\\hat{C}B$ using the tan-chord theorem, then combine it with $D\\hat{C}A$ to get the full angle $B\\hat{C}D$.",
            "2_concept": "$A\\hat{C}B = T\\hat{A}B = {ang_tab}^\\circ$ (tan chord theorem) and $B\\hat{A}D = 180^\\circ - B\\hat{C}D$ (opp $\\angle$s of cyclic quad).",
            "3_breakdown": f"$B\\hat{{C}}D = {ang_acb}^\\circ + {ang_dca}^\\circ = {ang_bcd}^\\circ \\implies B\\hat{{A}}D = 180^\\circ - {ang_bcd}^\\circ = {ang_bad}^\\circ$.",
        },
        misconception_tags=["tangent_chord_error", "omitted_geometric_reason"],
        keywords=["circle geometry", "cyclic quad", "tan chord theorem", "rider"],
        term=3,
        caps_weight_percent=35,
        suggested_duration_mins=5,
        mode="elementary_47_rider_cyclic_quad_and_tan_chord",
        difficulty=difficulty,
    )

# 48. Formal Theorem Proof: Line from Centre ⊥ to Chord Bisects Chord (RHS)
def arch_48_formal_proof_perp_from_centre_bisects_chord(r: random.Random, difficulty: str = "hard") -> Dict[str, Any]:
    rad_val = r.randint(10, 25)
    pts = {
        "O": (210.0, 155.0),
        "A": _pt_on_circle(140),
        "B": _pt_on_circle(40),
    }
    pts["P"] = (round((pts["A"][0] + pts["B"][0]) / 2, 1), round((pts["A"][1] + pts["B"][1]) / 2, 1))

    prompt = (
        f"In the circle with centre $O$ (radius $r = {rad_val}\\text{{ units}}$), $OP \\perp AB$ at $P$ on chord $AB$. "
        f"Prove the theorem that states: a line drawn from the centre of a circle perpendicular to a chord bisects the chord ($AP = PB$). "
        f"State the construction, the three congruency steps in $\\triangle OAP$ and $\\triangle OBP$, and the congruency condition."
    )

    diag = circle_geo_svg(
        title=f"Formal Proof (r = {rad_val}): Prove OP ⊥ AB ⇒ AP = PB (RHS)",
        points=pts,
        segments=[("O", "P"), ("A", "B")],
        dashed_segments=[("O", "A"), ("O", "B")],
        right_angle_at=pts["P"],
        callouts=[(210, 290, f"Construction: Join radii OA and OB (r = {rad_val}) — Prove △OAP ≡ △OBP", "#1d4ed8")],
    )

    steps = [
        step(from_latex=r"\text{Construction: Join radii } OA \text{ and } OB", to_latex_str=r"\text{In }\triangle OAP \text{ and }\triangle OBP: \; O\hat{P}A = O\hat{P}B = 90^\circ \quad (\text{given } OP \perp AB)", op="state construction and right angle", rule="given perpendicular",),
        step(from_latex=r"OA = OB \quad (\text{radii})", to_latex_str=r"OP = OP \quad (\text{common side})", op="identify equal radii and common side OP", rule="equal radii and common side",),
        step(from_latex=r"\therefore \triangle OAP \equiv \triangle OBP \quad (\text{RHS})", to_latex_str=r"\therefore AP = PB \quad (\text{corresponding sides of }\equiv \triangle\text{s})", op="conclude congruency by RHS and deduce AP = PB", rule="RHS congruency",),
    ]
    canonical = solution_graph(goal="prove OP perp AB implies AP = PB by RHS", steps=steps, final_latex=r"AP = PB \quad (\text{RHS})")

    return make_math_question(
        prefix="g11_cg_48",
        topic=TOPIC_NAME,
        subskill="48_formal_proof_perp_from_centre_bisects_chord",
        learning_objective_id=f"{LEARNING_OBJECTIVE_ID}_48",
        prompt=prompt,
        prompt_latex=prompt,
        answer_latex=r"\triangle OAP \equiv \triangle OBP \text{ (RHS)} \implies AP = PB",
        answer_sympy="RHS",
        sample_answer=r"\text{Join } OA, OB. \text{ In }\triangle OAP, \triangle OBP: O\hat{P}A=O\hat{P}B=90^\circ, OA=OB \text{ (radii)}, OP=OP \text{ (common)} \implies \triangle OAP \equiv \triangle OBP \text{ (RHS)} \implies AP = PB",
        canonical_solution=canonical,
        diagram_spec=diag,
        marking_schema={
            "total_marks": 5,
            "marking_points": [
                {"id": "mp1", "desc": "Construction: Join radii OA and OB", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Angle OPA = Angle OPB = 90 deg (given)", "marks": 1, "editable": True},
                {"id": "mp3", "desc": "OA = OB (radii) and OP = OP (common)", "marks": 1, "editable": True},
                {"id": "mp4", "desc": "Triangle OAP congruent to Triangle OBP (RHS)", "marks": 1, "editable": True},
                {"id": "mp5", "desc": "Conclusion AP = PB", "marks": 1, "editable": True},
            ],
        },
        hints={
            "1_nudge": "Start with the construction: join radii $OA$ and $OB$ to form two right-angled triangles $\\triangle OAP$ and $\\triangle OBP$.",
            "2_concept": "Prove $\\triangle OAP \\equiv \\triangle OBP$ using Right-angle ($90^\\circ$), Hypotenuse ($OA = OB$ radii), and Side ($OP$ common).",
            "3_breakdown": "$\\triangle OAP \\equiv \\triangle OBP$ (RHS) $\\implies AP = PB$.",
        },
        misconception_tags=["used_ssa_instead_of_rhs", "omitted_construction_step"],
        keywords=["circle geometry", "formal theorem proof", "RHS congruency", "chord bisector"],
        term=3,
        caps_weight_percent=35,
        suggested_duration_mins=5,
        mode="elementary_48_formal_proof_perp_from_centre_bisects_chord",
        difficulty=difficulty,
    )

# 49. Formal Theorem Proof: Angle at Centre = 2 × Angle at Circumference
def arch_49_formal_proof_angle_at_centre_twice_circumference(r: random.Random, difficulty: str = "hard") -> Dict[str, Any]:
    ang_c1 = r.randint(18, 34)
    ang_c2 = r.randint(20, 36)
    ang_c = ang_c1 + ang_c2
    ang_o = 2 * ang_c

    pts = {
        "O": (210.0, 155.0),
        "A": _pt_on_circle(135),
        "B": _pt_on_circle(45),
        "C": _pt_on_circle(270),
        "P": (210.0, 215.0),
    }

    prompt = (
        f"In the circle with centre $O$, arc $AB$ subtends $A\\hat{{O}}B$ at the centre and $A\\hat{{C}}B$ at the circumference "
        f"(for instance where $\\hat{{C}}_1 = {ang_c1}^\\circ$ and $\\hat{{C}}_2 = {ang_c2}^\\circ$). "
        f"Prove the theorem that states: $A\\hat{{O}}B = 2 A\\hat{{C}}B$, and verify the result when $A\\hat{{C}}B = {ang_c}^\\circ$."
    )

    diag = circle_geo_svg(
        title=f"Formal Proof: ∠AOB = 2∠ACB (Verify for ∠C = {ang_c}° → ∠O = {ang_o}°)",
        points=pts,
        segments=[("O", "A"), ("O", "B"), ("C", "A"), ("C", "B")],
        dashed_segments=[("C", "P")],
        callouts=[(210, 292, f"Construction: Join CO and produce to P (∠C = {ang_c}° ⇒ ∠AOB = {ang_o}°)", "#1d4ed8")],
    )

    steps = [
        step(from_latex=r"\text{Construction: Join } CO \text{ and produce to } P", to_latex_str=r"\hat{O}_1 = \hat{A} + \hat{C}_1 \quad (\text{ext }\angle\text{ of }\triangle AOC)", op="use exterior angle of triangle AOC", rule="exterior angle of triangle",),
        step(from_latex=r"OA = OC \quad (\text{radii}) \implies \hat{A} = \hat{C}_1 \quad (\angle\text{s opp equal sides})", to_latex_str=r"\therefore \hat{O}_1 = 2\hat{C}_1 \quad \text{and similarly} \quad \hat{O}_2 = 2\hat{C}_2", op="express O1 and O2 in terms of C1 and C2", rule="angles opposite equal radii",),
        step(from_latex=r"A\hat{O}B = \hat{O}_1 + \hat{O}_2 = 2(\hat{C}_1 + \hat{C}_2) = 2A\hat{C}B", to_latex_str=rf"A\hat{{O}}B = 2({ang_c}^\circ) = {ang_o}^\circ", op="add O1 and O2 and factor out 2", rule="distributive property",),
    ]
    canonical = solution_graph(goal="prove angle at centre = 2 x angle at circumference", steps=steps, final_latex=rf"{ang_o}^\circ")

    return make_math_question(
        prefix="g11_cg_49",
        topic=TOPIC_NAME,
        subskill="49_formal_proof_angle_at_centre_twice_circumference",
        learning_objective_id=f"{LEARNING_OBJECTIVE_ID}_49",
        prompt=prompt,
        prompt_latex=prompt,
        answer_latex=rf"{ang_o}^\circ",
        answer_sympy=str(ang_o),
        sample_answer=rf"\text{{Join }} CO \text{{ produced to }} P. \; \hat{{O}}_1 = 2\hat{{C}}_1 \text{{ and }} \hat{{O}}_2 = 2\hat{{C}}_2 \text{{ (ext }}\angle\text{{ of }}\triangle, \text{{ radii)}} \implies A\hat{{O}}B = 2A\hat{{C}}B = {ang_o}^\circ",
        canonical_solution=canonical,
        diagram_spec=diag,
        marking_schema={
            "total_marks": 5,
            "marking_points": [
                {"id": "mp1", "desc": "Construction: Join CO and produce to P", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "O1 = A + C1 (ext angle of triangle AOC)", "marks": 1, "editable": True},
                {"id": "mp3", "desc": "OA = OC (radii) implies A = C1, so O1 = 2C1", "marks": 1, "editable": True},
                {"id": "mp4", "desc": "Similarly O2 = 2C2, so AOB = 2(C1 + C2) = 2ACB", "marks": 1, "editable": True},
                {"id": "mp5", "desc": f"Numerical verification AOB = {ang_o} deg", "marks": 1, "editable": True},
            ],
        },
        hints={
            "1_nudge": "Begin with the construction: join $CO$ and produce it to $P$, splitting $\\triangle ABC$ into two isosceles triangles $\\triangle AOC$ and $\\triangle BOC$.",
            "2_concept": "Use the exterior angle of $\\triangle AOC$ ($\\hat{O}_1 = \\hat{A} + \\hat{C}_1$) and equal radii ($OA = OC \\implies \\hat{A} = \\hat{C}_1$).",
            "3_breakdown": f"$\\hat{{O}}_1 + \\hat{{O}}_2 = 2(\\hat{{C}}_1 + \\hat{{C}}_2) = 2({ang_c}^\\circ) = {ang_o}^\\circ$.",
        },
        misconception_tags=["omitted_construction_step", "omitted_geometric_reason"],
        keywords=["circle geometry", "formal theorem proof", "angle at centre"],
        term=3,
        caps_weight_percent=35,
        suggested_duration_mins=6,
        mode="elementary_49_formal_proof_angle_at_centre_twice_circumference",
        difficulty=difficulty,
    )

# 50. Capstone Multi-Theorem Circle Geometry Rider (7 Marks)
def arch_50_capstone_multi_theorem_circle_rider(r: random.Random, difficulty: str = "hard") -> Dict[str, Any]:
    ang_d = r.randint(34, 52)
    ang_o1 = 2 * ang_d
    ang_b = 180 - ang_d
    ang_pac = ang_d

    pts = {
        "O": (210.0, 155.0),
        "A": (210.0, 247.0),
        "P": (95.0, 247.0),
        "T": (325.0, 247.0),
        "B": _pt_on_circle(25),
        "C": _pt_on_circle(315),
        "D": _pt_on_circle(215),
    }

    prompt = (
        f"In the diagram, the circle with centre $O$ passes through points $A$, $B$, $C$, and $D$. "
        f"Line $PT$ is a tangent to the circle at $A$, and radii $OA$ and $OC$ are drawn. "
        f"It is given that $A\\hat{{D}}C = {ang_d}^\\circ$. "
        f"Determine, with complete geometric reasons, the size of:\n"
        f"(a) $A\\hat{{O}}C$ (at the centre),\n"
        f"(b) $\\hat{{B}}$ (in cyclic quad $ABCD$),\n"
        f"(c) $P\\hat{{A}}C$ (between tangent $PT$ and chord $AC$),\n"
        f"and state the sum $A\\hat{{O}}C + \\hat{{B}} + P\\hat{{A}}C$."
    )

    total_sum = ang_o1 + ang_b + ang_pac

    diag = circle_geo_svg(
        title=f"Capstone Multi-Theorem Circle Rider: ∠ADC = {ang_d}°",
        points=pts,
        segments=[("P", "T"), ("O", "A"), ("O", "C"), ("A", "C"), ("A", "B"), ("B", "C"), ("C", "D"), ("D", "A")],
        callouts=[(162, 112, f"∠D={ang_d}°", "#1d4ed8"), (210, 292, "Find ∠AOC, ∠B, and ∠PAC", "#dc2626")],
    )

    steps = [
        step(from_latex=rf"A\hat{{D}}C = {ang_d}^\circ", to_latex_str=rf"A\hat{{O}}C = 2 \times {ang_d}^\circ = {ang_o1}^\circ \quad (\angle \text{{ at centre }} = 2\times\angle \text{{ at circ}})", op="apply angle at centre theorem", rule="angle at centre = 2 x angle at circumference",),
        step(from_latex=rf"A\hat{{D}}C = {ang_d}^\circ", to_latex_str=rf"\hat{{B}} = 180^\circ - {ang_d}^\circ = {ang_b}^\circ \quad (\text{{opp }}\angle\text{{s of cyclic quad}})", op="apply cyclic quad opposite angles theorem", rule="opposite angles of cyclic quadrilateral",),
        step(from_latex=rf"A\hat{{D}}C = {ang_d}^\circ", to_latex_str=rf"P\hat{{A}}C = A\hat{{D}}C = {ang_pac}^\circ \quad (\text{{tan chord theorem}})", op="apply tan-chord theorem and sum the three angles", rule="tan-chord theorem",),
    ]
    canonical = solution_graph(
        goal="determine all three rider angles and their sum",
        steps=steps,
        final_latex=rf"{total_sum}^\circ",
    )

    return make_math_question(
        prefix="g11_cg_50",
        topic=TOPIC_NAME,
        subskill="50_capstone_multi_theorem_circle_rider",
        learning_objective_id=f"{LEARNING_OBJECTIVE_ID}_50",
        prompt=prompt,
        prompt_latex=prompt,
        answer_latex=rf"{total_sum}^\circ",
        answer_sympy=str(total_sum),
        sample_answer=rf"A\hat{{O}}C = {ang_o1}^\circ \text{{ (}}\angle\text{{ at centre}} = 2\angle\text{{ at circ)}}; \; \hat{{B}} = {ang_b}^\circ \text{{ (opp }}\angle\text{{s of cyclic quad)}}; \; P\hat{{A}}C = {ang_pac}^\circ \text{{ (tan chord theorem)}}; \; \text{{Sum}} = {total_sum}^\circ",
        canonical_solution=canonical,
        diagram_spec=diag,
        marking_schema={
            "total_marks": 7,
            "marking_points": [
                {"id": "mp1", "desc": f"Angle AOC = {ang_o1} deg", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Reason: angle at centre = 2 x angle at circ", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Angle B = {ang_b} deg", "marks": 1, "editable": True},
                {"id": "mp4", "desc": "Reason: opp angles of cyclic quad", "marks": 1, "editable": True},
                {"id": "mp5", "desc": f"Angle PAC = {ang_pac} deg", "marks": 1, "editable": True},
                {"id": "mp6", "desc": "Reason: tan chord theorem", "marks": 1, "editable": True},
                {"id": "mp7", "desc": f"Total sum = {total_sum} deg", "marks": 1, "editable": True},
            ],
        },
        hints={
            "1_nudge": "Apply the angle at centre theorem for $A\\hat{O}C$, cyclic quad opposite angles for $\\hat{B}$, and the tan-chord theorem for $P\\hat{A}C$.",
            "2_concept": "$A\\hat{O}C = 2\\hat{D}$, $\\hat{B} = 180^\\circ - \\hat{D}$, and $P\\hat{A}C = \\hat{D}$.",
            "3_breakdown": f"$A\\hat{{O}}C = {ang_o1}^\\circ, \\; \\hat{{B}} = {ang_b}^\\circ, \\; P\\hat{{A}}C = {ang_pac}^\\circ \\implies \\text{{Sum}} = {total_sum}^\\circ$.",
        },
        misconception_tags=["omitted_geometric_reason", "confused_cyclic_quad_opposite_angles", "tangent_chord_error"],
        keywords=["circle geometry", "capstone rider", "angle at centre", "cyclic quad", "tan chord theorem"],
        term=3,
        caps_weight_percent=35,
        suggested_duration_mins=8,
        mode="compound",
        difficulty=difficulty,
    )

ARCHETYPE_BUILDERS_26_50: Dict[str, Callable[[random.Random, str], Dict[str, Any]]] = {
    "26_cyclic_quad_opposite_angles_supplementary": arch_26_cyclic_quad_opposite_angles_supplementary,
    "27_cyclic_quad_opposite_angles_algebraic_x": arch_27_cyclic_quad_opposite_angles_algebraic_x,
    "28_cyclic_quad_with_parallel_sides": arch_28_cyclic_quad_with_parallel_sides,
    "29_cyclic_quad_exterior_angle_basic": arch_29_cyclic_quad_exterior_angle_basic,
    "30_cyclic_quad_exterior_angle_algebraic": arch_30_cyclic_quad_exterior_angle_algebraic,
    "31_cyclic_quad_combined_centre_and_opposite": arch_31_cyclic_quad_combined_centre_and_opposite,
    "32_converse_cyclic_quad_opp_angles_supplementary": arch_32_converse_cyclic_quad_opp_angles_supplementary,
    "33_converse_cyclic_quad_exterior_equals_interior": arch_33_converse_cyclic_quad_exterior_equals_interior,
    "34_converse_cyclic_quad_line_subtends_equal_angles": arch_34_converse_cyclic_quad_line_subtends_equal_angles,
    "35_tangent_perp_radius_basic": arch_35_tangent_perp_radius_basic,
    "36_tangent_perp_radius_pythagoras_length": arch_36_tangent_perp_radius_pythagoras_length,
    "37_two_tangents_from_common_point_isosceles": arch_37_two_tangents_from_common_point_isosceles,
    "38_two_tangents_and_centre_kite": arch_38_two_tangents_and_centre_kite,
    "39_two_tangents_perimeter_triangle": arch_39_two_tangents_perimeter_triangle,
    "40_tan_chord_theorem_basic": arch_40_tan_chord_theorem_basic,
    "41_tan_chord_with_isosceles_chord_triangle": arch_41_tan_chord_with_isosceles_chord_triangle,
    "42_tan_chord_and_parallel_tangent": arch_42_tan_chord_and_parallel_tangent,
    "43_tan_chord_algebraic_x": arch_43_tan_chord_algebraic_x,
    "44_converse_tan_chord_prove_tangent": arch_44_converse_tan_chord_prove_tangent,
    "45_rider_two_tangents_and_tan_chord": arch_45_rider_two_tangents_and_tan_chord,
    "46_rider_diameter_and_tan_chord": arch_46_rider_diameter_and_tan_chord,
    "47_rider_cyclic_quad_and_tan_chord": arch_47_rider_cyclic_quad_and_tan_chord,
    "48_formal_proof_perp_from_centre_bisects_chord": arch_48_formal_proof_perp_from_centre_bisects_chord,
    "49_formal_proof_angle_at_centre_twice_circumference": arch_49_formal_proof_angle_at_centre_twice_circumference,
    "50_capstone_multi_theorem_circle_rider": arch_50_capstone_multi_theorem_circle_rider,
}
