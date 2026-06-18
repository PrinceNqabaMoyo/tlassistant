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
    guidelines: Optional[List[str]] = None,
    archetype_key: Optional[str] = None,
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
        display = vals if show_answers else ["" for _ in range(len(vals))]
        rows.append(_build_prefixed_row(table_index=0, row_index=rix, values=display, editable_cols=editable_cols))
        for cix, v0 in enumerate(vals):
            correct_map[f"t0_r{int(rix)}_c{int(cix)}"] = "" if v0 is None else str(v0)

    default_guidelines = [
        "Enter amounts in the correct column.",
        "Use the appropriate source document abbreviations.",
        "Calculate totals correctly.",
    ]

    out = _make_journal(
        prompt=prompt,
        journal_type=journal_type,
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        guidelines=guidelines if guidelines else default_guidelines,
        table_variant="grade_project",
        title_fields=title_fields if title_fields else [{"label": "", "value": ""}],
        cell_hints=cell_hints if mode_norm == "scaffold" and cell_hints else None,
    )
    out["id"] = _make_id("acct11_ct")
    if archetype_key:
        out["meta"] = {"archetype_key": archetype_key}
    return out


def _make_crj_format(*, r: random.Random, difficulty: str, mode: str) -> Dict[str, Any]:
    """Grade 11 Controlled Test - Cash Receipts Journal format."""
    business = r.choice(["Mamba Traders", "Baloyi Stores", "Tshabalala Traders"])
    month = r.choice(["January", "February", "March", "May"])
    year = int(r.choice([2024, 2025, 2023]))

    # CRJ columns: Doc, Day, Details, Fol, Analysis of receipts, Bank, Sales, Cost of Sales, Debtors' Control, Discount allowed, Sundry Accounts [Amount, Fol, Details]
    headers = [
        "Doc",
        "Day",
        "Details",
        "Fol",
        "Analysis of receipts",
        "Bank",
        "Sales",
        "Cost of sales",
        "Debtors' Control",
        "Discount allowed",
        "Sundry Accounts",
    ]

    # Generate sample transactions
    transactions = []
    days = r.sample(range(1, 28), k=4)
    days.sort()

    # Cash sales (CRR)
    sales_amount = float(r.choice([2500, 4800, 6500, 3200]))
    cost_of_sales = _round_money(sales_amount * 0.6)  # 60% cost
    transactions.append({
        "doc": "CRR",
        "day": days[0],
        "details": "Sales",
        "fol": "",
        "analysis": "",
        "bank": sales_amount,
        "sales": sales_amount,
        "cost_of_sales": cost_of_sales,
        "debtors_control": 0,
        "discount": 0,
        "sundry": "",
    })

    # Debtor payment (receipt)
    debtor_name = r.choice(["B. Mokoena", "K. Ndlovu", "S. Peters"])
    receipt_no = int(r.choice([101, 102, 103, 104]))
    payment = float(r.choice([1200, 2400, 1800, 3600]))
    discount = _round_money(payment * 0.05)  # 5% discount
    transactions.append({
        "doc": f"{receipt_no}",
        "day": days[1],
        "details": debtor_name,
        "fol": "",
        "analysis": "",
        "bank": payment,
        "sales": 0,
        "cost_of_sales": 0,
        "debtors_control": payment,
        "discount": discount,
        "sundry": "",
    })

    # Rent received (sundry)
    rent = float(r.choice([1500, 2000, 2500]))
    transactions.append({
        "doc": f"{receipt_no + 1}",
        "day": days[2],
        "details": "Rent received",
        "fol": "",
        "analysis": "",
        "bank": rent,
        "sales": 0,
        "cost_of_sales": 0,
        "debtors_control": 0,
        "discount": 0,
        "sundry": f"R{_money(rent)}",
    })

    # Another cash sale
    sales2 = float(r.choice([1800, 4200, 5500]))
    cost2 = _round_money(sales2 * 0.6)
    transactions.append({
        "doc": "CRR",
        "day": days[3],
        "details": "Sales",
        "fol": "",
        "analysis": "",
        "bank": sales2,
        "sales": sales2,
        "cost_of_sales": cost2,
        "debtors_control": 0,
        "discount": 0,
        "sundry": "",
    })

    # Build rows
    rows: List[List[Optional[str]]] = []
    rows.append([f"CASH RECEIPTS JOURNAL of {business} for {month} {year}", "", "", "", "", "", "", "", "", "", ""])

    for t in transactions:
        rows.append([
            t["doc"],
            str(t["day"]),
            t["details"],
            t["fol"],
            t["analysis"],
            _money(t["bank"]) if t["bank"] else "",
            _money(t["sales"]) if t["sales"] else "",
            _money(t["cost_of_sales"]) if t["cost_of_sales"] else "",
            _money(t["debtors_control"]) if t["debtors_control"] else "",
            _money(t["discount"]) if t["discount"] else "",
            t["sundry"],
        ])

    # Totals row
    total_bank = _round_money(sum(t["bank"] for t in transactions))
    total_sales = _round_money(sum(t["sales"] for t in transactions))
    total_cost = _round_money(sum(t["cost_of_sales"] for t in transactions))
    total_debtors = _round_money(sum(t["debtors_control"] for t in transactions))
    total_discount = _round_money(sum(t["discount"] for t in transactions))

    rows.append([
        "",
        "",
        "",
        "",
        "Totals",
        _money(total_bank),
        _money(total_sales),
        _money(total_cost),
        _money(total_debtors),
        _money(total_discount),
        "",
    ])

    cell_hints: Dict[str, str] = {}
    if str(mode or "").strip().lower() == "scaffold":
        cell_hints["t0_r0_c0"] = "CRJ header with business name and period."
        cell_hints["t0_r1_c0"] = "Cash sales use 'CRR' as source document."
        cell_hints["t0_r2_c0"] = "Debtor receipts use receipt numbers."
        cell_hints["t0_r3_c0"] = "Other receipts (rent/commission) go to Sundry Accounts."
        cell_hints["t0_r5_c0"] = "Verify totals balance correctly."

    prompt = "Controlled Test — Cash Receipts Journal (CRJ)\n\nEnter the transactions in the CRJ format."

    return _mk_journal(
        prompt=prompt,
        journal_type="crj_format",
        headers=headers,
        values_rows=rows,
        difficulty=difficulty,
        mode=mode,
        base_editable_cols=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        guidelines=[
            "Use 'CRR' for cash sales source documents.",
            "Use receipt numbers for debtor payments and other receipts.",
            "Enter amounts in the correct column.",
            "Calculate Cost of Sales as 60% of Sales (if applicable).",
            "Discount allowed is recorded separately from bank amount.",
        ],
        cell_hints=cell_hints,
        archetype_key="g11_ct1_q2_crj_format",
    )


