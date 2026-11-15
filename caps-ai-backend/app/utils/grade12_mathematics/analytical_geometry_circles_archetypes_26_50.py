"""Grade 12 Mathematics — Analytical Geometry (Circles) Archetypes 26–50.
100% Aligned with South African National Curriculum Standards (Grade 12 Term 2).
Grounded in curriculum_docs_auto/Mathematics_Gr12/Term 2/02. Analytical geometry.md.
"""
from __future__ import annotations

import math
import random
from typing import Any, Callable, Dict, List, Optional
import sympy as sp

from app.utils.grade12_mathematics._math_common import (
    make_math_question,
    num,
    solution_graph,
    step,
    to_latex,
)
from app.utils.grade12_mathematics.analytical_geometry_circles_archetypes_01_25 import (
    _fmt_general_circle,
    _fmt_shift,
    _q,
    _svg_spec,
)

x_sym = sp.Symbol("x")


def _line_latex(m_rat: sp.Rational, c_rat: sp.Rational) -> str:
    expr = m_rat * x_sym + c_rat
    return f"y = {to_latex(expr)}"


# 26. Gradient of radius and gradient of perpendicular tangent at point of contact
def build_26_radius_and_tangent_gradients_at_point(r: random.Random) -> Dict[str, Any]:
    a = r.randint(-5, 5)
    b = r.randint(-5, 5)
    dx = r.choice([-6, -5, -4, -3, -2, 2, 3, 4, 5, 6])
    dy = r.choice([-6, -5, -4, -3, -2, 2, 3, 4, 5, 6])
    px, py = a + dx, b + dy
    m_rad = sp.Rational(dy, dx)
    m_tan = sp.Rational(-dx, dy)
    ans = f"m_{{MP}} = {to_latex(m_rad)}; \\quad m_{{\\text{{tan}}}} = {to_latex(m_tan)}"
    prompt = (
        f"A circle has centre $M({a}; {b})$ and passes through the point of contact $P({px}; {py})$.\n\n"
        f"1. Calculate the gradient of the radius $MP$.\n"
        f"2. Hence write down the gradient of the tangent to the circle at $P$."
    )
    steps = [
        step(from_latex=f"m_{{MP}} = \\frac{{{py} - ({b})}}{{{px} - ({a})}}", to_latex_str=f"m_{{MP}} = \\frac{{{dy}}}{{{dx}}} = {to_latex(m_rad)}", op="Calculate gradient of radius MP", rule="Gradient formula"),
        step(from_latex="m_{MP} \\times m_{\\text{tan}} = -1", to_latex_str=f"m_{{\\text{{tan}}}} = {to_latex(m_tan)}", op="Use perpendicularity of radius and tangent", rule="Radius perpendicular to tangent"),
    ]
    return _q("26_radius_and_tangent_gradients_at_point", 26, prompt, ans, steps,
              "The tangent at P is perpendicular to the radius MP.",
              "First find m_MP = (y_P - y_M)/(x_P - x_M), then take the negative reciprocal -1 / m_MP.",
              f"m_MP = {to_latex(m_rad)} and m_tan = {to_latex(m_tan)}.",
              ["used_radius_gradient_without_negative_reciprocal"], "easy", 3)


# 27. Equation of tangent to an origin circle x^2 + y^2 = r^2 at P(x1; y1)
def build_27_tangent_equation_to_origin_circle(r: random.Random) -> Dict[str, Any]:
    px = r.choice([-6, -5, -4, -3, -2, 2, 3, 4, 5, 6])
    py = r.choice([-6, -5, -4, -3, -2, 2, 3, 4, 5, 6])
    r_sq = px * px + py * py
    m_rad = sp.Rational(py, px)
    m_tan = sp.Rational(-px, py)
    c_tan = sp.Rational(r_sq, py)
    ans = _line_latex(m_tan, c_tan)
    prompt = (
        f"Determine the equation of the tangent to the circle $x^2 + y^2 = {r_sq}$ "
        f"at the point $P({px}; {py})$ in the form $y = mx + c$."
    )
    steps = [
        step(from_latex=f"m_{{OP}} = \\frac{{{py}}}{{{px}}} = {to_latex(m_rad)}", to_latex_str=f"m_{{\\text{{tan}}}} = {to_latex(m_tan)}", op="Find gradient of radius OP and perpendicular tangent", rule="m_OP * m_tan = -1"),
        step(from_latex=f"y - ({py}) = {to_latex(m_tan)}(x - ({px}))", to_latex_str=ans, op="Substitute P and m_tan into point-gradient formula", rule="y - y1 = m(x - x1)"),
    ]
    return _q("27_tangent_equation_to_origin_circle", 27, prompt, ans, steps,
              f"Find the gradient of radius OP from (0; 0) to P({px}; {py}), then invert and change sign.",
              "Substitute P and m_tan into y - y_P = m_tan(x - x_P).",
              f"m_tan = {to_latex(m_tan)}, giving {ans}.",
              ["used_same_gradient_as_radius", "sign_error_in_point_gradient_substitution"], "medium", 4)


# 28. Equation of tangent to a shifted circle (x - a)^2 + (y - b)^2 = r^2 at P(x1; y1)
def build_28_tangent_equation_to_shifted_circle(r: random.Random) -> Dict[str, Any]:
    a = r.choice([-5, -4, -3, -2, 2, 3, 4, 5])
    b = r.choice([-5, -4, -3, -2, 2, 3, 4, 5])
    dx = r.choice([-4, -3, -2, -1, 1, 2, 3, 4])
    dy = r.choice([-4, -3, -2, 2, 3, 4])
    px, py = a + dx, b + dy
    r_sq = dx * dx + dy * dy
    m_rad = sp.Rational(dy, dx)
    m_tan = sp.Rational(-dx, dy)
    c_tan = py - m_tan * px
    eq_circle = f"{_fmt_shift('x', a)} + {_fmt_shift('y', b)} = {r_sq}"
    ans = _line_latex(m_tan, c_tan)
    prompt = (
        f"Determine the equation of the tangent to the circle ${eq_circle}$ "
        f"at the point $P({px}; {py})$ on its circumference."
    )
    steps = [
        step(from_latex=f"M({a}; {b}),\\; P({px}; {py})", to_latex_str=f"m_{{MP}} = \\frac{{{py} - ({b})}}{{{px} - ({a})}} = {to_latex(m_rad)} \\implies m_{{\\text{{tan}}}} = {to_latex(m_tan)}", op="Compute radius gradient and perpendicular tangent gradient", rule="m_rad * m_tan = -1"),
        step(from_latex=f"y - ({py}) = {to_latex(m_tan)}(x - ({px}))", to_latex_str=ans, op="Substitute P(x1; y1) into point-gradient form", rule="Equation of tangent"),
    ]
    return _q("28_tangent_equation_to_shifted_circle", 28, prompt, ans, steps,
              f"First identify the centre M({a}; {b}) from the standard circle equation.",
              f"Find m_MP = ({py} - ({b}))/({px} - ({a})), then m_tan = -1/m_MP, and use P({px}; {py}).",
              f"The tangent equation is {ans}.",
              ["sign_inversion_of_center", "substituted_centre_instead_of_point_of_contact_into_tangent"], "medium", 4)


