"""
Grade 7 Mathematics - Working with Whole Numbers Generator (Archetypes 01 to 25).
100% CAPS-aligned deterministic question generator.
Adheres strictly to the 6-Pillar Generator Contract and Zero-Meta-Curriculum Invariant.
Grounded in curriculum_docs_auto/Mathematics_Gr7/Term 1/01. Working with whole numbers.md.
"""
from __future__ import annotations
import math
import random
from typing import Any, Dict, List, Optional


# ==============================================================================
# CLUSTER 1: Place Value & Expanded Notation (01 - 08)
# ==============================================================================

def arch_01_place_value_digit_identification(rng: random.Random) -> Dict[str, Any]:
    places = [
        ("hundred thousands", 100000, 5),
        ("ten thousands", 10000, 4),
        ("thousands", 1000, 3),
        ("hundreds", 100, 2),
        ("tens", 10, 1),
        ("units", 1, 0),
    ]
    p_name, p_val, digit_pos = rng.choice(places)
    digits = [rng.randint(1, 9)] + [rng.randint(0, 9) for _ in range(5)]
    num = sum(d * (10 ** (5 - i)) for i, d in enumerate(digits))
    target_digit = digits[5 - digit_pos]
    value = target_digit * p_val

    num_str = f"{num:,}".replace(",", " ")
    prompt = (
        f"Consider the whole number: **{num_str}**.\n\n"
        f"1. Name the place value position of the digit **{target_digit}**.\n"
        f"2. Write down the numerical value represented by this digit."
    )
    sol = (
        f"**Step 1:** The digit **{target_digit}** occupies the **{p_name}** column [1 Mark: Method].\n\n"
        f"**Step 2:** Value = ${target_digit} \\times {p_val:,} = \\mathbf{{{value:,}}}$ [1 Mark: Accuracy].".replace(",", " ")
    )
    return {
        "id": f"g7_wn_01_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"Position: {p_name}; Value: {value:,}".replace(",", " "),
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "01_place_value_digit_identification",
        "hints": {
            "tier_1": "Count columns from the right: units, tens, hundreds, thousands, ten thousands, hundred thousands.",
            "tier_2": f"Multiply the digit {target_digit} by its place value ({p_val}).",
            "tier_3": f"Position: {p_name}, Value: {value}."
        }
    }


def arch_02_expanded_notation_to_standard_number(rng: random.Random) -> Dict[str, Any]:
    h_th = rng.randint(2, 8) * 100000
    t_th = rng.randint(1, 9) * 10000
    th = rng.randint(1, 9) * 1000
    h = rng.randint(1, 9) * 100
    t = rng.randint(1, 9) * 10
    u = rng.randint(1, 9)
    total = h_th + t_th + th + h + t + u

    expanded_terms = [f"{h_th:,}", f"{t_th:,}", f"{th:,}", f"{h:,}", f"{t:,}", f"{u}"]
    expanded_str = " + ".join(expanded_terms).replace(",", " ")
    total_str = f"{total:,}".replace(",", " ")

    prompt = (
        f"Write the following expanded notation sum as a single standard numeral:\n\n"
        f"$${expanded_str}$$"
    )
    sol = (
        f"**Step 1:** Add the values corresponding to each place value column [1 Mark: Method].\n\n"
        f"**Step 2:** Single number:\n\n"
        f"$$\\mathbf{{{total_str}}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_wn_02_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": total_str,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "02_expanded_notation_to_standard_number",
        "hints": {
            "tier_1": "Combine the digits into their respective place value columns.",
            "tier_2": f"Hundred thousands: {h_th // 100000}, Ten thousands: {t_th // 10000}, etc.",
            "tier_3": f"Single numeral is {total_str}."
        }
    }


