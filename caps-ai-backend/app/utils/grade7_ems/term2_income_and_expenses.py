"""Grade 7 Economic and Management Sciences - Term 2: Income and Expenses Generator.
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/EMS_Gr7/Term 2/02. Income and Expenses.md.
50 Distinct Semantic Archetypes (01 to 50).
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional

from .term2_income_and_expenses_archetypes_01_25 import BUILDERS_01_25
from .term2_income_and_expenses_archetypes_26_50 import BUILDERS_26_50

TOPIC_NAME = "Income and Expenses"
TOPIC_ID = "grade7_ems"
SUBTOPIC_ID = "term2_income_and_expenses"
CURRICULUM_REFERENCE = "Term 2 > Income and Expenses"
CURRICULUM_DOC = "curriculum_docs_auto/EMS_Gr7/Term 2/02. Income and Expenses.md"

ARCHETYPE_BUILDERS: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    **BUILDERS_01_25,
    **BUILDERS_26_50,
}

SUBSKILLS: List[str] = list(ARCHETYPE_BUILDERS.keys())
ORDERED_SUBSKILLS: List[str] = SUBSKILLS

DISPATCH_TABLE: Dict[str, Any] = {
    "def_personal_income": "01_personal_income_definition_wealth",
    "def_personal_expenses": "05_personal_expenses_definition_examples",
    "identify_assets": "09_current_assets_short_term_liquidity",
    "identify_liabilities": "12_current_vs_long_term_liabilities_split",
    "net_worth_equation": "13_net_worth_equation_surplus_deficit_concept",
    "net_worth_math": "15_net_worth_surplus_calculation",
    "render_statement_net_worth": "21_complete_donovan_statement_net_worth_table",
    "savings_wealth_creation": "43_investments_as_forced_tied_up_saving",
    "concepts": [s for s in SUBSKILLS if s[:2] in {"01", "02", "05", "08", "09", "10", "12", "13", "25", "26", "28", "31", "32", "40", "43", "45", "47"}],
    "discussion": [s for s in SUBSKILLS if s[:2] in {"03", "06", "07", "22", "23", "29", "33", "41", "42", "44"}],
    "calculation": [s for s in SUBSKILLS if s[:2] in {"04", "14", "15", "16", "17", "18", "20", "30", "35", "36", "37", "39", "46", "48", "49"}],
    "calculations": [s for s in SUBSKILLS if s[:2] in {"04", "14", "15", "16", "17", "18", "20", "30", "35", "36", "37", "39", "46", "48", "49"}],
    "journal": [s for s in SUBSKILLS if s[:2] in {"11", "19", "21", "24", "27", "34", "38", "50"}],
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
    """Generate questions for Grade 7 EMS Term 2: Income and Expenses."""
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
