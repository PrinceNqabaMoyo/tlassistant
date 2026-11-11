"""
Grade 8 Mathematics - Exponents Generator (Archetypes 01 to 25).
100% CAPS-aligned deterministic question generator.
Adheres strictly to the 6-Pillar Generator Contract and Zero-Meta-Curriculum Invariant.
Grounded in curriculum_docs_auto/Mathematics_Gr8/Term 1/03. Exponents.md.
"""
from __future__ import annotations
import math
import random
from typing import Any, Dict, List, Optional


# ==============================================================================
# CLUSTER 1: Fundamentals of Exponential Form (01 - 08)
# ==============================================================================

def arch_01_identify_base_and_exponent(rng: random.Random) -> Dict[str, Any]:
    base = rng.choice([3, 5, 7, 8, 12, "x", "y", "a", "b"])
    exp = rng.randint(3, 8)
    expr = f"({base})^{{{exp}}}" if isinstance(base, int) else f"{base}^{{{exp}}}"

    prompt = (
        f"For the exponential expression $${expr}$$:\n\n"
        f"1. State the base.\n"
        f"2. State the exponent (index).\n"
        f"3. Explain what the exponent indicates about repeated multiplication."
    )
    sol = (
        f"**Step 1:** The base is **{base}** [1 Mark].\n\n"
        f"**Step 2:** The exponent is **{exp}** [1 Mark].\n\n"
        f"**Step 3:** The exponent {exp} indicates that the base {base} is multiplied by itself {exp} times [1 Mark].\n\n"
        f"$$\\therefore \\text{{Base}} = {base}, \\quad \\text{{Exponent}} = {exp}$$"
    )
    ans = f"1. Base = {base}; 2. Exponent = {exp}; 3. The base is multiplied by itself {exp} times"
    return {
        "id": f"g8_exp_01_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 1,
        "subskill": "01_identify_base_and_exponent",
        "hints": {
            "tier_1": "The base is the number or variable being raised to a power.",
            "tier_2": "The exponent is the small superscript number indicating the power.",
            "tier_3": f"Base: {base}, Exponent: {exp}."
        },
        "misconception_tags": ["base_exponent_inversion"]
    }


def arch_02_expanded_factor_form_to_exponential(rng: random.Random) -> Dict[str, Any]:
    var = rng.choice(["x", "m", "p", "k", "c"])
    count = rng.randint(4, 8)
    expanded = " \\times ".join([var] * count)
    ans_expr = f"{var}^{count}"

    prompt = (
        f"Write the following repeated multiplication expression in exponential notation:\n\n"
        f"$${expanded}$$"
    )
    sol = (
        f"**Step 1:** Count the number of identical factors of ${var}$.\n"
        f"There are {count} factors of ${var}$ [1 Mark: Method].\n\n"
        f"**Step 2:** Write as a power with base ${var}$ and exponent ${count}$:\n"
        f"$${expanded} = {ans_expr}$$ [1 Mark: Accuracy]\n\n"
        f"$$\\therefore {ans_expr}$$"
    )
    return {
        "id": f"g8_exp_02_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans_expr,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "02_expanded_factor_form_to_exponential",
        "hints": {
            "tier_1": f"Count how many times {var} is multiplied by itself.",
            "tier_2": f"There are {count} factors of {var}.",
            "tier_3": f"{ans_expr}."
        },
        "misconception_tags": ["multiplication_represented_as_coefficient"]
    }


def arch_03_exponential_form_to_expanded_factor(rng: random.Random) -> Dict[str, Any]:
    var = rng.choice(["a", "b", "y", "t", "w"])
    exp = rng.randint(4, 7)
    expanded = " × ".join([var] * exp)

    prompt = (
        f"Write out the power $${var}^{{{exp}}}$$ in fully expanded factor form."
    )
    sol = (
        f"**Step 1:** Expand the power by multiplying the base ${var}$ by itself ${exp}$ times [1 Mark].\n\n"
        f"$${var}^{{{exp}}} = {expanded}$$ [1 Mark]\n\n"
        f"$$\\therefore {expanded}$$"
    )
    return {
        "id": f"g8_exp_03_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": expanded,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "03_exponential_form_to_expanded_factor",
        "hints": {
            "tier_1": "Write the base repeatedly multiplied by itself as many times as the exponent.",
            "tier_2": f"Write {var} multiplied {exp} times.",
            "tier_3": f"{expanded}."
        },
        "misconception_tags": ["expanded_form_addition_confusion"]
    }


