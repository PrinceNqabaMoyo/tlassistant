"""Grade 9 Mathematics — Construction of Geometric Figures Generator (Deterministic 6-Pillar Contract).

Curriculum Alignment:
- Grade 9 Term 3: Construction of geometric figures
- South African National Curriculum Standards (Senior Phase Mathematics)
- Compass and straight-edge constructions:
  * Angle bisector calculations & algebraic properties
  * Perpendicular bisector properties & equidistant points
  * Special construction angles (60°, 30°, 90°, 45°) and combination angles (75°, 105°, 135°)
  * Triangle construction conditions & Triangle Inequality Theorem (a + b > c)
  * Naming geometric centres (circumcentre from perpendicular bisectors, incentre from angle bisectors)

6 Pillars:
- Deterministic seed generation with zero LLM authority
- Directed solution graph with dependency tracking
- Adaptive deconstruction (atomic elementary sub-drills on error)
- Rich 3-tier hints (Conceptual, Procedural with construction rule, Concrete Step-by-Step with actual numbers)
- Misconception-targeted error taxonomy
- Native DiagramRenderer specs
"""
from __future__ import annotations

import math
import random
import uuid
from typing import Any, Dict, List, Optional

from app.utils.grade9_mathematics._math_common import rng

TOPIC = "grade9_math_construction_of_geometric_figures"
LO = "math9_construction_geometric_figures"


