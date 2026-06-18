from __future__ import annotations

import random
from typing import Any, Dict, List, Optional, Tuple

from ..grade10_accounting.scenario_builder import build_scenario
from ..sole_trader.core import fmt_money as _fmt_money
from ..sole_trader.core import make_id as _make_id
from ..sole_trader.core import round_money as _round_money
from ..sole_trader.journal_question import make_journal as _make_journal
from ..sole_trader.journal_table import build_prefixed_row as _build_prefixed_row
from ..sole_trader.journal_table import journal_editable_cols_by_difficulty as _journal_editable_cols_by_difficulty


def _rng(seed: Optional[int]) -> random.Random:
    r = random.Random()
    if seed is None:
        r.seed()
    else:
        r.seed(int(seed))
    return r


def _money(x: float) -> str:
    return _fmt_money(float(x))


def _make_calc(*, prompt: str, correct_value: float, unit: str = "", explanation: str = "", working_formula: str = "", mode: str = "", archetype_key: str = "") -> Dict[str, Any]:
    out: Dict[str, Any] = {
        "id": _make_id("acct11_partnership_balance_sheet_calc"),
        "question_type": "calc",
        "prompt": prompt,
        "correct_value": float(_round_money(correct_value)),
        "unit": unit,
        "working_formula": working_formula,
        "expected_answer_type": "number",
        "guidelines": [f"Formula: {working_formula}"] if working_formula else [],
    }
    if archetype_key:
        out["meta"] = {"archetype_key": archetype_key}
    if str(mode or "").strip().lower() == "scaffold" and str(explanation).strip():
        out["explanation"] = explanation
    return out


def _mk_journal(
    *,
    prompt: str,
    journal_type: str,
    headers: List[str],
    values_rows: List[List[Optional[str]]],
    difficulty: str,
    mode: str,
    base_editable_cols: List[int],
    title_fields: Optional[List[Dict[str, Any]]] = None,
    cell_hints: Optional[Dict[str, str]] = None,
    archetype_key: str = "",
    rubric_map: Optional[Dict[str, Dict[str, Any]]] = None,
    dependency_map: Optional[Dict[str, List[str]]] = None,
) -> Dict[str, Any]:
    diff = str(difficulty or "easy").strip().lower()
    mode_norm = str(mode or "").strip().lower()
    show_answers = mode_norm == "scaffold"

    editable_cols = _journal_editable_cols_by_difficulty(
        difficulty=diff,
        base_editable_cols=base_editable_cols,
        total_cols=len(headers),
        mode=mode_norm,
    )

    rows: List[List[Dict[str, Any]]] = []
    correct_map: Dict[str, Any] = {}

    for rix, vals in enumerate(values_rows):
        editable_set = set(int(c) for c in editable_cols)
        display = [
            ("" if int(cix) in editable_set else ("" if v0 is None else str(v0)))
            for cix, v0 in enumerate(vals)
        ]
        rows.append(_build_prefixed_row(table_index=0, row_index=rix, values=display, editable_cols=editable_cols))
        for cix, v0 in enumerate(vals):
            correct_map[f"t0_r{int(rix)}_c{int(cix)}"] = "" if v0 is None else str(v0)

    out = _make_journal(
        prompt=prompt,
        journal_type=journal_type,
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        guidelines=[
            "Use the correct layout and row labels.",
            "Enter amounts without a currency symbol.",
        ],
        table_variant="grade_project",
        title_fields=title_fields,
        cell_hints=cell_hints if mode_norm == "scaffold" and cell_hints else None,
        rubric_map=rubric_map,
        dependency_map=dependency_map,
    )
    out["id"] = _make_id("acct11_partnership_balance_sheet")
    if archetype_key:
        out["meta"] = {"archetype_key": archetype_key}
    return out


def _make_bundle(*, prompt: str, parts: List[Dict[str, Any]], archetype_key: str = "") -> Dict[str, Any]:
    out: Dict[str, Any] = {
        "id": _make_id("acct11_partnership_balance_sheet_bundle"),
        "question_type": "bundle",
        "prompt": prompt,
        "parts": parts,
    }
    if archetype_key:
        out["meta"] = {"archetype_key": archetype_key}
    return out


