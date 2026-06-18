from __future__ import annotations

import random
from typing import Any, Dict, List, Optional, Tuple

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


def _br_amount(x: float) -> str:
    # Expenses shown in brackets
    return f"({_money(abs(x))})" if x < 0 else _money(x)


def _make_bundle(*, prompt: str, parts: List[Dict[str, Any]], archetype_key: str = "") -> Dict[str, Any]:
    out: Dict[str, Any] = {
        "id": _make_id("acct12_financial_statements_bundle"),
        "question_type": "bundle",
        "prompt": prompt,
        "parts": parts,
    }
    if archetype_key:
        out["meta"] = {"archetype_key": archetype_key}
    return out


def _is_scaffold(mode: str) -> bool:
    return str(mode or "").strip().lower() == "scaffold"


def _should_omit_labels(*, difficulty: str, mode: str) -> bool:
    diff = str(difficulty or "easy").strip().lower()
    return (not _is_scaffold(mode)) and diff in {"hard"}


def _find_row_indices(rows_values: List[List[Optional[str]]], label: str, col_index: int = 0) -> List[int]:
    want = str(label or "").strip()
    if not want:
        return []
    out: List[int] = []
    for rix, row in enumerate(rows_values):
        if rix < 0 or rix >= len(rows_values):
            continue
        v = row[col_index] if col_index < len(row) else None
        if str(v or "").strip() == want:
            out.append(int(rix))
    return out


def _apply_label_omissions(
    *,
    rows_values: List[List[Optional[str]]],
    labels_to_omit: List[str],
    label_col_index: int = 0,
) -> List[int]:
    omit_rows: List[int] = []
    for lab in labels_to_omit:
        omit_rows.extend(_find_row_indices(rows_values, lab, col_index=label_col_index))

    omit_set = {int(x) for x in omit_rows}
    for rix in omit_set:
        if 0 <= int(rix) < len(rows_values) and label_col_index < len(rows_values[int(rix)]):
            rows_values[int(rix)][int(label_col_index)] = ""
    return sorted(omit_set)


def _attach_row_hints(
    *,
    cell_hints: Dict[str, str],
    rows_values: List[List[Optional[str]]],
    explanations: List[str],
    table_index: int = 0,
    col_index: int = 2,
) -> None:
    for rix in range(min(len(rows_values), len(explanations))):
        expl = str(explanations[rix] or "").strip()
        if expl:
            cell_hints[f"t{int(table_index)}_r{int(rix)}_c{int(col_index)}"] = expl


def _mk_income_statement_table(
    *,
    prompt: str,
    title_fields: List[Dict[str, Any]],
    values_rows: List[List[Optional[str]]],
    difficulty: str,
    mode: str,
    cell_hints: Optional[Dict[str, str]] = None,
    base_editable_cols: Optional[List[int]] = None,
    rubric_map: Optional[Dict[str, Dict[str, Any]]] = None,
    dependency_map: Optional[Dict[str, List[str]]] = None,
) -> Dict[str, Any]:
    headers = ["Item", "Note", "Amount"]

    diff = str(difficulty or "easy").strip().lower()
    mode_norm = str(mode or "").strip().lower()
    show_answers = mode_norm == "scaffold"

    base_editable_cols = list(base_editable_cols) if base_editable_cols is not None else [2]
    editable_cols = _journal_editable_cols_by_difficulty(
        difficulty=diff,
        base_editable_cols=base_editable_cols,
        total_cols=len(headers),
        mode=mode_norm,
    )

    rows: List[List[Dict[str, Any]]] = []
    correct_map: Dict[str, Any] = {}

    for rix, vals in enumerate(values_rows):
        if show_answers:
            display = vals
        else:
            editable_set = {int(c) for c in editable_cols}
            display = []
            for cix, v0 in enumerate(vals):
                v_str = "" if v0 is None else str(v0)
                is_label_col = int(cix) == 0
                label_was_omitted = is_label_col and (v_str.strip() == "")
                if int(cix) in editable_set and (not is_label_col or label_was_omitted):
                    display.append("")
                else:
                    display.append(v_str)
        rows.append(_build_prefixed_row(table_index=0, row_index=rix, values=display, editable_cols=editable_cols))
        for cix, v0 in enumerate(vals):
            correct_map[f"t0_r{int(rix)}_c{int(cix)}"] = "" if v0 is None else str(v0)

    out = _make_journal(
        prompt=prompt,
        journal_type="income_statement",
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        guidelines=[
            "Use the correct Grade 12 company Income Statement format.",
            "Expenses should be shown in brackets where applicable.",
            "Enter amounts without a currency symbol.",
        ],
        table_variant="grade_project",
        title_fields=title_fields,
        cell_hints=cell_hints if cell_hints else None,
        rubric_map=rubric_map,
        dependency_map=dependency_map,
    )
    out["id"] = _make_id("acct12_financial_statements")
    out["expected_answer_type"] = "journal"
    return out


def _mk_sci_table(
    *,
    prompt: str,
    title_fields: List[Dict[str, Any]],
    values_rows: List[List[Optional[str]]],
    difficulty: str,
    mode: str,
    cell_hints: Optional[Dict[str, str]] = None,
    base_editable_cols: Optional[List[int]] = None,
    rubric_map: Optional[Dict[str, Dict[str, Any]]] = None,
    dependency_map: Optional[Dict[str, List[str]]] = None,
) -> Dict[str, Any]:
    # Statement of Comprehensive Income uses same structure as income statement for our table UI.
    return _mk_income_statement_table(
        prompt=prompt,
        title_fields=title_fields,
        values_rows=values_rows,
        difficulty=difficulty,
        mode=mode,
        cell_hints=cell_hints,
        base_editable_cols=base_editable_cols,
        rubric_map=rubric_map,
        dependency_map=dependency_map,
    )


def _pick_company(r: random.Random) -> Tuple[str, str]:
    company = r.choice(["Aneesa Ltd", "Qoba Ltd", "Glebo Ltd", "Kwik Fix Ltd", "Kopano Ltd"])
    fy_end = r.choice(["28 February 2017", "30 June 2011", "28 February 2021", "30 June 2020", "28 February 2018"])
    return company, fy_end


