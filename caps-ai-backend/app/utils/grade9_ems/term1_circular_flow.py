import random
from app.utils.ems_namelist import get_ems_scenario, NAMES, AREAS

def _rng(seed=None):
    return random.Random(seed)

TOPIC_ID = 'grade9_ems'
SUBTOPIC_ID = 'term1_circular_flow'
CURRICULUM_REFERENCE = 'Term 1 > The Circular Flow'

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
        'id': f"g9_ems_mcq_{rng.randint(1000, 999999)}",
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
        'id': f"g9_ems_typed_{rng.randint(1000, 999999)}",
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
            'title': 'Circular Flow Participants',
            'prompt': "In the circular flow model of a closed economy, which THREE main participants are involved?",
            'options': ["Households, businesses, and the government", "Households, businesses, and foreign countries", "Banks, businesses, and the government", "Households, banks, and suppliers"],
            'correct_index': 0,
            'explanation': "The circular flow of a closed economy involves three main participants: households, businesses, and the government. Households provide factors of production to businesses and receive income. They also pay taxes to the government and receive transfers.",
            'difficulties': ['easy', 'medium'],
            'marks': 2,
            'hint_sections': [
                {'title': 'What is being tested?', 'text': 'Identifying the main participants in the circular flow model.'},
                {'title': 'Reasoning path', 'text': 'Think about who buys goods, who makes goods, and who regulates the economy.'}
            ],
            'guidelines': ['Select the option with households, businesses, and government.']
        }, subskill='concepts', learning_objective_id='lo_circular_flow_participants', question_family_id='circular_flow_participants', concept_id='circular_flow_participants', concept_group='circular_flow'),
        
        _with_metadata({
            'title': 'Flow of Money and Goods',
            'prompt': "In the circular flow model, households supply factors of production (like labour) to businesses. In exchange, businesses supply ______ to households.",
            'options': ["taxes", "goods and services", "source documents", "shares"],
            'correct_index': 1,
            'explanation': "Businesses supply goods and services to households in exchange for the factors of production. This is the real flow of goods and services from businesses to households.",
            'difficulties': ['easy', 'medium'],
            'marks': 2,
            'hint_sections': [
                {'title': 'What is being tested?', 'text': 'Understanding the real flow in the circular flow model.'},
                {'title': 'Reasoning path', 'text': 'If households give labour to businesses, what do businesses give back?'}
            ],
            'guidelines': ['Select the option about goods and services.']
        }, subskill='concepts', learning_objective_id='lo_real_flow', question_family_id='real_flow_mcq', concept_id='real_flow', concept_group='circular_flow'),
        
        _with_metadata({
            'title': 'Government Role',
            'prompt': "In the circular flow model, the government collects taxes from both households and businesses. What does the government provide in return?",
            'options': ["Shares and dividends", "Public goods and services (e.g., roads, education, healthcare)", "Raw materials for factories", "Private loans"],
            'correct_index': 1,
            'explanation': "The government provides public goods and services such as roads, education, healthcare, and defence. These services are funded by the taxes collected from households and businesses.",
            'difficulties': ['medium'],
            'marks': 2,
            'hint_sections': [
                {'title': 'What is being tested?', 'text': 'Understanding the role of government in the circular flow.'},
                {'title': 'Reasoning path', 'text': 'Think about what the government spends tax money on that benefits everyone.'}
            ],
            'guidelines': ['Select the option about public goods and services.']
        }, subskill='concepts', learning_objective_id='lo_government_role', question_family_id='government_role_mcq', concept_id='government_role', concept_group='circular_flow'),
        
        _with_metadata({
            'title': 'Factor Market vs Goods Market',
            'prompt': "The market where households SELL labour to businesses is called the:",
            'options': ["goods and services market", "factor market", "financial market", "foreign exchange market"],
            'correct_index': 1,
            'explanation': "The factor market is where factors of production (labour, land, capital) are bought and sold. Households sell their labour to businesses in the factor market.",
            'difficulties': ['medium', 'hard'],
            'marks': 2,
            'hint_sections': [
                {'title': 'What is being tested?', 'text': 'Distinguishing between the factor market and the goods market.'},
                {'title': 'Reasoning path', 'text': 'Factor market = factors of production (labour, land, capital). Goods market = finished products and services.'}
            ],
            'guidelines': ['Select the factor market.']
        }, subskill='concepts', learning_objective_id='lo_factor_market', question_family_id='factor_market_mcq', concept_id='factor_market', concept_group='circular_flow'),
    ]

def _discussion_pool(rng):
    return [
        _with_metadata({
            'title': 'Circular Flow Description',
            'prompt': "Describe the circular flow model of a closed economy. In your answer, explain the flow of goods, services, money, and factors of production between households, businesses, and the government. (6 marks)",
            'marks': 6,
            'marking_points': [
                "Households own factors of production (labour, land, capital).",
                "Households sell factors of production to businesses in the factor market.",
                "Businesses use these factors to produce goods and services.",
                "Businesses sell goods and services to households in the goods market.",
                "Money flows from businesses to households as income (wages, rent, profit).",
                "Money flows from households to businesses as payment for goods and services.",
                "The government collects taxes and provides public goods and services."
            ],
            'sample_answer': "In the circular flow model, households own factors of production such as labour, land, and capital. They sell these factors to businesses in the factor market and receive income (wages, rent, and profit) in return. Businesses use these factors to produce goods and services, which they sell to households in the goods market. Households pay money to businesses for these goods and services. The government is also involved: it collects taxes from both households and businesses and uses the revenue to provide public goods and services like roads, education, and healthcare.",
            'difficulties': ['medium', 'hard'],
            'hint_sections': [
                {'title': 'What is being tested?', 'text': 'Comprehensive understanding of the circular flow model.'},
                {'title': 'Reasoning path', 'text': 'Start with households, then trace the flow to businesses, then add the government. Mention both the real flow (goods/services/factors) and the money flow.'}
            ],
            'guidelines': ['Award marks for each valid point with clear explanation.']
        }, subskill='discussion', learning_objective_id='lo_circular_flow_description', question_family_id='circular_flow_essay', concept_id='circular_flow_model', concept_group='circular_flow'),
        
        _with_metadata({
            'title': 'Interdependence',
            'prompt': "Explain why households, businesses, and the government are interdependent in the circular flow model. Provide an example. (4 marks)",
            'marks': 4,
            'marking_points': [
                "Households need businesses to provide goods and services and jobs.",
                "Businesses need households to supply labour and buy their products.",
                "The government needs tax revenue from both to provide public services.",
                "All three depend on each other for the economy to function."
            ],
            'sample_answer': "Households, businesses, and the government are interdependent because each group needs the others to function. Households need businesses to provide jobs and goods, while businesses need households to supply labour and purchase their products. The government needs tax revenue from both households and businesses to fund public services like education and infrastructure. If one group fails, the entire flow is disrupted.",
            'difficulties': ['medium'],
            'hint_sections': [
                {'title': 'What is being tested?', 'text': 'Understanding interdependence in the circular flow.'},
                {'title': 'Reasoning path', 'text': 'Think about what happens to businesses if no households buy their products, or to households if no businesses offer jobs.'}
            ],
            'guidelines': ['Require explanation of interdependence with a valid example.']
        }, subskill='discussion', learning_objective_id='lo_interdependence', question_family_id='interdependence_essay', concept_id='interdependence', concept_group='circular_flow'),
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
