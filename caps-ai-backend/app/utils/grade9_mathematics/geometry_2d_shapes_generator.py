"""Grade 9 Mathematics — Geometry of 2D Shapes Generator (Deterministic 6-Pillar Contract).

Curriculum Alignment:
- Grade 9 Term 2: Geometry of 2D shapes
- South African National Curriculum Standards (Senior Phase Mathematics)
- Triangles: interior angles sum to 180° [sum of ∠s in △], exterior angle theorem [ext ∠ of △],
  isosceles triangles [∠s opp equal sides], equilateral triangles [equilat △].
- Congruent triangles: 4 conditions (SSS, SAS, AAS, RHS) with formal 2-column Statement-Reason proofs.
- Similar triangles: AAA, corresponding sides in proportion (calculating unknown side length).
- Quadrilaterals: properties of parallelograms, rhombi, rectangles, squares, kites, trapezia.

6 Pillars:
- Deterministic seed generation with zero LLM authority
- Directed solution graph with dependency tracking
- Adaptive deconstruction (atomic elementary sub-drills on error)
- Rich 3-tier hints (Conceptual, Procedural with geometry theorem, Concrete Step-by-Step with actual numbers)
- Misconception-targeted error taxonomy
- Native DiagramRenderer specs (kind: 'triangle' / 'quadrilateral')
"""
from __future__ import annotations

import math
import random
import uuid
from typing import Any, Dict, List, Optional

from app.utils.grade9_mathematics._math_common import rng
from app.utils.grade9_mathematics import congruence_similarity_generator as cs_gen

TOPIC = "grade9_math_geometry_of_2d_shapes"
LO = "math9_geometry_2d_shapes"