# 29. Equation of tangent when circle is given in expanded general form
def build_29_tangent_equation_from_general_circle_form(r: random.Random) -> Dict[str, Any]:
    a = r.choice([-5, -4, -3, -2, 2, 3, 4, 5])
    b = r.choice([-5, -4, -3, -2, 2, 3, 4, 5])
    dx = r.choice([-5, -3, -2, 2, 3, 5])
    dy = r.choice([-4, -3, -2, 2, 3, 4])
    px, py = a + dx, b + dy
    r_sq = dx * dx + dy * dy
    gen_eq = _fmt_general_circle(a, b, r_sq)
    m_rad = sp.Rational(dy, dx)
    m_tan = sp.Rational(-dx, dy)
    c_tan = py - m_tan * px
    ans = f"M({a}; {b}); \\quad {_line_latex(m_tan, c_tan)}"
    prompt = (
        f"A circle is defined by the equation ${gen_eq}$.\n\n"
        f"1. Complete the square to determine the coordinates of the centre $M$.\n"
        f"2. Hence find the equation of the tangent to the circle at the point $P({px}; {py})$."
    )
    steps = [
        step(from_latex=gen_eq, to_latex_str=f"{_fmt_shift('x', a)} + {_fmt_shift('y', b)} = {r_sq} \\implies M({a}; {b})", op="Complete the square to find centre M", rule="Completing the square"),
        step(from_latex=f"m_{{MP}} = \\frac{{{dy}}}{{{dx}}} = {to_latex(m_rad)}", to_latex_str=f"m_{{\\text{{tan}}}} = {to_latex(m_tan)}", op="Find perpendicular tangent gradient", rule="m_MP * m_tan = -1"),
        step(from_latex=f"y - ({py}) = {to_latex(m_tan)}(x - ({px}))", to_latex_str=_line_latex(m_tan, c_tan), op="Write equation of tangent at P", rule="Point-gradient formula"),
    ]
    return _q("29_tangent_equation_from_general_circle_form", 29, prompt, ans, steps,
              "Complete the square in x and y first to find the centre M(a; b).",
              "Then calculate the gradient of radius MP and use m_tan = -1 / m_MP through P.",
              f"Centre M({a}; {b}) and tangent {_line_latex(m_tan, c_tan)}.",
              ["forgot_add_both_sides", "used_same_gradient_as_radius"], "hard", 5)


# 30. Horizontal and vertical tangents to a circle (x - a)^2 + (y - b)^2 = r^2
def build_30_horizontal_and_vertical_tangents(r: random.Random) -> Dict[str, Any]:
    a = r.randint(-7, 7)
    b = r.randint(-7, 7)
    rad = r.randint(3, 12)
    r_sq = rad * rad
    kind = r.choice(["horizontal", "vertical"])
    eq = f"{_fmt_shift('x', a)} + {_fmt_shift('y', b)} = {r_sq}"
    if kind == "horizontal":
        y1, y2 = b - rad, b + rad
        ans = f"y = {y1} \\text{{ and }} y = {y2}"
        sub_q = "horizontal tangents (parallel to the line $y = 0$)"
        step_str = f"y = b \\pm r = {b} \\pm {rad}"
    else:
        x1, x2 = a - rad, a + rad
        ans = f"x = {x1} \\text{{ and }} x = {x2}"
        sub_q = "vertical tangents (parallel to the line $x = 0$)"
        step_str = f"x = a \\pm r = {a} \\pm {rad}"
    prompt = (
        f"Consider the circle with equation ${eq}$.\n\n"
        f"Write down the equations of the two {sub_q} to this circle."
    )
    steps = [
        step(from_latex=eq, to_latex_str=f"M({a}; {b}),\\; r = {rad}", op="Read off centre M(a; b) and radius r", rule="Standard circle parameters"),
        step(from_latex=step_str, to_latex_str=ans, op=f"Add and subtract r from the {'y' if kind=='horizontal' else 'x'}-coordinate of the centre", rule=f"Equations of {kind} tangents"),
    ]
    return _q("30_horizontal_and_vertical_tangents", 30, prompt, ans, steps,
              f"Find the centre M({a}; {b}) and radius r = {rad} first.",
              "Horizontal tangents have equations y = b +- r; vertical tangents have equations x = a +- r.",
              f"The two {kind} tangents are {ans}.",
              ["confused_x_and_y_equations_for_horizontal_vertical_lines"], "easy", 3)


# 31. Length of tangent segment PT from an external point T(x0; y0) using Pythagoras
def build_31_tangent_length_from_external_point_pythagoras(r: random.Random) -> Dict[str, Any]:
    a = r.randint(-4, 4)
    b = r.randint(-4, 4)
    # Choose right triangle (r, PT, MT) from Pythagorean triple or clean surd
    rad, pt_len, mt_len = r.choice([(3, 4, 5), (6, 8, 10), (5, 12, 13), (8, 15, 17), (9, 12, 15)])
    # Place T so MT^2 = mt_len^2: e.g. T = (a + mt_len, b) or (a, b + mt_len) or Pythagorean split
    if mt_len == 5:
        tx, ty = a + 3, b + 4
    elif mt_len == 10:
        tx, ty = a + 6, b - 8
    elif mt_len == 13:
        tx, ty = a - 5, b + 12
    elif mt_len == 15:
        tx, ty = a + 9, b + 12
    else:
        tx, ty = a + 8, b - 15
    r_sq = rad * rad
    mt_sq = mt_len * mt_len
    eq = f"{_fmt_shift('x', a)} + {_fmt_shift('y', b)} = {r_sq}"
    ans = f"PT = {pt_len}\\text{{ units}}"
    prompt = (
        f"From an external point $T({tx}; {ty})$, a tangent $TP$ is drawn to touch the circle "
        f"${eq}$ at $P$.\n\n"
        f"Calculate the length of the tangent segment $PT$."
    )
    steps = [
        step(from_latex=f"M({a}; {b}),\\; T({tx}; {ty})", to_latex_str=f"MT^2 = ({tx} - ({a}))^2 + ({ty} - ({b}))^2 = {mt_sq}", op="Compute squared distance MT^2 from centre M to external point T", rule="Distance formula"),
        step(from_latex=f"PT^2 = MT^2 - r^2 = {mt_sq} - {r_sq} = {pt_len*pt_len}", to_latex_str=ans, op="Apply Theorem of Pythagoras in right-angled triangle MPT (angle MPT = 90 deg)", rule="PT^2 = MT^2 - r^2"),
    ]
    return _q("31_tangent_length_from_external_point_pythagoras", 31, prompt, ans, steps,
              "Since the radius MP is perpendicular to the tangent PT at P, triangle MPT is right-angled at P.",
              "By Pythagoras, MT^2 = MP^2 + PT^2, so PT^2 = MT^2 - r^2.",
              f"MT^2 = {mt_sq} and r^2 = {r_sq}, so PT = sqrt({mt_sq - r_sq}) = {pt_len} units.",
              ["added_r_squared_instead_of_subtracting_in_pythagoras"], "medium", 4)


# 32. Equal tangents from an external point & kite area/perimeter (deltoid MP1TP2)
def build_32_two_tangents_from_external_point_kite_properties(r: random.Random) -> Dict[str, Any]:
    a = r.randint(-4, 4)
    b = r.randint(-4, 4)
    rad, pt_len, mt_len = r.choice([(3, 4, 5), (5, 12, 13), (6, 8, 10), (8, 15, 17)])
    tx, ty = a + mt_len, b
    r_sq = rad * rad
    area_kite = rad * pt_len
    perim_kite = 2 * (rad + pt_len)
    eq = f"{_fmt_shift('x', a)} + {_fmt_shift('y', b)} = {r_sq}"
    ans = f"PT_1 = PT_2 = {pt_len}; \\quad \\text{{Perimeter}} = {perim_kite}; \\quad \\text{{Area}} = {area_kite}\\text{{ sq. units}}"
    prompt = (
        f"Tangents $TP_1$ and $TP_2$ are drawn from the external point $T({tx}; {ty})$ to the circle "
        f"${eq}$ with centre $M({a}; {b})$.\n\n"
        f"Calculate the length of $TP_1$, the perimeter of kite $MP_1TP_2$, and the area of kite $MP_1TP_2$."
    )
    steps = [
        step(from_latex=f"MT^2 = {mt_len*mt_len},\\; r^2 = {r_sq}", to_latex_str=f"TP_1 = TP_2 = \\sqrt{{{mt_len*mt_len} - {r_sq}}} = {pt_len}", op="Find tangent length by Pythagoras and equal-tangents theorem", rule="Tangents from same external point are equal"),
        step(from_latex=f"\\text{{Perimeter}} = 2(r + TP_1),\\; \\text{{Area}} = 2 \\times \\frac{{1}}{{2}} r \\cdot TP_1", to_latex_str=ans, op="Compute perimeter and area of kite MP1TP2", rule="Two congruent right triangles"),
    ]
    return _q("32_two_tangents_from_external_point_kite_properties", 32, prompt, ans, steps,
              "Kite MP1TP2 consists of two congruent right-angled triangles MP1T and MP2T.",
              "Each right triangle has perpendicular legs r and TP1, so total kite area = 2 * (1/2 * r * TP1) = r * TP1.",
              f"TP1 = {pt_len}, Perimeter = {perim_kite}, Area = {area_kite}.",
              ["forgot_to_double_triangle_area_for_kite"], "medium", 4)