def arch_04_numerical_evaluation_small_powers(rng: random.Random) -> Dict[str, Any]:
    pair = rng.choice([(2, 5), (2, 6), (3, 4), (4, 3), (5, 3), (10, 4)])
    base, exp = pair
    ans = base ** exp

    prompt = (
        f"Calculate the exact numerical value of:\n\n"
        f"$${base}^{{{exp}}}$$"
    )
    sol = (
        f"**Step 1:** Expand into repeated multiplication: $${base}^{{{exp}}} = {' \\times '.join([str(base)] * exp)}$$ [1 Mark: Method]\n\n"
        f"**Step 2:** Calculate: $${ans:,}$$ [1 Mark: Accuracy]\n\n"
        f"$$\\therefore {ans:,}$$"
    )
    return {
        "id": f"g8_exp_04_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": str(ans),
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "04_numerical_evaluation_small_powers",
        "hints": {
            "tier_1": f"Multiply {base} by itself {exp} times.",
            "tier_2": f"Do not multiply base by exponent ({base} × {exp} = {base * exp} is incorrect).",
            "tier_3": f"{base}^{exp} = {ans:,}."
        },
        "misconception_tags": ["base_times_exponent_error"]
    }


def arch_05_zero_exponent_law_numerical(rng: random.Random) -> Dict[str, Any]:
    n = rng.randint(14, 99)
    prompt = (
        f"1. State the value of $${n}^0$$.\n"
        f"2. State the zero exponent rule: for any non-zero real number $a$, what is $a^0$?\n"
        f"3. Explain why $0^0$ is considered indeterminate."
    )
    sol = (
        f"**Step 1:** ${n}^0 = 1$ [1 Mark].\n\n"
        f"**Step 2:** Any non-zero base raised to the power of zero equals 1: $a^0 = 1$ ($a \\neq 0$) [1 Mark].\n\n"
        f"**Step 3:** $0^0$ is indeterminate because any number to power 0 is 1, but 0 to any power is 0, creating a mathematical contradiction [1 Mark].\n\n"
        f"$$\\therefore {n}^0 = 1, \\quad a^0 = 1 \\text{{ for }} a \\neq 0$$"
    )
    ans = f"1. 1; 2. a^0 = 1 (a ≠ 0); 3. 0^0 is indeterminate"
    return {
        "id": f"g8_exp_05_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 1,
        "subskill": "05_zero_exponent_law_numerical",
        "hints": {
            "tier_1": "Any non-zero number to the power of 0 equals 1.",
            "tier_2": "Recall quotient law: a^n / a^n = a^(n-n) = a^0 = 1.",
            "tier_3": f"{n}^0 = 1."
        },
        "misconception_tags": ["zero_exponent_equals_zero_error"]
    }


def arch_06_zero_exponent_law_complex_expression(rng: random.Random) -> Dict[str, Any]:
    c1 = rng.randint(2, 6)
    c2 = rng.randint(3, 8)
    ans = c1 * 1 + c2  # c1 * x^0 + c2 * (y)^0 = c1 + c2

    prompt = (
        f"Simplify the algebraic expression:\n\n"
        f"$${c1}x^0 + {c2}(y)^0$$\n\n"
        f"Explain clearly why the exponent $0$ applies only to $x$ in the first term, but to the entire bracket in the second term."
    )
    sol = (
        f"**Step 1:** In ${c1}x^0$, the power applies only to $x$: $x^0 = 1$, giving ${c1}(1) = {c1}$ [1 Mark].\n\n"
        f"**Step 2:** In ${c2}(y)^0$, $(y)^0 = 1$, giving ${c2}(1) = {c2}$ [1 Mark].\n\n"
        f"**Step 3:** Sum the terms: ${c1} + {c2} = {ans}$ [1 Mark].\n\n"
        f"$$\\therefore {ans}$$"
    )
    return {
        "id": f"g8_exp_06_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": str(ans),
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 1,
        "subskill": "06_zero_exponent_law_complex_expression",
        "hints": {
            "tier_1": "x^0 = 1. So 5x^0 = 5(1) = 5.",
            "tier_2": f"Both x^0 and (y)^0 equal 1.",
            "tier_3": f"{c1}(1) + {c2}(1) = {ans}."
        },
        "misconception_tags": ["coefficient_included_in_zero_exponent"]
    }


