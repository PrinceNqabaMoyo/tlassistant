"""
Grade 11 Accounting: Control Accounts (Debtors Control & Creditors Control Reconciliations)
Strictly aligned with South African National Curriculum Standards for Grade 11 Accounting (Term 1).
"""
import random
from typing import Any, Dict, List, Optional

SUBSKILLS = [
    "debtors_control_taccount_reconstruction",
    "creditors_control_taccount_reconstruction",
    "reconciling_debtors_control_with_debtors_list",
    "reconciling_creditors_control_with_creditors_list",
    "control_account_error_correction_matrix",
    "control_accounts_internal_controls",
]

PARTNERSHIPS = [
    "Mokoena & Dlamini Traders",
    "Naidoo & Botha Wholesalers",
    "Khumalo & Van Wyk Suppliers",
    "Ndlovu & Pillay Outfitters",
]


def _make_hints(t1: str, t2: str, t3: str) -> List[Dict[str, str]]:
    return [
        {"tier": 1, "title": "Conceptual Nudge", "content": t1},
        {"tier": 2, "title": "Procedural Step", "content": t2},
        {"tier": 3, "title": "Full Worked Example", "content": t3},
    ]


def _gen_debtors_control_taccount(r: random.Random) -> Dict[str, Any]:
    firm = r.choice(PARTNERSHIPS)
    open_bal = r.randint(45, 85) * 1000
    sales_dj = r.randint(120, 210) * 1000
    rd_cpj = r.randint(3, 8) * 1000
    int_gj = r.randint(1, 3) * 1000
    tot_dr = open_bal + sales_dj + rd_cpj + int_gj

    rec_crj = r.randint(95, 160) * 1000
    disc_crj = r.randint(3, 7) * 1000
    allow_daj = r.randint(4, 10) * 1000
    bad_gj = r.randint(2, 6) * 1000
    tot_cr_before_bal = rec_crj + disc_crj + allow_daj + bad_gj
    close_bal = tot_dr - tot_cr_before_bal

    headers = ["Debtors Control Account Entry", "Side (Debit / Credit)", "Amount (R)"]
    rows = [
        ["Opening balance b/d", "Debit", f"R{open_bal:,}"],
        ["Credit sales (DJ)", "Debit", f"R{sales_dj:,}"],
        ["Dishonoured cheque / EFT reversal (CPJ) + Interest charged (GJ)", "Debit", f"R{rd_cpj + int_gj:,}"],
        ["Total Debits", "Debit", "{r3_c2}"],
        ["Receipts from debtors + Discount allowed (CRJ)", "Credit", f"R{rec_crj + disc_crj:,}"],
        ["Debtors allowances (DAJ) + Bad debts written off (GJ)", "Credit", f"R{allow_daj + bad_gj:,}"],
        ["Closing balance c/d (owing by debtors)", "Credit (balancing)", "{r6_c2}"],
    ]
    correct_map = {
        "r3_c2": tot_dr,
        "r6_c2": close_bal,
    }
    worked = (
        f"**Debtors Control Account ({firm})**\n\n"
        f"- **Total Debits**: `R{open_bal:,} + R{sales_dj:,} + R{rd_cpj + int_gj:,} = R{tot_dr:,}`\n"
        f"- **Total Credits**: `R{rec_crj + disc_crj:,} + R{allow_daj + bad_gj:,} = R{tot_cr_before_bal:,}`\n"
        f"- **Closing Debit Balance c/d**: `R{tot_dr:,} - R{tot_cr_before_bal:,} = R{close_bal:,}`"
    )
    return {
        "question_type": "table_fill",
        "subskill": "debtors_control_taccount_reconstruction",
        "question_text": f"Complete the **Debtors Control Account** summary for **{firm}** at month-end.",
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "marks": 5,
        "worked_solution": worked,
        "canonical_solution": worked,
        "hints": _make_hints(
            "Debtors Control is an Asset account: it increases on the Debit side and decreases on the Credit side.",
            "Sum the three debit lines to find Total Debits, then subtract the credit entries to find the closing balance.",
            worked,
        ),
    }