# 33. Finding thetwo parallel tangents to a circle with a given gradient m
def build_33_two_parallel_tangents_with_given_gradient(r: random.Random) -> Dict[str, Any]:
    a = r.randint(-4, 4)
    b = r.randint(-4, 4)
    # Radius vector (dx, dy) gives normal to tangent; tangent gradient m_tan = -dx / dy
    dx, dy = r.choice([(3, 4), (4, 3), (-3, 4), (4, -3)])
    r_sq = dx * dx + dy * dy
    p1x, p1y = a + dx, b + dy
    p2x, p2y = a - dx, b - dy
    m_tan = sp.Rational(-dx, dy)
    c1 = p1y - m_tan * p1x
    c2 = p2y - m_tan * p2x
    eq_circle = f"{_fmt_shift('x', a)} + {_fmt_shift('y', b)} = {r_sq}"
    ans = f"P_1({p1x}; {p1y}),\\; P_2({p2x}; {p2y}); \\quad {_line_latex(m_tan, c1)} \\text{{ and }} {_line_latex(m_tan, c2)}"
    prompt = (
        f"A circle has equation ${eq_circle}$ with centre $M({a}; {b})$. "
        f"A diameter $P_1P_2$ has gradient $m_{{\\text{{rad}}}} = {to_latex(sp.Rational(dy, dx))}$, "
        f"meeting the circle at $P_1({p1x}; {p1y})$ and $P_2({p2x}; {p2y})$.\n\n"
        f"Determine the equations of the two parallel tangents to the circle at $P_1$ and $P_2$."
    )
    steps = [
        step(from_latex=f"m_{{\\text{{rad}}}} = {to_latex(sp.Rational(dy, dx))}", to_latex_str=f"m_{{\\text{{tan}}}} = {to_latex(m_tan)}", op="Both tangents are perpendicular to diameter P1P2", rule="Parallel tangents share gradient m_tan"),
        step(from_latex=f"P_1({p1x}; {p1y}),\\; P_2({p2x}; {p2y})", to_latex_str=f"{_line_latex(m_tan, c1)} \\text{{ and }} {_line_latex(m_tan, c2)}", op="Substitute P1 and P2 into y - y1 = m_tan(x - x1)", rule="Two parallel tangent lines"),
    ]
    return _q("33_two_parallel_tangents_with_given_gradient", 33, prompt, ans, steps,
              "Tangents at opposite ends of a diameter are parallel and both have gradient m_tan = -1 / m_rad.",
              f"Substitute m_tan = {to_latex(m_tan)} with P1 and with P2 separately.",
              f"The parallel tangents are {_line_latex(m_tan, c1)} and {_line_latex(m_tan, c2)}.",
              ["found_only_one_of_two_parallel_tangents"], "medium", 4)


# 34. Angle of inclination of radius and tangent at point of contact
def build_34_angle_of_inclination_of_radius_and_tangent(r: random.Random) -> Dict[str, Any]:
    a = r.randint(-4, 4)
    b = r.randint(-4, 4)
    # Pick dx > 0, dy > 0 so radius has acute inclination alpha, and tangent has obtuse inclination 90 + alpha
    dx, dy = r.choice([(1, 1), (3, 4), (4, 3), (5, 12), (2, 3), (3, 2), (1, 2), (2, 1)])
    px, py = a + dx, b + dy
    r_sq = dx * dx + dy * dy
    alpha = round(math.degrees(math.atan2(dy, dx)), 2)
    theta_tan = round(alpha + 90.0, 2)
    ans = f"\\alpha = {num(alpha, 2)}^\\circ; \\quad \\theta_{{\\text{{tan}}}} = {num(theta_tan, 2)}^\\circ"
    prompt = (
        f"A circle with centre $M({a}; {b})$ passes through $P({px}; {py})$.\n\n"
        f"1. Calculate the angle of inclination $\\alpha$ of the radius $MP$ (correct to 2 decimal places).\n"
        f"2. Hence determine the angle of inclination $\\theta_{{\\text{{tan}}}}$ of the tangent at $P$."
    )
    steps = [
        step(from_latex=f"\\tan \\alpha = m_{{MP}} = \\frac{{{dy}}}{{{dx}}}", to_latex_str=f"\\alpha = {num(alpha, 2)}^\\circ", op="Calculate acute inclination angle of radius MP", rule="tan(alpha) = m_MP"),
        step(from_latex=f"m_{{\\text{{tan}}}} = -\\frac{{{dx}}}{{{dy}}} < 0", to_latex_str=f"\\theta_{{\\text{{tan}}}} = 180^\\circ - \\arctan\\left(\\frac{{{dx}}}{{{dy}}}\\right) = 90^\\circ + \\alpha = {num(theta_tan, 2)}^\\circ", op="Compute obtuse inclination of perpendicular tangent", rule="Exterior angle / negative gradient inclination"),
    ]
    return _q("34_angle_of_inclination_of_radius_and_tangent", 34, prompt, ans, steps,
              f"First find tan(alpha) = {dy}/{dx}. Since m_tan = -{dx}/{dy} < 0, the tangent inclination is obtuse.",
              "Because the tangent is perpendicular to the radius with acute inclination alpha, theta_tan = alpha + 90 deg.",
              f"alpha = {num(alpha, 2)} deg and theta_tan = {num(theta_tan, 2)} deg.",
              ["reported_negative_acute_angle_for_obtuse_inclination"], "medium", 4)


# 35. Tangent to circle SVG coordinate diagram: find tangent equation and axis intercept
def build_35_circle_and_tangent_svg_diagram(r: random.Random) -> Dict[str, Any]:
    a = r.choice([-3, -2, -1, 1, 2, 3])
    b = r.choice([-3, -2, -1, 1, 2, 3])
    dx, dy = r.choice([(3, 4), (4, 3)])
    px, py = a + dx, b + dy
    r_sq = dx * dx + dy * dy
    m_tan = sp.Rational(-dx, dy)
    c_tan = py - m_tan * px
    rad_svg = 50 + ((a + b) % 11)
    svg = (
        f'<svg viewBox="0 0 360 240" xmlns="http://www.w3.org/2000/svg">'
        f'<rect x="0" y="0" width="360" height="240" fill="#f8fafc" rx="8"/>'
        f'<line x1="20" y1="135" x2="340" y2="135" stroke="#94a3b8" stroke-width="1.5"/>'
        f'<line x1="150" y1="15" x2="150" y2="225" stroke="#94a3b8" stroke-width="1.5"/>'
        f'<circle cx="170" cy="120" r="{rad_svg}" fill="none" stroke="#1d4ed8" stroke-width="2.5"/>'
        f'<circle cx="170" cy="120" r="3.5" fill="#0f172a"/>'
        f'<text x="142" y="132" font-size="11" font-family="sans-serif" fill="#0f172a">M({a}; {b})</text>'
        f'<line x1="170" y1="120" x2="{170 + int(rad_svg*0.6)}" y2="{120 - int(rad_svg*0.8)}" stroke="#64748b" stroke-width="1.8" stroke-dasharray="4,3"/>'
        f'<circle cx="{170 + int(rad_svg*0.6)}" cy="{120 - int(rad_svg*0.8)}" r="4" fill="#dc2626"/>'
        f'<text x="{176 + int(rad_svg*0.6)}" y="{115 - int(rad_svg*0.8)}" font-size="11" font-family="sans-serif" fill="#0f172a">P({px}; {py})</text>'
        f'<line x1="{170 + int(rad_svg*0.6) - 64}" y1="{120 - int(rad_svg*0.8) - 48}" x2="{170 + int(rad_svg*0.6) + 64}" y2="{120 - int(rad_svg*0.8) + 48}" stroke="#dc2626" stroke-width="2.2"/>'
        f'</svg>'
    )
    ans = f"{_line_latex(m_tan, c_tan)}; \\quad T\\left(0; {to_latex(c_tan)}\\right)"
    prompt = (
        f"Refer to the coordinate diagram of a circle with centre $M({a}; {b})$ and tangent at $P({px}; {py})$.\n\n"
        f"Determine the equation of the tangent at $P$ and the coordinates of its vertical-axis intercept $T(0; y_T)$."
    )
    steps = [
        step(from_latex=f"m_{{MP}} = \\frac{{{dy}}}{{{dx}}}", to_latex_str=f"m_{{\\text{{tan}}}} = {to_latex(m_tan)}", op="Calculate gradient of radius MP and perpendicular tangent", rule="m_MP * m_tan = -1"),
        step(from_latex=f"y - ({py}) = {to_latex(m_tan)}(x - ({px}))", to_latex_str=ans, op="Write tangent equation and set x = 0 for vertical intercept", rule="Tangent equation and y-intercept"),
    ]
    return _q("35_circle_and_tangent_svg_diagram", 35, prompt, ans, steps,
              f"Compute m_MP = {dy}/{dx}, then use m_tan = -{dx}/{dy} through P({px}; {py}).",
              "Set x = 0 in the tangent equation to get the vertical-axis intercept.",
              f"{ans}.",
              ["used_same_gradient_as_radius"], "medium", 4, _svg_spec(svg))


