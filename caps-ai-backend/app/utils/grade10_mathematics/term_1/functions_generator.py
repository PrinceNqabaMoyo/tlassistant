"""Grade 10 Mathematics — Term 1 — Functions (deterministic, SymPy-backed).

Curriculum source: ``curriculum_docs/Mathematics_Gr10/Functions.md``.

Functions is the first Gr10 topic whose core object is a *graph*. The
deterministic discipline still holds: every graph is a **computed** artefact
(parameters drawn from a seeded RNG, SymPy computes intercepts / turning points
/ ranges), every figure is a structured **Diagram Spec** (``function_graph``)
rather than an image, and marking compares structured values — never pixels.

Subskills (archetypes — SymPy computes the answers, so variety is unlimited):

    function_notation_eval   math_short(value)   evaluate f(x) at a value
    function_notation_solve  math_short(value)   find input x given f(x)=k
    domain_range             mcq                 domain/range (set ↔ interval)
    representation_convert   math_short          words/table ↔ formula
    linear_gradient_intercept math_short(pair)   read m and c from y=mx+c
    linear_intercepts        math_short(pair)    x-/y-intercepts of a line
    linear_find_equation     math_short(expr)    y=mx+c from two points
    quadratic_effect         mcq                 effect of a (shape) and q (shift)
    quadratic_features       math_short          turning point / axis / y-intercept
    hyperbola_features       math_short/mcq      asymptotes & effect of a, q
    exponential_features     math_short/mcq      growth/decay & asymptote
    trig_graph_features      math_short/mcq      amplitude / period / range
    interpret_graph          math_short(pair)    read a point off a rendered graph
    match_equation_graph     mcq                 match an equation to its graph
    parameter_manipulation   function_transform  drag a/q sliders to match a target

All answers are computed; given a seed the output is byte-identical.
"""
from __future__ import annotations

from typing import Any, Dict, List

import sympy as sp

from app.utils.grade10_mathematics import _diagram
from app.utils.grade10_mathematics._math_common import (
    build_generate,
    make_function_transform,
    make_mcq,
    make_short,
    num,
    nonzero,
    solution,
    step,
    to_latex_safe,
    with_metadata,
)

TOPIC = "grade10_math_functions"
LO = "math10_functions"

X = sp.Symbol("x")


# --------------------------------------------------------------------------- #
# Small LaTeX / coordinate helpers
# --------------------------------------------------------------------------- #
def _coord(px: Any, py: Any) -> str:
    """Ordered pair in SA notation (``;`` separator, comma decimals)."""
    return f"\\left({num(px)};\\,{num(py)}\\right)"


def _linear_latex(m: int, c: int, name: str = "f") -> str:
    """LaTeX for f(x) = mx + c with tidy signs."""
    if m == 1:
        mx = "x"
    elif m == -1:
        mx = "-x"
    else:
        mx = f"{m}x"
    if c == 0:
        body = mx
    elif c > 0:
        body = f"{mx} + {c}"
    else:
        body = f"{mx} - {abs(c)}"
    return f"{name}(x) = {body}"


def _quadratic_latex(a: int, q: int, name: str = "f") -> str:
    if a == 1:
        ax = "x^2"
    elif a == -1:
        ax = "-x^2"
    else:
        ax = f"{a}x^2"
    if q == 0:
        body = ax
    elif q > 0:
        body = f"{ax} + {q}"
    else:
        body = f"{ax} - {abs(q)}"
    return f"{name}(x) = {body}"


def _signed(value: int) -> str:
    return f"+ {value}" if value >= 0 else f"- {abs(value)}"


# --------------------------------------------------------------------------- #
# function_notation_eval
# --------------------------------------------------------------------------- #
def _build_function_notation_eval(r, difficulty: str) -> Dict[str, Any]:
    name = r.choice(["f", "g", "h", "p"])
    kind = r.choice(["linear", "linear", "quadratic"])
    if kind == "linear":
        m = nonzero(r, -4, 5)
        c = r.randint(-6, 6)
        expr = m * X + c
        eq_latex = _linear_latex(m, c, name)
    else:
        a = nonzero(r, -3, 3)
        q = r.randint(-5, 5)
        expr = a * X ** 2 + q
        eq_latex = _quadratic_latex(a, q, name)
    inp = nonzero(r, -4, 4)
    value = sp.Integer(expr.subs(X, inp))
    # Show the formula with x textually replaced by the bracketed input value.
    body = eq_latex.split("=", 1)[1].strip()
    plugged = body.replace("x", f"({num(inp)})")
    sol = solution(
        goal="evaluate the function",
        chain_type="expression",
        var="x",
        steps=[
            step(from_expr=None, to_expr=None, op=f"substitute x = {num(inp)}", rule="function notation",
                 from_latex=f"{name}({num(inp)})",
                 to_latex=f"{name}({num(inp)}) = {plugged}"),
            step(from_expr=None, to_expr=None, op="simplify", rule="arithmetic",
                 from_latex=f"{name}({num(inp)}) = {plugged}", to_latex=f"{name}({num(inp)}) = {num(int(value))}"),
        ],
        final_expr=value,
        final_latex=num(int(value)),
    )
    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Given }} {eq_latex}\\text{{, calculate }} {name}({num(inp)}).",
        answer_expr=value,
        answer_mode="value",
        marks=2,
        canonical_solution=sol,
        explanation=f"Substitute x = {num(inp)} into the formula and simplify.",
        hint="Replace every x with the input value, then work out the arithmetic.",
    )
    return with_metadata(
        q, topic=TOPIC, subskill="function_notation_eval",
        learning_objective_id=f"{LO}.notation",
        misconception_tags=["arithmetic_sign_error", "forgets_order_of_operations"],
        diagnostic_tags=["function_notation", "evaluate"],
        keywords=["function notation", "evaluate", "f(x)", "substitute"],
    )