def _make_current_accounts_note(
    *,
    r: random.Random,
    difficulty: str,
    mode: str,
    business: Optional[str] = None,
    year: Optional[int] = None,
    partners: Optional[Tuple[str, str]] = None,
    net_profit: Optional[float] = None,
) -> Dict[str, Any]:
    scenario = build_scenario(seed=year)
    business = business or scenario["business"]
    if partners:
        partner_a, partner_b = partners
    else:
        # Use owner from scenario and a random partner
        partner_a = scenario["owner"].split(" ")[-1]  # Get surname
        partner_b = r.sample(["Butler", "Johnson", "Baloyi", "Shabangu"], k=1)[0]
    year = int(year if year is not None else r.choice([20, 21, 22, 23, 24]))

    # Generate pre-adjustment data (the "INFORMATION")
    capital_a = float(r.choice([200000, 500000, 400000]))
    capital_b = float(r.choice([100000, 500000, 300000]))
    
    opening_a = float(r.choice([-8400, -1200, 5000, 16000, 24500]))
    opening_b = float(r.choice([-6700, 1200, 21800, 32000]))
    
    net_profit = float(net_profit if net_profit is not None else r.choice([376000, 384750, 420000]))
    
    interest_rate = float(r.choice([0.06, 0.10, 0.15]))
    interest_total = _round_money((capital_a + capital_b) * interest_rate)
    
    salary_a_monthly = float(r.choice([6700, 8000, 5000]))
    salary_b_monthly = float(r.choice([8500, 8000, 6000]))
    salaries_total = _round_money((salary_a_monthly + salary_b_monthly) * 12)
    
    drawings_a = float(r.choice([91000, 98000, 120000, 143000]))
    drawings_b = float(r.choice([90000, 91000, 144000, 150000]))
    
    # Calculate correct answers
    profit_a = _round_money(net_profit / 2.0)
    profit_b = _round_money(net_profit / 2.0)
    interest_a = _round_money(capital_a * interest_rate)
    interest_b = _round_money(capital_b * interest_rate)
    salary_a = _round_money(salary_a_monthly * 12)
    salary_b = _round_money(salary_b_monthly * 12)
    primary_a = _round_money(interest_a + salary_a)
    primary_b = _round_money(interest_b + salary_b)
    final_a = _round_money(profit_a - primary_a)
    final_b = _round_money(profit_b - primary_b)
    closing_a = _round_money(opening_a + profit_a - drawings_a)
    closing_b = _round_money(opening_b + profit_b - drawings_b)
    
    total_opening = _round_money(opening_a + opening_b)
    total_profit = _round_money(profit_a + profit_b)
    total_interest = _round_money(interest_a + interest_b)
    total_salaries = _round_money(salary_a + salary_b)
    total_primary = _round_money(primary_a + primary_b)
    total_final = _round_money(final_a + final_b)
    total_drawings = _round_money(-(drawings_a + drawings_b))
    total_closing = _round_money(closing_a + closing_b)

    headers = ["Current accounts", partner_a, partner_b, "Total"]
    
    # Define the correct answers for validation
    correct_values = [
        ["Balance at the beginning of the year", opening_a, opening_b, total_opening],
        ["Profit per the income statement", profit_a, profit_b, total_profit],
        ["Interest on capital", interest_a, interest_b, total_interest],
        ["Salaries", salary_a, salary_b, total_salaries],
        ["Primary division of profits", primary_a, primary_b, total_primary],
        ["Final division", final_a, final_b, total_final],
        ["Drawings during the year", -drawings_a, -drawings_b, total_drawings],
        ["Balance at the end of year", closing_a, closing_b, total_closing],
    ]
    
    # Build correct_map for validation
    correct_map: Dict[str, Any] = {}
    for row_idx, row in enumerate(correct_values):
        for col_idx in range(1, 4):  # columns 1, 2, 3 (partner_a, partner_b, Total)
            val = row[col_idx]
            correct_map[f"t0_r{row_idx}_c{col_idx}"] = _money(val)
    
    mode_norm = str(mode or "").strip().lower()

    # values_rows must always contain the correct answers. _mk_journal will blank
    # learner-input cells for practice mode based on editable cols.
    rows: List[List[Optional[str]]] = []
    for row in correct_values:
        rows.append([row[0], _money(row[1]), _money(row[2]), _money(row[3])])

    # Cell hints for scaffold mode
    cell_hints: Dict[str, str] = {}
    if mode_norm == "scaffold":
        cell_hints["t0_r0_c1"] = f"Opening balance for {partner_a}: may be debit (negative) or credit (positive)"
        cell_hints["t0_r0_c2"] = f"Opening balance for {partner_b}: may be debit (negative) or credit (positive)"
        cell_hints["t0_r2_c1"] = f"Interest = Capital × {int(interest_rate*100)}% = {capital_a} × {interest_rate}"
        cell_hints["t0_r2_c2"] = f"Interest = Capital × {int(interest_rate*100)}% = {capital_b} × {interest_rate}"
        cell_hints["t0_r3_c1"] = f"Salary = Monthly × 12 = {salary_a_monthly} × 12"
        cell_hints["t0_r3_c2"] = f"Salary = Monthly × 12 = {salary_b_monthly} × 12"
        cell_hints["t0_r4_c1"] = "Primary = Interest + Salary"
        cell_hints["t0_r4_c2"] = "Primary = Interest + Salary"
        cell_hints["t0_r5_c1"] = "Final = Profit share - Primary"
        cell_hints["t0_r5_c2"] = "Final = Profit share - Primary"
        cell_hints["t0_r6_c1"] = f"Drawings reduce current account (show as negative): -{drawings_a}"
        cell_hints["t0_r6_c2"] = f"Drawings reduce current account (show as negative): -{drawings_b}"
        cell_hints["t0_r7_c1"] = f"Closing = Opening + Profit - Drawings = {opening_a} + {profit_a} - {drawings_a}"
        cell_hints["t0_r7_c2"] = f"Closing = Opening + Profit - Drawings = {opening_b} + {profit_b} - {drawings_b}"

    # Build proper prompt with REQUIRED and INFORMATION sections
    prompt = f"""{business}

#### REQUIRED:
Prepare the Current Accounts note for the year ended 31 December 20{year}.

#### INFORMATION:

A. Balances on 31 December 20{year}:
Capital: {partner_a}, R{capital_a:,.0f}
Capital: {partner_b}, R{capital_b:,.0f}
Current account: {partner_a} (1 Jan 20{year}), R{opening_a:,.0f}
Current account: {partner_b} (1 Jan 20{year}), R{opening_b:,.0f}
Net profit as per Income Statement, R{net_profit:,.0f}

B. Partnership agreement:
- Interest on capital: {int(interest_rate*100)}% per annum on capital balances
- Partners' salaries:
  * {partner_a}: R{salary_a_monthly:,.0f} per month
  * {partner_b}: R{salary_b_monthly:,.0f} per month
- Remaining profits shared equally

C. Drawings for the year:
- {partner_a}: R{drawings_a:,.0f}
- {partner_b}: R{drawings_b:,.0f}"""

    return _mk_journal(
        prompt=prompt,
        journal_type="partnership_notes_current_accounts",
        headers=headers,
        values_rows=rows,
        difficulty=difficulty,
        mode=mode,
        base_editable_cols=[1, 2, 3],
        title_fields=[
            {"label": "Notes to the financial statements", "value": ""},
            {"label": "Current accounts", "value": ""},
            {"label": f"Year ended 31 December 20{year}", "value": ""},
        ],
        cell_hints=cell_hints,
        archetype_key="g11_partnership_balance_sheet_current_accounts_note",
    )


def _make_trade_and_other_payables_note(
    *,
    r: random.Random,
    difficulty: str,
    mode: str,
    business: Optional[str] = None,
    year: Optional[int] = None,
) -> Dict[str, Any]:
    scenario = build_scenario(seed=year)
    business = business or scenario["business"]
    year = int(year if year is not None else r.choice([20, 21, 22, 23, 24]))
    
    # Generate pre-adjustment data
    creditors_control = float(r.choice([200000, 240700, 180000]))
    accrued_expenses = float(r.choice([8000, 12500, 10000]))
    income_in_advance = float(r.choice([5000, 7200, 8000]))
    
    # Salary-related payables
    gross_salary = float(r.choice([48000, 52000, 45000]))
    paye = _round_money(gross_salary * 0.15)
    pension = float(r.choice([1700, 2000, 1800]))
    medical_employee = float(r.choice([2000, 2300, 2200]))
    medical_employer = _round_money(medical_employee * 2)
    uif_employee = _round_money(gross_salary * 0.01)
    uif_employer = uif_employee
    net_salary = _round_money(gross_salary - paye - pension - medical_employee - uif_employee)
    
    # Calculate correct answers
    creditors_for_salaries = net_salary
    sars_payable = paye
    pension_fund = pension
    medical_aid = _round_money(medical_employee + medical_employer)
    uif_total = _round_money(uif_employee + uif_employer)
    
    total = _round_money(creditors_control + accrued_expenses + income_in_advance + 
                         creditors_for_salaries + sars_payable + pension_fund + medical_aid + uif_total)
    
    headers = ["Trade and other payables", "Amount"]
    
    # Define correct values
    correct_values = [
        ["Creditors control", creditors_control],
        ["Accrued expenses", accrued_expenses],
        ["Income received in advance", income_in_advance],
        ["Creditors for salaries", creditors_for_salaries],
        ["SARS (PAYE)", sars_payable],
        ["Pension fund", pension_fund],
        ["Medical aid", medical_aid],
        ["UIF", uif_total],
        ["Total", total],
    ]
    
    # Build correct_map
    correct_map: Dict[str, Any] = {}
    for row_idx, row in enumerate(correct_values):
        correct_map[f"t0_r{row_idx}_c1"] = _money(row[1])
    
    mode_norm = str(mode or "").strip().lower()

    # values_rows must always contain the correct answers.
    rows: List[List[Optional[str]]] = []
    for row in correct_values:
        rows.append([row[0], _money(row[1])])

    # Cell hints
    cell_hints: Dict[str, str] = {}
    if mode_norm == "scaffold":
        cell_hints["t0_r0_c1"] = f"Creditors control: {creditors_control}"
        cell_hints["t0_r3_c1"] = f"Creditors for salaries = Net salary = {gross_salary} - {paye} - {pension} - {medical_employee} - {uif_employee}"
        cell_hints["t0_r4_c1"] = f"SARS PAYE: {paye}"
        cell_hints["t0_r6_c1"] = f"Medical aid = Employee ({medical_employee}) + Employer ({medical_employer}) = {medical_aid}"
        cell_hints["t0_r7_c1"] = f"UIF = Employee ({uif_employee}) + Employer ({uif_employer}) = {uif_total}"
    
    prompt = f"""{business}

#### REQUIRED:
Prepare the Trade and Other Payables note for the year ended 31 December 20{year}.

#### INFORMATION:

A. Balances on 31 December 20{year}:
Creditors control, R{creditors_control:,.0f}
Accrued expenses, R{accrued_expenses:,.0f}
Income received in advance, R{income_in_advance:,.0f}

B. Unprocessed Salaries Journal for December 20{year}:
Gross salary, R{gross_salary:,.0f}
PAYE deduction, R{paye:,.0f}
Pension fund deduction, R{pension:,.0f}
Medical aid deduction, R{medical_employee:,.0f}
UIF deduction, R{uif_employee:,.0f}
Net salary, R{net_salary:,.0f}

C. Employer contributions:
- Medical aid: R2 for every R1 contributed by employee
- UIF: 1% of gross salary (matching employee contribution)
- No contribution to pension fund"""

    return _mk_journal(
        prompt=prompt,
        journal_type="partnership_notes_trade_payables",
        headers=headers,
        values_rows=rows,
        difficulty=difficulty,
        mode=mode,
        base_editable_cols=[1],
        title_fields=[
            {"label": "Notes to the financial statements", "value": ""},
            {"label": "Trade and other payables", "value": ""},
            {"label": f"Year ended 31 December 20{year}", "value": ""},
        ],
        cell_hints=cell_hints,
        archetype_key="g11_partnership_balance_sheet_trade_payables_note",
    )


