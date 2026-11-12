"""
Grade 7 EMS — Term 1: Businesses (50 Semantic Archetype Dispatcher).
Grounded in curriculum_docs_auto/EMS_Gr7/Term 3/02. Businesses.md
and curriculum_docs/EMS_Gr7/Term 1/4-Businesses.md.
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional

from .term1_businesses_archetypes_01_25 import BUILDERS_01_25
from .term1_businesses_archetypes_26_50 import BUILDERS_26_50

CURRICULUM_DOC = "curriculum_docs_auto/EMS_Gr7/Term 3/02. Businesses.md"
TOPIC_NAME = "Businesses"

ARCHETYPE_BUILDERS: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    **BUILDERS_01_25,
    **BUILDERS_26_50,
}

SUBSKILLS: List[str] = list(ARCHETYPE_BUILDERS.keys())
ORDERED_SUBSKILLS: List[str] = SUBSKILLS

_LEGACY_POOLS: Dict[str, List[str]] = {
    "formal_informal_classification": [
        "01_formal_business_definition",
        "02_informal_business_definition",
        "03_formal_vs_informal_classification_table",
        "08_formal_informal_sectors_3x2_examples",
        "19_sars_tax_registration_vat_compliance",
        "37_business_registration_steps_cipc",
        "42_informal_tuckshop_vs_formal_supermarket",
    ],
    "goods_classification": [
        "04_trading_business_model",
        "09_trading_markup_profit_calculation",
        "44_profit_margin_informal_hawker",
    ],
    "manufacturers_def": [
        "05_manufacturing_business_model",
        "10_manufacturing_unit_cost_and_profit",
        "20_haccp_food_and_safety_standards",
        "43_primary_secondary_tertiary_business_flow",
    ],
    "service_business_classification": [
        "06_service_business_model",
        "07_three_business_types_table",
        "11_service_business_daily_income",
    ],
    "primary_sector_def": [
        "26_sa_agriculture_gdp_employment_data",
        "27_drought_maize_1990s_vs_western_cape",
        "28_drought_crop_revenue_loss_calculation",
        "46_sadc_regional_agricultural_trade",
    ],
    "capital_goods_def": [
        "21_business_as_producer_and_consumer",
        "41_loadshedding_infrastructure_shock_cost",
        "43_primary_secondary_tertiary_business_flow",
    ],
    "households_producers_explanation": [
        "21_business_as_producer_and_consumer",
        "45_fixed_vs_working_hours_flexibility",
    ],
    "socio_economic_shocks_on_business": [
        "23_natural_disasters_definition_examples",
        "24_five_impacts_of_disasters_on_business",
        "25_tsunami_flood_supply_chain_ripple",
        "29_formal_vs_informal_disaster_recovery",
        "35_disaster_vs_epidemic_impacts_table",
        "36_insurance_and_emergency_reserves",
        "48_disaster_continuity_planning_strategy",
        "49_business_environment_audit_table",
    ],
    "epidemics_impact": [
        "30_health_epidemics_hiv_tb_definition",
        "31_epidemics_productivity_absenteeism",
        "32_epidemics_household_demand_shift",
        "33_absenteeism_cost_calculation",
        "34_epidemics_affecting_informal_traders",
    ],
    "informal_business_advantages": [
        "14_informal_sector_advantages_flexibility",
        "15_informal_sector_disadvantages_risks",
        "16_developing_country_informal_share",
        "17_banks_loans_informal_barrier",
        "18_apartheid_legacy_and_bbbee_link",
        "38_transition_informal_to_formal_case",
        "39_small_business_employment_creation",
    ],
    "production_stages_exam": [
        "43_primary_secondary_tertiary_business_flow",
        "50_businesses_term_synthesis_evaluation",
    ],
    "concepts": [
        s
        for s in SUBSKILLS
        if not s.startswith(("09_", "10_", "11_", "16_", "26_", "28_", "33_", "39_", "41_", "44_"))
    ],
    "application": [
        "03_formal_vs_informal_classification_table",
        "07_three_business_types_table",
        "09_trading_markup_profit_calculation",
        "10_manufacturing_unit_cost_and_profit",
        "11_service_business_daily_income",
        "16_developing_country_informal_share",
        "22_formal_vs_informal_advantages_table",
        "26_sa_agriculture_gdp_employment_data",
        "28_drought_crop_revenue_loss_calculation",
        "33_absenteeism_cost_calculation",
        "35_disaster_vs_epidemic_impacts_table",
        "39_small_business_employment_creation",
        "41_loadshedding_infrastructure_shock_cost",
        "42_informal_tuckshop_vs_formal_supermarket",
        "44_profit_margin_informal_hawker",
        "49_business_environment_audit_table",
    ],
    "discussion": [
        "08_formal_informal_sectors_3x2_examples",
        "12_formal_sector_advantages_scale",
        "14_informal_sector_advantages_flexibility",
        "15_informal_sector_disadvantages_risks",
        "17_banks_loans_informal_barrier",
        "18_apartheid_legacy_and_bbbee_link",
        "24_five_impacts_of_disasters_on_business",
        "25_tsunami_flood_supply_chain_ripple",
        "29_formal_vs_informal_disaster_recovery",
        "31_epidemics_productivity_absenteeism",
        "32_epidemics_household_demand_shift",
        "34_epidemics_affecting_informal_traders",
        "38_transition_informal_to_formal_case",
        "46_sadc_regional_agricultural_trade",
        "48_disaster_continuity_planning_strategy",
        "50_businesses_term_synthesis_evaluation",
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
    subskill: Optional[str] = None,
    difficulty: str = "medium",
    count: int = 1,
    mode: str = "compound",
    seed: Optional[int] = None,
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
    return generate(subskill=subskill, count=1, seed=seed, **kwargs)[0]
