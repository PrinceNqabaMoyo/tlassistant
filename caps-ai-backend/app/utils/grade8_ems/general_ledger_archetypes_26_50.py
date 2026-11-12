"""Grade 8 EMS - General Ledger & Trial Balance of a Service Business: Archetypes 26 to 50.
Grounded strictly in curriculum_docs_auto/EMS_Gr8/Term 1/01. General ledger and Trial balance of a service business.md
and EMS_Gr8/Syllabus.md.
Zero-LLM, 100% deterministic, authentic South African Rand (R) contexts.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List

from app.utils.ems_namelist import get_ems_scenario
from .general_ledger_archetypes_01_25 import (
    _build_mcq,
    _build_short,
    _build_table,
    _fmt_r,
    _t_account_svg,
)


def arch_26_crj_to_bank_and_current_income_t_accounts(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    cur_inc = rng.randint(14, 38) * 500
    cap = rng.randint(15, 45) * 1000
    rent = rng.randint(3, 9) * 500
    bank_tot = cur_inc + cap + rent

    postings = [
        ("Bank", "Total Receipts (CRJ)", "Debit", str(bank_tot)),
        ("Current Income", "Bank (CRJ)", "Credit", str(cur_inc)),
        ("Capital", "Bank (CRJ)", "Credit", str(cap)),
        ("Rent Income", "Bank (CRJ)", "Credit", str(rent)),
    ]
    headers = ["General Ledger Account", "Details (Contra Account)", "Side (Debit / Credit)", "Amount (R)"]
    rows = []
    correct_map: Dict[str, str] = {}
    cell_hints: Dict[str, str] = {}
    md_lines = ["| General Ledger Account | Details | Side | Amount (R) |", "| --- | --- | --- | --- |"]

    for i, (acc, det, side, amt) in enumerate(postings):
        correct_map[f"t0_r{i}_c1"] = det
        correct_map[f"t0_r{i}_c2"] = side
        correct_map[f"t0_r{i}_c3"] = amt
        cell_hints[f"t0_r{i}_c1"] = "State the contra account with journal source, e.g. 'Total Receipts (CRJ)' for Bank or 'Bank (CRJ)'."
        cell_hints[f"t0_r{i}_c2"] = f"Apply DEAD CLIC to {acc} when cash is received."
        cell_hints[f"t0_r{i}_c3"] = f"Enter the numeric Rand total without spaces or R symbol ({amt})."
        rows.append([
            {"coordinate": f"t0_r{i}_c0", "cell_id": f"t0_r{i}_c0", "value": acc, "type": "given", "editable": False},
            {"coordinate": f"t0_r{i}_c1", "cell_id": f"t0_r{i}_c1", "value": "", "type": "required", "editable": True},
            {"coordinate": f"t0_r{i}_c2", "cell_id": f"t0_r{i}_c2", "value": "", "type": "required", "editable": True},
            {"coordinate": f"t0_r{i}_c3", "cell_id": f"t0_r{i}_c3", "value": "", "type": "required", "editable": True},
        ])
        md_lines.append(f"| {acc} | **{det}** | **{side}** | **{amt}** |")

    prompt = (
        f"The Cash Receipts Journal (CRJ) of **{sc['entrepreneur']}'s {sc['business_type']}** for May shows:\n"
        f"- **Bank column total:** {_fmt_r(bank_tot)}\n"
        f"- **Current Income column total:** {_fmt_r(cur_inc)}\n"
        f"- **Sundry Accounts:** May 2 Capital {_fmt_r(cap)}; May 20 Rent Income {_fmt_r(rent)}\n\n"
        f"Complete the General Ledger posting summary table below (`Details`, `Side`, and numeric `Amount (R)`)."
    )
    sample = f"Bank Dr {bank_tot}; Current Income Cr {cur_inc}; Capital Cr {cap}; Rent Income Cr {rent}"
    worked = "**CRJ General Ledger Posting Memorandum** [12 marks]:\n\n" + "\n".join(md_lines)
    return _build_table(
        rng,
        qid_prefix="g8_gl_26",
        subskill="26_crj_to_bank_and_current_income_t_accounts",
        title="Posting CRJ Totals & Sundry Items Table",
        prompt=prompt,
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=sample,
        marks=12,
        hints={
            "tier_1": "CRJ Bank total equals Current Income + Sundry items; Debit Bank and Credit each source account.",
            "tier_2": f"Bank Dr = {bank_tot}; Credit accounts sum to {cur_inc} + {cap} + {rent} = {bank_tot}.",
            "tier_3": sample,
        },
        marking_points=[{"id": f"mp_{i}", "desc": f"Posting for {postings[i][0]}", "marks": 3, "editable": True} for i in range(4)],
        misconception_tags=["crj_posting_side_reversal"],
    )


def arch_27_cpj_to_bank_and_expense_t_accounts(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    wages = rng.randint(6, 18) * 500
    stat = rng.randint(2, 9) * 200
    equip = rng.randint(8, 25) * 500
    draw = rng.randint(3, 10) * 500
    bank_tot = wages + stat + equip + draw

    postings = [
        ("Bank", "Total Payments (CPJ)", "Credit", str(bank_tot)),
        ("Wages", "Bank (CPJ)", "Debit", str(wages)),
        ("Stationery", "Bank (CPJ)", "Debit", str(stat)),
        ("Equipment", "Bank (CPJ)", "Debit", str(equip)),
        ("Drawings", "Bank (CPJ)", "Debit", str(draw)),
    ]
    headers = ["General Ledger Account", "Details (Contra Account)", "Side (Debit / Credit)", "Amount (R)"]
    rows = []
    correct_map: Dict[str, str] = {}
    cell_hints: Dict[str, str] = {}
    md_lines = ["| General Ledger Account | Details | Side | Amount (R) |", "| --- | --- | --- | --- |"]

    for i, (acc, det, side, amt) in enumerate(postings):
        correct_map[f"t0_r{i}_c1"] = det
        correct_map[f"t0_r{i}_c2"] = side
        correct_map[f"t0_r{i}_c3"] = amt
        cell_hints[f"t0_r{i}_c1"] = "Use 'Total Payments (CPJ)' for Bank, or 'Bank (CPJ)' for CPJ expense/sundry accounts."
        cell_hints[f"t0_r{i}_c2"] = f"Bank decreases on Credit; Expenses, Equipment (Asset), and Drawings increase on Debit."
        cell_hints[f"t0_r{i}_c3"] = f"Enter numeric amount ({amt})."
        rows.append([
            {"coordinate": f"t0_r{i}_c0", "cell_id": f"t0_r{i}_c0", "value": acc, "type": "given", "editable": False},
            {"coordinate": f"t0_r{i}_c1", "cell_id": f"t0_r{i}_c1", "value": "", "type": "required", "editable": True},
            {"coordinate": f"t0_r{i}_c2", "cell_id": f"t0_r{i}_c2", "value": "", "type": "required", "editable": True},
            {"coordinate": f"t0_r{i}_c3", "cell_id": f"t0_r{i}_c3", "value": "", "type": "required", "editable": True},
        ])
        md_lines.append(f"| {acc} | **{det}** | **{side}** | **{amt}** |")

    prompt = (
        f"The Cash Payments Journal (CPJ) of **{sc['entrepreneur']}'s {sc['business_type']}** for June reflects:\n"
        f"- **Bank total:** {_fmt_r(bank_tot)}\n"
        f"- **Wages total:** {_fmt_r(wages)}\n"
        f"- **Stationery total:** {_fmt_r(stat)}\n"
        f"- **Sundry Accounts:** June 6 Equipment {_fmt_r(equip)}; June 25 Drawings {_fmt_r(draw)}\n\n"
        f"Complete the General Ledger posting summary table below."
    )
    sample = f"Bank Cr {bank_tot}; Wages Dr {wages}; Stationery Dr {stat}; Equipment Dr {equip}; Drawings Dr {draw}"
    worked = "**CPJ General Ledger Posting Memorandum** [15 marks]:\n\n" + "\n".join(md_lines)
    return _build_table(
        rng,
        qid_prefix="g8_gl_27",
        subskill="27_cpj_to_bank_and_expense_t_accounts",
        title="Posting CPJ Totals & Sundry Items Table",
        prompt=prompt,
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=sample,
        marks=15,
        hints={
            "tier_1": "CPJ Bank total is Credited; Wages, Stationery, Equipment, and Drawings are Debited.",
            "tier_2": f"Check double entry: {wages} + {stat} + {equip} + {draw} = {bank_tot}.",
            "tier_3": sample,
        },
        marking_points=[{"id": f"mp_{i}", "desc": f"Posting for {postings[i][0]}", "marks": 3, "editable": True} for i in range(5)],
        misconception_tags=["cpj_debit_bank_error"],
    )


def arch_28_mixed_crj_cpj_posting_table(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    c_inc = rng.randint(15, 35) * 400
    tel = rng.randint(3, 9) * 150
    w_e = rng.randint(4, 12) * 200
    veh = rng.randint(40, 90) * 1000
    entries = [
        ("CRJ", "Current Income", str(c_inc), "Credit", "End of month"),
        ("CPJ", "Telephone", str(tel), "Debit", "End of month"),
        ("CPJ", "Water and Electricity", str(w_e), "Debit", "Transaction date"),
        ("CPJ", "Vehicles", str(veh), "Debit", "Transaction date"),
    ]
    headers = ["Source Journal", "Target Account", "Amount (R)", "Side Posted (Debit / Credit)", "Posting Timing (End of month / Transaction date)"]
    rows = []
    correct_map: Dict[str, str] = {}
    cell_hints: Dict[str, str] = {}
    md_lines = ["| Journal | Account | Amount (R) | Side Posted | Timing |", "| --- | --- | --- | --- | --- |"]

    for i, (jrn, acc, amt, side, timing) in enumerate(entries):
        correct_map[f"t0_r{i}_c3"] = side
        correct_map[f"t0_r{i}_c4"] = timing
        cell_hints[f"t0_r{i}_c3"] = f"From {jrn}, decide whether {acc} is Debited or Credited."
        cell_hints[f"t0_r{i}_c4"] = "Dedicated columns post 'End of month'; Sundry column items post on 'Transaction date'."
        rows.append([
            {"coordinate": f"t0_r{i}_c0", "cell_id": f"t0_r{i}_c0", "value": jrn, "type": "given", "editable": False},
            {"coordinate": f"t0_r{i}_c1", "cell_id": f"t0_r{i}_c1", "value": acc, "type": "given", "editable": False},
            {"coordinate": f"t0_r{i}_c2", "cell_id": f"t0_r{i}_c2", "value": amt, "type": "given", "editable": False},
            {"coordinate": f"t0_r{i}_c3", "cell_id": f"t0_r{i}_c3", "value": "", "type": "required", "editable": True},
            {"coordinate": f"t0_r{i}_c4", "cell_id": f"t0_r{i}_c4", "value": "", "type": "required", "editable": True},
        ])
        md_lines.append(f"| {jrn} | {acc} | {amt} | **{side}** | **{timing}** |")

    prompt = (
        f"For **{sc['entrepreneur']}'s {sc['business_type']}**, Current Income and Telephone have dedicated special columns in the CRJ/CPJ, "
        f"while Water and Electricity and Vehicles appear in Sundry Accounts.\n\n"
        f"Complete the mixed posting schedule (`Side Posted` and `Posting Timing`)."
    )
    sample = "; ".join(f"{a}: {s} ({t})" for _, a, _, s, t in entries)
    worked = "**Mixed CRJ/CPJ Posting Schedule** [8 marks]:\n\n" + "\n".join(md_lines)
    return _build_table(
        rng,
        qid_prefix="g8_gl_28",
        subskill="28_mixed_crj_cpj_posting_table",
        title="Mixed CRJ & CPJ Ledger Posting Table",
        prompt=prompt,
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=sample,
        marks=8,
        hints={
            "tier_1": "Income increases Credit; Expenses and Vehicles increase Debit.",
            "tier_2": "Special columns use End of month; Sundry accounts use Transaction date.",
            "tier_3": sample,
        },
        marking_points=[{"id": f"mp_{i}", "desc": f"Side and timing for {entries[i][1]}", "marks": 2, "editable": True} for i in range(4)],
        misconception_tags=["posting_sundry_column_total_error"],
    )


def arch_29_balancing_bank_t_account_debit_balance(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    opening_bal = rng.randint(8, 25) * 1000
    crj_total = rng.randint(15, 35) * 1000
    cpj_total = rng.randint(10, 22) * 1000
    total_debit = opening_bal + crj_total
    closing_bal = total_debit - cpj_total

    headers = ["Day", "Details (Debit)", "Amount (R)", "Day", "Details (Credit)", "Amount (R)"]
    rows = [
        [
            {"coordinate": "t0_r0_c0", "cell_id": "t0_r0_c0", "value": "May 1", "type": "given", "editable": False},
            {"coordinate": "t0_r0_c1", "cell_id": "t0_r0_c1", "value": "Balance b/d", "type": "given", "editable": False},
            {"coordinate": "t0_r0_c2", "cell_id": "t0_r0_c2", "value": str(opening_bal), "type": "given", "editable": False},
            {"coordinate": "t0_r0_c3", "cell_id": "t0_r0_c3", "value": "May 31", "type": "given", "editable": False},
            {"coordinate": "t0_r0_c4", "cell_id": "t0_r0_c4", "value": "Total Payments (CPJ)", "type": "given", "editable": False},
            {"coordinate": "t0_r0_c5", "cell_id": "t0_r0_c5", "value": str(cpj_total), "type": "given", "editable": False},
        ],
        [
            {"coordinate": "t0_r1_c0", "cell_id": "t0_r1_c0", "value": "May 31", "type": "given", "editable": False},
            {"coordinate": "t0_r1_c1", "cell_id": "t0_r1_c1", "value": "Total Receipts (CRJ)", "type": "given", "editable": False},
            {"coordinate": "t0_r1_c2", "cell_id": "t0_r1_c2", "value": str(crj_total), "type": "given", "editable": False},
            {"coordinate": "t0_r1_c3", "cell_id": "t0_r1_c3", "value": "", "type": "required", "editable": True},
            {"coordinate": "t0_r1_c4", "cell_id": "t0_r1_c4", "value": "", "type": "required", "editable": True},
            {"coordinate": "t0_r1_c5", "cell_id": "t0_r1_c5", "value": "", "type": "required", "editable": True},
        ],
        [
            {"coordinate": "t0_r2_c0", "cell_id": "t0_r2_c0", "value": "", "type": "must_be_empty", "editable": False},
            {"coordinate": "t0_r2_c1", "cell_id": "t0_r2_c1", "value": "Total", "type": "given", "editable": False},
            {"coordinate": "t0_r2_c2", "cell_id": "t0_r2_c2", "value": "", "type": "required", "editable": True},
            {"coordinate": "t0_r2_c3", "cell_id": "t0_r2_c3", "value": "", "type": "must_be_empty", "editable": False},
            {"coordinate": "t0_r2_c4", "cell_id": "t0_r2_c4", "value": "Total", "type": "given", "editable": False},
            {"coordinate": "t0_r2_c5", "cell_id": "t0_r2_c5", "value": "", "type": "required", "editable": True},
        ],
        [
            {"coordinate": "t0_r3_c0", "cell_id": "t0_r3_c0", "value": "", "type": "required", "editable": True},
            {"coordinate": "t0_r3_c1", "cell_id": "t0_r3_c1", "value": "", "type": "required", "editable": True},
            {"coordinate": "t0_r3_c2", "cell_id": "t0_r3_c2", "value": "", "type": "required", "editable": True},
            {"coordinate": "t0_r3_c3", "cell_id": "t0_r3_c3", "value": "", "type": "must_be_empty", "editable": False},
            {"coordinate": "t0_r3_c4", "cell_id": "t0_r3_c4", "value": "", "type": "must_be_empty", "editable": False},
            {"coordinate": "t0_r3_c5", "cell_id": "t0_r3_c5", "value": "", "type": "must_be_empty", "editable": False},
        ],
    ]
    correct_map = {
        "t0_r1_c3": "May 31",
        "t0_r1_c4": "Balance c/d",
        "t0_r1_c5": str(closing_bal),
        "t0_r2_c2": str(total_debit),
        "t0_r2_c5": str(total_debit),
        "t0_r3_c0": "Jun 1",
        "t0_r3_c1": "Balance b/d",
        "t0_r3_c2": str(closing_bal),
    }
    cell_hints = {
        "t0_r1_c3": "Enter the month-end date ('May 31') for Balance c/d.",
        "t0_r1_c4": "Enter 'Balance c/d' on the smaller (Credit) side.",
        "t0_r1_c5": f"Subtract CPJ ({cpj_total}) from Debit total ({total_debit}) -> {closing_bal}.",
        "t0_r2_c2": f"Larger side total ({opening_bal} + {crj_total} = {total_debit}) goes on both totals.",
        "t0_r2_c5": f"Must match the Debit total ({total_debit}).",
        "t0_r3_c0": "Opening date for next month is 'Jun 1'.",
        "t0_r3_c1": "Bring down the opening balance as 'Balance b/d'.",
        "t0_r3_c2": f"Opening Debit balance brought down equals {closing_bal}.",
    }
    worked = (
        f"**Completed Bank T-Account Memorandum** [8 marks]:\n\n"
        f"| Day | Details (Dr) | Amount (R) | Day | Details (Cr) | Amount (R) |\n"
        f"| --- | --- | --- | --- | --- | --- |\n"
        f"| May 1 | Balance b/d | {opening_bal} | May 31 | Total Payments (CPJ) | {cpj_total} |\n"
        f"| May 31 | Total Receipts (CRJ) | {crj_total} | **May 31** | **Balance c/d** | **{closing_bal}** |\n"
        f"| | Total | **{total_debit}** | | Total | **{total_debit}** |\n"
        f"| **Jun 1** | **Balance b/d** | **{closing_bal}** | | | |"
    )
    sample = f"Balance c/d May 31: {closing_bal}; Totals: {total_debit}; Balance b/d Jun 1: {closing_bal}"
    return _build_table(
        rng,
        qid_prefix="g8_gl_29",
        subskill="29_balancing_bank_t_account_debit_balance",
        title="Balancing the Bank T-Account",
        prompt=(
            f"Balance the **Bank** General Ledger T-account for **{sc['entrepreneur']}'s {sc['business_type']}** at 31 May "
            f"(Opening Debit balance: {_fmt_r(opening_bal)}, CRJ Receipts: {_fmt_r(crj_total)}, CPJ Payments: {_fmt_r(cpj_total)}). "
            f"Enter `Balance c/d` (`May 31`) on the smaller side, complete both `Total` cells, and bring down `Balance b/d` on `Jun 1`."
        ),
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=sample,
        marks=8,
        hints={
            "tier_1": "Compare total debits vs total credits; insert Balance c/d on the smaller side.",
            "tier_2": f"Debit total = {total_debit}. Balance c/d = {total_debit} - {cpj_total} = {closing_bal}.",
            "tier_3": sample,
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Correct Balance c/d ({closing_bal}) on Credit side", "marks": 3, "editable": True},
            {"id": "mp_2", "desc": f"Equal column totals ({total_debit})", "marks": 2, "editable": True},
            {"id": "mp_3", "desc": f"Balance b/d ({closing_bal}) on Jun 1 Debit side", "marks": 3, "editable": True},
        ],
        misconception_tags=["inverted_cd_bd_sides", "subtraction_error_in_balancing"],
    )


def arch_30_balancing_capital_or_income_credit_t_account(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    open_cap = rng.randint(25, 65) * 1000
    add_cap = rng.randint(5, 20) * 1000
    total_cap = open_cap + add_cap

    headers = ["Day", "Details (Debit)", "Amount (R)", "Day", "Details (Credit)", "Amount (R)"]
    rows = [
        [
            {"coordinate": "t0_r0_c0", "cell_id": "t0_r0_c0", "value": "", "type": "required", "editable": True},
            {"coordinate": "t0_r0_c1", "cell_id": "t0_r0_c1", "value": "", "type": "required", "editable": True},
            {"coordinate": "t0_r0_c2", "cell_id": "t0_r0_c2", "value": "", "type": "required", "editable": True},
            {"coordinate": "t0_r0_c3", "cell_id": "t0_r0_c3", "value": "Jul 1", "type": "given", "editable": False},
            {"coordinate": "t0_r0_c4", "cell_id": "t0_r0_c4", "value": "Balance b/d", "type": "given", "editable": False},
            {"coordinate": "t0_r0_c5", "cell_id": "t0_r0_c5", "value": str(open_cap), "type": "given", "editable": False},
        ],
        [
            {"coordinate": "t0_r1_c0", "cell_id": "t0_r1_c0", "value": "", "type": "must_be_empty", "editable": False},
            {"coordinate": "t0_r1_c1", "cell_id": "t0_r1_c1", "value": "", "type": "must_be_empty", "editable": False},
            {"coordinate": "t0_r1_c2", "cell_id": "t0_r1_c2", "value": "", "type": "must_be_empty", "editable": False},
            {"coordinate": "t0_r1_c3", "cell_id": "t0_r1_c3", "value": "Jul 14", "type": "given", "editable": False},
            {"coordinate": "t0_r1_c4", "cell_id": "t0_r1_c4", "value": "Bank (CRJ)", "type": "given", "editable": False},
            {"coordinate": "t0_r1_c5", "cell_id": "t0_r1_c5", "value": str(add_cap), "type": "given", "editable": False},
        ],
        [
            {"coordinate": "t0_r2_c0", "cell_id": "t0_r2_c0", "value": "", "type": "must_be_empty", "editable": False},
            {"coordinate": "t0_r2_c1", "cell_id": "t0_r2_c1", "value": "Total", "type": "given", "editable": False},
            {"coordinate": "t0_r2_c2", "cell_id": "t0_r2_c2", "value": "", "type": "required", "editable": True},
            {"coordinate": "t0_r2_c3", "cell_id": "t0_r2_c3", "value": "", "type": "must_be_empty", "editable": False},
            {"coordinate": "t0_r2_c4", "cell_id": "t0_r2_c4", "value": "Total", "type": "given", "editable": False},
            {"coordinate": "t0_r2_c5", "cell_id": "t0_r2_c5", "value": "", "type": "required", "editable": True},
        ],
        [
            {"coordinate": "t0_r3_c0", "cell_id": "t0_r3_c0", "value": "", "type": "must_be_empty", "editable": False},
            {"coordinate": "t0_r3_c1", "cell_id": "t0_r3_c1", "value": "", "type": "must_be_empty", "editable": False},
            {"coordinate": "t0_r3_c2", "cell_id": "t0_r3_c2", "value": "", "type": "must_be_empty", "editable": False},
            {"coordinate": "t0_r3_c3", "cell_id": "t0_r3_c3", "value": "", "type": "required", "editable": True},
            {"coordinate": "t0_r3_c4", "cell_id": "t0_r3_c4", "value": "", "type": "required", "editable": True},
            {"coordinate": "t0_r3_c5", "cell_id": "t0_r3_c5", "value": "", "type": "required", "editable": True},
        ],
    ]
    correct_map = {
        "t0_r0_c0": "Jul 31",
        "t0_r0_c1": "Balance c/d",
        "t0_r0_c2": str(total_cap),
        "t0_r2_c2": str(total_cap),
        "t0_r2_c5": str(total_cap),
        "t0_r3_c3": "Aug 1",
        "t0_r3_c4": "Balance b/d",
        "t0_r3_c5": str(total_cap),
    }
    cell_hints = {
        "t0_r0_c0": "Balance c/d is dated at month-end ('Jul 31').",
        "t0_r0_c1": "With zero Debits, enter 'Balance c/d' on the Debit side.",
        "t0_r0_c2": f"Closing balance equals {open_cap} + {add_cap} = {total_cap}.",
        "t0_r2_c2": f"Write total {total_cap} on both sides.",
        "t0_r2_c5": f"Sum of Credits = {total_cap}.",
        "t0_r3_c3": "Opening date for next month is 'Aug 1'.",
        "t0_r3_c4": "Enter 'Balance b/d' on the Credit side.",
        "t0_r3_c5": f"Credit opening balance = {total_cap}.",
    }
    worked = (
        f"**Completed Capital T-Account Memorandum** [8 marks]:\n\n"
        f"| Day | Details (Dr) | Amount (R) | Day | Details (Cr) | Amount (R) |\n"
        f"| --- | --- | --- | --- | --- | --- |\n"
        f"| **Jul 31** | **Balance c/d** | **{total_cap}** | Jul 1 | Balance b/d | {open_cap} |\n"
        f"| | | | Jul 14 | Bank (CRJ) | {add_cap} |\n"
        f"| | Total | **{total_cap}** | | Total | **{total_cap}** |\n"
        f"| | | | **Aug 1** | **Balance b/d** | **{total_cap}** |"
    )
    sample = f"Debit Balance c/d Jul 31: {total_cap}; Totals: {total_cap}; Credit Balance b/d Aug 1: {total_cap}"
    return _build_table(
        rng,
        qid_prefix="g8_gl_30",
        subskill="30_balancing_capital_or_income_credit_t_account",
        title="Balancing a Credit-Balance T-Account (Capital)",
        prompt=(
            f"Balance the **Capital** account of **{sc['entrepreneur']}'s {sc['business_type']}** on 31 July "
            f"(Opening Credit balance Jul 1: {_fmt_r(open_cap)}; additional Capital contribution Jul 14: {_fmt_r(add_cap)}). "
            f"Insert `Balance c/d` (`Jul 31`), equal `Total` rows, and bring down `Balance b/d` (`Aug 1`) on the Credit side."
        ),
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=sample,
        marks=8,
        hints={
            "tier_1": "Credit side is larger, so Balance c/d goes on the Debit side and Balance b/d drops to Credit.",
            "tier_2": f"Total Capital = {open_cap} + {add_cap} = {total_cap}.",
            "tier_3": sample,
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Debit Balance c/d ({total_cap})", "marks": 3, "editable": True},
            {"id": "mp_2", "desc": f"Matching totals ({total_cap})", "marks": 2, "editable": True},
            {"id": "mp_3", "desc": f"Credit Balance b/d Aug 1 ({total_cap})", "marks": 3, "editable": True},
        ],
        misconception_tags=["inverted_cd_bd_sides"],
    )


def arch_31_identifying_balance_cd_and_bd_sides(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    amt = rng.randint(5, 25) * 1000
    pair = rng.choice([
        ("Equipment", "Debit", "Credit", "Debit"),
        ("Loan", "Credit", "Debit", "Credit"),
        ("Bank (positive cash)", "Debit", "Credit", "Debit"),
    ])
    acc, normal, cd_side, bd_side = pair
    prompt = (
        f"When balancing the **{acc}** T-account of **{sc['entrepreneur']}'s {sc['business_type']}** with a closing value of **{_fmt_r(amt)}**, "
        f"on which sides must `Balance c/d` (carried down) and `Balance b/d` (brought down) be entered?"
    )
    correct = f"Balance c/d is entered on the {cd_side} (smaller) side above the totals, and Balance b/d is brought down on the {bd_side} (opposite/true) side below the totals."
    distractors = [
        f"Both Balance c/d and Balance b/d are written together on the {normal} side above the total line.",
        f"Balance c/d is entered on the {bd_side} side above the totals, and Balance b/d on the {cd_side} side below.",
        "Only Balance c/d is needed; Balance b/d is omitted so the Trial Balance remains blank.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g8_gl_31",
        subskill="31_identifying_balance_cd_and_bd_sides",
        title="Balance c/d vs Balance b/d Placement",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=f"`Balance c/d` closes the month by making the smaller side (`{cd_side}`) equal the larger side (`{normal}`). Then `Balance b/d` re-opens the next month on the **true** normal side (`{bd_side}`).",
        hints={
            "tier_1": "'c/d' fills the shortfall on the smaller side; 'b/d' lands on the opposite true side.",
            "tier_2": f"Since {acc} normally has a {normal} balance, b/d belongs on {bd_side}.",
            "tier_3": correct,
        },
        misconception_tags=["inverted_cd_bd_sides"],
    )


def arch_32_carrying_over_non_current_asset_balances(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    cost = rng.randint(120, 290) * 1000
    extra = rng.randint(15, 45) * 1000
    prompt = (
        f"**{sc['entrepreneur']}'s {sc['business_type']}** bought a delivery vehicle for **{_fmt_r(cost)}** in Month 1 and additional equipment for **{_fmt_r(extra)}** in Month 2.\n\n"
        f"Why does the **Vehicles** account balance of {_fmt_r(cost)} carry forward from Month 1 into Month 2, Month 3, and beyond rather than resetting to R0 each month?"
    )
    correct = "Because Vehicles is a permanent Balance Sheet Asset account; its value remains in the business until sold or disposed of, so its closing Balance c/d becomes next month's opening Balance b/d."
    distractors = [
        "Because Vehicles is a Nominal Expense that must be subtracted from monthly wages until depleted.",
        "Because only Cash Receipts Journal income resets to zero while vehicles double every month.",
        "Because the Receiver of Revenue requires vehicles to be re-purchased in every new trial balance.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g8_gl_32",
        subskill="32_carrying_over_non_current_asset_balances",
        title="Permanent Asset Balance Carry-Over",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=f"Balance Sheet section accounts (like **Vehicles** worth {_fmt_r(cost)}) are **permanent** accounts: their balances carry forward month-to-month via `Balance c/d` -> `Balance b/d` throughout the asset's life.",
        hints={
            "tier_1": "Think of the difference between permanent Balance Sheet assets and temporary Nominal accounts.",
            "tier_2": "A vehicle owned in Month 1 is still owned in Month 2.",
            "tier_3": correct,
        },
        misconception_tags=["resetting_asset_balances_monthly"],
    )


def arch_33_multi_month_closing_to_opening_balance_calc(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    open_aug = rng.randint(10, 30) * 1000
    crj_aug = rng.randint(12, 28) * 500
    cpj_aug = rng.randint(8, 22) * 500
    crj_sep = rng.randint(14, 30) * 500
    cpj_sep = rng.randint(9, 24) * 500
    bal_sep1 = open_aug + crj_aug - cpj_aug
    bal_oct1 = bal_sep1 + crj_sep - cpj_sep
    prompt = (
        f"**{sc['entrepreneur']}'s {sc['business_type']}** had a Bank opening balance of **{_fmt_r(open_aug)}** on 1 August.\n"
        f"- August: CRJ Receipts = **{_fmt_r(crj_aug)}**, CPJ Payments = **{_fmt_r(cpj_aug)}**\n"
        f"- September: CRJ Receipts = **{_fmt_r(crj_sep)}**, CPJ Payments = **{_fmt_r(cpj_sep)}**\n\n"
        f"Calculate the opening **Balance b/d** of Bank on **1 October** (in Rand)."
    )
    ans = _fmt_r(bal_oct1)
    sol = (
        f"**{ans}** [4 marks]\n\n"
        f"**Working:**\n"
        f"1. **Balance on 1 September:** ${open_aug} + {crj_aug} - {cpj_aug} = {bal_sep1}$ [2 marks]\n"
        f"2. **Balance on 1 October:** ${bal_sep1} + {crj_sep} - {cpj_sep} = {bal_oct1}$ (**{ans}**) [2 marks]"
    )
    return _build_short(
        rng,
        qid_prefix="g8_gl_33",
        subskill="33_multi_month_closing_to_opening_balance_calc",
        title="Multi-Month Bank Balance Progression",
        prompt=prompt,
        expected_answer=ans,
        worked_solution=sol,
        marks=4,
        hints={
            "tier_1": "First calculate September 1 Balance b/d from August figures.",
            "tier_2": f"Sep 1 Balance = {bal_sep1}. Now add Sep CRJ ({crj_sep}) and subtract Sep CPJ ({cpj_sep}).",
            "tier_3": f"Oct 1 Balance b/d = {ans}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Sep 1 closing/opening balance: {_fmt_r(bal_sep1)}", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": f"Oct 1 opening balance: {ans}", "marks": 2, "editable": True},
        ],
        misconception_tags=["omitting_previous_month_balance"],
    )


def arch_34_calculating_missing_cpj_or_crj_from_ledger(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    open_bal = rng.randint(10, 28) * 1000
    crj = rng.randint(12, 34) * 1000
    cpj = rng.randint(8, 25) * 1000
    close_bal = open_bal + crj - cpj
    find_cpj = rng.choice([True, False])

    if find_cpj:
        svg = _t_account_svg("Bank (B4)", [("Jul 1", "Balance b/d", str(open_bal)), ("Jul 31", "Total Receipts (CRJ)", str(crj))], [("Jul 31", "Total Payments (CPJ)", "?"), ("Jul 31", "Balance c/d", str(close_bal))])
        prompt = (
            f"Inspect the incomplete **Bank** T-account diagram for **{sc['entrepreneur']}'s {sc['business_type']}**.\n"
            f"Opening Debit balance: {_fmt_r(open_bal)}; CRJ Receipts: {_fmt_r(crj)}; Closing Balance c/d: {_fmt_r(close_bal)}.\n\n"
            f"Calculate the missing **Total Payments (CPJ)** figure (`?`)."
        )
        ans = _fmt_r(cpj)
        sol = (
            f"**{ans}** [3 marks]\n\n"
            f"**Working:**\n"
            f"Debit Total = ${open_bal} + {crj} = {open_bal + crj}$\n"
            f"$\\text{{CPJ Payments}} = \\text{{Debit Total}} - \\text{{Balance c/d}} = {open_bal + crj} - {close_bal} = {cpj}$ (**{ans}**)"
        )
    else:
        svg = _t_account_svg("Bank (B4)", [("Jul 1", "Balance b/d", str(open_bal)), ("Jul 31", "Total Receipts (CRJ)", "?")], [("Jul 31", "Total Payments (CPJ)", str(cpj)), ("Jul 31", "Balance c/d", str(close_bal))])
        prompt = (
            f"Inspect the incomplete **Bank** T-account diagram for **{sc['entrepreneur']}'s {sc['business_type']}**.\n"
            f"Opening Debit balance: {_fmt_r(open_bal)}; CPJ Payments: {_fmt_r(cpj)}; Closing Balance c/d: {_fmt_r(close_bal)}.\n\n"
            f"Calculate the missing **Total Receipts (CRJ)** figure (`?`)."
        )
        ans = _fmt_r(crj)
        sol = (
            f"**{ans}** [3 marks]\n\n"
            f"**Working:**\n"
            f"Credit Total = ${cpj} + {close_bal} = {cpj + close_bal}$\n"
            f"$\\text{{CRJ Receipts}} = \\text{{Credit Total}} - \\text{{Opening b/d}} = {cpj + close_bal} - {open_bal} = {crj}$ (**{ans}**)"
        )

    return _build_short(
        rng,
        qid_prefix="g8_gl_34",
        subskill="34_calculating_missing_cpj_or_crj_from_ledger",
        title="Solving Missing Journal Total in T-Account",
        prompt=prompt,
        expected_answer=ans,
        worked_solution=sol,
        marks=3,
        hints={
            "tier_1": "In a balanced T-account, the Debit side total must equal the Credit side total.",
            "tier_2": "Find the complete side's sum first, then subtract the known item on the incomplete side.",
            "tier_3": f"Missing journal figure = {ans}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": "Finds full side total", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": f"Solves missing entry: {ans}", "marks": 2, "editable": True},
        ],
        misconception_tags=["subtraction_error_in_balancing"],
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    )


def arch_35_totaling_nominal_income_and_expense_accounts(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    m1 = rng.randint(4, 15) * 300
    m2 = rng.randint(5, 16) * 300
    m3 = rng.randint(3, 12) * 300
    tot = m1 + m2 + m3
    acc = rng.choice([("Current Income", "Credit"), ("Wages", "Debit"), ("Material Cost", "Debit"), ("Rent Income", "Credit")])
    prompt = (
        f"In the Nominal Accounts Section of **{sc['entrepreneur']}'s {sc['business_type']}**, the **{acc[0]}** T-account contains "
        f"three entries all on the **{acc[1]}** side: **{_fmt_r(m1)}** (June), **{_fmt_r(m2)}** (July), and **{_fmt_r(m3)}** (August), with zero entries on the opposite side.\n\n"
        f"What is the cumulative total balance of **{acc[0]}** transferred to the Trial Balance ({acc[1]} column) at 31 August?"
    )
    ans = _fmt_r(tot)
    sol = (
        f"**{ans}** ({acc[1]} balance) [2 marks]\n\n"
        f"**Working:**\n"
        f"Nominal accounts accumulate entries on one side and are simply summed for the Trial Balance:\n"
        f"$${m1} + {m2} + {m3} = {tot}\\text{{ ({ans}, {acc[1]})}}$$"
    )
    return _build_short(
        rng,
        qid_prefix="g8_gl_35",
        subskill="35_totaling_nominal_income_and_expense_accounts",
        title="Totalling Multi-Month Nominal Accounts",
        prompt=prompt,
        expected_answer=ans,
        worked_solution=sol,
        marks=2,
        hints={
            "tier_1": "Add all three amounts recorded on the same side of the account.",
            "tier_2": f"{m1} + {m2} + {m3}",
            "tier_3": ans,
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Correct cumulative total {ans}", "marks": 2, "editable": True},
        ],
        misconception_tags=["nominal_total_arithmetic_error"],
    )


def arch_36_calculating_net_profit_from_nominal_accounts(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    cur_inc = rng.randint(30, 80) * 1000
    rent_inc = rng.randint(4, 15) * 1000
    wages = rng.randint(12, 26) * 1000
    water = rng.randint(2, 6) * 500
    cons = rng.randint(3, 9) * 500
    tot_inc = cur_inc + rent_inc
    tot_exp = wages + water + cons
    profit = tot_inc - tot_exp
    prompt = (
        f"Extract the Nominal Section balances of **{sc['entrepreneur']}'s {sc['business_type']}** to determine financial performance:\n"
        f"- Current Income: {_fmt_r(cur_inc)}\n"
        f"- Rent Income: {_fmt_r(rent_inc)}\n"
        f"- Wages: {_fmt_r(wages)}\n"
        f"- Water and Electricity: {_fmt_r(water)}\n"
        f"- Consumable goods: {_fmt_r(cons)}\n\n"
        f"Calculate the **Net Profit** using $\\text{{Profit}} = \\text{{Total Income}} - \\text{{Total Expenses}}$."
    )
    ans = _fmt_r(profit)
    sol = (
        f"**{ans}** [4 marks]\n\n"
        f"**Working:**\n"
        f"1. **Total Income** = ${cur_inc} + {rent_inc} = {tot_inc}$ [1 mark]\n"
        f"2. **Total Expenses** = ${wages} + {water} + {cons} = {tot_exp}$ [1 mark]\n"
        f"3. **Net Profit** = ${tot_inc} - {tot_exp} = {profit}$ (**{ans}**) [2 marks]"
    )
    return _build_short(
        rng,
        qid_prefix="g8_gl_36",
        subskill="36_calculating_net_profit_from_nominal_accounts",
        title="Net Profit from Nominal Accounts",
        prompt=prompt,
        expected_answer=ans,
        worked_solution=sol,
        marks=4,
        hints={
            "tier_1": "Group all Income accounts together and all Expense accounts together.",
            "tier_2": f"Total Income = {tot_inc}; Total Expenses = {tot_exp}.",
            "tier_3": f"Net Profit = {ans}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Total Income = {_fmt_r(tot_inc)}", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": f"Total Expenses = {_fmt_r(tot_exp)}", "marks": 1, "editable": True},
            {"id": "mp_3", "desc": f"Net Profit = {ans}", "marks": 2, "editable": True},
        ],
        misconception_tags=["including_capital_or_bank_in_profit"],
    )


def arch_37_trial_balance_purpose_mathematical_check(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    tot = rng.randint(80, 240) * 1000
    prompt = (
        f"After completing all month-end General Ledger postings for **{sc['entrepreneur']}'s {sc['business_type']}**, "
        f"both columns of the **Trial Balance** add up to **{_fmt_r(tot)}**.\n\n"
        f"What is the exact purpose of preparing a **Trial Balance**, and what does this equal total confirm?"
    )
    correct = "To test the mathematical accuracy of double-entry postings in the General Ledger by verifying that Total Debits equal Total Credits before preparing final financial statements."
    distractors = [
        "To serve as an official bank statement issued by a commercial bank to replace source documents.",
        "To prove with certainty that zero transactions were omitted or misnamed between two expense accounts.",
        "To calculate VAT refunds payable by customers on every cash till slip.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g8_gl_37",
        subskill="37_trial_balance_purpose_mathematical_check",
        title="Purpose of the Trial Balance",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation="The Trial Balance acts as a mathematical quality-control bridge between the General Ledger and Financial Statements, confirming $\\text{Total Debits} = \\text{Total Credits}$ (both " + _fmt_r(tot) + ").",
        hints={
            "tier_1": "Does the Trial Balance record new transactions or check ledger arithmetic?",
            "tier_2": "It verifies Total Debits = Total Credits before drawing up the Income Statement and Balance Sheet.",
            "tier_3": correct,
        },
        misconception_tags=["trial_balance_guarantees_zero_errors"],
    )


def arch_38_trial_balance_standard_account_ordering(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    prompt = (
        f"While assembling the Trial Balance for **{sc['entrepreneur']}'s {sc['business_type']}** from the accounts "
        f"`Wages`, `Capital`, `Bank`, `Current Income`, `Vehicles`, and `Drawings`, which listing order follows standard South African Trial Balance presentation?"
    )
    correct = "1. Balance Sheet Section (Owner's Equity: Capital, Drawings -> Non-Current Assets: Vehicles -> Current Assets: Bank), then 2. Nominal Section (Current Income, Wages)."
    distractors = [
        "1. Nominal Section (Wages, Current Income) alphabetically, then 2. Balance Sheet Section.",
        "1. All Debit balances mixed together regardless of section, then all Credit balances below.",
        "1. Current Assets first, followed by Expenses, followed by Owner's Equity at the bottom.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g8_gl_38",
        subskill="38_trial_balance_standard_account_ordering",
        title="Standard Order of Accounts in Trial Balance",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation="In the Grade 8 General Ledger & Trial Balance, **Balance Sheet Section** accounts (Owner's Equity, Non-Current Assets, Current Assets, Liabilities) are listed first, followed by **Nominal Section** accounts (Incomes and Expenses).",
        hints={
            "tier_1": "Which main section comes at the top of the Trial Balance: Balance Sheet or Nominal?",
            "tier_2": "Balance Sheet Section (B: Capital, Drawings, Fixed Assets, Bank) always precedes Nominal Section (N: Income, Expenses).",
            "tier_3": correct,
        },
        misconception_tags=["trial_balance_ordering_error"],
    )


def arch_39_trial_balance_debit_vs_credit_column_sorting(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    pool = [
        ("Capital", str(rng.randint(50, 90) * 1000), "Credit"),
        ("Drawings", str(rng.randint(3, 9) * 1000), "Debit"),
        ("Equipment", str(rng.randint(15, 35) * 1000), "Debit"),
        ("Bank", str(rng.randint(10, 25) * 1000), "Debit"),
        ("Current Income", str(rng.randint(25, 65) * 1000), "Credit"),
        ("Rent Income", str(rng.randint(4, 12) * 1000), "Credit"),
        ("Wages", str(rng.randint(8, 20) * 1000), "Debit"),
        ("Telephone", str(rng.randint(2, 6) * 500), "Debit"),
    ]
    selected = rng.sample(pool, 5)
    headers = ["Account Name", "Balance (R)", "Trial Balance Column (Debit / Credit)"]
    rows = []
    correct_map: Dict[str, str] = {}
    cell_hints: Dict[str, str] = {}
    md_lines = ["| Account Name | Balance (R) | Trial Balance Column |", "| --- | --- | --- |"]

    for i, (acc, amt, col) in enumerate(selected):
        correct_map[f"t0_r{i}_c2"] = col
        cell_hints[f"t0_r{i}_c2"] = f"Use DEAD (Debit: Drawings, Expenses, Assets) or CLIC (Credit: Capital, Liabilities, Income) for {acc}."
        rows.append([
            {"coordinate": f"t0_r{i}_c0", "cell_id": f"t0_r{i}_c0", "value": acc, "type": "given", "editable": False},
            {"coordinate": f"t0_r{i}_c1", "cell_id": f"t0_r{i}_c1", "value": amt, "type": "given", "editable": False},
            {"coordinate": f"t0_r{i}_c2", "cell_id": f"t0_r{i}_c2", "value": "", "type": "required", "editable": True},
        ])
        md_lines.append(f"| {acc} | {amt} | **{col}** |")

    worked = "**Trial Balance Column Allocation** [5 marks]:\n\n" + "\n".join(md_lines)
    sample = "; ".join(f"{a}: {c}" for a, _, c in selected)
    return _build_table(
        rng,
        qid_prefix="g8_gl_39",
        subskill="39_trial_balance_debit_vs_credit_column_sorting",
        title="Sorting Account Balances into Debit/Credit Columns",
        prompt=f"For each General Ledger balance extracted from **{sc['entrepreneur']}'s {sc['business_type']}**, specify whether it belongs in the `Debit` or `Credit` column of the Trial Balance.",
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=sample,
        marks=5,
        hints={
            "tier_1": "DEAD = Debit balances; CLIC = Credit balances.",
            "tier_2": "Assets, Drawings, Expenses -> Debit; Capital, Liabilities, Income -> Credit.",
            "tier_3": sample,
        },
        marking_points=[{"id": f"mp_{i}", "desc": f"{selected[i][0]} -> {selected[i][2]}", "marks": 1, "editable": True} for i in range(5)],
        misconception_tags=["trial_balance_debit_credit_inversion"],
    )


def arch_40_full_trial_balance_preparation_table(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    capital = rng.randint(50, 90) * 1000
    cur_inc = rng.randint(30, 65) * 1000
    rent_inc = rng.randint(6, 14) * 1000
    drawings = rng.randint(3, 8) * 1000
    equip = rng.randint(15, 32) * 1000
    wages = rng.randint(10, 22) * 1000
    stat = rng.randint(2, 6) * 500
    total_bal = capital + cur_inc + rent_inc
    bank_bal = total_bal - (drawings + equip + wages + stat)

    accounts = [
        ("B1", "Capital", "", str(capital)),
        ("B2", "Drawings", str(drawings), ""),
        ("B3", "Equipment", str(equip), ""),
        ("B4", "Bank", str(bank_bal), ""),
        ("N1", "Current Income", "", str(cur_inc)),
        ("N2", "Rent Income", "", str(rent_inc)),
        ("N3", "Wages", str(wages), ""),
        ("N4", "Stationery", str(stat), ""),
    ]
    headers = ["Fol", "Account", "Debit (R)", "Credit (R)"]
    rows = []
    correct_map: Dict[str, str] = {}
    cell_hints: Dict[str, str] = {}
    md_lines = ["| Fol | Account | Debit (R) | Credit (R) |", "| --- | --- | --- | --- |"]

    for r_idx, (fol, acc, deb, cred) in enumerate(accounts):
        correct_map[f"t0_r{r_idx}_c2"] = deb
        correct_map[f"t0_r{r_idx}_c3"] = cred
        cell_hints[f"t0_r{r_idx}_c2"] = f"Enter {acc} balance here if it is a DEAD account, else leave blank."
        cell_hints[f"t0_r{r_idx}_c3"] = f"Enter {acc} balance here if it is a CLIC account, else leave blank."
        rows.append([
            {"coordinate": f"t0_r{r_idx}_c0", "cell_id": f"t0_r{r_idx}_c0", "value": fol, "type": "given", "editable": False},
            {"coordinate": f"t0_r{r_idx}_c1", "cell_id": f"t0_r{r_idx}_c1", "value": acc, "type": "given", "editable": False},
            {"coordinate": f"t0_r{r_idx}_c2", "cell_id": f"t0_r{r_idx}_c2", "value": "", "type": "required" if deb else "must_be_empty", "editable": True},
            {"coordinate": f"t0_r{r_idx}_c3", "cell_id": f"t0_r{r_idx}_c3", "value": "", "type": "required" if cred else "must_be_empty", "editable": True},
        ])
        md_lines.append(f"| {fol} | {acc} | **{deb or '-'}** | **{cred or '-'}** |")

    tot_r = len(accounts)
    correct_map[f"t0_r{tot_r}_c2"] = str(total_bal)
    correct_map[f"t0_r{tot_r}_c3"] = str(total_bal)
    cell_hints[f"t0_r{tot_r}_c2"] = f"Sum all Debit column balances = {total_bal}."
    cell_hints[f"t0_r{tot_r}_c3"] = f"Sum all Credit column balances = {total_bal}."
    rows.append([
        {"coordinate": f"t0_r{tot_r}_c0", "cell_id": f"t0_r{tot_r}_c0", "value": "", "type": "must_be_empty", "editable": False},
        {"coordinate": f"t0_r{tot_r}_c1", "cell_id": f"t0_r{tot_r}_c1", "value": "Total", "type": "given", "editable": False},
        {"coordinate": f"t0_r{tot_r}_c2", "cell_id": f"t0_r{tot_r}_c2", "value": "", "type": "required", "editable": True},
        {"coordinate": f"t0_r{tot_r}_c3", "cell_id": f"t0_r{tot_r}_c3", "value": "", "type": "required", "editable": True},
    ])
    md_lines.append(f"| | Total | **{total_bal}** | **{total_bal}** |")

    bal_summary = ", ".join(f"{a}: R{d or c}" for _, a, d, c in accounts)
    prompt = (
        f"Prepare the complete **Trial Balance** of **{sc['entrepreneur']}'s {sc['business_type']}** on 31 August using these ledger balances: "
        f"{bal_summary}.\n\n"
        f"Place each figure in its correct `Debit (R)` or `Credit (R)` column (leave the unused cell blank) and compute both column totals."
    )
    worked = "**Completed Trial Balance Memorandum** [10 marks]:\n\n" + "\n".join(md_lines)
    sample = f"Total Debits = Total Credits = {_fmt_r(total_bal)}"
    return _build_table(
        rng,
        qid_prefix="g8_gl_40",
        subskill="40_full_trial_balance_preparation_table",
        title="Preparing Full Service Business Trial Balance",
        prompt=prompt,
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=sample,
        marks=10,
        hints={
            "tier_1": "Assign DEAD accounts to Debit and CLIC accounts to Credit.",
            "tier_2": f"Both columns balance at {total_bal}.",
            "tier_3": sample,
        },
        marking_points=[
            {"id": "mp_1", "desc": "All 8 accounts in correct Dr/Cr columns", "marks": 8, "editable": True},
            {"id": "mp_2", "desc": f"Both totals equal {total_bal}", "marks": 2, "editable": True},
        ],
        misconception_tags=["trial_balance_debit_credit_inversion"],
    )


def arch_41_solving_missing_trial_balance_figure(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    capital = rng.randint(45, 95) * 1000
    cur_inc = rng.randint(25, 55) * 1000
    equip = rng.randint(15, 35) * 1000
    wages = rng.randint(8, 20) * 1000
    stat = rng.randint(2, 6) * 500
    drawings = rng.randint(3, 8) * 1000
    credit_tot = capital + cur_inc
    bank = credit_tot - (equip + wages + stat + drawings)
    prompt = (
        f"The Trial Balance of **{sc['entrepreneur']}'s {sc['business_type']}** is completely balanced, except the **Bank** balance is missing:\n"
        f"- **Credits:** Capital {_fmt_r(capital)}, Current Income {_fmt_r(cur_inc)}\n"
        f"- **Debits:** Drawings {_fmt_r(drawings)}, Equipment {_fmt_r(equip)}, Wages {_fmt_r(wages)}, Stationery {_fmt_r(stat)}, Bank = ?\n\n"
        f"Calculate the missing **Bank** balance (in Rand)."
    )
    ans = _fmt_r(bank)
    known_dr = drawings + equip + wages + stat
    sol = (
        f"**{ans}** [3 marks]\n\n"
        f"**Working:**\n"
        f"1. **Total Credits** = ${capital} + {cur_inc} = {credit_tot}$ [1 mark]\n"
        f"2. **Known Debits** = ${drawings} + {equip} + {wages} + {stat} = {known_dr}$ [1 mark]\n"
        f"3. Since $\\text{{Total Debits}} = \\text{{Total Credits}}$, $\\text{{Bank}} = {credit_tot} - {known_dr} = {bank}$ (**{ans}**) [1 mark]"
    )
    return _build_short(
        rng,
        qid_prefix="g8_gl_41",
        subskill="41_solving_missing_trial_balance_figure",
        title="Solving Missing Balance in Trial Balance",
        prompt=prompt,
        expected_answer=ans,
        worked_solution=sol,
        marks=3,
        hints={
            "tier_1": "Total Debits must equal Total Credits.",
            "tier_2": f"Total Credits = {credit_tot}; subtract the sum of known debits ({known_dr}).",
            "tier_3": f"Missing Bank balance = {ans}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Total Credits = {_fmt_r(credit_tot)}", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": f"Sum of known debits = {_fmt_r(known_dr)}", "marks": 1, "editable": True},
            {"id": "mp_3", "desc": f"Bank = {ans}", "marks": 1, "editable": True},
        ],
        misconception_tags=["trial_balance_equation_error"],
    )


def arch_42_trial_balance_imbalance_diagnostic_calculation(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    base_tot = rng.randint(90, 180) * 1000
    omitted_amt = rng.randint(3, 14) * 500
    side = rng.choice(["Credit", "Debit"])
    if side == "Credit":
        dr_tot, cr_tot = base_tot, base_tot - omitted_amt
        missing_side = "Credit"
        example_acc = rng.choice(["Rent Income", "Current Income"])
    else:
        dr_tot, cr_tot = base_tot - omitted_amt, base_tot
        missing_side = "Debit"
        example_acc = rng.choice(["Water and Electricity", "Equipment"])
    prompt = (
        f"When compiling the Trial Balance for **{sc['entrepreneur']}'s {sc['business_type']}**, "
        f"the Debit column adds up to **{_fmt_r(dr_tot)}** while the Credit column adds up to **{_fmt_r(cr_tot)}**.\n\n"
        f"What is the exact Rand difference between the columns, and which single completely omitted ledger balance could explain this shortfall?"
    )
    ans = f"{_fmt_r(omitted_amt)} omitted from the {missing_side} column (e.g., {example_acc} of {_fmt_r(omitted_amt)})"
    sol = (
        f"**{ans}** [3 marks]\n\n"
        f"**Diagnostic:**\n"
        f"Difference = ${max(dr_tot, cr_tot)} - {min(dr_tot, cr_tot)} = {omitted_amt}$ ({_fmt_r(omitted_amt)}) [1 mark].\n"
        f"Because the **{missing_side}** total is lower by {_fmt_r(omitted_amt)}, omitting a single {missing_side}-normal account like **{example_acc}** ({_fmt_r(omitted_amt)}) accounts for the imbalance [2 marks]."
    )
    return _build_short(
        rng,
        qid_prefix="g8_gl_42",
        subskill="42_trial_balance_imbalance_diagnostic_calculation",
        title="Diagnosing Trial Balance Imbalance",
        prompt=prompt,
        expected_answer=ans,
        worked_solution=sol,
        marks=3,
        qtype="short_answer",
        hints={
            "tier_1": f"Subtract the smaller column total ({min(dr_tot, cr_tot)}) from the larger ({max(dr_tot, cr_tot)}).",
            "tier_2": f"Difference is {_fmt_r(omitted_amt)} lacking on the {missing_side} side.",
            "tier_3": ans,
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Correct discrepancy {_fmt_r(omitted_amt)}", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": f"Identifies {missing_side} omission (e.g. {example_acc})", "marks": 2, "editable": True},
        ],
        misconception_tags=["trial_balance_imbalance_diagnosis_error"],
    )


def arch_43_halving_rule_reversed_posting_error_detection(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    bal = rng.randint(4, 19) * 500
    diff = bal * 2
    acc_case = rng.choice([
        ("Drawings", "Debit", "Credit", "Debit column is lower than Credit column"),
        ("Rent Income", "Credit", "Debit", "Credit column is lower than Debit column"),
        ("Wages", "Debit", "Credit", "Debit column is lower than Credit column"),
    ])
    acc, true_side, wrong_side, symptom = acc_case
    prompt = (
        f"In the Trial Balance of **{sc['entrepreneur']}'s {sc['business_type']}**, the **{symptom}** by **{_fmt_r(diff)}**.\n\n"
        f"Using the accounting **halving rule** for a balance placed in the **wrong column**, which error caused this exact **{_fmt_r(diff)}** discrepancy?"
    )
    correct = f"The {acc} balance of {_fmt_r(bal)} (normally {true_side}) was mistakenly entered in the {wrong_side} column, creating a total discrepancy of 2 × {_fmt_r(bal)} = {_fmt_r(diff)}."
    distractors = [
        f"The {acc} balance of {_fmt_r(diff)} was entered accurately on the {true_side} side twice.",
        f"A cash receipt of {_fmt_r(bal)} was omitted completely from both Bank and Current Income.",
        f"Two separate expense accounts of {_fmt_r(diff)} each were added on the Debit side.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g8_gl_43",
        subskill="43_halving_rule_reversed_posting_error_detection",
        title="Wrong-Column Error Detection (Doubled Difference)",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=f"Moving a balance $x$ from its true side to the wrong side removes $x$ from the true column and adds $x$ to the wrong column, creating a column gap of $2x$. Dividing **{_fmt_r(diff)}** by 2 identifies **{_fmt_r(bal)}** ({acc} put in {wrong_side} instead of {true_side}).",
        hints={
            "tier_1": "Entering an item on the wrong side doubles the gap between columns (2 × amount).",
            "tier_2": f"Divide the gap {_fmt_r(diff)} by 2 -> {_fmt_r(bal)}.",
            "tier_3": correct,
        },
        misconception_tags=["not_halving_wrong_side_error"],
    )


def arch_44_ledger_posting_errors_not_revealed_by_tb(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    amt = rng.randint(5, 25) * 200
    tot = rng.randint(85, 160) * 1000
    prompt = (
        f"Both columns of **{sc['entrepreneur']}'s {sc['business_type']}** Trial Balance agree at **{_fmt_r(tot)}**.\n\n"
        f"However, the bookkeeper had mistakenly posted a **{_fmt_r(amt)}** purchase of **Stationery** to the Debit side of **Wages** (instead of Stationery) while still Crediting **Bank** with {_fmt_r(amt)}. Why did the Trial Balance still balance?"
    )
    correct = "Because Total Debits still equal Total Credits (both Wages and Stationery are Debit-normal accounts); a Trial Balance only proves arithmetic equality, not correct account selection."
    distractors = [
        "Because Wages and Stationery are automatically merged into Capital at the end of every week.",
        "Because Bank was also omitted whenever Stationery was misclassified.",
        "Because Trial Balance totals automatically self-correct misnamed accounts through double-entry.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g8_gl_44",
        subskill="44_ledger_posting_errors_not_revealed_by_tb",
        title="Errors Not Revealed by a Trial Balance",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation="Errors of commission (wrong account on the correct Debit/Credit side, e.g. Dr Wages instead of Dr Stationery) and complete omission of a transaction leave **Total Debits = Total Credits** intact, so the Trial Balance cannot detect them.",
        hints={
            "tier_1": "Check whether Debits still equal Credits when one Debit account replaces another Debit account.",
            "tier_2": "A Trial Balance checks mathematical equality, not whether the right Nominal expense name was picked.",
            "tier_3": correct,
        },
        misconception_tags=["trial_balance_guarantees_zero_errors"],
    )


def arch_45_trial_balance_sections_classification_b_vs_n(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    pool = [
        ("Capital", "Balance Sheet Section", "Balance Sheet"),
        ("Land and Buildings", "Balance Sheet Section", "Balance Sheet"),
        ("Cash Float", "Balance Sheet Section", "Balance Sheet"),
        ("Current Income", "Nominal Section", "Income Statement"),
        ("Material Cost", "Nominal Section", "Income Statement"),
        ("Telephone", "Nominal Section", "Income Statement"),
        ("Drawings", "Balance Sheet Section", "Balance Sheet"),
        ("Rent Income", "Nominal Section", "Income Statement"),
    ]
    chosen = rng.sample(pool, 4)
    headers = ["Trial Balance Account", "Trial Balance Section (Balance Sheet Section / Nominal Section)", "Final Statement (Balance Sheet / Income Statement)"]
    rows = []
    correct_map: Dict[str, str] = {}
    cell_hints: Dict[str, str] = {}
    md_lines = ["| Account | Trial Balance Section | Final Statement |", "| --- | --- | --- |"]

    for i, (acc, sec, stmt) in enumerate(chosen):
        correct_map[f"t0_r{i}_c1"] = sec
        correct_map[f"t0_r{i}_c2"] = stmt
        cell_hints[f"t0_r{i}_c1"] = "Permanent assets/equity/liabilities -> 'Balance Sheet Section'; Incomes/expenses -> 'Nominal Section'."
        cell_hints[f"t0_r{i}_c2"] = "Nominal accounts compute profit on 'Income Statement'; permanent accounts go to 'Balance Sheet'."
        rows.append([
            {"coordinate": f"t0_r{i}_c0", "cell_id": f"t0_r{i}_c0", "value": acc, "type": "given", "editable": False},
            {"coordinate": f"t0_r{i}_c1", "cell_id": f"t0_r{i}_c1", "value": "", "type": "required", "editable": True},
            {"coordinate": f"t0_r{i}_c2", "cell_id": f"t0_r{i}_c2", "value": "", "type": "required", "editable": True},
        ])
        md_lines.append(f"| {acc} | **{sec}** | **{stmt}** |")

    worked = "**Trial Balance to Financial Statements Mapping** [8 marks]:\n\n" + "\n".join(md_lines)
    sample = "; ".join(f"{a}: {s} -> {f}" for a, s, f in chosen)
    return _build_table(
        rng,
        qid_prefix="g8_gl_45",
        subskill="45_trial_balance_sections_classification_b_vs_n",
        title="Trial Balance Sections to Financial Statements",
        prompt=f"Classify each account from **{sc['entrepreneur']}'s** Trial Balance into its **Trial Balance Section** and target **Final Statement**.",
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=sample,
        marks=8,
        hints={
            "tier_1": "Income and Expenses belong to the Nominal Section used for the Income Statement.",
            "tier_2": "Assets, Capital, Drawings, and Liabilities belong to the Balance Sheet Section.",
            "tier_3": sample,
        },
        marking_points=[{"id": f"mp_{i}", "desc": f"Section & Statement for {chosen[i][0]}", "marks": 2, "editable": True} for i in range(4)],
        misconception_tags=["nominal_vs_balance_sheet_confusion"],
    )


def arch_46_crj_capital_and_services_bank_total_reconciliation(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    c1 = rng.randint(15, 40) * 1000
    s1 = rng.randint(8, 24) * 500
    s2 = rng.randint(6, 18) * 500
    rent = rng.randint(2, 8) * 500
    expected_bank = c1 + s1 + s2 + rent
    prompt = (
        f"Before posting the October CRJ of **{sc['entrepreneur']}'s {sc['business_type']}** to the General Ledger Bank account, "
        f"verify the cross-cast total:\n"
        f"- **Current Income total:** {_fmt_r(s1 + s2)} (from service receipts of {_fmt_r(s1)} and {_fmt_r(s2)})\n"
        f"- **Sundry Accounts entries:** Capital {_fmt_r(c1)} and Rent Income {_fmt_r(rent)}\n\n"
        f"What exact figure must be entered as the CRJ **Bank** total and posted to the **Debit** side of Bank?"
    )
    ans = _fmt_r(expected_bank)
    sol = (
        f"**{ans}** (Debit Bank) [3 marks]\n\n"
        f"**Cross-Cast Verification:**\n"
        f"$$\\text{{Bank CRJ Total}} = \\text{{Current Income}} + \\text{{Sundry Total}} = {s1 + s2} + ({c1} + {rent}) = {expected_bank}\\text{{ ({ans})}}$$"
    )
    return _build_short(
        rng,
        qid_prefix="g8_gl_46",
        subskill="46_crj_capital_and_services_bank_total_reconciliation",
        title="CRJ Cross-Cast Reconciliation Before Posting",
        prompt=prompt,
        expected_answer=ans,
        worked_solution=sol,
        marks=3,
        hints={
            "tier_1": "In a balanced CRJ, Bank Total = Current Income Total + Sundry Accounts Total.",
            "tier_2": f"Add {s1 + s2} + {c1} + {rent}.",
            "tier_3": ans,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Applies Bank = Current Income + Sundry", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": f"Correct CRJ Bank Debit total {ans}", "marks": 2, "editable": True},
        ],
        misconception_tags=["double_counting_analysis_of_receipts"],
    )


def arch_47_cpj_expenses_and_drawings_bank_total_reconciliation(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    wages = rng.randint(8, 22) * 500
    consum = rng.randint(3, 11) * 300
    draw = rng.randint(2, 9) * 500
    equip = rng.randint(5, 18) * 500
    bank_cr = wages + consum + draw + equip
    prompt = (
        f"Before posting the November CPJ of **{sc['entrepreneur']}'s {sc['business_type']}**, verify the cross-cast total from its analysis columns:\n"
        f"- **Wages:** {_fmt_r(wages)}\n"
        f"- **Consumable goods:** {_fmt_r(consum)}\n"
        f"- **Sundry Accounts:** Drawings {_fmt_r(draw)}, Equipment {_fmt_r(equip)}\n\n"
        f"What exact amount must be posted to the **Credit** side of the **Bank** T-account as `Total Payments (CPJ)`?"
    )
    ans = _fmt_r(bank_cr)
    sol = (
        f"**{ans}** (Credit Bank) [3 marks]\n\n"
        f"**Cross-Cast Verification:**\n"
        f"$$\\text{{Bank CPJ Total}} = {wages} + {consum} + {draw} + {equip} = {bank_cr}\\text{{ ({ans})}}$$"
    )
    return _build_short(
        rng,
        qid_prefix="g8_gl_47",
        subskill="47_cpj_expenses_and_drawings_bank_total_reconciliation",
        title="CPJ Cross-Cast Reconciliation Before Posting",
        prompt=prompt,
        expected_answer=ans,
        worked_solution=sol,
        marks=3,
        hints={
            "tier_1": "Add all CPJ special analysis columns plus every Sundry payment.",
            "tier_2": f"Sum {wages} + {consum} + {draw} + {equip}.",
            "tier_3": ans,
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Correct CPJ Bank Credit total {ans}", "marks": 3, "editable": True},
        ],
        misconception_tags=["omitting_sundry_from_cpj_bank"],
    )


def arch_48_posting_folio_cross_reference_audit(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    b_num = rng.randint(1, 5)
    n_num = rng.randint(1, 5)
    case = rng.choice([
        ("Bank", f"B{b_num}", "written directly underneath the Bank column total in the CRJ and CPJ", "Sundry Fol column row"),
        ("Current Income", f"N{n_num}", "written directly underneath the Current Income column total in the CRJ", "Sundry Fol column row"),
        ("Drawings", f"B{b_num}", "entered inside the Sundry Accounts Fol column on the exact transaction row in the CPJ", "underneath the Wages total"),
        ("Rent Income", f"N{n_num}", "entered inside the Sundry Accounts Fol column on the exact transaction row in the CRJ", "underneath the Current Income total"),
    ])
    acc, fol, correct_loc, wrong_loc = case
    prompt = (
        f"An accounting clerk at **{sc['entrepreneur']}'s {sc['business_type']}** posts **{acc}** (General Ledger folio **{fol}**) from the cash journals.\n\n"
        f"Where in the journal must folio code **{fol}** be recorded to prove posting is complete?"
    )
    correct = f"It must be {correct_loc}."
    distractors = [
        f"It must be {wrong_loc}, never matching the posting source.",
        "It is written only inside the customer's till slip and omitted from both the journal and ledger.",
        "It is replaced by 'Balance b/d' in the journal Details column.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g8_gl_48",
        subskill="48_posting_folio_cross_reference_audit",
        title="Journal-to-Ledger Folio Audit",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=f"Audit rule for folio cross-referencing: special column accounts place `{fol}` **under the column total**, whereas Sundry accounts record `{fol}` in the **Sundry Fol column** on that line.",
        hints={
            "tier_1": "Check whether the account has a dedicated journal column or goes through Sundry Accounts.",
            "tier_2": "Dedicated columns -> below total; Sundry items -> in the Sundry Fol column.",
            "tier_3": correct,
        },
        misconception_tags=["folio_prefix_confusion"],
    )


def arch_49_bank_overdraft_credit_balance_recognition(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    open_dr = rng.randint(3, 9) * 1000
    crj = rng.randint(5, 14) * 1000
    extra_spend = rng.randint(2, 8) * 1000
    cpj = open_dr + crj + extra_spend
    svg = _t_account_svg("Bank (B4)", [("Aug 1", "Balance b/d", str(open_dr)), ("Aug 31", "Total Receipts (CRJ)", str(crj))], [("Aug 31", "Total Payments (CPJ)", str(cpj))])
    prompt = (
        f"Inspect the **Bank** T-account diagram for **{sc['entrepreneur']}'s {sc['business_type']}**:\n"
        f"- Debit side: Opening balance {_fmt_r(open_dr)} + CRJ receipts {_fmt_r(crj)} = {_fmt_r(open_dr + crj)}\n"
        f"- Credit side: CPJ payments = {_fmt_r(cpj)}\n\n"
        f"After balancing, what is the amount and nature of the **Balance b/d** on 1 September?"
    )
    correct = f"{_fmt_r(extra_spend)} Credit balance (Bank Overdraft — a Liability owed to the bank)."
    distractors = [
        f"{_fmt_r(extra_spend)} Debit balance (favourable cash Asset).",
        f"{_fmt_r(cpj)} Credit balance (Total Expenses paid during August).",
        f"{_fmt_r(open_dr + crj)} Debit balance (cash remaining in the till).",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g8_gl_49",
        subskill="49_bank_overdraft_credit_balance_recognition",
        title="Recognising an Overdrawn Bank Balance",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=f"Credit side ({_fmt_r(cpj)}) exceeds Debit side ({_fmt_r(open_dr + crj)}) by **{_fmt_r(extra_spend)}**. `Balance c/d` sits on the Debit side and `Balance b/d` lands on the **Credit** side, representing a **Bank Overdraft**.",
        hints={
            "tier_1": "Which side of Bank is larger: Credits (payments) or Debits (receipts)?",
            "tier_2": f"Credit exceeds Debit by {cpj} - {open_dr + crj} = {extra_spend}.",
            "tier_3": correct,
        },
        misconception_tags=["assuming_bank_always_debit_balance"],
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    )


def arch_50_end_to_end_service_business_ledger_to_profit_synthesis(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    capital = rng.randint(40, 80) * 1000
    drawings = rng.randint(2, 7) * 1000
    cur_inc = rng.randint(25, 55) * 1000
    wages = rng.randint(8, 18) * 1000
    stat = rng.randint(2, 5) * 500
    equip = rng.randint(12, 24) * 1000
    bank_bal = capital + cur_inc - drawings - wages - stat - equip
    profit = cur_inc - (wages + stat)
    final_oe = capital + profit - drawings
    prompt = (
        f"During its first month of trading in {sc['area']}, **{sc['entrepreneur']}'s {sc['business_type']}** completed these cash transactions:\n"
        f"- CRJ: Capital invested **{_fmt_r(capital)}**; Current Income **{_fmt_r(cur_inc)}**\n"
        f"- CPJ: Equipment bought **{_fmt_r(equip)}**; Wages paid **{_fmt_r(wages)}**; Stationery paid **{_fmt_r(stat)}**; Owner Drawings **{_fmt_r(drawings)}**\n\n"
        f"Calculate: **(a)** Closing Bank balance, **(b)** Net Profit, and **(c)** Closing Owner's Equity."
    )
    expected = f"(a) Bank: {_fmt_r(bank_bal)}; (b) Net Profit: {_fmt_r(profit)}; (c) Owner's Equity: {_fmt_r(final_oe)}"
    sol = (
        f"**{expected}** [6 marks]\n\n"
        f"**Working:**\n"
        f"- **(a) Bank Closing Balance (Dr):** $({capital} + {cur_inc}) - ({equip} + {wages} + {stat} + {drawings}) = {bank_bal}$ (**{_fmt_r(bank_bal)}**) [2 marks]\n"
        f"- **(b) Net Profit (Nominal Section):** ${cur_inc} - ({wages} + {stat}) = {profit}$ (**{_fmt_r(profit)}**) [2 marks]\n"
        f"- **(c) Closing Owner's Equity:** ${capital} + {profit} - {drawings} = {final_oe}$ (**{_fmt_r(final_oe)}**) [2 marks]\n"
        f"*(Check: Total Assets = Bank {_fmt_r(bank_bal)} + Equipment {_fmt_r(equip)} = {_fmt_r(bank_bal + equip)} = Owner's Equity!)*"
    )
    return _build_short(
        rng,
        qid_prefix="g8_gl_50",
        subskill="50_end_to_end_service_business_ledger_to_profit_synthesis",
        title="End-to-End Service Business Ledger & Profit Synthesis",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=6,
        qtype="short_answer",
        hints={
            "tier_1": "Compute Bank from CRJ - CPJ, Profit from Income - Expenses (excluding Equipment/Drawings), and Equity from Capital + Profit - Drawings.",
            "tier_2": f"Remember Equipment ({_fmt_r(equip)}) is an Asset, not an Expense in profit.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": f"(a) Closing Bank = {_fmt_r(bank_bal)}", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": f"(b) Net Profit = {_fmt_r(profit)}", "marks": 2, "editable": True},
            {"id": "mp_3", "desc": f"(c) Closing Owner's Equity = {_fmt_r(final_oe)}", "marks": 2, "editable": True},
        ],
        misconception_tags=["including_equipment_in_profit", "omitting_drawings_from_equity"],
    )


BUILDERS_26_50 = {
    "26_crj_to_bank_and_current_income_t_accounts": arch_26_crj_to_bank_and_current_income_t_accounts,
    "27_cpj_to_bank_and_expense_t_accounts": arch_27_cpj_to_bank_and_expense_t_accounts,
    "28_mixed_crj_cpj_posting_table": arch_28_mixed_crj_cpj_posting_table,
    "29_balancing_bank_t_account_debit_balance": arch_29_balancing_bank_t_account_debit_balance,
    "30_balancing_capital_or_income_credit_t_account": arch_30_balancing_capital_or_income_credit_t_account,
    "31_identifying_balance_cd_and_bd_sides": arch_31_identifying_balance_cd_and_bd_sides,
    "32_carrying_over_non_current_asset_balances": arch_32_carrying_over_non_current_asset_balances,
    "33_multi_month_closing_to_opening_balance_calc": arch_33_multi_month_closing_to_opening_balance_calc,
    "34_calculating_missing_cpj_or_crj_from_ledger": arch_34_calculating_missing_cpj_or_crj_from_ledger,
    "35_totaling_nominal_income_and_expense_accounts": arch_35_totaling_nominal_income_and_expense_accounts,
    "36_calculating_net_profit_from_nominal_accounts": arch_36_calculating_net_profit_from_nominal_accounts,
    "37_trial_balance_purpose_mathematical_check": arch_37_trial_balance_purpose_mathematical_check,
    "38_trial_balance_standard_account_ordering": arch_38_trial_balance_standard_account_ordering,
    "39_trial_balance_debit_vs_credit_column_sorting": arch_39_trial_balance_debit_vs_credit_column_sorting,
    "40_full_trial_balance_preparation_table": arch_40_full_trial_balance_preparation_table,
    "41_solving_missing_trial_balance_figure": arch_41_solving_missing_trial_balance_figure,
    "42_trial_balance_imbalance_diagnostic_calculation": arch_42_trial_balance_imbalance_diagnostic_calculation,
    "43_halving_rule_reversed_posting_error_detection": arch_43_halving_rule_reversed_posting_error_detection,
    "44_ledger_posting_errors_not_revealed_by_tb": arch_44_ledger_posting_errors_not_revealed_by_tb,
    "45_trial_balance_sections_classification_b_vs_n": arch_45_trial_balance_sections_classification_b_vs_n,
    "46_crj_capital_and_services_bank_total_reconciliation": arch_46_crj_capital_and_services_bank_total_reconciliation,
    "47_cpj_expenses_and_drawings_bank_total_reconciliation": arch_47_cpj_expenses_and_drawings_bank_total_reconciliation,
    "48_posting_folio_cross_reference_audit": arch_48_posting_folio_cross_reference_audit,
    "49_bank_overdraft_credit_balance_recognition": arch_49_bank_overdraft_credit_balance_recognition,
    "50_end_to_end_service_business_ledger_to_profit_synthesis": arch_50_end_to_end_service_business_ledger_to_profit_synthesis,
}
