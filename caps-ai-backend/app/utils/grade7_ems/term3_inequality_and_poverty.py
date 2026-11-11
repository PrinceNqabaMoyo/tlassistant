import random
from app.utils.ems_namelist import get_ems_scenario, NAMES, AREAS

def _rng(seed=None):
    return random.Random(seed)

TOPIC_ID = 'grade7_ems'
SUBTOPIC_ID = 'term3_inequality_and_poverty'
CURRICULUM_REFERENCE = 'Term 3 > Inequality and Poverty'

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
    scenario = get_ems_scenario(rng)
    return [
        _with_metadata({
            'title': 'Causes of Poverty',
            'prompt': f"Studying economic challenges in {scenario['area']}, which of the following is a major cause of poverty in South Africa?",
            'options': ["High levels of education for all citizens", "Lack of job opportunities and skills", "Equal distribution of wealth", "Too many businesses operating"],
            'correct_index': 1,
            'explanation': "Lack of job opportunities and skills is a major cause of poverty. When people cannot find work or lack the skills employers need, they struggle to earn an income.",
            'difficulties': ['easy', 'medium'],
            'marks': 2,
            'hint_sections': [
                {'title': 'What is being tested?', 'text': 'Identifying causes of poverty and inequality.'},
                {'title': 'Reasoning path', 'text': 'Think about what prevents people from earning enough money to meet their needs.'}
            ],
            'guidelines': ['Select the option that describes a barrier to earning income.']
        }, subskill='concepts', learning_objective_id='lo_poverty_causes', question_family_id='poverty_causes_mcq', concept_id='poverty_causes', concept_group='inequality_and_poverty'),
        
        _with_metadata({
            'title': 'Service Delivery',
            'prompt': f"Poor municipal service delivery in a community like {scenario['area']} often leads to:",
            'options': ["Improved health for residents", "Better education outcomes", "Increased inequality and frustration", "Higher employment rates"],
            'correct_index': 2,
            'explanation': "When basic services like water, electricity, and sanitation are not delivered properly, it increases inequality and causes frustration among community members.",
            'difficulties': ['easy', 'medium'],
            'marks': 2,
            'hint_sections': [
                {'title': 'What is being tested?', 'text': 'Understanding the link between service delivery and inequality.'},
                {'title': 'Reasoning path', 'text': 'If some communities receive services and others do not, what happens to the gap between them?'}
            ],
            'guidelines': ['Look for the negative consequence of poor service delivery.']
        }, subskill='concepts', learning_objective_id='lo_service_delivery', question_family_id='service_delivery_mcq', concept_id='service_delivery', concept_group='inequality_and_poverty'),
        
        _with_metadata({
            'title': 'Skills and Education',
            'prompt': f"In communities like {scenario['area']}, how can quality education help fight inequality and poverty?",
            'options': ["By keeping children out of work", "By giving people knowledge and skills to find better jobs", "By making people dependent on government", "By reducing the number of schools"],
            'correct_index': 1,
            'explanation': "Education equips people with knowledge and skills, making them more employable and able to earn higher incomes, which helps reduce poverty.",
            'difficulties': ['easy', 'medium'],
            'marks': 2,
            'hint_sections': [
                {'title': 'What is being tested?', 'text': 'Understanding education as a tool against poverty.'},
                {'title': 'Reasoning path', 'text': 'Think about how learning new skills changes a person\'s ability to earn money.'}
            ],
            'guidelines': ['Select the option that links education to employability.']
        }, subskill='concepts', learning_objective_id='lo_education_poverty', question_family_id='education_poverty_mcq', concept_id='education_skills', concept_group='inequality_and_poverty'),
        
        _with_metadata({
            'title': 'Urban vs Rural Challenges',
            'prompt': f"Comparing {scenario['area']} to outlying rural communities, rural areas in South Africa often face more challenges because:",
            'options': ["They have better access to hospitals", "They have more job opportunities", "They often lack infrastructure like roads and clinics", "They receive more government funding"],
            'correct_index': 2,
            'explanation': "Rural areas often lack infrastructure such as good roads, clinics, and schools, which makes it harder for people to access services and opportunities.",
            'difficulties': ['medium', 'hard'],
            'marks': 2,
            'hint_sections': [
                {'title': 'What is being tested?', 'text': 'Comparing urban and rural challenges.'},
                {'title': 'Reasoning path', 'text': 'Think about what facilities and services are easier to find in cities compared to remote rural areas.'}
            ],
            'guidelines': ['Select the option that describes a lack of facilities.']
        }, subskill='concepts', learning_objective_id='lo_urban_rural', question_family_id='urban_rural_mcq', concept_id='urban_rural_challenges', concept_group='inequality_and_poverty'),
    ]

def _discussion_pool(rng):
    scenario = get_ems_scenario(rng)
    return [
        _with_metadata({
            'title': 'Fighting Inequality',
            'prompt': f"Examining unemployment in {scenario['area']}, discuss two ways in which the government and businesses can create sustainable job opportunities to reduce poverty in South Africa. (4 marks)",
            'marks': 4,
            'marking_points': [
                "Investing in infrastructure creates construction jobs.",
                "Supporting small businesses through funding and training.",
                "Improving education so people have better skills.",
                "Promoting tourism and local industries."
            ],
            'sample_answer': "The government can invest in infrastructure projects like building roads and clinics, which creates jobs for local workers. It can also support small businesses by providing funding and training, helping entrepreneurs create employment in their communities.",
            'difficulties': ['medium', 'hard'],
            'hint_sections': [
                {'title': 'What is being tested?', 'text': 'Understanding government strategies to reduce poverty.'},
                {'title': 'Reasoning path', 'text': 'Think about what the government spends money on and how that creates work for people.'}
            ],
            'guidelines': ['Accept any two valid strategies with brief explanation.']
        }, subskill='discussion', learning_objective_id='lo_job_creation', question_family_id='job_creation_essay', concept_id='sustainable_jobs', concept_group='inequality_and_poverty'),
        
        _with_metadata({
            'title': 'Education and Inequality',
            'prompt': f"In communities like {scenario['area']}, explain how improving education and skills can help fight inequality and injustice in South Africa. Provide an example. (4 marks)",
            'marks': 4,
            'marking_points': [
                "Education provides knowledge and skills for better-paying jobs.",
                "Skilled workers can contribute more to the economy.",
                "Education helps people understand their rights.",
                "Example of a learner studying to become a professional."
            ],
            'sample_answer': "Improving education gives people the skills they need to find better-paying jobs, which raises their standard of living. For example, a learner who studies nursing can work in a hospital, earn a stable income, and help their family escape poverty.",
            'difficulties': ['medium'],
            'hint_sections': [
                {'title': 'What is being tested?', 'text': 'Linking education to reduced inequality.'},
                {'title': 'Reasoning path', 'text': 'Think about what changes when a person goes from unskilled to skilled work.'}
            ],
            'guidelines': ['Require explanation and a valid example.']
        }, subskill='discussion', learning_objective_id='lo_education_inequality', question_family_id='education_inequality_essay', concept_id='education_justice', concept_group='inequality_and_poverty'),
    ]



SUBSKILLS = ['poverty_causes_mcq', 'service_delivery_mcq', 'education_poverty_mcq', 'urban_rural_mcq', 'job_creation_essay', 'education_inequality_essay']



SUBSKILLS = ['poverty_causes_mcq', 'service_delivery_mcq', 'education_poverty_mcq', 'urban_rural_mcq', 'job_creation_essay', 'education_inequality_essay']

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
