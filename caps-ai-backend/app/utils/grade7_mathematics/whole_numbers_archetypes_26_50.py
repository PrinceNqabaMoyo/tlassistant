"""
Grade 7 Mathematics - Working with Whole Numbers Generator (Archetypes 26 to 50).
100% CAPS-aligned deterministic question generator.
Adheres strictly to the 6-Pillar Generator Contract and Zero-Meta-Curriculum Invariant.
Grounded in curriculum_docs_auto/Mathematics_Gr7/Term 1/01. Working with whole numbers.md.
"""
from __future__ import annotations
import math
import random
from typing import Any, Dict, List, Optional


# ==============================================================================
# CLUSTER 4: Addition & Subtraction (26 - 32)
# ==============================================================================

def arch_26_column_subtraction_with_borrowing(rng: random.Random) -> Dict[str, Any]:
    n1 = rng.randint(45000, 95000)
    n2 = rng.randint(12000, n1 - 5000)
    diff = n1 - n2

    s1 = f"{n1:,}".replace(",", " ")
    s2 = f"{n2:,}".replace(",", " ")
    diff_s = f"{diff:,}".replace(",", " ")

    prompt = f"Calculate the difference using vertical column subtraction with borrowing: $${s1} - {s2}$$"
    sol = (
        f"**Step 1:** Subtract column by column from units, borrowing from the column to the left where minuend < subtrahend [1 Mark: Method].\n\n"
        f"**Step 2:** Final difference:\n\n"
        f"$$\\mathbf{{{diff_s}}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_wn_26_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": diff_s,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "26_column_subtraction_with_borrowing",
        "hints": {
            "tier_1": "Borrow 1 ten when a digit on top is smaller than the bottom digit.",
            "tier_2": f"{s1} - {s2}.",
            "tier_3": f"Difference = {diff_s}."
        }
    }


