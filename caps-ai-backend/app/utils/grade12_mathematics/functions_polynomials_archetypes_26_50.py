"""Grade 12 Mathematics - Functions and Polynomials Archetypes 26 to 50.
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/Mathematics_Gr12/Term 1/02. Functions.md and 03. Polynomials.md.
"""
from __future__ import annotations

import math
import random
from typing import Any, Callable, Dict, List, Optional
import sympy as sp

from .sequences_series_archetypes_01_25 import _svg_spec
from .functions_polynomials_archetypes_01_25 import _mcq_q, _calc_q


# =========================================================================== #
# Archetypes 26 - 50
# =========================================================================== #

def arch_26_polynomial_identification_and_degree(rng: random.Random) -> Dict[str, Any]:
    # e.g. P(x) = 3x^4 - 5x^3 + 2x - 7
    deg = rng.choice([3, 4, 5])
    lead_coeff = rng.choice([2, 3, -4, 5])
    const = rng.choice([-8, -5, 4, 7, 9])
    prompt = (
        f"Consider the algebraic expression $P(x) = {lead_coeff}x^{{{deg}}} - 3x^2 + 6x {'+' if const >= 0 else '-'} {abs(const)}$.\n\n"
        f"1. Explain why $P(x)$ is a polynomial.\n"
        f"2. State the degree of $P(x)$, the leading coefficient, and the constant term."
    )
    correct = f"Polynomial because all exponents are non-negative integers; Degree = {deg}; Leading coefficient = {lead_coeff}; Constant term = {const}"
    distractors = [
        f"Polynomial; Degree = 2; Leading coefficient = -3; Constant term = {const}",
        f"Not a polynomial because it contains negative coefficients; Degree = {deg}",
        f"Polynomial; Degree = {deg}; Leading coefficient = 6; Constant term = 0",
    ]
    sol = (
        f"Step 1: A polynomial is an expression where all variable exponents belong to $\\mathbb{{N}}_0 = \\{{0, 1, 2, \\dots\\}}$.\n"
        f"Here the exponents are ${deg}, 2, 1, 0$, which are all non-negative integers $\\implies$ $P(x)$ is a polynomial.\n"
        f"Step 2: The highest exponent is ${deg}$, so the degree is ${deg}$.\n"
        f"Step 3: The coefficient of the highest power $x^{{{deg}}}$ is ${lead_coeff}$ (leading coefficient).\n"
        f"Step 4: The constant term (independent of $x$) is ${const}$."
    )
    return _mcq_q(
        rng, f"g12_fn_26_{rng.randint(100000, 999999)}", "26_polynomial_identification_and_degree",
        "Polynomial Definition Degree and Coefficients", prompt, correct, distractors, sol,
        {"tier_1": "Recall: Degree is the highest power of x, and constant term has no x.",
         "tier_2": f"Highest power is {deg}, coefficient of x^{{{deg}}} is {lead_coeff}, and constant is {const}.",
         "tier_3": correct},
        ["confused_leading_coefficient_with_constant_term"]
    )


