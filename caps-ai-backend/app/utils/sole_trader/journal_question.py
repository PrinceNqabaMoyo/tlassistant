from __future__ import annotations

from typing import Any, Dict, List, Optional

from .column_help import headers_to_column_help
from .core import make_id


def make_journal(
    *,
    prompt: str,
    journal_type: str,
    headers: List[str],
    rows: List[List[Dict[str, Any]]],
    correct_map: Dict[str, Any],
    guidelines: Optional[List[str]] = None,
    table_variant: str = "studio",
    column_help: Optional[Dict[str, str]] = None,
    row_help: Optional[Dict[str, str]] = None,
    header_rows: Optional[List[List[Dict[str, Any]]]] = None,
    title_fields: Optional[List[Dict[str, Any]]] = None,
    cell_hints: Optional[Dict[str, str]] = None,
    cell_teaching_map: Optional[Dict[str, Dict[str, str]]] = None,
    derivation_map: Optional[Dict[str, str]] = None,
    working_map: Optional[Dict[str, str]] = None,
    rubric_map: Optional[Dict[str, Dict[str, Any]]] = None,
    dependency_map: Optional[Dict[str, List[str]]] = None,
) -> Dict[str, Any]:
    
    if column_help is None:
        try:
            column_help = headers_to_column_help(journal_type=journal_type, headers=headers)
        except Exception:
            column_help = {}

    journal: Dict[str, Any] = {
        "journal_type": journal_type,
        "table_variant": table_variant,
        "headers": headers,
        "rows": rows,
        "column_help": column_help or {},
        "row_help": row_help or {},
    }
    if header_rows:
        journal["header_rows"] = header_rows
    if title_fields:
        journal["title_fields"] = title_fields

    out: Dict[str, Any] = {
        "id": make_id("acct10_st_journal"),
        "question_type": "journal",
        "prompt": prompt,
        "journal": journal,
        "correct_map": correct_map,
        "guidelines": guidelines or [],
        "expected_answer_type": "journal",
    }
    if cell_hints:
        out["cell_hints"] = cell_hints
    if cell_teaching_map:
        out["cell_teaching_map"] = cell_teaching_map
    if derivation_map:
        out["derivation_map"] = derivation_map
    if working_map:
        out["working_map"] = working_map
    if rubric_map:
        out["rubric_map"] = rubric_map
    if dependency_map:
        out["dependency_map"] = dependency_map
    return out
