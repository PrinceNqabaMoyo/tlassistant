"""Grade 8 EMS - Term 3: Forms of ownership (50-Archetype Deterministic Generator).

Grounded strictly in curriculum_docs_auto/EMS_Gr8/Term 3/01. Forms of ownership.md
and EMS_Gr8/Syllabus.md.
Zero-LLM, deterministic, full South African National Curriculum Standards alignment.
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional

from .ownership_archetypes_01_25 import BUILDERS_01_25
from .ownership_archetypes_26_50 import BUILDERS_26_50

TOPIC_KEY = "grade8_ems_ownership"
LO = "g8_ems_ownership"

ARCHETYPE_BUILDERS: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    **BUILDERS_01_25,
    **BUILDERS_26_50,
}

SUBSKILLS: List[str] = list(ARCHETYPE_BUILDERS.keys())
ORDERED_SUBSKILLS: List[str] = list(SUBSKILLS)

_LEGACY_ALIASES: Dict[str, List[str]] = {
    "sole_trader_characteristics": [
        "01_sole_trader_definition_and_single_owner",
        "02_sole_trader_advantages_and_disadvantages",
        "03_sole_trader_unlimited_liability_risk_calculation",
        "20_sole_trader_vs_partnership_capital_and_skills_tradeoff",
        "38_sole_trader_income_statement_to_owner_drawings_calc",
    ],
    "partnerships_characteristics": [
        "04_partnership_owner_range_and_agreement",
        "05_partnership_profit_sharing_ratio_calculation",
        "06_partnership_joint_liability_and_continuity_exit",
        "22_partnership_capital_contribution_and_debt_shortfall",
        "48_partnership_dispute_without_written_agreement",
    ],
    "close_corporation_characteristics": [
        "07_close_corporation_cc_members_and_ck1_statement",
        "08_close_corporation_legal_entity_and_continuity",
        "44_close_corporation_legacy_status_and_conversion_option",
    ],
    "companies_private_vs_public": [
        "09_private_company_pty_ltd_name_and_share_restrictions",
        "10_private_company_moi_and_cipc_registration",
        "11_public_company_ltd_minimums_jse_and_prospectus",
        "12_prospectus_purpose_for_public_share_offer",
        "13_dividends_and_shareholder_return_calculation",
        "21_private_co_vs_public_co_capital_raising_and_control",
        "25_coca_cola_sa_pty_ltd_case_study_classification",
        "37_public_sector_soe_vs_public_company_distinction",
        "39_private_company_shareholder_voting_percentage_calc",
        "41_cipc_compliance_and_annual_audit_requirement",
    ],
    "smme_and_sustainable_job_creation": [
        "26_smme_definition_and_ownership_types",
        "27_smme_role_in_sustainable_job_creation",
        "28_smme_skills_transfer_and_youth_employment",
        "29_business_growth_progression_sole_to_company",
        "34_sustainable_use_of_renewable_resources",
        "35_non_renewable_resources_and_alternative_innovation",
        "36_large_company_ecological_footprint_vs_smme",
        "42_economic_growth_exports_and_smme_competitiveness",
        "47_corporate_social_and_environmental_sustainability_calc",
        "50_holistic_entrepreneurship_ownership_and_sustainability_synthesis",
    ],
    "liability_and_legal_persona_comparison": [
        "14_legal_entity_concept_suing_and_property_ownership",
        "15_limited_vs_unlimited_liability_case_comparison",
        "16_continuity_of_existence_across_ownership_forms",
        "17_naming_suffixes_identification_table",
        "18_owner_count_and_leadership_structure_table",
        "19_liability_and_legal_persona_comparison_table",
        "23_formation_documents_matching_table",
        "24_ownership_spectrum_svg_diagram_comparison",
        "40_converting_partnership_to_pty_ltd_scenario",
        "45_capital_to_liability_break_even_risk_diagram",
    ],
    "concepts": SUBSKILLS[:18],
    "discussion": [
        "02_sole_trader_advantages_and_disadvantages",
        "06_partnership_joint_liability_and_continuity_exit",
        "15_limited_vs_unlimited_liability_case_comparison",
        "27_smme_role_in_sustainable_job_creation",
        "29_business_growth_progression_sole_to_company",
        "33_decision_making_speed_vs_corporate_governance",
        "35_non_renewable_resources_and_alternative_innovation",
        "40_converting_partnership_to_pty_ltd_scenario",
        "48_partnership_dispute_without_written_agreement",
        "50_holistic_entrepreneurship_ownership_and_sustainability_synthesis",
    ],
    "application": [
        "03_sole_trader_unlimited_liability_risk_calculation",
        "05_partnership_profit_sharing_ratio_calculation",
        "13_dividends_and_shareholder_return_calculation",
        "17_naming_suffixes_identification_table",
        "18_owner_count_and_leadership_structure_table",
        "19_liability_and_legal_persona_comparison_table",
        "22_partnership_capital_contribution_and_debt_shortfall",
        "23_formation_documents_matching_table",
        "24_ownership_spectrum_svg_diagram_comparison",
        "31_profit_distribution_across_ownership_forms_table",
        "38_sole_trader_income_statement_to_owner_drawings_calc",
        "39_private_company_shareholder_voting_percentage_calc",
        "43_choosing_best_ownership_form_case_studies_table",
        "45_capital_to_liability_break_even_risk_diagram",
        "47_corporate_social_and_environmental_sustainability_calc",
        "49_ownership_misconception_error_audit_table",
        "50_holistic_entrepreneurship_ownership_and_sustainability_synthesis",
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
