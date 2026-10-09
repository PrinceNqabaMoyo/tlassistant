"""
Grade 7 Mathematics - Integers Generator
100% CAPS-aligned deterministic question generator.
Adheres strictly to the 6-Pillar Generator Contract and Zero-Meta-Curriculum Invariant.
Directly grounded in curriculum_docs/Mathematics_Gr7/Numbers-Operations-and-Relationships.md
and curriculum_docs_auto/Mathematics_Gr7/Term 1/1. Whole numbers and integers.md

Topics Covered (Grade 7 Term 1 CAPS):
- Counting, ordering, and comparing integers on a number line
- Addition and subtraction of positive and negative integers
- Real-world contexts: temperature changes, bank balances (debt vs deposit), elevation
- Additive inverse property: a + (-a) = 0
- Subtracting a negative integer: a - (-b) = a + b
"""

from __future__ import annotations
import random
from typing import Any, Dict, List, Optional


def _generate_temperature_context_question(rng: random.Random) -> Dict[str, Any]:
    """Generates real-world temperature drop/rise integer problem."""
    cities = [
        ("Sutherland", -5, 12),
        ("Bethlehem", -3, 14),
        ("Bloemfontein", -2, 16),
        ("Johannesburg", 4, 18),
        ("Underberg", -4, 11)
    ]
    city, min_t, max_t = rng.choice(cities)
    t_start = min_t + rng.randint(-3, 2)
    t_rise = rng.randint(8, 18)
    t_end = t_start + t_rise

    prompt = (
        f"At 06:00 in **{city}**, the temperature was **{t_start}^\\circ\\text{{C}}**.\n\n"
        f"By 14:00 in the afternoon, the temperature had **risen by {t_rise}^\\circ\\text{{C}}**.\n\n"
        f"1. Write down an integer addition statement to model this temperature change.\n"
        f"2. Calculate the temperature at 14:00.\n"
        f"3. Later that evening, the temperature dropped by **{t_rise + rng.randint(2, 6)}^\\circ\\text{{C}}** from its 14:00 reading. "
        f"Calculate the new night temperature."
    )

    t_drop = t_rise + rng.randint(2, 6)
    t_night = t_end - t_drop

    sol = (
        f"**Step 1:** Model the temperature rise:\n\n"
        f"$$\\text{{Temperature at 14:00}} = ({t_start}) + {t_rise} = {t_end}^\\circ\\text{{C}}$$\n\n"
        f"**Step 2:** Model the temperature drop:\n\n"
        f"$$\\text{{Night temperature}} = {t_end} - {t_drop} = {t_night}^\\circ\\text{{C}}$$\n\n"
        f"$$\\therefore \\text{{Final reading is }} {t_night}^\\circ\\text{{C}}$$"
    )

    return {
        "id": f"g7_math_int_temp_{rng.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": f"14:00 = {t_end}; Night = {t_night}",
        "answer_latex": f"{t_end}^\\circ\\text{{C}},\\ {t_night}^\\circ\\text{{C}}",
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 4,
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 4,
        "subskill": "integers_in_context",
        "learning_objective_id": "math_g7_integers_temperature_context",
        "misconception_tags": [
            "subtracting_negative_inversion",
            "negative_sign_subtraction_slip",
            "absolute_value_confusion"
        ],
        "diagnostic_tags": ["integers", "number_line", "directed_numbers"],
        "minimum_mastery_score": 75,
        "keywords": ["integers", "temperature", "degrees Celsius", "rise", "drop"],
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp_1", "desc": "Correct integer expression modeling temperature rise", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Accurate calculation of afternoon temperature", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "Correct integer expression for night temperature drop", "marks": 1, "editable": True},
                {"id": "mp_4", "desc": "Accurate final negative integer temperature", "marks": 1, "editable": True}
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy"
        },
        "hints": {
            "tier_1": f"Think of a thermometer or vertical number line. Moving up is positive, moving down is negative.",
            "tier_2": f"Start at {t_start}. Rising by {t_rise} means ({t_start}) + {t_rise}. Dropping means subtracting.",
            "tier_3": f"({t_start}) + {t_rise} = {t_end}. Then {t_end} - {t_drop} = {t_night}."
        }
    }