def _make_cpj_format(*, r: random.Random, difficulty: str, mode: str) -> Dict[str, Any]:
    """Grade 11 Controlled Test - Cash Payments Journal format."""
    business = r.choice(["Mamba Traders", "Baloyi Stores", "Tshabalala Traders"])
    month = r.choice(["January", "February", "March", "May"])
    year = int(r.choice([2024, 2025, 2023]))

    # CPJ columns: Doc, Day, Details, Bank, Trading Stock, Wages, Creditors' Control, Discount received, Sundry Accounts
    headers = [
        "Doc",
        "Day",
        "Details",
        "Bank",
        "Trading Stock",
        "Wages",
        "Creditors' Control",
        "Discount received",
        "Sundry Accounts",
    ]

    # Generate sample transactions
    transactions = []
    days = r.sample(range(1, 28), k=4)
    days.sort()

    cheque_nos = r.sample(["001", "002", "003", "004", "005"], k=4)

    # Cash purchase of trading stock
    stock_purchase = float(r.choice([1500, 2500, 3200, 4800]))
    transactions.append({
        "doc": cheque_nos[0],
        "day": days[0],
        "details": "Cash purchase",
        "bank": stock_purchase,
        "trading_stock": stock_purchase,
        "wages": 0,
        "creditors": 0,
        "discount": 0,
        "sundry": "",
    })

    # Wages paid
    wages = float(r.choice([800, 1200, 1500, 2000]))
    transactions.append({
        "doc": cheque_nos[1],
        "day": days[1],
        "details": "Wages",
        "bank": wages,
        "trading_stock": 0,
        "wages": wages,
        "creditors": 0,
        "discount": 0,
        "sundry": "",
    })

    # Creditor payment with discount
    creditor = r.choice(["ABC Suppliers", "XYZ Traders", "Debtors Control"])
    payment = float(r.choice([2000, 3500, 4800]))
    discount = _round_money(payment * 0.05)
    bank_paid = _round_money(payment - discount)
    transactions.append({
        "doc": cheque_nos[2],
        "day": days[2],
        "details": creditor,
        "bank": bank_paid,
        "trading_stock": 0,
        "wages": 0,
        "creditors": payment,
        "discount": discount,
        "sundry": "",
    })

    # Drawings/other sundry
    drawings = float(r.choice([500, 1000, 1500]))
    transactions.append({
        "doc": cheque_nos[3],
        "day": days[3],
        "details": "Drawings",
        "bank": drawings,
        "trading_stock": 0,
        "wages": 0,
        "creditors": 0,
        "discount": 0,
        "sundry": f"R{_money(drawings)}",
    })

    # Build rows
    rows: List[List[Optional[str]]] = []
    rows.append([f"CASH PAYMENTS JOURNAL of {business} for {month} {year}", "", "", "", "", "", "", "", ""])

    for t in transactions:
        rows.append([
            t["doc"],
            str(t["day"]),
            t["details"],
            _money(t["bank"]),
            _money(t["trading_stock"]) if t["trading_stock"] else "",
            _money(t["wages"]) if t["wages"] else "",
            _money(t["creditors"]) if t["creditors"] else "",
            _money(t["discount"]) if t["discount"] else "",
            t["sundry"],
        ])

    # Totals row
    total_bank = _round_money(sum(t["bank"] for t in transactions))
    total_stock = _round_money(sum(t["trading_stock"] for t in transactions))
    total_wages = _round_money(sum(t["wages"] for t in transactions))
    total_creditors = _round_money(sum(t["creditors"] for t in transactions))
    total_discount = _round_money(sum(t["discount"] for t in transactions))

    rows.append([
        "",
        "",
        "Totals",
        _money(total_bank),
        _money(total_stock),
        _money(total_wages),
        _money(total_creditors),
        _money(total_discount),
        "",
    ])

    cell_hints: Dict[str, str] = {}
    if str(mode or "").strip().lower() == "scaffold":
        cell_hints["t0_r0_c0"] = "CPJ header with business name and period."
        cell_hints["t0_r1_c0"] = "Cash purchases go to Trading Stock and Bank columns."
        cell_hints["t0_r2_c0"] = "Wages are recorded in Wages column."
        cell_hints["t0_r3_c0"] = "Creditor payments: full amount in Creditors' Control, discount in Discount received."
        cell_hints["t0_r4_c0"] = "Bank amount for creditors = Full amount - Discount received."
        cell_hints["t0_r5_c0"] = "Verify totals balance correctly."

    prompt = "Controlled Test — Cash Payments Journal (CPJ)\n\nEnter the transactions in the CPJ format."

    return _mk_journal(
        prompt=prompt,
        journal_type="cpj_format",
        headers=headers,
        values_rows=rows,
        difficulty=difficulty,
        mode=mode,
        base_editable_cols=[0, 1, 2, 3, 4, 5, 6, 7, 8],
        guidelines=[
            "Enter amounts in the correct column.",
            "For creditor payments: Creditors' Control = full amount, Bank = amount paid (less discount).",
            "Discount received reduces the bank payment but is recorded separately.",
            "Calculate totals for each column.",
        ],
        cell_hints=cell_hints,
        archetype_key="g11_ct1_q2_cpj_format",
    )


