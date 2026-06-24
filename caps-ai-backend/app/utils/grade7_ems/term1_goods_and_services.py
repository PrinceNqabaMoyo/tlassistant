import random
from app.utils.ems_namelist import get_ems_scenario, NAMES, AREAS

def _rng(seed=None):
    return random.Random(seed)

TOPIC_ID = 'grade7_ems'
SUBTOPIC_ID = 'term1_goods_and_services'
CURRICULUM_REFERENCE = 'Term 1 > Goods and Services'

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
    return [
        _with_metadata({
            'title': 'Goods vs Services',
            'prompt': "Which of the following is an example of a SERVICE rather than a good?",
            'options': ["A loaf of bread", "A haircut at a salon", "A pair of shoes", "A mobile phone"],
            'correct_index': 1,
            'explanation': "A haircut is a service because it is an intangible act that satisfies a need. Goods are physical items you can touch and own.",
            'difficulties': ['easy', 'medium'],
            'marks': 2,
            'hint_sections': [
                {'title': 'What is being tested?', 'text': 'Differentiating between tangible goods and intangible services.'},
                {'title': 'Reasoning path', 'text': 'Ask: Can I hold this in my hand and take it home? If yes, it is a good. If no, it is a service.'}
            ],
            'guidelines': ['Identify the intangible activity.']
        }, subskill='concepts', learning_objective_id='lo_goods_vs_services', question_family_id='goods_services_classification', concept_id='goods_vs_services', concept_group='goods_and_services'),
        
        _with_metadata({
            'title': 'Producer vs Consumer',
            'prompt': "A farmer grows wheat and sells it to a bakery. In this example, the farmer is the ______ and the bakery is the ______.",
            'options': ["consumer; producer", "producer; consumer", "retailer; wholesaler", "worker; employer"],
            'correct_index': 1,
            'explanation': "The farmer produces the wheat, making them the producer. The bakery buys (consumes) the wheat as a raw material, making them the consumer in this transaction.",
            'difficulties': ['easy', 'medium'],
            'marks': 2,
            'hint_sections': [
                {'title': 'What is being tested?', 'text': 'Identifying producers and consumers in a transaction.'},
                {'title': 'Reasoning path', 'text': 'The producer makes or grows the product. The consumer buys or uses it.'}
            ],
            'guidelines': ['Match the role to the participant.']
        }, subskill='concepts', learning_objective_id='lo_producer_consumer', question_family_id='producer_consumer_roles', concept_id='producer_consumer', concept_group='goods_and_services'),
        
        _with_metadata({
            'title': 'Recycling Benefit',
            'prompt': "Why is it important for businesses and households to recycle goods?",
            'options': ["To make products more expensive", "To reduce waste and protect the environment", "To increase the use of raw materials", "To create more pollution"],
            'correct_index': 1,
            'explanation': "Recycling reduces waste, conserves natural resources, and helps protect the environment for future generations.",
            'difficulties': ['easy', 'medium'],
            'marks': 2,
            'hint_sections': [
                {'title': 'What is being tested?', 'text': 'Understanding the purpose of recycling in the economy.'},
                {'title': 'Reasoning path', 'text': 'Think about what happens to waste that is not recycled versus waste that is reused.'}
            ],
            'guidelines': ['Select the option that mentions environmental benefit.']
        }, subskill='concepts', learning_objective_id='lo_recycling', question_family_id='recycling_benefits', concept_id='recycling', concept_group='goods_and_services'),
        
        _with_metadata({
            'title': 'Tertiary Sector Example',
            'prompt': "Which of the following businesses operates in the tertiary (service) sector?",
            'options': ["A coal mine", "A car factory", "A bank", "A forestry company"],
            'correct_index': 2,
            'explanation': "A bank provides financial services, placing it in the tertiary sector. Mining and forestry are primary sector, and a car factory is secondary sector.",
            'difficulties': ['medium', 'hard'],
            'marks': 2,
            'hint_sections': [
                {'title': 'What is being tested?', 'text': 'Identifying the three economic sectors.'},
                {'title': 'Reasoning path', 'text': 'Primary = raw materials, Secondary = manufacturing, Tertiary = services.'}
            ],
            'guidelines': ['Match the business to the correct sector.']
        }, subskill='concepts', learning_objective_id='lo_economic_sectors', question_family_id='sector_classification', concept_id='tertiary_sector', concept_group='goods_and_services'),
    ]

def _discussion_pool(rng):
    return [
        _with_metadata({
            'title': 'Household Roles',
            'prompt': "Explain how a household can act as both a producer and a consumer. Provide an example for each role. (4 marks)",
            'marks': 4,
            'marking_points': [
                "Households are consumers when they buy goods and services.",
                "Example of buying groceries or paying for electricity.",
                "Households are producers when members work to earn income.",
                "Example of a parent working as a teacher or a child helping with chores."
            ],
            'sample_answer': "A household acts as a consumer when it buys goods like groceries and services like electricity. It acts as a producer when household members offer their labour to earn an income, such as a parent working as a teacher.",
            'difficulties': ['medium', 'hard'],
            'hint_sections': [
                {'title': 'What is being tested?', 'text': 'Understanding dual roles of households in the economy.'},
                {'title': 'Reasoning path', 'text': 'Think about what your family buys versus what your family does to earn money.'}
            ],
            'guidelines': ['Require one example for consumer role and one for producer role.']
        }, subskill='discussion', learning_objective_id='lo_household_roles', question_family_id='household_roles_essay', concept_id='household_dual_role', concept_group='goods_and_services'),
        
        _with_metadata({
            'title': 'Recycling Discussion',
            'prompt': "Discuss two ways in which recycling and reusing goods can help satisfy the needs and wants of people in South Africa. (4 marks)",
            'marks': 4,
            'marking_points': [
                "Recycling reduces waste, keeping the environment clean.",
                "Reusing goods saves money, allowing people to spend on other needs.",
                "Recycling creates jobs in the recycling industry.",
                "It conserves natural resources for future generations."
            ],
            'sample_answer': "Recycling reduces waste and keeps the environment clean, which protects public health. Reusing goods also saves money, allowing households to spend their limited income on other important needs. Additionally, recycling creates job opportunities.",
            'difficulties': ['medium'],
            'hint_sections': [
                {'title': 'What is being tested?', 'text': 'Linking recycling to economic and environmental benefits.'},
                {'title': 'Reasoning path', 'text': 'Consider both environmental benefits and economic benefits of recycling.'}
            ],
            'guidelines': ['Accept any two valid points with brief explanation.']
        }, subskill='discussion', learning_objective_id='lo_recycling_discussion', question_family_id='recycling_discussion', concept_id='recycling_benefits', concept_group='goods_and_services'),
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