def _make_company_income_statement(*, r: random.Random, difficulty: str, mode: str) -> Dict[str, Any]:
    company, fy_end = _pick_company(r)

    # Pre-adjustment items (loosely based on the curriculum worked example)
    sales = float(r.choice([10_500_000, 9_000_000, 8_750_000, 11_250_000]))
    debtors_allowances = float(r.choice([145_200, 120_000, 98_400, 160_000]))
    net_sales = _round_money(sales - debtors_allowances)

    cost_of_sales = float(r.choice([7_487_000, 5_625_000, 6_050_000, 7_050_000]))

    # Trading stock deficit (opening stock figure from TB vs physical stock)
    trading_stock_tb = float(r.choice([955_000, 1_200_000, 875_000]))
    trading_stock_physical = float(r.choice([902_150, 1_135_000, 820_000]))
    trading_stock_deficit = _round_money(max(0.0, trading_stock_tb - trading_stock_physical))

    gross_profit = _round_money(net_sales - cost_of_sales)

    # Other operating income
    rent_income_tb = float(r.choice([176_880, 120_000, 240_000]))
    rent_received_in_advance = float(r.choice([0.0, 14_520, 10_000, 18_000]))
    rent_income_final = _round_money(rent_income_tb - rent_received_in_advance)

    interest_income_tb = float(r.choice([26_630, 18_000, 45_000]))
    fixed_deposit = float(r.choice([495_000, 600_000, 350_000]))
    fd_rate = float(r.choice([8.0, 10.0, 7.0]))
    interest_income_final = _round_money(fixed_deposit * (fd_rate / 100.0))
    interest_income_adjustment = _round_money(interest_income_final - interest_income_tb)

    bad_debts_recovered = float(r.choice([2_300, 1_750, 0.0, 4_200]))

    other_operating_income = _round_money(rent_income_final + interest_income_final + bad_debts_recovered)
    # In the curriculum example, interest income is shown later as "Interest income".
    # Here we keep it later (after operating profit) and keep other operating income to rent + bad debts recovered.
    other_operating_income = _round_money(rent_income_final + bad_debts_recovered)

    gross_operating_income = _round_money(gross_profit + other_operating_income)

    # Operating expenses (company-specific: directors + audit)
    directors_fees_tb = float(r.choice([840_000, 650_000, 900_000]))
    directors_fees_outstanding = float(r.choice([0.0, 22_500, 15_000, 30_000]))
    directors_fees_final = _round_money(directors_fees_tb + directors_fees_outstanding)

    audit_fees = float(r.choice([73_800, 40_000, 55_000, 85_000]))

    salaries_wages = float(r.choice([660_000, 520_000, 750_000]))

    packing_material_tb = float(r.choice([23_100, 18_000, 35_000]))
    packing_on_hand = float(r.choice([4_260, 3_500, 6_000]))
    packing_material_final = _round_money(max(0.0, packing_material_tb - packing_on_hand))

    marketing_expenses = float(r.choice([480_000, 350_000, 520_000]))
    sundry_expenses = float(r.choice([63_770, 55_000, 72_000]))

    bad_debts_tb = float(r.choice([12_000, 18_000, 9_500]))
    insolvent_debtor = float(r.choice([32_000, 24_000, 40_000]))
    estate_cents = float(r.choice([0.40, 0.25, 0.50]))
    write_off = _round_money(insolvent_debtor * (1.0 - estate_cents))
    bad_debts_final = _round_money(bad_debts_tb + write_off)

    prov_bad_debts_current = float(r.choice([18_000, 24_000, 15_000]))
    debtors_control = float(r.choice([396_000, 810_000, 520_000]))
    prov_pct = float(r.choice([0.05, 0.06, 0.04]))
    prov_required = _round_money(max(0.0, (debtors_control - write_off) * prov_pct))
    prov_adjustment = _round_money(max(0.0, prov_required - prov_bad_debts_current))

    depreciation = float(r.choice([148_800, 125_000, 175_000]))

    operating_expenses_total = _round_money(
        directors_fees_final
        + audit_fees
        + salaries_wages
        + packing_material_final
        + marketing_expenses
        + sundry_expenses
        + bad_debts_final
        + prov_adjustment
        + depreciation
        + trading_stock_deficit
    )

    operating_profit = _round_money(gross_operating_income - operating_expenses_total)

    # Interest income shown after operating profit (as in curriculum)
    profit_before_finance_cost = _round_money(operating_profit + interest_income_final)

    # Finance cost (interest expense) - use loan statement arithmetic from curriculum approach
    loan_open = float(r.choice([1_125_000, 900_000, 650_000]))
    repayments_total = float(r.choice([458_000, 320_000, 500_000]))
    loan_close = float(r.choice([804_500, 620_000, 500_000]))
    finance_cost = _round_money(max(0.0, repayments_total + loan_close - loan_open))

    profit_before_tax = _round_money(profit_before_finance_cost - finance_cost)

    income_tax = float(r.choice([150_285, 176_240, 93_640, 210_000]))
    net_profit_after_tax = _round_money(profit_before_tax - income_tax)

    # Build rows in the doc's format/order
    rows: List[List[Optional[str]]] = []

    rows.append([f"Sales ({_money(sales)} - {_money(debtors_allowances)})", "", _money(net_sales)])
    rows.append(["Cost of sales", "", f"({_money(cost_of_sales)})"])
    rows.append(["Gross profit", "", _money(gross_profit)])

    rows.append(["Other operating income", "", _money(other_operating_income)])
    rows.append([f"  Rent income", "", _money(rent_income_final)])
    if bad_debts_recovered:
        rows.append(["  Bad debts recovered", "", _money(bad_debts_recovered)])

    rows.append(["Gross operating income", "", _money(gross_operating_income)])

    rows.append(["Operating expenses", "", f"({_money(operating_expenses_total)})"])
    rows.append(["  Directors fees", "", _money(directors_fees_final)])
    rows.append(["  Audit fees", "", _money(audit_fees)])
    rows.append(["  Salaries and wages", "", _money(salaries_wages)])
    rows.append(["  Packing material", "", _money(packing_material_final)])
    rows.append(["  Marketing expenses", "", _money(marketing_expenses)])
    rows.append(["  Sundry expenses", "", _money(sundry_expenses)])
    rows.append(["  Bad debts", "", _money(bad_debts_final)])
    rows.append(["  Provision for bad debts adjustment", "", _money(prov_adjustment)])
    rows.append(["  Depreciation", "", _money(depreciation)])
    if trading_stock_deficit > 0:
        rows.append(["  Trading stock deficit", "", _money(trading_stock_deficit)])

    rows.append(["Operating profit", "", _money(operating_profit)])

    rows.append(["Interest income", "", _money(interest_income_final)])
    rows.append(["Profit before interest expenses/finance cost", "", _money(profit_before_finance_cost)])

    rows.append(["Interest expenses/finance cost", "", f"({_money(finance_cost)})"])
    rows.append(["Profit before tax", "", _money(profit_before_tax)])

    rows.append(["Income tax", "", f"({_money(income_tax)})"])
    rows.append(["Net profit after tax", "", _money(net_profit_after_tax)])

    omit_label_rows: List[int] = []
    if _should_omit_labels(difficulty=difficulty, mode=mode):
        omit_labels = [
            "Gross profit",
            "Operating expenses",
            "Operating profit",
            "Profit before tax",
            "Net profit after tax",
        ]
        omit_label_rows = _apply_label_omissions(rows_values=rows, labels_to_omit=omit_labels, label_col_index=0)

    cell_hints: Dict[str, str] = {}
    row_expl = [
        "Net sales: Sales less debtors' allowances (sales returns/discounts).",
        "Cost of sales: direct cost of goods sold (show in brackets).",
        "Gross profit: Net sales minus cost of sales.",
        "Other operating income: income earned from operations other than sales.",
        "Rent income earned for the year (adjust for any prepaid/received in advance).",
        "Bad debts recovered: previously written-off debt collected.",
        "Gross operating income: Gross profit plus other operating income.",
        "Operating expenses: total operating costs for the year (show in brackets).",
        "Directors' fees: include outstanding fees in the expense.",
        "Audit fees: expense for audit services.",
        "Salaries and wages: employee costs.",
        "Packing material: expense less packing material on hand.",
        "Marketing expenses: promotion/advertising costs.",
        "Sundry expenses: miscellaneous operating expenses.",
        "Bad debts: include irrecoverable amounts written off.",
        "Provision for bad debts adjustment: adjust provision to required %.",
        "Depreciation: non-cash expense on fixed assets.",
        "Trading stock deficit: stock shortage is an expense.",
        "Operating profit: Gross operating income less operating expenses.",
        "Interest income: income from investments.",
        "Profit before finance cost: Operating profit plus interest income.",
        "Finance cost: interest on loans (show in brackets).",
        "Profit before tax: profit after finance cost.",
        "Income tax: tax expense for the year (show in brackets).",
        "Net profit after tax: final profit for the year.",
    ]
    _attach_row_hints(cell_hints=cell_hints, rows_values=rows, explanations=row_expl, col_index=2)

    prompt = "Companies — Income Statement (Financial Statements & Notes)\n\nPrepare the Income Statement in the given format."

    q = _mk_income_statement_table(
        prompt=prompt,
        title_fields=[
            {"label": "INCOME STATEMENT", "value": ""},
            {"label": "Name of company", "value": company},
            {"label": "For the year ended", "value": fy_end},
        ],
        values_rows=rows,
        difficulty=difficulty,
        mode=mode,
        cell_hints=cell_hints,
        base_editable_cols=([2] if not omit_label_rows else [0, 2]),
    )

    q["meta"] = {
        "sales": sales,
        "debtors_allowances": debtors_allowances,
        "cost_of_sales": cost_of_sales,
        "rent_income_tb": rent_income_tb,
        "rent_received_in_advance": rent_received_in_advance,
        "interest_income_tb": interest_income_tb,
        "fixed_deposit": fixed_deposit,
        "fixed_deposit_rate_pct": fd_rate,
        "interest_income_adjustment": interest_income_adjustment,
        "directors_fees_tb": directors_fees_tb,
        "directors_fees_outstanding": directors_fees_outstanding,
        "bad_debts_tb": bad_debts_tb,
        "insolvent_debtor": insolvent_debtor,
        "estate_cents": estate_cents,
        "write_off": write_off,
        "provision_current": prov_bad_debts_current,
        "provision_required": prov_required,
        "provision_adjustment": prov_adjustment,
        "loan_open": loan_open,
        "repayments_total": repayments_total,
        "loan_close": loan_close,
        "finance_cost": finance_cost,
        "income_tax": income_tax,
        "archetype_key": "g12_fs_income_statement_basic",
    }

    return q