def _make_fixed_assets_timeline_calc(*, r: random.Random, difficulty: str, mode: str) -> Dict[str, Any]:
    """Grade 11 Controlled Test - Fixed Assets timeline calculations with monthly depreciation."""
    asset_types = ["Vehicle", "Equipment", "Machinery"]
    asset = r.choice(asset_types)
    business = r.choice(["Mamba Traders", "Baloyi Stores"])

    # Cost and depreciation rates
    cost_price = float(r.choice([180000, 240000, 320000, 150000]))
    dep_rate = float(r.choice([15, 20, 10]))  # % per annum

    # Purchase date (during the financial year)
    purchase_months = ["March", "June", "September", "November"]
    purchase_month = r.choice(purchase_months)

    # Months in use (for first year calculation)
    months_map = {"March": 12, "June": 9, "September": 6, "November": 4}
    months_in_use = months_map[purchase_month]

    # Financial year end
    fy_end = "28 February 2024"

    # Calculate depreciation
    annual_dep = cost_price * (dep_rate / 100)
    first_year_dep = _round_money((annual_dep / 12) * months_in_use)
    carrying_value = _round_money(cost_price - first_year_dep)

    # Build question data
    prompt = f"""Fixed Assets Calculation — {business}

A {asset.lower()} was purchased on 1 {purchase_month} 2023 for R{_money(cost_price)}.
The financial year ends on {fy_end}.
The asset is depreciated at {dep_rate}% per annum on cost price.

Calculate:
1. Depreciation for the first financial year
2. Carrying value at year-end
"""

    # Create a calculation question
    out: Dict[str, Any] = {
        "id": _make_id("acct11_fixed_assets_calc"),
        "question_type": "calc_multi",
        "prompt": prompt,
        "expected_answer_type": "number_multi",
        "parts": [
            {
                "label": "Depreciation for first year",
                "correct_value": float(first_year_dep),
                "unit": "R",
                "explanation": f"Annual depreciation = R{_money(cost_price)} × {dep_rate}% = R{_money(annual_dep)}. For {months_in_use} months: R{_money(annual_dep)} ÷ 12 × {months_in_use} = R{_money(first_year_dep)}" if str(mode or "").strip().lower() == "scaffold" else "",
            },
            {
                "label": "Carrying value at year-end",
                "correct_value": float(carrying_value),
                "unit": "R",
                "explanation": f"Carrying value = Cost - Accumulated depreciation = R{_money(cost_price)} - R{_money(first_year_dep)} = R{_money(carrying_value)}" if str(mode or "").strip().lower() == "scaffold" else "",
            },
        ],
        "meta": {
            "asset_type": asset,
            "cost_price": cost_price,
            "depreciation_rate_pct": dep_rate,
            "purchase_month": purchase_month,
            "months_in_use": months_in_use,
            "annual_depreciation": annual_dep,
            "first_year_depreciation": first_year_dep,
            "carrying_value": carrying_value,
            "archetype_key": "g11_ct1_q1_accdep_vehicles_timeline",
        },
    }

    return out


