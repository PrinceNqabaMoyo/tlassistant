"""
Grade 8 Mathematics - Fractions in Decimal Notation Archetypes (26 to 50).
100% CAPS-aligned deterministic question generators.
Adheres strictly to the 6-Pillar Generator Contract and Zero-Meta-Curriculum Invariant.
Grounded in curriculum_docs_auto/Mathematics_Gr8/Term 1/05. Fractions in decimal notation.md.
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional


def _fmt_sa(val: float, places: int = 2) -> str:
    s = f"{val:.{places}f}".rstrip("0").rstrip(".") if places > 2 else f"{val:.{places}f}"
    if s == "-0":
        s = "0"
    return s.replace(".", ",")


def arch_26_addition_of_decimals_same_decimal_places(rng: random.Random) -> Dict[str, Any]:
    a = round(rng.uniform(12.15, 68.85), 2)
    b = round(rng.uniform(5.15, 34.75), 2)
    ans = round(a + b, 2)

    a_str = _fmt_sa(a, 2)
    b_str = _fmt_sa(b, 2)
    ans_str = _fmt_sa(ans, 2)

    return {
        "title": "Addition of Decimals (Same Decimal Places)",
        "topic": "Fractions in decimal notation",
        "grade": 8,
        "term": 1,
        "subskill": "26_addition_of_decimals_same_decimal_places",
        "difficulty": "easy",
        "question_text": (
            f"Calculate the sum without using a calculator:\n\n"
            f"$${a_str} + {b_str}$$"
        ),
        "correct_answer": ans_str,
        "marking_schema": [
            f"Align decimal commas and add: {ans_str} (1 mark)",
        ],
        "hints": [
            "Align the decimal commas vertically before adding.",
            f"Add the hundredths, tenths, and whole numbers: {a_str} + {b_str}.",
            f"Sum = {ans_str}.",
        ],
        "misconception_tags": ["decimal_addition_column_misalignment"],
        "diagram_spec": None,
    }


def arch_27_addition_of_decimals_different_decimal_places(rng: random.Random) -> Dict[str, Any]:
    a = round(rng.uniform(14.2, 48.9), 1)
    b = round(rng.uniform(2.15, 9.85), 2)
    c = round(rng.uniform(0.125, 0.875), 3)
    ans = round(a + b + c, 3)

    a_str = _fmt_sa(a, 1)
    b_str = _fmt_sa(b, 2)
    c_str = _fmt_sa(c, 3)
    ans_str = _fmt_sa(ans, 3)

    return {
        "title": "Addition of Decimals (Different Decimal Places)",
        "topic": "Fractions in decimal notation",
        "grade": 8,
        "term": 1,
        "subskill": "27_addition_of_decimals_different_decimal_places",
        "difficulty": "medium",
        "question_text": (
            f"Calculate the sum by vertical column addition without using a calculator:\n\n"
            f"$${a_str} + {b_str} + {c_str}$$"
        ),
        "correct_answer": ans_str,
        "marking_schema": [
            f"Add with place value alignment: {ans_str} (2 marks)",
        ],
        "hints": [
            "Add trailing zeros so all terms have three decimal places (thousandths).",
            f"Align columns: {a_str}00 + {b_str}0 + {c_str}.",
            f"Total = {ans_str}.",
        ],
        "misconception_tags": ["decimal_ragged_right_alignment_error"],
        "diagram_spec": None,
    }


def arch_28_subtraction_of_decimals_same_decimal_places(rng: random.Random) -> Dict[str, Any]:
    b = round(rng.uniform(8.15, 25.45), 2)
    diff = round(rng.uniform(10.25, 30.55), 2)
    a = round(b + diff, 2)

    a_str = _fmt_sa(a, 2)
    b_str = _fmt_sa(b, 2)
    diff_str = _fmt_sa(diff, 2)

    return {
        "title": "Subtraction of Decimals",
        "topic": "Fractions in decimal notation",
        "grade": 8,
        "term": 1,
        "subskill": "28_subtraction_of_decimals_same_decimal_places",
        "difficulty": "easy",
        "question_text": (
            f"Calculate without using a calculator:\n\n"
            f"$${a_str} - {b_str}$$"
        ),
        "correct_answer": diff_str,
        "marking_schema": [
            f"Subtract aligned decimals: {diff_str} (1 mark)",
        ],
        "hints": [
            "Keep decimal commas aligned in vertical columns.",
            f"Subtract hundredths, tenths, units, and tens: {a_str} - {b_str}.",
            f"Difference = {diff_str}.",
        ],
        "misconception_tags": ["decimal_subtraction_borrowing_slip"],
        "diagram_spec": None,
    }


def arch_29_subtraction_of_decimals_borrowing_across_zero(rng: random.Random) -> Dict[str, Any]:
    whole = rng.randint(8, 25)
    sub = round(rng.uniform(1.245, 6.875), 3)
    diff = round(whole - sub, 3)

    sub_str = _fmt_sa(sub, 3)
    diff_str = _fmt_sa(diff, 3)

    return {
        "title": "Subtraction Borrowing Across Zeros",
        "topic": "Fractions in decimal notation",
        "grade": 8,
        "term": 1,
        "subskill": "29_subtraction_of_decimals_borrowing_across_zero",
        "difficulty": "medium",
        "question_text": (
            f"Calculate the following difference without using a calculator:\n\n"
            f"$${whole} - {sub_str}$$"
        ),
        "correct_answer": diff_str,
        "marking_schema": [
            f"Write whole number as {whole},000 and subtract: {diff_str} (2 marks)",
        ],
        "hints": [
            f"Write {whole} as a decimal with three zeros: {whole},000.",
            f"Borrow across the zero digits: ${whole},000 - {sub_str}$.",
            f"Difference = {diff_str}.",
        ],
        "misconception_tags": ["borrowing_across_zero_digit_drop_error"],
        "diagram_spec": None,
    }


def arch_30_combined_addition_and_subtraction_with_parentheses(rng: random.Random) -> Dict[str, Any]:
    start = round(rng.uniform(20.5, 45.5), 2)
    p1 = round(rng.uniform(3.2, 9.4), 2)
    p2 = round(rng.uniform(2.1, 7.8), 2)
    bracket_sum = round(p1 + p2, 2)
    ans = round(start - bracket_sum, 2)

    return {
        "title": "Combined Decimal Operations with Brackets",
        "topic": "Fractions in decimal notation",
        "grade": 8,
        "term": 1,
        "subskill": "30_combined_addition_and_subtraction_with_parentheses",
        "difficulty": "medium",
        "question_text": (
            f"Evaluate the following expression according to the order of operations:\n\n"
            f"$${_fmt_sa(start, 2)} - ({_fmt_sa(p1, 2)} + {_fmt_sa(p2, 2)})$$ "
        ),
        "correct_answer": _fmt_sa(ans, 2),
        "marking_schema": [
            f"Calculate bracket first: {_fmt_sa(bracket_sum, 2)} [1M]",
            f"Subtract: {_fmt_sa(ans, 2)} [1A]",
        ],
        "hints": [
            f"First perform the addition inside brackets: {_fmt_sa(p1, 2)} + {_fmt_sa(p2, 2)} = {_fmt_sa(bracket_sum, 2)}.",
            f"Now subtract from {_fmt_sa(start, 2)}: {_fmt_sa(start, 2)} - {_fmt_sa(bracket_sum, 2)}.",
            f"Answer = {_fmt_sa(ans, 2)}.",
        ],
        "misconception_tags": ["bodmas_bracket_evaluation_order_slip"],
        "diagram_spec": None,
    }


def arch_31_multiplication_of_decimal_by_power_of_ten(rng: random.Random) -> Dict[str, Any]:
    pow_ten = rng.choice([10, 100, 1000])
    shifts = {10: 1, 100: 2, 1000: 3}[pow_ten]
    val = round(rng.uniform(0.125, 9.876), 3)
    ans = round(val * pow_ten, 3)

    val_str = _fmt_sa(val, 3)
    ans_str = _fmt_sa(ans, 2)

    return {
        "title": "Multiplying Decimals by Powers of 10",
        "topic": "Fractions in decimal notation",
        "grade": 8,
        "term": 1,
        "subskill": "31_multiplication_of_decimal_by_power_of_ten",
        "difficulty": "easy",
        "question_text": (
            f"Calculate without using a calculator:\n\n"
            f"$${val_str} \\times {pow_ten}$$"
        ),
        "correct_answer": ans_str,
        "marking_schema": [
            f"Shift comma {shifts} place(s) right: {ans_str} (1 mark)",
        ],
        "hints": [
            f"Multiplying by {pow_ten} shifts the decimal comma {shifts} place(s) to the right.",
            f"Move the comma {shifts} position(s) right in {val_str}.",
            f"Result = {ans_str}.",
        ],
        "misconception_tags": ["multiplying_power_ten_direction_reversal"],
        "diagram_spec": None,
    }


def arch_32_division_of_decimal_by_power_of_ten(rng: random.Random) -> Dict[str, Any]:
    pow_ten = rng.choice([10, 100, 1000])
    shifts = {10: 1, 100: 2, 1000: 3}[pow_ten]
    val = round(rng.uniform(15.2, 850.5), 1)
    ans = round(val / pow_ten, 4)

    val_str = _fmt_sa(val, 1)
    ans_str = _fmt_sa(ans, 4)

    return {
        "title": "Dividing Decimals by Powers of 10",
        "topic": "Fractions in decimal notation",
        "grade": 8,
        "term": 1,
        "subskill": "32_division_of_decimal_by_power_of_ten",
        "difficulty": "easy",
        "question_text": (
            f"Calculate without using a calculator:\n\n"
            f"$${val_str} \\div {pow_ten}$$"
        ),
        "correct_answer": ans_str,
        "marking_schema": [
            f"Shift comma {shifts} place(s) left: {ans_str} (1 mark)",
        ],
        "hints": [
            f"Dividing by {pow_ten} shifts the decimal comma {shifts} place(s) to the left.",
            f"Move the comma {shifts} place(s) left in {val_str}.",
            f"Result = {ans_str}.",
        ],
        "misconception_tags": ["dividing_power_ten_direction_reversal"],
        "diagram_spec": None,
    }


def arch_33_multiplication_of_decimal_by_single_digit_whole_number(rng: random.Random) -> Dict[str, Any]:
    multiplier = rng.randint(3, 9)
    val = round(rng.uniform(2.15, 8.85), 2)
    ans = round(val * multiplier, 2)

    return {
        "title": "Multiplying Decimal by Single-Digit Whole Number",
        "topic": "Fractions in decimal notation",
        "grade": 8,
        "term": 1,
        "subskill": "33_multiplication_of_decimal_by_single_digit_whole_number",
        "difficulty": "easy",
        "question_text": (
            f"Calculate without using a calculator:\n\n"
            f"$${_fmt_sa(val, 2)} \\times {multiplier}$$"
        ),
        "correct_answer": _fmt_sa(ans, 2),
        "marking_schema": [
            f"Multiply and place 2 decimal places: {_fmt_sa(ans, 2)} (1 mark)",
        ],
        "hints": [
            f"Ignore the decimal comma and multiply: {int(val * 100)} * {multiplier} = {int(ans * 100)}.",
            "Count two decimal places from the right.",
            f"Result = {_fmt_sa(ans, 2)}.",
        ],
        "misconception_tags": ["decimal_multiplication_comma_placement_error"],
        "diagram_spec": None,
    }


def arch_34_multiplication_of_decimal_by_two_digit_whole_number(rng: random.Random) -> Dict[str, Any]:
    val = round(rng.uniform(1.25, 4.75), 2)
    factor = rng.randint(12, 25)
    ans = round(val * factor, 2)

    return {
        "title": "Multiplying Decimal by Two-Digit Whole Number",
        "topic": "Fractions in decimal notation",
        "grade": 8,
        "term": 1,
        "subskill": "34_multiplication_of_decimal_by_two_digit_whole_number",
        "difficulty": "medium",
        "question_text": (
            f"Calculate the product by long multiplication:\n\n"
            f"$${_fmt_sa(val, 2)} \\times {factor}$$"
        ),
        "correct_answer": _fmt_sa(ans, 2),
        "marking_schema": [
            f"Long multiplication: {int(val * 100)} * {factor} = {int(ans * 100)} [1M]",
            f"Insert decimal comma: {_fmt_sa(ans, 2)} [1A]",
        ],
        "hints": [
            f"Multiply whole numbers first: {int(val * 100)} * {factor}.",
            "Place the decimal comma so there are 2 decimal places in the answer.",
            f"Product = {_fmt_sa(ans, 2)}.",
        ],
        "misconception_tags": ["decimal_long_multiplication_slip"],
        "diagram_spec": None,
    }


def arch_35_multiplication_of_two_decimal_fractions(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([0.2, 0.3, 0.4, 0.6, 0.7, 0.8, 1.2])
    b = rng.choice([0.03, 0.04, 0.05, 0.07, 0.08, 0.15])
    ans = round(a * b, 4)

    a_str = _fmt_sa(a, 1)
    b_str = _fmt_sa(b, 2)
    ans_str = _fmt_sa(ans, 4)

    return {
        "title": "Multiplication of Two Decimal Fractions",
        "topic": "Fractions in decimal notation",
        "grade": 8,
        "term": 1,
        "subskill": "35_multiplication_of_two_decimal_fractions",
        "difficulty": "medium",
        "question_text": (
            f"Calculate without using a calculator:\n\n"
            f"$${a_str} \\times {b_str}$$"
        ),
        "correct_answer": ans_str,
        "marking_schema": [
            f"Count decimal places and multiply: {ans_str} (2 marks)",
        ],
        "hints": [
            f"Count total decimal places: {a_str} has {len(a_str.split(',')[1])} and {b_str} has {len(b_str.split(',')[1])}.",
            f"Multiply non-decimal values and position {len(a_str.split(',')[1]) + len(b_str.split(',')[1])} decimal places.",
            f"Result = {ans_str}.",
        ],
        "misconception_tags": ["decimal_places_sum_rule_omission"],
        "diagram_spec": None,
    }


def arch_36_squaring_a_decimal_fraction(rng: random.Random) -> Dict[str, Any]:
    base = rng.choice([0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.04, 0.05, 1.1, 1.2])
    ans = round(base ** 2, 4)
    base_str = _fmt_sa(base, 2)
    ans_str = _fmt_sa(ans, 4)

    return {
        "title": "Squaring a Decimal Fraction",
        "topic": "Fractions in decimal notation",
        "grade": 8,
        "term": 1,
        "subskill": "36_squaring_a_decimal_fraction",
        "difficulty": "medium",
        "question_text": (
            f"Evaluate without using a calculator:\n\n"
            f"$$({base_str})^2$$"
        ),
        "correct_answer": ans_str,
        "marking_schema": [
            f"Square decimal: ({base_str})^2 = {ans_str} (1 mark)",
        ],
        "hints": [
            f"Squaring means multiplying the number by itself: ${base_str} \\times {base_str}$.",
            "The number of decimal places doubles in the square.",
            f"Result = {ans_str}.",
        ],
        "misconception_tags": ["decimal_power_places_confusion"],
        "diagram_spec": None,
    }


def arch_37_cubing_a_decimal_fraction(rng: random.Random) -> Dict[str, Any]:
    base = rng.choice([0.1, 0.2, 0.3, 0.4, 0.5])
    ans = round(base ** 3, 4)
    base_str = _fmt_sa(base, 1)
    ans_str = _fmt_sa(ans, 4)

    return {
        "title": "Cubing a Decimal Fraction",
        "topic": "Fractions in decimal notation",
        "grade": 8,
        "term": 1,
        "subskill": "37_cubing_a_decimal_fraction",
        "difficulty": "medium",
        "question_text": (
            f"Calculate the value of:\n\n"
            f"$$({base_str})^3$$"
        ),
        "correct_answer": ans_str,
        "marking_schema": [
            f"Cube decimal: ({base_str})^3 = {ans_str} (1 mark)",
        ],
        "hints": [
            f"$({base_str})^3 = {base_str} \\times {base_str} \\times {base_str}$.",
            "The answer must have 3 times the number of decimal places as the base.",
            f"Value = {ans_str}.",
        ],
        "misconception_tags": ["decimal_power_places_confusion"],
        "diagram_spec": None,
    }


def arch_38_square_root_of_decimal_fraction(rng: random.Random) -> Dict[str, Any]:
    pairs = [
        (0.16, 0.4),
        (0.25, 0.5),
        (0.36, 0.6),
        (0.49, 0.7),
        (0.64, 0.8),
        (0.81, 0.9),
        (0.01, 0.1),
        (0.04, 0.2),
        (0.09, 0.3),
        (1.44, 1.2),
    ]
    val, root = rng.choice(pairs)
    val_str = _fmt_sa(val, 2)
    root_str = _fmt_sa(root, 1)

    return {
        "title": "Square Root of a Decimal Fraction",
        "topic": "Fractions in decimal notation",
        "grade": 8,
        "term": 1,
        "subskill": "38_square_root_of_decimal_fraction",
        "difficulty": "medium",
        "question_text": (
            f"Find the square root without using a calculator:\n\n"
            f"$$\\sqrt{{{val_str}}}$$"
        ),
        "correct_answer": root_str,
        "marking_schema": [
            f"Calculate square root: {root_str} (1 mark)",
        ],
        "hints": [
            f"Convert to a common fraction: $\\sqrt{{{val_str}}} = \\sqrt{{\\frac{{{int(val * 100)}}}{{100}}}}$.",
            f"$\\frac{{\\sqrt{{{int(val * 100)}}}}}{{\\sqrt{{100}}}} = \\frac{{{int(root * 10)}}}{{10}} = {root_str}$.",
            f"Result = {root_str}.",
        ],
        "misconception_tags": ["square_root_decimal_places_halving_error"],
        "diagram_spec": None,
    }


def arch_39_cube_root_of_decimal_fraction(rng: random.Random) -> Dict[str, Any]:
    triplets = [
        (0.001, 0.1, 1),
        (0.008, 0.2, 8),
        (0.027, 0.3, 27),
        (0.064, 0.4, 64),
        (0.125, 0.5, 125),
    ]
    val, c_root, num = rng.choice(triplets)
    val_str = _fmt_sa(val, 3)
    root_str = _fmt_sa(c_root, 1)

    return {
        "title": "Cube Root of a Decimal Fraction",
        "topic": "Fractions in decimal notation",
        "grade": 8,
        "term": 1,
        "subskill": "39_cube_root_of_decimal_fraction",
        "difficulty": "medium",
        "question_text": (
            f"Find the cube root without using a calculator:\n\n"
            f"$$\\sqrt[3]{{{val_str}}}$$"
        ),
        "correct_answer": root_str,
        "marking_schema": [
            f"Calculate cube root: {root_str} (1 mark)",
        ],
        "hints": [
            f"Write as fraction: $\\sqrt[3]{{{val_str}}} = \\sqrt[3]{{\\frac{{{num}}}{{1000}}}}$.",
            f"$\\frac{{\\sqrt[3]{{{num}}}}}{{\\sqrt[3]{{1000}}}} = \\frac{{{int(c_root * 10)}}}{{10}} = {root_str}$.",
            f"Result = {root_str}.",
        ],
        "misconception_tags": ["cube_root_decimal_places_third_rule_error"],
        "diagram_spec": None,
    }


def arch_40_division_of_decimal_by_single_digit_whole_number(rng: random.Random) -> Dict[str, Any]:
    divisor = rng.choice([3, 4, 5, 6, 8])
    ans_int = rng.randint(12, 85)
    dividend = round((ans_int * divisor) / 100, 2)
    ans = round(dividend / divisor, 2)

    return {
        "title": "Dividing Decimal by Single-Digit Whole Number",
        "topic": "Fractions in decimal notation",
        "grade": 8,
        "term": 1,
        "subskill": "40_division_of_decimal_by_single_digit_whole_number",
        "difficulty": "easy",
        "question_text": (
            f"Calculate without using a calculator:\n\n"
            f"$${_fmt_sa(dividend, 2)} \\div {divisor}$$"
        ),
        "correct_answer": _fmt_sa(ans, 2),
        "marking_schema": [
            f"Short division: {_fmt_sa(dividend, 2)} / {divisor} = {_fmt_sa(ans, 2)} (1 mark)",
        ],
        "hints": [
            f"Divide as with whole numbers, keeping the decimal comma directly above: ${int(dividend * 100)} \\div {divisor} = {ans_int}$.",
            f"Put the comma two places from the right: {_fmt_sa(ans, 2)}.",
            f"Quotient = {_fmt_sa(ans, 2)}.",
        ],
        "misconception_tags": ["decimal_short_division_comma_slip"],
        "diagram_spec": None,
    }


def arch_41_division_of_decimal_by_decimal_divisor(rng: random.Random) -> Dict[str, Any]:
    pairs = [
        (4.8, 0.6, 8),
        (3.6, 0.09, 40),
        (2.4, 0.06, 40),
        (0.72, 0.8, 0.9),
        (0.45, 0.05, 9),
        (5.6, 0.7, 8),
        (1.44, 0.12, 12),
    ]
    a, b, ans = rng.choice(pairs)
    a_str = _fmt_sa(a, 2)
    b_str = _fmt_sa(b, 2)
    ans_str = _fmt_sa(ans, 1)

    return {
        "title": "Dividing a Decimal by a Decimal Divisor",
        "topic": "Fractions in decimal notation",
        "grade": 8,
        "term": 1,
        "subskill": "41_division_of_decimal_by_decimal_divisor",
        "difficulty": "hard",
        "question_text": (
            f"Calculate without using a calculator:\n\n"
            f"$${a_str} \\div {b_str}$$"
        ),
        "correct_answer": ans_str,
        "marking_schema": [
            f"Multiply dividend and divisor by power of 10 to make divisor a whole number [1M]",
            f"Perform division: {ans_str} [1A]",
        ],
        "hints": [
            "Multiply both numbers by 10, 100, or 1000 so the divisor becomes a whole number.",
            f"$\\frac{{{a_str}}}{{{b_str}}} = \\frac{{{a_str} \\times 100}}{{{b_str} \\times 100}}$.",
            f"Quotient = {ans_str}.",
        ],
        "misconception_tags": ["decimal_divisor_powers_of_ten_clearing_error"],
        "diagram_spec": None,
    }


def arch_42_order_of_operations_bodmas_with_decimals(rng: random.Random) -> Dict[str, Any]:
    a = round(rng.uniform(2.5, 6.5), 1)
    b = round(rng.uniform(1.2, 3.4), 1)
    c = round(rng.choice([2.0, 3.0, 4.0, 0.5]), 1)
    prod = round(b * c, 2)
    ans = round(a + prod, 2)

    return {
        "title": "Order of Operations (BODMAS) with Decimals",
        "topic": "Fractions in decimal notation",
        "grade": 8,
        "term": 1,
        "subskill": "42_order_of_operations_bodmas_with_decimals",
        "difficulty": "hard",
        "question_text": (
            f"Calculate using the correct order of operations (BODMAS):\n\n"
            f"$${_fmt_sa(a, 1)} + {_fmt_sa(b, 1)} \\times {_fmt_sa(c, 1)}$$"
        ),
        "correct_answer": _fmt_sa(ans, 2),
        "marking_schema": [
            f"Perform multiplication first: {_fmt_sa(b, 1)} * {_fmt_sa(c, 1)} = {_fmt_sa(prod, 2)} [1M]",
            f"Perform addition: {_fmt_sa(ans, 2)} [1A]",
        ],
        "hints": [
            "According to BODMAS, multiplication must be done before addition.",
            f"Multiply: ${_fmt_sa(b, 1)} \\times {_fmt_sa(c, 1)} = {_fmt_sa(prod, 2)}$.",
            f"Add: ${_fmt_sa(a, 1)} + {_fmt_sa(prod, 2)} = {_fmt_sa(ans, 2)}$.",
        ],
        "misconception_tags": ["bodmas_addition_before_multiplication_slip"],
        "diagram_spec": None,
    }


def arch_43_real_world_money_shopping_budget_and_change(rng: random.Random) -> Dict[str, Any]:
    cost1 = round(rng.uniform(14.50, 45.75), 2)
    cost2 = round(rng.uniform(8.25, 29.50), 2)
    total_cost = round(cost1 + cost2, 2)
    tendered = 100.0 if total_cost < 85 else 200.0
    change = round(tendered - total_cost, 2)

    return {
        "title": "Financial Context: Shopping Total and Change",
        "topic": "Fractions in decimal notation",
        "grade": 8,
        "term": 1,
        "subskill": "43_real_world_money_shopping_budget_and_change",
        "difficulty": "medium",
        "question_text": (
            f"A customer buys two grocery items costing **R{_fmt_sa(cost1, 2)}** and **R{_fmt_sa(cost2, 2)}**.\n\n"
            f"If the customer pays with a **R{int(tendered)}** banknote, calculate the change received."
        ),
        "correct_answer": f"R{_fmt_sa(change, 2)}",
        "marking_schema": [
            f"Calculate total cost: R{_fmt_sa(cost1, 2)} + R{_fmt_sa(cost2, 2)} = R{_fmt_sa(total_cost, 2)} [1M]",
            f"Calculate change: R{int(tendered)} - R{_fmt_sa(total_cost, 2)} = R{_fmt_sa(change, 2)} [1A]",
        ],
        "hints": [
            f"Find the total cost: $\\text{{R}}{_fmt_sa(cost1, 2)} + \\text{{R}}{_fmt_sa(cost2, 2)} = \\text{{R}}{_fmt_sa(total_cost, 2)}$.",
            f"Subtract from R{int(tendered)}: $\\text{{R}}{int(tendered)} - \\text{{R}}{_fmt_sa(total_cost, 2)}$.",
            f"Change = R{_fmt_sa(change, 2)}.",
        ],
        "misconception_tags": ["money_subtraction_cent_borrowing_slip"],
        "diagram_spec": None,
    }


def arch_44_real_world_unit_pricing_best_buy_comparison(rng: random.Random) -> Dict[str, Any]:
    unit_a = round(rng.uniform(12.50, 24.50), 2)
    unit_b = round(unit_a + rng.choice([1.50, 2.00, 2.50]), 2)

    mass_a = 2.5
    cost_a = round(unit_a * mass_a, 2)
    mass_b = 1.0
    cost_b = round(unit_b * mass_b, 2)

    return {
        "title": "Unit Pricing and Best Buy Comparison",
        "topic": "Fractions in decimal notation",
        "grade": 8,
        "term": 1,
        "subskill": "44_real_world_unit_pricing_best_buy_comparison",
        "difficulty": "medium",
        "question_text": (
            f"Brand A costs **R{_fmt_sa(cost_a, 2)}** for a **{_fmt_sa(mass_a, 1)} kg** bag of rice.\n"
            f"Brand B costs **R{_fmt_sa(cost_b, 2)}** for a **1 kg** bag of rice.\n\n"
            f"Calculate the price per kilogram of Brand A to determine which brand is cheaper per kg."
        ),
        "correct_answer": f"R{_fmt_sa(unit_a, 2)}/kg",
        "marking_schema": [
            f"Divide cost by mass: R{_fmt_sa(cost_a, 2)} / {_fmt_sa(mass_a, 1)} = R{_fmt_sa(unit_a, 2)}/kg (2 marks)",
        ],
        "hints": [
            f"Divide the total cost of Brand A by its mass: $\\text{{R}}{_fmt_sa(cost_a, 2)} \\div {_fmt_sa(mass_a, 1)}$.",
            f"Brand A rate: R{_fmt_sa(unit_a, 2)} per kg.",
            f"Brand A (R{_fmt_sa(unit_a, 2)}/kg) is cheaper than Brand B (R{_fmt_sa(unit_b, 2)}/kg).",
        ],
        "misconception_tags": ["unit_rate_division_order_error"],
        "diagram_spec": None,
    }


def arch_45_real_world_metric_length_conversion_decimals(rng: random.Random) -> Dict[str, Any]:
    mm = rng.choice([450, 780, 1250, 3400, 85])
    m_val = round(mm / 1000.0, 3)

    return {
        "title": "Metric Length Conversion (mm to m)",
        "topic": "Fractions in decimal notation",
        "grade": 8,
        "term": 1,
        "subskill": "45_real_world_metric_length_conversion_decimals",
        "difficulty": "easy",
        "question_text": (
            f"Convert **{mm} mm** to meters ($m$) by expressing your answer as a decimal fraction."
        ),
        "correct_answer": f"{_fmt_sa(m_val, 3)} m",
        "marking_schema": [
            f"Divide by 1000: {mm} / 1000 = {_fmt_sa(m_val, 3)} m (1 mark)",
        ],
        "hints": [
            "There are 1 000 millimeters in 1 meter.",
            f"Divide by 1 000: ${mm} \\div 1\\,000$.",
            f"Answer = {_fmt_sa(m_val, 3)} m.",
        ],
        "misconception_tags": ["metric_prefix_conversion_factor_confusion"],
        "diagram_spec": None,
    }


def arch_46_real_world_metric_mass_conversion_decimals(rng: random.Random) -> Dict[str, Any]:
    grams = rng.choice([350, 625, 1450, 2750, 80])
    kg_val = round(grams / 1000.0, 3)

    return {
        "title": "Metric Mass Conversion (g to kg)",
        "topic": "Fractions in decimal notation",
        "grade": 8,
        "term": 1,
        "subskill": "46_real_world_metric_mass_conversion_decimals",
        "difficulty": "easy",
        "question_text": (
            f"Convert **{grams} g** into kilograms ($kg$) as a decimal fraction."
        ),
        "correct_answer": f"{_fmt_sa(kg_val, 3)} kg",
        "marking_schema": [
            f"Divide by 1000: {grams} / 1000 = {_fmt_sa(kg_val, 3)} kg (1 mark)",
        ],
        "hints": [
            "1 kg = 1 000 g.",
            f"Divide grams by 1 000: ${grams} \\div 1\\,000$.",
            f"Result = {_fmt_sa(kg_val, 3)} kg.",
        ],
        "misconception_tags": ["metric_prefix_conversion_factor_confusion"],
        "diagram_spec": None,
    }


def arch_47_real_world_metric_capacity_conversion_decimals(rng: random.Random) -> Dict[str, Any]:
    ml = rng.choice([250, 375, 500, 750, 1500, 2250])
    litres = round(ml / 1000.0, 3)

    return {
        "title": "Metric Capacity Conversion (ml to L)",
        "topic": "Fractions in decimal notation",
        "grade": 8,
        "term": 1,
        "subskill": "47_real_world_metric_capacity_conversion_decimals",
        "difficulty": "easy",
        "question_text": (
            f"Convert **{ml} ml** into litres ($L$) as a decimal fraction."
        ),
        "correct_answer": f"{_fmt_sa(litres, 3)} L",
        "marking_schema": [
            f"Divide by 1000: {ml} / 1000 = {_fmt_sa(litres, 3)} L (1 mark)",
        ],
        "hints": [
            "1 litre = 1 000 millilitres.",
            f"Divide by 1 000: ${ml} \\div 1\\,000$.",
            f"Result = {_fmt_sa(litres, 3)} L.",
        ],
        "misconception_tags": ["capacity_conversion_power_ten_slip"],
        "diagram_spec": None,
    }


def arch_48_geometry_perimeter_of_polygon_with_decimal_dimensions(rng: random.Random) -> Dict[str, Any]:
    s1 = round(rng.uniform(3.4, 7.8), 1)
    s2 = round(rng.uniform(2.5, 6.9), 1)
    s3 = round(rng.uniform(4.2, 8.6), 1)
    perim = round(s1 + s2 + s3, 1)

    return {
        "title": "Perimeter with Decimal Dimensions",
        "topic": "Fractions in decimal notation",
        "grade": 8,
        "term": 1,
        "subskill": "48_geometry_perimeter_of_polygon_with_decimal_dimensions",
        "difficulty": "medium",
        "question_text": (
            f"A triangle has side lengths of **{_fmt_sa(s1, 1)} cm**, **{_fmt_sa(s2, 1)} cm**, and **{_fmt_sa(s3, 1)} cm**.\n\n"
            f"Calculate the perimeter of the triangle in centimeters."
        ),
        "correct_answer": f"{_fmt_sa(perim, 1)} cm",
        "marking_schema": [
            f"Add all 3 side lengths: {_fmt_sa(s1, 1)} + {_fmt_sa(s2, 1)} + {_fmt_sa(s3, 1)} = {_fmt_sa(perim, 1)} cm (1 mark)",
        ],
        "hints": [
            "The perimeter of a polygon is the total distance around its outer boundary.",
            f"Add side lengths: ${_fmt_sa(s1, 1)} + {_fmt_sa(s2, 1)} + {_fmt_sa(s3, 1)}$.",
            f"Perimeter = {_fmt_sa(perim, 1)} cm.",
        ],
        "misconception_tags": ["perimeter_formula_side_omission_slip"],
        "diagram_spec": None,
    }


def arch_49_geometry_area_of_rectangle_with_decimal_dimensions(rng: random.Random) -> Dict[str, Any]:
    length = round(rng.choice([3.5, 4.2, 5.5, 6.4]), 1)
    width = round(rng.choice([1.5, 2.5, 3.2, 4.5]), 1)
    area = round(length * width, 2)

    return {
        "title": "Rectangle Area with Decimal Dimensions",
        "topic": "Fractions in decimal notation",
        "grade": 8,
        "term": 1,
        "subskill": "49_geometry_area_of_rectangle_with_decimal_dimensions",
        "difficulty": "medium",
        "question_text": (
            f"A rectangular garden bed measures **{_fmt_sa(length, 1)} m** in length and **{_fmt_sa(width, 1)} m** in width.\n\n"
            f"Calculate the area of the garden bed in square meters ($m^2$)."
        ),
        "correct_answer": f"{_fmt_sa(area, 2)} m^2",
        "marking_schema": [
            f"Multiply length * width: {_fmt_sa(length, 1)} * {_fmt_sa(width, 1)} = {_fmt_sa(area, 2)} m^2 (2 marks)",
        ],
        "hints": [
            "Area of a rectangle = length * width.",
            f"Multiply ${_fmt_sa(length, 1)} \\times {_fmt_sa(width, 1)}$.",
            f"Area = {_fmt_sa(area, 2)} $\\text{{m}}^2$.",
        ],
        "misconception_tags": ["decimal_area_units_power_omission"],
        "diagram_spec": None,
    }


def arch_50_real_world_fuel_consumption_rate_calculation(rng: random.Random) -> Dict[str, Any]:
    dist_km = rng.choice([250, 350, 400, 500])
    fuel_rate = round(rng.choice([6.2, 7.5, 8.4, 9.6]), 1)  # litres per 100 km
    total_fuel = round((dist_km / 100.0) * fuel_rate, 2)

    return {
        "title": "Fuel Consumption Rate Calculation",
        "topic": "Fractions in decimal notation",
        "grade": 8,
        "term": 1,
        "subskill": "50_real_world_fuel_consumption_rate_calculation",
        "difficulty": "hard",
        "question_text": (
            f"A car consumes fuel at an average rate of **{_fmt_sa(fuel_rate, 1)} litres per 100 km**.\n\n"
            f"How many litres of petrol are needed for a journey of **{dist_km} km**?"
        ),
        "correct_answer": f"{_fmt_sa(total_fuel, 2)} litres",
        "marking_schema": [
            f"Calculate hundreds of km: {dist_km} / 100 = {dist_km // 100} [1M]",
            f"Multiply by rate: ({dist_km}/100) * {_fmt_sa(fuel_rate, 1)} = {_fmt_sa(total_fuel, 2)} litres [1A]",
        ],
        "hints": [
            f"Find how many 100 km intervals there are: ${dist_km} \\div 100 = {_fmt_sa(dist_km / 100.0, 1)}$.",
            f"Multiply by the consumption rate per 100 km: ${_fmt_sa(dist_km / 100.0, 1)} \\times {_fmt_sa(fuel_rate, 1)}$.",
            f"Total fuel required = {_fmt_sa(total_fuel, 2)} litres.",
        ],
        "misconception_tags": ["rate_scaling_interval_error"],
        "diagram_spec": None,
    }


BUILDERS_26_50 = [
    arch_26_addition_of_decimals_same_decimal_places,
    arch_27_addition_of_decimals_different_decimal_places,
    arch_28_subtraction_of_decimals_same_decimal_places,
    arch_29_subtraction_of_decimals_borrowing_across_zero,
    arch_30_combined_addition_and_subtraction_with_parentheses,
    arch_31_multiplication_of_decimal_by_power_of_ten,
    arch_32_division_of_decimal_by_power_of_ten,
    arch_33_multiplication_of_decimal_by_single_digit_whole_number,
    arch_34_multiplication_of_decimal_by_two_digit_whole_number,
    arch_35_multiplication_of_two_decimal_fractions,
    arch_36_squaring_a_decimal_fraction,
    arch_37_cubing_a_decimal_fraction,
    arch_38_square_root_of_decimal_fraction,
    arch_39_cube_root_of_decimal_fraction,
    arch_40_division_of_decimal_by_single_digit_whole_number,
    arch_41_division_of_decimal_by_decimal_divisor,
    arch_42_order_of_operations_bodmas_with_decimals,
    arch_43_real_world_money_shopping_budget_and_change,
    arch_44_real_world_unit_pricing_best_buy_comparison,
    arch_45_real_world_metric_length_conversion_decimals,
    arch_46_real_world_metric_mass_conversion_decimals,
    arch_47_real_world_metric_capacity_conversion_decimals,
    arch_48_geometry_perimeter_of_polygon_with_decimal_dimensions,
    arch_49_geometry_area_of_rectangle_with_decimal_dimensions,
    arch_50_real_world_fuel_consumption_rate_calculation,
]
