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

def _generate_debtors_journal(rng, mode):
    business_name = rng.choice(["Trader Joes", "Quick Mart", "Smart Shopper", "Elite Electronics"])
    month = rng.choice(["March 2026", "June 2026", "September 2026", "November 2026"])
    markup_percentage = rng.choice([25, 50, 100])
    
    transactions = []
    
    # Credit Sales
    cp1 = rng.randint(20, 80) * 100
    sp1 = int(cp1 * (1 + markup_percentage / 100))
    transactions.append(f"Day 12: Sold trading stock on credit to B. Buyer for R{sp1}. Issued invoice 101. Cost price was R{cp1}.")
    
    cp2 = rng.randint(10, 50) * 100
    sp2 = int(cp2 * (1 + markup_percentage / 100))
    transactions.append(f"Day 18: Goods sold on credit to C. Customer, R{sp2}. Issued invoice 102. Cost price was R{cp2}.")

    data_rows = [
        ["101", "12", "B. Buyer", "D1", str(sp1), str(cp1)],
        ["102", "18", "C. Customer", "D2", str(sp2), str(cp2)]
    ]
    
    correct_map = {}
    ui_rows = []
    for i, row in enumerate(data_rows):
        ui_row = []
        for j, val in enumerate(row):
            correct_map[f"r{i}_c{j}"] = val
            ui_row.append({"value": "", "cell_id": f"r{i}_c{j}", "editable": True})
        ui_rows.append(ui_row)

    headers = ["Doc No", "Day", "Debtor", "Fol", "Sales", "Cost of Sales"]
    
    cell_hints = {}
    
    # Hint for Row 1
    cell_hints["r0_c4"] = f"Expectation: Sales Amount. Connection: Credit sales are recorded in the DJ. Selling price is R{sp1}."
    cell_hints["r0_c5"] = f"Expectation: Cost of Sales. Connection: Original cost price of the goods sold is R{cp1}."
    
    item = {
        "id": f"ems9_dj_{rng.randint(1000, 9999)}",
        "topic": "Debtors Journal",
        "question_type": "journal",
        "prompt": f"Complete the Debtors Journal for {business_name} for {month}. The business uses a fixed mark-up of {markup_percentage}% on cost.",
        "transactions": transactions,
        "journal": {
            "journal_type": "dj",
            "headers": headers,
            "rows": ui_rows
        },
        "editable_cols": [0, 1, 2, 3, 4, 5],
        "correct_map": correct_map,
        "cell_hints": cell_hints,
        "marks": 12,
        "sample_answer": "See completed table",
        "ideal_answer": "See completed table",
        "marking_points": ["Correct doc numbers, correct Debtors, and correct split of Sales and Cost of Sales."],
        "hint_sections": {
            "1_nudge": "The Debtors Journal (DJ) is used for CREDIT sales only.",
            "2_concept": "You must record both the selling price (Sales) and the cost price (Cost of Sales) for every transaction.",
            "3_breakdown": "Make sure you do not put cash sales in here."
        },
        "guidelines": ["Check that Sales and Cost of Sales are correctly identified."],
        "teaching_note": "Learners often put cash sales in the DJ or mix up cost and selling price."
    }
    return [_with_metadata(item, subskill='dj', learning_objective_id='lo_dj', question_family_id='dj_table', concept_id='dj_posting', concept_group='journals', diagnostic_tags=['tabular', 'accounting'])]

def generate(subskill="dj", difficulty="medium", count=1, mode="scaffold", seed=None, **kwargs):
    rng = _rng(seed)
    pool = _generate_debtors_journal(rng, mode)
    selected = pool
    if count < len(selected):
        selected = rng.sample(selected, count)
    return selected
