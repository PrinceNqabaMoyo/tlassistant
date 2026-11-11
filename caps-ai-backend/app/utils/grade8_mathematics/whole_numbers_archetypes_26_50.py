"""
Grade 8 Mathematics - Whole Numbers Generator (Archetypes 26 to 50).
100% CAPS-aligned deterministic question generator.
Adheres strictly to the 6-Pillar Generator Contract and Zero-Meta-Curriculum Invariant.
Grounded in curriculum_docs_auto/Mathematics_Gr8/Term 1/01. Whole numbers.md.
"""
from __future__ import annotations
import math
import random
from typing import Any, Dict, List, Optional


# ==============================================================================
# CLUSTER 3 (Cont.): Subtraction & Estimation (26 - 28)
# ==============================================================================

def arch_26_column_subtraction_with_multiple_borrows(rng: random.Random) -> Dict[str, Any]:
    n1 = rng.randint(45000, 95000)
    diff = rng.randint(12000, n1 - 10000)
    n2 = n1 - diff

    prompt = (
        f"Perform the column subtraction, showing all borrowing / decomposition steps:\n\n"
        f"$$\\begin{{array}}{{r@{{\\quad}}l}}\n"
        f"& {n1:,} \\\\\n"
        f"- & {n2:,} \\\\\n"
        f"\\hline\n"
        f"\\end{{array}}$$"
    )
    sol = (
        f"**Step 1:** Align numbers in columns by place value and subtract from right to left, borrowing 1 from the next column when minuend < subtrahend [1 Mark: Method].\n\n"
        f"**Step 2:** Result: $${n1:,} - {n2:,} = {diff:,}$$ [1 Mark: Accuracy]\n\n"
        f"$$\\therefore {diff:,}$$"
    )
    ans = f"{diff:,}"
    return {
        "id": f"g8_wn_26_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "26_column_subtraction_with_multiple_borrows",
        "hints": {
            "tier_1": "Subtract starting from the units column.",
            "tier_2": "When the top digit is smaller than the bottom digit, borrow 1 group of 10 from the column to the left.",
            "tier_3": f"Final difference is {diff:,}."
        },
        "misconception_tags": ["subtraction_smaller_from_larger_digit_error"]
    }


def arch_27_multi_step_sum_and_difference_word_problem(rng: random.Random) -> Dict[str, Any]:
    town1 = rng.choice(["Polokwane", "Nelspruit", "Kimberley", "George"])
    town2 = rng.choice(["Rustenburg", "Mthatha", "Upington", "Paarl"])
    pop1 = rng.randint(145000, 280000)
    pop2 = rng.randint(110000, pop1 - 15000)
    diff = pop1 - pop2
    total = pop1 + pop2

    prompt = (
        f"According to a municipal census, the population of {town1} is **{pop1:,}** and the population of {town2} is **{pop2:,}**.\n\n"
        f"1. What is the combined total population of both towns?\n"
        f"2. By how many residents does the population of {town1} exceed that of {town2}?"
    )
    sol = (
        f"**Step 1:** Total population = ${pop1:,} + {pop2:,} = {total:,}$ [1 Mark].\n\n"
        f"**Step 2:** Difference = ${pop1:,} - {pop2:,} = {diff:,}$ [1 Mark].\n\n"
        f"$$\\therefore \\text{{Total}} = {total:,}, \\quad \\text{{Difference}} = {diff:,}$$"
    )
    ans = f"1. {total:,}; 2. {diff:,}"
    return {
        "id": f"g8_wn_27_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "27_multi_step_sum_and_difference_word_problem",
        "hints": {
            "tier_1": "Combined total requires addition; difference requires subtraction.",
            "tier_2": f"Add {pop1} + {pop2} for total; subtract {pop1} - {pop2} for difference.",
            "tier_3": f"Total = {total:,}; Difference = {diff:,}."
        },
        "misconception_tags": ["word_problem_operation_selection_error"]
    }


def arch_28_estimating_sums_and_differences_via_rounding(rng: random.Random) -> Dict[str, Any]:
    n1 = rng.randint(23400, 68900)
    n2 = rng.randint(12300, 45600)
    r1 = round(n1 / 1000) * 1000
    r2 = round(n2 / 1000) * 1000
    est = r1 + r2
    exact = n1 + n2

    prompt = (
        f"For the calculation $${n1:,} + {n2:,}$$:\n\n"
        f"1. Estimate the sum by rounding each number off to the nearest 1 000 first.\n"
        f"2. Calculate the exact sum.\n"
        f"3. Calculate the difference between the exact answer and your estimated answer."
    )
    diff = abs(exact - est)
    sol = (
        f"**Step 1:** Rounding to nearest 1 000: ${n1:,} \\approx {r1:,}$ and ${n2:,} \\approx {r2:,}$.\n"
        f"$$\\text{{Estimated sum}} = {r1:,} + {r2:,} = {est:,}$$ [1 Mark]\n\n"
        f"**Step 2:** Exact sum: $${n1:,} + {n2:,} = {exact:,}$$ [1 Mark]\n\n"
        f"**Step 3:** Difference: $$|{exact:,} - {est:,}| = {diff:,}$$ [1 Mark]\n\n"
        f"$$\\therefore \\text{{Estimate}} = {est:,}, \\quad \\text{{Exact}} = {exact:,}, \\quad \\text{{Difference}} = {diff:,}$$"
    )
    ans = f"1. {est:,}; 2. {exact:,}; 3. {diff:,}"
    return {
        "id": f"g8_wn_28_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 1,
        "subskill": "28_estimating_sums_and_differences_via_rounding",
        "hints": {
            "tier_1": "Round both numbers to the nearest 1 000 before adding for the estimate.",
            "tier_2": f"Rounded: {r1:,} + {r2:,} = {est:,}.",
            "tier_3": f"Exact sum is {exact:,}; difference is {diff:,}."
        },
        "misconception_tags": ["rounding_after_calculation_error"]
    }


