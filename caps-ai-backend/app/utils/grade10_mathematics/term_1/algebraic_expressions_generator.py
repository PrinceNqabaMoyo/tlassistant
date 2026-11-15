"""Grade 10 Mathematics — Term 1 — Algebraic Expressions Generator.

Main coordinator and dispatcher module with 50 distinct semantic archetypes.
100% deterministic, SymPy-backed, zero LLM.

Curriculum source:
``curriculum_docs/Mathematics_Gr10/Term 1/1 Algebraic Expressions .md``.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from app.utils.grade10_mathematics._math_common import rng
from app.utils.grade10_mathematics.term_1.algebraic_expressions_archetypes_01_25 import BUILDERS_01_25
from app.utils.grade10_mathematics.term_1.algebraic_expressions_archetypes_26_50 import BUILDERS_26_50

TOPIC = "grade10_math_algebraic_expressions"
LO = "math10_algebraic_expressions"

# Combine 50 semantic builders
ALL_BUILDERS: Dict[str, Any] = {}
ALL_BUILDERS.update(BUILDERS_01_25)
ALL_BUILDERS.update(BUILDERS_26_50)

ORDERED_SUBSKILLS: List[str] = list(ALL_BUILDERS.keys())
SUBSKILLS: Dict[str, Any] = dict(ALL_BUILDERS)

# Separate dispatch lookup table for aliases and numeric indices
DISPATCH_TABLE: Dict[str, Any] = dict(ALL_BUILDERS)

# Legacy alias mappings for backward compatibility
LEGACY_ALIASES: Dict[str, str] = {
    "real_numbers": "01_classify_number_system_rational_irrational",
    "rounding": "07_round_to_n_decimal_places",
    "products": "13_multiply_binomial_by_binomial_foil",
    "factorise_common": "23_factorise_common_monomial_factor",
    "factorise_diff_squares": "26_factorise_difference_of_squares_simple",
    "factorise_trinomial": "33_factorise_trinomial_monic_positive_roots",
    "simplify_fractions": "42_simplify_fraction_common_factor_cancel",
    "concepts": "01_classify_number_system_rational_irrational",
}

for alias, target in LEGACY_ALIASES.items():
    if target in ALL_BUILDERS:
        DISPATCH_TABLE[alias] = ALL_BUILDERS[target]

# Index-based access in dispatch table
for idx, key in enumerate(ORDERED_SUBSKILLS, 1):
    DISPATCH_TABLE[str(idx)] = ALL_BUILDERS[key]
    DISPATCH_TABLE[f"{idx:02d}"] = ALL_BUILDERS[key]
    DISPATCH_TABLE[idx] = ALL_BUILDERS[key]

ARCHETYPES = list(ORDERED_SUBSKILLS)
ARCHETYPE_KEYS = list(ORDERED_SUBSKILLS)


def _resolve_builder(subskill: Optional[Any]) -> tuple[str, Any]:
    if subskill is None or subskill in ("mixed", "all", ""):
        return ORDERED_SUBSKILLS[0], ALL_BUILDERS[ORDERED_SUBSKILLS[0]]
    if isinstance(subskill, int) and 1 <= subskill <= len(ORDERED_SUBSKILLS):
        key = ORDERED_SUBSKILLS[subskill - 1]
        return key, ALL_BUILDERS[key]
    s_str = str(subskill).strip()
    if s_str.startswith("elementary_"):
        s_str = s_str[len("elementary_"):]
    if s_str in ALL_BUILDERS:
        return s_str, ALL_BUILDERS[s_str]
    if s_str in LEGACY_ALIASES:
        target = LEGACY_ALIASES[s_str]
        return target, ALL_BUILDERS[target]
    if s_str.isdigit():
        idx = int(s_str)
        if 1 <= idx <= len(ORDERED_SUBSKILLS):
            key = ORDERED_SUBSKILLS[idx - 1]
            return key, ALL_BUILDERS[key]
    # Fuzzy matching on snake_case
    for k in ORDERED_SUBSKILLS:
        if s_str in k:
            return k, ALL_BUILDERS[k]
    return ORDERED_SUBSKILLS[0], ALL_BUILDERS[ORDERED_SUBSKILLS[0]]


def generate(
    subskill: Optional[str] = None,
    difficulty: str = "medium",
    count: int = 1,
    seed: Optional[int] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    """Deterministic generator for Grade 10 Algebraic Expressions."""
    questions: List[Dict[str, Any]] = []
    base_seed = 42 if seed is None else int(seed)

    is_mixed = subskill in ("mixed", "all", None, "")

    for i in range(max(1, int(count))):
        sub_seed = base_seed * 1000 + i
        r = random.Random(sub_seed)

        if is_mixed:
            chosen_key = ORDERED_SUBSKILLS[(base_seed + i) % len(ORDERED_SUBSKILLS)]
            builder = ALL_BUILDERS[chosen_key]
        else:
            chosen_key, builder = _resolve_builder(subskill)

        q = builder(r, difficulty=difficulty)
        if seed is not None:
            q["id"] = f"{TOPIC}_{chosen_key}_{base_seed}_{i}"
        questions.append(q)

    return {"questions": questions}


def generate_question(
    subskill: Optional[str] = None,
    difficulty: str = "medium",
    seed: Optional[int] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    res = generate(subskill=subskill, difficulty=difficulty, count=1, seed=seed, **kwargs)
    return res["questions"][0]
