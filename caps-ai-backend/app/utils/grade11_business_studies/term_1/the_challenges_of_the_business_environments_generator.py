import random

from ..names import MANUFACTURING_SUFFIXES
from ..names import RETAIL_AND_LIFESTYLE_SUFFIXES
from ..names import pick_business_name as _pick_business_name


def _rng(seed=None):
    return random.Random(seed)


def _select_items(rng, pool, count, difficulty):
    filtered = [item for item in pool if difficulty in item.get('difficulties', ['easy', 'medium', 'hard'])]
    working = filtered or pool
    if not working:
        return []
    if count <= len(working):
        return rng.sample(working, count)
    result = working[:]
    rng.shuffle(result)
    while len(result) < count:
        result.append(rng.choice(working))
    return result[:count]


TOPIC_ID = 'grade11_business_studies'
SUBTOPIC_ID = 'challenges_of_the_business_environments'
CURRICULUM_REFERENCE = 'Term 1 > The challenges of the business environments'


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
        'difficulty_band': item.get('difficulty_band', item.get('difficulties', ['easy', 'medium', 'hard'])),
        'curriculum_reference': curriculum_reference,
        'misconception_tags': misconception_tags or [],
        'diagnostic_tags': diagnostic_tags or [],
        'answer_structure_tags': answer_structure_tags or [],
    })
    if minimum_mastery_score is not None:
        enriched['minimum_mastery_score'] = minimum_mastery_score
    return enriched


FILTERABLE_METADATA_KEYS = (
    'learning_objective_id',
    'concept_id',
    'concept_group',
    'question_family_id',
    'scenario_family_id',
)


def _matches_metadata(item, filters):
    for key, value in filters.items():
        if value is None:
            continue
        if item.get(key) != value:
            return False
    return True


def _apply_metadata_filters(pool, **kwargs):
    base_filters = {
        key: kwargs.get(key)
        for key in FILTERABLE_METADATA_KEYS
        if kwargs.get(key) is not None
    }
    retry_variant = kwargs.get('retry_variant')

    if not base_filters and retry_variant is None:
        return pool

    exact_filters = dict(base_filters)
    if retry_variant is not None:
        exact_filters['retry_variant'] = retry_variant

    exact_matches = [item for item in pool if _matches_metadata(item, exact_filters)]
    if exact_matches:
        return exact_matches

    family_line_matches = [item for item in pool if _matches_metadata(item, base_filters)]
    if family_line_matches:
        return family_line_matches

    broadened_filters = {
        key: value
        for key, value in base_filters.items()
        if key in ('learning_objective_id', 'concept_id', 'concept_group')
    }
    if retry_variant is not None and broadened_filters:
        broadened_variant_matches = [
            item for item in pool if _matches_metadata(item, {**broadened_filters, 'retry_variant': retry_variant})
        ]
        if broadened_variant_matches:
            return broadened_variant_matches

    if broadened_filters:
        broadened_matches = [item for item in pool if _matches_metadata(item, broadened_filters)]
        if broadened_matches:
            return broadened_matches

    return pool


def _mcq_question(rng, item):
    correct_option = item['options'][item['correct_index']]
    return {
        'id': f"g11_bs_challenges_mcq_{rng.randint(1000, 999999)}",
        'title': item.get('title', 'Concept check'),
        'question_type': 'mcq',
        'prompt': item['prompt'],
        'options': item['options'],
        'correct_index': str(item['correct_index']),
        'explanation': item['explanation'],
        'marks': 1,
        'hint_sections': item.get('hint_sections', []),
        'guidelines': item.get('guidelines', []),
        'sample_answer': correct_option,
        'ideal_answer': correct_option,
        'marking_points': [correct_option],
        'teaching_note': item.get('teaching_note', item['explanation']),
        'topic_id': item.get('topic_id'),
        'subtopic_id': item.get('subtopic_id'),
        'subskill': item.get('subskill'),
        'learning_objective_id': item.get('learning_objective_id'),
        'concept_id': item.get('concept_id'),
        'concept_group': item.get('concept_group'),
        'question_family_id': item.get('question_family_id'),
        'scenario_family_id': item.get('scenario_family_id'),
        'retry_variant': item.get('retry_variant', 'core'),
        'difficulty_band': item.get('difficulty_band', item.get('difficulties', ['easy', 'medium', 'hard'])),
        'curriculum_reference': item.get('curriculum_reference', CURRICULUM_REFERENCE),
        'misconception_tags': item.get('misconception_tags', []),
        'diagnostic_tags': item.get('diagnostic_tags', []),
        'answer_structure_tags': item.get('answer_structure_tags', []),
        'minimum_mastery_score': item.get('minimum_mastery_score', 1.0),
    }


def _typed_question(rng, item):
    return {
        'id': f"g11_bs_challenges_typed_{rng.randint(1000, 999999)}",
        'title': item.get('title', 'Written response'),
        'question_type': 'typed',
        'prompt': item['prompt'],
        'marks': item['marks'],
        'marking_points': item['marking_points'],
        'sample_answer': item['sample_answer'],
        'ideal_answer': item.get('ideal_answer', item['sample_answer']),
        'hint_sections': item.get('hint_sections', []),
        'answer_part_hints': item.get('answer_part_hints', []),
        'guidelines': item.get('guidelines', []),
        'teaching_note': item.get('teaching_note', ''),
        'keywords': item.get('keywords', []),
        'topic_id': item.get('topic_id'),
        'subtopic_id': item.get('subtopic_id'),
        'subskill': item.get('subskill'),
        'learning_objective_id': item.get('learning_objective_id'),
        'concept_id': item.get('concept_id'),
        'concept_group': item.get('concept_group'),
        'question_family_id': item.get('question_family_id'),
        'scenario_family_id': item.get('scenario_family_id'),
        'retry_variant': item.get('retry_variant', 'core'),
        'difficulty_band': item.get('difficulty_band', item.get('difficulties', ['easy', 'medium', 'hard'])),
        'curriculum_reference': item.get('curriculum_reference', CURRICULUM_REFERENCE),
        'misconception_tags': item.get('misconception_tags', []),
        'diagnostic_tags': item.get('diagnostic_tags', []),
        'answer_structure_tags': item.get('answer_structure_tags', []),
        'minimum_mastery_score': item.get('minimum_mastery_score', 0.6),
    }