def arch_03_standard_number_to_expanded_notation(rng: random.Random) -> Dict[str, Any]:
    d = [rng.randint(2, 9), rng.randint(1, 9), rng.randint(0, 9), rng.randint(1, 9), rng.randint(1, 9), rng.randint(1, 9)]
    num = d[0]*100000 + d[1]*10000 + d[2]*1000 + d[3]*100 + d[4]*10 + d[5]
    num_str = f"{num:,}".replace(",", " ")

    terms = [f"{d[0]*100000:,}", f"{d[1]*10000:,}"]
    if d[2] > 0:
        terms.append(f"{d[2]*1000:,}")
    terms.extend([f"{d[3]*100:,}", f"{d[4]*10:,}", f"{d[5]}"])
    exp_str = " + ".join(terms).replace(",", " ")

    prompt = f"Write the whole number **{num_str}** in full expanded notation."
    sol = (
        f"**Step 1:** Decompose each non-zero digit by its place value weight [1 Mark: Method].\n\n"
        f"**Step 2:** Expanded form:\n\n"
        f"$$\\mathbf{{{exp_str}}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_wn_03_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": exp_str,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "03_standard_number_to_expanded_notation",
        "hints": {
            "tier_1": "Break down each digit into its place value representation.",
            "tier_2": f"Start with {d[0]} × 100 000, then {d[1]} × 10 000...",
            "tier_3": f"Expanded notation: {exp_str}."
        }
    }


def arch_04_word_form_to_standard_numeral(rng: random.Random) -> Dict[str, Any]:
    th_part = rng.choice([
        (340, "three hundred and forty"),
        (512, "five hundred and twelve"),
        (205, "two hundred and five"),
        (480, "four hundred and eighty"),
        (625, "six hundred and twenty-five"),
    ])
    unit_part = rng.choice([
        (108, "one hundred and eight"),
        (450, "four hundred and fifty"),
        (314, "three hundred and fourteen"),
        (72, "seventy-two"),
    ])
    total = th_part[0] * 1000 + unit_part[0]
    words = f"{th_part[1]} thousand, {unit_part[1]}"
    ans_str = f"{total:,}".replace(",", " ")

    prompt = (
        f"Write down the standard number for the following verbal amount:\n\n"
        f"*\"{words}\"*"
    )
    sol = (
        f"**Step 1:** Translate thousands period: {th_part[0]} thousand $= {th_part[0]*1000:,}$ [1 Mark: Method].\n\n"
        f"**Step 2:** Add units period: ${th_part[0]*1000:,} + {unit_part[0]} = \\mathbf{{{ans_str}}}$ [1 Mark: Accuracy].".replace(",", " ")
    )
    return {
        "id": f"g7_wn_04_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": ans_str,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "04_word_form_to_standard_numeral",
        "hints": {
            "tier_1": "Separate the thousands group from the units group.",
            "tier_2": f"{th_part[0]} in the thousands period and {unit_part[0]:03d} in the units period.",
            "tier_3": f"Numeral is {ans_str}."
        }
    }


def arch_05_ordering_six_digit_numbers_ascending(rng: random.Random) -> Dict[str, Any]:
    base = rng.randint(400, 480) * 1000
    offsets = [rng.randint(10, 80), rng.randint(110, 250), rng.randint(310, 500), rng.randint(600, 950)]
    nums = [base + off for off in offsets]
    rng.shuffle(nums)
    s_nums = sorted(nums)
    raw_str = ", ".join(f"{x:,}".replace(",", " ") for x in nums)
    ans_str = "; ".join(f"{x:,}".replace(",", " ") for x in s_nums)

    prompt = (
        f"Arrange the following four numbers in **ascending order** (from smallest to biggest):\n\n"
        f"$$\\{{ {raw_str} \\}}$$"
    )
    sol = (
        f"**Step 1:** Compare place values starting from the highest column (hundred thousands, then ten thousands, etc.) [1 Mark: Method].\n\n"
        f"**Step 2:** Ascending order:\n\n"
        f"$$\\mathbf{{{ans_str}}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_wn_05_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": ans_str,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "05_ordering_six_digit_numbers_ascending",
        "hints": {
            "tier_1": "Compare the hundreds, tens, and units since thousands are equal.",
            "tier_2": "Arrange from smallest to largest.",
            "tier_3": f"Ascending order: {ans_str}."
        }
    }


