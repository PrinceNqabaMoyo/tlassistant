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


def _mk_income_statement_table(
    *,
    prompt: str,
    title_fields: List[Dict[str, Any]],
    values_rows: List[List[Optional[str]]],
    difficulty: str,
    mode: str,
    cell_hints: Optional[Dict[str, str]] = None,
) -> Dict[str, Any]:
    headers = ["Item", "Note", "Amount"]

    diff = str(difficulty or "easy").strip().lower()
    mode_norm = str(mode or "").strip().lower()
    show_answers = mode_norm == "scaffold"

    base_editable_cols = [2]
    editable_cols = _journal_editable_cols_by_difficulty(
        difficulty=diff,
        base_editable_cols=base_editable_cols,
        total_cols=len(headers),
        mode=mode_norm,
    )

    rows: List[List[Dict[str, Any]]] = []
    correct_map: Dict[str, Any] = {}

    for rix, vals in enumerate(values_rows):
        display = vals if show_answers else ["" for _ in range(len(vals))]
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
        cell_hints=cell_hints if mode_norm == "scaffold" and cell_hints else None,
    )
    out["id"] = _make_id("acct12_financial_statements")
    out["expected_answer_type"] = "journal"
    return out


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

    cell_hints: Dict[str, str] = {}
    if str(mode or "").strip().lower() == "scaffold":
        cell_hints["t0_r0_c2"] = "Net sales = Sales - Debtors allowances."
        cell_hints["t0_r1_c2"] = "Cost of sales is an expense and is shown in brackets."
        cell_hints["t0_r2_c2"] = "Gross profit = Net sales - Cost of sales."
        cell_hints["t0_r8_c2"] = "Directors' fees: add outstanding fees to the pre-adjustment amount."
        cell_hints["t0_r20_c2"] = "Finance cost can be calculated from the loan statement (interest capitalised)."
        cell_hints["t0_r-1_c0"] = ""  # placeholder

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

def _mk_retained_income_note_table(
    *,
    prompt: str,
    title_fields: List[Dict[str, Any]],
    values_rows: List[List[Optional[str]]],
    difficulty: str,
    mode: str,
    cell_hints: Optional[Dict[str, str]] = None,
) -> Dict[str, Any]:
    headers = ["Details", "Amount"]

    diff = str(difficulty or "easy").strip().lower()
    mode_norm = str(mode or "").strip().lower()
    show_answers = mode_norm == "scaffold"

    base_editable_cols = [1]
    editable_cols = _journal_editable_cols_by_difficulty(
        difficulty=diff,
        base_editable_cols=base_editable_cols,
        total_cols=len(headers),
        mode=mode_norm,
    )

    rows: List[List[Dict[str, Any]]] = []
    correct_map: Dict[str, Any] = {}

    for rix, vals in enumerate(values_rows):
        display = vals if show_answers else ["" for _ in range(len(vals))]
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

    cell_hints: Dict[str, str] = {}
    if str(mode or "").strip().lower() == "scaffold":
        cell_hints["t0_r0_c1"] = "Opening balance from previous year's balance sheet."
        cell_hints["t0_r1_c1"] = "Net profit after tax from the Income Statement."
        cell_hints["t0_r2_c1"] = "Total dividends paid/payable for the year."
        cell_hints["t0_r3_c1"] = "Breakdown of ordinary share dividends."
        cell_hints["t0_r4_c1"] = f"Buyback premium = {shares_repurchased:,} shares × R{buyback_premium_per_share:.2f} = R{total_buyback_premium:,.2f}"
        cell_hints["t0_r6_c1"] = "Closing balance = Opening + NPAT - Dividends - Buyback premium"

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
) -> Dict[str, Any]:
    headers = ["Details", "Note", "Amount"]

    diff = str(difficulty or "easy").strip().lower()
    mode_norm = str(mode or "").strip().lower()
    show_answers = mode_norm == "scaffold"

    base_editable_cols = [2]
    editable_cols = _journal_editable_cols_by_difficulty(
        difficulty=diff,
        base_editable_cols=base_editable_cols,
        total_cols=len(headers),
        mode=mode_norm,
    )

    rows: List[List[Dict[str, Any]]] = []
    correct_map: Dict[str, Any] = {}

    for rix, vals in enumerate(values_rows):
        display = vals if show_answers else ["" for _ in range(len(vals))]
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

    cell_hints: Dict[str, str] = {}
    if str(mode or "").strip().lower() == "scaffold":
        cell_hints["t0_r2_c2"] = "Fixed/Tangible assets = Carrying value of all fixed assets."
        cell_hints["t0_r9_c2"] = "Current assets = Inventories + Receivables + Cash."
        cell_hints["t0_r13_c2"] = "Total assets must equal Total equity + liabilities."
        cell_hints["t0_r14_c2"] = ""  # EQUITY AND LIABILITIES header
        cell_hints["t0_r15_c2"] = "Shareholders' equity = Share capital + Retained income."
        cell_hints["t0_r20_c2"] = "Non-current liabilities = Loan less current portion."
        cell_hints["t0_r24_c2"] = "Current liabilities = Total equity + liabilities - Equity - Non-current liabilities."

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

    cell_hints: Dict[str, str] = {}
    if str(mode or "").strip().lower() == "scaffold":
        cell_hints["t0_r0_c1"] = "Gross trade debtors before provision."
        cell_hints["t0_r1_c1"] = "Deduct provision for bad debts."
        cell_hints["t0_r2_c1"] = "Net trade debtors = Gross - Provision."
        cell_hints["t0_r3_c1"] = "SARS income tax receivable/overpaid."
        cell_hints["t0_r4_c1"] = "Prepaid expenses (expenses paid in advance)."

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

    # Support multiple archetype keys
    out: List[Dict[str, Any]] = []
    for i in range(n):
        # Rotate through available archetypes
        archetype_index = i % 4
        if archetype_index == 0:
            out.append(_make_company_income_statement(r=r, difficulty=difficulty, mode=mode))
        elif archetype_index == 1:
            out.append(_make_retained_income_note(r=r, difficulty=difficulty, mode=mode))
        elif archetype_index == 2:
            out.append(_make_balance_sheet(r=r, difficulty=difficulty, mode=mode))
        else:
            out.append(_mk_trade_receivables_note(r=r, difficulty=difficulty, mode=mode))

    return out