def _concept_pool():
    return [
        _with_metadata({
            'title': 'Micro environment challenge',
            'prompt': 'High employee absenteeism is a challenge of the ... environment.',
            'options': ['micro', 'market', 'macro', 'global'],
            'correct_index': 0,
            'explanation': 'Employee absenteeism originates inside the business and therefore belongs to the micro environment.',
            'difficulties': ['easy', 'medium', 'hard'],
            'hint_sections': [
                {'title': 'What is being tested?', 'text': 'Classify a challenge according to the correct business environment.'},
                {'title': 'Reasoning path', 'text': 'Ask whether the challenge comes from inside the business, from close external stakeholders, or from broad external forces.'},
                {'title': 'Transfer idea', 'text': 'Problems with employees, managers, and internal goals usually belong to the micro environment.'}
            ],
            'guidelines': ['Focus on the source of the challenge, not only on its effect.']
        }, subskill='concepts', learning_objective_id='lo_challenges_of_micro_environment', question_family_id='micro_challenge_classification', concept_id='micro_environment_challenges', concept_group='challenge_classification', misconception_tags=['confuses_micro_and_market'], diagnostic_tags=['classification', 'micro']),
        _with_metadata({
            'title': 'Market environment challenge',
            'prompt': 'A business that struggles because suppliers deliver raw materials late is facing a challenge of the ... environment.',
            'options': ['micro', 'market', 'macro', 'internal'],
            'correct_index': 1,
            'explanation': 'Suppliers belong to the market environment, so late deliveries are a market challenge.',
            'difficulties': ['easy', 'medium', 'hard'],
            'hint_sections': [
                {'title': 'What is being tested?', 'text': 'Identify whether the challenge comes from the immediate external environment.'},
                {'title': 'Reasoning path', 'text': 'Suppliers, customers, competitors, and intermediaries usually form part of the market environment.'},
                {'title': 'Transfer idea', 'text': 'Shortage of suppliers and unreliable deliveries affect production and sales but are not fully inside the business.'}
            ],
            'guidelines': ['Link the challenge to the stakeholder causing it.']
        }, subskill='concepts', learning_objective_id='lo_challenges_of_market_environment', question_family_id='market_challenge_classification', concept_id='market_environment_challenges', concept_group='challenge_classification', misconception_tags=['treats_suppliers_as_internal'], diagnostic_tags=['classification', 'market']),
        _with_metadata({
            'title': 'Macro environment challenge',
            'prompt': 'Labour restrictions and changes in legislation are challenges of the ... environment.',
            'options': ['micro', 'market', 'macro', 'internal'],
            'correct_index': 2,
            'explanation': 'Legislation and labour restrictions come from the broad external environment and are therefore macro challenges.',
            'difficulties': ['easy', 'medium', 'hard'],
            'hint_sections': [
                {'title': 'What is being tested?', 'text': 'Recognise a broad external challenge beyond the control of the business.'},
                {'title': 'Reasoning path', 'text': 'When the challenge comes from laws, politics, the economy, or social conditions, it is usually macro.'},
                {'title': 'Transfer idea', 'text': 'Businesses cannot control labour laws or national legislation directly.'}
            ],
            'guidelines': ['Think about whether the challenge affects many businesses, not only one business.']
        }, subskill='concepts', learning_objective_id='lo_challenges_of_macro_environment', question_family_id='macro_challenge_classification', concept_id='macro_environment_challenges', concept_group='challenge_classification', misconception_tags=['confuses_market_and_macro'], diagnostic_tags=['classification', 'macro']),
        _with_metadata({
            'title': 'Consumer behaviour challenge',
            'prompt': 'When customer tastes and preferences change and sales fall, the business is dealing with ...',
            'options': ['changes in consumer behaviour', 'lack of vision and mission', 'micro-lending', 'strikes and go-slows'],
            'correct_index': 0,
            'explanation': 'Changing tastes and preferences are changes in consumer behaviour, which create a market-environment challenge.',
            'difficulties': ['easy', 'medium', 'hard'],
            'hint_sections': [
                {'title': 'What is being tested?', 'text': 'Identify a common market challenge from its description.'},
                {'title': 'Reasoning path', 'text': 'If the problem comes from customer tastes, preferences, or buying habits, think consumer behaviour.'},
                {'title': 'Transfer idea', 'text': 'Businesses often need to adapt products or marketing when consumer behaviour changes.'}
            ],
            'guidelines': ['Choose the challenge that matches the customer-focused description.']
        }, subskill='concepts', learning_objective_id='lo_challenges_of_market_environment', question_family_id='consumer_behaviour_identification', concept_id='consumer_behaviour_challenges', concept_group='market_challenges', misconception_tags=['confuses_customer_behaviour_with_internal_issues'], diagnostic_tags=['classification', 'market']),
        _with_metadata({
            'title': 'Competition response',
            'prompt': 'Which action is the best way for a business to overcome competition in the market?',
            'options': ['Ignore customer complaints', 'Differentiate goods or services', 'Wait for regulations to change', 'Reduce employee training'],
            'correct_index': 1,
            'explanation': 'Differentiating goods or services helps a business stand out and respond strategically to competition.',
            'difficulties': ['easy', 'medium', 'hard'],
            'hint_sections': [
                {'title': 'What is being tested?', 'text': 'Recognise a practical competition response from the curriculum notes.'},
                {'title': 'Reasoning path', 'text': 'The best response should make the business more attractive to customers or more competitive than rivals.'},
                {'title': 'Transfer idea', 'text': 'Competition can be addressed through differentiation, pricing, service quality, and marketing.'}
            ],
            'guidelines': ['Choose the option that improves the business position in the market.']
        }, subskill='concepts', learning_objective_id='lo_overcome_competition_in_market_environment', question_family_id='competition_response_reasoning', concept_id='competition_response_strategies', concept_group='adaptation_and_response', misconception_tags=['treats_competition_as_unavoidable_without_response'], diagnostic_tags=['strategy', 'competition']),
        _with_metadata({
            'title': 'Contemporary legislation example',
            'prompt': 'Which option is an example of contemporary legislation that may affect business operations?',
            'options': ['Consumer Protection Act', 'Mission statement', 'Organisational chart', 'Team-building session'],
            'correct_index': 0,
            'explanation': 'The Consumer Protection Act is a current law that affects business operations and consumer relations.',
            'difficulties': ['easy', 'medium', 'hard'],
            'hint_sections': [
                {'title': 'What is being tested?', 'text': 'Distinguish legislation from internal business tools or activities.'},
                {'title': 'Reasoning path', 'text': 'Acts, laws, and regulations belong to legislation.'},
                {'title': 'Transfer idea', 'text': 'Examples include the LRA, BCEA, COIDA, SDA, CPA, NCA, EEA, and BBBEE.'}
            ],
            'guidelines': ['Choose the option that names an actual law or Act.']
        }, subskill='concepts', learning_objective_id='lo_examples_of_contemporary_legislation', question_family_id='contemporary_legislation_example', concept_id='contemporary_legislation_examples', concept_group='macro_challenges', misconception_tags=['confuses_internal_documents_with_legislation'], diagnostic_tags=['classification', 'legislation']),
    ]