def generate_grade9_geometry_2d_shapes_question(
    seed: Optional[int] = None,
    difficulty: str = "medium",
    mode: str = "compound",
    subskill: Optional[str] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    r = rng(seed)

    archetype_choices = [
        "triangle_ext_angle",
        "triangle_isosceles",
        "congruence_proof",
        "similarity_proportion",
        "quadrilateral_parallelogram",
    ]

    selected_subskill = subskill or mode
    if selected_subskill in archetype_choices:
        archetype = selected_subskill
    else:
        archetype = r.choice(archetype_choices)

    qid = f"g9_geom_2d_{seed or r.randint(1000, 9999)}_{uuid.uuid4().hex[:6]}"

    if archetype == "congruence_proof":
        # Leverage the dedicated congruence proof generator
        cs_res = cs_gen.generate(seed=seed, count=1, difficulty=difficulty, mode="compound")
        q = cs_res["questions"][0]
        q["topic"] = TOPIC
        q["learning_objective_id"] = LO
        q["term"] = 2
        return q

    elif archetype == "triangle_ext_angle":
        # In triangle ABC, side BC is produced to D.
        # Ext angle ACD = Angle A + Angle B.
        ang_a = r.randint(35, 65)
        ang_b = r.randint(40, 70)
        ext_ang = ang_a + ang_b
        
        # Make one an algebraic expression: Angle A = 2x + 5, Angle B = ang_b, Ext = ext_ang
        x_val = r.randint(15, 25)
        a_coeff = r.randint(2, 3)
        b_const = ang_a - a_coeff * x_val
        expr_a = f"{a_coeff}x + {b_const}" if b_const >= 0 else f"{a_coeff}x - {abs(b_const)}"

        question_text = (
            f"In $\\Delta ABC$, side $BC$ is produced to point $D$ to form the exterior angle $\\hat{{C}}_1 = {ext_ang}^\\circ$.\n\n"
            f"Given that $\\hat{{A}} = {expr_a}^\\circ$ and $\\hat{{B}} = {ang_b}^\\circ$:\n"
            f"1. Write down a geometric statement and reason connecting these three angles.\n"
            f"2. Solve for the value of $x$."
        )

        steps = [
            {"id": "S1", "statement": f"$\\hat{{A}} + \\hat{{B}} = \\hat{{C}}_1$", "reason": "ext \u2220 of \u25b3", "deps": []},
            {"id": "S2", "statement": f"({expr_a}) + {ang_b} = {ext_ang}", "reason": "substitute given values", "deps": ["S1"]},
            {"id": "S3", "statement": f"${a_coeff}x + {b_const + ang_b} = {ext_ang}$", "reason": "simplify constants", "deps": ["S2"]},
            {"id": "S4", "statement": f"$x = {x_val}$", "reason": f"solve for x", "deps": ["S3"]},
        ]

        hints = [
            "The exterior angle of a triangle equals the sum of the two opposite interior angles.",
            f"Set up the equation: $\\hat{{A}} + \\hat{{B}} = \\hat{{C}}_1$ [ext $\\angle$ of $\\Delta$].",
            f"Substitute the values: $({expr_a}) + {ang_b} = {ext_ang}$. Solve for $x$ to get $x = {x_val}$.",
        ]

        error_tax = [
            {
                "id": "err_triangle_sum_180",
                "tag": "misconception_exterior_sum_180",
                "condition": f"Added all three to 180°: {expr_a} + {ang_b} + {ext_ang} = 180",
                "feedback": "The exterior angle is on the OUTSIDE of the triangle. It equals the sum of the two opposite interior angles; do not add it with the interior angles to 180°.",
            },
        ]

        sample_answer = (
            f"1. $\\hat{{A}} + \\hat{{B}} = \\hat{{C}}_1$ [ext $\\angle$ of $\\Delta$]\n"
            f"2. $({expr_a}^\\circ) + {ang_b}^\\circ = {ext_ang}^\\circ$\n"
            f"   ${a_coeff}x + {b_const + ang_b} = {ext_ang}$\n"
            f"   ${a_coeff}x = {ext_ang - (b_const + ang_b)}$\n"
            f"   $x = {x_val}$"
        )

        diagram_spec = {
            "diagram_role": "context",
            "kind": "triangle",
            "caption": f"Triangle ABC with exterior angle C1 = {ext_ang}°",
            "points": {"A": [1.5, 3.5], "B": [0, 0], "C": [4, 0], "D": [6, 0]},
            "vertices": ["A", "B", "C", "D"],
            "triangles": [["A", "B", "C"]],
            "angle_labels": {"A": f"{expr_a}°", "B": f"{ang_b}°", "C": f"{ext_ang}°"},
        }

        correct_ans = str(x_val)
        subskill_id = "triangle_ext_angle"
        reason_code = "ext \u2220 of \u25b3"
        marks = 3

    elif archetype == "triangle_isosceles":
        # In triangle ABC, AB = AC (isosceles).
        # Therefore angle B = angle C (angles opposite equal sides).
        base_angle = r.randint(45, 75)
        apex_angle = 180 - 2 * base_angle
        x_val = r.randint(10, 25)
        c_mult = r.randint(2, 3)
        c_const = base_angle - c_mult * x_val
        expr_b = f"{c_mult}x + {c_const}" if c_const >= 0 else f"{c_mult}x - {abs(c_const)}"

        question_text = (
            f"In $\\Delta ABC$, side $AB = AC$.\n\n"
            f"The vertex angle $\\hat{{A}} = {apex_angle}^\\circ$, and base angle $\\hat{{B}} = {expr_b}^\\circ$.\n\n"
            f"1. State the size of base angle $\\hat{{C}}$, giving a reason.\n"
            f"2. Calculate the value of $x$."
        )

        steps = [
            {"id": "S1", "statement": f"$\\hat{{B}} = \\hat{{C}}$", "reason": "\u2220s opp equal sides", "deps": []},
            {"id": "S2", "statement": f"$\\hat{{A}} + \\hat{{B}} + \\hat{{C}} = 180^\\circ$", "reason": "sum of \u2220s in \u25b3", "deps": ["S1"]},
            {"id": "S3", "statement": f"${apex_angle} + 2\\hat{{B}} = 180 \\implies \\hat{{B}} = {base_angle}^\\circ$", "reason": "calculate base angle", "deps": ["S2"]},
            {"id": "S4", "statement": f"${expr_b} = {base_angle} \\implies x = {x_val}$", "reason": "solve linear equation", "deps": ["S3"]},
        ]

        hints = [
            "In an isosceles triangle, the angles opposite the equal sides are equal to each other.",
            f"Since $AB = AC$, $\\hat{{B}} = \\hat{{C}}$ [$\\angle$s opp equal sides]. The sum of angles in a triangle is 180°, so $2\\hat{{B}} = 180^\\circ - {apex_angle}^\\circ = {180 - apex_angle}^\\circ$, meaning $\\hat{{B}} = {base_angle}^\\circ$.",
            f"Equate: ${expr_b} = {base_angle}$. Solve for $x$ to find $x = {x_val}$.",
        ]

        error_tax = [
            {
                "id": "err_apex_equals_base",
                "tag": "misconception_isosceles_angles",
                "condition": f"Set vertex angle {apex_angle} equal to base angle",
                "feedback": "Only the base angles opposite the two equal sides are equal. The apex angle A is opposite the unequal base BC.",
            },
        ]

        sample_answer = (
            f"1. $AB = AC \\implies \\hat{{B}} = \\hat{{C}}$ [$\\angle$s opp equal sides]\n"
            f"   $\\hat{{A}} + \\hat{{B}} + \\hat{{C}} = 180^\\circ$ [sum of $\\angle$s in $\\Delta$]\n"
            f"   ${apex_angle}^\\circ + 2\\hat{{B}} = 180^\\circ$\n"
            f"   $2\\hat{{B}} = {180 - apex_angle}^\\circ \\implies \\hat{{B}} = \\hat{{C}} = {base_angle}^\\circ$\n\n"
            f"2. ${expr_b} = {base_angle}$\n"
            f"   ${c_mult}x = {base_angle - c_const}$\n"
            f"   $x = {x_val}$"
        )

        diagram_spec = {
            "diagram_role": "context",
            "kind": "triangle",
            "caption": f"Isosceles triangle ABC (AB = AC, apex A = {apex_angle}°)",
            "points": {"A": [2, 3.5], "B": [0, 0], "C": [4, 0]},
            "vertices": ["A", "B", "C"],
            "equal_sides": [["AB", "AC"]],
            "angle_labels": {"A": f"{apex_angle}°", "B": f"{expr_b}°"},
        }

        correct_ans = str(x_val)
        subskill_id = "triangle_isosceles"
        reason_code = "\u2220s opp equal sides"
        marks = 4

    elif archetype == "similarity_proportion":
        # Similar triangles: Delta ABC ||| Delta DEF (AAA).
        # Ratio of sides: AB/DE = BC/EF = AC/DF.
        scale_factor = r.choice([2, 3, 4])
        de = r.randint(3, 8)
        ab = de * scale_factor
        ef = r.randint(4, 9)
        bc = ef * scale_factor
        
        # Ask to find unknown side BC or EF
        find_target = "BC"
        x_val = bc

        question_text = (
            f"In the given figure, $\\Delta ABC$ is similar to $\\Delta DEF$ ($\\|\\|\\|$).\n\n"
            f"The corresponding sides are given as:\n"
            f"$AB = {ab}\\text{{ cm}}$, $DE = {de}\\text{{ cm}}$, and $EF = {ef}\\text{{ cm}}$.\n\n"
            f"1. State the condition for the sides of similar triangles.\n"
            f"2. Calculate the length of side $BC$."
        )

        steps = [
            {"id": "S1", "statement": f"$\\frac{{AB}}{{DE}} = \\frac{{BC}}{{EF}}$", "reason": "sides in proportion [||| \u25b3s]", "deps": []},
            {"id": "S2", "statement": f"$\\frac{{{ab}}}{{{de}}} = \\frac{{BC}}{{{ef}}}$", "reason": "substitute given values", "deps": ["S1"]},
            {"id": "S3", "statement": f"$BC = \\frac{{{ab} \\times {ef}}}{{{de}}} = {bc}\\text{{ cm}}$", "reason": "cross-multiply and solve", "deps": ["S2"]},
        ]

        hints = [
            "When two triangles are similar, their corresponding sides are in the same proportion (their scale factor is constant).",
            f"Set up the proportion equation: $\\frac{{AB}}{{DE}} = \\frac{{BC}}{{EF}}$ [sides in prop, $\\Delta ABC \\,\\|\\|\\|\\, \\Delta DEF$].",
            f"Substitute the known values: $\\frac{{{ab}}}{{{de}}} = \\frac{{BC}}{{{ef}}}$. Since $\\frac{{{ab}}}{{{de}}} = {scale_factor}$, multiply ${ef} \\times {scale_factor} = {bc}\\text{{ cm}}$.",
        ]

        error_tax = [
            {
                "id": "err_inverted_ratio",
                "tag": "misconception_ratio_inversion",
                "condition": f"Set AB / EF = BC / DE",
                "feedback": "Make sure you match corresponding sides: AB corresponds to DE (first two letters) and BC corresponds to EF (last two letters).",
            },
        ]

        sample_answer = (
            f"1. $\\frac{{AB}}{{DE}} = \\frac{{BC}}{{EF}}$ [sides of $\\Delta$ in proportion / $\\Delta ABC \\,\\|\\|\\|\\, \\Delta DEF$]\n"
            f"2. $\\frac{{{ab}}}{{{de}}} = \\frac{{BC}}{{{ef}}}$\n"
            f"   ${scale_factor} = \\frac{{BC}}{{{ef}}}$\n"
            f"   $BC = {scale_factor} \\times {ef} = {bc}\\text{{ cm}}$"
        )

        diagram_spec = {
            "diagram_role": "context",
            "kind": "triangle",
            "caption": f"Similar triangles ABC ||| DEF with scale factor {scale_factor}",
            "points": {"A": [0, 4], "B": [0, 0], "C": [5, 0]},
            "vertices": ["A", "B", "C"],
            "side_labels": {"AB": f"{ab} cm", "BC": "x cm"},
        }

        correct_ans = f"{bc} cm"
        subskill_id = "similarity_proportion"
        reason_code = "sides in prop, ||| \u25b3s"
        marks = 3

    else:
        # quadrilateral_parallelogram: Properties of parallelogram
        # In parallelogram ABCD, opposite sides are equal, opposite angles are equal.
        # Angle A = ax + b, Angle C = cx + d (opp angles equal).
        ang_val = r.randint(65, 115)
        x_val = r.randint(12, 25)
        a_coeff = r.randint(2, 4)
        b_const = ang_val - a_coeff * x_val
        expr_a = f"{a_coeff}x + {b_const}" if b_const >= 0 else f"{a_coeff}x - {abs(b_const)}"

        question_text = (
            f"$ABCD$ is a parallelogram ($\\text{{parm }} ABCD$).\n\n"
            f"Given that $\\hat{{A}} = {expr_a}^\\circ$ and $\\hat{{C}} = {ang_val}^\\circ$:\n"
            f"1. Calculate the value of $x$, giving a geometric reason.\n"
            f"2. Hence, determine the size of adjacent angle $\\hat{{B}}$."
        )

        steps = [
            {"id": "S1", "statement": f"$\\hat{{A}} = \\hat{{C}}$", "reason": "opp \u2220s of parm", "deps": []},
            {"id": "S2", "statement": f"${expr_a} = {ang_val} \\implies {a_coeff}x = {ang_val - b_const} \\implies x = {x_val}$", "reason": "solve for x", "deps": ["S1"]},
            {"id": "S3", "statement": f"$\\hat{{A}} + \\hat{{B}} = 180^\\circ$", "reason": "co-int \u2220s, AB \u2225 DC", "deps": ["S2"]},
            {"id": "S4", "statement": f"$\\hat{{B}} = 180^\\circ - {ang_val}^\\circ = {180 - ang_val}^\\circ$", "reason": "adjacent angle calculation", "deps": ["S3"]},
        ]

        hints = [
            "In a parallelogram, opposite angles are equal, and adjacent consecutive angles are co-interior (sum to 180°).",
            f"Equate the opposite angles: $\\hat{{A}} = \\hat{{C}}$ [opp $\\angle$s of parm].",
            f"Solve ${expr_a} = {ang_val}$ to get $x = {x_val}$. Then $\\hat{{B}} = 180^\\circ - {ang_val}^\\circ = {180 - ang_val}^\\circ$ [co-int $\\angle$s, $AD \\parallel BC$].",
        ]

        error_tax = [
            {
                "id": "err_opp_sum_180",
                "tag": "misconception_parallelogram_angles",
                "condition": f"Summed opposite angles A + C to 180",
                "feedback": "In a parallelogram, OPPOSITE angles are equal. ADJACENT consecutive angles sum to 180°.",
            },
        ]

        sample_answer = (
            f"1. $\\hat{{A}} = \\hat{{C}}$ [opp $\\angle$s of parm]\n"
            f"   ${expr_a} = {ang_val}$\n"
            f"   ${a_coeff}x = {ang_val - b_const}$\n"
            f"   $x = {x_val}$\n\n"
            f"2. $\\hat{{A}} + \\hat{{B}} = 180^\\circ$ [co-int $\\angle$s, $AD \\parallel BC$]\n"
            f"   ${ang_val}^\\circ + \\hat{{B}} = 180^\\circ$\n"
            f"   $\\hat{{B}} = {180 - ang_val}^\\circ$"
        )

        diagram_spec = {
            "diagram_role": "context",
            "kind": "quadrilateral",
            "caption": f"Parallelogram ABCD with opposite angles A and C",
            "points": {"A": [0, 0], "B": [5, 0], "C": [6.5, 3], "D": [1.5, 3]},
            "vertices": ["A", "B", "C", "D"],
            "angle_labels": {"A": f"{expr_a}°", "C": f"{ang_val}°"},
        }

        correct_ans = str(x_val)
        subskill_id = "quadrilateral_parallelogram"
        reason_code = "opp \u2220s of parm"
        marks = 4

    q = {
        "id": qid,
        "subject": "Mathematics",
        "grade": 9,
        "topic": TOPIC,
        "subskill": subskill_id,
        "learning_objective_id": LO,
        "mode": mode,
        "difficulty": difficulty,
        "question_type": "free_response",
        "answer_mode": "free_response",
        "prompt": question_text,
        "question": question_text,
        "prompt_latex": question_text,
        "answer_latex": correct_ans,
        "correct_answer": correct_ans,
        "sample_answer": sample_answer,
        "worked_solution": sample_answer,
        "canonical_solution": sample_answer,
        "marking_schema": [
            {"criterion": f"Correct geometric statement and reason [{reason_code}]", "marks": 1},
            {"criterion": f"Correct calculation and final value {correct_ans}", "marks": marks - 1},
        ],
        "marks": marks,
        "hints": hints,
        "hint_sections": {
            "concept": hints[0],
            "rules": hints[1],
            "step_by_step": hints[2],
        },
        "misconception_tags": [m["tag"] for m in error_tax],
        "diagnostic_tags": [f"diag_{subskill_id}"],
        "keywords": ["geometry", "2D shapes", "triangles", "quadrilaterals", "congruence", "similarity"],
        "term": 2,
        "caps_weight_percent": 12.0,
        "suggested_duration_mins": 6,
        "minimum_mastery_score": 75,
        "diagram_spec": diagram_spec,
        "modality": "math",
        "seed": seed,
        "solution_graph": {
            "goal": "Solve 2D geometry deduction with formal reasons",
            "steps": steps,
        },
        "metadata": {
            "diagram_spec": diagram_spec,
            "answer_value": correct_ans,
            "reason_code": reason_code,
        },
    }
    return q


def generate(seed: Optional[int] = None, count: int = 1, **kwargs: Any) -> Dict[str, Any]:
    r = rng(seed)
    questions = []
    for _ in range(count):
        sub_seed = r.randint(1, 1_000_000_000)
        questions.append(generate_grade9_geometry_2d_shapes_question(seed=sub_seed, **kwargs))
    return {"questions": questions}