# --------------------------------------------------------------------------- #
# function_notation_solve  (find the input)
# --------------------------------------------------------------------------- #
def _build_function_notation_solve(r, difficulty: str) -> Dict[str, Any]:
    name = r.choice(["f", "g", "h"])
    m = nonzero(r, -4, 5)
    root = nonzero(r, -5, 6)
    c = r.randint(-6, 6)
    k = int((m * root + c))  # ensures an integer solution x = root
    expr = m * X + c
    eq = sp.Eq(expr, k)
    sol = solution(
        goal="find x",
        chain_type="equation",
        var="x",
        steps=[
            step(from_expr=eq, to_expr=sp.Eq(m * X, k - c), op=f"subtract {num(c)}", rule="additive inverse",
                 common_errors=["sign_error"]),
            step(from_expr=sp.Eq(m * X, k - c), to_expr=sp.Eq(X, sp.Integer(root)), op=f"divide by {num(m)}",
                 rule="multiplicative inverse", common_errors=["division_error"]),
        ],
        final_expr=sp.Integer(root),
        final_latex=f"x = {num(root)}",
    )
    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Given }} {_linear_latex(m, c, name)}\\text{{, find }} x \\text{{ if }} {name}(x) = {num(k)}.",
        answer_expr=sp.Integer(root),
        answer_mode="value",
        marks=2,
        canonical_solution=sol,
        explanation=f"Set the formula equal to {num(k)} and solve the equation for x.",
        hint="Write mx + c = k, then solve the linear equation.",
    )
    return with_metadata(
        q, topic=TOPIC, subskill="function_notation_solve",
        learning_objective_id=f"{LO}.notation",
        misconception_tags=["solves_for_y_not_x", "sign_error"],
        diagnostic_tags=["function_notation", "solve_input"],
        keywords=["function notation", "find input", "solve"],
    )


# --------------------------------------------------------------------------- #
# domain_range
# --------------------------------------------------------------------------- #
_REAL_SET = "\\{x: x \\in \\mathbb{R}\\}"
_REAL_SET_Y = "\\{y: y \\in \\mathbb{R}\\}"


def _build_domain_range(r, difficulty: str) -> Dict[str, Any]:
    family = r.choice(["linear", "quadratic", "hyperbola", "exponential"])
    ask = r.choice(["domain", "range"])
    a = nonzero(r, -3, 3)
    q = r.randint(-4, 4)

    if family == "linear":
        eq = _linear_latex(a, q)
        correct = _REAL_SET if ask == "domain" else _REAL_SET_Y
        distractors = [f"\\{{x: x > 0\\}}", f"[{num(q)};\\infty)", f"\\{{y: y \\neq {num(q)}\\}}"]
    elif family == "quadratic":
        eq = _quadratic_latex(a, q)
        if ask == "domain":
            correct = _REAL_SET
            distractors = [f"[{num(q)};\\infty)", f"\\{{x: x \\neq 0\\}}", f"(-\\infty;{num(q)}]"]
        else:
            correct = f"[{num(q)};\\infty)" if a > 0 else f"(-\\infty;{num(q)}]"
            distractors = [
                f"(-\\infty;{num(q)}]" if a > 0 else f"[{num(q)};\\infty)",
                _REAL_SET_Y,
                f"\\{{y: y \\neq {num(q)}\\}}",
            ]
    elif family == "hyperbola":
        eq = f"f(x) = \\dfrac{{{num(a)}}}{{x}} {_signed(q)}"
        if ask == "domain":
            correct = "\\{x: x \\in \\mathbb{R},\\, x \\neq 0\\}"
            distractors = [_REAL_SET, f"\\{{x: x \\neq {num(q)}\\}}", f"[{num(q)};\\infty)"]
        else:
            correct = f"\\{{y: y \\in \\mathbb{{R}},\\, y \\neq {num(q)}\\}}"
            distractors = [_REAL_SET_Y, "\\{y: y \\neq 0\\}", f"[{num(q)};\\infty)"]
    else:  # exponential
        b = r.choice([2, 3])
        eq = f"f(x) = {num(a)} \\cdot {b}^{{x}} {_signed(q)}"
        if ask == "domain":
            correct = _REAL_SET
            distractors = [f"\\{{x: x > 0\\}}", f"({num(q)};\\infty)", f"\\{{x: x \\neq 0\\}}"]
        else:
            correct = f"({num(q)};\\infty)" if a > 0 else f"(-\\infty;{num(q)})"
            distractors = [
                f"[{num(q)};\\infty)",
                _REAL_SET_Y,
                f"\\{{y: y \\neq {num(q)}\\}}",
            ]

    options = [correct] + distractors
    r.shuffle(options)
    correct_index = options.index(correct)
    q_obj = make_mcq(
        prefix=TOPIC,
        prompt=f"Write down the {ask} of the function.",
        prompt_latex=f"\\text{{Write down the {ask} of }} {eq}.",
        options=[f"option {i+1}" for i in range(len(options))],
        options_latex=options,
        correct_index=correct_index,
        explanation=f"The {ask} is {correct.replace(chr(92), '')}.",
        hint="Linear: all reals. Quadratic range depends on the sign of a and the value of q. Hyperbola/exponential have an excluded value or asymptote.",
    )
    return with_metadata(
        q_obj, topic=TOPIC, subskill="domain_range",
        learning_objective_id=f"{LO}.domain_range",
        misconception_tags=["swapped_domain_range", "wrong_bracket_type", "ignores_asymptote"],
        diagnostic_tags=["domain_range", "notation"],
        keywords=["domain", "range", "set notation", "interval notation"],
    )


