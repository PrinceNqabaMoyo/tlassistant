"""Grade 8 EMS - Cash Receipts Journal 2 & Cash Payments Journal Generator.

100% Deterministic & Curriculum-Backed. Satisfies the 6-Pillar Generator Contract.
Grounded in curriculum_docs_auto/EMS_Gr8/Term 2/
03. Cash receipts journal for a services business 2.md and
04. Cash payments journal for a services business.md.
50 Distinct Semantic Archetypes (01 to 50).
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional

from .cpj_crj_archetypes_01_25 import BUILDERS_01_25, SUBTOPIC_ID, TOPIC_NAME
from .cpj_crj_archetypes_26_50 import BUILDERS_26_50

TOPIC_ID = "grade8_ems"
CURRICULUM_REFERENCE = "Term 2 > Cash Payments Journal & Combined CRJ/CPJ of a services business"

ARCHETYPE_BUILDERS: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    **BUILDERS_01_25,
    **BUILDERS_26_50,
}

SUBSKILLS: List[str] = list(ARCHETYPE_BUILDERS.keys())
ORDERED_SUBSKILLS: List[str] = SUBSKILLS

_LEGACY_ALIASES: Dict[str, str] = {
    "cpj": "27_cpj_three_transaction_wages_equipment_drawings",
    "cpj_table_completion": "29_cpj_five_transaction_comprehensive_journal",
    "combined_crj_cpj_journal_selection": "41_combined_crj_cpj_transaction_classification_table",
    "cpj_split_cheque_allocation": "22_cpj_split_payment_two_analysis_columns",
    "cpj_drawings_vs_wages_analysis": "24_cpj_owner_drawings_vs_staff_wages",
    "crj_cpj_bank_balance_effect": "45_combined_crj_cpj_closing_bank_balance",
    "cpj_source_cheque_counterfoil": "04_cpj_source_doc_cheque_counterfoil_and_eft",
    "cpj_bank_credit_entry": "09_cpj_bank_column_total_payment_credit_rule",
    "cpj_analysis_columns": "12_cpj_dedicated_analysis_columns_selection",
    "crj_cpj_comparison": "40_crj_vs_cpj_structural_comparison_table",
    "crj_cpj_bank_balance_calc": "46_combined_opening_bank_plus_crj_minus_cpj",
}

DISPATCH_TABLE: Dict[Any, Callable[[random.Random], Dict[str, Any]]] = {}
for idx, (sid, fn) in enumerate(ARCHETYPE_BUILDERS.items(), start=1):
    DISPATCH_TABLE[sid] = fn
    DISPATCH_TABLE[idx] = fn
    DISPATCH_TABLE[f"{idx:02d}"] = fn
    DISPATCH_TABLE[str(idx)] = fn
for alias, target in _LEGACY_ALIASES.items():
    DISPATCH_TABLE[alias] = ARCHETYPE_BUILDERS[target]


def get_subskills() -> List[str]:
    """Return ordered list of all 50 semantic CPJ & Combined CRJ/CPJ subskill IDs."""
    return list(ORDERED_SUBSKILLS)


def _resolve_subskill(
    subskill: Optional[str],
    mode: str,
    archetype_index: Optional[int],
    seed_offset: int,
) -> str:
    if archetype_index is not None:
        return SUBSKILLS[int(archetype_index) % len(SUBSKILLS)]

    cand = str(subskill or "").strip()
    if not cand or cand.lower() in {"mixed", "compound", "all"}:
        if mode.startswith("elementary_") and mode[len("elementary_"):] in ARCHETYPE_BUILDERS:
            return mode[len("elementary_"):]
        return SUBSKILLS[seed_offset % len(SUBSKILLS)]

    if cand.startswith("elementary_"):
        cand = cand[len("elementary_"):]
    if cand in ARCHETYPE_BUILDERS:
        return cand
    if cand.lower() in _LEGACY_ALIASES:
        return _LEGACY_ALIASES[cand.lower()]
    if cand in DISPATCH_TABLE:
        idx = int(cand) - 1
        return SUBSKILLS[idx % len(SUBSKILLS)]
    return SUBSKILLS[seed_offset % len(SUBSKILLS)]


def generate(
    subskill: Optional[str] = "mixed",
    difficulty: str = "medium",
    count: int = 1,
    mode: str = "scaffold",
    seed: Optional[int] = None,
    archetype_index: Optional[int] = None,
    **kwargs: Any,
) -> List[Dict[str, Any]]:
    """Generate Cash Payments Journal & Combined CRJ/CPJ questions across 50 semantic archetypes."""
    base_seed = int(seed) if seed is not None else random.randint(1, 1_000_000_000)
    results: List[Dict[str, Any]] = []
    topic_override = kwargs.get("topic")

    for i in range(max(1, int(count))):
        sub_rng = random.Random(base_seed + i * 31)
        chosen = _resolve_subskill(subskill, mode, archetype_index, base_seed + i)
        q = ARCHETYPE_BUILDERS[chosen](sub_rng)
        q.setdefault("grade", 8)
        q.setdefault("subject", "Economic and Management Sciences")
        q["topic"] = topic_override or q.get("topic") or TOPIC_NAME
        q.setdefault("term", 2)
        q.setdefault("difficulty", difficulty)
        q["mode"] = mode
        results.append(q)

    return results


def generate_question(
    subskill: Optional[str] = None,
    seed: Optional[int] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    """Single-question entry point for Cash Payments Journal & Combined CRJ/CPJ."""
    return generate(subskill=subskill, count=1, seed=seed, **kwargs)[0]
