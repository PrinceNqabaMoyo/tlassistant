"""Grade 12 Technical Mathematics — Polynomials & Cubic Equations (Deterministic 6-Pillar Generator).
Covers Chapter 5: Identifying polynomials, division of polynomials, Remainder Theorem,
Factor Theorem, factorising cubic polynomials, and solving cubic equations.
Strictly grounded in curriculum_docs_auto/TechnicalMathematics_Gr12/Term 1/02. Polynomials.md.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional
import sympy as sp

x = sp.Symbol("x")


def _rng(seed: Optional[int] = None) -> random.Random:
    r = random.Random()
    if seed is not None:
        r.seed(int(seed))
    return r


# --------------------------------------------------------------------------- #
# Sub-Drill: Remainder Theorem
# --------------------------------------------------------------------------- #
def _build_remainder_drill(r: random.Random) -> Dict[str, Any]:
    a = r.choice([1, 2, 3])
    b = r.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])
    c = r.choice([-6, -4, -2, 2, 4, 6])
    d = r.choice([-12, -8, -6, 6, 8, 12])
    poly = a*x**3 + b*x**2 + c*x + d

    k = r.choice([-3, -2, -1, 1, 2, 3])
    divisor_sign = "-" if k > 0 else "+"
    abs_k = abs(k)
    divisor_str = f"x {divisor_sign} {abs_k}"

    rem = int(poly.subs(x, k))
    poly_latex = sp.latex(poly)

    prompt = (
        f"Given the polynomial $f(x) = {poly_latex}$.\n\n"
        f"Use the Remainder Theorem to determine the remainder when $f(x)$ is divided by $({divisor_str})$."
    )

    step_sub = f"{a}({k})^3 + ({b})({k})^2 + ({c})({k}) + ({d})"
    ans_latex = f"R = f({k}) = {rem}"

    marking_schema = {
        "total_marks": 2,
        "marking_points": [
            {"id": "mp1", "desc": rf"Correct substitution into remainder theorem: f({k}) = {step_sub}", "marks": 1, "editable": True},
            {"id": "mp2", "desc": rf"Accurate remainder evaluation: {rem}", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "divisor_sign_error", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": f"According to the Remainder Theorem, the remainder when $f(x)$ is divided by $({divisor_str})$ is given by $f({k})$.",
        "tier_2": f"Substitute $x = {k}$ into $f(x)$: $f({k}) = {a}({k})^3 + ({b})({k})^2 + ({c})({k}) + ({d})$.",
        "tier_3": f"Evaluate each term carefully: $f({k}) = {rem}$. The remainder is {rem}.",
    }

    return {
        "id": f"tech_poly_rem_{r.randint(100000, 999999)}",
        "question_id": f"tech_poly_rem_{r.randint(100000, 999999)}",
        "topic": "technical_mathematics_polynomials",
        "subskill": "remainder_theorem",
        "learning_objective_id": "techmath_poly_remainder_theorem",
        "prompt": prompt,
        "prompt_latex": prompt,
        "expected_answer": str(rem),
        "solution_steps": [
            f"Step 1: Identify divisor root: {divisor_str} = 0 \\implies x = {k}",
            f"Step 2: Apply Remainder Theorem: R = f({k})",
            f"Step 3: Substitute x = {k}: f({k}) = {step_sub}",
            f"Step 4: Evaluate: R = {rem}",
        ],
        "worked_solution": f"According to the Remainder Theorem, $R = f({k})$.\n$$f({k}) = {a}({k})^3 + ({b})({k})^2 + ({c})({k}) + ({d}) = {rem}$$\nTherefore, the remainder is ${rem}$.",
        "marks": 2,
        "term": 1,
        "caps_weight_percent": 25,
        "suggested_duration_mins": 4,
        "mode": "elementary_remainder",
        "modality": "symbolic",
        "solution_type": "integer",
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["sign_error_divisor", "order_of_operations_exponent"],
    }


# --------------------------------------------------------------------------- #
# Sub-Drill: Unknown Coefficient via Factor Theorem
# --------------------------------------------------------------------------- #
def _build_unknown_coeff_drill(r: random.Random) -> Dict[str, Any]:
    k = r.choice([-2, -1, 1, 2, 3])
    r2 = r.choice([-3, -1, 1, 3])
    r3 = r.choice([-4, -2, 2, 4])
    
    # Construct (x - k)(x - r2)(x - r3) = x^3 - (k+r2+r3)x^2 + (k*r2 + k*r3 + r2*r3)x - k*r2*r3
    known_k = k
    # Let coeff of x be unknown 'p' or coeff of x^2 be 'k'
    c2 = -(k + r2 + r3)
    c1 = (k*r2 + k*r3 + r2*r3)
    c0 = -(k * r2 * r3)

    divisor_sign = "-" if known_k > 0 else "+"
    abs_k = abs(known_k)
    divisor_str = f"x {divisor_sign} {abs_k}"

    # Unknown parameter 'p' in place of c1
    # f(x) = x^3 + c2*x^2 + p*x + c0
    prompt = (
        f"Given $f(x) = x^3 + ({c2})x^2 + px + ({c0})$.\n\n"
        f"If $({divisor_str})$ is a factor of $f(x)$, calculate the value of $p$."
    )

    ans_val = c1
    marking_schema = {
        "total_marks": 3,
        "marking_points": [
            {"id": "mp1", "desc": rf"Factor theorem condition: f({known_k}) = 0", "marks": 1, "editable": True},
            {"id": "mp2", "desc": rf"Substitution: ({known_k})^3 + ({c2})({known_k})^2 + p({known_k}) + ({c0}) = 0", "marks": 1, "editable": True},
            {"id": "mp3", "desc": rf"Correct value of p: p = {ans_val}", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "sign_error_factor", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": f"Since $({divisor_str})$ is a factor, by the Factor Theorem, $f({known_k}) = 0$.",
        "tier_2": f"Substitute $x = {known_k}$ into $f(x)$ and set the expression equal to $0$: $({known_k})^3 + ({c2})({known_k})^2 + p({known_k}) + ({c0}) = 0$.",
        "tier_3": f"Solve the linear equation for $p$: ${known_k}p = {- (known_k**3 + c2*known_k**2 + c0)} \\implies p = {ans_val}$.",
    }

    return {
        "id": f"tech_poly_coeff_{r.randint(100000, 999999)}",
        "question_id": f"tech_poly_coeff_{r.randint(100000, 999999)}",
        "topic": "technical_mathematics_polynomials",
        "subskill": "factor_theorem_unknown_coeff",
        "learning_objective_id": "techmath_poly_factor_theorem",
        "prompt": prompt,
        "prompt_latex": prompt,
        "expected_answer": str(ans_val),
        "solution_steps": [
            f"Step 1: By Factor Theorem, if ({divisor_str}) is a factor, then f({known_k}) = 0",
            f"Step 2: ({known_k})^3 + ({c2})({known_k})^2 + p({known_k}) + ({c0}) = 0",
            f"Step 3: {known_k**3 + c2*known_k**2 + c0} + ({known_k})p = 0",
            f"Step 4: p = {ans_val}",
        ],
        "worked_solution": (
            f"By the Factor Theorem, if $({divisor_str})$ is a factor of $f(x)$, then $f({known_k}) = 0$.\n"
            f"$$({known_k})^3 + ({c2})({known_k})^2 + p({known_k}) + ({c0}) = 0$$\n"
            f"$${known_k**3 + c2*known_k**2 + c0} + {known_k}p = 0$$\n"
            f"$${known_k}p = {- (known_k**3 + c2*known_k**2 + c0)}$$\n"
            f"$$\\therefore p = {ans_val}$$"
        ),
        "marks": 3,
        "term": 1,
        "caps_weight_percent": 25,
        "suggested_duration_mins": 5,
        "mode": "elementary_coeff",
        "modality": "symbolic",
        "solution_type": "integer",
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["factor_theorem_remainder_confusion", "linear_equation_transposition_error"],
    }


# --------------------------------------------------------------------------- #
# Compound: Solving Cubic Equations
# --------------------------------------------------------------------------- #
def _build_solve_cubic_compound(r: random.Random) -> Dict[str, Any]:
    # Select 3 integer roots
    roots = r.sample([-4, -3, -2, -1, 1, 2, 3, 4], 3)
    roots.sort()
    r1, r2, r3 = roots

    # Expanded polynomial: (x - r1)(x - r2)(x - r3)
    poly = sp.expand((x - r1) * (x - r2) * (x - r3))
    poly_latex = sp.latex(poly)

    # Quadratic quotient after factoring out (x - r1): (x - r2)(x - r3)
    quad = sp.expand((x - r2) * (x - r3))
    quad_latex = sp.latex(quad)

    first_factor = f"(x - {r1})" if r1 > 0 else f"(x + {-r1})"

    prompt = (
        f"Solve for $x$ in the cubic equation:\n\n"
        f"$${poly_latex} = 0$$\n\n"
        f"Show all working, including finding the first rational root using the Factor Theorem."
    )

    roots_str = f"x = {r1} or x = {r2} or x = {r3}"

    marking_schema = {
        "total_marks": 5,
        "marking_points": [
            {"id": "mp1", "desc": rf"Testing candidate factors and establishing first root: f({r1}) = 0 \implies {first_factor} is a factor", "marks": 1, "editable": True},
            {"id": "mp2", "desc": rf"Polynomial or synthetic division to find quadratic factor: ({quad_latex})", "marks": 2, "editable": True},
            {"id": "mp3", "desc": rf"Factorisation of quadratic into linear factors: (x - {r2})(x - {r3}) = 0", "marks": 1, "editable": True},
            {"id": "mp4", "desc": rf"All three correct solutions: {roots_str}", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "omitted_two_roots", "penalty": -2}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": f"Test integer factors of the constant term. Notice that $f({r1}) = 0$, so ${first_factor}$ is a factor.",
        "tier_2": f"Divide ${poly_latex}$ by ${first_factor}$ using synthetic or long division to get the quadratic factor $({quad_latex}) = 0$.",
        "tier_3": f"Factorise $({quad_latex}) = 0$ into $(x - {r2})(x - {r3}) = 0$. Solutions are $x = {r1}$, $x = {r2}$, $x = {r3}$.",
    }

    return {
        "id": f"tech_poly_cubic_{r.randint(100000, 999999)}",
        "question_id": f"tech_poly_cubic_{r.randint(100000, 999999)}",
        "topic": "technical_mathematics_polynomials",
        "subskill": "solve_cubic_equation",
        "learning_objective_id": "techmath_poly_solve_cubic",
        "prompt": prompt,
        "prompt_latex": prompt,
        "expected_answer": roots_str,
        "solution_steps": [
            f"Step 1: Test factors of constant term. f({r1}) = 0, so {first_factor} is a factor.",
            f"Step 2: Divide {poly_latex} by {first_factor} to obtain ({quad_latex}) = 0.",
            f"Step 3: Factorise quadratic: (x - {r2})(x - {r3}) = 0.",
            f"Step 4: Solve linear factors: x = {r1} or x = {r2} or x = {r3}.",
        ],
        "worked_solution": (
            f"Let $f(x) = {poly_latex}$.\n\n"
            f"**Step 1: Factor Theorem inspection**\n"
            f"$$f({r1}) = ({r1})^3 + \\dots = 0 \\implies {first_factor} \\text{{ is a factor.}}$$\n\n"
            f"**Step 2: Division to find quadratic factor**\n"
            f"$${poly_latex} = {first_factor}({quad_latex}) = 0$$\n\n"
            f"**Step 3: Factorise quadratic factor**\n"
            f"$${first_factor}(x - {r2})(x - {r3}) = 0$$\n\n"
            f"**Step 4: Final roots**\n"
            f"$$\\therefore x = {r1} \\quad \\text{{or}} \\quad x = {r2} \\quad \\text{{or}} \\quad x = {r3}$$"
        ),
        "marks": 5,
        "term": 1,
        "caps_weight_percent": 25,
        "suggested_duration_mins": 8,
        "mode": "compound",
        "modality": "symbolic",
        "solution_type": "expression",
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["cubic_factor_omission", "synthetic_division_sign_error", "quadratic_factorisation_error"],
    }


def generate(
    subskill: Optional[str] = None,
    difficulty: Optional[str] = None,
    count: int = 1,
    seed: Optional[int] = None,
    mode: Optional[str] = None,
    **kwargs: Any,
) -> List[Dict[str, Any]]:
    """Generates deterministic questions for Grade 12 Technical Mathematics Polynomials."""
    r = _rng(seed)
    questions = []

    for _ in range(max(1, count)):
        eff_mode = (mode or "").lower()
        eff_sub = (subskill or "").lower()

        if "remainder" in eff_sub or eff_mode == "elementary_remainder":
            q = _build_remainder_drill(r)
        elif "coeff" in eff_sub or "factor" in eff_sub or eff_mode == "elementary_coeff":
            q = _build_unknown_coeff_drill(r)
        elif eff_mode == "elementary":
            q = r.choice([_build_remainder_drill(r), _build_unknown_coeff_drill(r)])
        else:
            q = _build_solve_cubic_compound(r)

        questions.append(q)

    return questions
