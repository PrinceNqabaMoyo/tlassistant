"""Grade 9 Mathematics — Theorem of Pythagoras in 2D & 3D (Deterministic 6-Pillar Generator).

Curriculum Alignment:
- Grade 9 Term 3: Theorem of Pythagoras
- South African National Curriculum Standards (Senior Phase Mathematics)
- In a right-angled triangle, the square on the hypotenuse is equal to the sum of the squares on the other two sides:
  c^2 = a^2 + b^2 [Pythagoras]
- Finding the hypotenuse: c = sqrt(a^2 + b^2)
- Finding a shorter side: a = sqrt(c^2 - b^2)
- Converse of Pythagoras Theorem: if a^2 + b^2 = c^2, then the angle opposite side c is 90° [Converse Pythagoras]
- Distance between two points in the Cartesian plane: d = sqrt((x2 - x1)^2 + (y2 - y1)^2)
- Space diagonal of a 3D rectangular box: d^2 = l^2 + b^2 + h^2

6 Pillars:
- Deterministic seed generation with zero LLM authority
- Directed solution graph with dependency tracking
- Adaptive deconstruction (atomic elementary sub-drills on error)
- Rich 3-tier hints (Conceptual, Procedural with formula, Concrete Step-by-Step with actual numbers)
- Misconception-targeted error taxonomy
- Native DiagramRenderer specs (kind: 'right_triangle')
"""
from __future__ import annotations

import math
import random
import uuid
from typing import Any, Dict, List, Optional

from app.utils.grade9_mathematics._math_common import rng

TOPIC = "grade9_math_theorem_of_pythagoras"
LO = "g9_math_pythagoras"

# Canonical Pythagorean triples (a, b, c)
PYTHAGOREAN_TRIPLES = [
    (3, 4, 5),
    (5, 12, 13),
    (6, 8, 10),
    (8, 15, 17),
    (7, 24, 25),
    (9, 12, 15),
    (12, 16, 20),
    (9, 40, 41),
    (10, 24, 26),
    (15, 20, 25),
]


