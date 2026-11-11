"""
Grade 8 Mathematics - Algebraic Expressions 1 Archetypes (01 to 25).
100% CAPS-aligned deterministic question generators.
Adheres strictly to the 6-Pillar Generator Contract and Zero-Meta-Curriculum Invariant.
Grounded in curriculum_docs_auto/Mathematics_Gr8/Term 2/01. Algebraic expressions 1.md.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from app.utils.grade8_mathematics.svg_diagrams import draw_flow_diagram_svg


def arch_01_translating_word_phrase_sum_product_to_expression(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(2, 7)
    b = rng.randint(3, 12)
    return {
        "title": "Translating Verbal Descriptions to Algebraic Expressions (Product and Sum)",
        "topic": "Algebraic expressions 1",
        "grade": 8,
        "term": 2,
        "subskill": "01_translating_word_phrase_sum_product_to_expression",
        "difficulty": "easy",
        "question_text": (
            f"Write an algebraic expression for the following phrase using the variable $x$:\n\n"
            f"> *'Multiply a number by {a} and then add {b} to the answer.'*"
        ),
        "correct_answer": f"{a}x + {b}",
        "marking_schema": [
            f"Multiply by {a}: {a}x [1 mark]",
            f"Add {b}: + {b} [1 mark]",
        ],
        "hints": [
            f"Let the unknown number be $x$.",
            f"Multiplying $x$ by {a} is written as {a}x.",
            f"Adding {b} gives {a}x + {b}.",
        ],
        "misconception_tags": ["word_to_algebraic_syntax_error"],
        "diagram_spec": None,
    }


def arch_02_translating_word_phrase_difference_quotient_to_expression(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([2, 3, 4, 5])
    b = rng.randint(2, 9)
    return {
        "title": "Translating Verbal Descriptions to Algebraic Expressions (Quotient and Difference)",
        "topic": "Algebraic expressions 1",
        "grade": 8,
        "term": 2,
        "subskill": "02_translating_word_phrase_difference_quotient_to_expression",
        "difficulty": "medium",
        "question_text": (
            f"Write an algebraic expression for the following statement using the variable $x$:\n\n"
            f"> *'{b} less than the quotient of a number and {a}.'*"
        ),
        "correct_answer": f"\\frac{{x}}{{{a}}} - {b}",
        "marking_schema": [
            f"Quotient of $x$ and {a}: x/{a} [1 mark]",
            f"{b} less than quotient: - {b} [1 mark]",
        ],
        "hints": [
            f"The quotient of a number $x$ and {a} is $\\frac{{x}}{{{a}}}$.",
            f"'{b} less than' means subtracting {b} from the quotient.",
            f"Expression: $\\frac{{x}}{{{a}}} - {b}$.",
        ],
        "misconception_tags": ["subtraction_order_reversal"],
        "diagram_spec": None,
    }


def arch_03_translating_flow_diagram_to_expression(rng: random.Random) -> Dict[str, Any]:
    seed = rng.randint(1, 1000000)
    a = rng.randint(2, 6)
    b = rng.randint(3, 10)
    op1 = f"× {a}"
    op2 = f"+ {b}"
    svg = draw_flow_diagram_svg(
        input_label="x",
        op1=op1,
        op2=op2,
        output_label="y",
        title="Input-Output Flow Diagram",
        seed=seed,
    )
    return {
        "title": "Translating a Flow Diagram into an Algebraic Expression",
        "topic": "Algebraic expressions 1",
        "grade": 8,
        "term": 2,
        "subskill": "03_translating_flow_diagram_to_expression",
        "difficulty": "easy",
        "question_text": (
            "A flow calculation sequence applies operations in order to an input number $x$:\n\n"
            f"- Step 1: Multiply by {a}\n"
            f"- Step 2: Add {b}\n\n"
            "Write the formula for the output $y$ in terms of $x$."
        ),
        "correct_answer": f"y = {a}x + {b}",
        "marking_schema": [
            f"First operation {a}x [1 mark]",
            f"Second operation + {b} yielding y = {a}x + {b} [1 mark]",
        ],
        "hints": [
            f"Follow the arrows from left to right.",
            f"After Step 1, the intermediate value is {a}x.",
            f"After Step 2, the final expression is {a}x + {b}.",
        ],
        "misconception_tags": ["flow_diagram_order_of_operations"],
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    }


def arch_04_identifying_number_of_terms_in_expression(rng: random.Random) -> Dict[str, Any]:
    n = rng.choice([2, 3, 4])
    if n == 2:
        expr = f"{rng.randint(2, 9)}x^2 - {rng.randint(2, 9)}"
    elif n == 3:
        expr = f"{rng.randint(2, 9)}x^2 - {rng.randint(2, 9)}x + {rng.randint(2, 9)}"
    else:
        expr = f"{rng.randint(2, 9)}x^3 - {rng.randint(2, 9)}x^2 + {rng.randint(2, 9)}x - {rng.randint(2, 9)}"

    return {
        "title": "Identifying Number of Terms in an Algebraic Expression",
        "topic": "Algebraic expressions 1",
        "grade": 8,
        "term": 2,
        "subskill": "04_identifying_number_of_terms_in_expression",
        "difficulty": "easy",
        "question_text": (
            f"Consider the algebraic expression:\n\n"
            f"$${expr}$$\n\n"
            "How many **terms** are there in this expression?"
        ),
        "correct_answer": str(n),
        "marking_schema": [
            f"Correctly identify {n} terms separated by + or - signs [1 mark]",
        ],
        "hints": [
            "Terms are separated by addition (+) and subtraction (-) signs.",
            "Count each distinct block separated by a plus or minus.",
            f"There are {n} terms.",
        ],
        "misconception_tags": ["term_boundary_miscounting"],
        "diagram_spec": None,
    }


def arch_05_classifying_monomial_binomial_trinomial_polynomial(rng: random.Random) -> Dict[str, Any]:
    types = [
        ("monomial", f"{rng.randint(3, 9)}x^2"),
        ("binomial", f"{rng.randint(3, 9)}x - {rng.randint(2, 8)}"),
        ("trinomial", f"{rng.randint(2, 7)}x^2 + {rng.randint(3, 8)}x - {rng.randint(2, 9)}"),
    ]
    correct_type, expr = rng.choice(types)
    return {
        "title": "Classifying Expressions: Monomial, Binomial, or Trinomial",
        "topic": "Algebraic expressions 1",
        "grade": 8,
        "term": 2,
        "subskill": "05_classifying_monomial_binomial_trinomial_polynomial",
        "difficulty": "easy",
        "question_text": (
            f"Classify the expression $${expr}$$\n\n"
            "as a **monomial**, **binomial**, or **trinomial**."
        ),
        "correct_answer": correct_type,
        "marking_schema": [
            f"Classify correctly as {correct_type} [1 mark]",
        ],
        "hints": [
            "Monomial = 1 term, Binomial = 2 terms, Trinomial = 3 terms.",
            "Count the number of terms separated by + and - signs.",
            f"The expression has terms matching a {correct_type}.",
        ],
        "misconception_tags": ["polynomial_classification_error"],
        "diagram_spec": None,
    }


def arch_06_identifying_variable_and_constant_term(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(2, 8)
    b = rng.randint(2, 8)
    c = rng.randint(3, 15)
    sign = rng.choice(["+", "-"])
    const_val = c if sign == "+" else -c

    return {
        "title": "Identifying the Constant Term in a Polynomial",
        "topic": "Algebraic expressions 1",
        "grade": 8,
        "term": 2,
        "subskill": "06_identifying_variable_and_constant_term",
        "difficulty": "easy",
        "question_text": (
            f"Given the expression:\n\n"
            f"$${a}x^2 + {b}x {sign} {c}$$\n\n"
            "Write down the value of the **constant term** (including its sign)."
        ),
        "correct_answer": str(const_val),
        "marking_schema": [
            f"Identify constant term with correct sign: {const_val} [1 mark]",
        ],
        "hints": [
            "A constant term does not contain any variables.",
            "Always include the sign in front of the constant.",
            f"The constant term is {const_val}.",
        ],
        "misconception_tags": ["constant_term_sign_omission"],
        "diagram_spec": None,
    }


def arch_07_identifying_coefficient_of_linear_term(rng: random.Random) -> Dict[str, Any]:
    c_x2 = rng.randint(2, 6)
    sign = rng.choice(["+", "-"])
    c_x_abs = rng.choice([1, 2, 3, 5, 7])
    c_x = c_x_abs if sign == "+" else -c_x_abs
    c_str = f"+ {c_x_abs}x" if sign == "+" else f"- {c_x_abs}x"
    if c_x_abs == 1:
        c_str = "+ x" if sign == "+" else "- x"
    const = rng.randint(4, 12)

    return {
        "title": "Identifying Coefficient of the Linear Term",
        "topic": "Algebraic expressions 1",
        "grade": 8,
        "term": 2,
        "subskill": "07_identifying_coefficient_of_linear_term",
        "difficulty": "medium",
        "question_text": (
            f"Consider the polynomial:\n\n"
            f"$${c_x2}x^2 {c_str} + {const}$$\n\n"
            "State the **coefficient of $x$**."
        ),
        "correct_answer": str(c_x),
        "marking_schema": [
            f"Identify coefficient of $x$ with sign: {c_x} [1 mark]",
        ],
        "hints": [
            "The coefficient is the numerical factor multiplying the variable $x$.",
            "Remember to include the negative sign if there is a minus in front.",
            f"The coefficient of $x$ is {c_x}.",
        ],
        "misconception_tags": ["implicit_coefficient_negation_error"],
        "diagram_spec": None,
    }


def arch_08_identifying_coefficient_of_squared_term(rng: random.Random) -> Dict[str, Any]:
    c_sq = rng.choice([-5, -4, -3, -2, -1, 2, 3, 4, 6])
    c_sq_str = f"{c_sq}x^2" if c_sq != -1 and c_sq != 1 else ("-x^2" if c_sq == -1 else "x^2")
    c_lin = rng.randint(2, 8)
    const = rng.randint(1, 9)

    return {
        "title": "Identifying Coefficient of the Squared Term",
        "topic": "Algebraic expressions 1",
        "grade": 8,
        "term": 2,
        "subskill": "08_identifying_coefficient_of_squared_term",
        "difficulty": "easy",
        "question_text": (
            f"Given the polynomial expression:\n\n"
            f"$${c_sq_str} + {c_lin}x - {const}$$\n\n"
            "State the **coefficient of $x^2$**."
        ),
        "correct_answer": str(c_sq),
        "marking_schema": [
            f"Identify coefficient of $x^2$: {c_sq} [1 mark]",
        ],
        "hints": [
            "Look at the term containing $x^2$.",
            "If the term is just $-x^2$, the coefficient is $-1$.",
            f"The coefficient of $x^2$ is {c_sq}.",
        ],
        "misconception_tags": ["squared_coefficient_confusion"],
        "diagram_spec": None,
    }


def arch_09_determining_degree_of_univariate_polynomial(rng: random.Random) -> Dict[str, Any]:
    deg = rng.choice([1, 2, 3, 4])
    if deg == 1:
        expr = f"{rng.randint(2, 9)}x + {rng.randint(1, 9)}"
    elif deg == 2:
        expr = f"{rng.randint(2, 9)}x^2 - {rng.randint(2, 9)}x + {rng.randint(1, 9)}"
    elif deg == 3:
        expr = f"{rng.randint(2, 9)}x^3 + {rng.randint(2, 9)}x^2 - {rng.randint(1, 9)}"
    else:
        expr = f"{rng.randint(2, 9)}x^4 - {rng.randint(2, 9)}x^2 + {rng.randint(1, 9)}"

    return {
        "title": "Determining Degree of a Univariate Polynomial",
        "topic": "Algebraic expressions 1",
        "grade": 8,
        "term": 2,
        "subskill": "09_determining_degree_of_univariate_polynomial",
        "difficulty": "easy",
        "question_text": (
            f"What is the **degree** of the algebraic expression:\n\n"
            f"$${expr}$$?"
        ),
        "correct_answer": str(deg),
        "marking_schema": [
            f"Identify highest exponent of variable as degree {deg} [1 mark]",
        ],
        "hints": [
            "The degree of a polynomial is the highest exponent of the variable in the expression.",
            "Look for the term with the largest power of $x$.",
            f"The highest power is {deg}.",
        ],
        "misconception_tags": ["polynomial_degree_highest_exponent_error"],
        "diagram_spec": None,
    }


def arch_10_identifying_like_terms_from_list(rng: random.Random) -> Dict[str, Any]:
    v = rng.choice(["x", "y", "a"])
    c1 = rng.randint(2, 5)
    c2 = rng.randint(6, 9)
    term1 = f"{c1}{v}^2"
    term2 = f"{c2}{v}^2"

    unlikes = [f"{rng.randint(2, 9)}{v}", f"{rng.randint(2, 9)}{v}^3", f"{rng.randint(2, 9)}"]
    all_terms = [term1, term2] + unlikes
    rng.shuffle(all_terms)
    terms_str = ", ".join(all_terms)

    return {
        "title": "Identifying Like Terms from a Set of Algebraic Terms",
        "topic": "Algebraic expressions 1",
        "grade": 8,
        "term": 2,
        "subskill": "10_identifying_like_terms_from_list",
        "difficulty": "easy",
        "question_text": (
            f"From the following list of terms:\n\n"
            f"$${terms_str}$$\n\n"
            "Identify the **two like terms**."
        ),
        "correct_answer": f"{term1} and {term2}",
        "marking_schema": [
            f"Identify pair of like terms: {term1} and {term2} [1 mark]",
        ],
        "hints": [
            "Like terms must have identical variables raised to the exact same exponents.",
            f"Look for the two terms that both have ${v}^2$.",
            f"The like terms are {term1} and {term2}.",
        ],
        "misconception_tags": ["like_terms_power_distinction_error"],
        "diagram_spec": None,
    }


def arch_11_distinguishing_like_from_unlike_terms_powers(rng: random.Random) -> Dict[str, Any]:
    c1 = rng.randint(2, 6)
    c2 = rng.randint(2, 6)
    return {
        "title": "Distinguishing Like from Unlike Terms (Powers)",
        "topic": "Algebraic expressions 1",
        "grade": 8,
        "term": 2,
        "subskill": "11_distinguishing_like_from_unlike_terms_powers",
        "difficulty": "medium",
        "question_text": (
            f"Explain why the terms **${c1}x^2$** and **${c2}x^3$** are **unlike terms** "
            "and cannot be combined into a single term."
        ),
        "correct_answer": "They are unlike terms because although they share the same variable (x), they have different exponents (powers 2 and 3).",
        "marking_schema": [
            "State that exponents/powers are different (2 vs 3) [1 mark]",
            "Explain that like terms require both identical variables and identical powers [1 mark]",
        ],
        "hints": [
            "Look at the exponent on $x$ in each term.",
            "Can you add apples to oranges, or $x^2$ to $x^3$?",
            "Different powers make terms unlike.",
        ],
        "misconception_tags": ["combining_unlike_powers_error"],
        "diagram_spec": None,
    }


def arch_12_distinguishing_like_from_unlike_terms_variables(rng: random.Random) -> Dict[str, Any]:
    c1 = rng.randint(3, 7)
    c2 = rng.randint(3, 7)
    return {
        "title": "Distinguishing Like from Unlike Terms (Variables)",
        "topic": "Algebraic expressions 1",
        "grade": 8,
        "term": 2,
        "subskill": "12_distinguishing_like_from_unlike_terms_variables",
        "difficulty": "medium",
        "question_text": (
            f"Explain why **${c1}ab$** and **${c2}a^2b$** are **unlike terms**."
        ),
        "correct_answer": "In the term a^2b, the variable a is raised to the power of 2, whereas in ab, the variable a is raised to the power of 1. Therefore, their variable factors are not identical.",
        "marking_schema": [
            "Point out that the exponent of $a$ differs ($a^1$ vs $a^2$) [1 mark]",
            "Conclude that terms are unlike [1 mark]",
        ],
        "hints": [
            "Compare the exponent of $a$ in $ab$ ($a^1$) with the exponent of $a$ in $a^2b$ ($a^2$).",
            "Since the powers on variable $a$ are not equal, they are unlike terms.",
        ],
        "misconception_tags": ["multivariable_power_confusion"],
        "diagram_spec": None,
    }


def arch_13_combining_linear_like_terms_positive_coefficients(rng: random.Random) -> Dict[str, Any]:
    c1 = rng.randint(2, 6)
    c2 = rng.randint(3, 8)
    c3 = rng.randint(2, 7)
    tot = c1 + c2 + c3
    return {
        "title": "Combining Linear Like Terms (Positive Coefficients)",
        "topic": "Algebraic expressions 1",
        "grade": 8,
        "term": 2,
        "subskill": "13_combining_linear_like_terms_positive_coefficients",
        "difficulty": "easy",
        "question_text": (
            f"Simplify the expression by combining like terms:\n\n"
            f"$${c1}x + {c2}x + {c3}x$$"
        ),
        "correct_answer": f"{tot}x",
        "marking_schema": [
            f"Add coefficients: {c1} + {c2} + {c3} = {tot} [1 mark]",
            f"Correct simplified term: {tot}x [1 mark]",
        ],
        "hints": [
            "Since all terms have the exact same variable $x$, add their coefficients together.",
            f"{c1} + {c2} + {c3} = {tot}.",
            f"Result = {tot}x.",
        ],
        "misconception_tags": ["variable_power_addition_error"],
        "diagram_spec": None,
    }


def arch_14_combining_linear_like_terms_with_negatives(rng: random.Random) -> Dict[str, Any]:
    c1 = rng.randint(7, 12)
    c2 = rng.randint(2, 5)
    c3 = rng.randint(3, 6)
    c4 = rng.randint(1, 4)
    tot = c1 - c2 + c3 - c4
    return {
        "title": "Combining Linear Like Terms with Positive and Negative Coefficients",
        "topic": "Algebraic expressions 1",
        "grade": 8,
        "term": 2,
        "subskill": "14_combining_linear_like_terms_with_negatives",
        "difficulty": "medium",
        "question_text": (
            f"Simplify the expression:\n\n"
            f"$${c1}x - {c2}x + {c3}x - {c4}x$$"
        ),
        "correct_answer": f"{tot}x",
        "marking_schema": [
            f"Perform integer operations: {c1} - {c2} + {c3} - {c4} = {tot} [1 mark]",
            f"Final answer: {tot}x [1 mark]",
        ],
        "hints": [
            f"Group positive terms: ({c1} + {c3})x = {c1 + c3}x.",
            f"Group negative terms: (-{c2} - {c4})x = -{c2 + c4}x.",
            f"Combine: {c1 + c3} - {c2 + c4} = {tot}x.",
        ],
        "misconception_tags": ["negative_coefficient_arithmetic_error"],
        "diagram_spec": None,
    }


def arch_15_combining_quadratic_and_linear_like_terms(rng: random.Random) -> Dict[str, Any]:
    a1 = rng.randint(3, 7)
    a2 = rng.randint(2, 5)
    b1 = rng.randint(4, 9)
    b2 = rng.randint(2, 6)
    tot_sq = a1 + a2
    tot_lin = b1 - b2
    sign = "+" if tot_lin >= 0 else "-"
    abs_lin = abs(tot_lin)

    return {
        "title": "Combining Quadratic and Linear Like Terms",
        "topic": "Algebraic expressions 1",
        "grade": 8,
        "term": 2,
        "subskill": "15_combining_quadratic_and_linear_like_terms",
        "difficulty": "medium",
        "question_text": (
            f"Simplify the following algebraic expression:\n\n"
            f"$${a1}x^2 + {b1}x + {a2}x^2 - {b2}x$$"
        ),
        "correct_answer": f"{tot_sq}x^2 {sign} {abs_lin}x",
        "marking_schema": [
            f"Combine $x^2$ terms: {a1} + {a2} = {tot_sq}x^2 [1 mark]",
            f"Combine $x$ terms: {b1} - {b2} = {tot_lin}x [1 mark]",
        ],
        "hints": [
            f"Group like terms: ({a1}x^2 + {a2}x^2) + ({b1}x - {b2}x).",
            f"Simplify $x^2$ terms: {tot_sq}x^2.",
            f"Simplify $x$ terms: {tot_lin}x.",
        ],
        "misconception_tags": ["mixing_powers_when_combining"],
        "diagram_spec": None,
    }


def arch_16_combining_multivariable_like_terms(rng: random.Random) -> Dict[str, Any]:
    c1 = rng.randint(3, 8)
    c2 = rng.randint(4, 9)
    c3 = rng.randint(2, 5)
    tot = c1 + c2 - c3
    return {
        "title": "Combining Multivariable Like Terms ($xy$)",
        "topic": "Algebraic expressions 1",
        "grade": 8,
        "term": 2,
        "subskill": "16_combining_multivariable_like_terms",
        "difficulty": "medium",
        "question_text": (
            f"Simplify by combining like terms:\n\n"
            f"$${c1}xy + {c2}xy - {c3}xy$$"
        ),
        "correct_answer": f"{tot}xy",
        "marking_schema": [
            f"Combine coefficients ({c1} + {c2} - {c3}) = {tot} [1 mark]",
            f"Result: {tot}xy [1 mark]",
        ],
        "hints": [
            "All terms have the exact same variable factor $xy$.",
            f"Calculate {c1} + {c2} - {c3} = {tot}.",
            f"Simplified answer = {tot}xy.",
        ],
        "misconception_tags": ["multivariable_product_combining_error"],
        "diagram_spec": None,
    }


def arch_17_rearranging_and_simplifying_trinomial_terms(rng: random.Random) -> Dict[str, Any]:
    a1 = rng.randint(2, 5)
    a2 = rng.randint(1, 4)
    b1 = rng.randint(3, 7)
    b2 = rng.randint(1, 4)
    c1 = rng.randint(4, 9)
    c2 = rng.randint(1, 3)

    tot_a = a1 - a2
    tot_b = b1 + b2
    tot_c = c1 - c2

    return {
        "title": "Rearranging and Simplifying Polynomials in Descending Powers",
        "topic": "Algebraic expressions 1",
        "grade": 8,
        "term": 2,
        "subskill": "17_rearranging_and_simplifying_trinomial_terms",
        "difficulty": "medium",
        "question_text": (
            f"Rearrange terms and simplify into descending powers of $x$:\n\n"
            f"$${b1}x + {a1}x^2 + {c1} - {a2}x^2 + {b2}x - {c2}$$"
        ),
        "correct_answer": f"{tot_a}x^2 + {tot_b}x + {tot_c}",
        "marking_schema": [
            f"Combine $x^2$ terms: ({a1} - {a2})x^2 = {tot_a}x^2 [1 mark]",
            f"Combine $x$ terms: ({b1} + {b2})x = {tot_b}x [1 mark]",
            f"Combine constant terms: {c1} - {c2} = {tot_c} [1 mark]",
        ],
        "hints": [
            f"Group like terms: ({a1}x^2 - {a2}x^2) + ({b1}x + {b2}x) + ({c1} - {c2}).",
            f"Combine each group separately.",
            f"Write in descending powers: {tot_a}x^2 + {tot_b}x + {tot_c}.",
        ],
        "misconception_tags": ["descending_powers_ordering_error"],
        "diagram_spec": None,
    }


def arch_18_evaluating_linear_expression_positive_integer(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(3, 8)
    b = rng.randint(2, 10)
    x_val = rng.randint(2, 6)
    ans = a * x_val + b

    return {
        "title": "Evaluating a Linear Expression (Positive Integer Substitution)",
        "topic": "Algebraic expressions 1",
        "grade": 8,
        "term": 2,
        "subskill": "18_evaluating_linear_expression_positive_integer",
        "difficulty": "easy",
        "question_text": (
            f"Evaluate the expression **${a}x + {b}$** if **$x = {x_val}$**."
        ),
        "correct_answer": str(ans),
        "marking_schema": [
            f"Substitute $x = {x_val}$: {a}({x_val}) + {b} = {a * x_val} + {b} [1 mark]",
            f"Final numerical answer: {ans} [1 mark]",
        ],
        "hints": [
            f"Replace $x$ with ({x_val}): {a} x ({x_val}) + {b}.",
            f"Calculate multiplication first: {a * x_val}.",
            f"Then add {b}: {a * x_val} + {b} = {ans}.",
        ],
        "misconception_tags": ["order_of_operations_substitution_error"],
        "diagram_spec": None,
    }


def arch_19_evaluating_linear_expression_negative_integer(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(3, 7)
    b = rng.randint(2, 8)
    x_val = -rng.randint(2, 5)
    ans = a * x_val - b

    return {
        "title": "Evaluating a Linear Expression (Negative Integer Substitution)",
        "topic": "Algebraic expressions 1",
        "grade": 8,
        "term": 2,
        "subskill": "19_evaluating_linear_expression_negative_integer",
        "difficulty": "medium",
        "question_text": (
            f"Find the numerical value of **${a}x - {b}$** when **$x = {x_val}$**."
        ),
        "correct_answer": str(ans),
        "marking_schema": [
            f"Substitute $x = {x_val}$: {a}({x_val}) - {b} = {a * x_val} - {b} [1 mark]",
            f"Result: {ans} [1 mark]",
        ],
        "hints": [
            f"Substitute ({x_val}) into the expression: {a}({x_val}) - {b}.",
            f"Multiply positive by negative: {a} x ({x_val}) = {a * x_val}.",
            f"Subtract {b}: {a * x_val} - {b} = {ans}.",
        ],
        "misconception_tags": ["negative_multiplication_sign_error"],
        "diagram_spec": None,
    }


def arch_20_evaluating_quadratic_expression_positive_integer(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([2, 3])
    b = rng.randint(2, 5)
    c = rng.randint(1, 6)
    x_val = rng.randint(2, 4)
    sq_part = a * (x_val ** 2)
    lin_part = b * x_val
    ans = sq_part + lin_part - c

    return {
        "title": "Evaluating a Quadratic Expression (Positive Integer)",
        "topic": "Algebraic expressions 1",
        "grade": 8,
        "term": 2,
        "subskill": "20_evaluating_quadratic_expression_positive_integer",
        "difficulty": "medium",
        "question_text": (
            f"Calculate the value of the expression:\n\n"
            f"$${a}x^2 + {b}x - {c}$$\n\n"
            f"when **$x = {x_val}$**."
        ),
        "correct_answer": str(ans),
        "marking_schema": [
            f"Evaluate powers: ({x_val})^2 = {x_val**2} and {a}({x_val**2}) = {sq_part} [1 mark]",
            f"Substitute and simplify: {sq_part} + {lin_part} - {c} = {ans} [1 mark]",
        ],
        "hints": [
            f"First calculate $x^2$: ({x_val})^2 = {x_val**2}.",
            f"Multiply by {a}: {a} x {x_val**2} = {sq_part}.",
            f"Add {b}({x_val}) and subtract {c}: {sq_part} + {lin_part} - {c} = {ans}.",
        ],
        "misconception_tags": ["exponent_before_multiplication_error"],
        "diagram_spec": None,
    }


def arch_21_evaluating_quadratic_expression_negative_integer(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([2, 3])
    b = rng.randint(2, 5)
    c = rng.randint(2, 7)
    x_val = -rng.randint(2, 3)
    sq_part = a * (x_val ** 2)
    lin_part = b * x_val
    ans = sq_part + lin_part + c

    return {
        "title": "Evaluating a Quadratic Expression (Negative Integer Substitution)",
        "topic": "Algebraic expressions 1",
        "grade": 8,
        "term": 2,
        "subskill": "21_evaluating_quadratic_expression_negative_integer",
        "difficulty": "hard",
        "question_text": (
            f"Evaluate **${a}x^2 + {b}x + {c}$** when **$x = {x_val}$**."
        ),
        "correct_answer": str(ans),
        "marking_schema": [
            f"Squaring negative integer: ({x_val})^2 = {x_val**2} [1 mark]",
            f"Full substitution: {a}({x_val**2}) + {b}({x_val}) + {c} = {sq_part} + ({lin_part}) + {c} = {ans} [1 mark]",
        ],
        "hints": [
            f"Remember that a negative number squared becomes positive: ({x_val})^2 = +{x_val**2}.",
            f"{a}({x_val**2}) = {sq_part}.",
            f"{b}({x_val}) = {lin_part}.",
            f"Add all parts: {sq_part} + ({lin_part}) + {c} = {ans}.",
        ],
        "misconception_tags": ["negative_squared_becomes_negative_misconception"],
        "diagram_spec": None,
    }


def arch_22_evaluating_expression_with_fractional_input(rng: random.Random) -> Dict[str, Any]:
    denom = rng.choice([2, 3, 4])
    k = rng.choice([1, 2, 3])
    x_val = k * denom
    b = rng.randint(3, 8)
    ans = k + b

    return {
        "title": "Evaluating an Algebraic Expression with a Division/Fraction",
        "topic": "Algebraic expressions 1",
        "grade": 8,
        "term": 2,
        "subskill": "22_evaluating_expression_with_fractional_input",
        "difficulty": "medium",
        "question_text": (
            f"Evaluate the expression:\n\n"
            f"$$\\frac{{x}}{{{denom}}} + {b}$$\n\n"
            f"when **$x = {x_val}$**."
        ),
        "correct_answer": str(ans),
        "marking_schema": [
            f"Divide $x$ by {denom}: {x_val}/{denom} = {k} [1 mark]",
            f"Add {b}: {k} + {b} = {ans} [1 mark]",
        ],
        "hints": [
            f"Substitute {x_val} into the numerator: \\frac{{{x_val}}}{{{denom}}}.",
            f"Simplify the fraction: {x_val} ÷ {denom} = {k}.",
            f"Add {b}: {k} + {b} = {ans}.",
        ],
        "misconception_tags": ["fraction_substitution_error"],
        "diagram_spec": None,
    }


def arch_23_evaluating_expression_with_zero(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(3, 9)
    b = rng.randint(2, 8)
    c = rng.randint(3, 7)
    const = rng.randint(4, 15)
    sign = rng.choice(["+", "-"])
    ans = const if sign == "+" else -const

    return {
        "title": "Evaluating a Polynomial Expression at Zero ($x = 0$)",
        "topic": "Algebraic expressions 1",
        "grade": 8,
        "term": 2,
        "subskill": "23_evaluating_expression_with_zero",
        "difficulty": "easy",
        "question_text": (
            f"Find the value of:\n\n"
            f"$${a}x^3 - {b}x^2 + {c}x {sign} {const}$$\n\n"
            f"when **$x = 0$**."
        ),
        "correct_answer": str(ans),
        "marking_schema": [
            f"Recognize that all variable terms evaluate to 0 [1 mark]",
            f"State remaining constant term: {ans} [1 mark]",
        ],
        "hints": [
            "Any number multiplied by 0 equals 0.",
            f"{a}(0)^3 - {b}(0)^2 + {c}(0) = 0 - 0 + 0 = 0.",
            f"Only the constant term remains: {ans}.",
        ],
        "misconception_tags": ["zero_substitution_elimination_gap"],
        "diagram_spec": None,
    }


def arch_24_verifying_equivalent_expressions_substitution(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(2, 5)
    b = rng.randint(2, 5)
    v1 = 2
    v2 = 5
    res1 = a * (v1 + b)
    res2 = a * (v2 + b)

    return {
        "title": "Verifying Equivalent Expressions by Substitution",
        "topic": "Algebraic expressions 1",
        "grade": 8,
        "term": 2,
        "subskill": "24_verifying_equivalent_expressions_substitution",
        "difficulty": "medium",
        "question_text": (
            f"Consider Expression A: **${a}(x + {b})$** and Expression B: **${a}x + {a * b}$**.\n\n"
            f"1. Evaluate both expressions for **$x = {v1}$**.\n"
            f"2. Evaluate both expressions for **$x = {v2}$**.\n"
            "3. State whether Expression A and Expression B are equivalent."
        ),
        "correct_answer": f"1. Both equal {res1}. 2. Both equal {res2}. 3. Yes, they are equivalent expressions.",
        "marking_schema": [
            f"Correct substitution at x={v1} (both equal {res1}) [1 mark]",
            f"Correct substitution at x={v2} (both equal {res2}) [1 mark]",
            "Conclude that expressions are equivalent [1 mark]",
        ],
        "hints": [
            f"For x={v1}: Expression A is {a}({v1} + {b}) = {res1}; Expression B is {a}({v1}) + {a*b} = {res1}.",
            f"For x={v2}: calculate both values.",
            "Since they produce the same numerical output for all values of $x$, they are equivalent.",
        ],
        "misconception_tags": ["equivalent_expression_verification_gap"],
        "diagram_spec": None,
    }


def arch_25_distinguishing_equivalent_from_non_equivalent_expressions(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(2, 5)
    b = rng.randint(2, 6)
    val_a = a * (1 + b)
    val_b = a * 1 + b

    return {
        "title": "Distinguishing Equivalent from Non-Equivalent Expressions",
        "topic": "Algebraic expressions 1",
        "grade": 8,
        "term": 2,
        "subskill": "25_distinguishing_equivalent_from_non_equivalent_expressions",
        "difficulty": "medium",
        "question_text": (
            f"A learner claims that **${a}(x + {b})$** and **${a}x + {b}$** are equivalent expressions.\n\n"
            f"Evaluate both expressions at **$x = 1$** to show whether this claim is true or false. "
            "Explain the learner's algebraic error."
        ),
        "correct_answer": f"False. At x = 1: {a}(1 + {b}) = {val_a}, whereas {a}(1) + {b} = {val_b}. The learner forgot to multiply the constant {b} by {a} when applying the distributive property.",
        "marking_schema": [
            f"Show values differ: {val_a} ≠ {val_b} [1 mark]",
            f"State claim is false and explain omission of distributing {a} to {b} [1 mark]",
        ],
        "hints": [
            f"Substitute x = 1 into {a}(x + {b}): {a}(1 + {b}) = {val_a}.",
            f"Substitute x = 1 into {a}x + {b}: {a}(1) + {b} = {val_b}.",
            f"Since {val_a} ≠ {val_b}, the expressions are not equivalent.",
        ],
        "misconception_tags": ["distributive_bracket_omission_fallacy"],
        "diagram_spec": None,
    }


BUILDERS_01_25 = [
    arch_01_translating_word_phrase_sum_product_to_expression,
    arch_02_translating_word_phrase_difference_quotient_to_expression,
    arch_03_translating_flow_diagram_to_expression,
    arch_04_identifying_number_of_terms_in_expression,
    arch_05_classifying_monomial_binomial_trinomial_polynomial,
    arch_06_identifying_variable_and_constant_term,
    arch_07_identifying_coefficient_of_linear_term,
    arch_08_identifying_coefficient_of_squared_term,
    arch_09_determining_degree_of_univariate_polynomial,
    arch_10_identifying_like_terms_from_list,
    arch_11_distinguishing_like_from_unlike_terms_powers,
    arch_12_distinguishing_like_from_unlike_terms_variables,
    arch_13_combining_linear_like_terms_positive_coefficients,
    arch_14_combining_linear_like_terms_with_negatives,
    arch_15_combining_quadratic_and_linear_like_terms,
    arch_16_combining_multivariable_like_terms,
    arch_17_rearranging_and_simplifying_trinomial_terms,
    arch_18_evaluating_linear_expression_positive_integer,
    arch_19_evaluating_linear_expression_negative_integer,
    arch_20_evaluating_quadratic_expression_positive_integer,
    arch_21_evaluating_quadratic_expression_negative_integer,
    arch_22_evaluating_expression_with_fractional_input,
    arch_23_evaluating_expression_with_zero,
    arch_24_verifying_equivalent_expressions_substitution,
    arch_25_distinguishing_equivalent_from_non_equivalent_expressions,
]