def _make_example2_statement_of_comprehensive_income(*, r: random.Random, difficulty: str, mode: str) -> Dict[str, Any]:
    company, fy_end = _pick_company(r)

    revenue = float(r.choice([10_500_000, 9_000_000, 8_750_000, 11_250_000]))
    cost_of_sales = float(r.choice([7_487_000, 5_625_000, 6_050_000, 7_050_000]))
    gross_profit = _round_money(revenue - cost_of_sales)

    other_income = float(r.choice([120_000, 176_880, 95_000, 210_000]))
    operating_expenses = float(r.choice([2_650_000, 2_980_000, 2_250_000, 3_150_000]))
    operating_profit = _round_money(gross_profit + other_income - operating_expenses)

    interest_income = float(r.choice([18_000, 26_630, 45_000, 32_000]))
    finance_cost = float(r.choice([120_000, 158_000, 93_640, 176_000]))
    profit_before_tax = _round_money(operating_profit + interest_income - finance_cost)

    income_tax = float(r.choice([150_285, 176_240, 93_640, 210_000]))
    profit_for_year = _round_money(profit_before_tax - income_tax)

    other_comprehensive_income = float(r.choice([0.0, 45_000, 80_000, 120_000]))
    total_comprehensive_income = _round_money(profit_for_year + other_comprehensive_income)

    rows: List[List[Optional[str]]] = []
    rows.append(["Revenue", "", _money(revenue)])
    rows.append(["Cost of sales", "", f"({_money(cost_of_sales)})"])
    rows.append(["Gross profit", "", _money(gross_profit)])
    rows.append(["Other income", "", _money(other_income)])
    rows.append(["Operating expenses", "", f"({_money(operating_expenses)})"])
    rows.append(["Operating profit", "", _money(operating_profit)])
    rows.append(["Interest income", "", _money(interest_income)])
    rows.append(["Finance cost", "", f"({_money(finance_cost)})"])
    rows.append(["Profit before tax", "", _money(profit_before_tax)])
    rows.append(["Income tax", "", f"({_money(income_tax)})"])
    rows.append(["Profit for the year", "", _money(profit_for_year)])
    rows.append(["Other comprehensive income", "", _money(other_comprehensive_income)])
    rows.append(["Total comprehensive income", "", _money(total_comprehensive_income)])

    omit_label_rows: List[int] = []
    if _should_omit_labels(difficulty=difficulty, mode=mode):
        omit_labels = [
            "Gross profit",
            "Operating profit",
            "Profit before tax",
            "Profit for the year",
            "Total comprehensive income",
        ]
        omit_label_rows = _apply_label_omissions(rows_values=rows, labels_to_omit=omit_labels, label_col_index=0)

    cell_hints: Dict[str, str] = {}
    row_expl = [
        "Revenue: total income from sales/services.",
        "Cost of sales: direct costs (show in brackets).",
        "Gross profit: Revenue minus cost of sales.",
        "Other income: additional income (e.g., rent/commission).",
        "Operating expenses: operating costs (show in brackets).",
        "Operating profit: Gross profit + other income - operating expenses.",
        "Interest income: income earned on investments.",
        "Finance cost: interest on loans (show in brackets).",
        "Profit before tax: before income tax is deducted.",
        "Income tax: tax expense for the year (show in brackets).",
        "Profit for the year: profit after tax.",
        "Other comprehensive income: gains/losses not included in profit (e.g., revaluation surplus).",
        "Total comprehensive income: Profit for the year + other comprehensive income.",
    ]
    _attach_row_hints(cell_hints=cell_hints, rows_values=rows, explanations=row_expl, col_index=2)

    prompt = (
        "Companies — Statement of Comprehensive Income (Financial Statements & Notes)\n\n"
        "Prepare the Statement of Comprehensive Income in the given format."
    )

    q = _mk_sci_table(
        prompt=prompt,
        title_fields=[
            {"label": "STATEMENT OF COMPREHENSIVE INCOME", "value": ""},
            {"label": "Name of company", "value": company},
            {"label": "For the year ended", "value": fy_end},
        ],
        values_rows=rows,
        difficulty=difficulty,
        mode=mode,
        cell_hints=cell_hints if _is_scaffold(mode) else None,
        base_editable_cols=([2] if not omit_label_rows else [0, 2]),
    )

    q["meta"] = {
        "revenue": revenue,
        "cost_of_sales": cost_of_sales,
        "operating_expenses": operating_expenses,
        "income_tax": income_tax,
        "other_comprehensive_income": other_comprehensive_income,
        "archetype_key": "g12_fs_example2_statement_of_comprehensive_income",
    }
    return q


def _make_example3_retained_note_and_balance_sheet_bundle(*, r: random.Random, difficulty: str, mode: str) -> Dict[str, Any]:
    retained = _make_retained_income_note(r=r, difficulty=difficulty, mode=mode)
    balance = _make_balance_sheet(r=r, difficulty=difficulty, mode=mode)

    prompt = (
        "Companies — Example 3 (Financial Statements & Notes)\n\n"
        "Prepare the Retained Income Note and the Balance Sheet from the same scenario."
    )
    return _make_bundle(
        prompt=prompt,
        parts=[retained, balance],
        archetype_key="g12_fs_example3_retained_note_and_balance_sheet_bundle",
    )

def _mk_retained_income_note_table(
    *,
    prompt: str,
    title_fields: List[Dict[str, Any]],
    values_rows: List[List[Optional[str]]],
    difficulty: str,
    mode: str,
    cell_hints: Optional[Dict[str, str]] = None,
    base_editable_cols: Optional[List[int]] = None,
    rubric_map: Optional[Dict[str, Dict[str, Any]]] = None,
    dependency_map: Optional[Dict[str, List[str]]] = None,
) -> Dict[str, Any]:
    headers = ["Details", "Amount"]

    diff = str(difficulty or "easy").strip().lower()
    mode_norm = str(mode or "").strip().lower()
    show_answers = mode_norm == "scaffold"

    base_editable_cols = list(base_editable_cols) if base_editable_cols is not None else [1]
    editable_cols = _journal_editable_cols_by_difficulty(
        difficulty=diff,
        base_editable_cols=base_editable_cols,
        total_cols=len(headers),
        mode=mode_norm,
    )

    rows: List[List[Dict[str, Any]]] = []
    correct_map: Dict[str, Any] = {}

    for rix, vals in enumerate(values_rows):
        if show_answers:
            display = vals
        else:
            editable_set = {int(c) for c in editable_cols}
            display = []
            for cix, v0 in enumerate(vals):
                v_str = "" if v0 is None else str(v0)
                is_label_col = int(cix) == 0
                label_was_omitted = is_label_col and (v_str.strip() == "")
                if int(cix) in editable_set and (not is_label_col or label_was_omitted):
                    display.append("")
                else:
                    display.append(v_str)
        rows.append(_build_prefixed_row(table_index=0, row_index=rix, values=display, editable_cols=editable_cols))
        for cix, v0 in enumerate(vals):
            correct_map[f"t0_r{int(rix)}_c{int(cix)}"] = "" if v0 is None else str(v0)

    out = _make_journal(
        prompt=prompt,
        journal_type="retained_income_note",
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        guidelines=[
            "Use the correct Grade 12 Retained Income Note format.",
            "Enter amounts without a currency symbol.",
            "Buyback premium reduces retained income.",
        ],
        table_variant="grade_project",
        title_fields=title_fields,
        cell_hints=cell_hints if mode_norm == "scaffold" and cell_hints else None,
        rubric_map=rubric_map,
        dependency_map=dependency_map,
    )
    out["id"] = _make_id("acct12_retained_income_note")
    out["expected_answer_type"] = "journal"
    return out


