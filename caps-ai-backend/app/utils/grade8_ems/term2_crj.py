"""Grade 8 EMS - Cash Receipts Journal of a Service Business Generator.

100% Deterministic & Curriculum-Backed. Satisfies the 6-Pillar Generator Contract.
Grounded in curriculum_docs_auto/EMS_Gr8/Term 2/
03. Cash receipts journal for a services business 1.md and 2.md.
50 Distinct Semantic Archetypes (01 to 50).
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional

from .crj_archetypes_01_25 import BUILDERS_01_25, SUBTOPIC_ID, TOPIC_NAME
from .crj_archetypes_26_50 import BUILDERS_26_50

TOPIC_ID = "grade8_ems"
CURRICULUM_REFERENCE = "Term 2 > Cash Receipts Journal of a services business"

ARCHETYPE_BUILDERS: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    **BUILDERS_01_25,
    **BUILDERS_26_50,
}

SUBSKILLS: List[str] = list(ARCHETYPE_BUILDERS.keys())
ORDERED_SUBSKILLS: List[str] = SUBSKILLS

_LEGACY_ALIASES: Dict[str, str] = {
    "crj": "27_crj_three_transaction_same_day_and_direct_deposit",
    "crj_starter": "26_crj_two_transaction_starter_journal",
    "crj_comprehensive": "29_crj_five_transaction_comprehensive_journal",
    "crj_accounting_equation": "46_crj_accounting_equation_multi_transaction_summary",
    "crj_account_mapping": "47_crj_account_1_account_2_mapping",
    "concepts": "01_crj_purpose_reducing_ledger_entries",
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
    """Return ordered list of all 50 semantic CRJ subskill IDs."""
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
        # Reverse-lookup canonical ID for numeric keys
        idx = int(cand) - 1
        return SUBSKILLS[idx % len(SUBSKILLS)]
    return SUBSKILLS[seed_offset % len(SUBSKILLS)]


def generate(
    subskill: Optional[str] = "crj",
    difficulty: str = "medium",
    count: int = 1,
    mode: str = "scaffold",
    seed: Optional[int] = None,
    archetype_index: Optional[int] = None,
    **kwargs: Any,
) -> List[Dict[str, Any]]:
    """Generate Cash Receipts Journal questions across 50 semantic archetypes."""
    base_seed = int(seed) if seed is not None else random.randint(1, 1_000_000_000)
    results: List[Dict[str, Any]] = []
    topic_override = kwargs.get("topic")

    for i in range(max(1, int(count))):
        sub_rng = random.Random(base_seed + i * 29)
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
    """Single-question entry point for Cash Receipts Journal."""
    return generate(subskill=subskill, count=1, seed=seed, **kwargs)[0]