def _make_accdep_equipment_taccount(*, r: random.Random, difficulty: str, mode: str) -> Dict[str, Any]:
    """Grade 11 Controlled Test - Accumulated Depreciation on Equipment T-account."""
    business = r.choice(["Mamba Traders", "Baloyi Stores", "Tshabalala Traders"])
    fy_end = "28 February 2024"
    
    # Equipment details
    equipment_cost = float(r.choice([45000, 60000, 75000, 90000]))
    dep_rate = float(r.choice([10, 15, 20]))  # % per annum on cost
    
    # Opening balance (accumulated depreciation from previous years)
    years_accumulated = int(r.choice([2, 3, 4]))
    opening_balance = _round_money(equipment_cost * (dep_rate / 100) * years_accumulated)
    
    # Current year depreciation
    current_year_dep = _round_money(equipment_cost * (dep_rate / 100))
    closing_balance = _round_money(opening_balance + current_year_dep)
    
    # Build T-account structure
    prompt = f"""Ledger Account — {business}

Required: Prepare the Accumulated Depreciation on Equipment account for the year ended {fy_end}.

Information:
- Equipment cost price: R{_money(equipment_cost)}
- Depreciation rate: {dep_rate}% per annum on cost price
- Opening balance (1 March 2023): R{_money(opening_balance)}
"""
    
    # T-account format: Date, Details, Fol, Amount (Debit), Date, Details, Fol, Amount (Credit)
    headers = ["Date", "Details", "Fol", "Amount", "Date", "Details", "Fol", "Amount"]
    
    rows = [
        [f"Accumulated Depreciation on Equipment", "", "", "", "", "", "", ""],
        ["", "", "", "", f"1 Mar 2023", "Balance", "b/d", _money(opening_balance)],
        [f"28 Feb 2024", "Depreciation", "GJ", _money(current_year_dep), "", "", "", ""],
        ["", "", "", "", f"28 Feb 2024", "Balance", "c/d", _money(closing_balance)],
        ["", "", _money(closing_balance), "", "", "", _money(closing_balance), ""],
        [f"1 Mar 2024", "Balance", "b/d", _money(closing_balance), "", "", "", ""],
    ]
    
    cell_hints = {}
    if str(mode or "").strip().lower() == "scaffold":
        cell_hints["t0_r1_c7"] = "Opening balance brought down on credit side"
        cell_hints["t0_r2_c0"] = "Current year depreciation entry"
        cell_hints["t0_r2_c3"] = f"Annual depreciation = R{_money(equipment_cost)} × {dep_rate}% = R{_money(current_year_dep)}"
        cell_hints["t0_r3_c7"] = "Closing balance carried down"
        cell_hints["t0_r5_c0"] = "Opening balance for next year"
    
    return _mk_journal(
        prompt=prompt,
        journal_type="accdep_equipment_taccount",
        headers=headers,
        values_rows=rows,
        difficulty=difficulty,
        mode=mode,
        base_editable_cols=[0, 1, 2, 3, 4, 5, 6, 7],
        guidelines=[
            "Accumulated Depreciation is a negative asset (contra-asset) account.",
            "The opening balance appears on the credit side (Balance b/d).",
            "Current year depreciation is recorded on the credit side.",
            "Total credits = Opening + Current depreciation = Closing balance c/d.",
            "Always balance the account with Balance c/d on the smaller side.",
        ],
        cell_hints=cell_hints,
        archetype_key="g11_ct1_q3_accdep_taccount",
    )


