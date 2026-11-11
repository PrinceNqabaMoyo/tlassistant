"""
Grade 8 Mathematics - Common Fractions Archetypes (26 to 50).
100% CAPS-aligned deterministic question generator.
Adheres strictly to the 6-Pillar Generator Contract and Zero-Meta-Curriculum Invariant.
Grounded in curriculum_docs/Mathematics_Gr8/Numbers-Operations-and-Relationships Studio.md (Term 3 Common Fractions).
"""
from __future__ import annotations

import math
import random
from typing import Any, Callable, Dict, List, Optional


# ----------------------------------------------------------------------
# 26. Division Two Proper Fractions
# ----------------------------------------------------------------------
def arch_26_division_two_proper_fractions(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([2, 3, 4])
    b = rng.choice([5, 7, 9])
    c = rng.choice([2, 3, 5])
    d = rng.choice([4, 6, 8])
    while math.gcd(a, b) != 1:
        b += 1
    while math.gcd(c, d) != 1:
        d += 1
    # a/b ÷ c/d = (a * d) / (b * c)
    num = a * d
    den = b * c
    g = math.gcd(num, den)
    ans_num = num // g
    ans_den = den // g

    prompt = (
        f"Calculate and simplify:\n"
        f"\\[ \\frac{{{a}}}{{{b}}} \\div \\frac{{{c}}}{{{d}}} \\]"
    )
    sol = (
        f"**Step 1:** Invert the second fraction (the divisor) and change division to multiplication:\n"
        f"\\[ \\frac{{{a}}}{{{b}}} \\div \\frac{{{c}}}{{{d}}} = \\frac{{{a}}}{{{b}}} \\times \\frac{{{d}}}{{{c}}} \\]\n\n"
        f"**Step 2:** Multiply numerators and denominators:\n"
        f"\\[ \\frac{{{a} \\times {d}}}{{{b} \\times {c}}} = \\frac{{{num}}}{{{den}}} \\]\n\n"
        f"**Step 3:** Simplify to lowest terms:\n"
        f"\\[ \\frac{{{ans_num}}}{{{ans_den}}} \\]"
    )
    if ans_num >= ans_den and ans_den != 1:
        ans = f"{ans_num // ans_den} {ans_num % ans_den}/{ans_den}"
    elif ans_den == 1:
        ans = str(ans_num)
    else:
        ans = f"{ans_num}/{ans_den}"
    return {
        "id": f"g8_frac_div_2_{rng.randint(100000, 999999)}",
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
        "subskill": "26_division_two_proper_fractions",
        "learning_objective_id": "math_g8_frac_div_two_proper",
        "hints": {
            "tier_1": f"Multiply by the reciprocal: {a}/{b} × {d}/{c}.",
            "tier_2": f"({a} × {d}) / ({b} × {c}) = {num}/{den}.",
            "tier_3": f"{ans}.",
        },
        "misconception_tags": ["inverting_dividend_instead_of_divisor"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 27. Division Mixed Numbers
# ----------------------------------------------------------------------
def arch_27_division_mixed_numbers(rng: random.Random) -> Dict[str, Any]:
    w1 = rng.choice([2, 3])
    w2 = 1
    b = rng.choice([2, 3, 4])
    d = rng.choice([3, 5])
    a = 1
    c = 1
    imp1 = w1 * b + a
    imp2 = w2 * d + c
    # (imp1 / b) ÷ (imp2 / d) = (imp1 * d) / (b * imp2)
    num = imp1 * d
    den = b * imp2
    g = math.gcd(num, den)
    ans_num = num // g
    ans_den = den // g

    prompt = (
        f"Divide the mixed numbers and write in simplest form:\n"
        f"\\[ {w1} \\frac{{{a}}}{{{b}}} \\div {w2} \\frac{{{c}}}{{{d}}} \\]"
    )
    sol = (
        f"**Step 1:** Convert both mixed numbers into improper fractions:\n"
        f"\\[ {w1} \\frac{{{a}}}{{{b}}} = \\frac{{{imp1}}}{{{b}}} \\quad \\text{{and}} \\quad {w2} \\frac{{{c}}}{{{d}}} = \\frac{{{imp2}}}{{{d}}} \\]\n\n"
        f"**Step 2:** Multiply by the reciprocal of the divisor:\n"
        f"\\[ \\frac{{{imp1}}}{{{b}}} \\times \\frac{{{d}}}{{{imp2}}} = \\frac{{{num}}}{{{den}}} = \\frac{{{ans_num}}}{{{ans_den}}} \\]"
    )
    if ans_num >= ans_den:
        w = ans_num // ans_den
        rem = ans_num % ans_den
        ans = f"{w} {rem}/{ans_den}" if rem > 0 else str(w)
    else:
        ans = f"{ans_num}/{ans_den}"
    return {
        "id": f"g8_frac_div_mix_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 4,
        "subskill": "27_division_mixed_numbers",
        "learning_objective_id": "math_g8_frac_div_mixed",
        "hints": {
            "tier_1": f"Convert to improper fractions first: {imp1}/{b} ÷ {imp2}/{d}.",
            "tier_2": f"Multiply {imp1}/{b} by {d}/{imp2}.",
            "tier_3": f"{ans}.",
        },
        "misconception_tags": ["dividing_whole_numbers_and_fractions_separately"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 28. Squaring Proper Fraction
# ----------------------------------------------------------------------
def arch_28_squaring_proper_fraction(rng: random.Random) -> Dict[str, Any]:
    b = rng.choice([3, 4, 5, 7, 9])
    a = rng.choice([2, 3, 4])
    while a >= b or math.gcd(a, b) != 1:
        a = rng.choice(range(1, b))
    sq_num = a ** 2
    sq_den = b ** 2

    prompt = (
        f"Calculate the square of the common fraction:\n"
        f"\\[ \\left(\\frac{{{a}}}{{{b}}}\\right)^2 \\]"
    )
    sol = (
        f"**Step 1:** Apply the exponent to both the numerator and the denominator:\n"
        f"\\[ \\left(\\frac{{{a}}}{{{b}}}\\right)^2 = \\frac{{{a}^2}}{{{b}^2}} \\]\n\n"
        f"**Step 2:** Calculate each power:\n"
        f"\\[ \\frac{{{sq_num}}}{{{sq_den}}} \\]"
    )
    ans = f"{sq_num}/{sq_den}"
    return {
        "id": f"g8_frac_sq_{rng.randint(100000, 999999)}",
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
        "subskill": "28_squaring_proper_fraction",
        "learning_objective_id": "math_g8_frac_squaring_proper",
        "hints": {
            "tier_1": f"Square the numerator and square the denominator.",
            "tier_2": f"{a}^2 = {sq_num}; {b}^2 = {sq_den}.",
            "tier_3": f"{sq_num}/{sq_den}.",
        },
        "misconception_tags": ["squaring_only_numerator"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 29. Squaring Mixed Number
# ----------------------------------------------------------------------
def arch_29_squaring_mixed_number(rng: random.Random) -> Dict[str, Any]:
    w = rng.choice([1, 2])
    b = rng.choice([2, 3, 4])
    a = 1
    imp = w * b + a
    sq_num = imp ** 2
    sq_den = b ** 2
    w_ans = sq_num // sq_den
    rem_ans = sq_num % sq_den

    prompt = (
        f"Calculate and write your answer as a simplified mixed number:\n"
        f"\\[ \\left({w} \\frac{{{a}}}{{{b}}}\\right)^2 \\]"
    )
    sol = (
        f"**Step 1:** Convert the mixed number to an improper fraction first:\n"
        f"\\[ {w} \\frac{{{a}}}{{{b}}} = \\frac{{{imp}}}{{{b}}} \\]\n\n"
        f"**Step 2:** Square both numerator and denominator:\n"
        f"\\[ \\left(\\frac{{{imp}}}{{{b}}}\\right)^2 = \\frac{{{sq_num}}}{{{sq_den}}} \\]\n\n"
        f"**Step 3:** Convert to a mixed number:\n"
        f"\\[ \\frac{{{sq_num}}}{{{sq_den}}} = {w_ans} \\frac{{{rem_ans}}}{{{sq_den}}} \\]"
    )
    ans = f"{w_ans} {rem_ans}/{sq_den}"
    return {
        "id": f"g8_frac_sq_mix_{rng.randint(100000, 999999)}",
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
        "subskill": "29_squaring_mixed_number",
        "learning_objective_id": "math_g8_frac_squaring_mixed",
        "hints": {
            "tier_1": f"Convert to improper fraction ({imp}/{b}) before squaring.",
            "tier_2": f"({imp}/{b})^2 = {sq_num}/{sq_den}.",
            "tier_3": f"{ans}.",
        },
        "misconception_tags": ["squaring_whole_and_fraction_separately"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 30. Cubing Proper Fraction
# ----------------------------------------------------------------------
def arch_30_cubing_proper_fraction(rng: random.Random) -> Dict[str, Any]:
    b = rng.choice([2, 3, 4, 5])
    a = 1 if b == 2 else rng.choice(range(1, b))
    while math.gcd(a, b) != 1:
        a = (a + 1) % b or 1
    cube_num = a ** 3
    cube_den = b ** 3

    prompt = (
        f"Calculate the cube of the common fraction:\n"
        f"\\[ \\left(\\frac{{{a}}}{{{b}}}\\right)^3 \\]"
    )
    sol = (
        f"**Step 1:** Cube both numerator and denominator:\n"
        f"\\[ \\left(\\frac{{{a}}}{{{b}}}\\right)^3 = \\frac{{{a}^3}}{{{b}^3}} \\]\n\n"
        f"**Step 2:** Calculate powers:\n"
        f"\\[ \\frac{{{cube_num}}}{{{cube_den}}} \\]"
    )
    ans = f"{cube_num}/{cube_den}"
    return {
        "id": f"g8_frac_cube_{rng.randint(100000, 999999)}",
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
        "subskill": "30_cubing_proper_fraction",
        "learning_objective_id": "math_g8_frac_cubing_proper",
        "hints": {
            "tier_1": f"Multiply the fraction by itself 3 times.",
            "tier_2": f"{a}^3 = {cube_num}; {b}^3 = {cube_den}.",
            "tier_3": f"{cube_num}/{cube_den}.",
        },
        "misconception_tags": ["multiplying_by_3_instead_of_cubing"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 31. Square Root Of Proper Fraction
# ----------------------------------------------------------------------
def arch_31_square_root_of_proper_fraction(rng: random.Random) -> Dict[str, Any]:
    b = rng.choice([3, 4, 5, 7, 8, 10])
    a = rng.choice(range(1, b))
    while math.gcd(a, b) != 1:
        a = (a + 1) % b or 1
    num = a ** 2
    den = b ** 2

    prompt = (
        f"Determine the square root by inspection:\n"
        f"\\[ \\sqrt{{\\frac{{{num}}}{{{den}}}}} \\]"
    )
    sol = (
        f"**Step 1:** Take the square root of the numerator and the denominator separately:\n"
        f"\\[ \\sqrt{{\\frac{{{num}}}{{{den}}}}} = \\frac{{\\sqrt{{{num}}}}}{{\\sqrt{{{den}}}}} \\]\n\n"
        f"**Step 2:** Evaluate roots:\n"
        f"\\[ \\frac{{{a}}}{{{b}}} \\]"
    )
    ans = f"{a}/{b}"
    return {
        "id": f"g8_frac_sqrt_{rng.randint(100000, 999999)}",
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
        "subskill": "31_square_root_of_proper_fraction",
        "learning_objective_id": "math_g8_frac_sqrt_proper",
        "hints": {
            "tier_1": f"√({num}/{den}) = √{num} / √{den}.",
            "tier_2": f"What number squared equals {num}? What squared equals {den}?",
            "tier_3": f"{a}/{b}.",
        },
        "misconception_tags": ["dividing_by_2_instead_of_square_root"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 32. Square Root Of Mixed Number
# ----------------------------------------------------------------------
def arch_32_square_root_of_mixed_number(rng: random.Random) -> Dict[str, Any]:
    # Form: (imp/b)^2 where b in [2, 3, 4, 5] and imp > b
    b = rng.choice([2, 3, 4])
    imp = b + rng.choice([1, 2])
    while math.gcd(imp, b) != 1:
        imp += 1
    sq_num = imp ** 2
    sq_den = b ** 2
    w = sq_num // sq_den
    rem = sq_num % sq_den

    prompt = (
        f"Calculate the square root of the mixed number:\n"
        f"\\[ \\sqrt{{{w} \\frac{{{rem}}}{{{sq_den}}}}} \\]"
    )
    sol = (
        f"**Step 1:** Convert the mixed number into an improper fraction first:\n"
        f"\\[ {w} \\frac{{{rem}}}{{{sq_den}}} = \\frac{{{w} \\times {sq_den} + {rem}}}{{{sq_den}}} = \\frac{{{sq_num}}}{{{sq_den}}} \\]\n\n"
        f"**Step 2:** Take the square root of numerator and denominator:\n"
        f"\\[ \\sqrt{{\\frac{{{sq_num}}}{{{sq_den}}}}} = \\frac{{\\sqrt{{{sq_num}}}}}{{\\sqrt{{{sq_den}}}}} = \\frac{{{imp}}}{{{b}}} \\]\n\n"
        f"**Step 3:** Convert to mixed number:\n"
        f"\\[ \\frac{{{imp}}}{{{b}}} = {imp // b} \\frac{{{imp % b}}}{{{b}}} \\]"
    )
    ans = f"{imp // b} {imp % b}/{b}"
    return {
        "id": f"g8_frac_sqrt_mix_{rng.randint(100000, 999999)}",
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
        "subskill": "32_square_root_of_mixed_number",
        "learning_objective_id": "math_g8_frac_sqrt_mixed",
        "hints": {
            "tier_1": f"Convert {w} {rem}/{sq_den} to improper fraction {sq_num}/{sq_den}.",
            "tier_2": f"√{sq_num} / √{sq_den} = {imp}/{b}.",
            "tier_3": f"{ans}.",
        },
        "misconception_tags": ["taking_square_root_of_whole_and_fraction_separately"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 33. Cube Root Of Proper Fraction
# ----------------------------------------------------------------------
def arch_33_cube_root_of_proper_fraction(rng: random.Random) -> Dict[str, Any]:
    b = rng.choice([2, 3, 4, 5])
    a = 1 if b == 2 else rng.choice(range(1, b))
    while math.gcd(a, b) != 1:
        a = (a + 1) % b or 1
    num = a ** 3
    den = b ** 3

    prompt = (
        f"Determine the cube root by inspection:\n"
        f"\\[ \\sqrt[3]{{\\frac{{{num}}}{{{den}}}}} \\]"
    )
    sol = (
        f"**Step 1:** Apply the cube root to both numerator and denominator:\n"
        f"\\[ \\sqrt[3]{{\\frac{{{num}}}{{{den}}}}} = \\frac{{\\sqrt[3]{{{num}}}}}{{\\sqrt[3]{{{den}}}}} \\]\n\n"
        f"**Step 2:** Evaluate roots:\n"
        f"\\[ \\frac{{{a}}}{{{b}}} \\]"
    )
    ans = f"{a}/{b}"
    return {
        "id": f"g8_frac_cbrt_{rng.randint(100000, 999999)}",
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
        "subskill": "33_cube_root_of_proper_fraction",
        "learning_objective_id": "math_g8_frac_cbrt_proper",
        "hints": {
            "tier_1": f"Find what number multiplied by itself 3 times gives {num} and {den}.",
            "tier_2": f"{a}^3 = {num}; {b}^3 = {den}.",
            "tier_3": f"{a}/{b}.",
        },
        "misconception_tags": ["dividing_by_3_instead_of_cube_root"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 34. Cube Root Of Mixed Number
# ----------------------------------------------------------------------
def arch_34_cube_root_of_mixed_number(rng: random.Random) -> Dict[str, Any]:
    b = 2
    imp = 3
    # (3/2)^3 = 27/8 = 3 3/8
    cube_num = imp ** 3
    cube_den = b ** 3
    w = cube_num // cube_den
    rem = cube_num % cube_den

    prompt = (
        f"Calculate the cube root of the mixed number:\n"
        f"\\[ \\sqrt[3]{{{w} \\frac{{{rem}}}{{{cube_den}}}}} \\]"
    )
    sol = (
        f"**Step 1:** Convert to an improper fraction:\n"
        f"\\[ {w} \\frac{{{rem}}}{{{cube_den}}} = \\frac{{{w} \\times {cube_den} + {rem}}}{{{cube_den}}} = \\frac{{{cube_num}}}{{{cube_den}}} \\]\n\n"
        f"**Step 2:** Take the cube root of numerator and denominator:\n"
        f"\\[ \\frac{{\\sqrt[3]{{{cube_num}}}}}{{\\sqrt[3]{{{cube_den}}}}} = \\frac{{{imp}}}{{{b}}} = {imp // b} \\frac{{{imp % b}}}{{{b}}} \\]"
    )
    ans = f"{imp // b} {imp % b}/{b}"
    return {
        "id": f"g8_frac_cbrt_mix_{rng.randint(100000, 999999)}",
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
        "subskill": "34_cube_root_of_mixed_number",
        "learning_objective_id": "math_g8_frac_cbrt_mixed",
        "hints": {
            "tier_1": f"Convert to improper fraction: {cube_num}/{cube_den}.",
            "tier_2": f"∛{cube_num} / ∛{cube_den} = {imp}/{b}.",
            "tier_3": f"{ans}.",
        },
        "misconception_tags": ["taking_cube_root_of_fraction_without_converting_to_improper"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 35. BODMAS Brackets And Addition
# ----------------------------------------------------------------------
def arch_35_bodmas_brackets_and_addition(rng: random.Random) -> Dict[str, Any]:
    # a/b * (c/d + e/f)
    a, b = 2, 3
    c, d = 1, 4
    e, f = 1, 2
    # c/d + e/f = 1/4 + 2/4 = 3/4
    # a/b * 3/4 = 2/3 * 3/4 = 2/4 = 1/2
    prompt = (
        f"Evaluate using the correct order of operations (BODMAS):\n"
        f"\\[ \\frac{{{a}}}{{{b}}} \\times \\left(\\frac{{{c}}}{{{d}}} + \\frac{{{e}}}{{{f}}}\\right) \\]"
    )
    sol = (
        f"**Step 1:** Calculate the expression inside the brackets first (LCD of {d} and {f} is {d}):\n"
        f"\\[ \\frac{{{c}}}{{{d}}} + \\frac{{{e}}}{{{f}}} = \\frac{{{c}}}{{{d}}} + \\frac{{{e * (d // f)}}}{{{d}}} = \\frac{{{c + e * (d // f)}}}{{{d}}} = \\frac{{3}}{{4}} \\]\n\n"
        f"**Step 2:** Multiply by the outside fraction:\n"
        f"\\[ \\frac{{{a}}}{{{b}}} \\times \\frac{{3}}{{4}} = \\frac{{{a} \\times 3}}{{{b} \\times 4}} = \\frac{{6}}{{12}} = \\frac{{1}}{{2}} \\]"
    )
    ans = "1/2"
    return {
        "id": f"g8_frac_bod_brk_{rng.randint(100000, 999999)}",
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
        "subskill": "35_bodmas_brackets_and_addition",
        "learning_objective_id": "math_g8_frac_bodmas_brackets",
        "hints": {
            "tier_1": f"Work inside brackets first.",
            "tier_2": f"1/4 + 1/2 = 3/4.",
            "tier_3": f"2/3 × 3/4 = 1/2.",
        },
        "misconception_tags": ["multiplying_before_brackets"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 36. BODMAS Multiplication Before Addition
# ----------------------------------------------------------------------
def arch_36_bodmas_multiplication_before_addition(rng: random.Random) -> Dict[str, Any]:
    # a/b + c/d * e/f
    a, b = 1, 2
    c, d = 2, 3
    e, f = 3, 4
    # c/d * e/f = 6/12 = 1/2
    # 1/2 + 1/2 = 1
    prompt = (
        f"Evaluate using BODMAS rules:\n"
        f"\\[ \\frac{{{a}}}{{{b}}} + \\frac{{{c}}}{{{d}}} \\times \\frac{{{e}}}{{{f}}} \\]"
    )
    sol = (
        f"**Step 1:** Perform multiplication before addition:\n"
        f"\\[ \\frac{{{c}}}{{{d}}} \\times \\frac{{{e}}}{{{f}}} = \\frac{{{c * e}}}{{{d * f}}} = \\frac{{6}}{{12}} = \\frac{{1}}{{2}} \\]\n\n"
        f"**Step 2:** Add the result to \\(\\frac{{{a}}}{{{b}}}\\):\n"
        f"\\[ \\frac{{{a}}}{{{b}}} + \\frac{{1}}{{2}} = \\frac{{1}}{{2}} + \\frac{{1}}{{2}} = 1 \\]"
    )
    ans = "1"
    return {
        "id": f"g8_frac_bod_mult_{rng.randint(100000, 999999)}",
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
        "subskill": "36_bodmas_multiplication_before_addition",
        "learning_objective_id": "math_g8_frac_bodmas_mult_add",
        "hints": {
            "tier_1": f"Multiplication takes precedence over addition.",
            "tier_2": f"Calculate {c}/{d} × {e}/{f} = 1/2 first.",
            "tier_3": f"1/2 + 1/2 = 1.",
        },
        "misconception_tags": ["adding_before_multiplying_from_left_to_right"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 37. BODMAS Division Before Subtraction
# ----------------------------------------------------------------------
def arch_37_bodmas_division_before_subtraction(rng: random.Random) -> Dict[str, Any]:
    # a/b - c/d ÷ e/f
    a, b = 3, 4
    c, d = 1, 2
    e, f = 2, 1
    # c/d ÷ e/f = 1/2 * 1/2 = 1/4
    # 3/4 - 1/4 = 2/4 = 1/2
    prompt = (
        f"Evaluate applying order of operations:\n"
        f"\\[ \\frac{{{a}}}{{{b}}} - \\frac{{{c}}}{{{d}}} \\div 2 \\]"
    )
    sol = (
        f"**Step 1:** Perform division before subtraction:\n"
        f"\\[ \\frac{{{c}}}{{{d}}} \\div 2 = \\frac{{{c}}}{{{d}}} \\times \\frac{{1}}{{2}} = \\frac{{1}}{{4}} \\]\n\n"
        f"**Step 2:** Subtract from \\(\\frac{{{a}}}{{{b}}}\\):\n"
        f"\\[ \\frac{{{a}}}{{{b}}} - \\frac{{1}}{{4}} = \\frac{{3}}{{4}} - \\frac{{1}}{{4}} = \\frac{{2}}{{4}} = \\frac{{1}}{{2}} \\]"
    )
    ans = "1/2"
    return {
        "id": f"g8_frac_bod_div_{rng.randint(100000, 999999)}",
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
        "subskill": "37_bodmas_division_before_subtraction",
        "learning_objective_id": "math_g8_frac_bodmas_div_sub",
        "hints": {
            "tier_1": f"Division takes precedence over subtraction.",
            "tier_2": f"1/2 ÷ 2 = 1/4.",
            "tier_3": f"3/4 - 1/4 = 1/2.",
        },
        "misconception_tags": ["subtracting_before_dividing"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 38. BODMAS Powers And Operations
# ----------------------------------------------------------------------
def arch_38_bodmas_powers_and_operations(rng: random.Random) -> Dict[str, Any]:
    # (1/2)^2 + 1/4 * 2 = 1/4 + 2/4 = 3/4
    prompt = (
        f"Calculate the value using BODMAS:\n"
        f"\\[ \\left(\\frac{{1}}{{2}}\\right)^2 + \\frac{{1}}{{4}} \\times 2 \\]"
    )
    sol = (
        f"**Step 1:** Evaluate the exponent (Orders) first:\n"
        f"\\[ \\left(\\frac{{1}}{{2}}\\right)^2 = \\frac{{1}}{{4}} \\]\n\n"
        f"**Step 2:** Perform multiplication:\n"
        f"\\[ \\frac{{1}}{{4}} \\times 2 = \\frac{{2}}{{4}} = \\frac{{1}}{{2}} \\]\n\n"
        f"**Step 3:** Perform addition:\n"
        f"\\[ \\frac{{1}}{{4}} + \\frac{{2}}{{4}} = \\frac{{3}}{{4}} \\]"
    )
    ans = "3/4"
    return {
        "id": f"g8_frac_bod_pwr_{rng.randint(100000, 999999)}",
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
        "subskill": "38_bodmas_powers_and_operations",
        "learning_objective_id": "math_g8_frac_bodmas_powers",
        "hints": {
            "tier_1": f"Orders (powers) come before multiplication and addition.",
            "tier_2": f"(1/2)^2 = 1/4 and 1/4 × 2 = 2/4.",
            "tier_3": f"1/4 + 2/4 = 3/4.",
        },
        "misconception_tags": ["adding_before_evaluating_powers"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 39. BODMAS Roots And Operations
# ----------------------------------------------------------------------
def arch_39_bodmas_roots_and_operations(rng: random.Random) -> Dict[str, Any]:
    # sqrt(9/16) - 1/2 * 1/2 = 3/4 - 1/4 = 2/4 = 1/2
    prompt = (
        f"Calculate using the order of operations:\n"
        f"\\[ \\sqrt{{\\frac{{9}}{{16}}}} - \\frac{{1}}{{2}} \\times \\frac{{1}}{{2}} \\]"
    )
    sol = (
        f"**Step 1:** Evaluate the square root first:\n"
        f"\\[ \\sqrt{{\\frac{{9}}{{16}}}} = \\frac{{3}}{{4}} \\]\n\n"
        f"**Step 2:** Perform multiplication:\n"
        f"\\[ \\frac{{1}}{{2}} \\times \\frac{{1}}{{2}} = \\frac{{1}}{{4}} \\]\n\n"
        f"**Step 3:** Perform subtraction:\n"
        f"\\[ \\frac{{3}}{{4}} - \\frac{{1}}{{4}} = \\frac{{2}}{{4}} = \\frac{{1}}{{2}} \\]"
    )
    ans = "1/2"
    return {
        "id": f"g8_frac_bod_root_{rng.randint(100000, 999999)}",
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
        "subskill": "39_bodmas_roots_and_operations",
        "learning_objective_id": "math_g8_frac_bodmas_roots",
        "hints": {
            "tier_1": f"Root comes first, then multiplication, then subtraction.",
            "tier_2": f"√(9/16) = 3/4 and 1/2 × 1/2 = 1/4.",
            "tier_3": f"3/4 - 1/4 = 1/2.",
        },
        "misconception_tags": ["subtracting_before_multiplying"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 40. Word Problem Fraction Of Pocket Money Spent
# ----------------------------------------------------------------------
def arch_40_word_problem_fraction_of_pocket_money_spent(rng: random.Random) -> Dict[str, Any]:
    total_money = rng.choice([240, 300, 360, 480])
    # spends 1/3 on food, 1/4 on transport
    # fraction spent = 1/3 + 1/4 = 7/12
    # fraction remaining = 5/12
    spent_food = total_money // 3
    spent_trans = total_money // 4
    rem_money = total_money - (spent_food + spent_trans)

    prompt = (
        f"Thabo receives a monthly allowance of **R{total_money}**. "
        f"He spends \\(\\frac{{1}}{{3}}\\) of his allowance on lunches and \\(\\frac{{1}}{{4}}\\) on transport.\n\n"
        f"1. What fraction of his allowance has he spent in total?\n"
        f"2. What fraction of his allowance remains?\n"
        f"3. Calculate the exact amount of money in Rands that Thabo has left."
    )
    sol = (
        f"**Step 1: Fraction spent**\n"
        f"LCD of 3 and 4 is 12:\n"
        f"\\[ \\frac{{1}}{{3}} + \\frac{{1}}{{4}} = \\frac{{4}}{{12}} + \\frac{{3}}{{12}} = \\frac{{7}}{{12}} \\]\n\n"
        f"**Step 2: Fraction remaining**\n"
        f"\\[ 1 - \\frac{{7}}{{12}} = \\frac{{12}}{{12}} - \\frac{{7}}{{12}} = \\frac{{5}}{{12}} \\]\n\n"
        f"**Step 3: Amount remaining**\n"
        f"\\[ \\frac{{5}}{{12}} \\times R{total_money} = 5 \\times R{total_money // 12} = R{rem_money} \\]"
    )
    ans = f"1. 7/12; 2. 5/12; 3. R{rem_money}"
    return {
        "id": f"g8_frac_pocket_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 4,
        "subskill": "40_word_problem_fraction_of_pocket_money_spent",
        "learning_objective_id": "math_g8_frac_pocket_money",
        "hints": {
            "tier_1": f"Add fractions spent: 1/3 + 1/4 = 7/12.",
            "tier_2": f"Remaining fraction = 1 - 7/12 = 5/12.",
            "tier_3": f"5/12 of R{total_money} = R{rem_money}.",
        },
        "misconception_tags": ["adding_denominators_giving_2_7"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 41. Word Problem Fractional Sharing Recipe
# ----------------------------------------------------------------------
def arch_41_word_problem_fractional_sharing_recipe(rng: random.Random) -> Dict[str, Any]:
    cups_flour = 2  # 2 1/2 cups
    batches = 3     # 1 1/2 batches
    # 2 1/2 * 1 1/2 = 5/2 * 3/2 = 15/4 = 3 3/4
    prompt = (
        f"A standard muffin recipe requires \\(2 \\frac{{1}}{{2}}\\) cups of flour. "
        f"A baker wishes to bake \\(1 \\frac{{1}}{{2}}\\) batches of the recipe.\n\n"
        f"How many cups of flour will the baker need in total? Express your answer as a mixed number in simplest form."
    )
    sol = (
        f"**Step 1:** Convert both mixed numbers to improper fractions:\n"
        f"\\[ 2 \\frac{{1}}{{2}} = \\frac{{5}}{{2}} \\quad \\text{{and}} \\quad 1 \\frac{{1}}{{2}} = \\frac{{3}}{{2}} \\]\n\n"
        f"**Step 2:** Multiply the two fractions:\n"
        f"\\[ \\frac{{5}}{{2}} \\times \\frac{{3}}{{2}} = \\frac{{15}}{{4}} \\]\n\n"
        f"**Step 3:** Convert to a mixed number:\n"
        f"\\[ \\frac{{15}}{{4}} = 3 \\frac{{3}}{{4}} \\text{{ cups}} \\]"
    )
    ans = "3 3/4 cups"
    return {
        "id": f"g8_frac_recipe_{rng.randint(100000, 999999)}",
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
        "subskill": "41_word_problem_fractional_sharing_recipe",
        "learning_objective_id": "math_g8_frac_recipe_scaling",
        "hints": {
            "tier_1": f"Multiply cups per batch by number of batches.",
            "tier_2": f"5/2 × 3/2 = 15/4.",
            "tier_3": f"3 3/4 cups.",
        },
        "misconception_tags": ["adding_quantities_instead_of_multiplying"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 42. Word Problem Journey Fraction Remaining
# ----------------------------------------------------------------------
def arch_42_word_problem_journey_fraction_remaining(rng: random.Random) -> Dict[str, Any]:
    total_dist = rng.choice([360, 420, 480, 600])
    # 2/5 in morning, 1/3 in afternoon
    # 2/5 + 1/3 = 6/15 + 5/15 = 11/15
    # rem = 4/15
    rem_dist = (total_dist * 4) // 15

    prompt = (
        f"A family drives a total distance of **{total_dist} km** on vacation. "
        f"They travel \\(\\frac{{2}}{{5}}\\) of the journey in the morning and \\(\\frac{{1}}{{3}}\\) of the journey in the afternoon.\n\n"
        f"1. What fraction of the total journey did they complete during the day?\n"
        f"2. What fraction remains to be driven?\n"
        f"3. How many kilometers do they still have left to drive?"
    )
    sol = (
        f"**Step 1: Fraction completed**\n"
        f"LCD of 5 and 3 is 15:\n"
        f"\\[ \\frac{{2}}{{5}} + \\frac{{1}}{{3}} = \\frac{{6}}{{15}} + \\frac{{5}}{{15}} = \\frac{{11}}{{15}} \\]\n\n"
        f"**Step 2: Fraction remaining**\n"
        f"\\[ 1 - \\frac{{11}}{{15}} = \\frac{{4}}{{15}} \\]\n\n"
        f"**Step 3: Kilometers remaining**\n"
        f"\\[ \\frac{{4}}{{15}} \\times {total_dist} = 4 \\times {total_dist // 15} = {rem_dist} \\text{{ km}} \\]"
    )
    ans = f"1. 11/15; 2. 4/15; 3. {rem_dist} km"
    return {
        "id": f"g8_frac_journey_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 4,
        "subskill": "42_word_problem_journey_fraction_remaining",
        "learning_objective_id": "math_g8_frac_journey_fraction",
        "hints": {
            "tier_1": f"2/5 + 1/3 = 11/15.",
            "tier_2": f"Remaining fraction = 1 - 11/15 = 4/15.",
            "tier_3": f"4/15 of {total_dist} km = {rem_dist} km.",
        },
        "misconception_tags": ["adding_denominators_giving_3_8"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 43. Word Problem Cutting Ribbon Division
# ----------------------------------------------------------------------
def arch_43_word_problem_cutting_ribbon_division(rng: random.Random) -> Dict[str, Any]:
    # e.g., 6 meters cut into pieces of 3/4 meters => 6 ÷ 3/4 = 6 * 4/3 = 8 pieces
    m = rng.choice([6, 9, 12, 15])
    # pieces of 3/4 meter
    num_pieces = (m * 4) // 3

    prompt = (
        f"A roll of decorative ribbon measures **{m} meters** in length. "
        f"A dressmaker cuts the entire roll into shorter strips measuring \\(\\frac{{3}}{{4}}\\) meter each.\n\n"
        f"How many complete ribbon strips can be cut from the roll?"
    )
    sol = (
        f"**Step 1:** Divide the total length by the length of one strip:\n"
        f"\\[ {m} \\div \\frac{{3}}{{4}} \\]\n\n"
        f"**Step 2:** Invert the divisor and multiply:\n"
        f"\\[ {m} \\times \\frac{{4}}{{3}} = \\frac{{{m} \\times 4}}{{3}} = \\frac{{{m * 4}}}{{3}} = {num_pieces} \\text{{ strips}} \\]"
    )
    ans = f"{num_pieces} strips"
    return {
        "id": f"g8_frac_ribbon_{rng.randint(100000, 999999)}",
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
        "subskill": "43_word_problem_cutting_ribbon_division",
        "learning_objective_id": "math_g8_frac_cutting_ribbon",
        "hints": {
            "tier_1": f"Divide total length {m} by piece size 3/4.",
            "tier_2": f"{m} × 4/3.",
            "tier_3": f"{num_pieces} strips.",
        },
        "misconception_tags": ["multiplying_length_by_fraction_instead_of_dividing"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 44. Converting Fraction To Percentage
# ----------------------------------------------------------------------
def arch_44_converting_fraction_to_percentage(rng: random.Random) -> Dict[str, Any]:
    b = rng.choice([4, 5, 10, 20, 25, 50])
    a = rng.choice([3, 7, 9, 11, 13, 17])
    while a >= b or math.gcd(a, b) != 1:
        a = rng.choice(range(1, b))
    pct = (a * 100) // b

    prompt = (
        f"Convert the common fraction into a percentage:\n"
        f"\\[ \\frac{{{a}}}{{{b}}} \\]"
    )
    sol = (
        f"**Step 1:** Multiply the common fraction by **100%**:\n"
        f"\\[ \\frac{{{a}}}{{{b}}} \\times 100\\% \\]\n\n"
        f"**Step 2:** Simplify by dividing 100 by {b}:\n"
        f"\\[ {a} \\times \\left(\\frac{{100}}{{{b}}}\\right)\\% = {a} \\times {100 // b}\\% = {pct}\\% \\]"
    )
    ans = f"{pct}%"
    return {
        "id": f"g8_frac_to_pct_{rng.randint(100000, 999999)}",
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
        "subskill": "44_converting_fraction_to_percentage",
        "learning_objective_id": "math_g8_frac_to_percentage",
        "hints": {
            "tier_1": f"Multiply by 100% to convert any fraction to a percentage.",
            "tier_2": f"({a} × 100) ÷ {b}.",
            "tier_3": f"{pct}%.",
        },
        "misconception_tags": ["forgetting_to_multiply_by_100"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 45. Converting Percentage To Simplest Fraction
# ----------------------------------------------------------------------
def arch_45_converting_percentage_to_simplest_fraction(rng: random.Random) -> Dict[str, Any]:
    pct = rng.choice([15, 35, 45, 65, 75, 85])
    g = math.gcd(pct, 100)
    num = pct // g
    den = 100 // g

    prompt = (
        f"Convert the percentage into a common fraction in simplest form:\n"
        f"\\[ {pct}\\% \\]"
    )
    sol = (
        f"**Step 1:** Write the percentage as a fraction with denominator 100:\n"
        f"\\[ {pct}\\% = \\frac{{{pct}}}{{100}} \\]\n\n"
        f"**Step 2:** Simplify by dividing both terms by \\(\\text{{HCF}} = {g}\\):\n"
        f"\\[ \\frac{{{pct} \\div {g}}}{{100 \\div {g}}} = \\frac{{{num}}}{{{den}}} \\]"
    )
    ans = f"{num}/{den}"
    return {
        "id": f"g8_pct_to_frac_{rng.randint(100000, 999999)}",
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
        "subskill": "45_converting_percentage_to_simplest_fraction",
        "learning_objective_id": "math_g8_pct_to_fraction",
        "hints": {
            "tier_1": f"Write over 100: {pct}/100.",
            "tier_2": f"Divide top and bottom by {g}.",
            "tier_3": f"{num}/{den}.",
        },
        "misconception_tags": ["forgetting_to_simplify_after_placing_over_100"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 46. Diagnosing Fraction Addition Denominator Error
# ----------------------------------------------------------------------
def arch_46_diagnosing_fraction_addition_denominator_error(rng: random.Random) -> Dict[str, Any]:
    a, b = 1, 2
    c, d = 1, 3
    false_num = a + c
    false_den = b + d
    correct_lcm = 6
    correct_num = a * 3 + c * 2

    prompt = (
        f"A learner solved \\(\\frac{{{a}}}{{{b}}} + \\frac{{{c}}}{{{d}}}\\) by writing:\n"
        f"\\[ \\frac{{{a}}}{{{b}}} + \\frac{{{c}}}{{{d}}} = \\frac{{{a} + {c}}}{{{b} + {d}}} = \\frac{{{false_num}}}{{{false_den}}} \\]\n\n"
        f"1. Explain what fundamental mistake the learner made.\n"
        f"2. Provide the correct calculation and simplified answer."
    )
    sol = (
        f"**Step 1: Diagnostic Explanation**\n"
        f"The learner added the numerators together and the denominators together (\\(\\frac{{1+1}}{{2+3}} = \\frac{{2}}{{5}}\\)).\n"
        f"Fractions can only be added when they share a **common denominator**.\n\n"
        f"**Step 2: Correct Calculation**\n"
        f"The LCD of 2 and 3 is 6:\n"
        f"\\[ \\frac{{1}}{{2}} + \\frac{{1}}{{3}} = \\frac{{3}}{{6}} + \\frac{{2}}{{6}} = \\frac{{5}}{{6}} \\]"
    )
    ans = "1. Added denominators instead of finding LCD; 2. 5/6"
    return {
        "id": f"g8_frac_diag_add_{rng.randint(100000, 999999)}",
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
        "subskill": "46_diagnosing_fraction_addition_denominator_error",
        "learning_objective_id": "math_g8_frac_diag_addition",
        "hints": {
            "tier_1": f"Never add denominators together.",
            "tier_2": f"Find LCD of {b} and {d} = {correct_lcm}.",
            "tier_3": f"Correct answer is {correct_num}/{correct_lcm}.",
        },
        "misconception_tags": ["adding_denominators_together"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 47. Diagnosing Fraction Division Inversion Error
# ----------------------------------------------------------------------
def arch_47_diagnosing_fraction_division_inversion_error(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A learner evaluated \\(\\frac{{2}}{{5}} \\div \\frac{{3}}{{4}}\\) as follows:\n"
        f"\\[ \\frac{{5}}{{2}} \\times \\frac{{3}}{{4}} = \\frac{{15}}{{8}} \\]\n\n"
        f"1. Identify the rule violation in the learner's method.\n"
        f"2. Calculate the correct answer."
    )
    sol = (
        f"**Step 1: Rule Violation**\n"
        f"The learner inverted the **first** fraction (dividend \\(\\frac{{2}}{{5}} \\to \\frac{{5}}{{2}}\\)) instead of the **second** fraction (the divisor \\(\\frac{{3}}{{4}}\\)).\n"
        f"The division rule states: multiply the dividend by the reciprocal of the **divisor**.\n\n"
        f"**Step 2: Correct Calculation**\n"
        f"\\[ \\frac{{2}}{{5}} \\div \\frac{{3}}{{4}} = \\frac{{2}}{{5}} \\times \\frac{{4}}{{3}} = \\frac{{8}}{{15}} \\]"
    )
    ans = "1. Inverted the dividend instead of the divisor; 2. 8/15"
    return {
        "id": f"g8_frac_diag_div_{rng.randint(100000, 999999)}",
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
        "subskill": "47_diagnosing_fraction_division_inversion_error",
        "learning_objective_id": "math_g8_frac_diag_division",
        "hints": {
            "tier_1": f"The divisor (second fraction) must be inverted, not the first.",
            "tier_2": f"2/5 × 4/3.",
            "tier_3": f"8/15.",
        },
        "misconception_tags": ["inverting_dividend_instead_of_divisor"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 48. Diagnosing Mixed Number Squaring Error
# ----------------------------------------------------------------------
def arch_48_diagnosing_mixed_number_squaring_error(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A learner squared the mixed number \\(2 \\frac{{1}}{{2}}\\) and wrote:\n"
        f"\\[ \\left(2 \\frac{{1}}{{2}}\\right)^2 = 2^2 + \\left(\\frac{{1}}{{2}}\\right)^2 = 4 \\frac{{1}}{{4}} \\]\n\n"
        f"1. Explain why squaring the whole number and fractional part separately is algebraically incorrect.\n"
        f"2. Show the correct method and evaluate the exact answer."
    )
    sol = (
        f"**Step 1: Algebraic Explanation**\n"
        f"\\(2 \\frac{{1}}{{2}}\\) means \\((2 + \\frac{{1}}{{2}})\\).\n"
        f"Squaring a binomial requires expanding \\((a + b)^2 = a^2 + 2ab + b^2\\).\n"
        f"The learner completely omitted the middle term \\(2 \\times 2 \\times \\frac{{1}}{{2}} = 2\\).\n\n"
        f"**Step 2: Correct Method**\n"
        f"Convert to an improper fraction first:\n"
        f"\\[ 2 \\frac{{1}}{{2}} = \\frac{{5}}{{2}} \\]\n"
        f"\\[ \\left(\\frac{{5}}{{2}}\\right)^2 = \\frac{{25}}{{4}} = 6 \\frac{{1}}{{4}} \\]"
    )
    ans = "1. Omitted middle term 2ab (must convert to improper first); 2. 6 1/4"
    return {
        "id": f"g8_frac_diag_sq_{rng.randint(100000, 999999)}",
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
        "subskill": "48_diagnosing_mixed_number_squaring_error",
        "learning_objective_id": "math_g8_frac_diag_squaring_mixed",
        "hints": {
            "tier_1": f"Mixed numbers must always be converted to improper fractions before squaring.",
            "tier_2": f"(5/2)^2 = 25/4.",
            "tier_3": f"6 1/4.",
        },
        "misconception_tags": ["squaring_whole_and_fraction_separately"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 49. Complex Fraction Stacked Division
# ----------------------------------------------------------------------
def arch_49_complex_fraction_stacked_division(rng: random.Random) -> Dict[str, Any]:
    # (a/b) / (c/d)
    a, b = 2, 3
    c, d = 4, 9
    # (2/3) / (4/9) = (2/3) * (9/4) = 18/12 = 3/2 = 1 1/2
    prompt = (
        f"Simplify the complex stacked fraction into a simplified mixed number:\n"
        f"\\[ \\frac{{\\frac{{{a}}}{{{b}}}}}{{\\frac{{{c}}}{{{d}}}}} \\]"
    )
    sol = (
        f"**Step 1:** Rewrite the complex fraction as a horizontal division statement:\n"
        f"\\[ \\frac{{{a}}}{{{b}}} \\div \\frac{{{c}}}{{{d}}} \\]\n\n"
        f"**Step 2:** Multiply by the reciprocal of the denominator fraction:\n"
        f"\\[ \\frac{{{a}}}{{{b}}} \\times \\frac{{{d}}}{{{c}}} = \\frac{{{a} \\times {d}}}{{{b} \\times {c}}} = \\frac{{18}}{{12}} \\]\n\n"
        f"**Step 3:** Simplify to lowest terms:\n"
        f"\\[ \\frac{{18 \\div 6}}{{12 \\div 6}} = \\frac{{3}}{{2}} = 1 \\frac{{1}}{{2}} \\]"
    )
    ans = "1 1/2"
    return {
        "id": f"g8_frac_stacked_{rng.randint(100000, 999999)}",
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
        "subskill": "49_complex_fraction_stacked_division",
        "learning_objective_id": "math_g8_frac_complex_stacked",
        "hints": {
            "tier_1": f"The main fraction bar represents division.",
            "tier_2": f"({a}/{b}) × ({d}/{c}).",
            "tier_3": f"1 1/2.",
        },
        "misconception_tags": ["inverting_numerator_fraction"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 50. Common Fractions Capstone Synthesis
# ----------------------------------------------------------------------
def arch_50_common_fractions_capstone_synthesis(rng: random.Random) -> Dict[str, Any]:
    salary = rng.choice([12000, 18000, 24000])
    # 1/3 rent, 1/4 food, 1/6 savings
    # 1/3 + 1/4 + 1/6 = 4/12 + 3/12 + 2/12 = 9/12 = 3/4
    # remaining = 1/4
    rem_amount = salary // 4

    prompt = (
        f"**Comprehensive Real-World Synthesis: Household Budgeting**\n\n"
        f"A family earns a combined monthly net income of **R{salary:,}**.\n".replace(",", " ") +
        f"Their budget allocates:\n"
        f"- \\(\\frac{{1}}{{3}}\\) for rent and housing\n"
        f"- \\(\\frac{{1}}{{4}}\\) for groceries and food\n"
        f"- \\(\\frac{{1}}{{6}}\\) for medical and emergency savings\n\n"
        f"1. What total fraction of their income is committed to these three categories?\n"
        f"2. What fraction remains for discretionary spending?\n"
        f"3. Calculate the discretionary spending amount in Rands."
    )
    sol = (
        f"**Step 1: Total committed fraction**\n"
        f"The LCD of 3, 4, and 6 is **12**:\n"
        f"\\[ \\frac{{1}}{{3}} + \\frac{{1}}{{4}} + \\frac{{1}}{{6}} = \\frac{{4}}{{12}} + \\frac{{3}}{{12}} + \\frac{{2}}{{12}} = \\frac{{9}}{{12}} = \\frac{{3}}{{4}} \\]\n\n"
        f"**Step 2: Discretionary fraction**\n"
        f"\\[ 1 - \\frac{{3}}{{4}} = \\frac{{1}}{{4}} \\]\n\n"
        f"**Step 3: Discretionary amount**\n"
        f"\\[ \\frac{{1}}{{4}} \\times R{salary:,} = R{rem_amount:,} \\]".replace(",", " ")
    )
    ans = f"1. 3/4; 2. 1/4; 3. R{rem_amount:,}".replace(",", " ")
    return {
        "id": f"g8_frac_capstone_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 5,
        "subskill": "50_common_fractions_capstone_synthesis",
        "learning_objective_id": "math_g8_frac_capstone",
        "hints": {
            "tier_1": f"Find LCD of 3, 4, 6 = 12.",
            "tier_2": f"Committed: 4/12 + 3/12 + 2/12 = 9/12 = 3/4.",
            "tier_3": f"Discretionary: 1/4 of R{salary:,} = R{rem_amount:,}.".replace(",", " "),
        },
        "misconception_tags": ["adding_denominators_together"],
        "diagram_spec": None,
    }


BUILDERS_26_50: List[Callable[[random.Random], Dict[str, Any]]] = [
    arch_26_division_two_proper_fractions,
    arch_27_division_mixed_numbers,
    arch_28_squaring_proper_fraction,
    arch_29_squaring_mixed_number,
    arch_30_cubing_proper_fraction,
    arch_31_square_root_of_proper_fraction,
    arch_32_square_root_of_mixed_number,
    arch_33_cube_root_of_proper_fraction,
    arch_34_cube_root_of_mixed_number,
    arch_35_bodmas_brackets_and_addition,
    arch_36_bodmas_multiplication_before_addition,
    arch_37_bodmas_division_before_subtraction,
    arch_38_bodmas_powers_and_operations,
    arch_39_bodmas_roots_and_operations,
    arch_40_word_problem_fraction_of_pocket_money_spent,
    arch_41_word_problem_fractional_sharing_recipe,
    arch_42_word_problem_journey_fraction_remaining,
    arch_43_word_problem_cutting_ribbon_division,
    arch_44_converting_fraction_to_percentage,
    arch_45_converting_percentage_to_simplest_fraction,
    arch_46_diagnosing_fraction_addition_denominator_error,
    arch_47_diagnosing_fraction_division_inversion_error,
    arch_48_diagnosing_mixed_number_squaring_error,
    arch_49_complex_fraction_stacked_division,
    arch_50_common_fractions_capstone_synthesis,
]
