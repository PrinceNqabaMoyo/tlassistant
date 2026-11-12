"""Grade 9 EMS - General Ledger & Trial Balance (Sole Trader): Archetypes 26 to 50.

Grounded strictly in:
- curriculum_docs_auto/EMS_Gr9/Term 2/03. General ledger and Trial balance (sole trader).md

Zero-LLM, 100% deterministic, authentic South African Rand (R) sole-trader contexts.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List

from app.utils.ems_namelist import get_ems_scenario
from .term1_general_ledger_archetypes_01_25 import (
    MONTH_YEARS,
    _build_mcq,
    _build_short,
    _build_table,
    _cell,
    _fmt_r,
    _trader_name,
)


def arch_26_cash_float_t_account_posting_and_increase(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = _trader_name(rng, sc)
    open_cf = rng.randint(4, 12) * 100
    topup = rng.randint(2, 8) * 100
    close_cf = open_cf + topup
    expected = str(close_cf)

    prompt = (
        f"**{biz}** starts the month with **Cash Float (B8)** of **{_fmt_r(open_cf)}** on the Debit side (`Balance b/d`). "
        f"On Day 12, the business cashes a cheque (`CPJ`) for **{_fmt_r(topup)}** to increase the shop till float.\n\n"
        f"Calculate the new **Debit balance** of **Cash Float (B8)**.\n*(Enter digits without spaces or R.)*"
    )
    worked = (
        f"**Cash Float (B8) Closing Debit Balance** [2 marks]\n\n"
        f"- Opening Balance b/d (Dr): `{_fmt_r(open_cf)}`\n"
        f"- Day 12 Bank (`CPJ`, Dr): `+{_fmt_r(topup)}`\n"
        f"- Closing Asset Balance (Dr) = `{_fmt_r(close_cf)}` -> Answer: `{expected}`"
    )
    return _build_short(
        rng,
        qid_prefix="g9_gl_26",
        subskill="26_cash_float_t_account_posting_and_increase",
        title="Cash Float (B8) General Ledger Balance",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=worked,
        marks=2,
        hints={
            "tier_1": "Cash Float is an Asset in the Balance Sheet section (DEAD -> Debit increases).",
            "tier_2": f"Add Opening Cash Float ({_fmt_r(open_cf)}) + CPJ increase ({_fmt_r(topup)}).",
            "tier_3": f"Closing Cash Float = {expected}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Debit Cash Float increases to {_fmt_r(close_cf)}", "marks": 2, "editable": True},
        ],
        misconception_tags=["treating_cash_float_as_expense"],
    )


def arch_27_rent_income_vs_rent_expense_classification(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = _trader_name(rng, sc)
    amt = rng.randint(3, 14) * 500
    is_income = rng.choice([True, False])

    if is_income:
        prompt = (
            f"**{biz}** sub-lets a spare storeroom and receives **{_fmt_r(amt)}** recorded in the CRJ.\n\n"
            f"Identify the correct General Ledger posting and Trial Balance column for **Rent Income**."
        )
        correct = f"Credit Rent Income (Nominal section, Details 'Bank', CRJ) with {_fmt_r(amt)}; placed in Credit column of Trial Balance."
        distractors = [
            f"Debit Rent Income (Balance Sheet section, Details 'Bank', CRJ) with {_fmt_r(amt)}; placed in Debit column of Trial Balance.",
            f"Credit Rent Expense (Nominal section, CPJ) with {_fmt_r(amt)}.",
            f"Debit Bank and Debit Rent Income simultaneously with {_fmt_r(amt)}.",
        ]
    else:
        prompt = (
            f"**{biz}** pays monthly shop rental of **{_fmt_r(amt)}** by EFT recorded in the CPJ.\n\n"
            f"Identify the correct General Ledger posting and Trial Balance column for **Rent Expense**."
        )
        correct = f"Debit Rent Expense (Nominal section, Details 'Bank', CPJ) with {_fmt_r(amt)}; placed in Debit column of Trial Balance."
        distractors = [
            f"Credit Rent Expense (Balance Sheet section, Details 'Bank', CPJ) with {_fmt_r(amt)}; placed in Credit column of Trial Balance.",
            f"Debit Rent Income (Nominal section, CRJ) with {_fmt_r(amt)}.",
            f"Credit Bank and Credit Rent Expense simultaneously with {_fmt_r(amt)}.",
        ]

    return _build_mcq(
        rng,
        qid_prefix="g9_gl_27",
        subskill="27_rent_income_vs_rent_expense_classification",
        title="Rent Income vs Rent Expense Ledger & Trial Balance",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=f"Income (CLIC) is Credited and Expense (DEAD) is Debited, both inside the **Nominal accounts section**. Specifically: **{correct}**",
        hints={
            "tier_1": "Check whether the business is receiving cash (CRJ -> Income -> Cr) or paying cash (CPJ -> Expense -> Dr).",
            "tier_2": "All incomes and expenses appear in the Nominal section of the Trial Balance.",
            "tier_3": correct,
        },
        misconception_tags=["confusing_rent_income_and_rent_expense"],
    )


def arch_28_stock_control_theft_or_shrinkage_detection(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = _trader_name(rng, sc)
    open_s = rng.randint(25, 65) * 500
    pur_s = rng.randint(15, 45) * 500
    cos_s = rng.randint(14, 38) * 500
    theo_close = open_s + pur_s - cos_s
    shortage = rng.randint(3, 18) * 200
    if shortage >= theo_close - 1000:
        shortage = 1200
    phys_count = theo_close - shortage
    expected = str(shortage)

    prompt = (
        f"During stocktake at **{biz}**, the **Trading Stock (B6)** General Ledger records:\n"
        f"- Opening Balance b/d: {_fmt_r(open_s)}\n"
        f"- CPJ Stock Purchases (Dr Bank): {_fmt_r(pur_s)}\n"
        f"- CRJ Cost of Sales (Cr Cost of Sales): {_fmt_r(cos_s)}\n\n"
        f"A physical count reveals actual stock on shelves worth **{_fmt_r(phys_count)}**.\n"
        f"Calculate the **stock shortage (shrinkage/theft loss)**.\n*(Enter digits without spaces or R.)*"
    )
    worked = (
        f"**Stock Control Shortage Calculation** [3 marks]\n\n"
        f"1. Theoretical Closing Stock (from Trading Stock T-account): `{_fmt_r(open_s)} + {_fmt_r(pur_s)} - {_fmt_r(cos_s)} = {_fmt_r(theo_close)}`\n"
        f"2. Less Physical Stock Count on hand: `{_fmt_r(phys_count)}`\n"
        f"3. Unaccounted Stock Shortage = `{_fmt_r(theo_close)} - {_fmt_r(phys_count)} = {_fmt_r(shortage)}` -> Answer: `{expected}`"
    )
    return _build_short(
        rng,
        qid_prefix="g9_gl_28",
        subskill="28_stock_control_theft_or_shrinkage_detection",
        title="Quantify Stock Shortage Using Trading Stock Ledger",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=worked,
        marks=3,
        hints={
            "tier_1": "First calculate expected Closing Stock from Trading Stock (B6), then subtract the physical count.",
            "tier_2": f"Ledger stock = {_fmt_r(theo_close)}; Physical = {_fmt_r(phys_count)}.",
            "tier_3": f"Stock shortage = {expected}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Theoretical stock balance = {_fmt_r(theo_close)}", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": f"Stock shortage = {_fmt_r(shortage)}", "marks": 1, "editable": True},
        ],
        misconception_tags=["stock_control_purpose_confusion"],
    )


def arch_29_bank_ledger_extract_with_subskill_bank_table(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = _trader_name(rng, sc)
    m_name, yr, last_d, m_abbr, next_m, _ = rng.choice(MONTH_YEARS)
    open_b = rng.randint(12, 40) * 1000
    crj_rec = rng.randint(22, 68) * 500
    cpj_pay = rng.randint(10, 32) * 500
    tot_dr = open_b + crj_rec
    if cpj_pay >= tot_dr - 2500:
        cpj_pay = tot_dr - 6000
    close_b = tot_dr - cpj_pay

    headers = ["Side", "Date", "Details", "Folio", "Amount (R)"]
    rows = [
        [_cell("t0_r0_c0", "Debit", "given", False), _cell("t0_r0_c1", f"{m_abbr} 01", "given", False), _cell("t0_r0_c2", "Balance", "given", False), _cell("t0_r0_c3", "b/d", "given", False), _cell("t0_r0_c4", str(open_b), "given", False)],
        [_cell("t0_r1_c0", "Debit", "given", False), _cell("t0_r1_c1", f"{m_abbr} {last_d}", "given", False), _cell("t0_r1_c2", "", "required", True), _cell("t0_r1_c3", "CRJ2", "given", False), _cell("t0_r1_c4", "", "required", True)],
        [_cell("t0_r2_c0", "Credit", "given", False), _cell("t0_r2_c1", f"{m_abbr} {last_d}", "given", False), _cell("t0_r2_c2", "", "required", True), _cell("t0_r2_c3", "CPJ2", "given", False), _cell("t0_r2_c4", "", "required", True)],
        [_cell("t0_r3_c0", "Credit", "given", False), _cell("t0_r3_c1", f"{m_abbr} {last_d}", "given", False), _cell("t0_r3_c2", "Balance", "given", False), _cell("t0_r3_c3", "c/d", "given", False), _cell("t0_r3_c4", "", "required", True)],
        [_cell("t0_r4_c0", "Debit (Next Month)", "given", False), _cell("t0_r4_c1", f"{next_m[:3]} 01", "given", False), _cell("t0_r4_c2", "Balance", "given", False), _cell("t0_r4_c3", "b/d", "given", False), _cell("t0_r4_c4", "", "required", True)],
    ]
    correct_map = {
        "t0_r1_c2": "Total receipts",
        "t0_r1_c4": str(crj_rec),
        "t0_r2_c2": "Total payments",
        "t0_r2_c4": str(cpj_pay),
        "t0_r3_c4": str(close_b),
        "t0_r4_c4": str(close_b),
    }
    cell_hints = {
        "t0_r1_c2": "Details for CRJ Bank total: Total receipts.",
        "t0_r1_c4": f"CRJ Bank total = {crj_rec}.",
        "t0_r2_c2": "Details for CPJ Bank total: Total payments.",
        "t0_r2_c4": f"CPJ Bank total = {cpj_pay}.",
        "t0_r3_c4": f"Closing Balance c/d = {open_b} + {crj_rec} - {cpj_pay} = {close_b}.",
        "t0_r4_c4": f"Opening Balance b/d next month = {close_b}.",
    }
    prompt = (
        f"Post the **CRJ2** and **CPJ2** totals into the **Bank (B7)** ledger table of **{biz}** for **{m_name} {yr}** and balance it "
        f"(Opening Bank: **{_fmt_r(open_b)}**; CRJ2 Bank total: **{_fmt_r(crj_rec)}**; CPJ2 Bank total: **{_fmt_r(cpj_pay)}**; digits without spaces or R)."
    )
    md = (
        "| Side | Date | Details | Folio | Amount (R) |\n"
        "| --- | --- | --- | --- | --- |\n"
        f"| Debit | {m_abbr} 01 | Balance | b/d | {_fmt_r(open_b)} |\n"
        f"| Debit | {m_abbr} {last_d} | **Total receipts** | CRJ2 | **{_fmt_r(crj_rec)}** |\n"
        f"| Credit | {m_abbr} {last_d} | **Total payments** | CPJ2 | **{_fmt_r(cpj_pay)}** |\n"
        f"| Credit | {m_abbr} {last_d} | Balance | c/d | **{_fmt_r(close_b)}** |\n"
        f"| Debit (Next Month) | {next_m[:3]} 01 | Balance | b/d | **{_fmt_r(close_b)}** |"
    )
    sample = f"Dr Total receipts {crj_rec}; Cr Total payments {cpj_pay}; Balance c/d & b/d = {close_b}"
    worked = f"**Bank (B7) Ledger Posting & Balancing Memorandum** [6 marks]\n\n{md}"
    return _build_table(
        rng,
        qid_prefix="g9_gl_29",
        subskill="29_bank_ledger_extract_with_subskill_bank_table",
        title="Bank (B7) Ledger Posting & Balancing Table",
        prompt=prompt,
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=sample,
        marks=6,
        hints={
            "tier_1": "Receipts increase Debit; Payments decrease Credit; Balance c/d = Total Dr - Total Cr.",
            "tier_2": f"Dr total = {tot_dr}; Closing balance = {tot_dr} - {cpj_pay} = {close_b}.",
            "tier_3": sample,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Total receipts & Total payments wording + amounts", "marks": 4, "editable": True},
            {"id": "mp_2", "desc": f"Balance c/d & b/d = {close_b}", "marks": 2, "editable": True},
        ],
        misconception_tags=["reversing_crj_cpj_sides_in_bank", "writing_sales_as_bank_total_detail"],
    )


def arch_30_trading_stock_ledger_with_shrinkage_check(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = _trader_name(rng, sc)
    m_name, yr, last_d, m_abbr, _, _ = rng.choice(MONTH_YEARS)
    open_s = rng.randint(15, 45) * 500
    pur_s = rng.randint(10, 35) * 500
    cos_s = rng.randint(8, 28) * 500
    close_s = open_s + pur_s - cos_s

    headers = ["Side", "Date", "Details", "Folio", "Amount (R)"]
    rows = [
        [_cell("t0_r0_c0", "Debit", "given", False), _cell("t0_r0_c1", f"{m_abbr} 01", "given", False), _cell("t0_r0_c2", "Balance", "given", False), _cell("t0_r0_c3", "b/d", "given", False), _cell("t0_r0_c4", str(open_s), "given", False)],
        [_cell("t0_r1_c0", "Debit", "given", False), _cell("t0_r1_c1", f"{m_abbr} {last_d}", "given", False), _cell("t0_r1_c2", "", "required", True), _cell("t0_r1_c3", "CPJ2", "given", False), _cell("t0_r1_c4", "", "required", True)],
        [_cell("t0_r2_c0", "Credit", "given", False), _cell("t0_r2_c1", f"{m_abbr} {last_d}", "given", False), _cell("t0_r2_c2", "", "required", True), _cell("t0_r2_c3", "CRJ2", "given", False), _cell("t0_r2_c4", "", "required", True)],
        [_cell("t0_r3_c0", "Credit", "given", False), _cell("t0_r3_c1", f"{m_abbr} {last_d}", "given", False), _cell("t0_r3_c2", "Balance", "given", False), _cell("t0_r3_c3", "c/d", "given", False), _cell("t0_r3_c4", "", "required", True)],
    ]
    correct_map = {
        "t0_r1_c2": "Bank",
        "t0_r1_c4": str(pur_s),
        "t0_r2_c2": "Cost of Sales",
        "t0_r2_c4": str(cos_s),
        "t0_r3_c4": str(close_s),
    }
    cell_hints = {
        "t0_r1_c2": "Stock purchases paid from Bank -> Details: Bank.",
        "t0_r1_c4": f"CPJ Trading Stock total = {pur_s}.",
        "t0_r2_c2": "Stock sold at cost -> Details: Cost of Sales.",
        "t0_r2_c4": f"CRJ Cost of Sales total = {cos_s}.",
        "t0_r3_c4": f"Closing stock c/d = {open_s} + {pur_s} - {cos_s} = {close_s}.",
    }
    prompt = (
        f"Complete the **Trading Stock (B6)** ledger summary for **{biz}** (**{m_name} {yr}**; digits without spaces or R):\n"
        f"- **Opening Balance b/d:** {_fmt_r(open_s)}\n"
        f"- **CPJ2 Trading Stock purchases:** {_fmt_r(pur_s)}\n"
        f"- **CRJ2 Cost of Sales:** {_fmt_r(cos_s)}"
    )
    md = (
        "| Side | Date | Details | Folio | Amount (R) |\n"
        "| --- | --- | --- | --- | --- |\n"
        f"| Debit | {m_abbr} 01 | Balance | b/d | {_fmt_r(open_s)} |\n"
        f"| Debit | {m_abbr} {last_d} | **Bank** | CPJ2 | **{_fmt_r(pur_s)}** |\n"
        f"| Credit | {m_abbr} {last_d} | **Cost of Sales** | CRJ2 | **{_fmt_r(cos_s)}** |\n"
        f"| Credit | {m_abbr} {last_d} | Balance | c/d | **{_fmt_r(close_s)}** |"
    )
    sample = f"Dr Bank {pur_s}; Cr Cost of Sales {cos_s}; Closing Stock c/d = {close_s}"
    worked = f"**Trading Stock (B6) Ledger Memorandum** [5 marks]\n\n{md}"
    return _build_table(
        rng,
        qid_prefix="g9_gl_30",
        subskill="30_trading_stock_ledger_with_shrinkage_check",
        title="Trading Stock (B6) Ledger Posting Table",
        prompt=prompt,
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=sample,
        marks=5,
        hints={
            "tier_1": "Debit Trading Stock with CPJ Bank purchases; Credit with CRJ Cost of Sales.",
            "tier_2": f"Closing Balance c/d = {open_s} + {pur_s} - {cos_s}.",
            "tier_3": sample,
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Dr Bank {pur_s} & Cr Cost of Sales {cos_s}", "marks": 4, "editable": True},
            {"id": "mp_2", "desc": f"Balance c/d = {close_s}", "marks": 1, "editable": True},
        ],
        misconception_tags=["putting_sales_instead_of_cost_of_sales_in_trading_stock"],
    )


def arch_31_trial_balance_purpose_and_structure_mcq(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = _trader_name(rng, sc)
    m_name, yr, last_d, _, _, _ = rng.choice(MONTH_YEARS)

    prompt = (
        f"At month-end (**{last_d} {m_name} {yr}**), **{biz}** prepares a **Trial Balance** after posting the CRJ and CPJ to the General Ledger.\n\n"
        f"Which statement accurately states the **heading format and core purpose** of a sole-trader Trial Balance?"
    )
    correct = f"Headed 'Trial Balance of {biz} on {last_d} {m_name} {yr}', divided into Balance Sheet (B) and Nominal (N) sections to prove Total Debits equal Total Credits."
    distractors = [
        f"Headed 'Trial Balance of {biz}' (dates forbidden), containing only Cash Receipts Journal sales totals.",
        "Prepared exclusively to replace the Cash Payments Journal so cheques never need to be written.",
        "Lists only Assets and Liabilities while completely excluding Cost of Sales, Sales, and Wages.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g9_gl_31",
        subskill="31_trial_balance_purpose_and_structure_mcq",
        title="Purpose & Heading of a Sole-Trader Trial Balance",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"Unlike the General Ledger (which shows NO date in its main heading), the Trial Balance takes a **snapshot on a specific date**: "
            f"**'Trial Balance of {biz} on {last_d} {m_name} {yr}'**, verifying arithmetical double-entry equality (`Debits = Credits`) across both `B` and `N` sections."
        ),
        hints={
            "tier_1": "Remember: General Ledger = no date in main heading; Trial Balance = 'on <closing date>'.",
            "tier_2": "A Trial Balance lists ALL active Balance Sheet (B) and Nominal (N) accounts to test Total Debits == Total Credits.",
            "tier_3": correct,
        },
        misconception_tags=["omitting_date_on_trial_balance_heading"],
    )


def arch_32_balance_sheet_vs_nominal_section_sorting_table(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = _trader_name(rng, sc)
    pool = [
        ("Capital", "Balance Sheet", "Credit"),
        ("Drawings", "Balance Sheet", "Debit"),
        ("Vehicles", "Balance Sheet", "Debit"),
        ("Trading Stock", "Balance Sheet", "Debit"),
        ("Cash Float", "Balance Sheet", "Debit"),
        ("Sales", "Nominal", "Credit"),
        ("Cost of Sales", "Nominal", "Debit"),
        ("Rent Income", "Nominal", "Credit"),
        ("Packing Material", "Nominal", "Debit"),
        ("Trading Licence", "Nominal", "Debit"),
    ]
    chosen = rng.sample(pool, 6)
    headers = ["Account Name", "Trial Balance Section (`Balance Sheet` / `Nominal`)", "Column (`Debit` / `Credit`)"]
    rows: List[List[Dict[str, Any]]] = []
    correct_map: Dict[str, str] = {}
    cell_hints: Dict[str, str] = {}
    md_lines = ["| Account Name | Section | Trial Balance Column |", "| --- | --- | --- |"]

    for i, (acc, sec, col) in enumerate(chosen):
        correct_map[f"t0_r{i}_c1"] = sec
        correct_map[f"t0_r{i}_c2"] = col
        cell_hints[f"t0_r{i}_c1"] = "Owner's Equity, Assets & Liabilities = Balance Sheet; Incomes & Expenses = Nominal."
        cell_hints[f"t0_r{i}_c2"] = "DEAD -> Debit; CLIC -> Credit."
        rows.append([
            _cell(f"t0_r{i}_c0", acc, "given", False),
            _cell(f"t0_r{i}_c1", "", "required", True),
            _cell(f"t0_r{i}_c2", "", "required", True),
        ])
        md_lines.append(f"| {acc} | **{sec}** | **{col}** |")

    prompt = (
        f"Sort the following accounts for **{biz}**'s Trial Balance by **Section** (`Balance Sheet` or `Nominal`) "
        f"and **Column** (`Debit` or `Credit`)."
    )
    sample = "; ".join(f"{acc}: {sec}, {col}" for acc, sec, col in chosen)
    worked = "**Trial Balance Section & Column Sorting Memorandum** [12 marks]\n\n" + "\n".join(md_lines)
    return _build_table(
        rng,
        qid_prefix="g9_gl_32",
        subskill="32_balance_sheet_vs_nominal_section_sorting_table",
        title="Sort Sole-Trader Accounts into Trial Balance Sections",
        prompt=prompt,
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=sample,
        marks=12,
        hints={
            "tier_1": "B-accounts = Capital, Drawings, Land/Buildings, Vehicles, Equipment, Trading Stock, Bank, Cash Float; N-accounts = Incomes & Expenses.",
            "tier_2": "Apply DEAD (Debit) and CLIC (Credit).",
            "tier_3": sample,
        },
        marking_points=[{"id": f"mp_{i}", "desc": f"{acc}: {sec}, {col}", "marks": 2, "editable": True} for i, (acc, sec, col) in enumerate(chosen)],
        misconception_tags=["balance_sheet_vs_nominal_confusion"],
    )


def arch_33_trial_balance_favourable_bank_placement(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = _trader_name(rng, sc)
    amt = rng.randint(15, 65) * 500

    prompt = (
        f"In **{biz}**'s General Ledger, **Bank (B7)** shows a closing **`Balance b/d` of {_fmt_r(amt)} on the Debit side**.\n\n"
        f"Where must **Bank (B7)** appear in the Trial Balance?"
    )
    correct = f"Balance Sheet accounts section, Debit column ({_fmt_r(amt)}), because a favourable bank balance is a positive Asset."
    distractors = [
        f"Balance Sheet accounts section, Credit column ({_fmt_r(amt)}), because Bank receives deposits from customers.",
        f"Nominal accounts section, Debit column ({_fmt_r(amt)}), alongside Wages and Stationery.",
        f"Omitted from the Trial Balance completely because cash is already recorded in CRJ and CPJ.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g9_gl_33",
        subskill="33_trial_balance_favourable_bank_placement",
        title="Trial Balance Placement: Favourable Bank (B7)",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=f"A Debit `Balance b/d` in **Bank (B7)** means positive cash in the bank (Asset -> Balance Sheet section, **Debit column**).",
        hints={
            "tier_1": "Check the side of the final `Balance b/d` in Bank (B7).",
            "tier_2": "Debit `b/d` goes straight into the Debit column of the Balance Sheet section.",
            "tier_3": correct,
        },
        misconception_tags=["crediting_favourable_bank_in_trial_balance"],
    )


def arch_34_trial_balance_bank_overdraft_placement(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = _trader_name(rng, sc)
    od = rng.randint(8, 32) * 500

    prompt = (
        f"After posting heavy stock purchases at **{biz}**, the **Bank (B7)** General Ledger ends with a **`Balance b/d` of {_fmt_r(od)} on the Credit side** (a Bank Overdraft).\n\n"
        f"Where is **Bank (B7)** entered in the Trial Balance?"
    )
    correct = f"Balance Sheet accounts section, Credit column ({_fmt_r(od)}), because an overdraft is a short-term Liability owed to the bank."
    distractors = [
        f"Balance Sheet accounts section, Debit column ({_fmt_r(od)}), because Bank is always placed in the Debit column.",
        f"Nominal accounts section, Debit column ({_fmt_r(od)}), treated as an operating expense.",
        f"Subtracted from Cash Float instead of appearing in the Trial Balance.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g9_gl_34",
        subskill="34_trial_balance_bank_overdraft_placement",
        title="Trial Balance Placement: Bank Overdraft (B7)",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"Just like Amiena's Dresses in the curriculum, when **Bank (B7)** ends with a **Credit `Balance b/d`** ({_fmt_r(od)}), "
            f"the business owes that amount to the bank (a Current Liability), so **{_fmt_r(od)}** goes into the **Credit column** under **Balance Sheet accounts**."
        ),
        hints={
            "tier_1": "Match the Trial Balance column to the side where `Balance b/d` rests in the T-account.",
            "tier_2": "A Bank Overdraft is a Liability (CLIC -> Credit).",
            "tier_3": correct,
        },
        misconception_tags=["assuming_bank_always_has_debit_balance"],
    )


def arch_35_trial_balance_capital_and_drawings_opposite_columns(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = _trader_name(rng, sc)
    cap = rng.randint(150, 350) * 1000
    draw = rng.randint(5, 22) * 500

    prompt = (
        f"In **{biz}**'s Trial Balance, **Capital (B1)** is **{_fmt_r(cap)}** and **Drawings (B2)** is **{_fmt_r(draw)}**.\n\n"
        f"Which statement accurately explains why **Capital** and **Drawings** sit in **opposite Trial Balance columns** inside the **Balance Sheet section**?"
    )
    correct = f"Capital ({_fmt_r(cap)}) increases Owner's Equity and goes in Credit, whereas Drawings ({_fmt_r(draw)}) reduces Owner's Equity and goes in Debit."
    distractors = [
        "Capital sits in Debit (DEAD) and Drawings sits in Credit (CLIC) because Drawings adds cash back.",
        "Both Capital and Drawings sit in the Nominal section because Drawings is treated like Salaries.",
        "Drawings is subtracted from Capital inside the ledger, so Drawings never appears in the Trial Balance.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g9_gl_35",
        subskill="35_trial_balance_capital_and_drawings_opposite_columns",
        title="Capital (Credit) vs Drawings (Debit) in Trial Balance",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"Under DEAD/CLIC: **Capital** increases on **Credit** (`{_fmt_r(cap)}`), while **Drawings** decreases Owner's Equity on **Debit** (`{_fmt_r(draw)}`). Both carry **`B`** folios in the Balance Sheet section."
        ),
        hints={
            "tier_1": "Remember: D in DEAD stands for Drawings (Debit); C in CLIC stands for Capital (Credit).",
            "tier_2": "Both belong to Owner's Equity (Balance Sheet section), acting in opposite directions.",
            "tier_3": correct,
        },
        misconception_tags=["placing_drawings_in_credit_column"],
    )


def arch_36_trial_balance_sales_and_cost_of_sales_placement(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = _trader_name(rng, sc)
    cos = rng.randint(20, 65) * 500
    sales = cos * rng.choice([125, 140, 150, 160]) // 100
    gp = sales - cos

    prompt = (
        f"In **{biz}**'s Trial Balance (**Nominal accounts section**), **Sales (N1)** equals **{_fmt_r(sales)}** and **Cost of Sales (N2)** equals **{_fmt_r(cos)}**.\n\n"
        f"Which columns hold **Sales** and **Cost of Sales**, and what is the **Gross Profit**?"
    )
    correct = f"Sales ({_fmt_r(sales)}) in Credit, Cost of Sales ({_fmt_r(cos)}) in Debit; Gross Profit = {_fmt_r(gp)}."
    distractors = [
        f"Sales ({_fmt_r(sales)}) in Debit, Cost of Sales ({_fmt_r(cos)}) in Credit; Gross Profit = {_fmt_r(gp)}.",
        f"Both Sales and Cost of Sales go in Credit because both relate to cash receipts; Gross Profit = {_fmt_r(sales + cos)}.",
        f"Cost of Sales goes in the Balance Sheet section alongside Trading Stock.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g9_gl_36",
        subskill="36_trial_balance_sales_and_cost_of_sales_placement",
        title="Sales (Credit) vs Cost of Sales (Debit) in Trial Balance",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"**Sales (N1)** is Income (Credit = **{_fmt_r(sales)}**). **Cost of Sales (N2)** is an Expense (Debit = **{_fmt_r(cos)}**). "
            f"Their difference gives **Gross Profit** = `{_fmt_r(sales)} - {_fmt_r(cos)} = {_fmt_r(gp)}`."
        ),
        hints={
            "tier_1": "Income -> Credit; Cost of Sales (Expense) -> Debit; Gross Profit = Sales - Cost of Sales.",
            "tier_2": f"Sales Cr {_fmt_r(sales)}, Cost of Sales Dr {_fmt_r(cos)}.",
            "tier_3": correct,
        },
        misconception_tags=["swapping_sales_and_cost_of_sales_sides"],
    )


def arch_37_trial_balance_operating_incomes_vs_expenses(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = _trader_name(rng, sc)
    sales = rng.randint(40, 90) * 500
    rent_inc = rng.randint(3, 12) * 500
    wages = rng.randint(6, 18) * 300
    water = rng.randint(2, 8) * 150
    licence = rng.randint(3, 9) * 100
    tot_cr_nom = sales + rent_inc

    prompt = (
        f"An extract of **{biz}**'s Nominal accounts shows:\n"
        f"- Sales (N1): {_fmt_r(sales)}\n"
        f"- Rent Income (N3): {_fmt_r(rent_inc)}\n"
        f"- Wages (N4): {_fmt_r(wages)}\n"
        f"- Water and Electricity (N11): {_fmt_r(water)}\n"
        f"- Trading Licence (N9): {_fmt_r(licence)}\n\n"
        f"Calculate the **sum of Credit balances** in this Nominal extract.\n*(Enter digits without spaces or R.)*"
    )
    expected = str(tot_cr_nom)
    worked = (
        f"**Nominal Credit Balances Sum** [2 marks]\n\n"
        f"- Credit items (Incomes, CLIC): `Sales ({_fmt_r(sales)}) + Rent Income ({_fmt_r(rent_inc)}) = {_fmt_r(tot_cr_nom)}`\n"
        f"- Debit items (Expenses, DEAD): `Wages ({_fmt_r(wages)}) + Water & Electricity ({_fmt_r(water)}) + Trading Licence ({_fmt_r(licence)})`\n"
        f"- Answer: `{expected}`"
    )
    return _build_short(
        rng,
        qid_prefix="g9_gl_37",
        subskill="37_trial_balance_operating_incomes_vs_expenses",
        title="Identify Credit Incomes vs Debit Expenses in Nominal Section",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=worked,
        marks=2,
        hints={
            "tier_1": "Only Income accounts sit in the Credit column of the Nominal section.",
            "tier_2": f"Add Sales ({_fmt_r(sales)}) and Rent Income ({_fmt_r(rent_inc)}).",
            "tier_3": f"Credit Nominal total = {expected}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Sums Sales + Rent Income = {_fmt_r(tot_cr_nom)}", "marks": 2, "editable": True},
        ],
        misconception_tags=["including_expenses_in_credit_nominal_sum"],
    )


def arch_38_missing_capital_balance_from_trial_balance_table(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = _trader_name(rng, sc)
    m_name, yr, last_d, _, _, _ = rng.choice(MONTH_YEARS)
    draw = rng.randint(4, 15) * 500
    equip = rng.randint(18, 55) * 1000
    stock = rng.randint(16, 48) * 500
    bank = rng.randint(12, 42) * 500
    cos = rng.randint(14, 38) * 500
    wages = rng.randint(6, 18) * 500
    sales = cos * 150 // 100
    tot_dr = draw + equip + stock + bank + cos + wages
    capital = tot_dr - sales

    headers = ["Account", "Folio", "Debit (R)", "Credit (R)"]
    rows = [
        [_cell("t0_r0_c0", "Capital", "given", False), _cell("t0_r0_c1", "B1", "given", False), _cell("t0_r0_c2", "", "must_be_empty", True), _cell("t0_r0_c3", "", "required", True)],
        [_cell("t0_r1_c0", "Drawings", "given", False), _cell("t0_r1_c1", "B2", "given", False), _cell("t0_r1_c2", str(draw), "given", False), _cell("t0_r1_c3", "", "must_be_empty", True)],
        [_cell("t0_r2_c0", "Equipment", "given", False), _cell("t0_r2_c1", "B5", "given", False), _cell("t0_r2_c2", str(equip), "given", False), _cell("t0_r2_c3", "", "must_be_empty", True)],
        [_cell("t0_r3_c0", "Trading Stock", "given", False), _cell("t0_r3_c1", "B6", "given", False), _cell("t0_r3_c2", str(stock), "given", False), _cell("t0_r3_c3", "", "must_be_empty", True)],
        [_cell("t0_r4_c0", "Bank", "given", False), _cell("t0_r4_c1", "B7", "given", False), _cell("t0_r4_c2", str(bank), "given", False), _cell("t0_r4_c3", "", "must_be_empty", True)],
        [_cell("t0_r5_c0", "Sales", "given", False), _cell("t0_r5_c1", "N1", "given", False), _cell("t0_r5_c2", "", "must_be_empty", True), _cell("t0_r5_c3", str(sales), "given", False)],
        [_cell("t0_r6_c0", "Cost of Sales", "given", False), _cell("t0_r6_c1", "N2", "given", False), _cell("t0_r6_c2", str(cos), "given", False), _cell("t0_r6_c3", "", "must_be_empty", True)],
        [_cell("t0_r7_c0", "Wages", "given", False), _cell("t0_r7_c1", "N4", "given", False), _cell("t0_r7_c2", str(wages), "given", False), _cell("t0_r7_c3", "", "must_be_empty", True)],
        [_cell("t0_r8_c0", "TOTALS", "given", False), _cell("t0_r8_c1", "", "given", False), _cell("t0_r8_c2", "", "required", True), _cell("t0_r8_c3", "", "required", True)],
    ]
    correct_map = {
        "t0_r0_c3": str(capital),
        "t0_r8_c2": str(tot_dr),
        "t0_r8_c3": str(tot_dr),
    }
    cell_hints = {
        "t0_r0_c3": f"Total Debits ({tot_dr}) minus Sales ({sales}) = {capital}.",
        "t0_r8_c2": f"Sum all Debit column entries = {tot_dr}.",
        "t0_r8_c3": f"Total Credits must equal Total Debits ({tot_dr}).",
    }
    prompt = (
        f"In the **Trial Balance of {biz} on {last_d} {m_name} {yr}**, the **Capital (B1)** figure was omitted.\n\n"
        f"Solve **Capital (B1)** and complete the balancing **TOTALS** row (digits without spaces or R)."
    )
    md = (
        "| Account | Folio | Debit (R) | Credit (R) |\n"
        "| --- | --- | --- | --- |\n"
        f"| Capital | B1 | | **{capital}** |\n"
        f"| Drawings | B2 | {draw} | |\n"
        f"| Equipment | B5 | {equip} | |\n"
        f"| Trading Stock | B6 | {stock} | |\n"
        f"| Bank | B7 | {bank} | |\n"
        f"| Sales | N1 | | {sales} |\n"
        f"| Cost of Sales | N2 | {cos} | |\n"
        f"| Wages | N4 | {wages} | |\n"
        f"| **TOTALS** | | **{tot_dr}** | **{tot_dr}** |"
    )
    sample = f"Capital = {capital}; Trial Balance Totals Dr = {tot_dr}, Cr = {tot_dr}"
    worked = f"**Trial Balance Missing Capital Memorandum** [4 marks]\n\n{md}"
    return _build_table(
        rng,
        qid_prefix="g9_gl_38",
        subskill="38_missing_capital_balance_from_trial_balance_table",
        title="Solve Missing Capital (B1) in Trial Balance",
        prompt=prompt,
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=sample,
        marks=4,
        hints={
            "tier_1": "First sum the complete Debit column, then remember Total Credits = Total Debits.",
            "tier_2": f"Total Debits = {tot_dr}; Capital = {tot_dr} - {sales}.",
            "tier_3": sample,
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Totals Debit & Credit = {tot_dr}", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": f"Derives Capital = {capital}", "marks": 2, "editable": True},
        ],
        misconception_tags=["trial_balance_imbalance_arithmetic"],
    )


def arch_39_missing_bank_or_drawings_from_trial_balance(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = _trader_name(rng, sc)
    cap = rng.randint(120, 260) * 1000
    sales = rng.randint(25, 65) * 1000
    tot = cap + sales
    veh = rng.randint(40, 110) * 1000
    stock = rng.randint(18, 45) * 500
    cos = sales * 100 // 125
    bank = tot - (veh + stock + cos)
    expected = str(bank)

    prompt = (
        f"A balanced Trial Balance of **{biz}** totals **{_fmt_r(tot)}** on both Debit and Credit sides (`Capital {_fmt_r(cap)} + Sales {_fmt_r(sales)}`).\n"
        f"Known Debit balances are: **Vehicles {_fmt_r(veh)}**, **Trading Stock {_fmt_r(stock)}**, and **Cost of Sales {_fmt_r(cos)}**.\n\n"
        f"Calculate the missing **Bank (Debit)** balance.\n*(Enter digits without spaces or R.)*"
    )
    worked = (
        f"**Missing Bank Balance Calculation** [3 marks]\n\n"
        f"- Total Debits (= Total Credits) = `{_fmt_r(tot)}`\n"
        f"- Known Debits = `{_fmt_r(veh)} + {_fmt_r(stock)} + {_fmt_r(cos)} = {_fmt_r(veh + stock + cos)}`\n"
        f"- Missing Bank (Dr) = `{_fmt_r(tot)} - {_fmt_r(veh + stock + cos)} = {_fmt_r(bank)}` -> Answer: `{expected}`"
    )
    return _build_short(
        rng,
        qid_prefix="g9_gl_39",
        subskill="39_missing_bank_or_drawings_from_trial_balance",
        title="Solve Missing Debit Asset from Balanced Trial Balance",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=worked,
        marks=3,
        hints={
            "tier_1": "In a balanced Trial Balance, all Debit items must add up to the same total as the Credit items.",
            "tier_2": f"Bank = {_fmt_r(tot)} - ({_fmt_r(veh)} + {_fmt_r(stock)} + {_fmt_r(cos)}).",
            "tier_3": f"Bank = {expected}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Subtracts known Debits from {_fmt_r(tot)} = {_fmt_r(bank)}", "marks": 3, "editable": True},
        ],
        misconception_tags=["trial_balance_imbalance_arithmetic"],
    )


def arch_40_full_sole_trader_trial_balance_compilation(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = _trader_name(rng, sc)
    m_name, yr, last_d, _, _, _ = rng.choice(MONTH_YEARS)
    draw = rng.randint(5, 16) * 500
    equip = rng.randint(16, 48) * 1000
    stock = rng.randint(15, 42) * 500
    bank = rng.randint(10, 36) * 500
    cos = rng.randint(12, 34) * 500
    wages = rng.randint(6, 18) * 500
    sales = cos * 150 // 100
    rent_inc = rng.randint(4, 12) * 500
    tot = draw + equip + stock + bank + cos + wages
    cap = tot - (sales + rent_inc)

    items = [
        ("Capital", "B1", cap, "Credit"),
        ("Drawings", "B2", draw, "Debit"),
        ("Equipment", "B5", equip, "Debit"),
        ("Trading Stock", "B6", stock, "Debit"),
        ("Bank", "B7", bank, "Debit"),
        ("Sales", "N1", sales, "Credit"),
        ("Cost of Sales", "N2", cos, "Debit"),
        ("Rent Income", "N3", rent_inc, "Credit"),
        ("Wages", "N4", wages, "Debit"),
    ]

    headers = ["Account", "Folio", "Debit (R)", "Credit (R)"]
    rows: List[List[Dict[str, Any]]] = []
    correct_map: Dict[str, str] = {}
    cell_hints: Dict[str, str] = {}
    md_lines = ["| Account | Folio | Debit (R) | Credit (R) |", "| --- | --- | --- | --- |"]

    for i, (acc, fol, amt, side) in enumerate(items):
        is_dr = side == "Debit"
        rows.append([
            _cell(f"t0_r{i}_c0", acc, "given", False),
            _cell(f"t0_r{i}_c1", fol, "given", False),
            _cell(f"t0_r{i}_c2", "", "required" if is_dr else "must_be_empty", True),
            _cell(f"t0_r{i}_c3", "", "must_be_empty" if is_dr else "required", True),
        ])
        if is_dr:
            correct_map[f"t0_r{i}_c2"] = str(amt)
            cell_hints[f"t0_r{i}_c2"] = f"{acc} ({fol}) has a Debit balance of {amt}."
            md_lines.append(f"| {acc} | {fol} | **{amt}** | |")
        else:
            correct_map[f"t0_r{i}_c3"] = str(amt)
            cell_hints[f"t0_r{i}_c3"] = f"{acc} ({fol}) has a Credit balance of {amt}."
            md_lines.append(f"| {acc} | {fol} | | **{amt}** |")

    tot_idx = len(items)
    rows.append([
        _cell(f"t0_r{tot_idx}_c0", "TOTALS", "given", False),
        _cell(f"t0_r{tot_idx}_c1", "", "given", False),
        _cell(f"t0_r{tot_idx}_c2", "", "required", True),
        _cell(f"t0_r{tot_idx}_c3", "", "required", True),
    ])
    correct_map[f"t0_r{tot_idx}_c2"] = str(tot)
    correct_map[f"t0_r{tot_idx}_c3"] = str(tot)
    cell_hints[f"t0_r{tot_idx}_c2"] = f"Total Debits = {tot}."
    cell_hints[f"t0_r{tot_idx}_c3"] = f"Total Credits = {tot}."
    md_lines.append(f"| **TOTALS** | | **{tot}** | **{tot}** |")

    prompt = (
        f"Compile the **Trial Balance of {biz} on {last_d} {m_name} {yr}** from the General Ledger balances below "
        f"(place each amount strictly in `Debit (R)` or `Credit (R)`, leave opposite side blank, and enter totals; digits without spaces or R):\n\n"
        f"- Capital {_fmt_r(cap)}; Drawings {_fmt_r(draw)}; Equipment {_fmt_r(equip)}; Trading Stock {_fmt_r(stock)}; Bank {_fmt_r(bank)}\n"
        f"- Sales {_fmt_r(sales)}; Cost of Sales {_fmt_r(cos)}; Rent Income {_fmt_r(rent_inc)}; Wages {_fmt_r(wages)}"
    )
    sample = f"Dr Totals = {tot}, Cr Totals = {tot} (Credits: Capital {cap}, Sales {sales}, Rent Income {rent_inc}; remainder Debit)"
    worked = f"**Completed Sole-Trader Trial Balance Memorandum** [11 marks]\n\n" + "\n".join(md_lines)
    return _build_table(
        rng,
        qid_prefix="g9_gl_40",
        subskill="40_full_sole_trader_trial_balance_compilation",
        title="Compile Full Sole-Trader Trial Balance",
        prompt=prompt,
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=sample,
        marks=11,
        hints={
            "tier_1": "Apply DEAD to Debit items (Drawings, Expenses, Assets) and CLIC to Credit items (Capital, Income).",
            "tier_2": f"Credit accounts = Capital ({cap}), Sales ({sales}), Rent Income ({rent_inc}); both Totals equal {tot}.",
            "tier_3": sample,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Balance Sheet section placements (Capital Cr; Drawings/Assets Dr)", "marks": 5, "editable": True},
            {"id": "mp_2", "desc": "Nominal section placements (Sales/Rent Cr; COS/Wages Dr)", "marks": 4, "editable": True},
            {"id": "mp_3", "desc": f"Equal Trial Balance Totals = {tot}", "marks": 2, "editable": True},
        ],
        misconception_tags=["placing_drawings_in_credit_column", "swapping_sales_and_cost_of_sales_sides"],
    )


def arch_41_post_journals_to_trial_balance_end_to_end(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = _trader_name(rng, sc)
    open_bank = rng.randint(15, 45) * 1000
    open_stock = rng.randint(12, 36) * 500
    open_cap = open_bank + open_stock

    crj_sales = rng.randint(18, 48) * 500
    crj_cos = crj_sales * 100 // 125
    crj_cap = rng.randint(10, 30) * 1000
    crj_bank = crj_sales + crj_cap

    cpj_stock = rng.randint(10, 28) * 500
    cpj_wages = rng.randint(4, 14) * 500
    cpj_bank = cpj_stock + cpj_wages

    close_bank = open_bank + crj_bank - cpj_bank
    close_stock = open_stock + cpj_stock - crj_cos
    close_cap = open_cap + crj_cap
    tb_tot = close_bank + close_stock + crj_cos + cpj_wages

    headers = ["Trial Balance Account", "Folio", "Debit (R)", "Credit (R)"]
    rows = [
        [_cell("t0_r0_c0", "Capital", "given", False), _cell("t0_r0_c1", "B1", "given", False), _cell("t0_r0_c2", "", "must_be_empty", True), _cell("t0_r0_c3", "", "required", True)],
        [_cell("t0_r1_c0", "Trading Stock", "given", False), _cell("t0_r1_c1", "B6", "given", False), _cell("t0_r1_c2", "", "required", True), _cell("t0_r1_c3", "", "must_be_empty", True)],
        [_cell("t0_r2_c0", "Bank", "given", False), _cell("t0_r2_c1", "B7", "given", False), _cell("t0_r2_c2", "", "required", True), _cell("t0_r2_c3", "", "must_be_empty", True)],
        [_cell("t0_r3_c0", "Sales", "given", False), _cell("t0_r3_c1", "N1", "given", False), _cell("t0_r3_c2", "", "must_be_empty", True), _cell("t0_r3_c3", "", "required", True)],
        [_cell("t0_r4_c0", "Cost of Sales", "given", False), _cell("t0_r4_c1", "N2", "given", False), _cell("t0_r4_c2", "", "required", True), _cell("t0_r4_c3", "", "must_be_empty", True)],
        [_cell("t0_r5_c0", "Wages", "given", False), _cell("t0_r5_c1", "N4", "given", False), _cell("t0_r5_c2", "", "required", True), _cell("t0_r5_c3", "", "must_be_empty", True)],
        [_cell("t0_r6_c0", "TOTALS", "given", False), _cell("t0_r6_c1", "", "given", False), _cell("t0_r6_c2", str(tb_tot), "given", False), _cell("t0_r6_c3", str(tb_tot), "given", False)],
    ]
    correct_map = {
        "t0_r0_c3": str(close_cap),
        "t0_r1_c2": str(close_stock),
        "t0_r2_c2": str(close_bank),
        "t0_r3_c3": str(crj_sales),
        "t0_r4_c2": str(crj_cos),
        "t0_r5_c2": str(cpj_wages),
    }
    cell_hints = {
        "t0_r0_c3": f"Opening Capital ({open_cap}) + CRJ Capital ({crj_cap}) = {close_cap}.",
        "t0_r1_c2": f"Opening Stock ({open_stock}) + CPJ Stock ({cpj_stock}) - CRJ COS ({crj_cos}) = {close_stock}.",
        "t0_r2_c2": f"Opening Bank ({open_bank}) + CRJ Bank ({crj_bank}) - CPJ Bank ({cpj_bank}) = {close_bank}.",
        "t0_r3_c3": f"CRJ Sales = {crj_sales}.",
        "t0_r4_c2": f"CRJ Cost of Sales = {crj_cos}.",
        "t0_r5_c2": f"CPJ Wages = {cpj_wages}.",
    }
    prompt = (
        f"Start from **{biz}**'s opening balances (`Bank {_fmt_r(open_bank)}`, `Trading Stock {_fmt_r(open_stock)}`, `Capital {_fmt_r(open_cap)}`) and post these monthly totals:\n"
        f"- **CRJ:** `Bank {_fmt_r(crj_bank)}`, `Sales {_fmt_r(crj_sales)}`, `Cost of Sales {_fmt_r(crj_cos)}`, `Sundry Capital {_fmt_r(crj_cap)}`\n"
        f"- **CPJ:** `Bank {_fmt_r(cpj_bank)}`, `Trading Stock {_fmt_r(cpj_stock)}`, `Wages {_fmt_r(cpj_wages)}`\n\n"
        f"Enter the closing General Ledger balances into the **Trial Balance** below (digits without spaces or R)."
    )
    md = (
        "| Account | Folio | Debit (R) | Credit (R) |\n"
        "| --- | --- | --- | --- |\n"
        f"| Capital | B1 | | **{close_cap}** |\n"
        f"| Trading Stock | B6 | **{close_stock}** | |\n"
        f"| Bank | B7 | **{close_bank}** | |\n"
        f"| Sales | N1 | | **{crj_sales}** |\n"
        f"| Cost of Sales | N2 | **{crj_cos}** | |\n"
        f"| Wages | N4 | **{cpj_wages}** | |\n"
        f"| TOTALS | | {tb_tot} | {tb_tot} |"
    )
    sample = f"Capital Cr {close_cap}; Stock Dr {close_stock}; Bank Dr {close_bank}; Sales Cr {crj_sales}; COS Dr {crj_cos}; Wages Dr {cpj_wages}"
    worked = f"**End-to-End Journals -> Ledger -> Trial Balance Memorandum** [6 marks]\n\n{md}"
    return _build_table(
        rng,
        qid_prefix="g9_gl_41",
        subskill="41_post_journals_to_trial_balance_end_to_end",
        title="Post CRJ & CPJ Movements to Trial Balance",
        prompt=prompt,
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=sample,
        marks=6,
        hints={
            "tier_1": "Update Capital (+CRJ), Trading Stock (+CPJ - CRJ COS), and Bank (+CRJ - CPJ) first.",
            "tier_2": f"Bank = {close_bank}; Stock = {close_stock}; Capital = {close_cap}; check Totals = {tb_tot}.",
            "tier_3": sample,
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Capital ({close_cap}), Stock ({close_stock}), Bank ({close_bank})", "marks": 3, "editable": True},
            {"id": "mp_2", "desc": f"Nominal Sales ({crj_sales}), COS ({crj_cos}), Wages ({cpj_wages})", "marks": 3, "editable": True},
        ],
        misconception_tags=["trial_balance_imbalance_arithmetic"],
    )


def arch_42_visual_trial_balance_error_spot_diagram(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = _trader_name(rng, sc)
    cap = rng.randint(100, 220) * 1000
    sales = rng.randint(30, 70) * 1000
    stock = rng.randint(25, 60) * 1000
    bank = cap + sales - stock - 6000
    cos = 6000
    # Deliberate side swap on Drawings OR Cost of Sales: let's place Cost of Sales on Credit!
    draw = rng.randint(4, 14) * 500
    # Adjust bank so true totals match cleanly:
    bank = cap + sales - stock - cos - draw
    true_tot = cap + sales
    wrong_dr = stock + bank + draw
    wrong_cr = cap + sales + cos

    svg = (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 230" width="540" height="230">'
        '<rect x="4" y="4" width="532" height="222" rx="6" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5"/>'
        f'<text x="270" y="24" font-size="12" font-weight="bold" text-anchor="middle" fill="#0f172a">Draft Trial Balance Extract — {biz}</text>'
        '<line x1="14" y1="34" x2="526" y2="34" stroke="#0f172a" stroke-width="1.5"/>'
        '<text x="20" y="50" font-size="10.5" font-weight="bold" fill="#475569">Account (Folio)</text>'
        '<text x="385" y="50" font-size="10.5" font-weight="bold" text-anchor="end" fill="#475569">Debit (R)</text>'
        '<text x="515" y="50" font-size="10.5" font-weight="bold" text-anchor="end" fill="#475569">Credit (R)</text>'
        f'<text x="20" y="72" font-size="10.5" fill="#0f172a">Capital (B1)</text><text x="515" y="72" font-size="10.5" text-anchor="end" fill="#0f172a">{cap:,}</text>'.replace(",", " ")
        + f'<text x="20" y="92" font-size="10.5" fill="#0f172a">Drawings (B2)</text><text x="385" y="92" font-size="10.5" text-anchor="end" fill="#0f172a">{draw:,}</text>'.replace(",", " ")
        + f'<text x="20" y="112" font-size="10.5" fill="#0f172a">Trading Stock (B6)</text><text x="385" y="112" font-size="10.5" text-anchor="end" fill="#0f172a">{stock:,}</text>'.replace(",", " ")
        + f'<text x="20" y="132" font-size="10.5" fill="#0f172a">Bank (B7)</text><text x="385" y="132" font-size="10.5" text-anchor="end" fill="#0f172a">{bank:,}</text>'.replace(",", " ")
        + f'<text x="20" y="152" font-size="10.5" fill="#0f172a">Sales (N1)</text><text x="515" y="152" font-size="10.5" text-anchor="end" fill="#0f172a">{sales:,}</text>'.replace(",", " ")
        + f'<text x="20" y="172" font-size="10.5" fill="#b91c1c" font-weight="bold">Cost of Sales (N2)</text><text x="515" y="172" font-size="10.5" text-anchor="end" fill="#b91c1c" font-weight="bold">{cos:,}</text>'.replace(",", " ")
        + '<line x1="14" y1="184" x2="526" y2="184" stroke="#0f172a" stroke-width="1.5"/>'
        + f'<text x="20" y="204" font-size="11" font-weight="bold" fill="#0f172a">DRAFT TOTALS</text>'
        + f'<text x="385" y="204" font-size="11" font-weight="bold" text-anchor="end" fill="#b91c1c">{wrong_dr:,}</text>'.replace(",", " ")
        + f'<text x="515" y="204" font-size="11" font-weight="bold" text-anchor="end" fill="#b91c1c">{wrong_cr:,}</text>'.replace(",", " ")
        + "</svg>"
    )
    prompt = (
        f"Inspect the **Draft Trial Balance Extract** above for **{biz}**, which fails to balance "
        f"(`Draft Debit = {_fmt_r(wrong_dr)}`, `Draft Credit = {_fmt_r(wrong_cr)}`).\n\n"
        f"Identify the misplaced account and state the **corrected equal Trial Balance total**."
    )
    correct = f"Cost of Sales ({_fmt_r(cos)}) was placed in Credit instead of Debit; moving it balances both columns at {_fmt_r(true_tot)}."
    distractors = [
        f"Capital ({_fmt_r(cap)}) was placed in Credit instead of Debit; moving it balances at {_fmt_r(wrong_dr)}.",
        f"Trading Stock ({_fmt_r(stock)}) belongs in Credit; moving it balances at {_fmt_r(wrong_cr)}.",
        f"Drawings ({_fmt_r(draw)}) should be deleted completely from the Trial Balance.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g9_gl_42",
        subskill="42_visual_trial_balance_error_spot_diagram",
        title="Spot Column-Placement Error in Draft Trial Balance",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"`Draft Cr - Draft Dr = {_fmt_r(wrong_cr - wrong_dr)} = 2 × {_fmt_r(cos)}`. "
            f"**Cost of Sales (N2)** is an Expense (Debit), so moving **{_fmt_r(cos)}** from Credit to Debit lowers Credit by {_fmt_r(cos)} and raises Debit by {_fmt_r(cos)}, balancing both at **{_fmt_r(true_tot)}**."
        ),
        hints={
            "tier_1": "Compare `Credit - Debit`, divide the difference by 2, and spot the account matching half the imbalance.",
            "tier_2": f"Imbalance = {_fmt_r(2 * cos)}; half = {_fmt_r(cos)} (Cost of Sales on the wrong side!).",
            "tier_3": correct,
        },
        misconception_tags=["swapping_sales_and_cost_of_sales_sides"],
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    )


def arch_43_trial_balance_side_reversal_double_difference_rule(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = _trader_name(rng, sc)
    bal = rng.randint(15, 65) * 150
    diff = 2 * bal
    expected = str(bal)

    prompt = (
        f"During an audit of **{biz}**'s Trial Balance, Total Debits exceed Total Credits by **{_fmt_r(diff)}** "
        f"because a single account balance was accidentally placed in the **Debit** column instead of the **Credit** column.\n\n"
        f"What is the **exact Rand balance** of that misplaced Credit account?\n*(Enter digits without spaces or R.)*"
    )
    worked = (
        f"**Double-Difference Reversal Diagnosis** [2 marks]\n\n"
        f"- Placing a Credit item of `x` in the Debit column subtracts `x` from Credit and adds `x` to Debit, creating a difference of `2x`.\n"
        f"- `2x = {_fmt_r(diff)}` -> `x = {_fmt_r(diff)} ÷ 2 = {_fmt_r(bal)}` -> Answer: `{expected}`"
    )
    return _build_short(
        rng,
        qid_prefix="g9_gl_43",
        subskill="43_trial_balance_side_reversal_double_difference_rule",
        title="Side-Reversal Double-Difference Rule in Trial Balance",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=worked,
        marks=2,
        hints={
            "tier_1": "Putting a Credit figure into Debit causes an imbalance equal to TWICE the balance.",
            "tier_2": f"Divide the total Trial Balance difference ({_fmt_r(diff)}) by 2.",
            "tier_3": f"Account balance = {expected}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Divides {_fmt_r(diff)} by 2 = {_fmt_r(bal)}", "marks": 2, "editable": True},
        ],
        misconception_tags=["trial_balance_imbalance_arithmetic"],
    )


def arch_44_errors_not_revealed_by_trial_balance_mcq(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = _trader_name(rng, sc)
    amt = rng.randint(4, 20) * 250

    prompt = (
        f"The Trial Balance of **{biz}** balances with equal Debit and Credit totals, yet an error occurred during the month when **{_fmt_r(amt)}** for **Packing Material** was debited to **Stationery** instead (while Bank was correctly credited).\n\n"
        f"Why did the Trial Balance **still balance**, and what does this prove?"
    )
    correct = f"Because equal Debits and Credits of {_fmt_r(amt)} were still posted; a balanced Trial Balance proves arithmetical Debit=Credit equality, NOT error-free accounting."
    distractors = [
        "Because Stationery and Packing Material are automatically combined into Capital at month-end.",
        "Because the General Ledger deletes any transaction that enters the wrong expense account.",
        "Because Bank was credited twice to compensate for the Stationery debit.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g9_gl_44",
        subskill="44_errors_not_revealed_by_trial_balance_mcq",
        title="Errors Not Revealed by a Balanced Trial Balance",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"Since a Debit of **{_fmt_r(amt)}** (albeit to `Stationery` instead of `Packing Material`) still matched the Credit of **{_fmt_r(amt)}** to `Bank`, "
            f"the Trial Balance remains equal (`error of principle/commission`, plus complete omissions, remain undetected by column totals)."
        ),
        hints={
            "tier_1": "Ask whether `Total Debits` still equals `Total Credits` when one Debit expense replaces another Debit expense.",
            "tier_2": "A balanced Trial Balance catches uneven Dr/Cr postings, not same-side misclassifications or complete omissions.",
            "tier_3": correct,
        },
        misconception_tags=["assuming_balanced_trial_balance_means_zero_errors"],
    )


def arch_45_diagnose_sundry_posted_at_month_end_error(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = _trader_name(rng, sc)
    m_name, _, last_d, _, _, _ = rng.choice(MONTH_YEARS)
    equip = rng.randint(10, 30) * 500
    draw = rng.randint(3, 12) * 400
    tot_sun = equip + draw

    prompt = (
        f"When posting **{biz}**'s CPJ for **{m_name}**, a trainee writes **one lump-sum entry of {_fmt_r(tot_sun)}** on **{last_d} {m_name}** "
        f"into `Sundry Account` instead of posting **Equipment ({_fmt_r(equip)}) on Day 07** and **Drawings ({_fmt_r(draw)}) on Day 21**.\n\n"
        f"Explain what is wrong with this posting."
    )
    correct = "There is NO single ledger account called 'Sundry Account'; every Sundry item must be posted individually to its named ledger account on its transaction date."
    distractors = [
        f"Only Equipment should be posted; Drawings must be omitted from the General Ledger.",
        f"Both items should be posted to the Credit side of Bank as two separate Totals lines.",
        f"Lump-sum Sundry posting is correct as long as the date is written as the 1st of the month.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g9_gl_45",
        subskill="45_diagnose_sundry_posted_at_month_end_error",
        title="Diagnose Month-End Lump-Sum Sundry Posting Error",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"**`Sundry Accounts`** in CRJ/CPJ is merely a multi-account journal column, NOT a General Ledger account. "
            f"**Equipment ({_fmt_r(equip)})** posts on **Day 07** and **Drawings ({_fmt_r(draw)})** posts on **Day 21**."
        ),
        hints={
            "tier_1": "Check if 'Sundry Account' exists in the General Ledger or Trial Balance.",
            "tier_2": "Sundry entries always post individually on their transaction day to their named account.",
            "tier_3": correct,
        },
        misconception_tags=["posting_sundry_column_total_as_one_account", "posting_sundry_on_month_end_date"],
    )


def arch_46_diagnose_cost_of_sales_posted_to_bank_error(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = _trader_name(rng, sc)
    sales = rng.randint(15, 45) * 500
    cos = sales * 100 // 125

    prompt = (
        f"While posting **{biz}**'s CRJ (`Sales = {_fmt_r(sales)}`, `Cost of Sales = {_fmt_r(cos)}`), a learner debits **Bank** with **{_fmt_r(sales + cos)}** "
        f"and credits **Cost of Sales** with **{_fmt_r(cos)}**.\n\n"
        f"Identify BOTH errors in the learner's posting."
    )
    correct = f"Cost of Sales ({_fmt_r(cos)}) is a non-cash memo figure so Bank must NOT include it, and Cost of Sales is DEBITED against a CREDIT to Trading Stock."
    distractors = [
        f"Sales ({_fmt_r(sales)}) should also be excluded from Bank so Bank equals Cost of Sales only.",
        f"Trading Stock should be debited with {_fmt_r(sales + cos)} and Bank credited with {_fmt_r(cos)}.",
        f"Cost of Sales belongs exclusively in the Cash Payments Journal, never in the CRJ or General Ledger.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g9_gl_46",
        subskill="46_diagnose_cost_of_sales_posted_to_bank_error",
        title="Diagnose Cost of Sales Posted to Bank Error",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"1. **Bank** records actual cash received only (so adding non-cash `{_fmt_r(cos)}` overstates Bank!).\n"
            f"2. **Cost of Sales** is an **Expense** (Debited, Details: `Trading Stock`) paired with **Trading Stock** Credited (Details: `Cost of Sales`)."
        ),
        hints={
            "tier_1": "Check whether Cost of Sales represents cash deposited into the bank.",
            "tier_2": "Cost of Sales never enters Bank; it pairs Debit Cost of Sales with Credit Trading Stock.",
            "tier_3": correct,
        },
        misconception_tags=["posting_cost_of_sales_to_bank"],
    )


def arch_47_calculate_net_profit_from_nominal_section_trial_balance(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = _trader_name(rng, sc)
    sales = rng.randint(45, 95) * 1000
    cos = sales * 100 // 150
    rent_inc = rng.randint(4, 14) * 500
    wages = rng.randint(6, 16) * 500
    rent_exp = rng.randint(4, 12) * 500
    stat = rng.randint(2, 8) * 250
    net_profit = (sales - cos) + rent_inc - (wages + rent_exp + stat)
    expected = str(net_profit)

    prompt = (
        f"Extract the **Nominal accounts section** from **{biz}**'s Trial Balance:\n"
        f"- **Sales (N1):** {_fmt_r(sales)} (Cr)\n"
        f"- **Cost of Sales (N2):** {_fmt_r(cos)} (Dr)\n"
        f"- **Rent Income (N3):** {_fmt_r(rent_inc)} (Cr)\n"
        f"- **Wages (N4):** {_fmt_r(wages)} (Dr)\n"
        f"- **Rent Expense (N10):** {_fmt_r(rent_exp)} (Dr)\n"
        f"- **Stationery (N7):** {_fmt_r(stat)} (Dr)\n\n"
        f"Calculate the business's **Net Profit** (`Total Incomes - Total Expenses including Cost of Sales`).\n*(Enter digits without spaces or R.)*"
    )
    worked = (
        f"**Net Profit from Trial Balance Nominal Section** [4 marks]\n\n"
        f"- Gross Profit = `Sales ({_fmt_r(sales)}) - Cost of Sales ({_fmt_r(cos)}) = {_fmt_r(sales - cos)}`\n"
        f"- Add Other Income (`Rent Income`): `+{_fmt_r(rent_inc)}` -> Total Income after COS = `{_fmt_r(sales - cos + rent_inc)}`\n"
        f"- Less Operating Expenses: `{_fmt_r(wages)} + {_fmt_r(rent_exp)} + {_fmt_r(stat)} = {_fmt_r(wages + rent_exp + stat)}`\n"
        f"- **Net Profit** = `{_fmt_r(net_profit)}` -> Answer: `{expected}`"
    )
    return _build_short(
        rng,
        qid_prefix="g9_gl_47",
        subskill="47_calculate_net_profit_from_nominal_section_trial_balance",
        title="Calculate Net Profit from Nominal Trial Balance Section",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=worked,
        marks=4,
        hints={
            "tier_1": "Only use Nominal (N) accounts: sum all Credits (Sales + Rent Income) and subtract all Debits (Cost of Sales + Expenses).",
            "tier_2": f"Incomes = {_fmt_r(sales + rent_inc)}; Debits = {_fmt_r(cos + wages + rent_exp + stat)}.",
            "tier_3": f"Net Profit = {expected}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Gross Profit = {_fmt_r(sales - cos)}", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": f"Adds Rent Income and subtracts operating expenses = {_fmt_r(net_profit)}", "marks": 3, "editable": True},
        ],
        misconception_tags=["including_balance_sheet_items_in_net_profit"],
    )


def arch_48_calculate_closing_equity_from_trial_balance(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = _trader_name(rng, sc)
    cap = rng.randint(140, 280) * 1000
    draw = rng.randint(6, 22) * 500
    net_profit = rng.randint(18, 55) * 500
    close_eq = cap + net_profit - draw
    expected = str(close_eq)

    prompt = (
        f"From **{biz}**'s year-end Trial Balance:\n"
        f"- **Capital (B1):** {_fmt_r(cap)}\n"
        f"- **Drawings (B2):** {_fmt_r(draw)}\n"
        f"- **Calculated Net Profit:** {_fmt_r(net_profit)}\n\n"
        f"Calculate the closing **Owner's Equity** (`Capital + Net Profit - Drawings`).\n*(Enter digits without spaces or R.)*"
    )
    worked = (
        f"**Closing Owner's Equity Calculation** [3 marks]\n\n"
        f"- Capital: `{_fmt_r(cap)}`\n"
        f"- Add Net Profit: `+{_fmt_r(net_profit)}`\n"
        f"- Less Drawings: `-{_fmt_r(draw)}`\n"
        f"- **Closing Owner's Equity** = `{_fmt_r(close_eq)}` -> Answer: `{expected}`"
    )
    return _build_short(
        rng,
        qid_prefix="g9_gl_48",
        subskill="48_calculate_closing_equity_from_trial_balance",
        title="Calculate Closing Owner's Equity from Trial Balance",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=worked,
        marks=3,
        hints={
            "tier_1": "Net Profit increases Owner's Equity; Drawings reduces Owner's Equity.",
            "tier_2": f"Equity = {_fmt_r(cap)} + {_fmt_r(net_profit)} - {_fmt_r(draw)}.",
            "tier_3": f"Closing Owner's Equity = {expected}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Capital + Net Profit - Drawings = {_fmt_r(close_eq)}", "marks": 3, "editable": True},
        ],
        misconception_tags=["adding_drawings_to_capital"],
    )


def arch_49_accounting_equation_from_general_ledger_entries(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = _trader_name(rng, sc)
    cos_amt = rng.randint(12, 36) * 250
    wages_amt = rng.randint(4, 14) * 250
    cap_amt = rng.randint(20, 60) * 1000

    headers = ["General Ledger Entry", "Source Journal (`CRJ` / `CPJ`)", "Assets Effect (`+/-` or `0`)", "Owner's Equity Effect (`+/-` or `0`)"]
    rows = [
        [_cell("t0_r0_c0", f"Dr Cost of Sales / Cr Trading Stock ({_fmt_r(cos_amt)})", "given", False), _cell("t0_r0_c1", "", "required", True), _cell("t0_r0_c2", "", "required", True), _cell("t0_r0_c3", "", "required", True)],
        [_cell("t0_r1_c0", f"Dr Wages / Cr Bank ({_fmt_r(wages_amt)})", "given", False), _cell("t0_r1_c1", "", "required", True), _cell("t0_r1_c2", "", "required", True), _cell("t0_r1_c3", "", "required", True)],
        [_cell("t0_r2_c0", f"Dr Bank / Cr Capital ({_fmt_r(cap_amt)})", "given", False), _cell("t0_r2_c1", "", "required", True), _cell("t0_r2_c2", "", "required", True), _cell("t0_r2_c3", "", "required", True)],
    ]
    correct_map = {
        "t0_r0_c1": "CRJ",
        "t0_r0_c2": f"-{cos_amt}",
        "t0_r0_c3": f"-{cos_amt}",
        "t0_r1_c1": "CPJ",
        "t0_r1_c2": f"-{wages_amt}",
        "t0_r1_c3": f"-{wages_amt}",
        "t0_r2_c1": "CRJ",
        "t0_r2_c2": f"+{cap_amt}",
        "t0_r2_c3": f"+{cap_amt}",
    }
    cell_hints = {
        "t0_r0_c1": "Cost of Sales accompanies Cash Sales in the CRJ.",
        "t0_r0_c2": f"Trading Stock decreases Assets (-{cos_amt}).",
        "t0_r0_c3": f"Cost of Sales expense decreases OE (-{cos_amt}).",
        "t0_r1_c1": "Wages paid out of Bank uses CPJ.",
        "t0_r1_c2": f"Bank decreases Assets (-{wages_amt}).",
        "t0_r1_c3": f"Wages expense decreases OE (-{wages_amt}).",
        "t0_r2_c1": "Capital cash received uses CRJ.",
        "t0_r2_c2": f"Bank increases Assets (+{cap_amt}).",
        "t0_r2_c3": f"Capital contribution increases OE (+{cap_amt}).",
    }
    prompt = (
        f"Translate these three General Ledger double entries from **{biz}** back into their **Source Journal** and **Accounting Equation (`A = OE + L`)** effects "
        f"(include `+` or `-` without spaces or R):"
    )
    md = (
        "| General Ledger Entry | Journal | Assets Effect | Owner's Equity Effect |\n"
        "| --- | --- | --- | --- |\n"
        f"| Dr Cost of Sales / Cr Trading Stock ({_fmt_r(cos_amt)}) | **CRJ** | **-{cos_amt}** | **-{cos_amt}** |\n"
        f"| Dr Wages / Cr Bank ({_fmt_r(wages_amt)}) | **CPJ** | **-{wages_amt}** | **-{wages_amt}** |\n"
        f"| Dr Bank / Cr Capital ({_fmt_r(cap_amt)}) | **CRJ** | **+{cap_amt}** | **+{cap_amt}** |"
    )
    sample = f"COS/Stock: CRJ A-{cos_amt} OE-{cos_amt}; Wages/Bank: CPJ A-{wages_amt} OE-{wages_amt}; Bank/Cap: CRJ A+{cap_amt} OE+{cap_amt}"
    worked = f"**General Ledger -> Accounting Equation Memorandum** [9 marks]\n\n{md}"
    return _build_table(
        rng,
        qid_prefix="g9_gl_49",
        subskill="49_accounting_equation_from_general_ledger_entries",
        title="Accounting Equation Effects from General Ledger Entries",
        prompt=prompt,
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=sample,
        marks=9,
        hints={
            "tier_1": "Debit Expenses reduce OE; Credit Trading Stock reduces Assets; Capital & Bank increase OE & Assets.",
            "tier_2": f"Cost of Sales uses CRJ (-{cos_amt}); Wages uses CPJ (-{wages_amt}); Capital uses CRJ (+{cap_amt}).",
            "tier_3": sample,
        },
        marking_points=[
            {"id": "mp_1", "desc": f"COS/Trading Stock: CRJ, A-{cos_amt}, OE-{cos_amt}", "marks": 3, "editable": True},
            {"id": "mp_2", "desc": f"Wages/Bank: CPJ, A-{wages_amt}, OE-{wages_amt}", "marks": 3, "editable": True},
            {"id": "mp_3", "desc": f"Bank/Capital: CRJ, A+{cap_amt}, OE+{cap_amt}", "marks": 3, "editable": True},
        ],
        misconception_tags=["omitting_cost_of_sales_second_entry"],
    )


def arch_50_comprehensive_sole_trader_gl_and_trial_balance_audit(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = _trader_name(rng, sc)
    open_bank = rng.randint(15, 40) * 1000
    open_stock = rng.randint(12, 32) * 500
    open_cap = open_bank + open_stock

    crj_cos = rng.randint(10, 28) * 500
    crj_sales = crj_cos * 140 // 100
    crj_cap = rng.randint(10, 25) * 1000
    crj_bank = crj_sales + crj_cap

    cpj_stock = rng.randint(10, 26) * 500
    cpj_draw = rng.randint(3, 10) * 500
    cpj_wages = rng.randint(4, 12) * 500
    cpj_bank = cpj_stock + cpj_draw + cpj_wages

    close_bank = open_bank + crj_bank - cpj_bank
    close_stock = open_stock + cpj_stock - crj_cos
    close_cap = open_cap + crj_cap
    tb_tot = close_bank + close_stock + cpj_draw + crj_cos + cpj_wages

    headers = ["Audit Item", "Ledger Derivation", "Closing Trial Balance Figure (R)"]
    specs = [
        ("Capital (B1) — Credit", f"{open_cap} + {crj_cap}", str(close_cap)),
        ("Drawings (B2) — Debit", "From CPJ Sundry", str(cpj_draw)),
        ("Trading Stock (B6) — Debit", f"{open_stock} + {cpj_stock} - {crj_cos}", str(close_stock)),
        ("Bank (B7) — Debit", f"{open_bank} + {crj_bank} - {cpj_bank}", str(close_bank)),
        ("Sales (N1) — Credit", "CRJ Sales Total", str(crj_sales)),
        ("Trial Balance Total (Dr = Cr)", "Capital + Sales = All Debits", str(tb_tot)),
    ]
    rows: List[List[Dict[str, Any]]] = []
    correct_map: Dict[str, str] = {}
    cell_hints: Dict[str, str] = {}
    md_lines = ["| Audit Item | Ledger Derivation | Closing Trial Balance Figure (R) |", "| --- | --- | --- |"]

    for i, (item, deriv, val) in enumerate(specs):
        ed = i in (0, 2, 3, 5)
        if ed:
            correct_map[f"t0_r{i}_c2"] = val
            cell_hints[f"t0_r{i}_c2"] = f"Compute {deriv} (enter digits without spaces or R)."
        rows.append([
            _cell(f"t0_r{i}_c0", item, "given", False),
            _cell(f"t0_r{i}_c1", deriv, "given", False),
            _cell(f"t0_r{i}_c2", "" if ed else val, "required" if ed else "given", ed),
        ])
        md_lines.append(f"| {item} | {deriv} | **{_fmt_r(int(val))}** |" if ed else f"| {item} | {deriv} | {_fmt_r(int(val))} |")

    prompt = (
        f"Perform a month-end General Ledger & Trial Balance audit for **{biz}** (plus `Cost of Sales = {_fmt_r(crj_cos)}` and `Wages = {_fmt_r(cpj_wages)}` in Debit):\n"
        f"- Opening Balances: `Bank {_fmt_r(open_bank)}`, `Trading Stock {_fmt_r(open_stock)}`, `Capital {_fmt_r(open_cap)}`\n"
        f"- **CRJ:** `Bank {_fmt_r(crj_bank)}`, `Sales {_fmt_r(crj_sales)}`, `COS {_fmt_r(crj_cos)}`, `Capital {_fmt_r(crj_cap)}`\n"
        f"- **CPJ:** `Bank {_fmt_r(cpj_bank)}`, `Trading Stock {_fmt_r(cpj_stock)}`, `Wages {_fmt_r(cpj_wages)}`, `Drawings {_fmt_r(cpj_draw)}`\n\n"
        f"Calculate the missing closing figures (`Capital`, `Trading Stock`, `Bank`, and `Trial Balance Total`)."
    )
    sample = f"Capital {close_cap}; Trading Stock {close_stock}; Bank {close_bank}; Trial Balance Total = {tb_tot}"
    worked = f"**Comprehensive General Ledger & Trial Balance Audit** [8 marks]\n\n" + "\n".join(md_lines)
    return _build_table(
        rng,
        qid_prefix="g9_gl_50",
        subskill="50_comprehensive_sole_trader_gl_and_trial_balance_audit",
        title="Comprehensive General Ledger & Trial Balance Audit",
        prompt=prompt,
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=sample,
        marks=8,
        hints={
            "tier_1": "Update each B-account balance using opening + inflows - outflows, then sum Credits = Capital + Sales.",
            "tier_2": f"Capital = {close_cap}; Stock = {close_stock}; Bank = {close_bank}; Totals = {close_cap} + {crj_sales} = {tb_tot}.",
            "tier_3": sample,
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Closing Capital = {close_cap}", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": f"Closing Trading Stock = {close_stock}", "marks": 2, "editable": True},
            {"id": "mp_3", "desc": f"Closing Bank = {close_bank}", "marks": 2, "editable": True},
            {"id": "mp_4", "desc": f"Equal Trial Balance Total = {tb_tot}", "marks": 2, "editable": True},
        ],
        misconception_tags=["trial_balance_imbalance_arithmetic"],
    )


BUILDERS_26_50 = {
    "26_cash_float_t_account_posting_and_increase": arch_26_cash_float_t_account_posting_and_increase,
    "27_rent_income_vs_rent_expense_classification": arch_27_rent_income_vs_rent_expense_classification,
    "28_stock_control_theft_or_shrinkage_detection": arch_28_stock_control_theft_or_shrinkage_detection,
    "29_bank_ledger_extract_with_bank_table": arch_29_bank_ledger_extract_with_subskill_bank_table,
    "30_trading_stock_ledger_with_shrinkage_check": arch_30_trading_stock_ledger_with_shrinkage_check,
    "31_trial_balance_purpose_and_structure_mcq": arch_31_trial_balance_purpose_and_structure_mcq,
    "32_balance_sheet_vs_nominal_section_sorting_table": arch_32_balance_sheet_vs_nominal_section_sorting_table,
    "33_trial_balance_favourable_bank_placement": arch_33_trial_balance_favourable_bank_placement,
    "34_trial_balance_bank_overdraft_placement": arch_34_trial_balance_bank_overdraft_placement,
    "35_trial_balance_capital_and_drawings_opposite_columns": arch_35_trial_balance_capital_and_drawings_opposite_columns,
    "36_trial_balance_sales_and_cost_of_sales_placement": arch_36_trial_balance_sales_and_cost_of_sales_placement,
    "37_trial_balance_operating_incomes_vs_expenses": arch_37_trial_balance_operating_incomes_vs_expenses,
    "38_missing_capital_balance_from_trial_balance_table": arch_38_missing_capital_balance_from_trial_balance_table,
    "39_missing_bank_or_drawings_from_trial_balance": arch_39_missing_bank_or_drawings_from_trial_balance,
    "40_full_sole_trader_trial_balance_compilation": arch_40_full_sole_trader_trial_balance_compilation,
    "41_post_journals_to_trial_balance_end_to_end": arch_41_post_journals_to_trial_balance_end_to_end,
    "42_visual_trial_balance_error_spot_diagram": arch_42_visual_trial_balance_error_spot_diagram,
    "43_trial_balance_side_reversal_double_difference_rule": arch_43_trial_balance_side_reversal_double_difference_rule,
    "44_errors_not_revealed_by_trial_balance_mcq": arch_44_errors_not_revealed_by_trial_balance_mcq,
    "45_diagnose_sundry_posted_at_month_end_error": arch_45_diagnose_sundry_posted_at_month_end_error,
    "46_diagnose_cost_of_sales_posted_to_bank_error": arch_46_diagnose_cost_of_sales_posted_to_bank_error,
    "47_calculate_net_profit_from_nominal_section_trial_balance": arch_47_calculate_net_profit_from_nominal_section_trial_balance,
    "48_calculate_closing_equity_from_trial_balance": arch_48_calculate_closing_equity_from_trial_balance,
    "49_accounting_equation_from_general_ledger_entries": arch_49_accounting_equation_from_general_ledger_entries,
    "50_comprehensive_sole_trader_gl_and_trial_balance_audit": arch_50_comprehensive_sole_trader_gl_and_trial_balance_audit,
}