def _make_asset_disposal_taccount(*, r: random.Random, difficulty: str, mode: str) -> Dict[str, Any]:
    """Grade 11 Controlled Test - Asset Disposal Account T-account."""
    business = r.choice(["Mamba Traders", "Baloyi Stores", "Tshabalala Traders"])
    fy_end = "28 February 2024"
    
    # Asset details
    asset_type = r.choice(["Equipment", "Vehicle", "Machinery"])
    cost_price = float(r.choice([80000, 120000, 150000]))
    dep_rate = float(r.choice([15, 20]))
    years_used = int(r.choice([2, 3, 4]))
    
    # Calculate accumulated depreciation
    accumulated_dep = _round_money(cost_price * (dep_rate / 100) * years_used)
    carrying_value = _round_money(cost_price - accumulated_dep)
    
    # Disposal details
    sold_for = _round_money(carrying_value * r.uniform(0.8, 1.3))
    profit_loss = _round_money(sold_for - carrying_value)
    profit_loss_label = "Profit on sale" if profit_loss >= 0 else "Loss on sale"
    
    # Build T-account
    prompt = f"""Ledger Account — {business}

Required: Prepare the Asset Disposal account for the disposal of {asset_type.lower()} on 31 December 2023.

Information:
- Cost price of {asset_type.lower()}: R{_money(cost_price)}
- Accumulated depreciation (31 Dec 2023): R{_money(accumulated_dep)}
- Carrying value: R{_money(carrying_value)}
- Sold for: R{_money(sold_for)}
- {profit_loss_label}: R{_money(abs(profit_loss))}
"""
    
    headers = ["Date", "Details", "Fol", "Amount", "Date", "Details", "Fol", "Amount"]
    
    rows = [
        [f"Asset Disposal", "", "", "", "", "", "", ""],
        [f"31 Dec 2023", f"{asset_type}", "", _money(cost_price), f"31 Dec 2023", "Acc Dep", "", _money(accumulated_dep)],
        ["", "", "", "", f"31 Dec 2023", "Bank/Debtors", "", _money(sold_for)],
        ["", "", "", "", f"31 Dec 2023", profit_loss_label, "", _money(abs(profit_loss))],
        ["", "", _money(cost_price), "", "", "", _money(cost_price), ""],
    ]
    
    cell_hints = {}
    if str(mode or "").strip().lower() == "scaffold":
        cell_hints["t0_r1_c3"] = "Cost price goes on debit side (removing the asset)"
        cell_hints["t0_r1_c7"] = "Accumulated depreciation goes on credit side (removing the contra-asset)"
        cell_hints["t0_r2_c7"] = "Amount received from sale"
        cell_hints["t0_r3_c7"] = f"{profit_loss_label} = Sold for R{_money(sold_for)} - Carrying value R{_money(carrying_value)} = R{_money(abs(profit_loss))}"
        cell_hints["t0_r3_c7"] = "Profit if sold > carrying value, Loss if sold < carrying value"
    
    return _mk_journal(
        prompt=prompt,
        journal_type="asset_disposal_taccount",
        headers=headers,
        values_rows=rows,
        difficulty=difficulty,
        mode=mode,
        base_editable_cols=[0, 1, 2, 3, 4, 5, 6, 7],
        guidelines=[
            "The Asset Disposal account is a temporary account to record asset disposals.",
            "Debit: Cost price of asset being removed.",
            "Credit: Accumulated depreciation of the disposed asset.",
            "Credit: Amount received from sale (Bank or Debtors).",
            "Difference = Profit (if credit) or Loss (if debit) on sale.",
        ],
        cell_hints=cell_hints,
        archetype_key="g11_ct1_q4_asset_disposal",
    )


def _make_fixed_assets_note(*, r: random.Random, difficulty: str, mode: str) -> Dict[str, Any]:
    """Grade 11 Controlled Test - Fixed Assets Note to Balance Sheet."""
    business = r.choice(["Mamba Traders", "Baloyi Stores"])
    fy_end = "28 February 2024"
    
    # Fixed asset categories
    land_buildings_cost = float(r.choice([250000, 350000, 450000]))
    vehicles_cost = float(r.choice([180000, 240000, 300000]))
    equipment_cost = float(r.choice([60000, 80000, 100000]))
    
    # Depreciation rates
    vehicles_dep_rate = 20  # %
    equipment_dep_rate = 15  # %
    
    # Opening balances (carrying values)
    vehicles_accdep_opening = _round_money(vehicles_cost * 0.4)  # 40% depreciated
    equipment_accdep_opening = _round_money(equipment_cost * 0.3)  # 30% depreciated
    
    vehicles_cv_opening = _round_money(vehicles_cost - vehicles_accdep_opening)
    equipment_cv_opening = _round_money(equipment_cost - equipment_accdep_opening)
    
    # Current year depreciation
    vehicles_dep = _round_money(vehicles_cv_opening * (vehicles_dep_rate / 100))
    equipment_dep = _round_money(equipment_cost * (equipment_dep_rate / 100))  # On cost
    
    # No disposals in this basic version
    vehicles_cv_closing = _round_money(vehicles_cv_opening - vehicles_dep)
    equipment_cv_closing = _round_money(equipment_cv_opening - equipment_dep)
    
    prompt = f"""Fixed Assets Note — {business}

Required: Complete the Fixed/Tangible Assets Note for the year ended {fy_end}.

Information:
- Land & Buildings: Cost R{_money(land_buildings_cost)} (not depreciated)
- Vehicles: Cost R{_money(vehicles_cost)}, Accumulated Depreciation (1 Mar) R{_money(vehicles_accdep_opening)}
- Equipment: Cost R{_money(equipment_cost)}, Accumulated Depreciation (1 Mar) R{_money(equipment_accdep_opening)}
- Depreciation: Vehicles {vehicles_dep_rate}% on diminishing balance, Equipment {equipment_dep_rate}% on cost
"""
    
    headers = ["", "Land & Buildings", "Vehicles", "Equipment"]
    
    rows = [
        ["Cost (1 March 2023)", _money(land_buildings_cost), _money(vehicles_cost), _money(equipment_cost)],
        ["Accumulated Depreciation (1 March 2023)", "—", _money(vehicles_accdep_opening), _money(equipment_accdep_opening)],
        ["Carrying Value (1 March 2023)", _money(land_buildings_cost), _money(vehicles_cv_opening), _money(equipment_cv_opening)],
        ["", "", "", ""],
        ["Movements:", "", "", ""],
        ["Additions at cost", "—", "—", "—"],
        ["Disposals at carrying value", "—", "—", "—"],
        ["Depreciation", "—", _money(vehicles_dep), _money(equipment_dep)],
        ["", "", "", ""],
        ["Cost (28 February 2024)", _money(land_buildings_cost), _money(vehicles_cost), _money(equipment_cost)],
        ["Accumulated Depreciation (28 Feb 2024)", "—", _money(_round_money(vehicles_accdep_opening + vehicles_dep)), _money(_round_money(equipment_accdep_opening + equipment_dep))],
        ["Carrying Value (28 February 2024)", _money(land_buildings_cost), _money(vehicles_cv_closing), _money(equipment_cv_closing)],
    ]
    
    cell_hints = {}
    if str(mode or "").strip().lower() == "scaffold":
        cell_hints["t0_r2_c2"] = "Carrying value = Cost - Accumulated Depreciation"
        cell_hints["t0_r7_c2"] = f"Vehicles depreciation = R{_money(vehicles_cv_opening)} × {vehicles_dep_rate}% = R{_money(vehicles_dep)} (diminishing balance)"
        cell_hints["t0_r7_c3"] = f"Equipment depreciation = R{_money(equipment_cost)} × {equipment_dep_rate}% = R{_money(equipment_dep)} (cost method)"
        cell_hints["t0_r10_c2"] = "Accumulated Depreciation = Opening + Current year depreciation"
        cell_hints["t0_r11_c2"] = "Closing carrying value = Cost - Closing accumulated depreciation"
    
    return _mk_journal(
        prompt=prompt,
        journal_type="fixed_assets_note",
        headers=headers,
        values_rows=rows,
        difficulty=difficulty,
        mode=mode,
        base_editable_cols=[1, 2, 3],
        guidelines=[
            "Land & Buildings are not depreciated (0% depreciation rate).",
            "Carrying Value = Cost - Accumulated Depreciation.",
            "Depreciation methods: Diminishing balance (on carrying value) or Cost method (on original cost).",
            "Accumulated Depreciation increases each year by the current depreciation.",
        ],
        cell_hints=cell_hints,
        archetype_key="g11_ct1_q5_fixed_assets_note",
    )


