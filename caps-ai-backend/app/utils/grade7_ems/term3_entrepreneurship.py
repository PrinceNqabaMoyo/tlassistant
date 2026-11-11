import random
from app.utils.ems_namelist import get_ems_scenario, NAMES

def _rng(seed=None):
    return random.Random(seed)

TOPIC_ID = 'grade7_ems'
SUBTOPIC_ID = 'term3_entrepreneurship'
CURRICULUM_REFERENCE = 'Term 3 > Entrepreneurship and Socio-Economic Issues'

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
    """MCQ concepts for term 3."""
    scenario = get_ems_scenario(rng)
    return [
        _with_metadata({
            'title': 'Defining the Poverty Line',
            'prompt': f"In assessing household conditions across {scenario['area']}, what does the 'poverty line' refer to?",
            'options': [
                "The physical boundary between wealthy suburbs and poor townships.", 
                "The minimum income needed to provide for basic needs, often considered as US$1 a day.", 
                "The amount of tax a business must pay to the government.", 
                "The total number of unemployed people in South Africa."
            ],
            'correct_index': 1,
            'explanation': "The poverty line is considered to be the minimum amount of money that you can earn to provide for your basic needs (historically around US$1 a day).",
            'difficulties': ['easy', 'medium'],
            'marks': 1,
            'hint_sections': [
                {'title': 'What is being tested?', 'text': 'Understanding the definition of the poverty line.'},
                {'title': 'Reasoning path', 'text': 'Think about what "line" separates people who have enough to survive from those who do not.'},
                {'title': 'Transfer idea', 'text': 'The poverty line is a global economic measure used to identify extreme poverty.'}
            ],
            'guidelines': ['Identify the correct definition of the poverty line.']
        }, subskill='concepts', learning_objective_id='lo_poverty_line', question_family_id='def_poverty_line', concept_id='poverty_line', concept_group='socio_economics', misconception_tags=['confuses_poverty_line_with_geography'], diagnostic_tags=['definition']),
        
        _with_metadata({
            'title': 'Defining an Entrepreneur',
            'prompt': f"{scenario['entrepreneur']} operates a venture in {scenario['area']}. Which statement BEST describes an entrepreneur?",
            'options': [
                "A person who identifies a business opportunity, takes calculated financial risks, and organizes resources to make a profit",
                "A person who is employed by the government to manage municipal water pipes",
                "A consumer who only purchases imported luxury goods on credit",
                "A bank teller who processes daily cash deposits for retail clients"
            ],
            'correct_index': 0,
            'explanation': "An entrepreneur is an innovator who identifies market needs, takes financial risks, and combines the factors of production (land, labour, capital) to create goods or services.",
            'difficulties': ['easy', 'medium', 'hard'],
            'marks': 1,
            'hint_sections': [
                {'title': 'What is being tested?', 'text': 'Understanding the definition and role of an entrepreneur.'},
                {'title': 'Reasoning path', 'text': 'What makes someone an entrepreneur rather than just an employee? They spot an opportunity and take a risk.'},
                {'title': 'Transfer idea', 'text': 'Entrepreneurs drive economic growth and create employment in South Africa.'}
            ],
            'guidelines': ['Identify the definition highlighting opportunity, risk, and resource organisation.']
        }, subskill='concepts', learning_objective_id='lo_def_entrepreneur', question_family_id='def_entrepreneur', concept_id='entrepreneur_concept', concept_group='entrepreneurship', misconception_tags=['confuses_entrepreneur_with_employee'], diagnostic_tags=['definition']),
        _with_metadata({
            'title': 'Characteristics of an Entrepreneur',
            'prompt': f"When evaluating business leaders in {scenario['area']}, which combination represents key personal characteristics of a successful entrepreneur?",
            'options': [
                "Perseverance, calculated risk-taking, creativity, and self-confidence",
                "Fear of failure, unwillingness to adapt, and total dependence on luck",
                "Avoiding all competition and refusing to advertise",
                "Spending all business income immediately on personal luxury"
            ],
            'correct_index': 0,
            'explanation': "Successful entrepreneurs demonstrate resilience, creativity, discipline, decision-making ability, and the courage to take calculated risks.",
            'difficulties': ['easy', 'medium', 'hard'],
            'marks': 1,
            'hint_sections': [
                {'title': 'What is being tested?', 'text': 'Personal traits of entrepreneurs.'},
                {'title': 'Reasoning path', 'text': 'Which traits help an entrepreneur overcome challenges when starting a new venture?'},
                {'title': 'Transfer idea', 'text': 'Resilience and problem-solving are essential when dealing with business setbacks.'}
            ],
            'guidelines': ['Select the positive entrepreneurial character traits.']
        }, subskill='concepts', learning_objective_id='lo_entrepreneur_traits', question_family_id='entrepreneurial_traits', concept_id='traits', concept_group='entrepreneurship', misconception_tags=['assumes_luck_drives_business'], diagnostic_tags=['traits']),
        _with_metadata({
            'title': 'School Entrepreneur\'s Day Planning',
            'prompt': f"When Grade 7 learners in {scenario['area']} organize a school Entrepreneur's Day, what is the FIRST crucial step in the planning process?",
            'options': [
                "Conducting market research to identify what products fellow learners need and want",
                "Printing expensive colour banners before deciding what product to sell",
                "Borrowing money from a bank at a high commercial interest rate",
                "Closing the school gate to external visitors"
            ],
            'correct_index': 0,
            'explanation': "Market research is the vital first step: finding out what customers (fellow learners, teachers, parents) want to buy, and what price they are willing to pay.",
            'difficulties': ['easy', 'medium', 'hard'],
            'marks': 1,
            'hint_sections': [
                {'title': 'What is being tested?', 'text': 'Planning for an Entrepreneur\'s Day.'},
                {'title': 'Reasoning path', 'text': 'Can you sell products successfully if you don\'t know what your target market wants?'},
                {'title': 'Transfer idea', 'text': 'Identify customer needs before investing money into stock production.'}
            ],
            'guidelines': ['Focus on market research as the prerequisite step.']
        }, subskill='concepts', learning_objective_id='lo_entrepreneurs_day', question_family_id='planning_entrepreneurs_day', concept_id='entrepreneurs_day', concept_group='starting_a_business', misconception_tags=['skips_market_research'], diagnostic_tags=['planning']),
        _with_metadata({
            'title': 'Needs vs Wants in Business Opportunities',
            'prompt': f"In {scenario['area']}, how can an entrepreneur turn a community's UNMET NEED into a viable business opportunity?",
            'options': [
                "By providing a reliable, affordable service (such as mobile phone repairs or after-school transport) that solves the community's problem",
                "By demanding that the municipal council ban all local competitors",
                "By selling luxury jewellery in a drought-stricken farming community",
                "By ignoring customer feedback and keeping store hours secret"
            ],
            'correct_index': 0,
            'explanation': "A viable business opportunity exists where an entrepreneur solves a genuine everyday problem or provides a product that satisfies an unmet need at an affordable price.",
            'difficulties': ['medium', 'hard'],
            'marks': 1,
            'hint_sections': [
                {'title': 'What is being tested?', 'text': 'Transforming community needs into entrepreneurial ventures.'},
                {'title': 'Reasoning path', 'text': 'Great businesses solve real problems. What problem can the entrepreneur solve?'},
                {'title': 'Transfer idea', 'text': 'Problem + Solution + Willingness to Pay = Viable Business Opportunity.'}
            ],
            'guidelines': ['Look for problem-solving services meeting community needs.']
        }, subskill='concepts', learning_objective_id='lo_business_opportunities', question_family_id='needs_wants_opportunity', concept_id='opportunity_identification', concept_group='entrepreneurship', misconception_tags=['confuses_need_with_unviable_want'], diagnostic_tags=['commercial_opportunity']),
        _with_metadata({
            'title': 'SWOT Analysis Elements',
            'prompt': f"When {scenario['entrepreneur']} conducts a SWOT analysis for a new venture in {scenario['area']}, which elements represent INTERNAL factors that the entrepreneur can directly control?",
            'options': [
                "Strengths and Weaknesses",
                "Opportunities and Threats",
                "Government regulations and inflation",
                "Competitor price cuts and weather disasters"
            ],
            'correct_index': 0,
            'explanation': "Strengths and Weaknesses are internal to the business (skills, product quality, location). Opportunities and Threats are external factors.",
            'difficulties': ['easy', 'medium', 'hard'],
            'marks': 1,
            'hint_sections': [
                {'title': 'What is being tested?', 'text': 'Internal vs external SWOT factors.'},
                {'title': 'Reasoning path', 'text': 'Can you control your own product recipe or staff training? Yes (Internal: S & W). Can you control the weather or interest rates? No (External: O & T).'},
                {'title': 'Transfer idea', 'text': 'Internal = Strengths & Weaknesses; External = Opportunities & Threats.'}
            ],
            'guidelines': ['Identify Strengths and Weaknesses as the internal controllable factors.']
        }, subskill='concepts', learning_objective_id='lo_swot_internal_external', question_family_id='swot_factors', concept_id='swot', concept_group='entrepreneurship', misconception_tags=['confuses_internal_with_external'], diagnostic_tags=['swot_analysis']),
        _with_metadata({
            'title': 'Fixed vs Variable Costs in Production',
            'prompt': f"If {scenario['entrepreneur']} bakes {scenario['item_sold']} for an Entrepreneur's Day stall in {scenario['area']}, which cost is classified as a VARIABLE cost?",
            'options': [
                "Flour, sugar, eggs, and paper baking cups",
                "The fixed table rental fee paid to the school for the stall",
                "The cost of the reusable wooden stall sign board",
                "The annual school hall insurance fee"
            ],
            'correct_index': 0,
            'explanation': "Variable costs change directly with the number of units produced (more muffins baked = more flour, eggs, and baking cups needed). Stall rental is fixed.",
            'difficulties': ['medium', 'hard'],
            'marks': 1,
            'hint_sections': [
                {'title': 'What is being tested?', 'text': 'Identifying variable costs in product manufacturing.'},
                {'title': 'Reasoning path', 'text': 'If you bake 10 muffins vs 100 muffins, which ingredient costs will increase?'},
                {'title': 'Transfer idea', 'text': 'Raw materials and packaging are direct variable costs.'}
            ],
            'guidelines': ['Identify ingredients and packaging that scale with production.']
        }, subskill='concepts', learning_objective_id='lo_production_costs', question_family_id='variable_costs_production', concept_id='production_costs', concept_group='entrepreneurship', misconception_tags=['confuses_fixed_stall_fee_with_variable'], diagnostic_tags=['costing']),
        _with_metadata({
            'title': 'Calculating Business Profit',
            'prompt': f"{scenario['entrepreneur']} generates R1 500 in sales revenue from selling {scenario['item_sold']} in {scenario['area']}. The total production and stall expenses amounted to R950. What is the net profit earned?",
            'options': [
                "R550 Net Profit (R1 500 - R950)",
                "R2 450 Net Profit (R1 500 + R950)",
                "R950 Operating Surplus",
                "R0 Breakeven Result"
            ],
            'correct_index': 0,
            'explanation': "Profit = Total Income - Total Expenses. R1 500 (Sales) - R950 (Expenses) = R550 Net Profit.",
            'difficulties': ['easy', 'medium', 'hard'],
            'marks': 1,
            'hint_sections': [
                {'title': 'What is being tested?', 'text': 'The basic profit formula.'},
                {'title': 'Reasoning path', 'text': 'Take the money collected from customers (Income) and subtract all the costs incurred (Expenses).'},
                {'title': 'Transfer idea', 'text': 'Sales Revenue - Total Costs = Net Profit.'}
            ],
            'guidelines': ['Subtract expenses from revenue to find net profit.']
        }, subskill='concepts', learning_objective_id='lo_profit_formula', question_family_id='calculate_profit_simple', concept_id='profit_calc', concept_group='entrepreneurship', misconception_tags=['adds_expenses_to_revenue'], diagnostic_tags=['calculation', 'profit']),
        _with_metadata({
            'title': 'Advertising and Promotion',
            'prompt': f"For {scenario['entrepreneur']}'s school Entrepreneur's Day stall in {scenario['area']}, which promotional strategy is MOST cost-effective?",
            'options': [
                "Creating colourful posters on school noticeboards, class announcements, and social media flyers",
                "Purchasing a prime-time national television commercial",
                "Hiring a helicopter to drop flyers across the town",
                "Taking out a full-page colour advert in a national Sunday newspaper"
            ],
            'correct_index': 0,
            'explanation': "Promotional media must be appropriate for the target market and budget. School noticeboards, word-of-mouth, and class posters reach fellow learners at near-zero cost.",
            'difficulties': ['easy', 'medium'],
            'marks': 1,
            'hint_sections': [
                {'title': 'What is being tested?', 'text': 'Choosing cost-effective promotional channels.'},
                {'title': 'Reasoning path', 'text': 'Where are your customers? They are inside the school. What is the cheapest way to reach them?'},
                {'title': 'Transfer idea', 'text': 'Target market alignment prevents wasting marketing capital.'}
            ],
            'guidelines': ['Select targeted, low-cost school-focused media.']
        }, subskill='concepts', learning_objective_id='lo_promotional_strategy', question_family_id='promotional_channels', concept_id='promotion', concept_group='starting_a_business', misconception_tags=['chooses_impractical_mass_media'], diagnostic_tags=['marketing']),
    ]