def _make_trade_and_other_payables_note_excluding_overdraft_and_current_loan(
    *,
    r: random.Random,
    difficulty: str,
    mode: str,
    business: Optional[str] = None,
    year: Optional[int] = None,
) -> Dict[str, Any]:
    scenario = build_scenario(seed=year)
    business = business or scenario["business"]
    year = int(year if year is not None else r.choice([21, 22, 23]))

    creditors_control = float(r.choice([24070, 57690, 83000, 763860]))
    accrued_expenses = float(r.choice([1130, 11430, 32700]))
    income_in_advance = float(r.choice([700, 4140, 13650]))

    # Employee omitted / not posted totals
    gross_salary = float(r.choice([10800, 48000, 52000]))
    paye = float(r.choice([3420, 6000, 1080]))
    uif_employee = float(r.choice([108, 480]))
    uif_employer = uif_employee

    pension_employee = float(r.choice([500, 1296, 1700]))
    # Employer contributes R1.50 for each R1 (use 2/3 factor if employee is 1.5× employer; keep simple)
    pension_employer = _round_money(pension_employee * (1.0 / 1.5))

    net_salary = _round_money(gross_salary - paye - uif_employee - pension_employee)

    creditors_for_salaries = net_salary
    uif_total = _round_money(uif_employee + uif_employer)
    pension_total = _round_money(pension_employee + pension_employer)

    total = _round_money(
        creditors_control + accrued_expenses + income_in_advance + creditors_for_salaries + paye + uif_total + pension_total
    )

    headers = ["Trade and other payables", "Amount"]
    correct_values = [
        ["Trade creditors", creditors_control],
        ["SARS: PAYE", paye],
        [">Accrued expenses", accrued_expenses],
        [">Income received in advance", income_in_advance],
        [">UIF", uif_total],
        [">Pension fund", pension_total],
        [">Creditors for salaries", creditors_for_salaries],
        [">Total", total],
    ]

    rows: List[List[Optional[str]]] = []
    for row in correct_values:
        rows.append([row[0], _money(row[1])])

    cell_hints: Dict[str, str] = {}
    if str(mode or "").strip().lower() == "scaffold":
        cell_hints["t0_r1_c1"] = f"PAYE payable from omitted salaries info: {paye:,.0f}"
        cell_hints["t0_r4_c1"] = f"UIF = employee + employer = {uif_employee:,.0f} + {uif_employer:,.0f}"
        cell_hints["t0_r5_c1"] = f"Pension fund = employee + employer = {pension_employee:,.0f} + {pension_employer:,.0f}"
        cell_hints["t0_r6_c1"] = f"Creditors for salaries = net salary = {gross_salary:,.0f} - {paye:,.0f} - {uif_employee:,.0f} - {pension_employee:,.0f}"

    prompt = f"""{business}

#### REQUIRED:
Prepare the Trade and other payables note for the year ended 28 February 20{year}.

Note: Show all short-term liabilities except Bank overdraft and Current portion of loan in this note.

#### INFORMATION:
A. Balances in the ledger on 28 February 20{year}:
- Creditors control / trade creditors, R{creditors_control:,.0f}
- Accrued expenses, R{accrued_expenses:,.0f}
- Income received in advance, R{income_in_advance:,.0f}

B. Omitted employee from Salaries Journal:
- Gross salary, R{gross_salary:,.0f}
- PAYE, R{paye:,.0f}
- UIF (employee), R{uif_employee:,.0f} (employer matches)
- Pension fund (employee), R{pension_employee:,.0f} (employer contributes R1.50 for each R1 contributed by employee)"""

    return _mk_journal(
        prompt=prompt,
        journal_type="partnership_notes_trade_payables_excluding_overdraft_current_loan",
        headers=headers,
        values_rows=rows,
        difficulty=difficulty,
        mode=mode,
        base_editable_cols=[1],
        title_fields=[
            {"label": "Notes to the financial statements", "value": ""},
            {"label": "Trade and other payables", "value": ""},
            {"label": f"Year ended 28 February 20{year}", "value": ""},
        ],
        cell_hints=cell_hints,
        archetype_key="g11_partnership_balance_sheet_trade_payables_note_excl_overdraft_current_loan",
    )


