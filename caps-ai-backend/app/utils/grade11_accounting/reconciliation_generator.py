from __future__ import annotations

import random
from typing import Any, Dict, List, Optional, Tuple

from ..grade10_accounting.scenario_builder import build_scenario

from ..sole_trader.core import fmt_money as _fmt_money
from ..sole_trader.core import make_id as _make_id
from ..sole_trader.core import round_money as _round_money
from ..sole_trader.journal_question import make_journal as _make_journal
from ..sole_trader.journal_table import build_prefixed_row as _build_prefixed_row
from ..sole_trader.journal_table import journal_editable_cols_by_difficulty as _journal_editable_cols_by_difficulty


def _rng(seed: Optional[int]) -> random.Random:
    r = random.Random()
    if seed is None:
        r.seed()
    else:
        r.seed(int(seed))
    return r


def _money(x: float) -> str:
    return _fmt_money(float(x))


def _brs_headers() -> List[str]:
    # Matches archetype: first column blank/description then Debit, Credit.
    return ["", "Debit", "Credit"]


def _build_brs_row_hints(rows: List[List[Optional[str]]]) -> Dict[str, str]:
    """Build cell_hints for a Bank Reconciliation Statement."""
    hints: Dict[str, str] = {}
    for rix, row in enumerate(rows):
        lbl = str(row[0] or "").strip().lower()
        if "balance as per bank statement" in lbl or "bank statement" in lbl and rix <= 1:
            hints[f"t0_r{rix}_c1"] = "Start with the balance per the bank statement. Favourable = Credit, Unfavourable = Debit."
            hints[f"t0_r{rix}_c2"] = "Start with the balance per the bank statement. Favourable = Credit, Unfavourable = Debit."
        elif "outstanding deposit" in lbl:
            col = "c2"  # deposits go in credit
            hints[f"t0_r{rix}_{col}"] = "Outstanding deposits not yet credited by the bank. Enter in the Credit column."
        elif "outstanding cheque" in lbl or "outstanding eft" in lbl:
            if "no." in lbl or "no " in lbl:
                hints[f"t0_r{rix}_c1"] = "Outstanding cheque/EFT not yet presented for payment. Enter in the Debit column."
            else:
                hints[f"t0_r{rix}_c1"] = "Outstanding cheques/EFTs heading row."
        elif "balance as per bank account" in lbl or "bank account" in lbl:
            hints[f"t0_r{rix}_c1"] = "Balancing figure: the balance per the Bank Account in the General Ledger."
            hints[f"t0_r{rix}_c2"] = "Balancing figure: the balance per the Bank Account in the General Ledger."
        elif "correction" in lbl or "error" in lbl or "incorrectly" in lbl:
            hints[f"t0_r{rix}_c1"] = "Correction of bank error. Debit if bank must reduce, Credit if bank must add."
            hints[f"t0_r{rix}_c2"] = "Correction of bank error. Debit if bank must reduce, Credit if bank must add."
    return hints


def _build_cash_journals_hints(rows: List[List[Optional[str]]]) -> Dict[str, str]:
    """Build cell_hints for Cash Journals totals table."""
    hints: Dict[str, str] = {}
    for rix, row in enumerate(rows):
        lbl = str(row[0] or "").strip().lower()
        if "provisional" in lbl:
            hints[f"t0_r{rix}_c1"] = "Provisional total from the Cash Receipts Journal before adjustments."
            hints[f"t0_r{rix}_c2"] = "Provisional total from the Cash Payments Journal before adjustments."
        elif "rent" in lbl or "deposit" in lbl and "direct" in lbl:
            hints[f"t0_r{rix}_c1"] = "Direct deposit by tenant — add to CRJ (receipts)."
        elif "interest income" in lbl or "interest on fixed" in lbl or "interest on credit" in lbl:
            hints[f"t0_r{rix}_c1"] = "Interest earned — add to CRJ (receipts)."
        elif "bank charges" in lbl or "service fee" in lbl or "cash handling" in lbl:
            hints[f"t0_r{rix}_c2"] = "Bank charges/fees — add to CPJ (payments)."
        elif "insurance" in lbl or "debit order" in lbl:
            hints[f"t0_r{rix}_c2"] = "Debit order paid by bank — add to CPJ (payments)."
        elif "dishonoured" in lbl:
            hints[f"t0_r{rix}_c2"] = "Dishonoured cheque — add to CPJ (payments) to reverse the receipt."
        elif "correct" in lbl and "total" in lbl:
            hints[f"t0_r{rix}_c1"] = "Correct CRJ total = Provisional + all CRJ adjustments."
            hints[f"t0_r{rix}_c2"] = "Correct CPJ total = Provisional + all CPJ adjustments."
    return hints


