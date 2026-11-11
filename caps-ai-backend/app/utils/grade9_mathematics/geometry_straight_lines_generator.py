"""Grade 9 Mathematics — Geometry of Straight Lines Generator (Deterministic 6-Pillar Contract).

Curriculum Alignment:
- Grade 9 Term 2: Geometry of straight lines
- South African National Curriculum Standards (Senior Phase Mathematics)
- Angle relationships on intersecting straight lines (vertically opposite, supplementary adjacent angles on a line, angles around a point)
- Parallel lines cut by a transversal: corresponding angles (F-shape), alternate angles (Z-shape), co-interior angles (C/U-shape)
- Two-column formal Euclidean deductions [Statement | Reason]
- Algebraic angle equations solving for unknown variable x and angle size

6 Pillars:
- Deterministic seed generation with zero LLM authority
- Directed solution graph with dependency tracking
- Adaptive deconstruction (atomic elementary sub-drills on error)
- Rich 3-tier hints (Conceptual, Procedural with geometry theorem, Concrete Step-by-Step with actual numbers)
- Misconception-targeted error taxonomy
- Native DiagramRenderer specs (kind: 'parallel_transversal' / 'angle_diagram')
"""
from __future__ import annotations

import random
import uuid
from typing import Any, Dict, List, Optional

from app.utils.grade9_mathematics._math_common import rng

TOPIC = "grade9_math_geometry_of_straight_lines"
LO = "math9_geometry_straight_lines"


