"""Grade 10 Mathematics — Term 1 — Exponents: Archetypes 26 to 50.

Ground truth: curriculum_docs/Mathematics_Gr10/Term 1/2 Exponents .md
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

TOPIC = "grade10_math_exponents"
LO = "math10_exponents"
x = sp.Symbol("x")
y = sp.Symbol("y")
n = sp.Symbol("n")


def _add_pillars(q: Dict[str, Any], subskill_name: str, duration: int = 3, weight: int = 15) -> Dict[str, Any]:
    marks = int(q.get("marks", 2))
    schema = [
        {"criterion": "Application of rational exponent / exponential equation method", "marks": max(1, marks - 1)},
        {"criterion": "Accurate final value / simplified expression", "marks": 1},
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
# 26_rational_exponent_definition_unit_fraction
# --------------------------------------------------------------------------- #
def _build_26_rational_exponent_definition_unit_fraction(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    n_val = r.choice([2, 3, 4, 5, 6])
    rad = f"\\sqrt[{n_val}]{{x}}" if n_val > 2 else "\\sqrt{x}"
    ans = x**sp.Rational(1, n_val)
    ans_latex = f"x^{{\\frac{{1}}{{{n_val}}}}}"

    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Write in exponential form: }} {rad}",
        answer_expr=ans,
        answer_mode="expression",
        answer_latex=ans_latex,
        marks=1,
        explanation=f"By the definition of rational exponents, $\\sqrt[n]{{a}} = a^{{1/n}}$. Thus ${rad} = {ans_latex}$.",
        hint="The root index becomes the denominator of the fractional exponent.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="26_rational_exponent_definition_unit_fraction",
        learning_objective_id=f"{LO}.26_unit_rational_exp",
        misconception_tags=["puts_root_in_numerator", "confuses_radical_with_division"],
        diagnostic_tags=["exponents", "rational_exponents"],
        keywords=["rational exponent", "radical form", "exponential form"],
    )
    return _add_pillars(q, "26_rational_exponent_definition_unit_fraction", duration=1, weight=15)


# --------------------------------------------------------------------------- #
# 27_rational_exponent_definition_general_fraction
# --------------------------------------------------------------------------- #
def _build_27_rational_exponent_definition_general_fraction(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    m_val = r.choice([2, 3, 4])
    n_val = r.choice([3, 5, 7])
    if m_val == n_val:
        n_val = m_val + 1
    rad = f"\\sqrt[{n_val}]{{x^{{{m_val}}}}}"
    ans_latex = f"x^{{\\frac{{{m_val}}}{{{n_val}}}}}"
    ans = x**sp.Rational(m_val, n_val)

    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Write in exponential form: }} {rad}",
        answer_expr=ans,
        answer_mode="expression",
        answer_latex=ans_latex,
        marks=1,
        explanation=f"Use the general law $\\sqrt[n]{{a^m}} = a^{{m/n}}$: the power is the numerator and the root is the denominator, giving ${ans_latex}$.",
        hint="Remember: power over root (m/n).",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="27_rational_exponent_definition_general_fraction",
        learning_objective_id=f"{LO}.27_general_rational_exp",
        misconception_tags=["inverts_power_and_root", "drops_root_index"],
        diagnostic_tags=["exponents", "rational_exponents"],
        keywords=["rational exponent", "power over root"],
    )
    return _add_pillars(q, "27_rational_exponent_definition_general_fraction", duration=1, weight=15)


# --------------------------------------------------------------------------- #
# 28_evaluate_numeric_power_unit_fraction_exponent
# --------------------------------------------------------------------------- #
def _build_28_evaluate_numeric_power_unit_fraction_exponent(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    triples = [
        (4, 2, 2), (9, 2, 3), (16, 2, 4), (25, 2, 5), (36, 2, 6), (49, 2, 7), (64, 2, 8),
        (8, 3, 2), (27, 3, 3), (64, 3, 4), (125, 3, 5),
        (16, 4, 2), (81, 4, 3),
        (32, 5, 2),
    ]
    base_val, denom_exp, result = r.choice(triples)
    prompt = f"{base_val}^{{\\frac{{1}}{{{denom_exp}}}}}"

    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Evaluate without a calculator: }} {prompt}",
        answer_expr=sp.Integer(result),
        answer_mode="value",
        answer_latex=str(result),
        marks=1,
        explanation=f"${base_val}^{{1/{denom_exp}}} = \\sqrt[{denom_exp}]{{{base_val}}} = {result}$ because ${result}^{{{denom_exp}}} = {base_val}$.",
        hint=f"Rewrite {base_val} as {result}^{denom_exp}.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="28_evaluate_numeric_power_unit_fraction_exponent",
        learning_objective_id=f"{LO}.28_eval_unit_fraction",
        misconception_tags=["multiplies_base_by_fraction", "confuses_cube_and_square_root"],
        diagnostic_tags=["exponents", "evaluating_roots"],
        keywords=["evaluate", "rational exponent", "roots"],
    )
    return _add_pillars(q, "28_evaluate_numeric_power_unit_fraction_exponent", duration=1, weight=15)


# --------------------------------------------------------------------------- #
# 29_evaluate_numeric_power_non_unit_rational_exponent
# --------------------------------------------------------------------------- #
def _build_29_evaluate_numeric_power_non_unit_rational_exponent(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    cases = [
        (8, 2, 3, 4, "8^{2/3} = (2^3)^{2/3} = 2^2 = 4"),
        (27, 2, 3, 9, "27^{2/3} = (3^3)^{2/3} = 3^2 = 9"),
        (16, 3, 4, 8, "16^{3/4} = (2^4)^{3/4} = 2^3 = 8"),
        (32, 2, 5, 4, "32^{2/5} = (2^5)^{2/5} = 2^2 = 4"),
        (32, 3, 5, 8, "32^{3/5} = (2^5)^{3/5} = 2^3 = 8"),
        (25, 3, 2, 125, "25^{3/2} = (5^2)^{3/2} = 5^3 = 125"),
        (4, 3, 2, 8, "4^{3/2} = (2^2)^{3/2} = 2^3 = 8"),
        (81, 3, 4, 27, "81^{3/4} = (3^4)^{3/4} = 3^3 = 27"),
    ]
    b, m_val, n_val, ans_val, expl_str = r.choice(cases)
    prompt = f"{b}^{{\\frac{{{m_val}}}{{{n_val}}}}}"

    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Evaluate without a calculator: }} {prompt}",
        answer_expr=sp.Integer(ans_val),
        answer_mode="value",
        answer_latex=str(ans_val),
        marks=2,
        explanation=f"Rewrite the base as a prime power: {expl_str}.",
        hint="Express the base as a power of a prime, then multiply the exponents.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="29_evaluate_numeric_power_non_unit_rational_exponent",
        learning_objective_id=f"{LO}.29_eval_non_unit_rational",
        misconception_tags=["calculates_power_before_root_making_large_numbers", "fraction_arithmetic_error"],
        diagnostic_tags=["exponents", "rational_powers"],
        keywords=["evaluate", "fractional exponent", "no calculator"],
    )
    return _add_pillars(q, "29_evaluate_numeric_power_non_unit_rational_exponent", duration=2, weight=15)


# --------------------------------------------------------------------------- #
# 30_evaluate_numeric_power_negative_rational_exponent
# --------------------------------------------------------------------------- #
def _build_30_evaluate_numeric_power_negative_rational_exponent(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    cases = [
        (8, 2, 3, 1, 4, "8^{-2/3} = 1 / 8^{2/3} = 1 / 4"),
        (27, 2, 3, 1, 9, "27^{-2/3} = 1 / 27^{2/3} = 1 / 9"),
        (16, 3, 4, 1, 8, "16^{-3/4} = 1 / 16^{3/4} = 1 / 8"),
        (4, 3, 2, 1, 8, "4^{-3/2} = 1 / 4^{3/2} = 1 / 8"),
        (25, 3, 2, 1, 125, "25^{-3/2} = 1 / 25^{3/2} = 1 / 125"),
    ]
    b, m_val, n_val, num_res, den_res, expl = r.choice(cases)
    prompt = f"{b}^{{-\\frac{{{m_val}}}{{{n_val}}}}}"
    ans_frac = sp.Rational(num_res, den_res)
    ans_latex = f"\\frac{{{num_res}}}{{{den_res}}}"

    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Evaluate: }} {prompt}",
        answer_expr=ans_frac,
        answer_mode="expression",
        answer_latex=ans_latex,
        marks=2,
        explanation=f"First apply $a^{{-n}} = 1/a^n$, then evaluate the rational exponent: {expl}.",
        hint="Invert the base to make the exponent positive, then take the root and raise to the power.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="30_evaluate_numeric_power_negative_rational_exponent",
        learning_objective_id=f"{LO}.30_eval_negative_rational",
        misconception_tags=["negative_sign_on_result", "forgets_to_invert"],
        diagnostic_tags=["exponents", "negative_rational_powers"],
        keywords=["negative rational exponent", "evaluate", "reciprocal"],
    )
    return _add_pillars(q, "30_evaluate_numeric_power_negative_rational_exponent", duration=2, weight=15)


# --------------------------------------------------------------------------- #
# 31_simplify_algebraic_expression_rational_exponents
# --------------------------------------------------------------------------- #
def _build_31_simplify_algebraic_expression_rational_exponents(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    # e.g. (x^(1/2) * y^(2/3))^6 = x^3 * y^4
    p = r.choice([2, 3])
    q_val = r.choice([2, 3])
    outer = r.choice([6, 12])
    exp_x = outer // 2
    exp_y = (outer * 2) // 3
    ans = x**exp_x * y**exp_y

    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Simplify: }} \\left(x^{{\\frac{{1}}{{2}}}} y^{{\\frac{{2}}{{3}}}}\\right)^{{{outer}}}",
        answer_expr=ans,
        answer_mode="expression",
        marks=2,
        explanation=f"Multiply each fractional exponent by the outer power {outer}: $\\frac{{1}}{{2}} \\times {outer} = {exp_x}$ and $\\frac{{2}}{{3}} \\times {outer} = {exp_y}$, giving ${to_latex(ans)}$.",
        hint="Multiply the outside power by each inside fractional exponent.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="31_simplify_algebraic_expression_rational_exponents",
        learning_objective_id=f"{LO}.31_alg_rational_simplify",
        misconception_tags=["adds_outer_power_instead_of_multiplying", "error_multiplying_fractions"],
        diagnostic_tags=["exponents", "algebraic_rational_powers"],
        keywords=["rational exponents", "algebraic", "simplify"],
    )
    return _add_pillars(q, "31_simplify_algebraic_expression_rational_exponents", duration=2, weight=15)


# --------------------------------------------------------------------------- #
# 32_multiply_powers_with_fractional_exponents
# --------------------------------------------------------------------------- #
def _build_32_multiply_powers_with_fractional_exponents(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    # x^(1/2) * x^(1/3) = x^(5/6)
    # x^(1/4) * x^(1/2) = x^(3/4)
    # x^(2/3) * x^(1/6) = x^(5/6)
    pairs = [
        (sp.Rational(1, 2), sp.Rational(1, 3), sp.Rational(5, 6), "\\frac{1}{2}", "\\frac{1}{3}", "\\frac{5}{6}"),
        (sp.Rational(1, 4), sp.Rational(1, 2), sp.Rational(3, 4), "\\frac{1}{4}", "\\frac{1}{2}", "\\frac{3}{4}"),
        (sp.Rational(2, 3), sp.Rational(1, 6), sp.Rational(5, 6), "\\frac{2}{3}", "\\frac{1}{6}", "\\frac{5}{6}"),
        (sp.Rational(3, 4), sp.Rational(1, 2), sp.Rational(5, 4), "\\frac{3}{4}", "\\frac{1}{2}", "\\frac{5}{4}"),
    ]
    f1, f2, f_sum, f1_l, f2_l, f_sum_l = r.choice(pairs)
    ans = x**f_sum
    ans_latex = f"x^{{{f_sum_l}}}"

    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Simplify: }} x^{{{f1_l}}} \\cdot x^{{{f2_l}}}",
        answer_expr=ans,
        answer_mode="expression",
        answer_latex=ans_latex,
        marks=2,
        explanation=f"Keep the base and add the fractional exponents: ${f1_l} + {f2_l} = {f_sum_l}$, giving ${ans_latex}$.",
        hint="Add the fractional exponents using a common denominator.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="32_multiply_powers_with_fractional_exponents",
        learning_objective_id=f"{LO}.32_multiply_fractional_powers",
        misconception_tags=["multiplies_fractions_instead_of_adding", "denominator_addition_error"],
        diagnostic_tags=["exponents", "adding_fractional_powers"],
        keywords=["product rule", "fractional exponents", "add fractions"],
    )
    return _add_pillars(q, "32_multiply_powers_with_fractional_exponents", duration=2, weight=15)


# --------------------------------------------------------------------------- #
# 33_quotient_powers_with_fractional_exponents
# --------------------------------------------------------------------------- #
def _build_33_quotient_powers_with_fractional_exponents(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    cases = [
        (sp.Rational(3, 4), sp.Rational(1, 2), sp.Rational(1, 4), "\\frac{3}{4}", "\\frac{1}{2}", "\\frac{1}{4}"),
        (sp.Rational(5, 6), sp.Rational(1, 3), sp.Rational(1, 2), "\\frac{5}{6}", "\\frac{1}{3}", "\\frac{1}{2}"),
        (sp.Rational(2, 3), sp.Rational(1, 6), sp.Rational(1, 2), "\\frac{2}{3}", "\\frac{1}{6}", "\\frac{1}{2}"),
        (sp.Rational(7, 4), sp.Rational(3, 4), sp.Integer(1), "\\frac{7}{4}", "\\frac{3}{4}", "1"),
    ]
    f1, f2, f_diff, f1_l, f2_l, f_diff_l = r.choice(cases)
    ans = x if f_diff == 1 else x**f_diff
    ans_latex = "x" if f_diff == 1 else f"x^{{{f_diff_l}}}"

    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Simplify: }} \\dfrac{{x^{{{f1_l}}}}}{{x^{{{f2_l}}}}}",
        answer_expr=ans,
        answer_mode="expression",
        answer_latex=ans_latex,
        marks=2,
        explanation=f"Subtract the exponents: ${f1_l} - {f2_l} = {f_diff_l}$, giving ${ans_latex}$.",
        hint="Subtract the bottom fractional exponent from the top fractional exponent.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="33_quotient_powers_with_fractional_exponents",
        learning_objective_id=f"{LO}.33_quotient_fractional_powers",
        misconception_tags=["divides_fractional_exponents", "subtraction_error_on_fractions"],
        diagnostic_tags=["exponents", "subtracting_fractional_powers"],
        keywords=["quotient rule", "fractional exponents", "subtract"],
    )
    return _add_pillars(q, "33_quotient_powers_with_fractional_exponents", duration=2, weight=15)


# --------------------------------------------------------------------------- #
# 34_power_of_power_fractional_exponents
# --------------------------------------------------------------------------- #
def _build_34_power_of_power_fractional_exponents(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    cases = [
        (sp.Rational(2, 3), sp.Rational(3, 4), sp.Rational(1, 2), "\\frac{2}{3}", "\\frac{3}{4}", "\\frac{1}{2}"),
        (sp.Rational(3, 5), sp.Rational(5, 6), sp.Rational(1, 2), "\\frac{3}{5}", "\\frac{5}{6}", "\\frac{1}{2}"),
        (sp.Rational(4, 3), sp.Rational(3, 2), sp.Integer(2), "\\frac{4}{3}", "\\frac{3}{2}", "2"),
    ]
    f1, f2, f_prod, f1_l, f2_l, f_prod_l = r.choice(cases)
    ans = x**f_prod
    ans_latex = f"x^{{{f_prod_l}}}" if f_prod != 1 else "x"

    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Simplify: }} \\left(x^{{{f1_l}}}\\right)^{{{f2_l}}}",
        answer_expr=ans,
        answer_mode="expression",
        answer_latex=ans_latex,
        marks=2,
        explanation=f"Multiply the two fractional exponents: ${f1_l} \\times {f2_l} = {f_prod_l}$, giving ${ans_latex}$.",
        hint="Multiply the inner fractional exponent by the outer fractional exponent.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="34_power_of_power_fractional_exponents",
        learning_objective_id=f"{LO}.34_power_of_power_fractional",
        misconception_tags=["adds_exponents_instead_of_multiplying", "fraction_multiplication_error"],
        diagnostic_tags=["exponents", "power_of_power_fractions"],
        keywords=["power of a power", "fractional exponents", "multiply"],
    )
    return _add_pillars(q, "34_power_of_power_fractional_exponents", duration=2, weight=15)


# --------------------------------------------------------------------------- #
# 35_radical_algebraic_simplification
# --------------------------------------------------------------------------- #
def _build_35_radical_algebraic_simplification(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    c = r.choice([2, 3, 4, 5])
    c_sq = c**2
    p = r.choice([2, 4, 6])
    q_exp = r.choice([2, 4, 6])
    ans = c * x**(p // 2) * y**(q_exp // 2)

    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Simplify assuming all variables are positive: }} \\sqrt{{{c_sq}x^{{{p}}} y^{{{q_exp}}}}}",
        answer_expr=ans,
        answer_mode="expression",
        marks=2,
        explanation=f"Take the square root of the coefficient ($\\sqrt{{{c_sq}}} = {c}$) and divide the exponents of the variables by 2: ${to_latex(ans)}$.",
        hint="Square root of a power means divide the exponent by 2.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="35_radical_algebraic_simplification",
        learning_objective_id=f"{LO}.35_radical_algebraic",
        misconception_tags=["takes_square_root_of_exponents_instead_of_halving", "leaves_radical"],
        diagnostic_tags=["radicals", "simplifying_roots"],
        keywords=["radical", "square root", "powers"],
    )
    return _add_pillars(q, "35_radical_algebraic_simplification", duration=2, weight=15)


# --------------------------------------------------------------------------- #
# 36_exponential_equation_simple_integer_power
# --------------------------------------------------------------------------- #
def _build_36_exponential_equation_simple_integer_power(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    b = r.choice([2, 3, 5])
    p = r.randint(2, 5) if b == 2 else r.randint(2, 4)
    rhs = b**p

    sol = solution(
        goal="solve simple exponential equation",
        chain_type="equation",
        var="x",
        steps=[
            step(from_expr=f"{b}^x = {rhs}", to_expr=f"{b}^x = {b}^{{{p}}}", op=f"express {rhs} as a power of base {b}", rule="prime base"),
            step(from_expr=f"{b}^x = {b}^{{{p}}}", to_expr=f"x = {p}", op="equate exponents", rule="one-to-one exponential property"),
        ],
        final_expr=sp.Integer(p),
    )
    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Solve for }} x: {b}^x = {rhs}",
        answer_expr=sp.Integer(p),
        answer_mode="value",
        answer_latex=str(p),
        marks=2,
        canonical_solution=sol,
        explanation=f"Express ${rhs} = {b}^{{{p}}}$. Since the bases are equal, $x = {p}$.",
        hint=f"Rewrite {rhs} as a power of {b}.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="36_exponential_equation_simple_integer_power",
        learning_objective_id=f"{LO}.36_exp_eq_simple",
        misconception_tags=["divides_rhs_by_base", "multiplies_base_by_x"],
        diagnostic_tags=["exponential_equations", "equating_bases"],
        keywords=["exponential equation", "equate bases", "solve for x"],
    )
    return _add_pillars(q, "36_exponential_equation_simple_integer_power", duration=2, weight=15)


# --------------------------------------------------------------------------- #
# 37_exponential_equation_linear_exponent
# --------------------------------------------------------------------------- #
def _build_37_exponential_equation_linear_exponent(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    b = r.choice([2, 3, 5])
    a_lin = r.choice([1, 2])
    c_lin = nonzero(r, -4, 4)
    x_val = r.randint(1, 4)
    rhs_power = a_lin * x_val + c_lin
    while rhs_power <= 0:
        x_val += 1
        rhs_power = a_lin * x_val + c_lin
    rhs = b**rhs_power

    sol = solution(
        goal="solve exponential equation with linear exponent",
        chain_type="equation",
        var="x",
        steps=[
            step(from_expr=f"{b}^{{{a_lin}x {'+' if c_lin >= 0 else ''} {c_lin}}} = {rhs}",
                 to_expr=f"{b}^{{{a_lin}x {'+' if c_lin >= 0 else ''} {c_lin}}} = {b}^{{{rhs_power}}}",
                 op=f"express {rhs} as {b}^{{{rhs_power}}}", rule="prime bases"),
            step(from_expr=f"{a_lin}x {'+' if c_lin >= 0 else ''} {c_lin} = {rhs_power}",
                 to_expr=f"x = {x_val}",
                 op="equate exponents and solve linear equation", rule="linear equation"),
        ],
        final_expr=sp.Integer(x_val),
    )
    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Solve for }} x: {b}^{{{a_lin}x {'+' if c_lin >= 0 else ''} {c_lin}}} = {rhs}",
        answer_expr=sp.Integer(x_val),
        answer_mode="value",
        answer_latex=str(x_val),
        marks=2,
        canonical_solution=sol,
        explanation=f"Rewrite ${rhs} = {b}^{{{rhs_power}}}$. Equate exponents: ${a_lin}x {'+' if c_lin >= 0 else ''} {c_lin} = {rhs_power} \\implies x = {x_val}$.",
        hint="Get the same base on both sides, then equate the exponents and solve for x.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="37_exponential_equation_linear_exponent",
        learning_objective_id=f"{LO}.37_exp_eq_linear",
        misconception_tags=["sign_error_solving_linear_exponent", "fails_to_equate_exponents"],
        diagnostic_tags=["exponential_equations", "linear_exponents"],
        keywords=["exponential equation", "linear exponent", "equate"],
    )
    return _add_pillars(q, "37_exponential_equation_linear_exponent", duration=2, weight=15)


# --------------------------------------------------------------------------- #
# 38_exponential_equation_negative_result
# --------------------------------------------------------------------------- #
def _build_38_exponential_equation_negative_result(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    b = r.choice([2, 3, 5])
    p = r.choice([2, 3, 4] if b == 2 else [2, 3])
    rhs_den = b**p
    ans_val = -p

    sol = solution(
        goal="solve exponential equation with fractional right hand side",
        chain_type="equation",
        var="x",
        steps=[
            step(from_expr=f"{b}^x = \\frac{{1}}{{{rhs_den}}}",
                 to_expr=f"{b}^x = \\frac{{1}}{{{b}^{{{p}}}}} = {b}^{{-{p}}}",
                 op="rewrite fraction using negative exponent", rule="a^-n = 1/a^n"),
            step(from_expr=f"{b}^x = {b}^{{-{p}}}", to_expr=f"x = -{p}", op="equate exponents", rule="equating bases"),
        ],
        final_expr=sp.Integer(ans_val),
    )
    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Solve for }} x: {b}^x = \\dfrac{{1}}{{{rhs_den}}}",
        answer_expr=sp.Integer(ans_val),
        answer_mode="value",
        answer_latex=str(ans_val),
        marks=2,
        canonical_solution=sol,
        explanation=f"Rewrite $\\dfrac{{1}}{{{rhs_den}}} = \\dfrac{{1}}{{{b}^{{{p}}}}} = {b}^{{-{p}}}$. Equating exponents gives $x = -{p}$.",
        hint="Write the fraction with a negative exponent: 1/b^n = b^-n.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="38_exponential_equation_negative_result",
        learning_objective_id=f"{LO}.38_exp_eq_neg_result",
        misconception_tags=["forgets_negative_sign", "treats_fraction_as_positive_exponent"],
        diagnostic_tags=["exponential_equations", "negative_exponents"],
        keywords=["fraction rhs", "negative exponent", "solve"],
    )
    return _add_pillars(q, "38_exponential_equation_negative_result", duration=2, weight=15)


# --------------------------------------------------------------------------- #
# 39_exponential_equation_composite_base_both_sides
# --------------------------------------------------------------------------- #
def _build_39_exponential_equation_composite_base_both_sides(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    # e.g. 4^(x - 1) = 8 -> 2^(2x - 2) = 2^3 -> 2x - 2 = 3 -> 2x = 5 -> x = 5/2
    k = r.randint(1, 3)
    # 4^(x + k) = 8 -> 2^(2x + 2k) = 2^3 -> 2x + 2k = 3 -> 2x = 3 - 2k -> x = (3 - 2k)/2
    ans_num = 3 - 2 * k
    ans_val = sp.Rational(ans_num, 2)
    ans_latex = f"\\frac{{{ans_num}}}{{2}}" if ans_num % 2 != 0 else str(ans_num // 2)

    sol = solution(
        goal="solve exponential equation with composite base on both sides",
        chain_type="equation",
        var="x",
        steps=[
            step(from_expr=f"4^{{x {'+' if k >= 0 else ''} {k}}} = 8",
                 to_expr=f"(2^2)^{{x {'+' if k >= 0 else ''} {k}}} = 2^3",
                 op="convert bases 4 and 8 to base 2", rule="prime bases"),
            step(from_expr=f"2^{{2x + {2*k}}} = 2^3",
                 to_expr=f"2x + {2*k} = 3 \\implies x = {ans_latex}",
                 op="equate exponents and solve for x", rule="linear equation"),
        ],
        final_expr=ans_val,
    )
    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Solve for }} x: 4^{{x {'+' if k >= 0 else ''} {k}}} = 8",
        answer_expr=ans_val,
        answer_mode="expression",
        answer_latex=ans_latex,
        marks=3,
        canonical_solution=sol,
        explanation=f"Rewrite $4 = 2^2$ and $8 = 2^3$. So $2^{{2x + {2*k}}} = 2^3 \\implies 2x + {2*k} = 3 \\implies x = {ans_latex}$.",
        hint="Express both 4 and 8 as powers of 2.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="39_exponential_equation_composite_base_both_sides",
        learning_objective_id=f"{LO}.39_exp_eq_composite_bases",
        misconception_tags=["forgets_to_distribute_power_to_both_terms", "confuses_power_multiplication"],
        diagnostic_tags=["exponential_equations", "composite_bases"],
        keywords=["composite base", "base 2", "solve"],
    )
    return _add_pillars(q, "39_exponential_equation_composite_base_both_sides", duration=3, weight=15)


# --------------------------------------------------------------------------- #
# 40_exponential_equation_composite_powers
# --------------------------------------------------------------------------- #
def _build_40_exponential_equation_composite_powers(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    # e.g. 9^(x + 1) = 27^(x - 1)
    # (3^2)^(x + 1) = (3^3)^(x - 1)
    # 2x + 2 = 3x - 3 -> x = 5
    a_shift = r.randint(1, 3)
    b_shift = r.randint(1, 3)
    # 2(x + a_shift) = 3(x - b_shift) -> 2x + 2*a_shift = 3x - 3*b_shift -> x = 2*a_shift + 3*b_shift
    ans_val = 2 * a_shift + 3 * b_shift

    sol = solution(
        goal="solve equation with composite powers on both sides",
        chain_type="equation",
        var="x",
        steps=[
            step(from_expr=f"9^{{x + {a_shift}}} = 27^{{x - {b_shift}}}",
                 to_expr=f"(3^2)^{{x + {a_shift}}} = (3^3)^{{x - {b_shift}}}",
                 op="convert 9 and 27 to base 3", rule="prime bases"),
            step(from_expr=f"3^{{2x + {2*a_shift}}} = 3^{{3x - {3*b_shift}}}",
                 to_expr=f"2x + {2*a_shift} = 3x - {3*b_shift} \\implies x = {ans_val}",
                 op="equate exponents and solve for x", rule="linear equation"),
        ],
        final_expr=sp.Integer(ans_val),
    )
    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Solve for }} x: 9^{{x + {a_shift}}} = 27^{{x - {b_shift}}}",
        answer_expr=sp.Integer(ans_val),
        answer_mode="value",
        answer_latex=str(ans_val),
        marks=3,
        canonical_solution=sol,
        explanation=f"Rewrite $9 = 3^2$ and $27 = 3^3$: $3^{{2(x + {a_shift})}} = 3^{{3(x - {b_shift})}} \\implies 2x + {2*a_shift} = 3x - {3*b_shift} \\implies x = {ans_val}$.",
        hint="Express both 9 and 27 as powers of 3, distribute the powers, and equate.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="40_exponential_equation_composite_powers",
        learning_objective_id=f"{LO}.40_exp_eq_composite_powers",
        misconception_tags=["distributive_law_error_in_exponents", "equating_bases_error"],
        diagnostic_tags=["exponential_equations", "powers_of_3"],
        keywords=["composite powers", "base 3", "distribute exponent"],
    )
    return _add_pillars(q, "40_exponential_equation_composite_powers", duration=3, weight=15)


# --------------------------------------------------------------------------- #
# 41_exponential_equation_fractional_base
# --------------------------------------------------------------------------- #
def _build_41_exponential_equation_fractional_base(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    b = r.choice([2, 3, 5])
    p = r.choice([2, 3, 4] if b == 2 else [2, 3])
    rhs = b**p
    ans_val = -p

    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Solve for }} x: \\left(\\dfrac{{1}}{{{b}}}\\right)^x = {rhs}",
        answer_expr=sp.Integer(ans_val),
        answer_mode="value",
        answer_latex=str(ans_val),
        marks=2,
        explanation=f"Rewrite $(1/{b})^x = ({b}^{{-1}})^x = {b}^{{-x}}$. Since ${rhs} = {b}^{{{p}}}$, $-x = {p} \\implies x = -{p}$.",
        hint="Express (1/b)^x as b^-x, and the RHS as a power of b.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="41_exponential_equation_fractional_base",
        learning_objective_id=f"{LO}.41_exp_eq_fractional_base",
        misconception_tags=["loses_negative_sign_on_x", "inverts_rhs_wrongly"],
        diagnostic_tags=["exponential_equations", "fractional_bases"],
        keywords=["fractional base", "negative exponent", "solve"],
    )
    return _add_pillars(q, "41_exponential_equation_fractional_base", duration=2, weight=15)


# --------------------------------------------------------------------------- #
# 42_exponential_equation_zero_exponent_property
# --------------------------------------------------------------------------- #
def _build_42_exponential_equation_zero_exponent_property(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    b = r.choice([2, 3, 5, 7])
    a_coeff = r.choice([1, 2, 3])
    c_val = r.randint(1, 6)
    # b^(a*x - c) = 1 -> a*x - c = 0 -> x = c/a
    while c_val % a_coeff != 0:
        c_val = r.randint(1, 6)
    ans_val = c_val // a_coeff

    sol = solution(
        goal="solve equation equal to 1 using zero exponent rule",
        chain_type="equation",
        var="x",
        steps=[
            step(from_expr=f"{b}^{{{a_coeff}x - {c_val}}} = 1",
                 to_expr=f"{b}^{{{a_coeff}x - {c_val}}} = {b}^0",
                 op="rewrite 1 as b^0", rule="zero exponent property"),
            step(from_expr=f"{a_coeff}x - {c_val} = 0",
                 to_expr=f"x = {ans_val}",
                 op="equate exponent to 0 and solve", rule="linear equation"),
        ],
        final_expr=sp.Integer(ans_val),
    )
    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Solve for }} x: {b}^{{{a_coeff}x - {c_val}}} = 1",
        answer_expr=sp.Integer(ans_val),
        answer_mode="value",
        answer_latex=str(ans_val),
        marks=2,
        canonical_solution=sol,
        explanation=f"Any non-zero base raised to the power 0 equals 1: ${b}^{{{a_coeff}x - {c_val}}} = {b}^0 \\implies {a_coeff}x - {c_val} = 0 \\implies x = {ans_val}$.",
        hint="Remember that 1 can be rewritten as any base raised to the power 0.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="42_exponential_equation_zero_exponent_property",
        learning_objective_id=f"{LO}.42_exp_eq_zero_property",
        misconception_tags=["sets_exponent_to_one", "divides_by_base_getting_zero"],
        diagnostic_tags=["exponential_equations", "zero_exponent"],
        keywords=["equals 1", "zero power", "solve"],
    )
    return _add_pillars(q, "42_exponential_equation_zero_exponent_property", duration=2, weight=15)


# --------------------------------------------------------------------------- #
# 43_exponential_equation_coefficient_division
# --------------------------------------------------------------------------- #
def _build_43_exponential_equation_coefficient_division(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    c = r.choice([2, 3, 5, 7])
    b = r.choice([2, 3])
    p = r.randint(2, 4)
    rhs = c * (b**p)

    sol = solution(
        goal="solve equation with leading coefficient",
        chain_type="equation",
        var="x",
        steps=[
            step(from_expr=f"{c} \\cdot {b}^x = {rhs}",
                 to_expr=f"{b}^x = {rhs // c}",
                 op=f"divide both sides by {c}", rule="isolate exponential term"),
            step(from_expr=f"{b}^x = {b**p}",
                 to_expr=f"x = {p}",
                 op=f"equate exponents with {rhs // c} = {b}^{{{p}}}", rule="equating bases"),
        ],
        final_expr=sp.Integer(p),
    )
    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Solve for }} x: {c} \\cdot {b}^x = {rhs}",
        answer_expr=sp.Integer(p),
        answer_mode="value",
        answer_latex=str(p),
        marks=2,
        canonical_solution=sol,
        explanation=f"First divide both sides by ${c}$: ${b}^x = {rhs // c} = {b}^{{{p}}} \\implies x = {p}$.",
        hint=f"Isolate the power of {b} first by dividing both sides by {c}.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="43_exponential_equation_coefficient_division",
        learning_objective_id=f"{LO}.43_exp_eq_coeff_div",
        misconception_tags=["multiplies_coefficient_into_base", "forgets_to_divide_coefficient"],
        diagnostic_tags=["exponential_equations", "coefficients"],
        keywords=["isolate power", "divide coefficient", "solve"],
    )
    return _add_pillars(q, "43_exponential_equation_coefficient_division", duration=2, weight=15)


# --------------------------------------------------------------------------- #
# 44_exponential_equation_common_factor_addition
# --------------------------------------------------------------------------- #
def _build_44_exponential_equation_common_factor_addition(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    # e.g. 2^(x+1) + 2^x = 24 -> 2^x(2 + 1) = 24 -> 2^x * 3 = 24 -> 2^x = 8 -> x = 3
    base_val = r.choice([2, 3])
    p_exp = r.choice([1, 2])
    bracket = base_val**p_exp + 1
    x_val = r.randint(2, 4)
    rhs = (base_val**x_val) * bracket

    sol = solution(
        goal="solve exponential equation by factoring common power",
        chain_type="equation",
        var="x",
        steps=[
            step(from_expr=f"{base_val}^{{x + {p_exp}}} + {base_val}^x = {rhs}",
                 to_expr=f"{base_val}^x({base_val}^{{{p_exp}}} + 1) = {rhs}",
                 op=f"factor out {base_val}^x", rule="common factor"),
            step(from_expr=f"{base_val}^x({bracket}) = {rhs}",
                 to_expr=f"{base_val}^x = {base_val**x_val}",
                 op=f"divide by {bracket}", rule="isolate power"),
            step(from_expr=f"{base_val}^x = {base_val**x_val}", to_expr=f"x = {x_val}", op="equate exponents", rule="solve for x"),
        ],
        final_expr=sp.Integer(x_val),
    )
    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Solve for }} x: {base_val}^{{x + {p_exp}}} + {base_val}^x = {rhs}",
        answer_expr=sp.Integer(x_val),
        answer_mode="value",
        answer_latex=str(x_val),
        marks=3,
        canonical_solution=sol,
        explanation=f"Factorise ${base_val}^x$ out: ${base_val}^x({base_val**p_exp} + 1) = {rhs} \\implies {base_val}^x({bracket}) = {rhs} \\implies {base_val}^x = {base_val**x_val} \\implies x = {x_val}$.",
        hint=f"Take out {base_val}^x as a common factor on the left hand side.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="44_exponential_equation_common_factor_addition",
        learning_objective_id=f"{LO}.44_exp_eq_common_factor_add",
        misconception_tags=["adds_bases_together", "attempts_to_solve_without_factoring"],
        diagnostic_tags=["exponential_equations", "common_factor_equations"],
        keywords=["common factor", "exponential equation", "addition"],
    )
    return _add_pillars(q, "44_exponential_equation_common_factor_addition", duration=3, weight=15)


# --------------------------------------------------------------------------- #
# 45_exponential_equation_common_factor_subtraction
# --------------------------------------------------------------------------- #
def _build_45_exponential_equation_common_factor_subtraction(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    # e.g. 3^(x+1) - 3^x = 18 -> 3^x(3 - 1) = 18 -> 3^x * 2 = 18 -> 3^x = 9 -> x = 2
    base_val = r.choice([2, 3])
    p_exp = r.choice([1, 2])
    bracket = base_val**p_exp - 1
    x_val = r.randint(2, 4)
    rhs = (base_val**x_val) * bracket

    sol = solution(
        goal="solve exponential equation with subtraction by factoring",
        chain_type="equation",
        var="x",
        steps=[
            step(from_expr=f"{base_val}^{{x + {p_exp}}} - {base_val}^x = {rhs}",
                 to_expr=f"{base_val}^x({base_val}^{{{p_exp}}} - 1) = {rhs}",
                 op=f"factor out {base_val}^x", rule="common factor"),
            step(from_expr=f"{base_val}^x({bracket}) = {rhs}",
                 to_expr=f"{base_val}^x = {base_val**x_val}",
                 op=f"divide by {bracket}", rule="isolate power"),
            step(from_expr=f"{base_val}^x = {base_val**x_val}", to_expr=f"x = {x_val}", op="equate exponents", rule="solve for x"),
        ],
        final_expr=sp.Integer(x_val),
    )
    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Solve for }} x: {base_val}^{{x + {p_exp}}} - {base_val}^x = {rhs}",
        answer_expr=sp.Integer(x_val),
        answer_mode="value",
        answer_latex=str(x_val),
        marks=3,
        canonical_solution=sol,
        explanation=f"Factorise ${base_val}^x$ out: ${base_val}^x({bracket}) = {rhs} \\implies {base_val}^x = {base_val**x_val} \\implies x = {x_val}$.",
        hint=f"Take out {base_val}^x as a common factor.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="45_exponential_equation_common_factor_subtraction",
        learning_objective_id=f"{LO}.45_exp_eq_common_factor_sub",
        misconception_tags=["subtracts_bases", "sign_error_in_common_bracket"],
        diagnostic_tags=["exponential_equations", "subtraction_equations"],
        keywords=["subtraction", "common factor", "exponential equation"],
    )
    return _add_pillars(q, "45_exponential_equation_common_factor_subtraction", duration=3, weight=15)


# --------------------------------------------------------------------------- #
# 46_exponential_equation_common_factor_negative_shift
# --------------------------------------------------------------------------- #
def _build_46_exponential_equation_common_factor_negative_shift(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    # e.g. 2^x + 2^(x-1) = 12 -> 2^x(1 + 1/2) = 12 -> 2^x(3/2) = 12 -> 2^x = 8 -> x = 3
    base_val = 2
    x_val = r.randint(2, 5)
    # 2^x * (1 + 1/2) = 2^x * 3/2
    rhs = (2**x_val * 3) // 2

    sol = solution(
        goal="solve equation with negative shift in exponent",
        chain_type="equation",
        var="x",
        steps=[
            step(from_expr=f"2^x + 2^{{x - 1}} = {rhs}",
                 to_expr=f"2^x(1 + 2^{{-1}}) = {rhs}",
                 op="factor out 2^x", rule="common factor"),
            step(from_expr=f"2^x \\left(\\frac{{3}}{{2}}\\right) = {rhs}",
                 to_expr=f"2^x = {2**x_val}",
                 op="multiply both sides by 2/3", rule="fraction division"),
            step(from_expr=f"2^x = {2**x_val}", to_expr=f"x = {x_val}", op="equate exponents", rule="solve for x"),
        ],
        final_expr=sp.Integer(x_val),
    )
    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Solve for }} x: 2^x + 2^{{x - 1}} = {rhs}",
        answer_expr=sp.Integer(x_val),
        answer_mode="value",
        answer_latex=str(x_val),
        marks=3,
        canonical_solution=sol,
        explanation=f"Factorise $2^x$ out: $2^x(1 + \\frac{{1}}{{2}}) = {rhs} \\implies 2^x(\\frac{{3}}{{2}}) = {rhs} \\implies 2^x = {2**x_val} \\implies x = {x_val}$.",
        hint="Write 2^(x - 1) as 2^x * 2^-1 = 2^x * 1/2, then factor out 2^x.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="46_exponential_equation_common_factor_negative_shift",
        learning_objective_id=f"{LO}.46_exp_eq_neg_shift",
        misconception_tags=["fraction_multiplication_error", "confuses_shifted_power"],
        diagnostic_tags=["exponential_equations", "fractional_coefficients"],
        keywords=["negative shift", "common factor", "solve"],
    )
    return _add_pillars(q, "46_exponential_equation_common_factor_negative_shift", duration=3, weight=15)


# --------------------------------------------------------------------------- #
# 47_equation_rational_exponent_unit_fraction
# --------------------------------------------------------------------------- #
def _build_47_equation_rational_exponent_unit_fraction(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    n_val = r.choice([2, 3])
    rhs = r.randint(2, 6)
    ans_val = rhs**n_val

    sol = solution(
        goal="solve equation with unit rational exponent",
        chain_type="equation",
        var="x",
        steps=[
            step(from_expr=f"x^{{\\frac{{1}}{{{n_val}}}}} = {rhs}",
                 to_expr=f"(x^{{\\frac{{1}}{{{n_val}}}}})^{{{n_val}}} = {rhs}^{{{n_val}}}",
                 op=f"raise both sides to the power {n_val}", rule="reciprocal power"),
            step(from_expr=f"x = {rhs}^{{{n_val}}}", to_expr=f"x = {ans_val}", op="evaluate power", rule="arithmetic"),
        ],
        final_expr=sp.Integer(ans_val),
    )
    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Solve for }} x: x^{{\\frac{{1}}{{{n_val}}}}} = {rhs}",
        answer_expr=sp.Integer(ans_val),
        answer_mode="value",
        answer_latex=str(ans_val),
        marks=2,
        canonical_solution=sol,
        explanation=f"Raise both sides to the power ${n_val}$: $(x^{{1/{n_val}}})^{{{n_val}}} = {rhs}^{{{n_val}}} \\implies x = {ans_val}$.",
        hint=f"Raise both sides to the power of {n_val} to eliminate the fraction 1/{n_val}.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="47_equation_rational_exponent_unit_fraction",
        learning_objective_id=f"{LO}.47_eq_rational_unit",
        misconception_tags=["multiplies_by_n_instead_of_power", "inverts_rhs"],
        diagnostic_tags=["equations", "rational_exponents"],
        keywords=["rational exponent", "solve", "unit fraction"],
    )
    return _add_pillars(q, "47_equation_rational_exponent_unit_fraction", duration=2, weight=15)


# --------------------------------------------------------------------------- #
# 48_equation_rational_exponent_general_fraction
# --------------------------------------------------------------------------- #
def _build_48_equation_rational_exponent_general_fraction(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    cases = [
        (2, 3, 4, 8, "x^{2/3} = 4 -> x = 4^{3/2} = (2^2)^{3/2} = 8"),
        (2, 3, 9, 27, "x^{2/3} = 9 -> x = 9^{3/2} = (3^2)^{3/2} = 27"),
        (3, 2, 8, 4, "x^{3/2} = 8 -> x = 8^{2/3} = (2^3)^{2/3} = 4"),
        (3, 4, 27, 81, "x^{3/4} = 27 -> x = 27^{4/3} = (3^3)^{4/3} = 81"),
    ]
    m_val, n_val, rhs, ans_val, expl = r.choice(cases)

    sol = solution(
        goal="solve equation with general rational exponent",
        chain_type="equation",
        var="x",
        steps=[
            step(from_expr=f"x^{{\\frac{{{m_val}}}{{{n_val}}}}} = {rhs}",
                 to_expr=f"(x^{{\\frac{{{m_val}}}{{{n_val}}}}})^{{\\frac{{{n_val}}}{{{m_val}}}}} = ({rhs})^{{\\frac{{{n_val}}}{{{m_val}}}}}",
                 op=f"raise both sides to reciprocal power {n_val}/{m_val}", rule="reciprocal exponent"),
            step(from_expr=f"x = ({rhs})^{{\\frac{{{n_val}}}{{{m_val}}}}}",
                 to_expr=f"x = {ans_val}",
                 op="evaluate numerical rational power", rule="prime bases"),
        ],
        final_expr=sp.Integer(ans_val),
    )
    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Solve for }} x: x^{{\\frac{{{m_val}}}{{{n_val}}}}} = {rhs}",
        answer_expr=sp.Integer(ans_val),
        answer_mode="value",
        answer_latex=str(ans_val),
        marks=2,
        canonical_solution=sol,
        explanation=f"Raise both sides to the reciprocal power ${n_val}/{m_val}$: $x = {rhs}^{{{n_val}/{m_val}}} = {ans_val}$.",
        hint=f"Raise both sides to the reciprocal power {n_val}/{m_val}.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="48_equation_rational_exponent_general_fraction",
        learning_objective_id=f"{LO}.48_eq_rational_general",
        misconception_tags=["forgets_to_invert_exponent", "evaluation_error_on_rational_power"],
        diagnostic_tags=["equations", "general_rational_exponents"],
        keywords=["rational exponent", "reciprocal power", "solve"],
    )
    return _add_pillars(q, "48_equation_rational_exponent_general_fraction", duration=2, weight=15)


# --------------------------------------------------------------------------- #
# 49_exponential_equation_quadratic_k_substitution
# --------------------------------------------------------------------------- #
def _build_49_exponential_equation_quadratic_k_substitution(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    # e.g. 2^(2x) - 6*2^x + 8 = 0
    # (k - 2)(k - 4) = 0 -> k = 2 or k = 4 -> 2^x = 2 or 2^x = 4 -> x = 1 or x = 2
    base_val = 2
    x1 = r.choice([0, 1])
    x2 = r.choice([2, 3])
    k1 = base_val**x1
    k2 = base_val**x2
    b_coeff = k1 + k2
    c_const = k1 * k2
    prompt = f"{base_val}^{{2x}} - {b_coeff} \\cdot {base_val}^x + {c_const} = 0"
    ans_str = f"x = {x1} \\text{{ or }} x = {x2}"

    sol = solution(
        goal="solve quadratic exponential equation via k-substitution",
        chain_type="equation",
        var="x",
        steps=[
            step(from_expr=prompt,
                 to_expr=f"k^2 - {b_coeff}k + {c_const} = 0",
                 op=f"let k = {base_val}^x", rule="substitution"),
            step(from_expr=f"(k - {k1})(k - {k2}) = 0",
                 to_expr=f"k = {k1} \\text{{ or }} k = {k2}",
                 op="solve quadratic for k", rule="zero factor law"),
            step(from_expr=f"{base_val}^x = {k1} \\text{{ or }} {base_val}^x = {k2}",
                 to_expr=ans_str,
                 op="solve for x", rule="equating bases"),
        ],
        final_expr=ans_str,
    )
    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Solve for }} x: {prompt}",
        answer_expr=ans_str,
        answer_mode="expression",
        answer_latex=ans_str,
        marks=4,
        canonical_solution=sol,
        explanation=f"Let $k = {base_val}^x$. Then $k^2 - {b_coeff}k + {c_const} = 0 \\implies (k - {k1})(k - {k2}) = 0$. Hence ${base_val}^x = {k1} \\implies x = {x1}$ or ${base_val}^x = {k2} \\implies x = {x2}$.",
        hint="Let k = 2^x to obtain a standard quadratic equation in k.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="49_exponential_equation_quadratic_k_substitution",
        learning_objective_id=f"{LO}.49_exp_eq_k_sub",
        misconception_tags=["stops_at_values_of_k", "quadratic_factorisation_error"],
        diagnostic_tags=["equations", "quadratic_exponents"],
        keywords=["k-substitution", "quadratic exponential", "solve"],
    )
    return _add_pillars(q, "49_exponential_equation_quadratic_k_substitution", duration=4, weight=15)


# --------------------------------------------------------------------------- #
# 50_exponential_application_growth_decay
# --------------------------------------------------------------------------- #
def _build_50_exponential_application_growth_decay(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    n0 = r.choice([50, 100, 200, 500])
    doubling_period = r.choice([2, 3, 4])
    periods = r.choice([2, 3, 4])
    total_time = doubling_period * periods
    final_count = n0 * (2**periods)

    q = make_short(
        prefix=TOPIC,
        prompt_latex=(
            f"\\text{{A bacterial culture starts with }} {n0} \\text{{ bacteria and doubles every }} {doubling_period} "
            f"\\text{{ hours according to }} N(t) = {n0} \\cdot 2^{{t/{doubling_period}}}. "
            f"\\text{{ Find the number of bacteria after }} {total_time} \\text{{ hours.}}"
        ),
        answer_expr=sp.Integer(final_count),
        answer_mode="value",
        answer_latex=str(final_count),
        marks=2,
        explanation=f"Substitute $t = {total_time}$: $N({total_time}) = {n0} \\cdot 2^{{{total_time}/{doubling_period}}} = {n0} \\cdot 2^{{{periods}}} = {n0} \\times {2**periods} = {final_count}$.",
        hint="Substitute the given time t into the exponential formula.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="50_exponential_application_growth_decay",
        learning_objective_id=f"{LO}.50_exponential_application",
        misconception_tags=["multiplies_initial_amount_by_two_first", "power_order_of_operations_error"],
        diagnostic_tags=["exponents", "applications"],
        keywords=["exponential growth", "doubling time", "application"],
    )
    return _add_pillars(q, "50_exponential_application_growth_decay", duration=2, weight=15)


BUILDERS_26_50: Dict[str, Any] = {
    "26_rational_exponent_definition_unit_fraction": _build_26_rational_exponent_definition_unit_fraction,
    "27_rational_exponent_definition_general_fraction": _build_27_rational_exponent_definition_general_fraction,
    "28_evaluate_numeric_power_unit_fraction_exponent": _build_28_evaluate_numeric_power_unit_fraction_exponent,
    "29_evaluate_numeric_power_non_unit_rational_exponent": _build_29_evaluate_numeric_power_non_unit_rational_exponent,
    "30_evaluate_numeric_power_negative_rational_exponent": _build_30_evaluate_numeric_power_negative_rational_exponent,
    "31_simplify_algebraic_expression_rational_exponents": _build_31_simplify_algebraic_expression_rational_exponents,
    "32_multiply_powers_with_fractional_exponents": _build_32_multiply_powers_with_fractional_exponents,
    "33_quotient_powers_with_fractional_exponents": _build_33_quotient_powers_with_fractional_exponents,
    "34_power_of_power_fractional_exponents": _build_34_power_of_power_fractional_exponents,
    "35_radical_algebraic_simplification": _build_35_radical_algebraic_simplification,
    "36_exponential_equation_simple_integer_power": _build_36_exponential_equation_simple_integer_power,
    "37_exponential_equation_linear_exponent": _build_37_exponential_equation_linear_exponent,
    "38_exponential_equation_negative_result": _build_38_exponential_equation_negative_result,
    "39_exponential_equation_composite_base_both_sides": _build_39_exponential_equation_composite_base_both_sides,
    "40_exponential_equation_composite_powers": _build_40_exponential_equation_composite_powers,
    "41_exponential_equation_fractional_base": _build_41_exponential_equation_fractional_base,
    "42_exponential_equation_zero_exponent_property": _build_42_exponential_equation_zero_exponent_property,
    "43_exponential_equation_coefficient_division": _build_43_exponential_equation_coefficient_division,
    "44_exponential_equation_common_factor_addition": _build_44_exponential_equation_common_factor_addition,
    "45_exponential_equation_common_factor_subtraction": _build_45_exponential_equation_common_factor_subtraction,
    "46_exponential_equation_common_factor_negative_shift": _build_46_exponential_equation_common_factor_negative_shift,
    "47_equation_rational_exponent_unit_fraction": _build_47_equation_rational_exponent_unit_fraction,
    "48_equation_rational_exponent_general_fraction": _build_48_equation_rational_exponent_general_fraction,
    "49_exponential_equation_quadratic_k_substitution": _build_49_exponential_equation_quadratic_k_substitution,
    "50_exponential_application_growth_decay": _build_50_exponential_application_growth_decay,
}
