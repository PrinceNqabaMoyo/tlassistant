import random
from app.utils.ems_namelist import get_ems_scenario

def _rng(seed=None):
    return random.Random(seed)

TOPIC_ID = 'grade8_ems'
SUBTOPIC_ID = 'term1_accounting_basics'
CURRICULUM_REFERENCE = 'Term 1 > Accounting Concepts and Source Documents'

def _with_metadata(
    item,
    *,
    subskill,
    learning_objective_id,
    question_family_id,
    concept_id=None,
    concept_group=None,
    scenario_family_id=None,
    retry_variant='core',
    curriculum_reference=CURRICULUM_REFERENCE,
    misconception_tags=None,
    diagnostic_tags=None,
    answer_structure_tags=None,
    minimum_mastery_score=None,
):
    enriched = dict(item)
    enriched.update({
        'topic_id': TOPIC_ID,
        'subtopic_id': SUBTOPIC_ID,
        'subskill': subskill,
        'learning_objective_id': learning_objective_id,
        'concept_id': concept_id,
        'concept_group': concept_group,
        'question_family_id': question_family_id,
        'scenario_family_id': scenario_family_id,
        'retry_variant': retry_variant,
        'difficulty_band': item.get('difficulties', ['easy', 'medium', 'hard']),
        'curriculum_reference': curriculum_reference,
        'misconception_tags': misconception_tags or [],
        'diagnostic_tags': diagnostic_tags or [],
        'answer_structure_tags': answer_structure_tags or [],
    })
    if minimum_mastery_score is not None:
        enriched['minimum_mastery_score'] = minimum_mastery_score
    return enriched

def _mcq_question(rng, item, mode="scaffold"):
    mode_norm = str(mode or "").strip().lower()
    correct_option = item['options'][item['correct_index']]
    
    question = {
        'id': f"g8_ems_mcq_{rng.randint(1000, 999999)}",
        'title': item.get('title', 'Concept check'),
        'question_type': 'mcq',
        'prompt': item['prompt'],
        'options': item['options'],
        'correct_index': str(item['correct_index']),
        'explanation': item['explanation'],
        'marks': item.get('marks', 1),
        'sample_answer': correct_option,
        'ideal_answer': correct_option,
        'marking_points': [correct_option],
        **{k: v for k, v in item.items() if k not in ['prompt', 'options', 'correct_index', 'explanation', 'title', 'marks', 'hint_sections', 'guidelines', 'teaching_note']}
    }
    
    if mode_norm == "scaffold":
        if 'hint_sections' in item: question['hint_sections'] = item['hint_sections']
        if 'guidelines' in item: question['guidelines'] = item['guidelines']
        if 'teaching_note' in item: question['teaching_note'] = item.get('teaching_note', item['explanation'])
        
    return question

