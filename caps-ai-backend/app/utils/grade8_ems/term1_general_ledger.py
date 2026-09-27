"""Grade 8 EMS — General Ledger & Trial Balance of a Service Business.
100% Deterministic & SymPy/math backed. Satisfies the 6-Pillar Generator Contract.
Directly aligns with `curriculum_docs_auto/EMS_Gr8/Term 1/01. General ledger and Trial balance of a service business.md`.
Covers:
- Double-entry principles & DEAD CLIC account behavior
- Posting CRJ and CPJ totals to General Ledger T-accounts
- Balancing ledger accounts (balance c/d and balance b/d)
- Preparation of the Trial Balance (Balance Sheet Section B vs Nominal Section N)
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


TOPIC_ID = "grade8_ems"
SUBTOPIC_ID = "term1_general_ledger"
CURRICULUM_REFERENCE = "Term 1 > General Ledger and Trial Balance of a Service Business"


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
        "concept_group": concept_group or "general_ledger",
        "question_family_id": question_family_id,
        "curriculum_reference": CURRICULUM_REFERENCE,
        "misconception_tags": misconception_tags or [],
        "diagnostic_tags": diagnostic_tags or ["accounting", "ledger"],
    })
    return enriched


# --------------------------------------------------------------------------- #
# Sub-Drill 1: DEAD CLIC Double-Entry Rule Classification
# --------------------------------------------------------------------------- #
def _build_dead_clic_drill(r: random.Random, mode: str = "scaffold") -> Dict[str, Any]:
    accounts_pool = [
        {"account": "Bank (Asset)", "type": "Asset", "rule": "DEAD", "normal": "Debit", "increase": "Debit", "decrease": "Credit"},
        {"account": "Capital (Owner's Equity)", "type": "Owner's Equity", "rule": "CLIC", "normal": "Credit", "increase": "Credit", "decrease": "Debit"},
        {"account": "Current Income (Income)", "type": "Income", "rule": "CLIC", "normal": "Credit", "increase": "Credit", "decrease": "Debit"},
        {"account": "Wages (Expense)", "type": "Expense", "rule": "DEAD", "normal": "Debit", "increase": "Debit", "decrease": "Credit"},
        {"account": "Stationery (Expense)", "type": "Expense", "rule": "DEAD", "normal": "Debit", "increase": "Debit", "decrease": "Credit"},
        {"account": "Drawings (Owner's Equity decrease)", "type": "Drawings", "rule": "DEAD", "normal": "Debit", "increase": "Debit", "decrease": "Credit"},
        {"account": "Equipment (Asset)", "type": "Asset", "rule": "DEAD", "normal": "Debit", "increase": "Debit", "decrease": "Credit"},
        {"account": "Rent Income (Income)", "type": "Income", "rule": "CLIC", "normal": "Credit", "increase": "Credit", "decrease": "Debit"},
        {"account": "Loan from ABC Bank (Liability)", "type": "Liability", "rule": "CLIC", "normal": "Credit", "increase": "Credit", "decrease": "Debit"},
    ]
    selected = r.sample(accounts_pool, 3)

    transactions = [
        f"1. {selected[0]['account']}",
        f"2. {selected[1]['account']}",
        f"3. {selected[2]['account']}",
    ]

    headers = ["No.", "Account Name", "Rule Group (DEAD / CLIC)", "Normal Balance Side", "Side to Record Increase"]
    rows = []
    correct_map: Dict[str, str] = {}
    cell_hints: Dict[str, str] = {}

    for idx, acc in enumerate(selected):
        correct_map[f"t0_r{idx}_c2"] = acc["rule"]
        correct_map[f"t0_r{idx}_c3"] = acc["normal"]
        correct_map[f"t0_r{idx}_c4"] = acc["increase"]

        cell_hints[f"t0_r{idx}_c2"] = f"Determine whether {acc['account']} falls under DEAD (Drawings, Expenses, Assets, Debtors) or CLIC (Capital, Liabilities, Income, Creditors)."
        cell_hints[f"t0_r{idx}_c3"] = f"{acc['rule']} accounts have a normal balance on the {acc['normal']} side."
        cell_hints[f"t0_r{idx}_c4"] = f"Accounts increase on their normal balance side ({acc['increase']})."

        rows.append([
            {"coordinate": f"t0_r{idx}_c0", "value": str(idx + 1), "type": "given", "editable": False},
            {"coordinate": f"t0_r{idx}_c1", "value": acc["account"], "type": "given", "editable": False},
            {"coordinate": f"t0_r{idx}_c2", "value": acc["rule"] if mode == "scaffold" else "", "type": "required", "editable": True},
            {"coordinate": f"t0_r{idx}_c3", "value": acc["normal"] if mode == "scaffold" else "", "type": "required", "editable": True},
            {"coordinate": f"t0_r{idx}_c4", "value": acc["increase"] if mode == "scaffold" else "", "type": "required", "editable": True},
        ])

    item = {
        "id": f"g8_gl_deadclic_{r.randint(1000, 9999)}",
        "title": "DEAD CLIC Double-Entry Rules",
        "question_type": "table_completion",
        "prompt": "Apply the double-entry rule mnemonic **DEAD CLIC** to determine the behavior of the following General Ledger accounts.",
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "cell_hints": cell_hints,
        "marks": 9,
        "sample_answer": f"Row 1: {selected[0]['rule']}, {selected[0]['normal']}, {selected[0]['increase']}",
        "ideal_answer": "All accounts correctly classified under DEAD or CLIC with matching debit/credit sides.",
        "hint_sections": {
            "1_nudge": "DEAD accounts (Drawings, Expenses, Assets, Debtors) increase on the DEBIT side.",
            "2_concept": "CLIC accounts (Capital, Liabilities, Income, Creditors) increase on the CREDIT side.",
            "3_breakdown": f"{selected[0]['account']} is a {selected[0]['type']}, belonging to {selected[0]['rule']}."
        },
        "marking_schema": {
            "total_marks": 9,
            "marking_points": [
                {"id": f"mp_{i}", "desc": f"Classification for {acc['account']}", "marks": 3, "editable": True}
                for i, acc in enumerate(selected)
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "misconception_tags": ["confuses_debit_and_credit", "dead_clic_rule_inversion"],
    }
    return _with_metadata(
        item,
        subskill="dead_clic",
        learning_objective_id="lo_g8_dead_clic",
        question_family_id="dead_clic_table",
        misconception_tags=["confuses_debit_and_credit", "dead_clic_rule_inversion"],
    )


# --------------------------------------------------------------------------- #
# Sub-Drill 2: Balancing a General Ledger T-Account
# --------------------------------------------------------------------------- #
def _build_balancing_drill(r: random.Random, mode: str = "scaffold") -> Dict[str, Any]:
    scenario = get_ems_scenario(r)
    opening_bal = r.randint(8, 25) * 1000
    crj_total = r.randint(15, 35) * 1000
    cpj_total = r.randint(10, 25) * 1000
    total_debit = opening_bal + crj_total
    closing_bal = total_debit - cpj_total

    prompt = (
        f"The Bank account in the General Ledger of **{scenario['entrepreneur']}'s {scenario['business_type']}** "
        f"reflects the following monthly totals for May:\n\n"
        f"• May 1: Opening balance (Debit): R{opening_bal:,}\n"
        f"• May 31: Total receipts per CRJ: R{crj_total:,}\n"
        f"• May 31: Total payments per CPJ: R{cpj_total:,}\n\n"
        f"Balance the Bank account at the end of May. Enter the 'Balance c/d' on the smaller side and bring it down "
        f"as 'Balance b/d' on June 1."
    )

    headers = ["Day", "Details (Debit)", "Amount (R)", "Day", "Details (Credit)", "Amount (R)"]
    rows = [
        [
            {"coordinate": "t0_r0_c0", "value": "1", "type": "given", "editable": False},
            {"coordinate": "t0_r0_c1", "value": "Balance b/d", "type": "given", "editable": False},
            {"coordinate": "t0_r0_c2", "value": str(opening_bal), "type": "given", "editable": False},
            {"coordinate": "t0_r0_c3", "value": "31", "type": "given", "editable": False},
            {"coordinate": "t0_r0_c4", "value": "Total Payments (CPJ)", "type": "given", "editable": False},
            {"coordinate": "t0_r0_c5", "value": str(cpj_total), "type": "given", "editable": False},
        ],
        [
            {"coordinate": "t0_r1_c0", "value": "31", "type": "given", "editable": False},
            {"coordinate": "t0_r1_c1", "value": "Total Receipts (CRJ)", "type": "given", "editable": False},
            {"coordinate": "t0_r1_c2", "value": str(crj_total), "type": "given", "editable": False},
            {"coordinate": "t0_r1_c3", "value": "31", "type": "required", "editable": True},
            {"coordinate": "t0_r1_c4", "value": "Balance c/d", "type": "required", "editable": True},
            {"coordinate": "t0_r1_c5", "value": str(closing_bal), "type": "required", "editable": True},
        ],
        [
            {"coordinate": "t0_r2_c0", "value": "", "type": "must_be_empty", "editable": False},
            {"coordinate": "t0_r2_c1", "value": "Total", "type": "given", "editable": False},
            {"coordinate": "t0_r2_c2", "value": str(total_debit), "type": "required", "editable": True},
            {"coordinate": "t0_r2_c3", "value": "", "type": "must_be_empty", "editable": False},
            {"coordinate": "t0_r2_c4", "value": "Total", "type": "given", "editable": False},
            {"coordinate": "t0_r2_c5", "value": str(total_debit), "type": "required", "editable": True},
        ],
        [
            {"coordinate": "t0_r3_c0", "value": "Jun 1", "type": "required", "editable": True},
            {"coordinate": "t0_r3_c1", "value": "Balance b/d", "type": "required", "editable": True},
            {"coordinate": "t0_r3_c2", "value": str(closing_bal), "type": "required", "editable": True},
            {"coordinate": "t0_r3_c3", "value": "", "type": "must_be_empty", "editable": False},
            {"coordinate": "t0_r3_c4", "value": "", "type": "must_be_empty", "editable": False},
            {"coordinate": "t0_r3_c5", "value": "", "type": "must_be_empty", "editable": False},
        ],
    ]

    correct_map: Dict[str, str] = {
        "t0_r1_c3": "31",
        "t0_r1_c4": "Balance c/d",
        "t0_r1_c5": str(closing_bal),
        "t0_r2_c2": str(total_debit),
        "t0_r2_c5": str(total_debit),
        "t0_r3_c0": "Jun 1",
        "t0_r3_c1": "Balance b/d",
        "t0_r3_c2": str(closing_bal),
    }

    cell_hints: Dict[str, str] = {
        "t0_r1_c4": "Write 'Balance c/d' on the smaller side so both sides add up to the same total.",
        "t0_r1_c5": f"Difference between total debits (R{total_debit:,}) and payments (R{cpj_total:,}) is R{closing_bal:,}.",
        "t0_r2_c2": f"Enter the larger total (R{total_debit:,}) on both sides.",
        "t0_r2_c5": f"Enter the larger total (R{total_debit:,}) on both sides.",
        "t0_r3_c1": "Bring the balance down to the opposite side under the total as 'Balance b/d'.",
        "t0_r3_c2": f"Opening balance for next month is R{closing_bal:,}.",
    }

    item = {
        "id": f"g8_gl_balance_{r.randint(1000, 9999)}",
        "title": "Balancing the Bank Account",
        "question_type": "table_completion",
        "prompt": prompt,
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "cell_hints": cell_hints,
        "marks": 8,
        "sample_answer": f"Balance c/d: R{closing_bal:,}; Total: R{total_debit:,}; Balance b/d: R{closing_bal:,}",
        "ideal_answer": "Complete T-account balanced with correct c/d and b/d lines.",
        "hint_sections": {
            "1_nudge": "Add up both sides. The Debit side is larger. Write the larger total on both sides.",
            "2_concept": "Subtract the smaller side from the larger side to get Balance c/d.",
            "3_breakdown": f"Total Debit = R{total_debit:,}. Balance c/d = R{total_debit:,} - R{cpj_total:,} = R{closing_bal:,}. Bring down as Balance b/d = R{closing_bal:,}."
        },
        "marking_schema": {
            "total_marks": 8,
            "marking_points": [
                {"id": "mp_cd", "desc": "Correct Balance c/d calculation and side", "marks": 3, "editable": True},
                {"id": "mp_tot", "desc": "Both sides totalled correctly", "marks": 2, "editable": True},
                {"id": "mp_bd", "desc": "Balance b/d brought down on Debit side", "marks": 3, "editable": True},
            ],
            "deductions": [{"rule": "must_be_empty_filled", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
        "misconception_tags": ["inverted_cd_bd_sides", "subtraction_error_in_balancing"],
    }
    return _with_metadata(
        item,
        subskill="balancing_accounts",
        learning_objective_id="lo_g8_balancing_t_accounts",
        question_family_id="t_account_balancing",
        misconception_tags=["inverted_cd_bd_sides", "subtraction_error_in_balancing"],
    )


# --------------------------------------------------------------------------- #
# Sub-Drill 3: Completing the Trial Balance of a Service Business
# --------------------------------------------------------------------------- #
def _build_trial_balance_drill(r: random.Random, mode: str = "scaffold") -> Dict[str, Any]:
    scenario = get_ems_scenario(r)
    capital = r.randint(40, 80) * 1000
    drawings = r.randint(3, 8) * 1000
    current_income = r.randint(30, 60) * 1000
    rent_income = r.randint(5, 12) * 1000
    wages = r.randint(10, 20) * 1000
    stationery = r.randint(2, 5) * 1000
    equipment = r.randint(15, 30) * 1000

    # Total credits = Capital + Current Income + Rent Income
    total_credit = capital + current_income + rent_income
    # Bank debit is whatever balances the Trial Balance
    # Total debit = Bank + Drawings + Equipment + Wages + Stationery
    debit_known = drawings + equipment + wages + stationery
    bank_bal = total_credit - debit_known

    prompt = (
        f"Prepare the **Trial Balance** of **{scenario['entrepreneur']}'s Services** on 31 May 2026. "
        f"Assign each account to either the Debit or Credit column according to DEAD CLIC and calculate the totals."
    )

    headers = ["Fol", "Account", "Debit (R)", "Credit (R)"]

    items_data = [
        # Balance Sheet Accounts Section
        ("B1", "Capital", "", str(capital), "CLIC (Capital increases on Credit)"),
        ("B2", "Drawings", str(drawings), "", "DEAD (Drawings normal balance is Debit)"),
        ("B3", "Equipment", str(equipment), "", "DEAD (Asset normal balance is Debit)"),
        ("B4", "Bank", str(bank_bal), "", "DEAD (Asset normal balance is Debit)"),
        # Nominal Accounts Section
        ("N1", "Current Income", "", str(current_income), "CLIC (Income normal balance is Credit)"),
        ("N2", "Rent Income", "", str(rent_income), "CLIC (Income normal balance is Credit)"),
        ("N3", "Wages", str(wages), "", "DEAD (Expense normal balance is Debit)"),
        ("N4", "Stationery", str(stationery), "", "DEAD (Expense normal balance is Debit)"),
    ]

    rows = []
    correct_map: Dict[str, str] = {}
    cell_hints: Dict[str, str] = {}

    for rix, (fol, name, deb, cred, hint_reason) in enumerate(items_data):
        coord_deb = f"t0_r{rix}_c2"
        coord_cred = f"t0_r{rix}_c3"

        correct_map[coord_deb] = deb
        correct_map[coord_cred] = cred

        cell_hints[coord_deb] = f"If {name} is a Debit balance account, enter R{deb} here. {hint_reason}."
        cell_hints[coord_cred] = f"If {name} is a Credit balance account, enter R{cred} here. {hint_reason}."

        rows.append([
            {"coordinate": f"t0_r{rix}_c0", "value": fol, "type": "given", "editable": False},
            {"coordinate": f"t0_r{rix}_c1", "value": name, "type": "given", "editable": False},
            {"coordinate": coord_deb, "value": deb if mode == "scaffold" else "", "type": "must_be_empty" if deb == "" else "required", "editable": True},
            {"coordinate": coord_cred, "value": cred if mode == "scaffold" else "", "type": "must_be_empty" if cred == "" else "required", "editable": True},
        ])

    # Totals Row
    tot_rix = len(items_data)
    correct_map[f"t0_r{tot_rix}_c2"] = str(total_credit)
    correct_map[f"t0_r{tot_rix}_c3"] = str(total_credit)
    cell_hints[f"t0_r{tot_rix}_c2"] = f"Total of Debit column must equal R{total_credit:,}."
    cell_hints[f"t0_r{tot_rix}_c3"] = f"Total of Credit column must equal R{total_credit:,}."

    rows.append([
        {"coordinate": f"t0_r{tot_rix}_c0", "value": "", "type": "must_be_empty", "editable": False},
        {"coordinate": f"t0_r{tot_rix}_c1", "value": "Total", "type": "given", "editable": False},
        {"coordinate": f"t0_r{tot_rix}_c2", "value": str(total_credit) if mode == "scaffold" else "", "type": "required", "editable": True},
        {"coordinate": f"t0_r{tot_rix}_c3", "value": str(total_credit) if mode == "scaffold" else "", "type": "required", "editable": True},
    ])

    item = {
        "id": f"g8_tb_{r.randint(1000, 9999)}",
        "title": "Trial Balance of a Service Business",
        "question_type": "table_completion",
        "prompt": prompt,
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "cell_hints": cell_hints,
        "marks": 16,
        "sample_answer": f"Total Debits = Total Credits = R{total_credit:,}",
        "ideal_answer": "All 8 accounts correctly allocated to Debit or Credit columns and columns balanced.",
        "hint_sections": {
            "1_nudge": "Remember DEAD (Drawings, Expenses, Assets) on the Debit side, and CLIC (Capital, Liabilities, Income) on the Credit side.",
            "2_concept": "The Trial Balance checks the mathematical accuracy of the General Ledger: Total Debits = Total Credits.",
            "3_breakdown": f"Debits: Drawings R{drawings:,}, Equipment R{equipment:,}, Bank R{bank_bal:,}, Wages R{wages:,}, Stationery R{stationery:,} = R{total_credit:,}. Credits: Capital R{capital:,}, Current Income R{current_income:,}, Rent Income R{rent_income:,} = R{total_credit:,}."
        },
        "marking_schema": {
            "total_marks": 16,
            "marking_points": [
                {"id": f"mp_{name}", "desc": f"{name} in correct column", "marks": 1, "editable": True}
                for _, name, _, _, _ in items_data
            ] + [
                {"id": "mp_debit_total", "desc": f"Correct Debit Total: R{total_credit:,}", "marks": 4, "editable": True},
                {"id": "mp_credit_total", "desc": f"Correct Credit Total: R{total_credit:,}", "marks": 4, "editable": True},
            ],
            "deductions": [{"rule": "must_be_empty_filled", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
        "misconception_tags": ["trial_balance_debit_credit_inversion", "confuses_income_and_expense_columns"],
    }
    return _with_metadata(
        item,
        subskill="trial_balance",
        learning_objective_id="lo_g8_trial_balance",
        question_family_id="trial_balance_table",
        misconception_tags=["trial_balance_debit_credit_inversion", "confuses_income_and_expense_columns"],
    )


# --------------------------------------------------------------------------- #
# Public Dispatcher
# --------------------------------------------------------------------------- #
BUILDERS = {
    "dead_clic": _build_dead_clic_drill,
    "balancing_accounts": _build_balancing_drill,
    "trial_balance": _build_trial_balance_drill,
    "concepts": _build_dead_clic_drill,
}


def generate(
    subskill: str = "dead_clic",
    difficulty: str = "medium",
    count: int = 1,
    mode: str = "scaffold",
    seed: Optional[int] = None,
    **kwargs: Any,
) -> List[Dict[str, Any]]:
    r = _rng(seed)
    builder = BUILDERS.get(subskill, _build_dead_clic_drill)
    questions = []
    for i in range(max(1, count)):
        sub_seed = None if seed is None else seed * 100 + i
        sub_r = _rng(sub_seed)
        q = builder(sub_r, mode=mode)
        questions.append(q)
    return questions