def _make_internal_control_vehicle(*, r: random.Random, difficulty: str, mode: str) -> Dict[str, Any]:
    """Grade 11 Controlled Test - Internal Control Measures for Vehicle Misuse."""
    business = r.choice(["Mamba Traders", "Baloyi Stores", "Tshabalala Traders"])
    
    # Control measures for vehicle misuse
    control_measures = [
        "Logbook system: Record all trips with date, destination, purpose, and mileage",
        "Fuel limit: Set monthly fuel allowance based on business needs only",
        "GPS tracking: Install GPS to monitor vehicle location and usage",
        "Authorized drivers only: Only designated employees may use company vehicle",
        "Regular servicing: Maintain vehicle at authorized dealers with record keeping",
        "Personal use prohibition: Strict policy against using vehicle for personal errands",
        "After-hours lock-up: Vehicle must be parked at business premises or designated location",
        "Mileage reconciliation: Compare odometer readings with logbook entries monthly",
        "Spot checks: Random verification of vehicle location and condition",
        "Disciplinary action: Clear consequences for misuse including possible termination",
    ]
    
    # Select 5-6 measures for the question
    selected_measures = r.sample(control_measures, k=r.choice([5, 6]))
    
    prompt = f"""Internal Control — {business}

The owner has noticed that the business vehicle is being used for personal purposes and suspects fuel theft.

Required: Name {len(selected_measures)} control measures that can be implemented to prevent the misuse of the vehicle.
"""
    
    # Create word bank style question
    word_bank = [{"id": str(i + 1), "label": m} for i, m in enumerate(selected_measures)]
    
    # Create empty answer slots
    rows = [[f"{i + 1}.", "", ""] for i in range(len(selected_measures))]
    
    # Build correct_map
    correct_map = {str(i): {"2": str(i + 1)} for i in range(len(selected_measures))}
    
    out = {
        "id": _make_id("acct11_internal_control"),
        "question_type": "table_wordbank",
        "prompt": prompt,
        "word_bank": word_bank,
        "table": {
            "headers": ["No.", "Control Measure", ""],
            "rows": rows,
        },
        "correct_map": correct_map,
        "guidelines": [
            "Internal controls are procedures to safeguard assets and prevent fraud.",
            "Vehicle controls should address: authorization, documentation, verification, and restriction.",
        ],
        "meta": {"archetype_key": "g11_ct1_q6_internal_control"},
    }
    
    return out


