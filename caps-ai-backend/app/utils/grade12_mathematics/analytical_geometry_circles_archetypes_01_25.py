"""Grade 12 Mathematics — Analytical Geometry (Circles) Archetypes 01–25.
100% Aligned with South African National Curriculum Standards (Grade 12 Term 2).
Grounded in curriculum_docs_auto/Mathematics_Gr12/Term 2/02. Analytical geometry.md.
"""
from __future__ import annotations

import math
import random
from typing import Any, Callable, Dict, List, Optional

from app.utils.grade12_mathematics._math_common import (
    make_math_question,
    num,
    solution_graph,
    step,
)

TOPIC = "Analytical geometry"
LO_PREFIX = "math12_analytical_circles"


def _svg_spec(svg: str) -> Dict[str, Any]:
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


def _fmt_shift(var: str, val: int) -> str:
    if val == 0:
        return f"{var}^2"
    if val > 0:
        return f"({var} - {val})^2"
    return f"({var} + {abs(val)})^2"


def _fmt_general_circle(a: int, b: int, r_sq: int) -> str:
    D = -2 * a
    E = -2 * b
    F = a * a + b * b - r_sq
    parts = ["x^2 + y^2"]
    if D != 0:
        parts.append(f"+ {D}x" if D > 0 else f"- {abs(D)}x")
    if E != 0:
        parts.append(f"+ {E}y" if E > 0 else f"- {abs(E)}y")
    if F != 0:
        parts.append(f"+ {F}" if F > 0 else f"- {abs(F)}")
    return " ".join(parts) + " = 0"


