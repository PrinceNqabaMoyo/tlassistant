"""Grade 10 Mathematics — Term 1 — Exponents (deterministic, SymPy-backed).

Curriculum source: ``curriculum_docs/Mathematics_Gr10/Term 1/2 Exponents .md``

Subskills:
    zero_negative_exponents   math_short    a^0=1, a^{-n}=1/a^n
    laws_monomial             math_short    product/quotient/power on monomials
    laws_with_brackets        math_short    (ab)^n, (a/b)^n, nested powers
    prime_base_simplify       math_short    rewrite composite bases, then simplify
    common_factor_exponents   math_short    factor a^t out of sums, cancel
    difference_of_squares_exp math_short    9^x-1 = (3^x)^2-1 factorise
    rational_exponents        math_short    a^{1/n}, roots, mixed
    exponential_equations     math_steps    equate bases & solve
"""
from __future__ import annotations

from typing import Any, Dict

import sympy as sp

from app.utils.grade10_mathematics._math_common import (
    build_generate,
    make_short,
    make_steps,
    nonzero,
    solution,
    step,
    to_latex,
    with_metadata,
)

TOPIC = "grade10_math_exponents"
LO = "math10_exponents"


def _prime_base_map():
    return {
        4: (2, 2), 8: (2, 3), 9: (3, 2), 16: (2, 4), 25: (5, 2),
        27: (3, 3), 32: (2, 5), 36: (6, 2), 49: (7, 2), 64: (2, 6),
        81: (3, 4), 100: (10, 2), 125: (5, 3), 128: (2, 7),
    }


# --------------------------------------------------------------------------- #
# zero_negative_exponents
# --------------------------------------------------------------------------- #
def _build_zero_negative_exponents(r, difficulty: str) -> Dict[str, Any]:
    case = r.choice(["zero", "negative_simple", "negative_fraction", "zero_with_coeff"])
    if case == "zero":
        base = r.choice([2, 3, 5, 7, 10, 11, 13])
        expr = sp.Pow(base, 0)
        ans = sp.Integer(1)
        steps = [step(from_expr=expr, to_expr=ans, op="apply zero exponent", rule="a^0 = 1",
                      common_errors=["zero_exponent"])]
    elif case == "negative_simple":
        base = r.choice([2, 3, 5, 10])
        exp = r.randint(1, 4)
        expr = sp.Pow(base, -exp)
        ans = sp.Pow(base, exp)
        steps = [step(from_expr=expr, to_expr=ans, op="rewrite negative exponent",
                      rule="a^{-n} = 1/a^n", common_errors=["negative_exponent_sign"])]
    elif case == "negative_fraction":
        base = r.choice([2, 3, 5])
        exp = r.choice([2, 3])
        expr = sp.Pow(sp.Rational(1, base), -exp)
        ans = sp.Pow(base, exp)
        steps = [step(from_expr=expr, to_expr=ans, op="rewrite negative exponent",
                      rule="(1/a)^{-n} = a^n", common_errors=["negative_exponent_sign"])]
    else:
        coeff = r.randint(2, 9)
        base = r.choice([2, 3, 5])
        var = sp.Symbol(r.choice(["a", "b", "x", "p"]))
        expr = coeff * var * sp.Pow(base, 0)
        ans = coeff * var
        steps = [step(from_expr=expr, to_expr=ans, op="apply zero exponent", rule="a^0 = 1",
                      common_errors=["zero_exponent"])]
    sol = solution(goal="simplify", chain_type="expression", var="x", steps=steps, final_expr=ans)
    q = make_short(prefix=TOPIC, prompt_latex=f"\\text{{Simplify: }} {to_latex(expr)}",
                   answer_expr=ans, answer_mode="expression_positive_exponents", marks=1,
                   canonical_solution=sol,
                   explanation="Any non-zero number raised to the power 0 equals 1. A negative exponent means take the reciprocal.",
                   hint="Remember: a^0 = 1 and a^{-n} = 1/a^n.")
    return with_metadata(q, topic=TOPIC, subskill="zero_negative_exponents",
                         learning_objective_id=f"{LO}.zero_negative",
                         misconception_tags=["zero_exponent", "negative_exponent_sign"],
                         diagnostic_tags=["exponent_rules", "negative_exponents"])