# --------------------------------------------------------------------------- #
# representation_convert
# --------------------------------------------------------------------------- #
def _build_representation_convert(r, difficulty: str) -> Dict[str, Any]:
    mode = r.choice(["words", "table"])
    if mode == "words":
        k = r.randint(2, 9)
        relation = r.choice(["less", "more", "times"])
        if relation == "less":
            expr = X - k
            words = f"the output is always {k} less than the input"
        elif relation == "more":
            expr = X + k
            words = f"the output is always {k} more than the input"
        else:
            expr = k * X
            words = f"the output is always {k} times the input"
        q = make_short(
            prefix=TOPIC,
            prompt_latex=f"\\text{{Write a formula }} f(x) \\text{{ for the rule: }}\\\\ \\text{{“{words}.”}}",
            answer_expr=expr,
            answer_mode="expression",
            marks=2,
            explanation=f"As a formula this is f(x) = {to_latex_safe(expr)}.",
            hint="Let x be the input; translate the words into operations on x.",
        )
        sub_tags = ["misreads_relation", "swaps_operation"]
    else:
        m = nonzero(r, -3, 4)
        c = r.randint(-5, 5)
        expr = m * X + c
        inp = nonzero(r, -4, 5)
        out = int(expr.subs(X, inp))
        # Build a small table with one missing output, ask for it.
        xs = sorted({inp, inp + 1, inp - 2})
        row_x = " & ".join(num(v) for v in xs)
        row_y = " & ".join("?" if v == inp else num(int(expr.subs(X, v))) for v in xs)
        table_latex = (
            "\\begin{array}{|c|" + "c|" * len(xs) + "}\\hline "
            f"x & {row_x} \\\\\\hline "
            f"f(x) & {row_y} \\\\\\hline \\end{{array}}"
        )
        q = make_short(
            prefix=TOPIC,
            prompt_latex=(
                f"\\text{{The table follows }} {_linear_latex(m, c)}\\text{{.}}\\\\ "
                f"{table_latex}\\\\ \\text{{Find the missing output value (where }} x = {num(inp)}\\text{{).}}"
            ),
            answer_expr=sp.Integer(out),
            answer_mode="value",
            marks=1,
            explanation=f"Substitute x = {num(inp)}: f({num(inp)}) = {num(out)}.",
            hint="Use the formula to compute f(x) at the missing input.",
        )
        sub_tags = ["table_misread", "arithmetic_sign_error"]
    return with_metadata(
        q, topic=TOPIC, subskill="representation_convert",
        learning_objective_id=f"{LO}.representations",
        misconception_tags=sub_tags,
        diagnostic_tags=["representations", "convert"],
        keywords=["table", "words", "formula", "representation", "ordered pairs"],
    )


# --------------------------------------------------------------------------- #
# linear_gradient_intercept
# --------------------------------------------------------------------------- #
def _build_linear_gradient_intercept(r, difficulty: str) -> Dict[str, Any]:
    m = nonzero(r, -5, 5)
    c = r.randint(-7, 7)
    pair = sp.Tuple(sp.Integer(m), sp.Integer(c))
    q = make_short(
        prefix=TOPIC,
        prompt_latex=(
            f"\\text{{For }} {_linear_latex(m, c)}\\text{{, write down the gradient and the }} y\\text{{-intercept }}"
            "\\text{as } (m;c)."
        ),
        answer_expr=pair,
        answer_mode="value_pair",
        marks=2,
        answer_latex=_coord(m, c),
        explanation=f"In y = mx + c the gradient is m = {num(m)} and the y-intercept is c = {num(c)}.",
        hint="Read the coefficient of x (gradient) and the constant term (y-intercept).",
    )
    return with_metadata(
        q, topic=TOPIC, subskill="linear_gradient_intercept",
        learning_objective_id=f"{LO}.linear",
        misconception_tags=["swapped_m_and_c", "sign_error"],
        diagnostic_tags=["linear", "gradient", "intercept"],
        keywords=["gradient", "y-intercept", "y=mx+c", "slope"],
    )


