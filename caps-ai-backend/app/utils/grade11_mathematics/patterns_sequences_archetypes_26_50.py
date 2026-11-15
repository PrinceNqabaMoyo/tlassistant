"""Grade 11 Mathematics — Number Patterns Archetypes 26–50.
100% Aligned with South African National Curriculum Standards (Grade 11 Term 1).
Grounded in curriculum_docs_auto/Mathematics_Gr11/Term 1/03. Number patterns.md.
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List

from app.utils.grade11_mathematics._math_common import (
    step,
)
from app.utils.grade11_mathematics.patterns_sequences_archetypes_01_25 import (
    _fmt_linear,
    _fmt_quad,
    _q,
    _svg_spec,
)


# 26. First differences as a linear sequence D_n = T_{n+1} - T_n
def build_26_quadratic_first_differences_as_linear_sequence(r: random.Random) -> Dict[str, Any]:
    a = r.choice([1, 2, 3, 4])
    b = r.randint(-7, 7)
    c = r.randint(-10, 10)
    terms = [a * n * n + b * n + c for n in range(1, 6)]
    d1 = [terms[i + 1] - terms[i] for i in range(4)]
    # D_n = T_{n+1} - T_n = 2an + (a + b)
    dn_str = _fmt_linear(2 * a, a + b)
    ans = f"D_n = {dn_str}"
    prompt = (
        f"Consider the quadratic number pattern: ${terms[0]};\\; {terms[1]};\\; {terms[2]};\\; {terms[3]};\\; {terms[4]};\\; ...$\n\n"
        f"Write down the first four terms of the sequence of first differences and determine its general term $D_n$."
    )
    steps = [
        step(from_latex=f"{terms[0]}; {terms[1]}; {terms[2]}; {terms[3]}; {terms[4]}", to_latex_str=f"\\text{{First differences: }} {d1[0]}; {d1[1]}; {d1[2]}; {d1[3]}", op="Calculate first four first differences", rule="D_n = T_{n+1} - T_n"),
        step(from_latex=f"a_{{D}} = {d1[0]},\\; d_{{D}} = {2*a}", to_latex_str=ans, op="Find linear general term for the first differences", rule="First differences of a quadratic sequence form a linear sequence"),
    ]
    return _q("26_quadratic_first_differences_as_linear_sequence", 26, prompt, ans, steps,
              "The first differences of a quadratic sequence form an arithmetic (linear) sequence with common difference 2a.",
              "D_n = D_1 + (n - 1)d_2 = 2an + (a + b).",
              f"First differences are {d1[0]}; {d1[1]}; {d1[2]}; {d1[3]}, so {ans}.",
              ["treated_first_differences_as_quadratic"], "medium", 3)


# 27. Which two consecutive terms have a given first difference
def build_27_quadratic_consecutive_terms_from_given_first_difference(r: random.Random) -> Dict[str, Any]:
    a = r.choice([1, 2, 3, 4])
    b = r.randint(-6, 6)
    c = r.randint(-12, 12)
    k = r.randint(9, 24)
    terms = [a * n * n + b * n + c for n in range(1, 5)]
    d1 = [terms[i + 1] - terms[i] for i in range(3)]
    target_diff = 2 * a * k + (a + b)
    dn_str = _fmt_linear(2 * a, a + b)
    ans = f"T_{{{k}}} \\text{{ and }} T_{{{k+1}}}"
    prompt = (
        f"Given the quadratic number pattern: ${terms[0]};\\; {terms[1]};\\; {terms[2]};\\; {terms[3]};\\; ...$\n\n"
        f"Between which two consecutive terms in the quadratic sequence is the first difference equal to ${target_diff}$?"
    )
    steps = [
        step(from_latex=f"D_1 = {d1[0]},\\; D_2 = {d1[1]},\\; D_3 = {d1[2]}", to_latex_str=f"D_n = T_{{n+1}} - T_n = {dn_str}", op="Find general term D_n of the first differences", rule="Linear sequence of first differences"),
        step(from_latex=f"{dn_str} = {target_diff}", to_latex_str=f"n = {k} \\implies \\text{{Between }} T_{{{k}}} \\text{{ and }} T_{{{k+1}}}", op="Solve D_n = target_diff for n", rule="D_n is the difference T_{n+1} - T_n"),
    ]
    return _q("27_quadratic_consecutive_terms_from_given_first_difference", 27, prompt, ans, steps,
              f"Remember that the n-th first difference D_n is the difference between T_n and T_(n+1).",
              "Set D_n = target difference and solve for n; the consecutive terms are T_n and T_{n+1}.",
              f"{dn_str} = {target_diff} gives n = {k}, so the difference occurs between T_{k} and T_{k+1}.",
              ["stated_t_n_minus_1_and_t_n_instead_of_t_n_and_t_n_plus_1"], "medium", 4)


# 28. Reconstruct quadratic sequence from first difference formula and T1
def build_28_quadratic_reconstruct_sequence_from_first_diff_formula(r: random.Random) -> Dict[str, Any]:
    a = r.choice([-3, -2, 1, 2, 3, 4])
    b = r.randint(-7, 7)
    c = r.randint(-12, 12)
    t1 = a + b + c
    p = 2 * a
    q_const = a + b
    dn_str = _fmt_linear(p, q_const)
    tn_str = _fmt_quad(a, b, c)
    ans = f"T_n = {tn_str}"
    prompt = (
        f"The first differences of a quadratic sequence $T_n = an^2 + bn + c$ are given by the linear formula:\n\n"
        f"$$D_n = T_{{n+1}} - T_n = {dn_str}$$\n\n"
        f"If the first term of the quadratic sequence is $T_1 = {t1}$, determine the general term $T_n$."
    )
    steps = [
        step(from_latex=f"D_n = {dn_str}", to_latex_str=f"D_1 = {p + q_const},\\; d_2 = {p} \\implies 2a = {p} \\implies a = {a}", op="Extract first difference D1 and second difference 2a", rule="2a = slope of D_n"),
        step(from_latex=f"3({a}) + b = {p + q_const},\\quad a + b + c = {t1}", to_latex_str=ans, op="Solve for b and c and write T_n", rule="3a + b = D1 and a + b + c = T1"),
    ]
    return _q("28_quadratic_reconstruct_sequence_from_first_diff_formula", 28, prompt, ans, steps,
              f"Calculate D1 = T2 - T1 by substituting n = 1 into D_n = {dn_str}, and note that the second difference is {p}.",
              "Since D_n = 2an + (a + b), the coefficient of n is 2a and D1 = 3a + b.",
              f"2a = {p} => a = {a}; 3({a}) + b = {p + q_const} => b = {b}; a + b + c = {t1} => c = {c}. Thus {ans}.",
              ["set_3a_plus_b_equal_to_q_const_instead_of_d1"], "hard", 4)


# 29. Unknown variable x in a quadratic pattern via equal second differences
def build_29_quadratic_unknown_variable_x_from_equal_second_differences(r: random.Random) -> Dict[str, Any]:
    a = r.choice([-3, -2, 1, 2, 3, 4])
    b = r.randint(-6, 6)
    c = r.randint(-10, 10)
    t = [a * n * n + b * n + c for n in range(1, 5)]
    # Replace T2 or T3 with x
    x_val = t[1]
    ans = f"x = {x_val}"
    prompt = (
        f"The first four terms of a quadratic number pattern are:\n\n"
        f"$${t[0]}; \\quad x; \\quad {t[2]}; \\quad {t[3]}$$\n\n"
        f"Calculate the value of $x$."
    )
    steps = [
        step(from_latex=f"\\text{{First diffs: }} x - ({t[0]});\\; {t[2]} - x;\\; {t[3] - t[2]}", to_latex_str=f"({t[2]} - x) - (x - ({t[0]})) = ({t[3] - t[2]}) - ({t[2]} - x)", op="Equate consecutive second differences", rule="Constant second difference"),
        step(from_latex=f"{t[2] + t[0]} - 2x = {t[3] - 2*t[2]} + x", to_latex_str=f"3x = {t[0] + 3*t[2] - t[3]} \\implies x = {x_val}", op="Solve linear equation for x", rule="Second difference equality"),
    ]
    return _q("29_quadratic_unknown_variable_x_from_equal_second_differences", 29, prompt, ans, steps,
              "Express the three first differences in terms of x, then set the two second differences equal to each other.",
              "In any quadratic sequence: (T3 - T2) - (T2 - T1) = (T4 - T3) - (T3 - T2).",
              f"Equating second differences gives 3x = {3*x_val}, so x = {x_val}.",
              ["equated_first_differences_instead_of_second_differences"], "medium", 4)


# 30. Missing middle terms in a quadratic sequence given constant second difference
def build_30_quadratic_missing_middle_terms_in_sequence(r: random.Random) -> Dict[str, Any]:
    a = r.choice([1, 2, 3, 4])
    b = r.randint(-5, 5)
    c = r.randint(-10, 10)
    t = [a * n * n + b * n + c for n in range(1, 5)]
    d2 = 2 * a
    ans = f"x = {t[1]}, \\quad y = {t[2]}"
    prompt = (
        f"A quadratic sequence has first four terms ${t[0]};\\; x;\\; y;\\; {t[3]}$ and a constant second difference of ${d2}$.\n\n"
        f"Determine the values of $x$ and $y$."
    )
    steps = [
        step(from_latex=f"\\text{{Second diffs}} = {d2}", to_latex_str=f"(y - x) - (x - ({t[0]})) = {d2} \\quad\\text{{and}}\\quad ({t[3]} - y) - (y - x) = {d2}", op="Set up two equations from the constant second difference", rule="Constant second difference"),
        step(from_latex=f"y - 2x = {d2 - t[0]},\\quad x - 2y = {d2 - t[3]}", to_latex_str=ans, op="Solve simultaneous linear equations for x and y", rule="Simultaneous equations"),
    ]
    return _q("30_quadratic_missing_middle_terms_in_sequence", 30, prompt, ans, steps,
              f"Set both second differences (y - 2x + {t[0]}) and ({t[3]} - 2y + x) equal to {d2}.",
              "Use T3 - 2T2 + T1 = d2 and T4 - 2T3 + T2 = d2.",
              f"Solving the simultaneous equations yields x = {t[1]} and y = {t[2]}.",
              ["sign_error_in_second_difference_expansion"], "hard", 4)


# 31. Minimum value of a quadratic sequence via completing the square
def build_31_quadratic_minimum_value_via_completing_square(r: random.Random) -> Dict[str, Any]:
    a = r.choice([1, 2, 3])
    p = r.randint(4, 11)
    q_min = r.randint(-25, 10)
    # T_n = a(n - p)^2 + q_min = a*n^2 - 2ap*n + (a*p^2 + q_min)
    b = -2 * a * p
    c = a * p * p + q_min
    tn_str = _fmt_quad(a, b, c)
    ans = f"\\text{{Minimum value}} = {q_min} \\text{{ at }} n = {p} \\;(T_{{{p}}} = {q_min})"
    prompt = (
        f"A quadratic sequence has general term:\n\n"
        f"$$T_n = {tn_str}$$\n\n"
        f"By completing the square or using the axis of symmetry, determine which term in the sequence has the minimum value, and state this minimum value."
    )
    steps = [
        step(from_latex=f"T_n = {tn_str}", to_latex_str=f"T_n = {a}(n - {p})^2 + ({q_min})", op="Complete the square in terms of n", rule="Vertex form a(n - p)^2 + q"),
        step(from_latex=f"(n - {p})^2 \\ge 0", to_latex_str=ans, op="Identify minimum value q at n = p", rule="Minimum of positive-a quadratic"),
    ]
    return _q("31_quadratic_minimum_value_via_completing_square", 31, prompt, ans, steps,
              "Use n = -b / (2a) or complete the square to write T_n = a(n - p)^2 + q.",
              "For a > 0, T_n = a(n - p)^2 + q attains its minimum value q when n = p.",
              f"n = -({b}) / (2*{a}) = {p}, and T_{p} = {q_min}.",
              ["confused_position_n_with_minimum_term_value_tn"], "medium", 4)


# 32. Maximum value of a quadratic sequence with negative a
def build_32_quadratic_maximum_value_negative_a_turning_point(r: random.Random) -> Dict[str, Any]:
    a = r.choice([-3, -2, -1])
    p = r.randint(4, 12)
    q_max = r.randint(15, 80)
    b = -2 * a * p
    c = a * p * p + q_max
    tn_str = _fmt_quad(a, b, c)
    ans = f"\\text{{Maximum value}} = {q_max} \\text{{ at }} n = {p} \\;(T_{{{p}}} = {q_max})"
    prompt = (
        f"The general term of a quadratic sequence is given by:\n\n"
        f"$$T_n = {tn_str}$$\n\n"
        f"Determine which term of the sequence has the greatest (maximum) value, and calculate this maximum value."
    )
    steps = [
        step(from_latex=f"n = -\\frac{{b}}{{2a}} = -\\frac{{{b}}}{{2({a})}}", to_latex_str=f"n = {p}", op="Find axis of symmetry n = -b / (2a)", rule="Turning point axis of symmetry"),
        step(from_latex=f"T_{{{p}}} = {a}({p})^2 + {b}({p}) + ({c})", to_latex_str=ans, op=f"Substitute n = {p} to find maximum value", rule="Maximum term evaluation"),
    ]
    return _q("32_quadratic_maximum_value_negative_a_turning_point", 32, prompt, ans, steps,
              "Since a < 0, the quadratic sequence reaches a maximum at n = -b / (2a).",
              "Evaluate n = -b / (2a), then substitute n into T_n to find the maximum value.",
              f"n = {p} and T_{p} = {q_max}.",
              ["sign_error_in_minus_b_over_2a"], "medium", 4)


# 33. Closest integer term when axis of symmetry is a half-integer
def build_33_quadratic_closest_integer_term_non_integer_axis(r: random.Random) -> Dict[str, Any]:
    a = r.choice([1, 2])
    k = r.randint(4, 10)
    # Axis at n = k + 0.5 => -b / (2a) = (2k + 1)/2 => b = -a(2k + 1)
    b = -a * (2 * k + 1)
    c = r.randint(-10, 20)
    t_k = a * k * k + b * k + c
    t_k1 = a * (k + 1) * (k + 1) + b * (k + 1) + c
    tn_str = _fmt_quad(a, b, c)
    ans = f"T_{{{k}}} = T_{{{k+1}}} = {t_k}"
    prompt = (
        f"Consider the quadratic sequence with general term $T_n = {tn_str}$.\n\n"
        f"Since $n \\in \\mathbb{{N}}$, determine the minimum term value in the sequence and the two term positions at which it occurs."
    )
    steps = [
        step(from_latex=f"n = -\\frac{{b}}{{2a}} = -\\frac{{{b}}}{{{2*a}}}", to_latex_str=f"n = {k}{{,}}5 \\notin \\mathbb{{N}}", op="Calculate continuous axis of symmetry", rule="Axis of symmetry"),
        step(from_latex=f"n = {k} \\text{{ and }} n = {k+1}", to_latex_str=ans, op="Evaluate closest natural numbers n = k and n = k + 1", rule="Discrete symmetry on integer lattice"),
    ]
    return _q("33_quadratic_closest_integer_term_non_integer_axis", 33, prompt, ans, steps,
              f"The parabola vertex occurs at n = {k},5, which is not a whole number! Test the nearest integers n = {k} and n = {k+1}.",
              "Because n must be a natural number, a half-integer axis of symmetry means the two adjacent integer terms are equal and share the extremum.",
              f"Axis is n = {k},5, so the minimum term value in the sequence occurs at n = {k} and n = {k+1}, where T_{k} = T_{k+1} = {t_k}.",
              ["reported_non_integer_n_as_term_position"], "hard", 4)


# 34. Simultaneous equations from three given non-consecutive terms
def build_34_quadratic_simultaneous_equations_from_three_given_terms(r: random.Random) -> Dict[str, Any]:
    a = r.choice([1, 2, 3])
    b = r.randint(-5, 5)
    c = r.randint(-8, 8)
    t1 = a + b + c
    t3 = 9 * a + 3 * b + c
    t5 = 25 * a + 5 * b + c
    tn_str = _fmt_quad(a, b, c)
    ans = f"a = {a},\\; b = {b},\\; c = {c} \\implies T_n = {tn_str}"
    prompt = (
        f"In a quadratic sequence $T_n = an^2 + bn + c$, it is given that "
        f"$T_1 = {t1}$, $T_3 = {t3}$, and $T_5 = {t5}$.\n\n"
        f"Set up simultaneous equations to determine the values of $a$, $b$, and $c$, and state $T_n$."
    )
    steps = [
        step(from_latex=f"a + b + c = {t1},\\quad 9a + 3b + c = {t3},\\quad 25a + 5b + c = {t5}", to_latex_str=f"8a + 2b = {t3 - t1} \\quad\\text{{and}}\\quad 16a + 2b = {t5 - t3}", op="Eliminate c by subtracting equations", rule="Simultaneous linear system"),
        step(from_latex=f"8a = {(t5 - t3) - (t3 - t1)}", to_latex_str=ans, op="Solve for a, back-substitute for b and c", rule="Elimination method"),
    ]
    return _q("34_quadratic_simultaneous_equations_from_three_given_terms", 34, prompt, ans, steps,
              "Substitute n = 1, n = 3, and n = 5 into T_n = an^2 + bn + c to form three linear equations.",
              "Subtracting the first equation from the second, and the second from the third, eliminates c immediately.",
              f"8a + 2b = {t3 - t1} and 16a + 2b = {t5 - t3}, giving 8a = {8*a} => a = {a}, b = {b}, c = {c}.",
              ["arithmetic_error_eliminating_c_in_simultaneous_system"], "hard", 5)


# 35. Quadratic sequence from given differences and sum condition
def build_35_quadratic_find_term_from_ratio_or_sum_condition(r: random.Random) -> Dict[str, Any]:
    a = r.choice([1, 2, 3])
    b = r.randint(-5, 5)
    c = r.randint(-9, 9)
    t1 = a + b + c
    t2 = 4 * a + 2 * b + c
    t3 = 9 * a + 3 * b + c
    d1 = t2 - t1
    d2_1 = t3 - t2
    s12 = t1 + t2
    tn_str = _fmt_quad(a, b, c)
    ans = f"T_1 = {t1},\\; T_2 = {t2},\\; T_n = {tn_str}"
    prompt = (
        f"In a quadratic number pattern $T_n = an^2 + bn + c$, the first two first differences are "
        f"$T_2 - T_1 = {d1}$ and $T_3 - T_2 = {d2_1}$, and the sum of the first two terms is $T_1 + T_2 = {s12}$.\n\n"
        f"Determine $T_1$, $T_2$, and the general term $T_n$."
    )
    steps = [
        step(from_latex=f"T_2 - T_1 = {d1},\\quad T_2 + T_1 = {s12}", to_latex_str=f"2T_2 = {d1 + s12} \\implies T_2 = {t2},\\; T_1 = {t1}", op="Solve for T1 and T2 from their sum and difference", rule="Simultaneous linear equations"),
        step(from_latex=f"d_2 = {d2_1} - ({d1}) = {2*a}", to_latex_str=ans, op="Use second difference 2a to determine a, b, c", rule="Quadratic formula from differences"),
    ]
    return _q("35_quadratic_find_term_from_ratio_or_sum_condition", 35, prompt, ans, steps,
              f"Add (T2 - T1 = {d1}) and (T2 + T1 = {s12}) to find 2*T2 first.",
              "Once T1, T2, and D2 are known, the constant second difference is D2 - D1.",
              f"T1 = {t1}, T2 = {t2}, second difference = {2*a}, so {ans}.",
              ["failed_to_combine_sum_and_difference_of_t1_and_t2"], "hard", 4)


# 36. Visual triangular dot array pattern with seeded SVG
def build_36_visual_triangular_dot_array_pattern(r: random.Random) -> Dict[str, Any]:
    extra = r.randint(0, 6)
    k = r.randint(10, 20)
    # T_n = n(n+1)/2 + extra
    t = [n * (n + 1) // 2 + extra for n in range(1, 5)]
    tk = k * (k + 1) // 2 + extra
    rad = 5 + (k % 3)
    svg = (
        f'<svg viewBox="0 0 420 140" xmlns="http://www.w3.org/2000/svg">'
        f'<rect x="0" y="0" width="420" height="140" fill="#f8fafc" rx="8"/>'
        f'<circle cx="65" cy="75" r="{rad}" fill="#1d4ed8"/>'
        f'<text x="65" y="115" font-size="11" font-family="sans-serif" fill="#1e293b" text-anchor="middle">Stage 1: {t[0]}</text>'
        f'<circle cx="175" cy="55" r="{rad}" fill="#1d4ed8"/>'
        f'<circle cx="163" cy="78" r="{rad}" fill="#1d4ed8"/><circle cx="187" cy="78" r="{rad}" fill="#1d4ed8"/>'
        f'<text x="175" y="115" font-size="11" font-family="sans-serif" fill="#1e293b" text-anchor="middle">Stage 2: {t[1]}</text>'
        f'<circle cx="310" cy="38" r="{rad}" fill="#1d4ed8"/>'
        f'<circle cx="298" cy="58" r="{rad}" fill="#1d4ed8"/><circle cx="322" cy="58" r="{rad}" fill="#1d4ed8"/>'
        f'<circle cx="286" cy="78" r="{rad}" fill="#1d4ed8"/><circle cx="310" cy="78" r="{rad}" fill="#1d4ed8"/><circle cx="334" cy="78" r="{rad}" fill="#1d4ed8"/>'
        f'<text x="310" y="115" font-size="11" font-family="sans-serif" fill="#1e293b" text-anchor="middle">Stage 3: {t[2]}</text>'
        f'</svg>'
    )
    c_str = f" + {extra}" if extra > 0 else ""
    ans = f"T_n = \\frac{{1}}{{2}}n^2 + \\frac{{1}}{{2}}n{c_str}; \\quad T_{{{k}}} = {tk}"
    prompt = (
        f"Refer to the diagram of the triangular dot arrangement, where each stage consists of a triangular array of dots plus ${extra}$ base markers, "
        f"giving the sequence ${t[0]};\\; {t[1]};\\; {t[2]};\\; {t[3]};\\; ...$\n\n"
        f"Determine the general formula $T_n$ and calculate the total count at Stage ${k}$."
    )
    steps = [
        step(from_latex=f"{t[0]}; {t[1]}; {t[2]}; {t[3]}", to_latex_str=f"T_n = \\frac{{n(n+1)}}{{2}}{c_str} = \\frac{{1}}{{2}}n^2 + \\frac{{1}}{{2}}n{c_str}", op="Identify triangular number formula plus constant", rule="Triangular numbers n(n+1)/2"),
        step(from_latex=f"n = {k}", to_latex_str=f"T_{{{k}}} = \\frac{{{k}({k+1})}}{{2}}{c_str} = {tk}", op=f"Evaluate at Stage {k}", rule="Direct evaluation"),
    ]
    return _q("36_visual_triangular_dot_array_pattern", 36, prompt, ans, steps,
              "Notice the first differences are 2, 3, 4, ..., so the constant second difference is 1 and a = 1/2.",
              "Triangular numbers follow n(n+1)/2 = 1/2 n^2 + 1/2 n.",
              f"T_n = n(n+1)/2{c_str}, so T_{k} = {tk}.",
              ["treated_triangular_numbers_as_linear"], "medium", 4, _svg_spec(svg))


# 37. Visual n x n matchstick grid pattern with seeded SVG
def build_37_visual_square_grid_matchstick_pattern(r: random.Random) -> Dict[str, Any]:
    k = r.randint(6, 15)
    # Horizontal matches: n(n+1), Vertical matches: n(n+1), Total: 2n(n+1) = 2n^2 + 2n
    tot_k = 2 * k * (k + 1)
    cell = 22 + (k % 7)
    svg = (
        f'<svg viewBox="0 0 420 145" xmlns="http://www.w3.org/2000/svg">'
        f'<rect x="0" y="0" width="420" height="145" fill="#fffbeb" rx="8"/>'
        f'<rect x="55" y="45" width="{cell}" height="{cell}" fill="none" stroke="#b45309" stroke-width="2.5"/>'
        f'<text x="{55+cell//2}" y="118" font-size="11" font-family="sans-serif" fill="#78350f" text-anchor="middle">1x1: 4 matches</text>'
        f'<rect x="165" y="35" width="{2*cell}" height="{2*cell}" fill="none" stroke="#b45309" stroke-width="2.5"/>'
        f'<line x1="{165+cell}" y1="35" x2="{165+cell}" y2="{35+2*cell}" stroke="#b45309" stroke-width="2"/>'
        f'<line x1="165" y1="{35+cell}" x2="{165+2*cell}" y2="{35+cell}" stroke="#b45309" stroke-width="2"/>'
        f'<text x="{165+cell}" y="118" font-size="11" font-family="sans-serif" fill="#78350f" text-anchor="middle">2x2: 12 matches</text>'
        f'<text x="330" y="65" font-size="12" font-family="sans-serif" font-weight="bold" fill="#78350f" text-anchor="middle">3x3: 24 matches</text>'
        f'<text x="330" y="90" font-size="12" font-family="sans-serif" fill="#92400e" text-anchor="middle">({k}x{k} = {tot_k})</text>'
        f'</svg>'
    )
    ans = f"T_n = 2n^2 + 2n; \\quad T_{{{k}}} = {tot_k}"
    prompt = (
        f"Refer to the diagram of the $n \\times n$ square matchstick arrangements. "
        f"A $1 \\times 1$ square uses $4$ matches, a $2 \\times 2$ arrangement uses $12$ matches, and a $3 \\times 3$ arrangement uses $24$ matches ($4;\\; 12;\\; 24;\\; 40;\\; ...$).\n\n"
        f"Determine the general formula $T_n$ for the total number of matches in an $n \\times n$ arrangement, and calculate the number of matches in a ${k} \\times {k}$ arrangement."
    )
    steps = [
        step(from_latex="4;\\; 12;\\; 24;\\; 40", to_latex_str="\\text{First diffs: } 8; 12; 16 \\implies 2a = 4 \\implies a = 2", op="Find first and second differences", rule="2a = second difference"),
        step(from_latex="3(2) + b = 8,\\quad 2 + b + c = 4", to_latex_str=f"T_n = 2n^2 + 2n,\\quad T_{{{k}}} = 2({k})^2 + 2({k}) = {tot_k}", op=f"Derive T_n and evaluate at n = {k}", rule="Quadratic matchstick grid formula"),
    ]
    return _q("37_visual_square_grid_matchstick_pattern", 37, prompt, ans, steps,
              "In an n x n square arrangement, there are n(n+1) horizontal matches and n(n+1) vertical matches.",
              "Total matches T_n = 2n(n+1) = 2n^2 + 2n.",
              f"T_n = 2n^2 + 2n, so for n = {k}, T_{k} = 2({k*k}) + 2({k}) = {tot_k}.",
              ["assumed_4n_squared_ignoring_shared_internal_edges"], "medium", 4, _svg_spec(svg))


# 38. Visual bordered tile frame pattern with seeded SVG
def build_38_visual_bordered_tile_frame_pattern(r: random.Random) -> Dict[str, Any]:
    c_add = r.randint(1, 5)
    k = r.randint(9, 18)
    # T_n = (n + 1)^2 + c_add * n = n^2 + (2 + c_add)n + 1
    b = 2 + c_add
    t = [n * n + b * n + 1 for n in range(1, 5)]
    tk = k * k + b * k + 1
    tn_str = _fmt_quad(1, b, 1)
    u = 16 + (k % 6)
    svg = (
        f'<svg viewBox="0 0 420 140" xmlns="http://www.w3.org/2000/svg">'
        f'<rect x="0" y="0" width="420" height="140" fill="#f8fafc" rx="8"/>'
        f'<rect x="45" y="40" width="{2*u}" height="{2*u}" fill="#cbd5e1" stroke="#334155" stroke-width="2"/>'
        f'<text x="{45+u}" y="115" font-size="11" font-family="sans-serif" fill="#1e293b" text-anchor="middle">n=1: {t[0]} tiles</text>'
        f'<rect x="165" y="30" width="{3*u}" height="{3*u}" fill="#cbd5e1" stroke="#334155" stroke-width="2"/>'
        f'<text x="{165+int(1.5*u)}" y="115" font-size="11" font-family="sans-serif" fill="#1e293b" text-anchor="middle">n=2: {t[1]} tiles</text>'
        f'<rect x="295" y="20" width="{4*u}" height="{4*u}" fill="#cbd5e1" stroke="#334155" stroke-width="2"/>'
        f'<text x="{295+2*u}" y="115" font-size="11" font-family="sans-serif" fill="#1e293b" text-anchor="middle">n=3: {t[2]} tiles</text>'
        f'</svg>'
    )
    ans = f"T_n = {tn_str}; \\quad T_{{{k}}} = {tk}"
    prompt = (
        f"Refer to the diagram of the tiled courtyard stages. "
        f"Stage $n$ consists of an $(n+1) \\times (n+1)$ central square of grey tiles plus ${c_add}n$ border tiles, "
        f"giving the sequence ${t[0]};\\; {t[1]};\\; {t[2]};\\; {t[3]};\\; ...$\n\n"
        f"Expand and simplify the general formula $T_n = (n+1)^2 + {c_add}n$ into the form $an^2 + bn + c$, and calculate $T_{{{k}}}$."
    )
    steps = [
        step(from_latex=f"T_n = (n + 1)^2 + {c_add}n", to_latex_str=f"T_n = n^2 + 2n + 1 + {c_add}n = {tn_str}", op="Expand binomial square and collect like terms", rule="Algebraic expansion"),
        step(from_latex=f"n = {k}", to_latex_str=f"T_{{{k}}} = ({k})^2 + {b}({k}) + 1 = {tk}", op=f"Substitute n = {k}", rule="Direct evaluation"),
    ]
    return _q("38_visual_bordered_tile_frame_pattern", 38, prompt, ans, steps,
              f"Expand (n + 1)^2 = n^2 + 2n + 1 and add {c_add}n.",
              "(n + 1)^2 + kn = n^2 + (2 + k)n + 1.",
              f"T_n = {tn_str} and T_{k} = {tk}.",
              ["expanded_n_plus_1_squared_as_n_squared_plus_1"], "medium", 4, _svg_spec(svg))


# 39. Visual L-shaped gnomon dot pattern with seeded SVG
def build_39_visual_l_shaped_gnomon_dot_pattern(r: random.Random) -> Dict[str, Any]:
    corner = r.randint(1, 4)
    arm_mult = r.choice([2, 3, 4])
    # T_n = arm_mult * n + corner
    k = r.randint(15, 35)
    t = [arm_mult * n + corner for n in range(1, 5)]
    tk = arm_mult * k + corner
    rad = 4 + (k % 3)
    svg = (
        f'<svg viewBox="0 0 420 135" xmlns="http://www.w3.org/2000/svg">'
        f'<rect x="0" y="0" width="420" height="135" fill="#f8fafc" rx="8"/>'
        f'<circle cx="55" cy="80" r="{rad}" fill="#0f766e"/><circle cx="55" cy="58" r="{rad}" fill="#0f766e"/><circle cx="77" cy="80" r="{rad}" fill="#0f766e"/>'
        f'<text x="66" y="112" font-size="11" font-family="sans-serif" fill="#1e293b" text-anchor="middle">Stage 1: {t[0]}</text>'
        f'<circle cx="175" cy="80" r="{rad}" fill="#0f766e"/><circle cx="175" cy="60" r="{rad}" fill="#0f766e"/><circle cx="175" cy="40" r="{rad}" fill="#0f766e"/>'
        f'<circle cx="195" cy="80" r="{rad}" fill="#0f766e"/><circle cx="215" cy="80" r="{rad}" fill="#0f766e"/>'
        f'<text x="195" y="112" font-size="11" font-family="sans-serif" fill="#1e293b" text-anchor="middle">Stage 2: {t[1]}</text>'
        f'<text x="330" y="68" font-size="12" font-family="sans-serif" font-weight="bold" fill="#0f766e" text-anchor="middle">Stage 3: {t[2]}</text>'
        f'<text x="330" y="92" font-size="12" font-family="sans-serif" fill="#115e59" text-anchor="middle">Stage 4: {t[3]}</text>'
        f'</svg>'
    )
    ans = f"T_n = {arm_mult}n + {corner}; \\quad T_{{{k}}} = {tk}"
    prompt = (
        f"Refer to the diagram of the L-shaped dot stages. "
        f"The number of dots in the first four stages is ${t[0]};\\; {t[1]};\\; {t[2]};\\; {t[3]};\\; ...$\n\n"
        f"Determine the general formula $T_n$ and calculate the number of dots in Stage ${k}$."
    )
    steps = [
        step(from_latex=f"d = {t[1]} - {t[0]} = {arm_mult}", to_latex_str=f"T_n = {arm_mult}n + {corner}", op="Find common difference and general term", rule="Linear gnomon growth"),
        step(from_latex=f"n = {k}", to_latex_str=f"T_{{{k}}} = {arm_mult}({k}) + {corner} = {tk}", op=f"Evaluate at n = {k}", rule="Direct substitution"),
    ]
    return _q("39_visual_l_shaped_gnomon_dot_pattern", 39, prompt, ans, steps,
              f"Each stage adds {arm_mult} dots to the arms while keeping the {corner} corner dots fixed.",
              "T_n = dn + c.",
              f"T_n = {arm_mult}n + {corner}, so T_{k} = {tk}.",
              ["double_counted_corner_dot_in_both_arms"], "easy", 3, _svg_spec(svg))


# 40. Visual discrete parabola coordinate plot (n; T_n) with seeded SVG
def build_40_visual_discrete_parabola_coordinate_plot(r: random.Random) -> Dict[str, Any]:
    a = r.choice([1, 2])
    b = r.randint(-3, 3)
    c = r.randint(1, 8)
    t = [a * n * n + b * n + c for n in range(1, 5)]
    tn_str = _fmt_quad(a, b, c)
    y_off = 125 - (c * 3)
    svg = (
        f'<svg viewBox="0 0 420 170" xmlns="http://www.w3.org/2000/svg">'
        f'<rect x="0" y="0" width="420" height="170" fill="#f8fafc" rx="8"/>'
        f'<line x1="50" y1="140" x2="380" y2="140" stroke="#334155" stroke-width="2"/>'
        f'<line x1="50" y1="20" x2="50" y2="140" stroke="#334155" stroke-width="2"/>'
        f'<circle cx="110" cy="{y_off}" r="5" fill="#dc2626"/>'
        f'<text x="110" y="{y_off-10}" font-size="11" font-family="sans-serif" fill="#0f172a" text-anchor="middle">(1; {t[0]})</text>'
        f'<circle cx="185" cy="{max(35, y_off - 15)}" r="5" fill="#dc2626"/>'
        f'<text x="185" y="{max(25, y_off - 25)}" font-size="11" font-family="sans-serif" fill="#0f172a" text-anchor="middle">(2; {t[1]})</text>'
        f'<circle cx="260" cy="{max(30, y_off - 35)}" r="5" fill="#dc2626"/>'
        f'<text x="260" y="{max(20, y_off - 45)}" font-size="11" font-family="sans-serif" fill="#0f172a" text-anchor="middle">(3; {t[2]})</text>'
        f'<circle cx="335" cy="{max(25, y_off - 60)}" r="5" fill="#dc2626"/>'
        f'<text x="335" y="{max(15, y_off - 70)}" font-size="11" font-family="sans-serif" fill="#0f172a" text-anchor="middle">(4; {t[3]})</text>'
        f'</svg>'
    )
    ans = f"T_n = {tn_str}"
    prompt = (
        f"Refer to the coordinate plot of the discrete points $(1; {t[0]})$, $(2; {t[1]})$, $(3; {t[2]})$, and $(4; {t[3]})$ "
        f"representing the first four terms $(n; T_n)$ of a quadratic sequence.\n\n"
        f"Determine the algebraic formula $T_n = an^2 + bn + c$."
    )
    steps = [
        step(from_latex=f"T_1 = {t[0]},\\; T_2 = {t[1]},\\; T_3 = {t[2]},\\; T_4 = {t[3]}", to_latex_str=f"2a = {2*a} \\implies a = {a}", op="Read terms from plotted points and find second difference", rule="2a = second difference"),
        step(from_latex=f"3({a}) + b = {t[1] - t[0]},\\quad {a} + b + c = {t[0]}", to_latex_str=ans, op="Solve for b and c", rule="Quadratic sequence coefficients"),
    ]
    return _q("40_visual_discrete_parabola_coordinate_plot", 40, prompt, ans, steps,
              f"Extract the sequence {t[0]}; {t[1]}; {t[2]}; {t[3]} from the y-coordinates of the plotted points.",
              "A quadratic sequence plotted against n lies on a discrete parabola T_n = an^2 + bn + c.",
              f"a = {a}, b = {b}, c = {c}, giving {ans}.",
              ["swapped_n_and_tn_coordinates_from_plot"], "medium", 4, _svg_spec(svg))


# 41. Visual triangular dots and connecting lines synthesis (Everything Maths Ch 3 capstone)
def build_41_visual_triangular_dots_and_connecting_lines_synthesis(r: random.Random) -> Dict[str, Any]:
    m_lines = r.choice([3, 5, 7])
    k = r.randint(10, 22)
    # Dots: n(n+1)/2, Lines: m_lines * n(n-1)/2
    # Total: [n^2 + n + m_lines*n^2 - m_lines*n]/2 = ((1+m_lines)/2)n^2 + ((1-m_lines)/2)n
    a = (1 + m_lines) // 2
    b = (1 - m_lines) // 2
    tn_str = _fmt_quad(a, b, 0)
    tk = a * k * k + b * k
    dots_3 = 6
    lines_3 = m_lines * 3
    tot_3 = dots_3 + lines_3
    svg = (
        f'<svg viewBox="0 0 420 140" xmlns="http://www.w3.org/2000/svg">'
        f'<rect x="0" y="0" width="420" height="140" fill="#f8fafc" rx="8"/>'
        f'<polygon points="80,35 50,90 110,90" fill="none" stroke="#475569" stroke-width="2"/>'
        f'<circle cx="80" cy="35" r="5" fill="#1e293b"/><circle cx="50" cy="90" r="5" fill="#1e293b"/><circle cx="110" cy="90" r="5" fill="#1e293b"/>'
        f'<text x="80" y="118" font-size="11" font-family="sans-serif" fill="#1e293b" text-anchor="middle">n=2: 3 dots, {m_lines} struts</text>'
        f'<polygon points="260,25 215,95 305,95" fill="none" stroke="#475569" stroke-width="2"/>'
        f'<line x1="237" y1="60" x2="283" y2="60" stroke="#475569" stroke-width="2"/>'
        f'<line x1="237" y1="60" x2="260" y2="95" stroke="#475569" stroke-width="2"/>'
        f'<line x1="283" y1="60" x2="260" y2="95" stroke="#475569" stroke-width="2"/>'
        f'<text x="260" y="118" font-size="11" font-family="sans-serif" fill="#1e293b" text-anchor="middle">n=3: 6 dots, {lines_3} struts (Total {tot_3})</text>'
        f'</svg>'
    )
    ans = f"T_n = {tn_str}; \\quad T_{{{k}}} = {tk}"
    prompt = (
        f"Refer to the diagram of the triangular truss network. "
        f"In Stage $n$, the number of joints (dots) is $\\frac{{n(n+1)}}{{2}}$ and the number of connecting struts is $\\frac{{{m_lines}n(n-1)}}{{2}}$.\n\n"
        f"Simplify the combined formula $T_n = \\frac{{n(n+1)}}{{2}} + \\frac{{{m_lines}n(n-1)}}{{2}}$ into the form $an^2 + bn$, and calculate the combined total for Stage ${k}$."
    )
    steps = [
        step(from_latex=f"T_n = \\frac{{n(n+1) + {m_lines}n(n-1)}}{{2}}", to_latex_str=f"T_n = \\frac{{(1 + {m_lines})n^2 + (1 - {m_lines})n}}{{2}} = {tn_str}", op="Combine over common denominator 2 and simplify like terms", rule="Algebraic fraction addition"),
        step(from_latex=f"n = {k}", to_latex_str=f"T_{{{k}}} = {a}({k})^2 + ({b})({k}) = {tk}", op=f"Evaluate at n = {k}", rule="Direct evaluation"),
    ]
    return _q("41_visual_triangular_dots_and_connecting_lines_synthesis", 41, prompt, ans, steps,
              f"Expand the numerators n^2 + n and {m_lines}n^2 - {m_lines}n over the common denominator 2.",
              "Add the two expressions over denominator 2 and simplify.",
              f"T_n = {tn_str} and T_{k} = {tk}.",
              ["sign_error_expanding_n_minus_1_numerator"], "hard", 4, _svg_spec(svg))


# 42. Context: round-robin tournament handshakes/games
def build_42_context_round_robin_tournament_handshakes(r: random.Random) -> Dict[str, Any]:
    m_times = r.choice([1, 2])
    n_teams = r.randint(8, 20)
    if m_times == 1:
        games = n_teams * (n_teams - 1) // 2
        formula_str = "\\frac{1}{2}n^2 - \\frac{1}{2}n"
        desc_str = "once"
    else:
        games = n_teams * (n_teams - 1)
        formula_str = "n^2 - n"
        desc_str = "twice (home and away)"
    ans = f"T_n = {formula_str}; \\quad n = {n_teams}\\text{{ teams}}"
    prompt = (
        f"In a sports league with $n$ teams, every team plays against every other team {desc_str}.\n\n"
        f"1. Write down the formula $T_n$ for the total number of matches played by $n$ teams.\n"
        f"2. If a total of ${games}$ matches were played in the season, determine the number of teams $n$ in the league."
    )
    steps = [
        step(from_latex=f"\\text{{Each of }} n \\text{{ teams plays }} (n - 1) \\text{{ opponents}}", to_latex_str=f"T_n = {formula_str}", op="Formulate quadratic match-count expression", rule="Combinatorial pairing"),
        step(from_latex=f"{formula_str} = {games}", to_latex_str=f"n(n - 1) = {n_teams * (n_teams - 1)} \\implies n = {n_teams}", op="Solve quadratic equation for positive integer n", rule="Quadratic equation in context"),
    ]
    return _q("42_context_round_robin_tournament_handshakes", 42, prompt, ans, steps,
              "Each of the n teams plays (n - 1) other teams.",
              "For single round-robin, divide n(n - 1) by 2 to avoid counting each match twice.",
              f"T_n = {formula_str}. Solving T_n = {games} gives n = {n_teams} teams.",
              ["forgot_to_divide_by_2_in_single_round_robin"], "medium", 4)


# 43. Context: stacked brick pyramid stages
def build_43_context_stacked_brick_pyramid_stages(r: random.Random) -> Dict[str, Any]:
    a = r.choice([1, 2, 3])
    b = r.randint(0, 5)
    c = r.randint(1, 8)
    k = r.randint(9, 16)
    terms = [a * n * n + b * n + c for n in range(1, 5)]
    tk = a * k * k + b * k + c
    tn_str = _fmt_quad(a, b, c)
    ans = f"T_n = {tn_str}; \\quad T_{{{k}}} = {tk}\\text{{ bricks}}"
    prompt = (
        f"An architectural brick display is built in stages. "
        f"Stages 1 to 4 contain ${terms[0]};\\; {terms[1]};\\; {terms[2]};\\; {terms[3]}$ bricks respectively.\n\n"
        f"Determine the general formula $T_n$ for the number of bricks in Stage $n$, and calculate how many bricks are needed for Stage ${k}$."
    )
    steps = [
        step(from_latex=f"{terms[0]}; {terms[1]}; {terms[2]}; {terms[3]}", to_latex_str=f"2a = {2*a} \\implies a = {a},\\; b = {b},\\; c = {c}", op="Use first and second differences to find a, b, c", rule="Quadratic pattern identification"),
        step(from_latex=f"T_n = {tn_str}", to_latex_str=f"T_{{{k}}} = {tk}", op=f"Substitute n = {k}", rule="Direct evaluation"),
    ]
    return _q("43_context_stacked_brick_pyramid_stages", 43, prompt, ans, steps,
              f"Calculate the first and second differences of {terms[0]}; {terms[1]}; {terms[2]}; {terms[3]} first.",
              "Since the second difference is constant, use T_n = an^2 + bn + c.",
              f"T_n = {tn_str} and T_{k} = {tk} bricks.",
              ["used_linear_formula_for_quadratic_brick_growth"], "medium", 4)


# 44. Context: auditorium seating rows pattern
def build_44_context_auditorium_seating_rows_pattern(r: random.Random) -> Dict[str, Any]:
    a1 = r.randint(18, 32)
    d = r.choice([2, 3, 4, 6])
    n_row = r.randint(14, 28)
    seats_n = a1 + (n_row - 1) * d
    c = a1 - d
    ans = f"T_n = {_fmt_linear(d, c)}; \\quad n = {n_row}"
    prompt = (
        f"A community theatre has ${a1}$ seats in Row 1, ${a1 + d}$ seats in Row 2, ${a1 + 2*d}$ seats in Row 3, and so on.\n\n"
        f"1. Write down the formula $T_n$ for the number of seats in Row $n$.\n"
        f"2. Which row contains exactly ${seats_n}$ seats?"
    )
    steps = [
        step(from_latex=f"a = {a1},\\; d = {d}", to_latex_str=f"T_n = {_fmt_linear(d, c)}", op="Derive linear seating formula", rule="T_n = a + (n - 1)d"),
        step(from_latex=f"{_fmt_linear(d, c)} = {seats_n}", to_latex_str=f"n = {n_row}", op="Solve for row number n", rule="Linear equation"),
    ]
    return _q("44_context_auditorium_seating_rows_pattern", 44, prompt, ans, steps,
              f"Each row adds d = {d} seats to the previous row.",
              "Use T_n = a + (n - 1)d and set T_n equal to the given seat count.",
              f"T_n = {_fmt_linear(d, c)} and Row {n_row} has {seats_n} seats.",
              ["off_by_one_row_index"], "easy", 3)


# 45. Classify sequence as linear, quadratic, or exponential
def build_45_classify_linear_quadratic_exponential_or_neither(r: random.Random) -> Dict[str, Any]:
    kind = r.choice(["linear", "quadratic", "exponential"])
    if kind == "linear":
        a1 = r.randint(3, 25)
        d = r.choice([-6, -4, 4, 5, 7, 9])
        terms = [a1 + i * d for i in range(5)]
        reason = f"\\text{{Linear (constant first difference }} d = {d}\\text{{)}}"
    elif kind == "quadratic":
        a = r.choice([1, 2, 3, 4])
        b = r.randint(-5, 5)
        c = r.randint(-8, 10)
        terms = [a * n * n + b * n + c for n in range(1, 6)]
        reason = f"\\text{{Quadratic (constant second difference }} 2a = {2*a}\\text{{)}}"
    else:
        a1 = r.choice([2, 3, 4, 5])
        ratio = r.choice([2, 3])
        terms = [a1 * (ratio ** i) for i in range(5)]
        reason = f"\\text{{Exponential / Geometric (constant ratio }} r = {ratio}\\text{{)}}"
    prompt = (
        f"Examine the sequence: ${terms[0]};\\; {terms[1]};\\; {terms[2]};\\; {terms[3]};\\; {terms[4]};\\; ...$\n\n"
        f"Classify the sequence as linear, quadratic, or exponential, and state the constant difference, second difference, or ratio that justifies your answer."
    )
    steps = [
        step(from_latex=f"{terms[0]}; {terms[1]}; {terms[2]}; {terms[3]}; {terms[4]}", to_latex_str="\\text{Test first differences, second differences, and ratios}", op="Check differences and ratios between consecutive terms", rule="Sequence classification"),
        step(from_latex=f"\\text{{Pattern type: }} {kind}", to_latex_str=reason, op="State classification with numeric justification", rule="Constant 1st diff vs 2nd diff vs ratio"),
    ]
    return _q("45_classify_linear_quadratic_exponential_or_neither", 45, prompt, reason, steps,
              "Test T2 - T1 vs T3 - T2 first; if not constant, check the second differences or the ratio T2 / T1.",
              "Linear: constant 1st difference. Quadratic: constant 2nd difference. Exponential: constant ratio.",
              reason,
              ["classified_exponential_as_quadratic_without_checking_third_difference"], "easy", 3)


# 46. Combined alternating odd and even sub-sequences
def build_46_combined_alternating_odd_even_sub_sequences(r: random.Random) -> Dict[str, Any]:
    # Odd positions (T1, T3, T5, ...): linear with d_odd
    a_odd = r.randint(2, 12)
    d_odd = r.choice([3, 4, 5, 6])
    # Even positions (T2, T4, T6, ...): k^2 + c_even
    c_even = r.randint(0, 8)
    odd_terms = [a_odd + i * d_odd for i in range(4)]
    even_terms = [(i + 1) ** 2 + c_even for i in range(4)]
    seq = [odd_terms[0], even_terms[0], odd_terms[1], even_terms[1], odd_terms[2], even_terms[2]]
    t7 = odd_terms[3]
    t8 = even_terms[3]
    ans = f"T_7 = {t7}, \\quad T_8 = {t8}"
    prompt = (
        f"Consider the combined alternating number pattern:\n\n"
        f"$${seq[0]}; \\quad {seq[1]}; \\quad {seq[2]}; \\quad {seq[3]}; \\quad {seq[4]}; \\quad {seq[5]}; \\quad ...$$\n\n"
        f"By separating the odd-positioned terms ($T_1; T_3; T_5; ...$) and the even-positioned terms ($T_2; T_4; T_6; ...$), "
        f"determine the next two terms $T_7$ and $T_8$."
    )
    steps = [
        step(from_latex=f"\\text{{Odd terms: }} {odd_terms[0]}; {odd_terms[1]}; {odd_terms[2]}", to_latex_str=f"d_{{\\text{{odd}}}} = {d_odd} \\implies T_7 = {odd_terms[2]} + {d_odd} = {t7}", op="Identify linear pattern in odd-positioned terms", rule="Odd sub-sequence"),
        step(from_latex=f"\\text{{Even terms: }} {even_terms[0]}; {even_terms[1]}; {even_terms[2]}", to_latex_str=f"k^2 + {c_even} \\implies T_8 = 4^2 + {c_even} = {t8}", op="Identify quadratic pattern in even-positioned terms", rule="Even sub-sequence"),
    ]
    return _q("46_combined_alternating_odd_even_sub_sequences", 46, prompt, ans, steps,
              "Split the sequence into two separate lists: positions 1, 3, 5, 7 and positions 2, 4, 6, 8.",
              "T7 is the 4th odd-positioned term and T8 is the 4th even-positioned term.",
              f"Odd terms add {d_odd} each step giving T7 = {t7}; even terms follow k^2 + {c_even} giving T8 = {t8}.",
              ["computed_consecutive_differences_across_interleaved_subsequences"], "hard", 4)


# 47. Algebraic derivation of first difference T_{n+1} - T_n
def build_47_algebraic_difference_T_n_plus_1_minus_T_n_derivation(r: random.Random) -> Dict[str, Any]:
    a = r.choice([-4, -3, -2, 2, 3, 4, 5])
    b = r.choice([-7, -5, -3, 3, 5, 7, 9])
    c = r.randint(-12, 12)
    tn_str = _fmt_quad(a, b, c)
    dn_str = _fmt_linear(2 * a, a + b)
    ans = f"T_{{n+1}} - T_n = {dn_str}"
    prompt = (
        f"Given the quadratic sequence with general term:\n\n"
        f"$$T_n = {tn_str}$$\n\n"
        f"Determine a simplified algebraic expression for the $n^{{\\text{{th}}}}$ first difference $T_{{n+1}} - T_n$ in terms of $n$."
    )
    steps = [
        step(from_latex=f"T_{{n+1}} = {a}(n+1)^2 + ({b})(n+1) + ({c})", to_latex_str=f"T_{{n+1}} = {a}n^2 + {2*a + b}n + ({a + b + c})", op="Substitute (n + 1) into T_n and expand", rule="Binomial expansion (n + 1)^2 = n^2 + 2n + 1"),
        step(from_latex=f"T_{{n+1}} - T_n", to_latex_str=ans, op="Subtract T_n and simplify to linear form 2an + (a + b)", rule="Algebraic first difference"),
    ]
    return _q("47_algebraic_difference_T_n_plus_1_minus_T_n_derivation", 47, prompt, ans, steps,
              "Replace n with (n + 1) to find T_(n+1), expand (n + 1)^2 = n^2 + 2n + 1, and subtract T_n.",
              "For T_n = an^2 + bn + c, T_{n+1} - T_n always simplifies to 2an + (a + b).",
              f"T_(n+1) - T_n = 2({a})n + ({a} + ({b})) = {dn_str}.",
              ["expanded_n_plus_1_squared_without_middle_2n_term"], "medium", 4)


# 48. First term in a quadratic sequence exceeding a threshold
def build_48_inequality_first_term_exceeding_threshold(r: random.Random) -> Dict[str, Any]:
    a = r.choice([1, 2, 3])
    b = r.randint(1, 6)
    c = r.randint(-10, 10)
    k = r.randint(8, 15)
    tk = a * k * k + b * k + c
    tk1 = a * (k + 1) * (k + 1) + b * (k + 1) + c
    thresh = tk + r.randint(1, max(1, tk1 - tk - 1))
    tn_str = _fmt_quad(a, b, c)
    ans = f"n = {k + 1} \\quad (T_{{{k+1}}} = {tk1} > {thresh})"
    prompt = (
        f"The general term of an increasing quadratic sequence (for $n \\ge 1$) is given by:\n\n"
        f"$$T_n = {tn_str}$$\n\n"
        f"Determine the position $n$ of the first term in the sequence whose value is strictly greater than ${thresh}$."
    )
    steps = [
        step(from_latex=f"{tn_str} > {thresh}", to_latex_str=f"T_{{{k}}} = {tk} \\le {thresh},\\quad T_{{{k+1}}} = {tk1} > {thresh}", op="Solve quadratic threshold and test adjacent natural numbers", rule="Discrete inequality on N"),
        step(from_latex=f"n \\in \\mathbb{{N}}", to_latex_str=ans, op="Select smallest integer n satisfying T_n > threshold", rule="Ceiling to next natural number"),
    ]
    return _q("48_inequality_first_term_exceeding_threshold", 48, prompt, ans, steps,
              f"Find where T_n = {thresh}, then round up to the next natural number n.",
              "Because n must be an integer, if T_k <= threshold < T_{k+1}, the first term exceeding the threshold is T_{k+1}.",
              f"Since T_{k} = {tk} and T_{k+1} = {tk1}, the first term greater than {thresh} is at n = {k+1}.",
              ["rounded_down_instead_of_up_for_threshold_inequality"], "hard", 4)


# 49. Diagnostic misconception analysis: setting a = second difference instead of 2a
def build_49_diagnostic_error_analysis_second_diff_equals_a_vs_2a(r: random.Random) -> Dict[str, Any]:
    a = r.choice([2, 3, 4, 5])
    b = r.randint(-5, 5)
    c = r.randint(-8, 8)
    terms = [a * n * n + b * n + c for n in range(1, 5)]
    d2 = 2 * a
    wrong_a = d2
    tn_str = _fmt_quad(a, b, c)
    ans = f"\\text{{Error: wrote }} a = {d2} \\text{{ instead of }} 2a = {d2}; \\quad \\text{{Correct: }} T_n = {tn_str}"
    prompt = (
        f"A learner is asked to find the general term of the quadratic sequence ${terms[0]};\\; {terms[1]};\\; {terms[2]};\\; {terms[3]};\\; ...$\n"
        f"The learner correctly finds the constant second difference as ${d2}$, but then writes $a = {wrong_a}$ as the first step.\n\n"
        f"Identify the learner's conceptual error and determine the correct general term $T_n$."
    )
    steps = [
        step(from_latex=f"\\text{{Learner wrote }} a = {d2}", to_latex_str=f"2a = {d2} \\implies a = {a}", op="Correct the misconception: second difference equals 2a, not a", rule="2a = second difference"),
        step(from_latex=f"3({a}) + b = {terms[1] - terms[0]},\\quad {a} + b + c = {terms[0]}", to_latex_str=ans, op="Calculate correct b, c, and general term T_n", rule="Quadratic sequence formula"),
    ]
    return _q("49_diagnostic_error_analysis_second_diff_equals_a_vs_2a", 49, prompt, ans, steps,
              "In a quadratic sequence, the constant second difference is 2a, so you must divide the second difference by 2 to get a.",
              "2a = second difference => a = (second difference) / 2.",
              f"2a = {d2} gives a = {a} (not {d2}). Correct formula: T_n = {tn_str}.",
              ["equated_a_directly_to_second_difference"], "medium", 4)


# 50. Compound NSC Exam Quadratic Pattern Synthesis with seeded SVG
def build_50_compound_nsc_exam_quadratic_pattern_synthesis(r: random.Random) -> Dict[str, Any]:
    a = r.choice([1, 2, 3])
    b = r.randint(-6, 6)
    c = r.randint(-10, 10)
    t = [a * n * n + b * n + c for n in range(1, 6)]
    d1 = [t[i + 1] - t[i] for i in range(4)]
    d2 = 2 * a
    k_diff = r.randint(10, 18)
    target_d = 2 * a * k_diff + (a + b)
    tn_str = _fmt_quad(a, b, c)
    w_col = 72 + (k_diff % 12)
    svg = (
        f'<svg viewBox="0 0 450 155" xmlns="http://www.w3.org/2000/svg">'
        f'<rect x="0" y="0" width="450" height="155" fill="#f8fafc" rx="8"/>'
        f'<rect x="20" y="20" width="410" height="36" fill="#dbeafe" rx="4"/>'
        f'<text x="65" y="43" font-size="12" font-family="sans-serif" font-weight="bold" fill="#1e3a8a" text-anchor="middle">T1 = {t[0]}</text>'
        f'<text x="{65+w_col}" y="43" font-size="12" font-family="sans-serif" font-weight="bold" fill="#1e3a8a" text-anchor="middle">T2 = {t[1]}</text>'
        f'<text x="{65+2*w_col}" y="43" font-size="12" font-family="sans-serif" font-weight="bold" fill="#1e3a8a" text-anchor="middle">T3 = {t[2]}</text>'
        f'<text x="{65+3*w_col}" y="43" font-size="12" font-family="sans-serif" font-weight="bold" fill="#1e3a8a" text-anchor="middle">T4 = {t[3]}</text>'
        f'<text x="{65+4*w_col}" y="43" font-size="12" font-family="sans-serif" font-weight="bold" fill="#1d4ed8" text-anchor="middle">T5 = ?</text>'
        f'<text x="{100}" y="88" font-size="12" font-family="sans-serif" fill="#0369a1" text-anchor="middle">D1 = {d1[0]}</text>'
        f'<text x="{100+w_col}" y="88" font-size="12" font-family="sans-serif" fill="#0369a1" text-anchor="middle">D2 = {d1[1]}</text>'
        f'<text x="{100+2*w_col}" y="88" font-size="12" font-family="sans-serif" fill="#0369a1" text-anchor="middle">D3 = {d1[2]}</text>'
        f'<text x="{135}" y="130" font-size="12" font-family="sans-serif" font-weight="bold" fill="#15803d" text-anchor="middle">2nd diff = {d2}</text>'
        f'<text x="{135+w_col}" y="130" font-size="12" font-family="sans-serif" font-weight="bold" fill="#15803d" text-anchor="middle">2nd diff = {d2}</text>'
        f'</svg>'
    )
    ans = f"T_5 = {t[4]}; \\quad T_n = {tn_str}; \\quad \\text{{Between }} T_{{{k_diff}}} \\text{{ and }} T_{{{k_diff+1}}}"
    prompt = (
        f"Refer to the quadratic sequence summary chart for ${t[0]};\\; {t[1]};\\; {t[2]};\\; {t[3]};\\; ...$\n\n"
        f"1. Write down the value of $T_5$.\n"
        f"2. Determine the general term $T_n$ in the form $T_n = an^2 + bn + c$.\n"
        f"3. Determine between which two consecutive terms the first difference is equal to ${target_d}$."
    )
    steps = [
        step(from_latex=f"D_4 = {d1[2]} + {d2} = {d1[3]}", to_latex_str=f"T_5 = {t[3]} + ({d1[3]}) = {t[4]}", op="Calculate fourth first difference and T5", rule="Recursive quadratic step"),
        step(from_latex=f"2a = {d2},\\; 3a + b = {d1[0]},\\; a + b + c = {t[0]}", to_latex_str=f"T_n = {tn_str}", op="Solve for a, b, and c to obtain T_n", rule="Quadratic general formula"),
        step(from_latex=f"D_n = {_fmt_linear(2*a, a+b)} = {target_d}", to_latex_str=f"n = {k_diff} \\implies T_{{{k_diff}}} \\text{{ and }} T_{{{k_diff+1}}}", op="Solve first difference equation for n", rule="Linear sequence of first differences"),
    ]
    return _q("50_compound_nsc_exam_quadratic_pattern_synthesis", 50, prompt, ans, steps,
              f"Find T5 using D4 = {d1[3]}, then solve 2a = {d2}, 3a + b = {d1[0]}, a + b + c = {t[0]}.",
              "Combine quadratic general term derivation with the linear formula D_n = 2an + (a + b) for the first differences.",
              ans,
              ["equated_tn_to_target_difference_instead_of_dn"], "hard", 6, _svg_spec(svg))


BUILDERS_26_50: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    "26_quadratic_first_differences_as_linear_sequence": build_26_quadratic_first_differences_as_linear_sequence,
    "27_quadratic_consecutive_terms_from_given_first_difference": build_27_quadratic_consecutive_terms_from_given_first_difference,
    "28_quadratic_reconstruct_sequence_from_first_diff_formula": build_28_quadratic_reconstruct_sequence_from_first_diff_formula,
    "29_quadratic_unknown_variable_x_from_equal_second_differences": build_29_quadratic_unknown_variable_x_from_equal_second_differences,
    "30_quadratic_missing_middle_terms_in_sequence": build_30_quadratic_missing_middle_terms_in_sequence,
    "31_quadratic_minimum_value_via_completing_square": build_31_quadratic_minimum_value_via_completing_square,
    "32_quadratic_maximum_value_negative_a_turning_point": build_32_quadratic_maximum_value_negative_a_turning_point,
    "33_quadratic_closest_integer_term_non_integer_axis": build_33_quadratic_closest_integer_term_non_integer_axis,
    "34_quadratic_simultaneous_equations_from_three_given_terms": build_34_quadratic_simultaneous_equations_from_three_given_terms,
    "35_quadratic_find_term_from_ratio_or_sum_condition": build_35_quadratic_find_term_from_ratio_or_sum_condition,
    "36_visual_triangular_dot_array_pattern": build_36_visual_triangular_dot_array_pattern,
    "37_visual_square_grid_matchstick_pattern": build_37_visual_square_grid_matchstick_pattern,
    "38_visual_bordered_tile_frame_pattern": build_38_visual_bordered_tile_frame_pattern,
    "39_visual_l_shaped_gnomon_dot_pattern": build_39_visual_l_shaped_gnomon_dot_pattern,
    "40_visual_discrete_parabola_coordinate_plot": build_40_visual_discrete_parabola_coordinate_plot,
    "41_visual_triangular_dots_and_connecting_lines_synthesis": build_41_visual_triangular_dots_and_connecting_lines_synthesis,
    "42_context_round_robin_tournament_handshakes": build_42_context_round_robin_tournament_handshakes,
    "43_context_stacked_brick_pyramid_stages": build_43_context_stacked_brick_pyramid_stages,
    "44_context_auditorium_seating_rows_pattern": build_44_context_auditorium_seating_rows_pattern,
    "45_classify_linear_quadratic_exponential_or_neither": build_45_classify_linear_quadratic_exponential_or_neither,
    "46_combined_alternating_odd_even_sub_sequences": build_46_combined_alternating_odd_even_sub_sequences,
    "47_algebraic_difference_T_n_plus_1_minus_T_n_derivation": build_47_algebraic_difference_T_n_plus_1_minus_T_n_derivation,
    "48_inequality_first_term_exceeding_threshold": build_48_inequality_first_term_exceeding_threshold,
    "49_diagnostic_error_analysis_second_diff_equals_a_vs_2a": build_49_diagnostic_error_analysis_second_diff_equals_a_vs_2a,
    "50_compound_nsc_exam_quadratic_pattern_synthesis": build_50_compound_nsc_exam_quadratic_pattern_synthesis,
}
