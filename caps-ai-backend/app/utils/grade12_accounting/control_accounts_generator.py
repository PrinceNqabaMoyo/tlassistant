"""
Grade 12 Accounting: Control Accounts (Company Debtors & Creditors Control Reconciliations)
Strictly aligned with South African National Curriculum Standards for Grade 12 Accounting (Term 2).
"""
import random
from typing import Any, Dict, List, Optional

SUBSKILLS = [
    "company_debtors_control_reconciliation",
    "company_creditors_control_reconciliation",
    "credit_balance_transfer_between_debtors_and_creditors",
    "vat_inclusive_control_account_adjustments",
    "audit_findings_on_company_control_accounts",
]

COMPANIES = [
    "Apex Wholesalers Ltd",
    "Highveld Distributors Ltd",
    "Protea Retail Ltd",
    "Zululand Supplies Ltd",
]


def _make_hints(t1: str, t2: str, t3: str) -> List[Dict[str, str]]:
    return [
        {"tier": 1, "title": "Conceptual Nudge", "content": t1},
        {"tier": 2, "title": "Procedural Step", "content": t2},
        {"tier": 3, "title": "Full Worked Example", "content": t3},
    ]


def _gen_company_debtors_control(r: random.Random) -> Dict[str, Any]:
    co = r.choice(COMPANIES)
    prelim = r.randint(140, 220) * 1000
    dj_under = r.randint(8, 16) * 1000
    daj_over = r.randint(3, 6) * 1000
    bad_omitted = r.randint(4, 9) * 1000
    final_bal = prelim + dj_under + daj_over - bad_omitted

    headers = ["Debtors Control Audit Adjustment", "Amount (R)"]
    rows = [
        ["Preliminary Debtors Control balance before audit adjustments", f"R{prelim:,}"],
        [f"Add: Debtors Journal total was undercast by R{dj_under:,}", "{r1_c1}"],
        [f"Add: Debtors Allowances Journal total was overcast by R{daj_over:,}", "{r2_c1}"],
        [f"Less: Bad debts of R{bad_omitted:,} written off in GJ but omitted from Debtors Control", f"(R{bad_omitted:,})"],
        ["Audited Closing Balance of Debtors Control", "{r4_c1}"],
    ]
    correct_map = {
        "r1_c1": dj_under,
        "r2_c1": daj_over,
        "r4_c1": final_bal,
    }
    worked = (
        f"**Company Debtors Control Reconciliation ({co})**\n\n"
        f"- Add undercast DJ total (`+ R{dj_under:,}`)\n"
        f"- Add back overcast DAJ total (`+ R{daj_over:,}` because too much was credited)\n"
        f"- Deduct omitted bad debts (`- R{bad_omitted:,}`)\n"
        f"- **Audited Closing Balance**: `R{prelim:,} + R{dj_under:,} + R{daj_over:,} - R{bad_omitted:,} = R{final_bal:,}`"
    )
    return {
        "question_type": "table_fill",
        "subskill": "company_debtors_control_reconciliation",
        "question_text": f"Complete the year-end audit reconciliation of the **Debtors Control Account** for **{co}**.",
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "marks": 5,
        "worked_solution": worked,
        "canonical_solution": worked,
        "hints": _make_hints(
            "Overcasting the Debtors Allowances Journal means Debtors Control was credited by too much, so the overcast must be added back.",
            "Enter the two additions and compute the final audited balance.",
            worked,
        ),
    }


