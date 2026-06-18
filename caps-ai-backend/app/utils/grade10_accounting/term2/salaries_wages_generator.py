from __future__ import annotations

import random
import uuid
from typing import Any, Dict, List, Optional

from ...sole_trader.journal_question import make_journal as _make_journal
from ...sole_trader.journal_table import build_prefixed_row as _build_prefixed_row
from ...sole_trader.names import pick_business_name as _pick_business_name
from ...sole_trader.names import pick_person_names as _pick_person_names
from ..sole_trader_ledger_helpers import general_ledger_account_headers as _general_ledger_account_headers


class _SalariesWagesScenarioValidationError(ValueError):
    pass


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


# ---------------------------------------------------------------------------
# Question factories
# ---------------------------------------------------------------------------

def _make_mcq(*, prompt: str, options: List[str], correct_index: int, explanation: str) -> Dict[str, Any]:
    return {
        "id": _make_id("acct10_sw_mcq"),
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_index": int(correct_index),
        "explanation": explanation,
        "expected_answer_type": "mcq",
        "marks": 2,
        "guidelines": [explanation],
        "visual_aid_key": "salaries_wages",
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
        "id": _make_id("acct10_sw_typed"),
        "question_type": "typed",
        "prompt": prompt,
        "sample_answer": sample_answer,
        "answer_part_hints": answer_part_hints,
        "expected_answer_type": "text",
        "grading_rubric": grading_rubric or [],
        "marks": 4 if grading_rubric and len(grading_rubric) >= 2 else 2,
        "guidelines": [f"Ensure your answer includes: {', '.join(grading_rubric)}"] if grading_rubric else [],
        "visual_aid_key": "salaries_wages",
    }


def _make_calc(*, prompt: str, correct_answer: float, unit: str = "R", working_formula: str = "") -> Dict[str, Any]:
    return {
        "id": _make_id("acct10_sw_calc"),
        "question_type": "calc",
        "prompt": prompt,
        "correct_answer": float(correct_answer),
        "unit": unit,
        "working_formula": working_formula,
        "expected_answer_type": "number",
        "marks": 3,
        "guidelines": [f"Formula: {working_formula}"] if working_formula else [],
        "visual_aid_key": "salaries_wages",
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
        "id": _make_id("acct10_sw_table_wordbank"),
        "question_type": "table_wordbank",
        "prompt": prompt,
        "table": {"headers": headers, "rows": rows},
        "word_bank": word_bank,
        "correct_map": correct_map,
        "guidelines": guidelines or [],
        "expected_answer_type": "table_wordbank",
        "marks": len(rows) * 2,
        "visual_aid_key": "salaries_wages",
    }


def _with_validation(question: Dict[str, Any], family: str, **context: Any) -> Dict[str, Any]:
    enriched = dict(question)
    enriched["scenario_validation"] = {"family": family, **context}
    return enriched


def _set_recommended_difficulties(question: Dict[str, Any], *levels: str) -> Dict[str, Any]:
    enriched = dict(question)
    normalized = [str(level or "").strip().lower() for level in levels if str(level or "").strip()]
    enriched["recommended_difficulties"] = normalized or ["easy", "medium", "hard"]
    return enriched


def _difficulty_matches(question: Dict[str, Any], difficulty: str) -> bool:
    allowed = question.get("recommended_difficulties")
    if not isinstance(allowed, list) or not allowed:
        return True
    difficulty_norm = str(difficulty or "easy").strip().lower()
    return difficulty_norm in [str(level or "").strip().lower() for level in allowed]


def _money_matches(left: float, right: float) -> bool:
    return abs(_round_money(left) - _round_money(right)) < 0.01


def _fmt_money(x: float) -> str:
    return f"{_round_money(x):,.2f}"


def _readonly_table(
    *,
    table_index: int,
    heading: str,
    headers: List[str],
    row_values: List[List[Optional[str]]],
    journal_type: str,
) -> Dict[str, Any]:
    rows = [
        _build_prefixed_row(table_index=table_index, row_index=row_index, values=values, editable_cols=[])
        for row_index, values in enumerate(row_values)
    ]
    return {
        "journal_type": journal_type,
        "table_variant": "grade_project",
        "heading": heading,
        "headers": headers,
        "rows": rows,
        "column_help": {},
        "allow_extra_rows": False,
    }


def _build_table_rows(
    *,
    table_index: int,
    row_values: List[List[Optional[str]]],
    editable_cols_by_row: List[List[int]],
    cell_hint_builder: Optional[Any] = None,
    derivation_builder: Optional[Any] = None,
) -> Any:
    rows: List[List[Dict[str, Any]]] = []
    correct_map: Dict[str, Any] = {}
    cell_hints: Dict[str, str] = {}
    derivation_map: Dict[str, str] = {}

    for row_index, values in enumerate(row_values):
        editable_cols = list(editable_cols_by_row[row_index] if row_index < len(editable_cols_by_row) else [])
        display_values = ["" if col_index in editable_cols else value for col_index, value in enumerate(values)]
        rows.append(_build_prefixed_row(table_index=table_index, row_index=row_index, values=display_values, editable_cols=editable_cols))
        for col_index in editable_cols:
            key = f"t{table_index}_r{row_index}_c{col_index}"
            expected = "" if values[col_index] is None else str(values[col_index])
            correct_map[key] = expected
            if cell_hint_builder is not None:
                hint_text = str(cell_hint_builder(row_index, col_index, expected) or "").strip()
                if hint_text:
                    cell_hints[key] = hint_text
            if derivation_builder is not None:
                derivation_text = str(derivation_builder(row_index, col_index, expected) or "").strip()
                if derivation_text:
                    derivation_map[key] = derivation_text

    return rows, correct_map, cell_hints, derivation_map


# ---------------------------------------------------------------------------
# Scenario / name pools
# ---------------------------------------------------------------------------

def _pick_business(r: random.Random) -> str:
    return _pick_business_name(r=r)


def _pick_employee(r: random.Random) -> str:
    picks = _pick_person_names(r=r, k=1)
    return picks[0] if picks else "Alex Smith"


def _pick_employees(r: random.Random, n: int = 3) -> List[str]:
    return _pick_person_names(r=r, k=max(1, int(n)))


def _make_salary_journal_fill_question(*, r: random.Random, difficulty: str) -> Dict[str, Any]:
    business = _pick_business_name(r=r)
    employees = _pick_person_names(r=r, k=2)
    month = r.choice(["January", "February", "March", "April", "May", "June"])
    pension_pct = float(r.choice([7.5, 8.0]))
    uif_pct = 1.0

    entries: List[Dict[str, Any]] = []
    for employee in employees:
        basic_salary = float(r.choice([12000, 14500, 16800, 18400, 21000]))
        commission = float(r.choice([0, 1200, 2500, 4200]))
        bonus = float(r.choice([0, 800, 1500, 2200]))
        paye = float(r.choice([1200, 1650, 2100, 2850, 3400]))
        medical = float(r.choice([250, 450, 700, 980]))
        gross_salary = _round_money(basic_salary + commission + bonus)
        pension = _round_money(basic_salary * pension_pct / 100)
        uif = _round_money(basic_salary * uif_pct / 100)
        net_salary = _round_money(gross_salary - paye - pension - medical - uif)
        entries.append({
            "employee": employee,
            "basic_salary": basic_salary,
            "commission": commission,
            "bonus": bonus,
            "gross_salary": gross_salary,
            "paye": paye,
            "pension": pension,
            "medical": medical,
            "uif": uif,
            "net_salary": net_salary,
        })

    source_headers = ["Employee", "Basic salary", "Commission", "Bonus", "PAYE", "Medical aid"]
    source_rows = [
        [
            entry["employee"],
            _fmt_money(entry["basic_salary"]),
            _fmt_money(entry["commission"]),
            _fmt_money(entry["bonus"]),
            _fmt_money(entry["paye"]),
            _fmt_money(entry["medical"]),
        ]
        for entry in entries
    ]
    prompt_journal = _readonly_table(
        table_index=90,
        heading="Payroll information",
        headers=source_headers,
        row_values=source_rows,
        journal_type="salary_journal_source",
    )

    headers = [
        "Employee",
        "Basic salary",
        "Commission",
        "Bonus",
        "Gross salary",
        "PAYE",
        "Pension",
        "Medical aid",
        "UIF",
        "Net salary",
    ]
    total_row = [
        "TOTAL",
        _fmt_money(sum(entry["basic_salary"] for entry in entries)),
        _fmt_money(sum(entry["commission"] for entry in entries)),
        _fmt_money(sum(entry["bonus"] for entry in entries)),
        _fmt_money(sum(entry["gross_salary"] for entry in entries)),
        _fmt_money(sum(entry["paye"] for entry in entries)),
        _fmt_money(sum(entry["pension"] for entry in entries)),
        _fmt_money(sum(entry["medical"] for entry in entries)),
        _fmt_money(sum(entry["uif"] for entry in entries)),
        _fmt_money(sum(entry["net_salary"] for entry in entries)),
    ]
    row_values = [
        [
            entry["employee"],
            _fmt_money(entry["basic_salary"]),
            _fmt_money(entry["commission"]),
            _fmt_money(entry["bonus"]),
            _fmt_money(entry["gross_salary"]),
            _fmt_money(entry["paye"]),
            _fmt_money(entry["pension"]),
            _fmt_money(entry["medical"]),
            _fmt_money(entry["uif"]),
            _fmt_money(entry["net_salary"]),
        ]
        for entry in entries
    ] + [total_row]

    difficulty_norm = str(difficulty or "easy").strip().lower()
    if difficulty_norm == "easy":
        editable_cols = [4, 6, 8, 9]
    elif difficulty_norm == "medium":
        editable_cols = [2, 3, 4, 6, 8, 9]
    else:
        editable_cols = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    editable_cols_by_row = [editable_cols[:] for _ in row_values]

    def _cell_hint_builder(row_index: int, col_index: int, expected: str) -> str:
        if row_index == len(row_values) - 1:
            return "Add this column vertically to complete the totals row."
        if col_index == 4:
            return "Gross salary = basic salary + commission + bonus."
        if col_index == 6:
            return f"Pension deduction = {pension_pct}% of the employee's basic salary."
        if col_index == 8:
            return "UIF deduction = 1% of the employee's basic salary."
        if col_index == 9:
            return "Net salary = gross salary - PAYE - pension - medical aid - UIF."
        return "Copy the payroll amount into the matching Salary Journal column."

    def _derivation_builder(row_index: int, col_index: int, expected: str) -> str:
        if row_index == len(row_values) - 1:
            return f"Total this column to get R{expected}."
        entry = entries[row_index]
        if col_index == 4:
            return f"Gross salary = R{_fmt_money(entry['basic_salary'])} + R{_fmt_money(entry['commission'])} + R{_fmt_money(entry['bonus'])} = R{expected}."
        if col_index == 6:
            return f"Pension = {pension_pct}% × R{_fmt_money(entry['basic_salary'])} = R{expected}."
        if col_index == 8:
            return f"UIF = 1% × R{_fmt_money(entry['basic_salary'])} = R{expected}."
        if col_index == 9:
            return f"Net salary = R{_fmt_money(entry['gross_salary'])} - R{_fmt_money(entry['paye'])} - R{_fmt_money(entry['pension'])} - R{_fmt_money(entry['medical'])} - R{_fmt_money(entry['uif'])} = R{expected}."
        return f"Copy the payroll amount R{expected} into this column."

    rows, correct_map, cell_hints, derivation_map = _build_table_rows(
        table_index=0,
        row_values=row_values,
        editable_cols_by_row=editable_cols_by_row,
        cell_hint_builder=_cell_hint_builder,
        derivation_builder=_derivation_builder,
    )

    question = _make_journal(
        prompt=(
            f"{business}\n"
            f"Salary Journal for {month}\n\n"
            "Use the payroll information table to complete the Salary Journal.\n"
            f"- Pension deduction = {pension_pct}% of basic salary.\n"
            "- UIF deduction = 1% of basic salary.\n"
            "Required: complete the missing cells, including the totals row."
        ),
        journal_type="salary_journal",
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        guidelines=[
            "Copy the given payroll amounts into the correct Salary Journal columns.",
            "Calculate gross salary before deductions and net salary after deductions.",
            "Complete the totals row by adding each amount column vertically.",
        ],
        cell_hints=cell_hints,
        derivation_map=derivation_map,
    )
    question["journal"]["heading"] = "Salary Journal"
    question["prompt_journal"] = prompt_journal
    question["marks"] = max(4, len(correct_map))
    question["visual_aid_key"] = "salaries_wages"
    question = _with_validation(question, f"salary_journal_fill_in_{difficulty_norm}", expected_cells=len(correct_map))
    return _set_recommended_difficulties(question, difficulty_norm)


