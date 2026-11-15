"""Grade 10 Mathematics — Term 3: Finance and Growth (Deterministic 6-Pillar Generator).

100% Deterministic & Curriculum-Backed. Satisfies the 6-Pillar Generator Contract.
Grounded in curriculum_docs_auto/Mathematics_Gr10/Term 3/01. Finance and growth.md.
50 Distinct Semantic Archetypes (01 to 50).
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional

from .finance_growth_archetypes_01_25 import BUILDERS_01_25, SUBTOPIC_ID, TOPIC_ID, TOPIC_NAME
from .finance_growth_archetypes_26_50 import BUILDERS_26_50

ARCHETYPE_BUILDERS: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    **BUILDERS_01_25,
    **BUILDERS_26_50,
}

SUBSKILLS: List[str] = list(ARCHETYPE_BUILDERS.keys())
ORDERED_SUBSKILLS: List[str] = SUBSKILLS

_LEGACY_ALIASES: Dict[str, str] = {
    "simple_interest": "01_simple_interest_accumulated_amount",
    "compound_interest": "08_compound_interest_annual_accumulation",
    "hire_purchase": "16_hire_purchase_monthly_instalment",
    "exchange_rates": "23_foreign_exchange_convert_zar_to_foreign",
    "inflation": "20_inflation_future_price_compound_growth",
    "population": "22_population_compound_growth",
}

DISPATCH_TABLE: Dict[Any, Callable[[random.Random], Dict[str, Any]]] = {}
for idx, (sid, fn) in enumerate(ARCHETYPE_BUILDERS.items(), start=1):
    DISPATCH_TABLE[sid] = fn
    DISPATCH_TABLE[idx] = fn
    DISPATCH_TABLE[f"{idx:02d}"] = fn
    DISPATCH_TABLE[str(idx)] = fn
for alias, target in _LEGACY_ALIASES.items():
    DISPATCH_TABLE[alias] = ARCHETYPE_BUILDERS[target]


def get_subskills() -> List[str]:
    """Return ordered list of all 50 semantic Finance and Growth subskills."""
    return list(ORDERED_SUBSKILLS)


def _resolve_subskill(
    subskill: Optional[str],
    mode: str,
    archetype_index: Optional[int],
    seed_offset: int,
) -> str:
    if archetype_index is not None:
        return SUBSKILLS[int(archetype_index) % len(SUBSKILLS)]

    cand = str(subskill or "").strip()
    if not cand or cand.lower() in {"mixed", "compound", "all"}:
        if mode.startswith("elementary_") and mode[len("elementary_"):] in ARCHETYPE_BUILDERS:
            return mode[len("elementary_"):]
        return SUBSKILLS[seed_offset % len(SUBSKILLS)]

    if cand.startswith("elementary_"):
        cand = cand[len("elementary_"):]
    if cand in ARCHETYPE_BUILDERS:
        return cand
    if cand.lower() in _LEGACY_ALIASES:
        return _LEGACY_ALIASES[cand.lower()]
    if cand in DISPATCH_TABLE:
        try:
            idx = int(cand) - 1
            return SUBSKILLS[idx % len(SUBSKILLS)]
        except ValueError:
            pass
    return SUBSKILLS[seed_offset % len(SUBSKILLS)]


def generate(
    subskill: Optional[str] = None,
    difficulty: str = "medium",
    count: int = 1,
    mode: str = "scaffold",
    seed: Optional[int] = None,
    archetype_index: Optional[int] = None,
    **kwargs: Any,
) -> List[Dict[str, Any]]:
    """Generate Finance and Growth questions across 50 semantic archetypes."""
    base_seed = int(seed) if seed is not None else random.randint(1, 1_000_000_000)
    results: List[Dict[str, Any]] = []
    topic_override = kwargs.get("topic")

    for i in range(max(1, int(count))):
        sub_rng = random.Random(base_seed + i * 37)
        chosen = _resolve_subskill(subskill, mode, archetype_index, base_seed + i)
        q = ARCHETYPE_BUILDERS[chosen](sub_rng)
        q.setdefault("grade", 10)
        q.setdefault("subject", "Mathematics")
        q["topic"] = topic_override or q.get("topic") or TOPIC_NAME
        q.setdefault("term", 3)
        q.setdefault("difficulty", difficulty)
        q["mode"] = mode
        results.append(q)

    return results


def generate_question(
    subskill: Optional[str] = None,
    seed: Optional[int] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    """Single question generation entry point."""
    return generate(subskill=subskill, count=1, seed=seed, **kwargs)[0]
