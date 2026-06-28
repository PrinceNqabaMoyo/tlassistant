"""Grade 10 Mathematics — Term 1 — Equations & Inequalities (deterministic, SymPy-backed)."""
from __future__ import annotations
from typing import Any, Dict
import sympy as sp
from app.utils.grade10_mathematics._math_common import (
    build_generate, make_short, make_steps, nonzero, solution, step, to_latex, to_latex_safe, with_metadata,
)

TOPIC = "grade10_math_equations_inequalities"
LO = "math10_equations_inequalities"
x = sp.Symbol("x")


def _build_linear_equations(r, difficulty: str) -> Dict[str, Any]:
    case = r.choice(["simple", "brackets", "fraction", "mixed"])
    symbol = sp.Symbol(r.choice(["x", "y", "t", "a"]))
    if case == "simple":
        a = nonzero(r, 2, 9)
        b = nonzero(r, -9, 9)
        c = nonzero(r, -20, 20)
        expr = sp.Eq(a * symbol + b, c)
        ans = sp.solve(expr, symbol)[0]
        steps = [
            step(from_expr=expr, to_expr=sp.Eq(a * symbol, c - b), op="transpose constant", rule="additive inverse", common_errors=["sign_error_on_transpose"]),
            step(from_expr=sp.Eq(a * symbol, c - b), to_expr=sp.Eq(symbol, ans), op="divide by coefficient", rule="multiplicative inverse", common_errors=["sign_error"]),
        ]
    elif case == "brackets":
        a = nonzero(r, 2, 5)
        b = nonzero(r, -5, 5)
        c = nonzero(r, -20, 20)
        d = nonzero(r, -9, 9)
        expr = sp.Eq(a * (symbol + b), c)
        ans = sp.solve(expr, symbol)[0]
        steps = [
            step(from_expr=expr, to_expr=sp.Eq(symbol + b, sp.Rational(c, a)), op="divide by coefficient", rule="distributive", common_errors=["sign_error"]),
            step(from_expr=sp.Eq(symbol + b, sp.Rational(c, a)), to_expr=sp.Eq(symbol, ans), op="transpose constant", rule="additive inverse", common_errors=["sign_error_on_transpose"]),
        ]
    elif case == "fraction":
        a = nonzero(r, 1, 5)
        b = nonzero(r, -5, 5)
        c = nonzero(r, 2, 6)
        d = nonzero(r, 1, 5)
        e = nonzero(r, -9, 9)
        restriction = sp.solve(c * symbol + d, symbol)[0]
        expr = sp.Eq((a * symbol + b) / (c * symbol + d), e)
        ans = sp.solve(expr, symbol)[0]
        steps = [
            step(from_expr=expr, to_expr=sp.Eq(a * symbol + b, e * (c * symbol + d)), op="multiply by denominator", rule="clear fraction", common_errors=["sign_error"]),
            step(from_expr=sp.Eq(a * symbol + b, e * (c * symbol + d)), to_expr=None, op="expand and collect terms", rule="distributive", common_errors=["sign_error_on_transpose"]),
            step(from_expr=None, to_expr=sp.Eq(symbol, ans), op="solve linear equation", rule="linear equation", common_errors=["sign_error"]),
        ]
    else:  # mixed
        a = nonzero(r, 2, 5)
        b = nonzero(r, -5, 5)
        c = nonzero(r, -9, 9)
        d = nonzero(r, -20, 20)
        e = nonzero(r, -9, 9)
        expr = sp.Eq(a * (symbol + b) + c * symbol, d - e * symbol)
        ans = sp.solve(expr, symbol)[0]
        steps = [
            step(from_expr=expr, to_expr=None, op="expand brackets", rule="distributive", common_errors=["sign_error"]),
            step(from_expr=None, to_expr=None, op="collect like terms", rule="additive inverse", common_errors=["sign_error_on_transpose"]),
            step(from_expr=None, to_expr=sp.Eq(symbol, ans), op="solve", rule="linear equation", common_errors=["sign_error"]),
        ]
    sol = solution(goal=f"solve for {symbol}", chain_type="equation", var=str(symbol), steps=steps, final_expr=ans)
    q = make_steps(prefix=TOPIC, prompt_latex=f"\\text{{Solve for ${str(symbol)}$: }} {to_latex(expr)}",
                   canonical_solution=sol, marks=3,
                   explanation="Expand, collect like terms, then isolate the variable.",
                   hint="Remember to check your answer by substituting back.")
    return with_metadata(q, topic=TOPIC, subskill="linear_equations",
                         learning_objective_id=f"{LO}.linear",
                         misconception_tags=["sign_error_on_transpose", "divided_by_variable"],
                         diagnostic_tags=["linear_equations", "solve"])


