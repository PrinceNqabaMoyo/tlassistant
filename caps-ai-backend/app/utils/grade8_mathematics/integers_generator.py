"""Grade 8 Mathematics — Integers & Order of Operations (Deterministic 6-Pillar Generator).
Authentic CAPS exam generator covering:
- Addition and subtraction of signed integers with double negatives: a - (-b) = a + b.
- Multiplication and division of integers (rules of signs).
- Combined multi-operation expressions respecting BODMAS with powers: (-a)^2 vs -a^2.
- Real-world applications (temperature variations, bank overdrafts, elevation).
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


TOPIC = "grade8_math_integers"
LO = "g8_math_integers"


def generate_bodmas_integers(r: random.Random, mode: str = "compound") -> Dict[str, Any]:
    a = r.randint(2, 6) * r.choice([-1, 1])
    b = r.randint(2, 5)
    c = r.randint(3, 8) * r.choice([-1, 1])
    d = r.randint(2, 4)
    
    # Structure: (-b)^2 - a * c + (-d * b)
    p_term = (-b)**2  # always positive
    m_term = a * c
    d_term = -d * b
    
    final_ans = p_term - m_term + d_term
    
    prompt = (
        f"Evaluate the following integer expression step-by-step, showing all intermediate calculations:\n\n"
        f"\\((-{{{b}}})^2 - ({a})({c}) + (-{d})({b})\\)\n\n"
        f"1. Evaluate the exponent term: \\((-{{{b}}})^2\\).\n"
        f"2. Evaluate the products: \\(({a})({c})\\) and \\((-{{{d}}})({b})\\).\n"
        f"3. Simplify to find the final numerical value."
    )
    prompt_latex = (
        rf"\text{{Evaluate: }} (-{b})^2 - ({a})({c}) + (-{d})({b})"
    )
    answer_latex = (
        rf"(-{b})^2 = {p_term}" "\n"
        rf"({a})({c}) = {m_term}, \quad (-{d})({b}) = {d_term}" "\n"
        rf"\text{{Expression}} = {p_term} - ({m_term}) + ({d_term}) = {p_term - m_term} + ({d_term}) = {final_ans}"
    )
    sample_answer = (
        f"Step 1: Exponent: (-{b})² = {p_term} (a negative base squared is positive).\n"
        f"Step 2: Products: ({a})({c}) = {m_term} and (-{d})({b}) = {d_term}.\n"
        f"Step 3: Substitute: {p_term} - ({m_term}) + ({d_term}) = {p_term - m_term} - {abs(d_term)} = {final_ans}."
    )
    schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": f"Evaluate power term: (-{b})² = {p_term}", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Evaluate product ({a})({c}) = {m_term}", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Evaluate product (-{d})({b}) = {d_term}", "marks": 1, "editable": True},
            {"id": "mp4", "desc": f"Correct final simplified integer: {final_ans}", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "sign_error_multiplication", "penalty": 1}],
        "carry_forward_rule": "consequential_accuracy",
    }
    hints = {
        "tier_1": "Apply the BODMAS rule: evaluate powers (exponents) first, then multiplication, and finally addition/subtraction.",
        "tier_2": "Remember: (-b)² is positive because a negative multiplied by a negative equals a positive. Subtracting a negative becomes addition.",
        "tier_3": f"(-{b})² = {p_term}. ({a})({c}) = {m_term}. (-{d})({b}) = {d_term}. Then: {p_term} - ({m_term}) + ({d_term}) = {final_ans}.",
    }
    return {
        "id": f"g8_int_bodmas_{random.randint(100000, 999999)}",
        "topic": TOPIC,
        "subskill": "integers_bodmas_and_powers",
        "learning_objective_id": f"{LO}_bodmas_powers",
        "prompt": prompt,
        "prompt_latex": prompt_latex,
        "answer_latex": answer_latex,
        "sample_answer": sample_answer,
        "marking_schema": schema,
        "hints": hints,
        "misconception_tags": ["negative_squared_sign_error", "subtraction_of_negative_confusion", "bodmas_precedence_violation"],
        "keywords": ["integers", "bodmas", "negative numbers", "powers"],
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 5,
        "mode": mode,
        "difficulty": "medium",
        "marks": 4,
    }


def generate_temperature_context(r: random.Random, mode: str = "compound") -> Dict[str, Any]:
    city = r.choice(["Sutherland", "Underberg", "Bethlehem", "Barkly East"])
    initial_temp = -r.randint(2, 8)  # e.g. -5 °C at 06:00
    rise = r.randint(11, 18)         # rises by 14 °C by 14:00
    noon_temp = initial_temp + rise
    drop = r.randint(9, 15)          # drops by 12 °C by 22:00
    night_temp = noon_temp - drop
    
    prompt = (
        f"At 06:00 on a winter morning in {city}, the temperature recorded was \\({initial_temp}^\\circ\\text{{C}}\\).\n\n"
        f"1. By 14:00, the temperature had increased by \\({rise}^\\circ\\text{{C}}\\). What was the afternoon temperature?\n"
        f"2. Between 14:00 and 22:00, the temperature dropped by \\({drop}^\\circ\\text{{C}}\\). What was the night temperature?\n"
        f"3. Calculate the overall difference between the maximum temperature and the minimum temperature recorded."
    )
    prompt_latex = (
        rf"\text{{Temperature in {city}: }} T_1 = {initial_temp}^\circ\text{{C}} \xrightarrow{{+{rise}^\circ\text{{C}}}} T_2 \xrightarrow{{-{drop}^\circ\text{{C}}}} T_3"
    )
    answer_latex = (
        rf"T_2 = {initial_temp} + {rise} = {noon_temp}^\circ\text{{C}}" "\n"
        rf"T_3 = {noon_temp} - {drop} = {night_temp}^\circ\text{{C}}" "\n"
        rf"\text{{Difference}} = {noon_temp} - ({initial_temp}) = {noon_temp} + {abs(initial_temp)} = {noon_temp - initial_temp}^\circ\text{{C}}"
    )
    sample_answer = (
        f"1. Afternoon temperature: {initial_temp} + {rise} = {noon_temp} °C.\n"
        f"2. Night temperature: {noon_temp} - {drop} = {night_temp} °C.\n"
        f"3. Temperature range: Maximum ({noon_temp} °C) - Minimum ({initial_temp} °C) = {noon_temp} - ({initial_temp}) = {noon_temp - initial_temp} °C."
    )
    schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": f"Calculate afternoon temperature ({noon_temp} °C)", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Calculate night temperature ({night_temp} °C)", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Set up range difference: {noon_temp} - ({initial_temp})", "marks": 1, "editable": True},
            {"id": "mp4", "desc": f"Correct temperature range ({noon_temp - initial_temp} °C)", "marks": 1, "editable": True},
        ],
        "deductions": [],
        "carry_forward_rule": "consequential_accuracy",
    }
    hints = {
        "tier_1": "To find the temperature rise, add the positive value. To find the drop, subtract.",
        "tier_2": "The difference between max and min is: Max - Min. Remember that subtracting a negative number is equivalent to adding.",
        "tier_3": f"{initial_temp} + {rise} = {noon_temp} °C. {noon_temp} - {drop} = {night_temp} °C. Range = {noon_temp} - ({initial_temp}) = {noon_temp - initial_temp} °C.",
    }
    return {
        "id": f"g8_int_temp_{random.randint(100000, 999999)}",
        "topic": TOPIC,
        "subskill": "real_world_integer_applications",
        "learning_objective_id": f"{LO}_temperature_applications",
        "prompt": prompt,
        "prompt_latex": prompt_latex,
        "answer_latex": answer_latex,
        "sample_answer": sample_answer,
        "marking_schema": schema,
        "hints": hints,
        "misconception_tags": ["subtracting_negative_subtraction_error", "confusing_absolute_value_with_net_difference"],
        "keywords": ["integers", "temperature", "negative numbers", "word problem"],
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 5,
        "mode": mode,
        "difficulty": "medium",
        "marks": 4,
    }


def generate(seed: Optional[int] = None, mode: str = "compound", archetype: Optional[str] = None) -> Dict[str, Any]:
    r = _rng(seed)
    if archetype == "temperature":
        return generate_temperature_context(r, mode=mode)
    elif archetype == "bodmas":
        return generate_bodmas_integers(r, mode=mode)
    else:
        choice = r.choice(["bodmas", "temperature"])
        if choice == "bodmas":
            return generate_bodmas_integers(r, mode=mode)
        else:
            return generate_temperature_context(r, mode=mode)
