from __future__ import annotations

from typing import Any, Dict, List, Optional


def build_journal_row(*, row_index: int, values: List[Optional[str]], editable_cols: List[int]) -> List[Dict[str, Any]]:
    editable = set(int(c) for c in (editable_cols or []))
    cells: List[Dict[str, Any]] = []
    for c, v in enumerate(values):
        cell_id = f"r{row_index}_c{c}"
        cells.append({
            "cell_id": cell_id,
            "value": "" if v is None else str(v),
            "editable": c in editable,
        })
    return cells


def build_prefixed_row(
    *,
    table_index: int,
    row_index: int,
    values: List[Optional[str]],
    editable_cols: List[int],
) -> List[Dict[str, Any]]:
    editable = set(int(c) for c in (editable_cols or []))
    cells: List[Dict[str, Any]] = []
    for c, v in enumerate(values):
        cell_id = f"t{int(table_index)}_r{int(row_index)}_c{int(c)}"
        cells.append({
            "cell_id": cell_id,
            "value": "" if v is None else str(v),
            "editable": c in editable,
        })
    return cells


def journal_editable_cols_by_difficulty(
    *,
    difficulty: str,
    base_editable_cols: List[int],
    total_cols: int,
    mode: str,
) -> List[int]:
    diff = str(difficulty or "easy").strip().lower()
    if diff in ("medium", "hard"):
        difficulty_cols = set(range(3, int(total_cols)))
        base_cols = set(int(c) for c in (base_editable_cols or []))
        return sorted(difficulty_cols | base_cols)
    return list(int(c) for c in (base_editable_cols or []))
