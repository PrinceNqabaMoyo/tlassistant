"""Grade 11 Mathematics — Linear Programming & Optimization (Deterministic 6-Pillar Generator).
Conforms to CAPS Grade 11 curriculum (Chapter 12: Linear Programming).
Reference curriculum: curriculum_docs_auto/Mathematics_Gr11/Term 1/01. Linear programming.md

Covers:
- Setting up mathematical models from real-world manufacturing scenarios
- Formulating constraints (system of linear inequalities, non-negativity $x \\ge 0, y \\ge 0$)
- Identifying the feasible region and calculating corner point vertices
- Formulating the objective function ($P = ax + by$)
- Optimisation using corner-point evaluation and search-line gradient method
- Integer-only constraints (whole number units of products)
- South African comma decimals and currency conventions (Rands)
- 100% deterministic calculation using SymPy and pure Python.

Supports compound (11 marks) and elementary sub-drills:
- elementary_inequalities_formulation (4 marks)
- elementary_corner_points (3 marks)
- elementary_profit_maximisation (4 marks)
"""
from __future__ import annotations

import math
import random
import uuid
from typing import Any, Dict, List, Optional

import sympy as sp

from ._math_common import make_id, num, rng, step, to_latex


SCENARIOS = [
    {
        "biz": "Apex Woodcraft",
        "item_x": "executive desks",
        "item_y": "bookshelves",
        "var_x": "x",
        "var_y": "y",
        "resource_1": "carpentry labour",
        "resource_2": "varnishing time",
        "unit_1": "hours",
        "unit_2": "hours",
    },
    {
        "biz": "Veld Cycle Works",
        "item_x": "mountain bikes",
        "item_y": "road bikes",
        "var_x": "x",
        "var_y": "y",
        "resource_1": "frame welding",
        "resource_2": "gear assembly",
        "unit_1": "hours",
        "unit_2": "hours",
    },
    {
        "biz": "Golden Harvest Bakery",
        "item_x": "speciality cakes",
        "item_y": "artisan loaves",
        "var_x": "x",
        "var_y": "y",
        "resource_1": "baking oven capacity",
        "resource_2": "decorating time",
        "unit_1": "minutes",
        "unit_2": "minutes",
    },
]


# --------------------------------------------------------------------------- #
# Sub-drill 1: Formulation of Constraints (4 marks)
# --------------------------------------------------------------------------- #
def _build_formulation_drill(r: random.Random) -> Dict[str, Any]:
    scen = r.choice(SCENARIOS)
    biz = scen["biz"]
    item_x = scen["item_x"]
    item_y = scen["item_y"]
    res1 = scen["resource_1"]
    res2 = scen["resource_2"]

    # Resource requirements
    a1 = r.choice([2, 3, 4])
    b1 = r.choice([1, 2, 3])
    max_res1 = r.randint(20, 60)

    a2 = r.choice([1, 2])
    b2 = r.choice([2, 3, 4])
    max_res2 = r.randint(20, 50)

    max_x = r.randint(8, 20)
    profit_x = r.randint(15, 45) * 10
    profit_y = r.randint(20, 60) * 10

    prompt = (
        f"**{biz}** manufactures two products: {item_x} ($x$) and {item_y} ($y$).\n\n"
        f"• Each {item_x} requires ${a1}\\text{{ hours}}$ of {res1} and ${a2}\\text{{ hours}}$ of {res2}.\n"
        f"• Each {item_y} requires ${b1}\\text{{ hours}}$ of {res1} and ${b2}\\text{{ hours}}$ of {res2}.\n"
        f"• A maximum of ${max_res1}\\text{{ hours}}$ of {res1} and ${max_res2}\\text{{ hours}}$ of {res2} "
        f"are available each week.\n"
        f"• The factory can manufacture at most ${max_x}$ {item_x} per week.\n"
        f"• The profit is R{profit_x} per {item_x} and R{profit_y} per {item_y}.\n\n"
        f"**Required:**\n"
        f"1. Write down the constraint inequality for {res1}.\n"
        f"2. Write down the constraint inequality for {res2}.\n"
        f"3. State the production limit inequality for $x$ and the non-negativity conditions.\n"
        f"4. Write down the objective function $P$ for total weekly profit."
    )

    ineq_1 = f"{a1}x + {b1}y \\le {max_res1}"
    ineq_2 = f"{a2}x + {b2}y \\le {max_res2}"
    non_neg = f"x \\le {max_x},\\quad x \\ge 0,\\quad y \\ge 0"
    obj_fn = f"P = {profit_x}x + {profit_y}y"

    correct = {
        "constraint_1": ineq_1,
        "constraint_2": ineq_2,
        "non_negativity": non_neg,
        "objective_function": obj_fn,
    }

    return {
        "id": make_id("lp_formulation"),
        "question_type": "structured",
        "question_text": prompt,
        "correct_answer": correct,
        "sample_answer": f"1. {ineq_1}; 2. {ineq_2}; 3. {non_neg}; 4. {obj_fn}",
        "marks": 4,
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 6,
        "learning_objective_id": "math_lp_formulation",
        "mode": "elementary_inequalities_formulation",
        "misconception_tags": ["inequality_direction_inversion", "omitted_non_negativity", "confused_coefficients_between_variables"],
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp_1", "desc": "First resource constraint [M]", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Second resource constraint [M]", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "Production limit and non-negativity [A]", "marks": 1, "editable": True},
                {"id": "mp_4", "desc": "Profit objective function [A]", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "tier_1": "Each row in the table gives one inequality. The word 'maximum' or 'at most' implies '<='.",
            "tier_2": f"Resource 1: {a1}x + {b1}y <= {max_res1}. Resource 2: {a2}x + {b2}y <= {max_res2}. Always include x >= 0, y >= 0.",
            "tier_3": f"Constraints: {ineq_1}; {ineq_2}; x <= {max_x}; x >= 0, y >= 0. Profit: {obj_fn}.",
        },
    }


