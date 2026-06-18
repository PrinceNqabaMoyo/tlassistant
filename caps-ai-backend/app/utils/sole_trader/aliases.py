from __future__ import annotations

from typing import Dict, List, Optional


CREDITORS_CONTROL_ALIASES: List[str] = [
    "Creditors Control",
    "Creditors control",
    "Creditors' Control",
    "Creditors' control",
    "Creditors’ Control",
    "Creditors’ control",
]

DEBTORS_CONTROL_ALIASES: List[str] = [
    "Debtors Control",
    "Debtors control",
    "Debtors' Control",
    "Debtors' control",
    "Debtors’ Control",
    "Debtors’ control",
]

COST_OF_SALES_ALIASES: List[str] = [
    "Cost of sales",
    "Cost of Sales",
]

TRADING_STOCK_ALIASES: List[str] = [
    "Trading stock",
    "Trading Stock",
]


def find_col(headers: List[str], candidates: List[str]) -> Optional[int]:
    if not headers:
        return None
    cand_set = {str(c) for c in candidates}
    for i, h in enumerate(headers):
        if str(h) in cand_set:
            return int(i)
    return None


def header_index_map(headers: List[str]) -> Dict[str, int]:
    return {str(h): int(i) for i, h in enumerate(headers or [])}
