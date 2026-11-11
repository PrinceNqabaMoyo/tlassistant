import random
from app.utils.ems_namelist import get_ems_scenario, NAMES

def _rng(seed=None):
    return random.Random(seed)

TOPIC_ID = 'grade7_ems'
SUBTOPIC_ID = 'term2_income_and_expenses'
CURRICULUM_REFERENCE = 'Term 2 > Income and Expenses'

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
        'subskill': question_family_id or subskill,
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

def _concept_pool(rng):
    """Dynamic concept pool with 6 distinct CAPS archetypes."""
    scenario = get_ems_scenario(rng)
    return [
        _with_metadata({
            'title': 'Defining Personal Income',
            'prompt': f"{scenario['entrepreneur']} from {scenario['area']} calculates total annual household earnings. Which of the following best defines personal income?",
            'options': [
                "The total amount of money a business makes in a year before expenses.", 
                "An individual's total annual earnings from all sources such as wages, investments, and rent.", 
                "The amount of money owed to a bank for a personal loan.", 
                "The total value of a person's assets minus their liabilities."
            ],
            'correct_index': 1,
            'explanation': "Personal income is an individual's total earnings from all sources. The difference between assets and liabilities is Net Worth.",
            'difficulties': ['easy', 'medium'],
            'marks': 1,
            'hint_sections': [
                {'title': 'What is being tested?', 'text': 'Understanding the definition of personal income.'},
                {'title': 'Reasoning path', 'text': 'Look for the option that describes money coming INTO an individual\'s pocket from various sources.'},
                {'title': 'Transfer idea', 'text': 'Personal income includes salaries, wages, dividends, and interest.'}
            ],
            'guidelines': ['Identify the correct definition of personal income.']
        }, subskill='concepts', learning_objective_id='lo_personal_income', question_family_id='def_personal_income', concept_id='personal_income', concept_group='income_and_expenses', misconception_tags=['confuses_income_with_net_worth'], diagnostic_tags=['definition']),
        _with_metadata({
            'title': 'Defining Personal Expenses',
            'prompt': f"When {scenario['entrepreneur']} reviews monthly household spending in {scenario['area']}, which of the following is classified as a VARIABLE personal expense?",
            'options': [
                "Dining out at restaurants and entertainment",
                "Fixed monthly car insurance premium",
                "Monthly bond repayment on a flat",
                "Annual school tuition fee paid in fixed monthly installments"
            ],
            'correct_index': 0,
            'explanation': "Variable personal expenses change based on lifestyle choices and day-to-day decisions, such as entertainment, clothing, and dining out.",
            'difficulties': ['easy', 'medium'],
            'marks': 1,
            'hint_sections': [
                {'title': 'What is being tested?', 'text': 'Differentiating variable expenses from contractual fixed expenses.'},
                {'title': 'Reasoning path', 'text': 'Which of these expenses can you easily cut down immediately during a financially tight month?'},
                {'title': 'Transfer idea', 'text': 'Variable expenses are discretionary and easiest to adjust when balancing a personal budget.'}
            ],
            'guidelines': ['Identify the expense that fluctuates by personal choice.']
        }, subskill='concepts', learning_objective_id='lo_personal_expenses', question_family_id='def_personal_expenses', concept_id='personal_expenses', concept_group='income_and_expenses', misconception_tags=['confuses_fixed_with_variable'], diagnostic_tags=['classification']),
        _with_metadata({
            'title': 'Understanding Assets',
            'prompt': f"{scenario['entrepreneur']} in {scenario['area']} prepares a list of possessions. Which of the following items owned by an individual is classified as an ASSET?",
            'options': [
                "A fully paid family motor vehicle and cash in a savings account",
                "An outstanding student study loan owed to the bank",
                "Monthly credit card debt for clothing purchases",
                "An unpaid municipal water bill"
            ],
            'correct_index': 0,
            'explanation': "Assets are possessions and property of financial value that a person owns (vehicles, houses, savings, investments). Debts owed to others are liabilities.",
            'difficulties': ['easy', 'medium'],
            'marks': 1,
            'hint_sections': [
                {'title': 'What is being tested?', 'text': 'Identifying assets versus liabilities.'},
                {'title': 'Reasoning path', 'text': 'Assets are what you OWN; liabilities are what you OWE.'},
                {'title': 'Transfer idea', 'text': 'Assets put money in your pocket or hold resale value.'}
            ],
            'guidelines': ['Identify possessions of economic value owned by the person.']
        }, subskill='concepts', learning_objective_id='lo_personal_assets', question_family_id='identify_assets', concept_id='assets', concept_group='income_and_expenses', misconception_tags=['confuses_assets_with_liabilities'], diagnostic_tags=['terminology']),
        _with_metadata({
            'title': 'Understanding Liabilities',
            'prompt': f"{scenario['entrepreneur']} in {scenario['area']} reviews business debts. Which of the following is the best definition of a financial LIABILITY?",
            'options': [
                "Money, debt, or financial obligations that an individual or business owes to outside parties",
                "The total cash deposited into a fixed 32-day bank account",
                "The original purchase price of trading equipment",
                "The net profit generated from selling second-hand goods"
            ],
            'correct_index': 0,
            'explanation': "A liability is a legal debt or obligation owed to another person, business, or financial institution (e.g. loans, credit cards, bank overdrafts).",
            'difficulties': ['medium'],
            'marks': 1,
            'hint_sections': [
                {'title': 'What is being tested?', 'text': 'Defining financial liabilities.'},
                {'title': 'Reasoning path', 'text': 'If you borrow money to buy a computer, what is the money you still have to repay called?'},
                {'title': 'Transfer idea', 'text': 'Liabilities decrease your total net worth until settled.'}
            ],
            'guidelines': ['Focus on financial obligations owed to others.']
        }, subskill='concepts', learning_objective_id='lo_personal_liabilities', question_family_id='identify_liabilities', concept_id='liabilities', concept_group='income_and_expenses', misconception_tags=['confuses_debt_with_asset'], diagnostic_tags=['definition']),
        _with_metadata({
            'title': 'The Net Worth Formula',
            'prompt': f"When {scenario['entrepreneur']} in {scenario['area']} calculates personal net worth, what is the correct mathematical formula to calculate an individual's personal Net Worth?",
            'options': [
                "Net Worth = Total Assets - Total Liabilities",
                "Net Worth = Total Liabilities - Total Assets",
                "Net Worth = Monthly Income + Monthly Expenses",
                "Net Worth = Total Capital × Interest Rate"
            ],
            'correct_index': 0,
            'explanation': "Net Worth is the true financial value of an individual: what they OWN (Assets) minus what they OWE (Liabilities).",
            'difficulties': ['easy', 'medium'],
            'marks': 1,
            'hint_sections': [
                {'title': 'What is being tested?', 'text': 'The fundamental Net Worth equation.'},
                {'title': 'Reasoning path', 'text': 'Take everything you possess (Assets) and pay off every single debt (Liabilities). What remains is your Net Worth.'},
                {'title': 'Transfer idea', 'text': 'Assets - Liabilities = Owner\'s Equity / Net Worth.'}
            ],
            'guidelines': ['Select the subtraction of liabilities from assets.']
        }, subskill='concepts', learning_objective_id='lo_net_worth_formula', question_family_id='net_worth_equation', concept_id='net_worth_formula', concept_group='income_and_expenses', misconception_tags=['inverts_subtraction_order'], diagnostic_tags=['equation_rule']),
        _with_metadata({
            'title': 'Personal Savings & Wealth Creation',
            'prompt': f"If {scenario['entrepreneur']} in {scenario['area']} earns R20 000 per month, spends R16 000 on essential expenses, and deposits R4 000 into an investment account, what does the R4 000 represent?",
            'options': [
                "Personal savings / investment contributing to future wealth creation",
                "A non-operating fixed expenditure loss",
                "A short-term current liability debt",
                "A penalty fine payable to the bank"
            ],
            'correct_index': 0,
            'explanation': "Money saved from current disposable income and invested into interest-bearing assets increases personal wealth and future net worth.",
            'difficulties': ['medium', 'hard'],
            'marks': 1,
            'hint_sections': [
                {'title': 'What is being tested?', 'text': 'Understanding the role of savings in building wealth.'},
                {'title': 'Reasoning path', 'text': 'When income exceeds living expenses, the surplus saved builds assets over time.'},
                {'title': 'Transfer idea', 'text': 'Income - Expenses = Surplus (Savings).' }
            ],
            'guidelines': ['Connect personal savings to asset and wealth growth.']
        }, subskill='concepts', learning_objective_id='lo_savings_wealth', question_family_id='savings_wealth_creation', concept_id='savings_wealth', concept_group='income_and_expenses', misconception_tags=['considers_savings_an_expense'], diagnostic_tags=['financial_literacy']),
    ]