def _make_retained_income_note(*, r: random.Random, difficulty: str, mode: str) -> Dict[str, Any]:
    company, fy_end = _pick_company(r)

    # Opening retained income (from previous year balance)
    opening_retained_income = float(r.choice([890_000, 750_000, 1_200_000, 625_000]))

    # Net profit after tax from income statement
    net_profit_after_tax = float(r.choice([425_000, 380_000, 520_000, 295_000]))

    # Dividend payout rate from financial indicators
    dividend_payout_rate_pct = float(r.choice([70.0, 65.0, 80.0, 55.0]))
    total_dividends = _round_money(net_profit_after_tax * (dividend_payout_rate_pct / 100.0))

    # Share buyback effect (curriculum-specific: buyback reduces retained income by premium)
    # Premium = repurchase price - average issue price
    shares_repurchased = int(r.choice([10_000, 15_000, 8_000]))
    avg_issue_price = float(r.choice([8.50, 12.00, 6.75]))
    repurchase_price = float(r.choice([11.00, 15.50, 9.00]))  # Higher than avg issue price
    buyback_premium_per_share = repurchase_price - avg_issue_price
    total_buyback_premium = _round_money(shares_repurchased * buyback_premium_per_share)

    # Closing retained income calculation
    closing_retained_income = _round_money(
        opening_retained_income + net_profit_after_tax - total_dividends - total_buyback_premium
    )

    # Build note rows in curriculum format
    rows: List[List[Optional[str]]] = []

    rows.append(["Balance at beginning of year", _money(opening_retained_income)])
    rows.append(["Net profit after tax", _money(net_profit_after_tax)])
    rows.append(["Dividends", f"({_money(total_dividends)})"])
    rows.append(["  Ordinary share dividends", f"({_money(total_dividends)})"])
    rows.append(["Share buyback (premium)", f"({_money(total_buyback_premium)})"])
    rows.append(["  (Shares repurchased × premium per share)", ""])
    rows.append(["Balance at end of year", _money(closing_retained_income)])

    omit_label_rows: List[int] = []
    if _should_omit_labels(difficulty=difficulty, mode=mode):
        omit_labels = [
            "Balance at beginning of year",
            "Net profit after tax",
            "Dividends",
            "Balance at end of year",
        ]
        omit_label_rows = _apply_label_omissions(rows_values=rows, labels_to_omit=omit_labels, label_col_index=0)

    cell_hints: Dict[str, str] = {}
    row_expl = [
        "Opening retained income from previous year.",
        "Net profit after tax transferred from the income statement/statement of comprehensive income.",
        "Total ordinary share dividends for the year (show in brackets).",
        "Breakdown: ordinary share dividends.",
        "Share repurchase premium reduces retained income.",
        "Working line: shares repurchased × premium per share.",
        "Closing retained income for year-end.",
    ]
    _attach_row_hints(cell_hints=cell_hints, rows_values=rows, explanations=row_expl, col_index=1)
    cell_hints["t0_r4_c1"] = (
        f"Buyback premium = {shares_repurchased:,} shares × (repurchase price R{repurchase_price:.2f} - average issue price R{avg_issue_price:.2f})"
        f" = R{total_buyback_premium:,.2f}"
    )
    cell_hints["t0_r6_c1"] = "Closing balance = Opening + NPAT - Dividends - Buyback premium."

    prompt = "Companies — Retained Income Note (Financial Statements & Notes)\n\nPrepare the Retained Income Note in the given format."

    q = _mk_retained_income_note_table(
        prompt=prompt,
        title_fields=[
            {"label": "RETAINED INCOME NOTE", "value": ""},
            {"label": "Name of company", "value": company},
            {"label": "At", "value": fy_end},
        ],
        values_rows=rows,
        difficulty=difficulty,
        mode=mode,
        cell_hints=cell_hints,
        base_editable_cols=([1] if not omit_label_rows else [0, 1]),
    )

    q["meta"] = {
        "opening_retained_income": opening_retained_income,
        "net_profit_after_tax": net_profit_after_tax,
        "dividend_payout_rate_pct": dividend_payout_rate_pct,
        "total_dividends": total_dividends,
        "shares_repurchased": shares_repurchased,
        "avg_issue_price": avg_issue_price,
        "repurchase_price": repurchase_price,
        "buyback_premium_per_share": buyback_premium_per_share,
        "total_buyback_premium": total_buyback_premium,
        "closing_retained_income": closing_retained_income,
        "archetype_key": "g12_fs_retained_income_note_buyback",
    }

    return q


def _mk_balance_sheet_table(
    *,
    prompt: str,
    title_fields: List[Dict[str, Any]],
    values_rows: List[List[Optional[str]]],
    difficulty: str,
    mode: str,
    cell_hints: Optional[Dict[str, str]] = None,
    base_editable_cols: Optional[List[int]] = None,
    rubric_map: Optional[Dict[str, Dict[str, Any]]] = None,
    dependency_map: Optional[Dict[str, List[str]]] = None,
) -> Dict[str, Any]:
    headers = ["Details", "Note", "Amount"]

    diff = str(difficulty or "easy").strip().lower()
    mode_norm = str(mode or "").strip().lower()
    show_answers = mode_norm == "scaffold"

    base_editable_cols = list(base_editable_cols) if base_editable_cols is not None else [2]
    editable_cols = _journal_editable_cols_by_difficulty(
        difficulty=diff,
        base_editable_cols=base_editable_cols,
        total_cols=len(headers),
        mode=mode_norm,
    )

    rows: List[List[Dict[str, Any]]] = []
    correct_map: Dict[str, Any] = {}

    for rix, vals in enumerate(values_rows):
        if show_answers:
            display = vals
        else:
            editable_set = {int(c) for c in editable_cols}
            display = []
            for cix, v0 in enumerate(vals):
                v_str = "" if v0 is None else str(v0)
                is_label_col = int(cix) == 0
                label_was_omitted = is_label_col and (v_str.strip() == "")
                if int(cix) in editable_set and (not is_label_col or label_was_omitted):
                    display.append("")
                else:
                    display.append(v_str)
        rows.append(_build_prefixed_row(table_index=0, row_index=rix, values=display, editable_cols=editable_cols))
        for cix, v0 in enumerate(vals):
            correct_map[f"t0_r{int(rix)}_c{int(cix)}"] = "" if v0 is None else str(v0)

    out = _make_journal(
        prompt=prompt,
        journal_type="balance_sheet",
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        guidelines=[
            "Use the correct Grade 12 Balance Sheet format (Statement of Financial Position).",
            "Enter amounts without a currency symbol.",
            "Show notes reference numbers where applicable.",
        ],
        table_variant="grade_project",
        title_fields=title_fields,
        cell_hints=cell_hints if mode_norm == "scaffold" and cell_hints else None,
        rubric_map=rubric_map,
        dependency_map=dependency_map,
    )
    out["id"] = _make_id("acct12_balance_sheet")
    out["expected_answer_type"] = "journal"
    return out


