"""Grade 8 EMS — The Accounting Cycle (Deterministic 50-Archetype Generator).
Grounded strictly in: curriculum_docs_auto/EMS_Gr8/Term 2/01. the accounting cycle.md

Zero-LLM, 100% deterministic via rng: random.Random, authentic South African context.
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional

from app.utils.grade8_ems.accounting_cycle_archetypes_01_25 import (
    ARCHETYPES_01_25,
    CAPS_WEIGHT_PERCENT,
    LO,
    TERM,
    TOPIC_KEY,
    TOPIC_NAME,
)
from app.utils.grade8_ems.accounting_cycle_archetypes_26_50 import ARCHETYPES_26_50

TOPIC_ID = "grade8_ems"
SUBTOPIC_ID = "term2_accounting_cycle"
CURRICULUM_REFERENCE = "Term 2 > The Accounting Cycle"

ARCHETYPE_BUILDERS: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    **ARCHETYPES_01_25,
    **ARCHETYPES_26_50,
}

ORDERED_SUBSKILLS: List[str] = list(ARCHETYPE_BUILDERS.keys())
SUBSKILLS: List[str] = list(ORDERED_SUBSKILLS)

_LEGACY_ALIASES: Dict[str, List[str]] = {
    "accounting_cycle_definition": ["01_accounting_cycle_definition_period"],
    "source_doc_types": ["03_stage_2_source_documents_origin"],
    "subsidiary_journals": ["04_stage_3_subsidiary_journals_crj_cpj", "10_crj_purpose_and_entries", "11_cpj_purpose_and_entries"],
    "general_ledger_purpose": ["05_stage_4_general_ledger_posting", "16_ledger_t_account_anatomy"],
    "trial_balance_purpose": ["06_stage_5_trial_balance_check", "38_trial_balance_limitation_errors"],
    "accounting_cycle_order": ["08_cycle_sequence_next_step", "09_cycle_sequence_ordering_table"],
    "subsidiary_journals_purpose": ["13_why_journals_precede_ledger", "14_importance_of_subsidiary_journals"],
    "income_statement_vs_balance_sheet": ["39_income_statement_vs_balance_sheet_purpose", "17_balance_sheet_vs_nominal_sections"],
    "accounting_cycle_steps_essay": ["47_sole_trader_end_of_month_checklist", "50_comprehensive_cycle_capstone"],
    "concepts": ORDERED_SUBSKILLS[:25],
    "discussion": ["13_why_journals_precede_ledger", "14_importance_of_subsidiary_journals", "44_nominal_accounts_closing_purpose"],
}

DISPATCH_TABLE: Dict[str, Callable[[random.Random], Dict[str, Any]]] = dict(ARCHETYPE_BUILDERS)
for idx, key in enumerate(ORDERED_SUBSKILLS, start=1):
    DISPATCH_TABLE[str(idx)] = ARCHETYPE_BUILDERS[key]
    DISPATCH_TABLE[f"{idx:02d}"] = ARCHETYPE_BUILDERS[key]


def _rng(seed: Optional[int] = None) -> random.Random:
    return random.Random(seed) if seed is not None else random.Random()


def get_subskills() -> List[str]:
    return list(ORDERED_SUBSKILLS)


def _select_builder(subskill: Optional[str], rng: random.Random) -> Callable[[random.Random], Dict[str, Any]]:
    raw = str(subskill or "mixed").strip()
    low = raw.lower()
    if low in ("", "mixed", "all", "random", "compound"):
        return rng.choice(list(ARCHETYPE_BUILDERS.values()))
    if low.startswith("elementary_"):
        trimmed = low[len("elementary_"):]
        if trimmed in DISPATCH_TABLE:
            return DISPATCH_TABLE[trimmed]
    if raw in DISPATCH_TABLE:
        return DISPATCH_TABLE[raw]
    if low in DISPATCH_TABLE:
        return DISPATCH_TABLE[low]
    if low in _LEGACY_ALIASES:
        return ARCHETYPE_BUILDERS[rng.choice(_LEGACY_ALIASES[low])]
    for k, fn in ARCHETYPE_BUILDERS.items():
        if low in k.lower():
            return fn
    return rng.choice(list(ARCHETYPE_BUILDERS.values()))


def generate(
    subskill: str = "mixed",
    difficulty: str = "medium",
    count: int = 1,
    mode: str = "scaffold",
    seed: Optional[int] = None,
    **kwargs: Any,
) -> List[Dict[str, Any]]:
    rng = _rng(seed)
    total = max(1, int(count or 1))
    results: List[Dict[str, Any]] = []
    for _ in range(total):
        fn = _select_builder(subskill, rng)
        q = fn(rng)
        q["difficulty"] = difficulty
        q["mode"] = mode
        results.append(q)
    return results


def generate_question(
    subskill: str = "mixed",
    difficulty: str = "medium",
    seed: Optional[int] = None,
    mode: str = "scaffold",
    **kwargs: Any,
) -> Dict[str, Any]:
    return generate(subskill=subskill, difficulty=difficulty, count=1, mode=mode, seed=seed, **kwargs)[0]
