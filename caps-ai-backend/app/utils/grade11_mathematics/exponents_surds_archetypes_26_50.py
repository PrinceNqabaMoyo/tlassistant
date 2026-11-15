"""Grade 11 Mathematics — Exponents and Surds Archetypes 26–50.
Grounded in South African National Curriculum Standards for Grade 11 Mathematics (Term 1).
Reference: curriculum_docs_auto/Mathematics_Gr11/Term 1/01. Exponents and surds.md

Covers Archetypes 26–50:
- 26–29: Exponential equations: equal bases, prime base reduction, fractional powers (positive & negative)
- 30–31: Exponential equations with addition/subtraction: common factor extraction
- 32–34: Exponential equations with quadratic structure (k-substitution, extraneous non-positive base roots)
- 35–39: Surd equations: isolated single radical, isolate before squaring, linear RHS with extraneous root rejection, verification
- 40–42: Surd equations with k-substitution, quadratic radicand, and two radicals
- 43–44: Real number conditions (undefined/non-real fractions and surds) & nature of roots discriminant connection
- 45–48: Exponential applications: population growth, reducing-balance decay, radioactive half-life, bacterial doubling
- 49–50: Advanced surd simplification (nested radicals) & comprehensive synthesis
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional
import sympy as sp

from app.utils.grade11_mathematics._math_common import (
    make_math_question,
    step,
    solution_graph,
    num,
    to_latex,
    nonzero,
)

TOPIC = "Exponents and surds"
LO_PREFIX = "math11_exp_surds"


# ---------------------------------------------------------------------------
# 26. Exponential Equation: Equal Bases
# ---------------------------------------------------------------------------
def build_26_exponential_equation_equal_bases(r: random.Random) -> Dict[str, Any]:
    base = r.choice([2, 3, 5, 7])
    a = r.randint(1, 5)
    c = r.randint(6, 12)
    x_val = c - a

    eq_latex = f"{base}^{{x + {a}}} = {base}^{{{c}}}"
    prompt = f"Solve for $x$:\n\n$${eq_latex}$$"

    sol = solution_graph(
        goal="Solve exponential equation with equal bases",
        chain_type="equation",
        var="x",
        steps=[
            step(from_latex=eq_latex, to_latex_str=f"x + {a} = {c}", op="Equate exponents since bases are equal", rule="If b^u = b^v then u = v"),
            step(from_latex=f"x = {c} - {a}", to_latex_str=f"x = {x_val}", op=f"Subtract {a}", rule="Linear solve"),
        ],
        final_latex=str(x_val),
    )

    return make_math_question(
        prefix="g11_exp",
        topic=TOPIC,
        subskill="26_exponential_equation_equal_bases",
        learning_objective_id=f"{LO_PREFIX}_26",
        prompt=prompt,
        prompt_latex=prompt,
        answer_mode="typed",
        question_type="math_short",
        answer_latex=str(x_val),
        answer_sympy=str(x_val),
        sample_answer=str(x_val),
        canonical_solution=sol,
        marking_schema={"total_marks": 2, "steps": [{"desc": "Equate exponents", "marks": 1}, {"desc": "Solve for x", "marks": 1}]},
        hints={"nudge": "Since the bases are identical, equate the exponents.", "concept": "If b^M = b^N then M = N.", "breakdown": f"x + {a} = {c} \\implies x = {x_val}."},
        misconception_tags=["dividing_by_base_instead_of_equating_exponents"],
        term=1,
        caps_weight_percent=15,
        suggested_duration_mins=3,
        difficulty="easy",
    )


# ---------------------------------------------------------------------------
# 27. Exponential Equation: Prime Base Reduction
# ---------------------------------------------------------------------------
def build_27_exponential_equation_prime_base_reduction(r: random.Random) -> Dict[str, Any]:
    prime = r.choice([2, 3, 5])
    p = r.choice([3, 4, 5]) if prime == 2 else r.choice([3, 4])
    rhs_val = prime ** p
    c_int = r.choice([1, 3])
    if (p + c_int) % 2 == 0:
        x_val = (p + c_int) // 2
        sign_str = "-"
    else:
        x_val = (p - c_int) // 2
        sign_str = "+"

    eq_latex = f"{prime}^{{2x {sign_str} {c_int}}} = {rhs_val}"
    prompt = f"Solve for $x$ without a calculator:\n\n$${eq_latex}$$"

    sol = solution_graph(
        goal="Solve exponential equation via prime base reduction",
        chain_type="equation",
        var="x",
        steps=[
            step(from_latex=eq_latex, to_latex_str=f"{prime}^{{2x {sign_str} {c_int}}} = {prime}^{{{p}}}", op=f"Express {rhs_val} as power of prime {prime}", rule=f"{rhs_val} = {prime}^{p}"),
            step(from_latex=f"2x {sign_str} {c_int} = {p}", to_latex_str=f"2x = {2 * x_val}", op="Equate exponents and isolate 2x", rule="Equate exponents"),
            step(from_latex=f"2x = {2 * x_val}", to_latex_str=f"x = {x_val}", op="Divide by 2", rule="Linear solve"),
        ],
        final_latex=str(x_val),
    )

    return make_math_question(
        prefix="g11_exp",
        topic=TOPIC,
        subskill="27_exponential_equation_prime_base_reduction",
        learning_objective_id=f"{LO_PREFIX}_27",
        prompt=prompt,
        prompt_latex=prompt,
        answer_mode="typed",
        question_type="math_short",
        answer_latex=str(x_val),
        answer_sympy=str(x_val),
        sample_answer=str(x_val),
        canonical_solution=sol,
        marking_schema={"total_marks": 3, "steps": [{"desc": f"Rewrite {rhs_val} as {prime}^{p}", "marks": 1}, {"desc": "Equate exponents", "marks": 1}, {"desc": "Solve for x", "marks": 1}]},
        hints={"nudge": f"Write {rhs_val} in exponential form with base {prime}.", "concept": "Express both sides with equal bases.", "breakdown": f"{prime}^(2x {sign_str} {c_int}) = {prime}^{p} \\implies 2x = {2*x_val} \\implies x = {x_val}."},
        misconception_tags=["multiplying_by_base_instead_of_converting_to_power"],
        term=1,
        caps_weight_percent=15,
        suggested_duration_mins=4,
        difficulty="medium",
    )


# ---------------------------------------------------------------------------
# 28. Exponential Equation: Fractional Power Linear
# ---------------------------------------------------------------------------
def build_28_exponential_equation_fractional_power_linear(r: random.Random) -> Dict[str, Any]:
    case = r.choice([(3, 2, 8, 4), (2, 3, 9, 27), (3, 4, 8, 16), (5, 2, 32, 4), (2, 5, 4, 32)])
    m, n, rhs_val, ans_val = case

    eq_latex = f"x^{{\\frac{{{m}}}{{{n}}}}} = {rhs_val}"
    prompt = f"Solve for $x$ where $x > 0$:\n\n$${eq_latex}$$"

    sol = solution_graph(
        goal="Solve rational exponent equation",
        chain_type="equation",
        var="x",
        steps=[
            step(from_latex=eq_latex, to_latex_str=f"\\left(x^{{\\frac{{{m}}}{{{n}}}}}\\right)^{{\\frac{{{n}}}{{{m}}}}} = {rhs_val}^{{\\frac{{{n}}}{{{m}}}}}", op=f"Raise both sides to reciprocal power {n}/{m}", rule="Invert exponent"),
            step(from_latex=f"x = {rhs_val}^{{\\frac{{{n}}}{{{m}}}}}", to_latex_str=f"x = {ans_val}", op="Evaluate power", rule=f"x = {ans_val}"),
        ],
        final_latex=str(ans_val),
    )

    return make_math_question(
        prefix="g11_exp",
        topic=TOPIC,
        subskill="28_exponential_equation_fractional_power_linear",
        learning_objective_id=f"{LO_PREFIX}_28",
        prompt=prompt,
        prompt_latex=prompt,
        answer_mode="typed",
        question_type="math_short",
        answer_latex=str(ans_val),
        answer_sympy=str(ans_val),
        sample_answer=str(ans_val),
        canonical_solution=sol,
        marking_schema={"total_marks": 2, "steps": [{"desc": f"Raise to power {n}/{m}", "marks": 1}, {"desc": f"Solve x = {ans_val}", "marks": 1}]},
        hints={"nudge": f"Raise both sides to reciprocal exponent ({n}/{m}).", "concept": "(x^(m/n))^(n/m) = x.", "breakdown": f"x = {rhs_val}^({n}/{m}) = {ans_val}."},
        misconception_tags=["multiplying_by_fractional_exponent_instead_of_reciprocal_power"],
        term=1,
        caps_weight_percent=15,
        suggested_duration_mins=3,
        difficulty="medium",
    )


# ---------------------------------------------------------------------------
# 29. Exponential Equation: Negative Fractional Power
# ---------------------------------------------------------------------------
def build_29_exponential_equation_negative_fractional_power(r: random.Random) -> Dict[str, Any]:
    case = r.choice([(3, 4, 8, 16), (2, 3, 9, 27), (3, 2, 8, 4), (1, 3, 2, 8)])
    m, n, denom_rhs, ans_val = case

    eq_latex = f"x^{{-\\frac{{{m}}}{{{n}}}}} = \\frac{{1}}{{{denom_rhs}}}"
    prompt = f"Solve for $x$:\n\n$${eq_latex}$$"

    sol = solution_graph(
        goal="Solve negative rational exponent equation",
        chain_type="equation",
        var="x",
        steps=[
            step(from_latex=eq_latex, to_latex_str=f"x^{{\\frac{{{m}}}{{{n}}}}} = {denom_rhs}", op="Take reciprocal of both sides", rule="x^(-k) = 1/x^k"),
            step(from_latex=f"x^{{\\frac{{{m}}}{{{n}}}}} = {denom_rhs}", to_latex_str=f"x = {denom_rhs}^{{\\frac{{{n}}}{{{m}}}}} = {ans_val}", op=f"Raise to power {n}/{m}", rule="Invert exponent"),
        ],
        final_latex=str(ans_val),
    )

    return make_math_question(
        prefix="g11_exp",
        topic=TOPIC,
        subskill="29_exponential_equation_negative_fractional_power",
        learning_objective_id=f"{LO_PREFIX}_29",
        prompt=prompt,
        prompt_latex=prompt,
        answer_mode="typed",
        question_type="math_short",
        answer_latex=str(ans_val),
        answer_sympy=str(ans_val),
        sample_answer=str(ans_val),
        canonical_solution=sol,
        marking_schema={"total_marks": 3, "steps": [{"desc": "Take reciprocal", "marks": 1}, {"desc": f"Raise to power {n}/{m}", "marks": 1}, {"desc": "Solve for x", "marks": 1}]},
        hints={"nudge": "Take the reciprocal of both sides first.", "concept": "x^(-k) = 1/x^k.", "breakdown": f"x^({m}/{n}) = {denom_rhs} \\implies x = {ans_val}."},
        misconception_tags=["treating_negative_exponent_as_negative_number"],
        term=1,
        caps_weight_percent=15,
        suggested_duration_mins=4,
        difficulty="medium",
    )


# ---------------------------------------------------------------------------
# 30. Exponential Equation: Common Factor Extraction (Addition)
# ---------------------------------------------------------------------------
def build_30_exponential_equation_common_factor_extraction(r: random.Random) -> Dict[str, Any]:
    base = r.choice([2, 3])
    if base == 2:
        x_val = r.choice([2, 3, 4])
        bracket_sum = 3
        rhs_val = bracket_sum * (2 ** x_val)
        eq_latex = f"2^{{x + 1}} + 2^x = {rhs_val}"
    else:
        x_val = r.choice([2, 3])
        bracket_sum = 4
        rhs_val = bracket_sum * (3 ** x_val)
        eq_latex = f"3^{{x + 1}} + 3^x = {rhs_val}"

    prompt = f"Solve for $x$:\n\n$${eq_latex}$$"

    sol = solution_graph(
        goal="Solve exponential equation by common factor extraction",
        chain_type="equation",
        var="x",
        steps=[
            step(from_latex=eq_latex, to_latex_str=f"{base}^x \\left({base}^1 + 1\\right) = {rhs_val}", op=f"Factor out {base}^x", rule="Common factor extraction"),
            step(from_latex=f"{base}^x \\cdot {bracket_sum} = {rhs_val}", to_latex_str=f"{base}^x = {base ** x_val}", op=f"Divide by {bracket_sum}", rule="Isolate base power"),
            step(from_latex=f"{base}^x = {base}^{{{x_val}}}", to_latex_str=f"x = {x_val}", op="Equate exponents", rule=f"x = {x_val}"),
        ],
        final_latex=str(x_val),
    )

    return make_math_question(
        prefix="g11_exp",
        topic=TOPIC,
        subskill="30_exponential_equation_common_factor_extraction",
        learning_objective_id=f"{LO_PREFIX}_30",
        prompt=prompt,
        prompt_latex=prompt,
        answer_mode="typed",
        question_type="math_short",
        answer_latex=str(x_val),
        answer_sympy=str(x_val),
        sample_answer=str(x_val),
        canonical_solution=sol,
        marking_schema={"total_marks": 3, "steps": [{"desc": f"Factor out {base}^x", "marks": 1}, {"desc": f"Isolate {base}^x", "marks": 1}, {"desc": "Solve for x", "marks": 1}]},
        hints={"nudge": f"Factor out {base}^x from both terms on the LHS.", "concept": "a^(x+1) = a^x * a^1.", "breakdown": f"{base}^x({base} + 1) = {rhs_val} \\implies {base}^x = {base**x_val} \\implies x = {x_val}."},
        misconception_tags=["adding_bases_together_when_terms_are_added"],
        term=1,
        caps_weight_percent=15,
        suggested_duration_mins=4,
        difficulty="medium",
    )


# ---------------------------------------------------------------------------
# 31. Exponential Equation: Common Factor (Subtraction)
# ---------------------------------------------------------------------------
def build_31_exponential_equation_common_factor_subtraction(r: random.Random) -> Dict[str, Any]:
    base = r.choice([2, 3])
    if base == 2:
        x_val = r.choice([2, 3, 4])
        bracket_diff = 3
        rhs_val = bracket_diff * (2 ** x_val)
        eq_latex = f"2^{{x + 2}} - 2^x = {rhs_val}"
    else:
        x_val = r.choice([1, 2, 3])
        bracket_diff = 8
        rhs_val = bracket_diff * (3 ** x_val)
        eq_latex = f"3^{{x + 2}} - 3^x = {rhs_val}"

    prompt = f"Solve for $x$:\n\n$${eq_latex}$$"

    sol = solution_graph(
        goal="Solve exponential equation with subtraction via common factor",
        chain_type="equation",
        var="x",
        steps=[
            step(from_latex=eq_latex, to_latex_str=f"{base}^x \\left({base}^2 - 1\\right) = {rhs_val}", op=f"Factor out {base}^x", rule="Common factor"),
            step(from_latex=f"{base}^x \\cdot {bracket_diff} = {rhs_val}", to_latex_str=f"{base}^x = {base ** x_val}", op=f"Divide by {bracket_diff}", rule="Isolate base power"),
            step(from_latex=f"{base}^x = {base}^{{{x_val}}}", to_latex_str=f"x = {x_val}", op="Equate exponents", rule=f"x = {x_val}"),
        ],
        final_latex=str(x_val),
    )

    return make_math_question(
        prefix="g11_exp",
        topic=TOPIC,
        subskill="31_exponential_equation_common_factor_subtraction",
        learning_objective_id=f"{LO_PREFIX}_31",
        prompt=prompt,
        prompt_latex=prompt,
        answer_mode="typed",
        question_type="math_short",
        answer_latex=str(x_val),
        answer_sympy=str(x_val),
        sample_answer=str(x_val),
        canonical_solution=sol,
        marking_schema={"total_marks": 3, "steps": [{"desc": f"Factor out {base}^x", "marks": 1}, {"desc": f"Isolate {base}^x", "marks": 1}, {"desc": "Solve for x", "marks": 1}]},
        hints={"nudge": f"Write {base}^(x+2) as {base}^x * {base}^2 and factor out {base}^x.", "concept": "a^(x+k) - a^x = a^x(a^k - 1).", "breakdown": f"{base}^x({base**2 - 1}) = {rhs_val} \\implies {base}^x = {base**x_val} \\implies x = {x_val}."},
        misconception_tags=["subtracting_exponents_over_subtraction_sign"],
        term=1,
        caps_weight_percent=15,
        suggested_duration_mins=4,
        difficulty="medium",
    )


# ---------------------------------------------------------------------------
# 32. Exponential Equation: k-Substitution Distinct Roots
# ---------------------------------------------------------------------------
def build_32_exponential_equation_k_substitution_distinct_roots(r: random.Random) -> Dict[str, Any]:
    pair = r.choice([(1, 2, 2, 4, 6, 8), (0, 1, 1, 2, 3, 2), (1, 3, 2, 8, 10, 16), (0, 2, 1, 4, 5, 4)])
    x1, x2, k1, k2, b_coef, c_val = pair

    eq_latex = f"2^{{2x}} - {b_coef} \\cdot 2^x + {c_val} = 0"
    ans_latex = f"x = {x1} \\quad \\text{{or}} \\quad x = {x2}"
    prompt = f"Solve for $x$:\n\n$${eq_latex}$$"

    sol = solution_graph(
        goal="Solve quadratic exponential equation using k-substitution",
        chain_type="equation",
        var="x",
        steps=[
            step(from_latex=eq_latex, to_latex_str=f"k^2 - {b_coef}k + {c_val} = 0 \\quad (k = 2^x)", op="Substitute k = 2^x", rule="Quadratic substitution"),
            step(from_latex=f"(k - {k1})(k - {k2}) = 0", to_latex_str=f"k = {k1} \\text{{ or }} k = {k2}", op="Factorise quadratic", rule="Zero product rule"),
            step(from_latex=f"2^x = {k1} \\text{{ or }} 2^x = {k2}", to_latex_str=ans_latex, op="Solve for x", rule="2^x = 2^n implies x = n"),
        ],
        final_latex=ans_latex,
    )

    return make_math_question(
        prefix="g11_exp",
        topic=TOPIC,
        subskill="32_exponential_equation_k_substitution_distinct_roots",
        learning_objective_id=f"{LO_PREFIX}_32",
        prompt=prompt,
        prompt_latex=prompt,
        answer_mode="typed",
        question_type="math_short",
        answer_latex=ans_latex,
        answer_sympy=f"x = {x1} or x = {x2}",
        sample_answer=ans_latex,
        canonical_solution=sol,
        marking_schema={"total_marks": 4, "steps": [{"desc": "k-substitution", "marks": 1}, {"desc": "Factorise", "marks": 1}, {"desc": "Values for k", "marks": 1}, {"desc": "Values for x", "marks": 1}]},
        hints={"nudge": "Let k = 2^x to obtain a standard quadratic equation in k.", "concept": "2^(2x) = (2^x)² = k².", "breakdown": f"(k - {k1})(k - {k2}) = 0 \\implies k = {k1} or {k2} \\implies x = {x1} or {x2}."},
        misconception_tags=["stopping_at_k_instead_of_solving_for_x"],
        term=1,
        caps_weight_percent=15,
        suggested_duration_mins=5,
        difficulty="hard",
    )


# ---------------------------------------------------------------------------
# 33. Exponential Equation: k-Substitution (One Extraneous Root)
# ---------------------------------------------------------------------------
def build_33_exponential_equation_k_substitution_one_extraneous(r: random.Random) -> Dict[str, Any]:
    base = r.choice([2, 3])
    if base == 2:
        k_pos = r.choice([2, 4, 8])
        k_neg = r.choice([1, 2, 3])
        x_valid = int(round(math.log2(k_pos)))
    else:
        k_pos = r.choice([3, 9])
        k_neg = r.choice([1, 2])
        x_valid = int(round(math.log(k_pos, 3)))

    b_coef = k_pos - k_neg
    c_val = k_pos * k_neg
    quad_str = f"{base}^{{2x}} - {b_coef} \\cdot {base}^x - {c_val} = 0" if b_coef >= 0 else f"{base}^{{2x}} + {-b_coef} \\cdot {base}^x - {c_val} = 0"

    eq_latex = quad_str
    ans_latex = f"x = {x_valid}"
    prompt = f"Solve for $x$ in the real number system:\n\n$${eq_latex}$$"

    sol = solution_graph(
        goal="Solve quadratic exponential equation and reject negative root",
        chain_type="equation",
        var="x",
        steps=[
            step(from_latex=eq_latex, to_latex_str=f"k^2 - {b_coef}k - {c_val} = 0 \\quad (k = {base}^x)", op="Substitute k = base^x", rule="Quadratic substitution"),
            step(from_latex=f"(k - {k_pos})(k + {k_neg}) = 0", to_latex_str=f"k = {k_pos} \\text{{ or }} k = -{k_neg}", op="Factorise quadratic", rule="Zero product rule"),
            step(from_latex=f"{base}^x = {k_pos} \\text{{ or }} {base}^x = -{k_neg}", to_latex_str=f"x = {x_valid} \\quad ({base}^x = -{k_neg} \\text{{ no real solution}})", op="Reject negative root", rule="base^x > 0 for all real x"),
        ],
        final_latex=ans_latex,
    )

    return make_math_question(
        prefix="g11_exp",
        topic=TOPIC,
        subskill="33_exponential_equation_k_substitution_one_extraneous",
        learning_objective_id=f"{LO_PREFIX}_33",
        prompt=prompt,
        prompt_latex=prompt,
        answer_mode="typed",
        question_type="math_short",
        answer_latex=ans_latex,
        answer_sympy=f"x = {x_valid}",
        sample_answer=ans_latex,
        canonical_solution=sol,
        marking_schema={"total_marks": 4, "steps": [{"desc": "Quadratic in k", "marks": 1}, {"desc": "Factorise", "marks": 1}, {"desc": "Identify roots for k", "marks": 1}, {"desc": f"Reject negative root, x = {x_valid}", "marks": 1}]},
        hints={"nudge": f"Remember that {base}^x is strictly positive for all real x.", "concept": "b^x > 0. A negative root for k cannot produce any real value of x.", "breakdown": f"k = {k_pos} gives x = {x_valid}; k = -{k_neg} has no real solution."},
        misconception_tags=["failing_to_reject_negative_exponential_solution"],
        term=1,
        caps_weight_percent=15,
        suggested_duration_mins=5,
        difficulty="hard",
    )


# ---------------------------------------------------------------------------
# 34. Exponential Equation: Fractional Base Term
# ---------------------------------------------------------------------------
def build_34_exponential_equation_k_substitution_fractional(r: random.Random) -> Dict[str, Any]:
    x_val = r.choice([1, 2, 3])
    k_pos = 2 ** x_val
    k_neg = 1
    c_num = k_pos * k_neg
    b_rhs = k_pos - k_neg

    eq_latex = f"2^x - \\frac{{{c_num}}}{{2^x}} = {b_rhs}"
    ans_latex = f"x = {x_val}"
    prompt = f"Solve for $x$:\n\n$${eq_latex}$$"

    sol = solution_graph(
        goal="Solve exponential equation with reciprocal base term",
        chain_type="equation",
        var="x",
        steps=[
            step(from_latex=eq_latex, to_latex_str=f"\\left(2^x\\right)^2 - {c_num} = {b_rhs} \\cdot 2^x", op="Multiply by 2^x to clear fraction", rule="Clear fraction"),
            step(from_latex=f"\\left(2^x\\right)^2 - {b_rhs} \\cdot 2^x - {c_num} = 0", to_latex_str=f"(2^x - {k_pos})(2^x + {k_neg}) = 0", op="Factorise quadratic", rule="Trinomial factorisation"),
            step(from_latex=f"2^x = {k_pos} \\text{{ or }} 2^x = -{k_neg}", to_latex_str=ans_latex, op="Solve for x and reject negative root", rule="2^x > 0"),
        ],
        final_latex=ans_latex,
    )

    return make_math_question(
        prefix="g11_exp",
        topic=TOPIC,
        subskill="34_exponential_equation_k_substitution_fractional",
        learning_objective_id=f"{LO_PREFIX}_34",
        prompt=prompt,
        prompt_latex=prompt,
        answer_mode="typed",
        question_type="math_short",
        answer_latex=ans_latex,
        answer_sympy=f"x = {x_val}",
        sample_answer=ans_latex,
        canonical_solution=sol,
        marking_schema={"total_marks": 4, "steps": [{"desc": "Multiply by 2^x", "marks": 1}, {"desc": "Factorise quadratic", "marks": 1}, {"desc": "Reject negative base power", "marks": 1}, {"desc": f"x = {x_val}", "marks": 1}]},
        hints={"nudge": "Multiply each term by 2^x to eliminate the fraction.", "concept": "Multiplying through by 2^x produces a standard quadratic in 2^x.", "breakdown": f"(2^x - {k_pos})(2^x + {k_neg}) = 0 \\implies 2^x = {k_pos} \\implies x = {x_val}."},
        misconception_tags=["forgetting_to_multiply_rhs_by_lcd"],
        term=1,
        caps_weight_percent=15,
        suggested_duration_mins=5,
        difficulty="hard",
    )


# ---------------------------------------------------------------------------
# 35. Surd Equation: Simple Isolated Radical
# ---------------------------------------------------------------------------
def build_35_surd_equation_simple_isolated_radical(r: random.Random) -> Dict[str, Any]:
    b = r.randint(3, 7)
    b_sq = b * b
    a = r.randint(1, b_sq - 1)
    x_val = b_sq - a

    eq_latex = f"\\sqrt{{x + {a}}} = {b}"
    prompt = f"Solve for $x$:\n\n$${eq_latex}$$"

    sol = solution_graph(
        goal="Solve isolated surd equation",
        chain_type="equation",
        var="x",
        steps=[
            step(from_latex=eq_latex, to_latex_str=f"x + {a} = {b_sq}", op="Square both sides", rule="(sqrt(u))^2 = u"),
            step(from_latex=f"x + {a} = {b_sq}", to_latex_str=f"x = {x_val}", op=f"Subtract {a}", rule="Linear solve"),
        ],
        final_latex=str(x_val),
    )

    return make_math_question(
        prefix="g11_exp",
        topic=TOPIC,
        subskill="35_surd_equation_simple_isolated_radical",
        learning_objective_id=f"{LO_PREFIX}_35",
        prompt=prompt,
        prompt_latex=prompt,
        answer_mode="typed",
        question_type="math_short",
        answer_latex=str(x_val),
        answer_sympy=str(x_val),
        sample_answer=str(x_val),
        canonical_solution=sol,
        marking_schema={"total_marks": 2, "steps": [{"desc": "Square both sides", "marks": 1}, {"desc": f"x = {x_val}", "marks": 1}]},
        hints={"nudge": "The radical is already isolated. Square both sides.", "concept": "(√A)² = A.", "breakdown": f"x + {a} = {b_sq} \\implies x = {x_val}."},
        misconception_tags=["squaring_only_one_side_of_equation"],
        term=1,
        caps_weight_percent=15,
        suggested_duration_mins=3,
        difficulty="easy",
    )


# ---------------------------------------------------------------------------
# 36. Surd Equation: Isolate Before Squaring
# ---------------------------------------------------------------------------
def build_36_surd_equation_isolate_before_squaring(r: random.Random) -> Dict[str, Any]:
    b = r.choice([3, 5, 7])
    b_sq = b * b
    a = r.choice([1, 3, 5, 7])
    while (b_sq - a) % 2 != 0:
        a = r.choice([1, 3, 5, 7])
    x_val = (b_sq - a) // 2

    eq_latex = f"\\sqrt{{2x + {a}}} - {b} = 0"
    prompt = f"Solve for $x$:\n\n$${eq_latex}$$"

    sol = solution_graph(
        goal="Isolate radical before squaring",
        chain_type="equation",
        var="x",
        steps=[
            step(from_latex=eq_latex, to_latex_str=f"\\sqrt{{2x + {a}}} = {b}", op=f"Add {b} to both sides to isolate the surd", rule="Isolate radical"),
            step(from_latex=f"\\sqrt{{2x + {a}}} = {b}", to_latex_str=f"2x + {a} = {b_sq}", op="Square both sides", rule="(sqrt(u))^2 = u"),
            step(from_latex=f"2x = {b_sq - a}", to_latex_str=f"x = {x_val}", op="Divide by 2", rule="Linear solve"),
        ],
        final_latex=str(x_val),
    )

    return make_math_question(
        prefix="g11_exp",
        topic=TOPIC,
        subskill="36_surd_equation_isolate_before_squaring",
        learning_objective_id=f"{LO_PREFIX}_36",
        prompt=prompt,
        prompt_latex=prompt,
        answer_mode="typed",
        question_type="math_short",
        answer_latex=str(x_val),
        answer_sympy=str(x_val),
        sample_answer=str(x_val),
        canonical_solution=sol,
        marking_schema={"total_marks": 3, "steps": [{"desc": "Isolate surd", "marks": 1}, {"desc": "Square both sides", "marks": 1}, {"desc": f"x = {x_val}", "marks": 1}]},
        hints={"nudge": "Isolate the radical on the left before squaring both sides.", "concept": "Always isolate the square root term first.", "breakdown": f"\\sqrt{{2x+{a}}} = {b} \\implies 2x+{a} = {b_sq} \\implies x = {x_val}."},
        misconception_tags=["squaring_individual_terms_instead_of_whole_sides"],
        term=1,
        caps_weight_percent=15,
        suggested_duration_mins=4,
        difficulty="medium",
    )


# ---------------------------------------------------------------------------
# 37. Surd Equation: Linear RHS with One Valid Root
# ---------------------------------------------------------------------------
def build_37_surd_equation_linear_rhs_one_valid_root(r: random.Random) -> Dict[str, Any]:
    case = r.choice([(5, 1, 4, -1), (10, 2, 6, -1), (4, 2, 5, 0)])
    a_val, b_val, x_valid, x_extr = case

    eq_latex = f"\\sqrt{{x + {a_val}}} = x - {b_val}"
    ans_latex = f"x = {x_valid}"
    prompt = f"Solve for $x$ and test for extraneous solutions:\n\n$${eq_latex}$$"

    sol = solution_graph(
        goal="Solve surd equation and reject extraneous root",
        chain_type="equation",
        var="x",
        steps=[
            step(from_latex=eq_latex, to_latex_str=f"x + {a_val} = (x - {b_val})^2", op="Square both sides", rule="Squaring property"),
            step(from_latex=f"x + {a_val} = x^2 - {2 * b_val}x + {b_val ** 2}", to_latex_str=f"x^2 - {2 * b_val + 1}x + {b_val ** 2 - a_val} = 0", op="Standard quadratic form", rule="Rearrange terms"),
            step(from_latex=f"(x - {x_valid})(x - {x_extr}) = 0", to_latex_str=f"x = {x_valid} \\text{{ or }} x = {x_extr}", op="Factorise", rule="Zero product rule"),
            step(from_latex=f"\\text{{Test candidate roots}}", to_latex_str=ans_latex, op=f"Reject x = {x_extr} since RHS < 0", rule="Principal square root is non-negative"),
        ],
        final_latex=ans_latex,
    )

    return make_math_question(
        prefix="g11_exp",
        topic=TOPIC,
        subskill="37_surd_equation_linear_rhs_one_valid_root",
        learning_objective_id=f"{LO_PREFIX}_37",
        prompt=prompt,
        prompt_latex=prompt,
        answer_mode="typed",
        question_type="math_short",
        answer_latex=ans_latex,
        answer_sympy=f"x = {x_valid}",
        sample_answer=ans_latex,
        canonical_solution=sol,
        marking_schema={"total_marks": 4, "steps": [{"desc": "Square both sides", "marks": 1}, {"desc": "Quadratic form", "marks": 1}, {"desc": "Both candidate roots", "marks": 1}, {"desc": "Reject extraneous root", "marks": 1}]},
        hints={"nudge": f"Square both sides, but note that the RHS (x - {b_val}) must be >= 0.", "concept": "Squaring both sides can introduce invalid extraneous roots.", "breakdown": f"Roots are x = {x_valid} and {x_extr}. For x = {x_extr}, RHS = {x_extr - b_val} < 0 (rejected). Valid: x = {x_valid}."},
        misconception_tags=["forgetting_to_test_and_reject_extraneous_roots"],
        term=1,
        caps_weight_percent=15,
        suggested_duration_mins=5,
        difficulty="hard",
    )


# ---------------------------------------------------------------------------
# 38. Surd Equation: Linear RHS with Two Valid Roots
# ---------------------------------------------------------------------------
def build_38_surd_equation_linear_rhs_two_valid_roots(r: random.Random) -> Dict[str, Any]:
    case = r.choice([(5, 4, 1, 4), (7, 10, 2, 5), (7, 12, 3, 4), (10, 9, 1, 9)])
    a_coef, b_sub, x1, x2 = case

    eq_latex = f"\\sqrt{{{a_coef}x - {b_sub}}} = x"
    ans_latex = f"x = {x1} \\quad \\text{{or}} \\quad x = {x2}"
    prompt = f"Solve for $x$ and verify all roots:\n\n$${eq_latex}$$"

    sol = solution_graph(
        goal="Solve surd equation where both roots are valid",
        chain_type="equation",
        var="x",
        steps=[
            step(from_latex=eq_latex, to_latex_str=f"{a_coef}x - {b_sub} = x^2", op="Square both sides", rule="Squaring property"),
            step(from_latex=f"x^2 - {a_coef}x + {b_sub} = 0", to_latex_str=f"(x - {x1})(x - {x2}) = 0", op="Factorise quadratic", rule="Zero product rule"),
            step(from_latex=f"x = {x1} \\text{{ or }} x = {x2}", to_latex_str=ans_latex, op="Verify both roots in original equation", rule="Both roots are non-negative and valid"),
        ],
        final_latex=ans_latex,
    )

    return make_math_question(
        prefix="g11_exp",
        topic=TOPIC,
        subskill="38_surd_equation_linear_rhs_two_valid_roots",
        learning_objective_id=f"{LO_PREFIX}_38",
        prompt=prompt,
        prompt_latex=prompt,
        answer_mode="typed",
        question_type="math_short",
        answer_latex=ans_latex,
        answer_sympy=f"x = {x1} or x = {x2}",
        sample_answer=ans_latex,
        canonical_solution=sol,
        marking_schema={"total_marks": 4, "steps": [{"desc": "Square both sides", "marks": 1}, {"desc": "Standard form", "marks": 1}, {"desc": "Factorise", "marks": 1}, {"desc": "Verify both are valid", "marks": 1}]},
        hints={"nudge": "Square both sides, factorise the quadratic, and check both solutions.", "concept": "Both solutions are positive, so both satisfy the original equation.", "breakdown": f"x² - {a_coef}x + {b_sub} = 0 \\implies x = {x1} or x = {x2}."},
        misconception_tags=["assuming_one_solution_must_always_be_extraneous"],
        term=1,
        caps_weight_percent=15,
        suggested_duration_mins=4,
        difficulty="medium",
    )


# ---------------------------------------------------------------------------
# 39. Extraneous Root Identification
# ---------------------------------------------------------------------------
def build_39_surd_equation_with_extraneous_root_identification(r: random.Random) -> Dict[str, Any]:
    case = r.choice([(5, 1, 4, -1), (10, 2, 6, -1)])
    a_val, b_val, x_valid, x_extr = case
    eq_latex = f"\\sqrt{{x + {a_val}}} = x - {b_val}"
    
    correct = f"x = {x_extr} is extraneous because the RHS is negative ({x_extr - b_val}), but a principal square root must be non-negative."
    distractors = [
        f"x = {x_valid} is extraneous because squaring an equation always invalidates the larger root.",
        f"Neither root is extraneous because both satisfy the quadratic equation after squaring.",
        f"Both roots are extraneous because radical equations have no integer solutions.",
    ]
    options = [correct] + distractors
    r.shuffle(options)

    prompt = (
        f"A student solves the surd equation:\n\n$${eq_latex}$$\n\n"
        f"By squaring both sides, the candidate roots are $x = {x_valid}$ and $x = {x_extr}$.\n\n"
        f"Which statement correctly identifies the validity of these solutions?"
    )

    sol = solution_graph(
        goal="Explain why squaring creates extraneous roots",
        chain_type="classification",
        steps=[
            step(from_latex=f"\\text{{For }} x = {x_extr}: \\sqrt{{{x_extr + a_val}}} = {abs(x_extr - b_val)} \\ne {x_extr - b_val}", to_latex_str=correct, op="Test extraneous root", rule="Principal square root >= 0")
        ],
        final_latex=correct,
    )

    q = make_math_question(
        prefix="g11_exp",
        topic=TOPIC,
        subskill="39_surd_equation_with_extraneous_root_identification",
        learning_objective_id=f"{LO_PREFIX}_39",
        prompt=prompt,
        prompt_latex=prompt,
        answer_mode="mcq",
        question_type="mcq",
        answer_latex=correct,
        sample_answer=correct,
        canonical_solution=sol,
        marking_schema={"total_marks": 2, "steps": [{"desc": f"Identify x = {x_extr} as extraneous", "marks": 1}, {"desc": "Correct mathematical justification", "marks": 1}]},
        hints={"nudge": f"Substitute x = {x_extr} into both sides of the original equation.", "concept": "A principal square root √A is always >= 0.", "breakdown": f"LHS is positive, RHS = {x_extr - b_val} is negative."},
        misconception_tags=["believing_all_solutions_to_squared_quadratic_are_valid"],
        term=1,
        caps_weight_percent=15,
        suggested_duration_mins=3,
        difficulty="medium",
    )
    q["options"] = options
    return q


# ---------------------------------------------------------------------------
# 40. Surd Equation: k-Substitution (x - √x - c = 0)
# ---------------------------------------------------------------------------
def build_40_surd_equation_k_substitution(r: random.Random) -> Dict[str, Any]:
    pair = r.choice([(1, 6, 3, 2, 9), (1, 12, 4, 3, 16), (1, 20, 5, 4, 25), (2, 8, 4, 2, 16)])
    a_coef, b_val, p_val, q_val, ans_val = pair

    eq_latex = f"x - {a_coef}\\sqrt{{x}} - {b_val} = 0" if a_coef > 1 else f"x - \\sqrt{{x}} - {b_val} = 0"
    ans_latex = f"x = {ans_val}"
    prompt = f"Solve for $x$ in the real number system:\n\n$${eq_latex}$$"

    sol = solution_graph(
        goal="Solve quadratic in sqrt(x) using k-substitution",
        chain_type="equation",
        var="x",
        steps=[
            step(from_latex=eq_latex, to_latex_str=f"k^2 - {a_coef}k - {b_val} = 0 \\quad (k = \\sqrt{{x}}, k \\ge 0)", op="Substitute k = \\sqrt{x}", rule="Quadratic substitution"),
            step(from_latex=f"(k - {p_val})(k + {q_val}) = 0", to_latex_str=f"k = {p_val} \\text{{ or }} k = -{q_val}", op="Factorise quadratic in k", rule="Zero product rule"),
            step(from_latex=f"\\sqrt{{x}} = {p_val}", to_latex_str=ans_latex, op=f"Reject k = -{q_val} and square {p_val}", rule=f"x = {p_val}^2 = {ans_val}"),
        ],
        final_latex=ans_latex,
    )

    return make_math_question(
        prefix="g11_exp",
        topic=TOPIC,
        subskill="40_surd_equation_k_substitution",
        learning_objective_id=f"{LO_PREFIX}_40",
        prompt=prompt,
        prompt_latex=prompt,
        answer_mode="typed",
        question_type="math_short",
        answer_latex=ans_latex,
        answer_sympy=f"x = {ans_val}",
        sample_answer=ans_latex,
        canonical_solution=sol,
        marking_schema={"total_marks": 4, "steps": [{"desc": "Substitute k = \\sqrt{x}", "marks": 1}, {"desc": "Factorise", "marks": 1}, {"desc": "Reject negative k", "marks": 1}, {"desc": f"Solve x = {ans_val}", "marks": 1}]},
        hints={"nudge": "Let k = √x. Notice that x = (√x)² = k².", "concept": "Transform into quadratic in k: k² - ak - b = 0. √x must be >= 0.", "breakdown": f"k = {p_val} \\implies x = {p_val}² = {ans_val}."},
        misconception_tags=["squaring_negative_k_to_create_invalid_solution"],
        term=1,
        caps_weight_percent=15,
        suggested_duration_mins=4,
        difficulty="hard",
    )


# ---------------------------------------------------------------------------
# 41. Surd Equation: Quadratic Radicand
# ---------------------------------------------------------------------------
def build_41_surd_equation_quadratic_expression_under_radical(r: random.Random) -> Dict[str, Any]:
    b = r.choice([1, 2, 3])
    k = r.choice([2, 4, 6])
    a = (b * b) + (2 * b * k)
    x_val = k

    eq_latex = f"\\sqrt{{x^2 + {a}}} = x + {b}"
    ans_latex = f"x = {x_val}"
    prompt = f"Solve for $x$:\n\n$${eq_latex}$$"

    sol = solution_graph(
        goal="Solve radical equation with quadratic radicand",
        chain_type="equation",
        var="x",
        steps=[
            step(from_latex=eq_latex, to_latex_str=f"x^2 + {a} = x^2 + {2 * b}x + {b * b}", op="Square both sides", rule="Squaring property"),
            step(from_latex=f"{a} = {2 * b}x + {b * b}", to_latex_str=f"{2 * b}x = {a - b * b}", op="Cancel x^2 from both sides", rule="Linear reduction"),
            step(from_latex=f"{2 * b}x = {a - b * b}", to_latex_str=ans_latex, op=f"Divide by {2 * b}", rule=f"x = {x_val}"),
        ],
        final_latex=ans_latex,
    )

    return make_math_question(
        prefix="g11_exp",
        topic=TOPIC,
        subskill="41_surd_equation_quadratic_expression_under_radical",
        learning_objective_id=f"{LO_PREFIX}_41",
        prompt=prompt,
        prompt_latex=prompt,
        answer_mode="typed",
        question_type="math_short",
        answer_latex=ans_latex,
        answer_sympy=f"x = {x_val}",
        sample_answer=ans_latex,
        canonical_solution=sol,
        marking_schema={"total_marks": 3, "steps": [{"desc": "Square both sides", "marks": 1}, {"desc": "Cancel x^2", "marks": 1}, {"desc": f"Solve x = {x_val}", "marks": 1}]},
        hints={"nudge": "Square both sides. The x² terms cancel out on both sides.", "concept": "(x + b)² = x² + 2bx + b².", "breakdown": f"x² + {a} = x² + {2*b}x + {b*b} \\implies {2*b}x = {a - b*b} \\implies x = {x_val}."},
        misconception_tags=["failing_to_cancel_squared_terms_on_both_sides"],
        term=1,
        caps_weight_percent=15,
        suggested_duration_mins=4,
        difficulty="medium",
    )


# ---------------------------------------------------------------------------
# 42. Surd Equation: Two Radicals Basic
# ---------------------------------------------------------------------------
def build_42_surd_equation_two_radicals_basic(r: random.Random) -> Dict[str, Any]:
    a = r.randint(2, 6)
    b = r.randint(3, 9)
    x_val = a + b

    eq_latex = f"\\sqrt{{2x - {a}}} = \\sqrt{{x + {b}}}"
    ans_latex = f"x = {x_val}"
    prompt = f"Solve for $x$:\n\n$${eq_latex}$$"

    sol = solution_graph(
        goal="Solve equation with two equal radicals",
        chain_type="equation",
        var="x",
        steps=[
            step(from_latex=eq_latex, to_latex_str=f"2x - {a} = x + {b}", op="Square both sides", rule="Eliminate radicals"),
            step(from_latex=f"2x - x = {b} + {a}", to_latex_str=ans_latex, op="Isolate x", rule=f"x = {x_val}"),
        ],
        final_latex=ans_latex,
    )

    return make_math_question(
        prefix="g11_exp",
        topic=TOPIC,
        subskill="42_surd_equation_two_radicals_basic",
        learning_objective_id=f"{LO_PREFIX}_42",
        prompt=prompt,
        prompt_latex=prompt,
        answer_mode="typed",
        question_type="math_short",
        answer_latex=ans_latex,
        answer_sympy=f"x = {x_val}",
        sample_answer=ans_latex,
        canonical_solution=sol,
        marking_schema={"total_marks": 2, "steps": [{"desc": "Equate radicands", "marks": 1}, {"desc": f"x = {x_val}", "marks": 1}]},
        hints={"nudge": "Squaring both sides eliminates both square roots immediately.", "concept": "If √A = √B then A = B.", "breakdown": f"2x - {a} = x + {b} \\implies x = {x_val}."},
        misconception_tags=["introducing_extraneous_terms_when_squaring_single_radicals"],
        term=1,
        caps_weight_percent=15,
        suggested_duration_mins=3,
        difficulty="easy",
    )


# ---------------------------------------------------------------------------
# 43. Real Number Restrictions: Undefined or Non-Real Values
# ---------------------------------------------------------------------------
def build_43_surd_expression_undefined_condition(r: random.Random) -> Dict[str, Any]:
    a = r.randint(2, 9)
    q_type = r.choice(["non_real", "real"])
    
    if q_type == "non_real":
        prompt = f"For which values of $x$ will $\\frac{{1}}{{\\sqrt{{x - {a}}}}}$ be **non-real or undefined**?"
        correct = f"x \\le {a}"
        distractors = [f"x < {a}", f"x \\ge {a}", f"x = {a}"]
        reason = f"Radicand must be non-negative and denominator cannot be zero. Thus non-real or undefined when $x \\le {a}$."
    else:
        prompt = f"For which values of $x$ will $\\frac{{1}}{{\\sqrt{{x - {a}}}}}$ be **real and defined**?"
        correct = f"x > {a}"
        distractors = [f"x \\ge {a}", f"x < {a}", f"x \\ne {a}"]
        reason = f"Radicand must be strictly positive: $x - {a} > 0 \\implies x > {a}$."

    options = [f"${correct}$"] + [f"${d}$" for d in distractors]
    r.shuffle(options)

    sol = solution_graph(
        goal="Determine domain restrictions for radical fraction",
        chain_type="inequality",
        steps=[step(from_latex=f"\\frac{{1}}{{\\sqrt{{x - {a}}}}}", to_latex_str=correct, op="Apply non-real and zero-denominator restrictions", rule=reason)],
        final_latex=correct,
    )

    q = make_math_question(
        prefix="g11_exp",
        topic=TOPIC,
        subskill="43_surd_expression_undefined_condition",
        learning_objective_id=f"{LO_PREFIX}_43",
        prompt=prompt,
        prompt_latex=prompt,
        answer_mode="mcq",
        question_type="mcq",
        answer_latex=f"${correct}$",
        sample_answer=f"${correct}$",
        canonical_solution=sol,
        marking_schema={"total_marks": 2, "steps": [{"desc": "Radicand condition", "marks": 1}, {"desc": f"Inequality {correct}", "marks": 1}]},
        hints={"nudge": "Consider both the square root condition (radicand >= 0) and division by zero.", "concept": "1/√(f(x)) is real only when f(x) > 0.", "breakdown": reason},
        misconception_tags=["allowing_zero_in_denominator_of_radical_fraction"],
        term=1,
        caps_weight_percent=15,
        suggested_duration_mins=3,
        difficulty="medium",
    )
    q["options"] = options
    return q


# ---------------------------------------------------------------------------
# 44. Nature of Roots: Discriminant & Surd Connection
# ---------------------------------------------------------------------------
def build_44_nature_of_roots_discriminant_surd_connection(r: random.Random) -> Dict[str, Any]:
    case = r.choice(["perf_sq", "non_perf_sq", "zero", "negative"])
    if case == "perf_sq":
        delta = r.choice([16, 25, 36, 49, 64, 81])
        correct = "Real, rational and unequal"
        reason = f"\\Delta = {delta} > 0 and is a perfect square, so roots are real, rational and unequal."
        distractors = ["Real, irrational and unequal", "Real, rational and equal", "Non-real"]
    elif case == "non_perf_sq":
        delta = r.choice([12, 17, 20, 24, 28, 32])
        correct = "Real, irrational and unequal"
        reason = f"\\Delta = {delta} > 0 is not a perfect square, so roots are real, irrational and unequal."
        distractors = ["Real, rational and unequal", "Real, rational and equal", "Non-real"]
    elif case == "zero":
        delta = 0
        correct = "Real, rational and equal"
        reason = "\\Delta = 0, so roots are real, rational and equal."
        distractors = ["Real, irrational and unequal", "Real, rational and unequal", "Non-real"]
    else:
        delta = r.choice([-4, -7, -12, -16, -25])
        correct = "Non-real"
        reason = f"\\Delta = {delta} < 0, so square root is non-real; roots are non-real."
        distractors = ["Real, rational and unequal", "Real, irrational and unequal", "Real, rational and equal"]

    options = [correct] + distractors
    r.shuffle(options)

    prompt = f"If the discriminant of a quadratic equation is $\\Delta = {delta}$, describe the nature of the roots."

    sol = solution_graph(
        goal="Determine nature of roots from discriminant",
        chain_type="classification",
        steps=[step(from_latex=f"\\Delta = {delta}", to_latex_str=correct, op="Evaluate discriminant sign and square property", rule=reason)],
        final_latex=correct,
    )

    q = make_math_question(
        prefix="g11_exp",
        topic=TOPIC,
        subskill="44_nature_of_roots_discriminant_surd_connection",
        learning_objective_id=f"{LO_PREFIX}_44",
        prompt=prompt,
        prompt_latex=prompt,
        answer_mode="mcq",
        question_type="mcq",
        answer_latex=correct,
        sample_answer=correct,
        canonical_solution=sol,
        marking_schema={"total_marks": 2, "steps": [{"desc": "Evaluate delta", "marks": 1}, {"desc": "Correct nature of roots", "marks": 1}]},
        hints={"nudge": "Check if Δ is positive, zero, or negative, and whether it is a perfect square.", "concept": "Δ > 0 perf sq: rational; Δ > 0 not perf sq: irrational; Δ = 0: equal; Δ < 0: non-real.", "breakdown": reason},
        misconception_tags=["confusing_rational_and_irrational_discriminants"],
        term=1,
        caps_weight_percent=15,
        suggested_duration_mins=3,
        difficulty="easy",
    )
    q["options"] = options
    return q


# ---------------------------------------------------------------------------
# 45. Exponential Growth: Population Model Formula
# ---------------------------------------------------------------------------
def build_45_exponential_growth_compound_formula(r: random.Random) -> Dict[str, Any]:
    p0 = r.randint(10, 50) * 100
    rate_pct = r.choice([5, 8, 10, 12])
    t_years = r.choice([2, 3])
    
    r_dec = rate_pct / 100.0
    factor = 1.0 + r_dec
    final_amt = int(round(p0 * (factor ** t_years)))

    prompt = (
        f"A town has an initial population of ${p0}$. It grows exponentially at ${rate_pct}\\%$ per annum "
        f"using $A = P(1 + r)^t$.\n\nCalculate the population after ${t_years}$ years (nearest whole number)."
    )

    sol = solution_graph(
        goal="Calculate exponential population growth",
        chain_type="calculation",
        steps=[
            step(from_latex=f"A = {p0}(1 + {num(r_dec)})^{{{t_years}}}", to_latex_str=f"A = {p0}({num(factor)})^{{{t_years}}}", op="Substitute into compound growth model", rule="A = P(1+r)^t"),
            step(from_latex=f"A = {p0} \\times {num(round(factor ** t_years, 4))}", to_latex_str=f"A \\approx {final_amt}", op="Evaluate power", rule=f"A = {final_amt}"),
        ],
        final_latex=str(final_amt),
    )

    return make_math_question(
        prefix="g11_exp",
        topic=TOPIC,
        subskill="45_exponential_growth_compound_formula",
        learning_objective_id=f"{LO_PREFIX}_45",
        prompt=prompt,
        prompt_latex=prompt,
        answer_mode="typed",
        question_type="math_short",
        answer_latex=str(final_amt),
        answer_sympy=str(final_amt),
        sample_answer=str(final_amt),
        canonical_solution=sol,
        marking_schema={"total_marks": 3, "steps": [{"desc": "Formula substitution", "marks": 1}, {"desc": "Evaluate power", "marks": 1}, {"desc": f"Answer {final_amt}", "marks": 1}]},
        hints={"nudge": "Convert percentage to decimal: r = rate / 100.", "concept": "A = P(1 + r)^t.", "breakdown": f"A = {p0}({factor})^{t_years} ≈ {final_amt}."},
        misconception_tags=["using_simple_growth_instead_of_exponential"],
        term=1,
        caps_weight_percent=15,
        suggested_duration_mins=4,
        difficulty="medium",
    )


# ---------------------------------------------------------------------------
# 46. Exponential Decay: Reducing-Balance Depreciation Model
# ---------------------------------------------------------------------------
def build_46_exponential_decay_depreciation_model(r: random.Random) -> Dict[str, Any]:
    p0 = r.randint(15, 60) * 1000
    rate_pct = r.choice([10, 15, 20])
    t_years = r.choice([2, 3])

    r_dec = rate_pct / 100.0
    factor = 1.0 - r_dec
    final_amt = int(round(p0 * (factor ** t_years)))

    prompt = (
        f"Machinery purchased for R{p0} depreciates exponentially at ${rate_pct}\\%$ per annum "
        f"on a reducing balance ($A = P(1 - i)^n$).\n\nCalculate its value after ${t_years}$ years (nearest Rand)."
    )

    sol = solution_graph(
        goal="Calculate reducing balance depreciation",
        chain_type="calculation",
        steps=[
            step(from_latex=f"A = {p0}(1 - {num(r_dec)})^{{{t_years}}}", to_latex_str=f"A = {p0}({num(factor)})^{{{t_years}}}", op="Substitute into reducing balance model", rule="A = P(1-i)^n"),
            step(from_latex=f"A = {p0} \\times {num(round(factor ** t_years, 4))}", to_latex_str=f"A \\approx {final_amt}", op="Calculate final value", rule=f"A = {final_amt}"),
        ],
        final_latex=str(final_amt),
    )

    return make_math_question(
        prefix="g11_exp",
        topic=TOPIC,
        subskill="46_exponential_decay_depreciation_model",
        learning_objective_id=f"{LO_PREFIX}_46",
        prompt=prompt,
        prompt_latex=prompt,
        answer_mode="typed",
        question_type="math_short",
        answer_latex=str(final_amt),
        answer_sympy=str(final_amt),
        sample_answer=str(final_amt),
        canonical_solution=sol,
        marking_schema={"total_marks": 3, "steps": [{"desc": "Substitution", "marks": 1}, {"desc": "Decay factor", "marks": 1}, {"desc": f"R{final_amt}", "marks": 1}]},
        hints={"nudge": "For depreciation, use (1 - i).", "concept": "A = P(1 - i)^n.", "breakdown": f"A = {p0}({factor})^{t_years} = R{final_amt}."},
        misconception_tags=["using_addition_instead_of_subtraction_for_decay"],
        term=1,
        caps_weight_percent=15,
        suggested_duration_mins=4,
        difficulty="medium",
    )


# ---------------------------------------------------------------------------
# 47. Exponential Applications: Radioactive Half-Life Decay
# ---------------------------------------------------------------------------
def build_47_exponential_half_life_decay(r: random.Random) -> Dict[str, Any]:
    half_life = r.choice([4, 6, 8, 12])
    n_periods = r.choice([2, 3, 4])
    total_time = half_life * n_periods
    initial_mass = (2 ** n_periods) * r.choice([5, 10, 15])
    final_mass = initial_mass // (2 ** n_periods)

    prompt = (
        f"A radioactive isotope has a half-life of ${half_life}$ hours. Initial mass is ${initial_mass}\\text{{ g}}$. "
        f"What mass remains after ${total_time}$ hours according to $N(t) = N_0 \\left(\\frac{{1}}{{2}}\\right)^{{\\frac{{t}}{{T}}}}$?"
    )

    sol = solution_graph(
        goal="Calculate remaining radioactive mass after multiple half-lives",
        chain_type="calculation",
        steps=[
            step(from_latex=f"n = \\frac{{{total_time}}}{{{half_life}}} = {n_periods}", to_latex_str=f"N = {initial_mass}\\left(\\frac{{1}}{{2}}\\right)^{{{n_periods}}}", op="Find number of half-lives", rule="n = t/T"),
            step(from_latex=f"N = {initial_mass} \\times \\frac{{1}}{{{2 ** n_periods}}}", to_latex_str=f"N = {final_mass}\\text{{ g}}", op="Evaluate final mass", rule=f"N = {final_mass}"),
        ],
        final_latex=str(final_mass),
    )

    return make_math_question(
        prefix="g11_exp",
        topic=TOPIC,
        subskill="47_exponential_half_life_decay",
        learning_objective_id=f"{LO_PREFIX}_47",
        prompt=prompt,
        prompt_latex=prompt,
        answer_mode="typed",
        question_type="math_short",
        answer_latex=str(final_mass),
        answer_sympy=str(final_mass),
        sample_answer=str(final_mass),
        canonical_solution=sol,
        marking_schema={"total_marks": 3, "steps": [{"desc": "Find n", "marks": 1}, {"desc": "Decay factor", "marks": 1}, {"desc": f"{final_mass} g", "marks": 1}]},
        hints={"nudge": f"Divide total time ({total_time}) by half-life ({half_life}) to find the number of periods.", "concept": "N = N0 * (1/2)^n.", "breakdown": f"n = {n_periods}. N = {initial_mass} / {2**n_periods} = {final_mass} g."},
        misconception_tags=["confusing_half_life_period_with_decay_constant"],
        term=1,
        caps_weight_percent=15,
        suggested_duration_mins=4,
        difficulty="medium",
    )


# ---------------------------------------------------------------------------
# 48. Exponential Applications: Bacterial Doubling Model
# ---------------------------------------------------------------------------
def build_48_exponential_bacterial_doubling_model(r: random.Random) -> Dict[str, Any]:
    doubling_time_mins = r.choice([20, 30, 40])
    n_intervals = r.choice([3, 4, 5])
    total_time_mins = doubling_time_mins * n_intervals
    initial_count = r.choice([100, 200, 500])
    final_count = initial_count * (2 ** n_intervals)

    prompt = (
        f"A bacteria culture begins with ${initial_count}$ bacteria and doubles every ${doubling_time_mins}$ minutes. "
        f"How many bacteria are present after ${total_time_mins}$ minutes ($N = N_0 \\cdot 2^n$)?"
    )

    sol = solution_graph(
        goal="Calculate bacterial doubling population",
        chain_type="calculation",
        steps=[
            step(from_latex=f"n = \\frac{{{total_time_mins}}}{{{doubling_time_mins}}} = {n_intervals}", to_latex_str=f"N = {initial_count} \\cdot 2^{{{n_intervals}}}", op="Find doubling intervals", rule="n = t / T_double"),
            step(from_latex=f"N = {initial_count} \\times {2 ** n_intervals}", to_latex_str=f"N = {final_count}", op="Multiply by initial population", rule=f"N = {final_count}"),
        ],
        final_latex=str(final_count),
    )

    return make_math_question(
        prefix="g11_exp",
        topic=TOPIC,
        subskill="48_exponential_bacterial_doubling_model",
        learning_objective_id=f"{LO_PREFIX}_48",
        prompt=prompt,
        prompt_latex=prompt,
        answer_mode="typed",
        question_type="math_short",
        answer_latex=str(final_count),
        answer_sympy=str(final_count),
        sample_answer=str(final_count),
        canonical_solution=sol,
        marking_schema={"total_marks": 3, "steps": [{"desc": "Find intervals n", "marks": 1}, {"desc": "2^n", "marks": 1}, {"desc": f"Total {final_count}", "marks": 1}]},
        hints={"nudge": f"Number of intervals = {total_time_mins} / {doubling_time_mins}.", "concept": "N = N0 * 2^n.", "breakdown": f"n = {n_intervals}. N = {initial_count} * {2**n_intervals} = {final_count}."},
        misconception_tags=["multiplying_by_two_instead_of_two_to_power_n"],
        term=1,
        caps_weight_percent=15,
        suggested_duration_mins=4,
        difficulty="medium",
    )


# ---------------------------------------------------------------------------
# 49. Advanced Surds: Nested Radical Simplification
# ---------------------------------------------------------------------------
def build_49_simplify_nested_radical_surd(r: random.Random) -> Dict[str, Any]:
    pair = r.choice([(3, 2, 5, 6), (5, 2, 7, 10), (5, 3, 8, 15), (7, 2, 9, 14), (7, 3, 10, 21)])
    x, y, a, b = pair

    expr_latex = f"\\sqrt{{{a} + 2\\sqrt{{{b}}}}}"
    ans_latex = f"\\sqrt{{{x}}} + \\sqrt{{{y}}}"
    prompt = f"Simplify the nested radical into the form $\\sqrt{{x}} + \\sqrt{{y}}$:\n\n$${expr_latex}$$"

    sol = solution_graph(
        goal="Simplify nested radical by completing square under radical",
        chain_type="expression",
        steps=[
            step(from_latex=expr_latex, to_latex_str=f"\\sqrt{{{x} + 2\\sqrt{{{x * y}}} + {y}}}", op=f"Find x, y such that x+y={a} and xy={b}", rule=f"{x}+{y}={a}, {x}*{y}={b}"),
            step(from_latex=f"\\sqrt{{\\left(\\sqrt{{{x}}} + \\sqrt{{{y}}}\\right)^2}}", to_latex_str=ans_latex, op="Extract root of perfect square", rule="sqrt(u^2) = u"),
        ],
        final_latex=ans_latex,
    )

    return make_math_question(
        prefix="g11_exp",
        topic=TOPIC,
        subskill="49_simplify_nested_radical_surd",
        learning_objective_id=f"{LO_PREFIX}_49",
        prompt=prompt,
        prompt_latex=prompt,
        answer_mode="typed",
        question_type="math_short",
        answer_latex=ans_latex,
        answer_sympy=f"sqrt({x}) + sqrt({y})",
        sample_answer=ans_latex,
        canonical_solution=sol,
        marking_schema={"total_marks": 3, "steps": [{"desc": "Find x and y", "marks": 1}, {"desc": "Perfect square form", "marks": 1}, {"desc": f"Answer {ans_latex}", "marks": 1}]},
        hints={"nudge": f"Find two numbers that multiply to {b} and add to {a}.", "concept": "(√x + √y)² = x + y + 2√(xy).", "breakdown": f"\\sqrt{{{a} + 2\\sqrt{{{b}}}}} = \\sqrt{{(\\sqrt{{{x}}} + \\sqrt{{{y}}})²}} = {ans_latex}."},
        misconception_tags=["failing_to_recognize_perfect_square_in_nested_radical"],
        term=1,
        caps_weight_percent=15,
        suggested_duration_mins=4,
        difficulty="hard",
    )


# ---------------------------------------------------------------------------
# 50. Comprehensive Exponents and Surds Synthesis
# ---------------------------------------------------------------------------
def build_50_comprehensive_exponents_surds_synthesis(r: random.Random) -> Dict[str, Any]:
    c_exp = r.choice([1, 2])
    if c_exp == 1:
        int_part = 3
        surd_num = 6
        surd_ans_coef = 2
        prime_rad = 3
    else:
        int_part = 5
        surd_num = 4
        surd_ans_coef = 2
        prime_rad = 2

    expr_latex = f"\\frac{{2^{{x + {c_exp}}} + 2^x}}{{2^x}} + \\frac{{{surd_num}}}{{\\sqrt{{{prime_rad}}}}}"
    ans_latex = f"{int_part} + {surd_ans_coef}\\sqrt{{{prime_rad}}}"
    prompt = f"Simplify into the form $a + b\\sqrt{{c}}$:\n\n$${expr_latex}$$"

    sol = solution_graph(
        goal="Synthesize exponential factorisation and surd rationalisation",
        chain_type="expression",
        steps=[
            step(from_latex=f"\\frac{{2^{{x + {c_exp}}} + 2^x}}{{2^x}}", to_latex_str=f"{int_part}", op="Simplify exponential fraction", rule="Common factor cancellation"),
            step(from_latex=f"\\frac{{{surd_num}}}{{\\sqrt{{{prime_rad}}}}}", to_latex_str=f"{surd_ans_coef}\\sqrt{{{prime_rad}}}", op="Rationalise denominator", rule="Monomial rationalisation"),
            step(from_latex=f"{int_part} + {surd_ans_coef}\\sqrt{{{prime_rad}}}", to_latex_str=ans_latex, op="Combine terms", rule="Final synthesis"),
        ],
        final_latex=ans_latex,
    )

    return make_math_question(
        prefix="g11_exp",
        topic=TOPIC,
        subskill="50_comprehensive_exponents_surds_synthesis",
        learning_objective_id=f"{LO_PREFIX}_50",
        prompt=prompt,
        prompt_latex=prompt,
        answer_mode="typed",
        question_type="math_short",
        answer_latex=ans_latex,
        answer_sympy=f"{int_part} + {surd_ans_coef}*sqrt({prime_rad})",
        sample_answer=ans_latex,
        canonical_solution=sol,
        marking_schema={"total_marks": 4, "steps": [{"desc": f"Exponential part = {int_part}", "marks": 2}, {"desc": "Rationalise surd part", "marks": 1}, {"desc": f"Answer {ans_latex}", "marks": 1}]},
        hints={"nudge": "Simplify the exponential fraction first, then rationalise the surd fraction.", "concept": "Factor out 2^x from the first term. Multiply top and bottom of the second term by √c.", "breakdown": f"Term 1 = {int_part}. Term 2 = {surd_ans_coef}√{prime_rad}. Total = {ans_latex}."},
        misconception_tags=["combining_integer_and_surd_coefficients_illegally"],
        term=1,
        caps_weight_percent=15,
        suggested_duration_mins=5,
        difficulty="hard",
    )


# ---------------------------------------------------------------------------
# Registry of Archetypes 26–50
# ---------------------------------------------------------------------------
BUILDERS_26_50: Dict[str, Any] = {
    "26_exponential_equation_equal_bases": build_26_exponential_equation_equal_bases,
    "27_exponential_equation_prime_base_reduction": build_27_exponential_equation_prime_base_reduction,
    "28_exponential_equation_fractional_power_linear": build_28_exponential_equation_fractional_power_linear,
    "29_exponential_equation_negative_fractional_power": build_29_exponential_equation_negative_fractional_power,
    "30_exponential_equation_common_factor_extraction": build_30_exponential_equation_common_factor_extraction,
    "31_exponential_equation_common_factor_subtraction": build_31_exponential_equation_common_factor_subtraction,
    "32_exponential_equation_k_substitution_distinct_roots": build_32_exponential_equation_k_substitution_distinct_roots,
    "33_exponential_equation_k_substitution_one_extraneous": build_33_exponential_equation_k_substitution_one_extraneous,
    "34_exponential_equation_k_substitution_fractional": build_34_exponential_equation_k_substitution_fractional,
    "35_surd_equation_simple_isolated_radical": build_35_surd_equation_simple_isolated_radical,
    "36_surd_equation_isolate_before_squaring": build_36_surd_equation_isolate_before_squaring,
    "37_surd_equation_linear_rhs_one_valid_root": build_37_surd_equation_linear_rhs_one_valid_root,
    "38_surd_equation_linear_rhs_two_valid_roots": build_38_surd_equation_linear_rhs_two_valid_roots,
    "39_surd_equation_with_extraneous_root_identification": build_39_surd_equation_with_extraneous_root_identification,
    "40_surd_equation_k_substitution": build_40_surd_equation_k_substitution,
    "41_surd_equation_quadratic_expression_under_radical": build_41_surd_equation_quadratic_expression_under_radical,
    "42_surd_equation_two_radicals_basic": build_42_surd_equation_two_radicals_basic,
    "43_surd_expression_undefined_condition": build_43_surd_expression_undefined_condition,
    "44_nature_of_roots_discriminant_surd_connection": build_44_nature_of_roots_discriminant_surd_connection,
    "45_exponential_growth_compound_formula": build_45_exponential_growth_compound_formula,
    "46_exponential_decay_depreciation_model": build_46_exponential_decay_depreciation_model,
    "47_exponential_half_life_decay": build_47_exponential_half_life_decay,
    "48_exponential_bacterial_doubling_model": build_48_exponential_bacterial_doubling_model,
    "49_simplify_nested_radical_surd": build_49_simplify_nested_radical_surd,
    "50_comprehensive_exponents_surds_synthesis": build_50_comprehensive_exponents_surds_synthesis,
}