# --------------------------------------------------------------------------- #
# laws_monomial
# --------------------------------------------------------------------------- #
def _build_laws_monomial(r, difficulty: str) -> Dict[str, Any]:
    law = r.choice(["product", "quotient", "power", "product_quotient_mix"])
    var = sp.Symbol(r.choice(["x", "y", "t", "p"]))
    if law == "product":
        a = nonzero(r, 2, 9)
        b = nonzero(r, 2, 9)
        m = nonzero(r, 1, 5)
        n = nonzero(r, 1, 5)
        expr = (a * sp.Pow(var, m)) * (b * sp.Pow(var, n))
        ans = sp.simplify(expr)
        steps = [step(from_expr=expr, to_expr=ans, op="multiply coefficients, add exponents",
                      rule="a^m · a^n = a^{m+n}", common_errors=["multiply_instead_of_add_exponents"])]
    elif law == "quotient":
        a = r.randint(2, 12)
        divisors = [d for d in range(2, 13) if a % d == 0]
        b = r.choice(divisors) if divisors else 2
        m = nonzero(r, 2, 6)
        n = nonzero(r, 1, m - 1)
        expr = (a * sp.Pow(var, m)) / (b * sp.Pow(var, n))
        ans = sp.simplify(expr)
        steps = [step(from_expr=expr, to_expr=ans, op="divide coefficients, subtract exponents",
                      rule="a^m / a^n = a^{m-n}", common_errors=["subtract_wrong_direction"])]
    elif law == "power":
        a = nonzero(r, 2, 5)
        m = nonzero(r, 1, 4)
        n = nonzero(r, 2, 4)
        expr = sp.Pow(a * sp.Pow(var, m), n)
        ans = sp.simplify(expr)
        steps = [step(from_expr=expr, to_expr=ans, op="power of a product",
                      rule="(ab)^n = a^n b^n", common_errors=["distribute_power_over_sum", "coefficient_raised_wrongly"])]
    else:
        v1 = sp.Symbol(r.choice(["x", "a", "p"]))
        v2 = sp.Symbol(r.choice(["y", "b", "q"]))
        c1 = nonzero(r, 2, 8)
        c2 = nonzero(r, 2, 8)
        e1 = nonzero(r, 1, 5)
        e3 = nonzero(r, 1, 4)
        expr = (c1 * sp.Pow(v1, e1)) * (c2 * sp.Pow(v1, 1) * sp.Pow(v2, e3))
        ans = sp.simplify(expr)
        steps = [step(from_expr=expr, to_expr=ans, op="multiply coefficients, add exponents for each variable",
                      rule="a^m · a^n = a^{m+n}", common_errors=["multiply_instead_of_add_exponents"])]
    sol = solution(goal="simplify using exponent laws", chain_type="expression", var=str(var), steps=steps, final_expr=ans)
    q = make_short(prefix=TOPIC, prompt_latex=f"\\text{{Simplify: }} {to_latex(expr)}",
                   answer_expr=ans, answer_mode="expression_positive_exponents", marks=2, canonical_solution=sol,
                   explanation="Apply the product, quotient, and power laws of exponents.",
                   hint="When multiplying with the same base, add the exponents.")
    return with_metadata(q, topic=TOPIC, subskill="laws_monomial",
                         learning_objective_id=f"{LO}.laws_monomial",
                         misconception_tags=["multiply_instead_of_add_exponents", "subtract_wrong_direction", "coefficient_raised_wrongly"],
                         diagnostic_tags=["exponent_laws", "monomials"])


