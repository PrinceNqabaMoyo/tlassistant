"""Grade 12 Technical Mathematics — Polynomials Archetypes 01 to 25.

Grounded strictly in:
curriculum_docs_auto/TechnicalMathematics_Gr12/Term 1/02. Polynomials.md (Chapter 5)

Covers subskills 01 to 25:
- 01-05: Polynomial definitions, classification, degree/order, non-polynomial detection, function evaluation
- 06-07: Polynomial division (monomial, long division, synthetic division)
- 08-11: Remainder Theorem (monic linear, non-monic linear, zero remainder deduction)
- 12-15: Remainder Theorem with unknown coefficients (single unknown, constant term, equal remainders, simultaneous unknowns)
- 16-21: Factor Theorem (verifying linear factors, rational root search, solving unknown coefficients for factors)
- 22-25: Factoring fundamentals (common factor, grouping in pairs, sum/diff of cubes, finding quadratic factor)
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional
import sympy as sp

x = sp.Symbol("x")

TOPIC = "technical_mathematics_polynomials"
LO = "techmath_poly_ch5"


def _fmt_dec(val: float, decimals: int = 2) -> str:
    """Format float using South African comma decimal convention."""
    rounded = round(val, decimals)
    if decimals == 0 or rounded.is_integer():
        return str(int(rounded))
    s = f"{rounded:.{decimals}f}".rstrip("0").rstrip(".")
    return s.replace(".", "{,}")


def _add_pillars(q: Dict[str, Any], subskill: str) -> Dict[str, Any]:
    q.setdefault("topic", TOPIC)
    q.setdefault("subject", "Technical Mathematics")
    q.setdefault("grade", 12)
    q.setdefault("term", 1)
    q.setdefault("caps_weight_percent", 20)
    q.setdefault("suggested_duration_mins", 4)
    q.setdefault("mode", f"elementary_{subskill}")
    q.setdefault("learning_objective_id", LO)

    ans_str = str(q.get("expected_answer") or q.get("correct_answer") or "")
    marks = q.get("marks", 2)
    q.setdefault("marking_schema", [
        {"step": "Method and algebraic working", "marks": max(1, marks // 2)},
        {"step": f"Accurate final answer: {ans_str}", "marks": max(1, marks - marks // 2)},
    ])

    return q


# --------------------------------------------------------------------------- #
# 01_identify_polynomial_definition_and_degree
# --------------------------------------------------------------------------- #
def _build_01_identify_polynomial_definition_and_degree(r: random.Random) -> Dict[str, Any]:
    deg = r.choice([3, 4, 5])
    a = r.choice([2, 3, 5, -2, -4])
    b = r.choice([1, 4, -3, 6])
    c = r.choice([-7, 8, -5, 9])
    const = r.choice([12, -15, 18, -6])

    if deg == 3:
        poly_expr = a*x**3 + b*x**2 + c*x + const
    elif deg == 4:
        poly_expr = a*x**4 + b*x**2 + c*x + const
    else:
        poly_expr = a*x**5 + b*x**3 + c*x + const
    poly_latex = sp.latex(poly_expr)

    prompt = (
        f"Given the polynomial expression: $P(x) = {poly_latex}$.\n\n"
        f"Identify the **Degree (order)** of the polynomial, the **Leading Coefficient**, and the **Constant Term**."
    )
    corr = f"\\text{{Degree}} = {deg}, \\; \\text{{Leading Coefficient}} = {a}, \\; \\text{{Constant}} = {const}"
    opts = [
        f"\\text{{Degree}} = {deg}, \\; \\text{{Leading Coefficient}} = {a}, \\; \\text{{Constant}} = {const}",
        f"\\text{{Degree}} = {deg - 1}, \\; \\text{{Leading Coefficient}} = {b}, \\; \\text{{Constant}} = {const}",
        f"\\text{{Degree}} = {deg}, \\; \\text{{Leading Coefficient}} = {b}, \\; \\text{{Constant}} = {abs(const)}",
        f"\\text{{Degree}} = {deg + 1}, \\; \\text{{Leading Coefficient}} = {a}, \\; \\text{{Constant}} = {c}",
    ]
    r.shuffle(opts)

    return _add_pillars({
        "id": f"tech_poly_01_{r.randint(1000, 9999)}",
        "subskill": "01_identify_polynomial_definition_and_degree",
        "question_type": "mcq",
        "title": "Degree, Leading Coefficient, and Constant Term",
        "prompt": prompt,
        "question": prompt,
        "options": [f"${o}$" for o in opts],
        "correct_answer": f"${corr}$",
        "expected_answer": f"${corr}$",
        "sample_answer": f"${corr}$",
        "worked_solution": (
            f"\\text{{The highest exponent of }} x \\text{{ is }} {deg} \\implies \\text{{Degree}} = {deg}.\\\\\n"
            f"\\text{{The coefficient multiplying }} x^{deg} \\text{{ is }} {a} \\implies \\text{{Leading Coefficient}} = {a}.\\\\\n"
            f"\\text{{The term independent of }} x \\text{{ is }} {const} \\implies \\text{{Constant Term}} = {const}."
        ),
        "explanation": f"The degree is the highest exponent (${deg}$), leading coefficient is the coefficient of that term (${a}$), and constant term is ${const}$.",
        "marks": 2,
        "hints": {
            "tier_1": "The degree is the highest power of $x$ in the expression.",
            "tier_2": f"The highest power is ${deg}$, with coefficient ${a}$.",
            "tier_3": f"Degree $= {deg}$, Leading Coeff $= {a}$, Constant $= {const}$.",
        },
        "misconception_tags": ["confuses_degree_with_number_of_terms"],
    }, "01_identify_polynomial_definition_and_degree")


# --------------------------------------------------------------------------- #
# 02_identify_non_polynomial_negative_or_fractional_exponent
# --------------------------------------------------------------------------- #
def _build_02_identify_non_polynomial_negative_or_fractional_exponent(r: random.Random) -> Dict[str, Any]:
    non_poly_types = [
        ("fractional exponent", "3x^2 + 5\\sqrt{x} - 7", "it contains a fractional exponent (\\sqrt{x} = x^{1/2})"),
        ("negative exponent", "4x^3 - 2x^{-1} + 9", "it contains a negative exponent (x^{-1})"),
        ("variable in denominator", "x^2 + \\frac{6}{x} - 4", "the variable x is in the denominator (equivalent to 6x^{-1})"),
        ("variable under root", "2x^3 - 3\\sqrt[3]{x} + 1", "it has a fractional power (x^{1/3})"),
    ]
    name, expr_latex, reason = r.choice(non_poly_types)
    prompt = (
        f"Consider the algebraic expression: $E(x) = {expr_latex}$.\n\n"
        f"Explain why this expression is **NOT** classified as a polynomial in technical mathematics."
    )
    corr = f"Not a polynomial because {reason}"
    opts = [
        f"Not a polynomial because {reason}",
        "It is a polynomial of degree 3",
        "Not a polynomial because the coefficients are integers",
        "Not a polynomial because it has three terms",
    ]
    r.shuffle(opts)

    return _add_pillars({
        "id": f"tech_poly_02_{r.randint(1000, 9999)}",
        "subskill": "02_identify_non_polynomial_negative_or_fractional_exponent",
        "question_type": "mcq",
        "title": "Identifying Non-Polynomial Expressions",
        "prompt": prompt,
        "question": prompt,
        "options": [f"${o}$" for o in opts],
        "correct_answer": f"${corr}$",
        "expected_answer": f"${corr}$",
        "sample_answer": f"${corr}$",
        "worked_solution": (
            f"\\text{{A polynomial must only have non-negative integer exponents: }} n \\in \\mathbb{{N}}_0 = \\{{0, 1, 2, \\dots\\}}.\\\\\n"
            f"\\text{{In }} {expr_latex}, {reason}, \\text{{ therefore it is not a polynomial.}}"
        ),
        "explanation": f"In a polynomial, all variable exponents must be non-negative integers $\\mathbb{{N}}_0$. Because {reason}, it is not a polynomial.",
        "marks": 2,
        "hints": {
            "tier_1": "Check the powers of $x$. Are all exponents whole numbers $0, 1, 2, \\dots$?",
            "tier_2": f"Notice the term with {name}.",
            "tier_3": f"Correct conclusion: Not a polynomial because {reason}.",
        },
        "misconception_tags": ["believes_negative_exponents_are_allowed_in_polynomials"],
    }, "02_identify_non_polynomial_negative_or_fractional_exponent")


# --------------------------------------------------------------------------- #
# 03_classify_polynomial_monomial_binomial_trinomial
# --------------------------------------------------------------------------- #
def _build_03_classify_polynomial_monomial_binomial_trinomial(r: random.Random) -> Dict[str, Any]:
    choices = [
        ("Monomial", "7x^3", 1, 3),
        ("Binomial", "4x^3 - 9", 2, 3),
        ("Trinomial", "2x^3 - 5x + 8", 3, 3),
        ("Polynomial (4 terms)", "x^3 - 3x^2 + 4x - 12", 4, 3),
    ]
    classification, expr_latex, terms, deg = r.choice(choices)

    prompt = (
        f"Classify the expression $P(x) = {expr_latex}$ by its number of terms and state its degree."
    )
    corr = f"{classification} of degree {deg}"
    opts = [
        f"{classification} of degree {deg}",
        f"Binomial of degree {deg - 1}",
        f"Trinomial of degree {deg + 1}",
        f"Monomial of degree 1",
    ]
    r.shuffle(opts)

    return _add_pillars({
        "id": f"tech_poly_03_{r.randint(1000, 9999)}",
        "subskill": "03_classify_polynomial_monomial_binomial_trinomial",
        "question_type": "mcq",
        "title": "Classification by Number of Terms",
        "prompt": prompt,
        "question": prompt,
        "options": [f"${o}$" for o in opts],
        "correct_answer": f"${corr}$",
        "expected_answer": f"${corr}$",
        "sample_answer": f"${corr}$",
        "worked_solution": f"\\text{{The expression has }} {terms} \\text{{ term(s) and highest exponent }} {deg} \\implies {classification} \\text{{ of degree }} {deg}.",
        "explanation": f"With {terms} term(s) and highest exponent {deg}, it is a {classification} of degree {deg}.",
        "marks": 2,
        "hints": {
            "tier_1": "Count the number of non-zero terms separated by + or - signs.",
            "tier_2": f"There are {terms} terms and highest power is {deg}.",
            "tier_3": f"{classification} of degree {deg}.",
        },
        "misconception_tags": ["confuses_number_of_terms_with_degree"],
    }, "03_classify_polynomial_monomial_binomial_trinomial")


# --------------------------------------------------------------------------- #
# 04_polynomial_evaluation_function_notation
# --------------------------------------------------------------------------- #
def _build_04_polynomial_evaluation_function_notation(r: random.Random) -> Dict[str, Any]:
    a = r.choice([1, 2, -1])
    b = r.choice([2, -3, 4, -2])
    c = r.choice([-4, 5, -6, 3])
    d = r.choice([6, -8, 10, -5])
    poly = a*x**3 + b*x**2 + c*x + d

    k = r.choice([-2, -1, 1, 2, 3])
    val = int(poly.subs(x, k))
    poly_latex = sp.latex(poly)

    prompt = f"Given $f(x) = {poly_latex}$, calculate the value of $f({k})$."
    corr = f"f({k}) = {val}"
    opts = [
        f"f({k}) = {val}",
        f"f({k}) = {val + r.choice([2, 4, -3])}",
        f"f({k}) = {-val}",
        f"f({k}) = {val - r.choice([1, 5, -2])}",
    ]
    r.shuffle(opts)

    return _add_pillars({
        "id": f"tech_poly_04_{r.randint(1000, 9999)}",
        "subskill": "04_polynomial_evaluation_function_notation",
        "question_type": "mcq",
        "title": "Polynomial Functional Evaluation",
        "prompt": prompt,
        "question": prompt,
        "options": [f"${o}$" for o in opts],
        "correct_answer": f"${corr}$",
        "expected_answer": f"${corr}$",
        "sample_answer": f"${corr}$",
        "worked_solution": (
            f"f({k}) = {a}({k})^3 + ({b})({k})^2 + ({c})({k}) + ({d})\\\\\n"
            f"= {a * k**3} + {b * k**2} + {c * k} + {d} = {val}."
        ),
        "explanation": f"Substitute $x = {k}$ into the polynomial: $f({k}) = {val}$.",
        "marks": 2,
        "hints": {
            "tier_1": "Replace every occurrence of $x$ with the number inside the brackets.",
            "tier_2": f"Calculate powers of ${k}$ first: $({k})^3 = {k**3}$, $({k})^2 = {k**2}$.",
            "tier_3": f"Result: $f({k}) = {val}$.",
        },
        "misconception_tags": ["sign_error_negative_base_cubed"],
    }, "04_polynomial_evaluation_function_notation")


# --------------------------------------------------------------------------- #
# 05_polynomial_division_monomial_divisor
# --------------------------------------------------------------------------- #
def _build_05_polynomial_division_monomial_divisor(r: random.Random) -> Dict[str, Any]:
    c = r.choice([2, 3, 4])
    a = c * r.choice([2, 3, 5])
    b = c * r.choice([1, -2, 4])
    d = c * r.choice([-3, 5, -1])

    # (a*x^4 + b*x^3 + d*x^2) / (c*x^2)
    q1 = a // c
    q2 = b // c
    q3 = d // c
    quot_expr = q1*x**2 + q2*x + q3
    quot_latex = sp.latex(quot_expr)

    num_latex = sp.latex(a*x**4 + b*x**3 + d*x**2)
    den_latex = sp.latex(c*x**2)

    prompt = f"Simplify the algebraic division by dividing each term by the monomial divisor:\n\n$$\\frac{{{num_latex}}}{{{den_latex}}}$$"
    corr = f"{quot_latex}"
    opts = [
        f"{quot_latex}",
        f"{sp.latex(q1*x**3 + q2*x + q3)}",
        f"{sp.latex(a*x**2 + b*x + d)}",
        f"{sp.latex(q1*x**2 + b*x + q3)}",
    ]
    r.shuffle(opts)

    return _add_pillars({
        "id": f"tech_poly_05_{r.randint(1000, 9999)}",
        "subskill": "05_polynomial_division_monomial_divisor",
        "question_type": "mcq",
        "title": "Division of a Polynomial by a Monomial",
        "prompt": prompt,
        "question": prompt,
        "options": [f"${o}$" for o in opts],
        "correct_answer": f"${corr}$",
        "expected_answer": f"${corr}$",
        "sample_answer": f"${corr}$",
        "worked_solution": (
            f"\\frac{{{num_latex}}}{{{den_latex}}} = \\frac{{{a}x^4}}{{{c}x^2}} + \\frac{{{b}x^3}}{{{c}x^2}} + \\frac{{{d}x^2}}{{{c}x^2}}\\\\\n"
            f"= {q1}x^2 + ({q2})x + ({q3}) = {quot_latex}."
        ),
        "explanation": f"Divide each term separately: $\\frac{{{a}x^4}}{{{c}x^2}} + \\frac{{{b}x^3}}{{{c}x^2}} + \\frac{{{d}x^2}}{{{c}x^2}} = {quot_latex}$.",
        "marks": 2,
        "hints": {
            "tier_1": "Divide every term in the numerator by the denominator independently.",
            "tier_2": f"Subtract exponents: $x^4 / x^2 = x^2$, $x^3 / x^2 = x$, $x^2 / x^2 = 1$.",
            "tier_3": f"Quotient $= {quot_latex}$.",
        },
        "misconception_tags": ["divides_only_first_term_by_denominator"],
    }, "05_polynomial_division_monomial_divisor")


# --------------------------------------------------------------------------- #
# 06_polynomial_long_division_linear_divisor
# --------------------------------------------------------------------------- #
def _build_06_polynomial_long_division_linear_divisor(r: random.Random) -> Dict[str, Any]:
    c = r.choice([1, 2, 3])
    # dividend = (x - c)*(x^2 + q1*x + q0) + rem
    q1 = r.choice([-3, -2, 1, 2, 4])
    q0 = r.choice([-4, -2, 3, 5])
    rem = r.choice([2, 3, -1, -4, 5])

    quot = x**2 + q1*x + q0
    dividend = sp.expand((x - c) * quot + rem)
    div_latex = sp.latex(dividend)
    quot_latex = sp.latex(quot)

    prompt = (
        f"Perform polynomial division to divide $f(x) = {div_latex}$ by $(x - {c})$.\n\n"
        f"State the **Quotient** $Q(x)$ and the **Remainder** $R$."
    )
    corr = f"Q(x) = {quot_latex}, \\; R = {rem}"
    opts = [
        f"Q(x) = {quot_latex}, \\; R = {rem}",
        f"Q(x) = {quot_latex}, \\; R = {-rem}",
        f"Q(x) = {sp.latex(x**2 - q1*x + q0)}, \\; R = {rem}",
        f"Q(x) = {quot_latex}, \\; R = 0",
    ]
    r.shuffle(opts)

    return _add_pillars({
        "id": f"tech_poly_06_{r.randint(1000, 9999)}",
        "subskill": "06_polynomial_long_division_linear_divisor",
        "question_type": "mcq",
        "title": "Polynomial Long Division by a Linear Divisor",
        "prompt": prompt,
        "question": prompt,
        "options": [f"${o}$" for o in opts],
        "correct_answer": f"${corr}$",
        "expected_answer": f"${corr}$",
        "sample_answer": f"${corr}$",
        "worked_solution": (
            f"\\text{{Using polynomial long division, divide }} {div_latex} \\text{{ by }} (x - {c}):\\\\\n"
            f"\\text{{Quotient }} Q(x) = {quot_latex}\\\\\n"
            f"\\text{{Remainder }} R = {rem}.\\\\\n"
            f"\\text{{Check: }} (x - {c})({quot_latex}) + ({rem}) = {div_latex}."
        ),
        "explanation": f"Long division yields quotient $Q(x) = {quot_latex}$ and remainder $R = {rem}$.",
        "marks": 3,
        "hints": {
            "tier_1": "Divide the leading term of the dividend by $x$, multiply back, and subtract.",
            "tier_2": f"First term of quotient is $x^2$. Continue dividing to get $Q(x) = {quot_latex}$.",
            "tier_3": f"Final remainder is $R = {rem}$.",
        },
        "misconception_tags": ["sign_error_during_polynomial_subtraction"],
    }, "06_polynomial_long_division_linear_divisor")


# --------------------------------------------------------------------------- #
# 07_polynomial_synthetic_division_monic_divisor
# --------------------------------------------------------------------------- #
def _build_07_polynomial_synthetic_division_monic_divisor(r: random.Random) -> Dict[str, Any]:
    c = r.choice([-3, -2, 2, 3])
    # f(x) = (x - c)*(x^2 + p*x + q) + r
    p = r.choice([-4, -1, 2, 3])
    q_val = r.choice([-5, -2, 3, 6])
    rem = r.choice([-3, 1, 4, 7])

    quot = x**2 + p*x + q_val
    dividend = sp.expand((x - c) * quot + rem)
    div_latex = sp.latex(dividend)
    quot_latex = sp.latex(quot)

    div_sign = "-" if c > 0 else "+"
    div_str = f"x {div_sign} {abs(c)}"

    prompt = (
        f"Using **Synthetic Division**, divide the cubic polynomial $f(x) = {div_latex}$ by $({div_str})$.\n\n"
        f"Determine the resulting quadratic quotient $Q(x)$ and remainder $R$."
    )
    corr = f"Q(x) = {quot_latex}, \\; R = {rem}"
    opts = [
        f"Q(x) = {quot_latex}, \\; R = {rem}",
        f"Q(x) = {quot_latex}, \\; R = {-rem}",
        f"Q(x) = {sp.latex(x**2 - p*x + q_val)}, \\; R = {rem}",
        f"Q(x) = {sp.latex(2*x**2 + p*x + q_val)}, \\; R = {rem}",
    ]
    r.shuffle(opts)

    return _add_pillars({
        "id": f"tech_poly_07_{r.randint(1000, 9999)}",
        "subskill": "07_polynomial_synthetic_division_monic_divisor",
        "question_type": "mcq",
        "title": "Synthetic Division for Cubic Polynomials",
        "prompt": prompt,
        "question": prompt,
        "options": [f"${o}$" for o in opts],
        "correct_answer": f"${corr}$",
        "expected_answer": f"${corr}$",
        "sample_answer": f"${corr}$",
        "worked_solution": (
            f"\\text{{Divisor root: }} {div_str} = 0 \\implies x = {c}.\\\\\n"
            f"\\text{{Synthetic division row with multiplier }} {c} \\text{{ gives coefficients }}: [1, \\; {p}, \\; {q_val}] \\text{{ with remainder }} {rem}.\\\\\n"
            f"Q(x) = {quot_latex}, \\; R = {rem}."
        ),
        "explanation": f"Synthetic division by $x = {c}$ produces quotient $Q(x) = {quot_latex}$ and remainder $R = {rem}$.",
        "marks": 3,
        "hints": {
            "tier_1": f"The root of the divisor is $x = {c}$. Use {c} as your synthetic division multiplier.",
            "tier_2": "Bring down the leading coefficient 1, multiply by the root, add to next coefficient.",
            "tier_3": f"Quotient is ${quot_latex}$ with remainder ${rem}$.",
        },
        "misconception_tags": ["inverts_root_sign_in_synthetic_division"],
    }, "07_polynomial_synthetic_division_monic_divisor")


# --------------------------------------------------------------------------- #
# 08_remainder_theorem_linear_monic_positive_root
# --------------------------------------------------------------------------- #
def _build_08_remainder_theorem_linear_monic_positive_root(r: random.Random) -> Dict[str, Any]:
    c = r.choice([1, 2, 3, 4])
    a = r.choice([1, 2, 3])
    b = r.choice([-5, -3, 2, 4])
    k_const = r.choice([-8, -4, 6, 12])
    d = r.choice([-15, -6, 7, 10])

    poly = a*x**3 + b*x**2 + k_const*x + d
    rem = int(poly.subs(x, c))
    poly_latex = sp.latex(poly)

    prompt = (
        f"Use the **Remainder Theorem** to determine the remainder when "
        f"$f(x) = {poly_latex}$ is divided by $(x - {c})$."
    )
    corr = f"R = {rem}"
    wrong_sub = int(poly.subs(x, -c))
    opts = [
        f"R = {rem}",
        f"R = {wrong_sub}",
        f"R = {rem + 4}",
        f"R = 0",
    ]
    r.shuffle(opts)

    return _add_pillars({
        "id": f"tech_poly_08_{r.randint(1000, 9999)}",
        "subskill": "08_remainder_theorem_linear_monic_positive_root",
        "question_type": "mcq",
        "title": "Remainder Theorem (x - c)",
        "prompt": prompt,
        "question": prompt,
        "options": [f"${o}$" for o in opts],
        "correct_answer": f"${corr}$",
        "expected_answer": f"${corr}$",
        "sample_answer": f"${corr}$",
        "worked_solution": (
            f"\\text{{Divisor }} x - {c} = 0 \\implies x = {c}.\\\\\n"
            f"R = f({c}) = {a}({c})^3 + ({b})({c})^2 + ({k_const})({c}) + ({d})\\\\\n"
            f"= {a*c**3} + {b*c**2} + {k_const*c} + {d} = {rem}."
        ),
        "explanation": f"According to the Remainder Theorem, $R = f({c}) = {rem}$.",
        "marks": 2,
        "hints": {
            "tier_1": "Set the divisor to zero: $x - c = 0 \\implies x = c$. Then evaluate $f(c)$.",
            "tier_2": f"Substitute $x = {c}$ into $f(x)$.",
            "tier_3": f"$R = f({c}) = {rem}$.",
        },
        "misconception_tags": ["substitutes_negative_instead_of_positive_root"],
    }, "08_remainder_theorem_linear_monic_positive_root")


# --------------------------------------------------------------------------- #
# 09_remainder_theorem_linear_monic_negative_root
# --------------------------------------------------------------------------- #
def _build_09_remainder_theorem_linear_monic_negative_root(r: random.Random) -> Dict[str, Any]:
    c = r.choice([1, 2, 3])
    a = r.choice([1, 2])
    b = r.choice([-3, 1, 4])
    k_const = r.choice([-6, 2, 5])
    d = r.choice([-10, 8, -4])

    poly = a*x**3 + b*x**2 + k_const*x + d
    rem = int(poly.subs(x, -c))
    poly_latex = sp.latex(poly)

    prompt = (
        f"Use the **Remainder Theorem** to find the remainder when "
        f"$f(x) = {poly_latex}$ is divided by $(x + {c})$."
    )
    corr = f"R = {rem}"
    wrong_sub = int(poly.subs(x, c))
    opts = [
        f"R = {rem}",
        f"R = {wrong_sub}",
        f"R = {rem - 3}",
        f"R = 0",
    ]
    r.shuffle(opts)

    return _add_pillars({
        "id": f"tech_poly_09_{r.randint(1000, 9999)}",
        "subskill": "09_remainder_theorem_linear_monic_negative_root",
        "question_type": "mcq",
        "title": "Remainder Theorem (x + c)",
        "prompt": prompt,
        "question": prompt,
        "options": [f"${o}$" for o in opts],
        "correct_answer": f"${corr}$",
        "expected_answer": f"${corr}$",
        "sample_answer": f"${corr}$",
        "worked_solution": (
            f"\\text{{Divisor }} x + {c} = 0 \\implies x = -{c}.\\\\\n"
            f"R = f(-{c}) = {a}(-{c})^3 + ({b})(-{c})^2 + ({k_const})(-{c}) + ({d})\\\\\n"
            f"= {a*(-c)**3} + {b*(-c)**2} + {k_const*(-c)} + {d} = {rem}."
        ),
        "explanation": f"Set $x + {c} = 0 \\implies x = -{c}$. Therefore $R = f(-{c}) = {rem}$.",
        "marks": 2,
        "hints": {
            "tier_1": "Set the divisor to zero: $x + c = 0 \\implies x = -c$.",
            "tier_2": f"Substitute $x = -{c}$ into $f(x)$.",
            "tier_3": f"Evaluate carefully: $R = f(-{c}) = {rem}$.",
        },
        "misconception_tags": ["sign_error_divisor_substitution"],
    }, "09_remainder_theorem_linear_monic_negative_root")


# --------------------------------------------------------------------------- #
# 10_remainder_theorem_linear_non_monic_fraction_root
# --------------------------------------------------------------------------- #
def _build_10_remainder_theorem_linear_non_monic_fraction_root(r: random.Random) -> Dict[str, Any]:
    # Divisor (2x - 1) or (2x + 1) or (3x - 1)
    a_div, b_div = r.choice([(2, 1), (2, -1), (3, 1)])
    root = sp.Rational(b_div, a_div)

    # Let poly = 2*a_div * x^3 + ...
    p3 = a_div**2 * r.choice([1, 2])
    p2 = a_div * r.choice([-3, 4, 2])
    p1 = r.choice([-5, 6, -2])
    p0 = r.choice([4, -6, 8])

    poly = p3*x**3 + p2*x**2 + p1*x + p0
    rem = poly.subs(x, root)
    poly_latex = sp.latex(poly)

    sign_str = "-" if b_div > 0 else "+"
    div_str = f"{a_div}x {sign_str} {abs(b_div)}"

    prompt = (
        f"Apply the Remainder Theorem to calculate the remainder when "
        f"$f(x) = {poly_latex}$ is divided by the linear binomial $({div_str})$."
    )
    rem_latex = sp.latex(rem)
    corr = f"R = {rem_latex}"
    opts = [
        f"R = {rem_latex}",
        f"R = {sp.latex(rem + 2)}",
        f"R = {sp.latex(-rem)}",
        f"R = 0",
    ]
    r.shuffle(opts)

    return _add_pillars({
        "id": f"tech_poly_10_{r.randint(1000, 9999)}",
        "subskill": "10_remainder_theorem_linear_non_monic_fraction_root",
        "question_type": "mcq",
        "title": "Remainder Theorem with Non-Monic Linear Divisor (ax - b)",
        "prompt": prompt,
        "question": prompt,
        "options": [f"${o}$" for o in opts],
        "correct_answer": f"${corr}$",
        "expected_answer": f"${corr}$",
        "sample_answer": f"${corr}$",
        "worked_solution": (
            f"\\text{{Divisor }} {div_str} = 0 \\implies x = {sp.latex(root)}.\\\\\n"
            f"R = f\\left({sp.latex(root)}\\right) = {p3}\\left({sp.latex(root)}\\right)^3 + {p2}\\left({sp.latex(root)}\\right)^2 + {p1}\\left({sp.latex(root)}\\right) + {p0}\\\\\n"
            f"= {rem_latex}."
        ),
        "explanation": f"Set ${div_str} = 0 \\implies x = {sp.latex(root)}$. Evaluate $f({sp.latex(root)}) = {rem_latex}$.",
        "marks": 3,
        "hints": {
            "tier_1": f"Solve for $x$: ${div_str} = 0 \\implies x = {sp.latex(root)}$.",
            "tier_2": f"Substitute $x = {sp.latex(root)}$ into $f(x)$.",
            "tier_3": f"Calculate the fraction arithmetic to find $R = {rem_latex}$.",
        },
        "misconception_tags": ["fraction_arithmetic_error_in_polynomial_substitution"],
    }, "10_remainder_theorem_linear_non_monic_fraction_root")


# --------------------------------------------------------------------------- #
# 11_remainder_theorem_zero_remainder_deduction
# --------------------------------------------------------------------------- #
def _build_11_remainder_theorem_zero_remainder_deduction(r: random.Random) -> Dict[str, Any]:
    c = r.choice([-2, -1, 1, 2, 3])
    # Build polynomial where f(c) = 0 exactly
    q_fac = x**2 + r.choice([-3, 2, 4])*x + r.choice([-4, 5, -6])
    poly = sp.expand((x - c) * q_fac)
    poly_latex = sp.latex(poly)

    div_sign = "-" if c > 0 else "+"
    div_str = f"x {div_sign} {abs(c)}"

    prompt = (
        f"Evaluate the remainder when $f(x) = {poly_latex}$ is divided by $({div_str})$. "
        f"What geometric/algebraic deduction can you make about $({div_str})$ and $f(x)$?"
    )
    corr = f"R = 0, \\text{{ therefore }} ({div_str}) \\text{{ is an exact factor of }} f(x)"
    opts = [
        f"R = 0, \\text{{ therefore }} ({div_str}) \\text{{ is an exact factor of }} f(x)",
        f"R = 0, \\text{{ therefore }} ({div_str}) \\text{{ is NOT a factor of }} f(x)",
        f"R = {c}, \\text{{ therefore }} ({div_str}) \\text{{ is a factor}}",
        f"R = 1, \\text{{ therefore }} f(x) \\text{{ has no real roots}}",
    ]
    r.shuffle(opts)

    return _add_pillars({
        "id": f"tech_poly_11_{r.randint(1000, 9999)}",
        "subskill": "11_remainder_theorem_zero_remainder_deduction",
        "question_type": "mcq",
        "title": "Zero Remainder Deduction and Divisibility",
        "prompt": prompt,
        "question": prompt,
        "options": [f"${o}$" for o in opts],
        "correct_answer": f"${corr}$",
        "expected_answer": f"${corr}$",
        "sample_answer": f"${corr}$",
        "worked_solution": (
            f"f({c}) = 0 \\implies \\text{{Remainder }} R = 0.\\\\\n"
            f"\\text{{By the Factor Theorem, because the remainder is 0, }} ({div_str}) \\text{{ is an exact factor of }} f(x)."
        ),
        "explanation": f"Since $f({c}) = 0$, the remainder is $0$, meaning $({div_str})$ divides $f(x)$ without remainder (it is a factor).",
        "marks": 2,
        "hints": {
            "tier_1": "Calculate the remainder by evaluating $f(c)$.",
            "tier_2": f"$f({c}) = 0$.",
            "tier_3": "A remainder of 0 means the divisor is an exact factor.",
        },
        "misconception_tags": ["confuses_remainder_zero_with_undefined_division"],
    }, "11_remainder_theorem_zero_remainder_deduction")


# --------------------------------------------------------------------------- #
# 12_remainder_theorem_solve_unknown_coefficient_k
# --------------------------------------------------------------------------- #
def _build_12_remainder_theorem_solve_unknown_coefficient_k(r: random.Random) -> Dict[str, Any]:
    k_val = r.choice([-5, -4, -3, 2, 3, 4, 5])
    c = r.choice([1, 2, -1, -2])
    a = r.choice([1, 2])
    const = r.choice([-6, 8, -12, 10])

    # f(x) = a*x^3 + k*x^2 - 3*x + const
    # R = f(c)
    lin_coef = r.choice([-4, -2, 3, 5])
    poly_subs = a*c**3 + k_val*c**2 + lin_coef*c + const
    rem = poly_subs

    # In prompt: replace k_val with symbol k
    lin_str = f"+ {lin_coef}x" if lin_coef > 0 else f"- {abs(lin_coef)}x"
    const_str = f"+ {const}" if const > 0 else f"- {abs(const)}"
    poly_display = f"{a}x^3 + kx^2 {lin_str} {const_str}"

    div_sign = "-" if c > 0 else "+"
    div_str = f"x {div_sign} {abs(c)}"

    prompt = (
        f"When the polynomial $f(x) = {poly_display}$ is divided by $({div_str})$, "
        f"the remainder is ${rem}$. Determine the value of the unknown coefficient $k$."
    )
    corr = f"k = {k_val}"
    opts = [
        f"k = {k_val}",
        f"k = {k_val + 2}",
        f"k = {-k_val}",
        f"k = {k_val - 3}",
    ]
    r.shuffle(opts)

    return _add_pillars({
        "id": f"tech_poly_12_{r.randint(1000, 9999)}",
        "subskill": "12_remainder_theorem_solve_unknown_coefficient_k",
        "question_type": "mcq",
        "title": "Solve Unknown Coefficient k via Remainder Theorem",
        "prompt": prompt,
        "question": prompt,
        "options": [f"${o}$" for o in opts],
        "correct_answer": f"${corr}$",
        "expected_answer": f"${corr}$",
        "sample_answer": f"${corr}$",
        "worked_solution": (
            f"\\text{{By the Remainder Theorem, }} f({c}) = {rem}:\\\\\n"
            f"{a}({c})^3 + k({c})^2 + ({lin_coef})({c}) + ({const}) = {rem}\\\\\n"
            f"{a*c**3 + lin_coef*c + const} + {c**2}k = {rem}\\\\\n"
            f"{c**2}k = {rem - (a*c**3 + lin_coef*c + const)} \\implies k = {k_val}."
        ),
        "explanation": f"Set $f({c}) = {rem}$ and solve the linear equation in $k$: $k = {k_val}$.",
        "marks": 3,
        "hints": {
            "tier_1": f"Apply the Remainder Theorem: $f({c}) = {rem}$.",
            "tier_2": f"Substitute $x = {c}$ into the polynomial and set it equal to ${rem}$.",
            "tier_3": f"Solve for $k$: $k = {k_val}$.",
        },
        "misconception_tags": ["algebraic_isolation_error_for_unknown_coefficient"],
    }, "12_remainder_theorem_solve_unknown_coefficient_k")


# --------------------------------------------------------------------------- #
# 13_remainder_theorem_solve_unknown_constant_term
# --------------------------------------------------------------------------- #
def _build_13_remainder_theorem_solve_unknown_constant_term(r: random.Random) -> Dict[str, Any]:
    d_val = r.choice([-12, -8, -5, 6, 9, 14])
    c = r.choice([1, 2, -1, 3])
    a = r.choice([1, 2])
    b = r.choice([-3, 2, 4])
    k_lin = r.choice([-5, -2, 3])

    poly_subs = a*c**3 + b*c**2 + k_lin*c + d_val
    rem = poly_subs

    lin_str = f"+ {k_lin}x" if k_lin > 0 else f"- {abs(k_lin)}x"
    b_str = f"+ {b}x^2" if b > 0 else f"- {abs(b)}x^2"
    poly_display = f"{a}x^3 {b_str} {lin_str} + d"

    div_sign = "-" if c > 0 else "+"
    div_str = f"x {div_sign} {abs(c)}"

    prompt = (
        f"The polynomial $P(x) = {poly_display}$ leaves a remainder of ${rem}$ when divided by $({div_str})$. "
        f"Calculate the value of the constant term $d$."
    )
    corr = f"d = {d_val}"
    opts = [
        f"d = {d_val}",
        f"d = {d_val + 4}",
        f"d = {-d_val}",
        f"d = {d_val - 2}",
    ]
    r.shuffle(opts)

    return _add_pillars({
        "id": f"tech_poly_13_{r.randint(1000, 9999)}",
        "subskill": "13_remainder_theorem_solve_unknown_constant_term",
        "question_type": "mcq",
        "title": "Solve Unknown Constant Term d via Remainder Theorem",
        "prompt": prompt,
        "question": prompt,
        "options": [f"${o}$" for o in opts],
        "correct_answer": f"${corr}$",
        "expected_answer": f"${corr}$",
        "sample_answer": f"${corr}$",
        "worked_solution": (
            f"P({c}) = {rem} \\implies {a}({c})^3 + ({b})({c})^2 + ({k_lin})({c}) + d = {rem}\\\\\n"
            f"{a*c**3 + b*c**2 + k_lin*c} + d = {rem} \\implies d = {d_val}."
        ),
        "explanation": f"Set $P({c}) = {rem}$ and isolate $d$: $d = {d_val}$.",
        "marks": 2,
        "hints": {
            "tier_1": f"By the Remainder Theorem, $P({c}) = {rem}$.",
            "tier_2": f"Calculate the numerical sum of the non-constant terms: ${a*c**3 + b*c**2 + k_lin*c}$.",
            "tier_3": f"Subtract from ${rem}$ to find $d = {d_val}$.",
        },
        "misconception_tags": ["arithmetic_subtraction_error_for_constant"],
    }, "13_remainder_theorem_solve_unknown_constant_term")


# --------------------------------------------------------------------------- #
# 14_remainder_theorem_equal_remainders_two_divisors
# --------------------------------------------------------------------------- #
def _build_14_remainder_theorem_equal_remainders_two_divisors(r: random.Random) -> Dict[str, Any]:
    # f(x) = x^3 + p*x^2 + q*x + d
    # Given f(c1) = f(c2)
    c1 = 1
    c2 = -2
    # f(1) = 1 + p - 2 + d
    # f(-2) = -8 + 4p + 4 + d
    # f(1) = f(-2) => 1 + p - 2 = -8 + 4p + 4 => p - 1 = 4p - 4 => 3p = 3 => p = 1
    p_val = r.choice([-3, -2, 1, 2, 3])
    # Let's adjust lin_coef so p is an integer:
    # (c1^3 - c2^3) + lin_coef*(c1 - c2) + p*(c1^2 - c2^2) = 0
    # (1 - (-8)) + lin*(1 - (-2)) + p*(1 - 4) = 0 => 9 + 3*lin - 3p = 0 => 3 + lin - p = 0 => lin = p - 3
    lin_coef = p_val - 3
    const = r.choice([4, -6, 7])

    lin_str = f"+ {lin_coef}x" if lin_coef > 0 else f"- {abs(lin_coef)}x"
    const_str = f"+ {const}" if const > 0 else f"- {abs(const)}"
    poly_display = f"x^3 + px^2 {lin_str} {const_str}"

    prompt = (
        f"The polynomial $f(x) = {poly_display}$ leaves the **SAME remainder** when divided by $(x - 1)$ "
        f"as it does when divided by $(x + 2)$. Calculate the value of the parameter $p$."
    )
    corr = f"p = {p_val}"
    opts = [
        f"p = {p_val}",
        f"p = {p_val + 1}",
        f"p = {-p_val}",
        f"p = {p_val - 2}",
    ]
    r.shuffle(opts)

    return _add_pillars({
        "id": f"tech_poly_14_{r.randint(1000, 9999)}",
        "subskill": "14_remainder_theorem_equal_remainders_two_divisors",
        "question_type": "mcq",
        "title": "Equal Remainders with Two Linear Divisors",
        "prompt": prompt,
        "question": prompt,
        "options": [f"${o}$" for o in opts],
        "correct_answer": f"${corr}$",
        "expected_answer": f"${corr}$",
        "sample_answer": f"${corr}$",
        "worked_solution": (
            f"\\text{{Equal remainders }} \\implies f(1) = f(-2).\\\\\n"
            f"(1)^3 + p(1)^2 + ({lin_coef})(1) + ({const}) = (-2)^3 + p(-2)^2 + ({lin_coef})(-2) + ({const})\\\\\n"
            f"1 + p + {lin_coef} = -8 + 4p - 2({lin_coef})\\\\\n"
            f"p + {1 + lin_coef} = 4p + {-8 - 2*lin_coef} \\implies 3p = {1 + lin_coef - (-8 - 2*lin_coef)} \\implies p = {p_val}."
        ),
        "explanation": f"Equate $f(1) = f(-2)$ and solve the resulting linear equation for $p$: $p = {p_val}$.",
        "marks": 3,
        "hints": {
            "tier_1": "Set the two remainder expressions equal to each other: $f(1) = f(-2)$.",
            "tier_2": "Expand both sides and collect terms in $p$ on one side.",
            "tier_3": f"Solve: $3p = {3 * p_val} \\implies p = {p_val}$.",
        },
        "misconception_tags": ["forgets_to_equate_remainder_expressions"],
    }, "14_remainder_theorem_equal_remainders_two_divisors")


# --------------------------------------------------------------------------- #
# 15_remainder_theorem_simultaneous_two_unknown_coefficients
# --------------------------------------------------------------------------- #
def _build_15_remainder_theorem_simultaneous_two_unknown_coefficients(r: random.Random) -> Dict[str, Any]:
    # f(x) = x^3 + a*x^2 + b*x + 6
    a_val = r.choice([-3, -2, 1, 2, 3])
    b_val = r.choice([-4, -1, 3, 4])
    const = r.choice([2, -6, 8])

    # f(1) = R1
    # f(-1) = R2
    # f(1) = 1 + a + b + const => a + b = R1 - 1 - const
    # f(-1) = -1 + a - b + const => a - b = R2 + 1 - const
    r1 = 1 + a_val + b_val + const
    r2 = -1 + a_val - b_val + const

    const_str = f"+ {const}" if const > 0 else f"- {abs(const)}"
    poly_display = f"f(x) = x^3 + ax^2 + bx {const_str}"

    prompt = (
        f"When $f(x) = {poly_display}$ is divided by $(x - 1)$, the remainder is ${r1}$. "
        f"When it is divided by $(x + 1)$, the remainder is ${r2}$. "
        f"Solve simultaneously for the values of coefficients $a$ and $b$."
    )
    corr = f"a = {a_val}, \\; b = {b_val}"
    opts = [
        f"a = {a_val}, \\; b = {b_val}",
        f"a = {b_val}, \\; b = {a_val}",
        f"a = {a_val + 1}, \\; b = {b_val - 1}",
        f"a = {-a_val}, \\; b = {-b_val}",
    ]
    r.shuffle(opts)

    return _add_pillars({
        "id": f"tech_poly_15_{r.randint(1000, 9999)}",
        "subskill": "15_remainder_theorem_simultaneous_two_unknown_coefficients",
        "question_type": "mcq",
        "title": "Two Unknown Coefficients via Simultaneous Remainder Equations",
        "prompt": prompt,
        "question": prompt,
        "options": [f"${o}$" for o in opts],
        "correct_answer": f"${corr}$",
        "expected_answer": f"${corr}$",
        "sample_answer": f"${corr}$",
        "worked_solution": (
            f"\\text{{(1) }} f(1) = {r1} \\implies 1 + a + b + ({const}) = {r1} \\implies a + b = {a_val + b_val}\\text{{ [Eq 1]}}\\\\\n"
            f"\\text{{(2) }} f(-1) = {r2} \\implies -1 + a - b + ({const}) = {r2} \\implies a - b = {a_val - b_val}\\text{{ [Eq 2]}}\\\\\n"
            f"\\text{{Add [1] and [2]: }} 2a = {2*a_val} \\implies a = {a_val}.\\\\\n"
            f"\\text{{Substitute into [1]: }} {a_val} + b = {a_val + b_val} \\implies b = {b_val}."
        ),
        "explanation": f"Set up the system: $a + b = {a_val + b_val}$ and $a - b = {a_val - b_val}$. Solving simultaneously yields $a = {a_val}, b = {b_val}$.",
        "marks": 4,
        "hints": {
            "tier_1": "Set up two equations using the Remainder Theorem: $f(1) = R_1$ and $f(-1) = R_2$.",
            "tier_2": f"You get the linear system: $a + b = {a_val + b_val}$ and $a - b = {a_val - b_val}$.",
            "tier_3": f"Add the two equations to solve for $a$, then substitute to find $b$: $a = {a_val}, b = {b_val}$.",
        },
        "misconception_tags": ["simultaneous_elimination_sign_error"],
    }, "15_remainder_theorem_simultaneous_two_unknown_coefficients")


# --------------------------------------------------------------------------- #
# 16_factor_theorem_verify_linear_factor_monic
# --------------------------------------------------------------------------- #
def _build_16_factor_theorem_verify_linear_factor_monic(r: random.Random) -> Dict[str, Any]:
    c = r.choice([-3, -2, 2, 3])
    # Build polynomial with factor (x - c)
    q_fac = x**2 + r.choice([-4, 1, 3])*x + r.choice([-6, 2, 5])
    poly = sp.expand((x - c) * q_fac)
    poly_latex = sp.latex(poly)

    div_sign = "-" if c > 0 else "+"
    div_str = f"x {div_sign} {abs(c)}"

    prompt = (
        f"Use the **Factor Theorem** to test whether $({div_str})$ is a factor of the polynomial "
        f"$f(x) = {poly_latex}$."
    )
    corr = f"Yes: f({c}) = 0, \\text{{ so }} ({div_str}) \\text{{ is a factor}}"
    opts = [
        f"Yes: f({c}) = 0, \\text{{ so }} ({div_str}) \\text{{ is a factor}}",
        f"No: f({c}) \\neq 0, \\text{{ so }} ({div_str}) \\text{{ is not a factor}}",
        f"No: f(-{c}) = 0, \\text{{ so }} ({div_str}) \\text{{ is not a factor}}",
        "Cannot be determined without polynomial long division",
    ]
    r.shuffle(opts)

    return _add_pillars({
        "id": f"tech_poly_16_{r.randint(1000, 9999)}",
        "subskill": "16_factor_theorem_verify_linear_factor_monic",
        "question_type": "mcq",
        "title": "Verifying a Linear Factor via Factor Theorem",
        "prompt": prompt,
        "question": prompt,
        "options": [f"${o}$" for o in opts],
        "correct_answer": f"${corr}$",
        "expected_answer": f"${corr}$",
        "sample_answer": f"${corr}$",
        "worked_solution": (
            f"\\text{{Test divisor root: }} {div_str} = 0 \\implies x = {c}.\\\\\n"
            f"f({c}) = 0.\\\\\n"
            f"\\text{{By the Factor Theorem, since }} f({c}) = 0, \\; ({div_str}) \\text{{ is a factor of }} f(x)."
        ),
        "explanation": f"Evaluating $f({c})$ gives $0$. Since $f({c}) = 0$, $({div_str})$ is an exact factor.",
        "marks": 2,
        "hints": {
            "tier_1": f"According to the Factor Theorem, $(x - c)$ is a factor if and only if $f(c) = 0$.",
            "tier_2": f"Substitute $x = {c}$ into $f(x)$.",
            "tier_3": f"Because $f({c}) = 0$, the answer is YES.",
        },
        "misconception_tags": ["confuses_factor_theorem_condition_with_non_zero_remainder"],
    }, "16_factor_theorem_verify_linear_factor_monic")


# --------------------------------------------------------------------------- #
# 17_factor_theorem_verify_linear_factor_non_monic
# --------------------------------------------------------------------------- #
def _build_17_factor_theorem_verify_linear_factor_non_monic(r: random.Random) -> Dict[str, Any]:
    a_div = 2
    b_div = r.choice([-3, -1, 1, 3])
    root = sp.Rational(b_div, a_div)

    # (2x - b)*(x^2 + p*x + q)
    p = r.choice([-2, 1, 3])
    q_val = r.choice([-4, 2, 5])
    poly = sp.expand((a_div*x - b_div) * (x**2 + p*x + q_val))
    poly_latex = sp.latex(poly)

    sign_str = "-" if b_div > 0 else "+"
    div_str = f"2x {sign_str} {abs(b_div)}"

    prompt = (
        f"Apply the **Factor Theorem** to verify whether $({div_str})$ is a factor of "
        f"$P(x) = {poly_latex}$."
    )
    root_latex = sp.latex(root)
    corr = f"Yes: P\\left({root_latex}\\right) = 0, \\text{{ so }} ({div_str}) \\text{{ is a factor}}"
    opts = [
        f"Yes: P\\left({root_latex}\\right) = 0, \\text{{ so }} ({div_str}) \\text{{ is a factor}}",
        f"No: P\\left({root_latex}\\right) \\neq 0",
        f"Yes: P({b_div}) = 0",
        f"No: ({div_str}) \\text{{ is not monic}}",
    ]
    r.shuffle(opts)

    return _add_pillars({
        "id": f"tech_poly_17_{r.randint(1000, 9999)}",
        "subskill": "17_factor_theorem_verify_linear_factor_non_monic",
        "question_type": "mcq",
        "title": "Factor Theorem with Non-Monic Linear Factor",
        "prompt": prompt,
        "question": prompt,
        "options": [f"${o}$" for o in opts],
        "correct_answer": f"${corr}$",
        "expected_answer": f"${corr}$",
        "sample_answer": f"${corr}$",
        "worked_solution": (
            f"\\text{{Divisor root: }} {div_str} = 0 \\implies x = {root_latex}.\\\\\n"
            f"P\\left({root_latex}\\right) = 0.\\\\\n"
            f"\\text{{By the Factor Theorem, }} ({div_str}) \\text{{ is an exact factor of }} P(x)."
        ),
        "explanation": f"Since $P({root_latex}) = 0$, $({div_str})$ is a factor.",
        "marks": 2,
        "hints": {
            "tier_1": f"Find the root of the divisor: ${div_str} = 0 \\implies x = {root_latex}$.",
            "tier_2": f"Evaluate $P({root_latex})$.",
            "tier_3": f"Because $P({root_latex}) = 0$, $({div_str})$ is a factor.",
        },
        "misconception_tags": ["uses_integer_root_instead_of_fraction_for_non_monic_divisor"],
    }, "17_factor_theorem_verify_linear_factor_non_monic")


# --------------------------------------------------------------------------- #
# 18_factor_theorem_find_first_integer_factor_rational_root
# --------------------------------------------------------------------------- #
def _build_18_factor_theorem_find_first_integer_factor_rational_root(r: random.Random) -> Dict[str, Any]:
    root1 = r.choice([-2, -1, 1, 2])
    root2 = r.choice([-3, 3, 4])
    root3 = r.choice([-4, -5, 5])
    poly = sp.expand((x - root1) * (x - root2) * (x - root3))
    poly_latex = sp.latex(poly)

    factor_sign = "-" if root1 > 0 else "+"
    fac_str = f"x {factor_sign} {abs(root1)}"

    prompt = (
        f"By testing factors of the constant term (Rational Root Test), determine the first linear factor "
        f"of the cubic polynomial $f(x) = {poly_latex}$."
    )
    corr = f"({fac_str}) \\text{{ because }} f({root1}) = 0"
    wrong_root = -root1
    wrong_sign = "-" if wrong_root > 0 else "+"
    opts = [
        f"({fac_str}) \\text{{ because }} f({root1}) = 0",
        f"(x {wrong_sign} {abs(wrong_root)}) \\text{{ because }} f({wrong_root}) = 0",
        f"(x - 5) \\text{{ because }} f(5) = 0",
        "(x - 0) \\text{{ because constant is 0}}",
    ]
    r.shuffle(opts)

    return _add_pillars({
        "id": f"tech_poly_18_{r.randint(1000, 9999)}",
        "subskill": "18_factor_theorem_find_first_integer_factor_rational_root",
        "question_type": "mcq",
        "title": "Finding First Linear Factor via Rational Root Test",
        "prompt": prompt,
        "question": prompt,
        "options": [f"${o}$" for o in opts],
        "correct_answer": f"${corr}$",
        "expected_answer": f"${corr}$",
        "sample_answer": f"${corr}$",
        "worked_solution": (
            f"\\text{{Test possible integer factors of constant term }}: x \\in \\{{\\pm 1, \\pm 2, \\dots\\}}.\\\\\n"
            f"f({root1}) = 0 \\implies ({fac_str}) \\text{{ is a factor of }} f(x)."
        ),
        "explanation": f"Testing candidate roots yields $f({root1}) = 0$, establishing that $({fac_str})$ is a factor.",
        "marks": 2,
        "hints": {
            "tier_1": "Test small factors of the constant term: $\\pm 1, \\pm 2, \\dots$",
            "tier_2": f"Calculate $f({root1})$.",
            "tier_3": f"Since $f({root1}) = 0$, $({fac_str})$ is the first factor.",
        },
        "misconception_tags": ["inverts_factor_sign_from_tested_root"],
    }, "18_factor_theorem_find_first_integer_factor_rational_root")


# --------------------------------------------------------------------------- #
# 19_factor_theorem_solve_unknown_coefficient_for_factor
# --------------------------------------------------------------------------- #
def _build_19_factor_theorem_solve_unknown_coefficient_for_factor(r: random.Random) -> Dict[str, Any]:
    c = r.choice([-3, -2, 2, 3])
    k_val = r.choice([-5, -3, 2, 4, 6])
    a = r.choice([1, 2])
    const = r.choice([-12, 18, -6, 24])

    # f(c) = 0 => a*c^3 + k*c^2 + lin*c + const = 0
    # Let's adjust lin so k is an integer
    # lin*c = -(a*c^3 + k_val*c^2 + const)
    # Ensure divisible by c:
    num = -(a*c**3 + k_val*c**2 + const)
    lin_coef = num // c
    # Recheck
    actual_const = -(a*c**3 + k_val*c**2 + lin_coef*c)

    lin_str = f"+ {lin_coef}x" if lin_coef > 0 else f"- {abs(lin_coef)}x"
    const_str = f"+ {actual_const}" if actual_const > 0 else f"- {abs(actual_const)}"
    poly_display = f"{a}x^3 + kx^2 {lin_str} {const_str}"

    div_sign = "-" if c > 0 else "+"
    div_str = f"x {div_sign} {abs(c)}"

    prompt = (
        f"Given that $({div_str})$ is an exact **factor** of $P(x) = {poly_display}$, "
        f"calculate the value of the unknown coefficient $k$."
    )
    corr = f"k = {k_val}"
    opts = [
        f"k = {k_val}",
        f"k = {k_val + 2}",
        f"k = {-k_val}",
        f"k = {k_val - 3}",
    ]
    r.shuffle(opts)

    return _add_pillars({
        "id": f"tech_poly_19_{r.randint(1000, 9999)}",
        "subskill": "19_factor_theorem_solve_unknown_coefficient_for_factor",
        "question_type": "mcq",
        "title": "Solve Unknown Coefficient k when Divisor is a Factor",
        "prompt": prompt,
        "question": prompt,
        "options": [f"${o}$" for o in opts],
        "correct_answer": f"${corr}$",
        "expected_answer": f"${corr}$",
        "sample_answer": f"${corr}$",
        "worked_solution": (
            f"\\text{{Since }} ({div_str}) \\text{{ is a factor, }} P({c}) = 0:\\\\\n"
            f"{a}({c})^3 + k({c})^2 + ({lin_coef})({c}) + ({actual_const}) = 0\\\\\n"
            f"{c**2}k + {a*c**3 + lin_coef*c + actual_const} = 0 \\implies k = {k_val}."
        ),
        "explanation": f"Set $P({c}) = 0$ and solve for $k$: $k = {k_val}$.",
        "marks": 3,
        "hints": {
            "tier_1": f"If $({div_str})$ is a factor, then $P({c}) = 0$.",
            "tier_2": f"Substitute $x = {c}$ into the expression and equate to 0.",
            "tier_3": f"Solve for $k$: $k = {k_val}$.",
        },
        "misconception_tags": ["sets_polynomial_equal_to_factor_instead_of_zero"],
    }, "19_factor_theorem_solve_unknown_coefficient_for_factor")


# --------------------------------------------------------------------------- #
# 20_factor_theorem_solve_unknown_coefficient_non_monic_factor
# --------------------------------------------------------------------------- #
def _build_20_factor_theorem_solve_unknown_coefficient_non_monic_factor(r: random.Random) -> Dict[str, Any]:
    # Factor (2x - 1) => root = 1/2
    a_div = 2
    b_div = 1
    root = sp.Rational(1, 2)
    k_val = r.choice([-8, -6, 4, 8, 10])
    p3 = 4
    # P(1/2) = 4(1/8) + k(1/4) - 5(1/2) + d = 0
    # 1/2 + k/4 - 5/2 + d = 0 => k/4 - 2 + d = 0 => d = 2 - k/4
    const = int(2 - k_val // 4)

    poly_display = f"4x^3 + kx^2 - 5x + ({const})"

    prompt = (
        f"If $(2x - 1)$ is a factor of $f(x) = {poly_display}$, determine the value of coefficient $k$."
    )
    corr = f"k = {k_val}"
    opts = [
        f"k = {k_val}",
        f"k = {k_val + 4}",
        f"k = {-k_val}",
        f"k = {k_val // 2}",
    ]
    r.shuffle(opts)

    return _add_pillars({
        "id": f"tech_poly_20_{r.randint(1000, 9999)}",
        "subskill": "20_factor_theorem_solve_unknown_coefficient_non_monic_factor",
        "question_type": "mcq",
        "title": "Solve Coefficient with Non-Monic Factor (2x - 1)",
        "prompt": prompt,
        "question": prompt,
        "options": [f"${o}$" for o in opts],
        "correct_answer": f"${corr}$",
        "expected_answer": f"${corr}$",
        "sample_answer": f"${corr}$",
        "worked_solution": (
            f"\\text{{Root of factor: }} 2x - 1 = 0 \\implies x = \\frac{{1}}{{2}}.\\\\\n"
            f"f\\left(\\frac{{1}}{{2}}\\right) = 0 \\implies 4\\left(\\frac{{1}}{{2}}\\right)^3 + k\\left(\\frac{{1}}{{2}}\\right)^2 - 5\\left(\\frac{{1}}{{2}}\\right) + {const} = 0\\\\\n"
            f"\\frac{{1}}{{2}} + \\frac{{k}}{{4}} - \\frac{{5}}{{2}} + {const} = 0 \\implies \\frac{{k}}{{4}} = {2 - const} \\implies k = {k_val}."
        ),
        "explanation": f"Set $f(1/2) = 0$ and solve: $k/4 - 2 + {const} = 0 \\implies k = {k_val}$.",
        "marks": 3,
        "hints": {
            "tier_1": "Find the root: $2x - 1 = 0 \\implies x = 1/2$.",
            "tier_2": "Substitute $x = 1/2$ into $f(x)$ and set equal to 0.",
            "tier_3": f"Solve for $k$: $k = {k_val}$.",
        },
        "misconception_tags": ["fraction_exponent_square_error"],
    }, "20_factor_theorem_solve_unknown_coefficient_non_monic_factor")


# --------------------------------------------------------------------------- #
# 21_factor_theorem_determine_both_factors_from_quadratic_factor
# --------------------------------------------------------------------------- #
def _build_21_factor_theorem_determine_both_factors_from_quadratic_factor(r: random.Random) -> Dict[str, Any]:
    c = r.choice([1, 2, 3])
    # (x^2 - c^2) is a factor => both (x - c) and (x + c) are factors
    other = r.choice([-4, 4, 5])
    poly = sp.expand((x**2 - c**2) * (x - other))
    poly_latex = sp.latex(poly)

    prompt = (
        f"Given that $(x^2 - {c**2})$ is a factor of $P(x) = {poly_latex}$, "
        f"which two linear factors does this immediately guarantee by difference of squares?"
    )
    corr = f"(x - {c}) \\text{{ and }} (x + {c})"
    opts = [
        f"(x - {c}) \\text{{ and }} (x + {c})",
        f"(x - {c**2}) \\text{{ and }} (x + {c**2})",
        f"(x - {c}) \\text{{ only}}",
        f"(x + {c}) \\text{{ only}}",
    ]
    r.shuffle(opts)

    return _add_pillars({
        "id": f"tech_poly_21_{r.randint(1000, 9999)}",
        "subskill": "21_factor_theorem_determine_both_factors_from_quadratic_factor",
        "question_type": "mcq",
        "title": "Difference of Squares Quadratic Factor Deductions",
        "prompt": prompt,
        "question": prompt,
        "options": [f"${o}$" for o in opts],
        "correct_answer": f"${corr}$",
        "expected_answer": f"${corr}$",
        "sample_answer": f"${corr}$",
        "worked_solution": f"x^2 - {c**2} = (x - {c})(x + {c}). \\text{{ Therefore, both }} (x - {c}) \\text{{ and }} (x + {c}) \\text{{ are linear factors of }} P(x).",
        "explanation": f"Factorising $x^2 - {c**2} = (x - {c})(x + {c})$ directly guarantees both linear factors.",
        "marks": 2,
        "hints": {
            "tier_1": "Recall the difference of squares identity: $a^2 - b^2 = (a - b)(a + b)$.",
            "tier_2": f"Factorise $x^2 - {c**2} = (x - {c})(x + {c})$.",
            "tier_3": f"Both $(x - {c})$ and $(x + {c})$ are factors.",
        },
        "misconception_tags": ["forgets_conjugate_pair_in_difference_of_squares"],
    }, "21_factor_theorem_determine_both_factors_from_quadratic_factor")


# --------------------------------------------------------------------------- #
# 22_factorise_cubic_common_factor_first
# --------------------------------------------------------------------------- #
def _build_22_factorise_cubic_common_factor_first(r: random.Random) -> Dict[str, Any]:
    # x(x - r1)(x - r2)
    r1 = r.choice([-3, -2, 2, 4])
    r2 = r.choice([-4, -1, 3, 5])
    poly = sp.expand(x * (x - r1) * (x - r2))
    poly_latex = sp.latex(poly)

    fac_expr = sp.factor(poly)
    fac_latex = sp.latex(fac_expr)

    prompt = f"Factorise completely by first taking out a common factor:\n\n$$f(x) = {poly_latex}$$"
    corr = f"{fac_latex}"
    opts = [
        f"{fac_latex}",
        f"x(x - {r1 + 1})(x - {r2})",
        f"(x - {r1})(x - {r2})",
        f"x(x^2 - {r1 * r2})",
    ]
    r.shuffle(opts)

    return _add_pillars({
        "id": f"tech_poly_22_{r.randint(1000, 9999)}",
        "subskill": "22_factorise_cubic_common_factor_first",
        "question_type": "mcq",
        "title": "Factorising Cubic by Common Factor First",
        "prompt": prompt,
        "question": prompt,
        "options": [f"${o}$" for o in opts],
        "correct_answer": f"${corr}$",
        "expected_answer": f"${corr}$",
        "sample_answer": f"${corr}$",
        "worked_solution": (
            f"\\text{{Step 1: Extract common factor }} x:\\\\\n"
            f"f(x) = x({sp.latex(sp.expand((x - r1)*(x - r2)))})\\\\\n"
            f"\\text{{Step 2: Factorise the quadratic trinomial}}:\\\\\n"
            f"= {fac_latex}."
        ),
        "explanation": f"Take out $x$ as common factor: $x(x^2 + \\dots)$, then factorise the remaining quadratic to get ${fac_latex}$.",
        "marks": 2,
        "hints": {
            "tier_1": "Notice that every term contains the variable $x$. Extract $x$ first.",
            "tier_2": "Factorise the remaining quadratic bracket into two binomials.",
            "tier_3": f"Full factorisation: ${fac_latex}$.",
        },
        "misconception_tags": ["forgets_extracted_common_factor_x"],
    }, "22_factorise_cubic_common_factor_first")


# --------------------------------------------------------------------------- #
# 23_factorise_cubic_grouping_in_pairs
# --------------------------------------------------------------------------- #
def _build_23_factorise_cubic_grouping_in_pairs(r: random.Random) -> Dict[str, Any]:
    # (x + a)*(x^2 - b^2) or (x - a)*(x^2 + b)
    a_val = r.choice([-3, -2, 2, 3])
    b_val = r.choice([1, 4, 9])
    # (x - a_val)*(x^2 + b_val) = x^3 - a*x^2 + b*x - a*b
    poly = sp.expand((x - a_val) * (x**2 - b_val))
    poly_latex = sp.latex(poly)
    fac_expr = sp.factor(poly)
    fac_latex = sp.latex(fac_expr)

    prompt = f"Factorise the cubic polynomial completely by **grouping terms in pairs**:\n\n$$P(x) = {poly_latex}$$"
    corr = f"{fac_latex}"
    opts = [
        f"{fac_latex}",
        f"(x - {a_val})(x^2 + {b_val})",
        f"(x^2 - {a_val})(x - {b_val})",
        f"(x - 1)(x - {a_val * b_val})",
    ]
    r.shuffle(opts)

    return _add_pillars({
        "id": f"tech_poly_23_{r.randint(1000, 9999)}",
        "subskill": "23_factorise_cubic_grouping_in_pairs",
        "question_type": "mcq",
        "title": "Factorising Cubic by Grouping in Pairs",
        "prompt": prompt,
        "question": prompt,
        "options": [f"${o}$" for o in opts],
        "correct_answer": f"${corr}$",
        "expected_answer": f"${corr}$",
        "sample_answer": f"${corr}$",
        "worked_solution": (
            f"\\text{{Group first two terms and last two terms:}}\\\\\n"
            f"= x^2(x - {a_val}) - {b_val}(x - {a_val})\\\\\n"
            f"= (x - {a_val})(x^2 - {b_val}) = {fac_latex}."
        ),
        "explanation": f"Group in pairs: $x^2(x - {a_val}) - {b_val}(x - {a_val}) = (x - {a_val})(x^2 - {b_val}) = {fac_latex}$.",
        "marks": 3,
        "hints": {
            "tier_1": "Group the first two terms together and the last two terms together.",
            "tier_2": f"Extract $x^2$ from the first pair and the common constant from the second pair.",
            "tier_3": f"Take out the common bracket $(x - {a_val})$ to get ${fac_latex}$.",
        },
        "misconception_tags": ["sign_error_grouping_second_pair"],
    }, "23_factorise_cubic_grouping_in_pairs")


# --------------------------------------------------------------------------- #
# 24_factorise_cubic_sum_or_difference_of_cubes
# --------------------------------------------------------------------------- #
def _build_24_factorise_cubic_sum_or_difference_of_cubes(r: random.Random) -> Dict[str, Any]:
    a_coef = r.choice([1, 2, 3])
    b_val = r.choice([1, 2, 3, 4])
    is_sum = r.choice([True, False])

    if is_sum:
        poly_expr = a_coef**3 * x**3 + b_val**3
        bin_part = f"{a_coef}x + {b_val}" if a_coef > 1 else f"x + {b_val}"
        quad_part = f"{a_coef**2}x^2 - {a_coef*b_val}x + {b_val**2}"
    else:
        poly_expr = a_coef**3 * x**3 - b_val**3
        bin_part = f"{a_coef}x - {b_val}" if a_coef > 1 else f"x - {b_val}"
        quad_part = f"{a_coef**2}x^2 + {a_coef*b_val}x + {b_val**2}"

    poly_latex = sp.latex(poly_expr)
    corr = f"({bin_part})({quad_part})"
    wrong_mid = f"({bin_part})({a_coef**2}x^2 {'+' if is_sum else '-'} {2*a_coef*b_val}x + {b_val**2})"

    prompt = f"Factorise completely using the sum or difference of cubes formula:\n\n$$f(x) = {poly_latex}$$"
    opts = [
        corr,
        wrong_mid,
        f"({bin_part})^3",
        f"({bin_part})({a_coef**2}x^2 - {b_val**2})",
    ]
    r.shuffle(opts)

    return _add_pillars({
        "id": f"tech_poly_24_{r.randint(1000, 9999)}",
        "subskill": "24_factorise_cubic_sum_or_difference_of_cubes",
        "question_type": "mcq",
        "title": "Sum and Difference of Two Cubes",
        "prompt": prompt,
        "question": prompt,
        "options": [f"${o}$" for o in opts],
        "correct_answer": f"${corr}$",
        "expected_answer": f"${corr}$",
        "sample_answer": f"${corr}$",
        "worked_solution": (
            f"\\text{{Use the identity }} a^3 \\pm b^3 = (a \\pm b)(a^2 \\mp ab + b^2):\\\\\n"
            f"{poly_latex} = ({bin_part})({quad_part})."
        ),
        "explanation": f"Apply $a^3 \\pm b^3 = (a \\pm b)(a^2 \\mp ab + b^2)$ to get $({bin_part})({quad_part})$.",
        "marks": 2,
        "hints": {
            "tier_1": "Recall: $a^3 - b^3 = (a - b)(a^2 + ab + b^2)$ and $a^3 + b^3 = (a + b)(a^2 - ab + b^2)$.",
            "tier_2": f"Here $a = {a_coef}x$ and $b = {b_val}$.",
            "tier_3": f"Result: $({bin_part})({quad_part})$.",
        },
        "misconception_tags": ["puts_2ab_in_quadratic_factor_of_cubes"],
    }, "24_factorise_cubic_sum_or_difference_of_cubes")


# --------------------------------------------------------------------------- #
# 25_cubic_synthetic_division_to_find_quadratic_factor
# --------------------------------------------------------------------------- #
def _build_25_cubic_synthetic_division_to_find_quadratic_factor(r: random.Random) -> Dict[str, Any]:
    c = r.choice([-2, -1, 1, 2])
    q_b = r.choice([-4, -2, 3, 5])
    q_c = r.choice([-6, -3, 2, 4])
    quot = x**2 + q_b*x + q_c
    poly = sp.expand((x - c) * quot)
    poly_latex = sp.latex(poly)
    quot_latex = sp.latex(quot)

    div_sign = "-" if c > 0 else "+"
    fac_str = f"x {div_sign} {abs(c)}"

    prompt = (
        f"Given that $({fac_str})$ is a factor of $f(x) = {poly_latex}$, "
        f"divide $f(x)$ by $({fac_str})$ to determine the remaining quadratic factor $Q(x)$."
    )
    corr = f"Q(x) = {quot_latex}"
    opts = [
        f"Q(x) = {quot_latex}",
        f"Q(x) = {sp.latex(x**2 - q_b*x + q_c)}",
        f"Q(x) = {sp.latex(x**2 + q_b*x - q_c)}",
        f"Q(x) = {sp.latex(2*x**2 + q_b*x + q_c)}",
    ]
    r.shuffle(opts)

    return _add_pillars({
        "id": f"tech_poly_25_{r.randint(1000, 9999)}",
        "subskill": "25_cubic_synthetic_division_to_find_quadratic_factor",
        "question_type": "mcq",
        "title": "Finding Remaining Quadratic Factor after First Linear Factor",
        "prompt": prompt,
        "question": prompt,
        "options": [f"${o}$" for o in opts],
        "correct_answer": f"${corr}$",
        "expected_answer": f"${corr}$",
        "sample_answer": f"${corr}$",
        "worked_solution": (
            f"\\text{{Divide }} {poly_latex} \\text{{ by }} ({fac_str}) \\text{{ using inspection or synthetic division:}}\\\\\n"
            f"f(x) = ({fac_str})({quot_latex}) \\implies Q(x) = {quot_latex}."
        ),
        "explanation": f"Dividing $f(x)$ by $({fac_str})$ leaves the quadratic factor $Q(x) = {quot_latex}$.",
        "marks": 3,
        "hints": {
            "tier_1": f"Divide $f(x)$ by $({fac_str})$ using synthetic division or polynomial long division.",
            "tier_2": f"The root is $x = {c}$. Perform synthetic division on the coefficients.",
            "tier_3": f"$Q(x) = {quot_latex}$.",
        },
        "misconception_tags": ["sign_error_middle_term_quadratic_factor"],
    }, "25_cubic_synthetic_division_to_find_quadratic_factor")


BUILDERS_01_25: Dict[str, Any] = {
    "01_identify_polynomial_definition_and_degree": _build_01_identify_polynomial_definition_and_degree,
    "02_identify_non_polynomial_negative_or_fractional_exponent": _build_02_identify_non_polynomial_negative_or_fractional_exponent,
    "03_classify_polynomial_monomial_binomial_trinomial": _build_03_classify_polynomial_monomial_binomial_trinomial,
    "04_polynomial_evaluation_function_notation": _build_04_polynomial_evaluation_function_notation,
    "05_polynomial_division_monomial_divisor": _build_05_polynomial_division_monomial_divisor,
    "06_polynomial_long_division_linear_divisor": _build_06_polynomial_long_division_linear_divisor,
    "07_polynomial_synthetic_division_monic_divisor": _build_07_polynomial_synthetic_division_monic_divisor,
    "08_remainder_theorem_linear_monic_positive_root": _build_08_remainder_theorem_linear_monic_positive_root,
    "09_remainder_theorem_linear_monic_negative_root": _build_09_remainder_theorem_linear_monic_negative_root,
    "10_remainder_theorem_linear_non_monic_fraction_root": _build_10_remainder_theorem_linear_non_monic_fraction_root,
    "11_remainder_theorem_zero_remainder_deduction": _build_11_remainder_theorem_zero_remainder_deduction,
    "12_remainder_theorem_solve_unknown_coefficient_k": _build_12_remainder_theorem_solve_unknown_coefficient_k,
    "13_remainder_theorem_solve_unknown_constant_term": _build_13_remainder_theorem_solve_unknown_constant_term,
    "14_remainder_theorem_equal_remainders_two_divisors": _build_14_remainder_theorem_equal_remainders_two_divisors,
    "15_remainder_theorem_simultaneous_two_unknown_coefficients": _build_15_remainder_theorem_simultaneous_two_unknown_coefficients,
    "16_factor_theorem_verify_linear_factor_monic": _build_16_factor_theorem_verify_linear_factor_monic,
    "17_factor_theorem_verify_linear_factor_non_monic": _build_17_factor_theorem_verify_linear_factor_non_monic,
    "18_factor_theorem_find_first_integer_factor_rational_root": _build_18_factor_theorem_find_first_integer_factor_rational_root,
    "19_factor_theorem_solve_unknown_coefficient_for_factor": _build_19_factor_theorem_solve_unknown_coefficient_for_factor,
    "20_factor_theorem_solve_unknown_coefficient_non_monic_factor": _build_20_factor_theorem_solve_unknown_coefficient_non_monic_factor,
    "21_factor_theorem_determine_both_factors_from_quadratic_factor": _build_21_factor_theorem_determine_both_factors_from_quadratic_factor,
    "22_factorise_cubic_common_factor_first": _build_22_factorise_cubic_common_factor_first,
    "23_factorise_cubic_grouping_in_pairs": _build_23_factorise_cubic_grouping_in_pairs,
    "24_factorise_cubic_sum_or_difference_of_cubes": _build_24_factorise_cubic_sum_or_difference_of_cubes,
    "25_cubic_synthetic_division_to_find_quadratic_factor": _build_25_cubic_synthetic_division_to_find_quadratic_factor,
}
