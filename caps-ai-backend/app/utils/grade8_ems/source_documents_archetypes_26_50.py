"""Grade 8 EMS — Source Documents Archetypes 26–50.
Grounded strictly in curriculum_docs_auto/EMS_Gr8/Term 2/02. Source documents.md.
Zero-LLM, deterministic via rng: random.Random, authentic South African context.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List

from app.utils.ems_namelist import NAMES, SUPPLIERS
from app.utils.grade8_ems.source_documents_archetypes_01_25 import (
    _BANKS,
    _make_mcq,
    _make_rubric,
    _make_table,
    _make_typed,
    fmt_r,
    get_ems_scenario,
    svg_doc_plate,
)


def _b26_doc_stationery_purchase_analysis(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    sup = rng.choice(SUPPLIERS)
    amt = rng.randint(4, 19) * 100
    prompt = (
        f"{s['business']} buys pens, receipt books, and printer paper (Stationery) from {sup} for {fmt_r(amt)} cash/EFT. "
        f"Which Source Document, Journal, and General Ledger Accounts apply?"
    )
    ans = "Cash Invoice / EFT Proof -> CPJ -> Debit Stationery (Expense), Credit Bank (Asset -)"
    opts = [
        "Cash Invoice / EFT Proof -> CPJ -> Debit Stationery (Expense), Credit Bank (Asset -)",
        "Duplicate Receipt -> CRJ -> Debit Bank, Credit Stationery",
        "Cash Register Roll -> CPJ -> Debit Equipment, Credit Bank",
        "Bank Deposit Slip -> CRJ -> Debit Stationery, Credit Capital",
    ]
    exp = f"Buying stationery ({fmt_r(amt)}) from {sup} is a cash operating expense -> Cash Invoice/EFT Proof -> CPJ -> Dr Stationery (-OE), Cr Bank (-A)."
    return _make_mcq(
        rng,
        subskill="26_doc_stationery_purchase_analysis",
        title="Source Doc Analysis: Stationery Purchase",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Cash paid out for consumable stationery -> CPJ.",
            "tier_2": "Cash Invoice / EFT -> CPJ -> Dr Stationery, Cr Bank.",
            "tier_3": ans,
        },
        misconception_tags=["records_stationery_in_crj_or_as_equipment"],
        question_family_id="doc_analysis_stationery",
    )


def _b27_doc_capital_contribution_analysis(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    cap = rng.randint(35, 95) * 1000
    prompt = (
        f"{s['entrepreneur']} deposits {fmt_r(cap)} of personal savings into {s['business']}'s bank account as starting Capital. "
        f"Which Source Document and Accounting Equation effect apply?"
    )
    ans = f"Duplicate Receipt / Bank Deposit Slip -> CRJ -> Assets +{fmt_r(cap)}, Owner's Equity +{fmt_r(cap)}"
    opts = [
        f"Duplicate Receipt / Bank Deposit Slip -> CRJ -> Assets +{fmt_r(cap)}, Owner's Equity +{fmt_r(cap)}",
        f"Cheque Counterfoil -> CPJ -> Assets -{fmt_r(cap)}, Owner's Equity -{fmt_r(cap)}",
        f"Cash Register Roll -> CRJ -> Assets +{fmt_r(cap)}, Liabilities +{fmt_r(cap)}",
        f"Cash Invoice -> CPJ -> Assets 0, Owner's Equity +{fmt_r(cap)}",
    ]
    exp = f"Capital ({fmt_r(cap)}) is evidenced by Duplicate Receipt / Stamped Deposit Slip -> CRJ -> Bank (+A) and Capital (+OE)."
    return _make_mcq(
        rng,
        subskill="27_doc_capital_contribution_analysis",
        title="Source Doc Analysis: Capital Contribution",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Cash enters Bank and Capital increases Owner's Equity.",
            "tier_2": "Duplicate Receipt / Deposit Slip -> CRJ -> +A, +OE.",
            "tier_3": ans,
        },
        misconception_tags=["confuses_capital_source_document"],
        question_family_id="doc_analysis_capital",
    )


def _b28_doc_telephone_payment_analysis(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    amt = rng.randint(6, 24) * 100
    prompt = (
        f"{s['business']} settles its monthly business Telephone and Fibre internet bill of {fmt_r(amt)} via EFT. "
        f"Identify the retained Source Document, Journal, and Equation effect."
    )
    ans = f"EFT Proof of Payment / Bank Statement -> CPJ -> Assets -{fmt_r(amt)}, Owner's Equity -{fmt_r(amt)}"
    opts = [
        f"EFT Proof of Payment / Bank Statement -> CPJ -> Assets -{fmt_r(amt)}, Owner's Equity -{fmt_r(amt)}",
        f"Duplicate Receipt -> CRJ -> Assets +{fmt_r(amt)}, Owner's Equity +{fmt_r(amt)}",
        f"Cash Register Roll -> CPJ -> Assets -{fmt_r(amt)}, Liabilities +{fmt_r(amt)}",
        f"Bank Deposit Slip -> CRJ -> Assets 0, Owner's Equity -{fmt_r(amt)}",
    ]
    exp = f"Telephone ({fmt_r(amt)}) paid via EFT creates an EFT Proof / Bank Statement debit -> CPJ -> Bank decreases (-A) and Telephone expense reduces Owner's Equity (-OE)."
    return _make_mcq(
        rng,
        subskill="28_doc_telephone_payment_analysis",
        title="Source Doc Analysis: Telephone Payment",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Telephone is an Operating Expense paid out of Bank.",
            "tier_2": "EFT Proof / Bank Statement -> CPJ -> -A, -OE.",
            "tier_3": ans,
        },
        misconception_tags=["records_telephone_as_liability_increase"],
        question_family_id="doc_analysis_telephone",
    )


def _b29_doc_land_buildings_purchase_analysis(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    amt = rng.randint(350, 750) * 1000
    prompt = (
        f"{s['business']} purchases a commercial workshop property (Land and Buildings) in {s['area']} for {fmt_r(amt)} paid by EFT / bank transfer. "
        f"Which accounting analysis is accurate?"
    )
    ans = f"Transfer Deed / EFT Confirmation -> CPJ -> Land & Buildings (+A {fmt_r(amt)}) and Bank (-A {fmt_r(amt)}), net Assets effect 0"
    opts = [
        f"Transfer Deed / EFT Confirmation -> CPJ -> Land & Buildings (+A {fmt_r(amt)}) and Bank (-A {fmt_r(amt)}), net Assets effect 0",
        f"Cash Register Roll -> CRJ -> Rent Expense (+OE {fmt_r(amt)})",
        f"Duplicate Receipt -> CPJ -> Operating Expense (-OE {fmt_r(amt)})",
        f"Petty Cash Voucher -> CRJ -> Liabilities (+L {fmt_r(amt)})",
    ]
    exp = f"Buying Land & Buildings ({fmt_r(amt)}) cash/EFT swaps cash (Bank -A) for property (Land & Buildings +A) -> CPJ -> Net 0 change in Total Assets and no effect on OE."
    return _make_mcq(
        rng,
        subskill="29_doc_land_buildings_purchase_analysis",
        title="Source Doc Analysis: Land & Buildings Purchase",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Land & Buildings is a Fixed Asset, NOT an Operating Expense.",
            "tier_2": "EFT / Transfer Deed -> CPJ -> +A (Property) and -A (Bank).",
            "tier_3": ans,
        },
        misconception_tags=["treats_property_purchase_as_expense"],
        question_family_id="doc_analysis_land_buildings",
    )


def _b30_doc_current_income_crr_analysis(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    amt = rng.randint(18, 55) * 100
    prompt = (
        f"At closing time in {s['area']}, {s['business']} summarises cash fees received for customer services totalling {fmt_r(amt)}. "
        f"Identify the Source Document, Journal, and Accounting Equation effect."
    )
    ans = f"Cash Register Roll (CRR) / Duplicate Receipt -> CRJ -> Assets +{fmt_r(amt)}, Owner's Equity +{fmt_r(amt)}"
    opts = [
        f"Cash Register Roll (CRR) / Duplicate Receipt -> CRJ -> Assets +{fmt_r(amt)}, Owner's Equity +{fmt_r(amt)}",
        f"Cash Invoice -> CPJ -> Assets -{fmt_r(amt)}, Owner's Equity -{fmt_r(amt)}",
        f"Cheque Counterfoil -> CRJ -> Assets +{fmt_r(amt)}, Liabilities +{fmt_r(amt)}",
        f"Petty Cash Voucher -> CRJ -> Assets 0, Owner's Equity +{fmt_r(amt)}",
    ]
    exp = f"Daily cash service income ({fmt_r(amt)}) is backed by the internal CRR / Duplicate Receipt -> CRJ -> Bank (+A) and Current Income (+OE)."
    return _make_mcq(
        rng,
        subskill="30_doc_current_income_crr_analysis",
        title="Source Doc Analysis: Current Income (CRR)",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Service cash takings go into CRJ using the till tape / receipt book copy.",
            "tier_2": "CRR / Duplicate Receipt -> CRJ -> +A (Bank), +OE (Current Income).",
            "tier_3": ans,
        },
        misconception_tags=["confuses_crr_and_cash_invoice"],
        question_family_id="doc_analysis_current_income",
    )


def _b31_doc_consumable_goods_purchase(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    sup = rng.choice(SUPPLIERS)
    amt = rng.randint(6, 22) * 100
    prompt = (
        f"{s['business']} pays {fmt_r(amt)} cash/EFT to {sup} for Consumable Goods (packaging bags and cleaning detergent used during service work). "
        f"Which Source Document, Journal, and Account Debited are correct?"
    )
    ans = "Cash Invoice / EFT Proof -> CPJ -> Debit Consumable Goods / Stores (Expense)"
    opts = [
        "Cash Invoice / EFT Proof -> CPJ -> Debit Consumable Goods / Stores (Expense)",
        "Duplicate Receipt -> CRJ -> Debit Bank",
        "Cash Register Roll -> CPJ -> Debit Vehicles",
        "Bank Deposit Slip -> CRJ -> Credit Consumable Goods",
    ]
    exp = f"Buying consumable supplies ({fmt_r(amt)}) from {sup} is recorded from Cash Invoice/EFT Proof into CPJ -> Debit Consumable Goods (Expense, -OE), Credit Bank (-A)."
    return _make_mcq(
        rng,
        subskill="31_doc_consumable_goods_purchase",
        title="Source Doc Analysis: Consumable Goods",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Items used up quickly in daily services are Consumable Expenses paid out via CPJ.",
            "tier_2": "Cash Invoice / EFT -> CPJ -> Dr Consumable Goods.",
            "tier_3": ans,
        },
        misconception_tags=["classifies_consumable_goods_as_fixed_asset"],
        question_family_id="doc_analysis_consumables",
    )


def _b32_doc_rent_income_duplicate_receipt(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    tenant = rng.choice(NAMES)
    amt = rng.randint(25, 60) * 100
    prompt = (
        f"{tenant} pays {fmt_r(amt)} to {s['business']} for renting part of the shop floor. "
        f"Which Source Document proves receipt and what is the impact on A = OE + L?"
    )
    ans = f"Duplicate Receipt / Bank Statement -> CRJ -> Assets +{fmt_r(amt)}, Owner's Equity +{fmt_r(amt)}"
    opts = [
        f"Duplicate Receipt / Bank Statement -> CRJ -> Assets +{fmt_r(amt)}, Owner's Equity +{fmt_r(amt)}",
        f"Original Receipt -> CPJ -> Assets -{fmt_r(amt)}, Owner's Equity -{fmt_r(amt)}",
        f"Cheque Counterfoil -> CRJ -> Assets +{fmt_r(amt)}, Liabilities +{fmt_r(amt)}",
        f"Cash Invoice -> CPJ -> Assets 0, Liabilities +{fmt_r(amt)}",
    ]
    exp = f"When {tenant} pays Rent Income ({fmt_r(amt)}), {s['business']} keeps the Duplicate Receipt -> CRJ -> Bank (+A) and Rent Income (+OE)."
    return _make_mcq(
        rng,
        subskill="32_doc_rent_income_duplicate_receipt",
        title="Source Doc Analysis: Rent Income Received",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Who gets the Original Receipt vs Duplicate Receipt when money is received?",
            "tier_2": "Business keeps Duplicate Receipt -> CRJ -> +A (Bank), +OE (Rent Income).",
            "tier_3": ans,
        },
        misconception_tags=["confuses_rent_income_with_rent_expense"],
        question_family_id="doc_analysis_rent_income",
    )


def _b33_doc_cash_float_withdrawal(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    amt = rng.randint(4, 12) * 100
    prompt = (
        f"{s['entrepreneur']} withdraws {fmt_r(amt)} from the business bank account to place small coins and notes in the shop till as a Cash Float. "
        f"How does this Cash Float entry affect Total Assets?"
    )
    ans = f"Cash Float (Asset) increases +{fmt_r(amt)} and Bank (Asset) decreases -{fmt_r(amt)} (net effect 0, recorded in CPJ)"
    opts = [
        f"Cash Float (Asset) increases +{fmt_r(amt)} and Bank (Asset) decreases -{fmt_r(amt)} (net effect 0, recorded in CPJ)",
        f"Assets decrease -{fmt_r(amt)} and Owner's Equity decreases -{fmt_r(amt)} (Operating Expense)",
        f"Cash Float increases Owner's Equity +{fmt_r(amt)} (recorded in CRJ)",
        f"Assets decrease -{fmt_r(amt)} and Liabilities increase +{fmt_r(amt)}",
    ]
    exp = f"Withdrawing {fmt_r(amt)} from Bank for Cash Float shifts money from one Current Asset (Bank -) to another Current Asset (Cash Float +) via CPJ -> Net 0 change to Assets and OE."
    return _make_mcq(
        rng,
        subskill="33_doc_cash_float_withdrawal",
        title="Source Doc & Equation: Cash Float",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Notice Cash Float is still cash owned by the business inside the shop till!",
            "tier_2": "Bank leaves the bank account (CPJ, -A) into Cash Float (+A) -> Net 0 Assets.",
            "tier_3": ans,
        },
        misconception_tags=["treats_cash_float_as_expense_or_drawings"],
        question_family_id="doc_analysis_cash_float",
    )


def _b34_doc_owner_drawings_cash_slip(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    amt = rng.randint(8, 30) * 100
    prompt = (
        f"{s['entrepreneur']} transfers {fmt_r(amt)} from {s['business']}'s bank account to buy personal household furniture. "
        f"Which Source Document, Journal, and Equation impact apply?"
    )
    ans = f"EFT Confirmation / Withdrawal Slip -> CPJ -> Assets -{fmt_r(amt)}, Owner's Equity -{fmt_r(amt)} (Drawings)"
    opts = [
        f"EFT Confirmation / Withdrawal Slip -> CPJ -> Assets -{fmt_r(amt)}, Owner's Equity -{fmt_r(amt)} (Drawings)",
        f"Duplicate Receipt -> CRJ -> Assets +{fmt_r(amt)}, Owner's Equity +{fmt_r(amt)}",
        f"Cash Invoice -> CPJ -> Assets +{fmt_r(amt)} / -{fmt_r(amt)} (Equipment)",
        f"Bank Deposit Slip -> CPJ -> Liabilities -{fmt_r(amt)}",
    ]
    exp = f"Personal furniture paid from business funds ({fmt_r(amt)}) is Drawings -> EFT/Withdrawal confirmation -> CPJ -> Bank (-A) and Drawings (-OE)."
    return _make_mcq(
        rng,
        subskill="34_doc_owner_drawings_cash_slip",
        title="Source Doc Analysis: Owner Drawings",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Personal purchases using business bank funds are Drawings, not Equipment.",
            "tier_2": "EFT / Withdrawal slip -> CPJ -> -A (Bank), -OE (Drawings).",
            "tier_3": ans,
        },
        misconception_tags=["classifies_personal_furniture_as_business_equipment"],
        question_family_id="doc_analysis_drawings",
    )


def _b35_doc_water_electricity_municipal(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    amt = rng.randint(12, 38) * 100
    prompt = (
        f"{s['business']} in {s['area']} pays the municipality {fmt_r(amt)} via EFT for the monthly Water and Electricity account. "
        f"Identify the Source Document, Journal, and General Ledger accounts."
    )
    ans = "EFT Proof of Payment / Municipal Receipt -> CPJ -> Debit Water & Electricity, Credit Bank"
    opts = [
        "EFT Proof of Payment / Municipal Receipt -> CPJ -> Debit Water & Electricity, Credit Bank",
        "Cash Register Roll -> CRJ -> Debit Bank, Credit Water & Electricity",
        "Bank Deposit Slip -> CRJ -> Debit Water & Electricity, Credit Capital",
        "Duplicate Receipt -> CPJ -> Debit Bank, Credit Creditors Control",
    ]
    exp = f"Municipal utility payment ({fmt_r(amt)}) creates an EFT Proof / Receipt -> CPJ -> Dr Water & Electricity (Expense, -OE), Cr Bank (-A)."
    return _make_mcq(
        rng,
        subskill="35_doc_water_electricity_municipal",
        title="Source Doc Analysis: Water & Electricity",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Municipal utilities are Operating Expenses paid out of Bank.",
            "tier_2": "EFT Proof -> CPJ -> Dr Water & Electricity, Cr Bank.",
            "tier_3": ans,
        },
        misconception_tags=["reverses_utility_expense_dr_cr"],
        question_family_id="doc_analysis_utilities",
    )


def _b36_equation_with_source_doc_table_1(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    cap = rng.randint(40, 80) * 1000
    stat = rng.randint(4, 15) * 100
    inc = rng.randint(12, 35) * 100
    flt = rng.randint(3, 9) * 100
    headers = ["Transaction", "Source Document", "Journal", "Assets (A)", "Owner's Equity (OE)"]
    table_rows = [
        [(f"Owner invests {fmt_r(cap)} Capital.", "given", False), ("Duplicate Receipt", "required", True), ("CRJ", "required", True), (f"+{fmt_r(cap)}", "required", True), (f"+{fmt_r(cap)}", "required", True)],
        [(f"Bought Stationery cash, {fmt_r(stat)}.", "given", False), ("Cash Invoice / EFT", "required", True), ("CPJ", "required", True), (f"-{fmt_r(stat)}", "required", True), (f"-{fmt_r(stat)}", "required", True)],
        [(f"Cash services rendered, {fmt_r(inc)}.", "given", False), ("Cash Register Roll", "required", True), ("CRJ", "required", True), (f"+{fmt_r(inc)}", "required", True), (f"+{fmt_r(inc)}", "required", True)],
        [(f"Established Cash Float, {fmt_r(flt)}.", "given", False), ("Withdrawal Slip / Counterfoil", "required", True), ("CPJ", "required", True), ("0", "required", True), ("0", "required", True)],
    ]
    cell_hints = {
        "t0_r0_c1": "Duplicate Receipt issued to owner.",
        "t0_r0_c2": "CRJ",
        "t0_r0_c3": f"+{fmt_r(cap)}",
        "t0_r0_c4": f"+{fmt_r(cap)}",
        "t0_r1_c1": "Cash Invoice / EFT",
        "t0_r1_c2": "CPJ",
        "t0_r1_c3": f"-{fmt_r(stat)}",
        "t0_r1_c4": f"-{fmt_r(stat)}",
        "t0_r2_c1": "Cash Register Roll",
        "t0_r2_c2": "CRJ",
        "t0_r2_c3": f"+{fmt_r(inc)}",
        "t0_r2_c4": f"+{fmt_r(inc)}",
        "t0_r3_c1": "Withdrawal Slip / Counterfoil",
        "t0_r3_c2": "CPJ",
        "t0_r3_c3": f"Cash Float +{fmt_r(flt)} & Bank -{fmt_r(flt)} -> Net 0.",
        "t0_r3_c4": "0 (asset swap only).",
    }
    prompt = f"Complete the Source Document & Accounting Equation table below for {s['business']} in {s['area']}."
    return _make_table(
        rng,
        subskill="36_equation_with_source_doc_table_1",
        title="Source Docs & Equation Drill (Set 1)",
        prompt=prompt,
        journal_type="doc_equation_set1",
        headers=headers,
        table_rows=table_rows,
        cell_hints=cell_hints,
        hints={
            "tier_1": "Determine Source Document and Journal first, then track Assets & OE signs (+ / - / 0).",
            "tier_2": "Remember Cash Float swaps one Asset (Bank) for another (Cash Float) -> Net Assets 0, OE 0.",
            "tier_3": f"Row 4 Cash Float: Assets=0, OE=0 (CPJ).",
        },
        misconception_tags=["misses_net_zero_assets_on_cash_float"],
        question_family_id="doc_eq_table_1",
    )


def _b37_equation_with_source_doc_table_2(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    cons = rng.randint(5, 16) * 100
    rent = rng.randint(25, 55) * 100
    draw = rng.randint(7, 20) * 100
    elec = rng.randint(12, 28) * 100
    headers = ["Transaction", "Source Document", "Journal", "Assets (A)", "Owner's Equity (OE)"]
    table_rows = [
        [(f"Bought Consumable Goods cash, {fmt_r(cons)}.", "given", False), ("Cash Invoice / EFT", "required", True), ("CPJ", "required", True), (f"-{fmt_r(cons)}", "required", True), (f"-{fmt_r(cons)}", "required", True)],
        [(f"Received Rent Income EFT, {fmt_r(rent)}.", "given", False), ("Duplicate Receipt / Bank Statement", "required", True), ("CRJ", "required", True), (f"+{fmt_r(rent)}", "required", True), (f"+{fmt_r(rent)}", "required", True)],
        [(f"Owner Drawings in cash, {fmt_r(draw)}.", "given", False), ("EFT / Withdrawal Slip", "required", True), ("CPJ", "required", True), (f"-{fmt_r(draw)}", "required", True), (f"-{fmt_r(draw)}", "required", True)],
        [(f"Paid Water & Electricity EFT, {fmt_r(elec)}.", "given", False), ("EFT Proof of Payment", "required", True), ("CPJ", "required", True), (f"-{fmt_r(elec)}", "required", True), (f"-{fmt_r(elec)}", "required", True)],
    ]
    cell_hints = {
        "t0_r0_c1": "Cash Invoice / EFT",
        "t0_r0_c2": "CPJ",
        "t0_r0_c3": f"-{fmt_r(cons)}",
        "t0_r0_c4": f"-{fmt_r(cons)}",
        "t0_r1_c1": "Duplicate Receipt / Bank Statement",
        "t0_r1_c2": "CRJ",
        "t0_r1_c3": f"+{fmt_r(rent)}",
        "t0_r1_c4": f"+{fmt_r(rent)}",
        "t0_r2_c1": "EFT / Withdrawal Slip",
        "t0_r2_c2": "CPJ",
        "t0_r2_c3": f"-{fmt_r(draw)}",
        "t0_r2_c4": f"-{fmt_r(draw)}",
        "t0_r3_c1": "EFT Proof of Payment",
        "t0_r3_c2": "CPJ",
        "t0_r3_c3": f"-{fmt_r(elec)}",
        "t0_r3_c4": f"-{fmt_r(elec)}",
    }
    prompt = f"Complete the Source Document & Equation analysis table below for {s['business']}."
    return _make_table(
        rng,
        subskill="37_equation_with_source_doc_table_2",
        title="Source Docs & Equation Drill (Set 2)",
        prompt=prompt,
        journal_type="doc_equation_set2",
        headers=headers,
        table_rows=table_rows,
        cell_hints=cell_hints,
        hints={
            "tier_1": "Income (Rent Income) increases both A and OE; Expenses and Drawings decrease both A and OE.",
            "tier_2": "Verify CRJ rows carry '+' and CPJ expense/drawings rows carry '-'.",
            "tier_3": f"Rent Income (+{fmt_r(rent)}) is CRJ; Consumables, Drawings, Utilities are CPJ (-).",
        },
        misconception_tags=["gives_positive_sign_to_expense_or_drawings"],
        question_family_id="doc_eq_table_2",
    )


def _b38_visual_bank_reconcile_deposit_discrepancy(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    bank = rng.choice(_BANKS)
    crr_tot = rng.randint(45, 95) * 100
    banked = crr_tot - rng.randint(3, 12) * 100
    shortfall = crr_tot - banked
    ans = fmt_r(shortfall)
    svg = svg_doc_plate(
        f"AUDIT CROSS-CHECK — {s['business']}",
        f"{bank} Banking Verification",
        [
            ("Cash Register Roll (CRR) Daily Total", fmt_r(crr_tot)),
            ("Stamped Deposit Slip (Cash Banked)", fmt_r(banked)),
            ("Unexplained Cash Shortfall", "R ???"),
        ],
        footer="AUDIT ALERT: COMPARE INTERNAL TILL TAPE WITH BANK PROOF",
    )
    prompt = (
        f"During an internal audit at {s['business']}, compare the Cash Register Roll total against the {bank}-stamped Duplicate Deposit Slip. "
        f"Calculate the Unexplained Cash Shortfall (`R ???`) that must be investigated immediately."
    )
    steps = [
        f"Expected cash from CRR = {fmt_r(crr_tot)}; Actual banked on Deposit Slip = {fmt_r(banked)}.",
        f"Unexplained Cash Shortfall = {fmt_r(crr_tot)} - {fmt_r(banked)} = {ans}.",
    ]
    return _make_typed(
        rng,
        subskill="38_visual_bank_reconcile_deposit_discrepancy",
        title="Detect Cash Deposit Discrepancy",
        prompt=prompt,
        correct_ans=ans,
        acceptable_answers=[ans, f"R{shortfall}", str(shortfall)],
        steps=steps,
        hints={
            "tier_1": "Subtract actual cash deposited from total cash recorded on the CRR.",
            "tier_2": f"{fmt_r(crr_tot)} - {fmt_r(banked)}.",
            "tier_3": f"Cash shortfall = {ans}.",
        },
        misconception_tags=["misses_deposit_discrepancy_audit"],
        question_family_id="visual_deposit_audit",
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    )


def _b39_visual_cheque_error_identification(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    bank = rng.choice(_BANKS)
    chq_no = rng.randint(601, 899)
    amt_fig = rng.randint(15, 45) * 100
    amt_words_diff = amt_fig + 500
    defect_type = rng.choice(["words_figures", "unsigned"])
    if defect_type == "words_figures":
        fields = [
            ("Pay", rng.choice(SUPPLIERS)),
            ("Sum in Words", f"{amt_words_diff} Rand Only"),
            ("Sum in Figures", fmt_r(amt_fig)),
            ("Drawer Signature", s["entrepreneur"]),
        ]
        ans = f"The amount in words ({amt_words_diff}) does not match the amount in figures ({fmt_r(amt_fig)})"
    else:
        fields = [
            ("Pay", rng.choice(SUPPLIERS)),
            ("Sum in Figures", fmt_r(amt_fig)),
            ("Drawer Signature", "[BLANK — UNSIGNED]"),
        ]
        ans = "The drawer did not sign the cheque, making the payment instruction legally invalid"

    svg = svg_doc_plate(
        f"{bank} — SPECIMEN CHEQUE",
        f"Cheque #{chq_no}",
        fields,
        footer="BANK CLEARANCE CHECK REQUIRED",
    )
    prompt = f"Inspect Cheque #{chq_no} drawn on {s['business']}'s {bank} account. Why will {bank} refuse to honour this cheque?"
    opts = [
        ans,
        "Because crossed cheques can never be paid into a supplier's bank account",
        "Because every business cheque must exceed R10 000",
        "Because cheques are entered into the Cash Receipts Journal",
    ]
    exp = f"On Cheque #{chq_no}, {ans.lower()}, so {bank} will return/reject the instrument."
    return _make_mcq(
        rng,
        subskill="39_visual_cheque_error_identification",
        title="Spot the Defect on a Cheque",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Check every mandatory field on the cheque carefully: words, figures, and signature.",
            "tier_2": "A valid cheque requires matching words and figures AND the drawer's signature.",
            "tier_3": ans,
        },
        misconception_tags=["misses_invalid_cheque_defects"],
        question_family_id="visual_cheque_defect",
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    )


def _b40_sequential_doc_numbering_fraud_check(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    start_no = rng.randint(410, 480)
    missing = start_no + 2
    prompt = (
        f"While auditing {s['business']}'s pre-numbered Duplicate Receipt Book in {s['area']}, the bookkeeper sees Receipt #{start_no}, #{start_no + 1}, "
        f"and #{start_no + 3}, but Receipt #{missing} has been torn out completely (both original and duplicate are gone). "
        f"Explain TWO risks this poses and state the proper procedure if a clerk makes a mistake on a receipt."
    )
    sample = (
        f"1. Risk of cash skimming / fraud: A clerk could collect cash using Original #{missing} and destroy Duplicate #{missing} to hide the theft from CRJ.\n"
        f"2. Proper mistake procedure: NEVER tear out the duplicate copy! Write 'CANCELLED' diagonally across BOTH the original and duplicate and staple/leave both inside the book for audit verification."
    )
    pts = [
        f"Identifies theft/skimming risk when duplicate receipt #{missing} is missing from CRJ audit trail.",
        "States correct rule: write 'CANCELLED' across both original and duplicate and keep BOTH inside the receipt book.",
    ]
    return _make_rubric(
        rng,
        subskill="40_sequential_doc_numbering_fraud_check",
        title="Sequential Numbering & Spoilt Receipt Control",
        prompt=prompt,
        sample_answer=sample,
        marking_points=pts,
        hints={
            "tier_1": "Why are receipt books pre-numbered in strict sequence?",
            "tier_2": "Mention cash theft/skimming risk AND leaving spoilt receipts stamped 'CANCELLED' inside the book.",
            "tier_3": sample,
        },
        misconception_tags=["thinks_spoilt_receipts_should_be_thrown_away"],
        question_family_id="sequential_numbering_rubric",
        marks=2,
    )


def _b41_cash_vs_credit_source_doc_contrast(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    sup = rng.choice(SUPPLIERS)
    amt = rng.randint(3, 12) * 1000
    prompt = (
        f"{s['business']} buys stock worth {fmt_r(amt)} from {sup} on 30 days' credit rather than paying today. "
        f"How does the source document received differ from a Cash Purchase?"
    )
    ans = "A Credit Invoice is received (recording a Creditor liability) rather than a Cash Invoice / EFT Proof"
    opts = [
        "A Credit Invoice is received (recording a Creditor liability) rather than a Cash Invoice / EFT Proof",
        "A Cash Register Roll is issued to record immediate cash outflow in CPJ",
        "A Stamped Bank Deposit Slip proves the business received a cash loan",
        "No invoice is issued until the 30 days expire",
    ]
    exp = f"Buying on 30-day credit from {sup} ({fmt_r(amt)}) generates an Original Credit Invoice (deferred liability), whereas an immediate payment uses a Cash Invoice / EFT Proof."
    return _make_mcq(
        rng,
        subskill="41_cash_vs_credit_source_doc_contrast",
        title="Cash vs Credit Purchase Source Documents",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Match immediate payment vs 30-day credit payment to invoice type.",
            "tier_2": "Credit purchases use an Original Credit Invoice; immediate cash/EFT uses a Cash Invoice / EFT Proof.",
            "tier_3": ans,
        },
        misconception_tags=["confuses_cash_invoice_and_credit_invoice"],
        question_family_id="cash_vs_credit_doc",
    )


def _b42_source_doc_retention_five_year_rule(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    year = rng.choice([2025, 2026])
    prompt = (
        f"Why must {s['business']} file and preserve all {year} Duplicate Receipts, Invoices, EFT Confirmations, and Bank Statements neatly in chronological order for at least 5 years?"
    )
    sample = (
        f"1. Legal SARS Compliance: South African tax law requires businesses to keep source documents for at least 5 years to prove income and deductible expenses during SARS audits.\n"
        f"2. Dispute Resolution & Financial Tracking: Chronological filing makes it quick to resolve customer/supplier payment disputes and verify Warranty or Bank Statement queries."
    )
    pts = [
        "Mandatory 5-year legal retention period for SARS tax/VAT audit verification.",
        "Supports resolving supplier/customer disputes, warranties, and bank reconciliations.",
    ]
    return _make_rubric(
        rng,
        subskill="42_source_doc_retention_five_year_rule",
        title="5-Year Source Document Filing & Legal Retention",
        prompt=prompt,
        sample_answer=sample,
        marking_points=pts,
        hints={
            "tier_1": "Think about tax inspections and resolving future disputes.",
            "tier_2": "Include SARS 5-year audit retention law and settling payment/warranty disputes.",
            "tier_3": sample,
        },
        misconception_tags=["discards_old_source_documents_prematurely"],
        question_family_id="retention_5_year_rule",
        marks=2,
    )


def _b43_till_roll_vs_bank_deposit_verification(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    crr = rng.randint(55, 110) * 100
    petty_topup = rng.randint(3, 9) * 100
    bank_dep = crr - petty_topup
    ans = fmt_r(bank_dep)
    prompt = (
        f"At closing time for {s['business']}, the Cash Register Roll shows total cash takings of {fmt_r(crr)}. "
        f"{s['entrepreneur']} authorises setting aside {fmt_r(petty_topup)} (with a signed voucher) to replenish Petty Cash and banks the remaining cash. "
        f"What exact amount must appear on the Stamped Bank Deposit Slip?"
    )
    steps = [
        f"Total till cash on CRR = {fmt_r(crr)}.",
        f"Cash retained with voucher for Petty Cash = {fmt_r(petty_topup)}.",
        f"Cash banked on Deposit Slip = {fmt_r(crr)} - {fmt_r(petty_topup)} = {ans}.",
    ]
    return _make_typed(
        rng,
        subskill="43_till_roll_vs_bank_deposit_verification",
        title="Verify Cash Banked vs CRR Total",
        prompt=prompt,
        correct_ans=ans,
        acceptable_answers=[ans, f"R{bank_dep}", str(bank_dep)],
        steps=steps,
        hints={
            "tier_1": "Subtract the authorised Petty Cash replenishment from the day's CRR total.",
            "tier_2": f"{fmt_r(crr)} - {fmt_r(petty_topup)}.",
            "tier_3": f"Deposit Slip amount = {ans}.",
        },
        misconception_tags=["adds_petty_cash_to_bank_deposit"],
        question_family_id="crr_deposit_verification",
    )


def _b44_identify_wrong_source_doc_error(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    sup = rng.choice(SUPPLIERS)
    amt = rng.randint(15, 55) * 100
    prompt = (
        f"A trainee bookkeeper at {s['business']} takes a **Price Quotation** for {fmt_r(amt)} emailed by {sup} and enters it as an expense in the CPJ, "
        f"even though {s['business']} has NOT bought the goods or paid yet. Why is this an error?"
    )
    ans = "A Price Quotation is NOT a valid source document because no actual purchase or payment occurred yet"
    opts = [
        "A Price Quotation is NOT a valid source document because no actual purchase or payment occurred yet",
        "Because Price Quotations must be entered in the CRJ instead of CPJ",
        "Because only hand-written cheques count as source documents",
        f"Because {sup} invoices should enter the Trial Balance directly",
    ]
    exp = f"A Price Quotation from {sup} ({fmt_r(amt)}) only states an offer price — no transaction occurred! Only a Cash Invoice, EFT Proof, or Credit Invoice after purchase is a source document."
    return _make_mcq(
        rng,
        subskill="44_identify_wrong_source_doc_error",
        title="Invalid Source Document Error (Price Quotation)",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Did any money, goods, or debt actually change hands on a Price Quotation?",
            "tier_2": "Quotations are pre-transaction offers, not valid proof of payment or purchase.",
            "tier_3": ans,
        },
        misconception_tags=["treats_quotation_as_valid_source_document"],
        question_family_id="invalid_source_doc_error",
    )


def _b45_visual_eft_vs_bank_charges_table(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    c_in = rng.randint(25, 65) * 100
    s_out = rng.randint(12, 35) * 100
    chg = rng.randint(15, 35) * 10
    intr = rng.randint(10, 25) * 10
    headers = ["Bank Statement Entry", "Bookkeeping Category / Account", "Journal (CRJ / CPJ)", "Bank Effect (+ / -)"]
    table_rows = [
        [(f"EFT Deposit from Client, {fmt_r(c_in)}", "given", False), ("Current Income", "required", True), ("CRJ", "required", True), ("+", "required", True)],
        [(f"EFT Payment for Stationery, {fmt_r(s_out)}", "given", False), ("Stationery", "required", True), ("CPJ", "required", True), ("-", "required", True)],
        [(f"Monthly Service Fees, {fmt_r(chg)}", "given", False), ("Bank Charges", "required", True), ("CPJ", "required", True), ("-", "required", True)],
        [(f"Credit Interest Earned, {fmt_r(intr)}", "given", False), ("Interest Received", "required", True), ("CRJ", "required", True), ("+", "required", True)],
    ]
    cell_hints = {
        "t0_r0_c1": "Current Income",
        "t0_r0_c2": "CRJ",
        "t0_r0_c3": "+",
        "t0_r1_c1": "Stationery",
        "t0_r1_c2": "CPJ",
        "t0_r1_c3": "-",
        "t0_r2_c1": "Bank Charges",
        "t0_r2_c2": "CPJ",
        "t0_r2_c3": "-",
        "t0_r3_c1": "Interest Received",
        "t0_r3_c2": "CRJ",
        "t0_r3_c3": "+",
    }
    prompt = f"Reconcile each Bank Statement entry for {s['business']} into its exact Account Name, Journal (`CRJ` or `CPJ`), and Bank Effect (`+` or `-`)."
    return _make_table(
        rng,
        subskill="45_visual_eft_vs_bank_charges_table",
        title="Bank Statement Reconciling Table",
        prompt=prompt,
        journal_type="bank_stmt_reconcile",
        headers=headers,
        table_rows=table_rows,
        cell_hints=cell_hints,
        hints={
            "tier_1": "Fees charged by the bank reduce Bank (-, CPJ); interest earned increases Bank (+, CRJ).",
            "tier_2": "Use Current Income, Stationery, Bank Charges, and Interest Received.",
            "tier_3": "1: Current Income / CRJ / + | 2: Stationery / CPJ / - | 3: Bank Charges / CPJ / - | 4: Interest Received / CRJ / +.",
        },
        misconception_tags=["reverses_bank_charges_and_interest_journals"],
        question_family_id="bank_stmt_table",
    )


def _b46_scenario_multi_doc_crj_total(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    rec = rng.randint(15, 40) * 1000
    crr = rng.randint(4, 15) * 1000
    inv = rng.randint(2, 6) * 1000
    eft_out = rng.randint(1, 5) * 1000
    crj_tot = rec + crr
    ans = fmt_r(crj_tot)
    prompt = (
        f"During Week 1, {s['business']} has four source documents on file: "
        f"(1) Duplicate Receipt #101 for Capital {fmt_r(rec)}, "
        f"(2) Cash Register Roll Z-total for services {fmt_r(crr)}, "
        f"(3) Cash Invoice paid for supplies {fmt_r(inv)}, and "
        f"(4) EFT Proof for wages paid {fmt_r(eft_out)}. "
        f"Calculate the TOTAL cash received entered in the CRJ (exclude CPJ payments)."
    )
    steps = [
        f"Identify CRJ source documents (cash inflows): Duplicate Receipt ({fmt_r(rec)}) and CRR ({fmt_r(crr)}).",
        f"Exclude CPJ cash outflows: Cash Invoice ({fmt_r(inv)}) and Wages EFT ({fmt_r(eft_out)}).",
        f"Total CRJ Receipts = {fmt_r(rec)} + {fmt_r(crr)} = {ans}.",
    ]
    return _make_typed(
        rng,
        subskill="46_scenario_multi_doc_crj_total",
        title="Extract Total CRJ Receipts from Mixed Documents",
        prompt=prompt,
        correct_ans=ans,
        acceptable_answers=[ans, f"R{crj_tot}", str(crj_tot)],
        steps=steps,
        hints={
            "tier_1": "Filter ONLY documents showing money coming INTO the business.",
            "tier_2": "Add Duplicate Receipt + CRR only (leave out Cash Invoice and Wages EFT).",
            "tier_3": f"Total CRJ Receipts = {ans}.",
        },
        misconception_tags=["includes_cpj_payments_in_crj_total"],
        question_family_id="multi_doc_crj_total",
    )


def _b47_scenario_multi_doc_cpj_total(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    crr = rng.randint(6, 18) * 1000
    inv = rng.randint(2, 7) * 1000
    eft = rng.randint(1, 5) * 1000
    chg = rng.randint(2, 6) * 100
    cpj_tot = inv + eft + chg
    ans = fmt_r(cpj_tot)
    prompt = (
        f"Review these source documents from {s['business']}: "
        f"(1) Cash Register Roll for daily sales {fmt_r(crr)}, "
        f"(2) Paid Cash Invoice for Stationery {fmt_r(inv)}, "
        f"(3) EFT Proof for Telephone {fmt_r(eft)}, and "
        f"(4) Bank Statement Bank Charges {fmt_r(chg)}. "
        f"Calculate the TOTAL cash paid entered in the CPJ."
    )
    steps = [
        f"Identify CPJ outflows: Cash Invoice ({fmt_r(inv)}) + EFT Proof ({fmt_r(eft)}) + Bank Charges ({fmt_r(chg)}).",
        f"Exclude CRR ({fmt_r(crr)}, which belongs in CRJ).",
        f"Total CPJ Payments = {fmt_r(inv)} + {fmt_r(eft)} + {fmt_r(chg)} = {ans}.",
    ]
    return _make_typed(
        rng,
        subskill="47_scenario_multi_doc_cpj_total",
        title="Extract Total CPJ Payments from Mixed Documents",
        prompt=prompt,
        correct_ans=ans,
        acceptable_answers=[ans, f"R{cpj_tot}", str(cpj_tot)],
        steps=steps,
        hints={
            "tier_1": "Remember Bank Charges on a Bank Statement count as a CPJ cash outflow.",
            "tier_2": "Sum Cash Invoice + EFT Proof + Bank Charges (ignore CRR).",
            "tier_3": f"Total CPJ Payments = {ans}.",
        },
        misconception_tags=["omits_bank_charges_or_includes_crr_in_cpj"],
        question_family_id="multi_doc_cpj_total",
    )


def _b48_digital_vs_paper_source_docs_modern(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    fee_save = rng.randint(25, 65)
    prompt = (
        f"{s['business']} switches from paper cheques to digital EFT confirmations and electronic point-of-sale slips, "
        f"saving around {fee_save}% in banking processing fees. State TWO bookkeeping advantages and ONE security precaution when handling digital source documents."
    )
    sample = (
        f"Advantages: (1) Instant digital time-stamped proof cuts paper filing errors and lowers transaction fees by ~{fee_save}%; (2) Easy cloud backup preserves the 5-year SARS audit trail against fire or water damage.\n"
        "Security precaution: Protect banking logins with two-factor authentication and verify beneficiary bank details before releasing EFT funds to avoid fraud."
    )
    pts = [
        "Advantage 1: Faster digital processing / lower bank fees and reduced lost-slip risk.",
        "Advantage 2: Electronic backups preserve 5-year tax/audit trails cleanly.",
        "Security precaution: Two-factor authentication / verify beneficiary details before authorising EFTs.",
    ]
    return _make_rubric(
        rng,
        subskill="48_digital_vs_paper_source_docs_modern",
        title="Digital vs Paper Source Documents",
        prompt=prompt,
        sample_answer=sample,
        marking_points=pts,
        hints={
            "tier_1": "Consider speed, backups against fire/loss, and online security against EFT scams.",
            "tier_2": "Give two practical efficiency/audit benefits plus one cybersecurity/verification safeguard.",
            "tier_3": sample,
        },
        misconception_tags=["assumes_digital_docs_need_no_backup_or_control"],
        question_family_id="digital_source_docs_rubric",
        marks=3,
    )


def _b49_case_study_missing_source_docs_audit(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    amt = rng.randint(3, 12) * 1000
    prompt = (
        f"Over three months, {s['entrepreneur']} paid casual cleaners and emergency van repairs totalling {fmt_r(amt)} straight out of the shop till without collecting invoices or writing Petty Cash Vouchers. "
        f"Explain THREE specific consequences for {s['business']}'s accounting, cash control, and tax position."
    )
    sample = (
        f"1. Accounting violation ('No source document, no entry'): The {fmt_r(amt)} expenses cannot be verified in CPJ or Petty Cash, overstating Net Profit artificially.\n"
        f"2. Cash control / theft blindness: {s['entrepreneur']} cannot distinguish genuine till payouts from employee cash theft.\n"
        f"3. Higher SARS tax bill: Without valid receipts/vouchers, SARS disallows the {fmt_r(amt)} business expense deduction."
    )
    pts = [
        "Violates 'no source document, no entry', distorting true expenses and Net Profit.",
        "Prevents distinguishing genuine payouts from cash theft/skimming.",
        f"SARS may disallow the undocumented {fmt_r(amt)} expense deduction during tax assessment.",
    ]
    return _make_rubric(
        rng,
        subskill="49_case_study_missing_source_docs_audit",
        title="Case Study: Unrecorded Till Payouts Audit",
        prompt=prompt,
        sample_answer=sample,
        marking_points=pts,
        hints={
            "tier_1": "Examine what happens to Profit accuracy, theft detection, and SARS tax deductions.",
            "tier_2": "Cover book accuracy, fraud risk, and disallowed tax deductions.",
            "tier_3": sample,
        },
        misconception_tags=["underestimates_consequences_of_missing_receipts"],
        question_family_id="missing_docs_case_study",
        marks=3,
    )


def _b50_comprehensive_source_doc_capstone(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    cap_in = rng.randint(15, 35) * 1000
    crr_in = rng.randint(4, 12) * 1000
    eft_out = rng.randint(3, 8) * 1000
    chg_out = rng.randint(2, 5) * 100
    net_bank = cap_in + crr_in - eft_out - chg_out
    svg = svg_doc_plate(
        f"WEEKLY DOCUMENT BUNDLE — {s['business']}",
        f"Owner: {s['entrepreneur']}",
        [
            ("Duplicate Receipt #301 (Capital)", fmt_r(cap_in)),
            ("Cash Register Roll #18 (Current Income)", fmt_r(crr_in)),
            ("EFT Proof #882 (Equipment bought)", fmt_r(eft_out)),
            ("Bank Statement Debit (Bank Charges)", fmt_r(chg_out)),
        ],
        footer="AUDIT CHECK: CLASSIFY INTO CRJ/CPJ & COMPUTE NET BANK CHANGE",
    )
    prompt = (
        f"Examine the Weekly Document Bundle for {s['business']}. "
        f"(a) Identify which two documents enter the CRJ and which two enter the CPJ. "
        f"(b) Calculate the Net Change in Bank for the week. "
        f"(c) Explain why Duplicate Receipt #301 (and not the Original) is kept inside {s['business']}'s file."
    )
    sample = (
        f"(a) CRJ: Duplicate Receipt #301 ({fmt_r(cap_in)}) and CRR #18 ({fmt_r(crr_in)}). CPJ: EFT Proof #882 ({fmt_r(eft_out)}) and Bank Statement Bank Charges ({fmt_r(chg_out)}).\n"
        f"(b) Net Change in Bank = ({fmt_r(cap_in)} + {fmt_r(crr_in)}) - ({fmt_r(eft_out)} + {fmt_r(chg_out)}) = +{fmt_r(net_bank)}.\n"
        "(c) The Original Receipt is given to the payer as proof of payment, while the bound Duplicate Receipt remains inside the business book for CRJ entry and auditing."
    )
    pts = [
        "Correctly splits documents into CRJ (Duplicate Receipt, CRR) and CPJ (EFT Proof, Bank Charges).",
        f"Calculates Net Bank Change accurately as +{fmt_r(net_bank)}.",
        "Explains payer keeps Original Receipt while business keeps Duplicate for audit/CRJ.",
    ]
    return _make_rubric(
        rng,
        subskill="50_comprehensive_source_doc_capstone",
        title="Source Documents Comprehensive Audit Capstone",
        prompt=prompt,
        sample_answer=sample,
        marking_points=pts,
        hints={
            "tier_1": "Sort inflows (CRJ) vs outflows (CPJ), compute (Inflows - Outflows), and state Original vs Duplicate.",
            "tier_2": f"Inflows = {fmt_r(cap_in + crr_in)}; Outflows = {fmt_r(eft_out + chg_out)}.",
            "tier_3": sample,
        },
        misconception_tags=["misroutes_source_docs_or_miscalculates_net_bank"],
        question_family_id="source_doc_capstone",
        marks=4,
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    )


ARCHETYPES_26_50 = {
    "26_doc_stationery_purchase_analysis": _b26_doc_stationery_purchase_analysis,
    "27_doc_capital_contribution_analysis": _b27_doc_capital_contribution_analysis,
    "28_doc_telephone_payment_analysis": _b28_doc_telephone_payment_analysis,
    "29_doc_land_buildings_purchase_analysis": _b29_doc_land_buildings_purchase_analysis,
    "30_doc_current_income_crr_analysis": _b30_doc_current_income_crr_analysis,
    "31_doc_consumable_goods_purchase": _b31_doc_consumable_goods_purchase,
    "32_doc_rent_income_duplicate_receipt": _b32_doc_rent_income_duplicate_receipt,
    "33_doc_cash_float_withdrawal": _b33_doc_cash_float_withdrawal,
    "34_doc_owner_drawings_cash_slip": _b34_doc_owner_drawings_cash_slip,
    "35_doc_water_electricity_municipal": _b35_doc_water_electricity_municipal,
    "36_equation_with_source_doc_table_1": _b36_equation_with_source_doc_table_1,
    "37_equation_with_source_doc_table_2": _b37_equation_with_source_doc_table_2,
    "38_visual_bank_reconcile_deposit_discrepancy": _b38_visual_bank_reconcile_deposit_discrepancy,
    "39_visual_cheque_error_identification": _b39_visual_cheque_error_identification,
    "40_sequential_doc_numbering_fraud_check": _b40_sequential_doc_numbering_fraud_check,
    "41_cash_vs_credit_source_doc_contrast": _b41_cash_vs_credit_source_doc_contrast,
    "42_source_doc_retention_five_year_rule": _b42_source_doc_retention_five_year_rule,
    "43_till_roll_vs_bank_deposit_verification": _b43_till_roll_vs_bank_deposit_verification,
    "44_identify_wrong_source_doc_error": _b44_identify_wrong_source_doc_error,
    "45_visual_eft_vs_bank_charges_table": _b45_visual_eft_vs_bank_charges_table,
    "46_scenario_multi_doc_crj_total": _b46_scenario_multi_doc_crj_total,
    "47_scenario_multi_doc_cpj_total": _b47_scenario_multi_doc_cpj_total,
    "48_digital_vs_paper_source_docs_modern": _b48_digital_vs_paper_source_docs_modern,
    "49_case_study_missing_source_docs_audit": _b49_case_study_missing_source_docs_audit,
    "50_comprehensive_source_doc_capstone": _b50_comprehensive_source_doc_capstone,
}