def _make_wage_journal_fill_question(*, r: random.Random, difficulty: str) -> Dict[str, Any]:
    business = _pick_business_name(r=r)
    employees = _pick_person_names(r=r, k=2)
    month = r.choice(["January", "February", "March", "April", "May", "June"])
    pension_pct = 8.0

    entries: List[Dict[str, Any]] = []
    for employee in employees:
        ordinary_hours = int(r.choice([35, 40, 45]))
        hourly_rate = float(r.choice([24, 28, 32, 36, 42]))
        overtime_hours = int(r.choice([2, 4, 6, 8]))
        overtime_rate = _round_money(hourly_rate * r.choice([1.5, 2.0]))
        medical = float(r.choice([0, 120, 240, 360]))
        basic_wage = _round_money(ordinary_hours * hourly_rate)
        overtime = _round_money(overtime_hours * overtime_rate)
        gross_wage = _round_money(basic_wage + overtime)
        paye = _round_money(gross_wage * float(r.choice([0.18, 0.20, 0.22])))
        pension = _round_money(basic_wage * pension_pct / 100)
        uif = _round_money(gross_wage * 0.01)
        net_wage = _round_money(gross_wage - paye - pension - medical - uif)
        entries.append({
            "employee": employee,
            "ordinary_hours": ordinary_hours,
            "hourly_rate": hourly_rate,
            "overtime_hours": overtime_hours,
            "overtime_rate": overtime_rate,
            "basic_wage": basic_wage,
            "overtime": overtime,
            "gross_wage": gross_wage,
            "paye": paye,
            "pension": pension,
            "medical": medical,
            "uif": uif,
            "net_wage": net_wage,
        })

    source_headers = ["Worker", "Ordinary hours", "Hourly rate", "Overtime hours", "Overtime rate", "Medical aid"]
    source_rows = [
        [
            entry["employee"],
            str(entry["ordinary_hours"]),
            _fmt_money(entry["hourly_rate"]),
            str(entry["overtime_hours"]),
            _fmt_money(entry["overtime_rate"]),
            _fmt_money(entry["medical"]),
        ]
        for entry in entries
    ]
    prompt_journal = _readonly_table(
        table_index=91,
        heading="Time and wage data",
        headers=source_headers,
        row_values=source_rows,
        journal_type="wage_journal_source",
    )

    headers = [
        "Worker",
        "Basic wage",
        "Overtime",
        "Gross wage",
        "PAYE",
        "Pension",
        "Medical aid",
        "UIF",
        "Net wage",
    ]
    total_row = [
        "TOTAL",
        _fmt_money(sum(entry["basic_wage"] for entry in entries)),
        _fmt_money(sum(entry["overtime"] for entry in entries)),
        _fmt_money(sum(entry["gross_wage"] for entry in entries)),
        _fmt_money(sum(entry["paye"] for entry in entries)),
        _fmt_money(sum(entry["pension"] for entry in entries)),
        _fmt_money(sum(entry["medical"] for entry in entries)),
        _fmt_money(sum(entry["uif"] for entry in entries)),
        _fmt_money(sum(entry["net_wage"] for entry in entries)),
    ]
    row_values = [
        [
            entry["employee"],
            _fmt_money(entry["basic_wage"]),
            _fmt_money(entry["overtime"]),
            _fmt_money(entry["gross_wage"]),
            _fmt_money(entry["paye"]),
            _fmt_money(entry["pension"]),
            _fmt_money(entry["medical"]),
            _fmt_money(entry["uif"]),
            _fmt_money(entry["net_wage"]),
        ]
        for entry in entries
    ] + [total_row]

    difficulty_norm = str(difficulty or "easy").strip().lower()
    if difficulty_norm == "easy":
        editable_cols = [1, 2, 3, 7, 8]
    elif difficulty_norm == "medium":
        editable_cols = [1, 2, 3, 5, 7, 8]
    else:
        editable_cols = [1, 2, 3, 4, 5, 6, 7, 8]
    editable_cols_by_row = [editable_cols[:] for _ in row_values]

    def _cell_hint_builder(row_index: int, col_index: int, expected: str) -> str:
        if row_index == len(row_values) - 1:
            return "Add this column vertically to complete the totals row."
        if col_index == 1:
            return "Basic wage = ordinary hours × hourly rate."
        if col_index == 2:
            return "Overtime = overtime hours × overtime rate."
        if col_index == 3:
            return "Gross wage = basic wage + overtime."
        if col_index == 5:
            return f"Pension deduction = {pension_pct:.0f}% of basic wage."
        if col_index == 7:
            return "UIF deduction = 1% of gross wage."
        if col_index == 8:
            return "Net wage = gross wage - PAYE - pension - medical aid - UIF."
        return "Copy the given wage amount into the matching Wages Journal column."

    def _derivation_builder(row_index: int, col_index: int, expected: str) -> str:
        if row_index == len(row_values) - 1:
            return f"Total this column to get R{expected}."
        entry = entries[row_index]
        if col_index == 1:
            return f"Basic wage = {entry['ordinary_hours']} × R{_fmt_money(entry['hourly_rate'])} = R{expected}."
        if col_index == 2:
            return f"Overtime = {entry['overtime_hours']} × R{_fmt_money(entry['overtime_rate'])} = R{expected}."
        if col_index == 3:
            return f"Gross wage = R{_fmt_money(entry['basic_wage'])} + R{_fmt_money(entry['overtime'])} = R{expected}."
        if col_index == 5:
            return f"Pension = {pension_pct:.0f}% × R{_fmt_money(entry['basic_wage'])} = R{expected}."
        if col_index == 7:
            return f"UIF = 1% × R{_fmt_money(entry['gross_wage'])} = R{expected}."
        if col_index == 8:
            return f"Net wage = R{_fmt_money(entry['gross_wage'])} - R{_fmt_money(entry['paye'])} - R{_fmt_money(entry['pension'])} - R{_fmt_money(entry['medical'])} - R{_fmt_money(entry['uif'])} = R{expected}."
        return f"Copy the wage amount R{expected} into this column."

    rows, correct_map, cell_hints, derivation_map = _build_table_rows(
        table_index=0,
        row_values=row_values,
        editable_cols_by_row=editable_cols_by_row,
        cell_hint_builder=_cell_hint_builder,
        derivation_builder=_derivation_builder,
    )

    question = _make_journal(
        prompt=(
            f"{business}\n"
            f"Wages Journal for {month}\n\n"
            "Use the time and wage data table to complete the Wages Journal.\n"
            f"- Pension deduction = {pension_pct:.0f}% of basic wage.\n"
            "- UIF deduction = 1% of gross wage.\n"
            "Required: complete the missing cells, including the totals row."
        ),
        journal_type="wage_journal",
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        guidelines=[
            "Calculate basic wage and overtime first, then determine gross wage.",
            "Apply the deductions to arrive at the net wage.",
            "Complete the totals row by adding each amount column vertically.",
        ],
        cell_hints=cell_hints,
        derivation_map=derivation_map,
    )
    question["journal"]["heading"] = "Wages Journal"
    question["prompt_journal"] = prompt_journal
    question["marks"] = max(4, len(correct_map))
    question["visual_aid_key"] = "salaries_wages"
    question = _with_validation(question, f"wage_journal_fill_in_{difficulty_norm}", expected_cells=len(correct_map))
    return _set_recommended_difficulties(question, difficulty_norm)


def _make_general_ledger_fill_question(*, r: random.Random, difficulty: str) -> Dict[str, Any]:
    business = _pick_business_name(r=r)
    month = r.choice(["January", "February", "March", "April", "May", "June"])
    month_short = str(month)[:3]
    next_month_short = {"Jan": "Feb", "Feb": "Mar", "Mar": "Apr", "Apr": "May", "May": "Jun", "Jun": "Jul"}.get(month_short, month_short)
    employee = _pick_person_names(r=r, k=1)[0]

    gross_salary = float(r.choice([16800, 18400, 21250, 23800]))
    paye = float(r.choice([1850, 2200, 2650, 3120]))
    pension = float(r.choice([960, 1200, 1450, 1680]))
    medical = float(r.choice([300, 480, 620, 780]))
    uif = _round_money(gross_salary * 0.01)
    net_salary = _round_money(gross_salary - paye - pension - medical - uif)
    cpj_payment = net_salary
    opening_balance = float(r.choice([0, 1800, 2400]))

    prompt_journals = [
        _readonly_table(
            table_index=92,
            heading="Salary Journal totals",
            headers=["Gross salaries", "PAYE", "Pension", "Medical aid", "UIF", "Net salaries"],
            row_values=[[_fmt_money(gross_salary), _fmt_money(paye), _fmt_money(pension), _fmt_money(medical), _fmt_money(uif), _fmt_money(net_salary)]],
            journal_type="salary_journal_totals",
        ),
        _readonly_table(
            table_index=93,
            heading="Cash Payments Journal settlement",
            headers=["Day", "Details", "Bank", "Creditors for salaries"],
            row_values=[["30", f"Net salaries paid to {employee}", _fmt_money(cpj_payment), _fmt_money(cpj_payment)]],
            journal_type="cpj_totals_ledger",
        ),
    ]

    headers = _general_ledger_account_headers()
    difficulty_norm = str(difficulty or "easy").strip().lower()
    if difficulty_norm == "easy":
        editable_cols = [4, 9]
    elif difficulty_norm == "medium":
        editable_cols = [2, 3, 4, 7, 8, 9]
    else:
        editable_cols = list(range(len(headers)))

    debit_amount = _round_money(opening_balance + net_salary)
    credit_amount = cpj_payment
    balance = _round_money(debit_amount - credit_amount)
    total = _fmt_money(max(debit_amount, credit_amount))

    row_values = [
        [month_short, "1", "Balance b/d", "b/d", _fmt_money(opening_balance) if opening_balance else "", "", "", "", "", ""],
        [month_short, "30", "Salaries", "SJ", _fmt_money(net_salary), "", "", "", "", ""],
        ["", "", "", "", "", month_short, "30", "Bank", "CPJ", _fmt_money(cpj_payment)],
        ["", "", "", "", "", month_short, "30", "Balance c/d", "c/d", _fmt_money(balance)],
        ["", "", "Totals", "", total, "", "", "Totals", "", total],
        [next_month_short, "1", "Balance b/d", "b/d", _fmt_money(balance), "", "", "", "", ""],
    ]

    def _cell_hint_builder(row_index: int, col_index: int, expected: str) -> str:
        if row_index == 1 and col_index in {2, 3, 4}:
            return "Post the net salaries total from the Salary Journal to the debit side of Creditors for salaries."
        if row_index == 2 and col_index in {7, 8, 9}:
            return "Post the CPJ settlement on the credit side because the liability is being paid off."
        if row_index == 3 and col_index in {7, 8, 9, 2, 3, 4}:
            return "Balance c/d is the amount needed to make both sides equal."
        if row_index == 4:
            return "Totals must agree after the balancing figure has been inserted."
        if row_index == 5:
            return "Carry the closing balance down to the next month as Balance b/d."
        return "Use the source tables to decide the correct side, details, folio, and amount."

    def _derivation_builder(row_index: int, col_index: int, expected: str) -> str:
        if row_index == 1:
            return f"Post the net salaries total from the Salary Journal: debit Creditors for salaries R{_fmt_money(net_salary)}."
        if row_index == 2:
            return f"Post the CPJ settlement: credit Creditors for salaries R{_fmt_money(cpj_payment)}."
        if row_index == 3:
            return f"Balance c/d = debit total R{_fmt_money(debit_amount)} - credit total R{_fmt_money(credit_amount)} = R{_fmt_money(balance)}."
        if row_index == 4:
            return f"Totals on both sides must equal R{total}."
        if row_index == 5:
            return f"Carry forward the closing balance of R{_fmt_money(balance)} as Balance b/d."
        return f"Use the source information to enter {expected}."

    rows, correct_map, cell_hints, derivation_map = _build_table_rows(
        table_index=0,
        row_values=row_values,
        editable_cols_by_row=[editable_cols[:] for _ in row_values],
        cell_hint_builder=_cell_hint_builder,
        derivation_builder=_derivation_builder,
    )

    header_rows = [
        [{"label": f"General ledger of {business}", "colSpan": len(headers)}],
        [{"label": "Dr.", "colSpan": 1}, {"label": "Creditors for salaries", "colSpan": 8}, {"label": "B12", "colSpan": 1}],
        [{"label": "Month"}, {"label": "Day"}, {"label": "Details"}, {"label": "Fol"}, {"label": "Amount"}, {"label": "Month"}, {"label": "Day"}, {"label": "Details"}, {"label": "Fol"}, {"label": "Amount"}],
    ]

    question = _make_journal(
        prompt=(
            f"{business}\n"
            f"General Ledger for {month}\n\n"
            "Use the Salary Journal totals and the CPJ settlement to complete the Creditors for salaries account.\n"
            "Required: post the net salaries total, the payment, balance the account, and bring the balance down."
        ),
        journal_type="general_ledger",
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        header_rows=header_rows,
        guidelines=[
            "Post the net salaries amount from the Salary Journal to Creditors for salaries.",
            "Post the CPJ payment on the opposite side to reduce the liability.",
            "Insert the balancing figure, totals, and next month's Balance b/d.",
        ],
        cell_hints=cell_hints,
        derivation_map=derivation_map,
    )
    question["question_type"] = "ledger"
    question["expected_answer_type"] = "ledger"
    question["journal"]["heading"] = "Creditors for salaries account"
    question["journals"] = [question["journal"]]
    question["prompt_journals"] = prompt_journals
    question["marks"] = max(4, len(correct_map))
    question["visual_aid_key"] = "salaries_wages"
    question = _with_validation(question, f"general_ledger_fill_in_{difficulty_norm}", expected_cells=len(correct_map))
    return _set_recommended_difficulties(question, difficulty_norm)


