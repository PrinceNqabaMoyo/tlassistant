"""
Grade 8 Mathematics - Algebraic Equations 1 Archetypes (26 to 50).
100% CAPS-aligned deterministic question generators.
Adheres strictly to the 6-Pillar Generator Contract and Zero-Meta-Curriculum Invariant.
Grounded in curriculum_docs_auto/Mathematics_Gr8/Term 2/02. Algebraic equations 1.md.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from app.utils.grade8_mathematics.svg_diagrams import (
    draw_algebraic_shape_perimeter_svg,
    draw_flow_diagram_svg,
)


def arch_26_setting_up_equation_consecutive_integers(rng: random.Random) -> Dict[str, Any]:
    n = rng.randint(10, 35)
    s = 2 * n + 1
    next_n = n + 1

    return {
        "title": "Setting Up and Solving Equations: Consecutive Integers",
        "topic": "Algebraic equations 1",
        "grade": 8,
        "term": 2,
        "subskill": "26_setting_up_equation_consecutive_integers",
        "difficulty": "medium",
        "question_text": (
            f"The sum of two consecutive integers is **{s}**.\n\n"
            "1. Write an algebraic equation in terms of $n$ (where $n$ is the smaller integer).\n"
            "2. Solve the equation to find both consecutive integers."
        ),
        "correct_answer": f"1. n + (n + 1) = {s} (or 2n + 1 = {s}). 2. The integers are {n} and {next_n}.",
        "marking_schema": [
            f"Formulate equation: 2n + 1 = {s} [1 mark]",
            f"Solve: n = {n} and state both integers ({n} and {next_n}) [1 mark]",
        ],
        "hints": [
            "Let the smaller integer be $n$. The next integer is $n + 1$.",
            f"Sum = $n + n + 1 = 2n + 1 = {s}$.",
            f"Solve: $2n = {s - 1} \\implies n = {n}$.",
        ],
        "misconception_tags": ["consecutive_integer_equation_setup_error"],
        "diagram_spec": None,
    }


def arch_27_setting_up_equation_consecutive_even_integers(rng: random.Random) -> Dict[str, Any]:
    k = rng.randint(6, 20)
    n1 = 2 * k
    n2 = n1 + 2
    s = n1 + n2

    return {
        "title": "Setting Up and Solving Equations: Consecutive Even Integers",
        "topic": "Algebraic equations 1",
        "grade": 8,
        "term": 2,
        "subskill": "27_setting_up_equation_consecutive_even_integers",
        "difficulty": "medium",
        "question_text": (
            f"The sum of two consecutive even integers is **{s}**.\n\n"
            "1. Set up an equation using $x$ as the smaller even integer.\n"
            "2. Solve for $x$ and state both even integers."
        ),
        "correct_answer": f"1. x + (x + 2) = {s} (or 2x + 2 = {s}). 2. {n1} and {n2}.",
        "marking_schema": [
            f"Equation: 2x + 2 = {s} [1 mark]",
            f"Solve: x = {n1} and state both ({n1} and {n2}) [1 mark]",
        ],
        "hints": [
            "Consecutive even integers increase by 2: $x$ and $x + 2$.",
            f"$x + x + 2 = 2x + 2 = {s}$.",
            f"$2x = {s - 2} \\implies x = {n1}$.",
        ],
        "misconception_tags": ["consecutive_even_step_setup_error"],
        "diagram_spec": None,
    }


def arch_28_setting_up_equation_perimeter_of_square(rng: random.Random) -> Dict[str, Any]:
    ans = rng.randint(4, 15)
    p = 4 * ans

    return {
        "title": "Formulating Equations from Geometry: Perimeter of a Square",
        "topic": "Algebraic equations 1",
        "grade": 8,
        "term": 2,
        "subskill": "28_setting_up_equation_perimeter_of_square",
        "difficulty": "easy",
        "question_text": (
            f"A square of side length $x\\text{{ cm}}$ has a perimeter of **{p}\\text{{ cm}}**.\n\n"
            "1. Write down an algebraic equation connecting $x$ and the perimeter.\n"
            "2. Solve for $x$."
        ),
        "correct_answer": f"1. 4x = {p}. 2. x = {ans} cm.",
        "marking_schema": [
            f"Equation: 4x = {p} [1 mark]",
            f"Solution: x = {ans} cm [1 mark]",
        ],
        "hints": [
            "A square has 4 equal sides.",
            f"Perimeter = 4 x $x$ = 4x.",
            f"4x = {p} \\implies x = {p} ÷ 4 = {ans}.",
        ],
        "misconception_tags": ["square_perimeter_equation_gap"],
        "diagram_spec": None,
    }


def arch_29_setting_up_equation_perimeter_of_rectangle(rng: random.Random) -> Dict[str, Any]:
    seed = rng.randint(1, 1000000)
    breadth = rng.randint(3, 8)
    length = 2 * breadth
    p = 2 * (length + breadth)  # 6 * breadth

    svg = draw_algebraic_shape_perimeter_svg(
        shape_type="rectangle",
        side_labels=["2x", "x", "2x", "x"],
        title="Rectangle Dimensions",
        seed=seed,
    )

    return {
        "title": "Formulating Equations: Perimeter of a Rectangle",
        "topic": "Algebraic equations 1",
        "grade": 8,
        "term": 2,
        "subskill": "29_setting_up_equation_perimeter_of_rectangle",
        "difficulty": "medium",
        "question_text": (
            f"The length of a rectangle is twice its breadth ($x$). "
            f"The perimeter of the rectangle is **{p}\\text{{ cm}}**.\n\n"
            "1. Write an equation in terms of $x$ for the perimeter.\n"
            "2. Solve for $x$ and determine the length and breadth of the rectangle."
        ),
        "correct_answer": f"1. 2(2x + x) = {p} (or 6x = {p}). 2. Breadth = {breadth} cm, Length = {length} cm.",
        "marking_schema": [
            f"Equation: 6x = {p} [1 mark]",
            f"Solve: x = {breadth} cm; Length = {length} cm [1 mark]",
        ],
        "hints": [
            "Length is 2x and breadth is x.",
            f"Perimeter = 2(2x + x) = 2(3x) = 6x.",
            f"6x = {p} \\implies x = {breadth}.",
            f"Length = 2({breadth}) = {length} cm.",
        ],
        "misconception_tags": ["rectangle_perimeter_modeling_error"],
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    }


def arch_30_setting_up_equation_perimeter_of_triangle(rng: random.Random) -> Dict[str, Any]:
    x = rng.randint(4, 9)
    s1 = x
    s2 = x + 2
    s3 = x + 4
    p = s1 + s2 + s3  # 3x + 6

    return {
        "title": "Formulating Equations: Perimeter of a Triangle",
        "topic": "Algebraic equations 1",
        "grade": 8,
        "term": 2,
        "subskill": "30_setting_up_equation_perimeter_of_triangle",
        "difficulty": "medium",
        "question_text": (
            f"The three sides of a triangle measure $x\\text{{ cm}}$, $(x + 2)\\text{{ cm}}$, "
            f"and $(x + 4)\\text{{ cm}}$. The perimeter is **{p}\\text{{ cm}}**.\n\n"
            "1. Write an algebraic equation in terms of $x$.\n"
            "2. Solve for $x$ and state the length of the longest side."
        ),
        "correct_answer": f"1. 3x + 6 = {p}. 2. x = {x}; longest side = {s3} cm.",
        "marking_schema": [
            f"Equation: 3x + 6 = {p} [1 mark]",
            f"Solve: x = {x}; longest side = {s3} cm [1 mark]",
        ],
        "hints": [
            f"Sum of sides: $x + (x + 2) + (x + 4) = 3x + 6 = {p}$.",
            f"$3x = {p - 6} \\implies x = {x}$.",
            f"Longest side = $x + 4 = {x} + 4 = {s3}$ cm.",
        ],
        "misconception_tags": ["triangle_perimeter_equation_gap"],
        "diagram_spec": None,
    }


def arch_31_setting_up_equation_age_relationship(rng: random.Random) -> Dict[str, Any]:
    son = rng.randint(8, 14)
    mult = 3
    father = mult * son
    tot = son + father  # 4 * son

    return {
        "title": "Word Problem Modelling: Age Relationships",
        "topic": "Algebraic equations 1",
        "grade": 8,
        "term": 2,
        "subskill": "31_setting_up_equation_age_relationship",
        "difficulty": "medium",
        "question_text": (
            f"A father is **{mult} times as old** as his son. "
            f"The sum of their ages is **{tot} years**.\n\n"
            "1. If the son's age is $x$, formulate an equation representing the sum of their ages.\n"
            "2. Solve for $x$ and determine the age of both the son and the father."
        ),
        "correct_answer": f"1. x + {mult}x = {tot} (or 4x = {tot}). 2. Son is {son} years old; Father is {father} years old.",
        "marking_schema": [
            f"Equation: 4x = {tot} [1 mark]",
            f"Solve: x = {son}; Father = {father} years [1 mark]",
        ],
        "hints": [
            f"Son is $x$, father is {mult}x.",
            f"Sum: $x + {mult}x = 4x = {tot}$.",
            f"$x = {tot} ÷ 4 = {son}$.",
            f"Father's age = {mult} x {son} = {father}.",
        ],
        "misconception_tags": ["age_sum_equation_setup_error"],
        "diagram_spec": None,
    }


def arch_32_setting_up_equation_shopping_cost(rng: random.Random) -> Dict[str, Any]:
    n_books = rng.choice([3, 4, 5])
    book_price = rng.choice([12, 15, 18])
    pen_price = rng.choice([10, 15, 20])
    tot = n_books * book_price + pen_price

    return {
        "title": "Word Problem Modelling: Commercial Transactions",
        "topic": "Algebraic equations 1",
        "grade": 8,
        "term": 2,
        "subskill": "32_setting_up_equation_shopping_cost",
        "difficulty": "easy",
        "question_text": (
            f"Nomsa bought **{n_books} identical exercise books** and a calculator for **R{pen_price}**. "
            f"Her total bill was **R{tot}**.\n\n"
            "1. Write an algebraic equation using $x$ as the price of one exercise book.\n"
            "2. Solve the equation to find the cost of one exercise book."
        ),
        "correct_answer": f"1. {n_books}x + {pen_price} = {tot}. 2. x = R{book_price}.",
        "marking_schema": [
            f"Equation: {n_books}x + {pen_price} = {tot} [1 mark]",
            f"Solve: x = R{book_price} [1 mark]",
        ],
        "hints": [
            f"Cost of {n_books} books is {n_books}x.",
            f"Add calculator cost: {n_books}x + {pen_price} = {tot}.",
            f"{n_books}x = {tot - pen_price} \\implies x = {book_price}.",
        ],
        "misconception_tags": ["shopping_cost_linear_equation_error"],
        "diagram_spec": None,
    }


def arch_33_setting_up_equation_taxi_fare(rng: random.Random) -> Dict[str, Any]:
    base = rng.choice([15, 20])
    rate = rng.choice([8, 10])
    dist = rng.randint(5, 12)
    tot = base + rate * dist

    return {
        "title": "Word Problem Modelling: Rate and Fixed Base Costs",
        "topic": "Algebraic equations 1",
        "grade": 8,
        "term": 2,
        "subskill": "33_setting_up_equation_taxi_fare",
        "difficulty": "medium",
        "question_text": (
            f"A metered taxi charges a flat booking fee of **R{base}** plus **R{rate} per kilometre**.\n\n"
            f"If a passenger pays a total fare of **R{tot}**, write an equation and calculate "
            "the distance travelled in kilometres."
        ),
        "correct_answer": f"Equation: {base} + {rate}k = {tot}. Distance = {dist} km.",
        "marking_schema": [
            f"Equation: {rate}k + {base} = {tot} [1 mark]",
            f"Solve: k = {dist} km [1 mark]",
        ],
        "hints": [
            f"Cost = R{base} + R{rate}k = R{tot}.",
            f"{rate}k = {tot} - {base} = {tot - base}.",
            f"k = {tot - base} ÷ {rate} = {dist} km.",
        ],
        "misconception_tags": ["rate_modeling_equation_setup"],
        "diagram_spec": None,
    }


def arch_34_solving_equation_with_brackets_inspection(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([2, 3, 4])
    b = rng.randint(2, 6)
    ans = rng.randint(2, 7)
    target = a * (ans + b)

    return {
        "title": "Solving Equations Involving Parentheses: $a(x + b) = c$",
        "topic": "Algebraic equations 1",
        "grade": 8,
        "term": 2,
        "subskill": "34_solving_equation_with_brackets_inspection",
        "difficulty": "medium",
        "question_text": (
            f"Solve for $x$:\n\n"
            f"$${a}(x + {b}) = {target}$$"
        ),
        "correct_answer": str(ans),
        "marking_schema": [
            f"Divide by {a} (or expand): x + {b} = {target // a} [1 mark]",
            f"Solve: x = {ans} [1 mark]",
        ],
        "hints": [
            f"Method 1: Divide both sides by {a}: $x + {b} = {target // a}$.",
            f"Subtract {b}: $x = {target // a} - {b} = {ans}$.",
        ],
        "misconception_tags": ["bracket_equation_division_error"],
        "diagram_spec": None,
    }


def arch_35_solving_equation_with_brackets_difference(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([2, 3, 5])
    b = rng.randint(2, 6)
    ans = rng.randint(b + 1, b + 7)
    target = a * (ans - b)

    return {
        "title": "Solving Equations Involving Parentheses: $a(x - b) = c$",
        "topic": "Algebraic equations 1",
        "grade": 8,
        "term": 2,
        "subskill": "35_solving_equation_with_brackets_difference",
        "difficulty": "medium",
        "question_text": (
            f"Solve for $x$:\n\n"
            f"$${a}(x - {b}) = {target}$$"
        ),
        "correct_answer": str(ans),
        "marking_schema": [
            f"Divide by {a}: x - {b} = {target // a} [1 mark]",
            f"Add {b}: x = {ans} [1 mark]",
        ],
        "hints": [
            f"Divide both sides by {a}: $x - {b} = {target // a}$.",
            f"Add {b}: $x = {target // a} + {b} = {ans}$.",
        ],
        "misconception_tags": ["bracket_subtraction_equation_sign_error"],
        "diagram_spec": None,
    }


def arch_36_solving_equation_variable_both_sides_integer_inspection(rng: random.Random) -> Dict[str, Any]:
    ans = rng.randint(2, 6)
    c1 = rng.randint(4, 7)
    c2 = rng.randint(2, c1 - 1)
    diff_c = c1 - c2
    const_r = rng.randint(2, 8)
    const_l = const_r - diff_c * ans

    # c1 x + const_l = c2 x + const_r
    # => (c1 - c2)x = const_r - const_l = diff_c * ans => x = ans
    sign_l = "+" if const_l >= 0 else "-"
    abs_l = abs(const_l)

    return {
        "title": "Solving Equations with Variables on Both Sides",
        "topic": "Algebraic equations 1",
        "grade": 8,
        "term": 2,
        "subskill": "36_solving_equation_variable_both_sides_integer_inspection",
        "difficulty": "hard",
        "question_text": (
            f"Solve for $x$:\n\n"
            f"$${c1}x {sign_l} {abs_l} = {c2}x + {const_r}$$"
        ),
        "correct_answer": str(ans),
        "marking_schema": [
            f"Collect variable terms on left: {diff_c}x = {const_r - const_l} [1 mark]",
            f"Divide by {diff_c}: x = {ans} [1 mark]",
        ],
        "hints": [
            f"Subtract {c2}x from both sides: ({c1} - {c2})x = {diff_c}x.",
            f"Move constant to the right: {const_r} - ({const_l}) = {diff_c * ans}.",
            f"{diff_c}x = {diff_c * ans} \\implies x = {ans}.",
        ],
        "misconception_tags": ["variable_transposition_both_sides_error"],
        "diagram_spec": None,
    }


def arch_37_solving_equation_with_fractions_common_denominator(rng: random.Random) -> Dict[str, Any]:
    # x/2 + x/4 = target => 3x/4 = target => x = 4 * target / 3
    k = rng.choice([3, 6, 9])
    target = k
    ans = (4 * target) // 3

    return {
        "title": "Solving Linear Equations with Fractional Terms",
        "topic": "Algebraic equations 1",
        "grade": 8,
        "term": 2,
        "subskill": "37_solving_equation_with_fractions_common_denominator",
        "difficulty": "hard",
        "question_text": (
            f"Solve for $x$ by finding a common denominator:\n\n"
            f"$$\\frac{{x}}{{2}} + \\frac{{x}}{{4}} = {target}$$"
        ),
        "correct_answer": str(ans),
        "marking_schema": [
            f"Combine fractions: 2x/4 + x/4 = 3x/4 = {target} [1 mark]",
            f"Solve for x: x = ({target} * 4)/3 = {ans} [1 mark]",
        ],
        "hints": [
            "Express both fractions over the common denominator 4: $\\frac{2x}{4} + \\frac{x}{4} = \\frac{3x}{4}$.",
            f"$\\frac{{3x}}{{4}} = {target}$.",
            f"Multiply by 4: $3x = {target * 4}$.",
            f"Divide by 3: $x = {ans}$.",
        ],
        "misconception_tags": ["fraction_equation_lcd_error"],
        "diagram_spec": None,
    }


def arch_38_solving_equation_with_negative_constant_both_sides(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(2, 5)
    ans = rng.randint(3, 8)
    b = rng.randint(2, 6)
    # -a x + b = -c => -a x = -c - b => -c - b = -a * ans => -c = -a*ans + b
    c = a * ans - b

    return {
        "title": "Solving Equations with Negative Constants and Coefficients",
        "topic": "Algebraic equations 1",
        "grade": 8,
        "term": 2,
        "subskill": "38_solving_equation_with_negative_constant_both_sides",
        "difficulty": "hard",
        "question_text": (
            f"Solve for $x$:\n\n"
            f"$$-{a}x + {b} = -{c}$$"
        ),
        "correct_answer": str(ans),
        "marking_schema": [
            f"Subtract {b}: -{a}x = -{c + b} [1 mark]",
            f"Divide by -{a}: x = {ans} [1 mark]",
        ],
        "hints": [
            f"Subtract {b} from both sides: -{a}x = -{c} - {b} = -{c + b}.",
            f"Divide by -{a}: (-{c + b}) ÷ (-{a}) = +{ans}.",
        ],
        "misconception_tags": ["negative_division_sign_confusion"],
        "diagram_spec": None,
    }


def arch_39_flow_diagram_inversion_backtracking(rng: random.Random) -> Dict[str, Any]:
    seed = rng.randint(1, 1000000)
    a = rng.randint(2, 5)
    b = rng.randint(3, 9)
    ans = rng.randint(3, 8)
    out_val = a * ans + b

    svg = draw_flow_diagram_svg(
        input_label="x",
        op1=f"× {a}",
        op2=f"+ {b}",
        output_label=str(out_val),
        title="Inverting a Flow Calculation",
        seed=seed,
    )

    return {
        "title": "Solving Equations by Reversing Flow Diagrams (Backtracking)",
        "topic": "Algebraic equations 1",
        "grade": 8,
        "term": 2,
        "subskill": "39_flow_diagram_inversion_backtracking",
        "difficulty": "medium",
        "question_text": (
            f"An input number $x$ is multiplied by **{a}**, and then **{b}** is added to give an output of **{out_val}**.\n\n"
            "By reversing the operations (backtracking from output to input), find the value of $x$."
        ),
        "correct_answer": str(ans),
        "marking_schema": [
            f"Reverse Step 1 (subtract {b}): {out_val} - {b} = {out_val - b} [1 mark]",
            f"Reverse Step 2 (divide by {a}): {out_val - b} / {a} = {ans} [1 mark]",
        ],
        "hints": [
            f"Work backwards from the output {out_val}.",
            f"Inverse of '+ {b}' is '- {b}': {out_val} - {b} = {out_val - b}.",
            f"Inverse of 'x {a}' is '÷ {a}': {out_val - b} ÷ {a} = {ans}.",
        ],
        "misconception_tags": ["flow_diagram_inversion_order_error"],
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    }


def arch_40_diagnosing_transposition_sign_error(rng: random.Random) -> Dict[str, Any]:
    return {
        "title": "Diagnosing Common Algebraic Misconceptions: Sign Changes Across Equals Sign",
        "topic": "Algebraic equations 1",
        "grade": 8,
        "term": 2,
        "subskill": "40_diagnosing_transposition_sign_error",
        "difficulty": "medium",
        "question_text": (
            "A learner attempts to solve $x + 7 = 12$ and writes:\n\n"
            "> *'x = 12 + 7, so x = 19'*\n\n"
            "Explain why the learner's method is wrong and write the **correct solution**."
        ),
        "correct_answer": "The learner added 7 instead of subtracting 7. To maintain equality when isolating x, we must apply the additive inverse (-7) to both sides: x = 12 - 7 = 5.",
        "marking_schema": [
            "Explain that +7 becomes -7 (must subtract 7 from both sides) [1 mark]",
            "State correct solution: x = 5 [1 mark]",
        ],
        "hints": [
            "What is the inverse operation of adding 7?",
            "Subtract 7 from both sides.",
            "12 - 7 = 5.",
        ],
        "misconception_tags": ["transposition_sign_retention_fallacy"],
        "diagram_spec": None,
    }


def arch_41_diagnosing_division_coefficient_error(rng: random.Random) -> Dict[str, Any]:
    return {
        "title": "Diagnosing Common Algebraic Misconceptions: Coefficient Removal",
        "topic": "Algebraic equations 1",
        "grade": 8,
        "term": 2,
        "subskill": "41_diagnosing_division_coefficient_error",
        "difficulty": "medium",
        "question_text": (
            "A learner solves $4x = 20$ by writing:\n\n"
            "> *'x = 20 - 4, so x = 16'*\n\n"
            "Explain why subtracting 4 is incorrect and state the **correct algebraic operation and answer**."
        ),
        "correct_answer": "In 4x, the 4 is multiplying x, not adding to it. The inverse of multiplication is division, not subtraction. Both sides must be divided by 4: x = 20 ÷ 4 = 5.",
        "marking_schema": [
            "Explain that 4 is a multiplier and requires division, not subtraction [1 mark]",
            "State correct answer: x = 5 [1 mark]",
        ],
        "hints": [
            "$4x$ means $4 \\times x$.",
            "The inverse of multiplying by 4 is dividing by 4.",
            "20 ÷ 4 = 5.",
        ],
        "misconception_tags": ["coefficient_subtraction_vs_division_fallacy"],
        "diagram_spec": None,
    }


def arch_42_solving_equation_fractional_solution(rng: random.Random) -> Dict[str, Any]:
    a = 4
    num = rng.choice([6, 10, 14, 18])
    dec_val = num / a
    dec_str = f"{dec_val:.1f}".replace(".", ",")

    return {
        "title": "Solving Linear Equations with Decimal / Fractional Solutions",
        "topic": "Algebraic equations 1",
        "grade": 8,
        "term": 2,
        "subskill": "42_solving_equation_fractional_solution",
        "difficulty": "medium",
        "question_text": (
            f"Solve for $x$ and write your answer as a decimal number:\n\n"
            f"$${a}x = {num}$$"
        ),
        "correct_answer": dec_str,
        "marking_schema": [
            f"Divide by {a}: x = {num}/{a} [1 mark]",
            f"Write as decimal: {dec_str} [1 mark]",
        ],
        "hints": [
            f"Divide {num} by {a}.",
            f"{num} ÷ {a} = {dec_str}.",
        ],
        "misconception_tags": ["fraction_to_decimal_equation_root_error"],
        "diagram_spec": None,
    }


def arch_43_verifying_whether_given_value_is_root(rng: random.Random) -> Dict[str, Any]:
    a = 3
    b = 10
    test_x = -2
    lhs = a * test_x + b  # 3(-2) + 10 = 4

    return {
        "title": "Testing Solution Validity in Equations",
        "topic": "Algebraic equations 1",
        "grade": 8,
        "term": 2,
        "subskill": "43_verifying_whether_given_value_is_root",
        "difficulty": "easy",
        "question_text": (
            f"Is **$x = {test_x}$** a solution to the equation **${a}x + {b} = {lhs}$**?\n\n"
            "Justify your answer by calculating the value of the Left-Hand Side."
        ),
        "correct_answer": f"Yes. Substituting x = {test_x} gives LHS = {a}({test_x}) + {b} = -6 + {b} = {lhs}. Since LHS equals the RHS ({lhs}), x = {test_x} is a valid solution.",
        "marking_schema": [
            f"Calculate LHS: {a}({test_x}) + {b} = {lhs} [1 mark]",
            "Conclude Yes with justification [1 mark]",
        ],
        "hints": [
            f"Replace $x$ with ({test_x}): {a} x ({test_x}) + {b}.",
            f"-6 + {b} = {lhs}.",
            "Does it match the right-hand side?",
        ],
        "misconception_tags": ["root_verification_arithmetic_error"],
        "diagram_spec": None,
    }


def arch_44_solving_equation_square_root_inspection(rng: random.Random) -> Dict[str, Any]:
    root = rng.choice([6, 7, 8, 9, 10, 11, 12])
    sq = root ** 2

    return {
        "title": "Solving Equations Involving Squares: $x^2 = a^2$",
        "topic": "Algebraic equations 1",
        "grade": 8,
        "term": 2,
        "subskill": "44_solving_equation_square_root_inspection",
        "difficulty": "medium",
        "question_text": (
            f"Solve for $x$ by inspection (state the positive root):\n\n"
            f"$$x^2 = {sq}$$"
        ),
        "correct_answer": str(root),
        "marking_schema": [
            f"Take square root: $x = \\sqrt{{{sq}}} = {root}$ [1 mark]",
        ],
        "hints": [
            f"What number multiplied by itself equals {sq}?",
            f"$\\sqrt{{{sq}}} = {root}$.",
        ],
        "misconception_tags": ["square_vs_doubling_equation_error"],
        "diagram_spec": None,
    }


def arch_45_solving_equation_cube_root_inspection(rng: random.Random) -> Dict[str, Any]:
    root = rng.choice([2, 3, 4, 5])
    cube = root ** 3

    return {
        "title": "Solving Equations Involving Cubes: $x^3 = a^3$",
        "topic": "Algebraic equations 1",
        "grade": 8,
        "term": 2,
        "subskill": "45_solving_equation_cube_root_inspection",
        "difficulty": "medium",
        "question_text": (
            f"Find the value of $x$:\n\n"
            f"$$x^3 = {cube}$$"
        ),
        "correct_answer": str(root),
        "marking_schema": [
            f"Take cube root: $x = \\sqrt[3]{{{cube}}} = {root}$ [1 mark]",
        ],
        "hints": [
            f"What number multiplied by itself three times equals {cube}?",
            f"{root} x {root} x {root} = {cube}.",
            f"$x = {root}$.",
        ],
        "misconception_tags": ["cube_vs_tripling_equation_error"],
        "diagram_spec": None,
    }


def arch_46_setting_up_equation_two_angles_complementary(rng: random.Random) -> Dict[str, Any]:
    diff = rng.choice([10, 20, 30])
    # x + (x + diff) = 90 => 2x = 90 - diff
    ans = (90 - diff) // 2
    ang2 = ans + diff

    return {
        "title": "Geometric Modelling: Complementary Angles Equation",
        "topic": "Algebraic equations 1",
        "grade": 8,
        "term": 2,
        "subskill": "46_setting_up_equation_two_angles_complementary",
        "difficulty": "medium",
        "question_text": (
            f"Two angles are complementary (their sum is $90^\\circ$). "
            f"One angle is **$x^\\circ$** and the other angle is **$(x + {diff})^\\circ$**.\n\n"
            "1. Write an algebraic equation for the sum of the angles.\n"
            "2. Solve for $x$ and determine the size of both angles."
        ),
        "correct_answer": f"1. x + (x + {diff}) = 90 (or 2x + {diff} = 90). 2. Angles are {ans}° and {ang2}°.",
        "marking_schema": [
            f"Equation: 2x + {diff} = 90 [1 mark]",
            f"Solve: x = {ans}°; both angles {ans}° and {ang2}° [1 mark]",
        ],
        "hints": [
            "Complementary angles sum to 90 degrees.",
            f"$x + x + {diff} = 2x + {diff} = 90$.",
            f"$2x = {90 - diff} \\implies x = {ans}$.",
        ],
        "misconception_tags": ["complementary_angles_sum_gap"],
        "diagram_spec": None,
    }


def arch_47_setting_up_equation_two_angles_supplementary(rng: random.Random) -> Dict[str, Any]:
    # 2x + 3x = 180 => 5x = 180 => x = 36
    r1 = 2
    r2 = 3
    tot_r = r1 + r2
    ans = 180 // tot_r
    a1 = r1 * ans
    a2 = r2 * ans

    return {
        "title": "Geometric Modelling: Supplementary Angles Equation",
        "topic": "Algebraic equations 1",
        "grade": 8,
        "term": 2,
        "subskill": "47_setting_up_equation_two_angles_supplementary",
        "difficulty": "medium",
        "question_text": (
            f"Two adjacent angles lying on a straight line have sizes **${r1}x^\\circ$** and **${r2}x^\\circ$**.\n\n"
            "1. Formulate the equation based on angles on a straight line.\n"
            "2. Solve for $x$ and calculate the size of each angle."
        ),
        "correct_answer": f"1. {r1}x + {r2}x = 180 (or {tot_r}x = 180). 2. x = {ans}°; angles are {a1}° and {a2}°.",
        "marking_schema": [
            f"Equation: {tot_r}x = 180 [1 mark]",
            f"Solve: x = {ans}°; angles {a1}° and {a2}° [1 mark]",
        ],
        "hints": [
            "Angles on a straight line sum to 180 degrees.",
            f"${r1}x + {r2}x = {tot_r}x = 180$.",
            f"$x = 180 ÷ {tot_r} = {ans}$.",
            f"Angles: {r1}({ans}) = {a1}° and {r2}({ans}) = {a2}°.",
        ],
        "misconception_tags": ["supplementary_angles_sum_gap"],
        "diagram_spec": None,
    }


def arch_48_solving_equation_zero_product_property_intro(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([3, 4, 5, 7, 8])

    return {
        "title": "Solving Equations: Zero Product Property Introduction",
        "topic": "Algebraic equations 1",
        "grade": 8,
        "term": 2,
        "subskill": "48_solving_equation_zero_product_property_intro",
        "difficulty": "hard",
        "question_text": (
            f"Find the two solutions to the equation:\n\n"
            f"$$x(x - {a}) = 0$$"
        ),
        "correct_answer": f"x = 0 or x = {a}",
        "marking_schema": [
            f"State x = 0 [1 mark]",
            f"State x = {a} [1 mark]",
        ],
        "hints": [
            "If the product of two factors is 0, at least one factor must be 0.",
            "Either $x = 0$ or $(x - {a}) = 0$.",
            f"If $x - {a} = 0$, then $x = {a}$.",
        ],
        "misconception_tags": ["zero_product_property_single_root_error"],
        "diagram_spec": None,
    }


def arch_49_solving_equation_with_decimals_inspection(rng: random.Random) -> Dict[str, Any]:
    ans = rng.choice([3, 4, 5, 6])
    c = 0.5 * ans + 1.5
    c_str = f"{c:.1f}".replace(".", ",")

    return {
        "title": "Solving Linear Equations with Decimals",
        "topic": "Algebraic equations 1",
        "grade": 8,
        "term": 2,
        "subskill": "49_solving_equation_with_decimals_inspection",
        "difficulty": "medium",
        "question_text": (
            f"Solve for $x$:\n\n"
            f"$$0,5x + 1,5 = {c_str}$$"
        ),
        "correct_answer": str(ans),
        "marking_schema": [
            f"Subtract 1,5: 0,5x = {c - 1.5:.1f} [1 mark]",
            f"Divide by 0,5: x = {ans} [1 mark]",
        ],
        "hints": [
            f"Subtract 1,5 from {c_str}: 0,5x = {c - 1.5:.1f}.",
            f"Dividing by 0,5 is the same as multiplying by 2.",
            f"$x = {ans}$.",
        ],
        "misconception_tags": ["decimal_equation_subtraction_error"],
        "diagram_spec": None,
    }


def arch_50_algebraic_equations_1_comprehensive_modelling(rng: random.Random) -> Dict[str, Any]:
    ans = rng.randint(4, 9)
    mult = rng.choice([2, 3])
    add_val = rng.randint(5, 12)
    tot = mult * ans + add_val

    return {
        "title": "Comprehensive Equation Formulation, Solution & Verification",
        "topic": "Algebraic equations 1",
        "grade": 8,
        "term": 2,
        "subskill": "50_algebraic_equations_1_comprehensive_modelling",
        "difficulty": "hard",
        "question_text": (
            f"A school fundraising team sells tickets for a concert. "
            f"Adult tickets cost **R{mult}0** each and learner tickets cost **R{add_val}**. "
            f"Sipho bought **{mult} adult tickets** and paid an additional booking fee of **R{add_val}**, "
            f"spending a total of **R{tot}**.\n\n"
            f"1. Write an algebraic equation in terms of $x$ (where $x$ is the cost unit in tens).\n"
            "2. Solve for $x$.\n"
            "3. Verify your solution by substitution."
        ),
        "correct_answer": f"1. {mult}x + {add_val} = {tot}. 2. x = {ans}. 3. {mult}({ans}) + {add_val} = {tot} (verified).",
        "marking_schema": [
            f"Equation: {mult}x + {add_val} = {tot} [1 mark]",
            f"Solve: x = {ans} [1 mark]",
            f"Verification: {mult}({ans}) + {add_val} = {tot} [1 mark]",
        ],
        "hints": [
            f"Equation: ${mult}x + {add_val} = {tot}$.",
            f"${mult}x = {tot - add_val} \\implies x = {ans}$.",
            f"Check: ${mult}({ans}) + {add_val} = {mult * ans} + {add_val} = {tot}$.",
        ],
        "misconception_tags": ["comprehensive_equation_modeling_gap"],
        "diagram_spec": None,
    }


BUILDERS_26_50 = [
    arch_26_setting_up_equation_consecutive_integers,
    arch_27_setting_up_equation_consecutive_even_integers,
    arch_28_setting_up_equation_perimeter_of_square,
    arch_29_setting_up_equation_perimeter_of_rectangle,
    arch_30_setting_up_equation_perimeter_of_triangle,
    arch_31_setting_up_equation_age_relationship,
    arch_32_setting_up_equation_shopping_cost,
    arch_33_setting_up_equation_taxi_fare,
    arch_34_solving_equation_with_brackets_inspection,
    arch_35_solving_equation_with_brackets_difference,
    arch_36_solving_equation_variable_both_sides_integer_inspection,
    arch_37_solving_equation_with_fractions_common_denominator,
    arch_38_solving_equation_with_negative_constant_both_sides,
    arch_39_flow_diagram_inversion_backtracking,
    arch_40_diagnosing_transposition_sign_error,
    arch_41_diagnosing_division_coefficient_error,
    arch_42_solving_equation_fractional_solution,
    arch_43_verifying_whether_given_value_is_root,
    arch_44_solving_equation_square_root_inspection,
    arch_45_solving_equation_cube_root_inspection,
    arch_46_setting_up_equation_two_angles_complementary,
    arch_47_setting_up_equation_two_angles_supplementary,
    arch_48_solving_equation_zero_product_property_intro,
    arch_49_solving_equation_with_decimals_inspection,
    arch_50_algebraic_equations_1_comprehensive_modelling,
]
