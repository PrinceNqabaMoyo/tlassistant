"""
reconciliation_generator.py — Grade 12 Term 2
===============================================
Bank, Debtors & Creditors Reconciliations question generator.

Archetype classes covered:
  1. Bank reconciliation statement (BRS)
  2. CPJ/CRJ corrections
  3. Outstanding cheques
  4. Outstanding deposits
  5. Dishonoured/RD cheques
  6. Post-dated cheques
  7. Stale cheques (>6 months)
  8. Lost cheque replacement
  9. Bank errors on BRS
 10. Business errors (under/overcast)
 11. Debtors control reconciliation
 12. Debtors list corrections
 13. Creditors reconciliation
 14. Over/undercast journal corrections
 15. Age analysis interpretation
 16. Internal control
"""
from __future__ import annotations

import random
import uuid
from typing import Any, Dict, List, Optional


def _rng(seed: Optional[int]) -> random.Random:
    r = random.Random()
    r.seed() if seed is None else r.seed(int(seed))
    return r


def _make_id(prefix: str) -> str:
    return f"{prefix}_{uuid.uuid4().hex[:12]}"


def _rm(x: float) -> float:
    return round(float(x) + 1e-9, 2)


def _money(x: float) -> str:
    return f"R {x:,.2f}"


_BUSINESSES = [
    "Crystal Traders", "Zenith Stores", "Atlas Suppliers",
    "Beacon Trading", "Summit Wholesale", "Delta Electronics",
    "Horizon Logistics", "Pinnacle Motors", "Sterling Supplies",
    "Vanguard Retailers",
]

_DEBTOR_NAMES = [
    "R Jansen", "S Wonder", "P Collins", "M Carey", "C Dion",
    "T Naidoo", "B Zulu", "K Motaung", "L Govender", "J Nel",
]


def _make_mcq(*, prompt, options, correct_index, explanation):
    return {
        "id": _make_id("acct12_rec_mcq"), "question_type": "mcq",
        "prompt": prompt, "options": options,
        "correct_index": int(correct_index), "explanation": explanation,
        "expected_answer_type": "mcq", "marks": 2,
        "guidelines": [explanation], "visual_aid_key": "reconciliation_t2",
    }


def _make_typed(*, prompt, sample_answer, grading_rubric=None):
    gr = grading_rubric or []
    return {
        "id": _make_id("acct12_rec_typed"), "question_type": "typed",
        "prompt": prompt, "sample_answer": sample_answer,
        "expected_answer_type": "text", "grading_rubric": gr,
        "marks": 4 if len(gr) >= 2 else 2,
        "guidelines": [f"Include: {', '.join(gr)}"] if gr else [],
        "visual_aid_key": "reconciliation_t2",
    }


def _make_calc(*, prompt, correct_answer, unit="R", working_formula=""):
    return {
        "id": _make_id("acct12_rec_calc"), "question_type": "calc",
        "prompt": prompt, "correct_value": correct_answer,
        "correct_answer": correct_answer, "unit": unit,
        "working_formula": working_formula, "expected_answer_type": "number",
        "marks": 3, "correct_map": {"answer": correct_answer},
        "rubric_map": {"answer": working_formula},
        "guidelines": [working_formula] if working_formula else [],
        "visual_aid_key": "reconciliation_t2",
    }


# ---------------------------------------------------------------------------
# Bank Reconciliation generators
# ---------------------------------------------------------------------------

