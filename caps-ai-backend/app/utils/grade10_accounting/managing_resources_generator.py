"""Grade 10 Accounting — Managing Resources in a Sole Trader Generator.
100% Deterministic Python generator aligned with South African National Curriculum Standards (Term 1).
Focuses on financial resource management of Cash, Trading Stock, Debtors, Creditors, and Fixed Assets.
Covers 5 distinct subskills:
  1. cash_and_working_capital_management
  2. inventory_reorder_and_shrinkage_management
  3. debtors_credit_terms_and_early_settlement
  4. creditors_trade_and_settlement_discounts
  5. fixed_asset_depreciation_and_utilization
"""
from __future__ import annotations

import random
import uuid
from typing import Any, Dict, List, Optional

from .scenario_builder import build_scenario


SUBSKILLS = [
    "cash_and_working_capital_management",
    "inventory_reorder_and_shrinkage_management",
    "debtors_credit_terms_and_early_settlement",
    "creditors_trade_and_settlement_discounts",
    "fixed_asset_depreciation_and_utilization",
]


def _rng(seed: Optional[int]) -> random.Random:
    r = random.Random()
    if seed is not None:
        r.seed(int(seed))
    return r


def _fmt(val: float | int) -> str:
    return f"{int(round(val)):,}".replace(",", " ")


def _make_id(prefix: str) -> str:
    return f"{prefix}_{uuid.uuid4().hex[:10]}"


def _build_cash_and_working_capital(r: random.Random) -> Dict[str, Any]:
    scen = build_scenario(seed=r.randint(1, 100000))
    business = scen["business"]
    cash_sales = r.randint(45, 95) * 1000
    debtors_rec = r.randint(20, 45) * 1000
    stock_paid = r.randint(30, 55) * 1000
    operating_paid = r.randint(15, 28) * 1000
    open_bank = r.randint(8, 25) * 1000

    tot_inflow = cash_sales + debtors_rec
    tot_outflow = stock_paid + operating_paid
    net_flow = tot_inflow - tot_outflow
    close_bank = open_bank + net_flow

    headers = ["Cash Resource Item", "Amount (R)"]
    spec = [
        ("Opening Bank Balance (1 March)", _fmt(open_bank), False),
        ("Cash Sales banked during March", _fmt(cash_sales), False),
        ("Receipts collected from Debtors", _fmt(debtors_rec), False),
        ("Total Cash Inflows for March", _fmt(tot_inflow), True),
        ("Cash & EFT Payments for Trading Stock", _fmt(stock_paid), False),
        ("Operating Expenses Paid (Rent, Wages, Utilities)", _fmt(operating_paid), False),
        ("Total Cash Outflows for March", _fmt(tot_outflow), True),
        ("Net Cash Flow (Inflows less Outflows)", _fmt(net_flow), True),
        ("Closing Bank Balance (31 March)", _fmt(close_bank), True),
    ]
    rows = []
    correct_map = {}
    for idx, (lbl, val, req) in enumerate(spec):
        cid = f"t0_r{idx}_c1"
        if req:
            correct_map[cid] = val
        rows.append([
            {"cell_id": f"t0_r{idx}_c0", "value": lbl, "editable": False},
            {"cell_id": cid, "value": "" if req else val, "expected": val, "editable": req},
        ])

    prompt = (
        f"{scen['intro']}\n\n"
        f"**INFORMATION:**\n"
        f"{scen['owner']} is reviewing the monthly cash resource summary of **{business}** to ensure sufficient liquidity "
        f"to pay suppliers on time without incurring bank overdraft charges.\n\n"
        f"**REQUIRED:**\n"
        f"Complete the Cash Resource Management Table for March."
    )

    return {
        "id": _make_id("g10_mres_cash"),
        "question_type": "table_completion",
        "modality": "ledger",
        "subskill": "cash_and_working_capital_management",
        "prompt": prompt,
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "marks": 8,
        "explanation": f"Total Inflows = R{_fmt(tot_inflow)}; Total Outflows = R{_fmt(tot_outflow)}; Net Cash Flow = R{_fmt(net_flow)}; Closing Bank = R{_fmt(close_bank)}.",
    }


