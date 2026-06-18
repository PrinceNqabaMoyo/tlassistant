import random

def _rng(seed=None):
    if seed is not None:
        return random.Random(seed)
    return random.Random()

def _with_metadata(item, subskill, learning_objective_id, question_family_id, concept_id, concept_group, diagnostic_tags):
    item['subskill'] = subskill
    item['learning_objective_id'] = learning_objective_id
    item['question_family_id'] = question_family_id
    item['concept_id'] = concept_id
    item['concept_group'] = concept_group
    item['diagnostic_tags'] = diagnostic_tags
    return item

def _generate_general_ledger(rng, mode):
    business_name = rng.choice(["Trader Joes", "Quick Mart", "Smart Shopper", "Elite Electronics"])
    month = rng.choice(["March 2026", "June 2026", "September 2026", "November 2026"])
    
    # Simple Bank T-account posting
    total_receipts = rng.randint(20, 80) * 1000
    total_payments = rng.randint(10, 40) * 1000
    opening_balance = rng.randint(5, 15) * 1000
    closing_balance = opening_balance + total_receipts - total_payments
    
    prompt = f"Use the information provided to complete the Bank account in the General Ledger of {business_name} for the month ended {month}."
    transactions = [
        f"Bank balance at beginning of month: R{opening_balance}",
        f"Total receipts per CRJ for the month: R{total_receipts}",
        f"Total payments per CPJ for the month: R{total_payments}"
    ]
    
    # Ledger columns: Date(2), Details, Fol, Amount, Date(2), Details, Fol, Amount
    headers = ["Date", "", "Details", "Fol", "Amount", "Date", "", "Details", "Fol", "Amount"]
    
    data_rows = [
        ["1", "b/d", "Balance", "b/d", str(opening_balance), "31", "CRJ", "Total Receipts", "CRJ", str(total_receipts)],
        ["", "", "", "", "", "31", "CPJ", "Total Payments", "CPJ", str(total_payments)],
        ["", "", "", "", "", "31", "c/d", "Balance", "c/d", str(closing_balance)],
        ["", "", "", "", str(opening_balance + total_receipts), "", "", "", "", str(opening_balance + total_receipts)],
        ["1", "b/d", "Balance", "b/d", str(closing_balance), "", "", "", "", ""]
    ]
    
    # For a ledger, Grade 10 frontend usually expects 8 or 10 columns. 
    # Actually, a standard T-account has Date, Details, Fol, Amount for both sides.
    # We will use 10 columns: Day, Month, Details, Fol, Amount (Debit) and Day, Month, Details, Fol, Amount (Credit)
    
    # We will just map it simply to match Grade 10 logic.
    correct_map = {}
    ui_rows = []
    for i, row in enumerate(data_rows):
        ui_row = []
        for j, val in enumerate(row):
            correct_map[f"r{i}_c{j}"] = val
            ui_row.append({"value": "", "cell_id": f"r{i}_c{j}", "editable": True})
        ui_rows.append(ui_row)

    cell_hints = {}
    cell_hints["r0_c4"] = f"Expectation: Debit Amount. Connection: The opening balance is an asset, so it goes on the Debit side. R{opening_balance}."
    cell_hints["r0_c9"] = f"Expectation: Credit Amount. Connection: Is this right? Wait, receipts increase bank. So CRJ goes on Debit. Payments go on Credit."
    
    # FIX DATA ROWS: Bank is an asset.
    # Debit: Balance b/d, Total Receipts (CRJ)
    # Credit: Total Payments (CPJ), Balance c/d
    data_rows = [
        ["1", "Balance", "b/d", str(opening_balance), "31", "Total Payments", "CPJ", str(total_payments)],
        ["31", "Total Receipts", "CRJ", str(total_receipts), "31", "Balance", "c/d", str(closing_balance)],
        ["", "", "", str(opening_balance + total_receipts), "", "", "", str(opening_balance + total_receipts)],
        ["1", "Balance", "b/d", str(closing_balance), "", "", "", ""]
    ]
    
    headers = ["Day", "Details", "Fol", "Amount", "Day", "Details", "Fol", "Amount"]
    correct_map = {}
    ui_rows = []
    for i, row in enumerate(data_rows):
        ui_row = []
        for j, val in enumerate(row):
            correct_map[f"r{i}_c{j}"] = val
            ui_row.append({"value": "", "cell_id": f"r{i}_c{j}", "editable": True})
        ui_rows.append(ui_row)
        
    cell_hints = {
        "r0_c3": f"Debit amount. Bank is an asset with a debit balance. R{opening_balance}.",
        "r1_c3": f"Receipts increase the bank account (Debit). R{total_receipts}.",
        "r0_c7": f"Payments decrease the bank account (Credit). R{total_payments}.",
    }
    
    item = {
        "id": f"ems9_gl_{rng.randint(1000, 9999)}",
        "topic": "General Ledger - Bank Account",
        "question_type": "ledger",
        "prompt": prompt,
        "transactions": transactions,
        "journal": {
            "journal_type": "general_ledger",
            "headers": headers,
            "rows": ui_rows
        },
        "editable_cols": [0, 1, 2, 3, 4, 5, 6, 7],
        "correct_map": correct_map,
        "cell_hints": cell_hints,
        "marks": 16,
        "sample_answer": "See completed T-account",
        "ideal_answer": "See completed T-account",
        "marking_points": ["Correct balances", "Correct posting from CRJ and CPJ"],
        "hint_sections": {
            "1_nudge": "Bank is an asset. Assets increase on the Debit side and decrease on the Credit side.",
            "2_concept": "Receipts (CRJ) mean money in, so Debit Bank. Payments (CPJ) mean money out, so Credit Bank.",
            "3_breakdown": "Balance the account by finding the difference between total debits and total credits."
        },
        "guidelines": ["Check balancing."],
        "teaching_note": "Learners often reverse the CRJ and CPJ postings."
    }
    return [_with_metadata(item, subskill='general_ledger', learning_objective_id='lo_gl', question_family_id='gl_table', concept_id='gl_posting', concept_group='ledger', diagnostic_tags=['tabular', 'accounting'])]

def generate(subskill="general_ledger", difficulty="medium", count=1, mode="scaffold", seed=None, **kwargs):
    rng = _rng(seed)
    pool = _generate_general_ledger(rng, mode)
    selected = pool
    if count < len(selected):
        selected = rng.sample(selected, count)
    return selected