# --------------------------------------------------------------------------- #
# laws_with_brackets
# --------------------------------------------------------------------------- #
def _build_laws_with_brackets(r, difficulty: str) -> Dict[str, Any]:
    law = r.choice(["nested_power", "product_in_bracket", "quotient_in_bracket"])
    var = sp.Symbol(r.choice(["x", "a", "p"]))
    if law == "nested_power":
        base = nonzero(r, 2, 5)
        outer = nonzero(r, 2, 3)
        symbol = sp.Symbol(r.choice(["n", "x", "t"]))
        inner_exp = base * symbol + nonzero(r, 1, 5)
        expr = sp.Pow(sp.Pow(base, inner_exp), outer)
        ans = sp.simplify(expr)
        steps = [step(from_expr=expr, to_expr=ans, op="power of a power", rule="(a^m)^n = a^{mn}",
                      common_errors=["multiply_instead_of_add_exponents"])]
    elif law == "product_in_bracket":
        coeff = nonzero(r, 2, 6)
        var_pow = nonzero(r, 1, 4)
        outer = nonzero(r, 2, 4)
        expr = sp.Pow(coeff * sp.Pow(var, var_pow), outer)
        ans = sp.simplify(expr)
        steps = [step(from_expr=expr, to_expr=ans, op="distribute power over product", rule="(ab)^n = a^n b^n",
                      common_errors=["coefficient_raised_wrongly", "distribute_power_over_sum"])]
    else:
        num_exp = nonzero(r, 3, 8)
        den_exp = nonzero(r, 3, 8)
        outer = nonzero(r, 2, 4)
        v1 = sp.Symbol(r.choice(["x", "a"]))
        v2 = sp.Symbol(r.choice(["y", "b"]))
        expr = sp.Pow(sp.Pow(v1, num_exp) / sp.Pow(v2, den_exp), outer)
        ans = sp.simplify(expr)
        steps = [step(from_expr=expr, to_expr=ans, op="power of a quotient", rule="(a/b)^n = a^n/b^n",
                      common_errors=["distribute_power_over_sum"])]
    sol = solution(goal="simplify bracketed powers", chain_type="expression", var=str(var), steps=steps, final_expr=ans)
    q = make_short(prefix=TOPIC, prompt_latex=f"\\text{{Simplify: }} {to_latex(expr)}",
                   answer_expr=ans, answer_mode="expression_positive_exponents", marks=2, canonical_solution=sol,
                   explanation="Apply the power of a product and power of a quotient laws.",
                   hint="Every factor inside the bracket is raised to the outer power.")
    return with_metadata(q, topic=TOPIC, subskill="laws_with_brackets",
                         learning_objective_id=f"{LO}.laws_brackets",
                         misconception_tags=["distribute_power_over_sum", "coefficient_raised_wrongly"],
                         diagnostic_tags=["exponent_laws", "brackets"])