def _gen_bank_recon_balance(r: random.Random):
    """Calculate the corrected bank account balance from BRS adjustments."""
    biz = r.choice(_BUSINESSES)
    month = r.choice(["January", "February", "March", "April", "May", "June",
                       "July", "August", "September", "October", "November"])
    year = r.choice([2022, 2023, 2024])

    bs_balance = _rm(r.randint(50, 200) * 1000)  # credit balance on bank statement
    outstanding_deposit = _rm(r.randint(5, 25) * 1000)
    outstanding_chq1 = _rm(r.randint(1, 8) * 1000)
    outstanding_chq2 = _rm(r.randint(1, 5) * 1000)

    # bank_acc_balance = bs_balance + outstanding_deposit - outstanding_cheques
    bank_acc = _rm(bs_balance + outstanding_deposit - outstanding_chq1 - outstanding_chq2)

    return _make_calc(
        prompt=(
            f"{biz}: Prepare the bank reconciliation statement for {month} {year}.\n\n"
            f"• Credit balance per bank statement: {_money(bs_balance)}\n"
            f"• Outstanding deposit: {_money(outstanding_deposit)}\n"
            f"• Outstanding cheques: No. 45 = {_money(outstanding_chq1)}, "
            f"No. 48 = {_money(outstanding_chq2)}\n\n"
            f"Calculate the balance of the bank account in the general ledger."
        ),
        correct_answer=bank_acc, unit="R",
        working_formula=(
            f"{_money(bs_balance)} + {_money(outstanding_deposit)} − "
            f"{_money(outstanding_chq1)} − {_money(outstanding_chq2)} = {_money(bank_acc)}"
        ),
    )


def _gen_cpj_correction(r: random.Random):
    """Correct an understated/overstated CPJ entry."""
    biz = r.choice(_BUSINESSES)
    correct_amt = _rm(r.randint(200, 2000))
    recorded_amt = _rm(correct_amt + r.choice([-1, 1]) * r.randint(10, 100))
    diff = _rm(correct_amt - recorded_amt)
    direction = "understated" if diff > 0 else "overstated"

    chq_no = r.randint(200, 500)
    payee = r.choice(["Makro", "Pick n Pay", "Game", "Woolworths", "Shoprite"])

    return _make_calc(
        prompt=(
            f"{biz}: Cheque no. {chq_no} on the bank statement shows {_money(correct_amt)}, "
            f"but the amount in the CPJ was recorded as {_money(recorded_amt)}. "
            f"The payment was for goods purchased from {payee}.\n\n"
            f"By how much was the entry {direction}?"
        ),
        correct_answer=abs(diff), unit="R",
        working_formula=f"|{_money(correct_amt)} − {_money(recorded_amt)}| = {_money(abs(diff))}",
    )


def _gen_rd_cheque(r: random.Random):
    """Dishonoured (RD) cheque treatment."""
    biz = r.choice(_BUSINESSES)
    debtor = r.choice(_DEBTOR_NAMES)
    chq_amt = _rm(r.randint(100, 5000))
    invoice_amt = _rm(chq_amt + r.randint(0, 500))

    return _make_typed(
        prompt=(
            f"{biz}: A cheque of {_money(chq_amt)} received from {debtor} "
            f"in settlement of an invoice of {_money(invoice_amt)} was returned "
            f"by the bank due to insufficient funds. No entries have been made.\n\n"
            f"What entries should be made in the books to correct this?"
        ),
        sample_answer=(
            f"Record in the CPJ: Debit Debtors Control {_money(chq_amt)}, "
            f"Credit Bank {_money(chq_amt)}. "
            f"The debtor {debtor} now owes the full amount again. "
            f"Any discount allowed must also be reversed."
        ),
        grading_rubric=[
            "Debit Debtors Control / Credit Bank",
            "Record in Cash Payments Journal (CPJ)",
            "Debtor owes the full amount again",
        ],
    )