def arch_07_exponent_of_one_identity(rng: random.Random) -> Dict[str, Any]:
    n = rng.randint(18, 95)
    prompt = (
        f"1. What is the value of $${n}^1$$.\n"
        f"2. In the algebraic expression $$7x$$, what is the exponent on the variable $x$?"
    )
    sol = (
        f"**Step 1:** Any base raised to the power of $1$ equals the base itself: ${n}^1 = {n}$ [1 Mark].\n\n"
        f"**Step 2:** When no exponent is written, the exponent is understood to be **1** ($7x = 7x^1$) [1 Mark].\n\n"
        f"$$\\therefore {n}^1 = {n}, \\quad \\text{{Exponent on }} x \\text{{ is }} 1$$"
    )
    ans = f"1. {n}; 2. 1"
    return {
        "id": f"g8_exp_07_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "07_exponent_of_one_identity",
        "hints": {
            "tier_1": "A number with power 1 is just the number itself.",
            "tier_2": "An unwritten exponent is always 1.",
            "tier_3": f"Values are {n} and 1."
        },
        "misconception_tags": ["missing_exponent_treated_as_zero"]
    }


def arch_08_powers_of_ten_evaluation(rng: random.Random) -> Dict[str, Any]:
    exp = rng.choice([3, 4, 5, 6])
    ans = 10 ** exp

    prompt = (
        f"Evaluate the power of 10:\n\n"
        f"$$10^{{{exp}}}$$\n\n"
        f"State the relationship between the exponent and the number of zeros following the digit 1."
    )
    sol = (
        f"**Step 1:** $10^{{{exp}}} = {ans:,}$ [1 Mark].\n\n"
        f"**Step 2:** For powers of 10 with a positive integer exponent $n$, the number of trailing zeros is equal to the exponent $n$ ({exp} zeros) [1 Mark].\n\n"
        f"$$\\therefore 10^{{{exp}}} = {ans:,} \\text{{ ({exp} zeros)}}$$"
    )
    ans_text = f"{ans:,} ({exp} zeros)"
    return {
        "id": f"g8_exp_08_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans_text,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "08_powers_of_ten_evaluation",
        "hints": {
            "tier_1": "10^n has 1 followed by n zeros.",
            "tier_2": f"Write 1 followed by {exp} zeros.",
            "tier_3": f"10^{exp} = {ans:,}."
        },
        "misconception_tags": ["power_of_ten_zero_counting_error"]
    }


# ==============================================================================
# CLUSTER 2: Law 1 & Law 2 (Product & Quotient of Powers) (09 - 18)
# ==============================================================================

def arch_09_product_of_powers_same_base_numerical(rng: random.Random) -> Dict[str, Any]:
    base = rng.choice([2, 3, 5])
    e1 = rng.randint(2, 4)
    e2 = rng.randint(2, 4)
    total_exp = e1 + e2
    val = base ** total_exp

    prompt = (
        f"Simplify the following using the product rule for exponents, leaving your answer in exponential form:\n\n"
        f"$${base}^{{{e1}}} \\times {base}^{{{e2}}}$$\n\n"
        f"Then calculate its final numerical value."
    )
    sol = (
        f"**Step 1:** Apply Law 1 ($a^m \\times a^n = a^{{m+n}}$):\n"
        f"$${base}^{{{e1}}} \\times {base}^{{{e2}}} = {base}^{{{e1} + {e2}}} = {base}^{{{total_exp}}}$$ [1 Mark: Method]\n\n"
        f"**Step 2:** Calculate numerical value: $${base}^{{{total_exp}}} = {val:,}$$ [1 Mark: Value]\n\n"
        f"$$\\therefore {base}^{{{total_exp}}} = {val:,}$$"
    )
    ans = f"{base}^{total_exp} = {val:,}"
    return {
        "id": f"g8_exp_09_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "09_product_of_powers_same_base_numerical",
        "hints": {
            "tier_1": "When multiplying powers with the same base, keep the base and add the exponents.",
            "tier_2": f"Exponents: {e1} + {e2} = {total_exp}.",
            "tier_3": f"{base}^{total_exp} = {val:,}."
        },
        "misconception_tags": ["multiplying_bases_instead_of_adding_exponents"]
    }


def arch_10_product_of_powers_same_base_algebraic(rng: random.Random) -> Dict[str, Any]:
    var = rng.choice(["x", "y", "a", "m", "p"])
    e1 = rng.randint(3, 8)
    e2 = rng.randint(2, 7)
    tot = e1 + e2
    ans = f"{var}^{tot}"

    prompt = (
        f"Simplify using the laws of exponents:\n\n"
        f"$${var}^{{{e1}}} \\cdot {var}^{{{e2}}}$$"
    )
    sol = (
        f"**Step 1:** When bases are identical in multiplication, add the exponents:\n"
        f"$${var}^{{{e1}}} \\cdot {var}^{{{e2}}} = {var}^{{{e1} + {e2}}} = {var}^{{{tot}}}$$ [2 Marks]\n\n"
        f"$$\\therefore {ans}$$"
    )
    return {
        "id": f"g8_exp_10_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "10_product_of_powers_same_base_algebraic",
        "hints": {
            "tier_1": "Law 1: a^m × a^n = a^(m+n).",
            "tier_2": f"Add exponents {e1} + {e2}.",
            "tier_3": f"{var}^{tot}."
        },
        "misconception_tags": ["multiplying_exponents_product_rule_error"]
    }


