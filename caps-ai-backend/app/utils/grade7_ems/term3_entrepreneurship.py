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

def _concept_pool(rng):
    """MCQ concepts for term 3."""
    return [
        _with_metadata({
            'title': 'Defining the Poverty Line',
            'prompt': "What does the 'poverty line' refer to?",
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
            'prompt': "Which statement BEST describes an entrepreneur?",
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
            'prompt': "Which combination represents key personal characteristics of a successful entrepreneur?",
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
            'prompt': "When Grade 7 learners organize a school Entrepreneur's Day, what is the FIRST crucial step in the planning process?",
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
            'prompt': "In business ideation, how can an entrepreneur turn a community's UNMET NEED into a viable business opportunity?",
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
            'prompt': "In a SWOT analysis, which elements represent INTERNAL factors that the entrepreneur can directly control?",
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
            'prompt': "If a student bakes muffins for Entrepreneur's Day, which cost is classified as a VARIABLE cost?",
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
            'prompt': "An entrepreneur generates R1 500 in sales revenue from selling handcrafted beaded bracelets. The total production and stall expenses amounted to R950. What is the net profit earned?",
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
            'prompt': "Which promotional strategy is MOST cost-effective for a school Entrepreneur's Day stall?",
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
    business = get_ems_scenario()
    
    return [
        _with_metadata({
            'title': 'Socio-economic Imbalances',
            'prompt': "In your own words, explain what socio-economic imbalances are, and give examples. (2 marks)",
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
            'prompt': "Give three characteristics that a successful entrepreneur usually has, and briefly explain why each is important. (3 marks)",
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
            'prompt': "Read the scenario and prepare a SWOT analysis for the business. Show ONE aspect under each element (Strengths, Weaknesses, Opportunities, Threats). (4 marks)\n\nScenario: Roger owns a small shop that specialises in buying and selling computer games. He is highly motivated and has a solid client base. However, Roger has no experience when it comes to accounting. The management of the shopping centre has offered Roger larger premises from where he can run his business. He has also been informed that a large retail chain store will soon be opening next door and will also be selling computer games at a discount.",
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

def generate(subskill="concepts", difficulty="medium", count=1, mode="scaffold", seed=None, **kwargs):
    rng = _rng(seed)
    
    if subskill == "discussion":
        pool = _discussion_pool(rng)
        selected = [q for q in pool if difficulty in q.get('difficulties', ['medium'])]
        if not selected: selected = pool
        if count == 1 and seed is not None:
            chosen = [selected[int(seed) % len(selected)]]
        else:
            chosen = rng.sample(selected, min(count, len(selected)))
        return [_typed_question(rng, item, mode=mode) for item in chosen]
    else:
        pool = _concept_pool(rng)
        selected = [q for q in pool if difficulty in q.get('difficulties', ['medium'])]
        if not selected: selected = pool
        if count == 1 and seed is not None:
            chosen = [selected[int(seed) % len(selected)]]
        else:
            chosen = rng.sample(selected, min(count, len(selected)))
        return [_mcq_question(rng, item, mode=mode) for item in chosen]
