import random
from app.utils.ems_namelist import get_ems_scenario, get_random_need_and_want

def _rng(seed=None):
    return random.Random(seed)

TOPIC_ID = 'grade8_ems'
SUBTOPIC_ID = 'term2_crj'
CURRICULUM_REFERENCE = 'Term 2 > Cash Receipts Journal of a services business'

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

def _crj_table_pool(rng, mode="scaffold"):
    """
    Generates tabular CRJ questions.
    Grade 8 CRJ columns: Doc No, Day, Details, Analysis of Receipts, Bank, Current Income, Sundry Accounts Amount, Sundry Accounts Details.
    """
    scenario = get_ems_scenario()
    business_name = f"{scenario['entrepreneur']} {scenario['business_type']}s"
    month = "May 2024"
    
    # Generate 3 distinct CRJ transactions
    transactions = []
    data_rows = []
    cell_hints = {}
    
    # Row 1: Capital contribution (Direct deposit)
    cap_amount = rng.randint(5, 50) * 1000
    transactions.append(f"Day 2: {scenario['entrepreneur']} deposited R{cap_amount} directly into the business bank account as capital. Receipt 01 was issued.")
    # Doc No, Day, Details, Analysis, Bank, Current Income, Sundry Amt, Sundry Details
    data_rows.append(["Rec 01", "2", scenario['entrepreneur'], "", str(cap_amount), "", str(cap_amount), "Capital"])
    
    cell_hints["r0_c0"] = "Expectation: The document number. Location: Transaction states 'Receipt 01'. Connection: Write 'Rec 01'."
    cell_hints["r0_c1"] = "Expectation: The day of the transaction. Location: Transaction states 'Day 2'."
    cell_hints["r0_c2"] = f"Expectation: The name of the person or entity giving the money. Location: Transaction states {scenario['entrepreneur']} deposited the money."
    cell_hints["r0_c3"] = "Expectation: The till/cash register amount. Connection: A direct deposit does not go into the till, so Analysis of Receipts is left blank."
    cell_hints["r0_c4"] = f"Expectation: Total banked for the day. Location: R{cap_amount} was deposited directly into Bank."
    cell_hints["r0_c5"] = "Expectation: Current Income. Connection: This is a capital contribution, not service income, so leave blank."
    cell_hints["r0_c6"] = f"Expectation: Sundry accounts amount. Connection: Since it is not Current Income, the R{cap_amount} must be recorded in Sundry Accounts."
    cell_hints["r0_c7"] = "Expectation: The name of the account for the Sundry amount. Connection: The transaction states the money is 'as capital', so the account is 'Capital'."

    # Row 2: Cash services rendered (till slip)
    serv_amount = rng.randint(2, 9) * 100
    transactions.append(f"Day 15: Cash received for services rendered, R{serv_amount} according to the cash register roll (CRR 1).")
    data_rows.append(["CRR 1", "15", "Services rendered", str(serv_amount), str(serv_amount), str(serv_amount), "", ""])
    
    cell_hints["r1_c0"] = "Expectation: Document number. Location: Transaction mentions 'CRR 1'."
    cell_hints["r1_c1"] = "Expectation: Day. Location: 'Day 15'."
    cell_hints["r1_c2"] = "Expectation: Details. Connection: For cash register rolls where multiple cash customers paid, we write 'Services rendered' or 'Sales'."
    cell_hints["r1_c3"] = f"Expectation: Analysis of receipts. Connection: Money received in the till is first recorded here. Amount is R{serv_amount}."
    cell_hints["r1_c4"] = f"Expectation: Total banked for the day. Connection: If this is the only transaction on Day 15, the whole R{serv_amount} from Analysis of receipts is deposited."
    cell_hints["r1_c5"] = f"Expectation: Current Income. Connection: The money was for 'services rendered', which is Current Income. Write R{serv_amount}."
    cell_hints["r1_c6"] = "Expectation: Sundry amount. Connection: Already recorded under Current Income, so leave blank."
    cell_hints["r1_c7"] = "Expectation: Sundry details. Connection: Leave blank."

    # Row 3: Rent Income (Receipt)
    rent_amount = rng.randint(1, 5) * 500
    transactions.append(f"Day 28: Issued Receipt 02 to J. Smith for rent of a spare room, R{rent_amount}.")
    data_rows.append(["Rec 02", "28", "J. Smith", str(rent_amount), str(rent_amount), "", str(rent_amount), "Rent Income"])
    
    cell_hints["r2_c0"] = "Expectation: Document number. Location: 'Receipt 02'."
    cell_hints["r2_c1"] = "Expectation: Day. Location: 'Day 28'."
    cell_hints["r2_c2"] = "Expectation: Details. Location: The receipt was issued to 'J. Smith'."
    cell_hints["r2_c3"] = f"Expectation: Analysis of receipts. Connection: Rent paid in cash/cheque goes into the till first. Amount is R{rent_amount}."
    cell_hints["r2_c4"] = f"Expectation: Bank. Connection: The money from the till is deposited. Amount is R{rent_amount}."
    cell_hints["r2_c5"] = "Expectation: Current Income. Connection: Rent is not from normal services rendered, so leave blank."
    cell_hints["r2_c6"] = f"Expectation: Sundry amount. Connection: Since it is not Current Income, the R{rent_amount} goes to Sundry Accounts."
    cell_hints["r2_c7"] = "Expectation: Sundry details. Connection: The money was received for rent, so the account is 'Rent Income'."

    for i, row in enumerate(data_rows):
        ui_row = []
        for j, val in enumerate(row):
            correct_map[f"r{i}_c{j}"] = val
            ui_row.append({"value": "", "cell_id": f"r{i}_c{j}", "editable": True})
        ui_rows.append(ui_row)

    headers = ["Doc No", "Day", "Details", "Analysis of Receipts", "Bank", "Current Income", "Sundry Amount", "Sundry Details"]
    
    # In scaffold mode, we typically want them to fill out everything
    editable_cols = [0, 1, 2, 3, 4, 5, 6, 7]

    item = {
        "id": f"ems_crj_{random.randint(1000, 9999)}",
        "topic": "Cash Receipts Journal",
        "question_type": "journal",
        "prompt": f"Use the following transactions to complete the Cash Receipts Journal of {business_name} for {month}. Leave cells blank if they do not require an entry.",
        "journal": {
            "journal_type": "crj",
            "headers": headers,
            "rows": ui_rows
        },
        "editable_cols": editable_cols,
        "correct_map": correct_map,
        "cell_hints": cell_hints,
        'transactions': transactions,
        'marks': 24, # 3 rows * 8 columns
        'sample_answer': 'See completed table',
        'ideal_answer': 'See completed table',
        'marking_points': ['Correctly recorded doc numbers, details, and allocated amounts to Bank and correct analysis columns.'],
        'hint_sections': {
            '1_nudge': 'The CRJ is used to record all money RECEIVED by the business.',
            '2_concept': 'Money received goes into Analysis of Receipts first, unless it is a direct deposit. Then it goes to Bank, and finally is classified as either Current Income or a Sundry Account.',
            '3_breakdown': 'Remember: Bank = Current Income + Sundry Accounts for each day.'
        },
        'guidelines': ['Ensure direct deposits bypass Analysis of Receipts.', 'Check that Bank = Current Income + Sundry Amount for each transaction.'],
        'teaching_note': 'Grade 8 learners often struggle with direct deposits (putting them in Analysis of Receipts incorrectly) and omitting the Sundry Details name.'
    }
    
    return [_with_metadata(item, subskill='crj', learning_objective_id='lo_crj_practical', question_family_id='crj_table', concept_id='crj_practical', concept_group='journals', diagnostic_tags=['tabular', 'accounting'])]

def generate(subskill="crj", difficulty="medium", count=1, mode="scaffold", seed=None, **kwargs):
    rng = _rng(seed)
    
    pool = _crj_table_pool(rng, mode)
    selected = pool
    chosen = rng.sample(selected, min(count, len(selected)))
    return chosen