def _gen_stale_cheque(r: random.Random):
    """Stale cheque (>6 months) treatment."""
    biz = r.choice(_BUSINESSES)
    supplier = r.choice(["Shezi Stat", "SA Office", "Metro Supplies", "Atlas Printers"])
    chq_no = r.randint(100, 300)
    amount = _rm(r.randint(50, 2000))
    expense = r.choice(["Stationery", "Printing", "Office supplies", "Cleaning materials"])

    return _make_typed(
        prompt=(
            f"{biz}: Cheque no. {chq_no} was issued to {supplier} for {expense} "
            f"({_money(amount)}) more than 6 months ago but has never been presented "
            f"for payment.\n\n"
            f"How should this stale cheque be treated?"
        ),
        sample_answer=(
            f"Cancel the stale cheque in the CRJ: Debit Bank {_money(amount)}, "
            f"Credit {expense} {_money(amount)}. "
            f"If a replacement cheque is needed, issue a new one in the CPJ."
        ),
        grading_rubric=[
            "Cancel stale cheque in CRJ",
            "Debit Bank / Credit the expense account",
            "Issue replacement cheque in CPJ if needed",
        ],
    )


def _gen_bank_error(r: random.Random):
    """Bank errors on the BRS."""
    biz = r.choice(_BUSINESSES)
    error_type = r.choice(["debit", "credit"])
    amount = _rm(r.randint(500, 5000))

    if error_type == "debit":
        prompt = (
            f"Cheque no. 2230 for {_money(amount)} on the bank statement was drawn by "
            f"another client but erroneously debited to {biz}'s account."
        )
        answer = (
            f"Credit this amount on the bank reconciliation statement "
            f"(it will increase the balance). The bank must correct its error."
        )
    else:
        prompt = (
            f"A deposit of {_money(amount)} on the bank statement was made by "
            f"the owner into their personal account but the bank credited it to "
            f"{biz}'s business account."
        )
        answer = (
            f"Debit this amount on the bank reconciliation statement "
            f"(it will decrease the balance). The bank must correct its error."
        )

    return _make_typed(
        prompt=f"{biz}: {prompt}\n\nHow should this be treated on the BRS?",
        sample_answer=answer,
        grading_rubric=[
            "Bank error — record on BRS (not in CPJ/CRJ)",
            f"{'Credit' if error_type == 'debit' else 'Debit'} side of the BRS",
        ],
    )


# ---------------------------------------------------------------------------
# Debtors reconciliation
# ---------------------------------------------------------------------------

def _gen_debtors_control_correction(r: random.Random):
    """Correct the debtors control account balance."""
    biz = r.choice(_BUSINESSES)
    initial_bal = _rm(r.randint(150, 300) * 1000)

    overcast = _rm(r.randint(1, 5) * 1000)  # DJ overcast
    omitted_invoice = _rm(r.randint(1, 5) * 1000)  # not yet recorded
    rd_cheque = _rm(r.randint(5, 20) * 1000)  # RD cheque not entered

    corrected = _rm(initial_bal - overcast + omitted_invoice + rd_cheque)

    return _make_calc(
        prompt=(
            f"{biz}: The balance of the debtors' control account is {_money(initial_bal)}.\n"
            f"The following errors were discovered:\n"
            f"A. The debtors' journal was overcast by {_money(overcast)}.\n"
            f"B. An invoice of {_money(omitted_invoice)} to a debtor was not recorded.\n"
            f"C. An RD cheque of {_money(rd_cheque)} was not entered.\n\n"
            f"Calculate the correct closing balance of the debtors' control account."
        ),
        correct_answer=corrected, unit="R",
        working_formula=(
            f"{_money(initial_bal)} − {_money(overcast)} + {_money(omitted_invoice)} "
            f"+ {_money(rd_cheque)} = {_money(corrected)}"
        ),
    )


