"""Grade 10 Mathematics — Term 1 — Trigonometry (deterministic, SymPy-backed).

Curriculum source: ``curriculum_docs/Mathematics_Gr10/Term 1/5 Trigonometry.md``
(every ``DIAGRAM[...]`` is a right-angled triangle or a Cartesian point — both are
emitted here as a structured **Diagram Spec**, never an image).

Subskills (archetypes — SymPy computes the answers, so variety is unlimited):

    identify_sides     diagram_select  click the hypotenuse/opposite/adjacent
    ratio_from_triangle math_short     sin/cos/tan θ from a labelled triangle
    calculator_value   math_short      evaluate sin/cos/tan of an angle (2 d.p.)
    special_angles     math_short      exact surd value for 30°/45°/60°
    find_length        math_short      solve for a side using a ratio (2 d.p.)
    find_angle         math_short      solve for an angle from two sides (1 d.p.)
    solve_equation     math_short      solve e.g. cos θ = 0,2 for θ (2 d.p.)

All answers are computed; given a seed the output is byte-identical.
"""
from __future__ import annotations

from typing import Any, Dict, List, Tuple

import sympy as sp

from app.utils.grade10_mathematics import _diagram
from app.utils.grade10_mathematics._math_common import (
    build_generate,
    make_diagram_select,
    make_short,
    num,
    solution,
    step,
    to_latex_safe,
    with_metadata,
)

TOPIC = "grade10_math_trigonometry"
LO = "math10_trigonometry"

# Pythagorean triples (opposite, adjacent, hypotenuse) for exact ratios.
_TRIPLES: List[Tuple[int, int, int]] = [
    (3, 4, 5), (4, 3, 5), (5, 12, 13), (12, 5, 13),
    (8, 15, 17), (15, 8, 17), (6, 8, 10), (24, 7, 25),
]

_FUNCS = {"sin": sp.sin, "cos": sp.cos, "tan": sp.tan}


def _deg_latex(angle: int) -> str:
    return f"{angle}^{{\\circ}}"


def _round2(value: sp.Expr) -> sp.Rational:
    return sp.Rational(str(round(float(value), 2)))


# --------------------------------------------------------------------------- #
# identify_sides  (interactive diagram: click a side)
# --------------------------------------------------------------------------- #
def _build_identify_sides(r, difficulty: str) -> Dict[str, Any]:
    target_role = r.choice(["hypotenuse", "opposite", "adjacent"])
    labels = ["a", "b", "c"]
    r.shuffle(labels)
    # labels[0]->AB(adjacent), labels[1]->BC(opposite), labels[2]->AC(hypotenuse)
    spec = _diagram.right_triangle(
        adjacent=labels[0],
        opposite=labels[1],
        hypotenuse=labels[2],
        angle_label="θ",
        caption="Right-angled triangle. Click a side.",
    )
    correct_edge = _diagram.ROLE_EDGE[target_role]
    correct_label = {"AB": labels[0], "BC": labels[1], "AC": labels[2]}[correct_edge]
    q = make_diagram_select(
        prefix=TOPIC,
        prompt=f"With respect to angle θ, click the {target_role} side.",
        target=target_role,
        correct_edge=correct_edge,
        marks=1,
        explanation=(
            f"The {target_role} side is "
            + {
                "hypotenuse": "always opposite the right angle (the longest side)",
                "opposite": "across from angle θ",
                "adjacent": "next to angle θ (and not the hypotenuse)",
            }[target_role]
            + f". Here that is side {correct_label}."
        ),
        hint="The hypotenuse is opposite the right angle; the opposite side faces θ.",
    )
    return with_metadata(
        q,
        topic=TOPIC,
        subskill="identify_sides",
        learning_objective_id=f"{LO}.identify_sides",
        misconception_tags=["confuses_opposite_adjacent", "picks_hypotenuse_for_opposite"],
        diagnostic_tags=["trig_ratios", "side_identification"],
        keywords=["opposite", "adjacent", "hypotenuse", "SohCahToa"],
        diagram_spec=spec,
    )