# 36. Intersection of a straight line y = x + k and a circle (two points of intersection)
def build_36_secant_line_circle_intersection_points(r: random.Random) -> Dict[str, Any]:
    # Circle (x - a)^2 + (y - b)^2 = r^2 with points A(a + d1, b + d2) and B(a + d2, b + d1)
    # Line through A and B has gradient -1: x + y = a + b + d1 + d2 => y = -x + (a + b + d1 + d2)
    a = r.randint(-3, 3)
    b = r.randint(-3, 3)
    d1, d2 = r.choice([(3, 4), (-3, 4), (2, 5), (-2, 5), (1, 4), (2, 3)])
    r_sq = d1 * d1 + d2 * d2
    ax, ay = a + d1, b + d2
    bx, by = a + d2, b + d1
    c_line = a + b + d1 + d2
    line_eq = f"y = -x {'+' if c_line >= 0 else '-'} {abs(c_line)}"
    circle_eq = f"{_fmt_shift('x', a)} + {_fmt_shift('y', b)} = {r_sq}"
    ans = f"A({ax}; {ay}) \\text{{ and }} B({bx}; {by})"
    prompt = (
        f"Calculate the coordinates of the points of intersection $A$ and $B$ of the straight line "
        f"${line_eq}$ and the circle ${circle_eq}$."
    )
    steps = [
        step(from_latex=f"{line_eq},\\; {circle_eq}", to_latex_str=f"(x - ({a}))^2 + (-x + ({c_line - b}))^2 = {r_sq}", op="Substitute linear expression for y into circle equation", rule="Simultaneous substitution"),
        step(from_latex=f"(x - ({ax}))(x - ({bx})) = 0", to_latex_str=f"x = {ax} \\text{{ or }} x = {bx} \\implies {ans}", op="Expand, simplify quadratic in x, factorise, and find y-values", rule="Quadratic roots"),
    ]
    return _q("36_secant_line_circle_intersection_points", 36, prompt, ans, steps,
              f"Substitute {line_eq} into the circle equation so that only x remains.",
              "Expand and divide the resulting quadratic equation by 2, then factorise.",
              f"The points of intersection are {ans}.",
              ["algebraic_expansion_error_in_simultaneous_circle_line"], "hard", 5)


# 37. Midpoint of a chord AB and verifying perpendicular bisector passes through centre
def build_37_chord_midpoint_and_perpendicular_from_centre(r: random.Random) -> Dict[str, Any]:
    mx = r.randint(-4, 4)
    my = r.randint(-4, 4)
    # Chord midpoint N(nx, ny); vector MN = (ux, uy), vector NA = (-uy, ux) so MN perp AB!
    ux = r.choice([1, 2, 3, -1, -2, -3])
    uy = r.choice([1, 2, 3, -1, -2, -3])
    nx, ny = mx + ux, my + uy
    k = r.choice([1, 2])
    ax, ay = nx - k * uy, ny + k * ux
    bx, by = nx + k * uy, ny - k * ux
    m_ab = sp.Rational(ay - by, ax - bx)
    m_mn = sp.Rational(ny - my, nx - mx)
    ans = f"N({nx}; {ny}); \\quad m_{{AB}} \\times m_{{MN}} = ({to_latex(m_ab)})({to_latex(m_mn)}) = -1"
    prompt = (
        f"A circle with centre $M({mx}; {my})$ has a chord with endpoints $A({ax}; {ay})$ and $B({bx}; {by})$.\n\n"
        f"1. Determine the coordinates of $N$, the midpoint of chord $AB$.\n"
        f"2. Show by gradient calculation that $MN \\perp AB$."
    )
    steps = [
        step(from_latex=f"A({ax}; {ay}),\\; B({bx}; {by})", to_latex_str=f"N\\left(\\frac{{{ax}+({bx})}}{{2}}; \\frac{{{ay}+({by})}}{{2}}\\right) = N({nx}; {ny})", op="Calculate midpoint N of chord AB", rule="Midpoint formula"),
        step(from_latex=f"m_{{AB}} = {to_latex(m_ab)},\\; m_{{MN}} = {to_latex(m_mn)}", to_latex_str=f"m_{{AB}} \\times m_{{MN}} = -1 \\implies MN \\perp AB", op="Verify product of gradients equals -1", rule="Line from centre to midpoint of chord is perpendicular to chord"),
    ]
    return _q("37_chord_midpoint_and_perpendicular_from_centre", 37, prompt, ans, steps,
              "Use the midpoint formula to find N, then compute gradients m_AB and m_MN.",
              "Show that m_AB * m_MN = -1.",
              f"N({nx}; {ny}) and m_AB * m_MN = -1.",
              ["used_distance_formula_instead_of_gradients_for_perpendicularity"], "medium", 4)


# 38. Length of a chord cut off on a coordinate axis by a circle
def build_38_length_of_chord_on_coordinate_axis(r: random.Random) -> Dict[str, Any]:
    a = r.randint(-6, 6)
    b = r.choice([-5, -4, -3, -2, 2, 3, 4, 5])
    half_chord = r.choice([3, 4, 5, 6, 7, 8])
    r_sq = b * b + half_chord * half_chord
    x1, x2 = a - half_chord, a + half_chord
    chord_len = 2 * half_chord
    eq = f"{_fmt_shift('x', a)} + {_fmt_shift('y', b)} = {r_sq}"
    ans = f"AB = {chord_len}\\text{{ units}} \\quad (A({x1}; 0),\\; B({x2}; 0))"
    prompt = (
        f"The circle ${eq}$ intersects the line $y = 0$ at points $A$ and $B$.\n\n"
        f"Determine the coordinates of $A$ and $B$ and hence state the length of chord $AB$."
    )
    steps = [
        step(from_latex=f"y = 0 \\implies {_fmt_shift('x', a)} + ({-b})^2 = {r_sq}", to_latex_str=f"(x - ({a}))^2 = {half_chord*half_chord} \\implies x = {x1} \\text{{ or }} x = {x2}", op="Set y = 0 and solve for x", rule="Intercepts on y = 0"),
        step(from_latex=f"A({x1}; 0),\\; B({x2}; 0)", to_latex_str=f"AB = {x2} - ({x1}) = {chord_len}\\text{{ units}}", op="Subtract x-coordinates to find chord length", rule="Horizontal segment length"),
    ]
    return _q("38_length_of_chord_on_coordinate_axis", 38, prompt, ans, steps,
              "Substitute y = 0 into the circle equation to find the two x-coordinates.",
              "The length of the horizontal chord AB is x_B - x_A.",
              f"A({x1}; 0), B({x2}; 0), and AB = {chord_len} units.",
              ["gave_half_chord_length_instead_of_full_chord"], "medium", 3)


