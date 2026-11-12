"""Grade 8 EMS — The Markets (Deterministic 50-Archetype Generator).
Grounded strictly in: curriculum_docs_auto/EMS_Gr8/Term 4/02. The markets.md

Zero-LLM, 100% deterministic via rng: random.Random, authentic South African context.
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional

from app.utils.grade8_ems.markets_archetypes_01_25 import (
    ARCHETYPES_01_25,
    CAPS_WEIGHT_PERCENT,
    LO,
    TERM,
    TOPIC_KEY,
    TOPIC_NAME,
)
from app.utils.grade8_ems.markets_archetypes_26_50 import ARCHETYPES_26_50

ARCHETYPE_BUILDERS: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    **ARCHETYPES_01_25,
    **ARCHETYPES_26_50,
}

ORDERED_SUBSKILLS: List[str] = list(ARCHETYPE_BUILDERS.keys())
SUBSKILLS: List[str] = list(ORDERED_SUBSKILLS)

_LEGACY_ALIASES: Dict[str, List[str]] = {
    "definition_and_types_of_markets": ["01_market_definition_non_physical", "02_physical_vs_virtual_online_markets", "03_two_main_market_categories"],
    "goods_and_services_market": ["05_goods_vs_services_classification", "06_wholesale_market_definition_role", "07_retail_market_role_to_consumers"],
    "goods_services_market": ["05_goods_vs_services_classification", "06_wholesale_market_definition_role", "07_retail_market_role_to_consumers"],
    "factor_market_structure": ["26_factor_market_definition_services", "27_four_factors_and_remuneration_match"],
    "factor_market": ["26_factor_market_definition_services", "27_four_factors_and_remuneration_match"],
    "financial_markets": ["34_financial_markets_role_in_economy", "35_capital_market_long_term_funding", "36_jse_and_public_company_shares", "39_money_market_short_term_instruments"],
    "financial_market": ["34_financial_markets_role_in_economy", "35_capital_market_long_term_funding", "39_money_market_short_term_instruments"],
    "labour_market": ["29_labour_market_vacancy_channels", "30_wages_vs_salaries_distinction", "31_wage_vs_overtime_calculation"],
    "market_equilibrium": ["45_supply_demand_shortage_price_signal", "46_supply_demand_surplus_clearance"],
    "supply_demand_curves": ["45_supply_demand_shortage_price_signal", "46_supply_demand_surplus_clearance"],
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