# --------------------------------------------------------------------------- #
# prime_base_simplify
# --------------------------------------------------------------------------- #
def _build_prime_base_simplify(r, difficulty: str) -> Dict[str, Any]:
    pmap = _prime_base_map()
    composites = list(pmap.keys())
    style = r.choice(["single_base", "mixed_bases_quotient", "mixed_bases_product"])
    symbol = sp.Symbol(r.choice(["n", "x", "t"]))
    if style == "single_base":
        prime = r.choice([2, 3, 5])
        candidates = [c for c in composites if pmap[c][0] == prime]
        comp1, comp2 = r.sample(candidates, 2)
        pw1, pw2 = pmap[comp1][1], pmap[comp2][1]
        a = nonzero(r, 1, 3)
        b = nonzero(r, 1, 2)
        c = nonzero(r, 1, 3)
        expr = (sp.Pow(prime, a * symbol) * sp.Pow(comp1, b * symbol) * prime) / sp.Pow(comp2, c * symbol)
        ans = sp.simplify(expr)
        steps = [
            step(from_expr=expr, to_expr=None, op="rewrite composite bases to prime bases",
                 rule=f"{comp1}={prime}^{pw1}, {comp2}={prime}^{pw2}", common_errors=["forget_to_rewrite_base"]),
            step(from_expr=None, to_expr=ans, op="apply exponent laws",
                 rule="a^m·a^n=a^{{m+n}}; a^m/a^n=a^{{m-n}}", common_errors=["multiply_instead_of_add_exponents"]),
        ]
    elif style == "mixed_bases_quotient":
        prime1 = r.choice([3, 5])
        prime2 = r.choice([2, 3, 5])
        while prime2 == prime1:
            prime2 = r.choice([2, 3, 5])
        comp1 = prime1 ** 2
        comp2 = prime1 * prime2
        expr = (sp.Pow(prime1, 2 * symbol - 1) * sp.Pow(comp1, symbol - 2)) / sp.Pow(comp2, 2 * symbol - 3)
        ans = sp.simplify(expr)
        steps = [
            step(from_expr=expr, to_expr=None, op="rewrite composite bases to prime bases",
                 rule="factorise all bases into primes", common_errors=["forget_to_rewrite_base"]),
            step(from_expr=None, to_expr=ans, op="simplify using exponent laws",
                 rule="subtract exponents for same bases", common_errors=["subtract_wrong_direction"]),
        ]
    else:
        comp = r.choice(composites)
        prime, pw = pmap[comp]
        c1 = nonzero(r, 1, 3)
        c2 = nonzero(r, 1, 3)
        expr = sp.Pow(comp, c1 * symbol) * sp.Pow(prime, c2 * symbol)
        ans = sp.simplify(expr)
        steps = [step(from_expr=expr, to_expr=ans, op=f"rewrite {comp} as {prime}^{pw}",
                      rule="(a^m)^n = a^{mn}", common_errors=["forget_to_rewrite_base"])]
    sol = solution(goal="simplify by rewriting to prime bases", chain_type="expression", var="x", steps=steps, final_expr=ans)
    q = make_short(prefix=TOPIC, prompt_latex=f"\\text{{Simplify: }} {to_latex(expr)}",
                   answer_expr=ans, answer_mode="expression_positive_exponents", marks=3, canonical_solution=sol,
                   explanation="Rewrite all composite bases as powers of prime numbers, then apply exponent laws.",
                   hint="Break each base down into its prime factors first.")
    return with_metadata(q, topic=TOPIC, subskill="prime_base_simplify",
                         learning_objective_id=f"{LO}.prime_bases",
                         misconception_tags=["forget_to_rewrite_base", "multiply_instead_of_add_exponents"],
                         diagnostic_tags=["prime_bases", "exponent_laws"])


# --------------------------------------------------------------------------- #
# common_factor_exponents
# --------------------------------------------------------------------------- #
def _build_common_factor_exponents(r, difficulty: str) -> Dict[str, Any]:
    base = r.choice([2, 3, 5])
    symbol = sp.Symbol(r.choice(["t", "x", "n"]))
    a = nonzero(r, 1, 3)
    c1 = nonzero(r, 2, 5)
    c2 = nonzero(r, 1, c1 - 1)
    num_expr = sp.Pow(base, symbol) - sp.Pow(base, symbol - a)
    den_expr = c1 * sp.Pow(base, symbol) - c2 * sp.Pow(base, symbol)
    expr = num_expr / den_expr
    ans = sp.simplify(expr)
    steps = [
        step(from_expr=expr, to_expr=None, op="factor out common power from numerator",
             rule=f"factor out {base}^{symbol}", common_errors=["forget_common_factor"]),
        step(from_expr=None, to_expr=ans, op="cancel common factor and simplify",
             rule="divide numerator and denominator by the common factor", common_errors=["cancels_terms_not_factors"]),
    ]
    sol = solution(goal="factor and simplify", chain_type="expression", var=str(symbol), steps=steps, final_expr=ans)
    q = make_short(prefix=TOPIC, prompt_latex=f"\\text{{Simplify: }} \\dfrac{{{to_latex(num_expr)}}}{{{to_latex(den_expr)}}}",
                   answer_expr=ans, answer_mode="expression_positive_exponents", marks=3, canonical_solution=sol,
                   explanation="Factor out the common exponential term, then cancel it from numerator and denominator.",
                   hint="Look for the lowest power of the common base to factor out.")
    return with_metadata(q, topic=TOPIC, subskill="common_factor_exponents",
                         learning_objective_id=f"{LO}.common_factor",
                         misconception_tags=["forget_common_factor", "cancels_terms_not_factors"],
                         diagnostic_tags=["factorisation", "exponents"])


