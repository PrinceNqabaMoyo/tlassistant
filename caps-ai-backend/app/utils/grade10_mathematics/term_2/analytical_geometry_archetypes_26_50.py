"""Grade 10 Mathematics — Term 2 — Analytical Geometry Archetypes 26 to 50.

Grounded strictly in CAPS Grade 10 Mathematics Term 2 Chapter 8 Analytical Geometry syllabus.
Covers:
- Straight line equations: gradient-intercept form, point-slope form, two-point form
- Parallel and perpendicular lines equations
- Perpendicular bisector, triangle medians, and triangle altitudes
- Axis intercepts, points on lines, and line intersections
- Coordinate geometry proofs of quadrilaterals:
  * Parallelogram (opposite sides parallel, opposite sides equal, diagonals bisect)
  * Fourth vertex determination
  * Rectangle (parallelogram with right angle)
  * Rhombus (parallelogram with perpendicular diagonals)
  * Square (equal sides and right angle)
  * Trapezium (one pair of parallel sides)
  * Kite (two pairs of adjacent equal sides)
- Area of triangles, rectangles, and squares on the Cartesian plane
- Distance from origin and circle equation check (x^2 + y^2 = r^2)
- Multi-step exam synthesis problem

100% deterministic, zero-LLM, South African National Curriculum Standards compliant.
"""
from __future__ import annotations

import math
import random
from typing import Any, Callable, Dict, List, Optional, Tuple

from .analytical_geometry_archetypes_01_25 import (
    TERM,
    CAPS_WEIGHT,
    SUGGESTED_DURATION,
    TOPIC_ID,
    LEARNING_OBJECTIVE,
    _fmt_num,
    _coord,
    _signed,
    _make_svg_plane,
    _base_contract,
)


def _fmt_frac(num: int, den: int) -> str:
    """Format fraction cleanly in LaTeX."""
    if den < 0:
        num = -num
        den = -den
    g = math.gcd(abs(num), abs(den))
    num //= g
    den //= g
    if den == 1:
        return str(num)
    if num < 0:
        return f"-\frac{{{abs(num)}}}{{{den}}}"
    return f"\frac{{{num}}}{{{den}}}"


def _fmt_line_eq(m_num: int, m_den: int, c_num: int, c_den: int) -> str:
    """Format y = mx + c nicely in LaTeX."""
    # Simplify m
    if m_den < 0:
        m_num = -m_num
        m_den = -m_den
    gm = math.gcd(abs(m_num), abs(m_den))
    m_num //= gm
    m_den //= gm

    # Simplify c
    if c_den < 0:
        c_num = -c_num
        c_den = -c_den
    gc = math.gcd(abs(c_num), abs(c_den))
    c_num //= gc
    c_den //= gc

    # m string
    if m_num == 0:
        m_str = ""
    elif m_den == 1:
        if m_num == 1:
            m_str = "x"
        elif m_num == -1:
            m_str = "-x"
        else:
            m_str = f"{m_num}x"
    else:
        if m_num < 0:
            m_str = f"-\frac{{{abs(m_num)}}}{{{m_den}}}x"
        else:
            m_str = f"\frac{{{m_num}}}{{{m_den}}}x"

    # c string
    if c_num == 0:
        c_str = ""
    elif c_den == 1:
        if m_str == "":
            c_str = f"{c_num}"
        else:
            c_str = f" + {c_num}" if c_num > 0 else f" - {abs(c_num)}"
    else:
        if m_str == "":
            c_str = _fmt_frac(c_num, c_den)
        else:
            c_str = f" + \frac{{{c_num}}}{{{c_den}}}" if c_num > 0 else f" - \frac{{{abs(c_num)}}}{{{c_den}}}"

    if m_str == "" and c_str == "":
        return "y = 0"
    return f"y = {m_str}{c_str}"


def _make_svg_circle_plane(
    radius: float,
    test_points: List[Tuple[str, float, float]],
    viewbox: str = "0 0 400 300",
    origin: Tuple[int, int] = (200, 150),
    scale: float = 16.0,
) -> str:
    """SVG for circle centered at origin with test points."""
    ox, oy = origin
    svg_parts = [
        f'<svg viewBox="{viewbox}" width="100%" height="260" xmlns="http://www.w3.org/2000/svg">',
        '<style>',
        '  .grid { stroke: #e2e8f0; stroke-width: 1; }',
        '  .axis { stroke: #1e293b; stroke-width: 1.5; }',
        '  .circ { stroke: #2563eb; stroke-width: 2; fill: none; }',
        '  .dot { fill: #dc2626; stroke: #ffffff; stroke-width: 1.5; }',
        '  .label { font-family: ui-sans-serif, system-ui, sans-serif; font-size: 12px; fill: #1e293b; font-weight: 600; }',
        '  .axis-label { font-family: ui-sans-serif, system-ui, sans-serif; font-size: 13px; font-weight: bold; fill: #1e293b; }',
        '</style>',
        '<rect width="100%" height="100%" fill="#f8fafc" rx="6" />',
    ]
    # Grid
    for x in range(-10, 11):
        if x != 0:
            px = ox + x * scale
            svg_parts.append(f'<line x1="{px}" y1="10" x2="{px}" y2="{oy*2 - 10}" class="grid" />')
    for y in range(-8, 9):
        if y != 0:
            py = oy - y * scale
            svg_parts.append(f'<line x1="10" y1="{py}" x2="{ox*2 - 10}" y2="{py}" class="grid" />')

    # Axes
    svg_parts.append(f'<line x1="10" y1="{oy}" x2="{ox*2 - 10}" y2="{oy}" class="axis" />')
    svg_parts.append(f'<line x1="{ox}" y1="{oy*2 - 10}" x2="{ox}" y2="10" class="axis" />')
    svg_parts.append(f'<text x="{ox*2 - 18}" y="{oy - 6}" class="axis-label">x</text>')
    svg_parts.append(f'<text x="{ox + 8}" y="22" class="axis-label">y</text>')

    # Circle
    r_px = radius * scale
    svg_parts.append(f'<circle cx="{ox}" cy="{oy}" r="{r_px}" class="circ" />')

    # Points
    for name, x, y in test_points:
        px = ox + x * scale
        py = oy - y * scale
        svg_parts.append(f'<circle cx="{px}" cy="{py}" r="4.5" class="dot" />')
        svg_parts.append(f'<text x="{px + 7}" y="{py - 5}" class="label">{name}({int(x)}; {int(y)})</text>')

    svg_parts.append('</svg>')
    return "\n".join(svg_parts)


# =========================================================================== #
# Archetypes 26 to 50
# =========================================================================== #

def _build_26(rng: random.Random) -> Dict[str, Any]:
    sub = "26_equation_of_line_gradient_and_y_intercept"
    m = rng.choice([-4, -3, -2, -1, 1, 2, 3, 4, 5])
    c = rng.choice([-8, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 8])

    ans = f"${_fmt_line_eq(m, 1, c, 1)}$"
    d1 = f"${_fmt_line_eq(-m, 1, c, 1)}$"
    d2 = f"${_fmt_line_eq(m, 1, -c, 1)}$"
    d3 = f"${_fmt_line_eq(c, 1, m, 1)}$"
    opts = [ans, d1, d2, d3]
    rng.shuffle(opts)

    prompt = (
        f"A straight line has a gradient of $m = {m}$ and passes through the $y$-intercept $(0;\, {c})$. "
        f"Determine the equation of the straight line in standard gradient-intercept form $y = mx + c$."
    )
    steps = [
        {"rule": "Identify gradient and y-intercept", "op": f"m = {m},\; c = {c}", "to": f"m = {m},\; c = {c}"},
        {"rule": "Substitute into slope-intercept formula", "op": f"y = mx + c \implies y = ({m})x + ({c})", "to": ans.replace("$", "")},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="The gradient-intercept form of a linear equation is y = mx + c.",
        t2="The y-intercept (0; c) directly gives the constant term c.",
        t3=f"Substitute m = {m} and c = {c} into y = mx + c to obtain {ans}.",
        misconceptions=["swapped_m_and_c", "sign_error_intercept", "x_y_inversion"],
        marks=2,
    )


def _build_27(rng: random.Random) -> Dict[str, Any]:
    sub = "27_equation_of_line_from_gradient_and_point"
    m = rng.choice([-3, -2, -1, 1, 2, 3, 4])
    x1 = rng.choice([-4, -3, -2, -1, 1, 2, 3, 4])
    y1 = rng.choice([-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6])
    c = y1 - m * x1

    ans = f"${_fmt_line_eq(m, 1, c, 1)}$"
    d1 = f"${_fmt_line_eq(m, 1, y1 + m * x1, 1)}$"
    d2 = f"${_fmt_line_eq(-m, 1, c, 1)}$"
    d3 = f"${_fmt_line_eq(m, 1, -c, 1)}$"
    opts = [ans, d1, d2, d3]
    rng.shuffle(opts)

    pt_str = _coord(x1, y1)
    prompt = (
        f"Determine the equation of the straight line having gradient $m = {m}$ and passing through "
        f"the point $P{pt_str}$ in the form $y = mx + c$."
    )
    steps = [
        {"rule": "Apply point-slope formula", "op": f"y - y_1 = m(x - x_1)", "to": f"y - ({y1}) = {m}(x - ({x1}))"},
        {"rule": "Expand and solve for y", "op": f"y - {y1} = {m}x - {m*x1}", "to": f"y = {m}x + ({c})"},
        {"rule": "Write in final form", "op": f"y = mx + c", "to": ans.replace("$", "")},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="Use the point-slope form y - y_1 = m(x - x_1) or substitute (x_1; y_1) into y = mx + c to solve for c.",
        t2=f"c = y_1 - m(x_1) = {y1} - ({m})({x1}) = {c}.",
        t3=f"Write the resulting equation: {ans}.",
        misconceptions=["sign_error_subtraction", "forgot_expansion_bracket", "swapped_x_and_y"],
        marks=3,
    )