# --------------------------------------------------------------------------- #
# linear_intercepts
# --------------------------------------------------------------------------- #
def _build_linear_intercepts(r, difficulty: str) -> Dict[str, Any]:
    # Keep an integer x-intercept: c divisible by m.
    m = nonzero(r, -4, 4)
    root = nonzero(r, -5, 5)
    c = -m * root
    expr = m * X + c
    ask = r.choice(["x", "y"])
    if ask == "x":
        coord = sp.Tuple(sp.Integer(root), sp.Integer(0))
        ans_latex = _coord(root, 0)
        steps = [
            step(from_expr=None, to_expr=None, op="for the x-intercept, let y = 0", rule="x-intercept",
                 from_latex=f"0 = {to_latex_safe(expr)}", to_latex=f"0 = {to_latex_safe(expr)}"),
            step(from_expr=sp.Eq(expr, 0), to_expr=sp.Eq(X, sp.Integer(root)), op="solve for x",
                 rule="solve", common_errors=["sign_error", "division_error"]),
        ]
        goal = "find the x-intercept"
        prompt = f"\\text{{Determine the coordinates of the }} x\\text{{-intercept of }} {_linear_latex(m, c, 'g')}."
    else:
        coord = sp.Tuple(sp.Integer(0), sp.Integer(c))
        ans_latex = _coord(0, c)
        steps = [
            step(from_expr=None, to_expr=None, op="for the y-intercept, let x = 0", rule="y-intercept",
                 from_latex=f"g(0) = {to_latex_safe(expr)}".replace("x", "(0)"),
                 to_latex=f"g(0) = {num(c)}"),
        ]
        goal = "find the y-intercept"
        prompt = f"\\text{{Determine the coordinates of the }} y\\text{{-intercept of }} {_linear_latex(m, c, 'g')}."
    sol = solution(goal=goal, chain_type="equation", var="x", steps=steps, final_expr=coord, final_latex=ans_latex)
    q = make_short(
        prefix=TOPIC,
        prompt_latex=prompt,
        answer_expr=coord,
        answer_mode="value_pair",
        marks=2,
        canonical_solution=sol,
        answer_latex=ans_latex,
        explanation=f"The {ask}-intercept is {ans_latex.replace(chr(92), '')}.",
        hint="x-intercept: let y = 0 and solve. y-intercept: let x = 0.",
    )
    return with_metadata(
        q, topic=TOPIC, subskill="linear_intercepts",
        learning_objective_id=f"{LO}.linear",
        misconception_tags=["wrong_intercept_axis", "sign_error"],
        diagnostic_tags=["linear", "intercepts"],
        keywords=["x-intercept", "y-intercept", "coordinates"],
    )


# --------------------------------------------------------------------------- #
# linear_find_equation
# --------------------------------------------------------------------------- #
def _build_linear_find_equation(r, difficulty: str) -> Dict[str, Any]:
    m = nonzero(r, -3, 4)
    c = r.randint(-5, 5)
    x1 = nonzero(r, -4, 0)
    x2 = r.randint(1, 4)
    p1 = (x1, int(m * x1 + c))
    p2 = (x2, int(m * x2 + c))
    expr = m * X + c
    grad_latex = f"m = \\dfrac{{{num(p2[1])} - ({num(p1[1])})}}{{{num(p2[0])} - ({num(p1[0])})}} = {num(m)}"
    sol = solution(
        goal="find y = mx + c",
        chain_type="expression",
        var="x",
        steps=[
            step(from_expr=None, to_expr=None, op="find the gradient", rule="m = Δy/Δx",
                 from_latex="m = \\dfrac{y_2 - y_1}{x_2 - x_1}", to_latex=grad_latex,
                 common_errors=["swapped_subtraction_order", "sign_error"]),
            step(from_expr=None, to_expr=None, op="substitute a point to find c", rule="substitute",
                 from_latex=f"{num(p1[1])} = {num(m)}({num(p1[0])}) + c", to_latex=f"c = {num(c)}",
                 common_errors=["sign_error"]),
            step(from_expr=None, to_expr=None, op="write the equation", rule="y = mx + c",
                 from_latex="y = mx + c", to_latex=f"y = {to_latex_safe(expr)}"),
        ],
        final_expr=expr,
        final_latex=f"y = {to_latex_safe(expr)}",
    )
    q = make_short(
        prefix=TOPIC,
        prompt_latex=(
            f"\\text{{A straight line passes through }} {_coord(*p1)} \\text{{ and }} {_coord(*p2)}.\\\\ "
            "\\text{Determine its equation in the form } y = mx + c \\text{ (give the right-hand side).}"
        ),
        answer_expr=expr,
        answer_mode="expression",
        marks=3,
        canonical_solution=sol,
        answer_latex=to_latex_safe(expr),
        explanation=f"Gradient m = {num(m)}; substituting a point gives c = {num(c)}, so y = {to_latex_safe(expr)}.",
        hint="Find m from the two points, then substitute one point to find c.",
    )
    return with_metadata(
        q, topic=TOPIC, subskill="linear_find_equation",
        learning_objective_id=f"{LO}.linear",
        misconception_tags=["swapped_subtraction_order", "forgot_to_find_c"],
        diagnostic_tags=["linear", "find_equation"],
        keywords=["gradient", "two points", "equation of a line"],
    )


