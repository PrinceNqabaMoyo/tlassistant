"""Grade 10 Mathematics - Term 2 - Analytical Geometry (deterministic, SymPy-backed).

Curriculum source: CAPS Grade 10 Mathematics Term 2 - Analytical Geometry.
Implements the 6-pillar universal generator contract:
  1. Term & Calendar Metadata (term=2, caps_weight_percent=15, duration=8)
  2. Deconstructibility (mode="compound" | "elementary_distance" | "elementary_midpoint" | "elementary_gradient" | "elementary_parallel_perpendicular")
  3. Standardized Misconception Taxonomy (formula_swap, sign_error_subtraction, inversion_dx_dy, forgot_square_root)
  4. Teacher-Editable Marking Schema
  5. Deterministic 3-Tier Pre-baked Hints (Zero-LLM)
  6. Modality-Appropriate Representation (SymPy symbolic, KaTeX, South African comma decimals)
"""

from __future__ import annotations

import random
from typing import Any, Dict, List, Optional
import sympy as sp

from app.utils.grade10_mathematics._math_common import (
    rng,
    make_id,
    make_short,
    make_mcq,
    to_latex_safe,
    with_metadata,
)

TOPIC = "grade10_math_analytical_geometry"
LO = "math10_analytical_geometry"
TERM = 2
CAPS_WEIGHT = 15
SUGGESTED_DURATION = 8


# --------------------------------------------------------------------------- #
# Sub-drill 1: Distance Formula
# --------------------------------------------------------------------------- #
def _build_distance_drill(r: random.Random) -> Dict[str, Any]:
    """Calculate distance between two coordinates with integer or clean surd answers."""
    label_pairs = [("A", "B"), ("P", "Q"), ("M", "N"), ("K", "L"), ("C", "D"), ("R", "S"), ("E", "F"), ("X", "Y")]
    l1, l2 = r.choice(label_pairs)

    pairs = [
        (3, 4), (4, 3), (5, 12), (12, 5), (6, 8), (8, 6), (8, 15), (15, 8),
        (7, 24), (24, 7), (9, 12), (12, 9), (1, 2), (2, 1), (1, 3), (3, 1), (2, 3),
        (3, 2), (1, 4), (4, 1), (2, 4), (4, 2), (3, 5), (5, 3), (4, 5),
        (5, 4), (2, 5), (5, 2), (1, 5), (5, 1), (3, 6), (6, 3), (4, 7),
        (7, 4), (5, 7), (7, 5), (6, 10), (10, 6), (2, 7), (7, 2), (3, 7),
        (7, 3), (5, 8), (8, 5), (6, 9), (9, 6), (2, 9), (9, 2), (3, 8), (8, 3)
    ]
    dx, dy = r.choice(pairs)
    x1 = r.randint(-15, 15)
    y1 = r.randint(-15, 15)

    sx = r.choice([-1, 1])
    sy = r.choice([-1, 1])
    x2 = x1 + sx * dx
    y2 = y1 + sy * dy

    pt_a = f"{l1}({x1}; {y1})"
    pt_b = f"{l2}({x2}; {y2})"

    dist_squared = (x2 - x1)**2 + (y2 - y1)**2
    dist_sym = sp.sqrt(dist_squared)
    dist_latex = sp.latex(dist_sym)

    prompt = (
        f"Calculate the distance between the points ${pt_a}$ and ${pt_b}$. "
        f"Leave your answer in simplest surd form if not an integer."
    )

    t1_hint = f"Identify coordinates: $(x_1, y_1) = ({x1}; {y1})$ and $(x_2, y_2) = ({x2}; {y2})$."
    t2_hint = r"Apply the distance formula: $d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$. Take care with negative signs."
    t3_hint = (
        f"Substitute: $d = \\sqrt{{({x2} - ({x1}))^2 + ({y2} - ({y1}))^2}} "
        f"= \\sqrt{{{dx}^2 + {dy}^2}} = \\sqrt{{{dist_squared}}} = {dist_latex}$."
    )

    marking_schema = {
        "total_marks": 3,
        "marking_points": [
            {"id": "mp_dist_formula", "desc": "Correct distance formula substitution", "marks": 1, "editable": True},
            {"id": "mp_dist_arithmetic", "desc": "Simplification of differences squared", "marks": 1, "editable": True},
            {"id": "mp_dist_final", "desc": f"Accurate final distance: {dist_latex}", "marks": 1, "editable": True}
        ],
        "deductions": [
            {"rule": "forgot_square_root", "penalty": -1}
        ],
        "carry_forward_rule": "consequential_accuracy"
    }

    solution_steps = [
        {"from": f"{l1}{l2}^2 = (x_2 - x_1)^2 + (y_2 - y_1)^2", "to": f"{l1}{l2} = \\sqrt{{({x2} - ({x1}))^2 + ({y2} - ({y1}))^2}}", "rule": "distance formula substitution", "op": "substitute"},
        {"from": f"{l1}{l2} = \\sqrt{{({x2 - x1})^2 + ({y2 - y1})^2}}", "to": f"{l1}{l2} = \\sqrt{{{dist_squared}}}", "rule": "evaluate squares", "op": "simplify"},
        {"from": f"{l1}{l2} = \\sqrt{{{dist_squared}}}", "to": f"{l1}{l2} = {dist_latex}", "rule": "simplify surd", "op": "evaluate"}
    ]

    return {
        "question_id": make_id("dist"),
        "subskill": "distance_formula",
        "question_type": "math_short",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "math_short",
        "answer_latex": dist_latex,
        "answer_sympy": str(dist_sym),
        "total_marks": 3,
        "term": TERM,
        "caps_weight_percent": CAPS_WEIGHT,
        "suggested_duration_mins": 3,
        "misconception_tags": [
            "forgot_square_root",
            "sign_error_gradient_subtraction",
            "formula_swap_midpoint_vs_distance"
        ],
        "hints": [
            {"tier": 1, "title": "Focus Area", "text": t1_hint},
            {"tier": 2, "title": "Formula Rule", "text": t2_hint},
            {"tier": 3, "title": "Worked Step", "text": t3_hint}
        ],
        "marking_schema": marking_schema,
        "solution_steps": solution_steps,
        "points": {l1: [x1, y1], l2: [x2, y2]}
    }


