"""Grade 9 EMS — Term 4: Business Plan (50-Archetype Deterministic Generator).

Grounded strictly in curriculum_docs_auto/EMS_Gr9/Term 4/04. Business Plan.md
and EMS_Gr9/Syllabus.md.
Zero-LLM, 100% deterministic, aligned with South African National Curriculum Standards.
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional

from .term4_business_plan_archetypes_01_25 import BUILDERS_01_25
from .term4_business_plan_archetypes_26_50 import BUILDERS_26_50

TOPIC_ID = "grade9_ems"
SUBTOPIC_ID = "term4_business_plan"
CURRICULUM_REFERENCE = "Term 4 > Entrepreneurship: Business Plan"

ARCHETYPE_BUILDERS: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    **BUILDERS_01_25,
    **BUILDERS_26_50,
}

SUBSKILLS: List[str] = list(ARCHETYPE_BUILDERS.keys())
ORDERED_SUBSKILLS: List[str] = list(SUBSKILLS)
DISPATCH_TABLE: Dict[str, Callable[[random.Random], Dict[str, Any]]] = dict(ARCHETYPE_BUILDERS)

_LEGACY_ALIASES: Dict[str, List[str]] = {
    "breakeven_analysis": [
        "32_breakeven_point_units_formula_calculation",
        "33_breakeven_point_rand_turnover_value_calculation",
        "34_breakeven_graph_interpretation_tr_tc_fc_svg",
        "35_margin_of_safety_units_and_rand_calculation",
        "36_target_profit_required_sales_volume_calculation",
        "37_effect_of_price_or_cost_change_on_bep_sensitivity",
    ],
    "cost_classification": [
        "28_fixed_vs_variable_costs_classification_table",
        "29_semi_variable_and_stepped_fixed_costs_concept",
        "30_total_cost_tc_linear_equation_calculation",
    ],
    "swot_analysis": [
        "14_swot_analysis_internal_vs_external_classification_table",
        "15_swot_matrix_four_quadrants_diagram_svg",
        "16_converting_swot_weaknesses_and_threats_into_strategy",
    ],
    "concepts": SUBSKILLS[:25],
    "discussion": [
        "02_business_plan_external_audience_investors_lenders",
        "05_executive_summary_purpose_and_four_aspects",
        "13_economic_and_social_macro_factors_impact",
        "16_converting_swot_weaknesses_and_threats_into_strategy",
        "21_promotional_mix_advertising_sales_promo_pr_direct",
        "24_operational_production_plan_capacity_and_suppliers",
        "47_breakeven_unit_economics_and_pricing_strategy_case",
        "49_business_plan_review_updating_and_viability_check",
        "50_holistic_sa_business_plan_and_financial_viability_synthesis",
    ],
    "application": [
        "07_vision_mission_goals_and_objectives_table",
        "10_legal_requirements_bcea_lra_nca_and_licences_table",
        "12_pestle_macro_environment_analysis_table",
        "14_swot_analysis_internal_vs_external_classification_table",
        "15_swot_matrix_four_quadrants_diagram_svg",
        "23_seven_strategies_to_overcome_competition_table",
        "25_management_plan_organogram_and_key_roles_svg",
        "27_startup_capital_vs_operating_working_capital_calc",
        "28_fixed_vs_variable_costs_classification_table",
        "30_total_cost_tc_linear_equation_calculation",
        "31_contribution_margin_per_unit_and_ratio",
        "32_breakeven_point_units_formula_calculation",
        "33_breakeven_point_rand_turnover_value_calculation",
        "34_breakeven_graph_interpretation_tr_tc_fc_svg",
        "35_margin_of_safety_units_and_rand_calculation",
        "36_target_profit_required_sales_volume_calculation",
        "37_effect_of_price_or_cost_change_on_bep_sensitivity",
        "38_cost_price_selling_price_and_markup_percentage_calc",
        "39_calculating_selling_price_from_cost_and_markup_pct",
        "40_calculating_cost_price_backward_from_selling_price",
        "42_projected_income_statement_revenue_expenses_profit",
        "43_net_profit_percentage_on_revenue_calculation",
        "45_balance_sheet_accounting_equation_assets_liabilities_equity",
        "46_break_even_loss_vs_profit_decision_scenarios_table",
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
    subskill: str = "breakeven_analysis",
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
