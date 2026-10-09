"""Grade 8 Mathematics — Geometry of Straight Lines (Deterministic 6-Pillar Generator).
Authentic CAPS exam generator covering:
- Adjacent angles on a straight line: sum to 180° [adj ∠s on str line].
- Vertically opposite angles: are equal [vert opp ∠s].
- Parallel lines cut by a transversal:
  * Corresponding angles are equal [corresp ∠s, AB || CD].
  * Alternate angles are equal [alt ∠s, AB || CD].
  * Co-interior angles sum to 180° [co-int ∠s, AB || CD].
- Algebraic angle equations with geometric reasons.
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


TOPIC = "grade8_math_geometry_straight_lines"
LO = "g8_math_geometry_lines"


def generate_straight_line_angles(r: random.Random, mode: str = "compound") -> Dict[str, Any]:
    # Form: 2 angles on a straight line: (ax + b) and (cx + d) = 180
    a = r.randint(2, 4)
    c = r.randint(1, 3)
    sum_coeff = a + c
    
    # Choose x_val so that total angle is realistic
    x_val = r.randint(15, 30)
    total_val = sum_coeff * x_val
    remainder = 180 - total_val
    
    # Split remainder into b and d
    b = r.randint(-10, 15)
    d = remainder - b
    
    ang1_expr = rf"{a}x + {b}^\circ" if b >= 0 else rf"{a}x - {abs(b)}^\circ"
    ang2_expr = rf"{c}x + {d}^\circ" if d >= 0 else rf"{c}x - {abs(d)}^\circ"
    
    ang1_val = a * x_val + b
    ang2_val = c * x_val + d
    
    prompt = (
        f"In the given figure, line \\(AB\\) is a straight line. "
        f"Ray \\(OC\\) stands on line \\(AB\\) at point \\(O\\), forming adjacent angles "
        f"\\(\\hat{{O}}_1 = {ang1_expr}\\) and \\(\\hat{{O}}_2 = {ang2_expr}\\).\n\n"
        f"1. Write down an equation connecting \\(\\hat{{O}}_1\\) and \\(\\hat{{O}}_2\\), stating the geometric reason.\n"
        f"2. Solve the equation for \\(x\\).\n"
        f"3. Calculate the actual numerical size of \\(\\hat{{O}}_1\\) in degrees."
    )
    prompt_latex = (
        rf"\text{{Line }} AB\text{{ is a straight line with ray }} OC. \quad "
        rf"\hat{{O}}_1 = {ang1_expr}, \quad \hat{{O}}_2 = {ang2_expr}." "\n\n"
        r"\text{Calculate the value of } x \text{ and the size of } \hat{O}_1 \text{ with reasons.}"
    )
    answer_latex = (
        rf"\hat{{O}}_1 + \hat{{O}}_2 = 180^\circ \quad [\text{{adj }}\angle\text{{s on str line}}]" "\n"
        rf"({ang1_expr}) + ({ang2_expr}) = 180^\circ" "\n"
        rf"{sum_coeff}x + ({b + d})^\circ = 180^\circ \implies {sum_coeff}x = {180 - (b + d)}^\circ" "\n"
        rf"x = {x_val}^\circ" "\n"
        rf"\hat{{O}}_1 = {a}({x_val}) + ({b}) = {ang1_val}^\circ"
    )
    sample_answer = (
        f"1. ∠O₁ + ∠O₂ = 180° (adj ∠s on str line)\n"
        f"2. ({ang1_expr}) + ({ang2_expr}) = 180°\n"
        f"   {sum_coeff}x + {b + d}° = 180°\n"
        f"   {sum_coeff}x = 180° - {b + d}° = {180 - (b + d)}°\n"
        f"   x = {180 - (b + d)}° / {sum_coeff} = {x_val}°\n"
        f"3. ∠O₁ = {a}({x_val}°) + ({b}°) = {ang1_val}°."
    )
    schema = {
        "total_marks": 5,
        "marking_points": [
            {"id": "mp1", "desc": "Statement: ∠O₁ + ∠O₂ = 180° with correct reason [adj ∠s on str line]", "marks": 2, "editable": True},
            {"id": "mp2", "desc": f"Combine like terms: {sum_coeff}x + {b + d}° = 180°", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Solve for x = {x_val}°", "marks": 1, "editable": True},
            {"id": "mp4", "desc": f"Substitute x to find ∠O₁ = {ang1_val}°", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "omitted_geometric_reason", "penalty": 1}],
        "carry_forward_rule": "consequential_accuracy",
    }
    hints = {
        "tier_1": "Angles on a straight line always add up to 180°. State the geometric reason: [adj ∠s on str line].",
        "tier_2": f"Set up the equation: ({ang1_expr}) + ({ang2_expr}) = 180°. Combine the x-terms and the numbers.",
        "tier_3": f"{sum_coeff}x = {180 - (b + d)}°. Therefore x = {x_val}°. Substitute into ∠O₁: {a}({x_val}) + ({b}) = {ang1_val}°.",
    }
    return {
        "id": f"g8_geo_str_line_{random.randint(100000, 999999)}",
        "topic": TOPIC,
        "subskill": "adjacent_angles_on_straight_line",
        "learning_objective_id": f"{LO}_angles_on_straight_line",
        "prompt": prompt,
        "prompt_latex": prompt_latex,
        "answer_latex": answer_latex,
        "sample_answer": sample_answer,
        "marking_schema": schema,
        "hints": hints,
        "misconception_tags": ["omitted_geometric_reason", "confusing_supplementary_with_complementary"],
        "keywords": ["geometry", "straight line", "adjacent angles", "supplementary", "reasons"],
        "term": 2,
        "caps_weight_percent": 18,
        "suggested_duration_mins": 5,
        "mode": mode,
        "difficulty": "medium",
        "marks": 5,
    }


def generate_parallel_lines(r: random.Random, mode: str = "compound") -> Dict[str, Any]:
    angle_type = r.choice(["alternate", "corresponding", "co_interior"])
    x_val = r.randint(15, 35)
    
    if angle_type == "alternate":
        # ax + b = cx + d
        a = r.randint(3, 5)
        c = r.randint(1, a - 1)
        diff = a - c
        const_val = diff * x_val
        b = r.randint(5, 20)
        d = b + const_val
        
        expr1 = rf"{a}x - {b}^\circ"
        expr2 = rf"{c}x + {d - 2*b}^\circ" if d - 2*b >= 0 else rf"{c}x - {abs(d - 2*b)}^\circ"
        actual_ang = a * x_val - b
        
        rel_statement = "are equal"
        reason_tag = "alt \\angle\\text{s, } AB \\parallel CD"
        calc_eq = f"{a}x - {b} = {c}x + ({d - 2*b})"
    elif angle_type == "corresponding":
        a = r.randint(3, 5)
        c = r.randint(1, a - 1)
        diff = a - c
        const_val = diff * x_val
        b = r.randint(5, 20)
        d = b + const_val
        
        expr1 = rf"{a}x - {b}^\circ"
        expr2 = rf"{c}x + {d - 2*b}^\circ" if d - 2*b >= 0 else rf"{c}x - {abs(d - 2*b)}^\circ"
        actual_ang = a * x_val - b
        
        rel_statement = "are equal"
        reason_tag = "corresp \\angle\\text{s, } AB \\parallel CD"
        calc_eq = f"{a}x - {b} = {c}x + ({d - 2*b})"
    else:  # co_interior
        a = r.randint(2, 4)
        c = r.randint(1, 3)
        sum_c = a + c
        total = sum_c * x_val
        rem = 180 - total
        b = r.randint(-10, 15)
        d = rem - b
        
        expr1 = rf"{a}x + {b}^\circ" if b >= 0 else rf"{a}x - {abs(b)}^\circ"
        expr2 = rf"{c}x + {d}^\circ" if d >= 0 else rf"{c}x - {abs(d)}^\circ"
        actual_ang = a * x_val + b
        
        rel_statement = "sum to 180°"
        reason_tag = "co-int \\angle\\text{s, } AB \\parallel CD"
        calc_eq = rf"({expr1}) + ({expr2}) = 180^\circ"

    prompt = (
        f"In the given figure, line \\(AB\\) is parallel to line \\(CD\\) (\\(AB \\parallel CD\\)), "
        f"and line \\(EF\\) is a transversal cutting \\(AB\\) at \\(P\\) and \\(CD\\) at \\(Q\\).\n"
        f"Angle \\(\\hat{{P}}_1 = {expr1}\\) and angle \\(\\hat{{Q}}_2 = {expr2}\\).\n\n"
        f"Given that \\(\\hat{{P}}_1\\) and \\(\\hat{{Q}}_2\\) are **{angle_type.replace('_', '-')} angles**:\n"
        f"1. State the relationship between \\(\\hat{{P}}_1\\) and \\(\\hat{{Q}}_2\\), including the full geometric reason.\n"
        f"2. Set up an equation and solve for \\(x\\).\n"
        f"3. Calculate the actual size of \\(\\hat{{P}}_1\\) in degrees."
    )
    prompt_latex = (
        rf"AB \parallel CD \text{{ cut by transversal }} EF. \quad "
        rf"\hat{{P}}_1 = {expr1}, \quad \hat{{Q}}_2 = {expr2} \text{{ ({angle_type.replace('_', '-')} angles)}}." "\n\n"
        r"\text{Calculate the value of } x \text{ with full geometric reasons.}"
    )
    answer_latex = (
        rf"\text{{Relationship: }} \hat{{P}}_1 \text{{ and }} \hat{{Q}}_2 {rel_statement} \quad [{reason_tag}]" "\n"
        rf"\text{{Equation: }} {calc_eq}" "\n"
        rf"x = {x_val}^\circ" "\n"
        rf"\hat{{P}}_1 = {actual_ang}^\circ"
    )
    sample_answer = (
        f"1. Relationship: {angle_type.replace('_', '-')} angles {rel_statement} [{reason_tag}].\n"
        f"2. {calc_eq}\n"
        f"   Solving for x yields: x = {x_val}°.\n"
        f"3. ∠P₁ = {actual_ang}°."
    )
    schema = {
        "total_marks": 5,
        "marking_points": [
            {"id": "mp1", "desc": f"Correct geometric reason stating parallel lines: [{reason_tag}]", "marks": 2, "editable": True},
            {"id": "mp2", "desc": f"Correct algebraic equation: {calc_eq}", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Solve for x = {x_val}°", "marks": 1, "editable": True},
            {"id": "mp4", "desc": f"Calculate angle ∠P₁ = {actual_ang}°", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "omitted_parallel_line_names_in_reason", "penalty": 1}],
        "carry_forward_rule": "consequential_accuracy",
    }
    hints = {
        "tier_1": f"Look at the angle position (F-shape for corresponding, Z-shape for alternate, C/U-shape for co-interior). State: [{reason_tag}].",
        "tier_2": f"Alternate and corresponding angles are EQUAL. Co-interior angles add up to 180°. Don't forget to include the parallel lines in your reason: AB || CD.",
        "tier_3": f"Set up the equation {calc_eq} and solve for x = {x_val}°. Then substitute to find ∠P₁ = {actual_ang}°.",
    }
    return {
        "id": f"g8_geo_parallel_{random.randint(100000, 999999)}",
        "topic": TOPIC,
        "subskill": "parallel_lines_transversals_angles",
        "learning_objective_id": f"{LO}_parallel_lines",
        "prompt": prompt,
        "prompt_latex": prompt_latex,
        "answer_latex": answer_latex,
        "sample_answer": sample_answer,
        "marking_schema": schema,
        "hints": hints,
        "misconception_tags": ["omitted_parallel_line_names_in_reason", "confusing_alternate_with_cointerior"],
        "keywords": ["parallel lines", "transversal", "alternate angles", "corresponding angles", "co-interior angles"],
        "term": 2,
        "caps_weight_percent": 18,
        "suggested_duration_mins": 5,
        "mode": mode,
        "difficulty": "medium",
        "marks": 5,
    }


def generate(seed: Optional[int] = None, mode: str = "compound", archetype: Optional[str] = None) -> Dict[str, Any]:
    r = _rng(seed)
    if archetype == "straight_line":
        return generate_straight_line_angles(r, mode=mode)
    elif archetype == "parallel_lines" or archetype == "parallel":
        return generate_parallel_lines(r, mode=mode)
    else:
        choice = r.choice(["straight_line", "parallel_lines"])
        if choice == "straight_line":
            return generate_straight_line_angles(r, mode=mode)
        else:
            return generate_parallel_lines(r, mode=mode)
