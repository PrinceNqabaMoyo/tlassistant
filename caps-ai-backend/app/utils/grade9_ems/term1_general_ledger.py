"""Grade 9 EMS - General Ledger & Trial Balance (Sole Trader) Generator.

100% Deterministic & Curriculum-Backed. Satisfies the 6-Pillar Generator Contract.
Directly aligns with:
- curriculum_docs_auto/EMS_Gr9/Term 2/03. General ledger and Trial balance (sole trader).md

50 Distinct Semantic Archetypes (01 to 50) + legacy compatibility keys.
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional

from .term1_general_ledger_archetypes_01_25 import BUILDERS_01_25, SUBTOPIC_ID, TOPIC_ID, TOPIC_NAME
from .term1_general_ledger_archetypes_26_50 import BUILDERS_26_50

CURRICULUM_REFERENCE = "Term 1/2 > General Ledger and Trial Balance of a Sole Trader"

ARCHETYPE_BUILDERS: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    **BUILDERS_01_25,
    **BUILDERS_26_50,
}

SUBSKILLS: List[str] = list(ARCHETYPE_BUILDERS.keys())
ORDERED_SUBSKILLS: List[str] = SUBSKILLS

_LEGACY_ALIASES: Dict[str, str] = {
    "bank_ledger": "29_bank_ledger_extract_with_bank_table",
    "elementary_bank_ledger": "29_bank_ledger_extract_with_bank_table",
    "trading_stock_ledger": "30_trading_stock_ledger_with_shrinkage_check",
    "elementary_trading_stock_ledger": "30_trading_stock_ledger_with_shrinkage_check",
    "trial_balance": "40_full_sole_trader_trial_balance_compilation",
    "elementary_trial_balance": "40_full_sole_trader_trial_balance_compilation",
    "posting_crj_cpj": "09_crj_full_posting_summary_table",
    "concepts": "01_general_ledger_heading_and_date_rules",
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
    """Return all 50 canonical Grade 9 EMS General Ledger & Trial Balance subskill identifiers."""
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
    """Generate deterministic Grade 9 EMS General Ledger & Trial Balance questions."""
    base_seed = int(seed) if seed is not None else random.randint(1, 1_000_000_000)
    results: List[Dict[str, Any]] = []
    fixed_key = _resolve_subskill(subskill, mode, kwargs)

    for i in range(max(1, int(count))):
        sub_rng = random.Random(base_seed + i * 31)
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