# ---------------------------------------------------------------------------
# Sub-skill generators
# ---------------------------------------------------------------------------

def _gen_salary_scale(r: random.Random) -> List[Dict[str, Any]]:
    """Archetype Activity 1 — salary scale table + bonus + 13th cheque."""
    pool: List[Dict[str, Any]] = []
    biz = _pick_business(r)
    emp = _pick_employee(r)

    # Random salary scale parameters (like archetype: 180 000 × 12 000 – 204 000 × 18 000 – 240 000)
    start_salary = r.choice([96000, 120000, 144000, 156000, 168000, 180000, 192000, 204000])
    inc1 = r.choice([6000, 8000, 9000, 10000, 12000])
    notch_count1 = r.choice([2, 3])
    mid_salary = start_salary + inc1 * notch_count1
    inc2 = r.choice([12000, 15000, 18000, 20000])
    notch_count2 = r.choice([1, 2])
    max_salary = mid_salary + inc2 * notch_count2

    start_year = r.choice([2021, 2022, 2023, 2024])
    scale_str = f"{start_salary:,} × {inc1:,} – {mid_salary:,} × {inc2:,} – {max_salary:,}"
    scale_context = f"{biz} employed {emp} on 1 January {start_year}. The salary scale is: {scale_str}."
    first_increase_year = start_year + 1

    # Build salary table rows
    years_data = []
    current = start_salary
    yr = start_year
    for i in range(notch_count1 + notch_count2 + 1):
        monthly = _round_money(current / 12)
        if i == 0:
            increase = 0
        elif i <= notch_count1:
            increase = inc1
        else:
            increase = inc2
        current_before = current
        if i > 0:
            current = current_before  # already incremented below
        years_data.append({"year": yr, "increase": increase, "annual": current, "monthly": monthly})
        yr += 1
        if i < notch_count1:
            current += inc1
        elif i < notch_count1 + notch_count2:
            current += inc2

    # MCQ about salary scale concepts
    pool.append(_set_recommended_difficulties(_make_mcq(
        prompt=f"{scale_context}\n\nIn the salary scale notation, what does '×' represent?",
        options=[
            "Multiplication of the salary by that factor.",
            "The annual increment (increase) added to the previous notch.",
            "The monthly salary amount.",
            "The tax rate applied to the salary.",
        ],
        correct_index=1,
        explanation="In a salary scale, '×' indicates the annual increase (increment) from one notch to the next. It does NOT mean multiplication.",
    ), "easy", "medium"))

    pool.append(_set_recommended_difficulties(_with_validation(_make_calc(
        prompt=f"{scale_context}\n\nWhat is {emp}'s initial annual salary on appointment?",
        correct_answer=float(start_salary),
        working_formula=f"Starting annual salary = R{start_salary:,.2f}",
    ), "salary_scale_initial_annual", annual_salary=start_salary), "easy"))

    pool.append(_set_recommended_difficulties(_with_validation(_make_calc(
        prompt=f"{scale_context}\n\nWhat is the annual increase before {emp} reaches R{mid_salary:,.2f}?",
        correct_answer=float(inc1),
        working_formula=f"The first increase shown after × is R{inc1:,.2f}",
    ), "salary_scale_first_increment", increment=inc1), "easy"))

    pool.append(_set_recommended_difficulties(_make_mcq(
        prompt=f"{scale_context}\n\nWhen will {emp} receive the first salary increase on this scale?",
        options=[
            f"Immediately on 1 January {start_year}",
            f"In {first_increase_year}",
            f"Only after reaching R{mid_salary:,.2f}",
            f"Only after reaching the final notch of R{max_salary:,.2f}",
        ],
        correct_index=1,
        explanation=f"The employee starts on the opening notch in {start_year}. The first annual increase is received in the next year, {first_increase_year}.",
    ), "easy"))

    # Calc: monthly salary in Year 1
    pool.append(_set_recommended_difficulties(_with_validation(_make_calc(
        prompt=f"{scale_context}\n\nCalculate {emp}'s initial monthly salary on appointment (before deductions).",
        correct_answer=_round_money(start_salary / 12),
        working_formula=f"Annual salary ÷ 12 = {start_salary:,} ÷ 12",
    ), "salary_scale_monthly_year1", annual_salary=start_salary), "easy"))

    # Calc: annual salary in Year 3
    if len(years_data) >= 3:
        y3 = years_data[2]
        pool.append(_set_recommended_difficulties(_with_validation(_make_calc(
            prompt=f"{scale_context}\n\nWhat is {emp}'s annual salary in {y3['year']}?",
            correct_answer=float(y3["annual"]),
            working_formula=f"Year 1 salary + increment × 2 = {start_salary:,} + {inc1:,} × 2",
        ), "salary_scale_annual_year", expected_annual=float(y3["annual"])), "medium", "hard"))

    if len(years_data) >= 2:
        y2 = years_data[1]
        pool.append(_set_recommended_difficulties(_with_validation(_make_calc(
            prompt=(
                f"{scale_context}\n\n"
                f"In {y2['year']}, {emp}'s monthly salary is R{y2['monthly']:,.2f}. Calculate the annual salary for that year."
            ),
            correct_answer=float(y2["annual"]),
            working_formula=f"Annual salary = R{y2['monthly']:,.2f} × 12",
        ), "salary_scale_annual_from_monthly", monthly_salary=float(y2["monthly"])), "easy", "medium"))

        pool.append(_set_recommended_difficulties(_with_validation(_make_calc(
            prompt=(
                f"{scale_context}\n\n"
                f"Calculate the increase in annual salary from {years_data[0]['year']} to {y2['year']}."
            ),
            correct_answer=_round_money(float(y2["annual"]) - float(years_data[0]["annual"])),
            working_formula=(
                f"Increase = R{float(y2['annual']):,.2f} - R{float(years_data[0]['annual']):,.2f} = "
                f"R{_round_money(float(y2['annual']) - float(years_data[0]['annual'])):,.2f}"
            ),
        ), "salary_scale_annual_increase", later_annual=float(y2["annual"]), earlier_annual=float(years_data[0]["annual"])), "easy", "medium"))

    # Bonus calculation (archetype 1.2 pattern)
    bonus_pct = r.choice([50, 60, 70, 80])
    bonus_year_idx = min(2, len(years_data) - 1)
    bonus_monthly = years_data[bonus_year_idx]["monthly"]
    bonus_amount = _round_money(bonus_pct / 100 * bonus_monthly)
    bonus_total = _round_money(bonus_monthly + (bonus_pct / 100 * bonus_monthly))
    pool.append(_set_recommended_difficulties(_with_validation(_make_calc(
        prompt=(
            f"{scale_context}\n\n"
            f"In {years_data[bonus_year_idx]['year']}, {emp}'s monthly salary is R{bonus_monthly:,.2f} before deductions. "
            f"{emp} receives a bonus of {bonus_pct}% of monthly salary on 30 June {years_data[bonus_year_idx]['year']}. "
            f"What will the total salary payment (salary + bonus) be for that month, prior to deductions?"
        ),
        correct_answer=bonus_total,
        working_formula=(
            f"Monthly salary = R{bonus_monthly:,.2f}\n"
            f"Bonus = {bonus_pct}% × R{bonus_monthly:,.2f} = R{bonus_amount:,.2f}\n"
            f"Total salary payment = R{bonus_monthly:,.2f} + R{bonus_amount:,.2f} = R{bonus_total:,.2f}"
        ),
    ), "salary_scale_bonus_total", monthly_salary=float(bonus_monthly), bonus_pct=float(bonus_pct)), "medium", "hard"))

    # 13th cheque (archetype 1.3 pattern)
    last_idx = min(len(years_data) - 1, 4)
    cheque_monthly = years_data[last_idx]["monthly"]
    pool.append(_set_recommended_difficulties(_with_validation(_make_calc(
        prompt=(
            f"{scale_context}\n\n"
            f"In {years_data[last_idx]['year']}, {emp}'s monthly salary is R{cheque_monthly:,.2f} before deductions. "
            f"{emp} receives a thirteenth cheque on 31 December {years_data[last_idx]['year']} equal to one month's salary. "
            f"What is the total salary payment for December {years_data[last_idx]['year']}?"
        ),
        correct_answer=_round_money(cheque_monthly * 2),
        working_formula=(
            f"Monthly salary = R{cheque_monthly:,.2f}\n"
            f"Thirteenth cheque = R{cheque_monthly:,.2f}\n"
            f"Total salary payment = R{cheque_monthly:,.2f} + R{cheque_monthly:,.2f} = R{_round_money(cheque_monthly * 2):,.2f}"
        ),
    ), "salary_scale_thirteenth_cheque", monthly_salary=float(cheque_monthly)), "medium", "hard"))

    pool.append(_set_recommended_difficulties(_make_typed(
        prompt=f"{biz} uses the salary scale {scale_str}. Explain what the final figure in the salary scale tells you about {emp}'s remuneration.",
        sample_answer=(
            f"1. The final figure of R{max_salary:,.2f} shows the maximum annual salary on that salary scale.\n"
            f"2. Once {emp} reaches that notch, there are no further annual increases on this scale unless the scale itself is revised."
        ),
        grading_rubric=["maximum annual salary on the scale", "top notch / no further increase on that scale"],
    ), "medium", "hard"))

    return pool


