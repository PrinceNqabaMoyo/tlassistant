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

def _generate_debtors_ledger(rng, mode):
    business_name = rng.choice(["Trader Joes", "Quick Mart", "Smart Shopper", "Elite Electronics"])
    month = rng.choice(["March 2026", "June 2026", "September 2026", "November 2026"])
    
    opening_bal = rng.randint(5, 20) * 100
    sale_amt = rng.randint(2, 8) * 100
    receipt_amt = rng.randint(1, 5) * 100
    
    transactions = [
        f"1st: Account balance for debtor S. Sithole was R{opening_bal}.",
        f"12th: Sold goods on credit to S. Sithole, R{sale_amt}. Invoice 101.",
        f"20th: Received a cheque from S. Sithole for R{receipt_amt}. Receipt 44."
    ]

    data_rows = [
        ["1", "Account rendered", "b/d", "", "", str(opening_bal)],
        ["12", "Invoice 101", "DJ", str(sale_amt), "", str(opening_bal + sale_amt)],
        ["20", "Receipt 44", "CRJ", "", str(receipt_amt), str(opening_bal + sale_amt - receipt_amt)]
    ]
    
    correct_map = {}
    ui_rows = []
    for i, row in enumerate(data_rows):
        ui_row = []
        for j, val in enumerate(row):
            correct_map[f"r{i}_c{j}"] = val
            ui_row.append({"value": "", "cell_id": f"r{i}_c{j}", "editable": True})
        ui_rows.append(ui_row)

    headers = ["Date", "Details", "Fol", "Debit (+)", "Credit (-)", "Balance"]
    
    cell_hints = {}
    
    # Hint for Row 2
    cell_hints["r1_c3"] = f"Expectation: Debit Amount. Connection: Selling on credit increases what they owe us. R{sale_amt}."
    cell_hints["r1_c5"] = f"Expectation: New Balance. Connection: Add the debit to the previous balance."
    
    item = {
        "id": f"ems9_dl_{rng.randint(1000, 9999)}",
        "topic": "Debtors Ledger - S. Sithole",
        "question_type": "ledger",
        "prompt": f"Complete the Debtors Ledger account for S. Sithole for {month}.",
        "transactions": transactions,
        "journal": {
            "journal_type": "debtors_ledger",
            "headers": headers,
            "rows": ui_rows
        },
        "editable_cols": [0, 1, 2, 3, 4, 5],
        "correct_map": correct_map,
        "cell_hints": cell_hints,
        "marks": 18,
        "sample_answer": "See completed table",
        "ideal_answer": "See completed table",
        "marking_points": ["Correct folios", "Correct debit/credit columns", "Correct running balances"],
        "hint_sections": {
            "1_nudge": "A debtor is an asset. Their account increases on the Debit side (+) and decreases on the Credit side (-).",
            "2_concept": "Sales (DJ) increase the debt. Receipts (CRJ) decrease the debt.",
            "3_breakdown": "Calculate the running balance after every transaction."
        },
        "guidelines": ["Check that the balance updates correctly after each line."],
        "teaching_note": "Learners often put receipts on the debit side by mistake."
    }
    return [_with_metadata(item, subskill='dl', learning_objective_id='lo_dl', question_family_id='dl_table', concept_id='dl_posting', concept_group='ledger', diagnostic_tags=['tabular', 'accounting'])]

def generate(subskill="dl", difficulty="medium", count=1, mode="scaffold", seed=None, **kwargs):
    rng = _rng(seed)
    pool = _generate_debtors_ledger(rng, mode)
    selected = pool
    if count < len(selected):
        selected = rng.sample(selected, count)
    return selected
