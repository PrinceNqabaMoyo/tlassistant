"""Grade 12 Mathematics - Sequences and Series Archetypes 26 to 50.
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/Mathematics_Gr12/Term 1/01. Sequences and series.md.
"""
from __future__ import annotations

import math
import random
from typing import Any, Callable, Dict, List, Optional
import sympy as sp

from .sequences_series_archetypes_01_25 import _mcq_q, _calc_q, _svg_spec


# =========================================================================== #
# Archetypes 26 - 50
# =========================================================================== #

def arch_26_geometric_series_sum_formula_basic(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([2, 3, 4, 5])
    r = rng.choice([2, 3])
    n = rng.choice([6, 7, 8])
    sn = a * (r**n - 1) // (r - 1)
    t1, t2, t3 = a, a * r, a * r**2
    prompt = (
        f"Calculate the sum of the first ${n}$ terms of the geometric series:\n"
        f"$${t1} + {t2} + {t3} + \\dots$$"
    )
    ans = str(sn)
    sol = (
        f"Step 1: Parameters: $a = {a}$, $r = \\frac{{{t2}}}{{{t1}}} = {r}$, and $n = {n}$.\n"
        f"Step 2: Apply the geometric sum formula for $r > 1$:\n"
        f"$$S_n = \\frac{{a(r^n - 1)}}{{r - 1}}$$\n"
        f"$$S_{{{n}}} = \\frac{{{a}({r}^{{{n}}} - 1)}}{{{r} - 1}} = \\frac{{{a}({r**n} - 1)}}{{{r - 1}}} = \\frac{{{a}({r**n - 1})}}{{{r - 1}}} = {sn}$$."
    )
    return _calc_q(
        rng, f"g12_seq_26_{rng.randint(100000, 999999)}", "26_geometric_series_sum_formula_basic",
        "Sum of a Finite Geometric Series", prompt, ans, sol,
        {"tier_1": "Use the geometric sum formula Sn = a(r^n - 1) / (r - 1).",
         "tier_2": f"Here a = {a}, r = {r}, and n = {n}. Compute {r}^{{{n}}} first.",
         "tier_3": f"S_{{{n}}} = {sn}."},
        ["geometric_sum_formula_substitution_error"]
    )


def arch_27_geometric_series_solve_for_n_log(rng: random.Random) -> Dict[str, Any]:
    # Sn = a*(r^n - 1) / (r - 1) = target
    # r^n - 1 = target*(r - 1)/a  =>  r^n = target*(r - 1)/a + 1
    a = rng.choice([3, 4, 6])
    r = rng.choice([2, 3])
    n = rng.choice([6, 7, 8])
    target = a * (r**n - 1) // (r - 1)
    prompt = (
        f"The sum of the first $n$ terms of the geometric sequence with $a = {a}$ and $r = {r}$ is ${target}$.\n\n"
        f"Determine the number of terms $n$."
    )
    ans = f"n = {n}"
    sol = (
        f"Step 1: Set up $S_n = \\frac{{a(r^n - 1)}}{{r - 1}} = {target}$:\n"
        f"$$\\frac{{{a}({r}^n - 1)}}{{{r} - 1}} = {target}$$\n"
        f"$$({r}^n - 1) = \\frac{{{target} \\times ({r - 1})}}{{{a}}} = {(target * (r - 1)) // a}$$\n"
        f"$${r}^n = {(target * (r - 1)) // a + 1} = {r}^{{{n}}}$$\n"
        f"Step 2: Equate exponents (or take logarithms):\n"
        f"$$n = {n}$$."
    )
    return _calc_q(
        rng, f"g12_seq_27_{rng.randint(100000, 999999)}", "27_geometric_series_solve_for_n_log",
        "Solving for Number of Terms in Geometric Series", prompt, ans, sol,
        {"tier_1": "Substitute into Sn = a(r^n - 1) / (r - 1) and isolate r^n.",
         "tier_2": f"r^n = {r**n}. Use log base {r} or equate bases.",
         "tier_3": f"n = {n}."},
        ["forgot_to_isolate_exponential_term_before_log"]
    )


def arch_28_sum_to_infinity_condition_for_convergence(rng: random.Random) -> Dict[str, Any]:
    # Series: (2x - 1) + (2x - 1)^2 + (2x - 1)^3 ...
    # r = 2x - 1. -1 < 2x - 1 < 1  => 0 < 2x < 2 => 0 < x < 1
    # Parameterize r = mx + k
    m = rng.choice([2, 3, 4])
    k = rng.choice([-3, -1, 1, 2])
    # -1 < mx + k < 1  =>  -1 - k < mx < 1 - k
    lo_num = -1 - k
    hi_num = 1 - k
    # Format fractions or numbers
    def fmt_bound(num_val: int, den_val: int) -> str:
        g = math.gcd(abs(num_val), den_val)
        nv, dv = num_val // g, den_val // g
        if dv == 1:
            return str(nv)
        return f"{nv}/{dv}"

    lo_str = fmt_bound(lo_num, m)
    hi_str = fmt_bound(hi_num, m)
    correct_range = f"{lo_str} < x < {hi_str}"

    expr_r = f"{m}x {'+' if k >= 0 else '-'} {abs(k)}"
    prompt = (
        f"Given the infinite geometric series:\n"
        f"$$1 + ({expr_r}) + ({expr_r})^2 + ({expr_r})^3 + \\dots$$\n\n"
        f"Determine the values of $x$ for which this series converges."
    )
    correct = correct_range
    distractors = [
        f"x > {hi_str}",
        f"x < {lo_str}",
        f"{lo_str} <= x <= {hi_str}",
    ]
    sol = (
        f"Step 1: An infinite geometric series converges if and only if $-1 < r < 1$.\n"
        f"Step 2: Here the common ratio is $r = {expr_r}$. Set up the double inequality:\n"
        f"$$-1 < {expr_r} < 1$$\n"
        f"Subtract ${k}$ from all parts:\n"
        f"$${lo_num} < {m}x < {hi_num}$$\n"
        f"Divide by ${m}$:\n"
        f"$${correct_range}$$."
    )
    return _mcq_q(
        rng, f"g12_seq_28_{rng.randint(100000, 999999)}", "28_sum_to_infinity_condition_for_convergence",
        "Condition for Convergence of an Infinite Geometric Series", prompt, correct, distractors, sol,
        {"tier_1": "A geometric series converges when -1 < r < 1.",
         "tier_2": f"Set -1 < {expr_r} < 1 and solve for x.",
         "tier_3": correct},
        ["convergence_included_endpoints_violating_strict_inequality"]
    )


def arch_29_sum_to_infinity_calculation(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([12, 16, 24, 36, 48])
    # r = 1/2, 1/3, 1/4, 2/3, 3/4
    r_frac = rng.choice([(1, 2), (1, 3), (1, 4), (2, 3), (3, 4)])
    num_r, den_r = r_frac
    # S_inf = a / (1 - num_r/den_r) = a * den_r / (den_r - num_r)
    s_inf = (a * den_r) // (den_r - num_r)
    # terms
    t1 = a
    t2 = (a * num_r) // den_r
    t3 = (t2 * num_r) // den_r
    prompt = (
        f"Evaluate the sum to infinity ($S_\\infty$) of the convergent geometric series:\n"
        f"$${t1} + {t2} + {t3} + \\dots$$"
    )
    ans = str(s_inf)
    sol = (
        f"Step 1: First term $a = {t1}$.\n"
        f"Step 2: Common ratio $r = \\frac{{{t2}}}{{{t1}}} = \\frac{{{num_r}}}{{{den_r}}}$.\n"
        f"Since $|r| = \\frac{{{num_r}}}{{{den_r}}} < 1$, the series converges.\n"
        f"Step 3: Apply the sum to infinity formula:\n"
        f"$$S_\\infty = \\frac{{a}}{{1 - r}} = \\frac{{{a}}}{{1 - \\frac{{{num_r}}}{{{den_r}}}}} = \\frac{{{a}}}{{\\frac{{{den_r - num_r}}}{{{den_r}}}}} = \\frac{{{a} \\times {den_r}}}{{{den_r - num_r}}} = {s_inf}$$."
    )
    return _calc_q(
        rng, f"g12_seq_29_{rng.randint(100000, 999999)}", "29_sum_to_infinity_calculation",
        "Calculating Sum to Infinity of a Geometric Series", prompt, ans, sol,
        {"tier_1": "Use the formula S_infinity = a / (1 - r).",
         "tier_2": f"Here a = {a} and r = {num_r}/{den_r}. Simplify the denominator 1 - r.",
         "tier_3": f"S_infinity = {s_inf}."},
        ["fractional_denominator_division_error"]
    )


def arch_30_recurring_decimal_to_fraction_geometric(rng: random.Random) -> Dict[str, Any]:
    # e.g. 0.454545... = 45/100 + 45/10000 + ...
    # a = val/100, r = 1/100, S_inf = (val/100) / (99/100) = val/99
    val = rng.choice([27, 36, 45, 54, 63, 72, 81])
    g = math.gcd(val, 99)
    num_f = val // g
    den_f = 99 // g
    prompt = (
        f"Use an infinite geometric series to convert the recurring decimal $0{{,}}363636\\dots$ ($0{{,}}\\dot{{{val // 10}}}\\dot{{{val % 10}}}$) "
        f"into a simplified common fraction."
    )
    correct = f"{num_f}/{den_f}"
    distractors = [
        f"{val}/100",
        f"{val}/90",
        f"{num_f}/{den_f + 1}",
    ]
    sol = (
        f"Step 1: Write as an infinite geometric series:\n"
        f"$$0{{,}}\\dot{{{val // 10}}}\\dot{{{val % 10}}} = \\frac{{{val}}}{{100}} + \\frac{{{val}}}{{10000}} + \\frac{{{val}}}{{1000000}} + \\dots$$\n"
        f"Step 2: Identify parameters: $a = \\frac{{{val}}}{{100}}$ and $r = \\frac{{1}}{{100}}$.\n"
        f"Step 3: Apply $S_\\infty = \\frac{{a}}{{1 - r}}$:\n"
        f"$$S_\\infty = \\frac{{\\frac{{{val}}}{{100}}}}{{1 - \\frac{{1}}{{100}}}} = \\frac{{\\frac{{{val}}}{{100}}}}{{\\frac{{99}}{{100}}}} = \\frac{{{val}}}{{99}} = \\frac{{{num_f}}}{{{den_f}}}$$."
    )
    return _mcq_q(
        rng, f"g12_seq_30_{rng.randint(100000, 999999)}", "30_recurring_decimal_to_fraction_geometric",
        "Converting Recurring Decimal to Fraction via Geometric Series", prompt, correct, distractors, sol,
        {"tier_1": f"Express 0.{val}{val}... as {val}/100 + {val}/10000 + ...",
         "tier_2": f"Here a = {val}/100 and r = 1/100. Evaluate a / (1 - r).",
         "tier_3": correct},
        ["divided_by_100_instead_of_99_for_recurring_decimal"]
    )


def arch_31_infinite_geometric_solve_for_first_term_or_ratio(rng: random.Random) -> Dict[str, Any]:
    # Given S_inf and r, find a, OR given S_inf and a, find r
    r_num, r_den = rng.choice([(1, 2), (1, 3), (2, 5), (3, 5)])
    s_inf = rng.choice([25, 30, 45, 60, 90])
    # a = S_inf * (1 - r) = s_inf * (r_den - r_num) / r_den
    a = (s_inf * (r_den - r_num)) // r_den
    prompt = (
        f"An infinite geometric series converges to a sum of ${s_inf}$ ($S_\\infty = {s_inf}$). "
        f"The common ratio is $r = \\frac{{{r_num}}}{{{r_den}}}$.\n\n"
        f"Calculate the first term $a$ of the series."
    )
    ans = str(a)
    sol = (
        f"Step 1: Formula $S_\\infty = \\frac{{a}}{{1 - r}}$.\n"
        f"Step 2: Substitute given values:\n"
        f"$${s_inf} = \\frac{{a}}{{1 - \\frac{{{r_num}}}{{{r_den}}}}} = \\frac{{a}}{{\\frac{{{r_den - r_num}}}{{{r_den}}}}}$$\n"
        f"Step 3: Solve for $a$:\n"
        f"$$a = {s_inf} \\times \\frac{{{r_den - r_num}}}{{{r_den}}} = {a}$$."
    )
    return _calc_q(
        rng, f"g12_seq_31_{rng.randint(100000, 999999)}", "31_infinite_geometric_solve_for_first_term_or_ratio",
        "Solving for First Term from Sum to Infinity", prompt, ans, sol,
        {"tier_1": "Rearrange S_infinity = a / (1 - r) to make a the subject: a = S_infinity * (1 - r).",
         "tier_2": f"Compute 1 - {r_num}/{r_den} = {r_den - r_num}/{r_den}, then multiply by {s_inf}.",
         "tier_3": f"a = {a}."},
        ["incorrect_transposition_of_sum_to_infinity_formula"]
    )


def arch_32_sigma_notation_arithmetic_basic(rng: random.Random) -> Dict[str, Any]:
    c = rng.choice([2, 3, 4, 5])
    k_offset = rng.choice([-3, -1, 1, 4])
    n = rng.choice([15, 20, 25])
    # T_k = c*k + k_offset
    t1 = c * 1 + k_offset
    tn = c * n + k_offset
    total = (n * (t1 + tn)) // 2
    prompt = (
        f"Evaluate the following summation given in sigma notation:\n"
        f"$$\\sum_{{k=1}}^{{{n}}} ({c}k {'+' if k_offset >= 0 else '-'} {abs(k_offset)})$$"
    )
    ans = str(total)
    sol = (
        f"Step 1: Write down the first few terms by substituting $k = 1, 2, 3$:\n"
        f"$k=1: T_1 = {c}(1) {'+' if k_offset >= 0 else '-'} {abs(k_offset)} = {t1}$\n"
        f"$k=2: T_2 = {c}(2) {'+' if k_offset >= 0 else '-'} {abs(k_offset)} = {t1 + c}$\n"
        f"This is an arithmetic series with $a = {t1}$ and $d = {c}$.\n"
        f"Step 2: Number of terms $n = {n} - 1 + 1 = {n}$.\n"
        f"Step 3: Last term $T_{{{n}}} = {c}({n}) {'+' if k_offset >= 0 else '-'} {abs(k_offset)} = {tn}$.\n"
        f"Step 4: Sum: $S_{{{n}}} = \\frac{{{n}}}{{2}}(T_1 + T_{{{n}}}) = \\frac{{{n}}}{{2}}({t1} + {tn}) = {total}$."
    )
    return _calc_q(
        rng, f"g12_seq_32_{rng.randint(100000, 999999)}", "32_sigma_notation_arithmetic_basic",
        "Evaluating Arithmetic Sigma Summation", prompt, ans, sol,
        {"tier_1": f"Find the first term (k=1) and the last term (k={n}).",
         "tier_2": f"T1 = {t1}, Tn = {tn}, n = {n}. Apply Sn = n/2 * (a + l).",
         "tier_3": f"Sum = {total}."},
        ["sigma_index_miscalculation"]
    )


def arch_33_sigma_notation_arithmetic_non_unit_start(rng: random.Random) -> Dict[str, Any]:
    c = rng.choice([2, 3, 5])
    k_offset = rng.choice([-2, 1, 3])
    m = rng.choice([4, 5, 6])
    n = m + rng.choice([15, 20, 24])
    num_terms = n - m + 1
    t_first = c * m + k_offset
    t_last = c * n + k_offset
    total = (num_terms * (t_first + t_last)) // 2
    prompt = (
        f"Evaluate the sum:\n"
        f"$$\\sum_{{k={m}}}^{{{n}}} ({c}k {'+' if k_offset >= 0 else '-'} {abs(k_offset)})$$"
    )
    ans = str(total)
    sol = (
        f"Step 1: Calculate the number of terms: $n = \\text{{top}} - \\text{{bottom}} + 1 = {n} - {m} + 1 = {num_terms}$.\n"
        f"Step 2: First term ($k = {m}$): $a = {c}({m}) {'+' if k_offset >= 0 else '-'} {abs(k_offset)} = {t_first}$.\n"
        f"Step 3: Last term ($k = {n}$): $l = {c}({n}) {'+' if k_offset >= 0 else '-'} {abs(k_offset)} = {t_last}$.\n"
        f"Step 4: Sum: $S = \\frac{{{num_terms}}}{{2}}({t_first} + {t_last}) = {total}$."
    )
    return _calc_q(
        rng, f"g12_seq_33_{rng.randint(100000, 999999)}", "33_sigma_notation_arithmetic_non_unit_start",
        "Arithmetic Sigma Notation with Non-Unit Lower Index", prompt, ans, sol,
        {"tier_1": f"The number of terms is top - bottom + 1 = {n} - {m} + 1 = {num_terms}.",
         "tier_2": f"Find a by substituting k = {m}, and l by substituting k = {n}.",
         "tier_3": f"Sum = {total}."},
        ["off_by_one_number_of_terms_in_sigma"]
    )


def arch_34_sigma_notation_geometric_basic(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([2, 3, 5])
    r = rng.choice([2, 3])
    n = rng.choice([6, 7, 8])
    total = a * (r**n - 1) // (r - 1)
    prompt = (
        f"Evaluate the geometric series represented in sigma notation:\n"
        f"$$\\sum_{{k=1}}^{{{n}}} {a} \\cdot {r}^{{k - 1}}$$"
    )
    ans = str(total)
    sol = (
        f"Step 1: Substitute $k = 1, 2, 3$ to identify parameters:\n"
        f"$k=1: {a} \\cdot {r}^0 = {a}$\n"
        f"$k=2: {a} \\cdot {r}^1 = {a * r}$\n"
        f"This is a geometric series with $a = {a}$, $r = {r}$, and $n = {n}$.\n"
        f"Step 2: Apply $S_n = \\frac{{a(r^n - 1)}}{{r - 1}}$:\n"
        f"$$S_{{{n}}} = \\frac{{{a}({r}^{{{n}}} - 1)}}{{{r} - 1}} = {total}$."
    )
    return _calc_q(
        rng, f"g12_seq_34_{rng.randint(100000, 999999)}", "34_sigma_notation_geometric_basic",
        "Evaluating Geometric Sigma Summation", prompt, ans, sol,
        {"tier_1": f"Identify a = {a}, r = {r}, and n = {n}.",
         "tier_2": f"Use Sn = {a} * ({r}^{{{n}}} - 1) / ({r} - 1).",
         "tier_3": f"Sum = {total}."},
        ["geometric_sigma_power_index_confusion"]
    )


def arch_35_sigma_notation_geometric_non_unit_start(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([3, 4, 5])
    r = 2
    m = rng.choice([3, 4])
    n = m + rng.choice([5, 6, 7])
    num_terms = n - m + 1
    first_term = a * (r ** (m - 1))
    total = first_term * (r**num_terms - 1) // (r - 1)
    prompt = (
        f"Calculate the numerical value of:\n"
        f"$$\\sum_{{k={m}}}^{{{n}}} {a} \\cdot 2^{{k - 1}}$$"
    )
    ans = str(total)
    sol = (
        f"Step 1: Number of terms: $N = {n} - {m} + 1 = {num_terms}$.\n"
        f"Step 2: First term ($k = {m}$): $A = {a} \\cdot 2^{{{m} - 1}} = {first_term}$.\n"
        f"Step 3: Common ratio: $r = 2$.\n"
        f"Step 4: Sum: $S = \\frac{{{first_term}(2^{{{num_terms}}} - 1)}}{{2 - 1}} = {total}$."
    )
    return _calc_q(
        rng, f"g12_seq_35_{rng.randint(100000, 999999)}", "35_sigma_notation_geometric_non_unit_start",
        "Geometric Sigma with Non-Unit Start Index", prompt, ans, sol,
        {"tier_1": f"First substitute k = {m} to find the actual first term.",
         "tier_2": f"Number of terms is {n} - {m} + 1 = {num_terms}. Use Sn = A(r^N - 1)/(r - 1).",
         "tier_3": f"Sum = {total}."},
        ["incorrect_first_term_in_offset_sigma"]
    )


def arch_36_sigma_notation_infinite_series(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([18, 27, 36, 48])
    r_inv = rng.choice([2, 3, 4])
    # r = 1/r_inv
    # S_inf = a / (1 - 1/r_inv) = a * r_inv / (r_inv - 1)
    s_inf = (a * r_inv) // (r_inv - 1)
    prompt = (
        f"Evaluate the infinite series expressed in sigma notation:\n"
        f"$$\\sum_{{k=1}}^{{\\infty}} {a} \\left(\\frac{{1}}{{{r_inv}}}\\right)^{{k - 1}}$$"
    )
    ans = str(s_inf)
    sol = (
        f"Step 1: Substitute $k = 1$ to find the first term: $a = {a} \\left(\\frac{{1}}{{{r_inv}}}\\right)^0 = {a}$.\n"
        f"Step 2: Common ratio $r = \\frac{{1}}{{{r_inv}}}$. Since $|r| < 1$, the series converges.\n"
        f"Step 3: Apply $S_\\infty = \\frac{{a}}{{1 - r}}$:\n"
        f"$$S_\\infty = \\frac{{{a}}}{{1 - \\frac{{1}}{{{r_inv}}}}} = \\frac{{{a}}}{{\\frac{{{r_inv - 1}}}{{{r_inv}}}}} = \\frac{{{a} \\times {r_inv}}}{{{r_inv - 1}}} = {s_inf}$$."
    )
    return _calc_q(
        rng, f"g12_seq_36_{rng.randint(100000, 999999)}", "36_sigma_notation_infinite_series",
        "Evaluating Infinite Geometric Sigma Series", prompt, ans, sol,
        {"tier_1": "Recognise the infinite upper limit and use S_infinity = a / (1 - r).",
         "tier_2": f"Here a = {a} and r = 1/{r_inv}. Evaluate {a} / (1 - 1/{r_inv}).",
         "tier_3": f"Sum = {s_inf}."},
        ["applied_finite_sum_formula_to_infinite_series"]
    )


def arch_37_sigma_notation_solve_upper_limit_arithmetic(rng: random.Random) -> Dict[str, Any]:
    # Sum_{k=1}^n (2k + 1) = n^2 + 2n = target
    n = rng.choice([12, 15, 18, 22])
    # T_k = 2k + 1 => a = 3, l = 2n + 1, sum = n*(3 + 2n + 1)/2 = n*(n + 2) = n^2 + 2n
    target = n * (n + 2)
    prompt = (
        f"Solve for the upper limit $n$ in the summation:\n"
        f"$$\\sum_{{k=1}}^{{n}} (2k + 1) = {target}$$"
    )
    ans = f"n = {n}"
    sol = (
        f"Step 1: Write down terms: $T_1 = 3,\\ T_2 = 5,\\ \\dots,\\ T_n = 2n + 1$.\n"
        f"This is an arithmetic series with $a = 3$ and $d = 2$.\n"
        f"Step 2: Formula $S_n = \\frac{{n}}{{2}}(a + l) = \\frac{{n}}{{2}}(3 + 2n + 1) = \\frac{{n}}{{2}}(2n + 4) = n(n + 2)$.\n"
        f"Step 3: Equate to ${target}$ and solve the quadratic:\n"
        f"$$n^2 + 2n - {target} = 0$$\n"
        f"$$(n - {n})(n + {n + 2}) = 0 \\implies n = {n}$ (reject $n = -{n + 2}$ since $n \\in \\mathbb{{N}}$)."
    )
    return _calc_q(
        rng, f"g12_seq_37_{rng.randint(100000, 999999)}", "37_sigma_notation_solve_upper_limit_arithmetic",
        "Solving for Upper Limit in Arithmetic Sigma Sum", prompt, ans, sol,
        {"tier_1": f"Express the sum in terms of n as n/2 * (T1 + Tn) and equate to {target}.",
         "tier_2": "Solve the quadratic equation in n and choose the positive root.",
         "tier_3": f"n = {n}."},
        ["negative_root_not_rejected_for_index"]
    )


def arch_38_sigma_notation_solve_upper_limit_geometric(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([2, 3, 5])
    r = 2
    n = rng.choice([7, 8, 9])
    target = a * (2**n - 1)
    prompt = (
        f"Given that $\\sum_{{k=1}}^{{n}} {a} \\cdot 2^{{k - 1}} = {target}$, calculate the value of $n$."
    )
    ans = f"n = {n}"
    sol = (
        f"Step 1: First term $a = {a}$, common ratio $r = 2$.\n"
        f"Step 2: Formula $S_n = \\frac{{a(r^n - 1)}}{{r - 1}}$:\n"
        f"$$\\frac{{{a}(2^n - 1)}}{{2 - 1}} = {target}$$\n"
        f"$${a}(2^n - 1) = {target} \\implies 2^n - 1 = {target // a} \\implies 2^n = {2**n}$$\n"
        f"Step 3: Since $2^{{{n}}} = {2**n}$, we conclude $n = {n}$."
    )
    return _calc_q(
        rng, f"g12_seq_38_{rng.randint(100000, 999999)}", "38_sigma_notation_solve_upper_limit_geometric",
        "Solving for Upper Limit in Geometric Sigma Sum", prompt, ans, sol,
        {"tier_1": f"Apply the geometric series sum formula and isolate 2^n.",
         "tier_2": f"2^n = {2**n}. Express {2**n} as a power of 2.",
         "tier_3": f"n = {n}."},
        ["exponential_isolation_error"]
    )


def arch_39_write_series_in_sigma_notation(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([3, 5, 7])
    d = rng.choice([3, 4, 6])
    n = rng.choice([15, 20, 25])
    last = a + (n - 1) * d
    c = a - d
    sign = "+" if c >= 0 else "-"
    abs_c = abs(c)
    expr_k = f"{d}k {sign} {abs_c}" if abs_c != 0 else f"{d}k"
    prompt = (
        f"Write the following finite arithmetic series in sigma notation:\n"
        f"$${a} + {a + d} + {a + 2*d} + \\dots + {last}$$"
    )
    correct = f"\\sum_{{k=1}}^{{{n}}} ({expr_k})"
    distractors = [
        f"\\sum_{{k=1}}^{{{n + 1}}} ({expr_k})",
        f"\\sum_{{k=0}}^{{{n}}} ({expr_k})",
        f"\\sum_{{k=1}}^{{{n}}} ({d}k {'+' if a >= 0 else '-'} {abs(a)})",
    ]
    sol = (
        f"Step 1: Find general term formula $T_k = a + (k - 1)d = {a} + (k - 1)({d}) = {expr_k}$.\n"
        f"Step 2: Find number of terms $n$: ${last} = {expr_k} \\implies n = {n}$.\n"
        f"Step 3: In sigma notation with lower index $k = 1$ and upper limit $n = {n}$:\n"
        f"$$\\sum_{{k=1}}^{{{n}}} ({expr_k})$$."
    )
    return _mcq_q(
        rng, f"g12_seq_39_{rng.randint(100000, 999999)}", "39_write_series_in_sigma_notation",
        "Expressing an Explicit Series in Sigma Notation", prompt, correct, distractors, sol,
        {"tier_1": "Determine the formula for Tk first, then find the number of terms n for the upper limit.",
         "tier_2": f"General term is {expr_k} and last term is reached at k = {n}.",
         "tier_3": correct},
        ["incorrect_upper_limit_when_writing_sigma"]
    )


def arch_40_split_sigma_notation_addition(rng: random.Random) -> Dict[str, Any]:
    # Sum_{k=1}^n [ (2k + 3) + 3 * 2^(k-1) ]
    n = rng.choice([6, 7, 8])
    # Part 1: arithmetic sum of 2k + 3 for k=1..n
    # T1 = 5, Tn = 2n + 3. S_arith = n*(5 + 2n + 3)/2 = n*(n + 4)
    s_arith = n * (n + 4)
    # Part 2: geometric sum 3 * 2^(k-1) for k=1..n
    # S_geom = 3 * (2^n - 1)
    s_geom = 3 * (2**n - 1)
    total = s_arith + s_geom
    prompt = (
        f"Evaluate the combined summation:\n"
        f"$$\\sum_{{k=1}}^{{{n}}} \\left[ (2k + 3) + 3 \\cdot 2^{{k - 1}} \\right]$$\n\n"
        f"(Hint: Use the linearity property to split the summation into arithmetic and geometric parts)."
    )
    ans = str(total)
    sol = (
        f"Step 1: Split using the distributive law of summation:\n"
        f"$$\\sum_{{k=1}}^{{{n}}} (2k + 3) + \\sum_{{k=1}}^{{{n}}} 3 \\cdot 2^{{k - 1}}$$\n"
        f"Step 2: Arithmetic sum ($a = 5, d = 2, n = {n}$):\n"
        f"$$S_1 = \\frac{{{n}}}{{2}}[2(5) + ({n} - 1)(2)] = {s_arith}$$\n"
        f"Step 3: Geometric sum ($a = 3, r = 2, n = {n}$):\n"
        f"$$S_2 = \\frac{{3(2^{{{n}}} - 1)}}{{2 - 1}} = {s_geom}$$\n"
        f"Step 4: Combine the two sums:\n"
        f"$$\\text{{Total}} = {s_arith} + {s_geom} = {total}$$."
    )
    return _calc_q(
        rng, f"g12_seq_40_{rng.randint(100000, 999999)}", "40_split_sigma_notation_addition",
        "Splitting Combined Arithmetic-Geometric Sigma Sum", prompt, ans, sol,
        {"tier_1": "Split into two separate sums: an arithmetic series and a geometric series.",
         "tier_2": f"Arithmetic part sums to {s_arith}; geometric part sums to {s_geom}.",
         "tier_3": f"Total = {total}."},
        ["attempted_single_formula_on_mixed_sum"]
    )


def arch_41_mixed_sequence_alternating_arithmetic_geometric(rng: random.Random) -> Dict[str, Any]:
    # Sequence: T1, T2, T3, T4, T5, T6 ...
    # Odd terms arithmetic: a1 = 3, d1 = 4 => 3, 7, 11, 15...
    # Even terms geometric: a2 = 2, r2 = 3 => 2, 6, 18, 54...
    # Combined: 3; 2; 7; 6; 11; 18; 15; 54; ...
    a_arith = rng.choice([2, 3, 5])
    d_arith = rng.choice([3, 4, 5])
    a_geom = rng.choice([2, 4])
    r_geom = rng.choice([2, 3])

    target_pos = rng.choice([19, 20])
    if target_pos % 2 == 1:
        # Odd position -> arithmetic index m = (target_pos + 1) // 2
        m = (target_pos + 1) // 2
        val = a_arith + (m - 1) * d_arith
        series_type = "arithmetic subsequence of odd-positioned terms"
    else:
        # Even position -> geometric index m = target_pos // 2
        m = target_pos // 2
        val = a_geom * (r_geom ** (m - 1))
        series_type = "geometric subsequence of even-positioned terms"

    seq_disp = [
        a_arith, a_geom,
        a_arith + d_arith, a_geom * r_geom,
        a_arith + 2 * d_arith, a_geom * (r_geom**2),
    ]
    seq_str = "; ".join(str(x) for x in seq_disp)

    prompt = (
        f"Consider the sequence:\n"
        f"$${seq_str};\\ \\dots$$\n\n"
        f"Notice that the sequence is formed by interlacing an arithmetic sequence and a geometric sequence.\n"
        f"Determine the numerical value of the {target_pos}-th term ($T_{{{target_pos}}}$)."
    )
    ans = str(val)
    sol = (
        f"Step 1: Separate into odd-positioned and even-positioned terms:\n"
        f"Odd terms: ${seq_disp[0]};\\ {seq_disp[2]};\\ {seq_disp[4]};\\ \\dots$ (Arithmetic with $a = {a_arith}, d = {d_arith}$)\n"
        f"Even terms: ${seq_disp[1]};\\ {seq_disp[3]};\\ {seq_disp[5]};\\ \\dots$ (Geometric with $a = {a_geom}, r = {r_geom}$)\n"
        f"Step 2: Position ${target_pos}$ belongs to the {series_type} at index $m = {m}$.\n"
        f"Step 3: Value: $T_{{{target_pos}}} = {val}$."
    )
    return _calc_q(
        rng, f"g12_seq_41_{rng.randint(100000, 999999)}", "41_mixed_sequence_alternating_arithmetic_geometric",
        "Interlaced Mixed Arithmetic and Geometric Sequences", prompt, ans, sol,
        {"tier_1": f"Check whether position {target_pos} is odd (arithmetic) or even (geometric).",
         "tier_2": f"Position {target_pos} corresponds to term index {m} in the {series_type}.",
         "tier_3": f"T_{{{target_pos}}} = {val}."},
        ["confuses_interlaced_odd_and_even_indices"]
    )


def arch_42_quadratic_pattern_first_second_differences(rng: random.Random) -> Dict[str, Any]:
    # Tn = an^2 + bn + c
    a = rng.choice([1, 2, 3])
    b = rng.choice([-3, -1, 2, 4])
    c = rng.choice([-5, 2, 5, 8])
    terms = [a * (n**2) + b * n + c for n in range(1, 5)]
    d1 = [terms[i+1] - terms[i] for i in range(3)]
    d2 = d1[1] - d1[0]
    prompt = (
        f"Given the quadratic number pattern: ${terms[0]};\\ {terms[1]};\\ {terms[2]};\\ {terms[3]};\\ \\dots$\n\n"
        f"1. Determine the constant second difference ($2a$).\n"
        f"2. Determine the formula for the general term $T_n = an^2 + bn + c$."
    )
    correct = f"Second diff = {d2}; T_n = {a}n^2 {'+' if b >= 0 else '-'} {abs(b)}n {'+' if c >= 0 else '-'} {abs(c)}"
    distractors = [
        f"Second diff = {d2}; T_n = {d2}n^2 + {b}n + {c}",
        f"Second diff = {d1[0]}; T_n = {a}n^2 + {d1[0]}n + {c}",
        f"Second diff = {d2}; T_n = {a}n^2 {'-' if b >= 0 else '+'} {abs(b)}n + {c}",
    ]
    sol = (
        f"Step 1: First differences: ${terms[1]} - {terms[0]} = {d1[0]}$, ${terms[2]} - {terms[1]} = {d1[1]}$, ${terms[3]} - {terms[2]} = {d1[2]}$.\n"
        f"Second difference: ${d1[1]} - {d1[0]} = {d2}$.\n"
        f"Step 2: Solve for $a, b, c$:\n"
        f"$2a = {d2} \\implies a = {a}$\n"
        f"$3a + b = {d1[0]} \\implies 3({a}) + b = {d1[0]} \\implies b = {b}$\n"
        f"$a + b + c = {terms[0]} \\implies {a} + ({b}) + c = {terms[0]} \\implies c = {c}$.\n"
        f"Step 3: $T_n = {a}n^2 {'+' if b >= 0 else '-'} {abs(b)}n {'+' if c >= 0 else '-'} {abs(c)}$."
    )
    return _mcq_q(
        rng, f"g12_seq_42_{rng.randint(100000, 999999)}", "42_quadratic_pattern_first_second_differences",
        "Quadratic Sequence General Term and Second Difference", prompt, correct, distractors, sol,
        {"tier_1": "Calculate first differences then second difference. Recall 2a = second diff.",
         "tier_2": f"2a = {d2}, 3a + b = {d1[0]}, and a + b + c = {terms[0]}.",
         "tier_3": correct},
        ["equated_a_directly_to_second_difference_instead_of_2a"]
    )


def arch_43_quadratic_pattern_find_term_position(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([1, 2])
    b = rng.choice([-2, 1, 3])
    c = rng.choice([2, 5, 8])
    n = rng.choice([12, 15, 20])
    target = a * (n**2) + b * n + c
    prompt = (
        f"Given the quadratic pattern with general term $T_n = {a}n^2 {'+' if b >= 0 else '-'} {abs(b)}n {'+' if c >= 0 else '-'} {abs(c)}$:\n\n"
        f"Determine the position $n$ of the term that has a value of ${target}$."
    )
    ans = f"n = {n}"
    sol = (
        f"Step 1: Set $T_n = {target}$:\n"
        f"$${a}n^2 {'+' if b >= 0 else '-'} {abs(b)}n {'+' if c >= 0 else '-'} {abs(c)} = {target}$$\n"
        f"$${a}n^2 {'+' if b >= 0 else '-'} {abs(b)}n - {target - c} = 0$$\n"
        f"Step 2: Factorise: $(n - {n})(...) = 0 \\implies n = {n}$ (reject negative root)."
    )
    return _calc_q(
        rng, f"g12_seq_43_{rng.randint(100000, 999999)}", "43_quadratic_pattern_find_term_position",
        "Finding Term Position in a Quadratic Sequence", prompt, ans, sol,
        {"tier_1": f"Equate Tn = {target} and arrange into the standard quadratic form an^2 + bn + c = 0.",
         "tier_2": "Solve for n using factorisation or the quadratic formula.",
         "tier_3": f"n = {n}."},
        ["quadratic_equation_sign_error_rearranging"]
    )


def arch_44_geometric_bouncing_ball_total_distance(rng: random.Random) -> Dict[str, Any]:
    h = rng.choice([12, 16, 20, 24])
    # rebound fraction 1/2, 2/3, 3/4
    frac_choice = rng.choice([(1, 2), (2, 3), (3, 4)])
    num_f, den_f = frac_choice
    # Total distance: initial drop h + 2 * sum_{k=1}^inf h * (num_f/den_f)^k
    # sum_{k=1}^inf h * r^k = h * r / (1 - r)
    # Total = h + 2 * h * (num_f / den_f) / (1 - num_f / den_f)
    #       = h + 2 * h * num_f / (den_f - num_f)
    rebound_sum = (2 * h * num_f) // (den_f - num_f)
    total_dist = h + rebound_sum
    prompt = (
        f"A rubber ball is dropped from a vertical height of ${h}\\text{{ m}}$ onto a flat concrete floor. "
        f"Each time it strikes the ground, it rebounds to exactly $\\frac{{{num_f}}}{{{den_f}}}$ of its previous height.\n\n"
        f"Assuming the ball continues bouncing indefinitely, calculate the total vertical distance the ball travels "
        f"before coming to rest."
    )
    ans = f"{total_dist} m"
    sol = (
        f"Step 1: Initial downward drop is ${h}\\text{{ m}}$.\n"
        f"Step 2: For every bounce thereafter, the ball travels UP and DOWN (twice the height):\n"
        f"Bounce 1: $2 \\times \\left({h} \\times \\frac{{{num_f}}}{{{den_f}}}\\right) = {2 * h * num_f / den_f:.2f}\\text{{ m}}$\n"
        f"This forms an infinite geometric series with first term $a = 2 \\times {h} \\times \\frac{{{num_f}}}{{{den_f}}} = \\frac{{{2 * h * num_f}}}{{{den_f}}}$ "
        f"and common ratio $r = \\frac{{{num_f}}}{{{den_f}}}$.\n"
        f"Step 3: Sum of all rebounds:\n"
        f"$$S_\\infty = \\frac{{a}}{{1 - r}} = \\frac{{{2 * h * num_f / den_f}}}{{1 - \\frac{{{num_f}}}{{{den_f}}}}} = {rebound_sum}\\text{{ m}}$$\n"
        f"Step 4: Total vertical distance $= {h} + S_\\infty = {h} + {rebound_sum} = {total_dist}\\text{{ m}}$."
    )
    return _calc_q(
        rng, f"g12_seq_44_{rng.randint(100000, 999999)}", "44_geometric_bouncing_ball_total_distance",
        "Applied Infinite Geometric Series - Bouncing Ball Distance", prompt, ans, sol,
        {"tier_1": "Remember the ball travels down once initially, but goes UP and DOWN for each subsequent rebound.",
         "tier_2": f"Initial drop = {h}. Rebound series has a = 2 * {h} * ({num_f}/{den_f}) and r = {num_f}/{den_f}.",
         "tier_3": f"Total distance = {total_dist} m."},
        ["forgot_to_double_rebound_heights_for_up_and_down_motion"]
    )


def arch_45_geometric_fractal_perimeter_area_svg(rng: random.Random) -> Dict[str, Any]:
    side = rng.choice([16, 24, 32])
    # Area of square 1 = side^2.
    # Stage 1: 1 square of side s, area A0 = side^2
    # In each step, squares of half side are added at 4 corners
    a0 = side * side
    # r = 1/4 area per square * 4 = 1/2 total ratio or similar
    # Let's consider 3 concentric nested squares rotated 45 deg: ratio of area is 1/2 per step!
    # A0 = side^2, A1 = A0/2, A2 = A0/4 ...
    # Total area sum to infinity = A0 / (1 - 1/2) = 2 * A0
    total_area_inf = 2 * a0
    svg_body = (
        f'<rect x="190" y="20" width="200" height="200" fill="#dbeafe" stroke="#1d4ed8" stroke-width="2"/>'
        f'<polygon points="290,20 390,120 290,220 190,120" fill="#fef3c7" stroke="#b453a9" stroke-width="2"/>'
        f'<rect x="240" y="70" width="100" height="100" fill="#dcfce7" stroke="#15803d" stroke-width="2"/>'
        f'<text x="290" y="15" font-size="12" font-weight="bold" text-anchor="middle" fill="#0f172a">Nested Squares Geometric Pattern</text>'
        f'<text x="290" y="235" font-size="11" text-anchor="middle" fill="#475569">Square 1 side = {side} cm, each inscribed square joins midpoints of previous</text>'
    )
    prompt = (
        f"A sequence of inscribed squares is constructed such that each new square has its vertices at the midpoints "
        f"of the sides of the preceding square. The outermost square has side length ${side}\\text{{ cm}}$.\n\n"
        f"1. Explain why the areas of consecutive squares form a geometric sequence, and state the common ratio $r$.\n"
        f"2. Calculate the total sum of the areas of all squares if this construction continues indefinitely."
    )
    correct = f"r = 1/2; Total Area = {total_area_inf} cm^2"
    distractors = [
        f"r = 1/4; Total Area = {a0 * 4 // 3} cm^2",
        f"r = 1/2; Total Area = {a0} cm^2",
        f"r = 1/sqrt(2); Total Area = {a0 * 2} cm^2",
    ]
    sol = (
        f"Step 1: Outermost square side $s_0 = {side}\\text{{ cm}}$, area $A_0 = {side}^2 = {a0}\\text{{ cm}}^2$.\n"
        f"Step 2: By the Pythagorean theorem, the side of the inscribed midpoint square is $s_1 = \\sqrt{{(s/2)^2 + (s/2)^2}} = \\frac{{s}}{{\\sqrt{{2}}}}$.\n"
        f"Hence its area is $A_1 = s_1^2 = \\frac{{s^2}}{{2}} = \\frac{{A_0}}{{2}}$.\n"
        f"The common ratio of the areas is $r = \\frac{{1}}{{2}}$.\n"
        f"Step 3: Sum to infinity of areas:\n"
        f"$$S_\\infty = \\frac{{A_0}}{{1 - r}} = \\frac{{{a0}}}{{1 - \\frac{{1}}{{2}}}} = \\frac{{{a0}}}{{\\frac{{1}}{{2}}}} = {total_area_inf}\\text{{ cm}}^2$$."
    )
    return _mcq_q(
        rng, f"g12_seq_45_{rng.randint(100000, 999999)}", "45_geometric_fractal_perimeter_area_svg",
        "Nested Geometric Fractal Squares Area Pattern", prompt, correct, distractors, sol,
        {"tier_1": "Connecting midpoints of a square creates a new square with exactly half the area.",
         "tier_2": f"Here A0 = {a0} and r = 1/2. Use S_infinity = A0 / (1 - r).",
         "tier_3": correct},
        ["used_linear_ratio_instead_of_area_ratio"],
        diagram_spec=_svg_spec(svg_body, 580, 250)
    )


def arch_46_arithmetic_pattern_seating_tiles_svg(rng: random.Random) -> Dict[str, Any]:
    # Examination tables in a row: 1 table seats 4, 2 tables seat 6, 3 tables seat 8...
    # Tn = 2n + 2
    n_tables = rng.choice([15, 20, 25, 30])
    seats = 2 * n_tables + 2
    svg_body = (
        f'<rect x="60" y="80" width="80" height="50" rx="4" fill="#fed7aa" stroke="#c2410c" stroke-width="2"/>'
        f'<circle cx="100" cy="55" r="10" fill="#94a3b8"/>'
        f'<circle cx="100" cy="155" r="10" fill="#94a3b8"/>'
        f'<circle cx="35" cy="105" r="10" fill="#94a3b8"/>'
        f'<circle cx="165" cy="105" r="10" fill="#94a3b8"/>'
        f'<text x="100" y="195" font-size="11" text-anchor="middle" fill="#0f172a">1 table = 4 seats</text>'
        f'<rect x="230" y="80" width="160" height="50" rx="4" fill="#fed7aa" stroke="#c2410c" stroke-width="2"/>'
        f'<line x1="310" y1="80" x2="310" y2="130" stroke="#c2410c" stroke-dasharray="3,3"/>'
        f'<circle cx="270" cy="55" r="10" fill="#94a3b8"/><circle cx="350" cy="55" r="10" fill="#94a3b8"/>'
        f'<circle cx="270" cy="155" r="10" fill="#94a3b8"/><circle cx="350" cy="155" r="10" fill="#94a3b8"/>'
        f'<circle cx="205" cy="105" r="10" fill="#94a3b8"/><circle cx="415" cy="105" r="10" fill="#94a3b8"/>'
        f'<text x="310" y="195" font-size="11" text-anchor="middle" fill="#0f172a">2 tables = 6 seats</text>'
        f'<text x="290" y="25" font-size="12" font-weight="bold" text-anchor="middle" fill="#0f172a">Examination Seating Arrangement (Target {n_tables} Desks)</text>'
    )
    prompt = (
        f"Square examination desks are arranged end-to-end in a straight row. "
        f"A single desk seats $4$ learners. Two desks pushed together seat $6$ learners. Three desks seat $8$ learners.\n\n"
        f"1. State the linear general formula $T_n$ for the number of seats around a row of $n$ desks.\n"
        f"2. How many learners can be seated if ${n_tables}$ desks are joined together?"
    )
    correct = f"T_n = 2n + 2; {seats} learners"
    distractors = [
        f"T_n = 4n; {4 * n_tables} learners",
        f"T_n = 2n + 4; {2 * n_tables + 4} learners",
        f"T_n = 3n + 1; {3 * n_tables + 1} learners",
    ]
    sol = (
        f"Step 1: The sequence of seats is $4;\\ 6;\\ 8;\\ \\dots$\n"
        f"First term $a = 4$, common difference $d = 2$.\n"
        f"General term formula: $T_n = a + (n - 1)d = 4 + (n - 1)(2) = 2n + 2$.\n"
        f"Step 2: For $n = {n_tables}$ desks:\n"
        f"$T_{{{n_tables}}} = 2({n_tables}) + 2 = {seats}$ learners."
    )
    return _mcq_q(
        rng, f"g12_seq_46_{rng.randint(100000, 999999)}", "46_arithmetic_pattern_seating_tiles_svg",
        "Applied Linear Seating Pattern", prompt, correct, distractors, sol,
        {"tier_1": "Determine the common difference between consecutive rows of tables.",
         "tier_2": f"Each additional table adds 2 seats. Formula is Tn = 2n + 2. Substitute n = {n_tables}.",
         "tier_3": correct},
        ["assumed_seats_multiply_independently_4n"],
        diagram_spec=_svg_spec(svg_body, 580, 220)
    )


def arch_47_geometric_decay_halflife_or_depreciation(rng: random.Random) -> Dict[str, Any]:
    # Quantity Q0 decays by p% each period: r = 1 - p/100
    q0 = rng.choice([500, 800, 1000])
    p = rng.choice([10, 20, 25])
    r_val = (100 - p) / 100
    steps = rng.choice([3, 4, 5])
    val = round(q0 * (r_val ** steps), 2)
    prompt = (
        f"A medical isotope has an initial mass of ${q0}\\text{{ mg}}$. At the end of each hour, "
        f"its remaining mass decreases by ${p}\\%$ of the mass present at the beginning of that hour.\n\n"
        f"1. Explain why the remaining hourly mass forms a geometric sequence, and state the common ratio $r$.\n"
        f"2. Calculate the remaining mass of the isotope after ${steps}$ hours."
    )
    correct = f"r = {r_val}; {val} mg"
    distractors = [
        f"r = {p / 100}; {round(q0 * ((p/100)**steps), 2)} mg",
        f"r = {r_val}; {round(q0 - steps * (q0 * p / 100), 2)} mg",
        f"r = 1.{p}; {round(q0 * ((1 + p/100)**steps), 2)} mg",
    ]
    sol = (
        f"Step 1: Decreasing by ${p}\\%$ means retaining $100\\% - {p}\\% = {100 - p}\\%$ of the prior mass.\n"
        f"Thus $r = \\frac{{{100 - p}}}{{100}} = {r_val}$.\n"
        f"Step 2: Remaining mass after ${steps}$ hours:\n"
        f"$$M_{{{steps}}} = {q0} \\times ({r_val})^{{{steps}}} = {val}\\text{{ mg}}$$."
    )
    return _mcq_q(
        rng, f"g12_seq_47_{rng.randint(100000, 999999)}", "47_geometric_decay_halflife_or_depreciation",
        "Applied Geometric Decay and Percentage Depreciation", prompt, correct, distractors, sol,
        {"tier_1": f"A decrease of {p}% corresponds to multiplying by (1 - {p}/100) = {r_val}.",
         "tier_2": f"Compute {q0} * ({r_val})^{{{steps}}}.",
         "tier_3": correct},
        ["confused_percentage_lost_with_multiplier_ratio"]
    )


def arch_48_series_proof_arithmetic_sn(rng: random.Random) -> Dict[str, Any]:
    var_intro = rng.choice([
        "When examining the derivation of the arithmetic series formula",
        "In algebraic proof questions regarding arithmetic series",
        "When deriving the sum formula for an arithmetic series",
    ])
    prompt = (
        f"{var_intro}, you are required to prove from first principles that the sum of the first "
        f"$n$ terms of an arithmetic series is given by:\n"
        f"$$S_n = \\frac{{n}}{{2}}[2a + (n - 1)d]$$\n\n"
        f"Which of the following describes the key algebraic technique used in this proof?"
    )
    correct = "Write Sn forwards, write Sn in reverse order, add the two equations to get 2*Sn = n*[2a + (n-1)d], then divide by 2"
    distractors = [
        "Multiply Sn by the common difference d and subtract the resulting series from Sn",
        "Factorise out (n - 1) from every term and apply the quadratic formula",
        "Integrate the general term Tn with respect to n between limits 1 and n",
    ]
    sol = (
        f"Step 1: Write the sum in natural order:\n"
        f"$S_n = a + (a+d) + (a+2d) + \\dots + [a+(n-1)d]$\n"
        f"Step 2: Write the sum in reverse order:\n"
        f"$S_n = [a+(n-1)d] + [a+(n-2)d] + \\dots + a$\n"
        f"Step 3: Add corresponding terms vertically:\n"
        f"$2S_n = [2a+(n-1)d] + [2a+(n-1)d] + \\dots + [2a+(n-1)d]$ ($n$ times)\n"
        f"$2S_n = n[2a + (n - 1)d] \\implies S_n = \\frac{{n}}{{2}}[2a + (n - 1)d]$."
    )
    return _mcq_q(
        rng, f"g12_seq_48_{rng.randint(100000, 999999)}", "48_series_proof_arithmetic_sn",
        "Proof of Arithmetic Series Sum Formula", prompt, correct, distractors, sol,
        {"tier_1": "Recall how Gauss proved the sum of numbers by pairing first and last terms.",
         "tier_2": "Writing the series forwards and in reverse produces n identical pairs equal to 2a + (n - 1)d.",
         "tier_3": correct},
        ["confused_arithmetic_reverse_proof_with_geometric_subtraction_proof"]
    )


def arch_49_series_proof_geometric_sn(rng: random.Random) -> Dict[str, Any]:
    var_intro = rng.choice([
        "When examining the derivation of the geometric series formula",
        "In algebraic proof questions regarding geometric series",
        "When deriving the sum formula for a finite geometric series",
    ])
    prompt = (
        f"{var_intro}, you are required to prove from first principles that the sum of the first "
        f"$n$ terms of a geometric series ($r \\ne 1$) is given by:\n"
        f"$$S_n = \\frac{{a(r^n - 1)}}{{r - 1}}$$\n\n"
        f"Which algebraic procedure constitutes the core mechanism of this proof?"
    )
    correct = "Write out Sn, multiply the entire equation by r to get r*Sn, subtract Sn - r*Sn (or r*Sn - Sn) so all middle terms cancel, and factorise out Sn"
    distractors = [
        "Write Sn forwards and in reverse order and add the two equations together",
        "Divide each term by r and take the limit as n approaches infinity",
        "Differentiate both sides with respect to r and integrate from 0 to n",
    ]
    sol = (
        f"Step 1: Write the sum of $n$ geometric terms:\n"
        f"(1) $S_n = a + ar + ar^2 + \\dots + ar^{{n-1}}$\n"
        f"Step 2: Multiply equation (1) by $r$:\n"
        f"(2) $r S_n = ar + ar^2 + ar^3 + \\dots + ar^n$\n"
        f"Step 3: Subtract equation (1) from (2) (or vice versa):\n"
        f"$r S_n - S_n = ar^n - a$\n"
        f"$S_n(r - 1) = a(r^n - 1) \\implies S_n = \\frac{{a(r^n - 1)}}{{r - 1}}$ (for $r \\ne 1$)."
    )
    return _mcq_q(
        rng, f"g12_seq_49_{rng.randint(100000, 999999)}", "49_series_proof_geometric_sn",
        "Proof of Geometric Series Sum Formula", prompt, correct, distractors, sol,
        {"tier_1": "Multiplying Sn by r shifts all powers by 1.",
         "tier_2": "Subtracting eliminates all terms except the first and the last: ar^n - a.",
         "tier_3": correct},
        ["confused_geometric_proof_with_arithmetic_proof"]
    )


def arch_50_compound_nsc_exam_multi_step_sequences(rng: random.Random) -> Dict[str, Any]:
    # NSC Final Examination Style Question combining:
    # 1. Given 3 terms of an arithmetic sequence: (x + 3); (2x); (3x - 5)
    # 2. Find x and hence the arithmetic sequence
    # 3. Use that same x as the ratio or term in a geometric series
    x_val = rng.choice([6, 8, 10])
    # T1 = x + 2, T2 = 2x - 1, T3 = 3x - 4 => 2*(2x - 1) = (x + 2) + (3x - 4) => 4x - 2 = 4x - 2 (identity)
    # Let 2*T2 = T1 + T3
    # 2*(2x + 1) = (x + 5) + (4x - 2) => 4x + 2 = 5x + 3 => x = -1
    # Let T1 = 2x, T2 = 3x - 2, T3 = 5x - 8
    # 2*(3x - 2) = 2x + (5x - 8) => 6x - 4 = 7x - 8 => x = 4
    # For general x:
    # T1 = x, T2 = 2x - 3, T3 = 4x - 12 => 2*(2x - 3) = 4x - 6. (x) + (4x - 12) = 5x - 12 => x = 6!
    # T1 = 6, T2 = 9, T3 = 12 (d = 3).
    # Then consider geometric series with a = x = 6 and r = 1/2.
    # Calculate sum to infinity: S_inf = 6 / (1 - 1/2) = 12.
    d = 3
    t1 = x_val
    t2 = 2 * x_val - (x_val - d)  # x_val + d
    t3 = x_val + 2 * d
    # S_inf for geometric series with first term a = x_val and r = 1/3
    s_inf = (x_val * 3) // 2
    prompt = (
        f"**Examination Level 4 Challenge:**\n\n"
        f"1. The first three terms of an arithmetic sequence are:\n"
        f"$$(x);\\ (2x - {x_val - d});\\ (3x - {2*x_val - 2*d})$$\n"
        f"Show that $x = {x_val}$, and write down the common difference $d$.\n\n"
        f"2. A convergent geometric series has a first term equal to $x = {x_val}$ and a common ratio of $r = \\frac{{1}}{{3}}$.\n"
        f"Calculate the sum to infinity ($S_\\infty$) of this geometric series."
    )
    correct = f"x = {x_val}, d = {d}; S_infinity = {s_inf}"
    distractors = [
        f"x = {x_val}, d = {d + 1}; S_infinity = {s_inf + 3}",
        f"x = {x_val + 2}, d = {d}; S_infinity = {s_inf}",
        f"x = {x_val}, d = {d}; S_infinity = {x_val * 3}",
    ]
    sol = (
        f"Step 1: Arithmetic sequence condition $T_2 - T_1 = T_3 - T_2$:\n"
        f"$$2(T_2) = T_1 + T_3$$\n"
        f"Solving the linear equation yields $x = {x_val}$.\n"
        f"The terms are ${t1};\\ {t2};\\ {t3}$, so common difference $d = {t2} - {t1} = {d}$.\n"
        f"Step 2: Geometric series parameters: $a = {x_val}$ and $r = \\frac{{1}}{{3}}$.\n"
        f"Since $|r| < 1$, the series converges.\n"
        f"$$S_\\infty = \\frac{{a}}{{1 - r}} = \\frac{{{x_val}}}{{1 - \\frac{{1}}{{3}}}} = \\frac{{{x_val}}}{{\\frac{{2}}{{3}}}} = \\frac{{3 \\times {x_val}}}{{2}} = {s_inf}$$."
    )
    return _mcq_q(
        rng, f"g12_seq_50_{rng.randint(100000, 999999)}", "50_compound_nsc_exam_multi_step_sequences",
        "Compound Multi-Step Examination Sequences Problem", prompt, correct, distractors, sol,
        {"tier_1": "Solve for x using 2*T2 = T1 + T3, then apply S_infinity = a / (1 - r) using the resulting x.",
         "tier_2": f"x = {x_val} gives d = {d}. For the geometric series, evaluate {x_val} / (1 - 1/3).",
         "tier_3": correct},
        ["confused_arithmetic_and_geometric_formulas_in_multi_part_question"]
    )


BUILDERS_26_50: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    "26_geometric_series_sum_formula_basic": arch_26_geometric_series_sum_formula_basic,
    "27_geometric_series_solve_for_n_log": arch_27_geometric_series_solve_for_n_log,
    "28_sum_to_infinity_condition_for_convergence": arch_28_sum_to_infinity_condition_for_convergence,
    "29_sum_to_infinity_calculation": arch_29_sum_to_infinity_calculation,
    "30_recurring_decimal_to_fraction_geometric": arch_30_recurring_decimal_to_fraction_geometric,
    "31_infinite_geometric_solve_for_first_term_or_ratio": arch_31_infinite_geometric_solve_for_first_term_or_ratio,
    "32_sigma_notation_arithmetic_basic": arch_32_sigma_notation_arithmetic_basic,
    "33_sigma_notation_arithmetic_non_unit_start": arch_33_sigma_notation_arithmetic_non_unit_start,
    "34_sigma_notation_geometric_basic": arch_34_sigma_notation_geometric_basic,
    "35_sigma_notation_geometric_non_unit_start": arch_35_sigma_notation_geometric_non_unit_start,
    "36_sigma_notation_infinite_series": arch_36_sigma_notation_infinite_series,
    "37_sigma_notation_solve_upper_limit_arithmetic": arch_37_sigma_notation_solve_upper_limit_arithmetic,
    "38_sigma_notation_solve_upper_limit_geometric": arch_38_sigma_notation_solve_upper_limit_geometric,
    "39_write_series_in_sigma_notation": arch_39_write_series_in_sigma_notation,
    "40_split_sigma_notation_addition": arch_40_split_sigma_notation_addition,
    "41_mixed_sequence_alternating_arithmetic_geometric": arch_41_mixed_sequence_alternating_arithmetic_geometric,
    "42_quadratic_pattern_first_second_differences": arch_42_quadratic_pattern_first_second_differences,
    "43_quadratic_pattern_find_term_position": arch_43_quadratic_pattern_find_term_position,
    "44_geometric_bouncing_ball_total_distance": arch_44_geometric_bouncing_ball_total_distance,
    "45_geometric_fractal_perimeter_area_svg": arch_45_geometric_fractal_perimeter_area_svg,
    "46_arithmetic_pattern_seating_tiles_svg": arch_46_arithmetic_pattern_seating_tiles_svg,
    "47_geometric_decay_halflife_or_depreciation": arch_47_geometric_decay_halflife_or_depreciation,
    "48_series_proof_arithmetic_sn": arch_48_series_proof_arithmetic_sn,
    "49_series_proof_geometric_sn": arch_49_series_proof_geometric_sn,
    "50_compound_nsc_exam_multi_step_sequences": arch_50_compound_nsc_exam_multi_step_sequences,
}