# --------------------------------------------------------------------------- #
# difference_of_squares_exp
# --------------------------------------------------------------------------- #
def _build_difference_of_squares_exp(r, difficulty: str) -> Dict[str, Any]:
    inner = r.choice([2, 3, 4, 5])
    outer = inner ** 2
    symbol = sp.Symbol(r.choice(["x", "t", "n"]))
    style = r.choice(["direct", "fraction"])
    if style == "direct":
        expr = sp.Pow(outer, symbol) - 1
        inner_pow = sp.Pow(inner, symbol)
        ans = (inner_pow - 1) * (inner_pow + 1)
        steps = [step(from_expr=expr, to_expr=ans, op="rewrite as difference of squares",
                      rule=f"{outer}^x = ({inner}^x)^2", common_errors=["treats_as_sum_of_squares"])]
        prompt = f"\\text{{Factorise: }} {to_latex(expr)}"
        mode = "factored"
    else:
        expr = (sp.Pow(outer, symbol) - 1) / (sp.Pow(inner, symbol) + 1)
        ans = sp.Pow(inner, symbol) - 1
        steps = [
            step(from_expr=expr, to_expr=None, op="factorise numerator as difference of squares",
                 rule="a^2 - b^2 = (a-b)(a+b)", common_errors=["treats_as_sum_of_squares"]),
            step(from_expr=None, to_expr=ans, op="cancel common factor",
                 rule="divide by common factor", common_errors=["cancels_terms_not_factors"]),
        ]
        prompt = f"\\text{{Simplify: }} {to_latex(expr)}"
        mode = "expression_positive_exponents"
    sol = solution(goal="factorise using difference of squares", chain_type="expression", var=str(symbol), steps=steps, final_expr=ans)
    q = make_short(prefix=TOPIC, prompt_latex=prompt, answer_expr=ans, answer_mode=mode, marks=2, canonical_solution=sol,
                   explanation=f"Rewrite {outer}^x as ({inner}^x)^2, then apply difference of two squares.",
                   hint=f"Notice that {outer}^x = ({inner}^2)^x = ({inner}^x)^2.")
    return with_metadata(q, topic=TOPIC, subskill="difference_of_squares_exp",
                         learning_objective_id=f"{LO}.diff_squares_exp",
                         misconception_tags=["treats_as_sum_of_squares", "cancels_terms_not_factors"],
                         diagnostic_tags=["factorisation", "difference_of_squares"])


# --------------------------------------------------------------------------- #
# rational_exponents
# --------------------------------------------------------------------------- #
def _build_rational_exponents(r, difficulty: str) -> Dict[str, Any]:
    style = r.choice(["product", "power_of_power", "numeric_root", "mixed"])
    if style == "product":
        coeff1 = nonzero(r, 1, 5)
        coeff2 = nonzero(r, 1, 5)
        var = sp.Symbol(r.choice(["x", "a", "t"]))
        num = nonzero(r, 1, 4)
        den = r.choice([2, 3, 4])
        expr = (coeff1 * sp.Pow(var, sp.Rational(num, den))) * (coeff2 * sp.Pow(var, sp.Rational(-num, den)))
        ans = sp.simplify(expr)
        steps = [step(from_expr=expr, to_expr=ans, op="add exponents", rule="a^m · a^n = a^{m+n}",
                      common_errors=["multiply_instead_of_add_exponents"])]
    elif style == "power_of_power":
        base = r.choice([27, 8, 16, 32, 64])
        den = r.choice([2, 3])
        sign = r.choice([1, -1])
        expr = sp.Pow(base, sp.Rational(sign, den))
        ans = sp.simplify(expr)
        steps = [step(from_expr=expr, to_expr=ans, op="evaluate fractional power", rule="a^{1/n} = \\sqrt[n]{a}",
                      common_errors=["negative_exponent_sign"])]
    elif style == "numeric_root":
        base = sp.Rational(r.choice([1, 2, 4, 8]), r.choice([1, 10, 100, 1000]))
        den = r.choice([2, 3])
        expr = sp.Pow(base, sp.Rational(1, den))
        ans = sp.simplify(expr)
        steps = [step(from_expr=expr, to_expr=ans, op="rewrite as root and simplify",
                      rule="a^{1/n} = \\sqrt[n]{a}", common_errors=["negative_exponent_sign"])]
    else:
        coeff = nonzero(r, 2, 5)
        var = sp.Symbol(r.choice(["x", "a"]))
        p = nonzero(r, 1, 3)
        q = nonzero(r, 1, 3)
        expr = (coeff * sp.Pow(var, sp.Rational(p, q))) * sp.Pow(var, sp.Rational(-p, q))
        ans = sp.simplify(expr)
        steps = [step(from_expr=expr, to_expr=ans, op="add exponents", rule="a^m · a^n = a^{m+n}",
                      common_errors=["multiply_instead_of_add_exponents"])]
    sol = solution(goal="simplify rational exponents", chain_type="expression", var="x", steps=steps, final_expr=ans)
    q = make_short(prefix=TOPIC, prompt_latex=f"\\text{{Simplify: }} {to_latex(expr)}",
                   answer_expr=ans, answer_mode="expression_positive_exponents", marks=2, canonical_solution=sol,
                   explanation="Use a^{1/n} = nth root. When multiplying same base, add exponents.",
                   hint="Fractional exponent means a root. Negative exponent means a reciprocal.")
    return with_metadata(q, topic=TOPIC, subskill="rational_exponents",
                         learning_objective_id=f"{LO}.rational_exponents",
                         misconception_tags=["negative_exponent_sign", "multiply_instead_of_add_exponents"],
                         diagnostic_tags=["rational_exponents", "roots"])


