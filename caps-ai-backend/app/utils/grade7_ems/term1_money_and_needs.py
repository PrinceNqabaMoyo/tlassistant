import random
from app.utils.ems_namelist import get_ems_scenario, get_random_need_and_want, NAMES, AREAS

def _rng(seed=None):
    return random.Random(seed)

TOPIC_ID = 'grade7_ems'
SUBTOPIC_ID = 'term1_money_and_needs'
CURRICULUM_REFERENCE = 'Term 1 > History of Money, Needs and Wants'

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
    need_want = get_random_need_and_want()
    
    return [
        _with_metadata({
            'title': 'Needs vs Wants Classification',
            'prompt': f"{scenario['entrepreneur']} from {scenario['area']} is deciding what to buy. Which of the following is considered a basic NEED rather than a want?",
            'options': [
                "A designer jacket to stay warm", 
                "Clean water to drink", 
                f"A new smartphone to call friends in {scenario['area']}", 
                "A gaming console for entertainment"
            ],
            'correct_index': 1,
            'explanation': "Clean water is essential for survival, making it a primary or basic need. The other items are secondary needs (wants) because you can survive without them.",
            'difficulties': ['easy', 'medium'],
            'marks': 2,
            'hint_sections': [
                {'title': 'What is being tested?', 'text': 'Differentiating between primary needs (essential for survival) and secondary needs (wants).'},
                {'title': 'Reasoning path', 'text': 'Ask yourself: Would the person die if they did not have this item?'},
                {'title': 'Transfer idea', 'text': 'Needs are universal (food, water, shelter), while wants are specific desires that make life more comfortable but are not necessary to live.'}
            ],
            'guidelines': ['Identify the item essential for survival.']
        }, subskill='concepts', learning_objective_id='lo_needs_vs_wants', question_family_id='needs_vs_wants_classification', concept_id='primary_needs', concept_group='needs_and_wants', misconception_tags=['confuses_luxury_with_need'], diagnostic_tags=['classification', 'needs']),
        
        _with_metadata({
            'title': 'Traditional vs Modern Societies',
            'prompt': "Which of the following is a characteristic of a traditional society?",
            'options': [
                "Using electronic banking (EFTs) to pay for goods.", 
                "Being highly industrialised and relying on technology.", 
                "Being self-sufficient and producing food for their own use.", 
                "Having highly specialised skills like a mechanic or doctor."
            ],
            'correct_index': 2,
            'explanation': "Traditional societies are self-sufficient, meaning they produce goods and foods for their own use rather than relying on technology or specialized trade.",
            'difficulties': ['easy', 'medium'],
            'marks': 2,
            'hint_sections': [
                {'title': 'What is being tested?', 'text': 'Identifying the key features of a traditional society versus a modern society.'},
                {'title': 'Reasoning path', 'text': 'Think about societies before industrialization and modern technology. How did they survive?'},
                {'title': 'Transfer idea', 'text': 'Traditional societies are usually small, rural, agricultural, and self-sufficient.'}
            ],
            'guidelines': ['Look for the option describing basic, self-sufficient living without modern technology.']
        }, subskill='concepts', learning_objective_id='lo_societal_types', question_family_id='traditional_vs_modern', concept_id='traditional_society_features', concept_group='history_of_money', misconception_tags=['confuses_traditional_with_modern'], diagnostic_tags=['classification', 'societies']),
        
        _with_metadata({
            'title': 'Economic Problem True/False',
            'prompt': "Is the following statement TRUE or FALSE? Secondary needs are more important than primary needs.",
            'options': ["TRUE", "FALSE"],
            'correct_index': 1,
            'explanation': "FALSE. Primary needs are essential for survival (food, water). Secondary needs (wants) are not.",
            'difficulties': ['hard'],
            'marks': 1,
            'hint_sections': [
                {'title': 'What is being tested?', 'text': 'Evaluating the importance of primary versus secondary needs.'},
                {'title': 'Reasoning path', 'text': 'Can you survive without primary needs? Can you survive without secondary needs?'},
                {'title': 'Transfer idea', 'text': 'Because survival depends on primary needs, they are always more important.'}
            ],
            'guidelines': ['Identify that secondary needs are wants, which are less important than basic needs.']
        }, subskill='concepts', learning_objective_id='lo_needs_hierarchy', question_family_id='needs_true_false', concept_id='primary_vs_secondary', concept_group='needs_and_wants', misconception_tags=['values_wants_over_needs'], diagnostic_tags=['true_false']),
    ]

