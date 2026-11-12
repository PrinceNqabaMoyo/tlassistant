"""Grade 8 EMS — Source Documents (Deterministic 50-Archetype Generator).
Grounded strictly in: curriculum_docs_auto/EMS_Gr8/Term 2/02. Source documents.md

Zero-LLM, 100% deterministic via rng: random.Random, authentic South African context.
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional

from app.utils.grade8_ems.source_documents_archetypes_01_25 import (
    ARCHETYPES_01_25,
    CAPS_WEIGHT_PERCENT,
    LO,
    TERM,
    TOPIC_KEY,
    TOPIC_NAME,
)
from app.utils.grade8_ems.source_documents_archetypes_26_50 import ARCHETYPES_26_50

ARCHETYPE_BUILDERS: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    **ARCHETYPES_01_25,
    **ARCHETYPES_26_50,
}

ORDERED_SUBSKILLS: List[str] = list(ARCHETYPE_BUILDERS.keys())
SUBSKILLS: List[str] = list(ORDERED_SUBSKILLS)

_LEGACY_ALIASES: Dict[str, List[str]] = {
    "visual_documents": [
        "04_visual_receipt_plate_reading",
        "05_visual_receipt_missing_calc",
        "07_visual_deposit_slip_total_calc",
        "09_visual_crr_till_slip_audit",
        "12_visual_cheque_counterfoil_plate",
        "16_visual_cash_invoice_plate_calc",
        "18_visual_eft_confirmation_plate",
        "20_visual_bank_statement_extract",
    ],
    "documents": [
        "03_receipt_original_vs_duplicate",
        "06_deposit_slip_original_vs_duplicate",
        "08_cash_register_roll_vs_till_slip",
        "11_cheque_vs_counterfoil_retention",
        "17_eft_proof_of_payment_purpose",
        "19_bank_statement_purpose_items",
    ],
    "reading_documents": [
        "04_visual_receipt_plate_reading",
        "12_visual_cheque_counterfoil_plate",
        "16_visual_cash_invoice_plate_calc",
        "20_visual_bank_statement_extract",
    ],
    "concepts": ORDERED_SUBSKILLS[:25],
    "discussion": [
        "40_sequential_doc_numbering_fraud_check",
        "42_source_doc_retention_five_year_rule",
        "48_digital_vs_paper_source_docs_modern",
        "49_case_study_missing_source_docs_audit",
    ],
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
