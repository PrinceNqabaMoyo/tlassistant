"""Grade 9 Mathematics — Area and Perimeter of 2D Shapes Generator (Deterministic 6-Pillar Contract).

Curriculum Alignment:
- Grade 9 Term 3: Area and perimeter of 2D shapes
- South African National Curriculum Standards (Senior Phase Mathematics)
- Perimeter and Area of polygons:
  * Triangles: A = 1/2 * base * perp_height
  * Circles: Circumference C = 2 * pi * r, Area A = pi * r^2 (using pi = 22/7 or 3,14)
  * Quadrilaterals: Parallelogram (A = b * h), Trapezium (A = 1/2*(a + b)*h), Rhombus / Kite (A = 1/2*d1*d2)
  * Composite 2D figures (shaded area: rectangle minus circle, or rectangle plus triangle)
  * Dimension scaling: linear factor k increases perimeter by k and area by k^2

6 Pillars:
- Deterministic seed generation with zero LLM authority
- Directed solution graph with dependency tracking
- Adaptive deconstruction (atomic elementary sub-drills on error)
- Rich 3-tier hints (Conceptual, Procedural with formula, Concrete Step-by-Step with actual numbers)
- Misconception-targeted error taxonomy
- Native DiagramRenderer specs (kind: 'triangle' / 'quadrilateral')
"""
from __future__ import annotations

import math
import random
import uuid
from typing import Any, Dict, List, Optional

from app.utils.grade9_mathematics._math_common import rng

TOPIC = "grade9_math_area_and_perimeter_of_2d_shapes"
LO = "math9_area_perimeter_2d"