def _gen_debtor_individual_correction(r: random.Random):
    """Correct individual debtor's balance."""
    biz = r.choice(_BUSINESSES)
    debtor = r.choice(_DEBTOR_NAMES)
    bal = _rm(r.randint(5, 50) * 1000)

    # Wrong debtor charged
    wrong_amt = _rm(r.randint(2, 10) * 1000)
    # Posted to wrong side
    wrong_side_amt = _rm(r.randint(3, 8) * 1000)

    corrected = _rm(bal - wrong_amt + 2 * wrong_side_amt)

    return _make_calc(
        prompt=(
            f"{biz}: {debtor}'s balance in the debtors ledger is {_money(bal)}.\n"
            f"Errors discovered:\n"
            f"• Stock of {_money(wrong_amt)} was incorrectly charged to {debtor} "
            f"instead of another debtor.\n"
            f"• An invoice of {_money(wrong_side_amt)} was posted to the credit side "
            f"of {debtor}'s account instead of the debit side.\n\n"
            f"Calculate {debtor}'s correct balance."
        ),
        correct_answer=corrected, unit="R",
        working_formula=(
            f"{_money(bal)} − {_money(wrong_amt)} + 2 × {_money(wrong_side_amt)} = {_money(corrected)}"
        ),
    )


def _gen_creditors_recon(r: random.Random):
    """Creditors statement vs account reconciliation."""
    biz = r.choice(_BUSINESSES)
    supplier = r.choice(["Alpha Supplies", "Beta Trading", "Gamma Wholesale",
                         "Delta Distributors", "Epsilon Furnishers"])

    supplier_bal = _rm(r.randint(30, 100) * 1000)
    our_bal = _rm(r.randint(25, 95) * 1000)

    # Differences
    invoice_not_received = _rm(r.randint(2, 10) * 1000)
    payment_in_transit = _rm(r.randint(1, 8) * 1000)

    # Reconcile from supplier balance to our balance
    reconciled = _rm(supplier_bal - invoice_not_received - payment_in_transit)

    diff = _rm(abs(reconciled - our_bal))

    return _make_calc(
        prompt=(
            f"{biz}: The statement from {supplier} shows a balance of {_money(supplier_bal)}.\n"
            f"Our creditor's account shows {_money(our_bal)}.\n\n"
            f"Differences identified:\n"
            f"• Invoice from {supplier} not yet received: {_money(invoice_not_received)}\n"
            f"• Payment sent but not yet received by {supplier}: {_money(payment_in_transit)}\n\n"
            f"After these adjustments, what balance should our creditor's account show?"
        ),
        correct_answer=reconciled, unit="R",
        working_formula=(
            f"{_money(supplier_bal)} − {_money(invoice_not_received)} − "
            f"{_money(payment_in_transit)} = {_money(reconciled)}"
        ),
    )


def _gen_overcast_undercast(r: random.Random):
    """Over/undercast journal effect on control account."""
    biz = r.choice(_BUSINESSES)
    journal = r.choice(["Debtors Journal", "Creditors Journal", "Cash Receipts Journal"])
    direction = r.choice(["overcast", "undercast"])
    amount = _rm(r.randint(1, 10) * 1000)
    initial = _rm(r.randint(100, 300) * 1000)

    if direction == "overcast":
        corrected = _rm(initial - amount)
        effect = "too high by"
    else:
        corrected = _rm(initial + amount)
        effect = "too low by"

    return _make_calc(
        prompt=(
            f"{biz}: The {journal} was {direction} by {_money(amount)}. "
            f"The balance of the control account before correction is {_money(initial)}. "
            f"Calculate the corrected control account balance."
        ),
        correct_answer=corrected, unit="R",
        working_formula=(
            f"The total was {effect} {_money(amount)}. "
            f"Corrected = {_money(initial)} {'−' if direction == 'overcast' else '+'} "
            f"{_money(amount)} = {_money(corrected)}"
        ),
    )


# ---------------------------------------------------------------------------
# Concepts & internal control
# ---------------------------------------------------------------------------