def _make_bank_ledger_taccount(*, r: random.Random, difficulty: str, mode: str) -> Dict[str, Any]:
    """Grade 11 - Bank Account in General Ledger T-account format."""
    business = r.choice(["Mamba Traders", "Baloyi Stores", "Tshabalala Traders"])
    fy_end = "28 February 2024"
    
    # Opening balance (from previous year's BRS)
    opening_balance = float(r.choice([8500, 12400, 6800, 15200]))
    
    # Totals from cash journals
    crj_total = float(r.choice([45000, 52000, 38000, 62000]))
    cpj_total = float(r.choice([28000, 35000, 42000, 31000]))
    
    # Calculate closing balance
    closing_balance = _round_money(opening_balance + crj_total - cpj_total)
    
    # Bank T-account format
    headers = ["Date", "Details", "Fol", "Amount", "Date", "Details", "Fol", "Amount"]
    
    rows = [
        [f"BANK ACCOUNT", "", "", "", "", "", "", ""],
        ["", "", "", "", f"1 Mar 2023", "Balance", "b/d", _money(opening_balance)],
        [f"28 Feb 2024", "Cash receipts", "CRJ", _money(crj_total), f"28 Feb 2024", "Cash payments", "CPJ", _money(cpj_total)],
        [f"28 Feb 2024", "Balance", "c/d", "", "", "", "", ""],
        ["", "", _money(_round_money(opening_balance + crj_total)), "", "", "", _money(_round_money(opening_balance + crj_total)), ""],
        [f"1 Mar 2024", "Balance", "b/d", _money(closing_balance), "", "", "", ""],
    ]
    
    # Calculate balance c/d
    total_debit = opening_balance + crj_total
    balance_cd = _round_money(total_debit - cpj_total)
    rows[3][3] = _money(balance_cd)
    
    cell_hints = {}
    if str(mode or "").strip().lower() == "scaffold":
        cell_hints["t0_r1_c7"] = "Opening balance from previous year's bank reconciliation."
        cell_hints["t0_r2_c3"] = "Total cash receipts from CRJ (debit to Bank)."
        cell_hints["t0_r2_c7"] = "Total cash payments from CPJ (credit to Bank)."
        cell_hints["t0_r3_c3"] = f"Balance c/d = R{_money(opening_balance)} + R{_money(crj_total)} - R{_money(cpj_total)} = R{_money(balance_cd)}"
        cell_hints["t0_r5_c3"] = "Opening balance for next year."
    
    prompt = f"""Ledger Account — {business}

Required: Prepare the Bank account in the General Ledger for the year ended {fy_end}.

Information:
- Opening balance (1 March 2023): R{_money(opening_balance)}
- Total cash receipts for the year (CRJ): R{_money(crj_total)}
- Total cash payments for the year (CPJ): R{_money(cpj_total)}

Bank is an asset account (debit balance).
"""
    
    return _mk_journal(
        prompt=prompt,
        journal_type="bank_ledger_taccount",
        headers=headers,
        values_rows=rows,
        difficulty=difficulty,
        mode=mode,
        base_editable_cols=[0, 1, 2, 3, 4, 5, 6, 7],
        guidelines=[
            "Bank is an asset account - normal debit balance.",
            "Cash receipts (CRJ total) are debited to Bank.",
            "Cash payments (CPJ total) are credited to Bank.",
            "The account must balance: Total Debits = Total Credits.",
        ],
        cell_hints=cell_hints,
        archetype_key="g11_ct1_q2_bank_ledger",
    )