def _calculation_pool(rng):
    """Unlimited calculations for Net Worth."""
    person_name = rng.choice(NAMES)
    
    # Generate random asset values
    house_val = rng.randint(400, 900) * 1000
    car_val = rng.randint(50, 150) * 1000
    bank_val = rng.randint(10, 50) * 1000
    total_assets = house_val + car_val + bank_val
    
    # Generate random liability values
    house_debt = rng.randint(200, 400) * 1000
    car_debt = rng.randint(10, 40) * 1000
    total_liabilities = house_debt + car_debt
    
    net_worth = total_assets - total_liabilities
    
    return [
        _with_metadata({
            'title': 'Calculate Net Worth',
            'prompt': f"{person_name} owns a house worth R{house_val:,}. They still owe the bank R{house_debt:,} on the bond. {person_name} also financed a car worth R{car_val:,} and still owes R{car_debt:,} on it. They have R{bank_val:,} in cash in their bank account.\n\nCalculate {person_name}'s net worth.",
            'correct_value': net_worth,
            'explanation': f"Net Worth = Total Assets - Total Liabilities.\nAssets: House (R{house_val:,}) + Car (R{car_val:,}) + Bank (R{bank_val:,}) = R{total_assets:,}.\nLiabilities: Bond (R{house_debt:,}) + Car Debt (R{car_debt:,}) = R{total_liabilities:,}.\nNet Worth = R{total_assets:,} - R{total_liabilities:,} = R{net_worth:,}.",
            'difficulties': ['medium', 'hard'],
            'marks': 3,
            'hint_sections': [
                {'title': 'What is being tested?', 'text': 'Calculating Net Worth using the fundamental accounting equation.'},
                {'title': 'Reasoning path', 'text': 'First, add up all the things they OWN (Assets). Second, add up all the things they OWE (Liabilities). Finally, subtract Liabilities from Assets.'},
                {'title': 'Transfer idea', 'text': 'Net worth is the true financial value of a person or business after all debts are paid off.'}
            ],
            'guidelines': ['Look for the final numerical answer representing Assets minus Liabilities.'],
            'teaching_note': '1 mark for total assets, 1 mark for total liabilities, 1 mark for final answer.'
        }, subskill='calculations', learning_objective_id='lo_calculate_net_worth', question_family_id='net_worth_math', concept_id='net_worth', concept_group='income_and_expenses', misconception_tags=['subtracts_assets_from_liabilities'], diagnostic_tags=['calculation', 'math']),
    ]

