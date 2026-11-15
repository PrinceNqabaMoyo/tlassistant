"""Grade 12 Mathematics - Financial Mathematics: 50-Archetype Deterministic Generator.
100% Aligned with South African National Curriculum Standards (CAPS Grade 12 Paper 1).
Grounded strictly in curriculum_docs_auto/Mathematics_Gr12/Term 2/01. Finance.md and Syllabus.md.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from .finance_archetypes_01_25 import BUILDERS_01_25
from .finance_archetypes_26_50 import BUILDERS_26_50

TOPIC_ID = "grade12_mathematics"
SUBTOPIC_ID = "grade12_math_finance"
TOPIC_NAME = "Finance"
CURRICULUM_REFERENCE = "Grade 12 Mathematics > Term 2 > Finance (Paper 1)"

ARCHETYPE_BUILDERS: Dict[str, Any] = {
    **BUILDERS_01_25,
    **BUILDERS_26_50,
}

ORDERED_SUBSKILLS: List[str] = list(ARCHETYPE_BUILDERS.keys())
SUBSKILLS: List[str] = list(ORDERED_SUBSKILLS)

LEGACY_ALIAS_MAP: Dict[str, str] = {
    "future_value_annuity": "01_future_value_annuity_monthly_investment",
    "present_value_annuity": "11_present_value_annuity_home_loan_monthly_payment",
    "sinking_fund": "22_sinking_fund_monthly_deposit_calculation",
    "effective_nominal_rate": "23_nominal_vs_effective_interest_rate_annual",
    "loan_outstanding_balance": "16_outstanding_balance_loan_backward_method",
    "annuity_solve_n": "03_future_value_annuity_solve_time_period_n_log",
    "concepts": "01_future_value_annuity_monthly_investment",
}

DISPATCH_TABLE: Dict[str, Any] = {
    **ARCHETYPE_BUILDERS,
    **{alias: ARCHETYPE_BUILDERS[target] for alias, target in LEGACY_ALIAS_MAP.items() if target in ARCHETYPE_BUILDERS},
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
    out.setdefault("term", 2)
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
        builder = rng.choice(list(ARCHETYPE_BUILDERS.values()))
    q = builder(rng)
    return _apply_mode_meta(q, difficulty, mode)


def generate(
    subskill: Optional[str] = None,
    count: int = 1,
    seed: Optional[int] = None,
    **kwargs: Any,
) -> List[Dict[str, Any]]:
    """Primary 6-pillar entry point returning a list of generated question dicts."""
    rng = random.Random(seed)
    total = max(1, int(count or 1))
    results: List[Dict[str, Any]] = []

    target = subskill or kwargs.get("mode")
    builder = _resolve_builder(target)

    for i in range(total):
        item_seed = rng.randint(1000, 999999) if seed is not None else None
        item_rng = random.Random(item_seed)
        if builder is not None:
            chosen_builder = builder
        else:
            chosen_builder = ARCHETYPE_BUILDERS[ORDERED_SUBSKILLS[i % len(ORDERED_SUBSKILLS)]]
        q = chosen_builder(item_rng)
        q = _apply_mode_meta(q, kwargs.get("difficulty", "medium"), kwargs.get("mode", "scaffold"))
        results.append(q)

    return results


def generate_questions(
    count: int = 1,
    seed: Optional[int] = None,
    subskill: Optional[str] = None,
    **kwargs: Any,
) -> List[Dict[str, Any]]:
    """Legacy alias supporting generator_registry adapt_multi_item_generator."""
    return generate(subskill=subskill, count=count, seed=seed, **kwargs)
