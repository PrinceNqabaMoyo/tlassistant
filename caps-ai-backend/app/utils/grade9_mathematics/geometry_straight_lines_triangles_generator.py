"""Grade 9 Mathematics — Geometry of Straight Lines & Triangles (Deterministic 6-Pillar Generator).
Authentic CAPS exam generator covering:
- Exterior angle of a triangle: ext ∠ of △ = sum of two opposite int ∠s.
- Isosceles triangles: angles opposite equal sides are equal [∠s opp equal sides].
- Multi-step geometric rider with parallel lines and triangles.
- Formal two-column Statement & Reason deduction format.
Zero-Meta-Curriculum Invariant strictly enforced.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


def _rng(seed: Optional[int] = None) -> random.Random:
    r = random.Random()
    if seed is not None:
        r.seed(int(seed))
    return r


TOPIC = "grade9_math_geometry_triangles"
LO = "g9_math_geometry_triangles"


def generate_exterior_angle_triangle(r: random.Random, mode: str = "compound") -> Dict[str, Any]:
    # In triangle ABC, side BC is produced to D.
    # Angle A = ax + b, Angle B = cx + d, Ext Angle ACD = (a+c)x + (b+d)
    a = r.randint(2, 3)
    c = r.randint(1, 2)
    sum_coeff = a + c
    
    x_val = r.randint(15, 25)
    
    b = r.randint(5, 15)
    d = r.randint(10, 20)
    ext_const = b + d
    
    ang_a = a * x_val + b
    ang_b = c * x_val + d
    ext_ang = ang_a + ang_b
    
    prompt = (
        f"In \\(\\triangle ABC\\), side \\(BC\\) is extended (produced) past \\(C\\) to point \\(D\\), "
        f"forming exterior angle \\(A\\hat{{C}}D = {sum_coeff}x + {ext_const}^\\circ\\).\n"
        f"The two opposite interior angles are given as \\(\\hat{{A}} = {a}x + {b}^\\circ\\) "
        f"and \\(\\hat{{B}} = {ang_b}^\\circ\\).\n\n"
        f"1. State the theorem relating an exterior angle of a triangle to its interior angles, including the formal geometric reason.\n"
        f"2. Set up an algebraic equation and calculate the numerical value of \\(x\\).\n"
        f"3. Calculate the actual size of interior angle \\(\\hat{{A}}\\) and exterior angle \\(A\\hat{{C}}D\\) in degrees."
    )
    prompt_latex = (
        rf"\text{{In }}\triangle ABC\text{{ with }} BC \text{{ produced to }} D: \quad "
        rf"\hat{{A}} = {a}x + {b}^\circ, \quad \hat{{B}} = {ang_b}^\circ, \quad A\hat{{C}}D = {sum_coeff}x + {ext_const}^\circ." "\n\n"
        r"\text{Calculate } x, \, \hat{A}, \text{ and } A\hat{C}D \text{ with geometric reasons.}"
    )
    answer_latex = (
        rf"A\hat{{C}}D = \hat{{A}} + \hat{{B}} \quad [\text{{ext }}\angle\text{{ of }}\triangle]" "\n"
        rf"{sum_coeff}x + {ext_const}^\circ = ({a}x + {b}^\circ) + {ang_b}^\circ" "\n"
        rf"{sum_coeff}x - {a}x = ({b} + {ang_b}) - {ext_const} \implies {c}x = {c * x_val}^\circ \implies x = {x_val}^\circ" "\n"
        rf"\hat{{A}} = {a}({x_val}) + {b} = {ang_a}^\circ" "\n"
        rf"A\hat{{C}}D = {sum_coeff}({x_val}) + {ext_const} = {ext_ang}^\circ"
    )
    sample_answer = (
        f"1. Theorem: The exterior angle of a triangle is equal to the sum of the two opposite interior angles [ext ∠ of △].\n"
        f"2. Equation: AĈD = Â + B̂\n"
        f"   {sum_coeff}x + {ext_const}° = ({a}x + {b}°) + {ang_b}°\n"
        f"   {sum_coeff}x - {a}x = {b + ang_b}° - {ext_const}°\n"
        f"   {c}x = {c * x_val}°\n"
        f"   x = {x_val}°.\n"
        f"3. Angle sizes:\n"
        f"   Â = {a}({x_val}°) + {b}° = {ang_a}°\n"
        f"   AĈD = {sum_coeff}({x_val}°) + {ext_const}° = {ext_ang}°."
    )
    schema = {
        "total_marks": 5,
        "marking_points": [
            {"id": "mp1", "desc": "Statement: AĈD = Â + B̂ with geometric reason [ext ∠ of △]", "marks": 2, "editable": True},
            {"id": "mp2", "desc": f"Correct equation setup: {sum_coeff}x + {ext_const}° = {a}x + {b}° + {ang_b}°", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Solve for x = {x_val}°", "marks": 1, "editable": True},
            {"id": "mp4", "desc": f"Calculate accurate angles: Â = {ang_a}° and AĈD = {ext_ang}°", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "omitted_geometric_reason", "penalty": 1}],
        "carry_forward_rule": "consequential_accuracy",
    }
    hints = {
        "tier_1": "Recall that the exterior angle formed by extending a side of a triangle equals the sum of the two interior opposite angles.",
        "tier_2": "Equation: Ext Angle = Int Angle 1 + Int Angle 2. Reason: [ext ∠ of △].",
        "tier_3": f"{sum_coeff}x + {ext_const} = {a}x + {b + ang_b}. Group x terms on left: {c}x = {c * x_val}. Therefore x = {x_val}°.",
    }
    return {
        "id": f"g9_geo_ext_ang_{random.randint(100000, 999999)}",
        "topic": TOPIC,
        "subskill": "exterior_angle_of_triangle_theorems",
        "learning_objective_id": f"{LO}_exterior_angle",
        "prompt": prompt,
        "prompt_latex": prompt_latex,
        "answer_latex": answer_latex,
        "sample_answer": sample_answer,
        "marking_schema": schema,
        "hints": hints,
        "misconception_tags": ["confusing_exterior_angle_with_adjacent_supplementary", "omitted_geometric_reason"],
        "keywords": ["exterior angle", "triangle", "geometry", "reasons", "proof"],
        "term": 2,
        "caps_weight_percent": 18,
        "suggested_duration_mins": 5,
        "mode": mode,
        "difficulty": "medium",
        "marks": 5,
    }


def generate_isosceles_triangle_rider(r: random.Random, mode: str = "compound") -> Dict[str, Any]:
    # Triangle PQR where PQ = PR
    vertex_ang = r.choice([36, 40, 48, 52, 64, 70, 80])
    base_ang = (180 - vertex_ang) // 2
    
    prompt = (
        f"In \\(\\triangle PQR\\), side \\(PQ = PR\\). The vertex angle \\(\\hat{{P}} = {vertex_ang}^\\circ\\).\n\n"
        f"1. What type of triangle is \\(\\triangle PQR\\)?\n"
        f"2. State the relationship between base angles \\(\\hat{{Q}}\\) and \\(\\hat{{R}}\\), giving the formal geometric reason.\n"
        f"3. Calculate the size of base angle \\(\\hat{{Q}}\\) in degrees, showing all steps and citing all geometric reasons."
    )
    prompt_latex = (
        rf"\text{{In }}\triangle PQR\text{{, }} PQ = PR \quad \text{{and}} \quad \hat{{P}} = {vertex_ang}^\circ." "\n\n"
        r"\text{Calculate the size of base angle } \hat{Q} \text{ with full geometric reasons.}"
    )
    answer_latex = (
        r"\text{1. Isosceles triangle.}" "\n"
        r"\text{2. } \hat{Q} = \hat{R} \quad [\angle\text{s opp equal sides}]" "\n"
        rf"\text{{3. }} \hat{{P}} + \hat{{Q}} + \hat{{R}} = 180^\circ \quad [\angle\text{{ sum of }}\triangle]" "\n"
        rf"{vertex_ang}^\circ + 2\hat{{Q}} = 180^\circ \implies 2\hat{{Q}} = {180 - vertex_ang}^\circ" "\n"
        rf"\hat{{Q}} = \frac{{{180 - vertex_ang}^\circ}}{{2}} = {base_ang}^\circ"
    )
    sample_answer = (
        "1. Isosceles triangle (two sides are equal in length).\n"
        "2. Q̂ = R̂ [∠s opp equal sides].\n"
        "3. P̂ + Q̂ + R̂ = 180° [∠ sum of △]\n"
        f"   {vertex_ang}° + 2Q̂ = 180°\n"
        f"   2Q̂ = 180° - {vertex_ang}° = {180 - vertex_ang}°\n"
        f"   Q̂ = {base_ang}°."
    )
    schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": "Identify isosceles triangle", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Statement: Q̂ = R̂ with reason [∠s opp equal sides]", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Statement: P̂ + Q̂ + R̂ = 180° with reason [∠ sum of △]", "marks": 1, "editable": True},
            {"id": "mp4", f"desc": f"Accurate calculation of base angle Q̂ = {base_ang}°", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "omitted_geometric_reason", "penalty": 1}],
        "carry_forward_rule": "consequential_accuracy",
    }
    hints = {
        "tier_1": "In an isosceles triangle with PQ = PR, the angles opposite those equal sides (∠Q and ∠R) are equal.",
        "tier_2": "The sum of all three angles inside any triangle is 180° [∠ sum of △]. Let ∠Q = ∠R = x.",
        "tier_3": f"{vertex_ang}° + 2x = 180°. 2x = {180 - vertex_ang}°. Therefore x = {base_ang}°.",
    }
    return {
        "id": f"g9_geo_iso_{random.randint(100000, 999999)}",
        "topic": TOPIC,
        "subskill": "isosceles_triangle_angle_theorems",
        "learning_objective_id": f"{LO}_isosceles_angles",
        "prompt": prompt,
        "prompt_latex": prompt_latex,
        "answer_latex": answer_latex,
        "sample_answer": sample_answer,
        "marking_schema": schema,
        "hints": hints,
        "misconception_tags": ["omitted_geometric_reason", "assuming_all_angles_are_equal"],
        "keywords": ["isosceles triangle", "angles opposite equal sides", "triangle angle sum", "geometry"],
        "term": 2,
        "caps_weight_percent": 18,
        "suggested_duration_mins": 5,
        "mode": mode,
        "difficulty": "medium",
        "marks": 4,
    }


def generate(seed: Optional[int] = None, mode: str = "compound", archetype: Optional[str] = None) -> Dict[str, Any]:
    r = _rng(seed)
    if archetype == "exterior":
        return generate_exterior_angle_triangle(r, mode=mode)
    elif archetype == "isosceles":
        return generate_isosceles_triangle_rider(r, mode=mode)
    else:
        choice = r.choice(["exterior", "isosceles"])
        if choice == "exterior":
            return generate_exterior_angle_triangle(r, mode=mode)
        else:
            return generate_isosceles_triangle_rider(r, mode=mode)