# 39. Classifying a line as secant, tangent, or non-intersecting to a circle
def build_39_classify_line_circle_intersection_via_discriminant(r: random.Random) -> Dict[str, Any]:
    # Circle x^2 + y^2 = r^2 and line y = x + c
    # x^2 + (x + c)^2 = r^2 => 2x^2 + 2cx + (c^2 - r^2) = 0
    # Discriminant Delta = (2c)^2 - 4(2)(c^2 - r^2) = 8r^2 - 4c^2 = 4(2r^2 - c^2)
    rad = r.randint(3, 9)
    r_sq = rad * rad
    c_val = r.randint(2, 14)
    delta = 4 * (2 * r_sq - c_val * c_val)
    if delta > 0:
        nature = "secant (intersects in 2 distinct points)"
        rel = ">"
    elif delta == 0:
        nature = "tangent (touches in 1 point)"
        rel = "="
    else:
        nature = "non-intersecting (0 real points)"
        rel = "<"
    ans = f"\\Delta = {delta} {rel} 0 \\implies \\text{{{nature}}}"
    prompt = (
        f"Substitute the line $y = x + {c_val}$ into the circle $x^2 + y^2 = {r_sq}$ to obtain a quadratic equation in $x$.\n\n"
        f"Calculate its discriminant $\\Delta$ (for $2x^2 + 2({c_val})x + ({c_val*c_val - r_sq}) = 0$) and classify the line as a secant, a tangent, or non-intersecting."
    )
    steps = [
        step(from_latex=f"x^2 + (x + {c_val})^2 = {r_sq}", to_latex_str=f"2x^2 + {2*c_val}x + ({c_val*c_val - r_sq}) = 0", op="Substitute y = x + c and write in standard quadratic form", rule="ax^2 + bx + c = 0"),
        step(from_latex=f"\\Delta = ({2*c_val})^2 - 4(2)({c_val*c_val - r_sq})", to_latex_str=ans, op="Compute discriminant Delta = b^2 - 4ac and interpret sign", rule="Discriminant intersection test"),
    ]
    return _q("39_classify_line_circle_intersection_via_discriminant", 39, prompt, ans, steps,
              "After expanding x^2 + (x + c)^2 = r^2 into 2x^2 + 2cx + (c^2 - r^2) = 0, compute Delta = b^2 - 4ac.",
              "Delta > 0 means secant (2 points), Delta = 0 means tangent (1 point), Delta < 0 means 0 points.",
              f"Delta = {delta} {rel} 0, so the line is {nature}.",
              ["sign_error_in_b_squared_minus_4ac"], "medium", 4)


# 40. Finding values of k for which line y = mx + k is tangent to x^2 + y^2 = r^2
def build_40_tangent_parameter_k_via_equal_roots(r: random.Random) -> Dict[str, Any]:
    m = r.choice([1, 2, 3, -1, -2, -3])
    n_scale = r.choice([1, 2, 3, 4])
    # Choose r^2 = n_scale^2 * (1 + m^2) so k^2 = r^2(1 + m^2) = n_scale^2 * (1 + m^2)^2 => k = +- n_scale*(1 + m^2)
    one_plus_m2 = 1 + m * m
    r_sq = n_scale * n_scale * one_plus_m2
    k_pos = n_scale * one_plus_m2
    m_str = "x" if m == 1 else ("-x" if m == -1 else f"{m}x")
    ans = f"k = \\pm {k_pos}"
    prompt = (
        f"The straight line $y = {m_str} + k$ is a tangent to the circle $x^2 + y^2 = {r_sq}$.\n\n"
        f"Determine the two possible values of $k$."
    )
    steps = [
        step(from_latex=f"x^2 + ({m_str} + k)^2 = {r_sq}", to_latex_str=f"{one_plus_m2}x^2 + {2*m}kx + (k^2 - {r_sq}) = 0", op="Substitute y = mx + k into circle equation", rule="Simultaneous substitution"),
        step(from_latex=f"\\Delta = ({2*m}k)^2 - 4({one_plus_m2})(k^2 - {r_sq}) = 0", to_latex_str=f"k^2 = {r_sq}({one_plus_m2}) = {k_pos*k_pos} \\implies {ans}", op="Set discriminant Delta = 0 for tangency", rule="Equal roots condition Delta = 0"),
    ]
    return _q("40_tangent_parameter_k_via_equal_roots", 40, prompt, ans, steps,
              "A line is tangent to a circle when the quadratic equation formed by substitution has equal roots (Delta = 0).",
              f"Setting Delta = 0 yields k^2 = r^2(1 + m^2) = {r_sq} * {one_plus_m2}.",
              f"k^2 = {k_pos*k_pos}, so k = +- {k_pos}.",
              ["omitted_negative_value_of_k_for_second_tangent"], "hard", 4)


# 41. Distance between centres of two circles C1 and C2
def build_41_distance_between_two_circle_centres(r: random.Random) -> Dict[str, Any]:
    x1, y1 = r.randint(-5, 3), r.randint(-5, 3)
    dx, dy, dist = r.choice([(3, 4, 5), (6, 8, 10), (5, 12, 13), (8, 15, 17), (9, 12, 15)])
    x2, y2 = x1 + dx, y1 + dy
    r1_sq = r.randint(4, 25)
    r2_sq = r.randint(4, 25)
    eq1 = f"{_fmt_shift('x', x1)} + {_fmt_shift('y', y1)} = {r1_sq}"
    eq2 = _fmt_general_circle(x2, y2, r2_sq)
    ans = f"C_1({x1}; {y1}),\\; C_2({x2}; {y2}); \\quad C_1C_2 = {dist}\\text{{ units}}"
    prompt = (
        f"Two circles are given by $C_1: {eq1}$ and $C_2: {eq2}$.\n\n"
        f"Determine the coordinates of both centres $C_1$ and $C_2$, and calculate the distance $C_1C_2$ between the centres."
    )
    steps = [
        step(from_latex=f"C_1({x1}; {y1}),\\; C_2: {eq2}", to_latex_str=f"C_2({x2}; {y2})", op="Find centres of both circles", rule="Completing the square"),
        step(from_latex=f"C_1C_2 = \\sqrt{{({x2} - ({x1}))^2 + ({y2} - ({y1}))^2}}", to_latex_str=f"C_1C_2 = \\sqrt{{{dx*dx} + {dy*dy}}} = {dist}\\text{{ units}}", op="Calculate distance between C1 and C2", rule="Distance formula"),
    ]
    return _q("41_distance_between_two_circle_centres", 41, prompt, ans, steps,
              "Read C1 from the first equation and complete the square on the second equation to find C2.",
              "Apply the distance formula d = sqrt((x2 - x1)^2 + (y2 - y1)^2).",
              f"C1({x1}; {y1}), C2({x2}; {y2}), and C1C2 = {dist} units.",
              ["sign_inversion_of_center"], "medium", 4)


# 42. Proving two circles touch externally (d = r1 + r2)
def build_42_two_circles_touching_externally(r: random.Random) -> Dict[str, Any]:
    x1, y1 = r.randint(-4, 2), r.randint(-4, 2)
    dx, dy, dist = r.choice([(3, 4, 5), (6, 8, 10), (5, 12, 13), (9, 12, 15)])
    x2, y2 = x1 + dx, y1 + dy
    r1 = r.randint(1, dist - 1)
    r2 = dist - r1
    eq1 = f"{_fmt_shift('x', x1)} + {_fmt_shift('y', y1)} = {r1*r1}"
    eq2 = f"{_fmt_shift('x', x2)} + {_fmt_shift('y', y2)} = {r2*r2}"
    ans = f"C_1C_2 = {dist} = r_1 + r_2 = {r1} + {r2} \\implies \\text{{touch externally}}"
    prompt = (
        f"Consider the two circles:\n"
        f"$$C_1: {eq1} \\quad \\text{{and}} \\quad C_2: {eq2}$$\n"
        f"Calculate the distance $C_1C_2$ between their centres and compare it with $r_1 + r_2$ to prove that the circles touch externally."
    )
    steps = [
        step(from_latex=f"C_1({x1}; {y1}),\\; r_1 = {r1};\\quad C_2({x2}; {y2}),\\; r_2 = {r2}", to_latex_str=f"C_1C_2 = \\sqrt{{{dx}^2 + {dy}^2}} = {dist}", op="Extract centres, radii, and distance between centres", rule="Distance formula"),
        step(from_latex=f"r_1 + r_2 = {r1} + {r2} = {dist}", to_latex_str=ans, op="Verify C1C2 = r1 + r2", rule="External tangency condition d = r1 + r2"),
    ]
    return _q("42_two_circles_touching_externally", 42, prompt, ans, steps,
              "Two circles touch externally if and only if the distance between their centres equals the sum of their radii.",
              f"Show that C1C2 = {dist} and r1 + r2 = {r1} + {r2} = {dist}.",
              f"Since C1C2 = r1 + r2 = {dist}, the circles touch externally.",
              ["compared_d_with_r1_squared_plus_r2_squared"], "medium", 4)