def _build_creditors_recon_hints(rows: List[List[Optional[str]]], headers: List[str]) -> Dict[str, str]:
    """Build cell_hints for creditors reconciliation tables."""
    hints: Dict[str, str] = {}
    for rix, row in enumerate(rows):
        lbl = str(row[0] or "").strip().lower()
        if "balance" in lbl and rix == 0:
            hints[f"t0_r{rix}_c1"] = "Opening balance per the Creditor's Ledger before adjustments."
            if len(headers) > 2:
                hints[f"t0_r{rix}_c2"] = "Opening balance per the Statement from the supplier."
        elif "discount" in lbl:
            hints[f"t0_r{rix}_c1"] = "Discount error/omission — adjust the affected side (+/-)."
        elif "invoice" in lbl:
            hints[f"t0_r{rix}_c1"] = "Invoice amount difference — adjust the side where the error occurred."
        elif "payment" in lbl:
            col = "c2" if len(headers) > 2 else "c1"
            hints[f"t0_r{rix}_{col}"] = "Payment not yet reflected on the statement — adjust statement side."
        elif "correct" in lbl or "total" in lbl:
            hints[f"t0_r{rix}_c1"] = "Corrected balance — both columns must agree after all adjustments."
            if len(headers) > 2:
                hints[f"t0_r{rix}_c2"] = "Corrected balance — both columns must agree after all adjustments."
    return hints


def _mk_journal(
    *,
    prompt: str,
    journal_type: str,
    headers: List[str],
    values_rows: List[List[Optional[str]]],
    difficulty: str,
    mode: str,
    base_editable_cols: List[int],
    force_editable_cols: Optional[List[int]] = None,
    title_fields: Optional[List[Dict[str, Any]]] = None,
    cell_hints: Optional[Dict[str, str]] = None,
    rubric_map: Optional[Dict[str, Dict[str, Any]]] = None,
    dependency_map: Optional[Dict[str, List[str]]] = None,
) -> Dict[str, Any]:
    diff = str(difficulty or "easy").strip().lower()
    mode_norm = str(mode or "").strip().lower()
    show_answers = mode_norm == "scaffold"

    if force_editable_cols is not None:
        editable_cols = [int(c) for c in force_editable_cols]
    else:
        editable_cols = _journal_editable_cols_by_difficulty(
            difficulty=diff,
            base_editable_cols=base_editable_cols,
            total_cols=len(headers),
            mode=mode_norm,
        )

    rows: List[List[Dict[str, Any]]] = []
    correct_map: Dict[str, Any] = {}

    for rix, vals in enumerate(values_rows):
        editable_set = set(int(c) for c in editable_cols)
        display = [
            ("" if int(cix) in editable_set else ("" if v0 is None else str(v0)))
            for cix, v0 in enumerate(vals)
        ]
        rows.append(_build_prefixed_row(table_index=0, row_index=rix, values=display, editable_cols=editable_cols))
        for cix, v0 in enumerate(vals):
            correct_map[f"t0_r{int(rix)}_c{int(cix)}"] = "" if v0 is None else str(v0)

    out = _make_journal(
        prompt=prompt,
        journal_type=journal_type,
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        guidelines=[
            "Enter amounts in the correct column (Debit/Credit).",
            "Outstanding deposits increase the reconciliation (Credit column).",
            "Outstanding cheques decrease the reconciliation (Debit column).",
        ],
        table_variant="grade_project",
        title_fields=title_fields,
        cell_hints=cell_hints if mode_norm == "scaffold" and cell_hints else None,
        rubric_map=rubric_map,
        dependency_map=dependency_map,
    )
    out["id"] = _make_id("acct11_reconciliation")
    return out


def _make_bundle(*, prompt: str, parts: List[Dict[str, Any]], archetype_key: str = "") -> Dict[str, Any]:
    out: Dict[str, Any] = {
        "id": _make_id("acct11_reconciliation_bundle"),
        "question_type": "bundle",
        "prompt": prompt,
        "parts": parts,
    }
    if archetype_key:
        out["meta"] = {"archetype_key": archetype_key}
    return out


def _make_typed(*, prompt: str, sample_answer: str, mode: str, archetype_key: str = "") -> Dict[str, Any]:
    out: Dict[str, Any] = {
        "id": _make_id("acct11_reconciliation_typed"),
        "question_type": "typed",
        "prompt": prompt,
        "expected_answer_type": "text",
        "guidelines": [f"Sample expected answer: {sample_answer}"],
    }
    meta: Dict[str, Any] = {}
    if archetype_key:
        meta["archetype_key"] = archetype_key
    if meta:
        out["meta"] = meta
    if str(mode or "").strip().lower() == "scaffold":
        out["sample_answer"] = sample_answer
    return out


