import random
from datetime import datetime, timedelta
import copy

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

def _generate_crj_trading(rng, mode):
    business_name = rng.choice(["Trader Joes", "Quick Mart", "Smart Shopper", "Elite Electronics"])
    month = rng.choice(["March 2026", "June 2026", "September 2026", "November 2026"])
    
    markup_percentage = rng.choice([25, 50, 100])
    
    transactions = []
    
    # Capital contribution
    cap_amt = rng.randint(5, 50) * 1000
    transactions.append(f"Day 1: The owner, {rng.choice(['P. Smith', 'M. Jones', 'T. Ngcobo'])}, deposited R{cap_amt} directly into the business bank account as capital. Issued receipt 01.")
    
    # Cash Sales
    cp1 = rng.randint(10, 50) * 100
    sp1 = int(cp1 * (1 + markup_percentage / 100))
    transactions.append(f"Day 12: Cash sales of trading stock, R{sp1}. The cost price was R{cp1}. CRT 21-25.")
    
    # Rent Income
    rent = rng.randint(2, 8) * 1000
    transactions.append(f"Day 25: Received R{rent} from A. Tenant for rent. Issued receipt 02.")

    data_rows = [
        ["01", "1", "Capital", "", str(cap_amt), "", "", str(cap_amt), "Capital"],
        ["CRT", "12", "Sales", str(sp1), str(sp1), str(sp1), str(cp1), "", ""],
        ["02", "25", "A. Tenant", str(rent), str(rent), "", "", str(rent), "Rent Income"]
    ]
    
    correct_map = {}
    ui_rows = []
    for i, row in enumerate(data_rows):
        ui_row = []
        for j, val in enumerate(row):
            correct_map[f"r{i}_c{j}"] = val
            ui_row.append({"value": "", "cell_id": f"r{i}_c{j}", "editable": True})
        ui_rows.append(ui_row)

    headers = ["Doc No", "Day", "Details", "Analysis of Receipts", "Bank", "Sales", "Cost of Sales", "Sundry Amount", "Sundry Details"]
    
    cell_hints = {}
    
    # Hint for Row 1 Capital
    cell_hints["r0_c3"] = "Expectation: Analysis of receipts. Connection: Direct deposits go straight to Bank, leave this blank."
    cell_hints["r0_c4"] = f"Expectation: Bank. Connection: R{cap_amt} deposited."
    cell_hints["r0_c7"] = f"Expectation: Sundry Amount. Connection: Capital is not sales, so R{cap_amt} goes here."
    cell_hints["r0_c8"] = "Expectation: Sundry Details. Connection: The owner deposited money to start the business. Account is 'Capital'."
    
    # Hint for Row 2 Sales
    cell_hints["r1_c3"] = f"Expectation: Analysis. Connection: Cash sales put money in the till. R{sp1}."
    cell_hints["r1_c4"] = f"Expectation: Bank. Connection: Assuming it was banked on the same day, R{sp1}."
    cell_hints["r1_c5"] = f"Expectation: Sales. Connection: The selling price of the stock is R{sp1}."
    cell_hints["r1_c6"] = f"Expectation: Cost of Sales. Connection: The original cost price of the goods sold is R{cp1}."
    
    item = {
        "id": f"ems9_crj_{rng.randint(1000, 9999)}",
        "topic": "Cash Receipts Journal (Trading Business)",
        "question_type": "journal",
        "prompt": f"Complete the Cash Receipts Journal for {business_name} for {month}. The business uses a fixed mark-up of {markup_percentage}% on cost.",
        "transactions": transactions,
        "journal": {
            "journal_type": "crj",
            "headers": headers,
            "rows": ui_rows
        },
        "editable_cols": [0, 1, 2, 3, 4, 5, 6, 7, 8],
        "correct_map": correct_map,
        "cell_hints": cell_hints,
        "marks": 27,
        "sample_answer": "See completed table",
        "ideal_answer": "See completed table",
        "marking_points": ["Correct doc numbers, correct split of Sales and Cost of Sales, and correct sundry allocations."],
        "hint_sections": {
            "1_nudge": "In a trading business, when you sell goods, you must record both the selling price (Sales) and the cost price (Cost of Sales).",
            "2_concept": "Sales affects Bank and Analysis. Cost of Sales is a separate column and does NOT affect Bank.",
            "3_breakdown": "Direct deposits bypass the Analysis of Receipts column."
        },
        "guidelines": ["Check that Sales + Sundries = Bank for each row. Cost of Sales is separate."],
        "teaching_note": "Learners often forget Cost of Sales or add it to Bank."
    }
    return [_with_metadata(item, subskill='crj', learning_objective_id='lo_crj_trading', question_family_id='crj_table', concept_id='crj_trading', concept_group='journals', diagnostic_tags=['tabular', 'accounting'])]