def _build_inventory_reorder_and_shrinkage(r: random.Random) -> Dict[str, Any]:
    scen = build_scenario(seed=r.randint(1, 100000))
    business = scen["business"]
    open_stock = r.randint(35, 70) * 1000
    purchases = r.randint(110, 180) * 1000
    returns = r.randint(5, 15) * 1000
    cos = r.randint(95, 140) * 1000
    expected_close = open_stock + purchases - returns - cos
    shrinkage = r.randint(2, 6) * 1000
    physical_count = expected_close - shrinkage

    headers = ["Trading Stock Resource Calculation", "Amount (R)"]
    spec = [
        ("Opening Trading Stock (1 March)", _fmt(open_stock), False),
        ("Add: Net Purchases (Purchases R" + _fmt(purchases) + " less Returns R" + _fmt(returns) + ")", _fmt(purchases - returns), True),
        ("Cost of Goods Available for Sale", _fmt(open_stock + purchases - returns), True),
        ("Less: Cost of Sales for the period", _fmt(cos), False),
        ("Expected Closing Balance per General Ledger", _fmt(expected_close), True),
        ("Actual Physical Stock Count on 31 March", _fmt(physical_count), False),
        ("Trading Stock Deficit / Shrinkage Loss", _fmt(shrinkage), True),
    ]
    rows = []
    correct_map = {}
    for idx, (lbl, val, req) in enumerate(spec):
        cid = f"t0_r{idx}_c1"
        if req:
            correct_map[cid] = val
        rows.append([
            {"cell_id": f"t0_r{idx}_c0", "value": lbl, "editable": False},
            {"cell_id": cid, "value": "" if req else val, "expected": val, "editable": req},
        ])

    prompt = (
        f"{scen['intro']}\n\n"
        f"**INFORMATION:**\n"
        f"**{business}** uses the perpetual inventory system to manage its trading stock resource. At the end of the quarter, "
        f"{scen['owner']} compares the General Ledger Trading Stock balance against the physical warehouse count.\n\n"
        f"**REQUIRED:**\n"
        f"Complete the Trading Stock Resource & Shrinkage schedule below."
    )

    return {
        "id": _make_id("g10_mres_stock"),
        "question_type": "table_completion",
        "modality": "ledger",
        "subskill": "inventory_reorder_and_shrinkage_management",
        "prompt": prompt,
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "marks": 8,
        "explanation": f"Expected closing stock = R{_fmt(expected_close)}. Less physical count R{_fmt(physical_count)} = Trading stock deficit of R{_fmt(shrinkage)}.",
    }


def _build_debtors_credit_terms(r: random.Random) -> Dict[str, Any]:
    scen = build_scenario(seed=r.randint(1, 100000))
    business = scen["business"]
    inv_amt = r.choice([12000, 15000, 18000, 24000])
    disc_pct = r.choice([5, 10])
    disc_amt = int(round(inv_amt * disc_pct / 100))
    net_rec = inv_amt - disc_amt
    overdue_amt = r.choice([8000, 10000, 16000])
    int_rate = r.choice([12, 15])
    months_late = r.choice([2, 3])
    interest_charged = int(round(overdue_amt * (int_rate / 100) * (months_late / 12)))

    headers = ["Debtors Resource Scenario", "Calculation / Rule", "Amount (R)"]
    spec = [
        (f"Debtor A settles an invoice of R{_fmt(inv_amt)} within 30 days to qualify for a {disc_pct}% early settlement discount.", "Discount Allowed", _fmt(disc_amt), True),
        ("Net cash received and banked from Debtor A after settlement discount.", "Bank (CRJ)", _fmt(net_rec), True),
        (f"Debtor B's account of R{_fmt(overdue_amt)} is {months_late} months overdue. Interest is charged at {int_rate}% p.a.", "Interest Income (GJ)", _fmt(interest_charged), True),
        ("Updated balance owed by Debtor B after charging overdue interest.", "Debtors Control Closing Balance", _fmt(overdue_amt + interest_charged), True),
    ]
    rows = []
    correct_map = {}
    for idx, (sc_txt, rule, val, req) in enumerate(spec):
        cid = f"t0_r{idx}_c2"
        correct_map[cid] = val
        rows.append([
            {"cell_id": f"t0_r{idx}_c0", "value": sc_txt, "editable": False},
            {"cell_id": f"t0_r{idx}_c1", "value": rule, "editable": False},
            {"cell_id": cid, "value": "", "expected": val, "editable": True},
        ])

    prompt = (
        f"{scen['intro']}\n\n"
        f"**INFORMATION:**\n"
        f"Effective management of trade debtors at **{business}** requires rewarding early payers with settlement discounts "
        f"and charging interest on overdue accounts.\n\n"
        f"**REQUIRED:**\n"
        f"Calculate the required amounts in the Debtors Resource Management table below."
    )

    return {
        "id": _make_id("g10_mres_debtors"),
        "question_type": "table_completion",
        "modality": "ledger",
        "subskill": "debtors_credit_terms_and_early_settlement",
        "prompt": prompt,
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "marks": 8,
        "explanation": f"Discount allowed = R{_fmt(disc_amt)}, Net receipt = R{_fmt(net_rec)}, Overdue interest = R{_fmt(interest_charged)}.",
    }