def _make_bank_reconciliation_statement(*, r: random.Random, difficulty: str, mode: str) -> Dict[str, Any]:
    scenario = build_scenario(seed=r.randint(1, 1000))
    business = scenario["business"]
    day = int(r.choice([30, 31]))
    month = r.choice(["March", "May", "June", "August", "November"])
    year = int(r.choice([20, 21, 22, 23]))

    # Choose whether the bank statement balance is favourable (credit) or unfavourable (debit)
    bank_statement_favourable = bool(r.choice([True, True, False]))

    bank_statement_amount = float(r.choice([1254, 3450, 4383, 9720, 15400, 27500]))

    outstanding_deposits = [
        float(r.choice([1200, 1500, 1553, 9700, 23600, 64200])),
    ]
    if bool(r.choice([True, False])):
        outstanding_deposits.append(float(r.choice([1500, 2700, 8400])))

    cheques: List[Tuple[str, float]] = []
    for no in r.sample(["432", "778", "792", "798", "801", "354", "415"], k=3):
        amt = float(r.choice([250, 540, 1200, 2400, 5600, 6000, 2800]))
        cheques.append((no, amt))

    post_dated_cheque = 0
    if bool(r.choice([True, False])):
        post_dated_cheque = float(r.choice([800, 1400, 3200]))
        # We issued a post-dated cheque which is not yet due, so it's outstanding
        cheques.append(("PDC", post_dated_cheque))

    total_deposits = _round_money(sum(outstanding_deposits))
    total_cheques = _round_money(sum(a for _, a in cheques))

    # Reconciliation logic (consistent with archetype layout):
    # Start with bank statement balance, add outstanding deposits (credit), subtract outstanding cheques (debit)
    if bank_statement_favourable:
        start_credit = bank_statement_amount
        start_debit = 0.0
    else:
        start_debit = bank_statement_amount
        start_credit = 0.0

    # Final balance should end as the Bank account balance (could be unfavourable)
    # Compute as (credit - debit) after adjustments.
    net = _round_money((start_credit + total_deposits) - (start_debit + total_cheques))

    bank_account_unfavourable = net < 0
    bank_account_amount = abs(net)

    headers = _brs_headers()

    rows: List[List[Optional[str]]] = []
    rows.append([f"BANK RECONCILIATION STATEMENT of {business} as at {day} {month} {year}.2", "", ""])

    # Statement balance row
    if bank_statement_favourable:
        rows.append(["Favourable balance as per bank statement", "", _money(bank_statement_amount)])
    else:
        rows.append(["Unfavourable balance as per bank statement", _money(bank_statement_amount), ""])

    # Outstanding deposits
    rows.append(["Outstanding deposits", "", _money(total_deposits)])
    for i, dep in enumerate(outstanding_deposits, start=1):
        rows.append([f"  Deposit {i}", "", _money(dep)])

    # Outstanding cheques
    rows.append(["Outstanding cheques:", "", ""])
    for no, amt in cheques:
        rows.append([f"  No. {no}", _money(amt), ""])

    # Bank account balance
    if bank_account_unfavourable:
        rows.append(["Unfavourable balance as per Bank account", "", _money(bank_account_amount)])
        # In archetypes, this is often placed in Credit column as a plug; keep the same convention
        # (the total line balances debit and credit)
    else:
        rows.append(["Favourable balance as per Bank account", "", _money(bank_account_amount)])

    # Totals
    # Totals should be equal debit/credit.
    debit_total = _round_money(start_debit + total_cheques + (bank_account_amount if bank_statement_favourable else 0.0))
    credit_total = _round_money(start_credit + total_deposits + (bank_account_amount if not bank_statement_favourable else 0.0))

    # If totals drift due to our convention choices, force totals to max.
    tot = _money(max(debit_total, credit_total))
    rows.append(["", tot, tot])

    # Editable: amounts columns only
    cell_hints = _build_brs_row_hints(rows)

    info_lines = []
    if bank_statement_favourable:
        info_lines.append(f"- Favourable balance as per bank statement: {_money(bank_statement_amount)}")
    else:
        info_lines.append(f"- Unfavourable balance as per bank statement: {_money(bank_statement_amount)}")
    
    info_lines.append("- Outstanding deposits:")
    for i, dep in enumerate(outstanding_deposits, start=1):
        info_lines.append(f"  * Deposit {i}: {_money(dep)}")
    
    info_lines.append("- Outstanding cheques:")
    for no, amt in cheques:
        info_lines.append(f"  * Cheque No. {no}: {_money(amt)}")
        
    if bank_account_unfavourable:
        info_lines.append(f"- Unfavourable balance as per Bank account: {_money(bank_account_amount)}")
    else:
        info_lines.append(f"- Favourable balance as per Bank account: {_money(bank_account_amount)}")

    prompt = f"""{business}

#### REQUIRED:
Prepare the Bank Reconciliation Statement as at {day} {month} {year}.2.

#### INFORMATION:
{chr(10).join(info_lines)}"""

    q = _mk_journal(
        prompt=prompt,
        journal_type="bank_reconciliation_statement",
        headers=headers,
        values_rows=rows,
        difficulty=difficulty,
        mode=mode,
        base_editable_cols=[1, 2],
        title_fields=[
            {"label": "", "value": ""},
        ],
        cell_hints=cell_hints,
    )
    q["meta"] = {"archetype_key": "g11_recon_bank_reconciliation_statement_only"}
    return q