def _make_trade_and_other_receivables_note(
    *,
    r: random.Random,
    difficulty: str,
    mode: str,
    business: Optional[str] = None,
    year: Optional[int] = None,
) -> Dict[str, Any]:
    scenario = build_scenario(seed=year)
    business = business or scenario["business"]
    year = int(year if year is not None else r.choice([20, 21, 22, 23, 24]))
    
    # Generate pre-adjustment data
    debtors_control = float(r.choice([73500, 124490, 98000, 150000]))
    provision_existing = float(r.choice([2000, 2900, 3700]))
    
    # Adjustments
    dishonoured_cheque = float(r.choice([270, 300, 0]))
    correction_error = float(r.choice([30, 0]))
    provision_new = float(r.choice([3000, 3700, 5000]))
    
    accrued_income = float(r.choice([3800, 4500, 0]))
    prepaid_expenses = float(r.choice([2340, 1200, 0]))
    
    # Calculate correct answers
    trade_debtors = _round_money(debtors_control + dishonoured_cheque + correction_error)
    provision_adjustment = provision_new - provision_existing
    net_trade_debtors = _round_money(trade_debtors - provision_new)
    total = _round_money(net_trade_debtors + accrued_income + prepaid_expenses)
    
    headers = ["Trade and other receivables", "Amount"]
    
    # Define correct answers for validation
    correct_values = [
        ["Net trade debtors", net_trade_debtors],
        ["Trade debtors", trade_debtors],
        ["Provision for bad debts", -provision_new],
    ]
    if accrued_income > 0:
        correct_values.append(["Accrued income", accrued_income])
    if prepaid_expenses > 0:
        correct_values.append(["Prepaid expenses", prepaid_expenses])
    correct_values.append(["Total", total])
    
    # Build correct_map
    correct_map: Dict[str, Any] = {}
    for row_idx, row in enumerate(correct_values):
        correct_map[f"t0_r{row_idx}_c1"] = _money(row[1])
    
    mode_norm = str(mode or "").strip().lower()

    # values_rows must always contain the correct answers.
    rows: List[List[Optional[str]]] = []
    for row in correct_values:
        rows.append([row[0], _money(row[1])])

    # Cell hints
    cell_hints: Dict[str, str] = {}
    if mode_norm == "scaffold":
        cell_hints["t0_r0_c1"] = f"Net trade debtors = Trade debtors - Provision = {trade_debtors} - {provision_new}"
        cell_hints["t0_r1_c1"] = f"Trade debtors = Debtors control + Dishonoured cheque + Correction = {debtors_control} + {dishonoured_cheque} + {correction_error}"
        cell_hints["t0_r2_c1"] = f"Provision for bad debts (show as negative): -{provision_new}"
        if accrued_income > 0:
            cell_hints["t0_r3_c1"] = f"Accrued income: {accrued_income}"
        if prepaid_expenses > 0:
            idx = 3 if accrued_income == 0 else 4
            cell_hints[f"t0_r{idx}_c1"] = f"Prepaid expenses: {prepaid_expenses}"
    
    # Build adjustments text
    adjustments_text = ""
    if dishonoured_cheque > 0:
        adjustments_text += f"\n- A dishonoured cheque of R{dishonoured_cheque:,.0f} was received from a debtor"
    if correction_error > 0:
        adjustments_text += f"\n- A correction of R{correction_error:,.0f} must be processed"
    if provision_new != provision_existing:
        adjustments_text += f"\n- Provision for bad debts must be adjusted to R{provision_new:,.0f} (currently R{provision_existing:,.0f})"
    
    prompt = f"""{business}

#### REQUIRED:
Prepare the Trade and Other Receivables note for the year ended 31 December 20{year}.

#### INFORMATION:

A. Balances on 31 December 20{year}:
Debtors control, R{debtors_control:,.0f}
Provision for bad debts (current), R{provision_existing:,.0f}"""
    
    if accrued_income > 0:
        prompt += f"\nAccrued income, R{accrued_income:,.0f}"
    if prepaid_expenses > 0:
        prompt += f"\nPrepaid expenses, R{prepaid_expenses:,.0f}"
    
    if not adjustments_text:
        adjustments_text = "\n- No additional adjustments required"

    prompt += f"""

B. Additional information and adjustments:{adjustments_text}"""

    return _mk_journal(
        prompt=prompt,
        journal_type="partnership_notes_trade_receivables",
        headers=headers,
        values_rows=rows,
        difficulty=difficulty,
        mode=mode,
        base_editable_cols=[1],
        title_fields=[
            {"label": "Notes to the financial statements", "value": ""},
            {"label": "Trade and other receivables", "value": ""},
            {"label": f"Year ended 31 December 20{year}", "value": ""},
        ],
        cell_hints=cell_hints,
        archetype_key="g11_partnership_balance_sheet_trade_receivables_note",
    )


def _make_capital_note(
    *,
    r: random.Random,
    difficulty: str,
    mode: str,
    business: Optional[str] = None,
    year: Optional[int] = None,
    partners: Optional[Tuple[str, str]] = None,
) -> Dict[str, Any]:
    scenario = build_scenario(seed=year)
    business = business or scenario["business"]
    if partners:
        partner_a, partner_b = partners
    else:
        partner_a = scenario["owner"].split(" ")[-1]
        partner_b = r.sample(["Mac", "Adam", "Marvel", "Lane", "Jack", "Mazwi"], k=1)[0]
    year = int(year if year is not None else r.choice([21, 22, 23]))

    open_a = float(r.choice([100000, 200000, 315000, 360000]))
    open_b = float(r.choice([80000, 100000, 270000, 405000, 760000]))

    # Capital changes (could be blank for one partner, like the doc archetypes)
    add_a = float(r.choice([0, 40000, 100000, 175000, 225000]))
    add_b = float(r.choice([0, 0, 0, 100000]))
    with_a = float(r.choice([0, 0, 45000, 135000]))
    with_b = float(r.choice([0, 0, 20000, 45000, 135000]))

    close_a = _round_money(open_a + add_a - with_a)
    close_b = _round_money(open_b + add_b - with_b)

    headers = ["Capital", partner_a, partner_b]
    mode_norm = str(mode or "").strip().lower()

    # values_rows must always contain the correct answers.
    rows: List[List[Optional[str]]] = [
        ["Balance at the beginning of the year", _money(open_a), _money(open_b)],
        ["Additional capital contributed", _money(add_a), _money(add_b)],
        ["Withdrawal of capital", _money(-with_a), _money(-with_b)],
        ["Balance at the end of the year", _money(close_a), _money(close_b)],
    ]

    cell_hints: Dict[str, str] = {}
    if mode_norm == "scaffold":
        cell_hints["t0_r3_c1"] = f"Closing = Opening + Additions - Withdrawals = {open_a:,.0f} + {add_a:,.0f} - {with_a:,.0f}"
        cell_hints["t0_r3_c2"] = f"Closing = Opening + Additions - Withdrawals = {open_b:,.0f} + {add_b:,.0f} - {with_b:,.0f}"

    prompt = f"""{business}

#### REQUIRED:
Prepare the Capital note as it would appear in the notes to the financial statements for the year ended 28 February 20{year}.

#### INFORMATION:
A. Capital balances at beginning of year:
- Capital: {partner_a}, R{open_a:,.0f}
- Capital: {partner_b}, R{open_b:,.0f}

B. Capital changes during the year:
- Additional capital contributed: {partner_a} R{add_a:,.0f}; {partner_b} R{add_b:,.0f}
- Withdrawal of capital: {partner_a} R{with_a:,.0f}; {partner_b} R{with_b:,.0f}"""

    return _mk_journal(
        prompt=prompt,
        journal_type="partnership_notes_capital",
        headers=headers,
        values_rows=rows,
        difficulty=difficulty,
        mode=mode,
        base_editable_cols=[1, 2],
        title_fields=[
            {"label": "Notes to the financial statements", "value": ""},
            {"label": "Capital", "value": ""},
            {"label": f"Year ended 28 February 20{year}", "value": ""},
        ],
        cell_hints=cell_hints,
        archetype_key="g11_partnership_balance_sheet_capital_note",
    )


