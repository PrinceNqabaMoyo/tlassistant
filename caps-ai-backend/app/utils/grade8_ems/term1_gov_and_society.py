import random
from app.utils.ems_namelist import get_ems_scenario, get_random_need_and_want, NAMES, AREAS

def _rng(seed=None):
    return random.Random(seed)

TOPIC_ID = 'grade8_ems'
SUBTOPIC_ID = 'term1_gov_and_society'
CURRICULUM_REFERENCE = 'Term 1 > Government, National Budget, and Standard of Living'

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
        'id': f"g8_ems_mcq_{rng.randint(1000, 999999)}",
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
        'id': f"g8_ems_typed_{rng.randint(1000, 999999)}",
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
    scenario = get_ems_scenario()
    
    return [
        _with_metadata({
            'title': 'Levels of Government',
            'prompt': f"In South Africa, the government is divided into three levels. Which level of government is led by a Mayor and Councillors, and is responsible for running municipalities in places like {scenario['area']}?",
            'options': [
                "National government", 
                "Provincial government", 
                "Local government", 
                "Regional government"
            ],
            'correct_index': 2,
            'explanation': "The local government is the third level of government, responsible for running the municipality and is led by the Mayor and Councillors.",
            'difficulties': ['easy', 'medium'],
            'marks': 2,
            'hint_sections': [
                {'title': 'What is being tested?', 'text': 'Identifying the structure and leadership of different levels of government in South Africa.'},
                {'title': 'Nudge', 'text': 'Think about who you would contact if the streetlights in your immediate neighbourhood were broken.'},
                {'title': 'Breakdown', 'text': 'National government is led by the President. Provincial government is led by a Premier. Which level is left for the Mayor?'}
            ],
            'guidelines': ['Identify the level of government responsible for municipalities.']
        }, subskill='concepts', learning_objective_id='lo_levels_of_gov', question_family_id='gov_levels_classification', concept_id='local_gov', concept_group='government', misconception_tags=['confuses_levels_of_gov'], diagnostic_tags=['classification', 'government']),
        
        _with_metadata({
            'title': 'Direct vs Indirect Taxes',
            'prompt': f"{scenario['entrepreneur']} goes to the shop to buy groceries and pays Value-Added Tax (VAT) on some items. What type of tax is VAT?",
            'options': [
                "Direct tax", 
                "Indirect tax", 
                "Corporate tax", 
                "Income tax"
            ],
            'correct_index': 1,
            'explanation': "VAT is an indirect tax. This means people pay it to the government indirectly via a business or service provider, rather than paying it directly to SARS like Income Tax.",
            'difficulties': ['easy', 'medium'],
            'marks': 2,
            'hint_sections': [
                {'title': 'What is being tested?', 'text': 'Differentiating between direct and indirect taxes.'},
                {'title': 'Nudge', 'text': 'Does the consumer pay VAT directly to the government, or does the shop collect it first?'},
                {'title': 'Breakdown', 'text': 'Direct taxes (like Income Tax) are paid directly to the government by the person earning the income. Taxes that are shifted (paid to a business who then pays the government) are called what?'}
            ],
            'guidelines': ['Distinguish between direct and indirect tax based on who pays the government.']
        }, subskill='concepts', learning_objective_id='lo_tax_types', question_family_id='tax_classification', concept_id='indirect_tax', concept_group='national_budget', misconception_tags=['confuses_tax_types'], diagnostic_tags=['classification', 'budget']),
        
        _with_metadata({
            'title': 'Government Expenditure',
            'prompt': "When the government spends money on building RDP houses for the poor, under which category of the National Budget does this expenditure fall?",
            'options': [
                "Social welfare", 
                "Housing", 
                "Transport", 
                "Safety and security"
            ],
            'correct_index': 1,
            'explanation': "Building RDP houses for the poor, disadvantaged, and unemployed falls under Housing expenditure.",
            'difficulties': ['easy'],
            'marks': 1,
            'hint_sections': [
                {'title': 'What is being tested?', 'text': 'Categorizing government expenditure.'},
                {'title': 'Nudge', 'text': 'Look closely at the purpose of the spending in the question.'},
                {'title': 'Breakdown', 'text': 'The question specifically mentions "building RDP houses". Which option relates to houses?'}
            ],
            'guidelines': ['Match the expenditure to the correct category.']
        }, subskill='concepts', learning_objective_id='lo_gov_expenditure', question_family_id='expenditure_classification', concept_id='housing', concept_group='national_budget', misconception_tags=['confuses_social_welfare_with_housing'], diagnostic_tags=['classification', 'budget']),
        
        _with_metadata({
            'title': 'Lifestyles and Societies',
            'prompt': "Which of the following best describes a self-sufficient, rural society?",
            'options': [
                "People produce goods and services in large quantities for consumption by many different people.", 
                "People rely heavily on technology, commerce, and complex infrastructure.", 
                "People meet most of their own needs through their immediate environment and produce food for their own use.", 
                "People experience high levels of noise pollution and traffic congestion."
            ],
            'correct_index': 2,
            'explanation': "Self-sufficient, rural societies produce their own food and meet most of their needs from their immediate environment, rather than relying on mass production or modern commerce.",
            'difficulties': ['easy', 'medium'],
            'marks': 2,
            'hint_sections': [
                {'title': 'What is being tested?', 'text': 'Identifying characteristics of different types of societies.'},
                {'title': 'Nudge', 'text': 'What does the word "self-sufficient" mean?'},
                {'title': 'Breakdown', 'text': 'Self-sufficient means providing for oneself without needing outside help. Which option describes people providing for themselves?'}
            ],
            'guidelines': ['Identify the definition of a self-sufficient society.']
        }, subskill='concepts', learning_objective_id='lo_societies', question_family_id='society_classification', concept_id='rural_society', concept_group='standard_of_living', misconception_tags=['confuses_rural_with_modern'], diagnostic_tags=['classification', 'societies'])
    ]

