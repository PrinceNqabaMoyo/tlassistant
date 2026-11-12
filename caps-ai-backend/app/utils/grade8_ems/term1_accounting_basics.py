"""Grade 8 EMS — Accounting Concepts (Deterministic 50-Archetype Generator).
Grounded strictly in: curriculum_docs_auto/EMS_Gr8/Term 2/01. Accounting concepts.md

Zero-LLM, 100% deterministic via rng: random.Random, authentic South African context.
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional

from app.utils.grade8_ems.accounting_basics_archetypes_01_25 import (
    ARCHETYPES_01_25,
    CAPS_WEIGHT_PERCENT,
    LO,
    TERM,
    TOPIC_KEY,
    TOPIC_NAME,
)
from app.utils.grade8_ems.accounting_basics_archetypes_26_50 import ARCHETYPES_26_50

ARCHETYPE_BUILDERS: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    **ARCHETYPES_01_25,
    **ARCHETYPES_26_50,
}

ORDERED_SUBSKILLS: List[str] = list(ARCHETYPE_BUILDERS.keys())
SUBSKILLS: List[str] = list(ORDERED_SUBSKILLS)

_LEGACY_ALIASES: Dict[str, List[str]] = {
    "capital_and_owners_equity": [
        "01_capital_definition_contribution",
        "02_own_vs_borrowed_capital",
        "03_owners_equity_net_worth_calc",
        "04_drawings_cash_and_goods_impact",
    ],
    "assets_classification": [
        "05_fixed_non_current_assets_id",
        "06_current_assets_id",
        "07_cash_float_vs_petty_cash",
        "08_debtors_control_current_asset",
        "09_financial_investments_as_assets",
        "10_total_assets_calculation",
    ],
    "liabilities_classification": [
        "11_long_term_liabilities_id",
        "12_current_liabilities_id",
        "13_bank_vs_bank_overdraft_distinction",
        "14_creditors_vs_debtors_misconception",
        "15_total_liabilities_calculation",
    ],
    "income_and_expenses": [
        "16_service_vs_trading_income",
        "17_operating_expenses_classification",
        "18_asset_vs_expense_confusion",
    ],
    "profit_and_loss_calculation": [
        "19_profit_calculation_basic",
        "20_loss_calculation_basic",
        "21_missing_income_or_expense_reverse",
    ],
    "accounting_equation": [
        "22_accounting_equation_missing_term",
        "23_classify_accounts_table_drill",
        "24_accounting_equation_table_effect",
        "25_transaction_to_equity_impact",
    ],
    "concepts": ORDERED_SUBSKILLS[:25],
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
