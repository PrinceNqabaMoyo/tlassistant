"""Grade 8 EMS - Cash Receipts Journal (Service Business): Archetypes 26 to 50.

Grounded strictly in curriculum_docs_auto/EMS_Gr8/Term 2/
03. Cash receipts journal for a services business 1.md and 2.md.
Zero-LLM, 100% deterministic, South African Rand (R) contexts.
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Tuple

from .crj_archetypes_01_25 import (
    CRJ_HEADERS,
    SUBTOPIC_ID,
    TOPIC_NAME,
    _bank_stmt_svg,
    _biz_ctx,
    _build_mcq,
    _build_short,
    _build_table,
    _cell,
    _crj_flow_svg,
    _crj_journal_question,
    _crr_slip_svg,
    _fmt_r,
    _md_table,
    _receipt_svg,
)


def _crj_bar_svg(biz_name: str, title: str, bars: List[Tuple[str, int, str]]) -> str:
    """Context SVG horizontal breakdown bar chart of CRJ totals."""
    max_val = max((v for _, v, _ in bars), default=1) or 1
    rows_svg = []
    y = 64
    for lbl, val, color in bars:
        width = max(14, int(round((val / max_val) * 320)))
        rows_svg.append(
            f'<text x="20" y="{y + 15}" font-size="11" font-weight="bold" fill="#1e293b">{lbl}</text>'
            f'<rect x="175" y="{y}" width="{width}" height="22" rx="4" fill="{color}"/>'
            f'<text x="{182 + width}" y="{y + 15}" font-size="11" font-weight="bold" fill="#0f172a">{_fmt_r(val)}</text>'
        )
        y += 38
    h = max(160, y + 22)
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 {h}" width="600" height="{h}">'
        f'<rect width="600" height="{h}" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>'
        f'<text x="300" y="30" font-size="13" font-weight="bold" text-anchor="middle" fill="#0f172a">{biz_name} — {title}</text>'
        + "".join(rows_svg)
        + '</svg>'
    )


def _equation_table(
    rng: random.Random,
    *,
    qid_prefix: str,
    subskill: str,
    title: str,
    prompt: str,
    tx_rows: List[Tuple[str, str, str, str, str]],
    notes: str,
    hints: Dict[str, str],
    misconception_tags: List[str],
) -> Dict[str, Any]:
    """Build a 2D Accounting Equation table (Transaction, A, OE, L, Reason)."""
    headers = ["Transaction", "Assets (A)", "Owner's Equity (OE)", "Liabilities (L)", "Reason"]
    rows, cmap, chints, str_rows, mps = [], {}, {}, [], []
    mp_i = 1
    for r_i, (tx, a_val, oe_val, l_val, reason) in enumerate(tx_rows):
        str_rows.append([tx, a_val, oe_val, l_val, reason])
        cells = [_cell(r_i, 0, tx, editable=False)]
        for c_i, val in enumerate([a_val, oe_val, l_val, reason], start=1):
            cell = _cell(r_i, c_i, val, editable=True)
            cells.append(cell)
            cmap[cell["cell_id"]] = val
            chints[cell["cell_id"]] = "Use +R... / -R... / 0 for amounts, and state the accounting reason."
            mps.append({"id": f"mp_{mp_i}", "desc": f"R{r_i + 1} {headers[c_i]}: {val}", "marks": 1, "editable": True})
            mp_i += 1
        rows.append(cells)
    md = _md_table(headers, str_rows)
    worked = f"**Accounting Equation Analysis ({len(mps)} marks)**\n\n{md}\n\n{notes}"
    return _build_table(
        rng,
        qid_prefix=qid_prefix,
        subskill=subskill,
        title=title,
        prompt=prompt,
        headers=headers,
        rows=rows,
        correct_map=cmap,
        cell_hints=chints,
        worked_solution=worked,
        sample_answer=md,
        marks=len(mps),
        hints=hints,
        marking_points=mps,
        misconception_tags=misconception_tags,
        qtype="table_completion",
        journal_type="equation",
    )


# ---------------------------------------------------------------------------
# Archetypes 26 - 50
# ---------------------------------------------------------------------------

def build_26_crj_two_transaction_starter_journal(rng: random.Random) -> Dict[str, Any]:
    ctx = _biz_ctx(rng)
    cap = rng.randint(5, 12) * 10000
    svc = rng.randint(25, 65) * 100
    bank_tot = cap + svc
    prompt = (
        f"Prepare {ctx['crj_no']} for {ctx['biz_name']} during {ctx['month_full']} from these two opening transactions, and complete the Totals row:\n"
        f"- Day 01: Owner {ctx['entrepreneur']} deposited {_fmt_r(cap)} directly into the business bank account as Capital (Receipt R01, fol. B1).\n"
        f"- Day 06: Cash services rendered per Cash Register Roll (CRR), {_fmt_r(svc)}."
    )
    row_specs = [
        (["R01", "01", ctx["entrepreneur"], "B1", "", _fmt_r(cap), "", _fmt_r(cap), "Capital"], [0, 1, 3], {}),
        (["CRR", "06", "Services rendered", "", _fmt_r(svc), _fmt_r(svc), _fmt_r(svc), "", ""], [0, 1], {}),
        (["", "", "TOTALS", "", "", _fmt_r(bank_tot), _fmt_r(svc), _fmt_r(cap), ""], [0, 1, 2, 3, 4, 8], {}),
    ]
    return _crj_journal_question(
        rng,
        qid_prefix="crj26",
        subskill="26_crj_two_transaction_starter_journal",
        title="Two-Transaction Starter CRJ with Balancing Totals",
        prompt=prompt,
        row_specs=row_specs,
        explanation_notes=f"- Cross-check: Bank total ({_fmt_r(bank_tot)}) = Current Income ({_fmt_r(svc)}) + Sundry ({_fmt_r(cap)}).",
        hints={
            "tier_1": "Direct deposit skips Analysis of Receipts; till cash uses Analysis of Receipts.",
            "tier_2": "Sum Bank, Current Income, and Sundry Amount on the TOTALS row (never total Analysis of Receipts).",
            "tier_3": f"Bank total = {_fmt_r(cap)} + {_fmt_r(svc)} = {_fmt_r(bank_tot)}.",
        },
        misconception_tags=["crj_totals_imbalance", "direct_deposit_in_analysis"],
    )


def build_27_crj_three_transaction_same_day_and_direct_deposit(rng: random.Random) -> Dict[str, Any]:
    ctx = _biz_ctx(rng)
    cap = rng.randint(4, 10) * 10000
    rent = rng.randint(18, 42) * 100
    svc = rng.randint(20, 48) * 100
    day_same = f"{rng.randint(12, 24):02d}"
    same_bank = rent + svc
    tot_bank = cap + same_bank
    tot_sun = cap + rent
    prompt = (
        f"Complete {ctx['crj_no']} for {ctx['biz_name']} ({ctx['month_full']}) and balance the Totals row:\n"
        f"- Day 02: {ctx['entrepreneur']} transferred {_fmt_r(cap)} directly into the bank as Capital (R01, fol. B1).\n"
        f"- Day {day_same}: Received {_fmt_r(rent)} cash rent from {ctx['tenant']} (R02, fol. N2) AND {_fmt_r(svc)} cash per CRR for {ctx['svc_desc']}. Both were banked together at day-end."
    )
    row_specs = [
        (["R01", "02", ctx["entrepreneur"], "B1", "", _fmt_r(cap), "", _fmt_r(cap), "Capital"], [0, 1, 3], {}),
        (["R02", day_same, ctx["tenant"], "N2", _fmt_r(rent), "", "", _fmt_r(rent), "Rent income"], [0, 1, 3], {}),
        (["CRR", day_same, "Services rendered", "", _fmt_r(svc), _fmt_r(same_bank), _fmt_r(svc), "", ""], [0, 1], {}),
        (["", "", "TOTALS", "", "", _fmt_r(tot_bank), _fmt_r(svc), _fmt_r(tot_sun), ""], [0, 1, 2, 3, 4, 8], {}),
    ]
    return _crj_journal_question(
        rng,
        qid_prefix="crj27",
        subskill="27_crj_three_transaction_same_day_and_direct_deposit",
        title="CRJ with Direct Deposit + Same-Day Combined Receipts",
        prompt=prompt,
        row_specs=row_specs,
        explanation_notes=(
            f"- Day 02 EFT bypasses Analysis of Receipts.\n"
            f"- Day {day_same} combines {_fmt_r(rent)} + {_fmt_r(svc)} = {_fmt_r(same_bank)} into one Bank entry.\n"
            f"- Check: {_fmt_r(svc)} + {_fmt_r(tot_sun)} = {_fmt_r(tot_bank)}."
        ),
        hints={
            "tier_1": "Apply both golden rules: direct deposits skip Analysis; same-day cash receipts bank as one sum on the second line.",
            "tier_2": f"On Day {day_same}, keep Bank blank on Row 2 and enter {_fmt_r(same_bank)} on Row 3.",
            "tier_3": f"Totals: Bank = {_fmt_r(tot_bank)}, Current Income = {_fmt_r(svc)}, Sundry = {_fmt_r(tot_sun)}.",
        },
        misconception_tags=["same_day_banked_separately", "direct_deposit_in_analysis"],
    )


def build_28_crj_four_transaction_full_services_month(rng: random.Random) -> Dict[str, Any]:
    ctx = _biz_ctx(rng)
    loan = rng.randint(2, 6) * 10000
    s1 = rng.randint(15, 36) * 100
    rent = rng.randint(22, 44) * 100
    s2 = rng.randint(18, 40) * 100
    bank_sum = loan + s1 + rent + s2
    ci_sum = s1 + s2
    sun_sum = loan + rent
    loan_acct = f"Loan: {ctx['bank_name']}"
    prompt = (
        f"Complete {ctx['crj_no']} for {ctx['biz_name']} in {ctx['month_full']}:\n"
        f"- Day 04: Bank Statement (BS) shows a {_fmt_r(loan)} business loan credited by {ctx['bank_name']} (fol. B4).\n"
        f"- Day 11: CRR services rendered, {_fmt_r(s1)}.\n"
        f"- Day 19: Cash rent received from {ctx['tenant']} (R05, fol. N2), {_fmt_r(rent)} (banked same day with no other receipts).\n"
        f"- Day 27: CRR services rendered, {_fmt_r(s2)}."
    )
    row_specs = [
        (["BS", "04", ctx["bank_name"], "B4", "", _fmt_r(loan), "", _fmt_r(loan), loan_acct], [0, 1, 3], {}),
        (["CRR", "11", "Services rendered", "", _fmt_r(s1), _fmt_r(s1), _fmt_r(s1), "", ""], [0, 1], {}),
        (["R05", "19", ctx["tenant"], "N2", _fmt_r(rent), _fmt_r(rent), "", _fmt_r(rent), "Rent income"], [0, 1, 3], {}),
        (["CRR", "27", "Services rendered", "", _fmt_r(s2), _fmt_r(s2), _fmt_r(s2), "", ""], [0, 1], {}),
        (["", "", "TOTALS", "", "", _fmt_r(bank_sum), _fmt_r(ci_sum), _fmt_r(sun_sum), ""], [0, 1, 2, 3, 4, 8], {}),
    ]
    return _crj_journal_question(
        rng,
        qid_prefix="crj28",
        subskill="28_crj_four_transaction_full_services_month",
        title="Four-Transaction Service Business CRJ",
        prompt=prompt,
        row_specs=row_specs,
        explanation_notes=(
            f"- Loan from {ctx['bank_name']} (BS) goes straight to Bank & Sundry (`{loan_acct}`).\n"
            f"- Day 11, Day 19, and Day 27 each occur on separate dates so each banks individually.\n"
            f"- Cross-check: {_fmt_r(ci_sum)} + {_fmt_r(sun_sum)} = {_fmt_r(bank_sum)}."
        ),
        hints={
            "tier_1": "Notice every transaction takes place on a different day — check which one is a direct Bank Statement credit.",
            "tier_2": "BS skips Analysis of Receipts; cash days (11, 19, 27) pass through Analysis of Receipts individually.",
            "tier_3": f"Bank Total = {_fmt_r(bank_sum)}; Current Income = {_fmt_r(ci_sum)}; Sundry = {_fmt_r(sun_sum)}.",
        },
        misconception_tags=["loan_treated_as_current_income", "crj_totals_imbalance"],
    )


def build_29_crj_five_transaction_comprehensive_journal(rng: random.Random) -> Dict[str, Any]:
    ctx = _biz_ctx(rng)
    cap = rng.randint(5, 11) * 10000
    s1 = rng.randint(12, 30) * 100
    rent = rng.randint(20, 45) * 100
    s2 = rng.randint(15, 35) * 100
    interest = rng.randint(14, 48) * 10
    d_same = "20"
    same_bank = rent + s2
    b_tot = cap + s1 + same_bank + interest
    ci_tot = s1 + s2
    sun_tot = cap + rent + interest
    prompt = (
        f"Prepare the full 5-transaction {ctx['crj_no']} for {ctx['biz_name']} in {ctx['month_full']} and balance all columns:\n"
        f"- Day 01: {ctx['entrepreneur']} paid {_fmt_r(cap)} directly into the bank as Capital (R01, fol. B1).\n"
        f"- Day 09: CRR {ctx['svc_desc']}, {_fmt_r(s1)}.\n"
        f"- Day {d_same}: Received {_fmt_r(rent)} cash rent from {ctx['tenant']} (R02, fol. N2) AND {_fmt_r(s2)} per CRR for services, banked together.\n"
        f"- Day 30: Bank Statement (BS) from {ctx['bank_name']} shows {_fmt_r(interest)} interest credited (fol. N3)."
    )
    row_specs = [
        (["R01", "01", ctx["entrepreneur"], "B1", "", _fmt_r(cap), "", _fmt_r(cap), "Capital"], [0, 1, 3], {}),
        (["CRR", "09", "Services rendered", "", _fmt_r(s1), _fmt_r(s1), _fmt_r(s1), "", ""], [0, 1], {}),
        (["R02", d_same, ctx["tenant"], "N2", _fmt_r(rent), "", "", _fmt_r(rent), "Rent income"], [0, 1, 3], {}),
        (["CRR", d_same, "Services rendered", "", _fmt_r(s2), _fmt_r(same_bank), _fmt_r(s2), "", ""], [0, 1], {}),
        (["BS", "30", ctx["bank_name"], "N3", "", _fmt_r(interest), "", _fmt_r(interest), "Interest income"], [0, 1, 3], {}),
        (["", "", "TOTALS", "", "", _fmt_r(b_tot), _fmt_r(ci_tot), _fmt_r(sun_tot), ""], [0, 1, 2, 3, 4, 8], {}),
    ]
    return _crj_journal_question(
        rng,
        qid_prefix="crj29",
        subskill="29_crj_five_transaction_comprehensive_journal",
        title="Comprehensive Five-Transaction CRJ Preparation",
        prompt=prompt,
        row_specs=row_specs,
        explanation_notes=(
            f"- Direct deposits (Day 01 Capital & Day 30 Interest) leave `Analysis of Receipts` blank.\n"
            f"- Day {d_same} groups {_fmt_r(rent)} + {_fmt_r(s2)} = {_fmt_r(same_bank)} into one Bank entry.\n"
            f"- Cross-check: Bank {_fmt_r(b_tot)} = Current Income {_fmt_r(ci_tot)} + Sundry {_fmt_r(sun_tot)}."
        ),
        hints={
            "tier_1": "Handle direct deposits (Days 01 & 30), single till day (09), and combined same-day receipts (Day 20).",
            "tier_2": f"Day 20 Bank = {_fmt_r(rent)} + {_fmt_r(s2)} = {_fmt_r(same_bank)}.",
            "tier_3": f"Totals row: Bank = {_fmt_r(b_tot)}, Current Income = {_fmt_r(ci_tot)}, Sundry = {_fmt_r(sun_tot)}.",
        },
        misconception_tags=["comprehensive_crj_errors", "crj_totals_imbalance"],
    )


def build_30_crj_receipt_slip_to_journal_transcription(rng: random.Random) -> Dict[str, Any]:
    ctx = _biz_ctx(rng)
    doc = f"R{rng.randint(41, 88)}"
    day = f"{rng.randint(7, 19):02d}"
    amt = rng.randint(18, 52) * 100
    amt_str = _fmt_r(amt)
    svg = _receipt_svg(ctx["biz_name"], doc, f"{day} {ctx['month_full']}", ctx["tenant"], amt, "Cash workshop rent", ctx["entrepreneur"])
    prompt = (
        f"Inspect the duplicate receipt slip shown below for {ctx['biz_name']}. "
        f"Read the receipt number, day, payer, and amount directly from the slip to complete the entire CRJ row "
        f"(assuming cash was received at the counter and banked alone on that day; folio N2)."
    )
    row_specs = [
        ([doc, day, ctx["tenant"], "N2", amt_str, amt_str, "", amt_str, "Rent income"], [3], {
            0: "Copy the receipt number shown in the top-right corner of the slip.",
            1: "Enter the two-digit day number from the Date line.",
        }),
    ]
    return _crj_journal_question(
        rng,
        qid_prefix="crj30",
        subskill="30_crj_receipt_slip_to_journal_transcription",
        title="Transcribing a Duplicate Receipt Slip into the CRJ",
        prompt=prompt,
        row_specs=row_specs,
        explanation_notes=f"From Receipt {doc} ({day} {ctx['month_short']}), record `{ctx['tenant']}` in Details, {amt_str} in Analysis, Bank, and Sundry Amount (`Rent income`).",
        hints={
            "tier_1": "Read the receipt number (top-right), date, payer name, reason, and Rand amount from the slip.",
            "tier_2": "Counter cash goes into Analysis of Receipts first; rent belongs in Sundry Accounts.",
            "tier_3": f"Doc = {doc}, Day = {day}, Details = {ctx['tenant']}, Amounts = {amt_str}, Sundry Details = Rent income.",
        },
        misconception_tags=["source_doc_transcription_error"],
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    )


def build_31_crj_bank_statement_extract_to_crj_entries(rng: random.Random) -> Dict[str, Any]:
    ctx = _biz_ctx(rng)
    d1, d2 = "15", "29"
    rent = rng.randint(30, 60) * 100
    interest = rng.randint(15, 45) * 10
    tot = rent + interest
    svg = _bank_stmt_svg(
        ctx["bank_name"],
        ctx["biz_name"],
        ctx["month_full"],
        [
            (f"{d1} {ctx['month_short']}", f"EFT Rent — {ctx['tenant']}", rent),
            (f"{d2} {ctx['month_short']}", "Interest on credit balance", interest),
        ],
    )
    prompt = (
        f"Inspect the Bank Statement credit extract below for {ctx['biz_name']} ({ctx['month_full']}). "
        f"Transcribe both direct bank credits into {ctx['crj_no']} (folios N2 and N3) and enter the Bank and Sundry totals."
    )
    row_specs = [
        (["BS", d1, ctx["tenant"], "N2", "", _fmt_r(rent), "", _fmt_r(rent), "Rent income"], [3], {}),
        (["BS", d2, ctx["bank_name"], "N3", "", _fmt_r(interest), "", _fmt_r(interest), "Interest income"], [3], {}),
        (["", "", "TOTALS", "", "", _fmt_r(tot), "", _fmt_r(tot), ""], [0, 1, 2, 3, 4, 6, 8], {}),
    ]
    return _crj_journal_question(
        rng,
        qid_prefix="crj31",
        subskill="31_crj_bank_statement_extract_to_crj_entries",
        title="Transcribing Bank Statement Credits into the CRJ",
        prompt=prompt,
        row_specs=row_specs,
        explanation_notes=(
            f"- Both entries appear on the Bank Statement (`BS`) directly, so `Analysis of Receipts` is blank.\n"
            f"- Bank Total = {_fmt_r(rent)} + {_fmt_r(interest)} = {_fmt_r(tot)} = Sundry Total."
        ),
        hints={
            "tier_1": "Bank statement credits use Doc No 'BS' and skip Analysis of Receipts.",
            "tier_2": "Row 1 credits Rent income; Row 2 credits Interest income.",
            "tier_3": f"Total Bank = Total Sundry = {_fmt_r(tot)}.",
        },
        misconception_tags=["bs_entered_in_analysis"],
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    )


def build_32_crj_cross_checking_horizontal_balancing_rule(rng: random.Random) -> Dict[str, Any]:
    ctx = _biz_ctx(rng)
    ci = rng.randint(14, 48) * 1000 + rng.choice([200, 500, 800])
    sun = rng.randint(25, 85) * 1000
    bank = ci + sun
    solve_for = rng.choice(["Bank", "Current Income", "Sundry Accounts"])
    if solve_for == "Bank":
        bars = [("Current Income", ci, "#0284c7"), ("Sundry Accounts", sun, "#7c3aed")]
        prompt = (
            f"Study the {ctx['crj_no']} column summary chart for {ctx['biz_name']}: "
            f"Total Current Income = {_fmt_r(ci)} and Total Sundry Accounts = {_fmt_r(sun)}. "
            f"Apply the CRJ cross-checking formula to find the Total Bank column figure."
        )
        ans = _fmt_r(bank)
        worked = f"Total Bank = Current Income + Sundry Accounts = {_fmt_r(ci)} + {_fmt_r(sun)} = **{ans}**."
    elif solve_for == "Current Income":
        bars = [("Total Bank", bank, "#059669"), ("Sundry Accounts", sun, "#7c3aed")]
        prompt = (
            f"Study the {ctx['crj_no']} totals chart for {ctx['biz_name']}: "
            f"Total Bank = {_fmt_r(bank)} and Total Sundry Accounts = {_fmt_r(sun)}. "
            f"Calculate the missing Total Current Income figure."
        )
        ans = _fmt_r(ci)
        worked = f"Total Current Income = Total Bank - Sundry Accounts = {_fmt_r(bank)} - {_fmt_r(sun)} = **{ans}**."
    else:
        bars = [("Total Bank", bank, "#059669"), ("Current Income", ci, "#0284c7")]
        prompt = (
            f"Study the {ctx['crj_no']} totals chart for {ctx['biz_name']}: "
            f"Total Bank = {_fmt_r(bank)} and Total Current Income = {_fmt_r(ci)}. "
            f"Calculate the missing Total Sundry Accounts figure."
        )
        ans = _fmt_r(sun)
        worked = f"Total Sundry Accounts = Total Bank - Current Income = {_fmt_r(bank)} - {_fmt_r(ci)} = **{ans}**."
    svg = _crj_bar_svg(ctx["biz_name"], f"{ctx['crj_no']} Column Totals", bars)
    return _build_short(
        rng,
        qid_prefix="crj32",
        subskill="32_crj_cross_checking_horizontal_balancing_rule",
        title="Cross-Checking CRJ Totals (Horizontal Balancing)",
        prompt=prompt,
        expected_answer=ans,
        worked_solution=worked,
        hints={
            "tier_1": "In a balanced CRJ, the Bank total must equal the sum of all analysis and sundry columns.",
            "tier_2": "Use: Total Bank = Total Current Income + Total Sundry Accounts.",
            "tier_3": worked,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Applies Total Bank = Total Current Income + Total Sundry Accounts", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": f"Accurate missing total: {ans}", "marks": 2, "editable": True},
        ],
        misconception_tags=["crj_cross_check_formula_error"],
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    )


def build_33_crj_cross_check_verification_audit(rng: random.Random) -> Dict[str, Any]:
    ctx = _biz_ctx(rng)
    ci = rng.randint(15, 38) * 1000
    sun = rng.randint(30, 75) * 1000
    diff = rng.choice([0, 450, 900, 1200])
    bank = ci + sun + diff
    if diff == 0:
        correct = f"Yes, the CRJ cross-checks accurately because {_fmt_r(ci)} + {_fmt_r(sun)} = {_fmt_r(bank)}"
        dists = [
            f"No, Bank is overstated by {_fmt_r(1000)}",
            f"No, Current Income must always exceed Sundry Accounts",
            "No, Analysis of Receipts was omitted from the addition",
        ]
    else:
        correct = f"No, the journal does NOT balance because Current Income + Sundry ({_fmt_r(ci + sun)}) is {_fmt_r(diff)} less than Bank ({_fmt_r(bank)})"
        dists = [
            f"Yes, the CRJ balances accurately because {_fmt_r(bank)} > {_fmt_r(ci)}",
            f"No, Sundry Accounts is overstated by {_fmt_r(diff * 2)}",
            "Yes, differences under R2 000 are accepted in South African accounting",
        ]
    return _build_mcq(
        rng,
        qid_prefix="crj33",
        subskill="33_crj_cross_check_verification_audit",
        title="Auditing a CRJ Totals Row for Cross-Check Errors",
        prompt=(
            f"At month-end, {ctx['biz_name']}'s {ctx['crj_no']} reports Total Bank = {_fmt_r(bank)}, "
            f"Total Current Income = {_fmt_r(ci)}, and Total Sundry Accounts = {_fmt_r(sun)}. "
            f"Does this Cash Receipts Journal pass the horizontal cross-check?"
        ),
        correct_text=correct,
        distractors=dists,
        explanation=f"Current Income ({_fmt_r(ci)}) + Sundry Accounts ({_fmt_r(sun)}) = {_fmt_r(ci + sun)}, compared with Bank ({_fmt_r(bank)}).",
        hints={
            "tier_1": "Add Total Current Income and Total Sundry Accounts together.",
            "tier_2": "Compare that sum against Total Bank.",
            "tier_3": f"{_fmt_r(ci)} + {_fmt_r(sun)} = {_fmt_r(ci + sun)} vs Bank {_fmt_r(bank)}.",
        },
        misconception_tags=["ignored_cross_check_discrepancy"],
    )


def build_34_crj_closing_off_and_double_ruling_rules(rng: random.Random) -> Dict[str, Any]:
    ctx = _biz_ctx(rng)
    bank_tot = rng.randint(45, 98) * 1000
    variant = rng.choice(["ruling_and_columns", "analysis_exclusion"])
    if variant == "ruling_and_columns":
        prompt = f"When closing off {ctx['crj_no']} for {ctx['biz_name']} (Bank Total {_fmt_r(bank_tot)}) at the end of {ctx['month_full']}, which columns are summed and how are totals ruled?"
        correct = "Add Bank, Current Income, and Sundry Amount; draw a single line above totals and a double line below Bank, Current Income, and Sundry Amount"
        dists = [
            "Add Analysis of Receipts as well and post its total to the General Ledger",
            "Leave all totals un-ruled so entries from next month continue directly underneath",
            "Only rule off Sundry Details and leave Bank without a total",
        ]
    else:
        prompt = f"Why is the 'Analysis of Receipts' column in {ctx['biz_name']}'s {ctx['crj_no']} (Bank Total {_fmt_r(bank_tot)}) NOT totalled and posted at month-end?"
        correct = "Because every receipt in Analysis of Receipts has already been banked into the Bank column — posting it would double-count cash"
        dists = [
            "Because Analysis of Receipts records non-cash credit sales only",
            "Because Analysis of Receipts belongs to the Cash Payments Journal",
            "Because only the first day of the month is summed in Analysis of Receipts",
        ]
    return _build_mcq(
        rng,
        qid_prefix="crj34",
        subskill="34_crj_closing_off_and_double_ruling_rules",
        title="Closing Off the Cash Receipts Journal at Month-End",
        prompt=prompt,
        correct_text=correct,
        distractors=dists,
        explanation="At month-end, Bank, Current Income, and Sundry Amount are summed (single line above, double line below) and cross-checked. Analysis of Receipts is never totalled.",
        hints={
            "tier_1": "Think about which three money columns actually post to General Ledger accounts.",
            "tier_2": "Analysis of Receipts is merely a daily till staging column whose amounts flow into Bank.",
            "tier_3": "Only Bank, Current Income, and Sundry Amount receive single-top / double-bottom final totals.",
        },
        misconception_tags=["totalling_analysis_of_receipts", "missing_double_ruling"],
    )


def build_35_crj_missing_current_income_deduction(rng: random.Random) -> Dict[str, Any]:
    ctx = _biz_ctx(rng)
    cap = rng.randint(4, 9) * 10000
    rent = rng.randint(25, 50) * 100
    svc1 = rng.randint(18, 38) * 100
    svc2 = rng.randint(22, 46) * 100
    tot_ci = svc1 + svc2
    tot_sun = cap + rent
    tot_bank = tot_ci + tot_sun
    prompt = (
        f"Look at this partial {ctx['crj_no']} summary for {ctx['biz_name']} ({ctx['month_full']}):\n"
        f"- Total Bank column = {_fmt_r(tot_bank)}\n"
        f"- Sundry entries: Capital {_fmt_r(cap)} and Rent income {_fmt_r(rent)}\n"
        f"- One CRR service entry on Day 08 was {_fmt_r(svc1)}, and Day 22's CRR service fee amount [X] smudged.\n"
        f"Deduce the exact missing Current Income amount [X] on Day 22."
    )
    ans = _fmt_r(svc2)
    worked = (
        f"1. Total Sundry Accounts = {_fmt_r(cap)} + {_fmt_r(rent)} = {_fmt_r(tot_sun)}\n"
        f"2. Total Current Income = Total Bank - Total Sundry = {_fmt_r(tot_bank)} - {_fmt_r(tot_sun)} = {_fmt_r(tot_ci)}\n"
        f"3. Missing Day 22 CRR [X] = {_fmt_r(tot_ci)} - {_fmt_r(svc1)} = **{ans}**"
    )
    return _build_short(
        rng,
        qid_prefix="crj35",
        subskill="35_crj_missing_current_income_deduction",
        title="Deducing a Missing Current Income Entry",
        prompt=prompt,
        expected_answer=ans,
        worked_solution=worked,
        hints={
            "tier_1": "First find Total Sundry Accounts, then use Total Bank to find Total Current Income.",
            "tier_2": f"Total Current Income = {_fmt_r(tot_bank)} - ({_fmt_r(cap)} + {_fmt_r(rent)}).",
            "tier_3": f"Subtract Day 08 CRR ({_fmt_r(svc1)}) from Total Current Income ({_fmt_r(tot_ci)}).",
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Finds Total Current Income = {_fmt_r(tot_ci)}", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": f"Subtracts {_fmt_r(svc1)} to find missing CRR = {ans}", "marks": 1, "editable": True},
        ],
        misconception_tags=["incomplete_reverse_balancing"],
    )


def build_36_crj_missing_sundry_amount_and_account_deduction(rng: random.Random) -> Dict[str, Any]:
    ctx = _biz_ctx(rng)
    ci = rng.randint(12, 34) * 1000
    cap = rng.randint(3, 8) * 10000
    rent = rng.randint(32, 78) * 100
    tot_bank = ci + cap + rent
    prompt = (
        f"In {ctx['biz_name']}'s {ctx['crj_no']} ({ctx['month_full']}), Total Bank = {_fmt_r(tot_bank)} and Total Current Income = {_fmt_r(ci)}. "
        f"Only two Sundry entries occurred: owner Capital of {_fmt_r(cap)}, and a receipt from tenant {ctx['tenant']} for missing amount [Y]. "
        f"Calculate the missing Rent income amount [Y]."
    )
    ans = _fmt_r(rent)
    worked = (
        f"1. Total Sundry Accounts = {_fmt_r(tot_bank)} - {_fmt_r(ci)} = {_fmt_r(cap + rent)}\n"
        f"2. Missing Rent income [Y] = {_fmt_r(cap + rent)} - {_fmt_r(cap)} = **{ans}**"
    )
    return _build_short(
        rng,
        qid_prefix="crj36",
        subskill="36_crj_missing_sundry_amount_and_account_deduction",
        title="Deducing a Missing Sundry Entry from Totals",
        prompt=prompt,
        expected_answer=ans,
        worked_solution=worked,
        hints={
            "tier_1": "Find Total Sundry Accounts first by subtracting Current Income from Bank.",
            "tier_2": f"Total Sundry = {_fmt_r(tot_bank)} - {_fmt_r(ci)} = {_fmt_r(cap + rent)}.",
            "tier_3": f"Subtract Capital ({_fmt_r(cap)}) to isolate {ctx['tenant']}'s rent.",
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Total Sundry = {_fmt_r(cap + rent)}", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": f"Missing Rent income = {ans}", "marks": 2, "editable": True},
        ],
        misconception_tags=["sundry_reverse_deduction_error"],
    )


def build_37_crj_missing_same_day_deposit_reconstruction(rng: random.Random) -> Dict[str, Any]:
    ctx = _biz_ctx(rng)
    day = f"{rng.randint(8, 25):02d}"
    r1 = rng.randint(15, 40) * 100
    r2 = rng.randint(12, 35) * 100
    r3 = rng.randint(8, 25) * 100
    deposit = r1 + r2 + r3
    prompt = (
        f"On Day {day} in {ctx['crj_no']} ({ctx['biz_name']}), three physical cash receipts appear in 'Analysis of Receipts': "
        f"R08 ({_fmt_r(r1)}), R09 ({_fmt_r(r2)}), and CRR ({_fmt_r(r3)}). "
        f"Reconstruct the missing Bank column deposit slip figure for Day {day}."
    )
    ans = _fmt_r(deposit)
    return _build_short(
        rng,
        qid_prefix="crj37",
        subskill="37_crj_missing_same_day_deposit_reconstruction",
        title="Reconstructing a Missing Daily Bank Deposit",
        prompt=prompt,
        expected_answer=ans,
        worked_solution=f"All same-day till receipts deposit together: {_fmt_r(r1)} + {_fmt_r(r2)} + {_fmt_r(r3)} = **{ans}**.",
        hints={
            "tier_1": "Same-day cash receipts in Analysis of Receipts are summed once into Bank.",
            "tier_2": "Add all three amounts from Day " + day + ".",
            "tier_3": f"{_fmt_r(r1)} + {_fmt_r(r2)} + {_fmt_r(r3)} = {ans}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": "Sums all three same-day receipts", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": f"Deposit total: {ans}", "marks": 1, "editable": True},
        ],
        misconception_tags=["incomplete_daily_deposit_sum"],
    )


def build_38_crj_missing_analysis_entry_from_daily_bank(rng: random.Random) -> Dict[str, Any]:
    ctx = _biz_ctx(rng)
    day = f"{rng.randint(10, 26):02d}"
    known = rng.randint(18, 45) * 100
    missing = rng.randint(14, 38) * 100
    bank_day = known + missing
    prompt = (
        f"On Day {day} in {ctx['biz_name']}'s {ctx['crj_no']}, two cash receipts were banked together for a total Bank entry of {_fmt_r(bank_day)}. "
        f"Receipt R14 recorded {_fmt_r(known)} in Analysis of Receipts. What was the missing second receipt (CRR) in Analysis of Receipts?"
    )
    ans = _fmt_r(missing)
    return _build_short(
        rng,
        qid_prefix="crj38",
        subskill="38_crj_missing_analysis_entry_from_daily_bank",
        title="Finding a Missing Analysis Entry from Daily Bank Total",
        prompt=prompt,
        expected_answer=ans,
        worked_solution=f"Missing CRR = Daily Bank Deposit ({_fmt_r(bank_day)}) - Known Receipt ({_fmt_r(known)}) = **{ans}**.",
        hints={
            "tier_1": "The Bank entry on Day " + day + " equals the sum of all till receipts that day.",
            "tier_2": "Subtract the known Analysis entry from the Bank deposit.",
            "tier_3": f"{_fmt_r(bank_day)} - {_fmt_r(known)} = {ans}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": "Subtracts known receipt from daily deposit", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": f"Missing entry = {ans}", "marks": 1, "editable": True},
        ],
        misconception_tags=["analysis_bank_mismatch"],
    )


def build_39_crj_spot_error_direct_deposit_in_analysis(rng: random.Random) -> Dict[str, Any]:
    ctx = _biz_ctx(rng)
    amt = rng.randint(35, 90) * 100
    return _build_mcq(
        rng,
        qid_prefix="crj39",
        subskill="39_crj_spot_error_direct_deposit_in_analysis",
        title="Error Audit: Direct EFT Entered in Analysis of Receipts",
        prompt=(
            f"A trainee bookkeeper at {ctx['biz_name']} recorded a {_fmt_r(amt)} direct EFT payment from {ctx['tenant']} "
            f"inside the 'Analysis of Receipts' column before moving it to Bank. What problem does this mistake create?"
        ),
        correct_text=f"It falsely implies {_fmt_r(amt)} cash passed through the physical cash register till, throwing off daily cash-drawer reconciliation",
        distractors=[
            "It reverses the transaction so it becomes an expense in the Cash Payments Journal",
            "It turns Rent income into Current Income automatically",
            "It prevents the Bank total from matching Total Current Income + Sundry Accounts",
        ],
        explanation=f"EFT deposits go straight to {ctx['bank_name']} and never touch the till. Recording them in Analysis of Receipts creates a phantom {_fmt_r(amt)} shortage when counting cash in the till.",
        hints={
            "tier_1": "Think about what a cashier expects to find in the cash drawer when closing the till.",
            "tier_2": "Analysis of Receipts tracks physical till cash awaiting banking.",
            "tier_3": "Entering an EFT there makes it look like extra cash sits in the till.",
        },
        misconception_tags=["direct_deposit_in_analysis"],
    )


def build_40_crj_spot_error_same_day_banked_separately(rng: random.Random) -> Dict[str, Any]:
    ctx = _biz_ctx(rng)
    a1 = rng.randint(15, 35) * 100
    a2 = rng.randint(16, 40) * 100
    day = f"{rng.randint(5, 22):02d}"
    return _build_mcq(
        rng,
        qid_prefix="crj40",
        subskill="40_crj_spot_error_same_day_banked_separately",
        title="Error Audit: Same-Day Cash Receipts Banked Separately",
        prompt=(
            f"On Day {day}, {ctx['biz_name']} took {_fmt_r(a1)} (R04) and {_fmt_r(a2)} (CRR) in cash and made one deposit slip at {ctx['bank_name']}. "
            f"However, the CRJ shows {_fmt_r(a1)} in Bank on Row 1 and {_fmt_r(a2)} in Bank on Row 2. Identify the bookkeeper's error and correction."
        ),
        correct_text=f"Same-day cash receipts should be totalled once on Row 2 as {_fmt_r(a1 + a2)} in Bank, leaving Row 1's Bank cell blank to match the single bank deposit slip",
        distractors=[
            f"Row 2 should be deleted so only {_fmt_r(a1)} appears in Current Income",
            f"Both figures should be subtracted instead of added ({_fmt_r(abs(a2 - a1))})",
            "The entries are correct because every CRJ line must fill the Bank cell",
        ],
        explanation=f"The Bank Statement will reflect ONE single deposit of {_fmt_r(a1 + a2)}, so the CRJ Bank column must mirror that single {_fmt_r(a1 + a2)} deposit on the final line of Day {day}.",
        hints={
            "tier_1": "Compare the CRJ Bank column against what the Bank Statement actually prints for one deposit slip.",
            "tier_2": "One trip to the bank = one figure in the Bank column on that date.",
            "tier_3": f"Keep Row 1 Bank empty and enter {_fmt_r(a1 + a2)} on Row 2.",
        },
        misconception_tags=["same_day_banked_separately"],
    )


def build_41_crj_spot_error_sundry_posted_to_current_income(rng: random.Random) -> Dict[str, Any]:
    ctx = _biz_ctx(rng)
    amt = rng.randint(25, 85) * 100
    acct = rng.choice(["Rent income", "Capital", "Donations received"])
    return _build_short(
        rng,
        qid_prefix="crj41",
        subskill="41_crj_spot_error_sundry_posted_to_current_income",
        title="Impact of Misclassifying Sundry Income into Current Income",
        prompt=(
            f"At {ctx['biz_name']}, {_fmt_r(amt)} received for {acct} was wrongly entered into 'Current Income' instead of 'Sundry Accounts'. "
            f"Wait — Total Bank is still correct. By how many Rand is 'Current Income' overstated?"
        ),
        expected_answer=_fmt_r(amt),
        worked_solution=(
            f"- `Current Income` is overstated by **{_fmt_r(amt)}** (and `Sundry Accounts` / `{acct}` is understated by **{_fmt_r(amt)}**).\n"
            f"- Note: Total Bank remains unchanged because {_fmt_r(amt)} was still banked."
        ),
        hints={
            "tier_1": "Look at which column gained an amount that did not belong to core services.",
            "tier_2": f"{acct} is not Current Income, so the entire {_fmt_r(amt)} inflated Current Income.",
            "tier_3": f"Current Income is overstated by {_fmt_r(amt)}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Identifies {_fmt_r(amt)} overstatement in Current Income", "marks": 2, "editable": True},
        ],
        misconception_tags=["sundry_misclassified_as_current_income"],
    )


def build_42_crj_spot_error_analysis_added_to_totals(rng: random.Random) -> Dict[str, Any]:
    ctx = _biz_ctx(rng)
    bank_tot = rng.randint(35, 85) * 1000
    an_tot = rng.randint(12, 28) * 1000
    return _build_mcq(
        rng,
        qid_prefix="crj42",
        subskill="42_crj_spot_error_analysis_added_to_totals",
        title="Error Audit: Double-Counting the Analysis Column",
        prompt=(
            f"While closing off {ctx['crj_no']} for {ctx['biz_name']} (Bank Total {_fmt_r(bank_tot)}), "
            f"an intern summed 'Analysis of Receipts' ({_fmt_r(an_tot)}) and added it to Current Income + Sundry during cross-checking. Why did cross-checking fail?"
        ),
        correct_text=f"Analysis of Receipts ({_fmt_r(an_tot)}) is already included inside Current Income and Sundry; adding it double-counts till cash",
        distractors=[
            "Because Current Income is always subtracted from Bank during cross-checking",
            "Because Analysis of Receipts belongs in the Cash Payments Journal only",
            "Because Sundry Details must also be summed numerically",
        ],
        explanation=f"Cross-checking ONLY uses `Total Bank ({_fmt_r(bank_tot)}) = Total Current Income + Total Sundry Accounts`. Analysis of Receipts ({_fmt_r(an_tot)}) is never added at month-end.",
        hints={
            "tier_1": "Every till amount in Analysis of Receipts also entered Current Income or Sundry on the same line.",
            "tier_2": "Including Analysis of Receipts counts those till entries twice.",
            "tier_3": "Never total Analysis of Receipts at month-end.",
        },
        misconception_tags=["totalling_analysis_of_receipts"],
    )


def build_43_crj_accounting_equation_services_rendered(rng: random.Random) -> Dict[str, Any]:
    ctx = _biz_ctx(rng)
    amt = _fmt_r(rng.randint(14, 48) * 100)
    return _equation_table(
        rng,
        qid_prefix="crj43",
        subskill="43_crj_accounting_equation_services_rendered",
        title="Accounting Equation: Cash Services Rendered",
        prompt=f"Complete the Accounting Equation table for {ctx['biz_name']}: Received {amt} cash per CRR for {ctx['svc_desc']}.",
        tx_rows=[(f"CRR cash services {amt}", f"+{amt}", f"+{amt}", "0", "Cash increases Bank; Current income increases Equity")],
        notes=f"- `Bank` (Asset) increases (+{amt}).\n- `Current income` (Income) increases Owner's Equity (+{amt}).\n- Liabilities are unchanged (`0`).",
        hints={
            "tier_1": "Receiving money increases Bank (Asset), and earning service income grows Owner's Equity.",
            "tier_2": "Liabilities are unaffected (0).",
            "tier_3": f"Assets: +{amt}, Owner's Equity: +{amt}, Liabilities: 0.",
        },
        misconception_tags=["income_equity_effect_error"],
    )


def build_44_crj_accounting_equation_capital_contribution(rng: random.Random) -> Dict[str, Any]:
    ctx = _biz_ctx(rng)
    amt = _fmt_r(rng.randint(4, 15) * 10000)
    return _equation_table(
        rng,
        qid_prefix="crj44",
        subskill="44_crj_accounting_equation_capital_contribution",
        title="Accounting Equation: Owner Capital Contribution",
        prompt=f"Show the effect on the Accounting Equation when owner {ctx['entrepreneur']} deposits {amt} into {ctx['biz_name']}'s bank account as Capital (R01).",
        tx_rows=[(f"Owner deposits {amt} Capital", f"+{amt}", f"+{amt}", "0", "Cash increases Bank; Capital contribution increases Equity")],
        notes=f"- `Bank` (Asset) increases by +{amt}.\n- `Capital` (Owner's Equity) increases by +{amt}.",
        hints={
            "tier_1": "Owner money entering the business increases Bank (Asset) and Capital (Owner's Equity).",
            "tier_2": "Capital is NOT a liability owed to an external bank — Liabilities stay 0.",
            "tier_3": f"Assets: +{amt}, Owner's Equity: +{amt}, Liabilities: 0.",
        },
        misconception_tags=["capital_treated_as_liability"],
    )


def build_45_crj_accounting_equation_bank_loan_receipt(rng: random.Random) -> Dict[str, Any]:
    ctx = _biz_ctx(rng)
    amt = _fmt_r(rng.randint(2, 9) * 10000)
    return _equation_table(
        rng,
        qid_prefix="crj45",
        subskill="45_crj_accounting_equation_bank_loan_receipt",
        title="Accounting Equation: Receiving a Bank Loan",
        prompt=f"Complete the Accounting Equation effect when {ctx['biz_name']} receives a {amt} business loan from {ctx['bank_name']} (BS).",
        tx_rows=[(f"Bank loan received {amt}", f"+{amt}", "0", f"+{amt}", "Cash increases Bank; Loan obligation increases Liabilities")],
        notes=f"- `Bank` (Asset) increases by +{amt}.\n- `Loan: {ctx['bank_name']}` (Liability) increases by +{amt}; Owner's Equity is `0`.",
        hints={
            "tier_1": "Borrowed money boosts cash in the bank, but creates debt owed back to the bank.",
            "tier_2": "A bank loan is a Liability, NOT Owner's Equity (0).",
            "tier_3": f"Assets: +{amt}, Owner's Equity: 0, Liabilities: +{amt}.",
        },
        misconception_tags=["loan_treated_as_equity_or_income"],
    )


def build_46_crj_accounting_equation_multi_transaction_summary(rng: random.Random) -> Dict[str, Any]:
    ctx = _biz_ctx(rng)
    s_amt = rng.randint(15, 35) * 100
    r_amt = rng.randint(20, 45) * 100
    l_amt = rng.randint(15, 40) * 1000
    net_a = s_amt + r_amt + l_amt
    net_oe = s_amt + r_amt
    return _equation_table(
        rng,
        qid_prefix="crj46",
        subskill="46_crj_accounting_equation_multi_transaction_summary",
        title="Multi-Row CRJ Accounting Equation & Net Totals",
        prompt=f"Analyse these three {ctx['crj_no']} receipts for {ctx['biz_name']} and complete the Totals row:\n1. Services rendered (CRR): {_fmt_r(s_amt)}\n2. Rent income ({ctx['tenant']}): {_fmt_r(r_amt)}\n3. Bank loan ({ctx['bank_name']}): {_fmt_r(l_amt)}",
        tx_rows=[
            (f"1. Services rendered {_fmt_r(s_amt)}", f"+{_fmt_r(s_amt)}", f"+{_fmt_r(s_amt)}", "0", "Bank rises; Current income increases Equity"),
            (f"2. Rent income {_fmt_r(r_amt)}", f"+{_fmt_r(r_amt)}", f"+{_fmt_r(r_amt)}", "0", "Bank rises; Rent income increases Equity"),
            (f"3. Bank loan {_fmt_r(l_amt)}", f"+{_fmt_r(l_amt)}", "0", f"+{_fmt_r(l_amt)}", "Bank rises; Loan increases Liabilities"),
            ("TOTAL EFFECT", f"+{_fmt_r(net_a)}", f"+{_fmt_r(net_oe)}", f"+{_fmt_r(l_amt)}", f"Check: A (+{_fmt_r(net_a)}) = OE (+{_fmt_r(net_oe)}) + L (+{_fmt_r(l_amt)})"),
        ],
        notes=f"Final equation check: `{_fmt_r(net_a)} = {_fmt_r(net_oe)} + {_fmt_r(l_amt)}` holds true!",
        hints={
            "tier_1": "Income items (Services, Rent) increase A and OE; Loans increase A and L.",
            "tier_2": "Add each column vertically for the NET EFFECT row.",
            "tier_3": f"Net Assets = +{_fmt_r(net_a)}, Net OE = +{_fmt_r(net_oe)}, Net Liabilities = +{_fmt_r(l_amt)}.",
        },
        misconception_tags=["equation_imbalance", "loan_in_equity"],
    )


def build_47_crj_account_1_account_2_mapping(rng: random.Random) -> Dict[str, Any]:
    ctx = _biz_ctx(rng)
    c_amt = _fmt_r(rng.randint(5, 10) * 10000)
    s_amt = _fmt_r(rng.randint(25, 65) * 100)
    r_amt = _fmt_r(rng.randint(30, 55) * 100)
    items = [
        (f"Day 03: Direct Capital deposit of {c_amt} by {ctx['entrepreneur']}", "Bank", "Capital"),
        (f"Day 14: CRR Services rendered of {s_amt}", "Bank", "Current income"),
        (f"Day 28: Receipt to {ctx['tenant']} for {r_amt} Rent", "Bank", "Rent income"),
    ]
    rng.shuffle(items)
    headers = ["CRJ Receipt Transaction", "Account Debited (Account 1)", "Account Credited (Account 2)"]
    rows, cmap, chints, str_rows, mps = [], {}, {}, [], []
    mp_i = 1
    for r_i, (tx, dr_acct, cr_acct) in enumerate(items):
        str_rows.append([tx, dr_acct, cr_acct])
        c0 = _cell(r_i, 0, tx, editable=False)
        c1 = _cell(r_i, 1, dr_acct, editable=True)
        c2 = _cell(r_i, 2, cr_acct, editable=True)
        rows.append([c0, c1, c2])
        cmap[c1["cell_id"]] = dr_acct
        cmap[c2["cell_id"]] = cr_acct
        chints[c1["cell_id"]] = "In EVERY CRJ receipt, which Asset account receives the cash?"
        chints[c2["cell_id"]] = "Identify the exact source account (Capital, Current income, or Rent income)."
        mps.append({"id": f"mp_{mp_i}", "desc": f"R{r_i + 1} Dr: {dr_acct}", "marks": 1, "editable": True})
        mps.append({"id": f"mp_{mp_i + 1}", "desc": f"R{r_i + 1} Cr: {cr_acct}", "marks": 1, "editable": True})
        mp_i += 2
    md = _md_table(headers, str_rows)
    return _build_table(
        rng,
        qid_prefix="crj47",
        subskill="47_crj_account_1_account_2_mapping",
        title="CRJ Account 1 (Debit) & Account 2 (Credit) Mapping",
        prompt=f"For each CRJ entry of {ctx['biz_name']} below, identify Account 1 (Account Debited) and Account 2 (Account Credited).",
        headers=headers,
        rows=rows,
        correct_map=cmap,
        cell_hints=chints,
        worked_solution=f"**CRJ Double-Entry Mapping (6 marks)**\n\n{md}",
        sample_answer=md,
        marks=len(mps),
        hints={
            "tier_1": "Remember: every receipt increases Bank (Asset), and Assets increase on the Debit side.",
            "tier_2": "So Account Debited is ALWAYS Bank; Account Credited comes from Current income or Sundry Details.",
            "tier_3": "Fill 'Bank' in every Account 1 cell, then match Capital / Current income / Rent income.",
        },
        marking_points=mps,
        misconception_tags=["debit_credit_reversal_crj"],
        qtype="table_completion",
        journal_type="classification",
    )


def build_48_crj_crj1_vs_crj11_owner_capital_interpretation(rng: random.Random) -> Dict[str, Any]:
    ctx = _biz_ctx(rng)
    open_cap = rng.randint(8, 16) * 10000
    add_cap = rng.randint(2, 6) * 10000
    new_cap = open_cap + add_cap
    j_num = rng.randint(6, 12)
    return _build_short(
        rng,
        qid_prefix="crj48",
        subskill="48_crj_crj1_vs_crj11_owner_capital_interpretation",
        title="Capital Increase Calculation in Later Months (CRJ6–CRJ12)",
        prompt=(
            f"Before {ctx['month_full']}, {ctx['biz_name']} had an opening Capital balance of {_fmt_r(open_cap)}. "
            f"In journal CRJ{j_num}, {ctx['entrepreneur']} deposited a further {_fmt_r(add_cap)} as Capital. "
            f"Calculate {ctx['biz_name']}'s new total Capital balance after posting CRJ{j_num}."
        ),
        expected_answer=_fmt_r(new_cap),
        worked_solution=(
            f"- Journal CRJ{j_num} confirms the business is already trading (not CRJ1).\n"
            f"- New Capital = Opening Capital ({_fmt_r(open_cap)}) + Additional Capital ({_fmt_r(add_cap)}) = **{_fmt_r(new_cap)}**."
        ),
        hints={
            "tier_1": "Since CRJ" + str(j_num) + " is not CRJ1, the owner is adding to existing Capital.",
            "tier_2": "Add the CRJ capital deposit to the opening Capital balance.",
            "tier_3": f"{_fmt_r(open_cap)} + {_fmt_r(add_cap)} = {_fmt_r(new_cap)}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Adds {_fmt_r(open_cap)} + {_fmt_r(add_cap)}", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": f"New Capital = {_fmt_r(new_cap)}", "marks": 1, "editable": True},
        ],
        misconception_tags=["replaces_opening_capital_instead_of_adding"],
    )


def build_49_crj_posting_summary_to_general_ledger_totals(rng: random.Random) -> Dict[str, Any]:
    ctx = _biz_ctx(rng)
    ci = rng.randint(14, 32) * 1000
    cap = rng.randint(4, 8) * 10000
    rent = rng.randint(25, 55) * 100
    sun = cap + rent
    bank = ci + sun
    svg = _crj_flow_svg(ctx["biz_name"], ctx["crj_no"], rng.randint(15, 30), bank, ci, sun)
    headers = ["General Ledger Account", "Debit or Credit?", "Amount Posted from CRJ"]
    items = [
        ("Bank (B3)", "Debit", _fmt_r(bank)),
        ("Current income (N1)", "Credit", _fmt_r(ci)),
        ("Capital (B1)", "Credit", _fmt_r(cap)),
        ("Rent income (N2)", "Credit", _fmt_r(rent)),
    ]
    rows, cmap, chints, str_rows, mps = [], {}, {}, [], []
    mp_i = 1
    for r_i, (acct, side, amt) in enumerate(items):
        str_rows.append([acct, side, amt])
        c0 = _cell(r_i, 0, acct, editable=False)
        c1 = _cell(r_i, 1, side, editable=True)
        c2 = _cell(r_i, 2, amt, editable=True, is_money=True)
        rows.append([c0, c1, c2])
        cmap[c1["cell_id"]] = side
        cmap[c2["cell_id"]] = amt
        chints[c1["cell_id"]] = "Enter 'Debit' or 'Credit'."
        chints[c2["cell_id"]] = "Enter the exact total/Sundry Rand amount posted."
        mps.append({"id": f"mp_{mp_i}", "desc": f"{acct} side: {side}", "marks": 1, "editable": True})
        mps.append({"id": f"mp_{mp_i + 1}", "desc": f"{acct} amount: {amt}", "marks": 1, "editable": True})
        mp_i += 2
    md = _md_table(headers, str_rows)
    return _build_table(
        rng,
        qid_prefix="crj49",
        subskill="49_crj_posting_summary_to_general_ledger_totals",
        title="Posting Month-End CRJ Totals to the General Ledger",
        prompt=(
            f"Inspect the {ctx['crj_no']} to General Ledger posting diagram below for {ctx['biz_name']} "
            f"(Bank Total {_fmt_r(bank)}, Current Income {_fmt_r(ci)}, Sundry {_fmt_r(sun)}: Capital {_fmt_r(cap)} and Rent income {_fmt_r(rent)}). "
            f"Complete the General Ledger posting table."
        ),
        headers=headers,
        rows=rows,
        correct_map=cmap,
        cell_hints=chints,
        worked_solution=f"**CRJ to General Ledger Posting Summary (8 marks)**\n\n{md}",
        sample_answer=md,
        marks=len(mps),
        hints={
            "tier_1": "One account (Bank) is debited with the grand total; every source column/Sundry item is credited.",
            "tier_2": "Bank = Debit; Current income, Capital, and Rent income = Credit.",
            "tier_3": f"Verify Debits ({_fmt_r(bank)}) equal sum of Credits ({_fmt_r(ci)} + {_fmt_r(cap)} + {_fmt_r(rent)}).",
        },
        marking_points=mps,
        misconception_tags=["gl_posting_side_error", "sundry_posted_as_one_account"],
        qtype="table_completion",
        journal_type="posting",
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    )


def build_50_crj_month_end_cash_receipts_management_synthesis(rng: random.Random) -> Dict[str, Any]:
    ctx = _biz_ctx(rng)
    # Clean percentage pairs summing to clean Bank Total
    ci_pct = rng.choice([25, 30, 35, 40, 45, 50, 60])
    rent_pct = rng.choice([10, 15, 20])
    cap_pct = 100 - ci_pct - rent_pct
    unit = rng.randint(4, 12) * 100
    ci = ci_pct * unit
    rent = rent_pct * unit
    cap = cap_pct * unit
    bank_tot = ci + rent + cap
    bars = [
        ("Current Income", ci, "#0284c7"),
        ("Rent Income", rent, "#059669"),
        ("Capital Injection", cap, "#7c3aed"),
    ]
    svg = _crj_bar_svg(ctx["biz_name"], "Cash Inflow Composition", bars)
    prompt = (
        f"Inspect the Cash Inflow Composition chart below for {ctx['biz_name']} in {ctx['month_full']}: "
        f"Current Income = {_fmt_r(ci)}, Rent Income = {_fmt_r(rent)}, and Owner Capital = {_fmt_r(cap)} "
        f"(Total Bank Receipts = {_fmt_r(bank_tot)}). "
        f"What percentage of total cash receipts came from core day-to-day service operations (Current Income)?"
    )
    ans = f"{ci_pct}%"
    worked = (
        f"Core Services Percentage = (Current Income / Total Bank Receipts) x 100\n"
        f"= ({_fmt_r(ci)} / {_fmt_r(bank_tot)}) x 100 = **{ans}**."
    )
    return _build_short(
        rng,
        qid_prefix="crj50",
        subskill="50_crj_month_end_cash_receipts_management_synthesis",
        title="Analysing Cash Inflow Composition from the CRJ",
        prompt=prompt,
        expected_answer=ans,
        worked_solution=worked,
        hints={
            "tier_1": "Divide Current Income by Total Bank Receipts, then multiply by 100.",
            "tier_2": f"Use Total Bank Receipts = {_fmt_r(ci)} + {_fmt_r(rent)} + {_fmt_r(cap)} = {_fmt_r(bank_tot)}.",
            "tier_3": f"({_fmt_r(ci)} / {_fmt_r(bank_tot)}) x 100 = {ans}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Total Bank Receipts = {_fmt_r(bank_tot)}", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": f"Core service percentage = {ans}", "marks": 2, "editable": True},
        ],
        misconception_tags=["percentage_base_error", "included_capital_as_operating_income"],
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    )


BUILDERS_26_50: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    "26_crj_two_transaction_starter_journal": build_26_crj_two_transaction_starter_journal,
    "27_crj_three_transaction_same_day_and_direct_deposit": build_27_crj_three_transaction_same_day_and_direct_deposit,
    "28_crj_four_transaction_full_services_month": build_28_crj_four_transaction_full_services_month,
    "29_crj_five_transaction_comprehensive_journal": build_29_crj_five_transaction_comprehensive_journal,
    "30_crj_receipt_slip_to_journal_transcription": build_30_crj_receipt_slip_to_journal_transcription,
    "31_crj_bank_statement_extract_to_crj_entries": build_31_crj_bank_statement_extract_to_crj_entries,
    "32_crj_cross_checking_horizontal_balancing_rule": build_32_crj_cross_checking_horizontal_balancing_rule,
    "33_crj_cross_check_verification_audit": build_33_crj_cross_check_verification_audit,
    "34_crj_closing_off_and_double_ruling_rules": build_34_crj_closing_off_and_double_ruling_rules,
    "35_crj_missing_current_income_deduction": build_35_crj_missing_current_income_deduction,
    "36_crj_missing_sundry_amount_and_account_deduction": build_36_crj_missing_sundry_amount_and_account_deduction,
    "37_crj_missing_same_day_deposit_reconstruction": build_37_crj_missing_same_day_deposit_reconstruction,
    "38_crj_missing_analysis_entry_from_daily_bank": build_38_crj_missing_analysis_entry_from_daily_bank,
    "39_crj_spot_error_direct_deposit_in_analysis": build_39_crj_spot_error_direct_deposit_in_analysis,
    "40_crj_spot_error_same_day_banked_separately": build_40_crj_spot_error_same_day_banked_separately,
    "41_crj_spot_error_sundry_posted_to_current_income": build_41_crj_spot_error_sundry_posted_to_current_income,
    "42_crj_spot_error_analysis_added_to_totals": build_42_crj_spot_error_analysis_added_to_totals,
    "43_crj_accounting_equation_services_rendered": build_43_crj_accounting_equation_services_rendered,
    "44_crj_accounting_equation_capital_contribution": build_44_crj_accounting_equation_capital_contribution,
    "45_crj_accounting_equation_bank_loan_receipt": build_45_crj_accounting_equation_bank_loan_receipt,
    "46_crj_accounting_equation_multi_transaction_summary": build_46_crj_accounting_equation_multi_transaction_summary,
    "47_crj_account_1_account_2_mapping": build_47_crj_account_1_account_2_mapping,
    "48_crj_crj1_vs_crj11_owner_capital_interpretation": build_48_crj_crj1_vs_crj11_owner_capital_interpretation,
    "49_crj_posting_summary_to_general_ledger_totals": build_49_crj_posting_summary_to_general_ledger_totals,
    "50_crj_month_end_cash_receipts_management_synthesis": build_50_crj_month_end_cash_receipts_management_synthesis,
}