def arch_27_addition_subtraction_inverse_check(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(23400, 56700)
    b = rng.randint(12000, 38000)
    total = a + b

    s_a = f"{a:,}".replace(",", " ")
    s_b = f"{b:,}".replace(",", " ")
    s_tot = f"{total:,}".replace(",", " ")

    prompt = (
        f"1. Calculate the sum: ${s_a} + {s_b}$.\n"
        f"2. Write down the inverse subtraction statement to verify your calculation."
    )
    sol = (
        f"**Step 1:** Add: ${s_a} + {s_b} = \\mathbf{{{s_tot}}}$ [1 Mark: Accuracy].\n\n"
        f"**Step 2:** Inverse verification:\n\n"
        f"$${s_tot} - {s_b} = {s_a} \\text{{ [1 Mark: Method]}}$$"
    )
    return {
        "id": f"g7_wn_27_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"Sum: {s_tot}; Inverse: {s_tot} - {s_b} = {s_a}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "27_addition_subtraction_inverse_check",
        "hints": {
            "tier_1": "Subtraction is the inverse operation of addition.",
            "tier_2": f"If a + b = total, then total - b = a.",
            "tier_3": f"Sum = {s_tot}, check: {s_tot} - {s_b} = {s_a}."
        }
    }


def arch_28_estimating_sum_by_rounding(rng: random.Random) -> Dict[str, Any]:
    n1 = rng.randint(23400, 48900)
    n2 = rng.randint(12100, 36800)
    r1 = round(n1 / 1000) * 1000
    r2 = round(n2 / 1000) * 1000
    est = r1 + r2

    s1 = f"{n1:,}".replace(",", " ")
    s2 = f"{n2:,}".replace(",", " ")
    s_est = f"{est:,}".replace(",", " ")

    prompt = (
        f"Estimate the sum of **{s1}** and **{s2}** by rounding each number to the nearest **1 000** first."
    )
    sol = (
        f"**Step 1:** Round each term to nearest 1 000: ${n1} \\approx {r1:,}$ and ${n2} \\approx {r2:,}$ [1 Mark: Method].\n\n"
        f"**Step 2:** Add estimated values:\n\n"
        f"$${r1:,} + {r2:,} = \\mathbf{{{s_est}}} \\text{{ [1 Mark: Accuracy]}}$$"
    ).replace(",", " ")
    return {
        "id": f"g7_wn_28_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": s_est,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "28_estimating_sum_by_rounding",
        "hints": {
            "tier_1": "Round each number to nearest thousand before adding.",
            "tier_2": f"{n1} rounds to {r1}, and {n2} rounds to {r2}.",
            "tier_3": f"Estimated sum = {s_est}."
        }
    }


def arch_29_multi_step_addition_subtraction_budget(rng: random.Random) -> Dict[str, Any]:
    grant = rng.randint(45000, 85000)
    books = rng.randint(12000, 22000)
    desks = rng.randint(15000, 28000)
    paint = rng.randint(4000, 8000)
    rem = grant - books - desks - paint

    s_grant = f"{grant:,}".replace(",", " ")
    s_b = f"{books:,}".replace(",", " ")
    s_d = f"{desks:,}".replace(",", " ")
    s_p = f"{paint:,}".replace(",", " ")
    s_rem = f"{rem:,}".replace(",", " ")

    prompt = (
        f"A primary school receives a maintenance grant of **R{s_grant}**.\n\n"
        f"The school spends **R{s_b}** on library books, **R{s_d}** on learner desks, and **R{s_p}** on classroom paint.\n\n"
        f"Calculate the unspent funds remaining from the grant."
    )
    sol = (
        f"**Step 1:** Sum total expenses: ${books} + {desks} + {paint} = \\text{{R}}{books + desks + paint:,}$ [1 Mark: Method].\n\n"
        f"**Step 2:** Subtract from grant:\n\n"
        f"$$\\text{{R}}{grant:,} - \\text{{R}}{books + desks + paint:,} = \\mathbf{{\\text{{R}}{s_rem}}} \\text{{ [1 Mark: Accuracy]}}$$"
    ).replace(",", " ")
    return {
        "id": f"g7_wn_29_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"R{s_rem}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "29_multi_step_addition_subtraction_budget",
        "hints": {
            "tier_1": "Add up all three expenses first.",
            "tier_2": f"Total expenses = R{books + desks + paint:,}.".replace(",", " "),
            "tier_3": f"Remaining = R{s_rem}."
        }
    }


def arch_30_difference_between_two_large_populations(rng: random.Random) -> Dict[str, Any]:
    c1, pop1 = "City of Tshwane", rng.randint(2900000, 3200000)
    c2, pop2 = "City of Mangaung", rng.randint(750000, 890000)
    diff = pop1 - pop2

    s1 = f"{pop1:,}".replace(",", " ")
    s2 = f"{pop2:,}".replace(",", " ")
    s_diff = f"{diff:,}".replace(",", " ")

    prompt = (
        f"According to municipal census data, the population of **{c1}** is **{s1}**, "
        f"while **{c2}** has a population of **{s2}**.\n\n"
        f"Calculate how many more residents live in {c1} than in {c2}."
    )
    sol = (
        f"**Step 1:** Subtract the smaller population from the larger population [1 Mark: Method].\n\n"
        f"**Step 2:** Difference:\n\n"
        f"$${s1} - {s2} = \\mathbf{{{s_diff}}} \\text{{ residents [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_wn_30_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{s_diff} residents",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "30_difference_between_two_large_populations",
        "hints": {
            "tier_1": "Subtract the smaller number from the larger number.",
            "tier_2": f"{s1} - {s2}.",
            "tier_3": f"Difference = {s_diff} residents."
        }
    }


def arch_31_missing_digit_in_column_addition(rng: random.Random) -> Dict[str, Any]:
    # e.g., 4 A 7 + 2 8 5 = 7 3 2 -> A = 4
    a_digit = rng.randint(2, 7)
    d1 = rng.randint(3, 6)
    d2 = rng.randint(1, 3)
    u1 = rng.randint(4, 8)
    u2 = rng.randint(5, 9)

    n1 = d1 * 100 + a_digit * 10 + u1
    n2 = d2 * 100 + rng.randint(1, 8) * 10 + u2
    total = n1 + n2

    n1_masked = f"{d1} A {u1}"
    prompt = (
        f"In the following vertical addition, find the missing single digit **A**:\n\n"
        f"$$\\begin{{array}}{{r}} {n1_masked} \\\\ + \\; {n2} \\\\ \\hline {total} \\end{{array}}$$"
    )
    sol = (
        f"**Step 1:** Check column addition from units to find carries [1 Mark: Method].\n\n"
        f"**Step 2:** Solve for A: **A = {a_digit}** [1 Mark: Accuracy].\n\n"
        f"$$\\therefore \\mathbf{{A = {a_digit}}}$$"
    )
    return {
        "id": f"g7_wn_31_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"A = {a_digit}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "31_missing_digit_in_column_addition",
        "hints": {
            "tier_1": f"Subtract {n2} from {total} to find the first number.",
            "tier_2": f"{total} - {n2} = {n1}.",
            "tier_3": f"A = {a_digit}."
        }
    }


def arch_32_missing_digit_in_column_subtraction(rng: random.Random) -> Dict[str, Any]:
    b_digit = rng.randint(2, 8)
    n1 = 600 + b_digit * 10 + 4
    n2 = 287
    diff = n1 - n2

    prompt = (
        f"Determine the value of digit **B** in the subtraction below:\n\n"
        f"$$\\begin{{array}}{{r}} 6 \\, B \\, 4 \\\\ - \\; {n2} \\\\ \\hline {diff} \\end{{array}}$$"
    )
    sol = (
        f"**Step 1:** Rearrange using inverse addition: $6B4 = {diff} + {n2} = {n1}$ [1 Mark: Method].\n\n"
        f"**Step 2:** Comparing tens digit: **B = {b_digit}** [1 Mark: Accuracy].\n\n"
        f"$$\\therefore \\mathbf{{B = {b_digit}}}$$"
    )
    return {
        "id": f"g7_wn_32_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"B = {b_digit}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "32_missing_digit_in_column_subtraction",
        "hints": {
            "tier_1": f"Add {diff} + {n2} to find the top number.",
            "tier_2": f"{diff} + {n2} = {n1}.",
            "tier_3": f"B = {b_digit}."
        }
    }


# ==============================================================================
# CLUSTER 5: Multiplication & Division Algorithms (33 - 42)
# ==============================================================================

def arch_33_long_multiplication_3_digit_by_2_digit(rng: random.Random) -> Dict[str, Any]:
    n1 = rng.randint(135, 485)
    n2 = rng.randint(23, 68)
    prod = n1 * n2

    prod_s = f"{prod:,}".replace(",", " ")
    prompt = f"Calculate using long multiplication: $${n1} \\times {n2}$$"
    sol = (
        f"**Step 1:** Multiply by units digit: ${n1} \\times {n2 % 10} = {n1 * (n2 % 10):,}$ [1 Mark: Method].\n\n"
        f"**Step 2:** Multiply by tens digit: ${n1} \\times {n2 - (n2 % 10)} = {n1 * (n2 - (n2 % 10)):,}$\n\n"
        f"**Step 3:** Add partial products: $\\mathbf{{{prod_s}}}$ [1 Mark: Accuracy].".replace(",", " ")
    )
    return {
        "id": f"g7_wn_33_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": prod_s,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "33_long_multiplication_3_digit_by_2_digit",
        "hints": {
            "tier_1": f"Multiply {n1} by {n2 % 10}, then by {n2 // 10 * 10}.",
            "tier_2": f"Partial products: {n1 * (n2 % 10)} and {n1 * (n2 - (n2 % 10))}.",
            "tier_3": f"Product = {prod_s}."
        }
    }


def arch_34_lattice_or_box_multiplication_method(rng: random.Random) -> Dict[str, Any]:
    t1 = rng.randint(24, 75)
    t2 = rng.randint(18, 48)
    prod = t1 * t2

    prompt = (
        f"Use the area model (box method) to calculate the product: $${t1} \\times {t2}$$\n\n"
        f"Show all partial products."
    )
    a, b = (t1 // 10) * 10, t1 % 10
    c, d = (t2 // 10) * 10, t2 % 10
    sol = (
        f"**Step 1:** Decompose factors: ${t1} = {a} + {b}$ and ${t2} = {c} + {d}$ [1 Mark: Method].\n\n"
        f"**Step 2:** Calculate four grid cells:\n"
        f"- ${a} \\times {c} = {a*c:,}$\n"
        f"- ${a} \\times {d} = {a*d:,}$\n"
        f"- ${b} \\times {c} = {b*c:,}$\n"
        f"- ${b} \\times {d} = {b*d:,}$\n\n"
        f"**Step 3:** Sum: ${a*c} + {a*d} + {b*c} + {b*d} = \\mathbf{{{prod:,}}}$ [1 Mark: Accuracy].".replace(",", " ")
    )
    return {
        "id": f"g7_wn_34_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{prod:,}".replace(",", " "),
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "34_lattice_or_box_multiplication_method",
        "hints": {
            "tier_1": f"Break {t1} into {a} + {b} and {t2} into {c} + {d}.",
            "tier_2": "Add all four box products together.",
            "tier_3": f"Product = {prod}."
        }
    }


def arch_35_long_division_4_digit_by_2_digit_no_remainder(rng: random.Random) -> Dict[str, Any]:
    divisor = rng.randint(14, 28)
    quotient = rng.randint(112, 345)
    dividend = divisor * quotient

    d_s = f"{dividend:,}".replace(",", " ")
    q_s = f"{quotient:,}".replace(",", " ")

    prompt = f"Calculate using long division without a calculator: $${d_s} \\div {divisor}$$"
    sol = (
        f"**Step 1:** Perform long division algorithm: divide, multiply, subtract, bring down [1 Mark: Method].\n\n"
        f"**Step 2:** Exact quotient:\n\n"
        f"$$\\mathbf{{{d_s} \\div {divisor} = {q_s}}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_wn_35_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": q_s,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "35_long_division_4_digit_by_2_digit_no_remainder",
        "hints": {
            "tier_1": "Set up standard long division bracket.",
            "tier_2": f"{divisor} divides into {dividend} exactly.",
            "tier_3": f"Quotient = {q_s}."
        }
    }


def arch_36_long_division_with_remainder(rng: random.Random) -> Dict[str, Any]:
    divisor = rng.randint(15, 32)
    quotient = rng.randint(85, 240)
    rem = rng.randint(1, divisor - 1)
    dividend = divisor * quotient + rem

    d_s = f"{dividend:,}".replace(",", " ")
    ans_str = f"{quotient} rem {rem}"

    prompt = (
        f"Divide using long division. State both the quotient and the remainder:\n\n"
        f"$${d_s} \\div {divisor}$$"
    )
    sol = (
        f"**Step 1:** Divide ${dividend}$ by ${divisor}$ to obtain quotient **{quotient}** [1 Mark: Method].\n\n"
        f"**Step 2:** Multiply and subtract to find remainder: ${dividend} - ({divisor} \\times {quotient}) = {rem}$ [1 Mark: Accuracy].\n\n"
        f"$$\\therefore \\mathbf{{{quotient} \\text{{ rem }} {rem}}}$$"
    )
    return {
        "id": f"g7_wn_36_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": ans_str,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "36_long_division_with_remainder",
        "hints": {
            "tier_1": "Calculate the whole number quotient first.",
            "tier_2": f"Multiply {divisor} × {quotient} and subtract from {dividend}.",
            "tier_3": f"{ans_str}."
        }
    }


def arch_37_division_word_problem_equal_sharing_remainder(rng: random.Random) -> Dict[str, Any]:
    crates = rng.randint(14, 25)
    oranges = rng.randint(1200, 2400)
    per_crate = oranges // crates
    leftover = oranges % crates

    prompt = (
        f"A citrus farm in Nelspruit packs **{oranges} oranges** equally into **{crates} export crates**.\n\n"
        f"1. How many oranges are packed into each crate?\n"
        f"2. How many leftover oranges cannot be packed into a full crate?"
    )
    sol = (
        f"**Step 1:** Divide: ${oranges} \\div {crates} = {per_crate}$ [1 Mark: Method].\n\n"
        f"**Step 2:** Remainder: ${oranges} - ({crates} \\times {per_crate}) = {leftover}$ [1 Mark: Accuracy].\n\n"
        f"$$\\therefore \\mathbf{{{per_crate} \\text{{ per crate; }} {leftover} \\text{{ leftover}}}}$$"
    )
    return {
        "id": f"g7_wn_37_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{per_crate} per crate; {leftover} leftover",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "37_division_word_problem_equal_sharing_remainder",
        "hints": {
            "tier_1": f"Divide total oranges by {crates}.",
            "tier_2": f"{oranges} ÷ {crates} = {per_crate} with remainder {leftover}.",
            "tier_3": f"{per_crate} per crate, {leftover} leftover."
        }
    }


def arch_38_multiplying_by_multiples_of_10_100_1000(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(14, 85)
    mult = rng.choice([200, 300, 400, 500, 600, 800])
    prod = a * mult
    prod_s = f"{prod:,}".replace(",", " ")

    prompt = f"Calculate mentally using factors of $10$: $${a} \\times {mult}$$"
    sol = (
        f"**Step 1:** Rewrite ${mult}$ as ${mult // 100} \\times 100$: $({a} \\times {mult // 100}) \\times 100$ [1 Mark: Method].\n\n"
        f"**Step 2:** Calculate: ${a * (mult // 100)} \\times 100 = \\mathbf{{{prod_s}}}$ [1 Mark: Accuracy]."
    )
    return {
        "id": f"g7_wn_38_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": prod_s,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "38_multiplying_by_multiples_of_10_100_1000",
        "hints": {
            "tier_1": f"Multiply {a} by {mult // 100}, then add two zeros.",
            "tier_2": f"{a} × {mult // 100} = {a * (mult // 100)}.",
            "tier_3": f"Product = {prod_s}."
        }
    }


def arch_39_dividing_by_multiples_of_10_100(rng: random.Random) -> Dict[str, Any]:
    divisor = rng.choice([20, 30, 40, 50, 60, 80])
    quotient = rng.randint(25, 95)
    dividend = divisor * quotient

    prompt = f"Calculate mentally: $${dividend} \\div {divisor}$$"
    sol = (
        f"**Step 1:** Cancel zero by dividing both numbers by $10$: ${dividend // 10} \\div {divisor // 10}$ [1 Mark: Method].\n\n"
        f"**Step 2:** Compute quotient: ${dividend // 10} \\div {divisor // 10} = \\mathbf{{{quotient}}}$ [1 Mark: Accuracy]."
    )
    return {
        "id": f"g7_wn_39_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{quotient}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "39_dividing_by_multiples_of_10_100",
        "hints": {
            "tier_1": "Divide both numbers by 10 first.",
            "tier_2": f"{dividend // 10} ÷ {divisor // 10}.",
            "tier_3": f"Quotient = {quotient}."
        }
    }


def arch_40_multiplication_estimation_by_rounding(rng: random.Random) -> Dict[str, Any]:
    n1 = rng.randint(48, 89)
    n2 = rng.randint(28, 72)
    r1 = round(n1 / 10) * 10
    r2 = round(n2 / 10) * 10
    est = r1 * r2

    prompt = (
        f"Estimate the product of **{n1}** and **{n2}** by rounding each factor to the nearest **10**."
    )
    sol = (
        f"**Step 1:** Round factors: ${n1} \\approx {r1}$ and ${n2} \\approx {r2}$ [1 Mark: Method].\n\n"
        f"**Step 2:** Multiply rounded values:\n\n"
        f"$${r1} \\times {r2} = \\mathbf{{{est:,}}} \\text{{ [1 Mark: Accuracy]}}$$"
    ).replace(",", " ")
    return {
        "id": f"g7_wn_40_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{est:,}".replace(",", " "),
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "40_multiplication_estimation_by_rounding",
        "hints": {
            "tier_1": "Round both numbers to nearest ten first.",
            "tier_2": f"{r1} × {r2}.",
            "tier_3": f"Estimated product = {est:,}.".replace(",", " ")
        }
    }


def arch_41_rate_and_unit_price_calculation(rng: random.Random) -> Dict[str, Any]:
    kg = rng.choice([3, 4, 5, 6, 8])
    unit_cost = rng.choice([24, 28, 35, 42, 55])
    total = kg * unit_cost

    prompt = (
        f"A bag of **{kg} kg** of maize meal costs **R{total}**.\n\n"
        f"Calculate the unit price per kilogram (R/kg)."
    )
    sol = (
        f"**Step 1:** Unit price formula: $\\text{{Total Cost}} \\div \\text{{Mass}}$ [1 Mark: Method].\n\n"
        f"**Step 2:** Calculate: $\\text{{R}}{total} \\div {kg} = \\mathbf{{\\text{{R}}{unit_cost}\\text{{ per kg}}}}$ [1 Mark: Accuracy]."
    )
    return {
        "id": f"g7_wn_41_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"R{unit_cost}/kg",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "41_rate_and_unit_price_calculation",
        "hints": {
            "tier_1": "Divide total cost by total kilograms.",
            "tier_2": f"{total} ÷ {kg}.",
            "tier_3": f"Unit price = R{unit_cost}/kg."
        }
    }


def arch_42_inverse_operation_division_check(rng: random.Random) -> Dict[str, Any]:
    d = rng.randint(14, 28)
    q = rng.randint(45, 95)
    r = rng.randint(1, d - 1)
    dividend = d * q + r

    prompt = (
        f"A learner calculates: $${dividend} \\div {d} = {q} \\text{{ remainder }} {r}$$\n\n"
        f"Show how to check this answer using multiplication and addition."
    )
    sol = (
        f"**Step 1:** Formula: $\\text{{Dividend}} = (\\text{{Divisor}} \\times \\text{{Quotient}}) + \\text{{Remainder}}$ [1 Mark: Method].\n\n"
        f"**Step 2:** Verify:\n\n"
        f"$$({d} \\times {q}) + {r} = {d*q} + {r} = \\mathbf{{{dividend}}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_wn_42_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"({d} × {q}) + {r} = {dividend}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "42_inverse_operation_division_check",
        "hints": {
            "tier_1": "Multiply divisor by quotient and add remainder.",
            "tier_2": f"({d} × {q}) + {r}.",
            "tier_3": f"= {dividend}."
        }
    }


# ==============================================================================
# CLUSTER 6: Properties of Operations & Problem Solving (43 - 50)
# ==============================================================================

def arch_43_commutative_property_addition_and_multiplication(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(14, 48)
    b = rng.randint(12, 35)

    prompt = (
        f"1. State the **Commutative Property** of addition.\n"
        f"2. Show that ${a} + {b} = {b} + {a}$."
    )
    sol = (
        f"**Step 1:** The commutative property states that changing the order of the numbers does not change the sum: $a + b = b + a$ [1 Mark: Method].\n\n"
        f"**Step 2:** Both orders yield ${a + b}$: ${a} + {b} = {b} + {a} = \\mathbf{{{a + b}}}$ [1 Mark: Accuracy]."
    )
    return {
        "id": f"g7_wn_43_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{a + b}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "43_commutative_property_addition_and_multiplication",
        "hints": {
            "tier_1": "Order does not matter in addition or multiplication.",
            "tier_2": f"{a} + {b} = {b} + {a}.",
            "tier_3": f"Sum = {a + b}."
        }
    }


def arch_44_associative_property_grouping_strategy(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([25, 40, 50])
    b = rng.randint(13, 39)
    c = rng.choice([75, 60, 50])
    tot = a + b + c

    prompt = (
        f"Use the **Associative Property** of addition to calculate the following mentally by grouping friendly numbers:\n\n"
        f"$${a} + {b} + {c}$$"
    )
    sol = (
        f"**Step 1:** Regroup friendly pair: $({a} + {c}) + {b} = {a + c} + {b}$ [1 Mark: Method].\n\n"
        f"**Step 2:** Final sum: ${a + c} + {b} = \\mathbf{{{tot}}}$ [1 Mark: Accuracy]."
    )
    return {
        "id": f"g7_wn_44_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{tot}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "44_associative_property_grouping_strategy",
        "hints": {
            "tier_1": f"Group {a} and {c} first to make {a + c}.",
            "tier_2": f"{a + c} + {b}.",
            "tier_3": f"Sum = {tot}."
        }
    }


def arch_45_distributive_property_multiplication_over_addition(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(6, 12)
    b = rng.randint(20, 50)
    c = rng.randint(3, 9)
    total = a * (b + c)

    prompt = (
        f"Apply the **Distributive Property** to expand and calculate:\n\n"
        f"$${a} \\times ({b} + {c})$$"
    )
    sol = (
        f"**Step 1:** Distribute factor ${a}$: $({a} \\times {b}) + ({a} \\times {c})$ [1 Mark: Method].\n\n"
        f"**Step 2:** Compute: ${a*b} + {a*c} = \\mathbf{{{total}}}$ [1 Mark: Accuracy]."
    )
    return {
        "id": f"g7_wn_45_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{total}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "45_distributive_property_multiplication_over_addition",
        "hints": {
            "tier_1": "Multiply the outside number by each number inside the brackets.",
            "tier_2": f"({a} × {b}) + ({a} × {c}).",
            "tier_3": f"Total = {total}."
        }
    }


def arch_46_distributive_property_multiplication_over_subtraction(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(7, 14)
    b = rng.randint(30, 60)
    c = rng.randint(2, 6)
    total = a * (b - c)

    prompt = (
        f"Use the **Distributive Property** to evaluate:\n\n"
        f"$${a} \\times ({b} - {c})$$"
    )
    sol = (
        f"**Step 1:** Distribute: $({a} \\times {b}) - ({a} \\times {c})$ [1 Mark: Method].\n\n"
        f"**Step 2:** Compute: ${a*b} - {a*c} = \\mathbf{{{total}}}$ [1 Mark: Accuracy]."
    )
    return {
        "id": f"g7_wn_46_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{total}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "46_distributive_property_multiplication_over_subtraction",
        "hints": {
            "tier_1": f"({a} × {b}) - ({a} × {c}).",
            "tier_2": f"{a*b} - {a*c}.",
            "tier_3": f"Result = {total}."
        }
    }


def arch_47_identity_elements_zero_and_one(rng: random.Random) -> Dict[str, Any]:
    n = rng.randint(345, 982)

    prompt = (
        f"1. Name the **identity element for addition** and show what happens when added to **{n}**.\n"
        f"2. Name the **identity element for multiplication** and show what happens when multiplied by **{n}**."
    )
    sol = (
        f"**Step 1:** Additive identity is **0**: ${n} + 0 = {n}$ [1 Mark: Method].\n\n"
        f"**Step 2:** Multiplicative identity is **1**: ${n} \\times 1 = {n}$ [1 Mark: Accuracy]."
    )
    return {
        "id": f"g7_wn_47_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"Addition: 0 ({n} + 0 = {n}); Multiplication: 1 ({n} × 1 = {n})",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "47_identity_elements_zero_and_one",
        "hints": {
            "tier_1": "Adding 0 leaves the number unchanged; multiplying by 1 leaves the number unchanged.",
            "tier_2": f"{n} + 0 = {n} and {n} × 1 = {n}.",
            "tier_3": "0 is additive identity; 1 is multiplicative identity."
        }
    }


def arch_48_bodmas_order_of_operations_whole_numbers(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(12, 35)
    b = rng.randint(4, 9)
    c = rng.randint(3, 8)
    d = rng.randint(2, 6)
    # a + b * (c - d)
    inner = c + d
    ans = a + b * inner

    prompt = f"Calculate using the correct order of operations (BODMAS):\n\n$${a} + {b} \\times ({c} + {d})$$"
    sol = (
        f"**Step 1:** Brackets first: ${c} + {d} = {inner}$ [1 Mark: Method].\n\n"
        f"**Step 2:** Multiplication next: ${b} \\times {inner} = {b * inner}$\n\n"
        f"**Step 3:** Addition: ${a} + {b * inner} = \\mathbf{{{ans}}}$ [1 Mark: Accuracy]."
    )
    return {
        "id": f"g7_wn_48_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{ans}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "48_bodmas_order_of_operations_whole_numbers",
        "hints": {
            "tier_1": "BODMAS: Brackets, Orders, Division/Multiplication, Addition/Subtraction.",
            "tier_2": f"First do ({c} + {d}) = {inner}, then multiply by {b}, then add {a}.",
            "tier_3": f"Answer = {ans}."
        }
    }


def arch_49_financial_profit_bulk_resale_word_problem(rng: random.Random) -> Dict[str, Any]:
    crate_cost = rng.randint(180, 260)
    units = 24
    sell_price = rng.randint(12, 16)
    rev = units * sell_price
    profit = rev - crate_cost

    prompt = (
        f"A vendor buys a wholesale crate containing **{units} cold drink cans** for **R{crate_cost}**.\n\n"
        f"The vendor sells each can for **R{sell_price}**.\n\n"
        f"Calculate the vendor's total profit after selling all {units} cans."
    )
    sol = (
        f"**Step 1:** Total Revenue = ${units} \\times \\text{{R}}{sell_price} = \\text{{R}}{rev}$ [1 Mark: Method].\n\n"
        f"**Step 2:** Profit = Revenue minus Cost: $\\text{{R}}{rev} - \\text{{R}}{crate_cost} = \\mathbf{{\\text{{R}}{profit}}}$ [1 Mark: Accuracy]."
    )
    return {
        "id": f"g7_wn_49_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"R{profit}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "49_financial_profit_bulk_resale_word_problem",
        "hints": {
            "tier_1": "Calculate total revenue by multiplying cans by unit price.",
            "tier_2": f"Revenue = R{rev}. Subtract crate cost R{crate_cost}.",
            "tier_3": f"Profit = R{profit}."
        }
    }


def arch_50_two_step_word_problem_hire_purchase_or_savings(rng: random.Random) -> Dict[str, Any]:
    target = rng.randint(2400, 4800)
    deposit = rng.randint(600, 1200)
    months = rng.choice([6, 8, 10, 12])
    # Ensure divisible
    rem = target - deposit
    monthly = math.ceil(rem / months)
    actual_target = deposit + monthly * months

    prompt = (
        f"A learner saves to buy a bicycle costing **R{actual_target}**.\n\n"
        f"The learner's parents contribute a deposit of **R{deposit}**.\n\n"
        f"The learner saves equal amounts each month for **{months} months** to pay the remaining balance.\n\n"
        f"Calculate the monthly amount the learner must save."
    )
    sol = (
        f"**Step 1:** Remaining balance: $\\text{{R}}{actual_target} - \\text{{R}}{deposit} = \\text{{R}}{monthly * months}$ [1 Mark: Method].\n\n"
        f"**Step 2:** Monthly saving: $\\text{{R}}{monthly * months} \\div {months} = \\mathbf{{\\text{{R}}{monthly}}}$ [1 Mark: Accuracy]."
    )
    return {
        "id": f"g7_wn_50_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"R{monthly}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "50_two_step_word_problem_hire_purchase_or_savings",
        "hints": {
            "tier_1": "Subtract the deposit from the total cost first.",
            "tier_2": f"Remaining amount = R{monthly * months}. Divide by {months}.",
            "tier_3": f"Monthly savings = R{monthly}."
        }
    }
