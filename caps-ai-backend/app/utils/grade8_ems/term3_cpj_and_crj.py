import random
from app.utils.ems_namelist import get_ems_scenario

def _rng(seed=None):
    return random.Random(seed)

TOPIC_ID = 'grade8_ems'
SUBTOPIC_ID = 'term3_cpj_and_crj'
CURRICULUM_REFERENCE = 'Term 3 > Cash Payments Journal of a services business'

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

def _cpj_table_pool(rng, mode="scaffold"):
    """
    Generates tabular CPJ questions.
    Grade 8 CPJ columns: Doc No, Day, Name of Payee, Bank, Wages, Stationery, Sundry Accounts Amount, Sundry Accounts Details.
    """
    scenario = get_ems_scenario()
    business_name = f"{scenario['entrepreneur']} {scenario['business_type']}s"
    month = "July 2024"
    
    transactions = []
    data_rows = []
    cell_hints = {}
    
    # Row 1: Pay Wages
    wages_amount = rng.randint(5, 15) * 100
    transactions.append(f"Day 7: Cashed Cheque 101 to pay the weekly workers, R{wages_amount}.")
    data_rows.append(["101", "7", "Cash", str(wages_amount), str(wages_amount), "", "", ""])
    
    cell_hints["r0_c0"] = "Expectation: The document number. Location: Transaction states 'Cheque 101'."
    cell_hints["r0_c1"] = "Expectation: The day of the transaction. Location: 'Day 7'."
    cell_hints["r0_c2"] = "Expectation: Name of payee. Connection: When cashing a cheque to pay wages, the payee is usually 'Cash'."
    cell_hints["r0_c3"] = f"Expectation: Bank amount. Connection: Every payment goes through Bank. Amount is R{wages_amount}."
    cell_hints["r0_c4"] = f"Expectation: Wages amount. Connection: The payment was for workers, so write R{wages_amount} in the Wages column."
    cell_hints["r0_c5"] = "Expectation: Stationery amount. Connection: Leave blank."
    cell_hints["r0_c6"] = "Expectation: Sundry amount. Connection: Already recorded in Wages, so leave blank."
    cell_hints["r0_c7"] = "Expectation: Sundry details. Connection: Leave blank."

    # Row 2: Buy Equipment & Stationery from a single cheque
    stat_amt = rng.randint(1, 5) * 100
    equip_amt = rng.randint(20, 50) * 100
    total_amt = stat_amt + equip_amt
    transactions.append(f"Day 12: Issued Cheque 102 to {scenario['competitor']} for a new computer (R{equip_amt}) and printing paper (R{stat_amt}).")
    data_rows.append(["102", "12", scenario['competitor'], str(total_amt), "", str(stat_amt), str(equip_amt), "Equipment"])
    
    cell_hints["r1_c0"] = "Expectation: Document number. Location: 'Cheque 102'."
    cell_hints["r1_c1"] = "Expectation: Day. Location: 'Day 12'."
    cell_hints["r1_c2"] = f"Expectation: Name of Payee. Location: Cheque was issued to '{scenario['competitor']}'."
    cell_hints["r1_c3"] = f"Expectation: Bank amount. Formula: Total of both items = {stat_amt} + {equip_amt} = R{total_amt}."
    cell_hints["r1_c4"] = "Expectation: Wages. Connection: Leave blank."
    cell_hints["r1_c5"] = f"Expectation: Stationery. Connection: Printing paper is stationery. Write R{stat_amt}."
    cell_hints["r1_c6"] = f"Expectation: Sundry amount. Connection: The remaining R{equip_amt} for the computer goes here."
    cell_hints["r1_c7"] = "Expectation: Sundry details. Connection: A computer is classified as 'Equipment'."

    # Row 3: Drawings
    draw_amt = rng.randint(2, 9) * 100
    transactions.append(f"Day 25: {scenario['entrepreneur']} withdrew cash via ATM for personal use, R{draw_amt}. (Use BS1 as document number for Bank Statement)")
    data_rows.append(["BS1", "25", scenario['entrepreneur'], str(draw_amt), "", "", str(draw_amt), "Drawings"])
    
    cell_hints["r2_c0"] = "Expectation: Document number. Location: Transaction instructs to use 'BS1'."
    cell_hints["r2_c1"] = "Expectation: Day. Location: 'Day 25'."
    cell_hints["r2_c2"] = f"Expectation: Name of payee. Location: The owner {scenario['entrepreneur']} took the money."
    cell_hints["r2_c3"] = f"Expectation: Bank amount. Connection: Money left the bank account, R{draw_amt}."
    cell_hints["r2_c4"] = "Expectation: Wages. Connection: Leave blank."
    cell_hints["r2_c5"] = "Expectation: Stationery. Connection: Leave blank."
    cell_hints["r2_c6"] = f"Expectation: Sundry amount. Connection: Personal use is not wages or stationery. Write R{draw_amt}."
    cell_hints["r2_c7"] = "Expectation: Sundry details. Connection: Money taken for personal use is called 'Drawings'."

    ui_rows = []
    for i, row in enumerate(data_rows):
        ui_row = []
        for j, val in enumerate(row):
            correct_map[f"r{i}_c{j}"] = val
            ui_row.append({"value": "", "cell_id": f"r{i}_c{j}", "editable": True})
        ui_rows.append(ui_row)

    headers = ["Doc No", "Day", "Name of Payee", "Bank", "Wages", "Stationery", "Sundry Amount", "Sundry Details"]
    
    editable_cols = [0, 1, 2, 3, 4, 5, 6, 7]

    item = {
        "id": f"ems_cpj_{random.randint(1000, 9999)}",
        "topic": "Cash Payments Journal",
        "question_type": "journal",
        "prompt": f"Use the following transactions to complete the Cash Payments Journal of {business_name} for {month}. Leave cells blank if they do not require an entry.",
        "transactions": transactions,
        "journal": {
            "journal_type": "cpj",
            "headers": headers,
            "rows": ui_rows
        },
        "editable_cols": editable_cols,
        "correct_map": correct_map,
        "cell_hints": cell_hints,
        'marks': 24, # 3 rows * 8 columns
        'sample_answer': 'See completed table',
        'ideal_answer': 'See completed table',
        'marking_points': ['Correctly recorded doc numbers, payees, and allocated amounts to Bank and correct analysis columns.'],
        'hint_sections': {
            '1_nudge': 'The CPJ is used to record all money PAID out by the business.',
            '2_concept': 'Every single payment must have an amount in the Bank column. Then, you distribute that exact amount into the analysis columns (like Wages or Stationery).',
            '3_breakdown': 'If an item does not have its own dedicated analysis column, it must go to the Sundry Accounts with the correct account name.'
        },
        'guidelines': ['Check that Bank = Sum of all analysis columns for each row.'],
        'teaching_note': 'Grade 8 learners often split Bank amounts incorrectly when buying multiple items on one cheque.'
    }
    
    return [_with_metadata(item, subskill='cpj', learning_objective_id='lo_cpj_practical', question_family_id='cpj_table', concept_id='cpj_practical', concept_group='journals', diagnostic_tags=['tabular', 'accounting'])]

def generate(subskill="cpj", difficulty="medium", count=1, mode="scaffold", seed=None, **kwargs):
    rng = _rng(seed)
    
    pool = _cpj_table_pool(rng, mode)
    selected = pool
    chosen = rng.sample(selected, min(count, len(selected)))
    return chosen