def generate_grade9_construction_question(
    seed: Optional[int] = None,
    difficulty: str = "medium",
    mode: str = "compound",
    subskill: Optional[str] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    r = rng(seed)

    archetype_choices = [
        "triangle_inequality",
        "angle_bisector_algebra",
        "special_construction_angles",
        "perpendicular_bisector_property",
    ]

    selected_subskill = subskill or mode
    if selected_subskill in archetype_choices:
        archetype = selected_subskill
    else:
        archetype = r.choice(archetype_choices)

    qid = f"g9_construct_{seed or r.randint(1000, 9999)}_{uuid.uuid4().hex[:6]}"

    if archetype == "triangle_inequality":
        # Can a triangle be constructed with side lengths a, b, c?
        # Triangle Inequality Theorem: a + b > c for all three pairs.
        is_valid = r.choice([True, False])
        if is_valid:
            a = r.randint(5, 12)
            b = r.randint(5, 12)
            # c must be between |a-b|+1 and a+b-1
            min_c = abs(a - b) + 1
            max_c = a + b - 1
            c = r.randint(min_c, max_c)
            # Sort for clean display
            sides = sorted([a, b, c])
            s1, s2, s3 = sides
            ans_str = "Yes"
            explanation = (
                f"Check the two shorter sides: ${s1} + {s2} = {s1 + s2}$. "
                f"Since ${s1 + s2} > {s3}$, the sum of the two shorter sides is strictly greater than the longest side. "
                f"Therefore, a triangle CAN be constructed."
            )
        else:
            s1 = r.randint(3, 7)
            s2 = r.randint(3, 7)
            # c is >= s1 + s2
            s3 = s1 + s2 + r.choice([0, 1, 2, 3])
            ans_str = "No"
            explanation = (
                f"Check the two shorter sides: ${s1} + {s2} = {s1 + s2}$. "
                f"Since ${s1 + s2} \\le {s3}$, the two shorter sides cannot meet to form a vertex. "
                f"Therefore, a triangle CANNOT be constructed."
            )

        question_text = (
            f"A learner attempts to construct a triangle with side lengths "
            f"${s1}\\text{{ cm}}$, ${s2}\\text{{ cm}}$, and ${s3}\\text{{ cm}}$ using a ruler and a pair of compasses.\n\n"
            f"1. Is it geometrically possible to construct this triangle? (State 'Yes' or 'No').\n"
            f"2. Justify your answer using the Triangle Inequality Theorem."
        )

        steps = [
            {"id": "S1", "statement": f"Identify the two shorter sides: ${s1}\\text{{ cm}}$ and ${s2}\\text{{ cm}}$", "reason": "order sides", "deps": []},
            {"id": "S2", "statement": f"Calculate sum of two shorter sides: ${s1} + {s2} = {s1 + s2}\\text{{ cm}}$", "reason": "arithmetic", "deps": ["S1"]},
            {"id": "S3", "statement": f"Compare with longest side ${s3}\\text{{ cm}}$: ${s1 + s2} {'>' if is_valid else '\\le'} {s3}$", "reason": "Triangle Inequality Theorem", "deps": ["S2"]},
            {"id": "S4", "statement": f"Conclusion: {ans_str}", "reason": "constructibility criterion", "deps": ["S3"]},
        ]

        hints = [
            "The Triangle Inequality Theorem states that the sum of the lengths of any two sides of a triangle must be strictly greater than the third side.",
            f"Add the two shorter sides together: ${s1} + {s2} = {s1 + s2}\\text{{ cm}}$. Compare this sum to the longest side ${s3}\\text{{ cm}}$.",
            f"If the sum is greater than {s3}, the arcs will intersect and the answer is 'Yes'. If the sum is less than or equal to {s3}, the arcs will never meet and the answer is 'No'.",
        ]

        error_tax = [
            {
                "id": "err_equality_sufficient",
                "tag": "misconception_degenerate_triangle",
                "condition": f"Claimed Yes when {s1} + {s2} == {s3}",
                "feedback": "When the sum of the two shorter sides equals the third side, the three points form a flat line segment, not a triangle. The sum must be strictly greater.",
            },
        ]

        sample_answer = (
            f"1. {ans_str}\n"
            f"2. {explanation}"
        )

        diagram_spec = {
            "diagram_role": "context",
            "kind": "triangle",
            "caption": f"Side lengths: {s1} cm, {s2} cm, {s3} cm",
            "points": {"A": [0, 0], "B": [s3 / 2, 2], "C": [s3, 0]},
            "vertices": ["A", "B", "C"],
            "side_labels": {"AB": f"{s1} cm", "BC": f"{s2} cm", "AC": f"{s3} cm"},
        }

        correct_ans = ans_str
        subskill_id = "triangle_inequality"
        reason_code = "Triangle Inequality Theorem (a + b > c)"
        marks = 3

    elif archetype == "angle_bisector_algebra":
        # Compass construction: Angle bisector cuts angle ABC into two equal halves.
        # Ray BD bisects angle ABC. Angle ABD = ax + b, Angle DBC = total / 2.
        half_ang = r.randint(25, 55)
        total_ang = 2 * half_ang
        x_val = r.randint(10, 25)
        a_coeff = r.randint(2, 3)
        b_const = half_ang - a_coeff * x_val
        expr_half = f"{a_coeff}x + {b_const}" if b_const >= 0 else f"{a_coeff}x - {abs(b_const)}"

        question_text = (
            f"Ray $BD$ is constructed using a compass and straight edge to bisect angle $A\\hat{{B}}C$.\n\n"
            f"Given that the total angle $A\\hat{{B}}C = {total_ang}^\\circ$ and $A\\hat{{B}}D = {expr_half}^\\circ$:\n"
            f"1. State the geometric definition and effect of an angle bisector.\n"
            f"2. Calculate the value of $x$."
        )

        steps = [
            {"id": "S1", "statement": f"$A\\hat{{B}}D = \\frac{{1}}{{2}} A\\hat{{B}}C$", "reason": "BD bisects \u2220ABC", "deps": []},
            {"id": "S2", "statement": f"${expr_half} = \\frac{{{total_ang}}}{{2}} = {half_ang}^\\circ$", "reason": "substitute given values", "deps": ["S1"]},
            {"id": "S3", "statement": f"${a_coeff}x = {half_ang - b_const} \\implies x = {x_val}$", "reason": "solve linear equation", "deps": ["S2"]},
        ]

        hints = [
            "An angle bisector is a line or ray that divides an angle into two congruent (equal) angles.",
            f"Since $BD$ bisects $A\\hat{{B}}C$, each half equals half of {total_ang}°, so $A\\hat{{B}}D = {half_ang}^\\circ$.",
            f"Equate: ${expr_half} = {half_ang}$. Subtract {b_const} and divide by {a_coeff} to find $x = {x_val}$.",
        ]

        error_tax = [
            {
                "id": "err_bisector_adds_to_total",
                "tag": "misconception_bisector_vs_complementary",
                "condition": f"Set {expr_half} = {total_ang}",
                "feedback": "The bisector divides the total angle in half. The half angle must equal total / 2, not the full total angle.",
            },
        ]

        sample_answer = (
            f"1. An angle bisector divides an angle into two exactly equal halves.\n"
            f"   $A\\hat{{B}}D = \\frac{{1}}{{2}} A\\hat{{B}}C = \\frac{{{total_ang}^\\circ}}{{2}} = {half_ang}^\\circ$\n\n"
            f"2. ${expr_half} = {half_ang}$\n"
            f"   ${a_coeff}x = {half_ang - b_const}$\n"
            f"   $x = {x_val}$"
        )

        diagram_spec = {
            "diagram_role": "context",
            "kind": "angle_diagram",
            "caption": f"Angle ABC = {total_ang}° bisected by ray BD",
            "lines": [
                {"from": [0, 0], "to": [4, 0], "label": "BC"},
                {"from": [0, 0], "to": [2.5, 3.5], "label": "BA"},
                {"from": [0, 0], "to": [3.5, 2], "label": "BD"},
            ],
            "angles": [
                {"vertex": [0, 0], "label": f"{expr_half}°", "radius": 0.9},
                {"vertex": [0, 0], "label": f"{half_ang}°", "radius": 1.4},
            ],
        }

        correct_ans = str(x_val)
        subskill_id = "angle_bisector_algebra"
        reason_code = "definition of angle bisector"
        marks = 3

    elif archetype == "special_construction_angles":
        # How to construct 45°, 30°, 75°, 105°, 135° using compass & ruler
        target_angle = r.choice([30, 45, 75, 105, 135])
        if target_angle == 30:
            construction_recipe = "Construct an equilateral triangle (or 60° angle), then construct the angle bisector of the 60° angle (60° / 2 = 30°)."
        elif target_angle == 45:
            construction_recipe = "Construct a perpendicular line (90° angle), then bisect the 90° angle (90° / 2 = 45°)."
        elif target_angle == 75:
            construction_recipe = "Construct a 60° angle and a 90° angle on the same vertex. The angle between them is 30°. Bisect this 30° angle to get 15°, and add 60° + 15° = 75°."
        elif target_angle == 105:
            construction_recipe = "Construct a 90° angle and a 120° angle on the same vertex. Bisect the 30° angle between them to get 15°, giving 90° + 15° = 105°."
        else:  # 135
            construction_recipe = "Construct a 90° angle, then bisect the adjacent supplementary 90° angle on the straight line (90° + 45° = 135°)."

        question_text = (
            f"A Grade 9 learner needs to construct an angle of exactly ${target_angle}^\\circ$ "
            f"using ONLY a pair of compasses and a straight edge (ruler), without using a protractor.\n\n"
            f"Explain clearly, in numbered sequential steps, how this angle of ${target_angle}^\\circ$ "
            f"can be constructed."
        )

        steps = [
            {"id": "S1", "statement": f"Identify base special angle (60° or 90°)", "reason": "standard compass arc construction", "deps": []},
            {"id": "S2", "statement": f"Apply angle bisection to obtain required increment", "reason": "compass angle bisector", "deps": ["S1"]},
            {"id": "S3", "statement": f"Combine components: target ${target_angle}^\\circ$", "reason": "angle addition", "deps": ["S2"]},
        ]

        hints = [
            "Remember that with a compass, you can directly construct 60° (using equal radius arcs from an equilateral triangle) and 90° (perpendicular bisector of a line segment).",
            f"To get {target_angle}°, think about how {target_angle}° relates to 60°, 90°, or 180°, and how angle bisectors divide angles in half.",
            f"Procedure for {target_angle}°: {construction_recipe}",
        ]

        error_tax = [
            {
                "id": "err_use_protractor",
                "tag": "misconception_tool_violation",
                "condition": "Used a protractor to measure the angle",
                "feedback": "Geometric construction strictly requires a ruler (straight edge) and compass only. Using a protractor is drawing, not constructing.",
            },
        ]

        sample_answer = (
            f"Step-by-step compass construction for ${target_angle}^\\circ$:\n"
            f"{construction_recipe}"
        )

        diagram_spec = {
            "diagram_role": "context",
            "kind": "angle_diagram",
            "caption": f"Ruler & compass construction of {target_angle}°",
            "lines": [
                {"from": [0, 0], "to": [4, 0], "label": "Base arm"},
                {"from": [0, 0], "to": [4 * math.cos(math.radians(target_angle)), 4 * math.sin(math.radians(target_angle))], "label": f"{target_angle}° arm"},
            ],
            "angles": [{"vertex": [0, 0], "label": f"{target_angle}°", "radius": 1.2}],
        }

        correct_ans = f"{target_angle}°"
        subskill_id = "special_construction_angles"
        reason_code = "ruler & compass construction"
        marks = 3

    else:
        # perpendicular_bisector_property
        # Perpendicular bisector of AB. Any point P on the bisector satisfies PA = PB.
        # If PA = 3x - 4 and PB = 2x + 6, find x and PA.
        x_val = r.randint(5, 15)
        a_coeff = r.randint(3, 4)
        c_coeff = 2
        d_const = r.randint(5, 15)
        b_const = (a_coeff - c_coeff) * x_val - d_const
        pa_len = a_coeff * x_val - b_const

        question_text = (
            f"Line $XY$ is the perpendicular bisector of line segment $AB$.\n\n"
            f"Point $P$ lies anywhere on line $XY$. The distances from $P$ to the endpoints are given as:\n"
            f"$PA = {a_coeff}x - {b_const}\\text{{ cm}}$ and $PB = {c_coeff}x + {d_const}\\text{{ cm}}$.\n\n"
            f"1. What is the geometric relationship between $PA$ and $PB$?\n"
            f"2. Calculate the value of $x$ and the length of $PA$."
        )

        steps = [
            {"id": "S1", "statement": f"$PA = PB$", "reason": "P lies on perp bisector of AB", "deps": []},
            {"id": "S2", "statement": f"${a_coeff}x - {b_const} = {c_coeff}x + {d_const}$", "reason": "equate equidistant segments", "deps": ["S1"]},
            {"id": "S3", "statement": f"${a_coeff - c_coeff}x = {d_const + b_const} \\implies x = {x_val}$", "reason": "solve for x", "deps": ["S2"]},
            {"id": "S4", "statement": f"$PA = {a_coeff}({x_val}) - {b_const} = {pa_len}\\text{{ cm}}$", "reason": "calculate length", "deps": ["S3"]},
        ]

        hints = [
            "Any point lying on the perpendicular bisector of a line segment is equidistant from the two endpoints of the segment.",
            f"Therefore, $PA = PB$. Set up the equation: ${a_coeff}x - {b_const} = {c_coeff}x + {d_const}$.",
            f"Rearrange: ${a_coeff - c_coeff}x = {d_const + b_const}$, giving $x = {x_val}$. Then $PA = {a_coeff}({x_val}) - {b_const} = {pa_len}\\text{{ cm}}$.",
        ]

        error_tax = [
            {
                "id": "err_perp_bisector_confused",
                "tag": "misconception_bisector_endpoints",
                "condition": "Assumed PA and PB sum to 180 or length of AB",
                "feedback": "Points on a perpendicular bisector are equidistant from the endpoints: PA = PB.",
            },
        ]

        sample_answer = (
            f"1. $PA = PB$ (Any point on the perpendicular bisector of a segment is equidistant from its endpoints).\n"
            f"2. ${a_coeff}x - {b_const} = {c_coeff}x + {d_const}$\n"
            f"   ${a_coeff - c_coeff}x = {d_const + b_const}$\n"
            f"   $x = {x_val}$\n"
            f"   $PA = {a_coeff}({x_val}) - {b_const} = {pa_len}\\text{{ cm}}$"
        )

        diagram_spec = {
            "diagram_role": "context",
            "kind": "triangle",
            "caption": "P on perpendicular bisector of AB (PA = PB)",
            "points": {"A": [-3, 0], "B": [3, 0], "P": [0, 4], "M": [0, 0]},
            "vertices": ["A", "B", "P"],
            "equal_sides": [["PA", "PB"]],
            "side_labels": {"PA": f"{pa_len} cm", "PB": f"{pa_len} cm"},
            "right_angle_at": "M",
        }

        correct_ans = str(x_val)
        subskill_id = "perpendicular_bisector_property"
        reason_code = "equidistant from endpoints on perp bisector"
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
            {"criterion": f"Correct geometric theorem/property [{reason_code}]", "marks": 1},
            {"criterion": f"Correct calculation and answer {correct_ans}", "marks": marks - 1},
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
        "keywords": ["construction", "compass", "ruler", "bisector", "triangle inequality", "perpendicular"],
        "term": 3,
        "caps_weight_percent": 8.0,
        "suggested_duration_mins": 5,
        "minimum_mastery_score": 75,
        "diagram_spec": diagram_spec,
        "modality": "math",
        "seed": seed,
        "solution_graph": {
            "goal": "Solve geometric construction problem",
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
        questions.append(generate_grade9_construction_question(seed=sub_seed, **kwargs))
    return {"questions": questions}