# --------------------------------------------------------------------------- #
# ratio_from_triangle
# --------------------------------------------------------------------------- #
def _build_ratio_from_triangle(r, difficulty: str) -> Dict[str, Any]:
    opp, adj, hyp = r.choice(_TRIPLES)
    func = r.choice(["sin", "cos", "tan"])
    ratio = {"sin": sp.Rational(opp, hyp), "cos": sp.Rational(adj, hyp), "tan": sp.Rational(opp, adj)}[func]
    formula = {"sin": "\\frac{\\text{opp}}{\\text{hyp}}", "cos": "\\frac{\\text{adj}}{\\text{hyp}}", "tan": "\\frac{\\text{opp}}{\\text{adj}}"}[func]
    spec = _diagram.right_triangle(
        adjacent=str(adj), opposite=str(opp), hypotenuse=str(hyp), angle_label="θ",
    )
    sol = solution(
        goal=f"find {func} θ",
        chain_type="expression",
        var="x",
        steps=[
            step(from_expr=None, to_expr=None, op="apply the definition", rule="SohCahToa",
                 from_latex=f"\\{func}\\,θ = {formula}", to_latex=f"\\{func}\\,θ = {to_latex_safe(ratio)}"),
        ],
        final_expr=ratio,
    )
    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Use the triangle to write }} \\{func}\\,θ \\text{{ as a fraction in simplest form.}}",
        answer_expr=ratio,
        answer_mode="value",
        marks=1,
        canonical_solution=sol,
        explanation=f"{func} θ = {formula} = {to_latex_safe(ratio)}.",
        hint="Identify the opposite, adjacent and hypotenuse relative to θ, then apply SohCahToa.",
    )
    return with_metadata(
        q,
        topic=TOPIC,
        subskill="ratio_from_triangle",
        learning_objective_id=f"{LO}.ratio_from_triangle",
        misconception_tags=["swaps_opposite_adjacent", "uses_wrong_ratio"],
        diagnostic_tags=["trig_ratios", "soh_cah_toa"],
        keywords=["sin", "cos", "tan", "ratio", "triangle"],
        diagram_spec=spec,
    )


# --------------------------------------------------------------------------- #
# calculator_value
# --------------------------------------------------------------------------- #
def _build_calculator_value(r, difficulty: str) -> Dict[str, Any]:
    func = r.choice(["sin", "cos", "tan"])
    angle = r.choice([12, 26, 34, 38, 40, 48, 49, 65, 74])
    coeff = r.choice([1, 1, 2, 3])
    value = coeff * _FUNCS[func](sp.rad(angle))
    rounded = _round2(value)
    prefix_latex = "" if coeff == 1 else f"{coeff}\\,"
    sol = solution(
        goal="evaluate with a calculator",
        chain_type="expression",
        var="x",
        steps=[
            step(from_expr=None, to_expr=None, op="set calculator to degrees, then evaluate", rule="calculator",
                 from_latex=f"{prefix_latex}\\{func} {_deg_latex(angle)}",
                 to_latex=f"{prefix_latex}\\{func} {_deg_latex(angle)} = {num(rounded, 2)}"),
        ],
        final_expr=None,
        final_latex=num(rounded, 2),
    )
    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Evaluate (2 decimal places): }} {prefix_latex}\\{func} {_deg_latex(angle)}",
        answer_expr=rounded,
        answer_mode="value",
        marks=1,
        canonical_solution=sol,
        answer_latex=num(rounded, 2),
        explanation="Make sure your calculator is in degrees mode before evaluating.",
        hint="Check that your calculator is set to DEG, not RAD.",
    )
    return with_metadata(
        q,
        topic=TOPIC,
        subskill="calculator_value",
        learning_objective_id=f"{LO}.calculator_value",
        misconception_tags=["calculator_in_radians", "rounding_error"],
        diagnostic_tags=["calculator_skills"],
        keywords=["calculator", "degrees", "evaluate"],
    )


# --------------------------------------------------------------------------- #
# special_angles  (no calculator — exact surd value)
# --------------------------------------------------------------------------- #
def _build_special_angles(r, difficulty: str) -> Dict[str, Any]:
    func = r.choice(["sin", "cos", "tan"])
    angle = r.choice([30, 45, 60])
    exact = sp.nsimplify(_FUNCS[func](sp.rad(angle)), rational=False)
    exact = sp.radsimp(sp.simplify(exact))
    sol = solution(
        goal="recall the special-angle value",
        chain_type="expression",
        var="x",
        steps=[
            step(from_expr=None, to_expr=None, op="read from the special-angle triangle", rule="special angles",
                 from_latex=f"\\{func} {_deg_latex(angle)}", to_latex=f"\\{func} {_deg_latex(angle)} = {to_latex_safe(exact)}"),
        ],
        final_expr=exact,
    )
    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Without a calculator, give the exact value of }} \\{func} {_deg_latex(angle)}.",
        answer_expr=exact,
        answer_mode="value",
        marks=1,
        canonical_solution=sol,
        explanation="Use the 30°–60°–90° and 45°–45°–90° triangles to read off exact values.",
        hint="Draw the special triangle and apply SohCahToa with surds.",
    )
    return with_metadata(
        q,
        topic=TOPIC,
        subskill="special_angles",
        learning_objective_id=f"{LO}.special_angles",
        misconception_tags=["mixes_special_values", "decimalises_surd"],
        diagnostic_tags=["special_angles", "surds"],
        keywords=["special angles", "exact value", "surd", "30", "45", "60"],
    )


