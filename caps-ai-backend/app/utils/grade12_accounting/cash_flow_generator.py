from __future__ import annotations

import random
from typing import Any, Dict, List, Optional, Tuple

from ..sole_trader.core import fmt_money as _fmt_money
from ..sole_trader.core import make_id as _make_id
from ..sole_trader.core import round_money as _round_money
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


def _br(x: float) -> str:
    return f"({_money(abs(x))})" if x < 0 else _money(x)


def _pick_company(r: random.Random) -> Tuple[str, str]:
    company = r.choice(["Qoba Ltd", "Aneesa Ltd", "Glebo Ltd", "Kwik Fix Ltd"])
    fy_end = r.choice(["28 February 2017", "30 June 2018", "28 February 2021", "30 June 2020"])
    return company, fy_end


def _mk_table(
    *,
    table_index: int,
    journal_type: str,
    title_fields: List[Dict[str, Any]],
    headers: List[str],
    values_rows: List[List[Optional[str]]],
    difficulty: str,
    mode: str,
    base_editable_cols: List[int],
) -> Tuple[Dict[str, Any], Dict[str, Any]]:
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
        rows.append(_build_prefixed_row(table_index=table_index, row_index=rix, values=display, editable_cols=editable_cols))
        for cix, v0 in enumerate(vals):
            correct_map[f"t{int(table_index)}_r{int(rix)}_c{int(cix)}"] = "" if v0 is None else str(v0)

    journal = {
        "journal_type": journal_type,
        "table_variant": "grade_project",
        "headers": headers,
        "rows": rows,
        "column_help": {},
        "title_fields": title_fields,
    }

    return journal, correct_map