def _make_equity_and_liabilities_section_debt_equity(
    *,
    r: random.Random,
    difficulty: str,
    mode: str,
) -> Dict[str, Any]:
    scenario = build_scenario(seed=r.randint(1, 1000))
    business = scenario["business"]
    year = int(r.choice([21, 22, 23]))

    # Owners' equity (given / derived from capital + current accounts)
    capital_total = float(r.choice([280000, 600000, 1000000]))
    current_accounts_total = float(r.choice([89740, 129100, 200400, 174060]))
    owners_equity = _round_money(capital_total + current_accounts_total)

    # Debt:Equity ratio drives the loan figure
    debt_equity = float(r.choice([0.4, 0.5]))
    loan_total = _round_money(owners_equity * debt_equity)

    short_term_loan = float(r.choice([15000, 20000, 55000, 97200]))
    if short_term_loan >= loan_total:
        short_term_loan = _round_money(loan_total * 0.3)
    non_current_loan = _round_money(loan_total - short_term_loan)

    trade_payables = float(r.choice([45050, 55550, 96399, 106930]))
    bank_overdraft = float(r.choice([11940, 5250, 31250, 59940]))
    current_liabilities = _round_money(trade_payables + bank_overdraft + short_term_loan)

    total_equity_liabilities = _round_money(owners_equity + non_current_loan + current_liabilities)

    headers = ["Equity and liabilities", "Note", "Amount"]
    mode_norm = str(mode or "").strip().lower()

    # values_rows must always contain the correct answers.
    rows: List[List[Optional[str]]] = [
        ["EQUITY AND LIABILITIES", "", ""],
        ["Owners' equity", "", _money(owners_equity)],
        [">Capital", "", _money(capital_total)],
        [">Current accounts", "", _money(current_accounts_total)],
        ["Non-current liabilities", "", _money(non_current_loan)],
        [">Loan", "", _money(non_current_loan)],
        ["Current liabilities", "", _money(current_liabilities)],
        [">Trade and other payables", "", _money(trade_payables)],
        [">Bank overdraft", "", _money(bank_overdraft)],
        [">Current portion of loan", "", _money(short_term_loan)],
        ["TOTAL EQUITY AND LIABILITIES", "", _money(total_equity_liabilities)],
    ]

    cell_hints: Dict[str, str] = {}
    if mode_norm == "scaffold":
        cell_hints["t0_r4_c2"] = f"Loan (total) = Owners' equity × debt:equity = {owners_equity:,.0f} × {debt_equity}"
        cell_hints["t0_r5_c2"] = f"Non-current portion = Total loan - current portion = {loan_total:,.0f} - {short_term_loan:,.0f}"

    prompt = f"""{business}

#### REQUIRED:
Prepare the Equity and Liabilities section of the Statement of Financial Position as at 28 February 20{year}. Show calculations where notes are not required.

#### INFORMATION:
A. Owners' equity totals:
- Capital (total), R{capital_total:,.0f}
- Current accounts (total), R{current_accounts_total:,.0f}

B. Financial indicator:
- Debt : equity ratio = {debt_equity} : 1

C. Current liabilities balances:
- Trade and other payables, R{trade_payables:,.0f}
- Bank overdraft, R{bank_overdraft:,.0f}
- Current portion of loan, R{short_term_loan:,.0f}"""

    return _mk_journal(
        prompt=prompt,
        journal_type="partnership_sfp_equity_liabilities_section",
        headers=headers,
        values_rows=rows,
        difficulty=difficulty,
        mode=mode,
        base_editable_cols=[2],
        title_fields=[
            {"label": "NAME OF BUSINESS", "value": business},
            {"label": "STATEMENT OF FINANCIAL POSITION", "value": f"as at 28 February 20{year}"},
        ],
        cell_hints=cell_hints,
        archetype_key="g11_partnership_balance_sheet_equity_liabilities_debt_equity",
    )


def _make_equity_and_liabilities_section_current_ratio(
    *,
    r: random.Random,
    difficulty: str,
    mode: str,
) -> Dict[str, Any]:
    scenario = build_scenario(seed=r.randint(1, 1000))
    business = scenario["business"]
    year = int(r.choice([21, 22, 23]))

    current_ratio = float(r.choice([1.5, 2.0]))

    inventories = float(r.choice([84735, 58400, 286400, 134180]))
    receivables = float(r.choice([90160, 127230, 256790]))
    cash = float(r.choice([68000, 136600, 20200, 10317]))
    current_assets = _round_money(inventories + receivables + cash)

    current_liabilities = _round_money(current_assets / current_ratio)

    trade_payables = float(r.choice([28770, 106930, 96399, 871890]))
    short_term_loan = float(r.choice([9000, 15000, 55000, 91470]))
    # Derive overdraft as balancing figure
    bank_overdraft = _round_money(current_liabilities - trade_payables - short_term_loan)
    if bank_overdraft < 0:
        # keep overdraft non-negative; adjust payables to keep consistent
        trade_payables = _round_money(trade_payables + abs(bank_overdraft))
        bank_overdraft = 0.0
        current_liabilities = _round_money(trade_payables + short_term_loan + bank_overdraft)

    owners_equity = float(r.choice([408670, 2091100, 3130880]))
    non_current_loan = float(r.choice([31000, 518330, 1045550]))
    total_equity_liabilities = _round_money(owners_equity + non_current_loan + current_liabilities)

    headers = ["Equity and liabilities", "Note", "Amount"]
    rows: List[List[Optional[str]]] = [
        ["EQUITY AND LIABILITIES", "", ""],
        ["Owners' equity", "", _money(owners_equity)],
        ["Non-current liabilities", "", _money(non_current_loan)],
        [">Loan", "", _money(non_current_loan)],
        ["Current liabilities", "", _money(current_liabilities)],
        [">Trade and other payables", "", _money(trade_payables)],
        [">Short term loan", "", _money(short_term_loan)],
        [">Bank overdraft", "", _money(bank_overdraft)],
        ["TOTAL EQUITY AND LIABILITIES", "", _money(total_equity_liabilities)],
    ]

    cell_hints: Dict[str, str] = {}
    if str(mode or "").strip().lower() == "scaffold":
        cell_hints["t0_r4_c2"] = (
            f"Current liabilities = Current assets / current ratio = {current_assets:,.0f} / {current_ratio} = {current_liabilities:,.0f}"
        )
        cell_hints["t0_r7_c2"] = (
            f"Overdraft (balancing) = Current liabilities - (payables + short term loan) = {current_liabilities:,.0f} - ({trade_payables:,.0f} + {short_term_loan:,.0f})"
        )

    prompt = f"""{business}

#### REQUIRED:
Prepare the Equity and Liabilities section of the Statement of Financial Position as at 28 February 20{year}. Show calculations where required.

#### INFORMATION:
A. Current assets:
- Inventory, R{inventories:,.0f}
- Trade and other receivables, R{receivables:,.0f}
- Cash and cash equivalents, R{cash:,.0f}

B. Financial indicator:
- Current ratio = {current_ratio} : 1

C. Additional information:
- Trade and other payables, R{trade_payables:,.0f}
- Short term loan, R{short_term_loan:,.0f}

Use the current ratio to determine the total current liabilities and calculate the bank overdraft as the balancing figure."""

    return _mk_journal(
        prompt=prompt,
        journal_type="partnership_sfp_equity_liabilities_current_ratio",
        headers=headers,
        values_rows=rows,
        difficulty=difficulty,
        mode=mode,
        base_editable_cols=[2],
        title_fields=[
            {"label": "NAME OF BUSINESS", "value": business},
            {"label": "STATEMENT OF FINANCIAL POSITION", "value": f"as at 28 February 20{year}"},
        ],
        cell_hints=cell_hints,
        archetype_key="g11_partnership_balance_sheet_equity_liabilities_current_ratio",
    )


