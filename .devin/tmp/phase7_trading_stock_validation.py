from __future__ import annotations

import json
import pathlib
import random
import re
import sys
import traceback
from typing import Any, Dict, List, Tuple


ROOT = pathlib.Path(__file__).resolve().parents[2]
BACKEND_ROOT = ROOT / "caps-ai-backend"
REPORT_PATH = ROOT / ".windsurf" / "tmp" / "phase7_trading_stock_validation_report.json"
TOKEN_RE = re.compile(r"^\([a-z]+\)$", re.IGNORECASE)

if str(BACKEND_ROOT) not in sys.path:
    sys.path.insert(0, str(BACKEND_ROOT))

from app.utils.grade10_accounting import sole_trader_generator as generator  # noqa: E402
from app.utils.sole_trader import trading_stock_account as trading_stock  # noqa: E402


EXPECTED_VARIANTS = {
    "easy": {"prepare_from_journals", "fill_missing_details"},
    "medium": {
        "prepare_from_journals",
        "fill_missing_details",
        "casted_journals",
        "returns_percent",
        "discount_calc",
        "section3_typed",
    },
    "hard": {
        "prepare_from_journals",
        "fill_missing_details",
        "casted_journals",
        "returns_percent",
        "discount_calc",
        "section3_typed",
        "two_returns_percent",
        "markup_trade_discount_typed",
        "activity16_typed",
    },
}
EXPECTED_EDITABLE_COLUMNS = {
    "easy": [4, 9],
    "medium": [2, 4, 7, 9],
    "hard": [1, 2, 3, 4, 6, 7, 8, 9],
}
SEEDS = [11, 23, 37, 51, 71]
MODES = ["practice", "scaffold"]


def round_money(value: float) -> float:
    return round(float(value) + 1e-9, 2)


def parse_amount(value: Any) -> float:
    text = str(value or "").strip()
    if not text:
        return 0.0
    return round_money(float(text))


def classify_question(question: Dict[str, Any]) -> str:
    prompt = str(question.get("prompt") or "").lower()
    if "fill in the missing details" in prompt:
        return "fill_missing_details"
    if "calculate % returns to creditors on credit purchases" in prompt and "calculate % returns from debtors on total cost of sales" in prompt:
        return "two_returns_percent"
    if "calculate the returns percentage if returns to creditors amounted to" in prompt:
        return "returns_percent"
    if "cash purchases were paid for after a trade discount" in prompt:
        return "discount_calc"
    if "information: journal totals (casting)" in prompt and "additional information: opening trading stock balance" in prompt:
        return "casted_journals"
    if "the following totals were extracted from the journals" in prompt:
        return "prepare_from_journals"
    if "activity 16 (analysis - trading stock account)" in prompt:
        return "activity16_typed"
    if "trading stock account (section 3)" in prompt:
        return "section3_typed"
    if "trading stock calculations" in prompt:
        return "markup_trade_discount_typed"
    return "unknown"


def question_rows_with_answers(question: Dict[str, Any]) -> List[List[str]]:
    journal = question["journal"]
    rows = journal["rows"]
    correct_map = question["correct_map"]
    out: List[List[str]] = []
    for rix, row in enumerate(rows):
        out_row: List[str] = []
        for cix, cell in enumerate(row):
            key = f"t0_r{rix}_c{cix}"
            out_row.append(str(correct_map.get(key, cell.get("label", "")) or ""))
        out.append(out_row)
    return out


def tested_cells(question: Dict[str, Any]) -> List[Tuple[str, str, str, int]]:
    rows = question["journal"]["rows"]
    correct_map = question["correct_map"]
    out: List[Tuple[str, str, str, int]] = []
    for rix, row in enumerate(rows):
        for cix, cell in enumerate(row):
            key = f"t0_r{rix}_c{cix}"
            shown = str(cell.get("label", "") or "")
            expected = str(correct_map.get(key, shown) or "")
            if expected and shown != expected and (shown == "" or TOKEN_RE.match(shown)):
                out.append((key, shown, expected, cix))
    return out