def _concept_pool(rng):
    scenario = get_ems_scenario()
    money_value = rng.randint(500, 5000)
    
    return [
        _with_metadata({
            'title': 'Source Documents',
            'prompt': f"{scenario['entrepreneur']} receives R{money_value} cash from a customer for services rendered. Which source document should they issue to the customer?",
            'options': [
                "A cheque", 
                "A receipt", 
                "A deposit slip", 
                "A bank statement"
            ],
            'correct_index': 1,
            'explanation': "When a business receives cash, it issues a receipt to the customer as proof of payment.",
            'difficulties': ['easy', 'medium'],
            'marks': 1,
            'hint_sections': {
                '1_nudge': 'What document is given to someone when they hand you cash to prove they paid?',
                '2_concept': 'The business is receiving money, so they must acknowledge the "receipt" of that money.',
                '3_breakdown': 'A deposit slip is for putting money in the bank. A receipt is issued directly to a customer when they pay cash.'
            },
            'guidelines': ['Identify the correct source document for cash received.']
        }, subskill='concepts', learning_objective_id='lo_source_docs', question_family_id='source_docs_classification', concept_id='receipt', concept_group='source_documents', misconception_tags=['confuses_receipt_and_invoice'], diagnostic_tags=['classification', 'accounting']),
        
        _with_metadata({
            'title': 'Accounting Equation Basics',
            'prompt': "Which of the following correctly represents the Accounting Equation?",
            'options': [
                "Assets = Owner's Equity - Liabilities", 
                "Assets = Liabilities - Owner's Equity", 
                "Assets = Owner's Equity + Liabilities", 
                "Owner's Equity = Assets + Liabilities"
            ],
            'correct_index': 2,
            'explanation': "The accounting equation states that the Assets of a business are financed by either the owner (Owner's Equity) or outside parties (Liabilities). Therefore, Assets = Owner's Equity + Liabilities.",
            'difficulties': ['easy'],
            'marks': 1,
            'hint_sections': {
                '1_nudge': 'Think about how a business pays for its possessions. It uses either the owner\'s money or borrowed money.',
                '2_concept': 'Everything the business owns (Assets) must equal how they got it (Owner\'s Equity plus Liabilities).',
                '3_breakdown': 'The correct formula is Assets = Owner\'s Equity + Liabilities (A = OE + L).'
            },
            'guidelines': ['Identify the correct standard formula for the Accounting Equation.']
        }, subskill='concepts', learning_objective_id='lo_acc_equation', question_family_id='equation_formula', concept_id='accounting_equation', concept_group='accounting_equation', misconception_tags=['incorrect_equation_signs'], diagnostic_tags=['definition', 'accounting']),
    ]

