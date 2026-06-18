import random
from app.utils.ems_namelist import get_ems_scenario, get_random_need_and_want, NAMES, AREAS

def _rng(seed=None):
    return random.Random(seed)

TOPIC_ID = 'grade7_ems'
SUBTOPIC_ID = 'term1_businesses'
CURRICULUM_REFERENCE = 'Term 1 > Goods and Services, Businesses'

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
    """Dynamic concept pool that utilizes ems_namelist for variations."""
    scenario = get_ems_scenario()
    
    return [
        _with_metadata({
            'title': 'Formal vs Informal Business Identification',
            'prompt': f"{scenario['entrepreneur']} operates a spaza shop in {scenario['area']}. It is not registered for tax and is not monitored by the government. What type of business is this?",
            'options': [
                "A formal business.", 
                "An informal business.", 
                "A primary sector business.", 
                "A manufacturing business."
            ],
            'correct_index': 1,
            'explanation': "Because the spaza shop is not registered for tax and is not monitored by the government, it is classified as an informal business.",
            'difficulties': ['easy'],
            'marks': 1,
            'hint_sections': [
                {'title': 'What is being tested?', 'text': 'Identifying the difference between formal and informal businesses.'},
                {'title': 'Reasoning path', 'text': 'Check the key details: Is it registered for tax? Is the government monitoring it? If no, it falls into the informal sector.'},
                {'title': 'Transfer idea', 'text': 'Informal businesses like hawkers, car guards, and spaza shops do not pay income tax and are usually smaller scale.'}
            ],
            'guidelines': ['Identify the key characteristics of informal businesses (unregistered, no income tax).']
        }, subskill='concepts', learning_objective_id='lo_formal_informal', question_family_id='formal_informal_classification', concept_id='informal_businesses', concept_group='businesses', misconception_tags=['confuses_sectors_with_formality'], diagnostic_tags=['classification', 'businesses']),
        
        _with_metadata({
            'title': 'Categories of Goods',
            'prompt': f"A business in {scenario['area']} sells bread and milk. What category of goods are these?",
            'options': [
                "Durable goods", 
                "Capital goods", 
                "Consumable goods", 
                "Luxury goods"
            ],
            'correct_index': 2,
            'explanation': "Bread and milk are consumable goods because they do not last and are used up quickly after purchase.",
            'difficulties': ['easy', 'medium'],
            'marks': 1,
            'hint_sections': [
                {'title': 'What is being tested?', 'text': 'Classifying goods into specific categories (durable, consumable, capital, luxury).'},
                {'title': 'Reasoning path', 'text': 'How long do bread and milk last? Once you eat them, they are gone.'},
                {'title': 'Transfer idea', 'text': 'Consumable goods are used up quickly, whereas durable goods (like a wooden table) last a long time.'}
            ],
            'guidelines': ['Differentiate between durable and consumable.']
        }, subskill='concepts', learning_objective_id='lo_categories_of_goods', question_family_id='goods_classification', concept_id='consumable_goods', concept_group='goods_and_services', misconception_tags=['confuses_durable_consumable'], diagnostic_tags=['classification', 'goods']),
        
        _with_metadata({
            'title': 'Controlled Test Term 1 - Manufacturers',
            'prompt': "Which of the following best describes manufacturers?",
            'options': [
                "People who buy or use goods and services.",
                "People who use resources to produce goods and services.",
                "Businesses that pay tax.",
                "Inhabitants of developing countries."
            ],
            'correct_index': 1,
            'explanation': "Manufacturers are people or businesses who use resources to produce goods and services.",
            'difficulties': ['hard'],
            'marks': 1,
            'hint_sections': [
                {'title': 'What is being tested?', 'text': 'Defining the role of manufacturers.'},
                {'title': 'Reasoning path', 'text': 'Manufacturing involves making something. Who takes raw resources and makes products?'},
                {'title': 'Transfer idea', 'text': 'Manufacturers convert raw materials into finished goods.'}
            ],
            'guidelines': ['Match the definition to the correct terminology.']
        }, subskill='concepts', learning_objective_id='lo_manufacturers', question_family_id='manufacturers_def', concept_id='manufacturers', concept_group='businesses', misconception_tags=['confuses_manufacturer_consumer'], diagnostic_tags=['definition']),
    ]