def _build_creditors_trade_and_settlement_discounts(r: random.Random) -> Dict[str, Any]:
    scen = build_scenario(seed=r.randint(1, 100000))
    business = scen["business"]
    catalog_price = r.choice([40000, 50000, 60000, 80000])
    trade_disc_pct = r.choice([10, 15, 20])
    trade_disc_amt = int(round(catalog_price * trade_disc_pct / 100))
    invoice_net = catalog_price - trade_disc_amt
    settle_disc_pct = r.choice([5, 10])
    settle_disc_amt = int(round(invoice_net * settle_disc_pct / 100))
    eft_paid = invoice_net - settle_disc_amt

    headers = ["Creditors Purchasing & Settlement Step", "Amount (R)"]
    spec = [
        (" Gross Catalogue / List Price of bulk stock ordered", _fmt(catalog_price), False),
        (f"Less: {trade_disc_pct}% Trade Discount negotiated for bulk buying", _fmt(trade_disc_amt), True),
        ("Net Invoice Amount recorded in Creditors Journal (CJ)", _fmt(invoice_net), True),
        (f"Less: {settle_disc_pct}% Settlement Discount received for paying within 15 days", _fmt(settle_disc_amt), True),
        ("Actual EFT Payment from Bank in Cash Payments Journal (CPJ)", _fmt(eft_paid), True),
    ]
    rows = []
    correct_map = {}
    for idx, (lbl, val, req) in enumerate(spec):
        cid = f"t0_r{idx}_c1"
        if req:
            correct_map[cid] = val
        rows.append([
            {"cell_id": f"t0_r{idx}_c0", "value": lbl, "editable": False},
            {"cell_id": cid, "value": "" if req else val, "expected": val, "editable": req},
        ])

    prompt = (
        f"{scen['intro']}\n\n"
        f"**INFORMATION:**\n"
        f"{scen['owner']} negotiates both bulk **trade discounts** (deducted on the invoice before recording in the CJ) "
        f"and early **settlement discounts** (recorded as Discount Received in the CPJ) with suppliers of **{business}**.\n\n"
        f"**REQUIRED:**\n"
        f"Complete the Supplier Discount & Cash Outflow schedule below."
    )

    return {
        "id": _make_id("g10_mres_creditors"),
        "question_type": "table_completion",
        "modality": "ledger",
        "subskill": "creditors_trade_and_settlement_discounts",
        "prompt": prompt,
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "marks": 8,
        "explanation": f"Trade discount = R{_fmt(trade_disc_amt)}; CJ Invoice = R{_fmt(invoice_net)}; Discount received = R{_fmt(settle_disc_amt)}; EFT paid = R{_fmt(eft_paid)}.",
    }


