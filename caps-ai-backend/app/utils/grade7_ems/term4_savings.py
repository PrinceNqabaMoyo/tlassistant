"""Grade 7 EMS — Savings: 50-Archetype Deterministic Generator.
100% Aligned with South African National Curriculum Standards (Term 4: Financial Literacy).
Grounded strictly in curriculum_docs_auto/EMS_Gr7/Term 4/01. Savings.md.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from .term4_savings_archetypes_01_25 import BUILDERS_01_25
from .term4_savings_archetypes_26_50 import BUILDERS_26_50

TOPIC_ID = "grade7_ems"
SUBTOPIC_ID = "term4_savings"
TOPIC_NAME = "Savings"
CURRICULUM_REFERENCE = "Term 4 > Financial Literacy: Savings"

ARCHETYPE_BUILDERS: Dict[str, Any] = {
    **BUILDERS_01_25,
    **BUILDERS_26_50,
}

ORDERED_SUBSKILLS: List[str] = list(ARCHETYPE_BUILDERS.keys())
SUBSKILLS: List[str] = list(ORDERED_SUBSKILLS)

LEGACY_ALIAS_MAP: Dict[str, str] = {
    "personal_savings_calc": "02_personal_savings_monthly_calculation",
    "purpose_of_savings": "04_purpose_saving_avoiding_high_interest_credit",
    "stokvel_mechanics": "27_stokvel_rotational_lump_sum_calculation",
    "role_and_services_of_banks": "15_financial_intermediation_flow_diagram",
    "capital_sources": "38_loan_capital_borrowed_with_interest",
    "savings": "01_personal_savings_definition",
    "concepts": "01_personal_savings_definition",
    "discussion": "50_integrated_savings_banking_entrepreneurship_synthesis",
}

DISPATCH_TABLE: Dict[str, Any] = {
    **ARCHETYPE_BUILDERS,
    **{alias: ARCHETYPE_BUILDERS[target] for alias, target in LEGACY_ALIAS_MAP.items()},
}


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
    out.setdefault("mode", mode or "compound")
    out.setdefault("curriculum_reference", CURRICULUM_REFERENCE)
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
    builder = _resolve_builder(subskill)
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
    """Generate `count` deterministic questions for the requested subskill or across all 50 archetypes."""
    rng = random.Random(seed)
    total = max(1, int(count or 1))
    resolved = _resolve_builder(subskill)

    results: List[Dict[str, Any]] = []
    if resolved is not None:
        for _ in range(total):
            q = resolved(rng)
            results.append(_apply_mode_meta(q, difficulty, mode))
        return results

    start_idx = rng.randrange(len(ORDERED_SUBSKILLS))
    for idx in range(total):
        key = ORDERED_SUBSKILLS[(start_idx + idx) % len(ORDERED_SUBSKILLS)]
        q = ARCHETYPE_BUILDERS[key](rng)
        results.append(_apply_mode_meta(q, difficulty, mode))
    return results