def _discussion_pool(rng):
    """Dynamic discussion pool that utilizes ems_namelist for variations."""
    scenario = get_ems_scenario()
    
    return [
        _with_metadata({
            'title': 'Households as Producers',
            'prompt': f"Describe one way in which households in {scenario['area']} act as producers. (2 marks)",
            'marks': 2,
            'marking_points': [
                "Households sell/supply their labour to businesses.",
                "They get paid by businesses to do work that produces goods and services."
            ],
            'sample_answer': "Households act as producers by 'selling' their labour to businesses. People from households go to work and get paid by businesses to produce goods and services, making them producers of labour.",
            'difficulties': ['medium', 'hard'],
            'hint_sections': [
                {'title': 'What is being tested?', 'text': 'Understanding the dual role of households in the economy.'},
                {'title': 'Reasoning path', 'text': 'We know households buy things (consumers). But what do people in households provide to businesses in order to earn money?'},
                {'title': 'Transfer idea', 'text': 'Households provide the labour force that businesses need to operate.'}
            ],
            'guidelines': ['Ensure the answer explicitly mentions supplying labour to businesses.'],
            'teaching_note': 'Learners often forget that households produce labour.'
        }, subskill='discussion', learning_objective_id='lo_households_producers', question_family_id='households_producers_explanation', concept_id='households_as_producers', concept_group='goods_and_services', misconception_tags=['thinks_households_only_consume'], diagnostic_tags=['explanation', 'households']),
        
        _with_metadata({
            'title': 'Impact of Health Epidemics',
            'prompt': f"Explain why it is bad for formal and informal businesses in {scenario['area']} if their employees are affected by a health epidemic such as HIV/Aids. Name three specific effects. (6 marks)",
            'marks': 6,
            'marking_points': [
                "Sick workers are not productive because they are unwell and frequently absent.",
                "If an informal business owner is sick, the business must close and earns no money.",
                "Employees may miss work to care for sick family members.",
                "Households spend their money on medical costs instead of buying goods from businesses.",
                "Businesses lose skilled workers when they die or stop working, costing money to train new staff."
            ],
            'sample_answer': "Firstly, sick workers are not productive and are frequently off sick. Secondly, if an employee is not sick themselves, they might have to miss work to care for a sick family member, which also lowers productivity. Finally, households spend their savings on medical costs instead of buying goods from businesses, which negatively affects the economy.",
            'difficulties': ['hard'],
            'hint_sections': [
                {'title': 'What is being tested?', 'text': 'Analyzing the socio-economic impact of diseases on business productivity and consumer spending.'},
                {'title': 'Reasoning path', 'text': 'Think about three different angles: The sick worker, the healthy worker who has a sick relative, and how the family spends its money.'},
                {'title': 'Transfer idea', 'text': 'Health epidemics do not just affect hospitals; they reduce labour supply and shift consumer spending away from retail/services.'}
            ],
            'guidelines': ['Look for 3 distinct effects from the curriculum list.'],
            'teaching_note': 'Ensure they provide 3 points. They can get 2 marks per well-explained point.'
        }, subskill='discussion', learning_objective_id='lo_health_epidemics', question_family_id='epidemics_impact', concept_id='health_epidemics_on_business', concept_group='businesses', misconception_tags=['ignores_consumer_spending_shift'], diagnostic_tags=['explanation', 'socioeconomic']),
        
        _with_metadata({
            'title': 'Advantages of Informal Businesses',
            'prompt': "Identify and explain two advantages of operating an informal business in a local community. (4 marks)",
            'marks': 4,
            'marking_points': [
                "They provide income for families who cannot find formal employment.",
                "They offer convenient services to the local community.",
                "They require very little capital to start.",
                "They do not have to pay registration fees or complicated taxes."
            ],
            'sample_answer': "Two advantages of informal businesses are that they create jobs for people who cannot find work in the formal sector, and they provide convenient goods and services to the people living in their local community.",
            'difficulties': ['hard'],
            'hint_sections': [
                {'title': 'What is being tested?', 'text': 'Evaluating the positive aspects of the informal sector.'},
                {'title': 'Reasoning path', 'text': 'Why do people start informal businesses? Think about ease of entry and the benefit to the community.'},
                {'title': 'Transfer idea', 'text': 'Informal businesses often fill gaps that formal businesses might ignore due to lower profit margins.'}
            ],
            'guidelines': ['Provide any two valid advantages of informal businesses.']
        }, subskill='discussion', learning_objective_id='lo_informal_businesses', question_family_id='informal_business_advantages', concept_id='advantages_informal_businesses', concept_group='businesses', misconception_tags=['assumes_informal_is_bad'], diagnostic_tags=['explanation', 'businesses']),
        
        _with_metadata({
            'title': 'Production Stages',
            'prompt': "Use examples to explain why a business can be involved in more than one stage of the production process. (5 marks)",
            'marks': 5,
            'marking_points': [
                "Mentioning a business in the primary sector (e.g., farming).",
                "Mentioning the same business processing the goods (secondary sector).",
                "Mentioning the same business selling the goods directly (tertiary sector).",
                "Providing a clear, cohesive example linking all three."
            ],
            'sample_answer': "A business can be involved in multiple stages to maximize profit. For example, a farmer can grow fruit trees, which is the primary sector. The farmer can then dry the fruit to make jam, which is the secondary sector (manufacturing). Finally, the farmer can sell the jam directly to customers at a craft market, which is the tertiary sector.",
            'difficulties': ['hard'],
            'hint_sections': [
                {'title': 'What is being tested?', 'text': 'Understanding that primary, secondary, and tertiary sectors can overlap within one business.'},
                {'title': 'Reasoning path', 'text': 'Think of a product like fruit. Who grows it? Who turns it into jam? Who sells the jam? Can one person do all three?'},
                {'title': 'Transfer idea', 'text': 'By controlling multiple stages (e.g., raw material extraction, processing, and retail), a business reduces reliance on middlemen and increases profit.'}
            ],
            'guidelines': ['Give full marks if the student successfully explains how one entity can participate in 2 or 3 sectors using a clear example.']
        }, subskill='discussion', learning_objective_id='lo_production_stages', question_family_id='production_stages_exam', concept_id='production_stages', concept_group='businesses', misconception_tags=['believes_one_business_one_sector'], diagnostic_tags=['essay', 'exam_style']),
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
