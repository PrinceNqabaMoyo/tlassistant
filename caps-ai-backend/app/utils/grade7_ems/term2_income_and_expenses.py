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
        'id': f"g7_ems_mcq_{rng.randint(1000, 999999)}",
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

def _typed_question(rng, item, mode="scaffold"):
    mode_norm = str(mode or "").strip().lower()
    question = {
        'id': f"g7_ems_typed_{rng.randint(1000, 999999)}",
        'title': item.get('title', 'Written response'),
        'question_type': 'typed',
        'prompt': item['prompt'],
        'marks': item['marks'],
        'marking_points': item['marking_points'],
        'sample_answer': item['sample_answer'],
        'ideal_answer': item.get('ideal_answer', item['sample_answer']),
        **{k: v for k, v in item.items() if k not in ['prompt', 'marks', 'marking_points', 'sample_answer', 'ideal_answer', 'hint_sections', 'guidelines', 'teaching_note', 'title']}
    }
    
    if mode_norm == "scaffold":
        if 'hint_sections' in item: question['hint_sections'] = item['hint_sections']
        if 'guidelines' in item: question['guidelines'] = item['guidelines']
        if 'teaching_note' in item: question['teaching_note'] = item.get('teaching_note', '')
        
    return question

def _calc_question(rng, item, mode="scaffold"):
    mode_norm = str(mode or "").strip().lower()
    question = {
        'id': f"g7_ems_calc_{rng.randint(1000, 999999)}",
        'title': item.get('title', 'Calculation'),
        'question_type': 'calc',
        'prompt': item['prompt'],
        'marks': item['marks'],
        'correct_value': str(item['correct_value']),
        'explanation': item['explanation'],
        'sample_answer': str(item['correct_value']),
        'ideal_answer': str(item['correct_value']),
        'marking_points': [str(item['correct_value'])],
        **{k: v for k, v in item.items() if k not in ['prompt', 'marks', 'correct_value', 'explanation', 'title', 'hint_sections', 'guidelines', 'teaching_note']}
    }
    
    if mode_norm == "scaffold":
        if 'hint_sections' in item: question['hint_sections'] = item['hint_sections']
        if 'guidelines' in item: question['guidelines'] = item['guidelines']
        if 'teaching_note' in item: question['teaching_note'] = item.get('teaching_note', item['explanation'])
        
    return question

def _concept_pool(rng):
    """Dynamic concept pool with 6 distinct CAPS archetypes."""
    return [
        _with_metadata({
            'title': 'Defining Personal Income',
            'prompt': "Which of the following best defines personal income?",
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
            'prompt': "In personal finance, which of the following is classified as a VARIABLE personal expense?",
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
            'prompt': "Which of the following items owned by an individual is classified as an ASSET?",
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
            'prompt': "Which of the following is the best definition of a financial LIABILITY?",
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
            'prompt': "What is the correct mathematical formula to calculate an individual's personal Net Worth?",
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
            'prompt': "If an employee earns R20 000 per month, spends R16 000 on essential expenses, and deposits R4 000 into a unit trust investment, what does the R4 000 represent?",
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
    """Renders a Statement of Net Worth table."""
    person = rng.choice(NAMES)
    
    # Generate items
    bed = rng.randint(3000, 8000)
    laptop = rng.randint(4000, 10000)
    phone = rng.randint(2000, 6000)
    total = bed + laptop + phone
    
    table_md = f"""
| Item | Value |
| :--- | :--- |
| Bed | R{bed} |
| Laptop | R{laptop} |
| Smartphone | R{phone} |
"""
    
    return [
        _with_metadata({
            'title': 'Statement of Net Worth Table',
            'prompt': f"{person} has asked you to help calculate their net worth. They have no debts, but they have made a list of the things in their room:\n\n{table_md}\nDraw up {person}'s Statement of Net Worth. (4 marks)",
            'marks': 4,
            'marking_points': [
                "Heading: Statement of Net Worth",
                "ASSETS section listing the items and their values",
                "LIABILITIES section showing 0",
                f"Net Worth calculated correctly as R{total}"
            ],
            'sample_answer': f"**Statement of Net Worth of {person}**\n\n**ASSETS:** R{total}\nBed: R{bed}\nLaptop: R{laptop}\nSmartphone: R{phone}\n\n**LIABILITIES:** R0\n\n**NET WORTH:** R{total}",
            'difficulties': ['hard'],
            'hint_sections': [
                {'title': 'What is being tested?', 'text': 'Structuring a formal Statement of Net Worth.'},
                {'title': 'Reasoning path', 'text': 'Group all the items under ASSETS. Since there are no debts, what goes under LIABILITIES? Calculate the final figure.'},
                {'title': 'Transfer idea', 'text': 'A formal statement must be logically separated into Assets, Liabilities, and the final Net Worth calculation.'}
            ],
            'guidelines': ['Ensure the table/list structure clearly delineates Assets and Liabilities.'],
            'teaching_note': 'Students must show the zero liabilities to demonstrate understanding of the complete formula.'
        }, subskill='journals', learning_objective_id='lo_statement_net_worth', question_family_id='render_statement_net_worth', concept_id='statement_of_net_worth', concept_group='income_and_expenses', misconception_tags=['fails_to_structure_formally'], diagnostic_tags=['table_rendering', 'accounting']),
    ]

def generate(subskill="concepts", difficulty="medium", count=1, mode="scaffold", seed=None, **kwargs):
    rng = _rng(seed)
    
    if subskill == "calculation":
        pool = _calculation_pool(rng)
        selected = [q for q in pool if difficulty in q['difficulties']]
        if not selected: selected = pool
        chosen = rng.sample(selected, min(count, len(selected)))
        return [_calc_question(rng, item, mode=mode) for item in chosen]
    elif subskill == "journal":
        pool = _journal_pool(rng)
        selected = [q for q in pool if difficulty in q['difficulties']]
        if not selected: selected = pool
        chosen = rng.sample(selected, min(count, len(selected)))
        return [_typed_question(rng, item, mode=mode) for item in chosen]
    else:
        pool = _concept_pool(rng)
        selected = [q for q in pool if difficulty in q['difficulties']]
        if not selected: selected = pool
        if seed is not None and count == 1 and len(selected) > 1:
            chosen = [selected[int(seed) % len(selected)]]
        else:
            chosen = rng.sample(selected, min(count, len(selected)))
        return [_mcq_question(rng, item, mode=mode) for item in chosen]