def validate_rendered_account(question: Dict[str, Any]) -> Dict[str, Any]:
    rows = question_rows_with_answers(question)
    totals_index = next(i for i, row in enumerate(rows) if row[2] == "Totals" or row[7] == "Totals")
    pre_total_rows = rows[:totals_index]
    post_total_rows = rows[totals_index + 1 :]

    debit_total = round_money(sum(parse_amount(row[4]) for row in pre_total_rows))
    credit_total = round_money(sum(parse_amount(row[9]) for row in pre_total_rows))
    rendered_debit_total = parse_amount(rows[totals_index][4])
    rendered_credit_total = parse_amount(rows[totals_index][9])
    if rendered_debit_total != rendered_credit_total:
        raise AssertionError("Rendered total row is not balanced.")
    if rendered_debit_total != debit_total or rendered_credit_total != credit_total:
        raise AssertionError("Rendered total row does not equal recomputed totals.")

    balance_cd_rows = [row for row in pre_total_rows if row[2] == "Balance c/d" or row[7] == "Balance c/d"]
    balance_bd_rows = [row for row in post_total_rows if row[2] == "Balance b/d" or row[7] == "Balance b/d"]
    if len(balance_cd_rows) != 1 or len(balance_bd_rows) != 1:
        raise AssertionError("Trading Stock account must have exactly one Balance c/d row and one Balance b/d row.")

    balance_cd_row = balance_cd_rows[0]
    balance_bd_row = balance_bd_rows[0]
    balance_cd_on_credit = balance_cd_row[7] == "Balance c/d"
    balance_bd_on_debit = balance_bd_row[2] == "Balance b/d"
    balance_cd_amount = parse_amount(balance_cd_row[9] if balance_cd_on_credit else balance_cd_row[4])
    balance_bd_amount = parse_amount(balance_bd_row[4] if balance_bd_on_debit else balance_bd_row[9])

    raw_debit = round_money(sum(parse_amount(row[4]) for row in pre_total_rows if row is not balance_cd_row))
    raw_credit = round_money(sum(parse_amount(row[9]) for row in pre_total_rows if row is not balance_cd_row))
    expected_difference = round_money(abs(raw_debit - raw_credit))
    if balance_cd_amount != expected_difference:
        raise AssertionError("Balance c/d amount does not equal the difference between the two sides.")
    if raw_debit > raw_credit and not balance_cd_on_credit:
        raise AssertionError("Closing balance is on the wrong side for a debit-heavy account.")
    if raw_credit > raw_debit and balance_cd_on_credit:
        raise AssertionError("Closing balance is on the wrong side for a credit-heavy account.")
    if raw_debit == raw_credit:
        raise AssertionError("Expected a non-zero closing balance for Trading Stock account validation.")
    if balance_bd_amount != balance_cd_amount:
        raise AssertionError("Balance b/d does not match Balance c/d.")
    if balance_cd_on_credit != balance_bd_on_debit:
        raise AssertionError("Balance b/d is not carried down on the opposite side to Balance c/d.")

    rows_raw = question["journal"]["rows"]
    correct_map = question["correct_map"]
    for rix, row in enumerate(rows_raw):
        for cix, cell in enumerate(row):
            key = f"t0_r{rix}_c{cix}"
            shown = str(cell.get("label", "") or "")
            expected = str(correct_map.get(key, shown) or "")
            if shown and not TOKEN_RE.match(shown) and shown != expected:
                raise AssertionError(f"Visible cell {key} does not match correct_map.")

    return {
        "debit_total": debit_total,
        "credit_total": credit_total,
        "balance_cd_side": "credit" if balance_cd_on_credit else "debit",
        "balance_cd_amount": balance_cd_amount,
    }


def validate_scaffold(question: Dict[str, Any]) -> Dict[str, Any]:
    cell_hints = question.get("cell_hints")
    cell_teaching_map = question.get("cell_teaching_map")
    derivation_map = question.get("derivation_map")
    if not isinstance(cell_hints, dict) or not cell_hints:
        raise AssertionError("Scaffold output is missing cell_hints.")
    if not isinstance(cell_teaching_map, dict) or not cell_teaching_map:
        raise AssertionError("Scaffold output is missing cell_teaching_map.")
    if not isinstance(derivation_map, dict) or not derivation_map:
        raise AssertionError("Scaffold output is missing derivation_map.")

    tested = tested_cells(question)
    if not tested:
        raise AssertionError("Expected at least one tested cell in scaffold mode.")

    for key, _shown, _expected, column_index in tested:
        if not str(cell_hints.get(key) or "").strip():
            raise AssertionError(f"Tested cell {key} is missing a scaffold hint.")
        teaching = cell_teaching_map.get(key) or {}
        if not isinstance(teaching, dict) or not str(teaching.get("how_to_derive") or "").strip():
            raise AssertionError(f"Tested cell {key} is missing teaching metadata.")
        if column_index in {4, 9} and not str(derivation_map.get(key) or "").strip():
            raise AssertionError(f"Amount cell {key} is missing derivation guidance.")

    return {
        "tested_cell_count": len(tested),
        "hinted_tested_cell_count": len(tested),
    }