def arch_06_ordering_six_digit_numbers_descending(rng: random.Random) -> Dict[str, Any]:
    lead = rng.randint(5, 8) * 100000
    nums = [lead + rng.randint(1000, 95000) for _ in range(4)]
    nums = list(set(nums))
    while len(nums) < 4:
        nums.append(lead + rng.randint(1000, 95000))
    rng.shuffle(nums)
    s_nums = sorted(nums, reverse=True)
    raw_str = ", ".join(f"{x:,}".replace(",", " ") for x in nums)
    ans_str = "; ".join(f"{x:,}".replace(",", " ") for x in s_nums)

    prompt = (
        f"Arrange the following four numbers in **descending order** (from biggest to smallest):\n\n"
        f"$$\\{{ {raw_str} \\}}$$"
    )
    sol = (
        f"**Step 1:** Compare the ten thousands and thousands digits to identify the greatest number [1 Mark: Method].\n\n"
        f"**Step 2:** Descending order:\n\n"
        f"$$\\mathbf{{{ans_str}}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_wn_06_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": ans_str,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "06_ordering_six_digit_numbers_descending",
        "hints": {
            "tier_1": "Descending means largest to smallest.",
            "tier_2": "Look at the digits in the ten thousands and thousands places.",
            "tier_3": f"Descending sequence: {ans_str}."
        }
    }


def arch_07_comparing_six_digit_numbers_inequality(rng: random.Random) -> Dict[str, Any]:
    base = rng.randint(300, 800) * 1000
    n1 = base + rng.randint(100, 890)
    n2 = base + rng.randint(100, 890)
    while n1 == n2:
        n2 = base + rng.randint(100, 890)

    sym = "<" if n1 < n2 else ">"
    s1 = f"{n1:,}".replace(",", " ")
    s2 = f"{n2:,}".replace(",", " ")

    prompt = (
        f"Insert the correct inequality symbol ($<$ or $>$) to compare the two whole numbers:\n\n"
        f"$${s1} \\quad [\\; ? \\;] \\quad {s2}$$\n\n"
        f"Justify your choice using place value comparison."
    )
    sol = (
        f"**Step 1:** Both numbers share identical hundred-thousands and ten-thousands digits.\n\n"
        f"Comparing the subsequent digits establishes ${s1} {sym} {s2}$ [1 Mark: Method].\n\n"
        f"**Step 2:** Mathematical statement:\n\n"
        f"$$\\mathbf{{{s1} {sym} {s2}}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_wn_07_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{s1} {sym} {s2}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "07_comparing_six_digit_numbers_inequality",
        "hints": {
            "tier_1": "Compare the digits from left to right.",
            "tier_2": f"{s1} is {'smaller' if n1 < n2 else 'greater'} than {s2}.",
            "tier_3": f"Correct statement: {s1} {sym} {s2}."
        }
    }


def arch_08_rounding_to_nearest_ten_hundred_thousand(rng: random.Random) -> Dict[str, Any]:
    num = rng.randint(14250, 89750)
    r_10 = round(num / 10) * 10
    r_100 = round(num / 100) * 100
    r_1000 = round(num / 1000) * 1000

    num_str = f"{num:,}".replace(",", " ")
    prompt = (
        f"Round off the whole number **{num_str}** to:\n\n"
        f"1. The nearest $10$\n"
        f"2. The nearest $100$\n"
        f"3. The nearest $1\\ 000$"
    )
    sol = (
        f"**Step 1:** Look at the digit immediately to the right of the target rounding position (if $\\ge 5$, round up; if $< 5$, round down).\n\n"
        f"- Nearest $10$: **{r_10:,}** [1 Mark: Method]\n"
        f"- Nearest $100$: **{r_100:,}**\n"
        f"- Nearest $1\\ 000$: **{r_1000:,}** [1 Mark: Accuracy]".replace(",", " ")
    )
    ans_str = f"10: {r_10:,}; 100: {r_100:,}; 1000: {r_1000:,}".replace(",", " ")
    return {
        "id": f"g7_wn_08_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": ans_str,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "08_rounding_to_nearest_ten_hundred_thousand",
        "hints": {
            "tier_1": "For 10 look at units; for 100 look at tens; for 1000 look at hundreds.",
            "tier_2": "Digits 0-4 round down; digits 5-9 round up.",
            "tier_3": f"Rounded: nearest 10 = {r_10:,}, 100 = {r_100:,}, 1000 = {r_1000:,}.".replace(",", " ")
        }
    }


