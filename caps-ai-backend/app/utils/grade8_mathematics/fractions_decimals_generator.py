"""Grade 8 Mathematics - Fractions, Decimals and Percentages Generator.
Covers:
  - Common fractions: addition, subtraction, multiplication, division of proper fractions and mixed numbers.
  - Decimal fractions: calculation techniques, BODMAS with decimals, South African comma formatting.
  - Percentages: percentage of a quantity, percentage increase and decrease, financial discounts.

Follows South African CAPS curriculum specifications and the 6-Pillar Generator Contract.
Strictly zero-LLM, deterministic execution.
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


def _fmt_sa(val: float, places: int = 2) -> str:
    s = f"{val:.{places}f}"
    return s.replace(".", "{,}")


def generate_grade8_fractions_decimals_question(
    seed: Optional[int] = None,
    difficulty: str = "medium",
    mode: str = "compound",
) -> Dict[str, Any]:
    r = _rng(seed)
    subskill = mode if mode.startswith("elementary_") else "fractions_decimals_percentages"

    archetype = r.choice(["fraction_addition_subtraction", "fraction_multiplication_division", "decimal_operations", "percentage_increase_decrease"])
    if subskill == "elementary_fraction_addition":
        archetype = "fraction_addition_subtraction"
    elif subskill == "elementary_decimal_multiplication":
        archetype = "decimal_operations"

    if archetype == "fraction_addition_subtraction":
        d1 = r.choice([2, 3, 4])
        d2 = r.choice([3, 5, 6])
        if d1 == d2:
            d2 = 5
        n1 = r.randint(1, d1 - 1)
        n2 = r.randint(1, d2 - 1)
        lcm = math.lcm(d1, d2)
        m1 = lcm // d1
        m2 = lcm // d2
        num_res = n1 * m1 + n2 * m2
        common_factor = math.gcd(num_res, lcm)
        simp_num = num_res // common_factor
        simp_den = lcm // common_factor

        prompt = f"Calculate and simplify your answer:\n$$\\frac{{{n1}}}{{{d1}}} + \\frac{{{n2}}}{{{d2}}}$$"
        sample_answer = (
            rf"\text{{LCM}} = {lcm}\\\ "
            rf"\frac{{{n1} \times {m1}}}{{{lcm}}} + \\frac{{{n2} \times {m2}}}{{{lcm}}} = "
            rf"\frac{{{n1 * m1} + {n2 * m2}}}{{{lcm}}} = \\frac{{{num_res}}}{{{lcm}}}"
            + (rf" = \frac{{{simp_num}}}{{{simp_den}}}" if common_factor > 1 else "")
        )

        return {
            "id": f"g8_frac_add_{random.randint(100000, 999999)}",
            "subject": "mathematics",
            "grade": "grade-8",
            "topic": "Common Fractions",
            "subskill": "fraction_addition",
            "learning_objective_id": "g8_math_fractions_addition",
            "archetype": "fraction_addition_subtraction",
            "prompt": prompt,
            "sample_answer": sample_answer,
            "correct_value": f"{simp_num}/{simp_den}",
            "marks": 3,
            "marking_schema": {
                "total_marks": 3,
                "marking_points": [
                    {"id": "mp_1", "desc": f"Finding LCM of denominators ({lcm})", "marks": 1, "editable": True},
                    {"id": "mp_2", "desc": f"Equivalent fractions {n1 * m1}/{lcm} + {n2 * m2}/{lcm}", "marks": 1, "editable": True},
                    {"id": "mp_3", "desc": f"Fully simplified answer {simp_num}/{simp_den}", "marks": 1, "editable": True},
                ],
                "deductions": [{"rule": "unsimplified_fraction", "penalty": 1}],
                "carry_forward_rule": "consequential_accuracy",
            },
            "hints": {
                "tier_1": f"Find the Lowest Common Multiple (LCM) of the denominators ${d1}$ and ${d2}$.",
                "tier_2": rf"The $\text{{LCM}} = {lcm}$. Convert both fractions to have denominator ${lcm}$: $\frac{{{n1 * m1}}}{{{lcm}}} + \frac{{{n2 * m2}}}{{{lcm}}}$.",
                "tier_3": rf"Add the numerators: $\frac{{{num_res}}}{{{lcm}}}$" + (rf" and simplify by dividing numerator and denominator by ${common_factor}$ to get $\frac{{{simp_num}}}{{{simp_den}}}$." if common_factor > 1 else "."),
            },
            "misconception_tags": ["adding_denominators_together", "incorrect_lcm", "unsimplified_fraction"],
            "term": 1,
            "caps_weight_percent": 15,
            "suggested_duration_mins": 3,
            "mode": mode,
            "difficulty": "easy",
        }

    elif archetype == "fraction_multiplication_division":
        # (a/b) * (c/d) / (e/f)
        n1 = r.choice([2, 3, 4])
        d1 = r.choice([5, 7, 9])
        n2 = r.choice([3, 5])
        d2 = r.choice([2, 4, 8])

        # Multiplication
        prod_num = n1 * n2
        prod_den = d1 * d2
        gcd_val = math.gcd(prod_num, prod_den)
        simp_num = prod_num // gcd_val
        simp_den = prod_den // gcd_val

        prompt = f"Calculate and express in simplest form:\n$$\\frac{{{n1}}}{{{d1}}} \\times \\frac{{{n2}}}{{{d2}}}$$"
        sample_answer = rf"\frac{{{n1} \times {n2}}}{{{d1} \times {d2}}} = \frac{{{prod_num}}}{{{prod_den}}}" + (rf" = \frac{{{simp_num}}}{{{simp_den}}}" if gcd_val > 1 else "")

        return {
            "id": f"g8_frac_mult_{random.randint(100000, 999999)}",
            "subject": "mathematics",
            "grade": "grade-8",
            "topic": "Common Fractions",
            "subskill": "fraction_multiplication",
            "learning_objective_id": "g8_math_fractions_multiplication",
            "archetype": "fraction_multiplication_division",
            "prompt": prompt,
            "sample_answer": sample_answer,
            "correct_value": f"{simp_num}/{simp_den}",
            "marks": 2,
            "marking_schema": {
                "total_marks": 2,
                "marking_points": [
                    {"id": "mp_1", "desc": "Multiplying numerators and denominators", "marks": 1, "editable": True},
                    {"id": "mp_2", "desc": f"Fully simplified fraction {simp_num}/{simp_den}", "marks": 1, "editable": True},
                ],
                "deductions": [],
                "carry_forward_rule": "consequential_accuracy",
            },
            "hints": {
                "tier_1": "Multiply numerators straight across, and multiply denominators straight across.",
                "tier_2": rf"$\frac{{{n1} \times {n2}}}{{{d1} \times {d2}}} = \frac{{{prod_num}}}{{{prod_den}}}$.",
                "tier_3": rf"Simplify by dividing numerator and denominator by $\text{{HCF}} = {gcd_val}$: $\frac{{{simp_num}}}{{{simp_den}}}$.",
            },
            "misconception_tags": ["cross_multiplication_confusion", "unsimplified_fraction"],
            "term": 1,
            "caps_weight_percent": 15,
            "suggested_duration_mins": 2,
            "mode": mode,
            "difficulty": "easy",
        }

    elif archetype == "decimal_operations":
        # BODMAS with decimals: a,b + c,d * e
        a = r.choice([2.4, 3.5, 5.2, 7.8])
        b = r.choice([1.2, 2.5, 0.4, 1.5])
        c = r.choice([3, 4, 2])
        prod = b * c
        ans = a + prod

        a_str = _fmt_sa(a, 1)
        b_str = _fmt_sa(b, 1)
        c_str = str(c)
        prod_str = _fmt_sa(prod, 1)
        ans_str = _fmt_sa(ans, 1)

        prompt = f"Use the correct order of operations (BODMAS) to calculate:\n$${a_str} + {b_str} \\times {c_str}$$"
        sample_answer = rf"{a_str} + ({b_str} \times {c_str}) = {a_str} + {prod_str} = {ans_str}"

        return {
            "id": f"g8_dec_bodmas_{random.randint(100000, 999999)}",
            "subject": "mathematics",
            "grade": "grade-8",
            "topic": "Decimal Fractions",
            "subskill": "decimals_bodmas",
            "learning_objective_id": "g8_math_decimals_bodmas",
            "archetype": "decimal_operations",
            "prompt": prompt,
            "sample_answer": sample_answer,
            "correct_value": ans_str,
            "marks": 2,
            "marking_schema": {
                "total_marks": 2,
                "marking_points": [
                    {"id": "mp_1", "desc": f"Multiplication first: {b_str} * {c_str} = {prod_str}", "marks": 1, "editable": True},
                    {"id": "mp_2", "desc": f"Final addition {ans_str}", "marks": 1, "editable": True},
                ],
                "deductions": [{"rule": "bodmas_violation_addition_first", "penalty": 1}],
                "carry_forward_rule": "consequential_accuracy",
            },
            "hints": {
                "tier_1": "BODMAS rule: Multiplication MUST be performed before addition.",
                "tier_2": rf"First calculate ${b_str} \times {c_str} = {prod_str}$.",
                "tier_3": rf"Now add: ${a_str} + {prod_str} = {ans_str}$.",
            },
            "misconception_tags": ["bodmas_violation_addition_first", "decimal_alignment_error"],
            "term": 1,
            "caps_weight_percent": 15,
            "suggested_duration_mins": 2,
            "mode": mode,
            "difficulty": "medium",
        }

    else:
        # Percentage Increase / Decrease
        original_price = r.choice([250, 400, 500, 800, 1200])
        pct = r.choice([10, 15, 20, 25])
        is_increase = r.choice([True, False])
        action_word = "increase" if is_increase else "decrease (discount)"
        change_amount = (original_price * pct) / 100
        final_amount = original_price + change_amount if is_increase else original_price - change_amount

        prompt = (
            f"A retail clothing store decides to {action_word} the price of a jacket originally costing "
            f"\\(\\text{{R}}\\,{original_price}\\) by \\({pct}\\%\\).\n\n"
            f"1. Calculate the amount of the {action_word}.\n"
            f"2. Determine the new selling price of the jacket."
        )
        sample_answer = (
            rf"\text{{Change}} = \frac{{{pct}}}{{100}} \times {original_price} = \text{{R}}\,{int(change_amount)}\\\ "
            rf"\text{{New Price}} = {original_price} {'+' if is_increase else '-'} {int(change_amount)} = \text{{R}}\,{int(final_amount)}"
        )

        return {
            "id": f"g8_pct_calc_{random.randint(100000, 999999)}",
            "subject": "mathematics",
            "grade": "grade-8",
            "topic": "Percentages",
            "subskill": "percentage_increase_decrease",
            "learning_objective_id": "g8_math_percentage_finance",
            "archetype": "percentage_increase_decrease",
            "prompt": prompt,
            "sample_answer": sample_answer,
            "correct_value": f"R{int(final_amount)}",
            "marks": 3,
            "marking_schema": {
                "total_marks": 3,
                "marking_points": [
                    {"id": "mp_1", "desc": f"Percentage calculation ({pct}/100 * {original_price})", "marks": 1, "editable": True},
                    {"id": "mp_2", "desc": f"Correct change amount R{int(change_amount)}", "marks": 1, "editable": True},
                    {"id": "mp_3", "desc": f"Final price R{int(final_amount)}", "marks": 1, "editable": True},
                ],
                "deductions": [],
                "carry_forward_rule": "consequential_accuracy",
            },
            "hints": {
                "tier_1": f"To find {pct}% of R{original_price}, divide {pct} by 100 and multiply by {original_price}.",
                "tier_2": rf"Change amount is $\frac{{{pct}}}{{100}} \times {original_price} = \text{{R}}\,{int(change_amount)}$.",
                "tier_3": rf"{'Add' if is_increase else 'Subtract'} this amount: $\text{{R}}\,{original_price} {'+' if is_increase else '-'} \text{{R}}\,{int(change_amount)} = \text{{R}}\,{int(final_amount)}$.",
            },
            "misconception_tags": ["added_percentage_directly_to_value", "inverted_discount_addition"],
            "term": 1,
            "caps_weight_percent": 15,
            "suggested_duration_mins": 3,
            "mode": mode,
            "difficulty": "medium",
        }


def generate(
    count: int = 1,
    seed: Optional[int] = None,
    difficulty: str = "medium",
    mode: str = "compound",
) -> List[Dict[str, Any]]:
    base_seed = seed if seed is not None else 42
    return [
        generate_grade8_fractions_decimals_question(
            seed=base_seed + i,
            difficulty=difficulty,
            mode=mode,
        )
        for i in range(count)
    ]