def generate_grade9_geometry_straight_lines_question(
    seed: Optional[int] = None,
    difficulty: str = "medium",
    mode: str = "compound",
    subskill: Optional[str] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    r = rng(seed)

    archetype_choices = [
        "vert_opp",
        "straight_line_adj",
        "parallel_alternate",
        "parallel_corresponding",
        "parallel_cointerior",
        "compound_algebraic_transversal",
    ]

    selected_subskill = subskill or mode
    if selected_subskill in archetype_choices:
        archetype = selected_subskill
    else:
        archetype = r.choice(archetype_choices)

    qid = f"g9_geom_lines_{seed or r.randint(1000, 9999)}_{uuid.uuid4().hex[:6]}"

    if archetype == "vert_opp":
        x_val = r.randint(15, 35)
        a = r.randint(2, 4)
        c = 1
        d = (a - c) * x_val + r.randint(5, 20)
        b = d - (a - c) * x_val
        angle_val = a * x_val + b

        question_text = (
            f"Straight lines $AB$ and $CD$ intersect at point $O$.\n\n"
            f"If $\\hat{{O}}_1 = {a}x + {b}^\\circ$ and $\\hat{{O}}_3 = {angle_val}^\\circ$ are vertically opposite angles, "
            f"calculate the value of $x$ and give a reason for your statement."
        )

        steps = [
            {"id": "S1", "statement": f"${a}x + {b} = {angle_val}$", "reason": "vert opp \u2220s", "deps": []},
            {"id": "S2", "statement": f"${a}x = {angle_val - b}$", "reason": f"subtract {b}", "deps": ["S1"]},
            {"id": "S3", "statement": f"$x = {x_val}$", "reason": f"divide by {a}", "deps": ["S2"]},
        ]

        hints = [
            "Vertically opposite angles are formed when two straight lines intersect and cross. They are always equal.",
            f"Write the formal statement: $\\hat{{O}}_1 = \\hat{{O}}_3$ [vert opp $\\angle$s]. Then set up the linear equation: ${a}x + {b} = {angle_val}$.",
            f"Subtract {b} from {angle_val} to get ${a}x = {angle_val - b}$. Then divide by {a} to find $x = {x_val}$.",
        ]

        error_tax = [
            {
                "id": "err_wrong_reason",
                "tag": "misconception_theorem_confusion",
                "condition": "Used adjacent angles on straight line summing to 180 instead of equating",
                "feedback": "Vertically opposite angles are opposite each other across the intersection, so they are equal. Do not add them to 180°.",
            },
            {
                "id": "err_algebra_sign",
                "tag": "misconception_sign_error",
                "condition": f"Added {b} instead of subtracting",
                "feedback": f"When transposing +{b} across the equals sign, subtract {b} from {angle_val}.",
            },
        ]

        sample_answer = (
            f"$\\hat{{O}}_1 = \\hat{{O}}_3$ [vert opp $\\angle$s]\n"
            f"${a}x + {b} = {angle_val}$\n"
            f"${a}x = {angle_val - b}$\n"
            f"$x = {x_val}$"
        )

        diagram_spec = {
            "diagram_role": "context",
            "kind": "angle_diagram",
            "caption": "Intersecting straight lines AB and CD",
            "lines": [
                {"from": [-3, -2], "to": [3, 2], "label": "AB"},
                {"from": [-3, 2], "to": [3, -2], "label": "CD"},
            ],
            "angles": [
                {"vertex": [0, 0], "label": f"{a}x + {b}°", "radius": 0.8},
                {"vertex": [0, 0], "label": f"{angle_val}°", "radius": 0.8},
            ],
        }

        correct_ans = str(x_val)
        subskill_id = "elementary_vert_opp"
        reason_code = "vert opp \u2220s"
        marks = 3

    elif archetype == "straight_line_adj":
        x_val = r.randint(12, 28)
        a = r.randint(2, 3)
        c = r.randint(1, 2)
        total_coeff = a + c
        needed_const = 180 - total_coeff * x_val
        b = r.randint(5, 20)
        d = needed_const - b
        ang2 = c * x_val + d

        question_text = (
            f"Point $P$ lies on the straight line $AB$. Ray $PC$ forms two adjacent angles:\n\n"
            f"$\\hat{{P}}_1 = {a}x + {b}^\\circ$ and $\\hat{{P}}_2 = {ang2}^\\circ$.\n\n"
            f"Calculate the value of $x$, stating the geometric reason."
        )

        steps = [
            {"id": "S1", "statement": f"$\\hat{{P}}_1 + \\hat{{P}}_2 = 180^\\circ$", "reason": "\u2220s on a str line", "deps": []},
            {"id": "S2", "statement": f"${a}x + {b + ang2} = 180$", "reason": "substitute and collect constants", "deps": ["S1"]},
            {"id": "S3", "statement": f"$x = {x_val}$", "reason": f"solve linear equation", "deps": ["S2"]},
        ]

        hints = [
            "Adjacent angles that lie together on a straight line are supplementary, meaning their sum is 180°.",
            f"Write the equation: $({a}x + {b}) + {ang2} = 180^\\circ$ [$\\angle$s on a str line].",
            f"Combine like terms: ${a}x + {b + ang2} = 180$. Subtract {b + ang2} from 180 to get ${a}x = {180 - (b + ang2)}$, then divide by {a} to get $x = {x_val}$.",
        ]

        error_tax = [
            {
                "id": "err_set_equal",
                "tag": "misconception_equal_vs_supplementary",
                "condition": f"Equated {a}x + {b} = {ang2}",
                "feedback": "These angles lie together on a straight line; they are not equal, they sum to 180°.",
            },
        ]

        sample_answer = (
            f"$\\hat{{P}}_1 + \\hat{{P}}_2 = 180^\\circ$ [$\\angle$s on a str line]\n"
            f"${a}x + {b}^\\circ + {ang2}^\\circ = 180^\\circ$\n"
            f"${a}x + {b + ang2} = 180$\n"
            f"${a}x = {180 - (b + ang2)}$\n"
            f"$x = {x_val}$"
        )

        diagram_spec = {
            "diagram_role": "context",
            "kind": "angle_diagram",
            "caption": "Adjacent angles on straight line AB",
            "points": {"A": [-3, 0], "P": [0, 0], "B": [3, 0], "C": [1.5, 2.6]},
            "lines": [
                {"from": [-3, 0], "to": [3, 0], "label": "AB"},
                {"from": [0, 0], "to": [1.5, 2.6], "label": "PC"},
            ],
            "angle_labels": {"P1": f"{a}x + {b}°", "P2": f"{ang2}°"},
        }

        correct_ans = str(x_val)
        subskill_id = "elementary_straight_line"
        reason_code = "\u2220s on a str line"
        marks = 3

    elif archetype in ("parallel_alternate", "parallel_corresponding", "parallel_cointerior"):
        given_deg = r.choice([45, 55, 65, 75, 110, 125, 130])

        if archetype == "parallel_alternate":
            target_deg = given_deg
            rel_name = "alternate angles"
            reason_code = "alt \u2220s, AB \u2225 CD"
            shape_cue = "Z-shape or N-shape"
        elif archetype == "parallel_corresponding":
            target_deg = given_deg
            rel_name = "corresponding angles"
            reason_code = "corr \u2220s, AB \u2225 CD"
            shape_cue = "F-shape"
        else:
            target_deg = 180 - given_deg
            rel_name = "co-interior angles"
            reason_code = "co-int \u2220s, AB \u2225 CD"
            shape_cue = "C-shape or U-shape"

        question_text = (
            f"In the given figure, line $AB$ is parallel to line $CD$ ($AB \\parallel CD$). "
            f"Transversal $EF$ intersects $AB$ at $G$ and $CD$ at $H$.\n\n"
            f"Given that $\\hat{{G}}_1 = {given_deg}^\\circ$, determine the size of $\\hat{{H}}_2$ "
            f"(which forms {rel_name} with $\\hat{{G}}_1$). State your geometric reason."
        )

        steps = [
            {"id": "S1", "statement": f"Identify parallel lines: $AB \\parallel CD$", "reason": "Given", "deps": []},
            {"id": "S2", "statement": f"Apply {rel_name} theorem", "reason": reason_code, "deps": ["S1"]},
            {"id": "S3", "statement": f"$\\hat{{H}}_2 = {target_deg}^\\circ$", "reason": reason_code, "deps": ["S2"]},
        ]

        hints = [
            f"Look for the {shape_cue} formed by the parallel lines $AB$ and $CD$ and the transversal.",
            f"Recall the theorem for {rel_name}: {'they are equal when lines are parallel' if archetype != 'parallel_cointerior' else 'they add up to 180° when lines are parallel'}.",
            f"State the full reason with the parallel line names: [{reason_code}]. Therefore, the angle is {target_deg}°.",
        ]

        error_tax = [
            {
                "id": "err_omitted_parallel_in_reason",
                "tag": "misconception_incomplete_reason",
                "condition": "Wrote reason without naming parallel lines",
                "feedback": "In Euclidean geometry, you must always specify which lines are parallel in the reason, e.g. [alt ∠s, AB ∥ CD].",
            },
        ]

        sample_answer = (
            f"$\\hat{{H}}_2 = {target_deg}^\\circ$ [{reason_code}]"
            if archetype != "parallel_cointerior"
            else f"$\\hat{{G}}_1 + \\hat{{H}}_2 = 180^\\circ$ [{reason_code}]\n"
                 f"${given_deg}^\\circ + \\hat{{H}}_2 = 180^\\circ$\n"
                 f"$\\hat{{H}}_2 = {target_deg}^\\circ$"
        )

        diagram_spec = {
            "diagram_role": "context",
            "kind": "parallel_transversal",
            "caption": f"Parallel lines AB || CD with transversal ({given_deg}°)",
            "line1_label": "AB",
            "line2_label": "CD",
            "transversal_label": "EF",
            "given_angle": given_deg,
            "given_position": "top_left_interior",
        }

        correct_ans = str(target_deg)
        subskill_id = f"elementary_{archetype}"
        marks = 2

    else:
        # compound_algebraic_transversal
        x_val = r.randint(15, 30)
        a = r.randint(2, 3)
        c = r.randint(2, 3)
        total_coeff = a + c
        needed_const = 180 - total_coeff * x_val
        b = r.randint(10, 25)
        d = needed_const - b
        ang1 = a * x_val + b

        question_text = (
            f"In the diagram, $AB \\parallel CD$ and $EF$ is a transversal cutting $AB$ at $P$ and $CD$ at $Q$.\n\n"
            f"The co-interior angles are given as $\\hat{{P}}_2 = {a}x + {b}^\\circ$ and $\\hat{{Q}}_1 = {c}x + {d}^\\circ$.\n\n"
            f"1. Set up an equation and solve for $x$, giving a geometric reason.\n"
            f"2. Hence, calculate the actual size of $\\hat{{P}}_2$."
        )

        steps = [
            {"id": "S1", "statement": f"$({a}x + {b}) + ({c}x + {d}) = 180^\\circ$", "reason": "co-int \u2220s, AB \u2225 CD", "deps": []},
            {"id": "S2", "statement": f"${total_coeff}x + {b + d} = 180$", "reason": "collect like terms", "deps": ["S1"]},
            {"id": "S3", "statement": f"$x = {x_val}$", "reason": "solve for x", "deps": ["S2"]},
            {"id": "S4", "statement": f"$\\hat{{P}}_2 = {ang1}^\\circ$", "reason": f"substitute x = {x_val}", "deps": ["S3"]},
        ]

        hints = [
            "Co-interior angles lie on the same side of the transversal between the two parallel lines. They add up to 180°.",
            f"Set up the equation: $({a}x + {b}) + ({c}x + {d}) = 180^\\circ$ [co-int $\\angle$s, $AB \\parallel CD$].",
            f"Simplify to ${total_coeff}x + {b + d} = 180$, which gives $x = {x_val}$. Then calculate $\\hat{{P}}_2 = {a}({x_val}) + {b} = {ang1}^\\circ$.",
        ]

        error_tax = [
            {
                "id": "err_cointerior_equal",
                "tag": "misconception_cointerior_equal",
                "condition": f"Equated {a}x + {b} = {c}x + {d}",
                "feedback": "Co-interior angles are not equal unless both are 90°. They sum to 180° when lines are parallel.",
            },
        ]

        sample_answer = (
            f"1. $({a}x + {b}^\\circ) + ({c}x + {d}^\\circ) = 180^\\circ$ [co-int $\\angle$s, $AB \\parallel CD$]\n"
            f"   ${total_coeff}x + {b + d} = 180$\n"
            f"   ${total_coeff}x = {180 - (b + d)}$\n"
            f"   $x = {x_val}$\n\n"
            f"2. $\\hat{{P}}_2 = {a}({x_val}) + {b}^\\circ = {ang1}^\\circ$"
        )

        diagram_spec = {
            "diagram_role": "context",
            "kind": "parallel_transversal",
            "caption": "Parallel lines AB || CD with co-interior angles",
            "line1_label": "AB",
            "line2_label": "CD",
            "transversal_label": "EF",
            "given_angle": ang1,
            "given_position": "top_right_interior",
        }

        correct_ans = str(ang1)
        subskill_id = "compound_algebraic_transversal"
        reason_code = "co-int \u2220s, AB \u2225 CD"
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
            {"criterion": f"Stating correct statement with reason [{reason_code}]", "marks": 1},
            {"criterion": f"Calculation to answer {correct_ans}", "marks": marks - 1},
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
        "keywords": ["geometry", "parallel lines", "transversal", "angles", "alternate", "corresponding", "co-interior"],
        "term": 2,
        "caps_weight_percent": 10.0,
        "suggested_duration_mins": 5,
        "minimum_mastery_score": 75,
        "diagram_spec": diagram_spec,
        "modality": "math",
        "seed": seed,
        "solution_graph": {
            "goal": "Solve geometric angle rider with reason",
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
        questions.append(generate_grade9_geometry_straight_lines_question(seed=sub_seed, **kwargs))
    return {"questions": questions}