def generate_grade9_area_perimeter_2d_question(
    seed: Optional[int] = None,
    difficulty: str = "medium",
    mode: str = "compound",
    subskill: Optional[str] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    r = rng(seed)

    archetype_choices = [
        "circle_circumference_area",
        "trapezium_area",
        "kite_rhombus_area",
        "composite_shaded_area",
        "dimension_scaling_area",
    ]

    selected_subskill = subskill or mode
    if selected_subskill in archetype_choices:
        archetype = selected_subskill
    else:
        archetype = r.choice(archetype_choices)

    qid = f"g9_area2d_{seed or r.randint(1000, 9999)}_{uuid.uuid4().hex[:6]}"

    if archetype == "circle_circumference_area":
        # Radius multiple of 7 for clean 22/7 arithmetic, or multiple of 5 for 3.14
        use_fraction_pi = r.choice([True, False])
        if use_fraction_pi:
            r_val = r.choice([7, 14, 21, 28])
            pi_str = "\\frac{22}{7}"
            pi_val = 22 / 7
            c_val = int(2 * (22 / 7) * r_val)
            a_val = int((22 / 7) * (r_val ** 2))
        else:
            r_val = r.choice([5, 10, 15, 20])
            pi_str = "3{,}14"
            pi_val = 3.14
            c_val = round(2 * 3.14 * r_val, 2)
            a_val = round(3.14 * (r_val ** 2), 2)

        question_text = (
            f"A circular garden pond has a radius of $r = {r_val}\\text{{ m}}$. "
            f"(Use $\\pi = {pi_str}$).\n\n"
            f"1. Calculate the circumference ($C$) of the pond.\n"
            f"2. Calculate the area ($A$) of the pond."
        )

        steps = [
            {"id": "S1", "statement": f"$C = 2\\pi r = 2 \\times {pi_str} \\times {r_val} = {c_val}\\text{{ m}}$", "reason": "circumference formula", "deps": []},
            {"id": "S2", "statement": f"$A = \\pi r^2 = {pi_str} \\times ({r_val})^2 = {a_val}\\text{{ m}}^2$", "reason": "area formula", "deps": []},
        ]

        hints = [
            "Circumference is the distance around the circle: C = 2πr. Area is the surface enclosed by the circle: A = πr².",
            f"Use the formulas with r = {r_val}: $C = 2 \\times {pi_str} \\times {r_val}$ and $A = {pi_str} \\times {r_val}^2$.",
            f"Circumference $C = {c_val}\\text{{ m}}$ and Area $A = {a_val}\\text{{ m}}^2$.",
        ]

        error_tax = [
            {
                "id": "err_confused_c_and_a_formula",
                "tag": "misconception_circle_formulas",
                "condition": "Used πr² for circumference or 2πr for area",
                "feedback": "Circumference is a 1D linear distance (2πr, units of m). Area is 2D squared surface (πr², units of m²).",
            },
            {
                "id": "err_squared_diameter",
                "tag": "misconception_radius_vs_diameter",
                "condition": "Treated radius as diameter or forgot to square radius",
                "feedback": "Make sure you square the radius: r² = r × r.",
            },
        ]

        sample_answer = (
            f"1. $C = 2\\pi r$\n"
            f"   $C = 2 \\times {pi_str} \\times {r_val} = {c_val}\\text{{ m}}$\n\n"
            f"2. $A = \\pi r^2$\n"
            f"   $A = {pi_str} \\times ({r_val})^2 = {pi_str} \\times {r_val**2} = {a_val}\\text{{ m}}^2$"
        )

        diagram_spec = {
            "diagram_role": "context",
            "kind": "function_graph",
            "domain": [-r_val - 2, r_val + 2],
            "range": [-r_val - 2, r_val + 2],
            "caption": f"Circle with radius r = {r_val} m",
        }

        correct_ans = f"C = {c_val} m; A = {a_val} m²"
        subskill_id = "circle_circumference_area"
        reason_code = "C = 2pi*r, A = pi*r^2"
        marks = 4

    elif archetype == "trapezium_area":
        # Trapezium: parallel sides a and b, perpendicular height h. Area = 1/2*(a + b)*h
        h = r.randint(4, 12)
        a = r.randint(6, 16)
        b = a + 2 * r.randint(2, 6)
        area = int(0.5 * (a + b) * h)

        question_text = (
            f"A trapezium has two parallel sides of length $a = {a}\\text{{ cm}}$ "
            f"and $b = {b}\\text{{ cm}}$. The perpendicular height between them is $h = {h}\\text{{ cm}}$.\n\n"
            f"Calculate the area ($A$) of the trapezium."
        )

        steps = [
            {"id": "S1", "statement": "$A = \\frac{1}{2}(a + b)h$", "reason": "trapezium area formula", "deps": []},
            {"id": "S2", "statement": f"$A = \\frac{{1}}{{2}}({a} + {b})({h}) = \\frac{{1}}{{2}}({a + b})({h})$", "reason": "substitute given values", "deps": ["S1"]},
            {"id": "S3", "statement": f"$A = {area}\\text{{ cm}}^2$", "reason": "arithmetic calculation", "deps": ["S2"]},
        ]

        hints = [
            "The area of a trapezium equals half the sum of the parallel sides multiplied by the perpendicular height.",
            f"Formula: $A = \\frac{{1}}{{2}}(a + b)h = \\frac{{1}}{{2}}({a} + {b}) \\times {h}$.",
            f"Add the parallel sides first: ${a} + {b} = {a + b}$. Multiply by height {h}: ${(a + b) * h}$. Divide by 2: ${area}\\text{{ cm}}^2$.",
        ]

        error_tax = [
            {
                "id": "err_forgot_half",
                "tag": "misconception_trapezium_half",
                "condition": f"Calculated (a + b) * h = {(a + b) * h}",
                "feedback": "Do not forget the factor of 1/2 in the trapezium formula: A = 1/2(a + b)h.",
            },
        ]

        sample_answer = (
            f"$A = \\frac{{1}}{{2}}(a + b)h$\n"
            f"$A = \\frac{{1}}{{2}}({a} + {b})({h})$\n"
            f"$A = \\frac{{1}}{{2}}({a + b})({h}) = {area}\\text{{ cm}}^2$"
        )

        diagram_spec = {
            "diagram_role": "context",
            "kind": "quadrilateral",
            "caption": f"Trapezium with parallel sides {a} cm and {b} cm, height {h} cm",
            "points": {"A": [2, h], "B": [2 + a, h], "C": [b, 0], "D": [0, 0]},
            "vertices": ["A", "B", "C", "D"],
            "side_labels": {"AB": f"{a} cm", "CD": f"{b} cm"},
        }

        correct_ans = f"{area} cm²"
        subskill_id = "trapezium_area"
        reason_code = "A = 1/2*(a + b)*h"
        marks = 3

    elif archetype == "kite_rhombus_area":
        # Kite / Rhombus: Area = 1/2 * d1 * d2
        d1 = 2 * r.randint(4, 12)
        d2 = 2 * r.randint(5, 14)
        area = int(0.5 * d1 * d2)
        shape_type = r.choice(["kite", "rhombus"])

        question_text = (
            f"The two perpendicular diagonals of a ${shape_type}$ have lengths "
            f"$d_1 = {d1}\\text{{ cm}}$ and $d_2 = {d2}\\text{{ cm}}$.\n\n"
            f"Calculate the area of the ${shape_type}$."
        )

        steps = [
            {"id": "S1", "statement": f"$A = \\frac{{1}}{{2}} d_1 d_2$", "reason": f"{shape_type} area formula", "deps": []},
            {"id": "S2", "statement": f"$A = \\frac{{1}}{{2}}({d1})({d2}) = {area}\\text{{ cm}}^2$", "reason": "arithmetic", "deps": ["S1"]},
        ]

        hints = [
            f"The diagonals of a {shape_type} intersect perpendicularly at 90°. The area is half the product of the two diagonals.",
            f"Formula: $A = \\frac{{1}}{{2}} \\times d_1 \\times d_2 = \\frac{{1}}{{2}} \\times {d1} \\times {d2}$.",
            f"Multiply: $\\frac{{1}}{{2}} \\times {d1 * d2} = {area}\\text{{ cm}}^2$.",
        ]

        error_tax = [
            {
                "id": "err_forgot_half_diagonals",
                "tag": "misconception_rhombus_half",
                "condition": f"Calculated d1 * d2 = {d1 * d2}",
                "feedback": f"The area of a {shape_type} is HALF the product of the diagonals: A = 1/2 * d1 * d2.",
            },
        ]

        sample_answer = (
            f"$A = \\frac{{1}}{{2}} d_1 d_2$\n"
            f"$A = \\frac{{1}}{{2}}({d1})({d2}) = {area}\\text{{ cm}}^2$"
        )

        diagram_spec = {
            "diagram_role": "context",
            "kind": "quadrilateral",
            "caption": f"{shape_type.capitalize()} with diagonals d1 = {d1} cm, d2 = {d2} cm",
            "points": {"A": [0, d2 / 2], "B": [d1 / 3, 0], "C": [0, -d2 / 2], "D": [-2 * d1 / 3, 0]},
            "vertices": ["A", "B", "C", "D"],
        }

        correct_ans = f"{area} cm²"
        subskill_id = "kite_rhombus_area"
        reason_code = "A = 1/2*d1*d2"
        marks = 2

    elif archetype == "composite_shaded_area":
        # Shaded area: Rectangle with a right-angled triangle or circle cut out
        l = r.randint(12, 20)
        w = r.randint(8, 14)
        rect_area = l * w
        
        # Cutout right triangle at a corner: base tb, height th
        tb = r.randint(4, 8)
        th = r.randint(4, 6)
        tri_area = int(0.5 * tb * th)
        shaded_area = rect_area - tri_area

        question_text = (
            f"A metal plate is shaped as a rectangle of length $l = {l}\\text{{ cm}}$ and width $w = {w}\\text{{ cm}}$.\n\n"
            f"A right-angled triangular corner piece with base $b = {tb}\\text{{ cm}}$ and "
            f"height $h = {th}\\text{{ cm}}$ is cut out of the rectangle.\n\n"
            f"1. Calculate the area of the original rectangle.\n"
            f"2. Calculate the area of the cut-out triangle.\n"
            f"3. Hence, determine the area of the remaining shaded plate."
        )

        steps = [
            {"id": "S1", "statement": f"$A_{{\\text{{rect}}}} = l \\times w = {l} \\times {w} = {rect_area}\\text{{ cm}}^2$", "reason": "rectangle area formula", "deps": []},
            {"id": "S2", "statement": f"$A_{{\\text{{tri}}}} = \\frac{{1}}{{2}} b h = \\frac{{1}}{{2}}({tb})({th}) = {tri_area}\\text{{ cm}}^2$", "reason": "triangle area formula", "deps": []},
            {"id": "S3", "statement": f"$A_{{\\text{{shaded}}}} = A_{{\\text{{rect}}}} - A_{{\\text{{tri}}}} = {rect_area} - {tri_area} = {shaded_area}\\text{{ cm}}^2$", "reason": "subtract cutout from total", "deps": ["S1", "S2"]},
        ]

        hints = [
            "For composite shaded areas, subtract the unshaded cutout area from the total area of the enclosing figure.",
            f"Calculate the area of the rectangle: ${l} \\times {w} = {rect_area}\\text{{ cm}}^2$. Calculate the area of the triangular cutout: $\\frac{{1}}{{2}} \\times {tb} \\times {th} = {tri_area}\\text{{ cm}}^2$.",
            f"Subtract: ${rect_area} - {tri_area} = {shaded_area}\\text{{ cm}}^2$.",
        ]

        error_tax = [
            {
                "id": "err_added_cutout",
                "tag": "misconception_added_cutout",
                "condition": f"Added {rect_area} + {tri_area} = {rect_area + tri_area}",
                "feedback": "The triangle was CUT OUT (removed) from the plate, so its area must be SUBTRACTED, not added.",
            },
        ]

        sample_answer = (
            f"1. $A_{{\\text{{rect}}}} = l \\times w = {l} \\times {w} = {rect_area}\\text{{ cm}}^2$\n"
            f"2. $A_{{\\text{{tri}}}} = \\frac{{1}}{{2}} b h = \\frac{{1}}{{2}}({tb})({th}) = {tri_area}\\text{{ cm}}^2$\n"
            f"3. $A_{{\\text{{shaded}}}} = A_{{\\text{{rect}}}} - A_{{\\text{{tri}}}} = {rect_area} - {tri_area} = {shaded_area}\\text{{ cm}}^2$"
        )

        diagram_spec = {
            "diagram_role": "context",
            "kind": "quadrilateral",
            "caption": f"Rectangle {l}cm x {w}cm with {tb}cm x {th}cm corner cut out",
            "points": {"A": [0, w], "B": [l, w], "C": [l, 0], "D": [0, 0]},
            "vertices": ["A", "B", "C", "D"],
            "side_labels": {"AB": f"{l} cm", "AD": f"{w} cm"},
        }

        correct_ans = f"{shaded_area} cm²"
        subskill_id = "composite_shaded_area"
        reason_code = "A_total - A_cutout"
        marks = 4

    else:
        # dimension_scaling_area: Doubling / tripling dimensions
        factor = r.choice([2, 3, 4])
        orig_p = r.randint(20, 60)
        orig_a = r.randint(24, 120)
        new_p = orig_p * factor
        new_a = orig_a * (factor ** 2)

        question_text = (
            f"A rectangular playground has a perimeter of $P = {orig_p}\\text{{ m}}$ "
            f"and an area of $A = {orig_a}\\text{{ m}}^2$.\n\n"
            f"The municipality decides to enlarge the playground by multiplying both its length "
            f"and its breadth by a factor of $k = {factor}$.\n\n"
            f"1. Calculate the new perimeter of the enlarged playground.\n"
            f"2. Calculate the new area of the enlarged playground."
        )

        steps = [
            {"id": "S1", "statement": f"$P' = k \\times P = {factor} \\times {orig_p} = {new_p}\\text{{ m}}$", "reason": "perimeter scales by k", "deps": []},
            {"id": "S2", "statement": f"$A' = k^2 \\times A = {factor}^2 \\times {orig_a} = {factor**2} \\times {orig_a} = {new_a}\\text{{ m}}^2$", "reason": "area scales by k^2", "deps": []},
        ]

        hints = [
            "When the linear dimensions of a shape are multiplied by k:\n- Perimeter is a 1D length, so it multiplies by k.\n- Area is a 2D measure, so it multiplies by k².",
            f"New perimeter: $P' = {factor} \\times {orig_p} = {new_p}\\text{{ m}}$.",
            f"New area: $A' = ({factor})^2 \\times {orig_a} = {factor**2} \\times {orig_a} = {new_a}\\text{{ m}}^2$.",
        ]

        error_tax = [
            {
                "id": "err_area_scaled_by_k",
                "tag": "misconception_linear_area_scale",
                "condition": f"Scaled area by {factor} instead of {factor**2}",
                "feedback": "Both dimensions are scaled by k, so length × breadth becomes (k × l) × (k × b) = k² × (l × b). Area scales by k².",
            },
        ]

        sample_answer = (
            f"1. $P' = k \\times P = {factor} \\times {orig_p} = {new_p}\\text{{ m}}$\n"
            f"2. $A' = k^2 \\times A = ({factor})^2 \\times {orig_a} = {factor**2} \\times {orig_a} = {new_a}\\text{{ m}}^2$"
        )

        diagram_spec = {
            "diagram_role": "context",
            "kind": "quadrilateral",
            "caption": f"Scaling dimensions by factor k = {factor}",
            "points": {"A": [0, 3], "B": [6, 3], "C": [6, 0], "D": [0, 0]},
            "vertices": ["A", "B", "C", "D"],
        }

        correct_ans = f"P' = {new_p} m; A' = {new_a} m²"
        subskill_id = "dimension_scaling_area"
        reason_code = "P' = k*P, A' = k^2*A"
        marks = 3

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
            {"criterion": f"Correct area/perimeter formula [{reason_code}]", "marks": 1},
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
        "keywords": ["area", "perimeter", "trapezium", "circle", "circumference", "composite area", "scaling factor"],
        "term": 3,
        "caps_weight_percent": 10.0,
        "suggested_duration_mins": 5,
        "minimum_mastery_score": 75,
        "diagram_spec": diagram_spec,
        "modality": "math",
        "seed": seed,
        "solution_graph": {
            "goal": "Calculate 2D area and perimeter",
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
        questions.append(generate_grade9_area_perimeter_2d_question(seed=sub_seed, **kwargs))
    return {"questions": questions}