# ==============================================================================
# CLUSTER 2: Multiples, Factors & Divisibility (09 - 18)
# ==============================================================================

def arch_09_listing_multiples_within_interval(rng: random.Random) -> Dict[str, Any]:
    n = rng.choice([6, 7, 8, 9, 12])
    low = rng.randint(2, 5) * n + rng.randint(1, 3)
    high = low + rng.randint(3, 5) * n + rng.randint(1, 3)

    mults = [x for x in range(low, high + 1) if x % n == 0]
    ans_str = ", ".join(str(m) for m in mults)

    prompt = (
        f"List all the multiples of **{n}** that lie strictly between **{low}** and **{high}**."
    )
    sol = (
        f"**Step 1:** Generate multiples of ${n}$: ${n} \\times k$ [1 Mark: Method].\n\n"
        f"**Step 2:** Filter those within range $[{low}, {high}]$:\n\n"
        f"$$\\mathbf{{{ans_str}}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_wn_09_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": ans_str,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "09_listing_multiples_within_interval",
        "hints": {
            "tier_1": f"Find the first multiple of {n} greater than {low}.",
            "tier_2": f"Add {n} repeatedly until exceeding {high}.",
            "tier_3": f"Multiples: {ans_str}."
        }
    }


def arch_10_lowest_common_multiple_two_numbers(rng: random.Random) -> Dict[str, Any]:
    pairs = [(6, 8, 24), (8, 12, 24), (9, 12, 36), (12, 15, 60), (10, 15, 30), (14, 21, 42), (15, 20, 60)]
    a, b, lcm_val = rng.choice(pairs)

    prompt = f"Find the Lowest Common Multiple (LCM) of **{a}** and **{b}**."
    sol = (
        f"**Step 1:** List multiples or use prime factorisation:\n\n"
        f"- Multiples of ${a}$: ${', '.join(str(a*i) for i in range(1, 6))}, \\dots$\n"
        f"- Multiples of ${b}$: ${', '.join(str(b*i) for i in range(1, 5))}, \\dots$ [1 Mark: Method]\n\n"
        f"**Step 2:** The smallest multiple common to both is **{lcm_val}**:\n\n"
        f"$$\\mathbf{{\\text{{LCM}}({a}, {b}) = {lcm_val}}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_wn_10_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{lcm_val}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "10_lowest_common_multiple_two_numbers",
        "hints": {
            "tier_1": f"List the multiples of {a} and {b} until you find the first match.",
            "tier_2": f"Common multiples include {lcm_val}, {lcm_val*2}...",
            "tier_3": f"LCM({a}, {b}) = {lcm_val}."
        }
    }


def arch_11_lowest_common_multiple_three_numbers(rng: random.Random) -> Dict[str, Any]:
    triplets = [(4, 6, 8, 24), (3, 5, 6, 30), (4, 6, 10, 60), (6, 9, 12, 36), (5, 10, 15, 30)]
    a, b, c, lcm_val = rng.choice(triplets)

    prompt = f"Determine the Lowest Common Multiple (LCM) of **{a}**, **{b}**, and **{c}**."
    sol = (
        f"**Step 1:** Find prime factors of each number:\n\n"
        f"Take the highest power of each prime factor present [1 Mark: Method].\n\n"
        f"**Step 2:** Compute LCM:\n\n"
        f"$$\\mathbf{{\\text{{LCM}}({a}, {b}, {c}) = {lcm_val}}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_wn_11_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{lcm_val}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "11_lowest_common_multiple_three_numbers",
        "hints": {
            "tier_1": "Find the smallest number that all three numbers divide into evenly.",
            "tier_2": f"Multiples of {c} that are also divisible by {a} and {b}.",
            "tier_3": f"LCM = {lcm_val}."
        }
    }