def _gen_gross_wage(r: random.Random) -> List[Dict[str, Any]]:
    """Archetype Activity 2 — gross wage calculation with ordinary + overtime."""
    pool: List[Dict[str, Any]] = []
    emp = _pick_employee(r)

    ordinary_rate = r.choice([18, 20, 22, 25, 27, 30, 35, 40, 45, 50, 55, 60])
    overtime_rate = _round_money(ordinary_rate * r.choice([1.25, 1.5, 1.75]))
    total_hours = r.choice([42, 43, 44, 45, 46, 47, 48])

    ordinary_hours = 40
    overtime_hours = total_hours - ordinary_hours
    basic_wage = _round_money(ordinary_hours * ordinary_rate)
    overtime_pay = _round_money(overtime_hours * overtime_rate)
    gross_wage = _round_money(basic_wage + overtime_pay)

    # Concept MCQ
    pool.append(_make_mcq(
        prompt="What is ordinary time?",
        options=[
            "Any hours the employee chooses to work.",
            "The standard working hours per week, usually 40 hours.",
            "Only hours worked on weekdays.",
            "Hours worked during lunch breaks.",
        ],
        correct_index=1,
        explanation="Ordinary time is the standard working hours per week, usually 40 hours. Hours above this are overtime.",
    ))

    # Gross wage calc
    pool.append(_with_validation(_make_calc(
        prompt=f"{emp} receives R{ordinary_rate:.2f} per hour for ordinary time and R{overtime_rate:.2f} per hour for overtime. {emp} worked {total_hours} hours this week.\n\nCalculate the gross wage for the week.",
        correct_answer=gross_wage,
        working_formula=f"({ordinary_hours} × R{ordinary_rate:.2f}) + ({overtime_hours} × R{overtime_rate:.2f}) = R{basic_wage:.2f} + R{overtime_pay:.2f}",
    ), "gross_wage_total", ordinary_hours=ordinary_hours, ordinary_rate=float(ordinary_rate), overtime_hours=overtime_hours, overtime_rate=float(overtime_rate)))

    # Net wage formula MCQ
    pool.append(_make_mcq(
        prompt="Which formula correctly calculates net wage?",
        options=[
            "Net wage = Basic wage + Overtime",
            "Net wage = Gross wage – Deductions",
            "Net wage = Gross wage + Employer contributions",
            "Net wage = Cost of sales – Deductions",
        ],
        correct_index=1,
        explanation="Net wage = Gross wage – Deductions. Gross wage = Basic wage + Overtime.",
    ))

    # Public holiday scenario (archetype Activity 2 pattern)
    pub_holiday_hours = 8 * r.choice([3, 4])  # fewer ordinary hours due to PH
    remaining_ordinary = pub_holiday_hours
    extra_total = r.choice([pub_holiday_hours + 3, pub_holiday_hours + 5, pub_holiday_hours + 8])
    ot_hours_ph = extra_total - remaining_ordinary
    if ot_hours_ph < 0:
        ot_hours_ph = 0
    basic_ph = _round_money(remaining_ordinary * ordinary_rate)
    ot_ph = _round_money(ot_hours_ph * overtime_rate)
    gross_ph = _round_money(basic_ph + ot_ph)
    pool.append(_with_validation(_make_calc(
        prompt=f"Monday is a public holiday. {emp} worked {extra_total} hours during the week (ordinary rate R{ordinary_rate:.2f}/hr, overtime R{overtime_rate:.2f}/hr). Ordinary time = 8hrs × {remaining_ordinary // 8} days = {remaining_ordinary} hours.\n\nCalculate the gross wage.",
        correct_answer=gross_ph,
        working_formula=f"({remaining_ordinary} × R{ordinary_rate:.2f}) + ({ot_hours_ph} × R{overtime_rate:.2f})",
    ), "gross_wage_total", ordinary_hours=remaining_ordinary, ordinary_rate=float(ordinary_rate), overtime_hours=ot_hours_ph, overtime_rate=float(overtime_rate)))

    inferred_overtime = int(r.choice([2, 4, 6, 8]))
    inferred_gross = _round_money((ordinary_hours * ordinary_rate) + (inferred_overtime * overtime_rate))
    pool.append(_with_validation(_make_calc(
        prompt=(
            f"{emp} earns R{ordinary_rate:.2f} per hour for ordinary time and R{overtime_rate:.2f} per hour for overtime. "
            f"The gross wage for the week was R{inferred_gross:,.2f} after {ordinary_hours} ordinary hours were worked. "
            f"How many overtime hours were worked?"
        ),
        correct_answer=float(inferred_overtime),
        unit="",
        working_formula=(
            f"Basic wage = {ordinary_hours} × R{ordinary_rate:.2f} = R{_round_money(ordinary_hours * ordinary_rate):,.2f}\n"
            f"Overtime pay = R{inferred_gross:,.2f} - R{_round_money(ordinary_hours * ordinary_rate):,.2f} = R{_round_money(inferred_gross - (ordinary_hours * ordinary_rate)):,.2f}\n"
            f"Overtime hours = R{_round_money(inferred_gross - (ordinary_hours * ordinary_rate)):,.2f} ÷ R{overtime_rate:.2f} = {inferred_overtime}"
        ),
    ), "gross_wage_overtime_hours", gross_wage=float(inferred_gross), basic_wage=_round_money(ordinary_hours * ordinary_rate), overtime_rate=float(overtime_rate)))

    paye_pct = float(r.choice([18, 20, 22]))
    medical_deduction = float(r.choice([0, 120, 200, 260]))
    uif_deduction = _round_money(gross_wage * 0.01)
    paye_deduction = _round_money(gross_wage * paye_pct / 100)
    total_deductions = _round_money(paye_deduction + medical_deduction + uif_deduction)
    net_wage = _round_money(gross_wage - total_deductions)
    pool.append(_with_validation(_make_calc(
        prompt=(
            f"{emp}'s gross wage for the week is R{gross_wage:,.2f}. Deductions are PAYE {paye_pct}% of gross wage, "
            f"medical aid R{medical_deduction:,.2f}, and UIF 1% of gross wage. Calculate the net wage."
        ),
        correct_answer=net_wage,
        working_formula=(
            f"PAYE = R{paye_deduction:,.2f}\n"
            f"Medical aid = R{medical_deduction:,.2f}\n"
            f"UIF = R{uif_deduction:,.2f}\n"
            f"Total deductions = R{total_deductions:,.2f}\n"
            f"Net wage = R{gross_wage:,.2f} - R{total_deductions:,.2f} = R{net_wage:,.2f}"
        ),
    ), "gross_wage_net_wage", gross_wage=float(gross_wage), paye=paye_deduction, medical=medical_deduction, uif=uif_deduction))

    return pool


def _gen_deductions(r: random.Random) -> List[Dict[str, Any]]:
    """Deductions — PAYE, pension, medical, UIF concepts and calculations."""
    pool: List[Dict[str, Any]] = []
    emp = _pick_employee(r)
    biz = _pick_business(r)

    gross_salary = r.choice([8300, 10800, 12500, 15000, 18000, 20000, 25000])
    paye_pct = r.choice([18, 20, 22, 25])
    pension_pct = r.choice([7, 7.5, 8])
    medical = r.choice([200, 240, 280, 320, 400, 500, 600, 800, 960])
    uif_pct = 1  # always 1%

    paye_amt = _round_money(gross_salary * paye_pct / 100)
    pension_amt = _round_money(gross_salary * pension_pct / 100)
    uif_amt = _round_money(gross_salary * uif_pct / 100)
    total_ded = _round_money(paye_amt + pension_amt + medical + uif_amt)
    net_salary = _round_money(gross_salary - total_ded)

    # Concept MCQs
    pool.append(_make_mcq(
        prompt="What is PAYE?",
        options=[
            "Pay-as-you-earn — income tax deducted monthly from employee salaries.",
            "Profit after yearly expenses.",
            "Post-audit year-end evaluation.",
            "Pension accumulated yearly for employees.",
        ],
        correct_index=0,
        explanation="PAYE (Pay-As-You-Earn) is income tax deducted monthly from employees' salaries and paid to SARS.",
    ))

    pool.append(_make_mcq(
        prompt="Why are pension fund contributions deducted from employee salaries?",
        options=[
            "To pay for the employer's personal retirement.",
            "To save money for when the employee goes on pension/retirement.",
            "To pay income tax to SARS.",
            "To fund the business's insurance policy.",
        ],
        correct_index=1,
        explanation="Employees contribute to pension funds to save money for when they go on pension/retirement.",
    ))

    pool.append(_make_mcq(
        prompt="How is taxable income calculated for PAYE purposes?",
        options=[
            "Taxable income = Gross salary + Pension fund contribution.",
            "Taxable income = Net salary – Medical aid.",
            "Taxable income = Gross salary – Pension fund contribution.",
            "Taxable income = Gross salary × PAYE rate.",
        ],
        correct_index=2,
        explanation="Taxable income = Gross salary – Pension fund contribution. PAYE is then calculated on this amount.",
    ))

    # Net salary calculation
    pool.append(_with_validation(_make_calc(
        prompt=(
            f"{emp} at {biz} earns a gross monthly salary of R{gross_salary:,.2f}.\n"
            f"Deductions: PAYE {paye_pct}%, Pension {pension_pct}%, Medical aid R{medical:,.2f}, UIF {uif_pct}%.\n\n"
            f"Calculate the net salary."
        ),
        correct_answer=net_salary,
        working_formula=(
            f"PAYE = R{paye_amt:,.2f}, Pension = R{pension_amt:,.2f}, Medical = R{medical:,.2f}, UIF = R{uif_amt:,.2f}\n"
            f"Total deductions = R{total_ded:,.2f}\n"
            f"Net salary = R{gross_salary:,.2f} – R{total_ded:,.2f}"
        ),
    ), "deductions_net_salary", gross_salary=gross_salary, paye=paye_amt, pension=pension_amt, medical=medical, uif=uif_amt))

    # PAYE only calc
    pool.append(_with_validation(_make_calc(
        prompt=f"{emp} has a gross salary of R{gross_salary:,.2f}. PAYE is deducted at {paye_pct}% of gross salary. Calculate the PAYE deduction.",
        correct_answer=paye_amt,
        working_formula=f"{paye_pct}% × R{gross_salary:,.2f}",
    ), "deductions_single_percentage", gross_salary=gross_salary, percentage=paye_pct, expected=paye_amt))

    # Pension only calc
    pool.append(_with_validation(_make_calc(
        prompt=f"{emp} has a gross salary of R{gross_salary:,.2f}. Pension fund contribution is {pension_pct}% of gross salary. Calculate the pension deduction.",
        correct_answer=pension_amt,
        working_formula=f"{pension_pct}% × R{gross_salary:,.2f}",
    ), "deductions_single_percentage", gross_salary=gross_salary, percentage=pension_pct, expected=pension_amt))

    pool.append(_with_validation(_make_calc(
        prompt=(
            f"{emp}'s salary advice for the month shows gross salary R{gross_salary:,.2f}, pension fund deduction R{pension_amt:,.2f}, "
            f"medical aid R{medical:,.2f}, UIF R{uif_amt:,.2f}, and net salary R{net_salary:,.2f}. "
            f"Calculate the PAYE deduction shown on the salary advice."
        ),
        correct_answer=paye_amt,
        working_formula=(
            f"PAYE = Gross salary - (Pension + Medical aid + UIF + Net salary)\n"
            f"PAYE = R{gross_salary:,.2f} - (R{pension_amt:,.2f} + R{medical:,.2f} + R{uif_amt:,.2f} + R{net_salary:,.2f}) = R{paye_amt:,.2f}"
        ),
    ), "deductions_salary_advice_missing_paye", gross_salary=gross_salary, pension=pension_amt, medical=medical, uif=uif_amt, net_salary=net_salary))

    pool.append(_make_typed(
        prompt="Explain the difference between a deduction and an employer contribution in the salaries and wages system.",
        sample_answer=(
            "1. A deduction is an amount taken off the employee's gross salary or wage, such as PAYE, UIF, pension, or medical aid.\n"
            "2. An employer contribution is an additional amount paid by the employer on top of the employee's remuneration, such as SDL or the employer's UIF and pension contributions."
        ),
        grading_rubric=["deduction taken from employee pay", "contribution paid by employer in addition to pay"],
    ))

    return pool