def arch_11_product_of_powers_three_terms(rng: random.Random) -> Dict[str, Any]:
    var = rng.choice(["a", "x", "k", "t"])
    e1 = rng.randint(2, 5)
    e2 = rng.randint(2, 5)
    e3 = rng.randint(2, 5)
    tot = e1 + e2 + e3
    ans = f"{var}^{tot}"

    prompt = (
        f"Simplify the three-term exponential product:\n\n"
        f"$${var}^{{{e1}}} \\times {var}^{{{e2}}} \\times {var}^{{{e3}}}$$"
    )
    sol = (
        f"**Step 1:** Extend Law 1 across all three factors with base ${var}$:\n"
        f"$${var}^{{{e1} + {e2} + {e3}}} = {var}^{{{tot}}}$$ [2 Marks]\n\n"
        f"$$\\therefore {ans}$$"
    )
    return {
        "id": f"g8_exp_11_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "11_product_of_powers_three_terms",
        "hints": {
            "tier_1": "Add all three exponents together.",
            "tier_2": f"{e1} + {e2} + {e3} = {tot}.",
            "tier_3": f"{var}^{tot}."
        },
        "misconception_tags": ["three_term_exponent_addition_slip"]
    }


def arch_12_product_with_coefficients(rng: random.Random) -> Dict[str, Any]:
    c1 = rng.randint(2, 6)
    c2 = rng.randint(3, 7)
    e1 = rng.randint(2, 5)
    e2 = rng.randint(2, 6)
    c_prod = c1 * c2
    e_tot = e1 + e2
    ans = f"{c_prod}x^{e_tot}"

    prompt = (
        f"Simplify the product showing the multiplication of coefficients and powers separately:\n\n"
        f"$$({c1}x^{{{e1}}})({c2}x^{{{e2}}})$$"
    )
    sol = (
        f"**Step 1:** Multiply the numerical coefficients: ${c1} \\times {c2} = {c_prod}$ [1 Mark].\n\n"
        f"**Step 2:** Multiply the variable powers using Law 1: $x^{{{e1}}} \\times x^{{{e2}}} = x^{{{e1} + {e2}}} = x^{{{e_tot}}}$ [1 Mark].\n\n"
        f"**Step 3:** Combine: $${c_prod}x^{{{e_tot}}}$$ [1 Mark].\n\n"
        f"$$\\therefore {ans}$$"
    )
    return {
        "id": f"g8_exp_12_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 1,
        "subskill": "12_product_with_coefficients",
        "hints": {
            "tier_1": "Multiply coefficients together, and add exponents of like variables.",
            "tier_2": f"{c1} × {c2} = {c_prod}, and {e1} + {e2} = {e_tot}.",
            "tier_3": f"{ans}."
        },
        "misconception_tags": ["adding_coefficients_instead_of_multiplying"]
    }


def arch_13_quotient_of_powers_same_base_numerical(rng: random.Random) -> Dict[str, Any]:
    base = rng.choice([2, 3, 5, 7])
    diff = rng.randint(2, 4)
    e2 = rng.randint(2, 5)
    e1 = e2 + diff
    val = base ** diff

    prompt = (
        f"Simplify using the quotient rule for exponents:\n\n"
        f"$$\\frac{{{base}^{{{e1}}}}}{{{base}^{{{e2}}}}}$$\n\n"
        f"Write your answer in exponential form and evaluate its numerical value."
    )
    sol = (
        f"**Step 1:** Apply Law 2 ($a^m \\div a^n = a^{{m-n}}$):\n"
        f"$$\\frac{{{base}^{{{e1}}}}}{{{base}^{{{e2}}}}} = {base}^{{{e1} - {e2}}} = {base}^{{{diff}}}$$ [1 Mark: Method]\n\n"
        f"**Step 2:** Calculate: $${base}^{{{diff}}} = {val}$$ [1 Mark: Value]\n\n"
        f"$$\\therefore {base}^{{{diff}}} = {val}$$"
    )
    ans = f"{base}^{diff} = {val}"
    return {
        "id": f"g8_exp_13_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "13_quotient_of_powers_same_base_numerical",
        "hints": {
            "tier_1": "When dividing powers with the same base, subtract the exponents.",
            "tier_2": f"{e1} - {e2} = {diff}.",
            "tier_3": f"{base}^{diff} = {val}."
        },
        "misconception_tags": ["dividing_bases_quotient_rule_error"]
    }