def arch_12_listing_all_factors_of_number(rng: random.Random) -> Dict[str, Any]:
    nums = [36, 48, 60, 72, 84, 90]
    n = rng.choice(nums)
    factors = sorted([x for x in range(1, n + 1) if n % x == 0])
    ans_str = ", ".join(str(f) for f in factors)

    prompt = f"List all the factors of the number **{n}** in ascending order."
    sol = (
        f"**Step 1:** Find factor pairs $(a \\times b = {n})$ [1 Mark: Method].\n\n"
        f"**Step 2:** Ascending list of all divisors:\n\n"
        f"$$\\mathbf{{{ans_str}}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_wn_12_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": ans_str,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "12_listing_all_factors_of_number",
        "hints": {
            "tier_1": f"Pair up numbers that multiply to give {n} (e.g. 1 and {n}).",
            "tier_2": f"Check integers 1, 2, 3, 4, 5, 6...",
            "tier_3": f"Factors: {ans_str}."
        }
    }


def arch_13_highest_common_factor_two_numbers(rng: random.Random) -> Dict[str, Any]:
    pairs = [(24, 36, 12), (30, 45, 15), (48, 72, 24), (56, 84, 28), (40, 60, 20), (36, 54, 18)]
    a, b, hcf_val = rng.choice(pairs)

    prompt = f"Calculate the Highest Common Factor (HCF) of **{a}** and **{b}**."
    sol = (
        f"**Step 1:** List factors or prime factors of each number:\n\n"
        f"- Factors of ${a}$: common with ${b}$ [1 Mark: Method]\n\n"
        f"**Step 2:** The largest shared divisor is **{hcf_val}**:\n\n"
        f"$$\\mathbf{{\\text{{HCF}}({a}, {b}) = {hcf_val}}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_wn_13_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{hcf_val}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "13_highest_common_factor_two_numbers",
        "hints": {
            "tier_1": "Find the largest number that divides both without a remainder.",
            "tier_2": f"Both numbers are divisible by {hcf_val}.",
            "tier_3": f"HCF({a}, {b}) = {hcf_val}."
        }
    }


def arch_14_highest_common_factor_three_numbers(rng: random.Random) -> Dict[str, Any]:
    triplets = [(24, 36, 60, 12), (18, 27, 45, 9), (30, 45, 75, 15), (32, 48, 80, 16), (20, 40, 60, 20)]
    a, b, c, hcf_val = rng.choice(triplets)

    prompt = f"Find the Highest Common Factor (HCF) of the three numbers: **{a}**, **{b}**, and **{c}**."
    sol = (
        f"**Step 1:** Determine the common prime factors shared by all three numbers [1 Mark: Method].\n\n"
        f"**Step 2:** Multiply the shared prime factors:\n\n"
        f"$$\\mathbf{{\\text{{HCF}}({a}, {b}, {c}) = {hcf_val}}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_wn_14_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{hcf_val}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "14_highest_common_factor_three_numbers",
        "hints": {
            "tier_1": "Find common divisors of all three numbers.",
            "tier_2": f"The largest factor shared by {a}, {b}, and {c} is {hcf_val}.",
            "tier_3": f"HCF = {hcf_val}."
        }
    }


def arch_15_divisibility_rule_check_2_3_5(rng: random.Random) -> Dict[str, Any]:
    num = rng.choice([4320, 2475, 3816, 5140, 6735, 8292])
    d2 = (num % 2 == 0)
    d3 = (num % 3 == 0)
    d5 = (num % 5 == 0)

    sum_digits = sum(int(c) for c in str(num))
    prompt = (
        f"Apply divisibility rules to the number **{num}**:\n\n"
        f"1. Is it divisible by **2**? (State reason)\n"
        f"2. Is it divisible by **3**? (State reason using sum of digits)\n"
        f"3. Is it divisible by **5**? (State reason)"
    )
    sol = (
        f"**Step 1:** Divisibility checks:\n\n"
        f"- By 2: {'Yes' if d2 else 'No'}, last digit is {str(num)[-1]} ({'even' if d2 else 'odd'}) [1 Mark: Method]\n"
        f"- By 3: {'Yes' if d3 else 'No'}, sum of digits is ${' + '.join(str(num))} = {sum_digits}$ which is {'divisible' if d3 else 'not divisible'} by 3\n"
        f"- By 5: {'Yes' if d5 else 'No'}, ends in {str(num)[-1]} [1 Mark: Accuracy]\n\n"
        f"$$\\therefore \\text{{Divisible by 2: {d2}; 3: {d3}; 5: {d5}}}$$"
    )
    return {
        "id": f"g7_wn_15_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"2: {d2}; 3: {d3}; 5: {d5}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "15_divisibility_rule_check_2_3_5",
        "hints": {
            "tier_1": "2: ends in even digit; 3: sum of digits is multiple of 3; 5: ends in 0 or 5.",
            "tier_2": f"Sum of digits is {sum_digits}.",
            "tier_3": f"Divisible by 2: {d2}, 3: {d3}, 5: {d5}."
        }
    }


