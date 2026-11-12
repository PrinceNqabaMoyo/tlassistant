"""Grade 9 EMS — Term 3: Trade Unions (50-Archetype Deterministic Generator).

Grounded strictly in curriculum_docs_auto/EMS_Gr9/Term 1/01. Trade Unions.md,
curriculum_docs/EMS_Gr9/Term 3/8-Trade unions.md, and EMS_Gr9/Syllabus.md.
Zero-LLM, 100% deterministic, aligned with South African National Curriculum Standards.
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional

from .term3_trade_unions_archetypes_01_25 import BUILDERS_01_25
from .term3_trade_unions_archetypes_26_50 import BUILDERS_26_50

TOPIC_ID = "grade9_ems"
SUBTOPIC_ID = "term3_trade_unions"
CURRICULUM_REFERENCE = "Term 3 > The Economy: Trade Unions"

ARCHETYPE_BUILDERS: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    **BUILDERS_01_25,
    **BUILDERS_26_50,
}

SUBSKILLS: List[str] = list(ARCHETYPE_BUILDERS.keys())
ORDERED_SUBSKILLS: List[str] = list(SUBSKILLS)
DISPATCH_TABLE: Dict[str, Callable[[random.Random], Dict[str, Any]]] = dict(ARCHETYPE_BUILDERS)

_LEGACY_ALIASES: Dict[str, List[str]] = {
    "roles_vs_responsibilities": [
        "17_roles_vs_responsibilities_classification_table",
    ],
    "elementary_roles": [
        "18_collective_bargaining_purpose_and_process",
        "19_union_lobbying_government_on_labour_policy",
        "20_worker_education_training_and_legal_representation",
        "21_shop_steward_workplace_representation_role",
    ],
    "concepts": SUBSKILLS[:20],
    "discussion": [
        "11_post_1994_labour_law_transformation",
        "28_employer_lockout_defensive_industrial_action",
        "34_reasonable_vs_unreasonable_wage_demands_tradeoff",
        "40_benefits_of_trade_unions_to_businesses",
        "41_challenges_posed_by_unions_to_businesses",
        "42_economic_effects_of_strikes_on_gdp_and_communities",
        "44_equitable_wealth_distribution_and_consumer_spending",
        "50_holistic_sa_labour_relations_sustainable_economy_synthesis",
    ],
    "application": [
        "03_major_sa_trade_unions_and_sectors_matching_table",
        "05_four_worker_categories_classification_table",
        "17_roles_vs_responsibilities_classification_table",
        "24_ccma_and_lra_dispute_escalation_diagram",
        "26_forms_of_industrial_action_classification_table",
        "31_no_work_no_pay_principle_and_wage_calculation",
        "32_wage_increase_percentage_and_payroll_cost_calc",
        "33_lost_output_and_productivity_cost_during_strike_svg",
        "39_union_subscriptions_percentage_dues_calculation",
        "45_peaceful_industrial_dialogue_and_investor_confidence",
        "46_employer_vs_employee_rights_balance_table",
        "47_case_study_sa_mining_wage_deadlock_resolution",
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
    subskill: str = "concepts",
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