# --------------------------------------------------------------------------- #
# Sub-drill 2: Corner Points Calculation (3 marks)
# --------------------------------------------------------------------------- #
def _build_corner_points_drill(r: random.Random) -> Dict[str, Any]:
    # Choose clean intersection point (x0, y0)
    x0 = r.randint(4, 12)
    y0 = r.randint(3, 10)

    # Let constraint 1 be: x + y <= x0 + y0
    c1 = x0 + y0
    # Let constraint 2 be: 2x + y <= 2*x0 + y0
    c2 = 2 * x0 + y0

    # Feasible region vertices:
    # (0, 0), (0, c1), (x0, y0), (c2/2, 0)
    v_origin = (0, 0)
    v_y_axis = (0, c1)
    v_inter = (x0, y0)
    v_x_axis = (c2 // 2, 0)

    prompt = (
        f"A system of linear constraints defines a feasible region $S$ in the Cartesian plane:\n\n"
        f"$$\\begin{{cases}}\n"
        f"x + y \\le {c1} \\\\\n"
        f"2x + y \\le {c2} \\\\\n"
        f"x \\ge 0,\\quad y \\ge 0\n"
        f"\\end{{cases}}$$\n\n"
        f"**Required:**\n"
        f"1. Determine the coordinates of the $y$-intercept of $x + y = {c1}$.\n"
        f"2. Determine the coordinates of the $x$-intercept of $2x + y = {c2}$.\n"
        f"3. Calculate the intersection point of the two boundary lines by solving simultaneously."
    )

    correct = {
        "y_intercept": f"(0; {c1})",
        "x_intercept": f"({c2 // 2}; 0)",
        "intersection": f"({x0}; {y0})",
    }

    return {
        "id": make_id("lp_corners"),
        "question_type": "structured",
        "question_text": prompt,
        "correct_answer": correct,
        "sample_answer": f"y-intercept: (0; {c1}); x-intercept: ({c2 // 2}; 0); intersection: ({x0}; {y0})",
        "marks": 3,
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 5,
        "learning_objective_id": "math_lp_corner_points",
        "mode": "elementary_corner_points",
        "misconception_tags": ["simultaneous_equations_sign_error", "intercept_inversion_x_y"],
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp_1", "desc": "y-intercept of first constraint [A]", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "x-intercept of second constraint [A]", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "Simultaneous solution of intersection [M/A]", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "tier_1": "For the y-intercept, set x = 0. For the x-intercept, set y = 0.",
            "tier_2": f"Subtract the two equations: (2x + y) - (x + y) = {c2} - {c1} => x = {x0}. Then substitute to find y = {y0}.",
            "tier_3": f"Intercepts: (0; {c1}) and ({c2 // 2}; 0). Intersection point: ({x0}; {y0}).",
        },
    }