def arch_16_divisibility_rule_check_6_9_10(rng: random.Random) -> Dict[str, Any]:
    num = rng.choice([3240, 5670, 7830, 4518, 9180])
    d6 = (num % 6 == 0)
    d9 = (num % 9 == 0)
    d10 = (num % 10 == 0)

    prompt = (
        f"Test the number **{num}** for divisibility by **6**, **9**, and **10** using mathematical rules."
    )
    sol = (
        f"**Step 1:** Rules:\n\n"
        f"- By 6: Divisible by both 2 and 3 $\\rightarrow$ **{'Yes' if d6 else 'No'}** [1 Mark: Method]\n"
        f"- By 9: Sum of digits ({sum(int(c) for c in str(num))}) is multiple of 9 $\\rightarrow$ **{'Yes' if d9 else 'No'}**\n"
        f"- By 10: Ends in 0 $\\rightarrow$ **{'Yes' if d10 else 'No'}** [1 Mark: Accuracy]\n\n"
        f"$$\\therefore \\text{{Divisible by 6: {d6}; 9: {d9}; 10: {d10}}}$$"
    )
    return {
        "id": f"g7_wn_16_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"6: {d6}; 9: {d9}; 10: {d10}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "16_divisibility_rule_check_6_9_10",
        "hints": {
            "tier_1": "6: divisible by 2 and 3; 9: sum of digits divisible by 9; 10: ends in 0.",
            "tier_2": f"Sum of digits = {sum(int(c) for c in str(num))}.",
            "tier_3": f"6: {d6}, 9: {d9}, 10: {d10}."
        }
    }


def arch_17_identifying_prime_vs_composite_numbers(rng: random.Random) -> Dict[str, Any]:
    cand = rng.choice([(29, True), (37, True), (41, True), (51, False), (57, False), (67, True), (87, False), (91, False)])
    n, is_prime = cand
    factors = [x for x in range(1, n + 1) if n % x == 0]

    prompt = (
        f"Classify the number **{n}** as either **Prime** or **Composite**.\n\n"
        f"Justify your answer by stating all its factors."
    )
    type_str = "Prime" if is_prime else "Composite"
    sol = (
        f"**Step 1:** Determine the factors of ${n}$: $\\{{{', '.join(str(f) for f in factors)}\\}}$ [1 Mark: Method].\n\n"
        f"**Step 2:** A prime number has exactly two distinct factors (1 and itself). "
        f"Because ${n}$ has {len(factors)} factor(s), it is **{type_str}** [1 Mark: Accuracy].\n\n"
        f"$$\\therefore \\mathbf{{{type_str}}}$$"
    )
    return {
        "id": f"g7_wn_17_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{type_str} (Factors: {', '.join(str(f) for f in factors)})",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "17_identifying_prime_vs_composite_numbers",
        "hints": {
            "tier_1": "Prime numbers have exactly two factors: 1 and the number itself.",
            "tier_2": f"Factors of {n}: {', '.join(str(f) for f in factors)}.",
            "tier_3": f"{n} is {type_str}."
        }
    }


def arch_18_prime_numbers_in_range(rng: random.Random) -> Dict[str, Any]:
    ranges = [(10, 30, [11, 13, 17, 19, 23, 29]), (30, 50, [31, 37, 41, 43, 47]), (50, 70, [53, 59, 61, 67])]
    low, high, primes = rng.choice(ranges)
    ans_str = ", ".join(str(p) for p in primes)

    prompt = f"List all the prime numbers that lie between **{low}** and **{high}**."
    sol = (
        f"**Step 1:** Eliminate even numbers and multiples of 3, 5, etc. [1 Mark: Method].\n\n"
        f"**Step 2:** Primes in range:\n\n"
        f"$$\\mathbf{{{ans_str}}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_wn_18_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": ans_str,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "18_prime_numbers_in_range",
        "hints": {
            "tier_1": "Check odd numbers between the benchmarks.",
            "tier_2": f"Test divisibility by 3, 5, 7 for numbers between {low} and {high}.",
            "tier_3": f"Primes: {ans_str}."
        }
    }


