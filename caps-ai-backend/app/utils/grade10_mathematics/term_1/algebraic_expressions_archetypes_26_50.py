"""Grade 10 Mathematics — Term 1 — Algebraic Expressions: Archetypes 26 to 50.

Ground truth: curriculum_docs/Mathematics_Gr10/Term 1/1 Algebraic Expressions .md
Zero LLM, 100% deterministic SymPy-backed questions with step-by-step solutions.
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional
import sympy as sp

from app.utils.grade10_mathematics._math_common import (
    make_mcq,
    make_short,
    make_steps,
    nonzero,
    num,
    solution,
    step,
    to_latex,
    to_latex_safe,
    with_metadata,
)

TOPIC = "grade10_math_algebraic_expressions"
LO = "math10_algebraic_expressions"
x = sp.Symbol("x")
y = sp.Symbol("y")
a_sym = sp.Symbol("a")
b_sym = sp.Symbol("b")


def _add_pillars(q: Dict[str, Any], subskill_name: str, duration: int = 3, weight: int = 15) -> Dict[str, Any]:
    marks = int(q.get("marks", 2))
    schema = [
        {"criterion": "Factorisation / algebraic fraction procedure", "marks": max(1, marks - 1)},
        {"criterion": "Accurate final factorised expression / simplest fraction", "marks": 1},
    ]
    q.update({
        "term": 1,
        "caps_weight_percent": weight,
        "suggested_duration_mins": duration,
        "mode": f"elementary_{subskill_name}",
        "marking_schema": schema,
    })
    return q


# --------------------------------------------------------------------------- #
# 26_factorise_difference_of_squares_simple
# --------------------------------------------------------------------------- #
def _build_26_factorise_difference_of_squares_simple(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    b = r.choice([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    expr = x**2 - b**2
    factored = sp.factor(expr)

    sol = solution(
        goal="factorise difference of two squares",
        chain_type="expression",
        var="x",
        steps=[
            step(from_expr=expr, to_expr=f"(x)^2 - ({b})^2", op="express as difference of squares", rule="a^2 - b^2"),
            step(from_expr=f"(x)^2 - ({b})^2", to_expr=factored, op="factorise into conjugates", rule="(a - b)(a + b)"),
        ],
        final_expr=factored,
    )
    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Factorise fully: }} {to_latex(expr)}",
        answer_expr=factored,
        answer_mode="factored",
        marks=2,
        canonical_solution=sol,
        explanation=f"Express as a difference of two squares: $x^2 - {b**2} = (x - {b})(x + {b})$.",
        hint="Identify the square roots of both terms: a^2 - b^2 = (a - b)(a + b).",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="26_factorise_difference_of_squares_simple",
        learning_objective_id=f"{LO}.26_diff_squares_simple",
        misconception_tags=["sign_error_diff_squares", "takes_square_root_wrongly"],
        diagnostic_tags=["factorisation", "difference_of_squares"],
        keywords=["difference of squares", "factorise"],
    )
    return _add_pillars(q, "26_factorise_difference_of_squares_simple", duration=2, weight=15)


# --------------------------------------------------------------------------- #
# 27_factorise_difference_of_squares_with_coefficient
# --------------------------------------------------------------------------- #
def _build_27_factorise_difference_of_squares_with_coefficient(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    a = r.choice([2, 3, 4, 5])
    b = r.choice([1, 3, 5, 7])
    expr = (a * x)**2 - b**2
    factored = sp.factor(expr)

    sol = solution(
        goal="factorise difference of squares with leading coefficient",
        chain_type="expression",
        var="x",
        steps=[
            step(from_expr=expr, to_expr=f"({a}x)^2 - ({b})^2", op="rewrite terms as squares", rule="a^2 - b^2"),
            step(from_expr=f"({a}x)^2 - ({b})^2", to_expr=factored, op="apply difference of squares", rule="(ax - b)(ax + b)"),
        ],
        final_expr=factored,
    )
    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Factorise: }} {to_latex(expr)}",
        answer_expr=factored,
        answer_mode="factored",
        marks=2,
        canonical_solution=sol,
        explanation=f"Write as $({a}x)^2 - ({b})^2 = ({a}x - {b})({a}x + {b})$.",
        hint="Find the square root of both the coefficient of x^2 and the constant.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="27_factorise_difference_of_squares_with_coefficient",
        learning_objective_id=f"{LO}.27_diff_squares_coeff",
        misconception_tags=["fails_to_square_root_coefficient", "sign_error"],
        diagnostic_tags=["factorisation", "difference_of_squares"],
        keywords=["difference of squares", "coefficient", "factorise"],
    )
    return _add_pillars(q, "27_factorise_difference_of_squares_with_coefficient", duration=2, weight=15)


# --------------------------------------------------------------------------- #
# 28_factorise_difference_of_squares_common_factor_first
# --------------------------------------------------------------------------- #
def _build_28_factorise_difference_of_squares_common_factor_first(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    k = r.choice([2, 3, 5])
    b = r.choice([1, 2, 3, 4, 5])
    expr = k * (x**2 - b**2)
    factored = sp.factor(expr)

    sol = solution(
        goal="take common factor first then difference of squares",
        chain_type="expression",
        var="x",
        steps=[
            step(from_expr=expr, to_expr=f"{k}(x^2 - {b**2})", op="factor out common factor", rule="HCF"),
            step(from_expr=f"{k}(x^2 - {b**2})", to_expr=factored, op="factorise difference of squares", rule="(x - b)(x + b)"),
        ],
        final_expr=factored,
    )
    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Factorise fully: }} {to_latex(sp.expand(expr))}",
        answer_expr=factored,
        answer_mode="factored",
        marks=3,
        canonical_solution=sol,
        explanation=f"First take out the common factor of ${k}$: ${k}(x^2 - {b**2})$. Then factorise the difference of squares: ${to_latex(factored)}$.",
        hint=f"Always check for a common factor first (in this case, {k}).",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="28_factorise_difference_of_squares_common_factor_first",
        learning_objective_id=f"{LO}.28_diff_squares_common_first",
        misconception_tags=["forgets_common_factor_step", "stops_after_common_factor"],
        diagnostic_tags=["factorisation", "multi_step_factorisation"],
        keywords=["common factor", "difference of squares", "factorise fully"],
    )
    return _add_pillars(q, "28_factorise_difference_of_squares_common_factor_first", duration=3, weight=15)


# --------------------------------------------------------------------------- #
# 29_factorise_difference_of_squares_brackets
# --------------------------------------------------------------------------- #
def _build_29_factorise_difference_of_squares_brackets(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    a = nonzero(r, 1, 5)
    b = r.choice([2, 3, 4, 5])
    expr = (x + a)**2 - b**2
    part1 = x + a - b
    part2 = x + a + b
    factored = part1 * part2

    sol = solution(
        goal="factorise difference of squares with brackets",
        chain_type="expression",
        var="x",
        steps=[
            step(from_expr=expr, to_expr=f"[(x + {a}) - {b}][(x + {a}) + {b}]", op="apply difference of squares", rule="A^2 - B^2 = (A-B)(A+B)"),
            step(from_expr=f"[(x + {a}) - {b}][(x + {a}) + {b}]", to_expr=f"({to_latex(part1)})({to_latex(part2)})", op="simplify inside brackets", rule="combine constants"),
        ],
        final_expr=factored,
    )
    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Factorise fully: }} (x + {a})^2 - {b**2}",
        answer_expr=factored,
        answer_mode="factored",
        marks=3,
        canonical_solution=sol,
        explanation=f"Treat $(x + {a})$ as a single term: $[(x + {a}) - {b}][(x + {a}) + {b}] = ({to_latex(part1)})({to_latex(part2)})$.",
        hint="Treat the bracket as a single unit A, so A^2 - b^2 = (A - b)(A + b).",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="29_factorise_difference_of_squares_brackets",
        learning_objective_id=f"{LO}.29_diff_squares_brackets",
        misconception_tags=["expands_instead_of_factorising", "sign_error_combining_constants"],
        diagnostic_tags=["factorisation", "compound_difference_of_squares"],
        keywords=["difference of squares", "brackets", "factorise"],
    )
    return _add_pillars(q, "29_factorise_difference_of_squares_brackets", duration=3, weight=15)


# --------------------------------------------------------------------------- #
# 30_factorise_grouping_two_by_two_standard
# --------------------------------------------------------------------------- #
def _build_30_factorise_grouping_two_by_two_standard(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    a = nonzero(r, 2, 5)
    b = nonzero(r, 2, 6)
    k = nonzero(r, 1, 5)
    # k*a*x + k*a*y + b*x + b*y = (k*a + b)(x + y)
    term1 = k * a * x
    term2 = k * a * y
    term3 = b * x
    term4 = b * y
    expr = term1 + term2 + term3 + term4
    factored = (x + y) * (k * a + b)

    sol = solution(
        goal="factorise four terms by grouping in pairs",
        chain_type="expression",
        var="x",
        steps=[
            step(from_expr=expr, to_expr=f"({term1} + {term2}) + ({term3} + {term4})", op="group terms in pairs", rule="associative law"),
            step(from_expr=f"({term1} + {term2}) + ({term3} + {term4})", to_expr=f"{k*a}(x + y) + {b}(x + y)", op="factor common factor from each pair", rule="HCF"),
            step(from_expr=f"{k*a}(x + y) + {b}(x + y)", to_expr=factored, op="take out common bracket", rule="common binomial factor"),
        ],
        final_expr=factored,
    )
    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Factorise by grouping in pairs: }} {to_latex(expr)}",
        answer_expr=factored,
        answer_mode="factored",
        marks=3,
        canonical_solution=sol,
        explanation=f"Group first two terms and last two terms: ${k*a}(x + y) + {b}(x + y) = (x + y)({k*a + b})$.",
        hint="Group the first two terms and the last two terms to find a common bracket.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="30_factorise_grouping_two_by_two_standard",
        learning_objective_id=f"{LO}.30_grouping_standard",
        misconception_tags=["incorrect_grouping", "forgets_to_factor_common_bracket"],
        diagnostic_tags=["factorisation", "grouping"],
        keywords=["grouping", "pairs", "factorise"],
    )
    return _add_pillars(q, "30_factorise_grouping_two_by_two_standard", duration=3, weight=15)


# --------------------------------------------------------------------------- #
# 31_factorise_grouping_with_sign_change
# --------------------------------------------------------------------------- #
def _build_31_factorise_grouping_with_sign_change(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    a = nonzero(r, 2, 5)
    b = nonzero(r, 2, 5)
    # a*x - a*y - b*x + b*y = a(x - y) - b(x - y) = (x - y)(a - b)
    term1 = a * x
    term2 = -a * y
    term3 = -b * x
    term4 = b * y
    expr = term1 + term2 + term3 + term4
    factored = (x - y) * (a - b)

    sol = solution(
        goal="factorise by grouping with negative common factor",
        chain_type="expression",
        var="x",
        steps=[
            step(from_expr=expr, to_expr=f"{a}(x - y) - {b}(x - y)", op="factor -b from second pair", rule="sign change with negative factor"),
            step(from_expr=f"{a}(x - y) - {b}(x - y)", to_expr=factored, op="take out common bracket (x - y)", rule="common binomial factor"),
        ],
        final_expr=factored,
    )
    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Factorise fully: }} {to_latex(expr)}",
        answer_expr=factored,
        answer_mode="factored",
        marks=3,
        canonical_solution=sol,
        explanation=f"Factor ${a}$ from first pair and $-{b}$ from second pair: ${a}(x - y) - {b}(x - y) = (x - y)({a} - {b})$.",
        hint="When factoring out a negative from the second pair, remember the sign inside changes: -bx + by = -b(x - y).",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="31_factorise_grouping_with_sign_change",
        learning_objective_id=f"{LO}.31_grouping_sign_change",
        misconception_tags=["sign_error_taking_negative_common_factor", "brackets_do_not_match"],
        diagnostic_tags=["factorisation", "grouping_sign_change"],
        keywords=["grouping", "sign change", "factorise"],
    )
    return _add_pillars(q, "31_factorise_grouping_with_sign_change", duration=3, weight=15)


# --------------------------------------------------------------------------- #
# 32_factorise_grouping_three_and_one_diff_squares
# --------------------------------------------------------------------------- #
def _build_32_factorise_grouping_three_and_one_diff_squares(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    a = nonzero(r, 1, 5)
    # x^2 + 2ax + a^2 - y^2 = (x + a)^2 - y^2 = (x + a - y)(x + a + y)
    expr = x**2 + 2*a*x + a**2 - y**2
    part1 = x + a - y
    part2 = x + a + y
    factored = part1 * part2

    sol = solution(
        goal="factorise grouping 3 and 1 as difference of squares",
        chain_type="expression",
        var="x",
        steps=[
            step(from_expr=expr, to_expr=f"(x^2 + {2*a}x + {a**2}) - y^2", op="group trinomial perfect square", rule="trinomial grouping"),
            step(from_expr=f"(x^2 + {2*a}x + {a**2}) - y^2", to_expr=f"(x + {a})^2 - y^2", op="factor perfect square trinomial", rule="(x + a)^2"),
            step(from_expr=f"(x + {a})^2 - y^2", to_expr=factored, op="factor difference of squares", rule="A^2 - B^2 = (A - B)(A + B)"),
        ],
        final_expr=factored,
    )
    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Factorise fully: }} {to_latex(expr)}",
        answer_expr=factored,
        answer_mode="factored",
        marks=3,
        canonical_solution=sol,
        explanation=f"Group the first three terms as a perfect square: $(x + {a})^2 - y^2$. Then apply difference of squares: $({to_latex(part1)})({to_latex(part2)})$.",
        hint="Recognise the first three terms as a perfect square trinomial: (x + a)^2.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="32_factorise_grouping_three_and_one_diff_squares",
        learning_objective_id=f"{LO}.32_grouping_three_one",
        misconception_tags=["tries_2x2_grouping_instead_of_3x1", "fails_to_recognise_perfect_square"],
        diagnostic_tags=["factorisation", "advanced_grouping"],
        keywords=["grouping 3 and 1", "perfect square", "difference of squares"],
    )
    return _add_pillars(q, "32_factorise_grouping_three_and_one_diff_squares", duration=3, weight=15)


# --------------------------------------------------------------------------- #
# 33_factorise_trinomial_monic_positive_roots
# --------------------------------------------------------------------------- #
def _build_33_factorise_trinomial_monic_positive_roots(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    p = r.randint(1, 6)
    q_val = r.randint(1, 7)
    expr = (x + p) * (x + q_val)
    expanded = sp.expand(expr)

    sol = solution(
        goal="factorise monic trinomial with positive constant",
        chain_type="expression",
        var="x",
        steps=[
            step(from_expr=expanded, to_expr=f"(x + {p})(x + {q_val})",
                 op="find two factors of constant that add to middle coefficient",
                 rule=f"{p} * {q_val} = {p*q_val} and {p} + {q_val} = {p+q_val}"),
        ],
        final_expr=expr,
    )
    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Factorise: }} {to_latex(expanded)}",
        answer_expr=expr,
        answer_mode="factored",
        marks=2,
        canonical_solution=sol,
        explanation=f"Find two numbers that multiply to ${p*q_val}$ and add to ${p+q_val}$: the numbers are ${p}$ and ${q_val}$. Thus $(x + {p})(x + {q_val})$.",
        hint=f"Find two numbers that multiply to give {p*q_val} and add to give {p+q_val}.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="33_factorise_trinomial_monic_positive_roots",
        learning_objective_id=f"{LO}.33_trinomial_positive",
        misconception_tags=["wrong_factors_of_constant", "sign_error_trinomial"],
        diagnostic_tags=["factorisation", "quadratic_trinomial"],
        keywords=["trinomial", "monic", "quadratic", "factorise"],
    )
    return _add_pillars(q, "33_factorise_trinomial_monic_positive_roots", duration=2, weight=15)


# --------------------------------------------------------------------------- #
# 34_factorise_trinomial_monic_mixed_signs
# --------------------------------------------------------------------------- #
def _build_34_factorise_trinomial_monic_mixed_signs(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    p = nonzero(r, 1, 8)
    q_val = nonzero(r, 1, 8, exclude=[p])
    # (x + p)(x - q_val)
    expr = (x + p) * (x - q_val)
    expanded = sp.expand(expr)

    sol = solution(
        goal="factorise monic trinomial with negative constant",
        chain_type="expression",
        var="x",
        steps=[
            step(from_expr=expanded, to_expr=expr,
                 op="find factors of negative constant",
                 rule=f"{p} * (-{q_val}) = {-p*q_val} and {p} + (-{q_val}) = {p - q_val}"),
        ],
        final_expr=expr,
    )
    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Factorise: }} {to_latex(expanded)}",
        answer_expr=expr,
        answer_mode="factored",
        marks=2,
        canonical_solution=sol,
        explanation=f"Find two factors of ${-p*q_val}$ that sum to ${p - q_val}$: the numbers are ${p}$ and ${-q_val}$. Result: ${to_latex(expr)}$.",
        hint=f"Because the constant is negative, one factor is positive and one is negative.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="34_factorise_trinomial_monic_mixed_signs",
        learning_objective_id=f"{LO}.34_trinomial_mixed_signs",
        misconception_tags=["swaps_signs_on_factors", "sum_and_product_swapped"],
        diagnostic_tags=["factorisation", "trinomial_mixed_signs"],
        keywords=["trinomial", "mixed signs", "factorise"],
    )
    return _add_pillars(q, "34_factorise_trinomial_monic_mixed_signs", duration=2, weight=15)


# --------------------------------------------------------------------------- #
# 35_factorise_trinomial_non_monic
# --------------------------------------------------------------------------- #
def _build_35_factorise_trinomial_non_monic(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    a = r.choice([2, 3])
    b = nonzero(r, 1, 5)
    c = 1
    d = nonzero(r, -5, 5)
    b1 = a * x + b
    b2 = c * x + d
    expr = b1 * b2
    expanded = sp.expand(expr)

    sol = solution(
        goal="factorise non-monic trinomial",
        chain_type="expression",
        var="x",
        steps=[
            step(from_expr=expanded, to_expr=f"{a}x^2 + {a*d}x + {b}x + {b*d}", op="split middle term", rule=f"ac method: product = {a*b*d}"),
            step(from_expr=f"{a}x^2 + {a*d}x + {b}x + {b*d}", to_expr=expr, op="factorise by grouping", rule="grouping"),
        ],
        final_expr=expr,
    )
    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Factorise: }} {to_latex(expanded)}",
        answer_expr=expr,
        answer_mode="factored",
        marks=3,
        canonical_solution=sol,
        explanation=f"Use the ac method or cross method to factorise $ax^2 + bx + c$: $({to_latex(b1)})({to_latex(b2)})$.",
        hint="Use the ac method: multiply leading coefficient by constant, find two factors that add to the middle term.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="35_factorise_trinomial_non_monic",
        learning_objective_id=f"{LO}.35_trinomial_non_monic",
        misconception_tags=["treats_as_monic", "cross_multiplication_error"],
        diagnostic_tags=["factorisation", "non_monic_trinomial"],
        keywords=["non-monic", "quadratic trinomial", "ac method"],
    )
    return _add_pillars(q, "35_factorise_trinomial_non_monic", duration=3, weight=15)


# --------------------------------------------------------------------------- #
# 36_factorise_trinomial_common_factor_first
# --------------------------------------------------------------------------- #
def _build_36_factorise_trinomial_common_factor_first(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    k = r.choice([2, 3, 4, 5])
    p = nonzero(r, 1, 5)
    q_val = nonzero(r, -5, 5)
    tri = (x + p) * (x + q_val)
    expr = k * tri
    expanded = sp.expand(expr)
    factored = sp.factor(expanded)

    sol = solution(
        goal="take out common factor then factorise trinomial",
        chain_type="expression",
        var="x",
        steps=[
            step(from_expr=expanded, to_expr=f"{k}({to_latex(sp.expand(tri))})", op="take out HCF", rule="common factor"),
            step(from_expr=f"{k}({to_latex(sp.expand(tri))})", to_expr=factored, op="factorise remaining quadratic trinomial", rule="trinomial factorisation"),
        ],
        final_expr=factored,
    )
    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Factorise fully: }} {to_latex(expanded)}",
        answer_expr=factored,
        answer_mode="factored",
        marks=3,
        canonical_solution=sol,
        explanation=f"First take out the common factor ${k}$: ${k}({to_latex(sp.expand(tri))})$. Then factorise the trinomial: ${to_latex(factored)}$.",
        hint=f"Take out the common factor {k} first.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="36_factorise_trinomial_common_factor_first",
        learning_objective_id=f"{LO}.36_trinomial_common_first",
        misconception_tags=["forgets_to_factorise_trinomial_after_hcf", "drops_hcf_from_final_answer"],
        diagnostic_tags=["factorisation", "multi_step_trinomial"],
        keywords=["common factor", "trinomial", "factorise fully"],
    )
    return _add_pillars(q, "36_factorise_trinomial_common_factor_first", duration=3, weight=15)


# --------------------------------------------------------------------------- #
# 37_factorise_trinomial_negative_leading_coeff
# --------------------------------------------------------------------------- #
def _build_37_factorise_trinomial_negative_leading_coeff(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    p = nonzero(r, 1, 6)
    q_val = nonzero(r, -6, 6)
    tri = (x + p) * (x + q_val)
    expr = -1 * tri
    expanded = sp.expand(expr)
    factored = sp.factor(expanded)

    sol = solution(
        goal="factorise trinomial with negative leading coefficient",
        chain_type="expression",
        var="x",
        steps=[
            step(from_expr=expanded, to_expr=f"-({to_latex(sp.expand(tri))})", op="take out -1 as common factor", rule="factor out negative sign"),
            step(from_expr=f"-({to_latex(sp.expand(tri))})", to_expr=factored, op="factorise monic trinomial", rule="trinomial"),
        ],
        final_expr=factored,
    )
    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Factorise fully: }} {to_latex(expanded)}",
        answer_expr=factored,
        answer_mode="factored",
        marks=3,
        canonical_solution=sol,
        explanation=f"Take out $-1$ as a common factor first: $-({to_latex(sp.expand(tri))})$. Then factorise inside the bracket: ${to_latex(factored)}$.",
        hint="Always take out -1 as a common factor when the x^2 coefficient is negative.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="37_factorise_trinomial_negative_leading_coeff",
        learning_objective_id=f"{LO}.37_trinomial_negative_lead",
        misconception_tags=["sign_error_factoring_negative_one", "loses_negative_sign_in_front"],
        diagnostic_tags=["factorisation", "negative_leading_coefficient"],
        keywords=["negative leading coefficient", "trinomial", "factorise"],
    )
    return _add_pillars(q, "37_factorise_trinomial_negative_leading_coeff", duration=3, weight=15)


# --------------------------------------------------------------------------- #
# 38_factorise_sum_of_two_cubes
# --------------------------------------------------------------------------- #
def _build_38_factorise_sum_of_two_cubes(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    b = r.choice([1, 2, 3, 4, 5])
    expr = x**3 + b**3
    factored = (x + b) * (x**2 - b * x + b**2)

    sol = solution(
        goal="factorise sum of two cubes",
        chain_type="expression",
        var="x",
        steps=[
            step(from_expr=expr, to_expr=f"(x)^3 + ({b})^3", op="recognise sum of cubes", rule="a^3 + b^3"),
            step(from_expr=f"(x)^3 + ({b})^3", to_expr=factored, op="apply identity (a+b)(a^2 - ab + b^2)", rule="sum of cubes formula"),
        ],
        final_expr=factored,
    )
    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Factorise: }} {to_latex(expr)}",
        answer_expr=factored,
        answer_mode="factored",
        marks=2,
        canonical_solution=sol,
        explanation=f"Use $a^3 + b^3 = (a + b)(a^2 - ab + b^2)$: $x^3 + {b**3} = (x + {b})(x^2 - {b}x + {b**2})$.",
        hint="Sum of cubes: (a + b)(a^2 - ab + b^2). Note the middle sign is minus.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="38_factorise_sum_of_two_cubes",
        learning_objective_id=f"{LO}.38_sum_of_cubes",
        misconception_tags=["wrong_sign_in_trinomial", "doubles_middle_term_ab"],
        diagnostic_tags=["factorisation", "sum_of_cubes"],
        keywords=["sum of cubes", "factorise", "cubic identity"],
    )
    return _add_pillars(q, "38_factorise_sum_of_two_cubes", duration=2, weight=15)


# --------------------------------------------------------------------------- #
# 39_factorise_difference_of_two_cubes
# --------------------------------------------------------------------------- #
def _build_39_factorise_difference_of_two_cubes(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    b = r.choice([1, 2, 3, 4, 5])
    expr = x**3 - b**3
    factored = (x - b) * (x**2 + b * x + b**2)

    sol = solution(
        goal="factorise difference of two cubes",
        chain_type="expression",
        var="x",
        steps=[
            step(from_expr=expr, to_expr=f"(x)^3 - ({b})^3", op="recognise difference of cubes", rule="a^3 - b^3"),
            step(from_expr=f"(x)^3 - ({b})^3", to_expr=factored, op="apply identity (a-b)(a^2 + ab + b^2)", rule="difference of cubes formula"),
        ],
        final_expr=factored,
    )
    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Factorise: }} {to_latex(expr)}",
        answer_expr=factored,
        answer_mode="factored",
        marks=2,
        canonical_solution=sol,
        explanation=f"Use $a^3 - b^3 = (a - b)(a^2 + ab + b^2)$: $x^3 - {b**3} = (x - {b})(x^2 + {b}x + {b**2})$.",
        hint="Difference of cubes: (a - b)(a^2 + ab + b^2). Note the middle sign is plus.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="39_factorise_difference_of_two_cubes",
        learning_objective_id=f"{LO}.39_difference_of_cubes",
        misconception_tags=["wrong_sign_in_trinomial", "squares_brackets"],
        diagnostic_tags=["factorisation", "difference_of_cubes"],
        keywords=["difference of cubes", "factorise"],
    )
    return _add_pillars(q, "39_factorise_difference_of_two_cubes", duration=2, weight=15)


# --------------------------------------------------------------------------- #
# 40_factorise_sum_diff_cubes_with_common_factor
# --------------------------------------------------------------------------- #
def _build_40_factorise_sum_diff_cubes_with_common_factor(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    k = r.choice([2, 3, 5])
    b = r.choice([1, 2, 3])
    sign = r.choice(["sum", "diff"])
    if sign == "sum":
        inner = x**3 + b**3
        inner_factored = (x + b) * (x**2 - b * x + b**2)
    else:
        inner = x**3 - b**3
        inner_factored = (x - b) * (x**2 + b * x + b**2)

    expr = k * inner
    expanded = sp.expand(expr)
    factored = k * inner_factored

    sol = solution(
        goal="factorise cubes with common factor",
        chain_type="expression",
        var="x",
        steps=[
            step(from_expr=expanded, to_expr=f"{k}({to_latex(inner)})", op="take out common factor", rule="HCF"),
            step(from_expr=f"{k}({to_latex(inner)})", to_expr=factored, op="factorise sum/difference of cubes", rule="cubic identity"),
        ],
        final_expr=factored,
    )
    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Factorise fully: }} {to_latex(expanded)}",
        answer_expr=factored,
        answer_mode="factored",
        marks=3,
        canonical_solution=sol,
        explanation=f"First take out the common factor of ${k}$: ${k}({to_latex(inner)})$. Then factorise the cubic expression: ${to_latex(factored)}$.",
        hint=f"Take out {k} as a common factor first, then recognise the sum or difference of cubes.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="40_factorise_sum_diff_cubes_with_common_factor",
        learning_objective_id=f"{LO}.40_cubes_common_factor",
        misconception_tags=["forgets_common_factor", "incomplete_factorisation"],
        diagnostic_tags=["factorisation", "advanced_cubes"],
        keywords=["cubes", "common factor", "factorise fully"],
    )
    return _add_pillars(q, "40_factorise_sum_diff_cubes_with_common_factor", duration=3, weight=15)


# --------------------------------------------------------------------------- #
# 41_simplify_fraction_monomial_over_monomial
# --------------------------------------------------------------------------- #
def _build_41_simplify_fraction_monomial_over_monomial(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    c_num = r.randint(2, 6) * r.choice([2, 3, 5])
    c_den = r.randint(2, 6) * r.choice([2, 3, 5])
    m_exp = r.randint(2, 5)
    n_exp = r.randint(1, 4)
    p_exp = r.randint(1, 4)
    q_exp = r.randint(2, 5)

    num_expr = c_num * x**m_exp * y**n_exp
    den_expr = c_den * x**p_exp * y**q_exp
    simplified = sp.cancel(num_expr / den_expr)

    sol = solution(
        goal="simplify monomial algebraic fraction",
        chain_type="expression",
        var="x",
        steps=[
            step(from_expr=f"\\frac{{{to_latex(num_expr)}}}{{{to_latex(den_expr)}}}",
                 to_expr=simplified,
                 op="divide coefficients and subtract exponents of like bases", rule="quotient rule for exponents"),
        ],
        final_expr=simplified,
    )
    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Simplify: }} \\dfrac{{{to_latex(num_expr)}}}{{{to_latex(den_expr)}}}",
        answer_expr=simplified,
        answer_mode="expression",
        marks=2,
        canonical_solution=sol,
        explanation=f"Simplify the numerical coefficients by dividing by their HCF, and apply the exponent quotient rule $a^m / a^n = a^{{m-n}}$: ${to_latex(simplified)}$.",
        hint="Divide the numbers and subtract exponents for the same base.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="41_simplify_fraction_monomial_over_monomial",
        learning_objective_id=f"{LO}.41_fraction_monomial",
        misconception_tags=["adds_exponents_instead_of_subtracting", "fails_to_reduce_coefficients"],
        diagnostic_tags=["algebraic_fractions", "monomials"],
        keywords=["algebraic fraction", "monomial", "simplify"],
    )
    return _add_pillars(q, "41_simplify_fraction_monomial_over_monomial", duration=2, weight=15)


# --------------------------------------------------------------------------- #
# 42_simplify_fraction_common_factor_cancel
# --------------------------------------------------------------------------- #
def _build_42_simplify_fraction_common_factor_cancel(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    k = nonzero(r, 2, 5)
    a = nonzero(r, 1, 4)
    b = nonzero(r, -6, 6)
    num_expr = k * x * (a * x + b)
    den_expr = k * x
    simplified = a * x + b

    sol = solution(
        goal="simplify fraction with common factor",
        chain_type="expression",
        var="x",
        steps=[
            step(from_expr=f"\\frac{{{to_latex(sp.expand(num_expr))}}}{{{to_latex(den_expr)}}}",
                 to_expr=f"\\frac{{{k}x({to_latex(a*x + b)})}}{{{k}x}}",
                 op="factorise numerator", rule="HCF"),
            step(from_expr=f"\\frac{{{k}x({to_latex(a*x + b)})}}{{{k}x}}",
                 to_expr=simplified,
                 op="cancel common factor", rule="cancellation"),
        ],
        final_expr=simplified,
    )
    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Simplify: }} \\dfrac{{{to_latex(sp.expand(num_expr))}}}{{{to_latex(den_expr)}}}",
        answer_expr=simplified,
        answer_mode="expression",
        marks=2,
        canonical_solution=sol,
        explanation=f"Factorise ${k}x$ out of the numerator: $\\dfrac{{{k}x({to_latex(simplified)})}}{{{k}x}} = {to_latex(simplified)}$.",
        hint="Factorise the numerator first. Never cancel individual terms across an addition sign!",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="42_simplify_fraction_common_factor_cancel",
        learning_objective_id=f"{LO}.42_fraction_common_factor",
        misconception_tags=["cancels_individual_terms", "forgets_to_factorise_numerator"],
        diagnostic_tags=["algebraic_fractions", "common_factor"],
        keywords=["algebraic fraction", "common factor", "cancel"],
    )
    return _add_pillars(q, "42_simplify_fraction_common_factor_cancel", duration=2, weight=15)


# --------------------------------------------------------------------------- #
# 43_simplify_fraction_diff_squares_cancel
# --------------------------------------------------------------------------- #
def _build_43_simplify_fraction_diff_squares_cancel(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    b = r.choice([2, 3, 4, 5, 6, 7])
    sign = r.choice(["plus", "minus"])
    num_expr = x**2 - b**2
    den_expr = x + b if sign == "plus" else x - b
    simplified = x - b if sign == "plus" else x + b

    sol = solution(
        goal="simplify fraction with difference of squares",
        chain_type="expression",
        var="x",
        steps=[
            step(from_expr=f"\\frac{{{to_latex(num_expr)}}}{{{to_latex(den_expr)}}}",
                 to_expr=f"\\frac{{(x - {b})(x + {b})}}{{{to_latex(den_expr)}}}",
                 op="factorise numerator", rule="difference of squares"),
            step(from_expr=f"\\frac{{(x - {b})(x + {b})}}{{{to_latex(den_expr)}}}",
                 to_expr=simplified,
                 op="cancel common bracket", rule="cancellation"),
        ],
        final_expr=simplified,
    )
    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Simplify: }} \\dfrac{{{to_latex(num_expr)}}}{{{to_latex(den_expr)}}}",
        answer_expr=simplified,
        answer_mode="expression",
        marks=2,
        canonical_solution=sol,
        explanation=f"Factorise the numerator: $x^2 - {b**2} = (x - {b})(x + {b})$. Cancel with the denominator to get ${to_latex(simplified)}$.",
        hint="Factorise the numerator as a difference of two squares first.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="43_simplify_fraction_diff_squares_cancel",
        learning_objective_id=f"{LO}.43_fraction_diff_squares",
        misconception_tags=["cancels_x_squared_with_x", "sign_error_after_cancellation"],
        diagnostic_tags=["algebraic_fractions", "difference_of_squares"],
        keywords=["fraction", "difference of squares", "simplify"],
    )
    return _add_pillars(q, "43_simplify_fraction_diff_squares_cancel", duration=2, weight=15)


# --------------------------------------------------------------------------- #
# 44_simplify_fraction_trinomial_cancel
# --------------------------------------------------------------------------- #
def _build_44_simplify_fraction_trinomial_cancel(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    p = nonzero(r, 1, 5)
    q_val = nonzero(r, -5, 5, exclude=[-p])
    num_expr = (x + p) * (x + q_val)
    den_expr = x + p
    simplified = x + q_val

    sol = solution(
        goal="simplify fraction with quadratic trinomial",
        chain_type="expression",
        var="x",
        steps=[
            step(from_expr=f"\\frac{{{to_latex(sp.expand(num_expr))}}}{{{to_latex(den_expr)}}}",
                 to_expr=f"\\frac{{(x {'+' if p >= 0 else ''} {p})(x {'+' if q_val >= 0 else ''} {q_val})}}{{{to_latex(den_expr)}}}",
                 op="factorise trinomial in numerator", rule="trinomial factorisation"),
            step(from_expr=f"\\frac{{(x {'+' if p >= 0 else ''} {p})(x {'+' if q_val >= 0 else ''} {q_val})}}{{{to_latex(den_expr)}}}",
                 to_expr=simplified,
                 op="cancel matching bracket", rule="cancellation"),
        ],
        final_expr=simplified,
    )
    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Simplify: }} \\dfrac{{{to_latex(sp.expand(num_expr))}}}{{{to_latex(den_expr)}}}",
        answer_expr=simplified,
        answer_mode="expression",
        marks=2,
        canonical_solution=sol,
        explanation=f"Factorise the numerator into $(x {'+' if p >= 0 else ''} {p})(x {'+' if q_val >= 0 else ''} {q_val})$. Cancel $(x {'+' if p >= 0 else ''} {p})$ to obtain ${to_latex(simplified)}$.",
        hint="Factorise the quadratic in the numerator, then cancel the common factor.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="44_simplify_fraction_trinomial_cancel",
        learning_objective_id=f"{LO}.44_fraction_trinomial",
        misconception_tags=["incorrect_trinomial_factors", "cancels_terms_directly"],
        diagnostic_tags=["algebraic_fractions", "trinomial"],
        keywords=["fraction", "trinomial", "cancel"],
    )
    return _add_pillars(q, "44_simplify_fraction_trinomial_cancel", duration=2, weight=15)


# --------------------------------------------------------------------------- #
# 45_simplify_fraction_sum_diff_cubes_cancel
# --------------------------------------------------------------------------- #
def _build_45_simplify_fraction_sum_diff_cubes_cancel(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    b = r.choice([1, 2, 3, 4])
    sign = r.choice(["sum", "diff"])
    if sign == "sum":
        num_expr = x**3 + b**3
        den_expr = x + b
        simplified = x**2 - b * x + b**2
    else:
        num_expr = x**3 - b**3
        den_expr = x - b
        simplified = x**2 + b * x + b**2

    sol = solution(
        goal="simplify fraction with cubes",
        chain_type="expression",
        var="x",
        steps=[
            step(from_expr=f"\\frac{{{to_latex(num_expr)}}}{{{to_latex(den_expr)}}}",
                 to_expr=f"\\frac{{{to_latex(sp.factor(num_expr))}}}{{{to_latex(den_expr)}}}",
                 op="factorise cubic numerator", rule="cubes identity"),
            step(from_expr=f"\\frac{{{to_latex(sp.factor(num_expr))}}}{{{to_latex(den_expr)}}}",
                 to_expr=simplified,
                 op="cancel linear factor", rule="cancellation"),
        ],
        final_expr=simplified,
    )
    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Simplify: }} \\dfrac{{{to_latex(num_expr)}}}{{{to_latex(den_expr)}}}",
        answer_expr=simplified,
        answer_mode="expression",
        marks=2,
        canonical_solution=sol,
        explanation=f"Factorise the numerator using the {'sum' if sign == 'sum' else 'difference'} of cubes. Cancelling $(x {'+' if sign == 'sum' else '-'} {b})$ leaves ${to_latex(simplified)}$.",
        hint="Factorise the numerator using sum/difference of cubes.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="45_simplify_fraction_sum_diff_cubes_cancel",
        learning_objective_id=f"{LO}.45_fraction_cubes",
        misconception_tags=["wrong_sign_in_trinomial_quotient", "cubes_cancelled_directly"],
        diagnostic_tags=["algebraic_fractions", "cubes"],
        keywords=["fraction", "sum of cubes", "difference of cubes"],
    )
    return _add_pillars(q, "45_simplify_fraction_sum_diff_cubes_cancel", duration=2, weight=15)


# --------------------------------------------------------------------------- #
# 46_simplify_fraction_multiplication
# --------------------------------------------------------------------------- #
def _build_46_simplify_fraction_multiplication(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    a = r.choice([2, 3, 4])
    b = r.choice([1, 2, 5])
    # (x^2 - a^2)/(x + b) * (x + b)/(x - a) = x + a
    p_num = x**2 - a**2
    p_den = x + b
    q_num = x + b
    q_den = x - a
    simplified = x + a

    sol = solution(
        goal="multiply algebraic fractions",
        chain_type="expression",
        var="x",
        steps=[
            step(from_expr=f"\\frac{{{to_latex(p_num)}}}{{{to_latex(p_den)}}} \\times \\frac{{{to_latex(q_num)}}}{{{to_latex(q_den)}}}",
                 to_expr=f"\\frac{{(x - {a})(x + {a})}}{{{to_latex(p_den)}}} \\times \\frac{{{to_latex(q_num)}}}{{x - {a}}}",
                 op="factorise all numerators and denominators", rule="factorisation"),
            step(from_expr=f"\\frac{{(x - {a})(x + {a})}}{{{to_latex(p_den)}}} \\times \\frac{{{to_latex(q_num)}}}{{x - {a}}}",
                 to_expr=simplified,
                 op="cancel all common factors", rule="multiplication"),
        ],
        final_expr=simplified,
    )
    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Simplify: }} \\dfrac{{{to_latex(p_num)}}}{{{to_latex(p_den)}}} \\times \\dfrac{{{to_latex(q_num)}}}{{{to_latex(q_den)}}}",
        answer_expr=simplified,
        answer_mode="expression",
        marks=3,
        canonical_solution=sol,
        explanation=f"Factorise $x^2 - {a**2} = (x - {a})(x + {a})$. Then cancel $(x - {a})$ and $(x + {b})$ to leave ${to_latex(simplified)}$.",
        hint="Factorise all numerators and denominators first, then cancel common factors.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="46_simplify_fraction_multiplication",
        learning_objective_id=f"{LO}.46_fraction_multiplication",
        misconception_tags=["multiplies_out_without_factorising", "cancels_across_addition"],
        diagnostic_tags=["algebraic_fractions", "multiplication"],
        keywords=["fraction multiplication", "simplify", "cancel"],
    )
    return _add_pillars(q, "46_simplify_fraction_multiplication", duration=3, weight=15)


# --------------------------------------------------------------------------- #
# 47_simplify_fraction_division
# --------------------------------------------------------------------------- #
def _build_47_simplify_fraction_division(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    a = r.choice([2, 3, 5])
    k = r.choice([2, 3, 4])
    # (x^2 - a^2)/(k*x) ÷ (x + a)/(x) = (x - a)/k
    p_num = x**2 - a**2
    p_den = k * x
    q_num = x + a
    q_den = x
    simplified = (x - a) / sp.Integer(k)

    sol = solution(
        goal="divide algebraic fractions",
        chain_type="expression",
        var="x",
        steps=[
            step(from_expr=f"\\frac{{{to_latex(p_num)}}}{{{to_latex(p_den)}}} \\div \\frac{{{to_latex(q_num)}}}{{{to_latex(q_den)}}}",
                 to_expr=f"\\frac{{{to_latex(p_num)}}}{{{to_latex(p_den)}}} \\times \\frac{{{to_latex(q_den)}}}{{{to_latex(q_num)}}}",
                 op="invert divisor and change to multiplication", rule="division of fractions"),
            step(from_expr=f"\\frac{{(x - {a})(x + {a})}}{{{k}x}} \\times \\frac{{x}}{{x + {a}}}",
                 to_expr=simplified,
                 op="factorise and cancel common terms", rule="cancellation"),
        ],
        final_expr=simplified,
    )
    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Simplify: }} \\dfrac{{{to_latex(p_num)}}}{{{to_latex(p_den)}}} \\div \\dfrac{{{to_latex(q_num)}}}{{{to_latex(q_den)}}}",
        answer_expr=simplified,
        answer_mode="expression",
        marks=3,
        canonical_solution=sol,
        explanation=f"Invert the second fraction and multiply: $\\dfrac{{(x - {a})(x + {a})}}{{{k}x}} \\times \\dfrac{{x}}{{x + {a}}} = \\dfrac{{{to_latex(x - a)}}}{{{k}}}$.",
        hint="Invert the second fraction and change the division sign to multiplication.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="47_simplify_fraction_division",
        learning_objective_id=f"{LO}.47_fraction_division",
        misconception_tags=["forgets_to_invert_divisor", "cancels_before_inverting"],
        diagnostic_tags=["algebraic_fractions", "division"],
        keywords=["fraction division", "invert and multiply", "simplify"],
    )
    return _add_pillars(q, "47_simplify_fraction_division", duration=3, weight=15)


# --------------------------------------------------------------------------- #
# 48_simplify_fraction_addition_monomial_denominators
# --------------------------------------------------------------------------- #
def _build_48_simplify_fraction_addition_monomial_denominators(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    a = r.randint(1, 5)
    b = r.randint(1, 5)
    m = r.choice([2, 3])
    n = r.choice([4, 5])
    # a/(m*x) + b/(n*x)
    lcd_coeff = math.lcm(m, n)
    res_num = a * (lcd_coeff // m) + b * (lcd_coeff // n)
    # res_num / (lcd_coeff * x)
    ans = sp.Rational(res_num, lcd_coeff) / x

    sol = solution(
        goal="add fractions with monomial denominators",
        chain_type="expression",
        var="x",
        steps=[
            step(from_expr=f"\\frac{{{a}}}{{{m}x}} + \\frac{{{b}}}{{{n}x}}",
                 to_expr=f"\\frac{{{a * (lcd_coeff // m)} + {b * (lcd_coeff // n)}}}{{{lcd_coeff}x}}",
                 op=f"find LCD = {lcd_coeff}x and express over common denominator", rule="LCD"),
            step(from_expr=f"\\frac{{{a * (lcd_coeff // m)} + {b * (lcd_coeff // n)}}}{{{lcd_coeff}x}}",
                 to_expr=ans,
                 op="simplify numerator", rule="addition"),
        ],
        final_expr=ans,
    )
    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Simplify: }} \\dfrac{{{a}}}{{{m}x}} + \\dfrac{{{b}}}{{{n}x}}",
        answer_expr=ans,
        answer_mode="expression",
        marks=2,
        canonical_solution=sol,
        explanation=f"The lowest common denominator is ${lcd_coeff}x$. Convert each term: $\\dfrac{{{a * (lcd_coeff // m)}}}{{{lcd_coeff}x}} + \\dfrac{{{b * (lcd_coeff // n)}}}{{{lcd_coeff}x}} = {to_latex(ans)}$.",
        hint=f"Find the LCD of {m}x and {n}x ({lcd_coeff}x).",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="48_simplify_fraction_addition_monomial_denominators",
        learning_objective_id=f"{LO}.48_addition_monomial_den",
        misconception_tags=["adds_denominators_directly", "incorrect_lcd"],
        diagnostic_tags=["algebraic_fractions", "addition"],
        keywords=["addition of fractions", "monomial denominators", "LCD"],
    )
    return _add_pillars(q, "48_simplify_fraction_addition_monomial_denominators", duration=2, weight=15)


# --------------------------------------------------------------------------- #
# 49_simplify_fraction_addition_binomial_denominators
# --------------------------------------------------------------------------- #
def _build_49_simplify_fraction_addition_binomial_denominators(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    a = r.randint(1, 4)
    b = r.randint(1, 4)
    p = r.randint(1, 4)
    q_val = r.randint(1, 4)
    # a/(x - p) + b/(x + q_val) = [a(x + q_val) + b(x - p)] / [(x - p)(x + q_val)]
    num_combined = sp.expand(a * (x + q_val) + b * (x - p))
    den_combined = (x - p) * (x + q_val)
    ans = num_combined / den_combined

    sol = solution(
        goal="add fractions with binomial denominators",
        chain_type="expression",
        var="x",
        steps=[
            step(from_expr=f"\\frac{{{a}}}{{x - {p}}} + \\frac{{{b}}}{{x + {q_val}}}",
                 to_expr=f"\\frac{{{a}(x + {q_val}) + {b}(x - {p})}}{{(x - {p})(x + {q_val})}}",
                 op="express over common denominator (x - p)(x + q)", rule="LCD"),
            step(from_expr=f"\\frac{{{a}(x + {q_val}) + {b}(x - {p})}}{{(x - {p})(x + {q_val})}}",
                 to_expr=ans,
                 op="expand and collect like terms in numerator", rule="simplification"),
        ],
        final_expr=ans,
    )
    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Simplify as a single fraction: }} \\dfrac{{{a}}}{{x - {p}}} + \\dfrac{{{b}}}{{x + {q_val}}}",
        answer_expr=ans,
        answer_mode="expression",
        marks=3,
        canonical_solution=sol,
        explanation=f"The LCD is $(x - {p})(x + {q_val})$. Multiplying out the numerator gives ${to_latex(num_combined)}$, so the result is $\\dfrac{{{to_latex(num_combined)}}}{{(x - {p})(x + {q_val})}}$.",
        hint="The LCD is the product of the two different denominators.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="49_simplify_fraction_addition_binomial_denominators",
        learning_objective_id=f"{LO}.49_addition_binomial_den",
        misconception_tags=["adds_denominators", "sign_error_expanding_numerator"],
        diagnostic_tags=["algebraic_fractions", "binomial_denominators"],
        keywords=["fraction addition", "binomial denominator", "single fraction"],
    )
    return _add_pillars(q, "49_simplify_fraction_addition_binomial_denominators", duration=3, weight=15)


# --------------------------------------------------------------------------- #
# 50_simplify_fraction_addition_with_factorisation_lcd
# --------------------------------------------------------------------------- #
def _build_50_simplify_fraction_addition_with_factorisation_lcd(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    b = r.choice([2, 3, 4])
    a = r.randint(1, 4)
    k = r.randint(1, 4)
    # a/(x^2 - b^2) + k/(x + b) = [a + k(x - b)] / [(x - b)(x + b)]
    num_combined = sp.expand(a + k * (x - b))
    den_combined = (x - b) * (x + b)
    ans = num_combined / den_combined

    sol = solution(
        goal="add fractions requiring factorisation to find LCD",
        chain_type="expression",
        var="x",
        steps=[
            step(from_expr=f"\\frac{{{a}}}{{x^2 - {b**2}}} + \\frac{{{k}}}{{x + {b}}}",
                 to_expr=f"\\frac{{{a}}}{{(x - {b})(x + {b})}} + \\frac{{{k}}}{{x + {b}}}",
                 op="factorise denominator into (x - b)(x + b)", rule="difference of squares"),
            step(from_expr=f"\\frac{{{a}}}{{(x - {b})(x + {b})}} + \\frac{{{k}}}{{x + {b}}}",
                 to_expr=f"\\frac{{{a} + {k}(x - {b})}}{{(x - {b})(x + {b})}}",
                 op="express over LCD (x - b)(x + b)", rule="LCD"),
            step(from_expr=f"\\frac{{{a} + {k}(x - {b})}}{{(x - {b})(x + {b})}}",
                 to_expr=ans,
                 op="expand and simplify numerator", rule="simplify"),
        ],
        final_expr=ans,
    )
    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Simplify as a single fraction: }} \\dfrac{{{a}}}{{x^2 - {b**2}}} + \\dfrac{{{k}}}{{x + {b}}}",
        answer_expr=ans,
        answer_mode="expression",
        marks=3,
        canonical_solution=sol,
        explanation=f"Factorise $x^2 - {b**2} = (x - {b})(x + {b})$. The LCD is $(x - {b})(x + {b})$. Expanding the numerator gives ${to_latex(num_combined)}$, so the result is $\\dfrac{{{to_latex(num_combined)}}}{{(x - {b})(x + {b})}}$.",
        hint="Factorise x^2 - b^2 first to find the common denominator.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="50_simplify_fraction_addition_with_factorisation_lcd",
        learning_objective_id=f"{LO}.50_factorisation_lcd",
        misconception_tags=["multiplies_both_denominators_without_factorising", "sign_error_lcd"],
        diagnostic_tags=["algebraic_fractions", "lcd_factorisation"],
        keywords=["algebraic fractions", "LCD", "factorisation", "single fraction"],
    )
    return _add_pillars(q, "50_simplify_fraction_addition_with_factorisation_lcd", duration=3, weight=15)


BUILDERS_26_50: Dict[str, Any] = {
    "26_factorise_difference_of_squares_simple": _build_26_factorise_difference_of_squares_simple,
    "27_factorise_difference_of_squares_with_coefficient": _build_27_factorise_difference_of_squares_with_coefficient,
    "28_factorise_difference_of_squares_common_factor_first": _build_28_factorise_difference_of_squares_common_factor_first,
    "29_factorise_difference_of_squares_brackets": _build_29_factorise_difference_of_squares_brackets,
    "30_factorise_grouping_two_by_two_standard": _build_30_factorise_grouping_two_by_two_standard,
    "31_factorise_grouping_with_sign_change": _build_31_factorise_grouping_with_sign_change,
    "32_factorise_grouping_three_and_one_diff_squares": _build_32_factorise_grouping_three_and_one_diff_squares,
    "33_factorise_trinomial_monic_positive_roots": _build_33_factorise_trinomial_monic_positive_roots,
    "34_factorise_trinomial_monic_mixed_signs": _build_34_factorise_trinomial_monic_mixed_signs,
    "35_factorise_trinomial_non_monic": _build_35_factorise_trinomial_non_monic,
    "36_factorise_trinomial_common_factor_first": _build_36_factorise_trinomial_common_factor_first,
    "37_factorise_trinomial_negative_leading_coeff": _build_37_factorise_trinomial_negative_leading_coeff,
    "38_factorise_sum_of_two_cubes": _build_38_factorise_sum_of_two_cubes,
    "39_factorise_difference_of_two_cubes": _build_39_factorise_difference_of_two_cubes,
    "40_factorise_sum_diff_cubes_with_common_factor": _build_40_factorise_sum_diff_cubes_with_common_factor,
    "41_simplify_fraction_monomial_over_monomial": _build_41_simplify_fraction_monomial_over_monomial,
    "42_simplify_fraction_common_factor_cancel": _build_42_simplify_fraction_common_factor_cancel,
    "43_simplify_fraction_diff_squares_cancel": _build_43_simplify_fraction_diff_squares_cancel,
    "44_simplify_fraction_trinomial_cancel": _build_44_simplify_fraction_trinomial_cancel,
    "45_simplify_fraction_sum_diff_cubes_cancel": _build_45_simplify_fraction_sum_diff_cubes_cancel,
    "46_simplify_fraction_multiplication": _build_46_simplify_fraction_multiplication,
    "47_simplify_fraction_division": _build_47_simplify_fraction_division,
    "48_simplify_fraction_addition_monomial_denominators": _build_48_simplify_fraction_addition_monomial_denominators,
    "49_simplify_fraction_addition_binomial_denominators": _build_49_simplify_fraction_addition_binomial_denominators,
    "50_simplify_fraction_addition_with_factorisation_lcd": _build_50_simplify_fraction_addition_with_factorisation_lcd,
}
