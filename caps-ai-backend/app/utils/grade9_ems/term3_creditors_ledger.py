"""Grade 9 EMS — Credit transactions (Creditors 2): 50-Archetype Deterministic Generator.
100% Aligned with South African National Curriculum Standards (Term 3: Financial Literacy).
Grounded strictly in curriculum_docs_auto/EMS_Gr9/Term 3/01. Credit transactions (Creditors 2).md.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from .term3_creditors_ledger_archetypes_01_25 import BUILDERS_01_25
from .term3_creditors_ledger_archetypes_26_50 import BUILDERS_26_50

TOPIC_ID = "grade9_ems"
SUBTOPIC_ID = "term3_creditors_ledger"
TOPIC_NAME = "Credit transactions (Creditors 2)"
CURRICULUM_REFERENCE = "Term 3 > Financial Literacy: Credit transactions (Creditors 2)"

ARCHETYPE_BUILDERS: Dict[str, Any] = {
    **BUILDERS_01_25,
    **BUILDERS_26_50,
}

ORDERED_SUBSKILLS: List[str] = list(ARCHETYPE_BUILDERS.keys())
SUBSKILLS: List[str] = list(ORDERED_SUBSKILLS)

LEGACY_ALIAS_MAP: Dict[str, str] = {
    "creditors_ledger_account": "20_three_column_creditors_ledger_with_caj_return_2d_table",
    "creditors_reconciliation": "31_compiling_creditors_list_2d_table",
    "concepts": "01_credit_transaction_and_creditor_current_liability",
}

DISPATCH_TABLE: Dict[str, Any] = {
    **ARCHETYPE_BUILDERS,
    **{alias: ARCHETYPE_BUILDERS[target] for alias, target in LEGACY_ALIAS_MAP.items()},
}

BUILDERS: Dict[str, Any] = DISPATCH_TABLE


def get_subskills() -> List[str]:
    """Return the ordered list of 50 semantic subskill identifiers."""
    return list(ORDERED_SUBSKILLS)


def _resolve_builder(subskill: Optional[str]) -> Optional[Any]:
    if not subskill:
        return None
    raw = str(subskill).strip()
    if raw in DISPATCH_TABLE:
        return DISPATCH_TABLE[raw]
    lowered = raw.lower()
    if lowered in DISPATCH_TABLE:
        return DISPATCH_TABLE[lowered]
    if lowered.startswith("elementary_"):
        stripped = lowered[len("elementary_"):]
        if stripped in DISPATCH_TABLE:
            return DISPATCH_TABLE[stripped]
        lowered = stripped
    if lowered in ("compound", "all", "mixed", "auto", "default", "none", "general"):
        return None
    for key, builder in ARCHETYPE_BUILDERS.items():
        if lowered in key.lower():
            return builder
    return None


def _apply_mode_meta(q: Dict[str, Any], difficulty: str, mode: str) -> Dict[str, Any]:
    out = dict(q)
    out.setdefault("difficulty", difficulty or "medium")
    if mode and (mode == "compound" or str(mode).startswith("elementary_")):
        out["mode"] = mode
    else:
        out.setdefault("mode", "compound")
    out.setdefault("curriculum_reference", CURRICULUM_REFERENCE)
    out.setdefault("term", 3)
    return out


def generate_question(
    subskill: Optional[str] = None,
    difficulty: str = "medium",
    mode: str = "scaffold",
    seed: Optional[int] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    """Generate a single question dictionary for the requested subskill or random archetype."""
    rng = random.Random(seed)
    target = subskill or (mode if isinstance(mode, str) and mode.startswith("elementary_") else None)
    builder = _resolve_builder(target)
    if builder is None:
        chosen_key = rng.choice(ORDERED_SUBSKILLS)
        builder = ARCHETYPE_BUILDERS[chosen_key]
    q = builder(rng)
    return _apply_mode_meta(q, difficulty, mode)


def generate(
    subskill: Optional[str] = None,
    difficulty: str = "medium",
    count: int = 1,
    mode: str = "scaffold",
    seed: Optional[int] = None,
    **kwargs: Any,
) -> List[Dict[str, Any]]:
    """Generate `count` deterministic questions for Credit transactions (Creditors 2)."""
    total = max(1, int(count or 1))
    rng = random.Random(seed)
    target = subskill or (mode if isinstance(mode, str) and mode.startswith("elementary_") else None)
    fixed_builder = _resolve_builder(target)
    results: List[Dict[str, Any]] = []
    pool = list(ORDERED_SUBSKILLS)
    if fixed_builder is None and total <= len(pool):
        chosen_keys = rng.sample(pool, total)
        for key in chosen_keys:
            item_seed = rng.randint(1, 10_000_000)
            q = ARCHETYPE_BUILDERS[key](random.Random(item_seed))
            results.append(_apply_mode_meta(q, difficulty, mode))
        return results
    for idx in range(total):
        item_seed = None if seed is None else (seed * 1009 + idx * 97 + 13)
        item_rng = random.Random(item_seed)
        if fixed_builder is not None:
            q = fixed_builder(item_rng)
        else:
            key = rng.choice(pool)
            q = ARCHETYPE_BUILDERS[key](item_rng)
        results.append(_apply_mode_meta(q, difficulty, mode))
    return results
