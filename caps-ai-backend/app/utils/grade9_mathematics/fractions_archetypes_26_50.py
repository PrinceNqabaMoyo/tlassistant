"""Grade 9 Mathematics - Common Fractions Archetypes 26 to 50.
Grounded in curriculum_docs_auto/Mathematics_Gr9/Term 2/01. Fractions.md:
BODMAS with fractions and mixed numbers, powers and roots in expressions,
complex fractions, fractions of quantities and measurement units,
percentages as fractions, percentage increase/decrease, reverse fractions,
authentic South African word problems (fuel tanks, budgets, recipes, sharing, work rates),
visual pie chart interpretation, algebraic fraction evaluation, error analysis, and capstone.
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional, Tuple

from .fractions_svg import (
    draw_pie_fraction_svg,
    draw_tank_gauge_svg,
)


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
# 26. Order of Operations: Brackets, Multiplication, Addition
# ----------------------------------------------------------------------
def arch_26_order_of_operations_brackets_multiplication_addition(rng: random.Random) -> Dict[str, Any]:
    # (a/b + c/d) * e/f
    b = rng.choice([2, 3, 4])
    d = rng.choice([3, 5, 6])
    while b == d:
        d = 5
    a = 1
    c = 1

    lcd = math.lcm(b, d)
    sum_num = a * (lcd // b) + c * (lcd // d)

    e = rng.choice([2, 3, 4, 5])
    f = rng.choice([3, 7, 8])

    prod_num = sum_num * e
    prod_den = lcd * f

    ans_latex = _mixed_str(prod_num, prod_den)
    ns, ds = _simplify(prod_num, prod_den)
    ans_text = f"{ns}/{ds}"

    prompt = (
        f"Apply the correct order of operations (BODMAS) to calculate the value of:\n"
        f"\\[ \\left( \\frac{{{a}}}{{{b}}} + \\frac{{{c}}}{{{d}}} \\right) \\times \\frac{{{e}}}{{{f}}} \\]"
    )
    sol = (
        f"**Step 1: Simplify the expression inside the brackets.**\n"
        f"Find LCD({b}, {d}) = \\({lcd}\\):\n"
        f"\\[ \\frac{{{a}}}{{{b}}} + \\frac{{{c}}}{{{d}}} = \\frac{{{a * (lcd // b)}}}{{{lcd}}} + \\frac{{{c * (lcd // d)}}}{{{lcd}}} = \\frac{{{sum_num}}}{{{lcd}}} \\]\n\n"
        f"**Step 2: Multiply by \\(\\frac{{{e}}}{{{f}}}\\).**\n"
        f"\\[ \\frac{{{sum_num}}}{{{lcd}}} \\times \\frac{{{e}}}{{{f}}} = \\frac{{{prod_num}}}{{{prod_den}}} \\]\n\n"
        f"**Step 3: Simplify to lowest terms.**\n"
        f"\\[ = {ans_latex} \\]"
    )
    return {
        "id": f"g9_frac_bodmas_brack_{rng.randint(100000, 999999)}",
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
            {"desc": f"Evaluate bracket addition to get {sum_num}/{lcd}", "marks": 1},
            {"desc": f"Multiply by {e}/{f} to get {prod_num}/{prod_den}", "marks": 1},
            {"desc": f"Simplify to {ans_latex}", "marks": 1},
        ],
        "hints": [
            "BODMAS requires solving expressions inside brackets first.",
            f"Add the fractions in the brackets using LCD {lcd}.",
            f"Multiply the sum by {e}/{f} and simplify.",
        ],
    }


# ----------------------------------------------------------------------
# 27. Order of Operations: Powers and Roots with Operations
# ----------------------------------------------------------------------
def arch_27_order_of_operations_powers_roots_with_operations(rng: random.Random) -> Dict[str, Any]:
    # sqrt(p^2/q^2) + (c/d)^2
    p = rng.choice([1, 2, 3])
    q = rng.choice([2, 4, 5])
    while math.gcd(p, q) != 1:
        p = 1

    c = 1
    d = rng.choice([2, 3])

    sq_p = p ** 2
    sq_q = q ** 2
    p2_c = c ** 2
    p2_d = d ** 2

    # p/q + p2_c / p2_d
    lcd = math.lcm(q, p2_d)
    tot_num = p * (lcd // q) + p2_c * (lcd // p2_d)

    ans_latex = _mixed_str(tot_num, lcd)
    ns, ds = _simplify(tot_num, lcd)
    ans_text = f"{ns}/{ds}"

    prompt = (
        f"Evaluate the mathematical expression using the order of operations:\n"
        f"\\[ \\sqrt{{\\frac{{{sq_p}}}{{{sq_q}}}}} + \\left( \\frac{{{c}}}{{{d}}} \\right)^2 \\]"
    )
    sol = (
        f"**Step 1: Evaluate the square root and the power.**\n"
        f"\\[ \\sqrt{{\\frac{{{sq_p}}}{{{sq_q}}}}} = \\frac{{{p}}}{{{q}}} \\]\n"
        f"\\[ \\left( \\frac{{{c}}}{{{d}}} \\right)^2 = \\frac{{{p2_c}}}{{{p2_d}}} \\]\n\n"
        f"**Step 2: Add the two fractions using the LCD {lcd}.**\n"
        f"\\[ \\frac{{{p}}}{{{q}}} + \\frac{{{p2_c}}}{{{p2_d}}} = \\frac{{{p * (lcd // q)}}}{{{lcd}}} + \\frac{{{p2_c * (lcd // p2_d)}}}{{{lcd}}} "
        f"= \\frac{{{tot_num}}}{{{lcd}}} = {ans_latex} \\]"
    )
    return {
        "id": f"g9_frac_root_pow_{rng.randint(100000, 999999)}",
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
            {"desc": f"Evaluate square root as {p}/{q}", "marks": 1},
            {"desc": f"Evaluate power as {p2_c}/{p2_d}", "marks": 1},
            {"desc": f"Add using common denominator to get {ans_latex}", "marks": 1},
        ],
        "hints": [
            "Evaluate roots and powers before performing addition.",
            f"Square root is {p}/{q}, and power is {p2_c}/{p2_d}.",
            f"Find the LCD ({lcd}) and add the two fractions.",
        ],
    }


# ----------------------------------------------------------------------
# 28. Complex Fraction: Division of Sums
# ----------------------------------------------------------------------
def arch_28_complex_fraction_division_of_sums(rng: random.Random) -> Dict[str, Any]:
    # (1/a + 1/b) / (1/c - 1/d)
    a = rng.choice([2, 3])
    b = rng.choice([4, 5])
    num_lcd = math.lcm(a, b)
    n_top = (num_lcd // a) + (num_lcd // b)

    c = rng.choice([2, 3])
    d = rng.choice([4, 6])
    while c >= d:
        d = c + 2
    den_lcd = math.lcm(c, d)
    n_bot = (den_lcd // c) - (den_lcd // d)

    # (n_top / num_lcd) / (n_bot / den_lcd) = (n_top / num_lcd) * (den_lcd / n_bot)
    final_n = n_top * den_lcd
    final_d = num_lcd * n_bot

    ans_latex = _mixed_str(final_n, final_d)
    ns, ds = _simplify(final_n, final_d)
    ans_text = f"{ns}/{ds}"

    prompt = (
        f"Simplify the complex fraction to lowest terms:\n"
        f"\\[ \\frac{{\\frac{{1}}{{{a}}} + \\frac{{1}}{{{b}}}}}{{\\frac{{1}}{{{c}}} - \\frac{{1}}{{{d}}}}} \\]"
    )
    sol = (
        f"**Step 1: Simplify the numerator.**\n"
        f"\\[ \\frac{{1}}{{{a}}} + \\frac{{1}}{{{b}}} = \\frac{{{num_lcd // a} + {num_lcd // b}}}{{{num_lcd}}} = \\frac{{{n_top}}}{{{num_lcd}}} \\]\n\n"
        f"**Step 2: Simplify the denominator.**\n"
        f"\\[ \\frac{{1}}{{{c}}} - \\frac{{1}}{{{d}}} = \\frac{{{den_lcd // c} - {den_lcd // d}}}{{{den_lcd}}} = \\frac{{{n_bot}}}{{{den_lcd}}} \\]\n\n"
        f"**Step 3: Divide numerator by denominator (multiply by reciprocal).**\n"
        f"\\[ \\frac{{{n_top}}}{{{num_lcd}}} \\div \\frac{{{n_bot}}}{{{den_lcd}}} = \\frac{{{n_top}}}{{{num_lcd}}} \\times \\frac{{{den_lcd}}}{{{n_bot}}} "
        f"= \\frac{{{final_n}}}{{{final_d}}} = {ans_latex} \\]"
    )
    return {
        "id": f"g9_frac_complex_{rng.randint(100000, 999999)}",
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
            {"desc": f"Simplify top fraction sum to {n_top}/{num_lcd}", "marks": 1},
            {"desc": f"Simplify bottom fraction difference to {n_bot}/{den_lcd}", "marks": 1},
            {"desc": f"Divide by inverting and multiplying to get {ans_latex}", "marks": 1},
        ],
        "hints": [
            "Treat the main fraction bar as a division symbol between top and bottom expressions.",
            "Simplify the numerator and denominator independently first.",
            "Invert the denominator fraction and multiply.",
        ],
    }


# ----------------------------------------------------------------------
# 29. Nested Fraction and Mixed Operations
# ----------------------------------------------------------------------
def arch_29_nested_fraction_and_mixed_operations(rng: random.Random) -> Dict[str, Any]:
    configs = [
        (rng.randint(2, 6), 1, 2, 1, 3, 2, 3),  # (w 1/2 - 1/3) / (2/3)^2
        (rng.randint(2, 6), 3, 4, 1, 2, 1, 2),  # (w 3/4 - 1/2) / (1/2)^2
        (rng.randint(2, 6), 2, 3, 1, 4, 3, 4),  # (w 2/3 - 1/4) / (3/4)^2
        (rng.randint(2, 6), 4, 5, 1, 2, 2, 5),  # (w 4/5 - 1/2) / (2/5)^2
        (rng.randint(2, 6), 1, 3, 1, 6, 1, 3),  # (w 1/3 - 1/6) / (1/3)^2
    ]
    w, r1, d1, r2, d2, p, q = rng.choice(configs)

    imp_n = w * d1 + r1
    brack_lcd = math.lcm(d1, d2)
    s1 = imp_n * (brack_lcd // d1)
    s2 = r2 * (brack_lcd // d2)
    diff_n = s1 - s2
    diff_d = brack_lcd

    sq_p = p ** 2
    sq_q = q ** 2

    res_n = diff_n * sq_q
    res_d = diff_d * sq_p

    ans_latex = _mixed_str(res_n, res_d)
    ns, ds = _simplify(res_n, res_d)
    ans_text = f"{ns}/{ds}"

    prompt = (
        f"Calculate the following multi-operation expression. Write the result in simplest form:\n"
        f"\\[ \\left( {w}\\frac{{{r1}}}{{{d1}}} - \\frac{{{r2}}}{{{d2}}} \\right) \\div \\left( \\frac{{{p}}}{{{q}}} \\right)^2 \\]"
    )
    sol = (
        f"**Step 1: Evaluate the expression inside the first bracket.**\n"
        f"\\[ {w}\\frac{{{r1}}}{{{d1}}} - \\frac{{{r2}}}{{{d2}}} = \\frac{{{imp_n}}}{{{d1}}} - \\frac{{{r2}}}{{{d2}}} "
        f"= \\frac{{{s1} - {s2}}}{{{brack_lcd}}} = \\frac{{{diff_n}}}{{{diff_d}}} \\]\n\n"
        f"**Step 2: Evaluate the squared term.**\n"
        f"\\[ \\left( \\frac{{{p}}}{{{q}}} \\right)^2 = \\frac{{{sq_p}}}{{{sq_q}}} \\]\n\n"
        f"**Step 3: Perform division by multiplying by the reciprocal.**\n"
        f"\\[ \\frac{{{diff_n}}}{{{diff_d}}} \\times \\frac{{{sq_q}}}{{{sq_p}}} = \\frac{{{res_n}}}{{{res_d}}} = {ans_latex} \\]"
    )
    return {
        "id": f"g9_frac_nested_ops_{rng.randint(100000, 999999)}",
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
            {"desc": f"Subtract in brackets to get {diff_n}/{diff_d}", "marks": 1},
            {"desc": f"Square {p}/{q} to get {sq_p}/{sq_q}", "marks": 1},
            {"desc": f"Multiply by reciprocal and simplify to {ans_latex}", "marks": 1},
        ],
        "hints": [
            "Calculate the bracketed difference first.",
            f"Square the fraction in the second term: ({p}/{q})^2 = {sq_p}/{sq_q}.",
            f"Multiply by the reciprocal ({sq_q}/{sq_p}) and reduce to simplest form.",
        ],
    }


# ----------------------------------------------------------------------
# 30. Fraction of a Whole Quantity: Currency
# ----------------------------------------------------------------------
def arch_30_fraction_of_a_whole_quantity_currency(rng: random.Random) -> Dict[str, Any]:
    b = rng.choice([3, 4, 5, 6, 8, 10, 12])
    a = rng.randint(2, b - 1)
    while math.gcd(a, b) != 1:
        a = (a % (b - 1)) + 1

    unit_mult = rng.choice([15, 20, 25, 30, 40, 50, 60, 80])
    total_rand = b * unit_mult
    ans_rand = a * unit_mult

    prompt = (
        f"Calculate the fractional value of the given South African currency amount:\n"
        f"\\[ \\frac{{{a}}}{{{b}}} \\text{{ of }} \\text{{R}}{total_rand} \\]"
    )
    sol = (
        f"**Step 1: Divide the total amount by the denominator.**\n"
        f"\\[ \\text{{R}}{total_rand} \\div {b} = \\text{{R}}{unit_mult} \\]\n\n"
        f"**Step 2: Multiply by the numerator.**\n"
        f"\\[ \\text{{R}}{unit_mult} \\times {a} = \\text{{R}}{ans_rand} \\]"
    )
    return {
        "id": f"g9_frac_of_curr_{rng.randint(100000, 999999)}",
        "question_type": "currency",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"R{ans_rand}",
        "expected_answer": f"R{ans_rand}",
        "sample_answer": f"R{ans_rand}",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"Divide R{total_rand} by {b} to get R{unit_mult}", "marks": 1},
            {"desc": f"Multiply by {a} to get R{ans_rand}", "marks": 1},
        ],
        "hints": [
            "The word 'of' in mathematics indicates multiplication.",
            f"Divide R{total_rand} by {b} first.",
            f"Multiply the quotient by {a}.",
        ],
    }


# ----------------------------------------------------------------------
# 31. Fraction of a Quantity: Measurement Units
# ----------------------------------------------------------------------
def arch_31_fraction_of_a_quantity_measurement_units(rng: random.Random) -> Dict[str, Any]:
    unit_type = rng.choice(["mass", "length", "volume"])
    if unit_type == "mass":
        # Fraction of kg in grams
        denom = rng.choice([4, 5, 8, 10, 20])
        num = rng.randint(1, denom - 1)
        while math.gcd(num, denom) != 1:
            num = (num % (denom - 1)) + 1
        kg_val = rng.choice([1, 2, 3, 5])
        total_g = kg_val * 1000
        ans_g = (total_g // denom) * num
        prompt = f"Calculate \\(\\frac{{{num}}}{{{denom}}}\\) of \\({kg_val}\\text{{ kg}}\\). Give your answer in grams (g)."
        sol = (
            f"**Step 1: Convert kilograms to grams.**\n"
            f"\\[ {kg_val}\\text{{ kg}} = {total_g}\\text{{ g}} \\]\n\n"
            f"**Step 2: Calculate the fractional part.**\n"
            f"\\[ \\frac{{{num}}}{{{denom}}} \\times {total_g} = ({total_g} \\div {denom}) \\times {num} = {ans_g}\\text{{ g}} \\]"
        )
        ans_str = f"{ans_g} g"
    elif unit_type == "length":
        # Fraction of km in meters
        denom = rng.choice([4, 5, 8, 10])
        num = rng.randint(1, denom - 1)
        while math.gcd(num, denom) != 1:
            num = (num % (denom - 1)) + 1
        km_val = rng.choice([2, 4, 6])
        total_m = km_val * 1000
        ans_m = (total_m // denom) * num
        prompt = f"Calculate \\(\\frac{{{num}}}{{{denom}}}\\) of \\({km_val}\\text{{ km}}\\). Give your answer in metres (m)."
        sol = (
            f"**Step 1: Convert kilometres to metres.**\n"
            f"\\[ {km_val}\\text{{ km}} = {total_m}\\text{{ m}} \\]\n\n"
            f"**Step 2: Multiply by the fraction.**\n"
            f"\\[ \\frac{{{num}}}{{{denom}}} \\times {total_m} = {ans_m}\\text{{ m}} \\]"
        )
        ans_str = f"{ans_m} m"
    else:
        # Fraction of litres in mL
        denom = rng.choice([2, 4, 5, 8])
        num = rng.randint(1, denom - 1)
        while math.gcd(num, denom) != 1:
            num = (num % (denom - 1)) + 1
        l_val = rng.choice([1, 2, 4])
        total_ml = l_val * 1000
        ans_ml = (total_ml // denom) * num
        prompt = f"Calculate \\(\\frac{{{num}}}{{{denom}}}\\) of \\({l_val}\\text{{ litres}}\\). Give your answer in millilitres (mL)."
        sol = (
            f"**Step 1: Convert litres to millilitres.**\n"
            f"\\[ {l_val}\\text{{ L}} = {total_ml}\\text{{ mL}} \\]\n\n"
            f"**Step 2: Multiply by the fraction.**\n"
            f"\\[ \\frac{{{num}}}{{{denom}}} \\times {total_ml} = {ans_ml}\\text{{ mL}} \\]"
        )
        ans_str = f"{ans_ml} mL"

    return {
        "id": f"g9_frac_units_{rng.randint(100000, 999999)}",
        "question_type": "measurement",
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
            {"desc": "Convert larger unit to base unit (× 1000)", "marks": 1},
            {"desc": f"Calculate correct fractional quantity {ans_str}", "marks": 1},
        ],
        "hints": [
            "Convert the measurement to smaller units (1 kg = 1 000 g, 1 km = 1 000 m, 1 L = 1 000 mL).",
            "Divide by the denominator, then multiply by the numerator.",
            f"Answer: {ans_str}.",
        ],
    }


# ----------------------------------------------------------------------
# 32. Fraction of a Fraction: Remainder Word Problem
# ----------------------------------------------------------------------
def arch_32_fraction_of_a_fraction_word_problem(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(["Sipho", "Ayanda", "Lerato", "Zola", "Bongani", "Kagiso"])
    # Spends 1/b on item 1, then c/d of remainder on item 2
    b = rng.choice([3, 4, 5])
    d = rng.choice([2, 3, 4])
    c = 1

    # Remainder 1 = (b-1)/b
    # Item 2 = c/d * (b-1)/b
    # Remaining fraction = (b-1)/b * (d-c)/d
    total_den = b * d
    rem_num = (b - 1) * (d - c)
    ns, ds = _simplify(rem_num, total_den)

    # Pick budget multiple of total_den
    base_m = rng.choice([30, 40, 50, 60, 100])
    budget = total_den * base_m
    item1_spent = (budget // b)
    remainder1 = budget - item1_spent
    item2_spent = (remainder1 // d) * c
    final_left = remainder1 - item2_spent

    ans_latex = f"\\text{{R}}{final_left}"

    prompt = (
        f"{name} earns a monthly stipend of R{budget}. He spends \\(\\frac{{1}}{{{b}}}\\) of his stipend "
        f"on study materials and \\(\\frac{{{c}}}{{{d}}}\\) of the **remaining amount** on local transport. "
        f"How much money does {name} have left after these expenses?"
    )
    sol = (
        f"**Step 1: Calculate amount spent on study materials.**\n"
        f"\\[ \\text{{Study materials}} = \\frac{{1}}{{{b}}} \\times \\text{{R}}{budget} = \\text{{R}}{item1_spent} \\]\n\n"
        f"**Step 2: Find the remaining amount.**\n"
        f"\\[ \\text{{Remainder}} = \\text{{R}}{budget} - \\text{{R}}{item1_spent} = \\text{{R}}{remainder1} \\]\n\n"
        f"**Step 3: Calculate amount spent on transport.**\n"
        f"\\[ \\text{{Transport}} = \\frac{{{c}}}{{{d}}} \\times \\text{{R}}{remainder1} = \\text{{R}}{item2_spent} \\]\n\n"
        f"**Step 4: Calculate final remaining money.**\n"
        f"\\[ \\text{{Final balance}} = \\text{{R}}{remainder1} - \\text{{R}}{item2_spent} = \\text{{R}}{final_left} \\]"
    )
    return {
        "id": f"g9_frac_word_rem_{rng.randint(100000, 999999)}",
        "question_type": "currency",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"R{final_left}",
        "expected_answer": f"R{final_left}",
        "sample_answer": f"R{final_left}",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "marking_schema": [
            {"desc": f"Calculate initial expense R{item1_spent} and remainder R{remainder1}", "marks": 1},
            {"desc": f"Calculate transport expense R{item2_spent}", "marks": 1},
            {"desc": f"Final remaining amount R{final_left}", "marks": 1},
        ],
        "hints": [
            "Find the first expense by multiplying the total stipend by the first fraction.",
            "Subtract that expense from the total before calculating the second fraction.",
            f"The remaining money is R{final_left}.",
        ],
    }


# ----------------------------------------------------------------------
# 33. Reverse Fraction: Find the Whole from a Part
# ----------------------------------------------------------------------
def arch_33_reverse_fraction_find_the_whole_from_a_part(rng: random.Random) -> Dict[str, Any]:
    b = rng.choice([4, 5, 6, 8, 10])
    a = rng.randint(2, b - 1)
    while math.gcd(a, b) != 1:
        a = (a % (b - 1)) + 1

    unit_val = rng.randint(15, 45)
    part_val = a * unit_val
    total_val = b * unit_val

    prompt = (
        f"If \\(\\frac{{{a}}}{{{b}}}\\) of the Grade 9 learners at a school participate in athletics, "
        f"and this represents {part_val} learners, determine the total number of Grade 9 learners enrolled at the school."
    )
    sol = (
        f"**Step 1: Find the value of one fractional part (\\(\\frac{{1}}{{{b}}}\\)).**\n"
        f"\\[ \\frac{{1}}{{{b}}} = {part_val} \\div {a} = {unit_val} \\text{{ learners}} \\]\n\n"
        f"**Step 2: Multiply by the denominator ({b}) to find the whole.**\n"
        f"\\[ \\text{{Total learners}} = {unit_val} \\times {b} = {total_val} \\]"
    )
    return {
        "id": f"g9_frac_rev_{rng.randint(100000, 999999)}",
        "question_type": "numeric",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": str(total_val),
        "expected_answer": str(total_val),
        "sample_answer": str(total_val),
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"Find value of 1 part: {part_val} ÷ {a} = {unit_val}", "marks": 1},
            {"desc": f"Multiply by {b} to get total {total_val}", "marks": 1},
        ],
        "hints": [
            f"If {a} parts equal {part_val}, divide by {a} to find the value of 1 part.",
            f"Multiply that single part by {b} to find the whole quantity.",
            f"Total is {total_val}.",
        ],
    }


# ----------------------------------------------------------------------
# 34. Convert Common Fraction to Percentage
# ----------------------------------------------------------------------
def arch_34_convert_common_fraction_to_percentage(rng: random.Random) -> Dict[str, Any]:
    # Denominators that give nice percentages: 2, 4, 5, 8, 10, 20, 25, 40, 50
    den = rng.choice([4, 5, 8, 10, 20, 25, 40, 50])
    num = rng.randint(1, den - 1)
    while math.gcd(num, den) != 1:
        num = (num % (den - 1)) + 1

    pct_float = (num / den) * 100
    if pct_float.is_integer():
        ans_pct = f"{int(pct_float)}%"
        ans_latex = f"{int(pct_float)}\\%"
    else:
        # SA comma notation: 37,5%
        dec_s = f"{pct_float:.1f}".replace(".", "{,}")
        ans_pct = f"{pct_float:.1f}%".replace(".", ",")
        ans_latex = f"{dec_s}\\%"

    prompt = (
        f"Convert the common fraction to a percentage:\n"
        f"\\[ \\frac{{{num}}}{{{den}}} \\]"
    )
    sol = (
        f"**Step 1: Multiply the fraction by 100%.**\n"
        f"\\[ \\frac{{{num}}}{{{den}}} \\times 100\\% = \\frac{{{num} \\times 100}}{{{den}}}\\% \\]\n\n"
        f"**Step 2: Simplify the calculation.**\n"
        f"\\[ = \\frac{{{num * 100}}}{{{den}}}\\% = {ans_latex} \\]"
    )
    return {
        "id": f"g9_frac_to_pct_{rng.randint(100000, 999999)}",
        "question_type": "percentage",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans_pct,
        "expected_answer": ans_pct,
        "sample_answer": ans_pct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"Multiply fraction by 100%: ({num}/{den}) × 100", "marks": 1},
            {"desc": f"State percentage as {ans_pct}", "marks": 1},
        ],
        "hints": [
            "To convert any fraction to a percentage, multiply by 100%.",
            f"Calculation: ({num} × 100) / {den}.",
            f"The percentage is {ans_pct}.",
        ],
    }


# ----------------------------------------------------------------------
# 35. Convert Percentage to Simplified Common Fraction
# ----------------------------------------------------------------------
def arch_35_convert_percentage_to_simplified_common_fraction(rng: random.Random) -> Dict[str, Any]:
    # e.g. 15%, 35%, 45%, 55%, 65%, 75%, 85%, 24%, 36%, 64%, 84%
    pct = rng.choice([15, 24, 35, 36, 45, 55, 64, 68, 72, 85, 92])
    g = math.gcd(pct, 100)
    sn = pct // g
    sd = 100 // g

    ans_latex = f"\\frac{{{sn}}}{{{sd}}}"
    ans_text = f"{sn}/{sd}"

    prompt = (
        f"Convert \\({pct}\\%\\) to a common fraction in its simplest lowest terms."
    )
    sol = (
        f"**Step 1: Write the percentage as a fraction with denominator 100.**\n"
        f"\\[ {pct}\\% = \\frac{{{pct}}}{{100}} \\]\n\n"
        f"**Step 2: Simplify by dividing by the HCF ({g}).**\n"
        f"\\[ \\frac{{{pct} \\div {g}}}{{100 \\div {g}}} = {ans_latex} \\]"
    )
    return {
        "id": f"g9_pct_to_frac_{rng.randint(100000, 999999)}",
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
            {"desc": f"Write as {pct}/100", "marks": 1},
            {"desc": f"Simplify to lowest terms {ans_latex}", "marks": 1},
        ],
        "hints": [
            "A percentage represents parts out of 100.",
            f"Write as {pct}/100 and find the highest common factor.",
            f"The simplest fraction is {ans_text}.",
        ],
    }


# ----------------------------------------------------------------------
# 36. Convert Mixed Number Percentage to Fraction
# ----------------------------------------------------------------------
def arch_36_convert_mixed_number_percentage_to_fraction(rng: random.Random) -> Dict[str, Any]:
    choices = [
        ("12\\frac{1}{2}\\%", 25, 2, 1, 8),
        ("33\\frac{1}{3}\\%", 100, 3, 1, 3),
        ("66\\frac{2}{3}\\%", 200, 3, 2, 3),
        ("37\\frac{1}{2}\\%", 75, 2, 3, 8),
        ("62\\frac{1}{2}\\%", 125, 2, 5, 8),
        ("16\\frac{2}{3}\\%", 50, 3, 1, 6),
        ("87\\frac{1}{2}\\%", 175, 2, 7, 8),
    ]
    pct_latex, imp_n, imp_d, fn, fd = rng.choice(choices)

    ans_latex = f"\\frac{{{fn}}}{{{fd}}}"
    ans_text = f"{fn}/{fd}"

    prompt = (
        f"Convert the mixed percentage to a simplified common fraction:\n"
        f"\\[ {pct_latex} \\]"
    )
    sol = (
        f"**Step 1: Convert the mixed number percentage to an improper fraction.**\n"
        f"\\[ {pct_latex} = \\frac{{{imp_n}}}{{{imp_d}}}\\% \\]\n\n"
        f"**Step 2: Divide by 100 (multiply denominator by 100).**\n"
        f"\\[ = \\frac{{{imp_n}}}{{{imp_d} \\times 100}} = \\frac{{{imp_n}}}{{{imp_d * 100}}} \\]\n\n"
        f"**Step 3: Simplify by dividing by the common factor.**\n"
        f"\\[ = {ans_latex} \\]"
    )
    return {
        "id": f"g9_mixed_pct_to_frac_{rng.randint(100000, 999999)}",
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
            {"desc": f"Write percentage over 100 as ({imp_n}/{imp_d}) × (1/100)", "marks": 1},
            {"desc": f"Simplify fraction to {ans_latex}", "marks": 1},
        ],
        "hints": [
            "Convert the mixed number into an improper fraction first.",
            "Multiply the denominator by 100 to remove the percentage sign.",
            f"Simplify to {ans_text}.",
        ],
    }


# ----------------------------------------------------------------------
# 37. Percentage of a Quantity Using Fractions
# ----------------------------------------------------------------------
def arch_37_percentage_of_a_quantity_using_fractions(rng: random.Random) -> Dict[str, Any]:
    pct = rng.choice([15, 20, 25, 30, 40, 60, 75, 80])
    g = math.gcd(pct, 100)
    fn = pct // g
    fd = 100 // g

    k = rng.choice([12, 16, 20, 24, 30, 36, 40])
    total_val = fd * k
    ans_val = fn * k

    prompt = (
        f"Calculate \\({pct}\\%\\) of R{total_val} by converting the percentage into a simplified common fraction first."
    )
    sol = (
        f"**Step 1: Express {pct}% as a simplified fraction.**\n"
        f"\\[ {pct}\\% = \\frac{{{pct}}}{{100}} = \\frac{{{fn}}}{{{fd}}} \\]\n\n"
        f"**Step 2: Calculate the fraction of the quantity.**\n"
        f"\\[ \\frac{{{fn}}}{{{fd}}} \\times \\text{{R}}{total_val} = (\\text{{R}}{total_val} \\div {fd}) \\times {fn} "
        f"= \\text{{R}}{k} \\times {fn} = \\text{{R}}{ans_val} \\]"
    )
    return {
        "id": f"g9_pct_of_qty_{rng.randint(100000, 999999)}",
        "question_type": "currency",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"R{ans_val}",
        "expected_answer": f"R{ans_val}",
        "sample_answer": f"R{ans_val}",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"Convert {pct}% to simplified fraction {fn}/{fd}", "marks": 1},
            {"desc": f"Multiply by R{total_val} to get R{ans_val}", "marks": 1},
        ],
        "hints": [
            f"Simplify {pct}% as {fn}/{fd}.",
            f"Divide R{total_val} by {fd} and multiply by {fn}.",
            f"Result is R{ans_val}.",
        ],
    }


# ----------------------------------------------------------------------
# 38. Percentage Increase Using Fraction Multiplier
# ----------------------------------------------------------------------
def arch_38_percentage_increase_using_fraction_multiplier(rng: random.Random) -> Dict[str, Any]:
    pct = rng.choice([10, 15, 20, 25, 50])
    base_m = rng.choice([20, 40, 60, 80, 100, 120])
    old_price = 100 * (base_m // 20)
    increase = (old_price * pct) // 100
    new_price = old_price + increase

    prompt = (
        f"A jacket originally priced at R{old_price} increases in price by \\({pct}\\%\\). "
        f"Calculate the new selling price."
    )
    sol = (
        f"**Step 1: Calculate the amount of increase.**\n"
        f"\\[ \\text{{Increase}} = \\frac{{{pct}}}{{100}} \\times \\text{{R}}{old_price} = \\text{{R}}{increase} \\]\n\n"
        f"**Step 2: Add the increase to the original price.**\n"
        f"\\[ \\text{{New price}} = \\text{{R}}{old_price} + \\text{{R}}{increase} = \\text{{R}}{new_price} \\]"
    )
    return {
        "id": f"g9_pct_inc_{rng.randint(100000, 999999)}",
        "question_type": "currency",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"R{new_price}",
        "expected_answer": f"R{new_price}",
        "sample_answer": f"R{new_price}",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"Calculate increase: R{old_price} × {pct}/100 = R{increase}", "marks": 1},
            {"desc": f"Add to original to obtain R{new_price}", "marks": 1},
        ],
        "hints": [
            f"Find {pct}% of R{old_price}.",
            "Add that amount to the original price.",
            f"New price is R{new_price}.",
        ],
    }


# ----------------------------------------------------------------------
# 39. Percentage Decrease Using Fraction Multiplier
# ----------------------------------------------------------------------
def arch_39_percentage_decrease_using_fraction_multiplier(rng: random.Random) -> Dict[str, Any]:
    pct = rng.choice([10, 15, 20, 25, 30, 40])
    base_m = rng.choice([30, 50, 70, 80, 120])
    orig_price = 100 * (base_m // 10)
    discount = (orig_price * pct) // 100
    sale_price = orig_price - discount

    prompt = (
        f"During a seasonal sale, a pair of running shoes priced at R{orig_price} is discounted by \\({pct}\\%\\). "
        f"Determine the discounted sale price."
    )
    sol = (
        f"**Step 1: Calculate the discount amount.**\n"
        f"\\[ \\text{{Discount}} = \\frac{{{pct}}}{{100}} \\times \\text{{R}}{orig_price} = \\text{{R}}{discount} \\]\n\n"
        f"**Step 2: Subtract the discount from the original price.**\n"
        f"\\[ \\text{{Sale price}} = \\text{{R}}{orig_price} - \\text{{R}}{discount} = \\text{{R}}{sale_price} \\]"
    )
    return {
        "id": f"g9_pct_dec_{rng.randint(100000, 999999)}",
        "question_type": "currency",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"R{sale_price}",
        "expected_answer": f"R{sale_price}",
        "sample_answer": f"R{sale_price}",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"Calculate discount: R{orig_price} × {pct}/100 = R{discount}", "marks": 1},
            {"desc": f"Subtract from original price to obtain R{sale_price}", "marks": 1},
        ],
        "hints": [
            f"Calculate the discount: ({pct}/100) × R{orig_price}.",
            "Subtract the discount from the original price.",
            f"Sale price is R{sale_price}.",
        ],
    }


# ----------------------------------------------------------------------
# 40. Express One Quantity as Fraction and Percentage of Another
# ----------------------------------------------------------------------
def arch_40_express_one_quantity_as_fraction_and_percentage_of_another(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(["Ayanda", "Thabo", "Sipho", "Lerato", "Kagiso", "Fatima"])
    total_marks = rng.choice([40, 50, 60, 80])
    # Multiples that give whole percentages
    scored = rng.choice([int(total_marks * p / 100) for p in [45, 55, 65, 70, 75, 85]])

    g = math.gcd(scored, total_marks)
    sn = scored // g
    sd = total_marks // g

    pct = round((scored / total_marks) * 100)
    ans_latex = f"\\frac{{{sn}}}{{{sd}}} \\text{{ and }} {pct}\\%"
    ans_text = f"{sn}/{sd} and {pct}%"

    prompt = (
        f"In a Mathematics test out of {total_marks} marks, {name} scored {scored} marks. "
        f"Express {name}'s score as a simplified common fraction and as a percentage."
    )
    sol = (
        f"**Step 1: Write as a fraction of the total marks and simplify.**\n"
        f"\\[ \\frac{{{scored}}}{{{total_marks}}} = \\frac{{{scored} \\div {g}}}{{{total_marks} \\div {g}}} = \\frac{{{sn}}}{{{sd}}} \\]\n\n"
        f"**Step 2: Convert the fraction to a percentage.**\n"
        f"\\[ \\frac{{{sn}}}{{{sd}}} \\times 100\\% = {pct}\\% \\]"
    )
    return {
        "id": f"g9_frac_score_pct_{rng.randint(100000, 999999)}",
        "question_type": "compound_answer",
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
            {"desc": f"State simplified fraction {sn}/{sd}", "marks": 1},
            {"desc": f"Convert to percentage {pct}%", "marks": 1},
        ],
        "hints": [
            f"Place {scored} over {total_marks} and reduce to lowest terms.",
            "Multiply the simplified fraction by 100% to find the percentage.",
            f"Answers: {ans_text}.",
        ],
    }


# ----------------------------------------------------------------------
# 41. Sharing Quantity in Given Fractional Shares
# ----------------------------------------------------------------------
def arch_41_sharing_quantity_in_given_fractional_shares(rng: random.Random) -> Dict[str, Any]:
    # Total prize shared among 3 learners: 1/b to A, 1/d to B, remainder to C
    b = rng.choice([2, 3, 4])
    d = rng.choice([3, 5, 6])
    while b == d:
        d = 5

    lcd = math.lcm(b, d)
    sa = lcd // b
    sb = lcd // d
    sc = lcd - (sa + sb)
    while sc <= 0:
        b = 2
        d = 4
        lcd = 4
        sa = 2
        sb = 1
        sc = 1

    unit_k = rng.choice([40, 50, 60, 80, 100])
    total_rand = lcd * unit_k
    share_c = sc * unit_k

    prompt = (
        f"A prize of R{total_rand} is shared among three competition winners: "
        f"Winner A receives \\(\\frac{{1}}{{{b}}}\\) of the prize, "
        f"Winner B receives \\(\\frac{{1}}{{{d}}}\\), and "
        f"Winner C receives the remaining balance. "
        f"Determine the exact amount of money received by Winner C."
    )
    sol = (
        f"**Step 1: Calculate the fraction of the prize for Winner A and Winner B.**\n"
        f"\\[ \\text{{Winner A}} = \\frac{{1}}{{{b}}} \\times \\text{{R}}{total_rand} = \\text{{R}}{sa * unit_k} \\]\n"
        f"\\[ \\text{{Winner B}} = \\frac{{1}}{{{d}}} \\times \\text{{R}}{total_rand} = \\text{{R}}{sb * unit_k} \\]\n\n"
        f"**Step 2: Subtract their shares from the total prize.**\n"
        f"\\[ \\text{{Winner C}} = \\text{{R}}{total_rand} - (\\text{{R}}{sa * unit_k} + \\text{{R}}{sb * unit_k}) = \\text{{R}}{share_c} \\]"
    )
    return {
        "id": f"g9_frac_sharing_{rng.randint(100000, 999999)}",
        "question_type": "currency",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"R{share_c}",
        "expected_answer": f"R{share_c}",
        "sample_answer": f"R{share_c}",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "marking_schema": [
            {"desc": f"Calculate Winner A share R{sa * unit_k}", "marks": 1},
            {"desc": f"Calculate Winner B share R{sb * unit_k}", "marks": 1},
            {"desc": f"Subtract from total to find Winner C share R{share_c}", "marks": 1},
        ],
        "hints": [
            "Find each person's Rand share by calculating their fraction of the total.",
            "Add Winner A and Winner B shares together.",
            f"Winner C receives R{share_c}.",
        ],
    }


# ----------------------------------------------------------------------
# 42. Fuel Tank Capacity Fraction Problem (with SVG diagram)
# ----------------------------------------------------------------------
def arch_42_fuel_tank_capacity_fraction_problem(rng: random.Random) -> Dict[str, Any]:
    # Tank is initially 1/4 or 1/5 or 2/5 full. Adding L litres brings it to 3/4 or 4/5 full.
    denom = rng.choice([4, 5, 8, 10])
    init_num = rng.choice([1, 2])
    target_num = rng.choice([denom - 2, denom - 1])
    diff_num = target_num - init_num

    capacity_unit = rng.choice([8, 10, 12, 15])
    total_capacity = denom * capacity_unit
    litres_added = diff_num * capacity_unit

    seed_val = rng.randint(1000, 999999)
    svg = draw_tank_gauge_svg(init_num, denom, label="Initial Fuel Level", seed=seed_val)

    prompt = (
        f"A minibus taxi's fuel tank is initially \\(\\frac{{{init_num}}}{{{denom}}}\\) full, "
        f"as shown in the fuel gauge below. After the driver adds {litres_added} litres of petrol at a filling station, "
        f"the fuel tank is \\(\\frac{{{target_num}}}{{{denom}}}\\) full. "
        f"What is the total capacity of the minibus fuel tank in litres?"
    )
    sol = (
        f"**Step 1: Determine the fraction of the tank filled by the added petrol.**\n"
        f"\\[ \\frac{{{target_num}}}{{{denom}}} - \\frac{{{init_num}}}{{{denom}}} = \\frac{{{diff_num}}}{{{denom}}} \\]\n\n"
        f"**Step 2: Find the capacity represented by one fractional part (\\(\\frac{{1}}{{{denom}}}\\)).**\n"
        f"\\[ \\frac{{1}}{{{denom}}} = {litres_added} \\div {diff_num} = {capacity_unit} \\text{{ litres}} \\]\n\n"
        f"**Step 3: Multiply by the denominator ({denom}) to find full capacity.**\n"
        f"\\[ \\text{{Full capacity}} = {capacity_unit} \\times {denom} = {total_capacity} \\text{{ litres}} \\]"
    )
    return {
        "id": f"g9_frac_fuel_tank_{rng.randint(100000, 999999)}",
        "question_type": "measurement",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"{total_capacity} litres",
        "expected_answer": f"{total_capacity} litres",
        "sample_answer": f"{total_capacity} L",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "marking_schema": [
            {"desc": f"Calculate difference fraction: {target_num}/{denom} - {init_num}/{denom} = {diff_num}/{denom}", "marks": 1},
            {"desc": f"Find capacity of 1 unit = {capacity_unit} L", "marks": 1},
            {"desc": f"State total capacity {total_capacity} litres", "marks": 1},
        ],
        "hints": [
            f"Subtract the starting fraction from the final fraction to find what fraction represents {litres_added} litres.",
            f"Divide {litres_added} by {diff_num} to find 1 part of the tank.",
            f"Multiply by {denom} to find the total capacity ({total_capacity} litres).",
        ],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 43. Recipe and Ingredient Scaling with Mixed Numbers
# ----------------------------------------------------------------------
def arch_43_recipe_and_ingredient_scaling_mixed_numbers(rng: random.Random) -> Dict[str, Any]:
    # Recipe for N people requires w r/d cups of sugar. Scale for M people.
    n_base = rng.choice([4, 6])
    scale_factor = rng.choice([2, 3])
    m_target = n_base * scale_factor

    w = 1
    d = rng.choice([2, 3, 4])
    r = 1
    imp_n = w * d + r

    # Scaled = imp_n / d * scale_factor
    scaled_n = imp_n * scale_factor
    ans_latex = _mixed_str(scaled_n, d)
    ns, ds = _simplify(scaled_n, d)
    ans_text = f"{ns}/{ds}" if ds > 1 else str(ns)

    prompt = (
        f"A traditional South African koeksister recipe serving {n_base} people requires "
        f"\\({w}\\frac{{{r}}}{{{d}}}\\) cups of sugar. "
        f"How many cups of sugar are required to make the recipe for {m_target} people? "
        f"Give your answer as a simplified mixed number or whole number."
    )
    sol = (
        f"**Step 1: Determine the scaling ratio.**\n"
        f"\\[ \\text{{Scale factor}} = {m_target} \\div {n_base} = {scale_factor} \\]\n\n"
        f"**Step 2: Convert the ingredient quantity to an improper fraction.**\n"
        f"\\[ {w}\\frac{{{r}}}{{{d}}} = \\frac{{{imp_n}}}{{{d}}} \\text{{ cups}} \\]\n\n"
        f"**Step 3: Multiply by the scaling factor.**\n"
        f"\\[ \\frac{{{imp_n}}}{{{d}}} \\times {scale_factor} = \\frac{{{scaled_n}}}{{{d}}} = {ans_latex} \\text{{ cups}} \\]"
    )
    return {
        "id": f"g9_frac_recipe_{rng.randint(100000, 999999)}",
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
            {"desc": f"Determine scale factor = {scale_factor}", "marks": 1},
            {"desc": f"Multiply and express as {ans_latex} cups", "marks": 1},
        ],
        "hints": [
            f"Find how many times bigger the new batch is: {m_target} ÷ {n_base} = {scale_factor}.",
            f"Multiply the ingredient amount ({w} {r}/{d}) by {scale_factor}.",
            f"Result: {ans_latex} cups.",
        ],
    }


# ----------------------------------------------------------------------
# 44. Time and Work Rate Fractions
# ----------------------------------------------------------------------
def arch_44_time_and_work_rate_fractions(rng: random.Random) -> Dict[str, Any]:
    t1 = rng.choice([3, 4, 6])
    t2 = rng.choice([2, 5, 8])
    while t1 == t2:
        t2 = 5

    lcd = math.lcm(t1, t2)
    comb_num = (lcd // t1) + (lcd // t2)
    ans_latex = _frac_str(comb_num, lcd)
    ns, ds = _simplify(comb_num, lcd)
    ans_text = f"{ns}/{ds}"

    prompt = (
        f"Worker A can paint a fence in {t1} hours, and Worker B can paint the same fence in {t2} hours. "
        f"What fraction of the fence will they complete together in 1 hour if they work simultaneously? "
        f"Give your answer in simplest form."
    )
    sol = (
        f"**Step 1: Find each worker's 1-hour work rate.**\n"
        f"Worker A completes \\(\\frac{{1}}{{{t1}}}\\) of the job per hour.\n"
        f"Worker B completes \\(\\frac{{1}}{{{t2}}}\\) of the job per hour.\n\n"
        f"**Step 2: Add the two rates using LCD({t1}, {t2}) = {lcd}.**\n"
        f"\\[ \\frac{{1}}{{{t1}}} + \\frac{{1}}{{{t2}}} = \\frac{{{lcd // t1}}}{{{lcd}}} + \\frac{{{lcd // t2}}}{{{lcd}}} "
        f"= \\frac{{{comb_num}}}{{{lcd}}} = {ans_latex} \\]"
    )
    return {
        "id": f"g9_frac_work_rate_{rng.randint(100000, 999999)}",
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
            {"desc": f"State individual rates 1/{t1} and 1/{t2}", "marks": 1},
            {"desc": f"Sum rates to obtain {ans_latex}", "marks": 1},
        ],
        "hints": [
            f"In 1 hour, Worker A finishes 1/{t1} and Worker B finishes 1/{t2}.",
            f"Add 1/{t1} + 1/{t2} using LCD {lcd}.",
            f"The combined fraction is {ans_text}.",
        ],
    }


# ----------------------------------------------------------------------
# 45. Distance Travelled: Multi-Stage Fractions
# ----------------------------------------------------------------------
def arch_45_distance_travelled_multi_stage_fractions(rng: random.Random) -> Dict[str, Any]:
    b = rng.choice([3, 4, 5])
    d = rng.choice([2, 4, 6])
    while b == d:
        d = 6

    lcd = math.lcm(b, d)
    s1_parts = lcd // b
    s2_parts = lcd // d
    rem_parts = lcd - (s1_parts + s2_parts)
    while rem_parts <= 0:
        b = 3
        d = 6
        lcd = 6
        s1_parts = 2
        s2_parts = 1
        rem_parts = 3

    unit_dist = rng.choice([20, 30, 40, 50])
    total_km = lcd * unit_dist
    rem_km = rem_parts * unit_dist

    prompt = (
        f"A delivery vehicle completes a trip of {total_km} km between Polokwane and Pretoria. "
        f"The driver travels \\(\\frac{{1}}{{{b}}}\\) of the total distance on national highway, "
        f"\\(\\frac{{1}}{{{d}}}\\) of the total distance on provincial roads, and the remaining distance on city streets. "
        f"Calculate the distance travelled on city streets in kilometres."
    )
    sol = (
        f"**Step 1: Calculate distance on highway and provincial roads.**\n"
        f"\\[ \\text{{Highway}} = \\frac{{1}}{{{b}}} \\times {total_km} = {s1_parts * unit_dist} \\text{{ km}} \\]\n"
        f"\\[ \\text{{Provincial}} = \\frac{{1}}{{{d}}} \\times {total_km} = {s2_parts * unit_dist} \\text{{ km}} \\]\n\n"
        f"**Step 2: Subtract from the total trip distance.**\n"
        f"\\[ \\text{{City streets}} = {total_km} - ({s1_parts * unit_dist} + {s2_parts * unit_dist}) = {rem_km} \\text{{ km}} \\]"
    )
    return {
        "id": f"g9_frac_dist_multi_{rng.randint(100000, 999999)}",
        "question_type": "measurement",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"{rem_km} km",
        "expected_answer": f"{rem_km} km",
        "sample_answer": f"{rem_km} km",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "marking_schema": [
            {"desc": f"Calculate highway distance {s1_parts * unit_dist} km", "marks": 1},
            {"desc": f"Calculate provincial road distance {s2_parts * unit_dist} km", "marks": 1},
            {"desc": f"Subtract to obtain city street distance {rem_km} km", "marks": 1},
        ],
        "hints": [
            f"Find 1/{b} of {total_km} km and 1/{d} of {total_km} km.",
            "Add those two distances together.",
            f"Subtract the sum from {total_km} km to get {rem_km} km.",
        ],
    }


# ----------------------------------------------------------------------
# 46. Visual Pie Chart Fraction Sector Interpretation (with SVG diagram)
# ----------------------------------------------------------------------
def arch_46_visual_pie_chart_fraction_sector_interpretation(rng: random.Random) -> Dict[str, Any]:
    total_parts = rng.choice([8, 10, 12])
    if total_parts == 8:
        c1, c2, c3 = 3, 2, 3
    elif total_parts == 10:
        c1, c2, c3 = 4, 3, 3
    else:
        c1, c2, c3 = 5, 4, 3

    categories = [
        (c1, "Rent & Housing", "#2563EB"),
        (c2, "Food & Groceries", "#059669"),
        (c3, "Savings & Other", "#D97706"),
    ]

    target_idx = rng.choice([0, 1, 2])
    target_count, target_label, _ = categories[target_idx]

    ans_latex = _frac_str(target_count, total_parts)
    ns, ds = _simplify(target_count, total_parts)
    ans_text = f"{ns}/{ds}"

    seed_val = rng.randint(1000, 999999)
    svg = draw_pie_fraction_svg(categories, total_parts, seed=seed_val)

    prompt = (
        f"The circular pie chart below shows a family budget divided into {total_parts} equal sectors. "
        f"Determine the simplified common fraction of the total budget allocated to **{target_label}**."
    )
    sol = (
        f"**Step 1: Read the number of sectors for {target_label}.**\n"
        f"Sectors allocated = \\({target_count}\\) out of \\({total_parts}\\).\n\n"
        f"**Step 2: Simplify the fraction.**\n"
        f"\\[ \\frac{{{target_count}}}{{{total_parts}}} = {ans_latex} \\]"
    )
    return {
        "id": f"g9_frac_pie_budget_{rng.randint(100000, 999999)}",
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
            {"desc": f"Identify sector proportion {target_count}/{total_parts}", "marks": 1},
            {"desc": f"Simplify fraction to {ans_latex}", "marks": 1},
        ],
        "hints": [
            f"Check the legend: {target_label} has {target_count} parts out of {total_parts}.",
            f"Write the fraction {target_count}/{total_parts}.",
            f"Reduce to lowest terms: {ans_text}.",
        ],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 47. Budget Allocation and Remainder Fraction
# ----------------------------------------------------------------------
def arch_47_budget_allocation_and_remainder_fraction(rng: random.Random) -> Dict[str, Any]:
    # Income R12 000. 1/3 on rent, 1/4 on food, 1/6 on savings.
    income = rng.choice([12000, 18000, 24000, 30000])
    # Fractions: 1/3, 1/4, 1/6 -> LCD 12: 4/12 + 3/12 + 2/12 = 9/12 = 3/4. Remainder = 1/4.
    rem_fraction_n = 1
    rem_fraction_d = 4
    rem_rand = income // 4

    prompt = (
        f"Thabo earns a net monthly salary of R{income}. He allocates \\(\\frac{{1}}{{3}}\\) to accommodation rent, "
        f"\\(\\frac{{1}}{{4}}\\) to groceries, and \\(\\frac{{1}}{{6}}\\) to savings. "
        f"Calculate the amount of money Thabo has remaining for discretionary spending."
    )
    sol = (
        f"**Step 1: Calculate the common denominator for the allocated fractions.**\n"
        f"\\[ \\text{{LCD}}(3, 4, 6) = 12 \\]\n"
        f"\\[ \\text{{Total allocated fraction}} = \\frac{{4}}{{12}} + \\frac{{3}}{{12}} + \\frac{{2}}{{12}} = \\frac{{9}}{{12}} = \\frac{{3}}{{4}} \\]\n\n"
        f"**Step 2: Find the remaining fraction.**\n"
        f"\\[ 1 - \\frac{{3}}{{4}} = \\frac{{1}}{{4}} \\]\n\n"
        f"**Step 3: Calculate the remaining Rand amount.**\n"
        f"\\[ \\frac{{1}}{{4}} \\times \\text{{R}}{income} = \\text{{R}}{rem_rand} \\]"
    )
    return {
        "id": f"g9_frac_budget_rem_{rng.randint(100000, 999999)}",
        "question_type": "currency",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"R{rem_rand}",
        "expected_answer": f"R{rem_rand}",
        "sample_answer": f"R{rem_rand}",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "marking_schema": [
            {"desc": "Sum fractions: 1/3 + 1/4 + 1/6 = 3/4", "marks": 1},
            {"desc": "Find remaining fraction: 1 - 3/4 = 1/4", "marks": 1},
            {"desc": f"Calculate remaining money R{rem_rand}", "marks": 1},
        ],
        "hints": [
            "Add the three fractions together using the common denominator 12.",
            "Subtract the sum from 1 whole to find the fraction remaining.",
            f"Multiply that fraction by R{income} to get R{rem_rand}.",
        ],
    }


# ----------------------------------------------------------------------
# 48. Algebraic Fraction Evaluation: Numeric Substitution
# ----------------------------------------------------------------------
def arch_48_algebraic_fraction_evaluation_numeric_substitution(rng: random.Random) -> Dict[str, Any]:
    # Given x = 1/a, y = 1/b. Evaluate (x + y) / (x * y) = (a + b)
    a = rng.randint(2, 5)
    b = rng.randint(2, 5)
    while a == b:
        b = rng.randint(2, 6)

    ans_val = a + b
    ab = a * b
    a_plus_b = a + b
    prompt = (
        f"Given that \\(x = \\frac{{1}}{{{a}}}\\) and \\(y = \\frac{{1}}{{{b}}}\\), "
        f"evaluate the numerical value of the expression:\n"
        f"\\[ \\frac{{x + y}}{{x \\times y}} \\]"
    )
    sol = (
        f"**Step 1: Calculate \\(x + y\\).**\n"
        f"\\[ x + y = \\frac{{1}}{{{a}}} + \\frac{{1}}{{{b}}} = \\frac{{{a_plus_b}}}{{{ab}}} \\]\n\n"
        f"**Step 2: Calculate \\(x \\times y\\).**\n"
        f"\\[ x \\times y = \\frac{{1}}{{{a}}} \\times \\frac{{1}}{{{b}}} = \\frac{{1}}{{{ab}}} \\]\n\n"
        f"**Step 3: Divide \\((x + y)\\) by \\((x \\times y)\\).**\n"
        f"\\[ \\frac{{\\frac{{{a_plus_b}}}{{{ab}}}}}{{\\frac{{1}}{{{ab}}}}} = \\frac{{{a_plus_b}}}{{{ab}}} \\times \\frac{{{ab}}}{{1}} "
        f"= {a + b} \\]"
    )
    return {
        "id": f"g9_frac_alg_sub_{rng.randint(100000, 999999)}",
        "question_type": "numeric",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": str(ans_val),
        "expected_answer": str(ans_val),
        "sample_answer": str(ans_val),
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "marking_schema": [
            {"desc": f"Calculate numerator sum ({a+b})/({a*b})", "marks": 1},
            {"desc": f"Calculate denominator product 1/({a*b})", "marks": 1},
            {"desc": f"Divide to obtain {ans_val}", "marks": 1},
        ],
        "hints": [
            f"Substitute x = 1/{a} and y = 1/{b}.",
            "Find the sum in the numerator and the product in the denominator.",
            f"The final integer value is {ans_val}.",
        ],
    }


# ----------------------------------------------------------------------
# 49. Error Analysis: Diagnose Fraction Operation Error
# ----------------------------------------------------------------------
def arch_49_error_analysis_diagnose_fraction_operation_error(rng: random.Random) -> Dict[str, Any]:
    # Error: adding numerators and adding denominators directly: 1/a + 1/b = 2/(a+b)
    a = rng.choice([2, 3])
    b = rng.choice([4, 5])
    wrong_num = 2
    wrong_den = a + b

    lcd = math.lcm(a, b)
    correct_n = (lcd // a) + (lcd // b)
    ans_latex = _frac_str(correct_n, lcd)
    ns, ds = _simplify(correct_n, lcd)
    ans_text = f"{ns}/{ds}"

    prompt = (
        f"A learner made an error in the following calculation:\n"
        f"\\[ \\frac{{1}}{{{a}}} + \\frac{{1}}{{{b}}} = \\frac{{1 + 1}}{{{a} + {b}}} = \\frac{{{wrong_num}}}{{{wrong_den}}} \\]\n"
        f"Explain why this method is mathematically incorrect, and provide the correct sum in simplest form."
    )
    sol = (
        f"**Conceptual Error Explanation:**\n"
        f"The learner incorrectly added both the numerators and the denominators together. "
        f"Fractions cannot be added by combining denominators because denominators name the size of each fractional part. "
        f"A common denominator (LCD) must be found first.\n\n"
        f"**Correct Calculation:**\n"
        f"\\(\\text{{LCD}}({a}, {b}) = {lcd}\\)\n"
        f"\\[ \\frac{{1}}{{{a}}} + \\frac{{1}}{{{b}}} = \\frac{{{lcd // a}}}{{{lcd}}} + \\frac{{{lcd // b}}}{{{lcd}}} "
        f"= \\frac{{{correct_n}}}{{{lcd}}} = {ans_latex} \\]"
    )
    return {
        "id": f"g9_frac_err_diag_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
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
            {"desc": "Identify that denominators cannot be added directly without finding an LCD", "marks": 1},
            {"desc": f"Determine correct LCD = {lcd}", "marks": 1},
            {"desc": f"Calculate correct sum {ans_latex}", "marks": 1},
        ],
        "hints": [
            "Denominators represent the type/size of parts and must be identical before adding.",
            f"Find the LCD of {a} and {b}, which is {lcd}.",
            f"The correct sum is {ans_text}.",
        ],
    }


# ----------------------------------------------------------------------
# 50. Compound Multi-Step Fraction Capstone
# ----------------------------------------------------------------------
def arch_50_compound_multi_step_fraction_capstone(rng: random.Random) -> Dict[str, Any]:
    # (1 1/2 + 2/3) * sqrt(9/16) - (1/2)^2
    # 1 1/2 + 2/3 = 3/2 + 2/3 = 9/6 + 4/6 = 13/6
    # sqrt(9/16) = 3/4
    # (13/6) * (3/4) = 13/8
    # (1/2)^2 = 1/4 = 2/8
    # 13/8 - 2/8 = 11/8 = 1 3/8
    choices = [
        # (w1, r1, d1, r2, d2, sq_n, sq_d, p_n, p_d)
        (1, 1, 2, 2, 3, 9, 16, 1, 2),
        (1, 1, 4, 1, 3, 16, 25, 1, 5),
        (2, 1, 2, 1, 4, 4, 9, 1, 3),
        (1, 1, 3, 1, 2, 25, 36, 1, 4),
        (1, 2, 3, 1, 4, 9, 25, 1, 5),
        (2, 1, 3, 1, 6, 1, 4, 1, 2),
        (1, 3, 4, 1, 2, 4, 25, 1, 5),
        (2, 2, 5, 1, 2, 9, 49, 1, 7),
    ]
    w1, r1, d1, r2, d2, sq_n, sq_d, p_n, p_d = rng.choice(choices)

    # Compute step by step:
    imp1_n = w1 * d1 + r1
    brack_lcd = math.lcm(d1, d2)
    b_sum_n = imp1_n * (brack_lcd // d1) + r2 * (brack_lcd // d2)
    b_sum_d = brack_lcd

    root_n = int(round(math.isqrt(sq_n)))
    root_d = int(round(math.isqrt(sq_d)))

    prod_n = b_sum_n * root_n
    prod_d = b_sum_d * root_d

    pow_n = p_n ** 2
    pow_d = p_d ** 2

    final_lcd = math.lcm(prod_d, pow_d)
    final_n = prod_n * (final_lcd // prod_d) - pow_n * (final_lcd // pow_d)
    final_d = final_lcd

    ans_latex = _mixed_str(final_n, final_d)
    ns, ds = _simplify(final_n, final_d)
    ans_text = f"{ns}/{ds}"

    prompt = (
        f"Evaluate the comprehensive multi-step mathematical expression in simplest form:\n"
        f"\\[ \\left( {w1}\\frac{{{r1}}}{{{d1}}} + \\frac{{{r2}}}{{{d2}}} \\right) "
        f"\\times \\sqrt{{\\frac{{{sq_n}}}{{{sq_d}}}}} - \\left( \\frac{{{p_n}}}{{{p_d}}} \\right)^2 \\]"
    )
    sol = (
        f"**Step 1: Evaluate the sum inside the brackets.**\n"
        f"\\[ {w1}\\frac{{{r1}}}{{{d1}}} + \\frac{{{r2}}}{{{d2}}} = \\frac{{{imp1_n}}}{{{d1}}} + \\frac{{{r2}}}{{{d2}}} "
        f"= \\frac{{{b_sum_n}}}{{{b_sum_d}}} \\]\n\n"
        f"**Step 2: Evaluate the square root and power.**\n"
        f"\\[ \\sqrt{{\\frac{{{sq_n}}}{{{sq_d}}}}} = \\frac{{{root_n}}}{{{root_d}}}, \\quad "
        f"\\left( \\frac{{{p_n}}}{{{p_d}}} \\right)^2 = \\frac{{{pow_n}}}{{{pow_d}}} \\]\n\n"
        f"**Step 3: Perform multiplication before subtraction (BODMAS).**\n"
        f"\\[ \\frac{{{b_sum_n}}}{{{b_sum_d}}} \\times \\frac{{{root_n}}}{{{root_d}}} = \\frac{{{prod_n}}}{{{prod_d}}} \\]\n\n"
        f"**Step 4: Subtract using the common denominator {final_lcd}.**\n"
        f"\\[ \\frac{{{prod_n}}}{{{prod_d}}} - \\frac{{{pow_n}}}{{{pow_d}}} = \\frac{{{final_n}}}{{{final_d}}} = {ans_latex} \\]"
    )
    return {
        "id": f"g9_frac_capstone_{rng.randint(100000, 999999)}",
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
        "marks": 4,
        "marking_schema": [
            {"desc": f"Evaluate bracketed sum to get {b_sum_n}/{b_sum_d}", "marks": 1},
            {"desc": f"Evaluate square root as {root_n}/{root_d} and power as {pow_n}/{pow_d}", "marks": 1},
            {"desc": f"Multiply to obtain {prod_n}/{prod_d}", "marks": 1},
            {"desc": f"Complete subtraction to obtain {ans_latex}", "marks": 1},
        ],
        "hints": [
            "Follow BODMAS: Brackets first, then Powers and Roots, then Multiplication, and finally Subtraction.",
            f"Inside brackets = {b_sum_n}/{b_sum_d}.",
            f"Final result is {ans_latex}.",
        ],
    }
