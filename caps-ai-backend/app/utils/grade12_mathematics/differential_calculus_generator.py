"""Grade 12 Mathematics — Differential Calculus (Deterministic 6-Pillar Generator).
Covers official CAPS Examination standards (Level 3 & Level 4: 35 marks in NSC Paper 1).
Supports full compound exam questions and atomic elementary sub-drills for adaptive deconstruction.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional
import sympy as sp

from app.utils.grade12_mathematics._math_common import (
    make_id,
    make_math_question,
    nonzero,
    num,
    rng,
    solution_graph,
    step,
    to_latex,
)

TOPIC = "differential_calculus"
LO = "math12_calculus"
x = sp.Symbol("x")
h = sp.Symbol("h")


# --------------------------------------------------------------------------- #
# Compound Level 3 & 4: Differentiation from First Principles (5 Marks)
# --------------------------------------------------------------------------- #
def _build_first_principles_compound(r, difficulty: str) -> Dict[str, Any]:
    """Compound 5-mark NSC examination question: differentiation from first principles.
    f'(x) = lim_{h -> 0} [f(x+h) - f(x)] / h for quadratic f(x) = ax^2 + bx + c.
    Includes fully worked SymPy substitution, algebraic expansion, factorisation of h, and limit evaluation.
    """
    a = nonzero(r, -3, 3)
    b = r.randint(-5, 5)
    c = r.randint(-8, 8)
    fx = a * x**2 + b * x + c

    f_xh = a * (x + h)**2 + b * (x + h) + c
    expanded_f_xh = sp.expand(f_xh)
    diff_expr = sp.expand(f_xh - fx)
    factored_num = h * (2 * a * x + a * h + b)
    quotient = sp.cancel(diff_expr / h)
    deriv = 2 * a * x + b

    steps = [
        step(
            from_latex=r"f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}",
            to_latex_str=rf"f'(x) = \lim_{{h \to 0}} \frac{{{to_latex(f_xh)} - ({to_latex(fx)})}}{{h}}",
            op="substitute into definition formula",
            rule="definition of derivative",
        ),
        step(
            from_latex=rf"\lim_{{h \to 0}} \frac{{{to_latex(f_xh)} - ({to_latex(fx)})}}{{h}}",
            to_latex_str=rf"\lim_{{h \to 0}} \frac{{{to_latex(diff_expr)}}}{{h}}",
            op="expand binomial and distribute negative sign in numerator",
            rule="algebraic expansion",
            common_errors=["sign_error_distribution", "incorrect_binomial_expansion"],
        ),
        step(
            from_latex=rf"\lim_{{h \to 0}} \frac{{{to_latex(diff_expr)}}}{{h}}",
            to_latex_str=rf"\lim_{{h \to 0}} \frac{{{to_latex(factored_num)}}}{{h}}",
            op="factor out common factor h from numerator",
            rule="common factorisation",
            common_errors=["cancelling_h_before_factoring"],
        ),
        step(
            from_latex=rf"\lim_{{h \to 0}} \frac{{{to_latex(factored_num)}}}{{h}}",
            to_latex_str=rf"\lim_{{h \to 0}} ({to_latex(quotient)})",
            op="divide through by h (h != 0)",
            rule="algebraic simplification",
        ),
        step(
            from_latex=rf"\lim_{{h \to 0}} ({to_latex(quotient)})",
            to_latex_str=rf"f'(x) = {to_latex(deriv)}",
            op="evaluate limit by substituting h = 0",
            rule="limit evaluation",
            common_errors=["dropped_limit_symbol_prematurely", "forgot_to_substitute_h_zero"],
        ),
    ]

    canonical = solution_graph(
        goal="differentiate quadratic function from first principles",
        steps=steps,
        final_expr=deriv,
        chain_type="expression",
        final_latex=rf"f'(x) = {to_latex(deriv)}",
    )

    marking_schema = {
        "total_marks": 5,
        "marking_points": [
            {"id": "mp1", "desc": "Statement of formula and substitution of f(x+h) - f(x)", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Algebraic expansion of f(x+h)", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Simplifying numerator to terms containing h", "marks": 1, "editable": True},
            {"id": "mp4", "desc": "Factoring out h and dividing through by h", "marks": 1, "editable": True},
            {"id": "mp5", "desc": "Final derivative value f'(x) with limit evaluated", "marks": 1, "editable": True},
        ],
        "deductions": [
            {"rule": "dropped_limit_notation_prematurely", "penalty": -1},
            {"rule": "omitted_equals_signs_or_formula", "penalty": -1},
        ],
        "carry_forward_rule": "consequential_accuracy",
    }

    sample_answer = (
        rf"f'(x) = \lim_{{h \to 0}} \frac{{f(x+h) - f(x)}}{{h}}" "\n"
        rf"= \lim_{{h \to 0}} \frac{{{to_latex(f_xh)} - ({to_latex(fx)})}}{{h}}" "\n"
        rf"= \lim_{{h \to 0}} \frac{{{to_latex(diff_expr)}}}{{h}}" "\n"
        rf"= \lim_{{h \to 0}} \frac{{{to_latex(factored_num)}}}{{h}}" "\n"
        rf"= \lim_{{h \to 0}} ({to_latex(quotient)})" "\n"
        rf"= {to_latex(deriv)}"
    )

    hints = {
        "nudge": rf"Start with the definition formula: $f'(x) = \lim_{{h \to 0}} \frac{{f(x+h) - f(x)}}{{h}}$.",
        "concept": "Expand $f(x+h)$ completely, subtract $f(x)$, then factorise $h$ out of every term in the numerator so it cancels with the denominator before setting $h=0$.",
        "breakdown": (
            rf"1. Substitute: $f(x+h) = {to_latex(f_xh)}$." "\n"
            rf"2. Subtract $f(x)$ and expand: $f(x+h) - f(x) = {to_latex(diff_expr)}$." "\n"
            rf"3. Factorise $h$: $h({to_latex(quotient)})$." "\n"
            rf"4. Divide by $h$ and evaluate $\lim_{{h \to 0}}({to_latex(quotient)}) = {to_latex(deriv)}$."
        ),
    }

    return make_math_question(
        prefix="calc_fp_cmp",
        topic=TOPIC,
        subskill="first_principles_differentiation",
        learning_objective_id=f"{LO}_first_principles",
        prompt=rf"Determine $f'(x)$ from first principles if $f(x) = {to_latex(fx)}$.",
        prompt_latex=rf"f(x) = {to_latex(fx)}",
        answer_latex=to_latex(deriv),
        answer_sympy=sp.srepr(deriv),
        sample_answer=sample_answer,
        canonical_solution=canonical,
        marking_schema=marking_schema,
        hints=hints,
        misconception_tags=["dropped_limit_symbol", "sign_error_distribution", "cancelling_h_before_factoring"],
        keywords=["first principles", "derivative", "definition of derivative", "limit", "calculus", "NSC Paper 1"],
        term=1,
        caps_weight_percent=20,
        suggested_duration_mins=7,
        mode="compound",
        difficulty=difficulty,
    )


# --------------------------------------------------------------------------- #
# Sub-Drill: Elementary Difference Quotient [f(x+h) - f(x)] / h
# --------------------------------------------------------------------------- #
def _build_difference_quotient(r, difficulty: str) -> Dict[str, Any]:
    """Elementary sub-drill: isolating the algebraic manipulation of the difference quotient
    [f(x+h) - f(x)] / h before limit evaluation.
    """
    a = nonzero(r, -3, 3)
    b = r.randint(-5, 5)
    c = r.randint(-6, 6)
    fx = a * x**2 + b * x + c

    f_xh = a * (x + h)**2 + b * (x + h) + c
    diff_expr = sp.expand(f_xh - fx)
    factored_num = h * (2 * a * x + a * h + b)
    quotient = sp.cancel(diff_expr / h)

    steps = [
        step(
            from_latex=rf"\frac{{f(x+h) - f(x)}}{{h}}",
            to_latex_str=rf"\frac{{{to_latex(f_xh)} - ({to_latex(fx)})}}{{h}}",
            op="substitute x + h into function",
            rule="function substitution",
        ),
        step(
            from_latex=rf"\frac{{{to_latex(f_xh)} - ({to_latex(fx)})}}{{h}}",
            to_latex_str=rf"\frac{{{to_latex(diff_expr)}}}{{h}}",
            op="expand and simplify numerator",
            rule="algebraic expansion",
            common_errors=["sign_error_distribution", "incorrect_binomial_expansion"],
        ),
        step(
            from_latex=rf"\frac{{{to_latex(diff_expr)}}}{{h}}",
            to_latex_str=rf"\frac{{{to_latex(factored_num)}}}{{h}}",
            op="factor out h from numerator",
            rule="factorisation",
        ),
        step(
            from_latex=rf"\frac{{{to_latex(factored_num)}}}{{h}}",
            to_latex_str=to_latex(quotient),
            op="cancel common factor h",
            rule="algebraic fraction simplification",
        ),
    ]

    canonical = solution_graph(
        goal="simplify difference quotient",
        steps=steps,
        final_expr=quotient,
        chain_type="expression",
        final_latex=to_latex(quotient),
    )

    marking_schema = {
        "total_marks": 3,
        "marking_points": [
            {"id": "mp1", "desc": "Correct substitution for f(x+h)", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Expansion and subtraction of f(x) in numerator", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Factoring out h and dividing through to reach {to_latex(quotient)}", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "sign_error_distribution", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    sample_answer = (
        rf"\frac{{f(x+h) - f(x)}}{{h}} = \frac{{{to_latex(f_xh)} - ({to_latex(fx)})}}{{h}}" "\n"
        rf"= \frac{{{to_latex(diff_expr)}}}{{h}}" "\n"
        rf"= \frac{{{to_latex(factored_num)}}}{{h}}" "\n"
        rf"= {to_latex(quotient)}"
    )

    hints = {
        "nudge": rf"First determine $f(x+h)$ by replacing $x$ with $(x+h)$, then subtract $f(x)$ and divide by $h$.",
        "concept": r"The difference quotient $\frac{f(x+h) - f(x)}{h}$ is the algebraic core of first principles before the limit is taken.",
        "breakdown": rf"$f(x+h) = {to_latex(f_xh)}$. The numerator simplifies to ${to_latex(diff_expr)}$. Factoring out $h$ gives ${to_latex(quotient)}$.",
    }

    return make_math_question(
        prefix="calc_diff_quot",
        topic=TOPIC,
        subskill="elementary_difference_quotient",
        learning_objective_id=f"{LO}_difference_quotient",
        prompt=rf"Given the function $f(x) = {to_latex(fx)}$. Determine and simplify the difference quotient $\frac{{f(x+h) - f(x)}}{{h}}$ in terms of $x$ and $h$ (where $h \neq 0$).",
        prompt_latex=rf"f(x) = {to_latex(fx)}",
        answer_latex=to_latex(quotient),
        answer_sympy=sp.srepr(quotient),
        sample_answer=sample_answer,
        canonical_solution=canonical,
        marking_schema=marking_schema,
        hints=hints,
        misconception_tags=["sign_error_distribution", "cancelling_h_before_factoring", "confused_quotient_with_limit"],
        keywords=["difference quotient", "average gradient", "first principles", "algebraic simplification"],
        term=1,
        caps_weight_percent=15,
        suggested_duration_mins=4,
        mode="elementary_difference_quotient",
        difficulty="easy" if difficulty == "easy" else "medium",
    )



# --------------------------------------------------------------------------- #
# Sub-Drill: Power Rule with Fractional / Negative Exponents
# --------------------------------------------------------------------------- #
def _build_power_rule(r, difficulty: str) -> Dict[str, Any]:
    c1 = nonzero(r, 2, 6)
    n1 = r.randint(3, 5)
    c2 = nonzero(r, 2, 8)
    
    expr = c1 * x**n1 - c2 / x**2
    standard_form = c1 * x**n1 - c2 * x**(-2)
    deriv = sp.diff(expr, x)

    steps = [
        step(
            from_latex=f"y = {to_latex(expr)}",
            to_latex_str=f"y = {c1}x^{{{n1}}} - {c2}x^{{-2}}",
            op="convert to negative exponent",
            rule="exponential laws",
        ),
        step(
            from_latex=f"\\frac{{dy}}{{dx}} = \\frac{{d}}{{dx}}({c1}x^{{{n1}}} - {c2}x^{{-2}})",
            to_latex_str=f"\\frac{{dy}}{{dx}} = {to_latex(deriv)}",
            op="apply power rule: d/dx(x^n) = n*x^(n-1)",
            rule="power rule",
            common_errors=["forgot_negative_sign_flip", "subtracted_wrong_exponent"],
        ),
    ]

    canonical = solution_graph(
        goal="determine derivative using rules",
        steps=steps,
        final_expr=deriv,
        final_latex=f"\\frac{{dy}}{{dx}} = {to_latex(deriv)}",
    )

    marking_schema = {
        "total_marks": 3,
        "marking_points": [
            {"id": "mp1", "desc": "Rewrite term as negative exponent x^(-2)", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Differentiate first term", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Differentiate second term with correct sign", "marks": 1, "editable": True},
        ],
        "deductions": [],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "nudge": "Rewrite any fractions with $x$ in the denominator using negative exponents before differentiating.",
        "concept": "Apply the rule: $\\frac{d}{dx}[a x^n] = n \\cdot a x^{n-1}$. Note that subtracting 1 from $-2$ gives $-3$.",
        "breakdown": f"Rewrite as ${c1}x^{{{n1}}} - {c2}x^{{-2}}$. Differentiating gives ${to_latex(deriv)}$.",
    }

    return make_math_question(
        prefix="calc_pwr",
        topic=TOPIC,
        subskill="elementary_power_rule",
        learning_objective_id=f"{LO}_power_rule",
        prompt=f"Determine $\\frac{{dy}}{{dx}}$ if $y = {to_latex(expr)}$. Leave your answer with positive exponents where applicable.",
        prompt_latex=f"y = {to_latex(expr)}",
        answer_latex=to_latex(deriv),
        answer_sympy=sp.srepr(deriv),
        canonical_solution=canonical,
        marking_schema=marking_schema,
        hints=hints,
        misconception_tags=["negative_exponent_slip", "forgot_constant_multiplier", "incorrect_power_reduction"],
        keywords=["power rule", "differentiation", "negative exponents"],
        mode="elementary_power_rule",
        difficulty="medium",
    )


# --------------------------------------------------------------------------- #
# Sub-Drill: Tangent Line Equation
# --------------------------------------------------------------------------- #
def _build_tangent_line(r, difficulty: str) -> Dict[str, Any]:
    a = nonzero(r, 1, 2)
    b = nonzero(r, -4, 4)
    c = r.randint(-5, 5)
    f = a * x**2 + b * x + c
    x0 = r.randint(-2, 3)
    y0 = f.subs(x, x0)

    f_prime = sp.diff(f, x)
    m = f_prime.subs(x, x0)
    c_tan = y0 - m * x0
    tangent_eq = m * x + c_tan

    steps = [
        step(
            from_latex=f"f'(x) = \\frac{{d}}{{dx}}({to_latex(f)})",
            to_latex_str=f"f'(x) = {to_latex(f_prime)}",
            op="find derivative",
            rule="power rule",
        ),
        step(
            from_latex=f"m = f'({x0})",
            to_latex_str=f"m = {m}",
            op="substitute x0 to find gradient",
            rule="gradient of tangent",
        ),
        step(
            from_latex=f"y - y_1 = m(x - x_1)",
            to_latex_str=f"y - ({y0}) = {m}(x - ({x0})) \\implies y = {to_latex(tangent_eq)}",
            op="form equation of straight line",
            rule="point-slope formula",
        ),
    ]

    canonical = solution_graph(
        goal="determine equation of tangent",
        steps=steps,
        final_expr=tangent_eq,
        final_latex=f"y = {to_latex(tangent_eq)}",
    )

    marking_schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": "Derivative f'(x)", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Gradient m = f'(x_0)", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Substitution into straight line equation", "marks": 1, "editable": True},
            {"id": "mp4", "desc": "Final tangent equation y = mx + c", "marks": 1, "editable": True},
        ],
        "deductions": [],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "nudge": "The gradient of the tangent at a given point is equal to the derivative evaluated at that $x$-coordinate.",
        "concept": "Calculate $m = f'(x_0)$, find $y_0 = f(x_0)$, then substitute into $y - y_0 = m(x - x_0)$.",
        "breakdown": f"Derivative is $f'(x) = {to_latex(f_prime)}$. At $x = {x0}$, $m = {m}$. Since $(x_0, y_0) = ({x0}, {y0})$, the tangent is $y = {to_latex(tangent_eq)}$.",
    }

    return make_math_question(
        prefix="calc_tan",
        topic=TOPIC,
        subskill="elementary_tangent_line",
        learning_objective_id=f"{LO}_tangent_line",
        prompt=f"Determine the equation of the tangent to the curve $f(x) = {to_latex(f)}$ at the point where $x = {x0}$.",
        prompt_latex=f"f(x) = {to_latex(f)},\\quad x = {x0}",
        answer_latex=f"y = {to_latex(tangent_eq)}",
        answer_sympy=sp.srepr(tangent_eq),
        canonical_solution=canonical,
        marking_schema=marking_schema,
        hints=hints,
        misconception_tags=["confused_curve_y_with_gradient", "sign_error_tangent_c"],
        keywords=["tangent line", "gradient", "point-slope", "derivative"],
        mode="elementary_tangent_line",
        difficulty="medium",
    )


# --------------------------------------------------------------------------- #
# Compound Level 3 & 4 Exam Question: Cubic Curve Analysis
# --------------------------------------------------------------------------- #
def _build_cubic_compound(r, difficulty: str) -> Dict[str, Any]:
    # Design cubic with clean integer stationary points
    # f'(x) = 3(x - r1)(x - r2) = 3x^2 - 3(r1+r2)x + 3*r1*r2
    r1 = nonzero(r, -3, 0)
    r2 = nonzero(r, 1, 4, exclude=[r1])
    if r1 > r2:
        r1, r2 = r2, r1
    
    # f(x) = x^3 - 3/2*(r1+r2)x^2 + 3*r1*r2*x + d
    # To ensure integer coefficients, let's pick r1, r2 such that r1 + r2 is even
    if (r1 + r2) % 2 != 0:
        r2 += 1

    b = -3 * (r1 + r2) // 2
    c = 3 * r1 * r2
    d = r.randint(-6, 6)
    fx = x**3 + b * x**2 + c * x + d

    f_prime = sp.diff(fx, x)
    f_double_prime = sp.diff(f_prime, x)

    # Stationary points
    y1 = fx.subs(x, r1)
    y2 = fx.subs(x, r2)
    # Inflection point
    x_infl = sp.Rational(r1 + r2, 2)
    y_infl = fx.subs(x, x_infl)

    steps = [
        step(
            from_latex=f"f(x) = {to_latex(fx)}",
            to_latex_str=f"f'(x) = {to_latex(f_prime)}",
            op="differentiate f(x)",
            rule="power rule",
        ),
        step(
            from_latex=f"f'(x) = 0 \\implies {to_latex(f_prime)} = 0",
            to_latex_str=f"3(x - ({r1}))(x - ({r2})) = 0 \\implies x = {r1} \\quad \\text{{or}} \\quad x = {r2}",
            op="solve f'(x) = 0 for stationary points",
            rule="null factor law",
        ),
        step(
            from_latex=f"x = {r1}, x = {r2}",
            to_latex_str=f"f({r1}) = {y1} \\implies ({r1}; {y1}), \\quad f({r2}) = {y2} \\implies ({r2}; {y2})",
            op="substitute x-values into f(x) to find y-coordinates",
            rule="function evaluation",
        ),
        step(
            from_latex=f"f''(x) = {to_latex(f_double_prime)} = 0",
            to_latex_str=f"x = {to_latex(x_infl)} \\implies \\text{{Point of inflection at }} ({to_latex(x_infl)}; {to_latex(y_infl)})",
            op="find point of inflection where f''(x) = 0",
            rule="concavity change",
        ),
    ]

    canonical = solution_graph(
        goal="determine stationary points and point of inflection of cubic function",
        steps=steps,
        final_expr=f_prime,
        final_latex=f"({r1}; {y1}) \\text{{ and }} ({r2}; {y2}); \\text{{ Inflection: }} ({to_latex(x_infl)}; {to_latex(y_infl)})",
    )

    marking_schema = {
        "total_marks": 9,
        "marking_points": [
            {"id": "mp1", "desc": "Derivative f'(x) correct", "marks": 2, "editable": True},
            {"id": "mp2", "desc": "Equating f'(x) = 0 and solving for x", "marks": 2, "editable": True},
            {"id": "mp3", "desc": "Both y-coordinates calculated correctly", "marks": 2, "editable": True},
            {"id": "mp4", "desc": "Second derivative f''(x) = 0", "marks": 1, "editable": True},
            {"id": "mp5", "desc": "Inflection point coordinates (x; y)", "marks": 2, "editable": True},
        ],
        "deductions": [{"rule": "swapped_x_and_y_coordinates", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "nudge": "Find $f'(x)$ and solve $f'(x) = 0$ for the turning points. For the point of inflection, solve $f''(x) = 0$.",
        "concept": "Stationary points occur where the gradient is zero. The point of inflection occurs at the midpoint of the stationary $x$-values where concavity changes.",
        "breakdown": f"$f'(x) = {to_latex(f_prime)}$. Factoring gives roots $x = {r1}$ and $x = {r2}$. Coordinates: $({r1}; {y1})$ and $({r2}; {y2})$. Inflection point: $x = {to_latex(x_infl)}$.",
    }

    return make_math_question(
        prefix="calc_cubic",
        topic=TOPIC,
        subskill="cubic_curve_analysis",
        learning_objective_id=f"{LO}_cubic_analysis",
        prompt=(
            f"Given the cubic function $f(x) = {to_latex(fx)}$:\n\n"
            f"1. Determine the coordinates of the stationary points of $f$.\n"
            f"2. Determine the coordinates of the point of inflection of $f$.\n"
            f"3. State the values of $x$ for which the graph of $f$ is concave upwards."
        ),
        prompt_latex=f"f(x) = {to_latex(fx)}",
        answer_latex=f"\\text{{Stationary points: }} ({r1}; {y1}), ({r2}; {y2}); \\quad \\text{{Inflection: }} ({to_latex(x_infl)}; {to_latex(y_infl)}); \\quad \\text{{Concave up: }} x > {to_latex(x_infl)}",
        answer_sympy=sp.srepr(f_prime),
        canonical_solution=canonical,
        marking_schema=marking_schema,
        hints=hints,
        misconception_tags=["confused_f_prime_with_f", "omitted_y_coordinate_stationary", "incorrect_concavity_test"],
        keywords=["cubic function", "stationary points", "inflection point", "concavity", "turning points"],
        term=1,
        caps_weight_percent=25,
        suggested_duration_mins=12,
        mode="compound",
        difficulty="hard",
    )


def _build_compound(r, difficulty: str) -> Dict[str, Any]:
    """Compound Level 3 & 4 dispatcher: alternates between First Principles (5-mark)
    and Cubic Curve Analysis (9-mark) questions."""
    if r.random() < 0.5:
        return _build_first_principles_compound(r, difficulty)
    return _build_cubic_compound(r, difficulty)


# --------------------------------------------------------------------------- #
# Public Generator Dispatcher
# --------------------------------------------------------------------------- #
BUILDERS = {
    "compound": _build_compound,
    "compound_first_principles": _build_first_principles_compound,
    "first_principles": _build_first_principles_compound,
    "first_principles_differentiation": _build_first_principles_compound,
    "compound_cubic": _build_cubic_compound,
    "cubic_curve_analysis": _build_cubic_compound,
    "elementary_difference_quotient": _build_difference_quotient,
    "elementary_power_rule": _build_power_rule,
    "elementary_tangent_line": _build_tangent_line,
    "elementary_first_principles": _build_first_principles_compound,
}


def generate(
    subskill: Optional[str] = None,
    difficulty: str = "hard",
    count: int = 1,
    seed: Optional[int] = None,
    mode: str = "compound",
    **kwargs: Any,
) -> Dict[str, Any]:
    """Generates deterministic Grade 12 Differential Calculus questions."""
    base_seed = 42 if seed is None else int(seed)
    target = subskill if (subskill and subskill in BUILDERS) else mode
    builder = BUILDERS.get(target, BUILDERS.get(mode, _build_compound))

    questions = []
    for i in range(max(1, count)):
        r = rng(base_seed * 1000 + i)
        q = builder(r, difficulty)
        q["seed"] = base_seed * 1000 + i
        questions.append(q)

    return {"questions": questions}