def _gen_company_creditors_control(r: random.Random) -> Dict[str, Any]:
    co = r.choice(COMPANIES)
    prelim = r.randint(160, 260) * 1000
    cj_over = r.randint(6, 14) * 1000
    eft_reversal = r.randint(9, 18) * 1000
    disc_rev = r.randint(1, 2) * 1000
    final_bal = prelim - cj_over + eft_reversal + disc_rev

    headers = ["Creditors Control Audit Adjustment", "Amount (R)"]
    rows = [
        ["Preliminary Creditors Control balance", f"R{prelim:,}"],
        [f"Less: Creditors Journal total overcast by R{cj_over:,}", f"(R{cj_over:,})"],
        [f"Add: Post-dated / cancelled EFT payment of R{eft_reversal:,} reversed", "{r2_c1}"],
        [f"Add: Settlement discount of R{disc_rev:,} forfeited on cancelled payment", "{r3_c1}"],
        ["Audited Closing Balance of Creditors Control", "{r4_c1}"],
    ]
    correct_map = {
        "r2_c1": eft_reversal,
        "r3_c1": disc_rev,
        "r4_c1": final_bal,
    }
    worked = (
        f"**Company Creditors Control Reconciliation ({co})**\n\n"
        f"- Deduct overcast CJ (`- R{cj_over:,}`)\n"
        f"- Add back cancelled payment (`+ R{eft_reversal:,}`) and forfeited discount (`+ R{disc_rev:,}`)\n"
        f"- **Audited Closing Balance**: `R{final_bal:,}`"
    )
    return {
        "question_type": "table_fill",
        "subskill": "company_creditors_control_reconciliation",
        "question_text": f"Complete the year-end audit reconciliation of the **Creditors Control Account** for **{co}**.",
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "marks": 5,
        "worked_solution": worked,
        "canonical_solution": worked,
        "hints": _make_hints(
            "When a payment to a creditor is cancelled, both the payment and any settlement discount claimed must be added back to Creditors Control.",
            "Enter the reversed payment and forfeited discount, then calculate the closing balance.",
            worked,
        ),
    }


def _gen_credit_balance_transfer(r: random.Random) -> Dict[str, Any]:
    co = r.choice(COMPANIES)
    debt_bal = r.randint(90, 150) * 1000
    cred_bal = r.randint(110, 180) * 1000
    transfer_amt = r.randint(4, 9) * 1000

    headers = ["Control Account Transfer", "Debtors Control (R)", "Creditors Control (R)"]
    rows = [
        ["Balance before transferring debtor's credit balance", f"R{debt_bal:,}", f"R{cred_bal:,}"],
        [f"Transfer credit balance of R{transfer_amt:,} from a debtor's account to their account in the Creditors Ledger", "{r1_c1}", "{r1_c2}"],
        ["Adjusted Control Account Balances for Balance Sheet Notes", "{r2_c1}", "{r2_c2}"],
    ]
    correct_map = {
        "r1_c1": transfer_amt,
        "r1_c2": transfer_amt,
        "r2_c1": debt_bal + transfer_amt,
        "r2_c2": cred_bal + transfer_amt,
    }
    worked = (
        f"**Transferring a Credit Balance in Debtors Ledger ({co})**\n\n"
        f"- Removing a credit balance from Debtors Control requires a **Debit** to Debtors Control (`+ R{transfer_amt:,}` to its debit balance) and a **Credit** to Creditors Control (`+ R{transfer_amt:,}` to its credit balance).\n"
        f"- **Adjusted Debtors Control**: `R{debt_bal + transfer_amt:,}`\n"
        f"- **Adjusted Creditors Control**: `R{cred_bal + transfer_amt:,}`"
    )
    return {
        "question_type": "table_fill",
        "subskill": "credit_balance_transfer_between_debtors_and_creditors",
        "question_text": (
            f"At year-end, **{co}** transfers a credit balance of **R{transfer_amt:,}** in the Debtors Ledger to the Creditors Ledger. "
            f"Complete the impact on both Control Accounts."
        ),
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "marks": 6,
        "worked_solution": worked,
        "canonical_solution": worked,
        "hints": _make_hints(
            "Eliminating a negative (credit) balance inside Debtors Control increases the net Debit balance of Debtors Control and increases the Credit balance of Creditors Control.",
            f"Add R{transfer_amt:,} to both Debtors Control and Creditors Control.",
            worked,
        ),
    }