def _generate_cpj_trading(rng, mode):
    business_name = rng.choice(["Trader Joes", "Quick Mart", "Smart Shopper", "Elite Electronics"])
    month = rng.choice(["March 2026", "June 2026", "September 2026", "November 2026"])
    
    transactions = []
    
    # Buy trading stock
    stock_amt = rng.randint(20, 80) * 100
    transactions.append(f"Day 5: Issued cheque 101 for R{stock_amt} to Makro to purchase trading stock.")
    
    # Pay wages
    wage_amt = rng.randint(10, 30) * 100
    transactions.append(f"Day 14: Cashed a cheque to pay wages, R{wage_amt}.")
    
    data_rows = [
        ["101", "5", "Makro", str(stock_amt), str(stock_amt), "", "", "", ""],
        ["102", "14", "Cash", str(wage_amt), "", str(wage_amt), "", "", ""]
    ]
    
    correct_map = {}
    ui_rows = []
    for i, row in enumerate(data_rows):
        ui_row = []
        for j, val in enumerate(row):
            correct_map[f"r{i}_c{j}"] = val
            ui_row.append({"value": "", "cell_id": f"r{i}_c{j}", "editable": True})
        ui_rows.append(ui_row)

    headers = ["Doc No", "Day", "Name of Payee", "Bank", "Trading Stock", "Wages", "Consumable Stores", "Sundry Amount", "Sundry Details"]
    
    cell_hints = {}
    
    # Hint for Row 1
    cell_hints["r0_c4"] = f"Expectation: Trading Stock. Connection: Goods bought to resell are called Trading Stock. Enter R{stock_amt}."
    
    item = {
        "id": f"ems9_cpj_{rng.randint(1000, 9999)}",
        "topic": "Cash Payments Journal (Trading Business)",
        "question_type": "journal",
        "prompt": f"Complete the Cash Payments Journal for {business_name} for {month}.",
        "transactions": transactions,
        "journal": {
            "journal_type": "cpj",
            "headers": headers,
            "rows": ui_rows
        },
        "editable_cols": [0, 1, 2, 3, 4, 5, 6, 7, 8],
        "correct_map": correct_map,
        "cell_hints": cell_hints,
        "marks": 18,
        "sample_answer": "See completed table",
        "ideal_answer": "See completed table",
        "marking_points": ["Correct allocations to Trading Stock and Wages."],
        "hint_sections": {
            "1_nudge": "The CPJ records all payments. Remember that stock bought to resell is 'Trading Stock'.",
            "2_concept": "Every payment goes in Bank, then distributed to the correct analysis column.",
            "3_breakdown": "If buying stock, put it in the Trading Stock column, not Sundries."
        },
        "guidelines": ["Check that Bank = Sum of all analysis columns for each row."],
        "teaching_note": "Differentiate between Trading Stock and Consumable Stores."
    }
    return [_with_metadata(item, subskill='cpj', learning_objective_id='lo_cpj_trading', question_family_id='cpj_table', concept_id='cpj_trading', concept_group='journals', diagnostic_tags=['tabular', 'accounting'])]

def generate(subskill="crj", difficulty="medium", count=1, mode="scaffold", seed=None, **kwargs):
    rng = _rng(seed)
    
    if subskill == "crj":
        pool = _generate_crj_trading(rng, mode)
    elif subskill == "cpj":
        pool = _generate_cpj_trading(rng, mode)
    else:
        pool = _generate_crj_trading(rng, mode) + _generate_cpj_trading(rng, mode)
        
    selected = pool
    if count < len(selected):
        selected = rng.sample(selected, count)
        
    return selected