def _make_bank_reconciliation_full_workflow_bundle(*, r: random.Random, difficulty: str, mode: str) -> Dict[str, Any]:
    # Mirrors common exam flow: update totals -> bank account -> bank reconciliation statement.
    scenario = build_scenario(seed=r.randint(1, 1000))
    business = scenario["business"]
    day = int(r.choice([30, 31]))
    month = r.choice(["March", "May", "June", "August", "November"])
    year = int(r.choice([21, 22, 23]))

    # Provisional totals.
    crj_prov = float(r.choice([20420, 25670, 84300, 104000, 117600, 477400]))
    cpj_prov = float(r.choice([29070, 19800, 100950, 102000, 126200, 413500]))

    # Adjustments (simple but faithful): direct deposit, bank charges, interest, debit order, dishonoured cheque.
    adj_crj: List[Tuple[str, float]] = []
    adj_cpj: List[Tuple[str, float]] = []

    direct_deposit_rent = float(r.choice([0, 800, 3200, 14200, 17400]))
    if direct_deposit_rent:
        adj_crj.append(("Direct deposit: Rent income", direct_deposit_rent))

    interest_income = float(r.choice([0, 52, 400, 630, 3900]))
    if interest_income:
        adj_crj.append(("Interest income", interest_income))

    bank_charges = float(r.choice([179, 260, 378, 557, 1140]))
    adj_cpj.append(("Bank charges", bank_charges))

    debit_order_insurance = float(r.choice([150, 1860, 8900, 10600]))
    adj_cpj.append(("Debit order: Insurance", debit_order_insurance))

    dishonoured_cheque = float(r.choice([0, 900, 1870, 3600]))
    if dishonoured_cheque:
        adj_cpj.append(("Dishonoured cheque", dishonoured_cheque))

    # Error correction in Cash Journals
    error_correction_amount = 0
    if bool(r.choice([True, False])):
        error_type = r.choice(["undercast_crj", "overcast_cpj", "cheque_recorded_twice"])
        if error_type == "undercast_crj":
            error_correction_amount = float(r.choice([100, 250, 500]))
            adj_crj.append(("Error: CRJ undercast", error_correction_amount))
        elif error_type == "overcast_cpj":
            error_correction_amount = float(r.choice([300, 450, 700]))
            # To correct overcast CPJ, we effectively subtract from CPJ or add to CRJ. We will add to CRJ.
            adj_crj.append(("Correction: CPJ overcast", error_correction_amount))
        elif error_type == "cheque_recorded_twice":
            error_correction_amount = float(r.choice([120, 340, 560]))
            adj_crj.append(("Correction: Cheque recorded twice in CPJ", error_correction_amount))

    crj_total = _round_money(crj_prov + sum(v for _, v in adj_crj))
    cpj_total = _round_money(cpj_prov + sum(v for _, v in adj_cpj))

    # Part 1: Totals table.
    totals_headers = ["", "CRJ", "CPJ"]
    totals_rows: List[List[Optional[str]]] = [["Provisional totals", _money(crj_prov), _money(cpj_prov)]]
    for label, val in adj_crj:
        totals_rows.append([label, _money(val), ""])
    for label, val in adj_cpj:
        totals_rows.append([label, "", _money(val)])
    totals_rows.append(["Correct totals", _money(crj_total), _money(cpj_total)])

    info_lines = [
        f"- Provisional CRJ total: {_money(crj_prov)}",
        f"- Provisional CPJ total: {_money(cpj_prov)}",
        "Additional items from the bank statement and errors not yet recorded:"
    ]
    if direct_deposit_rent: info_lines.append(f"  * Direct deposit for rent: {_money(direct_deposit_rent)}")
    if interest_income: info_lines.append(f"  * Interest income: {_money(interest_income)}")
    if bank_charges: info_lines.append(f"  * Bank charges: {_money(bank_charges)}")
    if debit_order_insurance: info_lines.append(f"  * Debit order for insurance: {_money(debit_order_insurance)}")
    if dishonoured_cheque: info_lines.append(f"  * Dishonoured cheque: {_money(dishonoured_cheque)}")
    
    if error_correction_amount > 0:
        if "undercast" in adj_crj[-1][0]:
            info_lines.append(f"  * Error: The CRJ was undercast by {_money(error_correction_amount)}.")
        elif "overcast" in adj_crj[-1][0]:
            info_lines.append(f"  * Error: The CPJ was overcast by {_money(error_correction_amount)}.")
        elif "twice" in adj_crj[-1][0]:
            info_lines.append(f"  * Error: A cheque for {_money(error_correction_amount)} was recorded twice in the CPJ.")

    totals_prompt = f"""{business}

#### REQUIRED:
Calculate the correct totals for the Cash Receipts Journal and Cash Payments Journal for {month} {year}.2.

#### INFORMATION:
{chr(10).join(info_lines)}"""

    part_totals = _mk_journal(
        prompt=totals_prompt,
        journal_type="cash_journals_totals",
        headers=totals_headers,
        values_rows=totals_rows,
        difficulty=difficulty,
        mode=mode,
        base_editable_cols=[1, 2],
        cell_hints=_build_cash_journals_hints(totals_rows),
    )
    part_totals["meta"] = {"archetype_key": "g11_recon_bank_cash_journals_totals"}

    # Part 2: Bank account.
    bank_headers = ["Date", "Details", "Fol.", "Amount", "Date", "Details", "Fol.", "Amount"]
    opening_balance = float(r.choice([6912, 15600, 299600, 4383]))
    # Debit side: total receipts
    # Credit side: total payments
    closing_balance = _round_money(opening_balance + crj_total - cpj_total)
    bank_rows: List[List[Optional[str]]] = [
        [
            f"{year}.2 {month} {day}",
            "Total receipts",
            "CRJ",
            _money(crj_total),
            f"{year}.2 {month} {day}",
            "Total payments",
            "CPJ",
            _money(cpj_total),
        ],
        [
            "",
            "Balance",
            "c/d",
            _money(closing_balance),
            "",
            "",
            "",
            "",
        ],
    ]

    bank_prompt = f"""{business}

#### REQUIRED:
Prepare the Bank Account in the General Ledger for {month} {year}.2.

#### INFORMATION:
Use the corrected totals from the cash journals."""

    bank_hints: Dict[str, str] = {
        "t0_r0_c3": "Total receipts from the corrected CRJ total.",
        "t0_r0_c7": "Total payments from the corrected CPJ total.",
        "t0_r1_c3": "Closing balance = Opening balance + Total receipts – Total payments.",
    }
    part_bank = _mk_journal(
        prompt=bank_prompt,
        journal_type="bank_account",
        headers=bank_headers,
        values_rows=bank_rows,
        difficulty=difficulty,
        mode=mode,
        base_editable_cols=[3, 7],
        force_editable_cols=[3, 7],
        cell_hints=bank_hints,
    )
    part_bank["meta"] = {"archetype_key": "g11_recon_bank_account"}

    # Part 3: Bank reconciliation statement (standalone archetype builder for consistency).
    brs_part = _make_bank_reconciliation_statement(r=r, difficulty=difficulty, mode=mode)
    brs_part["meta"] = {"archetype_key": "g11_recon_bank_reconciliation_statement_in_bundle"}

    return _make_bundle(
        prompt=f"""{business}

Complete the following parts for {month} {year}.2.""",
        parts=[part_totals, part_bank, brs_part],
        archetype_key="g11_recon_bank_full_workflow_bundle",
    )


