"""Grade 10 Mathematics — Term 1 — Exponents: Archetypes 01 to 25.

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
t = sp.Symbol("t")


def _add_pillars(q: Dict[str, Any], subskill_name: str, duration: int = 3, weight: int = 15) -> Dict[str, Any]:
    marks = int(q.get("marks", 2))
    schema = [
        {"criterion": "Application of laws of exponents / prime base reduction", "marks": max(1, marks - 1)},
        {"criterion": "Accurate simplified expression with positive exponents", "marks": 1},
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
# 01_meaning_of_exponential_notation
# --------------------------------------------------------------------------- #
def _build_01_meaning_of_exponential_notation(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    base = r.choice([2, 3, 5, 7, x, y])
    power = r.randint(3, 6)
    base_latex = to_latex(base) if isinstance(base, sp.Symbol) else str(base)
    repeated = " \\times ".join([f"{base_latex}"] * power)

    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Write }} {repeated} \\text{{ in exponential form }} a^n.",
        answer_expr=f"{base_latex}^{{{power}}}",
        answer_mode="expression",
        answer_latex=f"{base_latex}^{{{power}}}",
        marks=1,
        explanation=f"The base {base_latex} is multiplied by itself {power} times, which is written as ${base_latex}^{{{power}}}$.",
        hint="Count how many times the base is multiplied by itself to find the exponent.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="01_meaning_of_exponential_notation",
        learning_objective_id=f"{LO}.01_meaning_notation",
        misconception_tags=["multiplies_base_by_exponent", "confuses_base_and_index"],
        diagnostic_tags=["exponents", "notation"],
        keywords=["exponential form", "base", "index", "exponent"],
    )
    return _add_pillars(q, "01_meaning_of_exponential_notation", duration=1, weight=15)


# --------------------------------------------------------------------------- #
# 02_zero_exponent_law_numerical
# --------------------------------------------------------------------------- #
def _build_02_zero_exponent_law_numerical(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    case = r.choice(["positive_base", "negative_with_bracket", "negative_without_bracket", "with_coefficient"])
    if case == "positive_base":
        b = r.choice([4, 7, 12, 25, 100])
        prompt = f"{b}^0"
        ans = sp.Integer(1)
        expl = "Any non-zero real number raised to the power 0 equals 1."
    elif case == "negative_with_bracket":
        b = r.choice([3, 5, 8, 11])
        prompt = f"(-{b})^0"
        ans = sp.Integer(1)
        expl = "The negative base is inside brackets, so (-b)^0 = 1."
    elif case == "negative_without_bracket":
        b = r.choice([3, 5, 8, 11])
        prompt = f"-{b}^0"
        ans = sp.Integer(-1)
        expl = "Without brackets, the power 0 applies only to the base b, so -b^0 = -(1) = -1."
    else:
        coeff = r.randint(2, 9)
        b = r.choice([2, 5, 10])
        prompt = f"{coeff} \\times {b}^0"
        ans = sp.Integer(coeff)
        expl = f"{coeff} * (b^0) = {coeff} * 1 = {coeff}."

    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Evaluate: }} {prompt}",
        answer_expr=ans,
        answer_mode="value",
        answer_latex=str(ans),
        marks=1,
        explanation=expl,
        hint="Remember that a^0 = 1 for any non-zero real number a. Watch out for negative signs outside brackets!",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="02_zero_exponent_law_numerical",
        learning_objective_id=f"{LO}.02_zero_exponent_num",
        misconception_tags=["zero_exponent_gives_zero", "sign_error_zero_exponent"],
        diagnostic_tags=["exponents", "zero_exponent"],
        keywords=["zero exponent", "evaluate"],
    )
    return _add_pillars(q, "02_zero_exponent_law_numerical", duration=1, weight=15)


# --------------------------------------------------------------------------- #
# 03_zero_exponent_law_algebraic
# --------------------------------------------------------------------------- #
def _build_03_zero_exponent_law_algebraic(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    c = nonzero(r, 2, 8)
    variant = r.choice(["coeff_times_power", "bracket_power", "sum_with_zero_power"])
    if variant == "coeff_times_power":
        prompt = f"{c}x^0"
        ans = sp.Integer(c)
        expl = f"Since $x^0 = 1$ for $x \\neq 0$, ${c}x^0 = {c}(1) = {c}$."
    elif variant == "bracket_power":
        prompt = f"({c}x)^0"
        ans = sp.Integer(1)
        expl = f"The entire bracket $({c}x)$ is raised to the power 0, so $({c}x)^0 = 1$."
    else:
        k = nonzero(r, 1, 9)
        prompt = f"{c}x^0 + {k}"
        ans = sp.Integer(c + k)
        expl = f"${c}x^0 + {k} = {c}(1) + {k} = {c + k}$."

    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Simplify (assuming }} x \\neq 0\\text{{): }} {prompt}",
        answer_expr=ans,
        answer_mode="value",
        answer_latex=str(ans),
        marks=1,
        explanation=expl,
        hint="Distinguish between c*x^0 = c*(1) and (c*x)^0 = 1.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="03_zero_exponent_law_algebraic",
        learning_objective_id=f"{LO}.03_zero_exponent_alg",
        misconception_tags=["applies_power_to_coefficient", "zero_exponent_cancels_everything"],
        diagnostic_tags=["exponents", "algebraic_zero_exponent"],
        keywords=["zero exponent", "algebraic", "simplify"],
    )
    return _add_pillars(q, "03_zero_exponent_law_algebraic", duration=1, weight=15)


# --------------------------------------------------------------------------- #
# 04_negative_exponent_law_numerical
# --------------------------------------------------------------------------- #
def _build_04_negative_exponent_law_numerical(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    variant = r.choice(["integer_base", "fraction_base", "reciprocal_negative"])
    if variant == "integer_base":
        b = r.choice([2, 3, 5, 10])
        p = r.choice([1, 2, 3, 4] if b == 2 else [1, 2, 3])
        ans = sp.Rational(1, b**p)
        prompt = f"{b}^{{-{p}}}"
        expl = f"Apply $a^{{-n}} = \\dfrac{{1}}{{a^n}}$: ${b}^{{-{p}}} = \\dfrac{{1}}{{{b}^{{{p}}}}} = \\dfrac{{1}}{{{b**p}}}$."
        ans_latex = f"\\frac{{1}}{{{b**p}}}"
    elif variant == "fraction_base":
        n_val = r.choice([2, 3])
        d_val = r.choice([3, 4, 5])
        if n_val >= d_val:
            d_val = n_val + 1
        p = r.choice([2, 3])
        ans = sp.Rational(d_val**p, n_val**p)
        prompt = f"\\left(\\dfrac{{{n_val}}}{{{d_val}}}\\right)^{{-{p}}}"
        expl = f"Invert the fraction: $\\left(\\dfrac{{{n_val}}}{{{d_val}}}\\right)^{{-{p}}} = \\left(\\dfrac{{{d_val}}}{{{n_val}}}\\right)^{{{p}}} = \\dfrac{{{d_val**p}}}{{{n_val**p}}}$."
        ans_latex = f"\\frac{{{d_val**p}}}{{{n_val**p}}}"
    else:
        b = r.choice([2, 3, 4, 5])
        p = r.choice([2, 3])
        ans = sp.Integer(b**p)
        prompt = f"\\dfrac{{1}}{{{b}^{{-{p}}}}}"
        expl = f"$\\dfrac{{1}}{{a^{{-n}}}} = a^n$: $\\dfrac{{1}}{{{b}^{{-{p}}}}} = {b}^{{{p}}} = {b**p}$."
        ans_latex = str(b**p)

    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Evaluate and simplify: }} {prompt}",
        answer_expr=ans,
        answer_mode="expression",
        answer_latex=ans_latex,
        marks=2,
        explanation=expl,
        hint="Negative exponents mean take the reciprocal: a^-n = 1/a^n.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="04_negative_exponent_law_numerical",
        learning_objective_id=f"{LO}.04_negative_exponent_num",
        misconception_tags=["negative_exponent_makes_number_negative", "forgets_to_invert_fraction"],
        diagnostic_tags=["exponents", "negative_exponents"],
        keywords=["negative exponent", "evaluate", "reciprocal"],
    )
    return _add_pillars(q, "04_negative_exponent_law_numerical", duration=2, weight=15)


# --------------------------------------------------------------------------- #
# 05_negative_exponent_law_algebraic
# --------------------------------------------------------------------------- #
def _build_05_negative_exponent_law_algebraic(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    c = nonzero(r, 2, 7)
    p = r.randint(2, 6)
    variant = r.choice(["coeff_neg_power", "fraction_neg_denom", "two_var_neg"])
    if variant == "coeff_neg_power":
        prompt = f"{c}x^{{-{p}}}"
        ans = sp.Mul(c, 1 / x**p, evaluate=False)
        ans_latex = f"\\frac{{{c}}}{{x^{{{p}}}}}"
        expl = f"Only the variable $x$ has the negative exponent: ${c}x^{{-{p}}} = \\dfrac{{{c}}}{{x^{{{p}}}}}.$"
    elif variant == "fraction_neg_denom":
        prompt = f"\\dfrac{{{c}}}{{x^{{-{p}}}}}"
        ans = c * x**p
        ans_latex = f"{c}x^{{{p}}}"
        expl = f"Move $x^{{-{p}}}$ to the numerator to make the exponent positive: ${c}x^{{{p}}}.$"
    else:
        q_exp = r.randint(2, 5)
        prompt = f"\\dfrac{{x^{{-{p}}}}}{{y^{{-{q_exp}}}}}"
        ans = y**q_exp / x**p
        ans_latex = f"\\frac{{y^{{{q_exp}}}}}{{x^{{{p}}}}}"
        expl = f"Swap positions to write with positive exponents: $\\dfrac{{y^{{{q_exp}}}}}{{x^{{{p}}}}}.$"

    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Rewrite with positive exponents only: }} {prompt}",
        answer_expr=ans,
        answer_mode="expression",
        answer_latex=ans_latex,
        marks=1,
        explanation=expl,
        hint="A term with a negative exponent moves across the fraction bar to become positive.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="05_negative_exponent_law_algebraic",
        learning_objective_id=f"{LO}.05_negative_exponent_alg",
        misconception_tags=["moves_coefficient_with_variable", "sign_error_on_exponents"],
        diagnostic_tags=["exponents", "algebraic_negative_exponents"],
        keywords=["positive exponents", "algebraic", "rewrite"],
    )
    return _add_pillars(q, "05_negative_exponent_law_algebraic", duration=2, weight=15)


# --------------------------------------------------------------------------- #
# 06_product_rule_same_base_numerical
# --------------------------------------------------------------------------- #
def _build_06_product_rule_same_base_numerical(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    b = r.choice([2, 3, 5])
    m_val = r.randint(2, 5)
    n_val = r.randint(2, 5)
    prompt = f"{b}^{{{m_val}}} \\times {b}^{{{n_val}}}"
    total = m_val + n_val
    ans = b**total

    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Simplify using exponent laws, leaving in power form: }} {prompt}",
        answer_expr=f"{b}^{{{total}}}",
        answer_mode="expression",
        answer_latex=f"{b}^{{{total}}}",
        marks=1,
        explanation=f"Apply the product rule $a^m \\times a^n = a^{{m+n}}$: ${b}^{{{m_val}}} \\times {b}^{{{n_val}}} = {b}^{{{m_val} + {n_val}}} = {b}^{{{total}}}$.",
        hint="When multiplying powers of the same base, keep the base and add the exponents.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="06_product_rule_same_base_numerical",
        learning_objective_id=f"{LO}.06_product_rule_num",
        misconception_tags=["multiplies_bases", "multiplies_exponents_instead_of_adding"],
        diagnostic_tags=["exponents", "product_rule"],
        keywords=["product rule", "same base", "add exponents"],
    )
    return _add_pillars(q, "06_product_rule_same_base_numerical", duration=1, weight=15)


# --------------------------------------------------------------------------- #
# 07_product_rule_same_base_algebraic
# --------------------------------------------------------------------------- #
def _build_07_product_rule_same_base_algebraic(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    c1 = nonzero(r, 2, 6)
    c2 = nonzero(r, 2, 6)
    m_val = r.randint(1, 5)
    n_val = r.randint(1, 5)
    prompt = f"({c1}x^{{{m_val}}})({c2}x^{{{n_val}}})"
    coeff = c1 * c2
    exp_sum = m_val + n_val
    ans = coeff * x**exp_sum

    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Simplify: }} {prompt}",
        answer_expr=ans,
        answer_mode="expression",
        marks=2,
        explanation=f"Multiply the numerical coefficients (${c1} \\times {c2} = {coeff}$) and add exponents on $x$ (${m_val} + {n_val} = {exp_sum}$): ${to_latex(ans)}$.",
        hint="Multiply the coefficients, and add the powers of the matching base.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="07_product_rule_same_base_algebraic",
        learning_objective_id=f"{LO}.07_product_rule_alg",
        misconception_tags=["adds_coefficients_instead_of_multiplying", "multiplies_exponents"],
        diagnostic_tags=["exponents", "product_rule_algebraic"],
        keywords=["product rule", "algebraic", "coefficients"],
    )
    return _add_pillars(q, "07_product_rule_same_base_algebraic", duration=2, weight=15)


# --------------------------------------------------------------------------- #
# 08_quotient_rule_same_base_numerical
# --------------------------------------------------------------------------- #
def _build_08_quotient_rule_same_base_numerical(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    b = r.choice([2, 3, 5, 7])
    m_val = r.randint(5, 9)
    n_val = r.randint(2, 4)
    diff = m_val - n_val
    prompt = f"\\dfrac{{{b}^{{{m_val}}}}}{{{b}^{{{n_val}}}}}"

    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Simplify in power form: }} {prompt}",
        answer_expr=f"{b}^{{{diff}}}",
        answer_mode="expression",
        answer_latex=f"{b}^{{{diff}}}",
        marks=1,
        explanation=f"Apply quotient rule $a^m / a^n = a^{{m-n}}$: ${b}^{{{m_val}}} / {b}^{{{n_val}}} = {b}^{{{m_val} - {n_val}}} = {b}^{{{diff}}}$.",
        hint="When dividing powers of the same base, subtract the bottom exponent from the top.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="08_quotient_rule_same_base_numerical",
        learning_objective_id=f"{LO}.08_quotient_rule_num",
        misconception_tags=["divides_exponents", "divides_bases"],
        diagnostic_tags=["exponents", "quotient_rule"],
        keywords=["quotient rule", "subtract exponents", "power form"],
    )
    return _add_pillars(q, "08_quotient_rule_same_base_numerical", duration=1, weight=15)


# --------------------------------------------------------------------------- #
# 09_quotient_rule_same_base_algebraic
# --------------------------------------------------------------------------- #
def _build_09_quotient_rule_same_base_algebraic(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    c_num = r.choice([12, 16, 18, 24, 30, 36])
    c_den = r.choice([2, 3, 4, 6])
    m_val = r.randint(4, 8)
    n_val = r.randint(1, 3)
    coeff = c_num // c_den
    diff = m_val - n_val
    ans = coeff * x**diff

    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Simplify: }} \\dfrac{{{c_num}x^{{{m_val}}}}}{{{c_den}x^{{{n_val}}}}}",
        answer_expr=ans,
        answer_mode="expression",
        marks=2,
        explanation=f"Divide the numerical coefficients (${c_num} \\div {c_den} = {coeff}$) and subtract the exponents on $x$ (${m_val} - {n_val} = {diff}$): ${to_latex(ans)}$.",
        hint="Divide the numbers and subtract the exponents of x.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="09_quotient_rule_same_base_algebraic",
        learning_objective_id=f"{LO}.09_quotient_rule_alg",
        misconception_tags=["subtracts_coefficients", "divides_exponents"],
        diagnostic_tags=["exponents", "quotient_rule_algebraic"],
        keywords=["quotient rule", "algebraic", "divide"],
    )
    return _add_pillars(q, "09_quotient_rule_same_base_algebraic", duration=2, weight=15)


# --------------------------------------------------------------------------- #
# 10_power_of_a_power_rule
# --------------------------------------------------------------------------- #
def _build_10_power_of_a_power_rule(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    m_val = r.randint(2, 5)
    n_val = r.randint(2, 4)
    prod = m_val * n_val
    ans = x**prod

    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Simplify: }} (x^{{{m_val}}})^{{{n_val}}}",
        answer_expr=ans,
        answer_mode="expression",
        marks=1,
        explanation=f"Apply $(a^m)^n = a^{{mn}}$: multiply the exponents $({m_val}) \\times ({n_val}) = {prod}$, giving $x^{{{prod}}}$.",
        hint="Multiply the inner exponent by the outer exponent.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="10_power_of_a_power_rule",
        learning_objective_id=f"{LO}.10_power_of_power",
        misconception_tags=["adds_exponents_instead_of_multiplying", "raises_inner_exponent_to_power"],
        diagnostic_tags=["exponents", "power_of_power"],
        keywords=["power of a power", "multiply exponents"],
    )
    return _add_pillars(q, "10_power_of_a_power_rule", duration=1, weight=15)


# --------------------------------------------------------------------------- #
# 11_power_of_a_product_rule
# --------------------------------------------------------------------------- #
def _build_11_power_of_a_product_rule(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    c = nonzero(r, -4, 4, exclude=[1])
    m_val = r.randint(1, 3)
    p_out = r.choice([2, 3])
    ans = (c**p_out) * (x**(m_val * p_out))

    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Simplify: }} ({c}x^{{{m_val}}})^{{{p_out}}}",
        answer_expr=ans,
        answer_mode="expression",
        marks=2,
        explanation=f"Raise every factor inside the bracket to the power {p_out}: $({c})^{{{p_out}}} \\times (x^{{{m_val}}})^{{{p_out}}} = {to_latex(ans)}$.",
        hint="Apply the outer power to both the coefficient and the variable.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="11_power_of_a_product_rule",
        learning_objective_id=f"{LO}.11_power_of_product",
        misconception_tags=["forgets_to_raise_coefficient", "sign_error_on_negative_coefficient"],
        diagnostic_tags=["exponents", "power_of_product"],
        keywords=["power of a product", "distribute power"],
    )
    return _add_pillars(q, "11_power_of_a_product_rule", duration=2, weight=15)


# --------------------------------------------------------------------------- #
# 12_power_of_a_quotient_rule
# --------------------------------------------------------------------------- #
def _build_12_power_of_a_quotient_rule(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    c_top = r.choice([2, 3])
    c_bot = r.choice([4, 5])
    p = r.choice([2, 3])
    ans = (c_top**p * x**p) / (c_bot**p * y**p)

    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Simplify: }} \\left(\\dfrac{{{c_top}x}}{{{c_bot}y}}\\right)^{{{p}}}",
        answer_expr=ans,
        answer_mode="expression",
        marks=2,
        explanation=f"Raise numerator and denominator to the power {p}: $\\dfrac{{{c_top}^{{{p}}} x^{{{p}}}}}{{{c_bot}^{{{p}}} y^{{{p}}}}} = \\dfrac{{{c_top**p}x^{{{p}}}}}{{{c_bot**p}y^{{{p}}}}}$.",
        hint="Raise both the numerator and the denominator to the outside power.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="12_power_of_a_quotient_rule",
        learning_objective_id=f"{LO}.12_power_of_quotient",
        misconception_tags=["only_raises_numerator", "multiplies_instead_of_powers"],
        diagnostic_tags=["exponents", "power_of_quotient"],
        keywords=["power of a quotient", "fractions with powers"],
    )
    return _add_pillars(q, "12_power_of_a_quotient_rule", duration=2, weight=15)


# --------------------------------------------------------------------------- #
# 13_combine_monomial_exponent_laws_basic
# --------------------------------------------------------------------------- #
def _build_13_combine_monomial_exponent_laws_basic(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    a = r.randint(2, 4)
    b = r.randint(2, 5)
    # [(a*x^2*y)^2] / [b*x*y^3]
    top_c = a**2
    bot_c = b
    hcf = math.gcd(top_c, bot_c)
    fin_top_c = top_c // hcf
    fin_bot_c = bot_c // hcf
    ans = (fin_top_c * x**3) / (fin_bot_c * y)

    sol = solution(
        goal="simplify monomial expression with exponent laws",
        chain_type="expression",
        var="x",
        steps=[
            step(from_expr=f"\\frac{{({a}x^2 y)^2}}{{{b}x y^3}}",
                 to_expr=f"\\frac{{{top_c}x^4 y^2}}{{{b}x y^3}}",
                 op="expand power of product in numerator", rule="(ab)^n = a^n b^n"),
            step(from_expr=f"\\frac{{{top_c}x^4 y^2}}{{{b}x y^3}}",
                 to_expr=ans,
                 op="cancel like factors and apply quotient rule", rule="quotient rule"),
        ],
        final_expr=ans,
    )
    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Simplify, leaving with positive exponents: }} \\dfrac{{({a}x^2 y)^2}}{{{b}x y^3}}",
        answer_expr=ans,
        answer_mode="expression",
        marks=3,
        canonical_solution=sol,
        explanation=f"Expand the numerator first to get ${top_c}x^4 y^2$. Then divide by ${b}xy^3$ using quotient rules: ${to_latex(ans)}$.",
        hint="Apply the power of a product rule to the numerator first, then cancel with the denominator.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="13_combine_monomial_exponent_laws_basic",
        learning_objective_id=f"{LO}.13_monomial_combined_basic",
        misconception_tags=["fails_to_square_coefficient", "leaves_negative_exponents"],
        diagnostic_tags=["exponents", "combined_monomials"],
        keywords=["combine laws", "monomial", "positive exponents"],
    )
    return _add_pillars(q, "13_combine_monomial_exponent_laws_basic", duration=3, weight=15)


# --------------------------------------------------------------------------- #
# 14_combine_monomial_exponent_laws_advanced
# --------------------------------------------------------------------------- #
def _build_14_combine_monomial_exponent_laws_advanced(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    c = r.choice([2, 3])
    # [(c*x^-2 y^3)^-2] * [x^4 y^-2]
    # = (c^-2 * x^4 * y^-6) * (x^4 * y^-2) = (1/c^2) * x^8 * y^-8 = x^8 / (c^2 y^8)
    denom_c = c**2
    ans = (x**8) / (denom_c * y**8)

    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Simplify, expressing your answer with positive exponents: }} ({c}x^{{-2}} y^3)^{{-2}} \\cdot (x^4 y^{{-2}})",
        answer_expr=ans,
        answer_mode="expression",
        marks=3,
        explanation=f"Distribute the exponent $-2$: ${c}^{{-2}} x^4 y^{{-6}}$. Multiply by $x^4 y^{{-2}}$: $\\dfrac{{1}}{{{denom_c}}} x^8 y^{{-8}} = \\dfrac{{x^8}}{{{denom_c}y^8}}$.",
        hint="Distribute the outside power of -2 first, remembering to multiply exponents and apply the power to the coefficient.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="14_combine_monomial_exponent_laws_advanced",
        learning_objective_id=f"{LO}.14_monomial_combined_adv",
        misconception_tags=["incorrect_negative_power_distribution", "sign_error_adding_exponents"],
        diagnostic_tags=["exponents", "negative_powers_combined"],
        keywords=["advanced exponents", "negative exponents", "positive form"],
    )
    return _add_pillars(q, "14_combine_monomial_exponent_laws_advanced", duration=3, weight=15)


# --------------------------------------------------------------------------- #
# 15_scientific_notation_standard_form
# --------------------------------------------------------------------------- #
def _build_15_scientific_notation_standard_form(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    variant = r.choice(["large_number", "small_decimal"])
    if variant == "large_number":
        a = r.randint(12, 98) / 10.0
        p = r.randint(4, 7)
        std_val = int(a * (10**p))
        a_sa = num(a, 1)
        q = make_short(
            prefix=TOPIC,
            prompt_latex=f"\\text{{Write }} {std_val} \\text{{ in scientific notation }} (A \\times 10^k \\text{{ where }} 1 \\le A < 10).",
            answer_expr=f"{a_sa} \\times 10^{{{p}}}",
            answer_mode="expression",
            answer_latex=f"{a_sa} \\times 10^{{{p}}}",
            marks=1,
            explanation=f"Shift the decimal point {p} places to the left to place it after the first non-zero digit: ${a_sa} \\times 10^{{{p}}}$.",
            hint="Move the decimal point until there is exactly one non-zero digit to the left of the decimal.",
        )
    else:
        a = r.randint(12, 98) / 10.0
        p = r.randint(3, 5)
        small_float = a * (10**(-p))
        a_sa = num(a, 1)
        small_sa = num(small_float, p + 1)
        q = make_short(
            prefix=TOPIC,
            prompt_latex=f"\\text{{Write }} {small_sa} \\text{{ in scientific notation.}}",
            answer_expr=f"{a_sa} \\times 10^{{-{p}}}",
            answer_mode="expression",
            answer_latex=f"{a_sa} \\times 10^{{-{p}}}",
            marks=1,
            explanation=f"Shift the decimal point {p} places to the right: ${a_sa} \\times 10^{{-{p}}}$.",
            hint="For decimals smaller than 1, the power of 10 is negative.",
        )

    with_metadata(
        q,
        topic=TOPIC,
        subskill="15_scientific_notation_standard_form",
        learning_objective_id=f"{LO}.15_scientific_notation",
        misconception_tags=["wrong_power_of_ten", "fails_to_place_decimal_after_first_digit"],
        diagnostic_tags=["scientific_notation", "powers_of_ten"],
        keywords=["scientific notation", "standard form", "powers of 10"],
    )
    return _add_pillars(q, "15_scientific_notation_standard_form", duration=2, weight=15)


# --------------------------------------------------------------------------- #
# 16_prime_base_factorisation_numerical
# --------------------------------------------------------------------------- #
def _build_16_prime_base_factorisation_numerical(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    # e.g. (8^2 * 9^3) / (6^4)
    # 8 = 2^3 -> 8^2 = 2^6
    # 9 = 3^2 -> 9^3 = 3^6
    # 6 = 2 * 3 -> 6^4 = 2^4 * 3^4
    # Result = 2^(6-4) * 3^(6-4) = 2^2 * 3^2 = 4 * 9 = 36
    p2_top = r.choice([2, 3])
    p3_top = r.choice([2, 3])
    p_bot = 2
    # 8^p2_top * 9^p3_top / 6^p_bot
    top_str = f"8^{{{p2_top}}} \\cdot 9^{{{p3_top}}}"
    bot_str = f"6^{{{p_bot}}}"
    pow2 = 3 * p2_top - p_bot
    pow3 = 2 * p3_top - p_bot
    ans_val = (2**pow2) * (3**pow3)

    sol = solution(
        goal="simplify using prime bases",
        chain_type="expression",
        var="x",
        steps=[
            step(from_expr=f"\\frac{{{top_str}}}{{{bot_str}}}",
                 to_expr=f"\\frac{{(2^3)^{{{p2_top}}} \\cdot (3^2)^{{{p3_top}}}}}{{(2 \\cdot 3)^{{{p_bot}}}}}",
                 op="express all composite bases as products of prime factors", rule="prime factorisation"),
            step(from_expr=f"\\frac{{2^{{{3*p2_top}}} \\cdot 3^{{{2*p3_top}}}}}{{2^{{{p_bot}}} \\cdot 3^{{{p_bot}}}}}",
                 to_expr=f"2^{{{pow2}}} \\cdot 3^{{{pow3}}} = {ans_val}",
                 op="apply exponent quotient rules on bases 2 and 3", rule="quotient rule"),
        ],
        final_expr=sp.Integer(ans_val),
    )
    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Simplify without a calculator by expressing bases as prime numbers: }} \\dfrac{{{top_str}}}{{{bot_str}}}",
        answer_expr=sp.Integer(ans_val),
        answer_mode="value",
        answer_latex=str(ans_val),
        marks=3,
        canonical_solution=sol,
        explanation=f"Rewrite $8 = 2^3$, $9 = 3^2$, and $6 = 2 \\cdot 3$. Apply exponent laws to simplify to ${ans_val}$.",
        hint="Break composite bases down to prime factors: 8 = 2^3, 9 = 3^2, 6 = 2 * 3.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="16_prime_base_factorisation_numerical",
        learning_objective_id=f"{LO}.16_prime_base_num",
        misconception_tags=["calculates_large_powers_directly", "fails_to_distribute_prime_factors"],
        diagnostic_tags=["exponents", "prime_bases"],
        keywords=["prime bases", "simplify", "no calculator"],
    )
    return _add_pillars(q, "16_prime_base_factorisation_numerical", duration=3, weight=15)


# --------------------------------------------------------------------------- #
# 17_prime_base_algebraic_exponents_single_var
# --------------------------------------------------------------------------- #
def _build_17_prime_base_algebraic_exponents_single_var(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    # e.g. [2^(2n) * 4^n * 2] / [16^n]
    # = [2^(2n) * 2^(2n) * 2^1] / [2^(4n)] = 2^(4n + 1 - 4n) = 2^1 = 2
    shift = r.choice([1, 2, 3])
    # 2^(2n) * 4^n * 2^shift / 16^n
    prompt = f"\\dfrac{{2^{{2n}} \\cdot 4^n \\cdot 2^{{{shift}}}}}{{16^n}}"
    ans_val = 2**shift

    sol = solution(
        goal="simplify expression with algebraic exponents",
        chain_type="expression",
        var="n",
        steps=[
            step(from_expr=prompt,
                 to_expr=f"\\frac{{2^{{2n}} \\cdot (2^2)^n \\cdot 2^{{{shift}}}}}{{(2^4)^n}}",
                 op="convert bases 4 and 16 to base 2", rule="prime bases"),
            step(from_expr=f"\\frac{{2^{{2n + 2n + {shift}}}}}{{2^{{4n}}}}",
                 to_expr=f"2^{{4n + {shift} - 4n}} = 2^{{{shift}}} = {ans_val}",
                 op="add exponents in numerator and subtract denominator exponent", rule="exponent laws"),
        ],
        final_expr=sp.Integer(ans_val),
    )
    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Simplify: }} {prompt}",
        answer_expr=sp.Integer(ans_val),
        answer_mode="value",
        answer_latex=str(ans_val),
        marks=3,
        canonical_solution=sol,
        explanation=f"Rewrite $4 = 2^2$ and $16 = 2^4$. Combine powers: $2^{{2n + 2n + {shift} - 4n}} = 2^{{{shift}}} = {ans_val}$.",
        hint="Express 4 and 16 as powers of 2, then add and subtract exponents.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="17_prime_base_algebraic_exponents_single_var",
        learning_objective_id=f"{LO}.17_prime_base_alg_single",
        misconception_tags=["forgets_to_multiply_powers_of_powers", "sign_error_subtracting_variable"],
        diagnostic_tags=["exponents", "algebraic_exponents"],
        keywords=["algebraic exponents", "prime base", "simplify"],
    )
    return _add_pillars(q, "17_prime_base_algebraic_exponents_single_var", duration=3, weight=15)


# --------------------------------------------------------------------------- #
# 18_prime_base_algebraic_exponents_two_bases
# --------------------------------------------------------------------------- #
def _build_18_prime_base_algebraic_exponents_two_bases(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    # e.g. [2^(n+1) * 3^(n-1)] / [6^n]
    # = [2^(n+1) * 3^(n-1)] / [2^n * 3^n] = 2^(n+1-n) * 3^(n-1-n) = 2^1 * 3^-1 = 2/3
    k1 = r.choice([1, 2])
    k2 = r.choice([1, 2])
    # 2^(n+k1) * 3^(n-k2) / 6^n
    prompt = f"\\dfrac{{2^{{n + {k1}}} \\cdot 3^{{n - {k2}}}}}{{6^n}}"
    ans_frac = sp.Rational(2**k1, 3**k2)
    ans_latex = f"\\frac{{{2**k1}}}{{{3**k2}}}"

    sol = solution(
        goal="simplify expression with composite base in denominator",
        chain_type="expression",
        var="n",
        steps=[
            step(from_expr=prompt,
                 to_expr=f"\\frac{{2^{{n + {k1}}} \\cdot 3^{{n - {k2}}}}}{{(2 \\cdot 3)^n}} = \\frac{{2^{{n + {k1}}} \\cdot 3^{{n - {k2}}}}}{{2^n \\cdot 3^n}}",
                 op="rewrite 6^n as 2^n * 3^n", rule="power of product"),
            step(from_expr=f"2^{{(n + {k1}) - n}} \\cdot 3^{{(n - {k2}) - n}}",
                 to_expr=f"2^{{{k1}}} \\cdot 3^{{-{k2}}} = \\frac{{{2**k1}}}{{{3**k2}}}",
                 op="simplify exponents for base 2 and base 3", rule="quotient rule"),
        ],
        final_expr=ans_frac,
    )
    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Simplify: }} {prompt}",
        answer_expr=ans_frac,
        answer_mode="expression",
        answer_latex=ans_latex,
        marks=3,
        canonical_solution=sol,
        explanation=f"Rewrite $6^n = 2^n \\cdot 3^n$. Then group like bases: $2^{{n + {k1} - n}} \\cdot 3^{{n - {k2} - n}} = 2^{{{k1}}} \\cdot 3^{{-{k2}}} = {ans_latex}$.",
        hint="Break down 6^n into 2^n * 3^n, then simplify base 2 and base 3 separately.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="18_prime_base_algebraic_exponents_two_bases",
        learning_objective_id=f"{LO}.18_prime_base_two_bases",
        misconception_tags=["fails_to_split_composite_base", "cancels_unlike_bases"],
        diagnostic_tags=["exponents", "two_bases"],
        keywords=["prime bases", "composite base", "simplify"],
    )
    return _add_pillars(q, "18_prime_base_algebraic_exponents_two_bases", duration=3, weight=15)


# --------------------------------------------------------------------------- #
# 19_prime_base_with_fractional_composite_bases
# --------------------------------------------------------------------------- #
def _build_19_prime_base_with_fractional_composite_bases(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    # e.g. [12^x * 3^(x+1)] / [6^(2x)]
    # 12^x = (2^2 * 3)^x = 2^(2x) * 3^x
    # 6^(2x) = (2 * 3)^(2x) = 2^(2x) * 3^(2x)
    # [2^(2x) * 3^(2x + 1)] / [2^(2x) * 3^(2x)] = 3^1 = 3
    shift = r.choice([1, 2, 3])
    prompt = f"\\dfrac{{12^x \\cdot 3^{{x + {shift}}}}}{{6^{{2x}}}}"
    ans_val = 3**shift

    sol = solution(
        goal="simplify composite exponential fraction",
        chain_type="expression",
        var="x",
        steps=[
            step(from_expr=prompt,
                 to_expr=f"\\frac{{(2^2 \\cdot 3)^x \\cdot 3^{{x + {shift}}}}}{{(2 \\cdot 3)^{{2x}}}}",
                 op="prime factorise 12 and 6", rule="prime bases"),
            step(from_expr=f"\\frac{{2^{{2x}} \\cdot 3^{{2x + {shift}}}}}{{2^{{2x}} \\cdot 3^{{2x}}}}",
                 to_expr=f"3^{{{shift}}} = {ans_val}",
                 op="cancel 2^(2x) and subtract exponents of 3", rule="quotient rule"),
        ],
        final_expr=sp.Integer(ans_val),
    )
    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Simplify: }} {prompt}",
        answer_expr=sp.Integer(ans_val),
        answer_mode="value",
        answer_latex=str(ans_val),
        marks=3,
        canonical_solution=sol,
        explanation=f"Prime factorise $12 = 2^2 \\cdot 3$ and $6 = 2 \\cdot 3$. Expanding powers gives $\\dfrac{{2^{{2x}} \\cdot 3^{{2x + {shift}}}}}{{2^{{2x}} \\cdot 3^{{2x}}}} = 3^{{{shift}}} = {ans_val}$.",
        hint="Express 12 as 2^2 * 3 and 6 as 2 * 3.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="19_prime_base_with_fractional_composite_bases",
        learning_objective_id=f"{LO}.19_composite_fractional",
        misconception_tags=["incorrect_factorisation_of_12", "loses_power_of_two"],
        diagnostic_tags=["exponents", "advanced_prime_bases"],
        keywords=["prime bases", "composite bases", "simplify"],
    )
    return _add_pillars(q, "19_prime_base_with_fractional_composite_bases", duration=3, weight=15)


# --------------------------------------------------------------------------- #
# 20_factorise_common_power_two_terms
# --------------------------------------------------------------------------- #
def _build_20_factorise_common_power_two_terms(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    # e.g. [2^(x+1) + 2^x] / [2^x] = 2 + 1 = 3
    base_val = r.choice([2, 3, 5])
    p = r.choice([1, 2, 3])
    prompt = f"\\dfrac{{{base_val}^{{x + {p}}} + {base_val}^x}}{{{base_val}^x}}"
    ans_val = base_val**p + 1

    sol = solution(
        goal="factorise common power from sum",
        chain_type="expression",
        var="x",
        steps=[
            step(from_expr=prompt,
                 to_expr=f"\\frac{{{base_val}^x({base_val}^{{{p}}} + 1)}}{{{base_val}^x}}",
                 op=f"factor out {base_val}^x from numerator", rule="common factor in exponents"),
            step(from_expr=f"\\frac{{{base_val}^x({base_val**p} + 1)}}{{{base_val}^x}}",
                 to_expr=f"{base_val**p} + 1 = {ans_val}",
                 op=f"cancel {base_val}^x and evaluate bracket", rule="cancellation"),
        ],
        final_expr=sp.Integer(ans_val),
    )
    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Simplify: }} {prompt}",
        answer_expr=sp.Integer(ans_val),
        answer_mode="value",
        answer_latex=str(ans_val),
        marks=3,
        canonical_solution=sol,
        explanation=f"Because terms are separated by $+$, factorise ${base_val}^x$ out of the numerator: $\\dfrac{{{base_val}^x({base_val}^{{{p}}} + 1)}}{{{base_val}^x}} = {base_val**p} + 1 = {ans_val}$.",
        hint="When terms are separated by a plus sign, you MUST factorise first; you cannot cancel across addition!",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="20_factorise_common_power_two_terms",
        learning_objective_id=f"{LO}.20_factorise_common_power",
        misconception_tags=["cancels_across_addition", "forgets_one_when_factoring_entire_term"],
        diagnostic_tags=["exponents", "factorisation"],
        keywords=["factorise", "common power", "plus sign"],
    )
    return _add_pillars(q, "20_factorise_common_power_two_terms", duration=3, weight=15)


# --------------------------------------------------------------------------- #
# 21_factorise_common_power_subtraction
# --------------------------------------------------------------------------- #
def _build_21_factorise_common_power_subtraction(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    base_val = r.choice([2, 3, 5])
    p = r.choice([2, 3])
    prompt = f"\\dfrac{{{base_val}^{{x + {p}}} - {base_val}^x}}{{{base_val}^x}}"
    ans_val = base_val**p - 1

    sol = solution(
        goal="factorise common power with subtraction",
        chain_type="expression",
        var="x",
        steps=[
            step(from_expr=prompt,
                 to_expr=f"\\frac{{{base_val}^x({base_val}^{{{p}}} - 1)}}{{{base_val}^x}}",
                 op=f"factor out {base_val}^x", rule="HCF"),
            step(from_expr=f"{base_val}^{{{p}}} - 1",
                 to_expr=f"{ans_val}",
                 op="evaluate arithmetic", rule="simplify"),
        ],
        final_expr=sp.Integer(ans_val),
    )
    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Simplify: }} {prompt}",
        answer_expr=sp.Integer(ans_val),
        answer_mode="value",
        answer_latex=str(ans_val),
        marks=3,
        canonical_solution=sol,
        explanation=f"Factorise ${base_val}^x$ out: $\\dfrac{{{base_val}^x({base_val}^{{{p}}} - 1)}}{{{base_val}^x}} = {base_val**p} - 1 = {ans_val}$.",
        hint=f"Take out {base_val}^x as a common factor in the numerator.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="21_factorise_common_power_subtraction",
        learning_objective_id=f"{LO}.21_factorise_subtraction",
        misconception_tags=["cancels_across_subtraction", "sign_error_in_bracket"],
        diagnostic_tags=["exponents", "subtraction_factorisation"],
        keywords=["factorise", "common factor", "subtraction"],
    )
    return _add_pillars(q, "21_factorise_common_power_subtraction", duration=3, weight=15)


# --------------------------------------------------------------------------- #
# 22_factorise_common_power_both_numerator_denominator
# --------------------------------------------------------------------------- #
def _build_22_factorise_common_power_both_numerator_denominator(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    # e.g. [2^(x+2) - 2^x] / [2^(x+1) + 2^x]
    # = [2^x(4 - 1)] / [2^x(2 + 1)] = 3/3 = 1
    base_val = r.choice([2, 3])
    p_num = r.choice([2, 3])
    p_den = 1
    top_bracket = base_val**p_num - 1
    bot_bracket = base_val**p_den + 1
    hcf = math.gcd(top_bracket, bot_bracket)
    fin_top = top_bracket // hcf
    fin_bot = bot_bracket // hcf
    ans_frac = sp.Rational(fin_top, fin_bot)
    ans_latex = str(fin_top) if fin_bot == 1 else f"\\frac{{{fin_top}}}{{{fin_bot}}}"

    prompt = f"\\dfrac{{{base_val}^{{x + {p_num}}} - {base_val}^x}}{{{base_val}^{{x + {p_den}}} + {base_val}^x}}"

    sol = solution(
        goal="factorise common power in numerator and denominator",
        chain_type="expression",
        var="x",
        steps=[
            step(from_expr=prompt,
                 to_expr=f"\\frac{{{base_val}^x({base_val}^{{{p_num}}} - 1)}}{{{base_val}^x({base_val}^{{{p_den}}} + 1)}}",
                 op=f"factor out {base_val}^x from top and bottom", rule="common factor"),
            step(from_expr=f"\\frac{{{top_bracket}}}{{{bot_bracket}}}",
                 to_expr=ans_latex,
                 op="simplify fraction", rule="fraction reduction"),
        ],
        final_expr=ans_frac,
    )
    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Simplify: }} {prompt}",
        answer_expr=ans_frac,
        answer_mode="expression",
        answer_latex=ans_latex,
        marks=3,
        canonical_solution=sol,
        explanation=f"Factorise ${base_val}^x$ from both numerator and denominator: $\\dfrac{{{base_val}^x({top_bracket})}}{{{base_val}^x({bot_bracket})}} = \\dfrac{{{top_bracket}}}{{{bot_bracket}}} = {ans_latex}$.",
        hint="Factor out the common exponential term from both the top and the bottom.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="22_factorise_common_power_both_numerator_denominator",
        learning_objective_id=f"{LO}.22_factorise_both_num_den",
        misconception_tags=["cancels_individual_terms", "wrong_bracket_evaluation"],
        diagnostic_tags=["exponents", "numerator_denominator_factorisation"],
        keywords=["factorise", "common power", "cancel"],
    )
    return _add_pillars(q, "22_factorise_common_power_both_numerator_denominator", duration=3, weight=15)


# --------------------------------------------------------------------------- #
# 23_factorise_common_power_with_negative_exponents
# --------------------------------------------------------------------------- #
def _build_23_factorise_common_power_with_negative_exponents(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    # e.g. [5^x - 5^(x-1)] / [5^x] = [5^x(1 - 5^-1)] / [5^x] = 1 - 1/5 = 4/5
    base_val = r.choice([2, 3, 5])
    # [base^x - base^(x-1)] / base^x = 1 - 1/base = (base - 1)/base
    ans_frac = sp.Rational(base_val - 1, base_val)
    ans_latex = f"\\frac{{{base_val - 1}}}{{{base_val}}}"
    prompt = f"\\dfrac{{{base_val}^x - {base_val}^{{x - 1}}}}{{{base_val}^x}}"

    sol = solution(
        goal="factorise expression with negative exponent shift",
        chain_type="expression",
        var="x",
        steps=[
            step(from_expr=prompt,
                 to_expr=f"\\frac{{{base_val}^x(1 - {base_val}^{{-1}})}}{{{base_val}^x}}",
                 op=f"factor out {base_val}^x", rule="common factor"),
            step(from_expr=f"1 - \\frac{{1}}{{{base_val}}}",
                 to_expr=ans_latex,
                 op="subtract fractions", rule="arithmetic"),
        ],
        final_expr=ans_frac,
    )
    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Simplify: }} {prompt}",
        answer_expr=ans_frac,
        answer_mode="expression",
        answer_latex=ans_latex,
        marks=3,
        canonical_solution=sol,
        explanation=f"Factorise ${base_val}^x$ out: $\\dfrac{{{base_val}^x(1 - {base_val}^{{-1}})}}{{{base_val}^x}} = 1 - \\dfrac{{1}}{{{base_val}}} = {ans_latex}$.",
        hint=f"Rewrite {base_val}^(x - 1) as {base_val}^x * {base_val}^-1, then factor out {base_val}^x.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="23_factorise_common_power_with_negative_exponents",
        learning_objective_id=f"{LO}.23_negative_shift",
        misconception_tags=["fails_to_evaluate_negative_power", "arithmetic_error_fractions"],
        diagnostic_tags=["exponents", "negative_exponent_factorisation"],
        keywords=["factorise", "negative exponent shift", "common factor"],
    )
    return _add_pillars(q, "23_factorise_common_power_with_negative_exponents", duration=3, weight=15)


# --------------------------------------------------------------------------- #
# 24_factorise_exponential_difference_of_squares
# --------------------------------------------------------------------------- #
def _build_24_factorise_exponential_difference_of_squares(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    # e.g. [4^x - 1] / [2^x + 1] = 2^x - 1
    # or [9^x - 16] / [3^x + 4] = 3^x - 4
    base_val = r.choice([2, 3])
    b = r.choice([1, 2, 4, 5])
    comp_base = base_val**2
    prompt = f"\\dfrac{{{comp_base}^x - {b**2}}}{{{base_val}^x + {b}}}"
    ans_expr = f"{base_val}^x - {b}"

    sol = solution(
        goal="factorise difference of squares in exponential fraction",
        chain_type="expression",
        var="x",
        steps=[
            step(from_expr=prompt,
                 to_expr=f"\\frac{{({base_val}^x)^2 - ({b})^2}}{{{base_val}^x + {b}}}",
                 op=f"recognise {comp_base}^x as ({base_val}^x)^2", rule="power of a power"),
            step(from_expr=f"\\frac{{({base_val}^x - {b})({base_val}^x + {b})}}{{{base_val}^x + {b}}}",
                 to_expr=ans_expr,
                 op="cancel common bracket", rule="difference of squares"),
        ],
        final_expr=ans_expr,
    )
    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Simplify: }} {prompt}",
        answer_expr=ans_expr,
        answer_mode="expression",
        answer_latex=ans_expr,
        marks=3,
        canonical_solution=sol,
        explanation=f"Recognise ${comp_base}^x = ({base_val}^x)^2$. Factorise the numerator as a difference of two squares: $({base_val}^x - {b})({base_val}^x + {b})$. Cancelling leaves ${ans_expr}$.",
        hint=f"Notice that {comp_base}^x = ({base_val}^x)^2. Apply difference of two squares to the top.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="24_factorise_exponential_difference_of_squares",
        learning_objective_id=f"{LO}.24_exponential_diff_squares",
        misconception_tags=["fails_to_recognise_squared_base", "cancels_terms_directly"],
        diagnostic_tags=["exponents", "difference_of_squares"],
        keywords=["difference of squares", "exponential", "factorise"],
    )
    return _add_pillars(q, "24_factorise_exponential_difference_of_squares", duration=3, weight=15)


# --------------------------------------------------------------------------- #
# 25_factorise_exponential_trinomial_cancel
# --------------------------------------------------------------------------- #
def _build_25_factorise_exponential_trinomial_cancel(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    # e.g. [2^(2x) - 5*2^x + 6] / [2^x - 2] = 2^x - 3
    base_val = r.choice([2, 3])
    p = r.randint(1, 4)
    q_val = r.randint(1, 4)
    # (k - p)(k - q) = k^2 - (p+q)k + pq where k = base_val^x
    b_coeff = p + q_val
    c_const = p * q_val
    prompt = f"\\dfrac{{{base_val}^{{2x}} - {b_coeff} \\cdot {base_val}^x + {c_const}}}{{{base_val}^x - {p}}}"
    ans_expr = f"{base_val}^x - {q_val}"

    sol = solution(
        goal="factorise exponential quadratic trinomial",
        chain_type="expression",
        var="x",
        steps=[
            step(from_expr=prompt,
                 to_expr=f"\\text{{Let }} k = {base_val}^x \\implies \\frac{{k^2 - {b_coeff}k + {c_const}}}{{k - {p}}}",
                 op="use k-substitution", rule="substitution"),
            step(from_expr=f"\\frac{{(k - {p})(k - {q_val})}}{{k - {p}}}",
                 to_expr=f"k - {q_val} = {ans_expr}",
                 op=f"factorise trinomial and substitute back k = {base_val}^x", rule="cancellation"),
        ],
        final_expr=ans_expr,
    )
    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Simplify: }} {prompt}",
        answer_expr=ans_expr,
        answer_mode="expression",
        answer_latex=ans_expr,
        marks=3,
        canonical_solution=sol,
        explanation=f"Let $k = {base_val}^x$. The numerator is $k^2 - {b_coeff}k + {c_const} = (k - {p})(k - {q_val})$. Cancelling $(k - {p})$ leaves $k - {q_val} = {ans_expr}$.",
        hint=f"Use k-substitution: let k = {base_val}^x and factorise the quadratic trinomial.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="25_factorise_exponential_trinomial_cancel",
        learning_objective_id=f"{LO}.25_exponential_trinomial",
        misconception_tags=["confuses_exponential_with_linear", "trinomial_sign_error"],
        diagnostic_tags=["exponents", "quadratic_substitution"],
        keywords=["k-substitution", "trinomial", "exponential fraction"],
    )
    return _add_pillars(q, "25_factorise_exponential_trinomial_cancel", duration=3, weight=15)


BUILDERS_01_25: Dict[str, Any] = {
    "01_meaning_of_exponential_notation": _build_01_meaning_of_exponential_notation,
    "02_zero_exponent_law_numerical": _build_02_zero_exponent_law_numerical,
    "03_zero_exponent_law_algebraic": _build_03_zero_exponent_law_algebraic,
    "04_negative_exponent_law_numerical": _build_04_negative_exponent_law_numerical,
    "05_negative_exponent_law_algebraic": _build_05_negative_exponent_law_algebraic,
    "06_product_rule_same_base_numerical": _build_06_product_rule_same_base_numerical,
    "07_product_rule_same_base_algebraic": _build_07_product_rule_same_base_algebraic,
    "08_quotient_rule_same_base_numerical": _build_08_quotient_rule_same_base_numerical,
    "09_quotient_rule_same_base_algebraic": _build_09_quotient_rule_same_base_algebraic,
    "10_power_of_a_power_rule": _build_10_power_of_a_power_rule,
    "11_power_of_a_product_rule": _build_11_power_of_a_product_rule,
    "12_power_of_a_quotient_rule": _build_12_power_of_a_quotient_rule,
    "13_combine_monomial_exponent_laws_basic": _build_13_combine_monomial_exponent_laws_basic,
    "14_combine_monomial_exponent_laws_advanced": _build_14_combine_monomial_exponent_laws_advanced,
    "15_scientific_notation_standard_form": _build_15_scientific_notation_standard_form,
    "16_prime_base_factorisation_numerical": _build_16_prime_base_factorisation_numerical,
    "17_prime_base_algebraic_exponents_single_var": _build_17_prime_base_algebraic_exponents_single_var,
    "18_prime_base_algebraic_exponents_two_bases": _build_18_prime_base_algebraic_exponents_two_bases,
    "19_prime_base_with_fractional_composite_bases": _build_19_prime_base_with_fractional_composite_bases,
    "20_factorise_common_power_two_terms": _build_20_factorise_common_power_two_terms,
    "21_factorise_common_power_subtraction": _build_21_factorise_common_power_subtraction,
    "22_factorise_common_power_both_numerator_denominator": _build_22_factorise_common_power_both_numerator_denominator,
    "23_factorise_common_power_with_negative_exponents": _build_23_factorise_common_power_with_negative_exponents,
    "24_factorise_exponential_difference_of_squares": _build_24_factorise_exponential_difference_of_squares,
    "25_factorise_exponential_trinomial_cancel": _build_25_factorise_exponential_trinomial_cancel,
}