def _gen_recon_concepts_mcq(r: random.Random):
    qs = [
        {
            "prompt": "Why is a bank reconciliation statement prepared?",
            "options": [
                "To explain differences between the bank account and the bank statement",
                "To calculate the profit for the year",
                "To prepare the income statement",
                "To record sales transactions",
            ],
            "correct": 0,
            "explanation": "A BRS explains why the bank account balance differs from the bank statement balance.",
        },
        {
            "prompt": "A cheque that has not been presented for payment within 6 months is called:",
            "options": [
                "A stale cheque",
                "A post-dated cheque",
                "A dishonoured cheque",
                "A cancelled cheque",
            ],
            "correct": 0,
            "explanation": "A cheque older than 6 months that hasn't been cashed is considered stale.",
        },
        {
            "prompt": "An RD cheque (returned/dishonoured cheque) must be recorded in the:",
            "options": [
                "Cash Payments Journal (CPJ)",
                "Cash Receipts Journal (CRJ)",
                "Debtors Journal (DJ)",
                "General Journal (GJ)",
            ],
            "correct": 0,
            "explanation": "An RD cheque is a payment going out of the bank account, so it's recorded in the CPJ.",
        },
    ]
    chosen = r.choice(qs)
    return _make_mcq(
        prompt=chosen["prompt"], options=chosen["options"],
        correct_index=chosen["correct"], explanation=chosen["explanation"],
    )


def _gen_age_analysis(r: random.Random):
    biz = r.choice(_BUSINESSES)
    current = _rm(r.randint(50, 150) * 1000)
    d30 = _rm(r.randint(20, 60) * 1000)
    d60 = _rm(r.randint(10, 30) * 1000)
    d90 = _rm(r.randint(5, 20) * 1000)
    total = _rm(current + d30 + d60 + d90)
    overdue_pct = round((d60 + d90) / total * 100, 1) if total > 0 else 0

    return _make_typed(
        prompt=(
            f"{biz}: Debtors' age analysis:\n"
            f"• Current: {_money(current)}\n"
            f"• 30 days: {_money(d30)}\n"
            f"• 60 days: {_money(d60)}\n"
            f"• 90+ days: {_money(d90)}\n"
            f"• Total: {_money(total)}\n\n"
            f"Comment on the debtors' position and suggest improvements."
        ),
        sample_answer=(
            f"The 60+ days overdue amount ({_money(_rm(d60 + d90))}) represents "
            f"{overdue_pct}% of total debtors — this is concerning. "
            f"The business should: 1) Follow up on overdue accounts. "
            f"2) Review credit terms and enforce a stricter collection policy. "
            f"3) Consider charging interest on overdue accounts."
        ),
        grading_rubric=[
            "Identifies overdue amounts as a concern",
            "Suggests follow-up on overdue accounts",
            "Proposes stricter credit/collection policy",
        ],
    )


def _gen_internal_control_cash(r: random.Random):
    return _make_typed(
        prompt="Suggest TWO internal control measures for managing the bank account and cash.",
        sample_answer=(
            "1. Require dual signatories for cheques above a specified amount. "
            "2. Perform monthly bank reconciliations and have them reviewed by a senior person. "
            "3. Deposit cash receipts daily. "
            "4. Separate duties — the person who writes cheques should not reconcile the bank statement."
        ),
        grading_rubric=[
            "Dual signatories or authorisation controls",
            "Regular bank reconciliation or separation of duties",
        ],
    )


# ---------------------------------------------------------------------------
# Main entry
# ---------------------------------------------------------------------------

_GENERATORS = [
    _gen_bank_recon_balance,
    _gen_cpj_correction,
    _gen_rd_cheque,
    _gen_stale_cheque,
    _gen_bank_error,
    _gen_debtors_control_correction,
    _gen_debtor_individual_correction,
    _gen_creditors_recon,
    _gen_overcast_undercast,
    _gen_recon_concepts_mcq,
    _gen_age_analysis,
    _gen_internal_control_cash,
]


def generate_questions(
    *, subskill="mixed", difficulty="easy", question_type="mixed",
    count=1, seed=None, mode="",
) -> List[Dict[str, Any]]:
    r = _rng(seed)
    questions = []
    for _ in range(count):
        q = r.choice(_GENERATORS)(r)
        q["difficulty"] = difficulty
        q["mode"] = mode
        questions.append(q)
    return questions
