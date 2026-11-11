"""
Grade 7 Mathematics - Exponents, Squares & Cubes Generator (Archetypes 26 to 50).
100% CAPS-aligned deterministic question generator.
Adheres strictly to the 6-Pillar Generator Contract and Zero-Meta-Curriculum Invariant.
Grounded in curriculum_docs_auto/Mathematics_Gr7/Term 1/02. Exponents.md.
"""
from __future__ import annotations
import math
import random
from typing import Any, Dict, List, Optional


# ==============================================================================
# CLUSTER 4: Exponent Laws / Rules in Arithmetic (26 - 34)
# ==============================================================================

def arch_26_product_of_powers_same_base(rng: random.Random) -> Dict[str, Any]:
    base = rng.choice([2, 3, 5, 7, 10])
    m = rng.choice([2, 3, 4])
    n = rng.choice([2, 3, 4])
    total_exp = m + n

    prompt = (
        f"Simplify the expression using exponential laws (leave your answer in exponential form):\n\n"
        f"$${base}^{{{m}}} \\times {base}^{{{n}}}$$"
    )
    sol = (
        f"**Step 1:** When multiplying powers with the same base, keep the base and add the exponents: "
        f"$a^m \\times a^n = a^{{m+n}}$ [1 Mark: Method].\n\n"
        f"**Step 2:** $${base}^{{{m} + {n}}} = \\mathbf{{{base}^{{{total_exp}}}}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_exp_26_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{base}^{total_exp}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "26_product_of_powers_same_base",
        "hints": {
            "tier_1": "Keep the base unchanged and add the exponents.",
            "tier_2": f"Add {m} and {n}.",
            "tier_3": f"{base}^{total_exp}."
        }
    }


def arch_27_quotient_of_powers_same_base(rng: random.Random) -> Dict[str, Any]:
    base = rng.choice([2, 3, 4, 5, 6, 10])
    diff = rng.choice([2, 3, 4])
    n = rng.choice([2, 3, 4])
    m = n + diff

    prompt = (
        f"Simplify the expression using exponential laws (leave your answer in exponential form):\n\n"
        f"$${base}^{{{m}}} \\div {base}^{{{n}}}$$"
    )
    sol = (
        f"**Step 1:** When dividing powers with the same base, keep the base and subtract the exponents: "
        f"$a^m \\div a^n = a^{{m-n}}$ [1 Mark: Method].\n\n"
        f"**Step 2:** $${base}^{{{m} - {n}}} = \\mathbf{{{base}^{{{diff}}}}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_exp_27_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{base}^{diff}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "27_quotient_of_powers_same_base",
        "hints": {
            "tier_1": "Keep the base unchanged and subtract the smaller exponent from the larger.",
            "tier_2": f"Subtract {n} from {m}.",
            "tier_3": f"{base}^{diff}."
        }
    }


def arch_28_power_of_a_power(rng: random.Random) -> Dict[str, Any]:
    base = rng.choice([2, 3, 5, 10])
    m = rng.choice([2, 3])
    n = rng.choice([2, 3, 4])
    prod_exp = m * n

    prompt = (
        f"Simplify using exponential laws (leave your answer in exponential form):\n\n"
        f"$$({base}^{{{m}}})^{{{n}}}$$"
    )
    sol = (
        f"**Step 1:** When raising a power to another power, keep the base and multiply the exponents: "
        f"$(a^m)^n = a^{{m \\times n}}$ [1 Mark: Method].\n\n"
        f"**Step 2:** $${base}^{{{m} \\times {n}}} = \\mathbf{{{base}^{{{prod_exp}}}}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_exp_28_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{base}^{prod_exp}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "28_power_of_a_power",
        "hints": {
            "tier_1": "Multiply the inside exponent by the outside exponent.",
            "tier_2": f"{m} * {n} = {prod_exp}.",
            "tier_3": f"{base}^{prod_exp}."
        }
    }


