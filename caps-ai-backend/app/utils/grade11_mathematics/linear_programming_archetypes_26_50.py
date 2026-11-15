"""Grade 11 Mathematics — Linear Programming & Investigations (Archetypes 26 to 50).
Aligned with South African National Curriculum Standards.
Reference: curriculum_docs_auto/Mathematics_Gr11/Term 1/01. Linear programming.md

Covers:
- Objective function evaluation, search-line gradient method, and corner-point theorem (26..38)
- Applied optimisation models, mathematical investigations, sensitivity analysis, and diagnostic autopsy (39..50)
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional, Tuple

from .linear_programming_archetypes_01_25 import (
    _fmt,
    _make_q,
    _svg_lp_quad_region,
    _svg_single_line_region,
)


# 26. Evaluate objective function at given feasible vertices (with SVG)
def build_26_evaluate_objective_function_at_given_feasible_vertices_svg(r: random.Random) -> Dict[str, Any]:
    ix = r.randint(4, 9)
    iy = r.randint(3, 8)
    if ix % 2 != iy % 2:
        iy += 1
    c1 = ix + iy
    c2 = 2 * ix + iy
    x_int_2 = c2 // 2
    px = r.randint(2, 6) * 100
    py = r.randint(2, 5) * 100
    pb = py * c1
    pc = px * ix + py * iy
    pd = px * x_int_2
    svg = _svg_lp_quad_region(c1, c1, c2, x_int_2, ix, iy, "Corner Point Evaluation", search_m=(px, py))
    prompt = (
        f"The feasible region shown in the diagram has corner vertices $A(0; 0)$, $B(0; {c1})$, $C({ix}; {iy})$, and $D({x_int_2}; 0)$.\n\n"
        f"Evaluate the objective function $P = {px}x + {py}y$ at each of the non-zero vertices $B$, $C$, and $D$."
    )
    ans = f"P(B) = \\text{{R }}{pb},\\ P(C) = \\text{{R }}{pc},\\ P(D) = \\text{{R }}{pd}"
    sol = (
        f"• At $B(0; {c1})$: $P = {px}(0) + {py}({c1}) = \\text{{R }}{pb}$.\n"
        f"• At $C({ix}; {iy})$: $P = {px}({ix}) + {py}({iy}) = {px * ix} + {py * iy} = \\text{{R }}{pc}$.\n"
        f"• At $D({x_int_2}; 0)$: $P = {px}({x_int_2}) + {py}(0) = \\text{{R }}{pd}$."
    )
    return _make_q(
        r, "26_evaluate_objective_function_at_given_feasible_vertices_svg", 26, prompt, ans, sol, 3,
        ["arithmetic_error_in_profit_evaluation"],
        [{"step": 1, "criterion": f"P(B) = R{pb}", "marks": 1}, {"step": 2, "criterion": f"P(C) = R{pc}", "marks": 1}, {"step": 3, "criterion": f"P(D) = R{pd}", "marks": 1}],
        {"tier_1": "Substitute the coordinates (x; y) of each vertex into P = ax + by.", "tier_2": f"B: {py}*{c1}; C: {px}*{ix} + {py}*{iy}; D: {px}*{x_int_2}.", "tier_3": ans},
        svg=svg,
    )


# 27. Maximise profit using corner point theorem (with SVG)
def build_27_maximise_profit_using_corner_point_theorem_svg(r: random.Random) -> Dict[str, Any]:
    ix = r.randint(4, 10)
    iy = r.randint(4, 10)
    if ix % 2 != iy % 2:
        iy += 1
    c1 = ix + iy
    c2 = 2 * ix + iy
    x_int_2 = c2 // 2
    # Choose px, py so that (ix, iy) is strictly optimal:
    # Gradient of P: -px/py lies strictly between -2 and -1 => py < px < 2*py
    py = r.randint(2, 6) * 100
    px = py + r.randint(1, py // 100 - 1) * 100
    max_p = px * ix + py * iy
    svg = _svg_lp_quad_region(c1, c1, c2, x_int_2, ix, iy, "Profit Maximisation", search_m=(px, py))
    prompt = (
        f"A feasible region $S$ (shown in the diagram) has vertices $(0; 0)$, $(0; {c1})$, $({ix}; {iy})$, and $({x_int_2}; 0)$.\n"
        f"The profit equation is $P = {px}x + {py}y$ (in Rands).\n\n"
        f"Determine the coordinates $(x; y)$ that **maximise** $P$ and state the **maximum profit**."
    )
    ans = f"({ix}; {iy}),\\ P_{{\\max}} = \\text{{R }}{max_p}"
    sol = (
        f"Test corner points:\n"
        f"• $(0; {c1}) \\implies P = \\text{{R }}{py * c1}$\n"
        f"• $({ix}; {iy}) \\implies P = {px}({ix}) + {py}({iy}) = \\text{{R }}{max_p}$\n"
        f"• $({x_int_2}; 0) \\implies P = \\text{{R }}{px * x_int_2}$\n"
        f"Maximum profit is $\\text{{R }}{max_p}$ at $({ix}; {iy})$."
    )
    return _make_q(
        r, "27_maximise_profit_using_corner_point_theorem_svg", 27, prompt, ans, sol, 4,
        ["tested_interior_point_instead_of_vertex"],
        [{"step": 1, "criterion": "Evaluate P at all corners", "marks": 2}, {"step": 2, "criterion": f"Optimal vertex ({ix}; {iy})", "marks": 1}, {"step": 3, "criterion": f"Max profit R{max_p}", "marks": 1}],
        {"tier_1": "Evaluate P at (0; c1), (ix; iy), and (x_int; 0) and select the largest value.", "tier_2": f"At ({ix}; {iy}), P = {px}*{ix} + {py}*{iy} = R{max_p}.", "tier_3": ans},
        svg=svg,
    )


# 28. Minimise cost using corner point theorem (with SVG)
def build_28_minimise_cost_using_corner_point_theorem_svg(r: random.Random) -> Dict[str, Any]:
    ix = r.randint(4, 9)
    iy = r.randint(4, 9)
    if ix % 2 != iy % 2:
        iy += 1
    c1 = ix + iy
    c2 = 2 * ix + iy
    cy = r.randint(2, 5) * 100
    cx = cy + r.randint(1, cy // 100 - 1) * 100
    min_c = cx * ix + cy * iy
    svg = _svg_lp_quad_region(c1, c1, c2, c2 // 2, ix, iy, "Cost Minimisation Boundary", search_m=(cx, cy))
    prompt = (
        f"An unbounded feasible region for a cost-minimisation model has lower boundary corner points "
        f"$A(0; {c2})$, $B({ix}; {iy})$, and $C({c1}; 0)$ (as indicated on the boundary graph).\n"
        f"The cost function is $C = {cx}x + {cy}y$ (in Rands).\n\n"
        f"Calculate the cost at each corner point and state the **minimum cost** and optimal pair $(x; y)$."
    )
    ans = f"({ix}; {iy}),\\ C_{{\\min}} = \\text{{R }}{min_c}"
    sol = (
        f"• At $A(0; {c2})$: $C = {cy}({c2}) = \\text{{R }}{cy * c2}$.\n"
        f"• At $B({ix}; {iy})$: $C = {cx}({ix}) + {cy}({iy}) = \\text{{R }}{min_c}$.\n"
        f"• At $C({c1}; 0)$: $C = {cx}({c1}) = \\text{{R }}{cx * c1}$.\n"
        f"Minimum cost is $\\text{{R }}{min_c}$ at $B({ix}; {iy})$."
    )
    return _make_q(
        r, "28_minimise_cost_using_corner_point_theorem_svg", 28, prompt, ans, sol, 4,
        ["selected_maximum_value_when_asked_for_minimum_cost"],
        [{"step": 1, "criterion": f"C(A) = R{cy * c2} and C(C) = R{cx * c1}", "marks": 2}, {"step": 2, "criterion": f"C(B) = R{min_c}", "marks": 1}, {"step": 3, "criterion": f"Minimum at ({ix}; {iy})", "marks": 1}],
        {"tier_1": "Evaluate C at each of the three lower-border vertices A, B, and C.", "tier_2": f"Compare R{cy * c2}, R{min_c}, and R{cx * c1}; choose the smallest.", "tier_3": ans},
        svg=svg,
    )


# 29. Gradient of search line from objective function (with SVG)
def build_29_gradient_of_search_line_from_objective_function_svg(r: random.Random) -> Dict[str, Any]:
    a_v = r.randint(2, 9) * 50
    b_v = r.randint(2, 9) * 50
    while a_v == b_v:
        b_v = r.randint(2, 9) * 50
    g = math.gcd(a_v, b_v)
    num_m = a_v // g
    den_m = b_v // g
    svg = _svg_lp_quad_region(10, 10, 14, 7, 4, 6, f"Search Line P = {a_v}x + {b_v}y", search_m=(num_m, den_m))
    prompt = (
        f"An objective function is given by $P = {a_v}x + {b_v}y$, represented by the dashed search line in the diagram.\n\n"
        f"Rearrange the equation into the form $y = mx + c$ and state the simplified exact gradient $m$ of the search line."
    )
    ans = f"m = -\\frac{{{num_m}}}{{{den_m}}}"
    sol = f"${b_v}y = -{a_v}x + P \\implies y = -\\frac{{{a_v}}}{{{b_v}}}x + \\frac{{P}}{{{b_v}}} = -\\frac{{{num_m}}}{{{den_m}}}x + \\frac{{P}}{{{b_v}}}$. Thus $m = -\\frac{{{num_m}}}{{{den_m}}}$."
    return _make_q(
        r, "29_gradient_of_search_line_from_objective_function_svg", 29, prompt, ans, sol, 2,
        ["omitted_negative_sign_in_search_line_gradient", "inverted_search_line_gradient_b_over_a"],
        [{"step": 1, "criterion": f"y = -({a_v}/{b_v})x + P/{b_v}", "marks": 1}, {"step": 2, "criterion": f"m = -{num_m}/{den_m}", "marks": 1}],
        {"tier_1": f"Make y the subject of P = {a_v}x + {b_v}y.", "tier_2": f"Gradient m = -{a_v}/{b_v}, simplified by dividing by {g}.", "tier_3": ans},
        svg=svg,
    )


# 30. Search line sliding direction for maximum vs minimum (with SVG)
def build_30_search_line_sliding_direction_for_maximum_vs_minimum_svg(r: random.Random) -> Dict[str, Any]:
    px = r.randint(2, 8) * 100
    py = r.randint(2, 8) * 100
    ix = r.randint(3, 8)
    iy = r.randint(3, 8)
    c1 = ix + iy
    c2 = 2 * ix + iy
    svg = _svg_lp_quad_region(c1, c1, c2, c2 // 2, ix, iy, "Sliding the Search Line", search_m=(px, py))
    prompt = (
        f"The objective function $P = {px}x + {py}y$ can be written as $y = -\\frac{{{px}}}{{{py}}}x + \\frac{{P}}{{{py}}}$, as shown on the diagram.\n\n"
        f"Explain how the $y$-intercept $\\frac{{P}}{{{py}}}$ changes as the search line is slid **upwards/rightwards** away from the origin $(0; 0)$, "
        f"and state what value of $P$ corresponds to a search line $y$-intercept of $c = {c1}$."
    )
    ans = f"\\text{{Increases (maximises }} P\\text{{)}};\\quad P = \\text{{R }}{py * c1}"
    sol = (
        f"Since $y\\text{{-intercept}} = \\frac{{P}}{{{py}}}$ and ${py} > 0$, sliding the search line upwards increases the $y$-intercept and therefore **maximises** $P$.\n"
        f"When the $y$-intercept is ${c1}$, $\\frac{{P}}{{{py}}} = {c1} \\implies P = {py} \\times {c1} = \\text{{R }}{py * c1}$."
    )
    return _make_q(
        r, "30_search_line_sliding_direction_for_maximum_vs_minimum_svg", 30, prompt, ans, sol, 3,
        ["slid_search_line_towards_origin_for_maximisation"],
        [{"step": 1, "criterion": "Sliding upwards increases y-intercept and P", "marks": 1}, {"step": 2, "criterion": f"P/{py} = {c1} => P = R{py * c1}", "marks": 2}],
        {"tier_1": f"Notice that the y-intercept of the search line is P / {py}.", "tier_2": f"Set P / {py} = {c1} and solve for P.", "tier_3": ans},
        svg=svg,
    )


# 31. Find optimal vertex using search line gradient comparison (with SVG)
def build_31_find_optimal_vertex_using_search_line_gradient_comparison_svg(r: random.Random) -> Dict[str, Any]:
    ix = r.randint(4, 10)
    iy = r.randint(4, 10)
    if ix % 2 != iy % 2:
        iy += 1
    c1 = ix + iy
    c2 = 2 * ix + iy
    # Line 1: x + y = c1 (m1 = -1). Line 2: 2x + y = c2 (m2 = -2).
    # Pick search line steeper than -2 (e.g. m = -3) or flatter than -1 (e.g. m = -1/2) or between (-3/2)
    case = r.choice(["between", "flatter", "steeper"])
    if case == "between":
        px, py = 300, 200
        opt_pt = f"C({ix}; {iy})"
    elif case == "flatter":
        px, py = 100, 200
        opt_pt = f"B(0; {c1})"
    else:
        px, py = 300, 100
        opt_pt = f"D({c2 // 2}; 0)"
    svg = _svg_lp_quad_region(c1, c1, c2, c2 // 2, ix, iy, "Search Line Gradient Comparison", search_m=(px // 100, py // 100))
    prompt = (
        f"The feasible region in the diagram is bounded by $L_1: x + y = {c1}$ ($m_1 = -1$) and $L_2: 2x + y = {c2}$ ($m_2 = -2$), "
        f"with vertices $B(0; {c1})$, $C({ix}; {iy})$, and $D({c2 // 2}; 0)$.\n\n"
        f"By comparing the gradient of the search line for $P = {px}x + {py}y$ with $m_1$ and $m_2$, identify which vertex maximises $P$."
    )
    ans = f"{opt_pt}"
    sol = (
        f"Search line gradient $m_P = -\\frac{{{px}}}{{{py}}}$. Comparing $m_P$ with $m_1 = -1$ and $m_2 = -2$ shows the last point of contact "
        f"when sliding outwards is **{opt_pt}**."
    )
    return _make_q(
        r, "31_find_optimal_vertex_using_search_line_gradient_comparison_svg", 31, prompt, ans, sol, 3,
        ["failed_to_compare_search_line_slope_with_boundary_slopes"],
        [{"step": 1, "criterion": f"Search gradient m_P = -{px}/{py}", "marks": 1}, {"step": 2, "criterion": f"Optimal vertex {opt_pt}", "marks": 2}],
        {"tier_1": "Find the gradient of the search line m_P = -px/py and compare with -1 and -2.", "tier_2": "You can also verify by substituting B, C, and D into P.", "tier_3": ans},
        svg=svg,
    )


# 32. Multiple optimal solutions along parallel boundary edge (with SVG)
def build_32_multiple_optimal_solutions_along_parallel_boundary_edge_svg(r: random.Random) -> Dict[str, Any]:
    ix = r.randint(4, 8)
    iy = r.randint(4, 8)
    if ix % 2 != iy % 2:
        iy += 1
    c1 = ix + iy
    c2 = 2 * ix + iy
    mult = r.randint(2, 6) * 100
    # Make P parallel to x + y = c1: P = mult*x + mult*y
    max_p = mult * c1
    n_int_pts = ix + 1  # x = 0, 1, ..., ix along segment from (0, c1) to (ix, iy)
    svg = _svg_lp_quad_region(c1, c1, c2, c2 // 2, ix, iy, "Parallel Search Line & Multiple Optima", search_m=(1, 1))
    prompt = (
        f"In the feasible region shown in the diagram, the upper boundary edge joining $B(0; {c1})$ and $C({ix}; {iy})$ lies on the line $x + y = {c1}$.\n"
        f"The profit function is $P = {mult}x + {mult}y$.\n\n"
        f"Explain why $B$ and $C$ yield the **same** maximum profit $\\text{{R }}{max_p}$, and determine how many **integer points** along segment $BC$ achieve this maximum."
    )
    ans = f"{n_int_pts}\\text{{ integer points }};\\ P_{{\\max}} = \\text{{R }}{max_p}"
    sol = (
        f"The search line $P = {mult}x + {mult}y$ has gradient $m = -1$, which is **parallel** to the boundary edge $x + y = {c1}$.\n"
        f"Every integer point $(x; {c1} - x)$ for $x \\in \\{{0, 1, \\dots, {ix}\\}}$ lies on $BC$, giving **${n_int_pts}$** optimal integer solutions with $P = \\text{{R }}{max_p}$."
    )
    return _make_q(
        r, "32_multiple_optimal_solutions_along_parallel_boundary_edge_svg", 32, prompt, ans, sol, 3,
        ["missed_alternative_integer_optima_on_parallel_boundary"],
        [{"step": 1, "criterion": "Search line gradient m = -1 equals boundary gradient", "marks": 1}, {"step": 2, "criterion": f"{n_int_pts} integer points for x = 0..{ix}", "marks": 2}],
        {"tier_1": "Compare the gradient of the objective function with the gradient of segment BC.", "tier_2": f"Since x can take any integer value from 0 to {ix} along x + y = {c1}, count 0..{ix}.", "tier_3": ans},
        svg=svg,
    )


# 33. Integer lattice optimisation when vertex is non-integral (with SVG)
def build_33_integer_lattice_optimisation_when_vertex_is_non_integral_svg(r: random.Random) -> Dict[str, Any]:
    # 2x + y <= c2 and x + 2y <= c1 with odd sum so intersection is half-integer
    k = r.randint(3, 7)
    # Let 2x + y <= 3k + 1 and x + 2y <= 3k + 1 => intersection (k + 1/3, k + 1/3)
    c_val = 3 * k + 1
    # For integer x, y with x + y maximized: if x = k, y = k, 2k + k = 3k <= 3k + 1 (valid!)
    # If x = k+1, y = k: 2(k+1) + k = 3k + 2 > 3k + 1 (invalid!). So max integer x + y is 2k at (k; k).
    px = r.randint(2, 5) * 100
    max_int_p = px * (2 * k)
    svg = _svg_lp_quad_region(c_val // 2, c_val, c_val, c_val // 2, k, k, "Non-Integral Vertex Lattice Search")
    prompt = (
        f"A feasible region (illustrated in the diagram) is defined for **integer** variables $x, y \\in \\mathbb{{Z}}_0^+$ by:\n"
        f"$$2x + y \\le {c_val},\\quad x + 2y \\le {c_val},\\quad x \\ge 0,\\quad y \\ge 0$$\n\n"
        f"1. Show that the continuous intersection point of the two boundary lines is non-integral: $\\left(\\frac{{{c_val}}}{{3}}; \\frac{{{c_val}}}{{3}}\\right)$.\n"
        f"2. Find the feasible **integer** point $(x; y)$ that maximises $P = {px}x + {px}y$ and state the maximum integer profit."
    )
    ans = f"({k}; {k}),\\ P_{{\\max}} = \\text{{R }}{max_int_p}"
    sol = (
        f"1. Adding the equations gives $3(x + y) = {2 * c_val} \\implies x = y = \\frac{{{c_val}}}{{3}} = {k}{{,}}33$, which is not an integer.\n"
        f"2. Since $3(x + y) \\le {2 * c_val} = {6 * k + 2}$ and $x + y$ is an integer, $x + y \\le {2 * k}$. "
        f"Testing $({k}; {k})$: $2({k}) + {k} = {3 * k} \\le {c_val}$ (valid). Thus optimal integer point is $({k}; {k})$ with $P = \\text{{R }}{max_int_p}$."
    )
    return _make_q(
        r, "33_integer_lattice_optimisation_when_vertex_is_non_integral_svg", 33, prompt, ans, sol, 4,
        ["accepted_fractional_vertex_for_discrete_integer_items"],
        [{"step": 1, "criterion": f"Continuous vertex ({c_val}/3; {c_val}/3)", "marks": 1}, {"step": 2, "criterion": f"Optimal integer point ({k}; {k})", "marks": 2}, {"step": 3, "criterion": f"Max profit R{max_int_p}", "marks": 1}],
        {"tier_1": "Add the two inequalities: 3x + 3y <= 2*c_val.", "tier_2": f"Divide by 3: x + y <= {2 * c_val}/3 = {2 * k}.67, so max integer x + y is {2 * k} at ({k}; {k}).", "tier_3": ans},
        svg=svg,
    )


# 34. Find unknown profit coefficient given optimal edge gradient
def build_34_find_unknown_profit_coefficient_given_optimal_edge_gradient(r: random.Random) -> Dict[str, Any]:
    a_v = r.randint(2, 6)
    b_v = r.randint(2, 6)
    mult = r.randint(20, 60)
    py = b_v * mult
    px = a_v * mult
    c_v = a_v * b_v * 3
    prompt = (
        f"In a linear programming problem, one of the active boundary constraints is ${a_v}x + {b_v}y \\le {c_v}$.\n"
        f"The profit function is $P = kx + {py}y$, where $k > 0$.\n\n"
        f"Calculate the value of $k$ if the objective function reaches its maximum at **every point** along the boundary segment ${a_v}x + {b_v}y = {c_v}$."
    )
    ans = f"k = {px}"
    sol = (
        f"For multiple optima along the boundary segment, the search line gradient must equal the boundary gradient:\n"
        f"$-\\frac{{k}}{{{py}}} = -\\frac{{{a_v}}}{{{b_v}}} \\implies k = \\frac{{{a_v} \\times {py}}}{{{b_v}}} = {px}$."
    )
    return _make_q(
        r, "34_find_unknown_profit_coefficient_given_optimal_edge_gradient", 34, prompt, ans, sol, 3,
        ["equated_gradients_with_wrong_ratio_inversion"],
        [{"step": 1, "criterion": f"Boundary gradient = -{a_v}/{b_v}", "marks": 1}, {"step": 2, "criterion": f"Equate -k/{py} = -{a_v}/{b_v}", "marks": 1}, {"step": 3, "criterion": f"k = {px}", "marks": 1}],
        {"tier_1": "Equate the gradient of the profit function (-k / py) to the gradient of the boundary line (-a / b).", "tier_2": f"k / {py} = {a_v} / {b_v}.", "tier_3": ans},
    )


# 35. Range of profit ratio preserving current optimal vertex
def build_35_range_of_profit_ratio_preserving_current_optimal_vertex(r: random.Random) -> Dict[str, Any]:
    a1 = r.randint(1, 3)
    b1 = r.randint(3, 6)
    a2 = r.randint(4, 8)
    b2 = r.randint(1, 3)
    # m1 = -a1/b1 (flatter), m2 = -a2/b2 (steeper)
    py = b1 * b2 * 10
    k_min = (a1 * py) // b1
    k_max = (a2 * py) // b2
    prompt = (
        f"Two boundary constraints intersect at the optimal vertex $C$: Constraint 1 is ${a1}x + {b1}y \\le {a1 * b1 * 4}$ "
        f"and Constraint 2 is ${a2}x + {b2}y \\le {a2 * b2 * 4}$.\n"
        f"The profit function is $P = kx + {py}y$.\n\n"
        f"Determine the closed interval of values of $k$ for which vertex $C$ remains an optimal solution."
    )
    ans = f"{k_min} \\le k \\le {k_max}"
    sol = (
        f"The gradient of the objective function $m_P = -\\frac{{k}}{{{py}}}$ must lie between the two boundary gradients "
        f"$m_2 = -\\frac{{{a2}}}{{{b2}}}$ and $m_1 = -\\frac{{{a1}}}{{{b1}}}$:\n"
        f"$\\frac{{{a1}}}{{{b1}}} \\le \\frac{{k}}{{{py}}} \\le \\frac{{{a2}}}{{{b2}}} \\implies {k_min} \\le k \\le {k_max}$."
    )
    return _make_q(
        r, "35_range_of_profit_ratio_preserving_current_optimal_vertex", 35, prompt, ans, sol, 3,
        ["reversed_inequality_bounds_when_multiplying_by_negative_gradient"],
        [{"step": 1, "criterion": f"Boundary slopes -{a1}/{b1} and -{a2}/{b2}", "marks": 1}, {"step": 2, "criterion": f"Lower bound k >= {k_min}", "marks": 1}, {"step": 3, "criterion": f"Upper bound k <= {k_max}", "marks": 1}],
        {"tier_1": "The search line slope -k/py must lie between the slopes of the two intersecting constraints.", "tier_2": f"{a1}/{b1} <= k/{py} <= {a2}/{b2}.", "tier_3": ans},
    )


# 36. Calculate slack and surplus resources at optimal point
def build_36_calculate_slack_and_surplus_resources_at_optimal_point(r: random.Random) -> Dict[str, Any]:
    ix = r.randint(5, 12)
    iy = r.randint(4, 10)
    c1 = 2 * ix + iy  # binding constraint (slack = 0)
    slack_val = r.randint(6, 20)
    c2 = ix + 3 * iy + slack_val  # non-binding constraint
    prompt = (
        f"At the optimal production point $({ix}; {iy})$, a factory faces two resource constraints:\n"
        f"• Assembly time: $2x + y \\le {c1}\\text{{ hours}}$\n"
        f"• Packaging time: $x + 3y \\le {c2}\\text{{ hours}}$\n\n"
        f"Calculate the **unused (slack) hours** in each department at the optimal point $({ix}; {iy})$, and state which constraint is **binding**."
    )
    ans = f"\\text{{Assembly slack}} = 0\\text{{ h (binding)}};\\ \\text{{Packaging slack}} = {slack_val}\\text{{ h}}"
    sol = (
        f"• Assembly used: $2({ix}) + {iy} = {c1}\\text{{ h}} \\implies \\text{{slack}} = {c1} - {c1} = 0\\text{{ h}}$ (**binding**).\n"
        f"• Packaging used: ${ix} + 3({iy}) = {ix + 3 * iy}\\text{{ h}} \\implies \\text{{slack}} = {c2} - {ix + 3 * iy} = {slack_val}\\text{{ h}}$."
    )
    return _make_q(
        r, "36_calculate_slack_and_surplus_resources_at_optimal_point", 36, prompt, ans, sol, 3,
        ["confused_binding_constraint_with_slack_constraint"],
        [{"step": 1, "criterion": "Assembly slack = 0 h (binding)", "marks": 1}, {"step": 2, "criterion": f"Packaging used = {ix + 3 * iy} h", "marks": 1}, {"step": 3, "criterion": f"Packaging slack = {slack_val} h", "marks": 1}],
        {"tier_1": "Substitute (x; y) into each constraint's LHS and subtract from the available RHS.", "tier_2": "A constraint with 0 slack is called binding.", "tier_3": ans},
    )


# 37. Shadow price / marginal value of additional resource unit
def build_37_shadow_price_marginal_value_of_additional_resource_unit(r: random.Random) -> Dict[str, Any]:
    ix = r.randint(4, 10)
    iy = r.randint(4, 10)
    c1 = ix + iy
    c2 = 2 * ix + iy
    px = r.randint(3, 7) * 100
    py = r.randint(2, 5) * 100
    # At (ix, iy): x = c2 - c1, y = 2*c1 - c2.
    # If c1 increases by 1 (to c1 + 1), new x' = ix - 1, new y' = iy + 2.
    # Change in P = px*(-1) + py*(+2) = 2*py - px
    while 2 * py <= px:
        py += 100
    p_old = px * ix + py * iy
    p_new = px * (ix - 1) + py * (iy + 2)
    shadow = p_new - p_old
    prompt = (
        f"A workshop's optimal production occurs at the intersection of $x + y = {c1}$ (Constraint 1) and $2x + y = {c2}$ (Constraint 2), "
        f"which is $({ix}; {iy})$, with profit $P = {px}x + {py}y = \\text{{R }}{p_old}$.\n\n"
        f"If Constraint 1's capacity increases by $1\\text{{ unit}}$ to $x + y = {c1 + 1}$ (while $2x + y = {c2}$ stays fixed), "
        f"calculate the new intersection point and the **marginal increase in maximum profit**."
    )
    ans = f"({ix - 1}; {iy + 2}),\\ \\Delta P = \\text{{R }}{shadow}"
    sol = (
        f"Solving $x + y = {c1 + 1}$ and $2x + y = {c2}$ gives $x = {c2} - {c1 + 1} = {ix - 1}$ and $y = {c1 + 1} - {ix - 1} = {iy + 2}$.\n"
        f"New profit $P_{{\\text{{new}}}} = {px}({ix - 1}) + {py}({iy + 2}) = \\text{{R }}{p_new}$.\n"
        f"Marginal profit increase $\\Delta P = {p_new} - {p_old} = \\text{{R }}{shadow}$."
    )
    return _make_q(
        r, "37_shadow_price_marginal_value_of_additional_resource_unit", 37, prompt, ans, sol, 3,
        ["assumed_both_x_and_y_increase_when_one_constraint_relaxes"],
        [{"step": 1, "criterion": f"New vertex ({ix - 1}; {iy + 2})", "marks": 1}, {"step": 2, "criterion": f"New profit R{p_new}", "marks": 1}, {"step": 3, "criterion": f"Increase = R{shadow}", "marks": 1}],
        {"tier_1": f"Solve x + y = {c1 + 1} and 2x + y = {c2} simultaneously.", "tier_2": f"Evaluate P at ({ix - 1}; {iy + 2}) and subtract R{p_old}.", "tier_3": ans},
    )


# 38. Break-even and minimum profit target constraint line (with SVG)
def build_38_break_even_and_minimum_profit_target_line_svg(r: random.Random) -> Dict[str, Any]:
    px = r.randint(2, 5) * 100
    py = r.randint(2, 5) * 100
    mult = r.randint(3, 6)
    target_p = (px * py // 100) * mult
    x_int = target_p // px
    y_int = target_p // py
    svg = _svg_single_line_region(px // 100, py // 100, target_p // 100, shade_below=False)
    prompt = (
        f"A small enterprise makes a profit of $\\text{{R }}{px}$ per unit of $x$ and $\\text{{R }}{py}$ per unit of $y$.\n"
        f"To cover fixed overhead expenses, weekly profit must be **at least** $\\text{{R }}{target_p}$ (represented by the shaded region in the diagram).\n\n"
        f"Write down this minimum profit target inequality and find its $x$- and $y$-intercepts."
    )
    ans = f"{px}x + {py}y \\ge {target_p},\\ ({x_int}; 0),\\ (0; {y_int})"
    sol = f"Inequality: ${px}x + {py}y \\ge {target_p}$. Setting $y = 0 \\implies x = {x_int}$; setting $x = 0 \\implies y = {y_int}$."
    return _make_q(
        r, "38_break_even_and_minimum_profit_target_constraint_line_svg", 38, prompt, ans, sol, 3,
        ["used_less_equal_for_minimum_profit_target"],
        [{"step": 1, "criterion": f"{px}x + {py}y >= {target_p}", "marks": 1}, {"step": 2, "criterion": f"Intercepts ({x_int}; 0) and (0; {y_int})", "marks": 2}],
        {"tier_1": "Set total profit >= target overhead.", "tier_2": f"Divide {target_p} by {px} and by {py} to find the intercepts.", "tier_3": ans},
        svg=svg,
    )


# 39. Manufacturing workshop desks and chairs full optimisation (with SVG)
def build_39_manufacturing_workshop_desks_and_chairs_full_optimisation_svg(r: random.Random) -> Dict[str, Any]:
    ix = r.randint(4, 10)
    iy = r.randint(4, 10)
    if ix % 2 != iy % 2:
        iy += 1
    c1 = ix + iy
    c2 = 2 * ix + iy
    py = r.randint(3, 6) * 100
    px = py + 100
    max_p = px * ix + py * iy
    svg = _svg_lp_quad_region(c1, c1, c2, c2 // 2, ix, iy, "Workshop Production Optimisation", search_m=(px // 100, py // 100))
    prompt = (
        f"Apex Woodcraft manufactures desks ($x$) and chairs ($y$). The weekly constraints (graphed in the diagram) are:\n"
        f"• Finishing department: $x + y \\le {c1}$\n"
        f"• Carpentry department: $2x + y \\le {c2}$\n"
        f"• $x \\ge 0,\\ y \\ge 0$\n"
        f"Profit is $\\text{{R }}{px}$ per desk and $\\text{{R }}{py}$ per chair.\n\n"
        f"Determine the optimal weekly production $(x; y)$ and the maximum weekly profit."
    )
    ans = f"{ix}\\text{{ desks, }}{iy}\\text{{ chairs; }}P_{{\\max}} = \\text{{R }}{max_p}"
    sol = (
        f"Vertices are $(0; 0)$, $(0; {c1})$, $({ix}; {iy})$, and $({c2 // 2}; 0)$.\n"
        f"Evaluating $P = {px}x + {py}y$:\n"
        f"• $(0; {c1}) \\implies \\text{{R }}{py * c1}$\n"
        f"• $({ix}; {iy}) \\implies \\text{{R }}{max_p}$\n"
        f"• $({c2 // 2}; 0) \\implies \\text{{R }}{px * (c2 // 2)}$\n"
        f"Maximum profit is $\\text{{R }}{max_p}$ when producing ${ix}$ desks and ${iy}$ chairs."
    )
    return _make_q(
        r, "39_manufacturing_workshop_desks_and_chairs_full_optimisation_svg", 39, prompt, ans, sol, 4,
        ["evaluated_profit_at_only_one_axis_intercept"],
        [{"step": 1, "criterion": f"Intersection vertex ({ix}; {iy})", "marks": 2}, {"step": 2, "criterion": "Corner point profit comparison", "marks": 1}, {"step": 3, "criterion": f"Max profit R{max_p}", "marks": 1}],
        {"tier_1": "Find the intersection of x + y = c1 and 2x + y = c2.", "tier_2": f"Test P at (0; {c1}), ({ix}; {iy}), and ({c2 // 2}; 0).", "tier_3": ans},
        svg=svg,
    )


# 40. Bakery cakes and loaves oven and decorating optimisation
def build_40_bakery_cakes_and_loaves_oven_and_decorating_optimisation(r: random.Random) -> Dict[str, Any]:
    ix = r.randint(5, 12)
    iy = r.randint(6, 14)
    c1 = ix + iy
    c2 = 3 * ix + iy
    py = r.randint(2, 4) * 50
    px = 2 * py
    max_p = px * ix + py * iy
    prompt = (
        f"Golden Harvest Bakery produces speciality cakes ($x$) and artisan loaves ($y$) daily.\n"
        f"• Total items baked cannot exceed ${c1}$: $x + y \\le {c1}$.\n"
        f"• Decorating time (3 units per cake, 1 unit per loaf) cannot exceed ${c2}$ units: $3x + y \\le {c2}$.\n"
        f"• Profit is $\\text{{R }}{px}$ per cake and $\\text{{R }}{py}$ per loaf.\n\n"
        f"Calculate the intersection corner point and the **maximum daily profit**."
    )
    ans = f"({ix}; {iy}),\\ P_{{\\max}} = \\text{{R }}{max_p}"
    sol = (
        f"Subtracting $x + y = {c1}$ from $3x + y = {c2}$ gives $2x = {c2 - c1} \\implies x = {ix}$ and $y = {iy}$.\n"
        f"Since the profit slope $-\\frac{{{px}}}{{{py}}} = -2$ lies between $-1$ and $-3$, the maximum occurs at $({ix}; {iy})$ with $P = {px}({ix}) + {py}({iy}) = \\text{{R }}{max_p}$."
    )
    return _make_q(
        r, "40_bakery_cakes_and_loaves_oven_and_decorating_optimisation", 40, prompt, ans, sol, 4,
        ["simultaneous_equations_division_error"],
        [{"step": 1, "criterion": f"Solve 2x = {c2 - c1} => x = {ix}, y = {iy}", "marks": 2}, {"step": 2, "criterion": f"Max profit R{max_p}", "marks": 2}],
        {"tier_1": "Solve x + y = c1 and 3x + y = c2 simultaneously.", "tier_2": f"2x = {c2 - c1} => x = {ix}, y = {iy}. Then substitute into P.", "tier_3": ans},
    )


# 41. School excursion minibus and coach hire cost minimisation (with SVG)
def build_41_school_excursion_minibus_and_coach_hire_cost_minimisation_svg(r: random.Random) -> Dict[str, Any]:
    ix = r.randint(3, 7)
    iy = r.randint(3, 7)
    if ix % 2 != iy % 2:
        iy += 1
    c1 = ix + iy
    c2 = 2 * ix + iy
    cy = r.randint(12, 20) * 100
    cx = cy + 600
    min_cost = cx * ix + cy * iy
    svg = _svg_lp_quad_region(c1, c1, c2, c2 // 2, ix, iy, "Excursion Transport Cost Minimisation", search_m=(cx // 100, cy // 100))
    prompt = (
        f"A school organises a tour using $x$ large buses and $y$ midi-buses (boundary lines shown in the diagram).\n"
        f"The constraints simplify to $x + y \\ge {c1}$ and $2x + y \\ge {c2}$ ($x \\ge 0, y \\ge 0$).\n"
        f"Hiring costs are $\\text{{R }}{cx}$ per large bus and $\\text{{R }}{cy}$ per midi-bus.\n\n"
        f"Determine the combination $(x; y)$ that **minimises** total transport cost and state the minimum cost."
    )
    ans = f"({ix}; {iy}),\\ C_{{\\min}} = \\text{{R }}{min_cost}"
    sol = (
        f"Lower boundary vertices are $(0; {c2})$, $({ix}; {iy})$, and $({c1}; 0)$.\n"
        f"• At $(0; {c2})$: $C = \\text{{R }}{cy * c2}$\n"
        f"• At $({ix}; {iy})$: $C = {cx}({ix}) + {cy}({iy}) = \\text{{R }}{min_cost}$\n"
        f"• At $({c1}; 0)$: $C = \\text{{R }}{cx * c1}$\n"
        f"Minimum cost is $\\text{{R }}{min_cost}$ at $({ix}; {iy})$."
    )
    return _make_q(
        r, "41_school_excursion_minibus_and_coach_hire_cost_minimisation_svg", 41, prompt, ans, sol, 4,
        ["evaluated_origin_zero_zero_for_minimum_cost_problem"],
        [{"step": 1, "criterion": f"Vertices (0; {c2}), ({ix}; {iy}), ({c1}; 0)", "marks": 2}, {"step": 2, "criterion": f"Min cost R{min_cost} at ({ix}; {iy})", "marks": 2}],
        {"tier_1": "Origin (0; 0) is not in the feasible region because constraints are >=.", "tier_2": f"Test (0; {c2}), ({ix}; {iy}), and ({c1}; 0) in C = {cx}x + {cy}y.", "tier_3": ans},
        svg=svg,
    )


# 42. Farm crop allocation maize and sunflowers profit maximisation
def build_42_farm_crop_allocation_maize_and_sunflowers_profit_maximisation(r: random.Random) -> Dict[str, Any]:
    min_x = r.randint(10, 25)
    min_y = r.randint(15, 30)
    total_land = min_x + min_y + r.randint(20, 50)
    px = r.randint(4, 8) * 1000
    py = px + r.randint(1, 3) * 1000  # py > px so allocate remaining land to y
    opt_x = min_x
    opt_y = total_land - min_x
    max_p = px * opt_x + py * opt_y
    prompt = (
        f"A co-operative farm has ${total_land}$ hectares available for maize ($x$) and sunflowers ($y$), so $x + y \\le {total_land}$.\n"
        f"Crop rotation rules require **at least** ${min_x}$ hectares of maize ($x \\ge {min_x}$) and **at least** ${min_y}$ hectares of sunflowers ($y \\ge {min_y}$).\n"
        f"Profit is $\\text{{R }}{px}$ per hectare of maize and $\\text{{R }}{py}$ per hectare of sunflowers.\n\n"
        f"Determine the optimal allocation $(x; y)$ and the maximum farm profit."
    )
    ans = f"({opt_x}; {opt_y}),\\ P_{{\\max}} = \\text{{R }}{max_p}"
    sol = (
        f"Since sunflowers yield a higher profit per hectare ($\\text{{R }}{py} > \\text{{R }}{px}$), we plant the minimum required maize "
        f"($x = {opt_x}$) and allocate the remaining land to sunflowers ($y = {total_land} - {opt_x} = {opt_y} \\ge {min_y}$).\n"
        f"Maximum profit $P = {px}({opt_x}) + {py}({opt_y}) = \\text{{R }}{max_p}$."
    )
    return _make_q(
        r, "42_farm_crop_allocation_maize_and_sunflowers_profit_maximisation", 42, prompt, ans, sol, 3,
        ["allocated_extra_land_to_lower_profit_crop"],
        [{"step": 1, "criterion": f"Optimal allocation ({opt_x}; {opt_y})", "marks": 2}, {"step": 2, "criterion": f"Max profit R{max_p}", "marks": 1}],
        {"tier_1": "Find the vertices of the triangle defined by x >= min_x, y >= min_y, and x + y <= total_land.", "tier_2": f"Upper vertices are ({min_x}; {opt_y}) and ({total_land - min_y}; {min_y}). Since py > px, ({min_x}; {opt_y}) wins.", "tier_3": ans},
    )


# 43. Clinic media production videos and books sales optimisation
def build_43_clinic_media_production_videos_and_books_sales_optimisation(r: random.Random) -> Dict[str, Any]:
    total_cap = r.randint(8, 15) * 1000
    min_v = r.randint(1, 3) * 1000
    max_b = r.randint(4, 7) * 1000
    while min_v + max_b >= total_cap:
        total_cap += 2000
    rev_v = r.randint(40, 70)
    rev_b = rev_v + r.randint(15, 35)
    # Since rev_b > rev_v, maximise books y = max_b and set videos x = total_cap - max_b
    opt_y = max_b
    opt_x = total_cap - max_b
    max_rev = rev_v * opt_x + rev_b * opt_y
    prompt = (
        f"A health clinic produces educational videos ($x$) and printed handbooks ($y$).\n"
        f"• Total copies produced: $x + y \\le {total_cap}$\n"
        f"• At least ${min_v}$ videos must be produced: $x \\ge {min_v}$\n"
        f"• At most ${max_b}$ handbooks can be printed: $y \\le {max_b}$\n"
        f"Each video generates $\\text{{R }}{rev_v}$ and each handbook generates $\\text{{R }}{rev_b}$ for the clinic fund.\n\n"
        f"Determine the combination $(x; y)$ that maximises total revenue and calculate this maximum revenue."
    )
    ans = f"({opt_x}; {opt_y}),\\ R_{{\\max}} = \\text{{R }}{max_rev}"
    sol = (
        f"Along $x + y = {total_cap}$, handbooks earn more per unit ($\\text{{R }}{rev_b} > \\text{{R }}{rev_v}$), so we set $y$ to its upper bound "
        f"$y = {opt_y}$ and $x = {total_cap} - {opt_y} = {opt_x}$ (which satisfies $x \\ge {min_v}$).\n"
        f"Maximum revenue $= {rev_v}({opt_x}) + {rev_b}({opt_y}) = \\text{{R }}{max_rev}$."
    )
    return _make_q(
        r, "43_clinic_media_production_videos_and_books_sales_optimisation", 43, prompt, ans, sol, 3,
        ["ignored_upper_bound_on_y_when_maximising"],
        [{"step": 1, "criterion": f"Optimal pair ({opt_x}; {opt_y})", "marks": 2}, {"step": 2, "criterion": f"Max revenue R{max_rev}", "marks": 1}],
        {"tier_1": "To maximise revenue along x + y = total_cap, make the higher-earning variable y as large as allowed.", "tier_2": f"Set y = {max_b} and x = {total_cap} - {max_b} = {opt_x}.", "tier_3": ans},
    )


# 44. Test design algebra and geometry section marks maximisation
def build_44_test_design_algebra_and_geometry_section_marks_maximisation(r: random.Random) -> Dict[str, Any]:
    min_x = r.randint(3, 6)
    max_y = r.randint(6, 10)
    # 2x + 3y <= time_limit; choose time_limit = 2*min_x + 3*opt_y
    opt_y = r.randint(4, max_y)
    time_lim = 2 * min_x + 3 * opt_y
    m_x = r.randint(4, 6)
    m_y = m_x * 2  # Geometry gives 2*m_x marks for 3 mins => higher marks per minute than algebra (m_x for 2 mins)
    max_marks = m_x * min_x + m_y * opt_y
    prompt = (
        f"A teacher designs a test with $x$ Algebra questions and $y$ Geometry questions:\n"
        f"• Minimum Algebra questions: $x \\ge {min_x}$\n"
        f"• Maximum Geometry questions: $0 \\le y \\le {max_y}$\n"
        f"• Time constraint ($2\\text{{ min}}$ per Algebra, $3\\text{{ min}}$ per Geometry): $2x + 3y \\le {time_lim}$\n"
        f"Each Algebra question carries ${m_x}$ marks and each Geometry question carries ${m_y}$ marks.\n\n"
        f"Write down the total marks objective function $T$ and calculate the maximum possible marks at the corner point $({min_x}; {opt_y})$."
    )
    ans = f"T = {m_x}x + {m_y}y,\\ T_{{\\max}} = {max_marks}\\text{{ marks}}"
    sol = (
        f"Objective function: $T = {m_x}x + {m_y}y$.\n"
        f"At the corner point $({min_x}; {opt_y})$ (where $x = {min_x}$ meets $2x + 3y = {time_lim}$), "
        f"$T = {m_x}({min_x}) + {m_y}({opt_y}) = {m_x * min_x} + {m_y * opt_y} = {max_marks}$ marks."
    )
    return _make_q(
        r, "44_test_design_algebra_and_geometry_section_marks_maximisation", 44, prompt, ans, sol, 3,
        ["substituted_time_coefficients_instead_of_mark_allocations"],
        [{"step": 1, "criterion": f"T = {m_x}x + {m_y}y", "marks": 1}, {"step": 2, "criterion": f"T({min_x}; {opt_y}) = {max_marks} marks", "marks": 2}],
        {"tier_1": f"Formulate T using the marks per question ({m_x} and {m_y}), not the minutes.", "tier_2": f"Substitute x = {min_x} and y = {opt_y} into T = {m_x}x + {m_y}y.", "tier_3": ans},
    )


# 45. Prize giveaway kettles and toasters cost minimisation (with SVG)
def build_45_prize_giveaway_kettles_and_toasters_cost_minimisation_svg(r: random.Random) -> Dict[str, Any]:
    min_k = r.randint(8, 15)
    min_t = r.randint(8, 15)
    total_prizes = min_k + min_t + r.randint(12, 25)
    cost_t = r.randint(9, 14) * 10
    cost_k = cost_t + r.randint(2, 6) * 10  # kettles cost more than toasters
    opt_k = min_k
    opt_t = total_prizes - min_k
    min_cost = cost_k * opt_k + cost_t * opt_t
    svg = _svg_single_line_region(1, 1, total_prizes, shade_below=False, test_pt=(opt_k, opt_t))
    prompt = (
        f"A store gives away **at least** ${total_prizes}$ prizes consisting of kettles ($x$) and toasters ($y$), as shown on the boundary graph.\n"
        f"• At least ${min_k}$ kettles ($x \\ge {min_k}$) and at least ${min_t}$ toasters ($y \\ge {min_t}$) must be included.\n"
        f"• A kettle costs $\\text{{R }}{cost_k}$ and a toaster costs $\\text{{R }}{cost_t}$.\n\n"
        f"Determine the cheapest combination $(x; y)$ and the **minimum total cost**."
    )
    ans = f"({opt_k}; {opt_t}),\\ C_{{\\min}} = \\text{{R }}{min_cost}"
    sol = (
        f"Lower boundary vertices on $x + y = {total_prizes}$ are $({min_k}; {opt_t})$ and $({total_prizes - min_t}; {min_t})$.\n"
        f"Since toasters are cheaper ($\\text{{R }}{cost_t} < \\text{{R }}{cost_k}$), minimum cost occurs at $({opt_k}; {opt_t})$:\n"
        f"$C_{{\\min}} = {cost_k}({opt_k}) + {cost_t}({opt_t}) = \\text{{R }}{min_cost}$."
    )
    return _make_q(
        r, "45_prize_giveaway_kettles_and_toasters_cost_minimisation_svg", 45, prompt, ans, sol, 3,
        ["maximised_expensive_item_when_minimising_total_cost"],
        [{"step": 1, "criterion": f"Optimal combination ({opt_k}; {opt_t})", "marks": 2}, {"step": 2, "criterion": f"Minimum cost R{min_cost}", "marks": 1}],
        {"tier_1": "Along x + y = total_prizes, keep the more expensive item (kettles) at its minimum allowed value.", "tier_2": f"Set x = {min_k} and y = {total_prizes} - {min_k} = {opt_t}.", "tier_3": ans},
        svg=svg,
    )


# 46. Bicycle assembly Mountees and Roadees discrete table investigation
def build_46_bicycle_assembly_mountees_and_roadees_discrete_table_investigation(r: random.Random) -> Dict[str, Any]:
    max_m = r.randint(4, 7)
    max_r = r.randint(3, 5)
    techs = max_m + 2 * max_r - r.randint(3, 5)
    pm = r.randint(6, 10) * 100
    pr = pm * 3
    # Find max P = pm*M + pr*R for 0 <= M <= max_m, 0 <= R <= max_r, M + 2R <= techs
    best_m, best_r, best_p = 0, 0, 0
    valid_count = 0
    for m_i in range(max_m + 1):
        for r_i in range(max_r + 1):
            if m_i + 2 * r_i <= techs:
                valid_count += 1
                p_val = pm * m_i + pr * r_i
                if p_val > best_p:
                    best_m, best_r, best_p = m_i, r_i, p_val
    prompt = (
        f"In a mathematical investigation of bicycle assembly, a workshop builds Mountees ($M$) and Roadees ($R$) daily:\n"
        f"• $0 \\le M \\le {max_m}$ and $0 \\le R \\le {max_r}$ ($M, R \\in \\mathbb{{Z}}_0^+$)\n"
        f"• Technician constraint: $M + 2R \\le {techs}$\n"
        f"• Daily profit: $P = {pm}M + {pr}R$\n\n"
        f"Determine the optimal integer pair $(M; R)$ and the maximum daily profit."
    )
    ans = f"({best_m}; {best_r}),\\ P_{{\\max}} = \\text{{R }}{best_p}"
    sol = (
        f"Since Roadees yield $3$ times the profit of Mountees while using only $2$ times the technicians, we maximise $R = {best_r}$, "
        f"leaving $M = {techs} - 2({best_r}) = {best_m}$ (with $0 \\le M \\le {max_m}$).\n"
        f"Maximum profit $P = {pm}({best_m}) + {pr}({best_r}) = \\text{{R }}{best_p}$."
    )
    return _make_q(
        r, "46_bicycle_assembly_mountees_and_roadees_discrete_table_investigation", 46, prompt, ans, sol, 3,
        ["violated_technician_constraint_when_picking_max_M_and_R"],
        [{"step": 1, "criterion": f"Optimal pair ({best_m}; {best_r})", "marks": 2}, {"step": 2, "criterion": f"Max profit R{best_p}", "marks": 1}],
        {"tier_1": f"Set R to its maximum possible value ({max_r}) and solve M + 2R <= {techs} for M.", "tier_2": f"When R = {best_r}, M = {techs} - {2 * best_r} = {best_m}.", "tier_3": ans},
    )


# 47. Investigation: parameter k scaling constraints and optimal value
def build_47_investigation_parameter_k_scaling_constraints_and_optimal_value(r: random.Random) -> Dict[str, Any]:
    p_base = r.randint(12, 35) * 100
    k_scale = r.randint(2, 5)
    p_new = p_base * k_scale
    area_factor = k_scale ** 2
    prompt = (
        f"**Mathematical Investigation:** In a linear programming model with constraints $a_1 x + b_1 y \\le c_1$, "
        f"$a_2 x + b_2 y \\le c_2$ ($x, y \\ge 0$), the maximum value of $P = px + qy$ is $P_{{\\max}} = \\text{{R }}{p_base}$.\n\n"
        f"Suppose both resource capacities $c_1$ and $c_2$ are multiplied by a constant scale factor $k = {k_scale}$ (while $a_i, b_i, p, q$ remain unchanged).\n"
        f"1. Calculate the new maximum profit $P'_{{\\max}}$.\n"
        f"2. State the factor by which the **area** of the feasible region increases."
    )
    ans = f"P'_{{\\max}} = \\text{{R }}{p_new},\\ \\text{{Area factor}} = {area_factor}"
    sol = (
        f"1. Scaling all RHS constants $c_i$ by $k = {k_scale}$ scales every corner-point coordinate $(x; y)$ to $({k_scale}x; {k_scale}y)$. "
        f"Since $P$ is linear, $P'_{{\\max}} = {k_scale} \\times {p_base} = \\text{{R }}{p_new}$.\n"
        f"2. Because all linear dimensions of the feasible polygon scale by $k = {k_scale}$, its area scales by $k^2 = {k_scale}^2 = {area_factor}$."
    )
    return _make_q(
        r, "47_investigation_parameter_k_scaling_constraints_and_optimal_value", 47, prompt, ans, sol, 3,
        ["scaled_linear_objective_by_k_squared_instead_of_k"],
        [{"step": 1, "criterion": f"New max profit = R{p_new} (scales by k)", "marks": 2}, {"step": 2, "criterion": f"Feasible area scales by k^2 = {area_factor}", "marks": 1}],
        {"tier_1": "Each vertex (x; y) becomes (kx; ky). Substitute (kx; ky) into P = px + qy.", "tier_2": f"P scales by k = {k_scale}, while 2D area scales by k^2 = {area_factor}.", "tier_3": ans},
    )


# 48. Investigation: comparative growth linear vs compound project model
def build_48_investigation_comparative_growth_linear_vs_compound_project_model(r: random.Random) -> Dict[str, Any]:
    p_val = r.randint(2, 6) * 1000
    rate_s = r.randint(10, 16)
    rate_c = r.randint(8, 12)
    n_yrs = r.randint(3, 6)
    a_simple = round(p_val * (1 + (rate_s / 100.0) * n_yrs), 2)
    a_comp = round(p_val * ((1 + rate_c / 100.0) ** n_yrs), 2)
    s_str = _fmt(a_simple, 2)
    c_str = _fmt(a_comp, 2)
    better = "Option A (Simple)" if a_simple >= a_comp else "Option B (Compound)"
    prompt = (
        f"**Project Investigation:** A firm invests its optimal weekly profit of $P = \\text{{R }}{p_val}$ for $n = {n_yrs}\\text{{ years}}$ and compares two models:\n"
        f"• **Option A (Linear / Simple Growth):** $A = P(1 + i \\cdot n)$ at ${rate_s}\\%$ p.a.\n"
        f"• **Option B (Exponential / Compound Growth):** $A = P(1 + i)^n$ at ${rate_c}\\%$ p.a.\n\n"
        f"Calculate the accumulated amount for both options (to two decimal places) and state which option yields the higher return after ${n_yrs}$ years."
    )
    ans = f"A_{{\\text{{simple}}}} = \\text{{R }}{s_str},\\ A_{{\\text{{comp}}}} = \\text{{R }}{c_str},\\ {better}"
    sol = (
        f"• Option A: $A = {p_val}(1 + {_fmt(rate_s / 100, 3)} \\times {n_yrs}) = \\text{{R }}{s_str}$.\n"
        f"• Option B: $A = {p_val}(1 + {_fmt(rate_c / 100, 3)})^{{{n_yrs}}} \\approx \\text{{R }}{c_str}$.\n"
        f"Better return after ${n_yrs}$ years: **{better}**."
    )
    return _make_q(
        r, "48_investigation_comparative_growth_linear_vs_compound_project_model", 48, prompt, ans, sol, 4,
        ["used_simple_interest_formula_for_compound_growth"],
        [{"step": 1, "criterion": f"Option A = R{s_str}", "marks": 1}, {"step": 2, "criterion": f"Option B = R{c_str}", "marks": 2}, {"step": 3, "criterion": f"Comparison: {better}", "marks": 1}],
        {"tier_1": "Evaluate A = P(1 + in) for Option A and A = P(1 + i)^n for Option B.", "tier_2": f"Option A gives R{s_str}; Option B gives R{c_str}.", "tier_3": ans},
    )


# 49. Sensitivity analysis: changing unit profit shifts optimum vertex (with SVG)
def build_49_sensitivity_analysis_changing_unit_profit_shifts_optimum_vertex_svg(r: random.Random) -> Dict[str, Any]:
    ix = r.randint(4, 9)
    iy = r.randint(4, 9)
    if ix % 2 != iy % 2:
        iy += 1
    c1 = ix + iy
    c2 = 2 * ix + iy
    x_int_2 = c2 // 2
    # Initially P1 = 150x + 100y (slope -1.5, optimal at C(ix, iy)).
    # After market shift, profit on x triples while y drops: P2 = 300x + 100y (slope -3, steeper than -2, so optimal shifts to D(x_int_2, 0))
    px_new = r.randint(3, 5) * 100
    py_new = 100
    p_at_c = px_new * ix + py_new * iy
    p_at_d = px_new * x_int_2
    svg = _svg_lp_quad_region(c1, c1, c2, x_int_2, ix, iy, "Sensitivity Analysis: Shift of Optimum", search_m=(px_new // 100, 1))
    prompt = (
        f"A feasible region (shown in the diagram) has vertices $B(0; {c1})$, $C({ix}; {iy})$, and $D({x_int_2}; 0)$.\n"
        f"Initially, the profit function has gradient $-1{{,}}5$, making $C({ix}; {iy})$ optimal.\n"
        f"Due to a market price surge, the profit function changes to $P_{{\\text{{new}}}} = {px_new}x + {py_new}y$.\n\n"
        f"Compare $P_{{\\text{{new}}}}$ at $C({ix}; {iy})$ and $D({x_int_2}; 0)$ to determine the **new optimal vertex** and maximum profit."
    )
    ans = f"D({x_int_2}; 0),\\ P_{{\\max}} = \\text{{R }}{p_at_d}"
    sol = (
        f"• At $C({ix}; {iy})$: $P_{{\\text{{new}}}} = {px_new}({ix}) + {py_new}({iy}) = \\text{{R }}{p_at_c}$.\n"
        f"• At $D({x_int_2}; 0)$: $P_{{\\text{{new}}}} = {px_new}({x_int_2}) + 0 = \\text{{R }}{p_at_d}$.\n"
        f"Since the new search line gradient $-{px_new // 100}$ is steeper than $-2$, the optimum shifts to **$D({x_int_2}; 0)$** with $P_{{\\max}} = \\text{{R }}{p_at_d}$."
    )
    return _make_q(
        r, "49_sensitivity_analysis_changing_unit_profit_shifts_optimum_vertex_svg", 49, prompt, ans, sol, 3,
        ["assumed_intersection_vertex_is_always_optimal_regardless_of_objective_slope"],
        [{"step": 1, "criterion": f"P_new(C) = R{p_at_c}", "marks": 1}, {"step": 2, "criterion": f"P_new(D) = R{p_at_d}", "marks": 1}, {"step": 3, "criterion": f"New optimum D({x_int_2}; 0)", "marks": 1}],
        {"tier_1": "Substitute both C and D into P_new and compare the values.", "tier_2": f"At C: R{p_at_c}; at D: R{p_at_d}. Since {p_at_d} > {p_at_c}, D is now optimal.", "tier_3": ans},
        svg=svg,
    )


# 50. Linear programming diagnostic autopsy and misconception repair
def build_50_linear_programming_diagnostic_autopsy_and_misconception_repair(r: random.Random) -> Dict[str, Any]:
    a_v = r.randint(2, 5)
    b_v = r.randint(6, 10)
    px = r.randint(2, 5) * 100
    py = r.randint(6, 9) * 100
    ix = r.randint(4, 8)
    iy = r.randint(5, 9)
    true_p = px * ix + py * iy
    wrong_p = py * ix + px * iy
    prompt = (
        f"A learner solves a linear programming question with objective function $P = {px}x + {py}y$ and constraint ${a_v}x + {b_v}y \\le {a_v * ix + b_v * iy}$:\n"
        f"• **Step 1:** Writes the search line gradient as $m = -\\frac{{{py}}}{{{px}}}$ instead of $-\\frac{{{px}}}{{{py}}}$.\n"
        f"• **Step 2:** Evaluates profit at $({ix}; {iy})$ as $P = {py}({ix}) + {px}({iy}) = \\text{{R }}{wrong_p}$.\n\n"
        f"Identify the error in Step 1 and Step 2, write down the **correct search line gradient**, and calculate the **correct profit** at $({ix}; {iy})$."
    )
    ans = f"m = -\\frac{{{px}}}{{{py}}},\\ P = \\text{{R }}{true_p}"
    sol = (
        f"• In Step 1, isolating $y$ in $P = {px}x + {py}y$ gives $y = -\\frac{{{px}}}{{{py}}}x + \\frac{{P}}{{{py}}}$, so the correct gradient is $m = -\\frac{{{px}}}{{{py}}}$ (not $-\\frac{{{py}}}{{{px}}}$).\n"
        f"• In Step 2, the learner swapped the $x$ and $y$ coefficients. Correct profit: $P = {px}({ix}) + {py}({iy}) = \\text{{R }}{true_p}$."
    )
    return _make_q(
        r, "50_linear_programming_diagnostic_autopsy_and_misconception_repair", 50, prompt, ans, sol, 3,
        ["inverted_search_line_gradient_b_over_a", "swapped_x_and_y_in_objective_substitution"],
        [{"step": 1, "criterion": "Identified coefficient inversion error", "marks": 1}, {"step": 2, "criterion": f"Correct gradient m = -{px}/{py}", "marks": 1}, {"step": 3, "criterion": f"Correct profit R{true_p}", "marks": 1}],
        {"tier_1": f"Isolate y in P = {px}x + {py}y to check the gradient.", "tier_2": f"Multiply {px} by x = {ix} and {py} by y = {iy}.", "tier_3": ans},
    )


ARCHETYPES_26_50 = {
    "26_evaluate_objective_function_at_given_feasible_vertices_svg": build_26_evaluate_objective_function_at_given_feasible_vertices_svg,
    "27_maximise_profit_using_corner_point_theorem_svg": build_27_maximise_profit_using_corner_point_theorem_svg,
    "28_minimise_cost_using_corner_point_theorem_svg": build_28_minimise_cost_using_corner_point_theorem_svg,
    "29_gradient_of_search_line_from_objective_function_svg": build_29_gradient_of_search_line_from_objective_function_svg,
    "30_search_line_sliding_direction_for_maximum_vs_minimum_svg": build_30_search_line_sliding_direction_for_maximum_vs_minimum_svg,
    "31_find_optimal_vertex_using_search_line_gradient_comparison_svg": build_31_find_optimal_vertex_using_search_line_gradient_comparison_svg,
    "32_multiple_optimal_solutions_along_parallel_boundary_edge_svg": build_32_multiple_optimal_solutions_along_parallel_boundary_edge_svg,
    "33_integer_lattice_optimisation_when_vertex_is_non_integral_svg": build_33_integer_lattice_optimisation_when_vertex_is_non_integral_svg,
    "34_find_unknown_profit_coefficient_given_optimal_edge_gradient": build_34_find_unknown_profit_coefficient_given_optimal_edge_gradient,
    "35_range_of_profit_ratio_preserving_current_optimal_vertex": build_35_range_of_profit_ratio_preserving_current_optimal_vertex,
    "36_calculate_slack_and_surplus_resources_at_optimal_point": build_36_calculate_slack_and_surplus_resources_at_optimal_point,
    "37_shadow_price_marginal_value_of_additional_resource_unit": build_37_shadow_price_marginal_value_of_additional_resource_unit,
    "38_break_even_and_minimum_profit_target_constraint_line_svg": build_38_break_even_and_minimum_profit_target_line_svg,
    "39_manufacturing_workshop_desks_and_chairs_full_optimisation_svg": build_39_manufacturing_workshop_desks_and_chairs_full_optimisation_svg,
    "40_bakery_cakes_and_loaves_oven_and_decorating_optimisation": build_40_bakery_cakes_and_loaves_oven_and_decorating_optimisation,
    "41_school_excursion_minibus_and_coach_hire_cost_minimisation_svg": build_41_school_excursion_minibus_and_coach_hire_cost_minimisation_svg,
    "42_farm_crop_allocation_maize_and_sunflowers_profit_maximisation": build_42_farm_crop_allocation_maize_and_sunflowers_profit_maximisation,
    "43_clinic_media_production_videos_and_books_sales_optimisation": build_43_clinic_media_production_videos_and_books_sales_optimisation,
    "44_test_design_algebra_and_geometry_section_marks_maximisation": build_44_test_design_algebra_and_geometry_section_marks_maximisation,
    "45_prize_giveaway_kettles_and_toasters_cost_minimisation_svg": build_45_prize_giveaway_kettles_and_toasters_cost_minimisation_svg,
    "46_bicycle_assembly_mountees_and_roadees_discrete_table_investigation": build_46_bicycle_assembly_mountees_and_roadees_discrete_table_investigation,
    "47_investigation_parameter_k_scaling_constraints_and_optimal_value": build_47_investigation_parameter_k_scaling_constraints_and_optimal_value,
    "48_investigation_comparative_growth_linear_vs_compound_project_model": build_48_investigation_comparative_growth_linear_vs_compound_project_model,
    "49_sensitivity_analysis_changing_unit_profit_shifts_optimum_vertex_svg": build_49_sensitivity_analysis_changing_unit_profit_shifts_optimum_vertex_svg,
    "50_linear_programming_diagnostic_autopsy_and_misconception_repair": build_50_linear_programming_diagnostic_autopsy_and_misconception_repair,
}
