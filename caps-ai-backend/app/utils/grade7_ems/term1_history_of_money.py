"""
Grade 7 EMS — Term 1: History of Money (50 Semantic Archetype Dispatcher).
Grounded in curriculum_docs_auto/EMS_Gr7/Term 1/01. History of money.md.
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional

from .term1_history_of_money_archetypes_01_25 import BUILDERS_01_25
from .term1_history_of_money_archetypes_26_50 import BUILDERS_26_50

CURRICULUM_DOC = "curriculum_docs_auto/EMS_Gr7/Term 1/01. History of money.md"
TOPIC_NAME = "History of money"

ARCHETYPE_BUILDERS: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    **BUILDERS_01_25,
    **BUILDERS_26_50,
}

SUBSKILLS: List[str] = list(ARCHETYPE_BUILDERS.keys())
ORDERED_SUBSKILLS: List[str] = SUBSKILLS

_LEGACY_POOLS: Dict[str, List[str]] = {
    "traditional_vs_modern_societies": [
        "01_traditional_society_definition",
        "02_modern_society_characteristics",
        "03_self_sufficiency_subsistence",
        "04_traditional_vs_modern_table",
        "05_hunter_gatherer_nomadic_living",
        "06_cattle_herding_wealth_lobola",
        "07_environment_shapes_barter_karoo_knysna",
    ],
    "bartering_limitations": [
        "08_bartering_definition_mechanism",
        "09_double_coincidence_of_wants",
        "10_silent_barter_trans_saharan",
        "11_barter_indivisibility_problem",
        "12_barter_perishability_storage",
        "13_barter_valuation_rate_calculation",
        "14_barter_advantages_context",
        "15_barter_disadvantages_table",
    ],
    "promissory_notes_and_receipts": [
        "25_promissory_note_definition_purpose",
        "26_promissory_note_elements_diagram",
        "27_promissory_note_seven_elements_table",
        "28_promissory_note_interest_repayment",
        "29_promissory_note_maturity_days",
        "30_tang_flying_money_arab_suftaja",
        "31_receipts_vs_promissory_notes",
    ],
    "evolution_of_money": [
        "16_early_trade_routes_commodities",
        "17_commodity_money_examples",
        "18_cowrie_shells_properties",
        "19_metal_ingots_weighed_silver",
        "20_early_stamped_coins_lydia_china",
        "21_coin_metals_gold_silver_copper",
        "22_sa_coinage_history_timeline",
        "23_decimalisation_pound_to_rand_1961",
        "24_metal_coinage_disadvantages",
        "32_paper_money_origin_goldsmith_notes",
        "33_sa_paper_money_lombaard_bank",
        "34_representative_vs_fiat_money",
        "35_face_value_vs_intrinsic_value",
        "36_gold_standard_rise_and_end",
        "37_security_features_sa_banknotes",
        "38_electronic_banking_eft_definition",
        "39_electronic_banking_advantages",
        "40_electronic_banking_risks_phishing",
        "41_payment_methods_comparison_table",
        "50_evolution_of_money_synthesis",
    ],
    "functions_of_money": [
        "42_role_medium_of_exchange",
        "43_role_unit_of_account",
        "44_role_store_of_value",
        "45_role_standard_of_deferred_payment",
        "46_four_roles_of_money_table",
        "47_characteristics_durable_divisible_transportable",
        "48_divisibility_change_calculation",
        "49_consumer_economy_spending_cycle",
    ],
    "concepts": [s for s in SUBSKILLS if not s.startswith(("11_", "13_", "23_", "28_", "29_", "35_", "43_", "45_", "48_"))],
    "application": [
        "04_traditional_vs_modern_table",
        "13_barter_valuation_rate_calculation",
        "15_barter_disadvantages_table",
        "23_decimalisation_pound_to_rand_1961",
        "27_promissory_note_seven_elements_table",
        "28_promissory_note_interest_repayment",
        "41_payment_methods_comparison_table",
        "43_role_unit_of_account",
        "45_role_standard_of_deferred_payment",
        "46_four_roles_of_money_table",
        "48_divisibility_change_calculation",
    ],
    "discussion": [
        "03_self_sufficiency_subsistence",
        "06_cattle_herding_wealth_lobola",
        "07_environment_shapes_barter_karoo_knysna",
        "09_double_coincidence_of_wants",
        "10_silent_barter_trans_saharan",
        "14_barter_advantages_context",
        "31_receipts_vs_promissory_notes",
        "34_representative_vs_fiat_money",
        "39_electronic_banking_advantages",
        "40_electronic_banking_risks_phishing",
        "44_role_store_of_value",
        "49_consumer_economy_spending_cycle",
        "50_evolution_of_money_synthesis",
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
