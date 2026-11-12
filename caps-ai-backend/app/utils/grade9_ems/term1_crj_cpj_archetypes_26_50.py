"""Grade 9 EMS - Cash Receipts Journal & Cash Payments Journal (Sole Trader): Archetypes 26 to 50.

Grounded strictly in:
- curriculum_docs_auto/EMS_Gr9/Term 2/02. Cash receipts journal and Cash payments journal (sole trader).md

Zero-LLM, 100% deterministic, authentic South African Rand (R) sole-trader contexts.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List

from app.utils.ems_namelist import get_ems_scenario
from .term1_crj_cpj_archetypes_01_25 import (
    CUSTOMERS_AND_PAYEES,
    MONTH_YEARS,
    _build_mcq,
    _build_short,
    _build_table,
    _fmt_r,
    _source_doc_svg,
    _trader_name,
)


def _cell(coord: str, value: str, ctype: str, editable: bool) -> Dict[str, Any]:
    return {
        "coordinate": coord,
        "cell_id": coord,
        "value": value,
        "type": ctype,
        "editable": editable,
    }


def arch_26_crj_capital_contribution_and_cash_sales_entry(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = _trader_name(rng, sc)
    m_name, yr, last_d, _ = rng.choice(MONTH_YEARS)
    markup = rng.choice([25, 40, 50])
    cap_amt = rng.randint(40, 120) * 1000
    cos_amt = rng.randint(12, 42) * 200
    sales_amt = cos_amt * (100 + markup) // 100
    bank_tot = cap_amt + sales_amt
    rec_no = f"REC {rng.randint(10, 88)}"
    crr_no = f"CRR {rng.randint(10, 45)}"

    headers = [
        "Doc. no.",
        "Day",
        "Details",
        "Analysis of Receipts",
        "Bank",
        "Sales",
        "Cost of Sales",
        "Sundry Amount",
        "Sundry Details",
    ]
    rows = [
        [
            _cell("t0_r0_c0", rec_no, "given", False),
            _cell("t0_r0_c1", "01", "given", False),
            _cell("t0_r0_c2", sc["entrepreneur"], "given", False),
            _cell("t0_r0_c3", "", "must_be_empty", True),
            _cell("t0_r0_c4", "", "required", True),
            _cell("t0_r0_c5", "", "must_be_empty", True),
            _cell("t0_r0_c6", "", "must_be_empty", True),
            _cell("t0_r0_c7", "", "required", True),
            _cell("t0_r0_c8", "", "required", True),
        ],
        [
            _cell("t0_r1_c0", crr_no, "given", False),
            _cell("t0_r1_c1", "12", "given", False),
            _cell("t0_r1_c2", "Sales", "given", False),
            _cell("t0_r1_c3", "", "required", True),
            _cell("t0_r1_c4", "", "required", True),
            _cell("t0_r1_c5", "", "required", True),
            _cell("t0_r1_c6", "", "required", True),
            _cell("t0_r1_c7", "", "must_be_empty", True),
            _cell("t0_r1_c8", "", "must_be_empty", True),
        ],
        [
            _cell("t0_r2_c0", "", "given", False),
            _cell("t0_r2_c1", last_d, "given", False),
            _cell("t0_r2_c2", "Totals", "given", False),
            _cell("t0_r2_c3", "-", "given", False),
            _cell("t0_r2_c4", "", "required", True),
            _cell("t0_r2_c5", str(sales_amt), "given", False),
            _cell("t0_r2_c6", str(cos_amt), "given", False),
            _cell("t0_r2_c7", str(cap_amt), "given", False),
            _cell("t0_r2_c8", "", "given", False),
        ],
    ]
    correct_map = {
        "t0_r0_c4": str(cap_amt),
        "t0_r0_c7": str(cap_amt),
        "t0_r0_c8": "Capital",
        "t0_r1_c3": str(sales_amt),
        "t0_r1_c4": str(sales_amt),
        "t0_r1_c5": str(sales_amt),
        "t0_r1_c6": str(cos_amt),
        "t0_r2_c4": str(bank_tot),
    }
    cell_hints = {
        "t0_r0_c4": "Direct EFT Capital goes straight to Bank (Analysis remains empty).",
        "t0_r0_c7": f"Enter {cap_amt} in Sundry Amount.",
        "t0_r0_c8": "Account name in Sundry Details: Capital.",
        "t0_r1_c3": f"Till cash sales go into Analysis of Receipts ({sales_amt}).",
        "t0_r1_c4": f"Daily deposit into Bank ({sales_amt}).",
        "t0_r1_c5": f"Selling Price goes to Sales ({sales_amt}).",
        "t0_r1_c6": f"Cost of Sales = {sales_amt} × 100 / {100 + markup} = {cos_amt}.",
        "t0_r2_c4": f"Bank total = Sales + Sundry = {sales_amt} + {cap_amt} = {bank_tot} (exclude Cost of Sales).",
    }
    prompt = (
        f"Record the following {m_name} {yr} transactions in the **Cash Receipts Journal** of **{biz}** "
        f"(mark-up is **{markup}% on cost**; enter numeric amounts without spaces or R, leave inapplicable cells blank):\n\n"
        f"- **Day 01 ({rec_no}):** Owner **{sc['entrepreneur']}** deposits **{_fmt_r(cap_amt)}** directly into the business bank account via EFT to start trading.\n"
        f"- **Day 12 ({crr_no}):** Cash sales per Cash Register Roll, **{_fmt_r(sales_amt)}**."
    )
    md = (
        "| Doc. no. | Day | Details | Analysis of Receipts | Bank | Sales | Cost of Sales | Sundry Amount | Sundry Details |\n"
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- |\n"
        f"| {rec_no} | 01 | {sc['entrepreneur']} | | **{cap_amt}** | | | **{cap_amt}** | **Capital** |\n"
        f"| {crr_no} | 12 | Sales | **{sales_amt}** | **{sales_amt}** | **{sales_amt}** | **{cos_amt}** | | |\n"
        f"| | {last_d} | Totals | - | **{bank_tot}** | {sales_amt} | {cos_amt} | {cap_amt} | |"
    )
    sample = f"Day 01: Bank {cap_amt}, Sundry {cap_amt} Capital; Day 12: Analysis/Bank/Sales {sales_amt}, COS {cos_amt}; Bank Total {bank_tot}"
    worked = f"**CRJ Capital & Cash Sales Memorandum** [8 marks]\n\n{md}"
    return _build_table(
        rng,
        qid_prefix="g9_cc_26",
        subskill="26_crj_capital_contribution_and_cash_sales_entry",
        title="CRJ Entry: Capital Direct EFT & Cash Sales",
        prompt=prompt,
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=sample,
        marks=8,
        hints={
            "tier_1": "Direct EFT skips Analysis of Receipts; cash sales from the till go through Analysis -> Bank -> Sales & Cost of Sales.",
            "tier_2": f"Cost of Sales = {cos_amt}; Bank total excludes Cost of Sales ({bank_tot}).",
            "tier_3": sample,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Direct Capital EFT in Bank & Sundry (Capital)", "marks": 3, "editable": True},
            {"id": "mp_2", "desc": f"Cash Sales Analysis/Bank/Sales = {sales_amt} and COS = {cos_amt}", "marks": 4, "editable": True},
            {"id": "mp_3", "desc": f"Bank total = {bank_tot}", "marks": 1, "editable": True},
        ],
        misconception_tags=["entering_direct_eft_in_analysis_of_receipts", "adding_cost_of_sales_to_bank_total"],
    )


def arch_27_crj_daily_banking_two_receipts_same_day(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = _trader_name(rng, sc)
    m_name, yr, _, _ = rng.choice(MONTH_YEARS)
    day = f"{rng.randint(5, 19):02d}"
    markup = rng.choice([25, 50])
    cos = rng.randint(10, 32) * 200
    sales_amt = cos * (100 + markup) // 100
    rent_amt = rng.randint(3, 12) * 400
    day_bank = sales_amt + rent_amt
    tenant = rng.choice(CUSTOMERS_AND_PAYEES[:5])
    crr_no = f"CRR {rng.randint(15, 65)}"
    rec_no = f"REC {rng.randint(21, 95)}"

    headers = ["Doc. no.", "Day", "Details", "Analysis of Receipts", "Bank", "Sales", "Cost of Sales", "Sundry Amount", "Sundry Details"]
    rows = [
        [
            _cell("t0_r0_c0", crr_no, "given", False),
            _cell("t0_r0_c1", day, "given", False),
            _cell("t0_r0_c2", "Sales", "given", False),
            _cell("t0_r0_c3", "", "required", True),
            _cell("t0_r0_c4", "", "must_be_empty", True),
            _cell("t0_r0_c5", "", "required", True),
            _cell("t0_r0_c6", "", "required", True),
            _cell("t0_r0_c7", "", "must_be_empty", True),
            _cell("t0_r0_c8", "", "must_be_empty", True),
        ],
        [
            _cell("t0_r1_c0", rec_no, "given", False),
            _cell("t0_r1_c1", "", "given", False),
            _cell("t0_r1_c2", tenant, "given", False),
            _cell("t0_r1_c3", "", "required", True),
            _cell("t0_r1_c4", "", "required", True),
            _cell("t0_r1_c5", "", "must_be_empty", True),
            _cell("t0_r1_c6", "", "must_be_empty", True),
            _cell("t0_r1_c7", "", "required", True),
            _cell("t0_r1_c8", "", "required", True),
        ],
    ]
    correct_map = {
        "t0_r0_c3": str(sales_amt),
        "t0_r0_c5": str(sales_amt),
        "t0_r0_c6": str(cos),
        "t0_r1_c3": str(rent_amt),
        "t0_r1_c4": str(day_bank),
        "t0_r1_c7": str(rent_amt),
        "t0_r1_c8": "Rent Income",
    }
    cell_hints = {
        "t0_r0_c3": f"First cash amount in till ({sales_amt}).",
        "t0_r0_c5": f"Sales amount ({sales_amt}).",
        "t0_r0_c6": f"Cost of Sales = {sales_amt} × 100 / {100 + markup} = {cos}.",
        "t0_r1_c3": f"Second cash amount received on Day {day} ({rent_amt}).",
        "t0_r1_c4": f"Combine both cash receipts on Day {day}: {sales_amt} + {rent_amt} = {day_bank}.",
        "t0_r1_c7": f"Rent goes into Sundry Amount ({rent_amt}).",
        "t0_r1_c8": "Sundry account name: Rent Income.",
    }
    prompt = (
        f"On **{day} {m_name} {yr}**, **{biz}** receives TWO cash amounts into the till (both banked together at closing time; mark-up **{markup}% on cost**):\n"
        f"- **{crr_no}:** Cash sales of **{_fmt_r(sales_amt)}**.\n"
        f"- **{rec_no}:** Cash received from tenant **{tenant}** for monthly rent, **{_fmt_r(rent_amt)}**.\n\n"
        f"Complete the same-day CRJ entries below (leave inapplicable cells blank; enter digits without spaces or R)."
    )
    md = (
        "| Doc. no. | Day | Details | Analysis of Receipts | Bank | Sales | Cost of Sales | Sundry Amount | Sundry Details |\n"
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- |\n"
        f"| {crr_no} | {day} | Sales | **{sales_amt}** | | **{sales_amt}** | **{cos}** | | |\n"
        f"| {rec_no} | | {tenant} | **{rent_amt}** | **{day_bank}** | | | **{rent_amt}** | **Rent Income** |"
    )
    sample = f"Analysis: {sales_amt} then {rent_amt}; combined Bank on line 2 = {day_bank}; Sales {sales_amt}, COS {cos}; Sundry {rent_amt} Rent Income"
    worked = f"**CRJ Same-Day Daily Banking Memorandum** [7 marks]\n\n{md}"
    return _build_table(
        rng,
        qid_prefix="g9_cc_27",
        subskill="27_crj_daily_banking_two_receipts_same_day",
        title="CRJ Same-Day Till Receipts & Daily Banking",
        prompt=prompt,
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=sample,
        marks=7,
        hints={
            "tier_1": "Keep Bank blank on the first receipt of the day and place the combined sum in Bank on the last receipt of that same day.",
            "tier_2": f"Bank on line 2 = {sales_amt} + {rent_amt} = {day_bank}; Cost of Sales = {cos}.",
            "tier_3": sample,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Line 1 Analysis, Sales, and Cost of Sales (Bank blank)", "marks": 3, "editable": True},
            {"id": "mp_2", "desc": f"Line 2 Analysis {rent_amt}, combined Bank {day_bank}, Sundry Rent Income", "marks": 4, "editable": True},
        ],
        misconception_tags=["banking_each_till_receipt_separately"],
    )


def arch_28_crj_direct_deposit_plus_till_cash_same_month(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = _trader_name(rng, sc)
    m_name, yr, _, _ = rng.choice(MONTH_YEARS)
    eft_amt = rng.randint(15, 55) * 1000
    eft_acc = rng.choice(["Capital", "Loan: Khanyisa Bank"])
    eft_payer = sc["entrepreneur"] if eft_acc == "Capital" else "Khanyisa Bank"
    till_sales = rng.randint(14, 48) * 250
    markup = 25
    till_cos = till_sales * 100 // 125

    headers = ["Doc. no.", "Day", "Details", "Analysis of Receipts", "Bank", "Sales", "Cost of Sales", "Sundry Amount", "Sundry Details"]
    rows = [
        [
            _cell("t0_r0_c0", "BS 01", "given", False),
            _cell("t0_r0_c1", "03", "given", False),
            _cell("t0_r0_c2", eft_payer, "given", False),
            _cell("t0_r0_c3", "", "must_be_empty", True),
            _cell("t0_r0_c4", "", "required", True),
            _cell("t0_r0_c5", "", "must_be_empty", True),
            _cell("t0_r0_c6", "", "must_be_empty", True),
            _cell("t0_r0_c7", "", "required", True),
            _cell("t0_r0_c8", "", "required", True),
        ],
        [
            _cell("t0_r1_c0", "CRR 09", "given", False),
            _cell("t0_r1_c1", "16", "given", False),
            _cell("t0_r1_c2", "Sales", "given", False),
            _cell("t0_r1_c3", "", "required", True),
            _cell("t0_r1_c4", "", "required", True),
            _cell("t0_r1_c5", "", "required", True),
            _cell("t0_r1_c6", "", "required", True),
            _cell("t0_r1_c7", "", "must_be_empty", True),
            _cell("t0_r1_c8", "", "must_be_empty", True),
        ],
    ]
    correct_map = {
        "t0_r0_c4": str(eft_amt),
        "t0_r0_c7": str(eft_amt),
        "t0_r0_c8": eft_acc,
        "t0_r1_c3": str(till_sales),
        "t0_r1_c4": str(till_sales),
        "t0_r1_c5": str(till_sales),
        "t0_r1_c6": str(till_cos),
    }
    cell_hints = {
        "t0_r0_c4": f"Direct EFT bypasses Analysis and enters Bank directly ({eft_amt}).",
        "t0_r0_c7": f"Sundry Amount = {eft_amt}.",
        "t0_r0_c8": f"Sundry Account = {eft_acc}.",
        "t0_r1_c3": f"Shop till sales pass through Analysis ({till_sales}).",
        "t0_r1_c4": f"Banked at day-end ({till_sales}).",
        "t0_r1_c5": f"Sales = {till_sales}.",
        "t0_r1_c6": f"Cost of Sales = {till_sales} × 100 / 125 = {till_cos}.",
    }
    desc_eft = "additional Capital directly into the business bank account" if eft_acc == "Capital" else "a business loan directly deposited into the business bank account"
    prompt = (
        f"Record these {m_name} {yr} CRJ entries for **{biz}** (mark-up **25% on cost**):\n"
        f"- **Day 03 (BS 01):** **{eft_payer}** transfers **{_fmt_r(eft_amt)}** as {desc_eft} (direct EFT).\n"
        f"- **Day 16 (CRR 09):** Cash sales via the shop till total **{_fmt_r(till_sales)}**."
    )
    md = (
        "| Doc. no. | Day | Details | Analysis of Receipts | Bank | Sales | Cost of Sales | Sundry Amount | Sundry Details |\n"
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- |\n"
        f"| BS 01 | 03 | {eft_payer} | | **{eft_amt}** | | | **{eft_amt}** | **{eft_acc}** |\n"
        f"| CRR 09 | 16 | Sales | **{till_sales}** | **{till_sales}** | **{till_sales}** | **{till_cos}** | | |"
    )
    sample = f"BS 01: Bank {eft_amt}, Sundry {eft_amt} {eft_acc} (Analysis empty); CRR 09: Analysis/Bank/Sales {till_sales}, COS {till_cos}"
    worked = f"**Direct EFT vs Till Cash CRJ Memorandum** [7 marks]\n\n{md}"
    return _build_table(
        rng,
        qid_prefix="g9_cc_28",
        subskill="28_crj_direct_deposit_plus_till_cash_same_month",
        title="CRJ Entry: Direct Bank Deposit vs Till Cash",
        prompt=prompt,
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=sample,
        marks=7,
        hints={
            "tier_1": "Direct EFT deposits bypass Analysis of Receipts; cash collected at the counter enters Analysis first.",
            "tier_2": f"Line 1: Bank {eft_amt}, Sundry {eft_acc}; Line 2: Analysis/Bank/Sales {till_sales}, COS {till_cos}.",
            "tier_3": sample,
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Direct EFT skips Analysis; Bank {eft_amt} and Sundry {eft_acc}", "marks": 3, "editable": True},
            {"id": "mp_2", "desc": f"Till cash in Analysis/Bank/Sales {till_sales}, COS {till_cos}", "marks": 4, "editable": True},
        ],
        misconception_tags=["entering_direct_eft_in_analysis_of_receipts"],
    )


def arch_29_crj_full_multi_transaction_journal_completion(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = _trader_name(rng, sc)
    m_name, yr, last_d, _ = rng.choice(MONTH_YEARS)
    markup = rng.choice([25, 50, 60])
    cap_amt = rng.randint(50, 140) * 1000
    cos1 = rng.randint(14, 40) * 200
    sp1 = cos1 * (100 + markup) // 100
    rent_amt = rng.randint(5, 16) * 500
    tenant = rng.choice(CUSTOMERS_AND_PAYEES[:5])
    sundry_tot = cap_amt + rent_amt
    bank_tot = sundry_tot + sp1

    headers = ["Doc. no.", "Day", "Details", "Analysis of Receipts", "Bank", "Sales", "Cost of Sales", "Sundry Amount", "Sundry Details"]
    rows = [
        [
            _cell("t0_r0_c0", "REC 01", "given", False),
            _cell("t0_r0_c1", "01", "given", False),
            _cell("t0_r0_c2", sc["entrepreneur"], "given", False),
            _cell("t0_r0_c3", "", "must_be_empty", True),
            _cell("t0_r0_c4", "", "required", True),
            _cell("t0_r0_c5", "", "must_be_empty", True),
            _cell("t0_r0_c6", "", "must_be_empty", True),
            _cell("t0_r0_c7", str(cap_amt), "given", False),
            _cell("t0_r0_c8", "", "required", True),
        ],
        [
            _cell("t0_r1_c0", "CRR 01", "given", False),
            _cell("t0_r1_c1", "10", "given", False),
            _cell("t0_r1_c2", "Sales", "given", False),
            _cell("t0_r1_c3", "", "required", True),
            _cell("t0_r1_c4", "", "required", True),
            _cell("t0_r1_c5", "", "required", True),
            _cell("t0_r1_c6", "", "required", True),
            _cell("t0_r1_c7", "", "must_be_empty", True),
            _cell("t0_r1_c8", "", "must_be_empty", True),
        ],
        [
            _cell("t0_r2_c0", "REC 02", "given", False),
            _cell("t0_r2_c1", "25", "given", False),
            _cell("t0_r2_c2", tenant, "given", False),
            _cell("t0_r2_c3", "", "required", True),
            _cell("t0_r2_c4", "", "required", True),
            _cell("t0_r2_c5", "", "must_be_empty", True),
            _cell("t0_r2_c6", "", "must_be_empty", True),
            _cell("t0_r2_c7", str(rent_amt), "given", False),
            _cell("t0_r2_c8", "", "required", True),
        ],
        [
            _cell("t0_r3_c0", "", "given", False),
            _cell("t0_r3_c1", last_d, "given", False),
            _cell("t0_r3_c2", "Totals", "given", False),
            _cell("t0_r3_c3", "-", "given", False),
            _cell("t0_r3_c4", "", "required", True),
            _cell("t0_r3_c5", "", "required", True),
            _cell("t0_r3_c6", "", "required", True),
            _cell("t0_r3_c7", "", "required", True),
            _cell("t0_r3_c8", "", "given", False),
        ],
    ]
    correct_map = {
        "t0_r0_c4": str(cap_amt),
        "t0_r0_c8": "Capital",
        "t0_r1_c3": str(sp1),
        "t0_r1_c4": str(sp1),
        "t0_r1_c5": str(sp1),
        "t0_r1_c6": str(cos1),
        "t0_r2_c3": str(rent_amt),
        "t0_r2_c4": str(rent_amt),
        "t0_r2_c8": "Rent Income",
        "t0_r3_c4": str(bank_tot),
        "t0_r3_c5": str(sp1),
        "t0_r3_c6": str(cos1),
        "t0_r3_c7": str(sundry_tot),
    }
    cell_hints = {
        "t0_r0_c4": f"Direct EFT enters Bank ({cap_amt}) without Analysis.",
        "t0_r0_c8": "Account name: Capital.",
        "t0_r1_c3": f"Till receipt in Analysis ({sp1}).",
        "t0_r1_c4": f"Banked on Day 10 ({sp1}).",
        "t0_r1_c5": f"Sales total ({sp1}).",
        "t0_r1_c6": f"Cost of Sales = {sp1} × 100 / {100 + markup} = {cos1}.",
        "t0_r2_c3": f"Till receipt from tenant ({rent_amt}).",
        "t0_r2_c4": f"Banked on Day 25 ({rent_amt}).",
        "t0_r2_c8": "Account name: Rent Income.",
        "t0_r3_c4": f"Sum Bank column = {cap_amt} + {sp1} + {rent_amt} = {bank_tot}.",
        "t0_r3_c5": f"Sales column total = {sp1}.",
        "t0_r3_c6": f"Cost of Sales column total = {cos1}.",
        "t0_r3_c7": f"Sundry column total = {cap_amt} + {rent_amt} = {sundry_tot}.",
    }
    prompt = (
        f"Complete the **Cash Receipts Journal (CRJ)** of **{biz}** for **{m_name} {yr}** (mark-up **{markup}% on cost**; enter digits without spaces or R):\n\n"
        f"- **Day 01 (REC 01):** **{sc['entrepreneur']}** deposits **{_fmt_r(cap_amt)}** directly into the business bank account as Capital.\n"
        f"- **Day 10 (CRR 01):** Cash sales of {sc['item_sold']} for **{_fmt_r(sp1)}**.\n"
        f"- **Day 25 (REC 02):** Received **{_fmt_r(rent_amt)}** cash in the till from tenant **{tenant}** for monthly rent (banked same day)."
    )
    md = (
        "| Doc. no. | Day | Details | Analysis of Receipts | Bank | Sales | Cost of Sales | Sundry Amount | Sundry Details |\n"
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- |\n"
        f"| REC 01 | 01 | {sc['entrepreneur']} | | **{cap_amt}** | | | {cap_amt} | **Capital** |\n"
        f"| CRR 01 | 10 | Sales | **{sp1}** | **{sp1}** | **{sp1}** | **{cos1}** | | |\n"
        f"| REC 02 | 25 | {tenant} | **{rent_amt}** | **{rent_amt}** | | | {rent_amt} | **Rent Income** |\n"
        f"| | {last_d} | Totals | - | **{bank_tot}** | **{sp1}** | **{cos1}** | **{sundry_tot}** | |\n\n"
        f"Cross-check: `Bank ({_fmt_r(bank_tot)}) = Sales ({_fmt_r(sp1)}) + Sundry ({_fmt_r(sundry_tot)})`."
    )
    sample = f"CRJ Totals -> Bank {bank_tot}, Sales {sp1}, COS {cos1}, Sundry {sundry_tot}"
    worked = f"**Completed Cash Receipts Journal Memorandum** [12 marks]\n\n{md}"
    return _build_table(
        rng,
        qid_prefix="g9_cc_29",
        subskill="29_crj_full_multi_transaction_journal_completion",
        title="Complete Multi-Transaction Sole-Trader CRJ",
        prompt=prompt,
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=sample,
        marks=12,
        hints={
            "tier_1": "Enter direct Capital straight in Bank + Sundry; till sales in Analysis/Bank/Sales/COS; tenant rent in Analysis/Bank/Sundry.",
            "tier_2": f"COS = {cos1}; CRJ Bank total ({bank_tot}) = Sales ({sp1}) + Sundry ({sundry_tot}).",
            "tier_3": sample,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Day 01 Capital direct Bank & details", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": f"Day 10 Cash Sales ({sp1}) & COS ({cos1})", "marks": 4, "editable": True},
            {"id": "mp_3", "desc": "Day 25 Rent Income till & Bank", "marks": 3, "editable": True},
            {"id": "mp_4", "desc": "Month-end balancing Totals row", "marks": 3, "editable": True},
        ],
        misconception_tags=["adding_cost_of_sales_to_bank_total", "entering_direct_eft_in_analysis_of_receipts"],
    )


def arch_30_crj_cash_sales_with_varied_markup_and_totals(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = _trader_name(rng, sc)
    m_name, yr, last_d, _ = rng.choice(MONTH_YEARS)
    markup = rng.choice([25, 40, 50])
    cos1 = rng.randint(10, 35) * 200
    sp1 = cos1 * (100 + markup) // 100
    cos2 = rng.randint(12, 38) * 200
    sp2 = cos2 * (100 + markup) // 100
    tot_sales = sp1 + sp2
    tot_cos = cos1 + cos2

    headers = ["Doc. no.", "Day", "Details", "Analysis of Receipts", "Bank", "Sales", "Cost of Sales"]
    rows = [
        [
            _cell("t0_r0_c0", "CRR 14", "given", False),
            _cell("t0_r0_c1", "08", "given", False),
            _cell("t0_r0_c2", "Sales", "given", False),
            _cell("t0_r0_c3", str(sp1), "given", False),
            _cell("t0_r0_c4", str(sp1), "given", False),
            _cell("t0_r0_c5", "", "required", True),
            _cell("t0_r0_c6", "", "required", True),
        ],
        [
            _cell("t0_r1_c0", "CRR 15", "given", False),
            _cell("t0_r1_c1", "22", "given", False),
            _cell("t0_r1_c2", "Sales", "given", False),
            _cell("t0_r1_c3", "", "required", True),
            _cell("t0_r1_c4", "", "required", True),
            _cell("t0_r1_c5", "", "required", True),
            _cell("t0_r1_c6", str(cos2), "given", False),
        ],
        [
            _cell("t0_r2_c0", "", "given", False),
            _cell("t0_r2_c1", last_d, "given", False),
            _cell("t0_r2_c2", "Totals", "given", False),
            _cell("t0_r2_c3", "-", "given", False),
            _cell("t0_r2_c4", "", "required", True),
            _cell("t0_r2_c5", "", "required", True),
            _cell("t0_r2_c6", "", "required", True),
        ],
    ]
    correct_map = {
        "t0_r0_c5": str(sp1),
        "t0_r0_c6": str(cos1),
        "t0_r1_c3": str(sp2),
        "t0_r1_c4": str(sp2),
        "t0_r1_c5": str(sp2),
        "t0_r2_c4": str(tot_sales),
        "t0_r2_c5": str(tot_sales),
        "t0_r2_c6": str(tot_cos),
    }
    cell_hints = {
        "t0_r0_c5": f"Cash sales on Day 08 = {sp1}.",
        "t0_r0_c6": f"Given SP {sp1} and mark-up {markup}%, COS = {sp1} × 100/{100 + markup} = {cos1}.",
        "t0_r1_c3": f"Given Cost Price {cos2} and mark-up {markup}%, SP = {cos2} × {100 + markup}/100 = {sp2}.",
        "t0_r1_c4": f"Bank on Day 22 = {sp2}.",
        "t0_r1_c5": f"Sales on Day 22 = {sp2}.",
        "t0_r2_c4": f"Total Bank = {sp1} + {sp2} = {tot_sales}.",
        "t0_r2_c5": f"Total Sales = {sp1} + {sp2} = {tot_sales}.",
        "t0_r2_c6": f"Total Cost of Sales = {cos1} + {cos2} = {tot_cos}.",
    }
    prompt = (
        f"Complete the cash-sales CRJ extract for **{biz}** (**{m_name} {yr}**, profit mark-up **{markup}% on cost**):\n"
        f"- **Day 08 (CRR 14):** Cash sales Selling Price = **{_fmt_r(sp1)}** (find Cost of Sales).\n"
        f"- **Day 22 (CRR 15):** Merchandise with a **Cost Price of {_fmt_r(cos2)}** is sold for cash (find Selling Price, Analysis, and Bank).\n\n"
        f"Complete all missing cells and column totals."
    )
    md = (
        "| Doc. no. | Day | Details | Analysis of Receipts | Bank | Sales | Cost of Sales |\n"
        "| --- | --- | --- | --- | --- | --- | --- |\n"
        f"| CRR 14 | 08 | Sales | {sp1} | {sp1} | **{sp1}** | **{cos1}** |\n"
        f"| CRR 15 | 22 | Sales | **{sp2}** | **{sp2}** | **{sp2}** | {cos2} |\n"
        f"| | {last_d} | Totals | - | **{tot_sales}** | **{tot_sales}** | **{tot_cos}** |"
    )
    sample = f"Day 08 COS {cos1}; Day 22 SP/Bank {sp2}; Totals: Bank {tot_sales}, Sales {tot_sales}, COS {tot_cos}"
    worked = f"**Two-Way Mark-up CRJ Sales Memorandum** [8 marks]\n\n{md}"
    return _build_table(
        rng,
        qid_prefix="g9_cc_30",
        subskill="30_crj_cash_sales_with_varied_markup_and_totals",
        title="CRJ Cash Sales: Forward & Reverse Mark-up Table",
        prompt=prompt,
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=sample,
        marks=8,
        hints={
            "tier_1": "Day 08 reverses from Selling Price to Cost Price; Day 22 calculates forward from Cost Price to Selling Price.",
            "tier_2": f"Day 08 COS = {cos1}; Day 22 SP = {sp2}.",
            "tier_3": sample,
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Day 08 Sales {sp1} and COS {cos1}", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": f"Day 22 Analysis/Bank/Sales {sp2}", "marks": 3, "editable": True},
            {"id": "mp_3", "desc": f"Totals: Bank {tot_sales}, Sales {tot_sales}, COS {tot_cos}", "marks": 3, "editable": True},
        ],
        misconception_tags=["confusing_forward_and_reverse_markup"],
    )


def arch_31_cpj_column_structure_and_source_docs(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = _trader_name(rng, sc)
    cases = [
        (
            "document number sequence and primary purpose of the Bank column in the CPJ",
            "Records cheques/EFTs in strict numerical order (`Cheque No.`/`EFT`) and shows total cash flowing OUT of the business bank account.",
            [
                "Lists only cash receipts collected through the cash register till in ascending order.",
                "Always omits transactions under R1 000 because petty cash belongs in Cost of Sales.",
                "Measures total Selling Price earned from cash customers during the month.",
            ],
        ),
        (
            "rule governing which accounts earn dedicated analysis columns versus Sundry Accounts in the CPJ",
            "Recurring payments made frequently (like Trading Stock, Wages, or Stationery) get dedicated analysis columns, while occasional items (Equipment, Drawings, Rent) go to Sundry Accounts.",
            [
                "Every single expense or asset must go into Sundry Accounts and no analysis columns are permitted.",
                "Sundry Accounts is exclusively for Capital and Sales receipts from customers.",
                "Fixed assets like Vehicles are combined into the Trading Stock column to save space.",
            ],
        ),
    ]
    focus, correct, distractors = rng.choice(cases)
    prompt = (
        f"When setting up the **Cash Payments Journal (CPJ)** for **{biz}** in {sc['area']}, "
        f"which statement accurately states the {focus}?"
    )
    return _build_mcq(
        rng,
        qid_prefix="g9_cc_31",
        subskill="31_cpj_column_structure_and_source_docs",
        title="CPJ Structure & Column Design Rules",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=f"In a sole-trader CPJ: **{correct}**",
        hints={
            "tier_1": "Think of how the CPJ tracks sequential cash outflows and organises frequent vs occasional payments.",
            "tier_2": "Bank tracks every payment out; frequent payments get dedicated analysis columns; once-off items use Sundry Accounts.",
            "tier_3": correct,
        },
        misconception_tags=["cpj_column_classification_error"],
    )


def arch_32_cpj_cash_payee_for_wages_and_cash_float(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = _trader_name(rng, sc)
    amt = rng.randint(12, 45) * 100
    item = rng.choice(["weekly staff Wages", "the shop's Cash Float"])

    prompt = (
        f"**{biz}** withdraws **{_fmt_r(amt)}** in bank notes over the counter (via cheque/cash withdrawal) to pay **{item}**.\n\n"
        f"What exact wording must appear in the **`Name of Payee`** column of the **Cash Payments Journal (CPJ)**?"
    )
    correct = "Cash (because notes are drawn physically over the bank counter rather than paid to a specific external named payee)."
    distractors = [
        f"{sc['entrepreneur']} (always write the owner's personal name regardless of payment type).",
        "Wages / Cash Float (the Name of Payee column always shows the ledger account name instead of the payee).",
        "Leave Name of Payee completely blank whenever Bank notes are withdrawn.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g9_cc_32",
        subskill="32_cpj_cash_payee_for_wages_and_cash_float",
        title="CPJ Name of Payee Rule for 'Cash' Withdrawals",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"When cash is withdrawn physically for **{item}** ({_fmt_r(amt)}), **`Name of Payee`** records **`Cash`** "
            f"(showing who/what the counter withdrawal was made out to), while the account allocation column records `{ 'Wages' if 'Wages' in item else 'Sundry: Cash Float' }`."
        ),
        hints={
            "tier_1": "When withdrawing banknotes from the bank for wages or a till float, who is the cheque made payable to?",
            "tier_2": "The Name of Payee column records 'Cash' — ledger account names belong in analysis or Sundry Details.",
            "tier_3": correct,
        },
        misconception_tags=["writing_account_name_in_payee_column"],
    )


def arch_33_cpj_split_cheque_trading_stock_and_stationery(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = _trader_name(rng, sc)
    m_name, yr, _, _ = rng.choice(MONTH_YEARS)
    stock_amt = rng.randint(15, 55) * 200
    stat_amt = rng.randint(4, 18) * 50
    total_bank = stock_amt + stat_amt
    chq_no = f"CHQ {rng.randint(102, 290)}"

    headers = ["Doc. no.", "Day", "Name of Payee", "Bank", "Trading Stock", "Wages", "Sundry Amount", "Sundry Details"]
    rows = [[
        _cell("t0_r0_c0", chq_no, "given", False),
        _cell("t0_r0_c1", "14", "given", False),
        _cell("t0_r0_c2", sc["supplier"], "given", False),
        _cell("t0_r0_c3", "", "required", True),
        _cell("t0_r0_c4", "", "required", True),
        _cell("t0_r0_c5", "", "must_be_empty", True),
        _cell("t0_r0_c6", "", "required", True),
        _cell("t0_r0_c7", "", "required", True),
    ]]
    correct_map = {
        "t0_r0_c3": str(total_bank),
        "t0_r0_c4": str(stock_amt),
        "t0_r0_c6": str(stat_amt),
        "t0_r0_c7": "Stationery",
    }
    cell_hints = {
        "t0_r0_c3": f"Total Bank cheque/EFT outflow = {stock_amt} + {stat_amt} = {total_bank}.",
        "t0_r0_c4": f"Stock portion ({stock_amt}) goes to Trading Stock.",
        "t0_r0_c6": f"Stationery portion ({stat_amt}) goes to Sundry Amount.",
        "t0_r0_c7": "Sundry account name: Stationery.",
    }
    prompt = (
        f"On **14 {m_name} {yr}**, **{biz}** pays **{sc['supplier']}** by cheque/EFT (**{chq_no}**) for:\n"
        f"- Merchandise bought for resale: **{_fmt_r(stock_amt)}**\n"
        f"- Office stationery for shop administration: **{_fmt_r(stat_amt)}**\n\n"
        f"Complete the CPJ row below (leave inapplicable cells blank; enter digits without spaces or R)."
    )
    md = (
        "| Doc. no. | Day | Name of Payee | Bank | Trading Stock | Wages | Sundry Amount | Sundry Details |\n"
        "| --- | --- | --- | --- | --- | --- | --- | --- |\n"
        f"| {chq_no} | 14 | {sc['supplier']} | **{total_bank}** | **{stock_amt}** | | **{stat_amt}** | **Stationery** |"
    )
    sample = f"Bank {total_bank}; Trading Stock {stock_amt}; Sundry {stat_amt} Stationery"
    worked = f"**CPJ Split Invoice Allocation Memorandum** [4 marks]\n\n{md}"
    return _build_table(
        rng,
        qid_prefix="g9_cc_33",
        subskill="33_cpj_split_cheque_trading_stock_and_stationery",
        title="CPJ Split Payment: Trading Stock & Stationery",
        prompt=prompt,
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=sample,
        marks=4,
        hints={
            "tier_1": "Enter the full cheque total in Bank, then split it across Trading Stock and Sundry Accounts (Stationery).",
            "tier_2": f"Bank = {total_bank}, Trading Stock = {stock_amt}, Sundry = {stat_amt} Stationery.",
            "tier_3": sample,
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Bank total = {total_bank}", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": f"Trading Stock = {stock_amt}", "marks": 1, "editable": True},
            {"id": "mp_3", "desc": f"Sundry {stat_amt} Stationery", "marks": 2, "editable": True},
        ],
        misconception_tags=["lumping_stationery_into_trading_stock"],
    )


def arch_34_cpj_split_cheque_business_and_owner_drawings(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = _trader_name(rng, sc)
    m_name, yr, _, _ = rng.choice(MONTH_YEARS)
    payee = rng.choice(["City Treasurer", "Metro Municipality", "Telkom SA"])
    bus_acc = "Telephone" if "Telkom" in payee else "Water and Electricity"
    bus_amt = rng.randint(12, 42) * 50
    draw_amt = rng.randint(6, 20) * 50
    tot_chq = bus_amt + draw_amt
    doc = f"EFT {rng.randint(301, 499)}"

    headers = ["Doc. no.", "Day", "Name of Payee", "Bank", "Trading Stock", "Wages", "Sundry Amount", "Sundry Details"]
    rows = [
        [
            _cell("t0_r0_c0", doc, "given", False),
            _cell("t0_r0_c1", "19", "given", False),
            _cell("t0_r0_c2", payee, "given", False),
            _cell("t0_r0_c3", "", "required", True),
            _cell("t0_r0_c4", "", "must_be_empty", True),
            _cell("t0_r0_c5", "", "must_be_empty", True),
            _cell("t0_r0_c6", "", "required", True),
            _cell("t0_r0_c7", "", "required", True),
        ],
        [
            _cell("t0_r1_c0", "", "given", False),
            _cell("t0_r1_c1", "", "given", False),
            _cell("t0_r1_c2", "", "given", False),
            _cell("t0_r1_c3", "", "must_be_empty", True),
            _cell("t0_r1_c4", "", "must_be_empty", True),
            _cell("t0_r1_c5", "", "must_be_empty", True),
            _cell("t0_r1_c6", "", "required", True),
            _cell("t0_r1_c7", "", "required", True),
        ],
    ]
    correct_map = {
        "t0_r0_c3": str(tot_chq),
        "t0_r0_c6": str(bus_amt),
        "t0_r0_c7": bus_acc,
        "t0_r1_c6": str(draw_amt),
        "t0_r1_c7": "Drawings",
    }
    cell_hints = {
        "t0_r0_c3": f"Single EFT outflow in Bank = {tot_chq}.",
        "t0_r0_c6": f"Business portion = {bus_amt}.",
        "t0_r0_c7": f"Business account name: {bus_acc}.",
        "t0_r1_c6": f"Owner's personal portion = {tot_chq} - {bus_amt} = {draw_amt}.",
        "t0_r1_c7": "Owner's personal account name: Drawings.",
    }
    prompt = (
        f"On **19 {m_name} {yr}**, **{biz}** issues one EFT (**{doc}**) to **{payee}** for **{_fmt_r(tot_chq)}**. "
        f"Of this amount, **{_fmt_r(bus_amt)}** is for the business's **{bus_acc}**, and the remainder pays **{sc['entrepreneur']}'s personal {bus_acc.lower()}**.\n\n"
        f"Complete both lines in the CPJ below (enter Bank ONCE on line 1; enter digits without spaces or R)."
    )
    md = (
        "| Doc. no. | Day | Name of Payee | Bank | Trading Stock | Wages | Sundry Amount | Sundry Details |\n"
        "| --- | --- | --- | --- | --- | --- | --- | --- |\n"
        f"| {doc} | 19 | {payee} | **{tot_chq}** | | | **{bus_amt}** | **{bus_acc}** |\n"
        f"| | | | | | | **{draw_amt}** | **Drawings** |"
    )
    sample = f"Bank {tot_chq}; Sundry lines: {bus_amt} {bus_acc} and {draw_amt} Drawings"
    worked = f"**CPJ Split Business & Drawings Memorandum** [5 marks]\n\n{md}"
    return _build_table(
        rng,
        qid_prefix="g9_cc_34",
        subskill="34_cpj_split_cheque_business_and_owner_drawings",
        title="CPJ Split EFT: Business Expense & Drawings",
        prompt=prompt,
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=sample,
        marks=5,
        hints={
            "tier_1": "When two Sundry items share one EFT, enter the full Bank amount once on the first line and split Sundry across two lines.",
            "tier_2": f"Bank = {tot_chq}; Line 1 Sundry = {bus_amt} ({bus_acc}); Line 2 Sundry = {draw_amt} (Drawings).",
            "tier_3": sample,
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Bank {tot_chq} entered once on line 1", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": f"Line 1 Sundry: {bus_amt} {bus_acc}", "marks": 2, "editable": True},
            {"id": "mp_3", "desc": f"Line 2 Sundry: {draw_amt} Drawings", "marks": 2, "editable": True},
        ],
        misconception_tags=["mixing_drawings_into_business_expenses"],
    )


def arch_35_cpj_fixed_asset_purchase_equipment_or_vehicles(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = _trader_name(rng, sc)
    m_name, yr, _, _ = rng.choice(MONTH_YEARS)
    asset_acc, item_desc, seller = rng.choice([
        ("Equipment", "electronic barcode scanner & display shelves", "Palesa Furnishers"),
        ("Vehicles", "used delivery bakkie", "Zanele Motors"),
    ])
    asset_amt = rng.randint(18, 85) * 500 if asset_acc == "Equipment" else rng.randint(60, 145) * 1000
    stock_amt = rng.randint(10, 35) * 300

    headers = ["Doc. no.", "Day", "Name of Payee", "Bank", "Trading Stock", "Wages", "Sundry Amount", "Sundry Details"]
    rows = [
        [
            _cell("t0_r0_c0", "CHQ 41", "given", False),
            _cell("t0_r0_c1", "05", "given", False),
            _cell("t0_r0_c2", seller, "given", False),
            _cell("t0_r0_c3", "", "required", True),
            _cell("t0_r0_c4", "", "must_be_empty", True),
            _cell("t0_r0_c5", "", "must_be_empty", True),
            _cell("t0_r0_c6", "", "required", True),
            _cell("t0_r0_c7", "", "required", True),
        ],
        [
            _cell("t0_r1_c0", "CHQ 42", "given", False),
            _cell("t0_r1_c1", "11", "given", False),
            _cell("t0_r1_c2", sc["supplier"], "given", False),
            _cell("t0_r1_c3", "", "required", True),
            _cell("t0_r1_c4", "", "required", True),
            _cell("t0_r1_c5", "", "must_be_empty", True),
            _cell("t0_r1_c6", "", "must_be_empty", True),
            _cell("t0_r1_c7", "", "must_be_empty", True),
        ],
    ]
    correct_map = {
        "t0_r0_c3": str(asset_amt),
        "t0_r0_c6": str(asset_amt),
        "t0_r0_c7": asset_acc,
        "t0_r1_c3": str(stock_amt),
        "t0_r1_c4": str(stock_amt),
    }
    cell_hints = {
        "t0_r0_c3": f"Total payment to {seller} ({asset_amt}).",
        "t0_r0_c6": f"Fixed asset goes into Sundry Amount ({asset_amt}), NOT Trading Stock.",
        "t0_r0_c7": f"Fixed asset account name: {asset_acc}.",
        "t0_r1_c3": f"Cash purchase from supplier ({stock_amt}).",
        "t0_r1_c4": f"Goods for resale go into Trading Stock ({stock_amt}).",
    }
    prompt = (
        f"Distinguish **Fixed Assets** from **Goods for Resale** in the CPJ of **{biz}** ({m_name} {yr}):\n"
        f"- **Day 05 (CHQ 41):** Bought a **{item_desc}** for business use from **{seller}** for **{_fmt_r(asset_amt)}**.\n"
        f"- **Day 11 (CHQ 42):** Bought merchandise for resale from **{sc['supplier']}** for **{_fmt_r(stock_amt)}**."
    )
    md = (
        "| Doc. no. | Day | Name of Payee | Bank | Trading Stock | Wages | Sundry Amount | Sundry Details |\n"
        "| --- | --- | --- | --- | --- | --- | --- | --- |\n"
        f"| CHQ 41 | 05 | {seller} | **{asset_amt}** | | | **{asset_amt}** | **{asset_acc}** |\n"
        f"| CHQ 42 | 11 | {sc['supplier']} | **{stock_amt}** | **{stock_amt}** | | | |"
    )
    sample = f"CHQ 41: Bank {asset_amt}, Sundry {asset_amt} {asset_acc}; CHQ 42: Bank {stock_amt}, Trading Stock {stock_amt}"
    worked = f"**CPJ Fixed Asset vs Trading Stock Memorandum** [5 marks]\n\n{md}"
    return _build_table(
        rng,
        qid_prefix="g9_cc_35",
        subskill="35_cpj_fixed_asset_purchase_equipment_or_vehicles",
        title="CPJ Allocation: Fixed Assets vs Trading Stock",
        prompt=prompt,
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=sample,
        marks=5,
        hints={
            "tier_1": "Fixed assets kept for long-term use go to Sundry Accounts (Equipment/Vehicles); only items bought to resell go to Trading Stock.",
            "tier_2": f"Day 05 -> Bank {asset_amt} & Sundry {asset_acc}; Day 11 -> Bank {stock_amt} & Trading Stock.",
            "tier_3": sample,
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Allocates {item_desc} to Sundry: {asset_acc}", "marks": 3, "editable": True},
            {"id": "mp_2", "desc": f"Allocates merchandise to Trading Stock ({stock_amt})", "marks": 2, "editable": True},
        ],
        misconception_tags=["putting_equipment_in_trading_stock"],
    )


def arch_36_cpj_trading_stock_and_carriage_on_purchases(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = _trader_name(rng, sc)
    stock_amt = rng.randint(18, 65) * 200
    carriage = rng.randint(4, 18) * 50
    tot_stock = stock_amt + carriage
    expected = str(tot_stock)

    prompt = (
        f"**{biz}** buys trading stock ({sc['item_sold']}) from **{sc['supplier']}** for **{_fmt_r(stock_amt)}** "
        f"plus a separate EFT of **{_fmt_r(carriage)}** to **Zanele Logistics** for **carriage on purchases** (delivering that stock to the shop).\n\n"
        f"According to historical cost accounting for a sole trader, what is the **total debit allocated to Trading Stock** from both CPJ payments?\n"
        f"*(Enter digits without spaces or R.)*"
    )
    worked = (
        f"**Total Cost of Trading Stock (Including Carriage on Purchases)** [3 marks]\n\n"
        f"- Invoice cost of goods: `{_fmt_r(stock_amt)}`\n"
        f"- Add carriage / railage on purchases: `{_fmt_r(carriage)}` (also recorded in the CPJ `Trading Stock` column because transport is required to bring stock into saleable condition/location)\n"
        f"- Total Trading Stock cost = `{_fmt_r(stock_amt)} + {_fmt_r(carriage)} = {_fmt_r(tot_stock)}` -> Answer: `{expected}`"
    )
    return _build_short(
        rng,
        qid_prefix="g9_cc_36",
        subskill="36_cpj_trading_stock_and_carriage_on_purchases",
        title="Carriage on Purchases Included in Trading Stock",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=worked,
        marks=3,
        hints={
            "tier_1": "Transport costs paid to bring trading stock into the shop form part of the cost of Trading Stock.",
            "tier_2": f"Add invoice price ({_fmt_r(stock_amt)}) and carriage on purchases ({_fmt_r(carriage)}).",
            "tier_3": f"Total Trading Stock = {expected}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": "Includes carriage on purchases in Trading Stock cost", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": f"Total = {_fmt_r(tot_stock)}", "marks": 2, "editable": True},
        ],
        misconception_tags=["omitting_carriage_from_trading_stock"],
    )


def arch_37_cpj_wages_increase_calculation_and_entry(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = _trader_name(rng, sc)
    old_wage = rng.randint(10, 45) * 100
    inc_pct = rng.choice([8, 10, 12, 15, 20])
    new_wage = old_wage * (100 + inc_pct) // 100
    expected = str(new_wage)

    prompt = (
        f"Shop assistants at **{biz}** previously earned weekly wages of **{_fmt_r(old_wage)}**. "
        f"Starting this Friday, wages increase by **{inc_pct}%**, and **{biz}** cashes a wage withdrawal (`Name of Payee: Cash`).\n\n"
        f"Calculate the new wage amount to enter in the **Bank** and **Wages** columns of the CPJ.\n"
        f"*(Enter digits without spaces or R.)*"
    )
    worked = (
        f"**Wages Increase CPJ Calculation** [2 marks]\n\n"
        f"- Increase = `{inc_pct}% × {_fmt_r(old_wage)} = {_fmt_r(new_wage - old_wage)}`\n"
        f"- New CPJ entry (`Payee: Cash`, `Bank` & `Wages`) = `{_fmt_r(old_wage)} + {_fmt_r(new_wage - old_wage)} = {_fmt_r(new_wage)}`\n"
        f"- Answer: `{expected}`"
    )
    return _build_short(
        rng,
        qid_prefix="g9_cc_37",
        subskill="37_cpj_wages_increase_calculation_and_entry",
        title="Calculate Wage Increase for CPJ Entry",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=worked,
        marks=2,
        hints={
            "tier_1": "Multiply previous wages by (100 + increase%) / 100.",
            "tier_2": f"New wages = {_fmt_r(old_wage)} × {100 + inc_pct} / 100.",
            "tier_3": f"CPJ Wages = {expected}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Calculates {_fmt_r(old_wage)} + {inc_pct}% = {_fmt_r(new_wage)}", "marks": 2, "editable": True},
        ],
        misconception_tags=["percentage_increase_arithmetic_error"],
    )


def arch_38_cpj_full_multi_transaction_journal_completion(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = _trader_name(rng, sc)
    m_name, yr, last_d, _ = rng.choice(MONTH_YEARS)
    stock_amt = rng.randint(15, 48) * 300
    wages_amt = rng.randint(6, 22) * 250
    draw_amt = rng.randint(5, 18) * 200
    bank_tot = stock_amt + wages_amt + draw_amt

    headers = ["Doc. no.", "Day", "Name of Payee", "Bank", "Trading Stock", "Wages", "Sundry Amount", "Sundry Details"]
    rows = [
        [
            _cell("t0_r0_c0", "CHQ 101", "given", False),
            _cell("t0_r0_c1", "04", "given", False),
            _cell("t0_r0_c2", sc["supplier"], "given", False),
            _cell("t0_r0_c3", "", "required", True),
            _cell("t0_r0_c4", "", "required", True),
            _cell("t0_r0_c5", "", "must_be_empty", True),
            _cell("t0_r0_c6", "", "must_be_empty", True),
            _cell("t0_r0_c7", "", "must_be_empty", True),
        ],
        [
            _cell("t0_r1_c0", "CHQ 102", "given", False),
            _cell("t0_r1_c1", "15", "given", False),
            _cell("t0_r1_c2", "", "required", True),
            _cell("t0_r1_c3", "", "required", True),
            _cell("t0_r1_c4", "", "must_be_empty", True),
            _cell("t0_r1_c5", "", "required", True),
            _cell("t0_r1_c6", "", "must_be_empty", True),
            _cell("t0_r1_c7", "", "must_be_empty", True),
        ],
        [
            _cell("t0_r2_c0", "EFT 103", "given", False),
            _cell("t0_r2_c1", "26", "given", False),
            _cell("t0_r2_c2", sc["entrepreneur"], "given", False),
            _cell("t0_r2_c3", "", "required", True),
            _cell("t0_r2_c4", "", "must_be_empty", True),
            _cell("t0_r2_c5", "", "must_be_empty", True),
            _cell("t0_r2_c6", str(draw_amt), "given", False),
            _cell("t0_r2_c7", "", "required", True),
        ],
        [
            _cell("t0_r3_c0", "", "given", False),
            _cell("t0_r3_c1", last_d, "given", False),
            _cell("t0_r3_c2", "Totals", "given", False),
            _cell("t0_r3_c3", "", "required", True),
            _cell("t0_r3_c4", "", "required", True),
            _cell("t0_r3_c5", "", "required", True),
            _cell("t0_r3_c6", "", "required", True),
            _cell("t0_r3_c7", "", "given", False),
        ],
    ]
    correct_map = {
        "t0_r0_c3": str(stock_amt),
        "t0_r0_c4": str(stock_amt),
        "t0_r1_c2": "Cash",
        "t0_r1_c3": str(wages_amt),
        "t0_r1_c5": str(wages_amt),
        "t0_r2_c3": str(draw_amt),
        "t0_r2_c7": "Drawings",
        "t0_r3_c3": str(bank_tot),
        "t0_r3_c4": str(stock_amt),
        "t0_r3_c5": str(wages_amt),
        "t0_r3_c6": str(draw_amt),
    }
    cell_hints = {
        "t0_r0_c3": f"Bank outflow on Day 04 = {stock_amt}.",
        "t0_r0_c4": f"Stock bought for resale = {stock_amt}.",
        "t0_r1_c2": "Physical cash wage withdrawal uses Payee: Cash.",
        "t0_r1_c3": f"Bank outflow for wages = {wages_amt}.",
        "t0_r1_c5": f"Wages column = {wages_amt}.",
        "t0_r2_c3": f"Bank outflow for owner's withdrawal = {draw_amt}.",
        "t0_r2_c7": "Personal owner withdrawal goes to Sundry Details: Drawings.",
        "t0_r3_c3": f"Sum all Bank payments = {stock_amt} + {wages_amt} + {draw_amt} = {bank_tot}.",
        "t0_r3_c4": f"Total Trading Stock = {stock_amt}.",
        "t0_r3_c5": f"Total Wages = {wages_amt}.",
        "t0_r3_c6": f"Total Sundry = {draw_amt}.",
    }
    prompt = (
        f"Complete the **Cash Payments Journal (CPJ)** of **{biz}** for **{m_name} {yr}** (enter digits without spaces or R):\n\n"
        f"- **Day 04 (CHQ 101):** Paid **{sc['supplier']}** **{_fmt_r(stock_amt)}** for trading stock.\n"
        f"- **Day 15 (CHQ 102):** Cashed a cheque for **{_fmt_r(wages_amt)}** to pay staff wages.\n"
        f"- **Day 26 (EFT 103):** Owner **{sc['entrepreneur']}** withdrew **{_fmt_r(draw_amt)}** via EFT for personal use."
    )
    md = (
        "| Doc. no. | Day | Name of Payee | Bank | Trading Stock | Wages | Sundry Amount | Sundry Details |\n"
        "| --- | --- | --- | --- | --- | --- | --- | --- |\n"
        f"| CHQ 101 | 04 | {sc['supplier']} | **{stock_amt}** | **{stock_amt}** | | | |\n"
        f"| CHQ 102 | 15 | **Cash** | **{wages_amt}** | | **{wages_amt}** | | |\n"
        f"| EFT 103 | 26 | {sc['entrepreneur']} | **{draw_amt}** | | | {draw_amt} | **Drawings** |\n"
        f"| | {last_d} | Totals | **{bank_tot}** | **{stock_amt}** | **{wages_amt}** | **{draw_amt}** | |\n\n"
        f"Cross-check: `Bank ({_fmt_r(bank_tot)}) = Trading Stock ({_fmt_r(stock_amt)}) + Wages ({_fmt_r(wages_amt)}) + Sundry ({_fmt_r(draw_amt)})`."
    )
    sample = f"CPJ Totals -> Bank {bank_tot}, Trading Stock {stock_amt}, Wages {wages_amt}, Sundry {draw_amt} (Drawings); Wage Payee Cash"
    worked = f"**Completed Cash Payments Journal Memorandum** [11 marks]\n\n{md}"
    return _build_table(
        rng,
        qid_prefix="g9_cc_38",
        subskill="38_cpj_full_multi_transaction_journal_completion",
        title="Complete Multi-Transaction Sole-Trader CPJ",
        prompt=prompt,
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=sample,
        marks=11,
        hints={
            "tier_1": "Remember 'Cash' as Payee for cashed wages, 'Drawings' in Sundry for owner withdrawal, and verify Bank = Stock + Wages + Sundry.",
            "tier_2": f"Bank total = {stock_amt} + {wages_amt} + {draw_amt} = {bank_tot}.",
            "tier_3": sample,
        },
        marking_points=[
            {"id": "mp_1", "desc": f"CHQ 101 Stock ({stock_amt})", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": f"CHQ 102 Payee Cash & Wages ({wages_amt})", "marks": 3, "editable": True},
            {"id": "mp_3", "desc": f"EFT 103 Drawings ({draw_amt})", "marks": 2, "editable": True},
            {"id": "mp_4", "desc": f"Closing Totals balancing to Bank {bank_tot}", "marks": 4, "editable": True},
        ],
        misconception_tags=["writing_account_name_in_payee_column", "classifying_drawings_as_wages"],
    )


def arch_39_cpj_cross_check_missing_analysis_column_table(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = _trader_name(rng, sc)
    stock = rng.randint(14, 48) * 500
    wages = rng.randint(6, 18) * 500
    stat = rng.randint(3, 12) * 200
    sundry = rng.randint(8, 28) * 500
    bank = stock + wages + stat + sundry

    headers = ["CPJ Column", "Status", "Total Amount (R)"]
    rows = [
        [_cell("t0_r0_c0", "Trading Stock", "given", False), _cell("t0_r0_c1", "Given", "given", False), _cell("t0_r0_c2", str(stock), "given", False)],
        [_cell("t0_r1_c0", "Wages", "given", False), _cell("t0_r1_c1", "Enter missing total", "given", False), _cell("t0_r1_c2", "", "required", True)],
        [_cell("t0_r2_c0", "Stationery", "given", False), _cell("t0_r2_c1", "Given", "given", False), _cell("t0_r2_c2", str(stat), "given", False)],
        [_cell("t0_r3_c0", "Sundry Accounts", "given", False), _cell("t0_r3_c1", "Given", "given", False), _cell("t0_r3_c2", str(sundry), "given", False)],
        [_cell("t0_r4_c0", "Bank (Total Payments)", "given", False), _cell("t0_r4_c1", "Given", "given", False), _cell("t0_r4_c2", str(bank), "given", False)],
    ]
    correct_map = {"t0_r1_c2": str(wages)}
    cell_hints = {"t0_r1_c2": f"Bank ({bank}) - Trading Stock ({stock}) - Stationery ({stat}) - Sundry ({sundry}) = {wages}."}
    prompt = (
        f"In **{biz}**'s month-end CPJ summary, ink smudged the **Wages** column total.\n\n"
        f"Use the CPJ cross-check identity (`Bank = sum of all analysis & sundry columns`) to solve the missing **Wages** total below (digits only, no spaces or R)."
    )
    md = (
        "| CPJ Column | Status | Total Amount (R) |\n"
        "| --- | --- | --- |\n"
        f"| Trading Stock | Given | {_fmt_r(stock)} |\n"
        f"| **Wages** | **Calculated** | **{_fmt_r(wages)}** |\n"
        f"| Stationery | Given | {_fmt_r(stat)} |\n"
        f"| Sundry Accounts | Given | {_fmt_r(sundry)} |\n"
        f"| Bank (Total Payments) | Given | {_fmt_r(bank)} |"
    )
    sample = f"Missing Wages Total = {wages}"
    worked = (
        f"**CPJ Cross-Check Balancing Memorandum** [3 marks]\n\n{md}\n\n"
        f"Working: `{_fmt_r(bank)} - ({_fmt_r(stock)} + {_fmt_r(stat)} + {_fmt_r(sundry)}) = {_fmt_r(wages)}`"
    )
    return _build_table(
        rng,
        qid_prefix="g9_cc_39",
        subskill="39_cpj_cross_check_missing_analysis_column_table",
        title="CPJ Column Cross-Check Balancing Table",
        prompt=prompt,
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=sample,
        marks=3,
        hints={
            "tier_1": "The CPJ Bank total must equal the sum of all analysis columns plus Sundry Accounts.",
            "tier_2": f"Wages = {bank} - ({stock} + {stat} + {sundry}).",
            "tier_3": sample,
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Derives missing Wages = {_fmt_r(wages)}", "marks": 3, "editable": True},
        ],
        misconception_tags=["cpj_cross_check_arithmetic_error"],
    )


def arch_40_bank_balance_effect_crj_vs_cpj_net_cashflow(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = _trader_name(rng, sc)
    open_bal = rng.randint(18, 65) * 500
    crj_bank = rng.randint(25, 85) * 500
    cpj_bank = rng.randint(15, 70) * 500
    close_bal = open_bal + crj_bank - cpj_bank
    expected = str(close_bal)

    prompt = (
        f"At the start of the month, **{biz}** had a favourable Bank balance of **{_fmt_r(open_bal)}**. "
        f"At month-end, the **CRJ Bank column totalled {_fmt_r(crj_bank)}** and the **CPJ Bank column totalled {_fmt_r(cpj_bank)}**.\n\n"
        f"Calculate the **closing Bank balance** at the end of the month.\n"
        f"*(Enter digits without spaces or R.)*"
    )
    worked = (
        f"**Closing Bank Balance from Cash Journals** [3 marks]\n\n"
        f"- Opening Bank Balance (Dr): `{_fmt_r(open_bal)}`\n"
        f"- Add Total Cash Receipts (CRJ Bank): `+{_fmt_r(crj_bank)}`\n"
        f"- Less Total Cash Payments (CPJ Bank): `-{_fmt_r(cpj_bank)}`\n"
        f"- Closing Bank Balance = `{_fmt_r(open_bal)} + {_fmt_r(crj_bank)} - {_fmt_r(cpj_bank)} = {_fmt_r(close_bal)}` -> Answer: `{expected}`"
    )
    return _build_short(
        rng,
        qid_prefix="g9_cc_40",
        subskill="40_bank_balance_effect_crj_vs_cpj_net_cashflow",
        title="Net Cash Flow & Closing Bank Balance",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=worked,
        marks=3,
        hints={
            "tier_1": "CRJ increases Bank; CPJ decreases Bank.",
            "tier_2": f"Closing Bank = {_fmt_r(open_bal)} + {_fmt_r(crj_bank)} - {_fmt_r(cpj_bank)}.",
            "tier_3": f"Closing Bank = {expected}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": "Adds CRJ Bank receipts and subtracts CPJ Bank payments", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": f"Closing Bank = {_fmt_r(close_bal)}", "marks": 1, "editable": True},
        ],
        misconception_tags=["subtracting_crj_or_adding_cpj_to_bank"],
    )


def arch_41_visual_cheque_counterfoil_to_cpj_mapping(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = _trader_name(rng, sc)
    m_name, yr, _, _ = rng.choice(MONTH_YEARS)
    day = f"{rng.randint(2, 27):02d}"
    chq_no = f"CHQ {rng.randint(204, 495)}"
    scenario = rng.choice([
        (sc["supplier"], "Merchandise for resale", "Trading Stock column", rng.randint(16, 48) * 250),
        ("Cash", "Weekly staff wages", "Wages column", rng.randint(8, 22) * 200),
        ("Palesa Furnishers", "New shop display counters (Equipment)", "Sundry Accounts (Equipment)", rng.randint(12, 36) * 500),
    ])
    payee, purpose, target_col, amt = scenario
    svg = _source_doc_svg(
        f"CHEQUE COUNTERFOIL — {biz.upper()}",
        chq_no,
        f"{day} {m_name} {yr}",
        [
            ("To", payee),
            ("For", purpose),
            ("This Cheque", _fmt_r(amt)),
        ],
        accent="#b45309",
    )
    prompt = (
        f"Examine the **Cheque Counterfoil** above from **{biz}**.\n\n"
        f"Which CPJ recording option is completely accurate for document **{chq_no}**?"
    )
    correct = f"Record {chq_no}, Payee '{payee}', Bank {_fmt_r(amt)}, and allocate {_fmt_r(amt)} to {target_col}."
    distractors = [
        f"Record {chq_no} in the Cash Receipts Journal under Analysis of Receipts and Sales ({_fmt_r(amt)}).",
        f"Record Payee '{purpose}', leave Bank blank, and enter {_fmt_r(amt)} in Cost of Sales.",
        f"Enter {_fmt_r(amt)} into both Trading Stock and Wages simultaneously to preserve double entry.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g9_cc_41",
        subskill="41_visual_cheque_counterfoil_to_cpj_mapping",
        title="Map Cheque Counterfoil to CPJ Columns",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"A Cheque Counterfoil proves cash left the bank (**CPJ**). Use `Doc. No.: {chq_no}`, `Name of Payee: {payee}`, "
            f"`Bank: {_fmt_r(amt)}`, and allocate **{_fmt_r(amt)}** to **{target_col}**."
        ),
        hints={
            "tier_1": "Cheque counterfoils always belong in the CPJ; check 'For' to pick the allocation column.",
            "tier_2": f"Purpose '{purpose}' belongs in {target_col}, with Bank credited {_fmt_r(amt)}.",
            "tier_3": correct,
        },
        misconception_tags=["cpj_column_classification_error"],
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    )


def arch_42_diagnose_crj_bank_includes_cost_of_sales_error(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = _trader_name(rng, sc)
    sales = rng.randint(20, 60) * 500
    cos = sales * 100 // 125
    sundry = rng.randint(8, 24) * 500
    true_bank = sales + sundry
    wrong_bank = true_bank + cos
    expected = str(true_bank)

    prompt = (
        f"A trainee bookkeeper at **{biz}** tries to cross-check the CRJ totals:\n"
        f"- `Sales`: {_fmt_r(sales)}\n"
        f"- `Cost of Sales`: {_fmt_r(cos)}\n"
        f"- `Sundry Accounts`: {_fmt_r(sundry)}\n\n"
        f"They erroneously wrote **{_fmt_r(wrong_bank)}** as the `Bank` total by including `Cost of Sales`. "
        f"Calculate the **corrected CRJ Bank total**.\n*(Enter digits without spaces or R.)*"
    )
    worked = (
        f"**CRJ Bank Cross-Check Error Correction** [3 marks]\n\n"
        f"- Cost of Sales (`{_fmt_r(cos)}`) is NOT cash received and must NEVER be added to Bank.\n"
        f"- Corrected CRJ Bank Total = `Sales + Sundry Accounts = {_fmt_r(sales)} + {_fmt_r(sundry)} = {_fmt_r(true_bank)}`\n"
        f"- Equivalently: `{_fmt_r(wrong_bank)} - {_fmt_r(cos)} = {_fmt_r(true_bank)}` -> Answer: `{expected}`"
    )
    return _build_short(
        rng,
        qid_prefix="g9_cc_42",
        subskill="42_diagnose_crj_bank_includes_cost_of_sales_error",
        title="Correct CRJ Bank Total Overstatement Error",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=worked,
        marks=3,
        hints={
            "tier_1": "Remember Cost of Sales is a non-cash memo column and never adds to Bank.",
            "tier_2": f"True Bank = Sales ({_fmt_r(sales)}) + Sundry ({_fmt_r(sundry)}).",
            "tier_3": f"Corrected Bank = {expected}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": "Excludes Cost of Sales from Bank total", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": f"Corrected Bank = {_fmt_r(true_bank)}", "marks": 2, "editable": True},
        ],
        misconception_tags=["adding_cost_of_sales_to_bank_total"],
    )


def arch_43_diagnose_analysis_of_receipts_double_banking_error(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = _trader_name(rng, sc)
    eft_amt = rng.randint(18, 60) * 1000
    r1 = rng.randint(8, 25) * 100
    r2 = rng.randint(6, 18) * 100
    banked = r1 + r2

    variants = [
        (
            f"entered a direct EFT Capital deposit of {_fmt_r(eft_amt)} into Analysis of Receipts AND wrote it in Bank on the same line, while till receipts of {_fmt_r(r1)} and {_fmt_r(r2)} were also banked on separate lines the same day",
            f"Direct EFT deposits never belong in Analysis of Receipts (only till cash goes there), and same-day till cash ({_fmt_r(r1)} + {_fmt_r(r2)}) should be banked as ONE daily deposit of {_fmt_r(banked)}.",
            [
                f"Both direct EFTs and till cash should be multiplied by 2 in Analysis of Receipts before entering Bank.",
                f"Rent and Capital receipts must be entered into the Cash Payments Journal instead of CRJ.",
                f"Same-day till receipts must never appear in Analysis of Receipts and should replace Cost of Sales.",
            ],
        ),
        (
            f"added the Analysis of Receipts column total ({_fmt_r(r1 + r2)}) to the Bank column total ({_fmt_r(eft_amt + banked)}) when reconciling cash deposited",
            "Analysis of Receipts is only a daily till-holding subtotal that gets carried into Bank at day-end; adding both totals counts till cash twice.",
            [
                "Analysis of Receipts tracks unpaid credit sales, so it always equals Creditors Control.",
                "Bank must always equal Analysis of Receipts minus Sales.",
                "Adding Analysis and Bank together adjusts for mark-up on stock sold.",
            ],
        ),
    ]
    mistake, correct, distractors = rng.choice(variants)
    prompt = (
        f"While auditing **{biz}**'s CRJ, you notice the bookkeeper {mistake}.\n\n"
        f"Which diagnosis correctly explains the bookkeeper's mistake?"
    )
    return _build_mcq(
        rng,
        qid_prefix="g9_cc_43",
        subskill="43_diagnose_analysis_of_receipts_double_banking_error",
        title="Diagnose Analysis of Receipts & Banking Errors",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=f"**Diagnosis:** {correct}",
        hints={
            "tier_1": "Consider how Analysis of Receipts feeds into Bank without duplicating money.",
            "tier_2": "Till cash flows Analysis -> combined daily Bank; direct EFT skips Analysis completely.",
            "tier_3": correct,
        },
        misconception_tags=["entering_direct_eft_in_analysis_of_receipts", "banking_each_till_receipt_separately"],
    )


def arch_44_classifying_sundry_vs_analysis_column_accounts_table(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = _trader_name(rng, sc)
    pool = [
        ("Cash sales of merchandise per CRR", "CRJ", "Sales & Cost of Sales"),
        ("Monthly shop rent received from tenant", "CRJ", "Sundry Accounts"),
        ("Merchandise purchased for resale by EFT", "CPJ", "Trading Stock"),
        ("Weekly wages drawn over the counter", "CPJ", "Wages"),
        ("Owner takes cash EFT for personal family holiday", "CPJ", "Sundry Accounts"),
        ("New cash register equipment bought by cheque", "CPJ", "Sundry Accounts"),
    ]
    chosen = rng.sample(pool, 5)
    headers = ["Transaction Description", "Journal (CRJ / CPJ)", "Target Column (`Sales & Cost of Sales`, `Trading Stock`, `Wages`, `Sundry Accounts`)"]
    rows: List[List[Dict[str, Any]]] = []
    correct_map: Dict[str, str] = {}
    cell_hints: Dict[str, str] = {}
    md_lines = ["| Transaction Description | Journal | Target Column |", "| --- | --- | --- |"]

    for i, (desc, jnl, col) in enumerate(chosen):
        correct_map[f"t0_r{i}_c1"] = jnl
        correct_map[f"t0_r{i}_c2"] = col
        cell_hints[f"t0_r{i}_c1"] = f"Cash received -> CRJ; Cash paid -> CPJ."
        cell_hints[f"t0_r{i}_c2"] = f"Exact column match from prompt list: '{col}'."
        rows.append([
            _cell(f"t0_r{i}_c0", desc, "given", False),
            _cell(f"t0_r{i}_c1", "", "required", True),
            _cell(f"t0_r{i}_c2", "", "required", True),
        ])
        md_lines.append(f"| {desc} | **{jnl}** | **{col}** |")

    prompt = (
        f"**{biz}** maintains CRJ analysis columns (`Sales`, `Cost of Sales`, `Sundry Accounts`) and CPJ analysis columns (`Trading Stock`, `Wages`, `Sundry Accounts`).\n\n"
        f"Classify each transaction below by Journal (`CRJ` or `CPJ`) and Target Column (`Sales & Cost of Sales`, `Trading Stock`, `Wages`, or `Sundry Accounts`)."
    )
    sample = "; ".join(f"{desc}: {jnl} -> {col}" for desc, jnl, col in chosen)
    worked = "**CRJ & CPJ Column Allocation Memorandum** [10 marks]\n\n" + "\n".join(md_lines)
    return _build_table(
        rng,
        qid_prefix="g9_cc_44",
        subskill="44_classifying_sundry_vs_analysis_column_accounts_table",
        title="Classify Cash Transactions by Journal & Column",
        prompt=prompt,
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=sample,
        marks=10,
        hints={
            "tier_1": "Inflows -> CRJ, Outflows -> CPJ; occasional accounts go to Sundry Accounts.",
            "tier_2": "Use 'Sales & Cost of Sales', 'Trading Stock', 'Wages', or 'Sundry Accounts'.",
            "tier_3": sample,
        },
        marking_points=[{"id": f"mp_{i}", "desc": f"{desc}: {jnl} ({col})", "marks": 2, "editable": True} for i, (desc, jnl, col) in enumerate(chosen)],
        misconception_tags=["cpj_column_classification_error"],
    )


def arch_45_cash_float_establishment_and_increase_cpj(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = _trader_name(rng, sc)
    amt = rng.randint(5, 25) * 100

    prompt = (
        f"To ensure change is available in the shop till on opening day, **{biz}** cashes a cheque for **{_fmt_r(amt)}** to establish a **Cash Float**.\n\n"
        f"How is this transaction recorded in the **CPJ** and on the **Accounting Equation (`A = OE + L`)**?"
    )
    correct = f"CPJ with Payee 'Cash', Bank {_fmt_r(amt)}, Sundry Accounts -> Cash Float {_fmt_r(amt)}; Assets change net 0 (+{_fmt_r(amt)} Cash Float, -{_fmt_r(amt)} Bank)."
    distractors = [
        f"CRJ with Payee '{sc['entrepreneur']}', Sales {_fmt_r(amt)}; Assets +{_fmt_r(amt)}, Owner's Equity +{_fmt_r(amt)}.",
        f"CPJ under Trading Stock {_fmt_r(amt)}; Owner's Equity decreases by -{_fmt_r(amt)}.",
        f"CPJ under Wages {_fmt_r(amt)}; Assets decrease by -{_fmt_r(amt)} and Liabilities decrease by -{_fmt_r(amt)}.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g9_cc_45",
        subskill="45_cash_float_establishment_and_increase_cpj",
        title="Establishing Cash Float: CPJ & Accounting Equation",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"Cash Float is cash kept on site in the shop till (an **Asset**). Cashing a cheque (`Payee: Cash`) transfers money from **Bank** (Asset -) into **Cash Float** (Asset +) "
            f"via **CPJ Sundry Accounts (`Cash Float`)**, leaving net Assets = 0 and Owner's Equity unchanged."
        ),
        hints={
            "tier_1": "Cash moves out of the business Bank account into the physical shop till (Cash Float).",
            "tier_2": "Both Bank and Cash Float are Assets, so total Assets stay balanced (0 net change).",
            "tier_3": correct,
        },
        misconception_tags=["treating_cash_float_as_expense"],
    )


def arch_46_crj_and_cpj_owner_drawings_cash_vs_goods(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = _trader_name(rng, sc)
    amt = rng.randint(8, 35) * 150

    prompt = (
        f"**{sc['entrepreneur']}**, sole proprietor of **{biz}**, draws **{_fmt_r(amt)}** via business EFT to pay for personal family groceries.\n\n"
        f"Why must this **NEVER** be recorded in the **CRJ**, **Wages**, or **Trading Stock** columns?"
    )
    correct = "Because cash withdrawn by the owner for private use decreases Bank and Owner's Equity, so it belongs strictly in CPJ Sundry Accounts under Drawings."
    distractors = [
        "Because the owner is considered an employee of the sole trader, making it part of monthly Wages.",
        "Because personal drawings count as cash sales at 0% profit mark-up in the CRJ.",
        "Because sole proprietors can offset personal groceries against Trading Stock without journal entries.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g9_cc_46",
        subskill="46_crj_and_cpj_owner_drawings_cash_vs_goods",
        title="Owner Drawings: Business Entity Concept in CPJ",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"Under the **business entity rule**, owner's personal transactions are kept separate from business operating expenses and trading stock. "
            f"Cash paid for the owner's benefit (**{_fmt_r(amt)}**) is recorded in **CPJ -> Bank & Sundry Accounts (`Drawings`)**."
        ),
        hints={
            "tier_1": "Recall the accounting entity principle separating the owner's private life from business operations.",
            "tier_2": "Owner withdrawals reduce cash (CPJ) and Equity via Drawings in Sundry Accounts.",
            "tier_3": correct,
        },
        misconception_tags=["classifying_drawings_as_wages"],
    )


def arch_47_trade_discount_vs_cash_discount_at_purchase(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = _trader_name(rng, sc)
    catalogue_price = rng.randint(15, 50) * 400
    trade_disc = rng.choice([10, 15, 20])
    after_trade = catalogue_price * (100 - trade_disc) // 100
    cash_disc = rng.choice([5, 10])
    net_paid = after_trade * (100 - cash_disc) // 100
    expected = str(net_paid)

    prompt = (
        f"**{sc['supplier']}** quotes trading stock at a list price of **{_fmt_r(catalogue_price)}** less a **{trade_disc}% trade discount**, "
        f"plus an additional **{cash_disc}% cash discount** on the discounted amount when **{biz}** pays immediately by EFT.\n\n"
        f"Calculate the **net amount entered in the CPJ Bank and Trading Stock columns**.\n"
        f"*(Enter digits without spaces or R.)*"
    )
    worked = (
        f"**Sequential Trade & Cash Discount CPJ Calculation** [3 marks]\n\n"
        f"1. After {trade_disc}% trade discount: `{_fmt_r(catalogue_price)} × {100 - trade_disc}/100 = {_fmt_r(after_trade)}`\n"
        f"2. After {cash_disc}% cash discount on the net invoice: `{_fmt_r(after_trade)} × {100 - cash_disc}/100 = {_fmt_r(net_paid)}`\n"
        f"- Enter `{_fmt_r(net_paid)}` in CPJ `Bank` and `Trading Stock` -> Answer: `{expected}`"
    )
    return _build_short(
        rng,
        qid_prefix="g9_cc_47",
        subskill="47_trade_discount_vs_cash_discount_at_purchase",
        title="Sequential Trade & Cash Discounts in CPJ",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=worked,
        marks=3,
        hints={
            "tier_1": "Apply the trade discount first, then take the cash discount on the reduced invoice total (do NOT add the percentages!).",
            "tier_2": f"After {trade_disc}% = {_fmt_r(after_trade)}; then less {cash_disc}% = {_fmt_r(after_trade)} × {100 - cash_disc}/100.",
            "tier_3": f"Net CPJ entry = {expected}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Invoice after {trade_disc}% trade discount = {_fmt_r(after_trade)}", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": f"Net after {cash_disc}% cash discount = {_fmt_r(net_paid)}", "marks": 2, "editable": True},
        ],
        misconception_tags=["adding_trade_and_cash_discount_percentages"],
    )


def arch_48_accounting_equation_loan_receipt_and_repayment(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = _trader_name(rng, sc)
    loan_amt = rng.randint(40, 120) * 1000
    repay_amt = rng.randint(3, 12) * 1000

    headers = ["Transaction", "Journal", "Account Debited", "Account Credited", "Assets", "Owner's Equity", "Liabilities"]
    rows = [
        [
            _cell("t0_r0_c0", f"Receive loan {_fmt_r(loan_amt)}", "given", False),
            _cell("t0_r0_c1", "", "required", True),
            _cell("t0_r0_c2", "", "required", True),
            _cell("t0_r0_c3", "Loan", "given", False),
            _cell("t0_r0_c4", "", "required", True),
            _cell("t0_r0_c5", "0", "given", False),
            _cell("t0_r0_c6", f"+{loan_amt}", "given", False),
        ],
        [
            _cell("t0_r1_c0", f"Repay capital {_fmt_r(repay_amt)}", "given", False),
            _cell("t0_r1_c1", "", "required", True),
            _cell("t0_r1_c2", "Loan", "given", False),
            _cell("t0_r1_c3", "", "required", True),
            _cell("t0_r1_c4", "", "required", True),
            _cell("t0_r1_c5", "0", "given", False),
            _cell("t0_r1_c6", f"-{repay_amt}", "given", False),
        ],
    ]
    correct_map = {
        "t0_r0_c1": "CRJ",
        "t0_r0_c2": "Bank",
        "t0_r0_c4": f"+{loan_amt}",
        "t0_r1_c1": "CPJ",
        "t0_r1_c3": "Bank",
        "t0_r1_c4": f"-{repay_amt}",
    }
    cell_hints = {
        "t0_r0_c1": "Money received into bank uses CRJ.",
        "t0_r0_c2": "Bank increases (Debit).",
        "t0_r0_c4": f"+{loan_amt} Bank (no spaces or R).",
        "t0_r1_c1": "Money paid out of bank uses CPJ.",
        "t0_r1_c3": "Bank decreases (Credit).",
        "t0_r1_c4": f"-{repay_amt} Bank (include minus sign, no spaces or R).",
    }
    prompt = (
        f"**{biz}** receives a business bank loan of **{_fmt_r(loan_amt)}** directly into its account, "
        f"and later repays **{_fmt_r(repay_amt)}** of the loan capital by EFT.\n\n"
        f"Complete the Accounting Equation table below (`CRJ`/`CPJ`, accounts, and `+/-` Assets effects without spaces or R)."
    )
    md = (
        "| Transaction | Journal | Account Debited | Account Credited | Assets | Owner's Equity | Liabilities |\n"
        "| --- | --- | --- | --- | --- | --- | --- |\n"
        f"| Receive loan {_fmt_r(loan_amt)} | **CRJ** | **Bank** | Loan | **+{loan_amt}** | 0 | +{loan_amt} |\n"
        f"| Repay capital {_fmt_r(repay_amt)} | **CPJ** | Loan | **Bank** | **-{repay_amt}** | 0 | -{repay_amt} |"
    )
    sample = f"Receipt: CRJ Dr Bank, Cr Loan, A +{loan_amt}, L +{loan_amt}; Repayment: CPJ Dr Loan, Cr Bank, A -{repay_amt}, L -{repay_amt}"
    worked = f"**Loan Receipt & Repayment Accounting Equation** [6 marks]\n\n{md}"
    return _build_table(
        rng,
        qid_prefix="g9_cc_48",
        subskill="48_accounting_equation_loan_receipt_and_repayment",
        title="Loan Receipt (CRJ) & Repayment (CPJ) Equation",
        prompt=prompt,
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=sample,
        marks=6,
        hints={
            "tier_1": "Loan inflows enter CRJ (+A, +L); loan repayments enter CPJ (-A, -L); neither alters Owner's Equity.",
            "tier_2": f"Line 1: CRJ, Bank, +{loan_amt}; Line 2: CPJ, Bank, -{repay_amt}.",
            "tier_3": sample,
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Loan receipt CRJ, Bank, +{loan_amt}", "marks": 3, "editable": True},
            {"id": "mp_2", "desc": f"Loan repayment CPJ, Bank, -{repay_amt}", "marks": 3, "editable": True},
        ],
        misconception_tags=["treating_loan_as_income_or_expense"],
    )


def arch_49_visual_trading_cash_cycle_flow(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = _trader_name(rng, sc)
    stock_cost = rng.randint(15, 45) * 400
    markup = rng.choice([25, 40, 50])
    half_cost = stock_cost // 2
    cash_sales = half_cost * (100 + markup) // 100
    gross_profit = cash_sales - half_cost

    svg = (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 175" width="600" height="175">'
        '<rect x="4" y="4" width="592" height="167" rx="8" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5"/>'
        f'<text x="300" y="26" font-size="12.5" font-weight="bold" text-anchor="middle" fill="#0f172a">Sole-Trader Cash Cycle — {biz}</text>'
        '<rect x="20" y="46" width="155" height="95" rx="8" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>'
        '<text x="97" y="68" font-size="11" font-weight="bold" text-anchor="middle" fill="#92400e">1. CPJ Stock Purchase</text>'
        f'<text x="97" y="92" font-size="12" font-weight="bold" text-anchor="middle" fill="#0f172a">{_fmt_r(stock_cost)}</text>'
        '<text x="97" y="114" font-size="10" text-anchor="middle" fill="#475569">Bank - | Trading Stock +</text>'
        '<path d="M 180 94 L 210 94" stroke="#475569" stroke-width="2" marker-end="url(#arrow)"/>'
        '<rect x="215" y="46" width="165" height="95" rx="8" fill="#e0f2fe" stroke="#0284c7" stroke-width="1.5"/>'
        '<text x="297" y="68" font-size="11" font-weight="bold" text-anchor="middle" fill="#075985">2. Sell 50% of Stock</text>'
        f'<text x="297" y="92" font-size="11.5" font-weight="bold" text-anchor="middle" fill="#0f172a">Mark-up: {markup}% on cost</text>'
        f'<text x="297" y="114" font-size="10" text-anchor="middle" fill="#475569">Cost Sold: {_fmt_r(half_cost)}</text>'
        '<path d="M 385 94 L 415 94" stroke="#475569" stroke-width="2" marker-end="url(#arrow)"/>'
        '<rect x="420" y="46" width="160" height="95" rx="8" fill="#dcfce7" stroke="#16a34a" stroke-width="1.5"/>'
        '<text x="500" y="68" font-size="11" font-weight="bold" text-anchor="middle" fill="#166534">3. CRJ Cash Sale</text>'
        f'<text x="500" y="92" font-size="12" font-weight="bold" text-anchor="middle" fill="#0f172a">Sales: {_fmt_r(cash_sales)}</text>'
        '<text x="500" y="114" font-size="10" text-anchor="middle" fill="#475569">Bank + | Sales +</text>'
        '<defs><marker id="arrow" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">'
        '<path d="M0,0 L0,6 L6,3 z" fill="#475569"/></marker></defs></svg>'
    )
    expected = str(gross_profit)
    prompt = (
        f"Follow the three stages in the **Sole-Trader Cash Cycle** shown above for **{biz}**.\n\n"
        f"Calculate the **Gross Profit** earned after selling 50% of the purchased stock in Stage 3.\n"
        f"*(Enter digits without spaces or R.)*"
    )
    worked = (
        f"**Cash Cycle Gross Profit Calculation** [3 marks]\n\n"
        f"- Stage 1 CPJ Stock bought: `{_fmt_r(stock_cost)}`\n"
        f"- Stage 2 Cost of half the stock sold (`Cost of Sales`): `{_fmt_r(half_cost)}`\n"
        f"- Stage 3 CRJ Cash Sales (`+{markup}%`): `{_fmt_r(cash_sales)}`\n"
        f"- Gross Profit = `Sales - Cost of Sales = {_fmt_r(cash_sales)} - {_fmt_r(half_cost)} = {_fmt_r(gross_profit)}` -> Answer: `{expected}`"
    )
    return _build_short(
        rng,
        qid_prefix="g9_cc_49",
        subskill="49_visual_trading_cash_cycle_flow",
        title="Sole-Trader Cash Cycle Gross Profit Analysis",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=worked,
        marks=3,
        hints={
            "tier_1": "Gross Profit equals CRJ Cash Sales minus the Cost of Sales of the stock actually sold.",
            "tier_2": f"Sales = {_fmt_r(cash_sales)}, Cost of Sales = {_fmt_r(half_cost)}.",
            "tier_3": f"Gross Profit = {expected}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Subtracts {_fmt_r(half_cost)} from {_fmt_r(cash_sales)} = {_fmt_r(gross_profit)}", "marks": 3, "editable": True},
        ],
        misconception_tags=["subtracting_total_purchases_instead_of_cost_of_sales"],
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    )


def arch_50_comprehensive_crj_cpj_reconciliation_audit(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = _trader_name(rng, sc)
    open_bank = rng.randint(15, 50) * 1000
    markup = rng.choice([25, 50])
    crj_cos = rng.randint(12, 36) * 200
    crj_sales = crj_cos * (100 + markup) // 100
    crj_sundry = rng.randint(6, 20) * 500
    crj_bank = crj_sales + crj_sundry

    cpj_stock = rng.randint(14, 42) * 200
    cpj_wages = rng.randint(6, 18) * 250
    cpj_sundry = rng.randint(4, 14) * 250
    cpj_bank = cpj_stock + cpj_wages + cpj_sundry

    close_bank = open_bank + crj_bank - cpj_bank
    gross_profit = crj_sales - crj_cos

    headers = ["Reconciliation Metric", "Formula / Given Basis", "Rand Amount (R)"]
    specs = [
        ("CRJ Sales Total", "Given", str(crj_sales), False),
        (f"CRJ Cost of Sales ({markup}% mark-up)", "Derived from Sales", str(crj_cos), True),
        ("CRJ Sundry Accounts Total", "Given", str(crj_sundry), False),
        ("CRJ Bank Total (Cash Receipts)", "Sales + Sundry", str(crj_bank), True),
        ("CPJ Trading Stock + Wages + Sundry", f"{cpj_stock} + {cpj_wages} + {cpj_sundry}", str(cpj_bank), True),
        (f"Closing Bank Balance (Opening {_fmt_r(open_bank)})", "Opening + CRJ Bank - CPJ Bank", str(close_bank), True),
    ]
    rows: List[List[Dict[str, Any]]] = []
    correct_map: Dict[str, str] = {}
    cell_hints: Dict[str, str] = {}
    md_lines = ["| Reconciliation Metric | Formula / Given Basis | Rand Amount (R) |", "| --- | --- | --- |"]

    for i, (metric, basis, val, ed) in enumerate(specs):
        if ed:
            correct_map[f"t0_r{i}_c2"] = val
            cell_hints[f"t0_r{i}_c2"] = f"Calculate {metric}: {basis} (digits only, no spaces or R)."
        rows.append([
            _cell(f"t0_r{i}_c0", metric, "given", False),
            _cell(f"t0_r{i}_c1", basis, "given", False),
            _cell(f"t0_r{i}_c2", "" if ed else val, "required" if ed else "given", ed),
        ])
        md_lines.append(f"| {metric} | {basis} | **{_fmt_r(int(val))}** |" if ed else f"| {metric} | {basis} | {_fmt_r(int(val))} |")

    prompt = (
        f"Audit the combined month-end **CRJ & CPJ Reconciliation Summary** for **{biz}** "
        f"(Opening Bank: **{_fmt_r(open_bank)}**; mark-up **{markup}% on cost**; enter digits without spaces or R)."
    )
    sample = f"CRJ COS {crj_cos}, CRJ Bank {crj_bank}, CPJ Bank {cpj_bank}, Closing Bank {close_bank} (Gross Profit {gross_profit})"
    worked = (
        f"**Comprehensive CRJ & CPJ Reconciliation Audit** [8 marks]\n\n"
        + "\n".join(md_lines)
        + f"\n\n- Gross Profit for the month = `{_fmt_r(crj_sales)} - {_fmt_r(crj_cos)} = {_fmt_r(gross_profit)}`"
    )
    return _build_table(
        rng,
        qid_prefix="g9_cc_50",
        subskill="50_comprehensive_crj_cpj_reconciliation_audit",
        title="Comprehensive CRJ & CPJ Reconciliation Audit",
        prompt=prompt,
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=sample,
        marks=8,
        hints={
            "tier_1": "Work top-to-bottom: Cost of Sales -> CRJ Bank (excluding COS) -> CPJ Bank -> Closing Bank.",
            "tier_2": f"COS = {crj_cos}; CRJ Bank = {crj_bank}; CPJ Bank = {cpj_bank}.",
            "tier_3": sample,
        },
        marking_points=[
            {"id": "mp_1", "desc": f"CRJ Cost of Sales = {crj_cos}", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": f"CRJ Bank = {crj_bank}", "marks": 2, "editable": True},
            {"id": "mp_3", "desc": f"CPJ Bank = {cpj_bank}", "marks": 2, "editable": True},
            {"id": "mp_4", "desc": f"Closing Bank Balance = {close_bank}", "marks": 2, "editable": True},
        ],
        misconception_tags=["adding_cost_of_sales_to_bank_total", "subtracting_crj_or_adding_cpj_to_bank"],
    )


BUILDERS_26_50 = {
    "26_crj_capital_contribution_and_cash_sales_entry": arch_26_crj_capital_contribution_and_cash_sales_entry,
    "27_crj_daily_banking_two_receipts_same_day": arch_27_crj_daily_banking_two_receipts_same_day,
    "28_crj_direct_deposit_plus_till_cash_same_month": arch_28_crj_direct_deposit_plus_till_cash_same_month,
    "29_crj_full_multi_transaction_journal_completion": arch_29_crj_full_multi_transaction_journal_completion,
    "30_crj_cash_sales_with_varied_markup_and_totals": arch_30_crj_cash_sales_with_varied_markup_and_totals,
    "31_cpj_column_structure_and_source_docs": arch_31_cpj_column_structure_and_source_docs,
    "32_cpj_cash_payee_for_wages_and_cash_float": arch_32_cpj_cash_payee_for_wages_and_cash_float,
    "33_cpj_split_cheque_trading_stock_and_stationery": arch_33_cpj_split_cheque_trading_stock_and_stationery,
    "34_cpj_split_cheque_business_and_owner_drawings": arch_34_cpj_split_cheque_business_and_owner_drawings,
    "35_cpj_fixed_asset_purchase_equipment_or_vehicles": arch_35_cpj_fixed_asset_purchase_equipment_or_vehicles,
    "36_cpj_trading_stock_and_carriage_on_purchases": arch_36_cpj_trading_stock_and_carriage_on_purchases,
    "37_cpj_wages_increase_calculation_and_entry": arch_37_cpj_wages_increase_calculation_and_entry,
    "38_cpj_full_multi_transaction_journal_completion": arch_38_cpj_full_multi_transaction_journal_completion,
    "39_cpj_cross_check_missing_analysis_column_table": arch_39_cpj_cross_check_missing_analysis_column_table,
    "40_bank_balance_effect_crj_vs_cpj_net_cashflow": arch_40_bank_balance_effect_crj_vs_cpj_net_cashflow,
    "41_visual_cheque_counterfoil_to_cpj_mapping": arch_41_visual_cheque_counterfoil_to_cpj_mapping,
    "42_diagnose_crj_bank_includes_cost_of_sales_error": arch_42_diagnose_crj_bank_includes_cost_of_sales_error,
    "43_diagnose_analysis_of_receipts_double_banking_error": arch_43_diagnose_analysis_of_receipts_double_banking_error,
    "44_classifying_sundry_vs_analysis_column_accounts_table": arch_44_classifying_sundry_vs_analysis_column_accounts_table,
    "45_cash_float_establishment_and_increase_cpj": arch_45_cash_float_establishment_and_increase_cpj,
    "46_crj_and_cpj_owner_drawings_cash_vs_goods": arch_46_crj_and_cpj_owner_drawings_cash_vs_goods,
    "47_trade_discount_vs_cash_discount_at_purchase": arch_47_trade_discount_vs_cash_discount_at_purchase,
    "48_accounting_equation_loan_receipt_and_repayment": arch_48_accounting_equation_loan_receipt_and_repayment,
    "49_visual_trading_cash_cycle_flow": arch_49_visual_trading_cash_cycle_flow,
    "50_comprehensive_crj_cpj_reconciliation_audit": arch_50_comprehensive_crj_cpj_reconciliation_audit,
}