def _discussion_pool(rng):
    """Typed discussion questions."""
    scenario = get_ems_scenario(rng)
    business = get_ems_scenario()
    
    return [
        _with_metadata({
            'title': 'Socio-economic Imbalances',
            'prompt': f"In communities like {scenario['area']}, explain in your own words what socio-economic imbalances are, and give examples. (2 marks)",
            'marks': 2,
            'marking_points': [
                "Imbalances in people's access to resources or opportunities.",
                "Examples include access to housing, health, education, or a decent standard of living."
            ],
            'sample_answer': "Socio-economic imbalances refer to the unequal distribution of and access to resources in a society. For example, some people have easy access to quality education, healthcare, and housing, while others do not.",
            'difficulties': ['medium', 'hard'],
            'hint_sections': [
                {'title': 'What is being tested?', 'text': 'Explaining the concept of socio-economic inequality.'},
                {'title': 'Reasoning path', 'text': 'Think about the differences between wealthy suburbs and poor communities. What do some people have that others lack?'},
                {'title': 'Transfer idea', 'text': 'Socio-economic imbalances are about the gap between the rich and the poor regarding basic human rights.'}
            ],
            'guidelines': ['Ensure the definition involves unequal access to resources, and one valid example is provided.'],
            'teaching_note': 'Accept any valid examples like water, electricity, jobs, schooling, etc.'
        }, subskill='discussion', learning_objective_id='lo_socio_economic', question_family_id='explain_imbalances', concept_id='inequality', concept_group='socio_economics', misconception_tags=['fails_to_provide_examples'], diagnostic_tags=['explanation']),
        
        _with_metadata({
            'title': 'Importance of Goal Setting',
            'prompt': f"{business['entrepreneur']} wants to start a business selling {business['item_sold']}. Explain to them why it is important to set goals for their new business, and mention the characteristics of good goals. (2 marks)",
            'marks': 2,
            'marking_points': [
                "It is important to set goals to help the business succeed, grow, and have direction.",
                "Goals should be SMART (Specific, Measurable, Achievable, Realistic, Time-bound)."
            ],
            'sample_answer': "Setting goals gives your business direction and helps it to succeed. It allows you to track progress. Good goals should follow the SMART criteria, meaning they are specific, measurable, achievable, realistic, and time-bound.",
            'difficulties': ['medium'],
            'hint_sections': [
                {'title': 'What is being tested?', 'text': 'Understanding the purpose of goal setting in business and the SMART criteria.'},
                {'title': 'Reasoning path', 'text': 'If you drive without knowing your destination, you get lost. A business without goals is similar. What acronym do we use for good goals?'},
                {'title': 'Transfer idea', 'text': 'Goals give a business a target to aim for.'}
            ],
            'guidelines': ['Look for a reason (success/direction) and a mention of SMART or its components.'],
            'teaching_note': 'The curriculum emphasizes SMART goals, so this must be mentioned for full marks.'
        }, subskill='discussion', learning_objective_id='lo_smart_goals', question_family_id='explain_goals', concept_id='goal_setting', concept_group='entrepreneurship', misconception_tags=['forgets_smart_criteria'], diagnostic_tags=['explanation']),
        
        _with_metadata({
            'title': 'Entrepreneurial Characteristics',
            'prompt': f"For an entrepreneur like {scenario['entrepreneur']} in {scenario['area']}, give three characteristics that a successful entrepreneur usually has, and briefly explain why each is important. (3 marks)",
            'marks': 3,
            'marking_points': [
                "Risk-taker: Willing to start something new without knowing if it will succeed.",
                "Hardworking/Persevering: Never gives up even when faced with adversity.",
                "Creative/Resourceful: Can find new ways of doing things or solving problems."
            ],
            'sample_answer': "1. Takes risks: They are willing to put their money and time into an idea that might fail.\n2. Perseveres: They do not give up when things get difficult.\n3. Creative: They find new and better ways to solve problems and create products.",
            'difficulties': ['easy', 'medium'],
            'hint_sections': [
                {'title': 'What is being tested?', 'text': 'Identifying and explaining the personal traits of entrepreneurs.'},
                {'title': 'Reasoning path', 'text': 'Think of someone who started a business. What kind of personality do they need to survive the stress, come up with ideas, and face the possibility of failure?'},
                {'title': 'Transfer idea', 'text': 'Entrepreneurs aren\'t just lucky; they have specific mindsets that help them overcome challenges.'}
            ],
            'guidelines': ['Accept any valid characteristics (e.g., confident, visionary, energetic, risk-taker, creative, hardworking) provided they are briefly explained.'],
            'guidelines': ['Mark out of 4 (1 mark for each valid step: e.g., surveying, calculating costs, advertising, opening).'],
            'teaching_note': 'Look for a logical progression from idea to execution.'
        }, subskill='discussion', learning_objective_id='lo_starting_process', question_family_id='start_business_steps', concept_id='starting_a_business', concept_group='starting_a_business', misconception_tags=['misses_planning_phase'], diagnostic_tags=['essay', 'business_process']),
        
        _with_metadata({
            'title': 'SWOT Analysis Case Study',
            'prompt': f"Read the scenario and prepare a SWOT analysis for the business in {scenario['area']}. Show ONE aspect under each element (Strengths, Weaknesses, Opportunities, Threats). (4 marks)\n\nScenario: {scenario['entrepreneur']} owns a small shop in {scenario['area']} that specialises in selling {scenario['item_sold']}. {scenario['entrepreneur']} is highly motivated and has a solid client base. However, {scenario['entrepreneur']} has no experience in accounting. The management of the shopping centre has offered larger premises to expand the business. However, a large retail chain store will soon open next door selling at a discount.",
            'marks': 4,
            'marking_points': [
                "Strength: Motivated / Solid client base",
                "Weakness: No knowledge of accounting",
                "Opportunity: Offered larger premises to expand",
                "Threat: Large retail chain store opening next door / selling at a discount"
            ],
            'sample_answer': "Strengths: Roger is highly motivated and has a solid client base.\nWeaknesses: He has no experience in accounting.\nOpportunities: He has been offered larger premises to expand his shop.\nThreats: A large retail chain store is opening next door and will sell games at a discount.",
            'difficulties': ['hard'],
            'hint_sections': [
                {'title': 'What is being tested?', 'text': 'Applying a SWOT analysis to a given business scenario.'},
                {'title': 'Reasoning path', 'text': 'Break down the acronym: S (internal good), W (internal bad), O (external good), T (external bad). Find one of each in the text.'},
                {'title': 'Transfer idea', 'text': 'SWOT helps businesses plan by leveraging what they are good at and preparing for external risks.'}
            ],
            'guidelines': ['Award 1 mark for each correctly identified element of the SWOT analysis from the text.']
        }, subskill='discussion', learning_objective_id='lo_swot', question_family_id='swot_case_study_exam', concept_id='swot_analysis', concept_group='starting_a_business', misconception_tags=['confuses_internal_external_factors'], diagnostic_tags=['case_study', 'exam_style']),
    ]



SUBSKILLS = ['def_poverty_line', 'def_entrepreneur', 'entrepreneurial_traits', 'planning_entrepreneurs_day', 'needs_wants_opportunity', 'swot_factors', 'variable_costs_production', 'calculate_profit_simple', 'promotional_channels', 'explain_imbalances', 'explain_goals', 'start_business_steps', 'swot_case_study_exam']



SUBSKILLS = ['def_poverty_line', 'def_entrepreneur', 'entrepreneurial_traits', 'planning_entrepreneurs_day', 'needs_wants_opportunity', 'swot_factors', 'variable_costs_production', 'calculate_profit_simple', 'promotional_channels', 'explain_imbalances', 'explain_goals', 'start_business_steps', 'swot_case_study_exam']

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
    for fn_name in ['_concept_pool', '_discussion_pool', '_build_sectors_questions', '_build_inputs_outputs_questions', '_build_productivity_questions', '_build_resources_questions', '_build_savings_pool']:
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
