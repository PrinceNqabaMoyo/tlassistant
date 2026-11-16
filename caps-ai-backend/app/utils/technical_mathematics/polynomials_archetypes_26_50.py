"""Grade 12 Technical Mathematics — Polynomials & Cubic Equations (Subskills 26–50).
Grounded strictly in curriculum_docs_auto/TechnicalMathematics_Gr12/Term 1/02. Polynomials.md.
Covers:
- Factorising cubic polynomials by inspection, grouping, and factor theorem
- Solving cubic equations with distinct, repeated, and surd real roots
- Non-monic cubics, fractional roots, and algebraic rearrangements
- Exponential substitutions reducible to cubic equations
- Technical engineering applications (sheet metal tray volume, beam deflection, hopper design)
Zero-LLM: 100% deterministic calculations with South African comma decimals ({,}) and inline SVG specs.
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional, Tuple
import sympy as sp

x = sp.Symbol("x")


def _svg_wrap(inner_svg: str, width: int = 360, height: int = 220) -> str:
    """Helper to wrap SVG elements in standard canvas."""
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
        f'width="{width}" height="{height}" style="background-color: #f8fafc; border: 1px solid #e2e8f0; border-radius: 6px;">'
        f"{inner_svg}</svg>"
    )


# =========================================================================== #
# Subskill 26: Factorise Cubic by Grouping Four Terms
# =========================================================================== #
def build_26_factorise_cubic_grouping_four_terms(rng: random.Random) -> Dict[str, Any]:
    # x^3 + a*x^2 - b^2*x - a*b^2 = x^2(x + a) - b^2(x + a) = (x + a)(x - b)(x + b)
    a = rng.choice([1, 2, 3, 4, 5])
    b = rng.choice([2, 3, 4, 5])
    b2 = b * b
    c0 = a * b2

    poly = x**3 + a*x**2 - b2*x - c0
    poly_latex = sp.latex(poly)

    prompt = (
        f"Factorise the cubic polynomial completely by grouping pairs of terms:\n\n"
        f"$${poly_latex}$$"
    )

    ans_latex = f"(x + {a})(x - {b})(x + {b})"
    ans_sympy = f"(x + {a})*(x - {b})*(x + {b})"

    sample = (
        f"\\text{{Group the first two terms and the last two terms:}}\\\\\n"
        f"x^3 + {a}x^2 - {b2}x - {c0} = x^2(x + {a}) - {b2}(x + {a})\\\\\n"
        f"= (x + {a})(x^2 - {b2})\\\\\n"
        f"= (x + {a})(x - {b})(x + {b}) \\quad (\\text{{difference of two squares}})."
    )

    return {
        "id": f"tech_poly_26_{rng.randint(100000, 999999)}",
        "question_id": f"tech_poly_26_{rng.randint(100000, 999999)}",
        "topic": "technical_mathematics_polynomials",
        "subskill": "26_factorise_cubic_grouping_four_terms",
        "learning_objective_id": "techmath_poly_factorise_cubic_grouping",
        "question_text": prompt,
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "answer_sympy": ans_sympy,
        "expected_answer": ans_latex,
        "sample_answer": sample,
        "worked_solution": sample,
        "marks": 3,
        "term": 1,
        "caps_weight_percent": 25,
        "suggested_duration_mins": 4,
        "mode": "elementary_factorisation",
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": f"Group pairs and factor out common binomial: (x + {a})(x^2 - {b2})", "marks": 1},
                {"id": "mp2", "desc": "Recognise difference of two squares", "marks": 1},
                {"id": "mp3", "desc": f"Complete linear factors: {ans_latex}", "marks": 1},
            ],
        },
        "hints": {
            "1_nudge": "Look at the first two terms x^3 + ax^2 and the last two terms -b^2x - ab^2 separately.",
            "2_concept": f"Take out x^2 from the first pair and -{b2} from the second pair to reveal (x + {a}).",
            "3_breakdown": f"Factor x^2 - {b2} into (x - {b})(x + {b}). Final answer: {ans_latex}.",
        },
        "misconception_tags": ["sign_error_grouping", "incomplete_factorisation_difference_squares"],
    }


# =========================================================================== #
# Subskill 27: Factorise Cubic with Common Monomial Factor
# =========================================================================== #
def build_27_factorise_cubic_common_monomial_factor(rng: random.Random) -> Dict[str, Any]:
    # x(x - r1)(x - r2)
    r1 = rng.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])
    r2 = rng.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])
    while r1 == r2 or r1 == 0 or r2 == 0:
        r2 = rng.choice([2, 3, 4])

    quad = (x - r1) * (x - r2)
    poly = x * sp.expand(quad)
    poly_latex = sp.latex(poly)

    f1 = f"(x - {r1})" if r1 > 0 else f"(x + {-r1})"
    f2 = f"(x - {r2})" if r2 > 0 else f"(x + {-r2})"
    ans_latex = f"x{f1}{f2}"

    prompt = (
        f"Factorise the cubic polynomial completely by first taking out a common monomial factor:\n\n"
        f"$${poly_latex}$$"
    )

    quad_exp = sp.expand(quad)
    sample = (
        f"\\text{{Step 1: Take out the common factor of }} x:\\\\\n"
        f"{poly_latex} = x({sp.latex(quad_exp)})\\\\\n"
        f"\\text{{Step 2: Factorise the quadratic trinomial:}}\\\\\n"
        f"= x{f1}{f2}."
    )

    return {
        "id": f"tech_poly_27_{rng.randint(100000, 999999)}",
        "question_id": f"tech_poly_27_{rng.randint(100000, 999999)}",
        "topic": "technical_mathematics_polynomials",
        "subskill": "27_factorise_cubic_common_monomial_factor",
        "learning_objective_id": "techmath_poly_factorise_monomial",
        "question_text": prompt,
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "answer_sympy": f"x*(x - {r1})*(x - {r2})",
        "expected_answer": ans_latex,
        "sample_answer": sample,
        "worked_solution": sample,
        "marks": 3,
        "term": 1,
        "caps_weight_percent": 25,
        "suggested_duration_mins": 3,
        "mode": "elementary_factorisation",
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": "Take out common factor x", "marks": 1},
                {"id": "mp2", "desc": "Factorise quadratic trinomial", "marks": 1},
                {"id": "mp3", "desc": f"Correct completely factorised expression {ans_latex}", "marks": 1},
            ],
        },
        "hints": {
            "1_nudge": "Every term contains at least one power of x. Factor x out first.",
            "2_concept": f"After factoring x, factorise the quadratic trinomial {sp.latex(quad_exp)}.",
            "3_breakdown": f"Factors are {ans_latex}.",
        },
        "misconception_tags": ["omitting_monomial_factor", "trinomial_sign_error"],
    }


# =========================================================================== #
# Subskill 28: Factorise Cubic Monic by Trial Factor & Inspection
# =========================================================================== #
def build_28_factorise_cubic_monic_trial_factor_inspection(rng: random.Random) -> Dict[str, Any]:
    # (x - r1)(x - r2)(x - r3) where r1 in {1, -1, 2, -2}
    r1 = rng.choice([-2, -1, 1, 2])
    r2 = rng.choice([-4, -3, 3, 4])
    r3 = rng.choice([-5, 5])

    poly = sp.expand((x - r1) * (x - r2) * (x - r3))
    poly_latex = sp.latex(poly)
    quad = sp.expand((x - r2) * (x - r3))

    f1 = f"(x - {r1})" if r1 > 0 else f"(x + {-r1})"
    f2 = f"(x - {r2})" if r2 > 0 else f"(x + {-r2})"
    f3 = f"(x - {r3})" if r3 > 0 else f"(x + {-r3})"
    ans_latex = f"{f1}{f2}{f3}"

    prompt = (
        f"Use the Factor Theorem and inspection to factorise the polynomial completely:\n\n"
        f"$$f(x) = {poly_latex}$$"
    )

    sample = (
        f"\\text{{Step 1: Test factors of the constant term using the Factor Theorem:}}\\\\\n"
        f"f({r1}) = 0 \\implies {f1} \\text{{ is a factor.}}\\\\\n"
        f"\\text{{Step 2: Determine the quadratic factor by inspection:}}\\\\\n"
        f"{poly_latex} = {f1}({sp.latex(quad)})\\\\\n"
        f"\\text{{Step 3: Factorise the quadratic expression:}}\\\\\n"
        f"= {ans_latex}."
    )

    return {
        "id": f"tech_poly_28_{rng.randint(100000, 999999)}",
        "question_id": f"tech_poly_28_{rng.randint(100000, 999999)}",
        "topic": "technical_mathematics_polynomials",
        "subskill": "28_factorise_cubic_monic_trial_factor_inspection",
        "learning_objective_id": "techmath_poly_factorise_monic_inspection",
        "question_text": prompt,
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "answer_sympy": f"(x - {r1})*(x - {r2})*(x - {r3})",
        "expected_answer": ans_latex,
        "sample_answer": sample,
        "worked_solution": sample,
        "marks": 4,
        "term": 1,
        "caps_weight_percent": 25,
        "suggested_duration_mins": 5,
        "mode": "elementary_factorisation",
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp1", "desc": f"Find initial rational root x = {r1} so that f({r1}) = 0", "marks": 1},
                {"id": "mp2", "desc": f"State first linear factor {f1}", "marks": 1},
                {"id": "mp3", "desc": f"Determine quotient quadratic factor ({sp.latex(quad)})", "marks": 1},
                {"id": "mp4", "desc": f"Complete factorisation: {ans_latex}", "marks": 1},
            ],
        },
        "hints": {
            "1_nudge": f"Test integer factors of the constant term: try substituting x = {r1}.",
            "2_concept": f"Since f({r1}) = 0, {f1} is a factor. Divide or inspect to find the quadratic factor.",
            "3_breakdown": f"Quotient is {sp.latex(quad)} which factors into {f2}{f3}.",
        },
        "misconception_tags": ["factor_theorem_sign_confusion", "middle_term_inspection_error"],
    }


# =========================================================================== #
# Subskill 29: Factorise Cubic Monic with Difference of Squares Quotient
# =========================================================================== #
def build_29_factorise_cubic_monic_difference_of_squares_quotient(rng: random.Random) -> Dict[str, Any]:
    # (x - r1)(x^2 - k^2)
    r1 = rng.choice([-3, -2, -1, 1, 2, 3])
    k = rng.choice([2, 3, 4, 5])
    k2 = k * k

    poly = sp.expand((x - r1) * (x**2 - k2))
    poly_latex = sp.latex(poly)

    f1 = f"(x - {r1})" if r1 > 0 else f"(x + {-r1})"
    ans_latex = f"{f1}(x - {k})(x + {k})"

    prompt = (
        f"Factorise the cubic polynomial completely into three linear factors:\n\n"
        f"$$g(x) = {poly_latex}$$"
    )

    sample = (
        f"\\text{{Test }} x = {r1}: g({r1}) = 0 \\implies {f1} \\text{{ is a factor.}}\\\\\n"
        f"g(x) = {f1}(x^2 - {k2})\\\\\n"
        f"= {ans_latex} \\quad (\\text{{difference of two squares}})."
    )

    return {
        "id": f"tech_poly_29_{rng.randint(100000, 999999)}",
        "question_id": f"tech_poly_29_{rng.randint(100000, 999999)}",
        "topic": "technical_mathematics_polynomials",
        "subskill": "29_factorise_cubic_monic_difference_of_squares_quotient",
        "learning_objective_id": "techmath_poly_factorise_diff_squares",
        "question_text": prompt,
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "answer_sympy": f"(x - {r1})*(x - {k})*(x + {k})",
        "expected_answer": ans_latex,
        "sample_answer": sample,
        "worked_solution": sample,
        "marks": 3,
        "term": 1,
        "caps_weight_percent": 25,
        "suggested_duration_mins": 4,
        "mode": "elementary_factorisation",
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": f"Identify factor {f1}", "marks": 1},
                {"id": "mp2", "desc": f"Obtain quadratic factor (x^2 - {k2})", "marks": 1},
                {"id": "mp3", "desc": f"Complete linear factors {ans_latex}", "marks": 1},
            ],
        },
        "hints": {
            "1_nudge": f"Show that g({r1}) = 0 to establish {f1} as a factor.",
            "2_concept": f"The quadratic factor is (x^2 - {k2}), which is a difference of two squares.",
            "3_breakdown": f"Factor x^2 - {k2} into (x - {k})(x + {k}).",
        },
        "misconception_tags": ["incomplete_factorisation", "difference_of_squares_sign_error"],
    }


# =========================================================================== #
# Subskill 30: Factorise Cubic Monic with Perfect Square Quotient
# =========================================================================== #
def build_30_factorise_cubic_monic_perfect_square_quotient(rng: random.Random) -> Dict[str, Any]:
    # (x - r1)(x - r2)^2
    r1 = rng.choice([-3, -2, -1, 1, 2, 3])
    r2 = rng.choice([-4, -2, 2, 4])
    while r1 == r2:
        r2 = rng.choice([-5, 5])

    poly = sp.expand((x - r1) * (x - r2)**2)
    poly_latex = sp.latex(poly)

    f1 = f"(x - {r1})" if r1 > 0 else f"(x + {-r1})"
    f2 = f"(x - {r2})" if r2 > 0 else f"(x + {-r2})"
    ans_latex = f"{f1}{f2}^2"

    prompt = (
        f"Factorise the cubic polynomial completely. Write your answer using index notation for any repeated factors:\n\n"
        f"$$p(x) = {poly_latex}$$"
    )

    quad = sp.expand((x - r2)**2)
    sample = (
        f"\\text{{Test }} x = {r1}: p({r1}) = 0 \\implies {f1} \\text{{ is a factor.}}\\\\\n"
        f"p(x) = {f1}({sp.latex(quad)})\\\\\n"
        f"\\text{{Notice that }} {sp.latex(quad)} \\text{{ is a perfect square: }}\\\\\n"
        f"= {f1}{f2}^2."
    )

    return {
        "id": f"tech_poly_30_{rng.randint(100000, 999999)}",
        "question_id": f"tech_poly_30_{rng.randint(100000, 999999)}",
        "topic": "technical_mathematics_polynomials",
        "subskill": "30_factorise_cubic_monic_perfect_square_quotient",
        "learning_objective_id": "techmath_poly_factorise_perfect_square",
        "question_text": prompt,
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "answer_sympy": f"(x - {r1})*(x - {r2})**2",
        "expected_answer": ans_latex,
        "sample_answer": sample,
        "worked_solution": sample,
        "marks": 3,
        "term": 1,
        "caps_weight_percent": 25,
        "suggested_duration_mins": 4,
        "mode": "elementary_factorisation",
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": f"Identify factor {f1}", "marks": 1},
                {"id": "mp2", "desc": f"Determine quotient {sp.latex(quad)}", "marks": 1},
                {"id": "mp3", "desc": f"Write as {ans_latex}", "marks": 1},
            ],
        },
        "hints": {
            "1_nudge": f"Substitute x = {r1} to verify that {f1} is a factor.",
            "2_concept": f"The remaining quadratic is a perfect square trinomial: {sp.latex(quad)} = {f2}^2.",
            "3_breakdown": f"Final factorisation: {ans_latex}.",
        },
        "misconception_tags": ["omitting_square_index", "perfect_square_sign_inversion"],
    }


# =========================================================================== #
# Subskill 31: Factorise Cubic with Leading Coefficient Two
# =========================================================================== #
def build_31_factorise_cubic_non_monic_leading_coeff_two(rng: random.Random) -> Dict[str, Any]:
    # (x - r1)(2x - r2)(x - r3) where r2 is odd integer
    r1 = rng.choice([-2, -1, 1, 2])
    r2 = rng.choice([-3, -1, 1, 3])
    r3 = rng.choice([-3, 3])

    poly = sp.expand((x - r1) * (2*x - r2) * (x - r3))
    poly_latex = sp.latex(poly)
    quad = sp.expand((2*x - r2) * (x - r3))

    f1 = f"(x - {r1})" if r1 > 0 else f"(x + {-r1})"
    f2 = f"(2x - {r2})" if r2 > 0 else f"(2x + {-r2})"
    f3 = f"(x - {r3})" if r3 > 0 else f"(x + {-r3})"
    ans_latex = f"{f1}{f2}{f3}"

    prompt = (
        f"Factorise the non-monic cubic polynomial completely:\n\n"
        f"$$f(x) = {poly_latex}$$"
    )

    sample = (
        f"\\text{{Test factors of constant term }} {int(poly.subs(x, 0))}:\\\\\n"
        f"f({r1}) = 0 \\implies {f1} \\text{{ is a factor.}}\\\\\n"
        f"\\text{{Divide by }} {f1} \\text{{ to obtain the quadratic factor:}}\\\\\n"
        f"{poly_latex} = {f1}({sp.latex(quad)})\\\\\n"
        f"\\text{{Factorise the non-monic quadratic:}}\\\\\n"
        f"= {ans_latex}."
    )

    return {
        "id": f"tech_poly_31_{rng.randint(100000, 999999)}",
        "question_id": f"tech_poly_31_{rng.randint(100000, 999999)}",
        "topic": "technical_mathematics_polynomials",
        "subskill": "31_factorise_cubic_non_monic_leading_coeff_two",
        "learning_objective_id": "techmath_poly_non_monic_factorise",
        "question_text": prompt,
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "answer_sympy": f"(x - {r1})*(2*x - {r2})*(x - {r3})",
        "expected_answer": ans_latex,
        "sample_answer": sample,
        "worked_solution": sample,
        "marks": 4,
        "term": 1,
        "caps_weight_percent": 25,
        "suggested_duration_mins": 5,
        "mode": "elementary_factorisation",
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp1", "desc": f"Verify f({r1}) = 0 and identify factor {f1}", "marks": 1},
                {"id": "mp2", "desc": f"Obtain quadratic factor ({sp.latex(quad)})", "marks": 2},
                {"id": "mp3", "desc": f"Complete factorisation: {ans_latex}", "marks": 1},
            ],
        },
        "hints": {
            "1_nudge": f"Test integer values first: x = {r1} gives f({r1}) = 0.",
            "2_concept": f"Divide by {f1} to find the quadratic ({sp.latex(quad)}).",
            "3_breakdown": f"Factor the quadratic into {f2}{f3}.",
        },
        "misconception_tags": ["non_monic_quadratic_factorisation_error", "dropped_leading_coefficient"],
    }


# =========================================================================== #
# Subskill 32: Factorise Cubic with Fractional Root Factor
# =========================================================================== #
def build_32_factorise_cubic_non_monic_fractional_root(rng: random.Random) -> Dict[str, Any]:
    # (3x - 1)(x - r2)(x - r3)
    c_lead = rng.choice([2, 3])
    r1_num = rng.choice([-1, 1])
    r2 = rng.choice([-2, 2])
    r3 = rng.choice([-3, 3])

    poly = sp.expand((c_lead*x - r1_num) * (x - r2) * (x - r3))
    poly_latex = sp.latex(poly)

    f1 = f"({c_lead}x - {r1_num})" if r1_num > 0 else f"({c_lead}x + {-r1_num})"
    f2 = f"(x - {r2})" if r2 > 0 else f"(x + {-r2})"
    f3 = f"(x - {r3})" if r3 > 0 else f"(x + {-r3})"
    ans_latex = f"{f1}{f2}{f3}"

    prompt = (
        f"Factorise the polynomial completely, where one factor has a fractional root:\n\n"
        f"$$p(x) = {poly_latex}$$\n\n"
        f"Show all working, starting by testing rational roots of the form $\\frac{{p}}{{q}}$."
    )

    quad = sp.expand((x - r2) * (x - r3))
    sample = (
        f"\\text{{Test rational candidates: }} p\\left(\\frac{{{r1_num}}}{{{c_lead}}}\\right) = 0 \\implies {f1} \\text{{ is a factor.}}\\\\\n"
        f"p(x) = {f1}({sp.latex(quad)})\\\\\n"
        f"= {ans_latex}."
    )

    return {
        "id": f"tech_poly_32_{rng.randint(100000, 999999)}",
        "question_id": f"tech_poly_32_{rng.randint(100000, 999999)}",
        "topic": "technical_mathematics_polynomials",
        "subskill": "32_factorise_cubic_non_monic_fractional_root",
        "learning_objective_id": "techmath_poly_fractional_root_factor",
        "question_text": prompt,
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "answer_sympy": f"({c_lead}*x - {r1_num})*(x - {r2})*(x - {r3})",
        "expected_answer": ans_latex,
        "sample_answer": sample,
        "worked_solution": sample,
        "marks": 4,
        "term": 1,
        "caps_weight_percent": 25,
        "suggested_duration_mins": 5,
        "mode": "elementary_factorisation",
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp1", "desc": f"Identify rational root x = {r1_num}/{c_lead} and factor {f1}", "marks": 2},
                {"id": "mp2", "desc": f"Obtain quadratic quotient ({sp.latex(quad)})", "marks": 1},
                {"id": "mp3", "desc": f"Complete factorisation: {ans_latex}", "marks": 1},
            ],
        },
        "hints": {
            "1_nudge": f"Rational root theorem: test factors of constant term divided by factors of leading coefficient {c_lead}.",
            "2_concept": f"Substitute x = {r1_num}/{c_lead} to show p({r1_num}/{c_lead}) = 0.",
            "3_breakdown": f"Factorisation is {ans_latex}.",
        },
        "misconception_tags": ["rational_root_test_failure", "fractional_root_bracket_inversion"],
    }


# =========================================================================== #
# Subskill 33: Factorise Cubic with Irreducible Quadratic Factor over Reals
# =========================================================================== #
def build_33_factorise_cubic_irreducible_quadratic_factor(rng: random.Random) -> Dict[str, Any]:
    # (x - r1)(x^2 + b*x + c) where b^2 - 4c < 0
    r1 = rng.choice([-3, -2, -1, 1, 2, 3])
    b_val = rng.choice([2, 4])
    c_val = rng.choice([5, 8, 10])  # b^2 - 4c < 0 always

    quad = x**2 + b_val*x + c_val
    poly = sp.expand((x - r1) * quad)
    poly_latex = sp.latex(poly)

    f1 = f"(x - {r1})" if r1 > 0 else f"(x + {-r1})"
    quad_str = f"(x^2 + {b_val}x + {c_val})"
    ans_latex = f"{f1}{quad_str}"

    prompt = (
        f"Factorise the cubic polynomial $f(x) = {poly_latex}$ completely over the set of real numbers $\\mathbb{{R}}$, "
        f"verifying why the remaining quadratic factor cannot be factorised further."
    )

    disc = b_val**2 - 4*1*c_val
    sample = (
        f"\\text{{Test }} x = {r1}: f({r1}) = 0 \\implies {f1} \\text{{ is a factor.}}\\\\\n"
        f"f(x) = {f1}{quad_str}.\\\\\n"
        f"\\text{{Check discriminant of quadratic factor: }}\\\\\n"
        f"\\Delta = b^2 - 4ac = ({b_val})^2 - 4(1)({c_val}) = {disc} < 0.\\\\\n"
        f"\\text{{Since }} \\Delta < 0, {quad_str} \\text{{ has non-real roots and cannot be factorised further over }} \\mathbb{{R}}.\\\\\n"
        f"\\therefore f(x) = {ans_latex}."
    )

    return {
        "id": f"tech_poly_33_{rng.randint(100000, 999999)}",
        "question_id": f"tech_poly_33_{rng.randint(100000, 999999)}",
        "topic": "technical_mathematics_polynomials",
        "subskill": "33_factorise_cubic_irreducible_quadratic_factor",
        "learning_objective_id": "techmath_poly_irreducible_factor",
        "question_text": prompt,
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "answer_sympy": f"(x - {r1})*(x**2 + {b_val}*x + {c_val})",
        "expected_answer": ans_latex,
        "sample_answer": sample,
        "worked_solution": sample,
        "marks": 4,
        "term": 1,
        "caps_weight_percent": 25,
        "suggested_duration_mins": 5,
        "mode": "elementary_factorisation",
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp1", "desc": f"Identify factor {f1}", "marks": 1},
                {"id": "mp2", "desc": f"Obtain quadratic factor {quad_str}", "marks": 1},
                {"id": "mp3", "desc": f"Evaluate discriminant Delta = {disc} < 0", "marks": 1},
                {"id": "mp4", "desc": f"Conclude {ans_latex}", "marks": 1},
            ],
        },
        "hints": {
            "1_nudge": f"First find the rational factor: test x = {r1}.",
            "2_concept": f"Calculate the discriminant b^2 - 4ac for {quad_str}.",
            "3_breakdown": f"Since Delta = {disc} < 0, the quadratic has no real linear factors. Answer: {ans_latex}.",
        },
        "misconception_tags": ["forcing_non_real_factorisation", "discriminant_calculation_error"],
    }


# =========================================================================== #
# Subskill 34: Solve Cubic with Three Distinct Integer Roots (Monic)
# =========================================================================== #
def build_34_solve_cubic_three_distinct_integer_roots_monic(rng: random.Random) -> Dict[str, Any]:
    # (x - r1)(x - r2)(x - r3) = 0
    roots = rng.sample([-4, -3, -2, -1, 1, 2, 3, 4], 3)
    roots.sort()
    r1, r2, r3 = roots

    poly = sp.expand((x - r1) * (x - r2) * (x - r3))
    poly_latex = sp.latex(poly)
    quad = sp.expand((x - r2) * (x - r3))

    f1 = f"(x - {r1})" if r1 > 0 else f"(x + {-r1})"
    roots_str = f"x = {r1} \\text{{ or }} x = {r2} \\text{{ or }} x = {r3}"

    prompt = (
        f"Solve for $x$ in the cubic equation:\n\n"
        f"$${poly_latex} = 0$$\n\n"
        f"Show all steps, including finding the first root using the Factor Theorem."
    )

    sample = (
        f"\\text{{Let }} f(x) = {poly_latex}.\\\\\n"
        f"\\text{{Testing integer factors: }} f({r1}) = 0 \\implies {f1} \\text{{ is a factor.}}\\\\\n"
        f"{poly_latex} = {f1}({sp.latex(quad)}) = 0\\\\\n"
        f"{f1}(x - {r2})(x - {r3}) = 0\\\\\n"
        f"\\therefore {roots_str}."
    )

    return {
        "id": f"tech_poly_34_{rng.randint(100000, 999999)}",
        "question_id": f"tech_poly_34_{rng.randint(100000, 999999)}",
        "topic": "technical_mathematics_polynomials",
        "subskill": "34_solve_cubic_three_distinct_integer_roots_monic",
        "learning_objective_id": "techmath_poly_solve_cubic_monic",
        "question_text": prompt,
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": roots_str,
        "answer_sympy": f"[{r1}, {r2}, {r3}]",
        "expected_answer": f"x = {r1} or x = {r2} or x = {r3}",
        "sample_answer": sample,
        "worked_solution": sample,
        "marks": 5,
        "term": 1,
        "caps_weight_percent": 25,
        "suggested_duration_mins": 6,
        "mode": "compound",
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp1", "desc": f"Identify first root x = {r1} by factor theorem", "marks": 1},
                {"id": "mp2", "desc": f"State first linear factor {f1}", "marks": 1},
                {"id": "mp3", "desc": f"Determine quotient quadratic ({sp.latex(quad)})", "marks": 1},
                {"id": "mp4", "desc": "Factorise quadratic into two linear factors", "marks": 1},
                {"id": "mp5", "desc": f"State all three solutions {roots_str}", "marks": 1},
            ],
        },
        "hints": {
            "1_nudge": f"Test factors of the constant term: x = {r1} is a root.",
            "2_concept": f"Divide the polynomial by {f1} to obtain ({sp.latex(quad)}) = 0.",
            "3_breakdown": f"Factorise ({sp.latex(quad)}) = 0 to get x = {r2} and x = {r3}.",
        },
        "misconception_tags": ["sign_inversion_root_to_factor", "omitting_roots"],
    }


# =========================================================================== #
# Subskill 35: Solve Cubic with Negative Constant Term
# =========================================================================== #
def build_35_solve_cubic_monic_with_negative_constant_term(rng: random.Random) -> Dict[str, Any]:
    # (x - r1)(x - r2)(x - r3) where product r1*r2*r3 is positive (so constant term is negative)
    # e.g. two negative roots and one positive root
    r1 = rng.choice([1, 2, 3])
    r2 = rng.choice([-3, -2, -1])
    r3 = rng.choice([-5, -4])

    poly = sp.expand((x - r1) * (x - r2) * (x - r3))
    poly_latex = sp.latex(poly)
    quad = sp.expand((x - r2) * (x - r3))

    f1 = f"(x - {r1})"
    roots_str = f"x = {r1} \\text{{ or }} x = {r2} \\text{{ or }} x = {r3}"

    prompt = (
        f"Solve for $x$ in the equation:\n\n"
        f"$${poly_latex} = 0$$"
    )

    sample = (
        f"\\text{{Test positive factor }} x = {r1}: f({r1}) = 0 \\implies {f1} \\text{{ is a factor.}}\\\\\n"
        f"{poly_latex} = {f1}({sp.latex(quad)}) = 0\\\\\n"
        f"{f1}(x - ({r2}))(x - ({r3})) = 0\\\\\n"
        f"\\therefore {roots_str}."
    )

    return {
        "id": f"tech_poly_35_{rng.randint(100000, 999999)}",
        "question_id": f"tech_poly_35_{rng.randint(100000, 999999)}",
        "topic": "technical_mathematics_polynomials",
        "subskill": "35_solve_cubic_monic_with_negative_constant_term",
        "learning_objective_id": "techmath_poly_solve_cubic_neg_const",
        "question_text": prompt,
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": roots_str,
        "answer_sympy": f"[{r1}, {r2}, {r3}]",
        "expected_answer": f"x = {r1} or x = {r2} or x = {r3}",
        "sample_answer": sample,
        "worked_solution": sample,
        "marks": 5,
        "term": 1,
        "caps_weight_percent": 25,
        "suggested_duration_mins": 6,
        "mode": "compound",
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp1", "desc": f"Find root x = {r1}", "marks": 1},
                {"id": "mp2", "desc": f"Divide by {f1}", "marks": 1},
                {"id": "mp3", "desc": f"Quotient {sp.latex(quad)}", "marks": 1},
                {"id": "mp4", "desc": "Factorise quotient", "marks": 1},
                {"id": "mp5", "desc": f"All roots: {roots_str}", "marks": 1},
            ],
        },
        "hints": {
            "1_nudge": f"Because the constant term is negative, test the positive factor x = {r1}.",
            "2_concept": f"Divide by {f1} to obtain the quadratic quotient.",
            "3_breakdown": f"Solutions are x = {r1}, x = {r2}, x = {r3}.",
        },
        "misconception_tags": ["constant_term_sign_confusion", "negative_root_sign_flip"],
    }


# =========================================================================== #
# Subskill 36: Solve Cubic with One Rational Root and Two Surd Roots
# =========================================================================== #
def build_36_solve_cubic_one_integer_two_surd_roots(rng: random.Random) -> Dict[str, Any]:
    # (x - r1)(x^2 - 2px + q) where Delta is non-square positive
    r1 = rng.choice([-2, -1, 1, 2])
    p = rng.choice([2, 3])
    # x^2 - 2px + 2 -> roots p +- sqrt(p^2 - 2)
    q_val = 2
    delta = 4*p*p - 4*q_val  # positive non-square

    poly = sp.expand((x - r1) * (x**2 - 2*p*x + q_val))
    poly_latex = sp.latex(poly)

    f1 = f"(x - {r1})" if r1 > 0 else f"(x + {-r1})"
    surd_rad = p*p - q_val
    ans_latex = f"x = {r1} \\text{{ or }} x = {p} \\pm \\sqrt{{{surd_rad}}}"

    prompt = (
        f"Solve for $x$ in the equation, leaving irrational roots in simplest surd form:\n\n"
        f"$${poly_latex} = 0$$"
    )

    sample = (
        f"\\text{{Step 1: Test }} x = {r1}: f({r1}) = 0 \\implies {f1} \\text{{ is a factor.}}\\\\\n"
        f"{poly_latex} = {f1}(x^2 - {2*p}x + {q_val}) = 0\\\\\n"
        f"\\text{{Step 2: Solve linear factor: }} x = {r1}\\\\\n"
        f"\\text{{Step 3: Solve quadratic factor using quadratic formula: }}\\\\\n"
        f"x = \\frac{{-({-2*p}) \\pm \\sqrt{{({-2*p})^2 - 4(1)({q_val})}}}}{{2(1)}} "
        f"= \\frac{{{2*p} \\pm \\sqrt{{{delta}}}}}{{2}} = {p} \\pm \\sqrt{{{surd_rad}}}.\\\\\n"
        f"\\therefore {ans_latex}."
    )

    return {
        "id": f"tech_poly_36_{rng.randint(100000, 999999)}",
        "question_id": f"tech_poly_36_{rng.randint(100000, 999999)}",
        "topic": "technical_mathematics_polynomials",
        "subskill": "36_solve_cubic_one_integer_two_surd_roots",
        "learning_objective_id": "techmath_poly_surd_roots",
        "question_text": prompt,
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "answer_sympy": f"[{r1}, '{p} + sqrt({surd_rad})', '{p} - sqrt({surd_rad})']",
        "expected_answer": f"x = {r1} or x = {p} +- sqrt({surd_rad})",
        "sample_answer": sample,
        "worked_solution": sample,
        "marks": 5,
        "term": 1,
        "caps_weight_percent": 25,
        "suggested_duration_mins": 6,
        "mode": "compound",
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp1", "desc": f"Find rational root x = {r1}", "marks": 1},
                {"id": "mp2", "desc": f"Obtain quadratic factor (x^2 - {2*p}x + {q_val})", "marks": 1},
                {"id": "mp3", "desc": "Apply quadratic formula with correct coefficients", "marks": 1},
                {"id": "mp4", "desc": f"Simplify surd to {p} +- sqrt({surd_rad})", "marks": 1},
                {"id": "mp5", "desc": f"State complete solution {ans_latex}", "marks": 1},
            ],
        },
        "hints": {
            "1_nudge": f"Show that x = {r1} is a rational root using the Factor Theorem.",
            "2_concept": f"Apply the quadratic formula to the remaining quadratic factor (x^2 - {2*p}x + {q_val}) = 0.",
            "3_breakdown": f"x = {r1} or x = {p} +- sqrt({surd_rad}).",
        },
        "misconception_tags": ["quadratic_formula_sign_error", "rounding_surd_to_decimal"],
    }


# =========================================================================== #
# Subskill 37: Solve Cubic with Repeated Double Root
# =========================================================================== #
def build_37_solve_cubic_repeated_double_root(rng: random.Random) -> Dict[str, Any]:
    # (x - r1)(x - r2)^2 = 0
    r1 = rng.choice([-3, -2, -1, 1, 2, 3])
    r2 = rng.choice([-4, -2, 2, 4])
    while r1 == r2:
        r2 = rng.choice([-5, 5])

    poly = sp.expand((x - r1) * (x - r2)**2)
    poly_latex = sp.latex(poly)

    f1 = f"(x - {r1})" if r1 > 0 else f"(x + {-r1})"
    f2 = f"(x - {r2})" if r2 > 0 else f"(x + {-r2})"
    ans_latex = f"x = {r1} \\text{{ or }} x = {r2} \\text{{ (multiplicity 2)}}"

    prompt = (
        f"Solve for $x$ in the cubic equation, noting any repeated roots:\n\n"
        f"$${poly_latex} = 0$$"
    )

    sample = (
        f"\\text{{Test }} x = {r1}: f({r1}) = 0 \\implies {f1} \\text{{ is a factor.}}\\\\\n"
        f"{poly_latex} = {f1}{f2}^2 = 0\\\\\n"
        f"\\therefore x = {r1} \\quad \\text{{or}} \\quad x = {r2} \\text{{ (repeated root)}}."
    )

    return {
        "id": f"tech_poly_37_{rng.randint(100000, 999999)}",
        "question_id": f"tech_poly_37_{rng.randint(100000, 999999)}",
        "topic": "technical_mathematics_polynomials",
        "subskill": "37_solve_cubic_repeated_double_root",
        "learning_objective_id": "techmath_poly_repeated_double_root",
        "question_text": prompt,
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "answer_sympy": f"[{r1}, {r2}]",
        "expected_answer": f"x = {r1} or x = {r2}",
        "sample_answer": sample,
        "worked_solution": sample,
        "marks": 4,
        "term": 1,
        "caps_weight_percent": 25,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp1", "desc": f"Find root x = {r1}", "marks": 1},
                {"id": "mp2", "desc": f"Factor out {f1}", "marks": 1},
                {"id": "mp3", "desc": f"Identify repeated factor {f2}^2", "marks": 1},
                {"id": "mp4", "desc": f"State roots x = {r1} or x = {r2}", "marks": 1},
            ],
        },
        "hints": {
            "1_nudge": f"Substitute x = {r1} to verify that {f1} is an initial factor.",
            "2_concept": f"The quotient is a perfect square trinomial.",
            "3_breakdown": f"Roots are x = {r1} and repeated root x = {r2}.",
        },
        "misconception_tags": ["treating_repeated_root_as_different", "dropping_multiplicity"],
    }


# =========================================================================== #
# Subskill 38: Solve Cubic with Repeated Triple Root
# =========================================================================== #
def build_38_solve_cubic_repeated_triple_root(rng: random.Random) -> Dict[str, Any]:
    # (x - r)^3 = x^3 - 3rx^2 + 3r^2x - r^3 = 0
    r_val = rng.choice([-3, -2, -1, 1, 2, 3])
    poly = sp.expand((x - r_val)**3)
    poly_latex = sp.latex(poly)

    f_linear = f"(x - {r_val})" if r_val > 0 else f"(x + {-r_val})"
    ans_latex = f"x = {r_val} \\text{{ (multiplicity 3)}}"

    prompt = (
        f"Solve for $x$ in the cubic equation:\n\n"
        f"$${poly_latex} = 0$$\n\n"
        f"Identify the multiplicity of the root."
    )

    sample = (
        f"\\text{{Notice that the expression is the binomial cube expansion of }} {f_linear}^3:\\\\\n"
        f"{poly_latex} = {f_linear}^3 = 0\\\\\n"
        f"\\therefore x = {r_val} \\text{{ with multiplicity 3 (three equal real roots)}}."
    )

    return {
        "id": f"tech_poly_38_{rng.randint(100000, 999999)}",
        "question_id": f"tech_poly_38_{rng.randint(100000, 999999)}",
        "topic": "technical_mathematics_polynomials",
        "subskill": "38_solve_cubic_repeated_triple_root",
        "learning_objective_id": "techmath_poly_triple_root",
        "question_text": prompt,
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "answer_sympy": str(r_val),
        "expected_answer": f"x = {r_val}",
        "sample_answer": sample,
        "worked_solution": sample,
        "marks": 3,
        "term": 1,
        "caps_weight_percent": 25,
        "suggested_duration_mins": 3,
        "mode": "elementary_factorisation",
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": f"Recognise or factorise into {f_linear}^3 = 0", "marks": 2},
                {"id": "mp2", "desc": f"Conclude x = {r_val} (triple root)", "marks": 1},
            ],
        },
        "hints": {
            "1_nudge": f"Look at the coefficients: 1, {-3*r_val}, {3*r_val**2}, {-r_val**3}.",
            "2_concept": f"This matches the expansion of (x - a)^3.",
            "3_breakdown": f"x = {r_val} (multiplicity 3).",
        },
        "misconception_tags": ["cube_formula_unrecognised", "missing_multiplicity"],
    }


# =========================================================================== #
# Subskill 39: Solve Non-Monic Cubic with Integer and Fractional Roots
# =========================================================================== #
def build_39_solve_cubic_non_monic_integer_and_fractional_roots(rng: random.Random) -> Dict[str, Any]:
    # (2x - r1)(x - r2)(x - r3) = 0 where r1 is odd integer
    r1 = rng.choice([-3, -1, 1, 3])
    r2 = rng.choice([-2, 2])
    r3 = rng.choice([-4, 4])

    poly = sp.expand((2*x - r1) * (x - r2) * (x - r3))
    poly_latex = sp.latex(poly)
    quad = sp.expand((2*x - r1) * (x - r3))

    f2 = f"(x - {r2})" if r2 > 0 else f"(x + {-r2})"
    frac_str = f"\\frac{{{r1}}}{{2}}" if r1 > 0 else f"-\\frac{{{-r1}}}{{2}}"
    roots_str = f"x = {frac_str} \\text{{ or }} x = {r2} \\text{{ or }} x = {r3}"

    prompt = (
        f"Solve for $x$ in the non-monic cubic equation:\n\n"
        f"$${poly_latex} = 0$$\n\n"
        f"Show all working, including finding an integer root first."
    )

    sample = (
        f"\\text{{Test integer factors of constant term: }} f({r2}) = 0 \\implies {f2} \\text{{ is a factor.}}\\\\\n"
        f"{poly_latex} = {f2}({sp.latex(quad)}) = 0\\\\\n"
        f"{f2}(2x - ({r1}))(x - ({r3})) = 0\\\\\n"
        f"\\therefore {roots_str}."
    )

    return {
        "id": f"tech_poly_39_{rng.randint(100000, 999999)}",
        "question_id": f"tech_poly_39_{rng.randint(100000, 999999)}",
        "topic": "technical_mathematics_polynomials",
        "subskill": "39_solve_cubic_non_monic_integer_and_fractional_roots",
        "learning_objective_id": "techmath_poly_solve_non_monic",
        "question_text": prompt,
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": roots_str,
        "answer_sympy": f"[{r1}/2, {r2}, {r3}]",
        "expected_answer": f"x = {r1}/2 or x = {r2} or x = {r3}",
        "sample_answer": sample,
        "worked_solution": sample,
        "marks": 5,
        "term": 1,
        "caps_weight_percent": 25,
        "suggested_duration_mins": 6,
        "mode": "compound",
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp1", "desc": f"Identify integer root x = {r2}", "marks": 1},
                {"id": "mp2", "desc": f"Obtain quadratic factor ({sp.latex(quad)})", "marks": 2},
                {"id": "mp3", "desc": "Solve quadratic factor", "marks": 1},
                {"id": "mp4", "desc": f"State solutions {roots_str}", "marks": 1},
            ],
        },
        "hints": {
            "1_nudge": f"Test integer factors first: x = {r2} makes the polynomial 0.",
            "2_concept": f"Divide by {f2} to obtain the non-monic quadratic factor.",
            "3_breakdown": f"Solve 2x - ({r1}) = 0 to get x = {frac_str}.",
        },
        "misconception_tags": ["fractional_root_omission", "synthetic_division_fraction_error"],
    }


# =========================================================================== #
# Subskill 40: Solve Cubic with Non-Zero RHS Rearrangement
# =========================================================================== #
def build_40_solve_cubic_non_zero_rhs_rearrangement(rng: random.Random) -> Dict[str, Any]:
    # Rearrange equation: x^3 + a*x^2 = b*x + c
    r1, r2, r3 = rng.sample([-3, -2, -1, 1, 2, 3], 3)
    r1, r2, r3 = sorted([r1, r2, r3])

    poly = sp.expand((x - r1) * (x - r2) * (x - r3))
    # Let LHS be x^3 + a*x^2 and RHS be -c1*x - c0
    c3 = 1
    c2 = -(r1 + r2 + r3)
    c1 = (r1*r2 + r1*r3 + r2*r3)
    c0 = -(r1 * r2 * r3)

    lhs = f"x^3 {'+ ' + str(c2) if c2 >= 0 else '- ' + str(abs(c2))}x^2"
    rhs = f"{-c1}x {'+ ' + str(-c0) if -c0 >= 0 else '- ' + str(abs(c0))}"

    roots_str = f"x = {r1} \\text{{ or }} x = {r2} \\text{{ or }} x = {r3}"

    prompt = (
        f"Solve for $x$ by first rewriting the equation in standard polynomial form:\n\n"
        f"$${lhs} = {rhs}$$"
    )

    sample = (
        f"\\text{{Rearrange all terms to LHS: }}\\\\\n"
        f"{sp.latex(poly)} = 0\\\\\n"
        f"\\text{{Test factors: }} f({r1}) = 0\\\\\n"
        f"\\text{{Factorise: }} (x - {r1})(x - {r2})(x - {r3}) = 0\\\\\n"
        f"\\therefore {roots_str}."
    )

    return {
        "id": f"tech_poly_40_{rng.randint(100000, 999999)}",
        "question_id": f"tech_poly_40_{rng.randint(100000, 999999)}",
        "topic": "technical_mathematics_polynomials",
        "subskill": "40_solve_cubic_non_zero_rhs_rearrangement",
        "learning_objective_id": "techmath_poly_rearrange_solve",
        "question_text": prompt,
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": roots_str,
        "answer_sympy": f"[{r1}, {r2}, {r3}]",
        "expected_answer": f"x = {r1} or x = {r2} or x = {r3}",
        "sample_answer": sample,
        "worked_solution": sample,
        "marks": 5,
        "term": 1,
        "caps_weight_percent": 25,
        "suggested_duration_mins": 6,
        "mode": "compound",
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp1", "desc": "Transpose terms to standard form ax^3 + bx^2 + cx + d = 0", "marks": 1},
                {"id": "mp2", "desc": f"Find first root x = {r1}", "marks": 1},
                {"id": "mp3", "desc": "Determine quotient quadratic factor", "marks": 1},
                {"id": "mp4", "desc": "Factorise quadratic", "marks": 1},
                {"id": "mp5", "desc": f"State solutions {roots_str}", "marks": 1},
            ],
        },
        "hints": {
            "1_nudge": "Always set the equation to zero by moving all terms to the left-hand side first.",
            "2_concept": f"Standard form is {sp.latex(poly)} = 0.",
            "3_breakdown": f"Roots are {roots_str}.",
        },
        "misconception_tags": ["transposition_sign_error", "attempting_to_solve_without_zero_rhs"],
    }


# =========================================================================== #
# Subskill 41: Solve Cubic with Distributive Expansion First
# =========================================================================== #
def build_41_solve_cubic_factored_lhs_with_distributive_expansion(rng: random.Random) -> Dict[str, Any]:
    # x(x^2 + p*x) = q*x + r -> x^3 + p*x^2 - q*x - r = 0
    r1 = rng.choice([-2, 2])
    r2 = rng.choice([-3, 3])
    r3 = rng.choice([-4, 4])
    r1, r2, r3 = sorted([r1, r2, r3])

    poly = sp.expand((x - r1) * (x - r2) * (x - r3))
    c2 = -(r1 + r2 + r3)
    c1 = (r1*r2 + r1*r3 + r2*r3)
    c0 = -(r1 * r2 * r3)

    lhs = f"x(x^2 {'+ ' + str(c2) if c2 >= 0 else '- ' + str(abs(c2))}x)"
    rhs = f"{-c1}x {'+ ' + str(-c0) if -c0 >= 0 else '- ' + str(abs(c0))}"

    roots_str = f"x = {r1} \\text{{ or }} x = {r2} \\text{{ or }} x = {r3}"

    prompt = (
        f"Solve for $x$ in the equation:\n\n"
        f"$${lhs} = {rhs}$$\n\n"
        f"Expand brackets and express in standard cubic form before solving."
    )

    sample = (
        f"\\text{{Expand LHS: }}\\\\\n"
        f"x^3 {'+ ' + str(c2) if c2 >= 0 else '- ' + str(abs(c2))}x^2 = {rhs}\\\\\n"
        f"\\text{{Move all terms to LHS: }}\\\\\n"
        f"{sp.latex(poly)} = 0\\\\\n"
        f"(x - {r1})(x - {r2})(x - {r3}) = 0\\\\\n"
        f"\\therefore {roots_str}."
    )

    return {
        "id": f"tech_poly_41_{rng.randint(100000, 999999)}",
        "question_id": f"tech_poly_41_{rng.randint(100000, 999999)}",
        "topic": "technical_mathematics_polynomials",
        "subskill": "41_solve_cubic_factored_lhs_with_distributive_expansion",
        "learning_objective_id": "techmath_poly_expand_and_solve",
        "question_text": prompt,
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": roots_str,
        "answer_sympy": f"[{r1}, {r2}, {r3}]",
        "expected_answer": f"x = {r1} or x = {r2} or x = {r3}",
        "sample_answer": sample,
        "worked_solution": sample,
        "marks": 5,
        "term": 1,
        "caps_weight_percent": 25,
        "suggested_duration_mins": 6,
        "mode": "compound",
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp1", "desc": "Expand LHS to cubic polynomial", "marks": 1},
                {"id": "mp2", "desc": "Transpose to standard form = 0", "marks": 1},
                {"id": "mp3", "desc": f"Find root x = {r1}", "marks": 1},
                {"id": "mp4", "desc": "Factorise quotient quadratic", "marks": 1},
                {"id": "mp5", "desc": f"State solutions {roots_str}", "marks": 1},
            ],
        },
        "hints": {
            "1_nudge": "Do not attempt to divide across the equal sign. Expand x(x^2 + px) first.",
            "2_concept": f"Transpose all terms to form {sp.latex(poly)} = 0.",
            "3_breakdown": f"Roots are {roots_str}.",
        },
        "misconception_tags": ["dividing_by_variable", "bracket_expansion_error"],
    }


# =========================================================================== #
# Subskill 42: Solve Cubic with Common Binomial Factor on Both Sides
# =========================================================================== #
def build_42_solve_cubic_common_binomial_factor(rng: random.Random) -> Dict[str, Any]:
    # k^2(x - a) = x^2(x - a) -> (x^2 - k^2)(x - a) = 0
    a = rng.choice([-3, -2, -1, 1, 2, 3])
    k = rng.choice([2, 3, 4, 5])
    k2 = k * k

    bin_str = f"(x - {a})" if a > 0 else f"(x + {-a})"
    roots_str = f"x = {a} \\text{{ or }} x = {k} \\text{{ or }} x = -{k}"

    prompt = (
        f"Solve for $x$ algebraically without dividing both sides by the variable expression ${bin_str}$:\n\n"
        f"$${k2}{bin_str} = x^2{bin_str}$$"
    )

    sample = (
        f"\\text{{Do NOT divide by }} {bin_str} \\text{{ as this eliminates a valid solution.}}\\\\\n"
        f"\\text{{Subtract }} {k2}{bin_str} \\text{{ from both sides: }}\\\\\n"
        f"x^2{bin_str} - {k2}{bin_str} = 0\\\\\n"
        f"{bin_str}(x^2 - {k2}) = 0\\\\\n"
        f"{bin_str}(x - {k})(x + {k}) = 0\\\\\n"
        f"\\therefore {roots_str}."
    )

    return {
        "id": f"tech_poly_42_{rng.randint(100000, 999999)}",
        "question_id": f"tech_poly_42_{rng.randint(100000, 999999)}",
        "topic": "technical_mathematics_polynomials",
        "subskill": "42_solve_cubic_common_binomial_factor",
        "learning_objective_id": "techmath_poly_common_binomial_solve",
        "question_text": prompt,
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": roots_str,
        "answer_sympy": f"[{a}, {k}, -{k}]",
        "expected_answer": f"x = {a} or x = {k} or x = -{k}",
        "sample_answer": sample,
        "worked_solution": sample,
        "marks": 4,
        "term": 1,
        "caps_weight_percent": 25,
        "suggested_duration_mins": 4,
        "mode": "compound",
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp1", "desc": f"Transpose and factor out common binomial {bin_str}", "marks": 2},
                {"id": "mp2", "desc": f"Factorise difference of squares (x^2 - {k2})", "marks": 1},
                {"id": "mp3", "desc": f"State all three solutions {roots_str}", "marks": 1},
            ],
        },
        "hints": {
            "1_nudge": f"Subtract to get x^2{bin_str} - {k2}{bin_str} = 0.",
            "2_concept": f"Take out the common binomial {bin_str} as a factor.",
            "3_breakdown": f"x = {a} or x = {k} or x = -{k}.",
        },
        "misconception_tags": ["dividing_by_variable_expression", "losing_root_by_cancelling"],
    }


# =========================================================================== #
# Subskill 43: Solve Cubic with Quadratic Factor having Non-Real Roots
# =========================================================================== #
def build_43_solve_cubic_quadratic_factor_non_real_roots(rng: random.Random) -> Dict[str, Any]:
    # (x - r1)(x^2 + c) = 0 where c > 0 -> only one real solution x = r1
    r1 = rng.choice([-4, -3, -2, -1, 1, 2, 3, 4])
    c_val = rng.choice([4, 9, 16, 25])

    poly = sp.expand((x - r1) * (x**2 + c_val))
    poly_latex = sp.latex(poly)

    f1 = f"(x - {r1})" if r1 > 0 else f"(x + {-r1})"
    ans_latex = f"x = {r1} \\quad (x^2 + {c_val} = 0 \\text{{ has no real solutions}})"

    prompt = (
        f"Solve for $x \\in \\mathbb{{R}}$ in the cubic equation:\n\n"
        f"$${poly_latex} = 0$$\n\n"
        f"State any real solutions and explain why no other real roots exist."
    )

    sample = (
        f"\\text{{Test }} x = {r1}: f({r1}) = 0 \\implies {f1} \\text{{ is a factor.}}\\\\\n"
        f"{poly_latex} = {f1}(x^2 + {c_val}) = 0\\\\\n"
        f"\\text{{For }} {f1} = 0 \\implies x = {r1}.\\\\\n"
        f"\\text{{For }} x^2 + {c_val} = 0 \\implies x^2 = -{c_val} \\implies x = \\pm \\sqrt{{-{c_val}}} \\notin \\mathbb{{R}}.\\\\\n"
        f"\\therefore \\text{{The only real solution is }} x = {r1}."
    )

    return {
        "id": f"tech_poly_43_{rng.randint(100000, 999999)}",
        "question_id": f"tech_poly_43_{rng.randint(100000, 999999)}",
        "topic": "technical_mathematics_polynomials",
        "subskill": "43_solve_cubic_quadratic_factor_non_real_roots",
        "learning_objective_id": "techmath_poly_non_real_roots",
        "question_text": prompt,
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "answer_sympy": str(r1),
        "expected_answer": f"x = {r1}",
        "sample_answer": sample,
        "worked_solution": sample,
        "marks": 4,
        "term": 1,
        "caps_weight_percent": 25,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp1", "desc": f"Find real root x = {r1}", "marks": 1},
                {"id": "mp2", "desc": f"Obtain quadratic factor (x^2 + {c_val})", "marks": 1},
                {"id": "mp3", "desc": f"Demonstrate that x^2 = -{c_val} has no real solutions", "marks": 1},
                {"id": "mp4", "desc": f"Conclude single real solution x = {r1}", "marks": 1},
            ],
        },
        "hints": {
            "1_nudge": f"Substitute x = {r1} to verify the real root.",
            "2_concept": f"The remaining equation is x^2 + {c_val} = 0.",
            "3_breakdown": f"x^2 = -{c_val} has no real solutions. Only real root is x = {r1}.",
        },
        "misconception_tags": ["inventing_real_roots_for_negative_square", "ignoring_domain_reals"],
    }


# =========================================================================== #
# Subskill 44: Exponential Equation Reducible to Cubic Form
# =========================================================================== #
def build_44_cubic_exponential_substitution_equation(rng: random.Random) -> Dict[str, Any]:
    base = rng.choice([2, 3])
    if base == 2:
        k_choices = rng.choice([(1, 2, 4, 0, 1, 2), (1, 2, 8, 0, 1, 3), (1, 4, 8, 0, 2, 3)])
    else:
        k_choices = rng.choice([(1, 3, 9, 0, 1, 2), (1, 3, 27, 0, 1, 3)])
    k1, k2, k3, x1, x2, x3 = k_choices

    poly_k = sp.expand((x - k1) * (x - k2) * (x - k3))
    c2 = int(poly_k.coeff(x, 2))
    c1 = int(poly_k.coeff(x, 1))
    c0 = int(poly_k.coeff(x, 0))

    eq_str = f"{base}^{{3x}} {'+ ' + str(c2) if c2 >= 0 else '- ' + str(abs(c2))} \\cdot {base}^{{2x}} + {c1} \\cdot {base}^x {'+ ' + str(c0) if c0 >= 0 else '- ' + str(abs(c0))} = 0"

    prompt = (
        f"Solve for $x$ by letting $k = {base}^x$ to transform the equation into a cubic polynomial:\n\n"
        f"$${eq_str}$$\n\n"
        f"Show all steps of substitution, factorisation, and back-substitution."
    )

    sample = (
        f"\\text{{Let }} k = {base}^x. \\text{{ Since }} {base}^{{3x}} = ({base}^x)^3 = k^3 \\text{{ and }} {base}^{{2x}} = k^2:\\\\\n"
        f"k^3 {'+ ' + str(c2) if c2 >= 0 else '- ' + str(abs(c2))}k^2 + {c1}k {'+ ' + str(c0) if c0 >= 0 else '- ' + str(abs(c0))} = 0\\\\\n"
        f"\\text{{Factorising the cubic in }} k:\\\\\n"
        f"(k - {k1})(k - {k2})(k - {k3}) = 0\\\\\n"
        f"k = {k1} \\quad \\text{{or}} \\quad k = {k2} \\quad \\text{{or}} \\quad k = {k3}\\\\\n"
        f"\\text{{Back-substitute }} k = {base}^x:\\\\\n"
        f"{base}^x = {k1} = {base}^{x1} \\implies x = {x1}\\\\\n"
        f"{base}^x = {k2} = {base}^{x2} \\implies x = {x2}\\\\\n"
        f"{base}^x = {k3} = {base}^{x3} \\implies x = {x3}\\\\\n"
        f"\\therefore x = {x1} \\quad \\text{{or}} \\quad x = {x2} \\quad \\text{{or}} \\quad x = {x3}."
    )

    ans_str = f"x = {x1} or x = {x2} or x = {x3}"
    ans_latex = f"x = {x1} \\text{{ or }} x = {x2} \\text{{ or }} x = {x3}"

    return {
        "id": f"tech_poly_44_{rng.randint(100000, 999999)}",
        "question_id": f"tech_poly_44_{rng.randint(100000, 999999)}",
        "topic": "technical_mathematics_polynomials",
        "subskill": "44_cubic_exponential_substitution_equation",
        "learning_objective_id": "techmath_poly_exponential_substitution",
        "question_text": prompt,
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "answer_sympy": f"[{x1}, {x2}, {x3}]",
        "expected_answer": ans_str,
        "sample_answer": sample,
        "worked_solution": sample,
        "marks": 6,
        "term": 1,
        "caps_weight_percent": 25,
        "suggested_duration_mins": 7,
        "mode": "compound",
        "marking_schema": {
            "total_marks": 6,
            "marking_points": [
                {"id": "mp1", "desc": f"Substitute k = {base}^x and form cubic equation in k", "marks": 1},
                {"id": "mp2", "desc": f"Factorise cubic in k: (k - {k1})(k - {k2})(k - {k3}) = 0", "marks": 2},
                {"id": "mp3", "desc": f"Solve for k: k = {k1}, {k2}, {k3}", "marks": 1},
                {"id": "mp4", "desc": f"Back-substitute {base}^x = k and equate exponents", "marks": 1},
                {"id": "mp5", "desc": f"Final answers x = {x1}, {x2}, {x3}", "marks": 1},
            ],
        },
        "hints": {
            "1_nudge": f"Replace {base}^x with k, so {base}^(2x) = k^2 and {base}^(3x) = k^3.",
            "2_concept": f"Solve the cubic polynomial in k: (k - {k1})(k - {k2})(k - {k3}) = 0.",
            "3_breakdown": f"Solve {base}^x = {k1}, {base}^x = {k2}, {base}^x = {k3} to find x = {x1}, {x2}, {x3}.",
        },
        "misconception_tags": ["forgetting_back_substitution", "exponential_power_law_error"],
    }


# =========================================================================== #
# Subskill 45: Determine Cubic Coefficients from Given Roots
# =========================================================================== #
def build_45_cubic_coefficients_from_given_roots(rng: random.Random) -> Dict[str, Any]:
    # Given roots r1, r2, r3, expand f(x) = x^3 + bx^2 + cx + d
    roots = rng.sample([-3, -2, -1, 1, 2, 3], 3)
    roots.sort()
    r1, r2, r3 = roots

    poly = sp.expand((x - r1) * (x - r2) * (x - r3))
    b_coeff = int(poly.coeff(x, 2))
    c_coeff = int(poly.coeff(x, 1))
    d_coeff = int(poly.coeff(x, 0))

    prompt = (
        f"A monic cubic polynomial $f(x) = x^3 + bx^2 + cx + d$ has roots "
        f"$x_1 = {r1}$, $x_2 = {r2}$, and $x_3 = {r3}$.\n\n"
        f"Determine the numerical values of the coefficients $b$, $c$, and $d$."
    )

    sample = (
        f"\\text{{Since the polynomial is monic and has roots }} {r1}, {r2}, {r3}:\\\\\n"
        f"f(x) = (x - ({r1}))(x - ({r2}))(x - ({r3}))\\\\\n"
        f"= (x {'- ' + str(r1) if r1 >= 0 else '+ ' + str(abs(r1))})"
        f"(x {'- ' + str(r2) if r2 >= 0 else '+ ' + str(abs(r2))})"
        f"(x {'- ' + str(r3) if r3 >= 0 else '+ ' + str(abs(r3))})\\\\\n"
        f"\\text{{Expanding the product: }}\\\\\n"
        f"= {sp.latex(poly)}\\\\\n"
        f"\\therefore b = {b_coeff}, \\quad c = {c_coeff}, \\quad d = {d_coeff}."
    )

    ans_latex = f"b = {b_coeff}, c = {c_coeff}, d = {d_coeff}"

    return {
        "id": f"tech_poly_45_{rng.randint(100000, 999999)}",
        "question_id": f"tech_poly_45_{rng.randint(100000, 999999)}",
        "topic": "technical_mathematics_polynomials",
        "subskill": "45_cubic_coefficients_from_given_roots",
        "learning_objective_id": "techmath_poly_reconstruct_coefficients",
        "question_text": prompt,
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "answer_sympy": f"[{b_coeff}, {c_coeff}, {d_coeff}]",
        "expected_answer": ans_latex,
        "sample_answer": sample,
        "worked_solution": sample,
        "marks": 3,
        "term": 1,
        "caps_weight_percent": 25,
        "suggested_duration_mins": 4,
        "mode": "elementary_factorisation",
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": f"Set up product (x - {r1})(x - {r2})(x - {r3})", "marks": 1},
                {"id": "mp2", "desc": f"Expand polynomial to {sp.latex(poly)}", "marks": 1},
                {"id": "mp3", "desc": f"Identify b = {b_coeff}, c = {c_coeff}, d = {d_coeff}", "marks": 1},
            ],
        },
        "hints": {
            "1_nudge": "If r is a root, then (x - r) is a factor.",
            "2_concept": f"Expand (x - ({r1}))(x - ({r2}))(x - ({r3})).",
            "3_breakdown": f"b = {b_coeff}, c = {c_coeff}, d = {d_coeff}.",
        },
        "misconception_tags": ["sign_inversion_in_factors", "polynomial_expansion_arithmetic_error"],
    }


# =========================================================================== #
# Subskill 46: Cubic Graph x-Intercepts Relation (with Vector Diagram Spec)
# =========================================================================== #
def build_46_cubic_graph_x_intercepts_relation(rng: random.Random) -> Dict[str, Any]:
    # Three roots r1 < r2 < r3 on Cartesian axes
    r1, r2, r3 = rng.sample([-3, -2, -1, 1, 2, 3], 3)
    r1, r2, r3 = sorted([r1, r2, r3])

    poly = sp.expand((x - r1) * (x - r2) * (x - r3))
    poly_latex = sp.latex(poly)
    y_int = int(poly.subs(x, 0))

    prompt = (
        f"In the accompanying figure, the cubic function $y = f(x) = {poly_latex}$ is graphed.\n\n"
        f"Determine the coordinates of the three $x$-intercepts by setting $f(x) = 0$."
    )

    ans_latex = f"({r1}; 0), ({r2}; 0), ({r3}; 0)"
    sample = (
        f"\\text{{To find the }} x\\text{{-intercepts, set }} y = 0:\\\\\n"
        f"{poly_latex} = 0\\\\\n"
        f"(x - ({r1}))(x - ({r2}))(x - ({r3})) = 0\\\\\n"
        f"x = {r1} \\quad \\text{{or}} \\quad x = {r2} \\quad \\text{{or}} \\quad x = {r3}\\\\\n"
        f"\\therefore \\text{{Coordinates: }} ({r1}{{,}} 0), ({r2}{{,}} 0), ({r3}{{,}} 0)."
    )

    # Inline SVG sketch of cubic function
    # Map x in [-4, 4] to SVG x [40, 320]
    def to_svg_x(val: float) -> int:
        return int(180 + val * 35)

    x1_svg = to_svg_x(r1)
    x2_svg = to_svg_x(r2)
    x3_svg = to_svg_x(r3)

    svg = _svg_wrap(
        f'<line x1="20" y1="110" x2="340" y2="110" stroke="#64748b" stroke-width="1.5"/>'
        f'<line x1="180" y1="20" x2="180" y2="200" stroke="#64748b" stroke-width="1.5"/>'
        f'<text x="330" y="105" font-family="sans-serif" font-size="12" fill="#64748b">x</text>'
        f'<text x="185" y="30" font-family="sans-serif" font-size="12" fill="#64748b">y</text>'
        # S-curve path passing through the three roots
        f'<path d="M 40 200 C {x1_svg - 20} 30, {x2_svg - 10} 40, {x2_svg} 110 C {x2_svg + 10} 180, {x3_svg + 20} 190, 320 20" fill="none" stroke="#2563eb" stroke-width="2.5"/>'
        f'<circle cx="{x1_svg}" cy="110" r="4" fill="#dc2626"/>'
        f'<circle cx="{x2_svg}" cy="110" r="4" fill="#dc2626"/>'
        f'<circle cx="{x3_svg}" cy="110" r="4" fill="#dc2626"/>'
        f'<text x="{x1_svg}" y="130" text-anchor="middle" font-family="sans-serif" font-size="11" font-weight="bold" fill="#dc2626">({r1}; 0)</text>'
        f'<text x="{x2_svg}" y="100" text-anchor="middle" font-family="sans-serif" font-size="11" font-weight="bold" fill="#dc2626">({r2}; 0)</text>'
        f'<text x="{x3_svg}" y="130" text-anchor="middle" font-family="sans-serif" font-size="11" font-weight="bold" fill="#dc2626">({r3}; 0)</text>'
        f'<text x="185" y="195" font-family="sans-serif" font-size="10" fill="#64748b">y-int: {y_int}</text>',
        width=360,
        height=220,
    )

    return {
        "id": f"tech_poly_46_{rng.randint(100000, 999999)}",
        "question_id": f"tech_poly_46_{rng.randint(100000, 999999)}",
        "topic": "technical_mathematics_polynomials",
        "subskill": "46_cubic_graph_x_intercepts_relation",
        "learning_objective_id": "techmath_poly_graph_intercepts",
        "question_text": prompt,
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "answer_sympy": f"[({r1}, 0), ({r2}, 0), ({r3}, 0)]",
        "expected_answer": ans_latex,
        "sample_answer": sample,
        "worked_solution": sample,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "title": f"Cubic graph intercepts (roots {r1}, {r2}, {r3})"},
        "marks": 4,
        "term": 1,
        "caps_weight_percent": 25,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp1", "desc": "Set y = 0 to establish cubic equation", "marks": 1},
                {"id": "mp2", "desc": "Solve for three x-intercepts", "marks": 2},
                {"id": "mp3", "desc": f"State coordinate pairs {ans_latex}", "marks": 1},
            ],
        },
        "hints": {
            "1_nudge": "The x-intercepts occur where y = 0.",
            "2_concept": f"Solve {poly_latex} = 0 by factorisation.",
            "3_breakdown": f"The coordinates are ({r1}; 0), ({r2}; 0), and ({r3}; 0).",
        },
        "misconception_tags": ["omitting_y_coordinate_in_intercept", "x_y_coordinate_inversion"],
    }


# =========================================================================== #
# Subskill 47: Engineering Sheet Metal Open-Top Tray Volume Optimization
# =========================================================================== #
def build_47_technical_cubic_open_top_sheet_metal_tray_volume(rng: random.Random) -> Dict[str, Any]:
    # Sheet L x W with square corners x cut out: V(x) = x(L - 2x)(W - 2x)
    # Choose clean integer solution x_target
    x_val = rng.choice([2, 3])
    length = 2 * x_val + rng.choice([6, 8, 10])
    width = 2 * x_val + rng.choice([4, 6])
    vol = x_val * (length - 2 * x_val) * (width - 2 * x_val)

    poly = x * (length - 2*x) * (width - 2*x) - vol
    poly_exp = sp.expand(poly)
    poly_latex = sp.latex(poly_exp)

    prompt = (
        f"A sheet metal technician constructs an open-top rectangular tray from a flat metal sheet of "
        f"length ${length}\\text{{ cm}}$ and width ${width}\\text{{ cm}}$ by cutting square corners of side length $x\\text{{ cm}}$ "
        f"and folding up the edges.\n\n"
        f"The volume of the resulting tray is given by $V(x) = x({length} - 2x)({width} - 2x)$.\n\n"
        f"If the required capacity is ${vol}\\text{{ cm}}^3$, form and solve the cubic equation to find the feasible "
        f"corner cutout dimension $x$ (where $0 < x < {width // 2}$)."
    )

    ans_latex = f"{x_val}\\text{{ cm}}"
    sample = (
        f"V(x) = x({length} - 2x)({width} - 2x) = {vol}\\\\\n"
        f"x({length * width} - {2 * length + 2 * width}x + 4x^2) = {vol}\\\\\n"
        f"4x^3 - {2 * (length + width)}x^2 + {length * width}x - {vol} = 0\\\\\n"
        f"\\text{{Test }} x = {x_val}: V({x_val}) = ({x_val})({length - 2*x_val})({width - 2*x_val}) = {vol}.\\\\\n"
        f"\\text{{Dividing gives }} (x - {x_val})({sp.latex(sp.expand(poly_exp / (x - x_val)))}) = 0.\\\\\n"
        f"\\text{{Since the physical cutout must satisfy }} 0 < x < {width / 2}, "
        f"\\text{{the only feasible engineering dimension is }} x = {x_val}\\text{{ cm}}."
    )

    # Inline SVG diagram of sheet metal blank with cut corners
    svg = _svg_wrap(
        f'<rect x="50" y="40" width="260" height="140" fill="#e2e8f0" stroke="#334155" stroke-width="2"/>'
        # Dotted cut lines for four corners
        f'<rect x="50" y="40" width="35" height="35" fill="#f8fafc" stroke="#dc2626" stroke-dasharray="3"/>'
        f'<rect x="275" y="40" width="35" height="35" fill="#f8fafc" stroke="#dc2626" stroke-dasharray="3"/>'
        f'<rect x="50" y="145" width="35" height="35" fill="#f8fafc" stroke="#dc2626" stroke-dasharray="3"/>'
        f'<rect x="275" y="145" width="35" height="35" fill="#f8fafc" stroke="#dc2626" stroke-dasharray="3"/>'
        f'<text x="67" y="62" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#dc2626">x</text>'
        f'<text x="180" y="30" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="bold" fill="#0f172a">Length = {length} cm</text>'
        f'<text x="25" y="115" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="bold" fill="#0f172a" transform="rotate(-90 25 115)">Width = {width} cm</text>'
        f'<text x="180" y="115" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#2563eb">Volume = {vol} cm³</text>',
        width=360,
        height=220,
    )

    return {
        "id": f"tech_poly_47_{rng.randint(100000, 999999)}",
        "question_id": f"tech_poly_47_{rng.randint(100000, 999999)}",
        "topic": "technical_mathematics_polynomials",
        "subskill": "47_technical_cubic_open_top_sheet_metal_tray_volume",
        "learning_objective_id": "techmath_poly_sheet_metal_volume",
        "question_text": prompt,
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "answer_sympy": str(x_val),
        "expected_answer": f"x = {x_val} cm",
        "sample_answer": sample,
        "worked_solution": sample,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "title": f"Sheet metal tray layout ({length}x{width} cm, Vol={vol})"},
        "marks": 5,
        "term": 1,
        "caps_weight_percent": 25,
        "suggested_duration_mins": 7,
        "mode": "compound",
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp1", "desc": f"Form cubic equation: {poly_latex} = 0", "marks": 2},
                {"id": "mp2", "desc": f"Apply factor theorem to find root x = {x_val}", "marks": 1},
                {"id": "mp3", "desc": f"Check feasibility condition 0 < x < {width // 2}", "marks": 1},
                {"id": "mp4", "desc": f"Final conclusion x = {x_val} cm", "marks": 1},
            ],
        },
        "hints": {
            "1_nudge": f"Expand x({length} - 2x)({width} - 2x) = {vol} and set to zero.",
            "2_concept": f"Test integer factor x = {x_val}.",
            "3_breakdown": f"x = {x_val} cm is the only valid physical solution.",
        },
        "misconception_tags": ["unphysical_root_selection", "tray_dimension_expansion_error"],
    }


# =========================================================================== #
# Subskill 48: Technical Machining Hollow Bushing Volume
# =========================================================================== #
def build_48_technical_cubic_machined_hollow_cylindrical_pipe(rng: random.Random) -> Dict[str, Any]:
    # Solid block x by x by (x + k) with drilled cylindrical hole
    # Or stepped shaft volume: V(x) = x^3 + a*x^2 - b*x = target
    x_val = rng.choice([3, 4, 5])
    k_val = rng.choice([2, 4])
    base_dim = x_val + k_val
    vol = x_val**3 + k_val * x_val**2

    prompt = (
        f"A mechanical component consists of an aluminium casting whose volume is described by "
        f"$V(x) = x^2(x + {k_val})\\text{{ cm}}^3$, where $x$ represents the base wall thickness in centimetres.\n\n"
        f"If the measured volume of the casting is ${vol}\\text{{ cm}}^3$, set up the cubic equation and "
        f"solve for the required wall thickness $x > 0$."
    )

    poly = x**3 + k_val*x**2 - vol
    poly_latex = sp.latex(poly)
    ans_latex = f"{x_val}\\text{{ cm}}"

    sample = (
        f"V(x) = x^2(x + {k_val}) = {vol}\\\\\n"
        f"{poly_latex} = 0\\\\\n"
        f"\\text{{Test positive factors of }} {vol}:\\\\\n"
        f"({x_val})^3 + {k_val}({x_val})^2 - {vol} = {x_val**3} + {k_val * x_val**2} - {vol} = 0\\\\\n"
        f"\\implies (x - {x_val}) \\text{{ is a factor.}}\\\\\n"
        f"\\text{{Dividing yields }} (x - {x_val})(x^2 + {x_val + k_val}x + {vol // x_val}) = 0.\\\\\n"
        f"\\text{{The quadratic factor has negative discriminant and no real roots.}}\\\\\n"
        f"\\therefore \\text{{The wall thickness is }} x = {x_val}\\text{{ cm}}."
    )

    # Inline SVG diagram of component cross-section
    svg = _svg_wrap(
        f'<rect x="70" y="50" width="220" height="120" fill="#f1f5f9" stroke="#0f172a" stroke-width="2"/>'
        f'<rect x="110" y="75" width="140" height="70" fill="#cbd5e1" stroke="#475569" stroke-width="1.5" stroke-dasharray="4"/>'
        f'<text x="180" y="115" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#0f172a">Hollow Cavity</text>'
        f'<text x="90" y="115" text-anchor="middle" font-family="sans-serif" font-size="11" font-weight="bold" fill="#2563eb">x = ?</text>'
        f'<text x="180" y="40" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#0f172a">Length = x + {k_val}</text>'
        f'<text x="180" y="195" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="bold" fill="#2563eb">Volume = {vol} cm³</text>',
        width=360,
        height=220,
    )

    return {
        "id": f"tech_poly_48_{rng.randint(100000, 999999)}",
        "question_id": f"tech_poly_48_{rng.randint(100000, 999999)}",
        "topic": "technical_mathematics_polynomials",
        "subskill": "48_technical_cubic_machined_hollow_cylindrical_pipe",
        "learning_objective_id": "techmath_poly_machined_component_volume",
        "question_text": prompt,
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "answer_sympy": str(x_val),
        "expected_answer": f"x = {x_val} cm",
        "sample_answer": sample,
        "worked_solution": sample,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "title": f"Machined aluminium component (Vol={vol} cm³, k={k_val})"},
        "marks": 4,
        "term": 1,
        "caps_weight_percent": 25,
        "suggested_duration_mins": 6,
        "mode": "compound",
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp1", "desc": f"Set up cubic equation: {poly_latex} = 0", "marks": 1},
                {"id": "mp2", "desc": f"Apply factor theorem to identify root x = {x_val}", "marks": 2},
                {"id": "mp3", "desc": f"Conclude x = {x_val} cm", "marks": 1},
            ],
        },
        "hints": {
            "1_nudge": f"Write the equation as x^3 + {k_val}x^2 - {vol} = 0.",
            "2_concept": f"Test positive divisors of {vol}: try x = {x_val}.",
            "3_breakdown": f"x = {x_val} cm.",
        },
        "misconception_tags": ["cubic_transposition_error", "unverified_root"],
    }


# =========================================================================== #
# Subskill 49: Structural Beam Deflection Zero-Crossing
# =========================================================================== #
def build_49_technical_cubic_beam_deflection_zero_crossing(rng: random.Random) -> Dict[str, Any]:
    # Beam deflection cubic: y(x) = x^3 - 3*L*x^2 + 2*L^2*x = x(x - L)(x - 2L)
    L_val = rng.choice([2, 3, 4, 5])
    poly = x * (x - L_val) * (x - 2*L_val)
    poly_exp = sp.expand(poly)
    poly_latex = sp.latex(poly_exp)

    prompt = (
        f"In civil engineering, the deflection curve $y(x)$ of a continuous beam supported at intervals "
        f"is modeled by the cubic polynomial equation:\n\n"
        f"$$y(x) = {poly_latex}$$\n\n"
        f"where $x$ represents the position along the span in metres.\n\n"
        f"Find all points $x \\ge 0$ along the beam where the deflection is zero (nodes/supports), by setting $y(x) = 0$."
    )

    ans_latex = f"x = 0\\text{{ m}}, x = {L_val}\\text{{ m}}, x = {2*L_val}\\text{{ m}}"
    sample = (
        f"\\text{{Set }} y(x) = 0:\\\\\n"
        f"{poly_latex} = 0\\\\\n"
        f"\\text{{Factor out }} x:\\\\\n"
        f"x(x^2 - {3*L_val}x + {2*L_val**2}) = 0\\\\\n"
        f"x(x - {L_val})(x - {2*L_val}) = 0\\\\\n"
        f"\\therefore x = 0\\text{{ m}}, \\quad x = {L_val}\\text{{ m}}, \\quad x = {2*L_val}\\text{{ m}}."
    )

    # Inline SVG diagram of beam and deflection curve
    svg = _svg_wrap(
        f'<line x1="40" y1="90" x2="320" y2="90" stroke="#0f172a" stroke-width="4"/>'
        f'<polygon points="40,92 30,115 50,115" fill="#64748b"/>'
        f'<polygon points="180,92 170,115 190,115" fill="#64748b"/>'
        f'<polygon points="320,92 310,115 330,115" fill="#64748b"/>'
        f'<text x="40" y="130" text-anchor="middle" font-family="sans-serif" font-size="11" font-weight="bold" fill="#0f172a">x = 0</text>'
        f'<text x="180" y="130" text-anchor="middle" font-family="sans-serif" font-size="11" font-weight="bold" fill="#0f172a">x = {L_val} m</text>'
        f'<text x="320" y="130" text-anchor="middle" font-family="sans-serif" font-size="11" font-weight="bold" fill="#0f172a">x = {2*L_val} m</text>'
        f'<path d="M 40 90 Q 110 50, 180 90 Q 250 130, 320 90" fill="none" stroke="#2563eb" stroke-width="2.5" stroke-dasharray="4"/>'
        f'<text x="180" y="35" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#2563eb">Deflection curve y(x)</text>',
        width=360,
        height=220,
    )

    return {
        "id": f"tech_poly_49_{rng.randint(100000, 999999)}",
        "question_id": f"tech_poly_49_{rng.randint(100000, 999999)}",
        "topic": "technical_mathematics_polynomials",
        "subskill": "49_technical_cubic_beam_deflection_zero_crossing",
        "learning_objective_id": "techmath_poly_beam_deflection",
        "question_text": prompt,
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "answer_sympy": f"[0, {L_val}, {2*L_val}]",
        "expected_answer": f"x = 0 m, x = {L_val} m, x = {2*L_val} m",
        "sample_answer": sample,
        "worked_solution": sample,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "title": f"Continuous beam deflection supports (L={L_val} m)"},
        "marks": 4,
        "term": 1,
        "caps_weight_percent": 25,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp1", "desc": "Factor out common factor x", "marks": 1},
                {"id": "mp2", "desc": f"Factorise quadratic (x - {L_val})(x - {2*L_val})", "marks": 2},
                {"id": "mp3", "desc": f"State all three positions {ans_latex}", "marks": 1},
            ],
        },
        "hints": {
            "1_nudge": "Factor out x first, since every term contains x.",
            "2_concept": f"The quadratic factor is x^2 - {3*L_val}x + {2*L_val**2}.",
            "3_breakdown": f"Zero points are x = 0 m, x = {L_val} m, x = {2*L_val} m.",
        },
        "misconception_tags": ["omitting_origin_zero_support", "quadratic_factorisation_error"],
    }


# =========================================================================== #
# Subskill 50: Comprehensive Engineering Storage Hopper Synthesis
# =========================================================================== #
def build_50_technical_cubic_comprehensive_engineering_synthesis(rng: random.Random) -> Dict[str, Any]:
    # Rectangular storage hopper with dimensions (x + a), (x - b), and x
    a_val = rng.choice([2, 3])
    b_val = rng.choice([1, 2])
    x_val = rng.choice([4, 5, 6])

    vol_target = x_val * (x_val + a_val) * (x_val - b_val)
    poly = x * (x + a_val) * (x - b_val) - vol_target
    poly_exp = sp.expand(poly)
    poly_latex = sp.latex(poly_exp)

    prompt = (
        f"An industrial storage hopper is designed in the shape of a rectangular container.\n"
        f"Its dimensions are: height $= x\\text{{ m}}$, length $= (x + {a_val})\\text{{ m}}$, and width $= (x - {b_val})\\text{{ m}}$.\n\n"
        f"The required storage capacity of the hopper is ${vol_target}\\text{{ m}}^3$.\n\n"
        f"a) Show that the volume equation reduces to the standard cubic equation $${poly_latex} = 0$$\n"
        f"b) Use the Factor Theorem to determine an initial root of this cubic equation.\n"
        f"c) Hence, factorise the equation completely and state the unique physical height $x$ of the hopper."
    )

    quad = sp.expand(poly_exp / (x - x_val))
    ans_latex = f"x = {x_val}\\text{{ m}}"

    sample = (
        f"\\text{{a) }} V = x(x + {a_val})(x - {b_val}) = x(x^2 + {a_val - b_val}x - {a_val * b_val}) "
        f"= x^3 + {a_val - b_val}x^2 - {a_val * b_val}x.\\\\\n"
        f"x^3 + {a_val - b_val}x^2 - {a_val * b_val}x = {vol_target} \\implies {poly_latex} = 0.\\\\\n\n"
        f"\\text{{b) Testing integer factors: }}\\\\\n"
        f"f({x_val}) = ({x_val})^3 + {a_val - b_val}({x_val})^2 - {a_val * b_val}({x_val}) - {vol_target} = 0\\\\\n"
        f"\\implies (x - {x_val}) \\text{{ is a factor.}}\\\\\n\n"
        f"\\text{{c) Dividing by }} (x - {x_val}):\\\\\n"
        f"{poly_latex} = (x - {x_val})({sp.latex(quad)}) = 0.\\\\\n"
        f"\\text{{The quadratic factor has negative discriminant and no real roots.}}\\\\\n"
        f"\\text{{Furthermore, since width }} = x - {b_val} > 0, \\text{{ we require }} x > {b_val}.\\\\\n"
        f"\\therefore \\text{{The unique physical height is }} x = {x_val}\\text{{ m}}."
    )

    # Inline SVG diagram of the 3D storage hopper
    svg = _svg_wrap(
        f'<polygon points="80,140 220,140 220,60 80,60" fill="#f8fafc" stroke="#0f172a" stroke-width="2"/>'
        f'<polygon points="220,140 280,100 280,30 220,60" fill="#e2e8f0" stroke="#0f172a" stroke-width="2"/>'
        f'<polygon points="80,60 140,20 280,30 220,60" fill="#cbd5e1" stroke="#0f172a" stroke-width="2"/>'
        f'<text x="150" y="160" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="bold" fill="#0f172a">Length: x + {a_val}</text>'
        f'<text x="265" y="125" font-family="sans-serif" font-size="11" font-weight="bold" fill="#0f172a">Width: x - {b_val}</text>'
        f'<text x="65" y="105" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="bold" fill="#2563eb">Height: x</text>'
        f'<text x="150" y="100" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="bold" fill="#2563eb">Capacity = {vol_target} m³</text>',
        width=360,
        height=220,
    )

    return {
        "id": f"tech_poly_50_{rng.randint(100000, 999999)}",
        "question_id": f"tech_poly_50_{rng.randint(100000, 999999)}",
        "topic": "technical_mathematics_polynomials",
        "subskill": "50_technical_cubic_comprehensive_engineering_synthesis",
        "learning_objective_id": "techmath_poly_engineering_synthesis",
        "question_text": prompt,
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "answer_sympy": str(x_val),
        "expected_answer": f"x = {x_val} m",
        "sample_answer": sample,
        "worked_solution": sample,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "title": f"Industrial hopper design (Vol={vol_target} m³, a={a_val}, b={b_val})"},
        "marks": 6,
        "term": 1,
        "caps_weight_percent": 25,
        "suggested_duration_mins": 8,
        "mode": "compound",
        "marking_schema": {
            "total_marks": 6,
            "marking_points": [
                {"id": "mp1", "desc": f"Derive standard cubic {poly_latex} = 0", "marks": 2},
                {"id": "mp2", "desc": f"Factor theorem proof for x = {x_val}", "marks": 1},
                {"id": "mp3", "desc": f"Quadratic factor ({sp.latex(quad)})", "marks": 1},
                {"id": "mp4", "desc": f"Physical feasibility condition x > {b_val}", "marks": 1},
                {"id": "mp5", "desc": f"Final answer x = {x_val} m", "marks": 1},
            ],
        },
        "hints": {
            "1_nudge": f"Multiply the three dimensions x(x + {a_val})(x - {b_val}) and equate to {vol_target}.",
            "2_concept": f"Test integer factor x = {x_val} using the Factor Theorem.",
            "3_breakdown": f"Height is x = {x_val} m.",
        },
        "misconception_tags": ["cubic_volume_formulation_error", "unphysical_negative_dimensions"],
    }


# =========================================================================== #
# Export Dictionary: ARCHETYPES_26_50
# =========================================================================== #
ARCHETYPES_26_50: Dict[str, Any] = {
    "26_factorise_cubic_grouping_four_terms": build_26_factorise_cubic_grouping_four_terms,
    "27_factorise_cubic_common_monomial_factor": build_27_factorise_cubic_common_monomial_factor,
    "28_factorise_cubic_monic_trial_factor_inspection": build_28_factorise_cubic_monic_trial_factor_inspection,
    "29_factorise_cubic_monic_difference_of_squares_quotient": build_29_factorise_cubic_monic_difference_of_squares_quotient,
    "30_factorise_cubic_monic_perfect_square_quotient": build_30_factorise_cubic_monic_perfect_square_quotient,
    "31_factorise_cubic_non_monic_leading_coeff_two": build_31_factorise_cubic_non_monic_leading_coeff_two,
    "32_factorise_cubic_non_monic_fractional_root": build_32_factorise_cubic_non_monic_fractional_root,
    "33_factorise_cubic_irreducible_quadratic_factor": build_33_factorise_cubic_irreducible_quadratic_factor,
    "34_solve_cubic_three_distinct_integer_roots_monic": build_34_solve_cubic_three_distinct_integer_roots_monic,
    "35_solve_cubic_monic_with_negative_constant_term": build_35_solve_cubic_monic_with_negative_constant_term,
    "36_solve_cubic_one_integer_two_surd_roots": build_36_solve_cubic_one_integer_two_surd_roots,
    "37_solve_cubic_repeated_double_root": build_37_solve_cubic_repeated_double_root,
    "38_solve_cubic_repeated_triple_root": build_38_solve_cubic_repeated_triple_root,
    "39_solve_cubic_non_monic_integer_and_fractional_roots": build_39_solve_cubic_non_monic_integer_and_fractional_roots,
    "40_solve_cubic_non_zero_rhs_rearrangement": build_40_solve_cubic_non_zero_rhs_rearrangement,
    "41_solve_cubic_factored_lhs_with_distributive_expansion": build_41_solve_cubic_factored_lhs_with_distributive_expansion,
    "42_solve_cubic_common_binomial_factor": build_42_solve_cubic_common_binomial_factor,
    "43_solve_cubic_quadratic_factor_non_real_roots": build_43_solve_cubic_quadratic_factor_non_real_roots,
    "44_cubic_exponential_substitution_equation": build_44_cubic_exponential_substitution_equation,
    "45_cubic_coefficients_from_given_roots": build_45_cubic_coefficients_from_given_roots,
    "46_cubic_graph_x_intercepts_relation": build_46_cubic_graph_x_intercepts_relation,
    "47_technical_cubic_open_top_sheet_metal_tray_volume": build_47_technical_cubic_open_top_sheet_metal_tray_volume,
    "48_technical_cubic_machined_hollow_cylindrical_pipe": build_48_technical_cubic_machined_hollow_cylindrical_pipe,
    "49_technical_cubic_beam_deflection_zero_crossing": build_49_technical_cubic_beam_deflection_zero_crossing,
    "50_technical_cubic_comprehensive_engineering_synthesis": build_50_technical_cubic_comprehensive_engineering_synthesis,
}

BUILDERS_26_50: Dict[str, Any] = ARCHETYPES_26_50

