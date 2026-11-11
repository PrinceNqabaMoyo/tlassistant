"""
Grade 8 Mathematics - Algebraic Expressions 2 Archetypes (26 to 50).
100% CAPS-aligned deterministic question generators.
Adheres strictly to the 6-Pillar Generator Contract and Zero-Meta-Curriculum Invariant.
Grounded in curriculum_docs_auto/Mathematics_Gr8/Term 2/01. Algebraic expressions 2.md.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from app.utils.grade8_mathematics.svg_diagrams import draw_algebraic_shape_perimeter_svg


def arch_26_factorisation_hcf_numerical(rng: random.Random) -> Dict[str, Any]:
    hcf = rng.randint(3, 8)
    rem = rng.randint(2, 7)
    term2 = hcf * rem

    return {
        "title": "Factorisation: Extracting Numerical Highest Common Factor (HCF)",
        "topic": "Algebraic expressions 2",
        "grade": 8,
        "term": 2,
        "subskill": "26_factorisation_hcf_numerical",
        "difficulty": "easy",
        "question_text": (
            f"Factorise the algebraic expression by taking out the highest common factor:\n\n"
            f"$${hcf}x + {term2}$$"
        ),
        "correct_answer": f"{hcf}(x + {rem})",
        "marking_schema": [
            f"Identify common factor {hcf} [1 mark]",
            f"Write in factored form: {hcf}(x + {rem}) [1 mark]",
        ],
        "hints": [
            f"Find the largest integer that divides both {hcf} and {term2}.",
            f"The HCF is {hcf}.",
            f"Divide each term by {hcf}: {hcf}(x + {rem}).",
        ],
        "misconception_tags": ["hcf_incomplete_extraction_error"],
        "diagram_spec": None,
    }


def arch_27_factorisation_hcf_negative_numerical(rng: random.Random) -> Dict[str, Any]:
    hcf = rng.randint(2, 6)
    rem = rng.randint(2, 7)
    term2 = hcf * rem

    return {
        "title": "Factorisation: Extracting a Negative Common Factor",
        "topic": "Algebraic expressions 2",
        "grade": 8,
        "term": 2,
        "subskill": "27_factorisation_hcf_negative_numerical",
        "difficulty": "medium",
        "question_text": (
            f"Factorise by taking out the negative common factor **$-{hcf}$**:\n\n"
            f"$$-{hcf}x - {term2}$$"
        ),
        "correct_answer": f"-{hcf}(x + {rem})",
        "marking_schema": [
            f"Extract -{hcf} and flip signs inside bracket: -{hcf}(x + {rem}) [2 marks]",
        ],
        "hints": [
            f"When you factor out a negative number (-{hcf}), the signs of the terms inside the bracket change.",
            f"(-{hcf}x) ÷ (-{hcf}) = +x.",
            f"(-{term2}) ÷ (-{hcf}) = +{rem}.",
        ],
        "misconception_tags": ["negative_hcf_sign_retention_error"],
        "diagram_spec": None,
    }


def arch_28_factorisation_hcf_single_variable(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(3, 9)

    return {
        "title": "Factorisation: Extracting a Common Variable Factor ($x$)",
        "topic": "Algebraic expressions 2",
        "grade": 8,
        "term": 2,
        "subskill": "28_factorisation_hcf_single_variable",
        "difficulty": "easy",
        "question_text": (
            f"Factorise completely:\n\n"
            f"$$x^2 + {a}x$$"
        ),
        "correct_answer": f"x(x + {a})",
        "marking_schema": [
            f"Extract common factor x: x(x + {a}) [1 mark]",
        ],
        "hints": [
            "Notice that both terms contain the variable $x$.",
            f"Divide $x^2$ by $x$ to get $x$.",
            f"Divide ${a}x$ by $x$ to get {a}.",
            f"Factored form: $x(x + {a})$.",
        ],
        "misconception_tags": ["variable_factorisation_remainder_drop"],
        "diagram_spec": None,
    }


def arch_29_factorisation_hcf_variable_and_number(rng: random.Random) -> Dict[str, Any]:
    hcf_num = rng.choice([2, 3, 4, 5])
    m = rng.choice([2, 3])
    n = rng.choice([3, 5, 7])
    c1 = hcf_num * m
    c2 = hcf_num * n

    return {
        "title": "Factorisation: Extracting Common Numerical and Variable Factors ($ax$)",
        "topic": "Algebraic expressions 2",
        "grade": 8,
        "term": 2,
        "subskill": "29_factorisation_hcf_variable_and_number",
        "difficulty": "medium",
        "question_text": (
            f"Factorise completely by finding the highest common factor of both terms:\n\n"
            f"$${c1}x^2 + {c2}x$$"
        ),
        "correct_answer": f"{hcf_num}x({m}x + {n})",
        "marking_schema": [
            f"Identify full HCF {hcf_num}x [1 mark]",
            f"Complete factored form: {hcf_num}x({m}x + {n}) [1 mark]",
        ],
        "hints": [
            f"Find the numerical HCF of {c1} and {c2}: it is {hcf_num}.",
            f"Find the variable HCF of $x^2$ and $x$: it is $x$.",
            f"Total HCF is {hcf_num}x.",
            f"Divide both terms by {hcf_num}x: {hcf_num}x({m}x + {n}).",
        ],
        "misconception_tags": ["composite_hcf_partial_extraction"],
        "diagram_spec": None,
    }


def arch_30_factorisation_hcf_with_powers_of_x(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(2, 6)
    b = rng.randint(3, 8)

    return {
        "title": "Factorisation: Extracting Common Higher Powers ($x^2$)",
        "topic": "Algebraic expressions 2",
        "grade": 8,
        "term": 2,
        "subskill": "30_factorisation_hcf_with_powers_of_x",
        "difficulty": "medium",
        "question_text": (
            f"Factorise by taking out the highest power of $x$ common to both terms:\n\n"
            f"$${a}x^3 - {b}x^2$$"
        ),
        "correct_answer": f"x^2({a}x - {b})",
        "marking_schema": [
            f"Extract x^2: x^2({a}x - {b}) [2 marks]",
        ],
        "hints": [
            "The highest common power of $x$ in $x^3$ and $x^2$ is $x^2$.",
            f"${a}x^3 ÷ x^2 = {a}x$.",
            f"-{b}x^2 ÷ x^2 = -{b}.",
        ],
        "misconception_tags": ["power_factorisation_lowest_power_rule"],
        "diagram_spec": None,
    }


def arch_31_factorisation_hcf_multivariable(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(2, 5)
    b = rng.randint(3, 7)

    return {
        "title": "Factorisation: Common Factors in Multivariable Terms ($xy$)",
        "topic": "Algebraic expressions 2",
        "grade": 8,
        "term": 2,
        "subskill": "31_factorisation_hcf_multivariable",
        "difficulty": "medium",
        "question_text": (
            f"Factorise completely:\n\n"
            f"$${a}x^2 y + {b}xy$$"
        ),
        "correct_answer": f"xy({a}x + {b})",
        "marking_schema": [
            f"Extract common factor xy: xy({a}x + {b}) [2 marks]",
        ],
        "hints": [
            "Look for variable factors present in both terms: both have at least one $x$ and one $y$.",
            "Factor out $xy$.",
            f"Divide: ${a}x^2 y ÷ xy = {a}x$ and ${b}xy ÷ xy = {b}$.",
        ],
        "misconception_tags": ["multivariable_common_factor_omission"],
        "diagram_spec": None,
    }


def arch_32_factorisation_trinomial_common_factor(rng: random.Random) -> Dict[str, Any]:
    hcf = rng.choice([2, 3, 5])
    a = rng.randint(2, 4)
    b = rng.randint(2, 5)
    c = rng.randint(1, 4)

    t1 = hcf * a
    t2 = hcf * b
    t3 = hcf * c

    return {
        "title": "Factorisation: Common Factor Across a Trinomial",
        "topic": "Algebraic expressions 2",
        "grade": 8,
        "term": 2,
        "subskill": "32_factorisation_trinomial_common_factor",
        "difficulty": "medium",
        "question_text": (
            f"Factorise the trinomial by extracting the common factor:\n\n"
            f"$${t1}x^2 + {t2}x - {t3}$$"
        ),
        "correct_answer": f"{hcf}({a}x^2 + {b}x - {c})",
        "marking_schema": [
            f"Extract {hcf}: {hcf}({a}x^2 + {b}x - {c}) [2 marks]",
        ],
        "hints": [
            f"Find the largest integer that divides {t1}, {t2}, and {t3}.",
            f"The HCF is {hcf}.",
            f"Divide all three terms by {hcf}.",
        ],
        "misconception_tags": ["trinomial_common_factor_omission"],
        "diagram_spec": None,
    }


def arch_33_factorisation_common_binomial_factor(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(2, 7)
    b = rng.randint(2, 7)

    return {
        "title": "Factorisation: Common Binomial Factor",
        "topic": "Algebraic expressions 2",
        "grade": 8,
        "term": 2,
        "subskill": "33_factorisation_common_binomial_factor",
        "difficulty": "medium",
        "question_text": (
            f"Factorise by grouping the common bracket factor:\n\n"
            f"$${a}(x + y) + {b}(x + y)$$"
        ),
        "correct_answer": f"(x + y)({a + b})",
        "marking_schema": [
            f"Extract common bracket (x + y): (x + y)({a} + {b}) [1 mark]",
            f"Simplify remaining factor: {a + b}(x + y) [1 mark]",
        ],
        "hints": [
            "Notice that the entire bracket $(x + y)$ is common to both terms.",
            f"Factor out $(x + y)$: $(x + y)({a} + {b})$.",
            f"Combine numerical terms: {a + b}(x + y).",
        ],
        "misconception_tags": ["common_binomial_factor_confusion"],
        "diagram_spec": None,
    }


def arch_34_factorisation_common_binomial_factor_with_variable(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(2, 8)
    b = rng.randint(2, 8)

    return {
        "title": "Factorisation: Common Binomial Factor with Variable Coefficient",
        "topic": "Algebraic expressions 2",
        "grade": 8,
        "term": 2,
        "subskill": "34_factorisation_common_binomial_factor_with_variable",
        "difficulty": "medium",
        "question_text": (
            f"Factorise completely:\n\n"
            f"$$x(x - {a}) + {b}(x - {a})$$"
        ),
        "correct_answer": f"(x - {a})(x + {b})",
        "marking_schema": [
            f"Take out common bracket (x - {a}): (x - {a})(x + {b}) [2 marks]",
        ],
        "hints": [
            f"Both terms share the bracket $(x - {a})$.",
            f"Take $(x - {a})$ to the front.",
            f"The remaining terms form the second bracket: $(x + {b})$.",
        ],
        "misconception_tags": ["binomial_factor_variable_pairing_error"],
        "diagram_spec": None,
    }


def arch_35_factorisation_difference_of_two_squares_monic(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([2, 3, 4, 5, 6, 7, 8, 9])
    sq = a ** 2

    return {
        "title": "Factorisation: Difference of Two Squares (Monic)",
        "topic": "Algebraic expressions 2",
        "grade": 8,
        "term": 2,
        "subskill": "35_factorisation_difference_of_two_squares_monic",
        "difficulty": "medium",
        "question_text": (
            f"Factorise the difference of two squares:\n\n"
            f"$$x^2 - {sq}$$"
        ),
        "correct_answer": f"(x - {a})(x + {a})",
        "marking_schema": [
            f"Recognize square roots $\\sqrt{{x^2}} = x$ and $\\sqrt{{{sq}}} = {a}$ [1 mark]",
            f"Write as product of conjugates: (x - {a})(x + {a}) [1 mark]",
        ],
        "hints": [
            f"This is a difference of two squares: $A^2 - B^2 = (A - B)(A + B)$.",
            f"Here $A = x$ and $B = \\sqrt{{{sq}}} = {a}$.",
            f"Factored form: $(x - {a})(x + {a})$.",
        ],
        "misconception_tags": ["difference_of_squares_single_bracket_fallacy"],
        "diagram_spec": None,
    }


def arch_36_factorisation_difference_of_two_squares_large_constant(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([10, 11, 12, 13, 15, 20])
    sq = a ** 2

    return {
        "title": "Factorisation: Difference of Two Squares (Larger Square Roots)",
        "topic": "Algebraic expressions 2",
        "grade": 8,
        "term": 2,
        "subskill": "36_factorisation_difference_of_two_squares_large_constant",
        "difficulty": "medium",
        "question_text": (
            f"Factorise completely:\n\n"
            f"$$x^2 - {sq}$$"
        ),
        "correct_answer": f"(x - {a})(x + {a})",
        "marking_schema": [
            f"Identify square root $\\sqrt{{{sq}}} = {a}$ [1 mark]",
            f"Factored form: (x - {a})(x + {a}) [1 mark]",
        ],
        "hints": [
            f"Find the square root of {sq}: $\\sqrt{{{sq}}} = {a}$.",
            f"Apply the rule: $x^2 - {a}^2 = (x - {a})(x + {a})$.",
        ],
        "misconception_tags": ["large_perfect_square_root_error"],
        "diagram_spec": None,
    }


def arch_37_factorisation_difference_of_two_squares_with_coefficient(rng: random.Random) -> Dict[str, Any]:
    m = rng.choice([2, 3, 5])
    n = rng.choice([1, 2, 4, 7])
    sq_m = m ** 2
    sq_n = n ** 2

    return {
        "title": "Factorisation: Difference of Two Squares with Leading Coefficient",
        "topic": "Algebraic expressions 2",
        "grade": 8,
        "term": 2,
        "subskill": "37_factorisation_difference_of_two_squares_with_coefficient",
        "difficulty": "hard",
        "question_text": (
            f"Factorise completely:\n\n"
            f"$${sq_m}x^2 - {sq_n}$$"
        ),
        "correct_answer": f"({m}x - {n})({m}x + {n})",
        "marking_schema": [
            f"Square roots: $\\sqrt{{{sq_m}x^2}} = {m}x$ and $\\sqrt{{{sq_n}}} = {n}$ [1 mark]",
            f"Factored form: ({m}x - {n})({m}x + {n}) [1 mark]",
        ],
        "hints": [
            f"Both terms are perfect squares.",
            f"$\\sqrt{{{sq_m}x^2}} = {m}x$.",
            f"$\\sqrt{{{sq_n}}} = {n}$.",
            f"Rule: $({m}x - {n})({m}x + {n})$.",
        ],
        "misconception_tags": ["coefficient_square_root_omission"],
        "diagram_spec": None,
    }


def arch_38_factorisation_difference_of_two_squares_common_factor_first(rng: random.Random) -> Dict[str, Any]:
    k = rng.choice([2, 3, 5])
    a = rng.choice([2, 3, 4])
    sq_a = a ** 2
    const = k * sq_a

    return {
        "title": "Factorisation: Extracting Common Factor Before Difference of Two Squares",
        "topic": "Algebraic expressions 2",
        "grade": 8,
        "term": 2,
        "subskill": "38_factorisation_difference_of_two_squares_common_factor_first",
        "difficulty": "hard",
        "question_text": (
            f"Factorise completely (Hint: take out a common factor first):\n\n"
            f"$${k}x^2 - {const}$$"
        ),
        "correct_answer": f"{k}(x - {a})(x + {a})",
        "marking_schema": [
            f"Step 1: Extract common factor {k}: {k}(x^2 - {sq_a}) [1 mark]",
            f"Step 2: Factorise difference of squares: {k}(x - {a})(x + {a}) [1 mark]",
        ],
        "hints": [
            f"First take out the common factor {k}: {k}(x^2 - {sq_a}).",
            f"Inside the bracket is a difference of two squares: $x^2 - {sq_a} = (x - {a})(x + {a})$.",
            f"Complete answer: {k}(x - {a})(x + {a}).",
        ],
        "misconception_tags": ["two_step_factorisation_incomplete_error"],
        "diagram_spec": None,
    }


def arch_39_square_root_of_monomial_square(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([3, 4, 5, 6, 7, 8, 9])
    sq = a ** 2

    return {
        "title": "Finding the Square Root of an Algebraic Monomial",
        "topic": "Algebraic expressions 2",
        "grade": 8,
        "term": 2,
        "subskill": "39_square_root_of_monomial_square",
        "difficulty": "easy",
        "question_text": (
            f"Simplify the following radical expression:\n\n"
            f"$$\\sqrt{{{sq}x^2}}$$"
        ),
        "correct_answer": f"{a}x",
        "marking_schema": [
            f"Square root of coefficient: $\\sqrt{{{sq}}} = {a}$ [1 mark]",
            f"Square root of variable: $\\sqrt{{x^2}} = x$ yielding {a}x [1 mark]",
        ],
        "hints": [
            f"$\\sqrt{{{sq}x^2}} = \\sqrt{{{sq}}} \\times \\sqrt{{x^2}}$.",
            f"$\\sqrt{{{sq}}} = {a}$.",
            f"$\\sqrt{{x^2}} = x$.",
        ],
        "misconception_tags": ["square_root_variable_power_half_error"],
        "diagram_spec": None,
    }


def arch_40_square_root_of_higher_power_monomial(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([2, 4, 5, 6])
    sq = a ** 2
    # x^4 or x^6
    power = rng.choice([4, 6])
    half_power = power // 2

    return {
        "title": "Finding Square Roots of Monomials with Even Powers",
        "topic": "Algebraic expressions 2",
        "grade": 8,
        "term": 2,
        "subskill": "40_square_root_of_higher_power_monomial",
        "difficulty": "medium",
        "question_text": (
            f"Simplify the radical expression:\n\n"
            f"$$\\sqrt{{{sq}x^{{{power}}}}}$$"
        ),
        "correct_answer": f"{a}x^{{{half_power}}}",
        "marking_schema": [
            f"Square root of coefficient: {a} [1 mark]",
            f"Halve the variable exponent: $x^{{{power}/2}} = x^{{{half_power}}}$ [1 mark]",
        ],
        "hints": [
            f"Take the square root of the coefficient: $\\sqrt{{{sq}}} = {a}$.",
            f"To take the square root of a variable power, halve the exponent: {power} ÷ 2 = {half_power}.",
            f"Result = ${a}x^{{{half_power}}}$.",
        ],
        "misconception_tags": ["square_root_of_power_root_confusion"],
        "diagram_spec": None,
    }


def arch_41_cube_root_of_monomial_cube(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([2, 3, 4, 5])
    cube = a ** 3

    return {
        "title": "Finding the Cube Root of an Algebraic Monomial",
        "topic": "Algebraic expressions 2",
        "grade": 8,
        "term": 2,
        "subskill": "41_cube_root_of_monomial_cube",
        "difficulty": "easy",
        "question_text": (
            f"Determine the value of the cube root:\n\n"
            f"$$\\sqrt[3]{{{cube}x^3}}$$"
        ),
        "correct_answer": f"{a}x",
        "marking_schema": [
            f"Cube root of {cube}: {a} [1 mark]",
            f"Cube root of $x^3$: x yielding {a}x [1 mark]",
        ],
        "hints": [
            f"What number multiplied by itself three times gives {cube}? ({a} x {a} x {a} = {cube}).",
            f"$\\sqrt[3]{{x^3}} = x$.",
            f"Answer = {a}x.",
        ],
        "misconception_tags": ["cube_root_monomial_confusion"],
        "diagram_spec": None,
    }


def arch_42_cube_root_of_higher_power_monomial(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([2, 3])
    cube = a ** 3
    power = rng.choice([6, 9])
    third_power = power // 3

    return {
        "title": "Finding Cube Roots of Monomials with Multiple of 3 Powers",
        "topic": "Algebraic expressions 2",
        "grade": 8,
        "term": 2,
        "subskill": "42_cube_root_of_higher_power_monomial",
        "difficulty": "medium",
        "question_text": (
            f"Simplify the expression:\n\n"
            f"$$\\sqrt[3]{{{cube}x^{{{power}}}}}$$"
        ),
        "correct_answer": f"{a}x^{{{third_power}}}",
        "marking_schema": [
            f"Cube root of coefficient: {a} [1 mark]",
            f"Divide exponent by 3: {power}/3 = {third_power} yielding {a}x^{{{third_power}}} [1 mark]",
        ],
        "hints": [
            f"$\\sqrt[3]{{{cube}}} = {a}$.",
            f"Divide the variable exponent by 3: {power} ÷ 3 = {third_power}.",
            f"Answer = ${a}x^{{{third_power}}}$.",
        ],
        "misconception_tags": ["cube_root_exponent_division_error"],
        "diagram_spec": None,
    }


def arch_43_cube_root_of_negative_monomial(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([2, 3, 4])
    cube = a ** 3

    return {
        "title": "Finding the Cube Root of a Negative Algebraic Monomial",
        "topic": "Algebraic expressions 2",
        "grade": 8,
        "term": 2,
        "subskill": "43_cube_root_of_negative_monomial",
        "difficulty": "medium",
        "question_text": (
            f"Simplify the cube root expression:\n\n"
            f"$$\\sqrt[3]{{-{cube}x^3}}$$"
        ),
        "correct_answer": f"-{a}x",
        "marking_schema": [
            f"Cube root of negative is negative: $\\sqrt[3]{{-{cube}}} = -{a}$ [1 mark]",
            f"Final answer: -{a}x [1 mark]",
        ],
        "hints": [
            "The cube root of a negative number is always negative.",
            f"(-{a}) x (-{a}) x (-{a}) = -{cube}.",
            f"Answer = -{a}x.",
        ],
        "misconception_tags": ["negative_cube_root_non_real_fallacy"],
        "diagram_spec": None,
    }


def arch_44_geometric_area_model_distributive_law(rng: random.Random) -> Dict[str, Any]:
    seed = rng.randint(1, 1000000)
    w = rng.randint(2, 5)
    b = rng.randint(3, 7)
    len_expr = f"x + {b}"

    svg = draw_algebraic_shape_perimeter_svg(
        shape_type="rectangle",
        side_labels=[len_expr, str(w), len_expr, str(w)],
        title="Rectangle Area Model",
        seed=seed,
    )

    return {
        "title": "Geometric Area Model of the Distributive Law",
        "topic": "Algebraic expressions 2",
        "grade": 8,
        "term": 2,
        "subskill": "44_geometric_area_model_distributive_law",
        "difficulty": "medium",
        "question_text": (
            f"A rectangular playground has width **${w}\\text{{ m}}$** and length **$({len_expr})\\text{{ m}}$**.\n\n"
            "1. Write the area as a product of width and length.\n"
            "2. Expand the expression to determine the total area in square metres."
        ),
        "correct_answer": f"1. {w}(x + {b}). 2. ({w}x + {w * b}) m^2.",
        "marking_schema": [
            f"Product formula: {w}(x + {b}) [1 mark]",
            f"Expanded area: {w}x + {w * b} m^2 [1 mark]",
        ],
        "hints": [
            f"Area = length x width = {w}(x + {b}).",
            f"Distribute {w}: {w} x $x$ + {w} x {b}.",
            f"Total area = {w}x + {w * b}.",
        ],
        "misconception_tags": ["area_model_distributive_expansion_gap"],
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    }


def arch_45_geometric_area_model_binomial_times_binomial(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(2, 5)
    b = rng.randint(2, 6)
    sum_ab = a + b
    prod_ab = a * b

    return {
        "title": "Geometric Area Model: Binomial Product Area",
        "topic": "Algebraic expressions 2",
        "grade": 8,
        "term": 2,
        "subskill": "45_geometric_area_model_binomial_times_binomial",
        "difficulty": "medium",
        "question_text": (
            f"A rectangular room has length **$(x + {a})\\text{{ m}}$** and width **$(x + {b})\\text{{ m}}$**.\n\n"
            "Write down the expanded trinomial expression for the total area of the room in square metres."
        ),
        "correct_answer": f"(x^2 + {sum_ab}x + {prod_ab}) m^2",
        "marking_schema": [
            f"Expand (x + {a})(x + {b}): x^2 + {sum_ab}x + {prod_ab} [2 marks]",
        ],
        "hints": [
            f"Area = (x + {a})(x + {b}).",
            f"FOIL: $x^2 + {b}x + {a}x + {prod_ab}$.",
            f"Area = $x^2 + {sum_ab}x + {prod_ab}$.",
        ],
        "misconception_tags": ["binomial_area_foil_error"],
        "diagram_spec": None,
    }


def arch_46_evaluating_expression_after_expanding(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(2, 4)
    b = rng.randint(2, 4)
    c = rng.randint(1, 3)
    d = rng.randint(2, 3)
    e = rng.randint(1, 4)
    x_val = rng.randint(2, 4)

    # a(bx - c) - d(x - e)
    # = (a*b - d)x - a*c + d*e
    c_x = a * b - d
    c_const = -a * c + d * e
    ans = c_x * x_val + c_const

    return {
        "title": "Expanding, Simplifying, and Evaluating an Algebraic Expression",
        "topic": "Algebraic expressions 2",
        "grade": 8,
        "term": 2,
        "subskill": "46_evaluating_expression_after_expanding",
        "difficulty": "hard",
        "question_text": (
            f"Given the expression:\n\n"
            f"$${a}({b}x - {c}) - {d}(x - {e})$$\n\n"
            f"1. Expand and simplify the expression completely.\n"
            f"2. Calculate its numerical value when **$x = {x_val}$**."
        ),
        "correct_answer": f"1. {c_x}x + {c_const} (or {c_x}x - {abs(c_const)}). 2. {ans}.",
        "marking_schema": [
            f"Expand and combine like terms: {c_x}x + {c_const} [1 mark]",
            f"Substitute x = {x_val} to get {ans} [1 mark]",
        ],
        "hints": [
            f"First expand: {a * b}x - {a * c} - {d}x + {d * e}.",
            f"Combine like terms: ({a * b} - {d})x + (-{a * c} + {d * e}) = {c_x}x + {c_const}.",
            f"Substitute $x = {x_val}$: {c_x}({x_val}) + {c_const} = {ans}.",
        ],
        "misconception_tags": ["expansion_before_substitution_error"],
        "diagram_spec": None,
    }


def arch_47_evaluating_expression_after_factoring(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([4, 5, 6])
    sq = a ** 2
    x_val = rng.choice([14, 15, 16])
    val1 = x_val - a
    val2 = x_val + a
    ans = val1 * val2

    return {
        "title": "Evaluating via Difference of Two Squares Factorisation",
        "topic": "Algebraic expressions 2",
        "grade": 8,
        "term": 2,
        "subskill": "47_evaluating_expression_after_factoring",
        "difficulty": "medium",
        "question_text": (
            f"By first factorising the difference of two squares $x^2 - {sq}$, "
            f"calculate its numerical value when **$x = {x_val}$** without using a calculator."
        ),
        "correct_answer": str(ans),
        "marking_schema": [
            f"Factorise: (x - {a})(x + {a}) [1 mark]",
            f"Evaluate factors: ({x_val} - {a})({x_val} + {a}) = {val1} x {val2} = {ans} [1 mark]",
        ],
        "hints": [
            f"Factorise: $x^2 - {sq} = (x - {a})(x + {a})$.",
            f"Substitute $x = {x_val}$: ({x_val} - {a})({x_val} + {a}) = {val1} x {val2}.",
            f"{val1} x {val2} = {ans}.",
        ],
        "misconception_tags": ["mental_math_factorisation_application_gap"],
        "diagram_spec": None,
    }


def arch_48_simplifying_fraction_by_factorising_numerator(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([2, 3, 4, 5, 6, 7])
    sq = a ** 2

    return {
        "title": "Simplifying Fractions by Factorising Difference of Squares",
        "topic": "Algebraic expressions 2",
        "grade": 8,
        "term": 2,
        "subskill": "48_simplifying_fraction_by_factorising_numerator",
        "difficulty": "hard",
        "question_text": (
            f"Simplify the fraction by factorising the numerator first:\n\n"
            f"$$\\frac{{x^2 - {sq}}}{{x + {a}}}$$"
        ),
        "correct_answer": f"x - {a}",
        "marking_schema": [
            f"Factorise numerator: (x - {a})(x + {a}) [1 mark]",
            f"Cancel common bracket (x + {a}) leaving x - {a} [1 mark]",
        ],
        "hints": [
            f"Factorise the numerator: $x^2 - {sq} = (x - {a})(x + {a})$.",
            f"Divide by $(x + {a})$.",
            f"The matching brackets cancel out, leaving $x - {a}$.",
        ],
        "misconception_tags": ["algebraic_fraction_term_cancellation_fallacy"],
        "diagram_spec": None,
    }


def arch_49_simplifying_fraction_by_factoring_hcf(rng: random.Random) -> Dict[str, Any]:
    k = rng.choice([3, 4, 5, 6])
    b = rng.randint(2, 7)
    kb = k * b

    return {
        "title": "Simplifying Fractions by Extracting HCF from Numerator",
        "topic": "Algebraic expressions 2",
        "grade": 8,
        "term": 2,
        "subskill": "49_simplifying_fraction_by_factoring_hcf",
        "difficulty": "medium",
        "question_text": (
            f"Simplify by factorising the numerator:\n\n"
            f"$$\\frac{{{k}x + {kb}}}{{x + {b}}}$$"
        ),
        "correct_answer": str(k),
        "marking_schema": [
            f"Factorise numerator: {k}(x + {b}) [1 mark]",
            f"Cancel (x + {b}) yielding {k} [1 mark]",
        ],
        "hints": [
            f"Take out {k} from the numerator: {k}(x + {b}).",
            f"Divide by the denominator $(x + {b})$.",
            f"The bracket cancels, leaving {k}.",
        ],
        "misconception_tags": ["hcf_fraction_cancellation_gap"],
        "diagram_spec": None,
    }


def arch_50_algebraic_expressions_2_synthesis_challenge(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([2, 3])
    b = rng.randint(2, 4)
    c = rng.choice([2, 3])

    return {
        "title": "Comprehensive Expansion, Simplification & Factorisation Challenge",
        "topic": "Algebraic expressions 2",
        "grade": 8,
        "term": 2,
        "subskill": "50_algebraic_expressions_2_synthesis_challenge",
        "difficulty": "hard",
        "question_text": (
            f"Given the expression: $${a}x(x + {b}) + {c}x(x - 1)$$\n\n"
            "1. Expand both brackets completely.\n"
            "2. Combine all like terms.\n"
            "3. Factorise your simplified answer by taking out the highest common factor."
        ),
        "correct_answer": f"1. {a}x^2 + {a*b}x + {c}x^2 - {c}x. 2. {a+c}x^2 + {a*b - c}x. 3. x({a+c}x + {a*b - c}).",
        "marking_schema": [
            f"Expand brackets: {a}x^2 + {a*b}x + {c}x^2 - {c}x [1 mark]",
            f"Simplify: {a+c}x^2 + {a*b - c}x [1 mark]",
            f"Factorise out x: x({a+c}x + {a*b - c}) [1 mark]",
        ],
        "hints": [
            f"Expand: ${a}x^2 + {a*b}x + {c}x^2 - {c}x$.",
            f"Combine: $({a+c})x^2 + ({a*b - c})x$.",
            f"Both terms contain $x$, so factor out $x$: $x({a+c}x + {a*b - c})$.",
        ],
        "misconception_tags": ["multi_step_algebraic_manipulation_error"],
        "diagram_spec": None,
    }


BUILDERS_26_50 = [
    arch_26_factorisation_hcf_numerical,
    arch_27_factorisation_hcf_negative_numerical,
    arch_28_factorisation_hcf_single_variable,
    arch_29_factorisation_hcf_variable_and_number,
    arch_30_factorisation_hcf_with_powers_of_x,
    arch_31_factorisation_hcf_multivariable,
    arch_32_factorisation_trinomial_common_factor,
    arch_33_factorisation_common_binomial_factor,
    arch_34_factorisation_common_binomial_factor_with_variable,
    arch_35_factorisation_difference_of_two_squares_monic,
    arch_36_factorisation_difference_of_two_squares_large_constant,
    arch_37_factorisation_difference_of_two_squares_with_coefficient,
    arch_38_factorisation_difference_of_two_squares_common_factor_first,
    arch_39_square_root_of_monomial_square,
    arch_40_square_root_of_higher_power_monomial,
    arch_41_cube_root_of_monomial_cube,
    arch_42_cube_root_of_higher_power_monomial,
    arch_43_cube_root_of_negative_monomial,
    arch_44_geometric_area_model_distributive_law,
    arch_45_geometric_area_model_binomial_times_binomial,
    arch_46_evaluating_expression_after_expanding,
    arch_47_evaluating_expression_after_factoring,
    arch_48_simplifying_fraction_by_factorising_numerator,
    arch_49_simplifying_fraction_by_factoring_hcf,
    arch_50_algebraic_expressions_2_synthesis_challenge,
]