def _build_28(rng: random.Random) -> Dict[str, Any]:
    sub = "28_equation_of_line_through_two_points"
    x1 = rng.choice([-5, -4, -3, -2, -1, 1, 2])
    dx = rng.choice([1, 2, 3, 4])
    x2 = x1 + dx
    m = rng.choice([-3, -2, -1, 1, 2, 3])
    y1 = rng.choice([-4, -3, -2, -1, 0, 1, 2, 3])
    y2 = y1 + m * dx
    c = y1 - m * x1

    ans = f"${_fmt_line_eq(m, 1, c, 1)}$"
    d1 = f"${_fmt_line_eq(-m, 1, c, 1)}$"
    d2 = f"${_fmt_line_eq(m, 1, -c, 1)}$"
    d3 = f"${_fmt_line_eq(dx, 1, c, 1)}$"
    opts = [ans, d1, d2, d3]
    rng.shuffle(opts)

    pA = ("A", x1, y1)
    pB = ("B", x2, y2)
    svg = _make_svg_plane([pA, pB], lines=[("A", "B")])
    diag = {"kind": "inline_svg", "svg": svg, "alt_text": "Straight line through points A and B"}

    coordA = _coord(x1, y1)
    coordB = _coord(x2, y2)
    prompt = (
        f"In the accompanying Cartesian diagram, the straight line passes through points $A{coordA}$ and $B{coordB}$. "
        f"Determine the equation of the line in the form $y = mx + c$."
    )
    steps = [
        {"rule": "Calculate gradient m", "op": f"m = \frac{{{y2} - ({y1})}}{{{x2} - ({x1})}}", "to": f"m = \frac{{{y2 - y1}}}{{{dx}}} = {m}"},
        {"rule": "Substitute point A into y = mx + c", "op": f"{y1} = {m}({x1}) + c", "to": f"c = {c}"},
        {"rule": "Write final equation", "op": f"y = mx + c", "to": ans.replace("$", "")},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="First calculate the gradient m using m = (y_2 - y_1) / (x_2 - x_1).",
        t2="Then substitute either point into y = mx + c to find the y-intercept c.",
        t3=f"m = {m}, then c = {y1} - ({m})({x1}) = {c}, giving {ans}.",
        misconceptions=["inverted_gradient_dx_dy", "sign_error_in_gradient", "wrong_intercept_calculation"],
        marks=3,
        diagram_spec=diag,
    )


def _build_29(rng: random.Random) -> Dict[str, Any]:
    sub = "29_equation_of_line_parallel_to_given_line"
    m = rng.choice([-4, -3, -2, -1, 2, 3, 4])
    c1 = rng.choice([-5, -3, -1, 1, 3, 5])
    x1 = rng.choice([-4, -3, -2, -1, 1, 2, 3, 4])
    y1 = rng.choice([-5, -4, -2, 0, 2, 4, 5])
    # Ensure point does not lie on line 1
    if y1 == m * x1 + c1:
        y1 += 2
    c2 = y1 - m * x1

    ans = f"${_fmt_line_eq(m, 1, c2, 1)}$"
    d1 = f"${_fmt_line_eq(-m, 1, c2, 1)}$"
    d2 = f"${_fmt_line_eq(m, 1, c1, 1)}$"
    d3 = f"${_fmt_line_eq(m, 1, -c2, 1)}$"
    opts = [ans, d1, d2, d3]
    rng.shuffle(opts)

    line1_str = _fmt_line_eq(m, 1, c1, 1)
    pt_str = _coord(x1, y1)
    prompt = (
        f"Determine the equation of the straight line that is parallel to the line ${line1_str}$ "
        f"and passes through the point $P{pt_str}$."
    )
    steps = [
        {"rule": "Identify parallel gradient", "op": f"m_1 = {m} \implies m_2 = {m}", "to": f"m_2 = {m}"},
        {"rule": "Substitute point P into point-slope equation", "op": f"y - ({y1}) = {m}(x - ({x1}))", "to": f"y = {m}x + ({c2})"},
        {"rule": "Final equation", "op": f"y = mx + c", "to": ans.replace("$", "")},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="Parallel lines have equal gradients: m_1 = m_2.",
        t2=f"The required line has gradient m = {m}. Substitute P{pt_str} into y = mx + c to find c.",
        t3=f"c = {y1} - ({m})({x1}) = {c2}, giving {ans}.",
        misconceptions=["used_perpendicular_gradient", "copied_same_c", "sign_error_in_c"],
        marks=3,
    )


def _build_30(rng: random.Random) -> Dict[str, Any]:
    sub = "30_equation_of_line_perpendicular_to_given_line"
    m1 = rng.choice([-3, -2, -1, 1, 2, 3])
    # m2 = -1 / m1
    c1 = rng.choice([-4, -2, 1, 3, 5])
    # Choose point P(x1, y1) such that c2 = y1 - m2*x1 is an integer
    # m2 = -1/m1 => x1 should be a multiple of m1
    k = rng.choice([-2, -1, 1, 2])
    x1 = k * m1
    y1 = rng.choice([-4, -2, 0, 2, 4])
    # m2_num = -1, m2_den = m1
    # c2 = y1 - (-1/m1)*x1 = y1 + (x1 / m1) = y1 + k
    c2 = y1 + k
    m2_num = -1 if m1 > 0 else 1
    m2_den = abs(m1)

    ans = f"${_fmt_line_eq(m2_num, m2_den, c2, 1)}$"
    d1 = f"${_fmt_line_eq(m1, 1, c2, 1)}$"
    d2 = f"${_fmt_line_eq(-m2_num, m2_den, c2, 1)}$"
    d3 = f"${_fmt_line_eq(m2_num, m2_den, -c2, 1)}$"
    opts = [ans, d1, d2, d3]
    rng.shuffle(opts)

    line1_str = _fmt_line_eq(m1, 1, c1, 1)
    pt_str = _coord(x1, y1)
    m2_frac = _fmt_frac(m2_num, m2_den)
    prompt = (
        f"Determine the equation of the straight line perpendicular to ${line1_str}$ "
        f"that passes through the point $P{pt_str}$."
    )
    steps = [
        {"rule": "Calculate perpendicular gradient", "op": f"m_1 \times m_2 = -1 \implies m_2 = -\frac{{1}}{{{m1}}}", "to": f"m_2 = {m2_frac}"},
        {"rule": "Substitute point P into linear equation", "op": f"y - ({y1}) = {m2_frac}(x - ({x1}))", "to": f"y = {m2_frac}x + ({c2})"},
        {"rule": "Write final equation", "op": f"y = mx + c", "to": ans.replace("$", "")},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="Perpendicular lines satisfy m_1 * m_2 = -1 (negative reciprocal gradient).",
        t2=f"Since m_1 = {m1}, the perpendicular gradient is m_2 = {m2_frac}.",
        t3=f"Substitute P{pt_str} to find c = {c2}, giving {ans}.",
        misconceptions=["used_parallel_gradient", "forgot_negative_sign_in_reciprocal", "reciprocal_error"],
        marks=3,
    )


def _build_31(rng: random.Random) -> Dict[str, Any]:
    sub = "31_equation_of_perpendicular_bisector"
    # Choose midpoint M(mx, my) integer
    mx = rng.choice([-3, -2, -1, 0, 1, 2, 3])
    my = rng.choice([-3, -2, -1, 0, 1, 2, 3])
    # Segment AB: slope m_AB = 1 or -1 or 2 or -2
    # For integer coordinates and perpendicular slope:
    # If slope m_AB = 1: dx = 2, dy = 2 => A(mx - 2, my - 2), B(mx + 2, my + 2)
    # Then m_perp = -1, passes through M(mx, my)
    # c_perp = my - (-1)*mx = my + mx
    m_case = rng.choice([1, -1])
    dx = rng.choice([2, 3, 4])
    dy = m_case * dx
    x1, y1 = mx - dx, my - dy
    x2, y2 = mx + dx, my + dy
    m_perp = -1 if m_case == 1 else 1
    c_perp = my - m_perp * mx

    ans = f"${_fmt_line_eq(m_perp, 1, c_perp, 1)}$"
    d1 = f"${_fmt_line_eq(m_case, 1, c_perp, 1)}$"
    d2 = f"${_fmt_line_eq(m_perp, 1, -c_perp, 1)}$"
    d3 = f"${_fmt_line_eq(m_perp, 1, my, 1)}$"
    opts = [ans, d1, d2, d3]
    rng.shuffle(opts)

    pA = ("A", x1, y1)
    pB = ("B", x2, y2)
    pM = ("M", mx, my)
    svg = _make_svg_plane([pA, pB, pM], lines=[("A", "B")])
    diag = {"kind": "inline_svg", "svg": svg, "alt_text": "Perpendicular bisector of segment AB"}

    coordA = _coord(x1, y1)
    coordB = _coord(x2, y2)
    coordM = _coord(mx, my)
    prompt = (
        f"In the accompanying Cartesian diagram, line segment $AB$ connects points $A{coordA}$ and $B{coordB}$. "
        f"Determine the equation of the perpendicular bisector of segment $AB$ in the form $y = mx + c$."
    )
    steps = [
        {"rule": "Find midpoint M of AB", "op": f"M = \left(\frac{{{x1} + ({x2})}}{{2}};\, \frac{{{y1} + ({y2})}}{{2}}\right)", "to": f"M{coordM}"},
        {"rule": "Calculate gradient of AB", "op": f"m_{{AB}} = \frac{{{y2} - ({y1})}}{{{x2} - ({x1})}}", "to": f"m_{{AB}} = {m_case}"},
        {"rule": "Determine perpendicular gradient", "op": f"m_\perp \times m_{{AB}} = -1", "to": f"m_\perp = {m_perp}"},
        {"rule": "Find equation of perpendicular line through M", "op": f"y - ({my}) = {m_perp}(x - ({mx}))", "to": ans.replace("$", "")},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="A perpendicular bisector passes through the midpoint M of the segment at a 90° angle.",
        t2=f"Midpoint M = {coordM}, gradient of AB is {m_case}, so perpendicular gradient is {m_perp}.",
        t3=f"Substitute M{coordM} into y - y_M = m_perp(x - x_M) to get {ans}.",
        misconceptions=["used_endpoint_instead_of_midpoint", "used_parallel_gradient", "arithmetic_midpoint_error"],
        marks=4,
        diagram_spec=diag,
    )