def _gen_employer_contributions(r: random.Random) -> List[Dict[str, Any]]:
    """Employer contributions — SDL, UIF, pension, medical aid matching."""
    pool: List[Dict[str, Any]] = []
    biz = _pick_business(r)
    employees = _pick_employees(r, 3)

    total_gross = r.choice([31600, 25000, 40000, 55000])
    sdl_pct = 1  # always 1%
    sdl = _round_money(total_gross * sdl_pct / 100)

    # SDL concept
    pool.append(_make_mcq(
        prompt="What is the Skills Development Levy (SDL)?",
        options=[
            "A deduction from employees' salaries for skills training.",
            "A levy paid by the employer (1% of gross salaries) to SARS to finance skills development.",
            "A voluntary donation by the business to schools.",
            "A tax paid by employees on their overtime income.",
        ],
        correct_index=1,
        explanation="SDL is paid by the employer at 1% of total gross salaries/wages and paid to SARS. It funds skills development through SETAs.",
    ))

    # SDL calc
    pool.append(_with_validation(_make_calc(
        prompt=f"{biz}'s total gross salaries for the month are R{total_gross:,.2f}. Calculate the Skills Development Levy (SDL) at 1%.",
        correct_answer=sdl,
        working_formula=f"1% × R{total_gross:,.2f}",
    ), "employer_single_percentage", gross_amount=total_gross, percentage=sdl_pct, expected=sdl))

    # Employer medical aid matching (archetype: R1.50 for each R1)
    emp_medical = r.choice([200, 240, 280, 400, 500])
    match_ratio = r.choice([1.0, 1.5, 2.0])
    employer_medical = _round_money(emp_medical * match_ratio)
    emp_name = r.choice(employees)
    pool.append(_with_validation(_make_calc(
        prompt=f"{biz}'s contribution to medical aid is R{match_ratio:.2f} for each R1 contributed by the employee. {emp_name}'s medical aid deduction is R{emp_medical:,.2f}.\n\nCalculate {biz}'s medical aid contribution for {emp_name}.",
        correct_answer=employer_medical,
        working_formula=f"R{match_ratio:.2f} × R{emp_medical:,.2f}",
    ), "employer_ratio_contribution", employee_amount=emp_medical, ratio=match_ratio, expected=employer_medical))

    # Employer pension matching (rand-to-rand)
    emp_pension = r.choice([581, 756, 875, 1200, 1500])
    pension_ratio = r.choice([1.0, 1.5])
    employer_pension = _round_money(emp_pension * pension_ratio)
    pool.append(_with_validation(_make_calc(
        prompt=f"{biz}'s pension fund contribution is on a {'rand-to-rand' if pension_ratio == 1.0 else f'R{pension_ratio:.2f} for every R1'} basis. {emp_name}'s pension deduction is R{emp_pension:,.2f}.\n\nCalculate {biz}'s pension contribution for {emp_name}.",
        correct_answer=employer_pension,
        working_formula=f"R{pension_ratio:.2f} × R{emp_pension:,.2f}",
    ), "employer_ratio_contribution", employee_amount=emp_pension, ratio=pension_ratio, expected=employer_pension))

    gross_salary = float(r.choice([14500, 18000, 22500, 26000]))
    employer_uif = _round_money(gross_salary * 0.01)
    employer_pension_cost = _round_money(gross_salary * r.choice([0.075, 0.10]))
    employer_medical_cost = float(r.choice([600, 900, 1200, 1500]))
    cost_to_company = _round_money(gross_salary + employer_uif + employer_pension_cost + employer_medical_cost)
    pool.append(_with_validation(_make_calc(
        prompt=(
            f"{biz} pays an employee a gross monthly salary of R{gross_salary:,.2f}. The employer also pays UIF of 1% of gross salary, "
            f"pension contribution of R{employer_pension_cost:,.2f}, and medical aid contribution of R{employer_medical_cost:,.2f}. "
            f"Calculate the total cost-to-company for the month."
        ),
        correct_answer=cost_to_company,
        working_formula=(
            f"Gross salary = R{gross_salary:,.2f}\n"
            f"Employer UIF = R{employer_uif:,.2f}\n"
            f"Employer pension = R{employer_pension_cost:,.2f}\n"
            f"Employer medical aid = R{employer_medical_cost:,.2f}\n"
            f"Cost-to-company = R{gross_salary:,.2f} + R{employer_uif:,.2f} + R{employer_pension_cost:,.2f} + R{employer_medical_cost:,.2f} = R{cost_to_company:,.2f}"
        ),
    ), "employer_cost_to_company", gross_salary=gross_salary, employer_uif=employer_uif, employer_pension=employer_pension_cost, employer_medical=employer_medical_cost))

    employee_uif_total = _round_money(total_gross * 0.01)
    employer_uif_total = _round_money(total_gross * 0.01)
    amount_payable_sars = _round_money(employee_uif_total + employer_uif_total + sdl)
    pool.append(_with_validation(_make_calc(
        prompt=(
            f"For the month, {biz} must pay employee UIF contributions of R{employee_uif_total:,.2f}, employer UIF contributions of R{employer_uif_total:,.2f}, "
            f"and SDL of R{sdl:,.2f} to SARS. Calculate the total amount payable to SARS."
        ),
        correct_answer=amount_payable_sars,
        working_formula=(
            f"Amount payable to SARS = Employee UIF + Employer UIF + SDL\n"
            f"= R{employee_uif_total:,.2f} + R{employer_uif_total:,.2f} + R{sdl:,.2f} = R{amount_payable_sars:,.2f}"
        ),
    ), "employer_amount_payable_sars", employee_uif=employee_uif_total, employer_uif=employer_uif_total, sdl=sdl))

    # UIF employer contribution concept
    pool.append(_make_mcq(
        prompt="Who pays UIF contributions?",
        options=[
            "Only the employee.",
            "Only the employer.",
            "Both the employer and the employee — paid to SARS monthly.",
            "Neither — UIF is funded by government directly.",
        ],
        correct_index=2,
        explanation="Both employer and employee contribute to UIF. Both contributions are paid to SARS at the end of each month.",
    ))

    return pool


def _gen_ethics(r: random.Random) -> List[Dict[str, Any]]:
    """Ethics related to salaries and wages — contracts, unions, fairness."""
    pool: List[Dict[str, Any]] = []

    pool.append(_make_mcq(
        prompt="An employer dismisses a worker who is HIV-positive because of their status. Is this legal?",
        options=[
            "Yes, the employer can dismiss anyone at any time.",
            "No — an employee may NOT be dismissed because they are HIV-positive. Dismissal can only occur due to incapacity if the employee can no longer do the work.",
            "Yes, but only if the employer pays severance.",
            "No, but the employer can reduce their salary instead.",
        ],
        correct_index=1,
        explanation="According to the Labour Relations Act, an employee may not be dismissed because of HIV/AIDS status. Dismissal may only occur on grounds of incapacity if the employee can no longer perform the work.",
    ))

    pool.append(_make_typed(
        prompt="Explain TWO ethical responsibilities of an employer regarding the payment of salaries and wages.",
        sample_answer=(
            "Required points:\n"
            "1. The employer must pay employees according to their agreed contract and in line with their responsibilities.\n"
            "2. The employer must make all statutory deductions, such as PAYE and UIF, correctly and pay them over to the relevant institution.\n"
            "Other valid points may be:\n"
            "- Employees should receive proper salary advice slips showing gross salary, deductions, and net salary.\n"
            "- The employer should keep accurate salary and wage records."
        ),
        grading_rubric=["pay according to contract / responsibilities", "correct statutory deductions", "salary advice / documentation"],
    ))

    pool.append(_make_mcq(
        prompt="What is the role of trade unions in the workplace?",
        options=[
            "Trade unions set the selling prices for the company's products.",
            "Trade unions represent employees and negotiate wages, working conditions, and protect workers' rights.",
            "Trade unions manage the company's bank account.",
            "Trade unions are responsible for paying PAYE to SARS.",
        ],
        correct_index=1,
        explanation="Trade unions represent employees in negotiations about wages, working conditions, and protect workers' rights.",
    ))

    pool.append(_make_typed(
        prompt="Explain ONE way HIV/AIDS can influence a business's costs related to salaries and wages.",
        sample_answer=(
            "One valid explanation:\n"
            "- HIV-positive employees may become ill, which can reduce work output and increase absenteeism.\n"
            "- The business may then face higher medical aid costs, more sick leave, and the cost of training replacement workers."
        ),
        grading_rubric=["decreased productivity / work output", "higher medical / sick leave costs", "training replacements"],
    ))

    return pool


def _gen_glossary_matching(r: random.Random) -> List[Dict[str, Any]]:
    """Glossary matching — table_wordbank for key terms."""
    pool: List[Dict[str, Any]] = []

    all_terms = [
        {"term": "Gross salary", "definition": "Basic salary per month prior to deductions."},
        {"term": "Net salary", "definition": "Gross salary minus deductions — the amount the employee takes home."},
        {"term": "Overtime remuneration", "definition": "Remuneration paid to workers who work longer hours than ordinary time."},
        {"term": "PAYE", "definition": "Pay-As-You-Earn — income tax deducted monthly from employees' salaries."},
        {"term": "SDL", "definition": "Skills Development Levy — 1% of gross salaries paid by the employer to SARS."},
        {"term": "UIF", "definition": "Unemployment Insurance Fund — contributions by both employer and employee."},
        {"term": "Salary advice", "definition": "Slip given to an employee showing gross salary, deductions, and net salary."},
        {"term": "Ordinary time", "definition": "Standard working hours per week, usually 40 hours."},
        {"term": "Gross wage", "definition": "Basic wage plus overtime prior to deductions."},
        {"term": "Net wage", "definition": "Gross wage minus deductions — amount paid to the worker."},
    ]

    distractors = [
        "Trading stock deficit",
        "Bad debts written off",
        "Depreciation on vehicles",
        "Creditors for salaries",
        "Accrued income",
    ]

    r.shuffle(all_terms)
    selected = all_terms[:5]

    terms_list = [t["term"] for t in selected] + r.sample(distractors, k=2)
    r.shuffle(terms_list)

    word_bank = [{"id": f"t{i}", "label": t} for i, t in enumerate(terms_list)]
    label_to_id = {wb["label"]: wb["id"] for wb in word_bank}

    rows = []
    correct_map = {}
    for i, item in enumerate(selected):
        rows.append([str(i + 1), item["definition"], ""])
        correct_map[str(i)] = {"2": label_to_id.get(item["term"], "")}

    pool.append(_make_table_wordbank(
        prompt="Match each definition with the correct term from the word bank.",
        headers=["No.", "Definition", "Term"],
        rows=rows,
        word_bank=word_bank,
        correct_map=correct_map,
        guidelines=["Read each definition carefully.", "Select the correct term from the word bank for each row."],
    ))

    return pool