def _make_loan_statement_backcalc_calc(*, r: random.Random, mode: str) -> Dict[str, Any]:
    year = int(r.choice([2021, 2022, 2023]))
    opening = float(r.choice([49_000, 692_000, 710_500, 1_010_000]))
    repayments = float(r.choice([12_000, 88_680, 178_900, 55_000]))
    interest = float(r.choice([20_000, 78_200, 90_550]))

    closing = _round_money(opening + interest - repayments)

    portion_pct = float(r.choice([0.15, 0.20]))
    next_year_portion = _round_money(closing * portion_pct)

    return _make_calc(
        prompt=(
            f"A loan statement shows:\n\n"
            f"Opening balance: R{opening:,.0f}\n"
            f"Interest capitalised: R{interest:,.0f}\n"
            f"Repayments (including interest): R{repayments:,.0f}\n\n"
            f"Calculate the closing balance of the loan. Then calculate {int(portion_pct*100)}% of the closing balance (to be paid off in the next year)."
        ),
        correct_value=closing,
        unit="R",
        explanation=(
            f"Closing balance = Opening + Interest - Repayments = {opening:,.0f} + {interest:,.0f} - {repayments:,.0f} = R{closing:,.2f}. "
            f"Next-year portion = {int(portion_pct*100)}% × {closing:,.0f} = R{next_year_portion:,.2f}."
        ),
        mode=mode,
        archetype_key="g11_partnership_balance_sheet_loan_statement_backcalc",
    )


def _make_receivables_payables_and_sfp_bundle(*, r: random.Random, difficulty: str, mode: str) -> Dict[str, Any]:
    business = r.choice(["Smackers Stores", "BCM Traders", "Ball Sport Traders"])
    year = int(r.choice([21, 22, 23]))

    q1 = _make_trade_and_other_receivables_note(r=r, difficulty=difficulty, mode=mode, business=business, year=year)
    q2 = _make_trade_and_other_payables_note_excluding_overdraft_and_current_loan(r=r, difficulty=difficulty, mode=mode, business=business, year=year)
    q3 = _make_balance_sheet(r=r, difficulty=difficulty, mode=mode, business=business, year=year)

    meta = {"scenario": "receivables_payables_sfp"}
    for q in (q1, q2, q3):
        q_meta = dict(q.get("meta") or {})
        q_meta.update(meta)
        q["meta"] = q_meta

    bundle_prompt = (
        f"{business}\n\n"
        "#### REQUIRED:\n"
        "1. Prepare the Trade and other receivables note.\n"
        "2. Prepare the Trade and other payables note (excluding bank overdraft and current portion of loan).\n"
        "3. Prepare the Statement of Financial Position (Balance Sheet).\n\n"
        "#### INFORMATION:\n"
        f"Financial year end: 28 February 20{year}\n"
        "Use the notes where applicable and show calculations for figures not supported by notes."
    )

    bundle = _make_bundle(
        prompt=bundle_prompt,
        parts=[q1, q2, q3],
        archetype_key="g11_partnership_balance_sheet_receivables_payables_sfp_bundle",
    )
    bundle_meta = dict(bundle.get("meta") or {})
    bundle_meta.update(meta)
    bundle["meta"] = bundle_meta
    return bundle


def _make_interest_on_capital_calc(*, r: random.Random, mode: str) -> Dict[str, Any]:
    partner = r.choice(["Mac", "Adam", "Hockey", "Jack"])
    capital1 = float(r.choice([100000, 160000, 200000, 1680000]))
    capital2 = float(r.choice([80000, 100000, 1480000]))
    rate = float(r.choice([0.10, 0.12, 0.15]))
    months_split = int(r.choice([6, 9]))
    interest = _round_money((capital1 * rate * (months_split / 12.0)) + (capital2 * rate * ((12 - months_split) / 12.0)))

    return _make_calc(
        prompt=(
            f"Calculate the interest on capital for partner {partner}. Interest is calculated at {int(rate*100)}% p.a.\n\n"
            f"Capital for first {months_split} months: R{capital1:,.0f}\n"
            f"Capital for last {12 - months_split} months: R{capital2:,.0f}"
        ),
        correct_value=interest,
        unit="R",
        explanation=(
            f"Interest = (Capital × Rate × months/12) summed. = {capital1:,.0f} × {int(rate*100)}% × {months_split}/12 + "
            f"{capital2:,.0f} × {int(rate*100)}% × {12 - months_split}/12 = R{interest:,.2f}"
        ),
        mode=mode,
        archetype_key="g11_partnership_balance_sheet_interest_on_capital_calc",
    )


def _make_drawings_calc(*, r: random.Random, mode: str) -> Dict[str, Any]:
    partner = r.choice(["Mac", "Bryan", "Marvel", "Hockey"])
    monthly = float(r.choice([6700, 8000, 26500, 40000]))
    cash = float(r.choice([4670, 8000, 12500]))
    stock_cost = float(r.choice([3500, 8790, 35000]))
    drawings = _round_money(monthly * 12 + cash + stock_cost)

    return _make_calc(
        prompt=(
            f"Calculate the drawings for the year for {partner}.\n\n"
            f"Monthly drawings (salary EFT): R{monthly:,.0f} per month\n"
            f"Additional cash drawings: R{cash:,.0f}\n"
            f"Trading stock taken for personal use (cost price): R{stock_cost:,.0f}"
        ),
        correct_value=drawings,
        unit="R",
        explanation=f"Drawings = (monthly × 12) + cash + stock = {monthly:,.0f}×12 + {cash:,.0f} + {stock_cost:,.0f} = R{drawings:,.2f}",
        mode=mode,
        archetype_key="g11_partnership_balance_sheet_drawings_calc",
    )