def _application_pool(rng):
    temba_case = _build_temba_context()
    steyn_case = _build_steyn_context()
    maureen_case = _build_maureen_context()
    competition_case = _build_competition_context(rng)
    return [
        _with_metadata({
            'title': 'Identify micro-environment challenges from statements',
            'prompt': f"Identify the challenges of the micro environment for {temba_case['business_name']} represented in EACH statement below. (8 marks)\n\n1. {temba_case['statement_1']}\n2. {temba_case['statement_2']}\n3. {temba_case['statement_3']}\n4. {temba_case['statement_4']}",
            'marks': 8,
            'marking_points': [
                'Difficult employees: the cleaner always complains about working hours and produces sub-standard work.',
                'Lack of vision and mission: management does not have a clear plan of where the business is going.',
                'Lack of adequate management skills: the sales team fails to meet targets because of a lack of leadership.',
                'Strikes or industrial action: employees are refusing to work until improved working conditions are met.'
            ],
            'sample_answer': 'The first statement shows difficult employees. The second shows a lack of vision and mission. The third shows a lack of adequate management skills. The fourth shows strikes or industrial action because employees are refusing to work until their demands are met.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': [
                {'title': 'What is being asked?', 'text': 'Name the micro-environment challenge shown in each statement.'},
                {'title': 'Reasoning path', 'text': 'Match each statement to the topic list: difficult employees, lack of vision and mission, poor management, and strikes or go-slows.'},
                {'title': 'Transfer idea', 'text': 'All four challenges come from inside the business and affect daily operations.'}
            ],
            'answer_part_hints': [
                'Name the challenge in statement 1.',
                'Name the challenge in statement 2.',
                'Name the challenge in statement 3.',
                'Name the challenge in statement 4.'
            ],
            'guidelines': ['Write the challenge names, not long explanations, unless the question specifically asks for discussion.'],
            'teaching_note': 'This item comes directly from the curriculum activity on micro-environment challenges.',
            'keywords': ['difficult employees', 'vision and mission', 'management skills', 'strikes', 'industrial action'],
        }, subskill='application', learning_objective_id='lo_challenges_of_micro_environment', question_family_id='micro_challenge_identification_from_statements', concept_id='micro_environment_challenges', concept_group='challenge_classification', scenario_family_id='temba_micro_challenges_case', retry_variant='core', diagnostic_tags=['scenario_analysis', 'micro_challenges'], answer_structure_tags=['identify', 'statement_match'], minimum_mastery_score=0.6),
        _with_metadata({
            'title': 'Challenge identification from scenario',
            'prompt': f"Read the scenario below and quote THREE challenges that {steyn_case['business_name']} has to deal with. (6 marks)\n\n{steyn_case['business_name']} employees are often late for work and do not want to work together. The business suffered losses due to its storeroom being broken into. Management is also struggling to find a reliable provider for raw materials.",
            'marks': 6,
            'marking_points': [
                'Employees are often late for work and do not want to work together.',
                'The business suffered losses due to its storeroom being broken into.',
                'Management is struggling to find a reliable provider for raw materials.'
            ],
            'sample_answer': 'The three challenges are that employees are often late for work and do not want to work together, the storeroom was broken into causing losses, and management is struggling to find a reliable provider for raw materials.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': [
                {'title': 'What is being asked?', 'text': 'Quote or identify the three challenge statements from the scenario.'},
                {'title': 'Reasoning path', 'text': 'Look for one internal people challenge, one wider external threat, and one supplier-related problem.'},
                {'title': 'Transfer idea', 'text': 'Challenge extraction comes before environment classification.'}
            ],
            'answer_part_hints': [
                'Quote the employee-related challenge.',
                'Quote the security or crime-related challenge.',
                'Quote the supplier-related challenge.'
            ],
            'guidelines': ['Stay close to the wording in the scenario when quoting challenges.'],
            'teaching_note': 'This follows the revision case on Steyn Manufacturers in the curriculum notes.',
            'keywords': ['late for work', 'do not work together', 'broken into', 'losses', 'reliable provider', 'raw materials'],
        }, subskill='application', learning_objective_id='lo_identify_challenges_from_scenarios', question_family_id='challenge_identification_from_scenario', concept_id='challenge_extraction', concept_group='scenario_reasoning', scenario_family_id='steyn_three_environment_challenges', retry_variant='core', diagnostic_tags=['scenario_analysis', 'challenge_extraction'], answer_structure_tags=['quote_or_identify', 'three_challenges'], minimum_mastery_score=0.6),
        _with_metadata({
            'title': 'Challenge identification from scenario with cues',
            'prompt': f"Use the case below to identify THREE challenges facing {steyn_case['business_name']}. Write one challenge linked to employees, one linked to crime or security, and one linked to suppliers. (6 marks)\n\n{steyn_case['business_name']} employees are often late for work and do not want to work together. The business suffered losses due to its storeroom being broken into. Management is also struggling to find a reliable provider for raw materials.",
            'marks': 6,
            'marking_points': [
                'Employees are often late for work and do not want to work together.',
                'The business suffered losses due to its storeroom being broken into.',
                'Management is struggling to find a reliable provider for raw materials.'
            ],
            'sample_answer': 'The employee challenge is that staff are often late for work and do not want to work together. The security challenge is that the storeroom was broken into. The supplier challenge is that management is struggling to find a reliable provider for raw materials.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': [
                {'title': 'What is being asked?', 'text': 'This guided version gives you three evidence lanes.'},
                {'title': 'Reasoning path', 'text': 'Match each lane to the exact sentence in the scenario.'},
                {'title': 'Transfer idea', 'text': 'Guided challenge extraction reduces search load but keeps the same evidence line.'}
            ],
            'answer_part_hints': [
                'Write the employee challenge.',
                'Write the crime or security challenge.',
                'Write the supplier challenge.'
            ],
            'guidelines': ['Keep each response focused on the challenge statement itself.'],
            'teaching_note': 'This guided retry narrows the scenario into three clear evidence categories.',
            'keywords': ['employees', 'crime', 'security', 'supplier', 'raw materials'],
        }, subskill='application', learning_objective_id='lo_identify_challenges_from_scenarios', question_family_id='challenge_identification_from_scenario', concept_id='challenge_extraction', concept_group='scenario_reasoning', scenario_family_id='steyn_three_environment_challenges', retry_variant='guided', diagnostic_tags=['scenario_analysis', 'challenge_extraction'], answer_structure_tags=['guided_identify', 'three_challenges'], minimum_mastery_score=0.6),
        _with_metadata({
            'title': 'Challenge identification from scenario reworded',
            'prompt': f"{steyn_case['business_name']} faces three different problems. Staff are often late and do not work well together, the storeroom was broken into, and management cannot find a reliable raw-material provider. Identify the three challenges shown. (6 marks)",
            'marks': 6,
            'marking_points': [
                'Employees are often late for work and do not want to work together.',
                'The business suffered losses due to its storeroom being broken into.',
                'Management is struggling to find a reliable provider for raw materials.'
            ],
            'sample_answer': 'The scenario shows poor employee conduct and teamwork, losses from crime, and supplier problems in finding a reliable raw-material provider.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': [
                {'title': 'What is being asked?', 'text': 'This is the same extraction task with simpler wording.'},
                {'title': 'Reasoning path', 'text': 'Separate the people problem, the crime problem, and the supply problem.'},
                {'title': 'Transfer idea', 'text': 'The goal is still to identify the evidence before classifying it.'}
            ],
            'answer_part_hints': [
                'State the employee challenge.',
                'State the crime challenge.',
                'State the supplier challenge.'
            ],
            'guidelines': ['Use short challenge phrases rather than long descriptions.'],
            'teaching_note': 'This reworded retry lowers language load while preserving the same challenge set.',
            'keywords': ['teamwork', 'crime', 'supplier', 'raw materials'],
        }, subskill='application', learning_objective_id='lo_identify_challenges_from_scenarios', question_family_id='challenge_identification_from_scenario', concept_id='challenge_extraction', concept_group='scenario_reasoning', scenario_family_id='steyn_three_environment_challenges', retry_variant='reworded', diagnostic_tags=['scenario_analysis', 'challenge_extraction'], answer_structure_tags=['reworded_identify', 'three_challenges'], minimum_mastery_score=0.6),
        _with_metadata({
            'title': 'Challenge identification from scenario transfer',
            'prompt': f"Use the prompts below to identify the three challenges facing {steyn_case['business_name']}. (6 marks)\n\n- One challenge linked to employees\n- One challenge linked to crime or losses\n- One challenge linked to raw materials or suppliers",
            'marks': 6,
            'marking_points': [
                'Employees are often late for work and do not want to work together.',
                'The business suffered losses due to its storeroom being broken into.',
                'Management is struggling to find a reliable provider for raw materials.'
            ],
            'sample_answer': 'The employee challenge is lateness and poor teamwork. The crime challenge is losses caused by a storeroom break-in. The supplier challenge is struggling to find a reliable provider for raw materials.',
            'difficulties': ['easy', 'medium', 'hard'],
            'hint_sections': [
                {'title': 'What is being asked?', 'text': 'This transfer version turns the same task into three direct prompts.'},
                {'title': 'Reasoning path', 'text': 'Give one clear challenge for each prompt.'},
                {'title': 'Transfer idea', 'text': 'Well-structured prompts can help you retrieve the same evidence more easily.'}
            ],
            'answer_part_hints': [
                'Write one employee challenge.',
                'Write one crime or losses challenge.',
                'Write one supplier challenge.'
            ],
            'guidelines': ['Answer each bullet with one clear challenge statement.'],
            'teaching_note': 'This transfer retry keeps the same evidence while lowering scenario-processing demand.',
            'keywords': ['employees', 'crime', 'losses', 'supplier'],
        }, subskill='application', learning_objective_id='lo_identify_challenges_from_scenarios', question_family_id='challenge_identification_from_scenario', concept_id='challenge_extraction', concept_group='scenario_reasoning', scenario_family_id='steyn_three_environment_challenges', retry_variant='transfer', diagnostic_tags=['scenario_analysis', 'challenge_extraction'], answer_structure_tags=['transfer_identify', 'three_challenges'], minimum_mastery_score=0.6),
        _with_metadata({
            'title': 'Classify challenges from scenario',
            'prompt': f"Classify EACH challenge in the scenario below according to the micro, market and macro environments. (6 marks)\n\n{steyn_case['business_name']} employees are often late for work and do not want to work together. The business suffered losses due to its storeroom being broken into. Management is also struggling to find a reliable provider for raw materials.",
            'marks': 6,
            'marking_points': [
                'Employees are often late for work and do not want to work together: micro environment.',
                'Storeroom break-in and losses due to crime: macro environment as a socio-economic issue.',
                'Struggling to find a reliable provider for raw materials: market environment.'
            ],
            'sample_answer': 'The employee problem belongs to the micro environment. The storeroom break-in belongs to the macro environment because crime is a socio-economic issue. The problem of finding a reliable provider for raw materials belongs to the market environment.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': [
                {'title': 'What is being asked?', 'text': 'You must match each challenge to the correct business environment.'},
                {'title': 'Reasoning path', 'text': 'Employees point to micro, suppliers point to market, and crime or broader socio-economic threats point to macro.'},
                {'title': 'Transfer idea', 'text': 'Classification depends on the source of the challenge, not on how serious the effect is.'}
            ],
            'answer_part_hints': [
                'Classify the employee challenge.',
                'Classify the crime-related challenge.',
                'Classify the supplier challenge.'
            ],
            'guidelines': ['Name both the challenge and its environment.'],
            'teaching_note': 'This item extends the same Steyn case into environment classification.',
            'keywords': ['micro', 'market', 'macro', 'crime', 'suppliers', 'employees'],
        }, subskill='application', learning_objective_id='lo_identify_challenges_from_scenarios', question_family_id='challenge_classification_from_scenario', concept_id='environment_challenge_classification', concept_group='scenario_reasoning', scenario_family_id='steyn_three_environment_challenges', retry_variant='core', diagnostic_tags=['scenario_analysis', 'classification'], answer_structure_tags=['classify', 'challenge_plus_environment'], minimum_mastery_score=0.6),
        _with_metadata({
            'title': 'Classify challenges from scenario with cues',
            'prompt': f"Use the case below to classify the challenges according to the micro, market and macro environments. Include one employee challenge, one crime-related challenge, and one supplier challenge. (6 marks)\n\n{steyn_case['business_name']} employees are often late for work and do not want to work together. The business suffered losses due to its storeroom being broken into. Management is also struggling to find a reliable provider for raw materials.",
            'marks': 6,
            'marking_points': [
                'Employees are often late for work and do not want to work together: micro environment.',
                'Storeroom break-in and losses due to crime: macro environment as a socio-economic issue.',
                'Struggling to find a reliable provider for raw materials: market environment.'
            ],
            'sample_answer': 'The employee challenge is micro. The crime-related challenge is macro because crime is a socio-economic issue. The supplier challenge is market.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': [
                {'title': 'What is being asked?', 'text': 'This guided version gives you three classification lanes.'},
                {'title': 'Reasoning path', 'text': 'Use the source of each problem to decide the correct environment.'},
                {'title': 'Transfer idea', 'text': 'Stakeholder and socio-economic clues often make classification easier.'}
            ],
            'answer_part_hints': [
                'Classify the employee challenge.',
                'Classify the crime challenge.',
                'Classify the supplier challenge.'
            ],
            'guidelines': ['Do not swap market and macro: suppliers are market, crime is macro.'],
            'teaching_note': 'This guided retry supports cleaner classification of the same three challenge types.',
            'keywords': ['micro', 'macro', 'market', 'crime', 'supplier'],
        }, subskill='application', learning_objective_id='lo_identify_challenges_from_scenarios', question_family_id='challenge_classification_from_scenario', concept_id='environment_challenge_classification', concept_group='scenario_reasoning', scenario_family_id='steyn_three_environment_challenges', retry_variant='guided', diagnostic_tags=['scenario_analysis', 'classification'], answer_structure_tags=['guided_classify', 'challenge_plus_environment'], minimum_mastery_score=0.6),
        _with_metadata({
            'title': 'Classify challenges from scenario reworded',
            'prompt': f"A business is dealing with poor employee behaviour, losses from a storeroom break-in, and unreliable access to raw materials. Explain which one belongs to the micro, market and macro environments. Use {steyn_case['business_name']} as the context. (6 marks)",
            'marks': 6,
            'marking_points': [
                'Employees are often late for work and do not want to work together: micro environment.',
                'Storeroom break-in and losses due to crime: macro environment as a socio-economic issue.',
                'Struggling to find a reliable provider for raw materials: market environment.'
            ],
            'sample_answer': 'Poor employee behaviour belongs to the micro environment. Losses from a storeroom break-in belong to the macro environment because crime is a socio-economic issue. Unreliable raw-material supply belongs to the market environment.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': [
                {'title': 'What is being asked?', 'text': 'This reworded version asks for the same classification in a shorter form.'},
                {'title': 'Reasoning path', 'text': 'Employees are internal, suppliers are immediate external, and crime is a wider external issue.'},
                {'title': 'Transfer idea', 'text': 'Reworded prompts change surface wording, not the required reasoning.'}
            ],
            'answer_part_hints': [
                'State the micro challenge.',
                'State the macro challenge.',
                'State the market challenge.'
            ],
            'guidelines': ['Use explanation language such as belongs to ... because ...'],
            'teaching_note': 'This reworded retry simplifies the wording while preserving the same classification line.',
            'keywords': ['employees', 'crime', 'raw materials', 'micro', 'market', 'macro'],
        }, subskill='application', learning_objective_id='lo_identify_challenges_from_scenarios', question_family_id='challenge_classification_from_scenario', concept_id='environment_challenge_classification', concept_group='scenario_reasoning', scenario_family_id='steyn_three_environment_challenges', retry_variant='reworded', diagnostic_tags=['scenario_analysis', 'classification'], answer_structure_tags=['reworded_classify', 'challenge_plus_environment'], minimum_mastery_score=0.6),
        _with_metadata({
            'title': 'Classify challenges from scenario transfer',
            'prompt': f"Use the prompts below to classify the challenges facing {steyn_case['business_name']}. (6 marks)\n\n- Which challenge belongs to the micro environment?\n- Which challenge belongs to the macro environment?\n- Which challenge belongs to the market environment?",
            'marks': 6,
            'marking_points': [
                'Employees are often late for work and do not want to work together: micro environment.',
                'Storeroom break-in and losses due to crime: macro environment as a socio-economic issue.',
                'Struggling to find a reliable provider for raw materials: market environment.'
            ],
            'sample_answer': 'The micro challenge is employees being late and not working together. The macro challenge is the storeroom break-in because crime is a socio-economic issue. The market challenge is finding a reliable provider for raw materials.',
            'difficulties': ['easy', 'medium', 'hard'],
            'hint_sections': [
                {'title': 'What is being asked?', 'text': 'This transfer version breaks the classification task into three direct questions.'},
                {'title': 'Reasoning path', 'text': 'Answer one environment at a time.'},
                {'title': 'Transfer idea', 'text': 'Organised prompts can support the same classification skill.'}
            ],
            'answer_part_hints': [
                'Write the micro challenge.',
                'Write the macro challenge.',
                'Write the market challenge.'
            ],
            'guidelines': ['Keep the challenge and the environment linked in each response.'],
            'teaching_note': 'This transfer retry preserves the same reasoning while reducing prompt complexity.',
            'keywords': ['micro', 'macro', 'market', 'crime', 'supplier'],
        }, subskill='application', learning_objective_id='lo_identify_challenges_from_scenarios', question_family_id='challenge_classification_from_scenario', concept_id='environment_challenge_classification', concept_group='scenario_reasoning', scenario_family_id='steyn_three_environment_challenges', retry_variant='transfer', diagnostic_tags=['scenario_analysis', 'classification'], answer_structure_tags=['transfer_classify', 'challenge_plus_environment'], minimum_mastery_score=0.6),
        _with_metadata({
            'title': 'Overcoming competition in the market',
            'prompt': f"Recommend ways in which {competition_case['business_name']} can overcome competition in the market. (6 marks)",
            'marks': 6,
            'marking_points': [
                'The business can produce unique or differentiated goods or services.',
                'The business can provide more personalised service and respond quickly to customer needs.',
                'The business can price goods or services competitively where appropriate.',
                'The business can improve quality and customer service.',
                'The business can undertake strong marketing campaigns and create a positive image.',
                'The business can offer low-cost extras such as loyalty schemes, better credit terms, or improved service value.'
            ],
            'sample_answer': f"{competition_case['business_name']} can overcome competition by offering differentiated products, improving quality and customer service, running strong marketing campaigns, and providing value through loyalty schemes or competitive pricing. The business should respond quickly to customer needs so that it stands out from rivals.",
            'difficulties': ['medium', 'hard'],
            'hint_sections': [
                {'title': 'What is being asked?', 'text': 'You must recommend practical ways for a business to respond to competitors.'},
                {'title': 'Reasoning path', 'text': 'Think about product difference, service, pricing, marketing, and customer retention.'},
                {'title': 'Transfer idea', 'text': 'Competition responses should make the business more attractive or more valuable to customers.'}
            ],
            'answer_part_hints': [
                'Recommend one differentiation or quality action.',
                'Recommend one service or pricing action.',
                'Recommend one marketing or customer-loyalty action.'
            ],
            'guidelines': ['Use practical action verbs such as improve, differentiate, price, market, and offer.'],
            'teaching_note': 'This family is based on the curriculum list of ways businesses can overcome competition in the market.',
            'keywords': ['differentiate', 'customer service', 'quality', 'pricing', 'marketing', 'loyalty schemes'],
        }, subskill='application', learning_objective_id='lo_overcome_competition_in_market_environment', question_family_id='competition_overcome_recommendations', concept_id='competition_response_strategies', concept_group='adaptation_and_response', scenario_family_id='competition_response_advice', retry_variant='core', diagnostic_tags=['recommendation', 'competition'], answer_structure_tags=['recommend', 'strategy'], minimum_mastery_score=0.6),
        _with_metadata({
            'title': 'Overcoming competition in the market with cues',
            'prompt': f"Recommend ways in which {competition_case['business_name']} can overcome competition in the market. Include one product or quality action, one customer-service or pricing action, and one marketing or loyalty action. (6 marks)",
            'marks': 6,
            'marking_points': [
                'The business can produce unique or differentiated goods or services.',
                'The business can provide more personalised service and respond quickly to customer needs.',
                'The business can price goods or services competitively where appropriate.',
                'The business can improve quality and customer service.',
                'The business can undertake strong marketing campaigns and create a positive image.',
                'The business can offer low-cost extras such as loyalty schemes, better credit terms, or improved service value.'
            ],
            'sample_answer': f"{competition_case['business_name']} can overcome competition by differentiating its products and improving quality. It can strengthen customer service or use competitive pricing. It can also run stronger marketing campaigns and offer loyalty benefits to keep customers.",
            'difficulties': ['medium', 'hard'],
            'hint_sections': [
                {'title': 'What is being asked?', 'text': 'This guided version groups competition responses into three useful categories.'},
                {'title': 'Reasoning path', 'text': 'Give at least one practical action in each category.'},
                {'title': 'Transfer idea', 'text': 'Balanced competition responses usually combine product, service, and marketing actions.'}
            ],
            'answer_part_hints': [
                'Recommend one product or quality action.',
                'Recommend one customer-service or pricing action.',
                'Recommend one marketing or loyalty action.'
            ],
            'guidelines': ['Organise the answer by category so the recommendation line is balanced.'],
            'teaching_note': 'This guided retry structures the same competition-response memo more explicitly.',
            'keywords': ['differentiation', 'quality', 'customer service', 'pricing', 'marketing', 'loyalty'],
        }, subskill='application', learning_objective_id='lo_overcome_competition_in_market_environment', question_family_id='competition_overcome_recommendations', concept_id='competition_response_strategies', concept_group='adaptation_and_response', scenario_family_id='competition_response_advice', retry_variant='guided', diagnostic_tags=['recommendation', 'competition'], answer_structure_tags=['guided_recommend', 'strategy'], minimum_mastery_score=0.6),
        _with_metadata({
            'title': 'Overcoming competition in the market reworded',
            'prompt': f"Explain how {competition_case['business_name']} can remain competitive when other businesses offer similar goods or services. (6 marks)",
            'marks': 6,
            'marking_points': [
                'The business can produce unique or differentiated goods or services.',
                'The business can provide more personalised service and respond quickly to customer needs.',
                'The business can price goods or services competitively where appropriate.',
                'The business can improve quality and customer service.',
                'The business can undertake strong marketing campaigns and create a positive image.',
                'The business can offer low-cost extras such as loyalty schemes, better credit terms, or improved service value.'
            ],
            'sample_answer': f"{competition_case['business_name']} can remain competitive by differentiating what it sells, improving quality and service, and using strong marketing. It can also respond better to customer needs and offer extra value through pricing or loyalty benefits.",
            'difficulties': ['medium', 'hard'],
            'hint_sections': [
                {'title': 'What is being asked?', 'text': 'This reworded version asks for the same response using a competitiveness frame.'},
                {'title': 'Reasoning path', 'text': 'Show how each action helps the business stand out or keep customers.'},
                {'title': 'Transfer idea', 'text': 'Remaining competitive usually requires value, quality, service, and visibility.'}
            ],
            'answer_part_hints': [
                'Explain one product or quality action.',
                'Explain one service or pricing action.',
                'Explain one marketing or loyalty action.'
            ],
            'guidelines': ['Use explanation language such as this helps the business to ...'],
            'teaching_note': 'This reworded retry keeps the same strategy line but changes the framing.',
            'keywords': ['competitive', 'differentiate', 'quality', 'service', 'marketing'],
        }, subskill='application', learning_objective_id='lo_overcome_competition_in_market_environment', question_family_id='competition_overcome_recommendations', concept_id='competition_response_strategies', concept_group='adaptation_and_response', scenario_family_id='competition_response_advice', retry_variant='reworded', diagnostic_tags=['recommendation', 'competition'], answer_structure_tags=['reworded_recommend', 'strategy'], minimum_mastery_score=0.6),
        _with_metadata({
            'title': 'Overcoming competition in the market transfer',
            'prompt': f"Use the prompts below to recommend how {competition_case['business_name']} can overcome competition. (6 marks)\n\n- One action linked to products or quality\n- One action linked to service or pricing\n- One action linked to marketing or customer loyalty",
            'marks': 6,
            'marking_points': [
                'The business can produce unique or differentiated goods or services.',
                'The business can provide more personalised service and respond quickly to customer needs.',
                'The business can price goods or services competitively where appropriate.',
                'The business can improve quality and customer service.',
                'The business can undertake strong marketing campaigns and create a positive image.',
                'The business can offer low-cost extras such as loyalty schemes, better credit terms, or improved service value.'
            ],
            'sample_answer': f"{competition_case['business_name']} can improve products and quality, strengthen service or pricing, and use marketing or loyalty schemes to keep customers and stand out from competitors.",
            'difficulties': ['easy', 'medium', 'hard'],
            'hint_sections': [
                {'title': 'What is being asked?', 'text': 'This transfer version breaks the same recommendation task into three prompts.'},
                {'title': 'Reasoning path', 'text': 'Give one clear action for each prompt.'},
                {'title': 'Transfer idea', 'text': 'The same competition strategy line can be organised in a simpler structure.'}
            ],
            'answer_part_hints': [
                'Write one product or quality action.',
                'Write one service or pricing action.',
                'Write one marketing or loyalty action.'
            ],
            'guidelines': ['Keep each answer practical and linked to the prompt category.'],
            'teaching_note': 'This transfer retry preserves the strategy line while reducing prompt complexity.',
            'keywords': ['quality', 'pricing', 'marketing', 'loyalty', 'differentiate'],
        }, subskill='application', learning_objective_id='lo_overcome_competition_in_market_environment', question_family_id='competition_overcome_recommendations', concept_id='competition_response_strategies', concept_group='adaptation_and_response', scenario_family_id='competition_response_advice', retry_variant='transfer', diagnostic_tags=['recommendation', 'competition'], answer_structure_tags=['transfer_recommend', 'strategy'], minimum_mastery_score=0.6),
        _with_metadata({
            'title': 'Identify macro-environment challenges with motivation',
            'prompt': f"Read the scenario below and identify TWO challenges of the macro environment. Motivate each answer by quoting from the scenario. (6 marks)\n\n{maureen_case['business_name']} has five employees on its payroll. One employee reported the business to the CCMA for failing to comply with the Basic Conditions of Employment Act. Another employee takes regular leave to collect ARV treatment from the local clinic.",
            'marks': 6,
            'marking_points': [
                'Challenge: contemporary legislation or labour restrictions. Motivation: failing to comply with the Basic Conditions of Employment Act.',
                'Challenge: socio-economic issues such as HIV/AIDS. Motivation: an employee takes regular leave to collect ARV treatment from the local clinic.'
            ],
            'sample_answer': 'One macro challenge is contemporary legislation or labour restrictions, as shown by the failure to comply with the Basic Conditions of Employment Act. Another macro challenge is a socio-economic issue such as HIV/AIDS, as shown by the employee taking regular leave to collect ARV treatment.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': [
                {'title': 'What is being asked?', 'text': 'Identify the macro challenges and support each one with a quote from the scenario.'},
                {'title': 'Reasoning path', 'text': 'Look for one law-related challenge and one broader social-health challenge.'},
                {'title': 'Transfer idea', 'text': 'Motivation questions require both the correct challenge and the evidence phrase.'}
            ],
            'answer_part_hints': [
                'Name the first macro challenge and quote the supporting phrase.',
                'Name the second macro challenge and quote the supporting phrase.'
            ],
            'guidelines': ['Keep the motivation close to the wording used in the scenario.'],
            'teaching_note': 'This item is drawn from the Maureen B&B Lodge macro-environment activity in the notes.',
            'keywords': ['Basic Conditions of Employment Act', 'CCMA', 'ARV', 'socio-economic issues', 'legislation'],
        }, subskill='application', learning_objective_id='lo_challenges_of_macro_environment', question_family_id='macro_challenge_identification_with_motivation', concept_id='macro_environment_challenges', concept_group='scenario_reasoning', scenario_family_id='maureen_lodge_macro_case', retry_variant='core', diagnostic_tags=['scenario_analysis', 'macro_challenges'], answer_structure_tags=['identify', 'motivate_with_quote'], minimum_mastery_score=0.6),
        _with_metadata({
            'title': 'Examples of contemporary legislation',
            'prompt': 'Name any FOUR examples of contemporary legislation that may affect business operations. (4 marks)',
            'marks': 4,
            'marking_points': [
                'Labour Relations Act (LRA).',
                'Basic Conditions of Employment Act (BCEA).',
                'Compensation for Occupational Injuries and Diseases Act (COIDA).',
                'Skills Development Act (SDA).',
                'Consumer Protection Act (CPA).',
                'National Credit Act (NCA).',
                'Employment Equity Act (EEA).',
                'Broad-Based Black Economic Empowerment Act (BBBEE).'
            ],
            'sample_answer': 'Examples include the Labour Relations Act, the Basic Conditions of Employment Act, the Consumer Protection Act, and the National Credit Act.',
            'difficulties': ['easy', 'medium', 'hard'],
            'hint_sections': [
                {'title': 'What is being asked?', 'text': 'List four laws that can affect business operations.'},
                {'title': 'Reasoning path', 'text': 'Think of labour, employment, credit, consumer, compensation, and empowerment laws.'},
                {'title': 'Transfer idea', 'text': 'Acts affecting labour, consumers, credit, and equity often appear in this topic.'}
            ],
            'answer_part_hints': [
                'Write four different Acts.',
                'Do not repeat the same Act in different wording.'
            ],
            'guidelines': ['Any four correct examples earn marks; you do not need to explain them unless asked.'],
            'teaching_note': 'This item supports recall of the legislation examples listed in the curriculum notes.',
            'keywords': ['LRA', 'BCEA', 'COIDA', 'SDA', 'CPA', 'NCA', 'EEA', 'BBBEE'],
        }, subskill='application', learning_objective_id='lo_examples_of_contemporary_legislation', question_family_id='contemporary_legislation_listing', concept_id='contemporary_legislation_examples', concept_group='macro_challenges', retry_variant='core', diagnostic_tags=['recall', 'legislation'], answer_structure_tags=['list_examples'], minimum_mastery_score=0.6),
    ]