def _gen_salary_journal(r: random.Random) -> List[Dict[str, Any]]:
    pool: List[Dict[str, Any]] = []
    pool.append(_make_salary_journal_fill_question(r=r, difficulty="easy"))
    pool.append(_make_salary_journal_fill_question(r=r, difficulty="medium"))
    pool.append(_make_salary_journal_fill_question(r=r, difficulty="hard"))
    biz = _pick_business(r)
    emp = _pick_employee(r)
    basic_salary = float(r.choice([12000, 15000, 17000, 18000, 20000]))
    commission = float(r.choice([0, 2500, 4000, 6500]))
    bonus = float(r.choice([0, 1500, 2500, 3200]))
    gross_salary = _round_money(basic_salary + commission)
    paye = float(r.choice([1200, 1500, 2200, 2750, 3300]))
    pension_pct = float(r.choice([7.5, 8.0]))
    pension = _round_money(basic_salary * pension_pct / 100)
    medical = float(r.choice([300, 600, 900, 1200]))
    uif = _round_money(basic_salary * 0.01)
    total_deductions = _round_money(paye + pension + medical + uif)
    net_salary = _round_money(gross_salary - total_deductions)
    employer_pension = _round_money(basic_salary * r.choice([0.10, 0.12, 0.15]))

    pool.append(_with_validation(_make_calc(
        prompt=(
            f"The Salary Journal of {biz} for month-end includes {emp}. {emp} earns a basic salary of R{basic_salary:,.2f} "
            f"and commission of R{commission:,.2f}. Deductions are PAYE R{paye:,.2f}, pension {pension_pct}% of basic salary, "
            f"medical aid R{medical:,.2f}, and UIF 1% of basic salary. Calculate the net salary to be entered in the Salary Journal."
        ),
        correct_answer=net_salary,
        working_formula=(
            f"Gross salary = R{basic_salary:,.2f} + R{commission:,.2f} = R{gross_salary:,.2f}\n"
            f"Total deductions = R{paye:,.2f} + R{pension:,.2f} + R{medical:,.2f} + R{uif:,.2f} = R{total_deductions:,.2f}\n"
            f"Net salary = R{gross_salary:,.2f} - R{total_deductions:,.2f} = R{net_salary:,.2f}"
        ),
    ), "salary_journal_net_salary", basic_salary=basic_salary, commission=commission, paye=paye, pension=pension, medical=medical, uif=uif))

    pool.append(_with_validation(_make_calc(
        prompt=(
            f"In the Salary Journal of {biz}, {emp}'s pension deduction is R{pension:,.2f} and the employer contributes R{employer_pension:,.2f}. "
            f"How much in total must be paid to the pension fund for {emp} for the month?"
        ),
        correct_answer=_round_money(pension + employer_pension),
        working_formula=(
            f"Employee pension deduction = R{pension:,.2f}\n"
            f"Employer pension contribution = R{employer_pension:,.2f}\n"
            f"Amount due to pension fund = R{pension:,.2f} + R{employer_pension:,.2f} = R{_round_money(pension + employer_pension):,.2f}"
        ),
    ), "salary_journal_pension_total", pension=pension, employer_pension=employer_pension))

    gross_salary_with_bonus = _round_money(basic_salary + commission + bonus)
    pool.append(_with_validation(_make_calc(
        prompt=(
            f"The Salary Journal for {biz} shows that {emp} earned a basic salary of R{basic_salary:,.2f}, commission of R{commission:,.2f}, "
            f"and a once-off bonus of R{bonus:,.2f} for the month. Calculate the gross salary column amount before deductions."
        ),
        correct_answer=gross_salary_with_bonus,
        working_formula=(
            f"Basic salary = R{basic_salary:,.2f}\n"
            f"Commission = R{commission:,.2f}\n"
            f"Bonus = R{bonus:,.2f}\n"
            f"Gross salary = R{basic_salary:,.2f} + R{commission:,.2f} + R{bonus:,.2f} = R{gross_salary_with_bonus:,.2f}"
        ),
    ), "salary_journal_gross_salary", basic_salary=basic_salary, commission=commission, bonus=bonus))

    salary_journal_word_bank = [
        {"id": "sj0", "label": "Basic salary"},
        {"id": "sj1", "label": "Commission"},
        {"id": "sj2", "label": "Bonus"},
        {"id": "sj3", "label": "Gross salary"},
        {"id": "sj4", "label": "PAYE"},
        {"id": "sj5", "label": "Net salary"},
        {"id": "sj6", "label": "Medical aid"},
    ]
    salary_journal_label_to_id = {item["label"]: item["id"] for item in salary_journal_word_bank}
    salary_journal_rows = [
        ["1", "The employee's fixed monthly remuneration before extras.", ""],
        ["2", "The extra earning based on performance or sales.", ""],
        ["3", "The once-off additional reward included in this month's remuneration.", ""],
        ["4", "The total remuneration before any deductions are taken off.", ""],
        ["5", "The statutory tax deduction paid over to SARS.", ""],
        ["6", "The amount still owed to the employee after deductions.", ""],
    ]
    salary_journal_correct_map = {
        "0": {"2": salary_journal_label_to_id["Basic salary"]},
        "1": {"2": salary_journal_label_to_id["Commission"]},
        "2": {"2": salary_journal_label_to_id["Bonus"]},
        "3": {"2": salary_journal_label_to_id["Gross salary"]},
        "4": {"2": salary_journal_label_to_id["PAYE"]},
        "5": {"2": salary_journal_label_to_id["Net salary"]},
    }
    pool.append(_with_validation(_make_table_wordbank(
        prompt="Match each Salary Journal description to the correct journal column heading from the word bank.",
        headers=["No.", "Salary Journal description", "Column heading"],
        rows=salary_journal_rows,
        word_bank=salary_journal_word_bank,
        correct_map=salary_journal_correct_map,
        guidelines=[
            "Decide whether the description refers to remuneration before deductions, a deduction, or the final amount due.",
            "Gross salary is before deductions, while net salary is after deductions.",
        ],
    ), "journal_wordbank", expected_rows=len(salary_journal_rows)))

    return pool


def _gen_wage_journal(r: random.Random) -> List[Dict[str, Any]]:
    pool: List[Dict[str, Any]] = []
    pool.append(_make_wage_journal_fill_question(r=r, difficulty="easy"))
    pool.append(_make_wage_journal_fill_question(r=r, difficulty="medium"))
    pool.append(_make_wage_journal_fill_question(r=r, difficulty="hard"))
    biz = _pick_business(r)
    emp = _pick_employee(r)
    normal_rate = float(r.choice([20, 25, 30, 40, 50, 60]))
    overtime_rate = _round_money(normal_rate * r.choice([1.5, 2.0]))
    normal_hours = int(r.choice([35, 40]))
    overtime_hours = int(r.choice([0, 4, 6, 8, 10]))
    basic_wage = _round_money(normal_hours * normal_rate)
    overtime_wage = _round_money(overtime_hours * overtime_rate)
    gross_wage = _round_money(basic_wage + overtime_wage)
    paye_pct = float(r.choice([18, 20, 22]))
    paye = _round_money(gross_wage * paye_pct / 100)
    pension = _round_money(basic_wage * 0.08)
    medical = float(r.choice([0, 150, 250, 320]))
    uif = _round_money(gross_wage * 0.01)
    total_deductions = _round_money(paye + pension + medical + uif)
    net_wage = _round_money(gross_wage - total_deductions)
    employer_uif = uif
    employer_pension = pension
    employer_medical = _round_money(medical * r.choice([1.0, 1.5, 2.0])) if medical else 0.0

    pool.append(_with_validation(_make_calc(
        prompt=(
            f"The Wages Journal of {biz} includes {emp}. {emp} worked {normal_hours} normal hours at R{normal_rate:,.2f} per hour "
            f"and {overtime_hours} overtime hours at R{overtime_rate:,.2f} per hour. Deductions are PAYE {paye_pct}% of gross wage, "
            f"pension 8% of basic wage, medical aid R{medical:,.2f}, and UIF 1% of gross wage. Calculate the net wage."
        ),
        correct_answer=net_wage,
        working_formula=(
            f"Gross wage = R{basic_wage:,.2f} + R{overtime_wage:,.2f} = R{gross_wage:,.2f}\n"
            f"Total deductions = R{paye:,.2f} + R{pension:,.2f} + R{medical:,.2f} + R{uif:,.2f} = R{total_deductions:,.2f}\n"
            f"Net wage = R{gross_wage:,.2f} - R{total_deductions:,.2f} = R{net_wage:,.2f}"
        ),
    ), "wage_journal_net_wage", basic_wage=basic_wage, overtime_wage=overtime_wage, paye=paye, pension=pension, medical=medical, uif=uif))

    pool.append(_with_validation(_make_calc(
        prompt=(
            f"For {emp} in the Wages Journal of {biz}, employer contributions are UIF R{employer_uif:,.2f}, pension fund R{employer_pension:,.2f}, "
            f"and medical aid R{employer_medical:,.2f}. Calculate the total employer contributions for the week."
        ),
        correct_answer=_round_money(employer_uif + employer_pension + employer_medical),
        working_formula=(
            f"Total employer contributions = R{employer_uif:,.2f} + R{employer_pension:,.2f} + R{employer_medical:,.2f} = R{_round_money(employer_uif + employer_pension + employer_medical):,.2f}"
        ),
    ), "wage_journal_employer_total", employer_uif=employer_uif, employer_pension=employer_pension, employer_medical=employer_medical))

    inferred_overtime_hours = int(r.choice([2, 4, 6, 8]))
    inferred_gross_wage = _round_money((normal_hours * normal_rate) + (inferred_overtime_hours * overtime_rate))
    pool.append(_with_validation(_make_calc(
        prompt=(
            f"The Wages Journal of {biz} shows a gross wage of R{inferred_gross_wage:,.2f} for {emp}. {emp} worked {normal_hours} normal hours at "
            f"R{normal_rate:,.2f} per hour and overtime is paid at R{overtime_rate:,.2f} per hour. How many overtime hours were worked to complete the journal?"
        ),
        correct_answer=float(inferred_overtime_hours),
        unit="",
        working_formula=(
            f"Basic wage = {normal_hours} × R{normal_rate:,.2f} = R{_round_money(normal_hours * normal_rate):,.2f}\n"
            f"Overtime pay = R{inferred_gross_wage:,.2f} - R{_round_money(normal_hours * normal_rate):,.2f} = R{_round_money(inferred_gross_wage - (normal_hours * normal_rate)):,.2f}\n"
            f"Overtime hours = R{_round_money(inferred_gross_wage - (normal_hours * normal_rate)):,.2f} ÷ R{overtime_rate:,.2f} = {inferred_overtime_hours}"
        ),
    ), "wage_journal_overtime_hours", gross_wage=inferred_gross_wage, basic_wage=_round_money(normal_hours * normal_rate), overtime_rate=overtime_rate, overtime_hours=inferred_overtime_hours))

    wage_journal_word_bank = [
        {"id": "wj0", "label": "Basic wage"},
        {"id": "wj1", "label": "Overtime"},
        {"id": "wj2", "label": "Gross wage"},
        {"id": "wj3", "label": "PAYE"},
        {"id": "wj4", "label": "UIF"},
        {"id": "wj5", "label": "Net wage"},
        {"id": "wj6", "label": "Medical aid"},
    ]
    wage_journal_label_to_id = {item["label"]: item["id"] for item in wage_journal_word_bank}
    wage_journal_rows = [
        ["1", "The employee's ordinary time remuneration before overtime is added.", ""],
        ["2", "Additional remuneration for hours worked above ordinary time.", ""],
        ["3", "Total wage before deductions.", ""],
        ["4", "The income tax deduction if applicable.", ""],
        ["5", "The statutory fund deduction contributed by both employer and employee.", ""],
        ["6", "The amount paid to the worker after deductions.", ""],
    ]
    wage_journal_correct_map = {
        "0": {"2": wage_journal_label_to_id["Basic wage"]},
        "1": {"2": wage_journal_label_to_id["Overtime"]},
        "2": {"2": wage_journal_label_to_id["Gross wage"]},
        "3": {"2": wage_journal_label_to_id["PAYE"]},
        "4": {"2": wage_journal_label_to_id["UIF"]},
        "5": {"2": wage_journal_label_to_id["Net wage"]},
    }
    pool.append(_with_validation(_make_table_wordbank(
        prompt="Match each Wages Journal description to the correct journal column heading from the word bank.",
        headers=["No.", "Wages Journal description", "Column heading"],
        rows=wage_journal_rows,
        word_bank=wage_journal_word_bank,
        correct_map=wage_journal_correct_map,
        guidelines=[
            "Separate amounts before deductions from deductions and the final amount paid.",
            "Gross wage is before deductions, while net wage is after deductions.",
        ],
    ), "journal_wordbank", expected_rows=len(wage_journal_rows)))

    return pool