# 43. Proving two circles touch internally (d = |r1 - r2|)
def build_43_two_circles_touching_internally(r: random.Random) -> Dict[str, Any]:
    x1, y1 = r.randint(-4, 2), r.randint(-4, 2)
    dx, dy, dist = r.choice([(3, 4, 5), (6, 8, 10), (5, 12, 13)])
    x2, y2 = x1 + dx, y1 + dy
    r2 = r.randint(2, 6)
    r1 = dist + r2
    eq1 = f"{_fmt_shift('x', x1)} + {_fmt_shift('y', y1)} = {r1*r1}"
    eq2 = f"{_fmt_shift('x', x2)} + {_fmt_shift('y', y2)} = {r2*r2}"
    ans = f"C_1C_2 = {dist} = r_1 - r_2 = {r1} - {r2} \\implies \\text{{touch internally}}"
    prompt = (
        f"Given two circles:\n"
        f"$$C_1: {eq1} \\quad \\text{{and}} \\quad C_2: {eq2}$$\n"
        f"Show by calculation that $C_1C_2 = |r_1 - r_2|$ and state the geometric relationship between the two circles."
    )
    steps = [
        step(from_latex=f"C_1({x1}; {y1}),\\; r_1 = {r1};\\quad C_2({x2}; {y2}),\\; r_2 = {r2}", to_latex_str=f"C_1C_2 = \\sqrt{{{dx}^2 + {dy}^2}} = {dist}", op="Compute distance C1C2 between centres", rule="Distance formula"),
        step(from_latex=f"|r_1 - r_2| = |{r1} - {r2}| = {dist}", to_latex_str=ans, op="Compare C1C2 with |r1 - r2|", rule="Internal tangency condition d = |r1 - r2|"),
    ]
    return _q("43_two_circles_touching_internally", 43, prompt, ans, steps,
              "Calculate the distance C1C2 between the centres and the difference |r1 - r2| between the radii.",
              "When C1C2 = |r1 - r2|, the smaller circle touches the larger circle internally at one point.",
              f"C1C2 = {dist} = {r1} - {r2}, so the circles touch internally.",
              ["confused_internal_and_external_touching_conditions"], "medium", 4)


