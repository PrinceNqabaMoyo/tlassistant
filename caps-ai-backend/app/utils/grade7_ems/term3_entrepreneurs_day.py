"""Grade 7 EMS: Term 3 - Entrepreneur's Day Generator (50 Semantic Archetypes).
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/EMS_Gr7/Term 3/01. Entrepreneur's Day.md.
Adheres strictly to the 6-Pillar Generator Contract.
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional

from .term3_entrepreneurs_day_archetypes_01_25 import BUILDERS_01_25
from .term3_entrepreneurs_day_archetypes_26_50 import BUILDERS_26_50

CURRICULUM_DOC = "curriculum_docs_auto/EMS_Gr7/Term 3/01. Entrepreneur's Day.md"
TOPIC_NAME = "Entrepreneur's Day"

ARCHETYPE_BUILDERS: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    **BUILDERS_01_25,
    **BUILDERS_26_50,
}

SUBSKILLS: List[str] = list(ARCHETYPE_BUILDERS.keys())
ORDERED_SUBSKILLS: List[str] = SUBSKILLS

DISPATCH_TABLE: Dict[Any, Callable[[random.Random], Dict[str, Any]]] = dict(ARCHETYPE_BUILDERS)
for idx, key in enumerate(SUBSKILLS, 1):
    DISPATCH_TABLE[idx] = ARCHETYPE_BUILDERS[key]
    DISPATCH_TABLE[f"{idx:02d}"] = ARCHETYPE_BUILDERS[key]

# Legacy backward-compatibility aliases
DISPATCH_TABLE["planning_entrepreneurs_day"] = ARCHETYPE_BUILDERS["03_market_research_buyer_surveys"]
DISPATCH_TABLE["promotional_channels"] = ARCHETYPE_BUILDERS["20_marketing_mix_creative_school_promotion"]
DISPATCH_TABLE["variable_costs_production"] = ARCHETYPE_BUILDERS["26_variable_vs_fixed_stall_costs"]
DISPATCH_TABLE["calculate_profit_simple"] = ARCHETYPE_BUILDERS["34_net_profit_vs_net_loss_calc"]
DISPATCH_TABLE["income_expenditure_statement"] = ARCHETYPE_BUILDERS["39_side_by_side_income_expenditure_statement"]


def get_subskills() -> List[str]:
    """Return the ordered list of 50 semantic subskill archetype IDs."""
    return list(SUBSKILLS)


def _rng(seed: Optional[int]) -> random.Random:
    return random.Random(seed) if seed is not None else random.Random()


def generate(
    subskill: Optional[str] = None,
    difficulty: str = "medium",
    count: int = 1,
    mode: str = "compound",
    seed: Optional[int] = None,
    archetype_index: Optional[int] = None,
    **kwargs: Any,
) -> List[Dict[str, Any]]:
    """Generate questions for Grade 7 EMS Term 3: Entrepreneur's Day."""
    rng = _rng(seed)
    results: List[Dict[str, Any]] = []
    mode_norm = str(mode or "compound").strip()

    for idx_loop in range(max(1, int(count))):
        builder: Optional[Callable[[random.Random], Dict[str, Any]]] = None
        if subskill is not None:
            sub_key = str(subskill).strip()
            if sub_key in DISPATCH_TABLE:
                builder = DISPATCH_TABLE[sub_key]
            else:
                sub_lower = sub_key.lower()
                if sub_lower not in ("", "mixed", "all", "compound", "auto", "default", "none"):
                    for k, b in DISPATCH_TABLE.items():
                        if isinstance(k, str) and (sub_lower in k.lower() or k.lower() in sub_lower):
                            builder = b
                            break

        if builder is None and archetype_index is not None:
            try:
                idx = int(archetype_index)
                if idx in DISPATCH_TABLE:
                    builder = DISPATCH_TABLE[idx]
                elif 1 <= idx <= len(SUBSKILLS):
                    builder = ARCHETYPE_BUILDERS[SUBSKILLS[idx - 1]]
            except (ValueError, TypeError):
                pass

        if builder is None:
            chosen = SUBSKILLS[(idx_loop if count > 1 else rng.randrange(len(SUBSKILLS))) % len(SUBSKILLS)]
            builder = ARCHETYPE_BUILDERS[chosen]

        q = builder(rng)
        q.setdefault("grade", 7)
        q.setdefault("subject", "Economic and Management Sciences")
        q.setdefault("term", 3)
        q.setdefault("topic", TOPIC_NAME)
        q.setdefault("caps_weight_percent", 30)
        q.setdefault("difficulty", difficulty)
        q.setdefault("suggested_duration_mins", max(2, int(int(q.get("marks", 2)) * 1.2)))
        if mode_norm.lower() in ("elementary", "scaffold"):
            q.setdefault("mode", f"elementary_{q.get('subskill', '')}")
        else:
            q.setdefault("mode", mode_norm or "compound")
        results.append(q)

    return results


def generate_question(
    subskill: Optional[str] = None,
    seed: Optional[int] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    """Single question generation entry point."""
    return generate(subskill=subskill, count=1, seed=seed, **kwargs)[0]
