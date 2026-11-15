"""Grade 11 Mathematics — Exponents and Surds Archetypes 01–25.
Grounded in South African National Curriculum Standards for Grade 11 Mathematics (Term 1).
Reference: curriculum_docs_auto/Mathematics_Gr11/Term 1/01. Exponents and surds.md

Covers Archetypes 01–25:
- 01–03: Real vs non-real classification, rational vs irrational surds, estimating surd bounds between consecutive integers
- 04–06: Exponent laws: product/quotient with prime base factorization, power-of-power with negative exponents, monomial exponential fractions
- 07–10: Exponential factorisation: common factor binomial numerator, split common factors numerator & denominator, difference of squares, exponential trinomials
- 11–14: Rational exponents: radical to rational exponent form, rational exponent to radical form, numerical evaluations, fractional exponent binomial products
- 15–18: Surd simplification: prime factorization to simplest radical form a√b, adding/subtracting like surds, higher coefficient surds, monomial surd products
- 19–21: Surd expansion: distributive property over binomial, squaring binomial surds, difference of squares conjugate products
- 22–25: Rationalising denominators: monomial denominators, binomial conjugates (sum & difference), two-term surd fraction sums
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
# 01. Real vs Non-Real Number Classification
# ---------------------------------------------------------------------------
def build_01_classify_real_nonreal_numbers(r: random.Random) -> Dict[str, Any]:
    val = r.choice([4, 9, 16, 25, 36, 49, 64, 81, 100])
    is_nonreal = r.choice([True, False])
    
    if is_nonreal:
        expr_latex = f"\\sqrt{{-{val}}}"
        correct = "Non-real"
        reason = f"The square root of a negative number (\\sqrt{{-{val}}}) is undefined in the real number system ($\\mathbb{{R}}'$)."
        distractors = ["Real and rational", "Real and irrational", "Integer"]
    else:
        # e.g. -sqrt(val) or (-val)^(2/3) or sqrt(val)
        sub_type = r.choice(["neg_outside", "positive_root"])
        if sub_type == "neg_outside":
            root_val = int(math.isqrt(val))
            expr_latex = f"-\\sqrt{{{val}}}"
            correct = "Real and rational"
            reason = f"The negative sign is outside the square root, so -\\sqrt{{{val}}} = -{root_val}, which is an integer and therefore real and rational ($\\mathbb{{Q}}$)."
        else:
            root_val = int(math.isqrt(val))
            expr_latex = f"\\sqrt{{{val}}}"
            correct = "Real and rational"
            reason = f"\\sqrt{{{val}}} = {root_val}, which is a whole number and therefore real and rational ($\\mathbb{{Q}}$)."
        distractors = ["Non-real", "Real and irrational", "Undefined"]

    options = [correct] + distractors
    r.shuffle(options)

    prompt = f"Classify the following number in the real number system:\n\n$${expr_latex}$$\n\nChoose the most accurate description."
    
    sol = solution_graph(
        goal="Classify number as real or non-real",
        chain_type="classification",
        steps=[
            step(
                from_latex=expr_latex,
                to_latex_str=correct,
                op="Evaluate radicand sign",
                rule=reason,
            )
        ],
        final_latex=correct,
    )

    q = make_math_question(
        prefix="g11_exp",
        topic=TOPIC,
        subskill="01_classify_real_nonreal_numbers",
        learning_objective_id=f"{LO_PREFIX}_01",
        prompt=prompt,
        prompt_latex=prompt,
        answer_mode="mcq",
        question_type="mcq",
        answer_latex=correct,
        sample_answer=correct,
        canonical_solution=sol,
        marking_schema={
            "total_marks": 2,
            "steps": [
                {"desc": "Identify whether radicand is negative under even root", "marks": 1},
                {"desc": "Correct classification", "marks": 1},
            ],
        },
        hints={
            "nudge": "Check the position of the negative sign relative to the radical symbol.",
            "concept": "The even root of any strictly negative number produces a non-real number in the high school curriculum.",
            "breakdown": reason,
        },
        misconception_tags=["confusing_negative_radicand_with_negative_root"],
        term=1,
        caps_weight_percent=15,
        suggested_duration_mins=3,
        difficulty="easy",
    )
    q["options"] = options
    return q


# ---------------------------------------------------------------------------
# 02. Classify Rational vs Irrational Surds
# ---------------------------------------------------------------------------
def build_02_classify_rational_irrational_surds(r: random.Random) -> Dict[str, Any]:
    case = r.choice(["irrational_surd", "rational_perfect_square", "rational_surd_fraction"])
    if case == "irrational_surd":
        rad = r.choice([2, 3, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15, 17, 18, 20])
        expr_latex = f"\\sqrt{{{rad}}}"
        correct = "Irrational"
        reason = f"{rad} is not a perfect square, so \\sqrt{{{rad}}} cannot be written as a quotient of integers; its decimal expansion is non-terminating and non-recurring."
        distractors = ["Rational", "Non-real", "Integer"]
    elif case == "rational_perfect_square":
        root = r.choice([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
        sq = root * root
        expr_latex = f"\\sqrt{{{sq}}}"
        correct = "Rational"
        reason = f"\\sqrt{{{sq}}} = {root} = \\frac{{{root}}}{{1}}, which is a ratio of two integers."
        distractors = ["Irrational", "Non-real", "Non-terminating"]
    else:
        root_num = r.choice([2, 3, 4])
        sq_num = root_num * root_num
        root_den = r.choice([5, 6, 7])
        sq_den = root_den * root_den
        expr_latex = f"\\sqrt{{\\frac{{{sq_num}}}{{{sq_den}}}}}"
        correct = "Rational"
        reason = f"\\sqrt{{\\frac{{{sq_num}}}{{{sq_den}}}}} = \\frac{{{root_num}}}{{{root_den}}}, which is a ratio of two non-zero integers."
        distractors = ["Irrational", "Non-real", "Imaginary"]

    options = [correct] + distractors
    r.shuffle(options)

    prompt = f"Without using a calculator, classify the number:\n\n$${expr_latex}$$\n\nState whether it is **Rational** or **Irrational**."
    
    sol = solution_graph(
        goal="Classify surd as rational or irrational",
        chain_type="classification",
        steps=[
            step(
                from_latex=expr_latex,
                to_latex_str=correct,
                op="Evaluate whether radicand is a perfect square",
                rule=reason,
            )
        ],
        final_latex=correct,
    )

    q = make_math_question(
        prefix="g11_exp",
        topic=TOPIC,
        subskill="02_classify_rational_irrational_surds",
        learning_objective_id=f"{LO_PREFIX}_02",
        prompt=prompt,
        prompt_latex=prompt,
        answer_mode="mcq",
        question_type="mcq",
        answer_latex=correct,
        sample_answer=correct,
        canonical_solution=sol,
        marking_schema={
            "total_marks": 2,
            "steps": [
                {"desc": "Evaluate perfect square status of radicand", "marks": 1},
                {"desc": "Correct classification as Rational or Irrational", "marks": 1},
            ],
        },
        hints={
            "nudge": "Can the radicand be simplified to an exact integer or fraction?",
            "concept": "A surd is defined as an indicated root of a rational number that cannot be expressed exactly as a rational number.",
            "breakdown": reason,
        },
        misconception_tags=["assuming_all_square_roots_are_irrational"],
        term=1,
        caps_weight_percent=15,
        suggested_duration_mins=3,
        difficulty="easy",
    )
    q["options"] = options
    return q


# ---------------------------------------------------------------------------
# 03. Estimate Surd Between Consecutive Integers
# ---------------------------------------------------------------------------
def build_03_estimate_surd_between_consecutive_integers(r: random.Random) -> Dict[str, Any]:
    n1 = r.choice([2, 3, 4, 5, 6, 7, 8, 9])
    n2 = n1 + 1
    sq1 = n1 * n1
    sq2 = n2 * n2
    # Choose a non-perfect square between sq1 and sq2
    val = r.randint(sq1 + 1, sq2 - 1)
    
    correct = f"{n1} and {n2}"
    distractors = [
        f"{n1 - 1} and {n1}",
        f"{n2} and {n2 + 1}",
        f"{sq1} and {sq2}",
    ]
    options = [correct] + distractors
    r.shuffle(options)

    prompt = f"Between which two consecutive integers does $\\sqrt{{{val}}}$ lie?\n\n(Do not use a calculator.)"
    reason = f"Since ${sq1} < {val} < {sq2}$, taking square roots gives $\\sqrt{{{sq1}}} < \\sqrt{{{val}}} < \\sqrt{{{sq2}}}$, so ${n1} < \\sqrt{{{val}}} < {n2}$."

    sol = solution_graph(
        goal="Estimate surd between consecutive integers",
        chain_type="inequality",
        steps=[
            step(
                from_latex=f"{sq1} < {val} < {sq2}",
                to_latex_str=f"{n1} < \\sqrt{{{val}}} < {n2}",
                op="Take positive square roots of perfect square bounding integers",
                rule=reason,
            )
        ],
        final_latex=correct,
    )

    q = make_math_question(
        prefix="g11_exp",
        topic=TOPIC,
        subskill="03_estimate_surd_between_consecutive_integers",
        learning_objective_id=f"{LO_PREFIX}_03",
        prompt=prompt,
        prompt_latex=prompt,
        answer_mode="mcq",
        question_type="mcq",
        answer_latex=correct,
        sample_answer=correct,
        canonical_solution=sol,
        marking_schema={
            "total_marks": 2,
            "steps": [
                {"desc": f"Identify bounding perfect squares {sq1} and {sq2}", "marks": 1},
                {"desc": f"State consecutive integers {n1} and {n2}", "marks": 1},
            ],
        },
        hints={
            "nudge": f"Look for the perfect squares immediately below and above {val}.",
            "concept": "If a < x < b and a, b are perfect squares, then sqrt(a) < sqrt(x) < sqrt(b).",
            "breakdown": reason,
        },
        misconception_tags=["using_half_of_radicand_instead_of_square_root"],
        term=1,
        caps_weight_percent=15,
        suggested_duration_mins=3,
        difficulty="easy",
    )
    q["options"] = options
    return q


# ---------------------------------------------------------------------------
# 04. Exponent Laws: Product and Quotient with Prime Base Factorisation
# ---------------------------------------------------------------------------
def build_04_exponent_laws_product_quotient_numerical(r: random.Random) -> Dict[str, Any]:
    base = r.choice([2, 3])
    x_var = "x"
    a = r.randint(1, 3)
    b = r.randint(1, 2)
    # Expression: (base^(x + a) * base^(2x)) / base^(3x - b)
    # = base^(x + a + 2x - (3x - b)) = base^(3x + a - 3x + b) = base^(a + b)
    ans_exp = a + b
    ans_val = base ** ans_exp

    num_latex = f"{base}^{{{x_var} + {a}}} \\cdot {base}^{{2{x_var}}}"
    den_latex = f"{base}^{{3{x_var} - {b}}}"
    expr_latex = f"\\frac{{{num_latex}}}{{{den_latex}}}"

    prompt = f"Simplify the expression fully without using a calculator:\n\n$${expr_latex}$$"

    sol = solution_graph(
        goal="Simplify exponential fraction using exponent laws",
        chain_type="expression",
        steps=[
            step(
                from_latex=expr_latex,
                to_latex_str=f"\\frac{{{base}^{{{x_var} + {a} + 2{x_var}}}}}{{{base}^{{3{x_var} - {b}}}}}",
                op="Apply product rule in numerator: a^m * a^n = a^(m+n)",
                rule="Product of powers with same base",
            ),
            step(
                from_latex=f"{base}^{{3{x_var} + {a} - (3{x_var} - {b})}}",
                to_latex_str=f"{base}^{{{a} + {b}}}",
                op="Apply quotient rule: a^m / a^n = a^(m-n)",
                rule="Quotient of powers with same base",
            ),
            step(
                from_latex=f"{base}^{{{ans_exp}}}",
                to_latex_str=f"{ans_val}",
                op="Evaluate final integer power",
                rule=f"{base}^{ans_exp} = {ans_val}",
            ),
        ],
        final_latex=str(ans_val),
    )

    q = make_math_question(
        prefix="g11_exp",
        topic=TOPIC,
        subskill="04_exponent_laws_product_quotient_numerical",
        learning_objective_id=f"{LO_PREFIX}_04",
        prompt=prompt,
        prompt_latex=prompt,
        answer_mode="typed",
        question_type="math_short",
        answer_latex=str(ans_val),
        answer_sympy=str(ans_val),
        sample_answer=str(ans_val),
        canonical_solution=sol,
        marking_schema={
            "total_marks": 3,
            "steps": [
                {"desc": "Add exponents in numerator", "marks": 1},
                {"desc": "Subtract exponent of denominator with correct brackets", "marks": 1},
                {"desc": f"Final simplified value {ans_val}", "marks": 1},
            ],
        },
        hints={
            "nudge": "All powers share the exact same base. Combine numerator terms first.",
            "concept": "Remember to distribute the negative sign when subtracting: - (3x - b) = -3x + b.",
            "breakdown": f"Exponents combine as: (x + {a}) + 2x - (3x - {b}) = 3x + {a} - 3x + {b} = {ans_exp}. Then {base}^{ans_exp} = {ans_val}.",
        },
        misconception_tags=["sign_error_when_subtracting_denominator_exponent"],
        term=1,
        caps_weight_percent=15,
        suggested_duration_mins=4,
        difficulty="medium",
    )
    return q


# ---------------------------------------------------------------------------
# 05. Exponent Laws: Power-of-Power with Negative Exponents
# ---------------------------------------------------------------------------
def build_05_exponent_laws_power_of_power_negative(r: random.Random) -> Dict[str, Any]:
    a = r.randint(1, 3)
    b = r.randint(2, 4)
    p = r.randint(2, 3)
    # (x^(-a) * y^b)^(-p) = x^(a*p) * y^(-b*p) = x^(a*p) / y^(b*p)
    exp_x = a * p
    exp_y = b * p
    
    expr_latex = f"\\left(x^{{-{a}}} y^{{{b}}}\\right)^{{-{p}}}"
    ans_latex = f"\\frac{{x^{{{exp_x}}}}}{{y^{{{exp_y}}}}}"

    prompt = f"Simplify the expression and write the answer with positive exponents only:\n\n$${expr_latex}$$"

    sol = solution_graph(
        goal="Apply power of power rule and express with positive exponents",
        chain_type="expression",
        steps=[
            step(
                from_latex=expr_latex,
                to_latex_str=f"x^{{(-{a}) \\cdot (-{p})}} \\cdot y^{{{b} \\cdot (-{p})}}",
                op="Multiply each internal exponent by the outer exponent: (x^m)^n = x^(m*n)",
                rule="Power of a power rule",
            ),
            step(
                from_latex=f"x^{{{exp_x}}} y^{{-{exp_y}}}",
                to_latex_str=ans_latex,
                op="Convert negative exponent into reciprocal: y^(-k) = 1 / y^k",
                rule="Definition of negative exponent",
            ),
        ],
        final_latex=ans_latex,
    )

    q = make_math_question(
        prefix="g11_exp",
        topic=TOPIC,
        subskill="05_exponent_laws_power_of_power_negative",
        learning_objective_id=f"{LO_PREFIX}_05",
        prompt=prompt,
        prompt_latex=prompt,
        answer_mode="typed",
        question_type="math_short",
        answer_latex=ans_latex,
        answer_sympy=f"x**{exp_x} / y**{exp_y}",
        sample_answer=ans_latex,
        canonical_solution=sol,
        marking_schema={
            "total_marks": 3,
            "steps": [
                {"desc": f"Correct exponent for x: (-{a}) * (-{p}) = {exp_x}", "marks": 1},
                {"desc": f"Correct exponent for y: {b} * (-{p}) = -{exp_y}", "marks": 1},
                {"desc": f"Written with positive exponent in denominator: {ans_latex}", "marks": 1},
            ],
        },
        hints={
            "nudge": "Multiply each exponent inside the bracket by the outer exponent.",
            "concept": "(a^m * b^n)^p = a^(m*p) * b^(n*p). A negative exponent means reciprocal: y^(-n) = 1/(y^n).",
            "breakdown": f"x: (-{a}) * (-{p}) = +{exp_x}. y: {b} * (-{p}) = -{exp_y}. Write with positive exponents: {ans_latex}.",
        },
        misconception_tags=["forgetting_to_distribute_power_to_all_factors"],
        term=1,
        caps_weight_percent=15,
        suggested_duration_mins=4,
        difficulty="medium",
    )
    return q


# ---------------------------------------------------------------------------
# 06. Simplify Monomial Exponential Fraction (Composite to Prime Bases)
# ---------------------------------------------------------------------------
def build_06_simplify_exponential_fraction_monomial(r: random.Random) -> Dict[str, Any]:
    # Simplify (6^n * 10^(n+1)) / (15^n * 2^(2n+1))
    # 6 = 2 * 3; 10 = 2 * 5; 15 = 3 * 5
    # Numerator: (2*3)^n * (2*5)^(n+1) = 2^n * 3^n * 2^(n+1) * 5^(n+1) = 2^(2n+1) * 3^n * 5^(n+1)
    # Denominator: (3*5)^n * 2^(2n+1) = 3^n * 5^n * 2^(2n+1)
    # Quotient: 5^(n+1 - n) = 5^1 = 5
    p_factor = r.choice([2, 3, 5])
    # Let's parameterize cleanly:
    # (6^n * 2) / (2^n * 3^n) = 2
    # or (10^n * 25) / (2^n * 5^(n+2)) = 1
    # Let's use: (6^n * 10) / (2^(n-1) * 3^n) = 20
    k = r.choice([1, 2, 3])
    # (2^(n+k) * 6^n) / (12^n) = (2^(n+k) * 2^n * 3^n) / (2^(2n) * 3^n) = 2^(2n+k) / 2^(2n) = 2^k
    ans_val = 2 ** k
    
    num_latex = f"2^{{n + {k}}} \\cdot 6^n"
    den_latex = f"12^n"
    expr_latex = f"\\frac{{{num_latex}}}{{{den_latex}}}"

    prompt = f"Simplify the expression to a single integer without using a calculator:\n\n$${expr_latex}$$"

    sol = solution_graph(
        goal="Simplify composite exponential fraction via prime bases",
        chain_type="expression",
        steps=[
            step(
                from_latex=expr_latex,
                to_latex_str=f"\\frac{{2^{{n + {k}}} \\cdot (2 \\cdot 3)^n}}{{(2^2 \\cdot 3)^n}}",
                op="Factorise bases 6 and 12 into prime factors (2 and 3)",
                rule="Prime base decomposition",
            ),
            step(
                from_latex=f"\\frac{{2^{{n + {k}}} \\cdot 2^n \\cdot 3^n}}{{2^{{2n}} \\cdot 3^n}}",
                to_latex_str=f"\\frac{{2^{{2n + {k}}} \\cdot 3^n}}{{2^{{2n}} \\cdot 3^n}}",
                op="Apply power of product and combine like bases in numerator",
                rule="Exponent product rule",
            ),
            step(
                from_latex=f"2^{{(2n + {k}) - 2n}} \\cdot 3^{{n - n}}",
                to_latex_str=f"2^{{{k}}} = {ans_val}",
                op="Apply quotient rule and evaluate integer power",
                rule="Exponent quotient rule",
            ),
        ],
        final_latex=str(ans_val),
    )

    q = make_math_question(
        prefix="g11_exp",
        topic=TOPIC,
        subskill="06_simplify_exponential_fraction_monomial",
        learning_objective_id=f"{LO_PREFIX}_06",
        prompt=prompt,
        prompt_latex=prompt,
        answer_mode="typed",
        question_type="math_short",
        answer_latex=str(ans_val),
        answer_sympy=str(ans_val),
        sample_answer=str(ans_val),
        canonical_solution=sol,
        marking_schema={
            "total_marks": 3,
            "steps": [
                {"desc": "Decompose 6 = 2*3 and 12 = 2^2 * 3", "marks": 1},
                {"desc": "Collect powers of 2 and powers of 3", "marks": 1},
                {"desc": f"Final answer {ans_val}", "marks": 1},
            ],
        },
        hints={
            "nudge": "Break composite numbers into prime factors: 6 = 2 · 3 and 12 = 2² · 3.",
            "concept": "Express every base as prime factors before applying product and quotient exponent rules.",
            "breakdown": f"Numerator becomes 2^(n+{k}) · 2^n · 3^n = 2^(2n+{k}) · 3^n. Denominator is 2^(2n) · 3^n. Dividing gives 2^{k} = {ans_val}.",
        },
        misconception_tags=["cancelling_bases_without_prime_factorisation"],
        term=1,
        caps_weight_percent=15,
        suggested_duration_mins=4,
        difficulty="medium",
    )
    return q


# ---------------------------------------------------------------------------
# 07. Exponential Factorisation: Common Factor Binomial Numerator
# ---------------------------------------------------------------------------
def build_07_exponential_common_factor_binomial_numerator(r: random.Random) -> Dict[str, Any]:
    base = r.choice([2, 3, 5])
    k = r.choice([1, 2, 3])
    # Expression: (base^(x + k) - base^x) / base^x
    # = base^x * (base^k - 1) / base^x = base^k - 1
    ans_val = (base ** k) - 1
    
    num_latex = f"{base}^{{x + {k}}} - {base}^x"
    den_latex = f"{base}^x"
    expr_latex = f"\\frac{{{num_latex}}}{{{den_latex}}}"

    prompt = f"Simplify the following algebraic fraction by factorising:\n\n$${expr_latex}$$"

    sol = solution_graph(
        goal="Simplify exponential fraction by common factor extraction",
        chain_type="expression",
        steps=[
            step(
                from_latex=expr_latex,
                to_latex_str=f"\\frac{{{base}^x \\cdot {base}^{{{k}}} - {base}^x}}{{{base}^x}}",
                op=f"Split {base}^(x+{k}) into {base}^x * {base}^{k}",
                rule="Exponent expansion: a^(m+n) = a^m * a^n",
            ),
            step(
                from_latex=f"\\frac{{{base}^x \\left({base}^{{{k}}} - 1\\right)}}{{{base}^x}}",
                to_latex_str=f"{base}^{{{k}}} - 1 = {ans_val}",
                op=f"Factor out common factor {base}^x and cancel with denominator",
                rule="Common factor cancellation",
            ),
        ],
        final_latex=str(ans_val),
    )

    q = make_math_question(
        prefix="g11_exp",
        topic=TOPIC,
        subskill="07_exponential_common_factor_binomial_numerator",
        learning_objective_id=f"{LO_PREFIX}_07",
        prompt=prompt,
        prompt_latex=prompt,
        answer_mode="typed",
        question_type="math_short",
        answer_latex=str(ans_val),
        answer_sympy=str(ans_val),
        sample_answer=str(ans_val),
        canonical_solution=sol,
        marking_schema={
            "total_marks": 3,
            "steps": [
                {"desc": f"Split base powers: {base}^(x+{k}) = {base}^x * {base}^{k}", "marks": 1},
                {"desc": f"Factor out common factor {base}^x", "marks": 1},
                {"desc": f"Evaluate bracket: {base}^{k} - 1 = {ans_val}", "marks": 1},
            ],
        },
        hints={
            "nudge": "Because the numerator has addition/subtraction terms, you CANNOT cancel individual terms; factor out the common power first.",
            "concept": "Split the powers: base^(x+k) = base^x · base^k. Then factor out base^x.",
            "breakdown": f"{base}^(x+{k}) - {base}^x = {base}^x({base}^{k} - 1). Cancelling {base}^x with the denominator leaves {base}^{k} - 1 = {ans_val}.",
        },
        misconception_tags=["illegal_cancellation_over_addition_subtraction"],
        term=1,
        caps_weight_percent=15,
        suggested_duration_mins=4,
        difficulty="medium",
    )
    return q


# ---------------------------------------------------------------------------
# 08. Exponential Common Factor Split Both Numerator and Denominator
# ---------------------------------------------------------------------------
def build_08_exponential_common_factor_split_both(r: random.Random) -> Dict[str, Any]:
    base = r.choice([2, 3])
    # Expression: (base^(x+2) - base^x) / (base^(x+1) + base^x)
    # = base^x * (base^2 - 1) / (base^x * (base + 1))
    # = (base^2 - 1) / (base + 1) = base - 1
    ans_val = base - 1

    num_latex = f"{base}^{{x + 2}} - {base}^x"
    den_latex = f"{base}^{{x + 1}} + {base}^x"
    expr_latex = f"\\frac{{{num_latex}}}{{{den_latex}}}"

    prompt = f"Simplify the algebraic fraction fully:\n\n$${expr_latex}$$"

    sol = solution_graph(
        goal="Simplify exponential fraction by factoring common terms in numerator and denominator",
        chain_type="expression",
        steps=[
            step(
                from_latex=expr_latex,
                to_latex_str=f"\\frac{{{base}^x \\left({base}^2 - 1\\right)}}{{{base}^x \\left({base} + 1\\right)}}",
                op=f"Factor out {base}^x from both numerator and denominator",
                rule="Common factor extraction",
            ),
            step(
                from_latex=f"\\frac{{{base}^2 - 1}}{{{base} + 1}}",
                to_latex_str=f"\\frac{{({base} - 1)({base} + 1)}}{{{base} + 1}} = {ans_val}",
                op="Factorise difference of squares in numerator and cancel",
                rule=f"({base}^2 - 1) = ({base}-1)({base}+1)",
            ),
        ],
        final_latex=str(ans_val),
    )

    q = make_math_question(
        prefix="g11_exp",
        topic=TOPIC,
        subskill="08_exponential_common_factor_split_both",
        learning_objective_id=f"{LO_PREFIX}_08",
        prompt=prompt,
        prompt_latex=prompt,
        answer_mode="typed",
        question_type="math_short",
        answer_latex=str(ans_val),
        answer_sympy=str(ans_val),
        sample_answer=str(ans_val),
        canonical_solution=sol,
        marking_schema={
            "total_marks": 3,
            "steps": [
                {"desc": f"Factor out {base}^x in numerator and denominator", "marks": 1},
                {"desc": "Cancel common factors", "marks": 1},
                {"desc": f"Simplify numerical expression to {ans_val}", "marks": 1},
            ],
        },
        hints={
            "nudge": f"Factorise {base}^x out of both the top and the bottom expressions.",
            "concept": "Always look for common factors when terms are separated by plus or minus signs in exponential fractions.",
            "breakdown": f"Top: {base}^x({base}² - 1) = {base}^x({base**2 - 1}). Bottom: {base}^x({base} + 1) = {base}^x({base + 1}). Ratio = {base**2 - 1}/{base + 1} = {ans_val}.",
        },
        misconception_tags=["subtracting_exponents_across_addition_terms"],
        term=1,
        caps_weight_percent=15,
        suggested_duration_mins=4,
        difficulty="medium",
    )
    return q


# ---------------------------------------------------------------------------
# 09. Exponential Difference of Squares
# ---------------------------------------------------------------------------
def build_09_exponential_difference_of_squares(r: random.Random) -> Dict[str, Any]:
    base = r.choice([2, 3])
    k = r.choice([1, 2])
    # Expression: ( (base^2)^x - k^2 ) / (base^x + k) = base^x - k
    # e.g. (4^x - 9) / (2^x + 3) = 2^x - 3
    base_sq = base * base
    k_sq = k * k

    num_latex = f"{base_sq}^x - {k_sq}"
    den_latex = f"{base}^x + {k}"
    expr_latex = f"\\frac{{{num_latex}}}{{{den_latex}}}"
    ans_latex = f"{base}^x - {k}"

    prompt = f"Factorise and simplify the algebraic fraction:\n\n$${expr_latex}$$"

    sol = solution_graph(
        goal="Factorise exponential difference of squares",
        chain_type="expression",
        steps=[
            step(
                from_latex=expr_latex,
                to_latex_str=f"\\frac{{\\left({base}^x\\right)^2 - {k}^2}}{{{base}^x + {k}}}",
                op=f"Rewrite {base_sq}^x as ({base}^x)^2",
                rule="Power of a power rule: a^(2x) = (a^x)^2",
            ),
            step(
                from_latex=f"\\frac{{\\left({base}^x - {k}\\right)\\left({base}^x + {k}\\right)}}{{{base}^x + {k}}}",
                to_latex_str=ans_latex,
                op=f"Factorise as difference of squares and cancel common binomial factor ({base}^x + {k})",
                rule="Difference of two squares",
            ),
        ],
        final_latex=ans_latex,
    )

    q = make_math_question(
        prefix="g11_exp",
        topic=TOPIC,
        subskill="09_exponential_difference_of_squares",
        learning_objective_id=f"{LO_PREFIX}_09",
        prompt=prompt,
        prompt_latex=prompt,
        answer_mode="typed",
        question_type="math_short",
        answer_latex=ans_latex,
        answer_sympy=f"{base}**x - {k}",
        sample_answer=ans_latex,
        canonical_solution=sol,
        marking_schema={
            "total_marks": 3,
            "steps": [
                {"desc": f"Recognize {base_sq}^x as ({base}^x)^2", "marks": 1},
                {"desc": f"Factorise numerator as ({base}^x - {k})({base}^x + {k})", "marks": 1},
                {"desc": f"Cancel common factor to leave {ans_latex}", "marks": 1},
            ],
        },
        hints={
            "nudge": f"Notice that {base_sq} = {base}², so {base_sq}^x = ({base}^x)².",
            "concept": "A² - B² = (A - B)(A + B), where A = base^x.",
            "breakdown": f"({base}^x - {k})({base}^x + {k}) / ({base}^x + {k}) = {base}^x - {k}.",
        },
        misconception_tags=["failing_to_recognize_exponential_difference_of_squares"],
        term=1,
        caps_weight_percent=15,
        suggested_duration_mins=4,
        difficulty="medium",
    )
    return q


# ---------------------------------------------------------------------------
# 10. Exponential Trinomial Factorisation
# ---------------------------------------------------------------------------
def build_10_exponential_trinomial_factorisation(r: random.Random) -> Dict[str, Any]:
    base = r.choice([2, 3])
    p = r.choice([1, 2])
    q_val = r.choice([3, 4])
    # (base^x - p)(base^x - q) = base^(2x) - (p+q)*base^x + p*q
    b_coef = p + q_val
    c_val = p * q_val

    num_latex = f"{base}^{{2x}} - {b_coef} \\cdot {base}^x + {c_val}"
    den_latex = f"{base}^x - {p}"
    expr_latex = f"\\frac{{{num_latex}}}{{{den_latex}}}"
    ans_latex = f"{base}^x - {q_val}"

    prompt = f"Simplify the algebraic fraction by factorising the trinomial:\n\n$${expr_latex}$$"

    sol = solution_graph(
        goal="Factorise quadratic exponential trinomial",
        chain_type="expression",
        steps=[
            step(
                from_latex=expr_latex,
                to_latex_str=f"\\frac{{\\left({base}^x - {p}\\right)\\left({base}^x - {q_val}\\right)}}{{{base}^x - {p}}}",
                op=f"Factorise quadratic in {base}^x (using k = {base}^x if helpful)",
                rule="Trinomial factorisation: k² - (p+q)k + pq = (k-p)(k-q)",
            ),
            step(
                from_latex=f"\\frac{{\\left({base}^x - {p}\\right)\\left({base}^x - {q_val}\\right)}}{{{base}^x - {p}}}",
                to_latex_str=ans_latex,
                op=f"Cancel ({base}^x - {p})",
                rule="Binomial cancellation",
            ),
        ],
        final_latex=ans_latex,
    )

    q = make_math_question(
        prefix="g11_exp",
        topic=TOPIC,
        subskill="10_exponential_trinomial_factorisation",
        learning_objective_id=f"{LO_PREFIX}_10",
        prompt=prompt,
        prompt_latex=prompt,
        answer_mode="typed",
        question_type="math_short",
        answer_latex=ans_latex,
        answer_sympy=f"{base}**x - {q_val}",
        sample_answer=ans_latex,
        canonical_solution=sol,
        marking_schema={
            "total_marks": 3,
            "steps": [
                {"desc": f"Factorise quadratic numerator as ({base}^x - {p})({base}^x - {q_val})", "marks": 2},
                {"desc": f"Cancel binomial denominator to get {ans_latex}", "marks": 1},
            ],
        },
        hints={
            "nudge": f"Let k = {base}^x. The numerator is a standard quadratic: k² - {b_coef}k + {c_val}.",
            "concept": "Find two numbers that multiply to {c_val} and add up to -{b_coef}.",
            "breakdown": f"k² - {b_coef}k + {c_val} = (k - {p})(k - {q_val}). Replacing k with {base}^x and dividing by ({base}^x - {p}) gives {base}^x - {q_val}.",
        },
        misconception_tags=["failing_to_treat_exponential_expression_as_quadratic"],
        term=1,
        caps_weight_percent=15,
        suggested_duration_mins=4,
        difficulty="hard",
    )
    return q


# ---------------------------------------------------------------------------
# 11. Convert Rational Exponent to Radical Form
# ---------------------------------------------------------------------------
def build_11_rational_exponent_to_radical_form(r: random.Random) -> Dict[str, Any]:
    base = r.choice(["x", "y", "a", "b"])
    m = r.choice([2, 3, 5])
    n = r.choice([3, 4, 7])
    while m == n:
        n = r.choice([3, 4, 7])

    expr_latex = f"{base}^{{\\frac{{{m}}}{{{n}}}}}"
    correct = f"\\sqrt[{n}]{{{base}^{{{m}}}}}"
    distractors = [
        f"\\sqrt[{m}]{{{base}^{{{n}}}}}",
        f"\\frac{{{base}^{{{m}}}}}{{{n}}}",
        f"{m}\\sqrt[{n}]{{{base}}}",
    ]
    options = [f"${correct}$"] + [f"${d}$" for d in distractors]
    r.shuffle(options)

    prompt = f"Convert the following expression with a rational exponent into radical form:\n\n$${expr_latex}$$\n\nChoose the correct radical representation."

    sol = solution_graph(
        goal="Convert rational exponent to radical form",
        chain_type="conversion",
        steps=[
            step(
                from_latex=expr_latex,
                to_latex_str=correct,
                op="Apply rule a^(m/n) = root_n(a^m)",
                rule="The denominator of a rational exponent is the root index, and the numerator is the power",
            )
        ],
        final_latex=correct,
    )

    q = make_math_question(
        prefix="g11_exp",
        topic=TOPIC,
        subskill="11_rational_exponent_to_radical_form",
        learning_objective_id=f"{LO_PREFIX}_11",
        prompt=prompt,
        prompt_latex=prompt,
        answer_mode="mcq",
        question_type="mcq",
        answer_latex=f"${correct}$",
        sample_answer=f"${correct}$",
        canonical_solution=sol,
        marking_schema={
            "total_marks": 2,
            "steps": [
                {"desc": f"Identify root index as denominator {n}", "marks": 1},
                {"desc": f"Correct radical form \\sqrt[{n}]{{{base}^{{{m}}}}}", "marks": 1},
            ],
        },
        hints={
            "nudge": "In a fractional exponent m/n, which number indicates the root and which indicates the power?",
            "concept": "The denominator 'n' always indicates the index of the radical (root), while the numerator 'm' is the exponent: a^(m/n) = nth-root(a^m).",
            "breakdown": f"The denominator is {n}, which becomes the root index \\sqrt[{n}]{{...}}. The numerator is {m}, so the radicand is {base}^{m}.",
        },
        misconception_tags=["swapping_root_index_and_power_in_rational_exponent"],
        term=1,
        caps_weight_percent=15,
        suggested_duration_mins=3,
        difficulty="easy",
    )
    q["options"] = options
    return q


# ---------------------------------------------------------------------------
# 12. Convert Radical Form to Rational Exponent Form
# ---------------------------------------------------------------------------
def build_12_radical_to_rational_exponent_form(r: random.Random) -> Dict[str, Any]:
    base = r.choice(["x", "y", "p", "q"])
    m = r.choice([3, 5, 7])
    n = r.choice([2, 4, 6])
    
    expr_latex = f"\\sqrt[{n}]{{{base}^{{{m}}}}}"
    correct = f"{base}^{{\\frac{{{m}}}{{{n}}}}}"
    distractors = [
        f"{base}^{{\\frac{{{n}}}{{{m}}}}}",
        f"{base}^{{{m} - {n}}}",
        f"{base}^{{{m} \\cdot {n}}}",
    ]
    options = [f"${correct}$"] + [f"${d}$" for d in distractors]
    r.shuffle(options)

    prompt = f"Express the following radical in rational exponent form $a^{{\\frac{{m}}{{n}}}}$:\n\n$${expr_latex}$$\n\nChoose the correct form."

    sol = solution_graph(
        goal="Convert radical form to rational exponent form",
        chain_type="conversion",
        steps=[
            step(
                from_latex=expr_latex,
                to_latex_str=correct,
                op="Rewrite root index as denominator of fraction exponent",
                rule="root_n(a^m) = a^(m/n)",
            )
        ],
        final_latex=correct,
    )

    q = make_math_question(
        prefix="g11_exp",
        topic=TOPIC,
        subskill="12_radical_to_rational_exponent_form",
        learning_objective_id=f"{LO_PREFIX}_12",
        prompt=prompt,
        prompt_latex=prompt,
        answer_mode="mcq",
        question_type="mcq",
        answer_latex=f"${correct}$",
        sample_answer=f"${correct}$",
        canonical_solution=sol,
        marking_schema={
            "total_marks": 2,
            "steps": [
                {"desc": f"Place power {m} in numerator and root index {n} in denominator", "marks": 2},
            ],
        },
        hints={
            "nudge": "The root index goes into the denominator of the fractional exponent.",
            "concept": "The general formula is root_n(a^m) = a^(m/n).",
            "breakdown": f"Here, power m = {m} and root index n = {n}, so the exponent is {m}/{n}.",
        },
        misconception_tags=["inverting_fractional_exponent_order"],
        term=1,
        caps_weight_percent=15,
        suggested_duration_mins=3,
        difficulty="easy",
    )
    q["options"] = options
    return q


# ---------------------------------------------------------------------------
# 13. Evaluate Numerical Fractional Exponent Without Calculator
# ---------------------------------------------------------------------------
def build_13_evaluate_numerical_fractional_exponent(r: random.Random) -> Dict[str, Any]:
    triplet = r.choice([
        (16, 3, 4, 2, 8),    # 16^(3/4) = (2^4)^(3/4) = 2^3 = 8
        (27, 2, 3, 3, 9),    # 27^(2/3) = (3^3)^(2/3) = 3^2 = 9
        (32, 3, 5, 2, 8),    # 32^(3/5) = (2^5)^(3/5) = 2^3 = 8
        (81, 3, 4, 3, 27),   # 81^(3/4) = (3^4)^(3/4) = 3^3 = 27
        (64, 2, 3, 4, 16),   # 64^(2/3) = (4^3)^(2/3) = 4^2 = 16
        (125, 2, 3, 5, 25),  # 125^(2/3) = (5^3)^(2/3) = 5^2 = 25
    ])
    base_val, m, n, prime_base, ans_val = triplet

    expr_latex = f"{base_val}^{{\\frac{{{m}}}{{{n}}}}}"

    prompt = f"Evaluate the expression without using a calculator:\n\n$${expr_latex}$$"

    sol = solution_graph(
        goal="Evaluate numerical expression with rational exponent",
        chain_type="expression",
        steps=[
            step(
                from_latex=expr_latex,
                to_latex_str=f"\\left({prime_base}^{{{n}}}\\right)^{{\\frac{{{m}}}{{{n}}}}}",
                op=f"Express {base_val} as prime power {prime_base}^{n}",
                rule="Prime base decomposition",
            ),
            step(
                from_latex=f"\\left({prime_base}^{{{n}}}\\right)^{{\\frac{{{m}}}{{{n}}}}}",
                to_latex_str=f"{prime_base}^{{{n} \\cdot \\frac{{{m}}}{{{n}}}}} = {prime_base}^{{{m}}}",
                op="Multiply exponents: n * (m/n) = m",
                rule="Power of a power rule",
            ),
            step(
                from_latex=f"{prime_base}^{{{m}}}",
                to_latex_str=str(ans_val),
                op=f"Evaluate integer power {prime_base}^{m}",
                rule=f"{prime_base}^{m} = {ans_val}",
            ),
        ],
        final_latex=str(ans_val),
    )

    q = make_math_question(
        prefix="g11_exp",
        topic=TOPIC,
        subskill="13_evaluate_numerical_fractional_exponent",
        learning_objective_id=f"{LO_PREFIX}_13",
        prompt=prompt,
        prompt_latex=prompt,
        answer_mode="typed",
        question_type="math_short",
        answer_latex=str(ans_val),
        answer_sympy=str(ans_val),
        sample_answer=str(ans_val),
        canonical_solution=sol,
        marking_schema={
            "total_marks": 2,
            "steps": [
                {"desc": f"Rewrite {base_val} as {prime_base}^{n}", "marks": 1},
                {"desc": f"Evaluate {prime_base}^{m} = {ans_val}", "marks": 1},
            ],
        },
        hints={
            "nudge": f"Write {base_val} in exponential form using base {prime_base}.",
            "concept": "(a^n)^(m/n) = a^m.",
            "breakdown": f"{base_val} = {prime_base}^{n}. Then ({prime_base}^{n})^({m}/{n}) = {prime_base}^{m} = {ans_val}.",
        },
        misconception_tags=["multiplying_base_by_fraction_instead_of_raising_to_power"],
        term=1,
        caps_weight_percent=15,
        suggested_duration_mins=3,
        difficulty="easy",
    )
    return q


# ---------------------------------------------------------------------------
# 14. Simplify Expression with Fractional Exponents (Binomial Conjugate)
# ---------------------------------------------------------------------------
def build_14_simplify_expression_with_fractional_exponents(r: random.Random) -> Dict[str, Any]:
    var = r.choice(["x", "a", "y"])
    k = r.choice([2, 3, 4, 5])
    k_sq = k * k

    # (var^(1/2) - k)(var^(1/2) + k) = (var^(1/2))^2 - k^2 = var - k_sq
    expr_latex = f"\\left({var}^{{\\frac{{1}}{{2}}}} - {k}\\right)\\left({var}^{{\\frac{{1}}{{2}}}} + {k}\\right)"
    ans_latex = f"{var} - {k_sq}"

    prompt = f"Expand and simplify the algebraic expression:\n\n$${expr_latex}$$"

    sol = solution_graph(
        goal="Expand conjugate binomials with fractional exponents",
        chain_type="expression",
        steps=[
            step(
                from_latex=expr_latex,
                to_latex_str=f"\\left({var}^{{\\frac{{1}}{{2}}}}\\right)^2 - {k}^2",
                op="Apply difference of squares formula (A - B)(A + B) = A² - B²",
                rule="Conjugate product",
            ),
            step(
                from_latex=f"\\left({var}^{{\\frac{{1}}{{2}}}}\\right)^2 - {k}^2",
                to_latex_str=ans_latex,
                op=f"Simplify (var^(1/2))^2 = var and {k}^2 = {k_sq}",
                rule="Exponent multiplication: (1/2)*2 = 1",
            ),
        ],
        final_latex=ans_latex,
    )

    q = make_math_question(
        prefix="g11_exp",
        topic=TOPIC,
        subskill="14_simplify_expression_with_fractional_exponents",
        learning_objective_id=f"{LO_PREFIX}_14",
        prompt=prompt,
        prompt_latex=prompt,
        answer_mode="typed",
        question_type="math_short",
        answer_latex=ans_latex,
        answer_sympy=f"{var} - {k_sq}",
        sample_answer=ans_latex,
        canonical_solution=sol,
        marking_schema={
            "total_marks": 2,
            "steps": [
                {"desc": f"Recognize difference of squares ( {var}^(1/2) )^2 - {k}^2", "marks": 1},
                {"desc": f"Final simplified form {ans_latex}", "marks": 1},
            ],
        },
        hints={
            "nudge": "Notice that this has the form (A - B)(A + B) = A² - B².",
            "concept": "(x^(1/2))² = x^(1/2 · 2) = x¹ = x.",
            "breakdown": f"( {var}^(1/2) )² - ({k})² = {var} - {k_sq}.",
        },
        misconception_tags=["middle_term_confusion_in_difference_of_squares"],
        term=1,
        caps_weight_percent=15,
        suggested_duration_mins=3,
        difficulty="easy",
    )
    return q


# ---------------------------------------------------------------------------
# 15. Simplify Single Surd into Simplest Radical Form a√b
# ---------------------------------------------------------------------------
def build_15_simplify_single_surd_prime_factorisation(r: random.Random) -> Dict[str, Any]:
    prime = r.choice([2, 3, 5, 7])
    a = r.choice([2, 3, 4, 5, 6])
    n = a * a * prime

    expr_latex = f"\\sqrt{{{n}}}"
    ans_latex = f"{a}\\sqrt{{{prime}}}"

    prompt = f"Write the surd in simplest form $a\\sqrt{{b}}$, where $b$ is a prime number:\n\n$${expr_latex}$$\n\n(Do not use a calculator.)"

    sol = solution_graph(
        goal="Simplify surd by extracting perfect square factor",
        chain_type="expression",
        steps=[
            step(
                from_latex=expr_latex,
                to_latex_str=f"\\sqrt{{{a * a} \\times {prime}}}",
                op=f"Factorise {n} into greatest perfect square {a * a} and prime {prime}",
                rule="Prime factorisation and square factor extraction",
            ),
            step(
                from_latex=f"\\sqrt{{{a * a}}} \\times \\sqrt{{{prime}}}",
                to_latex_str=ans_latex,
                op=f"Take square root of {a * a} to get {a}",
                rule="Surd multiplication rule: sqrt(a*b) = sqrt(a)*sqrt(b)",
            ),
        ],
        final_latex=ans_latex,
    )

    q = make_math_question(
        prefix="g11_exp",
        topic=TOPIC,
        subskill="15_simplify_single_surd_prime_factorisation",
        learning_objective_id=f"{LO_PREFIX}_15",
        prompt=prompt,
        prompt_latex=prompt,
        answer_mode="typed",
        question_type="math_short",
        answer_latex=ans_latex,
        answer_sympy=f"{a}*sqrt({prime})",
        sample_answer=ans_latex,
        canonical_solution=sol,
        marking_schema={
            "total_marks": 2,
            "steps": [
                {"desc": f"Extract largest perfect square factor {a * a}", "marks": 1},
                {"desc": f"Simplest surd form {ans_latex}", "marks": 1},
            ],
        },
        hints={
            "nudge": f"What is the largest perfect square (4, 9, 16, 25, 36...) that divides {n}?",
            "concept": "sqrt(a · b) = sqrt(a) · sqrt(b). Extract the square root of the square factor.",
            "breakdown": f"{n} = {a * a} · {prime}. Therefore \\sqrt{{{n}}} = \\sqrt{{{a * a}}} \\cdot \\sqrt{{{prime}}} = {ans_latex}.",
        },
        misconception_tags=["not_extracting_largest_perfect_square"],
        term=1,
        caps_weight_percent=15,
        suggested_duration_mins=3,
        difficulty="easy",
    )
    return q


# ---------------------------------------------------------------------------
# 16. Add and Subtract Like Surds
# ---------------------------------------------------------------------------
def build_16_add_subtract_like_surds(r: random.Random) -> Dict[str, Any]:
    prime = r.choice([2, 3, 5])
    c1 = r.choice([1, 2])
    c2 = r.choice([3, 4])
    c3 = r.choice([1, 2])
    
    n1 = (c1 ** 2) * prime
    n2 = (c2 ** 2) * prime
    n3 = (c3 ** 2) * prime
    
    final_coef = c1 + c2 - c3
    expr_latex = f"\\sqrt{{{n1}}} + \\sqrt{{{n2}}} - \\sqrt{{{n3}}}"
    ans_latex = f"{final_coef}\\sqrt{{{prime}}}" if final_coef != 1 else f"\\sqrt{{{prime}}}"

    prompt = f"Simplify without the use of a calculator:\n\n$${expr_latex}$$"

    sol = solution_graph(
        goal="Simplify and combine like surds",
        chain_type="expression",
        steps=[
            step(
                from_latex=expr_latex,
                to_latex_str=f"{c1}\\sqrt{{{prime}}} + {c2}\\sqrt{{{prime}}} - {c3}\\sqrt{{{prime}}}",
                op="Simplify each surd by extracting perfect square factors",
                rule=f"\\sqrt{{{n1}}}={c1}\\sqrt{{{prime}}}, \\sqrt{{{n2}}}={c2}\\sqrt{{{prime}}}, \\sqrt{{{n3}}}={c3}\\sqrt{{{prime}}}",
            ),
            step(
                from_latex=f"({c1} + {c2} - {c3})\\sqrt{{{prime}}}",
                to_latex_str=ans_latex,
                op=f"Add and subtract like surds: ({c1} + {c2} - {c3}) = {final_coef}",
                rule="Distributive property on like surd terms",
            ),
        ],
        final_latex=ans_latex,
    )

    q = make_math_question(
        prefix="g11_exp",
        topic=TOPIC,
        subskill="16_add_subtract_like_surds",
        learning_objective_id=f"{LO_PREFIX}_16",
        prompt=prompt,
        prompt_latex=prompt,
        answer_mode="typed",
        question_type="math_short",
        answer_latex=ans_latex,
        answer_sympy=f"{final_coef}*sqrt({prime})",
        sample_answer=ans_latex,
        canonical_solution=sol,
        marking_schema={
            "total_marks": 3,
            "steps": [
                {"desc": "Simplify each individual surd to simplest form", "marks": 2},
                {"desc": f"Collect like surds to obtain {ans_latex}", "marks": 1},
            ],
        },
        hints={
            "nudge": f"Simplify each square root individually to a multiple of \\sqrt{{{prime}}}.",
            "concept": "Like surds have identical radicands and can be added or subtracted just like like algebraic terms: a√p + b√p = (a+b)√p.",
            "breakdown": f"\\sqrt{{{n1}}} = {c1}\\sqrt{{{prime}}}, \\sqrt{{{n2}}} = {c2}\\sqrt{{{prime}}}, \\sqrt{{{n3}}} = {c3}\\sqrt{{{prime}}}. Combined: ({c1} + {c2} - {c3})\\sqrt{{{prime}}} = {ans_latex}.",
        },
        misconception_tags=["adding_radicands_directly_under_single_root"],
        term=1,
        caps_weight_percent=15,
        suggested_duration_mins=4,
        difficulty="medium",
    )
    return q


# ---------------------------------------------------------------------------
# 17. Add and Subtract Higher Coefficient Surds
# ---------------------------------------------------------------------------
def build_17_add_subtract_higher_coefficient_surds(r: random.Random) -> Dict[str, Any]:
    prime = r.choice([2, 3])
    k1 = r.randint(2, 4)
    k2 = r.randint(2, 3)
    
    # Let first surd be k1 * sqrt(18) = k1 * 3*sqrt(2)
    # Let second surd be k2 * sqrt(50) = k2 * 5*sqrt(2)
    c1 = r.choice([2, 3])
    c2 = r.choice([4, 5])
    
    rad1 = (c1 ** 2) * prime
    rad2 = (c2 ** 2) * prime
    
    total_coef = k1 * c1 - k2 * c2
    expr_latex = f"{k1}\\sqrt{{{rad1}}} - {k2}\\sqrt{{{rad2}}}"
    ans_latex = f"{total_coef}\\sqrt{{{prime}}}" if total_coef != 1 else f"\\sqrt{{{prime}}}"

    prompt = f"Simplify the expression fully without a calculator:\n\n$${expr_latex}$$"

    sol = solution_graph(
        goal="Combine surds with exterior coefficients",
        chain_type="expression",
        steps=[
            step(
                from_latex=expr_latex,
                to_latex_str=f"{k1} \\cdot \\left({c1}\\sqrt{{{prime}}}\\right) - {k2} \\cdot \\left({c2}\\sqrt{{{prime}}}\\right)",
                op="Extract square factors from radicands",
                rule=f"\\sqrt{{{rad1}}}={c1}\\sqrt{{{prime}}}, \\sqrt{{{rad2}}}={c2}\\sqrt{{{prime}}}",
            ),
            step(
                from_latex=f"{k1 * c1}\\sqrt{{{prime}}} - {k2 * c2}\\sqrt{{{prime}}}",
                to_latex_str=ans_latex,
                op=f"Multiply coefficients: ({k1 * c1} - {k2 * c2})\\sqrt{{{prime}}} = {total_coef}\\sqrt{{{prime}}}",
                rule="Combine like surds",
            ),
        ],
        final_latex=ans_latex,
    )

    q = make_math_question(
        prefix="g11_exp",
        topic=TOPIC,
        subskill="17_add_subtract_higher_coefficient_surds",
        learning_objective_id=f"{LO_PREFIX}_17",
        prompt=prompt,
        prompt_latex=prompt,
        answer_mode="typed",
        question_type="math_short",
        answer_latex=ans_latex,
        answer_sympy=f"{total_coef}*sqrt({prime})",
        sample_answer=ans_latex,
        canonical_solution=sol,
        marking_schema={
            "total_marks": 3,
            "steps": [
                {"desc": f"Simplify \\sqrt{{{rad1}}} to {c1}\\sqrt{{{prime}}} and \\sqrt{{{rad2}}} to {c2}\\sqrt{{{prime}}}", "marks": 1},
                {"desc": f"Multiply by outer coefficients: {k1 * c1}\\sqrt{{{prime}}} and {k2 * c2}\\sqrt{{{prime}}}", "marks": 1},
                {"desc": f"Final combined surd {ans_latex}", "marks": 1},
            ],
        },
        hints={
            "nudge": "Simplify the radical first, then multiply by the number in front of the root.",
            "concept": "k · √(a² · b) = k · a · √b.",
            "breakdown": f"{k1}·{c1}√{prime} - {k2}·{c2}√{prime} = {k1*c1}√{prime} - {k2*c2}√{prime} = {ans_latex}.",
        },
        misconception_tags=["adding_coefficients_before_simplifying_radicand"],
        term=1,
        caps_weight_percent=15,
        suggested_duration_mins=4,
        difficulty="medium",
    )
    return q


# ---------------------------------------------------------------------------
# 18. Multiply Monomial Surds
# ---------------------------------------------------------------------------
def build_18_multiply_monomial_surds(r: random.Random) -> Dict[str, Any]:
    # e.g. sqrt(6) * sqrt(15) = sqrt(90) = 3*sqrt(10)
    # or sqrt(10) * sqrt(14) = sqrt(140) = 2*sqrt(35)
    pair = r.choice([
        (6, 15, 90, 3, 10),
        (10, 14, 140, 2, 35),
        (8, 6, 48, 4, 3),
        (12, 10, 120, 2, 30),
        (15, 20, 300, 10, 3),
    ])
    r1, r2, prod, a_out, b_in = pair

    expr_latex = f"\\sqrt{{{r1}}} \\times \\sqrt{{{r2}}}"
    ans_latex = f"{a_out}\\sqrt{{{b_in}}}"

    prompt = f"Multiply and write in the form $a\\sqrt{{b}}$ where $b$ has no square factors:\n\n$${expr_latex}$$"

    sol = solution_graph(
        goal="Multiply surds and simplify product",
        chain_type="expression",
        steps=[
            step(
                from_latex=expr_latex,
                to_latex_str=f"\\sqrt{{{r1} \\times {r2}}} = \\sqrt{{{prod}}}",
                op="Multiply radicands under a single square root",
                rule="\\sqrt{a} \\times \\sqrt{b} = \\sqrt{a \\cdot b}",
            ),
            step(
                from_latex=f"\\sqrt{{{a_out * a_out} \\times {b_in}}}",
                to_latex_str=ans_latex,
                op=f"Extract square factor {a_out * a_out}",
                rule=f"\\sqrt{{{a_out * a_out}}} = {a_out}",
            ),
        ],
        final_latex=ans_latex,
    )

    q = make_math_question(
        prefix="g11_exp",
        topic=TOPIC,
        subskill="18_multiply_monomial_surds",
        learning_objective_id=f"{LO_PREFIX}_18",
        prompt=prompt,
        prompt_latex=prompt,
        answer_mode="typed",
        question_type="math_short",
        answer_latex=ans_latex,
        answer_sympy=f"{a_out}*sqrt({b_in})",
        sample_answer=ans_latex,
        canonical_solution=sol,
        marking_schema={
            "total_marks": 2,
            "steps": [
                {"desc": f"Multiply radicands: \\sqrt{{{prod}}}", "marks": 1},
                {"desc": f"Extract square factor to obtain {ans_latex}", "marks": 1},
            ],
        },
        hints={
            "nudge": "Multiply the numbers inside the radicals: √a · √b = √(ab).",
            "concept": "After multiplying, factor out the largest perfect square from the product.",
            "breakdown": f"\\sqrt{{{r1}}} \\cdot \\sqrt{{{r2}}} = \\sqrt{{{prod}}} = \\sqrt{{{a_out**2} \\cdot {b_in}}} = {ans_latex}.",
        },
        misconception_tags=["forgetting_to_simplify_final_surd_product"],
        term=1,
        caps_weight_percent=15,
        suggested_duration_mins=3,
        difficulty="easy",
    )
    return q


# ---------------------------------------------------------------------------
# 19. Distribute Monomial Surd Over Binomial
# ---------------------------------------------------------------------------
def build_19_distribute_monomial_surd_over_binomial(r: random.Random) -> Dict[str, Any]:
    # sqrt(3) * (2*sqrt(3) - sqrt(6)) = 2*3 - sqrt(18) = 6 - 3*sqrt(2)
    p = r.choice([2, 3, 5])
    c = r.choice([2, 3])
    other = r.choice([2, 3]) if p != 2 else 3

    # Expression: \sqrt{p} ( c\sqrt{p} - \sqrt{p * other} )
    # = c * p - \sqrt{p^2 * other} = c*p - p\sqrt{other}
    cp = c * p
    expr_latex = f"\\sqrt{{{p}}}\\left({c}\\sqrt{{{p}}} - \\sqrt{{{p * other}}}\\right)"
    ans_latex = f"{cp} - {p}\\sqrt{{{other}}}"

    prompt = f"Expand and simplify without using a calculator:\n\n$${expr_latex}$$"

    sol = solution_graph(
        goal="Distribute surd over binomial terms",
        chain_type="expression",
        steps=[
            step(
                from_latex=expr_latex,
                to_latex_str=f"{c} \\cdot \\left(\\sqrt{{{p}}}\\right)^2 - \\sqrt{{{p} \\times {p * other}}}",
                op="Multiply \\sqrt{p} by each term in parentheses",
                rule="Distributive law",
            ),
            step(
                from_latex=f"{c} \\cdot {p} - \\sqrt{{{p * p * other}}}",
                to_latex_str=ans_latex,
                op=f"Evaluate ({c})({p}) = {cp} and simplify \\sqrt{{{p**2} \\cdot {other}}} = {p}\\sqrt{{{other}}}",
                rule="Simplify integer product and radical",
            ),
        ],
        final_latex=ans_latex,
    )

    q = make_math_question(
        prefix="g11_exp",
        topic=TOPIC,
        subskill="19_distribute_monomial_surd_over_binomial",
        learning_objective_id=f"{LO_PREFIX}_19",
        prompt=prompt,
        prompt_latex=prompt,
        answer_mode="typed",
        question_type="math_short",
        answer_latex=ans_latex,
        answer_sympy=f"{cp} - {p}*sqrt({other})",
        sample_answer=ans_latex,
        canonical_solution=sol,
        marking_schema={
            "total_marks": 3,
            "steps": [
                {"desc": f"First term multiplication: {c} * (\\sqrt{{{p}}})^2 = {cp}", "marks": 1},
                {"desc": f"Second term multiplication: \\sqrt{{{p * p * other}}} = {p}\\sqrt{{{other}}}", "marks": 1},
                {"desc": f"Final simplified form {ans_latex}", "marks": 1},
            ],
        },
        hints={
            "nudge": "Apply the distributive property: a(b - c) = ab - ac.",
            "concept": "Remember that (√p)² = p, and √p · √(p · q) = √(p² · q) = p√q.",
            "breakdown": f"√{p} · {c}√{p} = {c} · {p} = {cp}. √{p} · √{p*other} = {p}√{other}. Result: {ans_latex}.",
        },
        misconception_tags=["forgetting_that_sqrt_a_squared_equals_a"],
        term=1,
        caps_weight_percent=15,
        suggested_duration_mins=4,
        difficulty="medium",
    )
    return q


# ---------------------------------------------------------------------------
# 20. Expand Binomial Surd Squared
# ---------------------------------------------------------------------------
def build_20_expand_binomial_surd_squared(r: random.Random) -> Dict[str, Any]:
    # (\sqrt{a} + \sqrt{b})^2 = a + 2\sqrt{ab} + b = (a+b) + 2\sqrt{ab}
    a = r.choice([2, 3, 5])
    b = r.choice([3, 5, 7])
    while a == b:
        b = r.choice([3, 5, 7])

    sum_ab = a + b
    prod_ab = a * b

    expr_latex = f"\\left(\\sqrt{{{a}}} + \\sqrt{{{b}}}\\right)^2"
    ans_latex = f"{sum_ab} + 2\\sqrt{{{prod_ab}}}"

    prompt = f"Expand and simplify the following without a calculator:\n\n$${expr_latex}$$"

    sol = solution_graph(
        goal="Expand perfect square of surd binomial",
        chain_type="expression",
        steps=[
            step(
                from_latex=expr_latex,
                to_latex_str=f"\\left(\\sqrt{{{a}}}\\right)^2 + 2\\left(\\sqrt{{{a}}}\\right)\\left(\\sqrt{{{b}}}\\right) + \\left(\\sqrt{{{b}}}\\right)^2",
                op="Apply (A + B)² = A² + 2AB + B²",
                rule="Perfect square binomial expansion",
            ),
            step(
                from_latex=f"{a} + 2\\sqrt{{{prod_ab}}} + {b}",
                to_latex_str=ans_latex,
                op=f"Add integers {a} + {b} = {sum_ab}",
                rule="Combine rational integers",
            ),
        ],
        final_latex=ans_latex,
    )

    q = make_math_question(
        prefix="g11_exp",
        topic=TOPIC,
        subskill="20_expand_binomial_surd_squared",
        learning_objective_id=f"{LO_PREFIX}_20",
        prompt=prompt,
        prompt_latex=prompt,
        answer_mode="typed",
        question_type="math_short",
        answer_latex=ans_latex,
        answer_sympy=f"{sum_ab} + 2*sqrt({prod_ab})",
        sample_answer=ans_latex,
        canonical_solution=sol,
        marking_schema={
            "total_marks": 3,
            "steps": [
                {"desc": f"Correct squared terms: (\\sqrt{{{a}}})^2 = {a} and (\\sqrt{{{b}}})^2 = {b}", "marks": 1},
                {"desc": f"Correct middle term: 2\\sqrt{{{prod_ab}}}", "marks": 1},
                {"desc": f"Final answer {ans_latex}", "marks": 1},
            ],
        },
        hints={
            "nudge": "Do not just square each term individually; remember the middle term 2AB!",
            "concept": "(√a + √b)² = a + 2√(ab) + b.",
            "breakdown": f"(\\sqrt{{{a}}})² + 2(\\sqrt{{{a}}})(\\sqrt{{{b}}}) + (\\sqrt{{{b}}})² = {a} + 2\\sqrt{{{prod_ab}}} + {b} = {ans_latex}.",
        },
        misconception_tags=["freshman_dream_omitting_middle_term_in_squared_binomial"],
        term=1,
        caps_weight_percent=15,
        suggested_duration_mins=4,
        difficulty="medium",
    )
    return q


# ---------------------------------------------------------------------------
# 21. Expand Difference of Squares Surd Conjugates
# ---------------------------------------------------------------------------
def build_21_expand_difference_of_squares_surds(r: random.Random) -> Dict[str, Any]:
    # (a + \sqrt{b})(a - \sqrt{b}) = a^2 - b
    a = r.choice([2, 3, 4, 5])
    b = r.choice([2, 3, 5, 7])
    ans_val = (a * a) - b

    expr_latex = f"\\left({a} + \\sqrt{{{b}}}\\right)\\left({a} - \\sqrt{{{b}}}\\right)"

    prompt = f"Simplify by multiplying the conjugate surds:\n\n$${expr_latex}$$"

    sol = solution_graph(
        goal="Multiply surd conjugates using difference of squares",
        chain_type="expression",
        steps=[
            step(
                from_latex=expr_latex,
                to_latex_str=f"{a}^2 - \\left(\\sqrt{{{b}}}\\right)^2",
                op="Apply difference of squares: (A + B)(A - B) = A² - B²",
                rule="Difference of squares identity",
            ),
            step(
                from_latex=f"{a * a} - {b}",
                to_latex_str=str(ans_val),
                op=f"Subtract rational integers {a * a} - {b} = {ans_val}",
                rule="Arithmetic evaluation",
            ),
        ],
        final_latex=str(ans_val),
    )

    q = make_math_question(
        prefix="g11_exp",
        topic=TOPIC,
        subskill="21_expand_difference_of_squares_surds",
        learning_objective_id=f"{LO_PREFIX}_21",
        prompt=prompt,
        prompt_latex=prompt,
        answer_mode="typed",
        question_type="math_short",
        answer_latex=str(ans_val),
        answer_sympy=str(ans_val),
        sample_answer=str(ans_val),
        canonical_solution=sol,
        marking_schema={
            "total_marks": 2,
            "steps": [
                {"desc": f"Apply difference of squares: {a}^2 - (\\sqrt{{{b}}})^2", "marks": 1},
                {"desc": f"Final evaluated rational number {ans_val}", "marks": 1},
            ],
        },
        hints={
            "nudge": "Conjugate terms multiply out to a difference of squares: (A + B)(A - B) = A² - B².",
            "concept": "Notice that (√b)² = b, so all radicals disappear!",
            "breakdown": f"{a}² - (√{b})² = {a*a} - {b} = {ans_val}.",
        },
        misconception_tags=["keeping_radicals_in_conjugate_product"],
        term=1,
        caps_weight_percent=15,
        suggested_duration_mins=3,
        difficulty="easy",
    )
    return q


# ---------------------------------------------------------------------------
# 22. Rationalise Monomial Denominator
# ---------------------------------------------------------------------------
def build_22_rationalise_monomial_denominator(r: random.Random) -> Dict[str, Any]:
    # a / \sqrt{b} -> if a is multiple of b, e.g. 10 / \sqrt{5} = 2\sqrt{5}
    # otherwise e.g. 6 / \sqrt{2} = 3\sqrt{2}, 12 / \sqrt{3} = 4\sqrt{3}
    b = r.choice([2, 3, 5, 7])
    k = r.choice([2, 3, 4, 5])
    a = k * b

    expr_latex = f"\\frac{{{a}}}{{\\sqrt{{{b}}}}}"
    ans_latex = f"{k}\\sqrt{{{b}}}"

    prompt = f"Rationalise the denominator and simplify fully:\n\n$${expr_latex}$$"

    sol = solution_graph(
        goal="Rationalise monomial surd denominator",
        chain_type="expression",
        steps=[
            step(
                from_latex=expr_latex,
                to_latex_str=f"\\frac{{{a}}}{{\\sqrt{{{b}}}}} \\times \\frac{{\\sqrt{{{b}}}}}{{\\sqrt{{{b}}}}}",
                op="Multiply numerator and denominator by \\sqrt{b}",
                rule="Multiplying by identity 1 in radical form",
            ),
            step(
                from_latex=f"\\frac{{{a}\\sqrt{{{b}}}}}{{{b}}}",
                to_latex_str=ans_latex,
                op=f"Divide {a} by {b} = {k}",
                rule=f"{a}/{b} = {k}",
            ),
        ],
        final_latex=ans_latex,
    )

    q = make_math_question(
        prefix="g11_exp",
        topic=TOPIC,
        subskill="22_rationalise_monomial_denominator",
        learning_objective_id=f"{LO_PREFIX}_22",
        prompt=prompt,
        prompt_latex=prompt,
        answer_mode="typed",
        question_type="math_short",
        answer_latex=ans_latex,
        answer_sympy=f"{k}*sqrt({b})",
        sample_answer=ans_latex,
        canonical_solution=sol,
        marking_schema={
            "total_marks": 2,
            "steps": [
                {"desc": f"Multiply numerator and denominator by \\sqrt{{{b}}}", "marks": 1},
                {"desc": f"Final simplified form {ans_latex}", "marks": 1},
            ],
        },
        hints={
            "nudge": f"Multiply both top and bottom by \\sqrt{{{b}}}.",
            "concept": "To eliminate a square root in the denominator, multiply by that same square root because √b · √b = b.",
            "breakdown": f"({a} · √{b}) / (√{b} · √{b}) = {a}√{b} / {b} = {ans_latex}.",
        },
        misconception_tags=["squaring_the_fraction_instead_of_multiplying_by_one"],
        term=1,
        caps_weight_percent=15,
        suggested_duration_mins=3,
        difficulty="easy",
    )
    return q


# ---------------------------------------------------------------------------
# 23. Rationalise Binomial Denominator (Sum with Conjugate)
# ---------------------------------------------------------------------------
def build_23_rationalise_binomial_denominator_sum(r: random.Random) -> Dict[str, Any]:
    # c / (\sqrt{a} + b)
    # Let's choose values such that denominator a - b^2 simplifies cleanly:
    # e.g. \sqrt{5} + 2 -> conj: \sqrt{5} - 2 -> den = 5 - 4 = 1
    # or \sqrt{3} + 1 -> conj: \sqrt{3} - 1 -> den = 3 - 1 = 2
    # e.g. 2 / (\sqrt{3} + 1) = 2(\sqrt{3} - 1) / 2 = \sqrt{3} - 1
    case = r.choice([
        (5, 2, 1, 1),   # 1 / (\sqrt{5} + 2) = \sqrt{5} - 2
        (3, 1, 2, 1),   # 2 / (\sqrt{3} + 1) = \sqrt{3} - 1
        (7, 2, 3, 1),   # 3 / (\sqrt{7} + 2) = \sqrt{7} - 2
        (10, 3, 1, 1),  # 1 / (\sqrt{10} + 3) = \sqrt{10} - 3
    ])
    rad_a, b_int, num_c, multiplier = case
    den_diff = rad_a - (b_int ** 2)

    expr_latex = f"\\frac{{{num_c}}}{{\\sqrt{{{rad_a}}} + {b_int}}}"
    ans_latex = f"\\sqrt{{{rad_a}}} - {b_int}"

    prompt = f"Rationalise the denominator and simplify fully:\n\n$${expr_latex}$$"

    sol = solution_graph(
        goal="Rationalise binomial surd denominator using conjugate",
        chain_type="expression",
        steps=[
            step(
                from_latex=expr_latex,
                to_latex_str=f"\\frac{{{num_c}\\left(\\sqrt{{{rad_a}}} - {b_int}\\right)}}{{\\left(\\sqrt{{{rad_a}}} + {b_int}\\right)\\left(\\sqrt{{{rad_a}}} - {b_int}\\right)}}",
                op=f"Multiply numerator and denominator by conjugate (\\sqrt{{{rad_a}}} - {b_int})",
                rule="Conjugate multiplication for binomial surd denominator",
            ),
            step(
                from_latex=f"\\frac{{{num_c}\\left(\\sqrt{{{rad_a}}} - {b_int}\\right)}}{{{rad_a} - {b_int ** 2}}}",
                to_latex_str=ans_latex,
                op=f"Simplify denominator ({rad_a} - {b_int**2} = {den_diff}) and cancel with {num_c}",
                rule="Difference of squares in denominator",
            ),
        ],
        final_latex=ans_latex,
    )

    q = make_math_question(
        prefix="g11_exp",
        topic=TOPIC,
        subskill="23_rationalise_binomial_denominator_sum",
        learning_objective_id=f"{LO_PREFIX}_23",
        prompt=prompt,
        prompt_latex=prompt,
        answer_mode="typed",
        question_type="math_short",
        answer_latex=ans_latex,
        answer_sympy=f"sqrt({rad_a}) - {b_int}",
        sample_answer=ans_latex,
        canonical_solution=sol,
        marking_schema={
            "total_marks": 3,
            "steps": [
                {"desc": f"Multiply top and bottom by conjugate \\sqrt{{{rad_a}}} - {b_int}", "marks": 1},
                {"desc": f"Correct denominator evaluation {rad_a} - {b_int**2} = {den_diff}", "marks": 1},
                {"desc": f"Final simplified form {ans_latex}", "marks": 1},
            ],
        },
        hints={
            "nudge": f"The conjugate of (\\sqrt{{{rad_a}}} + {b_int}) is (\\sqrt{{{rad_a}}} - {b_int}).",
            "concept": "Multiplying a binomial (A + B) by its conjugate (A - B) produces A² - B², which eliminates all radicals.",
            "breakdown": f"Top becomes {num_c}(\\sqrt{{{rad_a}}} - {b_int}). Bottom is (\\sqrt{{{rad_a}}})² - {b_int}² = {rad_a} - {b_int**2} = {den_diff}. Cancelling gives {ans_latex}.",
        },
        misconception_tags=["using_wrong_conjugate_sign"],
        term=1,
        caps_weight_percent=15,
        suggested_duration_mins=4,
        difficulty="medium",
    )
    return q


# ---------------------------------------------------------------------------
# 24. Rationalise Binomial Denominator (Difference with Conjugate)
# ---------------------------------------------------------------------------
def build_24_rationalise_binomial_denominator_diff(r: random.Random) -> Dict[str, Any]:
    # c / (\sqrt{a} - \sqrt{b})
    # e.g. (\sqrt{5} - \sqrt{3}) -> conjugate (\sqrt{5} + \sqrt{3}) -> den = 5 - 3 = 2
    # e.g. 2 / (\sqrt{5} - \sqrt{3}) = \sqrt{5} + \sqrt{3}
    case = r.choice([
        (5, 3, 2),  # 2 / (\sqrt{5} - \sqrt{3}) = \sqrt{5} + \sqrt{3}
        (7, 5, 2),  # 2 / (\sqrt{7} - \sqrt{5}) = \sqrt{7} + \sqrt{5}
        (5, 2, 3),  # 3 / (\sqrt{5} - \sqrt{2}) = \sqrt{5} + \sqrt{2}
        (3, 2, 1),  # 1 / (\sqrt{3} - \sqrt{2}) = \sqrt{3} + \sqrt{2}
    ])
    rad_a, rad_b, num_c = case
    den_diff = rad_a - rad_b

    expr_latex = f"\\frac{{{num_c}}}{{\\sqrt{{{rad_a}}} - \\sqrt{{{rad_b}}}}}"
    ans_latex = f"\\sqrt{{{rad_a}}} + \\sqrt{{{rad_b}}}"

    prompt = f"Rationalise the denominator and simplify fully:\n\n$${expr_latex}$$"

    sol = solution_graph(
        goal="Rationalise two-radical binomial denominator",
        chain_type="expression",
        steps=[
            step(
                from_latex=expr_latex,
                to_latex_str=f"\\frac{{{num_c}\\left(\\sqrt{{{rad_a}}} + \\sqrt{{{rad_b}}}\\right)}}{{\\left(\\sqrt{{{rad_a}}} - \\sqrt{{{rad_b}}}\\right)\\left(\\sqrt{{{rad_a}}} + \\sqrt{{{rad_b}}}\\right)}}",
                op=f"Multiply numerator and denominator by conjugate (\\sqrt{{{rad_a}}} + \\sqrt{{{rad_b}}})",
                rule="Conjugate multiplication for radical difference",
            ),
            step(
                from_latex=f"\\frac{{{num_c}\\left(\\sqrt{{{rad_a}}} + \\sqrt{{{rad_b}}}\\right)}}{{{rad_a} - {rad_b}}}",
                to_latex_str=ans_latex,
                op=f"Evaluate denominator ({rad_a} - {rad_b} = {den_diff}) and cancel with numerator {num_c}",
                rule="Difference of squares evaluation",
            ),
        ],
        final_latex=ans_latex,
    )

    q = make_math_question(
        prefix="g11_exp",
        topic=TOPIC,
        subskill="24_rationalise_binomial_denominator_diff",
        learning_objective_id=f"{LO_PREFIX}_24",
        prompt=prompt,
        prompt_latex=prompt,
        answer_mode="typed",
        question_type="math_short",
        answer_latex=ans_latex,
        answer_sympy=f"sqrt({rad_a}) + sqrt({rad_b})",
        sample_answer=ans_latex,
        canonical_solution=sol,
        marking_schema={
            "total_marks": 3,
            "steps": [
                {"desc": f"Multiply by conjugate \\sqrt{{{rad_a}}} + \\sqrt{{{rad_b}}}", "marks": 1},
                {"desc": f"Evaluate denominator as {rad_a} - {rad_b} = {den_diff}", "marks": 1},
                {"desc": f"Final simplified expression {ans_latex}", "marks": 1},
            ],
        },
        hints={
            "nudge": f"Multiply both top and bottom by (\\sqrt{{{rad_a}}} + \\sqrt{{{rad_b}}}).",
            "concept": "(√a - √b)(√a + √b) = a - b.",
            "breakdown": f"Top becomes {num_c}(√{rad_a} + √{rad_b}). Bottom is {rad_a} - {rad_b} = {den_diff}. Dividing by {den_diff} gives {ans_latex}.",
        },
        misconception_tags=["sign_error_conjugate"],
        term=1,
        caps_weight_percent=15,
        suggested_duration_mins=4,
        difficulty="medium",
    )
    return q


# ---------------------------------------------------------------------------
# 25. Rationalise Two-Term Surd Fraction Sum
# ---------------------------------------------------------------------------
def build_25_rationalise_two_term_surd_expression_sum(r: random.Random) -> Dict[str, Any]:
    # 1 / (\sqrt{n} + 1) + 1 / (\sqrt{n} - 1)
    # Common denominator = (\sqrt{n} + 1)(\sqrt{n} - 1) = n - 1
    # Numerator = (\sqrt{n} - 1) + (\sqrt{n} + 1) = 2\sqrt{n}
    # e.g. 1 / (\sqrt{3} + 1) + 1 / (\sqrt{3} - 1) = 2\sqrt{3} / (3 - 1) = \sqrt{3}
    # or n = 5: 1 / (\sqrt{5} + 1) + 1 / (\sqrt{5} - 1) = 2\sqrt{5} / 4 = \frac{\sqrt{5}}{2}
    n = r.choice([3, 5, 7])
    den = n - 1
    
    if den == 2:
        ans_latex = f"\\sqrt{{{n}}}"
        ans_sympy = f"sqrt({n})"
    else:
        half_den = den // 2
        ans_latex = f"\\frac{{\\sqrt{{{n}}}}}{{{half_den}}}"
        ans_sympy = f"sqrt({n})/{half_den}"

    expr_latex = f"\\frac{{1}}{{\\sqrt{{{n}}} + 1}} + \\frac{{1}}{{\\sqrt{{{n}}} - 1}}"

    prompt = f"Simplify the expression by finding a common denominator:\n\n$${expr_latex}$$"

    sol = solution_graph(
        goal="Simplify sum of two reciprocal conjugate surd fractions",
        chain_type="expression",
        steps=[
            step(
                from_latex=expr_latex,
                to_latex_str=f"\\frac{{\\left(\\sqrt{{{n}}} - 1\\right) + \\left(\\sqrt{{{n}}} + 1\\right)}}{{\\left(\\sqrt{{{n}}} + 1\\right)\\left(\\sqrt{{{n}}} - 1\\right)}}",
                op="Bring over common denominator (difference of squares)",
                rule="Fraction addition rule",
            ),
            step(
                from_latex=f"\\frac{{2\\sqrt{{{n}}}}}{{{n} - 1}}",
                to_latex_str=ans_latex,
                op=f"Simplify numerator (\\sqrt{{{n}}} - 1 + \\sqrt{{{n}}} + 1 = 2\\sqrt{{{n}}}) and denominator ({n} - 1 = {den})",
                rule=f"Divide numerator and denominator by 2",
            ),
        ],
        final_latex=ans_latex,
    )

    q = make_math_question(
        prefix="g11_exp",
        topic=TOPIC,
        subskill="25_rationalise_two_term_surd_expression_sum",
        learning_objective_id=f"{LO_PREFIX}_25",
        prompt=prompt,
        prompt_latex=prompt,
        answer_mode="typed",
        question_type="math_short",
        answer_latex=ans_latex,
        answer_sympy=ans_sympy,
        sample_answer=ans_latex,
        canonical_solution=sol,
        marking_schema={
            "total_marks": 3,
            "steps": [
                {"desc": f"Find LCD: (\\sqrt{{{n}}} + 1)(\\sqrt{{{n}}} - 1) = {den}", "marks": 1},
                {"desc": f"Combine numerators: \\sqrt{{{n}}} - 1 + \\sqrt{{{n}}} + 1 = 2\\sqrt{{{n}}}", "marks": 1},
                {"desc": f"Final simplified fraction {ans_latex}", "marks": 1},
            ],
        },
        hints={
            "nudge": "Find the LCD, which is the product of the two denominators: (√n + 1)(√n - 1).",
            "concept": "The product of the denominators is a difference of squares: (√n)² - 1² = n - 1.",
            "breakdown": f"Top becomes (√{n} - 1) + (√{n} + 1) = 2√{n}. Bottom is {n} - 1 = {den}. Simplifying gives {ans_latex}.",
        },
        misconception_tags=["failing_to_find_lcd_in_algebraic_fraction_sum"],
        term=1,
        caps_weight_percent=15,
        suggested_duration_mins=4,
        difficulty="hard",
    )
    return q


# ---------------------------------------------------------------------------
# Registry of Archetypes 01–25
# ---------------------------------------------------------------------------
BUILDERS_01_25: Dict[str, Any] = {
    "01_classify_real_nonreal_numbers": build_01_classify_real_nonreal_numbers,
    "02_classify_rational_irrational_surds": build_02_classify_rational_irrational_surds,
    "03_estimate_surd_between_consecutive_integers": build_03_estimate_surd_between_consecutive_integers,
    "04_exponent_laws_product_quotient_numerical": build_04_exponent_laws_product_quotient_numerical,
    "05_exponent_laws_power_of_power_negative": build_05_exponent_laws_power_of_power_negative,
    "06_simplify_exponential_fraction_monomial": build_06_simplify_exponential_fraction_monomial,
    "07_exponential_common_factor_binomial_numerator": build_07_exponential_common_factor_binomial_numerator,
    "08_exponential_common_factor_split_both": build_08_exponential_common_factor_split_both,
    "09_exponential_difference_of_squares": build_09_exponential_difference_of_squares,
    "10_exponential_trinomial_factorisation": build_10_exponential_trinomial_factorisation,
    "11_rational_exponent_to_radical_form": build_11_rational_exponent_to_radical_form,
    "12_radical_to_rational_exponent_form": build_12_radical_to_rational_exponent_form,
    "13_evaluate_numerical_fractional_exponent": build_13_evaluate_numerical_fractional_exponent,
    "14_simplify_expression_with_fractional_exponents": build_14_simplify_expression_with_fractional_exponents,
    "15_simplify_single_surd_prime_factorisation": build_15_simplify_single_surd_prime_factorisation,
    "16_add_subtract_like_surds": build_16_add_subtract_like_surds,
    "17_add_subtract_higher_coefficient_surds": build_17_add_subtract_higher_coefficient_surds,
    "18_multiply_monomial_surds": build_18_multiply_monomial_surds,
    "19_distribute_monomial_surd_over_binomial": build_19_distribute_monomial_surd_over_binomial,
    "20_expand_binomial_surd_squared": build_20_expand_binomial_surd_squared,
    "21_expand_difference_of_squares_surds": build_21_expand_difference_of_squares_surds,
    "22_rationalise_monomial_denominator": build_22_rationalise_monomial_denominator,
    "23_rationalise_binomial_denominator_sum": build_23_rationalise_binomial_denominator_sum,
    "24_rationalise_binomial_denominator_diff": build_24_rationalise_binomial_denominator_diff,
    "25_rationalise_two_term_surd_expression_sum": build_25_rationalise_two_term_surd_expression_sum,
}
