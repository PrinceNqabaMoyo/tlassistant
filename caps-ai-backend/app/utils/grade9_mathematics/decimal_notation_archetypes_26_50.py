"""Grade 9 Mathematics - Decimal Notation Archetypes 26 to 50.
Grounded in curriculum_docs_auto/Mathematics_Gr9/Term 1/01. The decimal notation for fractions.md:
Subtraction with borrowing, multiplication/division by powers of 10 and decimals,
squares, cubes, roots of decimals, BODMAS, Olympic timing comparisons, rates, and multi-step evaluation.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from .decimal_notation_svg import (
    draw_olympic_timing_board_svg,
)


# ----------------------------------------------------------------------
# 26. Subtraction of Two Decimals with Borrowing
# ----------------------------------------------------------------------
def arch_26_subtraction_of_two_decimals_with_borrowing(rng: random.Random) -> Dict[str, Any]:
    a = round(rng.uniform(25.1, 48.2), 2)
    b = round(rng.uniform(8.5, 20.8), 2)
    if b > a:
        a, b = b, a
    diff = round(a - b, 2)

    a_str = f"{a:.2f}".replace(".", ",")
    b_str = f"{b:.2f}".replace(".", ",")
    diff_str = f"{diff:.2f}".replace(".", ",")

    prompt = (
        f"Calculate the difference by vertical alignment, borrowing across place values where necessary:\n\n"
        f"\\[ {a_str} - {b_str} \\]"
    )
    sol = (
        f"**Vertical Decimal Subtraction:**\n"
        f"Align place value columns and borrow:\n"
        f"\\({a_str} - {b_str} = {diff_str}\\)."
    )
    return {
        "id": f"g9_dec_sub_borrow_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": diff_str,
        "expected_answer": diff_str,
        "sample_answer": diff_str,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": "Align commas and execute column borrowing", "marks": 1},
            {"desc": f"Accurate difference {diff_str}", "marks": 1},
        ],
        "hints": [
            "Align the decimal commas vertically.",
            "Borrow from the tenths or units column as needed.",
            f"Difference: {diff_str}.",
        ],
    }


# ----------------------------------------------------------------------
# 27. Subtraction: Whole Number Minus Multi-Decimal
# ----------------------------------------------------------------------
def arch_27_subtraction_whole_number_minus_multi_decimal(rng: random.Random) -> Dict[str, Any]:
    w = rng.randint(10, 30)
    sub_val = round(rng.uniform(2.15, 8.85), 3)
    diff = round(w - sub_val, 3)

    sub_str = f"{sub_val:.3f}".replace(".", ",")
    diff_str = f"{diff:.3f}".replace(".", ",")

    prompt = (
        f"Subtract the decimal fraction from the whole number:\n\n"
        f"\\[ {w} - {sub_str} \\]"
    )
    sol = (
        f"**Borrowing Across Zeros:**\n"
        f"Write \\({w}\\) as \\({w}{{,}}000\\).\n"
        f"\\({w}{{,}}000 - {sub_str} = {diff_str}\\)."
    )
    return {
        "id": f"g9_dec_sub_whole_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": diff_str,
        "expected_answer": diff_str,
        "sample_answer": diff_str,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"Express {w} as {w},000", "marks": 1},
            {"desc": f"Correct difference {diff_str}", "marks": 1},
        ],
        "hints": [
            f"Annex three zeros after a decimal comma: {w},000.",
            "Subtract column by column borrowing across zeros.",
            f"Answer: {diff_str}.",
        ],
    }


# ----------------------------------------------------------------------
# 28. Combined Addition and Subtraction Word Problem
# ----------------------------------------------------------------------
def arch_28_combined_addition_and_subtraction_word_problem(rng: random.Random) -> Dict[str, Any]:
    tot_length = round(rng.uniform(15.0, 25.0), 1)
    cut1 = round(rng.uniform(3.4, 7.8), 2)
    cut2 = round(rng.uniform(4.1, 6.5), 2)
    leftover = round(tot_length - cut1 - cut2, 2)

    t_str = f"{tot_length:.1f}".replace(".", ",")
    c1_str = f"{cut1:.2f}".replace(".", ",")
    c2_str = f"{cut2:.2f}".replace(".", ",")
    ans_str = f"{leftover:.2f}".replace(".", ",")

    prompt = (
        f"A fabric roll has a total length of \\({t_str}\\text{{ m}}\\). A tailor cuts off "
        f"\\({c1_str}\\text{{ m}}\\) on Monday and \\({c2_str}\\text{{ m}}\\) on Tuesday. "
        f"What length of fabric remains on the roll?"
    )
    sol = (
        f"**Remaining Length:**\n"
        f"Total cut: \\({c1_str} + {c2_str} = {cut1 + cut2:.2f}\\text{{ m}}\\).\n"
        f"Remaining: \\({t_str} - {cut1 + cut2:.2f} = {ans_str}\\text{{ m}}\\)."
    )
    return {
        "id": f"g9_dec_word_add_sub_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"{ans_str} m",
        "expected_answer": f"{ans_str} m",
        "sample_answer": f"{ans_str} m",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "marking_schema": [
            {"desc": "Sum the two cut lengths", "marks": 1},
            {"desc": "Subtract total cut from initial roll length", "marks": 1},
            {"desc": f"Correct remaining length {ans_str} m", "marks": 1},
        ],
        "hints": [
            "First add the two pieces that were cut off.",
            "Then subtract that sum from the initial total length.",
            f"Remaining: {ans_str} m.",
        ],
    }


# ----------------------------------------------------------------------
# 29. Multiplication by Powers of Ten: 10, 100, 1000
# ----------------------------------------------------------------------
def arch_29_multiplication_by_powers_of_ten_10_100_1000(rng: random.Random) -> Dict[str, Any]:
    w = rng.randint(2, 9)
    d1 = rng.randint(1, 9)
    d2 = rng.randint(1, 9)
    d3 = rng.randint(1, 9)
    val = w + d1 / 10 + d2 / 100 + d3 / 1000
    pwr = rng.choice([10, 100, 1000])

    val_str = f"{val:.3f}".replace(".", ",")
    res = round(val * pwr, 3)
    res_str = f"{res:.3f}".rstrip("0").rstrip(".").replace(".", ",")

    prompt = (
        f"Calculate without using a calculator, stating how the decimal comma shifts:\n\n"
        f"\\[ {val_str} \\times {pwr} \\]"
    )
    sol = (
        f"**Multiplication by {pwr}:**\n"
        f"Multiplying by \\({pwr}\\) shifts the decimal comma "
        f"\\({1 if pwr==10 else (2 if pwr==100 else 3)}\\) place(s) to the right.\n"
        f"Result: \\({res_str}\\)."
    )
    return {
        "id": f"g9_dec_mul_pwr10_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": res_str,
        "expected_answer": res_str,
        "sample_answer": res_str,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "marking_schema": [
            {"desc": f"Shift comma {1 if pwr==10 else (2 if pwr==100 else 3)} positions right: {res_str}", "marks": 1},
        ],
        "hints": [
            f"Multiplying by {pwr} moves the decimal comma right by {1 if pwr==10 else (2 if pwr==100 else 3)} places.",
            f"Answer: {res_str}.",
        ],
    }


# ----------------------------------------------------------------------
# 30. Multiplication of Decimal by Single-Digit Whole
# ----------------------------------------------------------------------
def arch_30_multiplication_of_decimal_by_single_digit_whole(rng: random.Random) -> Dict[str, Any]:
    dec = round(rng.uniform(2.15, 8.75), 2)
    m = rng.choice([3, 4, 6, 7, 8])
    prod = round(dec * m, 2)

    dec_str = f"{dec:.2f}".replace(".", ",")
    prod_str = f"{prod:.2f}".replace(".", ",")

    prompt = (
        f"Calculate the product:\n\n"
        f"\\[ {dec_str} \\times {m} \\]"
    )
    sol = (
        f"**Multiplication Steps:**\n"
        f"1. Multiply as whole numbers: \\({int(round(dec*100))} \\times {m} = {int(round(prod*100))}\\).\n"
        f"2. Place 2 decimal digits in the answer: \\({prod_str}\\)."
    )
    return {
        "id": f"g9_dec_mul_single_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": prod_str,
        "expected_answer": prod_str,
        "sample_answer": prod_str,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": "Multiply as integers", "marks": 1},
            {"desc": f"Correctly insert 2 decimal places: {prod_str}", "marks": 1},
        ],
        "hints": [
            f"Multiply {int(round(dec*100))} by {m}.",
            "Count 2 decimal places from the right.",
            f"Product: {prod_str}.",
        ],
    }


# ----------------------------------------------------------------------
# 31. Multiplication of Decimal by Two-Digit Whole
# ----------------------------------------------------------------------
def arch_31_multiplication_of_decimal_by_two_digit_whole(rng: random.Random) -> Dict[str, Any]:
    dec = round(rng.uniform(3.4, 9.8), 1)
    m = rng.randint(12, 35)
    prod = round(dec * m, 1)

    dec_str = f"{dec:.1f}".replace(".", ",")
    prod_str = f"{prod:.1f}".replace(".", ",")

    prompt = (
        f"Calculate the product by long multiplication:\n\n"
        f"\\[ {dec_str} \\times {m} \\]"
    )
    sol = (
        f"**Long Multiplication:**\n"
        f"\\({int(round(dec*10))} \\times {m} = {int(round(prod*10))}\\).\n"
        f"Inserting 1 decimal place gives: \\({prod_str}\\)."
    )
    return {
        "id": f"g9_dec_mul_two_digit_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": prod_str,
        "expected_answer": prod_str,
        "sample_answer": prod_str,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": "Execute long multiplication", "marks": 1},
            {"desc": f"Place decimal comma correctly: {prod_str}", "marks": 1},
        ],
        "hints": [
            f"Multiply {int(round(dec*10))} by {m}.",
            "Place 1 decimal digit in the product.",
            f"Result: {prod_str}.",
        ],
    }


# ----------------------------------------------------------------------
# 32. Multiplication of Two Decimals: Tenths by Tenths
# ----------------------------------------------------------------------
def arch_32_multiplication_of_two_decimals_tenths_by_tenths(rng: random.Random) -> Dict[str, Any]:
    d1 = rng.randint(3, 9)
    d2 = rng.randint(4, 9)
    prod = round((d1 / 10) * (d2 / 10), 2)

    d1_str = f"0{{,}}{d1}"
    d2_str = f"0{{,}}{d2}"
    prod_str = f"{prod:.2f}".replace(".", ",")

    prompt = (
        f"Calculate the product of two tenths:\n\n"
        f"\\[ {d1_str} \\times {d2_str} \\]"
    )
    sol = (
        f"**Tenths × Tenths Rule:**\n"
        f"\\(\\frac{{{d1}}}{{10}} \\times \\frac{{{d2}}}{{10}} = \\frac{{{d1*d2}}}{{100}} = {prod_str}\\)."
    )
    return {
        "id": f"g9_dec_mul_tenths_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": prod_str,
        "expected_answer": prod_str,
        "sample_answer": prod_str,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "marking_schema": [
            {"desc": f"Tenths × tenths gives hundredths: {prod_str}", "marks": 1},
        ],
        "hints": [
            f"Multiply {d1} * {d2} = {d1*d2}.",
            "Tenths multiplied by tenths yields hundredths (2 decimal places).",
            f"Answer: {prod_str}.",
        ],
    }


# ----------------------------------------------------------------------
# 33. Multiplication of Two Decimals: Hundredths by Tenths
# ----------------------------------------------------------------------
def arch_33_multiplication_of_two_decimals_hundredths_by_tenths(rng: random.Random) -> Dict[str, Any]:
    a = round(rng.choice([1.25, 2.15, 3.45, 0.75, 4.25]), 2)
    b = round(rng.choice([0.3, 0.4, 0.6, 0.7, 0.8]), 1)
    prod = round(a * b, 3)

    a_str = f"{a:.2f}".replace(".", ",")
    b_str = f"{b:.1f}".replace(".", ",")
    prod_str = f"{prod:.3f}".replace(".", ",")

    prompt = (
        f"Calculate the product:\n\n"
        f"\\[ {a_str} \\times {b_str} \\]"
    )
    sol = (
        f"**Decimal Decimal Multiplication:**\n"
        f"Count decimal places: \\({a_str}\\) has 2; \\({b_str}\\) has 1 (total 3 decimal places).\n"
        f"\\({int(round(a*100))} \\times {int(round(b*10))} = {int(round(prod*1000))}\\).\n"
        f"Final product: \\({prod_str}\\)."
    )
    return {
        "id": f"g9_dec_mul_hund_tenth_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": prod_str,
        "expected_answer": prod_str,
        "sample_answer": prod_str,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": "Multiply as whole numbers", "marks": 1},
            {"desc": f"Correctly assign 3 decimal places: {prod_str}", "marks": 1},
        ],
        "hints": [
            "Total decimal places = 2 + 1 = 3.",
            f"Multiply {int(round(a*100))} by {int(round(b*10))}.",
            f"Product: {prod_str}.",
        ],
    }


# ----------------------------------------------------------------------
# 34. Multiplication of Two Decimals: Hundredths by Hundredths
# ----------------------------------------------------------------------
def arch_34_multiplication_of_two_decimals_hundredths_by_hundredths(rng: random.Random) -> Dict[str, Any]:
    n1 = rng.choice([12, 15, 16, 25, 32])
    n2 = rng.choice([4, 6, 8, 12, 14])
    a = round(n1 / 100, 2)
    b = round(n2 / 100, 2)
    prod = round(a * b, 4)

    a_str = f"{a:.2f}".replace(".", ",")
    b_str = f"{b:.2f}".replace(".", ",")
    prod_str = f"{prod:.4f}".rstrip("0").rstrip(".").replace(".", ",")

    prompt = (
        f"Calculate the product:\n\n"
        f"\\[ {a_str} \\times {b_str} \\]"
    )
    sol = (
        f"**Hundredths × Hundredths:**\n"
        f"Total decimal places: \\(2 + 2 = 4\\).\n"
        f"\\({n1} \\times {n2} = {n1*n2}\\).\n"
        f"Placing 4 decimal places gives: \\({prod_str}\\)."
    )
    return {
        "id": f"g9_dec_mul_hund_hund_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": prod_str,
        "expected_answer": prod_str,
        "sample_answer": prod_str,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"Multiply integers {n1} * {n2} = {n1*n2}", "marks": 1},
            {"desc": f"Apply 4 decimal places: {prod_str}", "marks": 1},
        ],
        "hints": [
            "2 decimal places + 2 decimal places = 4 decimal places.",
            f"Multiply {n1} * {n2}.",
            f"Answer: {prod_str}.",
        ],
    }


# ----------------------------------------------------------------------
# 35. Division by Powers of Ten: 10, 100, 1000
# ----------------------------------------------------------------------
def arch_35_division_by_powers_of_ten_10_100_1000(rng: random.Random) -> Dict[str, Any]:
    w = rng.randint(45, 95)
    t = rng.randint(1, 9)
    val = round(w + t / 10, 1)
    div = rng.choice([10, 100, 1000])

    val_str = f"{val:.1f}".replace(".", ",")
    ans = round(val / div, 4)
    ans_str = f"{ans:.4f}".rstrip("0").replace(".", ",")

    prompt = (
        f"Calculate without using a calculator, stating how the decimal comma shifts:\n\n"
        f"\\[ {val_str} \\div {div} \\]"
    )
    sol = (
        f"**Division by {div}:**\n"
        f"Dividing by \\({div}\\) shifts the decimal comma "
        f"\\({1 if div==10 else (2 if div==100 else 3)}\\) position(s) to the left.\n"
        f"Result: \\({ans_str}\\)."
    )
    return {
        "id": f"g9_dec_div_pwr10_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans_str,
        "expected_answer": ans_str,
        "sample_answer": ans_str,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "marking_schema": [
            {"desc": f"Shift comma left by {1 if div==10 else (2 if div==100 else 3)}: {ans_str}", "marks": 1},
        ],
        "hints": [
            f"Division by {div} moves the comma to the left.",
            f"Answer is {ans_str}.",
        ],
    }


# ----------------------------------------------------------------------
# 36. Division of Decimal by Single-Digit Whole: No Remainder
# ----------------------------------------------------------------------
def arch_36_division_of_decimal_by_single_digit_whole_no_remainder(rng: random.Random) -> Dict[str, Any]:
    quot = round(rng.uniform(1.2, 5.8), 2)
    div = rng.choice([3, 4, 5, 6, 7])
    num = round(quot * div, 2)

    num_str = f"{num:.2f}".replace(".", ",")
    ans_str = f"{quot:.2f}".replace(".", ",")

    prompt = (
        f"Calculate the quotient using short division:\n\n"
        f"\\[ {num_str} \\div {div} \\]"
    )
    sol = (
        f"**Short Division:**\n"
        f"Divide whole units then tenths and hundredths:\n"
        f"\\({num_str} \\div {div} = {ans_str}\\)."
    )
    return {
        "id": f"g9_dec_div_whole_clean_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans_str,
        "expected_answer": ans_str,
        "sample_answer": ans_str,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": "Perform division keeping comma aligned", "marks": 1},
            {"desc": f"Accurate quotient {ans_str}", "marks": 1},
        ],
        "hints": [
            f"Divide each digit by {div}.",
            "Keep the decimal comma directly above the dividend's comma.",
            f"Quotient: {ans_str}.",
        ],
    }


# ----------------------------------------------------------------------
# 37. Division of Decimal by Whole Number Requiring Zero Annexing
# ----------------------------------------------------------------------
def arch_37_division_of_decimal_by_whole_number_requiring_zero_annexing(rng: random.Random) -> Dict[str, Any]:
    cases = [
        (3.5, 4, 0.875, "3{,}500 / 4 = 0{,}875"),
        (7.2, 5, 1.44, "7{,}20 / 5 = 1{,}44"),
        (9.4, 8, 1.175, "9{,}400 / 8 = 1{,}175"),
        (1.5, 4, 0.375, "1{,}500 / 4 = 0{,}375"),
    ]
    num, div, ans, work = rng.choice(cases)
    num_str = f"{num:.1f}".replace(".", ",")
    ans_str = f"{ans:.3f}".rstrip("0").replace(".", ",")

    prompt = (
        f"Divide by annexing trailing zeros to resolve the remainder:\n\n"
        f"\\[ {num_str} \\div {div} \\]"
    )
    sol = (
        f"**Annexing Zeros:**\n"
        f"{work}.\n"
        f"Result: \\({ans_str}\\)."
    )
    return {
        "id": f"g9_dec_div_annex_zeros_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans_str,
        "expected_answer": ans_str,
        "sample_answer": ans_str,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": "Annex trailing zeros to complete division", "marks": 1},
            {"desc": f"Correct quotient {ans_str}", "marks": 1},
        ],
        "hints": [
            "Add zeros after the last decimal digit to continue dividing.",
            f"Divide until there is no remainder.",
            f"Answer: {ans_str}.",
        ],
    }


# ----------------------------------------------------------------------
# 38. Division of Decimal by Decimal: Scaling Divisor
# ----------------------------------------------------------------------
def arch_38_division_of_decimal_by_decimal_scaling_divisor(rng: random.Random) -> Dict[str, Any]:
    quot = rng.choice([6, 8, 9, 12, 15, 16])
    div = rng.choice([0.2, 0.3, 0.4, 0.5, 0.6])
    num = round(quot * div, 2)

    num_str = f"{num:.1f}".replace(".", ",")
    div_str = f"{div:.1f}".replace(".", ",")
    scaled_num = int(round(num * 10))
    scaled_div = int(round(div * 10))

    prompt = (
        f"Calculate the quotient by scaling the divisor to a whole number:\n\n"
        f"\\[ {num_str} \\div {div_str} \\]"
    )
    sol = (
        f"**Scaling Divisor:**\n"
        f"Multiply both dividend and divisor by 10:\n"
        f"\\[ \\frac{{{num_str}}}{{{div_str}}} = \\frac{{{scaled_num}}}{{{scaled_div}}} = {quot} \\]"
    )
    return {
        "id": f"g9_dec_div_scale_divisor_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": str(quot),
        "expected_answer": str(quot),
        "sample_answer": str(quot),
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"Scale by 10 to {scaled_num} / {scaled_div}", "marks": 1},
            {"desc": f"State integer quotient {quot}", "marks": 1},
        ],
        "hints": [
            "Multiply numerator and denominator by 10 to clear the decimal from the divisor.",
            f"Calculate {scaled_num} / {scaled_div}.",
            f"Quotient: {quot}.",
        ],
    }


# ----------------------------------------------------------------------
# 39. Division of Decimal by Decimal: Yielding Decimal
# ----------------------------------------------------------------------
def arch_39_division_of_decimal_by_decimal_yielding_decimal(rng: random.Random) -> Dict[str, Any]:
    quot = round(rng.choice([2.4, 3.5, 4.2, 5.6, 6.5]), 1)
    div = round(rng.choice([0.2, 0.3, 0.4, 0.5]), 1)
    num = round(quot * div, 2)

    num_str = f"{num:.2f}".replace(".", ",")
    div_str = f"{div:.1f}".replace(".", ",")
    ans_str = f"{quot:.1f}".replace(".", ",")

    scaled_num = round(num * 10, 1)
    scaled_num_str = f"{scaled_num:.1f}".replace(".", ",")
    scaled_div = int(round(div * 10))

    prompt = (
        f"Calculate the quotient:\n\n"
        f"\\[ {num_str} \\div {div_str} \\]"
    )
    sol = (
        f"**Divisor Scaling:**\n"
        f"Multiply by 10: \\(\\frac{{{num_str}}}{{{div_str}}} = \\frac{{{scaled_num_str}}}{{{scaled_div}}}\\).\n"
        f"Divide: \\({scaled_num_str} \\div {scaled_div} = {ans_str}\\)."
    )
    return {
        "id": f"g9_dec_div_yield_dec_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans_str,
        "expected_answer": ans_str,
        "sample_answer": ans_str,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"Scale by 10 to {scaled_num_str} / {scaled_div}", "marks": 1},
            {"desc": f"Compute decimal quotient {ans_str}", "marks": 1},
        ],
        "hints": [
            "Multiply both numbers by 10 to make the divisor a whole number.",
            f"Divide {scaled_num_str} by {scaled_div}.",
            f"Answer: {ans_str}.",
        ],
    }


# ----------------------------------------------------------------------
# 40. Square of a Decimal Fraction
# ----------------------------------------------------------------------
def arch_40_square_of_decimal_fraction(rng: random.Random) -> Dict[str, Any]:
    cases = [
        (0.2, 0.04, "0{,}2", "0{,}04"),
        (0.3, 0.09, "0{,}3", "0{,}09"),
        (0.6, 0.36, "0{,}6", "0{,}36"),
        (0.05, 0.0025, "0{,}05", "0{,}0025"),
        (0.12, 0.0144, "0{,}12", "0{,}0144"),
    ]
    base, sq, base_str, sq_str = rng.choice(cases)

    prompt = (
        f"Evaluate the square of the decimal fraction:\n\n"
        f"\\[ ({base_str})^2 \\]"
    )
    sol = (
        f"**Squaring Decimals:**\n"
        f"\\(({base_str})^2 = {base_str} \\times {base_str} = {sq_str}\\).\n"
        f"Squaring doubles the number of decimal places."
    )
    return {
        "id": f"g9_dec_square_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": sq_str,
        "expected_answer": sq_str,
        "sample_answer": sq_str,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "marking_schema": [
            {"desc": f"Correct squared decimal {sq_str}", "marks": 1},
        ],
        "hints": [
            f"Multiply {base_str} by itself.",
            "Notice that the number of decimal places doubles.",
            f"Result: {sq_str}.",
        ],
    }


# ----------------------------------------------------------------------
# 41. Cube of a Decimal Fraction
# ----------------------------------------------------------------------
def arch_41_cube_of_decimal_fraction(rng: random.Random) -> Dict[str, Any]:
    cases = [
        (0.1, 0.001, "0{,}1", "0{,}001"),
        (0.2, 0.008, "0{,}2", "0{,}008"),
        (0.3, 0.027, "0{,}3", "0{,}027"),
        (0.4, 0.064, "0{,}4", "0{,}064"),
        (0.5, 0.125, "0{,}5", "0{,}125"),
    ]
    base, cube, base_str, cube_str = rng.choice(cases)

    prompt = (
        f"Evaluate the cube of the decimal fraction:\n\n"
        f"\\[ ({base_str})^3 \\]"
    )
    sol = (
        f"**Cubing Decimals:**\n"
        f"\\(({base_str})^3 = {base_str} \\times {base_str} \\times {base_str} = {cube_str}\\).\n"
        f"Cubing triples the number of decimal places."
    )
    return {
        "id": f"g9_dec_cube_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": cube_str,
        "expected_answer": cube_str,
        "sample_answer": cube_str,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "marking_schema": [
            {"desc": f"Correct cubed decimal {cube_str}", "marks": 1},
        ],
        "hints": [
            f"Multiply {base_str} * {base_str} * {base_str}.",
            "1 decimal place cubed gives 3 decimal places.",
            f"Result: {cube_str}.",
        ],
    }


# ----------------------------------------------------------------------
# 42. Square Root of a Decimal Fraction
# ----------------------------------------------------------------------
def arch_42_square_root_of_decimal_fraction(rng: random.Random) -> Dict[str, Any]:
    cases = [
        ("0{,}49", "0{,}7", "49/100 -> 7/10"),
        ("0{,}64", "0{,}8", "64/100 -> 8/10"),
        ("0{,}81", "0{,}9", "81/100 -> 9/10"),
        ("0{,}0144", "0{,}12", "144/10000 -> 12/100"),
        ("0{,}0025", "0{,}05", "25/10000 -> 5/100"),
    ]
    rad, root, exp = rng.choice(cases)

    prompt = (
        f"Evaluate the square root:\n\n"
        f"\\[ \\sqrt{{{rad}}} \\]"
    )
    sol = (
        f"**Square Root of Decimal:**\n"
        f"Convert to fraction: \\(\\sqrt{{{rad}}} = {exp} = {root}\\)."
    )
    return {
        "id": f"g9_dec_sqrt_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": root,
        "expected_answer": root,
        "sample_answer": root,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": "Convert to common fraction square root", "marks": 1},
            {"desc": f"State decimal root {root}", "marks": 1},
        ],
        "hints": [
            f"Write {rad} as a common fraction over 100 or 10000.",
            "Take the square root of numerator and denominator.",
            f"Answer: {root}.",
        ],
    }


# ----------------------------------------------------------------------
# 43. Cube Root of a Decimal Fraction
# ----------------------------------------------------------------------
def arch_43_cube_root_of_decimal_fraction(rng: random.Random) -> Dict[str, Any]:
    cases = [
        ("0{,}008", "0{,}2", "8/1000 -> 2/10"),
        ("0{,}027", "0{,}3", "27/1000 -> 3/10"),
        ("0{,}064", "0{,}4", "64/1000 -> 4/10"),
        ("0{,}125", "0{,}5", "125/1000 -> 5/10"),
        ("0{,}000008", "0{,}02", "8/1000000 -> 2/100"),
    ]
    rad, root, exp = rng.choice(cases)

    prompt = (
        f"Evaluate the cube root:\n\n"
        f"\\[ \\sqrt[3]{{{rad}}} \\]"
    )
    sol = (
        f"**Cube Root of Decimal:**\n"
        f"\\(\\sqrt[3]{{{rad}}} = {exp} = {root}\\)."
    )
    return {
        "id": f"g9_dec_cbrt_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": root,
        "expected_answer": root,
        "sample_answer": root,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": "Convert to fractional radicand", "marks": 1},
            {"desc": f"State decimal cube root {root}", "marks": 1},
        ],
        "hints": [
            f"Write {rad} as a fraction over 1000.",
            "Take the cube root of numerator and denominator.",
            f"Result: {root}.",
        ],
    }


# ----------------------------------------------------------------------
# 44. Order of Operations: BODMAS with Decimals Mixed
# ----------------------------------------------------------------------
def arch_44_order_of_operations_bodmas_with_decimals_mixed(rng: random.Random) -> Dict[str, Any]:
    # e.g., 3,2 + 1,5 * 0,4 - 0,25 = 3,2 + 0,6 - 0,25 = 3,8 - 0,25 = 3,55
    m1 = rng.choice([1.2, 1.5, 2.4, 2.5])
    m2 = rng.choice([0.2, 0.4, 0.5, 0.6])
    prod = round(m1 * m2, 2)
    add_val = round(rng.uniform(2.1, 5.5), 1)
    sub_val = round(rng.choice([0.15, 0.25, 0.35, 0.45]), 2)
    ans = round(add_val + prod - sub_val, 2)

    add_str = f"{add_val:.1f}".replace(".", ",")
    m1_str = f"{m1:.1f}".replace(".", ",")
    m2_str = f"{m2:.1f}".replace(".", ",")
    sub_str = f"{sub_val:.2f}".replace(".", ",")
    ans_str = f"{ans:.2f}".replace(".", ",")

    prompt = (
        f"Evaluate the decimal expression applying strict BODMAS priority:\n\n"
        f"\\[ {add_str} + {m1_str} \\times {m2_str} - {sub_str} \\]"
    )
    sol = (
        f"**BODMAS Execution:**\n"
        f"1. Multiplication: \\({m1_str} \\times {m2_str} = {prod:.2f}\\).\n"
        f"2. Addition: \\({add_str} + {prod:.2f} = {add_val + prod:.2f}\\).\n"
        f"3. Subtraction: \\({add_val + prod:.2f} - {sub_str} = {ans_str}\\)."
    )
    return {
        "id": f"g9_dec_bodmas_mixed_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans_str,
        "expected_answer": ans_str,
        "sample_answer": ans_str,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "marking_schema": [
            {"desc": f"Perform multiplication first: {prod:.2f}", "marks": 1},
            {"desc": "Perform addition and subtraction from left to right", "marks": 1},
            {"desc": f"Accurate final answer {ans_str}", "marks": 1},
        ],
        "hints": [
            "Multiply before adding or subtracting.",
            f"{m1_str} * {m2_str} = {prod:.2f}.",
            f"Final evaluated result: {ans_str}.",
        ],
    }


# ----------------------------------------------------------------------
# 45. Order of Operations: Brackets and Powers with Decimals
# ----------------------------------------------------------------------
def arch_45_order_of_operations_brackets_and_powers_decimals(rng: random.Random) -> Dict[str, Any]:
    # (0,3)^2 + (1,2 - 0,7) / 0,2 = 0,09 + 0,5 / 0,2 = 0,09 + 2,5 = 2,59
    sq_base = rng.choice([0.2, 0.3, 0.4])
    sq_val = round(sq_base ** 2, 2)
    b_diff = round(rng.choice([0.4, 0.6, 0.8]), 1)
    b_div = 0.2
    div_res = round(b_diff / b_div, 1)
    ans = round(sq_val + div_res, 2)

    b1 = round(1.2 + b_diff, 1)
    b2 = 1.2

    sq_str = f"{sq_base:.1f}".replace(".", ",")
    b1_str = f"{b1:.1f}".replace(".", ",")
    b2_str = f"{b2:.1f}".replace(".", ",")
    ans_str = f"{ans:.2f}".replace(".", ",")

    prompt = (
        f"Calculate the exact value of the expression:\n\n"
        f"\\[ ({sq_str})^2 + ({b1_str} - {b2_str}) \\div 0{{,}}2 \\]"
    )
    sol = (
        f"**Order of Operations:**\n"
        f"1. Power: \\(({sq_str})^2 = {sq_val:.2f}\\).\n"
        f"2. Brackets: \\({b1_str} - {b2_str} = {b_diff:.1f}\\).\n"
        f"3. Division: \\({b_diff:.1f} \\div 0{{,}}2 = {div_res:.1f}\\).\n"
        f"4. Addition: \\({sq_val:.2f} + {div_res:.1f} = {ans_str}\\)."
    )
    return {
        "id": f"g9_dec_bodmas_pwr_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans_str,
        "expected_answer": ans_str,
        "sample_answer": ans_str,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "marking_schema": [
            {"desc": f"Evaluate power ({sq_val:.2f}) and brackets ({b_diff:.1f})", "marks": 1},
            {"desc": f"Perform division to get {div_res:.1f}", "marks": 1},
            {"desc": f"Final sum {ans_str}", "marks": 1},
        ],
        "hints": [
            "Calculate brackets and powers first.",
            "Next perform the division.",
            f"Final result: {ans_str}.",
        ],
    }


# ----------------------------------------------------------------------
# 46. Olympic Timing: Margin of Victory Problem
# ----------------------------------------------------------------------
def arch_46_olympic_timing_margin_of_victory_problem(rng: random.Random) -> Dict[str, Any]:
    t1 = round(rng.uniform(9.85, 9.94), 2)
    diff = round(rng.choice([0.02, 0.03, 0.04, 0.05, 0.07]), 2)
    t2 = round(t1 + diff, 2)
    t3 = round(t2 + rng.choice([0.04, 0.06]), 2)
    t4 = round(t3 + rng.choice([0.05, 0.08]), 2)

    athletes = [
        ("4", "A. Simbine", t1),
        ("5", "N. Lyles", t2),
        ("6", "K. Thompson", t3),
        ("3", "F. Kerley", t4),
    ]
    svg = draw_olympic_timing_board_svg("Men's 100m Final", athletes, seed=rng.randint(1, 9999))
    ans_str = f"{diff:.2f}".replace(".", ",")

    prompt = (
        f"Consider the official electronic race timing results display below.\n\n"
        f"Calculate the margin of victory between the gold medallist (1st place) "
        f"and the silver medallist (2nd place) in hundredths of a second."
    )
    sol = (
        f"**Margin of Victory:**\n"
        f"Gold medal time (1st): \\({t1:.2f}\\text{{ s}}\\).\n"
        f"Silver medal time (2nd): \\({t2:.2f}\\text{{ s}}\\).\n"
        f"Margin of victory: \\({t2:.2f} - {t1:.2f} = {ans_str}\\text{{ s}}\\)."
    )
    return {
        "id": f"g9_dec_olympic_timing_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"{ans_str} s",
        "expected_answer": f"{ans_str} s",
        "sample_answer": f"{ans_str} s",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
        "marks": 2,
        "marking_schema": [
            {"desc": f"Extract times {t1:.2f} s and {t2:.2f} s", "marks": 1},
            {"desc": f"Subtract to obtain difference {ans_str} s", "marks": 1},
        ],
        "hints": [
            "Read the times for 1st and 2nd place from the scoreboard.",
            "Subtract the faster time from the slower time.",
            f"Difference is {ans_str} s.",
        ],
    }


# ----------------------------------------------------------------------
# 47. Fuel Consumption and Cost Rate Word Problem
# ----------------------------------------------------------------------
def arch_47_fuel_consumption_and_cost_rate_word_problem(rng: random.Random) -> Dict[str, Any]:
    litres = round(rng.uniform(35.5, 62.5), 1)
    rate = round(rng.uniform(21.40, 24.80), 2)
    tot = round(litres * rate, 2)

    l_str = f"{litres:.1f}".replace(".", ",")
    r_str = f"\\text{{R}}{rate:.2f}".replace(".", ",")
    tot_str = f"\\text{{R}}{tot:.2f}".replace(".", ",")

    prompt = (
        f"A motorist fills up a vehicle with \\({l_str}\\text{{ L}}\\) of petrol at a price of "
        f"\\({r_str}\\) per litre. Calculate the total cost of the fuel, rounding to the nearest cent."
    )
    sol = (
        f"**Fuel Cost Calculation:**\n"
        f"\\[ \\text{{Total Cost}} = {l_str} \\times {r_str} = {tot_str} \\]"
    )
    return {
        "id": f"g9_dec_fuel_rate_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": tot_str,
        "expected_answer": tot_str,
        "sample_answer": tot_str,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": "Multiply litres by price per litre", "marks": 1},
            {"desc": f"Accurate total rounded to nearest cent: {tot_str}", "marks": 1},
        ],
        "hints": [
            "Multiply volume in litres by unit price.",
            "Round off to two decimal places.",
            f"Total: {tot_str}.",
        ],
    }


# ----------------------------------------------------------------------
# 48. Unit Pricing: Best Buy Comparison with Decimals
# ----------------------------------------------------------------------
def arch_48_unit_pricing_best_buy_comparison_decimals(rng: random.Random) -> Dict[str, Any]:
    # Pack A: 2,5 kg for R62,50 -> R25,00/kg
    # Pack B: 5,0 kg for R115,00 -> R23,00/kg
    rate_a = round(rng.choice([24.50, 26.00, 28.50]), 2)
    rate_b = round(rate_a - rng.choice([1.50, 2.00, 3.20]), 2)
    mass_a = 2.5
    mass_b = 5.0
    cost_a = round(mass_a * rate_a, 2)
    cost_b = round(mass_b * rate_b, 2)

    cost_a_str = f"\\text{{R}}{cost_a:.2f}".replace(".", ",")
    cost_b_str = f"\\text{{R}}{cost_b:.2f}".replace(".", ",")
    rate_a_str = f"\\text{{R}}{rate_a:.2f}".replace(".", ",")
    rate_b_str = f"\\text{{R}}{rate_b:.2f}".replace(".", ",")

    prompt = (
        f"A supermarket sells maize meal in two sizes:\n"
        f"- Brand A: \\(2{{,}}5\\text{{ kg}}\\) for \\({cost_a_str}\\)\n"
        f"- Brand B: \\(5{{,}}0\\text{{ kg}}\\) for \\({cost_b_str}\\)\n\n"
        f"1. Calculate the unit price per kilogram for each brand.\n"
        f"2. State which brand offers the better value for money."
    )
    sol = (
        f"**Unit Price Comparison:**\n"
        f"Brand A: \\(\\frac{{{cost_a_str}}}{{2{{,}}5}} = {rate_a_str}/\\text{{kg}}\\).\n"
        f"Brand B: \\(\\frac{{{cost_b_str}}}{{5{{,}}0}} = {rate_b_str}/\\text{{kg}}\\).\n"
        f"Since \\({rate_b_str} < {rate_a_str}\\), **Brand B** is the better buy."
    )
    return {
        "id": f"g9_dec_unit_price_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"Brand A: {rate_a_str}/kg; Brand B: {rate_b_str}/kg; Better buy: Brand B",
        "expected_answer": f"Brand A: {rate_a_str}/kg; Brand B: {rate_b_str}/kg; Better buy: Brand B",
        "sample_answer": f"Brand A: {rate_a_str}/kg; Brand B: {rate_b_str}/kg; Better buy: Brand B",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "marking_schema": [
            {"desc": f"Brand A unit rate {rate_a_str}/kg", "marks": 1},
            {"desc": f"Brand B unit rate {rate_b_str}/kg", "marks": 1},
            {"desc": "Identify Brand B as better value", "marks": 1},
        ],
        "hints": [
            "Divide cost by mass for each brand to find price per 1 kg.",
            "Compare the two unit rates: lower rate is better value.",
            "Brand B is cheaper per kg.",
        ],
    }


# ----------------------------------------------------------------------
# 49. Error Analysis: Diagnosing Decimal Multiplication Place Value
# ----------------------------------------------------------------------
def arch_49_error_analysis_diagnosing_decimal_multiplication_place_value(rng: random.Random) -> Dict[str, Any]:
    n1 = rng.choice([0.4, 0.6, 0.8])
    n2 = rng.choice([0.03, 0.05, 0.07])
    correct_prod = round(n1 * n2, 3)
    flawed_prod = round(correct_prod * 10, 2)  # forgot one decimal place

    n1_str = f"{n1:.1f}".replace(".", ",")
    n2_str = f"{n2:.2f}".replace(".", ",")
    correct_str = f"{correct_prod:.3f}".replace(".", ",")
    flawed_str = f"{flawed_prod:.2f}".replace(".", ",")

    prompt = (
        f"A learner wrote the following calculation in a class test:\n\n"
        f"\\[ {n1_str} \\times {n2_str} = {flawed_str} \\]\n\n"
        f"Identify the conceptual error made by the learner and provide the correct product."
    )
    sol = (
        f"**Error Analysis:**\n"
        f"1. Error: The learner counted only 2 decimal places instead of \\(1 + 2 = 3\\) decimal places.\n"
        f"2. Correct evaluation: \\({int(round(n1*10))} \\times {int(round(n2*100))} = {int(round(correct_prod*1000))}\\).\n"
        f"With 3 decimal places: \\({correct_str}\\)."
    )
    return {
        "id": f"g9_dec_err_mul_pv_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"Learner omitted 1 decimal place; Correct: {correct_str}",
        "expected_answer": f"Learner omitted 1 decimal place; Correct: {correct_str}",
        "sample_answer": f"Learner omitted 1 decimal place; Correct: {correct_str}",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": "Identify failure to sum total decimal places (3 needed)", "marks": 1},
            {"desc": f"Provide correct product {correct_str}", "marks": 1},
        ],
        "hints": [
            f"{n1_str} has 1 decimal digit; {n2_str} has 2 decimal digits.",
            "Total decimal digits in product must be 1 + 2 = 3.",
            f"Correct answer is {correct_str}.",
        ],
    }


# ----------------------------------------------------------------------
# 50. Compound Multi-Step Decimal Fraction Evaluation
# ----------------------------------------------------------------------
def arch_50_compound_multi_step_decimal_fraction_evaluation(rng: random.Random) -> Dict[str, Any]:
    # e.g., (2,4 * 0,5 + 0,8) / 0,4 = (1,2 + 0,8) / 0,4 = 2,0 / 0,4 = 20 / 4 = 5
    m1 = rng.choice([1.6, 2.4, 3.2, 4.8])
    m2 = 0.5
    prod = round(m1 * m2, 2)
    add_val = round(rng.choice([0.8, 1.2, 1.6]), 1)
    num_tot = round(prod + add_val, 1)
    den = 0.4
    ans = round(num_tot / den, 1)
    ans_int = int(ans) if ans.is_integer() else ans

    m1_str = f"{m1:.1f}".replace(".", ",")
    add_str = f"{add_val:.1f}".replace(".", ",")
    num_tot_str = f"{num_tot:.1f}".replace(".", ",")

    prompt = (
        f"Evaluate the comprehensive decimal expression:\n\n"
        f"\\[ \\frac{{{m1_str} \\times 0{{,}}5 + {add_str}}}{{0{{,}}4}} \\]"
    )
    sol = (
        f"**Multi-step Evaluation:**\n"
        f"1. Numerator product: \\({m1_str} \\times 0{{,}}5 = {prod:.2f}\\).\n"
        f"2. Numerator sum: \\({prod:.2f} + {add_str} = {num_tot_str}\\).\n"
        f"3. Division by \\(0{{,}}4\\): \\(\\frac{{{num_tot_str}}}{{0{{,}}4}} = \\frac{{{int(num_tot*10)}}}{{4}} = {ans_int}\\)."
    )
    return {
        "id": f"g9_dec_compound_eval_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": str(ans_int),
        "expected_answer": str(ans_int),
        "sample_answer": str(ans_int),
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "marking_schema": [
            {"desc": f"Evaluate numerator to {num_tot_str}", "marks": 1},
            {"desc": "Scale divisor to 4 and divide", "marks": 1},
            {"desc": f"State final answer {ans_int}", "marks": 1},
        ],
        "hints": [
            "Evaluate the numerator completely before dividing.",
            f"Multiply {m1_str} by 0,5, then add {add_str}.",
            f"Divide by 0,4 to get {ans_int}.",
        ],
    }
