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
            'title': 'Defining a Budget',
            'prompt': f"{scenario['entrepreneur']} in {scenario['area']} prepares financial plans. Which of the following is the best definition of a budget?",
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
        _with_metadata({
            'title': 'Budget Surplus vs Deficit',
            'prompt': f"If {scenario['entrepreneur']}'s household in {scenario['area']} has an expected monthly income that is GREATER than its expected monthly expenditure, the budget reflects a …",
            'options': [
                "Budget Surplus",
                "Budget Deficit",
                "Capital Depreciation",
                "Liability Shortage"
            ],
            'correct_index': 0,
            'explanation': "When Total Income > Total Expenditure, the difference is a Budget Surplus (extra money available for savings or investments). If Expenditure > Income, it is a Deficit.",
            'difficulties': ['easy', 'medium'],
            'marks': 1,
            'hint_sections': [
                {'title': 'What is being tested?', 'text': 'Differentiating between a budget surplus and deficit.'},
                {'title': 'Reasoning path', 'text': 'Income is coming in; expenditure is going out. If you earn more than you spend, is it extra (surplus) or a shortage (deficit)?'},
                {'title': 'Transfer idea', 'text': 'A budget surplus should be allocated to savings or debt reduction.'}
            ],
            'guidelines': ['Identify that excess income over expenditure is a surplus.']
        }, subskill='concepts', learning_objective_id='lo_surplus_deficit', question_family_id='budget_surplus_deficit', concept_id='surplus_deficit', concept_group='budgets', misconception_tags=['confuses_surplus_with_deficit'], diagnostic_tags=['terminology']),
        _with_metadata({
            'title': 'Fixed vs Variable Expenses',
            'prompt': f"When {scenario['entrepreneur']} prepares a family budget in {scenario['area']}, which of the following items is classified as a FIXED expense?",
            'options': [
                "Monthly rent or house bond repayment",
                "Weekend entertainment and movies",
                "Buying birthday gifts for friends",
                "Monthly water and electricity bill that changes each season"
            ],
            'correct_index': 0,
            'explanation': "A fixed expense stays constant every month (e.g. rent, school fees, car bond). Variable expenses fluctuate based on consumption and lifestyle choices.",
            'difficulties': ['medium'],
            'marks': 1,
            'hint_sections': [
                {'title': 'What is being tested?', 'text': 'Classifying expenses as fixed or variable.'},
                {'title': 'Reasoning path', 'text': 'Which of these expenses stays the exact same amount every month regardless of your daily habits?'},
                {'title': 'Transfer idea', 'text': 'Fixed expenses must always be prioritized in a budget before variable or luxury spending.'}
            ],
            'guidelines': ['Identify the expense with a constant monthly obligation.']
        }, subskill='concepts', learning_objective_id='lo_fixed_variable_expenses', question_family_id='fixed_variable_expense', concept_id='expense_types', concept_group='budgets', misconception_tags=['confuses_fixed_with_variable'], diagnostic_tags=['classification']),
        _with_metadata({
            'title': 'Business vs Personal Budget',
            'prompt': f"For {scenario['entrepreneur']}'s business in {scenario['area']}, how does an operating budget for a small trading business primarily differ from a personal household budget?",
            'options': [
                "A business budget estimates sales revenue, cost of sales, and operating expenses to project net profit.",
                "A business budget only lists expenses and does not record any income.",
                "A personal budget must be audited by registered chartered accountants.",
                "A business budget never accounts for unexpected repairs or maintenance."
            ],
            'correct_index': 0,
            'explanation': "A business budget projects sales revenue, cost of sales (trading inventory), and operating expenses (rent, wages, utilities) to estimate whether the enterprise will yield a net profit.",
            'difficulties': ['medium', 'hard'],
            'marks': 1,
            'hint_sections': [
                {'title': 'What is being tested?', 'text': 'Understanding the commercial purpose of a business budget.'},
                {'title': 'Reasoning path', 'text': 'Why does an entrepreneur create a budget? To plan for sales revenue, overheads, and profit.'},
                {'title': 'Transfer idea', 'text': 'Business budgets connect sales volume to profitability.'}
            ],
            'guidelines': ['Connect trading revenues and operating expenses to net profit.']
        }, subskill='concepts', learning_objective_id='lo_business_budget_purpose', question_family_id='business_budget_comparison', concept_id='business_budget', concept_group='budgets', misconception_tags=['confuses_business_with_personal_finance'], diagnostic_tags=['commercial_application']),
        _with_metadata({
            'title': 'Budget Contingency & Savings',
            'prompt': f"When {scenario['entrepreneur']} budgets for family finances in {scenario['area']}, why should a prudent budget always include an allocation for savings or contingency funds?",
            'options': [
                "To absorb unexpected emergency expenses without incurring high-interest debt",
                "To ensure that all earned money is spent completely before month-end",
                "To reduce the bank balance to zero so inflation does not affect cash",
                "To hide income from financial records"
            ],
            'correct_index': 0,
            'explanation': "A contingency allocation provides an emergency safety cushion so that sudden unexpected expenses (car repairs, medical bills) do not force the household or business into high-interest debt.",
            'difficulties': ['easy', 'medium'],
            'marks': 1,
            'hint_sections': [
                {'title': 'What is being tested?', 'text': 'The role of emergency savings in financial planning.'},
                {'title': 'Reasoning path', 'text': 'What happens if a sudden medical bill or burst geyser occurs? Savings prevent taking emergency loans.'},
                {'title': 'Transfer idea', 'text': 'Emergency savings should ideally cover 3 to 6 months of essential fixed expenses.'}
            ],
            'guidelines': ['Focus on financial resilience against unexpected emergencies.']
        }, subskill='concepts', learning_objective_id='lo_contingency_savings', question_family_id='budget_contingency', concept_id='savings_contingency', concept_group='budgets', misconception_tags=['underestimates_financial_risk'], diagnostic_tags=['financial_literacy']),
        _with_metadata({
            'title': 'Budget Variance Interpretation',
            'prompt': f"If {scenario['entrepreneur']}'s business in {scenario['area']} budgeted R8 000 for monthly electricity but the actual municipal bill came to R11 500, how is this variance described?",
            'options': [
                "Unfavourable expense variance of R3 500",
                "Favourable savings surplus of R3 500",
                "Net capital gain of R3 500",
                "Balanced budget variance of R11 500"
            ],
            'correct_index': 0,
            'explanation': "When actual expenses exceed budgeted expenses, the variance is unfavourable (negative impact on profit). Overspending by R3 500 reduces net profit.",
            'difficulties': ['medium', 'hard'],
            'marks': 1,
            'hint_sections': [
                {'title': 'What is being tested?', 'text': 'Interpreting budget variance.'},
                {'title': 'Reasoning path', 'text': 'Did the business spend more or less than planned? If expenses were higher, is that good (favourable) or bad (unfavourable)?'},
                {'title': 'Transfer idea', 'text': 'Actual Expenses > Budgeted Expenses = Unfavourable Variance.'}
            ],
            'guidelines': ['Identify that excess spending is an unfavourable variance.']
        }, subskill='concepts', learning_objective_id='lo_variance_analysis', question_family_id='budget_variance_eval', concept_id='variance_analysis', concept_group='budgets', misconception_tags=['inverts_variance_polarity'], diagnostic_tags=['analytical_reasoning']),
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
    """Renders an interactive Business Operating Budget table."""
    business = get_ems_scenario(rng)
    
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
    
    actual_net = actual_sales - actual_total_exp
    
    headers = ["Category", "Line Item", "Actual (R)", "Budget (R)"]
    rows = [
        [{"cell_id": "r0_c0", "value": "INCOME", "editable": False}, {"cell_id": "r0_c1", "value": "Sales Revenue", "editable": False}, {"cell_id": "r0_c2", "value": f"{actual_sales}", "editable": False}, {"cell_id": "r0_c3", "value": f"{budget_sales}", "editable": False}],
        [{"cell_id": "r1_c0", "value": "EXPENDITURE", "editable": False}, {"cell_id": "r1_c1", "value": "Wages & Salaries", "editable": False}, {"cell_id": "r1_c2", "value": f"{actual_wages}", "editable": False}, {"cell_id": "r1_c3", "value": f"{budget_wages}", "editable": False}],
        [{"cell_id": "r2_c0", "value": "EXPENDITURE", "editable": False}, {"cell_id": "r2_c1", "value": "Operating Rent", "editable": False}, {"cell_id": "r2_c2", "value": f"{actual_rent}", "editable": False}, {"cell_id": "r2_c3", "value": f"{budget_rent}", "editable": False}],
        [{"cell_id": "r3_c0", "value": "EXPENDITURE", "editable": False}, {"cell_id": "r3_c1", "value": "Trading Supplies", "editable": False}, {"cell_id": "r3_c2", "value": f"{actual_supplies}", "editable": False}, {"cell_id": "r3_c3", "value": f"{budget_supplies}", "editable": False}],
        [{"cell_id": "r4_c0", "value": "TOTAL EXPENDITURE", "editable": False}, {"cell_id": "r4_c1", "value": "Sum of all operating costs", "editable": False}, {"cell_id": "r4_c2", "value": "", "expected": str(actual_total_exp), "editable": True}, {"cell_id": "r4_c3", "value": "", "expected": str(budget_total_exp), "editable": True}],
        [{"cell_id": "r5_c0", "value": "NET PROFIT", "editable": False}, {"cell_id": "r5_c1", "value": "Sales minus Total Expenditure", "editable": False}, {"cell_id": "r5_c2", "value": "", "expected": str(actual_net), "editable": True}, {"cell_id": "r5_c3", "value": "-", "editable": False}],
    ]
    correct_map = {
        "r4_c2": str(actual_total_exp),
        "r4_c3": str(budget_total_exp),
        "r5_c2": str(actual_net),
    }
    
    return [
        _with_metadata({
            'title': 'Operating Budget Statement',
            'prompt': f"{business['entrepreneur']} operates a business in {business['area']}. Look at the partial operating budget table below.\n\nCalculate the three missing figures in the table:\n1. Total Actual Expenditure\n2. Total Budgeted Expenditure\n3. Actual Net Profit (Actual Sales − Total Actual Expenditure).",
            'marks': 6,
            'modality': 'ledger',
            'question_type': 'journal',
            'solution_type': 'tabular_cells',
            'headers': headers,
            'rows': rows,
            'correct_map': correct_map,
            'expected_answer': f"Total Actual Expenditure = R{actual_total_exp:,}; Total Budgeted Expenditure = R{budget_total_exp:,}; Actual Net Profit = R{actual_net:,}",
            'sample_answer': f"Total Actual Expenditure = R{actual_total_exp:,}; Total Budgeted Expenditure = R{budget_total_exp:,}; Actual Net Profit = R{actual_net:,}",
            'worked_solution': f"1. Total Actual Expenditure = R{actual_wages:,} + R{actual_rent:,} + R{actual_supplies:,} = R{actual_total_exp:,}\n2. Total Budgeted Expenditure = R{budget_wages:,} + R{budget_rent:,} + R{budget_supplies:,} = R{budget_total_exp:,}\n3. Actual Net Profit = R{actual_sales:,} - R{actual_total_exp:,} = R{actual_net:,}",
            'explanation': f"Actual Exp = R{actual_total_exp:,}; Budget Exp = R{budget_total_exp:,}; Actual Net Profit = R{actual_net:,}",
            'canonical_solution': f"Total Actual Expenditure = R{actual_total_exp:,}; Total Budgeted Expenditure = R{budget_total_exp:,}; Actual Net Profit = R{actual_net:,}",
            'difficulties': ['hard'],
            'hints': {
                'tier_1': 'Add the expenditure lines for the Actual column and the Budget column separately.',
                'tier_2': f'Actual Expenditure = R{actual_wages} + R{actual_rent} + R{actual_supplies}. Then subtract it from Sales (R{actual_sales}) to find Net Profit.',
                'tier_3': f'Actual Exp: {actual_total_exp}; Budget Exp: {budget_total_exp}; Net Profit: {actual_net}.'
            },
        }, subskill='render_business_budget', learning_objective_id='lo_business_budget', question_family_id='render_business_budget', concept_id='business_budget', concept_group='budgets', misconception_tags=['subtracts_income_from_expenses'], diagnostic_tags=['table_rendering', 'accounting']),
    ]



SUBSKILLS = ['def_budget', 'budget_surplus_deficit', 'fixed_variable_expense', 'business_budget_comparison', 'budget_contingency', 'budget_variance_eval', 'variance_math', 'render_business_budget']



SUBSKILLS = ['def_budget', 'budget_surplus_deficit', 'fixed_variable_expense', 'business_budget_comparison', 'budget_contingency', 'budget_variance_eval', 'variance_math', 'render_business_budget']

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
