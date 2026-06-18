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
            'title': 'SWOT Analysis',
            'prompt': "In a business SWOT analysis, what does the 'T' stand for?",
            'options': [
                "Targets", 
                "Tactics", 
                "Threats", 
                "Taxes"
            ],
            'correct_index': 2,
            'explanation': "SWOT stands for Strengths, Weaknesses, Opportunities, and Threats.",
            'difficulties': ['easy'],
            'marks': 1,
            'hint_sections': [
                {'title': 'What is being tested?', 'text': 'Knowledge of the SWOT acronym.'},
                {'title': 'Reasoning path', 'text': 'S is for Strengths, W is for Weaknesses, O is for Opportunities... what is the opposite of an opportunity?'},
                {'title': 'Transfer idea', 'text': 'Threats are external factors that could negatively affect a business, like a new competitor.'}
            ],
            'guidelines': ['Identify the correct word for the T in SWOT.']
        }, subskill='concepts', learning_objective_id='lo_swot', question_family_id='swot_acronym', concept_id='swot', concept_group='entrepreneurship', misconception_tags=['confuses_t_with_targets'], diagnostic_tags=['definition', 'acronym']),
        
        _with_metadata({
            'title': 'Fixed vs Variable Costs',
            'prompt': "Which of the following is the best definition of a fixed cost?",
            'options': [
                "Costs that increase when you produce more goods.", 
                "Costs of producing goods that do not change, no matter how many goods are produced.", 
                "The final price at which a good is sold to a customer.", 
                "A cost that is negotiated with a supplier once a year."
            ],
            'correct_index': 1,
            'explanation': "Fixed costs are costs that do not change regardless of how many items a business produces (e.g., rent).",
            'difficulties': ['medium'],
            'marks': 1,
            'hint_sections': [
                {'title': 'What is being tested?', 'text': 'Differentiating fixed and variable costs.'},
                {'title': 'Reasoning path', 'text': 'What does "fixed" mean? It means it stays the same. Does it stay the same over time, or stay the same regardless of production volume?'},
                {'title': 'Transfer idea', 'text': 'Rent is a fixed cost. You pay the same rent whether you sell 1 cake or 100 cakes.'}
            ],
            'guidelines': ['Identify the correct definition of fixed costs relative to production volume.']
        }, subskill='concepts', learning_objective_id='lo_fixed_costs', question_family_id='def_fixed_costs', concept_id='fixed_costs', concept_group='entrepreneurship', misconception_tags=['confuses_fixed_with_variable_cost'], diagnostic_tags=['definition']),

        _with_metadata({
            'title': 'Advertising Principles',
            'prompt': "Which of these is a key principle when creating an advertisement for a new product?",
            'options': [
                "Ensure it reaches your target market and gives clear information.",
                "Include as much information as possible, even if it is not relevant.",
                "Always choose the most expensive advertising medium available.",
                "Focus only on the product features and ignore customer benefits."
            ],
            'correct_index': 0,
            'explanation': "Effective advertising must reach the target market, be clear, and communicate value.",
            'difficulties': ['medium'],
            'marks': 1,
            'hint_sections': [
                {'title': 'What is being tested?', 'text': 'Knowledge of the SWOT acronym.'},
                {'title': 'Reasoning path', 'text': 'S is for Strengths, W is for Weaknesses, O is for Opportunities... what is the opposite of an opportunity?'},
                {'title': 'Transfer idea', 'text': 'Threats are external factors that could negatively affect a business, like a new competitor.'}
            ],
            'guidelines': ['Look for advertising that hits the demographic effectively.']
        }, subskill='concepts', learning_objective_id='lo_advertising_principles', question_family_id='advertising_medium', concept_id='advertising_media', concept_group='starting_a_business', misconception_tags=['assumes_tv_is_always_best'], diagnostic_tags=['classification', 'advertising']),
        
        _with_metadata({
            'title': 'Controlled Test Term 3 - Advertising Principles',
            'prompt': "List TWO principles of advertising that you need to apply to ensure that you reach your goals.",
            'options': [
                "Ensure it reaches your target market and gives clear information.",
                "Always use television and hire famous people.",
                "Make it as long as possible and use difficult words.",
                "Only advertise once a year and don't include prices."
            ],
            'correct_index': 0,
            'explanation': "Advertising principles include reaching your target market, choosing the right medium for your budget, giving clear information, and making it stand out.",
            'difficulties': ['hard'],
            'marks': 2,
            'hint_sections': [
                {'title': 'What is being tested?', 'text': 'Understanding the core rules (principles) of advertising.'},
                {'title': 'Reasoning path', 'text': 'What makes an advert effective? Does it matter who sees it, and whether they understand what you are selling?'},
                {'title': 'Transfer idea', 'text': 'Good advertising must be clear, targeted, and budget-appropriate.'}
            ],
            'guidelines': ['Identify the valid principles of advertising.']
        }, subskill='concepts', learning_objective_id='lo_advertising_principles', question_family_id='advertising_principles_exam', concept_id='advertising_media', concept_group='starting_a_business', misconception_tags=['focuses_only_on_medium'], diagnostic_tags=['definition']),
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