def _gen_creditors_control_taccount(r: random.Random) -> Dict[str, Any]:
    firm = r.choice(PARTNERSHIPS)
    open_cr = r.randint(50, 95) * 1000
    purch_cj = r.randint(130, 220) * 1000
    int_gj = r.randint(2, 5) * 1000
    tot_cr = open_cr + purch_cj + int_gj

    pay_cpj = r.randint(100, 170) * 1000
    disc_cpj = r.randint(4, 9) * 1000
    allow_caj = r.randint(5, 12) * 1000
    tot_dr = pay_cpj + disc_cpj + allow_caj
    close_cr = tot_cr - tot_dr

    headers = ["Creditors Control Account Entry", "Side (Debit / Credit)", "Amount (R)"]
    rows = [
        ["Opening balance b/d", "Credit", f"R{open_cr:,}"],
        ["Credit purchases (CJ) + Interest charged by creditors (GJ)", "Credit", f"R{purch_cj + int_gj:,}"],
        ["Total Credits", "Credit", "{r2_c2}"],
        ["Payments to creditors + Discount received (CPJ)", "Debit", f"R{pay_cpj + disc_cpj:,}"],
        ["Creditors allowances / returns (CAJ)", "Debit", f"R{allow_caj:,}"],
        ["Closing balance c/d (owing to creditors)", "Debit (balancing)", "{r5_c2}"],
    ]
    correct_map = {
        "r2_c2": tot_cr,
        "r5_c2": close_cr,
    }
    worked = (
        f"**Creditors Control Account ({firm})**\n\n"
        f"- **Total Credits**: `R{open_cr:,} + R{purch_cj + int_gj:,} = R{tot_cr:,}`\n"
        f"- **Total Debits**: `R{pay_cpj + disc_cpj:,} + R{allow_caj:,} = R{tot_dr:,}`\n"
        f"- **Closing Credit Balance c/d**: `R{tot_cr:,} - R{tot_dr:,} = R{close_cr:,}`"
    )
    return {
        "question_type": "table_fill",
        "subskill": "creditors_control_taccount_reconstruction",
        "question_text": f"Complete the **Creditors Control Account** summary for **{firm}** at month-end.",
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "marks": 5,
        "worked_solution": worked,
        "canonical_solution": worked,
        "hints": _make_hints(
            "Creditors Control is a Liability account: it increases on the Credit side and decreases on the Debit side.",
            "Sum the credit entries to find Total Credits, then subtract payments, discounts received, and allowances.",
            worked,
        ),
    }


def _gen_reconcile_debtors_control_and_list(r: random.Random) -> Dict[str, Any]:
    firm = r.choice(PARTNERSHIPS)
    true_bal = r.randint(65, 115) * 1000
    dj_undercast = r.randint(3, 8) * 1000
    inv_omitted_ledger = r.randint(2, 6) * 1000

    prelim_control = true_bal - dj_undercast
    prelim_list = true_bal - inv_omitted_ledger

    headers = ["Reconciliation of Debtors Control & Debtors List", "Debtors Control Account (R)", "Debtors List Total (R)"]
    rows = [
        ["Preliminary balance / total before corrections", f"R{prelim_control:,}", f"R{prelim_list:,}"],
        [f"Correction 1: Debtors Journal total was undercast by R{dj_undercast:,}", "{r1_c1}", "0"],
        [f"Correction 2: Credit invoice of R{inv_omitted_ledger:,} posted to DJ but omitted from debtor's ledger account", "0", "{r2_c2}"],
        ["Reconciled Closing Balance / Total", "{r3_c1}", "{r3_c2}"],
    ]
    correct_map = {
        "r1_c1": dj_undercast,
        "r2_c2": inv_omitted_ledger,
        "r3_c1": true_bal,
        "r3_c2": true_bal,
    }
    worked = (
        f"**Reconciling Debtors Control and Debtors List ({firm})**\n\n"
        f"- **Undercast DJ total (`R{dj_undercast:,}`)**: Affects only the **Debtors Control Account** (`R{prelim_control:,} + R{dj_undercast:,} = R{true_bal:,}`).\n"
        f"- **Invoice omitted from individual debtor's account (`R{inv_omitted_ledger:,}`)**: Affects only the **Debtors List** (`R{prelim_list:,} + R{inv_omitted_ledger:,} = R{true_bal:,}`).\n"
        f"- Both reconcile to **`R{true_bal:,}`**."
    )
    return {
        "question_type": "table_fill",
        "subskill": "reconciling_debtors_control_with_debtors_list",
        "question_text": (
            f"Reconcile the **Debtors Control Account** and the **Debtors List** for **{firm}** after taking the two errors into account."
        ),
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "marks": 6,
        "worked_solution": worked,
        "canonical_solution": worked,
        "hints": _make_hints(
            "An casting error in a journal total affects only the Control Account, whereas a posting omission to an individual account affects only the List.",
            "Add the undercast DJ total to the Control Account column and add the omitted individual posting to the Debtors List column.",
            worked,
        ),
    }


