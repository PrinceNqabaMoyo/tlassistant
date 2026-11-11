"""Grade 9 Mathematics - Common Fractions Archetypes 01 to 25.
Grounded in curriculum_docs_auto/Mathematics_Gr9/Term 2/01. Fractions.md:
Fraction strips, equivalent fractions, simplification via HCF, improper/mixed conversions,
comparing and ordering, number lines, addition, subtraction, multiplication, division,
powers (squares, cubes) and roots (square roots, cube roots).
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional, Tuple

from .fractions_svg import (
    draw_fraction_number_line_svg,
    draw_fraction_strip_svg,
)


# ----------------------------------------------------------------------
# Helper functions
# ----------------------------------------------------------------------
def _simplify(n: int, d: int) -> Tuple[int, int]:
    g = math.gcd(n, d)
    return n // g, d // g


def _frac_str(n: int, d: int) -> str:
    n, d = _simplify(n, d)
    if d == 1:
        return str(n)
    return f"\\frac{{{n}}}{{{d}}}"


def _mixed_str(n: int, d: int) -> str:
    n, d = _simplify(n, d)
    if n < d:
        return f"\\frac{{{n}}}{{{d}}}"
    w = n // d
    r = n % d
    if r == 0:
        return str(w)
    return f"{w}\\frac{{{r}}}{{{d}}}"


# ----------------------------------------------------------------------
# 01. Fraction Strip Identification: Shaded Part
# ----------------------------------------------------------------------
def arch_01_fraction_strip_identification_shaded_part(rng: random.Random) -> Dict[str, Any]:
    d = rng.choice([5, 6, 7, 8, 9, 10, 12, 15])
    n = rng.randint(1, d - 1)
    # Ensure some variety in simplification
    ns, ds = _simplify(n, d)

    ans_latex = _frac_str(n, d)
    ans_text = f"{ns}/{ds}"
    seed_val = rng.randint(1000, 999999)
    svg = draw_fraction_strip_svg(n, d, label="Fraction Strip", seed=seed_val)

    prompt = (
        f"Determine the fraction represented by the shaded portion of the fraction strip shown below. "
        f"Give your answer as a simplified common fraction."
    )
    sol = (
        f"**Step 1: Count total equal parts and shaded parts.**\n"
        f"Total parts = \\({d}\\).\n"
        f"Shaded parts = \\({n}\\).\n\n"
        f"**Step 2: Express as a fraction and simplify.**\n"
        f"\\[ \\frac{{{n}}}{{{d}}} = {ans_latex} \\]"
    )
    return {
        "id": f"g9_frac_strip_{rng.randint(100000, 999999)}",
        "question_type": "fraction",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans_latex,
        "expected_answer": ans_latex,
        "sample_answer": ans_text,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"Identify initial fraction {n}/{d}", "marks": 1},
            {"desc": f"Simplify to {ans_latex}", "marks": 1},
        ],
        "hints": [
            f"Count how many equal parts the strip is divided into: that is the denominator.",
            f"Count how many parts are shaded: that is the numerator.",
            f"Simplify the fraction by dividing by the highest common factor.",
        ],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 02. Equivalent Fractions: Find Missing Numerator or Denominator
# ----------------------------------------------------------------------
def arch_02_equivalent_fractions_find_missing_numerator_or_denominator(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([2, 3, 4, 5, 7])
    b = rng.choice([3, 5, 7, 8, 9, 11])
    while math.gcd(a, b) != 1 or a >= b:
        b = a + rng.randint(1, 5)

    k = rng.randint(2, 9)
    missing_type = rng.choice(["numerator", "denominator"])

    if missing_type == "numerator":
        # a/b = x/(b*k)
        missing_val = a * k
        scaled_d = b * k
        prompt = (
            f"Determine the value of \\(x\\) that makes the statement true:\n"
            f"\\[ \\frac{{{a}}}{{{b}}} = \\frac{{x}}{{{scaled_d}}} \\]"
        )
        sol = (
            f"**Step 1: Determine the scale factor between denominators.**\n"
            f"\\[ {scaled_d} \\div {b} = {k} \\]\n\n"
            f"**Step 2: Multiply the numerator by the same factor.**\n"
            f"\\[ x = {a} \\times {k} = {missing_val} \\]"
        )
    else:
        # a/b = (a*k)/y
        missing_val = b * k
        scaled_n = a * k
        prompt = (
            f"Determine the value of \\(y\\) that makes the statement true:\n"
            f"\\[ \\frac{{{a}}}{{{b}}} = \\frac{{{scaled_n}}}{{y}} \\]"
        )
        sol = (
            f"**Step 1: Determine the scale factor between numerators.**\n"
            f"\\[ {scaled_n} \\div {a} = {k} \\]\n\n"
            f"**Step 2: Multiply the denominator by the same factor.**\n"
            f"\\[ y = {b} \\times {k} = {missing_val} \\]"
        )

    return {
        "id": f"g9_frac_equiv_{rng.randint(100000, 999999)}",
        "question_type": "numeric",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": str(missing_val),
        "expected_answer": str(missing_val),
        "sample_answer": str(missing_val),
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"Identify scale factor {k}", "marks": 1},
            {"desc": f"State missing value {missing_val}", "marks": 1},
        ],
        "hints": [
            "Fractions remain equivalent when numerator and denominator are multiplied by the same non-zero integer.",
            f"Find what the given number was multiplied by to get the scaled value.",
            f"The missing value is {missing_val}.",
        ],
    }


# ----------------------------------------------------------------------
# 03. Simplify Fraction to Lowest Terms via HCF
# ----------------------------------------------------------------------
def arch_03_simplify_fraction_to_lowest_terms_via_hcf(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([2, 3, 4, 5, 7])
    b = rng.choice([3, 5, 7, 8, 9, 11, 13])
    while math.gcd(a, b) != 1 or a >= b:
        b = a + rng.randint(2, 6)

    hcf = rng.choice([3, 4, 6, 8, 12, 14, 15])
    num = a * hcf
    den = b * hcf

    ans_latex = f"\\frac{{{a}}}{{{b}}}"
    ans_text = f"{a}/{b}"
    prompt = (
        f"Simplify the common fraction to its simplest lowest terms by finding the Highest Common Factor (HCF):\n"
        f"\\[ \\frac{{{num}}}{{{den}}} \\]"
    )
    sol = (
        f"**Step 1: Find the HCF of {num} and {den}.**\n"
        f"\\[ \\text{{HCF}}({num}, {den}) = {hcf} \\]\n\n"
        f"**Step 2: Divide both numerator and denominator by {hcf}.**\n"
        f"\\[ \\frac{{{num} \\div {hcf}}}{{{den} \\div {hcf}}} = {ans_latex} \\]"
    )
    return {
        "id": f"g9_frac_simp_{rng.randint(100000, 999999)}",
        "question_type": "fraction",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans_latex,
        "expected_answer": ans_latex,
        "sample_answer": ans_text,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"Identify HCF = {hcf}", "marks": 1},
            {"desc": f"Divide numerator and denominator to get {ans_latex}", "marks": 1},
        ],
        "hints": [
            "Find the greatest integer that divides evenly into both the numerator and denominator.",
            f"The HCF is {hcf}.",
            f"Divide top and bottom by {hcf} to get {ans_text}.",
        ],
    }


# ----------------------------------------------------------------------
# 04. Convert Improper Fraction to Mixed Number
# ----------------------------------------------------------------------
def arch_04_convert_improper_fraction_to_mixed_number(rng: random.Random) -> Dict[str, Any]:
    d = rng.choice([3, 4, 5, 6, 7, 8, 9, 11])
    w = rng.randint(2, 7)
    r = rng.randint(1, d - 1)
    while math.gcd(r, d) != 1:
        r = (r % (d - 1)) + 1
    num = w * d + r

    ans_latex = f"{w}\\frac{{{r}}}{{{d}}}"
    ans_text = f"{w} {r}/{d}"

    prompt = (
        f"Convert the improper fraction to a mixed number in simplest form:\n"
        f"\\[ \\frac{{{num}}}{{{d}}} \\]"
    )
    sol = (
        f"**Step 1: Divide the numerator by the denominator.**\n"
        f"\\[ {num} \\div {d} = {w} \\text{{ with a remainder of }} {r} \\]\n\n"
        f"**Step 2: Write the remainder over the divisor.**\n"
        f"\\[ = {ans_latex} \\]"
    )
    return {
        "id": f"g9_frac_imp_to_mix_{rng.randint(100000, 999999)}",
        "question_type": "mixed_number",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans_latex,
        "expected_answer": ans_latex,
        "sample_answer": ans_text,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"Calculate quotient {w} and remainder {r}", "marks": 1},
            {"desc": f"Write correct mixed number {ans_latex}", "marks": 1},
        ],
        "hints": [
            "Divide the top number by the bottom number to get the whole number part.",
            "The remainder forms the numerator of the fractional part, over the original denominator.",
            f"The answer is {ans_text}.",
        ],
    }


# ----------------------------------------------------------------------
# 05. Convert Mixed Number to Improper Fraction
# ----------------------------------------------------------------------
def arch_05_convert_mixed_number_to_improper_fraction(rng: random.Random) -> Dict[str, Any]:
    d = rng.choice([3, 4, 5, 6, 7, 8, 9, 12])
    w = rng.randint(2, 8)
    r = rng.randint(1, d - 1)
    while math.gcd(r, d) != 1:
        r = (r % (d - 1)) + 1
    num = w * d + r

    ans_latex = f"\\frac{{{num}}}{{{d}}}"
    ans_text = f"{num}/{d}"

    prompt = (
        f"Convert the mixed number to an improper fraction:\n"
        f"\\[ {w}\\frac{{{r}}}{{{d}}} \\]"
    )
    sol = (
        f"**Step 1: Multiply the whole number by the denominator.**\n"
        f"\\[ {w} \\times {d} = {w * d} \\]\n\n"
        f"**Step 2: Add the numerator to the product.**\n"
        f"\\[ {w * d} + {r} = {num} \\]\n\n"
        f"**Step 3: Place the result over the original denominator.**\n"
        f"\\[ = {ans_latex} \\]"
    )
    return {
        "id": f"g9_frac_mix_to_imp_{rng.randint(100000, 999999)}",
        "question_type": "fraction",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans_latex,
        "expected_answer": ans_latex,
        "sample_answer": ans_text,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"Calculate whole × denominator + numerator: ({w}×{d}) + {r} = {num}", "marks": 1},
            {"desc": f"Write improper fraction {ans_latex}", "marks": 1},
        ],
        "hints": [
            "Multiply the whole number by the denominator, then add the numerator.",
            f"Calculation: ({w} × {d}) + {r} = {num}.",
            f"The improper fraction is {ans_text}.",
        ],
    }


# ----------------------------------------------------------------------
# 06. Compare Two Fractions Using Inequality Symbols
# ----------------------------------------------------------------------
def arch_06_compare_two_fractions_using_inequality_symbols(rng: random.Random) -> Dict[str, Any]:
    b = rng.choice([3, 4, 5, 6, 8, 10])
    d = rng.choice([2, 5, 7, 9, 12])
    while b == d:
        d = rng.choice([2, 7, 9, 11])

    a = rng.randint(1, b - 1)
    c = rng.randint(1, d - 1)

    lcd = (b * d) // math.gcd(b, d)
    scaled_a = a * (lcd // b)
    scaled_c = c * (lcd // d)

    if scaled_a < scaled_c:
        symbol = "<"
    elif scaled_a > scaled_c:
        symbol = ">"
    else:
        symbol = "="

    prompt = (
        f"Insert the correct relation symbol (\\(<\\), \\(>\\), or \\(=\\)) to make the statement true:\n"
        f"\\[ \\frac{{{a}}}{{{b}}} \\quad \\square \\quad \\frac{{{c}}}{{{d}}} \\]"
    )
    sol = (
        f"**Step 1: Determine the Lowest Common Denominator (LCD).**\n"
        f"\\[ \\text{{LCD}}({b}, {d}) = {lcd} \\]\n\n"
        f"**Step 2: Convert both fractions to equivalent fractions with denominator {lcd}.**\n"
        f"\\[ \\frac{{{a}}}{{{b}}} = \\frac{{{scaled_a}}}{{{lcd}}}, \\quad \\frac{{{c}}}{{{d}}} = \\frac{{{scaled_c}}}{{{lcd}}} \\]\n\n"
        f"**Step 3: Compare the numerators.**\n"
        f"Since \\({scaled_a} {symbol} {scaled_c}\\), it follows that:\n"
        f"\\[ \\frac{{{a}}}{{{b}}} {symbol} \\frac{{{c}}}{{{d}}} \\]"
    )
    return {
        "id": f"g9_frac_comp_{rng.randint(100000, 999999)}",
        "question_type": "symbol",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": symbol,
        "expected_answer": symbol,
        "sample_answer": symbol,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"Find common denominator {lcd} and convert fractions", "marks": 1},
            {"desc": f"Correct inequality symbol '{symbol}'", "marks": 1},
        ],
        "hints": [
            "Find a common denominator for both fractions before comparing.",
            f"The LCD of {b} and {d} is {lcd}.",
            f"Compare {scaled_a}/{lcd} and {scaled_c}/{lcd}.",
        ],
    }


# ----------------------------------------------------------------------
# 07. Order Set of Fractions Ascending or Descending
# ----------------------------------------------------------------------
def arch_07_order_set_of_fractions_ascending_descending(rng: random.Random) -> Dict[str, Any]:
    base_lcm = rng.choice([12, 24, 30, 36, 48])
    if base_lcm == 12:
        denoms = [2, 3, 4, 6]
    elif base_lcm == 24:
        denoms = [3, 4, 6, 8]
    elif base_lcm == 30:
        denoms = [2, 3, 5, 10]
    elif base_lcm == 36:
        denoms = [3, 4, 6, 9]
    else:
        denoms = [4, 6, 8, 12]

    # Generate distinct fractions
    used_values = set()
    fracs = []
    for d in denoms:
        n = rng.randint(1, d - 1)
        val = n / d
        while val in used_values:
            n = (n % (d - 1)) + 1
            val = n / d
        used_values.add(val)
        fracs.append((n, d, val))

    order_dir = rng.choice(["ascending", "descending"])
    if order_dir == "ascending":
        sorted_fracs = sorted(fracs, key=lambda x: x[2])
    else:
        sorted_fracs = sorted(fracs, key=lambda x: x[2], reverse=True)

    given_str = ", \\; ".join([f"\\frac{{{n}}}{{{d}}}" for n, d, _ in fracs])
    ans_latex = "; \\; ".join([f"\\frac{{{n}}}{{{d}}}" for n, d, _ in sorted_fracs])
    ans_text = "; ".join([f"{n}/{d}" for n, d, _ in sorted_fracs])

    equiv_str = ", \\; ".join([f"\\frac{{{int(round(v * base_lcm))}}}{{{base_lcm}}}" for _, _, v in fracs])

    prompt = (
        f"Arrange the following set of fractions in **{order_dir}** order (from "
        f"{'smallest to largest' if order_dir == 'ascending' else 'largest to smallest'}):\n"
        f"\\[ {given_str} \\]"
    )
    sol = (
        f"**Step 1: Express all fractions with the common denominator {base_lcm}.**\n"
        f"\\[ {equiv_str} \\]\n\n"
        f"**Step 2: Order according to their numerators in {order_dir} order.**\n"
        f"\\[ {ans_latex} \\]"
    )
    return {
        "id": f"g9_frac_order_{rng.randint(100000, 999999)}",
        "question_type": "ordered_list",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans_latex,
        "expected_answer": ans_latex,
        "sample_answer": ans_text,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "marking_schema": [
            {"desc": f"Find LCD = {base_lcm} and equivalent numerators", "marks": 2},
            {"desc": f"Order correctly in {order_dir} sequence", "marks": 1},
        ],
        "hints": [
            f"Convert all fractions to equivalent fractions with a common denominator of {base_lcm}.",
            "Compare the numerators once the denominators are identical.",
            f"Arrange from {'smallest to largest' if order_dir == 'ascending' else 'largest to smallest'}.",
        ],
    }


# ----------------------------------------------------------------------
# 08. Fraction on Number Line: Identify Point
# ----------------------------------------------------------------------
def arch_08_fraction_on_number_line_identify_point(rng: random.Random) -> Dict[str, Any]:
    d = rng.choice([4, 5, 6, 8, 10, 12])
    k = rng.randint(1, d - 1)
    ns, ds = _simplify(k, d)

    seed_val = rng.randint(1000, 999999)
    svg = draw_fraction_number_line_svg(0, 1, d, [(k / d, "A")], seed=seed_val)

    ans_latex = _frac_str(k, d)
    ans_text = f"{ns}/{ds}"

    prompt = (
        f"Identify the common fraction represented by point \\(A\\) on the number line shown below. "
        f"Give your answer in simplest form."
    )
    sol = (
        f"**Step 1: Count the number of equal sub-intervals between 0 and 1.**\n"
        f"The interval \\([0, 1]\\) is divided into \\({d}\\) equal parts, so each tick mark represents \\(\\frac{{1}}{{{d}}}\\).\n\n"
        f"**Step 2: Count ticks from 0 to point A.**\n"
        f"Point \\(A\\) is at tick \\({k}\\), which corresponds to \\(\\frac{{{k}}}{{{d}}}\\).\n\n"
        f"**Step 3: Simplify the fraction.**\n"
        f"\\[ \\frac{{{k}}}{{{d}}} = {ans_latex} \\]"
    )
    return {
        "id": f"g9_frac_numline_{rng.randint(100000, 999999)}",
        "question_type": "fraction",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans_latex,
        "expected_answer": ans_latex,
        "sample_answer": ans_text,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"Identify point at position {k}/{d}", "marks": 1},
            {"desc": f"Simplify fraction to {ans_latex}", "marks": 1},
        ],
        "hints": [
            f"Count the number of equal spaces between 0 and 1: that is the denominator {d}.",
            f"Count the number of intervals from 0 up to point A: that is {k}.",
            f"Simplify {k}/{d} to lowest terms.",
        ],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 09. Addition of Proper Fractions with Like Denominators
# ----------------------------------------------------------------------
def arch_09_addition_proper_fractions_like_denominators(rng: random.Random) -> Dict[str, Any]:
    d = rng.choice([6, 8, 10, 12, 14, 15, 16, 20])
    a = rng.randint(1, d // 2)
    b = rng.randint(1, d - a - 1)
    tot = a + b
    ans_latex = _frac_str(tot, d)
    ans_text = f"{tot // math.gcd(tot, d)}/{d // math.gcd(tot, d)}"

    prompt = (
        f"Calculate and simplify the following sum to lowest terms:\n"
        f"\\[ \\frac{{{a}}}{{{d}}} + \\frac{{{b}}}{{{d}}} \\]"
    )
    sol = (
        f"**Step 1: Add the numerators over the common denominator.**\n"
        f"\\[ \\frac{{{a} + {b}}}{{{d}}} = \\frac{{{tot}}}{{{d}}} \\]\n\n"
        f"**Step 2: Simplify the resulting fraction.**\n"
        f"\\[ = {ans_latex} \\]"
    )
    return {
        "id": f"g9_frac_add_like_{rng.randint(100000, 999999)}",
        "question_type": "fraction",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans_latex,
        "expected_answer": ans_latex,
        "sample_answer": ans_text,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"Add numerators {a} + {b} = {tot}/{d}", "marks": 1},
            {"desc": f"Simplify to {ans_latex}", "marks": 1},
        ],
        "hints": [
            "When denominators are identical, add the numerators and keep the same denominator.",
            f"Add {a} + {b} = {tot}.",
            f"Simplify {tot}/{d} to lowest terms.",
        ],
    }


# ----------------------------------------------------------------------
# 10. Addition of Proper Fractions with Unlike Denominators
# ----------------------------------------------------------------------
def arch_10_addition_proper_fractions_unlike_denominators(rng: random.Random) -> Dict[str, Any]:
    b = rng.choice([3, 4, 6, 8, 10])
    d = rng.choice([2, 5, 7, 9, 12])
    while b == d:
        d = rng.choice([2, 5, 7, 11])

    a = rng.randint(1, b - 1)
    c = rng.randint(1, d - 1)

    lcd = (b * d) // math.gcd(b, d)
    m1 = lcd // b
    m2 = lcd // d
    num_tot = a * m1 + c * m2

    ans_latex = _mixed_str(num_tot, lcd)
    ns, ds = _simplify(num_tot, lcd)
    ans_text = f"{ns}/{ds}"

    prompt = (
        f"Calculate the following sum. Give your answer as a simplified fraction or mixed number:\n"
        f"\\[ \\frac{{{a}}}{{{b}}} + \\frac{{{c}}}{{{d}}} \\]"
    )
    sol = (
        f"**Step 1: Determine the Lowest Common Denominator (LCD).**\n"
        f"\\[ \\text{{LCD}}({b}, {d}) = {lcd} \\]\n\n"
        f"**Step 2: Convert both fractions to equivalent fractions with denominator {lcd}.**\n"
        f"\\[ \\frac{{{a} \\times {m1}}}{{{b} \\times {m1}}} + \\frac{{{c} \\times {m2}}}{{{d} \\times {m2}}} "
        f"= \\frac{{{a * m1}}}{{{lcd}}} + \\frac{{{c * m2}}}{{{lcd}}} \\]\n\n"
        f"**Step 3: Add numerators and simplify.**\n"
        f"\\[ \\frac{{{a * m1 + c * m2}}}{{{lcd}}} = \\frac{{{num_tot}}}{{{lcd}}} = {ans_latex} \\]"
    )
    return {
        "id": f"g9_frac_add_unlike_{rng.randint(100000, 999999)}",
        "question_type": "fraction",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans_latex,
        "expected_answer": ans_latex,
        "sample_answer": ans_text,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "marking_schema": [
            {"desc": f"Find LCD = {lcd}", "marks": 1},
            {"desc": f"Convert to equivalent fractions {a*m1}/{lcd} + {c*m2}/{lcd}", "marks": 1},
            {"desc": f"Final simplified answer {ans_latex}", "marks": 1},
        ],
        "hints": [
            f"Find the LCD of {b} and {d}, which is {lcd}.",
            f"Scale each fraction: {a}/{b} becomes {a*m1}/{lcd}, and {c}/{d} becomes {c*m2}/{lcd}.",
            f"Add the numerators: ({a*m1} + {c*m2})/{lcd}.",
        ],
    }


# ----------------------------------------------------------------------
# 11. Subtraction of Proper Fractions with Unlike Denominators
# ----------------------------------------------------------------------
def arch_11_subtraction_proper_fractions_unlike_denominators(rng: random.Random) -> Dict[str, Any]:
    b = rng.choice([3, 4, 6, 8, 10, 12])
    d = rng.choice([2, 5, 7, 9, 15])
    while b == d:
        d = rng.choice([2, 5, 7, 11])

    lcd = (b * d) // math.gcd(b, d)
    m1 = lcd // b
    m2 = lcd // d

    # Ensure a/b > c/d
    a = rng.randint(2, b - 1)
    c = rng.randint(1, d - 1)
    while a * m1 <= c * m2:
        a = min(b - 1, a + 1)
        c = max(1, c - 1)
        if a * m1 <= c * m2:
            a = b - 1
            c = 1

    diff = a * m1 - c * m2
    ans_latex = _frac_str(diff, lcd)
    ns, ds = _simplify(diff, lcd)
    ans_text = f"{ns}/{ds}"

    prompt = (
        f"Calculate the following difference and write the answer in simplest form:\n"
        f"\\[ \\frac{{{a}}}{{{b}}} - \\frac{{{c}}}{{{d}}} \\]"
    )
    sol = (
        f"**Step 1: Find the Lowest Common Denominator (LCD).**\n"
        f"\\[ \\text{{LCD}}({b}, {d}) = {lcd} \\]\n\n"
        f"**Step 2: Rewrite fractions with denominator {lcd}.**\n"
        f"\\[ \\frac{{{a * m1}}}{{{lcd}}} - \\frac{{{c * m2}}}{{{lcd}}} \\]\n\n"
        f"**Step 3: Subtract numerators and simplify.**\n"
        f"\\[ \\frac{{{a * m1} - {c * m2}}}{{{lcd}}} = \\frac{{{diff}}}{{{lcd}}} = {ans_latex} \\]"
    )
    return {
        "id": f"g9_frac_sub_unlike_{rng.randint(100000, 999999)}",
        "question_type": "fraction",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans_latex,
        "expected_answer": ans_latex,
        "sample_answer": ans_text,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "marking_schema": [
            {"desc": f"Find LCD = {lcd}", "marks": 1},
            {"desc": f"Rewrite with common denominator: {a*m1}/{lcd} - {c*m2}/{lcd}", "marks": 1},
            {"desc": f"Simplify difference to {ans_latex}", "marks": 1},
        ],
        "hints": [
            f"Find the LCD of {b} and {d}, which is {lcd}.",
            f"Convert to equivalent fractions with denominator {lcd}.",
            f"Subtract numerators: ({a*m1} - {c*m2})/{lcd} and simplify.",
        ],
    }


# ----------------------------------------------------------------------
# 12. Combined Addition and Subtraction of Three Fractions
# ----------------------------------------------------------------------
def arch_12_addition_and_subtraction_three_fractions(rng: random.Random) -> Dict[str, Any]:
    # Choose 3 denominators with a manageable LCD, e.g. 2, 3, 4 -> 12 or 2, 3, 6 -> 6 or 3, 4, 6 -> 12
    combo = rng.choice([
        (2, 3, 4),
        (3, 4, 6),
        (2, 5, 10),
        (4, 6, 12),
        (3, 5, 15),
    ])
    d1, d2, d3 = combo
    lcd = math.lcm(d1, d2, d3)

    n1 = rng.randint(1, d1 - 1)
    n2 = rng.randint(1, d2 - 1)
    # Ensure n1/d1 + n2/d2 > n3/d3
    scaled1 = n1 * (lcd // d1)
    scaled2 = n2 * (lcd // d2)
    max_n3_scaled = scaled1 + scaled2 - 1
    max_n3 = max(1, min(d3 - 1, max_n3_scaled // (lcd // d3)))
    n3 = rng.randint(1, max_n3)
    scaled3 = n3 * (lcd // d3)

    tot = scaled1 + scaled2 - scaled3
    ans_latex = _mixed_str(tot, lcd)
    ns, ds = _simplify(tot, lcd)
    ans_text = f"{ns}/{ds}"

    prompt = (
        f"Calculate the following expression. Give your answer in simplest form:\n"
        f"\\[ \\frac{{{n1}}}{{{d1}}} + \\frac{{{n2}}}{{{d2}}} - \\frac{{{n3}}}{{{d3}}} \\]"
    )
    sol = (
        f"**Step 1: Determine the LCD of {d1}, {d2}, and {d3}.**\n"
        f"\\[ \\text{{LCD}}({d1}, {d2}, {d3}) = {lcd} \\]\n\n"
        f"**Step 2: Convert all three fractions to equivalent fractions with denominator {lcd}.**\n"
        f"\\[ = \\frac{{{scaled1}}}{{{lcd}}} + \\frac{{{scaled2}}}{{{lcd}}} - \\frac{{{scaled3}}}{{{lcd}}} \\]\n\n"
        f"**Step 3: Combine numerators and simplify.**\n"
        f"\\[ = \\frac{{{scaled1} + {scaled2} - {scaled3}}}{{{lcd}}} = \\frac{{{tot}}}{{{lcd}}} = {ans_latex} \\]"
    )
    return {
        "id": f"g9_frac_add_sub_3_{rng.randint(100000, 999999)}",
        "question_type": "fraction",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans_latex,
        "expected_answer": ans_latex,
        "sample_answer": ans_text,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "marking_schema": [
            {"desc": f"Identify LCD = {lcd}", "marks": 1},
            {"desc": f"Express with common denominator ({scaled1} + {scaled2} - {scaled3})/{lcd}", "marks": 1},
            {"desc": f"Final simplified answer {ans_latex}", "marks": 1},
        ],
        "hints": [
            f"Find the LCD of all three denominators: {lcd}.",
            "Convert each fraction so it has this LCD.",
            "Add and subtract the numerators from left to right.",
        ],
    }


# ----------------------------------------------------------------------
# 13. Addition of Mixed Numbers with Unlike Denominators
# ----------------------------------------------------------------------
def arch_13_addition_of_mixed_numbers_with_unlike_denominators(rng: random.Random) -> Dict[str, Any]:
    w1 = rng.randint(1, 4)
    w2 = rng.randint(1, 4)
    b = rng.choice([2, 3, 4, 5])
    d = rng.choice([3, 4, 6, 8])
    while b == d:
        d = rng.choice([5, 6, 7])

    a = rng.randint(1, b - 1)
    c = rng.randint(1, d - 1)

    lcd = math.lcm(b, d)
    sa = a * (lcd // b)
    sc = c * (lcd // d)
    frac_sum = sa + sc
    extra_w = frac_sum // lcd
    rem_frac = frac_sum % lcd
    tot_w = w1 + w2 + extra_w

    ans_latex = _mixed_str(tot_w * lcd + rem_frac, lcd)
    ans_text = f"{tot_w} {rem_frac // math.gcd(rem_frac, lcd)}/{lcd // math.gcd(rem_frac, lcd)}" if rem_frac > 0 else str(tot_w)

    prompt = (
        f"Calculate the following sum of mixed numbers. Give the final answer as a mixed number in simplest form:\n"
        f"\\[ {w1}\\frac{{{a}}}{{{b}}} + {w2}\\frac{{{c}}}{{{d}}} \\]"
    )
    sol = (
        f"**Step 1: Add the whole numbers and fractional parts.**\n"
        f"Whole numbers: \\({w1} + {w2} = {w1 + w2}\\).\n"
        f"Fractional parts LCD({b}, {d}) = \\({lcd}\\):\n"
        f"\\[ \\frac{{{a}}}{{{b}}} + \\frac{{{c}}}{{{d}}} = \\frac{{{sa}}}{{{lcd}}} + \\frac{{{sc}}}{{{lcd}}} = \\frac{{{frac_sum}}}{{{lcd}}} \\]\n\n"
        f"**Step 2: Convert any improper fractional result to a mixed number and combine.**\n"
        f"\\[ \\frac{{{frac_sum}}}{{{lcd}}} = {extra_w}\\frac{{{rem_frac}}}{{{lcd}}} \\]\n"
        f"Total: \\({w1 + w2} + {extra_w}\\frac{{{rem_frac}}}{{{lcd}}} = {ans_latex}\\)"
    )
    return {
        "id": f"g9_frac_add_mix_{rng.randint(100000, 999999)}",
        "question_type": "mixed_number",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans_latex,
        "expected_answer": ans_latex,
        "sample_answer": ans_text,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "marking_schema": [
            {"desc": f"Add whole numbers ({w1} + {w2} = {w1+w2})", "marks": 1},
            {"desc": f"Find LCD {lcd} and add fractional parts", "marks": 1},
            {"desc": f"Combine and simplify to {ans_latex}", "marks": 1},
        ],
        "hints": [
            "Add the whole numbers first, or convert both mixed numbers into improper fractions.",
            f"The LCD for denominators {b} and {d} is {lcd}.",
            f"Combine whole and fractional parts into simplest form: {ans_latex}.",
        ],
    }


# ----------------------------------------------------------------------
# 14. Subtraction of Mixed Numbers Requiring Borrowing
# ----------------------------------------------------------------------
def arch_14_subtraction_of_mixed_numbers_requiring_borrowing(rng: random.Random) -> Dict[str, Any]:
    b = rng.choice([3, 4, 5, 6])
    d = rng.choice([2, 4, 8, 12])
    while b == d:
        d = rng.choice([7, 8, 9])
    lcd = math.lcm(b, d)

    # Ensure a/b < c/d so borrowing is mandatory
    # e.g. 5 1/4 - 2 2/3
    w1 = rng.randint(4, 8)
    w2 = rng.randint(1, w1 - 2)

    a = 1
    c = d - 1
    while a * (lcd // b) >= c * (lcd // d):
        c = min(d - 1, c + 1)
        a = max(1, a - 1)

    sa = a * (lcd // b)
    sc = c * (lcd // d)

    # Borrow 1 from w1
    borrowed_w1 = w1 - 1
    borrowed_num = sa + lcd
    diff_frac = borrowed_num - sc
    final_w = borrowed_w1 - w2
    tot_num = final_w * lcd + diff_frac

    ans_latex = _mixed_str(tot_num, lcd)
    ns, ds = _simplify(diff_frac, lcd)
    ans_text = f"{final_w} {ns}/{ds}" if diff_frac > 0 else str(final_w)

    prompt = (
        f"Calculate the difference. Give your answer as a mixed number in simplest form:\n"
        f"\\[ {w1}\\frac{{{a}}}{{{b}}} - {w2}\\frac{{{c}}}{{{d}}} \\]"
    )
    sol = (
        f"**Step 1: Find the common denominator.**\n"
        f"\\[ \\text{{LCD}}({b}, {d}) = {lcd} \\]\n"
        f"\\[ = {w1}\\frac{{{sa}}}{{{lcd}}} - {w2}\\frac{{{sc}}}{{{lcd}}} \\]\n\n"
        f"**Step 2: Notice that \\({sa} < {sc}\\), so borrow \\(1 = \\frac{{{lcd}}}{{{lcd}}}\\) from {w1}.**\n"
        f"\\[ {w1}\\frac{{{sa}}}{{{lcd}}} = {borrowed_w1}\\frac{{{sa} + {lcd}}}{{{lcd}}} = {borrowed_w1}\\frac{{{borrowed_num}}}{{{lcd}}} \\]\n\n"
        f"**Step 3: Subtract whole numbers and fractional parts.**\n"
        f"\\[ ({borrowed_w1} - {w2}) + \\frac{{{borrowed_num} - {sc}}}{{{lcd}}} = {final_w}\\frac{{{diff_frac}}}{{{lcd}}} = {ans_latex} \\]"
    )
    return {
        "id": f"g9_frac_sub_borrow_{rng.randint(100000, 999999)}",
        "question_type": "mixed_number",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans_latex,
        "expected_answer": ans_latex,
        "sample_answer": ans_text,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "marking_schema": [
            {"desc": f"Find LCD = {lcd} and identify need to borrow", "marks": 1},
            {"desc": f"Borrow 1 to get {borrowed_w1} {borrowed_num}/{lcd}", "marks": 1},
            {"desc": f"Complete subtraction to get {ans_latex}", "marks": 1},
        ],
        "hints": [
            f"Convert fractions to common denominator {lcd}.",
            f"Because {sa} is smaller than {sc}, borrow 1 whole from {w1}.",
            f"1 whole is {lcd}/{lcd}, giving {borrowed_w1} {borrowed_num}/{lcd}.",
        ],
    }


# ----------------------------------------------------------------------
# 15. Multiplication of Fraction by Whole Number
# ----------------------------------------------------------------------
def arch_15_multiplication_fraction_by_whole_number(rng: random.Random) -> Dict[str, Any]:
    b = rng.choice([3, 4, 5, 6, 8, 10])
    a = rng.randint(1, b - 1)
    while math.gcd(a, b) != 1:
        a = (a % (b - 1)) + 1

    # Whole number that has some common factors with b
    factor = rng.choice([2, 3, 4, 5, 6])
    k = b * factor + rng.choice([0, rng.randint(1, b - 1)])
    if k == 0:
        k = b * 2

    prod_num = a * k
    ans_latex = _mixed_str(prod_num, b)
    ns, ds = _simplify(prod_num, b)
    ans_text = f"{ns}/{ds}" if ds > 1 else str(ns)

    prompt = (
        f"Calculate the following product. Give your answer as a simplified fraction or mixed number:\n"
        f"\\[ \\frac{{{a}}}{{{b}}} \\times {k} \\]"
    )
    sol = (
        f"**Step 1: Write the whole number as a fraction over 1.**\n"
        f"\\[ \\frac{{{a}}}{{{b}}} \\times \\frac{{{k}}}{{1}} = \\frac{{{a} \\times {k}}}{{{b} \\times 1}} = \\frac{{{prod_num}}}{{{b}}} \\]\n\n"
        f"**Step 2: Simplify and convert to mixed number if improper.**\n"
        f"\\[ = {ans_latex} \\]"
    )
    return {
        "id": f"g9_frac_mul_whole_{rng.randint(100000, 999999)}",
        "question_type": "fraction",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans_latex,
        "expected_answer": ans_latex,
        "sample_answer": ans_text,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"Multiply numerator by whole number: {a} × {k} = {prod_num}", "marks": 1},
            {"desc": f"Simplify fraction to {ans_latex}", "marks": 1},
        ],
        "hints": [
            "Multiply the top number by the whole number, then divide by the denominator.",
            f"Product is ({a} × {k}) / {b} = {prod_num}/{b}.",
            f"Simplify to {ans_latex}.",
        ],
    }


# ----------------------------------------------------------------------
# 16. Multiplication of Two Proper Fractions: Cross-Cancellation
# ----------------------------------------------------------------------
def arch_16_multiplication_two_proper_fractions_cross_cancellation(rng: random.Random) -> Dict[str, Any]:
    # Design fractions with cross factors: e.g. a/b * c/d where gcd(a, d) > 1 and gcd(c, b) > 1
    cf1 = rng.choice([2, 3, 5])
    cf2 = rng.choice([3, 4, 7])

    a1 = rng.choice([1, 2])
    d1 = rng.choice([1, 2, 3])
    c1 = rng.choice([1, 2])
    b1 = rng.choice([1, 3, 4])

    a = a1 * cf1
    d = d1 * cf1
    c = c1 * cf2
    b = b1 * cf2

    # Ensure proper fractions
    if a >= b:
        b = a + cf2
    if c >= d:
        d = c + cf1

    num = a * c
    den = b * d
    ans_latex = _frac_str(num, den)
    ns, ds = _simplify(num, den)
    ans_text = f"{ns}/{ds}"

    prompt = (
        f"Calculate the product by cross-cancelling common factors first. Give the answer in simplest form:\n"
        f"\\[ \\frac{{{a}}}{{{b}}} \\times \\frac{{{c}}}{{{d}}} \\]"
    )
    sol = (
        f"**Step 1: Identify common factors diagonally for cross-cancellation.**\n"
        f"Between \\({a}\\) and \\({d}\\), divide by common factor \\({cf1}\\).\n"
        f"Between \\({c}\\) and \\({b}\\), divide by common factor \\({math.gcd(c, b)}\\).\n\n"
        f"**Step 2: Multiply the simplified numerators and denominators.**\n"
        f"\\[ \\frac{{{a} \\times {c}}}{{{b} \\times {d}}} = \\frac{{{num}}}{{{den}}} = {ans_latex} \\]"
    )
    return {
        "id": f"g9_frac_mul_cross_{rng.randint(100000, 999999)}",
        "question_type": "fraction",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans_latex,
        "expected_answer": ans_latex,
        "sample_answer": ans_text,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": "Cross-cancel common factors between numerators and denominators", "marks": 1},
            {"desc": f"Final simplified product {ans_latex}", "marks": 1},
        ],
        "hints": [
            "Cancel out common factors between any numerator and any denominator before multiplying.",
            "Multiply remaining numerators together and remaining denominators together.",
            f"The final simplified fraction is {ans_text}.",
        ],
    }


# ----------------------------------------------------------------------
# 17. Multiplication of Three Fractions Chained
# ----------------------------------------------------------------------
def arch_17_multiplication_three_fractions_chained(rng: random.Random) -> Dict[str, Any]:
    # a/b * c/d * e/f
    f1 = (rng.choice([2, 3]), rng.choice([4, 5]))
    f2 = (rng.choice([1, 5]), rng.choice([6, 7]))
    f3 = (rng.choice([2, 7]), rng.choice([8, 9]))

    a, b = f1
    c, d = f2
    e, f = f3

    num = a * c * e
    den = b * d * f
    ans_latex = _frac_str(num, den)
    ns, ds = _simplify(num, den)
    ans_text = f"{ns}/{ds}"

    prompt = (
        f"Evaluate the following product of three common fractions in simplest form:\n"
        f"\\[ \\frac{{{a}}}{{{b}}} \\times \\frac{{{c}}}{{{d}}} \\times \\frac{{{e}}}{{{f}}} \\]"
    )
    sol = (
        f"**Step 1: Multiply all numerators and all denominators.**\n"
        f"\\[ \\frac{{{a} \\times {c} \\times {e}}}{{{b} \\times {d} \\times {f}}} = \\frac{{{num}}}{{{den}}} \\]\n\n"
        f"**Step 2: Simplify by dividing by the HCF.**\n"
        f"\\[ \\text{{HCF}}({num}, {den}) = {math.gcd(num, den)} \\]\n"
        f"\\[ = {ans_latex} \\]"
    )
    return {
        "id": f"g9_frac_mul_3_{rng.randint(100000, 999999)}",
        "question_type": "fraction",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans_latex,
        "expected_answer": ans_latex,
        "sample_answer": ans_text,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"Multiply numerators and denominators to get {num}/{den}", "marks": 1},
            {"desc": f"Simplify to {ans_latex}", "marks": 1},
        ],
        "hints": [
            "Multiply all three top numbers together, and all three bottom numbers together.",
            "Cross-cancel common factors beforehand to make arithmetic simpler.",
            f"The answer is {ans_text}.",
        ],
    }


# ----------------------------------------------------------------------
# 18. Multiplication of Mixed Numbers
# ----------------------------------------------------------------------
def arch_18_multiplication_mixed_numbers(rng: random.Random) -> Dict[str, Any]:
    w1 = rng.randint(1, 3)
    b = rng.choice([2, 3, 4, 5])
    a = rng.randint(1, b - 1)
    while math.gcd(a, b) != 1:
        a = (a % (b - 1)) + 1

    w2 = rng.randint(1, 3)
    d = rng.choice([2, 3, 4, 5])
    c = rng.randint(1, d - 1)
    while math.gcd(c, d) != 1:
        c = (c % (d - 1)) + 1

    imp1_n = w1 * b + a
    imp2_n = w2 * d + c

    prod_n = imp1_n * imp2_n
    prod_d = b * d

    ans_latex = _mixed_str(prod_n, prod_d)
    ns, ds = _simplify(prod_n, prod_d)
    ans_text = f"{ns}/{ds}"

    prompt = (
        f"Calculate the product of the mixed numbers. Write the final answer as a mixed number in simplest form:\n"
        f"\\[ {w1}\\frac{{{a}}}{{{b}}} \\times {w2}\\frac{{{c}}}{{{d}}} \\]"
    )
    sol = (
        f"**Step 1: Convert both mixed numbers to improper fractions.**\n"
        f"\\[ {w1}\\frac{{{a}}}{{{b}}} = \\frac{{{imp1_n}}}{{{b}}}, \\quad {w2}\\frac{{{c}}}{{{d}}} = \\frac{{{imp2_n}}}{{{d}}} \\]\n\n"
        f"**Step 2: Multiply numerators and denominators.**\n"
        f"\\[ \\frac{{{imp1_n}}}{{{b}}} \\times \\frac{{{imp2_n}}}{{{d}}} = \\frac{{{prod_n}}}{{{prod_d}}} \\]\n\n"
        f"**Step 3: Simplify and write as a mixed number.**\n"
        f"\\[ = {ans_latex} \\]"
    )
    return {
        "id": f"g9_frac_mul_mix_{rng.randint(100000, 999999)}",
        "question_type": "mixed_number",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans_latex,
        "expected_answer": ans_latex,
        "sample_answer": ans_text,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "marking_schema": [
            {"desc": f"Convert to improper fractions {imp1_n}/{b} and {imp2_n}/{d}", "marks": 1},
            {"desc": f"Multiply to obtain {prod_n}/{prod_d}", "marks": 1},
            {"desc": f"Convert to simplest mixed number {ans_latex}", "marks": 1},
        ],
        "hints": [
            "Never multiply whole numbers and fractions separately; convert to improper fractions first.",
            f"Convert to {imp1_n}/{b} × {imp2_n}/{d}.",
            f"Multiply and simplify to {ans_latex}.",
        ],
    }


# ----------------------------------------------------------------------
# 19. Reciprocal of Fractions and Mixed Numbers
# ----------------------------------------------------------------------
def arch_19_reciprocal_of_fractions_and_mixed_numbers(rng: random.Random) -> Dict[str, Any]:
    kind = rng.choice(["fraction", "mixed_number"])
    if kind == "fraction":
        d = rng.choice([3, 4, 5, 7, 8, 9, 11])
        n = rng.randint(2, d - 1)
        while math.gcd(n, d) != 1:
            n = (n % (d - 1)) + 1
        given_str = f"\\frac{{{n}}}{{{d}}}"
        recip_n = d
        recip_d = n
        ans_latex = f"\\frac{{{recip_n}}}{{{recip_d}}}"
        ans_text = f"{recip_n}/{recip_d}"
        sol = (
            f"**Definition of Reciprocal:**\n"
            f"The reciprocal of a non-zero fraction \\(\\frac{{a}}{{b}}\\) is \\(\\frac{{b}}{{a}}\\), "
            f"such that their product is 1.\n\n"
            f"Reciprocal of \\({given_str}\\) is:\n"
            f"\\[ = {ans_latex} \\]"
        )
    else:
        w = rng.randint(2, 5)
        d = rng.choice([2, 3, 4, 5])
        r = rng.randint(1, d - 1)
        while math.gcd(r, d) != 1:
            r = (r % (d - 1)) + 1
        imp_n = w * d + r
        given_str = f"{w}\\frac{{{r}}}{{{d}}}"
        recip_n = d
        recip_d = imp_n
        ans_latex = f"\\frac{{{recip_n}}}{{{recip_d}}}"
        ans_text = f"{recip_n}/{recip_d}"
        sol = (
            f"**Step 1: Convert the mixed number to an improper fraction.**\n"
            f"\\[ {given_str} = \\frac{{{imp_n}}}{{{d}}} \\]\n\n"
            f"**Step 2: Invert the fraction to find its reciprocal.**\n"
            f"\\[ \\text{{Reciprocal}} = {ans_latex} \\]"
        )

    prompt = f"Determine the reciprocal (multiplicative inverse) of the number:\n\\[ {given_str} \\]"
    return {
        "id": f"g9_frac_recip_{rng.randint(100000, 999999)}",
        "question_type": "fraction",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans_latex,
        "expected_answer": ans_latex,
        "sample_answer": ans_text,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"Correct conversion to improper fraction if applicable", "marks": 1},
            {"desc": f"State reciprocal as {ans_latex}", "marks": 1},
        ],
        "hints": [
            "The reciprocal of a fraction is obtained by swapping its numerator and denominator.",
            "If it is a mixed number, convert it to an improper fraction first.",
            f"The reciprocal is {ans_text}.",
        ],
    }


# ----------------------------------------------------------------------
# 20. Division of Proper Fraction by Proper Fraction
# ----------------------------------------------------------------------
def arch_20_division_proper_fraction_by_proper_fraction(rng: random.Random) -> Dict[str, Any]:
    b = rng.choice([3, 4, 5, 6, 8])
    a = rng.randint(1, b - 1)
    while math.gcd(a, b) != 1:
        a = (a % (b - 1)) + 1

    d = rng.choice([2, 3, 5, 7, 9])
    c = rng.randint(1, d - 1)
    while math.gcd(c, d) != 1:
        c = (c % (d - 1)) + 1

    # a/b / c/d = a/b * d/c
    num = a * d
    den = b * c
    ans_latex = _mixed_str(num, den)
    ns, ds = _simplify(num, den)
    ans_text = f"{ns}/{ds}"

    prompt = (
        f"Calculate the following quotient and express the answer in simplest form:\n"
        f"\\[ \\frac{{{a}}}{{{b}}} \\div \\frac{{{c}}}{{{d}}} \\]"
    )
    sol = (
        f"**Step 1: Multiply by the reciprocal of the divisor.**\n"
        f"\\[ \\frac{{{a}}}{{{b}}} \\div \\frac{{{c}}}{{{d}}} = \\frac{{{a}}}{{{b}}} \\times \\frac{{{d}}}{{{c}}} \\]\n\n"
        f"**Step 2: Multiply numerators and denominators.**\n"
        f"\\[ = \\frac{{{a} \\times {d}}}{{{b} \\times {c}}} = \\frac{{{num}}}{{{den}}} \\]\n\n"
        f"**Step 3: Simplify to lowest terms.**\n"
        f"\\[ = {ans_latex} \\]"
    )
    return {
        "id": f"g9_frac_div_prop_{rng.randint(100000, 999999)}",
        "question_type": "fraction",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans_latex,
        "expected_answer": ans_latex,
        "sample_answer": ans_text,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"Invert divisor to multiply: ({a}/{b}) × ({d}/{c})", "marks": 1},
            {"desc": f"Multiply and simplify to {ans_latex}", "marks": 1},
        ],
        "hints": [
            "Dividing by a fraction is the same as multiplying by its reciprocal.",
            f"Rewrite as {a}/{b} × {d}/{c}.",
            f"Multiply across and simplify to {ans_latex}.",
        ],
    }


# ----------------------------------------------------------------------
# 21. Division of Mixed Numbers
# ----------------------------------------------------------------------
def arch_21_division_mixed_number_by_fraction_or_mixed_number(rng: random.Random) -> Dict[str, Any]:
    w1 = rng.randint(2, 5)
    b = rng.choice([2, 3, 4, 5])
    a = rng.randint(1, b - 1)
    while math.gcd(a, b) != 1:
        a = (a % (b - 1)) + 1

    w2 = rng.randint(1, 3)
    d = rng.choice([2, 3, 4])
    c = rng.randint(1, d - 1)
    while math.gcd(c, d) != 1:
        c = (c % (d - 1)) + 1

    imp1_n = w1 * b + a
    imp2_n = w2 * d + c

    num = imp1_n * d
    den = b * imp2_n
    ans_latex = _mixed_str(num, den)
    ns, ds = _simplify(num, den)
    ans_text = f"{ns}/{ds}"

    prompt = (
        f"Calculate the following division of mixed numbers. Give the answer in simplest form:\n"
        f"\\[ {w1}\\frac{{{a}}}{{{b}}} \\div {w2}\\frac{{{c}}}{{{d}}} \\]"
    )
    sol = (
        f"**Step 1: Convert both mixed numbers to improper fractions.**\n"
        f"\\[ {w1}\\frac{{{a}}}{{{b}}} = \\frac{{{imp1_n}}}{{{b}}}, \\quad {w2}\\frac{{{c}}}{{{d}}} = \\frac{{{imp2_n}}}{{{d}}} \\]\n\n"
        f"**Step 2: Change division to multiplication by the reciprocal.**\n"
        f"\\[ \\frac{{{imp1_n}}}{{{b}}} \\div \\frac{{{imp2_n}}}{{{d}}} = \\frac{{{imp1_n}}}{{{b}}} \\times \\frac{{{d}}}{{{imp2_n}}} \\]\n\n"
        f"**Step 3: Multiply and simplify.**\n"
        f"\\[ = \\frac{{{imp1_n} \\times {d}}}{{{b} \\times {imp2_n}}} = \\frac{{{num}}}{{{den}}} = {ans_latex} \\]"
    )
    return {
        "id": f"g9_frac_div_mix_{rng.randint(100000, 999999)}",
        "question_type": "mixed_number",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans_latex,
        "expected_answer": ans_latex,
        "sample_answer": ans_text,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "marking_schema": [
            {"desc": f"Convert to improper fractions {imp1_n}/{b} and {imp2_n}/{d}", "marks": 1},
            {"desc": f"Invert divisor: ({imp1_n}/{b}) × ({d}/{imp2_n})", "marks": 1},
            {"desc": f"Simplify quotient to {ans_latex}", "marks": 1},
        ],
        "hints": [
            "Convert both mixed numbers to improper fractions first.",
            "Multiply the first fraction by the reciprocal of the second fraction.",
            f"The final answer is {ans_latex}.",
        ],
    }


# ----------------------------------------------------------------------
# 22. Square of Proper Fraction and Mixed Number
# ----------------------------------------------------------------------
def arch_22_square_of_proper_fraction_and_mixed_number(rng: random.Random) -> Dict[str, Any]:
    kind = rng.choice(["proper", "mixed"])
    if kind == "proper":
        d = rng.choice([3, 4, 5, 6, 7, 8])
        n = rng.randint(1, d - 1)
        while math.gcd(n, d) != 1:
            n = (n % (d - 1)) + 1

        sq_n = n ** 2
        sq_d = d ** 2
        ans_latex = f"\\frac{{{sq_n}}}{{{sq_d}}}"
        ans_text = f"{sq_n}/{sq_d}"
        prompt = (
            f"Calculate the square of the common fraction in simplest form:\n"
            f"\\[ \\left( \\frac{{{n}}}{{{d}}} \\right)^2 \\]"
        )
        sol = (
            f"**Step 1: Apply the power rule to both numerator and denominator.**\n"
            f"\\[ \\left( \\frac{{{n}}}{{{d}}} \\right)^2 = \\frac{{{n}^2}}{{{d}^2}} \\]\n\n"
            f"**Step 2: Calculate the squares.**\n"
            f"\\[ = \\frac{{{sq_n}}}{{{sq_d}}} = {ans_latex} \\]"
        )
    else:
        w = rng.randint(1, 3)
        d = rng.choice([2, 3, 4])
        r = rng.randint(1, d - 1)
        while math.gcd(r, d) != 1:
            r = (r % (d - 1)) + 1
        imp_n = w * d + r
        sq_n = imp_n ** 2
        sq_d = d ** 2
        ans_latex = _mixed_str(sq_n, sq_d)
        ans_text = f"{sq_n}/{sq_d}"
        prompt = (
            f"Calculate the square of the mixed number. Give your answer as a mixed number in simplest form:\n"
            f"\\[ \\left( {w}\\frac{{{r}}}{{{d}}} \\right)^2 \\]"
        )
        sol = (
            f"**Step 1: Convert the mixed number to an improper fraction.**\n"
            f"\\[ {w}\\frac{{{r}}}{{{d}}} = \\frac{{{imp_n}}}{{{d}}} \\]\n\n"
            f"**Step 2: Square both numerator and denominator.**\n"
            f"\\[ \\left( \\frac{{{imp_n}}}{{{d}}} \\right)^2 = \\frac{{{sq_n}}}{{{sq_d}}} = {ans_latex} \\]"
        )

    return {
        "id": f"g9_frac_sq_{rng.randint(100000, 999999)}",
        "question_type": "fraction",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans_latex,
        "expected_answer": ans_latex,
        "sample_answer": ans_text,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": "Apply exponent to numerator and denominator", "marks": 1},
            {"desc": f"Calculate correct square {ans_latex}", "marks": 1},
        ],
        "hints": [
            "To square a fraction, square the numerator and square the denominator.",
            "If it is a mixed number, convert to an improper fraction before squaring.",
            f"The answer is {ans_latex}.",
        ],
    }


# ----------------------------------------------------------------------
# 23. Cube of Proper Fraction
# ----------------------------------------------------------------------
def arch_23_cube_of_proper_fraction(rng: random.Random) -> Dict[str, Any]:
    d = rng.choice([2, 3, 4, 5])
    n = rng.randint(1, d - 1)
    while math.gcd(n, d) != 1:
        n = (n % (d - 1)) + 1

    cube_n = n ** 3
    cube_d = d ** 3
    ans_latex = f"\\frac{{{cube_n}}}{{{cube_d}}}"
    ans_text = f"{cube_n}/{cube_d}"

    prompt = (
        f"Evaluate the cube of the common fraction:\n"
        f"\\[ \\left( \\frac{{{n}}}{{{d}}} \\right)^3 \\]"
    )
    sol = (
        f"**Step 1: Apply the cube exponent to both numerator and denominator.**\n"
        f"\\[ \\left( \\frac{{{n}}}{{{d}}} \\right)^3 = \\frac{{{n}^3}}{{{d}^3}} \\]\n\n"
        f"**Step 2: Calculate the cubes.**\n"
        f"\\[ {n}^3 = {cube_n}, \\quad {d}^3 = {cube_d} \\]\n\n"
        f"**Step 3: State the final fraction.**\n"
        f"\\[ = {ans_latex} \\]"
    )
    return {
        "id": f"g9_frac_cube_{rng.randint(100000, 999999)}",
        "question_type": "fraction",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans_latex,
        "expected_answer": ans_latex,
        "sample_answer": ans_text,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"Apply cube: ({n}^3)/({d}^3)", "marks": 1},
            {"desc": f"State result {ans_latex}", "marks": 1},
        ],
        "hints": [
            "To cube a fraction, multiply the numerator by itself 3 times, and denominator by itself 3 times.",
            f"Numerator: {n} × {n} × {n} = {cube_n}.",
            f"Denominator: {d} × {d} × {d} = {cube_d}.",
        ],
    }


# ----------------------------------------------------------------------
# 24. Square Root of Proper Fraction and Mixed Number
# ----------------------------------------------------------------------
def arch_24_square_root_of_proper_fraction_and_mixed_number(rng: random.Random) -> Dict[str, Any]:
    kind = rng.choice(["proper", "mixed"])
    if kind == "proper":
        q = rng.choice([2, 3, 4, 5, 6, 7, 8, 9, 10, 12])
        p = rng.randint(1, q - 1)
        while math.gcd(p, q) != 1:
            p = (p % (q - 1)) + 1

        sq_p = p ** 2
        sq_q = q ** 2
        ans_latex = f"\\frac{{{p}}}{{{q}}}"
        ans_text = f"{p}/{q}"

        prompt = (
            f"Calculate the square root of the fraction in simplest form:\n"
            f"\\[ \\sqrt{{\\frac{{{sq_p}}}{{{sq_q}}}}} \\]"
        )
        sol = (
            f"**Step 1: Take the square root of numerator and denominator separately.**\n"
            f"\\[ \\sqrt{{\\frac{{{sq_p}}}{{{sq_q}}}}} = \\frac{{\\sqrt{{{sq_p}}}}}{{\\sqrt{{{sq_q}}}}} \\]\n\n"
            f"**Step 2: Evaluate each square root.**\n"
            f"\\[ = \\frac{{{p}}}{{{q}}} = {ans_latex} \\]"
        )
    else:
        # Mixed number with perfect square improper numerator: e.g. 1 9/16 = 25/16 -> 5/4 = 1 1/4
        # or 2 7/9 = 25/9 -> 5/3 = 1 2/3
        # or 1 7/9 = 16/9 -> 4/3 = 1 1/3
        # or 3 1/16 = 49/16 -> 7/4 = 1 3/4
        mixed_examples = [
            (1, 9, 16, 5, 4),   # sqrt(25/16) = 5/4 = 1 1/4
            (2, 7, 9, 5, 3),    # sqrt(25/9) = 5/3 = 1 2/3
            (1, 7, 9, 4, 3),    # sqrt(16/9) = 4/3 = 1 1/3
            (3, 1, 16, 7, 4),   # sqrt(49/16) = 7/4 = 1 3/4
            (2, 14, 25, 8, 5),  # sqrt(64/25) = 8/5 = 1 3/5
            (1, 24, 25, 7, 5),  # sqrt(49/25) = 7/5 = 1 2/5
        ]
        w, r, d, p, q = rng.choice(mixed_examples)
        imp_n = w * d + r
        ans_latex = _mixed_str(p, q)
        ans_text = f"{p // q} {p % q}/{q}"

        prompt = (
            f"Calculate the square root of the mixed number. Give the answer as a mixed number in simplest form:\n"
            f"\\[ \\sqrt{{{w}\\frac{{{r}}}{{{d}}}}} \\]"
        )
        sol = (
            f"**Step 1: Convert the mixed number to an improper fraction.**\n"
            f"\\[ {w}\\frac{{{r}}}{{{d}}} = \\frac{{{imp_n}}}{{{d}}} \\]\n\n"
            f"**Step 2: Take the square root of the improper fraction.**\n"
            f"\\[ \\sqrt{{\\frac{{{imp_n}}}{{{d}}}}} = \\frac{{\\sqrt{{{imp_n}}}}}{{\\sqrt{{{d}}}}} = \\frac{{{p}}}{{{q}}} \\]\n\n"
            f"**Step 3: Convert to a mixed number.**\n"
            f"\\[ \\frac{{{p}}}{{{q}}} = {ans_latex} \\]"
        )

    return {
        "id": f"g9_frac_sqrt_{rng.randint(100000, 999999)}",
        "question_type": "fraction",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans_latex,
        "expected_answer": ans_latex,
        "sample_answer": ans_text,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": "Convert to improper fraction if needed and take square root of top and bottom", "marks": 1},
            {"desc": f"State final root {ans_latex}", "marks": 1},
        ],
        "hints": [
            "Square root of a fraction is the square root of the numerator divided by the square root of the denominator.",
            "For mixed numbers, always convert to an improper fraction first before taking the square root.",
            f"The answer is {ans_latex}.",
        ],
    }


# ----------------------------------------------------------------------
# 25. Cube Root of Proper Fraction
# ----------------------------------------------------------------------
def arch_25_cube_root_of_proper_fraction(rng: random.Random) -> Dict[str, Any]:
    kind = rng.choice(["proper", "mixed"])
    if kind == "proper":
        q = rng.choice([2, 3, 4, 5])
        p = rng.randint(1, q - 1)
        while math.gcd(p, q) != 1:
            p = (p % (q - 1)) + 1

        cb_p = p ** 3
        cb_q = q ** 3
        ans_latex = f"\\frac{{{p}}}{{{q}}}"
        ans_text = f"{p}/{q}"

        prompt = (
            f"Evaluate the cube root of the common fraction in simplest form:\n"
            f"\\[ \\sqrt[3]{{\\frac{{{cb_p}}}{{{cb_q}}}}} \\]"
        )
        sol = (
            f"**Step 1: Apply the cube root to both numerator and denominator.**\n"
            f"\\[ \\sqrt[3]{{\\frac{{{cb_p}}}{{{cb_q}}}}} = \\frac{{\\sqrt[3]{{{cb_p}}}}}{{\\sqrt[3]{{{cb_q}}}}} \\]\n\n"
            f"**Step 2: Evaluate the cube roots.**\n"
            f"\\[ \\sqrt[3]{{{cb_p}}} = {p}, \\quad \\sqrt[3]{{{cb_q}}} = {q} \\]\n\n"
            f"**Step 3: State the resulting fraction.**\n"
            f"\\[ = {ans_latex} \\]"
        )
    else:
        # Mixed number examples: 1 61/64 = 125/64 -> 5/4 = 1 1/4
        # or 3 3/8 = 27/8 -> 3/2 = 1 1/2
        mixed_cubes = [
            (1, 61, 64, 5, 4),  # cbrt(125/64) = 5/4 = 1 1/4
            (3, 3, 8, 3, 2),    # cbrt(27/8) = 3/2 = 1 1/2
            (1, 19, 27, 4, 3),  # cbrt(64/27) = 4/3 = 1 1/3
        ]
        w, r, d, p, q = rng.choice(mixed_cubes)
        imp_n = w * d + r
        ans_latex = _mixed_str(p, q)
        ans_text = f"{p // q} {p % q}/{q}"

        prompt = (
            f"Evaluate the cube root of the mixed number. Give your answer as a mixed number in simplest form:\n"
            f"\\[ \\sqrt[3]{{{w}\\frac{{{r}}}{{{d}}}}} \\]"
        )
        sol = (
            f"**Step 1: Convert the mixed number to an improper fraction.**\n"
            f"\\[ {w}\\frac{{{r}}}{{{d}}} = \\frac{{{imp_n}}}{{{d}}} \\]\n\n"
            f"**Step 2: Take the cube root of numerator and denominator.**\n"
            f"\\[ \\sqrt[3]{{\\frac{{{imp_n}}}{{{d}}}}} = \\frac{{\\sqrt[3]{{{imp_n}}}}}{{\\sqrt[3]{{{d}}}}} = \\frac{{{p}}}{{{q}}} \\]\n\n"
            f"**Step 3: Write as a mixed number.**\n"
            f"\\[ = {ans_latex} \\]"
        )

    return {
        "id": f"g9_frac_cbrt_{rng.randint(100000, 999999)}",
        "question_type": "fraction",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans_latex,
        "expected_answer": ans_latex,
        "sample_answer": ans_text,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": "Convert to improper fraction if applicable and apply cube root", "marks": 1},
            {"desc": f"State final cube root {ans_latex}", "marks": 1},
        ],
        "hints": [
            "Take the cube root of the top and bottom separately.",
            "If given a mixed number, convert to an improper fraction first.",
            f"The result is {ans_latex}.",
        ],
    }