# --------------------------------------------------------------------------- #
# quadratic_effect
# --------------------------------------------------------------------------- #
def _build_quadratic_effect(r, difficulty: str) -> Dict[str, Any]:
    which = r.choice(["q", "a_sign", "a_size"])
    if which == "q":
        q = nonzero(r, -4, 4)
        a = nonzero(r, 1, 3)
        direction = "upwards" if q > 0 else "downwards"
        correct = f"The graph of y = {num(a)}x^2 shifts {num(abs(q))} units {direction}."
        distractors = [
            f"The graph shifts {num(abs(q))} units {'downwards' if q > 0 else 'upwards'}.",
            f"The graph shifts {num(abs(q))} units to the {'right' if q > 0 else 'left'}.",
            "The graph becomes narrower.",
        ]
        prompt = f"What is the effect of q on the graph of y = {num(a)}x^2 {_signed(q)}?"
        expl = "q is a vertical shift: q > 0 moves the graph up, q < 0 moves it down."
    elif which == "a_sign":
        a = nonzero(r, -3, 3)
        shape = "a minimum turning point (a “smile”)" if a > 0 else "a maximum turning point (a “frown”)"
        correct = f"The graph has {shape}."
        distractors = [
            f"The graph has {'a maximum turning point (a “frown”)' if a > 0 else 'a minimum turning point (a “smile”)'}.",
            "The graph shifts vertically.",
            "The graph has no turning point.",
        ]
        prompt = f"For y = {num(a)}x^2 + q, what does the sign of a tell you about the shape?"
        expl = "a > 0 gives a minimum (smile); a < 0 gives a maximum (frown)."
    else:
        a = r.choice([2, 3, 4])
        correct = "The graph becomes narrower (a vertical stretch)."
        distractors = [
            "The graph becomes wider.",
            "The graph shifts upwards.",
            "The graph reflects in the x-axis.",
        ]
        prompt = f"How does the graph of y = {num(a)}x^2 compare to y = x^2?"
        expl = "Increasing |a| stretches the graph vertically, making it narrower."

    options = [correct] + distractors
    r.shuffle(options)
    q_obj = make_mcq(
        prefix=TOPIC,
        prompt=prompt,
        options=options,
        correct_index=options.index(correct),
        explanation=expl,
        hint="a controls the shape (stretch / reflection); q is a vertical shift.",
    )
    return with_metadata(
        q_obj, topic=TOPIC, subskill="quadratic_effect",
        learning_objective_id=f"{LO}.quadratic",
        misconception_tags=["confused_stretch_with_shift", "forgot_negative_reflection", "horizontal_vs_vertical"],
        diagnostic_tags=["quadratic", "effect_of_parameters"],
        keywords=["parabola", "effect of a", "effect of q", "vertical shift", "stretch"],
    )


# --------------------------------------------------------------------------- #
# quadratic_features
# --------------------------------------------------------------------------- #
def _build_quadratic_features(r, difficulty: str) -> Dict[str, Any]:
    a = nonzero(r, -3, 3)
    q = r.randint(-5, 5)
    ask = r.choice(["turning_point", "y_intercept", "axis"])
    spec = _diagram.function_graph(
        family="quadratic", a=a, q=q, domain=[-4, 4],
        features={"turning_point": [0, q], "y_intercept": [0, q]},
        caption=f"y = {num(a)}x² {('+ ' + num(q)) if q >= 0 else ('- ' + num(abs(q)))}",
    )
    if ask == "turning_point":
        coord = sp.Tuple(sp.Integer(0), sp.Integer(q))
        q_obj = make_short(
            prefix=TOPIC,
            prompt_latex=f"\\text{{Write down the coordinates of the turning point of }} {_quadratic_latex(a, q)}.",
            answer_expr=coord, answer_mode="value_pair", marks=2, answer_latex=_coord(0, q),
            explanation=f"For y = ax² + q the turning point is (0; q) = {_coord(0, q)}.",
            hint="For y = ax² + q the turning point is always on the y-axis at (0; q).",
        )
        tags = ["wrong_turning_point", "swaps_coordinates"]
    elif ask == "y_intercept":
        q_obj = make_short(
            prefix=TOPIC,
            prompt_latex=f"\\text{{Write down the }} y\\text{{-intercept value of }} {_quadratic_latex(a, q)}.",
            answer_expr=sp.Integer(q), answer_mode="value", marks=1,
            explanation=f"Let x = 0: y = {num(q)}.",
            hint="Let x = 0 in the formula.",
        )
        tags = ["wrong_intercept_axis"]
    else:
        # axis of symmetry x = 0
        q_obj = make_short(
            prefix=TOPIC,
            prompt_latex=f"\\text{{Write down the equation of the axis of symmetry of }} {_quadratic_latex(a, q)}.",
            answer_expr=sp.Eq(X, 0), answer_mode="equation", marks=1, answer_latex="x = 0",
            explanation="For y = ax² + q the axis of symmetry is the y-axis, x = 0.",
            hint="The axis of symmetry of y = ax² + q is the y-axis.",
        )
        tags = ["wrong_axis_of_symmetry"]
    return with_metadata(
        q_obj, topic=TOPIC, subskill="quadratic_features",
        learning_objective_id=f"{LO}.quadratic",
        misconception_tags=tags,
        diagnostic_tags=["quadratic", "features"],
        keywords=["turning point", "axis of symmetry", "y-intercept", "parabola"],
        diagram_spec=spec,
    )