def _make_cash_flow_question(*, r: random.Random, difficulty: str, mode: str) -> Dict[str, Any]:
    company, fy_end = _pick_company(r)

    # Reconciliation note items (deterministic but simplified)
    net_profit_before_tax = float(r.choice([451_770, 302_000, 520_000, 410_000]))
    depreciation = float(r.choice([25_320, 48_000, 36_500, 60_000]))
    interest_expense = float(r.choice([47_600, 72_000, 35_000, 55_000]))

    # Working capital changes: these are adjustments to arrive at cash generated from operations.
    inc_inventory = float(r.choice([0.0, 12_500, 39_425]))
    dec_inventory = float(r.choice([0.0, 18_000, 25_000]))
    if inc_inventory and dec_inventory:
        dec_inventory = 0.0

    inc_trade_receivables = float(r.choice([0.0, 14_230, 9_500]))
    dec_trade_receivables = float(r.choice([0.0, 6_700, 8_000]))
    if inc_trade_receivables and dec_trade_receivables:
        dec_trade_receivables = 0.0

    inc_trade_payables = float(r.choice([0.0, 11_500, 15_000]))
    dec_trade_payables = float(r.choice([0.0, 7_300, 9_000]))
    if inc_trade_payables and dec_trade_payables:
        dec_trade_payables = 0.0

    # Map these to plus/minus in reconciliation
    # In many exam formats:
    # - Increase in inventories/receivables = subtract
    # - Decrease in inventories/receivables = add
    # - Increase in payables = add
    # - Decrease in payables = subtract
    inv_effect = _round_money((-inc_inventory) + dec_inventory)
    rec_effect = _round_money((-inc_trade_receivables) + dec_trade_receivables)
    pay_effect = _round_money((inc_trade_payables) + (-dec_trade_payables))

    cash_generated_from_operations = _round_money(
        net_profit_before_tax + depreciation + interest_expense + inv_effect + rec_effect + pay_effect
    )

    income_tax_paid = float(r.choice([176_240, 150_285, 93_640, 210_000]))
    net_cash_from_operating = _round_money(cash_generated_from_operations - income_tax_paid)

    dividends_paid = float(r.choice([90_000, 120_000, 70_000]))
    loan_repaid = float(r.choice([285_000, 320_000, 458_000]))

    net_cash_from_financing = _round_money(-(dividends_paid + loan_repaid))

    purchase_fixed_assets = float(r.choice([160_000, 250_000, 95_000]))
    net_cash_from_investing = _round_money(-purchase_fixed_assets)

    net_change_cash = _round_money(net_cash_from_operating + net_cash_from_investing + net_cash_from_financing)

    opening_cash = float(r.choice([900.0, 12_340.0, 25_000.0]))
    closing_cash = _round_money(opening_cash + net_change_cash)

    # Table 1: reconciliation note
    rec_headers = ["Reconciliation note", "Amount"]
    rec_rows: List[List[Optional[str]]] = [
        ["Net profit before tax", _money(net_profit_before_tax)],
        ["Adjustments:", ""],
        ["  Depreciation", _money(depreciation)],
        ["  Interest expense", _money(interest_expense)],
        ["Changes in working capital:", ""],
        ["  Inventories", _br(inv_effect)],
        ["  Trade and other receivables", _br(rec_effect)],
        ["  Trade and other payables", _br(pay_effect)],
        ["Cash generated from operations", _money(cash_generated_from_operations)],
    ]

    j0, m0 = _mk_table(
        table_index=0,
        journal_type="cash_flow_reconciliation_note",
        title_fields=[
            {"label": "NOTE: reconciliation", "value": ""},
            {"label": "Company", "value": company},
            {"label": "Year ended", "value": fy_end},
        ],
        headers=rec_headers,
        values_rows=rec_rows,
        difficulty=difficulty,
        mode=mode,
        base_editable_cols=[1],
    )

    # Table 2: cash flow statement
    cfs_headers = ["Cash Flow Statement", "Amount"]
    cfs_rows: List[List[Optional[str]]] = [
        ["Cash generated from operations", _money(cash_generated_from_operations)],
        ["Income tax paid", f"({_money(income_tax_paid)})"],
        ["Net cash from operating activities", _money(net_cash_from_operating)],
        ["Cash flows from investing activities", ""],
        ["  Purchase of fixed/tangible assets", f"({_money(purchase_fixed_assets)})"],
        ["Net cash from investing activities", _money(net_cash_from_investing)],
        ["Cash flows from financing activities", ""],
        ["  Dividends paid", f"({_money(dividends_paid)})"],
        ["  Repayment of loan", f"({_money(loan_repaid)})"],
        ["Net cash from financing activities", _money(net_cash_from_financing)],
        ["Net change in cash and cash equivalents", _money(net_change_cash)],
        ["Cash and cash equivalents at beginning of year", _money(opening_cash)],
        ["Cash and cash equivalents at end of year", _money(closing_cash)],
    ]

    j1, m1 = _mk_table(
        table_index=1,
        journal_type="cash_flow_statement",
        title_fields=[
            {"label": "CASH FLOW STATEMENT", "value": ""},
            {"label": "Company", "value": company},
            {"label": "For the year ended", "value": fy_end},
        ],
        headers=cfs_headers,
        values_rows=cfs_rows,
        difficulty=difficulty,
        mode=mode,
        base_editable_cols=[1],
    )

    correct_map = {**m0, **m1}

    cell_hints: Dict[str, str] = {}
    if str(mode or "").strip().lower() == "scaffold":
        cell_hints["t0_r0_c1"] = "Start with net profit before tax."
        cell_hints["t0_r2_c1"] = "Depreciation is a non-cash expense (add back)."
        cell_hints["t0_r3_c1"] = "Interest expense is added back in the reconciliation note."
        cell_hints["t0_r5_c1"] = "Increase in inventories is subtracted; decrease is added."
        cell_hints["t1_r10_c1"] = "Net change = Operating + Investing + Financing."
        cell_hints["t1_r12_c1"] = "Closing cash = Opening cash + Net change."

    return {
        "id": _make_id("acct12_cash_flow"),
        "question_type": "journal",
        "prompt": "Companies — Cash Flow Statement\n\nComplete the reconciliation note and the cash flow statement in the given format.",
        "journals": [j0, j1],
        "correct_map": correct_map,
        "guidelines": [
            "Show negative cash flows in brackets where applicable.",
            "Use the correct format and subtotals.",
            "Enter amounts without a currency symbol.",
        ],
        "expected_answer_type": "journal",
        "cell_hints": cell_hints if str(mode or "").strip().lower() == "scaffold" else None,
        "meta": {
            "net_profit_before_tax": net_profit_before_tax,
            "depreciation": depreciation,
            "interest_expense": interest_expense,
            "inventories_effect": inv_effect,
            "receivables_effect": rec_effect,
            "payables_effect": pay_effect,
            "cash_generated_from_operations": cash_generated_from_operations,
            "income_tax_paid": income_tax_paid,
            "dividends_paid": dividends_paid,
            "loan_repaid": loan_repaid,
            "purchase_fixed_assets": purchase_fixed_assets,
            "opening_cash": opening_cash,
            "closing_cash": closing_cash,
            "archetype_key": "g12_cf_reconciliation_note",
        },
    }