def arch_14_quotient_of_powers_same_base_algebraic(rng: random.Random) -> Dict[str, Any]:
    var = rng.choice(["x", "y", "m", "p", "a"])
    e2 = rng.randint(2, 5)
    diff = rng.randint(2, 6)
    e1 = e2 + diff
    ans = f"{var}^{diff}"

    prompt = (
        f"Simplify using exponent laws:\n\n"
        f"$$\\frac{{{var}^{{{e1}}}}}{{{var}^{{{e2}}}}}$$"
    )
    sol = (
        f"**Step 1:** Subtract the denominator exponent from the numerator exponent:\n"
        f"$$\\frac{{{var}^{{{e1}}}}}{{{var}^{{{e2}}}}} = {var}^{{{e1} - {e2}}} = {var}^{{{diff}}}$$ [2 Marks]\n\n"
        f"$$\\therefore {ans}$$"
    )
    return {
        "id": f"g8_exp_14_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "14_quotient_of_powers_same_base_algebraic",
        "hints": {
            "tier_1": "Law 2: a^m / a^n = a^(m-n).",
            "tier_2": f"Subtract exponents: {e1} - {e2} = {diff}.",
            "tier_3": f"{var}^{diff}."
        },
        "misconception_tags": ["quotient_rule_adding_exponents_error"]
    }


def arch_15_quotient_with_coefficients(rng: random.Random) -> Dict[str, Any]:
    c_quot = rng.randint(2, 6)
    c_den = rng.randint(2, 5)
    c_num = c_quot * c_den
    e_den = rng.randint(2, 4)
    e_diff = rng.randint(2, 5)
    e_num = e_den + e_diff
    ans = f"{c_quot}x^{e_diff}"

    prompt = (
        f"Simplify the algebraic fraction:\n\n"
        f"$$\\frac{{{c_num}x^{{{e_num}}}}}{{{c_den}x^{{{e_den}}}}}$$"
    )
    sol = (
        f"**Step 1:** Divide the numerical coefficients: $\\frac{{{c_num}}}{{{c_den}}} = {c_quot}$ [1 Mark].\n\n"
        f"**Step 2:** Apply the quotient rule to powers: $\\frac{{x^{{{e_num}}}}}{{x^{{{e_den}}}}} = x^{{{e_num} - {e_den}}} = x^{{{e_diff}}}$ [1 Mark].\n\n"
        f"**Step 3:** Combine: $${c_quot}x^{{{e_diff}}}$$ [1 Mark].\n\n"
        f"$$\\therefore {ans}$$"
    )
    return {
        "id": f"g8_exp_15_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 1,
        "subskill": "15_quotient_with_coefficients",
        "hints": {
            "tier_1": "Divide coefficients: num / den.",
            "tier_2": f"Subtract exponents: {e_num} - {e_den} = {e_diff}.",
            "tier_3": f"{c_num}/{c_den} = {c_quot}; answer is {ans}."
        },
        "misconception_tags": ["subtracting_coefficients_in_fraction"]
    }


def arch_16_mixed_product_and_quotient_single_variable(rng: random.Random) -> Dict[str, Any]:
    e1 = rng.randint(3, 6)
    e2 = rng.randint(3, 6)
    e3 = rng.randint(2, 4)
    tot_num = e1 + e2
    ans_exp = tot_num - e3
    ans = f"x^{ans_exp}"

    prompt = (
        f"Simplify the combined exponential expression:\n\n"
        f"$$\\frac{{x^{{{e1}}} \\cdot x^{{{e2}}}}}{{x^{{{e3}}}}}$$"
    )
    sol = (
        f"**Step 1:** Simplify the numerator using Law 1: $x^{{{e1}}} \\cdot x^{{{e2}}} = x^{{{e1} + {e2}}} = x^{{{tot_num}}}$ [1 Mark].\n\n"
        f"**Step 2:** Apply Law 2 to divide by the denominator: $\\frac{{x^{{{tot_num}}}}}{{x^{{{e3}}}}} = x^{{{tot_num} - {e3}}} = x^{{{ans_exp}}}$ [1 Mark].\n\n"
        f"$$\\therefore {ans}$$"
    )
    return {
        "id": f"g8_exp_16_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "16_mixed_product_and_quotient_single_variable",
        "hints": {
            "tier_1": "Add the exponents in the numerator first, then subtract the denominator exponent.",
            "tier_2": f"Numerator is x^{tot_num}. Subtract {e3}.",
            "tier_3": f"x^{ans_exp}."
        },
        "misconception_tags": ["mixed_exponent_operations_order_error"]
    }