def _make_balance_sheet(*, r: random.Random, difficulty: str, mode: str) -> Dict[str, Any]:
    company, fy_end = _pick_company(r)

    # Fixed/Tangible Assets (from Fixed Assets Note)
    land_cost = float(r.choice([1_200_000, 950_000, 1_500_000]))
    buildings_cost = float(r.choice([800_000, 650_000, 1_100_000]))
    vehicles_cost = float(r.choice([450_000, 380_000, 520_000]))
    equipment_cost = float(r.choice([320_000, 280_000, 400_000]))

    # Accumulated depreciation (for existing assets)
    buildings_acc_dep = float(r.choice([80_000, 65_000, 100_000]))
    vehicles_acc_dep = float(r.choice([90_000, 75_000, 110_000]))
    equipment_acc_dep = float(r.choice([64_000, 50_000, 80_000]))

    # Current year depreciation
    buildings_dep = float(r.choice([20_000, 16_000, 25_000]))
    vehicles_dep = float(r.choice([45_000, 38_000, 52_000]))
    equipment_dep = float(r.choice([32_000, 28_000, 40_000]))

    # Carrying values
    buildings_cv = _round_money(buildings_cost - buildings_acc_dep - buildings_dep)
    vehicles_cv = _round_money(vehicles_cost - vehicles_acc_dep - vehicles_dep)
    equipment_cv = _round_money(equipment_cost - equipment_acc_dep - equipment_dep)
    tangible_assets_total = _round_money(land_cost + buildings_cv + vehicles_cv + equipment_cv)

    # Fixed deposit (investments)
    fixed_deposit = float(r.choice([495_000, 600_000, 350_000]))

    # Current Assets
    trading_stock = float(r.choice([902_150, 1_135_000, 820_000]))
    # Trade and other receivables
    trade_debtors = float(r.choice([396_000, 810_000, 520_000]))
    prov_bad_debts = float(r.choice([18_000, 24_000, 15_000]))
    net_debtors = _round_money(trade_debtors - prov_bad_debts)
    sars_income_tax = float(r.choice([25_000, 18_000, 32_000]))
    prepaid_expenses = float(r.choice([8_500, 12_000, 6_000]))
    trade_receivables_total = _round_money(net_debtors + sars_income_tax + prepaid_expenses)

    # Cash and cash equivalents
    bank = float(r.choice([85_000, 120_000, 65_000]))
    cash_float = float(r.choice([15_000, 10_000, 20_000]))
    cash_total = _round_money(bank + cash_float)

    current_assets_total = _round_money(trading_stock + trade_receivables_total + cash_total)
    total_assets = _round_money(tangible_assets_total + fixed_deposit + current_assets_total)

    # Shareholders' Equity
    # Ordinary share capital (from Share Capital Note)
    share_capital = float(r.choice([2_500_000, 1_800_000, 3_200_000]))
    # Retained income (from Retained Income Note)
    retained_income = float(r.choice([1_315_000, 950_000, 1_650_000]))
    shareholders_equity = _round_money(share_capital + retained_income)

    # Non-current liabilities (Loan)
    loan_total = float(r.choice([804_500, 620_000, 500_000]))
    loan_current_portion = float(r.choice([320_000, 250_000, 200_000]))
    loan_non_current = _round_money(loan_total - loan_current_portion)

    # Current liabilities
    trade_creditors = float(r.choice([275_000, 320_000, 240_000]))
    creditors_accrued_expenses = float(r.choice([22_500, 18_000, 30_000]))
    income_tax_payable = float(r.choice([125_285, 158_240, 93_640]))
    shareholders_dividends = float(r.choice([297_500, 247_000, 416_000]))
    bank_overdraft = float(r.choice([0.0, 45_000, 0.0]))
    current_liabilities_total = _round_money(
        trade_creditors + creditors_accrued_expenses + income_tax_payable +
        shareholders_dividends + loan_current_portion + bank_overdraft
    )

    total_equity_liabilities = _round_money(shareholders_equity + loan_non_current + current_liabilities_total)

    # Build balance sheet rows in curriculum format
    rows: List[List[Optional[str]]] = []

    # ASSETS
    rows.append(["ASSETS", "", ""])
    rows.append(["Non-current assets", "", _money(tangible_assets_total + fixed_deposit)])
    rows.append(["Fixed/Tangible assets", "1", _money(tangible_assets_total)])
    rows.append(["  Land and buildings", "", _money(land_cost + buildings_cv)])
    rows.append(["  Vehicles", "", _money(vehicles_cv)])
    rows.append(["  Equipment", "", _money(equipment_cv)])
    rows.append(["Fixed deposit (investments)", "", _money(fixed_deposit)])

    rows.append(["Current assets", "", _money(current_assets_total)])
    rows.append(["Inventories (Trading stock)", "", _money(trading_stock)])
    rows.append(["Trade and other receivables", "2", _money(trade_receivables_total)])
    rows.append(["Cash and cash equivalents", "3", _money(cash_total)])
    rows.append(["", "", _money(total_assets)])

    # EQUITY AND LIABILITIES
    rows.append(["EQUITY AND LIABILITIES", "", ""])
    rows.append(["Shareholders' equity", "", _money(shareholders_equity)])
    rows.append(["Ordinary share capital", "4", _money(share_capital)])
    rows.append(["Retained income", "5", _money(retained_income)])

    rows.append(["Non-current liabilities", "", _money(loan_non_current)])
    rows.append(["Loan", "6", _money(loan_non_current)])

    rows.append(["Current liabilities", "", _money(current_liabilities_total)])
    rows.append(["Trade and other payables", "7", _money(trade_creditors + creditors_accrued_expenses)])
    rows.append(["Shareholders for dividends", "", _money(shareholders_dividends)])
    rows.append(["SARS: Income tax", "", _money(income_tax_payable)])
    rows.append(["Current portion of loan", "", _money(loan_current_portion)])
    if bank_overdraft > 0:
        rows.append(["Bank overdraft", "", _money(bank_overdraft)])
    rows.append(["", "", _money(total_equity_liabilities)])

    omit_label_rows: List[int] = []
    if _should_omit_labels(difficulty=difficulty, mode=mode):
        omit_labels = [
            "ASSETS",
            "Non-current assets",
            "Current assets",
            "EQUITY AND LIABILITIES",
            "Shareholders' equity",
            "Non-current liabilities",
            "Current liabilities",
        ]
        omit_label_rows = _apply_label_omissions(rows_values=rows, labels_to_omit=omit_labels, label_col_index=0)

    cell_hints: Dict[str, str] = {}
    row_expl = [
        "Section heading: ASSETS.",
        "Non-current assets: long-term assets used by the business.",
        "Fixed/Tangible assets: carrying value (book value) of fixed assets.",
        "Land and buildings: land is not depreciated; buildings shown at carrying value.",
        "Vehicles: shown at carrying value.",
        "Equipment: shown at carrying value.",
        "Fixed deposit: financial asset/investment (non-current unless portion is current).",
        "Current assets: assets expected to be realised within 12 months.",
        "Inventories: stock/consumables on hand.",
        "Trade and other receivables: amounts owed to the business (net of provisions).",
        "Cash and cash equivalents: bank and cash balances.",
        "Total assets: sum of non-current and current assets.",
        "Section heading: EQUITY AND LIABILITIES.",
        "Shareholders' equity: owners' interest in the business.",
        "Ordinary share capital: issued share capital.",
        "Retained income: accumulated profits retained.",
        "Non-current liabilities: long-term obligations.",
        "Loan: non-current portion of loan.",
        "Current liabilities: amounts payable within 12 months.",
        "Trade and other payables: creditors and accruals.",
        "Shareholders for dividends: dividends declared but not yet paid.",
        "SARS: Income tax payable/owing.",
        "Current portion of loan: capital repayment due in next 12 months.",
        "Bank overdraft: negative bank balance (shown in brackets in some formats).",
        "Total equity and liabilities: must equal total assets.",
    ]
    _attach_row_hints(cell_hints=cell_hints, rows_values=rows, explanations=row_expl, col_index=2)

    prompt = "Companies — Balance Sheet (Statement of Financial Position)\n\nPrepare the Balance Sheet in the given format."

    q = _mk_balance_sheet_table(
        prompt=prompt,
        title_fields=[
            {"label": "BALANCE SHEET", "value": ""},
            {"label": "Name of company", "value": company},
            {"label": "At", "value": fy_end},
        ],
        values_rows=rows,
        difficulty=difficulty,
        mode=mode,
        cell_hints=cell_hints,
        base_editable_cols=([2] if not omit_label_rows else [0, 2]),
    )

    q["meta"] = {
        "land_cost": land_cost,
        "buildings_cost": buildings_cost,
        "vehicles_cost": vehicles_cost,
        "equipment_cost": equipment_cost,
        "buildings_carrying_value": buildings_cv,
        "vehicles_carrying_value": vehicles_cv,
        "equipment_carrying_value": equipment_cv,
        "tangible_assets_total": tangible_assets_total,
        "fixed_deposit": fixed_deposit,
        "trading_stock": trading_stock,
        "trade_receivables_total": trade_receivables_total,
        "cash_total": cash_total,
        "total_assets": total_assets,
        "share_capital": share_capital,
        "retained_income": retained_income,
        "shareholders_equity": shareholders_equity,
        "loan_non_current": loan_non_current,
        "loan_current_portion": loan_current_portion,
        "current_liabilities_total": current_liabilities_total,
        "total_equity_liabilities": total_equity_liabilities,
        "archetype_key": "g12_fs_balance_sheet_companies",
    }

    return q


def _mk_trade_receivables_note(*, r: random.Random, difficulty: str, mode: str) -> Dict[str, Any]:
    company, fy_end = _pick_company(r)

    # Trade debtors (net of provision)
    trade_debtors_gross = float(r.choice([420_000, 550_000, 380_000]))
    provision_bad_debts = float(r.choice([24_000, 30_000, 18_000]))
    net_trade_debtors = _round_money(trade_debtors_gross - provision_bad_debts)

    # Other receivables
    sars_income_tax = float(r.choice([25_000, 18_000, 32_000]))
    prepaid_expenses = float(r.choice([8_500, 12_000, 6_000]))
    accrued_income = float(r.choice([4_200, 0.0, 7_500]))

    total_trade_receivables = _round_money(net_trade_debtors + sars_income_tax + prepaid_expenses + accrued_income)

    # Build note rows in curriculum format
    rows: List[List[Optional[str]]] = []

    rows.append(["Trade debtors", _money(trade_debtors_gross)])
    rows.append(["Less: Provision for bad debts", f"({_money(provision_bad_debts)})"])
    rows.append(["Net trade debtors", _money(net_trade_debtors)])
    rows.append(["SARS: Income tax", _money(sars_income_tax)])
    rows.append(["Prepaid expenses", _money(prepaid_expenses)])
    if accrued_income > 0:
        rows.append(["Accrued income", _money(accrued_income)])
    rows.append(["Trade and other receivables", _money(total_trade_receivables)])

    omit_label_rows: List[int] = []
    if _should_omit_labels(difficulty=difficulty, mode=mode):
        omit_labels = [
            "Net trade debtors",
            "Trade and other receivables",
        ]
        omit_label_rows = _apply_label_omissions(rows_values=rows, labels_to_omit=omit_labels, label_col_index=0)

    cell_hints: Dict[str, str] = {}
    row_expl = [
        "Trade debtors: amounts owed by customers.",
        "Provision for bad debts: expected credit losses (deduct).",
        "Net trade debtors: trade debtors less provision.",
        "SARS (income tax): amount overpaid/receivable from SARS.",
        "Prepaid expenses: expenses paid in advance.",
        "Accrued income: income earned but not yet received.",
        "Total trade and other receivables transferred to current assets.",
    ]
    _attach_row_hints(cell_hints=cell_hints, rows_values=rows, explanations=row_expl, col_index=1)

    prompt = "Companies — Trade and Other Receivables Note (Financial Statements & Notes)\n\nPrepare the Trade and Other Receivables Note in the given format."

    q = _mk_retained_income_note_table(
        prompt=prompt,
        title_fields=[
            {"label": "TRADE AND OTHER RECEIVABLES NOTE", "value": ""},
            {"label": "Name of company", "value": company},
            {"label": "At", "value": fy_end},
        ],
        values_rows=rows,
        difficulty=difficulty,
        mode=mode,
        cell_hints=cell_hints,
        base_editable_cols=([1] if not omit_label_rows else [0, 1]),
    )

    q["id"] = _make_id("acct12_trade_receivables_note")
    q["meta"] = {
        "trade_debtors_gross": trade_debtors_gross,
        "provision_bad_debts": provision_bad_debts,
        "net_trade_debtors": net_trade_debtors,
        "sars_income_tax": sars_income_tax,
        "prepaid_expenses": prepaid_expenses,
        "accrued_income": accrued_income,
        "total_trade_receivables": total_trade_receivables,
        "archetype_key": "g12_fs_trade_receivables_note",
    }

    return q


