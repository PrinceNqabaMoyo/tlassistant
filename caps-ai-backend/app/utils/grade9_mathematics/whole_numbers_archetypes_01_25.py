"""Grade 9 Mathematics - Whole Numbers Archetypes 01 to 25.
Grounded in curriculum_docs_auto/Mathematics_Gr9/Term 1/01. Whole numbers.md.
Covers:
  - Number systems classification (Real, Rational, Irrational, Non-real, Undefined).
  - Estimating surds between consecutive integers.
  - Converting recurring decimals to common fractions.
  - Properties of operations (Commutative, Associative, Distributive, Identities, Inverses).
  - Prime factorisation in exponential form.
  - HCF and LCM for 2 and 3 numbers and practical word problems.
  - Ratio simplification, unit conversion, dividing in ratios (2-part and 3-part).
  - Direct proportion (constant ratio) and Inverse proportion (constant product).
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional, Tuple

from .whole_numbers_svg import (
    draw_number_system_hierarchy_svg,
    draw_surd_number_line_svg,
    draw_factor_tree_svg,
)


def _fmt_dec(val: float, decimals: int = 2) -> str:
    s = f"{val:.{decimals}f}"
    return s.replace(".", "{,}")


# ----------------------------------------------------------------------
# 01. Classify Numbers: Real, Rational, Irrational, Non-Real
# ----------------------------------------------------------------------
def arch_01_classify_numbers_real_rational_irrational_non_real(rng: random.Random) -> Dict[str, Any]:
    cases = [
        (r"\sqrt{36}", "Rational", "Rational (since $\\sqrt{36} = 6 = \\frac{6}{1} \\in \\mathbb{Q}$)"),
        (r"\sqrt{11}", "Irrational", "Irrational (since 11 is not a perfect square; non-terminating, non-recurring decimal)"),
        (r"-7", "Rational", "Rational (integer $-7 = \\frac{-7}{1} \\in \\mathbb{Q}$)"),
        (r"0{,}45", "Rational", "Rational (terminating decimal $0{,}45 = \\frac{45}{100} = \\frac{9}{20} \\in \\mathbb{Q}$)"),
        (r"\pi", "Irrational", "Irrational (ratio of circle circumference to diameter; non-terminating, non-recurring)"),
        (r"\sqrt{\frac{4}{9}}", "Rational", "Rational (since $\\sqrt{\\frac{4}{9}} = \\frac{2}{3} \\in \\mathbb{Q}$)"),
        (r"\sqrt[3]{-8}", "Rational", "Rational (since $(-2)^3 = -8$, so $\\sqrt[3]{-8} = -2 \\in \\mathbb{Q}$)"),
    ]
    expr, ans_type, reason = rng.choice(cases)
    svg = draw_number_system_hierarchy_svg(highlight_set=ans_type, seed=rng.randint(100, 999999))

    prompt = (
        f"Consider the following real number:\n\n"
        f"\\[ x = {expr} \\]\n\n"
        f"Classify $x$ as either **Rational** ($\\mathbb{{Q}}$) or **Irrational** ($\\mathbb{{Q}}'$), and justify your answer."
    )
    sol = (
        f"**Classification of \\({expr}\\):**\n"
        f"1. Evaluate or inspect the form: {reason}.\n"
        f"2. Conclusion: $x$ is **{ans_type}**."
    )
    return {
        "id": f"g9_num_classify_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans_type,
        "sample_answer": ans_type,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "01_classify_numbers_real_rational_irrational_non_real",
        "learning_objective_id": "math_g9_num_classify",
        "hints": {
            "tier_1": "Rational numbers can be written as a/b (a, b integers, b != 0).",
            "tier_2": "Roots of non-perfect squares like sqrt(11) are irrational.",
            "tier_3": ans_type,
        },
        "misconception_tags": ["confusing_irrational_with_non_real"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 02. Identify Non-Real: Even Roots of Negative Numbers
# ----------------------------------------------------------------------
def arch_02_identify_non_real_even_roots_of_negative_numbers(rng: random.Random) -> Dict[str, Any]:
    neg_val = rng.choice([-4, -9, -16, -25, -49, -100])
    pos_val = abs(neg_val)

    prompt = (
        f"Determine whether the following expression represents a **Real** number or a **Non-Real** number:\n\n"
        f"\\[ \\sqrt{{{neg_val}}} \\]\n\n"
        f"Explain why in terms of square roots."
    )
    sol = (
        f"**Analysis:**\n"
        f"The square of any real number is always non-negative ($x^2 \\ge 0$ for all $x \\in \\mathbb{{R}}$).\n"
        f"No real number squared produces a negative result: there is no $x \\in \\mathbb{{R}}$ such that $x^2 = {neg_val}$.\n"
        f"Therefore, $\\sqrt{{{neg_val}}}$ is **Non-Real** (or imaginary)."
    )
    ans = "Non-Real"
    return {
        "id": f"g9_non_real_{rng.randint(100000, 999999)}",
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
        "subskill": "02_identify_non_real_even_roots_of_negative_numbers",
        "learning_objective_id": "math_g9_non_real",
        "hints": {
            "tier_1": "Can you multiply any real number by itself to get a negative answer?",
            "tier_2": "Even roots of negative numbers are not real numbers.",
            "tier_3": "Non-Real.",
        },
        "misconception_tags": ["thinking_sqrt_negative_is_negative_real_number"],
    }


# ----------------------------------------------------------------------
# 03. Identify Undefined: Division by Zero
# ----------------------------------------------------------------------
def arch_03_identify_undefined_division_by_zero(rng: random.Random) -> Dict[str, Any]:
    num = rng.choice([7, 12, 25, 48, -15])
    k = rng.choice([2, 3, 5])
    denom_expr = f"{k} - {k}"

    prompt = (
        f"Evaluate or classify the mathematical value of the expression:\n\n"
        f"\\[ \\frac{{{num}}}{{{denom_expr}}} \\]\n\n"
        f"State whether this expression is **Zero**, **Non-Real**, or **Undefined**."
    )
    sol = (
        f"**Analysis:**\n"
        f"1. Simplify the denominator: ${denom_expr} = 0$.\n"
        f"2. The expression becomes $\\frac{{{num}}}{{0}}$.\n"
        f"3. Division by zero is mathematically meaningless (no number multiplied by 0 gives {num}).\n"
        f"Therefore, the expression is **Undefined**."
    )
    ans = "Undefined"
    return {
        "id": f"g9_undefined_{rng.randint(100000, 999999)}",
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
        "subskill": "03_identify_undefined_division_by_zero",
        "learning_objective_id": "math_g9_undefined",
        "hints": {
            "tier_1": f"Calculate the denominator: {k} - {k} = 0.",
            "tier_2": "What happens when a non-zero number is divided by zero?",
            "tier_3": "Undefined.",
        },
        "misconception_tags": ["confusing_undefined_division_by_zero_with_zero"],
    }


# ----------------------------------------------------------------------
# 04. Determine Between Which Two Integers Surd Lies
# ----------------------------------------------------------------------
def arch_04_determine_between_which_two_integers_surd_lies(rng: random.Random) -> Dict[str, Any]:
    # Non-perfect square between 2 and 99
    base = rng.choice([2, 3, 4, 5, 6, 7, 8])
    offset = rng.choice([1, 2, 3])
    n = base ** 2 + offset
    if n >= (base + 1) ** 2:
        n = (base + 1) ** 2 - 1

    lower_int = base
    upper_int = base + 1
    val = math.sqrt(n)
    surd_label = f"√{n}"

    svg = draw_surd_number_line_svg(
        val=val,
        surd_label=surd_label,
        lower_int=lower_int,
        upper_int=upper_int,
        seed=rng.randint(100, 999999),
    )

    prompt = (
        f"Without using a calculator:\n\n"
        f"1. Determine the two consecutive integers between which **$\\sqrt{{{n}}}$** lies.\n"
        f"2. Show your reasoning using consecutive perfect squares."
    )
    sol = (
        f"**Step 1: Identify perfect squares flanking {n}:**\n"
        f"\\[ {lower_int}^2 = {lower_int**2} \\quad \\text{{and}} \\quad {upper_int}^2 = {upper_int**2} \\]\n"
        f"Since ${lower_int**2} < {n} < {upper_int**2}$:\n"
        f"\\[ \\sqrt{{{lower_int**2}}} < \\sqrt{{{n}}} < \\sqrt{{{upper_int**2}}} \\]\n"
        f"\\[ {lower_int} < \\sqrt{{{n}}} < {upper_int} \\]\n\n"
        f"Therefore, $\\sqrt{{{n}}}$ lies between **{lower_int} and {upper_int}**."
    )
    ans = f"{lower_int} and {upper_int}"
    return {
        "id": f"g9_surd_integers_{rng.randint(100000, 999999)}",
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
        "subskill": "04_determine_between_which_two_integers_surd_lies",
        "learning_objective_id": "math_g9_surd_integers",
        "hints": {
            "tier_1": f"Find the closest perfect squares below and above {n}.",
            "tier_2": f"{lower_int}^2 = {lower_int**2} and {upper_int}^2 = {upper_int**2}.",
            "tier_3": f"Between {lower_int} and {upper_int}.",
        },
        "misconception_tags": ["halving_the_number_instead_of_square_root"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 05. Convert Recurring Decimal to Common Fraction (Single Digit)
# ----------------------------------------------------------------------
def arch_05_convert_recurring_decimal_to_common_fraction_single_digit(rng: random.Random) -> Dict[str, Any]:
    d = rng.choice([1, 2, 4, 5, 7, 8])  # avoid 3, 6, 9 for gcd simplification variety
    gcd = math.gcd(d, 9)
    num = d // gcd
    den = 9 // gcd

    prompt = (
        f"Convert the recurring decimal **$0{{,}}\\dot{{{d}}}$** ($0{{,}}{d}{d}{d}\\dots$) to a common fraction in simplest form, "
        f"showing all algebraic steps using $x$."
    )
    sol = (
        f"**Algebraic Method:**\n"
        f"Let \\( x = 0{{,}}\\dot{{{d}}} = 0{{,}}{d}{d}{d}\\dots \\quad \\text{{--- (1)}} \\)\n\n"
        f"Multiply equation (1) by 10:\n"
        f"\\[ 10x = {d}{{,}}\\dot{{{d}}} = {d}{{,}}{d}{d}{d}\\dots \\quad \\text{{--- (2)}} \\]\n\n"
        f"Subtract (1) from (2):\n"
        f"\\[ 10x - x = {d}{{,}}\\dot{{{d}}} - 0{{,}}\\dot{{{d}}} \\]\n"
        f"\\[ 9x = {d} \\]\n"
        f"\\[ x = \\frac{{{d}}}{{9}} " + (f"= \\frac{{{num}}}{{{den}}}" if gcd > 1 else "") + f" \\]"
    )
    ans = f"{num}/{den}"
    return {
        "id": f"g9_rec_dec_single_{rng.randint(100000, 999999)}",
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
        "subskill": "05_convert_recurring_decimal_to_common_fraction_single_digit",
        "learning_objective_id": "math_g9_rec_dec_single",
        "hints": {
            "tier_1": f"Let x = 0.{d}{d}{d}... and multiply by 10.",
            "tier_2": f"10x - x = 9x = {d}.",
            "tier_3": f"{num}/{den}.",
        },
        "misconception_tags": ["dividing_by_10_instead_of_9_for_recurring_decimals"],
    }


# ----------------------------------------------------------------------
# 06. Convert Recurring Decimal to Common Fraction (Two Digits)
# ----------------------------------------------------------------------
def arch_06_convert_recurring_decimal_to_common_fraction_two_digits(rng: random.Random) -> Dict[str, Any]:
    val = rng.choice([15, 27, 36, 45, 54, 72, 81])
    gcd = math.gcd(val, 99)
    num = val // gcd
    den = 99 // gcd

    prompt = (
        f"Convert the recurring decimal **$0{{,}}\\dot{{{val // 10}}}\\dot{{{val % 10}}}$** ($0{{,}}{val}{val}{val}\\dots$) "
        f"to a common fraction in simplest form, showing all algebraic working."
    )
    sol = (
        f"**Algebraic Method:**\n"
        f"Let \\( x = 0{{,}}\\dot{{{val // 10}}}\\dot{{{val % 10}}} = 0{{,}}{val}{val}{val}\\dots \\quad \\text{{--- (1)}} \\)\n\n"
        f"Multiply equation (1) by 100:\n"
        f"\\[ 100x = {val}{{,}}{val}{val}\\dots \\quad \\text{{--- (2)}} \\]\n\n"
        f"Subtract (1) from (2):\n"
        f"\\[ 100x - x = {val} \\]\n"
        f"\\[ 99x = {val} \\]\n"
        f"\\[ x = \\frac{{{val}}}{{99}} = \\frac{{{num}}}{{{den}}} \\]"
    )
    ans = f"{num}/{den}"
    return {
        "id": f"g9_rec_dec_double_{rng.randint(100000, 999999)}",
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
        "subskill": "06_convert_recurring_decimal_to_common_fraction_two_digits",
        "learning_objective_id": "math_g9_rec_dec_double",
        "hints": {
            "tier_1": "Multiply by 100 because 2 digits repeat.",
            "tier_2": f"100x - x = 99x = {val}.",
            "tier_3": f"{num}/{den}.",
        },
        "misconception_tags": ["dividing_by_100_instead_of_99_for_double_repeating_decimals"],
    }


# ----------------------------------------------------------------------
# 07. Properties of Operations: Commutative and Associative
# ----------------------------------------------------------------------
def arch_07_properties_of_operations_commutative_and_associative(rng: random.Random) -> Dict[str, Any]:
    choice = rng.choice(["commutative_add", "commutative_mult", "associative_add", "associative_mult"])
    if choice == "commutative_add":
        a, b = rng.randint(12, 45), rng.randint(15, 60)
        statement = f"{a} + {b} = {b} + {a}"
        prop = "Commutative property of addition"
    elif choice == "commutative_mult":
        a, b = rng.randint(4, 12), rng.randint(13, 25)
        statement = f"{a} \\times {b} = {b} \\times {a}"
        prop = "Commutative property of multiplication"
    elif choice == "associative_add":
        a, b, c = rng.randint(5, 20), rng.randint(5, 20), rng.randint(5, 20)
        statement = f"({a} + {b}) + {c} = {a} + ({b} + {c})"
        prop = "Associative property of addition"
    else:
        a, b, c = rng.randint(2, 6), rng.randint(3, 7), rng.randint(4, 9)
        statement = f"({a} \\times {b}) \\times {c} = {a} \\times ({b} \\times {c})"
        prop = "Associative property of multiplication"

    prompt = (
        f"Name the mathematical property of operations demonstrated by the following statement:\n\n"
        f"\\[ {statement} \\]"
    )
    sol = (
        f"**Property Identification:**\n"
        f"The equation demonstrates the **{prop}**."
    )
    return {
        "id": f"g9_prop_comm_assoc_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": prop,
        "sample_answer": prop,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "subskill": "07_properties_of_operations_commutative_and_associative",
        "learning_objective_id": "math_g9_prop_comm_assoc",
        "hints": {
            "tier_1": "Commutative means changing the order (a + b = b + a).",
            "tier_2": "Associative means changing the grouping ((a + b) + c = a + (b + c)).",
            "tier_3": prop,
        },
        "misconception_tags": ["confusing_commutative_with_associative_property"],
    }


# ----------------------------------------------------------------------
# 08. Properties of Operations: Distributive Over Addition
# ----------------------------------------------------------------------
def arch_08_properties_of_operations_distributive_over_addition(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(4, 9)
    b = rng.randint(10, 30)
    c = rng.randint(2, 8)
    res = a * (b + c)
    step1 = a * b
    step2 = a * c

    prompt = (
        f"Use the **distributive property of multiplication over addition** to evaluate without a calculator:\n\n"
        f"\\[ {a} \\times ({b} + {c}) \\]\n\n"
        f"Show both expanded terms and the final calculated sum."
    )
    sol = (
        f"**Distributive Calculation:**\n"
        f"\\[ {a} \\times ({b} + {c}) = ({a} \\times {b}) + ({a} \\times {c}) \\]\n"
        f"\\[ = {step1} + {step2} = {res} \\]"
    )
    ans = str(res)
    return {
        "id": f"g9_prop_distrib_{rng.randint(100000, 999999)}",
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
        "subskill": "08_properties_of_operations_distributive_over_addition",
        "learning_objective_id": "math_g9_prop_distrib",
        "hints": {
            "tier_1": f"Multiply {a} by {b}, and {a} by {c}.",
            "tier_2": f"{step1} + {step2}.",
            "tier_3": ans,
        },
        "misconception_tags": ["multiplying_only_first_term_in_brackets"],
    }


# ----------------------------------------------------------------------
# 09. Identity Elements: Additive Zero and Multiplicative One
# ----------------------------------------------------------------------
def arch_09_identity_elements_additive_zero_and_multiplicative_one(rng: random.Random) -> Dict[str, Any]:
    num = rng.choice([47, -83, 125, -240])

    prompt = (
        f"Answer the following regarding numerical identity elements:\n\n"
        f"1. State the **additive identity element** and calculate ${num} + (\\text{{additive identity}})$.\n"
        f"2. State the **multiplicative identity element** and calculate ${num} \\times (\\text{{multiplicative identity}})$."
    )
    sol = (
        f"**Identity Elements:**\n"
        f"1. The additive identity is **0**, because adding 0 leaves the number unchanged: ${num} + 0 = {num}$.\n"
        f"2. The multiplicative identity is **1**, because multiplying by 1 leaves the number unchanged: ${num} \\times 1 = {num}$."
    )
    ans = f"1. 0, {num}; 2. 1, {num}"
    return {
        "id": f"g9_identity_elements_{rng.randint(100000, 999999)}",
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
        "subskill": "09_identity_elements_additive_zero_and_multiplicative_one",
        "learning_objective_id": "math_g9_identity_elements",
        "hints": {
            "tier_1": "What number added to x gives x?",
            "tier_2": "What number multiplied by x gives x?",
            "tier_3": ans,
        },
        "misconception_tags": ["confusing_additive_identity_zero_with_multiplicative_identity_one"],
    }


# ----------------------------------------------------------------------
# 10. Inverses: Additive Inverse and Reciprocal
# ----------------------------------------------------------------------
def arch_10_inverses_additive_inverse_and_reciprocal(rng: random.Random) -> Dict[str, Any]:
    num = rng.choice([3, 5, 7, 8, -4, -6])
    add_inv = -num
    recip = f"1/{num}" if num > 0 else f"-1/{abs(num)}"
    recip_latex = f"\\frac{{1}}{{{num}}}" if num > 0 else f"-\\frac{{1}}{{{abs(num)}}}"

    prompt = (
        f"For the integer **${num}$**:\n\n"
        f"1. Write down its **additive inverse**.\n"
        f"2. Write down its **multiplicative inverse** (reciprocal)."
    )
    sol = (
        f"**Inverses for {num}:**\n"
        f"1. Additive inverse: The number that adds to {num} to give 0 is **{add_inv}** (${num} + ({add_inv}) = 0$).\n"
        f"2. Multiplicative inverse (reciprocal): The number that multiplies by {num} to give 1 is **${recip_latex}$** (${num} \\times \\left({recip_latex}\\right) = 1$)."
    )
    ans = f"1. {add_inv}; 2. {recip}"
    return {
        "id": f"g9_inverses_{rng.randint(100000, 999999)}",
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
        "subskill": "10_inverses_additive_inverse_and_reciprocal",
        "learning_objective_id": "math_g9_inverses",
        "hints": {
            "tier_1": "Additive inverse changes the sign: x -> -x.",
            "tier_2": "Multiplicative inverse flips the fraction: x -> 1/x.",
            "tier_3": ans,
        },
        "misconception_tags": ["changing_sign_when_finding_reciprocal"],
    }


# ----------------------------------------------------------------------
# 11. Prime Factorisation in Exponential Form
# ----------------------------------------------------------------------
def arch_11_prime_factorisation_written_in_exponential_form(rng: random.Random) -> Dict[str, Any]:
    p2 = rng.choice([2, 3])
    p3 = rng.choice([1, 2])
    p5 = rng.choice([1, 2])
    n = (2 ** p2) * (3 ** p3) * (5 ** p5)

    svg = draw_factor_tree_svg(n, [(2, n // 2)], seed=rng.randint(100, 999999))
    ans_latex = f"2^{{{p2}}} \\times 3^{{{p3}}} \\times 5^{{{p5}}}"

    prompt = (
        f"Express the composite number **{n}** as a product of its prime factors in exponential form, "
        f"using continuous ladder division or a factor tree."
    )
    sol = (
        f"**Prime Factorisation of {n}:**\n"
        f"Dividing {n} consecutively by prime numbers 2, 3, 5:\n"
        f"\\[ {n} = {ans_latex} \\]"
    )
    ans = f"2^{p2} * 3^{p3} * 5^{p5}"
    return {
        "id": f"g9_prime_fact_{rng.randint(100000, 999999)}",
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
        "subskill": "11_prime_factorisation_written_in_exponential_form",
        "learning_objective_id": "math_g9_prime_fact",
        "hints": {
            "tier_1": "Divide by the smallest prime number (2, 3, 5...) repeatedly.",
            "tier_2": f"Count how many 2s, 3s, and 5s divide into {n}.",
            "tier_3": ans,
        },
        "misconception_tags": ["leaving_non_prime_factors_like_4_or_6_in_factorisation"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 12. HCF Using Prime Factors: Two Numbers
# ----------------------------------------------------------------------
def arch_12_highest_common_factor_hcf_using_prime_factors_two_numbers(rng: random.Random) -> Dict[str, Any]:
    common = rng.choice([6, 12, 18, 24])
    m1 = rng.choice([2, 3, 5])
    m2 = rng.choice([7, 11])
    n1 = common * m1
    n2 = common * m2
    hcf = math.gcd(n1, n2)

    prompt = (
        f"Find the **Highest Common Factor (HCF)** of **{n1}** and **{n2}** by first expressing each number "
        f"as a product of prime factors."
    )
    sol = (
        f"**HCF Calculation:**\n"
        f"1. Express as prime factors:\n"
        f"   - \\({n1}\\)\n"
        f"   - \\({n2}\\)\n"
        f"2. Take the lowest power of each common prime factor:\n"
        f"\\[ \\text{{HCF}} = {hcf} \\]"
    )
    ans = str(hcf)
    return {
        "id": f"g9_hcf_two_{rng.randint(100000, 999999)}",
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
        "subskill": "12_highest_common_factor_hcf_using_prime_factors_two_numbers",
        "learning_objective_id": "math_g9_hcf_two",
        "hints": {
            "tier_1": "Break both numbers into prime factors.",
            "tier_2": "Multiply together only the prime factors shared by both numbers.",
            "tier_3": ans,
        },
        "misconception_tags": ["taking_highest_power_instead_of_lowest_power_for_hcf"],
    }


# ----------------------------------------------------------------------
# 13. HCF Using Prime Factors: Three Numbers
# ----------------------------------------------------------------------
def arch_13_highest_common_factor_hcf_using_prime_factors_three_numbers(rng: random.Random) -> Dict[str, Any]:
    hcf = rng.choice([6, 8, 12])
    n1 = hcf * 2
    n2 = hcf * 3
    n3 = hcf * 5

    prompt = (
        f"Determine the **Highest Common Factor (HCF)** of the three numbers **{n1}**, **{n2}**, and **{n3}** "
        f"using prime factorisation."
    )
    sol = (
        f"**HCF of Three Numbers:**\n"
        f"- Factors of {n1}, {n2}, {n3}.\n"
        f"- The common factors shared across all three numbers yield:\n"
        f"\\[ \\text{{HCF}}({n1}; {n2}; {n3}) = {hcf} \\]"
    )
    ans = str(hcf)
    return {
        "id": f"g9_hcf_three_{rng.randint(100000, 999999)}",
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
        "subskill": "13_highest_common_factor_hcf_using_prime_factors_three_numbers",
        "learning_objective_id": "math_g9_hcf_three",
        "hints": {
            "tier_1": "Find the prime factors of all three numbers.",
            "tier_2": "Select the lowest power of prime factors common to all three.",
            "tier_3": ans,
        },
        "misconception_tags": ["taking_factors_shared_by_only_two_numbers_in_hcf"],
    }


# ----------------------------------------------------------------------
# 14. LCM Using Prime Factors: Two Numbers
# ----------------------------------------------------------------------
def arch_14_lowest_common_multiple_lcm_using_prime_factors_two_numbers(rng: random.Random) -> Dict[str, Any]:
    n1 = rng.choice([12, 18, 20, 24])
    n2 = rng.choice([15, 28, 30, 36])
    hcf = math.gcd(n1, n2)
    lcm = (n1 * n2) // hcf

    prompt = (
        f"Determine the **Lowest Common Multiple (LCM)** of **{n1}** and **{n2}** using prime factorisation."
    )
    sol = (
        f"**LCM Calculation:**\n"
        f"1. Write prime factorisations:\n"
        f"2. Take the highest power of every prime factor occurring in either number:\n"
        f"\\[ \\text{{LCM}} = \\frac{{{n1} \\times {n2}}}{{\\text{{HCF}}}} = {lcm} \\]"
    )
    ans = str(lcm)
    return {
        "id": f"g9_lcm_two_{rng.randint(100000, 999999)}",
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
        "subskill": "14_lowest_common_multiple_lcm_using_prime_factors_two_numbers",
        "learning_objective_id": "math_g9_lcm_two",
        "hints": {
            "tier_1": "For LCM, take the highest power of each prime factor.",
            "tier_2": f"Formula: LCM = (a * b) / HCF.",
            "tier_3": ans,
        },
        "misconception_tags": ["confusing_lcm_with_hcf"],
    }


# ----------------------------------------------------------------------
# 15. LCM Using Prime Factors: Three Numbers
# ----------------------------------------------------------------------
def arch_15_lowest_common_multiple_lcm_using_prime_factors_three_numbers(rng: random.Random) -> Dict[str, Any]:
    n1, n2, n3 = rng.choice([(6, 8, 12), (8, 10, 15), (9, 12, 18), (12, 15, 20)])
    lcm = math.lcm(n1, n2, n3)

    prompt = (
        f"Calculate the **Lowest Common Multiple (LCM)** of the three numbers **{n1}**, **{n2}**, and **{n3}**."
    )
    sol = (
        f"**LCM of Three Numbers:**\n"
        f"Taking the highest power of each prime factor across {n1}, {n2}, and {n3} yields:\n"
        f"\\[ \\text{{LCM}}({n1}; {n2}; {n3}) = {lcm} \\]"
    )
    ans = str(lcm)
    return {
        "id": f"g9_lcm_three_{rng.randint(100000, 999999)}",
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
        "subskill": "15_lowest_common_multiple_lcm_using_prime_factors_three_numbers",
        "learning_objective_id": "math_g9_lcm_three",
        "hints": {
            "tier_1": "Prime factorise all 3 numbers.",
            "tier_2": "Take the highest power of all primes present.",
            "tier_3": ans,
        },
        "misconception_tags": ["multiplying_all_three_numbers_together_instead_of_finding_lcm"],
    }


# ----------------------------------------------------------------------
# 16. HCF / LCM Practical Word Problem
# ----------------------------------------------------------------------
def arch_16_hcf_lcm_word_problem_pencils_tiles_or_traffic_lights(rng: random.Random) -> Dict[str, Any]:
    choice = rng.choice(["traffic_lights", "pencil_packs"])
    if choice == "traffic_lights":
        t1, t2 = rng.choice([(24, 36), (30, 45), (40, 60)])
        lcm_val = math.lcm(t1, t2)
        prompt = (
            f"Two security beacons flash at regular intervals. Beacon A flashes every **{t1} seconds**, "
            f"and Beacon B flashes every **{t2} seconds**. If they flash together at 18:00, "
            f"after how many seconds will they next flash together simultaneously?"
        )
        sol = (
            f"**Application of LCM:**\n"
            f"The beacons flash together at common multiples of {t1} and {t2}.\n"
            f"The next simultaneous flash is at the Lowest Common Multiple:\n"
            f"\\[ \\text{{LCM}}({t1}; {t2}) = {lcm_val} \\text{{ seconds}} \\]"
        )
        ans = f"{lcm_val} seconds"
    else:
        pens = rng.choice([48, 60, 72])
        rulers = rng.choice([36, 45, 54])
        hcf_val = math.gcd(pens, rulers)
        prompt = (
            f"A school teacher has **{pens} pens** and **{rulers} rulers** to pack into stationery gift bags. "
            f"Each bag must contain the exact same number of pens and rulers, with none left over.\n\n"
            f"What is the **maximum number of identical bags** the teacher can make?"
        )
        sol = (
            f"**Application of HCF:**\n"
            f"To divide items into the greatest number of identical groups without remainder, find the HCF:\n"
            f"\\[ \\text{{HCF}}({pens}; {rulers}) = {hcf_val} \\text{{ bags}} \\]"
        )
        ans = f"{hcf_val} bags"

    return {
        "id": f"g9_hcf_lcm_word_{rng.randint(100000, 999999)}",
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
        "subskill": "16_hcf_lcm_word_problem_pencils_tiles_or_traffic_lights",
        "learning_objective_id": "math_g9_hcf_lcm_word",
        "hints": {
            "tier_1": "Simultaneous repeating events use LCM; packing items into greatest identical groups uses HCF.",
            "tier_2": "Calculate the HCF or LCM of the two numbers.",
            "tier_3": ans,
        },
        "misconception_tags": ["using_hcf_when_problem_requires_lcm"],
    }


# ----------------------------------------------------------------------
# 17. Simplify Ratios to Simplest Integer Form
# ----------------------------------------------------------------------
def arch_17_simplify_ratios_to_simplest_integer_form(rng: random.Random) -> Dict[str, Any]:
    common = rng.choice([6, 8, 12, 15])
    a_simp = rng.choice([2, 3, 5, 7])
    b_simp = rng.choice([3, 4, 7, 8])
    while math.gcd(a_simp, b_simp) != 1:
        b_simp += 1

    a = a_simp * common
    b = b_simp * common

    prompt = (
        f"Simplify the ratio **{a} : {b}** to its simplest integer form."
    )
    sol = (
        f"**Simplification:**\n"
        f"Divide both parts by their HCF ({common}):\n"
        f"\\[ \\frac{{{a}}}{{{common}}} : \\frac{{{b}}}{{{common}}} = {a_simp} : {b_simp} \\]"
    )
    ans = f"{a_simp}:{b_simp}"
    return {
        "id": f"g9_ratio_simp_{rng.randint(100000, 999999)}",
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
        "subskill": "17_simplify_ratios_to_simplest_integer_form",
        "learning_objective_id": "math_g9_ratio_simp",
        "hints": {
            "tier_1": "Find the highest common factor of both numbers.",
            "tier_2": f"Divide {a} and {b} by {common}.",
            "tier_3": ans,
        },
        "misconception_tags": ["subtracting_common_difference_instead_of_dividing_by_hcf"],
    }


# ----------------------------------------------------------------------
# 18. Simplify Ratios with Different Metric Units
# ----------------------------------------------------------------------
def arch_18_simplify_ratios_with_different_metric_units(rng: random.Random) -> Dict[str, Any]:
    # e.g., 400 m to 1.2 km or 750 g to 1.5 kg
    choice = rng.choice(["length", "mass"])
    if choice == "length":
        km = rng.choice([1.2, 1.5, 2.0, 2.4])
        m = rng.choice([300, 400, 600, 800])
        m_total = int(km * 1000)
        gcd = math.gcd(m, m_total)
        s1 = m // gcd
        s2 = m_total // gcd
        prompt = (
            f"Simplify the ratio **{m} m : {km} km** into simplest integer form.\n"
            f"(Note: Convert both quantities to the same unit first)."
        )
        sol = (
            f"**Unit Conversion & Simplification:**\n"
            f"1. Convert kilometres to metres: ${km} \\text{{ km}} = {m_total} \\text{{ m}}$.\n"
            f"2. Write ratio in same unit: ${m} : {m_total}$.\n"
            f"3. Divide by HCF ({gcd}):\n"
            f"\\[ {s1} : {s2} \\]"
        )
    else:
        kg = rng.choice([1.5, 2.0, 2.5])
        g = rng.choice([250, 500, 750])
        g_total = int(kg * 1000)
        gcd = math.gcd(g, g_total)
        s1 = g // gcd
        s2 = g_total // gcd
        prompt = (
            f"Simplify the ratio **{g} g : {kg} kg** into simplest integer form."
        )
        sol = (
            f"**Unit Conversion & Simplification:**\n"
            f"1. Convert kilograms to grams: ${kg} \\text{{ kg}} = {g_total} \\text{{ g}}$.\n"
            f"2. Ratio: ${g} : {g_total}$.\n"
            f"3. Divide by HCF ({gcd}):\n"
            f"\\[ {s1} : {s2} \\]"
        )
    ans = f"{s1}:{s2}"
    return {
        "id": f"g9_ratio_units_{rng.randint(100000, 999999)}",
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
        "subskill": "18_simplify_ratios_with_different_metric_units",
        "learning_objective_id": "math_g9_ratio_units",
        "hints": {
            "tier_1": "You cannot simplify a ratio until both quantities are in the same unit.",
            "tier_2": "Multiply km or kg by 1000 to convert to metres or grams.",
            "tier_3": ans,
        },
        "misconception_tags": ["ignoring_units_when_simplifying_ratios"],
    }


# ----------------------------------------------------------------------
# 19. Divide Amount in Given Two-Part Ratio
# ----------------------------------------------------------------------
def arch_19_divide_amount_in_given_two_part_ratio(rng: random.Random) -> Dict[str, Any]:
    r1 = rng.choice([2, 3, 4, 5])
    r2 = rng.choice([3, 5, 7])
    total_parts = r1 + r2
    multiplier = rng.choice([15, 20, 25, 40, 50])
    total_amount = total_parts * multiplier
    share1 = r1 * multiplier
    share2 = r2 * multiplier

    prompt = (
        f"Divide **R {total_amount}** between Sipho and Thabo in the ratio **{r1} : {r2}**.\n\n"
        f"Calculate the exact amount each person receives."
    )
    sol = (
        f"**Two-Part Ratio Division:**\n"
        f"1. Total ratio parts: \\({r1} + {r2} = {total_parts}\\).\n"
        f"2. Value of one part: \\(\\frac{{\\text{{R }}{total_amount}}}{{{total_parts}}} = \\text{{R }}{multiplier}\\).\n"
        f"3. Sipho's share: \\({r1} \\times \\text{{R }}{multiplier} = \\text{{R }}{share1}\\).\n"
        f"4. Thabo's share: \\({r2} \\times \\text{{R }}{multiplier} = \\text{{R }}{share2}\\)."
    )
    ans = f"Sipho: R {share1}, Thabo: R {share2}"
    return {
        "id": f"g9_ratio_two_part_{rng.randint(100000, 999999)}",
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
        "subskill": "19_divide_amount_in_given_two_part_ratio",
        "learning_objective_id": "math_g9_ratio_two_part",
        "hints": {
            "tier_1": f"Sum the parts: {r1} + {r2} = {total_parts}.",
            "tier_2": f"Find 1 part: R {total_amount} / {total_parts} = R {multiplier}.",
            "tier_3": ans,
        },
        "misconception_tags": ["dividing_total_by_individual_ratio_part_instead_of_sum"],
    }


# ----------------------------------------------------------------------
# 20. Divide Amount in Given Three-Part Ratio
# ----------------------------------------------------------------------
def arch_20_divide_amount_in_given_three_part_ratio(rng: random.Random) -> Dict[str, Any]:
    r1, r2, r3 = 2, 3, 5
    total_parts = r1 + r2 + r3  # 10
    unit = rng.choice([25, 40, 60, 75, 120])
    total_amount = total_parts * unit
    s1, s2, s3 = r1 * unit, r2 * unit, r3 * unit

    prompt = (
        f"A profit of **R {total_amount}** is shared among three business partners in the ratio **2 : 3 : 5**.\n\n"
        f"Calculate the share received by each partner."
    )
    sol = (
        f"**Three-Part Ratio Division:**\n"
        f"1. Total parts: \\(2 + 3 + 5 = 10\\).\n"
        f"2. Value per part: \\(\\frac{{\\text{{R }}{total_amount}}}{{10}} = \\text{{R }}{unit}\\).\n"
        f"3. Shares:\n"
        f"   - Partner 1: \\(2 \\times \\text{{R }}{unit} = \\text{{R }}{s1}\\)\n"
        f"   - Partner 2: \\(3 \\times \\text{{R }}{unit} = \\text{{R }}{s2}\\)\n"
        f"   - Partner 3: \\(5 \\times \\text{{R }}{unit} = \\text{{R }}{s3}\\)"
    )
    ans = f"R {s1}, R {s2}, R {s3}"
    return {
        "id": f"g9_ratio_three_part_{rng.randint(100000, 999999)}",
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
        "subskill": "20_divide_amount_in_given_three_part_ratio",
        "learning_objective_id": "math_g9_ratio_three_part",
        "hints": {
            "tier_1": "Add all three ratio terms to find the total number of parts.",
            "tier_2": f"Divide R {total_amount} by 10 to find the value of 1 part.",
            "tier_3": ans,
        },
        "misconception_tags": ["dividing_by_3_instead_of_sum_of_ratio_parts"],
    }


# ----------------------------------------------------------------------
# 21. Find Whole Amount Given One Ratio Share
# ----------------------------------------------------------------------
def arch_21_find_whole_amount_given_one_ratio_share(rng: random.Random) -> Dict[str, Any]:
    r1 = 3
    r2 = 5
    multiplier = rng.choice([40, 60, 80, 100])
    given_share = r1 * multiplier
    total_amount = (r1 + r2) * multiplier
    other_share = r2 * multiplier

    prompt = (
        f"Two quantities are in the ratio **{r1} : {r2}**.\n"
        f"If the smaller quantity is **{given_share}**, calculate:\n\n"
        f"1. The value of the larger quantity.\n"
        f"2. The total sum of the two quantities."
    )
    sol = (
        f"**Working:**\n"
        f"1. Smaller share represents {r1} parts = {given_share} \\(\\implies 1 \\text{{ part}} = \\frac{{{given_share}}}{{{r1}}} = {multiplier}\\).\n"
        f"2. Larger share ({r2} parts): \\({r2} \\times {multiplier} = {other_share}\\).\n"
        f"3. Total: \\({given_share} + {other_share} = {total_amount}\\)."
    )
    ans = f"1. {other_share}; 2. {total_amount}"
    return {
        "id": f"g9_ratio_find_whole_{rng.randint(100000, 999999)}",
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
        "subskill": "21_find_whole_amount_given_one_ratio_share",
        "learning_objective_id": "math_g9_ratio_find_whole",
        "hints": {
            "tier_1": f"Divide {given_share} by {r1} to find the value of 1 part.",
            "tier_2": f"Multiply 1 part by {r2} for the larger share, then add.",
            "tier_3": ans,
        },
        "misconception_tags": ["dividing_given_share_by_total_parts"],
    }


# ----------------------------------------------------------------------
# 22. Direct Proportion: Constant Ratio Calculation
# ----------------------------------------------------------------------
def arch_22_direct_proportion_constant_ratio_calculation(rng: random.Random) -> Dict[str, Any]:
    rate = rng.choice([15, 20, 25, 30])
    qty1 = rng.choice([3, 4, 5])
    cost1 = qty1 * rate
    qty2 = rng.choice([7, 8, 9, 12])
    cost2 = qty2 * rate

    prompt = (
        f"If **{qty1} notebooks** cost **R {cost1}**, and the cost is in direct proportion to the number of books:\n\n"
        f"1. Calculate the constant unit rate (cost per single notebook).\n"
        f"2. Calculate the cost of **{qty2} notebooks**."
    )
    sol = (
        f"**Direct Proportion (Constant Ratio):**\n"
        f"1. Unit price \\(k = \\frac{{\\text{{Cost}}}}{{\\text{{Quantity}}}} = \\frac{{\\text{{R }}{cost1}}}{{{qty1}}} = \\text{{R }}{rate}\\).\n"
        f"2. Cost of {qty2} notebooks: \\({qty2} \\times \\text{{R }}{rate} = \\text{{R }}{cost2}\\)."
    )
    ans = f"1. R {rate}; 2. R {cost2}"
    return {
        "id": f"g9_prop_direct_{rng.randint(100000, 999999)}",
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
        "subskill": "22_direct_proportion_constant_ratio_calculation",
        "learning_objective_id": "math_g9_prop_direct",
        "hints": {
            "tier_1": f"Find the price of 1 notebook: R {cost1} / {qty1}.",
            "tier_2": f"Multiply unit price by {qty2}.",
            "tier_3": ans,
        },
        "misconception_tags": ["multiplying_instead_of_dividing_for_unit_rate"],
    }


# ----------------------------------------------------------------------
# 23. Direct Proportion: Missing Table Values
# ----------------------------------------------------------------------
def arch_23_direct_proportion_missing_table_values(rng: random.Random) -> Dict[str, Any]:
    k = rng.choice([4, 6, 8, 12])
    x1, y1 = 2, 2 * k
    x2, y2 = 5, 5 * k
    x3 = 9
    y3 = x3 * k
    y4 = 11 * k
    x4 = 11

    prompt = (
        f"The variables $x$ and $y$ are in **direct proportion** ($y = kx$):\n\n"
        f"| $x$ | {x1} | {x2} | {x3} | $B$ |\n"
        f"|---|---|---|---|---|\n"
        f"| $y$ | {y1} | {y2} | $A$ | {y4} |\n\n"
        f"1. Find the constant of proportionality $k = \\frac{{y}}{{x}}$.\n"
        f"2. Calculate the missing table values $A$ and $B$."
    )
    sol = (
        f"**Direct Proportion Solution:**\n"
        f"1. Constant \\(k = \\frac{{{y1}}}{{{x1}}} = {k}\\).\n"
        f"2. \\(A = k \\times {x3} = {k} \\times {x3} = {y3}\\).\n"
        f"3. \\(B = \\frac{{{y4}}}{{k}} = \\frac{{{y4}}}{{{k}}} = {x4}\\)."
    )
    ans = f"k = {k}, A = {y3}, B = {x4}"
    return {
        "id": f"g9_prop_table_{rng.randint(100000, 999999)}",
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
        "subskill": "23_direct_proportion_missing_table_values",
        "learning_objective_id": "math_g9_prop_table",
        "hints": {
            "tier_1": f"Divide y by x from the first column: {y1} / {x1} = {k}.",
            "tier_2": f"A = {k} * {x3}; B = {y4} / {k}.",
            "tier_3": ans,
        },
        "misconception_tags": ["multiplying_to_find_x_instead_of_dividing_by_constant"],
    }


# ----------------------------------------------------------------------
# 24. Inverse Proportion: Constant Product (Worker-Hours)
# ----------------------------------------------------------------------
def arch_24_inverse_proportion_constant_product_worker_hours(rng: random.Random) -> Dict[str, Any]:
    w1 = rng.choice([2, 3, 4])
    d1 = rng.choice([6, 12, 18, 24])
    total_man_days = w1 * d1
    w2 = rng.choice([w for w in [2, 3, 4, 6, 8, 9, 12] if total_man_days % w == 0 and w != w1])
    d2 = total_man_days // w2

    prompt = (
        f"It takes **{w1} builders {d1} days** to construct a boundary wall working at the same pace.\n\n"
        f"1. Explain why this relationship is in **inverse proportion**.\n"
        f"2. Calculate how many days it will take **{w2} builders** to complete the identical wall."
    )
    sol = (
        f"**Inverse Proportion (Constant Product):**\n"
        f"1. As the number of builders increases, the time taken decreases proportionally ($w \\times d = k$).\n"
        f"2. Total builder-days required: \\({w1} \\times {d1} = {total_man_days}\\) builder-days.\n"
        f"3. Time for {w2} builders:\n"
        f"\\[ d = \\frac{{{total_man_days}}}{{{w2}}} = {d2} \\text{{ days}} \\]"
    )
    ans = f"{d2} days"
    return {
        "id": f"g9_inv_prop_workers_{rng.randint(100000, 999999)}",
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
        "subskill": "24_inverse_proportion_constant_product_worker_hours",
        "learning_objective_id": "math_g9_inv_prop_workers",
        "hints": {
            "tier_1": "In inverse proportion, the product of workers and days stays constant.",
            "tier_2": f"Total builder-days = {w1} * {d1} = {total_man_days}. Divide by {w2}.",
            "tier_3": ans,
        },
        "misconception_tags": ["applying_direct_proportion_cross_multiplication_to_inverse_problem"],
    }


# ----------------------------------------------------------------------
# 25. Inverse Proportion: Speed and Travel Time
# ----------------------------------------------------------------------
def arch_25_inverse_proportion_speed_and_travel_time(rng: random.Random) -> Dict[str, Any]:
    speed1 = rng.choice([60, 80, 90, 100])
    time1 = rng.choice([2.0, 3.0, 4.0])
    distance = speed1 * time1
    speed2 = rng.choice([s for s in [50, 60, 75, 80, 100, 120] if s != speed1])
    time2 = distance / speed2

    prompt = (
        f"A motorist travels between two towns at an average speed of **{speed1} km/h** taking **{time1:g} hours**.\n\n"
        f"1. Calculate the total distance between the two towns.\n"
        f"2. If the driver travels at **{speed2} km/h**, calculate the new travel time (in hours)."
    )
    sol = (
        f"**Inverse Proportion (Speed & Time):**\n"
        f"1. Total distance \\(d = \\text{{speed}} \\times \\text{{time}} = {speed1} \\times {time1:g} = {distance:g} \\text{{ km}}\\).\n"
        f"2. Time at {speed2} km/h:\n"
        f"\\[ t = \\frac{{{distance:g}}}{{{speed2}}} = {_fmt_dec(time2, 2)} \\text{{ hours}} \\]"
    )
    ans = f"1. {distance:g} km; 2. {_fmt_dec(time2, 2)} hours"
    return {
        "id": f"g9_inv_prop_speed_{rng.randint(100000, 999999)}",
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
        "subskill": "25_inverse_proportion_speed_and_travel_time",
        "learning_objective_id": "math_g9_inv_prop_speed",
        "hints": {
            "tier_1": f"Distance = speed * time = {speed1} * {time1:g} = {distance:g} km.",
            "tier_2": f"New time = Distance / new speed = {distance:g} / {speed2}.",
            "tier_3": ans,
        },
        "misconception_tags": ["multiplying_speed_by_new_speed_instead_of_dividing_distance"],
    }