def _make_creditors_reconciliation_statement_and_control_bundle(*, r: random.Random, difficulty: str, mode: str) -> Dict[str, Any]:
    # Mirrors Q2 pattern: creditors reconciliation statement + creditors control account.
    scenario = build_scenario(seed=r.randint(1, 1000))
    business = scenario["business"]
    supplier = r.choice(["Phindile Suppliers", "Sikhosana Equipment", "Mabutho Suppliers"])
    month = r.choice(["January", "March", "April"])
    year = int(r.choice([21, 22, 23]))

    bal_statement = float(r.choice([9519, 26070, 67500, 120000]))
    # Typical recon adjustments (all applied to statement to reach ledger) in doc.
    disc_omitted = float(r.choice([960, 200, 500]))
    invoice_wrong_account = float(r.choice([8700, 3380, 1600]))

    correct_balance = _round_money(bal_statement - disc_omitted + invoice_wrong_account)

    # Part 1: reconciliation statement (layout style).
    rs_headers = ["", "Amount"]
    rs_rows: List[List[Optional[str]]] = [
        ["Balance as per statement", _money(bal_statement)],
        ["Less: Discount omitted", _money(disc_omitted)],
        ["Add: Invoice recorded on another account", _money(invoice_wrong_account)],
        ["Correct balance as per Creditors Ledger", _money(correct_balance)],
    ]

    info_lines = [
        f"- Balance as per statement from {supplier}: {_money(bal_statement)}",
        f"- Discount omitted from the statement: {_money(disc_omitted)}",
        f"- Invoice recorded on another account by {supplier} in error: {_money(invoice_wrong_account)}",
        f"- Correct balance as per Creditor's Ledger: {_money(correct_balance)}"
    ]
    rs_prompt = f"""{business}

#### REQUIRED:
Prepare the Creditors Reconciliation Statement for {month} {year}.2 after comparing the creditor's ledger with the statement received from {supplier}.

#### INFORMATION:
{chr(10).join(info_lines)}"""

    rs_hints: Dict[str, str] = {
        "t0_r0_c1": "Start with the balance per the statement received from the supplier.",
        "t0_r1_c1": "Deduct discount that was omitted from the statement.",
        "t0_r2_c1": "Add invoice that was recorded on another debtor's account by the supplier.",
        "t0_r3_c1": "Correct balance must equal the Creditor's Ledger balance after adjustments.",
    }
    part_rs = _mk_journal(
        prompt=rs_prompt,
        journal_type="creditors_reconciliation_statement",
        headers=rs_headers,
        values_rows=rs_rows,
        difficulty=difficulty,
        mode=mode,
        base_editable_cols=[1],
        cell_hints=rs_hints,
    )
    part_rs["meta"] = {"archetype_key": "g11_recon_creditors_reconciliation_statement"}

    # Part 2: creditors control account (simplified T-account).
    cc_headers = ["Date", "Details", "Fol.", "Amount", "Date", "Details", "Fol.", "Amount"]
    opening = float(r.choice([20560, 135000, 56500]))
    payments = float(r.choice([17000, 67500, 5000]))
    purchases = _round_money(opening + correct_balance + float(r.choice([120, 0, 500])) - payments)
    closing = _round_money(opening + purchases - payments)

    cc_rows: List[List[Optional[str]]] = [
        [f"{year}.2 {month}", "Bank / EFT", "CPJ", _money(payments), f"{year}.2 {month}", "Balance", "b/d", _money(opening)],
        ["", "Balance", "c/d", _money(closing), "", "Sundry purchases", "CJ", _money(purchases)],
    ]

    info_lines_cc = [
        f"- Opening balance brought down: {_money(opening)}",
        f"- Total payments (Bank/EFT) during the month: {_money(payments)}",
        f"- Total credit purchases (Sundry purchases) during the month: {_money(purchases)}",
        f"- Closing balance to be carried down: {_money(closing)}"
    ]
    cc_prompt = f"""{business}

#### REQUIRED:
Draw up the Creditors Control account in the General Ledger.

#### INFORMATION:
{chr(10).join(info_lines_cc)}"""

    cc_hints: Dict[str, str] = {
        "t0_r0_c3": "Total payments (Bank/EFT + discount) to the creditor during the period.",
        "t0_r0_c7": "Opening balance brought forward from the previous period.",
        "t0_r1_c3": "Closing balance carried down — balancing figure.",
        "t0_r1_c7": "Total purchases on credit from the supplier during the period.",
    }
    part_cc = _mk_journal(
        prompt=cc_prompt,
        journal_type="creditors_control",
        headers=cc_headers,
        values_rows=cc_rows,
        difficulty=difficulty,
        mode=mode,
        base_editable_cols=[3, 7],
        force_editable_cols=[3, 7],
        cell_hints=cc_hints,
    )
    part_cc["meta"] = {"archetype_key": "g11_recon_creditors_control_account"}

    return _make_bundle(
        prompt=f"""{business}

Complete the following parts to reconcile {supplier} for {month} {year}.2.""",
        parts=[part_rs, part_cc],
        archetype_key="g11_recon_creditors_recon_statement_and_control_bundle",
    )


