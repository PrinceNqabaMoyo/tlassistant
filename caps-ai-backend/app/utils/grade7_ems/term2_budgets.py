import random
from app.utils.ems_namelist import get_ems_scenario, NAMES

def _rng(seed=None):
    return random.Random(seed)

TOPIC_ID = 'grade7_ems'
SUBTOPIC_ID = 'term2_budgets'
CURRICULUM_REFERENCE = 'Term 2 > Budgets'

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
    """Dynamic concept pool."""
    return [
        _with_metadata({
            'title': 'Defining a Budget',
            'prompt': "Which of the following is the best definition of a budget?",
            'options': [
                "A list of all the assets a business owns.", 
                "A document showing how much profit was made over the last year.", 
                "A list showing the money you expect to earn and the expenses you expect to have in the future.", 
                "The amount of capital an owner invests in a new business."
            ],
            'correct_index': 2,
            'explanation': "A budget is a future-facing document. It is a list showing expected earnings (income) and expected expenses over a specific period.",
            'difficulties': ['easy'],
            'marks': 1,
            'hint_sections': [
                {'title': 'What is being tested?', 'text': 'Understanding what a budget is used for.'},
                {'title': 'Reasoning path', 'text': 'When you "budget", are you looking at the past or planning for the future?'},
                {'title': 'Transfer idea', 'text': 'Budgets help you plan to ensure you don\'t spend more money than you earn.'}
            ],
            'guidelines': ['Identify the definition that involves future estimates of income and expenses.']
        }, subskill='concepts', learning_objective_id='lo_def_budget', question_family_id='def_budget', concept_id='budget', concept_group='budgets', misconception_tags=['confuses_budget_with_past_records'], diagnostic_tags=['definition']),
    ]

def _calculation_pool(rng):
    """Unlimited calculations for Budget Variances."""
    business = get_ems_scenario()
    
    actual_exp = rng.randint(40000, 60000)
    budgeted_exp = rng.randint(35000, 55000)
    
    # Calculate variance (Actual vs Budgeted)
    # The curriculum states if Actual > Budgeted for expenses, variance is negative impact
    variance_amount = actual_exp - budgeted_exp
    
    return [
        _with_metadata({
            'title': 'Calculate Variance',
            'prompt': f"{business['entrepreneur']}'s operating budget shows that the actual expenses for {business['item_sold']} were R{actual_exp:,} but the budgeted expenses were R{budgeted_exp:,}.\n\nCalculate the difference (variance) between the actual and budgeted amounts.",
            'correct_value': variance_amount,
            'explanation': f"The variance is calculated by finding the difference between the actual expenses (R{actual_exp:,}) and the budgeted expenses (R{budgeted_exp:,}). The difference is R{variance_amount:,}.",
            'difficulties': ['medium'],
            'marks': 2,
            'hint_sections': [
                {'title': 'What is being tested?', 'text': 'Calculating variance between budgeted and actual figures.'},
                {'title': 'Reasoning path', 'text': 'Variance simply means difference. Subtract the budgeted amount from the actual amount.'},
                {'title': 'Transfer idea', 'text': 'If actual expenses are higher than budgeted, the business spent more than it planned to.'}
            ],
            'guidelines': ['Ensure the variance is calculated as the absolute difference.'],
            'teaching_note': 'Grade 7 math accepts the absolute difference. The interpretation of whether it is good or bad is handled in discussion questions.'
        }, subskill='calculations', learning_objective_id='lo_calculate_variance', question_family_id='variance_math', concept_id='variance', concept_group='budgets', misconception_tags=['adds_instead_of_subtracts'], diagnostic_tags=['calculation']),
    ]

def _journal_pool(rng):
    """Renders a Business Budget table."""
    business = get_ems_scenario()
    
    # Generate randomized budget values
    budget_sales = rng.randint(70, 90) * 1000
    actual_sales = budget_sales + rng.randint(-5000, 15000)
    
    budget_wages = rng.randint(5, 8) * 1000
    actual_wages = budget_wages
    
    budget_rent = rng.randint(2, 4) * 1000
    actual_rent = budget_rent
    
    budget_supplies = rng.randint(30, 50) * 1000
    actual_supplies = budget_supplies + rng.randint(-2000, 4000)
    
    budget_total_exp = budget_wages + budget_rent + budget_supplies
    actual_total_exp = actual_wages + actual_rent + actual_supplies
    
    budget_net = budget_sales - budget_total_exp
    actual_net = actual_sales - actual_total_exp
    
    var_sales = actual_sales - budget_sales
    var_exp = actual_total_exp - budget_total_exp
    var_net = actual_net - budget_net
    
    table_md = f"""
| | Actual (R) | Budget (R) |
| :--- | :--- | :--- |
| **INCOME** | | |
| Sales | {actual_sales:,} | {budget_sales:,} |
| **EXPENDITURE** | | |
| Wages | {actual_wages:,} | {budget_wages:,} |
| Rent | {actual_rent:,} | {budget_rent:,} |
| Supplies | {actual_supplies:,} | {budget_supplies:,} |
"""
    
    return [
        _with_metadata({
            'title': 'Completing a Business Budget',
            'prompt': f"{business['entrepreneur']} owns a business in {business['area']}. Look at their partial operating budget below:\n\n{table_md}\nCalculate the following THREE missing figures:\n1. Total Actual Expenditure\n2. Total Budgeted Expenditure\n3. Actual Net Profit (Income - Expenditure). (6 marks)",
            'marks': 6,
            'marking_points': [
                f"Total Actual Expenditure = R{actual_total_exp:,}",
                f"Total Budgeted Expenditure = R{budget_total_exp:,}",
                f"Actual Net Profit = R{actual_net:,}"
            ],
            'sample_answer': f"1. Total Actual Expenditure = R{actual_wages:,} + R{actual_rent:,} + R{actual_supplies:,} = R{actual_total_exp:,}\n2. Total Budgeted Expenditure = R{budget_wages:,} + R{budget_rent:,} + R{budget_supplies:,} = R{budget_total_exp:,}\n3. Actual Net Profit = R{actual_sales:,} (Sales) - R{actual_total_exp:,} (Expenditure) = R{actual_net:,}",
            'difficulties': ['hard'],
            'hint_sections': [
                {'title': 'What is being tested?', 'text': 'Interpreting a business budget table and calculating totals and net profit.'},
                {'title': 'Reasoning path', 'text': 'Sum the expenses in the Actual column. Do the same for the Budget column. Finally, take the Actual Sales and subtract the Actual Expenditure to find the profit.'},
                {'title': 'Transfer idea', 'text': 'A business budget calculates net profit exactly like a personal budget: Total Income minus Total Expenses.'}
            ],
            'guidelines': ['Award 2 marks for each correctly calculated figure.'],
            'teaching_note': 'This tests their ability to read columns horizontally and sum vertically, which prepares them for Grade 8 Journals.'
        }, subskill='journals', learning_objective_id='lo_business_budget', question_family_id='render_business_budget', concept_id='business_budget', concept_group='budgets', misconception_tags=['subtracts_income_from_expenses'], diagnostic_tags=['table_rendering', 'accounting']),
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
        chosen = rng.sample(selected, min(count, len(selected)))
        return [_mcq_question(rng, item, mode=mode) for item in chosen]