def _discussion_pool():
    return [
        _with_metadata({
            'title': 'Discuss market-environment challenges',
            'prompt': 'Discuss the following challenges of the market environment: shortage of suppliers, changes in consumer behaviour, and demographics or psychographics. (12 marks)',
            'marks': 12,
            'marking_points': [
                'Shortage of suppliers can disrupt raw-material supply, reduce productivity, and lower profitability.',
                'Late, poor-quality, or expensive supplies can cause missed sales targets and loss of customers.',
                'Changes in consumer behaviour can reduce sales when tastes and preferences shift.',
                'Businesses may need to adapt products, services, or marketing to meet changing customer needs.',
                'Demographic changes affect the types of goods or services that consumers need.',
                'Psychographic changes affect customer attitudes, lifestyles, interests, and buying behaviour.'
            ],
            'sample_answer': 'A shortage of suppliers can disrupt access to raw materials and reduce productivity and profit. Changes in consumer behaviour can reduce sales when tastes and preferences shift, so businesses need to adapt products and marketing. Changes in demographics and psychographics also challenge businesses because age, income, lifestyle, and attitudes influence what consumers buy and how businesses should market to them.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': [
                {'title': 'What is being asked?', 'text': 'Discuss three different market challenges and show how each affects the business.'},
                {'title': 'Structure hint', 'text': 'Write separate discussion points for suppliers, consumer behaviour, and demographics or psychographics.'},
                {'title': 'Transfer idea', 'text': 'Strong discussion answers explain the effect of each challenge rather than only naming it.'}
            ],
            'answer_part_hints': [
                'Discuss shortage of suppliers.',
                'Discuss changes in consumer behaviour.',
                'Discuss demographics or psychographics.'
            ],
            'guidelines': ['Explain the business effect of each challenge, not only its definition.'],
            'teaching_note': 'This family follows the market-environment challenge discussion pattern in the topic activities.',
            'keywords': ['suppliers', 'consumer behaviour', 'demographics', 'psychographics', 'raw materials', 'sales'],
        }, subskill='discussion', learning_objective_id='lo_challenges_of_market_environment', question_family_id='market_environment_challenges_discussion', concept_id='market_environment_challenges', concept_group='discussion_reasoning', retry_variant='core', diagnostic_tags=['discussion', 'market_challenges'], answer_structure_tags=['discuss', 'multi_point_explanation'], minimum_mastery_score=0.7),
        _with_metadata({
            'title': 'Discuss market-environment challenges with structure cues',
            'prompt': 'Discuss the following market-environment challenges by writing about one supplier-related effect, one customer-behaviour effect, and one demographic or psychographic effect. (12 marks)',
            'marks': 12,
            'marking_points': [
                'Shortage of suppliers can disrupt raw-material supply, reduce productivity, and lower profitability.',
                'Late, poor-quality, or expensive supplies can cause missed sales targets and loss of customers.',
                'Changes in consumer behaviour can reduce sales when tastes and preferences shift.',
                'Businesses may need to adapt products, services, or marketing to meet changing customer needs.',
                'Demographic changes affect the types of goods or services that consumers need.',
                'Psychographic changes affect customer attitudes, lifestyles, interests, and buying behaviour.'
            ],
            'sample_answer': 'Supplier problems can reduce production and profit when raw materials are late or expensive. Changes in consumer behaviour can lower sales if the business does not adapt to new tastes. Demographic and psychographic changes also affect buying behaviour, so businesses must adjust products and marketing to suit the target market.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': [
                {'title': 'What is being asked?', 'text': 'This guided version gives you three discussion buckets.'},
                {'title': 'Structure hint', 'text': 'Use one clear explanation from each bucket so the answer is balanced.'},
                {'title': 'Transfer idea', 'text': 'Balanced discussion answers usually cover supply, demand, and customer-profile shifts.'}
            ],
            'answer_part_hints': [
                'Explain one supplier-related effect.',
                'Explain one consumer-behaviour effect.',
                'Explain one demographic or psychographic effect.'
            ],
            'guidelines': ['Avoid repeating the same sales point in all three sections.'],
            'teaching_note': 'This guided retry organises the same discussion line into three effect categories.',
            'keywords': ['suppliers', 'consumer behaviour', 'demographics', 'psychographics'],
        }, subskill='discussion', learning_objective_id='lo_challenges_of_market_environment', question_family_id='market_environment_challenges_discussion', concept_id='market_environment_challenges', concept_group='discussion_reasoning', retry_variant='guided', diagnostic_tags=['discussion', 'market_challenges'], answer_structure_tags=['guided_discussion', 'multi_point_explanation'], minimum_mastery_score=0.7),
        _with_metadata({
            'title': 'Discuss market-environment challenges reworded',
            'prompt': 'Explain how supplier problems, changing customer behaviour, and changing customer profiles can threaten business success. (12 marks)',
            'marks': 12,
            'marking_points': [
                'Shortage of suppliers can disrupt raw-material supply, reduce productivity, and lower profitability.',
                'Late, poor-quality, or expensive supplies can cause missed sales targets and loss of customers.',
                'Changes in consumer behaviour can reduce sales when tastes and preferences shift.',
                'Businesses may need to adapt products, services, or marketing to meet changing customer needs.',
                'Demographic changes affect the types of goods or services that consumers need.',
                'Psychographic changes affect customer attitudes, lifestyles, interests, and buying behaviour.'
            ],
            'sample_answer': 'Supplier problems can threaten success by disrupting stock and production. Changing customer behaviour can reduce sales if products no longer match customer needs. Changing customer profiles such as age, income, lifestyles, and attitudes also force businesses to adjust what they sell and how they market it.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': [
                {'title': 'What is being asked?', 'text': 'This reworded version frames the same discussion as threats to success.'},
                {'title': 'Structure hint', 'text': 'Link each challenge to its effect on sales, production, or customer fit.'},
                {'title': 'Transfer idea', 'text': 'The best responses move from the challenge to the business consequence.'}
            ],
            'answer_part_hints': [
                'Explain one supplier threat.',
                'Explain one customer-behaviour threat.',
                'Explain one demographic or psychographic threat.'
            ],
            'guidelines': ['Keep explaining how the challenge affects the business, not only what the challenge is.'],
            'teaching_note': 'This reworded retry keeps the same market-challenge memo line but simplifies the wording.',
            'keywords': ['supplier problems', 'customer behaviour', 'demographics', 'psychographics'],
        }, subskill='discussion', learning_objective_id='lo_challenges_of_market_environment', question_family_id='market_environment_challenges_discussion', concept_id='market_environment_challenges', concept_group='discussion_reasoning', retry_variant='reworded', diagnostic_tags=['discussion', 'market_challenges'], answer_structure_tags=['reworded_discussion', 'multi_point_explanation'], minimum_mastery_score=0.7),
        _with_metadata({
            'title': 'Explain macro-environment challenges',
            'prompt': 'Explain FOUR challenges of the macro environment. (12 marks)',
            'marks': 12,
            'marking_points': [
                'Changes in income levels reduce consumer spending and lower business profits.',
                'Political changes can create instability and force businesses to adapt to new laws and policies.',
                'Contemporary legislation creates compliance demands and penalties for non-compliance.',
                'Labour restrictions can make employers feel limited by legal protections for employees.',
                'Micro-lending can expose borrowers to high interest and limited protection.',
                'Globalisation increases international competition and can contribute to dumping or skills migration.',
                'Social values and demographics affect buying habits and the products consumers prefer.',
                'Socio-economic issues such as crime, poverty, HIV/AIDS, and corruption increase costs and reduce productivity.'
            ],
            'sample_answer': 'Macro-environment challenges include changes in income levels, which reduce consumer spending and profits; political changes, which can create instability; contemporary legislation and labour restrictions, which create compliance pressure; and socio-economic issues such as crime or HIV/AIDS, which increase costs and weaken the labour force. Globalisation and demographic change can also create new competitive and market pressures.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': [
                {'title': 'What is being asked?', 'text': 'Select any four macro challenges and explain how they affect businesses.'},
                {'title': 'Structure hint', 'text': 'Write separate explanation points for each chosen challenge.'},
                {'title': 'Transfer idea', 'text': 'Macro challenges usually come from broad political, economic, legal, social, or global forces.'}
            ],
            'answer_part_hints': [
                'Explain the first macro challenge.',
                'Explain the second macro challenge.',
                'Explain the third macro challenge.',
                'Explain the fourth macro challenge.'
            ],
            'guidelines': ['Choose distinct macro challenges rather than repeating the same idea with different wording.'],
            'teaching_note': 'This family supports the macro-challenge discussion objective from the topic notes.',
            'keywords': ['income levels', 'political changes', 'legislation', 'labour restrictions', 'globalisation', 'socio-economic issues'],
        }, subskill='discussion', learning_objective_id='lo_challenges_of_macro_environment', question_family_id='macro_environment_challenges_discussion', concept_id='macro_environment_challenges', concept_group='discussion_reasoning', retry_variant='core', diagnostic_tags=['discussion', 'macro_challenges'], answer_structure_tags=['explain', 'multi_point_explanation'], minimum_mastery_score=0.7),
        _with_metadata({
            'title': 'Explain macro-environment challenges with cues',
            'prompt': 'Explain FOUR challenges of the macro environment. Include one economic challenge, one political or legal challenge, one labour or regulation challenge, and one social or global challenge. (12 marks)',
            'marks': 12,
            'marking_points': [
                'Changes in income levels reduce consumer spending and lower business profits.',
                'Political changes can create instability and force businesses to adapt to new laws and policies.',
                'Contemporary legislation creates compliance demands and penalties for non-compliance.',
                'Labour restrictions can make employers feel limited by legal protections for employees.',
                'Micro-lending can expose borrowers to high interest and limited protection.',
                'Globalisation increases international competition and can contribute to dumping or skills migration.',
                'Social values and demographics affect buying habits and the products consumers prefer.',
                'Socio-economic issues such as crime, poverty, HIV/AIDS, and corruption increase costs and reduce productivity.'
            ],
            'sample_answer': 'An economic challenge is reduced income levels, which lower consumer spending. A political or legal challenge is political change or new legislation, which forces businesses to adapt. A labour or regulation challenge is labour restrictions that limit employer practices. A social or global challenge is crime, HIV/AIDS, or global competition, which increase costs and pressure on businesses.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': [
                {'title': 'What is being asked?', 'text': 'This guided version groups macro challenges into four categories.'},
                {'title': 'Structure hint', 'text': 'Choose one challenge from each category to avoid repetition.'},
                {'title': 'Transfer idea', 'text': 'Macro discussion is often easier when organised by broad force types.'}
            ],
            'answer_part_hints': [
                'Explain one economic challenge.',
                'Explain one political or legal challenge.',
                'Explain one labour or regulation challenge.',
                'Explain one social or global challenge.'
            ],
            'guidelines': ['Use the category cues to keep the answer broad and balanced.'],
            'teaching_note': 'This guided retry structures macro challenges by broad force type.',
            'keywords': ['economic', 'political', 'legal', 'labour', 'social', 'global'],
        }, subskill='discussion', learning_objective_id='lo_challenges_of_macro_environment', question_family_id='macro_environment_challenges_discussion', concept_id='macro_environment_challenges', concept_group='discussion_reasoning', retry_variant='guided', diagnostic_tags=['discussion', 'macro_challenges'], answer_structure_tags=['guided_discussion', 'multi_point_explanation'], minimum_mastery_score=0.7),
        _with_metadata({
            'title': 'Explain macro-environment challenges reworded',
            'prompt': 'Why do broad external forces such as income levels, legislation, crime, and globalisation create serious problems for businesses? Explain briefly. (12 marks)',
            'marks': 12,
            'marking_points': [
                'Changes in income levels reduce consumer spending and lower business profits.',
                'Political changes can create instability and force businesses to adapt to new laws and policies.',
                'Contemporary legislation creates compliance demands and penalties for non-compliance.',
                'Labour restrictions can make employers feel limited by legal protections for employees.',
                'Micro-lending can expose borrowers to high interest and limited protection.',
                'Globalisation increases international competition and can contribute to dumping or skills migration.',
                'Social values and demographics affect buying habits and the products consumers prefer.',
                'Socio-economic issues such as crime, poverty, HIV/AIDS, and corruption increase costs and reduce productivity.'
            ],
            'sample_answer': 'Broad external forces create serious problems because businesses cannot control them directly. Lower income levels reduce consumer spending, legislation creates compliance pressure, crime raises costs and losses, and globalisation increases competition. These forces can reduce profits, productivity, and long-term stability.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': [
                {'title': 'What is being asked?', 'text': 'This reworded version asks for the same explanation using a broad external-forces frame.'},
                {'title': 'Structure hint', 'text': 'Explain what each force does to costs, demand, compliance, or competition.'},
                {'title': 'Transfer idea', 'text': 'Macro challenges matter because they affect business performance while remaining outside direct control.'}
            ],
            'answer_part_hints': [
                'Explain one demand or income problem.',
                'Explain one legal or political problem.',
                'Explain one crime, health, or global competition problem.',
                'Link the explanation to business performance.'
            ],
            'guidelines': ['Keep linking each force to its business effect.'],
            'teaching_note': 'This reworded retry preserves the same macro-challenge memo while reducing prompt formality.',
            'keywords': ['income levels', 'legislation', 'crime', 'globalisation', 'profits', 'competition'],
        }, subskill='discussion', learning_objective_id='lo_challenges_of_macro_environment', question_family_id='macro_environment_challenges_discussion', concept_id='macro_environment_challenges', concept_group='discussion_reasoning', retry_variant='reworded', diagnostic_tags=['discussion', 'macro_challenges'], answer_structure_tags=['reworded_discussion', 'multi_point_explanation'], minimum_mastery_score=0.7),
    ]