def _mk_fixed_assets_note_table(
    *,
    prompt: str,
    title_fields: List[Dict[str, Any]],
    values_rows: List[List[Optional[str]]],
    difficulty: str,
    mode: str,
    cell_hints: Optional[Dict[str, str]] = None,
    base_editable_cols: Optional[List[int]] = None,
) -> Dict[str, Any]:
    headers = ["Details", "Land & Buildings", "Vehicles", "Total"]

    diff = str(difficulty or "easy").strip().lower()
    mode_norm = str(mode or "").strip().lower()
    show_answers = mode_norm == "scaffold"

    base_editable_cols = list(base_editable_cols) if base_editable_cols is not None else [1, 2, 3]
    editable_cols = _journal_editable_cols_by_difficulty(
        difficulty=diff,
        base_editable_cols=base_editable_cols,
        total_cols=len(headers),
        mode=mode_norm,
    )

    rows: List[List[Dict[str, Any]]] = []
    correct_map: Dict[str, Any] = {}

    for rix, vals in enumerate(values_rows):
        if show_answers:
            display = vals
        else:
            editable_set = {int(c) for c in editable_cols}
            display = []
            for cix, v0 in enumerate(vals):
                v_str = "" if v0 is None else str(v0)
                is_label_col = int(cix) == 0
                label_was_omitted = is_label_col and (v_str.strip() == "")
                if int(cix) in editable_set and (not is_label_col or label_was_omitted):
                    display.append("")
                else:
                    display.append(v_str)
        rows.append(_build_prefixed_row(table_index=0, row_index=rix, values=display, editable_cols=editable_cols))
        for cix, v0 in enumerate(vals):
            correct_map[f"t0_r{int(rix)}_c{int(cix)}"] = "" if v0 is None else str(v0)

    out = _make_journal(
        prompt=prompt,
        journal_type="fixed_assets_note",
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        guidelines=[
            "Use the correct Grade 12 Tangible/Fixed Assets Note format.",
            "Land and buildings are NOT depreciated (show 0 for depreciation).",
            "Enter amounts without a currency symbol.",
        ],
        table_variant="grade_project",
        title_fields=title_fields,
        cell_hints=cell_hints if mode_norm == "scaffold" and cell_hints else None,
    )
    out["id"] = _make_id("acct12_fixed_assets_note")
    out["expected_answer_type"] = "journal"
    return out


def _make_fixed_assets_note(*, r: random.Random, difficulty: str, mode: str) -> Dict[str, Any]:
    company, fy_end = _pick_company(r)

    # Land & Buildings
    lb_cost_open = float(r.choice([2_097_000, 1_800_000, 2_500_000]))
    lb_acc_dep_open = 0.0  # Land & buildings not depreciated
    lb_cv_open = _round_money(lb_cost_open - lb_acc_dep_open)
    lb_additions = float(r.choice([0.0, 350_000, 500_000]))
    lb_disposals_cv = 0.0
    lb_depreciation = 0.0
    lb_cv_close = _round_money(lb_cv_open + lb_additions - lb_disposals_cv - lb_depreciation)
    lb_cost_close = _round_money(lb_cost_open + lb_additions)
    lb_acc_dep_close = 0.0

    # Vehicles
    v_cost_open = float(r.choice([814_000, 650_000, 920_000]))
    v_acc_dep_open = float(r.choice([294_800, 180_000, 350_000]))
    v_cv_open = _round_money(v_cost_open - v_acc_dep_open)
    v_additions = float(r.choice([0.0, 120_000, 250_000]))
    v_disposal_cost = float(r.choice([0.0, 80_000, 150_000]))
    v_disposal_acc_dep = float(r.choice([0.0, 45_000, 90_000])) if v_disposal_cost > 0 else 0.0
    v_disposals_cv = _round_money(v_disposal_cost - v_disposal_acc_dep)
    v_dep_rate = float(r.choice([15.0, 20.0, 10.0]))
    v_dep_base = _round_money(v_cost_open + v_additions - v_disposal_cost)
    v_depreciation = _round_money(v_dep_base * (v_dep_rate / 100.0))
    v_cv_close = _round_money(v_cv_open + v_additions - v_disposals_cv - v_depreciation)
    v_cost_close = _round_money(v_cost_open + v_additions - v_disposal_cost)
    v_acc_dep_close = _round_money(v_acc_dep_open + v_depreciation - v_disposal_acc_dep)

    # Totals
    t_cv_open = _round_money(lb_cv_open + v_cv_open)
    t_additions = _round_money(lb_additions + v_additions)
    t_disposals_cv = _round_money(lb_disposals_cv + v_disposals_cv)
    t_depreciation = _round_money(lb_depreciation + v_depreciation)
    t_cv_close = _round_money(lb_cv_close + v_cv_close)
    t_cost_close = _round_money(lb_cost_close + v_cost_close)
    t_acc_dep_close = _round_money(lb_acc_dep_close + v_acc_dep_close)

    rows: List[List[Optional[str]]] = []
    rows.append(["Carrying value at beginning of year", _money(lb_cv_open), _money(v_cv_open), _money(t_cv_open)])
    rows.append(["Cost", _money(lb_cost_open), _money(v_cost_open), _money(lb_cost_open + v_cost_open)])
    rows.append(["Accumulated depreciation", _money(0), f"({_money(v_acc_dep_open)})", f"({_money(v_acc_dep_open)})"])
    rows.append(["", "", "", ""])
    rows.append(["Movements", "", "", ""])
    rows.append(["Additions", _money(lb_additions), _money(v_additions), _money(t_additions)])
    rows.append(["Disposals at carrying value", _money(lb_disposals_cv), _money(v_disposals_cv), _money(t_disposals_cv)])
    rows.append(["Depreciation", _money(0), f"({_money(v_depreciation)})", f"({_money(t_depreciation)})"])
    rows.append(["", "", "", ""])
    rows.append(["Carrying value at end of year", _money(lb_cv_close), _money(v_cv_close), _money(t_cv_close)])
    rows.append(["Cost", _money(lb_cost_close), _money(v_cost_close), _money(t_cost_close)])
    rows.append(["Accumulated depreciation", _money(0), f"({_money(v_acc_dep_close)})", f"({_money(t_acc_dep_close)})"])

    omit_label_rows: List[int] = []
    if _should_omit_labels(difficulty=difficulty, mode=mode):
        omit_labels = [
            "Carrying value at beginning of year",
            "Movements",
            "Carrying value at end of year",
        ]
        omit_label_rows = _apply_label_omissions(rows_values=rows, labels_to_omit=omit_labels, label_col_index=0)

    cell_hints: Dict[str, str] = {}
    row_expl = [
        "Carrying value at beginning = Cost minus accumulated depreciation at start.",
        "Cost of assets at the beginning of the year.",
        "Accumulated depreciation at the beginning (land is 0).",
        "",
        "Section: Movements during the year.",
        "Additions: new assets purchased during the year.",
        "Disposals at carrying value: cost minus accumulated depreciation of disposed assets.",
        "Depreciation: annual depreciation charge (land & buildings = 0).",
        "",
        "Carrying value at end = Opening CV + Additions - Disposals CV - Depreciation.",
        "Cost of assets at the end of the year.",
        "Accumulated depreciation at the end of the year.",
    ]
    _attach_row_hints(cell_hints=cell_hints, rows_values=rows, explanations=row_expl, col_index=3)

    prompt = "Companies — Tangible/Fixed Assets Note (Financial Statements & Notes)\n\nPrepare the Fixed Assets Note in the given format."

    q = _mk_fixed_assets_note_table(
        prompt=prompt,
        title_fields=[
            {"label": "TANGIBLE/FIXED ASSETS NOTE", "value": ""},
            {"label": "Name of company", "value": company},
            {"label": "At", "value": fy_end},
        ],
        values_rows=rows,
        difficulty=difficulty,
        mode=mode,
        cell_hints=cell_hints,
        base_editable_cols=([1, 2, 3] if not omit_label_rows else [0, 1, 2, 3]),
    )

    q["meta"] = {
        "lb_cost_open": lb_cost_open,
        "lb_cv_open": lb_cv_open,
        "lb_additions": lb_additions,
        "lb_cv_close": lb_cv_close,
        "v_cost_open": v_cost_open,
        "v_acc_dep_open": v_acc_dep_open,
        "v_cv_open": v_cv_open,
        "v_additions": v_additions,
        "v_disposals_cv": v_disposals_cv,
        "v_depreciation": v_depreciation,
        "v_cv_close": v_cv_close,
        "t_cv_close": t_cv_close,
        "archetype_key": "g12_fs_fixed_assets_note",
    }
    return q


