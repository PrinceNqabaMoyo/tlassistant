"""Grade 9 Mathematics - Algebraic Expressions 1 Archetypes (01 to 25).
Grounded strictly in:
  - curriculum_docs/Mathematics_Gr9/Algebraic Expressions Studio.md
  - curriculum_docs_auto/Mathematics_Gr9/Term 1/06. Algebraic expressions 1.md

Covers:
  - Algebraic language: variables, constants, coefficients, degree, monomial/binomial/trinomial, term counts
  - Substitution and order of operations (positive, negative, fractional)
  - Verbal instructions to expressions and bracket importance
  - Flow diagrams and graphical geometric substitutions
  - Like terms grouping, polynomial addition and subtraction
  - Distributive law (monomial * polynomial)
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from .algebraic_expressions_svg import (
    draw_algebraic_flow_diagram_svg,
    draw_algebraic_rectangle_svg,
    draw_algebraic_triangle_svg,
)


def arch_01_identify_variable_in_given_expression(rng: random.Random) -> Dict[str, Any]:
    """Identify the variable letter in a given polynomial."""
    var = rng.choice(["x", "y", "a", "b", "p", "m", "t", "k"])
    c2 = rng.choice([2, 3, 4, 5, 6, 7])
    c1 = rng.choice([-8, -6, -5, 4, 5, 9])
    c0 = rng.choice([-15, -12, -7, 8, 11, 20])
    s1 = f"- {abs(c1)}" if c1 < 0 else f"+ {c1}"
    s0 = f"- {abs(c0)}" if c0 < 0 else f"+ {c0}"
    expr = f"{c2}{var}^2 {s1}{var} {s0}"

    return {
        "subskill": "01_identify_variable_in_given_expression",
        "question_text": (
            f"Consider the algebraic expression:\n$${expr}$$\n\n"
            f"Identify the letter symbol that represents the **variable** in this expression."
        ),
        "correct_answer": var,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Identify the letter representing the variable: {var}", "marks": 1},
        ],
        "hints": [
            "A variable is a letter symbol that represents an unknown or changing quantity.",
            f"Look for the alphabet letter present alongside numbers in $${expr}$$.",
            f"The variable is ${var}$.",
        ],
    }


def arch_02_identify_constant_term_in_polynomial(rng: random.Random) -> Dict[str, Any]:
    """Identify the constant term in a univariate polynomial."""
    var = rng.choice(["x", "y", "a", "p"])
    a = rng.choice([2, 3, 5, 7])
    b = rng.choice([-9, -4, 4, 6, 8])
    c = rng.choice([-19, -14, -11, -8, -5, 7, 12, 15, 23])
    sb = f"- {abs(b)}" if b < 0 else f"+ {b}"
    sc = f"- {abs(c)}" if c < 0 else f"+ {c}"
    expr = f"{a}{var}^2 {sb}{var} {sc}"

    return {
        "subskill": "02_identify_constant_term_in_polynomial",
        "question_text": (
            f"Consider the expression:\n$${expr}$$\n\n"
            f"State the value of the **constant term**."
        ),
        "correct_answer": str(c),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Identify the standalone numerical term including sign: {c}", "marks": 1},
        ],
        "hints": [
            "A constant term is a number whose value never changes and has no variable attached.",
            f"Look at the term at the end that does not contain ${var}$. Remember to include its sign.",
            f"The constant term is ${c}$.",
        ],
    }


def arch_03_identify_coefficient_of_linear_term(rng: random.Random) -> Dict[str, Any]:
    """Identify the coefficient of the linear (degree 1) term."""
    var = rng.choice(["x", "y", "m", "p"])
    a = rng.choice([3, 4, 5, 6])
    b = rng.choice([-8, -7, -5, -3, 2, 4, 7, 9])
    c = rng.choice([-12, -6, 5, 11])
    sb = f"- {abs(b)}" if b < 0 else f"+ {b}"
    sc = f"- {abs(c)}" if c < 0 else f"+ {c}"
    expr = f"{a}{var}^2 {sb}{var} {sc}"

    return {
        "subskill": "03_identify_coefficient_of_linear_term",
        "question_text": (
            f"Given the quadratic expression:\n$${expr}$$\n\n"
            f"Determine the **coefficient of ${var}$**."
        ),
        "correct_answer": str(b),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Identify the numerical factor multiplying {var}, including its sign: {b}", "marks": 1},
        ],
        "hints": [
            f"The coefficient of a term is the numerical multiplier in front of the variable.",
            f"Find the term containing ${var}$ (not ${var}^2$) and note the number and sign preceding it.",
            f"The coefficient of ${var}$ is ${b}$.",
        ],
    }


def arch_04_identify_coefficient_of_squared_term(rng: random.Random) -> Dict[str, Any]:
    """Identify the coefficient of the squared (quadratic) term."""
    var = rng.choice(["x", "y", "a", "k"])
    a = rng.choice([-9, -7, -4, -1, 1, 2, 3, 5, 8])
    b = rng.choice([-5, 3, 6])
    c = rng.choice([-10, 4, 15])
    a_str = f"-{var}^2" if a == -1 else (f"{var}^2" if a == 1 else f"{a}{var}^2")
    sb = f"- {abs(b)}" if b < 0 else f"+ {b}"
    sc = f"- {abs(c)}" if c < 0 else f"+ {c}"
    expr = f"{a_str} {sb}{var} {sc}"

    return {
        "subskill": "04_identify_coefficient_of_squared_term",
        "question_text": (
            f"Given the polynomial expression:\n$${expr}$$\n\n"
            f"State the **coefficient of ${var}^2$**."
        ),
        "correct_answer": str(a),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Identify the numerical coefficient of {var}^2: {a}", "marks": 1},
        ],
        "hints": [
            f"Look at the term with power 2: ${var}^2$.",
            f"If there is just a minus sign in front of ${var}^2$, the coefficient is $-1$. If no number is shown, it is $1$.",
            f"The coefficient of ${var}^2$ is ${a}$.",
        ],
    }


def arch_05_determine_degree_of_univariate_polynomial(rng: random.Random) -> Dict[str, Any]:
    """Determine the degree of a polynomial in one variable."""
    var = "x"
    degree = rng.choice([2, 3, 4, 5])
    coeffs = [rng.choice([2, 3, 4, 5])] + [rng.choice([-6, -2, 3, 7]) for _ in range(degree)]
    terms = [f"{coeffs[0]}x^{degree}"]
    for p in range(degree - 1, 0, -1):
        c = coeffs[degree - p]
        sign = f"- {abs(c)}" if c < 0 else f"+ {c}"
        terms.append(f"{sign}x^{p}" if p > 1 else f"{sign}x")
    const = coeffs[-1]
    sign_c = f"- {abs(const)}" if const < 0 else f"+ {const}"
    terms.append(sign_c)
    expr = " ".join(terms)

    return {
        "subskill": "05_determine_degree_of_univariate_polynomial",
        "question_text": (
            f"Consider the polynomial:\n$${expr}$$\n\n"
            f"What is the **degree** of this polynomial?"
        ),
        "correct_answer": str(degree),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Identify highest exponent of the variable x: {degree}", "marks": 1},
        ],
        "hints": [
            "The degree of a polynomial in a single variable is the highest exponent (power) of that variable.",
            f"Scan the powers of $x$ in each term: the exponents are {list(range(degree, 0, -1))}.",
            f"The highest exponent is ${degree}$, so the degree is ${degree}$.",
        ],
    }


def arch_06_classify_expression_as_monomial_binomial_trinomial(rng: random.Random) -> Dict[str, Any]:
    """Classify an algebraic expression by number of terms."""
    choice = rng.choice(["monomial", "binomial", "trinomial"])
    if choice == "monomial":
        coeff = rng.choice([-7, -4, 3, 5, 8])
        p = rng.choice([1, 2, 3])
        expr = f"{coeff}x^{p}" if p > 1 else f"{coeff}x"
        ans = "monomial"
    elif choice == "binomial":
        a = rng.choice([2, 3, 5])
        b = rng.choice([-8, -3, 4, 7])
        sign = f"- {abs(b)}" if b < 0 else f"+ {b}"
        expr = f"{a}x^2 {sign}"
        ans = "binomial"
    else:
        a = rng.choice([2, 4])
        b = rng.choice([-5, 3])
        c = rng.choice([-7, 6])
        sb = f"- {abs(b)}" if b < 0 else f"+ {b}"
        sc = f"- {abs(c)}" if c < 0 else f"+ {c}"
        expr = f"{a}x^2 {sb}x {sc}"
        ans = "trinomial"

    return {
        "subskill": "06_classify_expression_as_monomial_binomial_trinomial",
        "question_text": (
            f"Classify the algebraic expression below as a **monomial**, **binomial**, or **trinomial**:\n"
            f"$${expr}$$\n\n"
            f"Enter your answer as a single word (monomial, binomial, or trinomial)."
        ),
        "correct_answer": ans,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Count terms separated by addition/subtraction and classify as {ans}", "marks": 1},
        ],
        "hints": [
            "Monomial has 1 term; binomial has 2 terms; trinomial has 3 terms.",
            f"Count the terms in $${expr}$$ separated by plus or minus signs.",
            f"It has {1 if ans == 'monomial' else (2 if ans == 'binomial' else 3)} term(s), so it is a {ans}.",
        ],
    }


def arch_07_count_number_of_terms_separated_by_plus_minus(rng: random.Random) -> Dict[str, Any]:
    """Count the total number of terms in an expression separated by + and - signs."""
    num_terms = rng.choice([2, 3, 4, 5])
    var = "x"
    parts = []
    for i in range(num_terms):
        c = rng.choice([2, 3, 4, 5, 7])
        p = num_terms - i - 1
        term = f"{c}{var}^{p}" if p > 1 else (f"{c}{var}" if p == 1 else f"{c}")
        if i == 0:
            parts.append(term)
        else:
            sign = rng.choice(["+", "-"])
            parts.append(f"{sign} {term}")
    expr = " ".join(parts)

    return {
        "subskill": "07_count_number_of_terms_separated_by_plus_minus",
        "question_text": (
            f"How many terms are in the algebraic expression:\n$${expr}$$\n\n"
            f"Enter an integer count."
        ),
        "correct_answer": str(num_terms),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Count distinct terms separated by + or - operators: {num_terms}", "marks": 1},
        ],
        "hints": [
            "Terms are mathematical entities separated by addition (+) or subtraction (-) signs.",
            "Multiplication and division do not separate terms, but + and - outside of brackets do.",
            f"There are {num_terms} terms in this expression.",
        ],
    }


def arch_08_evaluate_linear_expression_positive_integer_substitution(rng: random.Random) -> Dict[str, Any]:
    """Evaluate ax + b when x is a positive integer."""
    m = rng.choice([3, 4, 5, 6, 7])
    c = rng.choice([-15, -9, -4, 5, 8, 12])
    x_val = rng.choice([2, 3, 4, 5, 6])
    ans = m * x_val + c
    sc = f"- {abs(c)}" if c < 0 else f"+ {c}"

    return {
        "subskill": "08_evaluate_linear_expression_positive_integer_substitution",
        "question_text": (
            f"Evaluate the numerical value of the expression:\n$${m}x {sc}$$\n\n"
            f"when **$x = {x_val}$**."
        ),
        "correct_answer": str(ans),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Substitute x = {x_val}: {m}({x_val}) {sc}", "marks": 1},
            {"step": f"Compute result: {m * x_val} {sc} = {ans}", "marks": 1},
        ],
        "hints": [
            f"Replace $x$ with ${x_val}$ in the expression.",
            f"Calculate the multiplication first: ${m} \\times {x_val} = {m * x_val}$.",
            f"Now add/subtract ${c}$: ${m * x_val} {sc} = {ans}$.",
        ],
    }


def arch_09_evaluate_linear_expression_negative_integer_substitution(rng: random.Random) -> Dict[str, Any]:
    """Evaluate ax + b when x is a negative integer."""
    m = rng.choice([2, 3, 4, 5])
    c = rng.choice([-10, -7, 4, 9, 14])
    x_val = rng.choice([-5, -4, -3, -2])
    ans = m * x_val + c
    sc = f"- {abs(c)}" if c < 0 else f"+ {c}"

    return {
        "subskill": "09_evaluate_linear_expression_negative_integer_substitution",
        "question_text": (
            f"Calculate the value of the expression:\n$${m}x {sc}$$\n\n"
            f"when **$x = {x_val}$**."
        ),
        "correct_answer": str(ans),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Substitute x = {x_val} into expression: {m}({x_val}) {sc}", "marks": 1},
            {"step": f"Calculate {m * x_val} {sc} = {ans}", "marks": 1},
        ],
        "hints": [
            f"Always use brackets when substituting a negative number: ${m}({x_val}) {sc}$.",
            f"Multiply: positive $\\times$ negative is negative: ${m} \\times ({x_val}) = {m * x_val}$.",
            f"Combine: ${m * x_val} {sc} = {ans}$.",
        ],
    }


def arch_10_evaluate_quadratic_expression_negative_substitution(rng: random.Random) -> Dict[str, Any]:
    """Evaluate ax^2 + bx + c when x is negative."""
    a = rng.choice([2, 3, 4])
    b = rng.choice([-5, -3, 3, 5])
    c = rng.choice([-8, -2, 6, 10])
    x_val = rng.choice([-3, -2, -1])
    ans = a * (x_val**2) + b * x_val + c
    sb = f"- {abs(b)}" if b < 0 else f"+ {b}"
    sc = f"- {abs(c)}" if c < 0 else f"+ {c}"

    return {
        "subskill": "10_evaluate_quadratic_expression_negative_substitution",
        "question_text": (
            f"Evaluate the quadratic expression:\n$${a}x^2 {sb}x {sc}$$\n\n"
            f"for **$x = {x_val}$**."
        ),
        "correct_answer": str(ans),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Substitute x = {x_val}: {a}({x_val})^2 {sb}({x_val}) {sc}", "marks": 1},
            {"step": f"Evaluate power ({x_val})^2 = {x_val**2}", "marks": 1},
            {"step": f"Calculate final total: {ans}", "marks": 1},
        ],
        "hints": [
            f"Remember that squaring a negative gives a positive: $({x_val})^2 = {x_val**2}$.",
            f"Substitute: ${a}({x_val**2}) {sb}({x_val}) {sc} = {a * (x_val**2)} + ({b * x_val}) {sc}$.",
            f"Sum the terms to obtain ${ans}$.",
        ],
    }


def arch_11_evaluate_expression_with_fractional_substitution(rng: random.Random) -> Dict[str, Any]:
    """Evaluate an expression with fraction division: (ax + b) / c."""
    c = rng.choice([2, 3, 4, 5])
    k = rng.choice([3, 4, 5, 6])
    ans = k
    target = c * k  # numerator value
    a = rng.choice([2, 3, 4])
    x_val = rng.choice([2, 3, 4, 5])
    b = target - a * x_val
    sb = f"- {abs(b)}" if b < 0 else f"+ {b}"

    return {
        "subskill": "11_evaluate_expression_with_fractional_substitution",
        "question_text": (
            f"Evaluate the value of the algebraic fraction:\n$$\\frac{{{a}x {sb}}}{{{c}}}$$\n\n"
            f"when **$x = {x_val}$**."
        ),
        "correct_answer": str(ans),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Substitute x = {x_val} into the numerator: {a}({x_val}) {sb} = {target}", "marks": 1},
            {"step": f"Divide numerator by {c}: {target} / {c} = {ans}", "marks": 1},
        ],
        "hints": [
            f"First substitute $x = {x_val}$ into the numerator: ${a}({x_val}) {sb}$.",
            f"Compute the numerator: ${a * x_val} {sb} = {target}$.",
            f"Now divide by ${c}$: $\\frac{{{target}}}{{{c}}} = {ans}$.",
        ],
    }


def arch_12_verbal_description_to_algebraic_expression_basic(rng: random.Random) -> Dict[str, Any]:
    """Translate verbal description: 'Multiply a number x by m and subtract/add c'."""
    m = rng.choice([4, 5, 6, 7, 8])
    c = rng.choice([2, 3, 5, 9, 11])
    op = rng.choice(["add", "subtract"])
    if op == "add":
        phrase = f"Multiply a number $x$ by {m} and then add {c} to the product."
        correct_expr = f"{m}x + {c}"
    else:
        phrase = f"Multiply a number $x$ by {m} and then subtract {c} from the product."
        correct_expr = f"{m}x - {c}"

    return {
        "subskill": "12_verbal_description_to_algebraic_expression_basic",
        "question_text": (
            f"Write the following computational instruction as an algebraic expression using $x$ as the input number:\n\n"
            f"**\"{phrase}\"**"
        ),
        "correct_answer": correct_expr,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Represent multiplication by {m} as {m}x", "marks": 1},
            {"step": f"Apply constant operation to obtain {correct_expr}", "marks": 1},
        ],
        "hints": [
            f"Multiplying a variable $x$ by {m} is written as ${m}x$.",
            f"Adding or subtracting {c} is placed after the term: {correct_expr}.",
            f"The final expression is ${correct_expr}$.",
        ],
    }


def arch_13_verbal_description_to_algebraic_expression_nested_brackets(rng: random.Random) -> Dict[str, Any]:
    """Translate verbal description requiring brackets: 'Add c to x, then multiply the result by m'."""
    m = rng.choice([3, 4, 5, 6])
    c = rng.choice([2, 4, 7, 8])
    op = rng.choice(["Add", "Subtract"])
    if op == "Add":
        phrase = f"Add {c} to a number $x$, and then multiply the result by {m}."
        correct_expr = f"{m}(x + {c})"
    else:
        phrase = f"Subtract {c} from a number $x$, and then multiply the result by {m}."
        correct_expr = f"{m}(x - {c})"

    return {
        "subskill": "13_verbal_description_to_algebraic_expression_nested_brackets",
        "question_text": (
            f"Write an algebraic expression for the instruction using $x$ as the variable:\n\n"
            f"**\"{phrase}\"**\n\n"
            f"(Use brackets where necessary to ensure the addition/subtraction happens before multiplication)."
        ),
        "correct_answer": correct_expr,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Identify that {op.lower()}ing {c} must occur first inside brackets: (x {'+' if op == 'Add' else '-'} {c})", "marks": 1},
            {"step": f"Multiply entire bracket by {m}: {correct_expr}", "marks": 1},
        ],
        "hints": [
            f"Because the operation states 'and then multiply the result', brackets are mandatory around the first operation.",
            f"The first operation on $x$ is $(x {'+' if op == 'Add' else '-'} {c})$.",
            f"Multiplying this result by ${m}$ gives ${correct_expr}$.",
        ],
    }


def arch_14_distinguish_bracketed_product_from_unbracketed_addition(rng: random.Random) -> Dict[str, Any]:
    """Distinguish m(x + c) from mx + c numerically for a given input."""
    m = rng.choice([3, 4, 5])
    c = rng.choice([2, 3, 4])
    x_val = rng.choice([5, 6, 7])
    val_bracket = m * (x_val + c)
    val_unbracket = m * x_val + c
    diff = val_bracket - val_unbracket

    return {
        "subskill": "14_distinguish_bracketed_product_from_unbracketed_addition",
        "question_text": (
            f"Compare the two expressions:\n"
            f"Expression A: $${m}(x + {c})$$\n"
            f"Expression B: $${m}x + {c}$$\n\n"
            f"Evaluate both expressions for **$x = {x_val}$** and state the difference: $$\\text{{Value of A}} - \\text{{Value of B}}$$"
        ),
        "correct_answer": str(diff),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Evaluate Expression A: {m}({x_val} + {c}) = {val_bracket}", "marks": 1},
            {"step": f"Evaluate Expression B: {m}({x_val}) + {c} = {val_unbracket}", "marks": 1},
            {"step": f"Compute difference: {val_bracket} - {val_unbracket} = {diff}", "marks": 1},
        ],
        "hints": [
            f"For A: Add inside brackets first: ${x_val} + {c} = {x_val + c}$, then multiply by ${m}$ to get ${val_bracket}$.",
            f"For B: Multiply first: ${m} \\times {x_val} = {m * x_val}$, then add ${c}$ to get ${val_unbracket}$.",
            f"Subtract B from A: ${val_bracket} - {val_unbracket} = {diff}$.",
        ],
    }


def arch_15_flow_diagram_to_algebraic_expression_derivation(rng: random.Random) -> Dict[str, Any]:
    """Derive algebraic expression from a seeded visual flow diagram."""
    seed = rng.randint(1, 1_000_000)
    m = rng.choice([2, 3, 4, 5])
    c = rng.choice([3, 5, 7, 9])
    ops = [f"+ {c}", f"× {m}"]
    ans_expr = f"{m}(x + {c})"
    svg = draw_algebraic_flow_diagram_svg(ops, input_label="x", output_label="Output", seed=seed)

    return {
        "subskill": "15_flow_diagram_to_algebraic_expression_derivation",
        "question_text": (
            f"Write the algebraic expression that corresponds to the operations shown in the flow diagram below, "
            f"using $x$ as the input variable:"
        ),
        "correct_answer": ans_expr,
        "tolerance": 0.0,
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
        "marking_schema": [
            {"step": f"First operation adds {c} inside brackets: (x + {c})", "marks": 1},
            {"step": f"Second operation multiplies by {m}: {ans_expr}", "marks": 1},
        ],
        "hints": [
            f"Follow the arrows from left to right: first we add {c} to $x$.",
            f"Since the whole sum is multiplied by {m}, put brackets around $x + {c}$.",
            f"The final expression is ${ans_expr}$.",
        ],
    }


def arch_16_algebraic_expression_to_flow_diagram_derivation(rng: random.Random) -> Dict[str, Any]:
    """Identify the first operation in a flow diagram for mx - c."""
    m = rng.choice([4, 6, 7, 9])
    c = rng.choice([3, 5, 8, 11])
    expr = f"{m}x - {c}"

    return {
        "subskill": "16_algebraic_expression_to_flow_diagram_derivation",
        "question_text": (
            f"If the algebraic expression $${expr}$$ is converted into a two-step flow diagram starting from input $x$, "
            f"what is the **first operation** performed on $x$? "
            f"(State as: multiply by {m}, add {c}, or subtract {c})."
        ),
        "correct_answer": f"multiply by {m}",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Recognize order of operations requires multiplication before subtraction: multiply by {m}", "marks": 1},
        ],
        "hints": [
            "According to the order of operations (BODMAS), multiplication precedes subtraction when there are no brackets.",
            f"In ${expr}$, $x$ is multiplied by ${m}$ before ${c}$ is subtracted.",
            f"The first operation is: multiply by {m}.",
        ],
    }


def arch_17_substitute_into_geometric_perimeter_formula(rng: random.Random) -> Dict[str, Any]:
    """Substitute a value of x into an algebraic perimeter formula for a rectangle."""
    seed = rng.randint(1, 1_000_000)
    a, b = rng.choice([2, 3]), rng.choice([1, 4])
    c, d = 1, rng.choice([2, 3])
    x_val = rng.choice([3, 4, 5])
    length_str = f"{a}x + {b}"
    width_str = f"x + {d}"
    
    len_val = a * x_val + b
    wid_val = c * x_val + d
    perimeter = 2 * (len_val + wid_val)
    svg = draw_algebraic_rectangle_svg(length_str, width_str, seed=seed)

    return {
        "subskill": "17_substitute_into_geometric_perimeter_formula",
        "question_text": (
            f"A rectangle has a length of $({length_str})\\text{{ cm}}$ and a breadth of $({width_str})\\text{{ cm}}$.\n\n"
            f"Calculate the **numerical perimeter** of the rectangle in cm when **$x = {x_val}$**."
        ),
        "correct_answer": str(perimeter),
        "tolerance": 0.0,
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
        "marking_schema": [
            {"step": f"Calculate length when x = {x_val}: {a}({x_val}) + {b} = {len_val}", "marks": 1},
            {"step": f"Calculate breadth when x = {x_val}: {x_val} + {d} = {wid_val}", "marks": 1},
            {"step": f"Calculate perimeter P = 2(length + breadth) = 2({len_val} + {wid_val}) = {perimeter}", "marks": 1},
        ],
        "hints": [
            f"First substitute $x = {x_val}$ into length and breadth separately.",
            f"Length $= {len_val}\\text{{ cm}}$ and breadth $= {wid_val}\\text{{ cm}}$.",
            f"Perimeter $= 2({len_val} + {wid_val}) = {perimeter}\\text{{ cm}}$.",
        ],
    }


def arch_18_substitute_into_geometric_area_formula(rng: random.Random) -> Dict[str, Any]:
    """Substitute into algebraic area formula: A = l * b."""
    seed = rng.randint(1, 1_000_000)
    a = rng.choice([2, 3, 4])
    b = rng.choice([2, 3])
    x_val = rng.choice([2, 3, 4])
    length_str = f"{a}x"
    width_str = f"{b}x"
    area = (a * x_val) * (b * x_val)
    svg = draw_algebraic_rectangle_svg(length_str, width_str, seed=seed)

    return {
        "subskill": "18_substitute_into_geometric_area_formula",
        "question_text": (
            f"A rectangular plot has length ${length_str}\\text{{ m}}$ and width ${width_str}\\text{{ m}}$.\n\n"
            f"Determine the **numerical area** of the plot in $\\text{{m}}^2$ when **$x = {x_val}$**."
        ),
        "correct_answer": str(area),
        "tolerance": 0.0,
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
        "marking_schema": [
            {"step": f"Evaluate length: {a}({x_val}) = {a * x_val}", "marks": 1},
            {"step": f"Evaluate width: {b}({x_val}) = {b * x_val}", "marks": 1},
            {"step": f"Multiply length and width: {a * x_val} * {b * x_val} = {area}", "marks": 1},
        ],
        "hints": [
            f"Area of a rectangle is $\\text{{length}} \\times \\text{{width}}$.",
            f"Substitute $x = {x_val}$: length $= {a * x_val}\\text{{ m}}$, width $= {b * x_val}\\text{{ m}}$.",
            f"Area $= {a * x_val} \\times {b * x_val} = {area}\\text{{ m}}^2$.",
        ],
    }


def arch_19_identify_and_group_like_terms_single_variable(rng: random.Random) -> Dict[str, Any]:
    """Group like terms with single variable: ax^2 + bx + cx^2 + dx."""
    a, c = rng.choice([3, 4, 5]), rng.choice([2, 3, 6])
    b, d = rng.choice([-7, -4, 2]), rng.choice([-5, 3, 8])
    total_x2 = a + c
    total_x = b + d
    sb = f"- {abs(b)}" if b < 0 else f"+ {b}"
    sd = f"- {abs(d)}" if d < 0 else f"+ {d}"
    expr = f"{a}x^2 {sb}x + {c}x^2 {sd}x"

    s_tot = f"- {abs(total_x)}" if total_x < 0 else f"+ {total_x}"
    ans = f"{total_x2}x^2 {s_tot}x"

    return {
        "subskill": "19_identify_and_group_like_terms_single_variable",
        "question_text": (
            f"Simplify the expression by collecting like terms:\n$${expr}$$\n\n"
            f"Write your simplified answer in standard descending order."
        ),
        "correct_answer": ans,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Combine squared terms: ({a} + {c})x^2 = {total_x2}x^2", "marks": 1},
            {"step": f"Combine linear terms: ({b} + {d})x = {total_x}x", "marks": 1},
            {"step": f"State final simplified expression: {ans}", "marks": 1},
        ],
        "hints": [
            "Like terms are terms that contain exactly the same variable raised to the same power.",
            f"Group the $x^2$ terms: ${a}x^2 + {c}x^2 = {total_x2}x^2$.",
            f"Group the $x$ terms: ${b}x + ({d}x) = {total_x}x$. Result is ${ans}$.",
        ],
    }


def arch_20_identify_and_group_like_terms_two_variables(rng: random.Random) -> Dict[str, Any]:
    """Group like terms with two variables: ax + by + cx - dy."""
    a, c = rng.choice([3, 5, 7]), rng.choice([2, 4, 6])
    b, d = rng.choice([4, 6, 8]), rng.choice([2, 3, 5])
    tot_x = a + c
    tot_y = b - d
    expr = f"{a}x + {b}y + {c}x - {d}y"
    sy = f"- {abs(tot_y)}" if tot_y < 0 else f"+ {tot_y}"
    ans = f"{tot_x}x {sy}y"

    return {
        "subskill": "20_identify_and_group_like_terms_two_variables",
        "question_text": (
            f"Simplify the expression by combining like terms:\n$${expr}$$"
        ),
        "correct_answer": ans,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Group x-terms: {a}x + {c}x = {tot_x}x", "marks": 1},
            {"step": f"Group y-terms: {b}y - {d}y = {tot_y}y", "marks": 1},
        ],
        "hints": [
            f"Combine terms with $x$: ${a}x + {c}x = {tot_x}x$.",
            f"Combine terms with $y$: ${b}y - {d}y = {tot_y}y$.",
            f"The final simplified expression is ${ans}$.",
        ],
    }


def arch_21_add_polynomials_combining_like_terms(rng: random.Random) -> Dict[str, Any]:
    """Add two trinomials: (ax^2 + bx + c) + (dx^2 + ex + f)."""
    a, d = rng.choice([2, 3, 4]), rng.choice([1, 2, 5])
    b, e = rng.choice([-5, -2, 3]), rng.choice([-4, 1, 6])
    c, f = rng.choice([-7, 4, 9]), rng.choice([-8, 3, 5])
    tot_a = a + d
    tot_b = b + e
    tot_c = c + f

    sb = f"- {abs(b)}" if b < 0 else f"+ {b}"
    sc = f"- {abs(c)}" if c < 0 else f"+ {c}"
    se = f"- {abs(e)}" if e < 0 else f"+ {e}"
    sf = f"- {abs(f)}" if f < 0 else f"+ {f}"
    poly1 = f"{a}x^2 {sb}x {sc}"
    poly2 = f"{d}x^2 {se}x {sf}"

    stot_b = f"- {abs(tot_b)}" if tot_b < 0 else f"+ {tot_b}"
    stot_c = f"- {abs(tot_c)}" if tot_c < 0 else f"+ {tot_c}"
    ans = f"{tot_a}x^2 {stot_b}x {stot_c}"

    return {
        "subskill": "21_add_polynomials_combining_like_terms",
        "question_text": (
            f"Add the following polynomials:\n$$({poly1}) + ({poly2})$$"
        ),
        "correct_answer": ans,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Combine x^2 terms: ({a} + {d})x^2 = {tot_a}x^2", "marks": 1},
            {"step": f"Combine x terms: ({b} + {e})x = {tot_b}x", "marks": 1},
            {"step": f"Combine constant terms: {c} + {f} = {tot_c}", "marks": 1},
        ],
        "hints": [
            "Remove brackets and group matching degree terms together.",
            f"Add coefficients: $x^2$: {tot_a}, $x$: {tot_b}, constant: {tot_c}.",
            f"The sum is ${ans}$.",
        ],
    }


def arch_22_subtract_polynomials_distributing_negative_sign(rng: random.Random) -> Dict[str, Any]:
    """Subtract two polynomials: (ax^2 + bx + c) - (dx^2 + ex + f)."""
    a, d = rng.choice([5, 6, 7]), rng.choice([2, 3])
    b, e = rng.choice([3, 4, 7]), rng.choice([-5, -3, 2])
    c, f = rng.choice([-6, 2, 8]), rng.choice([-4, 3, 5])
    tot_a = a - d
    tot_b = b - e
    tot_c = c - f

    sb = f"- {abs(b)}" if b < 0 else f"+ {b}"
    sc = f"- {abs(c)}" if c < 0 else f"+ {c}"
    se = f"- {abs(e)}" if e < 0 else f"+ {e}"
    sf = f"- {abs(f)}" if f < 0 else f"+ {f}"
    poly1 = f"{a}x^2 {sb}x {sc}"
    poly2 = f"{d}x^2 {se}x {sf}"

    stot_b = f"- {abs(tot_b)}" if tot_b < 0 else f"+ {tot_b}"
    stot_c = f"- {abs(tot_c)}" if tot_c < 0 else f"+ {tot_c}"
    ans = f"{tot_a}x^2 {stot_b}x {stot_c}"

    return {
        "subskill": "22_subtract_polynomials_distributing_negative_sign",
        "question_text": (
            f"Subtract the second polynomial from the first:\n$$({poly1}) - ({poly2})$$"
        ),
        "correct_answer": ans,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Distribute negative sign to every term inside the second bracket", "marks": 1},
            {"step": f"Combine like terms to obtain {ans}", "marks": 1},
        ],
        "hints": [
            "Crucial step: Distribute the minus sign through the second bracket, flipping every sign inside.",
            f"Second bracket becomes: $-{d}x^2 {'+' if e < 0 else '-'} {abs(e)}x {'+' if f < 0 else '-'} {abs(f)}$.",
            f"Now combine like terms: ${ans}$.",
        ],
    }


def arch_23_simplify_polynomial_with_descending_powers_standard_form(rng: random.Random) -> Dict[str, Any]:
    """Rearrange and combine jumbled terms into descending standard form."""
    c0 = rng.choice([-9, -4, 5, 8])
    c2 = rng.choice([3, 4, 6])
    c1 = rng.choice([-7, 2, 5])
    c3 = rng.choice([1, 2])
    # Jumbled order: c1 x + c0 + c3 x^3 + c2 x^2
    s0 = f"- {abs(c0)}" if c0 < 0 else f"+ {c0}"
    s2 = f"- {abs(c2)}" if c2 < 0 else f"+ {c2}"
    s3 = f"- {abs(c3)}" if c3 < 0 else f"+ {c3}"
    jumbled = f"{c1}x {s0} {s3}x^3 {s2}x^2"

    s1_ans = f"- {abs(c1)}" if c1 < 0 else f"+ {c1}"
    ans = f"{c3}x^3 + {c2}x^2 {s1_ans}x {s0}"

    return {
        "subskill": "23_simplify_polynomial_with_descending_powers_standard_form",
        "question_text": (
            f"Rewrite the following polynomial in **standard form** (descending powers of $x$):\n$${jumbled}$$"
        ),
        "correct_answer": ans,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Order terms starting from highest power (x^3) to constant: {ans}", "marks": 1},
        ],
        "hints": [
            "Standard form arranges terms in descending order of exponents: $x^3$, then $x^2$, then $x$, then the constant.",
            "Make sure each term keeps its original sign as you rearrange them.",
            f"The standard form is ${ans}$.",
        ],
    }


def arch_24_distributive_law_monomial_times_binomial_positive(rng: random.Random) -> Dict[str, Any]:
    """Expand positive monomial * binomial: a(bx + c)."""
    a = rng.choice([3, 4, 5, 6])
    b = rng.choice([2, 3, 7])
    c = rng.choice([4, 5, 8, 9])
    tot_b = a * b
    tot_c = a * c
    ans = f"{tot_b}x + {tot_c}"

    return {
        "subskill": "24_distributive_law_monomial_times_binomial_positive",
        "question_text": (
            f"Expand and simplify using the distributive property:\n$${a}({b}x + {c})$$"
        ),
        "correct_answer": ans,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Multiply {a} by {b}x = {tot_b}x", "marks": 1},
            {"step": f"Multiply {a} by {c} = {tot_c}", "marks": 1},
        ],
        "hints": [
            "Distribute the number outside the brackets to both terms inside: $a(b + c) = a \\times b + a \\times c$.",
            f"Multiply: ${a} \\times {b}x = {tot_b}x$ and ${a} \\times {c} = {tot_c}$.",
            f"The expanded form is ${ans}$.",
        ],
    }


def arch_25_distributive_law_monomial_times_binomial_negative_monomial(rng: random.Random) -> Dict[str, Any]:
    """Expand negative monomial * binomial with mixed signs: -a(bx - c)."""
    a = rng.choice([2, 3, 4, 5])
    b = rng.choice([3, 4, 5])
    c = rng.choice([4, 6, 7])
    tot_b = -a * b
    tot_c = a * c  # -a * -c = +ac
    ans = f"{tot_b}x + {tot_c}"

    return {
        "subskill": "25_distributive_law_monomial_times_binomial_negative_monomial",
        "question_text": (
            f"Expand and simplify by removing the brackets:\n$$-{a}({b}x - {c})$$"
        ),
        "correct_answer": ans,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Multiply -{a} by {b}x = {tot_b}x", "marks": 1},
            {"step": f"Multiply -{a} by -{c} = +{tot_c}", "marks": 1},
        ],
        "hints": [
            "Watch out for signs: negative times positive is negative; negative times negative is positive.",
            f"Multiply: $-{a} \\times ({b}x) = {tot_b}x$.",
            f"Multiply: $-{a} \\times (-{c}) = +{tot_c}$. Result is ${ans}$.",
        ],
    }