def _journal_pool(rng):
    """Renders an interactive Statement of Net Worth table."""
    person = rng.choice(NAMES)
    
    bed = rng.randint(3000, 8000)
    laptop = rng.randint(4000, 10000)
    phone = rng.randint(2000, 6000)
    total_assets = bed + laptop + phone
    total_liabilities = 0
    net_worth = total_assets - total_liabilities
    
    headers = ["Classification", "Item / Description", "Amount (R)"]
    rows = [
        [{"cell_id": "r0_c0", "value": "ASSETS", "editable": False}, {"cell_id": "r0_c1", "value": "Bed & Furniture", "editable": False}, {"cell_id": "r0_c2", "value": f"{bed}", "editable": False}],
        [{"cell_id": "r1_c0", "value": "ASSETS", "editable": False}, {"cell_id": "r1_c1", "value": "Study Laptop", "editable": False}, {"cell_id": "r1_c2", "value": f"{laptop}", "editable": False}],
        [{"cell_id": "r2_c0", "value": "ASSETS", "editable": False}, {"cell_id": "r2_c1", "value": "Smartphone", "editable": False}, {"cell_id": "r2_c2", "value": f"{phone}", "editable": False}],
        [{"cell_id": "r3_c0", "value": "TOTAL ASSETS", "editable": False}, {"cell_id": "r3_c1", "value": "Total value of all possessions", "editable": False}, {"cell_id": "r3_c2", "value": "", "expected": str(total_assets), "editable": True}],
        [{"cell_id": "r4_c0", "value": "LIABILITIES", "editable": False}, {"cell_id": "r4_c1", "value": "Total Debts Owed", "editable": False}, {"cell_id": "r4_c2", "value": "0", "editable": False}],
        [{"cell_id": "r5_c0", "value": "NET WORTH", "editable": False}, {"cell_id": "r5_c1", "value": "Total Assets minus Liabilities", "editable": False}, {"cell_id": "r5_c2", "value": "", "expected": str(net_worth), "editable": True}],
    ]
    correct_map = {
        "r3_c2": str(total_assets),
        "r5_c2": str(net_worth),
    }
    
    return [
        _with_metadata({
            'title': 'Statement of Net Worth',
            'prompt': f"{person} has made a list of personal possessions: Bed (R{bed}), Study Laptop (R{laptop}), and Smartphone (R{phone}). {person} currently has zero debts.\n\nComplete the interactive Statement of Net Worth below by calculating:\n1. Total Assets\n2. Net Worth (Total Assets − Total Liabilities).",
            'marks': 4,
            'modality': 'ledger',
            'question_type': 'journal',
            'solution_type': 'tabular_cells',
            'headers': headers,
            'rows': rows,
            'correct_map': correct_map,
            'expected_answer': f"Total Assets = R{total_assets:,}; Net Worth = R{net_worth:,}",
            'sample_answer': f"Total Assets = R{total_assets:,}; Net Worth = R{net_worth:,}",
            'worked_solution': f"Total Assets = R{bed:,} + R{laptop:,} + R{phone:,} = R{total_assets:,}.\nTotal Liabilities = R0.\nNet Worth = R{total_assets:,} - R0 = R{net_worth:,}.",
            'explanation': f"Total Assets = R{bed:,} + R{laptop:,} + R{phone:,} = R{total_assets:,}. Net Worth = R{total_assets:,} - R0 = R{net_worth:,}.",
            'canonical_solution': f"Total Assets = R{total_assets:,}; Net Worth = R{net_worth:,}",
            'difficulties': ['medium', 'hard'],
            'hints': {
                'tier_1': 'Add up the three asset values to find Total Assets.',
                'tier_2': f'Total Assets = R{bed} + R{laptop} + R{phone}. Since Liabilities are 0, Net Worth equals Total Assets.',
                'tier_3': f'Total Assets: {total_assets}; Net Worth: {net_worth}.'
            },
        }, subskill='render_statement_net_worth', learning_objective_id='lo_statement_net_worth', question_family_id='render_statement_net_worth', concept_id='statement_of_net_worth', concept_group='income_and_expenses', misconception_tags=['fails_to_sum_assets'], diagnostic_tags=['table_rendering', 'accounting']),
    ]



