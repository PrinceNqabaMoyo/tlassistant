"""Grade 8 EMS - Term 1: The National Budget (50-Archetype Deterministic Generator).

Grounded strictly in curriculum_docs_auto/EMS_Gr8/Term 1/02. The National Budget.md
and EMS_Gr8/Syllabus.md.
Zero-LLM, deterministic, full South African National Curriculum Standards alignment.
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional

from .national_budget_archetypes_01_25 import BUILDERS_01_25
from .national_budget_archetypes_26_50 import BUILDERS_26_50

TOPIC_KEY = "grade8_ems_national_budget"
LO = "g8_ems_national_budget"

ARCHETYPE_BUILDERS: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    **BUILDERS_01_25,
    **BUILDERS_26_50,
}

SUBSKILLS: List[str] = list(ARCHETYPE_BUILDERS.keys())
ORDERED_SUBSKILLS: List[str] = list(SUBSKILLS)

_LEGACY_ALIASES: Dict[str, List[str]] = {
    "direct_vs_indirect_taxes": [
        "05_direct_tax_definition_and_incidence",
        "06_indirect_tax_definition_and_shifting",
        "07_direct_vs_indirect_taxes_classification_table",
        "08_paye_personal_income_tax_bracket_calculation",
        "09_corporate_business_income_tax_calculation",
        "10_vat_15_percent_forward_calculation",
        "11_vat_15_percent_reverse_extraction",
        "12_vat_zero_rated_basic_foodstuffs_equity",
        "13_sin_tax_excise_purpose_and_price_impact",
        "14_fuel_levy_and_road_accident_fund_mechanism",
        "38_indirect_tax_household_monthly_burden_calc",
    ],
    "government_expenditure_categories": [
        "18_education_spending_allocation_and_growth_impact",
        "19_health_expenditure_free_child_and_clinic_care",
        "20_housing_expenditure_rdp_low_cost_settlements",
        "21_social_welfare_grants_and_hivaids_family_support",
        "22_transport_infrastructure_roads_rail_ports_raf",
        "23_safety_security_and_justice_budget_pillars",
        "24_budget_functional_expenditure_matching_table",
        "25_national_budget_sector_bar_chart_diagram",
        "26_emergency_fund_contingency_reserve_purpose",
        "31_reducing_economic_inequality_five_mechanisms_table",
    ],
    "budget_balance_and_national_debt": [
        "15_government_borrowing_bonds_and_interest_cost",
        "17_budget_deficit_vs_budget_surplus_calculation",
        "36_debt_servicing_crowding_out_social_spending",
        "44_revenue_and_expenditure_balancing_audit_table",
        "45_budget_pie_share_and_percentage_comparison_diagram",
    ],
    "role_of_national_treasury": [
        "01_definition_and_purpose_of_national_budget",
        "02_minister_of_finance_and_national_treasury_roles",
        "03_sars_tax_collection_and_fiscal_year_schedule",
        "27_japanese_2011_tsunami_supply_chain_and_reserve_lesson",
        "39_conditional_grants_to_provinces_and_municipalities",
        "41_fiscal_allocation_trade_offs_opportunity_cost",
        "42_emergency_drought_or_flood_reallocation_calc",
    ],
    "concepts": SUBSKILLS[:20],
    "discussion": [
        "12_vat_zero_rated_basic_foodstuffs_equity",
        "27_japanese_2011_tsunami_supply_chain_and_reserve_lesson",
        "28_fiscal_policy_growth_tax_base_virtuous_cycle_diagram",
        "32_school_nutrition_programme_human_capital_benefit",
        "33_free_basic_water_and_electricity_poverty_alleviation",
        "35_tax_base_expansion_vs_increasing_tax_rates",
        "40_tax_evasion_vs_tax_avoidance_civic_impact",
        "47_smme_tax_compliance_and_formalisation_incentive",
        "50_comprehensive_national_budget_policy_synthesis",
    ],
    "application": [
        "07_direct_vs_indirect_taxes_classification_table",
        "10_vat_15_percent_forward_calculation",
        "11_vat_15_percent_reverse_extraction",
        "17_budget_deficit_vs_budget_surplus_calculation",
        "25_national_budget_sector_bar_chart_diagram",
        "29_subsidies_on_basic_goods_brown_bread_milk",
        "30_public_works_epwp_job_creation_calculation",
        "36_debt_servicing_crowding_out_social_spending",
        "38_indirect_tax_household_monthly_burden_calc",
        "44_revenue_and_expenditure_balancing_audit_table",
        "45_budget_pie_share_and_percentage_comparison_diagram",
        "50_comprehensive_national_budget_policy_synthesis",
    ],
}


def generate_question(
    subskill: Optional[str] = None,
    seed: Optional[int] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    rng = random.Random(seed)
    target = (subskill or "").strip()
    if not target or target in ("mixed", "compound", "default"):
        target = rng.choice(SUBSKILLS)
    elif target in _LEGACY_ALIASES:
        target = rng.choice(_LEGACY_ALIASES[target])
    elif target.startswith("elementary_"):
        candidate = target[len("elementary_"):]
        if candidate in ARCHETYPE_BUILDERS:
            target = candidate
        elif candidate in _LEGACY_ALIASES:
            target = rng.choice(_LEGACY_ALIASES[candidate])
        else:
            target = rng.choice(SUBSKILLS)
    elif target not in ARCHETYPE_BUILDERS:
        matches = [k for k in SUBSKILLS if target in k]
        target = rng.choice(matches) if matches else rng.choice(SUBSKILLS)

    q = ARCHETYPE_BUILDERS[target](rng)
    difficulty = kwargs.get("difficulty")
    if difficulty:
        q["difficulty"] = difficulty
    mode = kwargs.get("mode")
    if mode:
        q["mode"] = mode
    return q


def generate(
    subskill: str = "mixed",
    seed: Optional[int] = None,
    count: int = 1,
    **kwargs: Any,
) -> List[Dict[str, Any]]:
    base_rng = random.Random(seed)
    out: List[Dict[str, Any]] = []
    for i in range(max(1, int(count))):
        item_seed = (seed + i * 1009) if seed is not None else base_rng.randint(1, 10**8)
        out.append(generate_question(subskill=subskill, seed=item_seed, **kwargs))
    return out
