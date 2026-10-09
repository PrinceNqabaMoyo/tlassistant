"""Grade 8 Mathematics — Algebraic Expressions & Equations (Deterministic 6-Pillar Generator).
Authentic CAPS exam generator covering:
- Distributive law expansion: -a(bx - c) = -abx + ac.
- Combining like terms in multi-term polynomial expressions.
- Solving linear equations with the variable on both sides: ax + b = cx + d.
- Substitution of negative integers into polynomial expressions.
Zero-Meta-Curriculum Invariant strictly enforced.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


def _rng(seed: Optional[int] = None) -> random.Random:
    r = random.Random()
    if seed is not None:
        r.seed(int(seed))
    return r


TOPIC = "grade8_math_algebra"
LO = "g8_math_algebra"


def generate_linear_equation(r: random.Random, mode: str = "compound") -> Dict[str, Any]:
    # Form: a*x + b = c*x + d
    # Choose integer solution x first
    x_sol = r.choice([-6, -5, -4, -3, -2, -1, 2, 3, 4, 5, 6, 7])
    a = r.randint(3, 7)
    c = r.randint(1, a - 1)  # ensure a != c
    diff_coeff = a - c       # positive
    
    # Choose b, then compute d
    b = r.randint(-9, 9)
    # a*x_sol + b = c*x_sol + d  =>  d = (a - c)*x_sol + b
    d = diff_coeff * x_sol + b
    
    b_str = f"+ {b}" if b >= 0 else f"- {abs(b)}"
    d_str = f"+ {d}" if d >= 0 else f"- {abs(d)}"
    
    prompt = (
        f"Solve the following linear equation for \\(x\\), showing all algebraic inverse operations:\n\n"
        f"\\[{a}x {b_str} = {c}x {d_str}\\]\n\n"
        f"1. Collect the variable terms on the left-hand side and the constant terms on the right-hand side.\n"
        f"2. Simplify both sides.\n"
        f"3. Divide by the coefficient of \\(x\\) to find the solution."
    )
    prompt_latex = (
        rf"\text{{Solve for }} x\text{{: }} \quad {a}x {b_str} = {c}x {d_str}"
    )
    
    const_rhs = d - b
    answer_latex = (
        rf"{a}x - {c}x = {d} - ({b})" "\n"
        rf"{diff_coeff}x = {const_rhs}" "\n"
        rf"x = \frac{{{const_rhs}}}{{{diff_coeff}}} = {x_sol}"
    )
    sample_answer = (
        f"Step 1: Subtract {c}x from both sides and subtract {b} from both sides:\n"
        f"   {a}x - {c}x = {d} - ({b})\n"
        f"Step 2: Simplify both sides:\n"
        f"   {diff_coeff}x = {const_rhs}\n"
        f"Step 3: Divide both sides by {diff_coeff}:\n"
        f"   x = {const_rhs} / {diff_coeff} = {x_sol}."
    )
    schema = {
        "total_marks": 3,
        "marking_points": [
            {"id": "mp1", "desc": f"Group variable and constant terms: {a}x - {c}x = {d} - ({b})", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Simplify both sides: {diff_coeff}x = {const_rhs}", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Divide to obtain accurate solution x = {x_sol}", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "sign_error_transposition", "penalty": 1}],
        "carry_forward_rule": "consequential_accuracy",
    }
    hints = {
        "tier_1": f"Move the {c}x term to the left by subtracting {c}x from both sides, and move the constant term to the right.",
        "tier_2": f"Collect like terms: ({a} - {c})x = {diff_coeff}x on the left, and {d} - ({b}) = {const_rhs} on the right.",
        "tier_3": f"{diff_coeff}x = {const_rhs}. Divide both sides by {diff_coeff}: x = {const_rhs} / {diff_coeff} = {x_sol}.",
    }
    return {
        "id": f"g8_alg_eq_{random.randint(100000, 999999)}",
        "topic": TOPIC,
        "subskill": "linear_equations_variables_both_sides",
        "learning_objective_id": f"{LO}_linear_equations",
        "prompt": prompt,
        "prompt_latex": prompt_latex,
        "answer_latex": answer_latex,
        "sample_answer": sample_answer,
        "marking_schema": schema,
        "hints": hints,
        "misconception_tags": ["sign_error_transposition", "division_by_wrong_coefficient"],
        "keywords": ["linear equation", "algebra", "solve for x", "inverse operations"],
        "term": 2,
        "caps_weight_percent": 18,
        "suggested_duration_mins": 5,
        "mode": mode,
        "difficulty": "medium",
        "marks": 3,
    }


def generate_distributive_expansion(r: random.Random, mode: str = "compound") -> Dict[str, Any]:
    k = r.choice([-5, -4, -3, -2])
    m = r.choice([2, 3, 4])
    n = r.choice([-7, -6, -5, -4, 4, 5, 6, 7])
    
    # Expression: k * (m*x + n) - (p*x - q)
    p = r.choice([2, 3, 5])
    q = r.choice([-4, -3, 3, 4])
    
    # k(mx + n) - (px + q)
    # k*m*x + k*n - p*x - q
    term1_x = k * m
    term1_c = k * n
    
    final_x = term1_x - p
    final_c = term1_c - q
    
    n_str = f"+ {n}" if n >= 0 else f"- {abs(n)}"
    q_str = f"+ {q}" if q >= 0 else f"- {abs(q)}"
    final_c_str = f"+ {final_c}" if final_c >= 0 else f"- {abs(final_c)}"
    
    prompt = (
        f"Simplify the following algebraic expression fully by expanding brackets and collecting like terms:\n\n"
        f"\\[{k}({m}x {n_str}) - ({p}x {q_str})\\]\n\n"
        f"1. Multiply each term inside the first bracket by \\({k}\\).\n"
        f"2. Distribute the negative sign across the second bracket: \\(-({p}x {q_str})\\).\n"
        f"3. Group and combine like terms to write the simplified expression in standard polynomial form."
    )
    prompt_latex = (
        rf"\text{{Simplify: }} \quad {k}({m}x {n_str}) - ({p}x {q_str})"
    )
    answer_latex = (
        rf"= {term1_x}x + ({term1_c}) - {p}x - ({q})" "\n"
        rf"= ({term1_x} - {p})x + ({term1_c} - {q})" "\n"
        rf"= {final_x}x {final_c_str}"
    )
    sample_answer = (
        f"Step 1: Distribute {k} into the first bracket: {k} x {m}x = {term1_x}x, and {k} x ({n}) = {term1_c}.\n"
        f"Step 2: Distribute negative sign into the second bracket: -({p}x) = -{p}x, and -({q}) = {-q}.\n"
        f"Step 3: Combine like terms:\n"
        f"   x-terms: {term1_x}x - {p}x = {final_x}x\n"
        f"   constants: {term1_c} - ({q}) = {final_c}\n"
        f"Final simplified expression: {final_x}x {final_c_str}."
    )
    schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": f"Correct expansion of first bracket: {term1_x}x + ({term1_c})", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Correct distribution of negative sign into second bracket: -{p}x - ({q})", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Group like terms: ({term1_x} - {p})x and constants", "marks": 1, "editable": True},
            {"id": "mp4", "desc": f"Final simplified expression: {final_x}x {final_c_str}", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "sign_error_distributing_negative", "penalty": 1}],
        "carry_forward_rule": "consequential_accuracy",
    }
    hints = {
        "tier_1": "Be careful when multiplying a negative number outside the bracket into each term inside. Remember: negative x negative = positive.",
        "tier_2": f"Distribute {k}: {k}({m}x) = {term1_x}x and {k}({n}) = {term1_c}. Also distribute the negative sign: -({p}x) = -{p}x and -({q}) = {-q}.",
        "tier_3": f"{term1_x}x + {term1_c} - {p}x - ({q}) = ({term1_x} - {p})x + ({term1_c} - {q}) = {final_x}x {final_c_str}.",
    }
    return {
        "id": f"g8_alg_exp_{random.randint(100000, 999999)}",
        "topic": TOPIC,
        "subskill": "distributive_law_and_collecting_like_terms",
        "learning_objective_id": f"{LO}_distributive_law",
        "prompt": prompt,
        "prompt_latex": prompt_latex,
        "answer_latex": answer_latex,
        "sample_answer": sample_answer,
        "marking_schema": schema,
        "hints": hints,
        "misconception_tags": ["sign_error_distributing_negative", "combining_unlike_terms"],
        "keywords": ["distributive law", "algebraic expressions", "like terms", "simplification"],
        "term": 2,
        "caps_weight_percent": 18,
        "suggested_duration_mins": 5,
        "mode": mode,
        "difficulty": "medium",
        "marks": 4,
    }


def generate(seed: Optional[int] = None, mode: str = "compound", archetype: Optional[str] = None) -> Dict[str, Any]:
    r = _rng(seed)
    if archetype == "equation":
        return generate_linear_equation(r, mode=mode)
    elif archetype == "expansion" or archetype == "distributive":
        return generate_distributive_expansion(r, mode=mode)
    else:
        choice = r.choice(["equation", "expansion"])
        if choice == "equation":
            return generate_linear_equation(r, mode=mode)
        else:
            return generate_distributive_expansion(r, mode=mode)