def _discussion_pool(rng):
    """Dynamic discussion pool that utilizes ems_namelist for variations."""
    scenario = get_ems_scenario()
    need_want = get_random_need_and_want()
    
    return [
        _with_metadata({
            'title': 'The Economic Problem Essay',
            'prompt': f"Write a short paragraph describing the economic problem, using your own words. Use {scenario['entrepreneur']} from {scenario['area']} as an example in your explanation. (3 marks)",
            'marks': 3,
            'marking_points': [
                "Mentions that resources are scarce/limited.",
                "Mentions that human needs and wants are unlimited.",
                "Provides a valid example linking the two concepts."
            ],
            'sample_answer': f"The economic problem is that resources are limited but human needs and wants are unlimited. For example, {scenario['entrepreneur']} in {scenario['area']} has unlimited wants, like buying {need_want['want']}, but only has limited money (resources) to satisfy them.",
            'difficulties': ['medium', 'hard'],
            'hint_sections': [
                {'title': 'What is being tested?', 'text': 'Defining the fundamental economic problem.'},
                {'title': 'Reasoning path', 'text': 'Compare the amount of resources available in the world to the amount of things people desire.'},
                {'title': 'Transfer idea', 'text': 'Because we have limited resources and unlimited wants, we have to make choices. This is the basis of all economics.'}
            ],
            'guidelines': ['Ensure the definition explicitly mentions both "limited resources" and "unlimited wants".'],
            'teaching_note': 'Look for the contrast between limited inputs and infinite desires.'
        }, subskill='discussion', learning_objective_id='lo_economic_problem', question_family_id='economic_problem_essay', concept_id='the_economic_problem', concept_group='needs_and_wants', misconception_tags=['misses_scarcity_concept'], diagnostic_tags=['essay', 'economics']),
        
        _with_metadata({
            'title': 'Primary vs Secondary Needs',
            'prompt': "Explain why primary needs are more important than secondary needs. Provide an example. (3 marks)",
            'marks': 3,
            'marking_points': [
                "Primary needs are essential for survival (if not met, you die).",
                "Secondary needs cannot be focused on if primary needs are not met.",
                "Provides a valid example (e.g., cannot study if starving)."
            ],
            'sample_answer': "Primary needs are essential for survival. People cannot meet their secondary needs if their basic primary needs have not been met. For example, you cannot focus on your studies or buy luxury goods if you do not have enough food to eat.",
            'difficulties': ['easy', 'medium'],
            'hint_sections': [
                {'title': 'What is being tested?', 'text': 'Understanding the hierarchy of needs.'},
                {'title': 'Reasoning path', 'text': 'Think about what happens to a person if they do not have food or water, compared to what happens if they do not have a new phone.'},
                {'title': 'Transfer idea', 'text': 'Survival must always come before comfort or self-actualization.'}
            ],
            'guidelines': ['Ensure the answer clearly states that survival depends on primary needs.'],
            'teaching_note': 'This aligns with Maslow\'s hierarchy of needs, though Gr 7 EMS just calls them primary/secondary.'
        }, subskill='discussion', learning_objective_id='lo_primary_secondary', question_family_id='primary_vs_secondary_explanation', concept_id='hierarchy_of_needs', concept_group='needs_and_wants', misconception_tags=['treats_wants_as_needs'], diagnostic_tags=['explanation', 'needs']),
        
        _with_metadata({
            'title': 'Disadvantages of Bartering',
            'prompt': "Before money was invented, traditional societies used bartering. Discuss two disadvantages of the bartering system. (4 marks)",
            'marks': 4,
            'marking_points': [
                "It is difficult to find someone who wants exactly what you have and has exactly what you want (double coincidence of wants).",
                "Some items are not easily divisible (e.g., half a cow).",
                "It is difficult to store wealth with perishable commodities (e.g., tomatoes rot).",
                "It is hard to establish a standard measure of value (how many chickens equal one cow?)."
            ],
            'sample_answer': "One disadvantage of bartering is the 'double coincidence of wants'; it is hard to find a person who has what you want and also wants what you have. Another disadvantage is that it is difficult to store wealth, because commodities like vegetables will rot over time.",
            'difficulties': ['medium', 'hard'],
            'hint_sections': [
                {'title': 'What is being tested?', 'text': 'Understanding the limitations of trade without a standardized currency.'},
                {'title': 'Reasoning path', 'text': 'Imagine trying to trade a live cow for a loaf of bread. What are the problems with that transaction?'},
                {'title': 'Transfer idea', 'text': 'Money was invented specifically to solve these problems of divisibility, storage of value, and standardized exchange.'}
            ],
            'guidelines': ['Look for any two valid disadvantages from the standard economic theory of money.'],
            'teaching_note': 'The curriculum highlights the double coincidence of wants and the divisibility issue.'
        }, subskill='discussion', learning_objective_id='lo_bartering', question_family_id='bartering_disadvantages', concept_id='disadvantages_of_bartering', concept_group='history_of_money', misconception_tags=['thinks_bartering_is_easier'], diagnostic_tags=['explanation', 'money']),

        _with_metadata({
            'title': 'Paragraph Discussion on Needs',
            'prompt': "Write a paragraph in which you discuss primary and secondary needs in detail. Include what happens if they are not met, and how they drive human achievement. (10 marks)",
            'marks': 10,
            'marking_points': [
                "Primary needs are physical needs (food, water, shelter).",
                "If primary needs are not met, people cannot survive.",
                "Secondary needs are things our survival does not depend on.",
                "Secondary needs are also called wants.",
                "The constant desire to achieve a lifestyle to satisfy both needs and wants drives human achievement.",
                "Mentioning working hard or studying to earn more to satisfy wants."
            ],
            'sample_answer': "Basic or primary needs are physical needs like food, water, and shelter. If these are not met, people cannot survive. Once basic needs are met, people focus on secondary needs. Secondary needs (wants) are not essential for survival but are an important part of human development. The constant desire to satisfy our needs and wants drives us to achieve. We work hard, aim for promotions, and study to improve ourselves so we can satisfy more wants.",
            'difficulties': ['hard'],
            'hint_sections': [
                {'title': 'What is being tested?', 'text': 'A comprehensive understanding of primary vs secondary needs and their role in driving economic activity.'},
                {'title': 'Reasoning path', 'text': 'Start by defining primary needs and their link to survival. Then define secondary needs (wants). Finally, explain how the desire to satisfy wants motivates people to work and study.'},
                {'title': 'Transfer idea', 'text': 'Economics is driven by human behavior—specifically, the endless pursuit of satisfying unlimited wants.'}
            ],
            'guidelines': ['Award marks for defining primary needs, secondary needs, survival aspects, and the driving force of human achievement.']
        }, subskill='discussion', learning_objective_id='lo_needs_discussion', question_family_id='needs_essay_exam', concept_id='needs_essay', concept_group='needs_and_wants', misconception_tags=['misses_achievement_link'], diagnostic_tags=['essay', 'exam_style']),
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