def _gen_general_ledger(r: random.Random) -> List[Dict[str, Any]]:
    pool: List[Dict[str, Any]] = []
    pool.append(_make_general_ledger_fill_question(r=r, difficulty="easy"))
    pool.append(_make_general_ledger_fill_question(r=r, difficulty="medium"))
    pool.append(_make_general_ledger_fill_question(r=r, difficulty="hard"))
    word_bank = [
        {"id": "wb0", "label": "Creditors for salaries"},
        {"id": "wb1", "label": "Creditors for wages"},
        {"id": "wb2", "label": "SARS - PAYE"},
        {"id": "wb3", "label": "Pension fund"},
        {"id": "wb4", "label": "Pension fund contribution"},
        {"id": "wb5", "label": "Bank"},
        {"id": "wb6", "label": "Medical aid fund"},
        {"id": "wb7", "label": "Salaries"},
    ]
    label_to_id = {item["label"]: item["id"] for item in word_bank}
    rows = [
        ["1", "The net salary total from the Salaries Journal is posted to Salaries and ____.", ""],
        ["2", "Issued a cheque to settle PAYE: debit ____ ; credit Bank.", ""],
        ["3", "Employer pension contribution posted from the Salary Journal: debit ____ ; credit Pension fund.", ""],
        ["4", "Payment of net wages by cheque is posted as debit ____ ; credit Bank.", ""],
    ]
    correct_map = {
        "0": {"2": label_to_id["Creditors for salaries"]},
        "1": {"2": label_to_id["SARS - PAYE"]},
        "2": {"2": label_to_id["Pension fund contribution"]},
        "3": {"2": label_to_id["Creditors for wages"]},
    }
    pool.append(_with_validation(_make_table_wordbank(
        prompt="Match each General Ledger posting description to the missing account from the word bank.",
        headers=["No.", "Posting description", "Missing account"],
        rows=rows,
        word_bank=word_bank,
        correct_map=correct_map,
        guidelines=[
            "Think about the account that completes the double entry.",
            "Salary totals post to Salaries and Creditors for salaries, and settlement entries credit Bank.",
        ],
    ), "general_ledger_posting_wordbank", expected_rows=len(rows)))

    pool.append(_make_mcq(
        prompt="When the business pays net wages by cheque or EFT, which account is debited in the General Ledger?",
        options=[
            "Bank",
            "Creditors for wages",
            "Wages",
            "SARS - PAYE",
        ],
        correct_index=1,
        explanation="When net wages are paid, the business debits Creditors for wages to settle the liability and credits Bank.",
    ))

    paye_deduction = float(r.choice([1200, 1500, 1800, 2200]))
    pension_deduction = float(r.choice([750, 900, 1200, 1500]))
    net_salary = float(r.choice([9500, 11800, 13250, 15400]))
    pool.append(_with_validation(_make_typed(
        prompt=(
            f"The Salary Journal of {_pick_business(r)} shows PAYE of R{paye_deduction:,.2f}, pension deduction of R{pension_deduction:,.2f}, "
            f"and net salary of R{net_salary:,.2f}. Name the THREE accounts that will be credited when the journal is posted to the General Ledger."
        ),
        sample_answer=(
            "1. Credit SARS - PAYE for the PAYE deduction.\n"
            "2. Credit Pension fund for the pension deduction.\n"
            "3. Credit Creditors for salaries for the net salary owed to employees."
        ),
        grading_rubric=["SARS - PAYE", "Pension fund", "Creditors for salaries"],
    ), "general_ledger_credit_accounts_typed", minimum_parts=3))

    liability_account = r.choice(["Creditors for salaries", "Creditors for wages"])
    remuneration_label = "salaries" if liability_account == "Creditors for salaries" else "wages"
    settlement_amount = float(r.choice([8400, 9750, 11200, 14500]))
    pool.append(_with_validation(_make_typed(
        prompt=(
            f"A cheque is issued in the CPJ to pay net {remuneration_label} of R{settlement_amount:,.2f}. "
            f"State the TWO General Ledger accounts affected and explain which account is debited and which account is credited."
        ),
        sample_answer=(
            f"1. Debit {liability_account} because the liability for unpaid {remuneration_label} is being settled.\n"
            f"2. Credit Bank because cash leaves the business when the CPJ cheque is issued."
        ),
        grading_rubric=[liability_account, "Bank"],
    ), "general_ledger_cpj_settlement_typed", minimum_parts=2, liability_account=liability_account))

    return pool