def _make_dividends_paid_note(*, r: random.Random, difficulty: str, mode: str) -> Dict[str, Any]:
    """Grade 12 Cash Flow Statement - Dividends paid note."""
    company, fy_end = _pick_company(r)
    
    # Dividends payable balances
    dividends_payable_opening = float(r.choice([45_000, 62_000, 38_000, 75_000]))
    
    # Dividends declared during the year
    interim_dividends = float(r.choice([85_000, 120_000, 95_000]))
    final_dividends = float(r.choice([125_000, 160_000, 110_000]))
    total_dividends_declared = _round_money(interim_dividends + final_dividends)
    
    # Dividends payable closing
    dividends_payable_closing = float(r.choice([55_000, 40_000, 70_000]))
    
    # Calculate dividends paid
    dividends_paid = _round_money(dividends_payable_opening + total_dividends_declared - dividends_payable_closing)
    
    headers = ["Details", "Note", "Amount"]
    rows: List[List[Optional[str]]] = [
        ["Dividends payable at beginning of year", "", _money(dividends_payable_opening)],
        ["Dividends declared during the year", "", ""],
        ["  Interim dividends", "", _money(interim_dividends)],
        ["  Final dividends", "", _money(final_dividends)],
        ["", "", _money(total_dividends_declared)],
        ["", "", ""],
        ["Less: Dividends payable at end of year", "", f"({_money(dividends_payable_closing)})"],
        ["Dividends paid during the year", "", _money(dividends_paid)],
    ]
    
    cell_hints: Dict[str, str] = {}
    if str(mode or "").strip().lower() == "scaffold":
        cell_hints["t0_r0_c2"] = "Opening balance from previous year."
        cell_hints["t0_r2_c2"] = "Interim dividends declared during the year."
        cell_hints["t0_r3_c2"] = "Final dividends declared at year-end."
        cell_hints["t0_r6_c2"] = "Closing balance - still payable at year-end."
        cell_hints["t0_r7_c2"] = "Dividends paid = Opening + Declared - Closing."
    
    j, m = _mk_table(
        table_index=0,
        journal_type="cf_dividends_paid",
        title_fields=[
            {"label": "DIVIDENDS PAID NOTE", "value": ""},
            {"label": "Company", "value": company},
            {"label": "For the year ended", "value": fy_end},
        ],
        headers=headers,
        values_rows=rows,
        difficulty=difficulty,
        mode=mode,
        base_editable_cols=[2],
    )
    
    return {
        "id": _make_id("acct12_cf_dividends"),
        "question_type": "journal",
        "prompt": "Cash Flow Statement — Dividends Paid Note\n\nCalculate the dividends paid for the year.",
        "journal": j,
        "correct_map": m,
        "guidelines": [
            "Dividends payable is a current liability.",
            "Opening balance + Dividends declared = Total dividends obligation.",
            "Total obligation - Closing payable = Dividends paid in cash.",
        ],
        "expected_answer_type": "journal",
        "cell_hints": cell_hints if str(mode or "").strip().lower() == "scaffold" else None,
        "meta": {
            "dividends_payable_opening": dividends_payable_opening,
            "interim_dividends": interim_dividends,
            "final_dividends": final_dividends,
            "total_dividends_declared": total_dividends_declared,
            "dividends_payable_closing": dividends_payable_closing,
            "dividends_paid": dividends_paid,
            "archetype_key": "g12_cf_dividends_paid_note",
        },
    }