SUBSKILLS = ['def_personal_income', 'def_personal_expenses', 'identify_assets', 'identify_liabilities', 'net_worth_equation', 'net_worth_math', 'render_statement_net_worth', 'savings_wealth_creation']



SUBSKILLS = ['def_personal_income', 'def_personal_expenses', 'identify_assets', 'identify_liabilities', 'net_worth_equation', 'net_worth_math', 'render_statement_net_worth', 'savings_wealth_creation']

def _mcq_question(rng, item, mode="scaffold"):
    mode_norm = str(mode or "").strip().lower()
    correct_option = item['options'][item['correct_index']]
    explanation = item.get('explanation') or f"The correct option is: {correct_option}."
    sample_answer = correct_option
    
    # 3-tier hints
    if 'hints' in item:
        hints = item['hints']
    elif 'hint_sections' in item and len(item['hint_sections']) >= 3:
        hints = {
            'tier_1': item['hint_sections'][0]['text'],
            'tier_2': item['hint_sections'][1]['text'],
            'tier_3': item['hint_sections'][2]['text']
        }
    else:
        hints = {
            'tier_1': "Carefully review the economic definitions and scenarios presented.",
            'tier_2': explanation,
            'tier_3': f"The correct answer is: {correct_option}."
        }

    marks = item.get('marks', 2)
    question = {
        'id': f"g7_ems_mcq_{rng.randint(1000, 999999)}",
        'title': item.get('title', 'Concept check'),
        'question_type': 'mcq',
        'prompt': item['prompt'],
        'options': item['options'],
        'correct_index': str(item['correct_index']),
        'explanation': explanation,
        'worked_solution': explanation,
        'canonical_solution': explanation,
        'solution': explanation,
        'marks': marks,
        'total_marks': marks,
        'sample_answer': sample_answer,
        'ideal_answer': sample_answer,
        'correct_answer': sample_answer,
        'marking_points': [correct_option],
        'modality': 'math',
        'solution_type': 'mcq',
        'hints': hints,
        'marking_schema': {
            'total_marks': marks,
            'marking_points': [
                {'id': 'mp_1', 'desc': f"Correct option selection: {correct_option}", 'marks': marks, 'editable': True}
            ]
        },
        **{k: v for k, v in item.items() if k not in ['prompt', 'options', 'correct_index', 'explanation', 'title', 'marks', 'hint_sections', 'guidelines', 'teaching_note', 'hints']}
    }
    if mode_norm == "scaffold":
        if 'hint_sections' in item: question['hint_sections'] = item['hint_sections']
        if 'guidelines' in item: question['guidelines'] = item['guidelines']
        if 'teaching_note' in item: question['teaching_note'] = item.get('teaching_note', explanation)
    return question

