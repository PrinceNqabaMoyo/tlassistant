"""
Grade 8 Mathematics - Common Fractions Archetypes (01 to 25).
100% CAPS-aligned deterministic question generator.
Adheres strictly to the 6-Pillar Generator Contract and Zero-Meta-Curriculum Invariant.
Grounded in curriculum_docs/Mathematics_Gr8/Numbers-Operations-and-Relationships Studio.md (Term 3 Common Fractions).
"""
from __future__ import annotations

import math
import random
from typing import Any, Callable, Dict, List, Optional


# ----------------------------------------------------------------------
# 01. Simplifying Fraction HCF
# ----------------------------------------------------------------------
def arch_01_simplifying_fraction_hcf(rng: random.Random) -> Dict[str, Any]:
    common = rng.choice([3, 4, 6, 8, 12, 15])
    num_simp = rng.choice([2, 3, 5, 7])
    den_simp = rng.choice([9, 11, 13, 16, 17])
    while math.gcd(num_simp, den_simp) != 1:
        den_simp += 1
    num = num_simp * common
    den = den_simp * common

    prompt = (
        f"Simplify the common fraction to its simplest form (lowest terms):\n"
        f"\\[ \\frac{{{num}}}{{{den}}} \\]"
    )
    sol = (
        f"**Step 1:** Find the Highest Common Factor (HCF) of **{num}** and **{den}**.\n"
        f"\\(\\text{{HCF}}({num}; {den}) = {common}\\).\n\n"
        f"**Step 2:** Divide both the numerator and the denominator by {common}:\n"
        f"\\[ \\frac{{{num} \\div {common}}}{{{den} \\div {common}}} = \\frac{{{num_simp}}}{{{den_simp}}} \\]"
    )
    ans = f"{num_simp}/{den_simp}"
    return {
        "id": f"g8_frac_simp_{rng.randint(100000, 999999)}",
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
        "subskill": "01_simplifying_fraction_hcf",
        "learning_objective_id": "math_g8_frac_simplifying",
        "hints": {
            "tier_1": f"Find the greatest number that divides into both {num} and {den}.",
            "tier_2": f"The HCF is {common}.",
            "tier_3": f"{num_simp}/{den_simp}.",
        },
        "misconception_tags": ["dividing_only_numerator_by_factor"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 02. Equivalent Fractions Missing Numerator
# ----------------------------------------------------------------------
def arch_02_equivalent_fractions_missing_numerator(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([3, 5, 7, 9])
    b = rng.choice([4, 6, 8, 10, 12])
    while math.gcd(a, b) != 1:
        b += 1
    k = rng.choice([3, 4, 5, 6])
    d = b * k
    x = a * k

    prompt = (
        f"Find the value of \\(x\\) that makes the fractions equivalent:\n"
        f"\\[ \\frac{{{a}}}{{{b}}} = \\frac{{x}}{{{d}}} \\]"
    )
    sol = (
        f"**Step 1:** Determine the scaling factor between the denominators:\n"
        f"\\[ {d} \\div {b} = {k} \\]\n\n"
        f"**Step 2:** Multiply the numerator by the same scaling factor:\n"
        f"\\[ x = {a} \\times {k} = {x} \\]"
    )
    ans = str(x)
    return {
        "id": f"g8_frac_equiv_num_{rng.randint(100000, 999999)}",
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
        "subskill": "02_equivalent_fractions_missing_numerator",
        "learning_objective_id": "math_g8_frac_equivalent_num",
        "hints": {
            "tier_1": f"By what factor was the denominator {b} multiplied to get {d}?",
            "tier_2": f"{b} × {k} = {d}.",
            "tier_3": f"x = {a} × {k} = {x}.",
        },
        "misconception_tags": ["adding_difference_instead_of_multiplying"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 03. Equivalent Fractions Missing Denominator
# ----------------------------------------------------------------------
def arch_03_equivalent_fractions_missing_denominator(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([2, 4, 5, 7])
    b = rng.choice([3, 7, 9, 11])
    while math.gcd(a, b) != 1:
        b += 1
    k = rng.choice([3, 4, 6])
    c = a * k
    x = b * k

    prompt = (
        f"Find the value of \\(y\\) that makes the fractions equivalent:\n"
        f"\\[ \\frac{{{a}}}{{{b}}} = \\frac{{{c}}}{{y}} \\]"
    )
    sol = (
        f"**Step 1:** Determine the multiplier for the numerators:\n"
        f"\\[ {c} \\div {a} = {k} \\]\n\n"
        f"**Step 2:** Multiply the denominator by the same factor:\n"
        f"\\[ y = {b} \\times {k} = {x} \\]"
    )
    ans = str(x)
    return {
        "id": f"g8_frac_equiv_den_{rng.randint(100000, 999999)}",
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
        "subskill": "03_equivalent_fractions_missing_denominator",
        "learning_objective_id": "math_g8_frac_equivalent_den",
        "hints": {
            "tier_1": f"Find {c} ÷ {a}.",
            "tier_2": f"The multiplier is {k}.",
            "tier_3": f"y = {b} × {k} = {x}.",
        },
        "misconception_tags": ["adding_difference_instead_of_multiplying"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 04. Converting Improper Fraction To Mixed Number
# ----------------------------------------------------------------------
def arch_04_converting_improper_fraction_to_mixed_number(rng: random.Random) -> Dict[str, Any]:
    d = rng.choice([3, 4, 5, 6, 7, 8])
    whole = rng.choice([3, 4, 5, 7])
    rem = rng.choice(range(1, d))
    num = whole * d + rem

    prompt = (
        f"Convert the improper fraction into a mixed number in simplest form:\n"
        f"\\[ \\frac{{{num}}}{{{d}}} \\]"
    )
    sol = (
        f"**Step 1:** Divide the numerator by the denominator:\n"
        f"\\[ {num} \\div {d} = {whole} \\text{{ with a remainder of }} {rem} \\]\n\n"
        f"**Step 2:** Write as a mixed number \\(W \\frac{{R}}{{D}}\\):\n"
        f"\\[ \\frac{{{num}}}{{{d}}} = {whole} \\frac{{{rem}}}{{{d}}} \\]"
    )
    ans = f"{whole} {rem}/{d}"
    return {
        "id": f"g8_frac_imp_mix_{rng.randint(100000, 999999)}",
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
        "subskill": "04_converting_improper_fraction_to_mixed_number",
        "learning_objective_id": "math_g8_frac_improper_to_mixed",
        "hints": {
            "tier_1": f"Divide {num} by {d} to find the whole number.",
            "tier_2": f"{num} = ({whole} × {d}) + {rem}.",
            "tier_3": f"{whole} {rem}/{d}.",
        },
        "misconception_tags": ["writing_remainder_as_whole_number"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 05. Converting Mixed Number To Improper Fraction
# ----------------------------------------------------------------------
def arch_05_converting_mixed_number_to_improper_fraction(rng: random.Random) -> Dict[str, Any]:
    d = rng.choice([4, 5, 6, 7, 9])
    whole = rng.choice([2, 3, 5, 6])
    rem = rng.choice(range(1, d))
    num = whole * d + rem

    prompt = (
        f"Convert the mixed number into an improper fraction:\n"
        f"\\[ {whole} \\frac{{{rem}}}{{{d}}} \\]"
    )
    sol = (
        f"**Step 1:** Multiply the whole number by the denominator:\n"
        f"\\[ {whole} \\times {d} = {whole * d} \\]\n\n"
        f"**Step 2:** Add the numerator:\n"
        f"\\[ {whole * d} + {rem} = {num} \\]\n\n"
        f"**Step 3:** Place over the original denominator:\n"
        f"\\[ {whole} \\frac{{{rem}}}{{{d}}} = \\frac{{{num}}}{{{d}}} \\]"
    )
    ans = f"{num}/{d}"
    return {
        "id": f"g8_frac_mix_imp_{rng.randint(100000, 999999)}",
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
        "subskill": "05_converting_mixed_number_to_improper_fraction",
        "learning_objective_id": "math_g8_frac_mixed_to_improper",
        "hints": {
            "tier_1": f"Numerator = (Whole × Denominator) + Numerator.",
            "tier_2": f"({whole} × {d}) + {rem} = {num}.",
            "tier_3": f"{num}/{d}.",
        },
        "misconception_tags": ["adding_whole_to_numerator_without_multiplying"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 06. Comparing Fractions Common Denominator
# ----------------------------------------------------------------------
def arch_06_comparing_fractions_common_denominator(rng: random.Random) -> Dict[str, Any]:
    b = rng.choice([3, 4, 5])
    d = rng.choice([6, 7, 8])
    if b == d:
        d = b + 1
    a = rng.choice(range(1, b))
    c = rng.choice(range(1, d))
    lcm = math.lcm(b, d)
    val_a = a * (lcm // b)
    val_c = c * (lcm // d)
    if val_a == val_c:
        a += 1
        val_a = a * (lcm // b)

    symbol = ">" if val_a > val_c else "<"
    larger = f"{a}/{b}" if val_a > val_c else f"{c}/{d}"

    prompt = (
        f"Compare the two fractions by converting them to equivalent fractions with a common denominator. "
        f"Insert \\(>\\), \\(<\\), or \\(=\\):\n"
        f"\\[ \\frac{{{a}}}{{{b}}} \\quad \\square \\quad \\frac{{{c}}}{{{d}}} \\]"
    )
    sol = (
        f"**Step 1:** Find the Lowest Common Denominator (LCD) of {b} and {d}:\n"
        f"\\[ \\text{{LCD}}({b}; {d}) = {lcm} \\]\n\n"
        f"**Step 2:** Convert both fractions to have denominator {lcm}:\n"
        f"\\[ \\frac{{{a}}}{{{b}}} = \\frac{{{a} \\times {lcm // b}}}{{{lcm}}} = \\frac{{{val_a}}}{{{lcm}}} \\]\n"
        f"\\[ \\frac{{{c}}}{{{d}}} = \\frac{{{c} \\times {lcm // d}}}{{{lcm}}} = \\frac{{{val_c}}}{{{lcm}}} \\]\n\n"
        f"**Step 3:** Compare numerators:\n"
        f"Since \\({val_a} {symbol} {val_c}\\), we have \\(\\frac{{{a}}}{{{b}}} {symbol} \\frac{{{c}}}{{{d}}}\\)."
    )
    ans = f"{a}/{b} {symbol} {c}/{d}"
    return {
        "id": f"g8_frac_compare_{rng.randint(100000, 999999)}",
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
        "subskill": "06_comparing_fractions_common_denominator",
        "learning_objective_id": "math_g8_frac_comparing",
        "hints": {
            "tier_1": f"The LCD of {b} and {d} is {lcm}.",
            "tier_2": f"{val_a}/{lcm} versus {val_c}/{lcm}.",
            "tier_3": f"{symbol}.",
        },
        "misconception_tags": ["assuming_larger_denominator_means_larger_fraction"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 07. Ordering Three Fractions Ascending
# ----------------------------------------------------------------------
def arch_07_ordering_three_fractions_ascending(rng: random.Random) -> Dict[str, Any]:
    dens = [2, 3, 4] if rng.choice([True, False]) else [3, 4, 6]
    lcm = math.lcm(dens[0], math.lcm(dens[1], dens[2]))
    # choose distinct numerators
    nums = [1, 2, 3]
    # compute values:
    fracs = [
        (1, dens[0], 1 * (lcm // dens[0])),
        (2, dens[1], 2 * (lcm // dens[1])),
        (1, dens[2], 1 * (lcm // dens[2])),
    ]
    # sort by value
    fracs_sorted = sorted(fracs, key=lambda x: x[2])
    # ensure strictly distinct values
    if fracs_sorted[0][2] == fracs_sorted[1][2] or fracs_sorted[1][2] == fracs_sorted[2][2]:
        fracs_sorted = [(1, 4, 3), (1, 2, 6), (2, 3, 8)]

    orig_str = f"\\frac{{{fracs[0][0]}}}{{{fracs[0][1]}}}, \\quad \\frac{{{fracs[1][0]}}}{{{fracs[1][1]}}}, \\quad \\frac{{{fracs[2][0]}}}{{{fracs[2][1]}}}"
    sorted_str = ", ".join(f"{f[0]}/{f[1]}" for f in fracs_sorted)

    prompt = (
        f"Arrange the following fractions in ascending order (smallest to largest) by converting them to equivalent fractions with a common denominator:\n"
        f"\\[ {orig_str} \\]"
    )
    sol = (
        f"**Step 1:** Find the LCD of the denominators \\({dens}\\), which is **{lcm}**.\n\n"
        f"**Step 2:** Convert each fraction to denominator {lcm}:\n" +
        "\n".join(f"\\[ \\frac{{{f[0]}}}{{{f[1]}}} = \\frac{{{f[2]}}}{{{lcm}}} \\]" for f in fracs) +
        f"\n\n**Step 3:** Order from smallest to largest numerator:\n"
        f"**{sorted_str}**"
    )
    ans = sorted_str
    return {
        "id": f"g8_frac_order_{rng.randint(100000, 999999)}",
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
        "subskill": "07_ordering_three_fractions_ascending",
        "learning_objective_id": "math_g8_frac_ordering_ascending",
        "hints": {
            "tier_1": f"Express all fractions with common denominator {lcm}.",
            "tier_2": f"Compare their new numerators.",
            "tier_3": f"{sorted_str}.",
        },
        "misconception_tags": ["comparing_numerators_without_common_denominator"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 08. Fraction Of Whole Number Quantity
# ----------------------------------------------------------------------
def arch_08_fraction_of_whole_number_quantity(rng: random.Random) -> Dict[str, Any]:
    denom = rng.choice([4, 5, 6, 8, 10])
    num = rng.choice(range(1, denom))
    while math.gcd(num, denom) != 1:
        num = (num + 1) % denom or 1
    mult = rng.choice([15, 20, 25, 30, 40])
    total_amount = denom * mult
    result = num * mult

    prompt = (
        f"Calculate the value of:\n"
        f"\\[ \\frac{{{num}}}{{{denom}}} \\text{{ of R}}{total_amount} \\]"
    )
    sol = (
        f"**Step 1:** Divide the total amount by the denominator to find one unit part:\n"
        f"\\[ R{total_amount} \\div {denom} = R{mult} \\]\n\n"
        f"**Step 2:** Multiply by the numerator:\n"
        f"\\[ R{mult} \\times {num} = R{result} \\]"
    )
    ans = f"R{result}"
    return {
        "id": f"g8_frac_of_qty_{rng.randint(100000, 999999)}",
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
        "subskill": "08_fraction_of_whole_number_quantity",
        "learning_objective_id": "math_g8_frac_of_quantity",
        "hints": {
            "tier_1": f"'Of' means multiply: ({num} ÷ {denom}) × {total_amount}.",
            "tier_2": f"{total_amount} ÷ {denom} = {mult}.",
            "tier_3": f"R{result}.",
        },
        "misconception_tags": ["multiplying_denominator_by_whole_number"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 09. Fraction Of Measurement Unit Conversion
# ----------------------------------------------------------------------
def arch_09_fraction_of_measurement_unit_conversion(rng: random.Random) -> Dict[str, Any]:
    unit_type = rng.choice(["mass", "time", "length"])
    if unit_type == "mass":
        denom = rng.choice([4, 5, 8])
        num = rng.choice([3, 5, 7]) if denom == 8 else rng.choice([2, 3])
        total_conv = 1000  # 1 kg = 1000 g
        ans_val = (1000 // denom) * num
        unit_str = "kg"
        target_unit = "g"
    elif unit_type == "time":
        denom = rng.choice([3, 4, 5, 6])
        num = rng.choice([2, 3, 5]) if denom == 6 else rng.choice([2, 3])
        total_conv = 60  # 1 hour = 60 min
        ans_val = (60 // denom) * num
        unit_str = "hour"
        target_unit = "minutes"
    else:
        denom = rng.choice([4, 5, 10])
        num = rng.choice([3, 4, 7]) if denom == 10 else 3
        total_conv = 1000  # 1 km = 1000 m
        ans_val = (1000 // denom) * num
        unit_str = "km"
        target_unit = "m"

    prompt = (
        f"Calculate the following quantity and state your final answer in **{target_unit}**:\n"
        f"\\[ \\frac{{{num}}}{{{denom}}} \\text{{ of 1 {unit_str}}} \\]"
    )
    sol = (
        f"**Step 1:** Convert 1 {unit_str} into {target_unit}:\n"
        f"\\[ 1 \\text{{ {unit_str}}} = {total_conv} \\text{{ {target_unit}}} \\]\n\n"
        f"**Step 2:** Calculate \\(\\frac{{{num}}}{{{denom}}} \\times {total_conv}\\):\n"
        f"\\[ {total_conv} \\div {denom} = {total_conv // denom} \\]\n"
        f"\\[ {total_conv // denom} \\times {num} = {ans_val} \\text{{ {target_unit}}} \\]"
    )
    ans = f"{ans_val} {target_unit}"
    return {
        "id": f"g8_frac_unit_conv_{rng.randint(100000, 999999)}",
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
        "subskill": "09_fraction_of_measurement_unit_conversion",
        "learning_objective_id": "math_g8_frac_unit_conversion",
        "hints": {
            "tier_1": f"First convert 1 {unit_str} = {total_conv} {target_unit}.",
            "tier_2": f"Find {num}/{denom} of {total_conv}.",
            "tier_3": f"{ans_val} {target_unit}.",
        },
        "misconception_tags": ["forgetting_to_convert_unit_first"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 10. Addition Like Denominators Proper
# ----------------------------------------------------------------------
def arch_10_addition_like_denominators_proper(rng: random.Random) -> Dict[str, Any]:
    d = rng.choice([8, 10, 12, 16])
    a = rng.choice([1, 3, 5])
    b = rng.choice([1, 3, 5])
    sum_num = a + b
    g = math.gcd(sum_num, d)
    num_simp = sum_num // g
    den_simp = d // g

    prompt = (
        f"Calculate and simplify your answer to lowest terms:\n"
        f"\\[ \\frac{{{a}}}{{{d}}} + \\frac{{{b}}}{{{d}}} \\]"
    )
    sol = (
        f"**Step 1:** Since the denominators are identical, add the numerators directly:\n"
        f"\\[ \\frac{{{a} + {b}}}{{{d}}} = \\frac{{{sum_num}}}{{{d}}} \\]\n\n"
        f"**Step 2:** Simplify by dividing by \\(\\text{{HCF}} = {g}\\):\n"
        f"\\[ \\frac{{{sum_num} \\div {g}}}{{{d} \\div {g}}} = \\frac{{{num_simp}}}{{{den_simp}}} \\]"
    )
    ans = f"{num_simp}/{den_simp}"
    return {
        "id": f"g8_frac_add_like_{rng.randint(100000, 999999)}",
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
        "subskill": "10_addition_like_denominators_proper",
        "learning_objective_id": "math_g8_frac_add_like",
        "hints": {
            "tier_1": f"Add the numerators together and keep the denominator {d}.",
            "tier_2": f"{sum_num}/{d}.",
            "tier_3": f"Simplify to {num_simp}/{den_simp}.",
        },
        "misconception_tags": ["adding_denominators_together"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 11. Addition Unlike Denominators Multiples
# ----------------------------------------------------------------------
def arch_11_addition_unlike_denominators_multiples(rng: random.Random) -> Dict[str, Any]:
    b = rng.choice([3, 4, 5, 6])
    k = rng.choice([2, 3])
    d = b * k
    a = rng.choice(range(1, b))
    c = rng.choice(range(1, d))
    num_total = a * k + c
    g = math.gcd(num_total, d)
    ans_num = num_total // g
    ans_den = d // g

    prompt = (
        f"Calculate and write in simplest form:\n"
        f"\\[ \\frac{{{a}}}{{{b}}} + \\frac{{{c}}}{{{d}}} \\]"
    )
    sol = (
        f"**Step 1:** The Lowest Common Denominator (LCD) of {b} and {d} is **{d}**.\n\n"
        f"**Step 2:** Convert \\(\\frac{{{a}}}{{{b}}}\\) to an equivalent fraction with denominator {d}:\n"
        f"\\[ \\frac{{{a} \\times {k}}}{{{b} \\times {k}}} = \\frac{{{a * k}}}{{{d}}} \\]\n\n"
        f"**Step 3:** Add the numerators:\n"
        f"\\[ \\frac{{{a * k} + {c}}}{{{d}}} = \\frac{{{num_total}}}{{{d}}} \\]\n\n"
        f"**Step 4:** Simplify to lowest terms:\n"
        f"\\[ \\frac{{{ans_num}}}{{{ans_den}}} \\]"
    )
    ans = f"{ans_num}/{ans_den}"
    return {
        "id": f"g8_frac_add_mult_{rng.randint(100000, 999999)}",
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
        "subskill": "11_addition_unlike_denominators_multiples",
        "learning_objective_id": "math_g8_frac_add_multiples",
        "hints": {
            "tier_1": f"Notice that {d} is a multiple of {b}.",
            "tier_2": f"Convert {a}/{b} to {a * k}/{d}.",
            "tier_3": f"{ans_num}/{ans_den}.",
        },
        "misconception_tags": ["adding_denominators_instead_of_lcd"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 12. Addition Unlike Denominators Coprime
# ----------------------------------------------------------------------
def arch_12_addition_unlike_denominators_coprime(rng: random.Random) -> Dict[str, Any]:
    b = rng.choice([3, 5, 7])
    d = rng.choice([4, 6, 8])
    while math.gcd(b, d) != 1:
        d += 1
    a = rng.choice(range(1, b))
    c = rng.choice(range(1, d))
    lcm = b * d
    num_total = a * d + c * b
    g = math.gcd(num_total, lcm)
    ans_num = num_total // g
    ans_den = lcm // g

    prompt = (
        f"Calculate and express as a simplified fraction or mixed number:\n"
        f"\\[ \\frac{{{a}}}{{{b}}} + \\frac{{{c}}}{{{d}}} \\]"
    )
    sol = (
        f"**Step 1:** The LCD of {b} and {d} is \\({b} \\times {d} = {lcm}\\).\n\n"
        f"**Step 2:** Convert both fractions to denominator {lcm}:\n"
        f"\\[ \\frac{{{a} \\times {d}}}{{{lcm}}} + \\frac{{{c} \\times {b}}}{{{lcm}}} = \\frac{{{a * d}}}{{{lcm}}} + \\frac{{{c * b}}}{{{lcm}}} \\]\n\n"
        f"**Step 3:** Add numerators:\n"
        f"\\[ \\frac{{{a * d + c * b}}}{{{lcm}}} = \\frac{{{num_total}}}{{{lcm}}} \\]"
    )
    if ans_num >= ans_den:
        w = ans_num // ans_den
        rem = ans_num % ans_den
        ans = f"{w} {rem}/{ans_den}" if rem > 0 else str(w)
    else:
        ans = f"{ans_num}/{ans_den}"
    return {
        "id": f"g8_frac_add_coprime_{rng.randint(100000, 999999)}",
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
        "subskill": "12_addition_unlike_denominators_coprime",
        "learning_objective_id": "math_g8_frac_add_coprime",
        "hints": {
            "tier_1": f"LCD is {b} × {d} = {lcm}.",
            "tier_2": f"({a * d} + {c * b}) / {lcm}.",
            "tier_3": f"{ans}.",
        },
        "misconception_tags": ["adding_across_numerators_and_denominators"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 13. Addition Three Fractions LCD
# ----------------------------------------------------------------------
def arch_13_addition_three_fractions_lcd(rng: random.Random) -> Dict[str, Any]:
    d1, d2, d3 = rng.choice([(2, 3, 4), (2, 4, 8), (3, 4, 6), (2, 3, 6)])
    lcm = math.lcm(d1, math.lcm(d2, d3))
    a = 1
    b = 1
    c = 1
    num_total = a * (lcm // d1) + b * (lcm // d2) + c * (lcm // d3)
    g = math.gcd(num_total, lcm)
    ans_num = num_total // g
    ans_den = lcm // g

    prompt = (
        f"Calculate the sum of the three fractions and simplify:\n"
        f"\\[ \\frac{{{a}}}{{{d1}}} + \\frac{{{b}}}{{{d2}}} + \\frac{{{c}}}{{{d3}}} \\]"
    )
    sol = (
        f"**Step 1:** Find the LCD of **{d1}**, **{d2}**, and **{d3}**, which is **{lcm}**.\n\n"
        f"**Step 2:** Convert all fractions to denominator {lcm}:\n"
        f"\\[ \\frac{{{a * (lcm // d1)}}}{{{lcm}}} + \\frac{{{b * (lcm // d2)}}}{{{lcm}}} + \\frac{{{c * (lcm // d3)}}}{{{lcm}}} \\]\n\n"
        f"**Step 3:** Sum the numerators:\n"
        f"\\[ \\frac{{{a * (lcm // d1)} + {b * (lcm // d2)} + {c * (lcm // d3)}}}{{{lcm}}} = \\frac{{{num_total}}}{{{lcm}}} = \\frac{{{ans_num}}}{{{ans_den}}} \\]"
    )
    ans = f"{ans_num}/{ans_den}"
    return {
        "id": f"g8_frac_add_3_{rng.randint(100000, 999999)}",
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
        "subskill": "13_addition_three_fractions_lcd",
        "learning_objective_id": "math_g8_frac_add_three",
        "hints": {
            "tier_1": f"LCD of {d1}, {d2}, and {d3} is {lcm}.",
            "tier_2": f"Convert all three fractions to have denominator {lcm}.",
            "tier_3": f"{ans_num}/{ans_den}.",
        },
        "misconception_tags": ["adding_denominators_together"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 14. Addition Mixed Numbers Unlike Denominators
# ----------------------------------------------------------------------
def arch_14_addition_mixed_numbers_unlike_denominators(rng: random.Random) -> Dict[str, Any]:
    w1 = rng.choice([2, 3, 4])
    w2 = rng.choice([1, 2, 3])
    b = rng.choice([2, 3, 4])
    d = rng.choice([3, 5])
    if b == d:
        d = 5
    a = 1
    c = 1
    lcm = math.lcm(b, d)
    frac_num = a * (lcm // b) + c * (lcm // d)
    total_w = w1 + w2 + (frac_num // lcm)
    rem_num = frac_num % lcm
    g = math.gcd(rem_num, lcm) if rem_num > 0 else 1
    rem_num //= g
    lcm_simp = lcm // g

    prompt = (
        f"Calculate and write your final answer as a mixed number in simplest form:\n"
        f"\\[ {w1} \\frac{{{a}}}{{{b}}} + {w2} \\frac{{{c}}}{{{d}}} \\]"
    )
    sol = (
        f"**Step 1:** Add the whole numbers:\n"
        f"\\[ {w1} + {w2} = {w1 + w2} \\]\n\n"
        f"**Step 2:** Find the LCD of {b} and {d}, which is **{lcm}**, and add the fractional parts:\n"
        f"\\[ \\frac{{{a}}}{{{b}}} + \\frac{{{c}}}{{{d}}} = \\frac{{{a * (lcm // b)}}}{{{lcm}}} + \\frac{{{c * (lcm // d)}}}{{{lcm}}} = \\frac{{{frac_num}}}{{{lcm}}} \\]\n\n"
        f"**Step 3:** Combine whole and fractional parts:\n"
        f"\\[ {w1 + w2} + \\frac{{{frac_num}}}{{{lcm}}} = {total_w} \\frac{{{rem_num}}}{{{lcm_simp}}} \\]"
    )
    ans = f"{total_w} {rem_num}/{lcm_simp}" if rem_num > 0 else str(total_w)
    return {
        "id": f"g8_frac_add_mix_{rng.randint(100000, 999999)}",
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
        "subskill": "14_addition_mixed_numbers_unlike_denominators",
        "learning_objective_id": "math_g8_frac_add_mixed_numbers",
        "hints": {
            "tier_1": f"Add whole numbers ({w1} + {w2}) and fractions separately.",
            "tier_2": f"Fraction LCD is {lcm}.",
            "tier_3": f"{ans}.",
        },
        "misconception_tags": ["adding_denominators_together"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 15. Subtraction Like Denominators
# ----------------------------------------------------------------------
def arch_15_subtraction_like_denominators(rng: random.Random) -> Dict[str, Any]:
    d = rng.choice([8, 10, 12, 16])
    b = rng.choice([1, 2, 3])
    a = b + rng.choice([2, 4, 6])
    diff_num = a - b
    g = math.gcd(diff_num, d)
    num_simp = diff_num // g
    den_simp = d // g

    prompt = (
        f"Calculate and simplify:\n"
        f"\\[ \\frac{{{a}}}{{{d}}} - \\frac{{{b}}}{{{d}}} \\]"
    )
    sol = (
        f"**Step 1:** Subtract numerators directly over the common denominator:\n"
        f"\\[ \\frac{{{a} - {b}}}{{{d}}} = \\frac{{{diff_num}}}{{{d}}} \\]\n\n"
        f"**Step 2:** Simplify by dividing by \\(\\text{{HCF}} = {g}\\):\n"
        f"\\[ \\frac{{{diff_num} \\div {g}}}{{{d} \\div {g}}} = \\frac{{{num_simp}}}{{{den_simp}}} \\]"
    )
    ans = f"{num_simp}/{den_simp}"
    return {
        "id": f"g8_frac_sub_like_{rng.randint(100000, 999999)}",
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
        "subskill": "15_subtraction_like_denominators",
        "learning_objective_id": "math_g8_frac_sub_like",
        "hints": {
            "tier_1": f"Subtract the numerators: {a} - {b}.",
            "tier_2": f"{diff_num}/{d}.",
            "tier_3": f"{num_simp}/{den_simp}.",
        },
        "misconception_tags": ["subtracting_denominators_giving_zero"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 16. Subtraction Unlike Denominators
# ----------------------------------------------------------------------
def arch_16_subtraction_unlike_denominators(rng: random.Random) -> Dict[str, Any]:
    b = rng.choice([3, 4, 5])
    d = rng.choice([6, 7, 8])
    if b == d:
        d = b + 2
    lcm = math.lcm(b, d)
    # Ensure a/b > c/d
    a = b - 1
    c = 1
    num_diff = a * (lcm // b) - c * (lcm // d)
    g = math.gcd(num_diff, lcm)
    ans_num = num_diff // g
    ans_den = lcm // g

    prompt = (
        f"Calculate and write in simplest form:\n"
        f"\\[ \\frac{{{a}}}{{{b}}} - \\frac{{{c}}}{{{d}}} \\]"
    )
    sol = (
        f"**Step 1:** The LCD of {b} and {d} is **{lcm}**.\n\n"
        f"**Step 2:** Convert both fractions to denominator {lcm}:\n"
        f"\\[ \\frac{{{a} \\times {lcm // b}}}{{{lcm}}} - \\frac{{{c} \\times {lcm // d}}}{{{lcm}}} = \\frac{{{a * (lcm // b)}}}{{{lcm}}} - \\frac{{{c * (lcm // d)}}}{{{lcm}}} \\]\n\n"
        f"**Step 3:** Subtract numerators:\n"
        f"\\[ \\frac{{{a * (lcm // b) - c * (lcm // d)}}}{{{lcm}}} = \\frac{{{num_diff}}}{{{lcm}}} = \\frac{{{ans_num}}}{{{ans_den}}} \\]"
    )
    ans = f"{ans_num}/{ans_den}"
    return {
        "id": f"g8_frac_sub_unlike_{rng.randint(100000, 999999)}",
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
        "subskill": "16_subtraction_unlike_denominators",
        "learning_objective_id": "math_g8_frac_sub_unlike",
        "hints": {
            "tier_1": f"Find LCD of {b} and {d} = {lcm}.",
            "tier_2": f"({a * (lcm // b)} - {c * (lcm // d)}) / {lcm}.",
            "tier_3": f"{ans_num}/{ans_den}.",
        },
        "misconception_tags": ["subtracting_denominators"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 17. Subtraction From Whole Number
# ----------------------------------------------------------------------
def arch_17_subtraction_from_whole_number(rng: random.Random) -> Dict[str, Any]:
    w = rng.choice([3, 4, 5, 7])
    d = rng.choice([4, 5, 6, 8])
    num = rng.choice(range(1, d))
    while math.gcd(num, d) != 1:
        num = (num + 1) % d or 1
    # w - num/d = (w - 1) + (d - num)/d
    ans_w = w - 1
    ans_num = d - num

    prompt = (
        f"Subtract the fraction from the whole number:\n"
        f"\\[ {w} - \\frac{{{num}}}{{{d}}} \\]"
    )
    sol = (
        f"**Step 1:** Borrow 1 from the whole number **{w}** and rewrite it as a fraction with denominator {d}:\n"
        f"\\[ {w} = {w - 1} + 1 = {w - 1} \\frac{{{d}}}{{{d}}} \\]\n\n"
        f"**Step 2:** Subtract the fractional part:\n"
        f"\\[ {w - 1} \\frac{{{d}}}{{{d}}} - \\frac{{{num}}}{{{d}}} = {ans_w} \\frac{{{ans_num}}}{{{d}}} \\]"
    )
    ans = f"{ans_w} {ans_num}/{d}"
    return {
        "id": f"g8_frac_sub_whole_{rng.randint(100000, 999999)}",
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
        "subskill": "17_subtraction_from_whole_number",
        "learning_objective_id": "math_g8_frac_sub_whole_num",
        "hints": {
            "tier_1": f"Borrow 1 from {w}: {w} = {w - 1} + {d}/{d}.",
            "tier_2": f"{w - 1} and ({d} - {num})/{d}.",
            "tier_3": f"{ans_w} {ans_num}/{d}.",
        },
        "misconception_tags": ["subtracting_fraction_from_whole_directly_without_regrouping"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 18. Subtraction Mixed Numbers With Borrowing
# ----------------------------------------------------------------------
def arch_18_subtraction_mixed_numbers_with_borrowing(rng: random.Random) -> Dict[str, Any]:
    w1 = rng.choice([5, 6, 7])
    w2 = rng.choice([2, 3])
    d = rng.choice([4, 5, 6, 8])
    a = 1  # smaller fraction
    c = rng.choice([2, 3])  # larger fraction
    # w1 a/d - w2 c/d => (w1 - 1) (d + a)/d - w2 c/d
    ans_w = (w1 - 1) - w2
    ans_num = (d + a) - c
    g = math.gcd(ans_num, d)
    num_simp = ans_num // g
    den_simp = d // g

    prompt = (
        f"Calculate by regrouping (borrowing) and simplify:\n"
        f"\\[ {w1} \\frac{{{a}}}{{{d}}} - {w2} \\frac{{{c}}}{{{d}}} \\]"
    )
    sol = (
        f"**Step 1:** Since \\(\\frac{{{a}}}{{{d}}} < \\frac{{{c}}}{{{d}}}\\), borrow 1 from **{w1}**:\n"
        f"\\[ {w1} \\frac{{{a}}}{{{d}}} = {w1 - 1} \\left(1 + \\frac{{{a}}}{{{d}}}\\right) = {w1 - 1} \\frac{{{d + a}}}{{{d}}} \\]\n\n"
        f"**Step 2:** Subtract the whole numbers and fractions:\n"
        f"\\[ ({w1 - 1} - {w2}) + \\left(\\frac{{{d + a} - {c}}}{{{d}}}\\right) = {ans_w} \\frac{{{ans_num}}}{{{d}}} \\]\n\n"
        f"**Step 3:** Simplify to lowest terms:\n"
        f"\\[ {ans_w} \\frac{{{num_simp}}}{{{den_simp}}} \\]"
    )
    ans = f"{ans_w} {num_simp}/{den_simp}"
    return {
        "id": f"g8_frac_sub_borrow_{rng.randint(100000, 999999)}",
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
        "subskill": "18_subtraction_mixed_numbers_with_borrowing",
        "learning_objective_id": "math_g8_frac_sub_mixed_borrow",
        "hints": {
            "tier_1": f"Borrow 1 from {w1}: {w1} {a}/{d} = {w1 - 1} {d + a}/{d}.",
            "tier_2": f"Subtract {w2} {c}/{d}.",
            "tier_3": f"{ans}.",
        },
        "misconception_tags": ["subtracting_smaller_fraction_from_larger_inverting_order"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 19. Multiplication Fraction By Whole Number
# ----------------------------------------------------------------------
def arch_19_multiplication_fraction_by_whole_number(rng: random.Random) -> Dict[str, Any]:
    b = rng.choice([4, 6, 8, 9])
    a = rng.choice([2, 3, 5])
    while math.gcd(a, b) != 1:
        a = (a + 1) % b or 1
    mult = rng.choice([2, 3, 4])
    w = b * mult // 2  # ensures some cross cancellation
    num_tot = a * w
    g = math.gcd(num_tot, b)
    ans_num = num_tot // g
    ans_den = b // g

    prompt = (
        f"Multiply and simplify:\n"
        f"\\[ \\frac{{{a}}}{{{b}}} \\times {w} \\]"
    )
    sol = (
        f"**Step 1:** Write the whole number as a fraction over 1:\n"
        f"\\[ \\frac{{{a}}}{{{b}}} \\times \\frac{{{w}}}{{1}} \\]\n\n"
        f"**Step 2:** Cross-cancel common factors between {w} and {b}:\n"
        f"\\(\\gcd({w}; {b}) = {math.gcd(w, b)}\\).\n"
        f"\\[ \\frac{{{a} \\times {w // math.gcd(w, b)}}}{{{b // math.gcd(w, b)} \\times 1}} = \\frac{{{ans_num}}}{{{ans_den}}} \\]"
    )
    if ans_den == 1:
        ans = str(ans_num)
    elif ans_num > ans_den:
        ans = f"{ans_num // ans_den} {ans_num % ans_den}/{ans_den}"
    else:
        ans = f"{ans_num}/{ans_den}"
    return {
        "id": f"g8_frac_mult_whole_{rng.randint(100000, 999999)}",
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
        "subskill": "19_multiplication_fraction_by_whole_number",
        "learning_objective_id": "math_g8_frac_mult_whole",
        "hints": {
            "tier_1": f"Write {w} as {w}/1 and multiply numerators and denominators.",
            "tier_2": f"({a} × {w}) / {b}.",
            "tier_3": f"{ans}.",
        },
        "misconception_tags": ["multiplying_both_numerator_and_denominator_by_whole"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 20. Multiplication Two Proper Fractions
# ----------------------------------------------------------------------
def arch_20_multiplication_two_proper_fractions(rng: random.Random) -> Dict[str, Any]:
    # Choose values that allow cross-cancellation
    k = rng.choice([2, 3, 5])
    a = 2
    b = 3 * k
    c = 5 * k
    d = 7
    # a/b * c/d = (2 * 5) / (3 * 7) = 10/21
    num_tot = a * c
    den_tot = b * d
    g = math.gcd(num_tot, den_tot)
    ans_num = num_tot // g
    ans_den = den_tot // g

    prompt = (
        f"Calculate and simplify by cross-cancelling:\n"
        f"\\[ \\frac{{{a}}}{{{b}}} \\times \\frac{{{c}}}{{{d}}} \\]"
    )
    sol = (
        f"**Step 1:** Cross-cancel common factor {k} between numerator {c} and denominator {b}:\n"
        f"\\[ \\frac{{{a}}}{{{b // k}}} \\times \\frac{{{c // k}}}{{{d}}} = \\frac{{{a}}}{{{b // k}}} \\times \\frac{{{c // k}}}{{{d}}} \\]\n\n"
        f"**Step 2:** Multiply numerators and denominators:\n"
        f"\\[ \\frac{{{a} \\times {c // k}}}{{{b // k} \\times {d}}} = \\frac{{{ans_num}}}{{{ans_den}}} \\]"
    )
    ans = f"{ans_num}/{ans_den}"
    return {
        "id": f"g8_frac_mult_2_{rng.randint(100000, 999999)}",
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
        "subskill": "20_multiplication_two_proper_fractions",
        "learning_objective_id": "math_g8_frac_mult_two_proper",
        "hints": {
            "tier_1": f"Cross-cancel common factors before multiplying.",
            "tier_2": f"Both {c} and {b} share a factor of {k}.",
            "tier_3": f"{ans_num}/{ans_den}.",
        },
        "misconception_tags": ["cross_multiplying_during_multiplication"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 21. Multiplication Three Fractions Cross Cancel
# ----------------------------------------------------------------------
def arch_21_multiplication_three_fractions_cross_cancel(rng: random.Random) -> Dict[str, Any]:
    # e.g., 2/3 * 3/4 * 4/5 = 2/5
    d1 = rng.choice([3, 4, 5])
    d2 = d1 + 1
    d3 = d2 + 1
    n1 = 2
    n2 = d1
    n3 = d2
    # n1/d1 * n2/d2 * n3/d3 = 2/d1 * d1/d2 * d2/d3 = 2/d3
    g = math.gcd(n1, d3)
    ans_num = n1 // g
    ans_den = d3 // g

    prompt = (
        f"Calculate the product of the three fractions using cross-simplification:\n"
        f"\\[ \\frac{{{n1}}}{{{d1}}} \\times \\frac{{{n2}}}{{{d2}}} \\times \\frac{{{n3}}}{{{d3}}} \\]"
    )
    sol = (
        f"**Step 1:** Notice the telescoping cross-cancellation:\n"
        f"The {d1} in the denominator of the first fraction cancels with {n2} in the numerator of the second fraction.\n"
        f"The {d2} in the denominator of the second fraction cancels with {n3} in the numerator of the third fraction.\n\n"
        f"**Step 2:** Multiply remaining factors:\n"
        f"\\[ \\frac{{{n1}}}{{1}} \\times \\frac{{1}}{{1}} \\times \\frac{{1}}{{{d3}}} = \\frac{{{n1}}}{{{d3}}} = \\frac{{{ans_num}}}{{{ans_den}}} \\]"
    )
    ans = f"{ans_num}/{ans_den}"
    return {
        "id": f"g8_frac_mult_3_{rng.randint(100000, 999999)}",
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
        "subskill": "21_multiplication_three_fractions_cross_cancel",
        "learning_objective_id": "math_g8_frac_mult_three",
        "hints": {
            "tier_1": f"Cross-cancel matching numerators and denominators.",
            "tier_2": f"{d1} cancels with {n2}, {d2} cancels with {n3}.",
            "tier_3": f"{ans_num}/{ans_den}.",
        },
        "misconception_tags": ["multiplying_all_terms_without_cancelling_first"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 22. Multiplication Mixed Numbers
# ----------------------------------------------------------------------
def arch_22_multiplication_mixed_numbers(rng: random.Random) -> Dict[str, Any]:
    w1 = rng.choice([1, 2])
    w2 = rng.choice([1, 2])
    b = rng.choice([2, 3, 4])
    d = rng.choice([3, 5])
    a = 1
    c = 1
    # Convert to improper
    num1 = w1 * b + a
    num2 = w2 * d + c
    tot_num = num1 * num2
    tot_den = b * d
    g = math.gcd(tot_num, tot_den)
    simp_num = tot_num // g
    simp_den = tot_den // g

    prompt = (
        f"Multiply the mixed numbers and write in simplest form:\n"
        f"\\[ {w1} \\frac{{{a}}}{{{b}}} \\times {w2} \\frac{{{c}}}{{{d}}} \\]"
    )
    sol = (
        f"**Step 1:** Convert both mixed numbers into improper fractions:\n"
        f"\\[ {w1} \\frac{{{a}}}{{{b}}} = \\frac{{{num1}}}{{{b}}} \\quad \\text{{and}} \\quad {w2} \\frac{{{c}}}{{{d}}} = \\frac{{{num2}}}{{{d}}} \\]\n\n"
        f"**Step 2:** Multiply numerators and denominators:\n"
        f"\\[ \\frac{{{num1}}}{{{b}}} \\times \\frac{{{num2}}}{{{d}}} = \\frac{{{tot_num}}}{{{tot_den}}} = \\frac{{{simp_num}}}{{{simp_den}}} \\]"
    )
    if simp_num >= simp_den:
        w_ans = simp_num // simp_den
        rem_ans = simp_num % simp_den
        ans = f"{w_ans} {rem_ans}/{simp_den}" if rem_ans > 0 else str(w_ans)
    else:
        ans = f"{simp_num}/{simp_den}"
    return {
        "id": f"g8_frac_mult_mix_{rng.randint(100000, 999999)}",
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
        "subskill": "22_multiplication_mixed_numbers",
        "learning_objective_id": "math_g8_frac_mult_mixed",
        "hints": {
            "tier_1": f"Always convert mixed numbers to improper fractions first.",
            "tier_2": f"{num1}/{b} × {num2}/{d}.",
            "tier_3": f"{ans}.",
        },
        "misconception_tags": ["multiplying_whole_numbers_and_fractions_separately"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 23. Reciprocal Of Fraction And Mixed Number
# ----------------------------------------------------------------------
def arch_23_reciprocal_of_fraction_and_mixed_number(rng: random.Random) -> Dict[str, Any]:
    w = rng.choice([2, 3, 4])
    b = rng.choice([3, 5, 7])
    a = rng.choice(range(1, b))
    imp_num = w * b + a

    prompt = (
        f"Determine the reciprocal (multiplicative inverse) of the mixed number:\n"
        f"\\[ {w} \\frac{{{a}}}{{{b}}} \\]"
    )
    sol = (
        f"**Step 1:** Convert the mixed number into an improper fraction:\n"
        f"\\[ {w} \\frac{{{a}}}{{{b}}} = \\frac{{{w} \\times {b} + {a}}}{{{b}}} = \\frac{{{imp_num}}}{{{b}}} \\]\n\n"
        f"**Step 2:** Invert the numerator and denominator to find the reciprocal:\n"
        f"\\[ \\text{{Reciprocal}} = \\frac{{{b}}}{{{imp_num}}} \\]\n\n"
        f"**Check:** \\(\\frac{{{imp_num}}}{{{b}}} \\times \\frac{{{b}}}{{{imp_num}}} = 1\\)."
    )
    ans = f"{b}/{imp_num}"
    return {
        "id": f"g8_frac_recip_{rng.randint(100000, 999999)}",
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
        "subskill": "23_reciprocal_of_fraction_and_mixed_number",
        "learning_objective_id": "math_g8_frac_reciprocal",
        "hints": {
            "tier_1": f"First convert {w} {a}/{b} to an improper fraction.",
            "tier_2": f"Improper fraction is {imp_num}/{b}.",
            "tier_3": f"Swap numerator and denominator: {b}/{imp_num}.",
        },
        "misconception_tags": ["inverting_fractional_part_while_keeping_whole_number"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 24. Division Whole Number By Fraction
# ----------------------------------------------------------------------
def arch_24_division_whole_number_by_fraction(rng: random.Random) -> Dict[str, Any]:
    w = rng.choice([6, 8, 10, 12, 15])
    b = rng.choice([3, 4, 5])
    a = rng.choice([2, 3])
    while math.gcd(a, b) != 1 or w % a != 0:
        a = 2
        w = 8
        b = 3
    # w ÷ (a/b) = w * (b/a) = (w/a) * b
    ans_val = (w // a) * b

    prompt = (
        f"Calculate:\n"
        f"\\[ {w} \\div \\frac{{{a}}}{{{b}}} \\]"
    )
    sol = (
        f"**Step 1:** Multiply by the reciprocal of the divisor fraction:\n"
        f"\\[ {w} \\div \\frac{{{a}}}{{{b}}} = {w} \\times \\frac{{{b}}}{{{a}}} \\]\n\n"
        f"**Step 2:** Simplify by dividing {w} by {a}:\n"
        f"\\[ {w // a} \\times {b} = {ans_val} \\]"
    )
    ans = str(ans_val)
    return {
        "id": f"g8_frac_div_whole_{rng.randint(100000, 999999)}",
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
        "subskill": "24_division_whole_number_by_fraction",
        "learning_objective_id": "math_g8_frac_div_whole",
        "hints": {
            "tier_1": f"Multiply by the reciprocal: {w} × ({b}/{a}).",
            "tier_2": f"{w} × {b} ÷ {a}.",
            "tier_3": f"{ans_val}.",
        },
        "misconception_tags": ["inverting_dividend_instead_of_divisor"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 25. Division Fraction By Whole Number
# ----------------------------------------------------------------------
def arch_25_division_fraction_by_whole_number(rng: random.Random) -> Dict[str, Any]:
    b = rng.choice([3, 4, 5, 7])
    w = rng.choice([2, 3, 5])
    a = rng.choice([2, 3, 4])
    while math.gcd(a, b) != 1:
        a = (a + 1) % b or 1
    # a/b ÷ w = a / (b * w)
    tot_den = b * w
    g = math.gcd(a, tot_den)
    ans_num = a // g
    ans_den = tot_den // g

    prompt = (
        f"Calculate and simplify:\n"
        f"\\[ \\frac{{{a}}}{{{b}}} \\div {w} \\]"
    )
    sol = (
        f"**Step 1:** Write the whole number as \\(\\frac{{{w}}}{{1}}\\):\n"
        f"\\[ \\frac{{{a}}}{{{b}}} \\div \\frac{{{w}}}{{1}} \\]\n\n"
        f"**Step 2:** Invert the divisor and multiply:\n"
        f"\\[ \\frac{{{a}}}{{{b}}} \\times \\frac{{1}}{{{w}}} = \\frac{{{a}}}{{{tot_den}}} = \\frac{{{ans_num}}}{{{ans_den}}} \\]"
    )
    ans = f"{ans_num}/{ans_den}"
    return {
        "id": f"g8_frac_div_by_whole_{rng.randint(100000, 999999)}",
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
        "subskill": "25_division_fraction_by_whole_number",
        "learning_objective_id": "math_g8_frac_div_by_whole",
        "hints": {
            "tier_1": f"Multiply by 1/{w}.",
            "tier_2": f"Denominator becomes {b} × {w} = {tot_den}.",
            "tier_3": f"{ans_num}/{ans_den}.",
        },
        "misconception_tags": ["dividing_numerator_only_by_whole_number"],
        "diagram_spec": None,
    }


BUILDERS_01_25: List[Callable[[random.Random], Dict[str, Any]]] = [
    arch_01_simplifying_fraction_hcf,
    arch_02_equivalent_fractions_missing_numerator,
    arch_03_equivalent_fractions_missing_denominator,
    arch_04_converting_improper_fraction_to_mixed_number,
    arch_05_converting_mixed_number_to_improper_fraction,
    arch_06_comparing_fractions_common_denominator,
    arch_07_ordering_three_fractions_ascending,
    arch_08_fraction_of_whole_number_quantity,
    arch_09_fraction_of_measurement_unit_conversion,
    arch_10_addition_like_denominators_proper,
    arch_11_addition_unlike_denominators_multiples,
    arch_12_addition_unlike_denominators_coprime,
    arch_13_addition_three_fractions_lcd,
    arch_14_addition_mixed_numbers_unlike_denominators,
    arch_15_subtraction_like_denominators,
    arch_16_subtraction_unlike_denominators,
    arch_17_subtraction_from_whole_number,
    arch_18_subtraction_mixed_numbers_with_borrowing,
    arch_19_multiplication_fraction_by_whole_number,
    arch_20_multiplication_two_proper_fractions,
    arch_21_multiplication_three_fractions_cross_cancel,
    arch_22_multiplication_mixed_numbers,
    arch_23_reciprocal_of_fraction_and_mixed_number,
    arch_24_division_whole_number_by_fraction,
    arch_25_division_fraction_by_whole_number,
]
