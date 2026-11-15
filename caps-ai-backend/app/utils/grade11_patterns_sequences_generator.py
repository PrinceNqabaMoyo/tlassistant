"""
Grade 11 Mathematics — Number Patterns (Quadratic Sequences) Generator
======================================================================
100% Aligned with South African National Curriculum Standards (Grade 11 Term 1).
Covers 50 distinct semantic subskill archetypes across linear revision,
second differences, quadratic general terms T_n = an^2 + bn + c, solving for n,
turning points/extrema, geometric/visual patterns, simultaneous equations,
ratios, conjecture & proof, SA contextual modelling, and synthesis.
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional

from app.utils.grade11_mathematics.patterns_sequences_archetypes_01_25 import (
    BUILDERS_01_25,
)
from app.utils.grade11_mathematics.patterns_sequences_archetypes_26_50 import (
    BUILDERS_26_50,
)

TOPIC_ID = "grade11_math_patterns_sequences"
TOPIC_NAME = "Number patterns"

BUILDERS: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    **BUILDERS_01_25,
    **BUILDERS_26_50,
}

ARCHETYPES: Dict[str, Callable[[random.Random], Dict[str, Any]]] = dict(BUILDERS)
ORDERED_SUBSKILLS: List[str] = list(BUILDERS.keys())
SUBSKILLS: List[str] = list(ORDERED_SUBSKILLS)
AVAILABLE_SUBSKILLS: List[str] = list(ORDERED_SUBSKILLS)
_SUBSKILLS: List[str] = list(ORDERED_SUBSKILLS)

LEGACY_ALIASES: Dict[str, str] = {
    "linear_next_terms": "01_linear_sequence_common_difference_and_next_terms",
    "linear_general_term": "02_linear_sequence_general_term_formula",
    "quadratic_constant_second_diff": "05_constant_second_difference_identification",
    "quadratic_next_terms": "06_next_two_terms_from_second_difference",
    "quadratic_general_term": "11_general_term_standard_positive_a",
    "quadratic_find_term_value": "19_evaluate_specific_term_tk",
    "quadratic_find_n_given_tn": "21_solve_for_n_given_tn_positive_root",
    "quadratic_missing_terms": "08_missing_term_in_quadratic_sequence_numeric",
    "quadratic_algebraic_missing": "09_algebraic_unknown_x_in_quadratic_terms",
    "quadratic_max_min_term": "26_minimum_term_value_and_position",
    "quadratic_first_diff_sequence": "29_first_differences_as_linear_sequence_formula",
    "visual_dot_pattern": "31_visual_dot_array_triangular_rectangular",
    "compound": "50_multi_part_quadratic_pattern_exam_synthesis",
}


def _enrich_legacy_fields(q: Dict[str, Any], index: int = 1, seed_val: int = 42, difficulty: str = "medium") -> Dict[str, Any]:
    out = dict(q)
    out.setdefault("id", f"NP11-{index:03d}")
    out["difficulty"] = difficulty or out.get("difficulty", "medium")
    out["seed"] = seed_val
    out.setdefault("question", out.get("prompt", out.get("question_text", "")))
    out.setdefault("question_text", out.get("prompt", out.get("question", "")))
    out.setdefault("correct_answer", out.get("answer_latex", out.get("answer", "")))
    out.setdefault("explanation", out.get("worked_solution", out.get("solution", "")))
    out.setdefault("marks", out.get("total_marks", 4))
    out.setdefault("type", "short_answer")
    return out


def generate_question(
    subskill: Optional[str] = None,
    difficulty: str = "medium",
    seed: Optional[int] = None,
) -> Dict[str, Any]:
    base_seed = 42 if seed is None else int(seed)
    rng = random.Random(base_seed)
    resolved = LEGACY_ALIASES.get(str(subskill or ""), subskill)
    if resolved not in BUILDERS:
        resolved = rng.choice(ORDERED_SUBSKILLS)
    q = BUILDERS[resolved](rng)
    return _enrich_legacy_fields(q, 1, base_seed, difficulty)


def generate_questions(
    subskill: str = "mixed",
    difficulty: str = "easy",
    question_type: str = "mixed",
    count: int = 5,
    seed: Optional[int] = None,
    **kwargs: Any,
) -> List[Dict[str, Any]]:
    base_seed = 42 if seed is None else int(seed)
    rng = random.Random(base_seed)
    count = max(1, min(int(count or 1), 50))
    resolved = LEGACY_ALIASES.get(str(subskill or ""), subskill)

    questions: List[Dict[str, Any]] = []
    for i in range(count):
        item_seed = base_seed + i * 17
        item_rng = random.Random(item_seed)
        if resolved in BUILDERS:
            chosen = resolved
        else:
            chosen = ORDERED_SUBSKILLS[i % len(ORDERED_SUBSKILLS)] if count > 1 else rng.choice(ORDERED_SUBSKILLS)
        q = BUILDERS[chosen](item_rng)
        questions.append(_enrich_legacy_fields(q, i + 1, item_seed, difficulty))
    return questions


def generate(
    subskill: Optional[str] = None,
    difficulty: str = "medium",
    count: int = 1,
    seed: Optional[int] = None,
    mode: str = "compound",
    **kwargs: Any,
) -> List[Dict[str, Any]]:
    target = subskill or mode
    return generate_questions(
        subskill=str(target or "mixed"),
        difficulty=difficulty,
        count=count,
        seed=seed,
        **kwargs,
    )
