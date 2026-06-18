import random
from app.utils.ems_namelist import get_ems_scenario

def _rng(seed=None):
    return random.Random(seed)

TOPIC_ID = 'grade8_ems'
SUBTOPIC_ID = 'term3_ownership'
CURRICULUM_REFERENCE = 'Term 3 > Forms of Ownership'

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
            'title': 'Unlimited Liability',
            'prompt': f"{scenario['entrepreneur']} owns a business as a sole trader. If the business goes bankrupt and cannot pay its debts, what will happen to {scenario['entrepreneur']}'s personal assets?",
            'options': [
                "They are fully protected by law.", 
                "They may be seized and sold to pay off the business's debts.", 
                "Only the business's assets can be sold to pay the debt.", 
                "The government will pay off the debts on their behalf."
            ],
            'correct_index': 1,
            'explanation': "A sole trader has unlimited liability. This means there is no legal separation between the owner and the business, so the owner's personal assets are at risk to cover business debts.",
            'difficulties': ['easy', 'medium'],
            'marks': 2,
            'hint_sections': {
                '1_nudge': 'Think about the term "unlimited liability". What does "unlimited" mean for the owner\'s personal belongings?',
                '2_concept': 'In a sole trader, the owner and the business are considered the same legal entity.',
                '3_breakdown': 'Because they are the same legal entity, the owner is personally responsible for all debts of the business.'
            },
            'guidelines': ['Identify the meaning and consequence of unlimited liability.']
        }, subskill='concepts', learning_objective_id='lo_unlimited_liability', question_family_id='liability_classification', concept_id='unlimited_liability', concept_group='ownership', misconception_tags=['confuses_limited_with_unlimited'], diagnostic_tags=['classification', 'ownership']),
        
        _with_metadata({
            'title': 'Partnerships',
            'prompt': "Which form of ownership requires a minimum of two people and a maximum of twenty people who share the risks and profits?",
            'options': [
                "Sole trader", 
                "Partnership", 
                "Private Company", 
                "Public Company"
            ],
            'correct_index': 1,
            'explanation': "A partnership is formed by 2 to 20 people who pool their resources together and share the profits and risks.",
            'difficulties': ['easy'],
            'marks': 1,
            'hint_sections': {
                '1_nudge': 'Which form of ownership is defined by "partners" working together?',
                '2_concept': 'Sole trader is one person. Companies can have many shareholders.',
                '3_breakdown': 'A partnership specifically has between 2 and 20 owners (partners).'
            },
            'guidelines': ['Identify the ownership form based on the number of owners.']
        }, subskill='concepts', learning_objective_id='lo_partnership', question_family_id='partnership_definition', concept_id='partnership', concept_group='ownership', misconception_tags=['confuses_partnership_and_company'], diagnostic_tags=['definition', 'ownership']),
    ]

def _discussion_pool(rng):
    scenario = get_ems_scenario()
    
    return [
        _with_metadata({
            'title': 'Sole Trader Advantages',
            'prompt': f"{scenario['entrepreneur']} wants to start a small {scenario['business_type']} business in {scenario['area']}. Explain two advantages of starting this business as a sole trader. (4 marks)",
            'marks': 4,
            'marking_points': [
                "It is easy and cheap to establish (very few legal requirements).",
                "The owner makes all the decisions quickly without needing to consult others.",
                "The owner keeps all the profits.",
                "Personal contact with customers is easier."
            ],
            'sample_answer': "One advantage is that the owner receives all the profits generated by the business. A second advantage is that decision-making is very fast because the owner does not have to consult with any partners or shareholders.",
            'difficulties': ['medium', 'hard'],
            'hint_sections': {
                '1_nudge': 'Think about what is great about being the only boss of a business.',
                '2_concept': 'If you are the only owner, what happens to the money made? Who do you have to ask before making a change?',
                '3_breakdown': 'You keep 100% of the profits and you can make decisions immediately.'
            },
            'guidelines': ['Provide two distinct advantages of the sole trader form of ownership.'],
            'teaching_note': 'Ensure learners do not mention limited liability, as sole traders have unlimited liability.'
        }, subskill='discussion', learning_objective_id='lo_sole_trader_advantages', question_family_id='sole_trader_essay', concept_id='sole_trader', concept_group='ownership', misconception_tags=['confuses_advantages_of_ownership'], diagnostic_tags=['essay', 'ownership'])
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