# ==============================================================================
# CLUSTER 4: Multi-Digit Multiplication & Division (29 - 36)
# ==============================================================================

def arch_29_multiplying_by_multiples_of_10_100_1000(rng: random.Random) -> Dict[str, Any]:
    n = rng.randint(24, 85)
    factor = rng.choice([20, 30, 40, 50, 60, 200, 300, 400, 500, 2000])
    ans = n * factor

    prompt = (
        f"Calculate using mental multiplication strategies:\n\n"
        f"$${n} \\times {factor:,}$$\n\n"
        f"Show how breaking {factor:,} into a single digit multiplied by a power of 10 simplifies the calculation."
    )
    base_d = int(str(factor)[0])
    p10 = factor // base_d
    step1 = n * base_d
    sol = (
        f"**Step 1:** Factorize {factor:,}: $${factor:,} = {base_d} \\times {p10:,}$$ [1 Mark: Method]\n\n"
        f"**Step 2:** Multiply: $$({n} \\times {base_d}) \\times {p10:,} = {step1} \\times {p10:,} = {ans:,}$$ [1 Mark: Accuracy]\n\n"
        f"$$\\therefore {ans:,}$$"
    )
    ans_text = f"({n} × {base_d}) × {p10:,} = {step1} × {p10:,} = {ans:,}"
    return {
        "id": f"g8_wn_29_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": str(ans),
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "29_multiplying_by_multiples_of_10_100_1000",
        "hints": {
            "tier_1": f"Multiply {n} by {base_d}, then multiply by {p10:,}.",
            "tier_2": f"{n} × {base_d} = {step1}.",
            "tier_3": f"{step1} × {p10:,} = {ans:,}."
        },
        "misconception_tags": ["trailing_zeros_omission_error"]
    }


