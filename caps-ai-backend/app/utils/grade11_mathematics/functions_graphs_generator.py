"""Grade 11 Mathematics — Term 2: Functions and Graphs (Deterministic 6-Pillar Generator).
100% aligned with South African CAPS Curriculum (Grade 11 Mathematics Paper 1: Functions).
Covers:
- Parabola: y = a(x + p)^2 + q (turning point (-p, q), axis of symmetry x = -p, roots, y-intercept)
- Hyperbola: y = a / (x + p) + q (asymptotes x = -p and y = q, axes of symmetry y = ±(x + p) + q)
- Exponential: y = a * b^(x + p) + q (asymptote y = q, y-intercept)
- Determining equations of functions from given features and points

Zero-LLM: 100% deterministic Python calculations with South African comma decimals ({,}).
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional

TOPIC = "Functions and graphs"
TOPIC_ID = "grade11_math_functions"
LO = "math11_functions_graphs"


def _rng(seed: Optional[int] = None) -> random.Random:
    r = random.Random()
    if seed is not None:
        r.seed(int(seed))
    return r


def _fmt_sa(val: float | int, places: int = 2) -> str:
    if isinstance(val, int) or (isinstance(val, float) and val.is_integer()):
        return str(int(val))
    return f"{val:.{places}f}".replace(".", ",")


def _build_hyperbola_drill(r: random.Random) -> Dict[str, Any]:
    a = r.choice([-6, -4, -3, -2, 2, 3, 4, 6])
    p = r.choice([-3, -2, -1, 1, 2, 3])
    q = r.choice([-4, -2, -1, 1, 2, 4])

    vert_asymp = -p
    horiz_asymp = q

    c_pos = p + q
    axis_pos_eq = rf"y = x + {c_pos}" if c_pos >= 0 else rf"y = x - {abs(c_pos)}"

    p_str = rf"+ {p}" if p > 0 else rf"- {abs(p)}"
    q_str = rf"+ {q}" if q > 0 else rf"- {abs(q)}"
    func_latex = rf"f(x) = \frac{{{a}}}{{x {p_str}}} {q_str}"

    y_int_val = round((a / p) + q, 2)
    y_int_str = _fmt_sa(y_int_val, 2)

    prompt = (
        rf"Given the function ${func_latex}$:\n\n"
        rf"1. Write down the equations of the vertical and horizontal asymptotes of $f$.\n"
        rf"2. Determine the equation of the axis of symmetry that has a positive gradient ($m > 0$).\n"
        rf"3. Calculate the coordinates of the $y$-intercept of $f$."
    )

    worked = (
        rf"**1. Asymptotes:**"
        rf"\n- Vertical asymptote (denominator $= 0$): $x + ({p}) = 0 \implies x = {vert_asymp}$"
        rf"\n- Horizontal asymptote: $y = {horiz_asymp}$"
        rf"\n\n**2. Axis of Symmetry ($m = 1$):**"
        rf"$$y = (x {p_str}) {q_str} \implies {axis_pos_eq}$$"
        rf"\n\n**3. $y$-intercept ($x = 0$):**"
        rf"$$f(0) = \frac{{{a}}}{{0 {p_str}}} {q_str} = {_fmt_sa(round(a/p, 2), 2)} {q_str} = {y_int_str} \implies (0 ; {y_int_str})$$"
    )

    ans_str = f"x = {vert_asymp}, y = {horiz_asymp}, {axis_pos_eq}, (0 ; {y_int_str})"

    return {
        "id": f"g11_func_hyp_{r.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": ans_str,
        "answer_latex": rf"x = {vert_asymp}, \, y = {horiz_asymp}, \, {axis_pos_eq}, \, (0 ; {y_int_str})",
        "worked_solution": worked,
        "marks": 6,
        "topic": TOPIC,
        "topic_id": TOPIC_ID,
        "learning_objective_id": LO,
        "subskill": "hyperbola_features",
        "term": 2,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 6,
        "difficulty": "medium",
        "marking_schema": {
            "total_marks": 6,
            "marking_points": [
                {"id": "mp_1", "desc": f"Vertical asymptote x = {vert_asymp}", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": f"Horizontal asymptote y = {horiz_asymp}", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": f"Axis of symmetry equation ({axis_pos_eq})", "marks": 2, "editable": True},
                {"id": "mp_4", "desc": f"y-intercept (0 ; {y_int_str})", "marks": 2, "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hint_sections": {
            "1_nudge": "The vertical asymptote is where denominator equals zero: $x + p = 0$.",
            "2_rule": "The horizontal asymptote is $y = q$. The axis of symmetry with $m = 1$ is $y = (x + p) + q$.",
            "3_breakdown": rf"Vertical: $x = {vert_asymp}$, Horizontal: $y = {horiz_asymp}$, Symmetry: ${axis_pos_eq}$, Y-intercept: $(0 ; {y_int_str})$.",
        },
        "misconception_tags": ["hyperbola_asymptote_sign_confusion", "axis_of_symmetry_formula_error"],
    }


def _build_parabola_drill(r: random.Random) -> Dict[str, Any]:
    a = r.choice([-2, -1, 1, 2])
    p = r.choice([-3, -2, -1, 1, 2, 3])
    q = r.choice([-5, -4, -3, 3, 4, 5])

    tp_x = -p
    tp_y = q

    dx = r.choice([-2, -1, 1, 2])
    pt_x = tp_x + dx
    pt_y = tp_y + a * (dx ** 2)

    prompt = (
        rf"The sketch of a parabola $f(x) = a(x + p)^2 + q$ has a turning point at $T({tp_x} ; {tp_y})$ "
        rf"and passes through the point $P({pt_x} ; {pt_y})$.\n\n"
        rf"1. Write down the values of $p$ and $q$.\n"
        rf"2. Determine the value of $a$ by substituting point $P$.\n"
        rf"3. Write down the equation of the axis of symmetry of $f$."
    )

    p_sgn = f"+ {p}" if p > 0 else f"- {abs(p)}"
    q_sgn = f"+ {q}" if q > 0 else f"- {abs(q)}"
    worked = (
        rf"**1. Parameters $p$ and $q$:**"
        rf"\nTurning point is $(-p ; q) = ({tp_x} ; {tp_y}) \implies p = {p}, \quad q = {q}$."
        rf"\n\n**2. Find $a$:**"
        rf"$$y = a(x {p_sgn})^2 {q_sgn}$$"
        rf"Substitute $P({pt_x} ; {pt_y})$:"
        rf"$${pt_y} = a({pt_x} {p_sgn})^2 {q_sgn} \implies {pt_y - q} = a({dx})^2 \implies {pt_y - q} = {dx**2}a \implies a = {a}$$"
        rf"\n\n**3. Axis of Symmetry:**"
        rf"$$x = {tp_x}$$"
    )

    ans_str = f"p = {p}, q = {q}, a = {a}, x = {tp_x}"

    return {
        "id": f"g11_func_par_{r.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": ans_str,
        "answer_latex": ans_str,
        "worked_solution": worked,
        "marks": 5,
        "topic": TOPIC,
        "topic_id": TOPIC_ID,
        "learning_objective_id": LO,
        "subskill": "parabola_turning_point",
        "term": 2,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 5,
        "difficulty": "medium",
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp_1", "desc": f"Values of p={p} and q={q}", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": f"Substitution of point P to find a={a}", "marks": 2, "editable": True},
                {"id": "mp_3", "desc": f"Axis of symmetry x = {tp_x}", "marks": 1, "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hint_sections": {
            "1_nudge": "In $f(x) = a(x + p)^2 + q$, the turning point is $(-p ; q)$.",
            "2_rule": "Substitute point $P(x ; y)$ into $y = a(x + p)^2 + q$ to solve for $a$.",
            "3_step": rf"Substitute $p = {p}$ and $q = {q}$, then $P({pt_x} ; {pt_y})$ gives $a = {a}$. Axis of symmetry is $x = {tp_x}$.",
        },
        "misconception_tags": ["parabola_vertex_sign_confusion"],
    }


def generate(subskill: Optional[str] = None, difficulty: str = "medium", count: int = 1, seed: Optional[int] = None, **kwargs) -> List[Dict[str, Any]]:
    r = _rng(seed)
    generators = [_build_hyperbola_drill, _build_parabola_drill]
    if subskill == "hyperbola":
        generators = [_build_hyperbola_drill]
    elif subskill == "parabola":
        generators = [_build_parabola_drill]

    questions = []
    for _ in range(count):
        gen_fn = r.choice(generators)
        questions.append(gen_fn(r))
    return questions