def _build_temba_context():
    return {
        'business_name': 'Temba Stores',
        'statement_1': 'Pieter, the cleaner, always complains about working hours and produces sub-standard work.',
        'statement_2': 'Management does not have a clear plan of where the business is going.',
        'statement_3': 'The sales team fails to meet its targets because of a lack of leadership.',
        'statement_4': 'Employees are demanding improved working conditions and are refusing to work until their demands are met.',
    }


def _build_steyn_context():
    return {
        'business_name': 'Steyn Manufacturers',
    }


def _build_maureen_context():
    return {
        'business_name': 'Maureen B&B Lodge',
    }


def _build_competition_context(rng):
    return {
        'business_name': _pick_business_name(r=rng, suffixes=RETAIL_AND_LIFESTYLE_SUFFIXES or MANUFACTURING_SUFFIXES),
    }


def generate(subskill='concepts', difficulty='medium', count=1, seed=None, **kwargs):
    rng = _rng(seed)
    concepts = _apply_metadata_filters(_concept_pool(), **kwargs)
    application = _apply_metadata_filters(_application_pool(rng), **kwargs)
    discussion = _apply_metadata_filters(_discussion_pool(), **kwargs)

    if subskill == 'application':
        return [_typed_question(rng, item) for item in _select_items(rng, application, count, difficulty)]
    if subskill == 'discussion':
        return [_typed_question(rng, item) for item in _select_items(rng, discussion, count, difficulty)]
    if subskill == 'mixed':
        mixed_pool = [('mcq', item) for item in concepts] + [('typed', item) for item in application] + [('typed', item) for item in discussion]
        selected = _select_items(rng, mixed_pool, count, difficulty)
        questions = []
        for kind, item in selected:
            questions.append(_mcq_question(rng, item) if kind == 'mcq' else _typed_question(rng, item))
        return questions
    return [_mcq_question(rng, item) for item in _select_items(rng, concepts, count, difficulty)]