def _make_crj_cpj_adjustments(*, r: random.Random, difficulty: str, mode: str) -> Dict[str, Any]:
    """G11 CRJ/CPJ adjustments from bank statement + reconciliation context."""
    business = r.choice(["Mass Traders", "Baloyi Stores", "Mamba Traders"])
    month = r.choice(["March", "June", "September", "December"])
    year = int(r.choice([20, 21, 22, 23, 24]))
    opening_balance = float(r.choice([5000, 8500, 12300, 15600]))
    bank_charges = float(r.choice([250, 350, 450]))
    eft_cr = float(r.choice([0, 1200, 2500]))
    rd_amount = float(r.choice([0, 500, 800]))
    dishonoured = float(r.choice([0, 1800, 2400, 3000]))
    rent_income = float(r.choice([3500, 4200, 5000]))
    interest = float(r.choice([800, 1200, 1500]))
    crj_total = rent_income + interest + eft_cr + rd_amount
    cpj_total = bank_charges + dishonoured
    closing_balance = opening_balance + crj_total - cpj_total
    headers = ["Doc.no.", "Day", "Details", "Fol.", "Bank", "Sundry accounts", "Amount", "Details"]
    rows: List[List[Optional[str]]] = [
        ["", f"{month}", "", "", "", "", "", ""],
        ["", "5", "Rent income", "GL", _money(rent_income), "", "", ""],
        ["", "12", "Interest received", "GL", _money(interest), "", "", ""],
    ]
    if eft_cr > 0:
        rows.append(["EFT", "", "EFT received", "GL", _money(eft_cr), "", "", ""])
    if rd_amount > 0:
        rows.append(["", "", "RD Revenue", "GL", _money(rd_amount), "", "", ""])
    rows.append(["", "Sundry accounts:", "", "", "", "", "", ""])
    rows.append(["", "Rent income", "GL", "", "", "", _money(rent_income), "Rent income"])
    rows.append(["", "Interest received", "GL", "", "", "", _money(interest), "Interest received"])
    if eft_cr > 0:
        rows.append(["", "Bank", "GL", "", "", "", _money(eft_cr), "EFT"])
    if rd_amount > 0:
        rows.append(["", "Revenue Dept", "GL", "", "", "", _money(rd_amount), "RD"])
    prompt = f"""G11 Controlled Test — Cash Journals Adjustments
You are provided with the Bank Statement for {business} for {month} 20{year}. Some transactions have not yet been recorded in the Cash Receipts Journal (CRJ) and Cash Payments Journal (CPJ).
Bank Reconciliation context:
- Opening Bank balance (favourable): R{_money(opening_balance)}
- Bank charges not yet recorded: R{_money(bank_charges)}
- Dishonoured cheque not yet recorded: R{_money(dishonoured)}
- EFT received: R{_money(eft_cr)}
- RD (Revenue Department): R{_money(rd_amount)}
- Rent income: R{_money(rent_income)}
- Interest received: R{_money(interest)}
Required: Record the missing entries in the CRJ below."""
    cell_hints: Dict[str, str] = {}
    if str(mode or "").strip().lower() == "scaffold":
        cell_hints["t0_r1_c4"] = "Enter the rent income amount in the Bank column."
        cell_hints["t0_r2_c4"] = "Enter the interest amount in the Bank column."
    return _mk_journal(
        prompt=prompt,
        journal_type="crj_adjustments",
        headers=headers,
        values_rows=rows,
        difficulty=difficulty,
        mode=mode,
        base_editable_cols=[0, 1, 2, 3, 4, 6, 7],
        title_fields=[
            {"label": "CASH RECEIPTS JOURNAL", "value": f"of {business}"},
            {"label": "Month", "value": f"{month} 20{year}"},
        ],
        cell_hints=cell_hints,
        archetype_key="g11_ct1_q2_crj_cpj_adjustments",
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
    qtype_norm = str(question_type or "mixed").strip().lower()

    # Build pool of question generators
    pool_generators = []

    if subskill_norm in {"mixed", "crj", "cash_receipts"}:
        pool_generators.append(lambda: _make_crj_format(r=r, difficulty=difficulty, mode=mode))

    if subskill_norm in {"mixed", "cpj", "cash_payments"}:
        pool_generators.append(lambda: _make_cpj_format(r=r, difficulty=difficulty, mode=mode))

    if subskill_norm in {"mixed", "fixed_assets", "depreciation", "timeline"}:
        pool_generators.append(lambda: _make_fixed_assets_timeline_calc(r=r, difficulty=difficulty, mode=mode))

    if subskill_norm in {"mixed", "accdep", "accumulated_depreciation", "taccount"}:
        pool_generators.append(lambda: _make_accdep_equipment_taccount(r=r, difficulty=difficulty, mode=mode))

    if subskill_norm in {"mixed", "disposal", "asset_disposal"}:
        pool_generators.append(lambda: _make_asset_disposal_taccount(r=r, difficulty=difficulty, mode=mode))

    if subskill_norm in {"mixed", "fixed_assets_note", "assets_note"}:
        pool_generators.append(lambda: _make_fixed_assets_note(r=r, difficulty=difficulty, mode=mode))

    if subskill_norm in {"mixed", "internal_control", "control"}:
        pool_generators.append(lambda: _make_internal_control_vehicle(r=r, difficulty=difficulty, mode=mode))

    if subskill_norm in {"mixed", "bank_ledger", "general_ledger", "bank"}:
        pool_generators.append(lambda: _make_bank_ledger_taccount(r=r, difficulty=difficulty, mode=mode))

    if subskill_norm in {"mixed", "crj_cpj_adj", "adjustments", "crj_cpj"}:
        pool_generators.append(lambda: _make_crj_cpj_adjustments(r=r, difficulty=difficulty, mode=mode))

    # If no specific subskill matched, include all
    if not pool_generators:
        pool_generators = [
            lambda: _make_crj_format(r=r, difficulty=difficulty, mode=mode),
            lambda: _make_cpj_format(r=r, difficulty=difficulty, mode=mode),
            lambda: _make_fixed_assets_timeline_calc(r=r, difficulty=difficulty, mode=mode),
            lambda: _make_accdep_equipment_taccount(r=r, difficulty=difficulty, mode=mode),
            lambda: _make_asset_disposal_taccount(r=r, difficulty=difficulty, mode=mode),
            lambda: _make_fixed_assets_note(r=r, difficulty=difficulty, mode=mode),
            lambda: _make_internal_control_vehicle(r=r, difficulty=difficulty, mode=mode),
            lambda: _make_bank_ledger_taccount(r=r, difficulty=difficulty, mode=mode),
            lambda: _make_crj_cpj_adjustments(r=r, difficulty=difficulty, mode=mode),
        ]

    out: List[Dict[str, Any]] = []
    for i in range(n):
        gen = pool_generators[i % len(pool_generators)]
        out.append(gen())

    return out