def generate_grade9_pythagoras_question(
    seed: Optional[int] = None,
    difficulty: str = "medium",
    mode: str = "compound",
    subskill: Optional[str] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    r = rng(seed)

    archetype_choices = [
        "find_hypotenuse",
        "find_shorter_side",
        "converse_pythagoras",
        "cartesian_distance",
        "space_diagonal_3d",
    ]

    selected_subskill = subskill or mode
    if selected_subskill in archetype_choices:
        archetype = selected_subskill
    else:
        archetype = r.choice(archetype_choices)

    qid = f"g9_pyth_{seed or r.randint(1000, 9999)}_{uuid.uuid4().hex[:6]}"

    if archetype == "find_hypotenuse":
        triple = r.choice(PYTHAGOREAN_TRIPLES)
        mult = r.choice([1, 2]) if difficulty == "easy" else r.choice([1, 2, 3])
        a, b, c = triple[0] * mult, triple[1] * mult, triple[2] * mult
        if r.random() > 0.5:
            a, b = b, a

        question_text = (
            f"In right-angled triangle $\\Delta ABC$, $\\hat{{B}} = 90^\\circ$.\n\n"
            f"The two shorter sides are given as $AB = {a}\\text{{ cm}}$ and $BC = {b}\\text{{ cm}}$.\n\n"
            f"Calculate the length of the hypotenuse $AC$, stating the geometric theorem used."
        )

        steps = [
            {"id": "S1", "statement": "$AC^2 = AB^2 + BC^2$", "reason": "Pythagoras [\\hat{B} = 90^\\circ]", "deps": []},
            {"id": "S2", "statement": f"$AC^2 = {a}^2 + {b}^2 = {a**2} + {b**2} = {c**2}$", "reason": "substitute side lengths", "deps": ["S1"]},
            {"id": "S3", "statement": f"$AC = \\sqrt{{{c**2}}} = {c}\\text{{ cm}}$", "reason": "take square root", "deps": ["S2"]},
        ]

        hints = [
            "In any right-angled triangle, the square on the hypotenuse is equal to the sum of the squares on the other two sides.",
            f"Write the theorem: $AC^2 = AB^2 + BC^2$ [Pythagoras].",
            f"Substitute: $AC^2 = ({a})^2 + ({b})^2 = {a**2} + {b**2} = {c**2}$. Take the positive square root: $AC = \\sqrt{{{c**2}}} = {c}\\text{{ cm}}$.",
        ]

        error_tax = [
            {
                "id": "err_forgot_square_root",
                "tag": "misconception_forgot_sqrt",
                "condition": f"Answered {c**2} instead of {c}",
                "feedback": f"You found AC² = {c**2}. Remember to take the square root to find AC = {c} cm.",
            },
            {
                "id": "err_subtracted_instead",
                "tag": "misconception_pythagoras_operation",
                "condition": "Subtracted side lengths instead of adding",
                "feedback": "When finding the hypotenuse (the longest side opposite 90°), you ADD the squares of the two shorter sides.",
            },
        ]

        sample_answer = (
            f"$AC^2 = AB^2 + BC^2$ [Pythagoras, $\\hat{{B}} = 90^\\circ$]\n"
            f"$AC^2 = ({a})^2 + ({b})^2$\n"
            f"$AC^2 = {a**2} + {b**2} = {c**2}$\n"
            f"$AC = \\sqrt{{{c**2}}} = {c}\\text{{ cm}}$"
        )

        diagram_spec = {
            "diagram_role": "context",
            "kind": "right_triangle",
            "caption": f"Right-angled triangle ABC (AB = {a} cm, BC = {b} cm)",
            "points": {"A": [0, b], "B": [0, 0], "C": [a, 0]},
            "vertex_labels": {"A": "A", "B": "B", "C": "C"},
            "sides": [
                {"edge": "AB", "from": "A", "to": "B"},
                {"edge": "BC", "from": "B", "to": "C"},
                {"edge": "AC", "from": "A", "to": "C"},
            ],
            "side_labels": {"AB": f"{a} cm", "BC": f"{b} cm", "AC": "x"},
            "right_angle_at": "B",
        }

        correct_ans = f"{c} cm"
        subskill_id = "find_hypotenuse"
        reason_code = "Pythagoras"
        marks = 3

    elif archetype == "find_shorter_side":
        triple = r.choice(PYTHAGOREAN_TRIPLES)
        mult = r.choice([1, 2])
        a, b, c = triple[0] * mult, triple[1] * mult, triple[2] * mult
        if r.random() > 0.5:
            a, b = b, a

        question_text = (
            f"In right-angled triangle $\\Delta PQR$, $\\hat{{Q}} = 90^\\circ$.\n\n"
            f"The hypotenuse $PR = {c}\\text{{ cm}}$ and one side $QR = {b}\\text{{ cm}}$.\n\n"
            f"Calculate the length of the unknown side $PQ$, giving a geometric reason."
        )

        steps = [
            {"id": "S1", "statement": "$PQ^2 + QR^2 = PR^2$", "reason": "Pythagoras [\\hat{Q} = 90^\\circ]", "deps": []},
            {"id": "S2", "statement": f"$PQ^2 = PR^2 - QR^2 = {c}^2 - {b}^2 = {c**2} - {b**2} = {a**2}$", "reason": "isolate unknown side", "deps": ["S1"]},
            {"id": "S3", "statement": f"$PQ = \\sqrt{{{a**2}}} = {a}\\text{{ cm}}$", "reason": "take square root", "deps": ["S2"]},
        ]

        hints = [
            "To find a shorter side, rearrange the Theorem of Pythagoras by subtracting the known side squared from the hypotenuse squared: a² = c² - b².",
            f"Formula: $PQ^2 = PR^2 - QR^2$ [Pythagoras].",
            f"Substitute: $PQ^2 = ({c})^2 - ({b})^2 = {c**2} - {b**2} = {a**2}$. Therefore $PQ = \\sqrt{{{a**2}}} = {a}\\text{{ cm}}$.",
        ]

        error_tax = [
            {
                "id": "err_added_to_hypotenuse",
                "tag": "misconception_added_hypotenuse",
                "condition": f"Added c² + b² = {c**2 + b**2}",
                "feedback": "You already know the hypotenuse (PR = {c} cm). A shorter side cannot be longer than the hypotenuse; you must SUBTRACT: PQ² = PR² - QR².",
            },
        ]

        sample_answer = (
            f"$PQ^2 + QR^2 = PR^2$ [Pythagoras, $\\hat{{Q}} = 90^\\circ$]\n"
            f"$PQ^2 = PR^2 - QR^2$\n"
            f"$PQ^2 = ({c})^2 - ({b})^2 = {c**2} - {b**2} = {a**2}$\n"
            f"$PQ = \\sqrt{{{a**2}}} = {a}\\text{{ cm}}$"
        )

        diagram_spec = {
            "diagram_role": "context",
            "kind": "right_triangle",
            "caption": f"Right-angled triangle PQR (PR = {c} cm, QR = {b} cm)",
            "points": {"P": [0, a], "Q": [0, 0], "R": [b, 0]},
            "vertex_labels": {"P": "P", "Q": "Q", "R": "R"},
            "sides": [
                {"edge": "PQ", "from": "P", "to": "Q"},
                {"edge": "QR", "from": "Q", "to": "R"},
                {"edge": "PR", "from": "P", "to": "R"},
            ],
            "side_labels": {"PQ": "x", "QR": f"{b} cm", "PR": f"{c} cm"},
            "right_angle_at": "Q",
        }

        correct_ans = f"{a} cm"
        subskill_id = "find_shorter_side"
        reason_code = "Pythagoras"
        marks = 3

    elif archetype == "converse_pythagoras":
        is_right = r.choice([True, False])
        if is_right:
            triple = r.choice(PYTHAGOREAN_TRIPLES)
            mult = r.choice([1, 2])
            a, b, c = triple[0] * mult, triple[1] * mult, triple[2] * mult
            sum_sq = a**2 + b**2
            c_sq = c**2
            result_str = "Yes, it is a right-angled triangle"
            conclusion_text = f"Since ${a}^2 + {b}^2 = {sum_sq} = {c}^2$, the triangle is right-angled [Converse Pythagoras]."
        else:
            a = r.randint(5, 12)
            b = r.randint(6, 14)
            c = int(math.isqrt(a**2 + b**2)) + r.choice([-1, 1, 2])
            if c <= max(a, b):
                c = max(a, b) + 2
            sum_sq = a**2 + b**2
            c_sq = c**2
            result_str = "No, it is not a right-angled triangle"
            conclusion_text = f"Since ${a}^2 + {b}^2 = {sum_sq} \\neq {c}^2 = {c_sq}$, the triangle is NOT right-angled."

        question_text = (
            f"The three side lengths of $\\Delta DEF$ are given as $DE = {a}\\text{{ cm}}$, "
            f"$EF = {b}\\text{{ cm}}$, and $DF = {c}\\text{{ cm}}$.\n\n"
            f"1. Calculate $DE^2 + EF^2$ and $DF^2$ separately.\n"
            f"2. Use the Converse of the Theorem of Pythagoras to determine whether $\\Delta DEF$ "
            f"is a right-angled triangle."
        )

        steps = [
            {"id": "S1", "statement": f"Calculate sum of squares of two shorter sides: ${a}^2 + {b}^2 = {a**2} + {b**2} = {sum_sq}$", "reason": "arithmetic", "deps": []},
            {"id": "S2", "statement": f"Calculate square of longest side: ${c}^2 = {c_sq}$", "reason": "arithmetic", "deps": []},
            {"id": "S3", "statement": f"Compare: ${sum_sq} {'=' if is_right else '\\neq'} {c_sq}$", "reason": "Converse of Pythagoras Theorem", "deps": ["S1", "S2"]},
            {"id": "S4", "statement": f"Conclusion: {result_str}", "reason": "final deduction", "deps": ["S3"]},
        ]

        hints = [
            "To prove whether a triangle is right-angled, calculate the sum of the squares of the two shorter sides separately from the square of the longest side.",
            f"Calculate: ${a}^2 + {b}^2 = {sum_sq}$, and compare it with the longest side squared: ${c}^2 = {c_sq}$.",
            f"If $a^2 + b^2 = c^2$, it is right-angled by the Converse of Pythagoras. If $a^2 + b^2 \\neq c^2$, it is not right-angled.",
        ]

        error_tax = [
            {
                "id": "err_assumed_right_angle",
                "tag": "misconception_circular_reasoning",
                "condition": "Wrote DE² + EF² = DF² [Pythagoras] as an initial statement",
                "feedback": "You cannot state DE² + EF² = DF² as a fact initially! You must calculate both sides separately and then compare them to test if they are equal.",
            },
        ]

        sample_answer = (
            f"1. $DE^2 + EF^2 = ({a})^2 + ({b})^2 = {a**2} + {b**2} = {sum_sq}$\n"
            f"   $DF^2 = ({c})^2 = {c_sq}$\n\n"
            f"2. {conclusion_text}"
        )

        diagram_spec = {
            "diagram_role": "context",
            "kind": "triangle",
            "caption": f"Testing triangle DEF (sides {a} cm, {b} cm, {c} cm)",
            "points": {"D": [0, a], "E": [0, 0], "F": [b, 0]},
            "vertices": ["D", "E", "F"],
            "side_labels": {"DE": f"{a} cm", "EF": f"{b} cm", "DF": f"{c} cm"},
        }

        correct_ans = "Yes" if is_right else "No"
        subskill_id = "converse_pythagoras"
        reason_code = "Converse Pythagoras"
        marks = 4

    elif archetype == "cartesian_distance":
        # Distance between (x1, y1) and (x2, y2)
        base_pairs = [(3, 4, 5), (6, 8, 10), (5, 12, 13)]
        dx, dy, dist = r.choice(base_pairs)
        x1 = r.randint(-5, 3)
        y1 = r.randint(-5, 3)
        sx = r.choice([1, -1])
        sy = r.choice([1, -1])
        x2 = x1 + sx * dx
        y2 = y1 + sy * dy

        question_text = (
            f"Points $A({x1}; {y1})$ and $B({x2}; {y2})$ are plotted on a Cartesian plane.\n\n"
            f"Using the Theorem of Pythagoras (distance formula), calculate the length of the line segment $AB$."
        )

        steps = [
            {"id": "S1", "statement": "$AB^2 = (x_2 - x_1)^2 + (y_2 - y_1)^2$", "reason": "distance formula / Pythagoras", "deps": []},
            {"id": "S2", "statement": f"$AB^2 = ({x2} - ({x1}))^2 + ({y2} - ({y1}))^2 = ({abs(x2 - x1)})^2 + ({abs(y2 - y1)})^2$", "reason": "substitute coordinates", "deps": ["S1"]},
            {"id": "S3", "statement": f"$AB^2 = {dx**2} + {dy**2} = {dist**2}$", "reason": "arithmetic sum", "deps": ["S2"]},
            {"id": "S4", "statement": f"$AB = \\sqrt{{{dist**2}}} = {dist}\\text{{ units}}$", "reason": "take square root", "deps": ["S3"]},
        ]

        hints = [
            "The distance formula is directly derived from Pythagoras: d² = (Δx)² + (Δy)².",
            f"Calculate the horizontal distance: $\\Delta x = |{x2} - ({x1})| = {dx}$, and vertical distance: $\\Delta y = |{y2} - ({y1})| = {dy}$.",
            f"Apply Pythagoras: $AB^2 = ({dx})^2 + ({dy})^2 = {dx**2} + {dy**2} = {dist**2}$. Therefore $AB = \\sqrt{{{dist**2}}} = {dist}\\text{{ units}}$.",
        ]

        error_tax = [
            {
                "id": "err_sign_subtracting_negatives",
                "tag": "misconception_coordinate_sign",
                "condition": f"Calculated {x2} - {x1} incorrectly with negative signs",
                "feedback": "Be very careful subtracting negative coordinates: e.g. 2 - (-3) = 2 + 3 = 5.",
            },
        ]

        sample_answer = (
            f"$AB^2 = (x_2 - x_1)^2 + (y_2 - y_1)^2$ [Pythagoras]\n"
            f"$AB^2 = ({x2} - ({x1}))^2 + ({y2} - ({y1}))^2$\n"
            f"$AB^2 = ({dx})^2 + ({dy})^2 = {dx**2} + {dy**2} = {dist**2}$\n"
            f"$AB = \\sqrt{{{dist**2}}} = {dist}\\text{{ units}}$"
        )

        diagram_spec = {
            "diagram_role": "context",
            "kind": "function_graph",
            "domain": [-8, 8],
            "range": [-8, 8],
            "landmarks": [
                {"x": x1, "y": y1, "label": f"A({x1}; {y1})"},
                {"x": x2, "y": y2, "label": f"B({x2}; {y2})"},
            ],
        }

        correct_ans = f"{dist} units"
        subskill_id = "cartesian_distance"
        reason_code = "distance formula / Pythagoras"
        marks = 4

    else:
        # space_diagonal_3d
        base_triples = [(2, 3, 6, 7), (1, 4, 8, 9), (4, 12, 3, 13), (2, 10, 11, 15)]
        l, b, h, diag = r.choice(base_triples)
        scale = r.choice([1, 2])
        l, b, h, diag = l * scale, b * scale, h * scale, diag * scale

        floor_diag_sq = l**2 + b**2

        question_text = (
            f"A rectangular room or storage box has length $l = {l}\\text{{ m}}$, "
            f"breadth $b = {b}\\text{{ m}}$, and height $h = {h}\\text{{ m}}$.\n\n"
            f"1. Calculate the diagonal of the floor of the room.\n"
            f"2. Use the Theorem of Pythagoras to calculate the space diagonal (the distance from a bottom corner to the opposite top corner)."
        )

        steps = [
            {"id": "S1", "statement": f"$\\text{{Floor diagonal}}^2 = l^2 + b^2 = {l}^2 + {b}^2 = {floor_diag_sq}$", "reason": "Pythagoras on floor", "deps": []},
            {"id": "S2", "statement": f"$\\text{{Space diagonal}}^2 = \\text{{Floor diagonal}}^2 + h^2 = {floor_diag_sq} + {h}^2$", "reason": "Pythagoras on vertical triangle", "deps": ["S1"]},
            {"id": "S3", "statement": f"$d^2 = {floor_diag_sq} + {h**2} = {diag**2}$", "reason": "sum of squares", "deps": ["S2"]},
            {"id": "S4", "statement": f"$d = \\sqrt{{{diag**2}}} = {diag}\\text{{ m}}$", "reason": "take square root", "deps": ["S3"]},
        ]

        hints = [
            "In 3D, the space diagonal of a rectangular prism satisfies: d² = l² + b² + h².",
            f"Calculate the floor diagonal first: $d_{{\\text{{floor}}}}^2 = ({l})^2 + ({b})^2 = {floor_diag_sq}$.",
            f"Then add height squared: $d^2 = {floor_diag_sq} + ({h})^2 = {floor_diag_sq} + {h**2} = {diag**2}$. Thus $d = \\sqrt{{{diag**2}}} = {diag}\\text{{ m}}$.",
        ]

        error_tax = [
            {
                "id": "err_added_dimensions_directly",
                "tag": "misconception_linear_vs_diagonal",
                "condition": f"Added l + b + h = {l + b + h}",
                "feedback": "You cannot add lengths directly to find diagonal distance. You must use the 3D Theorem of Pythagoras: d² = l² + b² + h².",
            },
        ]

        sample_answer = (
            f"1. $d_{{\\text{{floor}}}}^2 = l^2 + b^2 = ({l})^2 + ({b})^2 = {l**2} + {b**2} = {floor_diag_sq}$\n"
            f"2. $d^2 = d_{{\\text{{floor}}}}^2 + h^2$ [Pythagoras]\n"
            f"   $d^2 = {floor_diag_sq} + ({h})^2 = {floor_diag_sq} + {h**2} = {diag**2}$\n"
            f"   $d = \\sqrt{{{diag**2}}} = {diag}\\text{{ m}}$"
        )

        diagram_spec = {
            "diagram_role": "context",
            "kind": "solid_3d",
            "type": "rectangular_prism",
            "length": l,
            "breadth": b,
            "height": h,
            "caption": f"Rectangular room {l}m x {b}m x {h}m with space diagonal",
        }

        correct_ans = f"{diag} m"
        subskill_id = "space_diagonal_3d"
        reason_code = "3D Pythagoras: d^2 = l^2 + b^2 + h^2"
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
            {"criterion": f"Correct Pythagoras formula and statement [{reason_code}]", "marks": 1},
            {"criterion": f"Correct substitution and calculation {correct_ans}", "marks": marks - 1},
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
        "keywords": ["Pythagoras", "hypotenuse", "right-angled triangle", "converse", "distance formula", "space diagonal"],
        "term": 3,
        "caps_weight_percent": 12.0,
        "suggested_duration_mins": 5,
        "minimum_mastery_score": 75,
        "diagram_spec": diagram_spec,
        "modality": "math",
        "seed": seed,
        "solution_graph": {
            "goal": "Apply Theorem of Pythagoras to calculate unknown distance",
            "steps": steps,
        },
        "metadata": {
            "diagram_spec": diagram_spec,
            "answer_value": correct_ans,
            "reason_code": reason_code,
        },
    }
    return q


def generate_space_diagonal_3d(r: random.Random, mode: str = "compound") -> Dict[str, Any]:
    return generate_grade9_pythagoras_question(seed=r.randint(1, 100000), subskill="space_diagonal_3d", mode=mode)


def generate_cartesian_distance(r: random.Random, mode: str = "compound") -> Dict[str, Any]:
    return generate_grade9_pythagoras_question(seed=r.randint(1, 100000), subskill="cartesian_distance", mode=mode)


def generate(seed: Optional[int] = None, count: int = 1, **kwargs: Any) -> Dict[str, Any]:
    r = rng(seed)
    questions = []
    for _ in range(count):
        sub_seed = r.randint(1, 1_000_000_000)
        questions.append(generate_grade9_pythagoras_question(seed=sub_seed, **kwargs))
    return {"questions": questions}