# --------------------------------------------------------------------------- #
# exponential_equations
# --------------------------------------------------------------------------- #
def _build_exponential_equations(r, difficulty: str) -> Dict[str, Any]:
    eq_type = r.choice(["same_base_simple", "different_base_rewritable", "common_factor", "quadratic_in_disguise"])
    symbol = sp.Symbol(r.choice(["x", "t", "y"]))
    if eq_type == "same_base_simple":
        base = r.choice([2, 3, 5])
        rhs_exp = r.randint(2, 5)
        lhs_shift = nonzero(r, 1, 3)
        lhs_const = nonzero(r, 1, 5)
        lhs_exp = lhs_shift * symbol + lhs_const
        rhs_val = sp.Pow(base, rhs_exp)
        expr = sp.Eq(sp.Pow(base, lhs_exp), rhs_val)
        ans = sp.solve(expr, symbol)[0]
        steps = [
            step(from_expr=expr, to_expr=None, op="rewrite RHS as power of same base",
                 rule=f"{rhs_val} = {base}^{rhs_exp}", common_errors=["forget_to_rewrite_base"]),
            step(from_expr=None, to_expr=sp.Eq(lhs_exp, rhs_exp), op="equate exponents",
                 rule="if a^m = a^n then m = n", common_errors=["subtract_wrong_direction"]),
            step(from_expr=sp.Eq(lhs_exp, rhs_exp), to_expr=sp.Eq(symbol, ans), op="solve for x",
                 rule="linear equation", common_errors=["sign_error"]),
        ]
    elif eq_type == "different_base_rewritable":
        base = r.choice([2, 3, 5])
        p1 = r.choice([2, 3, 4, 5, 6])
        p2 = r.choice([2, 3, 4, 5, 6])
        while p2 == p1:
            p2 = r.choice([2, 3, 4, 5, 6])
        lhs_base = base ** p1
        rhs_base = base ** p2
        a = nonzero(r, 1, 3)
        b = nonzero(r, 1, 5)
        c = nonzero(r, 1, 3)
        d = nonzero(r, 1, 5)
        expr = sp.Eq(sp.Pow(lhs_base, a * symbol + b), sp.Pow(rhs_base, c * symbol + d))
        ans = sp.solve(expr, symbol)[0]
        steps = [
            step(from_expr=expr, to_expr=None, op=f"rewrite both sides as powers of {base}",
                 rule=f"{lhs_base}={base}^{p1}, {rhs_base}={base}^{p2}", common_errors=["forget_to_rewrite_base"]),
            step(from_expr=None, to_expr=sp.Eq(p1 * (a * symbol + b), p2 * (c * symbol + d)),
                 op="equate exponents", rule="(a^m)^n = a^{mn}", common_errors=["multiply_instead_of_add_exponents"]),
            step(from_expr=sp.Eq(p1 * (a * symbol + b), p2 * (c * symbol + d)),
                 to_expr=sp.Eq(symbol, ans), op="solve linear equation", rule="linear equation", common_errors=["sign_error"]),
        ]
    elif eq_type == "common_factor":
        base = r.choice([2, 3, 5])
        c1 = nonzero(r, 1, 5)
        c2 = nonzero(r, 2, 6)
        rhs = (1 + c1 * base) * base ** c2
        expr = sp.Eq(sp.Pow(base, symbol) + c1 * sp.Pow(base, symbol + 1), rhs)
        ans = sp.Integer(c2)
        factored = sp.Eq(sp.Pow(base, symbol) * (1 + c1 * base), rhs)
        steps = [
            step(from_expr=expr, to_expr=factored, op="factor out common power",
                 rule=f"factor out {base}^{symbol}", common_errors=["forget_common_factor"]),
            step(from_expr=factored, to_expr=sp.Eq(sp.Pow(base, symbol), sp.Pow(base, c2)), op="simplify",
                 rule=f"divide both sides by {1 + c1 * base}", common_errors=["sign_error"]),
            step(from_expr=sp.Eq(sp.Pow(base, symbol), sp.Pow(base, c2)),
                 to_expr=sp.Eq(symbol, ans), op="equate exponents",
                 rule="if a^m = a^n then m = n", common_errors=["subtract_wrong_direction"]),
        ]
    else:
        u = sp.Symbol("u")
        root1 = nonzero(r, 2, 9)
        root2 = nonzero(r, 2, 9)
        while root2 == root1:
            root2 = nonzero(r, 2, 9)
        sum_roots = root1 + root2
        prod_roots = root1 * root2
        expr = sp.Eq(symbol - sum_roots * sp.Pow(symbol, sp.Rational(1, 2)) + prod_roots, 0)
        ans = sp.FiniteSet(root1 ** 2, root2 ** 2)
        steps = [
            step(from_expr=expr, to_expr=None, op="substitute u for the square root",
                 rule=f"let u = {symbol}^{{1/2}}, so u^2 = {symbol}", common_errors=["forget_substitution"]),
            step(from_expr=None, to_expr=sp.Eq(u ** 2 - sum_roots * u + prod_roots, 0),
                 op="rewrite as quadratic in u", rule="u^2 - Su + P = 0", common_errors=["sign_error"]),
            step(from_expr=sp.Eq(u ** 2 - sum_roots * u + prod_roots, 0), to_expr=None,
                 op="factorise quadratic", rule="(u-r1)(u-r2)=0", common_errors=["wrong_factors"]),
            step(from_expr=None, to_expr=ans, op="solve and square back",
                 rule=f"{symbol} = u^2", common_errors=["forget_to_square_back"]),
        ]
    sol = solution(goal="solve exponential equation", chain_type="equation", var=str(symbol), steps=steps, final_expr=ans)
    q = make_steps(prefix=TOPIC, prompt_latex=f"\\text{{Solve for {str(symbol)}: }} {to_latex(expr)}",
                   canonical_solution=sol, marks=4,
                   explanation="Rewrite both sides with the same base, then equate the exponents.",
                   hint="Express every term as a power of the same prime base.")
    return with_metadata(q, topic=TOPIC, subskill="exponential_equations",
                         learning_objective_id=f"{LO}.exp_equations",
                         misconception_tags=["forget_to_rewrite_base", "forget_common_factor", "forget_to_square_back"],
                         diagnostic_tags=["exponential_equations", "equate_bases"])


# --------------------------------------------------------------------------- #
# Dispatcher
# --------------------------------------------------------------------------- #
generate = build_generate(
    {
        "zero_negative_exponents": _build_zero_negative_exponents,
        "laws_monomial": _build_laws_monomial,
        "laws_with_brackets": _build_laws_with_brackets,
        "prime_base_simplify": _build_prime_base_simplify,
        "common_factor_exponents": _build_common_factor_exponents,
        "difference_of_squares_exp": _build_difference_of_squares_exp,
        "rational_exponents": _build_rational_exponents,
        "exponential_equations": _build_exponential_equations,
    },
    default_subskill="zero_negative_exponents",
)