def _accounting_equation_pool(rng, mode="scaffold"):
    """
    Generates tabular accounting equation questions.
    Grade 8 format: Assets, Owner's Equity, Liabilities (and effects: +, -, 0).
    """
    scenario = get_ems_scenario()
    
    # Generate 3 random transactions
    transactions = []
    data_rows = []
    cell_hints = {}
    
    # T1: Owner contributes capital
    cap_amount = rng.randint(10, 50) * 1000
    transactions.append(f"1. {scenario['entrepreneur']} started the business by depositing R{cap_amount} into the business bank account.")
    # Assets increase (Bank), OE increases (Capital)
    data_rows.append(["1", f"+R{cap_amount}", f"+R{cap_amount}", "0"])
    
    cell_hints["r0_c1"] = f"Expectation: Change in Assets. Location: Transaction 1 states R{cap_amount} was deposited. Connection: Bank is an asset, so Assets increase by R{cap_amount}."
    cell_hints["r0_c2"] = f"Expectation: Change in Owner's Equity. Location: Transaction 1 states it's for starting the business. Connection: This is Capital, which increases Owner's Equity by R{cap_amount}."
    cell_hints["r0_c3"] = "Expectation: Change in Liabilities. Connection: No money was borrowed, so there is no effect on Liabilities (0)."
    
    # T2: Buy equipment on credit
    equip_amount = rng.randint(2, 8) * 1000
    transactions.append(f"2. Bought equipment on credit from {scenario['competitor']} for R{equip_amount}.")
    # Assets increase (Equipment), Liabilities increase (Creditors)
    data_rows.append(["2", f"+R{equip_amount}", "0", f"+R{equip_amount}"])
    
    cell_hints["r1_c1"] = f"Expectation: Change in Assets. Location: Transaction 2 mentions buying equipment. Connection: Equipment is an asset, so Assets increase by R{equip_amount}."
    cell_hints["r1_c2"] = "Expectation: Change in Owner's Equity. Connection: Buying an asset on credit does not affect income, expenses, or capital. Therefore, OE is 0."
    cell_hints["r1_c3"] = f"Expectation: Change in Liabilities. Location: Transaction 2 mentions buying 'on credit'. Connection: We owe money to a creditor, which increases Liabilities by R{equip_amount}."

    # T3: Pay rent
    rent_amount = rng.randint(1, 5) * 500
    transactions.append(f"3. Paid rent via EFT for the month, R{rent_amount}.")
    # Assets decrease (Bank), OE decreases (Expense)
    data_rows.append(["3", f"-R{rent_amount}", f"-R{rent_amount}", "0"])
    
    cell_hints["r2_c1"] = f"Expectation: Change in Assets. Location: Transaction 3 mentions paying via EFT. Connection: Money leaves the Bank (an asset), so Assets decrease by R{rent_amount}."
    cell_hints["r2_c2"] = f"Expectation: Change in Owner's Equity. Location: Transaction 3 mentions 'Paid rent'. Connection: Rent is an expense. Expenses decrease profit, thereby decreasing Owner's Equity by R{rent_amount}."
    cell_hints["r2_c3"] = "Expectation: Change in Liabilities. Connection: Paying an expense immediately does not create or settle a debt. So Liabilities is 0."

    ui_rows = []
    correct_map = {}
    for i, row in enumerate(data_rows):
        ui_row = []
        for j, val in enumerate(row):
            correct_map[f"r{i}_c{j}"] = val
            ui_row.append({"value": row[0] if j == 0 else "", "cell_id": f"r{i}_c{j}", "editable": j > 0})
        ui_rows.append(ui_row)

    headers = ["No.", "Assets", "Owner's Equity", "Liabilities"]
    
    # Determine which columns are editable based on scaffold vs practice. 
    # In scaffold, maybe all effect columns.
    editable_cols = [1, 2, 3]

    item = {
        "id": f"ems_accteq_{random.randint(1000, 9999)}",
        "topic": "The Accounting Equation",
        "prompt": f"Analyse the following transactions for {scenario['entrepreneur']}'s new business in {scenario['area']}. Indicate the effect on the accounting equation (Assets, Owner's Equity, Liabilities) using a + for increase, - for decrease, and 0 for no change, followed by the amount (e.g., +R5000 or 0).",
        "transactions": transactions,
        "question_type": "journal",
        "journal": {
            "journal_type": "accounting_equation",
            "headers": headers,
            "rows": ui_rows
        },
        "editable_cols": editable_cols,
        "correct_map": correct_map,
        "cell_hints": cell_hints,
        'marks': 9, # 3 transactions * 3 columns
        'sample_answer': 'See completed table',
        'ideal_answer': 'See completed table',
        'marking_points': ['Correct effects applied to Assets, OE, and Liabilities for all transactions.'],
        'hint_sections': {
            '1_nudge': 'Remember the equation: Assets = Owner\'s Equity + Liabilities. Every transaction must keep this equation balanced.',
            '2_concept': 'Identify the two accounts involved in each transaction. e.g. "Paid rent" affects Bank and Rent Expense.',
            '3_breakdown': 'Bank is an asset (decreases when paying). Rent is an expense (decreases Owner\'s Equity). Therefore, A decreases and OE decreases.'
        },
        'guidelines': ['Ensure the equation A = OE + L remains balanced for every row. Use 0 for no effect.'],
        'teaching_note': 'Grade 8 learners often forget to include the sign (+ or -) or leave cells blank instead of writing 0.'
    }
    
    return [_with_metadata(item, subskill='accounting_equation', learning_objective_id='lo_acc_equation_practical', question_family_id='equation_table', concept_id='equation_practical', concept_group='accounting_equation', diagnostic_tags=['tabular', 'accounting'])]

def generate(subskill="concepts", difficulty="medium", count=1, mode="scaffold", seed=None, **kwargs):
    rng = _rng(seed)
    
    if subskill == "accounting_equation":
        pool = _accounting_equation_pool(rng, mode)
        selected = pool
        chosen = rng.sample(selected, min(count, len(selected)))
        # Return as-is since the pool generates the exact structure
        return chosen
    else:
        pool = _concept_pool(rng)
        selected = [q for q in pool if difficulty in q['difficulty_band']]
        if not selected: selected = pool
        chosen = rng.sample(selected, min(count, len(selected)))
        return [_mcq_question(rng, item, mode=mode) for item in chosen]
