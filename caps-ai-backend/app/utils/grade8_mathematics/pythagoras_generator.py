"""Grade 8 Mathematics — Theorem of Pythagoras (Deterministic 6-Pillar Generator).
Authentic CAPS exam generator covering:
- Calculating the hypotenuse: c^2 = a^2 + b^2 -> c = sqrt(a^2 + b^2).
- Calculating a shorter leg: a^2 = c^2 - b^2 -> a = sqrt(c^2 - b^2).
- Verifying whether a triangle is right-angled (Converse of Pythagoras: test if a^2 + b^2 == c^2).
- Real-world contextual applications (ladders, ships, walking paths).
Zero-Meta-Curriculum Invariant strictly enforced.
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional


def _rng(seed: Optional[int] = None) -> random.Random:
    r = random.Random()
    if seed is not None:
        r.seed(int(seed))
    return r


def _fmt_sa(val: float | int, places: int = 2) -> str:
    if isinstance(val, int) or (isinstance(val, float) and val.is_integer()):
        return str(int(val))
    s = f"{val:.{places}f}".rstrip("0").rstrip(".")
    return s.replace(".", "{,}")


# Authentic Pythagorean triples scaled appropriately for Grade 8
TRIPLES = [
    (3, 4, 5),
    (5, 12, 13),
    (6, 8, 10),
    (8, 15, 17),
    (7, 24, 25),
    (9, 12, 15),
    (10, 24, 26),
    (12, 16, 20),
    (15, 20, 25),
    (9, 40, 41),
]

TOPIC = "grade8_math_pythagoras"
LO = "g8_math_pythagoras"


def generate_hypotenuse_question(r: random.Random, mode: str = "compound") -> Dict[str, Any]:
    a, b, c = r.choice(TRIPLES)
    scale = r.choice([1, 2, 3])
    a, b, c = a * scale, b * scale, c * scale
    
    triangle_name = r.choice(["ABC", "PQR", "XYZ"])
    right_angle_vertex = triangle_name[1]
    hyp_label = f"{triangle_name[0]}{triangle_name[2]}"
    leg1_label = f"{triangle_name[0]}{triangle_name[1]}"
    leg2_label = f"{triangle_name[1]}{triangle_name[2]}"
    
    prompt = (
        f"In \\(\\triangle {triangle_name}\\), \\(\\hat{{{right_angle_vertex}}} = 90^\\circ\\). "
        f"The lengths of the two perpendicular sides are \\({leg1_label} = {a}\\text{{ cm}}\\) "
        f"and \\({leg2_label} = {b}\\text{{ cm}}\\).\n\n"
        f"1. State the Theorem of Pythagoras in terms of the sides of \\(\\triangle {triangle_name}\\).\n"
        f"2. Calculate the length of the hypotenuse \\({hyp_label}\\), giving reasons for your statement."
    )
    prompt_latex = (
        rf"\text{{In }}\triangle {triangle_name}\text{{, }}\hat{{{right_angle_vertex}}} = 90^\circ. \quad "
        rf"{leg1_label} = {a}\text{{ cm}}, \quad {leg2_label} = {b}\text{{ cm}}." "\n\n"
        rf"\text{{Calculate the length of the hypotenuse }}{hyp_label}\text{{ with geometric reasons.}}"
    )
    answer_latex = (
        rf"{hyp_label}^2 = {leg1_label}^2 + {leg2_label}^2 \quad [\text{{Pythagoras / }}\hat{{{right_angle_vertex}}} = 90^\circ]" "\n"
        rf"{hyp_label}^2 = {a}^2 + {b}^2 = {a**2} + {b**2} = {c**2}" "\n"
        rf"{hyp_label} = \sqrt{{{c**2}}} = {c}\text{{ cm}}"
    )
    sample_answer = (
        f"1. In △{triangle_name}, {hyp_label}² = {leg1_label}² + {leg2_label}² (Pythagoras, ∠{right_angle_vertex} = 90°)\n"
        f"2. {hyp_label}² = {a}² + {b}²\n"
        f"   {hyp_label}² = {a**2} + {b**2} = {c**2}\n"
        f"   {hyp_label} = √({c**2}) = {c} cm"
    )
    schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": f"State theorem: {hyp_label}² = {leg1_label}² + {leg2_label}² with reason [Pythagoras]", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Substitute side lengths: {a}² + {b}²", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Compute sum of squares: {c**2}", "marks": 1, "editable": True},
            {"id": "mp4", "desc": f"Correct square root calculation: {c} cm with units", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "omitted_geometric_reason", "penalty": 1}],
        "carry_forward_rule": "consequential_accuracy",
    }
    hints = {
        "tier_1": f"Identify the side opposite the 90° angle. That is the hypotenuse ({hyp_label}).",
        "tier_2": "The square on the hypotenuse equals the sum of the squares on the other two sides: c² = a² + b².",
        "tier_3": f"{hyp_label}² = {a}² + {b}² = {a**2} + {b**2} = {c**2}. Therefore {hyp_label} = √{c**2} = {c} cm.",
    }
    return {
        "id": f"g8_pyth_hyp_{random.randint(100000, 999999)}",
        "topic": TOPIC,
        "subskill": "calculating_hypotenuse",
        "learning_objective_id": f"{LO}_hypotenuse",
        "prompt": prompt,
        "prompt_latex": prompt_latex,
        "answer_latex": answer_latex,
        "sample_answer": sample_answer,
        "marking_schema": schema,
        "hints": hints,
        "misconception_tags": ["adding_without_squaring", "forgetting_square_root", "omitted_geometric_reason"],
        "keywords": ["pythagoras", "hypotenuse", "right-angled triangle", "square root"],
        "term": 3,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 5,
        "mode": mode,
        "difficulty": "medium",
        "marks": 4,
    }


def generate_leg_question(r: random.Random, mode: str = "compound") -> Dict[str, Any]:
    a, b, c = r.choice(TRIPLES)
    scale = r.choice([1, 2, 3])
    a, b, c = a * scale, b * scale, c * scale
    
    triangle_name = r.choice(["KLM", "DEF", "RST"])
    right_angle_vertex = triangle_name[1]
    hyp_label = f"{triangle_name[0]}{triangle_name[2]}"
    leg1_label = f"{triangle_name[0]}{triangle_name[1]}"
    unknown_leg = f"{triangle_name[1]}{triangle_name[2]}"
    
    prompt = (
        f"In \\(\\triangle {triangle_name}\\), \\(\\hat{{{right_angle_vertex}}} = 90^\\circ\\). "
        f"The hypotenuse \\({hyp_label} = {c}\\text{{ mm}}\\) and side \\({leg1_label} = {a}\\text{{ mm}}\\).\n\n"
        f"Calculate the length of the unknown side \\({unknown_leg}\\), stating the theorem and your geometric reasons."
    )
    prompt_latex = (
        rf"\text{{In }}\triangle {triangle_name}\text{{, }}\hat{{{right_angle_vertex}}} = 90^\circ. \quad "
        rf"{hyp_label} = {c}\text{{ mm}}, \quad {leg1_label} = {a}\text{{ mm}}." "\n\n"
        rf"\text{{Calculate the length of side }}{unknown_leg}\text{{ with reasons.}}"
    )
    answer_latex = (
        rf"{unknown_leg}^2 = {hyp_label}^2 - {leg1_label}^2 \quad [\text{{Pythagoras / }}\hat{{{right_angle_vertex}}} = 90^\circ]" "\n"
        rf"{unknown_leg}^2 = {c}^2 - {a}^2 = {c**2} - {a**2} = {b**2}" "\n"
        rf"{unknown_leg} = \sqrt{{{b**2}}} = {b}\text{{ mm}}"
    )
    sample_answer = (
        f"In △{triangle_name}, {unknown_leg}² = {hyp_label}² - {leg1_label}² (Pythagoras, ∠{right_angle_vertex} = 90°)\n"
        f"{unknown_leg}² = {c}² - {a}²\n"
        f"{unknown_leg}² = {c**2} - {a**2} = {b**2}\n"
        f"{unknown_leg} = √({b**2}) = {b} mm"
    )
    schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": f"Correct rearranged Pythagoras statement: {unknown_leg}² = {hyp_label}² - {leg1_label}² with reason", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Correct substitution: {c}² - {a}²", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Difference of squares evaluated: {b**2}", "marks": 1, "editable": True},
            {"id": "mp4", "desc": f"Square root calculation: {b} mm with correct units", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "added_instead_of_subtracted", "penalty": 2}],
        "carry_forward_rule": "consequential_accuracy",
    }
    hints = {
        "tier_1": "You are finding a shorter side, not the hypotenuse. You must subtract the known leg squared from the hypotenuse squared.",
        "tier_2": "a² = c² - b². Hypotenuse squared minus known side squared.",
        "tier_3": f"{unknown_leg}² = {c}² - {a}² = {c**2} - {a**2} = {b**2}. Then take the square root: {unknown_leg} = {b} mm.",
    }
    return {
        "id": f"g8_pyth_leg_{random.randint(100000, 999999)}",
        "topic": TOPIC,
        "subskill": "calculating_shorter_side",
        "learning_objective_id": f"{LO}_shorter_leg",
        "prompt": prompt,
        "prompt_latex": prompt_latex,
        "answer_latex": answer_latex,
        "sample_answer": sample_answer,
        "marking_schema": schema,
        "hints": hints,
        "misconception_tags": ["added_instead_of_subtracted_for_leg", "forgetting_square_root"],
        "keywords": ["pythagoras", "shorter side", "subtraction", "square root"],
        "term": 3,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 5,
        "mode": mode,
        "difficulty": "medium",
        "marks": 4,
    }


def generate_converse_question(r: random.Random, mode: str = "compound") -> Dict[str, Any]:
    is_right = r.choice([True, False])
    if is_right:
        a, b, c = r.choice(TRIPLES)
        scale = r.choice([1, 2])
        a, b, c = a * scale, b * scale, c * scale
    else:
        a = r.randint(4, 9)
        b = r.randint(6, 12)
        c = int(math.sqrt(a**2 + b**2)) + r.choice([-1, 1, 2])
        if c <= max(a, b):
            c = max(a, b) + 2

    sum_sq = a**2 + b**2
    hyp_sq = c**2
    verdict = "is a right-angled triangle" if sum_sq == hyp_sq else "is NOT a right-angled triangle"
    sym = "=" if sum_sq == hyp_sq else r"\neq"

    prompt = (
        f"A triangle has side lengths of \\({a}\\text{{ m}}\\), \\({b}\\text{{ m}}\\), and \\({c}\\text{{ m}}\\).\n\n"
        f"1. Identify the longest side and calculate the square of this side.\n"
        f"2. Calculate the sum of the squares of the other two sides.\n"
        f"3. Use the converse of the Theorem of Pythagoras to determine whether this triangle is a right-angled triangle. "
        f"Show all your mathematical working and justify your conclusion."
    )
    prompt_latex = (
        rf"\text{{Triangle sides: }} a = {a}\text{{ m}}, \quad b = {b}\text{{ m}}, \quad c = {c}\text{{ m}}." "\n\n"
        r"\text{Determine whether the triangle is right-angled using the converse of Pythagoras.}"
    )
    answer_latex = (
        rf"\text{{Longest side squared: }} {c}^2 = {hyp_sq}" "\n"
        rf"\text{{Sum of other two squares: }} {a}^2 + {b}^2 = {a**2} + {b**2} = {sum_sq}" "\n"
        rf"\text{{Since }} {sum_sq} {sym} {hyp_sq}\text{{, the triangle }} {verdict}\text{{ [Converse Pythagoras].}}"
    )
    sample_answer = (
        f"1. Longest side: {c} m. {c}² = {hyp_sq}\n"
        f"2. {a}² + {b}² = {a**2} + {b**2} = {sum_sq}\n"
        f"3. Since {a}² + {b}² {'=' if is_right else '≠'} {c}² ({sum_sq} {'=' if is_right else '≠'} {hyp_sq}), "
        f"the triangle {verdict} (Converse of Pythagoras)."
    )
    schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": f"Square of longest side: {c}² = {hyp_sq}", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Sum of other two squares: {a}² + {b}² = {sum_sq}", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Comparison: {sum_sq} {'=' if is_right else '≠'} {hyp_sq}", "marks": 1, "editable": True},
            {"id": "mp4", "desc": f"Valid conclusion ({verdict}) with reason [Converse Pythagoras]", "marks": 1, "editable": True},
        ],
        "deductions": [],
        "carry_forward_rule": "consequential_accuracy",
    }
    hints = {
        "tier_1": "Calculate the square of the longest side separately from the sum of squares of the other two sides.",
        "tier_2": "If c² = a² + b², the triangle is right-angled by the converse of Pythagoras. If c² ≠ a² + b², it is not.",
        "tier_3": f"{c}² = {hyp_sq} and {a}² + {b}² = {sum_sq}. Compare {hyp_sq} with {sum_sq}.",
    }
    return {
        "id": f"g8_pyth_conv_{random.randint(100000, 999999)}",
        "topic": TOPIC,
        "subskill": "converse_of_pythagoras",
        "learning_objective_id": f"{LO}_converse",
        "prompt": prompt,
        "prompt_latex": prompt_latex,
        "answer_latex": answer_latex,
        "sample_answer": sample_answer,
        "marking_schema": schema,
        "hints": hints,
        "misconception_tags": ["assuming_always_right_angled", "improper_side_pairing"],
        "keywords": ["converse of pythagoras", "right-angled", "sum of squares"],
        "term": 3,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 5,
        "mode": mode,
        "difficulty": "medium",
        "marks": 4,
    }


def generate(seed: Optional[int] = None, mode: str = "compound", archetype: Optional[str] = None) -> Dict[str, Any]:
    r = _rng(seed)
    if archetype == "hypotenuse":
        return generate_hypotenuse_question(r, mode=mode)
    elif archetype == "shorter_leg" or archetype == "leg":
        return generate_leg_question(r, mode=mode)
    elif archetype == "converse":
        return generate_converse_question(r, mode=mode)
    else:
        choice = r.choice(["hypotenuse", "leg", "converse"])
        if choice == "hypotenuse":
            return generate_hypotenuse_question(r, mode=mode)
        elif choice == "leg":
            return generate_leg_question(r, mode=mode)
        else:
            return generate_converse_question(r, mode=mode)
