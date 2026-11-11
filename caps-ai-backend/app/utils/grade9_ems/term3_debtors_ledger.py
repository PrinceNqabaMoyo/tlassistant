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

def _generate_debtors_ledger(rng, mode, seed=None):
    businesses = ["Trader Joes", "Quick Mart", "Smart Shopper", "Elite Electronics", "Soweto General Dealers", "Durban Retailers"]
    months = ["March 2026", "June 2026", "September 2026", "November 2026"]
    debtors = ["S. Sithole", "B. Khumalo", "N. Dlamini", "T. Naidoo", "P. Van der Merwe", "L. Mthembu"]
    
    business_name = rng.choice(businesses)
    month = rng.choice(months)
    debtor_name = rng.choice(debtors)
    debtor_fol = "D1"
    
    opening_bal = rng.randint(8, 25) * 100
    sale_amt = rng.randint(12, 35) * 100
    return_amt = rng.randint(2, 6) * 100
    receipt_amt = rng.randint(6, 18) * 100
    
    bal1 = opening_bal
    bal2 = bal1 + sale_amt
    bal3 = bal2 - return_amt
    bal4 = bal3 - receipt_amt
    
    transactions = [
        f"1st: Account rendered balance brought forward: R{bal1:,}.",
        f"12th: Sold goods on credit to {debtor_name}, R{sale_amt:,}. Issued duplicate invoice 101 (DJ).",
        f"17th: Issued Credit Note 35 to {debtor_name} for damaged goods returned, R{return_amt:,} (DAJ).",
        f"25th: Received payment of R{receipt_amt:,} from {debtor_name} in partial settlement of account. Issued duplicate receipt 88 (CRJ)."
    ]

    data_rows = [
        ["1", "Account rendered", "b/d", "", "", str(bal1)],
        ["12", "Invoice 101", "DJ", str(sale_amt), "", str(bal2)],
        ["17", "Credit Note 35", "DAJ", "", str(return_amt), str(bal3)],
        ["25", "Receipt 88", "CRJ", "", str(receipt_amt), str(bal4)],
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
            is_opening = (i == 0 and j in [0, 1, 2, 5])
            ui_row.append({
                "coordinate": coord,
                "value": val if (mode == "scaffold" or is_opening) else "",
                "type": "given" if is_opening else ("must_be_empty" if is_empty else "required"),
                "editable": not is_opening,
            })
        ui_rows.append(ui_row)

    headers = ["Date", "Details", "Fol", "Debit (+)", "Credit (-)", "Balance"]
    
    cell_hints["t0_r1_c3"] = f"Credit sale from DJ: Debit column increases debtor's balance by R{sale_amt:,}."
    cell_hints["t0_r1_c5"] = f"New Balance = Previous Balance (R{bal1:,}) + Debit (R{sale_amt:,}) = R{bal2:,}."
    cell_hints["t0_r2_c4"] = f"Allowance / return from DAJ: Credit column decreases debtor's balance by R{return_amt:,}."
    cell_hints["t0_r2_c5"] = f"New Balance = Previous Balance (R{bal2:,}) - Credit (R{return_amt:,}) = R{bal3:,}."
    cell_hints["t0_r3_c4"] = f"Payment received from CRJ: Credit column decreases debtor's balance by R{receipt_amt:,}."
    cell_hints["t0_r3_c5"] = f"New Balance = Previous Balance (R{bal3:,}) - Credit (R{receipt_amt:,}) = R{bal4:,}."
    
    item = {
        "id": f"ems9_dl_{rng.randint(1000, 9999)}",
        "topic": f"Debtors Ledger - {debtor_name} ({debtor_fol})",
        "question_type": "table_completion",
        "modality": "ledger",
        "prompt": f"Complete the **Debtors Ledger** account for **{debtor_name} ({debtor_fol})** in the books of **{business_name}** for {month}. Starting balance: R{opening_bal:,}.",
        "transactions": transactions,
        "headers": headers,
        "rows": ui_rows,
        "journal": {
            "journal_type": "debtors_ledger",
            "headers": headers,
            "rows": ui_rows
        },
        "editable_cols": [0, 1, 2, 3, 4, 5],
        "correct_map": correct_map,
        "cell_hints": cell_hints,
        "marks": 16,
        "sample_answer": f"Final balance owed by {debtor_name} on Sept 25: R{bal4:,} (Debit balance). Reconciles with Debtors Control (B4) in the General Ledger.",
        "ideal_answer": "Complete 3-column Debtors Ledger account showing accurate entries for DJ (Debit +), DAJ (Credit -), and CRJ (Credit -).",
        "worked_solution": (
            f"Step 1: Balance b/d on Day 1 is R{bal1:,}.\n"
            f"Step 2: On Day 12, credit sale of R{sale_amt:,} (DJ) is entered in Debit (+) -> Balance becomes R{bal1:,} + R{sale_amt:,} = R{bal2:,}.\n"
            f"Step 3: On Day 17, goods returned R{return_amt:,} (DAJ) entered in Credit (-) -> Balance becomes R{bal2:,} - R{return_amt:,} = R{bal3:,}.\n"
            f"Step 4: On Day 25, payment R{receipt_amt:,} (CRJ) entered in Credit (-) -> Balance becomes R{bal3:,} - R{receipt_amt:,} = R{bal4:,}."
        ),
        "marking_points": [
            f"Day 12: Invoice 101 (DJ) in Debit (+), Balance R{bal2:,}",
            f"Day 17: Credit Note 35 (DAJ) in Credit (-), Balance R{bal3:,}",
            f"Day 25: Receipt 88 (CRJ) in Credit (-), Balance R{bal4:,}",
            f"Accurate running balances throughout."
        ],
        "hint_sections": {
            "1_nudge": "A debtor is an asset. Debits (+) INCREASE what they owe us. Credits (-) DECREASE what they owe us.",
            "2_concept": "Sales (DJ) increase the debt. Allowances/returns (DAJ) and payments (CRJ) decrease the debt.",
            "3_breakdown": f"Bal = R{bal1:,} + R{sale_amt:,} (DJ) - R{return_amt:,} (DAJ) - R{receipt_amt:,} (CRJ) = R{bal4:,}."
        },
        "guidelines": ["Check that the balance updates correctly after each transaction."],
        "teaching_note": "Learners often put payments or returns on the debit side by mistake."
    }
    return [_with_metadata(item, subskill='dl', learning_objective_id='lo_dl', question_family_id='dl_table', concept_id='dl_posting', concept_group='ledger', diagnostic_tags=['tabular', 'accounting'])]

def generate(subskill="dl", difficulty="medium", count=1, mode="scaffold", seed=None, **kwargs):
    rng = _rng(seed)
    pool = _generate_debtors_ledger(rng, mode, seed=seed)
    selected = pool
    if count < len(selected):
        selected = rng.sample(selected, count)
    return selected
