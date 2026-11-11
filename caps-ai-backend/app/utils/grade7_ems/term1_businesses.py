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
    """Dynamic concept pool that utilizes ems_namelist for variations."""
    scenario = get_ems_scenario(rng)
    
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
            'difficulties': ['easy', 'medium', 'hard'],
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
            'difficulties': ['easy', 'medium', 'hard'],
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
            'prompt': f"{scenario['entrepreneur']} investigates the supply chain of enterprises in {scenario['area']}. Which of the following best describes manufacturers?",
            'options': [
                "People who buy or use goods and services.",
                "People who use resources to produce goods and services.",
                "Businesses that pay tax.",
                "Inhabitants of developing countries."
            ],
            'correct_index': 1,
            'explanation': "Manufacturers are people or businesses who use resources to produce goods and services.",
            'difficulties': ['easy', 'medium', 'hard'],
            'marks': 1,
            'hint_sections': [
                {'title': 'What is being tested?', 'text': 'Defining the role of manufacturers.'},
                {'title': 'Reasoning path', 'text': 'Manufacturing involves making something. Who takes raw resources and makes products?'},
                {'title': 'Transfer idea', 'text': 'Manufacturers convert raw materials into finished goods.'}
            ],
            'guidelines': ['Match the definition to the correct terminology.']
        }, subskill='concepts', learning_objective_id='lo_manufacturers', question_family_id='manufacturers_def', concept_id='manufacturers', concept_group='businesses', misconception_tags=['confuses_manufacturer_consumer'], diagnostic_tags=['definition']),

        _with_metadata({
            'title': 'Trading vs Service Business',
            'prompt': f"{scenario['entrepreneur']} operates a hair salon and car wash in {scenario['area']}. What type of business is this?",
            'options': [
                "A service business, because they provide skills, expertise, and labour rather than tangible goods.",
                "A manufacturing business, because they build vehicles from raw metals.",
                "A trading business, because they buy and sell pre-packaged supermarket items.",
                "A primary sector business, because they harvest agricultural crops."
            ],
            'correct_index': 0,
            'explanation': "A service business sells activities, skills, advice, or labour (hair styling, washing) rather than physical merchandise.",
            'difficulties': ['easy', 'medium', 'hard'],
            'marks': 1,
            'hint_sections': [
                {'title': 'What is being tested?', 'text': 'Distinguishing service businesses from trading and manufacturing businesses.'},
                {'title': 'Reasoning path', 'text': 'Does a salon customer walk away with a manufactured product, or did they pay for a skilled service?'},
                {'title': 'Transfer idea', 'text': 'Service businesses satisfy intangible needs.'}
            ],
            'guidelines': ['Identify that hair salons and car washes are service businesses.']
        }, subskill='concepts', learning_objective_id='lo_service_business', question_family_id='service_business_classification', concept_id='service_business', concept_group='businesses', misconception_tags=['confuses_service_with_trading'], diagnostic_tags=['classification']),

        _with_metadata({
            'title': 'Sectors of Production - Primary Sector',
            'prompt': f"A business in {scenario['area']} extracts coal from a mine and grows timber on a plantation. Which economic sector is this?",
            'options': [
                "Primary sector, which involves extracting natural resources directly from the earth.",
                "Secondary sector, which manufactures finished furniture and plastics.",
                "Tertiary sector, which sells insurance and internet banking.",
                "Quaternary sector, which develops artificial intelligence software."
            ],
            'correct_index': 0,
            'explanation': "The primary sector deals with raw material extraction from nature (mining, agriculture, fishing, forestry).",
            'difficulties': ['easy', 'medium', 'hard'],
            'marks': 1,
            'hint_sections': [
                {'title': 'What is being tested?', 'text': 'Identifying the primary sector of production.'},
                {'title': 'Reasoning path', 'text': 'Where does the resource come from? Directly from the ground or nature.'},
                {'title': 'Transfer idea', 'text': 'Primary sector activities provide the raw inputs for factories in the secondary sector.'}
            ],
            'guidelines': ['Identify the primary sector.']
        }, subskill='concepts', learning_objective_id='lo_primary_sector', question_family_id='primary_sector_def', concept_id='primary_sector', concept_group='businesses', misconception_tags=['confuses_primary_secondary'], diagnostic_tags=['classification']),

        _with_metadata({
            'title': 'Durable vs Non-Durable Capital Goods',
            'prompt': f"Which of the following is considered a CAPITAL GOOD purchased by a bakery in {scenario['area']}?",
            'options': [
                "An industrial commercial baking oven that lasts for 10 years to produce bread.",
                "Bags of cake flour and packets of yeast used in daily baking.",
                "Paper bags and serviettes given to customers.",
                "Fresh milk purchased every morning for staff tea."
            ],
            'correct_index': 0,
            'explanation': "Capital goods are long-lasting man-made tools and machinery used by businesses to produce other goods and services.",
            'difficulties': ['easy', 'medium', 'hard'],
            'marks': 1,
            'hint_sections': [
                {'title': 'What is being tested?', 'text': 'Identifying capital goods used in production.'},
                {'title': 'Reasoning path', 'text': 'What machine or tool does the bakery use repeatedly over many years to make products?'},
                {'title': 'Transfer idea', 'text': 'Flour and yeast are raw materials; the oven is a capital good.'}
            ],
            'guidelines': ['Select the industrial oven as a capital good.']
        }, subskill='concepts', learning_objective_id='lo_capital_goods', question_family_id='capital_goods_def', concept_id='capital_goods', concept_group='goods_and_services', misconception_tags=['confuses_capital_good_raw_material'], diagnostic_tags=['classification']),
    ]

