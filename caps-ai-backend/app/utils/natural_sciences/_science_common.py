"""Shared utilities, seed helpers, and 6-pillar formatting for Natural Sciences generators."""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


def rng(seed: Optional[int] = None) -> random.Random:
    """Returns a deterministic random generator instance."""
    r = random.Random()
    if seed is not None:
        r.seed(int(seed))
    return r


def fmt_sa(val: float | int, places: int = 2) -> str:
    """Formats numeric values with South African comma decimals and tight LaTeX spacing."""
    if isinstance(val, int) or val.is_integer():
        return str(int(val))
    s = f"{val:.{places}f}".rstrip("0").rstrip(".")
    return s.replace(".", "{,}")


def make_id(prefix: str = "ns") -> str:
    return f"{prefix}_{random.randint(100000, 999999)}"


def make_science_question(
    prefix: str,
    topic: str,
    subskill: str,
    learning_objective_id: str,
    prompt: str,
    prompt_latex: str,
    answer_latex: str,
    sample_answer: str,
    marking_schema: Dict[str, Any],
    hints: Dict[str, str],
    misconception_tags: List[str],
    keywords: List[str],
    term: int,
    caps_weight_percent: int,
    suggested_duration_mins: int,
    mode: str = "compound",
    difficulty: str = "hard",
    marks: Optional[int] = None,
) -> Dict[str, Any]:
    """Factory creating fully normalized 6-pillar CAPS Natural Sciences questions."""
    total_marks = marks if marks is not None else marking_schema.get("total_marks", 5)

    # Standardize 3-tier hints
    standard_hints = {
        "tier_1": hints.get("nudge") or hints.get("tier_1") or "Inspect the given parameters and units carefully.",
        "tier_2": hints.get("concept") or hints.get("tier_2") or "Recall the relevant scientific law or formula.",
        "tier_3": hints.get("breakdown") or hints.get("tier_3") or f"Worked calculation: {answer_latex}",
    }

    return {
        "id": make_id(prefix),
        "question_id": make_id(prefix),
        "topic": topic,
        "subskill": subskill,
        "learning_objective_id": learning_objective_id,
        "prompt": prompt,
        "prompt_latex": prompt_latex,
        "answer_latex": answer_latex,
        "sample_answer": sample_answer,
        "ideal_answer": answer_latex,
        "marking_schema": marking_schema,
        "hints": standard_hints,
        "misconception_tags": misconception_tags,
        "keywords": keywords,
        "term": term,
        "caps_weight_percent": caps_weight_percent,
        "suggested_duration_mins": suggested_duration_mins,
        "mode": mode,
        "difficulty": difficulty,
        "marks": total_marks,
    }