# 44. Classifying relative position of two general circles (intersecting, disjoint, touching)
def build_44_classify_relative_position_of_two_circles(r: random.Random) -> Dict[str, Any]:
    x1, y1 = r.randint(-3, 2), r.randint(-3, 2)
    dx, dy, dist = r.choice([(3, 4, 5), (6, 8, 10), (5, 12, 13)])
    x2, y2 = x1 + dx, y1 + dy
    case = r.choice(["intersect_two_points", "disjoint_external", "disjoint_internal"])
    if case == "intersect_two_points":
        r1 = dist - 2
        r2 = 4
        rel_str = f"|r_1 - r_2| = {abs(r1-r2)} < {dist} < r_1 + r_2 = {r1+r2}"
        verdict = "intersect in two distinct points"
    elif case == "disjoint_external":
        r1 = max(1, dist // 2 - 1)
        r2 = max(1, dist - r1 - 2)
        rel_str = f"C_1C_2 = {dist} > r_1 + r_2 = {r1+r2}"
        verdict = "do not intersect (lie completely outside each other)"
    else:
        r2 = 2
        r1 = dist + r2 + 3
        rel_str = f"C_1C_2 = {dist} < |r_1 - r_2| = {abs(r1-r2)}"
        verdict = "do not intersect (one circle lies completely inside the other)"
    eq1 = f"{_fmt_shift('x', x1)} + {_fmt_shift('y', y1)} = {r1*r1}"
    eq2 = f"{_fmt_shift('x', x2)} + {_fmt_shift('y', y2)} = {r2*r2}"
    ans = f"{rel_str} \\implies \\text{{{verdict}}}"
    prompt = (
        f"Determine the relative position of the two circles:\n"
        f"$$C_1: {eq1} \\quad \\text{{and}} \\quad C_2: {eq2}$$\n"
        f"Justify your answer by comparing $C_1C_2$ with $r_1 + r_2$ and $|r_1 - r_2|$."
    )
    steps = [
        step(from_latex=f"C_1({x1}; {y1}),\\; C_2({x2}; {y2})", to_latex_str=f"C_1C_2 = {dist},\\; r_1 = {r1},\\; r_2 = {r2}", op="Compute centre distance and radii", rule="Distance and radii"),
        step(from_latex=f"r_1 + r_2 = {r1+r2},\\; |r_1 - r_2| = {abs(r1-r2)}", to_latex_str=ans, op="Compare C1C2 against sum and difference of radii", rule="Two-circle intersection criteria"),
    ]
    return _q("44_classify_relative_position_of_two_circles", 44, prompt, ans, steps,
              f"Calculate C1C2 = {dist}, r1 + r2 = {r1+r2}, and |r1 - r2| = {abs(r1-r2)}.",
              "Compare d against |r1 - r2| and r1 + r2.",
              f"{rel_str}, so the circles {verdict}.",
              ["only_checked_sum_of_radii_ignoring_difference"], "medium", 4)


# 45. Unknown radius r2 so that two circles touch externally
def build_45_unknown_radius_for_touching_circles(r: random.Random) -> Dict[str, Any]:
    x1, y1 = r.randint(-5, 2), r.randint(-5, 2)
    dx, dy, dist = r.choice([(6, 8, 10), (5, 12, 13), (8, 15, 17), (9, 12, 15)])
    x2, y2 = x1 + dx, y1 + dy
    r1 = r.randint(2, dist - 2)
    r2 = dist - r1
    k_rhs = r2 * r2
    eq1 = f"{_fmt_shift('x', x1)} + {_fmt_shift('y', y1)} = {r1*r1}"
    eq2 = f"{_fmt_shift('x', x2)} + {_fmt_shift('y', y2)} = k"
    ans = f"r_2 = {r2}\\text{{ units}}; \\quad k = {k_rhs}"
    prompt = (
        f"The circles $C_1: {eq1}$ and $C_2: {eq2}$ (where $k > 0$) touch each other externally.\n\n"
        f"Determine the radius $r_2$ of circle $C_2$ and hence the value of $k$."
    )
    steps = [
        step(from_latex=f"C_1({x1}; {y1}),\\; C_2({x2}; {y2})", to_latex_str=f"C_1C_2 = \\sqrt{{{dx}^2 + {dy}^2}} = {dist}", op="Find distance between centres C1 and C2", rule="Distance formula"),
        step(from_latex=f"r_1 + r_2 = C_1C_2 \\implies {r1} + r_2 = {dist}", to_latex_str=f"r_2 = {r2} \\implies k = r_2^2 = {k_rhs}", op="Solve for r2 and square to find k", rule="External touching d = r1 + r2"),
    ]
    return _q("45_unknown_radius_for_touching_circles", 45, prompt, ans, steps,
              f"First calculate C1C2 = {dist}, and note that r1 = {r1}.",
              "For external touching, r1 + r2 = C1C2, and k = r2^2.",
              f"r2 = {dist} - {r1} = {r2}, so k = {k_rhs}.",
              ["forgot_to_square_r2_to_find_k"], "medium", 4)


# 46. Two circles SVG diagram: external/secant centres and common chord / line of centres
def build_46_two_circles_svg_diagram_line_of_centres(r: random.Random) -> Dict[str, Any]:
    x1, y1 = r.randint(-4, 0), r.randint(-3, 1)
    dx, dy, dist = r.choice([(3, 4, 5), (6, 8, 10), (5, 12, 13)])
    x2, y2 = x1 + dx, y1 + dy
    r1 = r.randint(2, dist - 1)
    r2 = dist - r1
    m_centres = sp.Rational(dy, dx)
    r1_px = 44 + (r1 % 12)
    r2_px = 34 + (r2 % 12)
    svg = (
        f'<svg viewBox="0 0 380 220" xmlns="http://www.w3.org/2000/svg">'
        f'<rect x="0" y="0" width="380" height="220" fill="#f8fafc" rx="8"/>'
        f'<circle cx="135" cy="115" r="{r1_px}" fill="none" stroke="#1d4ed8" stroke-width="2.5"/>'
        f'<circle cx="{135 + r1_px + r2_px}" cy="115" r="{r2_px}" fill="none" stroke="#0f766e" stroke-width="2.5"/>'
        f'<line x1="135" y1="115" x2="{135 + r1_px + r2_px}" y2="115" stroke="#dc2626" stroke-width="2" stroke-dasharray="4,3"/>'
        f'<circle cx="135" cy="115" r="4" fill="#1d4ed8"/>'
        f'<text x="100" y="138" font-size="11" font-family="sans-serif" fill="#0f172a">C1({x1}; {y1})</text>'
        f'<circle cx="{135 + r1_px + r2_px}" cy="115" r="4" fill="#0f766e"/>'
        f'<text x="{120 + r1_px + r2_px}" y="138" font-size="11" font-family="sans-serif" fill="#0f172a">C2({x2}; {y2})</text>'
        f'<circle cx="{135 + r1_px}" cy="115" r="4" fill="#dc2626"/>'
        f'<text x="{128 + r1_px}" y="103" font-size="11" font-family="sans-serif" fill="#dc2626">P</text>'
        f'</svg>'
    )
    ans = f"C_1C_2 = {dist}\\text{{ units}}; \\quad m_{{C_1C_2}} = {to_latex(m_centres)}; \\quad m_{{\\text{{tan}}}} = {to_latex(sp.Rational(-dx, dy))}"
    prompt = (
        f"Refer to the diagram of two externally touching circles with centres $C_1({x1}; {y1})$ and $C_2({x2}; {y2})$ "
        f"meeting at their point of contact $P$.\n\n"
        f"Calculate the distance $C_1C_2$, the gradient of the line of centres $C_1C_2$, and the gradient of the common tangent at $P$."
    )
    steps = [
        step(from_latex=f"C_1({x1}; {y1}),\\; C_2({x2}; {y2})", to_latex_str=f"C_1C_2 = \\sqrt{{{dx}^2 + {dy}^2}} = {dist}", op="Compute distance between centres", rule="Distance formula"),
        step(from_latex=f"m_{{C_1C_2}} = \\frac{{{dy}}}{{{dx}}} = {to_latex(m_centres)}", to_latex_str=f"m_{{\\text{{tan}}}} = {to_latex(sp.Rational(-dx, dy))}", op="Common tangent at P is perpendicular to line of centres C1C2", rule="m_centres * m_tan = -1"),
    ]
    return _q("46_two_circles_svg_diagram_line_of_centres", 46, prompt, ans, steps,
              "The common internal tangent at the point of contact P is perpendicular to the line of centres C1C2.",
              f"Find C1C2 = {dist} and m_C1C2 = {to_latex(m_centres)}, then invert and negate for m_tan.",
              f"{ans}.",
              ["used_line_of_centres_gradient_as_tangent_gradient"], "medium", 4, _svg_spec(svg))


# 47. Ellipse standard equation x^2/a^2 + y^2/b^2 = 1: vertices and foci c^2 = a^2 - b^2
def build_47_ellipse_standard_equation_axes_and_foci(r: random.Random) -> Dict[str, Any]:
    # Pythagorean triple (b, c, a) so a^2 - b^2 = c^2
    b_val, c_val, a_val = r.choice([(3, 4, 5), (4, 3, 5), (5, 12, 13), (12, 5, 13), (6, 8, 10), (8, 15, 17)])
    a_sq = a_val * a_val
    b_sq = b_val * b_val
    eq = f"\\frac{{x^2}}{{{a_sq}}} + \\frac{{y^2}}{{{b_sq}}} = 1"
    ans = f"(\\pm {a_val}; 0),\\; (0; \\pm {b_val}); \\quad F(\\pm {c_val}; 0)"
    prompt = (
        f"Consider the ellipse with equation:\n"
        f"$${eq}$$\n"
        f"1. Write down the coordinates of the horizontal and vertical intercepts (vertices).\n"
        f"2. Using $c^2 = a^2 - b^2$, determine the coordinates of the foci $F_1$ and $F_2$."
    )
    steps = [
        step(from_latex=f"a^2 = {a_sq},\\; b^2 = {b_sq}", to_latex_str=f"a = {a_val},\\; b = {b_val} \\implies (\\pm {a_val}; 0),\\; (0; \\pm {b_val})", op="Extract semi-major and semi-minor axes a and b", rule="Ellipse intercepts"),
        step(from_latex=f"c^2 = a^2 - b^2 = {a_sq} - {b_sq} = {c_val*c_val}", to_latex_str=f"c = {c_val} \\implies F(\\pm {c_val}; 0)", op="Calculate focal distance c", rule="c^2 = a^2 - b^2"),
    ]
    return _q("47_ellipse_standard_equation_axes_and_foci", 47, prompt, ans, steps,
              f"Here a^2 = {a_sq} and b^2 = {b_sq}, so a = {a_val} and b = {b_val}.",
              f"Substitute into c^2 = a^2 - b^2 = {a_sq} - {b_sq} = {c_val*c_val}.",
              f"Intercepts are (+-{a_val}; 0), (0; +-{b_val}) and foci are (+-{c_val}; 0).",
              ["added_a_squared_and_b_squared_for_ellipse_foci"], "medium", 3)


# 48. Locus of a point equidistant from origin or fixed ratio / circle locus
def build_48_circle_locus_from_perpendicular_gradients_diameter(r: random.Random) -> Dict[str, Any]:
    a = r.randint(-5, 5)
    b = r.randint(-5, 5)
    rad = r.randint(3, 8)
    ax, ay = a - rad, b
    bx, by = a + rad, b
    r_sq = rad * rad
    eq = f"{_fmt_shift('x', a)} + {_fmt_shift('y', b)} = {r_sq}"
    ans = f"M({a}; {b}),\\; r = {rad}; \\quad {eq}"
    prompt = (
        f"Points $A({ax}; {ay})$ and $B({bx}; {by})$ are fixed. A point $P(x; y)$ moves such that "
        f"$\\hat{{P}} = 90^\\circ$ ($AP \\perp BP$).\n\n"
        f"Using the converse of the angle-in-a-semicircle theorem ($AB$ is a diameter), find the centre $M$, radius $r$, and standard equation of the circular locus of $P$."
    )
    steps = [
        step(from_latex=f"A({ax}; {ay}),\\; B({bx}; {by})", to_latex_str=f"M({a}; {b}),\\; r = \\frac{{AB}}{{2}} = {rad}", op="Find midpoint M and half-length r of diameter AB", rule="Angle in a semicircle = 90 deg"),
        step(from_latex=f"M({a}; {b}),\\; r^2 = {r_sq}", to_latex_str=eq, op="Write standard equation of the circle", rule="(x - a)^2 + (y - b)^2 = r^2"),
    ]
    return _q("48_circle_locus_from_perpendicular_gradients_diameter", 48, prompt, ans, steps,
              "Since angle APB = 90 deg, P lies on the circle with diameter AB.",
              f"The centre M is the midpoint of AB and the radius is half the distance AB.",
              f"M({a}; {b}), r = {rad}, giving {eq}.",
              ["used_full_diameter_as_radius"], "medium", 3)


# 49. Misconception diagnosis: auditing a learner's completing-the-square & centre sign error
def build_49_error_analysis_completing_square_and_centre_sign(r: random.Random) -> Dict[str, Any]:
    a = r.choice([3, 4, 5, 6, 7, 8])
    b = r.choice([-8, -7, -6, -5, -4, -3])
    rad = r.randint(4, 10)
    r_sq = rad * rad
    F = a * a + b * b - r_sq
    gen_eq = _fmt_general_circle(a, b, r_sq)
    std_eq = f"{_fmt_shift('x', a)} + {_fmt_shift('y', b)} = {r_sq}"
    ans = f"M({a}; {b}),\\; r = {rad}; \\quad {std_eq}"
    prompt = (
        f"Given the circle equation ${gen_eq}$, a learner writes:\n"
        f"$$(x - {a})^2 + (y + {abs(b)})^2 = {-F}$$\n"
        f"and states that the centre is $(-{a}; {abs(b)})$ with radius $\\sqrt{{{-F}}}$.\n\n"
        f"Identify the two errors made by the learner and determine the correct centre $M$ and radius $r$."
    )
    steps = [
        step(from_latex=f"\\text{{RHS}} = {-F} + ({a})^2 + ({b})^2 = {r_sq}", to_latex_str=f"r = \\sqrt{{{r_sq}}} = {rad}", op="Error 1: Learner forgot to add a^2 + b^2 to the RHS when completing the square", rule="Balance both sides of equation"),
        step(from_latex=std_eq, to_latex_str=f"M({a}; {b})", op="Error 2: Learner did not reverse bracket signs when reading off centre (a; b)", rule="(x - a)^2 + (y - b)^2 = r^2"),
    ]
    return _q("49_error_analysis_completing_square_and_centre_sign", 49, prompt, ans, steps,
              "Check both the RHS constant when completing the square and the signs of the centre coordinates.",
              f"Adding {a*a} + {b*b} to {-F} gives r^2 = {r_sq}, and (x - {a})^2 + (y + {abs(b)})^2 has centre ({a}; {b}).",
              f"Correct centre M({a}; {b}) and radius r = {rad}.",
              ["forgot_add_both_sides", "sign_inversion_of_center"], "medium", 4)


# 50. Multi-part NSC exam synthesis with seeded coordinate SVG diagram
def build_50_multi_part_circle_tangent_exam_synthesis(r: random.Random) -> Dict[str, Any]:
    a = r.choice([-4, -3, -2, 2, 3, 4])
    b = r.choice([-4, -3, -2, 2, 3, 4])
    dx, dy = r.choice([(3, 4), (4, 3)])
    px, py = a + dx, b + dy
    r_sq = dx * dx + dy * dy
    rad = int(math.isqrt(r_sq))
    gen_eq = _fmt_general_circle(a, b, r_sq)
    std_eq = f"{_fmt_shift('x', a)} + {_fmt_shift('y', b)} = {r_sq}"
    m_tan = sp.Rational(-dx, dy)
    c_tan = py - m_tan * px
    tan_eq = _line_latex(m_tan, c_tan)
    rad_svg = 52 + ((abs(a) + abs(b)) % 14)
    svg = (
        f'<svg viewBox="0 0 380 240" xmlns="http://www.w3.org/2000/svg">'
        f'<rect x="0" y="0" width="380" height="240" fill="#f8fafc" rx="8"/>'
        f'<line x1="20" y1="130" x2="360" y2="130" stroke="#94a3b8" stroke-width="1.5"/>'
        f'<line x1="160" y1="15" x2="160" y2="225" stroke="#94a3b8" stroke-width="1.5"/>'
        f'<circle cx="185" cy="115" r="{rad_svg}" fill="none" stroke="#1d4ed8" stroke-width="2.5"/>'
        f'<circle cx="185" cy="115" r="4" fill="#0f172a"/>'
        f'<text x="150" y="128" font-size="11" font-family="sans-serif" fill="#0f172a">M({a}; {b})</text>'
        f'<line x1="185" y1="115" x2="{185 + int(rad_svg*0.6)}" y2="{115 - int(rad_svg*0.8)}" stroke="#475569" stroke-width="1.8" stroke-dasharray="4,3"/>'
        f'<circle cx="{185 + int(rad_svg*0.6)}" cy="{115 - int(rad_svg*0.8)}" r="4" fill="#dc2626"/>'
        f'<text x="{192 + int(rad_svg*0.6)}" y="{112 - int(rad_svg*0.8)}" font-size="11" font-family="sans-serif" fill="#0f172a">P({px}; {py})</text>'
        f'<line x1="{185 + int(rad_svg*0.6) - 68}" y1="{115 - int(rad_svg*0.8) - 51}" x2="{185 + int(rad_svg*0.6) + 68}" y2="{115 - int(rad_svg*0.8) + 51}" stroke="#dc2626" stroke-width="2.2"/>'
        f'<text x="{185 + int(rad_svg*0.6) + 45}" y="{115 - int(rad_svg*0.8) + 64}" font-size="11" font-family="sans-serif" fill="#dc2626">T</text>'
        f'</svg>'
    )
    ans = f"M({a}; {b}),\\; r = {rad}; \\quad {tan_eq}; \\quad T\\left(0; {to_latex(c_tan)}\\right)"
    prompt = (
        f"Refer to the coordinate diagram of the circle ${gen_eq}$ with centre $M$ and tangent $PT$ at $P({px}; {py})$.\n\n"
        f"1. Write the circle equation in standard form ${std_eq}$ and state the centre $M$ and radius $r$.\n"
        f"2. Determine the equation of the tangent $PT$ in the form $y = mx + c$.\n"
        f"3. Write down the coordinates of $T$, the vertical-axis intercept of the tangent."
    )
    steps = [
        step(from_latex=gen_eq, to_latex_str=f"{std_eq} \\implies M({a}; {b}),\\; r = {rad}", op="Complete the square for centre M and radius r", rule="Completing the square"),
        step(from_latex=f"m_{{MP}} = \\frac{{{dy}}}{{{dx}}} \\implies m_{{\\text{{tan}}}} = {to_latex(m_tan)}", to_latex_str=tan_eq, op="Find tangent equation using perpendicular gradient at P", rule="m_MP * m_tan = -1"),
        step(from_latex="x = 0", to_latex_str=f"T\\left(0; {to_latex(c_tan)}\\right)", op="Evaluate vertical-axis intercept at x = 0", rule="y-intercept"),
    ]
    return _q("50_multi_part_circle_tangent_exam_synthesis", 50, prompt, ans, steps,
              "Complete the square first to confirm M(a; b) and r, then use m_MP * m_tan = -1.",
              f"Substitute P({px}; {py}) and m_tan = {to_latex(m_tan)} into y - y_P = m_tan(x - x_P).",
              f"M({a}; {b}), r = {rad}, tangent {tan_eq}, and T(0; {to_latex(c_tan)}).",
              ["sign_inversion_of_center", "used_same_gradient_as_radius"], "hard", 6, _svg_spec(svg))


BUILDERS_26_50: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    "26_radius_and_tangent_gradients_at_point": build_26_radius_and_tangent_gradients_at_point,
    "27_tangent_equation_to_origin_circle": build_27_tangent_equation_to_origin_circle,
    "28_tangent_equation_to_shifted_circle": build_28_tangent_equation_to_shifted_circle,
    "29_tangent_equation_from_general_circle_form": build_29_tangent_equation_from_general_circle_form,
    "30_horizontal_and_vertical_tangents": build_30_horizontal_and_vertical_tangents,
    "31_tangent_length_from_external_point_pythagoras": build_31_tangent_length_from_external_point_pythagoras,
    "32_two_tangents_from_external_point_kite_properties": build_32_two_tangents_from_external_point_kite_properties,
    "33_two_parallel_tangents_with_given_gradient": build_33_two_parallel_tangents_with_given_gradient,
    "34_angle_of_inclination_of_radius_and_tangent": build_34_angle_of_inclination_of_radius_and_tangent,
    "35_circle_and_tangent_svg_diagram": build_35_circle_and_tangent_svg_diagram,
    "36_secant_line_circle_intersection_points": build_36_secant_line_circle_intersection_points,
    "37_chord_midpoint_and_perpendicular_from_centre": build_37_chord_midpoint_and_perpendicular_from_centre,
    "38_length_of_chord_on_coordinate_axis": build_38_length_of_chord_on_coordinate_axis,
    "39_classify_line_circle_intersection_via_discriminant": build_39_classify_line_circle_intersection_via_discriminant,
    "40_tangent_parameter_k_via_equal_roots": build_40_tangent_parameter_k_via_equal_roots,
    "41_distance_between_two_circle_centres": build_41_distance_between_two_circle_centres,
    "42_two_circles_touching_externally": build_42_two_circles_touching_externally,
    "43_two_circles_touching_internally": build_43_two_circles_touching_internally,
    "44_classify_relative_position_of_two_circles": build_44_classify_relative_position_of_two_circles,
    "45_unknown_radius_for_touching_circles": build_45_unknown_radius_for_touching_circles,
    "46_two_circles_svg_diagram_line_of_centres": build_46_two_circles_svg_diagram_line_of_centres,
    "47_ellipse_standard_equation_axes_and_foci": build_47_ellipse_standard_equation_axes_and_foci,
    "48_circle_locus_from_perpendicular_gradients_diameter": build_48_circle_locus_from_perpendicular_gradients_diameter,
    "49_error_analysis_completing_square_and_centre_sign": build_49_error_analysis_completing_square_and_centre_sign,
    "50_multi_part_circle_tangent_exam_synthesis": build_50_multi_part_circle_tangent_exam_synthesis,
}