def _build_32(rng: random.Random) -> Dict[str, Any]:
    sub = "32_equation_of_median_in_triangle"
    # Vertex A, vertices B and C. Median from A to midpoint of BC.
    # Choose B and C so midpoint M_BC is integer.
    mx = rng.choice([-2, -1, 0, 1, 2])
    my = rng.choice([-2, -1, 0, 1, 2])
    dx = rng.choice([2, 4])
    dy = rng.choice([2, 4])
    xB, yB = mx - dx // 2, my - dy // 2
    xC, yC = mx + dx // 2, my + dy // 2
    # Choose A such that slope from A to M is integer
    m_AM = rng.choice([-2, -1, 1, 2])
    step_x = rng.choice([1, 2, 3])
    xA = mx + step_x
    yA = my + m_AM * step_x
    cA = yA - m_AM * xA  # which equals my - m_AM * mx

    ans = f"${_fmt_line_eq(m_AM, 1, cA, 1)}$"
    d1 = f"${_fmt_line_eq(-m_AM, 1, cA, 1)}$"
    d2 = f"${_fmt_line_eq(m_AM, 1, -cA, 1)}$"
    d3 = f"${_fmt_line_eq(m_AM, 1, yA, 1)}$"
    opts = [ans, d1, d2, d3]
    rng.shuffle(opts)

    pA = ("A", xA, yA)
    pB = ("B", xB, yB)
    pC = ("C", xC, yC)
    pM = ("M", mx, my)
    svg = _make_svg_plane([pA, pB, pC, pM], lines=[("A", "B"), ("B", "C"), ("C", "A"), ("A", "M")])
    diag = {"kind": "inline_svg", "svg": svg, "alt_text": "Median AM of triangle ABC"}

    coordA = _coord(xA, yA)
    coordB = _coord(xB, yB)
    coordC = _coord(xC, yC)
    coordM = _coord(mx, my)
    prompt = (
        f"In the accompanying Cartesian diagram, triangle $ABC$ has vertices $A{coordA}$, $B{coordB}$, and $C{coordC}$. "
        f"Determine the equation of the median passing through vertex $A$ and the midpoint $M$ of side $BC$."
    )
    steps = [
        {"rule": "Calculate midpoint M of side BC", "op": f"M = \left(\frac{{{xB} + ({xC})}}{{2}};\, \frac{{{yB} + ({yC})}}{{2}}\right)", "to": f"M{coordM}"},
        {"rule": "Calculate gradient of line AM", "op": f"m = \frac{{{my} - ({yA})}}{{{mx} - ({xA})}}", "to": f"m = {m_AM}"},
        {"rule": "Determine equation through A and M", "op": f"y - ({yA}) = {m_AM}(x - ({xA}))", "to": ans.replace("$", "")},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="A median in a triangle is a line segment drawn from a vertex to the midpoint of the opposite side.",
        t2=f"Calculate the midpoint M of side BC: M = {coordM}.",
        t3=f"Find the gradient of AM (m = {m_AM}) and substitute into y = mx + c to obtain {ans}.",
        misconceptions=["confused_median_with_altitude", "midpoint_formula_error", "sign_error_in_slope"],
        marks=4,
        diagram_spec=diag,
    )


def _build_33(rng: random.Random) -> Dict[str, Any]:
    sub = "33_equation_of_altitude_in_triangle"
    # Altitude from A perpendicular to side BC.
    # Choose B and C so slope m_BC is 1 or -1 or 2 or -2
    m_BC = rng.choice([-2, -1, 1, 2])
    xB = rng.choice([-4, -3, -2, -1, 0])
    dx = 2
    xC = xB + dx
    yB = rng.choice([-3, -2, -1, 0, 1])
    yC = yB + m_BC * dx

    # Altitude gradient m_alt = -1 / m_BC
    # If m_BC in [1, -1], m_alt is integer
    # If m_BC in [2, -2], m_alt is -1/2 or 1/2
    if abs(m_BC) == 1:
        m_alt = -m_BC
        m_num, m_den = m_alt, 1
    else:
        m_num = -1 if m_BC > 0 else 1
        m_den = 2

    # Choose A such that c_alt is integer: c = yA - (m_num/m_den)*xA => xA multiple of m_den
    xA = rng.choice([-2, 0, 2, 4])
    yA = rng.choice([3, 4, 5, 6])
    c_alt = yA - (m_num * xA) // m_den

    ans = f"${_fmt_line_eq(m_num, m_den, c_alt, 1)}$"
    d1 = f"${_fmt_line_eq(m_BC, 1, c_alt, 1)}$"
    d2 = f"${_fmt_line_eq(-m_num, m_den, c_alt, 1)}$"
    d3 = f"${_fmt_line_eq(m_num, m_den, -c_alt, 1)}$"
    opts = [ans, d1, d2, d3]
    rng.shuffle(opts)

    pA = ("A", xA, yA)
    pB = ("B", xB, yB)
    pC = ("C", xC, yC)
    svg = _make_svg_plane([pA, pB, pC], lines=[("A", "B"), ("B", "C"), ("C", "A")])
    diag = {"kind": "inline_svg", "svg": svg, "alt_text": "Altitude from vertex A in triangle ABC"}

    coordA = _coord(xA, yA)
    coordB = _coord(xB, yB)
    coordC = _coord(xC, yC)
    m_alt_str = _fmt_frac(m_num, m_den)
    prompt = (
        f"In the accompanying Cartesian diagram, triangle $ABC$ has vertices $A{coordA}$, $B{coordB}$, and $C{coordC}$. "
        f"Determine the equation of the altitude from vertex $A$ perpendicular to side $BC$."
    )
    steps = [
        {"rule": "Calculate gradient of side BC", "op": f"m_{{BC}} = \frac{{{yC} - ({yB})}}{{{xC} - ({xB})}}", "to": f"m_{{BC}} = {m_BC}"},
        {"rule": "Find perpendicular altitude gradient", "op": f"m_{{alt}} \times m_{{BC}} = -1", "to": f"m_{{alt}} = {m_alt_str}"},
        {"rule": "Determine line equation through vertex A", "op": f"y - ({yA}) = {m_alt_str}(x - ({xA}))", "to": ans.replace("$", "")},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="An altitude in a triangle is a line segment from a vertex perpendicular to the opposite side.",
        t2=f"Calculate the gradient of side BC (m_BC = {m_BC}) and find the perpendicular gradient m_alt = {m_alt_str}.",
        t3=f"Substitute vertex A{coordA} into y - y_A = m_alt(x - x_A) to get {ans}.",
        misconceptions=["confused_altitude_with_median", "used_parallel_slope", "perpendicular_reciprocal_sign_error"],
        marks=4,
        diagram_spec=diag,
    )