def arch_29_power_of_a_product(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([2, 3, 5])
    b = rng.choice([4, 6, 7])
    exp = rng.choice([2, 3])

    prompt = (
        f"Apply the power of a product rule to expand $(a \\times b)^m$:\n\n"
        f"$$({a} \\times {b})^{{{exp}}}$$"
    )
    sol = (
        f"**Step 1:** Distribute the exponent to each factor inside the brackets: "
        f"$(a \\times b)^m = a^m \\times b^m$ [1 Mark: Method].\n\n"
        f"**Step 2:** $$\\mathbf{{{a}^{{{exp}}} \\times {b}^{{{exp}}}}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_exp_29_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{a}^{exp} * {b}^{exp}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "29_power_of_a_product",
        "hints": {
            "tier_1": "Each factor inside the brackets receives the power.",
            "tier_2": f"{a}^{exp} * {b}^{exp}.",
            "tier_3": f"{a}^{exp} * {b}^{exp}."
        }
    }


def arch_30_missing_exponent_product_rule(rng: random.Random) -> Dict[str, Any]:
    base = rng.choice([2, 3, 5, 7])
    m = rng.choice([2, 3, 4])
    x_val = rng.choice([2, 3, 4, 5])
    total = m + x_val

    prompt = (
        f"Determine the value of the unknown exponent $x$ that makes the statement true:\n\n"
        f"$${base}^{{{m}}} \\times {base}^{{x}} = {base}^{{{total}}}$$"
    )
    sol = (
        f"**Step 1:** By the product rule of exponents, ${base}^{{{m} + x}} = {base}^{{{total}}}$ [1 Mark: Method].\n\n"
        f"**Step 2:** Equating exponents: $${m} + x = {total} \\implies x = {total} - {m} = \\mathbf{{{x_val}}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_exp_30_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{x_val}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "30_missing_exponent_product_rule",
        "hints": {
            "tier_1": f"Since bases are identical, {m} + x = {total}.",
            "tier_2": f"x = {total} - {m}.",
            "tier_3": f"x = {x_val}."
        }
    }


def arch_31_missing_exponent_quotient_rule(rng: random.Random) -> Dict[str, Any]:
    base = rng.choice([2, 3, 5, 10])
    n = rng.choice([2, 3, 4])
    diff = rng.choice([2, 3, 4])
    x_val = n + diff

    prompt = (
        f"Determine the value of the unknown exponent $x$:\n\n"
        f"$${base}^{{x}} \\div {base}^{{{n}}} = {base}^{{{diff}}}$$"
    )
    sol = (
        f"**Step 1:** By the quotient rule of exponents, ${base}^{{x - {n}}} = {base}^{{{diff}}}$ [1 Mark: Method].\n\n"
        f"**Step 2:** $x - {n} = {diff} \\implies x = {diff} + {n} = \\mathbf{{{x_val}}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_exp_31_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{x_val}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "31_missing_exponent_quotient_rule",
        "hints": {
            "tier_1": f"x - {n} = {diff}.",
            "tier_2": f"Add {n} to {diff}.",
            "tier_3": f"x = {x_val}."
        }
    }


def arch_32_missing_base_in_cube_equation(rng: random.Random) -> Dict[str, Any]:
    b = rng.choice([2, 3, 4, 5, 6])
    cube_val = b ** 3

    prompt = (
        f"Solve for $x$ where $x$ is a natural number:\n\n"
        f"$$x^3 = {cube_val}$$"
    )
    sol = (
        f"**Step 1:** To isolate $x$, take the cube root of both sides: $x = \\sqrt[3]{{{cube_val}}}$ [1 Mark: Method].\n\n"
        f"**Step 2:** Since ${b} \\times {b} \\times {b} = {cube_val}$, $$x = \\mathbf{{{b}}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_exp_32_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{b}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "32_missing_base_in_cube_equation",
        "hints": {
            "tier_1": f"What number multiplied by itself 3 times gives {cube_val}?",
            "tier_2": f"Find cbrt({cube_val}).",
            "tier_3": f"x = {b}."
        }
    }


def arch_33_missing_base_in_square_equation(rng: random.Random) -> Dict[str, Any]:
    b = rng.choice([7, 8, 9, 11, 12, 13, 14, 15])
    sq_val = b ** 2

    prompt = (
        f"Solve for $x$ where $x > 0$:\n\n"
        f"$$x^2 = {sq_val}$$"
    )
    sol = (
        f"**Step 1:** Take the square root of both sides: $x = \\sqrt{{{sq_val}}}$ [1 Mark: Method].\n\n"
        f"**Step 2:** Since ${b}^2 = {sq_val}$, $$x = \\mathbf{{{b}}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_exp_33_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{b}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "33_missing_base_in_square_equation",
        "hints": {
            "tier_1": f"Find sqrt({sq_val}).",
            "tier_2": f"{b} * {b} = {sq_val}.",
            "tier_3": f"x = {b}."
        }
    }


def arch_34_equivalence_of_exponential_representations(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([2, 3, 4])
    b = rng.choice([3, 5])
    prod = a * b
    exp = rng.choice([2, 3])
    val = prod ** exp

    prompt = (
        f"Show that $({a} \\times {b})^{{{exp}}} = {a}^{{{exp}}} \\times {b}^{{{exp}}}$ by calculating both sides independently."
    )
    sol = (
        f"**Left Hand Side (LHS):**\n"
        f"$$({a} \\times {b})^{{{exp}}} = ({prod})^{{{exp}}} = {val} \\text{{ [1 Mark]}}$$\n\n"
        f"**Right Hand Side (RHS):**\n"
        f"$${a}^{{{exp}}} \\times {b}^{{{exp}}} = {a**exp} \\times {b**exp} = {val} \\text{{ [1 Mark]}}$$\n\n"
        f"Since $\\text{{LHS}} = \\text{{RHS}} = \\mathbf{{{val}}}$, the equivalence is verified [1 Mark: Consequential Accuracy]."
    )
    return {
        "id": f"g7_exp_34_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{val}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 1,
        "subskill": "34_equivalence_of_exponential_representations",
        "hints": {
            "tier_1": f"Calculate ({prod})^{exp} first, then calculate {a}^{exp} * {b}^{exp}.",
            "tier_2": "Both sides will yield the same final numeric value.",
            "tier_3": f"Both equal {val}."
        }
    }


# ==============================================================================
# CLUSTER 5: Order of Operations (BODMAS) with Exponents and Roots (35 - 42)
# ==============================================================================

def arch_35_addition_of_squares(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([3, 4, 5, 6, 7])
    b = rng.choice([2, 3, 4, 5, 8])
    sq_a = a ** 2
    sq_b = b ** 2
    ans = sq_a + sq_b

    prompt = f"Calculate using the correct order of operations:\n\n$${a}^2 + {b}^2$$"
    sol = (
        f"**Step 1:** Evaluate powers first: ${a}^2 = {sq_a}$ and ${b}^2 = {sq_b}$ [1 Mark: Method].\n\n"
        f"**Step 2:** Add the results: $${sq_a} + {sq_b} = \\mathbf{{{ans}}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_exp_35_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{ans}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "35_addition_of_squares",
        "hints": {
            "tier_1": "Calculate each square first, then add.",
            "tier_2": f"{sq_a} + {sq_b}.",
            "tier_3": f"{ans}."
        }
    }


def arch_36_square_root_of_sum_vs_sum_of_roots(rng: random.Random) -> Dict[str, Any]:
    triples = [(3, 4, 9, 16, 25, 5), (6, 8, 36, 64, 100, 10), (5, 12, 25, 144, 169, 13)]
    a, b, a2, b2, c2, c = rng.choice(triples)

    prompt = (
        f"Calculate the following and state whether they are equal:\n\n"
        f"1. $$\\sqrt{{{a2} + {b2}}}$$\n"
        f"2. $$\\sqrt{{{a2}}} + \\sqrt{{{b2}}}$$"
    )
    sol = (
        f"**Expression 1:** Perform operation under the root first:\n"
        f"$$\\sqrt{{{a2} + {b2}}} = \\sqrt{{{c2}}} = \\mathbf{{{c}}} \\text{{ [1 Mark]}}$$\n\n"
        f"**Expression 2:** Evaluate separate roots first:\n"
        f"$$\\sqrt{{{a2}}} + \\sqrt{{{b2}}} = {a} + {b} = \\mathbf{{{a + b}}} \\text{{ [1 Mark]}}$$\n\n"
        f"**Conclusion:** $\\sqrt{{{a2} + {b2}}} \\neq \\sqrt{{{a2}}} + \\sqrt{{{b2}}}$ (i.e. ${c} \\neq {a + b}$) [1 Mark: Conceptual reasoning]."
    )
    return {
        "id": f"g7_exp_36_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"1) {c}; 2) {a + b}; Not equal",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 1,
        "subskill": "36_square_root_of_sum_vs_sum_of_roots",
        "hints": {
            "tier_1": "For the first expression, add inside the root first. For the second, take roots first.",
            "tier_2": f"sqrt({c2}) = {c}, while {a} + {b} = {a+b}.",
            "tier_3": f"Values are {c} and {a+b}; they are NOT equal."
        }
    }


def arch_37_multiplication_with_powers(rng: random.Random) -> Dict[str, Any]:
    c = rng.choice([3, 4, 5, 6, 7])
    base = rng.choice([2, 3])
    exp = rng.choice([2, 3, 4])
    p_val = base ** exp
    ans = c * p_val

    prompt = f"Calculate: $${c} \\times {base}^{{{exp}}}$$"
    sol = (
        f"**Step 1:** Evaluate the exponent first: ${base}^{{{exp}}} = {p_val}$ [1 Mark: Method].\n\n"
        f"**Step 2:** Multiply by ${c}$: $${c} \\times {p_val} = \\mathbf{{{ans}}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_exp_37_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{ans}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "37_multiplication_with_powers",
        "hints": {
            "tier_1": "BODMAS: calculate the power before multiplying.",
            "tier_2": f"{c} * {p_val}.",
            "tier_3": f"{ans}."
        }
    }


def arch_38_division_involving_powers(rng: random.Random) -> Dict[str, Any]:
    cases = [(2, 5, 32, 4, 8), (3, 4, 81, 9, 9), (5, 3, 125, 25, 5), (2, 6, 64, 8, 8), (10, 3, 1000, 50, 20)]
    b, exp, p_val, div, ans = rng.choice(cases)

    prompt = f"Calculate: $${b}^{{{exp}}} \\div {div}$$"
    sol = (
        f"**Step 1:** Evaluate the power: ${b}^{{{exp}}} = {p_val}$ [1 Mark: Method].\n\n"
        f"**Step 2:** Divide: $${p_val} \\div {div} = \\mathbf{{{ans}}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_exp_38_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{ans}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "38_division_involving_powers",
        "hints": {
            "tier_1": f"Compute {b}^{exp} first.",
            "tier_2": f"{p_val} / {div}.",
            "tier_3": f"{ans}."
        }
    }


def arch_39_combined_operations_power_and_subtraction(rng: random.Random) -> Dict[str, Any]:
    b1 = rng.choice([8, 9, 10])
    b2 = rng.choice([2, 3, 4])
    mult = rng.choice([2, 3])
    sq1 = b1 ** 2
    sq2 = b2 ** 2
    term2 = mult * sq2
    ans = sq1 - term2

    prompt = f"Calculate using BODMAS:\n\n$${b1}^2 - {mult} \\times {b2}^2$$"
    sol = (
        f"**Step 1:** Evaluate powers first: ${b1}^2 = {sq1}$ and ${b2}^2 = {sq2}$ [1 Mark: Method].\n\n"
        f"**Step 2:** Perform multiplication: ${mult} \\times {sq2} = {term2}$ [1 Mark: Method].\n\n"
        f"**Step 3:** Subtract: $${sq1} - {term2} = \\mathbf{{{ans}}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_exp_39_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{ans}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 1,
        "subskill": "39_combined_operations_power_and_subtraction",
        "hints": {
            "tier_1": "Powers first, then multiplication, then subtraction.",
            "tier_2": f"{sq1} - ({mult} * {sq2}) = {sq1} - {term2}.",
            "tier_3": f"{ans}."
        }
    }


def arch_40_brackets_and_square_root(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([7, 8, 9, 10])
    b = rng.choice([2, 3, 4])
    diff = a - b
    diff_sq = diff ** 2
    roots = [(16, 4), (25, 5), (36, 6), (49, 7), (64, 8), (81, 9)]
    rt_val, rt_ans = rng.choice(roots)
    ans = diff_sq + rt_ans

    prompt = f"Calculate:\n\n$$({a} - {b})^2 + \\sqrt{{{rt_val}}}$$"
    sol = (
        f"**Step 1:** Evaluate brackets: $({a} - {b}) = {diff}$ [1 Mark: Method].\n\n"
        f"**Step 2:** Evaluate power and root: ${diff}^2 = {diff_sq}$ and $\\sqrt{{{rt_val}}} = {rt_ans}$ [1 Mark: Method].\n\n"
        f"**Step 3:** Add: $${diff_sq} + {rt_ans} = \\mathbf{{{ans}}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_exp_40_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{ans}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 1,
        "subskill": "40_brackets_and_square_root",
        "hints": {
            "tier_1": "Subtract inside brackets, square the result, and add sqrt.",
            "tier_2": f"{diff}^2 + {rt_ans} = {diff_sq} + {rt_ans}.",
            "tier_3": f"{ans}."
        }
    }


def arch_41_operations_with_cubes_and_cube_roots(rng: random.Random) -> Dict[str, Any]:
    b = rng.choice([2, 3, 4])
    cube_val = b ** 3
    cbrt_cases = [(8, 2), (27, 3), (64, 4), (125, 5)]
    val_in, ans_in = rng.choice(cbrt_cases)
    ans = cube_val + ans_in

    prompt = f"Calculate: $${b}^3 + \\sqrt[3]{{{val_in}}}$$"
    sol = (
        f"**Step 1:** Evaluate cube: ${b}^3 = {cube_val}$ [1 Mark: Method].\n\n"
        f"**Step 2:** Evaluate cube root: $\\sqrt[3]{{{val_in}}} = {ans_in}$ [1 Mark: Method].\n\n"
        f"**Step 3:** Add: $${cube_val} + {ans_in} = \\mathbf{{{ans}}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_exp_41_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{ans}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 1,
        "subskill": "41_operations_with_cubes_and_cube_roots",
        "hints": {
            "tier_1": f"Find {b}^3 and cbrt({val_in}).",
            "tier_2": f"{cube_val} + {ans_in}.",
            "tier_3": f"{ans}."
        }
    }


def arch_42_nested_bracket_power_differences(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([2, 3, 4])
    b = rng.choice([2, 3])
    sum_ab = a + b
    sum_sq = sum_ab ** 2

    x = rng.choice([5, 6])
    y = rng.choice([3, 4])
    sq_diff = (x ** 2) - (y ** 2)

    ans = sum_sq - sq_diff

    prompt = f"Calculate the value of:\n\n$$({a} + {b})^2 - ({x}^2 - {y}^2)$$"
    sol = (
        f"**Step 1:** First bracket: $({a} + {b})^2 = {sum_ab}^2 = {sum_sq}$ [1 Mark: Method].\n\n"
        f"**Step 2:** Second bracket: $({x}^2 - {y}^2) = ({x**2} - {y**2}) = {sq_diff}$ [1 Mark: Method].\n\n"
        f"**Step 3:** Subtract results: $${sum_sq} - {sq_diff} = \\mathbf{{{ans}}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_exp_42_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{ans}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 1,
        "subskill": "42_nested_bracket_power_differences",
        "hints": {
            "tier_1": "Calculate each bracketed term completely before subtracting.",
            "tier_2": f"{sum_sq} - {sq_diff}.",
            "tier_3": f"{ans}."
        }
    }


# ==============================================================================
# CLUSTER 6: Scientific Notation, Powers of 10 & Real-World Geometry (43 - 50)
# ==============================================================================

def arch_43_writing_numbers_as_powers_of_ten(rng: random.Random) -> Dict[str, Any]:
    lead = rng.choice([3, 4, 5, 6, 7, 8, 9, 25, 48, 75])
    zeros = rng.choice([3, 4, 5, 6])
    full_val = lead * (10 ** zeros)
    val_s = f"{full_val:,}".replace(",", " ")

    prompt = (
        f"Express the number ${val_s}$ in the form $A \\times 10^n$, where $A = {lead}$:"
    )
    sol = (
        f"**Step 1:** Count the number of trailing zeros: {zeros} zeros [1 Mark: Method].\n\n"
        f"**Step 2:** Write as a power of 10: $${val_s} = \\mathbf{{{lead} \\times 10^{{{zeros}}}}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_exp_43_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{lead} * 10^{zeros}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "43_writing_numbers_as_powers_of_ten",
        "hints": {
            "tier_1": f"Count how many zeros follow {lead}.",
            "tier_2": f"There are {zeros} zeros, which corresponds to 10^{zeros}.",
            "tier_3": f"{lead} * 10^{zeros}."
        }
    }


def arch_44_expanded_powers_of_ten_reconstruction(rng: random.Random) -> Dict[str, Any]:
    d4 = rng.choice([2, 3, 5, 7, 8])
    d3 = rng.choice([1, 4, 6, 9])
    d2 = rng.choice([2, 5, 7])
    d0 = rng.choice([1, 3, 4, 8])
    num = d4 * 10000 + d3 * 1000 + d2 * 100 + d0
    num_s = f"{num:,}".replace(",", " ")

    prompt = (
        f"Reconstruct the standard whole number from its expanded exponential form:\n\n"
        f"$${d4} \\times 10^4 + {d3} \\times 10^3 + {d2} \\times 10^2 + {d0}$$"
    )
    sol = (
        f"**Step 1:** Expand each power of 10:\n"
        f"- ${d4} \\times 10^4 = {d4 * 10000}$\n"
        f"- ${d3} \\times 10^3 = {d3 * 1000}$\n"
        f"- ${d2} \\times 10^2 = {d2 * 100}$\n"
        f"- Units: ${d0}$ [1 Mark: Method].\n\n"
        f"**Step 2:** Add together: $$\\mathbf{{{num_s}}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_exp_44_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": num_s,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "44_expanded_powers_of_ten_reconstruction",
        "hints": {
            "tier_1": "Tens of thousands, thousands, hundreds, and units. Notice tens is 0.",
            "tier_2": f"{d4*10000} + {d3*1000} + {d2*100} + {d0}.",
            "tier_3": f"{num_s}."
        }
    }


def arch_45_astronomical_distance_powers_of_ten(rng: random.Random) -> Dict[str, Any]:
    context = rng.choice([
        ("distance from Earth to the Sun", 150000000, 15, 7, "km"),
        ("approximate distance to the Moon", 384000, 384, 3, "km"),
        ("speed of light per hour in thousands of km", 1080000, 108, 4, "km/h")
    ])
    item, full_val, lead, exp, unit = context
    val_s = f"{full_val:,}".replace(",", " ")

    prompt = (
        f"The {item} is approximately ${val_s}\\text{{ {unit}}}$.\n\n"
        f"Write this measurement in the form ${lead} \\times 10^n\\text{{ {unit}}}$, finding the value of $n$."
    )
    sol = (
        f"**Step 1:** Divide ${val_s}$ by ${lead}$: ${full_val} \\div {lead} = 10^{{{exp}}}$ [1 Mark: Method].\n\n"
        f"**Step 2:** The power of 10 is $n = \\mathbf{{{exp}}}$ [1 Mark: Accuracy].\n\n"
        f"Hence, ${val_s} = \\mathbf{{{lead} \\times 10^{{{exp}}}\\text{{ {unit}}}}}.$"
    )
    return {
        "id": f"g7_exp_45_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"n = {exp}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "45_astronomical_distance_powers_of_ten",
        "hints": {
            "tier_1": f"Count the zeros that follow {lead}.",
            "tier_2": f"There are {exp} zeros.",
            "tier_3": f"n = {exp}."
        }
    }


def arch_46_comparing_powers_of_ten(rng: random.Random) -> Dict[str, Any]:
    lead1 = rng.choice([3, 4, 5])
    exp1 = rng.choice([4, 5])
    lead2 = rng.choice([2, 6, 8])
    exp2 = exp1 + rng.choice([-1, 1])

    val1 = lead1 * (10 ** exp1)
    val2 = lead2 * (10 ** exp2)
    sym = ">" if val1 > val2 else "<"

    prompt = (
        f"Compare using $>$, $<$, or $=$.\n\n"
        f"$${lead1} \\times 10^{{{exp1}}} \\quad \\square \\quad {lead2} \\times 10^{{{exp2}}}$$"
    )
    sol = (
        f"**Step 1:** Evaluate both numbers in standard notation:\n"
        f"- ${lead1} \\times 10^{{{exp1}}} = {val1:,}$\n"
        f"- ${lead2} \\times 10^{{{exp2}}} = {val2:,}$ [1 Mark: Method].\n\n"
        f"**Step 2:** Compare: since ${val1:,} {sym} {val2:,}$, the correct symbol is $$\\mathbf{{{sym}}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_exp_46_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": sym,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "46_comparing_powers_of_ten",
        "hints": {
            "tier_1": "Look at the power of 10 first; higher exponent usually means much larger value.",
            "tier_2": f"{val1} vs {val2}.",
            "tier_3": f"Use {sym}."
        }
    }


def arch_47_doubling_pattern_exponential_growth(rng: random.Random) -> Dict[str, Any]:
    hours = rng.choice([3, 4, 5, 6])
    cells = 2 ** hours

    prompt = (
        f"A single cell divides into 2 cells every hour.\n\n"
        f"1. Write an exponential expression for the number of cells after {hours} hours.\n"
        f"2. Calculate the total number of cells after {hours} hours."
    )
    sol = (
        f"**Step 1:** The number of cells doubles each hour: initial 1, after $h$ hours $= 2^h$. "
        f"After {hours} hours: $$\\mathbf{{2^{{{hours}}}}} \\text{{ [1 Mark: Method]}}$$\n\n"
        f"**Step 2:** Evaluate: $$2^{{{hours}}} = \\mathbf{{{cells}}} \\text{{ cells [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_exp_47_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"2^{hours} = {cells}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "47_doubling_pattern_exponential_growth",
        "hints": {
            "tier_1": f"Express as base 2 raised to power {hours}.",
            "tier_2": f"2^{hours} = {cells}.",
            "tier_3": f"2^{hours} = {cells} cells."
        }
    }


def arch_48_area_of_square_using_exponents(rng: random.Random) -> Dict[str, Any]:
    s = rng.choice([4, 6, 8, 9, 11, 12, 14, 15])
    area = s ** 2

    # Clean 2D diagram spec for the square
    svg_diag = {
        "kind": "inline_svg",
        "svg": (
            f'<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg" style="background:#ffffff;">'
            f'<rect x="40" y="40" width="120" height="120" fill="#f8fafc" stroke="#1e293b" stroke-width="2.5"/>'
            f'<text x="100" y="30" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" fill="#0f172a" text-anchor="middle">{s} cm</text>'
            f'<text x="170" y="105" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" fill="#0f172a" text-anchor="start">{s} cm</text>'
            f'<text x="100" y="105" font-family="system-ui, sans-serif" font-size="13" fill="#64748b" text-anchor="middle">Area = s²</text>'
            f'</svg>'
        ),
        "caption": f"Square with side length s = {s} cm",
        "diagram_role": "context"
    }

    prompt = (
        f"A square has a side length of $s = {s}\\text{{ cm}}$.\n\n"
        f"1. Write down the exponential formula for the area of a square.\n"
        f"2. Calculate its area."
    )
    sol = (
        f"**Step 1:** Formula: $$\\text{{Area}} = s^2 \\text{{ [1 Mark: Method]}}$$\n\n"
        f"**Step 2:** Substitute: $$\\text{{Area}} = {s}^2 = \\mathbf{{{area}\\text{{ cm}}^2}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_exp_48_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{area} cm^2",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "diagram_spec": svg_diag,
        "subskill": "48_area_of_square_using_exponents",
        "hints": {
            "tier_1": "Area of a square = side squared.",
            "tier_2": f"{s}^2 = {s} * {s}.",
            "tier_3": f"{area} cm^2."
        }
    }


def arch_49_side_of_square_from_area_using_roots(rng: random.Random) -> Dict[str, Any]:
    s = rng.choice([5, 7, 8, 10, 12, 13])
    area = s ** 2

    svg_diag = {
        "kind": "inline_svg",
        "svg": (
            f'<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg" style="background:#ffffff;">'
            f'<rect x="40" y="40" width="120" height="120" fill="#f8fafc" stroke="#1e293b" stroke-width="2.5"/>'
            f'<text x="100" y="105" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" fill="#0f172a" text-anchor="middle">Area = {area} m²</text>'
            f'<text x="100" y="180" font-family="system-ui, sans-serif" font-size="13" fill="#64748b" text-anchor="middle">side = s</text>'
            f'</svg>'
        ),
        "caption": f"Square with known area = {area} m²",
        "diagram_role": "context"
    }

    prompt = (
        f"The area of a square playground is ${area}\\text{{ m}}^2$.\n\n"
        f"Calculate the length of one side of the playground."
    )
    sol = (
        f"**Step 1:** Since $\\text{{Area}} = s^2$, side $s = \\sqrt{{\\text{{Area}}}}$ [1 Mark: Method].\n\n"
        f"**Step 2:** $$s = \\sqrt{{{area}}} = \\mathbf{{{s}\\text{{ m}}}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_exp_49_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{s} m",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "diagram_spec": svg_diag,
        "subskill": "49_side_of_square_from_area_using_roots",
        "hints": {
            "tier_1": f"Take the square root of the area: sqrt({area}).",
            "tier_2": f"{s} * {s} = {area}.",
            "tier_3": f"{s} m."
        }
    }


def arch_50_volume_of_cube_using_exponents(rng: random.Random) -> Dict[str, Any]:
    e = rng.choice([2, 3, 4, 5, 6])
    vol = e ** 3

    # Clean isometric cube SVG
    svg_diag = {
        "kind": "inline_svg",
        "svg": (
            f'<svg viewBox="0 0 240 220" xmlns="http://www.w3.org/2000/svg" style="background:#ffffff;">'
            f'<polygon points="60,90 120,60 180,90 120,120" fill="#f1f5f9" stroke="#1e293b" stroke-width="2"/>'
            f'<polygon points="60,90 120,120 120,180 60,150" fill="#e2e8f0" stroke="#1e293b" stroke-width="2"/>'
            f'<polygon points="120,120 180,90 180,150 120,180" fill="#cbd5e1" stroke="#1e293b" stroke-width="2"/>'
            f'<text x="80" y="175" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="middle">edge = {e} cm</text>'
            f'<text x="120" y="45" font-family="system-ui, sans-serif" font-size="13" fill="#64748b" text-anchor="middle">Volume = e³</text>'
            f'</svg>'
        ),
        "caption": f"Cube with edge length e = {e} cm",
        "diagram_role": "context"
    }

    prompt = (
        f"A cube has an edge length of ${e}\\text{{ cm}}$.\n\n"
        f"1. Write down the exponential formula for the volume of a cube.\n"
        f"2. Calculate its volume."
    )
    sol = (
        f"**Step 1:** Formula: $$\\text{{Volume}} = e^3 \\text{{ [1 Mark: Method]}}$$\n\n"
        f"**Step 2:** Substitute: $$\\text{{Volume}} = {e}^3 = \\mathbf{{{vol}\\text{{ cm}}^3}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_exp_50_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{vol} cm^3",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "diagram_spec": svg_diag,
        "subskill": "50_volume_of_cube_using_exponents",
        "hints": {
            "tier_1": "Volume of a cube = edge cubed (e^3).",
            "tier_2": f"{e}^3 = {e} * {e} * {e}.",
            "tier_3": f"{vol} cm^3."
        }
    }
