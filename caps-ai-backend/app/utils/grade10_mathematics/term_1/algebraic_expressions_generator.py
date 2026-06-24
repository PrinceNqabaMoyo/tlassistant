"""Grade 10 Mathematics — Term 1 — Algebraic Expressions (deterministic).

Curriculum source:
``curriculum_docs/Mathematics_Gr10/Term 1/1 Algebraic Expressions .md``.

Subskills (archetypes, not copied questions — SymPy produces unlimited variety):
    real_numbers          mcq         classify rational / irrational
    rounding              math_short  round to n decimal places (comma decimals)
    products              math_steps  expand binomial x binomial (FOIL)
    factorise_common      math_short  common-factor factorisation
    factorise_diff_squares math_short difference of two squares
    factorise_trinomial   math_short  quadratic trinomial
    simplify_fractions    math_short  simplify an algebraic fraction

All answers are computed; given a seed the output is identical.
"""
from __future__ import annotations

from typing import Any, Dict

import sympy as sp

from app.utils.grade10_mathematics._math_common import (
    build_generate,
    make_mcq,
    make_short,
    make_steps,
    nonzero,
    num,
    solution,
    step,
    to_latex,
    with_metadata,
)

TOPIC = "grade10_math_algebraic_expressions"
LO = "math10_algebraic_expressions"
x = sp.Symbol("x")


# --------------------------------------------------------------------------- #
# real_numbers
# --------------------------------------------------------------------------- #
def _build_real_numbers(r, difficulty: str) -> Dict[str, Any]:
    rationals = ["\\frac{3}{4}", "0{,}25", "7", "-\\frac{2}{5}", "0{,}\\overline{3}"]
    irrationals = ["\\sqrt{2}", "\\sqrt{5}", "\\pi", "\\sqrt[3]{7}", "\\frac{1+\\sqrt{5}}{2}"]
    pick_irrational = r.random() < 0.5
    if pick_irrational:
        target = r.choice(irrationals)
        options = [target] + r.sample(rationals, 3)
        correct_kind = "irrational"
    else:
        target = r.choice(rationals)
        options = [target] + r.sample(irrationals, 3)
        correct_kind = "rational"
    r.shuffle(options)
    correct_index = options.index(target)
    q = make_mcq(
        prefix=TOPIC,
        prompt="Which of the following numbers is " + ("irrational" if pick_irrational else "rational") + "?",
        options=[f"${o}$" for o in options],
        options_latex=options,
        correct_index=correct_index,
        explanation=(
            "A rational number can be written as a fraction a/b of integers (and its "
            "decimal terminates or recurs). An irrational number cannot, and its decimal "
            "neither terminates nor recurs."
        ),
        marks=1,
    )
    return with_metadata(
        q,
        topic=TOPIC,
        subskill="real_numbers",
        learning_objective_id=f"{LO}.real_numbers",
        misconception_tags=["confuses_surd_with_rational", "thinks_pi_is_rational"],
        diagnostic_tags=["number_classification"],
        keywords=["rational", "irrational", "surd", "recurring"],
    )


# --------------------------------------------------------------------------- #
# rounding (exercises the comma decimal convention)
# --------------------------------------------------------------------------- #
def _build_rounding(r, difficulty: str) -> Dict[str, Any]:
    places = r.choice([1, 2, 2, 3])
    whole = r.randint(0, 99)
    frac = r.randint(1, 9999)
    value = float(f"{whole}.{frac:04d}")
    rounded = round(value, places)
    plural = "s" if places != 1 else ""
    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Round {num(value)} to {places} decimal place{plural}.}}",
        answer_expr=sp.Rational(str(rounded)),
        answer_mode="value",
        answer_latex=num(rounded, places),
        marks=1,
        explanation=f"Look at the digit in position {places + 1}; round up if it is 5 or more.",
        hint="Identify the rounding digit, then check the next digit.",
    )
    return with_metadata(
        q,
        topic=TOPIC,
        subskill="rounding",
        learning_objective_id=f"{LO}.rounding",
        misconception_tags=["rounds_wrong_digit", "truncates_instead_of_rounds"],
        diagnostic_tags=["rounding"],
        keywords=["round", "decimal place"],
    )


# --------------------------------------------------------------------------- #
# products (math_steps, expression chain)
# --------------------------------------------------------------------------- #
def _build_products(r, difficulty: str) -> Dict[str, Any]:
    a = nonzero(r, 1, 4)
    b = nonzero(r, -6, 6)
    c = nonzero(r, 1, 4)
    d = nonzero(r, -6, 6)
    product = (a * x + b) * (c * x + d)
    expanded = sp.expand(product)

    # Uncollected distribution line (display only).
    uncollected = (
        f"({a}x)({c}x) "
        f"+ ({a}x)({_paren(d)}) "
        f"+ ({_paren(b)})({c}x) "
        f"+ ({_paren(b)})({_paren(d)})"
    )

    sol = solution(
        goal="expand the product",
        chain_type="expression",
        var="x",
        steps=[
            step(
                from_expr=product,
                to_expr=expanded,
                op="multiply each term (FOIL)",
                rule="distributive law",
                from_latex=to_latex(product),
                to_latex=uncollected,
                common_errors=["sign_error", "forgot_middle_term", "only_multiplied_firsts"],
            ),
            step(
                from_expr=expanded,
                to_expr=expanded,
                op="collect like terms",
                rule="add like terms",
                from_latex=uncollected,
                to_latex=to_latex(expanded),
                common_errors=["combined_unlike_terms"],
            ),
        ],
        final_expr=expanded,
        final_latex=to_latex(expanded),
    )
    q = make_steps(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Expand: }} {to_latex(product)}",
        canonical_solution=sol,
        marks=3,
        explanation="Multiply every term in the first bracket by every term in the second, then collect like terms.",
        hint="Use FOIL: First, Outer, Inner, Last.",
    )
    return with_metadata(
        q,
        topic=TOPIC,
        subskill="products",
        learning_objective_id=f"{LO}.products",
        misconception_tags=["sign_error", "forgot_middle_term"],
        diagnostic_tags=["expansion", "distributive_law"],
        keywords=["expand", "product", "FOIL", "distribute"],
    )


