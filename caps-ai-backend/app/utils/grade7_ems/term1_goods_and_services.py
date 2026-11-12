"""
Grade 7 EMS — Term 1: Goods and Services (50 Semantic Archetype Dispatcher).
Grounded in curriculum_docs_auto/EMS_Gr7/Term 1/03. Goods and Service.md.
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional

from .term1_goods_and_services_archetypes_01_25 import BUILDERS_01_25
from .term1_goods_and_services_archetypes_26_50 import BUILDERS_26_50

CURRICULUM_DOC = "curriculum_docs_auto/EMS_Gr7/Term 1/03. Goods and Service.md"
TOPIC_NAME = "Goods and services"

ARCHETYPE_BUILDERS: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    **BUILDERS_01_25,
    **BUILDERS_26_50,
}

SUBSKILLS: List[str] = list(ARCHETYPE_BUILDERS.keys())
ORDERED_SUBSKILLS: List[str] = SUBSKILLS

_LEGACY_POOLS: Dict[str, List[str]] = {
    "goods_services_classification": [
        "01_goods_tangible_definition",
        "02_services_intangible_definition",
        "03_goods_vs_services_classification_table",
        "04_natural_goods_raw_examples",
        "05_manufactured_goods_processing",
        "06_utility_goods_everyday_function",
        "07_luxury_goods_status_examples",
        "08_consumable_vs_durable_goods",
        "09_capital_goods_production_role",
        "10_seven_categories_of_goods_table",
        "11_essential_vs_nonessential_services",
        "12_consumer_goods_mass_market",
        "44_service_quality_comparison_scenario",
        "45_capital_vs_consumer_good_context",
    ],
    "producer_consumer_roles": [
        "13_producer_definition_value_addition",
        "14_consumer_definition_buying_power",
        "15_producers_and_consumers_interdependence",
        "24_households_as_consumers_budget",
        "25_households_as_producers_labour_factors",
        "26_households_dual_role_circular_flow",
        "47_tuckshop_goods_and_services_inventory",
    ],
    "sector_classification": [
        "16_primary_sector_extraction",
        "17_secondary_sector_manufacturing",
        "18_tertiary_sector_services_retail",
        "19_three_economic_sectors_table",
        "20_production_chain_bread_or_sugar",
        "21_sector_value_added_calculation",
        "22_developing_vs_developed_sector_share",
        "23_sector_interdependence_disruption",
        "46_export_raw_vs_processed_goods_value",
        "49_goods_services_sectors_audit_table",
    ],
    "household_roles_essay": [
        "25_households_as_producers_labour_factors",
        "26_households_dual_role_circular_flow",
        "50_goods_services_sustainability_synthesis",
    ],
    "recycling_benefits": [
        "27_efficient_vs_effective_use_definitions",
        "28_water_scarcity_sa_demand_supply",
        "29_five_water_saving_methods",
        "30_dripping_tap_water_waste_calculation",
        "31_electricity_efficient_appliances_saving",
        "32_reuse_definition_and_examples",
        "33_repair_vs_replace_cost_calculation",
        "34_buying_secondhand_used_goods_benefits",
        "35_reduce_reuse_recycle_table",
        "36_recycling_definition_and_materials",
        "37_recycling_four_step_process",
        "38_recycling_economic_benefits_jobs",
        "39_recycling_environmental_benefits",
        "40_greenhouse_gas_landfill_saving",
        "41_paper_vs_glass_vs_metal_recycling_table",
        "43_sustainable_packaging_consumer_choice",
    ],
    "recycling_discussion": [
        "37_recycling_four_step_process",
        "38_recycling_economic_benefits_jobs",
        "39_recycling_environmental_benefits",
        "42_informal_waste_pickers_value_chain",
        "48_green_jobs_entrepreneur_opportunity",
        "50_goods_services_sustainability_synthesis",
    ],
    "concepts": [
        s
        for s in SUBSKILLS
        if not s.startswith(("21_", "24_", "30_", "31_", "33_", "40_", "46_", "47_"))
    ],
    "application": [
        "03_goods_vs_services_classification_table",
        "10_seven_categories_of_goods_table",
        "11_essential_vs_nonessential_services",
        "19_three_economic_sectors_table",
        "21_sector_value_added_calculation",
        "24_households_as_consumers_budget",
        "30_dripping_tap_water_waste_calculation",
        "31_electricity_efficient_appliances_saving",
        "33_repair_vs_replace_cost_calculation",
        "35_reduce_reuse_recycle_table",
        "40_greenhouse_gas_landfill_saving",
        "41_paper_vs_glass_vs_metal_recycling_table",
        "46_export_raw_vs_processed_goods_value",
        "47_tuckshop_goods_and_services_inventory",
        "49_goods_services_sectors_audit_table",
    ],
    "discussion": [
        "05_manufactured_goods_processing",
        "15_producers_and_consumers_interdependence",
        "20_production_chain_bread_or_sugar",
        "22_developing_vs_developed_sector_share",
        "23_sector_interdependence_disruption",
        "26_households_dual_role_circular_flow",
        "28_water_scarcity_sa_demand_supply",
        "38_recycling_economic_benefits_jobs",
        "39_recycling_environmental_benefits",
        "42_informal_waste_pickers_value_chain",
        "48_green_jobs_entrepreneur_opportunity",
        "50_goods_services_sustainability_synthesis",
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
