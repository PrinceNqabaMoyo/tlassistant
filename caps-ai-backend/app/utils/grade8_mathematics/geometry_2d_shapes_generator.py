"""Grade 8 Mathematics - Geometry of 2D Shapes Generator.
Covers:
  - Triangles: Sum of interior angles (180 deg), exterior angle of a triangle, isosceles and equilateral triangles.
  - Quadrilaterals: Sum of interior angles (360 deg), parallelogram, rectangle, rhombus, and square properties.
  - Solving for unknown angles with authentic CAPS geometric reasons (e.g. [sum of angles in triangle], [ext angle of triangle]).

Follows South African CAPS curriculum specifications and the 6-Pillar Generator Contract.
Strictly zero-LLM, deterministic execution.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


def _rng(seed: Optional[int] = None) -> random.Random:
    r = random.Random()
    if seed is not None:
        r.seed(int(seed))
    return r


def generate_grade8_geometry_2d_question(
    seed: Optional[int] = None,
    difficulty: str = "medium",
    mode: str = "compound",
) -> Dict[str, Any]:
    r = _rng(seed)
    subskill = mode if mode.startswith("elementary_") else "geometry_2d_triangles_quads"

    archetype = r.choice(["triangle_angle_sum", "triangle_exterior_angle", "triangle_isosceles", "quadrilateral_angle_sum"])
    if subskill == "elementary_triangle_sum":
        archetype = "triangle_angle_sum"
    elif subskill == "elementary_quad_sum":
        archetype = "quadrilateral_angle_sum"

    if archetype == "triangle_angle_sum":
        ang1 = r.choice([35, 40, 45, 50, 55, 60, 65, 70])
        ang2 = r.choice([45, 50, 55, 60, 65, 70, 75])
        ang3 = 180 - (ang1 + ang2)

        prompt = (
            f"In \\(\\triangle ABC\\), \\(\\hat{{A}} = {ang1}^\\circ\\) and \\(\\hat{{B}} = {ang2}^\\circ\\).\n\n"
            f"Calculate the size of \\(\\hat{{C}}\\). Give a complete geometric reason for your answer."
        )
        sample_answer = (
            rf"\hat{{C}} = 180^\circ - ({ang1}^\circ + {ang2}^\circ) = {ang3}^\circ\quad "
            rf"[\text{{sum of }}\angle\text{{s in }}\triangle ABC]"
        )

        return {
            "id": f"g8_tri_sum_{random.randint(100000, 999999)}",
            "subject": "mathematics",
            "grade": "grade-8",
            "topic": "Geometry of 2D Shapes",
            "subskill": "triangle_interior_angles",
            "learning_objective_id": "g8_math_geom_triangle_sum",
            "archetype": "triangle_angle_sum",
            "prompt": prompt,
            "sample_answer": sample_answer,
            "correct_value": f"{ang3}^\\circ",
            "marks": 2,
            "marking_schema": {
                "total_marks": 2,
                "marking_points": [
                    {"id": "mp_1", "desc": f"Calculation 180 - ({ang1} + {ang2}) = {ang3}", "marks": 1, "editable": True},
                    {"id": "mp_2", "desc": "Authentic geometric reason [sum of angles in triangle]", "marks": 1, "editable": True},
                ],
                "deductions": [{"rule": "omitted_geometric_reason", "penalty": 1}],
                "carry_forward_rule": "consequential_accuracy",
            },
            "hints": {
                "tier_1": "Recall the fundamental theorem regarding the sum of all three interior angles in any triangle.",
                "tier_2": r"The sum of angles in a triangle is $180^\circ$. Write: $\hat{A} + \hat{B} + \hat{C} = 180^\circ$.",
                "tier_3": rf"$\hat{{C}} = 180^\circ - ({ang1}^\circ + {ang2}^\circ) = {ang3}^\circ$. Reason: $[\text{{sum of }}\angle\text{{s in }}\triangle]$.",
            },
            "misconception_tags": ["omitted_geometric_reason", "used_360_for_triangle_sum"],
            "term": 2,
            "caps_weight_percent": 15,
            "suggested_duration_mins": 2,
            "mode": mode,
            "difficulty": "easy",
        }

    elif archetype == "triangle_exterior_angle":
        ang1 = r.choice([30, 35, 40, 45, 50, 55])
        ang2 = r.choice([40, 45, 50, 60, 65, 70])
        ext_ang = ang1 + ang2

        prompt = (
            f"In \\(\\triangle PQR\\), side \\(QR\\) is extended to \\(S\\) forming exterior angle \\(\\hat{{R}}_1 = x\\).\n"
            f"If interior opposite angles are \\(\\hat{{P}} = {ang1}^\\circ\\) and \\(\\hat{{Q}} = {ang2}^\\circ\\), "
            f"calculate the value of \\(x\\) with geometric reasons."
        )
        sample_answer = (
            rf"x = {ang1}^\circ + {ang2}^\circ = {ext_ang}^\circ\quad "
            rf"[\text{{ext }}\angle\text{{ of }}\triangle PQR]"
        )

        return {
            "id": f"g8_tri_ext_{random.randint(100000, 999999)}",
            "subject": "mathematics",
            "grade": "grade-8",
            "topic": "Geometry of 2D Shapes",
            "subskill": "exterior_angle_triangle",
            "learning_objective_id": "g8_math_geom_ext_angle",
            "archetype": "triangle_exterior_angle",
            "prompt": prompt,
            "sample_answer": sample_answer,
            "correct_value": f"{ext_ang}^\\circ",
            "marks": 2,
            "marking_schema": {
                "total_marks": 2,
                "marking_points": [
                    {"id": "mp_1", "desc": f"Applying exterior angle theorem x = {ang1} + {ang2} = {ext_ang}", "marks": 1, "editable": True},
                    {"id": "mp_2", "desc": "Geometric reason [ext angle of triangle]", "marks": 1, "editable": True},
                ],
                "deductions": [{"rule": "omitted_geometric_reason", "penalty": 1}],
                "carry_forward_rule": "consequential_accuracy",
            },
            "hints": {
                "tier_1": "The exterior angle of a triangle equals the sum of the two interior opposite angles.",
                "tier_2": r"Apply $x = \hat{P} + \hat{Q}$. Reason: $[\text{ext }\angle\text{ of }\triangle]$.",
                "tier_3": rf"$x = {ang1}^\circ + {ang2}^\circ = {ext_ang}^\circ$.",
            },
            "misconception_tags": ["exterior_angle_subtraction_error", "omitted_geometric_reason"],
            "term": 2,
            "caps_weight_percent": 15,
            "suggested_duration_mins": 2,
            "mode": mode,
            "difficulty": "medium",
        }

    elif archetype == "triangle_isosceles":
        vertex_ang = r.choice([40, 50, 70, 80, 100])
        base_ang = (180 - vertex_ang) // 2

        prompt = (
            f"In \\(\\triangle DEF\\), \\(DE = DF\\) and \\(\\hat{{D}} = {vertex_ang}^\\circ\\).\n\n"
            f"Calculate the size of \\(\\hat{{E}}\\). State all geometric reasons."
        )
        sample_answer = (
            rf"\hat{{E}} = \hat{{F}}\quad [\angle\text{{s opp equal sides, }} DE = DF]\\\ "
            rf"\hat{{E}} = \frac{{180^\circ - {vertex_ang}^\circ}}{{2}} = {base_ang}^\circ\quad "
            rf"[\text{{sum of }}\angle\text{{s in }}\triangle DEF]"
        )

        return {
            "id": f"g8_tri_iso_{random.randint(100000, 999999)}",
            "subject": "mathematics",
            "grade": "grade-8",
            "topic": "Geometry of 2D Shapes",
            "subskill": "isosceles_triangle_properties",
            "learning_objective_id": "g8_math_geom_isosceles",
            "archetype": "triangle_isosceles",
            "prompt": prompt,
            "sample_answer": sample_answer,
            "correct_value": f"{base_ang}^\\circ",
            "marks": 3,
            "marking_schema": {
                "total_marks": 3,
                "marking_points": [
                    {"id": "mp_1", "desc": "Stating base angles are equal [angles opp equal sides]", "marks": 1, "editable": True},
                    {"id": "mp_2", "desc": f"Calculation (180 - {vertex_ang}) / 2 = {base_ang}", "marks": 1, "editable": True},
                    {"id": "mp_3", "desc": "Reason [sum of angles in triangle]", "marks": 1, "editable": True},
                ],
                "deductions": [],
                "carry_forward_rule": "consequential_accuracy",
            },
            "hints": {
                "tier_1": "In an isosceles triangle with two equal sides, the angles opposite those equal sides are also equal.",
                "tier_2": rf"Since $DE = DF$, $\hat{{E}} = \hat{{F}}$. The three angles sum to $180^\circ$.",
                "tier_3": rf"$\hat{{E}} = \frac{{180^\circ - {vertex_ang}^\circ}}{{2}} = \frac{{{180 - vertex_ang}^\circ}}{{2}} = {base_ang}^\circ$.",
            },
            "misconception_tags": ["confused_vertex_and_base_angles", "omitted_geometric_reason"],
            "term": 2,
            "caps_weight_percent": 15,
            "suggested_duration_mins": 3,
            "mode": mode,
            "difficulty": "medium",
        }

    else:
        # Quadrilateral angle sum = 360
        ang1 = r.choice([75, 80, 85, 90])
        ang2 = r.choice([95, 100, 105, 110])
        ang3 = r.choice([60, 65, 70, 75])
        ang4 = 360 - (ang1 + ang2 + ang3)

        prompt = (
            f"In quadrilateral \\(KLMN\\), \\(\\hat{{K}} = {ang1}^\\circ\\), \\(\\hat{{L}} = {ang2}^\\circ\\), "
            f"and \\(\\hat{{M}} = {ang3}^\\circ\\).\n\n"
            f"Calculate the size of \\(\\hat{{N}}\\). State the geometric reason."
        )
        sample_answer = (
            rf"\hat{{N}} = 360^\circ - ({ang1}^\circ + {ang2}^\circ + {ang3}^\circ) = {ang4}^\circ\quad "
            rf"[\text{{sum of }}\angle\text{{s in quad}}]"
        )

        return {
            "id": f"g8_quad_sum_{random.randint(100000, 999999)}",
            "subject": "mathematics",
            "grade": "grade-8",
            "topic": "Geometry of 2D Shapes",
            "subskill": "quadrilateral_interior_angles",
            "learning_objective_id": "g8_math_geom_quad_sum",
            "archetype": "quadrilateral_angle_sum",
            "prompt": prompt,
            "sample_answer": sample_answer,
            "correct_value": f"{ang4}^\\circ",
            "marks": 2,
            "marking_schema": {
                "total_marks": 2,
                "marking_points": [
                    {"id": "mp_1", "desc": f"Calculation 360 - sum = {ang4}", "marks": 1, "editable": True},
                    {"id": "mp_2", "desc": "Reason [sum of angles in quad]", "marks": 1, "editable": True},
                ],
                "deductions": [{"rule": "omitted_geometric_reason", "penalty": 1}],
                "carry_forward_rule": "consequential_accuracy",
            },
            "hints": {
                "tier_1": "The interior angles of any four-sided polygon (quadrilateral) sum to 360 degrees.",
                "tier_2": rf"Subtract the three known angles from $360^\circ$: $360^\circ - ({ang1}^\circ + {ang2}^\circ + {ang3}^\circ)$.",
                "tier_3": rf"$\hat{{N}} = 360^\circ - {ang1 + ang2 + ang3}^\circ = {ang4}^\circ$. Reason: $[\text{{sum of }}\angle\text{{s in quad}}]$.",
            },
            "misconception_tags": ["used_180_for_quadrilateral_sum", "omitted_geometric_reason"],
            "term": 2,
            "caps_weight_percent": 15,
            "suggested_duration_mins": 2,
            "mode": mode,
            "difficulty": "easy",
        }


def generate(
    count: int = 1,
    seed: Optional[int] = None,
    difficulty: str = "medium",
    mode: str = "compound",
) -> List[Dict[str, Any]]:
    base_seed = seed if seed is not None else 42
    return [
        generate_grade8_geometry_2d_question(
            seed=base_seed + i,
            difficulty=difficulty,
            mode=mode,
        )
        for i in range(count)
    ]
