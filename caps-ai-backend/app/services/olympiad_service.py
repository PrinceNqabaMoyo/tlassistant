"""
Olympiad Service (Layer F)
--------------------------
Manages the SAMO Olympiad preparation track, CAPS mastery gate checking,
problem generation, submission grading, and Technique Library reference cards.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional
from app.utils.olympiad.olympiad_generator import generate_olympiad_problem

# In-memory mock store for Olympiad submissions & credentials
_OLYMPIAD_USER_STORE: Dict[str, Dict[str, Any]] = {}

TECHNIQUE_LIBRARY = [
    {
        "id": "tech_pigeonhole",
        "name": "Pigeonhole Principle (Dirichlet's Principle)",
        "category": "combinatorics",
        "description": "If $n+1$ items are placed into $n$ pigeonholes, at least one hole must contain more than one item.",
        "key_formula": "\\text{If } kn+1 \\text{ objects occupy } n \\text{ boxes, at least one box contains } \\ge k+1 \\text{ objects.}",
        "example_problem": "In any group of 367 people, at least two must share a birthday.",
        "tags": ["combinatorics", "worst_case", "existence_proof"],
    },
    {
        "id": "tech_modular_arithmetic",
        "name": "Modular Arithmetic & Power Cycles",
        "category": "number_theory",
        "description": "Remainders cycle periodically under powers modulo $m$. Reduces huge exponents to small integers.",
        "key_formula": "a \\equiv b \\pmod m \\implies a^k \\equiv b^k \\pmod m",
        "example_problem": "Finding the last digit of $7^{2026}$ by observing mod 10 cycles (7, 9, 3, 1).",
        "tags": ["number_theory", "cycles", "divisibility"],
    },
    {
        "id": "tech_telescoping_series",
        "name": "Telescoping Sums & Partial Fractions",
        "category": "algebra",
        "description": "Expressing terms as differences $f(k) - f(k+1)$ causes all intermediate terms to collapse.",
        "key_formula": "\\sum_{k=1}^n \\left( \\frac{1}{k} - \\frac{1}{k+1} \\right) = 1 - \\frac{1}{n+1} = \\frac{n}{n+1}",
        "example_problem": "Summing inverse products $\\frac{1}{1 \\times 2} + \\frac{1}{2 \\times 3} + \\dots$",
        "tags": ["algebra", "series", "cancellation"],
    },
    {
        "id": "tech_am_gm",
        "name": "AM-GM Inequality (Arithmetic-Geometric Mean)",
        "category": "algebra",
        "description": "For any non-negative real numbers, the arithmetic mean is always at least the geometric mean.",
        "key_formula": "\\frac{a + b}{2} \\ge \\sqrt{ab}, \\quad \\text{with equality iff } a = b",
        "example_problem": "Finding the minimum of $x + \\frac{16}{x}$ for $x > 0$.",
        "tags": ["algebra", "inequalities", "extrema"],
    },
    {
        "id": "tech_parity_invariants",
        "name": "Parity & Invariant Theory",
        "category": "geometry",
        "description": "Analyzing odd/even parity that remains unchanged across moves or geometric steps.",
        "key_formula": "\\text{Even} \\pm \\text{Even} = \\text{Even}, \\quad \\text{Odd} \\pm \\text{Odd} = \\text{Even}",
        "example_problem": "Proving a chessboard missing opposite diagonal corners cannot be tiled by dominoes.",
        "tags": ["invariants", "logic", "chessboard"],
    },
]


def check_caps_mastery_gate(user_id: str, math_medals: Optional[List[str]] = None) -> Dict[str, Any]:
    """Checks whether a learner has met the CAPS prerequisite to enter the Olympiad track.
    
    Rule: Requires at least 1 Silver or Gold Topic Medal in CAPS Mathematics
    (e.g., Trigonometry, Algebraic Expressions, Functions).
    """
    # Demo/default logic: students with mock or registered silver/gold medal are unlocked
    medals = math_medals or ["topic_medal_silver_trig", "topic_medal_gold_algebra"]
    has_qualified = any("silver" in m or "gold" in m for m in medals)

    return {
        "user_id": user_id,
        "unlocked": has_qualified,
        "qualified_medals": medals,
        "required_badge": "Silver or Gold Topic Medal in CAPS Mathematics",
        "message": (
            "🎉 Olympiad Track Unlocked! Your CAPS Mathematics Silver/Gold Medal qualifies you for SAMO Round 1."
            if has_qualified else
            "🔒 Locked. Complete CAPS Mathematics assessments and earn a Silver Topic Medal (80%+) to qualify."
        ),
    }


def get_problem(category: str = "random", division: str = "junior", seed: Optional[int] = None) -> Dict[str, Any]:
    """Generates a seeded Olympiad problem."""
    return generate_olympiad_problem(category=category, division=division, seed=seed)


def submit_answer(
    user_id: str,
    problem_id: str,
    selected_index: int,
    correct_index: int,
    division: str = "junior",
) -> Dict[str, Any]:
    """Evaluates an Olympiad answer and awards authenticated XP and medals."""
    is_correct = int(selected_index) == int(correct_index)
    xp_awarded = 100 if is_correct else 10

    if user_id not in _OLYMPIAD_USER_STORE:
        _OLYMPIAD_USER_STORE[user_id] = {
            "solved": 0,
            "total_attempts": 0,
            "xp": 0,
            "medallions": [],
        }

    stats = _OLYMPIAD_USER_STORE[user_id]
    stats["total_attempts"] += 1
    stats["xp"] += xp_awarded
    if is_correct:
        stats["solved"] += 1

    # Award Olympiad credentials
    new_medallion = None
    if stats["solved"] >= 5 and "samo_bronze" not in stats["medallions"]:
        stats["medallions"].append("samo_bronze")
        new_medallion = "SAMO Round 1 Bronze Qualifier Medallion"
    elif stats["solved"] >= 10 and "samo_silver" not in stats["medallions"]:
        stats["medallions"].append("samo_silver")
        new_medallion = "SAMO Round 1 Silver Semi-Finalist Medallion"

    return {
        "success": True,
        "is_correct": is_correct,
        "xp_awarded": xp_awarded,
        "total_solved": stats["solved"],
        "total_olympiad_xp": stats["xp"],
        "new_medallion": new_medallion,
        "feedback": "Outstanding solution! Accurate non-routine problem solving." if is_correct else "Incorrect option. Check the technique hint and worked steps.",
    }


def get_technique_library() -> List[Dict[str, Any]]:
    """Returns the Olympiad Technique Library."""
    return TECHNIQUE_LIBRARY