def _make_bank_internal_control_typed(*, r: random.Random, mode: str) -> Dict[str, Any]:
    # Mirrors Q10.4/Q11.4: identify a problem + suggest internal controls.
    scenario = build_scenario(seed=r.randint(1, 1000))
    business = scenario["business"]
    prompt = f"""{business}

#### REQUIRED:
Explain TWO different internal control measures that the owner can implement, based on the problems identified in the information provided.

#### INFORMATION:
The following problems were identified during the reconciliation process:
1. Cash deposits were not verified and a shortfall had to be written off.
2. Duplicate charges appeared on the bank statement.

Focus on preventing these specific errors and fraud."""

    sample = (
        "Problem: Cash deposits were not verified and a shortfall had to be written off.\n"
        "Control measure 1: Separate duties (one person prepares deposit, another verifies/authorises).\n"
        "Control measure 2: Use pre-numbered deposit slips and reconcile cash register totals to bank deposits daily.\n\n"
        "Problem: Duplicate charges appeared on the bank statement.\n"
        "Control measure: Review bank statement monthly and follow up immediately with the bank; keep supporting documents for all debit orders/EFTs."
    )

    return _make_typed(
        prompt=prompt,
        sample_answer=sample,
        mode=mode,
        archetype_key="g11_recon_internal_control_typed",
    )