# ==============================================================================
# CLUSTER 3: Prime Factorisation (19 - 24)
# ==============================================================================

def arch_19_prime_factorisation_factor_tree(rng: random.Random) -> Dict[str, Any]:
    cases = [(24, "2^3 × 3", "2 × 2 × 2 × 3"), (36, "2^2 × 3^2", "2 × 2 × 3 × 3"), (40, "2^3 × 5", "2 × 2 × 2 × 5"), (48, "2^4 × 3", "2 × 2 × 2 × 2 × 3"), (60, "2^2 × 3 × 5", "2 × 2 × 3 × 5")]
    n, exp_form, prod_form = rng.choice(cases)

    prompt = (
        f"Use a factor tree to find the prime factorisation of **{n}**.\n\n"
        f"Write your final answer as a product of prime factors."
    )
    sol = (
        f"**Step 1:** Branch into factors until only prime numbers remain at the leaves [1 Mark: Method].\n\n"
        f"**Step 2:** Product of primes:\n\n"
        f"$${n} = {prod_form} = \\mathbf{{{exp_form}}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_wn_19_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": prod_form,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "19_prime_factorisation_factor_tree",
        "hints": {
            "tier_1": "Divide by the smallest prime (2, 3, 5...) repeatedly.",
            "tier_2": f"Keep factoring until all branches terminate in prime numbers.",
            "tier_3": f"{n} = {prod_form}."
        }
    }


def arch_20_prime_factorisation_ladder_division_method(rng: random.Random) -> Dict[str, Any]:
    cases = [(72, "2^3 × 3^2"), (84, "2^2 × 3 × 7"), (90, "2 × 3^2 × 5"), (108, "2^2 × 3^3"), (120, "2^3 × 3 × 5")]
    n, exp_form = rng.choice(cases)

    prompt = (
        f"Using the division ladder method, express **{n}** as a product of its prime factors in exponential notation."
    )
    sol = (
        f"**Step 1:** Successively divide by prime factors ($2, 3, 5, \\dots$) down to $1$ [1 Mark: Method].\n\n"
        f"**Step 2:** Group identical prime factors into powers:\n\n"
        f"$$\\mathbf{{{n} = {exp_form}}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_wn_20_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{exp_form}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "20_prime_factorisation_ladder_division_method",
        "hints": {
            "tier_1": "Divide repeatedly by prime numbers: 2, 3, 5...",
            "tier_2": "Count how many times each prime factor appears.",
            "tier_3": f"{n} = {exp_form}."
        }
    }


def arch_21_prime_factors_in_exponential_form(rng: random.Random) -> Dict[str, Any]:
    cases = [(144, "2^4 × 3^2"), (180, "2^2 × 3^2 × 5"), (200, "2^3 × 5^2"), (225, "3^2 × 5^2")]
    n, ans = rng.choice(cases)

    prompt = f"Express **{n}** as a product of prime factors in exponential form."
    sol = (
        f"**Step 1:** Break into prime factors [1 Mark: Method].\n\n"
        f"**Step 2:** Write with powers:\n\n"
        f"$$\\mathbf{{{n} = {ans}}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_wn_21_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": ans,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "21_prime_factors_in_exponential_form",
        "hints": {
            "tier_1": "Find all prime factors.",
            "tier_2": "Write repeated prime factors using exponent powers.",
            "tier_3": f"{n} = {ans}."
        }
    }