def _paren(n: int) -> str:
    return str(n) if n >= 0 else f"-{abs(n)}"


# --------------------------------------------------------------------------- #
# factorise_common
# --------------------------------------------------------------------------- #
def _build_factorise_common(r, difficulty: str) -> Dict[str, Any]:
    k = r.randint(2, 6)
    p = r.randint(1, 5)
    q_coeff = nonzero(r, -6, 6)
    expr = sp.expand(k * x * (p * x + q_coeff))
    factored = sp.factor(expr)
    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Factorise: }} {to_latex(expr)}",
        answer_expr=factored,
        answer_mode="factored",
        marks=2,
        explanation="Take out the highest common factor of the coefficients and the common variable.",
        hint="What is the largest number and power of x that divides every term?",
    )
    return with_metadata(
        q,
        topic=TOPIC,
        subskill="factorise_common",
        learning_objective_id=f"{LO}.factorise_common",
        misconception_tags=["incomplete_common_factor", "drops_variable"],
        diagnostic_tags=["factorisation", "common_factor"],
        keywords=["factorise", "common factor", "HCF"],
    )


# --------------------------------------------------------------------------- #
# factorise_diff_squares
# --------------------------------------------------------------------------- #
def _build_factorise_diff_squares(r, difficulty: str) -> Dict[str, Any]:
    a = r.randint(1, 6)      # coefficient sqrt
    b = r.randint(1, 9)
    expr = sp.expand((a * x) ** 2 - b ** 2)
    factored = sp.factor(expr)
    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Factorise: }} {to_latex(expr)}",
        answer_expr=factored,
        answer_mode="factored",
        marks=2,
        explanation="A difference of two squares a^2 - b^2 factorises as (a - b)(a + b).",
        hint="Write each term as a perfect square first.",
    )
    return with_metadata(
        q,
        topic=TOPIC,
        subskill="factorise_diff_squares",
        learning_objective_id=f"{LO}.factorise_diff_squares",
        misconception_tags=["sign_error", "treats_as_sum_of_squares"],
        diagnostic_tags=["factorisation", "difference_of_squares"],
        keywords=["difference of squares", "factorise"],
    )


# --------------------------------------------------------------------------- #
# factorise_trinomial
# --------------------------------------------------------------------------- #
def _build_factorise_trinomial(r, difficulty: str) -> Dict[str, Any]:
    root1 = nonzero(r, -6, 6)
    root2 = nonzero(r, -6, 6)
    expr = sp.expand((x - root1) * (x - root2))
    factored = sp.factor(expr)
    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Factorise: }} {to_latex(expr)}",
        answer_expr=factored,
        answer_mode="factored",
        marks=2,
        explanation="Find two numbers that multiply to the constant term and add to the coefficient of x.",
        hint="Which two numbers multiply to give the constant and add to give the middle coefficient?",
    )
    return with_metadata(
        q,
        topic=TOPIC,
        subskill="factorise_trinomial",
        learning_objective_id=f"{LO}.factorise_trinomial",
        misconception_tags=["wrong_sign_pair", "product_sum_swapped"],
        diagnostic_tags=["factorisation", "trinomial"],
        keywords=["trinomial", "factorise", "quadratic"],
    )


# --------------------------------------------------------------------------- #
# simplify_fractions
# --------------------------------------------------------------------------- #
def _build_simplify_fractions(r, difficulty: str) -> Dict[str, Any]:
    root = nonzero(r, -5, 5)
    other = nonzero(r, -5, 5, exclude=[root])
    numerator = sp.expand((x - root) * (x - other))
    denominator = x - root
    expr = numerator / denominator
    simplified = sp.cancel(expr)
    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Simplify: }} \\dfrac{{{to_latex(numerator)}}}{{{to_latex(denominator)}}}",
        answer_expr=simplified,
        answer_mode="expression",
        marks=2,
        explanation="Factorise the numerator, then cancel the common factor with the denominator.",
        hint="Factorise the top first; look for a factor matching the bottom.",
    )
    return with_metadata(
        q,
        topic=TOPIC,
        subskill="simplify_fractions",
        learning_objective_id=f"{LO}.simplify_fractions",
        misconception_tags=["cancels_terms_not_factors"],
        diagnostic_tags=["algebraic_fractions", "simplification"],
        keywords=["simplify", "fraction", "cancel", "factor"],
    )


SUBSKILLS = {
    "real_numbers": _build_real_numbers,
    "rounding": _build_rounding,
    "products": _build_products,
    "factorise_common": _build_factorise_common,
    "factorise_diff_squares": _build_factorise_diff_squares,
    "factorise_trinomial": _build_factorise_trinomial,
    "simplify_fractions": _build_simplify_fractions,
    # default / mixed alias
    "concepts": _build_real_numbers,
}

generate = build_generate(SUBSKILLS, default_subskill="real_numbers")