def arch_30_multiplying_3_digit_by_2_digit_column_method(rng: random.Random) -> Dict[str, Any]:
    n1 = rng.randint(145, 680)
    n2 = rng.randint(24, 78)
    prod = n1 * n2

    prompt = (
        f"Calculate the product using vertical column multiplication, showing both partial products:\n\n"
        f"$$\\begin{{array}}{{r@{{\\quad}}l}}\n"
        f"& {n1} \\\\\n"
        f"\\times & {n2} \\\\\n"
        f"\\hline\n"
        f"\\end{{array}}$$"
    )
    u = n2 % 10
    t = (n2 // 10) * 10
    p_u = n1 * u
    p_t = n1 * t
    sol = (
        f"**Step 1:** Multiply by units: ${n1} \\times {u} = {p_u:,}$ [1 Mark: Partial Product 1].\n\n"
        f"**Step 2:** Multiply by tens: ${n1} \\times {t} = {p_t:,}$ [1 Mark: Partial Product 2].\n\n"
        f"**Step 3:** Sum the partial products: ${p_u:,} + {p_t:,} = {prod:,}$ [1 Mark: Total].\n\n"
        f"$$\\therefore {prod:,}$$"
    )
    ans = f"{prod:,}"
    return {
        "id": f"g8_wn_30_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 1,
        "subskill": "30_multiplying_3_digit_by_2_digit_column_method",
        "hints": {
            "tier_1": f"Multiply {n1} by {u}, then multiply {n1} by {t}.",
            "tier_2": f"Partial products: {p_u:,} and {p_t:,}.",
            "tier_3": f"Sum is {prod:,}."
        },
        "misconception_tags": ["column_multiplication_placeholder_zero_forgotten"]
    }


def arch_31_multiplying_4_digit_by_2_digit_with_carries(rng: random.Random) -> Dict[str, Any]:
    n1 = rng.randint(1240, 4890)
    n2 = rng.randint(32, 85)
    prod = n1 * n2

    prompt = (
        f"Calculate the product of **{n1:,}** and **{n2}** using the standard multiplication algorithm."
    )
    sol = (
        f"**Step 1:** Set up vertical multiplication and compute partial products [1 Mark: Method].\n\n"
        f"**Step 2:** Multiply and sum accurately:\n"
        f"$${n1:,} \\times {n2} = {prod:,}$$ [1 Mark: Accuracy]\n\n"
        f"$$\\therefore {prod:,}$$"
    )
    ans = f"{prod:,}"
    return {
        "id": f"g8_wn_31_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "31_multiplying_4_digit_by_2_digit_with_carries",
        "hints": {
            "tier_1": "Multiply each digit carefully from right to left, noting carry values.",
            "tier_2": "Remember to place a zero in the units column when multiplying by the tens digit.",
            "tier_3": f"Product is {prod:,}."
        },
        "misconception_tags": ["large_multiplication_carry_addition_error"]
    }


def arch_32_distributive_breakdown_multiplication(rng: random.Random) -> Dict[str, Any]:
    n1 = rng.randint(1200, 3500)
    tens_digit = rng.randint(3, 7)
    units_digit = rng.randint(2, 8)
    n2 = tens_digit * 10 + units_digit
    prod = n1 * n2

    prompt = (
        f"Use the **distributive breakdown method** (expanded notation) to calculate:\n\n"
        f"$${n2} \\times {n1:,}$$\n\n"
        f"1. Expand **{n2}** into $({tens_digit * 10} + {units_digit})$.\n"
        f"2. Write out the two partial multiplication terms and evaluate the final product."
    )
    p1 = (tens_digit * 10) * n1
    p2 = units_digit * n1
    sol = (
        f"**Step 1:** Expand {n2}: $${n2} \\times {n1:,} = ({tens_digit * 10} \\times {n1:,}) + ({units_digit} \\times {n1:,})$$ [1 Mark: Expansion]\n\n"
        f"**Step 2:** Calculate partial products:\n"
        f"$$= {p1:,} + {p2:,} = {prod:,}$$ [1 Mark: Calculation]\n\n"
        f"$$\\therefore {prod:,}$$"
    )
    ans = f"1. ({tens_digit * 10} × {n1:,}) + ({units_digit} × {n1:,}); 2. {prod:,}"
    return {
        "id": f"g8_wn_32_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "32_distributive_breakdown_multiplication",
        "hints": {
            "tier_1": f"Split {n2} into {tens_digit * 10} and {units_digit}.",
            "tier_2": f"Calculate ({tens_digit * 10} × {n1:,}) and ({units_digit} × {n1:,}).",
            "tier_3": f"{p1:,} + {p2:,} = {prod:,}."
        },
        "misconception_tags": ["expanded_multiplication_splitting_error"]
    }


def arch_33_long_division_3_digit_by_1_digit_with_remainder(rng: random.Random) -> Dict[str, Any]:
    divisor = rng.randint(4, 9)
    quot = rng.randint(35, 95)
    rem = rng.randint(1, divisor - 1)
    dividend = divisor * quot + rem

    prompt = (
        f"Divide **{dividend}** by **{divisor}** without using a calculator.\n\n"
        f"State the quotient and the remainder in the form: **$q \\text{{ R }} r$**."
    )
    sol = (
        f"**Step 1:** Perform long division dividing into each digit of {dividend} [1 Mark: Method].\n\n"
        f"**Step 2:** Quotient = **{quot}**, Remainder = **{rem}** [1 Mark: Accuracy].\n\n"
        f"$$\\therefore {quot} \\text{{ R }} {rem}$$"
    )
    ans = f"{quot} R {rem}"
    return {
        "id": f"g8_wn_33_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "33_long_division_3_digit_by_1_digit_with_remainder",
        "hints": {
            "tier_1": f"Divide {dividend} by {divisor}.",
            "tier_2": f"{divisor} goes into {dividend} {quot} full times.",
            "tier_3": f"{quot} with remainder {rem} ({quot} R {rem})."
        },
        "misconception_tags": ["remainder_greater_than_divisor_error"]
    }


def arch_34_long_division_4_digit_by_2_digit_exact(rng: random.Random) -> Dict[str, Any]:
    divisor = rng.randint(15, 45)
    quot = rng.randint(120, 380)
    dividend = divisor * quot

    prompt = (
        f"Use the long division method to calculate:\n\n"
        f"$${dividend:,} \\div {divisor}$$\n\n"
        f"Show all subtraction steps."
    )
    sol = (
        f"**Step 1:** Set up long division: divide, multiply, subtract, bring down [1 Mark: Method].\n\n"
        f"**Step 2:** The division works out exactly with remainder 0:\n"
        f"$${dividend:,} \\div {divisor} = {quot}$$ [1 Mark: Accuracy]\n\n"
        f"$$\\therefore {quot}$$"
    )
    ans = str(quot)
    return {
        "id": f"g8_wn_34_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "34_long_division_4_digit_by_2_digit_exact",
        "hints": {
            "tier_1": "Divide into the first two or three digits, multiply, subtract, and bring down.",
            "tier_2": f"{divisor} goes into {dividend:,} exactly {quot} times.",
            "tier_3": f"Quotient is {quot}."
        },
        "misconception_tags": ["long_division_bringing_down_error"]
    }


def arch_35_long_division_4_digit_by_2_digit_with_remainder(rng: random.Random) -> Dict[str, Any]:
    divisor = rng.randint(22, 55)
    quot = rng.randint(65, 180)
    rem = rng.randint(3, divisor - 1)
    dividend = divisor * quot + rem

    prompt = (
        f"Calculate $${dividend:,} \\div {divisor}$$ showing all long division workings.\n\n"
        f"Write your final answer in the format: **$q \\text{{ R }} r$**."
    )
    sol = (
        f"**Step 1:** Apply long division algorithm: divide, multiply, subtract, bring down [1 Mark].\n\n"
        f"**Step 2:** Quotient = **{quot}**, Remainder = **{rem}** [1 Mark].\n\n"
        f"$$\\therefore {quot} \\text{{ R }} {rem}$$"
    )
    ans = f"{quot} R {rem}"
    return {
        "id": f"g8_wn_35_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "35_long_division_4_digit_by_2_digit_with_remainder",
        "hints": {
            "tier_1": f"Divide {dividend:,} by {divisor}.",
            "tier_2": f"{divisor} × {quot} = {divisor * quot:,}.",
            "tier_3": f"{quot} with remainder {rem} ({quot} R {rem})."
        },
        "misconception_tags": ["remainder_subtraction_slip"]
    }


def arch_36_multiplication_division_inverse_verification(rng: random.Random) -> Dict[str, Any]:
    d = rng.randint(12, 35)
    q = rng.randint(45, 120)
    r = rng.randint(1, d - 1)
    n = d * q + r

    prompt = (
        f"A learner solved a division problem and obtained:\n\n"
        f"$${n:,} \\div {d} = {q} \\text{{ R }} {r}$$\n\n"
        f"1. State the formula relating Dividend, Divisor, Quotient, and Remainder.\n"
        f"2. Use multiplication and addition to verify whether the learner's answer is correct."
    )
    prod = d * q
    check = prod + r
    sol = (
        f"**Step 1:** Division relation: $\\text{{Dividend}} = (\\text{{Divisor}} \\times \\text{{Quotient}}) + \\text{{Remainder}}$ [1 Mark].\n\n"
        f"**Step 2:** Verification calculation:\n"
        f"$$({d} \\times {q}) + {r} = {prod:,} + {r} = {check:,}$$ [1 Mark]\n\n"
        f"Since ${check:,} = {n:,}$, the answer is **correct** [1 Mark].\n\n"
        f"$$\\therefore \\text{{Verified correct: }} ({d} \\times {q}) + {r} = {n:,}$$"
    )
    ans = f"1. Dividend = (Divisor × Quotient) + Remainder; 2. ({d} × {q}) + {r} = {prod:,} + {r} = {n:,} (Correct)"
    return {
        "id": f"g8_wn_36_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 1,
        "subskill": "36_multiplication_division_inverse_verification",
        "hints": {
            "tier_1": "Multiply the divisor by the quotient and add the remainder.",
            "tier_2": f"Calculate ({d} × {q}) + {r}.",
            "tier_3": f"{prod:,} + {r} = {n:,}. Correct."
        },
        "misconception_tags": ["division_check_formula_inversion"]
    }


# ==============================================================================
# CLUSTER 5: Ratio, Rate & Proportion (37 - 44)
# ==============================================================================

def arch_37_simplifying_ratios_to_simplest_form(rng: random.Random) -> Dict[str, Any]:
    common = rng.choice([6, 8, 12, 14, 15, 18, 24])
    a = rng.choice([2, 3, 4, 5, 7])
    b = rng.choice([3, 5, 7, 9, 11])
    while math.gcd(a, b) != 1:
        b += 1
    term1 = a * common
    term2 = b * common

    prompt = (
        f"Simplify the ratio to its simplest form (lowest terms):\n\n"
        f"$${term1} : {term2}$$"
    )
    sol = (
        f"**Step 1:** Find the $\\text{{HCF}}({term1}, {term2}) = {common}$ [1 Mark: Method].\n\n"
        f"**Step 2:** Divide both parts of the ratio by their HCF:\n"
        f"$$\\frac{{{term1}}}{{{common}}} : \\frac{{{term2}}}{{{common}}} = {a} : {b}$$ [1 Mark: Accuracy]\n\n"
        f"$$\\therefore {a} : {b}$$"
    )
    ans = f"{a} : {b}"
    return {
        "id": f"g8_wn_37_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "37_simplifying_ratios_to_simplest_form",
        "hints": {
            "tier_1": "Divide both numbers by their highest common factor.",
            "tier_2": f"Both numbers divide by {common}.",
            "tier_3": f"{term1} : {term2} = {a} : {b}."
        },
        "misconception_tags": ["ratio_incomplete_simplification"]
    }


def arch_38_dividing_an_amount_in_a_two_part_ratio(rng: random.Random) -> Dict[str, Any]:
    p1 = rng.choice(["Sipho", "Thabo", "Kagiso", "Lethabo"])
    p2 = rng.choice(["Zola", "Buhle", "Nomsa", "Amina"])
    r1 = rng.randint(2, 5)
    r2 = rng.randint(3, 7)
    while math.gcd(r1, r2) != 1:
        r2 += 1
    parts = r1 + r2
    unit_val = rng.choice([25, 40, 50, 75, 100, 150])
    total = parts * unit_val
    share1 = r1 * unit_val
    share2 = r2 * unit_val

    prompt = (
        f"Divide an amount of **R{total:,}** between {p1} and {p2} in the ratio **{r1} : {r2}**.\n\n"
        f"1. How many total parts are there in the ratio?\n"
        f"2. How much money does each person receive?"
    )
    sol = (
        f"**Step 1:** Total parts = ${r1} + {r2} = {parts}$ parts [1 Mark].\n\n"
        f"**Step 2:** Value per part = $\\frac{{\\text{{R}}{total:,}}}{{{parts}}} = \\text{{R}}{unit_val}$ [1 Mark].\n\n"
        f"**Step 3:** Shares:\n"
        f"- {p1}: ${r1} \\times \\text{{R}}{unit_val} = \\text{{R}}{share1:,}$\n"
        f"- {p2}: ${r2} \\times \\text{{R}}{unit_val} = \\text{{R}}{share2:,}$ [1 Mark].\n\n"
        f"$$\\therefore {p1}: \\text{{R}}{share1:,}, \\quad {p2}: \\text{{R}}{share2:,}$$"
    )
    ans = f"1. {parts} parts; 2. {p1}: R{share1:,}, {p2}: R{share2:,}"
    return {
        "id": f"g8_wn_38_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 1,
        "subskill": "38_dividing_an_amount_in_a_two_part_ratio",
        "hints": {
            "tier_1": f"Add the ratio terms: {r1} + {r2} = {parts}.",
            "tier_2": f"Divide R{total:,} by {parts} to find the value of 1 part (R{unit_val}).",
            "tier_3": f"{p1} gets R{share1:,} and {p2} gets R{share2:,}."
        },
        "misconception_tags": ["ratio_sharing_total_parts_omission"]
    }


def arch_39_dividing_an_amount_in_a_three_part_ratio(rng: random.Random) -> Dict[str, Any]:
    r1, r2, r3 = 2, 3, 5
    parts = r1 + r2 + r3
    unit_val = rng.choice([30, 45, 60, 80, 120])
    total = parts * unit_val
    s1, s2, s3 = r1 * unit_val, r2 * unit_val, r3 * unit_val

    prompt = (
        f"Three partners invest in a small business and agree to divide a annual bonus of **R{total:,}** "
        f"in the ratio **{r1} : {r2} : {r3}**.\n\n"
        f"Determine the exact bonus payout for each partner."
    )
    sol = (
        f"**Step 1:** Total parts = ${r1} + {r2} + {r3} = {parts}$ [1 Mark].\n\n"
        f"**Step 2:** Value per part = $\\text{{R}}{total:,} \\div {parts} = \\text{{R}}{unit_val}$ [1 Mark].\n\n"
        f"**Step 3:** Payouts:\n"
        f"- Partner 1: ${r1} \\times \\text{{R}}{unit_val} = \\text{{R}}{s1:,}$\n"
        f"- Partner 2: ${r2} \\times \\text{{R}}{unit_val} = \\text{{R}}{s2:,}$\n"
        f"- Partner 3: ${r3} \\times \\text{{R}}{unit_val} = \\text{{R}}{s3:,}$ [1 Mark].\n\n"
        f"$$\\therefore \\text{{R}}{s1:,}, \\quad \\text{{R}}{s2:,}, \\quad \\text{{R}}{s3:,}$$"
    )
    ans = f"R{s1:,}, R{s2:,}, R{s3:,}"
    return {
        "id": f"g8_wn_39_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 1,
        "subskill": "39_dividing_an_amount_in_a_three_part_ratio",
        "hints": {
            "tier_1": f"Sum of parts = {r1} + {r2} + {r3} = {parts}.",
            "tier_2": f"Each part is R{unit_val}.",
            "tier_3": f"Payouts: R{s1:,}, R{s2:,}, R{s3:,}."
        },
        "misconception_tags": ["three_part_ratio_part_sum_error"]
    }


def arch_40_equivalent_ratios_finding_unknown_term(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([3, 4, 5, 7])
    b = rng.choice([4, 6, 8, 9])
    while a == b:
        b = rng.choice([4, 6, 8, 9])
    k = rng.randint(4, 12)
    c = a * k
    d = b * k

    prompt = (
        f"Solve for the unknown value $x$ in the equivalent ratio statement:\n\n"
        f"$${a} : {b} = {c} : x$$"
    )
    sol = (
        f"**Step 1:** Write as equivalent fractions:\n"
        f"$$\\frac{{{a}}}{{{b}}} = \\frac{{{c}}}{{x}}$$ [1 Mark: Method]\n\n"
        f"**Step 2:** Cross-multiply or find scaling factor $k = {c} \\div {a} = {k}$:\n"
        f"$$x = {b} \\times {k} = {d}$$ [1 Mark: Accuracy]\n\n"
        f"$$\\therefore x = {d}$$"
    )
    ans = str(d)
    return {
        "id": f"g8_wn_40_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "40_equivalent_ratios_finding_unknown_term",
        "hints": {
            "tier_1": f"Find the multiplier from {a} to {c}.",
            "tier_2": f"{c} ÷ {a} = {k}. Multiply {b} by {k}.",
            "tier_3": f"x = {d}."
        },
        "misconception_tags": ["ratio_cross_multiplication_inversion"]
    }


def arch_41_constant_rate_speed_distance_time(rng: random.Random) -> Dict[str, Any]:
    speed = rng.choice([60, 75, 80, 90, 100, 110, 120])
    hours = rng.randint(2, 6)
    dist = speed * hours

    prompt = (
        f"A minibus taxi travels between Johannesburg and Durban at a constant average speed of **{speed} km/h**.\n\n"
        f"1. How far will the taxi travel in **{hours} hours**?\n"
        f"2. Write down the formula relating distance, speed, and time."
    )
    sol = (
        f"**Step 1:** Formula: $\\text{{Distance}} = \\text{{Speed}} \\times \\text{{Time}}$ [1 Mark].\n\n"
        f"**Step 2:** Calculate: $${speed} \\times {hours} = {dist}\\text{{ km}}$$ [1 Mark].\n\n"
        f"$$\\therefore \\text{{Distance}} = {dist}\\text{{ km}}$$"
    )
    ans = f"1. {dist} km; 2. Distance = Speed × Time"
    return {
        "id": f"g8_wn_41_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "41_constant_rate_speed_distance_time",
        "hints": {
            "tier_1": "Distance = Speed × Time.",
            "tier_2": f"Multiply {speed} km/h by {hours} hours.",
            "tier_3": f"Total distance is {dist} km."
        },
        "misconception_tags": ["speed_distance_time_formula_confusion"]
    }


def arch_42_constant_rate_consumption_and_pricing(rng: random.Random) -> Dict[str, Any]:
    qty1 = rng.choice([3, 4, 5])
    unit_p = rng.randint(14, 38)
    cost1 = qty1 * unit_p
    qty2 = rng.choice([7, 8, 9, 12])
    cost2 = qty2 * unit_p

    prompt = (
        f"A local supermarket sells **{qty1} kg** of rice for **R{cost1}**.\n\n"
        f"1. Calculate the unit price per kilogram (R/kg).\n"
        f"2. How much will **{qty2} kg** of the same rice cost at this rate?"
    )
    sol = (
        f"**Step 1:** Unit rate = $\\text{{R}}{cost1} \\div {qty1} = \\text{{R}}{unit_p}\\text{{/kg}}$ [1 Mark].\n\n"
        f"**Step 2:** Cost for {qty2} kg = ${qty2} \\times \\text{{R}}{unit_p} = \\text{{R}}{cost2}$ [1 Mark].\n\n"
        f"$$\\therefore \\text{{R}}{unit_p}/\\text{{kg}}, \\quad \\text{{Cost}} = \\text{{R}}{cost2}$$"
    )
    ans = f"1. R{unit_p}/kg; 2. R{cost2}"
    return {
        "id": f"g8_wn_42_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "42_constant_rate_consumption_and_pricing",
        "hints": {
            "tier_1": "Find the price of 1 kg first by dividing.",
            "tier_2": f"Unit price = R{cost1} ÷ {qty1} = R{unit_p}/kg.",
            "tier_3": f"{qty2} kg costs {qty2} × R{unit_p} = R{cost2}."
        },
        "misconception_tags": ["unit_rate_division_order_slip"]
    }


def arch_43_growth_rate_and_population_increase(rng: random.Random) -> Dict[str, Any]:
    trees = rng.randint(450, 1200)
    rate_per_month = rng.randint(35, 80)
    months = rng.choice([4, 6, 8, 12])
    growth = rate_per_month * months
    total = trees + growth

    prompt = (
        f"An indigenous timber forestry plantation has **{trees} trees**. "
        f"The community planting team plants new saplings at a constant rate of **{rate_per_month} trees per month**.\n\n"
        f"1. How many new trees are planted over **{months} months**?\n"
        f"2. What will be the total number of trees in the plantation after {months} months?"
    )
    sol = (
        f"**Step 1:** Trees added = ${rate_per_month} \\times {months} = {growth}$ trees [1 Mark].\n\n"
        f"**Step 2:** Total = ${trees} + {growth} = {total}$ trees [1 Mark].\n\n"
        f"$$\\therefore \\text{{Added}} = {growth}, \\quad \\text{{Total}} = {total}$$"
    )
    ans = f"1. {growth} trees; 2. {total} trees"
    return {
        "id": f"g8_wn_43_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "43_growth_rate_and_population_increase",
        "hints": {
            "tier_1": "Multiply rate per month by number of months.",
            "tier_2": "Add the growth to the starting count.",
            "tier_3": f"Added = {growth}; Total = {total}."
        },
        "misconception_tags": ["growth_rate_initial_value_omission"]
    }


def arch_44_direct_proportion_production_table(rng: random.Random) -> Dict[str, Any]:
    rate = rng.randint(12, 28)
    h1, h2, h3 = 2, 5, 8
    p1 = rate * h1
    p2 = rate * h2
    p3 = rate * h3

    prompt = (
        f"A bakery machine produces bread loaves at a constant rate.\n\n"
        f"| Hours ($h$) | 2 | 5 | 8 |\n"
        f"|---|---|---|---|\n"
        f"| Loaves ($L$) | {p1} | $x$ | {p3} |\n\n"
        f"1. Determine the constant rate of production in loaves per hour.\n"
        f"2. Calculate the missing value of $x$."
    )
    sol = (
        f"**Step 1:** Rate = $\\frac{{{p1}}}{{2}} = {rate}$ loaves/hour [1 Mark].\n\n"
        f"**Step 2:** Value $x = {h2} \\times {rate} = {p2}$ loaves [1 Mark].\n\n"
        f"$$\\therefore \\text{{Rate}} = {rate} \\text{{ loaves/h}}, \\quad x = {p2}$$"
    )
    ans = f"1. {rate} loaves/hour; 2. x = {p2}"
    return {
        "id": f"g8_wn_44_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "44_direct_proportion_production_table",
        "hints": {
            "tier_1": "Find the constant unit rate by dividing loaves by hours.",
            "tier_2": f"Rate = {p1} / 2 = {rate} per hour.",
            "tier_3": f"For 5 hours, x = 5 × {rate} = {p2}."
        },
        "misconception_tags": ["direct_proportion_constant_rate_error"]
    }


# ==============================================================================
# CLUSTER 6: Financial Mathematics (45 - 50)
# ==============================================================================

def arch_45_cost_price_selling_price_and_profit(rng: random.Random) -> Dict[str, Any]:
    cp = rng.choice([150, 200, 250, 300, 400, 500])
    pct_profit = rng.choice([10, 20, 25, 30, 40, 50])
    profit = int(cp * pct_profit / 100)
    sp = cp + profit

    prompt = (
        f"A craft trader buys handmade beaded wire sculptures at a cost price of **R{cp}** each. "
        f"She sells each sculpture for **R{sp}**.\n\n"
        f"1. Calculate the rand profit made on each sculpture.\n"
        f"2. Calculate the percentage profit based on the cost price."
    )
    sol = (
        f"**Step 1:** Profit = $\\text{{Selling Price}} - \\text{{Cost Price}} = \\text{{R}}{sp} - \\text{{R}}{cp} = \\text{{R}}{profit}$ [1 Mark].\n\n"
        f"**Step 2:** Percentage profit = $\\frac{{\\text{{Profit}}}}{{\\text{{Cost Price}}}} \\times 100\\% = \\frac{{{profit}}}{{{cp}}} \\times 100\\% = {pct_profit}\\%$ [1 Mark].\n\n"
        f"$$\\therefore \\text{{Profit}} = \\text{{R}}{profit}, \\quad \\text{{Percentage Profit}} = {pct_profit}\\%$$"
    )
    ans = f"1. R{profit}; 2. {pct_profit}%"
    return {
        "id": f"g8_wn_45_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "45_cost_price_selling_price_and_profit",
        "hints": {
            "tier_1": "Profit = Selling Price - Cost Price.",
            "tier_2": "Percentage profit is always calculated over the Cost Price.",
            "tier_3": f"Profit = R{profit}; Percentage = {pct_profit}%."
        },
        "misconception_tags": ["percentage_profit_over_selling_price_error"]
    }


def arch_46_cost_price_selling_price_and_loss(rng: random.Random) -> Dict[str, Any]:
    cp = rng.choice([200, 250, 400, 500, 800])
    pct_loss = rng.choice([10, 15, 20, 25])
    loss = int(cp * pct_loss / 100)
    sp = cp - loss

    prompt = (
        f"A retailer purchased electronic accessories for **R{cp}**. "
        f"Due to excess stock, they were sold at a clearance price of **R{sp}**.\n\n"
        f"1. Calculate the loss incurred.\n"
        f"2. Determine the percentage loss based on the original cost price."
    )
    sol = (
        f"**Step 1:** Loss = $\\text{{Cost Price}} - \\text{{Selling Price}} = \\text{{R}}{cp} - \\text{{R}}{sp} = \\text{{R}}{loss}$ [1 Mark].\n\n"
        f"**Step 2:** Percentage loss = $\\frac{{\\text{{Loss}}}}{{\\text{{Cost Price}}}} \\times 100\\% = \\frac{{{loss}}}{{{cp}}} \\times 100\\% = {pct_loss}\\%$ [1 Mark].\n\n"
        f"$$\\therefore \\text{{Loss}} = \\text{{R}}{loss}, \\quad \\text{{Percentage Loss}} = {pct_loss}\\%$$"
    )
    ans = f"1. R{loss}; 2. {pct_loss}%"
    return {
        "id": f"g8_wn_46_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "46_cost_price_selling_price_and_loss",
        "hints": {
            "tier_1": "Loss = Cost Price - Selling Price.",
            "tier_2": "Percentage loss = (Loss / Cost Price) × 100%.",
            "tier_3": f"Loss = R{loss}; Percentage Loss = {pct_loss}%."
        },
        "misconception_tags": ["loss_calculated_over_discount_price"]
    }


def arch_47_percentage_discount_on_marked_price(rng: random.Random) -> Dict[str, Any]:
    marked = rng.choice([350, 450, 600, 750, 800, 1200])
    pct = rng.choice([10, 15, 20, 25, 30])
    discount = int(marked * pct / 100)
    sale_price = marked - discount

    prompt = (
        f"A winter jacket with a marked price of **R{marked}** is offered on sale at a **{pct}% discount**.\n\n"
        f"1. Calculate the rand value of the discount.\n"
        f"2. Determine the final sale price of the jacket."
    )
    sol = (
        f"**Step 1:** Discount = $\\frac{{{pct}}}{{100}} \\times \\text{{R}}{marked} = \\text{{R}}{discount}$ [1 Mark].\n\n"
        f"**Step 2:** Sale price = $\\text{{R}}{marked} - \\text{{R}}{discount} = \\text{{R}}{sale_price}$ [1 Mark].\n\n"
        f"$$\\therefore \\text{{Discount}} = \\text{{R}}{discount}, \\quad \\text{{Sale Price}} = \\text{{R}}{sale_price}$$"
    )
    ans = f"1. R{discount}; 2. R{sale_price}"
    return {
        "id": f"g8_wn_47_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "47_percentage_discount_on_marked_price",
        "hints": {
            "tier_1": f"Calculate {pct}% of R{marked}.",
            "tier_2": "Subtract the discount from the original marked price.",
            "tier_3": f"Discount = R{discount}; Sale price = R{sale_price}."
        },
        "misconception_tags": ["discount_added_instead_of_subtracted"]
    }


def arch_48_value_added_tax_vat_15_percent_addition(rng: random.Random) -> Dict[str, Any]:
    excl = rng.choice([200, 400, 600, 800, 1200, 1600, 2400])
    vat = int(excl * 0.15)
    incl = excl + vat

    prompt = (
        f"In South Africa, Value Added Tax (VAT) is charged at a standard rate of **15%**.\n\n"
        f"A laptop repair service quotes a price of **R{excl:,}** excluding VAT.\n\n"
        f"1. Calculate the amount of VAT payable.\n"
        f"2. Calculate the total price including VAT."
    )
    sol = (
        f"**Step 1:** VAT = $15\\% \\times \\text{{R}}{excl:,} = 0.15 \\times {excl} = \\text{{R}}{vat:,}$ [1 Mark].\n\n"
        f"**Step 2:** Total price = $\\text{{R}}{excl:,} + \\text{{R}}{vat:,} = \\text{{R}}{incl:,}$ [1 Mark].\n\n"
        f"$$\\therefore \\text{{VAT}} = \\text{{R}}{vat:,}, \\quad \\text{{Total (incl. VAT)}} = \\text{{R}}{incl:,}$$"
    )
    ans = f"1. R{vat:,}; 2. R{incl:,}"
    return {
        "id": f"g8_wn_48_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "48_value_added_tax_vat_15_percent_addition",
        "hints": {
            "tier_1": "Calculate 15% of the exclusive price.",
            "tier_2": "Add the VAT amount to the exclusive price.",
            "tier_3": f"VAT = R{vat:,}; Total = R{incl:,}."
        },
        "misconception_tags": ["vat_rate_14_percent_legacy_error"]
    }


def arch_49_value_added_tax_extracting_exclusive_price(rng: random.Random) -> Dict[str, Any]:
    base = rng.choice([230, 460, 690, 920, 1150, 2300])
    # base is 115% of something: excl = base / 1.15
    excl = int(base / 1.15)
    vat = base - excl

    prompt = (
        f"A school buys sports equipment for **R{base:,}**, which **includes 15% VAT**.\n\n"
        f"1. Calculate the price of the equipment excluding VAT.\n"
        f"2. Determine the exact amount of VAT included in the purchase price."
    )
    sol = (
        f"**Step 1:** Since the price includes 15% VAT, it represents $115\\%$ of the exclusive price:\n"
        f"$$\\text{{Price (excl. VAT)}} = \\frac{{\\text{{R}}{base:,}}}{{1.15}} = \\text{{R}}{excl:,}$$ [1 Mark]\n\n"
        f"**Step 2:** VAT amount = $\\text{{R}}{base:,} - \\text{{R}}{excl:,} = \\text{{R}}{vat:,}$ [1 Mark].\n\n"
        f"$$\\therefore \\text{{Excl. VAT}} = \\text{{R}}{excl:,}, \\quad \\text{{VAT}} = \\text{{R}}{vat:,}$$"
    )
    ans = f"1. R{excl:,}; 2. R{vat:,}"
    return {
        "id": f"g8_wn_49_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "49_value_added_tax_extracting_exclusive_price",
        "hints": {
            "tier_1": "Do not simply subtract 15% of the total. Divide by 1.15.",
            "tier_2": f"Exclusive price = R{base:,} / 1.15 = R{excl:,}.",
            "tier_3": f"VAT = R{base:,} - R{excl:,} = R{vat:,}."
        },
        "misconception_tags": ["subtracting_15_percent_from_inclusive_price_error"]
    }


def arch_50_simple_interest_annual_calculation(rng: random.Random) -> Dict[str, Any]:
    principal = rng.choice([2000, 3000, 4000, 5000, 6000, 8000, 10000])
    rate = rng.choice([6, 7, 8, 9, 10])
    years = rng.choice([2, 3, 4, 5])
    interest = int(principal * rate * years / 100)
    total = principal + interest

    prompt = (
        f"Sipho deposits **R{principal:,}** into a fixed savings account that earns simple interest at **{rate}% per annum** for **{years} years**.\n\n"
        f"1. Use the simple interest formula $I = \\frac{{P \\times r \\times t}}{{100}}$ to calculate the total interest earned.\n"
        f"2. Calculate the total accumulated amount in the account at the end of {years} years."
    )
    sol = (
        f"**Step 1:** Simple interest formula: $I = \\frac{{{principal} \\times {rate} \\times {years}}}{{100}} = \\text{{R}}{interest:,}$ [1 Mark].\n\n"
        f"**Step 2:** Total accumulated amount = $\\text{{Principal}} + \\text{{Interest}} = \\text{{R}}{principal:,} + \\text{{R}}{interest:,} = \\text{{R}}{total:,}$ [1 Mark].\n\n"
        f"$$\\therefore \\text{{Interest}} = \\text{{R}}{interest:,}, \\quad \\text{{Total}} = \\text{{R}}{total:,}$$"
    )
    ans = f"1. R{interest:,}; 2. R{total:,}"
    return {
        "id": f"g8_wn_50_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "50_simple_interest_annual_calculation",
        "hints": {
            "tier_1": "I = (P × r × t) / 100.",
            "tier_2": f"I = ({principal} × {rate} × {years}) / 100 = R{interest:,}.",
            "tier_3": f"Total amount = R{principal:,} + R{interest:,} = R{total:,}."
        },
        "misconception_tags": ["simple_interest_formula_substitution_error"]
    }