# --------------------------------------------------------------------------- #
# Sub-drill 2: Midpoint Formula
# --------------------------------------------------------------------------- #
def _build_midpoint_drill(r: random.Random) -> Dict[str, Any]:
    """Calculate midpoint coordinates M((x1+x2)/2, (y1+y2)/2)."""
    # Pick x1, x2 and y1, y2
    x1 = r.randint(-8, 8)
    y1 = r.randint(-8, 8)
    x2 = r.randint(-8, 8)
    y2 = r.randint(-8, 8)

    mx = sp.Rational(x1 + x2, 2)
    my = sp.Rational(y1 + y2, 2)

    mx_latex = sp.latex(mx)
    my_latex = sp.latex(my)
    answer_coord = f"({mx_latex}; {my_latex})"

    pt_a = f"P({x1}; {y1})"
    pt_b = f"Q({x2}; {y2})"

    prompt = (
        f"Determine the coordinates of the midpoint $M$ of line segment $PQ$, "
        f"where ${pt_a}$ and ${pt_b}$."
    )

    t1_hint = f"Focus on points $P({x1}; {y1})$ and $Q({x2}; {y2})$."
    t2_hint = r"Recall the midpoint coordinates: $M\left(\frac{x_1 + x_2}{2}; \frac{y_1 + y_2}{2}\right)$."
    t3_hint = (
        f"Compute: $M\\left(\\frac{{{x1} + ({x2})}}{{2}}; \\frac{{{y1} + ({y2})}}{{2}}\\right) "
        f"= \\left(\\frac{{{x1+x2}}}{{2}}; \\frac{{{y1+y2}}}{{2}}\\right) = {answer_coord}$."
    )

    marking_schema = {
        "total_marks": 2,
        "marking_points": [
            {"id": "mp_mid_x", "desc": f"Correct x-coordinate: {mx_latex}", "marks": 1, "editable": True},
            {"id": "mp_mid_y", "desc": f"Correct y-coordinate: {my_latex}", "marks": 1, "editable": True}
        ],
        "deductions": [
            {"rule": "formula_swap_midpoint_vs_distance", "penalty": -1}
        ],
        "carry_forward_rule": "consequential_accuracy"
    }

    solution_steps = [
        {"from": f"M = ((x_1 + x_2)/2; (y_1 + y_2)/2)", "to": f"M = (({x1} + ({x2}))/2; ({y1} + ({y2}))/2)", "rule": "midpoint formula substitution", "op": "substitute"},
        {"from": f"M = (({x1+x2})/2; ({y1+y2})/2)", "to": f"M = {answer_coord}", "rule": "simplify coordinates", "op": "evaluate"}
    ]

    return {
        "question_id": make_id("mid"),
        "subskill": "midpoint_formula",
        "question_type": "math_short",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "math_short",
        "answer_latex": answer_coord,
        "answer_sympy": f"({mx}, {my})",
        "total_marks": 2,
        "term": TERM,
        "caps_weight_percent": CAPS_WEIGHT,
        "suggested_duration_mins": 2,
        "misconception_tags": [
            "formula_swap_midpoint_vs_distance",
            "sign_error_gradient_subtraction"
        ],
        "hints": [
            {"tier": 1, "title": "Focus Area", "text": t1_hint},
            {"tier": 2, "title": "Formula Rule", "text": t2_hint},
            {"tier": 3, "title": "Worked Step", "text": t3_hint}
        ],
        "marking_schema": marking_schema,
        "solution_steps": solution_steps,
        "points": {"P": [x1, y1], "Q": [x2, y2]}
    }