def _make_notes_only_bundle(*, r: random.Random, difficulty: str, mode: str) -> Dict[str, Any]:
    business = r.choice(["MacAdam Stores", "Marvellous Candy Store", "IronMan Toy Store"])
    year = int(r.choice([21, 22, 23]))
    partner_a, partner_b = r.sample(["Mac", "Adam", "Marvel", "Lane", "Iron", "Man"], k=2)

    q1 = _make_capital_note(r=r, difficulty=difficulty, mode=mode, business=business, year=year, partners=(partner_a, partner_b))
    q2 = _make_current_accounts_note(r=r, difficulty=difficulty, mode=mode, business=business, year=year, partners=(partner_a, partner_b))

    meta = {"scenario": "notes_only"}
    for q in (q1, q2):
        q_meta = dict(q.get("meta") or {})
        q_meta.update(meta)
        q["meta"] = q_meta

    bundle_prompt = (
        f"{business}\n\n"
        "#### REQUIRED:\n"
        "1. Prepare the Capital note.\n"
        "2. Prepare the Current accounts note.\n\n"
        "#### INFORMATION:\n"
        f"Financial year end: 28 February 20{year}\n"
        f"Partners: {partner_a} and {partner_b}"
    )

    bundle = _make_bundle(
        prompt=bundle_prompt,
        parts=[q1, q2],
        archetype_key="g11_partnership_balance_sheet_notes_only_bundle",
    )
    bundle_meta = dict(bundle.get("meta") or {})
    bundle_meta.update(meta)
    bundle["meta"] = bundle_meta
    return bundle


def _make_balance_sheet(
    *,
    r: random.Random,
    difficulty: str,
    mode: str,
    business: Optional[str] = None,
    year: Optional[int] = None,
) -> Dict[str, Any]:
    business = business or r.choice(["John and John", "NM Stores", "BaSha Stores"])
    year = int(year if year is not None else r.choice([20, 21, 22, 23, 24]))

    # Minimal but coherent balance sheet build (A1 format: Item | Note | Amount)
    land_buildings = float(r.choice([800000, 516000, 1310000]))
    vehicles = float(r.choice([404860, 415200, 350000]))
    equipment = float(r.choice([100000, 117280, 130000]))
    acc_dep_veh = float(r.choice([25000, 103200, 150000]))
    acc_dep_eq = float(r.choice([56000, 35184, 46000]))

    non_current_assets = _round_money(land_buildings + (vehicles - acc_dep_veh) + (equipment - acc_dep_eq))

    trading_stock = float(r.choice([310000, 134180, 92500]))
    debtors = float(r.choice([124490, 64970, 73500]))
    bank = float(r.choice([-6500, 10317, 25000]))

    current_assets = _round_money(trading_stock + debtors + max(bank, 0.0))

    total_assets = _round_money(non_current_assets + current_assets)

    capital = float(r.choice([1000000, 980000, 850000]))
    current_accounts = float(r.choice([200400, 15000, 118800]))
    owners_equity = _round_money(capital + current_accounts)

    loan = float(r.choice([200000, 40000, 60000]))
    non_current_liabilities = _round_money(loan)

    creditors = float(r.choice([240700, 57852, 45000]))
    accrued_expenses = float(r.choice([12500, 6100, 5420]))
    income_in_advance = float(r.choice([7200, 0, 1500]))

    current_liabilities = _round_money(
        creditors + accrued_expenses + income_in_advance + (abs(bank) if bank < 0 else 0.0)
    )

    total_equity_liabilities = _round_money(owners_equity + non_current_liabilities + current_liabilities)

    # Adjust by forcing owners equity to balance if needed.
    delta = _round_money(total_assets - total_equity_liabilities)
    if abs(delta) > 0.01:
        owners_equity = _round_money(owners_equity + delta)
        current_accounts = _round_money(current_accounts + delta)
        total_equity_liabilities = _round_money(owners_equity + non_current_liabilities + current_liabilities)

    headers = ["Item", "Note", "Amount"]

    rows: List[List[Optional[str]]] = [
        ["ASSETS", "", ""],
        ["Non-current assets", "", _money(non_current_assets)],
        ["Land and Buildings", "", _money(land_buildings)],
        ["Vehicles (carrying value)", "", _money(vehicles - acc_dep_veh)],
        ["Equipment (carrying value)", "", _money(equipment - acc_dep_eq)],
        ["Current assets", "", _money(current_assets)],
        ["Trading stock", "", _money(trading_stock)],
        ["Trade and other receivables", "", _money(debtors)],
        ["Bank", "", _money(bank)],
        ["TOTAL ASSETS", "", _money(total_assets)],
        ["", "", ""],
        ["EQUITY AND LIABILITIES", "", ""],
        ["Owner's equity", "", _money(owners_equity)],
        ["Capital", "", _money(capital)],
        ["Current accounts", "", _money(current_accounts)],
        ["Non-current liabilities", "", _money(non_current_liabilities)],
        ["Loan", "", _money(loan)],
        ["Current liabilities", "", _money(current_liabilities)],
        ["Creditors control", "", _money(creditors)],
        ["Accrued expenses", "", _money(accrued_expenses)],
        ["Income received in advance", "", _money(income_in_advance)],
    ]

    if bank < 0:
        rows.append(["Bank overdraft", "", _money(abs(bank))])

    rows.append(["TOTAL EQUITY AND LIABILITIES", "", _money(total_equity_liabilities)])

    cell_hints: Dict[str, str] = {}
    if str(mode or "").strip().lower() == "scaffold":
        for rix, row in enumerate(rows):
            lbl = str(row[0] or "").strip().lower()
            key = f"t0_r{rix}_c2"
            if lbl == "assets":
                cell_hints[key] = "Heading row — no amount."
            elif "non-current assets" in lbl:
                cell_hints[key] = "Non-current assets = Land & Buildings + Vehicles (CV) + Equipment (CV)."
            elif "land" in lbl:
                cell_hints[key] = "Land and buildings at cost (no depreciation on land/buildings at Gr11)."
            elif "vehicle" in lbl:
                cell_hints[key] = f"Carrying value = Cost – Accumulated depreciation = {vehicles:,.0f} – {acc_dep_veh:,.0f}."
            elif "equipment" in lbl:
                cell_hints[key] = f"Carrying value = Cost – Accumulated depreciation = {equipment:,.0f} – {acc_dep_eq:,.0f}."
            elif "current assets" in lbl and "total" not in lbl:
                cell_hints[key] = "Current assets = Trading stock + Trade receivables + Bank (if positive)."
            elif "trading stock" in lbl:
                cell_hints[key] = "Trading stock / inventory value after adjustments."
            elif "receivable" in lbl:
                cell_hints[key] = "Trade and other receivables per the note."
            elif lbl == "bank" and bank >= 0:
                cell_hints[key] = "Favourable bank balance — current asset."
            elif "total assets" in lbl:
                cell_hints[key] = "Total assets = Non-current assets + Current assets."
            elif "equity and liabilities" in lbl and "total" not in lbl:
                cell_hints[key] = "Heading row — no amount."
            elif "owner" in lbl and "equity" in lbl:
                cell_hints[key] = "Owners' equity = Capital + Current accounts."
            elif lbl == "capital":
                cell_hints[key] = "Total capital per the Capital note."
            elif "current account" in lbl:
                cell_hints[key] = "Total current accounts per the Current accounts note."
            elif "non-current liabilities" in lbl:
                cell_hints[key] = "Long-term portion of the loan (excluding current portion)."
            elif lbl == "loan":
                cell_hints[key] = "Loan balance (non-current portion only)."
            elif "current liabilities" in lbl and "total" not in lbl:
                cell_hints[key] = "Current liabilities = Creditors + Accrued expenses + Income in advance + Overdraft."
            elif "creditor" in lbl:
                cell_hints[key] = "Trade creditors / creditors control."
            elif "accrued" in lbl:
                cell_hints[key] = "Accrued expenses — amounts owed but not yet paid."
            elif "income received in advance" in lbl or "income in advance" in lbl:
                cell_hints[key] = "Income received in advance — liability until earned."
            elif "overdraft" in lbl:
                cell_hints[key] = "Bank overdraft — current liability (unfavourable bank balance)."
            elif "total equity" in lbl:
                cell_hints[key] = "Must equal Total assets."

    prompt = "Partnerships — Statement of Financial Position\n\nRequired: Prepare the Balance Sheet (A1 format)."

    return _mk_journal(
        prompt=prompt,
        journal_type="partnership_balance_sheet",
        headers=headers,
        values_rows=rows,
        difficulty=difficulty,
        mode=mode,
        base_editable_cols=[2],
        title_fields=[
            {"label": "NAME OF BUSINESS", "value": business},
            {"label": "BALANCE SHEET", "value": f"at 31 December {year}.5"},
        ],
        cell_hints=cell_hints,
        archetype_key="g11_partnership_balance_sheet_statement",
    )