def _generate_integer_operations_question(rng: random.Random) -> Dict[str, Any]:
    """Generates multi-term integer calculation testing rules of signs."""
    a = rng.choice([-15, -12, -9, -8, -6, 7, 9, 11])
    b = rng.choice([-7, -5, -4, -3, 4, 6, 8])
    c = rng.choice([-9, -6, -4, 5, 8])

    expr_type = rng.choice(["add_sub_chain", "subtracting_negative", "bracket_inverse"])

    if expr_type == "subtracting_negative":
        x = rng.randint(-18, -4)
        y = rng.randint(-15, -2)
        ans = x - y
        prompt = (
            f"Calculate the value of the following integer expression:\n\n"
            f"$${x} - ({y})$$\n\n"
            f"1. State the rule for subtracting a negative number.\n"
            f"2. Simplify the expression and find the final answer."
        )
        sol = (
            f"**Step 1:** Subtracting a negative is equivalent to adding its additive inverse:\n\n"
            f"$$a - (-b) = a + b$$\n\n"
            f"**Step 2:** Apply to the numbers:\n\n"
            f"$${x} - ({y}) = {x} + {abs(y)} = {ans}$$\n\n"
            f"$$\\therefore \\text{{Answer is }} {ans}$$"
        )
        target_ans = ans
    else:
        ans = a + b - c
        prompt = (
            f"Simplify the following integer expression step-by-step:\n\n"
            f"$$({a}) + ({b}) - ({c})$$\n\n"
            f"1. Perform the first addition: $({a}) + ({b})$.\n"
            f"2. Subtract $({c})$ from your result to find the final integer."
        )
        first_step = a + b
        sol = (
            f"**Step 1:** Add the first two integers:\n\n"
            f"$$({a}) + ({b}) = {first_step}$$\n\n"
            f"**Step 2:** Subtract the third integer:\n\n"
            f"$${first_step} - ({c}) = {ans}$$\n\n"
            f"$$\\therefore \\text{{Answer is }} {ans}$$"
        )
        target_ans = ans

    return {
        "id": f"g7_math_int_op_{rng.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": str(target_ans),
        "answer_latex": f"{target_ans}",
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 3,
        "subskill": "integer_arithmetic_rules",
        "learning_objective_id": "math_g7_integers_operations_rules",
        "misconception_tags": [
            "subtracting_negative_inversion",
            "adding_two_negatives_gives_positive_confusion",
            "sign_multiplication_in_addition"
        ],
        "diagnostic_tags": ["integers", "signs_rule", "directed_numbers"],
        "minimum_mastery_score": 75,
        "keywords": ["integers", "negative", "positive", "subtract negative", "additive inverse"],
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp_1", "desc": "Correct application of double negative / sign rule", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Accurate intermediate sum or subtraction", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "Accurate final integer with correct sign", "marks": 1, "editable": True}
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy"
        },
        "hints": {
            "tier_1": f"Pay careful attention to the signs in front of each number. Two negatives together (minus a minus) become a plus.",
            "tier_2": f"Subtracting a negative number is the same as adding a positive: -(-y) = +y.",
            "tier_3": f"Evaluate step-by-step: the final evaluated integer is {target_ans}."
        }
    }


def _generate_number_line_ordering_question(rng: random.Random) -> Dict[str, Any]:
    """Generates integer ordering and comparison problem on the number line."""
    nums = rng.sample(range(-25, 25), 6)
    nums_sorted_asc = sorted(nums)
    nums_str = ", ".join(str(n) for n in nums)
    sorted_str = ", ".join(str(n) for n in nums_sorted_asc)

    prompt = (
        f"Consider the following set of integers:\n\n"
        f"$$\\{{{nums_str}\\}}$$\n\n"
        f"1. Arrange the integers in **ascending order** (from smallest to largest).\n"
        f"2. Write down the **additive inverse** of the smallest integer in the list.\n"
        f"3. Insert either $>$ or $<$ between the two integers with the largest absolute values."
    )

    smallest = nums_sorted_asc[0]
    inverse_smallest = -smallest

    sol = (
        f"**Step 1:** Arrange in ascending order on the number line (further left is smaller):\n\n"
        f"$${sorted_str}$$\n\n"
        f"**Step 2:** Additive inverse of the smallest integer (${smallest}$):\n\n"
        f"$$\\text{{Additive inverse of }} {smallest} = {inverse_smallest}$$\n\n"
        f"**Step 3:** The smallest integer is ${smallest}$, which is further to the left on the number line than all other values."
    )

    return {
        "id": f"g7_math_int_order_{rng.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": sorted_str,
        "answer_latex": f"{sorted_str}",
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 4,
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 4,
        "subskill": "integers_ordering_number_line",
        "learning_objective_id": "math_g7_integers_ordering_inverse",
        "misconception_tags": [
            "greater_magnitude_negative_mistaken_for_larger",
            "zero_omission_on_number_line",
            "additive_inverse_sign_slip"
        ],
        "diagnostic_tags": ["integers", "number_line", "ordering"],
        "minimum_mastery_score": 75,
        "keywords": ["integers", "ascending order", "number line", "additive inverse", "smallest"],
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp_1", "desc": "Correct placement of negative integers in order", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "Correct placement of positive integers in order", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "Identification of additive inverse of smallest integer", "marks": 1, "editable": True}
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy"
        },
        "hints": {
            "tier_1": f"Remember: for negative numbers, the larger the numeral after the minus sign, the smaller the number is (it is further to the left).",
            "tier_2": f"Smallest negative number is the one furthest below zero. Order from left to right on the number line.",
            "tier_3": f"Ascending order: {sorted_str}."
        }
    }


def generate(
    count: int = 1,
    seed: Optional[int] = None,
    difficulty: str = "medium",
    mode: str = "compound",
    subskill: Optional[str] = None,
    **kwargs
) -> List[Dict[str, Any]]:
    """
    Main entry point for Grade 7 Integers Question Generator.
    Supports atomic micro-drills:
    - mode="elementary_temperature"
    - mode="elementary_operations"
    - mode="elementary_ordering"
    - mode="compound"
    """
    rng = random.Random(seed) if seed is not None else random.Random()
    questions = []

    for _ in range(count):
        if mode == "elementary_temperature" or subskill == "temperature":
            q = _generate_temperature_context_question(rng)
        elif mode == "elementary_ordering" or subskill == "ordering":
            q = _generate_number_line_ordering_question(rng)
        elif mode == "elementary_operations" or subskill == "operations":
            q = _generate_integer_operations_question(rng)
        else: # compound: pick across all archetypes
            archetype = rng.choice([
                _generate_temperature_context_question,
                _generate_integer_operations_question,
                _generate_number_line_ordering_question
            ])
            q = archetype(rng)
        questions.append(q)

    return questions