def arch_17_mixed_product_and_quotient_two_variables(rng: random.Random) -> Dict[str, Any]:
    c_quot = rng.randint(2, 5)
    c_den = rng.randint(2, 4)
    c_num = c_quot * c_den
    xa, xb = rng.randint(4, 7), rng.randint(1, 3)
    ya, yb = rng.randint(4, 7), rng.randint(1, 3)
    x_diff = xa - xb
    y_diff = ya - yb
    ans = f"{c_quot}a^{x_diff}b^{y_diff}"

    prompt = (
        f"Simplify the algebraic fraction with two variables:\n\n"
        f"$$\\frac{{{c_num}a^{{{xa}}}b^{{{ya}}}}}{{{c_den}a^{{{xb}}}b^{{{yb}}}}}$$"
    )
    sol = (
        f"**Step 1:** Coefficients: $\\frac{{{c_num}}}{{{c_den}}} = {c_quot}$ [1 Mark].\n\n"
        f"**Step 2:** Variable $a$: $a^{{{xa} - {xb}}} = a^{{{x_diff}}}$ [1 Mark].\n\n"
        f"**Step 3:** Variable $b$: $b^{{{ya} - {yb}}} = b^{{{y_diff}}}$ [1 Mark].\n\n"
        f"$$\\therefore {ans}$$"
    )
    return {
        "id": f"g8_exp_17_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 1,
        "subskill": "17_mixed_product_and_quotient_two_variables",
        "hints": {
            "tier_1": "Simplify coefficients and each variable base independently.",
            "tier_2": f"For a: {xa} - {xb} = {x_diff}; for b: {ya} - {yb} = {y_diff}.",
            "tier_3": f"{ans}."
        },
        "misconception_tags": ["subtracting_exponents_across_different_bases"]
    }


def arch_18_rational_cancellation_with_coefficients(rng: random.Random) -> Dict[str, Any]:
    common = rng.choice([3, 4, 6, 9])
    n_top = rng.choice([2, 4, 5])
    n_bot = rng.choice([3, 7])
    while math.gcd(n_top, n_bot) != 1:
        n_bot += 1
    c1 = n_top * common
    c2 = n_bot * common
    e_top = rng.randint(5, 8)
    e_bot = rng.randint(1, 3)
    e_diff = e_top - e_bot
    ans = f"({n_top}x^{e_diff})/{n_bot}"

    prompt = (
        f"Simplify the fraction to its lowest terms:\n\n"
        f"$$\\frac{{{c1}x^{{{e_top}}}}}{{{c2}x^{{{e_bot}}}}}$$"
    )
    sol = (
        f"**Step 1:** Simplify the coefficients $\\frac{{{c1}}}{{{c2}}}$ by dividing by their HCF (${common}$):\n"
        f"$$\\frac{{{c1} \\div {common}}}{{{c2} \\div {common}}} = \\frac{{{n_top}}}{{{n_bot}}}$$ [1 Mark]\n\n"
        f"**Step 2:** Apply the quotient rule: $x^{{{e_top} - {e_bot}}} = x^{{{e_diff}}}$ [1 Mark]\n\n"
        f"$$\\therefore \\frac{{{n_top}x^{{{e_diff}}}}}{{{n_bot}}}$$"
    )
    return {
        "id": f"g8_exp_18_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "18_rational_cancellation_with_coefficients",
        "hints": {
            "tier_1": "Reduce the numerical fraction and subtract exponents of x.",
            "tier_2": f"{c1}/{c2} reduces to {n_top}/{n_bot}.",
            "tier_3": f"({n_top}x^{e_diff})/{n_bot}."
        },
        "misconception_tags": ["fraction_coefficient_reduction_error"]
    }


# ==============================================================================
# CLUSTER 3: Law 3, Law 4 & Law 5 (Power Rules) (19 - 25)
# ==============================================================================

def arch_19_power_of_a_power_numerical(rng: random.Random) -> Dict[str, Any]:
    base = rng.choice([2, 3])
    m = 2 if base == 3 else rng.randint(2, 3)
    n = 2 if base == 3 else rng.randint(2, 3)
    prod = m * n
    val = base ** prod

    prompt = (
        f"Simplify using the power of a power rule:\n\n"
        f"$$({base}^{{{m}}})^{{{n}}}$$\n\n"
        f"Write your result in single-power form, and calculate its numerical value."
    )
    sol = (
        f"**Step 1:** Apply Law 3 ($(a^m)^n = a^{{m \\times n}}$):\n"
        f"$$({base}^{{{m}}})^{{{n}}} = {base}^{{{m} \\times {n}}} = {base}^{{{prod}}}$$ [1 Mark: Method]\n\n"
        f"**Step 2:** Calculate numerical value: $${base}^{{{prod}}} = {val}$$ [1 Mark: Value]\n\n"
        f"$$\\therefore {base}^{{{prod}}} = {val}$$"
    )
    ans = f"{base}^{prod} = {val}"
    return {
        "id": f"g8_exp_19_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "19_power_of_a_power_numerical",
        "hints": {
            "tier_1": "Multiply the inner exponent by the outer exponent.",
            "tier_2": f"{m} × {n} = {prod}.",
            "tier_3": f"{base}^{prod} = {val}."
        },
        "misconception_tags": ["adding_exponents_in_power_of_power"]
    }