def _make_q1_full_scenario(*, r: random.Random, difficulty: str, mode: str) -> Dict[str, Any]:
    business = r.choice(["John and John", "NM Stores", "BaSha Stores"])
    year = int(r.choice([20, 21, 22, 23, 24]))
    partner_a, partner_b = r.sample(["Butler", "Johnson", "Baloyi", "Shabangu"], k=2)

    # Bundles the sub-questions under one shared context.
    # Net profit adjustment calculations will be added as a separate sub-question once the format is confirmed.
    q1 = _make_current_accounts_note(
        r=r,
        difficulty=difficulty,
        mode=mode,
        business=business,
        year=year,
        partners=(partner_a, partner_b),
    )
    q2 = _make_trade_and_other_receivables_note(r=r, difficulty=difficulty, mode=mode, business=business, year=year)
    q3 = _make_trade_and_other_payables_note(r=r, difficulty=difficulty, mode=mode, business=business, year=year)
    q4 = _make_balance_sheet(r=r, difficulty=difficulty, mode=mode, business=business, year=year)

    meta = {"scenario": "q1_full"}
    for q in (q1, q2, q3, q4):
        q_meta = dict(q.get("meta") or {})
        q_meta.update(meta)
        q["meta"] = q_meta

    bundle_prompt = (
        f"{business}\n\n"
        "#### REQUIRED:\n"
        "1.1 Prepare the Current accounts note.\n"
        "1.2 Prepare the Trade and other receivables note.\n"
        "1.3 Prepare the Trade and other payables note.\n"
        "1.4 Prepare the Statement of Financial Position (Balance Sheet).\n\n"
        "#### INFORMATION:\n"
        f"Financial year end: 31 December 20{year}\n"
        f"Partners: {partner_a} and {partner_b}"
    )

    bundle = _make_bundle(
        prompt=bundle_prompt,
        parts=[q1, q2, q3, q4],
        archetype_key="g11_partnership_balance_sheet_q1_full_bundle",
    )
    bundle_meta = dict(bundle.get("meta") or {})
    bundle_meta.update(meta)
    bundle["meta"] = bundle_meta
    return bundle


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

    n = int(count) if isinstance(count, int) else 1
    if n < 1:
        n = 1
    if n > 20:
        n = 20

    subskill_norm = str(subskill or "mixed").strip().lower()
    qtype_norm = str(question_type or "mixed").strip().lower()

    builders: List[Any] = [
        lambda: _make_current_accounts_note(r=r, difficulty=difficulty, mode=mode),
        lambda: _make_trade_and_other_receivables_note(r=r, difficulty=difficulty, mode=mode),
        lambda: _make_trade_and_other_payables_note(r=r, difficulty=difficulty, mode=mode),
        lambda: _make_balance_sheet(r=r, difficulty=difficulty, mode=mode),
        lambda: _make_capital_note(r=r, difficulty=difficulty, mode=mode),
        lambda: _make_equity_and_liabilities_section_debt_equity(r=r, difficulty=difficulty, mode=mode),
        lambda: _make_equity_and_liabilities_section_current_ratio(r=r, difficulty=difficulty, mode=mode),
        lambda: _make_interest_on_capital_calc(r=r, mode=mode),
        lambda: _make_drawings_calc(r=r, mode=mode),
        lambda: _make_notes_only_bundle(r=r, difficulty=difficulty, mode=mode),
        lambda: _make_loan_statement_backcalc_calc(r=r, mode=mode),
        lambda: _make_trade_and_other_payables_note_excluding_overdraft_and_current_loan(r=r, difficulty=difficulty, mode=mode),
        lambda: _make_receivables_payables_and_sfp_bundle(r=r, difficulty=difficulty, mode=mode),
        lambda: _make_q1_full_scenario(r=r, difficulty=difficulty, mode=mode),
    ]

    if subskill_norm in {"current_accounts", "current", "note_current"}:
        builders = [builders[0]]
    elif subskill_norm in {"capital", "capital_note", "note_capital"}:
        builders = [builders[4]]
    elif subskill_norm in {"receivables", "trade_receivables", "note_receivables"}:
        builders = [builders[1]]
    elif subskill_norm in {"payables", "trade_payables", "note_payables", "creditors"}:
        builders = [builders[2]]
    elif subskill_norm in {"balance_sheet", "sfp", "statement_of_financial_position"}:
        builders = [builders[3]]
    elif subskill_norm in {"equity_liabilities", "equity_and_liabilities", "equity", "liabilities"}:
        builders = [builders[5]]
    elif subskill_norm in {"current_ratio", "current_ratio_sfp", "equity_liabilities_current_ratio"}:
        builders = [builders[6]]
    elif subskill_norm in {"interest", "interest_on_capital"}:
        builders = [builders[7]]
    elif subskill_norm in {"drawings", "drawings_calc"}:
        builders = [builders[8]]
    elif subskill_norm in {"notes_only", "capital_and_current"}:
        builders = [builders[9]]
    elif subskill_norm in {"loan_statement", "loan_backcalc", "loan"}:
        builders = [builders[10]]
    elif subskill_norm in {"payables_excl", "payables_excluding", "trade_payables_excluding"}:
        builders = [builders[11]]
    elif subskill_norm in {"receivables_payables_sfp", "notes_and_sfp", "receivables_payables_bundle"}:
        builders = [builders[12]]
    elif subskill_norm in {"full", "full_scenario", "scenario", "q1", "q1_full"}:
        builders = [builders[13]]

    out: List[Dict[str, Any]] = []
    for _ in range(n):
        q = r.choice(builders)()
        if qtype_norm != "mixed" and str(q.get("question_type") or "").strip().lower() != qtype_norm:
            # If filtered to a type that doesn't match, just ignore filter (most are journals anyway).
            pass
        out.append(q)

    return out