def _build_quadratic_by_factorising(r, difficulty: str) -> Dict[str, Any]:
    symbol = sp.Symbol(r.choice(["x", "y", "p"]))
    # Generate factorable quadratics: (symbol + a)(symbol + b) = 0
    a = nonzero(r, -8, 8)
    b = nonzero(r, -8, 8)
    while a == 0 or b == 0:
        a = nonzero(r, -8, 8)
        b = nonzero(r, -8, 8)
    expanded = sp.expand((symbol + a) * (symbol + b))
    expr = sp.Eq(expanded, 0)
    ans = sp.FiniteSet(-a, -b)
    steps = [
        step(from_expr=expr, to_expr=None, op="factorise quadratic", rule="find two numbers that multiply to c and add to b", common_errors=["wrong_factors"]),
        step(from_expr=None, to_expr=sp.Eq((symbol + a) * (symbol + b), 0), op="write in factored form", rule="(x+r1)(x+r2)=0", common_errors=["sign_error"]),
        step(from_expr=sp.Eq((symbol + a) * (symbol + b), 0), to_expr=ans, op="set each factor to zero", rule="if ab=0 then a=0 or b=0", common_errors=["dropped_a_root"]),
    ]
    sol = solution(goal=f"solve quadratic for {symbol}", chain_type="equation", var=str(symbol), steps=steps, final_expr=ans)
    q = make_steps(prefix=TOPIC, prompt_latex=f"\\text{{Solve for ${str(symbol)}$: }} {to_latex(expr)}",
                   canonical_solution=sol, marks=3,
                   explanation="Factorise the quadratic, then set each factor equal to zero.",
                   hint="Look for two numbers that multiply to the constant term and add to the coefficient of x.")
    return with_metadata(q, topic=TOPIC, subskill="quadratic_by_factorising",
                         learning_objective_id=f"{LO}.quad_factor",
                         misconception_tags=["wrong_factors", "dropped_a_root", "sign_error"],
                         diagnostic_tags=["quadratic", "factorisation"])


def _build_quadratic_restrictions(r, difficulty: str) -> Dict[str, Any]:
    symbol = sp.Symbol(r.choice(["x", "y"]))
    a = nonzero(r, 1, 5)
    b = nonzero(r, -5, 5)
    c = nonzero(r, -9, 9)
    d = nonzero(r, 1, 5)
    e = nonzero(r, 1, 5)
    # (ax+b)/(cx+d) = e  with restriction cx+d != 0
    restriction = sp.solve(c * symbol + d, symbol)[0]
    expr = sp.Eq((a * symbol + b) / (c * symbol + d), e)
    ans = sp.solve(expr, symbol)[0]
    steps = [
        step(from_expr=expr, to_expr=sp.Eq(a * symbol + b, e * (c * symbol + d)),
             op="multiply by denominator", rule="clear fraction; restriction: denominator != 0", common_errors=["ignored_restriction"]),
        step(from_expr=sp.Eq(a * symbol + b, e * (c * symbol + d)), to_expr=None, op="expand and solve",
             rule="distributive + collect like terms", common_errors=["sign_error_on_transpose"]),
        step(from_expr=None, to_expr=sp.Eq(symbol, ans), op="check restriction", rule=f"{symbol} != {to_latex(restriction)}", common_errors=["ignored_restriction"]),
    ]
    sol = solution(goal=f"solve with restriction", chain_type="equation", var=str(symbol), steps=steps, final_expr=ans)
    q = make_steps(prefix=TOPIC, prompt_latex=f"\\text{{Solve for ${str(symbol)}$ (state restrictions): }} {to_latex(expr)}",
                   canonical_solution=sol, marks=4,
                   explanation="Clear the fraction, solve the linear equation, and state any restrictions.",
                   hint="Always state the restriction that the denominator cannot be zero.")
    return with_metadata(q, topic=TOPIC, subskill="quadratic_restrictions",
                         learning_objective_id=f"{LO}.quad_restrictions",
                         misconception_tags=["ignored_restriction", "sign_error_on_transpose"],
                         diagnostic_tags=["fractions", "restrictions", "quadratic"])