def _q(
    subskill: str,
    idx: int,
    prompt: str,
    ans_latex: str,
    steps_list: List[Dict[str, Any]],
    nudge: str,
    concept: str,
    breakdown: str,
    tags: List[str],
    difficulty: str = "medium",
    marks: int = 3,
    diagram_spec: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    sol = solution_graph(
        goal=f"Solve {subskill}",
        chain_type="expression",
        var="x",
        steps=steps_list,
        final_latex=ans_latex,
    )
    marking = {
        "total_marks": marks,
        "marking_points": [
            {"id": f"mp_{i+1}", "desc": st.get("op", f"Step {i+1}"), "marks": 1, "editable": True}
            for i, st in enumerate(steps_list[:marks])
        ] or [{"id": "mp_1", "desc": "Correct answer", "marks": marks, "editable": True}],
        "deductions": [],
        "carry_forward_rule": "consequential_accuracy",
    }
    return make_math_question(
        prefix=f"g12_ag_{idx:02d}",
        topic=TOPIC,
        subskill=subskill,
        learning_objective_id=f"{LO_PREFIX}_{idx:02d}",
        prompt=prompt,
        prompt_latex=prompt,
        answer_latex=ans_latex,
        answer_sympy=ans_latex,
        sample_answer=ans_latex,
        canonical_solution=sol,
        marking_schema=marking,
        hints={"nudge": nudge, "concept": concept, "breakdown": breakdown},
        misconception_tags=tags,
        term=2,
        caps_weight_percent=25,
        suggested_duration_mins=5,
        difficulty=difficulty,
        diagram_spec=diagram_spec,
    )


# 01. Origin circle equation from given integer radius
def build_01_origin_circle_equation_from_radius(r: random.Random) -> Dict[str, Any]:
    rad = r.randint(2, 19)
    r_sq = rad * rad
    ans = f"x^2 + y^2 = {r_sq}"
    prompt = (
        f"Determine the equation of the circle centred at the origin $(0; 0)$ "
        f"with a radius of $r = {rad}$ units."
    )
    steps = [
        step(from_latex="x^2 + y^2 = r^2", to_latex_str=f"x^2 + y^2 = ({rad})^2", op="Substitute radius r into standard origin circle equation", rule="x^2 + y^2 = r^2"),
        step(from_latex=f"r^2 = {rad}^2", to_latex_str=ans, op="Square the radius", rule="Simplification"),
    ]
    return _q("01_origin_circle_equation_from_radius", 1, prompt, ans, steps,
              "Substitute the given radius into x^2 + y^2 = r^2.",
              "A circle with centre (0; 0) and radius r has equation x^2 + y^2 = r^2.",
              f"Squaring r = {rad} gives x^2 + y^2 = {r_sq}.",
              ["forgot_to_square_radius_on_rhs"], "easy", 2)


# 02. Origin circle equation from surd radius
def build_02_origin_circle_equation_from_surd_radius(r: random.Random) -> Dict[str, Any]:
    k = r.choice([2, 3, 4, 5, 6])
    m = r.choice([2, 3, 5, 6, 7, 10, 11])
    r_sq = k * k * m
    ans = f"x^2 + y^2 = {r_sq}"
    prompt = (
        f"Write down the equation of the circle with centre at the origin $(0; 0)$ "
        f"and radius $r = {k}\\sqrt{{{m}}}$ units."
    )
    steps = [
        step(from_latex="x^2 + y^2 = r^2", to_latex_str=f"x^2 + y^2 = ({k}\\sqrt{{{m}}})^2", op="Substitute surd radius into x^2 + y^2 = r^2", rule="Origin circle formula"),
        step(from_latex=f"({k}\\sqrt{{{m}}})^2 = {k*k} \\times {m}", to_latex_str=ans, op="Evaluate the square of the surd", rule="(k*sqrt(m))^2 = k^2 * m"),
    ]
    return _q("02_origin_circle_equation_from_surd_radius", 2, prompt, ans, steps,
              f"Square both the integer factor {k} and the surd sqrt({m}).",
              "(k*sqrt(m))^2 = k^2 * m.",
              f"r^2 = {k}^2 * {m} = {r_sq}, giving {ans}.",
              ["squared_only_the_radical_and_not_coefficient"], "easy", 2)


# 03. Radius and simplified surd from origin circle equation
def build_03_origin_circle_radius_from_equation(r: random.Random) -> Dict[str, Any]:
    coeff = r.choice([2, 3, 4, 5])
    k = r.choice([2, 3, 4, 5])
    m = r.choice([2, 3, 5, 6, 7])
    r_sq = k * k * m
    rhs = coeff * r_sq
    ans = f"r = \\sqrt{{{r_sq}}} = {k}\\sqrt{{{m}}}\\text{{ units}}"
    prompt = (
        f"Given the circle with equation ${coeff}x^2 + {coeff}y^2 = {rhs}$:\n\n"
        f"Write the equation in standard form $x^2 + y^2 = r^2$ and express the radius $r$ in simplest surd form."
    )
    steps = [
        step(from_latex=f"{coeff}x^2 + {coeff}y^2 = {rhs}", to_latex_str=f"x^2 + y^2 = {r_sq}", op=f"Divide throughout by {coeff}", rule="Normalise coefficients of x^2 and y^2 to 1"),
        step(from_latex=f"r^2 = {r_sq}", to_latex_str=ans, op="Take positive square root and simplify surd", rule="r = sqrt(r^2) > 0"),
    ]
    return _q("03_origin_circle_radius_from_equation", 3, prompt, ans, steps,
              f"First divide the entire equation by {coeff} so the coefficients of x^2 and y^2 equal 1.",
              "Once in the form x^2 + y^2 = r^2, take the positive square root of the RHS.",
              f"x^2 + y^2 = {r_sq}, so r = sqrt({r_sq}) = {k}*sqrt({m}).",
              ["did_not_divide_by_common_coefficient_before_root"], "easy", 3)


# 04. Origin circle passing through a given point P(x1; y1)
def build_04_origin_circle_passing_through_point(r: random.Random) -> Dict[str, Any]:
    px = r.choice([-9, -8, -7, -6, -5, -4, -3, 3, 4, 5, 6, 7, 8, 9])
    py = r.choice([-9, -7, -6, -5, -4, -2, 2, 4, 5, 6, 7, 9])
    r_sq = px * px + py * py
    ans = f"x^2 + y^2 = {r_sq}"
    prompt = (
        f"Find the equation of the circle with centre at the origin $(0; 0)$ "
        f"that passes through the point $P({px}; {py})$."
    )
    steps = [
        step(from_latex=f"P({px}; {py}) \\in x^2 + y^2 = r^2", to_latex_str=f"r^2 = ({px})^2 + ({py})^2 = {px*px} + {py*py} = {r_sq}", op="Substitute coordinates of P into x^2 + y^2 = r^2", rule="Point on circumference satisfies circle equation"),
        step(from_latex=f"r^2 = {r_sq}", to_latex_str=ans, op="State circle equation", rule="x^2 + y^2 = r^2"),
    ]
    return _q("04_origin_circle_passing_through_point", 4, prompt, ans, steps,
              f"Substitute x = {px} and y = {py} into x^2 + y^2 = r^2.",
              "The square of the distance from (0; 0) to P(x1; y1) is r^2 = x1^2 + y1^2.",
              f"r^2 = ({px})^2 + ({py})^2 = {r_sq}, so {ans}.",
              ["negative_square_sign_error"], "easy", 3)


# 05.Unknown coordinate on an origin circle in a specified quadrant
def build_05_origin_circle_unknown_coordinate(r: random.Random) -> Dict[str, Any]:
    triples = [(3, 4, 5), (5, 12, 13), (6, 8, 10), (8, 15, 17), (9, 12, 15), (7, 24, 25)]
    a, b, rad = r.choice(triples)
    if r.choice([True, False]):
        a, b = b, a
    sign_x = r.choice([-1, 1])
    sign_y = r.choice([-1, 1])
    px = sign_x * a
    py = sign_y * b
    r_sq = rad * rad
    cond = "y < 0" if py < 0 else "y > 0"
    ans = f"k = {py}"
    prompt = (
        f"The point $A({px}; k)$ lies on the circle $x^2 + y^2 = {r_sq}$, where ${cond}$.\n\n"
        f"Calculate the value of $k$."
    )
    steps = [
        step(from_latex=f"({px})^2 + k^2 = {r_sq}", to_latex_str=f"k^2 = {r_sq} - {px*px} = {b*b}", op="Substitute x-coordinate into circle equation", rule="Coordinate substitution"),
        step(from_latex=f"k = \\pm {b},\\; {cond}", to_latex_str=ans, op="Select sign matching the given inequality", rule="Sign selection"),
    ]
    return _q("05_origin_circle_unknown_coordinate", 5, prompt, ans, steps,
              f"Substitute x = {px} into x^2 + y^2 = {r_sq} and solve for k^2.",
              f"Take the square root and apply the condition {cond}.",
              f"k^2 = {b*b}, and since {cond}, {ans}.",
              ["omitted_negative_root_when_solving_quadratic"], "easy", 3)


# 06. Testing whether a point lies inside, on, or outside an origin circle
def build_06_point_position_relative_to_origin_circle(r: random.Random) -> Dict[str, Any]:
    rad = r.randint(5, 14)
    r_sq = rad * rad
    px = r.randint(-12, 12)
    py = r.randint(-12, 12)
    d_sq = px * px + py * py
    if d_sq < r_sq:
        pos = "inside"
        rel = "<"
    elif d_sq == r_sq:
        pos = "on"
        rel = "="
    else:
        pos = "outside"
        rel = ">"
    ans = f"OP^2 = {d_sq} {rel} {r_sq} \\implies \\text{{{pos} the circle}}"
    prompt = (
        f"A circle with centre at the origin has equation $x^2 + y^2 = {r_sq}$.\n\n"
        f"Determine by calculation whether the point $P({px}; {py})$ lies inside, on, or outside the circle."
    )
    steps = [
        step(from_latex=f"OP^2 = x_P^2 + y_P^2", to_latex_str=f"OP^2 = ({px})^2 + ({py})^2 = {d_sq}", op="Compute squared distance OP^2 from origin to P", rule="Distance formula squared"),
        step(from_latex=f"OP^2 = {d_sq},\\; r^2 = {r_sq}", to_latex_str=ans, op="Compare OP^2 with r^2", rule="Interior/exterior test"),
    ]
    return _q("06_point_position_relative_to_origin_circle", 6, prompt, ans, steps,
              f"Calculate OP^2 = ({px})^2 + ({py})^2 and compare with r^2 = {r_sq}.",
              "If OP^2 < r^2 the point is inside; if OP^2 = r^2 it is on; if OP^2 > r^2 it is outside.",
              f"OP^2 = {d_sq} {rel} {r_sq}, so P lies {pos} the circle.",
              ["compared_op_squared_with_r_instead_of_r_squared"], "easy", 3)


# 07. Symmetry and reflections of a point on an origin circle
def build_07_origin_circle_symmetry_and_reflections(r: random.Random) -> Dict[str, Any]:
    px = r.choice([-11, -9, -7, -5, -4, 4, 5, 7, 9, 11])
    py = r.choice([-10, -8, -6, -3, 3, 6, 8, 10])
    r_sq = px * px + py * py
    rule_choice = r.choice(["x_axis", "y_axis", "line_y_eq_x", "origin"])
    if rule_choice == "x_axis":
        desc = "reflection about the horizontal coordinate axis ($y = 0$)"
        qx, qy = px, -py
    elif rule_choice == "y_axis":
        desc = "reflection about the vertical coordinate axis ($x = 0$)"
        qx, qy = -px, py
    elif rule_choice == "line_y_eq_x":
        desc = "reflection about the line $y = x$"
        qx, qy = py, px
    else:
        desc = "rotation of $180^\\circ$ about the origin $(0; 0)$"
        qx, qy = -px, -py
    ans = f"Q({qx}; {qy}); \\quad x^2 + y^2 = {r_sq}"
    prompt = (
        f"The point $P({px}; {py})$ lies on a circle centred at the origin.\n\n"
        f"1. Write down the equation of the circle.\n"
        f"2. Determine the coordinates of $Q$, the transformed point obtained from $P$ under {desc}, and verify that $Q$ lies on the circle."
    )
    steps = [
        step(from_latex=f"r^2 = ({px})^2 + ({py})^2", to_latex_str=f"x^2 + y^2 = {r_sq}", op="Determine circle equation", rule="x^2 + y^2 = r^2"),
        step(from_latex=f"P({px}; {py})", to_latex_str=f"Q({qx}; {qy}),\\quad ({qx})^2 + ({qy})^2 = {r_sq}", op=f"Apply {desc}", rule="Circle symmetry about origin"),
    ]
    return _q("07_origin_circle_symmetry_and_reflections", 7, prompt, ans, steps,
              "Apply the coordinate transformation rule to P(x; y).",
              "A circle centred at the origin is symmetric under reflections in both axes, y = x, and the origin.",
              f"The circle is x^2 + y^2 = {r_sq} and the image is Q({qx}; {qy}).",
              ["swapped_coordinates_for_axis_reflection"], "easy", 3)


# 08. Origin circle SVG coordinate diagram: read point P and find equation & diameter
def build_08_origin_circle_svg_coordinate_diagram(r: random.Random) -> Dict[str, Any]:
    px = r.choice([3, 4, 5, 6, 7, 8]) * r.choice([-1, 1])
    py = r.choice([3, 4, 5, 6, 7, 8]) * r.choice([-1, 1])
    r_sq = px * px + py * py
    qx, qy = -px, -py
    rad_px = 52 + (r_sq % 18)
    svg = (
        f'<svg viewBox="0 0 320 240" xmlns="http://www.w3.org/2000/svg">'
        f'<rect x="0" y="0" width="320" height="240" fill="#f8fafc" rx="8"/>'
        f'<line x1="30" y1="120" x2="290" y2="120" stroke="#64748b" stroke-width="1.5"/>'
        f'<line x1="160" y1="20" x2="160" y2="220" stroke="#64748b" stroke-width="1.5"/>'
        f'<circle cx="160" cy="120" r="{rad_px}" fill="none" stroke="#1d4ed8" stroke-width="2.5"/>'
        f'<line x1="{160 - int(rad_px*0.7)}" y1="{120 + int(rad_px*0.7)}" x2="{160 + int(rad_px*0.7)}" y2="{120 - int(rad_px*0.7)}" stroke="#dc2626" stroke-width="2"/>'
        f'<circle cx="{160 + int(rad_px*0.7)}" cy="{120 - int(rad_px*0.7)}" r="4" fill="#dc2626"/>'
        f'<text x="{168 + int(rad_px*0.7)}" y="{116 - int(rad_px*0.7)}" font-size="12" font-family="sans-serif" fill="#0f172a">P({px}; {py})</text>'
        f'<circle cx="{160 - int(rad_px*0.7)}" cy="{120 + int(rad_px*0.7)}" r="4" fill="#dc2626"/>'
        f'<text x="{110 - int(rad_px*0.7)}" y="{136 + int(rad_px*0.7)}" font-size="12" font-family="sans-serif" fill="#0f172a">Q</text>'
        f'<text x="165" y="134" font-size="11" font-family="sans-serif" fill="#334155">O(0;0)</text>'
        f'</svg>'
    )
    ans = f"x^2 + y^2 = {r_sq}; \\quad Q({qx}; {qy})"
    prompt = (
        f"Refer to the coordinate sketch of a circle centred at the origin $O(0; 0)$ with diameter $PQ$, "
        f"where $P({px}; {py})$ lies on the circumference.\n\n"
        f"Determine the equation of the circle and the coordinates of $Q$."
    )
    steps = [
        step(from_latex=f"P({px}; {py})", to_latex_str=f"r^2 = ({px})^2 + ({py})^2 = {r_sq} \\implies x^2 + y^2 = {r_sq}", op="Substitute P into x^2 + y^2 = r^2", rule="Origin circle"),
        step(from_latex="\\text{Midpoint of } PQ = O(0; 0)", to_latex_str=f"Q({qx}; {qy})", op="Use midpoint O(0; 0) to find opposite end of diameter", rule="x_Q = -x_P, y_Q = -y_P"),
    ]
    return _q("08_origin_circle_svg_coordinate_diagram", 8, prompt, ans, steps,
              "Since O(0; 0) is the midpoint of diameter PQ, Q has coordinates (-x_P; -y_P).",
              "Substitute P into x^2 + y^2 = r^2 for the circle equation.",
              f"x^2 + y^2 = {r_sq} and Q({qx}; {qy}).",
              ["halved_coordinates_instead_of_negating_for_origin_midpoint"], "easy", 3, _svg_spec(svg))


# 09. Standard form (x - a)^2 + (y - b)^2 = r^2 from centre and radius
def build_09_standard_circle_equation_from_centre_and_radius(r: random.Random) -> Dict[str, Any]:
    a = r.choice([-9, -7, -6, -5, -4, -3, -2, 2, 3, 4, 5, 6, 7, 9])
    b = r.choice([-8, -7, -5, -4, -3, -1, 1, 3, 4, 5, 7, 8])
    rad = r.randint(2, 15)
    r_sq = rad * rad
    ans = f"{_fmt_shift('x', a)} + {_fmt_shift('y', b)} = {r_sq}"
    prompt = (
        f"Write down the equation of the circle with centre $M({a}; {b})$ "
        f"and radius $r = {rad}$ units in standard form."
    )
    steps = [
        step(from_latex="(x - a)^2 + (y - b)^2 = r^2", to_latex_str=f"{_fmt_shift('x', a)} + {_fmt_shift('y', b)} = ({rad})^2", op=f"Substitute a = {a}, b = {b}, r = {rad}", rule="Standard circle equation"),
        step(from_latex=f"r^2 = {r_sq}", to_latex_str=ans, op="Square the radius", rule="Simplification"),
    ]
    return _q("09_standard_circle_equation_from_centre_and_radius", 9, prompt, ans, steps,
              "Remember the minus signs in (x - a)^2 + (y - b)^2 = r^2.",
              f"Substituting a = {a} and b = {b} reverses the signs inside the brackets.",
              f"The equation is {ans}.",
              ["sign_inversion_of_center"], "easy", 2)


# 10. Reading centre and radius from standard form equation
def build_10_read_centre_and_radius_from_standard_form(r: random.Random) -> Dict[str, Any]:
    a = r.choice([-11, -8, -6, -4, -2, 0, 2, 4, 6, 8, 11])
    b = r.choice([-9, -7, -5, -3, 3, 5, 7, 9])
    rad = r.randint(3, 16)
    r_sq = rad * rad
    eq = f"{_fmt_shift('x', a)} + {_fmt_shift('y', b)} = {r_sq}"
    ans = f"\\text{{Centre}} = ({a}; {b}); \\quad r = {rad}\\text{{ units}}"
    prompt = (
        f"Given the circle with equation ${eq}$:\n\n"
        f"Write down the coordinates of the centre and the length of the radius."
    )
    steps = [
        step(from_latex=eq, to_latex_str=f"(a; b) = ({a}; {b})", op="Extract centre coordinates by comparing with (x - a)^2 + (y - b)^2 = r^2", rule="Centre extraction"),
        step(from_latex=f"r^2 = {r_sq}", to_latex_str=f"r = \\sqrt{{{r_sq}}} = {rad}", op="Take positive square root for radius", rule="r = sqrt(r^2)"),
    ]
    return _q("10_read_centre_and_radius_from_standard_form", 10, prompt, ans, steps,
              "Compare each bracket with (x - a)^2 and (y - b)^2.",
              "If a bracket is (x + k)^2, the coordinate is -k; if x^2 appears alone, the coordinate is 0.",
              f"Centre = ({a}; {b}) and r = {rad} units.",
              ["sign_inversion_of_center", "reported_r_squared_as_radius"], "easy", 2)


# 11. Circle equation given centre M(a; b) and point P(x1; y1) on circumference
def build_11_circle_equation_from_centre_and_point(r: random.Random) -> Dict[str, Any]:
    a = r.randint(-6, 6)
    b = r.randint(-6, 6)
    dx = r.choice([-6, -5, -4, -3, -2, 2, 3, 4, 5, 6])
    dy = r.choice([-6, -5, -4, -3, -2, 2, 3, 4, 5, 6])
    px = a + dx
    py = b + dy
    r_sq = dx * dx + dy * dy
    ans = f"{_fmt_shift('x', a)} + {_fmt_shift('y', b)} = {r_sq}"
    prompt = (
        f"Determine the standard equation of the circle with centre $M({a}; {b})$ "
        f"that passes through the point $P({px}; {py})$."
    )
    steps = [
        step(from_latex=f"r^2 = ({px} - ({a}))^2 + ({py} - ({b}))^2", to_latex_str=f"r^2 = ({dx})^2 + ({dy})^2 = {r_sq}", op="Calculate r^2 using distance formula between M and P", rule="r^2 = (x_P - a)^2 + (y_P - b)^2"),
        step(from_latex=f"M({a}; {b}),\\; r^2 = {r_sq}", to_latex_str=ans, op="Substitute centre and r^2 into standard form", rule="(x - a)^2 + (y - b)^2 = r^2"),
    ]
    return _q("11_circle_equation_from_centre_and_point", 11, prompt, ans, steps,
              f"Substitute M({a}; {b}) and P({px}; {py}) into r^2 = (x - a)^2 + (y - b)^2.",
              "The radius squared is the squared distance between the centre M and point P.",
              f"r^2 = {dx}^2 + {dy}^2 = {r_sq}, giving {ans}.",
              ["substituted_point_as_centre_coordinates"], "medium", 3)


# 12. Circle equation given endpoints A and B of a diameter
def build_12_circle_equation_from_diameter_endpoints(r: random.Random) -> Dict[str, Any]:
    a = r.randint(-5, 5)
    b = r.randint(-5, 5)
    dx = r.choice([2, 3, 4, 5, 6]) * r.choice([-1, 1])
    dy = r.choice([2, 3, 4, 5, 6]) * r.choice([-1, 1])
    ax, ay = a - dx, b - dy
    bx, by = a + dx, b + dy
    r_sq = dx * dx + dy * dy
    ans = f"{_fmt_shift('x', a)} + {_fmt_shift('y', b)} = {r_sq}"
    prompt = (
        f"The line segment joining $A({ax}; {ay})$ and $B({bx}; {by})$ is a diameter of a circle.\n\n"
        f"1. Determine the coordinates of the centre $M$ of the circle.\n"
        f"2. Determine the equation of the circle in standard form."
    )
    steps = [
        step(from_latex=f"M = \\left(\\frac{{{ax} + ({bx})}}{{2}}; \\frac{{{ay} + ({by})}}{{2}}\\right)", to_latex_str=f"M({a}; {b})", op="Find centre M as midpoint of diameter AB", rule="Midpoint formula"),
        step(from_latex=f"r^2 = MB^2 = ({bx} - ({a}))^2 + ({by} - ({b}))^2", to_latex_str=f"r^2 = {dx*dx} + {dy*dy} = {r_sq}", op="Compute squared radius from M to B", rule="Distance formula"),
        step(from_latex=f"M({a}; {b}),\\; r^2 = {r_sq}", to_latex_str=ans, op="Write standard circle equation", rule="(x - a)^2 + (y - b)^2 = r^2"),
    ]
    return _q("12_circle_equation_from_diameter_endpoints", 12, prompt, ans, steps,
              "The centre M is the midpoint of diameter AB, and the radius is the distance MB.",
              "Do not use the full length AB as the radius; r = AB / 2 = MB.",
              f"Centre M({a}; {b}) and r^2 = {r_sq}, so {ans}.",
              ["used_diameter_squared_instead_of_radius_squared"], "medium", 4)


# 13. Expanding standard circle equation into general form x^2 + y^2 + Dx + Ey + F = 0
def build_13_expand_standard_to_general_form(r: random.Random) -> Dict[str, Any]:
    a = r.choice([-7, -6, -5, -4, -3, -2, 2, 3, 4, 5, 6, 7])
    b = r.choice([-7, -6, -5, -4, -3, -2, 2, 3, 4, 5, 6, 7])
    rad = r.randint(3, 10)
    r_sq = rad * rad
    std_eq = f"{_fmt_shift('x', a)} + {_fmt_shift('y', b)} = {r_sq}"
    gen_eq = _fmt_general_circle(a, b, r_sq)
    D, E, F = -2 * a, -2 * b, a * a + b * b - r_sq
    ans = f"{gen_eq} \\quad (D = {D},\\; E = {E},\\; F = {F})"
    prompt = (
        f"Rewrite the circle equation ${std_eq}$ in the general expanded form "
        f"$x^2 + y^2 + Dx + Ey + F = 0$, stating the values of $D$, $E$, and $F$."
    )
    steps = [
        step(from_latex=std_eq, to_latex_str=f"(x^2 {'+' if D>0 else '-'} {abs(D)}x + {a*a}) + (y^2 {'+' if E>0 else '-'} {abs(E)}y + {b*b}) = {r_sq}", op="Expand both binomial squares", rule="(u - v)^2 = u^2 - 2uv + v^2"),
        step(from_latex=f"F = {a*a} + {b*b} - {r_sq} = {F}", to_latex_str=ans, op="Collect constant terms on the LHS", rule="Standard general form"),
    ]
    return _q("13_expand_standard_to_general_form", 13, prompt, ans, steps,
              "Expand both squared brackets using (x - a)^2 = x^2 - 2ax + a^2.",
              "Subtract r^2 from both sides so the RHS equals 0.",
              f"Expanding gives {gen_eq}.",
              ["omitted_middle_term_when_squaring_binomial"], "easy", 3)


# 14. Completing the square (even coefficients) to find centre and radius
def build_14_complete_square_even_coefficients(r: random.Random) -> Dict[str, Any]:
    a = r.choice([-8, -6, -5, -4, -3, -2, 2, 3, 4, 5, 6, 8])
    b = r.choice([-7, -6, -5, -4, -3, -1, 1, 3, 4, 5, 6, 7])
    rad = r.randint(3, 11)
    r_sq = rad * rad
    gen_eq = _fmt_general_circle(a, b, r_sq)
    std_eq = f"{_fmt_shift('x', a)} + {_fmt_shift('y', b)} = {r_sq}"
    ans = f"{std_eq}; \\quad M({a}; {b}),\\; r = {rad}"
    prompt = (
        f"The equation of a circle is given by ${gen_eq}$.\n\n"
        f"Complete the square to write the equation in standard form and state the centre $M$ and radius $r$."
    )
    F = a * a + b * b - r_sq
    steps = [
        step(from_latex=gen_eq, to_latex_str=f"(x^2 {'+' if -2*a>0 else '-'} {abs(2*a)}x + {a*a}) + (y^2 {'+' if -2*b>0 else '-'} {abs(2*b)}y + {b*b}) = {-F} + {a*a} + {b*b}", op="Group x and y terms and add (half coefficient)^2 to both sides", rule="Completing the square"),
        step(from_latex=std_eq, to_latex_str=ans, op="Factorise trinomials and read off centre and radius", rule="(x - a)^2 + (y - b)^2 = r^2"),
    ]
    return _q("14_complete_square_even_coefficients", 14, prompt, ans, steps,
              "Move the constant term to the RHS and add (D/2)^2 and (E/2)^2 to both sides.",
              f"Adding {a*a} and {b*b} to both sides completes the squares in x and y.",
              f"Standard form: {std_eq}, so M({a}; {b}) and r = {rad}.",
              ["forgot_add_both_sides", "sign_inversion_of_center"], "medium", 4)


# 15. Completing the square when x^2 and y^2 have a non-unit coefficient k > 1
def build_15_complete_square_non_unit_leading_coefficient(r: random.Random) -> Dict[str, Any]:
    k = r.choice([2, 3, 4])
    a = r.choice([-5, -4, -3, -2, 2, 3, 4, 5])
    b = r.choice([-5, -4, -3, -2, 2, 3, 4, 5])
    rad = r.randint(2, 7)
    r_sq = rad * rad
    D = -2 * a * k
    E = -2 * b * k
    F = k * (a * a + b * b - r_sq)
    eq = f"{k}x^2 + {k}y^2 {'+' if D>0 else '-'} {abs(D)}x {'+' if E>0 else '-'} {abs(E)}y {'+' if F>=0 else '-'} {abs(F)} = 0"
    std_eq = f"{_fmt_shift('x', a)} + {_fmt_shift('y', b)} = {r_sq}"
    ans = f"{std_eq}; \\quad M({a}; {b}),\\; r = {rad}"
    prompt = (
        f"Determine the coordinates of the centre $M$ and the length of the radius $r$ of the circle:\n"
        f"$${eq}$$"
    )
    steps = [
        step(from_latex=eq, to_latex_str=_fmt_general_circle(a, b, r_sq), op=f"Divide every term by {k}", rule="Normalise leading coefficients to 1"),
        step(from_latex=_fmt_general_circle(a, b, r_sq), to_latex_str=ans, op="Complete the square in x and y", rule="(x - a)^2 + (y - b)^2 = r^2"),
    ]
    return _q("15_complete_square_non_unit_leading_coefficient", 15, prompt, ans, steps,
              f"First divide the entire equation by {k} so that the coefficients of x^2 and y^2 are 1.",
              "Never complete the square before dividing out the common coefficient of x^2 and y^2.",
              f"Dividing by {k} and completing the square gives {std_eq}, M({a}; {b}), r = {rad}.",
              ["completed_square_without_dividing_by_leading_coefficient"], "medium", 4)


# 16. Completing the square with odd linear coefficients (fractional centre)
def build_16_complete_square_odd_coefficients_fractional_centre(r: random.Random) -> Dict[str, Any]:
    num_a = r.choice([-7, -5, -3, -1, 1, 3, 5, 7])
    num_b = r.choice([-7, -5, -3, -1, 1, 3, 5, 7])
    # (x - num_a/2)^2 + (y - num_b/2)^2 = r_num / 4
    # x^2 - num_a x + num_a^2/4 + y^2 - num_b y + num_b^2/4 = R^2
    F_int = r.randint(-8, 4)
    rhs_num = num_a * num_a + num_b * num_b - 4 * F_int
    D = -num_a
    E = -num_b
    eq = f"x^2 + y^2 {'+' if D>0 else '-'} {abs(D)}x {'+' if E>0 else '-'} {abs(E)}y {'+' if F_int>=0 else '-'} {abs(F_int)} = 0"
    sa = "-" if num_a > 0 else "+"
    sb = "-" if num_b > 0 else "+"
    ans = f"\\text{{Centre}} = \\left(\\frac{{{num_a}}}{{2}}; \\frac{{{num_b}}}{{2}}\\right); \\quad r = \\frac{{\\sqrt{{{rhs_num}}}}}{{2}}"
    prompt = (
        f"By completing the square, find the centre and radius of the circle with equation:\n"
        f"$${eq}$$"
    )
    steps = [
        step(from_latex=eq, to_latex_str=f"\\left(x {sa} \\frac{{{abs(num_a)}}}{{2}}\\right)^2 + \\left(y {sb} \\frac{{{abs(num_b)}}}{{2}}\\right)^2 = {-F_int} + \\frac{{{num_a*num_a}}}{{4}} + \\frac{{{num_b*num_b}}}{{4}} = \\frac{{{rhs_num}}}{{4}}", op="Halve odd coefficients and add squares to both sides", rule="Fractional completing the square"),
        step(from_latex=f"r^2 = \\frac{{{rhs_num}}}{{4}}", to_latex_str=ans, op="Extract fractional centre and square-root RHS", rule="Centre and radius"),
    ]
    return _q("16_complete_square_odd_coefficients_fractional_centre", 16, prompt, ans, steps,
              f"Half of {D} is {D}/2, and its square is {num_a*num_a}/4.",
              "Add both fractional squares to the RHS over a common denominator of 4.",
              f"r^2 = {rhs_num}/4, so {ans}.",
              ["forgot_to_square_denominator_when_completing_square"], "hard", 4)


# 17. Finding unknown constant k in general circle equation given radius r
def build_17_unknown_constant_for_given_radius(r: random.Random) -> Dict[str, Any]:
    a = r.choice([-6, -5, -4, -3, -2, 2, 3, 4, 5, 6])
    b = r.choice([-6, -5, -4, -3, -2, 2, 3, 4, 5, 6])
    rad = r.randint(4, 11)
    r_sq = rad * rad
    k_val = a * a + b * b - r_sq
    D, E = -2 * a, -2 * b
    eq = f"x^2 + y^2 {'+' if D>0 else '-'} {abs(D)}x {'+' if E>0 else '-'} {abs(E)}y + k = 0"
    ans = f"k = {k_val}"
    prompt = (
        f"The circle with equation ${eq}$ has a radius of ${rad}$ units.\n\n"
        f"Determine the numerical value of $k$."
    )
    steps = [
        step(from_latex=eq, to_latex_str=f"{_fmt_shift('x', a)} + {_fmt_shift('y', b)} = {a*a} + {b*b} - k = {a*a + b*b} - k", op="Complete the square in terms of k", rule="r^2 = a^2 + b^2 - k"),
        step(from_latex=f"{a*a + b*b} - k = {r_sq}", to_latex_str=ans, op=f"Equate r^2 to {rad}^2 = {r_sq} and solve for k", rule="Linear equation in k"),
    ]
    return _q("17_unknown_constant_for_given_radius", 17, prompt, ans, steps,
              f"Complete the square to express r^2 = {a*a} + {b*b} - k.",
              f"Since r = {rad}, set {a*a + b*b} - k = {r_sq}.",
              f"Solving {a*a + b*b} - k = {r_sq} gives k = {k_val}.",
              ["equated_r_squared_expression_to_r_instead_of_r_squared"], "medium", 3)


# 18. Condition on k for x^2 + y^2 + Dx + Ey + k = 0 to represent a real non-degenerate circle
def build_18_condition_for_valid_real_circle(r: random.Random) -> Dict[str, Any]:
    a = r.choice([-7, -6, -5, -4, -3, 3, 4, 5, 6, 7])
    b = r.choice([-7, -6, -5, -4, -3, 3, 4, 5, 6, 7])
    bound = a * a + b * b
    D, E = -2 * a, -2 * b
    eq = f"x^2 + y^2 {'+' if D>0 else '-'} {abs(D)}x {'+' if E>0 else '-'} {abs(E)}y + k = 0"
    ans = f"k < {bound}"
    prompt = (
        f"Consider the equation ${eq}$.\n\n"
        f"Determine the set of values of $k$ for which this equation represents a real circle with positive radius."
    )
    steps = [
        step(from_latex=eq, to_latex_str=f"r^2 = ({a})^2 + ({b})^2 - k = {bound} - k", op="Complete the square to find r^2 in terms of k", rule="r^2 = a^2 + b^2 - k"),
        step(from_latex=f"r^2 > 0 \\implies {bound} - k > 0", to_latex_str=ans, op="Require strictly positive squared radius r^2 > 0", rule="Existence of real circle"),
    ]
    return _q("18_condition_for_valid_real_circle", 18, prompt, ans, steps,
              "For a real circle to exist, the right-hand side r^2 must be strictly greater than 0.",
              f"Complete the square: r^2 = {bound} - k > 0.",
              f"Therefore {ans}.",
              ["used_greater_than_instead_of_less_than_for_k"], "medium", 3)


# 19. Translation of a circle by horizontal and vertical shifts
def build_19_circle_translation_transformation(r: random.Random) -> Dict[str, Any]:
    a = r.randint(-5, 5)
    b = r.randint(-5, 5)
    rad = r.randint(3, 9)
    r_sq = rad * rad
    dx = r.choice([-6, -5, -4, -3, 3, 4, 5, 6])
    dy = r.choice([-6, -5, -4, -3, 3, 4, 5, 6])
    na, nb = a + dx, b + dy
    dir_x = f"{abs(dx)} units to the right" if dx > 0 else f"{abs(dx)} units to the left"
    dir_y = f"{abs(dy)} units upwards" if dy > 0 else f"{abs(dy)} units downwards"
    old_eq = f"{_fmt_shift('x', a)} + {_fmt_shift('y', b)} = {r_sq}"
    new_eq = f"{_fmt_shift('x', na)} + {_fmt_shift('y', nb)} = {r_sq}"
    ans = f"M'({na}; {nb}); \\quad {new_eq}"
    prompt = (
        f"A circle with equation ${old_eq}$ is translated {dir_x} and {dir_y}.\n\n"
        f"Write down the coordinates of the new centre $M'$ and the equation of the translated circle."
    )
    steps = [
        step(from_latex=f"M({a}; {b})", to_latex_str=f"M'({a} + ({dx}); {b} + ({dy})) = M'({na}; {nb})", op="Translate the centre coordinates (a; b)", rule="(x; y) -> (x + dx; y + dy)"),
        step(from_latex=f"M'({na}; {nb}),\\; r^2 = {r_sq}", to_latex_str=new_eq, op="Write equation with unchanged radius", rule="Rigid translation preserves radius"),
    ]
    return _q("19_circle_translation_transformation", 19, prompt, ans, steps,
              "First extract the original centre M(a; b), apply the shift to the point M, and then write the new equation.",
              "Translation changes the centre coordinates but leaves the radius r unchanged.",
              f"New centre M'({na}; {nb}), giving {new_eq}.",
              ["applied_shift_with_wrong_sign_directly_to_bracket"], "medium", 3)


# 20. Reflection of a circle across x-axis, y-axis, or y = x
def build_20_circle_reflection_transformation(r: random.Random) -> Dict[str, Any]:
    a = r.choice([-8, -7, -5, -4, -3, 3, 4, 5, 7, 8])
    b = r.choice([-9, -6, -5, -3, -2, 2, 3, 5, 6, 9])
    rad = r.randint(2, 10)
    r_sq = rad * rad
    kind = r.choice(["x_axis", "y_axis", "y_eq_x"])
    if kind == "x_axis":
        desc = "the horizontal axis ($y = 0$)"
        na, nb = a, -b
    elif kind == "y_axis":
        desc = "the vertical axis ($x = 0$)"
        na, nb = -a, b
    else:
        desc = "the line $y = x$"
        na, nb = b, a
    old_eq = f"{_fmt_shift('x', a)} + {_fmt_shift('y', b)} = {r_sq}"
    new_eq = f"{_fmt_shift('x', na)} + {_fmt_shift('y', nb)} = {r_sq}"
    ans = f"M'({na}; {nb}); \\quad {new_eq}"
    prompt = (
        f"The circle ${old_eq}$ is reflected across {desc}.\n\n"
        f"Determine the coordinates of the reflected centre $M'$ and the equation of the reflected circle."
    )
    steps = [
        step(from_latex=f"M({a}; {b})", to_latex_str=f"M'({na}; {nb})", op=f"Reflect centre M across {desc}", rule="Coordinate reflection rule"),
        step(from_latex=f"M'({na}; {nb}),\\; r^2 = {r_sq}", to_latex_str=new_eq, op="Write standard circle equation with radius r", rule="Isometry preserves radius"),
    ]
    return _q("20_circle_reflection_transformation", 20, prompt, ans, steps,
              f"Find the centre M({a}; {b}) first, reflect M across {desc}, and substitute into standard form.",
              "Reflection is an isometry, so the radius squared remains unchanged.",
              f"M'({na}; {nb}) and {new_eq}.",
              ["sign_inversion_of_center"], "easy", 3)


# 21. Circle touching the x-axis or y-axis (tangent to coordinate axis)
def build_21_circle_tangent_to_coordinate_axis(r: random.Random) -> Dict[str, Any]:
    a = r.choice([-8, -7, -6, -5, -4, -3, 3, 4, 5, 6, 7, 8])
    b = r.choice([-9, -7, -6, -5, -4, -3, 3, 4, 5, 6, 7, 9])
    touch_x = r.choice([True, False])
    if touch_x:
        axis_desc = "touches the line $y = 0$ (the horizontal coordinate axis)"
        rad = abs(b)
        pt = f"({a}; 0)"
    else:
        axis_desc = "touches the line $x = 0$ (the vertical coordinate axis)"
        rad = abs(a)
        pt = f"(0; {b})"
    r_sq = rad * rad
    eq = f"{_fmt_shift('x', a)} + {_fmt_shift('y', b)} = {r_sq}"
    ans = f"{eq}; \\quad \\text{{Point of contact}} = {pt}"
    prompt = (
        f"A circle has centre $M({a}; {b})$ and {axis_desc}.\n\n"
        f"Determine the standard equation of the circle and the coordinates of the point of contact."
    )
    steps = [
        step(from_latex=f"M({a}; {b})", to_latex_str=f"r = {rad},\\quad r^2 = {r_sq}", op="Distance from centre to tangent coordinate axis gives radius r", rule="Radius perpendicular to tangent axis"),
        step(from_latex=f"r^2 = {r_sq}", to_latex_str=ans, op="Write circle equation and point of contact", rule="(x - a)^2 + (y - b)^2 = r^2"),
    ]
    return _q("21_circle_tangent_to_coordinate_axis", 21, prompt, ans, steps,
              "Draw a quick mental sketch: the perpendicular distance from M(a; b) to y = 0 is |b|, and to x = 0 is |a|.",
              "Since the axis is tangent to the circle, the radius is perpendicular to that axis.",
              f"r = {rad}, so {ans}.",
              ["used_wrong_coordinate_as_radius_for_axis_tangency"], "medium", 3)


# 22. Coordinate circle SVG diagram with shifted centre M(a; b) and point P(x1; y1)
def build_22_shifted_circle_svg_diagram_equation(r: random.Random) -> Dict[str, Any]:
    a = r.choice([2, 3, 4, 5]) * r.choice([-1, 1])
    b = r.choice([2, 3, 4, 5]) * r.choice([-1, 1])
    dx, dy = r.choice([(3, 4), (4, 3), (5, 12), (6, 8)])
    px, py = a + dx, b + dy
    r_sq = dx * dx + dy * dy
    rad = int(math.isqrt(r_sq))
    cx_svg = 165 + a * 6
    cy_svg = 120 - b * 6
    rad_svg = 48 + (rad % 15)
    svg = (
        f'<svg viewBox="0 0 340 240" xmlns="http://www.w3.org/2000/svg">'
        f'<rect x="0" y="0" width="340" height="240" fill="#f8fafc" rx="8"/>'
        f'<line x1="20" y1="120" x2="320" y2="120" stroke="#94a3b8" stroke-width="1.5"/>'
        f'<line x1="165" y1="15" x2="165" y2="225" stroke="#94a3b8" stroke-width="1.5"/>'
        f'<circle cx="{cx_svg}" cy="{cy_svg}" r="{rad_svg}" fill="none" stroke="#1d4ed8" stroke-width="2.5"/>'
        f'<circle cx="{cx_svg}" cy="{cy_svg}" r="4" fill="#1e293b"/>'
        f'<text x="{cx_svg - 28}" y="{cy_svg + 16}" font-size="11" font-family="sans-serif" fill="#0f172a">M({a}; {b})</text>'
        f'<line x1="{cx_svg}" y1="{cy_svg}" x2="{cx_svg + int(rad_svg*0.8)}" y2="{cy_svg - int(rad_svg*0.6)}" stroke="#dc2626" stroke-width="2" stroke-dasharray="4,3"/>'
        f'<circle cx="{cx_svg + int(rad_svg*0.8)}" cy="{cy_svg - int(rad_svg*0.6)}" r="4" fill="#dc2626"/>'
        f'<text x="{cx_svg + int(rad_svg*0.8) + 6}" y="{cy_svg - int(rad_svg*0.6) - 4}" font-size="11" font-family="sans-serif" fill="#0f172a">P({px}; {py})</text>'
        f'</svg>'
    )
    eq = f"{_fmt_shift('x', a)} + {_fmt_shift('y', b)} = {r_sq}"
    ans = f"r = {rad}\\text{{ units}}; \\quad {eq}"
    prompt = (
        f"Refer to the coordinate diagram of the circle with centre $M({a}; {b})$ "
        f"passing through $P({px}; {py})$.\n\n"
        f"Calculate the length of the radius $MP$ and write down the equation of the circle in standard form."
    )
    steps = [
        step(from_latex=f"MP^2 = ({px} - ({a}))^2 + ({py} - ({b}))^2", to_latex_str=f"MP^2 = {dx}^2 + {dy}^2 = {r_sq} \\implies r = {rad}", op="Calculate radius MP using distance formula", rule="Distance formula"),
        step(from_latex=f"M({a}; {b}),\\; r^2 = {r_sq}", to_latex_str=eq, op="Write standard circle equation", rule="(x - a)^2 + (y - b)^2 = r^2"),
    ]
    return _q("22_shifted_circle_svg_diagram_equation", 22, prompt, ans, steps,
              f"Calculate MP^2 = ({px} - ({a}))^2 + ({py} - ({b}))^2.",
              "Substitute M(a; b) and r^2 into (x - a)^2 + (y - b)^2 = r^2.",
              f"r = {rad} and {eq}.",
              ["sign_inversion_of_center"], "easy", 3, _svg_spec(svg))


# 23. Intercepts of a circle (x - a)^2 + (y - b)^2 = r^2 with the coordinate axes
def build_23_circle_coordinate_axis_intercepts(r: random.Random) -> Dict[str, Any]:
    a = r.randint(-5, 5)
    dy = r.choice([3, 4, 5, 6, 7])
    b = r.choice([2, 3, 4]) * r.choice([-1, 1])
    # x-intercepts when y = 0: (x - a)^2 + b^2 = r^2 => choose r^2 = dy^2 + b^2 so x - a = +- dy
    r_sq = dy * dy + b * b
    x1, x2 = a - dy, a + dy
    eq = f"{_fmt_shift('x', a)} + {_fmt_shift('y', b)} = {r_sq}"
    ans = f"({x1}; 0) \\text{{ and }} ({x2}; 0)"
    prompt = (
        f"A circle is given by the equation ${eq}$.\n\n"
        f"Determine the coordinates of the horizontal axis intercepts (where $y = 0$)."
    )
    steps = [
        step(from_latex=f"y = 0 \\implies {_fmt_shift('x', a)} + (0 - ({b}))^2 = {r_sq}", to_latex_str=f"{_fmt_shift('x', a)} = {r_sq} - {b*b} = {dy*dy}", op="Substitute y = 0 into circle equation", rule="x-intercept condition y = 0"),
        step(from_latex=f"x - ({a}) = \\pm {dy}", to_latex_str=ans, op="Take both square roots and solve for x", rule="Two x-intercepts"),
    ]
    return _q("23_circle_coordinate_axis_intercepts", 23, prompt, ans, steps,
              "Substitute y = 0 into the circle equation and solve for x.",
              f"Remember to take both +sqrt({dy*dy}) and -sqrt({dy*dy}).",
              f"x = {a} +- {dy}, giving ({x1}; 0) and ({x2}; 0).",
              ["lost_negative_square_root_finding_circle_intercepts"], "medium", 3)


# 24. Concentric circles: finding equation of a second circle with same centre
def build_24_concentric_circle_equation(r: random.Random) -> Dict[str, Any]:
    a = r.choice([-6, -5, -4, -3, 2, 3, 4, 5, 6])
    b = r.choice([-6, -5, -4, -3, 2, 3, 4, 5, 6])
    r1 = r.randint(3, 6)
    gen_eq = _fmt_general_circle(a, b, r1 * r1)
    dx = r.choice([2, 3, 4, 5, 7])
    dy = r.choice([3, 4, 5, 6, 8])
    px, py = a + dx, b + dy
    r2_sq = dx * dx + dy * dy
    ans = f"{_fmt_shift('x', a)} + {_fmt_shift('y', b)} = {r2_sq}"
    prompt = (
        f"A circle $C_2$ is concentric with the circle $C_1: {gen_eq}$ "
        f"and passes through the point $P({px}; {py})$.\n\n"
        f"Determine the equation of circle $C_2$ in standard form."
    )
    steps = [
        step(from_latex=gen_eq, to_latex_str=f"M({a}; {b})", op="Complete the square on C1 to find the shared centre M", rule="Concentric circles share the same centre"),
        step(from_latex=f"r_2^2 = ({px} - ({a}))^2 + ({py} - ({b}))^2 = {r2_sq}", to_latex_str=ans, op="Compute r2^2 using P and write standard equation", rule="(x - a)^2 + (y - b)^2 = r_2^2"),
    ]
    return _q("24_concentric_circle_equation", 24, prompt, ans, steps,
              "Concentric circles have the exact same centre M(a; b).",
              f"Find the centre M({a}; {b}) from C1, then compute the squared distance MP^2.",
              f"Shared centre M({a}; {b}) and r_2^2 = {r2_sq} give {ans}.",
              ["reused_radius_of_first_circle_instead_of_centre"], "medium", 4)


# 25. Circle with centre on a given line y = mx + c passing through two given points
def build_25_circle_centre_on_line_through_two_points(r: random.Random) -> Dict[str, Any]:
    # Choose centre M(a; b) where b = m*a + c, and points A(a + dx; b + dy), B(a - dy; b + dx) so MA^2 = MB^2
    a = r.randint(-4, 4)
    m = r.choice([1, 2, -1, -2])
    c = r.randint(-5, 5)
    b = m * a + c
    dx = r.choice([2, 3, 4, 5])
    dy = r.choice([1, 2, 3, 4])
    if dx == dy:
        dy += 1
    ax, ay = a + dx, b + dy
    bx, by = a - dy, b + dx
    r_sq = dx * dx + dy * dy
    line_str = f"y = {m}x {'+' if c >= 0 else '-'} {abs(c)}" if abs(m) != 1 else (f"y = {'x' if m==1 else '-x'} {'+' if c >= 0 else '-'} {abs(c)}")
    ans = f"M({a}; {b}); \\quad {_fmt_shift('x', a)} + {_fmt_shift('y', b)} = {r_sq}"
    prompt = (
        f"A circle passes through the points $A({ax}; {ay})$ and $B({bx}; {by})$. "
        f"Its centre $M(a; b)$ lies on the line ${line_str}$.\n\n"
        f"Use $MA^2 = MB^2$ to find the coordinates of $M$ and the standard equation of the circle."
    )
    steps = [
        step(from_latex=f"b = {m}a + ({c}),\\quad MA^2 = MB^2", to_latex_str=f"(a - ({ax}))^2 + (b - ({ay}))^2 = (a - ({bx}))^2 + (b - ({by}))^2", op="Equate squared radii MA^2 = MB^2", rule="Equidistant centre"),
        step(from_latex=f"b = {m}a + ({c})", to_latex_str=f"a = {a},\\; b = {b},\\; r^2 = {r_sq}", op="Substitute b in terms of a and solve linear equation", rule="Simultaneous solution"),
        step(from_latex=f"M({a}; {b}),\\; r^2 = {r_sq}", to_latex_str=ans, op="State standard circle equation", rule="(x - a)^2 + (y - b)^2 = r^2"),
    ]
    return _q("25_circle_centre_on_line_through_two_points", 25, prompt, ans, steps,
              "Equate MA^2 = MB^2; the a^2 and b^2 terms cancel out to leave a linear relation between a and b.",
              f"Solve simultaneously with b = {m}a + ({c}) to find M(a; b).",
              f"M({a}; {b}) and r^2 = {r_sq}.",
              ["algebraic_sign_error_expanding_equidistant_condition"], "hard", 5)


BUILDERS_01_25: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    "01_origin_circle_equation_from_radius": build_01_origin_circle_equation_from_radius,
    "02_origin_circle_equation_from_surd_radius": build_02_origin_circle_equation_from_surd_radius,
    "03_origin_circle_radius_from_equation": build_03_origin_circle_radius_from_equation,
    "04_origin_circle_passing_through_point": build_04_origin_circle_passing_through_point,
    "05_origin_circle_unknown_coordinate": build_05_origin_circle_unknown_coordinate,
    "06_point_position_relative_to_origin_circle": build_06_point_position_relative_to_origin_circle,
    "07_origin_circle_symmetry_and_reflections": build_07_origin_circle_symmetry_and_reflections,
    "08_origin_circle_svg_coordinate_diagram": build_08_origin_circle_svg_coordinate_diagram,
    "09_standard_circle_equation_from_centre_and_radius": build_09_standard_circle_equation_from_centre_and_radius,
    "10_read_centre_and_radius_from_standard_form": build_10_read_centre_and_radius_from_standard_form,
    "11_circle_equation_from_centre_and_point": build_11_circle_equation_from_centre_and_point,
    "12_circle_equation_from_diameter_endpoints": build_12_circle_equation_from_diameter_endpoints,
    "13_expand_standard_to_general_form": build_13_expand_standard_to_general_form,
    "14_complete_square_even_coefficients": build_14_complete_square_even_coefficients,
    "15_complete_square_non_unit_leading_coefficient": build_15_complete_square_non_unit_leading_coefficient,
    "16_complete_square_odd_coefficients_fractional_centre": build_16_complete_square_odd_coefficients_fractional_centre,
    "17_unknown_constant_for_given_radius": build_17_unknown_constant_for_given_radius,
    "18_condition_for_valid_real_circle": build_18_condition_for_valid_real_circle,
    "19_circle_translation_transformation": build_19_circle_translation_transformation,
    "20_circle_reflection_transformation": build_20_circle_reflection_transformation,
    "21_circle_tangent_to_coordinate_axis": build_21_circle_tangent_to_coordinate_axis,
    "22_shifted_circle_svg_diagram_equation": build_22_shifted_circle_svg_diagram_equation,
    "23_circle_coordinate_axis_intercepts": build_23_circle_coordinate_axis_intercepts,
    "24_concentric_circle_equation": build_24_concentric_circle_equation,
    "25_circle_centre_on_line_through_two_points": build_25_circle_centre_on_line_through_two_points,
}
