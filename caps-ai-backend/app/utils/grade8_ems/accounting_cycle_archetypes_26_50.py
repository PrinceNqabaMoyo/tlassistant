"""Grade 8 EMS — The Accounting Cycle Archetypes 26–50.
Grounded strictly in curriculum_docs_auto/EMS_Gr8/Term 2/01. the accounting cycle.md.
Zero-LLM, deterministic via rng: random.Random, authentic South African context.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List
from xml.sax.saxutils import escape as _xml_escape

from app.utils.ems_namelist import SUPPLIERS
from app.utils.grade8_ems.accounting_cycle_archetypes_01_25 import (
    _BANKS,
    _make_mcq,
    _make_rubric,
    _make_table,
    _make_typed,
    _svg_cycle_flow,
    _svg_t_account,
    fmt_r,
    get_ems_scenario,
)


def _svg_summary_card(title: str, subtitle: str, rows: List[tuple[str, str]]) -> str:
    """Render a crisp Paper & Ink accounting extract card SVG."""
    row_h = 24
    h = 78 + len(rows) * row_h
    lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 {h}" width="100%" style="max-width:540px;font-family:Arial,sans-serif;">',
        f'<rect x="4" y="4" width="532" height="{h - 8}" rx="8" fill="#FFFFFF" stroke="#1E293B" stroke-width="1.5"/>',
        f'<rect x="4" y="4" width="532" height="44" rx="8" fill="#13519C"/>',
        f'<rect x="4" y="34" width="532" height="14" fill="#13519C"/>',
        f'<text x="20" y="24" font-size="13" font-weight="bold" fill="#FFFFFF">{_xml_escape(title)}</text>',
        f'<text x="20" y="40" font-size="10" fill="#DBEAFE">{_xml_escape(subtitle)}</text>',
    ]
    for idx, (lbl, val) in enumerate(rows):
        y = 70 + idx * row_h
        bg = "#F8FAFC" if idx % 2 == 0 else "#FFFFFF"
        lines.append(f'<rect x="14" y="{y - 15}" width="512" height="22" fill="{bg}" rx="3"/>')
        lines.append(f'<text x="22" y="{y}" font-size="12" fill="#1E293B">{_xml_escape(lbl)}</text>')
        lines.append(f'<text x="516" y="{y}" font-size="12" font-weight="bold" text-anchor="end" fill="#0F172A">{_xml_escape(val)}</text>')
    lines.append("</svg>")
    return "".join(lines)


def _b26_trace_drawings_cash_through_cycle(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    amt = rng.randint(5, 25) * 100
    prompt = (
        f"Trace the transaction: '{s['entrepreneur']} withdraws {fmt_r(amt)} from the bank account of {s['business']} for personal family expenses.' "
        f"Which accounting cycle pathway is correct?"
    )
    ans = "EFT / Bank Statement -> CPJ -> Debit Drawings, Credit Bank"
    opts = [
        "EFT / Bank Statement -> CPJ -> Debit Drawings, Credit Bank",
        "Duplicate Receipt -> CRJ -> Debit Bank, Credit Drawings",
        "Cash Invoice -> CPJ -> Debit Expenses, Credit Capital",
        "Deposit Slip -> CRJ -> Debit Drawings, Credit Capital",
    ]
    exp = f"Personal cash withdrawals ({fmt_r(amt)}) reduce Bank -> CPJ -> Debit Drawings (reduces Owner's Equity) and Credit Bank (reduces Assets)."
    return _make_mcq(
        rng,
        subskill="26_trace_drawings_cash_through_cycle",
        title="Trace Owner Drawings Through Cycle",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Cash leaves the business bank account -> CPJ.",
            "tier_2": "Drawings increases on Debit (DEAD) and decreases Bank on Credit.",
            "tier_3": ans,
        },
        misconception_tags=["records_drawings_in_crj_or_credits_drawings"],
        question_family_id="trace_drawings",
    )


def _b27_trace_rent_income_through_cycle(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    amt = rng.randint(25, 65) * 100
    prompt = (
        f"Trace the transaction: '{s['business']} receives {fmt_r(amt)} EFT from a tenant for sub-letting an unused storeroom in {s['area']}.' "
        f"Select the correct cycle sequence."
    )
    ans = "Duplicate Receipt / Bank Statement -> CRJ -> Debit Bank, Credit Rent Income"
    opts = [
        "Duplicate Receipt / Bank Statement -> CRJ -> Debit Bank, Credit Rent Income",
        "EFT Payment Advice -> CPJ -> Debit Rent Expense, Credit Bank",
        "Cash Register Roll -> CPJ -> Debit Bank, Credit Rent Income",
        "Cash Invoice -> CRJ -> Debit Rent Income, Credit Bank",
    ]
    exp = f"Receiving {fmt_r(amt)} rent increases Bank -> CRJ -> Debit Bank (Asset +) and Credit Rent Income (Income +)."
    return _make_mcq(
        rng,
        subskill="27_trace_rent_income_through_cycle",
        title="Trace Rent Income Through Cycle",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Money was RECEIVED by the business -> CRJ.",
            "tier_2": "Dr Bank (Asset +), Cr Rent Income (Nominal Account +).",
            "tier_3": ans,
        },
        misconception_tags=["confuses_rent_income_and_rent_expense"],
        question_family_id="trace_rent_income",
    )


def _b28_trace_equipment_cash_through_cycle(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    sup = rng.choice(SUPPLIERS)
    amt = rng.randint(5, 22) * 1000
    prompt = (
        f"Trace the transaction: '{s['business']} purchases office shelving and a till printer from {sup} for {fmt_r(amt)}, paying immediately via EFT.' "
        f"Choose the correct Source Doc -> Journal -> Ledger posting."
    )
    ans = "Cash Invoice / EFT Proof -> CPJ -> Debit Equipment, Credit Bank"
    opts = [
        "Cash Invoice / EFT Proof -> CPJ -> Debit Equipment, Credit Bank",
        "Duplicate Receipt -> CRJ -> Debit Bank, Credit Equipment",
        "EFT Proof -> CPJ -> Debit Stationery, Credit Bank",
        "Deposit Slip -> CPJ -> Debit Creditors Control, Credit Bank",
    ]
    exp = f"Paying {fmt_r(amt)} to {sup} for lasting equipment enters CPJ -> Debit Equipment (Fixed Asset +), Credit Bank (Asset -)."
    return _make_mcq(
        rng,
        subskill="28_trace_equipment_cash_through_cycle",
        title="Trace Cash Equipment Purchase",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Money left Bank to buy a lasting Asset (Equipment).",
            "tier_2": "CPJ -> Debit Equipment (Asset +), Credit Bank (Asset -).",
            "tier_3": ans,
        },
        misconception_tags=["records_equipment_as_stationery_expense"],
        question_family_id="trace_equipment",
    )


def _b29_trace_wages_payment_through_cycle(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    amt = rng.randint(14, 38) * 100
    prompt = (
        f"Trace the transaction: '{s['business']} pays weekly wages of {fmt_r(amt)} to assistant workers from the business bank account.' "
        f"Which cycle path applies?"
    )
    ans = "EFT Confirmation / Wages Register -> CPJ -> Debit Wages, Credit Bank"
    opts = [
        "EFT Confirmation / Wages Register -> CPJ -> Debit Wages, Credit Bank",
        "Duplicate Receipt -> CRJ -> Debit Bank, Credit Wages",
        "Cash Register Roll -> CPJ -> Debit Drawings, Credit Bank",
        "Bank Deposit Slip -> CRJ -> Debit Wages, Credit Capital",
    ]
    exp = f"Weekly wages paid ({fmt_r(amt)}) leave Bank via CPJ -> Debit Wages (Expense + / OE -) and Credit Bank (Asset -)."
    return _make_mcq(
        rng,
        subskill="29_trace_wages_payment_through_cycle",
        title="Trace Wages Payment Through Cycle",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Staff wages are an Operating Expense paid out of Bank.",
            "tier_2": "CPJ -> Dr Wages, Cr Bank.",
            "tier_3": ans,
        },
        misconception_tags=["confuses_wages_with_drawings"],
        question_family_id="trace_wages",
    )


def _b30_trace_bank_loan_receipt_through_cycle(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    bank = rng.choice(_BANKS)
    amt = rng.randint(30, 90) * 1000
    prompt = (
        f"Trace the transaction: '{s['business']} receives a {fmt_r(amt)} 3-year business loan from {bank}, deposited straight into the business bank account.' "
        f"Which cycle entry is correct?"
    )
    ans = "Bank Statement / Loan Agreement -> CRJ -> Debit Bank, Credit Loan (Liability)"
    opts = [
        "Bank Statement / Loan Agreement -> CRJ -> Debit Bank, Credit Loan (Liability)",
        "EFT Payment Advice -> CPJ -> Debit Loan, Credit Bank",
        "Cash Invoice -> CRJ -> Debit Bank, Credit Current Income",
        "Deposit Slip -> CRJ -> Debit Capital, Credit Bank",
    ]
    exp = f"Receiving {fmt_r(amt)} loan proceeds increases Bank (CRJ) -> Dr Bank (Asset +) and Cr Bank Loan (Long-term Liability +)."
    return _make_mcq(
        rng,
        subskill="30_trace_bank_loan_receipt_through_cycle",
        title="Trace Bank Loan Receipt Through Cycle",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Cash enters Bank (CRJ), while a repayment debt (Liability) is created.",
            "tier_2": "CRJ -> Dr Bank (+A), Cr Bank Loan (+L).",
            "tier_3": ans,
        },
        misconception_tags=["credits_current_income_for_bank_loan"],
        question_family_id="trace_bank_loan",
    )


def _b31_accounting_equation_vehicle_table(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    cap = rng.randint(50, 120) * 1000
    veh = rng.randint(35, 80) * 1000
    equip = rng.randint(6, 15) * 1000
    headers = ["Transaction", "Assets (A)", "Owner's Equity (OE)", "Liabilities (L)"]
    table_rows = [
        [(f"Owner deposits {fmt_r(cap)} Capital.", "given", False), (f"+{fmt_r(cap)}", "required", True), (f"+{fmt_r(cap)}", "required", True), ("0", "required", True)],
        [(f"Bought delivery vehicle cash/EFT for {fmt_r(veh)}.", "given", False), (f"+{fmt_r(veh)} / -{fmt_r(veh)} (0)", "required", True), ("0", "required", True), ("0", "required", True)],
        [(f"Bought equipment on credit for {fmt_r(equip)}.", "given", False), (f"+{fmt_r(equip)}", "required", True), ("0", "required", True), (f"+{fmt_r(equip)}", "required", True)],
    ]
    cell_hints = {
        "t0_r0_c1": f"Bank increases by {fmt_r(cap)} -> +{fmt_r(cap)}.",
        "t0_r0_c2": f"Capital increases Owner's Equity -> +{fmt_r(cap)}.",
        "t0_r0_c3": "No liability created -> 0.",
        "t0_r1_c1": f"Vehicles +{fmt_r(veh)} and Bank -{fmt_r(veh)} -> write +{fmt_r(veh)} / -{fmt_r(veh)} (0).",
        "t0_r1_c2": "Asset exchange does not affect OE -> 0.",
        "t0_r1_c3": "Paid cash/EFT, so Liabilities unchanged -> 0.",
        "t0_r2_c1": f"Equipment increases -> +{fmt_r(equip)}.",
        "t0_r2_c2": "Buying asset on credit does not change OE -> 0.",
        "t0_r2_c3": f"Creditors Control increases -> +{fmt_r(equip)}.",
    }
    prompt = f"Complete the Accounting Equation analysis table below for {s['business']} in {s['area']}."
    return _make_table(
        rng,
        subskill="31_accounting_equation_vehicle_table",
        title="Accounting Equation: Capital, Vehicle & Equipment",
        prompt=prompt,
        journal_type="accounting_equation",
        headers=headers,
        table_rows=table_rows,
        cell_hints=cell_hints,
        hints={
            "tier_1": "Watch Row 2 carefully: buying a vehicle for cash increases Vehicles AND decreases Bank!",
            "tier_2": "Row 1 (+A, +OE), Row 2 (+A/-A = 0 net), Row 3 (+A, +L).",
            "tier_3": f"Row 2 Assets cell: +{fmt_r(veh)} / -{fmt_r(veh)} (0).",
        },
        misconception_tags=["forgets_bank_decrease_on_cash_asset_purchase"],
        question_family_id="equation_vehicle_table",
    )


def _b32_accounting_equation_income_expense_table(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    svc = rng.randint(18, 45) * 100
    tel = rng.randint(6, 18) * 100
    draw = rng.randint(8, 22) * 100
    headers = ["Transaction", "Account Debited", "Account Credited", "A = OE + L Net Effect"]
    table_rows = [
        [(f"Cash received for services rendered, {fmt_r(svc)}.", "given", False), ("Bank", "required", True), ("Current Income", "required", True), (f"+{fmt_r(svc)} = +{fmt_r(svc)} + 0", "required", True)],
        [(f"Paid Telephone account via EFT, {fmt_r(tel)}.", "given", False), ("Telephone", "required", True), ("Bank", "required", True), (f"-{fmt_r(tel)} = -{fmt_r(tel)} + 0", "required", True)],
        [(f"Owner withdrew {fmt_r(draw)} cash for personal use.", "given", False), ("Drawings", "required", True), ("Bank", "required", True), (f"-{fmt_r(draw)} = -{fmt_r(draw)} + 0", "required", True)],
    ]
    cell_hints = {
        "t0_r0_c1": "Bank receives cash (+Asset = Dr).",
        "t0_r0_c2": "Service revenue -> Current Income (+Income = Cr).",
        "t0_r0_c3": f"+{fmt_r(svc)} = +{fmt_r(svc)} + 0",
        "t0_r1_c1": "Expense increases on Debit -> Telephone.",
        "t0_r1_c2": "Bank decreases on Credit -> Bank.",
        "t0_r1_c3": f"-{fmt_r(tel)} = -{fmt_r(tel)} + 0",
        "t0_r2_c1": "Owner withdrawal -> Drawings (Dr).",
        "t0_r2_c2": "Cash paid out of Bank (Cr).",
        "t0_r2_c3": f"-{fmt_r(draw)} = -{fmt_r(draw)} + 0",
    }
    prompt = f"Record Account Debited, Account Credited, and the Accounting Equation effect (`+R... = +R... + 0` or `-R... = -R... + 0`) for {s['business']}."
    return _make_table(
        rng,
        subskill="32_accounting_equation_income_expense_table",
        title="Double Entry & Equation Integration Table",
        prompt=prompt,
        journal_type="dr_cr_equation",
        headers=headers,
        table_rows=table_rows,
        cell_hints=cell_hints,
        hints={
            "tier_1": "Apply DEAD (Dr increases Drawings, Expenses, Assets) and CLIC (Cr increases Liabilities, Income, Capital).",
            "tier_2": "Service income increases Bank & OE; expenses & drawings decrease Bank & OE.",
            "tier_3": "Row 1: Bank / Current Income | Row 2: Telephone / Bank | Row 3: Drawings / Bank.",
        },
        misconception_tags=["reverses_dr_cr_on_income_or_drawings"],
        question_family_id="dr_cr_equation_table",
    )


def _b33_full_cycle_mapping_table_drill(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    amt1 = rng.randint(20, 60) * 1000
    amt2 = rng.randint(5, 19) * 100
    amt3 = rng.randint(15, 45) * 100
    headers = ["Transaction", "Source Document", "Journal", "Account Debited", "Account Credited"]
    table_rows = [
        [(f"Owner contributed {fmt_r(amt1)} Capital.", "given", False), ("Duplicate Receipt", "required", True), ("CRJ", "required", True), ("Bank", "required", True), ("Capital", "required", True)],
        [(f"Paid {fmt_r(amt2)} for Stationery via EFT.", "given", False), ("EFT Proof / Cash Invoice", "required", True), ("CPJ", "required", True), ("Stationery", "required", True), ("Bank", "required", True)],
        [(f"Services rendered cash, {fmt_r(amt3)}.", "given", False), ("Cash Register Roll", "required", True), ("CRJ", "required", True), ("Bank", "required", True), ("Current Income", "required", True)],
    ]
    cell_hints = {
        "t0_r0_c1": "Duplicate Receipt issued to owner.",
        "t0_r0_c2": "CRJ (cash received).",
        "t0_r0_c3": "Bank",
        "t0_r0_c4": "Capital",
        "t0_r1_c1": "EFT Proof / Cash Invoice",
        "t0_r1_c2": "CPJ (cash paid).",
        "t0_r1_c3": "Stationery",
        "t0_r1_c4": "Bank",
        "t0_r2_c1": "Cash Register Roll",
        "t0_r2_c2": "CRJ",
        "t0_r2_c3": "Bank",
        "t0_r2_c4": "Current Income",
    }
    prompt = f"Trace all three transactions of {s['business']} across the full cycle stages in the table below."
    return _make_table(
        rng,
        subskill="33_full_cycle_mapping_table_drill",
        title="Full Accounting Cycle Mapping Table",
        prompt=prompt,
        journal_type="full_cycle_trace",
        headers=headers,
        table_rows=table_rows,
        cell_hints=cell_hints,
        hints={
            "tier_1": "Identify whether cash came in (CRJ) or went out (CPJ) on each row first.",
            "tier_2": "Bank is debited in CRJ transactions and credited in CPJ transactions.",
            "tier_3": "1: Duplicate Receipt / CRJ / Bank / Capital | 2: EFT / CPJ / Stationery / Bank | 3: CRR / CRJ / Bank / Current Income.",
        },
        misconception_tags=["breaks_source_doc_journal_ledger_alignment"],
        question_family_id="full_cycle_mapping",
    )


def _b34_crj_monthly_total_bank_posting(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    cap = rng.randint(30, 80) * 1000
    curr_inc = rng.randint(15, 45) * 1000
    rent_inc = rng.randint(4, 12) * 1000
    bank_tot = cap + curr_inc + rent_inc
    ans = fmt_r(bank_tot)
    svg = _svg_summary_card(
        f"{s['business']} — CRJ Monthly Totals",
        f"Month-end Journal Summary ({s['area']})",
        [
            ("Current Income column total", fmt_r(curr_inc)),
            ("Sundry: Capital", fmt_r(cap)),
            ("Sundry: Rent Income", fmt_r(rent_inc)),
            ("Bank column total", "???"),
        ],
    )
    prompt = (
        f"Examine the Cash Receipts Journal (CRJ) monthly summary for {s['business']}. "
        f"Calculate the total Bank Debit posting that will be transferred to the General Ledger Bank T-account at month-end."
    )
    steps = [
        f"In CRJ, Total Bank = Current Income + all Sundry Receipts.",
        f"Bank Total = {fmt_r(curr_inc)} + {fmt_r(cap)} + {fmt_r(rent_inc)} = {ans}.",
        f"Posted as Dr Bank 'Total Receipts (CRJ)' {ans}.",
    ]
    return _make_typed(
        rng,
        subskill="34_crj_monthly_total_bank_posting",
        title="CRJ Month-End Bank Posting Total",
        prompt=prompt,
        correct_ans=ans,
        acceptable_answers=[ans, f"R{bank_tot}", str(bank_tot)],
        steps=steps,
        hints={
            "tier_1": "Every receipt deposited in CRJ contributes to the Bank column total.",
            "tier_2": "Add Current Income + Capital + Rent Income.",
            "tier_3": f"Bank total debited = {ans}.",
        },
        misconception_tags=["omits_sundry_accounts_from_bank_total"],
        question_family_id="crj_total_posting",
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    )


def _b35_cpj_monthly_total_bank_posting(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    wages = rng.randint(8, 20) * 1000
    stat = rng.randint(1, 5) * 1000
    equip = rng.randint(10, 28) * 1000
    bank_tot = wages + stat + equip
    ans = fmt_r(bank_tot)
    prompt = (
        f"At month-end, the Cash Payments Journal (CPJ) of {s['business']} shows Wages total {fmt_r(wages)}, "
        f"Stationery total {fmt_r(stat)}, and a Sundry Account payment of {fmt_r(equip)} for Equipment. "
        f"Calculate the total amount CREDITED to the Bank T-account in the General Ledger."
    )
    steps = [
        f"Add all CPJ payment columns and sundry payments: Wages ({fmt_r(wages)}) + Stationery ({fmt_r(stat)}) + Equipment ({fmt_r(equip)}).",
        f"Total Credited to Bank = {ans}.",
    ]
    return _make_typed(
        rng,
        subskill="35_cpj_monthly_total_bank_posting",
        title="CPJ Month-End Bank Credit Total",
        prompt=prompt,
        correct_ans=ans,
        acceptable_answers=[ans, f"R{bank_tot}", str(bank_tot)],
        steps=steps,
        hints={
            "tier_1": "Total cash paid out of Bank includes both analysis columns and Sundry payments.",
            "tier_2": f"Sum {fmt_r(wages)} + {fmt_r(stat)} + {fmt_r(equip)}.",
            "tier_3": f"Bank Credit total = {ans}.",
        },
        misconception_tags=["omits_sundry_from_cpj_bank_total"],
        question_family_id="cpj_total_posting",
    )


def _b36_general_ledger_balance_b_d_calc(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    dr_tot = rng.randint(45, 95) * 1000
    cr_tot = rng.randint(18, 40) * 1000
    bal = dr_tot - cr_tot
    ans = fmt_r(bal)
    svg = _svg_t_account("Bank (B3)", "Total Receipts (CRJ)", fmt_r(dr_tot), "Total Payments (CPJ)", fmt_r(cr_tot))
    prompt = (
        f"Inspect the General Ledger Bank T-account of {s['business']}. "
        f"Calculate the closing Debit balance brought down (Balance b/d) at month-end."
    )
    steps = [
        f"Total Debit side (Receipts) = {fmt_r(dr_tot)}. Total Credit side (Payments) = {fmt_r(cr_tot)}.",
        f"Since Debit > Credit, subtract Payments from Receipts: {fmt_r(dr_tot)} - {fmt_r(cr_tot)} = {ans}.",
        f"Bank carries a favourable Debit balance b/d of {ans}.",
    ]
    return _make_typed(
        rng,
        subskill="36_general_ledger_balance_b_d_calc",
        title="Balancing a General Ledger T-Account",
        prompt=prompt,
        correct_ans=ans,
        acceptable_answers=[ans, f"R{bal}", str(bal)],
        steps=steps,
        hints={
            "tier_1": "Subtract the smaller side (Payments Cr) from the larger side (Receipts Dr).",
            "tier_2": f"Balance = {fmt_r(dr_tot)} - {fmt_r(cr_tot)}.",
            "tier_3": f"Closing Bank Balance b/d = {ans}.",
        },
        misconception_tags=["adds_debit_and_credit_sides_instead_of_balancing"],
        question_family_id="balance_t_account",
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    )


def _b37_trial_balance_balancing_check(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    cap = rng.randint(80, 150) * 1000
    inc = rng.randint(30, 65) * 1000
    cr_total = cap + inc
    veh = rng.randint(50, 90) * 1000
    exp = rng.randint(15, 25) * 1000
    missing_bank = cr_total - (veh + exp)
    ans = fmt_r(missing_bank)
    prompt = (
        f"In the Trial Balance of {s['business']}, the Credit column contains Capital ({fmt_r(cap)}) and Current Income ({fmt_r(inc)}). "
        f"The Debit column lists Vehicles ({fmt_r(veh)}), Operating Expenses ({fmt_r(exp)}), and Bank (missing). "
        f"If Total Debits equal Total Credits, calculate the missing Bank balance."
    )
    steps = [
        f"Total Credits = {fmt_r(cap)} + {fmt_r(inc)} = {fmt_r(cr_total)}.",
        f"Known Debits = {fmt_r(veh)} + {fmt_r(exp)} = {fmt_r(veh + exp)}.",
        f"Missing Bank Debit balance = {fmt_r(cr_total)} - {fmt_r(veh + exp)} = {ans}.",
    ]
    return _make_typed(
        rng,
        subskill="37_trial_balance_balancing_check",
        title="Solving Missing Balance in Trial Balance",
        prompt=prompt,
        correct_ans=ans,
        acceptable_answers=[ans, f"R{missing_bank}", str(missing_bank)],
        steps=steps,
        hints={
            "tier_1": "First add all Credit balances to find Total Credits (which equals Total Debits).",
            "tier_2": "Subtract known Debits (Vehicles + Expenses) from Total Credits.",
            "tier_3": f"Missing Bank balance = {ans}.",
        },
        misconception_tags=["puts_capital_in_debit_column"],
        question_family_id="trial_balance_missing",
    )


def _b38_trial_balance_limitation_errors(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    amt = rng.randint(5, 25) * 100
    prompt = (
        f"The Trial Balance of {s['business']} balances at both Totals, yet {s['entrepreneur']} notices a {fmt_r(amt)} Stationery payment was accidentally debited to Telephone instead of Stationery. "
        f"Why did the Trial Balance STILL balance?"
    )
    ans = "Because an equal Debit and Credit of the same amount was still posted (an error of principle/commission to the wrong account does not upset Dr = Cr)"
    opts = [
        "Because an equal Debit and Credit of the same amount was still posted (an error of principle/commission to the wrong account does not upset Dr = Cr)",
        "Because Trial Balances only check the Cash Receipts Journal and ignore Expenses",
        "Because Telephone is a Credit account in the Balance Sheet section",
        "Because mistakes under R5 000 are automatically adjusted by commercial banks",
    ]
    exp = f"A Trial Balance only tests whether Total Debits equal Total Credits. Debiting Telephone instead of Stationery for {fmt_r(amt)} keeps Dr = Cr equal while posting to the wrong Nominal account."
    return _make_mcq(
        rng,
        subskill="38_trial_balance_limitation_errors",
        title="Limitations of the Trial Balance",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Did both sides still receive a Debit and Credit of the exact same Rand value?",
            "tier_2": "Dr Telephone = Cr Bank still satisfies Total Debits = Total Credits.",
            "tier_3": ans,
        },
        misconception_tags=["believes_balanced_trial_balance_means_zero_errors"],
        question_family_id="trial_balance_limitations",
    )


def _b39_income_statement_vs_balance_sheet_purpose(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    year = rng.choice([2024, 2025, 2026])
    prompt = (
        f"At the end of the {year} financial year, {s['business']} prepares both an Income Statement and a Balance Sheet. "
        f"Which comparison accurately states what each financial statement shows?"
    )
    ans = "Income Statement calculates Net Profit/Loss (Income - Expenses) for the year; Balance Sheet shows financial position (A = OE + L) on the final day"
    opts = [
        "Income Statement calculates Net Profit/Loss (Income - Expenses) for the year; Balance Sheet shows financial position (A = OE + L) on the final day",
        "Income Statement lists Vehicles and Capital; Balance Sheet lists only daily till slips",
        "Both statements perform the exact same calculation using only Nominal accounts",
        "Balance Sheet calculates Net Profit; Income Statement lists Assets and Liabilities",
    ]
    exp = f"For {s['business']} ({year}), the Income Statement summarises financial performance (Income minus Expenses = Profit/Loss) over 12 months, while the Balance Sheet presents Assets = OE + L on the closing date."
    return _make_mcq(
        rng,
        subskill="39_income_statement_vs_balance_sheet_purpose",
        title="Income Statement vs Balance Sheet",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Match Nominal accounts (Income/Expenses) vs Balance Sheet accounts (A/OE/L).",
            "tier_2": "Income Statement -> Profit over a year; Balance Sheet -> Assets = OE + L on a specific date.",
            "tier_3": ans,
        },
        misconception_tags=["swaps_income_statement_and_balance_sheet_contents"],
        question_family_id="income_stmt_vs_balance_sheet",
    )


def _b40_income_statement_net_profit_from_tb(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    cap = rng.randint(90, 180) * 1000
    veh = rng.randint(60, 120) * 1000
    curr_inc = rng.randint(45, 95) * 1000
    wages = rng.randint(15, 28) * 1000
    tel = rng.randint(3, 8) * 1000
    profit = curr_inc - (wages + tel)
    ans = fmt_r(profit)
    svg = _svg_summary_card(
        f"{s['business']} — Trial Balance Extract",
        f"Year-End Balances ({s['area']})",
        [
            ("Capital (Balance Sheet Sec.)", fmt_r(cap)),
            ("Vehicles (Balance Sheet Sec.)", fmt_r(veh)),
            ("Current Income (Nominal Sec.)", fmt_r(curr_inc)),
            ("Wages (Nominal Sec.)", fmt_r(wages)),
            ("Telephone (Nominal Sec.)", fmt_r(tel)),
        ],
    )
    prompt = (
        f"Inspect the Trial Balance extract provided for {s['business']}. "
        f"Using ONLY the relevant Nominal Accounts Section balances, calculate the Net Profit for the Income Statement."
    )
    steps = [
        f"Select ONLY Income and Expense accounts (exclude Capital {fmt_r(cap)} and Vehicles {fmt_r(veh)}).",
        f"Total Income = Current Income = {fmt_r(curr_inc)}.",
        f"Total Expenses = Wages ({fmt_r(wages)}) + Telephone ({fmt_r(tel)}) = {fmt_r(wages + tel)}.",
        f"Net Profit = {fmt_r(curr_inc)} - {fmt_r(wages + tel)} = {ans}.",
    ]
    return _make_typed(
        rng,
        subskill="40_income_statement_net_profit_from_tb",
        title="Calculate Net Profit from Trial Balance",
        prompt=prompt,
        correct_ans=ans,
        acceptable_answers=[ans, f"R{profit}", str(profit)],
        steps=steps,
        hints={
            "tier_1": "Ignore Capital and Vehicles — those belong in the Balance Sheet, not the Income Statement.",
            "tier_2": "Net Profit = Current Income - (Wages + Telephone).",
            "tier_3": f"Net Profit = {ans}.",
        },
        misconception_tags=["includes_capital_or_vehicles_in_income_statement"],
        question_family_id="tb_to_income_statement",
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    )


def _b41_balance_sheet_total_assets_from_tb(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    land = rng.randint(250, 450) * 1000
    equip = rng.randint(25, 65) * 1000
    bank = rng.randint(12, 38) * 1000
    cred = rng.randint(10, 25) * 1000
    curr_inc = rng.randint(35, 70) * 1000
    tot_assets = land + equip + bank
    ans = fmt_r(tot_assets)
    prompt = (
        f"From the Trial Balance of {s['business']}: Land & Buildings {fmt_r(land)}, Equipment {fmt_r(equip)}, "
        f"Bank (Debit) {fmt_r(bank)}, Creditors Control {fmt_r(cred)}, Current Income {fmt_r(curr_inc)}. "
        f"Calculate Total Assets to be reported on the Balance Sheet."
    )
    steps = [
        f"Identify Assets only: Land & Buildings ({fmt_r(land)}) + Equipment ({fmt_r(equip)}) + Bank ({fmt_r(bank)}).",
        f"Exclude Creditors Control ({fmt_r(cred)}, Liability) and Current Income ({fmt_r(curr_inc)}, Nominal Income).",
        f"Total Assets = {ans}.",
    ]
    return _make_typed(
        rng,
        subskill="41_balance_sheet_total_assets_from_tb",
        title="Balance Sheet Total Assets from Trial Balance",
        prompt=prompt,
        correct_ans=ans,
        acceptable_answers=[ans, f"R{tot_assets}", str(tot_assets)],
        steps=steps,
        hints={
            "tier_1": "Only include Fixed Assets and Current Assets.",
            "tier_2": f"Sum Land & Buildings + Equipment + Bank.",
            "tier_3": f"Total Assets = {ans}.",
        },
        misconception_tags=["adds_current_income_into_balance_sheet_assets"],
        question_family_id="tb_to_balance_sheet_assets",
    )


def _b42_balance_sheet_net_worth_equality(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    cap = rng.randint(100, 180) * 1000
    profit = rng.randint(25, 55) * 1000
    drawings = rng.randint(8, 20) * 1000
    liab = rng.randint(30, 75) * 1000
    closing_oe = cap + profit - drawings
    total_assets = closing_oe + liab
    ans = fmt_r(total_assets)
    prompt = (
        f"At year-end for {s['business']}, Capital was {fmt_r(cap)}, Net Profit was {fmt_r(profit)}, Drawings were {fmt_r(drawings)}, "
        f"and Total Liabilities (Loan + Creditors) were {fmt_r(liab)}. Using Balance Sheet equality (Assets = Owner's Equity + Liabilities), "
        f"what must Total Assets equal?"
    )
    steps = [
        f"Closing Owner's Equity = {fmt_r(cap)} + {fmt_r(profit)} - {fmt_r(drawings)} = {fmt_r(closing_oe)}.",
        f"Total Assets = Closing OE + Liabilities = {fmt_r(closing_oe)} + {fmt_r(liab)} = {ans}.",
    ]
    return _make_typed(
        rng,
        subskill="42_balance_sheet_net_worth_equality",
        title="Balance Sheet Equality Verification",
        prompt=prompt,
        correct_ans=ans,
        acceptable_answers=[ans, f"R{total_assets}", str(total_assets)],
        steps=steps,
        hints={
            "tier_1": "Compute Closing Owner's Equity first (Capital + Profit - Drawings).",
            "tier_2": "Add Total Liabilities to Closing Owner's Equity to find Total Assets.",
            "tier_3": f"Total Assets = {ans}.",
        },
        misconception_tags=["forgets_profit_or_drawings_when_balancing_balance_sheet"],
        question_family_id="balance_sheet_equality",
    )


def _b43_stage_to_document_matching_table(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    pairs = [
        ("Trial Balance", "Lists all General Ledger balances to verify Total Debits equal Total Credits"),
        ("Cash Receipts Journal", "Summarises all cash and EFT inflows chronologically before ledger posting"),
        ("Income Statement", "Reports Total Income minus Total Expenses to determine Net Profit or Loss"),
        ("General Ledger", "Contains individual T-accounts separated into Balance Sheet and Nominal sections"),
        ("Source Documents", "Provides original written transaction proof before any journal entry"),
    ]
    chosen = rng.sample(pairs, 4)
    headers = ["Accounting Record / Statement", "Primary Purpose in Cycle"]
    table_rows = [[(doc, "given", False), (purp, "required", True)] for doc, purp in chosen]
    cell_hints = {f"t0_r{i}_c1": f"Summarise the role of {doc}." for i, (doc, _) in enumerate(chosen)}
    prompt = f"Match each accounting cycle record of {s['business']} to its primary purpose in the table below."
    return _make_table(
        rng,
        subskill="43_stage_to_document_matching_table",
        title="Accounting Records Purpose Matching Table",
        prompt=prompt,
        journal_type="cycle_record_purpose",
        headers=headers,
        table_rows=table_rows,
        cell_hints=cell_hints,
        hints={
            "tier_1": "Think of the distinct function each stage performs in sequence.",
            "tier_2": "Source Docs = proof; CRJ = inflows; Ledger = T-accounts; Trial Balance = Dr=Cr check; Income Statement = Profit.",
            "tier_3": " | ".join(f"{d}: {p}" for d, p in chosen),
        },
        misconception_tags=["confuses_trial_balance_with_income_statement"],
        question_family_id="cycle_record_matching",
    )


def _b44_nominal_accounts_closing_purpose(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    year = rng.choice([2025, 2026])
    prompt = (
        f"Explain why Nominal Accounts (Current Income, Wages, Telephone) at {s['business']} are closed off at the end of {year} "
        f"to reset to zero for the new financial year, whereas Balance Sheet Accounts (Vehicles, Bank, Capital) carry their balances forward."
    )
    sample = (
        f"1. Nominal Accounts measure financial performance (profit or loss) for ONLY ONE financial period ({year}), so resetting them to zero prevents last year's revenue/expenses from distorting next year's profit.\n"
        f"2. Net Profit calculated from closed Nominal Accounts is transferred into Capital, while physical/financial Balances (Vehicles, Bank, Capital) continue into the new year."
    )
    pts = [
        f"Nominal Accounts measure profit/loss for a single period ({year}) and must start at zero next year for accurate comparison.",
        "Net Profit updates Capital, while Balance Sheet accounts represent ongoing Assets, Liabilities, and Owner's Equity carried forward.",
    ]
    return _make_rubric(
        rng,
        subskill="44_nominal_accounts_closing_purpose",
        title="Why Nominal Accounts Close While Balance Sheet Accounts Carry Forward",
        prompt=prompt,
        sample_answer=sample,
        marking_points=pts,
        hints={
            "tier_1": "Think: Should last year's Telephone bill count towards next year's profit? What about last year's delivery van?",
            "tier_2": "Income/Expenses belong to one year (Nominal -> reset); Assets/Capital persist across years (Balance Sheet -> carry forward).",
            "tier_3": sample,
        },
        misconception_tags=["carries_nominal_expenses_into_next_year"],
        question_family_id="nominal_closing_concept",
        marks=2,
    )


def _b45_cycle_missing_step_diagnostic(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    skipped = rng.choice(["Stage 3 (Subsidiary Journals CRJ/CPJ)", "Stage 5 (Trial Balance)"])
    prompt = (
        f"A new clerk at {s['business']} in {s['area']} decides to skip {skipped} to 'save time'. "
        f"Explain TWO concrete accounting problems or errors this shortcut will cause."
    )
    if "Journals" in skipped:
        sample = (
            "1. Massive clutter & lost chronological control: Every single receipt and EFT would crowd the General Ledger Bank T-account instead of neat monthly totals.\n"
            "2. Loss of internal verification: Cross-casting analysis columns in CRJ/CPJ would disappear, making missing deposits or duplicate entries hard to trace."
        )
        pts = [
            "General Ledger Bank account becomes cluttered with hundreds of single entries instead of monthly totals.",
            "Loss of cross-cast error detection and chronological cash-flow analysis.",
        ]
    else:
        sample = (
            "1. Undetected mathematical imbalance: Posting errors where Debits did not equal Credits would pass straight into the Financial Statements.\n"
            "2. Balance Sheet failure: The Balance Sheet (Assets = OE + L) would fail to balance with no easy schedule to locate which T-account was misposted."
        )
        pts = [
            "Debit/Credit arithmetic imbalances pass undetected into Financial Statements.",
            "Harder to locate misposted T-account balances before drafting the Balance Sheet.",
        ]
    return _make_rubric(
        rng,
        subskill="45_cycle_missing_step_diagnostic",
        title="Diagnosing a Skipped Accounting Cycle Stage",
        prompt=prompt,
        sample_answer=sample,
        marking_points=pts,
        hints={
            "tier_1": f"Think directly about the protective job that {skipped} does.",
            "tier_2": "Focus on summary efficiency/error control (for Journals) or Dr=Cr verification (for Trial Balance).",
            "tier_3": sample,
        },
        misconception_tags=["assumes_cycle_stages_are_optional"],
        question_family_id="skipped_stage_diagnostic",
        marks=2,
    )


def _b46_journal_to_ledger_folio_reference(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    amt = rng.randint(12, 48) * 1000
    folio = rng.choice(["CRJ4", "CPJ3"])
    if folio.startswith("CRJ"):
        meaning = f"The {fmt_r(amt)} Debit entry in Bank came from page {folio[3]} of the Cash Receipts Journal"
    else:
        meaning = f"The {fmt_r(amt)} Credit entry in Bank came from page {folio[3]} of the Cash Payments Journal"
    prompt = (
        f"Inside the General Ledger Bank account of {s['business']}, the folio column beside an entry of {fmt_r(amt)} shows '{folio}'. "
        f"What does the folio code '{folio}' indicate?"
    )
    opts = [
        meaning,
        f"It is the business's annual SARS tax registration number",
        f"It means the customer received a {folio[3]}% cash discount",
        f"It is the serial number of the shop cash register",
    ]
    exp = f"Folio references cross-link journals and ledger accounts for fast auditing: '{folio}' tells any auditor/bookkeeper which journal page originated the {fmt_r(amt)} entry."
    return _make_mcq(
        rng,
        subskill="46_journal_to_ledger_folio_reference",
        title="Interpreting Folio Cross-References",
        prompt=prompt,
        options=opts,
        correct_ans=meaning,
        explanation=exp,
        hints={
            "tier_1": "Notice the letters CRJ/CPJ and page number inside the folio code.",
            "tier_2": "Folio codes cross-reference the exact source journal and page number.",
            "tier_3": meaning,
        },
        misconception_tags=["ignores_folio_audit_trail_purpose"],
        question_family_id="folio_reference",
    )


def _b47_sole_trader_end_of_month_checklist(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    month = rng.choice(["March", "June", "September", "November"])
    prompt = (
        f"List in strict chronological order the FOUR closing tasks {s['entrepreneur']} must complete at the end of {month} "
        f"to take {s['business']}'s records from daily source documents up to a verified Trial Balance."
    )
    sample = (
        f"1. Verify all {month} receipts, till rolls, invoices, and EFT slips are entered in CRJ and CPJ, then cast (total) and cross-cast all columns.\n"
        "2. Compare the journals against the monthly Bank Statement to catch bank charges or direct deposits.\n"
        "3. Post monthly totals and Sundry items from CRJ and CPJ to the General Ledger T-accounts and balance each account.\n"
        "4. Extract all General Ledger closing balances into the Trial Balance and confirm Total Debits equal Total Credits."
    )
    pts = [
        "Complete and cast/cross-cast CRJ and CPJ from source documents.",
        "Check Bank Statement for bank charges / direct entries.",
        "Post monthly totals & sundry accounts to General Ledger and balance T-accounts.",
        "Prepare Trial Balance confirming Total Debits = Total Credits.",
    ]
    return _make_rubric(
        rng,
        subskill="47_sole_trader_end_of_month_checklist",
        title="Month-End Closing Checklist",
        prompt=prompt,
        sample_answer=sample,
        marking_points=pts,
        hints={
            "tier_1": "Start from journals/documents and move step-by-step down the cycle.",
            "tier_2": "Sequence: Journals & cast -> Bank Statement check -> Ledger posting & balancing -> Trial Balance.",
            "tier_3": sample,
        },
        misconception_tags=["reverses_ledger_and_trial_balance_closing"],
        question_family_id="month_end_checklist",
    )


def _b48_spot_posting_error_dr_vs_cr(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    amt = rng.randint(15, 55) * 100
    prompt = (
        f"When {s['business']} received {fmt_r(amt)} cash for services rendered, a junior clerk mistakenly CREDITED Bank with {fmt_r(amt)} and DEBITED Current Income with {fmt_r(amt)}. "
        f"What was wrong with this posting and what is the correct General Ledger entry?"
    )
    ans = f"Both sides were reversed — Bank (Asset) increases on Debit and Current Income (Income) increases on Credit, so Dr Bank {fmt_r(amt)}, Cr Current Income {fmt_r(amt)}"
    opts = [
        f"Both sides were reversed — Bank (Asset) increases on Debit and Current Income (Income) increases on Credit, so Dr Bank {fmt_r(amt)}, Cr Current Income {fmt_r(amt)}",
        f"Only the amount was wrong — Services rendered should be posted to Capital",
        f"The clerk posted correctly because cash received always credits Bank",
        f"Services rendered should only be debited to Vehicles",
    ]
    exp = f"Receiving {fmt_r(amt)} increases Bank (Asset -> Debit) and increases Current Income (Income -> Credit). The clerk inverted both Debit and Credit."
    return _make_mcq(
        rng,
        subskill="48_spot_posting_error_dr_vs_cr",
        title="Diagnose Inverted Debit/Credit Posting",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Check DEAD (Debit Assets) and CLIC (Credit Income).",
            "tier_2": "Bank should increase on Debit; Current Income should increase on Credit.",
            "tier_3": ans,
        },
        misconception_tags=["inverts_debit_and_credit_on_cash_receipt"],
        question_family_id="spot_posting_inversion",
    )


def _b49_case_study_journal_and_equation_audit(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    open_bank = rng.randint(8, 18) * 1000
    crj_cash = rng.randint(15, 35) * 1000
    cpj_exp = rng.randint(6, 14) * 1000
    cpj_equip = rng.randint(4, 9) * 1000
    closing_bank = open_bank + crj_cash - (cpj_exp + cpj_equip)
    ans = fmt_r(closing_bank)
    prompt = (
        f"{s['business']} started the month with {fmt_r(open_bank)} in Bank. "
        f"During the month, CRJ receipts for Current Income totalled {fmt_r(crj_cash)}, while CPJ payments included "
        f"{fmt_r(cpj_exp)} for Operating Expenses and {fmt_r(cpj_equip)} for new Equipment. "
        f"Calculate the closing Bank balance at the end of the accounting cycle month."
    )
    steps = [
        f"Opening Bank + CRJ Receipts = {fmt_r(open_bank)} + {fmt_r(crj_cash)} = {fmt_r(open_bank + crj_cash)}.",
        f"Total CPJ Payments = {fmt_r(cpj_exp)} + {fmt_r(cpj_equip)} = {fmt_r(cpj_exp + cpj_equip)}.",
        f"Closing Bank Balance = {fmt_r(open_bank + crj_cash)} - {fmt_r(cpj_exp + cpj_equip)} = {ans}.",
    ]
    return _make_typed(
        rng,
        subskill="49_case_study_journal_and_equation_audit",
        title="Calculate Closing Bank Balance Across CRJ & CPJ",
        prompt=prompt,
        correct_ans=ans,
        acceptable_answers=[ans, f"R{closing_bank}", str(closing_bank)],
        steps=steps,
        hints={
            "tier_1": "Both Expense payments and Equipment payments reduce Bank via CPJ.",
            "tier_2": "Closing Bank = Opening Bank + CRJ Total - Total CPJ Payments.",
            "tier_3": f"Closing Bank = {ans}.",
        },
        misconception_tags=["ignores_asset_purchases_in_bank_balance"],
        question_family_id="closing_bank_crj_cpj",
    )


def _b50_comprehensive_cycle_capstone(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    amt = rng.randint(12, 35) * 100
    svg = _svg_cycle_flow(s["business"], 1)
    prompt = (
        f"Refer to the Accounting Cycle schematic for {s['business']}. "
        f"{s['business']} receives {fmt_r(amt)} EFT from a client for repair services. "
        f"State: (a) the Source Document, (b) the Subsidiary Journal, (c) Account Debited & Account Credited in the General Ledger, and (d) which Financial Statement reports this {fmt_r(amt)}."
    )
    sample = (
        f"(a) Source Document: Duplicate Receipt / Bank Statement EFT credit.\n"
        f"(b) Subsidiary Journal: Cash Receipts Journal (CRJ).\n"
        f"(c) General Ledger: Debit Bank {fmt_r(amt)}, Credit Current Income {fmt_r(amt)}.\n"
        f"(d) Financial Statement: Income Statement (Current Income) — while the closing Bank balance enters the Balance Sheet."
    )
    pts = [
        "Source Document: Duplicate Receipt / Bank Statement.",
        "Subsidiary Journal: Cash Receipts Journal (CRJ).",
        f"General Ledger: Debit Bank ({fmt_r(amt)}), Credit Current Income ({fmt_r(amt)}).",
        "Financial Statement: Income Statement (under Income).",
    ]
    return _make_rubric(
        rng,
        subskill="50_comprehensive_cycle_capstone",
        title="Full Accounting Cycle Capstone",
        prompt=prompt,
        sample_answer=sample,
        marking_points=pts,
        hints={
            "tier_1": "Walk sequentially through Stages 2, 3, 4, and 6 of the cycle.",
            "tier_2": "Receipt -> CRJ -> Dr Bank, Cr Current Income -> Income Statement.",
            "tier_3": sample,
        },
        misconception_tags=["disconnects_ledger_accounts_from_financial_statements"],
        question_family_id="cycle_capstone",
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    )


ARCHETYPES_26_50 = {
    "26_trace_drawings_cash_through_cycle": _b26_trace_drawings_cash_through_cycle,
    "27_trace_rent_income_through_cycle": _b27_trace_rent_income_through_cycle,
    "28_trace_equipment_cash_through_cycle": _b28_trace_equipment_cash_through_cycle,
    "29_trace_wages_payment_through_cycle": _b29_trace_wages_payment_through_cycle,
    "30_trace_bank_loan_receipt_through_cycle": _b30_trace_bank_loan_receipt_through_cycle,
    "31_accounting_equation_vehicle_table": _b31_accounting_equation_vehicle_table,
    "32_accounting_equation_income_expense_table": _b32_accounting_equation_income_expense_table,
    "33_full_cycle_mapping_table_drill": _b33_full_cycle_mapping_table_drill,
    "34_crj_monthly_total_bank_posting": _b34_crj_monthly_total_bank_posting,
    "35_cpj_monthly_total_bank_posting": _b35_cpj_monthly_total_bank_posting,
    "36_general_ledger_balance_b_d_calc": _b36_general_ledger_balance_b_d_calc,
    "37_trial_balance_balancing_check": _b37_trial_balance_balancing_check,
    "38_trial_balance_limitation_errors": _b38_trial_balance_limitation_errors,
    "39_income_statement_vs_balance_sheet_purpose": _b39_income_statement_vs_balance_sheet_purpose,
    "40_income_statement_net_profit_from_tb": _b40_income_statement_net_profit_from_tb,
    "41_balance_sheet_total_assets_from_tb": _b41_balance_sheet_total_assets_from_tb,
    "42_balance_sheet_net_worth_equality": _b42_balance_sheet_net_worth_equality,
    "43_stage_to_document_matching_table": _b43_stage_to_document_matching_table,
    "44_nominal_accounts_closing_purpose": _b44_nominal_accounts_closing_purpose,
    "45_cycle_missing_step_diagnostic": _b45_cycle_missing_step_diagnostic,
    "46_journal_to_ledger_folio_reference": _b46_journal_to_ledger_folio_reference,
    "47_sole_trader_end_of_month_checklist": _b47_sole_trader_end_of_month_checklist,
    "48_spot_posting_error_dr_vs_cr": _b48_spot_posting_error_dr_vs_cr,
    "49_case_study_journal_and_equation_audit": _b49_case_study_journal_and_equation_audit,
    "50_comprehensive_cycle_capstone": _b50_comprehensive_cycle_capstone,
}