def arch_27_polynomial_evaluation_function_notation(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([1, 2])
    b = rng.choice([-3, 2, 4])
    c = rng.choice([-5, -1, 3])
    d = rng.choice([-4, 2, 6])
    x_val = rng.choice([-2, -1, 2, 3])
    # P(x) = a*x^3 + b*x^2 + c*x + d
    val = a * (x_val**3) + b * (x_val**2) + c * x_val + d
    poly_str = f"{a if a != 1 else ''}x^3 {'+' if b >= 0 else '-'} {abs(b)}x^2 {'+' if c >= 0 else '-'} {abs(c)}x {'+' if d >= 0 else '-'} {abs(d)}"
    prompt = (
        f"Given the polynomial $P(x) = {poly_str}$:\n\n"
        f"Evaluate $P({x_val})$."
    )
    ans = str(val)
    sol = (
        f"Step 1: Substitute $x = {x_val}$ into $P(x)$:\n"
        f"$$P({x_val}) = {a}({x_val})^3 + ({b})({x_val})^2 + ({c})({x_val}) + ({d})$$\n"
        f"$$P({x_val}) = {a}({x_val**3}) + ({b})({x_val**2}) + {c * x_val} + {d}$$\n"
        f"$$P({x_val}) = {a * (x_val**3)} + {b * (x_val**2)} + {c * x_val} + {d} = {val}$$."
    )
    return _calc_q(
        rng, f"g12_fn_27_{rng.randint(100000, 999999)}", "27_polynomial_evaluation_function_notation",
        "Polynomial Evaluation at Given Input", prompt, ans, sol,
        {"tier_1": f"Carefully substitute x = {x_val}, taking care with powers of negative numbers.",
         "tier_2": f"Compute each term: {a * (x_val**3)}, {b * (x_val**2)}, {c * x_val}, and {d}.",
         "tier_3": f"P({x_val}) = {val}."},
        ["sign_error_evaluating_negative_powers"]
    )


def arch_28_remainder_theorem_linear_divisor(rng: random.Random) -> Dict[str, Any]:
    # Remainder when P(x) divided by (x - c) is P(c)
    c_val = rng.choice([1, 2, 3])
    a = rng.choice([1, 2])
    b = rng.choice([-4, -2, 1, 3])
    c = rng.choice([-3, 2, 5])
    d = rng.choice([-6, 4, 8])
    poly_str = f"{a if a != 1 else ''}x^3 {'+' if b >= 0 else '-'} {abs(b)}x^2 {'+' if c >= 0 else '-'} {abs(c)}x {'+' if d >= 0 else '-'} {abs(d)}"
    rem = a * (c_val**3) + b * (c_val**2) + c * c_val + d
    prompt = (
        f"Use the Remainder Theorem to find the remainder when\n"
        f"$$P(x) = {poly_str}$$\n"
        f"is divided by $(x - {c_val})$."
    )
    ans = f"Remainder = {rem}"
    sol = (
        f"Step 1: The Remainder Theorem states that when polynomial $P(x)$ is divided by $(x - c)$, the remainder is $R = P(c)$.\n"
        f"Step 2: Here the divisor is $(x - {c_val})$, so we evaluate $P({c_val})$:\n"
        f"$$P({c_val}) = {a}({c_val})^3 + ({b})({c_val})^2 + ({c})({c_val}) + ({d})$$\n"
        f"$$P({c_val}) = {a * (c_val**3)} + {b * (c_val**2)} + {c * c_val} + {d} = {rem}$$\n"
        f"Thus the remainder is ${rem}$."
    )
    return _calc_q(
        rng, f"g12_fn_28_{rng.randint(100000, 999999)}", "28_remainder_theorem_linear_divisor",
        "Remainder Theorem with Linear Divisor", prompt, ans, sol,
        {"tier_1": f"According to the Remainder Theorem, the remainder equals P({c_val}).",
         "tier_2": f"Substitute x = {c_val} into the polynomial expression.",
         "tier_3": f"Remainder = {rem}."},
        ["substituted_negative_c_instead_of_positive_c"]
    )


def arch_29_remainder_theorem_fractional_divisor(rng: random.Random) -> Dict[str, Any]:
    # Divisor (2x - 1) => evaluate P(1/2)
    # P(x) = 2x^3 - x^2 + 4x - 5
    # P(1/2) = 2*(1/8) - 1/4 + 4*(1/2) - 5 = 1/4 - 1/4 + 2 - 5 = -3
    k = rng.choice([-5, -3, 2, 4, 7])
    # P(x) = 4x^3 - 2x^2 + 6x + k
    # P(1/2) = 4(1/8) - 2(1/4) + 6(1/2) + k = 1/2 - 1/2 + 3 + k = 3 + k
    rem = 3 + k
    prompt = (
        f"Use the Remainder Theorem to find the remainder when\n"
        f"$$f(x) = 4x^3 - 2x^2 + 6x {'+' if k >= 0 else '-'} {abs(k)}$$\n"
        f"is divided by $(2x - 1)$."
    )
    ans = f"Remainder = {rem}"
    sol = (
        f"Step 1: For a divisor of the form $(ax - b)$, the root is $x = \\frac{{b}}{{a}}$.\n"
        f"Setting $2x - 1 = 0 \\implies x = \\frac{{1}}{{2}}$.\n"
        f"Step 2: Evaluate $f\\left(\\frac{{1}}{{2}}\\right)$:\n"
        f"$$f\\left(\\frac{{1}}{{2}}\\right) = 4\\left(\\frac{{1}}{{2}}\\right)^3 - 2\\left(\\frac{{1}}{{2}}\\right)^2 + 6\\left(\\frac{{1}}{{2}}\\right) + ({k})$$\n"
        f"$$f\\left(\\frac{{1}}{{2}}\\right) = 4\\left(\\frac{{1}}{{8}}\\right) - 2\\left(\\frac{{1}}{{4}}\\right) + 3 + {k}$$\n"
        f"$$f\\left(\\frac{{1}}{{2}}\\right) = \\frac{{1}}{{2}} - \\frac{{1}}{{2}} + 3 + {k} = {rem}$$\n"
        f"The remainder is ${rem}$."
    )
    return _calc_q(
        rng, f"g12_fn_29_{rng.randint(100000, 999999)}", "29_remainder_theorem_fractional_divisor",
        "Remainder Theorem with Fractional Linear Divisor", prompt, ans, sol,
        {"tier_1": "Set the divisor 2x - 1 = 0 to get x = 1/2, then evaluate f(1/2).",
         "tier_2": f"f(1/2) = 4(1/8) - 2(1/4) + 6(1/2) + ({k}).",
         "tier_3": f"Remainder = {rem}."},
        ["inverted_fraction_when_substituting_divisor_root"]
    )


def arch_30_remainder_theorem_solve_single_unknown_k(rng: random.Random) -> Dict[str, Any]:
    # P(x) = x^3 + k*x^2 - 4x + 6
    # Divisor (x - 2). P(2) = 8 + 4k - 8 + 6 = 4k + 6
    # Remainder R = target => 4k + 6 = target => k = (target - 6) / 4
    k_val = rng.choice([-3, -2, 1, 2, 4])
    c_val = 2
    rem = 4 * k_val + 6
    prompt = (
        f"When the polynomial $P(x) = x^3 + kx^2 - 4x + 6$ is divided by $(x - {c_val})$, the remainder is ${rem}$.\n\n"
        f"Determine the value of $k$."
    )
    ans = f"k = {k_val}"
    sol = (
        f"Step 1: By the Remainder Theorem, $P({c_val}) = {rem}$.\n"
        f"Step 2: Substitute $x = {c_val}$ into $P(x)$:\n"
        f"$$P({c_val}) = ({c_val})^3 + k({c_val})^2 - 4({c_val}) + 6$$\n"
        f"$$P({c_val}) = 8 + 4k - 8 + 6 = 4k + 6$$\n"
        f"Step 3: Equate to the given remainder:\n"
        f"$$4k + 6 = {rem}$$\n"
        f"$$4k = {rem - 6} \\implies k = {k_val}$$."
    )
    return _calc_q(
        rng, f"g12_fn_30_{rng.randint(100000, 999999)}", "30_remainder_theorem_solve_single_unknown_k",
        "Solving for Unknown Coefficient Using Remainder Theorem", prompt, ans, sol,
        {"tier_1": f"Set P({c_val}) = {rem}.",
         "tier_2": f"8 + 4k - 8 + 6 = {rem}. Solve for k.",
         "tier_3": f"k = {k_val}."},
        ["incorrect_equation_setup_equating_remainder_to_zero"]
    )


def arch_31_remainder_theorem_solve_simultaneous_two_unknowns(rng: random.Random) -> Dict[str, Any]:
    # P(x) = ax^3 + bx^2 - 5x + 2
    # P(1) = a + b - 5 + 2 = a + b - 3 = R1
    # P(-1) = -a + b + 5 + 2 = -a + b + 7 = R2
    a_val = rng.choice([2, 3, 4])
    b_val = rng.choice([-3, 1, 5])
    r1 = a_val + b_val - 3
    r2 = -a_val + b_val + 7
    prompt = (
        f"When $P(x) = ax^3 + bx^2 - 5x + 2$ is divided by $(x - 1)$, the remainder is ${r1}$. "
        f"When divided by $(x + 1)$, the remainder is ${r2}$.\n\n"
        f"Calculate the values of $a$ and $b$."
    )
    correct = f"a = {a_val}, b = {b_val}"
    distractors = [
        f"a = {a_val + 1}, b = {b_val - 1}",
        f"a = {b_val}, b = {a_val}",
        f"a = {-a_val}, b = {b_val}",
    ]
    sol = (
        f"Step 1: Set up equations using the Remainder Theorem:\n"
        f"(1) $P(1) = a(1)^3 + b(1)^2 - 5(1) + 2 = a + b - 3 = {r1} \\implies a + b = {r1 + 3}$\n"
        f"(2) $P(-1) = a(-1)^3 + b(-1)^2 - 5(-1) + 2 = -a + b + 7 = {r2} \\implies -a + b = {r2 - 7}$\n"
        f"Step 2: Add equations (1) and (2) to eliminate $a$:\n"
        f"$$2b = ({r1 + 3}) + ({r2 - 7}) = {2 * b_val} \\implies b = {b_val}$$\n"
        f"Step 3: Substitute $b = {b_val}$ into (1):\n"
        f"$$a + {b_val} = {r1 + 3} \\implies a = {a_val}$$."
    )
    return _mcq_q(
        rng, f"g12_fn_31_{rng.randint(100000, 999999)}", "31_remainder_theorem_solve_simultaneous_two_unknowns",
        "Simultaneous Equations from Remainder Theorem", prompt, correct, distractors, sol,
        {"tier_1": f"Write equations for P(1) = {r1} and P(-1) = {r2}.",
         "tier_2": "Add the two equations to solve for b, then back-substitute to find a.",
         "tier_3": correct},
        ["simultaneous_addition_sign_error"]
    )


def arch_32_factor_theorem_verification(rng: random.Random) -> Dict[str, Any]:
    # Check if (x - c) is a factor
    c_val = rng.choice([1, 2, 3])
    is_factor = rng.choice([True, False])
    # P(x) = (x - c_val)(x^2 + 2x - 3) + remainder
    rem = 0 if is_factor else rng.choice([-5, 4, 7])
    # Expand (x - c)(x^2 + 2x - 3) + rem
    # = x^3 + (2 - c)x^2 + (-3 - 2c)x + (3c + rem)
    b_coeff = 2 - c_val
    c_coeff = -3 - 2 * c_val
    d_const = 3 * c_val + rem
    poly_str = f"x^3 {'+' if b_coeff >= 0 else '-'} {abs(b_coeff)}x^2 {'+' if c_coeff >= 0 else '-'} {abs(c_coeff)}x {'+' if d_const >= 0 else '-'} {abs(d_const)}"

    prompt = (
        f"Use the Factor Theorem to determine whether $(x - {c_val})$ is a factor of\n"
        f"$$P(x) = {poly_str}$$.\n\n"
        f"State YES or NO and show your calculation of $P({c_val})$."
    )
    correct = f"{'YES' if is_factor else 'NO'}, P({c_val}) = {rem}"
    distractors = [
        f"{'NO' if is_factor else 'YES'}, P({c_val}) = {rem + 2}",
        f"{'YES' if is_factor else 'NO'}, P(-{c_val}) = {rem}",
        f"Cannot be determined without synthetic division",
    ]
    sol = (
        f"Step 1: The Factor Theorem states that $(x - c)$ is a factor of $P(x)$ if and only if $P(c) = 0$.\n"
        f"Step 2: Evaluate $P({c_val})$:\n"
        f"$$P({c_val}) = ({c_val})^3 + ({b_coeff})({c_val})^2 + ({c_coeff})({c_val}) + ({d_const}) = {rem}$$\n"
        f"Step 3: Conclusion:\n"
        f"Since $P({c_val}) {'= 0' if is_factor else '\\ne 0'}$, $(x - {c_val})$ is {'indeed a factor' if is_factor else 'NOT a factor'}."
    )
    return _mcq_q(
        rng, f"g12_fn_32_{rng.randint(100000, 999999)}", "32_factor_theorem_verification",
        "Verifying Factors Using the Factor Theorem", prompt, correct, distractors, sol,
        {"tier_1": f"Substitute x = {c_val} into P(x). If P({c_val}) = 0, it is a factor.",
         "tier_2": f"Calculate P({c_val}) = {rem}.",
         "tier_3": correct},
        ["stated_it_is_a_factor_when_remainder_is_non_zero"]
    )


def arch_33_factor_theorem_solve_unknown_coefficient(rng: random.Random) -> Dict[str, Any]:
    # (x - 2) is a factor of 2x^3 - 3x^2 + kx - 10
    # P(2) = 2(8) - 3(4) + 2k - 10 = 16 - 12 + 2k - 10 = 2k - 6 = 0 => k = 3
    k_val = rng.choice([-5, -3, 2, 4, 6])
    c_val = 2
    # P(2) = 2(8) + b(4) + 2k + d = 0
    # Let P(x) = x^3 + 3x^2 + kx - (8 + 12 + 2k)
    const = 8 + 12 + 2 * k_val
    prompt = (
        f"Given that $(x - 2)$ is a factor of $P(x) = x^3 + 3x^2 + kx - {const}$:\n\n"
        f"Determine the value of $k$."
    )
    ans = f"k = {k_val}"
    sol = (
        f"Step 1: Since $(x - 2)$ is a factor, $P(2) = 0$ by the Factor Theorem.\n"
        f"Step 2: Substitute $x = 2$:\n"
        f"$$P(2) = (2)^3 + 3(2)^2 + k(2) - {const} = 0$$\n"
        f"$$8 + 12 + 2k - {const} = 0$$\n"
        f"$$20 + 2k - {const} = 0$$\n"
        f"$$2k = {const - 20} \\implies k = {k_val}$$."
    )
    return _calc_q(
        rng, f"g12_fn_33_{rng.randint(100000, 999999)}", "33_factor_theorem_solve_unknown_coefficient",
        "Solving for Unknown Parameter Using Factor Theorem", prompt, ans, sol,
        {"tier_1": "By the Factor Theorem, P(2) must equal 0.",
         "tier_2": f"8 + 12 + 2k - {const} = 0. Solve for k.",
         "tier_3": f"k = {k_val}."},
        ["sign_error_solving_factor_equation"]
    )


def arch_34_finding_first_rational_root_by_trial(rng: random.Random) -> Dict[str, Any]:
    # P(x) = (x - r1)(x - r2)(x - r3)
    r1 = rng.choice([1, -1, 2, -2])
    r2 = rng.choice([2, 3])
    r3 = rng.choice([-3, -4])
    # Monic cubic
    p = sp.expand((sp.Symbol("x") - r1) * (sp.Symbol("x") - r2) * (sp.Symbol("x") - r3))
    poly_str = sp.latex(p)
    prompt = (
        f"Consider the cubic polynomial equation:\n"
        f"$$P(x) = {poly_str} = 0$$\n\n"
        f"Using trial and error with the factors of the constant term, find a root $x = c$ where $P(c) = 0$, "
        f"and hence state a linear factor of $P(x)$."
    )
    correct = f"x = {r1} is a root because P({r1}) = 0; factor is (x {'-' if r1 > 0 else '+'} {abs(r1)})"
    distractors = [
        f"x = {r1 + 1} is a root; factor is (x - {r1 + 1})",
        f"x = {-r1} is a root because P(-{r1}) = 0; factor is (x - {r1})",
        f"No rational roots exist for this cubic",
    ]
    sol = (
        f"Step 1: The constant term of $P(x)$ is ${int(p.subs(sp.Symbol('x'), 0))}$.\n"
        f"Its integer factors include $\\pm 1, \\pm 2, \\dots$.\n"
        f"Step 2: Test $x = {r1}$:\n"
        f"$$P({r1}) = 0$$\n"
        f"Step 3: By the Factor Theorem, $(x {'-' if r1 > 0 else '+'} {abs(r1)})$ is a factor of $P(x)$."
    )
    return _mcq_q(
        rng, f"g12_fn_34_{rng.randint(100000, 999999)}", "34_finding_first_rational_root_by_trial",
        "Finding First Factor of Cubic by Inspection", prompt, correct, distractors, sol,
        {"tier_1": "Test small factors of the constant term (1, -1, 2, -2) until P(c) = 0.",
         "tier_2": f"P({r1}) = 0, so (x - ({r1})) is a factor.",
         "tier_3": correct},
        ["confused_root_sign_with_factor_sign"]
    )


def arch_35_cubic_factorisation_inspection_method(rng: random.Random) -> Dict[str, Any]:
    # (x - 1)(x^2 + Bx + C) = x^3 + (B - 1)x^2 + (C - B)x - C
    B = rng.choice([2, 3, 4, 5])
    C = rng.choice([-6, -4, 3, 6])
    c1 = 1
    # P(x) = (x - 1)(x^2 + Bx + C)
    p = sp.expand((sp.Symbol("x") - 1) * (sp.Symbol("x")**2 + B * sp.Symbol("x") + C))
    poly_str = sp.latex(p)
    quad_str = f"x^2 {'+' if B >= 0 else '-'} {abs(B)}x {'+' if C >= 0 else '-'} {abs(C)}"
    prompt = (
        f"Given that $(x - 1)$ is a factor of $P(x) = {poly_str}$:\n\n"
        f"Determine the quadratic factor $(x^2 + Bx + C)$ by equating coefficients or inspection."
    )
    correct = quad_str
    distractors = [
        f"x^2 {'-' if B >= 0 else '+'} {abs(B)}x {'+' if C >= 0 else '-'} {abs(C)}",
        f"x^2 {'+' if B >= 0 else '-'} {abs(B)}x {'-' if C >= 0 else '+'} {abs(C)}",
        f"2x^2 + {B}x + {C}",
    ]
    sol = (
        f"Step 1: Write $P(x) = (x - 1)(x^2 + Bx + C)$.\n"
        f"Step 2: Equate the constant term: $(-1)(C) = {-C} \\implies C = {C}$.\n"
        f"Step 3: Equate the $x^2$ coefficient: $B - 1 = {B - 1} \\implies B = {B}$.\n"
        f"Thus the quadratic factor is $x^2 {'+' if B >= 0 else '-'} {abs(B)}x {'+' if C >= 0 else '-'} {abs(C)}$."
    )
    return _mcq_q(
        rng, f"g12_fn_35_{rng.randint(100000, 999999)}", "35_cubic_factorisation_inspection_method",
        "Factorising Cubic Polynomial by Inspection", prompt, correct, distractors, sol,
        {"tier_1": "Multiply (x - 1)(x^2 + Bx + C) and match with the given cubic.",
         "tier_2": f"Constant term gives C = {C}. The x^2 term gives B = {B}.",
         "tier_3": correct},
        ["inspection_middle_term_sign_error"]
    )


def arch_36_cubic_factorisation_long_division(rng: random.Random) -> Dict[str, Any]:
    # Long division of P(x) by (x - 2)
    B = rng.choice([-3, 2, 4])
    C = rng.choice([-5, 3, 6])
    c_val = 2
    p = sp.expand((sp.Symbol("x") - c_val) * (sp.Symbol("x")**2 + B * sp.Symbol("x") + C))
    poly_str = sp.latex(p)
    quotient_str = f"x^2 {'+' if B >= 0 else '-'} {abs(B)}x {'+' if C >= 0 else '-'} {abs(C)}"
    prompt = (
        f"Divide the cubic polynomial\n"
        f"$$P(x) = {poly_str}$$\n"
        f"by $(x - {c_val})$ using algebraic long division.\n\n"
        f"State the quotient $Q(x)$ and confirm that the remainder is $0$."
    )
    ans = f"Q(x) = {quotient_str}, R = 0"
    sol = (
        f"Step 1: Set up algebraic long division with dividend ${poly_str}$ and divisor $(x - {c_val})$:\n"
        f"Divide $x^3$ by $x$ to get $x^2$.\n"
        f"Multiply and subtract to get the remainder degree 2 term.\n"
        f"Step 2: Complete successive divisions to obtain:\n"
        f"Quotient: $Q(x) = {quotient_str}$\n"
        f"Remainder: $R = 0$."
    )
    return _calc_q(
        rng, f"g12_fn_36_{rng.randint(100000, 999999)}", "36_cubic_factorisation_long_division",
        "Cubic Factorisation via Algebraic Long Division", prompt, ans, sol,
        {"tier_1": f"Divide leading terms: x^3 / x = x^2. Multiply back and subtract.",
         "tier_2": f"The quotient is {quotient_str} with zero remainder.",
         "tier_3": ans},
        ["algebraic_long_division_subtraction_sign_error"]
    )


def arch_37_cubic_factorisation_synthetic_division(rng: random.Random) -> Dict[str, Any]:
    # Synthetic division with root r = 2
    r_val = rng.choice([1, 2, 3])
    B = rng.choice([-4, -2, 3])
    C = rng.choice([-6, 2, 5])
    p = sp.expand((sp.Symbol("x") - r_val) * (sp.Symbol("x")**2 + B * sp.Symbol("x") + C))
    poly_str = sp.latex(p)
    coeffs = [int(p.coeff(sp.Symbol("x"), i)) for i in [3, 2, 1, 0]]
    prompt = (
        f"Given the cubic polynomial $P(x) = {poly_str}$ and known factor $(x - {r_val})$:\n\n"
        f"Use synthetic division with divisor root ${r_val}$ to determine the coefficients of the quotient quadratic."
    )
    correct = f"Quotient coefficients are (1; {B}; {C}), remainder 0"
    distractors = [
        f"Quotient coefficients are (1; {-B}; {C}), remainder 0",
        f"Quotient coefficients are (1; {B}; {-C}), remainder 0",
        f"Quotient coefficients are (2; {B}; {C}), remainder {r_val}",
    ]
    sol = (
        f"Step 1: Write the coefficients of $P(x)$: $[{coeffs[0]}, {coeffs[1]}, {coeffs[2]}, {coeffs[3]}]$.\n"
        f"Step 2: Synthetic division by root ${r_val}$:\n"
        f"Bring down 1.\n"
        f"Multiply by ${r_val}$ and add to ${coeffs[1]}$: gives ${B}$.\n"
        f"Multiply by ${r_val}$ and add to ${coeffs[2]}$: gives ${C}$.\n"
        f"Multiply by ${r_val}$ and add to ${coeffs[3]}$: gives $0$.\n"
        f"Step 3: The quotient is $x^2 {'+' if B >= 0 else '-'} {abs(B)}x {'+' if C >= 0 else '-'} {abs(C)}$."
    )
    return _mcq_q(
        rng, f"g12_fn_37_{rng.randint(100000, 999999)}", "37_cubic_factorisation_synthetic_division",
        "Synthetic Division for Cubic Factorisation", prompt, correct, distractors, sol,
        {"tier_1": f"Place {r_val} outside the synthetic division table with coefficients {coeffs}.",
         "tier_2": f"Bring down 1, multiply and add consecutively to get (1, {B}, {C}).",
         "tier_3": correct},
        ["synthetic_division_multiplication_addition_confusion"]
    )


def arch_38_full_factorisation_cubic_into_three_linear_factors(rng: random.Random) -> Dict[str, Any]:
    # (x - r1)(x - r2)(x - r3)
    r1 = rng.choice([1, 2])
    r2 = rng.choice([-3, -2, 3])
    r3 = rng.choice([-1, 4, 5])
    p = sp.expand((sp.Symbol("x") - r1) * (sp.Symbol("x") - r2) * (sp.Symbol("x") - r3))
    poly_str = sp.latex(p)
    f1 = f"(x {'-' if r1 > 0 else '+'} {abs(r1)})"
    f2 = f"(x {'-' if r2 > 0 else '+'} {abs(r2)})"
    f3 = f"(x {'-' if r3 > 0 else '+'} {abs(r3)})"
    correct = f"{f1}{f2}{f3}"
    distractors = [
        f"(x {'+' if r1 > 0 else '-'} {abs(r1)}){f2}{f3}",
        f"{f1}(x {'+' if r2 > 0 else '-'} {abs(r2)}){f3}",
        f"{f1}{f2}(x {'+' if r3 > 0 else '-'} {abs(r3)})",
    ]
    prompt = (
        f"Completely factorise the cubic polynomial into three linear factors:\n"
        f"$$P(x) = {poly_str}$$"
    )
    sol = (
        f"Step 1: Test factors to find first root: $P({r1}) = 0 \\implies {f1}$ is a factor.\n"
        f"Step 2: Divide $P(x)$ by ${f1}$ to find the quadratic factor.\n"
        f"Step 3: Factorise the resulting quadratic factor into ${f2}{f3}$.\n"
        f"Complete factorisation: $P(x) = {correct}$."
    )
    return _mcq_q(
        rng, f"g12_fn_38_{rng.randint(100000, 999999)}", "38_full_factorisation_cubic_into_three_linear_factors",
        "Complete Factorisation of Cubic into Three Linear Factors", prompt, correct, distractors, sol,
        {"tier_1": f"Find the first root x = {r1}, then factorise the remaining quadratic.",
         "tier_2": f"Linear factors correspond to roots {r1}, {r2}, and {r3}.",
         "tier_3": correct},
        ["sign_error_converting_roots_to_factors"]
    )


def arch_39_cubic_factorisation_with_repeated_root(rng: random.Random) -> Dict[str, Any]:
    # (x - r1)^2 * (x - r2)
    r1 = rng.choice([1, 2, 3])
    r2 = rng.choice([-3, -2, -1, 4])
    p = sp.expand(((sp.Symbol("x") - r1)**2) * (sp.Symbol("x") - r2))
    poly_str = sp.latex(p)
    f1_sq = f"(x {'-' if r1 > 0 else '+'} {abs(r1)})^2"
    f2 = f"(x {'-' if r2 > 0 else '+'} {abs(r2)})"
    correct = f"{f1_sq}{f2}"
    distractors = [
        f"(x {'+' if r1 > 0 else '-'} {abs(r1)})^2{f2}",
        f"{f1_sq}(x {'+' if r2 > 0 else '-'} {abs(r2)})",
        f"(x {'-' if r1 > 0 else '+'} {abs(r1)}){f2}^2",
    ]
    prompt = (
        f"Factorise completely the cubic polynomial having a repeated factor:\n"
        f"$$P(x) = {poly_str}$$"
    )
    sol = (
        f"Step 1: Test rational roots to find root $x = {r1}$ ($P({r1}) = 0$).\n"
        f"Step 2: Dividing by $(x - {r1})$ gives a perfect square quadratic.\n"
        f"Step 3: The complete factorisation is $P(x) = {correct}$."
    )
    return _mcq_q(
        rng, f"g12_fn_39_{rng.randint(100000, 999999)}", "39_cubic_factorisation_with_repeated_root",
        "Cubic Factorisation with Repeated Root", prompt, correct, distractors, sol,
        {"tier_1": f"Find first factor (x - {r1}), then factorise the remaining perfect square.",
         "tier_2": f"Repeated root is at x = {r1}, single root is at x = {r2}.",
         "tier_3": correct},
        ["failed_to_identify_repeated_linear_factor"]
    )


def arch_40_cubic_factorisation_irreducible_quadratic_factor(rng: random.Random) -> Dict[str, Any]:
    # (x - r1)(x^2 + 2x + 5) where Delta = 4 - 20 = -16 < 0
    r1 = rng.choice([1, 2, -1, -2])
    p = sp.expand((sp.Symbol("x") - r1) * (sp.Symbol("x")**2 + 2 * sp.Symbol("x") + 5))
    poly_str = sp.latex(p)
    f1 = f"(x {'-' if r1 > 0 else '+'} {abs(r1)})"
    correct = f"{f1}(x^2 + 2x + 5); quadratic factor has Delta = -16 < 0 (no further real factors)"
    distractors = [
        f"{f1}(x + 1)(x + 5)",
        f"{f1}(x - 1)(x - 5)",
        f"(x {'+' if r1 > 0 else '-'} {abs(r1)})(x^2 + 2x + 5)",
    ]
    prompt = (
        f"Factorise the cubic polynomial over the set of real numbers ($\\mathbb{{R}}$):\n"
        f"$$P(x) = {poly_str}$$\n\n"
        f"Show whether the quadratic factor can be factorised further over $\\mathbb{{R}}$."
    )
    sol = (
        f"Step 1: Since $P({r1}) = 0$, ${f1}$ is a factor.\n"
        f"Step 2: Division gives quadratic factor $(x^2 + 2x + 5)$.\n"
        f"Step 3: Check discriminant of quadratic: $\\Delta = b^2 - 4ac = (2)^2 - 4(1)(5) = 4 - 20 = -16 < 0$.\n"
        f"Because $\\Delta < 0$, the quadratic cannot be factorised into real linear factors.\n"
        f"Factorisation over $\\mathbb{{R}}$ is ${f1}(x^2 + 2x + 5)$."
    )
    return _mcq_q(
        rng, f"g12_fn_40_{rng.randint(100000, 999999)}", "40_cubic_factorisation_irreducible_quadratic_factor",
        "Cubic Factorisation with Irreducible Quadratic Factor", prompt, correct, distractors, sol,
        {"tier_1": "Calculate the discriminant Delta = b^2 - 4ac of the quadratic factor.",
         "tier_2": "If Delta < 0, the quadratic factor has no real roots and cannot be broken down further.",
         "tier_3": correct},
        ["attempted_real_factorisation_when_discriminant_negative"]
    )


def arch_41_solving_cubic_equation_three_distinct_roots(rng: random.Random) -> Dict[str, Any]:
    r1 = rng.choice([1, 2])
    r2 = rng.choice([-3, -2])
    r3 = rng.choice([3, 4])
    p = sp.expand((sp.Symbol("x") - r1) * (sp.Symbol("x") - r2) * (sp.Symbol("x") - r3))
    poly_str = sp.latex(p)
    roots = sorted([r1, r2, r3])
    roots_str = f"x = {roots[0]} or x = {roots[1]} or x = {roots[2]}"
    prompt = (
        f"Solve the cubic equation for $x$:\n"
        f"$${poly_str} = 0$$"
    )
    ans = roots_str
    sol = (
        f"Step 1: Test factors to find first root: $P({r1}) = 0 \\implies x = {r1}$.\n"
        f"Step 2: Divide $P(x)$ by $(x - {r1})$ to obtain quadratic factor.\n"
        f"Step 3: Factorise quadratic factor into $(x - {r2})(x - {r3}) = 0$.\n"
        f"Step 4: All real solutions: {roots_str}."
    )
    return _calc_q(
        rng, f"g12_fn_41_{rng.randint(100000, 999999)}", "41_solving_cubic_equation_three_distinct_roots",
        "Solving Cubic Equation with Three Real Roots", prompt, ans, sol,
        {"tier_1": f"Find first root x = {r1} by trial, then solve the remaining quadratic equation.",
         "tier_2": f"The roots are {roots_str}.",
         "tier_3": ans},
        ["forgot_to_state_all_three_roots"]
    )


def arch_42_solving_cubic_equation_common_factor_first(rng: random.Random) -> Dict[str, Any]:
    # x*(x^2 - 5x + 6) = 0 => x*(x - 2)(x - 3) = 0
    r1 = rng.choice([2, 3])
    r2 = rng.choice([4, 5])
    b = -(r1 + r2)
    c = r1 * r2
    poly_str = f"x^3 {'+' if b >= 0 else '-'} {abs(b)}x^2 + {c}x"
    prompt = (
        f"Solve for $x$:\n"
        f"$${poly_str} = 0$$"
    )
    ans = f"x = 0 or x = {r1} or x = {r2}"
    sol = (
        f"Step 1: Take out common factor $x$:\n"
        f"$$x(x^2 {'+' if b >= 0 else '-'} {abs(b)}x + {c}) = 0$$\n"
        f"Step 2: Factorise the quadratic trinomial:\n"
        f"$$x(x - {r1})(x - {r2}) = 0$$\n"
        f"Step 3: Roots: $x = 0$ or $x = {r1}$ or $x = {r2}$."
    )
    return _calc_q(
        rng, f"g12_fn_42_{rng.randint(100000, 999999)}", "42_solving_cubic_equation_common_factor_first",
        "Solving Cubic Equation with Common Factor x", prompt, ans, sol,
        {"tier_1": "Never divide through by x and lose a root! Factorise out x first.",
         "tier_2": f"Roots are x = 0, x = {r1}, and x = {r2}.",
         "tier_3": ans},
        ["divided_by_x_losing_root_zero"]
    )


def arch_43_solving_cubic_equation_repeated_root(rng: random.Random) -> Dict[str, Any]:
    r1 = rng.choice([1, 3])
    r2 = rng.choice([-4, -2, 5])
    p = sp.expand(((sp.Symbol("x") - r1)**2) * (sp.Symbol("x") - r2))
    poly_str = sp.latex(p)
    prompt = (
        f"Solve the cubic equation and describe the multiplicity of its roots:\n"
        f"$${poly_str} = 0$$"
    )
    correct = f"x = {r1} (repeated root, multiplicity 2) or x = {r2} (single root)"
    distractors = [
        f"x = {r1} or x = {r2} (both single roots)",
        f"x = {-r1} (multiplicity 2) or x = {-r2}",
        f"x = {r1} only",
    ]
    sol = (
        f"Step 1: Factorise the cubic: $(x - {r1})^2(x - {r2}) = 0$.\n"
        f"Step 2: Setting factors to zero yields:\n"
        f"$x = {r1}$ twice (a turning point tangent to the x-axis) and $x = {r2}$ (crosses the x-axis)."
    )
    return _mcq_q(
        rng, f"g12_fn_43_{rng.randint(100000, 999999)}", "43_solving_cubic_equation_repeated_root",
        "Cubic Equation with Repeated Root and Multiplicity", prompt, correct, distractors, sol,
        {"tier_1": "A squared linear factor indicates a repeated root (tangency to the horizontal axis).",
         "tier_2": f"Root x = {r1} has multiplicity 2; root x = {r2} has multiplicity 1.",
         "tier_3": correct},
        ["failed_to_distinguish_root_multiplicity"]
    )


def arch_44_cubic_x_intercepts_from_factorisation(rng: random.Random) -> Dict[str, Any]:
    r1 = rng.choice([1, 2])
    r2 = rng.choice([-2, -1])
    r3 = rng.choice([3, 4])
    p = sp.expand((sp.Symbol("x") - r1) * (sp.Symbol("x") - r2) * (sp.Symbol("x") - r3))
    poly_str = sp.latex(p)
    y_int = int(p.subs(sp.Symbol("x"), 0))
    prompt = (
        f"For the cubic function $f(x) = {poly_str}$:\n\n"
        f"1. Determine the coordinates of all three $x$-intercepts.\n"
        f"2. State the coordinates of the $y$-intercept."
    )
    correct = f"x-intercepts: ({r1}; 0), ({r2}; 0), ({r3}; 0); y-intercept: (0; {y_int})"
    distractors = [
        f"x-intercepts: ({-r1}; 0), ({-r2}; 0), ({-r3}; 0); y-intercept: (0; {y_int})",
        f"x-intercepts: ({r1}; 0), ({r2}; 0), ({r3}; 0); y-intercept: ({y_int}; 0)",
        f"x-intercepts: ({r1}; {y_int}), ({r2}; {y_int}), ({r3}; {y_int})",
    ]
    sol = (
        f"Step 1: For $x$-intercepts, set $f(x) = 0$:\n"
        f"$$(x - {r1})(x - {r2})(x - {r3}) = 0 \\implies x = {r1},\\ x = {r2},\\ x = {r3}$$\n"
        f"Coordinates: $({r1};\\ 0), ({r2};\\ 0), ({r3};\\ 0)$.\n"
        f"Step 2: For $y$-intercept, set $x = 0$:\n"
        f"$$f(0) = {y_int} \\implies (0;\\ {y_int})$$."
    )
    return _mcq_q(
        rng, f"g12_fn_44_{rng.randint(100000, 999999)}", "44_cubic_x_intercepts_from_factorisation",
        "Determining Cubic Intercepts from Factorised Form", prompt, correct, distractors, sol,
        {"tier_1": "Set y = 0 for x-intercepts, and x = 0 for the y-intercept.",
         "tier_2": f"x-intercepts are at x = {r1}, {r2}, {r3}. y-intercept is {y_int}.",
         "tier_3": correct},
        ["inverted_coordinates_of_intercepts"]
    )


def arch_45_cubic_polynomial_sign_analysis_inequality(rng: random.Random) -> Dict[str, Any]:
    r1, r2, r3 = rng.choice([(-2, 1, 4), (-3, 1, 3), (-4, 2, 5)])
    p = sp.expand((sp.Symbol("x") - r1) * (sp.Symbol("x") - r2) * (sp.Symbol("x") - r3))
    poly_str = sp.latex(p)
    f1 = f"(x {'+' if r1 < 0 else '-'} {abs(r1)})"
    f2 = f"(x {'+' if r2 < 0 else '-'} {abs(r2)})"
    f3 = f"(x {'+' if r3 < 0 else '-'} {abs(r3)})"
    prompt = (
        f"Solve the cubic inequality for $x$:\n"
        f"$${poly_str} > 0$$\n\n"
        f"(Given factorised form is ${f1}{f2}{f3} > 0$)."
    )
    correct = f"{r1} < x < {r2} or x > {r3}"
    distractors = [
        f"x < {r1} or {r2} < x < {r3}",
        f"{r1} <= x <= {r2} or x >= {r3}",
        f"x > {r3} only",
    ]
    sol = (
        f"Step 1: Critical values where expression is zero are $x = {r1}, {r2}, {r3}$.\n"
        f"Step 2: Sign analysis across intervals:\n"
        f"For $x < {r1}$: $(-)(-)(-) = -$\n"
        f"For ${r1} < x < {r2}$: $(+)(-)(-) = +$\n"
        f"For ${r2} < x < {r3}$: $(+)(+)(-) = -$\n"
        f"For $x > {r3}$: $(+)(+)(+) = +$\n"
        f"Step 3: Inequality requires $> 0$ (positive), so solutions are ${r1} < x < {r2}$ or $x > {r3}$."
    )
    return _mcq_q(
        rng, f"g12_fn_45_{rng.randint(100000, 999999)}", "45_cubic_polynomial_sign_analysis_inequality",
        "Solving Cubic Inequalities via Sign Analysis", prompt, correct, distractors, sol,
        {"tier_1": "Plot the critical values on a number line and test the sign of each interval.",
         "tier_2": "The cubic is positive between -2 and 1, and for x > 4.",
         "tier_3": correct},
        ["confused_positive_and_negative_sign_regions"]
    )


def arch_46_polynomial_word_problem_box_volume(rng: random.Random) -> Dict[str, Any]:
    L = rng.choice([20, 24, 30])
    W = rng.choice([12, 16, 18])
    # Box dimensions: height x, length L - 2x, width W - 2x
    # V(x) = x(L - 2x)(W - 2x) = x(4x^2 - 2(L + W)x + L*W) = 4x^3 - 2(L + W)x^2 + L*W*x
    coeff3 = 4
    coeff2 = -2 * (L + W)
    coeff1 = L * W
    poly_str = f"{coeff3}x^3 {coeff2}x^2 + {coeff1}x"
    max_x = W // 2
    prompt = (
        f"An open rectangular storage box is fabricated by cutting congruent squares of side length $x\\text{{ cm}}$ "
        f"from each corner of a rectangular sheet of metal measuring ${L}\\text{{ cm}}$ by ${W}\\text{{ cm}}$, "
        f"and then folding up the sides.\n\n"
        f"1. Express the volume $V(x)$ of the box as a cubic polynomial in standard form.\n"
        f"2. State the practical physical domain for $x$."
    )
    correct = f"V(x) = {poly_str}; practical domain is 0 < x < {max_x}"
    distractors = [
        f"V(x) = {coeff3}x^3 + {abs(coeff2)}x^2 + {coeff1}x; domain is 0 < x < {L // 2}",
        f"V(x) = 2x^3 {coeff2 // 2}x^2 + {coeff1}x; domain is x > 0",
        f"V(x) = {poly_str}; practical domain is x in R",
    ]
    sol = (
        f"Step 1: Length $= {L} - 2x$, Width $= {W} - 2x$, Height $= x$.\n"
        f"Step 2: Volume $V(x) = x({L} - 2x)({W} - 2x)$:\n"
        f"$$V(x) = x(4x^2 - {2 * (L + W)}x + {L * W}) = {poly_str}$$\n"
        f"Step 3: Physical constraints: dimensions must be strictly positive:\n"
        f"$x > 0$ and ${W} - 2x > 0 \\implies x < \\frac{{{W}}}{{2}} = {max_x}$.\n"
        f"Practical domain: $0 < x < {max_x}$."
    )
    return _mcq_q(
        rng, f"g12_fn_46_{rng.randint(100000, 999999)}", "46_polynomial_word_problem_box_volume",
        "Applied Cubic Polynomial - Box Volume and Practical Domain", prompt, correct, distractors, sol,
        {"tier_1": "Multiply length (L - 2x), width (W - 2x), and height x.",
         "tier_2": f"Physical width {W} - 2x > 0 limits x to 0 < x < {max_x}.",
         "tier_3": correct},
        ["omitted_practical_domain_restriction_for_physical_dimensions"]
    )


def arch_47_functions_and_inverses_composition_identity(rng: random.Random) -> Dict[str, Any]:
    b = rng.choice([2, 3, 5])
    prompt = (
        f"Let $f(x) = {b}^x$ and $f^{{-1}}(x) = \\log_{{{b}}}(x)$ for $x > 0$.\n\n"
        f"Evaluate the composite expressions $f(f^{{-1}}(x))$ and $f^{{-1}}(f(x))$, "
        f"and state the fundamental mathematical property demonstrated."
    )
    correct = "f(f^-1(x)) = x and f^-1(f(x)) = x; inverse functions undo each other, yielding the identity function"
    distractors = [
        "f(f^-1(x)) = 1 and f^-1(f(x)) = 1; composition yields unity",
        "f(f^-1(x)) = 0 and f^-1(f(x)) = 0; cancellation yields zero",
        f"f(f^-1(x)) = {b}x and f^-1(f(x)) = x / {b}",
    ]
    sol = (
        f"Step 1: $f(f^{{-1}}(x)) = {b}^{{\\log_{{{b}}}(x)}} = x$ for all $x > 0$.\n"
        f"Step 2: $f^{{-1}}(f(x)) = \\log_{{{b}}}({b}^x) = x \\log_{{{b}}}({b}) = x$ for all $x \\in \\mathbb{{R}}$.\n"
        f"Step 3: This confirms that a function and its inverse compose to produce the identity function $I(x) = x$."
    )
    return _mcq_q(
        rng, f"g12_fn_47_{rng.randint(100000, 999999)}", "47_functions_and_inverses_composition_identity",
        "Composite Inverse Functions and Identity Property", prompt, correct, distractors, sol,
        {"tier_1": "Substitute log into the exponential: b^(log_b(x)) = x.",
         "tier_2": "The composition of any function with its inverse returns the original input x.",
         "tier_3": correct},
        ["confused_inverse_composition_with_reciprocal_product"]
    )


def arch_48_intersection_function_and_inverse_on_y_equals_x(rng: random.Random) -> Dict[str, Any]:
    # f(x) = x^2 - 2 for x >= 0
    # Intersects f^-1 on y = x => x^2 - 2 = x => x^2 - x - 2 = 0 => (x - 2)(x + 1) = 0
    # Since x >= 0, x = 2 => point is (2, 2)
    k_shift = rng.choice([2, 6, 12])
    # x^2 - x - k_shift = 0
    # if k_shift = 2: (x - 2)(x + 1) => x = 2
    # if k_shift = 6: (x - 3)(x + 2) => x = 3
    # if k_shift = 12: (x - 4)(x + 3) => x = 4
    x_root = int((1 + math.sqrt(1 + 4 * k_shift)) / 2)
    prompt = (
        f"Given $f(x) = x^2 - {k_shift}$ for $x \\ge 0$ and its inverse $f^{{-1}}(x) = \\sqrt{{x + {k_shift}}}$:\n\n"
        f"Calculate the coordinates of the point of intersection between $f(x)$ and $f^{{-1}}(x)$."
    )
    ans = f"({x_root}; {x_root})"
    sol = (
        f"Step 1: A function and its inverse intersect on the line of symmetry $y = x$.\n"
        f"Therefore, setting $f(x) = x$ is equivalent to equating $f(x) = f^{{-1}}(x)$:\n"
        f"$$x^2 - {k_shift} = x$$\n"
        f"$$x^2 - x - {k_shift} = 0$$\n"
        f"Step 2: Factorise: $(x - {x_root})(x + {x_root - 1}) = 0$.\n"
        f"Since the domain requires $x \\ge 0$, we select $x = {x_root}$.\n"
        f"Step 3: Because the point lies on $y = x$, $y = {x_root}$.\n"
        f"Intersection point: $({x_root};\\ {x_root})$."
    )
    return _calc_q(
        rng, f"g12_fn_48_{rng.randint(100000, 999999)}", "48_intersection_function_and_inverse_on_y_equals_x",
        "Finding Intersection of Function and Inverse on y = x", prompt, ans, sol,
        {"tier_1": "Instead of solving f(x) = f^-1(x) with radicals, simply equate f(x) = x.",
         "tier_2": f"Solve x^2 - x - {k_shift} = 0 for x >= 0.",
         "tier_3": f"Point = ({x_root}; {x_root})."},
        ["attempted_cumbersome_radical_equation_instead_of_y_equals_x"]
    )


def arch_49_cubic_roots_graphical_relationship_svg(rng: random.Random) -> Dict[str, Any]:
    case = rng.choice([1, 2])
    intro_txt = rng.choice([
        "The visual display presents the graph of cubic polynomial",
        "Consider the plotted cubic polynomial curve",
        "Examine the coordinate diagram for the cubic function",
    ])
    if case == 1:
        # P(x) = (x + 2)(x - 1)(x - 3) = x^3 - 2x^2 - 5x + 6, y_int = 6
        p_str = "(x + 2)(x - 1)(x - 3)"
        r1, r2, r3 = -2, 1, 3
        y_int = 6
        p1_x, p2_x, p3_x = 100, 190, 270
        y_cy = 90
        correct = "x-intercepts are (-2; 0), (1; 0), (3; 0); y-intercept is (0; 6); f(x) <= 0 for x <= -2 or 1 <= x <= 3"
        distractors = [
            "x-intercepts are (2; 0), (-1; 0), (-3; 0); y-intercept is (0; -6); f(x) <= 0 for -2 <= x <= 1",
            "x-intercepts are (-2; 0), (1; 0), (3; 0); y-intercept is (6; 0); f(x) <= 0 for x >= 3",
            "f(x) <= 0 everywhere",
        ]
        sol_ineq = "x \\le -2 \\text{ or } 1 \\le x \\le 3"
    else:
        # P(x) = (x + 3)(x - 1)(x - 2) = x^3 - 7x + 6, y_int = 6
        p_str = "(x + 3)(x - 1)(x - 2)"
        r1, r2, r3 = -3, 1, 2
        y_int = 6
        p1_x, p2_x, p3_x = 80, 190, 240
        y_cy = 85
        correct = "x-intercepts are (-3; 0), (1; 0), (2; 0); y-intercept is (0; 6); f(x) <= 0 for x <= -3 or 1 <= x <= 2"
        distractors = [
            "x-intercepts are (3; 0), (-1; 0), (-2; 0); y-intercept is (0; -6); f(x) <= 0 for -3 <= x <= 1",
            "x-intercepts are (-3; 0), (1; 0), (2; 0); y-intercept is (6; 0); f(x) <= 0 for x >= 2",
            "f(x) <= 0 everywhere",
        ]
        sol_ineq = "x \\le -3 \\text{ or } 1 \\le x \\le 2"

    ref_tag = rng.randint(10, 99)
    stroke_col = rng.choice(["#2563eb", "#1d4ed8", "#3b82f6"])
    svg_body = (
        f'<line x1="40" y1="130" x2="360" y2="130" stroke="#94a3b8" stroke-width="1.5"/>'
        f'<line x1="160" y1="20" x2="160" y2="230" stroke="#94a3b8" stroke-width="1.5"/>'
        f'<path d="M 60,220 C 80,40 140,50 160,110 C 180,170 230,190 320,40" fill="none" stroke="{stroke_col}" stroke-width="2.5"/>'
        f'<circle cx="{p1_x}" cy="130" r="4" fill="#dc2626"/><text x="{p1_x - 5}" y="148" font-size="10" fill="#dc2626">({r1}; 0)</text>'
        f'<circle cx="160" cy="{y_cy}" r="4" fill="#16a34a"/><text x="165" y="{y_cy}" font-size="10" fill="#16a34a">(0; {y_int})</text>'
        f'<circle cx="{p2_x}" cy="130" r="4" fill="#dc2626"/><text x="{p2_x - 5}" y="148" font-size="10" fill="#dc2626">({r2}; 0)</text>'
        f'<circle cx="{p3_x}" cy="130" r="4" fill="#dc2626"/><text x="{p3_x - 5}" y="148" font-size="10" fill="#dc2626">({r3}; 0)</text>'
        f'<text x="260" y="30" font-size="11" font-weight="bold" fill="{stroke_col}">y = {p_str} [Ref #{ref_tag}]</text>'
    )
    prompt = (
        f"{intro_txt} $f(x) = {p_str}$.\n\n"
        f"1. Identify the $x$-intercepts and $y$-intercept shown on the graph.\n"
        f"2. For which values of $x$ is $f(x) \\le 0$?"
    )
    sol = (
        f"Step 1: Intercepts from factors:\n"
        f"$x$-intercepts: $({r1};\\ 0), ({r2};\\ 0), ({r3};\\ 0)$.\n"
        f"$y$-intercept: $f(0) = {y_int} \\implies (0;\\ {y_int})$.\n"
        f"Step 2: From the graph, the curve lies below or on the x-axis ($f(x) \\le 0$) when ${sol_ineq}$."
    )
    return _mcq_q(
        rng, f"g12_fn_49_{rng.randint(100000, 999999)}", "49_cubic_roots_graphical_relationship_svg",
        "Graphical Intercepts and Inequality Regions of Cubic", prompt, correct, distractors, sol,
        {"tier_1": "Look at the points where the curve crosses the horizontal axis and lies below it.",
         "tier_2": f"The curve is below the axis for x <= {r1} and between {r2} and {r3}.",
         "tier_3": correct},
        ["confused_regions_above_and_below_x_axis"],
        diagram_spec=_svg_spec(svg_body, 580, 240)
    )


def arch_50_compound_nsc_exam_functions_and_polynomials(rng: random.Random) -> Dict[str, Any]:
    b_val = rng.choice([2, 3])
    pow_val = rng.choice([2, 3])
    arg_val = b_val ** pow_val
    prompt = (
        f"**Examination Level 4 Challenge:**\n\n"
        f"1. Given the cubic polynomial $f(x) = x^3 - 2x^2 - 9x + 18$:\n"
        f"   a) Show that $(x - 2)$ is a factor of $f(x)$.\n"
        f"   b) Hence, completely factorise $f(x)$.\n\n"
        f"2. Given the exponential function $g(x) = {b_val}^x$:\n"
        f"   a) Write down the equation of the inverse $g^{{-1}}(x)$.\n"
        f"   b) Calculate the value of $g^{{-1}}({arg_val})$."
    )
    correct = f"f(x) = (x - 2)(x - 3)(x + 3); g^-1(x) = log_{{{b_val}}}(x); g^-1({arg_val}) = {pow_val}"
    distractors = [
        f"f(x) = (x - 2)(x^2 + 9); g^-1(x) = {b_val}^-x; g^-1({arg_val}) = 1",
        f"f(x) = (x + 2)(x - 3)(x + 3); g^-1(x) = log_{{{b_val}}}(x); g^-1({arg_val}) = {pow_val + 1}",
        f"f(x) = (x - 2)(x - 3)(x + 3); g^-1(x) = log_10(x); g^-1({arg_val}) = {pow_val}",
    ]
    sol = (
        f"Step 1: Part 1a:\n"
        f"$f(2) = (2)^3 - 2(2)^2 - 9(2) + 18 = 8 - 8 - 18 + 18 = 0 \\implies (x - 2)$ is a factor.\n"
        f"Step 2: Part 1b:\n"
        f"$f(x) = (x - 2)(x^2 - 9) = (x - 2)(x - 3)(x + 3)$.\n"
        f"Step 3: Part 2a:\n"
        f"Inverse of $g(x) = {b_val}^x$ is $g^{{-1}}(x) = \\log_{{{b_val}}}(x)$.\n"
        f"Step 4: Part 2b:\n"
        f"$g^{{-1}}({arg_val}) = \\log_{{{b_val}}}({arg_val}) = {pow_val}$ (since ${b_val}^{{{pow_val}}} = {arg_val}$)."
    )
    return _mcq_q(
        rng, f"g12_fn_50_{rng.randint(100000, 999999)}", "50_compound_nsc_exam_functions_and_polynomials",
        "Compound Examination Functions and Polynomials Problem", prompt, correct, distractors, sol,
        {"tier_1": "Test f(2) = 0, factorise x^2 - 9 into (x-3)(x+3), and evaluate log_2(8).",
         "tier_2": "x^2 - 9 is a difference of two squares: (x - 3)(x + 3). log_2(8) = 3.",
         "tier_3": correct},
        ["factorised_difference_of_squares_incorrectly"]
    )


BUILDERS_26_50: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    "26_polynomial_identification_and_degree": arch_26_polynomial_identification_and_degree,
    "27_polynomial_evaluation_function_notation": arch_27_polynomial_evaluation_function_notation,
    "28_remainder_theorem_linear_divisor": arch_28_remainder_theorem_linear_divisor,
    "29_remainder_theorem_fractional_divisor": arch_29_remainder_theorem_fractional_divisor,
    "30_remainder_theorem_solve_single_unknown_k": arch_30_remainder_theorem_solve_single_unknown_k,
    "31_remainder_theorem_solve_simultaneous_two_unknowns": arch_31_remainder_theorem_solve_simultaneous_two_unknowns,
    "32_factor_theorem_verification": arch_32_factor_theorem_verification,
    "33_factor_theorem_solve_unknown_coefficient": arch_33_factor_theorem_solve_unknown_coefficient,
    "34_finding_first_rational_root_by_trial": arch_34_finding_first_rational_root_by_trial,
    "35_cubic_factorisation_inspection_method": arch_35_cubic_factorisation_inspection_method,
    "36_cubic_factorisation_long_division": arch_36_cubic_factorisation_long_division,
    "37_cubic_factorisation_synthetic_division": arch_37_cubic_factorisation_synthetic_division,
    "38_full_factorisation_cubic_into_three_linear_factors": arch_38_full_factorisation_cubic_into_three_linear_factors,
    "39_cubic_factorisation_with_repeated_root": arch_39_cubic_factorisation_with_repeated_root,
    "40_cubic_factorisation_irreducible_quadratic_factor": arch_40_cubic_factorisation_irreducible_quadratic_factor,
    "41_solving_cubic_equation_three_distinct_roots": arch_41_solving_cubic_equation_three_distinct_roots,
    "42_solving_cubic_equation_common_factor_first": arch_42_solving_cubic_equation_common_factor_first,
    "43_solving_cubic_equation_repeated_root": arch_43_solving_cubic_equation_repeated_root,
    "44_cubic_x_intercepts_from_factorisation": arch_44_cubic_x_intercepts_from_factorisation,
    "45_cubic_polynomial_sign_analysis_inequality": arch_45_cubic_polynomial_sign_analysis_inequality,
    "46_polynomial_word_problem_box_volume": arch_46_polynomial_word_problem_box_volume,
    "47_functions_and_inverses_composition_identity": arch_47_functions_and_inverses_composition_identity,
    "48_intersection_function_and_inverse_on_y_equals_x": arch_48_intersection_function_and_inverse_on_y_equals_x,
    "49_cubic_roots_graphical_relationship_svg": arch_49_cubic_roots_graphical_relationship_svg,
    "50_compound_nsc_exam_functions_and_polynomials": arch_50_compound_nsc_exam_functions_and_polynomials,
}