# --------------------------------------------------------------------------- #
# hyperbola_features
# --------------------------------------------------------------------------- #
def _build_hyperbola_features(r, difficulty: str) -> Dict[str, Any]:
    a = nonzero(r, -6, 6)
    q = nonzero(r, -4, 4)
    eq = f"f(x) = \\dfrac{{{num(a)}}}{{x}} {_signed(q)}"
    spec = _diagram.function_graph(
        family="hyperbola", a=a, q=q, domain=[-6, 6],
        features={"asymptotes": {"horizontal": q, "vertical": 0}},
        caption="Hyperbola with asymptotes shown",
    )
    ask = r.choice(["horizontal", "vertical"])
    if ask == "horizontal":
        q_obj = make_short(
            prefix=TOPIC,
            prompt_latex=f"\\text{{For }} {eq}\\text{{, the horizontal asymptote is }} y = \\;?",
            answer_expr=sp.Integer(q), answer_mode="value", marks=1,
            explanation=f"The horizontal asymptote of y = a/x + q is y = q = {num(q)}.",
            hint="The +q shifts the whole graph; the horizontal asymptote moves to y = q.",
        )
        tags = ["wrong_asymptote", "ignores_q_shift"]
    else:
        q_obj = make_short(
            prefix=TOPIC,
            prompt_latex=f"\\text{{For }} {eq}\\text{{, the vertical asymptote is }} x = \\;?",
            answer_expr=sp.Integer(0), answer_mode="value", marks=1,
            explanation="The vertical asymptote of y = a/x + q is x = 0 (division by zero).",
            hint="Where is the function undefined? That is the vertical asymptote.",
        )
        tags = ["wrong_asymptote"]
    return with_metadata(
        q_obj, topic=TOPIC, subskill="hyperbola_features",
        learning_objective_id=f"{LO}.hyperbola",
        misconception_tags=tags,
        diagnostic_tags=["hyperbola", "asymptote"],
        keywords=["hyperbola", "asymptote", "y=a/x+q"],
        diagram_spec=spec,
    )


# --------------------------------------------------------------------------- #
# exponential_features
# --------------------------------------------------------------------------- #
def _build_exponential_features(r, difficulty: str) -> Dict[str, Any]:
    a = r.choice([1, 1, 2, -1])
    b = r.choice([2, 3])
    q = r.randint(-3, 3)
    eq = f"f(x) = {('' if a == 1 else ('-' if a == -1 else num(a) + ' \\cdot '))}{b}^{{x}} {_signed(q)}"
    spec = _diagram.function_graph(
        family="exponential", a=a, q=q, b=b, domain=[-4, 4],
        features={"asymptotes": {"horizontal": q}},
        caption="Exponential graph with horizontal asymptote",
    )
    ask = r.choice(["asymptote", "growth"])
    if ask == "asymptote":
        q_obj = make_short(
            prefix=TOPIC,
            prompt_latex=f"\\text{{For }} {eq}\\text{{, the horizontal asymptote is }} y = \\;?",
            answer_expr=sp.Integer(q), answer_mode="value", marks=1,
            explanation=f"The horizontal asymptote of y = a·bˣ + q is y = q = {num(q)}.",
            hint="As x → −∞ the bˣ term vanishes, leaving y = q.",
        )
        return with_metadata(
            q_obj, topic=TOPIC, subskill="exponential_features",
            learning_objective_id=f"{LO}.exponential",
            misconception_tags=["wrong_asymptote", "ignores_q_shift"],
            diagnostic_tags=["exponential", "asymptote"],
            keywords=["exponential", "asymptote", "growth", "decay"],
            diagram_spec=spec,
        )
    # growth vs decay (a>0): base > 1 → growth
    grows = a > 0
    correct = "The graph increases (exponential growth)." if grows else "The graph is reflected and decreases."
    distractors = [
        "The graph decreases towards the asymptote (decay)." if grows else "The graph increases (exponential growth).",
        "The graph is a straight line.",
        "The graph has a turning point.",
    ]
    options = [correct] + distractors
    r.shuffle(options)
    q_obj = make_mcq(
        prefix=TOPIC,
        prompt=f"Describe the behaviour of y = {('' if a == 1 else (str(a) + '·'))}{b}^x {('+' + str(q)) if q >= 0 else ('-' + str(abs(q)))}.",
        options=options, correct_index=options.index(correct),
        explanation="With base b > 1 and a > 0 the graph grows; a < 0 reflects it in its asymptote.",
        hint="b > 1 with a > 0 means growth; a < 0 flips the graph.",
    )
    return with_metadata(
        q_obj, topic=TOPIC, subskill="exponential_features",
        learning_objective_id=f"{LO}.exponential",
        misconception_tags=["confuses_growth_decay", "forgot_negative_reflection"],
        diagnostic_tags=["exponential", "growth_decay"],
        keywords=["exponential", "growth", "decay"],
        diagram_spec=spec,
    )


