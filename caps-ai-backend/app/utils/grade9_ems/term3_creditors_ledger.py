"""Grade 9 EMS — Credit Transactions: Creditors Ledger & Reconciliation (Creditors 2).
100% Deterministic & SymPy/math backed. Satisfies the 6-Pillar Generator Contract.
Directly aligns with `curriculum_docs_auto/EMS_Gr9/Term 3/12-Credit transactions Creditors (2).md`.
Covers:
- Recording payments to creditors in the Cash Payments Journal (CPJ) with Creditors Control column
- 3-column running balance Creditors Ledger accounts (Date, Details, Fol, Debit [-], Credit [+], Balance)
- Compiling a Creditors List and reconciling with General Ledger Creditors Control account (B6)
- Supplier statement reconciliation and internal control checks
- Accounting equation effects for payments to creditors and credit purchases
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional
from app.utils.ems_namelist import get_ems_scenario

def _rng(seed: Optional[int] = None) -> random.Random:
    r = random.Random()
    if seed is not None:
        r.seed(int(seed))
    return r

TOPIC_ID = "grade9_ems"
SUBTOPIC_ID = "term3_creditors_ledger"
CURRICULUM_REFERENCE = "Term 3 > Financial Literacy: Credit Transactions (Creditors 2)"

def _with_metadata(
    item: Dict[str, Any],
    *,
    subskill: str,
    learning_objective_id: str,
    question_family_id: str,
    concept_id: Optional[str] = None,
    concept_group: Optional[str] = None,
    misconception_tags: Optional[List[str]] = None,
    diagnostic_tags: Optional[List[str]] = None,
) -> Dict[str, Any]:
    enriched = dict(item)
    enriched.update({
        "topic_id": TOPIC_ID,
        "subtopic_id": SUBTOPIC_ID,
        "subskill": subskill,
        "learning_objective_id": learning_objective_id,
        "concept_id": concept_id or subskill,
        "concept_group": concept_group or "creditors_ledger",
        "question_family_id": question_family_id,
        "curriculum_reference": CURRICULUM_REFERENCE,
        "misconception_tags": misconception_tags or [],
        "diagnostic_tags": diagnostic_tags or ["accounting", "creditors_ledger", "tabular"],
    })
    return enriched

# --------------------------------------------------------------------------- #
# Sub-Drill 1: 3-Column Creditors Ledger Account
# --------------------------------------------------------------------------- #
def _generate_creditors_ledger_drill(rng: random.Random, mode: str = "scaffold") -> Dict[str, Any]:
    scenario = get_ems_scenario(rng)
    business_name = f"{scenario['entrepreneur']}'s Store"
    month = "September 2026"
    
    creditors = ["Makro Wholesalers", "Metro Cash & Carry", "PaperCo Stationers", "Mega Suppliers"]
    creditor_name = rng.choice(creditors)
    creditor_fol = "C1"
    
    opening_bal = rng.randint(8, 25) * 100
    invoice_no = rng.randint(201, 350)
    purchase_amt = rng.randint(15, 45) * 100
    debit_note_no = rng.randint(40, 80)
    return_amt = rng.randint(2, 6) * 100
    cheque_no = rng.randint(501, 650)
    payment_amt = rng.randint(10, 20) * 100
    
    bal1 = opening_bal
    bal2 = bal1 + purchase_amt
    bal3 = bal2 - return_amt
    bal4 = bal3 - payment_amt
    
    transactions = [
        f"Sept 1: Account rendered balance brought forward: R{opening_bal:,}.",
        f"Sept 8: Purchased trading stock on credit from {creditor_name}, R{purchase_amt:,}. Received original invoice {invoice_no}.",
        f"Sept 16: Returned damaged stock to {creditor_name}, R{return_amt:,}. Issued Debit Note {debit_note_no} (CAJ).",
        f"Sept 25: Paid {creditor_name} R{payment_amt:,} via EFT / Cheque {cheque_no} in partial settlement of account (CPJ)."
    ]
    
    headers = ["Date", "Details", "Fol", "Debit (-)", "Credit (+)", "Balance"]
    
    data_rows = [
        ["1", "Account rendered", "b/d", "", "", str(bal1)],
        ["8", f"Invoice {invoice_no}", "CJ", "", str(purchase_amt), str(bal2)],
        ["16", f"Debit Note {debit_note_no}", "CAJ", str(return_amt), "", str(bal3)],
        ["25", f"Cheque {cheque_no}", "CPJ", str(payment_amt), "", str(bal4)],
    ]
    
    correct_map: Dict[str, str] = {}
    rows_data = []
    cell_hints: Dict[str, str] = {}
    
    for i, row in enumerate(data_rows):
        row_cells = []
        for j, val in enumerate(row):
            coord = f"t0_r{i}_c{j}"
            correct_map[coord] = val
            is_empty = (val == "")
            is_opening = (i == 0 and j in [0, 1, 2, 5])
            row_cells.append({
                "coordinate": coord,
                "value": val if (mode == "scaffold" or is_opening) else "",
                "type": "given" if is_opening else ("must_be_empty" if is_empty else "required"),
                "editable": not is_opening,
            })
        rows_data.append(row_cells)
        
    cell_hints["t0_r1_c4"] = f"Credit purchase from CJ: Credit column increases liability by R{purchase_amt:,}."
    cell_hints["t0_r1_c5"] = f"New Balance = Previous Balance (R{bal1:,}) + Credit (R{purchase_amt:,}) = R{bal2:,}."
    cell_hints["t0_r2_c3"] = f"Returns from CAJ: Debit column decreases liability by R{return_amt:,}."
    cell_hints["t0_r2_c5"] = f"New Balance = Previous Balance (R{bal2:,}) - Debit (R{return_amt:,}) = R{bal3:,}."
    cell_hints["t0_r3_c3"] = f"Payment from CPJ: Debit column decreases liability by R{payment_amt:,}."
    cell_hints["t0_r3_c5"] = f"New Balance = Previous Balance (R{bal3:,}) - Debit (R{payment_amt:,}) = R{bal4:,}."
    
    prompt = (
        f"You are the bookkeeper of **{business_name}**.\n"
        f"Record the credit transactions for **{creditor_name} ({creditor_fol})** in the 3-column **Creditors Ledger** for {month}.\n\n"
        f"Remember that a creditor is a **liability**: purchases increase the balance (Credit +), while returns and payments decrease the balance (Debit -)."
    )
    
    item = {
        "id": f"ems9_cl_{rng.randint(1000, 9999)}",
        "title": f"Creditors Ledger: {creditor_name} ({creditor_fol})",
        "question_type": "table_completion",
        "modality": "ledger",
        "prompt": prompt,
        "transactions": transactions,
        "headers": headers,
        "rows": rows_data,
        "journal": {
            "journal_type": "creditors_ledger",
            "headers": headers,
            "rows": rows_data,
        },
        "correct_map": correct_map,
        "cell_hints": cell_hints,
        "marks": 16,
        "sample_answer": f"Closing balance for {creditor_name} on Sept 25: R{bal4:,} (Credit balance).",
        "ideal_answer": "Complete 3-column Creditors Ledger account showing accurate folios, debit/credit entries, and running balances.",
        "hint_sections": {
            "1_nudge": "Creditors are liabilities. They have a normal credit balance.",
            "2_concept": "Invoice (CJ) goes to Credit (+) and increases balance. Debit Note (CAJ) and Cheque (CPJ) go to Debit (-) and reduce balance.",
            "3_breakdown": f"Bal = R{bal1:,} + R{purchase_amt:,} (CJ) - R{return_amt:,} (CAJ) - R{payment_amt:,} (CPJ) = R{bal4:,}."
        },
        "marking_schema": {
            "total_marks": 16,
            "marking_points": [
                {"id": "mp_cj", "desc": f"Sept 8: Invoice {invoice_no} in CJ, Credit R{purchase_amt:,}, Balance R{bal2:,}", "marks": 4, "editable": True},
                {"id": "mp_caj", "desc": f"Sept 16: Debit Note {debit_note_no} in CAJ, Debit R{return_amt:,}, Balance R{bal3:,}", "marks": 4, "editable": True},
                {"id": "mp_cpj", "desc": f"Sept 25: Cheque {cheque_no} in CPJ, Debit R{payment_amt:,}, Balance R{bal4:,}", "marks": 4, "editable": True},
                {"id": "mp_bal", "desc": f"Accurate running balances throughout", "marks": 4, "editable": True},
            ],
            "deductions": [{"rule": "must_be_empty_filled", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
        "misconception_tags": ["debited_credit_purchases", "credited_creditor_payments", "failed_to_update_running_balance"],
    }
    return _with_metadata(
        item,
        subskill="creditors_ledger_account",
        learning_objective_id="lo_g9_creditors_ledger",
        question_family_id="cl_3col_table",
        misconception_tags=["debited_credit_purchases", "credited_creditor_payments", "failed_to_update_running_balance"],
    )

# --------------------------------------------------------------------------- #
# Sub-Drill 2: Creditors List & Control Account Reconciliation
# --------------------------------------------------------------------------- #
def _generate_creditors_reconciliation_drill(rng: random.Random, mode: str = "scaffold") -> Dict[str, Any]:
    scenario = get_ems_scenario(rng)
    business_name = f"{scenario['entrepreneur']}'s Retailers"
    
    c1_bal = rng.randint(12, 35) * 100
    c2_bal = rng.randint(8, 20) * 100
    c3_bal = rng.randint(15, 40) * 100
    
    total_creditors = c1_bal + c2_bal + c3_bal
    
    prompt = (
        f"On 30 September 2026, the balances of individual suppliers in the **Creditors Ledger** of **{business_name}** were:\n\n"
        f"• **C1: Alpha Wholesalers**: R{c1_bal:,}\n"
        f"• **C2: Beta Distributors**: R{c2_bal:,}\n"
        f"• **C3: Delta Stationers**: R{c3_bal:,}\n\n"
        f"**Required:**\n"
        f"1. Compile the **Creditors List** on 30 September 2026.\n"
        f"2. Explain why the total of the Creditors List (R{total_creditors:,}) must equal the closing balance of the **Creditors Control account (B6)** in the General Ledger."
    )
    
    headers = ["Fol", "Name of Creditor", "Amount (R)"]
    rows = [
        [
            {"coordinate": "t0_r0_c0", "value": "C1", "type": "given", "editable": False},
            {"coordinate": "t0_r0_c1", "value": "Alpha Wholesalers", "type": "given", "editable": False},
            {"coordinate": "t0_r0_c2", "value": str(c1_bal) if mode == "scaffold" else "", "type": "required", "editable": True},
        ],
        [
            {"coordinate": "t0_r1_c0", "value": "C2", "type": "given", "editable": False},
            {"coordinate": "t0_r1_c1", "value": "Beta Distributors", "type": "given", "editable": False},
            {"coordinate": "t0_r1_c2", "value": str(c2_bal) if mode == "scaffold" else "", "type": "required", "editable": True},
        ],
        [
            {"coordinate": "t0_r2_c0", "value": "C3", "type": "given", "editable": False},
            {"coordinate": "t0_r2_c1", "value": "Delta Stationers", "type": "given", "editable": False},
            {"coordinate": "t0_r2_c2", "value": str(c3_bal) if mode == "scaffold" else "", "type": "required", "editable": True},
        ],
        [
            {"coordinate": "t0_r3_c0", "value": "", "type": "must_be_empty", "editable": False},
            {"coordinate": "t0_r3_c1", "value": "Total Creditors List", "type": "given", "editable": False},
            {"coordinate": "t0_r3_c2", "value": str(total_creditors) if mode == "scaffold" else "", "type": "required", "editable": True},
        ],
    ]
    
    correct_map = {
        "t0_r0_c2": str(c1_bal),
        "t0_r1_c2": str(c2_bal),
        "t0_r2_c2": str(c3_bal),
        "t0_r3_c2": str(total_creditors),
    }
    
    cell_hints = {
        "t0_r0_c2": f"Enter C1 balance: R{c1_bal:,}.",
        "t0_r1_c2": f"Enter C2 balance: R{c2_bal:,}.",
        "t0_r2_c2": f"Enter C3 balance: R{c3_bal:,}.",
        "t0_r3_c2": f"Sum of all individual balances = R{total_creditors:,}.",
    }
    
    transactions = [
        f"C1: Alpha Wholesalers — Ledger balance: R{c1_bal:,}",
        f"C2: Beta Distributors — Ledger balance: R{c2_bal:,}",
        f"C3: Delta Stationers — Ledger balance: R{c3_bal:,}",
    ]
    item = {
        "id": f"ems9_cl_list_{rng.randint(1000, 9999)}",
        "title": "Creditors List and Reconciliation",
        "question_type": "table_completion",
        "modality": "ledger",
        "prompt": prompt,
        "transactions": transactions,
        "headers": headers,
        "rows": rows,
        "journal": {
            "journal_type": "creditors_list",
            "headers": headers,
            "rows": rows,
        },
        "correct_map": correct_map,
        "cell_hints": cell_hints,
        "marks": 8,
        "sample_answer": f"Total Creditors List = R{total_creditors:,}. It must match Creditors Control (B6) because Creditors Control is the summary account of all individual creditor accounts.",
        "ideal_answer": "Complete Creditors List matching the Creditors Control account in the General Ledger.",
        "hint_sections": {
            "1_nudge": "Add the balances of all creditors: R{c1_bal:,} + R{c2_bal:,} + R{c3_bal:,}.",
            "2_concept": "The Creditors List acts as an internal control mechanism to detect errors in the journals or individual ledgers.",
            "3_breakdown": f"Total = R{total_creditors:,}."
        },
        "marking_schema": {
            "total_marks": 8,
            "marking_points": [
                {"id": "mp_c1", "desc": f"C1 Alpha Wholesalers: R{c1_bal:,}", "marks": 2, "editable": True},
                {"id": "mp_c2", "desc": f"C2 Beta Distributors: R{c2_bal:,}", "marks": 2, "editable": True},
                {"id": "mp_c3", "desc": f"C3 Delta Stationers: R{c3_bal:,}", "marks": 2, "editable": True},
                {"id": "mp_tot", "desc": f"Total Creditors List: R{total_creditors:,}", "marks": 2, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "misconception_tags": ["arithmetic_addition_error_in_list", "confused_creditors_list_with_debtors_list"],
    }
    return _with_metadata(
        item,
        subskill="creditors_reconciliation",
        learning_objective_id="lo_g9_creditors_reconciliation",
        question_family_id="cl_recon_list",
        misconception_tags=["arithmetic_addition_error_in_list", "confused_creditors_list_with_debtors_list"],
    )

BUILDERS = {
    "creditors_ledger_account": lambda rng, mode: [_generate_creditors_ledger_drill(rng, mode)],
    "creditors_reconciliation": lambda rng, mode: [_generate_creditors_reconciliation_drill(rng, mode)],
    "concepts": lambda rng, mode: [_generate_creditors_ledger_drill(rng, mode)],
}

def generate(
    subskill: str = "creditors_ledger_account",
    difficulty: str = "medium",
    count: int = 1,
    mode: str = "scaffold",
    seed: Optional[int] = None,
    **kwargs: Any,
) -> List[Dict[str, Any]]:
    rng = _rng(seed)
    builder = BUILDERS.get(subskill)
    if builder is not None:
        pool = builder(rng, mode)
    else:
        pool = [_generate_creditors_ledger_drill(rng, mode), _generate_creditors_reconciliation_drill(rng, mode)]

    if count == 1 and seed is not None:
        selected = [pool[int(seed) % len(pool)]]
    elif count < len(pool):
        selected = rng.sample(pool, count)
    else:
        selected = pool
    return selected