def validate_prepare_progression() -> Dict[str, Any]:
    progression: Dict[str, Any] = {}
    for difficulty, expected_columns in EXPECTED_EDITABLE_COLUMNS.items():
        question = trading_stock.make_trading_stock_prepare_from_journals_question(
            r=random.Random(101), difficulty=difficulty, mode="practice"
        )
        columns = sorted({column_index for _key, _shown, _expected, column_index in tested_cells(question)})
        if columns != expected_columns:
            raise AssertionError(
                f"Prepare-from-journals blank columns for {difficulty} were {columns}, expected {expected_columns}."
            )
        progression[difficulty] = {
            "blank_columns": columns,
            "tested_cell_count": len(tested_cells(question)),
        }
    return progression


def validate_variant_mix() -> Dict[str, Any]:
    summary: Dict[str, Any] = {}
    for difficulty, expected_variants in EXPECTED_VARIANTS.items():
        questions = generator._generate_questions_internal(
            r=random.Random(211),
            n=len(expected_variants),
            subskill="trading stock account",
            difficulty=difficulty,
            mode="practice",
            variant="",
        )
        actual_variants = {classify_question(question) for question in questions}
        if actual_variants != expected_variants:
            raise AssertionError(
                f"Variant mix for {difficulty} was {sorted(actual_variants)}, expected {sorted(expected_variants)}."
            )
        summary[difficulty] = {
            "pool_size": len(questions),
            "variants": sorted(actual_variants),
        }
    return summary


def main() -> int:
    failures: List[Dict[str, Any]] = []
    coverage: List[Dict[str, Any]] = []

    try:
        progression = validate_prepare_progression()
    except Exception as exc:
        failures.append({
            "phase": "difficulty_progression",
            "error": str(exc),
            "traceback": traceback.format_exc(),
        })
        progression = {}

    try:
        variant_mix = validate_variant_mix()
    except Exception as exc:
        failures.append({
            "phase": "variant_mix",
            "error": str(exc),
            "traceback": traceback.format_exc(),
        })
        variant_mix = {}

    for difficulty, expected_variants in EXPECTED_VARIANTS.items():
        for mode in MODES:
            for seed in SEEDS:
                try:
                    questions = generator._generate_questions_internal(
                        r=random.Random(seed),
                        n=len(expected_variants),
                        subskill="trading stock account",
                        difficulty=difficulty,
                        mode=mode,
                        variant="",
                    )
                    if len(questions) != len(expected_variants):
                        raise AssertionError(
                            f"Expected {len(expected_variants)} questions for {difficulty}/{mode}, got {len(questions)}."
                        )
                    actual_variants = {classify_question(question) for question in questions}
                    if actual_variants != expected_variants:
                        raise AssertionError(
                            f"Variant set mismatch for {difficulty}/{mode}/seed {seed}: {sorted(actual_variants)}"
                        )

                    journal_count = 0
                    scaffold_count = 0
                    for question in questions:
                        if str(question.get("question_type") or "") != "journal":
                            continue
                        journal_count += 1
                        balance_info = validate_rendered_account(question)
                        scaffold_info: Dict[str, Any] = {}
                        if mode == "scaffold":
                            scaffold_info = validate_scaffold(question)
                            scaffold_count += 1
                        coverage.append({
                            "difficulty": difficulty,
                            "mode": mode,
                            "seed": seed,
                            "variant": classify_question(question),
                            "question_type": question.get("question_type"),
                            "balance": balance_info,
                            "scaffold": scaffold_info,
                        })

                    if mode == "scaffold" and scaffold_count != journal_count:
                        raise AssertionError(
                            f"Expected scaffold metadata for all journal questions in {difficulty}/{mode}/seed {seed}."
                        )
                except Exception as exc:
                    failures.append({
                        "difficulty": difficulty,
                        "mode": mode,
                        "seed": seed,
                        "error": str(exc),
                        "traceback": traceback.format_exc(),
                    })

    report = {
        "status": "passed" if not failures else "failed",
        "checked_seeds": SEEDS,
        "checked_modes": MODES,
        "difficulty_progression": progression,
        "variant_mix": variant_mix,
        "coverage_entries": len(coverage),
        "failures": failures,
    }
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text(json.dumps(report, indent=2), encoding="utf-8")
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
