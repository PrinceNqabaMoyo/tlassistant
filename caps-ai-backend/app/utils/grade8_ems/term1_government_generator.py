"""Grade 8 EMS - Term 1: Government (50-Archetype Deterministic Generator).

Grounded strictly in curriculum_docs_auto/EMS_Gr8/Term 1/01. Government.md
and EMS_Gr8/Syllabus.md.
Zero-LLM, deterministic, full South African National Curriculum Standards alignment.
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional

from .government_archetypes_01_25 import BUILDERS_01_25
from .government_archetypes_26_50 import BUILDERS_26_50

TOPIC_KEY = "grade8_ems_government"
LO = "g8_ems_government"

ARCHETYPE_BUILDERS: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    **BUILDERS_01_25,
    **BUILDERS_26_50,
}

SUBSKILLS: List[str] = list(ARCHETYPE_BUILDERS.keys())
ORDERED_SUBSKILLS: List[str] = list(SUBSKILLS)

_LEGACY_ALIASES: Dict[str, List[str]] = {
    "three_levels_of_government": [
        "07_three_levels_of_government_hierarchy",
        "08_national_government_scope_and_leadership",
        "09_provincial_government_scope_leadership_and_funding",
        "10_local_government_municipalities_and_leadership",
        "12_three_branches_of_national_government",
        "13_legislative_branch_parliament_lawmaking",
        "14_executive_branch_president_and_cabinet",
        "15_judicial_branch_constitutional_supreme_high_courts",
        "37_sphere_responsibility_five_scenario_table",
        "45_separation_of_powers_checks_and_balances",
    ],
    "roles_of_government_economy": [
        "21_government_assisting_households_public_goods_nonprofit",
        "22_government_food_subsidies_affordability_mechanism",
        "23_social_grants_supporting_vulnerable_households",
        "24_government_as_employer_civil_servants",
        "25_state_owned_enterprises_soes_role",
        "26_smme_support_skills_and_startup_finance",
        "28_physical_infrastructure_roads_ports_railways",
        "29_service_infrastructure_police_fire_health",
        "30_utility_infrastructure_electricity_water_sewerage",
        "32_business_legislation_classification_table",
    ],
    "circular_flow_government_role": [
        "03_economic_participants_households_businesses_government",
        "04_producers_vs_consumers_role_distinction",
        "05_households_as_labour_producers_and_goods_consumers",
        "06_businesses_as_output_producers_and_resource_consumers",
        "27_government_tenders_and_procurement_from_businesses",
        "35_tax_revenue_collection_to_public_service_cycle",
        "36_circular_flow_with_government_role_diagram",
        "39_economic_flow_producer_vs_consumer_summary_table",
    ],
    "municipal_service_delivery": [
        "10_local_government_municipalities_and_leadership",
        "11_constitutional_objectives_of_local_government",
        "17_local_municipal_essential_utility_services",
        "19_ward_councillor_civic_engagement_and_accountability",
        "38_municipal_utility_rate_and_budget_calculation",
        "42_service_delivery_failure_economic_consequences",
        "43_rural_vs_urban_infrastructure_equity",
        "48_civic_tax_compliance_and_municipal_rates_duty",
    ],
    "concepts": SUBSKILLS[:20],
    "discussion": [
        "26_smme_support_skills_and_startup_finance",
        "31_natural_resource_protection_and_sustainability",
        "33_labour_relations_act_worker_employer_balance",
        "41_export_support_trade_and_business_competitiveness",
        "42_service_delivery_failure_economic_consequences",
        "44_intergovernmental_disaster_and_crisis_coordination",
        "46_public_goods_vs_private_goods_comparison",
        "50_holistic_sa_government_economic_ecosystem_synthesis",
    ],
    "application": [
        "27_government_tenders_and_procurement_from_businesses",
        "32_business_legislation_classification_table",
        "36_circular_flow_with_government_role_diagram",
        "37_sphere_responsibility_five_scenario_table",
        "38_municipal_utility_rate_and_budget_calculation",
        "39_economic_flow_producer_vs_consumer_summary_table",
        "47_government_tender_multiplier_and_employment_calc",
        "49_sphere_and_branch_misallocation_audit",
        "50_holistic_sa_government_economic_ecosystem_synthesis",
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
