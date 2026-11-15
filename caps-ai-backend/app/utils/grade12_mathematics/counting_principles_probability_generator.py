"""Grade 12 Mathematics — Counting Principles & Probability (50-Archetype Generator).
Grounded in curriculum_docs_auto/Mathematics_Gr12/Term 3/02. Probability.md.
Covers official South African National Curriculum Standards (NSC Paper 1, Questions 10 & 11: 15–20 marks).
Zero-LLM: 100% deterministic SymPy mathematics with South African comma decimals ({,}) and inline SVG diagram specs.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from app.utils.grade12_mathematics.counting_principles_probability_archetypes_01_25 import (
    ARCHETYPES_01_25,
)
from app.utils.grade12_mathematics.counting_principles_probability_archetypes_26_50 import (
    ARCHETYPES_26_50,
)

TOPIC = "grade12_math_counting_probability"
LO = "math12_probability"

ARCHETYPES: Dict[str, Any] = {
    **ARCHETYPES_01_25,
    **ARCHETYPES_26_50,
}

SUBSKILLS: List[str] = list(ARCHETYPES.keys())
ORDERED_SUBSKILLS: List[str] = list(SUBSKILLS)
AVAILABLE_SUBSKILLS: List[str] = list(SUBSKILLS)

LEGACY_BUILDERS: Dict[str, Any] = {
    "compound": ARCHETYPES["50_comprehensive_counting_and_venn_synthesis"],
    "compound_seating_venn": ARCHETYPES["50_comprehensive_counting_and_venn_synthesis"],
    "counting_principles_venn_compound": ARCHETYPES["50_comprehensive_counting_and_venn_synthesis"],
    "compound_digits_independence": ARCHETYPES["44_digit_codes_overlapping_prime_and_even_case_split"],
    "counting_principles_digits_compound": ARCHETYPES["44_digit_codes_overlapping_prime_and_even_case_split"],
    "elementary_factorial_calc": ARCHETYPES["31_permutations_r_from_n_distinct_objects"],
    "factorial_permutations": ARCHETYPES["31_permutations_r_from_n_distinct_objects"],
    "elementary_grouping_restriction": ARCHETYPES["36_grouping_single_group_together_block_method"],
    "grouping_restriction": ARCHETYPES["36_grouping_single_group_together_block_method"],
    "elementary_independence_test": ARCHETYPES["09_testing_independence_from_probabilities"],
    "independence_test": ARCHETYPES["09_testing_independence_from_probabilities"],
}

BUILDERS: Dict[str, Any] = {
    **ARCHETYPES,
}


def get_subskills() -> List[str]:
    """Return the list of all 50 semantic subskills."""
    return list(SUBSKILLS)


def generate_question(
    subskill: Optional[str] = None,
    seed: Optional[int] = None,
    difficulty: str = "hard",
    mode: str = "compound",
    **kwargs: Any,
) -> Dict[str, Any]:
    """Generate a single deterministic Grade 12 Probability question."""
    r = random.Random(seed if seed is not None else 42)
    target = subskill or (mode if mode in BUILDERS or mode in LEGACY_BUILDERS else r.choice(SUBSKILLS))
    builder = BUILDERS.get(target) or LEGACY_BUILDERS.get(target) or ARCHETYPES[r.choice(SUBSKILLS)]
    try:
        q = builder(r)
    except TypeError:
        q = builder(r, difficulty=difficulty)
    if seed is not None:
        q["seed"] = seed
    return q


def generate(
    subskill: Optional[str] = None,
    difficulty: str = "hard",
    count: int = 1,
    seed: Optional[int] = None,
    mode: str = "compound",
    **kwargs: Any,
) -> Dict[str, Any]:
    """Generates deterministic Grade 12 Counting Principles & Probability questions."""
    base_seed = 42 if seed is None else int(seed)
    chosen_target = subskill if (subskill and subskill != "mixed") else (mode if mode in BUILDERS else None)

    questions = []
    for i in range(max(1, count)):
        curr_seed = base_seed * 1000 + i
        r = random.Random(curr_seed)
        target = chosen_target
        if not target or (target not in BUILDERS and target not in LEGACY_BUILDERS):
            target = SUBSKILLS[i % len(SUBSKILLS)] if count > 1 else r.choice(SUBSKILLS)
        builder = BUILDERS.get(target) or LEGACY_BUILDERS.get(target) or ARCHETYPES[SUBSKILLS[0]]
        try:
            q = builder(r)
        except TypeError:
            q = builder(r, difficulty=difficulty)
        q["seed"] = curr_seed
        questions.append(q)

    return {"questions": questions}


def generate_questions(
    subskill: Optional[str] = None,
    difficulty: str = "hard",
    count: int = 1,
    seed: Optional[int] = None,
    **kwargs: Any,
) -> List[Dict[str, Any]]:
    """Legacy helper returning a flat list of questions."""
    return generate(subskill=subskill, difficulty=difficulty, count=count, seed=seed, **kwargs).get("questions", [])