def _make_taxation_paid_note(*, r: random.Random, difficulty: str, mode: str) -> Dict[str, Any]:
    """Grade 12 Cash Flow Statement - Taxation paid note."""
    company, fy_end = _pick_company(r)
    
    # SARS income tax balances
    sars_opening = float(r.choice([45_000, 32_000, 58_000, 25_000]))
    income_tax_expense = float(r.choice([125_000, 158_000, 198_000, 240_000]))
    sars_closing = float(r.choice([65_000, 48_000, 82_000, 35_000]))
    
    # Calculate taxation paid
    taxation_paid = _round_money(sars_opening + income_tax_expense - sars_closing)
    
    headers = ["Details", "Note", "Amount"]
    rows: List[List[Optional[str]]] = [
        ["SARS (Income tax) at beginning of year", "", _money(sars_opening)],
        ["Income tax expense for the year", "", _money(income_tax_expense)],
        ["", "", _money(_round_money(sars_opening + income_tax_expense))],
        ["", "", ""],
        ["Less: SARS (Income tax) at end of year", "", f"({_money(sars_closing)})"],
        ["Taxation paid during the year", "", _money(taxation_paid)],
    ]
    
    cell_hints: Dict[str, str] = {}
    if str(mode or "").strip().lower() == "scaffold":
        cell_hints["t0_r0_c2"] = "Opening balance owing to SARS."
        cell_hints["t0_r1_c2"] = "Tax expense for current year."
        cell_hints["t0_r4_c2"] = "Closing balance still owing to SARS."
        cell_hints["t0_r5_c2"] = "Tax paid = Opening + Expense - Closing."
    
    j, m = _mk_table(
        table_index=0,
        journal_type="cf_taxation_paid",
        title_fields=[
            {"label": "TAXATION PAID NOTE", "value": ""},
            {"label": "Company", "value": company},
            {"label": "For the year ended", "value": fy_end},
        ],
        headers=headers,
        values_rows=rows,
        difficulty=difficulty,
        mode=mode,
        base_editable_cols=[2],
    )
    
    return {
        "id": _make_id("acct12_cf_taxation"),
        "question_type": "journal",
        "prompt": "Cash Flow Statement — Taxation Paid Note\n\nCalculate the taxation paid for the year.",
        "journal": j,
        "correct_map": m,
        "guidelines": [
            "SARS (Income Tax) is a current liability when owing.",
            "Opening balance + Income tax expense = Total tax obligation.",
            "Total obligation - Closing payable = Tax paid in cash.",
        ],
        "expected_answer_type": "journal",
        "cell_hints": cell_hints if str(mode or "").strip().lower() == "scaffold" else None,
        "meta": {
            "sars_opening": sars_opening,
            "income_tax_expense": income_tax_expense,
            "sars_closing": sars_closing,
            "taxation_paid": taxation_paid,
            "archetype_key": "g12_cf_taxation_paid_note",
        },
    }


