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
    
    # 1. Trading stock
    stock_amt1 = rng.randint(25, 60) * 100
    transactions.append(f"Day 4: Received original invoice 45 from Wholesalers Ltd for trading stock bought on credit, R{stock_amt1:,}.")
    
    # 2. Stationery
    stat_amt = rng.randint(3, 8) * 100
    transactions.append(f"Day 12: Bought office stationery on credit from PaperCo for R{stat_amt:,}. Invoice 88.")
    
    # 3. Equipment (Sundry Accounts)
    equip_amt = rng.randint(15, 35) * 100
    transactions.append(f"Day 18: Purchased computer equipment on credit from Office Mart, R{equip_amt:,}. Invoice 210.")
    
    # 4. Trading stock subject to trade discount
    gross_stock = rng.randint(30, 50) * 100
    discount_pct = rng.choice([10, 20])
    net_stock = int(gross_stock * (100 - discount_pct) / 100)
    transactions.append(f"Day 26: Bought trading stock on credit from Wholesalers Ltd for R{gross_stock:,} less {discount_pct}% trade discount. Invoice 52.")

    data_rows = [
        ["45", "4", "Wholesalers Ltd", "C1", str(stock_amt1), str(stock_amt1), "", "", ""],
        ["88", "12", "PaperCo", "C2", str(stat_amt), "", str(stat_amt), "", ""],
        ["210", "18", "Office Mart", "C3", str(equip_amt), "", "", str(equip_amt), "Equipment"],
        ["52", "26", "Wholesalers Ltd", "C1", str(net_stock), str(net_stock), "", "", ""],
    ]
    
    correct_map = {}
    ui_rows = []
    cell_hints = {}
    
    for i, row in enumerate(data_rows):
        ui_row = []
        for j, val in enumerate(row):
            coord = f"t0_r{i}_c{j}"
            correct_map[coord] = val
            is_empty = (val == "")
            ui_row.append({
                "coordinate": coord,
                "value": val if mode == "scaffold" else "",
                "type": "must_be_empty" if is_empty else "required",
                "editable": True
            })
        ui_rows.append(ui_row)
        
    cell_hints["t0_r0_c4"] = f"Total credit purchase in Creditors Control: R{stock_amt1:,}."
    cell_hints["t0_r0_c5"] = f"Trading Stock column: R{stock_amt1:,}."
    cell_hints["t0_r1_c4"] = f"Total credit purchase in Creditors Control: R{stat_amt:,}."
    cell_hints["t0_r1_c6"] = f"Stationery column: R{stat_amt:,}."
    cell_hints["t0_r2_c4"] = f"Total credit purchase in Creditors Control: R{equip_amt:,}."
    cell_hints["t0_r2_c7"] = f"Equipment goes to Sundry Accounts: R{equip_amt:,}."
    cell_hints["t0_r2_c8"] = "Account name is 'Equipment'."
    cell_hints["t0_r3_c4"] = f"Trade discount deducted immediately: R{gross_stock:,} - {discount_pct}% = R{net_stock:,} in Creditors Control."
    cell_hints["t0_r3_c5"] = f"Net stock recorded: R{net_stock:,}."

    headers = ["Doc No", "Day", "Creditor", "Fol", "Creditors Control", "Trading Stock", "Stationery", "Sundry Amount", "Sundry Details"]
    
    tot_cc = stock_amt1 + stat_amt + equip_amt + net_stock
    tot_stock = stock_amt1 + net_stock
    
    item = {
        "id": f"ems9_cj_{rng.randint(1000, 9999)}",
        "topic": "Creditors Journal",
        "question_type": "journal",
        "modality": "ledger",
        "prompt": f"Complete the **Creditors Journal** for **{business_name}** for {month}. Note that trade discounts must be deducted before recording invoice values.",
        "transactions": transactions,
        "headers": headers,
        "rows": ui_rows,
        "journal": {
            "journal_type": "cj",
            "headers": headers,
            "rows": ui_rows
        },
        "editable_cols": [0, 1, 2, 3, 4, 5, 6, 7, 8],
        "correct_map": correct_map,
        "cell_hints": cell_hints,
        "marks": 36,
        "sample_answer": (
            f"Creditors Journal month-end totals for {business_name}:\n"
            f"• Creditors Control: R{tot_cc:,}\n"
            f"• Trading Stock: R{tot_stock:,}\n"
            f"• Stationery: R{stat_amt:,}\n"
            f"• Sundry Accounts (Equipment): R{equip_amt:,}\n"
            f"Cross-cast check: R{tot_stock:,} + R{stat_amt:,} + R{equip_amt:,} = R{tot_cc:,}."
        ),
        "ideal_answer": "Complete 2D Creditors Journal table with correct calculations, trade discount deductions, and column cross-casting.",
        "worked_solution": (
            f"Step 1: Original invoices are recorded in order.\n"
            f"Step 2: Enter date, creditor name, and Creditors Ledger folios (C1, C2, C3).\n"
            f"Step 3: In Row 4, deduct {discount_pct}% trade discount: R{gross_stock:,} x (100 - {discount_pct})/100 = R{net_stock:,}.\n"
            f"Step 4: Record totals in Creditors Control (liability increase) and analyze into Trading Stock, Stationery, or Sundries.\n"
            f"Step 5: Verify cross-casting: Creditors Control (R{tot_cc:,}) = Trading Stock (R{tot_stock:,}) + Stationery (R{stat_amt:,}) + Equipment (R{equip_amt:,})."
        ),
        "marking_points": [
            "Original invoice numbers and dates correctly recorded.",
            "Creditor names and folios (C1, C2, C3) entered.",
            f"Trade discount calculated accurately on Day 26 (R{net_stock:,}).",
            f"Creditors Control column entries correctly matching sum of analysis columns.",
            f"Equipment allocated to Sundry Accounts."
        ],
        "hint_sections": {
            "1_nudge": "The Creditors Journal (CJ) is used for purchases on CREDIT only. Always deduct trade discount before recording the invoice.",
            "2_concept": "Every row must have an entry in Creditors Control equal to the sum of all other analysis columns.",
            "3_breakdown": f"Total Creditors Control = R{tot_cc:,}. Stock = R{tot_stock:,}. Stationery = R{stat_amt:,}. Equipment = R{equip_amt:,}."
        },
        "guidelines": ["Check that Creditors Control = Trading Stock + Stationery + Sundry Amount for every row."],
        "teaching_note": "Learners often forget to deduct trade discounts or forget to specify the account name in Sundry Details."
    }
    return [_with_metadata(item, subskill='cj', learning_objective_id='lo_cj', question_family_id='cj_table', concept_id='cj_posting', concept_group='journals', diagnostic_tags=['tabular', 'accounting'])]

def generate(subskill="cj", difficulty="medium", count=1, mode="scaffold", seed=None, **kwargs):
    rng = _rng(seed)
    pool = _generate_creditors_journal(rng, mode)
    selected = pool
    if count < len(selected):
        selected = rng.sample(selected, count)
    return selected
