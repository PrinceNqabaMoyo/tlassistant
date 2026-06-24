"""Shared deterministic helpers for Grade 10 Business Studies generators.

Mirrors the deterministic gold-standard pattern used by grade10_accounting
(seeded RNG + curated content banks + builder functions) but emits the question
shapes understood by the Business Studies /generate and /mark endpoints:

    mcq    -> {question_type, prompt, options, correct_index(str), explanation, marks, ...}
    typed  -> {question_type, prompt, marking_points, sample_answer, explanation, marks, ...}

No LLM is used. Generation is fully deterministic given a seed.
"""
from __future__ import annotations

import random
import uuid
from typing import Any, Dict, List, Optional


def rng(seed: Optional[int] = None) -> random.Random:
    r = random.Random()
    r.seed(int(seed)) if seed is not None else r.seed()
    return r


def make_id(prefix: str) -> str:
    return f"{prefix}_{uuid.uuid4().hex[:12]}"


# A small bank of South-African flavoured business scenarios used to add
# context variety to questions without changing the assessed content.
BUSINESS_SCENARIOS: List[Dict[str, str]] = [
    {"business": "Olwethu Beauty Salon", "owner": "Olwethu", "industry": "beauty and hairdressing"},
    {"business": "Sarah's Bakery", "owner": "Sarah", "industry": "baking"},
    {"business": "Mzobe Traders", "owner": "Mr Mzobe", "industry": "retail"},
    {"business": "Thandi's Tech", "owner": "Thandi", "industry": "electronics"},
    {"business": "Khanya Construction", "owner": "Khanya", "industry": "construction"},
    {"business": "Lerato Logistics", "owner": "Lerato", "industry": "transport"},
]


def pick_scenario(r: random.Random) -> Dict[str, str]:
    return r.choice(BUSINESS_SCENARIOS)


def make_mcq(
    *,
    prefix: str,
    prompt: str,
    options: List[str],
    correct_index: int,
    explanation: str,
    marks: int = 2,
    hint: Optional[str] = None,
    visual_aid_key: Optional[str] = None,
) -> Dict[str, Any]:
    hint_text = hint or explanation
    return {
        "id": make_id(f"{prefix}_mcq"),
        "question_type": "mcq",
        "prompt": prompt,
        "options": list(options),
        "correct_index": str(int(correct_index)),
        "explanation": explanation,
        "marks": int(marks),
        "hint_trigger": hint_text,
        "guidelines": [hint_text],
        "visual_aid_key": visual_aid_key,
    }


def make_typed(
    *,
    prefix: str,
    prompt: str,
    marking_points: List[str],
    sample_answer: str,
    marks: Optional[int] = None,
    hint: Optional[str] = None,
    visual_aid_key: Optional[str] = None,
) -> Dict[str, Any]:
    resolved_marks = int(marks) if marks is not None else max(1, len(marking_points))
    hint_text = hint or (f"Make sure your answer covers: {', '.join(marking_points[:3])}." if marking_points else "")
    return {
        "id": make_id(f"{prefix}_typed"),
        "question_type": "typed",
        "prompt": prompt,
        "marking_points": list(marking_points),
        "sample_answer": sample_answer,
        "explanation": sample_answer,
        "marks": resolved_marks,
        "hint_trigger": hint_text,
        "guidelines": [hint_text] if hint_text else [],
        "visual_aid_key": visual_aid_key,
    }


def make_wordbank(
    *,
    prefix: str,
    prompt: str,
    pool: List[str],
    blanks: List[str],
    correct_map: Dict[str, str],
    explanation: str,
    marks: int = 2,
    hint: Optional[str] = None,
    visual_aid_key: Optional[str] = None,
    text_parts: Optional[List[str]] = None,
) -> Dict[str, Any]:
    """Build a word-bank question.

    `blanks`   – list of blank labels, e.g. ["1", "2", "3"]
    `correct_map` – dict mapping blank label -> correct word from pool,
                   e.g. {"1": "Marketing", "2": "Production"}
    `text_parts` – optional list of text segments surrounding blanks.
                   Length should be len(blanks) + 1. Used by WordBankQuestionUI.
    """
    hint_text = hint or explanation
    # Structured blanks for frontend WordBankQuestionUI compatibility
    structured_blanks = [{"id": str(b), "label": str(b)} for b in blanks]
    resolved_text_parts = list(text_parts) if text_parts else [prompt] + [""] * len(blanks)
    return {
        "id": make_id(f"{prefix}_wb"),
        "question_type": "word_bank",
        "prompt": prompt,
        "word_bank": list(pool),
        "blanks": structured_blanks,
        "correct_map": dict(correct_map),
        "text_parts": resolved_text_parts,
        "explanation": explanation,
        "marks": int(marks),
        "hint_trigger": hint_text,
        "guidelines": [hint_text] if hint_text else [],
        "visual_aid_key": visual_aid_key,
    }