# --------------------------------------------------------------------------- #
# trig_graph_features
# --------------------------------------------------------------------------- #
def _build_trig_graph_features(r, difficulty: str) -> Dict[str, Any]:
    fam = r.choice(["sin", "cos"])
    a = nonzero(r, -3, 3)
    q = r.randint(-2, 2)
    eq = f"y = {('' if a == 1 else ('-' if a == -1 else num(a)))}\\{fam}\\,\\theta {_signed(q)}"
    spec = _diagram.function_graph(
        family=fam, a=a, q=q, domain=[0, 360],
        caption=f"y = a·{fam}θ + q on [0°; 360°]",
    )
    ask = r.choice(["amplitude", "range", "period"])
    if ask == "amplitude":
        q_obj = make_short(
            prefix=TOPIC,
            prompt_latex=f"\\text{{Write down the amplitude of }} {eq}.",
            answer_expr=sp.Integer(abs(a)), answer_mode="value", marks=1,
            explanation=f"The amplitude is |a| = {num(abs(a))}.",
            hint="Amplitude is the absolute value of a.",
        )
        tags = ["amplitude_sign_error"]
    elif ask == "period":
        q_obj = make_short(
            prefix=TOPIC,
            prompt_latex=f"\\text{{Write down the period (in degrees) of }} {eq}.",
            answer_expr=sp.Integer(360), answer_mode="value", marks=1, answer_latex="360^{\\circ}",
            explanation="The period of sin and cos is 360°.",
            hint="One full cycle of sin/cos is 360°.",
        )
        tags = ["wrong_period"]
    else:
        lo = q - abs(a)
        hi = q + abs(a)
        pair = sp.Tuple(sp.Integer(lo), sp.Integer(hi))
        q_obj = make_short(
            prefix=TOPIC,
            prompt_latex=f"\\text{{Write down the range of }} {eq} \\text{{ as }} (\\text{{min}};\\text{{max}}).",
            answer_expr=pair, answer_mode="value_pair", marks=2, answer_latex=_coord(lo, hi),
            explanation=f"The range is [q − |a|; q + |a|] = {_coord(lo, hi)}.",
            hint="Range runs from q − |a| to q + |a|.",
        )
        tags = ["wrong_range", "forgets_q_shift"]
    return with_metadata(
        q_obj, topic=TOPIC, subskill="trig_graph_features",
        learning_objective_id=f"{LO}.trig",
        misconception_tags=tags,
        diagnostic_tags=["trig_graphs", "features"],
        keywords=["amplitude", "period", "range", "sine", "cosine"],
        diagram_spec=spec,
    )


# --------------------------------------------------------------------------- #
# interpret_graph  (read a point off a rendered graph)
# --------------------------------------------------------------------------- #
def _build_interpret_graph(r, difficulty: str) -> Dict[str, Any]:
    m = nonzero(r, -3, 3)
    root = nonzero(r, -4, 4)
    c = -m * root
    expr = m * X + c
    ask = r.choice(["x", "y"])
    spec = _diagram.function_graph(
        family="linear", a=m, q=c, domain=[-6, 6],
        features={"x_intercepts": [[root, 0]], "y_intercept": [0, c]},
        caption="Read the required intercept from the graph.",
    )
    if ask == "x":
        coord = sp.Tuple(sp.Integer(root), sp.Integer(0))
        ans_latex = _coord(root, 0)
        prompt = "\\text{Read off the coordinates of the } x\\text{-intercept from the graph.}"
    else:
        coord = sp.Tuple(sp.Integer(0), sp.Integer(c))
        ans_latex = _coord(0, c)
        prompt = "\\text{Read off the coordinates of the } y\\text{-intercept from the graph.}"
    q_obj = make_short(
        prefix=TOPIC, prompt_latex=prompt, answer_expr=coord, answer_mode="value_pair",
        marks=1, answer_latex=ans_latex,
        explanation=f"The required intercept is {ans_latex.replace(chr(92), '')}.",
        hint="The x-intercept is where the line crosses the x-axis; the y-intercept where it crosses the y-axis.",
    )
    return with_metadata(
        q_obj, topic=TOPIC, subskill="interpret_graph",
        learning_objective_id=f"{LO}.interpret",
        misconception_tags=["swaps_coordinates", "wrong_intercept_axis"],
        diagnostic_tags=["interpretation", "read_graph"],
        keywords=["interpret graph", "read off", "intercept"],
        diagram_spec=spec,
    )