def _build_simultaneous_substitution(r, difficulty: str) -> Dict[str, Any]:
    x_sym = sp.Symbol("x")
    y_sym = sp.Symbol("y")
    a = nonzero(r, 1, 5)
    b = nonzero(r, -5, 5)
    c = nonzero(r, -20, 20)
    # eq1: y = a*x + b
    # eq2: c*x + d*y = e
    d = nonzero(r, 1, 5)
    e = nonzero(r, -20, 20)
    eq1 = sp.Eq(y_sym, a * x_sym + b)
    eq2 = sp.Eq(c * x_sym + d * y_sym, e)
    soln = sp.solve([eq1, eq2], [x_sym, y_sym])
    x_ans, y_ans = soln[x_sym], soln[y_sym]
    steps = [
        step(from_expr=eq2, to_expr=None, op="substitute expression for y",
             rule=f"replace y with {to_latex(a * x_sym + b)}", common_errors=["sign_error_on_transpose"]),
        step(from_expr=None, to_expr=None, op="solve for x", rule="linear equation in x", common_errors=["sign_error"]),
        step(from_expr=None, to_expr=sp.Eq(x_sym, x_ans), op="find x", rule="simplify", common_errors=["sign_error"]),
        step(from_expr=sp.Eq(x_sym, x_ans), to_expr=sp.Eq(y_sym, y_ans), op="substitute back to find y",
             rule=f"y = {a}({to_latex(x_ans)}) + {b}", common_errors=["sign_error"]),
    ]
    sol = solution(goal="solve simultaneous equations", chain_type="equation", var="x", steps=steps, final_expr=sp.Tuple(x_ans, y_ans))
    q = make_steps(prefix=TOPIC, prompt_latex=f"\\text{{Solve simultaneously: }} {to_latex(eq1)} \\quad \\text{{and}} \\quad {to_latex(eq2)}",
                   canonical_solution=sol, marks=4,
                   explanation="Substitute the expression for y into the second equation, solve for x, then find y.",
                   hint="Use the equation where y is already isolated.")
    return with_metadata(q, topic=TOPIC, subskill="simultaneous_substitution",
                         learning_objective_id=f"{LO}.simul_sub",
                         misconception_tags=["sign_error_on_transpose", "sign_error"],
                         diagnostic_tags=["simultaneous", "substitution"])


