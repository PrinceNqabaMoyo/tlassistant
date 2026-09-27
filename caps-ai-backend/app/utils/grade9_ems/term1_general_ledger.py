"""Grade 9 EMS — General Ledger & Trial Balance of a Trading Business.
100% Deterministic & SymPy/math backed. Satisfies the 6-Pillar Generator Contract.
Directly aligns with `curriculum_docs_auto/EMS_Gr9/Term 2/03. General ledger and Trial balance (sole trader).md`.
Covers:
- General Ledger Bank T-account posting & balancing
- General Ledger Trading Stock T-account (Purchases vs Cost of Sales)
- Trial Balance of a Trading Business (Balance Sheet accounts B vs Nominal accounts N)
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
SUBTOPIC_ID = "term1_general_ledger"
CURRICULUM_REFERENCE = "Term 1/2 > General Ledger and Trial Balance of a Sole Trader"


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
# Sub-Drill 1: Bank Account T-Account Posting & Balancing
# --------------------------------------------------------------------------- #
def _generate_bank_ledger(rng: random.Random, mode: str = "scaffold") -> Dict[str, Any]:
    scenario = get_ems_scenario(rng)
    business_name = f"{scenario['entrepreneur']}'s Trading Store"
    month = "May 2026"

    opening_bal = rng.randint(10, 30) * 1000
    crj_bank = rng.randint(40, 90) * 1000
    cpj_bank = rng.randint(30, 70) * 1000
    total_debit = opening_bal + crj_bank
    closing_bal = total_debit - cpj_bank

    prompt = (
        f"Post the monthly totals from the cash journals to the **Bank account** in the General Ledger "
        f"of **{business_name}** for {month}, and balance the account on 31 May.\n\n"
        f"• 1 May 2026: Balance b/d: R{opening_bal:,}\n"
        f"• 31 May 2026: Total receipts per CRJ: R{crj_bank:,}\n"
        f"• 31 May 2026: Total payments per CPJ: R{cpj_bank:,}"
    )

    headers = ["Day", "Details (Debit)", "Fol", "Amount (R)", "Day", "Details (Credit)", "Fol", "Amount (R)"]

    rows = [
        [
            {"coordinate": "t0_r0_c0", "value": "1", "type": "given", "editable": False},
            {"coordinate": "t0_r0_c1", "value": "Balance", "type": "given", "editable": False},
            {"coordinate": "t0_r0_c2", "value": "b/d", "type": "given", "editable": False},
            {"coordinate": "t0_r0_c3", "value": str(opening_bal), "type": "given", "editable": False},
            {"coordinate": "t0_r0_c4", "value": "31", "type": "given", "editable": False},
            {"coordinate": "t0_r0_c5", "value": "Total Payments", "type": "given", "editable": False},
            {"coordinate": "t0_r0_c6", "value": "CPJ", "type": "given", "editable": False},
            {"coordinate": "t0_r0_c7", "value": str(cpj_bank), "type": "given", "editable": False},
        ],
        [
            {"coordinate": "t0_r1_c0", "value": "31", "type": "given", "editable": False},
            {"coordinate": "t0_r1_c1", "value": "Total Receipts", "type": "given", "editable": False},
            {"coordinate": "t0_r1_c2", "value": "CRJ", "type": "given", "editable": False},
            {"coordinate": "t0_r1_c3", "value": str(crj_bank), "type": "given", "editable": False},
            {"coordinate": "t0_r1_c4", "value": "31", "type": "required", "editable": True},
            {"coordinate": "t0_r1_c5", "value": "Balance", "type": "required", "editable": True},
            {"coordinate": "t0_r1_c6", "value": "c/d", "type": "required", "editable": True},
            {"coordinate": "t0_r1_c7", "value": str(closing_bal), "type": "required", "editable": True},
        ],
        [
            {"coordinate": "t0_r2_c0", "value": "", "type": "must_be_empty", "editable": False},
            {"coordinate": "t0_r2_c1", "value": "Total", "type": "given", "editable": False},
            {"coordinate": "t0_r2_c2", "value": "", "type": "must_be_empty", "editable": False},
            {"coordinate": "t0_r2_c3", "value": str(total_debit), "type": "required", "editable": True},
            {"coordinate": "t0_r2_c4", "value": "", "type": "must_be_empty", "editable": False},
            {"coordinate": "t0_r2_c5", "value": "Total", "type": "given", "editable": False},
            {"coordinate": "t0_r2_c6", "value": "", "type": "must_be_empty", "editable": False},
            {"coordinate": "t0_r2_c7", "value": str(total_debit), "type": "required", "editable": True},
        ],
        [
            {"coordinate": "t0_r3_c0", "value": "Jun 1", "type": "required", "editable": True},
            {"coordinate": "t0_r3_c1", "value": "Balance", "type": "required", "editable": True},
            {"coordinate": "t0_r3_c2", "value": "b/d", "type": "required", "editable": True},
            {"coordinate": "t0_r3_c3", "value": str(closing_bal), "type": "required", "editable": True},
            {"coordinate": "t0_r3_c4", "value": "", "type": "must_be_empty", "editable": False},
            {"coordinate": "t0_r3_c5", "value": "", "type": "must_be_empty", "editable": False},
            {"coordinate": "t0_r3_c6", "value": "", "type": "must_be_empty", "editable": False},
            {"coordinate": "t0_r3_c7", "value": "", "type": "must_be_empty", "editable": False},
        ],
    ]

    correct_map = {
        "t0_r1_c4": "31",
        "t0_r1_c5": "Balance",
        "t0_r1_c6": "c/d",
        "t0_r1_c7": str(closing_bal),
        "t0_r2_c3": str(total_debit),
        "t0_r2_c7": str(total_debit),
        "t0_r3_c0": "Jun 1",
        "t0_r3_c1": "Balance",
        "t0_r3_c2": "b/d",
        "t0_r3_c3": str(closing_bal),
    }

    cell_hints = {
        "t0_r1_c5": "Balance c/d on the credit side reconciles the account.",
        "t0_r1_c7": f"Balance c/d = Total Debit (R{total_debit:,}) - CPJ Payments (R{cpj_bank:,}) = R{closing_bal:,}.",
        "t0_r2_c3": f"Total of larger side = R{total_debit:,}.",
        "t0_r2_c7": f"Total of larger side = R{total_debit:,}.",
        "t0_r3_c3": f"Opening balance on June 1 = R{closing_bal:,}.",
    }

    item = {
        "id": f"ems9_gl_bank_{rng.randint(1000, 9999)}",
        "title": "General Ledger - Bank Account",
        "question_type": "table_completion",
        "prompt": prompt,
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "cell_hints": cell_hints,
        "marks": 10,
        "sample_answer": f"Balance c/d: R{closing_bal:,}; Total: R{total_debit:,}; Balance b/d on Jun 1: R{closing_bal:,}",
        "ideal_answer": "Complete General Ledger Bank account balanced with correct c/d and b/d lines.",
        "hint_sections": {
            "1_nudge": "Bank is an asset. Money received increases Bank on the Debit side; payments decrease on Credit.",
            "2_concept": "To balance the account, enter Balance c/d on the credit side so both sides add up to R{total_debit:,}.",
            "3_breakdown": f"Closing balance = R{total_debit:,} - R{cpj_bank:,} = R{closing_bal:,}."
        },
        "marking_schema": {
            "total_marks": 10,
            "marking_points": [
                {"id": "mp_cd", "desc": f"Balance c/d: R{closing_bal:,}", "marks": 4, "editable": True},
                {"id": "mp_tot", "desc": f"Total: R{total_debit:,}", "marks": 2, "editable": True},
                {"id": "mp_bd", "desc": f"Balance b/d: R{closing_bal:,}", "marks": 4, "editable": True},
            ],
            "deductions": [{"rule": "must_be_empty_filled", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
        "misconception_tags": ["inverted_cd_bd_sides", "subtraction_error_in_balancing"],
    }
    return _with_metadata(
        item,
        subskill="bank_ledger",
        learning_objective_id="lo_g9_gl_bank",
        question_family_id="gl_bank_table",
        misconception_tags=["inverted_cd_bd_sides", "subtraction_error_in_balancing"],
    )


# --------------------------------------------------------------------------- #
# Sub-Drill 2: Trading Stock T-Account
# --------------------------------------------------------------------------- #
def _generate_trading_stock_ledger(rng: random.Random, mode: str = "scaffold") -> Dict[str, Any]:
    scenario = get_ems_scenario(rng)
    opening_stock = rng.randint(20, 50) * 1000
    cash_purchases = rng.randint(15, 35) * 1000
    credit_purchases = rng.randint(10, 25) * 1000
    cost_of_sales = rng.randint(25, 60) * 1000
    total_debit = opening_stock + cash_purchases + credit_purchases
    closing_stock = total_debit - cost_of_sales

    prompt = (
        f"Complete the **Trading Stock account (B5)** in the General Ledger of **{scenario['entrepreneur']}'s Store** "
        f"for May 2026 and balance the account at month-end.\n\n"
        f"• 1 May: Opening stock on hand (Debit): R{opening_stock:,}\n"
        f"• 31 May: Cash purchases of stock per CPJ: R{cash_purchases:,}\n"
        f"• 31 May: Credit purchases of stock per CJ: R{credit_purchases:,}\n"
        f"• 31 May: Total Cost of Sales for the month (CRJ + DJ): R{cost_of_sales:,}"
    )

    headers = ["Day", "Details (Debit)", "Fol", "Amount (R)", "Day", "Details (Credit)", "Fol", "Amount (R)"]

    rows = [
        [
            {"coordinate": "t0_r0_c0", "value": "1", "type": "given", "editable": False},
            {"coordinate": "t0_r0_c1", "value": "Balance", "type": "given", "editable": False},
            {"coordinate": "t0_r0_c2", "value": "b/d", "type": "given", "editable": False},
            {"coordinate": "t0_r0_c3", "value": str(opening_stock), "type": "given", "editable": False},
            {"coordinate": "t0_r0_c4", "value": "31", "type": "given", "editable": False},
            {"coordinate": "t0_r0_c5", "value": "Cost of Sales", "type": "given", "editable": False},
            {"coordinate": "t0_r0_c6", "value": "CRJ/DJ", "type": "given", "editable": False},
            {"coordinate": "t0_r0_c7", "value": str(cost_of_sales), "type": "given", "editable": False},
        ],
        [
            {"coordinate": "t0_r1_c0", "value": "31", "type": "given", "editable": False},
            {"coordinate": "t0_r1_c1", "value": "Bank", "type": "given", "editable": False},
            {"coordinate": "t0_r1_c2", "value": "CPJ", "type": "given", "editable": False},
            {"coordinate": "t0_r1_c3", "value": str(cash_purchases), "type": "given", "editable": False},
            {"coordinate": "t0_r1_c4", "value": "31", "type": "required", "editable": True},
            {"coordinate": "t0_r1_c5", "value": "Balance", "type": "required", "editable": True},
            {"coordinate": "t0_r1_c6", "value": "c/d", "type": "required", "editable": True},
            {"coordinate": "t0_r1_c7", "value": str(closing_stock), "type": "required", "editable": True},
        ],
        [
            {"coordinate": "t0_r2_c0", "value": "31", "type": "given", "editable": False},
            {"coordinate": "t0_r2_c1", "value": "Creditors Control", "type": "given", "editable": False},
            {"coordinate": "t0_r2_c2", "value": "CJ", "type": "given", "editable": False},
            {"coordinate": "t0_r2_c3", "value": str(credit_purchases), "type": "given", "editable": False},
            {"coordinate": "t0_r2_c4", "value": "", "type": "must_be_empty", "editable": False},
            {"coordinate": "t0_r2_c5", "value": "", "type": "must_be_empty", "editable": False},
            {"coordinate": "t0_r2_c6", "value": "", "type": "must_be_empty", "editable": False},
            {"coordinate": "t0_r2_c7", "value": "", "type": "must_be_empty", "editable": False},
        ],
        [
            {"coordinate": "t0_r3_c0", "value": "", "type": "must_be_empty", "editable": False},
            {"coordinate": "t0_r3_c1", "value": "Total", "type": "given", "editable": False},
            {"coordinate": "t0_r3_c2", "value": "", "type": "must_be_empty", "editable": False},
            {"coordinate": "t0_r3_c3", "value": str(total_debit), "type": "required", "editable": True},
            {"coordinate": "t0_r3_c4", "value": "", "type": "must_be_empty", "editable": False},
            {"coordinate": "t0_r3_c5", "value": "Total", "type": "given", "editable": False},
            {"coordinate": "t0_r3_c6", "value": "", "type": "must_be_empty", "editable": False},
            {"coordinate": "t0_r3_c7", "value": str(total_debit), "type": "required", "editable": True},
        ],
        [
            {"coordinate": "t0_r4_c0", "value": "Jun 1", "type": "required", "editable": True},
            {"coordinate": "t0_r4_c1", "value": "Balance", "type": "required", "editable": True},
            {"coordinate": "t0_r4_c2", "value": "b/d", "type": "required", "editable": True},
            {"coordinate": "t0_r4_c3", "value": str(closing_stock), "type": "required", "editable": True},
            {"coordinate": "t0_r4_c4", "value": "", "type": "must_be_empty", "editable": False},
            {"coordinate": "t0_r4_c5", "value": "", "type": "must_be_empty", "editable": False},
            {"coordinate": "t0_r4_c6", "value": "", "type": "must_be_empty", "editable": False},
            {"coordinate": "t0_r4_c7", "value": "", "type": "must_be_empty", "editable": False},
        ],
    ]

    correct_map = {
        "t0_r1_c4": "31",
        "t0_r1_c5": "Balance",
        "t0_r1_c6": "c/d",
        "t0_r1_c7": str(closing_stock),
        "t0_r3_c3": str(total_debit),
        "t0_r3_c7": str(total_debit),
        "t0_r4_c0": "Jun 1",
        "t0_r4_c1": "Balance",
        "t0_r4_c2": "b/d",
        "t0_r4_c3": str(closing_stock),
    }

    cell_hints = {
        "t0_r1_c5": "Enter 'Balance c/d' on the credit side.",
        "t0_r1_c7": f"Closing stock = Total Debit (R{total_debit:,}) - Cost of Sales (R{cost_of_sales:,}) = R{closing_stock:,}.",
        "t0_r3_c3": f"Total = R{total_debit:,}.",
        "t0_r3_c7": f"Total = R{total_debit:,}.",
        "t0_r4_c3": f"Opening stock for June 1 = R{closing_stock:,}.",
    }

    item = {
        "id": f"ems9_gl_stock_{rng.randint(1000, 9999)}",
        "title": "General Ledger - Trading Stock Account",
        "question_type": "table_completion",
        "prompt": prompt,
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "cell_hints": cell_hints,
        "marks": 10,
        "sample_answer": f"Balance c/d: R{closing_stock:,}; Total: R{total_debit:,}; Balance b/d: R{closing_stock:,}",
        "ideal_answer": "Complete Trading Stock T-account showing stock increases on Debit and Cost of Sales on Credit.",
        "hint_sections": {
            "1_nudge": "Trading Stock is an asset. Increases (purchases) go on the Debit side; decreases (Cost of Sales) go on Credit.",
            "2_concept": "Cost of Sales represents the cost price of goods sold that have left the business.",
            "3_breakdown": f"Total stock available = R{total_debit:,}. Minus sold = R{cost_of_sales:,}. Stock on hand = R{closing_stock:,}."
        },
        "marking_schema": {
            "total_marks": 10,
            "marking_points": [
                {"id": "mp_cd", "desc": f"Balance c/d: R{closing_stock:,}", "marks": 4, "editable": True},
                {"id": "mp_tot", "desc": f"Total: R{total_debit:,}", "marks": 2, "editable": True},
                {"id": "mp_bd", "desc": f"Balance b/d: R{closing_stock:,}", "marks": 4, "editable": True},
            ],
            "deductions": [{"rule": "must_be_empty_filled", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
        "misconception_tags": ["credited_purchases_to_stock", "omitted_cost_of_sales_credit"],
    }
    return _with_metadata(
        item,
        subskill="trading_stock_ledger",
        learning_objective_id="lo_g9_gl_trading_stock",
        question_family_id="gl_trading_stock_table",
        misconception_tags=["credited_purchases_to_stock", "omitted_cost_of_sales_credit"],
    )


# --------------------------------------------------------------------------- #
# Sub-Drill 3: Trial Balance of a Trading Business
# --------------------------------------------------------------------------- #
def _generate_trial_balance_trading(rng: random.Random, mode: str = "scaffold") -> Dict[str, Any]:
    scenario = get_ems_scenario(rng)
    capital = rng.randint(60, 120) * 1000
    drawings = rng.randint(4, 10) * 1000
    trading_stock = rng.randint(25, 45) * 1000
    debtors_control = rng.randint(10, 25) * 1000
    creditors_control = rng.randint(15, 30) * 1000
    sales = rng.randint(80, 150) * 1000
    cost_of_sales = int(sales * 0.6) # 40% margin
    rent_income = rng.randint(6, 14) * 1000
    salaries = rng.randint(18, 30) * 1000
    stationery = rng.randint(2, 6) * 1000

    # Total credits = Capital + Creditors Control + Sales + Rent Income
    total_credit = capital + creditors_control + sales + rent_income
    # Debits known = Drawings + Trading Stock + Debtors Control + Cost of Sales + Salaries + Stationery
    debits_known = drawings + trading_stock + debtors_control + cost_of_sales + salaries + stationery
    bank_debit = total_credit - debits_known

    prompt = (
        f"Prepare the **Trial Balance** of **{scenario['entrepreneur']}'s Trading Store** on 31 May 2026. "
        f"Classify each account into the Balance Sheet Accounts Section (B) or Nominal Accounts Section (N), "
        f"place balances in the correct Debit or Credit column, and calculate totals."
    )

    headers = ["Fol", "Account Name", "Debit (R)", "Credit (R)"]

    items_data = [
        ("B1", "Capital", "", str(capital)),
        ("B2", "Drawings", str(drawings), ""),
        ("B3", "Trading Stock", str(trading_stock), ""),
        ("B4", "Debtors Control", str(debtors_control), ""),
        ("B5", "Bank", str(bank_debit), ""),
        ("B6", "Creditors Control", "", str(creditors_control)),
        ("N1", "Sales", "", str(sales)),
        ("N2", "Cost of Sales", str(cost_of_sales), ""),
        ("N3", "Rent Income", "", str(rent_income)),
        ("N4", "Salaries", str(salaries), ""),
        ("N5", "Stationery", str(stationery), ""),
    ]

    rows = []
    correct_map: Dict[str, str] = {}
    cell_hints: Dict[str, str] = {}

    for rix, (fol, name, deb, cred) in enumerate(items_data):
        coord_deb = f"t0_r{rix}_c2"
        coord_cred = f"t0_r{rix}_c3"

        correct_map[coord_deb] = deb
        correct_map[coord_cred] = cred

        cell_hints[coord_deb] = f"Enter on Debit side if {name} has a normal debit balance."
        cell_hints[coord_cred] = f"Enter on Credit side if {name} has a normal credit balance."

        rows.append([
            {"coordinate": f"t0_r{rix}_c0", "value": fol, "type": "given", "editable": False},
            {"coordinate": f"t0_r{rix}_c1", "value": name, "type": "given", "editable": False},
            {"coordinate": coord_deb, "value": deb if mode == "scaffold" else "", "type": "must_be_empty" if deb == "" else "required", "editable": True},
            {"coordinate": coord_cred, "value": cred if mode == "scaffold" else "", "type": "must_be_empty" if cred == "" else "required", "editable": True},
        ])

    tot_rix = len(items_data)
    correct_map[f"t0_r{tot_rix}_c2"] = str(total_credit)
    correct_map[f"t0_r{tot_rix}_c3"] = str(total_credit)
    cell_hints[f"t0_r{tot_rix}_c2"] = f"Total of Debit column = R{total_credit:,}."
    cell_hints[f"t0_r{tot_rix}_c3"] = f"Total of Credit column = R{total_credit:,}."

    rows.append([
        {"coordinate": f"t0_r{tot_rix}_c0", "value": "", "type": "must_be_empty", "editable": False},
        {"coordinate": f"t0_r{tot_rix}_c1", "value": "Total", "type": "given", "editable": False},
        {"coordinate": f"t0_r{tot_rix}_c2", "value": str(total_credit) if mode == "scaffold" else "", "type": "required", "editable": True},
        {"coordinate": f"t0_r{tot_rix}_c3", "value": str(total_credit) if mode == "scaffold" else "", "type": "required", "editable": True},
    ])

    item = {
        "id": f"ems9_tb_trading_{rng.randint(1000, 9999)}",
        "title": "Trial Balance of a Trading Business",
        "question_type": "table_completion",
        "prompt": prompt,
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "cell_hints": cell_hints,
        "marks": 22,
        "sample_answer": f"Total Debits = Total Credits = R{total_credit:,}",
        "ideal_answer": "Complete Trial Balance with correct allocations for Trading Stock, Cost of Sales, and Sales.",
        "hint_sections": {
            "1_nudge": "In a trading business: Trading Stock is an Asset (Debit), Sales is Income (Credit), Cost of Sales is an Expense (Debit).",
            "2_concept": "Check that Total Debits equal Total Credits. If they do not match, recheck your Sales and Cost of Sales sides.",
            "3_breakdown": f"Debits = R{total_credit:,}; Credits = R{total_credit:,}."
        },
        "marking_schema": {
            "total_marks": 22,
            "marking_points": [
                {"id": f"mp_{name}", "desc": f"{name} placed in correct column", "marks": 1, "editable": True}
                for _, name, _, _ in items_data
            ] + [
                {"id": "mp_deb_tot", "desc": f"Correct Debit Total: R{total_credit:,}", "marks": 5, "editable": True},
                {"id": "mp_cred_tot", "desc": f"Correct Credit Total: R{total_credit:,}", "marks": 6, "editable": True},
            ],
            "deductions": [{"rule": "must_be_empty_filled", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
        "misconception_tags": ["inverted_sales_and_cost_of_sales_columns", "trial_balance_debit_credit_inversion"],
    }
    return _with_metadata(
        item,
        subskill="trial_balance",
        learning_objective_id="lo_g9_trial_balance_trading",
        question_family_id="tb_trading_table",
        misconception_tags=["inverted_sales_and_cost_of_sales_columns", "trial_balance_debit_credit_inversion"],
    )


# --------------------------------------------------------------------------- #
# Public Dispatcher
# --------------------------------------------------------------------------- #
BUILDERS = {
    "bank_ledger": lambda rng, mode: [_generate_bank_ledger(rng, mode)],
    "elementary_bank_ledger": lambda rng, mode: [_generate_bank_ledger(rng, mode)],
    "trading_stock_ledger": lambda rng, mode: [_generate_trading_stock_ledger(rng, mode)],
    "elementary_trading_stock_ledger": lambda rng, mode: [_generate_trading_stock_ledger(rng, mode)],
    "trial_balance": lambda rng, mode: [_generate_trial_balance_trading(rng, mode)],
    "elementary_trial_balance": lambda rng, mode: [_generate_trial_balance_trading(rng, mode)],
}


def generate(
    subskill: str = "bank_ledger",
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
        pool = (
            [_generate_bank_ledger(rng, mode)]
            + [_generate_trading_stock_ledger(rng, mode)]
            + [_generate_trial_balance_trading(rng, mode)]
        )

    selected = pool
    if count < len(selected):
        selected = rng.sample(selected, count)
    return selected