def _gen_reconcile_creditors_control_and_list(r: random.Random) -> Dict[str, Any]:
    firm = r.choice(PARTNERSHIPS)
    true_bal = r.randint(70, 125) * 1000
    caj_overcast = r.randint(2, 5) * 1000
    posted_twice_list = r.randint(3, 7) * 1000

    prelim_control = true_bal - caj_overcast
    prelim_list = true_bal + posted_twice_list

    headers = ["Reconciliation of Creditors Control & Creditors List", "Creditors Control Account (R)", "Creditors List Total (R)"]
    rows = [
        ["Preliminary balance / total before corrections", f"R{prelim_control:,}", f"R{prelim_list:,}"],
        [f"Correction 1: Creditors Allowances Journal (CAJ) total was overcast by R{caj_overcast:,}", "{r1_c1}", "0"],
        [f"Correction 2: Credit purchase invoice of R{posted_twice_list:,} was credited twice to supplier's individual account", "0", f"({posted_twice_list})"],
        ["Reconciled Closing Balance / Total", "{r3_c1}", "{r3_c2}"],
    ]
    correct_map = {
        "r1_c1": caj_overcast,
        "r3_c1": true_bal,
        "r3_c2": true_bal,
    }
    worked = (
        f"**Reconciling Creditors Control and Creditors List ({firm})**\n\n"
        f"- **CAJ overcast (`R{caj_overcast:,}`)**: Too much was deducted on the debit side of Creditors Control, so add back `R{caj_overcast:,}` (`R{prelim_control:,} + R{caj_overcast:,} = R{true_bal:,}`).\n"
        f"- **Invoice credited twice to individual creditor (`R{posted_twice_list:,}`)**: Deduct `R{posted_twice_list:,}` from the Creditors List (`R{prelim_list:,} - R{posted_twice_list:,} = R{true_bal:,}`)."
    )
    return {
        "question_type": "table_fill",
        "subskill": "reconciling_creditors_control_with_creditors_list",
        "question_text": (
            f"Reconcile the **Creditors Control Account** and the **Creditors List** for **{firm}**."
        ),
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "marks": 5,
        "worked_solution": worked,
        "canonical_solution": worked,
        "hints": _make_hints(
            "Overcasting the CAJ means we debited Creditors Control by too much; we must add the overcast back to the Credit balance.",
            "Enter the CAJ overcast in Row 2 Column 1, then verify that both reconciled totals equal.",
            worked,
        ),
    }