def _build_simultaneous_elimination(r, difficulty: str) -> Dict[str, Any]:
    x_sym = sp.Symbol("x")
    y_sym = sp.Symbol("y")
    a = nonzero(r, 1, 5)
    b = nonzero(r, 1, 5)
    c = nonzero(r, -20, 20)
    d = nonzero(r, 1, 5)
    e = nonzero(r, -20, 20)
    f = nonzero(r, -20, 20)
    eq1 = sp.Eq(a * x_sym + b * y_sym, c)
    eq2 = sp.Eq(d * x_sym + e * y_sym, f)
    soln = sp.solve([eq1, eq2], [x_sym, y_sym])
    x_ans, y_ans = soln[x_sym], soln[y_sym]
    steps = [
        step(from_expr=sp.Tuple(eq1, eq2), to_expr=None, op="match coefficients",
             rule="multiply equations to make x or y coefficients equal", common_errors=["sign_error"]),
        step(from_expr=None, to_expr=None, op="subtract equations to eliminate one variable",
             rule="elimination", common_errors=["sign_error_on_transpose"]),
        step(from_expr=None, to_expr=sp.Eq(y_sym, y_ans), op="solve for y", rule="linear equation", common_errors=["sign_error"]),
        step(from_expr=sp.Eq(y_sym, y_ans), to_expr=sp.Eq(x_sym, x_ans), op="substitute back to find x",
             rule="substitute y into first equation", common_errors=["sign_error"]),
    ]
    sol = solution(goal="solve simultaneous equations", chain_type="equation", var="x", steps=steps, final_expr=sp.Tuple(x_ans, y_ans))
    q = make_steps(prefix=TOPIC, prompt_latex=f"\\text{{Solve simultaneously: }} {to_latex(eq1)} \\quad \\text{{and}} \\quad {to_latex(eq2)}",
                   canonical_solution=sol, marks=4,
                   explanation="Multiply equations to match coefficients, subtract to eliminate one variable, then substitute back.",
                   hint="Choose to eliminate the variable with the simplest coefficients.")
    return with_metadata(q, topic=TOPIC, subskill="simultaneous_elimination",
                         learning_objective_id=f"{LO}.simul_elim",
                         misconception_tags=["sign_error_on_transpose", "sign_error"],
                         diagnostic_tags=["simultaneous", "elimination"])


def _build_word_problems(r, difficulty: str) -> Dict[str, Any]:
    symbol = sp.Symbol(r.choice(["x", "n", "y"]))
    a = nonzero(r, 2, 5)
    b = nonzero(r, -10, 10)
    c = nonzero(r, -30, 30)
    # "The sum of a number and its triple is 20" -> symbol + 3*symbol = 20
    expr = sp.Eq(symbol + a * symbol, c)
    ans = sp.solve(expr, symbol)[0]
    verb = r.choice(["sum", "total", "difference"])
    if verb == "sum":
        prompt = f"\\text{{The sum of a number and its {a}-times is {c}. Find the number.}}"
    elif verb == "total":
        prompt = f"\\text{{A number multiplied by {a} and then added to itself gives {c}. Find the number.}}"
    else:
        prompt = f"\\text{{The difference between {a}-times a number and the number is {c}. Find the number.}}"
        expr = sp.Eq(a * symbol - symbol, c)
        ans = sp.solve(expr, symbol)[0]
    steps = [
        step(from_expr=expr, to_expr=None, op="translate words to equation", rule="let the number be x", common_errors=["sign_error"]),
        step(from_expr=None, to_expr=sp.Eq(symbol, ans), op="solve", rule="linear equation", common_errors=["sign_error"]),
    ]
    sol = solution(goal="solve word problem", chain_type="equation", var=str(symbol), steps=steps, final_expr=ans)
    q = make_steps(prefix=TOPIC, prompt_latex=prompt, canonical_solution=sol, marks=3,
                   explanation="Translate the words into an equation, then solve.",
                   hint="Let the unknown number be x, then write the equation.")
    return with_metadata(q, topic=TOPIC, subskill="word_problems",
                         learning_objective_id=f"{LO}.word",
                         misconception_tags=["sign_error"],
                         diagnostic_tags=["word_problems", "translation"])


def _build_literal_equations(r, difficulty: str) -> Dict[str, Any]:
    target = sp.Symbol(r.choice(["x", "y", "h", "r"]))
    other = sp.Symbol(r.choice(["a", "b", "c", "d", "k", "m"]))
    while str(other) == str(target):
        other = sp.Symbol(r.choice(["a", "b", "c", "d", "k", "m"]))
    a = nonzero(r, 1, 5)
    b = nonzero(r, -5, 5)
    c = nonzero(r, -9, 9)
    expr = sp.Eq(a * target + b * other, c)
    ans = sp.solve(expr, target)[0]
    steps = [
        step(from_expr=expr, to_expr=sp.Eq(a * target, c - b * other), op="transpose term with other variable",
             rule="additive inverse", common_errors=["sign_error_on_transpose"]),
        step(from_expr=sp.Eq(a * target, c - b * other), to_expr=sp.Eq(target, ans), op="divide by coefficient",
             rule="multiplicative inverse", common_errors=["sign_error"]),
    ]
    sol = solution(goal=f"change the subject to {target}", chain_type="equation", var=str(target), steps=steps, final_expr=ans)
    q = make_steps(prefix=TOPIC, prompt_latex=f"\\text{{Make ${str(target)}$ the subject: }} {to_latex(expr)}",
                   canonical_solution=sol, marks=3,
                   explanation="Isolate the target variable by moving other terms and dividing by the coefficient.",
                   hint="Treat the other variables as constants.")
    return with_metadata(q, topic=TOPIC, subskill="literal_equations",
                         learning_objective_id=f"{LO}.literal",
                         misconception_tags=["sign_error_on_transpose", "sign_error"],
                         diagnostic_tags=["literal_equations", "change_subject"])


