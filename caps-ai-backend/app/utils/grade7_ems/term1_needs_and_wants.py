"""
Grade 7 EMS — Term 1: Needs and Wants (50 Semantic Archetype Dispatcher).
Grounded in curriculum_docs_auto/EMS_Gr7/Term 1/02. Needs and Wants.md.
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional

from .term1_needs_and_wants_archetypes_01_25 import BUILDERS_01_25
from .term1_needs_and_wants_archetypes_26_50 import BUILDERS_26_50

CURRICULUM_DOC = "curriculum_docs_auto/EMS_Gr7/Term 1/02. Needs and Wants.md"
TOPIC_NAME = "Needs and Wants"

ARCHETYPE_BUILDERS: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    **BUILDERS_01_25,
    **BUILDERS_26_50,
}

SUBSKILLS: List[str] = list(ARCHETYPE_BUILDERS.keys())
ORDERED_SUBSKILLS: List[str] = SUBSKILLS

_LEGACY_POOLS: Dict[str, List[str]] = {
    "primary_vs_secondary_needs": [
        "01_needs_definition_survival",
        "05_primary_needs_survival_list",
        "06_secondary_needs_wellbeing",
        "07_primary_vs_secondary_table",
        "08_prioritising_primary_over_secondary",
        "09_needs_of_individuals",
        "10_family_emotional_social_needs",
    ],
    "needs_vs_wants_classification": [
        "02_wants_definition_desires",
        "03_needs_vs_wants_distinction",
        "04_needs_vs_wants_table",
        "36_luxury_wants_vs_basic_necessities",
        "39_needs_evolution_with_technology",
        "40_maslow_basic_to_higher_hierarchy",
        "47_consumer_rights_vs_want_advertising",
    ],
    "the_basic_economic_problem": [
        "14_unlimited_wants_advertising_effect",
        "15_limited_resources_scarcity_definition",
        "16_basic_economic_problem_statement",
        "21_natural_resources_land_examples",
        "22_labour_human_effort_skills",
        "23_capital_physical_vs_money",
        "24_entrepreneurship_role_innovation",
        "25_four_factors_of_production_table",
        "26_factors_of_production_remuneration_table",
        "49_needs_wants_resource_chain_diagram",
    ],
    "community_service_delivery_needs": [
        "11_community_needs_infrastructure",
        "12_country_national_needs",
        "13_four_levels_of_needs_table",
        "27_business_meets_community_needs",
        "28_government_public_goods_provision",
        "29_municipal_service_delivery_priorities",
        "30_service_delivery_protests_causes",
        "31_rural_vs_urban_community_needs",
        "42_public_vs_private_provision_table",
        "44_sharing_and_community_ubuntu",
        "48_disaster_disrupts_basic_needs",
    ],
    "scarcity_and_choice_evaluation": [
        "17_scarcity_choice_budget_calculation",
        "18_opportunity_cost_tradeoff",
        "19_scarce_time_allocation_choice",
        "20_scarce_water_household_conservation",
        "32_agricultural_food_security_land",
        "33_arable_land_crop_yield_calculation",
        "34_renewable_vs_nonrenewable_resources",
        "35_sustainable_resource_management",
        "37_utility_and_priority_ranking",
        "38_household_income_vs_wants_ratio",
        "41_entrepreneur_spots_unmet_need",
        "43_inflation_impact_on_basic_needs",
        "45_government_budget_tradeoff_country",
        "46_scarcity_price_signal_supply",
        "50_economic_problem_synthesis_essay",
    ],
    "concepts": [
        s
        for s in SUBSKILLS
        if not s.startswith(("08_", "17_", "19_", "20_", "33_", "37_", "38_", "43_", "45_"))
    ],
    "application": [
        "04_needs_vs_wants_table",
        "07_primary_vs_secondary_table",
        "08_prioritising_primary_over_secondary",
        "13_four_levels_of_needs_table",
        "17_scarcity_choice_budget_calculation",
        "19_scarce_time_allocation_choice",
        "20_scarce_water_household_conservation",
        "25_four_factors_of_production_table",
        "26_factors_of_production_remuneration_table",
        "31_rural_vs_urban_community_needs",
        "33_arable_land_crop_yield_calculation",
        "37_utility_and_priority_ranking",
        "38_household_income_vs_wants_ratio",
        "42_public_vs_private_provision_table",
        "43_inflation_impact_on_basic_needs",
        "45_government_budget_tradeoff_country",
    ],
    "discussion": [
        "03_needs_vs_wants_distinction",
        "10_family_emotional_social_needs",
        "12_country_national_needs",
        "16_basic_economic_problem_statement",
        "24_entrepreneurship_role_innovation",
        "29_municipal_service_delivery_priorities",
        "30_service_delivery_protests_causes",
        "32_agricultural_food_security_land",
        "35_sustainable_resource_management",
        "41_entrepreneur_spots_unmet_need",
        "48_disaster_disrupts_basic_needs",
        "50_economic_problem_synthesis_essay",
    ],
}

DISPATCH_TABLE: Dict[Any, Callable[[random.Random], Dict[str, Any]]] = dict(ARCHETYPE_BUILDERS)
for _idx, _sub_key in enumerate(SUBSKILLS, start=1):
    DISPATCH_TABLE[_idx] = ARCHETYPE_BUILDERS[_sub_key]
    DISPATCH_TABLE[str(_idx)] = ARCHETYPE_BUILDERS[_sub_key]
    DISPATCH_TABLE[f"{_idx:02d}"] = ARCHETYPE_BUILDERS[_sub_key]


def get_subskills() -> List[str]:
    return list(SUBSKILLS)


def _resolve_pool(
    subskill: Optional[str],
    mode: str,
    archetype_index: Optional[int],
) -> List[Callable[[random.Random], Dict[str, Any]]]:
    if archetype_index is not None and archetype_index in DISPATCH_TABLE:
        return [DISPATCH_TABLE[archetype_index]]

    if subskill and subskill.startswith("elementary_"):
        subskill = subskill[len("elementary_"):]

    if subskill in DISPATCH_TABLE:
        return [DISPATCH_TABLE[subskill]]

    if subskill:
        key_lower = subskill.strip().lower()
        if key_lower in _LEGACY_POOLS:
            return [ARCHETYPE_BUILDERS[k] for k in _LEGACY_POOLS[key_lower] if k in ARCHETYPE_BUILDERS]
        for k in SUBSKILLS:
            if k.endswith(key_lower) or key_lower in k:
                return [ARCHETYPE_BUILDERS[k]]

    if mode and mode.startswith("elementary_"):
        target = mode[len("elementary_"):]
        if target in DISPATCH_TABLE:
            return [DISPATCH_TABLE[target]]

    return [ARCHETYPE_BUILDERS[k] for k in SUBSKILLS]


def generate(
    count: int = 1,
    seed: Optional[int] = None,
    difficulty: str = "medium",
    mode: str = "compound",
    subskill: Optional[str] = None,
    archetype_index: Optional[int] = None,
    **kwargs: Any,
) -> List[Dict[str, Any]]:
    rng = random.Random(seed) if seed is not None else random.Random()
    pool = _resolve_pool(subskill=subskill, mode=mode, archetype_index=archetype_index)
    n = max(1, int(count))
    results: List[Dict[str, Any]] = []
    for _ in range(n):
        builder = pool[0] if len(pool) == 1 else rng.choice(pool)
        item = builder(rng)
        item["mode"] = mode or "compound"
        if difficulty in ("easy", "medium", "hard") and item.get("difficulty") not in ("easy", "medium", "hard"):
            item["difficulty"] = difficulty
        results.append(item)
    return results


def generate_question(
    subskill: Optional[str] = None,
    seed: Optional[int] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    return generate(count=1, seed=seed, subskill=subskill, **kwargs)[0]