def arch_20_power_of_a_power_algebraic(rng: random.Random) -> Dict[str, Any]:
    var = rng.choice(["x", "y", "m", "t", "a"])
    m = rng.randint(2, 6)
    n = rng.randint(2, 5)
    prod = m * n
    ans = f"{var}^{prod}"

    prompt = (
        f"Simplify using the laws of exponents:\n\n"
        f"$$({var}^{{{m}}})^{{{n}}}$$"
    )
    sol = (
        f"**Step 1:** Multiply the inside exponent by the outside exponent:\n"
        f"$$({var}^{{{m}}})^{{{n}}} = {var}^{{{m} \\times {n}}} = {var}^{{{prod}}}$$ [2 Marks]\n\n"
        f"$$\\therefore {ans}$$"
    )
    return {
        "id": f"g8_exp_20_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "20_power_of_a_power_algebraic",
        "hints": {
            "tier_1": "Law 3: (a^m)^n = a^(mn).",
            "tier_2": f"Multiply exponents: {m} × {n} = {prod}.",
            "tier_3": f"{var}^{prod}."
        },
        "misconception_tags": ["power_of_power_addition_error"]
    }


def arch_21_power_of_a_product_numerical(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(2, 4)
    b = rng.randint(2, 3)
    exp = rng.randint(2, 3)
    ans = (a * b) ** exp

    prompt = (
        f"Demonstrate the **power of a product law** on:\n\n"
        f"$$({a} \\times {b})^{{{exp}}}$$\n\n"
        f"1. Expand using the law: $(ab)^n = a^n b^n$.\n"
        f"2. Calculate the final numerical value."
    )
    t1 = a ** exp
    t2 = b ** exp
    sol = (
        f"**Step 1:** Distribute the exponent to each factor:\n"
        f"$$({a} \\times {b})^{{{exp}}} = {a}^{{{exp}}} \\times {b}^{{{exp}}}$$ [1 Mark]\n\n"
        f"**Step 2:** Calculate: $${t1} \\times {t2} = {ans}$$ [1 Mark]\n\n"
        f"$$\\therefore {a}^{{{exp}}} \\times {b}^{{{exp}}} = {ans}$$"
    )
    ans_text = f"1. {a}^{exp} × {b}^{exp}; 2. {ans}"
    return {
        "id": f"g8_exp_21_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans_text,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "21_power_of_a_product_numerical",
        "hints": {
            "tier_1": "Apply the exponent to each number inside the brackets.",
            "tier_2": f"{a}^{exp} × {b}^{exp} = {t1} × {t2}.",
            "tier_3": f"Final value is {ans}."
        },
        "misconception_tags": ["power_of_product_partial_distribution"]
    }


def arch_22_power_of_a_product_algebraic(rng: random.Random) -> Dict[str, Any]:
    vars_pair = rng.choice([("x", "y"), ("a", "b"), ("m", "n"), ("p", "q")])
    v1, v2 = vars_pair
    exp = rng.randint(3, 7)
    ans = f"{v1}^{exp}{v2}^{exp}"

    prompt = (
        f"Expand the expression using exponent laws:\n\n"
        f"$$({v1}{v2})^{{{exp}}}$$"
    )
    sol = (
        f"**Step 1:** Apply the power of a product rule: $(ab)^n = a^n b^n$:\n"
        f"$$({v1}{v2})^{{{exp}}} = {v1}^{{{exp}}}{v2}^{{{exp}}}$$ [2 Marks]\n\n"
        f"$$\\therefore {ans}$$"
    )
    return {
        "id": f"g8_exp_22_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "22_power_of_a_product_algebraic",
        "hints": {
            "tier_1": "Distribute the outer exponent to both variables inside.",
            "tier_2": f"Both {v1} and {v2} receive power {exp}.",
            "tier_3": f"{ans}."
        },
        "misconception_tags": ["power_applied_only_to_second_variable"]
    }


def arch_23_power_of_a_product_with_coefficients_and_powers(rng: random.Random) -> Dict[str, Any]:
    c = rng.choice([2, 3, 4, 5])
    e_x = rng.randint(2, 4)
    e_y = rng.randint(2, 4)
    outer = rng.choice([2, 3])
    c_pow = c ** outer
    x_pow = e_x * outer
    y_pow = e_y * outer
    ans = f"{c_pow}x^{x_pow}y^{y_pow}"

    prompt = (
        f"Simplify the expression by applying the power to every factor inside the bracket:\n\n"
        f"$$({c}x^{{{e_x}}}y^{{{e_y}}})^{{{outer}}}$$"
    )
    sol = (
        f"**Step 1:** Apply the exponent ${outer}$ to coefficient: ${c}^{{{outer}}} = {c_pow}$ [1 Mark].\n\n"
        f"**Step 2:** Apply exponent ${outer}$ to variables: $(x^{{{e_x}}})^{{{outer}}} = x^{{{x_pow}}}$ and $(y^{{{e_y}}})^{{{outer}}} = y^{{{y_pow}}}$ [1 Mark].\n\n"
        f"**Step 3:** Combine: $${c_pow}x^{{{x_pow}}}y^{{{y_pow}}}$$ [1 Mark].\n\n"
        f"$$\\therefore {ans}$$"
    )
    return {
        "id": f"g8_exp_23_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 1,
        "subskill": "23_power_of_a_product_with_coefficients_and_powers",
        "hints": {
            "tier_1": f"Remember to raise the number {c} to power {outer} as well.",
            "tier_2": f"{c}^{outer} = {c_pow}; multiply variable exponents by {outer}.",
            "tier_3": f"{ans}."
        },
        "misconception_tags": ["forgetting_to_raise_coefficient_to_power"]
    }


def arch_24_power_of_a_quotient_numerical(rng: random.Random) -> Dict[str, Any]:
    pair = rng.choice([(2, 3), (3, 4), (2, 5), (3, 5)])
    num, den = pair
    exp = rng.randint(2, 3)
    p_num = num ** exp
    p_den = den ** exp
    ans = f"{p_num}/{p_den}"

    prompt = (
        f"Calculate the value of the fraction raised to a power:\n\n"
        f"$$\\left(\\frac{{{num}}}{{{den}}}\\right)^{{{exp}}}$$"
    )
    sol = (
        f"**Step 1:** Apply Law 5: $\\left(\\frac{{a}}{{b}}\\right)^n = \\frac{{a^n}}{{b^n}}$ [1 Mark: Method]:\n"
        f"$$\\frac{{{num}^{{{exp}}}}}{{{den}^{{{exp}}}}}$$ \n\n"
        f"**Step 2:** Calculate numerator and denominator: $\\frac{{{p_num}}}{{{p_den}}}$ [1 Mark: Accuracy].\n\n"
        f"$$\\therefore \\frac{{{p_num}}}{{{p_den}}}$$"
    )
    return {
        "id": f"g8_exp_24_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "24_power_of_a_quotient_numerical",
        "hints": {
            "tier_1": "Raise both the top and bottom of the fraction to the power.",
            "tier_2": f"{num}^{exp} / {den}^{exp}.",
            "tier_3": f"{p_num}/{p_den}."
        },
        "misconception_tags": ["raising_only_numerator_to_power"]
    }


def arch_25_power_of_a_quotient_algebraic(rng: random.Random) -> Dict[str, Any]:
    v1, v2 = rng.choice([("a", "b"), ("x", "y"), ("m", "n")])
    exp = rng.randint(3, 6)
    ans = f"({v1}^{exp})/({v2}^{exp})"

    prompt = (
        f"Simplify using the power of a quotient law:\n\n"
        f"$$\\left(\\frac{{{v1}}}{{{v2}}}\\right)^{{{exp}}}$$"
    )
    sol = (
        f"**Step 1:** Apply exponent ${exp}$ to both numerator and denominator:\n"
        f"$$\\left(\\frac{{{v1}}}{{{v2}}}\\right)^{{{exp}}} = \\frac{{{v1}^{{{exp}}}}}{{{v2}^{{{exp}}}}}$$ [2 Marks]\n\n"
        f"$$\\therefore \\frac{{{v1}^{{{exp}}}}}{{{v2}^{{{exp}}}}}$$"
    )
    return {
        "id": f"g8_exp_25_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "25_power_of_a_quotient_algebraic",
        "hints": {
            "tier_1": "Law 5: (a/b)^n = a^n / b^n.",
            "tier_2": f"Apply power {exp} to {v1} and {v2}.",
            "tier_3": f"({v1}^{exp})/({v2}^{exp})."
        },
        "misconception_tags": ["power_of_quotient_single_distribution_error"]
    }
