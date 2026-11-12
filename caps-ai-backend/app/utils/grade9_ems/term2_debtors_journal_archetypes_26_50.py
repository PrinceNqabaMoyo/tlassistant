"""Grade 9 EMS - Credit Transactions (Debtors 1): Archetypes 26 to 50.

Grounded strictly in:
- curriculum_docs_auto/EMS_Gr9/Term 3/01. Credit transactions (Debtors 1).md
- curriculum_docs/EMS_Gr9/Term 2/5-Credit transactions- Debtors 1.md

Imports shared builders and SA scenario helpers from `.term2_debtors_journal_archetypes_01_25`.
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List

from app.utils.ems_namelist import get_ems_scenario
from .term2_debtors_journal_archetypes_01_25 import (
    DEBTOR_POOL,
    MONTH_DATA,
    biz_name,
    build_mcq,
    build_short,
    build_table,
    fmt_r,
    make_grid_rows,
    pick_debtors,
    source_doc_svg,
)


def arch_26_why_document_is_called_credit_note(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    debtor, _ = rng.choice(DEBTOR_POOL)
    amt = rng.randint(2, 12) * 100

    prompt = (
        f"**{debtor}** returns defective goods worth **{fmt_r(amt)}** to **{biz}**. "
        f"**{biz}** issues a **Credit Note** (and enters the duplicate in the DAJ).\n\n"
        "Why is this source document called a **Credit Note**?"
    )
    correct = f"Because the customer's account ({debtor}) is credited — meaning the balance owed by the debtor decreases by {fmt_r(amt)}."
    distractors = [
        f"Because {debtor} is being granted extra credit to buy more stock worth {fmt_r(amt)}.",
        f"Because the business credits Bank in the Cash Payments Journal to refund cash immediately.",
        f"Because Credit Notes increase what {debtor} owes in the Debtors Journal.",
    ]
    return build_mcq(
        rng,
        qid="g9_dj_26",
        subskill="26_why_document_is_called_credit_note",
        title="Why a Credit Note Decreases a Debtor's Account",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"Debtors are Assets with Debit balances. Reducing what **{debtor}** owes requires a **credit entry** "
            f"of {fmt_r(amt)} on their account—hence the supplier calls the document a **Credit Note**."
        ),
        hints={
            "tier_1": "Debtors are Asset accounts: Debits increase them, Credits decrease them.",
            "tier_2": "Crediting a debtor's account writes down/reduces the amount they owe.",
            "tier_3": correct,
        },
        misconception_tags=["thinking_credit_note_grants_extra_credit"],
    )


def arch_27_daj_cost_of_sales_reversal_calculation(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    debtor, _ = rng.choice(DEBTOR_POOL)
    markup = rng.choice([25, 40, 50, 60, 80])
    cp_ret = rng.randint(4, 18) * 100
    sp_ret = cp_ret * (100 + markup) // 100
    cn_no = rng.randint(12, 68)

    prompt = (
        f"**{biz}** sells all trading stock at a mark-up of **{markup}% on cost**.\n\n"
        f"Debtor **{debtor}** returns undamaged wrong-size stock originally invoiced at **{fmt_r(sp_ret)}** "
        f"(Duplicate Credit Note **{cn_no}**).\n\n"
        "Calculate the **Cost of Sales** reversal in the **Debtors Allowance Journal (DAJ)** [3].\n"
        "*(Enter whole digits without spaces or the R symbol.)*"
    )
    worked = (
        f"**DAJ Cost of Sales Reversal (Credit Note {cn_no})** [3 marks]\n\n"
        f"- Returned Selling Price (Debtors Allowance): `{fmt_r(sp_ret)}`\n"
        f"- Cost price placed back into Trading Stock: `{sp_ret} × 100 / {100 + markup} = {fmt_r(cp_ret)}`\n"
        f"- Answer: `{cp_ret}`"
    )
    return build_short(
        rng,
        qid="g9_dj_27",
        subskill="27_daj_cost_of_sales_reversal_calculation",
        title="Calculate DAJ Cost of Sales Reversal",
        prompt=prompt,
        expected_answer=str(cp_ret),
        worked_solution=worked,
        marks=3,
        hints={
            "tier_1": "Use the exact same mark-up relationship as in the Debtors Journal.",
            "tier_2": f"Cost of Sales returned = {sp_ret} × 100 / {100 + markup}.",
            "tier_3": f"DAJ Cost of Sales = {cp_ret}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Applies 100/{100 + markup} to {sp_ret} = {cp_ret}", "marks": 3, "editable": True},
        ],
        misconception_tags=["omitting_cost_of_sales_in_daj"],
    )


def arch_28_daj_overcharge_allowance_no_stock_return_calc(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    debtor, _ = rng.choice(DEBTOR_POOL)
    billed = rng.randint(18, 35) * 100
    correct_amt = billed - rng.randint(2, 6) * 100
    overcharge = billed - correct_amt
    cn_no = rng.randint(41, 95)

    prompt = (
        f"**{biz}** mistakenly billed **{debtor}** **{fmt_r(billed)}** instead of **{fmt_r(correct_amt)}** on a prior invoice. "
        f"No physical goods were returned; Credit Note **{cn_no}** is issued solely to correct the price overcharge.\n\n"
        "What amounts go into the **Debtors Allowance** and **Cost of Sales** columns of the DAJ?"
    )
    correct = f"Debtors Allowance = {fmt_r(overcharge)}; Cost of Sales = R0 (blank), because no merchandise returned to stock."
    distractors = [
        f"Debtors Allowance = {fmt_r(billed)}; Cost of Sales = {fmt_r(correct_amt)}.",
        f"Debtors Allowance = {fmt_r(overcharge)}; Cost of Sales = {fmt_r(overcharge)} because both columns always match.",
        f"Debtors Allowance = R0; Cost of Sales = {fmt_r(overcharge)} in the Debtors Journal.",
    ]
    return build_mcq(
        rng,
        qid="g9_dj_28",
        subskill="28_daj_overcharge_allowance_no_stock_return_calc",
        title="DAJ Treatment of Price Overcharge Allowance",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"The overcharge is `{fmt_r(billed)} - {fmt_r(correct_amt)} = {fmt_r(overcharge)}`, entered in **Debtors Allowance**. "
            "Because **no physical stock came back** into the storeroom, **Cost of Sales stays blank / R0**."
        ),
        hints={
            "tier_1": "Ask whether any physical trading stock returned onto the shelves.",
            "tier_2": f"Allowance = {fmt_r(billed)} - {fmt_r(correct_amt)} = {fmt_r(overcharge)}; Cost of Sales = R0 for pure overcharges.",
            "tier_3": correct,
        },
        misconception_tags=["calculating_cost_of_sales_on_overcharge_allowance"],
    )


def arch_29_daj_complete_4row_table(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    m_name, yr, _ = rng.choice(MONTH_DATA)
    markup = rng.choice([25, 50, 80])
    debtors = pick_debtors(rng, 3)
    cn0 = rng.randint(11, 35)
    cp1, cp2, cp3 = rng.randint(4, 10) * 100, rng.randint(3, 8) * 100, rng.randint(5, 12) * 100
    sp1, sp2, sp3 = [c * (100 + markup) // 100 for c in (cp1, cp2, cp3)]
    overcharge = rng.choice([150, 200, 250, 300])

    txns = [
        f"Day 07: {debtors[0][0]} ({debtors[0][1]}) returned damaged stock, {fmt_r(sp1)}. Issued Credit Note {cn0}.",
        f"Day 14: Issued Credit Note {cn0 + 1} to {debtors[1][0]} ({debtors[1][1]}) for wrong-size goods returned, {fmt_r(sp2)}.",
        f"Day 21: Granted {debtors[2][0]} ({debtors[2][1]}) an allowance of {fmt_r(overcharge)} via Credit Note {cn0 + 2} for an invoice overcharge (no goods returned).",
        f"Day 28: {debtors[0][0]} ({debtors[0][1]}) returned defective items sold at {fmt_r(sp3)} (Credit Note {cn0 + 3}).",
    ]
    data_rows = [
        [str(cn0), "7", debtors[0][0], debtors[0][1], str(sp1), str(cp1)],
        [str(cn0 + 1), "14", debtors[1][0], debtors[1][1], str(sp2), str(cp2)],
        [str(cn0 + 2), "21", debtors[2][0], debtors[2][1], str(overcharge), ""],
        [str(cn0 + 3), "28", debtors[0][0], debtors[0][1], str(sp3), str(cp3)],
    ]
    headers = ["Doc No", "Day", "Debtor", "Fol", "Debtors Allowance", "Cost of Sales"]
    rows, correct_map = make_grid_rows(data_rows)
    cell_hints = {
        "t0_r0_c5": f"Cost of Sales = {sp1} × 100 / {100 + markup} = {cp1}.",
        "t0_r1_c5": f"Cost of Sales = {sp2} × 100 / {100 + markup} = {cp2}.",
        "t0_r2_c5": "Price overcharge only (no physical stock returned) -> leave Cost of Sales EMPTY.",
        "t0_r3_c5": f"Cost of Sales = {sp3} × 100 / {100 + markup} = {cp3}.",
    }
    tot_allow = sp1 + sp2 + overcharge + sp3
    tot_cos = cp1 + cp2 + cp3
    md_rows = "\n".join(
        f"| {r[0]} | {r[1]} | {r[2]} | {r[3]} | {r[4]} | {r[5] or '—'} |" for r in data_rows
    )
    worked = (
        f"**Debtors Allowance Journal of {biz} for {m_name} {yr}** [12 marks]\n\n"
        "| Doc No | Day | Debtor | Fol | Debtors Allowance | Cost of Sales |\n| --- | --- | --- | --- | --- | --- |\n"
        f"{md_rows}\n| | | **TOTAL** | | **{tot_allow}** | **{tot_cos}** |\n\n"
        f"Note: Credit Note {cn0 + 2} (Day 21) is an overcharge rebate with **no stock returned**, so Cost of Sales stays blank."
    )
    prompt = (
        f"Complete the **Debtors Allowance Journal (DAJ)** of **{biz}** for **{m_name} {yr}** (mark-up **{markup}% on cost**).\n"
        "*(Leave Cost of Sales blank if no physical goods were returned; enter digits without spaces or R.)*"
    )
    return build_table(
        rng,
        qid="g9_dj_29",
        subskill="29_daj_complete_4row_table",
        title="Complete Full Debtors Allowance Journal (DAJ)",
        prompt=prompt,
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=f"Total Debtors Allowance = {tot_allow}; Total Cost of Sales = {tot_cos}.",
        marks=12,
        hints={
            "tier_1": "Record Credit Note numbers, Days, Debtors, Folios, Allowance amounts, and Cost of Sales (except overcharges).",
            "tier_2": f"Day 21 overcharge ({fmt_r(overcharge)}) has blank Cost of Sales; compute CP = SP × 100/{100+markup} for Days 7, 14, 28.",
            "tier_3": f"Total DAJ Allowance = {tot_allow}; Total DAJ Cost of Sales = {tot_cos}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Returns Days 7, 14, 28 with CoS ({cp1}, {cp2}, {cp3})", "marks": 9, "editable": True},
            {"id": "mp_2", "desc": f"Day 21 overcharge ({overcharge}) leaves CoS blank", "marks": 3, "editable": True},
        ],
        misconception_tags=["computing_cost_of_sales_for_overcharge_rebate"],
        journal_type="daj",
        transactions=txns,
    )


def arch_30_daj_vs_dj_side_by_side_comparison_table(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    rows_spec = rng.sample([
        ("Source Document", "Duplicate Invoice", "Duplicate Credit Note"),
        ("Effect on Debtor Balance", "Increases (+)", "Decreases (-)"),
        ("Effect on Trading Stock", "Decreases (stock leaves)", "Increases (stock returns)"),
        ("Main Folio Prefix", "D1 / D2 / D3 (Debtors Ledger)", "D1 / D2 / D3 (Debtors Ledger)"),
        ("Selling-Value Column Name", "Sales", "Debtors Allowance"),
    ], 4)
    headers = ["Comparison Dimension", "Debtors Journal (DJ)", "Debtors Allowance Journal (DAJ)"]
    data_rows = [[dim, dj_v, daj_v] for dim, dj_v, daj_v in rows_spec]
    given = {(i, 0) for i in range(4)} | {(0, 1), (2, 2)}
    rows, correct_map = make_grid_rows(data_rows, given_coords=given)
    cell_hints = {
        f"t0_r{i}_c1": f"DJ value for '{dim}': {dj_v}" for i, (dim, dj_v, _) in enumerate(rows_spec) if (i, 1) not in given
    }
    cell_hints.update({
        f"t0_r{i}_c2": f"DAJ value for '{dim}': {daj_v}" for i, (dim, _, daj_v) in enumerate(rows_spec) if (i, 2) not in given
    })
    prompt = "Complete the missing cells comparing the **Debtors Journal (DJ)** and the **Debtors Allowance Journal (DAJ)**."
    md_rows = "\n".join(f"| {a} | {b} | {c} |" for a, b, c in data_rows)
    worked = "**DJ vs DAJ Comparison Matrix** [6 marks]\n\n| Dimension | DJ | DAJ |\n| --- | --- | --- |\n" + md_rows
    return build_table(
        rng,
        qid="g9_dj_30",
        subskill="30_daj_vs_dj_side_by_side_comparison_table",
        title="Compare Debtors Journal vs Debtors Allowance Journal",
        prompt=prompt,
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer="; ".join(f"{a}: {b} vs {c}" for a, b, c in data_rows),
        marks=6,
        hints={
            "tier_1": "DJ records credit sales (invoices); DAJ reverses them on returns/allowances (credit notes).",
            "tier_2": "Recall source documents (Duplicate Invoice vs Duplicate Credit Note) and opposite effects on debtor debt.",
            "tier_3": "; ".join(f"{a}: DJ={b}, DAJ={c}" for a, b, c in rows_spec),
        },
        marking_points=[
            {"id": "mp_1", "desc": "Accurate DJ vs DAJ entries across all dimensions", "marks": 6, "editable": True},
        ],
        misconception_tags=["confusing_invoice_and_credit_note_effects"],
        journal_type="comparison_matrix",
    )


def arch_31_crj_debtor_receipt_source_document_svg(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    debtor, fol = rng.choice(DEBTOR_POOL[:4])
    rec_no = rng.randint(55, 98)
    m_name, yr, _ = rng.choice(MONTH_DATA)
    day = rng.randint(3, 27)
    amt = rng.randint(8, 36) * 100

    svg = source_doc_svg(
        f"DUPLICATE RECEIPT — {biz}",
        f"R-{rec_no}",
        f"{day:02d} {m_name} {yr}",
        [
            ("Received From", f"{debtor} ({fol})"),
            ("In Payment Of", "Settlement on credit account"),
            ("Amount Received", fmt_r(amt)),
            ("Method", "Cash / Till drawer"),
        ],
        accent="#0f766e",
    )
    prompt = (
        f"Inspect the **Duplicate Receipt** (`R-{rec_no}`) issued by **{biz}** to **{debtor}** in the source document card below.\n\n"
        f"Which **CRJ columns** record this **{fmt_r(amt)}** settlement (assuming it is the only receipt deposited that day)?"
    )
    correct = "Analysis of Receipts, Bank, and Debtors Control (NOT Sales)."
    distractors = [
        "Analysis of Receipts, Bank, Sales, and Cost of Sales.",
        "Debtors Journal Sales column and Cost of Sales column.",
        "Bank and Sundry Accounts -> Debtors Allowance in the CPJ.",
    ]
    return build_mcq(
        rng,
        qid="g9_dj_31",
        subskill="31_crj_debtor_receipt_source_document_svg",
        title="Read Duplicate Receipt for Debtor Settlement",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"When **{debtor}** pays off an existing debt of **{fmt_r(amt)}**, the sale was ALREADY recorded earlier in the DJ. "
            "So the CRJ records it in **Analysis of Receipts** (till), **Bank** (deposit), and **Debtors Control** — never Sales again."
        ),
        hints={
            "tier_1": "Was this goods sold today, or a customer paying off an older invoice?",
            "tier_2": "Collecting from a debtor enters Analysis of Receipts, Bank, and Debtors Control.",
            "tier_3": correct,
        },
        misconception_tags=["double_counting_debtor_receipt_as_sales"],
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    )


def arch_32_crj_debtors_control_column_recording_rule(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    debtor, _ = rng.choice(DEBTOR_POOL)
    amt = rng.randint(10, 40) * 100

    prompt = (
        f"**{debtor}** comes into **{biz}** to pay **{fmt_r(amt)}** toward goods bought on credit last month.\n\n"
        "Why is it an accounting error to record this receipt in the **Sales** column of the Cash Receipts Journal (CRJ)?"
    )
    correct = "Because the sale revenue was already recorded in the Debtors Journal (DJ) when the invoice was issued; recording it in CRJ Sales would double-count Sales and fail to reduce Debtors Control."
    distractors = [
        "Because customer payments always belong in the Cash Payments Journal (CPJ) under Drawings.",
        "Because CRJ only records Bank totals without any analysis columns for Debtors.",
        "Because receipts from debtors must be multiplied by Cost of Sales before banking.",
    ]
    return build_mcq(
        rng,
        qid="g9_dj_32",
        subskill="32_crj_debtors_control_column_recording_rule",
        title="Why Debtor Receipts Exclude Sales Column",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            "Revenue (`Sales`) is recognised **once** when credit goods are invoiced in the **DJ**. "
            "Later cash collections enter **Debtors Control** in the **CRJ** to convert the receivable into Bank cash."
        ),
        hints={
            "tier_1": "Remember when Sales was already counted for that credit purchase.",
            "tier_2": "Putting debtor payments into Sales would count the exact same revenue twice.",
            "tier_3": correct,
        },
        misconception_tags=["double_counting_debtor_receipt_as_sales"],
    )


def arch_33_crj_settlement_full_opening_debt_calc(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    debtors = pick_debtors(rng, 2)
    bal1 = rng.randint(12, 35) * 50
    bal2 = rng.randint(8, 28) * 50
    new_sale = rng.randint(6, 18) * 100
    m_name, yr, _ = rng.choice(MONTH_DATA)

    prompt = (
        f"Debtors List of **{biz}** on **1 {m_name} {yr}**:\n"
        f"- **{debtors[0][0]}:** {fmt_r(bal1)}\n"
        f"- **{debtors[1][0]}:** {fmt_r(bal2)}\n\n"
        f"On **10 {m_name}**, {debtors[0][0]} buys goods on credit for {fmt_r(new_sale)}.\n"
        f"On **17 {m_name}**, **{debtors[0][0]}** sends a payment to settle **the debt as at 1 {m_name} {yr}** in full.\n\n"
        f"Calculate the amount to record in **Debtors Control** of the CRJ on **17 {m_name}** [2].\n"
        "*(Enter whole digits without spaces or the R symbol.)*"
    )
    worked = (
        f"**Settlement of Opening Balance (`1 {m_name} {yr}`)** [2 marks]\n\n"
        f"- The wording *'debt as at 1 {m_name}'* refers strictly to the opening balance (**{fmt_r(bal1)}**), "
        f"excluding the new {fmt_r(new_sale)} credit sale on 10 {m_name}.\n"
        f"- CRJ Debtors Control entry: `{bal1}`"
    )
    return build_short(
        rng,
        qid="g9_dj_33",
        subskill="33_crj_settlement_full_opening_debt_calc",
        title="CRJ Receipt: Settlement of 1st-of-Month Debt",
        prompt=prompt,
        expected_answer=str(bal1),
        worked_solution=worked,
        marks=2,
        hints={
            "tier_1": "Read the exact cutoff date carefully: 'debt as at 1st of the month'.",
            "tier_2": f"Ignore the 10 {m_name} invoice ({fmt_r(new_sale)}); pay only the 1 {m_name} balance.",
            "tier_3": f"Receipt amount = {bal1}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Selects opening balance {bal1} (excludes 10th sale)", "marks": 2, "editable": True},
        ],
        misconception_tags=["including_current_month_invoices_when_settling_opening_balance"],
    )


def arch_34_crj_settlement_up_to_date_after_credit_sale_calc(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    debtor, fol = rng.choice(DEBTOR_POOL[:4])
    m_name, yr, _ = rng.choice(MONTH_DATA)
    open_bal = rng.randint(4, 15) * 100
    inv1 = rng.randint(8, 22) * 100
    ret1 = rng.randint(2, 5) * 100
    inv2 = rng.randint(5, 14) * 100
    due_to_date = open_bal + inv1 - ret1

    prompt = (
        f"**{debtor} ({fol})** has an opening balance of **{fmt_r(open_bal)}** owed to **{biz}** on **1 {m_name} {yr}**.\n\n"
        f"Month events for {debtor}:\n"
        f"- **08 {m_name}:** Bought goods on credit, **{fmt_r(inv1)}** (DJ)\n"
        f"- **14 {m_name}:** Returned damaged stock for Credit Note, **{fmt_r(ret1)}** (DAJ)\n"
        f"- **22 {m_name}:** Paid the full balance owing **to date** (Receipt issued, CRJ)\n"
        f"- **29 {m_name}:** Bought goods on credit, **{fmt_r(inv2)}** (DJ)\n\n"
        f"Calculate the **CRJ Debtors Control** amount received from **{debtor}** on **22 {m_name}** [3].\n"
        "*(Enter whole digits without spaces or the R symbol.)*"
    )
    worked = (
        f"**Account Balance Up to Date (22 {m_name})** [3 marks]\n\n"
        f"- Opening balance (1 {m_name}): `{fmt_r(open_bal)}`\n"
        f"- Plus 08 {m_name} credit sale (DJ): `+{fmt_r(inv1)}`\n"
        f"- Less 14 {m_name} credit note (DAJ): `-{fmt_r(ret1)}`\n"
        f"- Balance settled up to **22 {m_name}**: `{open_bal} + {inv1} - {ret1} = {due_to_date}`\n"
        f"*(The 29 {m_name} invoice happens AFTER 22 {m_name}, so it is excluded.)*"
    )
    return build_short(
        rng,
        qid="g9_dj_34",
        subskill="34_crj_settlement_up_to_date_after_credit_sale_calc",
        title="CRJ Receipt: Full Settlement Up to Date",
        prompt=prompt,
        expected_answer=str(due_to_date),
        worked_solution=worked,
        marks=3,
        hints={
            "tier_1": "Track every transaction UP TO the payment date (22nd), and exclude anything dated after.",
            "tier_2": f"Compute Opening ({open_bal}) + 08th Invoice ({inv1}) - 14th Credit Note ({ret1}).",
            "tier_3": f"Settlement received on 22nd = {due_to_date}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": "Adds DJ invoice and subtracts DAJ return up to 22nd", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": f"Excludes 29th invoice; total = {due_to_date}", "marks": 1, "editable": True},
        ],
        misconception_tags=["forgetting_to_subtract_credit_note_before_settlement"],
    )


def arch_35_crj_partial_settlement_and_remaining_debt_calc(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    debtor, _ = rng.choice(DEBTOR_POOL)
    total_owed = rng.randint(12, 40) * 200
    pct = rng.choice([25, 40, 50, 60, 75])
    paid = total_owed * pct // 100
    remaining = total_owed - paid

    prompt = (
        f"**{debtor}** owes **{biz}** **{fmt_r(total_owed)}** on account.\n\n"
        f"On payday, **{debtor}** settles **{pct}%** of the debt via EFT and promises to pay the remainder next month.\n\n"
        "Calculate the **remaining balance** still owed by {0} **after** this partial payment [3].\n"
        "*(Enter whole digits without spaces or the R symbol.)*".format(debtor)
    )
    worked = (
        "**Step 1 — Cash Received in CRJ (Debtors Control):**\n"
        f"`{pct}% × {fmt_r(total_owed)} = {fmt_r(paid)}` [1]\n\n"
        "**Step 2 — Remaining Debtor Balance:**\n"
        f"`{fmt_r(total_owed)} - {fmt_r(paid)} = {fmt_r(remaining)}` [2] -> Answer: `{remaining}`"
    )
    return build_short(
        rng,
        qid="g9_dj_35",
        subskill="35_crj_partial_settlement_and_remaining_debt_calc",
        title="Partial Settlement & Remaining Debtor Debt",
        prompt=prompt,
        expected_answer=str(remaining),
        worked_solution=worked,
        marks=3,
        hints={
            "tier_1": "First find the amount paid into CRJ, then subtract it from total debt.",
            "tier_2": f"Paid = {total_owed} × {pct}/100 = {paid}.",
            "tier_3": f"Remaining debt = {total_owed} - {paid} = {remaining}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": f"CRJ payment = {fmt_r(paid)}", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": f"Remaining debt = {remaining}", "marks": 2, "editable": True},
        ],
        misconception_tags=["reporting_amount_paid_instead_of_remaining_balance"],
    )


def arch_36_crj_complete_with_debtors_control_table(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    m_name, yr, _ = rng.choice(MONTH_DATA)
    markup = rng.choice([25, 50])
    debtors = pick_debtors(rng, 2)
    cap_amt = rng.randint(20, 40) * 1000
    cos1 = rng.randint(12, 26) * 100
    sales1 = cos1 * (100 + markup) // 100
    deb1 = rng.randint(6, 18) * 100
    deb2 = rng.randint(8, 22) * 100
    rec0 = rng.randint(51, 80)

    txns = [
        f"Day 01: Owner {sc['entrepreneur']} increased capital by {fmt_r(cap_amt)} (direct EFT into bank; Receipt {rec0}).",
        f"Day 09: Cash sales per Cash Register Roll (CRR), {fmt_r(sales1)}.",
        f"Day 15: Received {fmt_r(deb1)} cash in the till from {debtors[0][0]} ({debtors[0][1]}) in settlement of account (Receipt {rec0 + 1}; banked at day-end).",
        f"Day 24: {debtors[1][0]} ({debtors[1][1]}) paid {fmt_r(deb2)} cash into the till on account (Receipt {rec0 + 2}; banked at day-end).",
    ]
    headers = [
        "Doc No", "Day", "Details", "Fol",
        "Analysis", "Bank", "Sales", "Cost of Sales",
        "Debtors Control", "Sundry Amt", "Sundry Details",
    ]
    data_rows = [
        [str(rec0), "1", sc["entrepreneur"], "", "", str(cap_amt), "", "", "", str(cap_amt), "Capital"],
        ["CRR", "9", "Sales", "", str(sales1), str(sales1), str(sales1), str(cos1), "", "", ""],
        [str(rec0 + 1), "15", debtors[0][0], debtors[0][1], str(deb1), str(deb1), "", "", str(deb1), "", ""],
        [str(rec0 + 2), "24", debtors[1][0], debtors[1][1], str(deb2), str(deb2), "", "", str(deb2), "", ""],
    ]
    given = {(i, 0) for i in range(4)} | {(i, 1) for i in range(4)} | {(i, 2) for i in range(4)} | {(i, 3) for i in range(4)}
    rows, correct_map = make_grid_rows(data_rows, given_coords=given)
    cell_hints = {
        "t0_r0_c4": "Direct EFT into Bank skips Analysis of Receipts — leave Analysis EMPTY.",
        "t0_r0_c9": f"Capital goes to Sundry Amount = {cap_amt}.",
        "t0_r1_c7": f"Cost of Sales = {sales1} × 100 / {100 + markup} = {cos1}.",
        "t0_r2_c8": f"Debtor receipt goes to Debtors Control = {deb1} (NOT Sales).",
        "t0_r3_c8": f"Debtor receipt goes to Debtors Control = {deb2} (NOT Sales).",
    }
    bank_tot = cap_amt + sales1 + deb1 + deb2
    deb_tot = deb1 + deb2
    prompt = (
        f"Complete the money columns of the **Cash Receipts Journal (CRJ)** for **{biz}** for **{m_name} {yr}** "
        f"(mark-up **{markup}% on cost**). Leave unused cells empty *(digits only, no spaces or R)*."
    )
    worked = (
        f"**Completed CRJ with Debtors Control Column ({m_name} {yr})** [10 marks]\n\n"
        "| Doc | Day | Details | Fol | Analysis | Bank | Sales | CoS | Debtors Control | Sundry | Account |\n"
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |\n"
        f"| {rec0} | 1 | {sc['entrepreneur']} | | — | {cap_amt} | — | — | — | {cap_amt} | Capital |\n"
        f"| CRR | 9 | Sales | | {sales1} | {sales1} | {sales1} | {cos1} | — | — | — |\n"
        f"| {rec0+1} | 15 | {debtors[0][0]} | {debtors[0][1]} | {deb1} | {deb1} | — | — | {deb1} | — | — |\n"
        f"| {rec0+2} | 24 | {debtors[1][0]} | {debtors[1][1]} | {deb2} | {deb2} | — | — | {deb2} | — | — |\n\n"
        f"Bank Total = `{bank_tot}`; Debtors Control Total = `{deb_tot}`."
    )
    return build_table(
        rng,
        qid="g9_dj_36",
        subskill="36_crj_complete_with_debtors_control_table",
        title="CRJ with Debtors Control Column",
        prompt=prompt,
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=f"Bank={bank_tot}; Sales={sales1}; CoS={cos1}; Debtors Control={deb_tot}; Sundry={cap_amt} (Capital)",
        marks=10,
        hints={
            "tier_1": "Direct EFT skips Analysis; Cash Sales fills Sales + CoS; Debtor receipts fill Debtors Control.",
            "tier_2": f"Day 15 ({deb1}) and Day 24 ({deb2}) belong in Debtors Control, NOT Sales.",
            "tier_3": f"Bank Total = {bank_tot}; Debtors Control Total = {deb_tot}; CoS = {cos1}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Direct EFT Capital {cap_amt} skips Analysis", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": f"Cash sales {sales1} & CoS {cos1}", "marks": 3, "editable": True},
            {"id": "mp_3", "desc": f"Debtors Control entries {deb1} and {deb2}", "marks": 5, "editable": True},
        ],
        misconception_tags=["recording_debtor_receipts_in_crj_sales_column"],
        journal_type="crj",
        transactions=txns,
    )


def arch_37_crj_same_day_banking_cash_sales_and_debtor_receipt(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    debtor, _ = rng.choice(DEBTOR_POOL)
    crr_amt = rng.randint(14, 38) * 100
    debt_amt = rng.randint(6, 22) * 100
    bank_day = crr_amt + debt_amt
    day = rng.randint(5, 25)

    prompt = (
        f"On **Day {day}**, **{biz}** receives two cash amounts in the shop till and banks all till money together at closing:\n"
        f"1. **Cash sales (CRR):** {fmt_r(crr_amt)}\n"
        f"2. **Receipt from debtor {debtor}:** {fmt_r(debt_amt)}\n\n"
        f"Calculate the single combined deposit entered in the **Bank** column of the CRJ for **Day {day}** [2].\n"
        "*(Enter whole digits without spaces or the R symbol.)*"
    )
    worked = (
        f"**Same-Day Banking Deposit (Day {day})** [2 marks]\n\n"
        f"- Analysis of Receipts: `{fmt_r(crr_amt)}` and `{fmt_r(debt_amt)}`\n"
        f"- Single combined Bank deposit on the final line of Day {day}: `{crr_amt} + {debt_amt} = {bank_day}`"
    )
    return build_short(
        rng,
        qid="g9_dj_37",
        subskill="37_crj_same_day_banking_cash_sales_and_debtor_receipt",
        title="Same-Day Banking: Cash Sales + Debtor Receipt",
        prompt=prompt,
        expected_answer=str(bank_day),
        worked_solution=worked,
        marks=2,
        hints={
            "tier_1": "Cash sitting in the till on the same calendar day is deposited at the bank in ONE combined batch.",
            "tier_2": f"Sum {fmt_r(crr_amt)} and {fmt_r(debt_amt)}.",
            "tier_3": f"Bank deposit = {bank_day}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Combined daily Bank deposit = {bank_day}", "marks": 2, "editable": True},
        ],
        misconception_tags=["banking_same_day_till_receipts_separately"],
    )


def arch_38_crj_direct_eft_payment_by_debtor_rule(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    debtor, _ = rng.choice(DEBTOR_POOL)
    amt = rng.randint(15, 55) * 100

    prompt = (
        f"**{debtor}** transfers **{fmt_r(amt)}** directly into **{biz}**'s business bank account via **EFT** "
        "to settle an overdue invoice.\n\n"
        f"How must **{biz}** record this **{fmt_r(amt)}** EFT in the Cash Receipts Journal (CRJ)?"
    )
    correct = f"Leave Analysis of Receipts blank, enter {fmt_r(amt)} directly into Bank, and enter {fmt_r(amt)} in Debtors Control."
    distractors = [
        f"Enter {fmt_r(amt)} in Analysis of Receipts and leave Bank blank until cash is withdrawn.",
        f"Enter {fmt_r(amt)} in Bank and Sales so total profit increases immediately.",
        f"Enter {fmt_r(amt)} in the Debtors Journal as a negative credit sale.",
    ]
    return build_mcq(
        rng,
        qid="g9_dj_38",
        subskill="38_crj_direct_eft_payment_by_debtor_rule",
        title="Debtor Direct EFT Deposit in CRJ",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            "Money paid via **EFT** goes directly into the business bank account without passing through the shop till, "
            "so **Analysis of Receipts** stays empty and the entry goes straight to **Bank** and **Debtors Control**."
        ),
        hints={
            "tier_1": "Did the cash ever touch the physical till drawer?",
            "tier_2": "Direct EFTs bypass Analysis of Receipts and enter Bank + Debtors Control directly.",
            "tier_3": correct,
        },
        misconception_tags=["entering_direct_eft_in_analysis_of_receipts"],
    )


def arch_39_crj_discount_allowed_vs_settlement_amount_check(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    debtor, _ = rng.choice(DEBTOR_POOL)
    owed = rng.randint(10, 30) * 200
    disc_pct = rng.choice([5, 10])
    disc_amt = owed * disc_pct // 100
    cash_rec = owed - disc_amt

    prompt = (
        f"**{debtor}** owes **{biz}** **{fmt_r(owed)}** and qualifies for a **{disc_pct}% early-settlement discount** "
        "by paying before the 30-day deadline.\n\n"
        f"Calculate the actual **Rand cash amount** received in the CRJ **Bank** column [3].\n"
        "*(Enter whole digits without spaces or the R symbol.)*"
    )
    worked = (
        "**Step 1 — Early-Settlement Discount Allowed:**\n"
        f"`{disc_pct}% × {fmt_r(owed)} = {fmt_r(disc_amt)}` [1]\n\n"
        "**Step 2 — Actual Cash Received (Bank):**\n"
        f"`{fmt_r(owed)} - {fmt_r(disc_amt)} = {fmt_r(cash_rec)}` [2] -> Answer: `{cash_rec}`"
    )
    return build_short(
        rng,
        qid="g9_dj_39",
        subskill="39_crj_discount_allowed_vs_settlement_amount_check",
        title="Early-Settlement Cash Received Calculation",
        prompt=prompt,
        expected_answer=str(cash_rec),
        worked_solution=worked,
        marks=3,
        hints={
            "tier_1": "Subtract the settlement discount from the total debt owed.",
            "tier_2": f"Discount = {owed} × {disc_pct}/100 = {disc_amt}.",
            "tier_3": f"Cash banked = {owed} - {disc_amt} = {cash_rec}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Discount = {disc_amt}", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": f"Net cash banked = {cash_rec}", "marks": 2, "editable": True},
        ],
        misconception_tags=["adding_discount_instead_of_subtracting"],
    )


def arch_40_combined_dj_and_crj_transaction_routing_table(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    debtor, _ = rng.choice(DEBTOR_POOL)
    a1, a2, a3, a4 = [rng.randint(5, 25) * 100 for _ in range(4)]

    items = [
        (f"Sold stock on credit to {debtor}, R{a1}", "DJ", "Duplicate Invoice", str(a1)),
        (f"Received EFT from {debtor} on account, R{a2}", "CRJ", "Duplicate Receipt", str(a2)),
        (f"Issued Credit Note to {debtor} for returns, R{a3}", "DAJ", "Duplicate Credit Note", str(a3)),
        (f"Cash register sales for the day, R{a4}", "CRJ", "Cash Register Roll", str(a4)),
    ]
    rng.shuffle(items)
    headers = ["Transaction Description", "Journal (DJ / DAJ / CRJ)", "Source Document", "Amount (R)"]
    data_rows = [[desc, jrn, doc, amt] for desc, jrn, doc, amt in items]
    rows, correct_map = make_grid_rows(data_rows, given_coords={(i, 0) for i in range(4)} | {(i, 3) for i in range(4)})
    cell_hints = {
        f"t0_r{i}_c1": f"Journal for '{desc[:28]}...' is {jrn}." for i, (desc, jrn, _, _) in enumerate(items)
    }
    prompt = f"Route each transaction of **{biz}** to its correct **Journal** and **Source Document** in the table below."
    md_rows = "\n".join(f"| {a} | **{b}** | **{c}** | {d} |" for a, b, c, d in items)
    worked = "**Transaction Routing Summary** [8 marks]\n\n| Transaction | Journal | Source Document | Amount |\n| --- | --- | --- | --- |\n" + md_rows
    return build_table(
        rng,
        qid="g9_dj_40",
        subskill="40_combined_dj_and_crj_transaction_routing_table",
        title="Route Transactions to Journal & Source Document",
        prompt=prompt,
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer="; ".join(f"{b} ({c})" for _, b, c, _ in items),
        marks=8,
        hints={
            "tier_1": "Pair each credit sale/return/receipt with its matching duplicate document.",
            "tier_2": "Credit sale = DJ (Duplicate Invoice); Return = DAJ (Duplicate Credit Note); Receipts/Cash sales = CRJ.",
            "tier_3": "; ".join(f"{b} -> {c}" for _, b, c, _ in items),
        },
        marking_points=[
            {"id": f"mp_{i+1}", "desc": f"Row {i+1}: {b} + {c}", "marks": 2, "editable": True}
            for i, (_, b, c, _) in enumerate(items)
        ],
        misconception_tags=["mismatched_source_document_and_journal"],
        journal_type="routing_table",
    )


def arch_41_debtors_control_opening_plus_dj_minus_crj_daj_calc(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    open_bal = rng.randint(10, 30) * 1000
    dj_sales = rng.randint(15, 35) * 1000
    daj_ret = rng.randint(1, 5) * 1000
    crj_rec = rng.randint(12, 28) * 1000
    closing = open_bal + dj_sales - daj_ret - crj_rec

    prompt = (
        f"At the start of the month, debtors owed **{biz}** **{fmt_r(open_bal)}**.\n\n"
        "Monthly journal totals affecting debtors:\n"
        f"- **Debtors Journal (Sales):** {fmt_r(dj_sales)}\n"
        f"- **Debtors Allowance Journal:** {fmt_r(daj_ret)}\n"
        f"- **Cash Receipts Journal (Debtors Control):** {fmt_r(crj_rec)}\n\n"
        "Calculate the total amount owed by debtors at month-end [3].\n"
        "*(Enter whole digits without spaces or the R symbol.)*"
    )
    worked = (
        "**Closing Debtors Control Formula** [3 marks]\n\n"
        f"`Closing = Opening ({fmt_r(open_bal)}) + DJ Credit Sales ({fmt_r(dj_sales)}) "
        f"- DAJ Allowances ({fmt_r(daj_ret)}) - CRJ Receipts ({fmt_r(crj_rec)})`\n"
        f"`= {open_bal} + {dj_sales} - {daj_ret} - {crj_rec} = {closing}`"
    )
    return build_short(
        rng,
        qid="g9_dj_41",
        subskill="41_debtors_control_opening_plus_dj_minus_crj_daj_calc",
        title="Net Movement & Closing Debtors Total",
        prompt=prompt,
        expected_answer=str(closing),
        worked_solution=worked,
        marks=3,
        hints={
            "tier_1": "Credit sales increase debt; allowances and receipts decrease debt.",
            "tier_2": f"Compute {open_bal} + {dj_sales} - {daj_ret} - {crj_rec}.",
            "tier_3": f"Closing Debtors Control = {closing}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Closing balance = {closing}", "marks": 3, "editable": True},
        ],
        misconception_tags=["adding_daj_or_crj_instead_of_subtracting"],
    )


def arch_42_evaluate_debtor_credit_limit_compliance_table(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    debtors = pick_debtors(rng, 4)
    limits = [2000, 3500, 5000, 1500]
    rng.shuffle(limits)
    balances = [
        limits[0] - rng.choice([200, 500]),
        limits[1] + rng.choice([300, 700]),
        limits[2] - rng.choice([400, 900]),
        limits[3] + rng.choice([250, 600]),
    ]
    headers = ["Debtor", "Credit Limit (R)", "Closing Balance (R)", "Status (Within Limit / Limit Exceeded)"]
    data_rows = []
    for (name, _), lim, bal in zip(debtors, limits, balances):
        status = "Within Limit" if bal <= lim else "Limit Exceeded"
        data_rows.append([name, str(lim), str(bal), status])
    rows, correct_map = make_grid_rows(data_rows, given_coords={(i, 0) for i in range(4)} | {(i, 1) for i in range(4)} | {(i, 2) for i in range(4)})
    cell_hints = {
        f"t0_r{i}_c3": f"Compare Balance ({r[2]}) against Credit Limit ({r[1]}) -> {r[3]}."
        for i, r in enumerate(data_rows)
    }
    prompt = (
        f"Audit the credit-limit compliance of four debtors at **{biz}** and classify each row as "
        "**`Within Limit`** or **`Limit Exceeded`**."
    )
    md_rows = "\n".join(f"| {r[0]} | {r[1]} | {r[2]} | **{r[3]}** |" for r in data_rows)
    worked = "**Credit Limit Compliance Audit** [4 marks]\n\n| Debtor | Credit Limit | Balance | Status |\n| --- | --- | --- | --- |\n" + md_rows
    return build_table(
        rng,
        qid="g9_dj_42",
        subskill="42_evaluate_debtor_credit_limit_compliance_table",
        title="Audit Debtor Credit Limit Compliance",
        prompt=prompt,
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer="; ".join(f"{r[0]}: {r[3]}" for r in data_rows),
        marks=4,
        hints={
            "tier_1": "If Closing Balance > Credit Limit, the debtor has exceeded their authorised ceiling.",
            "tier_2": "Check each pair carefully row by row.",
            "tier_3": "; ".join(f"{r[0]} -> {r[3]}" for r in data_rows),
        },
        marking_points=[
            {"id": f"mp_{i+1}", "desc": f"{r[0]} classified as {r[3]}", "marks": 1, "editable": True}
            for i, r in enumerate(data_rows)
        ],
        misconception_tags=["ignoring_credit_limit_breaches"],
        journal_type="audit_table",
    )


def arch_43_evaluate_debtor_payment_within_30_days_policy(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    debtor, _ = rng.choice(DEBTOR_POOL)
    limit = rng.choice([3000, 4500, 6000])
    bal = limit - rng.choice([400, 800])
    days_unpaid = rng.choice([45, 58, 72])

    prompt = (
        f"**{debtor}** has a credit limit of **{fmt_r(limit)}** with 30-day credit terms at **{biz}**.\n"
        f"Currently **{debtor}** owes **{fmt_r(bal)}** (still below the limit), but the balance has remained unpaid for **{days_unpaid} days**, "
        f"yet **{biz}** allows {debtor} to buy even more stock on credit.\n\n"
        "How should management evaluate **{debtor}**'s account?"
    )
    correct = f"Not managed well: although {debtor} stayed below the {fmt_r(limit)} limit, payment exceeded the 30-day credit term and granting additional credit risks reckless lending."
    distractors = [
        f"Managed well: as long as a debtor stays below {fmt_r(limit)}, payment timing beyond 30 days does not matter.",
        "Managed well: overdue accounts automatically convert into Capital contributions.",
        "Not managed well solely because the Credit Note column in the DJ is missing.",
    ]
    return build_mcq(
        rng,
        qid="g9_dj_43",
        subskill="43_evaluate_debtor_payment_within_30_days_policy",
        title="Credit Management: Overdue Within Limit",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"Good credit control requires **both** conditions: staying within the **credit limit** ({fmt_r(limit)}) AND "
            f"paying within the **credit term** (30 days). Letting an overdue {days_unpaid}-day account buy more is risky and poor management."
        ),
        hints={
            "tier_1": "Must a well-managed debtor satisfy ONLY the limit, or BOTH limit and credit terms?",
            "tier_2": f"{days_unpaid} days exceeds the 30-day term, and granting more credit to an overdue debtor is unsafe.",
            "tier_3": correct,
        },
        misconception_tags=["assuming_credit_limit_alone_determines_account_health"],
    )


def arch_44_irresponsible_lending_additional_credit_over_limit(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    debtor, _ = rng.choice(DEBTOR_POOL)
    limit = rng.choice([2500, 4000, 5000])
    owed = limit + rng.choice([300, 750])
    new_req = rng.choice([600, 900])

    prompt = (
        f"**{debtor}** already owes **{fmt_r(owed)}** against a **{fmt_r(limit)}** credit limit (30-day terms, currently overdue) "
        f"and asks **{biz}** to sell another **{fmt_r(new_req)}** of goods on account.\n\n"
        "What is the **best credit-control action** for **{biz}** to take?"
    )
    correct = f"Decline further credit immediately and insist {debtor} settles the overdue excess balance first to avoid reckless lending and bad debts."
    distractors = [
        f"Approve the {fmt_r(new_req)} credit sale in the DJ and raise the limit blindly to {fmt_r(owed + new_req)}.",
        "Record the new order in the Cash Payments Journal as a supplier expense.",
        "Wait 180 days without contacting the debtor before issuing a Credit Note.",
    ]
    return build_mcq(
        rng,
        qid="g9_dj_44",
        subskill="44_irresponsible_lending_additional_credit_over_limit",
        title="Preventing Irresponsible Credit Extension",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"Allowing **{debtor}** to purchase more while already over the **{fmt_r(limit)}** limit and overdue "
            "constitutes **irresponsible lending** and sharply increases bad-debt exposure."
        ),
        hints={
            "tier_1": "Should a store extend more credit to a debtor who has broken both limit and repayment terms?",
            "tier_2": "Suspend additional credit purchases until arrears are settled.",
            "tier_3": correct,
        },
        misconception_tags=["extending_credit_to_overlimit_debtors"],
    )


def arch_45_credit_control_age_analysis_management_ranking_table(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    debtors = pick_debtors(rng, 3)
    lim1, lim2, lim3 = 4000, 2500, 5000
    bal1 = rng.choice([3400, 3600])  # well managed: largest balance, within limit, paid <= 28d
    bal2 = rng.choice([2900, 3200])  # poorly managed: over limit & overdue
    bal3 = rng.choice([1800, 2200])  # well managed too, smaller balance, paid on time -> or make 1 best, 1 warning, 1 breach!
    # Wait: test Well Managed vs Overdue-Risk vs Breach cleanly
    headers = ["Debtor", "Limit (R)", "Balance (R)", "Days Taken (Term 30d)", "Rating (Well Managed / Poorly Managed)"]
    data_rows = [
        [debtors[0][0], str(lim1), str(bal1), "25", "Well Managed"],
        [debtors[1][0], str(lim2), str(bal2), "52", "Poorly Managed"],
        [debtors[2][0], str(lim3), str(bal3), "45", "Poorly Managed"],
    ]
    rng.shuffle(data_rows)
    rows, correct_map = make_grid_rows(data_rows, given_coords={(i, j) for i in range(3) for j in range(4)})
    cell_hints = {
        f"t0_r{i}_c4": (
            "Within limit AND <= 30 days -> Well Managed; over limit OR > 30 days -> Poorly Managed."
        )
        for i in range(3)
    }
    prompt = (
        f"Review the debtors summary for **{biz}** (standard term: **30 days**) and classify each account as "
        "**`Well Managed`** or **`Poorly Managed`**."
    )
    md_rows = "\n".join(f"| {r[0]} | {r[1]} | {r[2]} | {r[3]} | **{r[4]}** |" for r in data_rows)
    worked = (
        "**Debtors Age & Limit Evaluation** [3 marks]\n\n"
        "| Debtor | Limit | Balance | Days | Rating |\n| --- | --- | --- | --- | --- |\n" + md_rows
    )
    return build_table(
        rng,
        qid="g9_dj_45",
        subskill="45_credit_control_age_analysis_management_ranking_table",
        title="Evaluate Debtors Account Management Ratings",
        prompt=prompt,
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer="; ".join(f"{r[0]}: {r[4]}" for r in data_rows),
        marks=3,
        hints={
            "tier_1": "Even a large balance can be Well Managed if within the credit limit and paid within 30 days!",
            "tier_2": "A balance > Limit OR Days Taken > 30 makes the account Poorly Managed.",
            "tier_3": "; ".join(f"{r[0]} -> {r[4]}" for r in data_rows),
        },
        marking_points=[
            {"id": f"mp_{i+1}", "desc": f"{r[0]} = {r[4]}", "marks": 1, "editable": True}
            for i, r in enumerate(data_rows)
        ],
        misconception_tags=["judging_management_by_balance_size_instead_of_terms"],
        journal_type="audit_table",
    )


def arch_46_nca_credit_limit_enforcement_threshold_calc(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    debtor, _ = rng.choice(DEBTOR_POOL)
    limit = rng.choice([3000, 4500, 5000, 7500])
    current = rng.randint(12, 24) * 100
    headroom = limit - current

    prompt = (
        f"**{debtor}** has an approved credit limit of **{fmt_r(limit)}** at **{biz}** and currently owes **{fmt_r(current)}** (up to date).\n\n"
        f"What is the **maximum additional credit purchase** {debtor} may charge today without exceeding the credit limit? [2]\n"
        "*(Enter whole digits without spaces or the R symbol.)*"
    )
    worked = (
        "**Available Credit Headroom** [2 marks]\n\n"
        f"`Credit Limit ({fmt_r(limit)}) - Current Balance ({fmt_r(current)}) = {fmt_r(headroom)}` -> Answer: `{headroom}`"
    )
    return build_short(
        rng,
        qid="g9_dj_46",
        subskill="46_nca_credit_limit_enforcement_threshold_calc",
        title="Calculate Available Credit Limit Headroom",
        prompt=prompt,
        expected_answer=str(headroom),
        worked_solution=worked,
        marks=2,
        hints={
            "tier_1": "Subtract what the debtor already owes from their approved credit limit.",
            "tier_2": f"Headroom = {limit} - {current}.",
            "tier_3": f"Maximum additional purchase = {headroom}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Headroom = {headroom}", "marks": 2, "editable": True},
        ],
        misconception_tags=["adding_current_balance_to_credit_limit"],
    )


def arch_47_calculate_debtors_allowance_percentage_of_sales(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    sales_tot = rng.randint(10, 40) * 1000
    pct = rng.choice([4, 5, 8, 10, 12])
    allow_tot = sales_tot * pct // 100

    prompt = (
        f"For the quarter, **{biz}** recorded total **Credit Sales (DJ)** of **{fmt_r(sales_tot)}** "
        f"and total **Debtors Allowances (DAJ)** of **{fmt_r(allow_tot)}**.\n\n"
        "Calculate **Debtors Allowances as a percentage (%) of Credit Sales** [2].\n"
        "*(Enter the percentage number only, e.g. `8`.)*"
    )
    worked = (
        "**Debtors Allowance Rate** [2 marks]\n\n"
        f"$$\\frac{{\\text{{Debtors Allowance}}}}{{\\text{{Credit Sales}}}} \\times 100 = \\frac{{{allow_tot}}}{{{sales_tot}}} \\times 100 = {pct}\\%$$\n"
        f"Answer: `{pct}`"
    )
    return build_short(
        rng,
        qid="g9_dj_47",
        subskill="47_calculate_debtors_allowance_percentage_of_sales",
        title="Debtors Allowance Percentage of Credit Sales",
        prompt=prompt,
        expected_answer=str(pct),
        worked_solution=worked,
        marks=2,
        hints={
            "tier_1": "Express Debtors Allowance as a fraction of total Credit Sales, then multiply by 100.",
            "tier_2": f"Calculate ({allow_tot} / {sales_tot}) × 100.",
            "tier_3": f"Return rate = {pct}%.",
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Calculates {pct}% return rate", "marks": 2, "editable": True},
        ],
        misconception_tags=["dividing_credit_sales_by_allowance"],
    )


def arch_48_detect_duplicate_entry_or_missing_cos_in_dj_audit(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    debtor, _ = rng.choice(DEBTOR_POOL)
    sp = rng.randint(15, 45) * 100
    crr_amt = rng.randint(20, 40) * 100

    prompt = (
        f"While reviewing a junior clerk's **Debtors Journal (DJ)** for **{biz}**, you notice two issues:\n"
        f"- Invoice to **{debtor}** for **{fmt_r(sp)}** has an amount in **Sales** but `Cost of Sales` was left blank.\n"
        f"- A **Cash Register Roll (CRR)** cash sale of **{fmt_r(crr_amt)}** was also typed into the DJ.\n\n"
        "How must both errors be corrected?"
    )
    correct = f"Remove the {fmt_r(crr_amt)} cash sale (record in CRJ instead) and calculate Cost of Sales for {debtor}'s {fmt_r(sp)} credit sale."
    distractors = [
        f"Keep the {fmt_r(crr_amt)} CRR in the DJ and leave {debtor}'s Cost of Sales blank.",
        f"Move both transactions to the Cash Payments Journal as Trading Stock purchases.",
        f"Write {fmt_r(sp)} again in the Debtors Allowance column so Cost of Sales balances.",
    ]
    return build_mcq(
        rng,
        qid="g9_dj_48",
        subskill="48_detect_duplicate_entry_or_missing_cos_in_dj_audit",
        title="Audit & Correct Errors in Debtors Journal",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            "Every **credit sale** in the DJ requires **both** a `Sales` and `Cost of Sales` amount, "
            "while **cash sales (CRR)** belong exclusively in the **CRJ**."
        ),
        hints={
            "tier_1": "Check the two golden rules of the Debtors Journal: credit-only AND dual price/cost recording.",
            "tier_2": "CRR cash sales move to CRJ; every DJ row needs Cost of Sales calculated.",
            "tier_3": correct,
        },
        misconception_tags=["omitting_cost_of_sales_in_dj"],
    )


def arch_49_unethical_high_markup_pricing_and_consumer_protection(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    high_mu = rng.choice([250, 320, 400])

    prompt = (
        f"A rural general dealer near {sc['rural_area']} faces little competition and decides to apply an exploitative "
        f"**{high_mu}% mark-up** on essential food sold on 30-day credit to local households.\n\n"
        "Why is applying an excessively high mark-up in credit agreements considered poor / **unethical business practice**?"
    )
    correct = "It exploits vulnerable consumers, drives unaffordable household debt (contrary to fair-lending ethics and the NCA), and harms long-term community trust."
    distractors = [
        f"Because a {high_mu}% mark-up cannot be recorded in the Debtors Journal Sales column.",
        "Because higher profit margins force a store to replace Duplicate Invoices with Cheque Counterfoils.",
        "Because Trading Stock increases whenever Selling Price is raised above Cost Price.",
    ]
    return build_mcq(
        rng,
        qid="g9_dj_49",
        subskill="49_unethical_high_markup_pricing_and_consumer_protection",
        title="Business Ethics: Excessive Mark-Up & Credit",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"While high mark-ups like 80%–{high_mu}% occasionally appear in textbook calculation drills for arithmetic ease, "
            "charging exploitative mark-ups on credit essentials harms consumers and contradicts responsible credit ethics."
        ),
        hints={
            "tier_1": "Think about fairness to low-income households buying essentials on credit.",
            "tier_2": "Excessive mark-ups exploit consumers and increase bad-debt / over-indebtedness risk.",
            "tier_3": correct,
        },
        misconception_tags=["ignoring_ethical_pricing_responsibilities"],
    )


def arch_50_capstone_dj_daj_crj_and_credit_management_audit_table(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    debtor, fol = rng.choice(DEBTOR_POOL[:4])
    markup = rng.choice([25, 50])
    limit = 4000
    open_bal = rng.randint(12, 20) * 100
    cp_sale = rng.randint(16, 26) * 100
    sp_sale = cp_sale * (100 + markup) // 100
    cp_ret = rng.randint(2, 6) * 100
    sp_ret = cp_ret * (100 + markup) // 100
    crj_paid = rng.randint(10, 18) * 100
    closing = open_bal + sp_sale - sp_ret - crj_paid
    status = "Within Limit" if closing <= limit else "Limit Exceeded"

    headers = ["Audit Metric", "Value / Status"]
    data_rows = [
        ["Opening Balance (Day 1)", str(open_bal)],
        [f"DJ Credit Sale (SP, mark-up {markup}%)", str(sp_sale)],
        ["DJ Cost of Sales", str(cp_sale)],
        ["DAJ Return (SP)", str(sp_ret)],
        ["CRJ Receipt (Debtors Control)", str(crj_paid)],
        [f"Closing Balance owed by {debtor} ({fol})", str(closing)],
        [f"Credit Limit ({limit}) Check", status],
    ]
    rows, correct_map = make_grid_rows(data_rows, given_coords={(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (3, 0), (3, 1), (4, 0), (4, 1), (5, 0), (6, 0)})
    cell_hints = {
        "t0_r2_c1": f"DJ CoS = {sp_sale} × 100 / {100 + markup} = {cp_sale}.",
        "t0_r5_c1": f"Closing = {open_bal} + {sp_sale} - {sp_ret} - {crj_paid} = {closing}.",
        "t0_r6_c1": f"Compare Closing ({closing}) against Credit Limit ({limit}) -> {status}.",
    }
    prompt = (
        f"Complete the final **Debtors Audit Summary** for **{debtor} ({fol})** at **{biz}** "
        f"(mark-up **{markup}% on cost**, Credit Limit **R{limit}**). "
        "Fill in DJ Cost of Sales, Closing Balance, and Limit Compliance Status."
    )
    worked = (
        f"**Capstone Debtors Audit ({debtor})** [6 marks]\n\n"
        "| Audit Metric | Result |\n| --- | --- |\n"
        f"| Opening Balance | {fmt_r(open_bal)} |\n"
        f"| DJ Credit Sale | +{fmt_r(sp_sale)} (Cost of Sales: **{fmt_r(cp_sale)}**) |\n"
        f"| DAJ Allowance | -{fmt_r(sp_ret)} |\n"
        f"| CRJ Receipt | -{fmt_r(crj_paid)} |\n"
        f"| **Closing Balance** | **{fmt_r(closing)}** |\n"
        f"| **Limit ({fmt_r(limit)}) Check** | **{status}** |"
    )
    return build_table(
        rng,
        qid="g9_dj_50",
        subskill="50_capstone_dj_daj_crj_and_credit_management_audit_table",
        title="Capstone: DJ, DAJ, CRJ & Credit Limit Audit",
        prompt=prompt,
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=f"CoS={cp_sale}; Closing={closing}; Status={status}",
        marks=6,
        hints={
            "tier_1": "First recover Cost of Sales from Selling Price, then compute Opening + DJ - DAJ - CRJ.",
            "tier_2": f"CoS = {sp_sale} × 100/{100 + markup}; Closing = {open_bal} + {sp_sale} - {sp_ret} - {crj_paid}.",
            "tier_3": f"CoS = {cp_sale}; Closing = {closing}; Limit Check = {status}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": f"DJ Cost of Sales = {cp_sale}", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": f"Closing Balance = {closing}", "marks": 2, "editable": True},
            {"id": "mp_3", "desc": f"Credit Limit status = {status}", "marks": 2, "editable": True},
        ],
        misconception_tags=["miscomputing_closing_debtor_balance"],
        journal_type="audit_summary",
    )


ARCHETYPE_BUILDERS_26_50: Dict[str, Callable[[random.Random, str], Dict[str, Any]]] = {
    "26_why_document_is_called_credit_note": arch_26_why_document_is_called_credit_note,
    "27_daj_cost_of_sales_reversal_calculation": arch_27_daj_cost_of_sales_reversal_calculation,
    "28_daj_overcharge_allowance_no_stock_return_calc": arch_28_daj_overcharge_allowance_no_stock_return_calc,
    "29_daj_complete_4row_table": arch_29_daj_complete_4row_table,
    "30_daj_vs_dj_side_by_side_comparison_table": arch_30_daj_vs_dj_side_by_side_comparison_table,
    "31_crj_debtor_receipt_source_document_svg": arch_31_crj_debtor_receipt_source_document_svg,
    "32_crj_debtors_control_column_recording_rule": arch_32_crj_debtors_control_column_recording_rule,
    "33_crj_settlement_full_opening_debt_calc": arch_33_crj_settlement_full_opening_debt_calc,
    "34_crj_settlement_up_to_date_after_credit_sale_calc": arch_34_crj_settlement_up_to_date_after_credit_sale_calc,
    "35_crj_partial_settlement_and_remaining_debt_calc": arch_35_crj_partial_settlement_and_remaining_debt_calc,
    "36_crj_complete_with_debtors_control_table": arch_36_crj_complete_with_debtors_control_table,
    "37_crj_same_day_banking_cash_sales_and_debtor_receipt": arch_37_crj_same_day_banking_cash_sales_and_debtor_receipt,
    "38_crj_direct_eft_payment_by_debtor_rule": arch_38_crj_direct_eft_payment_by_debtor_rule,
    "39_crj_discount_allowed_vs_settlement_amount_check": arch_39_crj_discount_allowed_vs_settlement_amount_check,
    "40_combined_dj_and_crj_transaction_routing_table": arch_40_combined_dj_and_crj_transaction_routing_table,
    "41_debtors_control_opening_plus_dj_minus_crj_daj_calc": arch_41_debtors_control_opening_plus_dj_minus_crj_daj_calc,
    "42_evaluate_debtor_credit_limit_compliance_table": arch_42_evaluate_debtor_credit_limit_compliance_table,
    "43_evaluate_debtor_payment_within_30_days_policy": arch_43_evaluate_debtor_payment_within_30_days_policy,
    "44_irresponsible_lending_additional_credit_over_limit": arch_44_irresponsible_lending_additional_credit_over_limit,
    "45_credit_control_age_analysis_management_ranking_table": arch_45_credit_control_age_analysis_management_ranking_table,
    "46_nca_credit_limit_enforcement_threshold_calc": arch_46_nca_credit_limit_enforcement_threshold_calc,
    "47_calculate_debtors_allowance_percentage_of_sales": arch_47_calculate_debtors_allowance_percentage_of_sales,
    "48_detect_duplicate_entry_or_missing_cos_in_dj_audit": arch_48_detect_duplicate_entry_or_missing_cos_in_dj_audit,
    "49_unethical_high_markup_pricing_and_consumer_protection": arch_49_unethical_high_markup_pricing_and_consumer_protection,
    "50_capstone_dj_daj_crj_and_credit_management_audit_table": arch_50_capstone_dj_daj_crj_and_credit_management_audit_table,
}