def _make_trade_payables_note(*, r: random.Random, difficulty: str, mode: str) -> Dict[str, Any]:
    company, fy_end = _pick_company(r)

    trade_creditors = float(r.choice([487_300, 350_000, 520_000]))
    expenses_accrued = float(r.choice([7_200, 12_000, 5_500]))
    income_received_advance = float(r.choice([0.0, 14_520, 8_000]))
    shareholders_dividends = float(r.choice([266_000, 180_000, 320_000]))
    sars_income_tax = float(r.choice([0.0, 25_000, 40_000]))
    creditors_salaries = float(r.choice([12_300, 8_000, 15_000]))
    uif = float(r.choice([2_500, 1_800, 3_200]))
    pension_fund = float(r.choice([18_000, 12_000, 24_000]))
    medical_aid = float(r.choice([0.0, 6_000, 8_500]))

    total = _round_money(
        trade_creditors + expenses_accrued + income_received_advance
        + shareholders_dividends + sars_income_tax + creditors_salaries
        + uif + pension_fund + medical_aid
    )

    rows: List[List[Optional[str]]] = []
    rows.append(["Trade creditors", _money(trade_creditors)])
    rows.append(["Expenses accrued (payable)", _money(expenses_accrued)])
    if income_received_advance > 0:
        rows.append(["Income received in advance", _money(income_received_advance)])
    rows.append(["Shareholders for dividends", _money(shareholders_dividends)])
    if sars_income_tax > 0:
        rows.append(["SARS (income tax)", _money(sars_income_tax)])
    rows.append(["Creditors for salaries", _money(creditors_salaries)])
    rows.append(["Unemployment insurance fund", _money(uif)])
    rows.append(["Pension fund", _money(pension_fund)])
    if medical_aid > 0:
        rows.append(["Medical aid fund", _money(medical_aid)])
    rows.append(["Trade and other payables", _money(total)])

    omit_label_rows: List[int] = []
    if _should_omit_labels(difficulty=difficulty, mode=mode):
        omit_labels = [
            "Trade and other payables",
        ]
        omit_label_rows = _apply_label_omissions(rows_values=rows, labels_to_omit=omit_labels, label_col_index=0)

    cell_hints: Dict[str, str] = {}
    hint_list = [
        "Trade creditors: amounts owed to suppliers.",
        "Expenses accrued: expenses incurred but not yet paid.",
        "Income received in advance: income received for future periods.",
        "Shareholders for dividends: dividends declared but not yet paid (final dividend).",
        "SARS (income tax): amount still owing to SARS.",
        "Creditors for salaries: gross salaries less deductions.",
        "UIF: deductions + employer contributions.",
        "Pension fund: deductions + employer contributions.",
        "Medical aid fund: deductions + employer contributions.",
        "Total transferred to current liabilities section of the Balance Sheet.",
    ]
    # Attach hints to actual rows (some rows may be conditionally omitted)
    for rix in range(len(rows)):
        if rix < len(hint_list):
            cell_hints[f"t0_r{rix}_c1"] = hint_list[min(rix, len(hint_list) - 1)]

    prompt = "Companies — Trade and Other Payables Note (Financial Statements & Notes)\n\nPrepare the Trade and Other Payables Note in the given format."

    q = _mk_retained_income_note_table(
        prompt=prompt,
        title_fields=[
            {"label": "TRADE AND OTHER PAYABLES NOTE", "value": ""},
            {"label": "Name of company", "value": company},
            {"label": "At", "value": fy_end},
        ],
        values_rows=rows,
        difficulty=difficulty,
        mode=mode,
        cell_hints=cell_hints,
        base_editable_cols=([1] if not omit_label_rows else [0, 1]),
    )

    q["id"] = _make_id("acct12_trade_payables_note")
    q["meta"] = {
        "trade_creditors": trade_creditors,
        "expenses_accrued": expenses_accrued,
        "income_received_advance": income_received_advance,
        "shareholders_dividends": shareholders_dividends,
        "sars_income_tax": sars_income_tax,
        "creditors_salaries": creditors_salaries,
        "uif": uif,
        "pension_fund": pension_fund,
        "medical_aid": medical_aid,
        "total": total,
        "archetype_key": "g12_fs_trade_payables_note",
    }
    return q