def _build_linear_inequalities(r, difficulty: str) -> Dict[str, Any]:
    symbol = sp.Symbol(r.choice(["x", "y", "r", "q"]))
    case = r.choice(["simple", "brackets", "negative_coeff"])
    if case == "simple":
        a = nonzero(r, 2, 6)
        b = nonzero(r, -10, 10)
        c = nonzero(r, -20, 20)
        expr = sp.Lt(a * symbol + b, c) if r.random() < 0.5 else sp.Gt(a * symbol + b, c)
    elif case == "brackets":
        a = nonzero(r, 2, 5)
        b = nonzero(r, -5, 5)
        c = nonzero(r, -20, 20)
        expr = sp.Lt(a * (symbol + b), c) if r.random() < 0.5 else sp.Gt(a * (symbol + b), c)
    else:  # negative_coeff
        a = -nonzero(r, 2, 6)
        b = nonzero(r, -10, 10)
        c = nonzero(r, -20, 20)
        expr = sp.Lt(a * symbol + b, c) if r.random() < 0.5 else sp.Gt(a * symbol + b, c)
    # Solve
    ans = sp.solve_univariate_inequality(expr, symbol, relational=False)
    # For the canonical solution, use the simplified inequality form
    simplified = sp.solve_univariate_inequality(expr, symbol)
    steps = [
        step(from_expr=expr, to_expr=None, op="expand/collect terms", rule="distributive", common_errors=["sign_error"]),
        step(from_expr=None, to_expr=None, op="transpose constant", rule="additive inverse", common_errors=["sign_error_on_transpose"]),
        step(from_expr=None, to_expr=simplified, op="divide by coefficient",
             rule=f"divide by {a}; {'flip inequality' if a < 0 else 'do not flip'}", common_errors=["forgot_to_flip_inequality"]),
    ]
    sol = solution(goal=f"solve inequality for {symbol}", chain_type="equation", var=str(symbol), steps=steps, final_expr=simplified)
    q = make_steps(prefix=TOPIC, prompt_latex=f"\\text{{Solve for ${str(symbol)}$: }} {to_latex(expr)}",
                   canonical_solution=sol, marks=3,
                   explanation="Solve like a linear equation, but flip the inequality sign when dividing by a negative number.",
                   hint="Be careful: multiplying or dividing by a negative number flips the inequality sign.")
    return with_metadata(q, topic=TOPIC, subskill="linear_inequalities",
                         learning_objective_id=f"{LO}.inequalities",
                         misconception_tags=["forgot_to_flip_inequality", "sign_error_on_transpose"],
                         diagnostic_tags=["inequalities", "linear"])


# --------------------------------------------------------------------------- #
# Dispatcher
# --------------------------------------------------------------------------- #
generate = build_generate(
    {
        "linear_equations": _build_linear_equations,
        "quadratic_by_factorising": _build_quadratic_by_factorising,
        "quadratic_restrictions": _build_quadratic_restrictions,
        "simultaneous_substitution": _build_simultaneous_substitution,
        "simultaneous_elimination": _build_simultaneous_elimination,
        "word_problems": _build_word_problems,
        "literal_equations": _build_literal_equations,
        "linear_inequalities": _build_linear_inequalities,
    },
    default_subskill="linear_equations",
)
