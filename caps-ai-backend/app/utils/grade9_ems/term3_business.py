"""Grade 9 EMS — Term 3: Functions of a Business (50-Archetype Deterministic Generator).

Grounded strictly in curriculum_docs_auto/EMS_Gr9/Term 4/04. Functions of a business.md,
curriculum_docs/EMS_Gr9/Term 3/11-Functions of a Business.md, and EMS_Gr9/Syllabus.md.
Zero-LLM, 100% deterministic, aligned with South African National Curriculum Standards.
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional

from .term3_business_archetypes_01_25 import BUILDERS_01_25
from .term3_business_archetypes_26_50 import BUILDERS_26_50

TOPIC_ID = "grade9_ems"
SUBTOPIC_ID = "term3_business"
CURRICULUM_REFERENCE = "Term 3 > Entrepreneurship: Functions of a Business"

ARCHETYPE_BUILDERS: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    **BUILDERS_01_25,
    **BUILDERS_26_50,
}

SUBSKILLS: List[str] = list(ARCHETYPE_BUILDERS.keys())
ORDERED_SUBSKILLS: List[str] = list(SUBSKILLS)
DISPATCH_TABLE: Dict[str, Callable[[random.Random], Dict[str, Any]]] = dict(ARCHETYPE_BUILDERS)

_LEGACY_ALIASES: Dict[str, List[str]] = {
    "business_functions": SUBSKILLS,
    "concepts": SUBSKILLS[:25],
    "discussion": [
        "05_planning_and_organising_in_general_management",
        "08_administration_importance_for_decision_making",
        "16_financial_own_vs_borrowed_capital_comparison",
        "20_publicity_crisis_communication_and_csr",
        "27_general_management_strategic_and_succession_risks",
        "29_purchasing_supplier_failure_and_stock_shortage_risk",
        "33_marketing_reputation_and_unsold_inventory_risk",
        "36_human_resources_staff_turnover_and_skills_shortage_risk",
        "39_small_micro_enterprise_multi_hat_owner_challenge",
        "50_holistic_eight_functions_and_risk_governance_synthesis",
    ],
    "application": [
        "02_eight_business_functions_classification_table",
        "04_three_levels_of_management_hierarchy_svg",
        "11_production_function_input_process_output_svg",
        "12_production_quality_control_and_unit_cost_calc",
        "14_marketing_mix_four_ps_classification_table",
        "18_human_resources_sa_labour_legislation_table",
        "24_eight_functions_organisational_ecosystem_svg",
        "25_ntuli_beauty_style_scenario_function_identification",
        "30_purchasing_reorder_point_and_buffer_stock_calculation",
        "32_production_defect_rate_and_scrap_loss_calculation",
        "35_financial_working_capital_and_cash_shortfall_calc",
        "38_function_risk_mitigation_matching_table",
        "42_purchasing_bulk_discount_vs_storage_cost_calculation",
        "43_marketing_promotional_campaign_roi_calculation",
        "44_hr_training_investment_and_productivity_gain_calc",
        "45_risk_impact_vs_likelihood_matrix_svg",
        "46_cross_function_problem_solving_product_recall_case",
        "47_insurable_vs_non_insurable_business_risks_table",
    ],
}


def get_subskills() -> List[str]:
    return list(SUBSKILLS)


def _resolve_target(rng: random.Random, subskill: Optional[str]) -> str:
    target = (subskill or "").strip()
    if not target or target in ("mixed", "compound", "default", "all", "auto"):
        return rng.choice(SUBSKILLS)
    if target in ARCHETYPE_BUILDERS:
        return target
    if target in _LEGACY_ALIASES:
        return rng.choice(_LEGACY_ALIASES[target])
    if target.startswith("elementary_"):
        candidate = target[len("elementary_"):]
        if candidate in ARCHETYPE_BUILDERS:
            return candidate
        if candidate in _LEGACY_ALIASES:
            return rng.choice(_LEGACY_ALIASES[candidate])
        matches = [k for k in SUBSKILLS if candidate in k]
        return rng.choice(matches) if matches else rng.choice(SUBSKILLS)
    matches = [k for k in SUBSKILLS if target in k]
    return rng.choice(matches) if matches else rng.choice(SUBSKILLS)


def generate_question(
    subskill: Optional[str] = None,
    seed: Optional[int] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    rng = random.Random(seed)
    requested = kwargs.get("archetype") or subskill
    target = _resolve_target(rng, requested)
    q = ARCHETYPE_BUILDERS[target](rng)
    difficulty = kwargs.get("difficulty")
    if difficulty:
        q["difficulty"] = difficulty
    mode = kwargs.get("mode")
    if mode:
        q["mode"] = mode
    return q


def generate(
    subskill: str = "business_functions",
    difficulty: str = "medium",
    count: int = 1,
    mode: str = "scaffold",
    seed: Optional[int] = None,
    **kwargs: Any,
) -> List[Dict[str, Any]]:
    base_rng = random.Random(seed)
    out: List[Dict[str, Any]] = []
    for i in range(max(1, int(count))):
        item_seed = (seed + i * 1009) if seed is not None else base_rng.randint(1, 10**8)
        out.append(
            generate_question(
                subskill=subskill,
                seed=item_seed,
                difficulty=difficulty,
                mode=mode,
                **kwargs,
            )
        )
    return out