# --------------------------------------------------------------------------- #
# match_equation_graph
# --------------------------------------------------------------------------- #
def _build_match_equation_graph(r, difficulty: str) -> Dict[str, Any]:
    family = r.choice(["linear", "quadratic", "exponential"])
    if family == "linear":
        m = nonzero(r, -3, 3)
        c = r.randint(-4, 4)
        spec = _diagram.function_graph(family="linear", a=m, q=c, domain=[-6, 6])
        correct = _linear_latex(m, c).replace("f(x) =", "y =")
        distractors = [
            _linear_latex(-m, c).replace("f(x) =", "y ="),
            _linear_latex(m, -c).replace("f(x) =", "y ="),
            _quadratic_latex(1, c).replace("f(x) =", "y ="),
        ]
    elif family == "quadratic":
        a = nonzero(r, -3, 3)
        q = r.randint(-4, 4)
        spec = _diagram.function_graph(family="quadratic", a=a, q=q, domain=[-4, 4])
        correct = _quadratic_latex(a, q).replace("f(x) =", "y =")
        distractors = [
            _quadratic_latex(-a, q).replace("f(x) =", "y ="),
            _quadratic_latex(a, -q).replace("f(x) =", "y ="),
            _linear_latex(a, q).replace("f(x) =", "y ="),
        ]
    else:
        b = r.choice([2, 3])
        q = r.randint(-2, 2)
        spec = _diagram.function_graph(family="exponential", a=1, q=q, b=b, domain=[-4, 4])
        correct = f"y = {b}^{{x}} {_signed(q)}"
        distractors = [
            f"y = {b}^{{x}} {_signed(-q)}",
            _quadratic_latex(1, q).replace("f(x) =", "y ="),
            _linear_latex(b, q).replace("f(x) =", "y ="),
        ]
    options = [correct] + distractors
    r.shuffle(options)
    q_obj = make_mcq(
        prefix=TOPIC,
        prompt="Which equation matches the graph shown?",
        options=[f"option {i+1}" for i in range(len(options))],
        options_latex=options,
        correct_index=options.index(correct),
        explanation=f"The graph is {correct}.",
        hint="Match the shape (line / parabola / exponential), the direction (sign of a) and the shift (q).",
    )
    return with_metadata(
        q_obj, topic=TOPIC, subskill="match_equation_graph",
        learning_objective_id=f"{LO}.interpret",
        misconception_tags=["confuses_family", "ignores_sign", "ignores_shift"],
        diagnostic_tags=["interpretation", "match_graph"],
        keywords=["match", "equation", "graph", "family"],
        diagram_spec=spec,
    )


# --------------------------------------------------------------------------- #
# parameter_manipulation  (interactive grapher)
# --------------------------------------------------------------------------- #
def _build_parameter_manipulation(r, difficulty: str) -> Dict[str, Any]:
    family = r.choice(["linear", "quadratic", "exponential"])
    a = nonzero(r, -3, 3)
    q = r.randint(-4, 4)
    b = r.choice([2, 3])
    target = {"a": a, "q": q}
    family_label = {"linear": "y = ax + q", "quadratic": "y = ax² + q", "exponential": f"y = a·{b}ˣ + q"}[family]
    target_latex = {
        "linear": _linear_latex(a, q).replace("f(x) =", "y ="),
        "quadratic": _quadratic_latex(a, q).replace("f(x) =", "y ="),
        "exponential": f"y = {('' if a == 1 else ('-' if a == -1 else num(a) + '·'))}{b}^x {_signed(q)}",
    }[family]
    spec = _diagram.function_graph(
        family=family, a=1, q=0, b=b,
        domain=[0, 360] if family in ("sin", "cos", "tan") else ([-4, 4] if family == "quadratic" else [-6, 6]),
        interactive={"sliders": ["a", "q"], "target": {"a": a, "q": q, "b": b}},
        caption=f"Drag the a and q sliders so your curve ({family_label}) matches the dashed target.",
    )
    q_obj = make_function_transform(
        prefix=TOPIC,
        prompt=f"Use the sliders to make the curve match the dashed target graph ({target_latex}).",
        target_params=target,
        sliders=["a", "q"],
        marks=2,
        tolerance=0.0,
        explanation=f"The target is {target_latex}, so a = {num(a)} and q = {num(q)}.",
        hint="a changes the shape/stretch (and reflects when negative); q shifts the graph vertically.",
    )
    q_obj["prompt_latex"] = f"\\text{{Drag the sliders so your curve matches the dashed target: }} {target_latex}."
    return with_metadata(
        q_obj, topic=TOPIC, subskill="parameter_manipulation",
        learning_objective_id=f"{LO}.quadratic",
        misconception_tags=["confused_stretch_with_shift", "forgot_negative_reflection"],
        diagnostic_tags=["effect_of_parameters", "interactive_grapher"],
        keywords=["parameters", "a", "q", "transform", "grapher", "sliders"],
        diagram_spec=spec,
    )


SUBSKILLS = {
    "function_notation_eval": _build_function_notation_eval,
    "function_notation_solve": _build_function_notation_solve,
    "domain_range": _build_domain_range,
    "representation_convert": _build_representation_convert,
    "linear_gradient_intercept": _build_linear_gradient_intercept,
    "linear_intercepts": _build_linear_intercepts,
    "linear_find_equation": _build_linear_find_equation,
    "quadratic_effect": _build_quadratic_effect,
    "quadratic_features": _build_quadratic_features,
    "hyperbola_features": _build_hyperbola_features,
    "exponential_features": _build_exponential_features,
    "trig_graph_features": _build_trig_graph_features,
    "interpret_graph": _build_interpret_graph,
    "match_equation_graph": _build_match_equation_graph,
    "parameter_manipulation": _build_parameter_manipulation,
    # default / mixed alias
    "concepts": _build_function_notation_eval,
}

generate = build_generate(SUBSKILLS, default_subskill="function_notation_eval")