def _gen_vat_inclusive_control_adjustments(r: random.Random) -> Dict[str, Any]:
    co = r.choice(COMPANIES)
    excl = r.choice([6000, 8000, 10000, 12000])
    vat = int(excl * 0.15)
    incl = excl + vat

    headers = ["Unrecorded Credit Return by Debtor", "Account Adjusted", "Amount (R)"]
    rows = [
        [f"Goods returned by debtor (Selling price excl. VAT = R{excl:,}) — Sales Return (Debtors Allowances)", "Debtors Allowances (Debit)", "{r0_c2}"],
        ["15% Output VAT reversed on goods returned", "VAT Control (Debit)", "{r1_c2}"],
        ["Total VAT-inclusive credit note credited to Debtors Control", "Debtors Control (Credit)", "{r2_c2}"],
    ]
    correct_map = {
        "r0_c2": excl,
        "r1_c2": vat,
        "r2_c2": incl,
    }
    worked = (
        f"**VAT-Inclusive Control Account Adjustment ({co})**\n\n"
        f"- **Debtors Allowances (excl. VAT)**: `R{excl:,}`\n"
        f"- **VAT Control (15%)**: `R{vat:,}`\n"
        f"- **Debtors Control (incl. VAT)**: `R{excl:,} + R{vat:,} = R{incl:,}`"
    )
    return {
        "question_type": "table_fill",
        "subskill": "vat_inclusive_control_account_adjustments",
        "question_text": (
            f"A credit note for goods returned by a debtor of **{co}** (VAT-exclusive selling price **R{excl:,}**, plus **15% VAT**) "
            f"was omitted from the books. Complete the adjustment amounts."
        ),
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "marks": 5,
        "worked_solution": worked,
        "canonical_solution": worked,
        "hints": _make_hints(
            "Debtors Control always records the full VAT-inclusive amount, while Debtors Allowances records the VAT-exclusive amount.",
            "Enter the exclusive amount in Row 1, 15% VAT in Row 2, and the sum in Row 3.",
            worked,
        ),
    }


def _gen_audit_findings_control_accounts(r: random.Random) -> Dict[str, Any]:
    headers = ["Internal Audit Finding on Control Accounts", "Corrective Entry Required (General Journal Entry / Post to Subsidiary Ledger Only / Adjust Control Account Only)"]
    rows = [
        ["Interest of R1,850 charged on an overdue debtor's account was completely omitted from all books", "{r0_c1}"],
        ["A credit sales invoice of R4,200 was entered in the DJ and posted to Debtors Control, but omitted from the debtor's individual account", "{r1_c1}"],
        ["The Sales column in the Debtors Journal was undercast by R10,000, though individual debtors' accounts were posted correctly", "{r2_c1}"],
    ]
    correct_map = {
        "r0_c1": "General Journal Entry",
        "r1_c1": "Post to Subsidiary Ledger Only",
        "r2_c1": "Adjust Control Account Only",
    }
    worked = (
        "**Audit Findings on Company Control Accounts**\n\n"
        "- Complete omission of overdue interest requires a **General Journal Entry** (posting to both Control Account and Subsidiary Ledger).\n"
        "- Omission from the individual account only requires **Post to Subsidiary Ledger Only**.\n"
        "- Undercast journal total requires **Adjust Control Account Only**."
    )
    return {
        "question_type": "table_fill",
        "subskill": "audit_findings_on_company_control_accounts",
        "question_text": "Select the required corrective action for each internal audit finding from the column heading.",
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "marks": 6,
        "worked_solution": worked,
        "canonical_solution": worked,
        "hints": _make_hints(
            "Determine whether the error affected both records, only the subsidiary ledger, or only the control account total.",
            "Match each finding to one of the three corrective options in the column header.",
            worked,
        ),
    }


_BUILDERS = {
    "company_debtors_control_reconciliation": _gen_company_debtors_control,
    "company_creditors_control_reconciliation": _gen_company_creditors_control,
    "credit_balance_transfer_between_debtors_and_creditors": _gen_credit_balance_transfer,
    "vat_inclusive_control_account_adjustments": _gen_vat_inclusive_control_adjustments,
    "audit_findings_on_company_control_accounts": _gen_audit_findings_control_accounts,
}


def generate_questions(
    count: int = 1,
    subskill: Optional[str] = None,
    seed: Optional[int] = None,
    **kwargs,
) -> List[Dict[str, Any]]:
    r = random.Random(seed)
    out: List[Dict[str, Any]] = []
    for _ in range(count):
        chosen = subskill if (subskill and subskill in _BUILDERS) else r.choice(SUBSKILLS)
        q = _BUILDERS[chosen](r)
        q["subskill"] = chosen
        q["topic"] = "Control accounts"
        q["grade"] = "12"
        out.append(q)
    return out
