"""Grade 9 EMS - Credit Transactions (Creditors 1): Archetypes 26 to 50.

Grounded strictly in:
- curriculum_docs_auto/EMS_Gr9/Term 3/01. Credit transactions (Creditors 1).md
- curriculum_docs/EMS_Gr9/Term 3/10-Credit transactions Creditors (1).md
- curriculum_docs_auto/EMS_Gr9/Term 3/01. Credit transactions (Debtors 2).md (Lesson 6 Creditors Journal)

Zero-LLM, 100% deterministic, authentic South African Rand (R) sole-trader contexts.
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Tuple

from app.utils.ems_namelist import get_ems_scenario

from .term3_creditors_journal_archetypes_01_25 import (
    CAJ_HEADERS,
    CJ_HEADERS,
    CREDITOR_POOL,
    CURRICULUM_REFERENCE,
    MONTH_DATA,
    STOCK_LINES,
    SUBTOPIC_ID,
    SUNDRY_ITEMS,
    TOPIC_ID,
    TOPIC_NAME,
    biz_name,
    build_mcq,
    build_short,
    build_table,
    fmt_cell,
    fmt_r,
    make_grid_rows,
    pick_creditors,
)


def arch_26_caj_trade_discount_proportional_return_calc(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    sup, _ = rng.choice(CREDITOR_POOL)
    pct = rng.choice([5, 10, 12.5, 15, 20])
    pct_str = f"{pct}".replace(".", ",")
    gross_return = rng.randint(4, 20) * 800
    disc_amt = int(round(gross_return * pct / 100))
    net_allowance = gross_return - disc_amt

    prompt = (
        f"**{biz}** returns damaged stock with a catalogue (list) price of **{fmt_r(gross_return)}** to **{sup}**.\n\n"
        f"When originally purchased, {sup} had granted a **{pct_str}% trade discount**.\n\n"
        f"Calculate the **net allowance amount** to record in the **Creditors Allowance Journal (CAJ)** "
        f"(plain number without R or spaces)."
    )
    worked = (
        f"**{fmt_r(net_allowance)}** (`{net_allowance}`) [3 marks]\n\n"
        f"- **Accounting Rule**: Returns must be valued at the **actual price billed** (net after trade discount), "
        f"not the catalogue price.\n"
        f"- **Trade Discount Adjustment**: ${fmt_r(gross_return)} \\times {pct_str}\\% = {fmt_r(disc_amt)}$ [1 mark]\n"
        f"- **Net CAJ Entry**: ${fmt_r(gross_return)} - {fmt_r(disc_amt)} = {fmt_r(net_allowance)}$ (`{net_allowance}`) [2 marks]."
    )
    hints = {
        "tier_1": f"The supplier only charged the net price when selling; you must deduct the same {pct_str}% discount on returns.",
        "tier_2": f"Net return = List price x (100% - {pct_str}%).",
        "tier_3": f"{gross_return} - ({gross_return} x {pct}/100) = {net_allowance}.",
    }
    return build_short(
        rng, qid="g9_cj_26", subskill="26_caj_trade_discount_proportional_return_calc",
        title="Calculate Net Return Value After Trade Discount in CAJ",
        prompt=prompt, expected_answer=str(net_allowance), worked_solution=worked, hints=hints,
        marking_points=[
            {"id": "mp_1", "desc": f"Calculates proportional {pct_str}% discount = {fmt_r(disc_amt)}", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": f"Subtracts to get net allowance {fmt_r(net_allowance)}", "marks": 2, "editable": True},
        ],
        misconception_tags=["recorded_gross_return_in_caj"],
        marks=3, qtype="math_short",
    )


def arch_27_caj_complete_3row_table(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    month, year, _ = rng.choice(MONTH_DATA)
    creds = pick_creditors(rng, 3)
    days = sorted(rng.sample(range(6, 28), 3))

    r1_ts = rng.randint(4, 15) * 150  # Trading stock return
    r2_st = rng.randint(3, 10) * 100  # Stationery allowance
    r3_sun = rng.randint(5, 16) * 150  # Packing material / Equipment allowance

    tot_ts = r1_ts
    tot_st = r2_st
    tot_sun = r3_sun
    tot_cc = tot_ts + tot_st + tot_sun

    tx_list = [
        f"Day {days[0]}: Issued Debit Note DN1 to {creds[0][0]} for damaged trading stock returned, {fmt_r(r1_ts)}.",
        f"Day {days[1]}: Issued Debit Note DN2 to {creds[1][0]} for overcharge on office stationery invoice, {fmt_r(r2_st)}.",
        f"Day {days[2]}: Issued Debit Note DN3 to {creds[2][0]} for defective shop packing material returned, {fmt_r(r3_sun)}.",
    ]

    data_rows = [
        ["DN1", str(days[0]), creds[0][0], "C1", fmt_cell(r1_ts), fmt_cell(r1_ts), "", "", ""],
        ["DN2", str(days[1]), creds[1][0], "C2", fmt_cell(r2_st), "", fmt_cell(r2_st), "", ""],
        ["DN3", str(days[2]), creds[2][0], "C3", fmt_cell(r3_sun), "", "", fmt_cell(r3_sun), "Packing material"],
        ["", "", "Totals", "", fmt_cell(tot_cc), fmt_cell(tot_ts), fmt_cell(tot_st), fmt_cell(tot_sun), ""],
    ]
    given_coords = {(r, 0) for r in range(3)} | {(r, 1) for r in range(3)} | {(r, 3) for r in range(3)} | {(3, 2)}
    rows, cmap = make_grid_rows(data_rows, given_coords)
    cell_hints = {
        "t0_r1_c6": "Overcharge on stationery reduces Stationery expense in CAJ.",
        "t0_r2_c8": "Packing material is recorded in Sundry Accounts in CAJ.",
        "t0_r3_c4": "Creditors Control total in CAJ equals Trading Stock + Stationery + Sundry totals.",
    }

    prompt = (
        f"Record the following Debit Note transactions in the **Creditors Allowance Journal (CAJ)** of **{biz}** "
        f"for **{month} {year}**, and total all columns.\n\n"
        + "\n".join(f"- {t}" for t in tx_list)
        + "\n\nEnter amounts as plain digits without `R` or spaces; leave blank if a column does not apply."
    )
    worked = (
        f"**Creditors Allowance Journal of {biz} — {month} {year}** [14 marks]\n\n"
        "| Doc No | Day | Creditor | Fol | Creditors Control | Trading Stock | Stationery | Sundry Amount | Sundry Details |\n"
        "|---|---:|---|---|---:|---:|---:|---:|---|\n"
        f"| DN1 | {days[0]} | {creds[0][0]} | C1 | {fmt_cell(r1_ts)} | {fmt_cell(r1_ts)} | | | |\n"
        f"| DN2 | {days[1]} | {creds[1][0]} | C2 | {fmt_cell(r2_st)} | | {fmt_cell(r2_st)} | | |\n"
        f"| DN3 | {days[2]} | {creds[2][0]} | C3 | {fmt_cell(r3_sun)} | | | {fmt_cell(r3_sun)} | Packing material |\n"
        f"| | | **Totals** | | **{fmt_cell(tot_cc)}** | **{fmt_cell(tot_ts)}** | **{fmt_cell(tot_st)}** | **{fmt_cell(tot_sun)}** | |\n\n"
        f"- **Cross-check**: ${tot_ts} + {tot_st} + {tot_sun} = {tot_cc}$."
    )
    hints = {
        "tier_1": "Debit Notes reduce Creditors Control and the relevant asset/expense columns.",
        "tier_2": "Row 1 = Trading Stock, Row 2 = Stationery, Row 3 = Sundry Accounts (Packing material).",
        "tier_3": f"Totals: CC = {tot_cc}, TS = {tot_ts}, Stat = {tot_st}, Sundry = {tot_sun}.",
    }
    return build_table(
        rng, qid="g9_cj_27", subskill="27_caj_complete_3row_table",
        title="Complete 3-Row Creditors Allowance Journal (CAJ)",
        prompt=prompt, headers=CAJ_HEADERS, rows=rows, correct_map=cmap, cell_hints=cell_hints,
        worked_solution=worked, sample_answer=f"Total CAJ Creditors Control = {fmt_r(tot_cc)}.",
        marks=14, hints=hints, transactions=tx_list,
        marking_points=[{"id": "mp_1", "desc": "Accurately completes CAJ rows and Totals", "marks": 14, "editable": True}],
        misconception_tags=["caj_entered_in_cj", "sundry_details_omitted_in_caj"],
        journal_type="caj",
    )


def arch_28_caj_vs_cj_columns_comparison_table(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)

    features = [
        ("Primary purpose", "Records credit purchases from suppliers", "Records returns & allowances to suppliers"),
        ("Source document issued/received", "Original Invoice received (renumbered C1, C2...)", "Debit Note issued (DN1, DN2...)"),
        ("Effect on Creditors Control liability", "Increases liability (+)", "Decreases liability (-)"),
        ("Posting to Creditors Ledger", "Credited to Creditor's account (plus column)", "Debited to Creditor's account (minus column)"),
    ]
    rng.shuffle(features)

    headers = ["Feature", "Creditors Journal (CJ)", "Creditors Allowance Journal (CAJ)"]
    data_rows = [[feat, cj_val, caj_val] for feat, cj_val, caj_val in features]
    given_coords = {(r, 0) for r in range(4)}
    rows, cmap = make_grid_rows(data_rows, given_coords)
    cell_hints = {
        f"t0_r{r}_c1": "Describe the CJ rule or effect." for r in range(4)
    }

    prompt = (
        f"Compare the **Creditors Journal (CJ)** and the **Creditors Allowance Journal (CAJ)** for **{biz}** "
        f"by completing the missing cells in the comparison matrix below."
    )
    md_rows = "\n".join(f"| {f} | {a} | {b} |" for f, a, b in features)
    worked = (
        f"**Comparison: Creditors Journal (CJ) vs Creditors Allowance Journal (CAJ)** [8 marks]\n\n"
        f"| Feature | Creditors Journal (CJ) | Creditors Allowance Journal (CAJ) |\n|---|---|---|\n{md_rows}"
    )
    hints = {
        "tier_1": "CJ is for purchases (increases what you owe); CAJ is for returns/rebates (reduces what you owe).",
        "tier_2": "CJ source doc = Original Invoice; CAJ source doc = Debit Note.",
        "tier_3": "CJ increases liability (Credit); CAJ decreases liability (Debit).",
    }
    return build_table(
        rng, qid="g9_cj_28", subskill="28_caj_vs_cj_columns_comparison_table",
        title="Comparison Matrix: CJ vs CAJ",
        prompt=prompt, headers=headers, rows=rows, correct_map=cmap, cell_hints=cell_hints,
        worked_solution=worked, sample_answer="See CJ vs CAJ comparison table.",
        marks=8, hints=hints,
        marking_points=[{"id": "mp_1", "desc": "Accurate comparisons across all 4 features", "marks": 8, "editable": True}],
        misconception_tags=["caj_effect_on_liability_reversed"],
        journal_type="comparison_matrix",
    )


def arch_29_transaction_analysis_credit_purchases_table(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    creds = pick_creditors(rng, 4)
    a1 = rng.randint(15, 35) * 200
    a2 = rng.randint(5, 15) * 100
    a3 = rng.randint(12, 30) * 200
    a4 = rng.randint(6, 18) * 150

    cases = [
        (f"1. Bought trading stock on credit from {creds[0][0]}, {fmt_r(a1)}", "Trading stock", "Creditors control", fmt_cell(a1)),
        (f"2. Bought office stationery on credit from {creds[1][0]}, {fmt_r(a2)}", "Stationery", "Creditors control", fmt_cell(a2)),
        (f"3. Bought display equipment on credit from {creds[2][0]}, {fmt_r(a3)}", "Equipment", "Creditors control", fmt_cell(a3)),
        (f"4. Had store security gate repaired on credit by {creds[3][0]}, {fmt_r(a4)}", "Repairs", "Creditors control", fmt_cell(a4)),
    ]
    rng.shuffle(cases)

    headers = ["Transaction Description", "Account Debited", "Account Credited", "Amount"]
    data_rows = [[t, dr, cr, amt] for t, dr, cr, amt in cases]
    given_coords = {(r, 0) for r in range(4)}
    rows, cmap = make_grid_rows(data_rows, given_coords)
    cell_hints = {
        f"t0_r{r}_c2": "Every credit purchase in the CJ credits 'Creditors control'." for r in range(4)
    }

    prompt = (
        f"For each credit purchase transaction at **{biz}**, complete the **Transaction Analysis Table** below "
        f"stating the **Account Debited**, **Account Credited**, and **Amount** (plain numbers, no R or spaces)."
    )
    md_rows = "\n".join(f"| {t} | {dr} | {cr} | {fmt_r(int(a))} |" for t, dr, cr, a in cases)
    worked = (
        f"**Transaction Analysis Table for {biz}** [12 marks]\n\n"
        f"| Transaction Description | Account Debited | Account Credited | Amount |\n|---|---|---|---:|\n{md_rows}\n\n"
        "- **Rule**: The asset or expense received is **Debited**; the liability owed to suppliers (**Creditors control**) is **Credited**."
    )
    hints = {
        "tier_1": "Assets and expenses increase on the Debit side. Liabilities increase on the Credit side.",
        "tier_2": "Debit Trading stock, Stationery, Equipment, or Repairs; Credit Creditors control.",
        "tier_3": "Creditors control is always the credited account for purchases on credit in the CJ.",
    }
    return build_table(
        rng, qid="g9_cj_29", subskill="29_transaction_analysis_credit_purchases_table",
        title="Transaction Analysis Table for Credit Purchases",
        prompt=prompt, headers=headers, rows=rows, correct_map=cmap, cell_hints=cell_hints,
        worked_solution=worked, sample_answer="See transaction analysis table.",
        marks=12, hints=hints,
        marking_points=[{"id": "mp_1", "desc": "Accurate Debit, Credit, and Amount for all 4 transactions", "marks": 12, "editable": True}],
        misconception_tags=["debited_creditors_control_for_purchase"],
        journal_type="transaction_analysis",
    )


def arch_30_classify_credit_purchases_asset_vs_expense_mcq(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    sup, _ = rng.choice(CREDITOR_POOL)
    eq_name = rng.choice(["electronic cash register", "display shelving unit", "delivery trailer"])

    prompt = (
        f"**{biz}** buys a **{eq_name}** and **stationery** on credit from **{sup}**.\n\n"
        f"How are these two items classified under the Elements of Accounting?"
    )
    correct = (
        f"The {eq_name} is an Asset (Non-Current Asset) because it will benefit {biz} for many years; "
        "Stationery is an Expense because it is consumed in daily office operations."
    )
    distractors = [
        f"Both the {eq_name} and Stationery are classified as Expenses because they reduce profit immediately.",
        f"Both items are classified as Current Liabilities because they were bought from {sup} on credit.",
        f"The {eq_name} is an Expense (Repairs), and Stationery is an Asset (Trading Stock).",
    ]
    explanation = (
        f"- **{eq_name.capitalize()}** is durable capital equipment used repeatedly to run the shop -> **Asset**.\n"
        f"- **Stationery** (paper, pens, envelopes) is used up quickly in administration -> **Expense**.\n"
        f"- The debt owed to **{sup}** is the **Liability (Creditors Control)**, but the purchased items themselves are Asset and Expense respectively."
    )
    hints = {
        "tier_1": "Durable long-term equipment vs consumables used up in the office.",
        "tier_2": "Equipment = Asset; Stationery = Expense.",
        "tier_3": f"{eq_name} = Asset; Stationery = Expense.",
    }
    return build_mcq(
        rng, qid="g9_cj_30", subskill="30_classify_credit_purchases_asset_vs_expense_mcq",
        title="Classify Purchases: Asset vs Expense",
        prompt=prompt, correct_text=correct, distractors=distractors,
        explanation=explanation, hints=hints,
        misconception_tags=["equipment_treated_as_expense"],
    )


def arch_31_double_entry_cj_posting_rule_mcq(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)

    prompt = (
        f"At the end of the month, the bookkeeper of **{biz}** posts the totals of the **Creditors Journal (CJ)** "
        f"to the **General Ledger**.\n\n"
        f"Which double-entry rule correctly records the posting of the CJ totals?"
    )
    correct = (
        "DEBIT the individual asset and expense accounts (Trading Stock, Stationery, Sundries), "
        "and CREDIT Creditors Control with the total of the Creditors Control column."
    )
    distractors = [
        "DEBIT Creditors Control with the total, and CREDIT Bank with the total.",
        "DEBIT Creditors Control with the total, and CREDIT Trading Stock and Stationery.",
        "DEBIT Bank with the total, and CREDIT individual creditors in the General Ledger.",
    ]
    explanation = (
        f"- **Trading Stock** (+Asset) is **Debited**.\n"
        f"- **Stationery** (+Expense) is **Debited**.\n"
        f"- **Sundry Accounts** (+Assets / +Expenses) are **Debited** individually.\n"
        f"- **Creditors Control** (+Liability) is **Credited** with the full CJ total."
    )
    hints = {
        "tier_1": "Assets and expenses increase on the Debit side; liabilities increase on the Credit side.",
        "tier_2": "Credit purchases INCREASE Creditors Control (Liability), so Creditors Control is Credited.",
        "tier_3": "Debit Trading Stock, Stationery, Sundries; Credit Creditors Control.",
    }
    return build_mcq(
        rng, qid="g9_cj_31", subskill="31_double_entry_cj_posting_rule_mcq",
        title="Double-Entry Posting Rule for CJ Totals",
        prompt=prompt, correct_text=correct, distractors=distractors,
        explanation=explanation, hints=hints,
        misconception_tags=["reversed_debit_credit_in_cj_posting"],
    )


def arch_32_accounting_equation_credit_purchase_of_trading_stock_table(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    sup, _ = rng.choice(CREDITOR_POOL)
    goods = rng.choice(STOCK_LINES)
    amt = rng.randint(14, 45) * 200

    prompt = (
        f"Analyze the effect of this transaction on the **Accounting Equation ($A = E + L$)** for **{biz}**:\n\n"
        f"*Bought {goods} on credit from {sup} for {fmt_r(amt)} (Original invoice C1).*\n\n"
        f"Complete the Source Document, Account Debited, Account Credited, and the changes to Assets, Owner's Equity, "
        f"and Liabilities in the table below (use `+{amt}`, `0`, or `-{amt}`)."
    )
    headers = ["Source Document", "Account Debited", "Account Credited", "Assets", "Owner's Equity", "Liabilities"]
    data_rows = [["Original Invoice", "Trading stock", "Creditors control", f"+{amt}", "0", f"+{amt}"]]
    rows, cmap = make_grid_rows(data_rows, set())
    cell_hints = {
        "t0_r0_c3": f"Trading stock is an asset increasing by {amt}: enter +{amt}.",
        "t0_r0_c4": "No profit or expense is recognized at the moment of buying stock: enter 0.",
        "t0_r0_c5": f"Creditors control is a liability increasing by {amt}: enter +{amt}.",
    }

    worked = (
        f"**Accounting Equation: Credit Purchase of Trading Stock** [6 marks]\n\n"
        f"| Source Document | Account Debited | Account Credited | Assets | Owner's Equity | Liabilities |\n"
        f"|---|---|---|---:|---:|---:|\n"
        f"| Original Invoice | Trading stock | Creditors control | +{amt} | 0 | +{amt} |\n\n"
        f"- **Explanation**: Trading stock increases Assets (+{fmt_r(amt)}); Creditors control increases Liabilities (+{fmt_r(amt)}). "
        f"Equation balances: $+{amt} = 0 + {amt}$."
    )
    hints = {
        "tier_1": "Source doc = Original Invoice. Goods bought for resale = Trading stock.",
        "tier_2": "Assets increase by +amount; Liabilities increase by +amount; Equity is unaffected.",
        "tier_3": f"Original Invoice, Trading stock, Creditors control, +{amt}, 0, +{amt}.",
    }
    return build_table(
        rng, qid="g9_cj_32", subskill="32_accounting_equation_credit_purchase_of_trading_stock_table",
        title="Accounting Equation: Credit Purchase of Trading Stock",
        prompt=prompt, headers=headers, rows=rows, correct_map=cmap, cell_hints=cell_hints,
        worked_solution=worked, sample_answer=f"+{amt} = 0 + {amt}",
        marks=6, hints=hints,
        marking_points=[{"id": "mp_1", "desc": f"Accurate source doc, accounts, and +{amt} / 0 / +{amt}", "marks": 6, "editable": True}],
        misconception_tags=["trading_stock_treated_as_expense_reducing_equity"],
        journal_type="accounting_equation",
    )


def arch_33_accounting_equation_credit_purchase_of_equipment_table(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    sup, _ = rng.choice(CREDITOR_POOL)
    amt = rng.randint(18, 50) * 200

    prompt = (
        f"Analyze the effect of this transaction on the **Accounting Equation ($A = E + L$)** for **{biz}**:\n\n"
        f"*Bought a new computer system for the cash register on credit from {sup} for {fmt_r(amt)}.*\n\n"
        f"Complete the table below using `+{amt}`, `0`, or `-{amt}` for the monetary columns."
    )
    headers = ["Source Document", "Account Debited", "Account Credited", "Assets", "Owner's Equity", "Liabilities"]
    data_rows = [["Original Invoice", "Equipment", "Creditors control", f"+{amt}", "0", f"+{amt}"]]
    rows, cmap = make_grid_rows(data_rows, set())
    cell_hints = {
        "t0_r0_c1": "Computer system for the store is classified as Equipment.",
        "t0_r0_c3": f"Equipment increases assets: enter +{amt}.",
        "t0_r0_c5": f"Creditors control increases liabilities: enter +{amt}.",
    }

    worked = (
        f"**Accounting Equation: Credit Purchase of Equipment** [6 marks]\n\n"
        f"| Source Document | Account Debited | Account Credited | Assets | Owner's Equity | Liabilities |\n"
        f"|---|---|---|---:|---:|---:|\n"
        f"| Original Invoice | Equipment | Creditors control | +{amt} | 0 | +{amt} |\n\n"
        f"- **Balance**: $+{amt} = 0 + {amt}$."
    )
    hints = {
        "tier_1": "Equipment is a long-term asset, not an expense.",
        "tier_2": "Assets increase by +amount; Liabilities increase by +amount; Equity is 0.",
        "tier_3": f"Original Invoice, Equipment, Creditors control, +{amt}, 0, +{amt}.",
    }
    return build_table(
        rng, qid="g9_cj_33", subskill="33_accounting_equation_credit_purchase_of_equipment_table",
        title="Accounting Equation: Credit Purchase of Equipment",
        prompt=prompt, headers=headers, rows=rows, correct_map=cmap, cell_hints=cell_hints,
        worked_solution=worked, sample_answer=f"+{amt} = 0 + {amt}",
        marks=6, hints=hints,
        marking_points=[{"id": "mp_1", "desc": f"Accurate source doc, accounts, and +{amt} / 0 / +{amt}", "marks": 6, "editable": True}],
        misconception_tags=["equipment_treated_as_expense_reducing_equity"],
        journal_type="accounting_equation",
    )


def arch_34_accounting_equation_credit_expense_stationery_repairs_table(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    sup, _ = rng.choice(CREDITOR_POOL)
    is_stat = rng.choice([True, False])
    if is_stat:
        acct = "Stationery"
        desc = "office receipt books, pens and printing paper"
        amt = rng.randint(6, 18) * 100
    else:
        acct = "Repairs"
        desc = "emergency electrical repair of shop refrigeration"
        amt = rng.randint(8, 25) * 150

    prompt = (
        f"Analyze the effect on the **Accounting Equation ($A = E + L$)** for **{biz}**:\n\n"
        f"*Purchased {desc} on credit from {sup} for {fmt_r(amt)}.*\n\n"
        f"Complete the table below (enter `+{amt}`, `0`, or `-{amt}`)."
    )
    headers = ["Source Document", "Account Debited", "Account Credited", "Assets", "Owner's Equity", "Liabilities"]
    data_rows = [["Original Invoice", acct, "Creditors control", "0", f"-{amt}", f"+{amt}"]]
    rows, cmap = make_grid_rows(data_rows, set())
    cell_hints = {
        "t0_r0_c3": "Expenses do not change Assets at the time of purchase: enter 0.",
        "t0_r0_c4": f"{acct} is an expense that reduces net profit / owner's equity: enter -{amt}.",
        "t0_r0_c5": f"Debt owed to {sup} increases: enter +{amt}.",
    }

    worked = (
        f"**Accounting Equation: Credit Expense ({acct})** [6 marks]\n\n"
        f"| Source Document | Account Debited | Account Credited | Assets | Owner's Equity | Liabilities |\n"
        f"|---|---|---|---:|---:|---:|\n"
        f"| Original Invoice | {acct} | Creditors control | 0 | -{amt} | +{amt} |\n\n"
        f"- **Balance**: $0 = -{amt} + {amt} = 0$."
    )
    hints = {
        "tier_1": f"{acct} is an expense. What do expenses do to Owner's Equity?",
        "tier_2": "Expenses reduce Owner's Equity (-), while buying on credit increases Liabilities (+). Assets are 0.",
        "tier_3": f"Original Invoice, {acct}, Creditors control, 0, -{amt}, +{amt}.",
    }
    return build_table(
        rng, qid="g9_cj_34", subskill="34_accounting_equation_credit_expense_stationery_repairs_table",
        title="Accounting Equation: Credit Purchase of an Expense Item",
        prompt=prompt, headers=headers, rows=rows, correct_map=cmap, cell_hints=cell_hints,
        worked_solution=worked, sample_answer=f"0 = -{amt} + {amt}",
        marks=6, hints=hints,
        marking_points=[{"id": "mp_1", "desc": f"Accurate source doc, accounts, and 0 / -{amt} / +{amt}", "marks": 6, "editable": True}],
        misconception_tags=["expense_not_deducted_from_equity"],
        journal_type="accounting_equation",
    )


def arch_35_accounting_equation_creditors_return_caj_stock_and_expense_table(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    sup, _ = rng.choice(CREDITOR_POOL)
    amt = rng.randint(4, 18) * 150

    prompt = (
        f"Analyze the effect on the **Accounting Equation ($A = E + L$)** for **{biz}**:\n\n"
        f"*Issued Debit Note DN1 to {sup} for damaged trading stock returned, {fmt_r(amt)}.*\n\n"
        f"Complete the table below using `+{amt}`, `0`, or `-{amt}`."
    )
    headers = ["Source Document", "Account Debited", "Account Credited", "Assets", "Owner's Equity", "Liabilities"]
    data_rows = [["Debit Note", "Creditors control", "Trading stock", f"-{amt}", "0", f"-{amt}"]]
    rows, cmap = make_grid_rows(data_rows, set())
    cell_hints = {
        "t0_r0_c1": "Creditor liability is decreasing, so Creditors control is Debited.",
        "t0_r0_c2": "Trading stock is leaving the business, so Trading stock is Credited.",
        "t0_r0_c3": f"Trading stock decreases assets: enter -{amt}.",
        "t0_r0_c5": f"Creditors control decreases liabilities: enter -{amt}.",
    }

    worked = (
        f"**Accounting Equation: Return of Trading Stock (CAJ)** [6 marks]\n\n"
        f"| Source Document | Account Debited | Account Credited | Assets | Owner's Equity | Liabilities |\n"
        f"|---|---|---|---:|---:|---:|\n"
        f"| Debit Note | Creditors control | Trading stock | -{amt} | 0 | -{amt} |\n\n"
        f"- **Balance**: $-{amt} = 0 - {amt}$."
    )
    hints = {
        "tier_1": "Source doc = Debit Note. Returning stock reverses the credit purchase.",
        "tier_2": "Debit Creditors control (reduces liability); Credit Trading stock (reduces asset).",
        "tier_3": f"Debit Note, Creditors control, Trading stock, -{amt}, 0, -{amt}.",
    }
    return build_table(
        rng, qid="g9_cj_35", subskill="35_accounting_equation_creditors_return_caj_stock_and_expense_table",
        title="Accounting Equation: Creditors Allowance for Returned Stock",
        prompt=prompt, headers=headers, rows=rows, correct_map=cmap, cell_hints=cell_hints,
        worked_solution=worked, sample_answer=f"-{amt} = 0 - {amt}",
        marks=6, hints=hints,
        marking_points=[{"id": "mp_1", "desc": f"Accurate source doc, accounts, and -{amt} / 0 / -{amt}", "marks": 6, "editable": True}],
        misconception_tags=["reversed_debit_and_credit_on_creditor_return"],
        journal_type="accounting_equation",
    )


def arch_36_accounting_equation_4row_cj_caj_mixed_table(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    creds = pick_creditors(rng, 4)
    a1 = rng.randint(15, 35) * 200
    a2 = rng.randint(6, 18) * 100
    a3 = rng.randint(4, 14) * 150
    a4 = rng.randint(12, 28) * 200

    cases = [
        (f"1. Bought stock on credit from {creds[0][0]}, {fmt_r(a1)}", "Original Invoice", "Trading stock", "Creditors control", f"+{a1}", "0", f"+{a1}"),
        (f"2. Bought stationery on credit from {creds[1][0]}, {fmt_r(a2)}", "Original Invoice", "Stationery", "Creditors control", "0", f"-{a2}", f"+{a2}"),
        (f"3. Returned damaged stock to {creds[2][0]}, {fmt_r(a3)}", "Debit Note", "Creditors control", "Trading stock", f"-{a3}", "0", f"-{a3}"),
        (f"4. Bought equipment on credit from {creds[3][0]}, {fmt_r(a4)}", "Original Invoice", "Equipment", "Creditors control", f"+{a4}", "0", f"+{a4}"),
    ]
    rng.shuffle(cases)

    headers = ["Transaction", "Source Document", "Account Debited", "Account Credited", "Assets", "Owner's Equity", "Liabilities"]
    data_rows = [[t, s, dr, cr, a, e, l] for t, s, dr, cr, a, e, l in cases]
    given_coords = {(r, 0) for r in range(4)}
    rows, cmap = make_grid_rows(data_rows, given_coords)
    cell_hints = {
        f"t0_r{r}_c1": "Enter 'Original Invoice' or 'Debit Note'." for r in range(4)
    }

    prompt = (
        f"Analyze the 4 transactions below on the **Accounting Equation ($A = E + L$)** for **{biz}**.\n\n"
        "Complete the Source Document, Account Debited, Account Credited, and the changes to Assets, Owner's Equity, "
        "and Liabilities (`+amount`, `0`, or `-amount`)."
    )
    md_rows = "\n".join(f"| {t} | {s} | {dr} | {cr} | {a} | {e} | {l} |" for t, s, dr, cr, a, e, l in cases)
    worked = (
        f"**Mixed CJ & CAJ Accounting Equation Analysis** [16 marks]\n\n"
        f"| Transaction | Source Document | Account Debited | Account Credited | Assets | Owner's Equity | Liabilities |\n"
        f"|---|---|---|---|---:|---:|---:|\n{md_rows}"
    )
    hints = {
        "tier_1": "Watch row 3: returns use Debit Note and reverse the debit/credit order.",
        "tier_2": "Stationery reduces Equity (-); Stock & Equipment increase Assets (+); all credit purchases increase Liabilities (+).",
        "tier_3": "Returns decrease Assets (-) and decrease Liabilities (-).",
    }
    return build_table(
        rng, qid="g9_cj_36", subskill="36_accounting_equation_4row_cj_caj_mixed_table",
        title="4-Row Mixed CJ & CAJ Accounting Equation Analysis",
        prompt=prompt, headers=headers, rows=rows, correct_map=cmap, cell_hints=cell_hints,
        worked_solution=worked, sample_answer="See mixed accounting equation table.",
        marks=16, hints=hints,
        marking_points=[{"id": "mp_1", "desc": "Accurately completes all 4 transactions across all columns", "marks": 16, "editable": True}],
        misconception_tags=["failed_to_reverse_signs_on_return"],
        journal_type="accounting_equation",
    )


def arch_37_cash_flow_planning_importance_of_creditors_records(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    sup, _ = rng.choice(CREDITOR_POOL)
    days = rng.choice([30, 60])
    amt = rng.randint(25, 75) * 500

    prompt = (
        f"**{biz}** owes **{sup}** **{fmt_r(amt)}** payable within **{days} days**.\n\n"
        f"Why is keeping an accurate **Creditors Journal** and **Creditors Ledger** essential for **cash flow planning**?"
    )
    correct = (
        f"It allows {biz} to forecast upcoming cash outflows so that sufficient bank funds are set aside before the {days} days expire, "
        "preventing defaults, penalty interest, and suspension of supplier credit."
    )
    distractors = [
        "It guarantees that the bank will automatically cancel all supplier debts if sales are slow.",
        "It turns the liability into cash revenue so the business never needs to pay the supplier.",
        "It ensures that debtors pay their accounts exactly on the same day the supplier is paid.",
    ]
    explanation = (
        f"- Buying on credit defers cash payment, but the debt of **{fmt_r(amt)}** **must** be settled within **{days} days**.\n"
        f"- Up-to-date creditors records enable the owner to plan cash inflows and avoid liquidity crises, legal action, or supply blacklisting."
    )
    hints = {
        "tier_1": "What happens if a business doesn't plan for bills that must be paid in 30 or 60 days?",
        "tier_2": "Creditors records forecast cash outflows to ensure sufficient bank balance.",
        "tier_3": f"Creditors records enable {biz} to budget cash outflows and maintain good credit standing with {sup}.",
    }
    return build_mcq(
        rng, qid="g9_cj_37", subskill="37_cash_flow_planning_importance_of_creditors_records",
        title="Role of Creditors Records in Cash Flow Planning",
        prompt=prompt, correct_text=correct, distractors=distractors,
        explanation=explanation, hints=hints,
        misconception_tags=["cash_flow_planning_misunderstood"],
    )


def arch_38_early_settlement_vs_trade_discount_distinction(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    sup, _ = rng.choice(CREDITOR_POOL)
    td = rng.choice([10, 15])
    sd = rng.choice([2.5, 5])
    sd_str = f"{sd}".replace(".", ",")

    prompt = (
        f"**{sup}** offers **{biz}** two discounts:\n"
        f"- A **{td}% Trade Discount** on the catalogue price at purchase.\n"
        f"- A **{sd_str}% Settlement Discount** if the invoice is paid within 14 days.\n\n"
        f"How do these two discounts differ in how they are recorded in the journals?"
    )
    correct = (
        f"The {td}% trade discount is deducted immediately on the invoice before recording in the CJ (never recorded separately); "
        f"the {sd_str}% settlement discount is recorded in the CPJ (Discount Received) ONLY if payment is made within 14 days."
    )
    distractors = [
        f"Both the {td}% and {sd_str}% discounts are recorded as Discount Received columns in the Creditors Journal.",
        f"Neither discount is recorded anywhere because discounts are illegal in South African retail accounting.",
        f"The {td}% trade discount is recorded in the CPJ, while the {sd_str}% settlement discount is entered in the CJ.",
    ]
    explanation = (
        f"- **Trade Discount ({td}%)**: Deducted immediately on the invoice; only the net amount enters the **CJ**.\n"
        f"- **Settlement Discount ({sd_str}%)**: An incentive for prompt payment; recorded as **Discount Received** in the **CPJ** only when early payment actually occurs."
    )
    hints = {
        "tier_1": "Trade discount happens at purchase (CJ); settlement discount happens at payment (CPJ).",
        "tier_2": "Trade discount adjusts the purchase price; settlement discount is recorded when paying early.",
        "tier_3": "Trade discount = immediate net price in CJ. Settlement discount = Discount Received in CPJ upon early payment.",
    }
    return build_mcq(
        rng, qid="g9_cj_38", subskill="38_early_settlement_vs_trade_discount_distinction",
        title="Trade Discount vs Settlement Discount Distinction",
        prompt=prompt, correct_text=correct, distractors=distractors,
        explanation=explanation, hints=hints,
        misconception_tags=["settlement_discount_entered_in_cj"],
    )


def arch_39_calculate_creditors_outstanding_balance_table(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    month, year, _ = rng.choice(MONTH_DATA)
    creds = pick_creditors(rng, 3)

    c_data = []
    for name, fol in creds:
        op = rng.randint(10, 30) * 200
        pur = rng.randint(12, 35) * 200
        ret = rng.randint(2, 6) * 100
        pay = rng.randint(8, 25) * 200
        cl = op + pur - ret - pay
        c_data.append((name, fol, op, pur, ret, pay, cl))

    headers = ["Creditor", "Fol", "Opening Balance", "CJ Purchases (+)", "CAJ Returns (-)", "CPJ Payments (-)", "Closing Balance Owing"]
    data_rows = [[name, fol, fmt_cell(op), fmt_cell(pur), fmt_cell(ret), fmt_cell(pay), fmt_cell(cl)] for name, fol, op, pur, ret, pay, cl in c_data]
    given_coords = {(r, 0) for r in range(3)} | {(r, 1) for r in range(3)} | {(r, 2) for r in range(3)} | {(r, 3) for r in range(3)} | {(r, 4) for r in range(3)} | {(r, 5) for r in range(3)}
    rows, cmap = make_grid_rows(data_rows, given_coords)
    cell_hints = {f"t0_r{r}_c6": "Opening Balance + Purchases - Returns - Payments = Closing Balance." for r in range(3)}

    prompt = (
        f"Calculate the **Closing Balance Owing** to each of **{biz}**'s creditors at the end of **{month} {year}**.\n\n"
        f"Formula: $\\text{{Closing Balance}} = \\text{{Opening}} + \\text{{Purchases (CJ)}} - \\text{{Returns (CAJ)}} - \\text{{Payments (CPJ)}}$"
    )
    md_rows = "\n".join(f"| {n} | {f} | {fmt_r(op)} | {fmt_r(p)} | {fmt_r(r)} | {fmt_r(pay)} | **{fmt_r(cl)}** |" for n, f, op, p, r, pay, cl in c_data)
    worked = (
        f"**Creditors Balances at End of {month} {year}** [6 marks]\n\n"
        f"| Creditor | Fol | Opening Balance | CJ Purchases (+) | CAJ Returns (-) | CPJ Payments (-) | Closing Balance |\n"
        f"|---|---|---:|---:|---:|---:|---:|\n{md_rows}"
    )
    hints = {
        "tier_1": "Purchases add to what you owe; returns and payments reduce what you owe.",
        "tier_2": "Closing = Opening + CJ - CAJ - CPJ.",
        "tier_3": f"Row 1: {c_data[0][2]} + {c_data[0][3]} - {c_data[0][4]} - {c_data[0][5]} = {c_data[0][6]}.",
    }
    return build_table(
        rng, qid="g9_cj_39", subskill="39_calculate_creditors_outstanding_balance_table",
        title="Calculate Closing Balances of Creditors",
        prompt=prompt, headers=headers, rows=rows, correct_map=cmap, cell_hints=cell_hints,
        worked_solution=worked, sample_answer="See creditors closing balances table.",
        marks=6, hints=hints,
        marking_points=[{"id": "mp_1", "desc": "Accurately calculates all 3 closing balances", "marks": 6, "editable": True}],
        misconception_tags=["added_payments_to_liability"],
        journal_type="creditors_schedule",
    )


def arch_40_calculate_creditors_total_owed_across_5_suppliers_calc(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    creds = [c[0] for c in pick_creditors(rng, 5)]
    balances = [rng.randint(12, 45) * 200 for _ in range(5)]
    total_owed = sum(balances)

    lines = [f"- **{name}**: {fmt_r(bal)}" for name, bal in zip(creds, balances)]
    prompt = (
        f"At month-end, the Creditors Ledger of **{biz}** shows the following individual balances:\n"
        + "\n".join(lines)
        + "\n\nCalculate the total balance of the **Creditors Control Account** in the General Ledger "
        f"(plain number, no R or spaces)."
    )
    calc_str = " + ".join(fmt_r(b) for b in balances)
    worked = (
        f"**{fmt_r(total_owed)}** (`{total_owed}`) [3 marks]\n\n"
        f"- **Creditors Control Balance** equals the sum of all individual creditor balances:\n"
        f"$$\\text{{Total Owed}} = {calc_str} = {fmt_r(total_owed)}$$ (`{total_owed}`) [3 marks]."
    )
    hints = {
        "tier_1": "Creditors Control is the summary account that must equal the sum of all individual creditors.",
        "tier_2": "Add all 5 creditor balances together.",
        "tier_3": f"{' + '.join(str(b) for b in balances)} = {total_owed}.",
    }
    return build_short(
        rng, qid="g9_cj_40", subskill="40_calculate_creditors_total_owed_across_5_suppliers_calc",
        title="Sum Creditors Ledger Balances for Creditors Control",
        prompt=prompt, expected_answer=str(total_owed), worked_solution=worked, hints=hints,
        marking_points=[{"id": "mp_1", "desc": f"Sums all 5 creditor balances to {fmt_r(total_owed)}", "marks": 3, "editable": True}],
        misconception_tags=["creditors_control_reconciliation_sum_error"],
        marks=3, qtype="math_short",
    )


def arch_41_evaluate_creditor_credit_limit_breaches_table(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    creds = pick_creditors(rng, 4)

    rows_info = []
    for i, (name, _) in enumerate(creds):
        limit = rng.randint(15, 35) * 1000
        # Make row 1 and row 3 exceed limit; row 0 and row 2 stay within limit
        if i % 2 == 1:
            owed = limit + rng.randint(2, 8) * 500
            status = "Breached"
        else:
            owed = limit - rng.randint(3, 10) * 500
            status = "Within Limit"
        diff = abs(limit - owed)
        rows_info.append((name, limit, owed, status, diff))

    headers = ["Creditor", "Credit Limit", "Current Balance Owed", "Compliance Status", "Difference"]
    data_rows = [[n, fmt_cell(lim), fmt_cell(ow), st, fmt_cell(d)] for n, lim, ow, st, d in rows_info]
    given_coords = {(r, 0) for r in range(4)} | {(r, 1) for r in range(4)} | {(r, 2) for r in range(4)}
    rows, cmap = make_grid_rows(data_rows, given_coords)
    cell_hints = {
        f"t0_r{r}_c3": "Enter 'Breached' or 'Within Limit'." for r in range(4)
    }

    prompt = (
        f"**{biz}**'s finance manager conducts a credit compliance audit.\n\n"
        f"For each supplier, determine the **Compliance Status (`Breached` or `Within Limit`)** "
        f"and calculate the **Difference** (amount by which the balance exceeds or stays under the limit, as a positive number)."
    )
    md_rows = "\n".join(f"| {n} | {fmt_r(l)} | {fmt_r(o)} | **{s}** | {fmt_r(d)} |" for n, l, o, s, d in rows_info)
    worked = (
        f"**Credit Limit Compliance Audit for {biz}** [8 marks]\n\n"
        f"| Creditor | Credit Limit | Current Balance Owed | Compliance Status | Difference |\n"
        f"|---|---:|---:|---|---:|\n{md_rows}"
    )
    hints = {
        "tier_1": "If Current Balance > Credit Limit, the limit is 'Breached'. Otherwise it is 'Within Limit'.",
        "tier_2": "Difference = |Credit Limit - Current Balance|.",
        "tier_3": f"Row 1: {rows_info[0][3]}; Row 2: {rows_info[1][3]}; Row 3: {rows_info[2][3]}; Row 4: {rows_info[3][3]}.",
    }
    return build_table(
        rng, qid="g9_cj_41", subskill="41_evaluate_creditor_credit_limit_breaches_table",
        title="Credit Limit Compliance Audit Table",
        prompt=prompt, headers=headers, rows=rows, correct_map=cmap, cell_hints=cell_hints,
        worked_solution=worked, sample_answer="See credit limit compliance audit table.",
        marks=8, hints=hints,
        marking_points=[{"id": "mp_1", "desc": "Accurately evaluates compliance and difference for all 4 suppliers", "marks": 8, "editable": True}],
        misconception_tags=["credit_limit_breach_inverted"],
        journal_type="credit_limit_audit",
    )


def arch_42_evaluate_creditor_credit_term_days_compliance_mcq(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    sup, _ = rng.choice(CREDITOR_POOL)
    term_days = rng.choice([30, 60])
    actual_days = term_days + rng.choice([12, 18, 25])
    amt = rng.randint(15, 45) * 500

    prompt = (
        f"**{sup}** sells stock worth **{fmt_r(amt)}** to **{biz}** on credit terms of **{term_days} days**.\n\n"
        f"Due to poor cash management, **{biz}** pays the account after **{actual_days} days** ({actual_days - term_days} days late).\n\n"
        f"What is the most likely consequence of this breach of credit terms for **{biz}**?"
    )
    correct = (
        f"{sup} may charge penalty interest on the overdue {fmt_r(amt)}, reduce {biz}'s credit limit, "
        "or refuse to supply future orders on credit."
    )
    distractors = [
        f"{sup} will reward {biz} with a higher trade discount on the next purchase.",
        f"The South African Revenue Service will automatically pay the {fmt_r(amt)} on {biz}'s behalf.",
        f"{biz}'s bank account will automatically increase by the interest charged.",
    ]
    explanation = (
        f"- Failing to settle within the agreed **{term_days}-day credit term** damages {biz}'s credit rating.\n"
        f"- Suppliers typically charge **overdue penalty interest**, suspend credit deliveries, or demand cash on delivery (COD)."
    )
    hints = {
        "tier_1": "What happens when a business pays its supplier late?",
        "tier_2": "Suppliers protect themselves with penalty interest and by cutting off credit.",
        "tier_3": f"Late payment ({actual_days} vs {term_days} days) leads to penalty interest and loss of credit facilities.",
    }
    return build_mcq(
        rng, qid="g9_cj_42", subskill="42_evaluate_creditor_credit_term_days_compliance_mcq",
        title="Consequences of Breaching Supplier Credit Terms",
        prompt=prompt, correct_text=correct, distractors=distractors,
        explanation=explanation, hints=hints,
        misconception_tags=["credit_term_compliance_misunderstood"],
    )


def arch_43_rank_best_and_worst_managed_creditor_accounts_table(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    creds = pick_creditors(rng, 3)

    accounts = [
        (creds[0][0], "R30 000", "R12 000 (40%)", "Paid within 25 days (Terms 30 days)", "Best Managed"),
        (creds[1][0], "R20 000", "R19 500 (97.5%)", "Paid within 29 days (Terms 30 days)", "Moderate Risk"),
        (creds[2][0], "R25 000", "R28 000 (112%)", "62 days overdue; credit frozen", "Highest Risk"),
    ]
    rng.shuffle(accounts)

    headers = ["Creditor", "Credit Limit", "Balance Owed (% of Limit)", "Payment Track Record", "Management Assessment"]
    data_rows = [[n, lim, bal, rec, assess] for n, lim, bal, rec, assess in accounts]
    given_coords = {(r, 0) for r in range(3)} | {(r, 1) for r in range(3)} | {(r, 2) for r in range(3)} | {(r, 3) for r in range(3)}
    rows, cmap = make_grid_rows(data_rows, given_coords)
    cell_hints = {
        f"t0_r{r}_c4": "Choose 'Best Managed', 'Moderate Risk', or 'Highest Risk'." for r in range(3)
    }

    prompt = (
        f"Evaluate the management of **{biz}**'s creditor accounts in the table below.\n\n"
        f"Assign each account its correct **Management Assessment** (`Best Managed`, `Moderate Risk`, or `Highest Risk`)."
    )
    md_rows = "\n".join(f"| {n} | {lim} | {bal} | {rec} | **{assess}** |" for n, lim, bal, rec, assess in accounts)
    worked = (
        f"**Creditors Account Management Assessment** [6 marks]\n\n"
        f"| Creditor | Credit Limit | Balance Owed | Payment Record | Assessment |\n|---|---|---|---|---|\n{md_rows}"
    )
    hints = {
        "tier_1": "Low utilization + early payment = Best Managed. Exceeding limit + frozen account = Highest Risk.",
        "tier_2": "Examine both the percentage of credit limit used and the days taken to pay.",
        "tier_3": "Best Managed = low utilization on-time; Highest Risk = over credit limit and overdue.",
    }
    return build_table(
        rng, qid="g9_cj_43", subskill="43_rank_best_and_worst_managed_creditor_accounts_table",
        title="Assess Creditor Account Risk & Management",
        prompt=prompt, headers=headers, rows=rows, correct_map=cmap, cell_hints=cell_hints,
        worked_solution=worked, sample_answer="See creditor management assessment table.",
        marks=6, hints=hints,
        marking_points=[{"id": "mp_1", "desc": "Accurately classifies risk level for all 3 accounts", "marks": 6, "editable": True}],
        misconception_tags=["credit_risk_evaluation_error"],
        journal_type="risk_assessment",
    )


def arch_44_available_credit_headroom_before_order_calc(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    sup, _ = rng.choice(CREDITOR_POOL)
    limit = rng.randint(20, 50) * 1000
    curr_bal = rng.randint(12, limit // 1000 - 4) * 1000 + rng.randint(2, 8) * 100
    debit_note = rng.randint(4, 15) * 100
    # Available credit = limit - (curr_bal - debit_note)
    adj_bal = curr_bal - debit_note
    headroom = limit - adj_bal

    prompt = (
        f"**{sup}** sets a strict credit limit of **{fmt_r(limit)}** for **{biz}**.\n\n"
        f"Currently, {biz} owes {sup} **{fmt_r(curr_bal)}**, but has just been issued an accepted **Debit Note** "
        f"of **{fmt_r(debit_note)}** for returned goods that has not yet been processed by the supplier.\n\n"
        f"What is the **maximum additional credit order** {biz} can place with {sup} without exceeding the credit limit? "
        f"(plain number, no R or spaces)."
    )
    worked = (
        f"**{fmt_r(headroom)}** (`{headroom}`) [3 marks]\n\n"
        f"- **Adjusted Balance Owed**: ${fmt_r(curr_bal)} - {fmt_r(debit_note)} = {fmt_r(adj_bal)}$ [1 mark]\n"
        f"- **Available Credit Headroom**: ${fmt_r(limit)} - {fmt_r(adj_bal)} = {fmt_r(headroom)}$ (`{headroom}`) [2 marks]."
    )
    hints = {
        "tier_1": "First subtract the Debit Note from what is currently owed, then subtract that from the credit limit.",
        "tier_2": "Available Credit = Credit Limit - (Current Balance - Debit Note).",
        "tier_3": f"{limit} - ({curr_bal} - {debit_note}) = {limit} - {adj_bal} = {headroom}.",
    }
    return build_short(
        rng, qid="g9_cj_44", subskill="44_available_credit_headroom_before_order_calc",
        title="Calculate Available Credit Headroom Before Next Order",
        prompt=prompt, expected_answer=str(headroom), worked_solution=worked, hints=hints,
        marking_points=[
            {"id": "mp_1", "desc": f"Adjusts balance for Debit Note = {fmt_r(adj_bal)}", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": f"Finds available headroom {fmt_r(headroom)}", "marks": 2, "editable": True},
        ],
        misconception_tags=["added_debit_note_instead_of_subtracting"],
        marks=3, qtype="math_short",
    )


def arch_45_posting_cj_totals_to_general_ledger_table(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    ts_tot = rng.randint(20, 50) * 200
    st_tot = rng.randint(6, 18) * 100
    eq_tot = rng.randint(10, 25) * 200
    cc_tot = ts_tot + st_tot + eq_tot

    postings = [
        ("Trading Stock column total", "Trading Stock", "B5", "Debit", fmt_cell(ts_tot)),
        ("Stationery column total", "Stationery", "N1", "Debit", fmt_cell(st_tot)),
        ("Equipment (Sundry Accounts)", "Equipment", "B6", "Debit", fmt_cell(eq_tot)),
        ("Creditors Control column total", "Creditors Control", "B8", "Credit", fmt_cell(cc_tot)),
    ]
    rng.shuffle(postings)

    headers = ["CJ Column Total", "General Ledger Account", "Folio", "Debit or Credit", "Amount"]
    data_rows = [[col, acct, fol, dc, amt] for col, acct, fol, dc, amt in postings]
    given_coords = {(r, 0) for r in range(4)} | {(r, 2) for r in range(4)} | {(r, 4) for r in range(4)}
    rows, cmap = make_grid_rows(data_rows, given_coords)
    cell_hints = {
        f"t0_r{r}_c3": "Enter 'Debit' or 'Credit'." for r in range(4)
    }

    prompt = (
        f"At month-end, the CJ totals for **{biz}** are posted to the **General Ledger**.\n\n"
        f"Complete the **General Ledger Account** and **Debit or Credit** columns for each CJ total."
    )
    md_rows = "\n".join(f"| {c} | {a} | {f} | **{dc}** | {fmt_r(int(amt))} |" for c, a, f, dc, amt in postings)
    worked = (
        f"**Posting CJ Totals to General Ledger** [8 marks]\n\n"
        f"| CJ Column Total | General Ledger Account | Folio | Debit or Credit | Amount |\n|---|---|---|---|---:|\n{md_rows}\n\n"
        f"- **Double Entry Rule**: Debit Assets & Expenses ({ts_tot} + {st_tot} + {eq_tot} = {cc_tot}); Credit Liabilities (Creditors Control {cc_tot})."
    )
    hints = {
        "tier_1": "Trading Stock, Stationery, and Equipment are DEBITED. Creditors Control is CREDITED.",
        "tier_2": "Assets and expenses increase on the Debit side; Liabilities increase on the Credit side.",
        "tier_3": "Creditors Control = Credit; all other analysis totals = Debit.",
    }
    return build_table(
        rng, qid="g9_cj_45", subskill="45_posting_cj_totals_to_general_ledger_table",
        title="Post CJ Totals to General Ledger Accounts",
        prompt=prompt, headers=headers, rows=rows, correct_map=cmap, cell_hints=cell_hints,
        worked_solution=worked, sample_answer="See CJ posting table.",
        marks=8, hints=hints,
        marking_points=[{"id": "mp_1", "desc": "Accurate account names and Debit/Credit classifications", "marks": 8, "editable": True}],
        misconception_tags=["reversed_debit_credit_in_gl_posting"],
        journal_type="gl_posting",
    )


def arch_46_spot_recording_error_in_cj_double_counting_or_omitted_discount(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    sup, _ = rng.choice(CREDITOR_POOL)
    list_p = rng.randint(15, 35) * 200
    disc = rng.choice([10, 15, 20])
    disc_r = list_p * disc // 100
    net_p = list_p - disc_r

    prompt = (
        f"The trainee bookkeeper at **{biz}** recorded a credit purchase from **{sup}**:\n"
        f"- Catalogue price: **{fmt_r(list_p)}**, subject to a **{disc}% trade discount**.\n"
        f"- Trainee entered **{fmt_r(list_p)}** in Creditors Control, **{fmt_r(net_p)}** in Trading Stock, "
        f"and entered **{fmt_r(disc_r)}** as 'Discount Received' in Sundry Accounts.\n\n"
        f"Identify the bookkeeper's error and state the correct entry."
    )
    correct = (
        f"Trade discount should NOT be recorded as an account; the trainee must enter ONLY the net amount "
        f"({fmt_r(net_p)}) in BOTH Creditors Control and Trading Stock, with zero in Sundry Accounts."
    )
    distractors = [
        f"The trainee should have entered {fmt_r(list_p)} in Trading Stock and nothing in Creditors Control.",
        f"The trainee should have recorded {fmt_r(disc_r)} in the Debtors Journal instead of Sundry Accounts.",
        f"The entry was completely correct because South African law requires trade discount to be shown in Sundry Accounts.",
    ]
    explanation = (
        f"- **Rule**: **Trade discount is NEVER recorded in any journal or ledger account**.\n"
        f"- The invoice is recorded at the **net figure ({fmt_r(net_p)})** in **Creditors Control** "
        f"and in **Trading Stock**.\n"
        f"- Creating a 'Discount Received' Sundry entry incorrectly inflates both the liability and expenses/income."
    )
    hints = {
        "tier_1": "Remember the fundamental rule about trade discount in the Creditors Journal.",
        "tier_2": "Trade discount is deducted before writing up the journal; only the net amount appears.",
        "tier_3": f"Only {fmt_r(net_p)} should appear in Creditors Control and Trading Stock; trade discount is not an account.",
    }
    return build_mcq(
        rng, qid="g9_cj_46", subskill="46_spot_recording_error_in_cj_double_counting_or_omitted_discount",
        title="Spot the Bookkeeping Error: Trade Discount Treatment in CJ",
        prompt=prompt, correct_text=correct, distractors=distractors,
        explanation=explanation, hints=hints,
        misconception_tags=["trade_discount_recorded_in_sundry"],
    )


def arch_47_ethical_creditor_management_and_late_payment_risks(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    sup, _ = rng.choice(CREDITOR_POOL)

    prompt = (
        f"**{biz}**'s owner considers deliberately delaying payment to **{sup}** by 90 days "
        f"despite having agreed to 30-day credit terms, to use the supplier's cash as free working capital.\n\n"
        f"Which statement best explains why this practice is **unethical and harmful** to long-term business success?"
    )
    correct = (
        "It exploits the supplier's working capital unfairly, damages trust and business reputation, "
        "and leads to legal action, credit blacklisting, and refusal of credit by other suppliers."
    )
    distractors = [
        "It is standard smart practice that earns the business bonus points with the South African Chamber of Commerce.",
        "It automatically reduces the business's tax liability by 90% each month payment is delayed.",
        "It forces the supplier to lower their list prices on all future stock purchases by law.",
    ]
    explanation = (
        f"- Commercial credit is built on **mutual trust and contracts**.\n"
        f"- Unilateral delays harm the supplier's liquidity and result in credit bureau blacklisting, "
        f"penalty interest, and eventual bankruptcy of trading relationships."
    )
    hints = {
        "tier_1": "Think of business ethics, trust, and the consequences of defaulting on commercial contracts.",
        "tier_2": "Suppliers will cut off credit and report defaults to credit rating agencies.",
        "tier_3": "Unethical delay damages commercial reputation and cuts off future trade credit.",
    }
    return build_mcq(
        rng, qid="g9_cj_47", subskill="47_ethical_creditor_management_and_late_payment_risks",
        title="Business Ethics: Creditor Relations & Late Payment Risks",
        prompt=prompt, correct_text=correct, distractors=distractors,
        explanation=explanation, hints=hints,
        misconception_tags=["ethics_in_financial_literacy"],
    )


def arch_48_credit_cycle_document_matching_matrix_table(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)

    steps = [
        ("Step 1: Formal request to buy goods on credit", "Purchase Order", "None (filed in Order Book)"),
        ("Step 2: Goods delivered with bill from supplier", "Original Credit Invoice", "Creditors Journal (CJ)"),
        ("Step 3: Defective goods returned to supplier", "Debit Note", "Creditors Allowance Journal (CAJ)"),
        ("Step 4: Monthly settlement paid to supplier", "Bank Statement / EFT Proof", "Cash Payments Journal (CPJ)"),
    ]
    rng.shuffle(steps)

    headers = ["Cycle Stage", "Source Document", "Accounting Journal"]
    data_rows = [[st, doc, jrnl] for st, doc, jrnl in steps]
    given_coords = {(r, 0) for r in range(4)}
    rows, cmap = make_grid_rows(data_rows, given_coords)
    cell_hints = {
        f"t0_r{r}_c1": "Name the source document." for r in range(4)
    }

    prompt = (
        f"Match each stage in the **credit purchasing cycle** of **{biz}** to its correct **Source Document** "
        f"and **Accounting Journal** in the table below."
    )
    md_rows = "\n".join(f"| {st} | {doc} | {jrnl} |" for st, doc, jrnl in steps)
    worked = (
        f"**Credit Purchasing Cycle: Document & Journal Matrix** [8 marks]\n\n"
        f"| Cycle Stage | Source Document | Accounting Journal |\n|---|---|---|\n{md_rows}"
    )
    hints = {
        "tier_1": "Step 1 = Purchase Order; Step 2 = Original Invoice -> CJ; Step 3 = Debit Note -> CAJ; Step 4 = EFT/Bank -> CPJ.",
        "tier_2": "Original Invoice goes to CJ; Debit Note goes to CAJ.",
        "tier_3": "Order -> Invoice (CJ) -> Debit Note (CAJ) -> EFT/Bank (CPJ).",
    }
    return build_table(
        rng, qid="g9_cj_48", subskill="48_credit_cycle_document_matching_matrix_table",
        title="Credit Cycle Source Document Matching Matrix",
        prompt=prompt, headers=headers, rows=rows, correct_map=cmap, cell_hints=cell_hints,
        worked_solution=worked, sample_answer="See credit cycle matching matrix.",
        marks=8, hints=hints,
        marking_points=[{"id": "mp_1", "desc": "Accurate documents and journals for all 4 cycle stages", "marks": 8, "editable": True}],
        misconception_tags=["source_document_journal_mismatch"],
        journal_type="document_matching",
    )


def arch_49_combined_cj_and_cpj_net_cash_vs_credit_spending_calc(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    month, year, _ = rng.choice(MONTH_DATA)
    cash_stock = rng.randint(20, 60) * 500
    credit_stock = rng.randint(30, 80) * 500
    returns = rng.randint(3, 12) * 500
    net_credit_stock = credit_stock - returns
    total_stock_acquired = cash_stock + net_credit_stock

    prompt = (
        f"During **{month} {year}**, **{biz}** had these stock transactions:\n"
        f"- Cash purchases of trading stock recorded in CPJ: **{fmt_r(cash_stock)}**\n"
        f"- Credit purchases of trading stock recorded in CJ: **{fmt_r(credit_stock)}**\n"
        f"- Damaged trading stock returned to suppliers recorded in CAJ: **{fmt_r(returns)}**\n\n"
        f"Calculate the **net trading stock acquired** during the month (plain number, no R or spaces)."
    )
    worked = (
        f"**{fmt_r(total_stock_acquired)}** (`{total_stock_acquired}`) [3 marks]\n\n"
        f"- **Net Credit Purchases**: ${fmt_r(credit_stock)} - {fmt_r(returns)} = {fmt_r(net_credit_stock)}$ [1 mark]\n"
        f"- **Total Net Stock Acquired**: ${fmt_r(cash_stock)} + {fmt_r(net_credit_stock)} = {fmt_r(total_stock_acquired)}$ (`{total_stock_acquired}`) [2 marks]."
    )
    hints = {
        "tier_1": "Combine cash purchases from CPJ and net credit purchases from CJ minus CAJ.",
        "tier_2": "Total stock = Cash stock + Credit stock - Returned stock.",
        "tier_3": f"{cash_stock} + {credit_stock} - {returns} = {total_stock_acquired}.",
    }
    return build_short(
        rng, qid="g9_cj_49", subskill="49_combined_cj_and_cpj_net_cash_vs_credit_spending_calc",
        title="Calculate Total Net Stock Acquired (Cash CPJ + Credit CJ/CAJ)",
        prompt=prompt, expected_answer=str(total_stock_acquired), worked_solution=worked, hints=hints,
        marking_points=[
            {"id": "mp_1", "desc": f"Calculates net credit stock = {fmt_r(net_credit_stock)}", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": f"Sums cash and net credit stock = {fmt_r(total_stock_acquired)}", "marks": 2, "editable": True},
        ],
        misconception_tags=["omitted_returns_from_total_stock"],
        marks=3, qtype="math_short",
    )


def arch_50_capstone_cj_caj_cross_check_and_creditor_limit_audit_table(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    month, year, _ = rng.choice(MONTH_DATA)
    creds = pick_creditors(rng, 3)

    c1_pur = rng.randint(15, 30) * 400
    c1_ret = rng.randint(2, 6) * 400
    c1_pay = rng.randint(10, 20) * 400
    c1_net = c1_pur - c1_ret - c1_pay

    c2_pur = rng.randint(12, 28) * 400
    c2_ret = rng.randint(1, 4) * 400
    c2_pay = rng.randint(8, 16) * 400
    c2_net = c2_pur - c2_ret - c2_pay

    c3_pur = rng.randint(18, 35) * 400
    c3_ret = rng.randint(2, 5) * 400
    c3_pay = rng.randint(12, 24) * 400
    c3_net = c3_pur - c3_ret - c3_pay

    tot_pur = c1_pur + c2_pur + c3_pur
    tot_ret = c1_ret + c2_ret + c3_ret
    tot_pay = c1_pay + c2_pay + c3_pay
    tot_net = c1_net + c2_net + c3_net

    headers = ["Creditor", "Fol", "CJ Purchases", "CAJ Returns", "CPJ Payments", "Net Month-End Liability"]
    data_rows = [
        [creds[0][0], "C1", fmt_cell(c1_pur), fmt_cell(c1_ret), fmt_cell(c1_pay), fmt_cell(c1_net)],
        [creds[1][0], "C2", fmt_cell(c2_pur), fmt_cell(c2_ret), fmt_cell(c2_pay), fmt_cell(c2_net)],
        [creds[2][0], "C3", fmt_cell(c3_pur), fmt_cell(c3_ret), fmt_cell(c3_pay), fmt_cell(c3_net)],
        ["Totals", "", fmt_cell(tot_pur), fmt_cell(tot_ret), fmt_cell(tot_pay), fmt_cell(tot_net)],
    ]
    given_coords = {(r, 0) for r in range(3)} | {(r, 1) for r in range(3)} | {(r, 2) for r in range(3)} | {(r, 3) for r in range(3)} | {(r, 4) for r in range(3)}
    rows, cmap = make_grid_rows(data_rows, given_coords)
    cell_hints = {
        "t0_r3_c5": "Net Month-End Liability Total = CJ Total - CAJ Total - CPJ Total.",
    }

    prompt = (
        f"**Capstone Creditors Reconciliation for {biz} — {month} {year}**\n\n"
        f"Complete the **Net Month-End Liability** for each creditor and complete the **Totals row** "
        f"($\\text{{Net Liability}} = \\text{{Purchases}} - \\text{{Returns}} - \\text{{Payments}}$)."
    )
    worked = (
        f"**Capstone Creditors Reconciliation for {biz} — {month} {year}** [10 marks]\n\n"
        "| Creditor | Fol | CJ Purchases | CAJ Returns | CPJ Payments | Net Month-End Liability |\n"
        "|---|---|---:|---:|---:|---:|\n"
        f"| {creds[0][0]} | C1 | {fmt_cell(c1_pur)} | {fmt_cell(c1_ret)} | {fmt_cell(c1_pay)} | **{fmt_cell(c1_net)}** |\n"
        f"| {creds[1][0]} | C2 | {fmt_cell(c2_pur)} | {fmt_cell(c2_ret)} | {fmt_cell(c2_pay)} | **{fmt_cell(c2_net)}** |\n"
        f"| {creds[2][0]} | C3 | {fmt_cell(c3_pur)} | {fmt_cell(c3_ret)} | {fmt_cell(c3_pay)} | **{fmt_cell(c3_net)}** |\n"
        f"| **Totals** | | **{fmt_cell(tot_pur)}** | **{fmt_cell(tot_ret)}** | **{fmt_cell(tot_pay)}** | **{fmt_cell(tot_net)}** |\n\n"
        f"- **Reconciliation Check**: ${tot_pur} - {tot_ret} - {tot_pay} = {tot_net}$."
    )
    hints = {
        "tier_1": "For each row: Purchases - Returns - Payments = Net Month-End Liability.",
        "tier_2": "Sum each column vertically to complete the Totals row.",
        "tier_3": f"Totals: Purchases = {tot_pur}, Returns = {tot_ret}, Payments = {tot_pay}, Net Liability = {tot_net}.",
    }
    return build_table(
        rng, qid="g9_cj_50", subskill="50_capstone_cj_caj_cross_check_and_creditor_limit_audit_table",
        title="Capstone Synthesis: Creditors Reconciliation & Totals",
        prompt=prompt, headers=headers, rows=rows, correct_map=cmap, cell_hints=cell_hints,
        worked_solution=worked, sample_answer=f"Total Net Month-End Liability = {fmt_r(tot_net)}.",
        marks=10, hints=hints,
        marking_points=[{"id": "mp_1", "desc": "Accurately calculates net liabilities and column totals", "marks": 10, "editable": True}],
        misconception_tags=["capstone_creditors_reconciliation_error"],
        journal_type="capstone_reconciliation",
    )


ARCHETYPE_BUILDERS_26_50: Dict[str, Callable[[random.Random, str], Dict[str, Any]]] = {
    "26_caj_trade_discount_proportional_return_calc": arch_26_caj_trade_discount_proportional_return_calc,
    "27_caj_complete_3row_table": arch_27_caj_complete_3row_table,
    "28_caj_vs_cj_columns_comparison_table": arch_28_caj_vs_cj_columns_comparison_table,
    "29_transaction_analysis_credit_purchases_table": arch_29_transaction_analysis_credit_purchases_table,
    "30_classify_credit_purchases_asset_vs_expense_mcq": arch_30_classify_credit_purchases_asset_vs_expense_mcq,
    "31_double_entry_cj_posting_rule_mcq": arch_31_double_entry_cj_posting_rule_mcq,
    "32_accounting_equation_credit_purchase_of_trading_stock_table": arch_32_accounting_equation_credit_purchase_of_trading_stock_table,
    "33_accounting_equation_credit_purchase_of_equipment_table": arch_33_accounting_equation_credit_purchase_of_equipment_table,
    "34_accounting_equation_credit_expense_stationery_repairs_table": arch_34_accounting_equation_credit_expense_stationery_repairs_table,
    "35_accounting_equation_creditors_return_caj_stock_and_expense_table": arch_35_accounting_equation_creditors_return_caj_stock_and_expense_table,
    "36_accounting_equation_4row_cj_caj_mixed_table": arch_36_accounting_equation_4row_cj_caj_mixed_table,
    "37_cash_flow_planning_importance_of_creditors_records": arch_37_cash_flow_planning_importance_of_creditors_records,
    "38_early_settlement_vs_trade_discount_distinction": arch_38_early_settlement_vs_trade_discount_distinction,
    "39_calculate_creditors_outstanding_balance_table": arch_39_calculate_creditors_outstanding_balance_table,
    "40_calculate_creditors_total_owed_across_5_suppliers_calc": arch_40_calculate_creditors_total_owed_across_5_suppliers_calc,
    "41_evaluate_creditor_credit_limit_breaches_table": arch_41_evaluate_creditor_credit_limit_breaches_table,
    "42_evaluate_creditor_credit_term_days_compliance_mcq": arch_42_evaluate_creditor_credit_term_days_compliance_mcq,
    "43_rank_best_and_worst_managed_creditor_accounts_table": arch_43_rank_best_and_worst_managed_creditor_accounts_table,
    "44_available_credit_headroom_before_order_calc": arch_44_available_credit_headroom_before_order_calc,
    "45_posting_cj_totals_to_general_ledger_table": arch_45_posting_cj_totals_to_general_ledger_table,
    "46_spot_recording_error_in_cj_double_counting_or_omitted_discount": arch_46_spot_recording_error_in_cj_double_counting_or_omitted_discount,
    "47_ethical_creditor_management_and_late_payment_risks": arch_47_ethical_creditor_management_and_late_payment_risks,
    "48_credit_cycle_document_matching_matrix_table": arch_48_credit_cycle_document_matching_matrix_table,
    "49_combined_cj_and_cpj_net_cash_vs_credit_spending_calc": arch_49_combined_cj_and_cpj_net_cash_vs_credit_spending_calc,
    "50_capstone_cj_caj_cross_check_and_creditor_limit_audit_table": arch_50_capstone_cj_caj_cross_check_and_creditor_limit_audit_table,
}
