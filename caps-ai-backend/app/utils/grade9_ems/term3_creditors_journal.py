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

def _generate_creditors_journal(rng, mode):
    business_name = rng.choice(["Trader Joes", "Quick Mart", "Smart Shopper", "Elite Electronics"])
    month = rng.choice(["March 2026", "June 2026", "September 2026", "November 2026"])
    
    transactions = []
    
    # Buy trading stock on credit
    stock_amt = rng.randint(20, 80) * 100
    transactions.append(f"Day 4: Received original invoice 45 from Wholesalers Ltd for trading stock, R{stock_amt}.")
    
    # Buy stationery on credit
    stat_amt = rng.randint(2, 10) * 100
    transactions.append(f"Day 15: Bought stationery on credit from PaperCo for R{stat_amt}. Invoice 46.")

    data_rows = [
        ["45", "4", "Wholesalers Ltd", "C1", str(stock_amt), str(stock_amt), "", "", ""],
        ["46", "15", "PaperCo", "C2", str(stat_amt), "", str(stat_amt), "", ""]
    ]
    
    correct_map = {}
    ui_rows = []
    for i, row in enumerate(data_rows):
        ui_row = []
        for j, val in enumerate(row):
            correct_map[f"r{i}_c{j}"] = val
            ui_row.append({"value": "", "cell_id": f"r{i}_c{j}", "editable": True})
        ui_rows.append(ui_row)

    headers = ["Doc No", "Day", "Creditor", "Fol", "Creditors Control", "Trading Stock", "Stationery", "Sundry Amount", "Sundry Details"]
    
    cell_hints = {}
    
    # Hint for Row 1
    cell_hints["r0_c4"] = f"Expectation: Creditors Control. Connection: We owe Wholesalers Ltd R{stock_amt}."
    cell_hints["r0_c5"] = f"Expectation: Trading Stock. Connection: We bought trading stock, R{stock_amt}."
    
    item = {
        "id": f"ems9_cj_{rng.randint(1000, 9999)}",
        "topic": "Creditors Journal",
        "question_type": "journal",
        "prompt": f"Complete the Creditors Journal for {business_name} for {month}.",
        "transactions": transactions,
        "journal": {
            "journal_type": "cj",
            "headers": headers,
            "rows": ui_rows
        },
        "editable_cols": [0, 1, 2, 3, 4, 5, 6, 7, 8],
        "correct_map": correct_map,
        "cell_hints": cell_hints,
        "marks": 18,
        "sample_answer": "See completed table",
        "ideal_answer": "See completed table",
        "marking_points": ["Correct doc numbers, correct Creditors, and correct allocations."],
        "hint_sections": {
            "1_nudge": "The Creditors Journal (CJ) is used when buying on CREDIT.",
            "2_concept": "Every transaction must have an amount in the Creditors Control column.",
            "3_breakdown": "Distribute the amount to the specific expense or asset account (e.g., Trading Stock or Stationery)."
        },
        "guidelines": ["Check that Creditors Control = Sum of all analysis columns for each row."],
        "teaching_note": "Learners often put cash purchases in the CJ."
    }
    return [_with_metadata(item, subskill='cj', learning_objective_id='lo_cj', question_family_id='cj_table', concept_id='cj_posting', concept_group='journals', diagnostic_tags=['tabular', 'accounting'])]

def generate(subskill="cj", difficulty="medium", count=1, mode="scaffold", seed=None, **kwargs):
    rng = _rng(seed)
    pool = _generate_creditors_journal(rng, mode)
    selected = pool
    if count < len(selected):
        selected = rng.sample(selected, count)
    return selected