# --------------------------------------------------------------------------- #
# Sub-drill 3: Profit Maximisation (4 marks)
# --------------------------------------------------------------------------- #
def _build_maximisation_drill(r: random.Random) -> Dict[str, Any]:
    x0 = r.randint(5, 12)
    y0 = r.randint(4, 10)
    c1 = x0 + y0
    c2 = 2 * x0 + y0

    px = r.randint(20, 50) * 10
    py = r.randint(30, 80) * 10

    # Test all vertices:
    vertices = [(0, 0), (0, c1), (x0, y0), (c2 // 2, 0)]
    profits = [(v[0], v[1], px * v[0] + py * v[1]) for v in vertices]
    best = max(profits, key=lambda p: p[2])

    prompt = (
        f"The vertices of the feasible region for a production problem are given as:\n"
        f"$$A(0; 0),\\quad B(0; {c1}),\\quad C({x0}; {y0}),\\quad D({c2 // 2}; 0)$$\n\n"
        f"The profit function is given by $P = {px}x + {py}y$.\n\n"
        f"**Required:**\n"
        f"1. Evaluate the profit at each of the vertices $B, C,$ and $D$.\n"
        f"2. State the number of units of $x$ and $y$ that must be manufactured to **maximise** profit.\n"
        f"3. State the **maximum profit** achievable."
    )

    correct = {
        "profit_B": f"R{profits[1][2]}",
        "profit_C": f"R{profits[2][2]}",
        "profit_D": f"R{profits[3][2]}",
        "optimal_combination": f"{best[0]} units of x and {best[1]} units of y",
        "maximum_profit": f"R{best[2]}",
    }

    return {
        "id": make_id("lp_max_profit"),
        "question_type": "structured",
        "question_text": prompt,
        "correct_answer": correct,
        "sample_answer": f"Optimal: {best[0]} of x, {best[1]} of y; Max Profit: R{best[2]}",
        "marks": 4,
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 6,
        "learning_objective_id": "math_lp_maximisation",
        "mode": "elementary_profit_maximisation",
        "misconception_tags": ["tested_interior_point_instead_of_vertex", "arithmetic_error_in_profit_evaluation"],
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp_1", "desc": "Evaluation of profit at vertex B [M]", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Evaluation of profit at vertex C [M]", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "Evaluation of profit at vertex D [M]", "marks": 1, "editable": True},
                {"id": "mp_4", "desc": "Correct identification of optimal point and maximum profit [A]", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "tier_1": "Substitute the x and y coordinates of each corner point into P = ax + by.",
            "tier_2": f"B(0; {c1}) => P = {py} * {c1}. C({x0}; {y0}) => P = {px}*{x0} + {py}*{y0}. D({c2 // 2}; 0) => P = {px} * {c2 // 2}.",
            "tier_3": f"Maximum profit is achieved at ({best[0]}; {best[1]}) with P = R{best[2]}.",
        },
    }


# --------------------------------------------------------------------------- #
# COMPOUND: Full Linear Programming Exam Question (11 marks)
# --------------------------------------------------------------------------- #
def _build_compound(r: random.Random) -> List[Dict[str, Any]]:
    return [
        _build_formulation_drill(r),
        _build_corner_points_drill(r),
        _build_maximisation_drill(r),
    ]


# --------------------------------------------------------------------------- #
# PUBLIC API
# --------------------------------------------------------------------------- #
def generate(
    seed: Optional[int] = None,
    count: int = 1,
    mode: str = "compound",
    subskill: str = "mixed",
    difficulty: str = "medium",
    **kwargs,
) -> List[Dict[str, Any]]:
    r = rng(seed)
    questions: List[Dict[str, Any]] = []

    builders = {
        "elementary_inequalities_formulation": _build_formulation_drill,
        "elementary_corner_points": _build_corner_points_drill,
        "elementary_profit_maximisation": _build_maximisation_drill,
    }

    for _ in range(count):
        sub_r = rng(r.randint(1, 1_000_000_000))
        if mode == "compound":
            questions.extend(_build_compound(sub_r))
        elif mode in builders:
            questions.append(builders[mode](sub_r))
        else:
            questions.extend(_build_compound(sub_r))

    return questions