def _build_fixed_asset_utilization(r: random.Random) -> Dict[str, Any]:
    scen = build_scenario(seed=r.randint(1, 100000))
    business = scen["business"]
    eq_cost = r.choice([120000, 150000, 180000])
    eq_acc = int(round(eq_cost * 0.2))
    rate = r.choice([10, 15, 20])
    dep_sl = int(round(eq_cost * rate / 100))
    cv_sl = eq_cost - eq_acc - dep_sl
    dep_db = int(round((eq_cost - eq_acc) * rate / 100))
    cv_db = eq_cost - eq_acc - dep_db

    headers = ["Fixed Asset Valuation Item", f"Method A: {rate}% p.a. on Cost Price (R)", f"Method B: {rate}% p.a. on Carrying Value (R)"]
    spec = [
        ("Original Cost Price of Equipment (1 March 2025)", _fmt(eq_cost), _fmt(eq_cost), False),
        ("Accumulated Depreciation (1 March 2025)", _fmt(eq_acc), _fmt(eq_acc), False),
        ("Carrying Value at beginning of year (1 March 2025)", _fmt(eq_cost - eq_acc), _fmt(eq_cost - eq_acc), True),
        ("Depreciation for the current year (28 February 2026)", _fmt(dep_sl), _fmt(dep_db), True),
        ("Carrying Value at end of year (28 February 2026)", _fmt(cv_sl), _fmt(cv_db), True),
    ]
    rows = []
    correct_map = {}
    for idx, (lbl, v1, v2, req) in enumerate(spec):
        c1 = f"t0_r{idx}_c1"
        c2 = f"t0_r{idx}_c2"
        if req:
            correct_map[c1] = v1
            correct_map[c2] = v2
        rows.append([
            {"cell_id": f"t0_r{idx}_c0", "value": lbl, "editable": False},
            {"cell_id": c1, "value": "" if req else v1, "expected": v1, "editable": req},
            {"cell_id": c2, "value": "" if req else v2, "expected": v2, "editable": req},
        ])

    prompt = (
        f"{scen['intro']}\n\n"
        f"**INFORMATION:**\n"
        f"Proper management of tangible/fixed assets at **{business}** includes tracking wear-and-tear through annual depreciation "
        f"and maintaining an up-to-date Fixed Asset Register.\n\n"
        f"**REQUIRED:**\n"
        f"Compare the **Fixed Instalment (Cost Price)** method and the **Diminishing Balance (Carrying Value)** method "
        f"by completing the table below."
    )

    return {
        "id": _make_id("g10_mres_assets"),
        "question_type": "table_completion",
        "modality": "ledger",
        "subskill": "fixed_asset_depreciation_and_utilization",
        "prompt": prompt,
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "marks": 6,
        "explanation": f"Cost method depreciation = R{_fmt(dep_sl)}; Diminishing balance depreciation = R{_fmt(dep_db)}.",
    }


BUILDERS = {
    "cash_and_working_capital_management": _build_cash_and_working_capital,
    "inventory_reorder_and_shrinkage_management": _build_inventory_reorder_and_shrinkage,
    "debtors_credit_terms_and_early_settlement": _build_debtors_credit_terms,
    "creditors_trade_and_settlement_discounts": _build_creditors_trade_and_settlement_discounts,
    "fixed_asset_depreciation_and_utilization": _build_fixed_asset_utilization,
}


def generate_questions(
    *,
    count: int = 1,
    seed: Optional[int] = None,
    subskill: Optional[str] = None,
    difficulty: str = "medium",
    **kwargs: Any,
) -> List[Dict[str, Any]]:
    r = _rng(seed)
    n = max(1, int(count or 1))
    req_sub = str(subskill or "").strip().lower()
    out: List[Dict[str, Any]] = []
    for _ in range(n):
        chosen_key = req_sub if req_sub in BUILDERS else r.choice(SUBSKILLS)
        q = BUILDERS[chosen_key](r)
        q["difficulty"] = difficulty
        q["subskill"] = chosen_key
        out.append(q)
    return out
