"""Shared deterministic helpers for Grade 11 Mathematics generators.
Strictly zero-LLM: uses SymPy to compute answers, steps, and canonical solution graphs.
Enforces South African CAPS comma decimal convention ({,}) and the 6-Pillar Generator Contract.
"""
from __future__ import annotations

import random
import re
import uuid
from typing import Any, Dict, List, Optional
import sympy as sp


def rng(seed: Optional[int] = None) -> random.Random:
    r = random.Random()
    if seed is not None:
        r.seed(int(seed))
    return r


def make_id(prefix: str) -> str:
    return f"{prefix}_{uuid.uuid4().hex[:12]}"


def nonzero(r: random.Random, lo: int, hi: int, exclude: Optional[List[int]] = None) -> int:
    excl = set(exclude or [])
    excl.add(0)
    choices = [n for n in range(lo, hi + 1) if n not in excl]
    return r.choice(choices) if choices else 1


def _commaize(latex: str) -> str:
    """Render decimal points as tight commas for South African CAPS notation."""
    return re.sub(r"(?<=\d)\.(?=\d)", "{,}", latex)


def to_latex(expr: Any) -> str:
    """SymPy object -> KaTeX string with comma decimals."""
    return _commaize(sp.latex(expr))


def num(value: Any, places: Optional[int] = None) -> str:
    """Format numeric values with South African comma decimal separator."""
    if places is not None:
        s = f"{float(value):.{places}f}"
    elif isinstance(value, int) or (isinstance(value, float) and value.is_integer()):
        s = str(int(value))
    else:
        s = str(value)
    return s.replace(".", "{,}")


def step(
    *,
    from_expr: Any = None,
    to_expr: Any = None,
    op: str,
    rule: str = "",
    common_errors: Optional[List[str]] = None,
    from_latex: Optional[str] = None,
    to_latex_str: Optional[str] = None,
) -> Dict[str, Any]:
    fl = from_latex if from_latex is not None else (to_latex(from_expr) if from_expr is not None else "")
    tl = to_latex_str if to_latex_str is not None else (to_latex(to_expr) if to_expr is not None else "")
    return {
        "from_latex": fl,
        "to_latex": tl,
        "from_sympy": sp.srepr(from_expr) if from_expr is not None else "",
        "to_sympy": sp.srepr(to_expr) if to_expr is not None else "",
        "op": op,
        "rule": rule,
        "common_errors": list(common_errors or []),
    }


def solution_graph(
    *,
    goal: str,
    steps: List[Dict[str, Any]],
    final_expr: Any = None,
    chain_type: str = "expression",
    var: str = "x",
    final_latex: Optional[str] = None,
) -> Dict[str, Any]:
    fl = final_latex if final_latex is not None else (to_latex(final_expr) if final_expr is not None else "")
    return {
        "goal": goal,
        "chain_type": chain_type,
        "var": var,
        "steps": list(steps),
        "final_latex": fl,
        "final_sympy": sp.srepr(final_expr) if final_expr is not None else "",
    }


def make_math_question(
    *,
    prefix: str,
    topic: str,
    subskill: str,
    learning_objective_id: str,
    prompt: str,
    prompt_latex: str,
    answer_mode: str = "typed",
    question_type: str = "math_short",
    answer_latex: str = "",
    answer_sympy: str = "",
    sample_answer: str = "",
    canonical_solution: Optional[Dict[str, Any]] = None,
    marking_schema: Dict[str, Any],
    hints: Dict[str, str],
    misconception_tags: Optional[List[str]] = None,
    diagnostic_tags: Optional[List[str]] = None,
    keywords: Optional[List[str]] = None,
    term: int = 2,
    caps_weight_percent: int = 35,
    suggested_duration_mins: int = 8,
    mode: str = "compound",
    difficulty: str = "medium",
    minimum_mastery_score: float = 0.8,
    diagram_spec: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    total_marks = marking_schema.get("total_marks", 4)
    q = {
        "id": make_id(prefix),
        "subject": "mathematics",
        "grade": "grade-11",
        "topic": topic,
        "subskill": subskill,
        "learning_objective_id": learning_objective_id,
        "mode": mode,
        "difficulty": difficulty,
        "question_type": question_type,
        "answer_mode": answer_mode,
        "prompt": prompt,
        "prompt_latex": prompt_latex,
        "answer_latex": answer_latex,
        "answer_sympy": answer_sympy,
        "sample_answer": sample_answer or answer_latex,
        "canonical_solution": canonical_solution or {},
        "marking_schema": marking_schema,
        "marks": total_marks,
        "hint_sections": {
            "1_nudge": hints.get("nudge", "Identify the applicable theorem or trigonometric reduction."),
            "2_concept": hints.get("concept", "Apply the standard formula or geometric rule with correct reasoning."),
            "3_breakdown": hints.get("breakdown", "Follow the stepwise calculation."),
        },
        "hints": [
            {"tier": 1, "text": hints.get("nudge", "Identify the applicable theorem or trigonometric reduction.")},
            {"tier": 2, "text": hints.get("concept", "Apply the standard formula or geometric rule with correct reasoning.")},
            {"tier": 3, "text": hints.get("breakdown", "Follow the stepwise calculation.")},
        ],
        "misconception_tags": list(misconception_tags or []),
        "diagnostic_tags": list(diagnostic_tags or ["grade11", "math"]),
        "keywords": list(keywords or []),
        "term": term,
        "caps_weight_percent": caps_weight_percent,
        "suggested_duration_mins": suggested_duration_mins,
        "minimum_mastery_score": minimum_mastery_score,
    }
    if diagram_spec is not None:
        q["diagram_spec"] = diagram_spec
    return q
