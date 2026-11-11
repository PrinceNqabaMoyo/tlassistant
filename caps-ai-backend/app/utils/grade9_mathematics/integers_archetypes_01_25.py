"""Grade 9 Mathematics - Integers Archetypes 01 to 25.
Grounded in curriculum_docs_auto/Mathematics_Gr9/Term 1/02. Integers.md.
Covers:
  - Integer concept, number line plotting, additive inverses.
  - Contextual representations: sub-zero temperatures, elevation/depth, bank overdrafts.
  - Addition and subtraction of signed integers (including double negatives).
  - Mixed multi-term additions and subtractions.
  - Multiplication and division of signed integers (rules of signs, multiple factors).
  - Properties of operations (distributive, commutative, associative with negatives).
  - Distance between integers on the real line.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional, Tuple

from .integers_svg import (
    draw_integer_number_line_svg,
    draw_thermometer_reading_svg,
    draw_elevation_depth_svg,
)


# ----------------------------------------------------------------------
# 01. Integer Number Line Plotting and Ordering
# ----------------------------------------------------------------------
def arch_01_integer_number_line_plotting_and_ordering(rng: random.Random) -> Dict[str, Any]:
    pts = rng.sample([-7, -5, -3, -1, 2, 4, 6], 4)
    ordered = sorted(pts)
    markers = {p: str(p) for p in pts}
    svg = draw_integer_number_line_svg(min_val=-8, max_val=8, markers=markers, seed=rng.randint(100, 999999))

    prompt = (
        f"Consider the set of integers: **\\({{{', '.join(str(p) for p in pts)}}}\\)**.\n\n"
        f"1. Arrange these integers in ascending order (from smallest to greatest).\n"
        f"2. State which integer lies furthest to the left on the number line."
    )
    sol = (
        f"**Ordering Integers:**\n"
        f"1. Ascending order: \\({', '.join(str(p) for p in ordered)}\\).\n"
        f"2. Furthest to the left is the smallest integer: **{ordered[0]}**."
    )
    ans = f"1. {', '.join(str(p) for p in ordered)}; 2. {ordered[0]}"
    return {
        "id": f"g9_int_order_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "01_integer_number_line_plotting_and_ordering",
        "learning_objective_id": "math_g9_int_order",
        "hints": {
            "tier_1": "Negative numbers with larger absolute values are smaller and lie further to the left.",
            "tier_2": f"Smallest is {ordered[0]}, biggest is {ordered[-1]}.",
            "tier_3": ans,
        },
        "misconception_tags": ["thinking_negative_seven_is_greater_than_negative_one"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 02. Integer Additive Inverse Concept
# ----------------------------------------------------------------------
def arch_02_integer_additive_inverse_concept(rng: random.Random) -> Dict[str, Any]:
    n = rng.choice([-38, -25, -14, 19, 32, 45])
    inv = -n

    prompt = (
        f"For the integer **${n}$**:\n\n"
        f"1. State its **additive inverse**.\n"
        f"2. Write down the property equation confirming that this number is the additive inverse of ${n}$."
    )
    sol = (
        f"**Additive Inverse:**\n"
        f"1. The additive inverse of ${n}$ is **{inv}** (the sign reverses).\n"
        f"2. Property equation: \\({n} + ({inv}) = 0\\)."
    )
    ans = f"1. {inv}; 2. {n} + ({inv}) = 0"
    return {
        "id": f"g9_int_add_inv_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "02_integer_additive_inverse_concept",
        "learning_objective_id": "math_g9_int_add_inv",
        "hints": {
            "tier_1": "The additive inverse is the number that sums to zero with the original number.",
            "tier_2": f"-({n}) = {inv}.",
            "tier_3": ans,
        },
        "misconception_tags": ["confusing_additive_inverse_with_multiplicative_reciprocal"],
    }


# ----------------------------------------------------------------------
# 03. Thermometer Temperature Reading: Negative Celsius
# ----------------------------------------------------------------------
def arch_03_thermometer_temperature_reading_negative_celsius(rng: random.Random) -> Dict[str, Any]:
    temp = rng.choice([-25, -20, -15, -10, -5])
    svg = draw_thermometer_reading_svg(temp_c=temp, seed=rng.randint(100, 999999))

    prompt = (
        f"A laboratory freezer operates at sub-zero temperatures.\n"
        f"The temperature inside is **{temp}°C**.\n\n"
        f"1. How many degrees below the freezing point of water (0°C) is this temperature?\n"
        f"2. If the temperature drops by a further **5°C**, what will the new temperature reading be?"
    )
    sol = (
        f"**Temperature Analysis:**\n"
        f"1. The freezing point is 0°C. Distance below 0°C = \\(0 - ({temp}) = {abs(temp)}^\\circ\\text{{C}}\\).\n"
        f"2. Dropping by 5°C: \\({temp} - 5 = {temp - 5}^\\circ\\text{{C}}\\)."
    )
    ans = f"1. {abs(temp)}°C below freezing; 2. {temp - 5}°C"
    return {
        "id": f"g9_int_thermo_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "03_thermometer_temperature_reading_negative_celsius",
        "learning_objective_id": "math_g9_int_thermo",
        "hints": {
            "tier_1": "Temperatures below 0°C are negative integers.",
            "tier_2": f"Dropping 5 degrees from {temp}°C means subtracting 5.",
            "tier_3": ans,
        },
        "misconception_tags": ["adding_drop_instead_of_subtracting_further_into_negative"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 04. Temperature Change: Drop and Rise Calculation
# ----------------------------------------------------------------------
def arch_04_temperature_change_drop_and_rise_calculation(rng: random.Random) -> Dict[str, Any]:
    t_start = rng.choice([-8, -6, -4, -2])
    t_rise = rng.choice([12, 15, 18])
    t_end = t_start + t_rise

    prompt = (
        f"At 05:00 in Sutherland, the temperature was **{t_start}°C**.\n"
        f"By 14:00 in the afternoon, the temperature had risen by **{t_rise}°C**.\n\n"
        f"Calculate the temperature at 14:00, showing your integer calculation."
    )
    sol = (
        f"**Temperature Rise Calculation:**\n"
        f"\\[ \\text{{New Temperature}} = {t_start} + {t_rise} = {t_end}^\\circ\\text{{C}} \\]"
    )
    ans = f"{t_end}°C"
    return {
        "id": f"g9_int_temp_change_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "04_temperature_change_drop_and_rise_calculation",
        "learning_objective_id": "math_g9_int_temp_change",
        "hints": {
            "tier_1": f"Add the rise ({t_rise}) to the starting temperature ({t_start}).",
            "tier_2": f"{t_start} + {t_rise} = {t_end}.",
            "tier_3": ans,
        },
        "misconception_tags": ["subtracting_rise_from_starting_temperature"],
    }


# ----------------------------------------------------------------------
# 05. Elevation and Depth: Sea Level Difference
# ----------------------------------------------------------------------
def arch_05_elevation_and_depth_sea_level_difference(rng: random.Random) -> Dict[str, Any]:
    mountain = rng.choice([1200, 1500, 1800, 2400])
    depth = rng.choice([-400, -600, -800, -1200])
    diff = mountain - depth  # mountain + abs(depth)

    svg = draw_elevation_depth_svg(mountain_m=mountain, mine_m=depth, seed=rng.randint(100, 999999))

    prompt = (
        f"A weather observatory sits on a mountain peak at an altitude of **+{mountain} m** above sea level.\n"
        f"An underground research laboratory is situated in a deep mine shaft at **{depth} m** below sea level (sea level = 0 m).\n\n"
        f"Calculate the **vertical distance** (height difference) between the mountain observatory and the underground lab."
    )
    sol = (
        f"**Vertical Distance Calculation:**\n"
        f"Vertical difference = Top altitude - Bottom altitude:\n"
        f"\\[ \\Delta h = {mountain} - ({depth}) = {mountain} + {abs(depth)} = {diff} \\text{{ m}} \\]"
    )
    ans = f"{diff} m"
    return {
        "id": f"g9_int_elev_depth_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "subskill": "05_elevation_and_depth_sea_level_difference",
        "learning_objective_id": "math_g9_int_elev_depth",
        "hints": {
            "tier_1": "Vertical distance is the difference between peak and depth: top - bottom.",
            "tier_2": f"{mountain} - ({depth}) = {mountain} + {abs(depth)}.",
            "tier_3": ans,
        },
        "misconception_tags": ["subtracting_absolute_values_instead_of_accounting_for_negative_depth"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 06. Financial Bank Balance: Overdraft, Deposit, Withdrawal
# ----------------------------------------------------------------------
def arch_06_financial_bank_balance_overdraft_deposit_withdrawal(rng: random.Random) -> Dict[str, Any]:
    overdraft = rng.choice([-850, -1200, -1500, -2400])
    deposit = rng.choice([2000, 2500, 3000])
    withdrawal = rng.choice([600, 800, 1100])
    final_balance = overdraft + deposit - withdrawal

    prompt = (
        f"A small business account starts the month with an overdraft of **R {abs(overdraft)}** (balance = **R {overdraft}**).\n"
        f"During the week, the owner makes a deposit of **R {deposit}**, followed by an electronic payment withdrawal of **R {withdrawal}**.\n\n"
        f"Calculate the **final account balance**, stating clearly whether the account is in credit or overdrawn."
    )
    sol = (
        f"**Balance Calculation:**\n"
        f"\\[ \\text{{Balance}} = ({overdraft}) + {deposit} - {withdrawal} \\]\n"
        f"\\[ = {overdraft + deposit} - {withdrawal} = \\text{{R }}{final_balance} \\]\n"
        f"Conclusion: Since the balance is positive, the account is in **credit by R {final_balance}**."
    )
    ans = f"R {final_balance} (in credit)"
    return {
        "id": f"g9_int_bank_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "subskill": "06_financial_bank_balance_overdraft_deposit_withdrawal",
        "learning_objective_id": "math_g9_int_bank",
        "hints": {
            "tier_1": "An overdraft is a negative integer balance.",
            "tier_2": f"Compute: {overdraft} + {deposit} - {withdrawal}.",
            "tier_3": ans,
        },
        "misconception_tags": ["treating_overdraft_as_positive_cash_balance"],
    }


# ----------------------------------------------------------------------
# 07. Addition of Two Negative Integers
# ----------------------------------------------------------------------
def arch_07_addition_of_two_negative_integers(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(8, 25)
    b = rng.randint(7, 30)
    ans = -(a + b)

    prompt = (
        f"Evaluate the sum without using a calculator:\n\n"
        f"\\[ (-{a}) + (-{b}) \\]"
    )
    sol = (
        f"**Adding Two Negatives:**\n"
        f"When adding numbers with the same negative sign, add their magnitudes and keep the negative sign:\n"
        f"\\[ (-{a}) + (-{b}) = -({a} + {b}) = {ans} \\]"
    )
    return {
        "id": f"g9_int_add_two_neg_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": str(ans),
        "sample_answer": str(ans),
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "subskill": "07_addition_of_two_negative_integers",
        "learning_objective_id": "math_g9_int_add_two_neg",
        "hints": {
            "tier_1": "Adding two negative numbers always yields a more negative number.",
            "tier_2": f"-({a} + {b}) = {ans}.",
            "tier_3": str(ans),
        },
        "misconception_tags": ["applying_multiplication_sign_rule_to_addition_thinking_two_negatives_make_positive"],
    }


# ----------------------------------------------------------------------
# 08. Addition of Positive and Negative Integer
# ----------------------------------------------------------------------
def arch_08_addition_of_positive_and_negative_integer(rng: random.Random) -> Dict[str, Any]:
    pos = rng.randint(10, 35)
    neg = rng.randint(12, 40)
    ans = pos + (-neg)

    prompt = (
        f"Calculate the value of:\n\n"
        f"\\[ {pos} + (-{neg}) \\]"
    )
    sol = (
        f"**Calculation:**\n"
        f"Adding a negative number is equivalent to subtraction:\n"
        f"\\[ {pos} + (-{neg}) = {pos} - {neg} = {ans} \\]"
    )
    return {
        "id": f"g9_int_add_pos_neg_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": str(ans),
        "sample_answer": str(ans),
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "subskill": "08_addition_of_positive_and_negative_integer",
        "learning_objective_id": "math_g9_int_add_pos_neg",
        "hints": {
            "tier_1": f"+ (-{neg}) becomes - {neg}.",
            "tier_2": f"{pos} - {neg} = {ans}.",
            "tier_3": str(ans),
        },
        "misconception_tags": ["adding_magnitudes_instead_of_subtracting_different_signs"],
    }


# ----------------------------------------------------------------------
# 09. Subtraction: Positive Minus Larger Positive
# ----------------------------------------------------------------------
def arch_09_subtraction_positive_minus_larger_positive(rng: random.Random) -> Dict[str, Any]:
    small = rng.randint(5, 18)
    large = small + rng.randint(6, 25)
    ans = small - large

    prompt = (
        f"Evaluate without a calculator:\n\n"
        f"\\[ {small} - {large} \\]"
    )
    sol = (
        f"**Calculation:**\n"
        f"Subtracting a larger number from a smaller number produces a negative result:\n"
        f"\\[ {small} - {large} = -({large} - {small}) = {ans} \\]"
    )
    return {
        "id": f"g9_int_sub_pos_large_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": str(ans),
        "sample_answer": str(ans),
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "subskill": "09_subtraction_positive_minus_larger_positive",
        "learning_objective_id": "math_g9_int_sub_pos_large",
        "hints": {
            "tier_1": "The answer must be negative because you are subtracting more than you have.",
            "tier_2": f"-({large} - {small}) = {ans}.",
            "tier_3": str(ans),
        },
        "misconception_tags": ["inverting_order_giving_positive_difference"],
    }


# ----------------------------------------------------------------------
# 10. Subtraction of Negative Integer: Double Negative Rule
# ----------------------------------------------------------------------
def arch_10_subtraction_of_negative_integer_double_negative_rule(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(8, 25)
    b = rng.randint(5, 20)
    ans = a + b

    prompt = (
        f"Evaluate the expression:\n\n"
        f"\\[ {a} - (-{b}) \\]\n\n"
        f"Explain the operation rule used."
    )
    sol = (
        f"**Double Negative Rule:**\n"
        f"Subtracting a negative number is equivalent to adding its positive additive inverse:\n"
        f"\\[ -(-{b}) = +{b} \\]\n"
        f"\\[ {a} - (-{b}) = {a} + {b} = {ans} \\]"
    )
    return {
        "id": f"g9_int_double_neg_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": str(ans),
        "sample_answer": str(ans),
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "10_subtraction_of_negative_integer_double_negative_rule",
        "learning_objective_id": "math_g9_int_double_neg",
        "hints": {
            "tier_1": "Subtracting a negative becomes addition: -(-b) = +b.",
            "tier_2": f"{a} + {b} = {ans}.",
            "tier_3": str(ans),
        },
        "misconception_tags": ["keeping_subtraction_sign_despite_double_negative"],
    }


# ----------------------------------------------------------------------
# 11. Subtraction: Negative Minus Positive Integer
# ----------------------------------------------------------------------
def arch_11_subtraction_negative_minus_positive_integer(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(6, 20)
    b = rng.randint(5, 25)
    ans = -a - b

    prompt = (
        f"Evaluate:\n\n"
        f"\\[ -{a} - {b} \\]"
    )
    sol = (
        f"**Calculation:**\n"
        f"Starting at $-{a}$ and subtracting ${b}$ moves ${b}$ units further to the left on the number line:\n"
        f"\\[ -{a} - {b} = -({a} + {b}) = {ans} \\]"
    )
    return {
        "id": f"g9_int_neg_minus_pos_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": str(ans),
        "sample_answer": str(ans),
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "subskill": "11_subtraction_negative_minus_positive_integer",
        "learning_objective_id": "math_g9_int_neg_minus_pos",
        "hints": {
            "tier_1": "Both signs are negative, so combine their magnitudes and keep the negative sign.",
            "tier_2": f"-({a} + {b}) = {ans}.",
            "tier_3": str(ans),
        },
        "misconception_tags": ["cancelling_signs_thinking_subtraction_makes_positive"],
    }


# ----------------------------------------------------------------------
# 12. Subtraction: Negative Minus Negative Integer
# ----------------------------------------------------------------------
def arch_12_subtraction_negative_minus_negative_integer(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(8, 25)
    b = rng.randint(5, 30)
    ans = -a + b

    prompt = (
        f"Evaluate the expression:\n\n"
        f"\\[ (-{a}) - (-{b}) \\]"
    )
    sol = (
        f"**Calculation:**\n"
        f"Apply double negative rule $-(-{b}) = +{b}$:\n"
        f"\\[ (-{a}) - (-{b}) = -{a} + {b} = {ans} \\]"
    )
    return {
        "id": f"g9_int_neg_minus_neg_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": str(ans),
        "sample_answer": str(ans),
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "12_subtraction_negative_minus_negative_integer",
        "learning_objective_id": "math_g9_int_neg_minus_neg",
        "hints": {
            "tier_1": "Convert -(-b) to +b.",
            "tier_2": f"-{a} + {b} = {ans}.",
            "tier_3": str(ans),
        },
        "misconception_tags": ["combining_all_negatives_into_a_large_negative_sum"],
    }


# ----------------------------------------------------------------------
# 13. Mixed Addition and Subtraction: Three Terms
# ----------------------------------------------------------------------
def arch_13_mixed_addition_and_subtraction_three_terms(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([-15, -12, -8, 7, 11])
    b = rng.choice([-9, -6, 5, 8])
    c = rng.choice([-7, -4, 6, 9])
    ans = a + b - c

    b_str = f"+ ({b})" if b < 0 else f"+ {b}"
    c_str = f"- ({c})" if c < 0 else f"- {c}"

    prompt = (
        f"Calculate the value of the three-term integer expression:\n\n"
        f"\\[ {a} {b_str} {c_str} \\]"
    )
    sol = (
        f"**Step-by-step Working:**\n"
        f"1. Simplify signs: \\({a} {b_str} {c_str}\\)\n"
        f"2. Evaluate from left to right:\n"
        f"\\[ = ({a + b}) {c_str} = {ans} \\]"
    )
    return {
        "id": f"g9_int_mixed_3_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": str(ans),
        "sample_answer": str(ans),
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "13_mixed_addition_and_subtraction_three_terms",
        "learning_objective_id": "math_g9_int_mixed_3",
        "hints": {
            "tier_1": "Resolve consecutive signs (+ - becomes -, - - becomes +).",
            "tier_2": "Work from left to right.",
            "tier_3": str(ans),
        },
        "misconception_tags": ["sign_resolution_error_in_multi_term_addition"],
    }


# ----------------------------------------------------------------------
# 14. Mixed Addition and Subtraction: Four Terms
# ----------------------------------------------------------------------
def arch_14_mixed_addition_and_subtraction_four_terms(rng: random.Random) -> Dict[str, Any]:
    non_zeros = [x for x in range(-20, 21) if x != 0]
    nums = [rng.choice(non_zeros) for _ in range(4)]
    ans = nums[0] - nums[1] + nums[2] - nums[3]

    expr = f"{nums[0]} - ({nums[1]}) + ({nums[2]}) - ({nums[3]})"

    prompt = (
        f"Simplify the four-term expression completely:\n\n"
        f"\\[ {expr} \\]"
    )
    sol = (
        f"**Grouping Positives and Negatives:**\n"
        f"Expression: \\({expr}\\)\n"
        f"Final evaluated result: \\({ans}\\)."
    )
    return {
        "id": f"g9_int_mixed_4_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": str(ans),
        "sample_answer": str(ans),
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "14_mixed_addition_and_subtraction_four_terms",
        "learning_objective_id": "math_g9_int_mixed_4",
        "hints": {
            "tier_1": "Simplify all double signs first.",
            "tier_2": "Group positive numbers together and negative numbers together.",
            "tier_3": str(ans),
        },
        "misconception_tags": ["losing_track_of_signs_across_four_terms"],
    }


# ----------------------------------------------------------------------
# 15. Multiplication: Positive Times Negative Integer
# ----------------------------------------------------------------------
def arch_15_multiplication_positive_times_negative_integer(rng: random.Random) -> Dict[str, Any]:
    pos = rng.randint(4, 12)
    neg = rng.randint(3, 11)
    ans = - (pos * neg)

    prompt = (
        f"Calculate the product:\n\n"
        f"\\[ {pos} \\times (-{neg}) \\]"
    )
    sol = (
        f"**Multiplication Rule of Signs:**\n"
        f"A positive multiplied by a negative always gives a negative product:\n"
        f"\\[ (+) \\times (-) = (-) \\]\n"
        f"\\[ {pos} \\times (-{neg}) = {ans} \\]"
    )
    return {
        "id": f"g9_int_mult_pos_neg_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": str(ans),
        "sample_answer": str(ans),
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "subskill": "15_multiplication_positive_times_negative_integer",
        "learning_objective_id": "math_g9_int_mult_pos_neg",
        "hints": {
            "tier_1": "Positive * Negative = Negative.",
            "tier_2": f"-({pos} * {neg}) = {ans}.",
            "tier_3": str(ans),
        },
        "misconception_tags": ["thinking_product_of_opposite_signs_is_positive"],
    }


# ----------------------------------------------------------------------
# 16. Multiplication: Negative Times Negative Integer
# ----------------------------------------------------------------------
def arch_16_multiplication_negative_times_negative_integer(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(3, 12)
    b = rng.randint(4, 12)
    ans = a * b

    prompt = (
        f"Calculate the product:\n\n"
        f"\\[ (-{a}) \\times (-{b}) \\]"
    )
    sol = (
        f"**Multiplication Rule of Signs:**\n"
        f"A negative multiplied by a negative yields a positive result:\n"
        f"\\[ (-) \\times (-) = (+) \\]\n"
        f"\\[ (-{a}) \\times (-{b}) = {ans} \\]"
    )
    return {
        "id": f"g9_int_mult_neg_neg_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": str(ans),
        "sample_answer": str(ans),
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "subskill": "16_multiplication_negative_times_negative_integer",
        "learning_objective_id": "math_g9_int_mult_neg_neg",
        "hints": {
            "tier_1": "Negative * Negative = Positive.",
            "tier_2": f"{a} * {b} = {ans}.",
            "tier_3": str(ans),
        },
        "misconception_tags": ["forgetting_that_product_of_two_negatives_is_positive"],
    }


# ----------------------------------------------------------------------
# 17. Multiplication: Three Signed Integers (Odd Negatives)
# ----------------------------------------------------------------------
def arch_17_multiplication_three_signed_integers_odd_negatives(rng: random.Random) -> Dict[str, Any]:
    # 3 negative factors -> negative result
    a = rng.randint(2, 5)
    b = rng.randint(2, 4)
    c = rng.randint(2, 6)
    ans = -(a * b * c)

    prompt = (
        f"Evaluate the product of three signed integers:\n\n"
        f"\\[ (-{a}) \\times (-{b}) \\times (-{c}) \\]"
    )
    sol = (
        f"**Parity of Negative Factors:**\n"
        f"1. There are 3 negative factors (an odd count), so the final result is **negative**.\n"
        f"2. \\((-({a} \\times {b})) \\times (-{c}) = (+{a * b}) \\times (-{c}) = {ans}\\)."
    )
    return {
        "id": f"g9_int_mult_3_neg_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": str(ans),
        "sample_answer": str(ans),
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "17_multiplication_three_signed_integers_odd_negatives",
        "learning_objective_id": "math_g9_int_mult_3_neg",
        "hints": {
            "tier_1": "An odd number of negative factors gives a negative result.",
            "tier_2": f"Multiply {a} * {b} * {c} = {abs(ans)}, then apply negative sign.",
            "tier_3": str(ans),
        },
        "misconception_tags": ["assuming_all_negative_products_turn_positive"],
    }


# ----------------------------------------------------------------------
# 18. Multiplication: Four Signed Integers (Even Negatives)
# ----------------------------------------------------------------------
def arch_18_multiplication_four_signed_integers_even_negatives(rng: random.Random) -> Dict[str, Any]:
    # 2 negatives and 2 positives OR 4 negatives
    a, b, c, d = 2, 3, 2, rng.choice([2, 3, 4])
    ans = a * b * c * d

    prompt = (
        f"Determine the product:\n\n"
        f"\\[ (-{a}) \\times (-{b}) \\times (-{c}) \\times (-{d}) \\]"
    )
    sol = (
        f"**Counting Negative Factors:**\n"
        f"There are 4 negative factors (even count), which pair up into positive products:\n"
        f"\\[ [(-{a}) \\times (-{b})] \\times [(-{c}) \\times (-{d})] = (+{a*b}) \\times (+{c*d}) = {ans} \\]"
    )
    return {
        "id": f"g9_int_mult_4_neg_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": str(ans),
        "sample_answer": str(ans),
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "18_multiplication_four_signed_integers_even_negatives",
        "learning_objective_id": "math_g9_int_mult_4_neg",
        "hints": {
            "tier_1": "An even number of negative factors produces a POSITIVE answer.",
            "tier_2": f"{a} * {b} * {c} * {d} = {ans}.",
            "tier_3": str(ans),
        },
        "misconception_tags": ["assigning_negative_sign_to_product_with_even_negatives"],
    }


# ----------------------------------------------------------------------
# 19. Division: Negative Divided by Positive Integer
# ----------------------------------------------------------------------
def arch_19_division_negative_divided_by_positive_integer(rng: random.Random) -> Dict[str, Any]:
    divisor = rng.randint(3, 9)
    quotient = rng.randint(4, 12)
    dividend = divisor * quotient
    ans = -quotient

    prompt = (
        f"Evaluate the quotient:\n\n"
        f"\\[ \\frac{{-{dividend}}}{{{divisor}}} \\]"
    )
    sol = (
        f"**Division Rule of Signs:**\n"
        f"\\[ \\frac{{(-)}}{{(+)}} = (-) \\]\n"
        f"\\[ \\frac{{-{dividend}}}{{{divisor}}} = -\\left(\\frac{{{dividend}}}{{{divisor}}}\\right) = {ans} \\]"
    )
    return {
        "id": f"g9_int_div_neg_pos_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": str(ans),
        "sample_answer": str(ans),
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "subskill": "19_division_negative_divided_by_positive_integer",
        "learning_objective_id": "math_g9_int_div_neg_pos",
        "hints": {
            "tier_1": "Negative divided by positive is negative.",
            "tier_2": f"-({dividend} / {divisor}) = {ans}.",
            "tier_3": str(ans),
        },
        "misconception_tags": ["sign_error_in_division"],
    }


# ----------------------------------------------------------------------
# 20. Division: Positive Divided by Negative Integer
# ----------------------------------------------------------------------
def arch_20_division_positive_divided_by_negative_integer(rng: random.Random) -> Dict[str, Any]:
    divisor = rng.randint(3, 8)
    quotient = rng.randint(5, 12)
    dividend = divisor * quotient
    ans = -quotient

    prompt = (
        f"Evaluate the quotient:\n\n"
        f"\\[ \\frac{{{dividend}}}{{-{divisor}}} \\]"
    )
    sol = (
        f"**Division Rule of Signs:**\n"
        f"\\[ \\frac{{(+)}}{{(-)}} = (-) \\]\n"
        f"\\[ \\frac{{{dividend}}}{{-{divisor}}} = {ans} \\]"
    )
    return {
        "id": f"g9_int_div_pos_neg_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": str(ans),
        "sample_answer": str(ans),
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "subskill": "20_division_positive_divided_by_negative_integer",
        "learning_objective_id": "math_g9_int_div_pos_neg",
        "hints": {
            "tier_1": "Positive / Negative = Negative.",
            "tier_2": f"-({dividend} / {divisor}) = {ans}.",
            "tier_3": str(ans),
        },
        "misconception_tags": ["thinking_negative_denominator_makes_fraction_undefined"],
    }


# ----------------------------------------------------------------------
# 21. Division: Negative Divided by Negative Integer
# ----------------------------------------------------------------------
def arch_21_division_negative_divided_by_negative_integer(rng: random.Random) -> Dict[str, Any]:
    divisor = rng.randint(4, 9)
    quotient = rng.randint(4, 12)
    dividend = divisor * quotient
    ans = quotient

    prompt = (
        f"Evaluate the division:\n\n"
        f"\\[ \\frac{{-{dividend}}}{{-{divisor}}} \\]"
    )
    sol = (
        f"**Division of Two Negatives:**\n"
        f"\\[ \\frac{{(-)}}{{(-)}} = (+) \\]\n"
        f"\\[ \\frac{{-{dividend}}}{{-{divisor}}} = +\\left(\\frac{{{dividend}}}{{{divisor}}}\\right) = {ans} \\]"
    )
    return {
        "id": f"g9_int_div_neg_neg_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": str(ans),
        "sample_answer": str(ans),
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "subskill": "21_division_negative_divided_by_negative_integer",
        "learning_objective_id": "math_g9_int_div_neg_neg",
        "hints": {
            "tier_1": "Negative divided by negative is positive.",
            "tier_2": f"{dividend} / {divisor} = {ans}.",
            "tier_3": str(ans),
        },
        "misconception_tags": ["keeping_negative_sign_in_quotient_of_two_negatives"],
    }


# ----------------------------------------------------------------------
# 22. Combined Multiplication and Division of Signed Integers
# ----------------------------------------------------------------------
def arch_22_combined_multiplication_and_division_of_signed_integers(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([4, 6, 8, 9])
    b = rng.choice([-3, -4, -6])
    c = rng.choice([-2, 2])
    ans = (a * b) // c

    prompt = (
        f"Evaluate the fractional expression:\n\n"
        f"\\[ \\frac{{{a} \\times ({b})}}{{{c}}} \\]"
    )
    sol = (
        f"**Step-by-step Evaluation:**\n"
        f"1. Numerator: \\({a} \\times ({b}) = {a * b}\\).\n"
        f"2. Division: \\(\\frac{{{a * b}}}{{{c}}} = {ans}\\)."
    )
    return {
        "id": f"g9_int_mult_div_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": str(ans),
        "sample_answer": str(ans),
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "22_combined_multiplication_and_division_of_signed_integers",
        "learning_objective_id": "math_g9_int_mult_div",
        "hints": {
            "tier_1": "Multiply the numerator first, then divide by the denominator.",
            "tier_2": f"({a * b}) / ({c}) = {ans}.",
            "tier_3": str(ans),
        },
        "misconception_tags": ["double_sign_flip_error_in_fractional_division"],
    }


# ----------------------------------------------------------------------
# 23. Properties: Distributive Law with Negative Multiplier
# ----------------------------------------------------------------------
def arch_23_properties_distributive_law_with_negative_multiplier(rng: random.Random) -> Dict[str, Any]:
    k = -rng.randint(3, 7)
    x_val = rng.randint(4, 9)
    y_val = -rng.randint(2, 6)
    ans = k * (x_val + y_val)
    term1 = k * x_val
    term2 = k * y_val

    prompt = (
        f"Expand and evaluate using the distributive property:\n\n"
        f"\\[ {k} \\times ({x_val} + ({y_val})) \\]\n\n"
        f"Show both individual products and the final sum."
    )
    sol = (
        f"**Distributive Property:**\n"
        f"\\[ {k}({x_val} + ({y_val})) = [{k} \\times {x_val}] + [{k} \\times ({y_val})] \\]\n"
        f"\\[ = ({term1}) + (+{term2}) = {ans} \\]"
    )
    return {
        "id": f"g9_int_distrib_neg_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": str(ans),
        "sample_answer": str(ans),
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "23_properties_distributive_law_with_negative_multiplier",
        "learning_objective_id": "math_g9_int_distrib_neg",
        "hints": {
            "tier_1": f"Multiply {k} by {x_val}, and {k} by {y_val}.",
            "tier_2": f"({term1}) + ({term2}) = {ans}.",
            "tier_3": str(ans),
        },
        "misconception_tags": ["distributing_negative_sign_only_to_first_bracket_term"],
    }


# ----------------------------------------------------------------------
# 24. Properties: Commutative and Associative with Signed Integers
# ----------------------------------------------------------------------
def arch_24_properties_commutative_and_associative_signed_integers(rng: random.Random) -> Dict[str, Any]:
    a, b = -8, 14
    prop = "Commutative property of addition"

    prompt = (
        f"Name the mathematical property that guarantees that:\n\n"
        f"\\[ (-8) + 14 = 14 + (-8) \\]"
    )
    sol = (
        f"**Property Identification:**\n"
        f"Changing the order of terms in addition does not affect the sum: **{prop}**."
    )
    return {
        "id": f"g9_int_comm_assoc_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": prop,
        "sample_answer": prop,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "subskill": "24_properties_commutative_and_associative_signed_integers",
        "learning_objective_id": "math_g9_int_comm_assoc",
        "hints": {
            "tier_1": "Changing the order of addition is commutative.",
            "tier_2": "a + b = b + a.",
            "tier_3": prop,
        },
        "misconception_tags": ["confusing_commutative_with_associative_property"],
    }


# ----------------------------------------------------------------------
# 25. Difference Between Integers: Distance on Number Line
# ----------------------------------------------------------------------
def arch_25_difference_between_integers_distance_on_number_line(rng: random.Random) -> Dict[str, Any]:
    p1 = -rng.randint(3, 7)
    p2 = rng.randint(4, 8)
    dist = p2 - p1

    svg = draw_integer_number_line_svg(
        min_val=-8,
        max_val=8,
        markers={p1: f"A({p1})", p2: f"B({p2})"},
        jump=(p1, p2, f"Distance = {dist}"),
        seed=rng.randint(100, 999999),
    )

    prompt = (
        f"Point $A$ lies at **{p1}** and Point $B$ lies at **{p2}** on an integer number line.\n\n"
        f"Calculate the **distance** between Point $A$ and Point $B$."
    )
    sol = (
        f"**Distance on Number Line:**\n"
        f"Distance is the absolute difference between coordinates:\n"
        f"\\[ \\text{{Distance}} = {p2} - ({p1}) = {p2} + {abs(p1)} = {dist} \\text{{ units}} \\]"
    )
    ans = f"{dist} units"
    return {
        "id": f"g9_int_distance_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "25_difference_between_integers_distance_on_number_line",
        "learning_objective_id": "math_g9_int_distance",
        "hints": {
            "tier_1": "Distance between a and b is |b - a|.",
            "tier_2": f"{p2} - ({p1}) = {dist}.",
            "tier_3": ans,
        },
        "misconception_tags": ["reporting_negative_distance"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }
