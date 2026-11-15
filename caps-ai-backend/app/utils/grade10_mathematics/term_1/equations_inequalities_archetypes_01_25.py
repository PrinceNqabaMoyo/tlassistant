"""Grade 10 Mathematics — Term 1 — Equations and Inequalities: Archetypes 01 to 25.
Grounded in CAPS curriculum_docs_auto/Mathematics_Gr10/Term 1/04. Equations and inequalities.md
Focus: Linear equations (one-step, brackets, fractions, restrictions, identities/inconsistent),
and Quadratic equations (standard form, common factor, difference of squares, trinomials, fractions).
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


# 01. Linear one-step addition/subtraction: x + b = c or x - b = c
def arch_01_linear_one_step_addition_subtraction(rng: random.Random) -> Dict[str, Any]:
    var = rng.choice(["x", "y", "m", "p", "t"])
    b = rng.randint(3, 25)
    c = rng.randint(-30, 30)
    op = rng.choice(["+", "-"])
    if op == "+":
        ans = c - b
        eq_str = f"{var} + {b} = {c}"
        sol_step = f"{var} = {c} - {b} = {ans}"
        h1 = f"Subtract {b} from both sides."
    else:
        ans = c + b
        eq_str = f"{var} - {b} = {c}"
        sol_step = f"{var} = {c} + {b} = {ans}"
        h1 = f"Add {b} to both sides."

    prompt = f"Solve for \\({var}\\):\n\\[ {eq_str} \\]"
    sol = (
        f"**Step 1:** Apply the additive inverse to isolate the variable:\n"
        f"\\[ {sol_step} \\]\n\n"
        f"**Conclusion:** \\({var} = {ans}\\)"
    )
    return {
        "id": f"g10_eq_01_{rng.randint(100000, 999999)}",
        "subskill": "01_linear_one_step_addition_subtraction",
        "question_type": "short_answer",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": str(ans),
        "sample_answer": f"{var} = {ans}",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g10_eq_01",
        "misconception_tags": ["sign_error_on_transpose"],
        "marking_schema": [
            {"step": 1, "criterion": "Transpose constant with correct sign change", "marks": 1},
            {"step": 2, "criterion": "Accurate final value", "marks": 1},
        ],
        "hints": {
            "tier_1": h1,
            "tier_2": f"Perform the inverse operation on the right-hand side.",
            "tier_3": f"{var} = {ans}",
        },
        "topic": "Equations and inequalities",
        "grade": "10",
        "subject": "Mathematics",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 2,
        "mode": "elementary_01_linear_one_step_addition_subtraction",
    }


# 02. Linear one-step multiplication/division: ax = b or x/a = b
def arch_02_linear_one_step_multiplication_division(rng: random.Random) -> Dict[str, Any]:
    var = rng.choice(["x", "k", "n", "w"])
    case = rng.choice(["mult", "div"])
    if case == "mult":
        a = rng.choice([-9, -8, -7, -6, -5, -4, -3, -2, 2, 3, 4, 5, 6, 7, 8, 9])
        ans = rng.randint(-12, 12)
        b = a * ans
        eq_str = f"{a}{var} = {b}"
        sol_step = f"{var} = \\frac{{{b}}}{{{a}}} = {ans}"
        h1 = f"Divide both sides by {a}."
    else:
        a = rng.choice([-8, -6, -5, -4, -3, -2, 2, 3, 4, 5, 6, 8])
        ans = rng.randint(-15, 15)
        # x / a = b -> b = ans / a (choose integer b)
        b = rng.randint(-10, 10)
        ans = a * b
        eq_str = f"\\frac{{{var}}}{{{a}}} = {b}"
        sol_step = f"{var} = {b} \\times ({a}) = {ans}"
        h1 = f"Multiply both sides by {a}."

    prompt = f"Solve for \\({var}\\):\n\\[ {eq_str} \\]"
    sol = (
        f"**Step 1:** Apply the multiplicative inverse to isolate \\({var}\\):\n"
        f"\\[ {sol_step} \\]\n\n"
        f"**Conclusion:** \\({var} = {ans}\\)"
    )
    return {
        "id": f"g10_eq_02_{rng.randint(100000, 999999)}",
        "subskill": "02_linear_one_step_multiplication_division",
        "question_type": "short_answer",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": str(ans),
        "sample_answer": f"{var} = {ans}",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g10_eq_02",
        "misconception_tags": ["multiplicative_inverse_error", "sign_error_division"],
        "marking_schema": [
            {"step": 1, "criterion": "Apply correct inverse operation", "marks": 1},
            {"step": 2, "criterion": "Correct calculation of answer", "marks": 1},
        ],
        "hints": {
            "tier_1": h1,
            "tier_2": f"Keep careful track of negative signs.",
            "tier_3": f"{var} = {ans}",
        },
        "topic": "Equations and inequalities",
        "grade": "10",
        "subject": "Mathematics",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 2,
        "mode": "elementary_02_linear_one_step_multiplication_division",
    }


# 03. Linear two-step ax + b = c
def arch_03_linear_two_step_ax_plus_b_equals_c(rng: random.Random) -> Dict[str, Any]:
    var = rng.choice(["x", "y", "a", "q"])
    a = rng.choice([-7, -6, -5, -4, -3, -2, 2, 3, 4, 5, 6, 7])
    ans = rng.randint(-10, 10)
    b = rng.choice([-15, -12, -9, -7, -5, -3, 3, 5, 7, 9, 12, 15])
    c = a * ans + b
    sign_b = f"+ {b}" if b > 0 else f"- {abs(b)}"

    prompt = f"Solve for \\({var}\\):\n\\[ {a}{var} {sign_b} = {c} \\]"
    step1_rhs = c - b
    sol = (
        f"**Step 1:** Subtract {b} from both sides:\n"
        f"\\[ {a}{var} = {c} - ({b}) = {step1_rhs} \\]\n\n"
        f"**Step 2:** Divide both sides by {a}:\n"
        f"\\[ {var} = \\frac{{{step1_rhs}}}{{{a}}} = {ans} \\]"
    )
    return {
        "id": f"g10_eq_03_{rng.randint(100000, 999999)}",
        "subskill": "03_linear_two_step_ax_plus_b_equals_c",
        "question_type": "short_answer",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": str(ans),
        "sample_answer": f"{var} = {ans}",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g10_eq_03",
        "misconception_tags": ["order_of_operations_reversal", "sign_error_on_transpose"],
        "marking_schema": [
            {"step": 1, "criterion": "Transpose constant term", "marks": 1},
            {"step": 2, "criterion": "Divide by coefficient to find root", "marks": 1},
        ],
        "hints": {
            "tier_1": f"First isolate the term {a}{var} by moving {b} across the equals sign.",
            "tier_2": f"{a}{var} = {step1_rhs}.",
            "tier_3": f"{var} = {ans}",
        },
        "topic": "Equations and inequalities",
        "grade": "10",
        "subject": "Mathematics",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 2,
        "mode": "elementary_03_linear_two_step_ax_plus_b_equals_c",
    }


# 04. Linear brackets distributive single: a(x + b) = c
def arch_04_linear_brackets_distributive_single(rng: random.Random) -> Dict[str, Any]:
    var = rng.choice(["x", "p", "t", "u"])
    a = rng.choice([-5, -4, -3, -2, 2, 3, 4, 5])
    ans = rng.randint(-8, 8)
    b = rng.choice([-9, -7, -5, -3, 3, 5, 7, 9])
    c = a * (ans + b)
    sign_b = f"+ {b}" if b > 0 else f"- {abs(b)}"

    prompt = f"Solve for \\({var}\\):\n\\[ {a}({var} {sign_b}) = {c} \\]"
    expanded_const = a * b
    sign_exp = f"+ {expanded_const}" if expanded_const > 0 else f"- {abs(expanded_const)}"
    rhs_transposed = c - expanded_const

    sol = (
        f"**Step 1:** Expand the brackets using the distributive property:\n"
        f"\\[ {a}{var} {sign_exp} = {c} \\]\n\n"
        f"**Step 2:** Transpose the constant term:\n"
        f"\\[ {a}{var} = {c} - ({expanded_const}) = {rhs_transposed} \\]\n\n"
        f"**Step 3:** Divide by {a}:\n"
        f"\\[ {var} = \\frac{{{rhs_transposed}}}{{{a}}} = {ans} \\]"
    )
    return {
        "id": f"g10_eq_04_{rng.randint(100000, 999999)}",
        "subskill": "04_linear_brackets_distributive_single",
        "question_type": "short_answer",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": str(ans),
        "sample_answer": f"{var} = {ans}",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g10_eq_04",
        "misconception_tags": ["distributive_bracket_omission", "sign_error_expansion"],
        "marking_schema": [
            {"step": 1, "criterion": "Correct expansion of brackets", "marks": 1},
            {"step": 2, "criterion": "Isolate variable term", "marks": 1},
            {"step": 3, "criterion": "Correct answer", "marks": 1},
        ],
        "hints": {
            "tier_1": f"Distribute {a} across both terms inside the bracket.",
            "tier_2": f"Alternatively, divide both sides by {a} first: {var} {sign_b} = {c // a}.",
            "tier_3": f"{var} = {ans}",
        },
        "topic": "Equations and inequalities",
        "grade": "10",
        "subject": "Mathematics",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 3,
        "mode": "elementary_04_linear_brackets_distributive_single",
    }


# 05. Linear brackets both sides: a(x + b) = c(x + d)
def arch_05_linear_brackets_both_sides(rng: random.Random) -> Dict[str, Any]:
    var = rng.choice(["x", "y", "m"])
    # a*(x+b) = c*(x+d) -> (a-c)*x = c*d - a*b
    a = rng.choice([3, 4, 5, 6])
    c = rng.choice([2, 7])
    while a == c:
        c = rng.choice([2, 7, 8])
    ans = rng.randint(-6, 6)
    b = rng.randint(-5, 5)
    # c*d = a*ans + a*b - c*ans = a*(ans+b) - c*ans
    # let d be chosen so equation holds
    lhs_val = a * (ans + b)
    # c*(ans + d) = lhs_val => ans + d = lhs_val / c -> need lhs_val divisible by c
    # simpler: pick d, compute ans
    d = rng.randint(-5, 5)
    while a - c == 0:
        c = rng.randint(2, 6)
    # (a - c)*ans = c*d - a*b
    # Let's construct: choose ans, a, c, b, then d = (a*(ans+b) - c*ans) / c
    # To ensure d is integer, choose a=3, c=2, etc. where denominator is 1 or divides.
    # Alternatively: a*(x + b) + k = c*(x + d)
    a = 3
    c = 2
    ans = rng.randint(-8, 8)
    b = rng.randint(-6, 6)
    # 3*(ans + b) = 2*(ans + d) => 3*ans + 3*b - 2*ans = 2*d => ans + 3*b = 2*d
    # make ans + 3*b even by adjusting b
    if (ans + 3 * b) % 2 != 0:
        b += 1
    d = (ans + 3 * b) // 2

    sign_b = f"+ {b}" if b >= 0 else f"- {abs(b)}"
    sign_d = f"+ {d}" if d >= 0 else f"- {abs(d)}"

    prompt = f"Solve for \\({var}\\):\n\\[ {a}({var} {sign_b}) = {c}({var} {sign_d}) \\]"
    lhs_exp = f"{a}{var} {'+' if a*b>=0 else '-'} {abs(a*b)}"
    rhs_exp = f"{c}{var} {'+' if c*d>=0 else '-'} {abs(c*d)}"

    sol = (
        f"**Step 1:** Expand both sides:\n"
        f"\\[ {lhs_exp} = {rhs_exp} \\]\n\n"
        f"**Step 2:** Collect like terms on either side:\n"
        f"\\[ {a}{var} - {c}{var} = {c*d} - ({a*b}) \\]\n"
        f"\\[ {a - c}{var} = {c*d - a*b} \\]\n\n"
        f"**Step 3:** Solve for \\({var}\\):\n"
        f"\\[ {var} = {ans} \\]"
    )
    return {
        "id": f"g10_eq_05_{rng.randint(100000, 999999)}",
        "subskill": "05_linear_brackets_both_sides",
        "question_type": "short_answer",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": str(ans),
        "sample_answer": f"{var} = {ans}",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g10_eq_05",
        "misconception_tags": ["sign_error_both_sides", "bracket_expansion_omission"],
        "marking_schema": [
            {"step": 1, "criterion": "Distribute brackets accurately on both sides", "marks": 1},
            {"step": 2, "criterion": "Group variables on one side, constants on other", "marks": 1},
            {"step": 3, "criterion": "Correct final solution", "marks": 1},
        ],
        "hints": {
            "tier_1": "Multiply out both brackets first before grouping terms.",
            "tier_2": f"Move the {c}{var} to the left and constant {a*b} to the right.",
            "tier_3": f"{var} = {ans}",
        },
        "topic": "Equations and inequalities",
        "grade": "10",
        "subject": "Mathematics",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 3,
        "mode": "elementary_05_linear_brackets_both_sides",
    }


# 06. Linear variables both sides collect: ax + b = cx + d
def arch_06_linear_variables_both_sides_collect(rng: random.Random) -> Dict[str, Any]:
    var = rng.choice(["x", "k", "p"])
    a = rng.choice([4, 5, 6, 7, 8])
    c = rng.choice([2, 3])
    ans = rng.randint(-9, 9)
    b = rng.randint(-15, 15)
    # (a - c)*ans + b = d => d = (a-c)*ans + b
    d = (a - c) * ans + b
    sign_b = f"+ {b}" if b >= 0 else f"- {abs(b)}"
    sign_d = f"+ {d}" if d >= 0 else f"- {abs(d)}"

    prompt = f"Solve for \\({var}\\):\n\\[ {a}{var} {sign_b} = {c}{var} {sign_d} \\]"
    sol = (
        f"**Step 1:** Subtract {c}{var} from both sides and subtract {b} from both sides:\n"
        f"\\[ {a}{var} - {c}{var} = {d} - ({b}) \\]\n"
        f"\\[ {a - c}{var} = {d - b} \\]\n\n"
        f"**Step 2:** Divide by {a - c}:\n"
        f"\\[ {var} = \\frac{{{d - b}}}{{{a - c}}} = {ans} \\]"
    )
    return {
        "id": f"g10_eq_06_{rng.randint(100000, 999999)}",
        "subskill": "06_linear_variables_both_sides_collect",
        "question_type": "short_answer",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": str(ans),
        "sample_answer": f"{var} = {ans}",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g10_eq_06",
        "misconception_tags": ["sign_error_on_transpose", "combining_unlike_terms"],
        "marking_schema": [
            {"step": 1, "criterion": "Transpose variable terms to LHS and constants to RHS", "marks": 1},
            {"step": 2, "criterion": "Simplify both sides", "marks": 1},
            {"step": 3, "criterion": "Divide by coefficient to isolate variable", "marks": 1},
        ],
        "hints": {
            "tier_1": f"Move {c}{var} to the left side and {b} to the right side.",
            "tier_2": f"{a - c}{var} = {d - b}.",
            "tier_3": f"{var} = {ans}",
        },
        "topic": "Equations and inequalities",
        "grade": "10",
        "subject": "Mathematics",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 3,
        "mode": "elementary_06_linear_variables_both_sides_collect",
    }


# 07. Linear fractions numerical denominator monomial: x/a + x/b = c
def arch_07_linear_fractions_numerical_denominator_monomial(rng: random.Random) -> Dict[str, Any]:
    var = rng.choice(["x", "y", "t"])
    a = rng.choice([2, 3, 4])
    b = rng.choice([3, 5, 6])
    while a == b:
        b = rng.choice([3, 5, 6])
    # LCM of a, b
    import math
    lcm = (a * b) // math.gcd(a, b)
    mult_a = lcm // a
    mult_b = lcm // b
    sum_coeffs = mult_a + mult_b
    # choose ans so c is integer: sum_coeffs * ans = c * lcm
    # let ans be multiple of lcm // gcd(sum_coeffs, lcm) or pick ans and define c
    ans_int = rng.choice([-12, -6, 6, 12, 18, 24])
    # x/a + x/b = (mult_a + mult_b)*ans / lcm = c
    val = (ans_int * sum_coeffs)
    if val % lcm != 0:
        ans_int = lcm * rng.choice([-3, -2, -1, 1, 2, 3])
    c = (ans_int * sum_coeffs) // lcm

    prompt = f"Solve for \\({var}\\):\n\\[ \\frac{{{var}}}{{{a}}} + \\frac{{{var}}}{{{b}}} = {c} \\]"
    sol = (
        f"**Step 1:** Find the Lowest Common Denominator (LCD) of {a} and {b}, which is **{lcm}**.\n\n"
        f"**Step 2:** Multiply every term on both sides by {lcm}:\n"
        f"\\[ {lcm} \\left( \\frac{{{var}}}{{{a}}} \\right) + {lcm} \\left( \\frac{{{var}}}{{{b}}} \\right) = {lcm} \\times {c} \\]\n"
        f"\\[ {mult_a}{var} + {mult_b}{var} = {lcm * c} \\]\n\n"
        f"**Step 3:** Combine like terms and divide:\n"
        f"\\[ {sum_coeffs}{var} = {lcm * c} \\]\n"
        f"\\[ {var} = \\frac{{{lcm * c}}}{{{sum_coeffs}}} = {ans_int} \\]"
    )
    return {
        "id": f"g10_eq_07_{rng.randint(100000, 999999)}",
        "subskill": "07_linear_fractions_numerical_denominator_monomial",
        "question_type": "short_answer",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": str(ans_int),
        "sample_answer": f"{var} = {ans_int}",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g10_eq_07",
        "misconception_tags": ["failure_to_multiply_rhs_by_lcd", "incorrect_lcd"],
        "marking_schema": [
            {"step": 1, "criterion": "Identify correct LCD and multiply all terms", "marks": 1},
            {"step": 2, "criterion": "Simplify to linear equation without fractions", "marks": 1},
            {"step": 3, "criterion": "Accurate solution for variable", "marks": 1},
        ],
        "hints": {
            "tier_1": f"The LCD of {a} and {b} is {lcm}. Multiply every term by {lcm}.",
            "tier_2": f"Remember to multiply the right-hand side ({c}) by {lcm} as well!",
            "tier_3": f"{var} = {ans_int}",
        },
        "topic": "Equations and inequalities",
        "grade": "10",
        "subject": "Mathematics",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 3,
        "mode": "elementary_07_linear_fractions_numerical_denominator_monomial",
    }


# 08. Linear fractions numerical denominators binomial numerators: (x + a)/b - (x - c)/d = e
def arch_08_linear_fractions_numerical_denominators_binomial_numerators(rng: random.Random) -> Dict[str, Any]:
    var = rng.choice(["x", "y", "m"])
    b = 2
    d = 3
    lcm = 6
    ans = rng.randint(-8, 8)
    a = rng.choice([-5, -3, -1, 1, 3, 5])
    c = rng.choice([-4, -2, 2, 4])
    # 3*(ans + a) - 2*(ans + c) = 3*ans + 3*a - 2*ans - 2*c = ans + 3*a - 2*c
    # In the equation: ((var + a)/2) - ((var + c)/3) = e => 6*LHS = ans + 3*a - 2*c => e = (ans + 3*a - 2*c)/6
    # To make e integer:
    target_num = ans + 3 * a - 2 * c
    if target_num % 6 != 0:
        ans += (6 - (target_num % 6))
    e = (ans + 3 * a - 2 * c) // 6

    sign_a = f"+ {a}" if a >= 0 else f"- {abs(a)}"
    sign_c = f"+ {c}" if c >= 0 else f"- {abs(c)}"

    prompt = f"Solve for \\({var}\\):\n\\[ \\frac{{{var} {sign_a}}}{{2}} - \\frac{{{var} {sign_c}}}{{3}} = {e} \\]"
    sol = (
        f"**Step 1:** Multiply the entire equation by the LCD of 2 and 3, which is 6:\n"
        f"\\[ 6 \\left( \\frac{{{var} {sign_a}}}{{2}} \\right) - 6 \\left( \\frac{{{var} {sign_c}}}{{3}} \\right) = 6 \\times {e} \\]\n"
        f"\\[ 3({var} {sign_a}) - 2({var} {sign_c}) = {6 * e} \\]\n\n"
        f"**Step 2:** Expand brackets (watch the negative sign on the second term!):\n"
        f"\\[ 3{var} {'+' if 3*a>=0 else '-'} {abs(3*a)} - 2{var} {'-' if 2*c>=0 else '+'} {abs(2*c)} = {6 * e} \\]\n"
        f"\\[ {var} {'+' if 3*a-2*c>=0 else '-'} {abs(3*a-2*c)} = {6 * e} \\]\n\n"
        f"**Step 3:** Solve for \\({var}\\):\n"
        f"\\[ {var} = {6 * e} - ({3*a - 2*c}) = {ans} \\]"
    )
    return {
        "id": f"g10_eq_08_{rng.randint(100000, 999999)}",
        "subskill": "08_linear_fractions_numerical_denominators_binomial_numerators",
        "question_type": "short_answer",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": str(ans),
        "sample_answer": f"{var} = {ans}",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 4,
        "learning_objective_id": "math_g10_eq_08",
        "misconception_tags": ["sign_error_distributing_negative_into_numerator", "lcd_omission"],
        "marking_schema": [
            {"step": 1, "criterion": "Multiply through by LCD = 6", "marks": 1},
            {"step": 2, "criterion": "Correct distribution of -2 across numerator terms", "marks": 1},
            {"step": 3, "criterion": "Combine terms and solve", "marks": 2},
        ],
        "hints": {
            "tier_1": "Multiply all terms by the LCD 6 to clear fractions.",
            "tier_2": f"Be extremely careful with the minus sign: -2({var} {sign_c}) = -2{var} {'-' if c>=0 else '+'} {abs(2*c)}.",
            "tier_3": f"{var} = {ans}",
        },
        "topic": "Equations and inequalities",
        "grade": "10",
        "subject": "Mathematics",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 3,
        "mode": "elementary_08_linear_fractions_numerical_denominators_binomial_numerators",
    }


# 09. Linear fractions LCD clearing three terms
def arch_09_linear_fractions_lcd_clearing_three_terms(rng: random.Random) -> Dict[str, Any]:
    var = rng.choice(["x", "n", "p"])
    # (x/2) + (x/3) - (x/4) = k
    # LCD = 12: 6x + 4x - 3x = 7x = 12k
    k = rng.choice([7, 14, 21, 28, 35])
    ans = (12 * k) // 7

    prompt = f"Solve for \\({var}\\):\n\\[ \\frac{{{var}}}{{2}} + \\frac{{{var}}}{{3}} - \\frac{{{var}}}{{4}} = {k} \\]"
    sol = (
        f"**Step 1:** Find the LCD of 2, 3, and 4, which is **12**.\n\n"
        f"**Step 2:** Multiply every term by 12:\n"
        f"\\[ 12\\left(\\frac{{{var}}}{{2}}\\right) + 12\\left(\\frac{{{var}}}{{3}}\\right) - 12\\left(\\frac{{{var}}}{{4}}\\right) = 12 \\times {k} \\]\n"
        f"\\[ 6{var} + 4{var} - 3{var} = {12 * k} \\]\n\n"
        f"**Step 3:** Simplify the LHS:\n"
        f"\\[ 7{var} = {12 * k} \\]\n"
        f"\\[ {var} = \\frac{{{12 * k}}}{{7}} = {ans} \\]"
    )
    return {
        "id": f"g10_eq_09_{rng.randint(100000, 999999)}",
        "subskill": "09_linear_fractions_lcd_clearing_three_terms",
        "question_type": "short_answer",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": str(ans),
        "sample_answer": f"{var} = {ans}",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g10_eq_09",
        "misconception_tags": ["lcd_identification_error", "combining_fraction_coefficients"],
        "marking_schema": [
            {"step": 1, "criterion": "Multiply all terms by LCD 12", "marks": 1},
            {"step": 2, "criterion": "Simplify variable coefficients", "marks": 1},
            {"step": 3, "criterion": "Final root calculation", "marks": 1},
        ],
        "hints": {
            "tier_1": "The LCD of 2, 3, and 4 is 12.",
            "tier_2": "6x + 4x - 3x = 7x.",
            "tier_3": f"{var} = {ans}",
        },
        "topic": "Equations and inequalities",
        "grade": "10",
        "subject": "Mathematics",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 3,
        "mode": "elementary_09_linear_fractions_lcd_clearing_three_terms",
    }


# 10. Linear fraction variable denominator restriction: a / (x + b) = c
def arch_10_linear_fraction_variable_denominator_restriction(rng: random.Random) -> Dict[str, Any]:
    var = "x"
    b = rng.choice([-6, -5, -4, -3, -2, 2, 3, 4, 5, 6])
    ans = rng.choice([-8, -7, -6, -5, -4, -3, -2, 1, 2, 3, 4, 5, 7, 8])
    while ans == -b:
        ans += 2
    denom_val = ans + b
    # c is an integer, a = c * denom_val
    c = rng.choice([-4, -3, -2, 2, 3, 4])
    a = c * denom_val
    sign_b = f"+ {b}" if b >= 0 else f"- {abs(b)}"
    restriction = -b

    prompt = (
        f"Solve for \\({var}\\) and state the restriction on the variable:\n"
        f"\\[ \\frac{{{a}}}{{{var} {sign_b}}} = {c} \\]"
    )
    sol = (
        f"**Step 1:** State the restriction:\n"
        f"The denominator cannot be zero, so:\n"
        f"\\[ {var} {sign_b} \\neq 0 \\implies {var} \\neq {restriction} \\]\n\n"
        f"**Step 2:** Multiply both sides by \\(({var} {sign_b})\\):\n"
        f"\\[ {a} = {c}({var} {sign_b}) \\]\n"
        f"\\[ {a} = {c}{var} {'+' if c*b>=0 else '-'} {abs(c*b)} \\]\n\n"
        f"**Step 3:** Solve for \\({var}\\):\n"
        f"\\[ {c}{var} = {a} - ({c*b}) = {a - c*b} \\]\n"
        f"\\[ {var} = \\frac{{{a - c*b}}}{{{c}}} = {ans} \\]\n\n"
        f"Since \\({ans} \\neq {restriction}\\), the solution is valid: **\\({var} = {ans}\\)**."
    )
    return {
        "id": f"g10_eq_10_{rng.randint(100000, 999999)}",
        "subskill": "10_linear_fraction_variable_denominator_restriction",
        "question_type": "short_answer",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": f"{ans}",
        "sample_answer": f"{var} = {ans}; restriction: {var} != {restriction}",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g10_eq_10",
        "misconception_tags": ["ignoring_domain_restrictions", "division_by_zero_neglect"],
        "marking_schema": [
            {"step": 1, "criterion": "State restriction on denominator", "marks": 1},
            {"step": 2, "criterion": "Multiply by denominator and isolate x", "marks": 1},
            {"step": 3, "criterion": "State valid root", "marks": 1},
        ],
        "hints": {
            "tier_1": f"The denominator cannot be 0, so {var} != {restriction}.",
            "tier_2": f"Cross-multiply: {a} = {c}({var} {sign_b}).",
            "tier_3": f"{var} = {ans}",
        },
        "topic": "Equations and inequalities",
        "grade": "10",
        "subject": "Mathematics",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 3,
        "mode": "elementary_10_linear_fraction_variable_denominator_restriction",
    }


# 11. Linear fraction difference of squares denominator: a / (x^2 - b^2) + c / (x - b) = 0
def arch_11_linear_fraction_difference_of_squares_denominator(rng: random.Random) -> Dict[str, Any]:
    b = rng.choice([2, 3, 4, 5])
    b2 = b * b
    # a / (x^2 - b^2) + c / (x - b) = 0
    # multiply by (x - b)(x + b): a + c(x + b) = 0 => c*x = -a - c*b => x = (-a - c*b)/c
    # Choose c = 1, then x = -a - b. We want x != b and x != -b.
    c = 1
    # Pick ans distinct from b and -b
    ans = rng.choice([n for n in range(-8, 9) if n not in [b, -b, 0]])
    # -a - b = ans => a = -ans - b
    a = -ans - b

    prompt = (
        f"Solve for \\(x\\) (state all restrictions):\n"
        f"\\[ \\frac{{{a}}}{{x^2 - {b2}}} + \\frac{{{c}}}{{x - {b}}} = 0 \\]"
    )
    sol = (
        f"**Step 1:** Factorise the denominator and state restrictions:\n"
        f"\\[ x^2 - {b2} = (x - {b})(x + {b}) \\]\n"
        f"Restrictions: \\(x \\neq {b}\\) and \\(x \\neq -{b}\\).\n\n"
        f"**Step 2:** Multiply through by the LCD \\((x - {b})(x + {b})\\):\n"
        f"\\[ {a} + {c}(x + {b}) = 0 \\]\n"
        f"\\[ {a} + x + {b} = 0 \\]\n"
        f"\\[ x = -({a} + {b}) = {ans} \\]\n\n"
        f"Since \\({ans} \\neq {b}\\) and \\({ans} \\neq -{b}\\), the solution is **\\(x = {ans}\\)**."
    )
    return {
        "id": f"g10_eq_11_{rng.randint(100000, 999999)}",
        "subskill": "11_linear_fraction_difference_of_squares_denominator",
        "question_type": "short_answer",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": str(ans),
        "sample_answer": f"x = {ans}",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 4,
        "learning_objective_id": "math_g10_eq_11",
        "misconception_tags": ["factorisation_error_difference_of_squares", "ignoring_restrictions"],
        "marking_schema": [
            {"step": 1, "criterion": "Factorise denominator and state restrictions x != +/- b", "marks": 1},
            {"step": 2, "criterion": "Multiply through by LCD (x-b)(x+b)", "marks": 1},
            {"step": 3, "criterion": "Solve linear equation", "marks": 1},
            {"step": 4, "criterion": "Verify solution against restrictions", "marks": 1},
        ],
        "hints": {
            "tier_1": f"Notice that x^2 - {b2} = (x - {b})(x + {b}).",
            "tier_2": f"Restrictions: x != {b} and x != -{b}. Multiply all terms by (x - {b})(x + {b}).",
            "tier_3": f"x = {ans}",
        },
        "topic": "Equations and inequalities",
        "grade": "10",
        "subject": "Mathematics",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 4,
        "mode": "elementary_11_linear_fraction_difference_of_squares_denominator",
    }


# 12. Linear equation no solution / inconsistent: 2(x + 3) = 2x + 5 -> 0x = -1
def arch_12_linear_equation_no_solution_inconsistent(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([2, 3, 4, 5])
    b = rng.randint(2, 6)
    diff = rng.choice([-4, -3, -2, 2, 3, 4])
    d = a * b + diff

    prompt = (
        f"Solve for \\(x\\):\n"
        f"\\[ {a}(x + {b}) = {a}x + {d} \\]"
    )
    sol = (
        f"**Step 1:** Expand the left-hand side:\n"
        f"\\[ {a}x + {a * b} = {a}x + {d} \\]\n\n"
        f"**Step 2:** Subtract \\({a}x\\) from both sides:\n"
        f"\\[ {a}x - {a}x = {d} - {a * b} \\]\n"
        f"\\[ 0x = {d - a * b} \\]\n"
        f"\\[ 0 = {d - a * b} \\]\n\n"
        f"**Conclusion:** The statement \\(0 = {d - a * b}\\) is false for all values of \\(x\\).\n"
        f"Therefore, there is **no solution** (the equation is inconsistent)."
    )
    return {
        "id": f"g10_eq_12_{rng.randint(100000, 999999)}",
        "subskill": "12_linear_equation_no_solution_inconsistent",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": ["No solution", "x = 0", "x = 1", "Infinitely many solutions"],
        "correct_answer": "No solution",
        "sample_answer": "No solution",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g10_eq_12",
        "misconception_tags": ["confusing_no_solution_with_zero", "false_equation_interpretation"],
        "marking_schema": [
            {"step": 1, "criterion": "Expand and simplify to 0 = k (where k != 0)", "marks": 1},
            {"step": 2, "criterion": "Conclude no solution", "marks": 1},
        ],
        "hints": {
            "tier_1": "Expand the LHS and see what happens to the x terms.",
            "tier_2": f"Both sides have {a}x, leaving {a*b} = {d}, which is impossible.",
            "tier_3": "No solution",
        },
        "topic": "Equations and inequalities",
        "grade": "10",
        "subject": "Mathematics",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 2,
        "mode": "elementary_12_linear_equation_no_solution_inconsistent",
    }


# 13. Linear equation identity all real numbers: 3(x + 2) - 6 = 3x -> 0x = 0
def arch_13_linear_equation_identity_all_real_numbers(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([2, 3, 4, 5])
    b = rng.randint(2, 6)
    c = a * b

    prompt = (
        f"Solve for \\(x\\):\n"
        f"\\[ {a}(x + {b}) - {c} = {a}x \\]"
    )
    sol = (
        f"**Step 1:** Expand the LHS:\n"
        f"\\[ {a}x + {a * b} - {c} = {a}x \\]\n"
        f"\\[ {a}x + 0 = {a}x \\]\n"
        f"\\[ {a}x = {a}x \\]\n\n"
        f"**Step 2:** Subtract \\({a}x\\) from both sides:\n"
        f"\\[ 0 = 0 \\]\n\n"
        f"**Conclusion:** The statement \\(0 = 0\\) is always true regardless of \\(x\\).\n"
        f"Therefore, the solution is **all real numbers** (\\(x \\in \\mathbb{{R}}\\))."
    )
    return {
        "id": f"g10_eq_13_{rng.randint(100000, 999999)}",
        "subskill": "13_linear_equation_identity_all_real_numbers",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": ["All real numbers (x in R)", "x = 0", "No solution", "x = 1"],
        "correct_answer": "All real numbers (x in R)",
        "sample_answer": "x in R",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g10_eq_13",
        "misconception_tags": ["confusing_identity_with_zero", "misunderstanding_infinte_solutions"],
        "marking_schema": [
            {"step": 1, "criterion": "Simplify equation to identity 0 = 0", "marks": 1},
            {"step": 2, "criterion": "Conclude x in R / infinitely many solutions", "marks": 1},
        ],
        "hints": {
            "tier_1": "Expand the brackets and collect like terms.",
            "tier_2": "You obtain 0 = 0, which is always true.",
            "tier_3": "All real numbers (x in R)",
        },
        "topic": "Equations and inequalities",
        "grade": "10",
        "subject": "Mathematics",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 2,
        "mode": "elementary_13_linear_equation_identity_all_real_numbers",
    }


# 14. Quadratic standard form identification: arrange into ax^2 + bx + c = 0
def arch_14_quadratic_standard_form_identification(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([2, 3, 5])
    b = rng.randint(-7, 7)
    while b == 0:
        b = rng.randint(-7, 7)
    c = rng.randint(-15, 15)
    while c == 0:
        c = rng.randint(-15, 15)
    
    # Given as a*x^2 = -b*x - c
    neg_b = -b
    neg_c = -c
    rhs_str = f"{neg_b}x {'+' if neg_c>=0 else '-'} {abs(neg_c)}"
    
    std_str = f"{a}x^2 {'+' if b>=0 else '-'} {abs(b)}x {'+' if c>=0 else '-'} {abs(c)} = 0"
    prompt = (
        f"Rewrite the quadratic equation in standard form \\(ax^2 + bx + c = 0\\) and identify the values of \\(a\\), \\(b\\), and \\(c\\):\n"
        f"\\[ {a}x^2 = {rhs_str} \\]"
    )
    ans = f"a = {a}, b = {b}, c = {c}"
    sol = (
        f"**Step 1:** Move all terms to the left-hand side so the right-hand side equals 0:\n"
        f"\\[ {std_str} \\]\n\n"
        f"**Step 2:** Read off coefficients:\n"
        f"- \\(a = {a}\\)\n"
        f"- \\(b = {b}\\)\n"
        f"- \\(c = {c}\\)"
    )
    return {
        "id": f"g10_eq_14_{rng.randint(100000, 999999)}",
        "subskill": "14_quadratic_standard_form_identification",
        "question_type": "short_answer",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g10_eq_14",
        "misconception_tags": ["sign_error_standard_form", "misidentifying_coefficients"],
        "marking_schema": [
            {"step": 1, "criterion": "Transpose terms to get RHS = 0", "marks": 1},
            {"step": 2, "criterion": "Correctly identify a, b, and c", "marks": 1},
        ],
        "hints": {
            "tier_1": "Standard form requires all terms on one side equal to zero: ax^2 + bx + c = 0.",
            "tier_2": f"Add {b}x and {c} to both sides.",
            "tier_3": ans,
        },
        "topic": "Equations and inequalities",
        "grade": "10",
        "subject": "Mathematics",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 2,
        "mode": "elementary_14_quadratic_standard_form_identification",
    }


# 15. Quadratic common factor monomial: ax^2 + bx = 0
def arch_15_quadratic_common_factor_monomial(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([2, 3, 4, 5])
    r1 = 0
    r2 = rng.choice([-8, -6, -4, -2, 2, 4, 6, 8])
    # a*x*(x - r2) = a*x^2 - a*r2*x = 0
    b = -a * r2
    sign_b = f"+ {b}" if b >= 0 else f"- {abs(b)}"

    prompt = f"Solve for \\(x\\) by factorisation:\n\\[ {a}x^2 {sign_b}x = 0 \\]"
    # answer format: x = 0 or x = r2
    ans = f"x = 0 or x = {r2}"
    sol = (
        f"**Step 1:** Factor out the common monomial factor \\({a}x\\):\n"
        f"\\[ {a}x(x {'-' if r2>=0 else '+'} {abs(r2)}) = 0 \\]\n\n"
        f"**Step 2:** Apply the zero-product property:\n"
        f"\\[ {a}x = 0 \\quad \\text{{or}} \\quad x {'-' if r2>=0 else '+'} {abs(r2)} = 0 \\]\n"
        f"\\[ x = 0 \\quad \\text{{or}} \\quad x = {r2} \\]"
    )
    return {
        "id": f"g10_eq_15_{rng.randint(100000, 999999)}",
        "subskill": "15_quadratic_common_factor_monomial",
        "question_type": "short_answer",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": f"0 or {r2}",
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g10_eq_15",
        "misconception_tags": ["dividing_by_variable_losing_root_zero", "zero_product_omission"],
        "marking_schema": [
            {"step": 1, "criterion": "Factor out common factor x", "marks": 1},
            {"step": 2, "criterion": "State x = 0 root", "marks": 1},
            {"step": 3, "criterion": f"State x = {r2} root", "marks": 1},
        ],
        "hints": {
            "tier_1": "Never divide both sides by x, or you lose the solution x = 0! Factorise instead.",
            "tier_2": f"Factor out {a}x: {a}x(x - {r2}) = 0.",
            "tier_3": ans,
        },
        "topic": "Equations and inequalities",
        "grade": "10",
        "subject": "Mathematics",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 3,
        "mode": "elementary_15_quadratic_common_factor_monomial",
    }


# 16. Quadratic difference of two squares: x^2 - k^2 = 0 or a^2 x^2 - b^2 = 0
def arch_16_quadratic_difference_of_two_squares(rng: random.Random) -> Dict[str, Any]:
    k = rng.choice([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    k2 = k * k
    prompt = f"Solve for \\(x\\):\n\\[ x^2 - {k2} = 0 \\]"
    ans = f"x = {k} or x = -{k}"
    sol = (
        f"**Step 1:** Factorise as a difference of two squares:\n"
        f"\\[ (x - {k})(x + {k}) = 0 \\]\n\n"
        f"**Step 2:** Set each factor to zero:\n"
        f"\\[ x - {k} = 0 \\quad \\text{{or}} \\quad x + {k} = 0 \\]\n"
        f"\\[ x = {k} \\quad \\text{{or}} \\quad x = -{k} \\]"
    )
    return {
        "id": f"g10_eq_16_{rng.randint(100000, 999999)}",
        "subskill": "16_quadratic_difference_of_two_squares",
        "question_type": "short_answer",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": f"{k} or -{k}",
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g10_eq_16",
        "misconception_tags": ["forgetting_negative_square_root", "difference_of_squares_sign_error"],
        "marking_schema": [
            {"step": 1, "criterion": "Factorise difference of squares (x - k)(x + k)", "marks": 1},
            {"step": 2, "criterion": "State positive root", "marks": 1},
            {"step": 3, "criterion": "State negative root", "marks": 1},
        ],
        "hints": {
            "tier_1": f"Recall a^2 - b^2 = (a - b)(a + b). Here b = {k}.",
            "tier_2": f"Both positive and negative roots must be given: x = +{k} and x = -{k}.",
            "tier_3": ans,
        },
        "topic": "Equations and inequalities",
        "grade": "10",
        "subject": "Mathematics",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 2,
        "mode": "elementary_16_quadratic_difference_of_two_squares",
    }


# 17. Quadratic trinomial monic positive constant: x^2 + bx + c = 0 (c > 0)
def arch_17_quadratic_trinomial_monic_positive_constant(rng: random.Random) -> Dict[str, Any]:
    # (x + p)(x + q) = 0 where p, q have same sign
    sign = rng.choice([1, -1])
    p = sign * rng.randint(1, 6)
    q = sign * rng.randint(2, 7)
    b = p + q
    c = p * q
    r1 = -p
    r2 = -q
    sign_b = f"+ {b}" if b >= 0 else f"- {abs(b)}"

    prompt = f"Solve for \\(x\\) by factorisation:\n\\[ x^2 {sign_b}x + {c} = 0 \\]"
    ans = f"x = {r1} or x = {r2}"
    sol = (
        f"**Step 1:** Find two numbers that multiply to \\({c}\\) and add to \\({b}\\):\n"
        f"The numbers are \\({p}\\) and \\({q}\\).\n\n"
        f"**Step 2:** Write in factored form:\n"
        f"\\[ (x {'+' if p>=0 else '-'} {abs(p)})(x {'+' if q>=0 else '-'} {abs(q)}) = 0 \\]\n\n"
        f"**Step 3:** Set each factor equal to zero:\n"
        f"\\[ x = {r1} \\quad \\text{{or}} \\quad x = {r2} \\]"
    )
    return {
        "id": f"g10_eq_17_{rng.randint(100000, 999999)}",
        "subskill": "17_quadratic_trinomial_monic_positive_constant",
        "question_type": "short_answer",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": f"{r1} or {r2}",
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g10_eq_17",
        "misconception_tags": ["incorrect_factor_pair_selection", "sign_reversal_when_extracting_roots"],
        "marking_schema": [
            {"step": 1, "criterion": "Correct factors (x + p)(x + q)", "marks": 1},
            {"step": 2, "criterion": "First root", "marks": 1},
            {"step": 3, "criterion": "Second root", "marks": 1},
        ],
        "hints": {
            "tier_1": f"Look for two numbers that multiply to {c} and add to {b}.",
            "tier_2": f"The factors are (x {'+' if p>=0 else '-'} {abs(p)}) and (x {'+' if q>=0 else '-'} {abs(q)}).",
            "tier_3": ans,
        },
        "topic": "Equations and inequalities",
        "grade": "10",
        "subject": "Mathematics",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 3,
        "mode": "elementary_17_quadratic_trinomial_monic_positive_constant",
    }


# 18. Quadratic trinomial monic negative constant: x^2 + bx + c = 0 (c < 0)
def arch_18_quadratic_trinomial_monic_negative_constant(rng: random.Random) -> Dict[str, Any]:
    # (x + p)(x - q) = 0 where p > 0, q > 0
    p = rng.randint(1, 8)
    q = rng.randint(1, 8)
    while p == q:
        q = rng.randint(1, 8)
    b = p - q
    c = -p * q
    r1 = -p
    r2 = q
    sign_b = f"+ {b}" if b >= 0 else f"- {abs(b)}"

    prompt = f"Solve for \\(x\\) by factorisation:\n\\[ x^2 {sign_b}x - {abs(c)} = 0 \\]"
    ans = f"x = {r1} or x = {r2}"
    sol = (
        f"**Step 1:** Find two numbers that multiply to \\({c}\\) and add to \\({b}\\):\n"
        f"The numbers are \\({p}\\) and \\(-{q}\\).\n\n"
        f"**Step 2:** Write in factored form:\n"
        f"\\[ (x + {p})(x - {q}) = 0 \\]\n\n"
        f"**Step 3:** Set each factor equal to zero:\n"
        f"\\[ x = {r1} \\quad \\text{{or}} \\quad x = {r2} \\]"
    )
    return {
        "id": f"g10_eq_18_{rng.randint(100000, 999999)}",
        "subskill": "18_quadratic_trinomial_monic_negative_constant",
        "question_type": "short_answer",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": f"{r1} or {r2}",
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g10_eq_18",
        "misconception_tags": ["sign_error_opposite_signs_factors", "sign_reversal_roots"],
        "marking_schema": [
            {"step": 1, "criterion": "Correct factors (x + p)(x - q)", "marks": 1},
            {"step": 2, "criterion": "First root", "marks": 1},
            {"step": 3, "criterion": "Second root", "marks": 1},
        ],
        "hints": {
            "tier_1": f"Since the constant term is negative, the two factors have opposite signs.",
            "tier_2": f"Factors: (x + {p})(x - {q}) = 0.",
            "tier_3": ans,
        },
        "topic": "Equations and inequalities",
        "grade": "10",
        "subject": "Mathematics",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 3,
        "mode": "elementary_18_quadratic_trinomial_monic_negative_constant",
    }


# 19. Quadratic trinomial non-monic prime leading coefficient: 2x^2 + bx + c = 0
def arch_19_quadratic_trinomial_non_monic_prime_leading(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([2, 3])
    # (a*x + p)(x + q) = a*x^2 + (a*q + p)*x + p*q = 0
    p = rng.choice([-5, -3, -1, 1, 3, 5])
    q = rng.choice([-4, -2, -1, 1, 2, 4])
    b = a * q + p
    c = p * q
    # roots: x = -p/a or x = -q
    sign_b = f"+ {b}" if b >= 0 else f"- {abs(b)}"
    sign_c = f"+ {c}" if c >= 0 else f"- {abs(c)}"

    prompt = f"Solve for \\(x\\) by factorisation:\n\\[ {a}x^2 {sign_b}x {sign_c} = 0 \\]"
    root1_str = f"{-p}/{a}" if p % a != 0 else str(-p // a)
    root2_str = str(-q)
    ans = f"x = {root1_str} or x = {root2_str}"

    sol = (
        f"**Step 1:** Factorise the non-monic trinomial into binomial factors:\n"
        f"\\[ ({a}x {'+' if p>=0 else '-'} {abs(p)})(x {'+' if q>=0 else '-'} {abs(q)}) = 0 \\]\n\n"
        f"**Step 2:** Set each factor to zero:\n"
        f"\\[ {a}x {'+' if p>=0 else '-'} {abs(p)} = 0 \\implies x = {root1_str} \\]\n"
        f"\\[ x {'+' if q>=0 else '-'} {abs(q)} = 0 \\implies x = {root2_str} \\]"
    )
    return {
        "id": f"g10_eq_19_{rng.randint(100000, 999999)}",
        "subskill": "19_quadratic_trinomial_non_monic_prime_leading",
        "question_type": "short_answer",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": f"{root1_str} or {root2_str}",
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g10_eq_19",
        "misconception_tags": ["non_monic_grouping_error", "omitting_fractional_root"],
        "marking_schema": [
            {"step": 1, "criterion": "Factorise non-monic trinomial correctly", "marks": 1},
            {"step": 2, "criterion": "Solve for fractional root", "marks": 1},
            {"step": 3, "criterion": "Solve for integer root", "marks": 1},
        ],
        "hints": {
            "tier_1": f"Split the middle term or test factors of {a} and {c}.",
            "tier_2": f"Binomial factors are ({a}x {'+' if p>=0 else '-'} {abs(p)})(x {'+' if q>=0 else '-'} {abs(q)}).",
            "tier_3": ans,
        },
        "topic": "Equations and inequalities",
        "grade": "10",
        "subject": "Mathematics",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 3,
        "mode": "elementary_19_quadratic_trinomial_non_monic_prime_leading",
    }


# 20. Quadratic perfect square binomial: (x + p)^2 = 0 or (x - p)^2 = 0
def arch_20_quadratic_perfect_square_binomial(rng: random.Random) -> Dict[str, Any]:
    p = rng.choice([-8, -7, -6, -5, -4, -3, 3, 4, 5, 6, 7, 8])
    b = 2 * p
    c = p * p
    sign_b = f"+ {b}" if b >= 0 else f"- {abs(b)}"
    ans = -p

    prompt = f"Solve for \\(x\\):\n\\[ x^2 {sign_b}x + {c} = 0 \\]"
    sol = (
        f"**Step 1:** Recognise the expression as a perfect square trinomial:\n"
        f"\\[ (x {'+' if p>=0 else '-'} {abs(p)})^2 = 0 \\]\n\n"
        f"**Step 2:** Take the square root of both sides:\n"
        f"\\[ x {'+' if p>=0 else '-'} {abs(p)} = 0 \\]\n"
        f"\\[ x = {ans} \\quad \\text{{(repeated root)}} \\]"
    )
    return {
        "id": f"g10_eq_20_{rng.randint(100000, 999999)}",
        "subskill": "20_quadratic_perfect_square_binomial",
        "question_type": "short_answer",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": str(ans),
        "sample_answer": f"x = {ans}",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g10_eq_20",
        "misconception_tags": ["missing_repeated_root_concept", "sign_error_square_root"],
        "marking_schema": [
            {"step": 1, "criterion": "Express as perfect square binomial squared", "marks": 1},
            {"step": 2, "criterion": "State equal/repeated root", "marks": 1},
        ],
        "hints": {
            "tier_1": f"Notice that ({p})^2 = {c} and 2*({p}) = {b}.",
            "tier_2": f"(x {'+' if p>=0 else '-'} {abs(p)})^2 = 0.",
            "tier_3": f"x = {ans}",
        },
        "topic": "Equations and inequalities",
        "grade": "10",
        "subject": "Mathematics",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 2,
        "mode": "elementary_20_quadratic_perfect_square_binomial",
    }


# 21. Quadratic fraction cross multiplication: x / a = b / x
def arch_21_quadratic_fraction_cross_multiplication(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([2, 3, 4, 8, 9])
    ans_val = rng.choice([6, 8, 10, 12])
    # x^2 = a * b = ans_val^2 => b = ans_val^2 / a
    b = (ans_val * ans_val) // a
    while b * a != ans_val * ans_val:
        a = 2
        ans_val = 6
        b = 18

    prompt = (
        f"Solve for \\(x\\) (state restrictions):\n"
        f"\\[ \\frac{{x}}{{{a}}} = \\frac{{{b}}}{{x}} \\]"
    )
    ans = f"x = {ans_val} or x = -{ans_val}"
    sol = (
        f"**Step 1:** State restriction:\n"
        f"\\(x \\neq 0\\) since \\(x\\) is in the denominator.\n\n"
        f"**Step 2:** Cross-multiply:\n"
        f"\\[ x \\times x = {a} \\times {b} \\]\n"
        f"\\[ x^2 = {a * b} \\]\n\n"
        f"**Step 3:** Take the square root of both sides:\n"
        f"\\[ x = \\pm \\sqrt{{{a * b}}} = \\pm {ans_val} \\]\n"
        f"\\[ x = {ans_val} \\quad \\text{{or}} \\quad x = -{ans_val} \\]"
    )
    return {
        "id": f"g10_eq_21_{rng.randint(100000, 999999)}",
        "subskill": "21_quadratic_fraction_cross_multiplication",
        "question_type": "short_answer",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": f"{ans_val} or -{ans_val}",
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g10_eq_21",
        "misconception_tags": ["omitting_negative_root", "ignoring_zero_denominator_restriction"],
        "marking_schema": [
            {"step": 1, "criterion": "Cross multiply to obtain x^2 = k", "marks": 1},
            {"step": 2, "criterion": "Include both +/- square roots", "marks": 1},
            {"step": 3, "criterion": "Confirm validity against x != 0", "marks": 1},
        ],
        "hints": {
            "tier_1": "Cross-multiply: x * x = a * b.",
            "tier_2": f"x^2 = {a*b}. Remember to include both + and - square roots.",
            "tier_3": ans,
        },
        "topic": "Equations and inequalities",
        "grade": "10",
        "subject": "Mathematics",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 3,
        "mode": "elementary_21_quadratic_fraction_cross_multiplication",
    }


# 22. Quadratic fraction clearing binomial denominator: x + k/x = m
def arch_22_quadratic_fraction_clearing_binomial_denominator(rng: random.Random) -> Dict[str, Any]:
    # x + k/x = m => x^2 - m*x + k = 0
    # choose roots r1, r2 != 0
    r1 = rng.choice([1, 2, 3, 4])
    r2 = rng.choice([2, 3, 5, 6])
    while r1 == r2:
        r2 = rng.choice([5, 6, 7])
    m = r1 + r2
    k = r1 * r2

    prompt = (
        f"Solve for \\(x\\) (state restrictions):\n"
        f"\\[ x + \\frac{{{k}}}{{x}} = {m} \\]"
    )
    ans = f"x = {r1} or x = {r2}"
    sol = (
        f"**Step 1:** State restriction: \\(x \\neq 0\\).\n\n"
        f"**Step 2:** Multiply the entire equation by \\(x\\) to clear fractions:\n"
        f"\\[ x(x) + x\\left(\\frac{{{k}}}{{x}}\\right) = x({m}) \\]\n"
        f"\\[ x^2 + {k} = {m}x \\]\n\n"
        f"**Step 3:** Rearrange into standard quadratic form:\n"
        f"\\[ x^2 - {m}x + {k} = 0 \\]\n\n"
        f"**Step 4:** Factorise and solve:\n"
        f"\\[ (x - {r1})(x - {r2}) = 0 \\]\n"
        f"\\[ x = {r1} \\quad \\text{{or}} \\quad x = {r2} \\]"
    )
    return {
        "id": f"g10_eq_22_{rng.randint(100000, 999999)}",
        "subskill": "22_quadratic_fraction_clearing_binomial_denominator",
        "question_type": "short_answer",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": f"{r1} or {r2}",
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 4,
        "learning_objective_id": "math_g10_eq_22",
        "misconception_tags": ["clearing_fraction_partially", "sign_error_standard_form"],
        "marking_schema": [
            {"step": 1, "criterion": "Multiply all terms by x and state x != 0", "marks": 1},
            {"step": 2, "criterion": "Write in standard form x^2 - mx + k = 0", "marks": 1},
            {"step": 3, "criterion": "Factorise trinomial", "marks": 1},
            {"step": 4, "criterion": "State both valid roots", "marks": 1},
        ],
        "hints": {
            "tier_1": "Multiply every term by x to eliminate the fraction.",
            "tier_2": f"Rearrange to x^2 - {m}x + {k} = 0 and factorise.",
            "tier_3": ans,
        },
        "topic": "Equations and inequalities",
        "grade": "10",
        "subject": "Mathematics",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 3,
        "mode": "elementary_22_quadratic_fraction_clearing_binomial_denominator",
    }


# 23. Quadratic substituting and verifying roots
def arch_23_quadratic_substituting_and_verifying_roots(rng: random.Random) -> Dict[str, Any]:
    # Check whether a given value is a root of x^2 + bx + c = 0
    r1 = rng.choice([-4, -3, -2, 2, 3, 4])
    r2 = rng.choice([-5, -1, 1, 5])
    b = -(r1 + r2)
    c = r1 * r2
    sign_b = f"+ {b}" if b >= 0 else f"- {abs(b)}"
    sign_c = f"+ {c}" if c >= 0 else f"- {abs(c)}"

    is_root = rng.choice([True, False])
    test_val = r1 if is_root else r1 + rng.choice([-1, 1])

    prompt = (
        f"Determine whether \\(x = {test_val}\\) is a valid root of the quadratic equation:\n"
        f"\\[ x^2 {sign_b}x {sign_c} = 0 \\]"
    )
    ans = "Yes" if is_root else "No"
    val_calc = (test_val ** 2) + b * test_val + c
    sol = (
        f"**Step 1:** Substitute \\(x = {test_val}\\) into the left-hand side (LHS):\n"
        f"\\[ \\text{{LHS}} = ({test_val})^2 {sign_b}({test_val}) {sign_c} \\]\n"
        f"\\[ \\text{{LHS}} = {test_val**2} {'+' if b*test_val>=0 else '-'} {abs(b*test_val)} {sign_c} = {val_calc} \\]\n\n"
        f"**Step 2:** Compare with the right-hand side (RHS = 0):\n"
        f"Since \\(\\text{{LHS}} {('=' if is_root else '\\neq')} \\text{{RHS}}\\), \\(x = {test_val}\\) **{('is a valid root' if is_root else 'is not a root')}**."
    )
    return {
        "id": f"g10_eq_23_{rng.randint(100000, 999999)}",
        "subskill": "23_quadratic_substituting_and_verifying_roots",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": ["Yes", "No"],
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g10_eq_23",
        "misconception_tags": ["arithmetic_error_negative_squaring", "root_verification_misunderstanding"],
        "marking_schema": [
            {"step": 1, "criterion": "Correct substitution into quadratic expression", "marks": 1},
            {"step": 2, "criterion": f"Correct evaluation and Yes/No conclusion", "marks": 1},
        ],
        "hints": {
            "tier_1": f"Replace x with {test_val} and evaluate the expression.",
            "tier_2": f"LHS evaluates to {val_calc}.",
            "tier_3": ans,
        },
        "topic": "Equations and inequalities",
        "grade": "10",
        "subject": "Mathematics",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 2,
        "mode": "elementary_23_quadratic_substituting_and_verifying_roots",
    }


# 24. Quadratic extraneous root restriction elimination: (x^2 - 4)/(x - 2) = 5
def arch_24_quadratic_extraneous_root_restriction_elimination(rng: random.Random) -> Dict[str, Any]:
    b = rng.choice([2, 3, 4, 5])
    b2 = b * b
    # (x^2 - b^2)/(x - b) = k => x + b = k => x = k - b
    # If k = 2*b, then x = b, which is excluded by restriction x != b!
    # Let's test a case where quadratic factorisation produces two apparent roots, one restricted:
    # x - 1 = (x^2 - 1)/(x - 1)...
    # Better: (x^2 + a*x) / (x + a) = 3 => x = 3
    # Standard Gr10 case:
    # x + (b)/(x - b) = b + (b)/(x - b) -> x = b, but x != b so no solution!
    # Or: (x^2 - b^2) / (x - b) = k
    k = rng.randint(6, 15)
    ans = k - b

    prompt = (
        f"Solve for \\(x\\) and check against restrictions:\n"
        f"\\[ \\frac{{x^2 - {b2}}}{{x - {b}}} = {k} \\]"
    )
    sol = (
        f"**Step 1:** State the restriction:\n"
        f"\\[ x - {b} \\neq 0 \\implies x \\neq {b} \\]\n\n"
        f"**Step 2:** Factorise the numerator as a difference of two squares:\n"
        f"\\[ \\frac{{(x - {b})(x + {b})}}{{x - {b}}} = {k} \\]\n\n"
        f"**Step 3:** Cancel the common factor \\((x - {b})\\) (valid since \\(x \\neq {b}\\)):\n"
        f"\\[ x + {b} = {k} \\]\n"
        f"\\[ x = {k} - {b} = {ans} \\]\n\n"
        f"Since \\({ans} \\neq {b}\\), the solution is valid: **\\(x = {ans}\\)**."
    )
    return {
        "id": f"g10_eq_24_{rng.randint(100000, 999999)}",
        "subskill": "24_quadratic_extraneous_root_restriction_elimination",
        "question_type": "short_answer",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": str(ans),
        "sample_answer": f"x = {ans}",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g10_eq_24",
        "misconception_tags": ["extraneous_root_acceptance", "cancelling_without_restriction"],
        "marking_schema": [
            {"step": 1, "criterion": "State restriction x != b", "marks": 1},
            {"step": 2, "criterion": "Factorise difference of squares and simplify", "marks": 1},
            {"step": 3, "criterion": "Solve and verify validity", "marks": 1},
        ],
        "hints": {
            "tier_1": f"Restriction: x cannot equal {b}.",
            "tier_2": f"Factorise x^2 - {b2} = (x - {b})(x + {b}) and cancel (x - {b}).",
            "tier_3": f"x = {ans}",
        },
        "topic": "Equations and inequalities",
        "grade": "10",
        "subject": "Mathematics",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 3,
        "mode": "elementary_24_quadratic_extraneous_root_restriction_elimination",
    }


# 25. Simultaneous linear substitution direct variable: y = ax + b and cx + dy = e
def arch_25_simultaneous_linear_substitution_direct_variable(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([2, 3])
    x_val = rng.randint(1, 5)
    b = rng.randint(-4, 4)
    y_val = a * x_val + b
    # equation 2: c*x + d*y = e
    c = rng.choice([2, 3, 4])
    d = rng.choice([1, 2])
    e = c * x_val + d * y_val

    sign_b = f"+ {b}" if b >= 0 else f"- {abs(b)}"

    prompt = (
        f"Solve the system of simultaneous equations using the **substitution method**:\n"
        f"\\[ (1) \\quad y = {a}x {sign_b} \\]\n"
        f"\\[ (2) \\quad {c}x + {d}y = {e} \\]"
    )
    ans = f"x = {x_val}, y = {y_val}"
    sol = (
        f"**Step 1:** Substitute equation (1) into equation (2):\n"
        f"\\[ {c}x + {d}({a}x {sign_b}) = {e} \\]\n\n"
        f"**Step 2:** Expand brackets and solve for \\(x\\):\n"
        f"\\[ {c}x + {d*a}x {'+' if d*b>=0 else '-'} {abs(d*b)} = {e} \\]\n"
        f"\\[ {c + d*a}x = {e} - ({d*b}) = {e - d*b} \\]\n"
        f"\\[ x = \\frac{{{e - d*b}}}{{{c + d*a}}} = {x_val} \\]\n\n"
        f"**Step 3:** Substitute \\(x = {x_val}\\) back into equation (1) to find \\(y\\):\n"
        f"\\[ y = {a}({x_val}) {sign_b} = {a * x_val + b} = {y_val} \\]\n\n"
        f"**Solution:** \\(x = {x_val},\\; y = {y_val}\\)"
    )
    return {
        "id": f"g10_eq_25_{rng.randint(100000, 999999)}",
        "subskill": "25_simultaneous_linear_substitution_direct_variable",
        "question_type": "short_answer",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": f"x = {x_val}, y = {y_val}",
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 4,
        "learning_objective_id": "math_g10_eq_25",
        "misconception_tags": ["substitution_bracket_error", "omitting_second_variable"],
        "marking_schema": [
            {"step": 1, "criterion": "Substitute expression for y into equation (2)", "marks": 1},
            {"step": 2, "criterion": "Solve for x correctly", "marks": 1},
            {"step": 3, "criterion": "Substitute back to solve for y", "marks": 1},
            {"step": 4, "criterion": "State complete coordinate pair / solution", "marks": 1},
        ],
        "hints": {
            "tier_1": f"Equation (1) already gives y = {a}x {sign_b}. Replace y in equation (2) with ({a}x {sign_b}).",
            "tier_2": f"You get {c + d*a}x + {d*b} = {e}, which gives x = {x_val}.",
            "tier_3": ans,
        },
        "topic": "Equations and inequalities",
        "grade": "10",
        "subject": "Mathematics",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 4,
        "mode": "elementary_25_simultaneous_linear_substitution_direct_variable",
    }


BUILDERS_01_25 = {
    "01_linear_one_step_addition_subtraction": arch_01_linear_one_step_addition_subtraction,
    "02_linear_one_step_multiplication_division": arch_02_linear_one_step_multiplication_division,
    "03_linear_two_step_ax_plus_b_equals_c": arch_03_linear_two_step_ax_plus_b_equals_c,
    "04_linear_brackets_distributive_single": arch_04_linear_brackets_distributive_single,
    "05_linear_brackets_both_sides": arch_05_linear_brackets_both_sides,
    "06_linear_variables_both_sides_collect": arch_06_linear_variables_both_sides_collect,
    "07_linear_fractions_numerical_denominator_monomial": arch_07_linear_fractions_numerical_denominator_monomial,
    "08_linear_fractions_numerical_denominators_binomial_numerators": arch_08_linear_fractions_numerical_denominators_binomial_numerators,
    "09_linear_fractions_lcd_clearing_three_terms": arch_09_linear_fractions_lcd_clearing_three_terms,
    "10_linear_fraction_variable_denominator_restriction": arch_10_linear_fraction_variable_denominator_restriction,
    "11_linear_fraction_difference_of_squares_denominator": arch_11_linear_fraction_difference_of_squares_denominator,
    "12_linear_equation_no_solution_inconsistent": arch_12_linear_equation_no_solution_inconsistent,
    "13_linear_equation_identity_all_real_numbers": arch_13_linear_equation_identity_all_real_numbers,
    "14_quadratic_standard_form_identification": arch_14_quadratic_standard_form_identification,
    "15_quadratic_common_factor_monomial": arch_15_quadratic_common_factor_monomial,
    "16_quadratic_difference_of_two_squares": arch_16_quadratic_difference_of_two_squares,
    "17_quadratic_trinomial_monic_positive_constant": arch_17_quadratic_trinomial_monic_positive_constant,
    "18_quadratic_trinomial_monic_negative_constant": arch_18_quadratic_trinomial_monic_negative_constant,
    "19_quadratic_trinomial_non_monic_prime_leading": arch_19_quadratic_trinomial_non_monic_prime_leading,
    "20_quadratic_perfect_square_binomial": arch_20_quadratic_perfect_square_binomial,
    "21_quadratic_fraction_cross_multiplication": arch_21_quadratic_fraction_cross_multiplication,
    "22_quadratic_fraction_clearing_binomial_denominator": arch_22_quadratic_fraction_clearing_binomial_denominator,
    "23_quadratic_substituting_and_verifying_roots": arch_23_quadratic_substituting_and_verifying_roots,
    "24_quadratic_extraneous_root_restriction_elimination": arch_24_quadratic_extraneous_root_restriction_elimination,
    "25_simultaneous_linear_substitution_direct_variable": arch_25_simultaneous_linear_substitution_direct_variable,
}