# --------------------------------------------------------------------------- #
# find_length
# --------------------------------------------------------------------------- #
def _build_find_length(r, difficulty: str) -> Dict[str, Any]:
    angle = r.choice([22, 25, 30, 37, 49, 50, 55])
    known = r.randint(6, 40)
    case = r.choice(["opp_from_hyp", "adj_from_hyp", "opp_from_adj"])
    if case == "opp_from_hyp":
        func, formula = "sin", "\\frac{\\text{opp}}{\\text{hyp}}"
        value = known * sp.sin(sp.rad(angle))
        eq_latex = f"\\sin {_deg_latex(angle)} = \\dfrac{{x}}{{{known}}}"
        rearr = f"x = {known} \\sin {_deg_latex(angle)}"
        spec = _diagram.right_triangle(hypotenuse=str(known), opposite="x", angle_label=f"{angle}°")
    elif case == "adj_from_hyp":
        func, formula = "cos", "\\frac{\\text{adj}}{\\text{hyp}}"
        value = known * sp.cos(sp.rad(angle))
        eq_latex = f"\\cos {_deg_latex(angle)} = \\dfrac{{x}}{{{known}}}"
        rearr = f"x = {known} \\cos {_deg_latex(angle)}"
        spec = _diagram.right_triangle(hypotenuse=str(known), adjacent="x", angle_label=f"{angle}°")
    else:
        func, formula = "tan", "\\frac{\\text{opp}}{\\text{adj}}"
        value = known * sp.tan(sp.rad(angle))
        eq_latex = f"\\tan {_deg_latex(angle)} = \\dfrac{{x}}{{{known}}}"
        rearr = f"x = {known} \\tan {_deg_latex(angle)}"
        spec = _diagram.right_triangle(adjacent=str(known), opposite="x", angle_label=f"{angle}°")
    rounded = _round2(value)
    sol = solution(
        goal="solve for x",
        chain_type="expression",
        var="x",
        steps=[
            step(from_expr=None, to_expr=None, op="choose the ratio with the known and unknown sides", rule="SohCahToa",
                 from_latex=f"\\{func}\\,θ = {formula}", to_latex=eq_latex),
            step(from_expr=None, to_expr=None, op="make x the subject", rule="rearrange",
                 from_latex=eq_latex, to_latex=rearr),
            step(from_expr=None, to_expr=None, op="evaluate (degrees mode)", rule="calculator",
                 from_latex=rearr, to_latex=f"x = {num(rounded, 2)}"),
        ],
        final_expr=None,
        final_latex=f"x = {num(rounded, 2)}",
    )
    q = make_short(
        prefix=TOPIC,
        prompt_latex="\\text{Find the length of } x \\text{ (2 decimal places).}",
        answer_expr=rounded,
        answer_mode="value",
        marks=2,
        canonical_solution=sol,
        answer_latex=num(rounded, 2),
        explanation="Pick the ratio relating the known side and x, rearrange, then evaluate.",
        hint="Which ratio uses the side you know and the side you want?",
    )
    return with_metadata(
        q,
        topic=TOPIC,
        subskill="find_length",
        learning_objective_id=f"{LO}.find_length",
        misconception_tags=["wrong_ratio_choice", "forgot_to_rearrange", "calculator_in_radians"],
        diagnostic_tags=["solving_triangles", "find_length"],
        keywords=["find length", "trig ratio", "solve"],
        diagram_spec=spec,
    )