def _make_creditors_reconciliation_plus_minus(*, r: random.Random, difficulty: str, mode: str) -> Dict[str, Any]:
    # Mirrors Q4/Q6/Q7 style: effect table to reconcile creditor ledger vs statement.
    scenario = build_scenario(seed=r.randint(1, 1000))
    business = scenario["business"]
    supplier = r.choice(["Big Music", "Kajee Meats", "Vuyi Suppliers"])
    month = r.choice(["May", "April", "October", "March"])
    year = int(r.choice([21, 22, 23]))

    ledger_bal = float(r.choice([42794, 56500, 41680, 135000]))
    stmt_bal = float(r.choice([46820, 67500, 26070, 120000]))

    # A few common recon items.
    items: List[Tuple[str, float, float]] = []  # (label, ledger_effect, stmt_effect)
    # discount recorded/omitted
    disc = float(r.choice([67, 160, 200, 500]))
    items.append(("Discount error/omission", -disc, 0.0))
    # invoice misrecorded
    inv_diff = float(r.choice([110, 4500, 9000]))
    items.append(("Invoice amount incorrect", inv_diff, 0.0))
    # invoice omitted on statement
    inv_omit = float(r.choice([1600, 2500, 3380]))
    items.append(("Invoice omitted on statement", 0.0, inv_omit))
    # payment in ledger not on statement
    pay = float(r.choice([2840, 4000, 5000]))
    items.append(("Payment not yet on statement", 0.0, -pay))

    corr_ledger = _round_money(ledger_bal + sum(a for _, a, _ in items))
    corr_stmt = _round_money(stmt_bal + sum(b for _, _, b in items))
    # Force equality by adjusting last item on statement.
    diff = _round_money(corr_ledger - corr_stmt)
    if items:
        label, le, se = items[-1]
        items[-1] = (label, le, _round_money(se + diff))
    corr_stmt = _round_money(stmt_bal + sum(b for _, _, b in items))

    headers = ["No.", "Creditor's Ledger", "Statement"]
    rows: List[List[Optional[str]]] = [["Balance", _money(ledger_bal), _money(stmt_bal)]]
    for i, (label, le, se) in enumerate(items, start=1):
        def _fmt(x: float) -> str:
            if x == 0:
                return ""
            sign = "+" if x > 0 else "-"
            return f"{sign}{_money(abs(x))}"

        rows.append([f"{i}. {label}", _fmt(le), _fmt(se)])
    rows.append(["Correct totals", _money(corr_ledger), _money(corr_stmt)])

    info_lines = [
        f"- Creditor's Ledger balance for {supplier}: {_money(ledger_bal)}",
        f"- Statement balance received from {supplier}: {_money(stmt_bal)}",
        "Errors and omissions identified:"
    ]
    for i, (label, le, se) in enumerate(items, start=1):
        # We need to construct a human-readable reason for the effect
        amount = max(abs(le), abs(se))
        if "Discount" in label:
            desc = f"Discount of {_money(amount)} was omitted."
        elif "Invoice amount" in label:
            desc = f"An invoice was recorded incorrectly, causing a difference of {_money(amount)}."
        elif "Invoice omitted" in label:
            desc = f"An invoice for {_money(amount)} was omitted from the statement."
        elif "Payment not yet" in label:
            desc = f"A payment of {_money(amount)} is not yet reflected on the statement."
        else:
            desc = f"{label} for {_money(amount)}."
        info_lines.append(f"  {i}. {desc}")

    prompt = f"""{business}

#### REQUIRED:
Complete the creditors reconciliation effect table to reconcile the Creditor's Ledger balance of {supplier} with the statement received for {month} {year}.2.

#### INFORMATION:
{chr(10).join(info_lines)}

Indicate an increase (+) or decrease (-) for each error/omission and calculate the corrected totals."""

    q = _mk_journal(
        prompt=prompt,
        journal_type="creditors_reconciliation_effects",
        headers=headers,
        values_rows=rows,
        difficulty=difficulty,
        mode=mode,
        base_editable_cols=[1, 2],
        cell_hints=_build_creditors_recon_hints(rows, headers),
    )
    q["meta"] = {"archetype_key": "g11_recon_creditors_plus_minus_table"}
    return q


