"""Grade 8 EMS - Term 3: Levels and functions of management (50-Archetype Deterministic Generator).

Grounded strictly in curriculum_docs_auto/EMS_Gr8/Term 3/02. Levels and functions of management.md
and EMS_Gr8/Syllabus.md.
Zero-LLM, deterministic, full South African National Curriculum Standards alignment.
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional

from .management_archetypes_01_25 import BUILDERS_01_25
from .management_archetypes_26_50 import BUILDERS_26_50

TOPIC_ID = "grade8_ems"
SUBTOPIC_ID = "term3_management"
CURRICULUM_REFERENCE = "Term 3 > Entrepreneurship: Levels and Functions of Management"
TOPIC_KEY = "grade8_ems_management"
LO = "g8_ems_management"

ARCHETYPE_BUILDERS: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    **BUILDERS_01_25,
    **BUILDERS_26_50,
}

SUBSKILLS: List[str] = list(ARCHETYPE_BUILDERS.keys())
ORDERED_SUBSKILLS: List[str] = list(SUBSKILLS)

_LEGACY_ALIASES: Dict[str, List[str]] = {
    "elementary_levels": [
        "02_three_levels_of_management_pyramid_diagram",
        "03_top_management_titles_and_strategic_horizon",
        "04_middle_management_departmental_bridging_role",
        "05_lower_first_line_management_operational_tasks",
        "06_management_levels_classification_table",
        "29_chain_of_command_and_communication_flow_diagram",
        "31_comparing_time_horizons_and_scope_table",
        "32_managing_across_business_functions_overview",
        "44_feedback_loop_bottom_up_to_top_management",
    ],
    "levels": [
        "02_three_levels_of_management_pyramid_diagram",
        "03_top_management_titles_and_strategic_horizon",
        "04_middle_management_departmental_bridging_role",
        "05_lower_first_line_management_operational_tasks",
        "06_management_levels_classification_table",
        "31_comparing_time_horizons_and_scope_table",
    ],
    "elementary_tasks": [
        "07_polc_four_management_tasks_overview",
        "08_planning_task_definition_and_forecasting",
        "09_planning_vs_budget_forecast_calculation",
        "10_organising_task_delegation_and_resource_allocation",
        "11_span_of_control_and_organising_ratio_calculation",
        "12_leading_task_communication_and_staff_motivation",
        "13_controlling_task_standards_and_corrective_action",
        "14_controlling_variance_calculation_actual_vs_budget",
        "15_polc_management_tasks_scenario_table",
        "16_polc_interdependence_why_all_four_matter",
        "33_marketing_manager_polc_application",
        "34_production_manager_quality_and_safety_control",
        "35_finance_manager_cash_budget_and_controlling",
    ],
    "tasks": [
        "07_polc_four_management_tasks_overview",
        "08_planning_task_definition_and_forecasting",
        "10_organising_task_delegation_and_resource_allocation",
        "12_leading_task_communication_and_staff_motivation",
        "13_controlling_task_standards_and_corrective_action",
        "15_polc_management_tasks_scenario_table",
    ],
    "elementary_styles": [
        "17_management_styles_three_types_overview",
        "18_autocratic_style_features_pros_and_cons",
        "19_democratic_participatory_style_features_and_buy_in",
        "20_permissive_laissez_faire_free_rein_delegation",
        "21_management_styles_situational_matching_table",
        "38_comparing_autocratic_democratic_permissive_table",
        "39_blended_adaptive_leadership_by_situation",
    ],
    "styles": [
        "17_management_styles_three_types_overview",
        "18_autocratic_style_features_pros_and_cons",
        "19_democratic_participatory_style_features_and_buy_in",
        "20_permissive_laissez_faire_free_rein_delegation",
        "21_management_styles_situational_matching_table",
        "38_comparing_autocratic_democratic_permissive_table",
    ],
    "elementary_characteristics": [
        "22_characteristics_of_a_good_manager_nine_traits",
        "23_good_manager_taking_responsibility_vs_blaming_staff",
        "24_good_manager_people_skills_and_keeping_staff_happy",
        "25_management_traits_matching_scenario_table",
        "26_good_manager_punctuality_and_organisation",
        "27_good_manager_qualified_and_industry_knowledge",
        "28_good_manager_positive_attitude_and_extra_effort",
        "40_ethical_conduct_and_setting_good_example",
        "41_conflict_resolution_and_people_skills_case",
    ],
    "characteristics": [
        "22_characteristics_of_a_good_manager_nine_traits",
        "23_good_manager_taking_responsibility_vs_blaming_staff",
        "24_good_manager_people_skills_and_keeping_staff_happy",
        "25_management_traits_matching_scenario_table",
        "26_good_manager_punctuality_and_organisation",
        "40_ethical_conduct_and_setting_good_example",
    ],
    "concepts": SUBSKILLS[:20],
    "discussion": [
        "04_middle_management_departmental_bridging_role",
        "16_polc_interdependence_why_all_four_matter",
        "18_autocratic_style_features_pros_and_cons",
        "20_permissive_laissez_faire_free_rein_delegation",
        "23_good_manager_taking_responsibility_vs_blaming_staff",
        "24_good_manager_people_skills_and_keeping_staff_happy",
        "39_blended_adaptive_leadership_by_situation",
        "46_poor_management_warning_signs_and_fixes",
        "50_comprehensive_management_pyramid_polc_and_style_synthesis",
    ],
    "application": [
        "02_three_levels_of_management_pyramid_diagram",
        "06_management_levels_classification_table",
        "09_planning_vs_budget_forecast_calculation",
        "11_span_of_control_and_organising_ratio_calculation",
        "14_controlling_variance_calculation_actual_vs_budget",
        "15_polc_management_tasks_scenario_table",
        "21_management_styles_situational_matching_table",
        "25_management_traits_matching_scenario_table",
        "29_chain_of_command_and_communication_flow_diagram",
        "31_comparing_time_horizons_and_scope_table",
        "34_production_manager_quality_and_safety_control",
        "35_finance_manager_cash_budget_and_controlling",
        "37_departmental_staffing_and_shift_scheduling_calc",
        "42_productivity_efficiency_output_per_worker_calc",
        "43_overtime_cost_control_and_planning_calc",
        "45_management_level_and_polc_matrix_table",
        "48_team_incentive_bonus_and_leading_motivation_calc",
        "49_management_misconception_error_audit_table",
        "50_comprehensive_management_pyramid_polc_and_style_synthesis",
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
    subskill: str = "compound",
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
