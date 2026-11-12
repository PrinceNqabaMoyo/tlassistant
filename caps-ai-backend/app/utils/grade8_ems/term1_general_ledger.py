"""Grade 8 EMS - General Ledger & Trial Balance of a Service Business Generator.
100% Deterministic & Curriculum-Backed. Satisfies the 6-Pillar Generator Contract.
Directly aligns with curriculum_docs_auto/EMS_Gr8/Term 1/01. General ledger and Trial balance of a service business.md.
50 Distinct Semantic Archetypes (01 to 50).
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional

from .general_ledger_archetypes_01_25 import BUILDERS_01_25
from .general_ledger_archetypes_26_50 import BUILDERS_26_50

TOPIC_ID = "grade8_ems"
SUBTOPIC_ID = "term1_general_ledger"
TOPIC_NAME = "General ledger and Trial balance of a service business"
CURRICULUM_REFERENCE = "Term 1 > General Ledger and Trial Balance of a Service Business"

ARCHETYPE_BUILDERS: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    **BUILDERS_01_25,
    **BUILDERS_26_50,
}

SUBSKILLS: List[str] = list(ARCHETYPE_BUILDERS.keys())
ORDERED_SUBSKILLS: List[str] = SUBSKILLS

_LEGACY_ALIASES: Dict[str, str] = {
    "dead_clic_rules": "09_account_normal_balance_classification_table",
    "dead_clic": "07_dead_mnemonic_debit_increase_accounts",
    "posting_crj_cpj": "26_crj_to_bank_and_current_income_t_accounts",
    "balancing_ledger_accounts": "29_balancing_bank_t_account_debit_balance",
    "balancing_accounts": "29_balancing_bank_t_account_debit_balance",
    "trial_balance_preparation": "40_full_trial_balance_preparation_table",
    "trial_balance": "40_full_trial_balance_preparation_table",
    "concepts": "03_double_entry_principle_duality",
}


def generate(
    subskill: Optional[str] = "mixed",
    difficulty: str = "medium",
    count: int = 1,
    mode: str = "scaffold",
    seed: Optional[int] = None,
    **kwargs: Any,
) -> List[Dict[str, Any]]:
    """Generate questions for General Ledger and Trial Balance of a Service Business."""
    base_seed = int(seed) if seed is not None else random.randint(1, 1_000_000_000)
    results: List[Dict[str, Any]] = []

    sub_norm = str(subskill or "mixed").strip()
    mapped_sub = _LEGACY_ALIASES.get(sub_norm.lower(), sub_norm)

    for i in range(max(1, int(count))):
        sub_rng = random.Random(base_seed + i * 19)
        if mapped_sub in ARCHETYPE_BUILDERS:
            chosen = mapped_sub
        else:
            chosen = SUBSKILLS[(base_seed + i) % len(SUBSKILLS)]

        q = ARCHETYPE_BUILDERS[chosen](sub_rng)
        q.setdefault("grade", 8)
        q.setdefault("subject", "Economic and Management Sciences")
        q.setdefault("topic", TOPIC_NAME)
        q.setdefault("term", 1)
        q.setdefault("difficulty", difficulty)
        q["mode"] = mode
        results.append(q)

    return results


def generate_question(
    subskill: Optional[str] = None,
    seed: Optional[int] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    """Single question generation entry point."""
    return generate(subskill=subskill, count=1, seed=seed, **kwargs)[0]
