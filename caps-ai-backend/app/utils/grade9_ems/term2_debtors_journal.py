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
    
    # 4 Credit Sales
    debtor_names = [("B. Buyer", "D1"), ("C. Customer", "D2"), ("D. Dealer", "D3"), ("B. Buyer", "D1")]
    days = [5, 12, 19, 26]
    data_rows = []
    cell_hints = {}
    
    for idx, (d_name, d_fol) in enumerate(debtor_names):
        inv_no = str(101 + idx)
        day_str = str(days[idx])
        cp = rng.randint(10 + idx * 5, 30 + idx * 10) * 100
        sp = int(cp * (1 + markup_percentage / 100))
        
        transactions.append(f"Day {day_str}: Sold goods on credit to {d_name} for R{sp:,}. Issued duplicate invoice {inv_no}. The cost price was R{cp:,}.")
        data_rows.append([inv_no, day_str, d_name, d_fol, str(sp), str(cp)])
        
        cell_hints[f"t0_r{idx}_c0"] = f"Invoice number is {inv_no}."
        cell_hints[f"t0_r{idx}_c1"] = f"Day is {day_str}."
        cell_hints[f"t0_r{idx}_c2"] = f"Debtor is {d_name}."
        cell_hints[f"t0_r{idx}_c3"] = f"Debtors Ledger folio is {d_fol}."
        cell_hints[f"t0_r{idx}_c4"] = f"Sales column: R{sp:,}."
        cell_hints[f"t0_r{idx}_c5"] = f"Cost of Sales column: CP = SP x 100 / (100 + {markup_percentage}%) = R{cp:,}."

    correct_map = {}
    ui_rows = []
    for i, row in enumerate(data_rows):
        ui_row = []
        for j, val in enumerate(row):
            coord = f"t0_r{i}_c{j}"
            correct_map[coord] = val
            ui_row.append({
                "coordinate": coord,
                "value": val if mode == "scaffold" else "",
                "type": "required",
                "editable": True
            })
        ui_rows.append(ui_row)

    headers = ["Doc No", "Day", "Debtor", "Fol", "Sales", "Cost of Sales"]
    
    tot_sales = sum(int(r[4]) for r in data_rows)
    tot_cos = sum(int(r[5]) for r in data_rows)
    
    item = {
        "id": f"ems9_dj_{rng.randint(1000, 9999)}",
        "topic": "Debtors Journal",
        "question_type": "journal",
        "modality": "ledger",
        "prompt": f"Complete the **Debtors Journal** for **{business_name}** for {month}. The business applies a fixed mark-up of **{markup_percentage}% on cost**.",
        "transactions": transactions,
        "headers": headers,
        "rows": ui_rows,
        "journal": {
            "journal_type": "dj",
            "headers": headers,
            "rows": ui_rows
        },
        "editable_cols": [0, 1, 2, 3, 4, 5],
        "correct_map": correct_map,
        "cell_hints": cell_hints,
        "marks": 24,
        "sample_answer": f"Total Sales: R{tot_sales:,}; Total Cost of Sales: R{tot_cos:,}. General Ledger posting: Dr Debtors Control R{tot_sales:,}, Cr Sales R{tot_sales:,}; Dr Cost of Sales R{tot_cos:,}, Cr Trading Stock R{tot_cos:,}.",
        "ideal_answer": "Complete Debtors Journal table with accurate documentation, debtor allocations, sales values, and cost of sales calculations.",
        "worked_solution": (
            f"Step 1: Record duplicate invoice numbers (101 to 104) and dates.\n"
            f"Step 2: Enter debtor names and ledger folios.\n"
            f"Step 3: Record selling price in the Sales column.\n"
            f"Step 4: Calculate Cost of Sales using formula: CP = SP x 100 / (100 + {markup_percentage}%).\n"
            f"Step 5: Month-end totals: Total Sales = R{tot_sales:,}, Total Cost of Sales = R{tot_cos:,}."
        ),
        "marking_points": [
            "Correct duplicate invoice numbers and dates.",
            "Correct debtor names and folio references (D1, D2, D3).",
            f"Sales column entries totaling R{tot_sales:,}.",
            f"Cost of Sales column entries calculated at {markup_percentage}% mark-up, totaling R{tot_cos:,}."
        ],
        "hint_sections": {
            "1_nudge": "The Debtors Journal (DJ) is used for CREDIT sales of trading stock only.",
            "2_concept": "Every credit sale requires two entries: one for the selling price (Sales) and one for the cost price (Cost of Sales).",
            "3_breakdown": f"Markup formula: CP = SP x 100 / {100 + markup_percentage}. Total Sales = R{tot_sales:,}."
        },
        "guidelines": ["Check that both Sales and Cost of Sales columns are completed for each transaction."],
        "teaching_note": "Learners often forget to calculate Cost of Sales or confuse Selling Price with Cost Price."
    }
    return [_with_metadata(item, subskill='dj', learning_objective_id='lo_dj', question_family_id='dj_table', concept_id='dj_posting', concept_group='journals', diagnostic_tags=['tabular', 'accounting'])]

def generate(subskill="dj", difficulty="medium", count=1, mode="scaffold", seed=None, **kwargs):
    rng = _rng(seed)
    pool = _generate_debtors_journal(rng, mode)
    selected = pool
    if count < len(selected):
        selected = rng.sample(selected, count)
    return selected