def _typed_question(rng, item, mode="scaffold"):
    mode_norm = str(mode or "").strip().lower()
    memo = item.get('sample_answer') or item.get('explanation') or "\n".join(item.get('marking_points', []))
    marks = item.get('marks', 3)
    mps = item.get('marking_points', [memo])
    
    # 3-tier hints
    if 'hints' in item:
        hints = item['hints']
    elif 'hint_sections' in item and len(item['hint_sections']) >= 3:
        hints = {
            'tier_1': item['hint_sections'][0]['text'],
            'tier_2': item['hint_sections'][1]['text'],
            'tier_3': item['hint_sections'][2]['text']
        }
    else:
        hints = {
            'tier_1': "Structure your answer clearly, addressing all parts of the question prompt.",
            'tier_2': "Identify the core economic principles, definitions, or calculations required.",
            'tier_3': f"Model solution points:\n{memo}"
        }

    question = {
        'id': f"g7_ems_typed_{rng.randint(1000, 999999)}",
        'title': item.get('title', 'Written response'),
        'question_type': 'typed',
        'prompt': item['prompt'],
        'marks': marks,
        'total_marks': marks,
        'marking_points': mps,
        'sample_answer': memo,
        'ideal_answer': item.get('ideal_answer', memo),
        'correct_answer': memo,
        'explanation': memo,
        'worked_solution': memo,
        'canonical_solution': memo,
        'solution': memo,
        'modality': 'semantic',
        'solution_type': 'marking_points',
        'hints': hints,
        'marking_schema': {
            'total_marks': marks,
            'marking_points': [
                {'id': f"mp_{idx + 1}", 'desc': str(p), 'marks': 1, 'editable': True}
                for idx, p in enumerate(mps)
            ],
            'carry_forward_rule': 'consequential_accuracy'
        },
        **{k: v for k, v in item.items() if k not in ['prompt', 'marks', 'marking_points', 'sample_answer', 'ideal_answer', 'hint_sections', 'guidelines', 'teaching_note', 'title', 'hints', 'explanation']}
    }
    if mode_norm == "scaffold":
        if 'hint_sections' in item: question['hint_sections'] = item['hint_sections']
        if 'guidelines' in item: question['guidelines'] = item['guidelines']
        if 'teaching_note' in item: question['teaching_note'] = item.get('teaching_note', '')
    return question

def _get_all_pool_items(rng):
    pool = []
    import sys
    mod = sys.modules[__name__]
    for fn_name in ['_concept_pool', '_calculation_pool', '_journal_pool', '_discussion_pool']:
        if hasattr(mod, fn_name):
            try:
                res = getattr(mod, fn_name)(rng)
                if isinstance(res, list): pool.extend(res)
                elif isinstance(res, dict): pool.extend(res.values())
            except Exception:
                pass
    return pool

def generate(subskill=None, difficulty="medium", count=1, mode="scaffold", seed=None, **kwargs):
    rng = _rng(seed)
    all_items = _get_all_pool_items(rng)
    fam_map = {}
    for it in all_items:
        key = it.get('question_family_id') or it.get('subskill') or it.get('title')
        if key and key not in fam_map:
            fam_map[key] = it

    target_sub = str(subskill or "").strip().lower()
    if target_sub in fam_map:
        item = fam_map[target_sub]
        fn = _mcq_question if 'options' in item else _typed_question
        return [fn(rng, item, mode=mode)]

    # Substring / partial match on subskill
    if target_sub and target_sub not in ("concepts", "discussion", "compound", "all", "mixed", "auto", "default", "none"):
        for k, it in fam_map.items():
            if target_sub in str(k).lower():
                fn = _mcq_question if 'options' in it else _typed_question
                return [fn(rng, it, mode=mode)]

    # If count requested, generate count distinct questions cycling through SUBSKILLS
    results = []
    for i in range(count):
        sub_key = SUBSKILLS[i % len(SUBSKILLS)]
        item = fam_map.get(sub_key, all_items[i % len(all_items)])
        fn = _mcq_question if 'options' in item else _typed_question
        results.append(fn(rng, item, mode=mode))
    return results
