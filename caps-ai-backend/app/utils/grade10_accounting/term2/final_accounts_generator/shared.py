from __future__ import annotations

import random
import re
import uuid
from typing import Any, Dict, List, Optional


def _rng(seed: Optional[int]) -> random.Random:
    r = random.Random()
    if seed is None:
        r.seed()
    else:
        r.seed(int(seed))
    return r


def _make_id(prefix: str) -> str:
    return f"{prefix}_{uuid.uuid4().hex[:12]}"


def _round_money(x: float) -> float:
    return round(float(x) + 1e-9, 2)


def _formula_hint_from_working(working_formula: str = "") -> str:
    formula = str(working_formula or "").strip()
    if not formula:
        return ""
    if "=" in formula:
        return formula.split("=")[0].strip()
    return formula


def _make_mcq(*, prompt: str, options: List[str], correct_index: int, explanation: str) -> Dict[str, Any]:
    return {
        "id": _make_id("acct10_fa_mcq"),
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_index": int(correct_index),
        "explanation": explanation,
        "expected_answer_type": "mcq",
        "marks": 2,
        "guidelines": [explanation],
        "visual_aid_key": "final_accounts",
    }


def _build_answer_part_hints(*, sample_answer: str, grading_rubric: Optional[List[str]] = None) -> List[Dict[str, str]]:
    lines = [line.strip() for line in str(sample_answer or "").splitlines() if line.strip()]
    rubric = list(grading_rubric or [])
    return [
        {
            "label": str(rubric[idx] if idx < len(rubric) else f"Memo point {idx + 1}"),
            "value": line,
        }
        for idx, line in enumerate(lines)
    ]


def _make_typed(*, prompt: str, sample_answer: str, grading_rubric: Optional[List[str]] = None) -> Dict[str, Any]:
    answer_part_hints = _build_answer_part_hints(sample_answer=sample_answer, grading_rubric=grading_rubric)
    return {
        "id": _make_id("acct10_fa_typed"),
        "question_type": "typed",
        "prompt": prompt,
        "sample_answer": sample_answer,
        "answer_part_hints": answer_part_hints,
        "expected_answer_type": "text",
        "grading_rubric": grading_rubric or [],
        "marks": 4 if grading_rubric and len(grading_rubric) >= 2 else 2,
        "guidelines": [f"Ensure your answer includes: {', '.join(grading_rubric)}"] if grading_rubric else [],
        "visual_aid_key": "final_accounts",
    }


def _make_calc(*, prompt: str, correct_answer: float, unit: str = "R", working_formula: str = "", formula_hint: str = "") -> Dict[str, Any]:
    resolved_formula_hint = formula_hint or _formula_hint_from_working(working_formula)
    return {
        "id": _make_id("acct10_fa_calc"),
        "question_type": "calc",
        "prompt": prompt,
        "correct_answer": float(correct_answer),
        "unit": unit,
        "working_formula": working_formula,
        "formula_hint": resolved_formula_hint,
        "expected_answer_type": "number",
        "marks": 3,
        "guidelines": [f"Formula: {resolved_formula_hint}"] if resolved_formula_hint else [],
        "visual_aid_key": "final_accounts",
    }


def _make_table_wordbank(
    *,
    prompt: str,
    headers: List[str],
    rows: List[List[str]],
    word_bank: List[Dict[str, str]],
    correct_map: Dict[str, Dict[str, str]],
    guidelines: Optional[List[str]] = None,
) -> Dict[str, Any]:
    return {
        "id": _make_id("acct10_fa_table_wordbank"),
        "question_type": "table_wordbank",
        "prompt": prompt,
        "table": {"headers": headers, "rows": rows},
        "word_bank": word_bank,
        "correct_map": correct_map,
        "guidelines": guidelines or [],
        "expected_answer_type": "table_wordbank",
        "marks": len(rows) * 2,
        "visual_aid_key": "final_accounts",
    }


def _cell(value: Any = "", *, editable: bool = False, cell_id: Optional[str] = None, colSpan: Optional[int] = None, rowSpan: Optional[int] = None) -> Dict[str, Any]:
    payload: Dict[str, Any] = {"value": "" if value is None else value}
    if editable:
        payload["editable"] = True
    if cell_id:
        payload["cell_id"] = str(cell_id)
    if colSpan and int(colSpan) != 1:
        payload["colSpan"] = int(colSpan)
    if rowSpan and int(rowSpan) != 1:
        payload["rowSpan"] = int(rowSpan)
    return payload