# --------------------------------------------------------------------------- #
# Sub-drill 3: Gradient Formula & Parallel/Perpendicular
# --------------------------------------------------------------------------- #
def _build_gradient_drill(r: random.Random) -> Dict[str, Any]:
    """Calculate gradient m = (y2 - y1) / (x2 - x1)."""
    x1 = r.randint(-6, 6)
    y1 = r.randint(-6, 6)
    dx = r.choice([-5, -4, -3, -2, 2, 3, 4, 5])
    dy = r.randint(-8, 8)
    x2 = x1 + dx
    y2 = y1 + dy

    m_sym = sp.Rational(dy, dx)
    m_latex = sp.latex(m_sym)

    pt_a = f"A({x1}; {y1})"
    pt_b = f"B({x2}; {y2})"

    prompt = (
        f"Calculate the gradient ($m$) of the line passing through ${pt_a}$ and ${pt_b}$. "
        f"Express as a simplified fraction or integer."
    )

    t1_hint = f"Coordinates are $(x_1, y_1) = ({x1}; {y1})$ and $(x_2, y_2) = ({x2}; {y2})$."
    t2_hint = r"Recall the gradient formula: $m = \frac{y_2 - y_1}{x_2 - x_1}$."
    t3_hint = (
        f"Substitute: $m = \\frac{{{y2} - ({y1})}}{{{x2} - ({x1})}} "
        f"= \\frac{{{dy}}}{{{dx}}} = {m_latex}$."
    )

    marking_schema = {
        "total_marks": 2,
        "marking_points": [
            {"id": "mp_grad_sub", "desc": "Correct gradient formula substitution", "marks": 1, "editable": True},
            {"id": "mp_grad_val", "desc": f"Simplified gradient: {m_latex}", "marks": 1, "editable": True}
        ],
        "deductions": [
            {"rule": "inversion_dx_dy", "penalty": -1},
            {"rule": "sign_error_gradient_subtraction", "penalty": -1}
        ],
        "carry_forward_rule": "consequential_accuracy"
    }

    solution_steps = [
        {"from": f"m = (y_2 - y_1)/(x_2 - x_1)", "to": f"m = ({y2} - ({y1}))/({x2} - ({x1}))", "rule": "gradient formula substitution", "op": "substitute"},
        {"from": f"m = ({dy})/({dx})", "to": f"m = {m_latex}", "rule": "simplify fraction", "op": "evaluate"}
    ]

    return {
        "question_id": make_id("grad"),
        "subskill": "gradient_formula",
        "question_type": "math_short",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "math_short",
        "answer_latex": m_latex,
        "answer_sympy": str(m_sym),
        "total_marks": 2,
        "term": TERM,
        "caps_weight_percent": CAPS_WEIGHT,
        "suggested_duration_mins": 2,
        "misconception_tags": [
            "inversion_dx_dy",
            "sign_error_gradient_subtraction"
        ],
        "hints": [
            {"tier": 1, "title": "Focus Area", "text": t1_hint},
            {"tier": 2, "title": "Formula Rule", "text": t2_hint},
            {"tier": 3, "title": "Worked Step", "text": t3_hint}
        ],
        "marking_schema": marking_schema,
        "solution_steps": solution_steps,
        "points": {"A": [x1, y1], "B": [x2, y2]}
    }