def _make_cash_flow_statement(*, r: random.Random, difficulty: str, mode: str) -> Dict[str, Any]:
    company, fy_end = _pick_company(r)

    # --- Note 1: Reconciliation between profit before tax and cash generated from operations ---
    profit_before_tax = float(r.choice([30_000, 541_960, 250_000, 420_000]))
    depreciation = float(r.choice([12_000, 148_800, 65_000, 95_000]))
    interest_expense = float(r.choice([9_200, 137_500, 42_800, 75_000]))
    adjustments_total = _round_money(depreciation + interest_expense)
    op_profit_before_wc = _round_money(profit_before_tax + adjustments_total)

    inventory_change = float(r.choice([-3_000, -15_000, 5_000, -8_000]))
    debtors_change = float(r.choice([5_600, -12_000, 8_000, -4_500]))
    creditors_change = float(r.choice([2_400, 7_500, -3_000, 12_000]))
    wc_changes = _round_money(inventory_change + debtors_change + creditors_change)
    cash_generated = _round_money(op_profit_before_wc + wc_changes)

    # --- Main Cash Flow Statement ---
    income_tax_paid = float(r.choice([150_285, 176_240, 93_640, 120_000]))
    dividends_paid = float(r.choice([140_000, 266_000, 180_000, 95_000]))

    cash_from_operations = _round_money(cash_generated - income_tax_paid - dividends_paid)

    # Investing activities
    fixed_assets_purchased = float(r.choice([120_000, 250_000, 48_000, 180_000]))
    fixed_assets_sold = float(r.choice([0.0, 35_000, 80_000]))
    fixed_deposit_change = float(r.choice([-5_000, -20_000, 10_000, 0.0]))
    cash_from_investing = _round_money(fixed_assets_sold - fixed_assets_purchased + fixed_deposit_change)

    # Financing activities
    shares_issued_proceeds = float(r.choice([79_600, 380_000, 0.0, 150_000]))
    shares_repurchased_cost = float(r.choice([0.0, 24_600, 180_000, 0.0]))
    loan_repayments = float(r.choice([6_000, 48_000, 105_600, 36_000]))
    cash_from_financing = _round_money(shares_issued_proceeds - shares_repurchased_cost - loan_repayments)

    net_change_cash = _round_money(cash_from_operations + cash_from_investing + cash_from_financing)
    cash_opening = float(r.choice([12_040, 35_300, 8_450, 25_000]))
    cash_closing = _round_money(cash_opening + net_change_cash)

    # --- Build Note 1 rows (reconciliation) ---
    note1_rows: List[List[Optional[str]]] = []
    note1_rows.append(["Profit before tax", "", _money(profit_before_tax)])
    note1_rows.append(["Adjustments i.r.o.:", "", _money(adjustments_total)])
    note1_rows.append(["  Depreciation", "", _money(depreciation)])
    note1_rows.append(["  Interest expense", "", _money(interest_expense)])
    note1_rows.append(["Operating profit before changes in working capital", "", _money(op_profit_before_wc)])
    note1_rows.append(["Changes in working capital", "", _money(wc_changes)])

    inv_label = f"{'(Increase)' if inventory_change < 0 else 'Decrease'} in inventory"
    note1_rows.append([f"  {inv_label}", "", _money(inventory_change) if inventory_change >= 0 else f"({_money(abs(inventory_change))})"])

    deb_label = f"{'(Increase)' if debtors_change < 0 else 'Decrease'} in debtors"
    note1_rows.append([f"  {deb_label}", "", _money(debtors_change) if debtors_change >= 0 else f"({_money(abs(debtors_change))})"])

    cred_label = f"{'Increase' if creditors_change >= 0 else '(Decrease)'} in creditors"
    note1_rows.append([f"  {cred_label}", "", _money(creditors_change) if creditors_change >= 0 else f"({_money(abs(creditors_change))})"])

    note1_rows.append(["Cash generated from operations", "", _money(cash_generated)])

    note1_hints: Dict[str, str] = {}
    note1_expl = [
        "Profit before tax: taken from the Income Statement.",
        "Adjustments: add back non-cash items and interest.",
        "Depreciation: non-cash expense, add back.",
        "Interest expense: add back (shown separately in CFS).",
        "Operating profit before working capital changes.",
        "Changes in working capital: current assets and liabilities movements.",
        "(Increase)/Decrease in inventory: increase = cash outflow (brackets).",
        "(Increase)/Decrease in debtors: increase = cash outflow (brackets).",
        "Increase/(Decrease) in creditors: increase = cash inflow.",
        "Cash generated from operations: operating profit adjusted for working capital.",
    ]
    _attach_row_hints(cell_hints=note1_hints, rows_values=note1_rows, explanations=note1_expl, col_index=2)

    note1_omit: List[int] = []
    if _should_omit_labels(difficulty=difficulty, mode=mode):
        note1_omit_labels = [
            "Operating profit before changes in working capital",
            "Cash generated from operations",
        ]
        note1_omit = _apply_label_omissions(rows_values=note1_rows, labels_to_omit=note1_omit_labels, label_col_index=0)

    note1_q = _mk_income_statement_table(
        prompt="Note 1: Reconciliation between profit before tax and cash generated from operations",
        title_fields=[
            {"label": "NOTE 1", "value": "Reconciliation"},
            {"label": "Name of company", "value": company},
        ],
        values_rows=note1_rows,
        difficulty=difficulty,
        mode=mode,
        cell_hints=note1_hints,
        base_editable_cols=([2] if not note1_omit else [0, 2]),
    )
    note1_q["meta"] = {"archetype_key": "g12_fs_cfs_note1_reconciliation"}

    # --- Build main CFS rows ---
    cfs_rows: List[List[Optional[str]]] = []
    cfs_rows.append(["CASH FLOW FROM OPERATING ACTIVITIES", "", ""])
    cfs_rows.append(["Cash generated from operations (Note 1)", "", _money(cash_generated)])
    cfs_rows.append(["Income tax paid", "", f"({_money(income_tax_paid)})"])
    cfs_rows.append(["Dividends paid", "", f"({_money(dividends_paid)})"])
    cfs_rows.append(["Cash from operating activities", "", _money(cash_from_operations)])
    cfs_rows.append(["", "", ""])
    cfs_rows.append(["CASH FLOW FROM INVESTING ACTIVITIES", "", ""])
    cfs_rows.append(["Fixed assets purchased", "", f"({_money(fixed_assets_purchased)})"])
    if fixed_assets_sold > 0:
        cfs_rows.append(["Proceeds from sale of fixed assets", "", _money(fixed_assets_sold)])
    if fixed_deposit_change != 0:
        fd_label = "Increase in fixed deposit" if fixed_deposit_change < 0 else "Decrease in fixed deposit"
        cfs_rows.append([fd_label, "", _money(abs(fixed_deposit_change)) if fixed_deposit_change > 0 else f"({_money(abs(fixed_deposit_change))})"])
    cfs_rows.append(["Cash from investing activities", "", _money(cash_from_investing) if cash_from_investing >= 0 else f"({_money(abs(cash_from_investing))})"])
    cfs_rows.append(["", "", ""])
    cfs_rows.append(["CASH FLOW FROM FINANCING ACTIVITIES", "", ""])
    if shares_issued_proceeds > 0:
        cfs_rows.append(["Proceeds from shares issued", "", _money(shares_issued_proceeds)])
    if shares_repurchased_cost > 0:
        cfs_rows.append(["Shares repurchased", "", f"({_money(shares_repurchased_cost)})"])
    cfs_rows.append(["Loan repayments", "", f"({_money(loan_repayments)})"])
    cfs_rows.append(["Cash from financing activities", "", _money(cash_from_financing) if cash_from_financing >= 0 else f"({_money(abs(cash_from_financing))})"])
    cfs_rows.append(["", "", ""])
    cfs_rows.append(["Net change in cash and cash equivalents", "", _money(net_change_cash) if net_change_cash >= 0 else f"({_money(abs(net_change_cash))})"])
    cfs_rows.append(["Cash and cash equivalents at beginning of year", "", _money(cash_opening)])
    cfs_rows.append(["Cash and cash equivalents at end of year", "", _money(cash_closing) if cash_closing >= 0 else f"({_money(abs(cash_closing))})"])

    cfs_hints: Dict[str, str] = {}
    cfs_expl_map = {
        "CASH FLOW FROM OPERATING ACTIVITIES": "Operating activities: day-to-day business cash flows.",
        "Cash generated from operations (Note 1)": "From Note 1 reconciliation.",
        "Income tax paid": "Cash outflow: tax paid to SARS (show in brackets).",
        "Dividends paid": "Cash outflow: dividends paid to shareholders (show in brackets).",
        "Cash from operating activities": "Net cash from operating activities.",
        "CASH FLOW FROM INVESTING ACTIVITIES": "Investing activities: buying/selling long-term assets.",
        "Fixed assets purchased": "Cash outflow: assets bought (show in brackets).",
        "Proceeds from sale of fixed assets": "Cash inflow: proceeds from asset sales.",
        "Cash from investing activities": "Net cash from investing activities.",
        "CASH FLOW FROM FINANCING ACTIVITIES": "Financing activities: shares and loans.",
        "Proceeds from shares issued": "Cash inflow: money received from issuing shares.",
        "Shares repurchased": "Cash outflow: cost of buying back shares (show in brackets).",
        "Loan repayments": "Cash outflow: capital repayments on loans (show in brackets).",
        "Cash from financing activities": "Net cash from financing activities.",
        "Net change in cash and cash equivalents": "Sum of operating + investing + financing cash flows.",
        "Cash and cash equivalents at beginning of year": "Opening cash balance from previous year.",
        "Cash and cash equivalents at end of year": "Closing cash = opening + net change. Must agree with Balance Sheet.",
    }
    for rix, row in enumerate(cfs_rows):
        label = str(row[0] or "").strip()
        if label in cfs_expl_map:
            cfs_hints[f"t0_r{rix}_c2"] = cfs_expl_map[label]

    cfs_omit: List[int] = []
    if _should_omit_labels(difficulty=difficulty, mode=mode):
        cfs_omit_labels = [
            "Cash from operating activities",
            "Cash from investing activities",
            "Cash from financing activities",
            "Net change in cash and cash equivalents",
            "Cash and cash equivalents at end of year",
        ]
        cfs_omit = _apply_label_omissions(rows_values=cfs_rows, labels_to_omit=cfs_omit_labels, label_col_index=0)

    cfs_q = _mk_income_statement_table(
        prompt="Companies — Cash Flow Statement (Financial Statements & Notes)\n\nPrepare the Cash Flow Statement in the given format.",
        title_fields=[
            {"label": "CASH FLOW STATEMENT", "value": ""},
            {"label": "Name of company", "value": company},
            {"label": "For the year ended", "value": fy_end},
        ],
        values_rows=cfs_rows,
        difficulty=difficulty,
        mode=mode,
        cell_hints=cfs_hints,
        base_editable_cols=([2] if not cfs_omit else [0, 2]),
    )
    cfs_q["meta"] = {"archetype_key": "g12_fs_cash_flow_statement"}

    # Bundle: Note 1 + CFS
    prompt_bundle = (
        "Companies — Cash Flow Statement with Notes (Financial Statements & Notes)\n\n"
        "Prepare Note 1 (Reconciliation) and the Cash Flow Statement."
    )
    return _make_bundle(
        prompt=prompt_bundle,
        parts=[note1_q, cfs_q],
        archetype_key="g12_fs_cash_flow_statement_bundle",
    )


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

    builders: List[Any] = [
        lambda: _make_company_income_statement(r=r, difficulty=difficulty, mode=mode),
        lambda: _make_example2_statement_of_comprehensive_income(r=r, difficulty=difficulty, mode=mode),
        lambda: _make_retained_income_note(r=r, difficulty=difficulty, mode=mode),
        lambda: _make_balance_sheet(r=r, difficulty=difficulty, mode=mode),
        lambda: _mk_trade_receivables_note(r=r, difficulty=difficulty, mode=mode),
        lambda: _make_example3_retained_note_and_balance_sheet_bundle(r=r, difficulty=difficulty, mode=mode),
        lambda: _make_fixed_assets_note(r=r, difficulty=difficulty, mode=mode),
        lambda: _make_trade_payables_note(r=r, difficulty=difficulty, mode=mode),
        lambda: _make_cash_flow_statement(r=r, difficulty=difficulty, mode=mode),
    ]

    if subskill_norm in {"income-statement", "income_statement", "income"}:
        builders = [builders[0]]
    elif subskill_norm in {"statement-of-comprehensive-income", "sci", "comprehensive-income"}:
        builders = [builders[1]]
    elif subskill_norm in {"retained-income-note", "retained_income_note", "retained"}:
        builders = [builders[2]]
    elif subskill_norm in {"balance-sheet", "balance_sheet", "statement-of-financial-position", "sfp"}:
        builders = [builders[3]]
    elif subskill_norm in {"trade-receivables-note", "trade_receivables_note", "receivables-note"}:
        builders = [builders[4]]
    elif subskill_norm in {"example3", "example-3", "example3-bundle", "bundle"}:
        builders = [builders[5]]
    elif subskill_norm in {"fixed-assets-note", "fixed_assets_note", "tangible-assets-note"}:
        builders = [builders[6]]
    elif subskill_norm in {"trade-payables-note", "trade_payables_note", "payables-note"}:
        builders = [builders[7]]
    elif subskill_norm in {"cash-flow-statement", "cash_flow_statement", "cfs", "cash-flow"}:
        builders = [builders[8]]

    out: List[Dict[str, Any]] = []
    for _ in range(n):
        out.append(r.choice(builders)())
    return out
