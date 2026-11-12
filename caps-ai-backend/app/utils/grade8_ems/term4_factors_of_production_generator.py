"""Grade 8 EMS — Factors of Production (Deterministic 50-Archetype Generator).
Grounded strictly in: curriculum_docs_auto/EMS_Gr8/Term 4/03. Factors of production.md

Zero-LLM, 100% deterministic via rng: random.Random, authentic South African context.
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional

from app.utils.grade8_ems.factors_of_production_archetypes_01_25 import (
    ARCHETYPES_01_25,
    CAPS_WEIGHT_PERCENT,
    LO,
    TERM,
    TOPIC_KEY,
    TOPIC_NAME,
)
from app.utils.grade8_ems.factors_of_production_archetypes_26_50 import ARCHETYPES_26_50

ARCHETYPE_BUILDERS: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    **ARCHETYPES_01_25,
    **ARCHETYPES_26_50,
}

ORDERED_SUBSKILLS: List[str] = list(ARCHETYPE_BUILDERS.keys())
SUBSKILLS: List[str] = list(ORDERED_SUBSKILLS)

_LEGACY_ALIASES: Dict[str, List[str]] = {
    "four_factors_classification": ["02_four_factors_identification", "04_factors_and_remuneration_table"],
    "remuneration_of_factors": ["03_factor_remuneration_matching", "04_factors_and_remuneration_table"],
    "remuneration_factors": ["03_factor_remuneration_matching", "04_factors_and_remuneration_table"],
    "capital_own_vs_borrowed": ["22_own_vs_borrowed_capital_comparison", "23_borrowed_capital_interest_cost_calc"],
    "capital_infrastructure": ["20_capital_financial_vs_physical_goods", "21_consumer_good_vs_capital_good"],
    "labour_skill_levels_and_laws": ["10_unskilled_labour_characteristics", "12_skilled_labour_characteristics", "29_lra_labour_relations_act_purpose", "30_bcea_working_hours_overtime"],
    "labour_workforce": ["09_labour_definition_human_effort", "13_classify_labour_skill_levels_table"],
    "natural_resources_land": ["05_natural_resources_land_definition", "06_renewable_vs_non_renewable_resources"],
    "entrepreneurship_role": ["25_entrepreneurship_combining_factors_role", "26_entrepreneur_seven_qualities_id"],
    "concepts": ORDERED_SUBSKILLS[:25],
}

DISPATCH_TABLE: Dict[str, Callable[[random.Random], Dict[str, Any]]] = dict(ARCHETYPE_BUILDERS)
for idx, key in enumerate(ORDERED_SUBSKILLS, start=1):
    DISPATCH_TABLE[str(idx)] = ARCHETYPE_BUILDERS[key]
    DISPATCH_TABLE[f"{idx:02d}"] = ARCHETYPE_BUILDERS[key]


def _rng(seed: Optional[int] = None) -> random.Random:
    return random.Random(seed) if seed is not None else random.Random()


def get_subskills() -> List[str]:
    return list(ORDERED_SUBSKILLS)


def _select_builder(subskill: Optional[str], rng: random.Random) -> Callable[[random.Random], Dict[str, Any]]:
    raw = str(subskill or "mixed").strip()
    low = raw.lower()
    if low in ("", "mixed", "all", "random", "compound"):
        return rng.choice(list(ARCHETYPE_BUILDERS.values()))
    if low.startswith("elementary_"):
        trimmed = low[len("elementary_"):]
        if trimmed in DISPATCH_TABLE:
            return DISPATCH_TABLE[trimmed]
    if raw in DISPATCH_TABLE:
        return DISPATCH_TABLE[raw]
    if low in DISPATCH_TABLE:
        return DISPATCH_TABLE[low]
    if low in _LEGACY_ALIASES:
        return ARCHETYPE_BUILDERS[rng.choice(_LEGACY_ALIASES[low])]
    for k, fn in ARCHETYPE_BUILDERS.items():
        if low in k.lower():
            return fn
    return rng.choice(list(ARCHETYPE_BUILDERS.values()))


def generate(
    subskill: str = "mixed",
    difficulty: str = "medium",
    count: int = 1,
    mode: str = "scaffold",
    seed: Optional[int] = None,
    **kwargs: Any,
) -> List[Dict[str, Any]]:
    rng = _rng(seed)
    total = max(1, int(count or 1))
    results: List[Dict[str, Any]] = []
    for _ in range(total):
        fn = _select_builder(subskill, rng)
        q = fn(rng)
        q["difficulty"] = difficulty
        q["mode"] = mode
        results.append(q)
    return results


def generate_question(
    subskill: str = "mixed",
    difficulty: str = "medium",
    seed: Optional[int] = None,
    mode: str = "scaffold",
    **kwargs: Any,
) -> Dict[str, Any]:
    return generate(subskill=subskill, difficulty=difficulty, count=1, mode=mode, seed=seed, **kwargs)[0]