# --------------------------------------------------------------------------- #
# Sub-drill 4: Parallel & Perpendicular Lines (MCQ)
# --------------------------------------------------------------------------- #
def _build_parallel_perpendicular_drill(r: random.Random) -> Dict[str, Any]:
    """Test relationship between two lines using gradients m1 and m2."""
    is_perpendicular = r.choice([True, False])
    num = r.randint(1, 5)
    den = r.choice([1, 2, 3, 4])
    m1 = sp.Rational(num, den)

    if is_perpendicular:
        m2 = -sp.Rational(den, num)
        correct_rel = "perpendicular"
        explanation = (
            f"Since $m_1 \\times m_2 = ({sp.latex(m1)}) \\times ({sp.latex(m2)}) = -1$, "
            f"the lines are perpendicular."
        )
    else:
        m2 = m1
        correct_rel = "parallel"
        explanation = (
            f"Since $m_1 = m_2 = {sp.latex(m1)}$, the lines have equal gradients "
            f"and are therefore parallel."
        )

    options = ["parallel", "perpendicular", "neither parallel nor perpendicular", "coincident"]
    r.shuffle(options)
    correct_index = options.index(correct_rel)

    prompt = (
        f"Line $L_1$ has gradient $m_1 = {sp.latex(m1)}$ and line $L_2$ has gradient $m_2 = {sp.latex(m2)}$. "
        f"What is the geometric relationship between $L_1$ and $L_2$?"
    )

    t1_hint = f"Compare the gradients: $m_1 = {sp.latex(m1)}$ and $m_2 = {sp.latex(m2)}$."
    t2_hint = r"Rule: Parallel lines have $m_1 = m_2$. Perpendicular lines satisfy $m_1 \times m_2 = -1$."
    t3_hint = explanation

    marking_schema = {
        "total_marks": 2,
        "marking_points": [
            {"id": "mp_rel", "desc": f"Correct geometric classification: {correct_rel}", "marks": 2, "editable": True}
        ],
        "deductions": [],
        "carry_forward_rule": "none"
    }

    return {
        "question_id": make_id("par_perp"),
        "subskill": "parallel_perpendicular",
        "question_type": "mcq",
        "prompt": prompt,
        "prompt_latex": prompt,
        "options": options,
        "correct_index": correct_index,
        "explanation": explanation,
        "total_marks": 2,
        "term": TERM,
        "caps_weight_percent": CAPS_WEIGHT,
        "suggested_duration_mins": 2,
        "misconception_tags": [
            "parallel_perpendicular_reciprocal_confusion",
            "sign_error_gradient_subtraction"
        ],
        "hints": [
            {"tier": 1, "title": "Focus Area", "text": t1_hint},
            {"tier": 2, "title": "Formula Rule", "text": t2_hint},
            {"tier": 3, "title": "Worked Step", "text": t3_hint}
        ],
        "marking_schema": marking_schema
    }