def _teaching_hint(
    *,
    role_in_requirement: str = "",
    evidence_from_question: str = "",
    rule_or_principle: str = "",
    method_or_formula: str = "",
    record_link: str = "",
    how_to_derive: str = "",
    transfer_tip: str = "",
) -> Dict[str, str]:
    return {
        "role_in_requirement": str(role_in_requirement or "").strip(),
        "evidence_from_question": str(evidence_from_question or "").strip(),
        "rule_or_principle": str(rule_or_principle or "").strip(),
        "method_or_formula": str(method_or_formula or "").strip(),
        "record_link": str(record_link or "").strip(),
        "how_to_derive": str(how_to_derive or "").strip(),
        "transfer_tip": str(transfer_tip or "").strip(),
    }


def _normalize_label(value: Any) -> str:
    text = str(value or "").strip().lower()
    text = re.sub(r"[^a-z0-9]+", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def _cell_text(cell: Any) -> str:
    if isinstance(cell, dict):
        return str(cell.get("value") or "").strip()
    return str(cell or "").strip()


def _list_tables(single_table: Optional[Dict[str, Any]], many_tables: Optional[List[Dict[str, Any]]]) -> List[Dict[str, Any]]:
    if isinstance(many_tables, list):
        return [table for table in many_tables if isinstance(table, dict)]
    if isinstance(single_table, dict):
        return [single_table]
    return []


def _to_number(value: Any) -> Optional[float]:
    if value is None:
        return None
    if isinstance(value, (int, float)):
        return float(value)
    text = str(value).strip().replace("R", "").replace("r", "").replace(",", "")
    if not text:
        return None
    try:
        return float(text)
    except Exception:
        return None


def _values_match(left: Any, right: Any) -> bool:
    left_number = _to_number(left)
    right_number = _to_number(right)
    if left_number is not None and right_number is not None:
        return abs(_round_money(left_number) - _round_money(right_number)) < 0.01
    return _normalize_label(left) == _normalize_label(right)


def _infer_balance_side(label: str) -> str:
    normalized = _normalize_label(label)
    if not normalized:
        return ""
    credit_tokens = ["capital", "creditors", "loan", "sales", "income", "accumulated depreciation", "accrued expenses", "accrued expense"]
    debit_tokens = ["bank", "stock", "equipment", "vehicle", "vehicles", "fixtures", "debtors", "expense", "drawings", "cost of sales", "depreciation", "prepaid", "accrued income"]
    if any(token in normalized for token in credit_tokens) and "accrued income" not in normalized:
        return "credit"
    if any(token in normalized for token in debit_tokens):
        return "debit"
    return ""


def _collect_prompt_rows(prompt_tables: List[Dict[str, Any]]) -> List[Dict[str, str]]:
    rows: List[Dict[str, str]] = []
    for table in prompt_tables:
        heading = str(table.get("heading") or "Source information").strip()
        for row in table.get("rows") or []:
            values = [_cell_text(cell) for cell in (row or [])]
            values = [value for value in values if value]
            if not values:
                continue
            rows.append({
                "heading": heading,
                "row_label": values[0],
                "row_text": " | ".join(values),
            })
    return rows


def _collect_answer_cell_meta(answer_tables: List[Dict[str, Any]]) -> Dict[str, Dict[str, str]]:
    meta: Dict[str, Dict[str, str]] = {}
    for table_index, table in enumerate(answer_tables):
        heading = str(table.get("heading") or f"Table {table_index + 1}").strip()
        headers = [str(header or "").strip() for header in (table.get("headers") or [])]
        for row_index, row in enumerate(table.get("rows") or []):
            row_values = [_cell_text(cell) for cell in (row or [])]
            row_label = next((value for value in row_values if value), f"Row {row_index + 1}")
            for col_index, cell in enumerate(row or []):
                if not isinstance(cell, dict) or not cell.get("cell_id"):
                    continue
                meta[str(cell["cell_id"])] = {
                    "table_heading": heading,
                    "row_label": str(row_label).strip(),
                    "header_label": headers[col_index] if col_index < len(headers) else f"Column {col_index + 1}",
                }
    return meta


def _find_source_row(row_label: str, prompt_rows: List[Dict[str, str]]) -> Optional[Dict[str, str]]:
    target = _normalize_label(row_label)
    if not target:
        return None
    for row in prompt_rows:
        label = _normalize_label(row.get("row_label"))
        if label == target or (target and label and (target in label or label in target)):
            return row
    for row in prompt_rows:
        label = _normalize_label(row.get("row_label"))
        if any(token and token in label for token in target.split() if len(token) > 3):
            return row
    return None


def _auto_enrich_fill_in_table_guidance(
    *,
    question_type: str,
    table: Optional[Dict[str, Any]],
    tables: Optional[List[Dict[str, Any]]],
    prompt_table: Optional[Dict[str, Any]],
    prompt_tables: Optional[List[Dict[str, Any]]],
    correct_map: Dict[str, Any],
    derivation_map: Optional[Dict[str, Any]],
    cell_hints: Optional[Dict[str, str]],
    cell_teaching_map: Optional[Dict[str, Dict[str, str]]],
    working_map: Optional[Dict[str, str]],
) -> Dict[str, Dict[str, Any]]:
    answer_tables = _list_tables(table, tables)
    source_tables = _list_tables(prompt_table, prompt_tables)
    prompt_rows = _collect_prompt_rows(source_tables)
    answer_meta = _collect_answer_cell_meta(answer_tables)
    next_hints = dict(cell_hints or {})
    next_working = dict(working_map or {})
    next_teaching = {str(cell_id): dict(value or {}) for cell_id, value in (cell_teaching_map or {}).items()}

    for cell_id, expected in correct_map.items():
        meta = answer_meta.get(str(cell_id))
        if not meta:
            continue
        row_label = str(meta.get("row_label") or "").strip()
        header_label = str(meta.get("header_label") or "").strip()
        source_row = _find_source_row(row_label, prompt_rows)
        derivation_text = str((derivation_map or {}).get(str(cell_id)) or "").strip()
        role_text = f"This cell completes {row_label or 'the required row'} in the {header_label or 'required'} column of {meta.get('table_heading') or 'this table'}."
        evidence_text = (
            f"Look in '{source_row['heading']}' at '{source_row['row_text']}'. Use that source and apply any stated year-end adjustment before writing the final answer here."
            if source_row
            else "Use the source list or passage above, then match the relevant account and any year-end adjustment to this cell."
        )
        if str(row_label).strip().lower() in {"total", "totals"}:
            evidence_text = "Use the figures you have already completed in this table. Total cells are worked out from the finished column, not copied directly from a source row."
        rule_text = "Match the figure to the correct accounting record and keep linked amounts consistent across the workflow."
        if question_type == "trial_balance_table":
            side = _infer_balance_side(row_label)
            if side:
                rule_text = f"{row_label} belongs in the {side} column based on the nature of the account."
            else:
                rule_text = "In a trial balance, each account appears once on the correct side only."
        elif question_type == "journal":
            rule_text = "Use the correct double entry: the debit and credit must reflect the same year-end adjustment amount."
        elif question_type == "ledger":
            rule_text = "Ledger postings must agree with the journal entry, and the Details column usually shows the opposite account."
        elif question_type == "adjustment_analysis_table":
            rule_text = "Use the same adjustment amount across the amount, double-entry, and statement-effect columns."
        elif question_type == "final_account_table":
            rule_text = "Carry the adjusted figure to the correct statement section and keep the same figure consistent across linked extracts."
        method_text = derivation_text or (
            "Complete the individual amounts first, then add the column total."
            if str(row_label).strip().lower() in {"total", "totals"}
            else "Trace the figure from the source information, apply any adjustment shown in the question, and then enter the final value here."
        )

        linked_refs: List[str] = []
        for other_cell_id, other_meta in answer_meta.items():
            if other_cell_id == str(cell_id):
                continue
            if _values_match(correct_map.get(other_cell_id), expected):
                ref = f"{other_meta.get('table_heading')} → {other_meta.get('row_label')} ({other_meta.get('header_label')})"
                if ref not in linked_refs:
                    linked_refs.append(ref)
        record_link = ""
        if linked_refs:
            record_link = f"The same figure is also used in {', '.join(linked_refs[:2])}. Keep the amount consistent as you carry it between records."

        teaching_hint = dict(next_teaching.get(str(cell_id)) or {})
        defaults = {
            "role_in_requirement": role_text,
            "evidence_from_question": evidence_text,
            "rule_or_principle": rule_text,
            "method_or_formula": method_text,
            "record_link": record_link,
            "how_to_derive": method_text,
            "transfer_tip": record_link or "Use the same logic again when this balance is carried into a later table or statement extract.",
        }
        for key, value in defaults.items():
            if value and not str(teaching_hint.get(key) or "").strip():
                teaching_hint[key] = value
        next_teaching[str(cell_id)] = teaching_hint

        if not str(next_hints.get(str(cell_id)) or "").strip():
            next_hints[str(cell_id)] = (
                f"Use '{source_row['row_label']}' from '{source_row['heading']}' and apply the correct rule for this cell."
                if source_row
                else rule_text
            )
        if record_link and not str(next_working.get(str(cell_id)) or "").strip():
            next_working[str(cell_id)] = record_link

    return {
        "cell_hints": next_hints,
        "cell_teaching_map": next_teaching,
        "working_map": next_working,
    }


def _make_fill_in_table_question(
    *,
    question_type: str,
    prompt: str,
    correct_map: Dict[str, Any],
    table: Optional[Dict[str, Any]] = None,
    tables: Optional[List[Dict[str, Any]]] = None,
    prompt_table: Optional[Dict[str, Any]] = None,
    prompt_tables: Optional[List[Dict[str, Any]]] = None,
    guidelines: Optional[List[str]] = None,
    marks: Optional[int] = None,
    derivation_map: Optional[Dict[str, Any]] = None,
    cell_hints: Optional[Dict[str, str]] = None,
    cell_teaching_map: Optional[Dict[str, Dict[str, str]]] = None,
    working_map: Optional[Dict[str, str]] = None,
) -> Dict[str, Any]:
    enriched_guidance = _auto_enrich_fill_in_table_guidance(
        question_type=question_type,
        table=table,
        tables=tables,
        prompt_table=prompt_table,
        prompt_tables=prompt_tables,
        correct_map=correct_map,
        derivation_map=derivation_map,
        cell_hints=cell_hints,
        cell_teaching_map=cell_teaching_map,
        working_map=working_map,
    )
    payload: Dict[str, Any] = {
        "id": _make_id(f"acct10_fa_{question_type}"),
        "question_type": question_type,
        "prompt": prompt,
        "correct_map": correct_map,
        "guidelines": guidelines or [],
        "expected_answer_type": "table_cells",
        "marks": int(marks if marks is not None else max(4, len(correct_map))),
        "visual_aid_key": "final_accounts",
    }
    if table is not None:
        payload["table"] = table
    if tables is not None:
        payload["tables"] = tables
    if prompt_table is not None:
        payload["prompt_table"] = prompt_table
    if prompt_tables is not None:
        payload["prompt_tables"] = prompt_tables
    if derivation_map is not None:
        payload["derivation_map"] = derivation_map
    if enriched_guidance.get("cell_hints"):
        payload["cell_hints"] = enriched_guidance["cell_hints"]
    if enriched_guidance.get("cell_teaching_map"):
        payload["cell_teaching_map"] = enriched_guidance["cell_teaching_map"]
    if enriched_guidance.get("working_map"):
        payload["working_map"] = enriched_guidance["working_map"]
    return payload


def _with_validation(question: Dict[str, Any], family: str, **context: Any) -> Dict[str, Any]:
    enriched = dict(question)
    enriched["scenario_validation"] = {"family": family, **context}
    return enriched


def _money_matches(left: float, right: float) -> bool:
    return abs(_round_money(left) - _round_money(right)) < 0.01


def _float_or_zero(value: Any) -> float:
    try:
        return float(value)
    except Exception:
        return 0.0


__all__ = [
    "_rng",
    "_make_id",
    "_round_money",
    "_formula_hint_from_working",
    "_make_mcq",
    "_build_answer_part_hints",
    "_make_typed",
    "_make_calc",
    "_make_table_wordbank",
    "_cell",
    "_teaching_hint",
    "_make_fill_in_table_question",
    "_with_validation",
    "_money_matches",
    "_float_or_zero",
]
