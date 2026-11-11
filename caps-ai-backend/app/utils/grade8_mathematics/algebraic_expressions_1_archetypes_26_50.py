"""
Grade 8 Mathematics - Algebraic Expressions 1 Archetypes (26 to 50).
100% CAPS-aligned deterministic question generators.
Adheres strictly to the 6-Pillar Generator Contract and Zero-Meta-Curriculum Invariant.
Grounded in curriculum_docs_auto/Mathematics_Gr8/Term 2/01. Algebraic expressions 1.md.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from app.utils.grade8_mathematics.svg_diagrams import draw_algebraic_shape_perimeter_svg


def arch_26_perimeter_of_equilateral_triangle_in_terms_of_x(rng: random.Random) -> Dict[str, Any]:
    seed = rng.randint(1, 1000000)
    a = rng.randint(2, 5)
    b = rng.randint(1, 6)
    side_expr = f"{a}x + {b}"
    p_a = 3 * a
    p_b = 3 * b

    svg = draw_algebraic_shape_perimeter_svg(
        shape_type="triangle",
        side_labels=[side_expr, side_expr, side_expr],
        title="Equilateral Triangle",
        seed=seed,
    )

    return {
        "title": "Perimeter of an Equilateral Triangle in Terms of x",
        "topic": "Algebraic expressions 1",
        "grade": 8,
        "term": 2,
        "subskill": "26_perimeter_of_equilateral_triangle_in_terms_of_x",
        "difficulty": "medium",
        "question_text": (
            f"An equilateral triangle has each side of length **$({side_expr})\\text{{ cm}}$**.\n\n"
            "Write a simplified algebraic expression in terms of $x$ for the **perimeter** of the triangle."
        ),
        "correct_answer": f"({p_a}x + {p_b}) cm",
        "marking_schema": [
            f"Multiply side by 3: 3({side_expr}) [1 mark]",
            f"Expand and simplify: {p_a}x + {p_b} [1 mark]",
        ],
        "hints": [
            "An equilateral triangle has 3 sides of equal length.",
            f"Perimeter = 3 x ({side_expr}).",
            f"Distribute 3: 3 x {a}x + 3 x {b} = {p_a}x + {p_b}.",
        ],
        "misconception_tags": ["perimeter_distributive_omission"],
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    }


def arch_27_perimeter_of_rectangle_in_terms_of_x(rng: random.Random) -> Dict[str, Any]:
    seed = rng.randint(1, 1000000)
    a = rng.randint(2, 4)
    b = rng.randint(1, 5)
    c = rng.randint(1, 3)
    d = rng.randint(1, 4)

    len_expr = f"{a}x + {b}"
    br_expr = f"{c}x + {d}"

    p_x = 2 * (a + c)
    p_const = 2 * (b + d)

    svg = draw_algebraic_shape_perimeter_svg(
        shape_type="rectangle",
        side_labels=[len_expr, br_expr, len_expr, br_expr],
        title="Rectangle Dimensions",
        seed=seed,
    )

    return {
        "title": "Perimeter of a Rectangle in Terms of x",
        "topic": "Algebraic expressions 1",
        "grade": 8,
        "term": 2,
        "subskill": "27_perimeter_of_rectangle_in_terms_of_x",
        "difficulty": "medium",
        "question_text": (
            f"A rectangular vegetable garden has length **$({len_expr})\\text{{ m}}$** "
            f"and breadth **$({br_expr})\\text{{ m}}$**.\n\n"
            "Determine the simplified algebraic expression for the **perimeter** of the garden."
        ),
        "correct_answer": f"({p_x}x + {p_const}) m",
        "marking_schema": [
            f"Formula P = 2(length + breadth): 2[({len_expr}) + ({br_expr})] [1 mark]",
            f"Combine like terms and expand: {p_x}x + {p_const} [1 mark]",
        ],
        "hints": [
            "Perimeter of a rectangle = 2(length + breadth).",
            f"Add length and breadth: ({a}x + {b}) + ({c}x + {d}) = {a + c}x + {b + d}.",
            f"Double the sum: 2({a + c}x + {b + d}) = {p_x}x + {p_const}.",
        ],
        "misconception_tags": ["rectangle_perimeter_formula_error"],
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    }


def arch_28_perimeter_of_scalene_triangle_combining_like_terms(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(2, 4)
    b = rng.randint(1, 5)
    c = rng.randint(1, 3)
    d = rng.randint(1, 4)
    e = rng.randint(2, 4)
    f = rng.randint(1, 6)

    s1 = f"{a}x + {b}"
    s2 = f"{c}x - {d}"
    s3 = f"{e}x + {f}"

    tot_x = a + c + e
    tot_const = b - d + f
    sign = "+" if tot_const >= 0 else "-"
    abs_const = abs(tot_const)

    return {
        "title": "Perimeter of a Scalene Triangle (Combining Like Terms)",
        "topic": "Algebraic expressions 1",
        "grade": 8,
        "term": 2,
        "subskill": "28_perimeter_of_scalene_triangle_combining_like_terms",
        "difficulty": "medium",
        "question_text": (
            f"The three sides of a triangle measure **$({s1})\\text{{ cm}}$**, "
            f"**$({s2})\\text{{ cm}}$**, and **$({s3})\\text{{ cm}}$**.\n\n"
            "Find the simplified expression for the perimeter of the triangle."
        ),
        "correct_answer": f"{tot_x}x {sign} {abs_const} cm",
        "marking_schema": [
            f"Add all three side expressions: ({s1}) + ({s2}) + ({s3}) [1 mark]",
            f"Combine $x$ terms and constants: {tot_x}x {sign} {abs_const} [1 mark]",
        ],
        "hints": [
            "Perimeter is the sum of all three outer sides.",
            f"Add $x$ coefficients: {a} + {c} + {e} = {tot_x}.",
            f"Add constant terms: {b} - {d} + {f} = {tot_const}.",
        ],
        "misconception_tags": ["triangle_perimeter_sign_error"],
        "diagram_spec": None,
    }


def arch_29_perimeter_of_square_in_terms_of_x(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(2, 6)
    b = rng.randint(2, 7)
    side_expr = f"{a}x - {b}"
    p_x = 4 * a
    p_const = 4 * b

    return {
        "title": "Perimeter of a Square in Terms of x",
        "topic": "Algebraic expressions 1",
        "grade": 8,
        "term": 2,
        "subskill": "29_perimeter_of_square_in_terms_of_x",
        "difficulty": "easy",
        "question_text": (
            f"A square has side length **$({side_expr})\\text{{ cm}}$**.\n\n"
            "Write a simplified algebraic expression for its **perimeter**."
        ),
        "correct_answer": f"({p_x}x - {p_const}) cm",
        "marking_schema": [
            f"Multiply side by 4: 4({side_expr}) [1 mark]",
            f"Expand: {p_x}x - {p_const} [1 mark]",
        ],
        "hints": [
            "All four sides of a square are equal.",
            f"Perimeter = 4 x ({side_expr}).",
            f"4 x {a}x - 4 x {b} = {p_x}x - {p_const}.",
        ],
        "misconception_tags": ["square_perimeter_expansion_error"],
        "diagram_spec": None,
    }


def arch_30_translating_consecutive_integers_to_algebra(rng: random.Random) -> Dict[str, Any]:
    return {
        "title": "Expressing Consecutive Integers and Their Sum",
        "topic": "Algebraic expressions 1",
        "grade": 8,
        "term": 2,
        "subskill": "30_translating_consecutive_integers_to_algebra",
        "difficulty": "medium",
        "question_text": (
            "Let $n$ represent any integer.\n\n"
            "1. Write algebraic expressions for the **next two consecutive integers**.\n"
            "2. Write and simplify an expression for the **sum** of all three consecutive integers."
        ),
        "correct_answer": "1. n + 1 and n + 2. 2. 3n + 3.",
        "marking_schema": [
            "Next two integers: n + 1 and n + 2 [1 mark]",
            "Sum simplified: n + (n + 1) + (n + 2) = 3n + 3 [1 mark]",
        ],
        "hints": [
            "Consecutive integers increase by 1 each time.",
            "If the first is $n$, the next two are $n + 1$ and $n + 2$.",
            "Add all three: $n + n + 1 + n + 2 = 3n + 3$.",
        ],
        "misconception_tags": ["consecutive_integer_representation_error"],
        "diagram_spec": None,
    }


def arch_31_translating_consecutive_even_integers(rng: random.Random) -> Dict[str, Any]:
    return {
        "title": "Expressing Consecutive Even Integers and Their Sum",
        "topic": "Algebraic expressions 1",
        "grade": 8,
        "term": 2,
        "subskill": "31_translating_consecutive_even_integers",
        "difficulty": "medium",
        "question_text": (
            "Let $2n$ represent an even integer.\n\n"
            "1. Write expressions for the **next two consecutive even integers**.\n"
            "2. Determine the simplified expression for the **sum** of these three even integers."
        ),
        "correct_answer": "1. 2n + 2 and 2n + 4. 2. 6n + 6.",
        "marking_schema": [
            "Next two even integers: 2n + 2 and 2n + 4 [1 mark]",
            "Sum simplified: 2n + (2n + 2) + (2n + 4) = 6n + 6 [1 mark]",
        ],
        "hints": [
            "Consecutive even numbers increase by 2 (e.g. 2, 4, 6).",
            "The next two even integers are $2n + 2$ and $2n + 4$.",
            "Add: $2n + 2n + 2 + 2n + 4 = 6n + 6$.",
        ],
        "misconception_tags": ["even_consecutive_step_size_error"],
        "diagram_spec": None,
    }


def arch_32_translating_age_word_problem_to_expression(rng: random.Random) -> Dict[str, Any]:
    mult = rng.choice([3, 4, 5])
    years = rng.randint(4, 9)
    return {
        "title": "Translating Age Relationships into Algebraic Expressions",
        "topic": "Algebraic expressions 1",
        "grade": 8,
        "term": 2,
        "subskill": "32_translating_age_word_problem_to_expression",
        "difficulty": "medium",
        "question_text": (
            f"Lindiwe is $x$ years old. Her mother is currently **{mult} times** as old as Lindiwe.\n\n"
            f"Write an algebraic expression in terms of $x$ for her mother's age in **{years} years' time**."
        ),
        "correct_answer": f"{mult}x + {years}",
        "marking_schema": [
            f"Mother's current age: {mult}x [1 mark]",
            f"Mother's age in {years} years: {mult}x + {years} [1 mark]",
        ],
        "hints": [
            f"Lindiwe is $x$, so her mother is currently {mult}x.",
            f"In {years} years, everyone will be {years} years older.",
            f"Add {years} to the mother's current age: {mult}x + {years}.",
        ],
        "misconception_tags": ["age_translation_bracket_confusion"],
        "diagram_spec": None,
    }


def arch_33_translating_taxi_fare_to_expression(rng: random.Random) -> Dict[str, Any]:
    base = rng.choice([15, 20, 25])
    rate = rng.choice([8, 10, 12])
    return {
        "title": "Translating Real-World Transport Cost into an Algebraic Expression",
        "topic": "Algebraic expressions 1",
        "grade": 8,
        "term": 2,
        "subskill": "33_translating_taxi_fare_to_expression",
        "difficulty": "easy",
        "question_text": (
            f"A minibus taxi charges a boarding base fare of **R{base}** plus **R{rate} per kilometre** travelled.\n\n"
            f"Write an algebraic expression for the total fare in Rands for a trip of **$k$ kilometres**."
        ),
        "correct_answer": f"R({base} + {rate}k)",
        "marking_schema": [
            f"Variable distance cost: {rate}k [1 mark]",
            f"Include base fare: {base} + {rate}k [1 mark]",
        ],
        "hints": [
            f"For 1 km, the distance cost is R{rate} x 1.",
            f"For $k$ km, the distance cost is R{rate}k.",
            f"Add the fixed base fare of R{base}: {base} + {rate}k.",
        ],
        "misconception_tags": ["fixed_vs_variable_cost_confusion"],
        "diagram_spec": None,
    }


def arch_34_simplifying_expression_with_parentheses_addition(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(2, 6)
    b = rng.randint(3, 9)
    c = rng.randint(2, 5)
    d = rng.randint(2, 8)
    tot_x = a + c
    tot_const = b + d

    return {
        "title": "Simplifying Algebraic Addition of Binomials",
        "topic": "Algebraic expressions 1",
        "grade": 8,
        "term": 2,
        "subskill": "34_simplifying_expression_with_parentheses_addition",
        "difficulty": "easy",
        "question_text": (
            f"Simplify the following expression:\n\n"
            f"$$({a}x + {b}) + ({c}x + {d})$$"
        ),
        "correct_answer": f"{tot_x}x + {tot_const}",
        "marking_schema": [
            f"Add $x$ coefficients: {a} + {c} = {tot_x}x [1 mark]",
            f"Add constants: {b} + {d} = {tot_const} [1 mark]",
        ],
        "hints": [
            "With addition between brackets, remove the parentheses directly.",
            f"Group like terms: ({a}x + {c}x) + ({b} + {d}).",
            f"Result = {tot_x}x + {tot_const}.",
        ],
        "misconception_tags": ["parentheses_addition_error"],
        "diagram_spec": None,
    }


def arch_35_simplifying_expression_with_parentheses_subtraction(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(5, 9)
    b = rng.randint(3, 8)
    c = rng.randint(2, 4)
    d = rng.randint(2, 6)
    tot_x = a - c
    tot_const = b + d  # (b - (-d)) = b + d

    return {
        "title": "Simplifying Algebraic Subtraction of Binomials (Distributing Negative Sign)",
        "topic": "Algebraic expressions 1",
        "grade": 8,
        "term": 2,
        "subskill": "35_simplifying_expression_with_parentheses_subtraction",
        "difficulty": "hard",
        "question_text": (
            f"Simplify the expression by removing brackets and collecting like terms:\n\n"
            f"$$({a}x + {b}) - ({c}x - {d})$$"
        ),
        "correct_answer": f"{tot_x}x + {tot_const}",
        "marking_schema": [
            f"Distribute negative sign: -({c}x - {d}) = -{c}x + {d} [1 mark]",
            f"Combine like terms: {tot_x}x + {tot_const} [1 mark]",
        ],
        "hints": [
            "Be very careful when subtracting a bracket: distribute the minus sign to EVERY term inside.",
            f"-({c}x - {d}) becomes -{c}x + {d}.",
            f"Combine: ({a}x - {c}x) + ({b} + {d}) = {tot_x}x + {tot_const}.",
        ],
        "misconception_tags": ["bracket_subtraction_sign_distribution_error"],
        "diagram_spec": None,
    }


def arch_36_identifying_sign_error_in_subtraction_of_binomial(rng: random.Random) -> Dict[str, Any]:
    a = 5
    b = 3
    c = 2
    d = 4
    wrong_const = b - d  # -1 instead of +7
    correct_const = b + d  # +7

    return {
        "title": "Diagnosing Common Errors: Subtraction Across Parentheses",
        "topic": "Algebraic expressions 1",
        "grade": 8,
        "term": 2,
        "subskill": "36_identifying_sign_error_in_subtraction_of_binomial",
        "difficulty": "medium",
        "question_text": (
            "A learner simplified $(5x + 3) - (2x - 4)$ and obtained $3x - 1$.\n\n"
            "Identify the learner's error and write down the **correct simplified expression**."
        ),
        "correct_answer": "The learner only subtracted the first term (2x) and failed to change the sign of -4 to +4 (since -(-4) = +4). The correct simplified expression is 3x + 7.",
        "marking_schema": [
            "Identify that -(-4) must become +4 (sign error on constant) [1 mark]",
            "Provide correct answer: 3x + 7 [1 mark]",
        ],
        "hints": [
            "Look at the constant terms: 3 - (-4).",
            "Subtracting a negative number is equivalent to adding: 3 + 4 = 7.",
            "The correct expression is 3x + 7.",
        ],
        "misconception_tags": ["minus_times_minus_parentheses_error"],
        "diagram_spec": None,
    }


def arch_37_combining_cubed_and_squared_terms(rng: random.Random) -> Dict[str, Any]:
    a1 = rng.randint(3, 7)
    a2 = rng.randint(1, 3)
    b1 = rng.randint(2, 6)
    b2 = rng.randint(1, 4)
    tot_cube = a1 - a2
    tot_sq = b1 + b2

    return {
        "title": "Combining Higher Order Like Terms (Cubed and Squared)",
        "topic": "Algebraic expressions 1",
        "grade": 8,
        "term": 2,
        "subskill": "37_combining_cubed_and_squared_terms",
        "difficulty": "medium",
        "question_text": (
            f"Simplify the following algebraic expression:\n\n"
            f"$${a1}x^3 + {b1}x^2 - {a2}x^3 + {b2}x^2$$"
        ),
        "correct_answer": f"{tot_cube}x^3 + {tot_sq}x^2",
        "marking_schema": [
            f"Combine $x^3$ terms: ({a1} - {a2})x^3 = {tot_cube}x^3 [1 mark]",
            f"Combine $x^2$ terms: ({b1} + {b2})x^2 = {tot_sq}x^2 [1 mark]",
        ],
        "hints": [
            f"Group like terms together: ({a1}x^3 - {a2}x^3) + ({b1}x^2 + {b2}x^2).",
            f"Combine $x^3$ terms: {tot_cube}x^3.",
            f"Combine $x^2$ terms: {tot_sq}x^2.",
        ],
        "misconception_tags": ["higher_order_power_confusion"],
        "diagram_spec": None,
    }


def arch_38_writing_expression_for_shaded_area_difference(rng: random.Random) -> Dict[str, Any]:
    p1 = rng.randint(8, 12)
    p2 = rng.randint(3, 6)
    c1 = rng.randint(5, 10)
    c2 = rng.randint(1, 4)
    diff_x = p1 - p2
    diff_const = c1 - c2

    return {
        "title": "Expressing Differences in Perimeter Between Two Shapes",
        "topic": "Algebraic expressions 1",
        "grade": 8,
        "term": 2,
        "subskill": "38_writing_expression_for_shaded_area_difference",
        "difficulty": "medium",
        "question_text": (
            f"Shape A has a perimeter of **$({p1}x + {c1})\\text{{ cm}}$**.\n"
            f"Shape B has a perimeter of **$({p2}x + {c2})\\text{{ cm}}$**.\n\n"
            "Write a simplified algebraic expression for how much larger Shape A's perimeter is than Shape B's perimeter."
        ),
        "correct_answer": f"({diff_x}x + {diff_const}) cm",
        "marking_schema": [
            f"Set up subtraction: ({p1}x + {c1}) - ({p2}x + {c2}) [1 mark]",
            f"Simplify: {diff_x}x + {diff_const} [1 mark]",
        ],
        "hints": [
            f"Subtract Shape B from Shape A: ({p1}x + {c1}) - ({p2}x + {c2}).",
            f"Subtract $x$ terms: {p1}x - {p2}x = {diff_x}x.",
            f"Subtract constants: {c1} - {c2} = {diff_const}.",
        ],
        "misconception_tags": ["geometric_difference_expression_error"],
        "diagram_spec": None,
    }


def arch_39_writing_expression_for_total_cost_items(rng: random.Random) -> Dict[str, Any]:
    p_pen = rng.choice([5, 6, 8])
    p_book = rng.choice([12, 15, 20])
    return {
        "title": "Writing Algebraic Expression for Multi-Item Shopping Cost",
        "topic": "Algebraic expressions 1",
        "grade": 8,
        "term": 2,
        "subskill": "39_writing_expression_for_total_cost_items",
        "difficulty": "easy",
        "question_text": (
            f"At a stationery shop, ballpoint pens cost **R{p_pen} each** and exercise books cost **R{p_book} each**.\n\n"
            f"Write an algebraic expression in Rands for the total cost of buying **$x$ pens** and **$y$ exercise books**."
        ),
        "correct_answer": f"R({p_pen}x + {p_book}y)",
        "marking_schema": [
            f"Cost of pens: {p_pen}x [1 mark]",
            f"Cost of books: {p_book}y yielding total {p_pen}x + {p_book}y [1 mark]",
        ],
        "hints": [
            f"Cost for $x$ pens = R{p_pen} x $x$.",
            f"Cost for $y$ books = R{p_book} x $y$.",
            f"Total cost = {p_pen}x + {p_book}y.",
        ],
        "misconception_tags": ["two_variable_cost_modeling_error"],
        "diagram_spec": None,
    }


def arch_40_simplifying_fractions_with_monomial_denominator(rng: random.Random) -> Dict[str, Any]:
    factor = rng.choice([2, 3, 4, 5])
    a_mult = rng.choice([2, 3, 4])
    b_mult = rng.choice([3, 5, 6])
    c1 = a_mult * factor
    c2 = b_mult * factor
    tot_mult = a_mult + b_mult

    return {
        "title": "Simplifying Algebraic Fractions with a Monomial Denominator",
        "topic": "Algebraic expressions 1",
        "grade": 8,
        "term": 2,
        "subskill": "40_simplifying_fractions_with_monomial_denominator",
        "difficulty": "medium",
        "question_text": (
            f"Simplify the algebraic fraction by first combining like terms in the numerator:\n\n"
            f"$$\\frac{{{c1}x + {c2}x}}{{{factor}}}$$"
        ),
        "correct_answer": f"{tot_mult}x",
        "marking_schema": [
            f"Combine numerator: {c1}x + {c2}x = {c1 + c2}x [1 mark]",
            f"Divide by {factor}: ({c1 + c2}x)/{factor} = {tot_mult}x [1 mark]",
        ],
        "hints": [
            f"First add the terms in the numerator: {c1}x + {c2}x = {c1 + c2}x.",
            f"Divide {c1 + c2} by {factor}.",
            f"Result = {tot_mult}x.",
        ],
        "misconception_tags": ["fractional_cancellation_numerator_error"],
        "diagram_spec": None,
    }


def arch_41_evaluating_two_variable_expression(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(2, 5)
    b = rng.randint(2, 6)
    x_val = rng.randint(2, 5)
    y_val = rng.randint(2, 5)
    ans = a * x_val + b * y_val

    return {
        "title": "Evaluating a Two-Variable Linear Expression",
        "topic": "Algebraic expressions 1",
        "grade": 8,
        "term": 2,
        "subskill": "41_evaluating_two_variable_expression",
        "difficulty": "medium",
        "question_text": (
            f"Calculate the numerical value of **${a}x + {b}y$** when **$x = {x_val}$** and **$y = {y_val}$**."
        ),
        "correct_answer": str(ans),
        "marking_schema": [
            f"Substitute values: {a}({x_val}) + {b}({y_val}) = {a * x_val} + {b * y_val} [1 mark]",
            f"Simplify: {ans} [1 mark]",
        ],
        "hints": [
            f"Replace $x$ with {x_val} and $y$ with {y_val}.",
            f"{a} x {x_val} = {a * x_val}.",
            f"{b} x {y_val} = {b * y_val}.",
            f"Add them: {a * x_val} + {b * y_val} = {ans}.",
        ],
        "misconception_tags": ["two_variable_substitution_cross_confusion"],
        "diagram_spec": None,
    }


def arch_42_evaluating_two_variable_expression_with_negatives(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(2, 5)
    b = rng.randint(2, 4)
    x_val = -rng.randint(2, 4)
    y_val = -rng.randint(2, 5)
    ans = a * x_val - b * y_val

    return {
        "title": "Evaluating a Two-Variable Expression with Negative Integers",
        "topic": "Algebraic expressions 1",
        "grade": 8,
        "term": 2,
        "subskill": "42_evaluating_two_variable_expression_with_negatives",
        "difficulty": "hard",
        "question_text": (
            f"Find the numerical value of **${a}x - {b}y$** when **$x = {x_val}$** and **$y = {y_val}$**."
        ),
        "correct_answer": str(ans),
        "marking_schema": [
            f"Substitute negative values: {a}({x_val}) - {b}({y_val}) = {a * x_val} - ({b * y_val}) [1 mark]",
            f"Simplify signs: {a * x_val} + {abs(b * y_val)} = {ans} [1 mark]",
        ],
        "hints": [
            f"{a} x ({x_val}) = {a * x_val}.",
            f"-{b} x ({y_val}) = +{abs(b * y_val)}.",
            f"Combine: {a * x_val} + {abs(b * y_val)} = {ans}.",
        ],
        "misconception_tags": ["two_variable_negative_sign_error"],
        "diagram_spec": None,
    }


def arch_43_finding_missing_term_to_make_expressions_equivalent(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(2, 5)
    b = rng.randint(3, 8)
    diff = rng.randint(3, 7)
    target_a = a + diff

    return {
        "title": "Finding a Missing Term to Establish Algebraic Equivalence",
        "topic": "Algebraic expressions 1",
        "grade": 8,
        "term": 2,
        "subskill": "43_finding_missing_term_to_make_expressions_equivalent",
        "difficulty": "medium",
        "question_text": (
            f"What term must be added to **${a}x + {b}$** to make it equivalent to **${target_a}x + {b}$**?"
        ),
        "correct_answer": f"{diff}x",
        "marking_schema": [
            f"Subtract expressions: ({target_a}x + {b}) - ({a}x + {b}) [1 mark]",
            f"Correct missing term: {diff}x [1 mark]",
        ],
        "hints": [
            f"Notice that the constant {b} is already the same in both expressions.",
            f"How many more $x$'s are needed to go from {a}x to {target_a}x?",
            f"{target_a} - {a} = {diff}, so add {diff}x.",
        ],
        "misconception_tags": ["additive_equivalence_gap"],
        "diagram_spec": None,
    }


def arch_44_translating_geometric_pattern_to_algebraic_expression(rng: random.Random) -> Dict[str, Any]:
    diff = rng.choice([3, 4, 5])
    c = rng.choice([1, 2])
    # Pattern: stage 1 = diff + c, stage 2 = 2*diff + c, etc.
    t1 = diff + c
    t2 = 2 * diff + c
    t3 = 3 * diff + c

    return {
        "title": "Generalising a Linear Matchstick Pattern to an Algebraic Rule",
        "topic": "Algebraic expressions 1",
        "grade": 8,
        "term": 2,
        "subskill": "44_translating_geometric_pattern_to_algebraic_expression",
        "difficulty": "medium",
        "question_text": (
            "A geometric pattern of matchstick figures has the following number of matches:\n\n"
            f"- Stage 1: **{t1} matches**\n"
            f"- Stage 2: **{t2} matches**\n"
            f"- Stage 3: **{t3} matches**\n\n"
            "Write an algebraic rule for the number of matches $T_n$ in **Stage $n$**."
        ),
        "correct_answer": f"T_n = {diff}n + {c}",
        "marking_schema": [
            f"Identify common difference d = {diff} [1 mark]",
            f"Determine constant c = {c} yielding T_n = {diff}n + {c} [1 mark]",
        ],
        "hints": [
            f"Find the constant difference between consecutive stages: {t2} - {t1} = {diff}.",
            f"The rule starts with {diff}n.",
            f"Check Stage 1: {diff}(1) + c = {t1} => c = {c}.",
            f"Rule: $T_n = {diff}n + {c}$.",
        ],
        "misconception_tags": ["pattern_to_formula_constant_error"],
        "diagram_spec": None,
    }


def arch_45_descending_powers_arrangement_polynomial(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(2, 6)
    b = rng.randint(3, 8)
    c = rng.randint(2, 5)
    d = rng.randint(4, 9)

    unordered = f"{b}x - {d} + {a}x^3 - {c}x^2"
    ordered = f"{a}x^3 - {c}x^2 + {b}x - {d}"

    return {
        "title": "Arranging a Polynomial in Descending Powers of the Variable",
        "topic": "Algebraic expressions 1",
        "grade": 8,
        "term": 2,
        "subskill": "45_descending_powers_arrangement_polynomial",
        "difficulty": "easy",
        "question_text": (
            f"Write the following expression in **descending powers of $x$**:\n\n"
            f"$${unordered}$$"
        ),
        "correct_answer": ordered,
        "marking_schema": [
            f"Order terms from highest exponent to constant: {ordered} [1 mark]",
        ],
        "hints": [
            "Descending powers means starting with the highest power of $x$ down to the constant term.",
            "Powers order: $x^3$, then $x^2$, then $x^1$, then constant.",
            "Keep the correct sign attached to each term.",
        ],
        "misconception_tags": ["descending_powers_sign_detachment"],
        "diagram_spec": None,
    }


def arch_46_ascending_powers_arrangement_polynomial(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(2, 6)
    b = rng.randint(3, 8)
    c = rng.randint(4, 9)

    unordered = f"{a}x^2 - {b}x + {c}"
    ordered = f"{c} - {b}x + {a}x^2"

    return {
        "title": "Arranging a Polynomial in Ascending Powers of the Variable",
        "topic": "Algebraic expressions 1",
        "grade": 8,
        "term": 2,
        "subskill": "46_ascending_powers_arrangement_polynomial",
        "difficulty": "easy",
        "question_text": (
            f"Rewrite the expression in **ascending powers of $x$**:\n\n"
            f"$${unordered}$$"
        ),
        "correct_answer": ordered,
        "marking_schema": [
            f"Order terms from constant up to highest power: {ordered} [1 mark]",
        ],
        "hints": [
            "Ascending powers means starting with the constant term and ending with the highest power of $x$.",
            "Order: constant, then $x$, then $x^2$.",
            f"Result = {ordered}.",
        ],
        "misconception_tags": ["ascending_powers_direction_confusion"],
        "diagram_spec": None,
    }


def arch_47_evaluating_expression_with_brackets(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(2, 5)
    b = rng.randint(5, 10)
    c = rng.randint(2, 6)
    x_val = rng.randint(1, 4)
    inside = b - x_val
    ans = a * inside + c

    return {
        "title": "Evaluating an Expression Containing Parentheses (BODMAS)",
        "topic": "Algebraic expressions 1",
        "grade": 8,
        "term": 2,
        "subskill": "47_evaluating_expression_with_brackets",
        "difficulty": "medium",
        "question_text": (
            f"Calculate the value of **${a}({b} - x) + {c}$** when **$x = {x_val}$**."
        ),
        "correct_answer": str(ans),
        "marking_schema": [
            f"Calculate bracket first: ({b} - {x_val}) = {inside} [1 mark]",
            f"Multiply and add: {a}({inside}) + {c} = {a * inside} + {c} = {ans} [1 mark]",
        ],
        "hints": [
            f"Substitute {x_val} for $x$: {a}({b} - {x_val}) + {c}.",
            f"Calculate inside the brackets first: {b} - {x_val} = {inside}.",
            f"Multiply by {a} and add {c}: {a} x {inside} + {c} = {ans}.",
        ],
        "misconception_tags": ["bodmas_bracket_evaluation_error"],
        "diagram_spec": None,
    }


def arch_48_identifying_non_polynomial_expression(rng: random.Random) -> Dict[str, Any]:
    return {
        "title": "Identifying Non-Polynomial Algebraic Expressions",
        "topic": "Algebraic expressions 1",
        "grade": 8,
        "term": 2,
        "subskill": "48_identifying_non_polynomial_expression",
        "difficulty": "medium",
        "question_text": (
            "Explain why the algebraic expression $$\\frac{3}{x} + 5$$\n\n"
            "is **not** a polynomial expression."
        ),
        "correct_answer": "In a polynomial, all exponents of the variable must be non-negative integers (whole numbers 0, 1, 2, ...). In 3/x, the variable x is in the denominator, which is equivalent to 3x^(-1) having a negative exponent.",
        "marking_schema": [
            "Explain that variables in denominators correspond to negative powers [1 mark]",
            "State that polynomials only allow non-negative integer exponents [1 mark]",
        ],
        "hints": [
            "What power of $x$ is $\\frac{1}{x}$? (It is $x^{-1}$).",
            "Can polynomials have negative exponents or variables under division?",
            "Polynomials only contain whole-number powers ($0, 1, 2, \\dots$).",
        ],
        "misconception_tags": ["polynomial_definition_exponent_rule"],
        "diagram_spec": None,
    }


def arch_49_combining_constants_and_variables_in_shopping_budget(rng: random.Random) -> Dict[str, Any]:
    budget = 100
    cost_fixed = rng.choice([20, 25, 30])
    unit_cost = rng.choice([3, 4, 5])
    change_const = budget - cost_fixed

    return {
        "title": "Writing Algebraic Expression for Remaining Money / Change",
        "topic": "Algebraic expressions 1",
        "grade": 8,
        "term": 2,
        "subskill": "49_combining_constants_and_variables_in_shopping_budget",
        "difficulty": "medium",
        "question_text": (
            f"Themba has a total budget of **R{budget}**. He pays a taxi fare of **R{cost_fixed}** "
            f"and buys **$x$ snacks** at **R{unit_cost} each**.\n\n"
            "Write a simplified algebraic expression in terms of $x$ for the change Themba has left."
        ),
        "correct_answer": f"R({change_const} - {unit_cost}x)",
        "marking_schema": [
            f"Total spent: R({cost_fixed} + {unit_cost}x) [1 mark]",
            f"Subtract from {budget}: {budget} - ({cost_fixed} + {unit_cost}x) = {change_const} - {unit_cost}x [1 mark]",
        ],
        "hints": [
            f"Total money spent is R{cost_fixed} + R{unit_cost}x.",
            f"Change = R{budget} - (money spent).",
            f"{budget} - ({cost_fixed} + {unit_cost}x) = {change_const} - {unit_cost}x.",
        ],
        "misconception_tags": ["budget_change_algebraic_modeling_error"],
        "diagram_spec": None,
    }


def arch_50_algebraic_expression_summary_challenge(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([2, 3, 4])
    b = rng.choice([2, 3, 5])
    c = rng.choice([3, 7])
    d = rng.choice([2, 6])

    expr = f"-{a}x^3 + {b}x^2 - {c}x + {d}"
    # evaluate at x = -1
    # -a(-1) + b(1) - c(-1) + d = a + b + c + d
    val_neg1 = a + b + c + d

    return {
        "title": "Comprehensive Polynomial Anatomy & Evaluation Challenge",
        "topic": "Algebraic expressions 1",
        "grade": 8,
        "term": 2,
        "subskill": "50_algebraic_expression_summary_challenge",
        "difficulty": "hard",
        "question_text": (
            f"Consider the polynomial:\n\n"
            f"$${expr}$$\n\n"
            "1. State the **degree** of the polynomial.\n"
            "2. State the **leading coefficient** (the coefficient of the term with the highest power).\n"
            "3. State the **constant term**.\n"
            "4. Calculate the value of the expression when **$x = -1$**."
        ),
        "correct_answer": f"1. Degree: 3. 2. Leading coefficient: -{a}. 3. Constant term: +{d}. 4. Value at x = -1: {val_neg1}.",
        "marking_schema": [
            "Degree: 3 [1 mark]",
            f"Leading coefficient: -{a} [1 mark]",
            f"Constant term: {d} [1 mark]",
            f"Evaluation: -{a}(-1)^3 + {b}(-1)^2 - {c}(-1) + {d} = {val_neg1} [1 mark]",
        ],
        "hints": [
            "The degree is the highest exponent on $x$ (which is 3).",
            f"The leading coefficient is the coefficient of $x^3$ (which is -{a}).",
            f"The constant term has no variable (which is {d}).",
            f"At x = -1, $(-1)^3 = -1$ and $(-1)^2 = 1$. Substitute and simplify to get {val_neg1}.",
        ],
        "misconception_tags": ["polynomial_anatomy_synthesis_gap"],
        "diagram_spec": None,
    }


BUILDERS_26_50 = [
    arch_26_perimeter_of_equilateral_triangle_in_terms_of_x,
    arch_27_perimeter_of_rectangle_in_terms_of_x,
    arch_28_perimeter_of_scalene_triangle_combining_like_terms,
    arch_29_perimeter_of_square_in_terms_of_x,
    arch_30_translating_consecutive_integers_to_algebra,
    arch_31_translating_consecutive_even_integers,
    arch_32_translating_age_word_problem_to_expression,
    arch_33_translating_taxi_fare_to_expression,
    arch_34_simplifying_expression_with_parentheses_addition,
    arch_35_simplifying_expression_with_parentheses_subtraction,
    arch_36_identifying_sign_error_in_subtraction_of_binomial,
    arch_37_combining_cubed_and_squared_terms,
    arch_38_writing_expression_for_shaded_area_difference,
    arch_39_writing_expression_for_total_cost_items,
    arch_40_simplifying_fractions_with_monomial_denominator,
    arch_41_evaluating_two_variable_expression,
    arch_42_evaluating_two_variable_expression_with_negatives,
    arch_43_finding_missing_term_to_make_expressions_equivalent,
    arch_44_translating_geometric_pattern_to_algebraic_expression,
    arch_45_descending_powers_arrangement_polynomial,
    arch_46_ascending_powers_arrangement_polynomial,
    arch_47_evaluating_expression_with_brackets,
    arch_48_identifying_non_polynomial_expression,
    arch_49_combining_constants_and_variables_in_shopping_budget,
    arch_50_algebraic_expression_summary_challenge,
]
