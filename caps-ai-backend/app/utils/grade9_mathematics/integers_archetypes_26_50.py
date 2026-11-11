"""Grade 9 Mathematics - Integers Archetypes 26 to 50.
Grounded in curriculum_docs_auto/Mathematics_Gr9/Term 1/02. Integers.md.
Covers:
  - Powers of negative integers (even vs odd exponents).
  - Distinguishing (-a)^n vs -a^n.
  - Square roots with leading negation and Cube roots of negative integers.
  - Combined powers and roots expressions.
  - Order of operations (BODMAS) with nested brackets and fractional bars.
  - Algebraic substitution with negative integer values.
  - Solving linear equations with negative coefficients.
  - Contextual problems: submarine descent/ascent, mine shaft lifts.
  - Error analysis: double negative, exponent bracket errors, BODMAS precedence errors.
  - Compound multi-step integer challenge problems.
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional, Tuple


# ----------------------------------------------------------------------
# 26. Power of Negative Integer: Even Exponent
# ----------------------------------------------------------------------
def arch_26_power_of_negative_integer_even_exponent(rng: random.Random) -> Dict[str, Any]:
    base = rng.choice([2, 3, 4, 5])
    exp = rng.choice([2, 4])
    ans = base ** exp

    prompt = (
        f"Evaluate the power:\n\n"
        f"\\[ (-{base})^{{{exp}}} \\]\n\n"
        f"Explain why the final result is positive."
    )
    sol = (
        f"**Even Exponent Rule:**\n"
        f"A negative number raised to an **even exponent** results in an even number of negative factors, "
        f"which multiply in pairs to produce a positive product:\n"
        f"\\[ (-{base})^{{{exp}}} = +({base}^{{{exp}}}) = {ans} \\]"
    )
    return {
        "id": f"g9_int_pow_even_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": str(ans),
        "sample_answer": str(ans),
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "26_power_of_negative_integer_even_exponent",
        "learning_objective_id": "math_g9_int_pow_even",
        "hints": {
            "tier_1": "Even power of a negative number is always positive.",
            "tier_2": f"(-{base}) * (-{base}) = {base ** 2}.",
            "tier_3": str(ans),
        },
        "misconception_tags": ["keeping_negative_sign_for_even_powers"],
    }


# ----------------------------------------------------------------------
# 27. Power of Negative Integer: Odd Exponent
# ----------------------------------------------------------------------
def arch_27_power_of_negative_integer_odd_exponent(rng: random.Random) -> Dict[str, Any]:
    base = rng.choice([2, 3, 4, 5])
    exp = 3
    ans = -(base ** exp)

    prompt = (
        f"Evaluate the power:\n\n"
        f"\\[ (-{base})^{{{exp}}} \\]\n\n"
        f"State whether the result is positive or negative, and give the numeric value."
    )
    sol = (
        f"**Odd Exponent Rule:**\n"
        f"A negative base raised to an **odd exponent** has an unpaired negative factor, "
        f"resulting in a negative answer:\n"
        f"\\[ (-{base})^3 = (-{base}) \\times (-{base}) \\times (-{base}) = (+{base**2}) \\times (-{base}) = {ans} \\]"
    )
    return {
        "id": f"g9_int_pow_odd_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": str(ans),
        "sample_answer": str(ans),
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "27_power_of_negative_integer_odd_exponent",
        "learning_objective_id": "math_g9_int_pow_odd",
        "hints": {
            "tier_1": "Odd powers of negative numbers preserve the negative sign.",
            "tier_2": f"-({base}^3) = {ans}.",
            "tier_3": str(ans),
        },
        "misconception_tags": ["thinking_all_squared_and_cubed_negatives_become_positive"],
    }


# ----------------------------------------------------------------------
# 28. Distinguish Bracketed Power vs Unbracketed Negation
# ----------------------------------------------------------------------
def arch_28_distinguish_bracketed_power_vs_unbracketed_negation(rng: random.Random) -> Dict[str, Any]:
    n = rng.choice([3, 4, 5, 6])
    ans_bracketed = n ** 2
    ans_unbracketed = -(n ** 2)

    prompt = (
        f"Compare and evaluate both expressions without a calculator:\n\n"
        f"1. \\( (-{n})^2 \\)\n"
        f"2. \\( -{n}^2 \\)\n\n"
        f"Explain the critical difference in how brackets affect the sign."
    )
    sol = (
        f"**Comparison of Powers:**\n"
        f"1. In \\((- {n})^2\\), the base is \\(-{n}\\): \\((- {n}) \\times (- {n}) = {ans_bracketed}\\).\n"
        f"2. In \\(-{n}^2\\), the base is only \\({n}\\), with negation applied afterwards: \\(-( {n} \\times {n}) = {ans_unbracketed}\\).\n\n"
        f"Therefore, \\((- {n})^2 = {ans_bracketed}\\) while \\(-{n}^2 = {ans_unbracketed}\\)."
    )
    ans = f"1. {ans_bracketed}; 2. {ans_unbracketed}"
    return {
        "id": f"g9_int_pow_distinguish_{rng.randint(100000, 999999)}",
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
        "subskill": "28_distinguish_bracketed_power_vs_unbracketed_negation",
        "learning_objective_id": "math_g9_int_pow_distinguish",
        "hints": {
            "tier_1": "Without brackets, the exponent applies only to the base number, not the negative sign.",
            "tier_2": f"(-{n})^2 = +{ans_bracketed}, but -{n}^2 = {ans_unbracketed}.",
            "tier_3": ans,
        },
        "misconception_tags": ["treating_minus_n_squared_as_positive"],
    }


# ----------------------------------------------------------------------
# 29. Square Root with Leading Negation Outside Radical
# ----------------------------------------------------------------------
def arch_29_square_root_with_negative_sign_outside_radical(rng: random.Random) -> Dict[str, Any]:
    root_val = rng.choice([6, 7, 8, 9, 11, 12])
    radicand = root_val ** 2
    ans = -root_val

    prompt = (
        f"Evaluate the real number expression:\n\n"
        f"\\[ -\\sqrt{{{radicand}}} \\]\n\n"
        f"Explain why this expression is a valid real number, whereas $\\sqrt{{-{radicand}}}$ is non-real."
    )
    sol = (
        f"**Evaluation:**\n"
        f"1. First evaluate the principal square root inside the radical: \\(\\sqrt{{{radicand}}} = {root_val}\\).\n"
        f"2. Apply the negative sign outside: \\(-({root_val}) = {ans}\\).\n"
        f"This is a real number because the radicand ({radicand}) is positive; $\\sqrt{{-{radicand}}}$ has a negative radicand and is non-real."
    )
    return {
        "id": f"g9_int_neg_sqrt_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": str(ans),
        "sample_answer": str(ans),
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "29_square_root_with_negative_sign_outside_radical",
        "learning_objective_id": "math_g9_int_neg_sqrt",
        "hints": {
            "tier_1": "Evaluate the square root first, then apply the negative sign.",
            "tier_2": f"-({root_val}) = {ans}.",
            "tier_3": str(ans),
        },
        "misconception_tags": ["confusing_negative_outside_radical_with_negative_inside"],
    }


# ----------------------------------------------------------------------
# 30. Cube Root of Negative Integer
# ----------------------------------------------------------------------
def arch_30_cube_root_of_negative_integer(rng: random.Random) -> Dict[str, Any]:
    root_val = rng.choice([2, 3, 4, 5])
    radicand = -(root_val ** 3)
    ans = -root_val

    prompt = (
        f"Evaluate without a calculator:\n\n"
        f"\\[ \\sqrt[3]{{{radicand}}} \\]\n\n"
        f"Verify your answer by cubing it."
    )
    sol = (
        f"**Cube Root of Negative:**\n"
        f"Since $(-{root_val})^3 = (-{root_val}) \\times (-{root_val}) \\times (-{root_val}) = {radicand}$:\n"
        f"\\[ \\sqrt[3]{{{radicand}}} = {ans} \\]"
    )
    return {
        "id": f"g9_int_cbrt_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": str(ans),
        "sample_answer": str(ans),
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "30_cube_root_of_negative_integer",
        "learning_objective_id": "math_g9_int_cbrt",
        "hints": {
            "tier_1": "Cube roots of negative numbers are real and negative.",
            "tier_2": f"What number multiplied by itself three times gives {radicand}?",
            "tier_3": str(ans),
        },
        "misconception_tags": ["believing_cube_root_of_negative_is_non_real"],
    }


# ----------------------------------------------------------------------
# 31. Combined Powers and Roots of Negative Integers
# ----------------------------------------------------------------------
def arch_31_combined_powers_and_roots_of_negative_integers(rng: random.Random) -> Dict[str, Any]:
    # e.g., (-2)^3 + cbrt(-27) - (-3)^2 = -8 + (-3) - 9 = -20
    b = rng.choice([2, 3])
    pow_term = -(b ** 3)
    cbrt_num = -rng.choice([8, 27, 64])
    cbrt_val = round(math.copysign(abs(cbrt_num)**(1/3), cbrt_num))
    sq_base = rng.choice([2, 3, 4])
    sq_val = sq_base ** 2
    ans = pow_term + cbrt_val - sq_val

    prompt = (
        f"Simplify the expression by evaluating each term:\n\n"
        f"\\[ (-{b})^3 + \\sqrt[3]{{{cbrt_num}}} - (-{sq_base})^2 \\]"
    )
    sol = (
        f"**Step-by-step Evaluation:**\n"
        f"1. \\((- {b})^3 = {pow_term}\\)\n"
        f"2. \\(\\sqrt[3]{{{cbrt_num}}} = {cbrt_val}\\)\n"
        f"3. \\((- {sq_base})^2 = {sq_val}\\)\n\n"
        f"Combine terms:\n"
        f"\\[ ({pow_term}) + ({cbrt_val}) - ({sq_val}) = {ans} \\]"
    )
    return {
        "id": f"g9_int_pow_root_combo_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": str(ans),
        "sample_answer": str(ans),
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "subskill": "31_combined_powers_and_roots_of_negative_integers",
        "learning_objective_id": "math_g9_int_pow_root_combo",
        "hints": {
            "tier_1": f"(-{b})^3 = {pow_term}, cbrt({cbrt_num}) = {cbrt_val}, (-{sq_base})^2 = {sq_val}.",
            "tier_2": f"Combine: {pow_term} + ({cbrt_val}) - {sq_val}.",
            "tier_3": str(ans),
        },
        "misconception_tags": ["sign_error_when_subtracting_squared_term"],
    }


# ----------------------------------------------------------------------
# 32. Order of Operations: Brackets & Multiplication with Integers
# ----------------------------------------------------------------------
def arch_32_order_of_operations_brackets_and_multiplication_with_integers(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(2, 6)
    b = -rng.randint(3, 8)
    c = rng.randint(4, 9)
    ans = a * (b + c)

    prompt = (
        f"Apply the correct order of operations (BODMAS) to evaluate:\n\n"
        f"\\[ {a} \\times ({b} + {c}) \\]"
    )
    sol = (
        f"**BODMAS Working:**\n"
        f"1. Inner brackets first: \\({b} + {c} = {b + c}\\).\n"
        f"2. Multiply: \\({a} \\times ({b + c}) = {ans}\\)."
    )
    return {
        "id": f"g9_int_bodmas_brack_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": str(ans),
        "sample_answer": str(ans),
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "32_order_of_operations_brackets_and_multiplication_with_integers",
        "learning_objective_id": "math_g9_int_bodmas_brack",
        "hints": {
            "tier_1": "Calculate the operation inside the bracket first.",
            "tier_2": f"{b} + {c} = {b + c}, then multiply by {a}.",
            "tier_3": str(ans),
        },
        "misconception_tags": ["multiplying_before_simplifying_brackets_incorrectly"],
    }


# ----------------------------------------------------------------------
# 33. Order of Operations: Nested Brackets and Negatives
# ----------------------------------------------------------------------
def arch_33_order_of_operations_nested_brackets_and_negatives(rng: random.Random) -> Dict[str, Any]:
    # e.g., 5 - 2 * [ -3 + (-4 * -2) ] = 5 - 2 * [-3 + 8] = 5 - 2 * 5 = -5
    a = rng.randint(3, 8)
    b = rng.randint(2, 4)
    c = -rng.randint(3, 6)
    d = -rng.randint(2, 4)
    e = -rng.randint(2, 3)

    inner = c + (d * e)
    bracket_res = inner
    ans = a - b * bracket_res

    prompt = (
        f"Evaluate the nested integer expression:\n\n"
        f"\\[ {a} - {b} \\times [ {c} + ({d}) \\times ({e}) ] \\]"
    )
    sol = (
        f"**Nested Brackets Evaluation:**\n"
        f"1. Innermost multiplication: \\(({d}) \\times ({e}) = +{d * e}\\).\n"
        f"2. Square brackets: \\({c} + {d * e} = {inner}\\).\n"
        f"3. Multiply before subtraction: \\({b} \\times {inner} = {b * inner}\\).\n"
        f"4. Final subtraction: \\({a} - ({b * inner}) = {ans}\\)."
    )
    return {
        "id": f"g9_int_nested_brack_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": str(ans),
        "sample_answer": str(ans),
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "subskill": "33_order_of_operations_nested_brackets_and_negatives",
        "learning_objective_id": "math_g9_int_nested_brack",
        "hints": {
            "tier_1": "Innermost round brackets first, then square brackets, then outer operations.",
            "tier_2": f"Inside square brackets: {c} + {d*e} = {inner}.",
            "tier_3": str(ans),
        },
        "misconception_tags": ["subtracting_a_minus_b_before_multiplying_by_brackets"],
    }


# ----------------------------------------------------------------------
# 34. Order of Operations: Powers Before Multiplication Signed
# ----------------------------------------------------------------------
def arch_34_order_of_operations_powers_before_multiplication_signed(rng: random.Random) -> Dict[str, Any]:
    # e.g., -3 * (-2)^3 - 4 * (-1)^4
    a = -rng.randint(2, 5)
    b = -2
    b_pow = 3
    b_val = b ** b_pow  # -8
    c = rng.randint(3, 7)
    ans = (a * b_val) - c

    prompt = (
        f"Evaluate respecting operation precedence:\n\n"
        f"\\[ {a} \\times ({b})^3 - {c} \\]"
    )
    sol = (
        f"**Precedence (Powers before Multiplication):**\n"
        f"1. Evaluate power first: \\(({b})^3 = {b_val}\\).\n"
        f"2. Multiply: \\({a} \\times ({b_val}) = {a * b_val}\\).\n"
        f"3. Subtract: \\({a * b_val} - {c} = {ans}\\)."
    )
    return {
        "id": f"g9_int_pow_mult_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": str(ans),
        "sample_answer": str(ans),
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "34_order_of_operations_powers_before_multiplication_signed",
        "learning_objective_id": "math_g9_int_pow_mult",
        "hints": {
            "tier_1": "Calculate (-2)^3 first.",
            "tier_2": f"Multiply {a} * ({b_val}) = {a * b_val}, then subtract {c}.",
            "tier_3": str(ans),
        },
        "misconception_tags": ["multiplying_base_by_coefficient_before_applying_exponent"],
    }


# ----------------------------------------------------------------------
# 35. Fractional Expression: Signed Numerator and Denominator
# ----------------------------------------------------------------------
def arch_35_fractional_expression_signed_numerator_and_denominator(rng: random.Random) -> Dict[str, Any]:
    # e.g., (-18 + (-6)) / (-3 - 5) = -24 / -8 = 3
    den_tot = -rng.choice([2, 3, 4, 6])
    ans = rng.choice([-5, -4, -3, -2, 2, 3, 4, 5])
    num_tot = ans * den_tot
    num1 = -rng.randint(6, 15)
    num2 = num_tot - num1

    den1 = den_tot // 2
    den2 = den_tot - den1

    prompt = (
        f"Simplify the fraction by evaluating numerator and denominator separately:\n\n"
        f"\\[ \\frac{{{num1} + ({num2})}}{{{den1} + ({den2})}} \\]"
    )
    sol = (
        f"**Fraction Evaluation:**\n"
        f"1. Numerator: \\({num1} + ({num2}) = {num_tot}\\).\n"
        f"2. Denominator: \\({den1} + ({den2}) = {den_tot}\\).\n"
        f"3. Divide: \\(\\frac{{{num_tot}}}{{{den_tot}}} = {ans}\\)."
    )
    return {
        "id": f"g9_int_frac_eval_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": str(ans),
        "sample_answer": str(ans),
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "subskill": "35_fractional_expression_signed_numerator_and_denominator",
        "learning_objective_id": "math_g9_int_frac_eval",
        "hints": {
            "tier_1": "The fraction bar acts as a grouping symbol: calculate top and bottom completely first.",
            "tier_2": f"Numerator = {num_tot}, Denominator = {den_tot}.",
            "tier_3": str(ans),
        },
        "misconception_tags": ["cancelling_individual_terms_across_addition_in_fraction"],
    }


# ----------------------------------------------------------------------
# 36. Fractional Expression: Order of Operations with Roots
# ----------------------------------------------------------------------
def arch_36_fractional_expression_order_of_operations_with_roots(rng: random.Random) -> Dict[str, Any]:
    # e.g., (sqrt(100 - 36)) / (-2) = sqrt(64) / -2 = 8 / -2 = -4
    ans = -rng.choice([2, 3, 4, 5])
    den = -2
    root_val = ans * den  # positive
    radicand = root_val ** 2
    p1 = 100
    p2 = p1 - radicand

    prompt = (
        f"Evaluate the expression completely:\n\n"
        f"\\[ \\frac{{\\sqrt{{{p1} - {p2}}}}}{{{den}}} \\]"
    )
    sol = (
        f"**Step-by-step Evaluation:**\n"
        f"1. Simplify under the radical: \\({p1} - {p2} = {radicand}\\).\n"
        f"2. Principal square root: \\(\\sqrt{{{radicand}}} = {root_val}\\).\n"
        f"3. Divide by denominator: \\(\\frac{{{root_val}}}{{{den}}} = {ans}\\)."
    )
    return {
        "id": f"g9_int_frac_root_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": str(ans),
        "sample_answer": str(ans),
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "subskill": "36_fractional_expression_order_of_operations_with_roots",
        "learning_objective_id": "math_g9_int_frac_root",
        "hints": {
            "tier_1": "Subtract under the square root before taking the root.",
            "tier_2": f"sqrt({radicand}) = {root_val}, then divide by {den}.",
            "tier_3": str(ans),
        },
        "misconception_tags": ["distributing_square_root_across_subtraction"],
    }


# ----------------------------------------------------------------------
# 37. Algebraic Substitution: Linear Expression (Negative Variable)
# ----------------------------------------------------------------------
def arch_37_algebraic_substitution_linear_expression_negative_variable(rng: random.Random) -> Dict[str, Any]:
    x_val = -rng.randint(2, 6)
    m = rng.choice([3, 4, 5, -2, -3])
    c = rng.choice([-8, -5, 6, 9])
    ans = m * x_val + c

    c_str = f"+ {c}" if c >= 0 else f"- {abs(c)}"

    prompt = (
        f"Given that **$x = {x_val}$**, evaluate the linear expression:\n\n"
        f"\\[ {m}x {c_str} \\]"
    )
    sol = (
        f"**Substitution Working:**\n"
        f"\\[ {m}({x_val}) {c_str} = {m * x_val} {c_str} = {ans} \\]"
    )
    return {
        "id": f"g9_int_subst_lin_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": str(ans),
        "sample_answer": str(ans),
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "37_algebraic_substitution_linear_expression_negative_variable",
        "learning_objective_id": "math_g9_int_subst_lin",
        "hints": {
            "tier_1": f"Replace x with ({x_val}) in brackets.",
            "tier_2": f"{m} * ({x_val}) = {m * x_val}.",
            "tier_3": str(ans),
        },
        "misconception_tags": ["forgetting_brackets_when_substituting_negative_variable"],
    }


# ----------------------------------------------------------------------
# 38. Algebraic Substitution: Quadratic Expression (Negative Variable)
# ----------------------------------------------------------------------
def arch_38_algebraic_substitution_quadratic_expression_negative_variable(rng: random.Random) -> Dict[str, Any]:
    x_val = -rng.randint(2, 5)
    a = rng.choice([2, 3, -1])
    b = rng.choice([-4, -2, 3, 5])
    c = rng.choice([-6, 7])
    ans = a * (x_val ** 2) + b * x_val + c

    b_str = f"+ {b}x" if b >= 0 else f"- {abs(b)}x"
    c_str = f"+ {c}" if c >= 0 else f"- {abs(c)}"

    prompt = (
        f"If **$x = {x_val}$**, calculate the numeric value of:\n\n"
        f"\\[ {a}x^2 {b_str} {c_str} \\]"
    )
    sol = (
        f"**Quadratic Substitution:**\n"
        f"1. Replace $x$ with $({x_val})$:\n"
        f"\\[ {a}({x_val})^2 + ({b})({x_val}) + ({c}) \\]\n"
        f"2. \\(({x_val})^2 = {x_val**2}\\)\n"
        f"3. \\({a}({x_val**2}) = {a * (x_val**2)}\\)\n"
        f"4. \\(({b})({x_val}) = {b * x_val}\\)\n"
        f"Combine: \\({a * (x_val**2)} + ({b * x_val}) + ({c}) = {ans}\\)."
    )
    return {
        "id": f"g9_int_subst_quad_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": str(ans),
        "sample_answer": str(ans),
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "subskill": "38_algebraic_substitution_quadratic_expression_negative_variable",
        "learning_objective_id": "math_g9_int_subst_quad",
        "hints": {
            "tier_1": f"Remember that ({x_val})^2 is POSITIVE {x_val**2}.",
            "tier_2": f"Calculate {a} * {x_val**2} + ({b} * {x_val}) + {c}.",
            "tier_3": str(ans),
        },
        "misconception_tags": ["squaring_negative_number_and_getting_negative_result"],
    }


# ----------------------------------------------------------------------
# 39. Algebraic Substitution: Cubic and Powers (Negative Variable)
# ----------------------------------------------------------------------
def arch_39_algebraic_substitution_cubic_and_powers_negative_variable(rng: random.Random) -> Dict[str, Any]:
    x_val = -2
    ans = (x_val ** 3) - 2 * (x_val ** 2) + 5 * x_val - 3  # -8 - 8 - 10 - 3 = -29

    prompt = (
        f"Evaluate the cubic polynomial for **$x = {x_val}$**:\n\n"
        f"\\[ x^3 - 2x^2 + 5x - 3 \\]"
    )
    sol = (
        f"**Cubic Substitution for x = {x_val}:**\n"
        f"1. \\(({x_val})^3 = {x_val**3}\\)\n"
        f"2. \\(-2({x_val})^2 = -2(4) = -8\\)\n"
        f"3. \\(5({x_val}) = -10\\)\n"
        f"4. \\(-3\\)\n"
        f"Sum: \\({x_val**3} - 8 - 10 - 3 = {ans}\\)."
    )
    return {
        "id": f"g9_int_subst_cube_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": str(ans),
        "sample_answer": str(ans),
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "subskill": "39_algebraic_substitution_cubic_and_powers_negative_variable",
        "learning_objective_id": "math_g9_int_subst_cube",
        "hints": {
            "tier_1": f"(-2)^3 = -8, but (-2)^2 = +4.",
            "tier_2": "Combine: -8 - 2(4) + 5(-2) - 3.",
            "tier_3": str(ans),
        },
        "misconception_tags": ["confusing_odd_and_even_powers_in_polynomial_substitution"],
    }


# ----------------------------------------------------------------------
# 40. Algebraic Substitution: Two Negative Variables
# ----------------------------------------------------------------------
def arch_40_algebraic_substitution_two_negative_variables(rng: random.Random) -> Dict[str, Any]:
    a = -rng.randint(2, 4)
    b = -rng.randint(2, 5)
    ans = 2 * (a ** 2) - 3 * a * b + b ** 2

    prompt = (
        f"Evaluate the algebraic expression when **$a = {a}$** and **$b = {b}$**:\n\n"
        f"\\[ 2a^2 - 3ab + b^2 \\]"
    )
    sol = (
        f"**Two-Variable Substitution:**\n"
        f"1. \\(2({a})^2 = 2({a**2}) = {2 * (a**2)}\\)\n"
        f"2. \\(-3({a})({b}) = -3({a * b}) = {-3 * (a * b)}\\)\n"
        f"3. \\(({b})^2 = {b**2}\\)\n"
        f"Total: \\({2 * (a**2)} + ({-3 * a * b}) + {b**2} = {ans}\\)."
    )
    return {
        "id": f"g9_int_subst_two_var_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": str(ans),
        "sample_answer": str(ans),
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "subskill": "40_algebraic_substitution_two_negative_variables",
        "learning_objective_id": "math_g9_int_subst_two_var",
        "hints": {
            "tier_1": f"Substitute a = ({a}) and b = ({b}).",
            "tier_2": f"Note that -3({a})({b}) = -3 * ({a*b}) = {-3*a*b}.",
            "tier_3": str(ans),
        },
        "misconception_tags": ["sign_error_in_middle_product_of_two_negatives_with_leading_minus"],
    }


# ----------------------------------------------------------------------
# 41. Solve Simple Linear Equation: Negative Coefficients
# ----------------------------------------------------------------------
def arch_41_solve_simple_linear_equation_negative_coefficients(rng: random.Random) -> Dict[str, Any]:
    x_sol = -rng.randint(2, 8)
    a = -rng.randint(3, 7)
    b = rng.randint(5, 20)
    c = a * x_sol + b

    prompt = (
        f"Solve the linear equation for $x$:\n\n"
        f"\\[ {a}x + {b} = {c} \\]"
    )
    sol = (
        f"**Solving Linear Equation:**\n"
        f"1. Subtract {b} from both sides:\n"
        f"\\[ {a}x = {c} - {b} \\]\n"
        f"\\[ {a}x = {c - b} \\]\n"
        f"2. Divide by {a}:\n"
        f"\\[ x = \\frac{{{c - b}}}{{{a}}} = {x_sol} \\]"
    )
    return {
        "id": f"g9_int_solve_eq1_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": str(x_sol),
        "sample_answer": str(x_sol),
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "subskill": "41_solve_simple_linear_equation_negative_coefficients",
        "learning_objective_id": "math_g9_int_solve_eq1",
        "hints": {
            "tier_1": f"Subtract {b} from both sides first.",
            "tier_2": f"Divide by {a}.",
            "tier_3": str(x_sol),
        },
        "misconception_tags": ["forgetting_to_divide_by_negative_sign"],
    }


# ----------------------------------------------------------------------
# 42. Solve Linear Equation: Negative Variables Both Sides
# ----------------------------------------------------------------------
def arch_42_solve_linear_equation_negative_variables_both_sides(rng: random.Random) -> Dict[str, Any]:
    x_sol = rng.choice([-5, -3, 2, 4])
    a = -5
    b = 12
    c = -2
    d = (a * x_sol + b) - (c * x_sol)  # so -5x + 12 = -2x + d

    prompt = (
        f"Solve for $x$:\n\n"
        f"\\[ -5x + {b} = -2x + ({d}) \\]"
    )
    sol = (
        f"**Isolating Variables:**\n"
        f"1. Collect $x$-terms on the left: \\(-5x + 2x = {d} - {b}\\)\n"
        f"2. Simplify: \\(-3x = {d - b}\\)\n"
        f"3. Divide by -3: \\(x = \\frac{{{d - b}}}{{-3}} = {x_sol}\\)."
    )
    return {
        "id": f"g9_int_solve_eq2_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": str(x_sol),
        "sample_answer": str(x_sol),
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "subskill": "42_solve_linear_equation_negative_variables_both_sides",
        "learning_objective_id": "math_g9_int_solve_eq2",
        "hints": {
            "tier_1": "Add 2x to both sides to group x terms.",
            "tier_2": f"-3x = {d - b}.",
            "tier_3": str(x_sol),
        },
        "misconception_tags": ["sign_error_when_transposing_terms_across_equals_sign"],
    }


# ----------------------------------------------------------------------
# 43. Integer Magic Square or Grid: Row / Column Sum
# ----------------------------------------------------------------------
def arch_43_integer_magic_square_or_grid_row_column_sum(rng: random.Random) -> Dict[str, Any]:
    target_sum = 0
    # 3x3 with target sum 0
    # row 1: -4, 3, 1
    # row 2: x, 0, -x
    a, b = -4, 3
    c = target_sum - (a + b)  # 1

    prompt = (
        f"In an integer magic square, every row, column, and diagonal sums to **{target_sum}**.\n\n"
        f"If the first two numbers in a row are **{a}** and **{b}**, determine the missing third integer in that row."
    )
    sol = (
        f"**Row Sum Equation:**\n"
        f"\\[ {a} + {b} + x = {target_sum} \\]\n"
        f"\\[ {a + b} + x = {target_sum} \\]\n"
        f"\\[ x = {target_sum} - ({a + b}) = {c} \\]"
    )
    return {
        "id": f"g9_int_magic_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": str(c),
        "sample_answer": str(c),
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "43_integer_magic_square_or_grid_row_column_sum",
        "learning_objective_id": "math_g9_int_magic",
        "hints": {
            "tier_1": f"Sum of row = {a} + {b} + x = {target_sum}.",
            "tier_2": f"x = {target_sum} - ({a + b}).",
            "tier_3": str(c),
        },
        "misconception_tags": ["subtraction_sign_error_when_solving_for_missing_grid_integer"],
    }


# ----------------------------------------------------------------------
# 44. Integer Consecutive Sum Problem: Negative Integers
# ----------------------------------------------------------------------
def arch_44_integer_consecutive_sum_problem_negative_integers(rng: random.Random) -> Dict[str, Any]:
    n1 = -rng.randint(8, 20)
    n2 = n1 + 1
    n3 = n1 + 2
    total_sum = n1 + n2 + n3

    prompt = (
        f"The sum of three consecutive integers is **{total_sum}**.\n\n"
        f"Find the three integers, showing an algebraic method."
    )
    sol = (
        f"**Algebraic Formulation:**\n"
        f"Let the three consecutive integers be $x$, $x + 1$, and $x + 2$.\n"
        f"\\[ x + (x + 1) + (x + 2) = {total_sum} \\]\n"
        f"\\[ 3x + 3 = {total_sum} \\]\n"
        f"\\[ 3x = {total_sum - 3} \\]\n"
        f"\\[ x = {n1} \\]\n\n"
        f"The three consecutive integers are **{n1}, {n2}, and {n3}**."
    )
    ans = f"{n1}, {n2}, {n3}"
    return {
        "id": f"g9_int_consec_{rng.randint(100000, 999999)}",
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
        "subskill": "44_integer_consecutive_sum_problem_negative_integers",
        "learning_objective_id": "math_g9_int_consec",
        "hints": {
            "tier_1": "Consecutive integers differ by 1: x, x+1, x+2.",
            "tier_2": f"3x + 3 = {total_sum}.",
            "tier_3": ans,
        },
        "misconception_tags": ["assuming_consecutive_negatives_are_x_minus_one_without_checking_order"],
    }


# ----------------------------------------------------------------------
# 45. Submarine Depth and Ascent Context Problem
# ----------------------------------------------------------------------
def arch_45_submarine_depth_and_ascent_context_problem(rng: random.Random) -> Dict[str, Any]:
    d_start = -rng.choice([150, 200, 250, 300])
    descent = rng.choice([50, 75, 100])
    ascent = rng.choice([80, 120, 150])
    final_depth = d_start - descent + ascent

    prompt = (
        f"A naval submarine is cruising at a depth of **{abs(d_start)} m below sea level** ($-{abs(d_start)}$ m).\n"
        f"It then descends a further **{descent} m**, before ascending **{ascent} m**.\n\n"
        f"Write down an integer calculation and determine the submarine's **final depth** below sea level."
    )
    sol = (
        f"**Submarine Depth Calculation:**\n"
        f"1. Initial depth: \\({d_start}\\) m.\n"
        f"2. Descending 50 m: \\({d_start} - {descent} = {d_start - descent}\\) m.\n"
        f"3. Ascending 80 m: \\({d_start - descent} + {ascent} = {final_depth}\\) m.\n"
        f"The submarine is at a depth of **{abs(final_depth)} m below sea level**."
    )
    ans = f"{abs(final_depth)} m below sea level (or {final_depth} m)"
    return {
        "id": f"g9_int_sub_depth_{rng.randint(100000, 999999)}",
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
        "subskill": "45_submarine_depth_and_ascent_context_problem",
        "learning_objective_id": "math_g9_int_sub_depth",
        "hints": {
            "tier_1": "Descending means subtracting; ascending means adding.",
            "tier_2": f"{d_start} - {descent} + {ascent} = {final_depth}.",
            "tier_3": ans,
        },
        "misconception_tags": ["adding_when_descending"],
    }


# ----------------------------------------------------------------------
# 46. Mine Shaft Elevation Lift Movement Problem
# ----------------------------------------------------------------------
def arch_46_mine_shaft_elevation_lift_movement_problem(rng: random.Random) -> Dict[str, Any]:
    level1 = -rng.choice([400, 600, 800])
    level2 = -rng.choice([150, 200, 300])
    diff = level2 - level1  # positive ascent

    prompt = (
        f"A gold mine lift cage moves underground between Level 4 at **{level1} m** and Level 1 at **{level2} m** "
        f"(both levels measured relative to surface level at 0 m).\n\n"
        f"1. Did the cage move up or down from Level 4 to Level 1?\n"
        f"2. Calculate the distance and direction of the movement as a signed integer."
    )
    sol = (
        f"**Lift Movement Calculation:**\n"
        f"Movement = Final position - Initial position:\n"
        f"\\[ \\Delta y = ({level2}) - ({level1}) = {level2} + {abs(level1)} = +{diff} \\text{{ m}} \\]\n"
        f"Conclusion: The cage moved **upwards by {diff} m** (+{diff} m)."
    )
    ans = f"1. Upwards; 2. +{diff} m (or {diff} m)"
    return {
        "id": f"g9_int_mine_lift_{rng.randint(100000, 999999)}",
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
        "subskill": "46_mine_shaft_elevation_lift_movement_problem",
        "learning_objective_id": "math_g9_int_mine_lift",
        "hints": {
            "tier_1": f"-{abs(level2)} is closer to the surface (higher) than -{abs(level1)}.",
            "tier_2": f"Change = final - initial = ({level2}) - ({level1}).",
            "tier_3": ans,
        },
        "misconception_tags": ["thinking_negative_eight_hundred_is_higher_than_negative_two_hundred"],
    }


# ----------------------------------------------------------------------
# 47. Error Analysis: Diagnosing Double Negative Subtraction Error
# ----------------------------------------------------------------------
def arch_47_error_analysis_diagnosing_double_negative_subtraction_error(rng: random.Random) -> Dict[str, Any]:
    a = 15
    b = 8
    flawed = a - b   # 7 (ignored negative on b)
    correct = a + b  # 23

    prompt = (
        f"A learner was asked to calculate **{a} - (-{b})**.\n"
        f"The learner answered **{flawed}**, claiming that subtraction always reduces a number.\n\n"
        f"1. Explain why the learner's reasoning is incorrect.\n"
        f"2. Provide the correct calculation and answer."
    )
    sol = (
        f"**Error Analysis:**\n"
        f"1. Explanation: Subtracting a negative number is equivalent to adding its positive additive inverse. "
        f"Subtracting debt increases wealth ($a - (-b) = a + b$).\n"
        f"2. Correct working:\n"
        f"\\[ {a} - (-{b}) = {a} + {b} = {correct} \\]"
    )
    ans = f"Subtracting negative adds: {a} + {b} = {correct}"
    return {
        "id": f"g9_err_double_neg_{rng.randint(100000, 999999)}",
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
        "subskill": "47_error_analysis_diagnosing_double_negative_subtraction_error",
        "learning_objective_id": "math_g9_err_double_neg",
        "hints": {
            "tier_1": "Double negative rule: -(-b) = +b.",
            "tier_2": f"{a} + {b} = {correct}.",
            "tier_3": ans,
        },
        "misconception_tags": ["belief_that_subtraction_always_makes_a_number_smaller"],
    }


# ----------------------------------------------------------------------
# 48. Error Analysis: Diagnosing Power Bracket Sign Error
# ----------------------------------------------------------------------
def arch_48_error_analysis_diagnosing_power_bracket_sign_error(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A learner wrote in an exam test:\n"
        f"\\[ -4^2 = 16 \\]\n\n"
        f"1. Point out the error in the learner's understanding.\n"
        f"2. State the correct value of **$-4^2$** and **$(-4)^2$**."
    )
    sol = (
        f"**Error Diagnosis:**\n"
        f"1. Error: Without brackets, the power applies only to 4, not the negative sign ($-4^2 = -(4 \\times 4) = -16$).\n"
        f"2. Values: **$-4^2 = -16$** and **$(-4)^2 = +16$**."
    )
    ans = "-4^2 = -16; (-4)^2 = 16"
    return {
        "id": f"g9_err_pow_sign_{rng.randint(100000, 999999)}",
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
        "subskill": "48_error_analysis_diagnosing_power_bracket_sign_error",
        "learning_objective_id": "math_g9_err_pow_sign",
        "hints": {
            "tier_1": "The negative sign is only squared if it is enclosed inside brackets.",
            "tier_2": "-4^2 = -(16) = -16.",
            "tier_3": ans,
        },
        "misconception_tags": ["treating_negative_sign_as_part_of_base_without_brackets"],
    }


# ----------------------------------------------------------------------
# 49. Error Analysis: BODMAS Addition Before Multiplication Error
# ----------------------------------------------------------------------
def arch_49_error_analysis_diagnosing_bodmas_addition_before_multiplication_error(rng: random.Random) -> Dict[str, Any]:
    # e.g., 8 - 3 * (-4) -> learner does (8 - 3) * (-4) = 5 * (-4) = -20
    # correct is 8 - (-12) = 20
    flawed = (8 - 3) * (-4)
    correct = 8 - (3 * -4)

    prompt = (
        f"A learner evaluated **$8 - 3 \\times (-4)$** as follows:\n"
        f"\\[ 8 - 3 \\times (-4) = 5 \\times (-4) = -20 \\]\n\n"
        f"1. Explain what error of precedence the learner made.\n"
        f"2. Calculate the correct answer using BODMAS."
    )
    sol = (
        f"**Precedence Diagnosis:**\n"
        f"1. Error: The learner subtracted $8 - 3 = 5$ before multiplying. "
        f"Under BODMAS rules, multiplication must be executed before subtraction.\n"
        f"2. Correct working:\n"
        f"\\[ 8 - [3 \\times (-4)] = 8 - (-12) = 8 + 12 = {correct} \\]"
    )
    ans = f"Subtracted before multiplying; correct = {correct}"
    return {
        "id": f"g9_err_bodmas_{rng.randint(100000, 999999)}",
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
        "subskill": "49_error_analysis_diagnosing_bodmas_addition_before_multiplication_error",
        "learning_objective_id": "math_g9_err_bodmas",
        "hints": {
            "tier_1": "Multiplication has higher priority than subtraction.",
            "tier_2": f"3 * (-4) = -12, so 8 - (-12) = {correct}.",
            "tier_3": ans,
        },
        "misconception_tags": ["executing_addition_or_subtraction_from_left_to_right_ignoring_multiplication"],
    }


# ----------------------------------------------------------------------
# 50. Compound Multi-Step Integer Expression Evaluation
# ----------------------------------------------------------------------
def arch_50_compound_multi_step_integer_expression_evaluation(rng: random.Random) -> Dict[str, Any]:
    # e.g., [ (-3)^2 - (-2)^3 ] / [ -5 - (-2) ] = [ 9 - (-8) ] / [ -5 + 2 ] = 17 / -3 (need clean integer)
    # Let's craft clean integer:
    # num: (-2)^3 - (-4) = -8 + 4 = -4
    # den: -2
    # ans = 2
    p_cube = -8  # (-2)^3
    sub_term = -rng.choice([4, 6, 8])
    num = p_cube - sub_term
    den = rng.choice([-2, 2])
    ans = num // den

    prompt = (
        f"Evaluate the comprehensive multi-operation integer expression:\n\n"
        f"\\[ \\frac{{(-2)^3 - ({sub_term})}}{{{den}}} \\]"
    )
    sol = (
        f"**Multi-step Evaluation:**\n"
        f"1. Power: \\((-2)^3 = -8\\).\n"
        f"2. Numerator subtraction: \\(-8 - ({sub_term}) = -8 + {abs(sub_term)} = {num}\\).\n"
        f"3. Division: \\(\\frac{{{num}}}{{{den}}} = {ans}\\)."
    )
    return {
        "id": f"g9_int_compound_challenge_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": str(ans),
        "sample_answer": str(ans),
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "subskill": "50_compound_multi_step_integer_expression_evaluation",
        "learning_objective_id": "math_g9_int_compound_challenge",
        "hints": {
            "tier_1": "Evaluate (-2)^3 = -8 first.",
            "tier_2": f"Numerator is -8 - ({sub_term}) = {num}.",
            "tier_3": str(ans),
        },
        "misconception_tags": ["sign_error_in_compound_numerator_division"],
    }
