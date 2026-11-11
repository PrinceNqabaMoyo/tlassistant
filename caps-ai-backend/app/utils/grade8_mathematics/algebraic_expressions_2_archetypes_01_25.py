"""
Grade 8 Mathematics - Algebraic Expressions 2 Archetypes (01 to 25).
100% CAPS-aligned deterministic question generators.
Adheres strictly to the 6-Pillar Generator Contract and Zero-Meta-Curriculum Invariant.
Grounded in curriculum_docs_auto/Mathematics_Gr8/Term 2/01. Algebraic expressions 2.md.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


def arch_01_distributive_law_positive_monomial_binomial_sum(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(2, 6)
    b = rng.randint(2, 5)
    c = rng.randint(3, 9)
    prod_x = a * b
    prod_c = a * c

    return {
        "title": "Distributive Law: Monomial Times Binomial Sum",
        "topic": "Algebraic expressions 2",
        "grade": 8,
        "term": 2,
        "subskill": "01_distributive_law_positive_monomial_binomial_sum",
        "difficulty": "easy",
        "question_text": (
            f"Expand the expression by applying the distributive property:\n\n"
            f"$${a}({b}x + {c})$$"
        ),
        "correct_answer": f"{prod_x}x + {prod_c}",
        "marking_schema": [
            f"Multiply {a} by {b}x: {prod_x}x [1 mark]",
            f"Multiply {a} by {c}: {prod_c} yielding {prod_x}x + {prod_c} [1 mark]",
        ],
        "hints": [
            f"Multiply the term outside the bracket ({a}) by each term inside.",
            f"{a} x {b}x = {prod_x}x.",
            f"{a} x {c} = {prod_c}.",
        ],
        "misconception_tags": ["distributive_single_term_omission"],
        "diagram_spec": None,
    }


def arch_02_distributive_law_positive_monomial_binomial_difference(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(2, 6)
    b = rng.randint(2, 5)
    c = rng.randint(3, 9)
    prod_x = a * b
    prod_c = a * c

    return {
        "title": "Distributive Law: Monomial Times Binomial Difference",
        "topic": "Algebraic expressions 2",
        "grade": 8,
        "term": 2,
        "subskill": "02_distributive_law_positive_monomial_binomial_difference",
        "difficulty": "easy",
        "question_text": (
            f"Expand the algebraic expression:\n\n"
            f"$${a}({b}x - {c})$$"
        ),
        "correct_answer": f"{prod_x}x - {prod_c}",
        "marking_schema": [
            f"Multiply {a} by {b}x: {prod_x}x [1 mark]",
            f"Multiply {a} by -{c}: -{prod_c} [1 mark]",
        ],
        "hints": [
            f"Distribute {a} across both terms inside the bracket.",
            f"{a} x {b}x = {prod_x}x.",
            f"{a} x (-{c}) = -{prod_c}.",
        ],
        "misconception_tags": ["subtraction_sign_distribution_error"],
        "diagram_spec": None,
    }


def arch_03_distributive_law_negative_monomial_binomial_sum(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(2, 5)
    b = rng.randint(2, 4)
    c = rng.randint(2, 7)
    prod_x = -a * b
    prod_c = -a * c

    return {
        "title": "Distributive Law: Negative Multiplier with Binomial Sum",
        "topic": "Algebraic expressions 2",
        "grade": 8,
        "term": 2,
        "subskill": "03_distributive_law_negative_monomial_binomial_sum",
        "difficulty": "medium",
        "question_text": (
            f"Expand and simplify:\n\n"
            f"$$-{a}({b}x + {c})$$"
        ),
        "correct_answer": f"{prod_x}x - {abs(prod_c)}",
        "marking_schema": [
            f"Multiply -{a} by {b}x: {prod_x}x [1 mark]",
            f"Multiply -{a} by +{c}: {prod_c} [1 mark]",
        ],
        "hints": [
            f"Multiply both terms inside by -{a}.",
            f"(-{a}) x ({b}x) = {prod_x}x.",
            f"(-{a}) x (+{c}) = {prod_c}.",
        ],
        "misconception_tags": ["negative_multiplier_sign_flip_error"],
        "diagram_spec": None,
    }


def arch_04_distributive_law_negative_monomial_binomial_difference(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(2, 5)
    b = rng.randint(2, 4)
    c = rng.randint(2, 8)
    prod_x = -a * b
    prod_c = a * c  # -a * -c = +ac

    return {
        "title": "Distributive Law: Negative Multiplier with Binomial Difference",
        "topic": "Algebraic expressions 2",
        "grade": 8,
        "term": 2,
        "subskill": "04_distributive_law_negative_monomial_binomial_difference",
        "difficulty": "medium",
        "question_text": (
            f"Expand the expression:\n\n"
            f"$$-{a}({b}x - {c})$$"
        ),
        "correct_answer": f"{prod_x}x + {prod_c}",
        "marking_schema": [
            f"Multiply -{a} by {b}x: {prod_x}x [1 mark]",
            f"Multiply -{a} by -{c}: +{prod_c} [1 mark]",
        ],
        "hints": [
            f"Remember: a negative multiplied by a negative gives a positive.",
            f"(-{a}) x ({b}x) = {prod_x}x.",
            f"(-{a}) x (-{c}) = +{prod_c}.",
        ],
        "misconception_tags": ["negative_times_negative_error"],
        "diagram_spec": None,
    }


def arch_05_distributive_law_variable_multiplier(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(2, 6)
    b = rng.randint(3, 9)

    return {
        "title": "Distributive Law: Variable Multiplier ($x$)",
        "topic": "Algebraic expressions 2",
        "grade": 8,
        "term": 2,
        "subskill": "05_distributive_law_variable_multiplier",
        "difficulty": "easy",
        "question_text": (
            f"Expand the expression by distributing $x$:\n\n"
            f"$$x({a}x + {b})$$"
        ),
        "correct_answer": f"{a}x^2 + {b}x",
        "marking_schema": [
            f"Multiply $x$ by {a}x: {a}x^2 [1 mark]",
            f"Multiply $x$ by {b}: {b}x [1 mark]",
        ],
        "hints": [
            f"$x \\times x = x^2$.",
            f"$x \\times {a}x = {a}x^2$.",
            f"$x \\times {b} = {b}x$.",
        ],
        "misconception_tags": ["x_times_x_equals_2x_fallacy"],
        "diagram_spec": None,
    }


def arch_06_distributive_law_variable_multiplier_with_negative(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(2, 5)
    b = rng.randint(3, 8)

    return {
        "title": "Distributive Law: Negative Variable Multiplier ($-x$)",
        "topic": "Algebraic expressions 2",
        "grade": 8,
        "term": 2,
        "subskill": "06_distributive_law_variable_multiplier_with_negative",
        "difficulty": "medium",
        "question_text": (
            f"Expand and simplify:\n\n"
            f"$$-x({a}x - {b})$$"
        ),
        "correct_answer": f"-{a}x^2 + {b}x",
        "marking_schema": [
            f"Multiply -x by {a}x: -{a}x^2 [1 mark]",
            f"Multiply -x by -{b}: +{b}x [1 mark]",
        ],
        "hints": [
            f"(-x) x ({a}x) = -{a}x^2.",
            f"(-x) x (-{b}) = +{b}x.",
            f"Result = -{a}x^2 + {b}x.",
        ],
        "misconception_tags": ["negative_x_distribution_error"],
        "diagram_spec": None,
    }


def arch_07_distributive_law_monomial_with_variable_and_coefficient(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(2, 5)
    b = rng.randint(2, 4)
    c = rng.randint(3, 7)
    prod_sq = a * b
    prod_lin = a * c

    return {
        "title": "Distributive Law: Monomial Term $ax(bx + c)$",
        "topic": "Algebraic expressions 2",
        "grade": 8,
        "term": 2,
        "subskill": "07_distributive_law_monomial_with_variable_and_coefficient",
        "difficulty": "medium",
        "question_text": (
            f"Expand the expression:\n\n"
            f"$${a}x({b}x + {c})$$"
        ),
        "correct_answer": f"{prod_sq}x^2 + {prod_lin}x",
        "marking_schema": [
            f"Multiply {a}x by {b}x: {prod_sq}x^2 [1 mark]",
            f"Multiply {a}x by {c}: {prod_lin}x [1 mark]",
        ],
        "hints": [
            f"Multiply coefficients: {a} x {b} = {prod_sq}.",
            f"Multiply variables: $x \\times x = x^2$.",
            f"Then multiply {a}x by {c}: {prod_lin}x.",
        ],
        "misconception_tags": ["monomial_binomial_coefficient_product_error"],
        "diagram_spec": None,
    }


def arch_08_distributive_law_monomial_with_variable_and_negative_coefficient(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(2, 5)
    b = rng.randint(2, 4)
    c = rng.randint(3, 8)
    prod_sq = -a * b
    prod_lin = a * c

    return {
        "title": "Distributive Law: Negative Monomial Term $-ax(bx - c)$",
        "topic": "Algebraic expressions 2",
        "grade": 8,
        "term": 2,
        "subskill": "08_distributive_law_monomial_with_variable_and_negative_coefficient",
        "difficulty": "medium",
        "question_text": (
            f"Expand and simplify:\n\n"
            f"$$-{a}x({b}x - {c})$$"
        ),
        "correct_answer": f"{prod_sq}x^2 + {prod_lin}x",
        "marking_schema": [
            f"Multiply -{a}x by {b}x: {prod_sq}x^2 [1 mark]",
            f"Multiply -{a}x by -{c}: +{prod_lin}x [1 mark]",
        ],
        "hints": [
            f"(-{a}x) x ({b}x) = {prod_sq}x^2.",
            f"(-{a}x) x (-{c}) = +{prod_lin}x.",
            f"Final answer = {prod_sq}x^2 + {prod_lin}x.",
        ],
        "misconception_tags": ["negative_monomial_sign_error"],
        "diagram_spec": None,
    }


def arch_09_distributive_law_monomial_times_trinomial(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(2, 4)
    b = rng.randint(2, 4)
    c = rng.randint(2, 5)
    d = rng.randint(2, 6)

    t1 = a * b
    t2 = a * c
    t3 = a * d

    return {
        "title": "Distributive Law: Monomial Times Trinomial",
        "topic": "Algebraic expressions 2",
        "grade": 8,
        "term": 2,
        "subskill": "09_distributive_law_monomial_times_trinomial",
        "difficulty": "medium",
        "question_text": (
            f"Expand the expression by distributing {a} across all three terms:\n\n"
            f"$${a}({b}x^2 + {c}x - {d})$$"
        ),
        "correct_answer": f"{t1}x^2 + {t2}x - {t3}",
        "marking_schema": [
            f"Expand all 3 terms: {t1}x^2 + {t2}x - {t3} [2 marks]",
        ],
        "hints": [
            f"Multiply {a} by {b}x^2 = {t1}x^2.",
            f"Multiply {a} by {c}x = {t2}x.",
            f"Multiply {a} by -{d} = -{t3}.",
        ],
        "misconception_tags": ["trinomial_distribution_omission"],
        "diagram_spec": None,
    }


def arch_10_distributive_law_negative_monomial_times_trinomial(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(2, 4)
    b = rng.randint(2, 4)
    c = rng.randint(2, 5)
    d = rng.randint(2, 6)

    t1 = -a * b
    t2 = a * c   # -a * -c = +ac
    t3 = -a * d

    return {
        "title": "Distributive Law: Negative Multiplier with Trinomial",
        "topic": "Algebraic expressions 2",
        "grade": 8,
        "term": 2,
        "subskill": "10_distributive_law_negative_monomial_times_trinomial",
        "difficulty": "hard",
        "question_text": (
            f"Expand and simplify:\n\n"
            f"$$-{a}({b}x^2 - {c}x + {d})$$"
        ),
        "correct_answer": f"{t1}x^2 + {t2}x - {abs(t3)}",
        "marking_schema": [
            f"Expand with careful signs: {t1}x^2 + {t2}x - {abs(t3)} [2 marks]",
        ],
        "hints": [
            f"(-{a}) x ({b}x^2) = {t1}x^2.",
            f"(-{a}) x (-{c}x) = +{t2}x.",
            f"(-{a}) x (+{d}) = -{abs(t3)}.",
        ],
        "misconception_tags": ["negative_trinomial_sign_error"],
        "diagram_spec": None,
    }


def arch_11_expanding_and_simplifying_sum_of_two_distributed_brackets(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(2, 4)
    b = rng.randint(2, 5)
    c = rng.randint(2, 4)
    d = rng.randint(2, 6)

    tot_x = a + c
    tot_const = (a * b) + (c * d)

    return {
        "title": "Expanding and Simplifying: Sum of Two Binomial Products",
        "topic": "Algebraic expressions 2",
        "grade": 8,
        "term": 2,
        "subskill": "11_expanding_and_simplifying_sum_of_two_distributed_brackets",
        "difficulty": "medium",
        "question_text": (
            f"Expand and simplify by combining like terms:\n\n"
            f"$${a}(x + {b}) + {c}(x + {d})$$"
        ),
        "correct_answer": f"{tot_x}x + {tot_const}",
        "marking_schema": [
            f"Expand both brackets: {a}x + {a * b} + {c}x + {c * d} [1 mark]",
            f"Combine like terms: {tot_x}x + {tot_const} [1 mark]",
        ],
        "hints": [
            f"Expand the first bracket: {a}(x + {b}) = {a}x + {a * b}.",
            f"Expand the second bracket: {c}(x + {d}) = {c}x + {c * d}.",
            f"Combine like terms: ({a}x + {c}x) + ({a * b} + {c * d}) = {tot_x}x + {tot_const}.",
        ],
        "misconception_tags": ["nested_expansion_combining_error"],
        "diagram_spec": None,
    }


def arch_12_expanding_and_simplifying_difference_of_two_distributed_brackets(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(4, 7)
    b = rng.randint(2, 5)
    c = rng.randint(2, 3)
    d = rng.randint(2, 5)

    tot_x = a - c
    tot_const = (a * b) + (c * d)  # a*b - c*(-d) = a*b + c*d

    return {
        "title": "Expanding and Simplifying: Difference of Two Binomial Products",
        "topic": "Algebraic expressions 2",
        "grade": 8,
        "term": 2,
        "subskill": "12_expanding_and_simplifying_difference_of_two_distributed_brackets",
        "difficulty": "hard",
        "question_text": (
            f"Expand and simplify completely:\n\n"
            f"$${a}(x + {b}) - {c}(x - {d})$$"
        ),
        "correct_answer": f"{tot_x}x + {tot_const}",
        "marking_schema": [
            f"Expand with correct signs: {a}x + {a * b} - {c}x + {c * d} [1 mark]",
            f"Combine like terms: {tot_x}x + {tot_const} [1 mark]",
        ],
        "hints": [
            f"First bracket: {a}x + {a * b}.",
            f"Second bracket: -{c}(x - {d}) = -{c}x + {c * d}.",
            f"Combine: ({a} - {c})x + ({a * b} + {c * d}) = {tot_x}x + {tot_const}.",
        ],
        "misconception_tags": ["nested_bracket_subtraction_sign_error"],
        "diagram_spec": None,
    }


def arch_13_expanding_and_simplifying_variable_brackets_with_like_terms(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(2, 5)
    b = rng.randint(1, 4)
    # x(x + a) + 2x(x - b) = x^2 + ax + 2x^2 - 2bx = 3x^2 + (a - 2b)x
    tot_sq = 3
    tot_lin = a - 2 * b
    sign = "+" if tot_lin >= 0 else "-"
    abs_lin = abs(tot_lin)

    return {
        "title": "Expanding and Simplifying: Variable Multipliers",
        "topic": "Algebraic expressions 2",
        "grade": 8,
        "term": 2,
        "subskill": "13_expanding_and_simplifying_variable_brackets_with_like_terms",
        "difficulty": "hard",
        "question_text": (
            f"Expand and simplify:\n\n"
            f"$$x(x + {a}) + 2x(x - {b})$$"
        ),
        "correct_answer": f"{tot_sq}x^2 {sign} {abs_lin}x" if abs_lin != 0 else f"{tot_sq}x^2",
        "marking_schema": [
            f"Expand brackets: x^2 + {a}x + 2x^2 - {2 * b}x [1 mark]",
            f"Combine like terms: {tot_sq}x^2 {sign} {abs_lin}x [1 mark]",
        ],
        "hints": [
            f"$x(x + {a}) = x^2 + {a}x$.",
            f"$2x(x - {b}) = 2x^2 - {2 * b}x$.",
            f"Combine $x^2$ and $x$ terms.",
        ],
        "misconception_tags": ["variable_distribution_power_error"],
        "diagram_spec": None,
    }


def arch_14_expanding_binomial_product_positive_terms(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(2, 6)
    b = rng.randint(3, 7)
    sum_ab = a + b
    prod_ab = a * b

    return {
        "title": "Expanding Binomial Products: $(x + a)(x + b)$",
        "topic": "Algebraic expressions 2",
        "grade": 8,
        "term": 2,
        "subskill": "14_expanding_binomial_product_positive_terms",
        "difficulty": "medium",
        "question_text": (
            f"Expand and simplify the product of two binomials:\n\n"
            f"$$(x + {a})(x + {b})$$"
        ),
        "correct_answer": f"x^2 + {sum_ab}x + {prod_ab}",
        "marking_schema": [
            f"Apply FOIL: x^2 + {b}x + {a}x + {prod_ab} [1 mark]",
            f"Combine middle terms: x^2 + {sum_ab}x + {prod_ab} [1 mark]",
        ],
        "hints": [
            "Use FOIL (First, Outer, Inner, Last).",
            f"First: $x \\times x = x^2$.",
            f"Outer + Inner: {b}x + {a}x = {sum_ab}x.",
            f"Last: {a} x {b} = {prod_ab}.",
        ],
        "misconception_tags": ["foil_inner_outer_omission"],
        "diagram_spec": None,
    }


def arch_15_expanding_binomial_product_mixed_signs(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(4, 8)
    b = rng.randint(2, 5)
    diff_ab = a - b
    prod_ab = a * b
    sign = "+" if diff_ab >= 0 else "-"
    abs_diff = abs(diff_ab)

    return {
        "title": "Expanding Binomial Products with Mixed Signs: $(x + a)(x - b)$",
        "topic": "Algebraic expressions 2",
        "grade": 8,
        "term": 2,
        "subskill": "15_expanding_binomial_product_mixed_signs",
        "difficulty": "medium",
        "question_text": (
            f"Expand and simplify:\n\n"
            f"$$(x + {a})(x - {b})$$"
        ),
        "correct_answer": f"x^2 {sign} {abs_diff}x - {prod_ab}",
        "marking_schema": [
            f"FOIL expansion: x^2 - {b}x + {a}x - {prod_ab} [1 mark]",
            f"Combine like terms: x^2 {sign} {abs_diff}x - {prod_ab} [1 mark]",
        ],
        "hints": [
            f"First: $x^2$.",
            f"Outer + Inner: -{b}x + {a}x = {diff_ab}x.",
            f"Last: (+{a}) x (-{b}) = -{prod_ab}.",
        ],
        "misconception_tags": ["mixed_signs_foil_middle_term_error"],
        "diagram_spec": None,
    }


def arch_16_expanding_binomial_product_both_negative(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(2, 6)
    b = rng.randint(3, 7)
    sum_ab = a + b
    prod_ab = a * b

    return {
        "title": "Expanding Binomial Products: $(x - a)(x - b)$",
        "topic": "Algebraic expressions 2",
        "grade": 8,
        "term": 2,
        "subskill": "16_expanding_binomial_product_both_negative",
        "difficulty": "medium",
        "question_text": (
            f"Expand and simplify:\n\n"
            f"$$(x - {a})(x - {b})$$"
        ),
        "correct_answer": f"x^2 - {sum_ab}x + {prod_ab}",
        "marking_schema": [
            f"FOIL expansion: x^2 - {b}x - {a}x + {prod_ab} [1 mark]",
            f"Combine middle terms: x^2 - {sum_ab}x + {prod_ab} [1 mark]",
        ],
        "hints": [
            f"First: $x^2$.",
            f"Outer + Inner: -{b}x - {a}x = -{sum_ab}x.",
            f"Last: (-{a}) x (-{b}) = +{prod_ab}.",
        ],
        "misconception_tags": ["negative_times_negative_constant_sign_error"],
        "diagram_spec": None,
    }


def arch_17_squaring_binomial_sum(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(2, 8)
    mid = 2 * a
    sq = a ** 2

    return {
        "title": "Squaring a Binomial Sum: $(x + a)^2$",
        "topic": "Algebraic expressions 2",
        "grade": 8,
        "term": 2,
        "subskill": "17_squaring_binomial_sum",
        "difficulty": "medium",
        "question_text": (
            f"Expand and simplify:\n\n"
            f"$$(x + {a})^2$$"
        ),
        "correct_answer": f"x^2 + {mid}x + {sq}",
        "marking_schema": [
            f"Rewrite as (x + {a})(x + {a}) and expand: x^2 + {a}x + {a}x + {sq} [1 mark]",
            f"Final trinomial: x^2 + {mid}x + {sq} [1 mark]",
        ],
        "hints": [
            f"$(x + {a})^2 = (x + {a})(x + {a})$.",
            f"Middle term is $2 \\times a \\times x = {mid}x$.",
            f"Last term is ${a}^2 = {sq}$.",
        ],
        "misconception_tags": ["binomial_squaring_middle_term_drop"],
        "diagram_spec": None,
    }


def arch_18_squaring_binomial_difference(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(2, 8)
    mid = 2 * a
    sq = a ** 2

    return {
        "title": "Squaring a Binomial Difference: $(x - a)^2$",
        "topic": "Algebraic expressions 2",
        "grade": 8,
        "term": 2,
        "subskill": "18_squaring_binomial_difference",
        "difficulty": "medium",
        "question_text": (
            f"Expand and simplify:\n\n"
            f"$$(x - {a})^2$$"
        ),
        "correct_answer": f"x^2 - {mid}x + {sq}",
        "marking_schema": [
            f"Rewrite as (x - {a})(x - {a}) [1 mark]",
            f"Trinomial result: x^2 - {mid}x + {sq} [1 mark]",
        ],
        "hints": [
            f"$(x - {a})^2 = (x - {a})(x - {a})$.",
            f"Middle term is $-2 \\times a \\times x = -{mid}x$.",
            f"Last term is $(-{a})^2 = +{sq}$.",
        ],
        "misconception_tags": ["binomial_difference_squaring_error"],
        "diagram_spec": None,
    }


def arch_19_diagnosing_binomial_squaring_error(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([3, 4, 5])
    return {
        "title": "Diagnosing Binomial Squaring Misconceptions",
        "topic": "Algebraic expressions 2",
        "grade": 8,
        "term": 2,
        "subskill": "19_diagnosing_binomial_squaring_error",
        "difficulty": "medium",
        "question_text": (
            f"A learner wrote that $$(x + {a})^2 = x^2 + {a**2}$$\n\n"
            "Explain why this statement is mathematically incorrect and write down the **correct expansion**."
        ),
        "correct_answer": f"The learner forgot to expand (x + {a})(x + {a}) using FOIL, which produces the middle term 2({a})x = {2*a}x. The correct expansion is x^2 + {2*a}x + {a**2}.",
        "marking_schema": [
            f"Explain omission of the middle cross-product term ({2*a}x) [1 mark]",
            f"Provide correct trinomial: x^2 + {2*a}x + {a**2} [1 mark]",
        ],
        "hints": [
            f"Remember $(x + {a})^2$ means $(x + {a})(x + {a})$.",
            f"The outer and inner terms give ${a}x + {a}x = {2*a}x$.",
            f"The correct expansion is $x^2 + {2*a}x + {a**2}$.",
        ],
        "misconception_tags": ["freshman_dream_algebraic_fallacy"],
        "diagram_spec": None,
    }


def arch_20_product_of_sum_and_difference(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(2, 9)
    sq = a ** 2

    return {
        "title": "Expanding Product of Sum and Difference: $(x + a)(x - a)$",
        "topic": "Algebraic expressions 2",
        "grade": 8,
        "term": 2,
        "subskill": "20_product_of_sum_and_difference",
        "difficulty": "medium",
        "question_text": (
            f"Expand and simplify the product:\n\n"
            f"$$(x + {a})(x - {a})$$"
        ),
        "correct_answer": f"x^2 - {sq}",
        "marking_schema": [
            f"Show outer and inner terms cancel: +{a}x - {a}x = 0 [1 mark]",
            f"Final difference of squares: x^2 - {sq} [1 mark]",
        ],
        "hints": [
            f"Notice that the two binomials are conjugates (identical terms with opposite signs).",
            f"Outer term = -{a}x; Inner term = +{a}x.",
            f"They cancel out, leaving $x^2 - {sq}$.",
        ],
        "misconception_tags": ["difference_of_squares_expansion_error"],
        "diagram_spec": None,
    }


def arch_21_dividing_binomial_by_numerical_monomial(rng: random.Random) -> Dict[str, Any]:
    c = rng.choice([2, 3, 4, 5])
    m = rng.randint(2, 5)
    n = rng.randint(2, 6)
    a = m * c
    b = n * c

    return {
        "title": "Dividing a Binomial by a Numerical Monomial",
        "topic": "Algebraic expressions 2",
        "grade": 8,
        "term": 2,
        "subskill": "21_dividing_binomial_by_numerical_monomial",
        "difficulty": "medium",
        "question_text": (
            f"Simplify the algebraic fraction by dividing each term in the numerator by the denominator:\n\n"
            f"$$\\frac{{{a}x + {b}}}{{{c}}}$$"
        ),
        "correct_answer": f"{m}x + {n}",
        "marking_schema": [
            f"Divide first term: ({a}x)/{c} = {m}x [1 mark]",
            f"Divide second term: {b}/{c} = {n} yielding {m}x + {n} [1 mark]",
        ],
        "hints": [
            f"Split into two fractions: $\\frac{{{a}x}}{{{c}}} + \\frac{{{b}}}{{{c}}}$.",
            f"{a} ÷ {c} = {m}.",
            f"{b} ÷ {c} = {n}.",
        ],
        "misconception_tags": ["partial_fraction_division_error"],
        "diagram_spec": None,
    }


def arch_22_dividing_binomial_by_variable_monomial(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(2, 7)
    b = rng.randint(3, 9)

    return {
        "title": "Dividing a Binomial by a Variable ($x$)",
        "topic": "Algebraic expressions 2",
        "grade": 8,
        "term": 2,
        "subskill": "22_dividing_binomial_by_variable_monomial",
        "difficulty": "medium",
        "question_text": (
            f"Simplify the algebraic fraction:\n\n"
            f"$$\\frac{{{a}x^2 + {b}x}}{{x}}$$"
        ),
        "correct_answer": f"{a}x + {b}",
        "marking_schema": [
            f"Divide {a}x^2 by x: {a}x [1 mark]",
            f"Divide {b}x by x: {b} yielding {a}x + {b} [1 mark]",
        ],
        "hints": [
            f"Split the numerator: $\\frac{{{a}x^2}}{{x}} + \\frac{{{b}x}}{{x}}$.",
            f"$x^2 ÷ x = x$.",
            f"$x ÷ x = 1$.",
        ],
        "misconception_tags": ["variable_cancellation_remainder_error"],
        "diagram_spec": None,
    }


def arch_23_dividing_trinomial_by_variable_monomial(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(2, 5)
    b = rng.randint(2, 6)
    c = rng.randint(3, 8)

    return {
        "title": "Dividing a Trinomial by a Variable ($x$)",
        "topic": "Algebraic expressions 2",
        "grade": 8,
        "term": 2,
        "subskill": "23_dividing_trinomial_by_variable_monomial",
        "difficulty": "medium",
        "question_text": (
            f"Simplify completely:\n\n"
            f"$$\\frac{{{a}x^3 + {b}x^2 - {c}x}}{{x}}$$"
        ),
        "correct_answer": f"{a}x^2 + {b}x - {c}",
        "marking_schema": [
            f"Divide each term by x: {a}x^2 + {b}x - {c} [2 marks]",
        ],
        "hints": [
            f"Divide each term in the numerator by $x$.",
            f"${a}x^3 ÷ x = {a}x^2$.",
            f"${b}x^2 ÷ x = {b}x$.",
            f"-{c}x ÷ x = -{c}.",
        ],
        "misconception_tags": ["polynomial_division_power_reduction_error"],
        "diagram_spec": None,
    }


def arch_24_dividing_polynomial_by_signed_monomial(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(2, 6)
    b = rng.randint(3, 8)

    return {
        "title": "Dividing a Binomial by a Negative Variable ($-x$)",
        "topic": "Algebraic expressions 2",
        "grade": 8,
        "term": 2,
        "subskill": "24_dividing_polynomial_by_signed_monomial",
        "difficulty": "hard",
        "question_text": (
            f"Simplify the algebraic fraction:\n\n"
            f"$$\\frac{{{a}x^2 - {b}x}}{{-x}}$$"
        ),
        "correct_answer": f"-{a}x + {b}",
        "marking_schema": [
            f"Divide {a}x^2 by -x: -{a}x [1 mark]",
            f"Divide -{b}x by -x: +{b} yielding -{a}x + {b} [1 mark]",
        ],
        "hints": [
            f"Divide each term by -x.",
            f"Positive divided by negative is negative: ${a}x^2 ÷ (-x) = -{a}x$.",
            f"Negative divided by negative is positive: (-{b}x) ÷ (-x) = +{b}.",
        ],
        "misconception_tags": ["division_by_negative_variable_sign_error"],
        "diagram_spec": None,
    }


def arch_25_dividing_polynomial_by_monomial_with_coefficient(rng: random.Random) -> Dict[str, Any]:
    c = rng.choice([2, 3, 4])
    m = rng.randint(2, 4)
    n = rng.randint(2, 5)
    a = m * c
    b = n * c

    return {
        "title": "Dividing a Binomial by a Monomial with Coefficient ($cx$)",
        "topic": "Algebraic expressions 2",
        "grade": 8,
        "term": 2,
        "subskill": "25_dividing_polynomial_by_monomial_with_coefficient",
        "difficulty": "medium",
        "question_text": (
            f"Simplify the following fraction:\n\n"
            f"$$\\frac{{{a}x^2 + {b}x}}{{{c}x}}$$"
        ),
        "correct_answer": f"{m}x + {n}",
        "marking_schema": [
            f"Divide coefficients and powers: ({a}x^2)/({c}x) = {m}x [1 mark]",
            f"Divide second term: ({b}x)/({c}x) = {n} yielding {m}x + {n} [1 mark]",
        ],
        "hints": [
            f"Split the fraction: $\\frac{{{a}x^2}}{{{c}x}} + \\frac{{{b}x}}{{{c}x}}$.",
            f"{a} ÷ {c} = {m} and $x^2 ÷ x = x$.",
            f"{b} ÷ {c} = {n} and $x ÷ x = 1$.",
        ],
        "misconception_tags": ["monomial_denominator_coefficient_error"],
        "diagram_spec": None,
    }


BUILDERS_01_25 = [
    arch_01_distributive_law_positive_monomial_binomial_sum,
    arch_02_distributive_law_positive_monomial_binomial_difference,
    arch_03_distributive_law_negative_monomial_binomial_sum,
    arch_04_distributive_law_negative_monomial_binomial_difference,
    arch_05_distributive_law_variable_multiplier,
    arch_06_distributive_law_variable_multiplier_with_negative,
    arch_07_distributive_law_monomial_with_variable_and_coefficient,
    arch_08_distributive_law_monomial_with_variable_and_negative_coefficient,
    arch_09_distributive_law_monomial_times_trinomial,
    arch_10_distributive_law_negative_monomial_times_trinomial,
    arch_11_expanding_and_simplifying_sum_of_two_distributed_brackets,
    arch_12_expanding_and_simplifying_difference_of_two_distributed_brackets,
    arch_13_expanding_and_simplifying_variable_brackets_with_like_terms,
    arch_14_expanding_binomial_product_positive_terms,
    arch_15_expanding_binomial_product_mixed_signs,
    arch_16_expanding_binomial_product_both_negative,
    arch_17_squaring_binomial_sum,
    arch_18_squaring_binomial_difference,
    arch_19_diagnosing_binomial_squaring_error,
    arch_20_product_of_sum_and_difference,
    arch_21_dividing_binomial_by_numerical_monomial,
    arch_22_dividing_binomial_by_variable_monomial,
    arch_23_dividing_trinomial_by_variable_monomial,
    arch_24_dividing_polynomial_by_signed_monomial,
    arch_25_dividing_polynomial_by_monomial_with_coefficient,
]