def _validate_salaries_wages_question(*, question: Dict[str, Any], subskill: str) -> None:
    prompt = str(question.get("prompt") or "").strip()
    if not prompt:
        raise _SalariesWagesScenarioValidationError("Generated SWJ question is missing a prompt.")

    qt = str(question.get("question_type") or "").strip().lower()
    if qt == "typed" and not str(question.get("sample_answer") or "").strip():
        raise _SalariesWagesScenarioValidationError("Typed SWJ question is missing a sample answer.")

    if qt == "table_wordbank":
        rows = list(question.get("table", {}).get("rows") or [])
        correct_map = question.get("correct_map") if isinstance(question.get("correct_map"), dict) else {}
        token_ids = {str(item.get("id")) for item in list(question.get("word_bank") or []) if item.get("id") is not None}
        if not rows or not correct_map:
            raise _SalariesWagesScenarioValidationError("Table word-bank SWJ question is missing rows or a correct map.")
        for row_key, column_map in correct_map.items():
            row_index = int(row_key)
            if row_index < 0 or row_index >= len(rows):
                raise _SalariesWagesScenarioValidationError("Table word-bank SWJ question maps to an invalid row index.")
            if not isinstance(column_map, dict) or not column_map:
                raise _SalariesWagesScenarioValidationError("Table word-bank SWJ question has an invalid column mapping.")
            for token_id in column_map.values():
                if str(token_id) not in token_ids:
                    raise _SalariesWagesScenarioValidationError("Table word-bank SWJ question maps to a token that is not in the word bank.")

    if qt in ("journal", "ledger"):
        journals = list(question.get("journals") or []) if isinstance(question.get("journals"), list) else []
        if not journals and isinstance(question.get("journal"), dict):
            journals = [question.get("journal")]
        correct_map = question.get("correct_map") if isinstance(question.get("correct_map"), dict) else {}
        if not journals or not correct_map:
            raise _SalariesWagesScenarioValidationError("Journal/Ledger SWJ question is missing its table structure or correct_map.")
        seen_cell_ids = set()
        for journal in journals:
            rows = list(journal.get("rows") or []) if isinstance(journal, dict) else []
            if not rows:
                raise _SalariesWagesScenarioValidationError("Journal/Ledger SWJ question has a table with no rows.")
            for row in rows:
                for cell in list(row or []):
                    cell_id = str(cell.get("cell_id") or "").strip() if isinstance(cell, dict) else ""
                    if cell_id:
                        seen_cell_ids.add(cell_id)
        for key in correct_map.keys():
            if str(key) not in seen_cell_ids:
                raise _SalariesWagesScenarioValidationError("Journal/Ledger SWJ correct_map references a cell that is not present in the table.")

    answer_part_hints = list(question.get("answer_part_hints") or []) if isinstance(question.get("answer_part_hints"), list) else []
    if qt == "typed":
        prompt_lower = prompt.lower()
        minimum_parts = 1
        if " three " in f" {prompt_lower} ":
            minimum_parts = 3
        elif " two " in f" {prompt_lower} ":
            minimum_parts = 2
        if len(answer_part_hints) < minimum_parts:
            raise _SalariesWagesScenarioValidationError("Typed SWJ memo structure is too shallow for the prompt.")

    prompt_lower = prompt.lower()
    if subskill == "salary_scales":
        if "bonus of" in prompt_lower and "monthly salary is" not in prompt_lower and "salary scale is:" not in prompt_lower:
            raise _SalariesWagesScenarioValidationError("Bonus question is missing the salary basis in the prompt.")
        if "thirteenth cheque" in prompt_lower and "monthly salary is" not in prompt_lower and "salary scale is:" not in prompt_lower:
            raise _SalariesWagesScenarioValidationError("Thirteenth-cheque question is missing the salary basis in the prompt.")

    if subskill in ("gross_wage", "wages_calc", "wage_journal"):
        if "worked" in prompt_lower and "overtime" in prompt_lower and "per hour" not in prompt_lower and "rate" not in prompt_lower:
            raise _SalariesWagesScenarioValidationError("Wage question is missing rate information in the prompt.")

    if subskill == "general_ledger" and qt not in ("typed", "table_wordbank", "mcq", "ledger"):
        raise _SalariesWagesScenarioValidationError("General ledger SWJ question resolved to an unsupported question type.")

    validation = question.get("scenario_validation") if isinstance(question.get("scenario_validation"), dict) else None
    if validation:
        family = str(validation.get("family") or "").strip().lower()
        if family == "salary_scale_monthly_year1":
            expected = _round_money(float(validation.get("annual_salary", 0.0)) / 12)
            if not _money_matches(float(question.get("correct_answer") or 0.0), expected):
                raise _SalariesWagesScenarioValidationError("Salary scale monthly salary failed recomputation.")
        elif family == "salary_scale_initial_annual":
            expected = _round_money(float(validation.get("annual_salary", 0.0)))
            if not _money_matches(float(question.get("correct_answer") or 0.0), expected):
                raise _SalariesWagesScenarioValidationError("Salary scale initial annual salary failed recomputation.")
        elif family == "salary_scale_first_increment":
            expected = _round_money(float(validation.get("increment", 0.0)))
            if not _money_matches(float(question.get("correct_answer") or 0.0), expected):
                raise _SalariesWagesScenarioValidationError("Salary scale first increment failed recomputation.")
        elif family == "salary_scale_annual_year":
            expected = _round_money(float(validation.get("expected_annual", 0.0)))
            if not _money_matches(float(question.get("correct_answer") or 0.0), expected):
                raise _SalariesWagesScenarioValidationError("Salary scale annual salary failed recomputation.")
        elif family == "salary_scale_annual_from_monthly":
            expected = _round_money(float(validation.get("monthly_salary", 0.0)) * 12)
            if not _money_matches(float(question.get("correct_answer") or 0.0), expected):
                raise _SalariesWagesScenarioValidationError("Salary scale annual-from-monthly failed recomputation.")
        elif family == "salary_scale_annual_increase":
            expected = _round_money(float(validation.get("later_annual", 0.0)) - float(validation.get("earlier_annual", 0.0)))
            if not _money_matches(float(question.get("correct_answer") or 0.0), expected):
                raise _SalariesWagesScenarioValidationError("Salary scale increase failed recomputation.")
        elif family == "salary_scale_bonus_total":
            expected = _round_money(float(validation.get("monthly_salary", 0.0)) * (1 + (float(validation.get("bonus_pct", 0.0)) / 100)))
            if not _money_matches(float(question.get("correct_answer") or 0.0), expected):
                raise _SalariesWagesScenarioValidationError("Salary scale bonus total failed recomputation.")
        elif family == "salary_scale_thirteenth_cheque":
            expected = _round_money(float(validation.get("monthly_salary", 0.0)) * 2)
            if not _money_matches(float(question.get("correct_answer") or 0.0), expected):
                raise _SalariesWagesScenarioValidationError("Salary scale thirteenth cheque failed recomputation.")
        elif family == "gross_wage_total":
            expected = _round_money(
                float(validation.get("ordinary_hours", 0.0)) * float(validation.get("ordinary_rate", 0.0))
                + float(validation.get("overtime_hours", 0.0)) * float(validation.get("overtime_rate", 0.0))
            )
            if not _money_matches(float(question.get("correct_answer") or 0.0), expected):
                raise _SalariesWagesScenarioValidationError("Gross wage total failed recomputation.")
        elif family == "gross_wage_overtime_hours":
            overtime_pay = _round_money(float(validation.get("gross_wage", 0.0)) - float(validation.get("basic_wage", 0.0)))
            expected = overtime_pay / float(validation.get("overtime_rate", 1.0))
            if abs(float(question.get("correct_answer") or 0.0) - expected) > 0.01:
                raise _SalariesWagesScenarioValidationError("Gross wage overtime-hours inference failed recomputation.")
        elif family == "gross_wage_net_wage":
            expected = _round_money(
                float(validation.get("gross_wage", 0.0))
                - (
                    float(validation.get("paye", 0.0))
                    + float(validation.get("medical", 0.0))
                    + float(validation.get("uif", 0.0))
                )
            )
            if not _money_matches(float(question.get("correct_answer") or 0.0), expected):
                raise _SalariesWagesScenarioValidationError("Gross wage net wage failed recomputation.")
        elif family == "deductions_salary_advice_missing_paye":
            expected = _round_money(
                float(validation.get("gross_salary", 0.0))
                - (
                    float(validation.get("pension", 0.0))
                    + float(validation.get("medical", 0.0))
                    + float(validation.get("uif", 0.0))
                    + float(validation.get("net_salary", 0.0))
                )
            )
            if not _money_matches(float(question.get("correct_answer") or 0.0), expected):
                raise _SalariesWagesScenarioValidationError("Salary advice PAYE inference failed recomputation.")
        elif family == "salary_journal_net_salary":
            expected = _round_money(
                float(validation.get("basic_salary", 0.0))
                + float(validation.get("commission", 0.0))
                - (
                    float(validation.get("paye", 0.0))
                    + float(validation.get("pension", 0.0))
                    + float(validation.get("medical", 0.0))
                    + float(validation.get("uif", 0.0))
                )
            )
            if not _money_matches(float(question.get("correct_answer") or 0.0), expected):
                raise _SalariesWagesScenarioValidationError("Salary Journal net salary answer failed recomputation.")
        elif family == "salary_journal_pension_total":
            expected = _round_money(float(validation.get("pension", 0.0)) + float(validation.get("employer_pension", 0.0)))
            if not _money_matches(float(question.get("correct_answer") or 0.0), expected):
                raise _SalariesWagesScenarioValidationError("Salary Journal pension total failed recomputation.")
        elif family == "salary_journal_gross_salary":
            expected = _round_money(
                float(validation.get("basic_salary", 0.0))
                + float(validation.get("commission", 0.0))
                + float(validation.get("bonus", 0.0))
            )
            if not _money_matches(float(question.get("correct_answer") or 0.0), expected):
                raise _SalariesWagesScenarioValidationError("Salary Journal gross salary failed recomputation.")
        elif family == "wage_journal_net_wage":
            expected = _round_money(
                float(validation.get("basic_wage", 0.0))
                + float(validation.get("overtime_wage", 0.0))
                - (
                    float(validation.get("paye", 0.0))
                    + float(validation.get("pension", 0.0))
                    + float(validation.get("medical", 0.0))
                    + float(validation.get("uif", 0.0))
                )
            )
            if not _money_matches(float(question.get("correct_answer") or 0.0), expected):
                raise _SalariesWagesScenarioValidationError("Wages Journal net wage failed recomputation.")
        elif family == "wage_journal_employer_total":
            expected = _round_money(
                float(validation.get("employer_uif", 0.0))
                + float(validation.get("employer_pension", 0.0))
                + float(validation.get("employer_medical", 0.0))
            )
            if not _money_matches(float(question.get("correct_answer") or 0.0), expected):
                raise _SalariesWagesScenarioValidationError("Wages Journal employer total failed recomputation.")
        elif family == "wage_journal_overtime_hours":
            overtime_pay = _round_money(float(validation.get("gross_wage", 0.0)) - float(validation.get("basic_wage", 0.0)))
            expected = overtime_pay / float(validation.get("overtime_rate", 1.0))
            if abs(float(question.get("correct_answer") or 0.0) - expected) > 0.01:
                raise _SalariesWagesScenarioValidationError("Wages Journal overtime hours failed recomputation.")
        elif family == "deductions_net_salary":
            expected = _round_money(
                float(validation.get("gross_salary", 0.0))
                - (
                    float(validation.get("paye", 0.0))
                    + float(validation.get("pension", 0.0))
                    + float(validation.get("medical", 0.0))
                    + float(validation.get("uif", 0.0))
                )
            )
            if not _money_matches(float(question.get("correct_answer") or 0.0), expected):
                raise _SalariesWagesScenarioValidationError("Deductions net salary failed recomputation.")
        elif family in ("deductions_single_percentage", "employer_single_percentage"):
            expected = _round_money(float(validation.get("gross_amount", 0.0)) * float(validation.get("percentage", 0.0)) / 100)
            if validation.get("expected") is not None:
                expected = _round_money(float(validation.get("expected", 0.0)))
            if not _money_matches(float(question.get("correct_answer") or 0.0), expected):
                raise _SalariesWagesScenarioValidationError("Single-percentage SWJ calculation failed recomputation.")
        elif family == "employer_ratio_contribution":
            expected = _round_money(float(validation.get("employee_amount", 0.0)) * float(validation.get("ratio", 0.0)))
            if validation.get("expected") is not None:
                expected = _round_money(float(validation.get("expected", 0.0)))
            if not _money_matches(float(question.get("correct_answer") or 0.0), expected):
                raise _SalariesWagesScenarioValidationError("Employer ratio contribution failed recomputation.")
        elif family == "employer_cost_to_company":
            expected = _round_money(
                float(validation.get("gross_salary", 0.0))
                + float(validation.get("employer_uif", 0.0))
                + float(validation.get("employer_pension", 0.0))
                + float(validation.get("employer_medical", 0.0))
            )
            if not _money_matches(float(question.get("correct_answer") or 0.0), expected):
                raise _SalariesWagesScenarioValidationError("Employer cost-to-company failed recomputation.")
        elif family == "employer_amount_payable_sars":
            expected = _round_money(
                float(validation.get("employee_uif", 0.0))
                + float(validation.get("employer_uif", 0.0))
                + float(validation.get("sdl", 0.0))
            )
            if not _money_matches(float(question.get("correct_answer") or 0.0), expected):
                raise _SalariesWagesScenarioValidationError("Employer amount payable to SARS failed recomputation.")
        elif family in ("journal_wordbank", "general_ledger_posting_wordbank"):
            expected_rows = int(validation.get("expected_rows") or 0)
            row_count = len(list(question.get("table", {}).get("rows") or []))
            map_count = len(question.get("correct_map") or {}) if isinstance(question.get("correct_map"), dict) else 0
            if row_count != expected_rows or map_count != expected_rows:
                raise _SalariesWagesScenarioValidationError("Journal/Ledger word-bank rows do not match the expected validation count.")
        elif family == "general_ledger_credit_accounts_typed":
            minimum_parts = int(validation.get("minimum_parts") or 0)
            if len(answer_part_hints) < minimum_parts:
                raise _SalariesWagesScenarioValidationError("General Ledger typed memo does not contain the required number of answer parts.")
        elif family == "general_ledger_cpj_settlement_typed":
            minimum_parts = int(validation.get("minimum_parts") or 0)
            if len(answer_part_hints) < minimum_parts:
                raise _SalariesWagesScenarioValidationError("General Ledger CPJ settlement memo does not contain the required number of answer parts.")
        elif family in (
            "salary_journal_fill_in_easy",
            "salary_journal_fill_in_medium",
            "salary_journal_fill_in_hard",
            "wage_journal_fill_in_easy",
            "wage_journal_fill_in_medium",
            "wage_journal_fill_in_hard",
            "general_ledger_fill_in_easy",
            "general_ledger_fill_in_medium",
            "general_ledger_fill_in_hard",
        ):
            expected_cells = int(validation.get("expected_cells") or 0)
            actual_cells = len(question.get("correct_map") or {}) if isinstance(question.get("correct_map"), dict) else 0
            if expected_cells <= 0 or actual_cells != expected_cells:
                raise _SalariesWagesScenarioValidationError("SWJ journal/ledger fill question does not match its expected editable-cell count.")


# ---------------------------------------------------------------------------
# Main entry point
# ---------------------------------------------------------------------------

def generate_questions(
    *,
    subskill: str = "mixed",
    difficulty: str = "easy",
    question_type: str = "mixed",
    count: int = 1,
    seed: Optional[int] = None,
    mode: str = "",
) -> List[Dict[str, Any]]:
    r = _rng(seed)

    def _prompt_signature(question: Dict[str, Any]) -> str:
        prompt = str(question.get("prompt") or "").strip().lower()
        return " ".join(prompt.split())

    n = max(1, min(int(count), 20))
    difficulty_norm = str(difficulty or "easy").strip().lower() or "easy"
    subskill_norm = str(subskill or "mixed").strip().lower()
    subskill_aliases = {
        "wages_calc": "gross_wage",
    }
    resolved_subskill = subskill_aliases.get(subskill_norm, subskill_norm)

    # Build pools
    salary_scale_pool = _gen_salary_scale(r)
    gross_wage_pool = _gen_gross_wage(r)
    deductions_pool = _gen_deductions(r)
    employer_pool = _gen_employer_contributions(r)
    ethics_pool = _gen_ethics(r)
    glossary_pool = _gen_glossary_matching(r)
    salary_journal_pool = _gen_salary_journal(r)
    wage_journal_pool = _gen_wage_journal(r)
    general_ledger_pool = _gen_general_ledger(r)

    all_pools = {
        "salary_scales": salary_scale_pool,
        "gross_wage": gross_wage_pool,
        "wages_calc": gross_wage_pool,
        "deductions": deductions_pool,
        "employer_contributions": employer_pool,
        "salary_journal": salary_journal_pool,
        "wage_journal": wage_journal_pool,
        "general_ledger": general_ledger_pool,
        "ethics": ethics_pool,
        "glossary": glossary_pool,
        "mixed": salary_scale_pool + gross_wage_pool + deductions_pool + employer_pool + salary_journal_pool + wage_journal_pool + general_ledger_pool + ethics_pool + glossary_pool,
    }

    pool = all_pools.get(resolved_subskill, all_pools["mixed"])
    filtered_pool = [q for q in pool if _difficulty_matches(q, difficulty_norm)]
    if filtered_pool:
        pool = filtered_pool
    if resolved_subskill in ("salary_journal", "wage_journal"):
        journal_only_pool = [q for q in pool if str(q.get("question_type") or "").strip().lower() == "journal"]
        if journal_only_pool:
            pool = journal_only_pool
    if resolved_subskill == "general_ledger":
        ledger_only_pool = [q for q in pool if str(q.get("question_type") or "").strip().lower() == "ledger"]
        if ledger_only_pool:
            pool = ledger_only_pool
    if not pool:
        pool = all_pools["mixed"]

    out: List[Dict[str, Any]] = []
    used_signatures = set()
    for _ in range(n):
        selected: Optional[Dict[str, Any]] = None
        fallback_selected: Optional[Dict[str, Any]] = None
        for _attempt in range(18):
            try:
                q = r.choice(pool)
                q_copy = dict(q)
                q_copy["difficulty"] = difficulty_norm
                q_copy["subskill"] = subskill
                _validate_salaries_wages_question(question=q_copy, subskill=resolved_subskill)
                q_copy.pop("recommended_difficulties", None)
                signature = _prompt_signature(q_copy)
                if signature in used_signatures:
                    if fallback_selected is None:
                        fallback_selected = q_copy
                    continue
                selected = q_copy
                used_signatures.add(signature)
                break
            except _SalariesWagesScenarioValidationError:
                continue
        if selected is None and fallback_selected is not None:
            selected = fallback_selected
            used_signatures.add(_prompt_signature(fallback_selected))
        if selected is None:
            raise _SalariesWagesScenarioValidationError(f"Could not generate a valid SWJ question for subskill '{resolved_subskill}'.")
        out.append(selected)

    return out