def _discussion_pool(rng):
    """Dynamic discussion pool that utilizes ems_namelist for variations."""
    scenario = get_ems_scenario(rng)
    
    return [
        _with_metadata({
            'title': 'Households as Producers',
            'diagram_spec': {
        "diagram_role": "context",
                'kind': 'circular_flow',
                'title': 'Two-Sector Economic Circular Flow (Households & Businesses)',
            },
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
            'title': 'Impact of Socio-Economic Shocks & Health Epidemics on Businesses',
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
        }, subskill='discussion', learning_objective_id='lo_health_epidemics', question_family_id='socio_economic_shocks_on_business', concept_id='health_epidemics_on_business', concept_group='businesses', misconception_tags=['ignores_consumer_spending_shift'], diagnostic_tags=['explanation', 'socioeconomic']),
        
        _with_metadata({
            'title': 'Advantages of Informal Businesses',
            'prompt': f"{scenario['entrepreneur']} observes informal traders operating in {scenario['area']}. Identify and explain two advantages of operating an informal business in this community. (4 marks)",
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
            'diagram_spec': {
        "diagram_role": "context",
                'kind': 'production_chain',
                'raw': 'Raw Fruit Harvest',
                'primary': 'Fruit Farm (Orchard)',
                'secondary': 'Jam Processing Factory',
                'tertiary': 'Retail Food Market',
                'product': 'Jars of Fruit Jam'
            },
            'prompt': f"An agricultural entrepreneur in {scenario['area']} seeks to expand. Use examples to explain why a business can be involved in more than one stage of the production process. (5 marks)",
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



SUBSKILLS = ['formal_informal_classification', 'goods_classification', 'manufacturers_def', 'service_business_classification', 'primary_sector_def', 'capital_goods_def', 'households_producers_explanation', 'socio_economic_shocks_on_business', 'epidemics_impact', 'informal_business_advantages', 'production_stages_exam']



SUBSKILLS = ['formal_informal_classification', 'goods_classification', 'manufacturers_def', 'service_business_classification', 'primary_sector_def', 'capital_goods_def', 'households_producers_explanation', 'socio_economic_shocks_on_business', 'epidemics_impact', 'informal_business_advantages', 'production_stages_exam']

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