def _make_bank_recon_classification_matrix(*, r: random.Random, difficulty: str, mode: str) -> Dict[str, Any]:
    # Mirrors Exercise 3: classify each transaction (journal+GL, bank account Dr/Cr, BRS Dr/Cr, or no entry).
    headers = [
        "No.",
        "Details in subsidiary journal",
        "Amount",
        "Bank account (Dr)",
        "Bank account (Cr)",
        "BRS (Dr)",
        "BRS (Cr)",
        "No entry",
    ]

    txs = [
        ("1", "Outstanding deposit", 9800.0, "", "", "", "X", ""),
        ("2", "Direct deposit: Rent income", 3200.0, "X", "", "", "", ""),
        ("3", "Debit order: Cell phone", 685.0, "", "X", "", "", ""),
        ("4", "Dishonoured cheque", 900.0, "", "X", "", "", ""),
        ("5", "Post-dated cheque received", 764.0, "", "", "", "", "X"),
    ]

    rows: List[List[Optional[str]]] = []
    for no, details, amt, bdr, bcr, rdr, rcr, noent in txs:
        rows.append([no, details, _money(amt), bdr, bcr, rdr, rcr, noent])

    info_lines = [
        "- Transaction 1: Outstanding deposit of R9 800.",
        "- Transaction 2: Direct deposit for rent income of R3 200.",
        "- Transaction 3: Debit order for cell phone of R685.",
        "- Transaction 4: Dishonoured cheque of R900.",
        "- Transaction 5: Post-dated cheque received of R764.",
    ]

    prompt = f"""Reconciliation

#### REQUIRED:
Analyse each transaction and indicate where it must be recorded (cash journals / Bank account / Bank reconciliation statement), or whether no entry is required.

#### INFORMATION:
The following transactions occurred:
{chr(10).join(info_lines)}

Use an "X" in the appropriate column."""

    class_hints: Dict[str, str] = {}
    for rix, row in enumerate(rows):
        det = str(row[1] or "").lower()
        
        # Add generic hints to all editable columns for the row to prevent giving away the answer
        class_hints[f"t0_r{rix}_c3"] = "Bank account (Dr): Used to record money received by the business (from Cash Receipts Journal)."
        class_hints[f"t0_r{rix}_c4"] = "Bank account (Cr): Used to record money paid by the business (from Cash Payments Journal)."
        class_hints[f"t0_r{rix}_c5"] = "BRS (Dr): Used for reconciling items like unpresented cheques or bank errors to debit."
        class_hints[f"t0_r{rix}_c6"] = "BRS (Cr): Used for reconciling items like outstanding deposits or bank errors to credit."
        class_hints[f"t0_r{rix}_c7"] = "No entry: Used when the transaction does not affect the bank account or bank reconciliation statement yet."
        
        # Optionally we could inject specific row-level context into the hints, 
        # but generic column definitions force the student to evaluate.

    q = _mk_journal(
        prompt=prompt,
        journal_type="bank_recon_classification",
        headers=headers,
        values_rows=rows,
        difficulty=difficulty,
        mode=mode,
        base_editable_cols=list(range(len(headers))),
        force_editable_cols=[3, 4, 5, 6, 7],
        cell_hints=class_hints,
    )
    q["meta"] = {"archetype_key": "g11_recon_bank_classification_matrix"}
    return q


def generate_questions(
    *,
    subskill: str = "mixed",
    difficulty: str = "easy",
    question_type: str = "mixed",
    count: int = 1,
    seed: Optional[int] = None,
    mode: str = "",
) -> List[Dict[str, Any]]:
    r = _rng(seed)

    n = int(count) if isinstance(count, int) else 1
    if n < 1:
        n = 1
    if n > 20:
        n = 20

    subskill_norm = str(subskill or "mixed").strip().lower()
    qtype_norm = str(question_type or "mixed").strip().lower()

    builders: List[Any] = [
        lambda: _make_bank_reconciliation_statement(r=r, difficulty=difficulty, mode=mode),
        lambda: _make_bank_reconciliation_full_workflow_bundle(r=r, difficulty=difficulty, mode=mode),
        lambda: _make_creditors_reconciliation_plus_minus(r=r, difficulty=difficulty, mode=mode),
        lambda: _make_bank_recon_classification_matrix(r=r, difficulty=difficulty, mode=mode),
        lambda: _make_creditors_reconciliation_statement_and_control_bundle(r=r, difficulty=difficulty, mode=mode),
        lambda: _make_bank_internal_control_typed(r=r, mode=mode),
    ]

    # Subskill routing
    if subskill_norm in {"bank", "bank-recon", "bank_recon", "bank_reconciliation", "brs"}:
        builders = [builders[0], builders[1], builders[3], builders[5]]
    elif subskill_norm in {"creditors", "creditors-recon", "creditors_recon", "creditors_reconciliation"}:
        builders = [builders[2], builders[4]]
    elif subskill_norm in {"classification", "matrix", "analyse", "analysis"}:
        builders = [builders[3]]
    elif subskill_norm in {"control", "internal-control", "internal_control", "ethics"}:
        builders = [builders[5]]

    out: List[Dict[str, Any]] = []
    for _ in range(n):
        q = r.choice(builders)()
        if qtype_norm != "mixed" and str(q.get("question_type") or "").strip().lower() != qtype_norm:
            # Retry once; if still mismatch, keep anyway.
            q2 = r.choice(builders)()
            if str(q2.get("question_type") or "").strip().lower() == qtype_norm:
                q = q2
        out.append(q)

    return out