def arch_22_hcf_from_prime_factorisations(rng: random.Random) -> Dict[str, Any]:
    # 72 = 2^3 * 3^2, 108 = 2^2 * 3^3 -> HCF = 2^2 * 3^2 = 36
    a, p_a = 72, "2^3 \\times 3^2"
    b, p_b = 108, "2^2 \\times 3^3"
    hcf_val = 36

    prompt = (
        f"Given the prime factorisations:\n\n"
        f"$${a} = {p_a}$$\n"
        f"$${b} = {p_b}$$\n\n"
        f"Calculate the Highest Common Factor (HCF) of **{a}** and **{b}**."
    )
    sol = (
        f"**Step 1:** Take the lowest power of each common prime factor:\n\n"
        f"$$\\text{{HCF}} = 2^2 \\times 3^2 \\text{{ [1 Mark: Method]}}$$\n\n"
        f"**Step 2:** Calculate product:\n\n"
        f"$$4 \\times 9 = \\mathbf{{{hcf_val}}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_wn_22_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{hcf_val}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "22_hcf_from_prime_factorisations",
        "hints": {
            "tier_1": "For HCF, take the smallest power of each shared prime factor.",
            "tier_2": "2^2 × 3^2 = 4 × 9.",
            "tier_3": f"HCF = {hcf_val}."
        }
    }


def arch_23_lcm_from_prime_factorisations(rng: random.Random) -> Dict[str, Any]:
    a, p_a = 18, "2 \\times 3^2"
    b, p_b = 24, "2^3 \\times 3"
    lcm_val = 72

    prompt = (
        f"Given the prime factorisations:\n\n"
        f"$${a} = {p_a}$$\n"
        f"$${b} = {p_b}$$\n\n"
        f"Calculate the Lowest Common Multiple (LCM) of **{a}** and **{b}**."
    )
    sol = (
        f"**Step 1:** Take the highest power of every prime factor present:\n\n"
        f"$$\\text{{LCM}} = 2^3 \\times 3^2 \\text{{ [1 Mark: Method]}}$$\n\n"
        f"**Step 2:** Calculate product:\n\n"
        f"$$8 \\times 9 = \\mathbf{{{lcm_val}}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_wn_23_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{lcm_val}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "23_lcm_from_prime_factorisations",
        "hints": {
            "tier_1": "For LCM, take the largest power of each prime factor.",
            "tier_2": "2^3 × 3^2 = 8 × 9.",
            "tier_3": f"LCM = {lcm_val}."
        }
    }


def arch_24_square_root_using_prime_factors(rng: random.Random) -> Dict[str, Any]:
    cases = [(144, "2^4 \\times 3^2", 12), (324, "2^2 \\times 3^4", 18), (400, "2^4 \\times 5^2", 20), (900, "2^2 \\times 3^2 \\times 5^2", 30)]
    n, prime_exp, sqrt_val = rng.choice(cases)

    prompt = (
        f"Use prime factorisation to determine the value of: $$\\sqrt{{{n}}}$$\n\n"
        f"Show all steps."
    )
    sol = (
        f"**Step 1:** Express ${n}$ in prime factors: ${n} = {prime_exp}$ [1 Mark: Method].\n\n"
        f"**Step 2:** Halve all exponents under square root:\n\n"
        f"$$\\sqrt{{{n}}} = \\mathbf{{{sqrt_val}}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_wn_24_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{sqrt_val}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "24_square_root_using_prime_factors",
        "hints": {
            "tier_1": "Find the prime factors and group them into pairs.",
            "tier_2": "Halve each exponent to find the square root.",
            "tier_3": f"sqrt({n}) = {sqrt_val}."
        }
    }


# ==============================================================================
# CLUSTER 4: Addition and Subtraction Operations (25)
# ==============================================================================

def arch_25_column_addition_five_digit_numbers(rng: random.Random) -> Dict[str, Any]:
    n1 = rng.randint(24000, 68000)
    n2 = rng.randint(15000, 31000)
    tot = n1 + n2

    s1 = f"{n1:,}".replace(",", " ")
    s2 = f"{n2:,}".replace(",", " ")
    tot_s = f"{tot:,}".replace(",", " ")

    prompt = f"Calculate the sum using vertical column addition: $${s1} + {s2}$$"
    sol = (
        f"**Step 1:** Align columns by place value and add with carrying [1 Mark: Method].\n\n"
        f"**Step 2:** Sum:\n\n"
        f"$$\\mathbf{{{tot_s}}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_wn_25_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": tot_s,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "25_column_addition_five_digit_numbers",
        "hints": {
            "tier_1": "Add units first, then tens, carrying forward tens as needed.",
            "tier_2": f"{s1} + {s2}.",
            "tier_3": f"Sum = {tot_s}."
        }
    }