def _build_34(rng: random.Random) -> Dict[str, Any]:
    sub = "34_line_intercepts_with_axes"
    a = rng.choice([2, 3, 4, 5])
    b = rng.choice([2, 3, 4, 6])
    c = a * b * rng.choice([-2, -1, 1, 2])
    x_int = c // a
    y_int = c // b

    ans = f"$x\text{{-intercept}}: ({x_int};\, 0),\; y\text{{-intercept}}: (0;\, {y_int})$"
    d1 = f"$x\text{{-intercept}}: (0;\, {x_int}),\; y\text{{-intercept}}: ({y_int};\, 0)$"
    d2 = f"$x\text{{-intercept}}: ({-x_int};\, 0),\; y\text{{-intercept}}: (0;\, {y_int})$"
    d3 = f"$x\text{{-intercept}}: ({y_int};\, 0),\; y\text{{-intercept}}: (0;\, {x_int})$"
    opts = [ans, d1, d2, d3]
    rng.shuffle(opts)

    prompt = (
        f"Determine both the $x$-intercept and $y$-intercept of the straight line with equation "
        f"${a}x + {b}y = {c}$."
    )
    steps = [
        {"rule": "Calculate x-intercept by setting y = 0", "op": f"{a}x + {b}(0) = {c} \implies {a}x = {c}", "to": f"x = {x_int} \implies ({x_int};\, 0)"},
        {"rule": "Calculate y-intercept by setting x = 0", "op": f"{a}(0) + {b}y = {c} \implies {b}y = {c}", "to": f"y = {y_int} \implies (0;\, {y_int})"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="For the x-intercept, set y = 0 and solve for x. For the y-intercept, set x = 0 and solve for y.",
        t2=f"x = {c}/{a} = {x_int}, and y = {c}/{b} = {y_int}.",
        t3=f"Write intercepts as coordinate points: ({x_int}; 0) and (0; {y_int}).",
        misconceptions=["swapped_x_and_y_intercepts", "forgot_zero_in_coordinate_pair", "division_sign_error"],
        marks=3,
    )


def _build_35(rng: random.Random) -> Dict[str, Any]:
    sub = "35_point_lies_on_line_test"
    m = rng.choice([-3, -2, -1, 1, 2, 3, 4])
    c = rng.choice([-6, -4, -2, 1, 3, 5])
    k_val = rng.choice([-4, -3, -2, -1, 1, 2, 3, 4])
    y_val = m * k_val + c

    ans = f"$k = {k_val}$"
    d1 = f"$k = {-k_val}$"
    d2 = f"$k = {k_val + 2}$"
    d3 = f"$k = {k_val - 2}$"
    opts = [ans, d1, d2, d3]
    rng.shuffle(opts)

    line_str = _fmt_line_eq(m, 1, c, 1)
    prompt = (
        f"The point $P(k;\, {y_val})$ lies on the straight line with equation ${line_str}$. "
        f"Calculate the value of $k$."
    )
    steps = [
        {"rule": "Substitute point coordinates into equation", "op": f"y = mx + c \implies {y_val} = {m}(k) + ({c})", "to": f"{y_val} = {m}k + ({c})"},
        {"rule": "Isolate the variable term", "op": f"{m}k = {y_val} - ({c})", "to": f"{m}k = {y_val - c}"},
        {"rule": "Solve for k", "op": f"k = \frac{{{y_val - c}}}{{{m}}}", "to": ans.replace("$", "")},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="Substitute the given x and y values of the point into the line equation.",
        t2=f"Substitute y = {y_val} and x = k into {line_str}: {y_val} = {m}k + {c}.",
        t3=f"Solve for k: {m}k = {y_val - c} => k = {k_val}.",
        misconceptions=["swapped_k_into_y", "sign_error_transposition", "division_error"],
        marks=2,
    )


def _build_36(rng: random.Random) -> Dict[str, Any]:
    sub = "36_point_of_intersection_of_two_lines"
    # Choose intersection point P(px, py)
    px = rng.choice([-3, -2, -1, 1, 2, 3])
    py = rng.choice([-4, -2, 0, 2, 4])
    m1 = rng.choice([1, 2, 3])
    m2 = rng.choice([-2, -1, -3])
    c1 = py - m1 * px
    c2 = py - m2 * px

    ans = f"${_coord(px, py)}$"
    d1 = f"${_coord(-px, py)}$"
    d2 = f"${_coord(px, -py)}$"
    d3 = f"${_coord(py, px)}$"
    opts = [ans, d1, d2, d3]
    rng.shuffle(opts)

    line1 = _fmt_line_eq(m1, 1, c1, 1)
    line2 = _fmt_line_eq(m2, 1, c2, 1)

    pP = ("P", px, py)
    svg = _make_svg_plane([pP])
    diag = {"kind": "inline_svg", "svg": svg, "alt_text": "Intersection of two straight lines"}

    prompt = (
        f"In the accompanying Cartesian diagram, the straight lines with equations "
        f"${line1}$ and ${line2}$ intersect at point $P$. "
        f"Calculate the coordinates of the point of intersection $P$."
    )
    steps = [
        {"rule": "Equate the two line equations", "op": f"{line1.replace('y = ', '')} = {line2.replace('y = ', '')}", "to": f"({m1} - ({m2}))x = {c2} - ({c1})"},
        {"rule": "Solve for x", "op": f"{m1 - m2}x = {c2 - c1}", "to": f"x = {px}"},
        {"rule": "Substitute x to find y", "op": f"y = {m1}({px}) + ({c1})", "to": f"y = {py}"},
        {"rule": "Write coordinates of intersection", "op": "P(x; y)", "to": ans.replace("$", "")},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="To find where two straight lines intersect, equate their expressions for y and solve for x.",
        t2=f"Equate: {line1.replace('y = ', '')} = {line2.replace('y = ', '')} and solve for x = {px}.",
        t3=f"Substitute x = {px} into either equation to get y = {py}, yielding {ans}.",
        misconceptions=["sign_error_equating", "solved_x_forgot_y", "swapped_x_and_y_in_coord"],
        marks=3,
        diagram_spec=diag,
    )


def _build_37(rng: random.Random) -> Dict[str, Any]:
    sub = "37_parallelogram_properties_opposite_sides_parallel"
    # Create parallelogram ABCD
    xA = rng.choice([-5, -4, -3])
    yA = rng.choice([-3, -2, -1])
    dx1 = rng.choice([3, 4, 5])
    dy1 = rng.choice([0, 1, 2])
    xB, yB = xA + dx1, yA + dy1
    dx2 = rng.choice([1, 2, 3])
    dy2 = rng.choice([3, 4, 5])
    xC, yC = xB + dx2, yB + dy2
    xD, yD = xA + dx2, yA + dy2

    m_AB = _fmt_frac(yB - yA, xB - xA)
    m_DC = _fmt_frac(yC - yD, xC - xD)
    m_AD = _fmt_frac(yD - yA, xD - xA)
    m_BC = _fmt_frac(yC - yB, xC - xB)

    ans = f"$m_{{AB}} = m_{{DC}} = {m_AB}\quad\text{{and}}\quad m_{{AD}} = m_{{BC}} = {m_AD}$"
    d1 = f"$m_{{AB}} = m_{{BC}} = {m_AB}\quad\text{{and}}\quad m_{{AD}} = m_{{DC}} = {m_AD}$"
    d2 = f"$m_{{AB}} = -m_{{DC}} = {m_AB}\quad\text{{and}}\quad m_{{AD}} = -m_{{BC}} = {m_AD}$"
    d3 = f"$m_{{AB}} = m_{{DC}} = {m_AD}\quad\text{{and}}\quad m_{{AD}} = m_{{BC}} = {m_AB}$"
    opts = [ans, d1, d2, d3]
    rng.shuffle(opts)

    pA = ("A", xA, yA)
    pB = ("B", xB, yB)
    pC = ("C", xC, yC)
    pD = ("D", xD, yD)
    svg = _make_svg_plane([pA, pB, pC, pD], lines=[("A", "B"), ("B", "C"), ("C", "D"), ("D", "A")])
    diag = {"kind": "inline_svg", "svg": svg, "alt_text": "Parallelogram ABCD on Cartesian plane"}

    coordA = _coord(xA, yA)
    coordB = _coord(xB, yB)
    coordC = _coord(xC, yC)
    coordD = _coord(xD, yD)
    prompt = (
        f"In the accompanying Cartesian diagram, quadrilateral $ABCD$ has vertices $A{coordA}$, $B{coordB}$, "
        f"$C{coordC}$, and $D{coordD}$. Verify that $ABCD$ is a parallelogram by determining the gradients of opposite sides."
    )
    steps = [
        {"rule": "Calculate gradients of horizontal opposite sides", "op": f"m_{{AB}} = \frac{{{yB} - ({yA})}}{{{xB} - ({xA})}},\; m_{{DC}} = \frac{{{yC} - ({yD})}}{{{xC} - ({xD})}}", "to": f"m_{{AB}} = m_{{DC}} = {m_AB}"},
        {"rule": "Calculate gradients of slanted opposite sides", "op": f"m_{{AD}} = \frac{{{yD} - ({yA})}}{{{xD} - ({xA})}},\; m_{{BC}} = \frac{{{yC} - ({yB})}}{{{xC} - ({xB})}}", "to": f"m_{{AD}} = m_{{BC}} = {m_AD}"},
        {"rule": "Conclude parallelogram", "op": "Both pairs of opposite sides are parallel", "to": ans.replace("$", "")},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="A quadrilateral is a parallelogram if both pairs of opposite sides are parallel (equal gradients).",
        t2=f"Check m_AB = m_DC = {m_AB} and m_AD = m_BC = {m_AD}.",
        t3=f"Since opposite sides have equal gradients, ABCD is a parallelogram: {ans}.",
        misconceptions=["compared_adjacent_sides", "inverted_gradient_formula", "sign_error_in_differences"],
        marks=4,
        diagram_spec=diag,
    )


def _build_38(rng: random.Random) -> Dict[str, Any]:
    sub = "38_parallelogram_properties_opposite_sides_equal"
    xA = rng.choice([-4, -3, -2])
    yA = rng.choice([-3, -2, -1])
    dx1, dy1 = rng.choice([(4, 0), (3, 0), (5, 0)])
    xB, yB = xA + dx1, yA + dy1
    dx2, dy2 = rng.choice([(2, 3), (1, 4), (2, 4)])
    xC, yC = xB + dx2, yB + dy2
    xD, yD = xA + dx2, yA + dy2

    len_AB_sq = (xB - xA) ** 2 + (yB - yA) ** 2
    len_AD_sq = (xD - xA) ** 2 + (yD - yA) ** 2

    ans = f"$AB = DC = {math.isqrt(len_AB_sq)}\quad\text{{and}}\quad AD = BC = \sqrt{{{len_AD_sq}}}$"
    d1 = f"$AB = BC = {math.isqrt(len_AB_sq)}\quad\text{{and}}\quad AD = DC = \sqrt{{{len_AD_sq}}}$"
    d2 = f"$AB = DC = \sqrt{{{len_AD_sq}}}\quad\text{{and}}\quad AD = BC = {math.isqrt(len_AB_sq)}$"
    d3 = f"$AB = DC = {len_AB_sq}\quad\text{{and}}\quad AD = BC = {len_AD_sq}$"
    opts = [ans, d1, d2, d3]
    rng.shuffle(opts)

    pA = ("A", xA, yA)
    pB = ("B", xB, yB)
    pC = ("C", xC, yC)
    pD = ("D", xD, yD)
    svg = _make_svg_plane([pA, pB, pC, pD], lines=[("A", "B"), ("B", "C"), ("C", "D"), ("D", "A")])
    diag = {"kind": "inline_svg", "svg": svg, "alt_text": "Parallelogram side lengths on Cartesian plane"}

    coordA = _coord(xA, yA)
    coordB = _coord(xB, yB)
    coordC = _coord(xC, yC)
    coordD = _coord(xD, yD)
    prompt = (
        f"In the accompanying Cartesian diagram, quadrilateral $ABCD$ has vertices $A{coordA}$, $B{coordB}$, "
        f"$C{coordC}$, and $D{coordD}$. Verify that $ABCD$ is a parallelogram by calculating the lengths of opposite sides."
    )
    steps = [
        {"rule": "Calculate lengths of AB and DC", "op": f"AB = \sqrt{{({xB} - {xA})^2 + ({yB} - {yA})^2}}", "to": f"AB = DC = {math.isqrt(len_AB_sq)}"},
        {"rule": "Calculate lengths of AD and BC", "op": f"AD = \sqrt{{({xD} - {xA})^2 + ({yD} - {yA})^2}}", "to": f"AD = BC = \sqrt{{{len_AD_sq}}}"},
        {"rule": "Conclude opposite sides equal", "op": "Both pairs of opposite sides are equal in length", "to": ans.replace("$", "")},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="A quadrilateral is a parallelogram if both pairs of opposite sides are equal in length.",
        t2="Apply the distance formula d = sqrt((x_2 - x_1)^2 + (y_2 - y_1)^2) to each pair of opposite sides.",
        t3=f"Calculate AB = DC = {math.isqrt(len_AB_sq)} and AD = BC = sqrt({len_AD_sq}): {ans}.",
        misconceptions=["forgot_square_root", "computed_adjacent_sides", "arithmetic_error_in_distance"],
        marks=4,
        diagram_spec=diag,
    )


def _build_39(rng: random.Random) -> Dict[str, Any]:
    sub = "39_parallelogram_diagonals_bisect_each_other"
    # Choose midpoint of diagonals M(mx, my) integer
    mx = rng.choice([-1, 0, 1, 2])
    my = rng.choice([-1, 0, 1, 2])
    # A and C symmetric around M
    dx1, dy1 = rng.choice([(3, 2), (4, 1), (3, 3)])
    xA, yA = mx - dx1, my - dy1
    xC, yC = mx + dx1, my + dy1
    # B and D symmetric around M
    dx2, dy2 = rng.choice([(2, -3), (1, -4), (3, -2)])
    xB, yB = mx - dx2, my - dy2
    xD, yD = mx + dx2, my + dy2

    mid_str = _coord(mx, my)
    ans = f"Midpoint of $AC$ = Midpoint of $BD$ = ${mid_str}$"
    d1 = f"Midpoint of $AC$ = ${mid_str}$, Midpoint of $BD$ = ${_coord(mx + 1, my)}$"
    d2 = f"Midpoint of $AB$ = Midpoint of $CD$ = ${mid_str}$"
    d3 = f"Midpoint of $AC$ = Midpoint of $BD$ = ${_coord(-mx, -my)}$"
    opts = [ans, d1, d2, d3]
    rng.shuffle(opts)

    pA = ("A", xA, yA)
    pB = ("B", xB, yB)
    pC = ("C", xC, yC)
    pD = ("D", xD, yD)
    pM = ("M", mx, my)
    svg = _make_svg_plane([pA, pB, pC, pD, pM], lines=[("A", "B"), ("B", "C"), ("C", "D"), ("D", "A"), ("A", "C"), ("B", "D")])
    diag = {"kind": "inline_svg", "svg": svg, "alt_text": "Diagonals of parallelogram bisecting each other"}

    coordA = _coord(xA, yA)
    coordB = _coord(xB, yB)
    coordC = _coord(xC, yC)
    coordD = _coord(xD, yD)
    prompt = (
        f"In the accompanying Cartesian diagram, quadrilateral $ABCD$ has vertices $A{coordA}$, $B{coordB}$, "
        f"$C{coordC}$, and $D{coordD}$. Determine the midpoints of diagonals $AC$ and $BD$ to show that they bisect each other."
    )
    steps = [
        {"rule": "Calculate midpoint of diagonal AC", "op": f"M_{{AC}} = \left(\frac{{{xA} + ({xC})}}{{2}};\, \frac{{{yA} + ({yC})}}{{2}}\right)", "to": f"M_{{AC}} = {mid_str}"},
        {"rule": "Calculate midpoint of diagonal BD", "op": f"M_{{BD}} = \left(\frac{{{xB} + ({xD})}}{{2}};\, \frac{{{yB} + ({yD})}}{{2}}\right)", "to": f"M_{{BD}} = {mid_str}"},
        {"rule": "Conclude diagonals bisect each other", "op": "M_{AC} = M_{BD} \implies \text{diagonals bisect}", "to": ans},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="A quadrilateral is a parallelogram if and only if its diagonals bisect each other (have the same midpoint).",
        t2=f"Calculate the midpoint of AC and the midpoint of BD using ((x_1 + x_2)/2; (y_1 + y_2)/2).",
        t3=f"Both midpoints equal {mid_str}, confirming that ABCD is a parallelogram.",
        misconceptions=["calculated_sides_midpoints_instead_of_diagonals", "subtraction_in_midpoint", "sign_error"],
        marks=4,
        diagram_spec=diag,
    )


def _build_40(rng: random.Random) -> Dict[str, Any]:
    sub = "40_find_fourth_vertex_of_parallelogram"
    # Given A, B, C of parallelogram ABCD, find D.
    # D = A + C - B
    xA = rng.choice([-4, -3, -2, -1])
    yA = rng.choice([-3, -2, -1, 0])
    dx = rng.choice([3, 4, 5])
    dy = rng.choice([0, 1, 2])
    xB, yB = xA + dx, yA + dy
    dx2 = rng.choice([1, 2, 3])
    dy2 = rng.choice([3, 4, 5])
    xC, yC = xB + dx2, yB + dy2
    xD = xA + xC - xB
    yD = yA + yC - yB

    ans = f"$D{_coord(xD, yD)}$"
    d1 = f"$D{_coord(-xD, yD)}$"
    d2 = f"$D{_coord(xD, -yD)}$"
    d3 = f"$D{_coord(xB + xC - xA, yB + yC - yA)}$"
    opts = [ans, d1, d2, d3]
    rng.shuffle(opts)

    pA = ("A", xA, yA)
    pB = ("B", xB, yB)
    pC = ("C", xC, yC)
    pD = ("D", xD, yD)
    svg = _make_svg_plane([pA, pB, pC, pD], lines=[("A", "B"), ("B", "C"), ("C", "D"), ("D", "A")])
    diag = {"kind": "inline_svg", "svg": svg, "alt_text": "Finding fourth vertex D of parallelogram ABCD"}

    coordA = _coord(xA, yA)
    coordB = _coord(xB, yB)
    coordC = _coord(xC, yC)
    prompt = (
        f"In the accompanying Cartesian diagram, $ABCD$ is a parallelogram with given vertices "
        f"$A{coordA}$, $B{coordB}$, and $C{coordC}$. Determine the coordinates of the fourth vertex $D$."
    )
    steps = [
        {"rule": "Use midpoint property of diagonals", "op": "\frac{x_A + x_C}{2} = \frac{x_B + x_D}{2} \implies x_D = x_A + x_C - x_B", "to": f"x_D = {xA} + ({xC}) - ({xB}) = {xD}"},
        {"rule": "Solve for y_D coordinate", "op": "\frac{y_A + y_C}{2} = \frac{y_B + y_D}{2} \implies y_D = y_A + y_C - y_B", "to": f"y_D = {yA} + ({yC}) - ({yB}) = {yD}"},
        {"rule": "Write coordinates of vertex D", "op": "D(x_D; y_D)", "to": ans.replace("$", "")},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="Since diagonals AC and BD bisect each other, their midpoints are equal: M_AC = M_BD.",
        t2=f"x_D = x_A + x_C - x_B = {xA} + {xC} - ({xB}) = {xD}, and y_D = y_A + y_C - y_B = {yA} + {yC} - ({yB}) = {yD}.",
        t3=f"The coordinates of D are {ans}.",
        misconceptions=["used_vector_formula_in_wrong_order", "sign_error_subtracting_B", "swapped_A_and_C"],
        marks=3,
        diagram_spec=diag,
    )


def _build_41(rng: random.Random) -> Dict[str, Any]:
    sub = "41_rectangle_proof_parallelogram_with_right_angle"
    # Rectangle vertices: adjacent sides perpendicular
    xA = rng.choice([-4, -3, -2])
    yA = rng.choice([-3, -2, -1])
    # AB horizontal or angled
    # Let AB have vector (4, 2), then AD has vector (-2, 4) or (-1, 2)
    # dx1=4, dy1=2 => m_AB = 1/2. Perpendicular vector: dx2=-2, dy2=4 => m_AD = -2. Product = -1!
    dx1, dy1 = 4, 2
    dx2, dy2 = -2, 4
    xB, yB = xA + dx1, yA + dy1
    xC, yC = xB + dx2, yB + dy2
    xD, yD = xA + dx2, yA + dy2

    m_AB = "\frac{1}{2}"
    m_BC = "-2"

    ans = f"$m_{{AB}} = \frac{{1}}{{2}},\; m_{{BC}} = -2 \implies m_{{AB}} \times m_{{BC}} = -1$"
    d1 = f"$m_{{AB}} = \frac{{1}}{{2}},\; m_{{BC}} = 2 \implies m_{{AB}} \times m_{{BC}} = 1$"
    d2 = f"$m_{{AB}} = 2,\; m_{{BC}} = -\frac{{1}}{{2}} \implies m_{{AB}} \times m_{{BC}} = -1$"
    d3 = f"$m_{{AB}} = 1,\; m_{{BC}} = -1 \implies m_{{AB}} \times m_{{BC}} = -1$"
    opts = [ans, d1, d2, d3]
    rng.shuffle(opts)

    pA = ("A", xA, yA)
    pB = ("B", xB, yB)
    pC = ("C", xC, yC)
    pD = ("D", xD, yD)
    svg = _make_svg_plane([pA, pB, pC, pD], lines=[("A", "B"), ("B", "C"), ("C", "D"), ("D", "A")])
    diag = {"kind": "inline_svg", "svg": svg, "alt_text": "Rectangle ABCD on Cartesian plane"}

    coordA = _coord(xA, yA)
    coordB = _coord(xB, yB)
    coordC = _coord(xC, yC)
    coordD = _coord(xD, yD)
    prompt = (
        f"In the accompanying Cartesian diagram, quadrilateral $ABCD$ has vertices $A{coordA}$, $B{coordB}$, "
        f"$C{coordC}$, and $D{coordD}$. Prove that $ABCD$ is a rectangle by verifying that adjacent sides $AB$ and $BC$ are perpendicular."
    )
    steps = [
        {"rule": "Calculate gradient of side AB", "op": f"m_{{AB}} = \frac{{{yB} - ({yA})}}{{{xB} - ({xA})}}", "to": "m_{AB} = \frac{1}{2}"},
        {"rule": "Calculate gradient of adjacent side BC", "op": f"m_{{BC}} = \frac{{{yC} - ({yB})}}{{{xC} - ({xB})}}", "to": "m_{BC} = -2"},
        {"rule": "Check perpendicularity condition", "op": "m_{AB} \times m_{BC} = \left(\frac{1}{2}\right)(-2)", "to": "-1 \implies AB \perp BC"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="A rectangle is a parallelogram with at least one right angle (adjacent sides perpendicular).",
        t2="Calculate m_AB and m_BC, then verify that m_AB * m_BC = -1.",
        t3=f"m_AB = 1/2, m_BC = -2, and (1/2)(-2) = -1: {ans}.",
        misconceptions=["multiplied_opposite_sides", "forgot_negative_one_condition", "reciprocal_arithmetic_error"],
        marks=4,
        diagram_spec=diag,
    )


def _build_42(rng: random.Random) -> Dict[str, Any]:
    sub = "42_rhombus_proof_parallelogram_with_perpendicular_diagonals"
    # Rhombus: diagonals are perpendicular (m_AC * m_BD = -1)
    # Choose center M(0, 0)
    # AC along x-axis or angle, BD perpendicular
    # Let A(-3, 0), C(3, 0), B(0, -4), D(0, 4)
    a_val = rng.choice([3, 4, 5])
    b_val = rng.choice([2, 3, 4])
    xA, yA = -a_val, 0
    xC, yC = a_val, 0
    xB, yB = 0, -b_val
    xD, yD = 0, b_val

    ans = "Diagonals are perpendicular: $AC$ is horizontal ($m=0$) and $BD$ is vertical ($m$ undefined)"
    d1 = "Diagonals are parallel: $m_{AC} = m_{BD} = 0$"
    d2 = "Diagonals have equal lengths: $AC = BD$"
    d3 = "Diagonals bisect at an angle of $45^\circ$"
    opts = [ans, d1, d2, d3]
    rng.shuffle(opts)

    pA = ("A", xA, yA)
    pB = ("B", xB, yB)
    pC = ("C", xC, yC)
    pD = ("D", xD, yD)
    svg = _make_svg_plane([pA, pB, pC, pD], lines=[("A", "B"), ("B", "C"), ("C", "D"), ("D", "A"), ("A", "C"), ("B", "D")])
    diag = {"kind": "inline_svg", "svg": svg, "alt_text": "Rhombus ABCD with perpendicular diagonals"}

    coordA = _coord(xA, yA)
    coordB = _coord(xB, yB)
    coordC = _coord(xC, yC)
    coordD = _coord(xD, yD)
    prompt = (
        f"In the accompanying Cartesian diagram, quadrilateral $ABCD$ has vertices $A{coordA}$, $B{coordB}$, "
        f"$C{coordC}$, and $D{coordD}$. Prove that $ABCD$ is a rhombus by examining its diagonals $AC$ and $BD$."
    )
    steps = [
        {"rule": "Analyze diagonal AC", "op": f"A({xA}; 0)\\text{{ and }}C({xC}; 0)", "to": "m_{AC} = 0\\;\\text{(horizontal line along x-axis)}"},
        {"rule": "Analyze diagonal BD", "op": f"B(0; {-b_val})\\text{{ and }}D(0; {b_val})", "to": "m_{BD}\\text{ is undefined (vertical line along y-axis)}"},
        {"rule": "Conclude perpendicularity", "op": "Horizontal line \\perp Vertical line", "to": "AC \\perp BD \\implies ABCD\\text{ is a rhombus}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="A parallelogram is a rhombus if its diagonals intersect at right angles (perpendicular diagonals).",
        t2="Examine the slopes or orientations of diagonal AC and diagonal BD.",
        t3="AC is horizontal and BD is vertical, meaning they are perpendicular, proving ABCD is a rhombus.",
        misconceptions=["confused_rhombus_with_rectangle", "thought_diagonals_must_be_equal", "slope_undefined_confusion"],
        marks=3,
        diagram_spec=diag,
    )


def _build_43(rng: random.Random) -> Dict[str, Any]:
    sub = "43_square_proof_all_sides_equal_and_perpendicular"
    # Square: side length s
    s = rng.choice([3, 4, 5])
    xA, yA = 0, 0
    xB, yB = s, 0
    xC, yC = s, s
    xD, yD = 0, s

    ans = f"All 4 sides equal ${s}$ units and adjacent sides perpendicular ($m_{{AB}} = 0 \\perp m_{{BC}}\\text{{ undefined}}$)"
    d1 = f"All 4 sides equal ${s}$ units but adjacent sides are not perpendicular"
    d2 = f"Opposite sides are parallel but side lengths are unequal"
    d3 = f"Adjacent sides are perpendicular but side lengths are ${s}$ and ${s+2}$"
    opts = [ans, d1, d2, d3]
    rng.shuffle(opts)

    pA = ("A", xA, yA)
    pB = ("B", xB, yB)
    pC = ("C", xC, yC)
    pD = ("D", xD, yD)
    svg = _make_svg_plane([pA, pB, pC, pD], lines=[("A", "B"), ("B", "C"), ("C", "D"), ("D", "A")])
    diag = {"kind": "inline_svg", "svg": svg, "alt_text": "Square ABCD on Cartesian plane"}

    coordA = _coord(xA, yA)
    coordB = _coord(xB, yB)
    coordC = _coord(xC, yC)
    coordD = _coord(xD, yD)
    prompt = (
        f"In the accompanying Cartesian diagram, quadrilateral $ABCD$ has vertices $A{coordA}$, $B{coordB}$, "
        f"$C{coordC}$, and $D{coordD}$. Prove that $ABCD$ is a square by checking side lengths and perpendicularity."
    )
    steps = [
        {"rule": "Calculate side lengths", "op": f"AB = BC = CD = DA = {s}", "to": f"\text{{All four sides}} = {s}\text{{ units}}"},
        {"rule": "Verify adjacent sides perpendicular", "op": f"m_{{AB}} = 0\; (\text{{horizontal}}),\; m_{{BC}}\text{{ undefined (vertical)}}", "to": "AB \perp BC"},
        {"rule": "Conclude square", "op": "Equal sides + right angle", "to": ans},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="A square is both a rectangle (right angles) and a rhombus (all four sides equal).",
        t2=f"Check that all 4 sides equal {s} units, and adjacent sides meet at a 90° angle.",
        t3=f"Since all four sides are {s} and AB is perpendicular to BC, ABCD is a square.",
        misconceptions=["confused_square_with_rhombus_only", "checked_only_side_lengths", "forgot_90_degree_check"],
        marks=3,
        diagram_spec=diag,
    )


def _build_44(rng: random.Random) -> Dict[str, Any]:
    sub = "44_trapezium_proof_one_pair_parallel_sides"
    # Trapezium: AB parallel to DC (horizontal), AD not parallel to BC
    base_y1 = rng.choice([-3, -2, -1])
    base_y2 = rng.choice([2, 3, 4])
    w1 = rng.choice([3, 4, 5])
    w2 = rng.choice([1, 2])
    cx = rng.choice([-1, 0, 1])

    xA, yA = cx - w1, base_y1
    xB, yB = cx + w1, base_y1  # AB horizontal (slope 0)
    xD, yD = cx - w2, base_y2
    xC, yC = cx + w2, base_y2  # DC horizontal (slope 0) => AB // DC

    m_AD = _fmt_frac(yD - yA, xD - xA)
    m_BC = _fmt_frac(yC - yB, xC - xB)

    ans = f"$m_{{AB}} = m_{{DC}} = 0\\; (AB \\parallel DC)\\quad\\text{{and}}\\quad m_{{AD}} = {m_AD} \\neq m_{{BC}} = {m_BC}\\; (AD \\not\\parallel BC)$"
    d1 = f"$m_{{AB}} = m_{{DC}} = 0\\quad\\text{{and}}\\quad m_{{AD}} = m_{{BC}} = {m_AD}\\implies\\text{{parallelogram}}$"
    d2 = "$m_{AB} \\neq m_{DC}\\quad\\text{and}\\quad m_{AD} \\neq m_{BC}\\implies\\text{no parallel sides}$"
    d3 = "$m_{AB} \\times m_{DC} = -1\\implies\\text{perpendicular sides}$"
    opts = [ans, d1, d2, d3]
    rng.shuffle(opts)

    pA = ("A", xA, yA)
    pB = ("B", xB, yB)
    pC = ("C", xC, yC)
    pD = ("D", xD, yD)
    svg = _make_svg_plane([pA, pB, pC, pD], lines=[("A", "B"), ("B", "C"), ("C", "D"), ("D", "A")])
    diag = {"kind": "inline_svg", "svg": svg, "alt_text": "Trapezium ABCD on Cartesian plane"}

    coordA = _coord(xA, yA)
    coordB = _coord(xB, yB)
    coordC = _coord(xC, yC)
    coordD = _coord(xD, yD)
    prompt = (
        f"In the accompanying Cartesian diagram, quadrilateral $ABCD$ has vertices $A{coordA}$, $B{coordB}$, "
        f"$C{coordC}$, and $D{coordD}$. Prove that $ABCD$ is a trapezium by determining the gradients of opposite sides."
    )
    steps = [
        {"rule": "Calculate gradients of AB and DC", "op": f"m_{{AB}} = \\frac{{{yB} - ({yA})}}{{{xB} - ({xA})}} = 0,\\; m_{{DC}} = \\frac{{{yC} - ({yD})}}{{{xC} - ({xD})}} = 0", "to": "m_{AB} = m_{DC} = 0 \\implies AB \\parallel DC"},
        {"rule": "Calculate gradients of AD and BC", "op": f"m_{{AD}} = \\frac{{{yD} - ({yA})}}{{{xD} - ({xA})}} = {m_AD},\\; m_{{BC}} = \\frac{{{yC} - ({yB})}}{{{xC} - ({xB})}} = {m_BC}", "to": f"m_{{AD}} \\neq m_{{BC}} \\implies AD \\not\\parallel BC"},
        {"rule": "Conclude trapezium", "op": "Exactly one pair of opposite sides parallel", "to": ans.replace("$", "")},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="A trapezium is a quadrilateral with exactly ONE pair of parallel opposite sides.",
        t2="Calculate the gradients of AB, DC, AD, and BC.",
        t3="m_AB = m_DC = 0 (parallel), while m_AD = 5/2 != m_BC = -5/2 (not parallel), proving it is a trapezium.",
        misconceptions=["thought_trapezium_has_two_parallel_pairs", "sign_error_claiming_slopes_equal", "forgot_to_check_non_parallel_pair"],
        marks=4,
        diagram_spec=diag,
    )


def _build_45(rng: random.Random) -> Dict[str, Any]:
    sub = "45_kite_proof_adjacent_pairs_equal"
    # Kite: two pairs of adjacent sides equal: AB = AD and CB = CD
    # Center on y-axis: A(0, 4), C(0, -3), B(-3, 0), D(3, 0)
    top_y = rng.choice([3, 4, 5])
    bot_y = rng.choice([-2, -3, -4])
    wing_x = rng.choice([2, 3, 4])
    xA, yA = 0, top_y
    xC, yC = 0, bot_y
    xB, yB = -wing_x, 0
    xD, yD = wing_x, 0

    len_top_sq = wing_x**2 + top_y**2
    len_bot_sq = wing_x**2 + bot_y**2

    ans = f"$AB = AD = \sqrt{{{len_top_sq}}}\quad\text{{and}}\quad CB = CD = \sqrt{{{len_bot_sq}}}$"
    d1 = f"$AB = CD = \sqrt{{{len_top_sq}}}\quad\text{{and}}\quad AD = CB = \sqrt{{{len_bot_sq}}}$"
    d2 = f"$AB = AD = {len_top_sq}\quad\text{{and}}\quad CB = CD = {len_bot_sq}$"
    d3 = f"$AB = BC = CD = DA = \sqrt{{{len_top_sq}}}$"
    opts = [ans, d1, d2, d3]
    rng.shuffle(opts)

    pA = ("A", xA, yA)
    pB = ("B", xB, yB)
    pC = ("C", xC, yC)
    pD = ("D", xD, yD)
    svg = _make_svg_plane([pA, pB, pC, pD], lines=[("A", "B"), ("B", "C"), ("C", "D"), ("D", "A"), ("A", "C"), ("B", "D")])
    diag = {"kind": "inline_svg", "svg": svg, "alt_text": "Kite ABCD with adjacent pairs of equal sides"}

    coordA = _coord(xA, yA)
    coordB = _coord(xB, yB)
    coordC = _coord(xC, yC)
    coordD = _coord(xD, yD)
    prompt = (
        f"In the accompanying Cartesian diagram, quadrilateral $ABCD$ has vertices $A{coordA}$, $B{coordB}$, "
        f"$C{coordC}$, and $D{coordD}$. Prove that $ABCD$ is a kite by calculating the lengths of adjacent sides."
    )
    steps = [
        {"rule": "Calculate lengths of adjacent sides AB and AD", "op": f"AB = \sqrt{{({-wing_x} - 0)^2 + (0 - {top_y})^2}},\; AD = \sqrt{{({wing_x} - 0)^2 + (0 - {top_y})^2}}", "to": f"AB = AD = \sqrt{{{len_top_sq}}}"},
        {"rule": "Calculate lengths of adjacent sides CB and CD", "op": f"CB = \sqrt{{({-wing_x} - 0)^2 + (0 - ({bot_y}))^2}},\; CD = \sqrt{{({wing_x} - 0)^2 + (0 - ({bot_y}))^2}}", "to": f"CB = CD = \sqrt{{{len_bot_sq}}}"},
        {"rule": "Conclude kite property", "op": "Two distinct pairs of adjacent sides are equal in length", "to": ans.replace("$", "")},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="A kite is a quadrilateral with two distinct pairs of equal adjacent sides.",
        t2="Calculate distances AB, AD, CB, and CD.",
        t3=f"AB = AD = sqrt({len_top_sq}) and CB = CD = sqrt({len_bot_sq}), proving ABCD is a kite: {ans}.",
        misconceptions=["confused_kite_with_parallelogram", "matched_opposite_sides_instead_of_adjacent", "forgot_square_root"],
        marks=4,
        diagram_spec=diag,
    )


def _build_46(rng: random.Random) -> Dict[str, Any]:
    sub = "46_area_of_triangle_right_angled"
    # Right-angled triangle at B
    b = rng.choice([3, 4, 6, 8])
    h = rng.choice([4, 5, 6, 8, 10])
    area = (b * h) // 2

    xA, yA = 0, h
    xB, yB = 0, 0
    xC, yC = b, 0

    ans = f"$\text{{Area}} = {area}\text{{ sq units}}$"
    d1 = f"$\text{{Area}} = {b * h}\text{{ sq units}}$"
    d2 = f"$\text{{Area}} = {area * 2}\text{{ sq units}}$"
    d3 = f"$\text{{Area}} = {b + h}\text{{ sq units}}$"
    opts = [ans, d1, d2, d3]
    rng.shuffle(opts)

    pA = ("A", xA, yA)
    pB = ("B", xB, yB)
    pC = ("C", xC, yC)
    svg = _make_svg_plane([pA, pB, pC], lines=[("A", "B"), ("B", "C"), ("C", "A")])
    diag = {"kind": "inline_svg", "svg": svg, "alt_text": "Right-angled triangle on Cartesian plane"}

    coordA = _coord(xA, yA)
    coordB = _coord(xB, yB)
    coordC = _coord(xC, yC)
    prompt = (
        f"In the accompanying Cartesian diagram, right-angled triangle $ABC$ has vertices $A{coordA}$, $B{coordB}$, "
        f"and $C{coordC}$ with the right angle at vertex $B$. Calculate the area of triangle $ABC$."
    )
    steps = [
        {"rule": "Determine base length BC", "op": f"BC = {b} - 0", "to": f"\text{{base}} = {b}"},
        {"rule": "Determine perpendicular height AB", "op": f"AB = {h} - 0", "to": f"\text{{height}} = {h}"},
        {"rule": "Calculate area", "op": f"\text{{Area}} = \frac{{1}}{{2}} \times \text{{base}} \times \text{{height}} = \frac{{1}}{{2}} \times {b} \times {h}", "to": ans.replace("$", "")},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="The area of a right-angled triangle is 1/2 * base * height.",
        t2=f"The perpendicular sides are AB = {h} and BC = {b}.",
        t3=f"Area = 1/2 * {b} * {h} = {area} sq units.",
        misconceptions=["forgot_half_factor", "used_hypotenuse_in_area", "added_dimensions_instead_of_multiplying"],
        marks=3,
        diagram_spec=diag,
    )


def _build_47(rng: random.Random) -> Dict[str, Any]:
    sub = "47_area_of_rectangle_or_square_on_cartesian_plane"
    L = rng.choice([4, 5, 6, 7])
    W = rng.choice([2, 3, 4, 5])
    area = L * W

    xA, yA = -2, -1
    xB, yB = xA + L, yA
    xC, yC = xB, yA + W
    xD, yD = xA, yA + W

    ans = f"$\text{{Area}} = {area}\text{{ sq units}}$"
    d1 = f"$\text{{Area}} = {(L + W) * 2}\text{{ sq units}}$"
    d2 = f"$\text{{Area}} = {area // 2}\text{{ sq units}}$"
    d3 = f"$\text{{Area}} = {L**2}\text{{ sq units}}$"
    opts = [ans, d1, d2, d3]
    rng.shuffle(opts)

    pA = ("A", xA, yA)
    pB = ("B", xB, yB)
    pC = ("C", xC, yC)
    pD = ("D", xD, yD)
    svg = _make_svg_plane([pA, pB, pC, pD], lines=[("A", "B"), ("B", "C"), ("C", "D"), ("D", "A")])
    diag = {"kind": "inline_svg", "svg": svg, "alt_text": "Rectangle ABCD on Cartesian plane"}

    coordA = _coord(xA, yA)
    coordB = _coord(xB, yB)
    coordC = _coord(xC, yC)
    coordD = _coord(xD, yD)
    prompt = (
        f"In the accompanying Cartesian diagram, rectangle $ABCD$ has vertices $A{coordA}$, $B{coordB}$, "
        f"$C{coordC}$, and $D{coordD}$. Calculate the area of rectangle $ABCD$."
    )
    steps = [
        {"rule": "Calculate length of side AB", "op": f"AB = {xB} - ({xA})", "to": f"\text{{Length}} = {L}"},
        {"rule": "Calculate width of side BC", "op": f"BC = {yC} - ({yB})", "to": f"\text{{Width}} = {W}"},
        {"rule": "Compute area of rectangle", "op": f"\text{{Area}} = \text{{Length}} \times \text{{Width}} = {L} \times {W}", "to": ans.replace("$", "")},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="The area of a rectangle is length * width.",
        t2=f"Calculate side lengths: AB = {L} and BC = {W}.",
        t3=f"Area = {L} * {W} = {area} sq units.",
        misconceptions=["calculated_perimeter_instead_of_area", "divided_by_two_triangle_formula", "squared_single_side"],
        marks=3,
        diagram_spec=diag,
    )


def _build_48(rng: random.Random) -> Dict[str, Any]:
    sub = "48_distance_from_origin"
    # Point P(x, y) distance from O(0, 0)
    # Use Pythagorean triples: (3, 4)->5, (5, 12)->13, (6, 8)->10, (8, 15)->17
    triples = [(3, 4, 5), (6, 8, 10), (5, 12, 13), (8, 15, 17)]
    base_x, base_y, d_val = rng.choice(triples)
    sx = rng.choice([1, -1])
    sy = rng.choice([1, -1])
    px = base_x * sx
    py = base_y * sy

    ans = f"$OP = {d_val}$"
    d1 = f"$OP = {base_x + base_y}$"
    d2 = f"$OP = {d_val**2}$"
    d3 = f"$OP = {d_val - 1}$"
    opts = [ans, d1, d2, d3]
    rng.shuffle(opts)

    pO = ("O", 0, 0)
    pP = ("P", px, py)
    svg = _make_svg_plane([pO, pP], lines=[("O", "P")])
    diag = {"kind": "inline_svg", "svg": svg, "alt_text": "Distance from origin to point P"}

    coordP = _coord(px, py)
    prompt = (
        f"In the accompanying Cartesian diagram, determine the distance from the origin $O(0;\, 0)$ "
        f"to the point $P{coordP}$."
    )
    steps = [
        {"rule": "Apply distance from origin formula", "op": "OP = \sqrt{x^2 + y^2}", "to": f"OP = \sqrt{{({px})^2 + ({py})^2}}"},
        {"rule": "Calculate sum of squares", "op": f"OP = \sqrt{{{px**2} + {py**2}}}", "to": f"OP = \sqrt{{{d_val**2}}}"},
        {"rule": "Evaluate square root", "op": f"\sqrt{{{d_val**2}}}", "to": ans.replace("$", "")},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="The distance from the origin O(0; 0) to P(x; y) is given by OP = sqrt(x^2 + y^2).",
        t2=f"Calculate ({px})^2 + ({py})^2 = {px**2} + {py**2} = {d_val**2}.",
        t3=f"Take the square root: sqrt({d_val**2}) = {d_val}.",
        misconceptions=["added_coordinates_directly", "forgot_square_root", "squared_negative_improperly"],
        marks=2,
        diagram_spec=diag,
    )


def _build_49(rng: random.Random) -> Dict[str, Any]:
    sub = "49_circle_center_origin_equation_check"
    r = rng.choice([3, 4, 5, 6, 7])
    r_sq = r**2

    # Choose a point: either exactly on circle, inside, or outside
    case = rng.choice(["on", "inside", "outside"])
    if case == "on":
        if r == 5:
            px, py = rng.choice([(3, 4), (-3, 4), (4, -3), (-4, -3)])
        else:
            px, py = rng.choice([(r, 0), (0, r), (-r, 0), (0, -r)])
        val = px**2 + py**2
        ans = "Point $P$ lies on the circle ($x^2 + y^2 = r^2$)"
    elif case == "inside":
        px = rng.randint(0, r - 2)
        py = rng.randint(0, r - 2)
        val = px**2 + py**2
        ans = "Point $P$ lies inside the circle ($x^2 + y^2 < r^2$)"
    else:
        px = r + rng.randint(1, 3)
        py = rng.randint(1, 3)
        val = px**2 + py**2
        ans = "Point $P$ lies outside the circle ($x^2 + y^2 > r^2$)"

    d1 = "Point $P$ lies on the circle ($x^2 + y^2 = r^2$)" if case != "on" else "Point $P$ lies inside the circle ($x^2 + y^2 < r^2$)"
    d2 = "Point $P$ lies inside the circle ($x^2 + y^2 < r^2$)" if case != "inside" else "Point $P$ lies outside the circle ($x^2 + y^2 > r^2$)"
    d3 = "Point $P$ lies outside the circle ($x^2 + y^2 > r^2$)" if case != "outside" else "Point $P$ lies on the circle ($x^2 + y^2 = r^2$)"
    opts = list(set([ans, d1, d2, d3]))
    while len(opts) < 4:
        opts.append(f"Point $P$ lies on the circumference at radius ${r+1}$")
    rng.shuffle(opts)

    svg = _make_svg_circle_plane(r, [("P", px, py)])
    diag = {"kind": "inline_svg", "svg": svg, "alt_text": "Circle centered at origin and point P"}

    coordP = _coord(px, py)
    prompt = (
        f"In the accompanying Cartesian diagram, a circle centered at the origin has the equation "
        f"$x^2 + y^2 = {r_sq}$. Determine whether the point $P{coordP}$ lies on, inside, or outside the circle."
    )
    steps = [
        {"rule": "Calculate x^2 + y^2 for point P", "op": f"({px})^2 + ({py})^2", "to": f"{px**2} + {py**2} = {val}"},
        {"rule": "Compare with r^2", "op": f"{val} \text{{ vs }} {r_sq}", "to": f"{val} {'=' if val==r_sq else ('<' if val < r_sq else '>')} {r_sq}"},
        {"rule": "Conclude position of point", "op": "Position check", "to": ans},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="Substitute the point's coordinates into x^2 + y^2 and compare the result with r^2.",
        t2=f"x^2 + y^2 = ({px})^2 + ({py})^2 = {val}. The circle has r^2 = {r_sq}.",
        t3=f"Since {val} {'=' if val==r_sq else ('<' if val < r_sq else '>')} {r_sq}, {ans}.",
        misconceptions=["compared_with_r_instead_of_r_squared", "arithmetic_error_in_squares", "misinterpreted_inequality"],
        marks=2,
        diagram_spec=diag,
    )


def _build_50(rng: random.Random) -> Dict[str, Any]:
    sub = "50_comprehensive_coordinate_geometry_multi_step_problem"
    # Exam synthesis: triangle ABC. Line through A parallel to BC.
    # Choose B and C with integer gradient
    xB = rng.choice([-5, -4, -3])
    yB = rng.choice([-3, -2, -1])
    dx = rng.choice([2, 3, 4])
    m_BC = rng.choice([-2, -1, 1, 2])
    xC = xB + dx
    yC = yB + m_BC * dx

    # Choose vertex A
    xA = rng.choice([-2, -1, 0, 1, 2])
    yA = rng.choice([3, 4, 5])
    # Line parallel to BC through A: gradient m = m_BC
    c_line = yA - m_BC * xA

    ans = f"${_fmt_line_eq(m_BC, 1, c_line, 1)}$"
    d1 = f"${_fmt_line_eq(-m_BC, 1, c_line, 1)}$"
    d2 = f"${_fmt_line_eq(m_BC, 1, -c_line, 1)}$"
    d3 = f"${_fmt_line_eq(m_BC, 1, yA, 1)}$"
    opts = [ans, d1, d2, d3]
    rng.shuffle(opts)

    pA = ("A", xA, yA)
    pB = ("B", xB, yB)
    pC = ("C", xC, yC)
    svg = _make_svg_plane([pA, pB, pC], lines=[("A", "B"), ("B", "C"), ("C", "A")])
    diag = {"kind": "inline_svg", "svg": svg, "alt_text": "Comprehensive coordinate geometry problem on triangle ABC"}

    coordA = _coord(xA, yA)
    coordB = _coord(xB, yB)
    coordC = _coord(xC, yC)
    prompt = (
        f"In the accompanying Cartesian diagram, triangle $ABC$ has vertices $A{coordA}$, $B{coordB}$, "
        f"and $C{coordC}$. Determine the equation of the straight line passing through vertex $A$ "
        f"that is parallel to side $BC$."
    )
    steps = [
        {"rule": "Calculate gradient of side BC", "op": f"m_{{BC}} = \frac{{{yC} - ({yB})}}{{{xC} - ({xB})}}", "to": f"m_{{BC}} = {m_BC}"},
        {"rule": "Use parallel lines condition", "op": f"m_{{parallel}} = m_{{BC}} = {m_BC}", "to": f"m = {m_BC}"},
        {"rule": "Determine equation through vertex A", "op": f"y - ({yA}) = {m_BC}(x - ({xA}))", "to": f"y = {m_BC}x + ({c_line})"},
        {"rule": "Write in standard form", "op": "y = mx + c", "to": ans.replace("$", "")},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="Lines that are parallel share identical gradients: m_1 = m_2.",
        t2=f"Calculate the gradient of BC (m_BC = {m_BC}), then substitute point A{coordA} into y - y_1 = m(x - x_1).",
        t3=f"c = {yA} - ({m_BC})({xA}) = {c_line}, giving {ans}.",
        misconceptions=["used_perpendicular_gradient", "substituted_B_or_C_instead_of_A", "sign_error_in_intercept"],
        marks=4,
        diagram_spec=diag,
    )


BUILDERS_26_50: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    "26_equation_of_line_gradient_and_y_intercept": _build_26,
    "27_equation_of_line_from_gradient_and_point": _build_27,
    "28_equation_of_line_through_two_points": _build_28,
    "29_equation_of_line_parallel_to_given_line": _build_29,
    "30_equation_of_line_perpendicular_to_given_line": _build_30,
    "31_equation_of_perpendicular_bisector": _build_31,
    "32_equation_of_median_in_triangle": _build_32,
    "33_equation_of_altitude_in_triangle": _build_33,
    "34_line_intercepts_with_axes": _build_34,
    "35_point_lies_on_line_test": _build_35,
    "36_point_of_intersection_of_two_lines": _build_36,
    "37_parallelogram_properties_opposite_sides_parallel": _build_37,
    "38_parallelogram_properties_opposite_sides_equal": _build_38,
    "39_parallelogram_diagonals_bisect_each_other": _build_39,
    "40_find_fourth_vertex_of_parallelogram": _build_40,
    "41_rectangle_proof_parallelogram_with_right_angle": _build_41,
    "42_rhombus_proof_parallelogram_with_perpendicular_diagonals": _build_42,
    "43_square_proof_all_sides_equal_and_perpendicular": _build_43,
    "44_trapezium_proof_one_pair_parallel_sides": _build_44,
    "45_kite_proof_adjacent_pairs_equal": _build_45,
    "46_area_of_triangle_right_angled": _build_46,
    "47_area_of_rectangle_or_square_on_cartesian_plane": _build_47,
    "48_distance_from_origin": _build_48,
    "49_circle_center_origin_equation_check": _build_49,
    "50_comprehensive_coordinate_geometry_multi_step_problem": _build_50,
}