def _make_fixed_assets_backcalc(*, r: random.Random, difficulty: str, mode: str) -> Dict[str, Any]:
    """G12 Fixed assets purchased (back-calc additions at cost from note movements)."""
    company, fy_end = _pick_company(r)
    
    # Fixed assets note data - some figures given, some missing
    land_buildings_opening = float(r.choice([800000, 950000, 1100000]))
    land_buildings_additions = float(r.choice([0, 150000, 200000]))  # Missing to calculate
    land_buildings_disposals = float(r.choice([0, 0, 50000]))
    land_buildings_closing = land_buildings_opening + land_buildings_additions - land_buildings_disposals
    
    vehicles_opening = float(r.choice([350000, 420000, 480000]))
    vehicles_cost_missing = True  # Student needs to calculate this
    vehicles_disposals = float(r.choice([80000, 120000, 0]))
    vehicles_depreciation_rate = float(r.choice([0.15, 0.20, 0.25]))  # 15%, 20%, or 25%
    vehicles_depreciation = (vehicles_opening - vehicles_disposals) * vehicles_depreciation_rate
    
    # Back-calc: vehicles closing = opening + additions - disposals
    # Given: closing, opening, disposals, depreciation
    # Missing: additions (additions at cost)
    vehicles_closing = float(r.choice([380000, 450000, 520000]))
    vehicles_additions = vehicles_closing - vehicles_opening + vehicles_disposals  # This is the answer
    
    equipment_opening = float(r.choice([180000, 220000, 250000]))
    equipment_additions = float(r.choice([30000, 50000, 0]))
    equipment_disposals = float(r.choice([0, 25000, 40000]))
    equipment_closing = equipment_opening + equipment_additions - equipment_disposals
    
    prompt = f"""{company} — Fixed Assets Note (extract)
Financial year end: {fy_end}

The following information relates to tangible assets. Some figures have been accidentally omitted.
You are required to calculate the missing figures.

LAND AND BUILDINGS
- Cost at beginning of year: R{_money(land_buildings_opening)}
- Additions at cost: R{_money(land_buildings_additions) if not r.choice([True, False]) else "?"}
- Disposals at cost: R{_money(land_buildings_disposals)}
- Cost at end of year: R{_money(land_buildings_closing)}

VEHICLES
- Cost at beginning of year: R{_money(vehicles_opening)}
- Additions at cost: ? (CALCULATE THIS)
- Disposals at cost: R{_money(vehicles_disposals)}
- Depreciation for the year: R{_money(vehicles_depreciation)} ({int(vehicles_depreciation_rate*100)}% on cost)
- Cost at end of year: R{_money(vehicles_closing)}

EQUIPMENT
- Cost at beginning of year: R{_money(equipment_opening)}
- Additions at cost: R{_money(equipment_additions)}
- Disposals at cost: R{_money(equipment_disposals)}
- Cost at end of year: R{_money(equipment_closing)}

Required: Calculate the Additions at cost for Vehicles."""

    explanation = f"""To calculate Additions at cost for Vehicles:
Formula: Additions = Closing balance - Opening balance + Disposals
Additions = R{_money(vehicles_closing)} - R{_money(vehicles_opening)} + R{_money(vehicles_disposals)}
Additions = R{_money(vehicles_additions)}"""

    result = {
        "id": _make_id("acct12_fixed_assets_backcalc"),
        "question_type": "calc",
        "prompt": prompt,
        "correct_value": float(_round_money(vehicles_additions)),
        "unit": "",
        "expected_answer_type": "number",
        "meta": {"archetype_key": "g12_ct1_fixed_assets_backcalc_additions"},
    }
    
    if str(mode or "").strip().lower() == "scaffold":
        result["explanation"] = explanation
    
    return result


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
    
    # Build pool based on subskill
    pool = []
    if subskill_norm in {"mixed", "reconciliation", "cf_reconciliation", "full_statement"}:
        pool.append(lambda: _make_cash_flow_question(r=r, difficulty=difficulty, mode=mode))
    if subskill_norm in {"mixed", "dividends_paid", "cf_dividends"}:
        pool.append(lambda: _make_dividends_paid_note(r=r, difficulty=difficulty, mode=mode))
    if subskill_norm in {"mixed", "taxation_paid", "cf_taxation"}:
        pool.append(lambda: _make_taxation_paid_note(r=r, difficulty=difficulty, mode=mode))
    if subskill_norm in {"mixed", "fixed_assets_backcalc", "backcalc", "additions"}:
        pool.append(lambda: _make_fixed_assets_backcalc(r=r, difficulty=difficulty, mode=mode))
    
    # If no specific subskill matched, include all
    if not pool:
        pool = [
            lambda: _make_cash_flow_question(r=r, difficulty=difficulty, mode=mode),
            lambda: _make_dividends_paid_note(r=r, difficulty=difficulty, mode=mode),
            lambda: _make_taxation_paid_note(r=r, difficulty=difficulty, mode=mode),
            lambda: _make_fixed_assets_backcalc(r=r, difficulty=difficulty, mode=mode),
        ]

    out: List[Dict[str, Any]] = []
    for i in range(n):
        gen = pool[i % len(pool)]
        out.append(gen())

    return out
