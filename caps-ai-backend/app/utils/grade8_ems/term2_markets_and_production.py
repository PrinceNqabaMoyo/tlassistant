import random
from app.utils.ems_namelist import get_ems_scenario

def _rng(seed=None):
    return random.Random(seed)

TOPIC_ID = 'grade8_ems'
SUBTOPIC_ID = 'term2_markets_and_production'
CURRICULUM_REFERENCE = 'Term 2 > Factors of Production and The Markets'

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
            'title': 'Factors of Production',
            'prompt': f"{scenario['entrepreneur']} hires a manager to run their business in {scenario['area']}. The manager is an example of which factor of production?",
            'options': [
                "Capital", 
                "Land", 
                "Labour", 
                "Entrepreneurship"
            ],
            'correct_index': 2,
            'explanation': "The manager provides physical or mental effort (work) to the business in exchange for a salary, which makes them part of the Labour factor of production.",
            'difficulties': ['easy', 'medium'],
            'marks': 1,
            'hint_sections': {
                '1_nudge': 'Which factor of production relates to people working for the business?',
                '2_concept': 'Land is natural resources, Capital is money/machinery. Entrepreneurship is the owner taking the risk.',
                '3_breakdown': 'Since the manager is hired to do work for a salary, they provide human effort, known as Labour.'
            },
            'guidelines': ['Identify the factor of production that represents human workers.']
        }, subskill='concepts', learning_objective_id='lo_factors', question_family_id='factors_classification', concept_id='labour', concept_group='factors_of_production', misconception_tags=['confuses_labour_with_entrepreneurship'], diagnostic_tags=['classification', 'production']),
        
        _with_metadata({
            'title': 'The Factor Market',
            'prompt': "In which market do households sell their labour, land, or capital to businesses?",
            'options': [
                "The goods and services market", 
                "The factor market", 
                "The financial market", 
                "The international market"
            ],
            'correct_index': 1,
            'explanation': "The factor market is where the factors of production (such as labour, land, and capital) are bought and sold. Households provide these factors to businesses in this market.",
            'difficulties': ['easy', 'medium'],
            'marks': 1,
            'hint_sections': {
                '1_nudge': 'Look at what is being sold: labour, land, and capital. What are these collectively called?',
                '2_concept': 'They are the "factors of production".',
                '3_breakdown': 'The market where factors of production are exchanged is called the factor market.'
            },
            'guidelines': ['Identify the market where production resources are exchanged.']
        }, subskill='concepts', learning_objective_id='lo_markets', question_family_id='market_classification', concept_id='factor_market', concept_group='markets', misconception_tags=['confuses_goods_and_factor_markets'], diagnostic_tags=['definition', 'markets']),
    ]

def _discussion_pool(rng):
    scenario = get_ems_scenario()
    
    return [
        _with_metadata({
            'title': 'Remuneration of Factors',
            'prompt': f"Name the four factors of production and state the remuneration (reward) that each factor receives. (8 marks)",
            'marks': 8,
            'marking_points': [
                "Land - Rent",
                "Labour - Salaries/Wages",
                "Capital - Interest",
                "Entrepreneurship - Profit"
            ],
            'sample_answer': "1. Land receives Rent.\n2. Labour receives Salaries or Wages.\n3. Capital receives Interest.\n4. Entrepreneurship receives Profit.",
            'difficulties': ['medium', 'hard'],
            'hint_sections': {
                '1_nudge': 'Think about what a business pays for using natural resources, workers, borrowed money, and the owner\'s risk.',
                '2_concept': 'Workers get wages. What do you pay for using a building (Land)? Rent. What does the bank charge for a loan (Capital)? Interest.',
                '3_breakdown': 'The four factors are Land (Rent), Labour (Wages), Capital (Interest), and Entrepreneurship (Profit).'
            },
            'guidelines': ['List all four factors of production and correctly match each to its remuneration.'],
            'teaching_note': 'A common mistake is assigning "salary" to entrepreneurship. Emphasize that the specific reward for taking a business risk is Profit.'
        }, subskill='discussion', learning_objective_id='lo_remuneration', question_family_id='factors_remuneration', concept_id='remuneration', concept_group='factors_of_production', misconception_tags=['confuses_profit_with_salary'], diagnostic_tags=['listing', 'production'])
    ]

def generate(subskill="concepts", difficulty="medium", count=1, mode="scaffold", seed=None, **kwargs):
    rng = _rng(seed)
    
    if subskill == "discussion":
        pool = _discussion_pool(rng)
    else:
        pool = _concept_pool(rng)
        
    selected = [q for q in pool if difficulty in q['difficulty_band']]
    if not selected: selected = pool
    chosen = rng.sample(selected, min(count, len(selected)))
    
    if subskill == "discussion":
        return [_typed_question(rng, item, mode=mode) for item in chosen]
    else:
        return [_mcq_question(rng, item, mode=mode) for item in chosen]