# --------------------------------------------------------------------------- #
# find_angle
# --------------------------------------------------------------------------- #
def _build_find_angle(r, difficulty: str) -> Dict[str, Any]:
    opp, adj, hyp = r.choice(_TRIPLES)
    case = r.choice(["from_opp_adj", "from_opp_hyp", "from_adj_hyp"])
    if case == "from_opp_adj":
        func, inv = "tan", sp.atan(sp.Rational(opp, adj))
        frac_latex = f"\\dfrac{{{opp}}}{{{adj}}}"
        spec = _diagram.right_triangle(opposite=str(opp), adjacent=str(adj), angle_label="θ")
    elif case == "from_opp_hyp":
        func, inv = "sin", sp.asin(sp.Rational(opp, hyp))
        frac_latex = f"\\dfrac{{{opp}}}{{{hyp}}}"
        spec = _diagram.right_triangle(opposite=str(opp), hypotenuse=str(hyp), angle_label="θ")
    else:
        func, inv = "cos", sp.acos(sp.Rational(adj, hyp))
        frac_latex = f"\\dfrac{{{adj}}}{{{hyp}}}"
        spec = _diagram.right_triangle(adjacent=str(adj), hypotenuse=str(hyp), angle_label="θ")
    ratio_latex = f"\\{func} θ = {frac_latex}"
    angle_deg = sp.deg(inv)
    rounded = sp.Rational(str(round(float(angle_deg), 1)))
    inv_name = {"sin": "\\sin^{-1}", "cos": "\\cos^{-1}", "tan": "\\tan^{-1}"}[func]
    sol = solution(
        goal="solve for θ",
        chain_type="expression",
        var="x",
        steps=[
            step(from_expr=None, to_expr=None, op="write the ratio for θ", rule="SohCahToa",
                 from_latex="θ = ?", to_latex=ratio_latex),
            step(from_expr=None, to_expr=None, op="apply the inverse function", rule="inverse trig",
                 from_latex=ratio_latex, to_latex=f"θ = {inv_name}\\left({frac_latex}\\right)"),
            step(from_expr=None, to_expr=None, op="evaluate (degrees mode)", rule="calculator",
                 from_latex=f"θ = {inv_name}(\\ldots)", to_latex=f"θ = {num(rounded, 1)}{{}}^{{\\circ}}"),
        ],
        final_expr=None,
        final_latex=f"θ = {num(rounded, 1)}^{{\\circ}}",
    )
    q = make_short(
        prefix=TOPIC,
        prompt_latex="\\text{Find the size of angle } θ \\text{ (1 decimal place).}",
        answer_expr=rounded,
        answer_mode="value",
        marks=2,
        canonical_solution=sol,
        answer_latex=num(rounded, 1),
        explanation="Form the ratio for θ, then use the inverse trig function on your calculator.",
        hint="Use sin⁻¹, cos⁻¹ or tan⁻¹ (SHIFT) to get the angle from the ratio.",
    )
    return with_metadata(
        q,
        topic=TOPIC,
        subskill="find_angle",
        learning_objective_id=f"{LO}.find_angle",
        misconception_tags=["forgot_inverse_function", "wrong_ratio_choice"],
        diagnostic_tags=["solving_triangles", "find_angle"],
        keywords=["find angle", "inverse trig", "solve"],
        diagram_spec=spec,
    )


# --------------------------------------------------------------------------- #
# solve_equation
# --------------------------------------------------------------------------- #
def _build_solve_equation(r, difficulty: str) -> Dict[str, Any]:
    func = r.choice(["sin", "cos", "tan"])
    if func == "tan":
        rhs = sp.Rational(str(round(r.uniform(0.3, 4.0), 2)))
        inv = sp.deg(sp.atan(rhs))
        inv_name = "\\tan^{-1}"
    else:
        rhs = sp.Rational(str(round(r.uniform(0.15, 0.95), 2)))
        inv = sp.deg(sp.asin(rhs) if func == "sin" else sp.acos(rhs))
        inv_name = "\\sin^{-1}" if func == "sin" else "\\cos^{-1}"
    rounded = sp.Rational(str(round(float(inv), 2)))
    sol = solution(
        goal="solve for θ",
        chain_type="expression",
        var="x",
        steps=[
            step(from_expr=None, to_expr=None, op="apply the inverse function", rule="inverse trig",
                 from_latex=f"\\{func} θ = {num(rhs, 2)}", to_latex=f"θ = {inv_name}({num(rhs, 2)})"),
            step(from_expr=None, to_expr=None, op="evaluate (degrees mode)", rule="calculator",
                 from_latex=f"θ = {inv_name}({num(rhs, 2)})", to_latex=f"θ = {num(rounded, 2)}{{}}^{{\\circ}}"),
        ],
        final_expr=None,
        final_latex=f"θ = {num(rounded, 2)}^{{\\circ}}",
    )
    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Solve for }} θ \\text{{ (2 decimal places): }} \\{func} θ = {num(rhs, 2)}",
        answer_expr=rounded,
        answer_mode="value",
        marks=1,
        canonical_solution=sol,
        answer_latex=num(rounded, 2),
        explanation="Isolate the trig ratio, then apply the inverse function.",
        hint="Use the inverse (SHIFT) function for the ratio given.",
    )
    return with_metadata(
        q,
        topic=TOPIC,
        subskill="solve_equation",
        learning_objective_id=f"{LO}.solve_equation",
        misconception_tags=["forgot_inverse_function", "calculator_in_radians"],
        diagnostic_tags=["trig_equations"],
        keywords=["solve", "trig equation", "inverse"],
    )


SUBSKILLS = {
    "identify_sides": _build_identify_sides,
    "ratio_from_triangle": _build_ratio_from_triangle,
    "calculator_value": _build_calculator_value,
    "special_angles": _build_special_angles,
    "find_length": _build_find_length,
    "find_angle": _build_find_angle,
    "solve_equation": _build_solve_equation,
    # default / mixed alias
    "concepts": _build_identify_sides,
}

generate = build_generate(SUBSKILLS, default_subskill="identify_sides")
