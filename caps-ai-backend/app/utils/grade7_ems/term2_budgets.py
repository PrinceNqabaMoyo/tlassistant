"""Grade 7 Economic and Management Sciences - Term 2: Budgets Generator.
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/EMS_Gr7/Term 2/03. Budgets.md.
50 Distinct Semantic Archetypes (01 to 50).
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional

from .term2_budgets_archetypes_01_25 import BUILDERS_01_25
from .term2_budgets_archetypes_26_50 import BUILDERS_26_50

TOPIC_NAME = "Budgets"
TOPIC_ID = "grade7_ems"
SUBTOPIC_ID = "term2_budgets"
CURRICULUM_REFERENCE = "Term 2 > Budgets"
CURRICULUM_DOC = "curriculum_docs_auto/EMS_Gr7/Term 2/03. Budgets.md"

ARCHETYPE_BUILDERS: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    **BUILDERS_01_25,
    **BUILDERS_26_50,
}

SUBSKILLS: List[str] = list(ARCHETYPE_BUILDERS.keys())
ORDERED_SUBSKILLS: List[str] = SUBSKILLS

DISPATCH_TABLE: Dict[str, Any] = {
    "def_budget": "01_budget_definition_future_earnings_expenses",
    "budget_surplus_deficit": "08_personal_budget_monthly_savings_surplus_calc",
    "fixed_variable_expense": "12_fixed_vs_variable_personal_expenses_classify",
    "business_budget_comparison": "24_comparing_personal_vs_business_budget_scope",
    "budget_contingency": "15_emergency_savings_separate_from_goal_purchase",
    "budget_variance_eval": "35_interpreting_negative_variance_corrective_action",
    "variance_math": "32_unfavourable_expense_overspend_variance_calc",
    "render_business_budget": "38_celebrate_catering_three_column_variance_table",
    "concepts": [s for s in SUBSKILLS if s[:2] in {"01", "02", "05", "12", "15", "25", "26", "27", "28", "30"}],
    "discussion": [s for s in SUBSKILLS if s[:2] in {"03", "04", "14", "16", "24", "31", "35", "40", "49"}],
    "calculation": [s for s in SUBSKILLS if s[:2] in {"06", "07", "08", "09", "11", "17", "18", "19", "20", "22", "23", "29", "32", "33", "34", "36", "39", "41", "44", "45", "46", "48"}],
    "calculations": [s for s in SUBSKILLS if s[:2] in {"06", "07", "08", "09", "11", "17", "18", "19", "20", "22", "23", "29", "32", "33", "34", "36", "39", "41", "44", "45", "46", "48"}],
    "journal": [s for s in SUBSKILLS if s[:2] in {"10", "13", "21", "37", "38", "42", "43", "47", "50"}],
}


def _rng(seed: Optional[int] = None) -> random.Random:
    return random.Random(seed) if seed is not None else random.Random()


def _resolve_subskill(subskill: Optional[str], rng: random.Random) -> str:
    if subskill and subskill in ARCHETYPE_BUILDERS:
        return subskill
    low = str(subskill or "").strip().lower()
    if low in DISPATCH_TABLE:
        mapped = DISPATCH_TABLE[low]
        return rng.choice(mapped) if isinstance(mapped, list) else mapped
    if low and low not in ("mixed", "all", "auto", "default", "none"):
        for k in SUBSKILLS:
            if low in k.lower():
                return k
    return rng.choice(SUBSKILLS)


def generate(
    subskill: Optional[str] = None,
    difficulty: str = "medium",
    count: int = 1,
    mode: str = "scaffold",
    seed: Optional[int] = None,
    **kwargs: Any,
) -> List[Dict[str, Any]]:
    """Generate questions for Grade 7 EMS Term 2: Budgets."""
    rng = _rng(seed)
    results: List[Dict[str, Any]] = []
    n = max(1, int(count))

    for i in range(n):
        if subskill in (None, "", "mixed", "all", "auto", "default"):
            chosen = SUBSKILLS[i % len(SUBSKILLS)] if n > 1 else rng.choice(SUBSKILLS)
        else:
            chosen = _resolve_subskill(subskill, rng)
        q = ARCHETYPE_BUILDERS[chosen](rng)
        q.setdefault("grade", "7")
        q.setdefault("subject", "Economic and Management Sciences")
        q.setdefault("term", 2)
        q.setdefault("topic", TOPIC_NAME)
        q.setdefault("topic_id", TOPIC_ID)
        q.setdefault("subtopic_id", SUBTOPIC_ID)
        q.setdefault("curriculum_reference", CURRICULUM_REFERENCE)
        q.setdefault("difficulty", difficulty)
        q.setdefault("mode", mode)
        results.append(q)

    return results


def generate_question(
    subskill: Optional[str] = None,
    difficulty: str = "medium",
    mode: str = "scaffold",
    seed: Optional[int] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    """Single-question convenience entrypoint."""
    return generate(subskill=subskill, difficulty=difficulty, count=1, mode=mode, seed=seed, **kwargs)[0]