def make_matching(
    *,
    prefix: str,
    prompt: str,
    column_a: List[str],
    column_b: List[str],
    correct_pairs: Dict[str, str],
    explanation: str,
    marks: int = 2,
    hint: Optional[str] = None,
    visual_aid_key: Optional[str] = None,
) -> Dict[str, Any]:
    """Build a matching-columns question.

    `column_a`    – left-side items, e.g. ["A", "B", "C"]
    `column_b`    – right-side items, e.g. ["1", "2", "3"]
    `correct_pairs` – mapping from column_a label -> column_b label,
                     e.g. {"A": "2", "B": "1", "C": "3"}
    """
    hint_text = hint or explanation
    return {
        "id": make_id(f"{prefix}_match"),
        "question_type": "matching_columns",
        "prompt": prompt,
        "column_a": list(column_a),
        "column_b": list(column_b),
        "correct_pairs": dict(correct_pairs),
        "explanation": explanation,
        "marks": int(marks),
        "hint_trigger": hint_text,
        "guidelines": [hint_text] if hint_text else [],
        "visual_aid_key": visual_aid_key,
    }


def make_crossword(
    *,
    prefix: str,
    prompt: str,
    words: List[str],
    clues: Dict[str, str],
    grid_size: int = 10,
    explanation: str,
    marks: int = 2,
    hint: Optional[str] = None,
    visual_aid_key: Optional[str] = None,
) -> Dict[str, Any]:
    """Build a crossword question.

    `words`    – list of words to place in the grid (uppercase)
    `clues`    – dict mapping word -> clue text
    `grid_size`– size of the square grid
    """
    hint_text = hint or explanation
    return {
        "id": make_id(f"{prefix}_cross"),
        "question_type": "crossword",
        "prompt": prompt,
        "words": [w.upper() for w in words],
        "clues": dict(clues),
        "grid_size": int(grid_size),
        "explanation": explanation,
        "marks": int(marks),
        "hint_trigger": hint_text,
        "guidelines": [hint_text] if hint_text else [],
        "visual_aid_key": visual_aid_key,
    }


def make_essay(
    *,
    prefix: str,
    prompt: str,
    rubric: List[Dict[str, Any]],
    sample_answer: str,
    marks: int = 20,
    min_words: int = 150,
    max_words: int = 400,
    hint: Optional[str] = None,
    visual_aid_key: Optional[str] = None,
) -> Dict[str, Any]:
    """Build an essay / long-form question.

    `rubric` – list of criteria dicts, e.g.
        [{"criterion": "Introduction", "marks": 4, "description": "..."}, ...]
    """
    hint_text = hint or (
        "Plan your answer: write an introduction, develop your points in the body, "
        "and finish with a conclusion."
    )
    return {
        "id": make_id(f"{prefix}_essay"),
        "question_type": "essay",
        "prompt": prompt,
        "rubric": list(rubric),
        "sample_answer": sample_answer,
        "explanation": sample_answer,
        "marks": int(marks),
        "min_words": int(min_words),
        "max_words": int(max_words),
        "hint_trigger": hint_text,
        "guidelines": [hint_text],
        "visual_aid_key": visual_aid_key,
    }


def sample_pool(r: random.Random, pool: List[Dict[str, Any]], count: int) -> List[Dict[str, Any]]:
    """Pick `count` items from a pool of *factory callables or dicts*.

    Each pool entry is a zero-arg callable returning a fresh question dict
    (so ids/scenario shuffles differ per call). Sampling is without
    replacement when the pool is large enough, otherwise with replacement.
    """
    n = max(1, min(int(count or 1), 50))
    if not pool:
        return []
    if len(pool) >= n:
        chosen = r.sample(pool, n)
    else:
        chosen = [r.choice(pool) for _ in range(n)]
    return [item() if callable(item) else dict(item) for item in chosen]


def build_generate(pools_builder):
    """Return a `generate(subskill, difficulty, count, seed=None, **kw)` function.

    `pools_builder(r)` must return a dict mapping subskill-key -> list of
    factory callables. A 'mixed' key is auto-derived from the union if absent.
    """

    def generate(subskill: str = "concepts", difficulty: str = "medium", count: int = 1, seed: Optional[int] = None, **_kw) -> List[Dict[str, Any]]:
        r = rng(seed)
        pools = pools_builder(r)
        if "mixed" not in pools:
            union: List[Any] = []
            for key, items in pools.items():
                union.extend(items)
            pools["mixed"] = union
        key = str(subskill or "concepts").strip().lower()
        pool = pools.get(key) or pools.get("mixed") or []
        return sample_pool(r, pool, count)

    return generate
