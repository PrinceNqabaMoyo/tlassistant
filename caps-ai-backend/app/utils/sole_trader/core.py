from __future__ import annotations

import random
import uuid
from typing import Any, Dict, List, Optional


def rng(seed: Optional[int]) -> random.Random:
    r = random.Random()
    if seed is None:
        r.seed()
    else:
        r.seed(int(seed))
    return r


def make_id(prefix: str) -> str:
    return f"{prefix}_{uuid.uuid4().hex[:12]}"


def round_money(x: float) -> float:
    return round(float(x) + 1e-9, 2)


def fmt_money(x: Optional[float]) -> str:
    if x is None:
        return ""
    return f"{round_money(x):.2f}"


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


def choose_journal_identity_layout(
    *,
    r: random.Random,
    mode: str,
    difficulty: str,
    identity_cols: List[Optional[int]],
) -> Dict[str, List[int]]:
    cols = sorted({int(c) for c in identity_cols if c is not None})
    if not cols:
        return {"prefilled": [], "editable": []}

    mode_norm = str(mode or "").strip().lower()
    diff = str(difficulty or "easy").strip().lower()

    if mode_norm != "scaffold":
        return {"prefilled": [], "editable": cols}

    if len(cols) == 1:
        if diff in ("medium", "hard"):
            return {"prefilled": [], "editable": cols}
        return {"prefilled": cols, "editable": []}

    prefill_count = 2 if diff == "easy" else 1
    prefill_count = max(0, min(prefill_count, len(cols) - 1))
    prefilled = sorted(r.sample(cols, k=prefill_count)) if prefill_count else []
    editable = [c for c in cols if c not in set(prefilled)]
    return {"prefilled": prefilled, "editable": editable}


def journal_editable_cols_by_difficulty(*, difficulty: str, base_editable_cols: List[int], total_cols: int) -> List[int]:
    """On medium/hard, let learners decide which columns to use by making most cells editable."""
    diff = str(difficulty or "easy").strip().lower()
    if diff in ("medium", "hard"):
        difficulty_cols = set(range(3, int(total_cols)))
        base_cols = {int(c) for c in (base_editable_cols or [])}
        return sorted(difficulty_cols | base_cols)
    return list(base_editable_cols)


def make_mcq(*, prompt: str, options: List[str], correct_index: int, explanation: str) -> Dict[str, Any]:
    return {
        "id": make_id("acct10_st_mcq"),
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_index": int(correct_index),
        "explanation": explanation,
        "expected_answer_type": "mcq",
    }


def make_typed(*, prompt: str, sample_answer: str) -> Dict[str, Any]:
    return {
        "id": make_id("acct10_st_typed"),
        "question_type": "typed",
        "prompt": prompt,
        "sample_answer": sample_answer,
        "expected_answer_type": "text",
    }


def make_calc(*, prompt: str, correct_value: float, unit: str = "", derivation_map: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    out = {
        "id": make_id("acct10_st_calc"),
        "question_type": "calc",
        "prompt": prompt,
        "correct_value": float(correct_value),
        "unit": unit,
        "expected_answer_type": "number",
    }
    if derivation_map:
        out["derivation_map"] = derivation_map
    return out

def make_inline_fill(*, prompt: str, text_parts: List[str], blanks: List[str]) -> Dict[str, Any]:
    answers = {}
    blank_data = []
    for i, ans in enumerate(blanks):
        b_id = f"blank_{i}"
        blank_data.append({"id": b_id})
        answers[b_id] = ans
        
    return {
        "id": make_id("acct10_st_fill"),
        "question_type": "inline_fill",
        "prompt": prompt,
        "text_parts": text_parts,
        "blanks": blank_data,
        "correct_map": answers,
        "expected_answer_type": "inline_fill",
    }


def make_match(*, prompt: str, pairs: List[Dict[str, str]]) -> Dict[str, Any]:
    # pairs should be list of dicts with 'left' and 'right' keys
    # generate stable IDs for grading
    left_items = []
    right_items = []
    matches = {}
    
    for i, pair in enumerate(pairs):
        l_id = f"L_{i}"
        r_id = f"R_{i}"
        left_items.append({"id": l_id, "text": pair["left"]})
        right_items.append({"id": r_id, "text": pair["right"]})
        matches[l_id] = r_id
        
    return {
        "id": make_id("acct10_st_match"),
        "question_type": "match",
        "prompt": prompt,
        "left_items": left_items,
        "right_items": right_items,
        "correct_map": matches,
        "expected_answer_type": "match",
    }


def make_word_bank(*, prompt: str, text_parts: List[str], blanks: List[str], word_bank: List[str]) -> Dict[str, Any]:
    # text_parts: literal text surrounding the blanks. len(text_parts) == len(blanks) + 1
    # blanks: the correct word for each blank in order
    # word_bank: all available words (including distractors)
    
    answers = {}
    blank_data = []
    for i, ans in enumerate(blanks):
        b_id = f"blank_{i}"
        blank_data.append({"id": b_id})
        answers[b_id] = ans
        
    return {
        "id": make_id("acct10_st_wb"),
        "question_type": "word_bank",
        "prompt": prompt,
        "text_parts": text_parts,
        "blanks": blank_data,
        "word_bank": word_bank,
        "correct_map": answers,
        "expected_answer_type": "word_bank",
    }


def make_journal(
    *,
    prompt: str,
    journal_type: str,
    headers: List[str],
    rows: List[List[Dict[str, Any]]],
    correct_map: Dict[str, Any],
    guidelines: Optional[List[str]] = None,
    table_variant: str = "grade_project",
    column_help: Optional[Dict[str, str]] = None,
    cell_hints: Optional[Dict[str, Any]] = None,
    cell_teaching_map: Optional[Dict[str, Dict[str, str]]] = None,
    header_rows: Optional[List[List[Dict[str, Any]]]] = None,
    title_fields: Optional[List[Dict[str, Any]]] = None,
    id_prefix: str = "acct10_st_journal",
) -> Dict[str, Any]:
    journal: Dict[str, Any] = {
        "journal_type": journal_type,
        "table_variant": table_variant,
        "headers": headers,
        "rows": rows,
        "column_help": column_help or {},
    }
    if cell_hints:
        journal["cell_hints"] = cell_hints
    if cell_teaching_map:
        journal["cell_teaching_map"] = cell_teaching_map
    if header_rows:
        journal["header_rows"] = header_rows
    if title_fields:
        journal["title_fields"] = title_fields

    out = {
        "id": make_id(id_prefix),
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
    return out


def calc_cost_price_from_selling_price_and_margin(*, sp: float, profit_margin_pct: float) -> float:
    return round_money(sp / (1.0 + (profit_margin_pct / 100.0)))


def calc_selling_price_from_cost_price_and_margin(*, cp: float, profit_margin_pct: float) -> float:
    return round_money(cp * (1.0 + (profit_margin_pct / 100.0)))
