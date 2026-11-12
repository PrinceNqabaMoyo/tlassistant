"""Grade 8 EMS - Cash Receipts Journal 2 & Cash Payments Journal: Archetypes 26 to 50.

Grounded strictly in curriculum_docs_auto/EMS_Gr8/Term 2/
03. Cash receipts journal for a services business 2.md and
04. Cash payments journal for a services business.md.
Zero-LLM, 100% deterministic, South African Rand (R) contexts.
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Tuple

from .cpj_crj_archetypes_01_25 import (
    CPJ_HEADERS,
    _biz_ctx,
    _build_mcq,
    _build_short,
    _build_table,
    _cell,
    _cheque_counterfoil_svg,
    _cpj_crj_flow_svg,
    _cpj_journal_question,
    _fmt_r,
    _md_table,
)


def _cpj_bar_svg(biz_name: str, title: str, bars: List[Tuple[str, int, str]]) -> str:
    """Context SVG horizontal breakdown bar chart of CPJ column totals."""
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


def _bank_t_account_svg(
    biz_name: str,
    month_full: str,
    open_bal: int,
    crj_tot: int,
    cpj_tot: int,
    closing_bal: int | None = None,
) -> str:
    """Context SVG showing the General Ledger Bank T-Account (Dr Receipts vs Cr Payments)."""
    dr_total = open_bal + crj_tot
    close_str = _fmt_r(closing_bal) if closing_bal is not None else "?"
    return (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 225" width="600" height="225">'
        '<rect width="600" height="225" rx="8" fill="#ffffff" stroke="#334155" stroke-width="1.5"/>'
        f'<text x="300" y="24" font-size="13" font-weight="bold" text-anchor="middle" fill="#0f172a">{biz_name} — Bank Account (B3) | {month_full}</text>'
        '<text x="24" y="42" font-size="11" font-weight="bold" fill="#047857">Dr (+)</text>'
        '<text x="576" y="42" font-size="11" font-weight="bold" text-anchor="end" fill="#be123c">Cr (-)</text>'
        '<line x1="20" y1="50" x2="580" y2="50" stroke="#0f172a" stroke-width="2"/>'
        '<line x1="300" y1="50" x2="300" y2="205" stroke="#0f172a" stroke-width="2"/>'
        '<text x="28" y="76" font-size="11" fill="#1e293b">01 Balance b/d</text>'
        f'<text x="284" y="76" font-size="11" font-weight="bold" text-anchor="end" fill="#0f172a">{_fmt_r(open_bal)}</text>'
        '<text x="28" y="102" font-size="11" fill="#1e293b">30 Total receipts (CRJ)</text>'
        f'<text x="284" y="102" font-size="11" font-weight="bold" text-anchor="end" fill="#047857">{_fmt_r(crj_tot)}</text>'
        '<line x1="180" y1="120" x2="286" y2="120" stroke="#475569"/>'
        f'<text x="284" y="138" font-size="12" font-weight="bold" text-anchor="end" fill="#0f172a">{_fmt_r(dr_total)}</text>'
        '<line x1="180" y1="146" x2="286" y2="146" stroke="#0f172a" stroke-width="1.5"/>'
        '<text x="316" y="76" font-size="11" fill="#1e293b">30 Total payments (CPJ)</text>'
        f'<text x="572" y="76" font-size="11" font-weight="bold" text-anchor="end" fill="#be123c">{_fmt_r(cpj_tot)}</text>'
        '<text x="316" y="102" font-size="11" fill="#1e293b">30 Balance c/d</text>'
        f'<text x="572" y="102" font-size="12" font-weight="bold" text-anchor="end" fill="#1d4ed8">{close_str}</text>'
        '<line x1="468" y1="120" x2="574" y2="120" stroke="#475569"/>'
        f'<text x="572" y="138" font-size="12" font-weight="bold" text-anchor="end" fill="#0f172a">{_fmt_r(dr_total)}</text>'
        '<line x1="468" y1="146" x2="574" y2="146" stroke="#0f172a" stroke-width="1.5"/>'
        '<text x="28" y="182" font-size="11" fill="#334155">Next Month 01 Balance b/d</text>'
        f'<text x="284" y="182" font-size="11" font-weight="bold" text-anchor="end" fill="#1d4ed8">{close_str}</text>'
        '</svg>'
    )


def _cpj_eq_table(
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
            chints[cell["cell_id"]] = "Enter +R..., -R..., or 0 for overall column change, then state the accounting reason."
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

def build_26_cpj_two_transaction_starter_journal(rng: random.Random) -> Dict[str, Any]:
    ctx = _biz_ctx(rng)
    w_amt = rng.randint(15, 35) * 100
    s_amt = rng.randint(4, 15) * 100
    tot = w_amt + s_amt
    prompt = (
        f"Prepare {ctx['cpj_no']} for {ctx['biz_name']} ({ctx['month_full']}) from these two opening payments and complete the Totals row:\n"
        f"- Day 05: Cashed cheque C01 for {_fmt_r(w_amt)} to pay weekly staff wages.\n"
        f"- Day 12: Paid {ctx['supplier']} {_fmt_r(s_amt)} by EFT (EFT1) for stationery."
    )
    row_specs = [
        (["C01", "05", "Cash", "", _fmt_r(w_amt), _fmt_r(w_amt), "", "", ""], [0, 1], {}),
        (["EFT1", "12", ctx["supplier"], "", _fmt_r(s_amt), "", _fmt_r(s_amt), "", ""], [0, 1], {}),
        (["", "", "TOTALS", "", _fmt_r(tot), _fmt_r(w_amt), _fmt_r(s_amt), "", ""], [0, 1, 2, 3, 7, 8], {}),
    ]
    return _cpj_journal_question(
        rng,
        qid_prefix="cpj26",
        subskill="26_cpj_two_transaction_starter_journal",
        title="Two-Transaction Starter CPJ with Totals",
        prompt=prompt,
        row_specs=row_specs,
        explanation_notes=f"Cross-check: Bank ({_fmt_r(tot)}) = Wages ({_fmt_r(w_amt)}) + Stationery ({_fmt_r(s_amt)}).",
        hints={
            "tier_1": "Use Payee 'Cash' for wages, supplier name for stationery, and sum each money column at the bottom.",
            "tier_2": "Leave Sundry columns blank because both payments have dedicated columns.",
            "tier_3": f"Bank Total = {_fmt_r(tot)}, Wages = {_fmt_r(w_amt)}, Stationery = {_fmt_r(s_amt)}.",
        },
        misconception_tags=["cpj_totals_imbalance", "wages_written_as_payee"],
    )


def build_27_cpj_three_transaction_wages_equipment_drawings(rng: random.Random) -> Dict[str, Any]:
    ctx = _biz_ctx(rng)
    w_amt = rng.randint(16, 36) * 100
    eq_amt = rng.randint(4, 14) * 1000
    dr_amt = rng.randint(12, 32) * 100
    tot_b = w_amt + eq_amt + dr_amt
    tot_sun = eq_amt + dr_amt
    prompt = (
        f"Complete {ctx['cpj_no']} for {ctx['biz_name']} ({ctx['month_full']}) and balance the Totals row:\n"
        f"- Day 04: Paid {ctx['supplier']} {_fmt_r(eq_amt)} via cheque C11 for salon/workshop equipment (fol. B2).\n"
        f"- Day 11: Cashed cheque C12 for {_fmt_r(w_amt)} for staff wages.\n"
        f"- Day 18: Owner {ctx['entrepreneur']} withdrew {_fmt_r(dr_amt)} (cheque C13) for personal household use (fol. B6)."
    )
    row_specs = [
        (["C11", "04", ctx["supplier"], "B2", _fmt_r(eq_amt), "", "", _fmt_r(eq_amt), "Equipment"], [0, 1, 3], {}),
        (["C12", "11", "Cash", "", _fmt_r(w_amt), _fmt_r(w_amt), "", "", ""], [0, 1], {}),
        (["C13", "18", ctx["entrepreneur"], "B6", _fmt_r(dr_amt), "", "", _fmt_r(dr_amt), "Drawings"], [0, 1, 3], {}),
        (["", "", "TOTALS", "", _fmt_r(tot_b), _fmt_r(w_amt), "", _fmt_r(tot_sun), ""], [0, 1, 2, 3, 6, 8], {}),
    ]
    return _cpj_journal_question(
        rng,
        qid_prefix="cpj27",
        subskill="27_cpj_three_transaction_wages_equipment_drawings",
        title="Three-Transaction CPJ: Equipment, Wages & Drawings",
        prompt=prompt,
        row_specs=row_specs,
        explanation_notes=(
            f"- Equipment and Drawings both enter `Sundry Accounts`.\n"
            f"- Check: Wages ({_fmt_r(w_amt)}) + Sundry ({_fmt_r(tot_sun)}) = Bank ({_fmt_r(tot_b)})."
        ),
        hints={
            "tier_1": "Equipment and Drawings lack dedicated columns here, so both enter Sundry Accounts.",
            "tier_2": "Wages uses Payee 'Cash' and enters the Wages column.",
            "tier_3": f"Bank = {_fmt_r(tot_b)}, Wages = {_fmt_r(w_amt)}, Sundry = {_fmt_r(tot_sun)}.",
        },
        misconception_tags=["drawings_classified_as_wages", "cpj_totals_imbalance"],
    )


def build_28_cpj_four_transaction_with_split_cheque(rng: random.Random) -> Dict[str, Any]:
    ctx = _biz_ctx(rng)
    w_amt = rng.randint(15, 32) * 100
    s_part = rng.randint(5, 14) * 100
    eq_part = rng.randint(25, 55) * 100
    split_tot = s_part + eq_part
    rent_amt = rng.randint(30, 65) * 100
    fee = rng.randint(15, 38) * 10 + 5
    tot_b = w_amt + split_tot + rent_amt + fee
    tot_sun = eq_part + rent_amt + fee
    prompt = (
        f"Complete {ctx['cpj_no']} for {ctx['biz_name']} ({ctx['month_full']}) and balance the Totals row:\n"
        f"- Day 02: Paid {ctx['landlord']} {_fmt_r(rent_amt)} (EFT1) for monthly rent (fol. N4).\n"
        f"- Day 09: Cashed cheque C21 for {_fmt_r(w_amt)} for wages.\n"
        f"- Day 16: Paid {ctx['supplier']} {_fmt_r(split_tot)} (EFT2) in one transfer for {_fmt_r(s_part)} stationery and {_fmt_r(eq_part)} equipment (fol. B2).\n"
        f"- Day 30: Bank Statement (BS) from {ctx['bank_name']} shows {_fmt_r(fee)} bank charges (fol. N8)."
    )
    row_specs = [
        (["EFT1", "02", ctx["landlord"], "N4", _fmt_r(rent_amt), "", "", _fmt_r(rent_amt), "Rent expense"], [0, 1, 3], {}),
        (["C21", "09", "Cash", "", _fmt_r(w_amt), _fmt_r(w_amt), "", "", ""], [0, 1], {}),
        (["EFT2", "16", ctx["supplier"], "B2", _fmt_r(split_tot), "", _fmt_r(s_part), _fmt_r(eq_part), "Equipment"], [0, 1, 3], {}),
        (["BS", "30", ctx["bank_name"], "N8", _fmt_r(fee), "", "", _fmt_r(fee), "Bank charges"], [0, 1, 3], {}),
        (["", "", "TOTALS", "", _fmt_r(tot_b), _fmt_r(w_amt), _fmt_r(s_part), _fmt_r(tot_sun), ""], [0, 1, 2, 3, 8], {}),
    ]
    return _cpj_journal_question(
        rng,
        qid_prefix="cpj28",
        subskill="28_cpj_four_transaction_with_split_cheque",
        title="Four-Transaction CPJ with Split Payment & Bank Charges",
        prompt=prompt,
        row_specs=row_specs,
        explanation_notes=(
            f"- EFT2 enters Bank once as {_fmt_r(split_tot)} and splits across Stationery ({_fmt_r(s_part)}) and Equipment ({_fmt_r(eq_part)}).\n"
            f"- Check: {_fmt_r(w_amt)} + {_fmt_r(s_part)} + {_fmt_r(tot_sun)} = {_fmt_r(tot_b)}."
        ),
        hints={
            "tier_1": "Pay attention to Row 3 (one EFT split across Stationery and Sundry Equipment) and Row 4 (Bank charges on BS).",
            "tier_2": f"EFT2 Bank = {_fmt_r(split_tot)}; Rent is 'Rent expense'; BS charges are 'Bank charges'.",
            "tier_3": f"Totals: Bank = {_fmt_r(tot_b)}, Wages = {_fmt_r(w_amt)}, Stationery = {_fmt_r(s_part)}, Sundry = {_fmt_r(tot_sun)}.",
        },
        misconception_tags=["split_cheque_duplicated_in_bank", "bank_charges_missing_or_in_crj"],
    )


def build_29_cpj_five_transaction_comprehensive_journal(rng: random.Random) -> Dict[str, Any]:
    ctx = _biz_ctx(rng)
    w1 = rng.randint(14, 28) * 100
    st = rng.randint(5, 13) * 100
    eq = rng.randint(25, 55) * 100
    we = rng.randint(11, 26) * 100
    dr = rng.randint(10, 25) * 100
    tot_b = w1 + st + eq + we + dr
    tot_sun = eq + we + dr
    prompt = (
        f"Prepare the comprehensive 5-transaction {ctx['cpj_no']} for {ctx['biz_name']} in {ctx['month_full']} and balance all money columns:\n"
        f"- Day 03: Cashed cheque C31 for {_fmt_r(w1)} for wages.\n"
        f"- Day 08: Paid {ctx['supplier']} {_fmt_r(st)} (EFT3) for stationery.\n"
        f"- Day 14: Paid {ctx['competitor']} {_fmt_r(eq)} (C32) for new workshop equipment (fol. B2).\n"
        f"- Day 21: Paid {ctx['municipality']} {_fmt_r(we)} (EFT4) for water and electricity (fol. N7).\n"
        f"- Day 26: {ctx['entrepreneur']} took {_fmt_r(dr)} via EFT5 for personal expenses (fol. B6)."
    )
    row_specs = [
        (["C31", "03", "Cash", "", _fmt_r(w1), _fmt_r(w1), "", "", ""], [0, 1], {}),
        (["EFT3", "08", ctx["supplier"], "", _fmt_r(st), "", _fmt_r(st), "", ""], [0, 1], {}),
        (["C32", "14", ctx["competitor"], "B2", _fmt_r(eq), "", "", _fmt_r(eq), "Equipment"], [0, 1, 3], {}),
        (["EFT4", "21", ctx["municipality"], "N7", _fmt_r(we), "", "", _fmt_r(we), "Water and electricity"], [0, 1, 3], {}),
        (["EFT5", "26", ctx["entrepreneur"], "B6", _fmt_r(dr), "", "", _fmt_r(dr), "Drawings"], [0, 1, 3], {}),
        (["", "", "TOTALS", "", _fmt_r(tot_b), _fmt_r(w1), _fmt_r(st), _fmt_r(tot_sun), ""], [0, 1, 2, 3, 8], {}),
    ]
    return _cpj_journal_question(
        rng,
        qid_prefix="cpj29",
        subskill="29_cpj_five_transaction_comprehensive_journal",
        title="Comprehensive Five-Transaction CPJ Preparation",
        prompt=prompt,
        row_specs=row_specs,
        explanation_notes=(
            f"- Wages ({_fmt_r(w1)}) and Stationery ({_fmt_r(st)}) fill dedicated analysis columns.\n"
            f"- Equipment ({_fmt_r(eq)}), Water and electricity ({_fmt_r(we)}), and Drawings ({_fmt_r(dr)}) sum to Sundry {_fmt_r(tot_sun)}.\n"
            f"- Check: {_fmt_r(w1)} + {_fmt_r(st)} + {_fmt_r(tot_sun)} = {_fmt_r(tot_b)}."
        ),
        hints={
            "tier_1": "Sort Wages and Stationery into their own columns, and group Equipment, utilities, and Drawings into Sundry.",
            "tier_2": "Remember Payee 'Cash' on Day 03 and 'Drawings' on Day 26.",
            "tier_3": f"Bank Total = {_fmt_r(tot_b)}, Wages = {_fmt_r(w1)}, Stationery = {_fmt_r(st)}, Sundry = {_fmt_r(tot_sun)}.",
        },
        misconception_tags=["comprehensive_cpj_errors", "cpj_totals_imbalance"],
    )


def build_30_cpj_cheque_counterfoil_to_journal_transcription(rng: random.Random) -> Dict[str, Any]:
    ctx = _biz_ctx(rng)
    c_no = f"C{rng.randint(104, 198)}"
    day = f"{rng.randint(8, 22):02d}"
    amt = rng.randint(14, 48) * 100
    amt_s = _fmt_r(amt)
    svg = _cheque_counterfoil_svg(ctx["biz_name"], c_no, f"{day} {ctx['month_full']}", ctx["supplier"], "Office stationery & receipt books", amt)
    prompt = (
        f"Inspect the cheque counterfoil stub shown below for {ctx['biz_name']}. "
        f"Read the cheque number, day, payee, purpose, and Rand amount from the stub to complete the full CPJ row."
    )
    row_specs = [
        ([c_no, day, ctx["supplier"], "", amt_s, "", amt_s, "", ""], [], {
            0: "Copy the cheque number from the top-right badge.",
            1: "Extract the two-digit day from the Date line.",
            2: "Copy the Payee name from 'To (Payee)'.",
        }),
    ]
    return _cpj_journal_question(
        rng,
        qid_prefix="cpj30",
        subskill="30_cpj_cheque_counterfoil_to_journal_transcription",
        title="Transcribing a Cheque Counterfoil Stub into the CPJ",
        prompt=prompt,
        row_specs=row_specs,
        explanation_notes=f"From stub {c_no} ({day} {ctx['month_short']}), pay `{ctx['supplier']}` {amt_s} in `Bank` and `Stationery`.",
        hints={
            "tier_1": "Read Cheque No, Day, To (Payee), Reason, and Amount from the stub.",
            "tier_2": "Stationery has its own dedicated analysis column.",
            "tier_3": f"Doc={c_no}, Day={day}, Payee={ctx['supplier']}, Bank={amt_s}, Stationery={amt_s}.",
        },
        misconception_tags=["cpj_transcription_error"],
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    )


def build_31_cpj_cross_checking_horizontal_balancing_rule(rng: random.Random) -> Dict[str, Any]:
    ctx = _biz_ctx(rng)
    w = rng.randint(6, 18) * 1000
    st = rng.randint(15, 45) * 100
    sun = rng.randint(10, 35) * 1000
    bank = w + st + sun
    target = rng.choice(["Bank", "Sundry Accounts", "Stationery"])
    if target == "Bank":
        bars = [("Wages", w, "#0284c7"), ("Stationery", st, "#d97706"), ("Sundry Accounts", sun, "#7c3aed")]
        prompt = f"Study the {ctx['cpj_no']} totals chart for {ctx['biz_name']}: Wages = {_fmt_r(w)}, Stationery = {_fmt_r(st)}, and Sundry Accounts = {_fmt_r(sun)}. Calculate Total Bank payments."
        ans = _fmt_r(bank)
        worked = f"Total Bank = {_fmt_r(w)} + {_fmt_r(st)} + {_fmt_r(sun)} = **{ans}**."
    elif target == "Sundry Accounts":
        bars = [("Total Bank", bank, "#be123c"), ("Wages", w, "#0284c7"), ("Stationery", st, "#d97706")]
        prompt = f"Study the {ctx['cpj_no']} totals chart for {ctx['biz_name']}: Total Bank = {_fmt_r(bank)}, Wages = {_fmt_r(w)}, and Stationery = {_fmt_r(st)}. Calculate Total Sundry Accounts."
        ans = _fmt_r(sun)
        worked = f"Total Sundry Accounts = {_fmt_r(bank)} - ({_fmt_r(w)} + {_fmt_r(st)}) = **{ans}**."
    else:
        bars = [("Total Bank", bank, "#be123c"), ("Wages", w, "#0284c7"), ("Sundry Accounts", sun, "#7c3aed")]
        prompt = f"Study the {ctx['cpj_no']} totals chart for {ctx['biz_name']}: Total Bank = {_fmt_r(bank)}, Wages = {_fmt_r(w)}, and Sundry Accounts = {_fmt_r(sun)}. Calculate Total Stationery."
        ans = _fmt_r(st)
        worked = f"Total Stationery = {_fmt_r(bank)} - ({_fmt_r(w)} + {_fmt_r(sun)}) = **{ans}**."
    svg = _cpj_bar_svg(ctx["biz_name"], f"{ctx['cpj_no']} Totals Summary", bars)
    return _build_short(
        rng,
        qid_prefix="cpj31",
        subskill="31_cpj_cross_checking_horizontal_balancing_rule",
        title="Cross-Checking CPJ Column Totals",
        prompt=prompt,
        expected_answer=ans,
        worked_solution=worked,
        hints={
            "tier_1": "In a balanced CPJ, Total Bank equals the sum of all analysis and Sundry totals.",
            "tier_2": "Use Total Bank = Wages + Stationery + Sundry Accounts.",
            "tier_3": worked,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Applies CPJ horizontal balancing identity", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": f"Correct missing total: {ans}", "marks": 2, "editable": True},
        ],
        misconception_tags=["cpj_cross_check_error"],
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    )


def build_32_cpj_missing_sundry_or_wages_entry_deduction(rng: random.Random) -> Dict[str, Any]:
    ctx = _biz_ctx(rng)
    w = rng.randint(4, 12) * 1000
    st = rng.randint(12, 35) * 100
    rent = rng.randint(35, 75) * 100
    miss_equip = rng.randint(25, 65) * 100
    tot_b = w + st + rent + miss_equip
    prompt = (
        f"A partially damaged {ctx['cpj_no']} summary for {ctx['biz_name']} shows:\n"
        f"- Total Bank payments = {_fmt_r(tot_b)}\n"
        f"- Total Wages = {_fmt_r(w)}, Total Stationery = {_fmt_r(st)}\n"
        f"- Sundry items consist of Rent expense {_fmt_r(rent)} and an Equipment purchase of missing amount [K].\n"
        f"Calculate the missing Equipment amount [K]."
    )
    ans = _fmt_r(miss_equip)
    worked = (
        f"1. Total Sundry = {_fmt_r(tot_b)} - ({_fmt_r(w)} + {_fmt_r(st)}) = {_fmt_r(rent + miss_equip)}\n"
        f"2. Missing Equipment [K] = {_fmt_r(rent + miss_equip)} - {_fmt_r(rent)} = **{ans}**."
    )
    return _build_short(
        rng,
        qid_prefix="cpj32",
        subskill="32_cpj_missing_sundry_or_wages_entry_deduction",
        title="Deducing a Missing CPJ Payment Entry from Totals",
        prompt=prompt,
        expected_answer=ans,
        worked_solution=worked,
        hints={
            "tier_1": "Find Total Sundry first by subtracting Wages and Stationery from Total Bank.",
            "tier_2": f"Total Sundry = {_fmt_r(rent + miss_equip)}.",
            "tier_3": f"Subtract Rent ({_fmt_r(rent)}) to get {ans}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Finds Total Sundry = {_fmt_r(rent + miss_equip)}", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": f"Missing Equipment = {ans}", "marks": 2, "editable": True},
        ],
        misconception_tags=["cpj_reverse_deduction_error"],
    )


def build_33_cpj_spot_error_split_cheque_entered_twice_in_bank(rng: random.Random) -> Dict[str, Any]:
    ctx = _biz_ctx(rng)
    a1 = rng.randint(12, 28) * 100
    a2 = rng.randint(6, 18) * 100
    return _build_mcq(
        rng,
        qid_prefix="cpj33",
        subskill="33_cpj_spot_error_split_cheque_entered_twice_in_bank",
        title="Error Audit: Split Cheque Entered on Separate Bank Lines",
        prompt=(
            f"Cheque C48 to {ctx['supplier']} paid {_fmt_r(a1)} for Material costs and {_fmt_r(a2)} for Stationery ({_fmt_r(a1 + a2)} total). "
            f"A learner listed C48 twice in {ctx['cpj_no']} with {_fmt_r(a1)} in Bank on Row 1 and {_fmt_r(a2)} in Bank on Row 2. What is wrong?"
        ),
        correct_text=f"While Total Bank sums to {_fmt_r(a1 + a2)}, splitting one cheque into two Bank entries breaks Bank Statement reconciliation, which shows ONE single payment of {_fmt_r(a1 + a2)}",
        distractors=[
            f"The two amounts should be multiplied together inside Stationery",
            "One cheque always requires two separate Bank column entries in South African books",
            "Material costs and Stationery must be subtracted in Sundry",
        ],
        explanation=f"A single cheque ({_fmt_r(a1 + a2)}) clears the Bank Statement once, so CPJ must show ONE line with {_fmt_r(a1 + a2)} in Bank split across Material costs and Stationery.",
        hints={
            "tier_1": "Check how many entries the bank statement will show for a single cheque.",
            "tier_2": "One cheque = one row and one combined Bank amount.",
            "tier_3": f"Combine into one row showing {_fmt_r(a1 + a2)} in Bank.",
        },
        misconception_tags=["split_cheque_duplicated_in_bank"],
    )


def build_34_cpj_spot_error_drawings_recorded_as_wages(rng: random.Random) -> Dict[str, Any]:
    ctx = _biz_ctx(rng)
    amt = rng.randint(15, 45) * 100
    return _build_short(
        rng,
        qid_prefix="cpj34",
        subskill="34_cpj_spot_error_drawings_recorded_as_wages",
        title="Audit Effect: Owner Drawings Misclassified Under Wages",
        prompt=(
            f"Owner {ctx['entrepreneur']} paid {_fmt_r(amt)} from {ctx['biz_name']}'s bank account for private family groceries, "
            f"but the bookkeeper entered {_fmt_r(amt)} in the 'Wages' column instead of Sundry ('Drawings'). "
            f"By how much are business Wages overstated?"
        ),
        expected_answer=_fmt_r(amt),
        worked_solution=(
            f"- Business `Wages` expense is overstated by **{_fmt_r(amt)}** (which artificially lowers business net profit!).\n"
            f"- Owner `Drawings` in Sundry Accounts is understated by **{_fmt_r(amt)}**."
        ),
        hints={
            "tier_1": "How much personal spending accidentally entered the Wages expense column?",
            "tier_2": "Every Rand of private Drawings placed in Wages inflates Wages by that exact amount.",
            "tier_3": f"Wages is overstated by {_fmt_r(amt)}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": f"States {_fmt_r(amt)} overstatement in Wages", "marks": 2, "editable": True},
        ],
        misconception_tags=["drawings_classified_as_wages"],
    )


def build_35_cpj_accounting_equation_expense_payment(rng: random.Random) -> Dict[str, Any]:
    ctx = _biz_ctx(rng)
    amt = _fmt_r(rng.randint(14, 42) * 100)
    exp_acct = rng.choice(["Wages", "Water and electricity", "Stationery", "Repairs"])
    return _cpj_eq_table(
        rng,
        qid_prefix="cpj35",
        subskill="35_cpj_accounting_equation_expense_payment",
        title=f"Accounting Equation: Paying {exp_acct}",
        prompt=f"Complete the Accounting Equation effect when {ctx['biz_name']} pays {amt} for {exp_acct} in {ctx['cpj_no']}.",
        tx_rows=[(f"Paid {amt} for {exp_acct}", f"-{amt}", f"-{amt}", "0", f"Bank decreases Asset; {exp_acct} expense decreases Equity")],
        notes=f"- `Bank` (Asset) decreases (-{amt}).\n- `{exp_acct}` (Expense) decreases Owner's Equity (-{amt}).",
        hints={
            "tier_1": "Paying cash reduces Bank (Asset), and operating expenses reduce Owner's Equity.",
            "tier_2": "Liabilities remain unchanged (0).",
            "tier_3": f"Assets: -{amt}, Owner's Equity: -{amt}, Liabilities: 0.",
        },
        misconception_tags=["expense_increases_equity_error"],
    )


def build_36_cpj_accounting_equation_asset_purchase_neutral(rng: random.Random) -> Dict[str, Any]:
    ctx = _biz_ctx(rng)
    amt = _fmt_r(rng.randint(4, 15) * 1000)
    return _cpj_eq_table(
        rng,
        qid_prefix="cpj36",
        subskill="36_cpj_accounting_equation_asset_purchase_neutral",
        title="Accounting Equation: Buying Equipment for Cash",
        prompt=(
            f"Show the overall change (+R..., -R..., or 0) on the Accounting Equation when {ctx['biz_name']} buys Equipment for {amt} cash/EFT (CPJ)."
        ),
        tx_rows=[(f"Bought Equipment for {amt} cash", "0", "0", "0", f"Equipment (+{amt}) and Bank (-{amt}) are both Assets")],
        notes=f"- One asset (`Equipment`) increases by +{amt} while another asset (`Bank`) decreases by -{amt}, so overall Assets change by `0`!",
        hints={
            "tier_1": "Buying Equipment is NOT an expense — you traded one Asset (money) for another Asset (equipment).",
            "tier_2": f"Assets change by +{amt} and -{amt}, giving overall 0; OE and L are also 0.",
            "tier_3": "Assets: 0, Owner's Equity: 0, Liabilities: 0.",
        },
        misconception_tags=["equipment_treated_as_expense_reducing_equity"],
    )


def build_37_cpj_accounting_equation_owner_drawings(rng: random.Random) -> Dict[str, Any]:
    ctx = _biz_ctx(rng)
    amt = _fmt_r(rng.randint(15, 45) * 100)
    return _cpj_eq_table(
        rng,
        qid_prefix="cpj37",
        subskill="37_cpj_accounting_equation_owner_drawings",
        title="Accounting Equation: Owner Drawings",
        prompt=f"Complete the Accounting Equation effect when owner {ctx['entrepreneur']} withdraws {amt} from {ctx['biz_name']} for personal use (CPJ).",
        tx_rows=[(f"Owner Drawings {amt}", f"-{amt}", f"-{amt}", "0", "Bank decreases Asset; Drawings decreases Owner's Equity")],
        notes=f"- `Bank` decreases (-{amt}).\n- `Drawings` reduces Owner's Equity (-{amt}).",
        hints={
            "tier_1": "Cash leaves Bank (Asset -), and the owner's stake in the business shrinks (Owner's Equity -).",
            "tier_2": "Liabilities stay 0.",
            "tier_3": f"Assets: -{amt}, Owner's Equity: -{amt}, Liabilities: 0.",
        },
        misconception_tags=["drawings_effects_misunderstood"],
    )


def build_38_cpj_accounting_equation_loan_repayment(rng: random.Random) -> Dict[str, Any]:
    ctx = _biz_ctx(rng)
    amt = _fmt_r(rng.randint(25, 75) * 100)
    return _cpj_eq_table(
        rng,
        qid_prefix="cpj38",
        subskill="38_cpj_accounting_equation_loan_repayment",
        title="Accounting Equation: Repaying a Bank Loan",
        prompt=f"Show the Accounting Equation effect when {ctx['biz_name']} pays {amt} via debit order to repay part of its loan from {ctx['bank_name']} (CPJ).",
        tx_rows=[(f"Loan repayment {amt}", f"-{amt}", "0", f"-{amt}", f"Bank decreases Asset; Loan: {ctx['bank_name']} decreases Liabilities")],
        notes=f"- Paying off debt lowers `Bank` (-{amt}) and lowers `Loan` Liability (-{amt}). Owner's Equity is unaffected (`0`).",
        hints={
            "tier_1": "Repaying a bank loan reduces cash in the bank and shrinks what the business owes.",
            "tier_2": "Loan repayment is NOT an expense — Owner's Equity stays 0.",
            "tier_3": f"Assets: -{amt}, Owner's Equity: 0, Liabilities: -{amt}.",
        },
        misconception_tags=["loan_repayment_classified_as_expense"],
    )


def build_39_crj_vs_cpj_account1_account2_double_entry_table(rng: random.Random) -> Dict[str, Any]:
    ctx = _biz_ctx(rng)
    items = [
        (f"Day 02: Owner {ctx['entrepreneur']} deposited {_fmt_r(50000)} as Capital", "CRJ", "Bank", "Capital"),
        (f"Day 09: CRR Services rendered {_fmt_r(3200)}", "CRJ", "Bank", "Current income"),
        (f"Day 14: Cashed cheque for {_fmt_r(2100)} Wages", "CPJ", "Wages", "Bank"),
        (f"Day 21: Bought Equipment via EFT for {_fmt_r(8400)}", "CPJ", "Equipment", "Bank"),
    ]
    rng.shuffle(items)
    headers = ["Transaction", "Journal (CRJ / CPJ)", "Account Debited (Account 1)", "Account Credited (Account 2)"]
    rows, cmap, chints, str_rows, mps = [], {}, {}, [], []
    mp_i = 1
    for r_i, (tx, jrn, dr, cr) in enumerate(items):
        str_rows.append([tx, jrn, dr, cr])
        c0 = _cell(r_i, 0, tx, editable=False)
        c1 = _cell(r_i, 1, jrn, editable=True)
        c2 = _cell(r_i, 2, dr, editable=True)
        c3 = _cell(r_i, 3, cr, editable=True)
        rows.append([c0, c1, c2, c3])
        cmap[c1["cell_id"]] = jrn
        cmap[c2["cell_id"]] = dr
        cmap[c3["cell_id"]] = cr
        chints[c1["cell_id"]] = "Enter CRJ (money received) or CPJ (money paid)."
        chints[c2["cell_id"]] = "Account debited: Bank for CRJ; item/expense/asset received for CPJ."
        chints[c3["cell_id"]] = "Account credited: source account for CRJ; Bank for CPJ."
        mps.append({"id": f"mp_{mp_i}", "desc": f"R{r_i + 1} Journal: {jrn}", "marks": 1, "editable": True})
        mps.append({"id": f"mp_{mp_i + 1}", "desc": f"R{r_i + 1} Dr: {dr}", "marks": 1, "editable": True})
        mps.append({"id": f"mp_{mp_i + 2}", "desc": f"R{r_i + 1} Cr: {cr}", "marks": 1, "editable": True})
        mp_i += 3
    md = _md_table(headers, str_rows)
    return _build_table(
        rng,
        qid_prefix="cpj39",
        subskill="39_crj_vs_cpj_account1_account2_double_entry_table",
        title="CRJ vs CPJ Account 1 (Debit) & Account 2 (Credit) Table",
        prompt=f"For each mixed cash transaction of {ctx['biz_name']}, select the correct journal (CRJ or CPJ), Account Debited (Account 1), and Account Credited (Account 2).",
        headers=headers,
        rows=rows,
        correct_map=cmap,
        cell_hints=chints,
        worked_solution=f"**CRJ & CPJ Double-Entry Mapping (12 marks)**\n\n{md}",
        sample_answer=md,
        marks=len(mps),
        hints={
            "tier_1": "In CRJ, Bank is ALWAYS Debited; in CPJ, Bank is ALWAYS Credited.",
            "tier_2": "Pair Bank with Capital / Current income (CRJ) or Wages / Equipment (CPJ).",
            "tier_3": "Match each transaction to CRJ (+Bank Dr) or CPJ (-Bank Cr).",
        },
        marking_points=mps,
        misconception_tags=["debit_credit_reversal_crj_cpj"],
        qtype="table_completion",
        journal_type="classification",
    )


def build_40_crj_vs_cpj_structural_comparison_table(rng: random.Random) -> Dict[str, Any]:
    ctx = _biz_ctx(rng)
    headers = ["Feature", "Cash Receipts Journal (CRJ)", "Cash Payments Journal (CPJ)"]
    items = [
        ("Cash direction", "Cash received (inflow)", "Cash paid (outflow)"),
        ("Primary source document example", "Duplicate receipt / CRR", "Cheque counterfoil / EFT slip"),
        ("Effect on General Ledger Bank", "Debit", "Credit"),
        ("Includes Analysis of Receipts column?", "Yes", "No"),
    ]
    rows, cmap, chints, str_rows, mps = [], {}, {}, [], []
    mp_i = 1
    for r_i, (feat, crj_val, cpj_val) in enumerate(items):
        str_rows.append([feat, crj_val, cpj_val])
        # Alternate prefilled column across rows to vary cleanly
        pre_crj = (r_i % 2 == 0)
        c0 = _cell(r_i, 0, feat, editable=False)
        c1 = _cell(r_i, 1, crj_val, editable=not pre_crj)
        c2 = _cell(r_i, 2, cpj_val, editable=pre_crj)
        rows.append([c0, c1, c2])
        target_c, target_v = (c2, cpj_val) if pre_crj else (c1, crj_val)
        cmap[target_c["cell_id"]] = target_v
        chints[target_c["cell_id"]] = f"State the exact contrasting CRJ/CPJ property for '{feat}'."
        mps.append({"id": f"mp_{mp_i}", "desc": f"{feat}: {target_v}", "marks": 1, "editable": True})
        mp_i += 1
    md = _md_table(headers, str_rows)
    return _build_table(
        rng,
        qid_prefix="cpj40",
        subskill="40_crj_vs_cpj_structural_comparison_table",
        title="Side-by-Side Structural Comparison: CRJ vs CPJ",
        prompt=f"Help {ctx['entrepreneur']} complete this comparison chart between {ctx['biz_name']}'s Cash Receipts Journal and Cash Payments Journal.",
        headers=headers,
        rows=rows,
        correct_map=cmap,
        cell_hints=chints,
        worked_solution=f"**CRJ vs CPJ Comparison (4 marks)**\n\n{md}",
        sample_answer=md,
        marks=len(mps),
        hints={
            "tier_1": "CRJ and CPJ are mirror images: one handles cash inflows, the other cash outflows.",
            "tier_2": "Think: Debit vs Credit Bank, Duplicate vs Cheque/EFT, Analysis of Receipts Yes vs No.",
            "tier_3": "Fill the 4 blank cells symmetrically opposite the given side.",
        },
        marking_points=mps,
        misconception_tags=["crj_cpj_mirror_confusion"],
        qtype="table_completion",
        journal_type="classification",
    )


def build_41_combined_crj_cpj_transaction_classification_table(rng: random.Random) -> Dict[str, Any]:
    ctx = _biz_ctx(rng)
    items = [
        (f"Received {_fmt_r(rng.randint(15, 35) * 100)} from walk-in clients (CRR)", "CRJ", "Current income"),
        (f"Paid {ctx['supplier']} {_fmt_r(rng.randint(6, 18) * 100)} by EFT for paper", "CPJ", "Stationery"),
        (f"Tenant paid {_fmt_r(rng.randint(25, 45) * 100)} cash rent (Duplicate receipt)", "CRJ", "Rent income"),
        (f"Cashed cheque for {_fmt_r(rng.randint(14, 28) * 100)} weekly staff pay", "CPJ", "Wages"),
        (f"Owner withdrew {_fmt_r(rng.randint(10, 22) * 100)} for family trip", "CPJ", "Drawings"),
    ]
    rng.shuffle(items)
    headers = ["Business Transaction", "Journal (CRJ or CPJ)", "Contra Ledger Account"]
    rows, cmap, chints, str_rows, mps = [], {}, {}, [], []
    mp_i = 1
    for r_i, (tx, jrn, acct) in enumerate(items):
        str_rows.append([tx, jrn, acct])
        c0 = _cell(r_i, 0, tx, editable=False)
        c1 = _cell(r_i, 1, jrn, editable=True)
        c2 = _cell(r_i, 2, acct, editable=True)
        rows.append([c0, c1, c2])
        cmap[c1["cell_id"]] = jrn
        cmap[c2["cell_id"]] = acct
        chints[c1["cell_id"]] = "Type CRJ (cash in) or CPJ (cash out)."
        chints[c2["cell_id"]] = "Name the matching income, expense, or equity account."
        mps.append({"id": f"mp_{mp_i}", "desc": f"R{r_i + 1} Journal: {jrn}", "marks": 1, "editable": True})
        mps.append({"id": f"mp_{mp_i + 1}", "desc": f"R{r_i + 1} Account: {acct}", "marks": 1, "editable": True})
        mp_i += 2
    md = _md_table(headers, str_rows)
    return _build_table(
        rng,
        qid_prefix="cpj41",
        subskill="41_combined_crj_cpj_transaction_classification_table",
        title="Combined CRJ & CPJ Transaction Routing Table",
        prompt=f"Route each transaction of {ctx['biz_name']} ({ctx['month_full']}) into either 'CRJ' or 'CPJ', and identify its Contra Ledger Account.",
        headers=headers,
        rows=rows,
        correct_map=cmap,
        cell_hints=chints,
        worked_solution=f"**CRJ & CPJ Routing Table (10 marks)**\n\n{md}",
        sample_answer=md,
        marks=len(mps),
        hints={
            "tier_1": "First decide: did cash flow IN (CRJ) or OUT (CPJ)?",
            "tier_2": "Next name the reason: Current income, Rent income, Stationery, Wages, or Drawings.",
            "tier_3": "Fill CRJ/CPJ and exact account names in every row.",
        },
        marking_points=mps,
        misconception_tags=["wrong_journal_selected"],
        qtype="table_completion",
        journal_type="classification",
    )


def build_42_combined_crj_cpj_zippy_traders_worked_audit(rng: random.Random) -> Dict[str, Any]:
    ctx = _biz_ctx(rng)
    cap = rng.randint(8, 15) * 10000
    s1 = rng.randint(35, 65) * 100
    s2 = rng.randint(20, 42) * 100
    rent = rng.randint(25, 48) * 100
    day_same_bank = s2 + rent
    tot_ci = s1 + s2
    tot_sun = cap + rent
    tot_bank = tot_ci + tot_sun
    headers = ["CRJ Metric", "Calculated Rand Amount"]
    items = [
        ("Combined Bank deposit on Day 29 (Services + Rent)", _fmt_r(day_same_bank)),
        ("Total Bank column", _fmt_r(tot_bank)),
        ("Total Current Income column", _fmt_r(tot_ci)),
        ("Total Sundry Accounts column", _fmt_r(tot_sun)),
    ]
    rows, cmap, chints, str_rows, mps = [], {}, {}, [], []
    for r_i, (lbl, val) in enumerate(items):
        str_rows.append([lbl, val])
        c0 = _cell(r_i, 0, lbl, editable=False)
        c1 = _cell(r_i, 1, val, editable=True, is_money=True)
        rows.append([c0, c1])
        cmap[c1["cell_id"]] = val
        chints[c1["cell_id"]] = "Sum the matching receipts accurately in Rands."
        mps.append({"id": f"mp_{r_i + 1}", "desc": f"{lbl}: {val}", "marks": 1, "editable": True})
    md = _md_table(headers, str_rows)
    return _build_table(
        rng,
        qid_prefix="cpj42",
        subskill="42_combined_crj_cpj_zippy_traders_worked_audit",
        title="CRJ Summary Verification (Same-Day Deposit & Cross-Check)",
        prompt=(
            f"{ctx['biz_name']} recorded four entries in {ctx['crj_no']} ({ctx['month_full']}):\n"
            f"- Day 03: {ctx['entrepreneur']} Capital direct deposit {_fmt_r(cap)}\n"
            f"- Day 13: CRR Services rendered {_fmt_r(s1)}\n"
            f"- Day 29: CRR Services rendered {_fmt_r(s2)} AND Receipt Rent income {_fmt_r(rent)} (banked together).\n"
            f"Calculate the four CRJ verification totals below."
        ),
        headers=headers,
        rows=rows,
        correct_map=cmap,
        cell_hints=chints,
        worked_solution=f"**CRJ Totals Verification (4 marks)**\n\n{md}\n\nCheck: `{_fmt_r(tot_ci)} + {_fmt_r(tot_sun)} = {_fmt_r(tot_bank)}`.",
        sample_answer=md,
        marks=4,
        hints={
            "tier_1": "Day 29 sums Services + Rent into one deposit; Capital + Rent make up Sundry.",
            "tier_2": "Verify that Current Income Total + Sundry Total equals Total Bank.",
            "tier_3": f"Day 29 Bank = {_fmt_r(day_same_bank)}; Bank = {_fmt_r(tot_bank)}; CI = {_fmt_r(tot_ci)}; Sundry = {_fmt_r(tot_sun)}.",
        },
        marking_points=mps,
        misconception_tags=["crj_totals_imbalance"],
        qtype="table_completion",
        journal_type="crj_audit",
    )


def build_43_combined_crj_cpj_bank_column_effect_classification(rng: random.Random) -> Dict[str, Any]:
    ctx = _biz_ctx(rng)
    crj_tot = rng.randint(35, 75) * 1000
    cpj_tot = rng.randint(18, 32) * 1000
    return _build_mcq(
        rng,
        qid_prefix="cpj43",
        subskill="43_combined_crj_cpj_bank_column_effect_classification",
        title="How CRJ and CPJ Affect the General Ledger Bank Account",
        prompt=(
            f"In {ctx['month_full']}, {ctx['biz_name']} recorded {_fmt_r(crj_tot)} in its CRJ Bank column and {_fmt_r(cpj_tot)} in its CPJ Bank column. "
            f"How are these two totals posted to the General Ledger Bank account (Asset)?"
        ),
        correct_text=f"Debit Bank with {_fmt_r(crj_tot)} (from CRJ, increasing cash) and Credit Bank with {_fmt_r(cpj_tot)} (from CPJ, decreasing cash)",
        distractors=[
            f"Credit Bank with {_fmt_r(crj_tot)} and Debit Bank with {_fmt_r(cpj_tot)}",
            f"Debit Bank with BOTH {_fmt_r(crj_tot)} and {_fmt_r(cpj_tot)} because both journals have a Bank column",
            f"Post only the difference {_fmt_r(crj_tot - cpj_tot)} to Current Income",
        ],
        explanation=f"Bank is an Asset: receipts from CRJ ({_fmt_r(crj_tot)}) increase Bank on the Debit side, while payments from CPJ ({_fmt_r(cpj_tot)}) decrease Bank on the Credit side.",
        hints={
            "tier_1": "Apply DEAD CLIC to Bank (an Asset account).",
            "tier_2": "CRJ brings money in (+ Debit); CPJ sends money out (- Credit).",
            "tier_3": f"Debit Bank {_fmt_r(crj_tot)}; Credit Bank {_fmt_r(cpj_tot)}.",
        },
        misconception_tags=["cpj_bank_debited_instead_of_credited"],
    )


def build_44_combined_crj_cpj_net_cash_flow_surplus_or_deficit(rng: random.Random) -> Dict[str, Any]:
    ctx = _biz_ctx(rng)
    crj_tot = rng.randint(28, 72) * 1000
    cpj_tot = rng.randint(14, 48) * 1000
    if crj_tot == cpj_tot:
        crj_tot += 4000
    diff = abs(crj_tot - cpj_tot)
    kind = "surplus" if crj_tot > cpj_tot else "shortfall"
    svg = _cpj_crj_flow_svg(ctx["biz_name"], crj_tot, cpj_tot)
    prompt = (
        f"Study the Cash Flow Journals overview diagram for {ctx['biz_name']} in {ctx['month_full']}: "
        f"Total CRJ receipts = {_fmt_r(crj_tot)} and Total CPJ payments = {_fmt_r(cpj_tot)}. "
        f"Calculate the monthly cash flow change and state whether it is a cash surplus or cash shortfall."
    )
    ans = f"{_fmt_r(diff)} {kind}"
    worked = (
        f"Cash Flow Change = CRJ Bank Total - CPJ Bank Total = {_fmt_r(crj_tot)} - {_fmt_r(cpj_tot)} "
        f"({'+' if crj_tot >= cpj_tot else '-'}{_fmt_r(diff)}) -> **{ans}**."
    )
    return _build_short(
        rng,
        qid_prefix="cpj44",
        subskill="44_combined_crj_cpj_net_cash_flow_surplus_or_deficit",
        title="Monthly Cash Surplus or Shortfall (CRJ vs CPJ)",
        prompt=prompt,
        expected_answer=ans,
        worked_solution=worked,
        hints={
            "tier_1": "Compare total cash inflows (CRJ) against total cash outflows (CPJ).",
            "tier_2": "If CRJ > CPJ, the business achieved a cash surplus; if CPJ > CRJ, a cash shortfall.",
            "tier_3": f"Compute |{_fmt_r(crj_tot)} - {_fmt_r(cpj_tot)}| and state '{kind}'.",
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Finds difference {_fmt_r(diff)}", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": f"Identifies {kind}", "marks": 1, "editable": True},
        ],
        misconception_tags=["surplus_vs_shortfall_reversed"],
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    )


def build_45_combined_crj_cpj_closing_bank_balance(rng: random.Random) -> Dict[str, Any]:
    ctx = _biz_ctx(rng)
    open_b = rng.randint(10, 35) * 1000
    crj_tot = rng.randint(25, 60) * 1000
    cpj_tot = rng.randint(12, 30) * 1000
    close_b = open_b + crj_tot - cpj_tot
    ans = _fmt_r(close_b)
    return _build_short(
        rng,
        qid_prefix="cpj45",
        subskill="45_combined_crj_cpj_closing_bank_balance",
        title="Calculating Closing Bank Balance from CRJ & CPJ",
        prompt=(
            f"On 01 {ctx['month_full']}, {ctx['biz_name']} had a favourable Bank balance of {_fmt_r(open_b)}. "
            f"During {ctx['month_short']}, CRJ Total Receipts = {_fmt_r(crj_tot)} and CPJ Total Payments = {_fmt_r(cpj_tot)}. "
            f"Calculate the closing Bank balance at month-end."
        ),
        expected_answer=ans,
        worked_solution=(
            f"Closing Bank = Opening Bank + CRJ Receipts - CPJ Payments\n"
            f"= {_fmt_r(open_b)} + {_fmt_r(crj_tot)} - {_fmt_r(cpj_tot)} = **{ans}**."
        ),
        hints={
            "tier_1": "Start with the opening Bank balance, add cash inflows (CRJ), and subtract cash outflows (CPJ).",
            "tier_2": f"First add {_fmt_r(open_b)} + {_fmt_r(crj_tot)} = {_fmt_r(open_b + crj_tot)}.",
            "tier_3": f"Subtract CPJ ({_fmt_r(cpj_tot)}) -> {ans}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Total cash available = {_fmt_r(open_b + crj_tot)}", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": f"Closing Bank balance = {ans}", "marks": 2, "editable": True},
        ],
        misconception_tags=["subtracted_crj_or_added_cpj"],
    )


def build_46_combined_opening_bank_plus_crj_minus_cpj(rng: random.Random) -> Dict[str, Any]:
    ctx = _biz_ctx(rng)
    open_b = rng.randint(12, 28) * 1000
    crj_tot = rng.randint(22, 54) * 1000
    cpj_tot = rng.randint(14, 34) * 1000
    close_b = open_b + crj_tot - cpj_tot
    svg = _bank_t_account_svg(ctx["biz_name"], ctx["month_full"], open_b, crj_tot, cpj_tot, closing_bal=None)
    ans = _fmt_r(close_b)
    return _build_short(
        rng,
        qid_prefix="cpj46",
        subskill="46_combined_opening_bank_plus_crj_minus_cpj",
        title="Balancing the Bank T-Account from CRJ & CPJ Totals",
        prompt=(
            f"Inspect the General Ledger Bank T-Account diagram below for {ctx['biz_name']} in {ctx['month_full']}: "
            f"Opening Balance b/d = {_fmt_r(open_b)}, CRJ Receipts (Dr) = {_fmt_r(crj_tot)}, CPJ Payments (Cr) = {_fmt_r(cpj_tot)}. "
            f"Calculate the missing Balance c/d (Closing Bank balance)."
        ),
        expected_answer=ans,
        worked_solution=(
            f"1. Debit side total = {_fmt_r(open_b)} + {_fmt_r(crj_tot)} = {_fmt_r(open_b + crj_tot)}.\n"
            f"2. Balance c/d = {_fmt_r(open_b + crj_tot)} - {_fmt_r(cpj_tot)} = **{ans}**."
        ),
        hints={
            "tier_1": "In a T-account, add the larger (Debit) side and subtract the Credit total to find Balance c/d.",
            "tier_2": f"Debit side total = {_fmt_r(open_b + crj_tot)}.",
            "tier_3": f"{_fmt_r(open_b + crj_tot)} - {_fmt_r(cpj_tot)} = {ans}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Debit total = {_fmt_r(open_b + crj_tot)}", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": f"Balance c/d = {ans}", "marks": 2, "editable": True},
        ],
        misconception_tags=["t_account_balancing_error"],
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    )


def build_47_combined_missing_cpj_total_from_bank_reconciliation(rng: random.Random) -> Dict[str, Any]:
    ctx = _biz_ctx(rng)
    open_b = rng.randint(15, 32) * 1000
    crj_tot = rng.randint(28, 56) * 1000
    cpj_tot = rng.randint(16, 36) * 1000
    close_b = open_b + crj_tot - cpj_tot
    ans = _fmt_r(cpj_tot)
    return _build_short(
        rng,
        qid_prefix="cpj47",
        subskill="47_combined_missing_cpj_total_from_bank_reconciliation",
        title="Reconstructing Missing CPJ Total Payments from Bank Balances",
        prompt=(
            f"On 01 {ctx['month_short']}, {ctx['biz_name']} opened with {_fmt_r(open_b)} in Bank. "
            f"Monthly CRJ receipts totalled {_fmt_r(crj_tot)}, and the month-end Bank balance closed at {_fmt_r(close_b)}. "
            f"Calculate the missing CPJ Total Payments for {ctx['month_short']}."
        ),
        expected_answer=ans,
        worked_solution=(
            f"1. Total cash available = {_fmt_r(open_b)} + {_fmt_r(crj_tot)} = {_fmt_r(open_b + crj_tot)}\n"
            f"2. CPJ Total Payments = {_fmt_r(open_b + crj_tot)} - {_fmt_r(close_b)} = **{ans}**."
        ),
        hints={
            "tier_1": "Compare how much total cash was available with how much remained at month-end.",
            "tier_2": "CPJ Payments = (Opening Bank + CRJ Receipts) - Closing Bank.",
            "tier_3": f"{_fmt_r(open_b + crj_tot)} - {_fmt_r(close_b)} = {ans}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Cash available = {_fmt_r(open_b + crj_tot)}", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": f"CPJ Total Payments = {ans}", "marks": 2, "editable": True},
        ],
        misconception_tags=["reverse_bank_reconciliation_error"],
    )


def build_48_combined_bank_overdraft_warning_threshold(rng: random.Random) -> Dict[str, Any]:
    ctx = _biz_ctx(rng)
    open_b = rng.randint(5, 14) * 1000
    crj_tot = rng.randint(12, 24) * 1000
    overdraft = rng.randint(2, 9) * 1000
    cpj_tot = open_b + crj_tot + overdraft
    ans = _fmt_r(overdraft)
    return _build_short(
        rng,
        qid_prefix="cpj48",
        subskill="48_combined_bank_overdraft_warning_threshold",
        title="Detecting a Bank Overdraft When CPJ Exceeds Available Funds",
        prompt=(
            f"{ctx['biz_name']} started {ctx['month_full']} with {_fmt_r(open_b)} in Bank, received {_fmt_r(crj_tot)} in {ctx['crj_no']}, "
            f"and paid out {_fmt_r(cpj_tot)} in {ctx['cpj_no']}. "
            f"Because payments exceeded cash available, the account went into overdraft. Calculate the exact overdraft amount in Rand."
        ),
        expected_answer=ans,
        worked_solution=(
            f"1. Total cash available = {_fmt_r(open_b)} + {_fmt_r(crj_tot)} = {_fmt_r(open_b + crj_tot)}\n"
            f"2. CPJ Payments ({_fmt_r(cpj_tot)}) - Available Cash ({_fmt_r(open_b + crj_tot)}) = **{ans} overdraft**."
        ),
        hints={
            "tier_1": "Add Opening Bank and CRJ Receipts first, then compare against CPJ Payments.",
            "tier_2": f"Available cash = {_fmt_r(open_b + crj_tot)}, which is less than CPJ ({_fmt_r(cpj_tot)}).",
            "tier_3": f"{_fmt_r(cpj_tot)} - {_fmt_r(open_b + crj_tot)} = {ans}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Cash available = {_fmt_r(open_b + crj_tot)}", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": f"Overdraft amount = {ans}", "marks": 2, "editable": True},
        ],
        misconception_tags=["overdraft_calculation_error"],
    )


def build_49_combined_crj_cpj_dual_mini_journal_completion(rng: random.Random) -> Dict[str, Any]:
    ctx = _biz_ctx(rng)
    open_b = rng.randint(15, 30) * 1000
    ci = rng.randint(14, 30) * 1000
    sun_r = rng.randint(6, 18) * 1000
    crj_tot = ci + sun_r
    avail = open_b + crj_tot
    wages = rng.randint(6, 14) * 1000
    sun_p = rng.randint(4, 12) * 1000
    cpj_tot = wages + sun_p
    close_b = avail - cpj_tot
    headers = ["Cash Control Line Item", "Amount (R)"]
    items = [
        ("Opening Bank Balance (01 " + ctx["month_short"] + ")", _fmt_r(open_b), True),
        ("Add: Total CRJ Receipts (Current Income + Sundry)", _fmt_r(crj_tot), False),
        ("Equals: Total Cash Available", _fmt_r(avail), False),
        ("Less: Total CPJ Payments (Wages + Sundry)", _fmt_r(cpj_tot), False),
        ("Closing Bank Balance (Month-End)", _fmt_r(close_b), False),
    ]
    rows, cmap, chints, str_rows, mps = [], {}, {}, [], []
    mp_i = 1
    for r_i, (lbl, val, pre) in enumerate(items):
        str_rows.append([lbl, val])
        c0 = _cell(r_i, 0, lbl, editable=False)
        c1 = _cell(r_i, 1, val, editable=not pre, is_money=True)
        rows.append([c0, c1])
        if not pre:
            cmap[c1["cell_id"]] = val
            chints[c1["cell_id"]] = "Combine the journal figures given in the prompt carefully."
            mps.append({"id": f"mp_{mp_i}", "desc": f"{lbl}: {val}", "marks": 1, "editable": True})
            mp_i += 1
    md = _md_table(headers, str_rows)
    return _build_table(
        rng,
        qid_prefix="cpj49",
        subskill="49_combined_crj_cpj_dual_mini_journal_completion",
        title="Month-End Bank Control Summary (CRJ & CPJ Integration)",
        prompt=(
            f"Complete the Month-End Cash Control Summary table for {ctx['biz_name']} ({ctx['month_full']}):\n"
            f"- Opening Bank = {_fmt_r(open_b)}\n"
            f"- CRJ columns: Current Income {_fmt_r(ci)}, Sundry {_fmt_r(sun_r)}\n"
            f"- CPJ columns: Wages {_fmt_r(wages)}, Sundry {_fmt_r(sun_p)}."
        ),
        headers=headers,
        rows=rows,
        correct_map=cmap,
        cell_hints=chints,
        worked_solution=f"**Month-End Cash Control Summary (4 marks)**\n\n{md}",
        sample_answer=md,
        marks=len(mps),
        hints={
            "tier_1": "First add CRJ columns for Total Receipts, and CPJ columns for Total Payments.",
            "tier_2": "Total Cash Available = Opening Bank + Total CRJ Receipts.",
            "tier_3": f"CRJ = {_fmt_r(crj_tot)}, Avail = {_fmt_r(avail)}, CPJ = {_fmt_r(cpj_tot)}, Closing = {_fmt_r(close_b)}.",
        },
        marking_points=mps,
        misconception_tags=["cash_control_summary_error"],
        qtype="table_completion",
        journal_type="reconciliation",
    )


def build_50_combined_crj_cpj_full_accounting_equation_synthesis(rng: random.Random) -> Dict[str, Any]:
    ctx = _biz_ctx(rng)
    cap = rng.randint(4, 8) * 10000
    svc = rng.randint(25, 55) * 100
    eq = rng.randint(8, 20) * 1000
    wag = rng.randint(15, 35) * 100
    net_a = cap + svc - wag
    net_oe = cap + svc - wag
    return _cpj_eq_table(
        rng,
        qid_prefix="cpj50",
        subskill="50_combined_crj_cpj_full_accounting_equation_synthesis",
        title="Combined CRJ & CPJ Accounting Equation Synthesis",
        prompt=(
            f"Record the overall Accounting Equation effect for all four mixed CRJ/CPJ transactions of {ctx['biz_name']} and complete the COMBINED TOTAL row:\n"
            f"1. CRJ: Owner Capital deposit {_fmt_r(cap)}\n"
            f"2. CRJ: CRR Services rendered {_fmt_r(svc)}\n"
            f"3. CPJ: Bought Equipment for {_fmt_r(eq)} EFT\n"
            f"4. CPJ: Paid staff Wages {_fmt_r(wag)} cash cheque."
        ),
        tx_rows=[
            (f"1. CRJ Capital {_fmt_r(cap)}", f"+{_fmt_r(cap)}", f"+{_fmt_r(cap)}", "0", "Bank rises; Capital increases Equity"),
            (f"2. CRJ Services {_fmt_r(svc)}", f"+{_fmt_r(svc)}", f"+{_fmt_r(svc)}", "0", "Bank rises; Current income increases Equity"),
            (f"3. CPJ Equipment {_fmt_r(eq)}", "0", "0", "0", f"Equipment (+{_fmt_r(eq)}) replaces Bank (-{_fmt_r(eq)})"),
            (f"4. CPJ Wages {_fmt_r(wag)}", f"-{_fmt_r(wag)}", f"-{_fmt_r(wag)}", "0", "Bank drops; Wages expense decreases Equity"),
            ("COMBINED TOTAL", f"+{_fmt_r(net_a)}", f"+{_fmt_r(net_oe)}", "0", f"Check: A (+{_fmt_r(net_a)}) = OE (+{_fmt_r(net_oe)}) + L (0)"),
        ],
        notes=f"Final check: Assets `+{_fmt_r(net_a)}` = Owner's Equity `+{_fmt_r(net_oe)}` + Liabilities `0`.",
        hints={
            "tier_1": "Equipment bought for cash swaps one Asset for another (overall 0); Wages decrease both Assets and Equity.",
            "tier_2": "Sum each column vertically: Capital + Services - Wages.",
            "tier_3": f"Combined Assets = +{_fmt_r(net_a)}, Combined Equity = +{_fmt_r(net_oe)}, Liabilities = 0.",
        },
        misconception_tags=["equipment_treated_as_expense", "equation_imbalance"],
    )


BUILDERS_26_50: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    "26_cpj_two_transaction_starter_journal": build_26_cpj_two_transaction_starter_journal,
    "27_cpj_three_transaction_wages_equipment_drawings": build_27_cpj_three_transaction_wages_equipment_drawings,
    "28_cpj_four_transaction_with_split_cheque": build_28_cpj_four_transaction_with_split_cheque,
    "29_cpj_five_transaction_comprehensive_journal": build_29_cpj_five_transaction_comprehensive_journal,
    "30_cpj_cheque_counterfoil_to_journal_transcription": build_30_cpj_cheque_counterfoil_to_journal_transcription,
    "31_cpj_cross_checking_horizontal_balancing_rule": build_31_cpj_cross_checking_horizontal_balancing_rule,
    "32_cpj_missing_sundry_or_wages_entry_deduction": build_32_cpj_missing_sundry_or_wages_entry_deduction,
    "33_cpj_spot_error_split_cheque_entered_twice_in_bank": build_33_cpj_spot_error_split_cheque_entered_twice_in_bank,
    "34_cpj_spot_error_drawings_recorded_as_wages": build_34_cpj_spot_error_drawings_recorded_as_wages,
    "35_cpj_accounting_equation_expense_payment": build_35_cpj_accounting_equation_expense_payment,
    "36_cpj_accounting_equation_asset_purchase_neutral": build_36_cpj_accounting_equation_asset_purchase_neutral,
    "37_cpj_accounting_equation_owner_drawings": build_37_cpj_accounting_equation_owner_drawings,
    "38_cpj_accounting_equation_loan_repayment": build_38_cpj_accounting_equation_loan_repayment,
    "39_crj_vs_cpj_account1_account2_double_entry_table": build_39_crj_vs_cpj_account1_account2_double_entry_table,
    "40_crj_vs_cpj_structural_comparison_table": build_40_crj_vs_cpj_structural_comparison_table,
    "41_combined_crj_cpj_transaction_classification_table": build_41_combined_crj_cpj_transaction_classification_table,
    "42_combined_crj_cpj_zippy_traders_worked_audit": build_42_combined_crj_cpj_zippy_traders_worked_audit,
    "43_combined_crj_cpj_bank_column_effect_classification": build_43_combined_crj_cpj_bank_column_effect_classification,
    "44_combined_crj_cpj_net_cash_flow_surplus_or_deficit": build_44_combined_crj_cpj_net_cash_flow_surplus_or_deficit,
    "45_combined_crj_cpj_closing_bank_balance": build_45_combined_crj_cpj_closing_bank_balance,
    "46_combined_opening_bank_plus_crj_minus_cpj": build_46_combined_opening_bank_plus_crj_minus_cpj,
    "47_combined_missing_cpj_total_from_bank_reconciliation": build_47_combined_missing_cpj_total_from_bank_reconciliation,
    "48_combined_bank_overdraft_warning_threshold": build_48_combined_bank_overdraft_warning_threshold,
    "49_combined_crj_cpj_dual_mini_journal_completion": build_49_combined_crj_cpj_dual_mini_journal_completion,
    "50_combined_crj_cpj_full_accounting_equation_synthesis": build_50_combined_crj_cpj_full_accounting_equation_synthesis,
}