# --------------------------------------------------------------------------- #
# Compound Generator: Multi-Step Analytical Geometry Proof
# --------------------------------------------------------------------------- #
def _build_compound_drill(r: random.Random) -> Dict[str, Any]:
    """
    Compound problem combining distance, midpoint, and gradient:
    Given vertices of a triangle ABC, determine if it is an isosceles or right-angled triangle.
    """
    # Create clean right-angled triangle or isosceles
    x_a, y_a = 0, 0
    x_b, y_b = r.choice([(4, 0), (6, 0), (8, 0)])
    x_c, y_c = 0, r.choice([(3, 0), (0, 3), (0, 4), (0, 6)])[1]
    if y_c == 0:
        y_c = r.choice([3, 4, 5])

    pt_a = f"A({x_a}; {y_a})"
    pt_b = f"B({x_b}; {y_b})"
    pt_c = f"C({x_c}; {y_c})"

    ab_sq = (x_b - x_a)**2 + (y_b - y_a)**2
    ac_sq = (x_c - x_a)**2 + (y_c - y_a)**2
    bc_sq = (x_c - x_b)**2 + (y_c - y_b)**2

    is_right = (ab_sq + ac_sq == bc_sq) or (ab_sq + bc_sq == ac_sq) or (ac_sq + bc_sq == ab_sq)
    bc_len = sp.latex(sp.sqrt(bc_sq))

    prompt = (
        f"In the Cartesian plane, points are given as ${pt_a}$, ${pt_b}$, and ${pt_c}$.\n"
        f"1. Calculate the length of segment $BC$.\n"
        f"2. Determine whether $\\triangle ABC$ is a right-angled triangle by using Pythagoras' theorem converse."
    )

    t1_hint = f"Use coordinates $B({x_b}; {y_b})$ and $C({x_c}; {y_c})$ for the length of $BC$."
    t2_hint = r"To prove right-angled: check if the sum of squares of two shorter sides equals the square of the longest side ($a^2 + b^2 = c^2$)."
    t3_hint = (
        f"$BC^2 = ({x_c} - {x_b})^2 + ({y_c} - {y_b})^2 = {bc_sq} \\implies BC = {bc_len}$. "
        f"Since $AB^2 + AC^2 = {ab_sq} + {ac_sq} = {bc_sq} = BC^2$, $\\triangle ABC$ is right-angled at $A$."
    )

    marking_schema = {
        "total_marks": 5,
        "marking_points": [
            {"id": "mp_bc_sub", "desc": "Distance formula substitution for BC", "marks": 1, "editable": True},
            {"id": "mp_bc_len", "desc": f"Correct length BC = {bc_len}", "marks": 2, "editable": True},
            {"id": "mp_pyth_converse", "desc": "Verification of AB^2 + AC^2 = BC^2", "marks": 1, "editable": True},
            {"id": "mp_conclusion", "desc": "Valid geometric conclusion (right-angled at A)", "marks": 1, "editable": True}
        ],
        "deductions": [
            {"rule": "forgot_square_root", "penalty": -1}
        ],
        "carry_forward_rule": "consequential_accuracy"
    }

    solution_steps = [
        {"from": f"BC = \\sqrt{{(x_C - x_B)^2 + (y_C - y_B)^2}}", "to": f"BC = \\sqrt{{{bc_sq}}} = {bc_len}", "rule": "distance calculation", "op": "evaluate"},
        {"from": f"AB^2 + AC^2 = {ab_sq} + {ac_sq}", "to": f"AB^2 + AC^2 = {bc_sq} = BC^2", "rule": "converse of Pythagoras", "op": "compare"}
    ]

    return {
        "question_id": make_id("compound_geom"),
        "subskill": "compound_analytical_geometry",
        "question_type": "math_steps",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "steps",
        "answer_latex": f"BC = {bc_len}; \\text{{ Right-angled at }} A",
        "total_marks": 5,
        "term": TERM,
        "caps_weight_percent": CAPS_WEIGHT,
        "suggested_duration_mins": 8,
        "misconception_tags": [
            "forgot_square_root",
            "sign_error_gradient_subtraction"
        ],
        "hints": [
            {"tier": 1, "title": "Focus Area", "text": t1_hint},
            {"tier": 2, "title": "Formula Rule", "text": t2_hint},
            {"tier": 3, "title": "Worked Step", "text": t3_hint}
        ],
        "marking_schema": marking_schema,
        "solution_steps": solution_steps,
        "points": {"A": [x_a, y_a], "B": [x_b, y_b], "C": [x_c, y_c]}
    }


# --------------------------------------------------------------------------- #
# Public Dispatcher Implementing 6-Pillar Generator Contract
# --------------------------------------------------------------------------- #
def generate_analytical_geometry_question(
    seed: Optional[int] = None,
    mode: str = "compound",
    difficulty: str = "medium",
    subskill: Optional[str] = None,
    **kwargs: Any
) -> Dict[str, Any]:
    """
    Dispatcher generating seeded, deterministic Analytical Geometry questions.
    
    Args:
        seed: Deterministic integer seed (same seed -> byte-identical output).
        mode: "compound" | "elementary_distance" | "elementary_midpoint" |
              "elementary_gradient" | "elementary_parallel_perpendicular"
        difficulty: "easy" | "medium" | "hard"
        subskill: Optional subskill key mapping to elementary drill modes.
    """
    r = rng(seed)

    effective_mode = mode
    if subskill:
        if "distance" in subskill:
            effective_mode = "elementary_distance"
        elif "midpoint" in subskill:
            effective_mode = "elementary_midpoint"
        elif "gradient" in subskill:
            effective_mode = "elementary_gradient"
        elif "parallel" in subskill or "perpendicular" in subskill:
            effective_mode = "elementary_parallel_perpendicular"
        else:
            effective_mode = subskill

    if effective_mode == "elementary_distance":
        question = _build_distance_drill(r)
    elif effective_mode == "elementary_midpoint":
        question = _build_midpoint_drill(r)
    elif mode == "elementary_gradient":
        question = _build_gradient_drill(r)
    elif mode == "elementary_parallel_perpendicular":
        question = _build_parallel_perpendicular_drill(r)
    else:
        # Default compound or random sub-drill
        generators = [
            _build_compound_drill,
            _build_distance_drill,
            _build_midpoint_drill,
            _build_gradient_drill,
            _build_parallel_perpendicular_drill
        ]
        chosen_gen = r.choice(generators)
        question = chosen_gen(r)

    # Attach shared topic and curriculum metadata
    question["topic"] = TOPIC
    question["learning_objective_id"] = LO
    question["seed"] = seed
    question["mode"] = mode
    question["difficulty"] = difficulty

    return question


# Standard 6-pillar generator contract alias
generate = generate_analytical_geometry_question