def _gen_error_correction_matrix(r: random.Random) -> Dict[str, Any]:
    headers = ["Error Discovered", "Affects Control Account? (Yes / No)", "Affects Subsidiary Ledger List? (Yes / No)"]
    rows = [
        ["Source document (credit invoice) completely omitted from the Debtors Journal", "{r0_c1}", "{r0_c2}"],
        ["Debtors Journal column total added up incorrectly (casting error)", "{r1_c1}", "{r1_c2}"],
        ["Invoice correctly entered in DJ but posted to the wrong debtor's account in the Debtors Ledger", "{r2_c1}", "{r2_c2}"],
        ["Invoice correctly entered in DJ but not posted to the debtor's individual account", "{r3_c1}", "{r3_c2}"],
    ]
    correct_map = {
        "r0_c1": "Yes",
        "r0_c2": "Yes",
        "r1_c1": "Yes",
        "r1_c2": "No",
        "r2_c1": "No",
        "r2_c2": "No",
        "r3_c1": "No",
        "r3_c2": "Yes",
    }
    worked = (
        "**Control Account Error Impact Matrix**\n\n"
        "- **Complete omission from DJ**: Affects **Both** (`Yes` / `Yes`) because neither the journal total nor the individual account has the entry.\n"
        "- **Journal casting error**: Affects **Control Account only** (`Yes` / `No`).\n"
        "- **Posted to wrong debtor's account**: Affects **Neither total** (`No` / `No`) — the overall Debtors List total is still unchanged, though the two individual accounts need adjustment.\n"
        "- **Omitted from individual posting**: Affects **Subsidiary List only** (`Yes` = No on Control, `Yes` on List)."
    )
    return {
        "question_type": "table_fill",
        "subskill": "control_account_error_correction_matrix",
        "question_text": (
            "For each error below, state whether it affects the **Debtors Control Account balance** and/or the **Debtors List total** (**Yes** or **No**)."
        ),
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "marks": 8,
        "worked_solution": worked,
        "canonical_solution": worked,
        "hints": _make_hints(
            "Ask: Was the journal total wrong (Control Account), or was the individual ledger posting wrong (Subsidiary List), or both?",
            "Remember that posting to the wrong debtor changes individual balances but leaves the sum of the Debtors List unchanged.",
            worked,
        ),
    }


def _gen_control_internal_controls(r: random.Random) -> Dict[str, Any]:
    headers = ["Risk / Control Weakness", "Control Measure (Segregation of Duties / Monthly Reconciliation / Credit Limit Approval)"]
    rows = [
        ["The clerk who receives cash from debtors also posts to the Debtors Ledger and writes off bad debts", "{r0_c1}"],
        ["Posting omissions and casting errors in the Debtors Ledger go undetected for several months", "{r1_c1}"],
        ["Sales staff continue selling on credit to customers who already have long-overdue balances", "{r2_c1}"],
    ]
    correct_map = {
        "r0_c1": "Segregation of Duties",
        "r1_c1": "Monthly Reconciliation",
        "r2_c1": "Credit Limit Approval",
    }
    worked = (
        "**Internal Controls over Control Accounts**\n\n"
        "- Combining cash receipting and ledger posting violates **Segregation of Duties**.\n"
        "- Undetected posting/casting errors are prevented by **Monthly Reconciliation** of the Control Account to the Debtors List.\n"
        "- Selling to overdue debtors is prevented by **Credit Limit Approval**."
    )
    return {
        "question_type": "table_fill",
        "subskill": "control_accounts_internal_controls",
        "question_text": (
            "Match each control weakness to the correct internal control procedure from the brackets."
        ),
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "marks": 6,
        "worked_solution": worked,
        "canonical_solution": worked,
        "hints": _make_hints(
            "Control accounts act as an independent check on the subsidiary ledger when prepared by a different person.",
            "Match each weakness to Segregation of Duties, Monthly Reconciliation, or Credit Limit Approval.",
            worked,
        ),
    }


_BUILDERS = {
    "debtors_control_taccount_reconstruction": _gen_debtors_control_taccount,
    "creditors_control_taccount_reconstruction": _gen_creditors_control_taccount,
    "reconciling_debtors_control_with_debtors_list": _gen_reconcile_debtors_control_and_list,
    "reconciling_creditors_control_with_creditors_list": _gen_reconcile_creditors_control_and_list,
    "control_account_error_correction_matrix": _gen_error_correction_matrix,
    "control_accounts_internal_controls": _gen_control_internal_controls,
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
        q["grade"] = "11"
        out.append(q)
    return out
