"""Grade 9 Mathematics — Factorisation & Algebraic Fractions (Deterministic 6-Pillar Generator).
Covers all 4 CAPS factorisation types and terminal algebraic fraction simplification (Term 2).
Supports full compound exam questions and atomic elementary sub-drills for adaptive deconstruction.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional
import sympy as sp

from app.utils.grade9_mathematics._math_common import (
    make_id,
    make_math_question,
    nonzero,
    rng,
    solution_graph,
    step,
    to_latex,
)

TOPIC = "algebraic_factorisation"
LO = "math9_factorisation"
x = sp.Symbol("x")
y = sp.Symbol("y")
a = sp.Symbol("a")
b = sp.Symbol("b")


# --------------------------------------------------------------------------- #
# Sub-Drill: Common Factor Extraction
# --------------------------------------------------------------------------- #
def _build_common_factor(r, difficulty: str) -> Dict[str, Any]:
    c = nonzero(r, 2, 6)
    p = nonzero(r, 1, 4)
    q = nonzero(r, -5, 5, exclude=[0])
    
    expr = c * p * x + c * q
    factored = c * (p * x + q)

    steps = [
        step(
            from_latex=f"{to_latex(expr)}",
            to_latex_str=f"{c}({to_latex(p * x + q)})",
            op=f"factor out common factor {c}",
            rule="highest common factor (HCF)",
        )
    ]

    canonical = solution_graph(
        goal="factorise by extracting common factor",
        steps=steps,
        final_expr=factored,
        final_latex=to_latex(factored),
    )

    marking_schema = {
        "total_marks": 2,
        "marking_points": [
            {"id": "mp1", "desc": f"Correct common factor {c}", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Correct remaining bracket ({to_latex(p * x + q)})", "marks": 1, "editable": True},
        ],
        "deductions": [],
        "carry_forward_rule": "strict",
    }

    hints = {
        "nudge": f"Look for the largest number that divides both terms ({c * p} and {c * q}).",
        "concept": "Find the Highest Common Factor (HCF) and divide each term by it.",
        "breakdown": f"HCF is {c}. Dividing each term gives {c}({to_latex(p * x + q)}).",
    }

    return make_math_question(
        prefix="fact_cf",
        topic=TOPIC,
        subskill="elementary_common_factor",
        learning_objective_id=f"{LO}_common_factor",
        prompt=f"Factorise fully by taking out the highest common factor:\n\n$${to_latex(expr)}$$",
        prompt_latex=to_latex(expr),
        answer_latex=to_latex(factored),
        answer_sympy=sp.srepr(factored),
        canonical_solution=canonical,
        marking_schema=marking_schema,
        hints=hints,
        misconception_tags=["incomplete_common_factor", "sign_error_division"],
        keywords=["factorise", "common factor", "HCF"],
        mode="elementary_common_factor",
        difficulty="easy",
    )


# --------------------------------------------------------------------------- #
# Sub-Drill: Difference of Two Squares
# --------------------------------------------------------------------------- #
def _build_diff_squares(r, difficulty: str) -> Dict[str, Any]:
    n1 = r.choice([1, 2, 3, 4, 5])
    n2 = nonzero(r, 1, 9, exclude=[n1])
    
    expr = (n1 * x)**2 - n2**2
    factored = (n1 * x - n2) * (n1 * x + n2)

    steps = [
        step(
            from_latex=f"{to_latex(expr)}",
            to_latex_str=f"({n1}x)^2 - ({n2})^2",
            op="identify square roots of both terms",
            rule="difference of two squares",
        ),
        step(
            from_latex=f"({n1}x)^2 - ({n2})^2",
            to_latex_str=f"({n1}x - {n2})({n1}x + {n2})",
            op="factorise into conjugate binomials (a - b)(a + b)",
            rule="difference of two squares identity",
        ),
    ]

    canonical = solution_graph(
        goal="factorise difference of two squares",
        steps=steps,
        final_expr=factored,
        final_latex=to_latex(factored),
    )

    marking_schema = {
        "total_marks": 2,
        "marking_points": [
            {"id": "mp1", "desc": "First binomial factor with minus sign", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Second binomial factor with plus sign", "marks": 1, "editable": True},
        ],
        "deductions": [],
        "carry_forward_rule": "strict",
    }

    hints = {
        "nudge": "Both terms are perfect squares separated by a minus sign: $a^2 - b^2 = (a - b)(a + b)$.",
        "concept": "Take the square root of the first term and the square root of the second term.",
        "breakdown": f"\\sqrt{{{n1**2}x^2}} = {n1}x and \\sqrt{{{n2**2}}} = {n2}. Answer: $({n1}x - {n2})({n1}x + {n2})$.",
    }

    return make_math_question(
        prefix="fact_dots",
        topic=TOPIC,
        subskill="elementary_diff_squares",
        learning_objective_id=f"{LO}_diff_squares",
        prompt=f"Factorise fully:\n\n$${to_latex(expr)}$$",
        prompt_latex=to_latex(expr),
        answer_latex=to_latex(factored),
        answer_sympy=sp.srepr(factored),
        canonical_solution=canonical,
        marking_schema=marking_schema,
        hints=hints,
        misconception_tags=["forgot_plus_minus_split", "square_root_coefficient_error"],
        keywords=["difference of squares", "factorise", "conjugates"],
        mode="elementary_diff_squares",
        difficulty="easy",
    )


# --------------------------------------------------------------------------- #
# Sub-Drill: Quadratic Trinomials
# --------------------------------------------------------------------------- #
def _build_trinomial(r, difficulty: str) -> Dict[str, Any]:
    p = nonzero(r, -6, 6)
    q = nonzero(r, -6, 6)
    
    b_val = p + q
    c_val = p * q
    expr = x**2 + b_val * x + c_val
    factored = (x + p) * (x + q)

    steps = [
        step(
            from_latex=f"{to_latex(expr)}",
            to_latex_str=f"\\text{{Find factors of }} {c_val} \\text{{ that add up to }} {b_val}: ({p}) \\times ({q}) = {c_val}, \\; ({p}) + ({q}) = {b_val}",
            op="find factor pair",
            rule="trinomial factor product and sum",
        ),
        step(
            from_latex=f"{to_latex(expr)}",
            to_latex_str=f"({to_latex(x + p)})({to_latex(x + q)})",
            op="write factorised binomials",
            rule="quadratic factorisation",
        ),
    ]

    canonical = solution_graph(
        goal="factorise quadratic trinomial",
        steps=steps,
        final_expr=factored,
        final_latex=to_latex(factored),
    )

    marking_schema = {
        "total_marks": 2,
        "marking_points": [
            {"id": "mp1", "desc": f"First factor ({to_latex(x + p)})", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Second factor ({to_latex(x + q)})", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "sign_error_factors", "penalty": -1}],
        "carry_forward_rule": "strict",
    }

    hints = {
        "nudge": f"Find two numbers that multiply to give {c_val} and add together to give {b_val}.",
        "concept": "For $x^2 + bx + c$, factor pairs of $c$ must sum to $b$.",
        "breakdown": f"The factors are {p} and {q}. Factorisation: $({to_latex(x + p)})({to_latex(x + q)})$.",
    }

    return make_math_question(
        prefix="fact_tri",
        topic=TOPIC,
        subskill="elementary_trinomial",
        learning_objective_id=f"{LO}_trinomial",
        prompt=f"Factorise the quadratic trinomial fully:\n\n$${to_latex(expr)}$$",
        prompt_latex=to_latex(expr),
        answer_latex=to_latex(factored),
        answer_sympy=sp.srepr(factored),
        canonical_solution=canonical,
        marking_schema=marking_schema,
        hints=hints,
        misconception_tags=["sign_error_factors", "sum_product_confusion"],
        keywords=["trinomial", "quadratic", "factorise", "factors"],
        mode="elementary_trinomial",
        difficulty="medium",
    )


# --------------------------------------------------------------------------- #
# Sub-Drill: Grouping with Sign Change
# --------------------------------------------------------------------------- #
def _build_grouping_sign_change(r, difficulty: str) -> Dict[str, Any]:
    # a(x - y) - b(x - y) or a(x - y) + b(y - x) -> a(x - y) - b(x - y) = (x - y)(a - b)
    # Let's test the sign-change archetype: k*(x - 3) + m*(3 - x)
    k_val = nonzero(r, 2, 5)
    m_val = nonzero(r, 2, 5, exclude=[k_val])
    d_val = nonzero(r, 1, 5)

    orig_str = f"{k_val}(x - {d_val}) + {m_val}({d_val} - x)"
    sign_flipped_str = f"{k_val}(x - {d_val}) - {m_val}(x - {d_val})"
    factored_str = f"(x - {d_val})({k_val} - {m_val})"
    res_val = k_val - m_val
    final_str = f"{res_val}(x - {d_val})"

    steps = [
        step(
            from_latex=orig_str,
            to_latex_str=sign_flipped_str,
            op="take out negative sign from second bracket to create common bracket (x - d)",
            rule="sign change rule: (d - x) = -(x - d)",
        ),
        step(
            from_latex=sign_flipped_str,
            to_latex_str=f"(x - {d_val})({k_val} - {m_val}) = {final_str}",
            op="factor out common bracket (x - d)",
            rule="common binomial factor",
        ),
    ]

    canonical = solution_graph(
        goal="factorise by grouping and sign change",
        steps=steps,
        final_latex=final_str,
    )

    marking_schema = {
        "total_marks": 3,
        "marking_points": [
            {"id": "mp1", "desc": "Sign change applied to make brackets identical", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Extracting common bracket (x - {d_val})", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Simplifying remaining terms to {final_str}", "marks": 1, "editable": True},
        ],
        "deductions": [],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "nudge": f"Notice that $({d_val} - x) = -(x - {d_val})$. Change the sign in front of {m_val}.",
        "concept": "When brackets have opposite signs, take out a factor of $-1$ so the brackets become identical.",
        "breakdown": f"Rewrite as ${k_val}(x - {d_val}) - {m_val}(x - {d_val})$. Factor out $(x - {d_val})$ to get ${final_str}$.",
    }

    return make_math_question(
        prefix="fact_grp",
        topic=TOPIC,
        subskill="elementary_grouping_sign_change",
        learning_objective_id=f"{LO}_grouping_sign_change",
        prompt=f"Factorise and simplify fully by applying a sign change:\n\n$${orig_str}$$",
        prompt_latex=orig_str,
        answer_latex=final_str,
        answer_sympy=final_str,
        canonical_solution=canonical,
        marking_schema=marking_schema,
        hints=hints,
        misconception_tags=["forgot_to_change_sign_outside", "did_not_invert_terms_inside"],
        keywords=["sign change", "grouping", "factorise", "common bracket"],
        mode="elementary_grouping_sign_change",
        difficulty="medium",
    )


# --------------------------------------------------------------------------- #
# Compound Level 3 & 4 Exam Question: Multi-Factor Algebraic Fractions
# --------------------------------------------------------------------------- #
def _build_compound_algebraic_fractions(r, difficulty: str) -> Dict[str, Any]:
    # (x^2 - a^2)/(x^2 + (a+b)x + ab) / (2x - 2a)/(x + b)
    # Numerator 1: (x - a)(x + a) = x^2 - a^2
    # Denominator 1: (x + a)(x + b) = x^2 + (a+b)x + ab
    # Numerator 2: k*(x - a)
    # Denominator 2: (x + b)
    # When divided: [(x-a)(x+a) / ((x+a)(x+b))] * [(x+b) / (k(x-a))] = 1 / k
    a_val = r.choice([2, 3, 4, 5])
    b_val = nonzero(r, 1, 6, exclude=[a_val])
    k_val = r.choice([2, 3, 4])

    num1 = x**2 - a_val**2
    den1 = x**2 + (a_val + b_val) * x + a_val * b_val
    num2 = k_val * x - k_val * a_val
    den2 = x + b_val

    frac1_str = f"\\frac{{{to_latex(num1)}}}{{{to_latex(den1)}}}"
    frac2_str = f"\\frac{{{to_latex(num2)}}}{{{to_latex(den2)}}}"
    expr_str = f"{frac1_str} \\div {frac2_str}"

    num1_fact = f"(x - {a_val})(x + {a_val})"
    den1_fact = f"(x + {a_val})(x + {b_val})"
    num2_fact = f"{k_val}(x - {a_val})"

    inverted_str = f"\\frac{{{num1_fact}}}{{{den1_fact}}} \\times \\frac{{{to_latex(den2)}}}{{{num2_fact}}}"
    final_ans = f"\\frac{{1}}{{{k_val}}}"

    steps = [
        step(
            from_latex=expr_str,
            to_latex_str=f"\\frac{{{num1_fact}}}{{{den1_fact}}} \\div \\frac{{{num2_fact}}}{{{to_latex(den2)}}}",
            op="factorise all numerators and denominators (difference of squares, trinomial, common factor)",
            rule="factorisation before simplification",
        ),
        step(
            from_latex=f"\\frac{{{num1_fact}}}{{{den1_fact}}} \\div \\frac{{{num2_fact}}}{{{to_latex(den2)}}}",
            to_latex_str=inverted_str,
            op="invert second fraction and change division to multiplication",
            rule="fraction division rule (multiply by reciprocal)",
        ),
        step(
            from_latex=inverted_str,
            to_latex_str=final_ans,
            op="cancel identical binomial factors: (x - a), (x + a), (x + b)",
            rule="algebraic fraction cancellation",
        ),
    ]

    canonical = solution_graph(
        goal="simplify complex algebraic fraction division",
        steps=steps,
        final_latex=final_ans,
    )

    marking_schema = {
        "total_marks": 6,
        "marking_points": [
            {"id": "mp1", "desc": f"Factorise numerator 1 as difference of squares: {num1_fact}", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Factorise denominator 1 as trinomial: {den1_fact}", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Factorise numerator 2 with common factor: {num2_fact}", "marks": 1, "editable": True},
            {"id": "mp4", "desc": "Invert fraction and change division to multiplication", "marks": 1, "editable": True},
            {"id": "mp5", "desc": "Cancelling identical binomial factors", "marks": 1, "editable": True},
            {"id": "mp6", "desc": f"Final simplified value: {final_ans}", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "cancelled_terms_before_factoring", "penalty": -2}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "nudge": "Do NOT try to cancel individual terms! Factorise each numerator and denominator completely first.",
        "concept": "Change the division sign $\\div$ to $\\times$ and flip the second fraction (reciprocal), then cancel common binomial brackets.",
        "breakdown": f"Numerator 1 = ${num1_fact}$. Denominator 1 = ${den1_fact}$. Inverted second fraction = $\\frac{{{to_latex(den2)}}}{{{num2_fact}}}$. All brackets cancel, leaving ${final_ans}$.",
    }

    return make_math_question(
        prefix="fact_frac_compound",
        topic=TOPIC,
        subskill="algebraic_fractions_compound",
        learning_objective_id=f"{LO}_algebraic_fractions",
        prompt=f"Simplify the following algebraic expression fully. Show all factorisation steps:\n\n$${expr_str}$$",
        prompt_latex=expr_str,
        answer_latex=final_ans,
        answer_sympy=f"1/{k_val}",
        canonical_solution=canonical,
        marking_schema=marking_schema,
        hints=hints,
        misconception_tags=["cancelled_terms_before_factoring", "forgot_to_invert_divisor", "trinomial_sign_slip"],
        keywords=["algebraic fractions", "factorise", "simplify", "difference of squares", "trinomial"],
        term=2,
        caps_weight_percent=30,
        suggested_duration_mins=10,
        mode="compound",
        difficulty="hard",
    )


# --------------------------------------------------------------------------- #
# Public Dispatcher
# --------------------------------------------------------------------------- #
BUILDERS = {
    "compound": _build_compound_algebraic_fractions,
    "elementary_common_factor": _build_common_factor,
    "elementary_diff_squares": _build_diff_squares,
    "elementary_trinomial": _build_trinomial,
    "elementary_grouping_sign_change": _build_grouping_sign_change,
}


def generate(
    subskill: Optional[str] = None,
    difficulty: str = "hard",
    count: int = 1,
    seed: Optional[int] = None,
    mode: str = "compound",
    **kwargs: Any,
) -> Dict[str, Any]:
    """Generates deterministic Grade 9 Factorisation and Algebraic Fraction questions."""
    base_seed = 42 if seed is None else int(seed)
    chosen_mode = mode if mode in BUILDERS else ("compound" if subskill is None else subskill)
    builder = BUILDERS.get(chosen_mode, _build_compound_algebraic_fractions)

    questions = []
    for i in range(max(1, count)):
        r = rng(base_seed * 1000 + i)
        q = builder(r, difficulty)
        q["seed"] = base_seed * 1000 + i
        questions.append(q)

    return {"questions": questions}
