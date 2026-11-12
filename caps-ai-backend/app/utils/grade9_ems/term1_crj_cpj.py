"""Grade 9 EMS - Cash Receipts Journal & Cash Payments Journal (Sole Trader) Generator.

100% Deterministic & Curriculum-Backed. Satisfies the 6-Pillar Generator Contract.
Directly aligns with:
- curriculum_docs_auto/EMS_Gr9/Term 2/02. Cash receipts journal and Cash payments journal (sole trader).md

50 Distinct Semantic Archetypes (01 to 50) + legacy compatibility keys.
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional

from .term1_crj_cpj_archetypes_01_25 import BUILDERS_01_25, SUBTOPIC_ID, TOPIC_ID, TOPIC_NAME
from .term1_crj_cpj_archetypes_26_50 import BUILDERS_26_50

CURRICULUM_REFERENCE = "Term 1/2 > Cash Journals of a Trading Business"

ARCHETYPE_BUILDERS: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    **BUILDERS_01_25,
    **BUILDERS_26_50,
}

SUBSKILLS: List[str] = list(ARCHETYPE_BUILDERS.keys())
ORDERED_SUBSKILLS: List[str] = SUBSKILLS

_LEGACY_ALIASES: Dict[str, str] = {
    "cost_of_sales": "04_cost_of_sales_from_selling_price_and_markup",
    "elementary_cost_of_sales": "04_cost_of_sales_from_selling_price_and_markup",
    "trading_equation": "23_accounting_equation_cash_sale_dual_entry",
    "elementary_trading_equation": "23_accounting_equation_cash_sale_dual_entry",
    "source_docs_pipeline": "15_source_document_classification_crj_vs_cpj_table",
    "elementary_source_doc_pipeline": "15_source_document_classification_crj_vs_cpj_table",
    "crj": "29_crj_full_multi_transaction_journal_completion",
    "cpj": "38_cpj_full_multi_transaction_journal_completion",
    "concepts": "01_service_vs_trading_business_comparison",
    "markup": "02_what_i_want_what_i_have_markup_framework",
}

DISPATCH_TABLE: Dict[Any, Callable[[random.Random], Dict[str, Any]]] = {}
for idx, key in enumerate(SUBSKILLS, start=1):
    builder = ARCHETYPE_BUILDERS[key]
    DISPATCH_TABLE[key] = builder
    DISPATCH_TABLE[idx] = builder
    DISPATCH_TABLE[str(idx)] = builder
    DISPATCH_TABLE[f"{idx:02d}"] = builder

for legacy_key, target_key in _LEGACY_ALIASES.items():
    DISPATCH_TABLE[legacy_key] = ARCHETYPE_BUILDERS[target_key]

BUILDERS: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    **ARCHETYPE_BUILDERS,
    **{k: ARCHETYPE_BUILDERS[v] for k, v in _LEGACY_ALIASES.items()},
}


def get_subskills() -> List[str]:
    """Return all 50 canonical Grade 9 EMS CRJ & CPJ subskill identifiers."""
    return list(SUBSKILLS)


def _resolve_subskill(subskill: Optional[str], mode: str, kwargs: Dict[str, Any]) -> Optional[str]:
    if "archetype_index" in kwargs and kwargs["archetype_index"] is not None:
        raw_idx = kwargs["archetype_index"]
        if isinstance(raw_idx, int) and 1 <= raw_idx <= len(SUBSKILLS):
            return SUBSKILLS[raw_idx - 1]
    cand = (subskill or "").strip()
    if cand in ARCHETYPE_BUILDERS:
        return cand
    if cand.lower() in _LEGACY_ALIASES:
        return _LEGACY_ALIASES[cand.lower()]
    if mode and mode.strip().lower() in _LEGACY_ALIASES:
        return _LEGACY_ALIASES[mode.strip().lower()]
    if mode and mode.strip() in ARCHETYPE_BUILDERS:
        return mode.strip()
    if cand in DISPATCH_TABLE:
        for k, v in ARCHETYPE_BUILDERS.items():
            if DISPATCH_TABLE[cand] is v:
                return k
    if cand and cand.lower() not in {"mixed", "compound", "all", "default"}:
        low = cand.lower()
        for k in SUBSKILLS:
            if low in k.lower():
                return k
    return None


def generate(
    subskill: str = "mixed",
    difficulty: str = "medium",
    count: int = 1,
    mode: str = "scaffold",
    seed: Optional[int] = None,
    **kwargs: Any,
) -> List[Dict[str, Any]]:
    """Generate deterministic Grade 9 EMS Cash Receipts & Cash Payments Journal questions."""
    base_seed = int(seed) if seed is not None else random.randint(1, 1_000_000_000)
    results: List[Dict[str, Any]] = []
    fixed_key = _resolve_subskill(subskill, mode, kwargs)

    for i in range(max(1, int(count))):
        sub_rng = random.Random(base_seed + i * 29)
        chosen = fixed_key if fixed_key is not None else SUBSKILLS[(base_seed + i) % len(SUBSKILLS)]
        q = ARCHETYPE_BUILDERS[chosen](sub_rng)
        q.setdefault("grade", 9)
        q.setdefault("subject", "Economic and Management Sciences")
        q.setdefault("topic", TOPIC_NAME)
        q.setdefault("topic_id", TOPIC_ID)
        q.setdefault("subtopic_id", SUBTOPIC_ID)
        q.setdefault("term", 1)
        q.setdefault("curriculum_reference", CURRICULUM_REFERENCE)
        q["difficulty"] = difficulty
        q["mode"] = mode
        results.append(q)

    return results


def generate_question(
    subskill: Optional[str] = None,
    seed: Optional[int] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    """Single question generation entry point."""
    return generate(subskill=subskill or "mixed", count=1, seed=seed, **kwargs)[0]