def _discussion_pool(rng):
    scenario = get_ems_scenario()
    
    return [
        _with_metadata({
            'title': 'The National Budget',
            'prompt': f"Explain how the South African government uses the National Budget to address economic inequalities in communities like {scenario['area']}. Provide at least three examples. (6 marks)",
            'marks': 6,
            'marking_points': [
                "Mentions providing free health care (e.g. for children/pregnant women).",
                "Mentions nutrition programmes for school learners.",
                "Mentions building low-cost housing or improving infrastructure.",
                "Mentions providing social grants (old-age, disability, child support).",
                "Mentions creating employment through community work programmes."
            ],
            'sample_answer': "The government addresses economic inequalities by using tax revenue to support the poor. They do this by providing social grants to the elderly and disabled. They also build low-cost (RDP) housing for the poor and improve infrastructure in disadvantaged areas. Furthermore, they provide free healthcare and nutrition programmes in schools to ensure basic needs are met.",
            'difficulties': ['medium', 'hard'],
            'hint_sections': [
                {'title': 'What is being tested?', 'text': 'Explaining the practical applications of government revenue to solve social issues.'},
                {'title': 'Nudge', 'text': 'Think about what the government gives to people who cannot afford basic necessities.'},
                {'title': 'Breakdown', 'text': 'List three specific ways the government helps the poor. Consider housing, money (grants), and food/health.'}
            ],
            'guidelines': ['Provide three distinct examples of government spending aimed at reducing inequality.'],
            'teaching_note': 'Ensure learners do not confuse general infrastructure (like national highways) with targeted inequality redress (like RDP housing or grants).'
        }, subskill='discussion', learning_objective_id='lo_economic_inequality', question_family_id='inequality_essay', concept_id='national_budget_inequality', concept_group='national_budget', misconception_tags=['vague_understanding_of_inequality'], diagnostic_tags=['essay', 'budget']),
        
        _with_metadata({
            'title': 'Government as a Producer and Consumer',
            'prompt': "The government plays a role as both a producer and a consumer in the economy. Explain one way the government acts as a producer, and one way it acts as a consumer for households. (4 marks)",
            'marks': 4,
            'marking_points': [
                "Producer: Employs civil servants (teachers, police) or provides services like Eskom.",
                "Producer: Provides skills/training or financial assistance.",
                "Consumer: Buys goods/services from businesses to build infrastructure.",
                "Consumer: Provides public goods/services that businesses don't provide."
            ],
            'sample_answer': "As a producer, the government produces services by employing civil servants like teachers and police officers to serve the households. As a consumer, the government buys goods and services, such as materials to build infrastructure (like roads and clinics) which are then used by households.",
            'difficulties': ['medium', 'hard'],
            'hint_sections': [
                {'title': 'What is being tested?', 'text': 'Differentiating the dual roles of the government in the circular flow.'},
                {'title': 'Nudge', 'text': 'When the government hires people, what role is it playing? When it buys cement to build a road, what role is it playing?'},
                {'title': 'Breakdown', 'text': 'Producer = making/providing things (like laws, police services). Consumer = buying/using things (like buying office supplies or building materials).'}
            ],
            'guidelines': ['Clearly separate the explanation into one point for producer and one point for consumer.']
        }, subskill='discussion', learning_objective_id='lo_gov_roles', question_family_id='gov_roles_essay', concept_id='gov_producer_consumer', concept_group='government', misconception_tags=['confuses_producer_consumer'], diagnostic_tags=['essay', 'government']),
        
        _with_metadata({
            'title': 'Standard of Living',
            'prompt': f"Analyse the link between a person's lifestyle and their standard of living, using {scenario['entrepreneur']} as an example. (4 marks)",
            'marks': 4,
            'marking_points': [
                "Defines standard of living (access to goods/services making life comfortable).",
                "Defines lifestyle (how a person lives, spends money, expresses culture).",
                "Explains the link: Standard of living affects lifestyle choices.",
                "Provides an example (e.g., low standard of living limits health and education choices)."
            ],
            'sample_answer': f"Standard of living is a person's access to goods and services that make life comfortable, while lifestyle is the way a person lives and expresses their culture. The two are linked because standard of living affects lifestyle. If {scenario['entrepreneur']} has a low standard of living, their lifestyle choices are limited because they cannot afford proper healthcare or education, forcing them to live differently than someone with high wealth.",
            'difficulties': ['medium', 'hard'],
            'hint_sections': [
                {'title': 'What is being tested?', 'text': 'Connecting the concepts of standard of living and lifestyle.'},
                {'title': 'Nudge', 'text': 'How does having more money (standard of living) change the way you live your daily life (lifestyle)?'},
                {'title': 'Breakdown', 'text': 'First define both terms. Then explain how one limits or expands the other.'}
            ],
            'guidelines': ['Define both terms and explicitly state how they influence each other.']
        }, subskill='discussion', learning_objective_id='lo_lifestyle_standard', question_family_id='lifestyle_essay', concept_id='standard_vs_lifestyle', concept_group='standard_of_living', misconception_tags=['confuses_standard_and_lifestyle'], diagnostic_tags=['essay', 'societies'])
    ]

def generate(seed=None, difficulty=None, mode='scaffold', **kwargs):
    rng = _rng(seed)
    
    pools = [
        _concept_pool(rng),
        _discussion_pool(rng)
    ]
    
    selected_pool = rng.choice(pools)
    
    if difficulty:
        filtered = [q for q in selected_pool if difficulty in q['difficulty_band']]
        if filtered:
            selected_pool = filtered
            
    raw_item = rng.choice(selected_pool)
    
    if raw_item['question_type'] == 'mcq':
        return _mcq_question(rng, raw_item, mode)
    else:
        return _typed_question(rng, raw_item, mode)
